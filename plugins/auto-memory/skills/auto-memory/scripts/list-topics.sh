#!/bin/sh
# List topic files (everything except MEMORY.md) in the memory directory.
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
mem_dir=$("$SCRIPT_DIR/resolve-memory-dir.sh")

if [ -d "$mem_dir" ]; then
  files=$(find "$mem_dir" -name '*.md' ! -name 'MEMORY.md' -exec basename {} \; 2>/dev/null)
  if [ -n "$files" ]; then
    echo "$files"
  else
    echo "(none yet)"
  fi
else
  echo "(none yet)"
fi
