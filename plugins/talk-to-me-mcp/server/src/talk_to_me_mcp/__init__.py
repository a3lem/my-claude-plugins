"""
HTTP MCP server for text-to-speech notifications to the user.

Start with: uvx --from <path> talk-to-me-server
"""

from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import typing as T
from pathlib import Path

from fastmcp import FastMCP
from loguru import logger

if T.TYPE_CHECKING:
    from pocket_tts import TTSModel

# State file location - shared between plugin command and MCP server
STATE_DIR = Path(os.environ.get("XDG_STATE_HOME", Path.home() / ".local" / "state"))
ENABLED_FLAG_FILE = STATE_DIR / "talk-to-me-mcp" / "enabled"

# Voice to use for TTS
VOICE = os.environ.get("TALK_TO_ME_VOICE", "azelma")

# Global TTS model state (loaded lazily on first use)
_tts_model: TTSModel | None = None
_voice_state: T.Any | None = None  # Voice state type is opaque


def _load_tts_model() -> tuple[TTSModel, T.Any]:
    """Load the TTS model and voice state. Cached after first call."""
    global _tts_model, _voice_state

    if _tts_model is not None and _voice_state is not None:
        return _tts_model, _voice_state

    from pocket_tts import TTSModel

    logger.info("Loading TTS model with voice '{}'...", VOICE)
    _tts_model = TTSModel.load_model()
    _voice_state = _tts_model.get_state_for_audio_prompt(VOICE)
    logger.info("TTS model loaded")

    return _tts_model, _voice_state


def _play_audio_file(path: str) -> None:
    """Play an audio file using platform-appropriate player."""
    logger.debug("Playing audio file: {}", path)
    if sys.platform == "darwin":
        subprocess.run(["afplay", path], check=True)
    elif sys.platform == "linux":
        subprocess.run(["aplay", path], check=True)
    else:
        # Windows
        import winsound  # type: ignore[import-not-found]
        winsound.PlaySound(path, winsound.SND_FILENAME)


def speak_text(text: str) -> None:
    """Generate and play TTS audio using pocket-tts with the azelma voice."""
    logger.debug("Generating TTS for text: {}", text[:50] + "..." if len(text) > 50 else text)
    try:
        import scipy.io.wavfile
        tts_model, voice_state = _load_tts_model()
    except ImportError as e:
        # Fallback to macOS say command if dependencies not available
        logger.warning("pocket-tts not available ({}), falling back to 'say' command", e)
        subprocess.run(["say", text], check=True)
        return

    # Generate audio
    audio = tts_model.generate_audio(voice_state, text)

    # Write to temp file and play
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        output_path = f.name

    try:
        scipy.io.wavfile.write(output_path, tts_model.sample_rate, audio.numpy())
        _play_audio_file(output_path)
    finally:
        Path(output_path).unlink(missing_ok=True)


mcp = FastMCP(
    name="talk-to-me",
    instructions="""
    This server provides text-to-speech capabilities for notifying users when input is needed.

    IMPORTANT: The speak-to-user-for-input tool should ONLY be called when:
    1. The user has enabled the feature by typing 'talk to me' or using /talk-to-me
    2. You (the agent) are blocked waiting for user input to continue

    Use this tool sparingly - only when you genuinely need user input to proceed.
    """,
)


def is_enabled() -> bool:
    """Check if the talk-to-me feature is enabled."""
    return ENABLED_FLAG_FILE.exists()


def enable() -> None:
    """Enable the talk-to-me feature."""
    ENABLED_FLAG_FILE.parent.mkdir(parents=True, exist_ok=True)
    ENABLED_FLAG_FILE.touch()


def disable() -> None:
    """Disable the talk-to-me feature."""
    if ENABLED_FLAG_FILE.exists():
        ENABLED_FLAG_FILE.unlink()


@mcp.tool()
def speak_to_user_for_input(
    summary: str,
    agent_id: str,
) -> str:
    """
    Speak to the user via TTS when input is needed to continue.

    This tool generates spoken audio to notify the user that the agent needs input.
    Only use this when you are blocked and cannot proceed without user input.

    Args:
        summary: A concise summary (1-2 sentences) of the current state or what
                 input is needed. Keep it brief - this will be spoken aloud.
        agent_id: A short identifier for context - e.g., the project name,
                  current task, or session purpose. Should be intelligible to
                  a human hearing it spoken.

    Returns:
        Status message indicating whether the notification was sent.
    """
    logger.info("speak_to_user_for_input called | agent_id={} summary={}", agent_id, summary[:50])

    if not is_enabled():
        logger.warning("Tool called but feature is not enabled")
        return (
            "Talk-to-me feature is not enabled. "
            "The user must first type 'talk to me' or use /talk-to-me to enable it."
        )

    # Construct the spoken message
    message = f"{agent_id}. {summary}"

    try:
        speak_text(message)
        logger.info("Successfully spoke to user")
        return f"Spoke to user: {message}"
    except Exception as e:
        logger.exception("Failed to speak")
        return f"Failed to speak: {e}"


@mcp.tool()
def enable_talk_to_me() -> str:
    """
    Enable the talk-to-me feature.

    This allows the speak_to_user_for_input tool to function.
    The user should invoke this (or use /talk-to-me) to opt-in to spoken notifications.

    Returns:
        Confirmation message.
    """
    logger.info("enable_talk_to_me called")
    enable()
    return "Talk-to-me feature enabled. The agent can now speak to you when input is needed."


@mcp.tool()
def disable_talk_to_me() -> str:
    """
    Disable the talk-to-me feature.

    This prevents the speak_to_user_for_input tool from producing audio.

    Returns:
        Confirmation message.
    """
    logger.info("disable_talk_to_me called")
    disable()
    return "Talk-to-me feature disabled. The agent will no longer speak to you."


@mcp.tool()
def check_talk_to_me_status() -> str:
    """
    Check if the talk-to-me feature is currently enabled.

    Returns:
        Status message indicating enabled/disabled state.
    """
    enabled = is_enabled()
    logger.info("check_talk_to_me_status called | enabled={}", enabled)
    if enabled:
        return "Talk-to-me feature is ENABLED. The agent can speak to you when input is needed."
    return "Talk-to-me feature is DISABLED. Use /talk-to-me or enable_talk_to_me to enable it."


def main() -> None:
    """Run the MCP server."""
    import argparse

    import uvicorn

    parser = argparse.ArgumentParser(description="Talk-to-me MCP server")
    parser.add_argument(
        "--voice",
        default=os.environ.get("TALK_TO_ME_VOICE", "azelma"),
        help="Voice to use for TTS (default: azelma)",
    )
    parser.add_argument("--host", default=os.environ.get("TALK_TO_ME_HOST", "127.0.0.1"))
    parser.add_argument("--port", type=int, default=int(os.environ.get("TALK_TO_ME_PORT", "8347")))
    parser.add_argument(
        "--directory", "-d",
        type=Path,
        help="State directory for enabled flag (default: ~/.local/state/talk-to-me-mcp)",
    )
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    args = parser.parse_args()

    # Configure logging level
    if not args.debug:
        logger.remove()
        logger.add(sys.stderr, level="INFO")

    # Override voice from CLI
    global VOICE
    VOICE = args.voice

    # Override state directory if provided
    if args.directory:
        global ENABLED_FLAG_FILE
        ENABLED_FLAG_FILE = args.directory / "enabled"

    # Pre-load the TTS model for faster first response
    logger.info("Pre-loading TTS model...")
    try:
        _load_tts_model()
    except Exception as e:
        logger.warning("Could not pre-load TTS model: {}", e)
        logger.warning("Will fall back to 'say' command if pocket-tts unavailable")

    logger.info("Starting talk-to-me MCP server on http://{}:{}", args.host, args.port)
    logger.info("State file: {}", ENABLED_FLAG_FILE)
    logger.info("Feature enabled: {}", is_enabled())

    # Run as HTTP server
    uvicorn.run(
        mcp.http_app(),
        host=args.host,
        port=args.port,
        log_level="debug" if args.debug else "info",
    )


if __name__ == "__main__":
    main()
