# project-knowledge

Routing plugin for project knowledge. Helps decide where information should live and where to find it.

## What It Does

Provides a taxonomy of knowledge stores ordered by contract strength (specs > docs > decisions > notes > journal) and routing rules for "where does this go?" and "where do I look?".

This plugin doesn't manage any store directly — it routes to **spec-driven-dev** (for `specs/`), **project-notes** (for `notes/`, journal, decisions), and `docs/` (no plugin needed).

## Quick Reference

| Store | Location | Contract | Purpose |
|-------|----------|----------|---------|
| Specs | `specs/` | Strongest | Behavioral truth, Gherkin scenarios |
| Docs | `docs/` | Strong | Durable reference, maintained |
| Decisions | `notes/DECISIONS.md` | Medium | What was decided |
| Notes | `notes/` | Weak | Working knowledge |
| Journal | `notes/journal/` | Weakest | Timestamped snapshots |
