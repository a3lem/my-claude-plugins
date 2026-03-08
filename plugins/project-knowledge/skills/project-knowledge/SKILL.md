---
name: project-knowledge
description: |
  Routes project knowledge to the right store. Use when deciding where to put information,
  looking up existing knowledge, or understanding the relationship between specs, notes,
  decisions, journal entries, and docs. Triggers on: "where should I put this", "where do
  I find", "knowledge", "documentation strategy", "what goes where".
version: 1.0.0
---

# Project Knowledge

A routing guide for project knowledge. Each store has a different contract strength and purpose.

## Taxonomy

| Store | Location | Contract | Purpose |
|-------|----------|----------|---------|
| **Specs (reference)** | `specs/reference/` | Strongest | Source of truth for behavior. Gherkin scenarios. Verified before shipping. |
| **Specs (changes)** | `specs/changes/` | In-progress | Work underway. Proposals, delta specs, and designs for changes not yet shipped. |
| **Docs** | `docs/` | Strong | Durable reference content. Maintained, authoritative, human-reviewed. |
| **Decisions** | `notes/DECISIONS.md` | Medium | Concise record of what was decided. One-liners with `dcn-xxxx` codes. |
| **Notes** | `notes/` | Weak | Working knowledge, scratch pages, topic clusters. May go stale. |
| **Journal** | `notes/journal/` | Weakest | Timestamped snapshots. Capture a moment. Decay over time. |

## Where Does It Go?

| What you have | Where it goes |
|---------------|---------------|
| Behavioral requirement with testable scenarios | `specs/` (reference or change spec) |
| Durable reference that should stay current | `docs/` |
| "We decided to use X instead of Y" | `notes/DECISIONS.md` |
| Working notes, research, topic exploration | `notes/` |
| Observation, discovery, gotcha, lesson learned | `notes/journal/` |
| Implementation plan for a feature | `specs/changes/NNN-slug/` |
| API documentation, user guide | `docs/` |
| Design rationale for a specific change | `specs/changes/NNN-slug/design.md` |

## Where Do I Look?

| Looking for | Check |
|-------------|-------|
| How something should work | `specs/reference/` first, then `docs/` |
| Why a decision was made | `notes/DECISIONS.md`, then `specs/changes/archive/` |
| Current project conventions | `CLAUDE.md`, `docs/` |
| Recent observations or discoveries | `notes/journal/` |
| Working knowledge on a topic | `notes/`, then `notes/journal/` |
| History of a feature change | `specs/changes/archive/` |

## Promotion Path

Knowledge flows upward in contract strength:

```
journal → notes → docs
                   ↑
journal → notes → specs/reference/
```

- A journal observation that proves durable → extract into `notes/` or `docs/`
- A notes page that becomes authoritative → move to `docs/`
- A decision that needs behavioral enforcement → add Gherkin scenarios to `specs/`
- A completed change spec → merge scenarios into `specs/reference/`, archive the change

## Relationship to Other Plugins

This plugin provides routing guidance. The actual stores are managed by:

| Store | Plugin |
|-------|--------|
| `specs/` | **spec-driven-dev** — structured workflow with proposals, Gherkin specs, design, and archive |
| `notes/`, `notes/journal/`, `notes/DECISIONS.md` | **project-notes** — conventions for notes, journal entries, and decision log |
| `docs/` | No plugin needed — standard project documentation |

## Rules

- Don't duplicate knowledge across stores. Each piece of information lives in one place.
- Link between stores using `[[wikilinks]]` or relative markdown links.
- When in doubt about where something goes, check the taxonomy table above.
- Specs have the strongest contract: if a Gherkin scenario says it, the code must satisfy it.
- Docs have a strong contract: if it's in `docs/`, it should be current and maintained.
- Journal has the weakest contract: entries may be stale. Check recency and promotion status.
