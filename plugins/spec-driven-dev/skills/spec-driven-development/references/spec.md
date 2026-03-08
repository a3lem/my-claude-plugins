# Specification Phase Reference

How to write and refine specifications using Gherkin scenarios.

**Prerequisite:** Spec directory must already exist (see Initialize phase).

## Spec Structure

Specifications live in two locations:

- **`specs/reference/`** — full Gherkin specs describing how things work (the truth)
- **`specs/changes/NNN-slug/`** — delta specs describing what a change adds, modifies, or removes

### Reference Specs

A reference spec describes the current intended behavior of a component or feature. It is the source of truth.

```
specs/reference/
├── authentication.md
├── billing.md
└── notifications.md
```

Use `templates/reference-spec.md` as a starting point.

### Delta Specs

A delta spec describes what a specific change does relative to the reference. It uses ADDED/MODIFIED/REMOVED sections.

```
specs/changes/003-oauth-support/
├── proposal.md     # Why we're doing this
├── spec.md         # What changes (delta spec)
├── design.md       # How we're building it (optional)
└── notes/          # Research, learnings (optional)
```

Use `templates/delta-spec.md` as a starting point.

## Mode Detection

- If `spec.md` doesn't exist → **Create mode**
- If `spec.md` exists → **Refine mode** (update based on instruction)

## Process

### 1. Load Context

Read existing spec files if present:
- `proposal.md` — problem context and motivation
- `spec.md` — current specification (if refining)
- `design.md` — design decisions (if exists)

### 2. Gather Information

In **Create mode**: Use AskUserQuestion to understand:
- What behavior changes (added, modified, removed)
- Acceptance scenarios (Given/When/Then)
- Known constraints

In **Refine mode**: Apply the user's instruction to existing spec.

### 3. Write spec.md

Use `templates/delta-spec.md` for change specs.

**Template guidance:**
- Organize by ADDED / MODIFIED / REMOVED sections
- Each scenario should test ONE behavior
- Use concrete values in examples, not placeholders
- Delete sections that don't apply (e.g., no REMOVED section if nothing is removed)
- Delete HTML comments before finalizing

## Gherkin Quick Reference

Gherkin provides structured, testable scenarios using Given/When/Then.

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

| Keyword | Purpose |
|---------|---------|
| **Given** | Precondition — system state before the action |
| **When** | Action — what the user or system does |
| **Then** | Outcome — observable result |
| **And** | Continuation of previous keyword |
| **But** | Negative continuation (e.g., "But no email is sent") |

**Guidelines:**
- Write scenarios in third person, present tense
- One scenario per behavior — don't combine happy path and error in one
- Use concrete values: "2 seconds" not "quickly", "3 retries" not "a few times"
- Avoid: might, should, could, usually → Use: specific outcomes

### 4. Warn About Cascade

If spec changed significantly, warn user that design may need updating.

## 5. Validate Specification

Review against this checklist:

**Completeness:**
- [ ] Happy path scenarios documented
- [ ] Error/edge case scenarios documented
- [ ] Boundary conditions covered

**Clarity:**
- [ ] Each scenario tests one behavior
- [ ] Concrete values used (no vague terms)
- [ ] Given/When/Then structure consistent

**Consistency:**
- [ ] Terminology consistent across scenarios
- [ ] No contradictory scenarios
- [ ] ADDED/MODIFIED/REMOVED sections accurate (for delta specs)

**Testability:**
- [ ] Each scenario is directly verifiable
- [ ] Outcomes are observable
- [ ] No untestable assertions
