# New Spec Reference

How to create a new spec (directory or compact file). This is the first step before gathering requirements.

## Monorepo Support

In monorepos, `specs/` folders may be placed at any level to keep them close to the project they relate to:

```
monorepo/
├── packages/
│   ├── frontend/
│   │   └── specs/           # Frontend-specific specs
│   └── backend/
│       └── specs/           # Backend-specific specs
├── apps/
│   └── web/
│       └── specs/           # Web app specs
└── specs/                   # Cross-cutting or repo-wide specs
```

**Determining specs location:**
1. If user provides a path, use that
2. If working in a subdirectory that has `specs/`, use that
3. If multiple `specs/` exist, ask user which to use
4. Default to repo root `specs/`

Use Glob to discover existing specs locations: `**/specs/`

## Process

### 1. Determine Specs Location & Next Number

**For root-level specs:**
```bash
sh scripts/next-spec-number.sh
```

**For nested specs (monorepo):**
```bash
sh scripts/next-spec-number.sh packages/frontend/specs
```

This outputs a zero-padded number (e.g., `001`, `002`, `014`). The script:
- Creates the specs directory if it doesn't exist
- Finds the highest existing `NNN-*` directory or `NNN-*.md` file
- Returns the next number

### 2. Get Description

If no description was provided with `/new`, use AskUserQuestion:
- "What feature or capability are you specifying?"
- Keep it brief (2-5 words ideal)

### 3. Choose Format

**Compact format** (single file) when:
- 1-2 functional requirements
- No design decisions needed
- Single session work
- Clear implementation path

**Directory format** when:
- 3+ requirements
- Design decisions needed
- Multi-session work
- Research/exploration required

If user requests compact explicitly or the feature is clearly simple, use compact. When in doubt, use directory format (can consolidate later).

### 4. Create Spec (Directory or Compact)

Slugify the description:
- Lowercase
- Replace spaces with hyphens
- Remove special characters
- Example: "User Authentication" → `user-authentication`

**For directory format:**
```bash
mkdir -p specs/NNN-slugified-description
```

**For compact format:**
```bash
touch specs/NNN-slugified-description.md
```

### 5. Do NOT Create Empty Files Yet

**For directory format:** Do not create markdown files at this point. The skill will:
1. Gather requirements through conversation
2. Only then write `requirements.md` with actual content

**For compact format:** Create the file only after gathering requirements, using `templates/compact.md`.

Creating empty templates leads to irrelevant boilerplate. Let the requirements phase produce the first real artifact.

### 6. Continue to Requirements Phase

After the spec location exists, proceed to [requirements.md](requirements.md) to gather and document requirements.

## Example Flows

**Directory format (complex feature):**
```
User: /new user authentication

1. Run: sh scripts/next-spec-number.sh → "003"
2. Description: "user authentication"
3. Assess: Multi-session, multiple requirements → directory format
4. Create: mkdir -p specs/003-user-authentication
5. Proceed to requirements gathering
```

**Compact format (simple fix):**
```
User: /new fix login button

1. Run: sh scripts/next-spec-number.sh → "004"
2. Description: "fix login button"
3. Assess: Single requirement, obvious fix → compact format
4. Gather requirements, then create: specs/004-fix-login-button.md
5. Use templates/compact.md
```

**Monorepo (nested specs):**
```
User: /new (working in packages/frontend/)

1. Check for existing specs: Glob **/specs/ → packages/frontend/specs/
2. Run: sh scripts/next-spec-number.sh packages/frontend/specs → "002"
3. Continue as above, creating in packages/frontend/specs/
```
