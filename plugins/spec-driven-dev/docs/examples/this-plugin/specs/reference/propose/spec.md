# Propose

## Overview

The propose capability creates a new change and generates all specification artifacts in a single flow. It is the entry point for structured work -- turning a user's intent into a proposal, delta specs, and optionally design and tasks.

## Scenarios

### Requirement: Change directory creation

The system SHALL create a change directory under `specs/changes/` using a slugified version of the description.

#### Scenario: Slug from description
  Given a user invokes `/propose user authentication`
  When the system processes the description
  Then a directory `specs/changes/user-authentication/` is created

#### Scenario: Slug collision
  Given `specs/changes/user-authentication/` already exists
  When the user invokes `/propose user authentication`
  Then the system asks whether to continue the existing change or pick a different name

#### Scenario: No description provided
  When the user invokes `/propose` without a description
  Then the system asks "What feature or capability are you specifying?"

### Requirement: Proposal artifact

The system SHALL write a `proposal.md` as the first artifact in the change directory using `templates/proposal.md`.

#### Scenario: Proposal sections
  When the system writes proposal.md
  Then the file contains sections: Why, What Changes, Capabilities, Impact

#### Scenario: Capabilities contract
  Given the proposal lists `user-auth` under New Capabilities
  And the proposal lists `session-management` under Modified Capabilities
  When the propose phase proceeds to spec writing
  Then delta specs are created at `deltas/user-auth/spec.md` and `deltas/session-management/spec.md`
  And no other delta spec directories are created

### Requirement: Artifact generation flow

The system SHALL generate artifacts in dependency order: proposal → delta specs → design (optional) → tasks (optional).

#### Scenario: Full artifact flow
  Given a non-trivial change with multiple implementation steps
  When the propose phase completes
  Then proposal.md, at least one deltas/*/spec.md, design.md, and tasks.md all exist in the change directory

#### Scenario: Simple change skips optional artifacts
  Given a simple change (single capability, obvious implementation)
  When the propose phase completes
  Then proposal.md and at least one deltas/*/spec.md exist
  But design.md and tasks.md are not created

### Requirement: Critic invocation in high agency mode

WHEN operating in high agency mode, the system SHALL invoke the spec-critic agent after completing proposal and after completing specs + design.

#### Scenario: Critic after proposal
  Given high agency mode is active
  When proposal.md is written
  Then the spec-critic agent is invoked in `intra-spec` mode

#### Scenario: Critic after specs and design
  Given high agency mode is active
  When all delta specs and design.md are written
  Then the spec-critic agent is invoked in `intra-spec` + `spec-code` modes

## Non-Functional Requirements

The system SHALL keep proposals concise (1-2 pages). Implementation details belong in design.md, not proposal.md.

## Glossary

- Slug: A kebab-case identifier derived from the change description (e.g., "User Authentication" → `user-authentication`)
- Delta spec: A per-capability spec file describing changes (ADDED/MODIFIED/REMOVED/RENAMED) relative to a reference spec
- Capabilities contract: The mapping in proposal.md between capability names and the delta spec directories that will be created
