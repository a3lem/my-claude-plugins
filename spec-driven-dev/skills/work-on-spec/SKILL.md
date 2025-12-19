---
name: work-on-spec
description: This skill should be used when the user mentions "continue spec", "work on spec", "check requirements", "update progress", "spec 001", or wants to work with an existing specification directory. Provides guidance for reading, navigating, and updating spec files during implementation.
version: 1.0.0
---

# Working on a Spec

This skill provides guidance for working with existing specification directories during implementation.

## Overview

Spec directories contain structured documentation for features under development:
- `requirements.md` - Problem statement and success criteria (EARS notation)
- `design.md` - Architectural approach and key decisions
- `tasks.md` - Implementation plan and progress tracking
- `notes.md` - Implementation details and learnings

## When This Skill Applies

This skill activates when:
- Resuming work on an existing spec ("continue spec 3", "let's work on spec 001")
- Checking requirements or design decisions
- Updating task progress
- Adding implementation notes or learnings
- Navigating the specs/ directory

## Working with Specs

### Discovering Specs

List the `specs/` directory to find existing specs:

```
specs/
├── backlog.md           # Future spec ideas
├── 001-feature-name/
├── 002-another-feature/
└── 003-third-feature/
```

Specs are numbered sequentially (001, 002, etc.). When user says "spec 3" or "spec 003", look for `specs/003-*/`.

### Loading Context

Read all files in the relevant spec directory to understand:
- **requirements.md** - What to build, success criteria
- **design.md** - How to build it, architectural decisions
- **tasks.md** - Plan and progress checklist
- **notes.md** - Implementation details, learnings

### Before Coding

1. Check `requirements.md` for success criteria - implementation must satisfy these
2. Review `design.md` for architectural decisions to follow
3. Check `tasks.md` for current progress and next steps

### While Coding

1. Follow the approach outlined in `design.md`
2. Mark items complete in `tasks.md` as they finish
3. Add implementation details to `notes.md`

### When Stuck or Learning Something

1. Document findings in `notes.md` under Learnings section
2. Update `design.md` if architectural decisions change
3. Refine `requirements.md` if scope changes (confirm with user first)

## File Update Guidelines

### tasks.md

Two sections to maintain:

**Plan** - Strategic approach (update if approach changes)

**Progress** - Checklist of tasks
- Mark complete: `- [x] Task description`
- Add new tasks discovered during implementation
- Keep granular (one task = one logical change)

### notes.md

**Implementation Details** - Technical decisions, code patterns used

**Learnings** - Insights discovered during implementation, gotchas for future reference

### requirements.md

Only update with user confirmation. Changes here affect scope.

### design.md

Update when:
- Architectural approach changes
- New key decisions are made
- Trade-offs are reconsidered

## Spec Status Indicators

Infer spec status from tasks.md:
- **Not started** - All tasks unchecked
- **In progress** - Some tasks checked
- **Complete** - All tasks checked

## Cross-Spec References

When one spec relates to another, note the relationship in design.md or notes.md:
```markdown
Related: See [spec 002](../002-related-feature/) for the authentication approach.
```

## Shared References

- **`${CLAUDE_PLUGIN_ROOT}/shared/references/spec-driven-development.md`** - Philosophy and conventions of this approach
- **`${CLAUDE_PLUGIN_ROOT}/shared/references/ears-notation.md`** - EARS syntax for writing unambiguous requirements
