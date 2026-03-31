# Proposal: Archive Safety Guards

## Why

The archive phase merges delta specs into reference specs mechanically without checking whether the change is actually complete. Incomplete tasks get silently archived, and users have no visibility into what the merge will do to their reference specs before it happens. Both problems erode trust in reference specs as the source of truth.

## What Changes

- Add a completeness check that warns when tasks remain incomplete before archiving
- Add a sync summary that shows what each delta would do to its reference spec before merging
- Both are pre-merge gates: completeness warns, sync summary informs

## Capabilities

### Modified Capabilities
- `archive`: Add pre-merge completeness check and sync summary

## Impact

- `references/archive.md` -- two new process steps before the existing merge step
- `SKILL.md` -- archive phase description updated
- `commands/archive.md` -- updated to mention new steps
- No changes to the merge mechanics themselves
