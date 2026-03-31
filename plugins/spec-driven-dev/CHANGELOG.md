# Changelog

## [2.1.0] - 2026-03-13

Structural refinements and requirements engineering improvements based on expert review.

### Changed

- **Directory-per-capability structure**: Specs now use `capability-name/spec.md` instead of flat `capability-name.md` files. Both reference and delta specs use `spec.md` as the filename – the path conveys the role.

- **Template renames**: `delta-spec.md` → `change-spec.md`, `reference-spec.md` retained. Delta spec title simplified from `# Delta: [Capability Name]` to `# [Capability Name]` (the ADDED/MODIFIED/REMOVED/RENAMED sections already signal it's a delta).

- **Delta/reference heading alignment**: Reference spec template now uses `### Requirement: [name]` and `#### Scenario:` headings, matching delta format. This makes archive merge instructions ("find matching `### Requirement:` header, replace entire block") work correctly.

- **Complete EARS patterns**: Added complex/compound (`WHILE [state] WHEN [trigger]`), unwanted behavior (`IF [unwanted condition]`), and optional/product-line (`WHERE [feature is included]`) patterns to spec reference.

- **Test-first execution guidance**: Added recommended (not mandated) test-first approach to execution reference, with traceability convention for naming tests after scenarios.

### Added

- **Cross-cutting change guidance**: New section in spec reference addressing verbosity of changes that affect many capabilities, with grouping strategies.
- **Stakeholders section**: Optional `## Stakeholders` in proposal template.
- **Traceability checks**: Spec-code checklists in both critique reference and spec-critic agent now verify test files/functions correspond to scenario names.

### Removed

- Stale v1.0 anti-pattern (`FR-traceability markers like _[FR-001.1]_`) from tasks reference.

## [2.0.0] - 2026-03-13

Redesign of the spec model based on learnings from OpenSpec analysis.

### Changed

- **Per-capability delta specs**: Each change directory now has a `specs/` subdirectory with one file per capability affected, replacing the monolithic `spec.md`. Each delta file maps 1:1 to the reference spec it modifies.

- **Slug-only naming**: Change directories use slug names (`specs/changes/add-oauth/`) instead of numeric prefixes (`specs/changes/003-add-oauth/`). Date prefix added only on archive (`specs/changes/archive/YYYY-MM-DD-slug/`).

- **Structured monorepo layout**: Monorepo support is now controlled by `specs/config.toml` with a `[workspaces]` table mapping workspace names to repo paths, replacing the "specs/ anywhere" convention.

- **Proposal Capabilities section**: Proposals now include a `## Capabilities` section listing new and modified capabilities, creating a contract between proposal and spec phases.

- **Delta format expanded**: Delta specs now support four operations: ADDED, MODIFIED, REMOVED, and RENAMED. MODIFIED uses full replacement text (no "Was:" prefix). RENAMED uses FROM:/TO: format.

- **Mechanical archive**: Archive step applies each delta file to its matching reference spec mechanically (append ADDED, replace MODIFIED, delete REMOVED, rename RENAMED).

- **Design template**: Restructured with Goals/Non-Goals and named Decisions sections (replacing table format).

- **No frontmatter**: Removed YAML frontmatter (`status`, `locked` fields) from spec files and templates. Lifecycle state is conveyed by directory location (active in `changes/`, completed in `archive/`).

### Removed

- `next-spec-number.sh` script and `scripts/` directory
- Numeric spec prefixes (NNN-slug)
- `templates/compact.md` (already removed in prior update)

## [1.0.0] - 2025-12-30

Initial release of the spec-driven development plugin.

### Added

- **Unified workflow** with three commands:
  - `/new [description]` - Create spec
  - `/refine [instruction]` - Update requirements, design, or plan
  - `/execute [spec nr]` - Implement and verify against acceptance criteria

- **EARS notation** for requirements (Easy Approach to Requirements Syntax):
  - Patterns: WHEN, IF-THEN, WHILE, WHERE + SHALL
  - Single-line format ensuring testable acceptance criteria
  - Fully qualified IDs for traceability (FR-001.1, FR-001.2)

- **Spec-critic agent** for adversarial review:
  - Three critique modes: `intra-spec`, `spec-code`, `inter-spec`
  - Graduated verdicts: approved, approved-with-reservations, needs-work, blocked
  - Multi-turn dialogue with max 5 rounds before escalation
  - Automatic invocation in high agency mode at phase transitions

- **Status tracking** in frontmatter:
  - Values: `active`, `stale`, `archived`, `superseded`
  - Lock mechanism (`locked: true/false`) for editability control

- **Task traceability**:
  - Every task must reference requirements it satisfies
  - `[NEXT]` marker for current task in checklist
  - Verification task at end of every plan

- **Notes directory** (`notes/`):
  - Created during any phase when needed
  - For research findings, implementation learnings, gotchas
  - No duplication of other spec files

- **Agency modes**:
  - Interactive mode (default): User confirmation at each phase
  - High agency mode: Autonomous operation with critic validation

- **Templates**:
  - `requirements.md`, `design.md`, `tasks.md`
  - `notes/template.md` for note files

- **Helper scripts**:
  - `next-spec-number.sh` - Finds next available spec number

- **Reference documentation**:
  - `RULES.md` - Core tenets (always loaded)
  - Phase-specific guides in `references/`
  - Critique checklists for all three modes
