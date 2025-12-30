# Tasks Phase Reference

How to create the implementation plan and track progress.

## What tasks.md Contains

Tasks.md combines implementation planning with progress tracking:

| Section | Purpose |
|---------|---------|
| **Plan** | Implementation phases, file changes, code patterns |
| **Checklist** | Progress tracking with requirement references |

**Plan section** is the tactical breakdown - HOW to implement the design.

**Checklist section** is the status tracker - enables resuming across sessions.

## What Belongs in tasks.md

| tasks.md Contains | NOT in tasks.md (lives elsewhere) |
|-------------------|-----------------------------------|
| Implementation phases | Goal/problem (requirements.md) |
| File paths and changes | Solution approach (design.md) |
| Code transformation patterns | Acceptance criteria (requirements.md) |
| Sequencing and dependencies | Architectural decisions (design.md) |
| Progress checklist | - |

## Process

### 1. Load Context

Read the spec directory:
- `requirements.md` - What we're building (FR-/NFR-)
- `design.md` - Architectural approach (if exists)

### 2. Explore the Codebase

Before planning, understand:
- Existing patterns and conventions
- Files that will be affected
- Dependencies between components

**Capturing exploration:** If codebase exploration yields insights too incidental for tasks.md (e.g., file index, architectural observations, potential gotchas), record them in `notes/research.md`.

### 3. Write tasks.md

Use template from `templates/tasks.md`.

**What makes a plan actionable:**

- **Exact file paths** - Full paths, not vague references
- **Specific locations** - Line numbers or function names
- **Before/after patterns** - Show the transformation
- **Explicit sequencing** - Which changes must happen first
- **Phase boundaries** - Clear groupings of related changes

**Common gaps to avoid:**

- Ambiguous sequencing ("then update the rest")
- Vague locations ("somewhere in the file")
- Missing config/build file updates
- No mention of dependencies between phases

### 4. Create Checklist

Add checklist items that map to the plan phases:
- Use checkboxes: `- [ ]` pending, `- [x]` complete
- Mark current item with `[NEXT]`
- **Every task MUST reference the requirement(s) it satisfies** using `_[FR-001.1]_` format
- Final item should be verification

**Traceability is mandatory.** If a task doesn't trace to a requirement, either:
1. The requirement is missing → add it to requirements.md first
2. The task is out of scope → remove it

**Example:**
```markdown
## Checklist

- [x] Create user model _[FR-001.1]_
- [ ] [NEXT] Add authentication endpoint _[FR-002.1, FR-002.2]_
- [ ] Implement session management _[FR-003.1]_
- [ ] Verify all acceptance criteria _[FR-*, NFR-*]_
```

### 5. Get User Approval

Present the plan to the user before proceeding to execution. The tasks phase ends here - do NOT begin implementing until the user explicitly requests execution.

## During Execution

Update `tasks.md` as work progresses:
- Check off completed items in the checklist
- Move `[NEXT]` marker to current item
- Add items if plan evolves
- Update Plan section for significant changes
