---
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, AskUserQuestion
allowed-prompts:
  - tool: Read
    prompt: read files
argument-hint: "[spec number]"
---

Archive a completed spec. Use the spec-driven-development skill to:
1. Merge delta spec scenarios into relevant `specs/reference/` files
2. Move `specs/changes/NNN-slug/` → `specs/changes/archive/NNN-slug/`
3. Set `status: archived` in the moved spec files

Reference specs should describe how things work now, not how they changed.

$ARGUMENTS
