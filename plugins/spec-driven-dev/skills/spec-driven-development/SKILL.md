---
name: spec-driven-development
description: Unified spec-driven development workflow. Use for creating, designing, executing, and critiquing specifications. Triggers on "spec", "create spec", "design spec", "execute spec", "critique spec", "proposal", "archive spec", or spec numbers like "spec 001".
version: 2.0.0
---

# Spec-Driven Development

A structured workflow where specifications are the source of truth. Implementation follows from specs, not the other way around.

**Always read [RULES.md](RULES.md) first** - it contains immutable principles that apply at all times.

## Workflow Overview

```
Propose  →  Specify  →  Design  →  Execute  →  Archive  →  (Critique)
   │           │          │          │           │            │
   ▼           ▼          ▼          ▼           ▼            ▼
proposal    spec.md    design    code      merge to      verdict
            (delta)    (opt)              reference/
```

Each phase produces a specification artifact. `notes/` can be created during any phase when there's information worth recording (research, exploration findings, incidental insights, failed approaches).

## When to Use This Workflow

SDD is valuable for complex, multi-session, or collaborative work. For trivial changes (single-line fixes, routine refactors, obvious implementations), skip SDD and implement directly. See **RULES.md > When to Use Spec-Driven Development** for detailed guidance.

## Agency Modes

**Interactive mode** (default): Use AskUserQuestion at each phase to gather input and confirm decisions.

**High agency mode**: When the user requests autonomous operation (e.g., "work on this until done", "implement this end-to-end", "full autopilot"), iterate through phases without prompting:
1. Draft proposal with problem context and motivation
2. **Invoke spec-critic agent** (`intra-spec` mode) to validate proposal
3. Write Gherkin scenarios (delta spec)
4. Design the solution (if non-trivial)
5. **Invoke spec-critic agent** (`intra-spec` + `spec-code` modes) to validate design
6. Execute, looping back to earlier phases if snags arise
7. Verify against all Gherkin scenarios
8. **Invoke spec-critic agent** (`all` modes) before marking complete
9. Archive: merge deltas into reference specs

In high agency mode, only pause for user input when hitting a genuine ambiguity that cannot be resolved through reasoning, or when the critic escalates after 5 rounds.

## Spec Directory Structure

```
specs/
├── reference/                        # How things work (source of truth)
│   ├── authentication.md             # Full Gherkin spec
│   ├── billing.md
│   └── ...
└── changes/                          # What's changing
    ├── archive/                      # Completed changes (for history)
    │   └── 001-initial-auth/
    ├── 003-oauth-support/            # Active change
    │   ├── proposal.md               # Why (context, motivation, alternatives)
    │   ├── spec.md                   # What (ADDED/MODIFIED/REMOVED + Gherkin)
    │   ├── design.md                 # How (optional)
    │   └── notes/                    # Learnings (optional)
    └── 004-fix-login-bug.md          # Compact format (single file)
```

Spec files include `status` field in frontmatter: `active`, `stale`, `archived`, or `superseded`. See RULES.md for details.

Specs are numbered sequentially starting at 001. When user says "spec 3", look for `specs/changes/003-*/` (directory) or `specs/changes/003-*.md` (compact).

### Monorepo Support

In monorepos, `specs/` folders may be placed at any level to keep them close to the project they relate to:

```
packages/frontend/specs/     # Frontend-specific specs
packages/backend/specs/      # Backend-specific specs
specs/                       # Cross-cutting specs
```

Use Glob (`**/specs/`) to discover spec locations. When multiple exist, prefer the one closest to the current working context, or ask the user. See `references/new.md` for details.

## Compact Spec Format

For small, focused work, use a single-file spec instead of a directory:

```
specs/changes/NNN-brief-description.md   # Single file instead of directory
```

**Use compact format when:**
- 1-2 Gherkin scenarios
- No design decisions needed
- Can be completed in one session
- Clear, obvious implementation

**Use directory format when:**
- 3+ scenarios
- Design decisions needed
- Multi-session work
- Research or exploration required

Compact specs contain context + scenarios in one file. See `templates/compact.md`.

## Command Mapping

| Command | Action |
|---------|--------|
| `/new [description]` | **Create** - Create new spec in `specs/changes/` |
| `/refine [instruction]` | **Refine** - Update proposal, spec, or design |
| `/execute [spec nr]` | **Execute** - Implement the spec |
| `/archive [spec nr]` | **Archive** - Merge deltas into reference + move to archive |

For `/refine`, determine which file to update based on the instruction:
- Context/motivation-related → update `proposal.md`
- Scenario/behavior-related → update `spec.md`
- Architecture/design-related → update `design.md`

If unclear, use AskUserQuestion to clarify which aspect to refine.

## Phase: Initialize Spec

**REQUIRED reading:**
- [references/new.md](references/new.md) - Creating the spec directory

If spec already created, move on to next phase!

## Phase: Propose

Draft the proposal — problem context, motivation, alternatives considered.

**MANDATORY: Read [references/new.md](references/new.md) before proceeding.**

Use `templates/proposal.md`.

**Completion:**
- In high agency mode: **Invoke spec-critic agent** (`intra-spec` mode) before proceeding
- In interactive mode: Inform user they can continue with specifying scenarios

## Phase: Specify

Write Gherkin scenarios describing the change.

**MANDATORY: Read [references/spec.md](references/spec.md) before proceeding.**

Use `templates/delta-spec.md` for change specs, `templates/reference-spec.md` for reference specs.

**Completion:**
- In high agency mode: proceed to design (if needed) or execute
- In interactive mode: inform user they can continue with design (optional) or execute

## Phase: Design Approach

Create or refine architectural decisions.

**MANDATORY: Read [references/design.md](references/design.md) before proceeding.**

**When to skip:** Simple features, bug fixes, obvious implementations.

**Completion:**
- In high agency mode: **Invoke spec-critic agent** (`intra-spec` + `spec-code` modes) before proceeding
- In interactive mode: Inform user they can continue with execute

## Phase: Execute

Implement the specification.

**MANDATORY: Read [references/execution.md](references/execution.md) before proceeding.**

**Completion:**
- Verify against all Gherkin scenarios in spec.md
- Create notes only if there are learnings worth capturing
- In high agency mode: **Invoke spec-critic agent** (`all` modes) before marking spec complete

## Phase: Archive

After the change is verified and merged, archive it.

**Process:**
1. Merge delta spec scenarios into the relevant `specs/reference/` files
2. Move `specs/changes/NNN-slug/` → `specs/changes/archive/NNN-slug/`
3. Set `status: archived` in the moved spec files

Reference specs should describe how things work *now*, not how they changed. The archived change directory preserves the history.

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
- After completing proposal → run `intra-spec`
- After completing spec + design → run `intra-spec` + `spec-code`
- Before marking spec complete → run `all`

**Reference:** [references/critique.md](references/critique.md) for detailed checklists

## Iteration

Spec-driven development appears sequential but **all phases can be revisited**:

- **Refine mode**: If spec files already exist, apply user's instruction to update them
- **Phase loops**: Any phase can loop back to an earlier phase when new information surfaces
  - Execution snag → may indicate design flaw → or spec gap → or proposal issue
  - Design contradiction → may require spec clarification
- **Cascade warnings**: Changes to spec may invalidate design
- **Scope confirmation**: In interactive mode, confirm with user before scope changes. In high agency mode, document scope changes in `notes/` and proceed

## Sub-agents

This skill delegates critique to a specialized agent:

| Agent | Model | Purpose |
|-------|-------|---------|
| **spec-critic** | sonnet | Adversarial reviewer; challenges assumptions, validates alignment |

## Templates

All templates are in `templates/`:
- `proposal.md` - Problem context, motivation, alternatives (directory format)
- `delta-spec.md` - ADDED/MODIFIED/REMOVED with Gherkin scenarios (directory format)
- `reference-spec.md` - Full Gherkin spec for reference/ (reference specs)
- `design.md` - Design decisions (directory format)
- `notes/template.md` - Starting point for note files (any phase)
- `compact.md` - Single-file spec (compact format)

## Quick Reference

| Phase | Output | Key Tools |
|-------|--------|-----------|
| Propose | proposal.md | AskUserQuestion |
| Specify | spec.md (delta) | AskUserQuestion |
| Design | design.md | AskUserQuestion |
| Execute | code (+ notes/ if needed) | Bash, tests |
| Archive | updated reference/, archived change | Edit, Bash |
| Critique | verdict + findings | spec-critic |
