# Python Code Style

## Type Hints

- All code MUST be type hinted
- Alias the typing module as `T` when importing: `import typing as T`
- Do not use `typing.Any` - it defeats type safety:
  - Example: `dict[str, T.Any]` is a code smell.
- Write modern Python (3.12+) using builtin generics (e.g., `list[str]` not `T.List[str]`)
- Prefer structural typing over nominal typing - use Protocols, not abstract base classes
- Place type-checking-only imports inside `if T.TYPE_CHECKING:` blocks

## Imports

- Imports belong at the top of the module
- AVOID placing imports inside function bodies
- Exception: imports that risk circular dependencies may be placed locally

## Style Principles

- Avoid indirection unless clearly motivated
- Prefer composition over inheritance (unless a library's API prefers inheritance)
- Naming conventions:
  - `idx` = index (zero-based)
  - `nr` = number (often one-based)
- Error handling:
  - Use specific exception types, not bare `Exception`
  - Critical exceptions SHOULD crash the program
  - Error branches must NOT create fake data to compensate for missing data
- NEVER assume default values with `dict.get()` -- handle the `None` case explicitly
- Prefer the standard library over adding dependencies
- Do not make all fields of a class nullable/optional. This introduces headaches later. Prefer being strict.
  - If you must allow None, add a comment to motivate the choice.

## Logging

- Logging statements should show values that are inexpensive to compute
- Use multiline string literals for multiline outputs, NOT rows of `print()` statements

When working on applications or service code:

- Use **loguru** as the logging library, unless a different logging library is already used.
