---
name: better-comments
description: >-
  This skill should be used when the user asks to "write better comments",
  "add AI comments", "add provenance comments", "use [AI] markers",
  "improve code comments", "add context to comments", or when generating
  or modifying code that warrants meaningful comment blocks.
  Teaches Claude to write structured, reviewer-facing comment blocks
  with provenance, context, intent, and assumptions.
---

# Better Comments

Write code comments that are meaningful to human reviewers and useful to other AIs.
Include a brief comment block above each generated function, class, or logically distinct section.

Skip comment blocks for trivial changes (typo fixes, renames, formatting, one-liners).

When modifying code that already has an `[AI]` comment block, update it in place — replace the old block with one reflecting the current state, don't append.

## Elements of a Good Comment

| Field | Required | Purpose |
|-------|----------|---------|
| Provenance | Yes | `# [AI]` marker on the first line |
| Context | Yes | Reference the issue/ticket/task ID, task summary, or journal entry that motivated this change |
| Intent | Yes | Why the code was added or modified |
| Assumptions | If any | So the reviewer can validate them |
| Logic | Optional | How it works, only if non-obvious from the code itself |

### Example

```py
# [AI]
# Context: TASK-42 (add retry logic to GCS uploads)
# Intent: prevent transient failures from dropping documents
# Assumes: GCS client raises google.api_core.exceptions.ServiceUnavailable on transient errors
```

## Comments vs Docstrings

`[AI]` blocks are for **code reviewers**, not API consumers. Place them as `#` comments, never inside docstrings.

| Location | Use `#` comment block | Use docstring |
|----------|-----------------------|---------------|
| Module top-level | The `[AI]` block IS the module docstring — acceptable as the sole content | — |
| Function / method | `# [AI]` block **above** the `def` | Docstring inside the `def` for public API description (args, return, behaviour) |
| Class | `# [AI]` block **above** the `class` | Docstring inside for public description |

Docstrings are API-facing: they appear in `help()`, IDEs, and generated docs. The `[AI]` provenance block is internal reviewer context and must not pollute them.

## Inline Logic Comments

Beyond the `[AI]` block, add short inline comments when the reader needs non-local context to understand correctness:

- **Stack/queue mechanics**: what's pushed and popped, what invariant the structure maintains
- **Index juggling**: when code indexes into multiple structures, clarify which index refers to what
- **Nullability**: when a value can be None and it's not obvious why it's safe to use here
- **Non-obvious control flow**: early returns guarded by a condition established elsewhere, or loops with subtle exit conditions
- **Quiet mutation**: when a variable is reassigned or a structure is mutated in place and a reader scanning linearly might miss it

## Adapting to Context

When no issue, ticket, or task ID is available for the Context field, use a brief task summary instead:

```py
# [AI]
# Context: user request to add CSV export
# Intent: stream rows to avoid loading full dataset in memory
```

## Language-Specific Syntax

Adapt the comment marker to the language:

| Language | Comment syntax |
|----------|---------------|
| Python, Ruby, Shell | `# [AI]` |
| JavaScript, TypeScript, Java, C, Go, Rust | `// [AI]` |
| HTML, XML | `<!-- [AI] -->` |
| CSS | `/* [AI] */` |
| SQL | `-- [AI]` |
