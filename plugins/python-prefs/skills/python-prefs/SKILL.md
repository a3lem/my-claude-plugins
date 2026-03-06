---
name: python-prefs
description: This skill should be used when writing, reviewing, or refactoring Python code in any project. It defines coding preferences and conventions that apply to both AI and human developers. Load this skill whenever Python code is being produced or evaluated.
---
# Python Preferences

Coding preferences and conventions for writing Python. These apply universally -- whether the code is written by a human or an AI agent.

## Project Management

Use **uv** (by astral.sh) for all Python project management: virtual environments, dependency installation, and Python version management.

Use **uvx** for running Python-based CLI tools (linters, formatters, type checkers) without installing them into the project.

## Tooling

When developing, testing, or reviewing code, consult `references/TOOLING.md` for the preferred tool choices.

## Code Style

All code style conventions are documented in `references/STYLE.md`. Load it when writing or reviewing Python code.

The most critical conventions at a glance:

- **Type everything.** All code must be type-hinted. Alias the typing module as `T` (`import typing as T`). Never use `T.Any`.
- **Modern Python.** Target 3.12+. Use builtin generics (`list[str]`, not `T.List[str]`).
- **Structural typing.** Prefer `T.Protocol` over abstract base classes. No `abc` -- this isn't Java.
- **No silent errors.** Handle all errors with specific exception types. Critical exceptions crash the program. Error branches must not fabricate data.
- **No fake defaults.** Never assume default values with `dict.get()` -- handle the `None` case explicitly.
- **Strict fields.** Do not make class fields nullable/optional without a comment motivating the choice.
- **Loguru** for application logging (unless the project already uses something else).

For the full set of conventions, read `references/STYLE.md`.
