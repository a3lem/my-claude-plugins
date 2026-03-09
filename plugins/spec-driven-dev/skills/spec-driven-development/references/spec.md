# Specification Phase Reference

How to write and refine specifications using requirements and scenarios.

**Prerequisite:** Spec directory must already exist (see Initialize phase).

## Spec Structure

Specifications live in two locations:

- **`specs/reference/`** — full specs describing how things work (the truth)
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
- Acceptance criteria (requirements and scenarios)
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

## Specification Notation

Specs support three notations. Mix them freely within a single spec.

### SHALL Statements

Use SHALL for requirements, constraints, and non-functional requirements. Follows EARS (Easy Approach to Requirements Syntax) qualifiers.

| Pattern | Use When |
|---------|----------|
| The system SHALL [action] | Unconditional requirement |
| WHEN [trigger], the system SHALL [action] | Event-driven requirement |
| IF [condition], the system SHALL [action] | State-dependent requirement |
| WHILE [state], the system SHALL [action] | Ongoing constraint |

**Examples:**
- The system SHALL encrypt all data at rest using AES-256.
- WHEN a user exceeds 5 failed login attempts, the system SHALL lock the account for 15 minutes.
- IF the database is unreachable, the system SHALL retry 3 times with exponential backoff.
- WHILE the system is in maintenance mode, the system SHALL return 503 for all API requests.

### Given/When/Then Scenarios

Use Given/When/Then for behavioral specs that map directly to tests.

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

| Keyword | Purpose |
|---------|---------|
| **Given** | Precondition — system state before the action |
| **When** | Action — what the user or system does |
| **Then** | Outcome — observable result |
| **And** | Continuation of previous keyword |
| **But** | Negative continuation (e.g., "But no email is sent") |

### Plain Prose

Use plain prose where formal notation adds no value — overviews, context, migration notes, explanations.

### Choosing Notation

| Content | Recommended Notation |
|---------|---------------------|
| Functional requirements | SHALL statements |
| Constraints and NFRs | SHALL statements |
| Behavioral acceptance criteria | Given/When/Then scenarios |
| Test-mappable specifications | Given/When/Then scenarios |
| Context, overviews, migration notes | Plain prose |
| Complex multi-step interactions | Given/When/Then scenarios |

A single requirement often benefits from both: a SHALL statement declaring the rule, followed by a scenario demonstrating it.

### Hybrid Example

### Requirement: Session Timeout
The system SHALL expire sessions after 30 minutes of inactivity.

#### Scenario: Idle timeout
  Given an authenticated session
  When 30 minutes pass without activity
  Then the session is invalidated

#### Scenario: Activity resets timeout
  Given an authenticated session
  When the user performs an action at minute 29
  Then the session timeout resets to 30 minutes

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
- [ ] SHALL statements use EARS qualifiers correctly
- [ ] Given/When/Then structure consistent where used

**Consistency:**
- [ ] Terminology consistent across requirements and scenarios
- [ ] No contradictory requirements or scenarios
- [ ] ADDED/MODIFIED/REMOVED sections accurate (for delta specs)

**Testability:**
- [ ] Each requirement or scenario is directly verifiable
- [ ] Outcomes are observable
- [ ] No untestable assertions
