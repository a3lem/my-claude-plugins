---
description: >
  Create a new spec directory for a feature/task (context: spec-driven development)
allowed-tools: Bash(bash:*), Read, Write, Edit, Glob, Grep, AskUserQuestion
argument-hint: [description]
---

# Create New Spec

Create a new specification directory and guide the user through populating it with meaningful content.

## Phase 1: Scaffolding

1. Check if a `specs/` directory exists in the project root. If not, create it.

2. Run the scaffolding script:
   ```bash
   python ${CLAUDE_PLUGIN_ROOT}/scripts/new_spec.py "$arguments"
   ```

3. The script outputs the created directory path. Read the created files to confirm structure.

## Phase 2: Information Gathering

Use AskUserQuestion to gather information for populating the spec. Ask in focused batches.

### Batch 1: Problem & Goals

Ask these questions:

**Question 1:**
- Question: "What problem does this feature solve?"
- Header: "Problem"
- Options:
  - "User-facing issue" - A pain point users currently experience
  - "Technical limitation" - Current system can't do something needed
  - "New capability" - Enabling something not previously possible

**Question 2:**
- Question: "How will we know this feature is complete?"
- Header: "Done when"
- Options:
  - "Specific behavior works" - Feature performs expected action
  - "Metric achieved" - Performance or scale target met
  - "Integration complete" - Works with existing system

### Batch 2: Approach (after understanding the problem)

**Question 3:**
- Question: "What's the implementation approach?"
- Header: "Approach"
- Options:
  - "Extend existing" - Modify current code/components
  - "New component" - Create standalone module
  - "Replace existing" - Rewrite current solution

## Phase 3: Populate Spec Files

Using the gathered information, populate each file:

### requirements.md

Write requirements using EARS notation:
- `WHEN [condition] THE SYSTEM SHALL [behavior]`
- Include testable success criteria as checklist items

Example:
```markdown
## Success Criteria

WHEN a user submits the form with valid data
THE SYSTEM SHALL save the record and display confirmation

- [ ] Form validates required fields before submission
- [ ] Success message appears within 2 seconds
- [ ] Data persists after page refresh
```

### design.md

Document the approach and key decisions:
- High-level strategy
- Key technical decisions with rationale
- Components involved

### tasks.md

Break implementation into granular tasks:
- Group by phase (Setup, Implementation, Validation)
- Each task = one logical change
- Include testing tasks

### notes.md

Leave mostly empty - populated during implementation:
- Placeholder sections for Implementation Details and Learnings

## Completion

After populating the files:

1. Summarize what was created
2. Show the spec directory structure
3. Suggest next steps (e.g., "Run `/spec NNN` to start implementation")
