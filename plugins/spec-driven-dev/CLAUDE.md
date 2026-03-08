# CLAUDE.md

## Project

A Claude Code plugin for spec-driven development — a structured workflow where specifications are the source of truth.

## Architecture

Four commands, one unified skill:

```
/new [description]     → Create spec (proposal in specs/changes/)
/refine [instruction]  → Update proposal, spec, or design
/execute [spec nr]     → Implement and verify
/archive [spec nr]     → Merge deltas into reference + archive
    │
    ▼
skills/spec-driven-development/
├── SKILL.md      ← Main orchestration
├── RULES.md      ← Core tenets (always loaded)
├── references/   ← Phase-specific guidance (loaded on-demand)
├── templates/    ← Spec file templates
└── scripts/      ← Helper scripts (next-spec-number.sh)
```

**Sub-agents:**
- `spec-critic` (sonnet) - Adversarial reviewer; challenges assumptions, validates alignment

## Spec Structure

**Reference specs** (source of truth):
```
specs/reference/
├── authentication.md   # Full Gherkin spec
├── billing.md
└── ...
```

**Change specs** (what's changing):
```
specs/changes/NNN-slug/
├── proposal.md     # Why (context, motivation, alternatives)
├── spec.md         # What (ADDED/MODIFIED/REMOVED + Gherkin)
├── design.md       # How (optional)
└── notes/          # Learnings (optional)
```

**Compact format** (simple changes):
```
specs/changes/NNN-slug.md   # Single file with context + scenarios
```

**Archive** (completed changes):
```
specs/changes/archive/NNN-slug/   # Moved after merging into reference
```

**Monorepo support:** `specs/` folders may be placed at any level (e.g., `packages/frontend/specs/`). Use Glob to discover existing locations.

## Key Conventions

| Convention | Details |
|------------|---------|
| **Gherkin scenarios** | Given/When/Then for testable specifications |
| **Delta specs** | ADDED/MODIFIED/REMOVED sections for changes |
| **Reference specs** | Full specs in `specs/reference/` (source of truth) |
| **Status field** | `active`, `stale`, `archived`, `superseded` in frontmatter |
| **Lock field** | `locked: true/false` in frontmatter controls editability |
| **notes/** | Created during ANY phase when needed; no duplication of other files |

## When to Use SDD

**Use for:** Multi-scenario features, cross-cutting changes, multi-session work, ambiguous scope

**Skip for:** Single-line fixes, routine refactors, dependency updates, obvious implementations

See `RULES.md > When to Use Spec-Driven Development` for detailed guidance.

## Key Files

| File | Purpose |
|------|---------|
| `SKILL.md` | Phase orchestration, workflow overview, agency modes |
| `RULES.md` | Core tenets, when-to-use guidance, status/lock mechanisms |
| `references/new.md` | Spec creation (format selection, numbering) |
| `references/spec.md` | Specification writing, Gherkin quick reference |
| `references/design.md` | Architectural decisions |
| `references/execution.md` | Implementation, verification, archive step |
| `references/critique.md` | Critique checklists for intra-spec, spec-code, inter-spec modes |
| `templates/proposal.md` | Problem context, motivation, alternatives |
| `templates/delta-spec.md` | ADDED/MODIFIED/REMOVED with Gherkin |
| `templates/reference-spec.md` | Full Gherkin spec for reference/ |
| `templates/compact.md` | Single-file spec template |
| `templates/notes/template.md` | Starting point for note files |
| `agents/spec-critic.md` | Adversarial reviewer (sonnet) |

## Inspiration

- https://github.com/jasonkneen/kiro
- https://github.com/github/spec-kit
- https://kiro.dev/docs/
- https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
