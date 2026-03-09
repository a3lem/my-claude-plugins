---
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, AskUserQuestion
allowed-prompts:
  - tool: Read
    prompt: read files
argument-hint: "[spec number]"
---

Execute a spec. Use the spec-driven-development skill to:
1. Load spec context (proposal, spec, design, tasks.md)
2. Implement, satisfying all requirements and scenarios
3. Update tasks.md checkboxes as tasks are completed (if exists)
4. Verify completion against requirements and scenarios
5. Capture learnings in notes/ (or Notes section for compact specs)

**Monorepo support:** In monorepos, specs/ folders may exist at any level. Use Glob to find the spec across the codebase.

$ARGUMENTS
