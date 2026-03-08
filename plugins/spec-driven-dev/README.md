# Spec-Driven Development Plugin

A Claude Code plugin for structured feature development using Gherkin specifications with reference/changes separation.

## Overview

This plugin provides a workflow for planning and implementing features through structured specifications. Reference specs describe how things work (source of truth). Change specs describe what's changing (delta). After implementation, deltas are merged back into reference specs and archived.

**Core principle:** Specifications don't serve code—code serves specifications.

## Plugin Structure

```
spec-driven-dev/
├── commands/
│   ├── new.md                       # /new [description]
│   ├── refine.md                    # /refine [instruction]
│   ├── execute.md                   # /execute [spec number]
│   └── archive.md                   # /archive [spec number]
├── skills/
│   └── spec-driven-development/
│       ├── SKILL.md                 # Main orchestration
│       ├── RULES.md                 # Core tenets (always loaded)
│       ├── references/
│       │   ├── new.md               # Spec creation guide
│       │   ├── spec.md              # Specification phase guide
│       │   ├── design.md            # Design phase guide
│       │   ├── execution.md         # Execution + archive guide
│       │   └── critique.md          # Critique checklists
│       ├── scripts/
│       │   └── next-spec-number.sh  # Finds next available spec number
│       └── templates/
│           ├── proposal.md
│           ├── delta-spec.md
│           ├── reference-spec.md
│           ├── design.md
│           ├── compact.md
│           └── notes/
│               └── template.md
├── agents/
│   └── spec-critic.md               # Adversarial reviewer (sonnet)
```

## Usage

### Commands

| Command | Description | Example |
|---------|-------------|---------|
| `/new` | Create new spec with proposal | `/new user authentication` |
| `/refine` | Update proposal, spec, or design | `/refine add OAuth support` |
| `/execute` | Implement the specification | `/execute 001` |
| `/archive` | Merge deltas into reference + archive | `/archive 001` |

### Workflow

```
Propose → Specify → Design → Execute → Archive
   │         │         │        │         │
   ▼         ▼         ▼        ▼         ▼
proposal   spec.md   design   code    merge to
           (delta)   (opt)            reference/
```

### Spec Structure

```
specs/
├── reference/                  # Source of truth (full Gherkin specs)
│   ├── authentication.md
│   └── billing.md
└── changes/                    # Active and archived changes
    ├── archive/                # Completed changes
    │   └── 001-initial-auth/
    └── 003-oauth-support/      # Active change
        ├── proposal.md         # Why (context, motivation)
        ├── spec.md             # What (ADDED/MODIFIED/REMOVED + Gherkin)
        ├── design.md           # How (optional)
        └── notes/              # Learnings (optional)
```

### Compact Spec (Single File)

For simple changes, use a single-file spec:

```
specs/changes/004-fix-login-bug.md   # Single file instead of directory
```

Contains context + Gherkin scenarios in one file. Use for 1-2 scenarios that can be completed in one session.

### When to Use vs Skip

**Use SDD for:** Multi-scenario features, cross-cutting changes, multi-session work, ambiguous scope.

**Skip SDD for:** Single-line fixes, routine refactors, dependency updates, obvious implementations.

See `skills/spec-driven-development/RULES.md` for detailed guidance.

### Iteration

- `/new user auth` → creates new spec with proposal
- `/refine add OAuth support` → updates existing spec (proposal, spec, or design)
- `/execute 001` → implements the spec
- `/archive 001` → merges into reference, moves to archive

When upstream changes (spec, design), downstream may need updating.

## Gherkin Scenarios

Specifications use Gherkin syntax for testable scenarios:

```gherkin
Scenario: User logs in with valid credentials
  Given a registered user with email "user@example.com"
  When the user submits valid credentials
  Then the system returns an authentication token
  And the token expires in 24 hours

Scenario: User logs in with invalid password
  Given a registered user with email "user@example.com"
  When the user submits an invalid password
  Then the system returns a 401 error
  And no token is issued
```

## Core Rules

1. **Specifications are the source of truth** - Implementation follows from specs
2. **Proposal before specification, specification before implementation** - Don't skip phases
3. **specs/ is sacred** - No code files in spec directories
4. **Verification is mandatory** - Never claim "done" without evidence
5. **Iteration is expected** - Loop back to earlier phases when needed

See `skills/spec-driven-development/RULES.md` for the complete ruleset.

## Sub-agents

| Agent | Model | Purpose |
|-------|-------|---------|
| spec-critic | sonnet | Adversarial reviewer; challenges assumptions, validates alignment |

## Why Spec-Driven Development?

1. **Persistence** - Specs survive session boundaries
2. **Structure** - Consistent format for proposals, specs, design, and tracking
3. **Clarity** - Gherkin scenarios ensure testable specifications
4. **Traceability** - Reference specs evolve; change history is preserved in archive
5. **Verification** - Never ship without confirming scenarios are satisfied
