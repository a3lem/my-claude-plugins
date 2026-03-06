---
name: task-management
description: >
  This skill should be used when the user asks to "create a ticket", "add a task",
  "track an issue", "manage dependencies", "show blocked tickets", "list open tickets",
  "close a ticket", "add notes to a ticket", "link tickets", "query tickets",
  "what's ready to work on", "what's blocking", "break down an epic",
  or any task management operation using the `tk` CLI. Also triggers when the user
  mentions "tk", "ticket system", ".tickets", or asks about project task organization.
version: 0.1.0
---

# tk - CLI Ticket System

`tk` is a git-backed issue tracker storing markdown files with YAML frontmatter in `.tickets/`. Tickets are plain files, making them searchable, diffable, and easy for AI agents to work with.

## Core Concepts

- **Ticket IDs**: Format `prefix-hexsuffix` (e.g., `nw-5c46`). The prefix comes from the directory name. Partial ID matching works everywhere (suffix, prefix, or substring).
- **Ticket files**: Markdown with YAML frontmatter at `.tickets/<id>.md`
- **Statuses**: `open` -> `in_progress` -> `closed` (also `reopen` back to `open`)
- **Priority**: 0-4, where 0 is highest. Default is 2.
- **Types**: `bug`, `feature`, `task`, `epic`, `chore`. Default is `task`.
- **Dependencies**: Directed edges - "A depends on B" means B blocks A
- **Links**: Symmetric relationships between related tickets

## Command Reference

### Creating Tickets

```bash
tk create "Title" [-d "description"] [-t type] [-p priority] [-a assignee]
                   [--design "notes"] [--acceptance "criteria"]
                   [--parent <id>] [--tags tag1,tag2] [--external-ref gh-123]
```

Creates a ticket and prints its ID. The `.tickets/` directory is created automatically on first use. Assignee defaults to `git config user.name` if not specified.

### Status Management

```bash
tk start <id>              # Set to in_progress
tk close <id>              # Set to closed
tk reopen <id>             # Set back to open
tk status <id> <status>    # Set arbitrary status (open|in_progress|closed)
```

### Viewing Tickets

```bash
tk show <id>               # Full ticket details with blockers, children, links
tk edit <id>               # Prints file path (use Read to view/edit)
```

`show` enriches output with computed sections: Blockers (unclosed deps), Blocking (tickets depending on this one), Children (tickets with this as parent), and Linked tickets.

### Listing Tickets

```bash
tk ls [--status=X] [-a assignee] [-T tags]   # List tickets with optional filters
tk ready [-a X] [-T X]                         # Open/in-progress with all deps resolved
tk blocked [-a X] [-T X]                       # Open/in-progress with unresolved deps
tk closed [--limit=N] [-a X] [-T X]           # Recently closed (default 20)
```

- `ready` shows tickets sorted by priority (P0 first), then by ID. These are actionable tickets.
- `blocked` shows tickets with unclosed dependencies, listing only the unclosed blockers.
- All listing commands show format: `<id> [P<n>][status] - Title <- [dep1, dep2]` (e.g., `nw-5c46 [P2][open] - Add login endpoint <- [nw-3a21]`)

### Dependencies

```bash
tk dep <id> <dep-id>       # Add dependency (id depends on dep-id)
tk undep <id> <dep-id>     # Remove dependency
tk dep tree [--full] <id>  # Show dependency tree (--full disables dedup)
tk dep cycle               # Find dependency cycles in open tickets
```

Dependencies are idempotent - adding an existing one is a no-op. The dependency tree uses box-drawing characters and sorts children by subtree depth (deepest last), then by ID.

### Links

```bash
tk link <id> <id> [id...]  # Link tickets together (symmetric, all-pairs)
tk unlink <id> <target-id> # Remove link between two tickets
```

Links are symmetric - linking A to B also links B to A. Linking 3+ tickets creates all-pairs links. Idempotent.

### Notes

```bash
tk add-note <id> "text"    # Append timestamped note
echo "text" | tk add-note <id>  # Pipe via stdin
```

Notes are appended under a `## Notes` section with ISO timestamps.

### JSON Export

```bash
tk query                   # All tickets as JSONL
tk query '.status == "open"'  # Filtered with jq expression (requires jq)
```

Each JSONL line contains fields: `id`, `title`, `status`, `priority`, `type`, `assignee`, `deps`, `links`, `tags`, `parent`, `created`.

### Plugin System

External executables named `tk-<cmd>` or `ticket-<cmd>` in PATH are invoked automatically. Use `tk super <cmd>` to bypass plugins and run built-in commands directly.

## Workflow Patterns

### Starting Work on a Project

```bash
tk ready                   # See what's actionable
tk start <id>              # Mark ticket as in-progress
# ... do the work ...
tk close <id>              # Mark done
```

### Breaking Down Work

```bash
parent=$(tk create "Epic: Build auth system" -t epic)
child1=$(tk create "Design auth schema" --parent "$parent")
child2=$(tk create "Implement login endpoint" --parent "$parent")
tk dep "$child2" "$child1"   # Implementation depends on design
```

### Checking Progress

```bash
tk blocked                 # What's stuck?
tk dep tree <epic-id>      # Visualize the dependency graph
tk closed --limit=5        # What was recently completed?
```

### Reading Ticket Files Directly

Since tickets are plain markdown at `.tickets/<id>.md`, use Read or Grep to inspect them directly when bulk operations are needed. The YAML frontmatter contains all metadata fields.

## Important Behaviors

- **Directory resolution**: `tk` walks parent directories to find `.tickets/`, so it works from any subdirectory.
- **TICKETS_DIR env var**: Overrides directory resolution when set.
- **Partial IDs**: Work everywhere. Exact match takes precedence over partial. Ambiguous partials produce an error listing matches.
- **Idempotent operations**: `dep` and `link` are safe to repeat.
- **No `.tickets/` directory**: Read commands fail with "no .tickets directory found". `tk create` auto-creates it.
