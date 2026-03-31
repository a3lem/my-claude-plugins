# CLAUDE.md

A Claude Code plugin for spec-driven development. Specifications are the source of truth.

## Workflow

```
/explore [topic]       → Think before proposing (optional)
/propose [description] → Create change + all artifacts (proposal, deltas, design, tasks)
/refine [instruction]  → Update any artifact
/apply [spec slug]     → Implement and verify
/archive [spec slug]   → Sync deltas to reference + archive
```

## Spec Structure

```
specs/
├── reference/<capability>/spec.md   # How things work today
└── changes/
    ├── <slug>/                      # Active change
    │   ├── proposal.md              # Why we're doing this, what's changing
    │   ├── deltas/<capability>/spec.md  # Requirements and scenarios per capability
    │   ├── design.md                # Technical approach (optional)
    │   ├── tasks.md                 # Implementation checklist (optional)
    │   └── notes/                   # Learnings (optional)
    └── archive/YYYY-MM-DD-slug/     # Completed changes
```

Monorepo: each sub-project has its own `specs/` directory. `spectl` discovers them with `-r` (recursive). No central config needed.

## Plugin Layout

```
skills/spec-driven-development/
├── SKILL.md           # Orchestration and command mapping
├── RULES.md           # Stub (rules moved to SKILL.md)
├── references/        # Phase-specific guidance (loaded on-demand per command)
│   ├── explore.md, propose.md, apply.md, archive.md
│   ├── spec.md, design.md, tasks.md
│   └── critique.md
├── templates/         # proposal.md, spec-delta.md, reference-spec.md, design.md, tasks.md
└── agents/spec-critic.md  # Critical reviewer (sonnet)
```

## spectl

`scripts/spectl.py` is intended for use by an AI agent. Errors or problem cases should trigger an exit 1 with a clear explanation. This lets the agent explore solutions before continuing.

Whenever spectl is updated, check whether `validate` (+ `--fix`) logic needs updating to cover new fields or invariants.

## Inspiration

- [kiro](https://kiro.dev/docs/)
- [spec-kit](https://github.com/github/spec-kit)
- [openspec](https://github.com/nicobailon/openspec)
- [SDD tools (Fowler)](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)
