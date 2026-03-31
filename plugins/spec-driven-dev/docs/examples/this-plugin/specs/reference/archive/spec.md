# Archive

## Overview

The archive capability finalizes a completed change by merging delta specs into their corresponding reference specs and moving the change directory to the archive. It is the last phase of the workflow, ensuring reference specs always reflect the current intended behavior of the system.

## Scenarios

### Requirement: Delta-to-reference merge

The system SHALL merge each delta spec in `change-dir/deltas/` into the corresponding reference spec, matching by directory name.

#### Scenario: ADDED requirements
  Given a delta spec at `specs/changes/add-oauth/deltas/user-auth/spec.md` with an ADDED section containing "Requirement: OAuth Login"
  And a reference spec at `specs/reference/user-auth/spec.md`
  When the archive merge runs
  Then "Requirement: OAuth Login" is appended to the reference spec

#### Scenario: MODIFIED requirements
  Given a delta spec with a MODIFIED section for "Requirement: Session Timeout" containing updated text
  And the reference spec contains an existing "### Requirement: Session Timeout" block
  When the archive merge runs
  Then the entire "### Requirement: Session Timeout" block in the reference spec is replaced with the delta's version

#### Scenario: REMOVED requirements
  Given a delta spec with a REMOVED section for "Requirement: Legacy Auth"
  And the reference spec contains "### Requirement: Legacy Auth"
  When the archive merge runs
  Then the "### Requirement: Legacy Auth" block is deleted from the reference spec

#### Scenario: RENAMED requirements
  Given a delta spec with a RENAMED section mapping "Basic Auth" to "Password Auth"
  And the reference spec contains "### Requirement: Basic Auth"
  When the archive merge runs
  Then the heading is updated to "### Requirement: Password Auth"

#### Scenario: New capability (no existing reference)
  Given a delta spec at `specs/changes/add-oauth/deltas/oauth-provider/spec.md` with only ADDED sections
  And no reference spec exists at `specs/reference/oauth-provider/`
  When the archive merge runs
  Then `specs/reference/oauth-provider/spec.md` is created from the delta's ADDED sections

### Requirement: Archive directory move

The system SHALL move the change directory to `specs/changes/archive/YYYY-MM-DD-slug/` after merging.

#### Scenario: Date-prefixed archive
  Given today is 2026-03-14
  And the change directory is `specs/changes/add-oauth/`
  When the archive completes
  Then the directory is moved to `specs/changes/archive/2026-03-14-add-oauth/`

### Requirement: Reference spec freshness

The system SHALL ensure reference specs describe current behavior, not historical changes. ADDED/MODIFIED/REMOVED/RENAMED section markers from the delta SHALL NOT appear in the merged reference spec.

#### Scenario: Clean reference after merge
  Given a delta spec with "## ADDED Requirements" containing "### Requirement: OAuth Login"
  When the delta is merged into the reference spec
  Then the reference spec contains "### Requirement: OAuth Login" directly under the "## Scenarios" section
  And the text "## ADDED Requirements" does not appear in the reference spec

### Requirement: Post-merge validation

The system SHALL invoke the spec-critic agent in `inter-spec` mode on updated reference specs after merging to verify coherence.

#### Scenario: Critic finds conflict
  Given two reference specs with contradictory requirements after merge
  When the spec-critic validates in `inter-spec` mode
  Then the critic returns `needs-work` or `blocked`
  And the system fixes the reference specs before proceeding to the archive move

#### Scenario: Critic approves
  Given all reference specs are coherent after merge
  When the spec-critic validates in `inter-spec` mode
  Then the critic returns `approved` or `approved-with-reservations`
  And the system proceeds to the archive move

