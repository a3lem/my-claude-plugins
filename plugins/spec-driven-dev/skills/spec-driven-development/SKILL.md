---
name: spec-driven-development
description: Unified spec-driven development workflow. Use for creating, designing, planning, executing, and critiquing specifications. Triggers on "spec", "create spec", "design spec", "plan spec", "execute spec", "critique spec", "requirements", or spec numbers like "spec 001".
version: 1.0.0
---

# Spec-Driven Development

A structured workflow where specifications are the source of truth. Implementation follows from specs, not the other way around.

**Always read [RULES.md](RULES.md) first** - it contains immutable principles that apply at all times.

## Workflow Overview

```
Analysis  →  Design → Plan → Execute → (Critique)
    │           │        │        │          │
    ▼           ▼        ▼        ▼          ▼
requirements  design  tasks    code    verdict
              (opt)            (on-demand)
```

Each phase produces a specification artifact. `notes/` can be created during any phase when there's information worth recording (research, exploration findings, incidental insights, failed approaches).

## When to Use This Workflow

SDD is valuable for complex, multi-session, or collaborative work. For trivial changes (single-line fixes, routine refactors, obvious implementations), skip SDD and implement directly. See **RULES.md > When to Use Spec-Driven Development** for detailed guidance.

## Agency Modes

**Interactive mode** (default): Use AskUserQuestion at each phase to gather input and confirm decisions.

**High agency mode**: When the user requests autonomous operation (e.g., "work on this until done", "implement this end-to-end", "full autopilot"), iterate through phases without prompting:
1. Analyze the problem and draft requirements
2. **Invoke spec-critic agent** (`intra-spec` mode) to validate requirements
3. Design the solution (if non-trivial)
4. Plan implementation with clear checkpoints
5. **Invoke spec-critic agent** (`intra-spec` + `spec-code` modes) to validate plan
6. Execute, looping back to earlier phases if snags arise
7. Verify against all acceptance criteria
8. **Invoke spec-critic agent** (`all` modes) before marking complete

In high agency mode, only pause for user input when hitting a genuine ambiguity that cannot be resolved through reasoning, or when the critic escalates after 5 rounds.

## Spec Directory Structure

```
specs/NNN-[slugified-description]/
├── requirements.md   # What we're building (FR-/NFR- with EARS notation)
├── design.md         # How we're building it (optional)
├── tasks.md          # Implementation plan + checklist with [NEXT] markers
└── notes/            # Optional: created during any phase when needed
    ├── research.md   # Exploration findings, links, citations
    ├── implementation.md  # Execution-phase learnings, gotchas
    └── ...           # Any files that add new information
```

Spec files include `status` field in frontmatter: `active`, `stale`, `archived`, or `superseded`. See RULES.md for details.

Specs are numbered sequentially starting at 001. When user says "spec 3", look for `specs/003-*/` (directory) or `specs/003-*.md` (compact).

## Compact Spec Format

For small, focused work, use a single-file spec instead of a directory:

```
specs/NNN-brief-description.md   # Single file instead of directory
```

**Use compact format when:**
- 1-2 functional requirements
- No design decisions needed
- Can be completed in one session
- Clear, obvious implementation

**Use directory format when:**
- 3+ requirements
- Design decisions needed
- Multi-session work
- Research or exploration required

Compact specs contain requirements + tasks in one file. See `templates/compact.md`.

## Command Mapping

| Command | Action |
|---------|--------|
| `/new [description]` | **Specify** - Create new spec (compact or directory) |
| `/refine [instruction]` | **Refine** - Update requirements, design, or tasks |
| `/execute [spec nr]` | **Execute** - Implement the spec |

For `/refine`, determine which file to update based on the instruction:
- Requirements-related → update `requirements.md`
- Architecture/design-related → update `design.md`
- Plan/tasks-related → update `tasks.md`

If unclear, use AskUserQuestion to clarify which aspect to refine.

## Phase: Initialize Spec

**REQUIRED reading:**
- [references/new.md](references/new.md) - Creating the spec directory

If spec already created, move on to next phase!

## Phase: Analyze Requirements

Create or refine requirements.

**MANDATORY: Read [references/requirements.md](references/requirements.md) before proceeding.**

**Completion:**
- In high agency mode: **Invoke spec-critic agent** (`intra-spec` mode) before proceeding
- In interactive mode: Inform user they can continue with design (optional) or plan

## Phase: Design Approach

Create or refine architectural decisions.

**MANDATORY: Read [references/design.md](references/design.md) before proceeding.**

**When to skip:** Simple features, bug fixes, obvious implementations.

**Completion:** Inform user they can continue with plan.

## Phase: Plan Implementation

Create implementation plan and progress checklist.

**MANDATORY: Read [references/tasks.md](references/tasks.md) before proceeding.**

**Completion:**
- In high agency mode: **Invoke spec-critic agent** (`intra-spec` + `spec-code` modes) before proceeding
- In interactive mode: Inform user they can continue with execute

## Phase: Execute

Implement the specification.

**MANDATORY: Read [references/execution.md](references/execution.md) before proceeding.**

**Completion:**
- Mark all items complete in tasks.md
- Create notes only if there are learnings worth capturing
- In high agency mode: **Invoke spec-critic agent** (`all` modes) before marking spec complete

## Phase: Critique

On-demand adversarial review. Delegate to **spec-critic** agent.

The critic acts as a senior engineer stand-in, challenging assumptions and demanding proof. It engages in multi-turn dialogue until satisfied (max 5 rounds).

**Critique modes:**
- `intra-spec` - Coherence within the spec (no contradictions between spec files)
- `spec-code` - Alignment with codebase (assumptions validated, conventions followed)
- `inter-spec` - Consistency across specs (no conflicts with other active specs)
- `all` - Run all three modes

**Verdict levels:**
- `approved` - No issues, may proceed
- `approved-with-reservations` - Minor issues, may proceed
- `needs-work` - Significant issues, must address
- `blocked` - Critical problems, cannot proceed

**Invocation:** "Consult with the spec-critic agent to review [spec path] (critique mode: [mode])"

**Multi-turn dialogue:**
When critic returns `needs-work` or `blocked`:
1. Address the concerns or prepare response
2. Resume: "Resume agent {agent_id} and review whether the concerns have been addressed"
3. Repeat until `approved` or max rounds reached
4. If escalated to user after 5 rounds, present summary and request user decision

**When to invoke critic (high agency mode):**
- After completing requirements → run `intra-spec`
- After completing design → run `intra-spec`
- After completing tasks → run `intra-spec` + `spec-code`
- Before marking spec complete → run `all`

**Reference:** [references/critique.md](references/critique.md) for detailed checklists

## Iteration

Spec-driven development appears sequential but **all phases can be revisited**:

- **Refine mode**: If spec files already exist, apply user's instruction to update them
- **Phase loops**: Any phase can loop back to an earlier phase when new information surfaces
  - Execution snag → may indicate plan issue → or design flaw → or requirements gap
  - Design contradiction → may require requirements clarification
- **Cascade warnings**: Changes to requirements may invalidate design and tasks
- **Scope confirmation**: In interactive mode, confirm with user before scope changes. In high agency mode, document scope changes in `notes/` and proceed

## Sub-agents

This skill delegates critique to a specialized agent:

| Agent | Model | Purpose |
|-------|-------|---------|
| **spec-critic** | sonnet | Adversarial reviewer; challenges assumptions, validates alignment |

## Templates

All templates are in `templates/`:
- `requirements.md` - Full requirements (directory format)
- `design.md` - Design decisions (directory format)
- `tasks.md` - Implementation plan (directory format)
- `notes/template.md` - Starting point for note files (any phase)
- `compact.md` - Single-file spec (compact format)

## Quick Reference

| Phase | Output | Key Tools |
|-------|--------|-----------|
| Analysis | requirements.md | AskUserQuestion |
| Design | design.md | AskUserQuestion |
| Plan | tasks.md | Glob, Grep, Read |
| Execute | code (+ notes/ if needed) | Bash, tests |
| Critique | verdict + findings | spec-critic |

