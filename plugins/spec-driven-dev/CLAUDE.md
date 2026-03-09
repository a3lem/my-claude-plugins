# CLAUDE.md

## Project

A Claude Code plugin for spec-driven development — a structured workflow where specifications are the source of truth.

## Architecture

Four commands, one unified skill:

```
/new [description]     → Create spec (proposal in specs/changes/)
/refine [instruction]  → Update proposal, spec, design, or tasks.md
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
├── authentication.md   # Full spec
├── billing.md
└── ...
```

**Change specs** (what's changing):
```
specs/changes/NNN-slug/
├── proposal.md     # Why (context, motivation, alternatives)
├── spec.md         # What (ADDED/MODIFIED/REMOVED + requirements/scenarios)
├── design.md       # How (optional)
├── tasks.md        # Progress overview (optional)
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
| **Mixed notation** | SHALL statements, Given/When/Then scenarios, plain prose |
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
| `references/spec.md` | Specification writing, notation guide |
| `references/design.md` | Architectural decisions |
| `references/execution.md` | Implementation, verification, archive step |
| `references/critique.md` | Critique checklists for intra-spec, spec-code, inter-spec modes |
| `references/tasks.md` | Tasks.md guidance (progress overview) |
| `templates/proposal.md` | Problem context, motivation, alternatives |
| `templates/delta-spec.md` | ADDED/MODIFIED/REMOVED with requirements and scenarios |
| `templates/reference-spec.md` | Full spec for reference/ |
| `templates/tasks.md` | Progress overview with task checkboxes |
| `templates/compact.md` | Single-file spec template |
| `templates/notes/template.md` | Starting point for note files |
| `agents/spec-critic.md` | Adversarial reviewer (sonnet) |

## Inspiration

- https://github.com/jasonkneen/kiro
- https://github.com/github/spec-kit
- https://kiro.dev/docs/
- https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
