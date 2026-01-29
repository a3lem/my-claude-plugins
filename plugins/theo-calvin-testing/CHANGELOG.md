# Changelog

## [1.0.0] - 2026-01-29

Initial release of the theo-calvin-testing plugin.

### Added

- **SKILL.md** covering differential testing concepts:
  - Core philosophy: `input.json → run → output.json ←→ expected.json`
  - JSON comparison rules (objects order-invariant, arrays maintain order)
  - Directory structure and `run` executable format
  - Pattern matching for dynamic values (`<uuid>`, `<timestamp>`, etc.)
  - Command reference (`tc`, `tc new`, `tc list`, etc.)
  - Best practices for writing tests

### Reference

- Based on Theodore Calvin's testing framework: https://github.com/ahoward/tc
