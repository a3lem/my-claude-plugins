# CLAUDE.md

This is a Claude Code plugin marketplace.

## Session Setup

- Load /plugin-dev:skill-development

## References

- Example marketplace: `~/.claude/plugins/marketplaces/claude-plugins-official/`
- Docs: https://code.claude.com/docs/en/plugins
- Marketplace docs: https://code.claude.com/docs/en/plugin-marketplaces

## Adding a Plugin

1. Create `<plugin-name>/` with `.claude-plugin/plugin.json`, commands/, skills/, etc.
2. Add entry to `.claude-plugin/marketplace.json` `plugins` array

## Shared Utilities (`bin/`)

Reusable scripts live in `bin/` at the repo root. When Claude Code installs a plugin, it only copies the plugin directory - not the marketplace repo root. So `../../bin/` won't exist in installed plugins. To use a shared utility from a plugin, symlink it into the plugin directory (e.g. `ln -s ../../bin/inject-rules plugins/my-plugin/hooks/inject-rules`) so it ships with the plugin on install.
