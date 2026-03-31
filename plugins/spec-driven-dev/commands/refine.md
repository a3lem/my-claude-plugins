---
allowed-tools: Read, Write, Edit, Glob, Grep, AskUserQuestion
allowed-prompts:
  - tool: Read
    prompt: read files
argument-hint: "[instruction or spec slug]"
---

Refine an existing spec. Use the spec-driven-development skill to update:
- proposal.md (context and motivation)
- deltas/*/spec.md (per-capability spec deltas)
- design.md (design decisions)
- tasks.md (task breakdown and progress)

Determine which file(s) to update based on the instruction. For spec files, read the proposal's Capabilities section to map the instruction to the right capability's spec.md.

Instruction: $ARGUMENTS
