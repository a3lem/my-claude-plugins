---
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, AskUserQuestion
allowed-prompts:
  - tool: Read
    prompt: read files
argument-hint: "[spec slug]"
---

Apply a proposed change. Use the spec-driven-development skill to:
1. Load change context (proposal, deltas/*/spec.md, design, tasks.md)
2. Implement, satisfying all requirements and scenarios
3. Update tasks.md checkboxes as tasks are completed (if exists)
4. Verify completion against requirements and scenarios
5. Capture learnings in notes/ (if any)

$ARGUMENTS
