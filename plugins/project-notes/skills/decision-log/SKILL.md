---
name: decision-log
description: |
  Record and look up decisions in notes/DECISIONS.md with dcn-xxxx reference codes. Use for
  logging architectural choices, design decisions, and team agreements, or finding past decisions.
  Triggers on: "log a decision", "we decided", "record this decision", "decision log",
  "what did we decide about", "find decision".
version: 1.0.0
---

# Decision Log

Record decisions concisely in `notes/DECISIONS.md`.

## Format

- Decisions are grouped by `## <date>` sections (YYYY-MM-DD, as returned by `date '+%Y-%m-%d'`).
- Each entry is a single top-level bullet: `- dcn-<4-char-hex>: <description>`
- The description must be 120 characters or fewer (markup for status changes doesn't count).
- Generate the hash: `head -c 2 /dev/urandom | xxd -p`
- No nested list items. One bullet per decision.

## Optional Annotations

- `#tags` or `#key=value` tags, e.g. `#infra`, `#bead=kap-fg3`
- `[[wikilinks]]` to notes pages
- `[markdown](links)` to journal entries or other docs

## Status Changes

Decisions are active by default. This log is not append-only -- entries are edited in place for status changes:

- **Reverse**: ~~strikethrough~~ the entry and append `[reversed by dcn-xxxx]`
- **Supersede**: ~~strikethrough~~ the entry and append `[superseded by dcn-xxxx]`
- The replacing decision should note what it replaces, e.g. `(replaces dcn-xxxx)`

## Example

```markdown
## 2026-02-16

- ~~dcn-6c80: Use Redis for caching #infra~~ [superseded by dcn-a3f1]
- dcn-a3f1: Use Memorystore instead of self-hosted Redis #infra (replaces dcn-6c80)
- dcn-hk45: Isolate tenants on every data query
```

## Creating a New Entry

1. Open (or create) `notes/DECISIONS.md`
2. Find or create the `## <today's date>` section
3. Generate a hash: `head -c 2 /dev/urandom | xxd -p`
4. Add the entry: `- dcn-<hash>: <description 120 chars max>`

If the file doesn't exist yet, create it with a `# Decisions Log` heading and the format comment block (see File Template section).

### File Template

When creating `notes/DECISIONS.md` for the first time:

```markdown
<!--
## About this file

Concise log of all decisions. See the decision-log skill for format details.

- Entries grouped by ## <date> (YYYY-MM-DD)
- Format: `- dcn-<4-char-hex>: <description 120 chars max>`
- Hash: `head -c 2 /dev/urandom | xxd -p`
- Optional: #tags, [[wikilinks]], [markdown](links)
- Status: ~~strikethrough~~ + [reversed by dcn-xxxx] or [superseded by dcn-xxxx]
-->

# Decisions Log
```
