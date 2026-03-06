# project-notes

Project knowledge management plugin for Claude Code. Provides conventions for maintaining a `notes/` directory with wiki pages, a structured decision log, and timestamped journal entries.

## Skills

### project-notes

General note and wiki page management. Covers `notes/` directory conventions, `[[wikilinks]]`, `INDEX.md`, and routing guidance for when to use which type of note.

### decision-log

Structured `DECISIONS.md` format with `dcn-xxxx` reference codes, date-grouped entries, status tracking, and cross-references.

### journal

Timestamped entries in `notes/journal/` with origin markers (`ai`/`hu`), a scaffolding script, promotion via linking, and consolidation over time.

## Quick start

```bash
# Install from marketplace
claude plugin install project-notes

# Create a journal entry
bash "$(claude plugin root project-notes)/skills/journal/scripts/new-entry.sh" ai my-discovery --tags topic

# The notes/ directory will be created automatically
```
