---
name: auto-memory
description: >
  Persistent auto-memory that saves knowledge across sessions. Triggers on
  "remember this", "save to memory", "forget", "update memory", "what do you
  remember", "check memory", or when you encounter stable patterns, architectural
  decisions, recurring solutions, or user preferences worth preserving. Also
  triggers at natural task completion points to consider what's worth remembering.
version: 0.1.0
---

# Auto Memory

Persistent memory that carries knowledge across sessions. You save memories as files organized by topic, and consult them to build on previous experience.

## Memory Directory

**Resolved directory:** !`sh ${CLAUDE_PLUGIN_ROOT}/skills/auto-memory/scripts/resolve-memory-dir.sh`

The directory and any files are created on first write. All Read/Write/Edit paths below use this resolved directory.

## Current Memory

**MEMORY.md contents:**

!`sh ${CLAUDE_PLUGIN_ROOT}/skills/auto-memory/scripts/read-memory.sh`

**Existing topic files:**

!`sh ${CLAUDE_PLUGIN_ROOT}/skills/auto-memory/scripts/list-topics.sh`

## Core File: MEMORY.md

`MEMORY.md` is the index file. Keep it concise (under 200 lines). It should contain:

- High-level summaries and links to topic files
- Quick-reference facts that don't warrant their own file

For detailed notes, create separate topic files (e.g., `debugging.md`, `patterns.md`, `architecture.md`) and link to them from MEMORY.md.

## When to Save

Save memories when you encounter:

- **Stable patterns and conventions** confirmed across multiple interactions
- **Key architectural decisions**, important file paths, and project structure
- **User preferences** for workflow, tools, and communication style
- **Solutions to recurring problems** and debugging insights

### Explicit user requests

- When the user asks you to remember something (e.g., "always use bun", "never auto-commit"), save it immediately — no need to wait for multiple interactions
- When the user asks to forget something, find and remove the relevant entries
- When the user corrects something you stated from memory, update or remove the incorrect entry **before continuing** so the mistake does not repeat

## When NOT to Save

- Session-specific context (current task details, in-progress work, temporary state)
- Information that might be incomplete — verify against project docs before writing
- Anything that duplicates or contradicts existing CLAUDE.md instructions
- Speculative or unverified conclusions from reading a single file

## How to Save

1. **Check first**: Read existing memory files to avoid duplicates. If a relevant file exists, update it rather than creating a new one.
2. **Organize semantically**: Group by topic, not chronologically. One file per topic area.
3. **Keep MEMORY.md lean**: Summaries and links only. Detailed content goes in topic files.
4. **Update or remove** memories that turn out to be wrong or outdated.

## How to Consult

At the start of a session or when context would help, read `MEMORY.md` and any relevant topic files. Use what you find to avoid re-learning things and to respect established preferences.

## Example Structure

```
.agents/memory/
  MEMORY.md            # Index: summaries + links to topic files
  architecture.md      # Project structure, key decisions
  patterns.md          # Code conventions, recurring patterns
  debugging.md         # Solutions to past issues
  preferences.md       # User workflow and tool preferences
```
