---
name: python-project-management
description: Python project and dependency management guidelines. Use when setting up Python projects, managing dependencies, or running Python tooling.
---

# Python Project Management

## Package and Environment Management

Use **uv** (by astral.sh) for all Python project management:
- Virtual environment creation and management
- Dependency installation and resolution
- Python version management

Use **uvx** for running Python-based tooling (e.g., linters, formatters, type checkers).

## Key Principles

- Prefer uv over pip, pipenv, or poetry for new projects
- Always work within a virtual environment
- Pin dependencies with version constraints in `pyproject.toml`
- Use `uv lock` to generate reproducible lockfiles
