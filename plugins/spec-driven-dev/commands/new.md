---
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, AskUserQuestion
allowed-prompts:
  - tool: Read
    prompt: read files
argument-hint: "[description]"
---

Create a new spec. Use the spec-driven-development skill to:
1. Create a new spec directory (specs/NNN-slug/)
2. Gather requirements through conversation
3. Write requirements.md

**Monorepo support:** In monorepos, specs/ folders may be placed at any level (e.g., `packages/frontend/specs/`). Detect existing specs/ locations or ask user where to place the spec.

Starting description (may be empty): $ARGUMENTS
