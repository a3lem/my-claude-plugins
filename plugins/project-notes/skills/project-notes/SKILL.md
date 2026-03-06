---
name: project-notes
description: |
  This skill should be used when creating, updating, or organizing wiki pages and documentation
  in the notes/ directory. It covers notes/ conventions, INDEX.md curation, wikilinks, and
  routing guidance for choosing between wiki pages, journal entries, and decision log entries.
  Triggers on: "write a note", "document this", "create a page about", "add to notes",
  "where should I document this", "what type of note should this be".
version: 1.0.0
---

# Project Notes

All project knowledge lives in `notes/` at the repository root.

## Conventions

- **Format**: plain markdown files, organized by topic in subdirectories
- **Cross-references**: use `[[wikilinks]]` for internal links between notes; use relative markdown links `[text](path.md)` for everything else
- **Entry point**: `notes/INDEX.md` is the curated index of high-value content -- human-maintained, links to what matters

## Creating a Page

Create pages as plain `.md` files under `notes/`. Organize by topic in subdirectories when a cluster of related pages emerges. There is no prescribed directory structure beyond:

- `notes/INDEX.md` -- curated entry point
- `notes/DECISIONS.md` -- decision log (see decision-log skill)
- `notes/journal/` -- timestamped entries (see journal skill)

Everything else is freeform.

## Routing: Which Type of Note?

| What you're capturing | Use |
|---|---|
| Topical reference that will be updated over time | Wiki page in `notes/` |
| Timestamped observation, discovery, or insight | Journal entry in `notes/journal/` |
| Concise record of a decision made | Decision log entry in `notes/DECISIONS.md` |

**Wiki pages** are durable -- they get revised and maintained. **Journal entries** are timestamped snapshots -- they capture a moment. **Decision log entries** are one-liners -- they record what was decided, not the full reasoning.

When a journal entry proves durable, promote it: extract the lasting content into a wiki page and link to it from `INDEX.md`.

## INDEX.md

`notes/INDEX.md` serves as the curated entry point. It is not auto-generated -- a human (or agent, with human review) maintains it by linking to the most valuable content.

A page gains authority by being linked from `INDEX.md`. Unlinked pages are still searchable but are not actively trusted as current.

## Searching Notes

```
# Find pages by name
Glob: notes/**/*.md

# Search content
Grep: pattern="<keyword>" path="notes/"
```
