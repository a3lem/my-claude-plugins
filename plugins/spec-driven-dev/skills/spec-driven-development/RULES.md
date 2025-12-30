# Rules of Spec-Driven Development

These are immutable principles. They apply at all times, in all phases.

## Core Tenets

1. **Specifications don't serve code—code serves specifications.**
   The specification is the source of truth. Implementation follows from specs, not the other way around.

2. **Requirements before design, design before implementation.**
   Don't skip phases. Each phase has clear prerequisites and deliverables.

3. **specs/ is sacred—no code files, only specification artifacts.**
   The `specs/` directory contains only: `requirements.md`, `design.md`, `tasks.md`, and optionally `notes/`. All generated code goes elsewhere.

4. **Verification is mandatory—never claim "done" without evidence.**
   Run tests, or ask user to verify. Walk through each acceptance criterion.

5. **Iteration is expected; loop back to earlier phases when needed.**
   Specs are living documents. When implementation reveals gaps, refine the spec (with user confirmation for scope changes).

6. **Mark unclear areas with `[CLARIFICATION NEEDED]` and resolve before proceeding.**
   Don't make assumptions about ambiguous requirements. Surface uncertainty explicitly.

7. **Never fabricate assumptions or constraints.**
   Only document what was explicitly discussed or confirmed. If you're unsure, ask—don't invent. Assumptions not checked with the user are forbidden. Constraints not mentioned by the user are forbidden.

## When to Use Spec-Driven Development

SDD provides structure for complex work but is overhead for trivial changes.

### Use SDD When

- **Multi-requirement features** - More than 2-3 acceptance criteria
- **Cross-cutting changes** - Affects multiple components or systems
- **Multi-session work** - Too large to complete in one session
- **Ambiguous scope** - Requirements need clarification before implementation
- **High-risk changes** - Needs design review or careful planning
- **Collaborative work** - Multiple people or handoff expected

### Skip SDD When

- **Single-line fixes** - Typos, obvious bugs, trivial corrections
- **Routine refactors** - Rename, extract method, simple cleanup
- **Dependency updates** - Version bumps with no behavior change
- **Documentation-only changes** - README updates, comments
- **Exploratory spikes** - Quick experiments to inform a future spec

### Hybrid Approach

For medium-complexity work, consider a **compact spec** (single file) or skip design phase. When in doubt, ask the user.

## File Ownership

| File | Primary Owner | Others May Edit |
|------|---------------|-----------------|
| `requirements.md` | Specify phase | With user confirmation only |
| `design.md` | Design phase | With user confirmation only |
| `tasks.md` | Plan/Execute phases | Freely |
| `notes/summary.md` | All phases | Freely |
| `notes/*` (other) | All phases | Freely |

**Upstream changes invalidate downstream work.** Changing requirements may invalidate design and tasks. Always warn user.

## Lock Mechanism

Spec files (except `notes/`) have a `locked` property in their YAML frontmatter:

```yaml
---
locked: false
---
```

| Value | Meaning |
|-------|---------|
| `locked: false` | Agent MAY update this file |
| `locked: true` | Agent MAY NOT update this file |

This supports highly agentic workflows where certain specs are frozen (e.g., approved requirements) while others remain editable. When a file is locked and changes are needed, the agent must request the user unlock it first.

## Status Tracking

Spec files track their lifecycle state via the `status` field in YAML frontmatter:

```yaml
---
locked: false
status: active
---
```

| Status | Meaning |
|--------|---------|
| `active` | Current, being worked on or recently completed |
| `stale` | May be outdated; needs review before use |
| `archived` | Completed and no longer relevant; kept for reference |
| `superseded` | Replaced by another spec (add `superseded-by: NNN`) |

**Superseded example:**
```yaml
---
locked: true
status: superseded
superseded-by: 015
---
```

**Status transitions:**
- `active` → `stale` (when work pauses or requirements change upstream)
- `active` → `archived` (when feature is complete and shipped)
- `active` → `superseded` (when replaced by a new spec)
- `stale` → `active` (after review confirms still valid)

## Critique and Validation

The **spec-critic** agent provides adversarial review to ensure spec quality.

### Three Critique Modes

| Mode | What It Checks |
|------|---------------|
| `intra-spec` | Coherence within the spec |
| `spec-code` | Alignment between spec and codebase |
| `inter-spec` | Consistency across active specs |

### When to Request Critique

**Required (high agency mode):**
- Before transitioning from planning to execution
- Before marking a spec as complete

**Recommended:**
- After significant changes to requirements or design
- When resuming stale specs
- Before handoff to another person or session

### Responding to Critique

The critic returns a verdict: `approved`, `approved-with-reservations`, `needs-work`, or `blocked`.

- `approved` / `approved-with-reservations` → proceed
- `needs-work` / `blocked` → address concerns, resume dialogue
- After 5 rounds without resolution → escalate to user

### Critique Is Not Obstruction

The critic's role is quality assurance, not gatekeeping. It should:
- Approve when warranted
- Distinguish blocking issues from preferences
- Yield on minor style matters
- Escalate genuine disagreements to the user

## Anti-Patterns

- **Spec-after-the-fact** - Writing specs to document existing code defeats the purpose
- **Over-specification** - Specs should guide, not constrain every detail
- **Stale specs** - Specs that diverge from implementation lose value
- **Premature tasks** - Don't plan tasks until requirements are clear
- **Feature speculation** - No "might need" features; only what's explicitly required
- **Claiming done without verification** - Never mark complete without running tests or getting user confirmation
- **Fabricated assumptions** - Never add assumptions that weren't checked with the user
- **Invented constraints** - Never add constraints the user didn't mention

## Benefits of This Approach

- **Session persistence** - Specs survive context boundaries; work can resume days later
- **Reduced drift** - Requirements and implementation stay aligned
- **Testable outcomes** - EARS notation produces verifiable success criteria
- **Decision traceability** - Design rationale is captured, not lost

## Writing Style

- Unless stated otherwise, do not use emojis in your output.
