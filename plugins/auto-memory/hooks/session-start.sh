#!/usr/bin/env bash

mem_dir=$("${CLAUDE_PLUGIN_ROOT}/skills/auto-memory/scripts/resolve-memory-dir.sh")

echo "IMPORTANT: For auto memory, use the auto-memory skill (/auto-memory)."
echo ""
echo "Memory directory: $mem_dir"

# Show MEMORY.md contents (first 200 lines)
if [ -f "$mem_dir/MEMORY.md" ]; then
  echo ""
  echo "MEMORY.md contents:"
  head -200 "$mem_dir/MEMORY.md"
else
  echo ""
  echo "MEMORY.md: (not yet created — will be created on first write)"
fi

# List topic files
if [ -d "$mem_dir" ]; then
  topics=$(find "$mem_dir" -name '*.md' ! -name 'MEMORY.md' -exec basename {} \; 2>/dev/null)
  if [ -n "$topics" ]; then
    echo ""
    echo "Topic files: $topics"
  fi
fi
