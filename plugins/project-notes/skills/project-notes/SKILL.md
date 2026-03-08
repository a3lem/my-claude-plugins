---
name: project-notes
description: |
  This skill should be used when creating, updating, or organizing pages and documentation
  in the notes/ directory. It covers notes/ conventions, INDEX.md curation, wikilinks, and
  routing guidance for choosing between notes pages, journal entries, and decision log entries.
  Triggers on: "write a note", "document this", "create a page about", "add to notes",
  "where should I document this", "what type of note should this be".
version: 1.0.0
---

# Project Notes

All project knowledge lives in `notes/` at the repository root. For durable reference content, prefer `docs/`.

## Conventions

- **Format**: plain markdown files, organized by topic in subdirectories
- **Cross-references**: use `[[wikilinks]]` for internal links between notes; use relative markdown links `[text](path.md)` for everything else
- **Entry point**: `notes/INDEX.md` is the curated index of high-value content -- human-maintained, links to what matters

## Creating a Page

Create pages as plain `.md` files under `notes/`. Organize by topic in subdirectories when a cluster of related pages emerges. There is no prescribed directory structure beyond:

- `notes/INDEX.md` -- curated entry point
- `notes/DECISIONS.md` -- decision log (see decision-log skill)
- `notes/journal/` -- timestamped entries (see journal skill)

For durable reference content that will be maintained long-term, prefer `docs/`.

## Routing: Which Type of Note?

| What you're capturing | Use |
|---|---|
| Timestamped observation, discovery, or insight | Journal entry in `notes/journal/` |
| Concise record of a decision made | Decision log entry in `notes/DECISIONS.md` |
| Working notes, scratch pages, topic clusters | Page in `notes/` |
| Durable reference content | `docs/` |

**Journal entries** are timestamped snapshots -- they capture a moment. **Decision log entries** are one-liners -- they record what was decided, not the full reasoning. **Notes pages** are working knowledge -- they evolve but may go stale. **`docs/`** is durable reference -- maintained and authoritative.

When a journal entry proves durable, promote it: extract the lasting content into `docs/` and link to it from `INDEX.md`.

## INDEX.md

`notes/INDEX.md` serves as the curated entry point. It is not auto-generated -- a human (or agent, with human review) maintains it by linking to the most valuable content.

A page gains authority by being linked from `INDEX.md`. Unlinked pages are still searchable but are not actively trusted as current.

## What Notes Are (and Aren't)

`notes/` is shared, human-readable project knowledge -- what happened, what was learned, what was decided. It's the place for context that matters to anyone working on the project, human or AI.

Things that look similar but serve different purposes:

- **`specs/`** (if available) has a stronger contract. Gherkin scenarios in specs are verified before shipping; notes carry no such guarantee. If something must be enforced as behavior, it belongs in a spec, not a note.
- **`.agents/memory/`** (if available) is operational context for AI sessions -- how to work here, what to watch out for. It's AI-private and not meant for human consumption. Notes are shared and human-facing.
- **`docs/`** is durable reference. Notes may go stale; docs are expected to stay current.

When in doubt: if it's a behavioral contract, use specs. If it's an agent working pattern, use auto-memory. If it's lasting reference, use docs. Everything else -- observations, research, working knowledge -- belongs in notes.

## Searching Notes

```
# Find pages by name
Glob: notes/**/*.md

# Search content
Grep: pattern="<keyword>" path="notes/"
```
