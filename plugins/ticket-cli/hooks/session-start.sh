#!/usr/bin/env bash
set -euo pipefail

# Check if tk is available and this project has a .tickets directory.
# tk ls exits 0 when .tickets/ exists (even if empty), exits 1 otherwise.
if ! command -v tk >/dev/null 2>&1; then
  exit 0
fi

if ! tk ls >/dev/null 2>&1; then
  exit 0
fi

# Project uses tk - output priming message
help_output=$(tk help 2>&1)

cat <<EOF
This project uses a CLI for task management: `tk` (ticket). Issues, or 'tickets', are stored within the the project directory. 

Unless instructed otherwise, use `Bash(tk ...)` for managing tasks instead of Task*(...) tool calls.

Output of `tk --help`:

\`\`\`
${help_output}
\`\`\`
EOF
