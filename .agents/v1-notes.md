# Spec-Driven Dev Plugin - Session Notes

## Date: 2024-12-24

## Key Decisions

### Command/Skill Naming
- Settled on consistent `/verb-spec` pattern: `specify-spec`, `design-spec`, `plan-spec`, `execute-spec`
- Merged `init-spec` into `specify-spec` (directory creation is just a prerequisite, not a separate phase)
- Renamed `implement-spec` to `execute-spec` for better flow: specify → design → plan → execute

### File Structure
- Kept separate files (requirements.md, design.md, tasks.md, notes.md) for ownership/editing rights model
- Only `design.md` is truly optional
- `notes.md` is a scratch pad available during ALL phases, not just execution

### Requirements Flexibility (In Progress)
- Current template is too rigid/ceremonial for all cases
- Agreed on: **Goal** + **Success Criteria** always required
- Success Criteria format varies by complexity:
  - Bug fix: simple checklist
  - Simple feature: bullet points
  - Complex behavior: EARS notation
  - Needs traceability: numbered REQ-NNN
- Other sections (Problem, Constraints, Testable Properties, Out of Scope) chosen based on context

### Kiro-Inspired Additions
- **Testable Properties**: Invariants derived from success criteria (lightweight version of property-based testing)
- **Verification step**: Before marking complete, check criteria and properties
- **Bidirectional refinement**: When verification fails, surface choice: fix implementation, adjust property, or refine requirement

### Editing Rules
- Each phase "owns" its file
- Changing upstream files (requirements, design) needs user confirmation from other phases
- `notes.md` can be edited freely by any phase

### Timestamps
- Learnings in `notes.md` should include date (YYYY-MM-DD) for context

### Numbered Requirements
- Use REQ-001, REQ-002 for traceability across design, tasks, and verification
- Only when complexity warrants it

## Insights from Martin Fowler Article

Source: https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html

Key critiques that apply to our approach:
1. **One-size-fits-all workflow** - A bug fix doesn't need elaborate requirements analysis
2. **Review overhead** - Lots of markdown files become tedious
3. **Functional vs technical confusion** - When to stay high-level vs add implementation details
4. **MDD parallel warning** - Risk of awkward abstraction level creating overhead

Our response:
- Make requirements.md flexible (minimal core + optional sections)
- Keep separate files but vary content depth
- design-spec already says "skip for simple features" - apply same thinking to specify-spec

## Still To Do

- [ ] Finalize specify-spec SKILL.md with flexible template (Goal + Success Criteria required, format varies, other sections as needed)
- [ ] Update spec-driven-development.md to reflect flexible requirements approach
- [ ] Consider if README needs updating for the flexible approach

## Anti-Patterns Identified

- **Over-specification** for simple changes
- **Premature formality** - using EARS/REQ-NNN when a checklist suffices
- **Feature speculation** - no speculative features; all phases have clear prerequisites
