## ADDED Requirements

### Requirement: Task completeness check

IF `tasks.md` exists in the change directory, the system SHALL count incomplete tasks (`- [ ]`) and warn the user before proceeding with the archive.

#### Scenario: All tasks complete
  Given a change with tasks.md containing only checked items (`- [x]`)
  When the user invokes `/archive`
  Then the system proceeds to the sync summary without warning

#### Scenario: Incomplete tasks remain
  Given a change with tasks.md containing 3 checked and 2 unchecked items
  When the user invokes `/archive`
  Then the system warns "2 of 5 tasks are incomplete"
  And asks the user to confirm before proceeding

#### Scenario: No tasks.md
  Given a change without tasks.md
  When the user invokes `/archive`
  Then the system skips the completeness check
  And proceeds to the sync summary

### Requirement: Sync summary

The system SHALL present a summary of what each delta merge would change in the reference specs before performing the merge.

#### Scenario: Summary for new capability
  Given a delta spec `deltas/oauth-provider/spec.md` with 3 ADDED requirements
  And no reference spec exists at `specs/reference/oauth-provider/`
  When the sync summary is generated
  Then it shows: "oauth-provider: NEW capability (3 requirements added)"

#### Scenario: Summary for modified capability
  Given a delta spec `deltas/user-auth/spec.md` with 1 ADDED, 2 MODIFIED, and 1 REMOVED requirement
  And a reference spec exists at `specs/reference/user-auth/spec.md`
  When the sync summary is generated
  Then it shows: "user-auth: 1 added, 2 modified, 1 removed"

#### Scenario: Summary with multiple capabilities
  Given delta specs for `user-auth` and `session-management`
  When the sync summary is generated
  Then both capabilities appear in the summary
  And the summary is presented to the user before the merge begins
