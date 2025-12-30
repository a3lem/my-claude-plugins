# Design Phase Reference

How to create and refine architectural decisions for a specification.

## Mode Detection

- If `design.md` doesn't exist → **Create mode**
- If `design.md` exists → **Refine mode** (update based on instruction)

## When to Use

Use this phase for:
- Features with multiple valid implementation approaches
- Architectural decisions that need user input
- Complex integrations or trade-offs

Skip for simple features, bug fixes, or obvious implementations.

## Process

### 1. Load Context

Read the spec's `requirements.md` to understand:
- Problem being solved
- Success criteria to satisfy
- Constraints to respect

If refining, also read existing `design.md`.

### 2. Explore Approach

In **Create mode**: Use AskUserQuestion to explore:
- High-level implementation strategy
- Key architectural choices
- Trade-offs between approaches

In **Refine mode**: Apply the user's instruction to existing design.

**Capturing research:** If exploration yields insights too incidental for design.md (e.g., explored files, rejected approaches, useful links), record them in `notes/research.md`.

### 3. Write design.md

Use template from `templates/design.md`.

Document decisions and rationale:
- **Approach** - High-level implementation strategy
- **Decisions** - Table of choices with rationale
- **Risks** - Potential issues and mitigations

### Optional Sections

Include when relevant to the feature:
- **Architecture** - Component structure, layers
- **Data Flow** - How data moves through the system
- **Interfaces** - API contracts, function signatures
- **Data Models** - Schemas, types, entities
- **Error Handling** - Failure modes, recovery strategies
- **Testing Strategy** - What to test, how to test

### 4. Cascade Warning (Refine mode only)

If design changed significantly, warn user that tasks may need updating.
