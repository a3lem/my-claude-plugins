# CLAUDE.md

## Project

A Claude Code plugin for spec-driven development - a structured workflow where specifications are the source of truth.

## Architecture

Three commands, one unified skill:

```
/new [description]     → Create spec (compact or directory)
/refine [instruction]  → Update requirements, design, or plan
/execute [spec nr]     → Implement and verify
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

## Spec Formats

**Directory format** (complex features):
```
specs/NNN-slug/
├── requirements.md   # FR-/NFR- with EARS notation
├── design.md         # Optional architectural decisions
├── tasks.md          # Implementation plan + checklist
└── notes/            # Optional: research.md, implementation.md, etc.
```

**Compact format** (simple features):
```
specs/NNN-slug.md     # Single file with requirements + tasks
```

Use compact for 1-2 requirements, single session, obvious implementation.

## Key Conventions

| Convention | Details |
|------------|---------|
| **EARS notation** | WHEN/IF/WHILE/WHERE + SHALL for acceptance criteria |
| **Requirement IDs** | FR-001, NFR-001 (requirements); FR-001.1, FR-001.2 (criteria) |
| **Task traceability** | Every task MUST reference requirements it satisfies |
| **Status field** | `active`, `stale`, `archived`, `superseded` in frontmatter |
| **Lock field** | `locked: true/false` in frontmatter controls editability |
| **[NEXT] marker** | Current task in checklist |
| **notes/** | Created during ANY phase when needed; no duplication of other files |

## When to Use SDD

**Use for:** Multi-requirement features, cross-cutting changes, multi-session work, ambiguous scope

**Skip for:** Single-line fixes, routine refactors, dependency updates, obvious implementations

See `RULES.md > When to Use Spec-Driven Development` for detailed guidance.

## Key Files

| File | Purpose |
|------|---------|
| `SKILL.md` | Phase orchestration, workflow overview, agency modes |
| `RULES.md` | Core tenets, when-to-use guidance, status/lock mechanisms |
| `references/new.md` | Spec creation (format selection, numbering) |
| `references/requirements.md` | Requirements gathering, EARS quick reference |
| `references/design.md` | Architectural decisions |
| `references/tasks.md` | Implementation planning, traceability rules |
| `references/execution.md` | Implementation, verification, notes guidance |
| `references/critique.md` | Critique checklists for intra-spec, spec-code, inter-spec modes |
| `templates/compact.md` | Single-file spec template |
| `templates/notes/template.md` | Starting point for note files |
| `agents/spec-critic.md` | Adversarial reviewer (sonnet) |

## Inspiration

- https://github.com/jasonkneen/kiro
- https://github.com/github/spec-kit
- https://kiro.dev/docs/
- https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
