#!/bin/sh
# Resolve the auto-memory directory.
# 1. $A3LEM_AUTO_MEMORY_DIR if set
# 2. Walk up from $PWD looking for .agents/memory/
# 3. Fall back to $PWD/.agents/memory/

if [ -n "$A3LEM_AUTO_MEMORY_DIR" ]; then
  echo "$A3LEM_AUTO_MEMORY_DIR"
  exit 0
fi

dir="$PWD"
while [ "$dir" != "/" ]; do
  if [ -d "$dir/.agents/memory" ]; then
    echo "$dir/.agents/memory"
    exit 0
  fi
  dir=$(dirname "$dir")
done

echo "$PWD/.agents/memory"
