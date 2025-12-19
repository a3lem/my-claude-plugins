# Spec-Driven Development Plugin

A Claude Code plugin for structured feature development using specification directories.

## Overview

This plugin provides a workflow for planning and implementing features through structured spec directories. Each spec contains requirements (using EARS notation), design decisions, task tracking, and implementation notes.

## Installation

```bash
# From a marketplace
/plugin install spec-driven-dev@marketplace-name

# Or add to your project's .claude/plugins
```

## Usage

### Creating a New Spec

```
/new-spec Add user authentication
```

The command will:
1. Create a numbered spec directory
2. Ask questions to understand the problem and approach
3. Populate the spec files with meaningful content

Result:
```
specs/
└── 001-add-user-authentication/
    ├── requirements.md   # Problem statement, EARS requirements, success criteria
    ├── design.md         # Approach, key decisions, components
    ├── tasks.md          # Implementation plan and progress checklist
    └── notes.md          # Implementation details, learnings (filled during work)
```

### Working with Specs

The `work-on-spec` skill automatically activates when you mention specs:

- "Let's continue spec 001"
- "Check the requirements for the auth spec"
- "Update progress on spec 3"

Claude will read the spec files and resume context from where you left off.

## Spec Structure

| File | Purpose | Notation |
|------|---------|----------|
| `requirements.md` | What we're building and success criteria | EARS notation |
| `design.md` | How we'll build it, architectural decisions | Prose + tables |
| `tasks.md` | Plan (strategy) + Progress (checklist) | Markdown checklist |
| `notes.md` | Implementation details and learnings | Free-form |

### EARS Notation

Requirements use EARS (Easy Approach to Requirements Syntax) for clarity:

```markdown
WHEN a user submits valid credentials
THE SYSTEM SHALL authenticate them within 2 seconds

- [ ] Login with valid email/password succeeds
- [ ] Failed attempts are logged
- [ ] Session token returned on success
```

See `shared/references/ears-notation.md` for the full syntax guide.

## Skills

### create-new-spec

Triggered when creating new specs. Guides information gathering and file population using AskUserQuestion.

### work-on-spec

Triggered when continuing work on existing specs. Provides guidance for:
- Reading and navigating spec directories
- Updating progress in tasks.md
- Adding learnings to notes.md
- Maintaining design decisions

## Optional: Backlog

Create `specs/backlog.md` to collect future spec ideas:

```markdown
# Spec Backlog

- Add dark mode support
- Implement search functionality
- Refactor auth to use OAuth
```

## Why Spec-Driven Development?

1. **Persistence** - Specs survive session boundaries; return days later and resume
2. **Structure** - Consistent format for requirements, design, and tracking
3. **Clarity** - EARS notation ensures unambiguous, testable requirements
4. **Context** - Claude reads specs to understand what you're building
5. **Documentation** - Specs become living documentation of your features
