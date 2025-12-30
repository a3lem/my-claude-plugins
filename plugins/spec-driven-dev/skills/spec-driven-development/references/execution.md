# Execution Phase Reference

How to execute a planned specification, tracking progress and capturing learnings.

## Process

### 1. Load Context

Read the spec (directory or compact file):

**For directory format:**
- `requirements.md` - Success criteria to satisfy
- `tasks.md` - Implementation plan and progress checklist
- `design.md` - Architectural decisions (if exists)
- `notes/summary.md` - Previous learnings (if exists)

**For compact format:**
- Single `.md` file contains requirements + tasks

### 2. Determine Code Location

**Important:** The `specs/` directory is for specification files only. All generated code must go elsewhere.

1. Check project structure for obvious code locations (e.g., `src/`, `lib/`, `app/`, project root)
2. Check `design.md` for specified file paths
3. If unclear, use AskUserQuestion: "Where should I place the generated code?"

Never write code files (`.js`, `.ts`, `.py`, `.html`, etc.) inside `specs/*/`.

### 3. Execute

Work through the checklist in `tasks.md`:
- Follow the plan section and design decisions
- Mark current item with `[NEXT]`, mark complete with `[x]`
- Add new items discovered during execution

### 4. Track Progress

Update `tasks.md` checklist continuously:
- Mark completed items with `[x]`
- Move `[NEXT]` marker to current item
- Add blocking issues or new items as they arise
- Keep items granular

### 5. Capture Learnings (Optional)

Create or update `notes/` when there's new information worth recording. Notes can be created during any phase - the `notes/` directory may already exist from earlier phases (e.g., research during design).

**Suggested note files:**
- `research.md` - Exploration findings, links, citations (any phase)
- `implementation.md` - Execution-phase learnings, gotchas, failed approaches

**What belongs in notes:**
- Learnings and gotchas discovered during implementation
- Research findings and explored files index
- Failed approaches and why they didn't work
- Experiments and their outcomes
- Context for future maintainers that isn't obvious from the code

**What does NOT belong in notes:**
- Summaries of requirements (already in requirements.md)
- Restatements of design decisions (already in design.md)
- Task completion status (already in tasks.md)

**For compact format:** Use the Notes section at the bottom - leave it empty or minimal if nothing notable.

Timestamp learnings by date (YYYY-MM-DD) for context.

### 6. Verify & Complete

When all implementation tasks are done, **verification is required** before claiming completion:

1. **Run tests** if the project has a test framework
   - Execute relevant test suites
   - If tests fail, fix before proceeding

2. **If no automated tests exist**, use AskUserQuestion to request manual verification:
   - "Please verify the implementation meets these criteria: [list key acceptance criteria]"
   - Wait for user confirmation before marking complete

3. **Walk through each acceptance criterion** from `requirements.md`:
   - For each FR-NNN and NFR-NNN, confirm it's satisfied
   - Only document verification in notes if there are notable findings

4. **If verification fails**, surface the choice:
   - Fix implementation?
   - Adjust requirement? (needs user confirmation)

5. **Only after verification passes:**
   - Mark all items complete in `tasks.md`
   - If there were deviations or learnings, document in `notes/`
   - Mark spec as complete

**Never claim "all requirements met" without evidence of verification.**

## Finding Specs

Specs can be directories or single files:
- Directory: `specs/003-feature-name/`
- Compact: `specs/003-feature-name.md`

When user says "spec 3", check for both `specs/003-*/` (directory) and `specs/003-*.md` (compact file).

## Updating Requirements

Only modify `requirements.md` with user confirmation - changes affect scope.
