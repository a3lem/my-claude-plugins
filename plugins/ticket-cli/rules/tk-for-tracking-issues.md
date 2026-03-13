# `tk` - CLI for plain text task management

This project uses `tk` (ticket) to track issues as plain text files committed alongside code. Tickets are markdown with YAML frontmatter in `.tickets/`.

Use `Bash(tk ...)` for project work tracking instead of `Todo*(...)`. `TodoWrite`/`TodoRead` are still fine for ephemeral scratch notes, but actual issue tracking belongs in `tk`. If `tk` is not found on `PATH`, fall back to `Todo*` silently.

**Before starting any multi-step task**, check if a ticket already exists:

- `tk ready && tk blocked` to see all open work
- `tk query-all 'select(.title | test("keyword"; "i"))'` to search by title

If a matching ticket exists, use it. If not, create one. Trivial one-shot changes (single-line fix, typo, quick rename) don't need a ticket.

Each `tk` call should be a separate Bash tool invocation. Use the printed ID from `tk create` in subsequent commands.

## Things `--help` Won't Tell You

### No command for updating title, priority, assignee, tags, type, or description

Many commands mutate ticket files: `start`/`close`/`reopen` change status, `dep`/`undep` change dependencies, `link`/`unlink` change associations, `add-note` appends content. But there is no `tk update` for the remaining fields. To change a ticket's title, priority, assignee, tags, type, or description, edit `.tickets/<id>.md` directly using Read and Edit. The file format:

```markdown
---
id: nw-5c46
status: open
priority: 1
type: bug
assignee: maria
deps: [nw-3a21]
tags: [api, urgent]
---
# Ticket title goes here

Description body (plain markdown).
```

### Cancelling a ticket

There is no `cancel` command. Close the ticket and add a note: `tk close <id>` + `tk add-note <id> "Cancelled: <reason>"`.

### `query` vs `query-all` - different schemas

Both output JSONL (one JSON object per line, not an array). The jq filter argument is applied to each object individually - write expressions like `select(...)`, not `.[] | select(...)`.

`query` is lightweight but **omits `title` and `body`**. Use it for status/priority/type filtering:

```bash
tk query 'select(.status == "open" and .type == "bug")'
```

`query-all` includes `title` and `body`. Use it when you need to search by text:

```bash
tk query-all 'select(.title | test("login"; "i"))'
```

**Type gotcha:** `query` encodes priority as a string (`"1"`), `query-all` as an integer (`1`). Match accordingly:

```bash
tk query 'select(.priority == "0")'       # string in query
tk query-all 'select(.priority == 0)'     # int in query-all
```

### Parents, deps, and links are three different relationships

- **Parent-child** (`--parent <id>`) models hierarchy: epic → feature → task. A ticket has at most one parent. Use this for decomposition ("this task is part of that epic").
- **Dependencies** (= blocking; `tk dep A B`) model execution order: A can't start until B is done. Use this for sequencing ("implement OAuth after designing the schema").
- **Links** (`tk link A B`) are symmetric associations with no semantics. Use this for "related to" relationships.

### `dep tree` follows dependency edges only

`dep tree <id>` shows what `<id>` depends on, transitively. It does **not** traverse parent-child relationships. To see an epic's children, use `tk show <epic-id>` which has a computed Children section.

### `show` computes reverse relationships

`tk show <id>` enriches the raw ticket with sections not in the file: **Blockers** (unclosed deps), **Blocking** (reverse deps), **Children** (tickets with this as parent), **Linked** (symmetric links). This is the best way to understand a ticket's context.

## Workflow Example

User: "The login page times out after 5 seconds, it should be 30."

1. Check for existing tickets: `tk ready && tk blocked`
2. No match. Create one: `tk create "Fix login timeout (5s -> 30s)" -t bug -p 1`
   → prints `nw-a3f1`
3. Start work: `tk start nw-a3f1`
4. Fix the code
5. Close the ticket: `tk close nw-a3f1`

## Breaking Down Work

Create the epic first, then children with `--parent <epic-id>`, then wire dependencies:

```bash
tk create "Auth system" -t epic           # → nw-0001
tk create "Design schema" --parent nw-0001  # → nw-0002
tk create "Implement OAuth" --parent nw-0001  # → nw-0003
tk dep nw-0003 nw-0002                    # OAuth depends on schema
```

## Command Reference

Run `tk --help` for the full list. Key details not obvious from the help text:

- `tk ls` accepts `--status=X`, `-a X`, `-T X` for filtering by status, assignee, and tag. `ready` and `blocked` accept `-a` and `-T`.
- `ready` = open tickets with all deps resolved, sorted by priority. `blocked` = open tickets with unclosed deps. Together they cover all open work.
- Always pass `-a claude` when creating tickets.
- `tk tags` lists all tags by frequency with up to 3 associated ticket IDs.
- Listing format: `<id> [P<n>][status] - Title <- [dep1, dep2]`
- `dep` and `link` are idempotent.
- Partial IDs work everywhere. Ambiguous partials error with a list of matches.
- `tk` walks parent directories to find `.tickets/`, works from any subdirectory.
- Archived tickets live in `.tickets/archive/`.
