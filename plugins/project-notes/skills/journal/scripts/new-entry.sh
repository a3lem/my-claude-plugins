#!/usr/bin/env bash
# Create a new journal entry with the correct filename template.
#
# Usage:
#   new-entry.sh <ai|hu> <slug> [--tags tag1,tag2] [--refs ref1,ref2]
#
# Example:
#   new-entry.sh ai vllm-batch-limit --tags vllm,performance --refs issue-42

set -euo pipefail

JOURNAL_DIR="$(git rev-parse --show-toplevel)/notes/journal"

# --- args ---
origin="${1:?Usage: new-entry.sh <ai|hu> <slug> [--tags t1,t2] [--refs r1,r2]}"
slug="${2:?Usage: new-entry.sh <ai|hu> <slug> [--tags t1,t2] [--refs r1,r2]}"
shift 2

if [[ "$origin" != "ai" && "$origin" != "hu" ]]; then
  echo "Error: origin must be 'ai' or 'hu', got '$origin'" >&2
  exit 1
fi

tags=""
refs=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --tags) tags="$2"; shift 2 ;;
    --refs) refs="$2"; shift 2 ;;
    *) echo "Unknown option: $1" >&2; exit 1 ;;
  esac
done

# --- filename ---
ts=$(date -u +"%Y%m%d.%H%M")
filename="${ts}.${origin}.${slug}.md"
filepath="${JOURNAL_DIR}/${filename}"

if [[ -e "$filepath" ]]; then
  echo "Error: $filepath already exists" >&2
  exit 1
fi

mkdir -p "$JOURNAL_DIR"

# --- content ---
{
  if [[ -n "$tags" || -n "$refs" ]]; then
    echo "---"
    if [[ -n "$tags" ]]; then
      echo "tags: [$(echo "$tags" | sed 's/,/, /g')]"
    fi
    if [[ -n "$refs" ]]; then
      echo "refs: [$(echo "$refs" | sed 's/,/, /g')]"
    fi
    echo "---"
    echo ""
  fi
  echo "# ${slug//-/ }"
  echo ""
} > "$filepath"

echo "$filepath"
