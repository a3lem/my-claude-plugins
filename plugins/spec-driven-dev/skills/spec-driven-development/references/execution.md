# Execution Phase Reference

How to execute a planned specification, tracking progress and capturing learnings.

## Process

### 1. Load Context

Read the spec (directory or compact file):

**For directory format:**
- `proposal.md` - Problem context and motivation
- `spec.md` - Gherkin scenarios to satisfy
- `design.md` - Architectural decisions (if exists)
- `notes/` - Previous learnings (if exists)

**For compact format:**
- Single `.md` file contains context + scenarios

### 2. Determine Code Location

**Important:** The `specs/` directory is for specification files only. All generated code must go elsewhere.

1. Check project structure for obvious code locations (e.g., `src/`, `lib/`, `app/`, project root)
2. Check `design.md` for specified file paths
3. If unclear, use AskUserQuestion: "Where should I place the generated code?"

Never write code files (`.js`, `.ts`, `.py`, `.html`, etc.) inside `specs/*/`.

### 3. Execute

Work through the implementation:
- Follow the design decisions
- Satisfy each Gherkin scenario from `spec.md`
- Track progress in notes if the work spans multiple sessions

### 4. Capture Learnings (Optional)

Create or update `notes/` when there's new information worth recording. Notes can be created during any phase.

**Suggested note files:**
- `research.md` - Exploration findings, links, citations (any phase)
- `implementation.md` - Execution-phase learnings, gotchas, failed approaches

**What belongs in notes:**
- Learnings and gotchas discovered during implementation
- Research findings and explored files index
- Failed approaches and why they didn't work
- Context for future maintainers that isn't obvious from the code

**What does NOT belong in notes:**
- Restatements of proposal context (already in proposal.md)
- Restatements of scenarios (already in spec.md)
- Restatements of design decisions (already in design.md)

**For compact format:** Use the Notes section at the bottom.

### 5. Verify & Complete

When implementation is done, **verification is required** before claiming completion:

1. **Run tests** if the project has a test framework
   - Execute relevant test suites
   - If tests fail, fix before proceeding

2. **If no automated tests exist**, use AskUserQuestion to request manual verification:
   - "Please verify the implementation meets these criteria: [list key scenarios]"
   - Wait for user confirmation before marking complete

3. **Walk through each Gherkin scenario** from `spec.md`:
   - For each scenario, confirm it's satisfied
   - Only document verification in notes if there are notable findings

4. **If verification fails**, surface the choice:
   - Fix implementation?
   - Adjust spec? (needs user confirmation)

5. **Only after verification passes:**
   - If there were deviations or learnings, document in `notes/`
   - Mark spec as complete

**Never claim "all scenarios satisfied" without evidence of verification.**

### 6. Archive

After the change is verified and merged:

1. **Merge deltas into reference specs**: Update the relevant files in `specs/reference/` to reflect the new behavior. The reference spec should describe how things work now, not how they changed.

2. **Move the change directory**: `specs/changes/NNN-slug/` → `specs/changes/archive/NNN-slug/`

3. **Update frontmatter**: Set `status: archived` in the archived spec files.

Archive keeps the change history browsable without cluttering active specs.

## Finding Specs

Specs can be directories or single files:
- Directory: `specs/changes/003-feature-name/`
- Compact: `specs/changes/003-feature-name.md`

When user says "spec 3", check for both `specs/changes/003-*/` (directory) and `specs/changes/003-*.md` (compact file).

## Updating Specs

Only modify `spec.md` with user confirmation — changes affect scope.
