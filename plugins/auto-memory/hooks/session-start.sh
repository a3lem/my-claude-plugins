#!/bin/sh
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
mem_dir=$("$SCRIPT_DIR/../skills/auto-memory/scripts/resolve-memory-dir.sh")
echo "IMPORTANT: For auto memory, use the auto-memory skill (/auto-memory). Memory directory: $mem_dir"
