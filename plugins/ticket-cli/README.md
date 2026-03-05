# ticket-cli

Claude Code plugin for [ticket](https://github.com/wedow/ticket) (`tk`), a git-backed issue tracker for AI agents.

## What it does

- **SessionStart hook**: Detects if the current project has a `.tickets/` directory. If so, primes the session with `tk --help` output.
- **Skill**: Teaches Claude how to use `tk` for creating tickets, tracking blocking relationships between them, and organizing work.
