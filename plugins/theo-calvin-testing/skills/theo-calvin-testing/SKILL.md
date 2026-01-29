---
name: theo-calvin-testing
description: Differential testing with Theodore Calvin's framework (tc). Use when writing tc tests, reasoning about test scenarios, creating input/expected JSON pairs, or debugging test failures.
---

# Theodore Calvin's Testing Framework (tc)

> "In the AI age, specifications and tests are permanent while implementations are disposable."

## What is Differential Testing?

**Differential testing** compares actual output against expected output. No assertions, no matchers, no framework magic - just a diff.

## Philosophy

Tests are nothing more than a script that takes `input.json` and produces `output.json`, which is then diffed against `expected.json`. This simple model:

- Makes tests **language-agnostic** - the same test suite validates any implementation
- Separates **what** (the spec) from **how** (the implementation)
- Treats test suites as **specifications**, not just validation

## Core Concept

```
input.json → run → output.json ←→ diff ←→ expected.json
```

1. Your code reads `input.json` from stdin
2. Your code writes JSON to stdout
3. The framework compares output with `expected.json`

## JSON Comparison Rules

- **Objects are order-invariant** - `{"a":1,"b":2}` equals `{"b":2,"a":1}`
- **Arrays maintain order** - `[1,2,3]` does NOT equal `[3,2,1]`
- Comparison is deep and semantic, not string-based

## Directory Structure

```
tests/
└── my-test-suite/
    ├── run                    # Executable (any language)
    └── data/
        └── scenario-name/
            ├── input.json     # Test input
            └── expected.json  # Expected output
```

## The `run` Executable

The `run` file is any executable that:
1. Reads JSON from stdin
2. Writes JSON to stdout
3. Exit code 0 = success, non-zero = error

Example (bash):
```bash
#!/usr/bin/env bash
jq '.value * 2'
```

Example (python):
```python
#!/usr/bin/env python3
import json, sys
data = json.load(sys.stdin)
print(json.dumps({"result": data["value"] * 2}))
```

## Pattern Matching

For dynamic values, use patterns in `expected.json`:

| Pattern | Matches |
|---------|---------|
| `<uuid>` | UUID v4 format |
| `<timestamp>` | ISO 8601 datetime |
| `<number>` | Any number |
| `<string>` | Any string |
| `<boolean>` | true/false |
| `<any>` | Any value |
| `<null>` | null |

Example expected.json:
```json
{
  "id": "<uuid>",
  "created_at": "<timestamp>",
  "count": "<number>"
}
```

## Commands

```bash
tc                    # Run all tests in current directory
tc run path/to/suite  # Run specific suite
tc new path/to/suite  # Create new test suite scaffold
tc list               # List available test suites
tc tags               # Show available tags
tc explain suite      # Describe what a test does
tc --parallel         # Run tests in parallel
tc --tags=unit        # Filter by tag
```

## Creating a New Test

```bash
tc new tests/user-creation
```

This creates:
```
tests/user-creation/
├── run
└── data/
    └── basic/
        ├── input.json
        └── expected.json
```

## Best Practices

1. **One concept per test suite** - each `run` tests one thing
2. **Multiple scenarios per suite** - use `data/` subdirectories for variations
3. **Descriptive scenario names** - `data/empty-input/`, `data/unicode-handling/`
4. **Keep `run` minimal** - just wire input to your code and format output
5. **Use patterns for non-deterministic values** - timestamps, UUIDs, etc.

## Why This Approach

- **Portable**: Tests don't depend on any test framework or language
- **Diffable**: JSON diffs are clear and human-readable
- **AI-friendly**: Easy for AI to generate and verify tests
- **Implementation-agnostic**: Rewrite in any language, tests still pass

## Reference

- Repository: https://github.com/ahoward/tc
- Requires: bash 4.0+, jq
