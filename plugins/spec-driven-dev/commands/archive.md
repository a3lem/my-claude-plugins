---
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, AskUserQuestion
allowed-prompts:
  - tool: Read
    prompt: read files
argument-hint: "[spec slug]"
---

Archive a completed spec. Use the spec-driven-development skill to:
1. Check task completeness (warn if incomplete)
2. Show sync summary (what would change per capability)
3. Merge deltas into reference specs
4. Validate merged specs with spec-critic agent
5. Move to archive

$ARGUMENTS
