---
name: frontmatter
description: |
  Manage AI provenance metadata blocks in source files. Use to stamp files with
  review status and rule references, or scan directories for coverage. Triggers on:
  "stamp", "frontmatter", "ai-frontmatter", "mark as reviewed", "scan reviewed".
version: 0.1.0
---

# AI Frontmatter Skill

Manage `/// ai` metadata blocks in source files to track provenance: which files have been human-reviewed, which carry rule references, and which are raw AI output.

## Block Format

Inspired by [PEP 723](https://peps.python.org/pep-0723/) inline metadata. The block uses the file's comment character (`CC`) as a prefix:

```
{CC} /// ai
{CC} human_reviewed = false
{CC} rules = [".claude/rules/python.md"]  # (Optional. May also be a string.)
{CC} skills = ["ai-frontmatter"]           # (Optional.)
{CC} ///
```

Where `{CC}` is `#` for Python/Shell/YAML, `//` for JS/TS/Go/Rust/Java/C, etc.

### Fields

| Field | Type | Required | Default |
|-------|------|----------|---------|
| `human_reviewed` | bool | yes | `false` |
| `rules` | string array | no | omitted |
| `skills` | string array | no | omitted |
| `access` | string (`"write"`, `"read"`, `"hidden"`) | no | `"write"` |

- `human_reviewed`: whether a human has read and approved the file contents.
- `rules`: paths to rule files (relative to repo root) that the agent should consult when modifying this file.
- `skills`: skill names that agents must load (if not already loaded) before working in this file.
- `access`: controls whether AI agents may read or write the file. `"write"` = full access (read and write), `"read"` = read-only, `"hidden"` = no access. **If the field is absent, assume `"write"`** — this keeps all existing files fully accessible without needing updates.

### Placement

The block is inserted **after** any shebang or encoding declaration lines, followed by a blank line before the rest of the file content.

## Agent Rules

1. **MUST NOT** set `human_reviewed = true`. Only humans may do this.
2. **Absence** of a block means the file is unreviewed (`human_reviewed = false`) and fully accessible (`access = "write"`).
3. When pattern-matching or learning from existing code, **prefer** files with `human_reviewed = true`.
4. When modifying a file that has `human_reviewed = true`, **reset it to `false`** — your edit invalidates the review.
5. When creating new files, **stamp them** with `human_reviewed = false`.
6. **MUST NOT** modify or delete a file with `access = "read"`.
7. **MUST NOT** read, modify, or delete a file with `access = "hidden"`.
8. **MUST NOT** relax `access` (e.g. change `"read"` → `"write"`). Only humans may do that.
9. **MAY** tighten `access` (e.g. stamp a new file with `access = "read"`).

### Authority Hierarchy

When multiple files show different patterns, trust them in this order:

1. `human_reviewed = true` — highest trust
2. `human_reviewed = false` with `rules` — guided AI output
3. `human_reviewed = false` without `rules` — raw AI output
4. No block at all — unknown provenance. Notify user so that they can update the frontmatter.

## CLI Usage

### `stamp` — Add or update a frontmatter block

```bash
${CLAUDE_PLUGIN_ROOT}/skills/frontmatter/scripts/frontmatter.py stamp <file> \
  [--reviewed true|false] \
  [--rules path1,path2] \
  [--skills skill1,skill2] \
  [--access write|read|hidden] \
  [--comment-char CC]
```

- `--reviewed` defaults to `false`
- `--comment-char` auto-detected from file extension; use flag to override
- Idempotent: running twice produces the same output
- Replaces existing block if present; inserts after shebang/encoding if not

**Examples:**

```bash
# Stamp a Python file (auto-detects #)
${CLAUDE_PLUGIN_ROOT}/skills/frontmatter/scripts/frontmatter.py stamp libs/internal/foo/bar.py

# Stamp with rules
${CLAUDE_PLUGIN_ROOT}/skills/frontmatter/scripts/frontmatter.py stamp src/main.py \
  --rules .claude/rules/python.md,.claude/rules/trust.md

# Stamp as read-only
${CLAUDE_PLUGIN_ROOT}/skills/frontmatter/scripts/frontmatter.py stamp src/main.py --access read

# Human marks a file as reviewed
${CLAUDE_PLUGIN_ROOT}/skills/frontmatter/scripts/frontmatter.py stamp src/main.py --reviewed true

# Override comment char for an unusual extension
${CLAUDE_PLUGIN_ROOT}/skills/frontmatter/scripts/frontmatter.py stamp config.conf --comment-char "#"
```

### `scan` — Report frontmatter coverage

```bash
${CLAUDE_PLUGIN_ROOT}/skills/frontmatter/scripts/frontmatter.py scan \
  [--path .] \
  [--ext py,sh,ts,tsx,js,go]
```

- Uses `git ls-files` to respect `.gitignore`
- Groups results by directory
- Shows per-directory and total counts: stamped (reviewed / unreviewed) and unstamped

**Examples:**

```bash
# Scan entire repo for default extensions
${CLAUDE_PLUGIN_ROOT}/skills/frontmatter/scripts/frontmatter.py scan

# Scan only Python files in libs/
${CLAUDE_PLUGIN_ROOT}/skills/frontmatter/scripts/frontmatter.py scan --path libs/ --ext py

# Scan TypeScript files
${CLAUDE_PLUGIN_ROOT}/skills/frontmatter/scripts/frontmatter.py scan --ext ts,tsx
```

### Extension → Comment Character Map

| Extensions | CC |
|---|---|
| py, sh, bash, yaml, yml, toml, r, rb, pl | `#` |
| js, ts, tsx, jsx, go, rs, java, c, cpp, h, hpp, cs, swift, kt | `//` |


## Special case: Markdown

In Markdown, use YAML frontmatter instead of comments.

```
ai:
  human-reviewed: true
```
