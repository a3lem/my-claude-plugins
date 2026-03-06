#!/usr/bin/env python3
"""Manage AI provenance frontmatter blocks in source files.

Usage:
    frontmatter.py stamp <file> [--reviewed true|false] [--rules p1,p2]
                                [--skills s1,s2] [--access write|read|hidden]
                                [--comment-char CC]
    frontmatter.py scan [--path .] [--ext py,sh,ts,tsx,js,go]
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

# Extension → comment character mapping
COMMENT_CHARS: dict[str, str] = {
    "py": "#", "sh": "#", "bash": "#", "yaml": "#", "yml": "#",
    "toml": "#", "r": "#", "rb": "#", "pl": "#",
    "js": "//", "ts": "//", "tsx": "//", "jsx": "//", "go": "//",
    "rs": "//", "java": "//", "c": "//", "cpp": "//", "h": "//",
    "hpp": "//", "cs": "//", "swift": "//", "kt": "//",
}


def detect_comment_char(filepath: Path) -> str | None:
    """Return the comment character for a file based on its extension."""
    ext = filepath.suffix.lstrip(".")
    return COMMENT_CHARS.get(ext)


def build_block(
    cc: str,
    reviewed: str,
    rules: str | None,
    skills: str | None,
    access: str | None,
) -> str:
    """Build the frontmatter block string."""
    lines = [
        f"{cc} /// ai",
        f"{cc} human_reviewed = {reviewed}",
    ]
    if rules:
        parts = [f'"{r.strip()}"' for r in rules.split(",")]
        lines.append(f"{cc} rules = [{', '.join(parts)}]")
    if skills:
        parts = [f'"{s.strip()}"' for s in skills.split(",")]
        lines.append(f"{cc} skills = [{', '.join(parts)}]")
    # Only emit access when explicitly set and not the default "write"
    if access and access != "write":
        lines.append(f'{cc} access = "{access}"')
    lines.append(f"{cc} ///")
    return "\n".join(lines)


def find_existing_block(lines: list[str], cc: str) -> tuple[int, int] | None:
    """Find the start and end line indices of an existing frontmatter block.

    Returns (start, end) as 0-based inclusive indices, or None.
    """
    open_marker = f"{cc} /// ai"
    close_marker = f"{cc} ///"

    start = None
    for i, line in enumerate(lines):
        if start is None:
            if open_marker in line:
                start = i
        else:
            if line.rstrip() == close_marker:
                return (start, i)
    return None


def find_insert_position(lines: list[str]) -> int:
    """Determine where to insert a new block (after shebang/encoding lines).

    Returns the 0-based index to insert before.
    """
    insert_after = 0
    for i, line in enumerate(lines):
        if i == 0 and line.startswith("#!"):
            insert_after = i + 1
            continue
        if i <= 1 and "coding" in line:
            insert_after = i + 1
            continue
        break
    return insert_after


def do_stamp(args: argparse.Namespace) -> None:
    filepath = Path(args.file)
    if not filepath.is_file():
        print(f"Error: file not found: {filepath}", file=sys.stderr)
        sys.exit(1)

    # Resolve comment character
    cc = args.comment_char
    if not cc:
        cc = detect_comment_char(filepath)
        if not cc:
            ext = filepath.suffix.lstrip(".")
            print(
                f"Error: cannot detect comment char for .{ext} — use --comment-char",
                file=sys.stderr,
            )
            sys.exit(1)

    # Validate inputs
    if args.reviewed not in ("true", "false"):
        print(
            f"Error: --reviewed must be 'true' or 'false', got '{args.reviewed}'",
            file=sys.stderr,
        )
        sys.exit(1)

    if args.access and args.access not in ("write", "read", "hidden"):
        print(
            f"Error: --access must be 'write', 'read', or 'hidden', got '{args.access}'",
            file=sys.stderr,
        )
        sys.exit(1)

    block = build_block(cc, args.reviewed, args.rules, args.skills, args.access)
    content = filepath.read_text()
    lines = content.splitlines()

    existing = find_existing_block(lines, cc)

    if existing:
        start, end = existing
        new_lines = lines[:start] + block.splitlines() + lines[end + 1 :]
    else:
        pos = find_insert_position(lines)
        block_lines = block.splitlines() + [""]
        new_lines = lines[:pos] + block_lines + lines[pos:]

    # Preserve original trailing newline
    result = "\n".join(new_lines)
    if content.endswith("\n"):
        result += "\n"

    filepath.write_text(result)
    print(f"Stamped: {filepath}")


def do_scan(args: argparse.Namespace) -> None:
    scan_path = Path(args.path)
    extensions = [e.strip() for e in args.ext.split(",")]

    # Build git ls-files patterns
    patterns = [f"*.{ext}" for ext in extensions]

    try:
        result = subprocess.run(
            ["git", "ls-files", "--", *patterns],
            cwd=scan_path,
            capture_output=True,
            text=True,
            check=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        result = None

    if not result or not result.stdout.strip():
        print(f"No files found for extensions: {args.ext} in {scan_path}")
        return

    files = result.stdout.strip().splitlines()

    # Per-directory counters
    stats: dict[str, dict[str, int]] = defaultdict(
        lambda: {
            "stamped": 0,
            "reviewed": 0,
            "unreviewed": 0,
            "unstamped": 0,
            "access_read": 0,
            "access_hidden": 0,
        }
    )
    totals = {
        "stamped": 0,
        "reviewed": 0,
        "unreviewed": 0,
        "unstamped": 0,
        "access_read": 0,
        "access_hidden": 0,
    }

    for rel_file in files:
        filepath = scan_path / rel_file
        directory = str(Path(rel_file).parent)

        cc = detect_comment_char(filepath)
        if not cc:
            continue

        try:
            content = filepath.read_text()
        except OSError:
            continue

        open_marker = f"{cc} /// ai"

        if open_marker in content:
            stats[directory]["stamped"] += 1
            totals["stamped"] += 1

            if f"{cc} human_reviewed = true" in content:
                stats[directory]["reviewed"] += 1
                totals["reviewed"] += 1
            else:
                stats[directory]["unreviewed"] += 1
                totals["unreviewed"] += 1

            if f'{cc} access = "hidden"' in content:
                stats[directory]["access_hidden"] += 1
                totals["access_hidden"] += 1
            elif f'{cc} access = "read"' in content:
                stats[directory]["access_read"] += 1
                totals["access_read"] += 1
        else:
            stats[directory]["unstamped"] += 1
            totals["unstamped"] += 1

    # Print per-directory summary
    print(f"=== AI Frontmatter Scan: {scan_path} ===")
    print()

    for directory in sorted(stats):
        d = stats[directory]
        line = (
            f"  {directory}/: {d['stamped']} stamped "
            f"({d['reviewed']} reviewed, {d['unreviewed']} unreviewed), "
            f"{d['unstamped']} unstamped"
        )
        if d["access_read"] > 0 or d["access_hidden"] > 0:
            line += f" | access: {d['access_read']} read-only, {d['access_hidden']} hidden"
        print(line)

    print()
    total_line = (
        f"  TOTAL: {totals['stamped']} stamped "
        f"({totals['reviewed']} reviewed, {totals['unreviewed']} unreviewed), "
        f"{totals['unstamped']} unstamped"
    )
    if totals["access_read"] > 0 or totals["access_hidden"] > 0:
        total_line += (
            f" | access: {totals['access_read']} read-only, "
            f"{totals['access_hidden']} hidden"
        )
    print(total_line)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Manage AI provenance frontmatter blocks in source files."
    )
    subparsers = parser.add_subparsers(dest="command")

    # stamp subcommand
    stamp_parser = subparsers.add_parser("stamp", help="Add or update a frontmatter block")
    stamp_parser.add_argument("file", help="File to stamp")
    stamp_parser.add_argument("--reviewed", default="false", help="Review status (true/false)")
    stamp_parser.add_argument("--rules", default=None, help="Comma-separated rule paths")
    stamp_parser.add_argument("--skills", default=None, help="Comma-separated skill names agents must load")
    stamp_parser.add_argument("--access", default=None, help="Access mode (write/read/hidden)")
    stamp_parser.add_argument("--comment-char", default=None, help="Override comment character")

    # scan subcommand
    scan_parser = subparsers.add_parser("scan", help="Report frontmatter coverage")
    scan_parser.add_argument("--path", default=".", help="Directory to scan")
    scan_parser.add_argument("--ext", default="py,sh,ts,tsx,js,go", help="Comma-separated extensions")

    args = parser.parse_args()

    if args.command == "stamp":
        do_stamp(args)
    elif args.command == "scan":
        do_scan(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
