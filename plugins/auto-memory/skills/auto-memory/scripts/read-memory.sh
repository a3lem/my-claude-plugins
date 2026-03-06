#!/bin/sh
# Print MEMORY.md contents (up to 200 lines) or a placeholder.
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
mem_dir=$("$SCRIPT_DIR/resolve-memory-dir.sh")

if [ -f "$mem_dir/MEMORY.md" ]; then
  head -200 "$mem_dir/MEMORY.md"
else
  echo "(no MEMORY.md yet -- will be created on first write)"
fi
