# a3lem's Claude Code Plugins

Personal collection of Claude Code plugins, published as a marketplace.

## Plugins

- **[spec-driven-dev](plugins/spec-driven-dev)** - Spec-driven development with Gherkin scenarios, reference/changes separation, and structured archive flow.
- **[basedpyright-lsp](plugins/basedpyright-lsp)** - Enables the basedpyright LSP server for Python type checking.
- **[python-prefs](plugins/python-prefs)** - Python coding preferences and conventions.
- **[theo-calvin-testing](plugins/theo-calvin-testing)** - Differential testing with `tc`: input.json to output.json, diffed against expected.json.
- **[session-setup](plugins/session-setup)** - Runs Session Setup steps from CLAUDE.md on session start.
- **[ticket-cli](plugins/ticket-cli)** - Integration for [`tk`](https://github.com/wedow/ticket), a git-backed issue tracker for AI agents.
- **[auto-memory](plugins/auto-memory)** - Clone of Claude's built-in auto-memory, but stores memories in the project directory instead of `~/.claude/`.
- **[frontmatter](plugins/frontmatter)** - Use frontmatter in code files to track human review and set (soft) access controls for AI.
- **[better-comments](plugins/better-comments)** - Comment blocks that state their AI origin and focus on context, intent, and assumptions -- the "why", not the "what".
- **[project-notes](plugins/project-notes)** - Working knowledge in `notes/`, structured decision log, and timestamped journal entries.
- **[project-knowledge](plugins/project-knowledge)** - Routes knowledge to the right store based on contract strength.

## Knowledge Ecosystem

Three plugins work together to manage project knowledge:

| Store | Plugin | Contract | Purpose |
|-------|--------|----------|---------|
| `specs/` | spec-driven-dev | Strongest | Behavioral truth — Gherkin scenarios, verified before shipping |
| `docs/` | *(none needed)* | Strong | Durable reference — maintained, authoritative |
| `notes/DECISIONS.md` | project-notes | Medium | What was decided — concise `dcn-xxxx` entries |
| `notes/` | project-notes | Weak | Working knowledge — may go stale |
| `notes/journal/` | project-notes | Weakest | Timestamped snapshots — decay over time |

**project-knowledge** provides routing rules for deciding where information should live and where to look for it.
