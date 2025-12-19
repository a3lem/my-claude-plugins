# Spec-Driven Development

This reference describes the spec-driven development approach used by this plugin.

## Core Principle

Specifications are the source of truth. Implementation follows from specs, not the other way around. This inverts the typical flow where code is written first and documentation (if any) follows.

## Benefits

- **Session persistence** - Specs survive context boundaries; work can resume days later
- **Reduced drift** - Requirements and implementation stay aligned
- **Testable outcomes** - EARS notation produces verifiable success criteria
- **Decision traceability** - Design rationale is captured, not lost

## Spec Lifecycle

```
Idea → Requirements → Design → Tasks → Implementation → Completion
         ↑              ↑        ↑            ↑
         └──────────────┴────────┴────────────┘
                    (refinement as needed)
```

Specs are living documents. Update them as understanding evolves, but changes to requirements should be explicit and confirmed.

## File Responsibilities

| File | Question Answered | When to Update |
|------|-------------------|----------------|
| `requirements.md` | What are we building? | Scope changes (confirm first) |
| `design.md` | How will we build it? | Architectural decisions change |
| `tasks.md` | What's the plan/progress? | Continuously during implementation |
| `notes.md` | What did we learn? | Discoveries during implementation |

## Key Conventions

### Requirements First

Define success criteria before implementation. Use EARS notation for clarity:
- Ubiquitous: `THE SYSTEM SHALL [action]`
- Event-driven: `WHEN [trigger] THE SYSTEM SHALL [response]`
- State-driven: `WHILE [state] THE SYSTEM SHALL [behavior]`

### Design Documents Decisions

Capture the "why" alongside the "what":
- What approach was chosen
- What alternatives were considered
- Why this choice was made

This prevents re-litigating decisions and helps future maintainers.

### Granular Tasks

Break work into small, trackable units:
- One logical change per task
- Checkable as complete or not
- Ordered by dependency when possible

### Implementation Notes Are for Surprises

Don't document the obvious. Capture:
- Unexpected behaviors discovered
- Gotchas for future reference
- Deviations from the original design (and why)

## Anti-Patterns

- **Spec-after-the-fact** - Writing specs to document existing code defeats the purpose
- **Over-specification** - Specs should guide, not constrain every detail
- **Stale specs** - Specs that diverge from implementation lose value; keep them synchronized
- **Premature tasks** - Don't break down tasks until the design is clear

## References

This approach draws from:
- [Kiro Specs](https://kiro.dev/docs/specs/concepts/) - Three-file spec structure, EARS notation
- [GitHub Spec-Kit](https://github.com/github/spec-kit) - Specification as source of truth, constitutional principles
