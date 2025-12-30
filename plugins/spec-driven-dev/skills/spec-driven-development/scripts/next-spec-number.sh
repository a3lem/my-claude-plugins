#!/bin/bash
# Finds the next available spec number (NNN format)
# Checks both directory specs (NNN-slug/) and compact specs (NNN-slug.md)
# Outputs: The next spec number, zero-padded to 3 digits
# Exit codes:
#   0 - Success
#   1 - specs/ directory doesn't exist (creates it and returns 001)

SPECS_DIR="${1:-specs}"

# Create specs/ if it doesn't exist
if [ ! -d "$SPECS_DIR" ]; then
    mkdir -p "$SPECS_DIR"
    echo "001"
    exit 0
fi

# Find highest existing spec number from both directories (NNN-*) and files (NNN-*.md)
highest=$(ls -1 "$SPECS_DIR" 2>/dev/null | grep -E '^[0-9]{3}-' | sed 's/^\([0-9]\{3\}\).*/\1/' | sort -n | tail -1)

if [ -z "$highest" ]; then
    echo "001"
else
    # Remove leading zeros, increment, then re-pad
    next=$((10#$highest + 1))
    printf "%03d\n" "$next"
fi
