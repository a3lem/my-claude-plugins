# Spec-Driven Development Plugin

A Claude Code plugin for structured feature development. Reference specs are the source of truth; change specs describe deltas that get merged back after implementation.

## Commands

| Command | Description | Example |
|---------|-------------|---------|
| `/explore` | Think through a problem before proposing | `/explore auth strategy` |
| `/propose` | Create change with all artifacts | `/propose user authentication` |
| `/refine` | Update any artifact | `/refine add OAuth support` |
| `/apply` | Implement the specification | `/apply user-authentication` |
| `/archive` | Sync deltas to reference + archive | `/archive user-authentication` |

## Workflow

```
Explore → Propose → Apply → Archive
  │         │        │        │
  ▼         ▼        ▼        ▼
think    proposal   code    sync to
         deltas/*   tests   reference/
         design
         tasks
```

`/refine` can update any artifact at any point. Upstream changes cascade -- modifying a spec may invalidate the design.

## Spec Structure

```
specs/
├── reference/                  # Source of truth (full specs)
│   ├── authentication/
│   │   └── spec.md
│   └── billing/
│       └── spec.md
└── changes/
    ├── add-oauth/              # Active change
    │   ├── proposal.md         # Why, what changes, capabilities, impact
    │   ├── deltas/             # Per-capability deltas
    │   │   ├── session-management/spec.md
    │   │   └── user-auth/spec.md
    │   ├── design.md           # Optional
    │   ├── tasks.md            # Optional
    │   └── notes/              # Optional
    └── archive/                # Completed changes
        └── 2026-03-01-initial-auth/
```

## Notation

Specs use mixed notation -- SHALL statements, Given/When/Then scenarios, and plain prose. See `references/spec.md` for the full guide.

## When to Use

**Use for:** Multi-scenario features, cross-cutting changes, multi-session work, ambiguous scope.

**Skip for:** Single-line fixes, routine refactors, dependency updates, obvious implementations.

## Sub-agents

| Agent | Model | Purpose |
|-------|-------|---------|
| spec-critic | sonnet | Adversarial reviewer with multi-turn dialogue |
