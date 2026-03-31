---
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, AskUserQuestion
allowed-prompts:
  - tool: Read
    prompt: read files
argument-hint: "[description]"
---

Propose a new change. Use the spec-driven-development skill to:
1. Create a new change directory (specs/changes/slug/)
2. Gather context and write proposal.md
3. Write per-capability spec deltas (deltas/*/spec.md)
4. Write design.md (if non-trivial)
5. Write tasks.md (if multi-step)

All artifacts are generated in one flow. The Capabilities section in the proposal defines which spec files get created.

Starting description (may be empty): $ARGUMENTS
