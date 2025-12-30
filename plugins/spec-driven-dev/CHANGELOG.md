# Changelog

## [1.0.0] - 2025-12-30

Initial release of the spec-driven development plugin.

### Added

- **Unified workflow** with three commands:
  - `/new [description]` - Create spec (compact or directory format)
  - `/refine [instruction]` - Update requirements, design, or plan
  - `/execute [spec nr]` - Implement and verify against acceptance criteria

- **Two spec formats**:
  - Directory format (`specs/NNN-slug/`) for complex, multi-requirement features
  - Compact format (`specs/NNN-slug.md`) for simple, single-session work

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
  - `requirements.md`, `design.md`, `tasks.md` for directory format
  - `compact.md` for single-file specs
  - `notes/template.md` for note files

- **Helper scripts**:
  - `next-spec-number.sh` - Finds next available spec number

- **Reference documentation**:
  - `RULES.md` - Core tenets (always loaded)
  - Phase-specific guides in `references/`
  - Critique checklists for all three modes
