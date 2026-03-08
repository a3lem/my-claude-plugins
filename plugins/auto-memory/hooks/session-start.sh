#!/usr/bin/env bash

mem_dir=$("${CLAUDE_PLUGIN_ROOT}/skills/auto-memory/scripts/resolve-memory-dir.sh")
echo "IMPORTANT: For auto memory, use the auto-memory skill (/auto-memory). Memory directory: $mem_dir"
