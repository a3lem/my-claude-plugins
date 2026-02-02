---
allowed-tools: Read, Write, Edit, Glob, Grep, AskUserQuestion
allowed-prompts:
  - tool: Read
    prompt: read files
argument-hint: "[instruction or spec number]"
---

Refine an existing spec. Use the spec-driven-development skill to update:
- requirements.md (requirements refinement)
- design.md (design decisions)
- tasks.md (implementation plan)

Determine which file(s) to update based on the instruction.

**Monorepo support:** In monorepos, specs/ folders may exist at any level. Use Glob to find the spec across the codebase.

Instruction: $ARGUMENTS
