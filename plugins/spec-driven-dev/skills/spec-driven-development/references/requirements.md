# Requirements Phase Reference

How to gather and refine requirements for a specification.

**Prerequisite:** Spec directory must already exist (see Initialize phase).

## Mode Detection

- If `requirements.md` doesn't exist → **Create mode**
- If `requirements.md` exists → **Refine mode** (update based on instruction)

**Format detection:**
- If `specs/NNN-slug/` directory exists → directory format
- If `specs/NNN-slug.md` file exists → compact format

For compact format, requirements and tasks are in the same file.

## Process

### 1. Load Context

Read existing spec files if present:
- `requirements.md` - Current requirements (if refining)
- `design.md` - Design decisions (if exists)
- `tasks.md` - Implementation plan (if exists)

### 2. Gather Information

In **Create mode**: Use AskUserQuestion to understand:
- What problem this solves
- Acceptance criteria (what must be true when complete)
- Known constraints
- Make assumptions explicit

In **Refine mode**: Apply the user's instruction to existing requirements.

### 3. Render requirements.md

Use template from `templates/requirements.md`.

**Template guidance:**
- Omit sections marked `(optional)` if not applicable—keep specs lean
- Each requirement (FR-/NFR-) should represent ONE cohesive capability (but may have multiple acceptance criteria covering happy path, errors, edge cases)
- If acceptance criteria start covering unrelated behaviors, split into separate requirements
- Delete HTML comments before finalizing
- Use EARS notation for acceptance criteria (see below)
- Number requirements sequentially (FR-001, FR-002 for functional; NFR-001, NFR-002 for non-functional)
- Acceptance criteria use numbered lists (1., 2., 3.) within each requirement section
- When referencing criteria from other files (tasks.md, tests), use fully qualified IDs: `FR-001.1`, `FR-001.2`

## EARS Notation Quick Reference

EARS (Easy Approach to Requirements Syntax) provides patterns for unambiguous, testable requirements.

**CRITICAL: Each requirement is a single line.** Never break clauses across multiple lines.

| Pattern | When to Use | Example |
|---------|-------------|---------|
| **Ubiquitous** | Always active | [system] SHALL encrypt all stored passwords using bcrypt |
| **WHILE** (state) | Active during a state | WHILE in maintenance mode, [system] SHALL display a maintenance message |
| **WHEN** (event) | Triggered by event | WHEN user submits the login form, [system] SHALL validate credentials within 2 seconds |
| **WHERE** (feature) | Optional feature | WHERE audit logging is enabled, [system] SHALL record all data modifications |
| **IF-THEN** (error) | Unwanted behavior | IF database returns an error, THEN [system] SHALL retry up to 3 times |

**Complex requirements** combine patterns: `WHILE authenticated, WHEN user requests delete, [system] SHALL display confirmation`

**Avoid:** might, should, could, some, few, usually → **Use:** SHALL + specific numbers

### 4. Warn About Cascade

If requirements changed significantly, warn user that design and tasks may need updating.

## 5. Validate Requirements

Review the requirements against this checklist. Mark unclear areas with `[CLARIFICATION NEEDED]` tags inline, then use AskUserQuestion to resolve them before completing.

**Completeness:**
- [ ] Edge cases documented
- [ ] Error cases handled
- [ ] Business rules captured
- [ ] Normal flow scenarios covered

**Clarity:**
- [ ] Each requirement uses precise language
- [ ] No ambiguous terms (fast, easy, user-friendly)
- [ ] Technical jargon avoided or defined
- [ ] Expected behaviors are specific

**Consistency:**
- [ ] EARS notation used throughout
- [ ] Terminology consistent across requirements
- [ ] No contradictory requirements
- [ ] Similar scenarios handled similarly

**Testability:**
- [ ] Each requirement can be verified (by whatever testing strategy)
- [ ] Success criteria are observable
- [ ] Inputs and expected outputs specified
- [ ] Performance requirements are measurable
