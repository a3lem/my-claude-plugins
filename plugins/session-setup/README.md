# session-setup

A plugin that contributes a single simple hook that fires on session startup. This hook instructs Claude to execute any steps you want to run before Claude starts responding.

*Example CLAUDE.md*:

```md
# CLAUDE.md

## Session Setup

Load skills /python-dev /ai-comments /ticket-issues
```

Claude will load the three skills in the example before responding to the user's first question.

