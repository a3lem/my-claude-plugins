# talk-to-me-mcp

MCP server enabling Claude Code to speak to users via TTS when input is needed.

## Overview

This plugin provides a `speak-to-user-for-input` MCP tool that Claude can use to audibly notify you when it needs input to continue. The tool uses pocket-tts for text-to-speech generation.

## Setup

1. Start the MCP server in a separate terminal:

```bash
cd plugins/talk-to-me-mcp
uv run talk-to-me-server
```

The server runs on `http://127.0.0.1:8347` by default.

2. Enable the feature in your Claude Code session:

```
/talk-to-me
```

Or let Claude call the `enable_talk_to_me` tool.

## Configuration

Environment variables:
- `TALK_TO_ME_PORT` - Server port (default: 8347)
- `TALK_TO_ME_HOST` - Server host (default: 127.0.0.1)
- `TALK_TO_ME_VOICE` - Voice to use (default: azelma)

Available voices: alba, marius, javert, jean, fantine, cosette, eponine, azelma

## Tools

| Tool | Description |
|------|-------------|
| `speak_to_user_for_input` | Speak to user when input is needed (requires enabled state) |
| `enable_talk_to_me` | Enable spoken notifications |
| `disable_talk_to_me` | Disable spoken notifications |
| `check_talk_to_me_status` | Check if feature is enabled |

## How It Works

1. User starts the MCP server (`uv run talk-to-me-server`)
2. User enables the feature via `/talk-to-me` or the `enable_talk_to_me` tool
3. When Claude is blocked waiting for input, it calls `speak_to_user_for_input`
4. The tool generates TTS audio and plays it through your speakers

The enabled state is stored in `~/.local/state/talk-to-me-mcp/enabled`.

## Requirements

- Python 3.12+
- pocket-tts
- macOS (uses `afplay` for audio playback) or Linux (uses `aplay`)
