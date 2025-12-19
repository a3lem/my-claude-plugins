---
name: create-new-spec
description: This skill should be used when the user mentions creating a new spec.
version: 1.0.0
---

# Creating a New Spec

This skill guides the creation and population of a new specification directory.

## Overview

Spec creation is a two-phase process:
1. **Scaffolding** - Create the directory structure with template files
2. **Population** - Gather information and fill in meaningful content

## When This Skill Applies

This skill activates when:
- Creating a new spec (`/new-spec`, "create a spec for...")
- Starting a new feature with spec-driven approach
- Setting up specification documentation for a task

## Spec Creation Process

### Phase 1: Scaffolding

Run the scaffolding script to create the directory structure:

```bash
python ${CLAUDE_PLUGIN_ROOT}/scripts/new_spec.py "Feature description"
```

This creates:
```
specs/NNN-feature-description/
├── requirements.md
├── design.md
├── tasks.md
└── notes.md
```

### Phase 2: Information Gathering

Use AskUserQuestion to gather concrete information before populating the spec files. Ask questions in batches to avoid overwhelming the user.

#### Requirements Questions

Ask about the problem and success criteria:

```
Question: "What problem does this feature solve?"
Header: "Problem"
Options:
- User-facing issue (describe the user pain point)
- Technical debt (describe the current limitation)
- New capability (describe what becomes possible)
```

```
Question: "What must be true for this feature to be considered complete?"
Header: "Success"
Options:
- Functional criteria (behavior-based acceptance)
- Performance criteria (speed, scale requirements)
- Integration criteria (works with existing systems)
```

#### Design Questions

Ask about architectural approach:

```
Question: "What's the high-level approach for implementing this?"
Header: "Approach"
Options:
- Extend existing code (modify current implementation)
- New component (create standalone module)
- Replace existing (rewrite current solution)
```

```
Question: "Are there key constraints or decisions already made?"
Header: "Constraints"
Options:
- Technology constraints (must use X library/framework)
- Compatibility requirements (must work with existing Y)
- No specific constraints
```

### Phase 3: Populating Spec Files

After gathering information, populate each file using the templates.

#### requirements.md

Use EARS notation for requirements. See `${CLAUDE_PLUGIN_ROOT}/shared/references/ears-notation.md` for syntax.

Template structure:
```markdown
# Requirements: [Feature Name]

## Problem Statement

[Description of the problem being solved]

## User Stories

- As a [role], I want [capability] so that [benefit]

## Success Criteria

WHEN [condition]
THE SYSTEM SHALL [expected behavior]

- [ ] Criterion 1 (testable, specific)
- [ ] Criterion 2
```

#### design.md

Template structure:
```markdown
# Design: [Feature Name]

## Approach

[High-level description of how this will be implemented]

## Key Decisions

| Decision | Rationale |
|----------|-----------|
| Decision 1 | Why this choice |

## Components

- Component A: [responsibility]
- Component B: [responsibility]

## Data Flow

[Description or diagram of how data moves through the system]
```

#### tasks.md

Template structure:
```markdown
# Tasks: [Feature Name]

## Plan

[Strategic approach - what phases, what order]

## Progress

### Setup
- [ ] Task 1
- [ ] Task 2

### Implementation
- [ ] Task 3
- [ ] Task 4

### Validation
- [ ] Write tests
- [ ] Manual testing
- [ ] Documentation
```

#### notes.md

Template structure:
```markdown
# Notes: [Feature Name]

## Implementation Details

[Technical notes added during implementation]

## Learnings

[Insights discovered during implementation]
```

## Additional Resources

### Shared References

- **`${CLAUDE_PLUGIN_ROOT}/shared/references/spec-driven-development.md`** - Philosophy and conventions of this approach
- **`${CLAUDE_PLUGIN_ROOT}/shared/references/ears-notation.md`** - EARS syntax guide for requirements

### Templates

Example files in `templates/`:
- **`requirements.md`** - Requirements structure with EARS notation
- **`design.md`** - Design document structure
- **`tasks.md`** - Tasks and progress structure
- **`notes.md`** - Implementation notes structure

## Best Practices

### Requirements
- Write testable, specific success criteria
- Use EARS notation for clarity
- Focus on "what" not "how"

### Design
- Document decisions and their rationale
- Keep it high-level, avoid implementation details
- Update as decisions change during implementation

### Tasks
- Keep tasks granular (one logical change per task)
- Order tasks by dependency
- Include validation/testing tasks

### Notes
- Add details as implementation progresses
- Document learnings for future reference
- Note gotchas and edge cases discovered
