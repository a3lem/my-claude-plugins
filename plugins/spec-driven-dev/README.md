# Spec-Driven Development Plugin

A Claude Code plugin for structured feature development using specification directories or compact single-file specs.

## Overview

This plugin provides a unified workflow for planning and implementing features through structured spec directories. Each spec contains requirements, design decisions, task tracking, and implementation notes.

**Core principle:** Specifications don't serve code—code serves specifications.

## Plugin Structure

```
spec-driven-dev/
├── commands/
│   ├── new.md                       # /new [description]
│   ├── refine.md                    # /refine [instruction]
│   └── execute.md                   # /execute [spec number]
├── skills/
│   └── spec-driven-development/
│       ├── SKILL.md                 # Main orchestration
│       ├── RULES.md                 # Core tenets (always loaded)
│       ├── references/
│       │   ├── new.md               # Spec creation guide
│       │   ├── requirements.md      # Requirements phase guide
│       │   ├── design.md            # Design phase guide
│       │   ├── tasks.md             # Planning phase guide
│       │   ├── execution.md         # Execution phase guide
│       │   └── critique.md          # Critique checklists
│       ├── scripts/
│       │   └── next-spec-number.sh  # Finds next available spec number
│       └── templates/
│           ├── requirements.md
│           ├── design.md
│           ├── tasks.md
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
| `/new` | Create new spec (compact or directory) | `/new user authentication` |
| `/refine` | Update requirements, design, or plan | `/refine add OAuth support` |
| `/execute` | Implement the specification | `/execute 001` |

### Workflow

```
Specify → Design → Plan → Execute
   │         │        │        │
   ▼         ▼        ▼        ▼
requirements  design  tasks    code
              (opt)

notes/ created only when needed (learnings, research, gotchas)
```

### Spec Directory (Full Format)

```
specs/001-add-user-authentication/
├── requirements.md   # What we're building (FR-/NFR- with EARS notation)
├── design.md         # How we're building it (optional)
├── tasks.md          # Implementation plan + checklist with [NEXT] markers
└── notes/            # Optional: created during any phase
    ├── research.md   # Exploration findings (any phase)
    └── implementation.md  # Execution-phase learnings
```

### Compact Spec (Single File)

For simple features, use a single-file spec:

```
specs/002-fix-login-bug.md   # Single file instead of directory
```

Contains requirements + tasks in one file. No design section. Use for 1-2 requirements that can be completed in one session.

### When to Use vs Skip

**Use SDD for:** Multi-requirement features, cross-cutting changes, multi-session work, ambiguous scope.

**Skip SDD for:** Single-line fixes, routine refactors, dependency updates, obvious implementations.

See `skills/spec-driven-development/RULES.md` for detailed guidance.

### Iteration

- `/new user auth` → creates new spec with requirements
- `/refine add OAuth support` → updates existing spec (requirements, design, or plan)
- `/execute 001` → implements the spec

When upstream changes (requirements, design), downstream may need updating.

## EARS Notation

Requirements use EARS (Easy Approach to Requirements Syntax):

```markdown
### FR-001: User Login

**Acceptance Criteria:**

1. WHEN user submits valid credentials, [system] SHALL authenticate within 2 seconds
2. IF authentication fails, THEN [system] SHALL display error message
3. WHILE user is authenticated, [system] SHALL maintain session
```

When referencing specific criteria from other files (tasks, tests), use fully qualified IDs: `FR-001.1`, `FR-001.2`, etc.

## Core Rules

1. **Specifications are the source of truth** - Implementation follows from specs
2. **Requirements before design, design before implementation** - Don't skip phases
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
2. **Structure** - Consistent format for requirements, design, and tracking
3. **Clarity** - EARS notation ensures testable requirements
4. **Traceability** - Tasks reference requirements (FR-001, NFR-001)
5. **Verification** - Never ship without confirming requirements are met
