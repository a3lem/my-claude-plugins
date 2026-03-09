# Critique Reference

Detailed checklists and exploration patterns for the spec-critic agent.

## Intra-Spec Mode: Coherence Within the Spec

Checks for contradictions and coherence within a single spec.

### Specification Checklist

| Check | What to Look For |
|-------|-----------------|
| Notation correct | SHALL statements use EARS qualifiers; Given/When/Then structure consistent |
| No ambiguity | Avoid: should, could, might, usually, quickly, properly |
| Testability | Each scenario is specific and verifiable |
| Completeness | Happy path and error cases covered |
| Edge cases | Boundary conditions documented |
| Internal consistency | Scenarios don't contradict each other |
| Terminology | Same concept uses same term throughout |
| ADDED/MODIFIED/REMOVED | Delta spec sections are accurate (for change specs) |

### Proposal Checklist

| Check | What to Look For |
|-------|-----------------|
| Motivation | Clear problem statement, not just "we want X" |
| Context | Current state described accurately |
| Scope | Out-of-scope items listed to prevent creep |
| Constraints | Technical/business limitations documented |

### Design Checklist

| Check | What to Look For |
|-------|-----------------|
| Coverage | All scenarios are addressed |
| Rationale | Decisions have documented reasoning |
| Alignment | Decisions don't contradict spec scenarios |
| Risks | Potential issues identified with mitigations |
| Feasibility | Proposed approach is technically sound |

### Cross-File Checklist

| Check | What to Look For |
|-------|-----------------|
| Scope alignment | proposal → spec → design → tasks.md tell consistent story |
| No drift | Design doesn't add features not in spec |
| Tasks alignment | tasks.md (if present) covers spec scope without additions |
| Terminology | Consistent across all files |

---

## Spec-Code Mode: Alignment with Codebase

Checks that spec assumptions match codebase reality.

### Exploration Patterns

**Find project rules:**
```
Glob: **/CLAUDE.md
Glob: **/.claude/rules/**
Glob: **/.claude/settings.json
```

**Verify files exist:**
```
# Extract paths from design.md
# For each path: Glob to verify existence
```

**Check existing patterns:**
```
# For each referenced function/class:
Grep: "def {function_name}" or "class {class_name}"
# Read the file, verify behavior matches assumption
```

**Understand conventions:**
```
# Find similar code in codebase
Grep: pattern from design
# Compare style, naming, structure
```

### Assumptions to Validate

| Assumption Type | How to Validate |
|-----------------|-----------------|
| "File X exists" | Glob for the file |
| "Function Y does Z" | Read the function, verify behavior |
| "Module uses pattern P" | Read module, check pattern |
| "API returns shape S" | Find API definition, verify |
| "Config has option O" | Read config file |

### Convention Checks

| Convention | Where to Find |
|------------|---------------|
| Code style | Existing files in same directory |
| Naming | CLAUDE.md, existing code |
| Error handling | Similar features in codebase |
| Testing approach | Existing test files |
| Documentation | Existing docstrings/comments |

### Red Flags

- Design references files that don't exist
- Design assumes behavior that code doesn't have
- Plan ignores existing implementation of same feature
- Proposed changes conflict with CLAUDE.md rules
- No tests planned but codebase has test coverage

---

## Inter-Spec Mode: Consistency Across Specs

Checks for conflicts between this spec and other active specs.

### Finding Other Specs

```
# Reference specs
Glob: specs/reference/*.md

# Change specs (directory format)
Glob: specs/changes/*/spec.md

# Change specs (compact format)
Glob: specs/changes/*.md

# Filter by status (check frontmatter)
# Only consider: status: active
# Ignore: status: stale, archived, superseded
```

### Conflict Types

| Conflict | Example |
|----------|---------|
| **Contradictory scenarios** | Spec A: "Then system uses REST" / Spec B: "Then system uses GraphQL" |
| **Shared component collision** | Both specs modify same file differently |
| **Terminology divergence** | Spec A calls it "user", Spec B calls it "customer" |
| **Sequencing conflict** | Spec A depends on X, Spec B removes X |
| **Resource contention** | Both specs need same limited resource |

### Conflict Detection Process

1. List all active specs
2. For each active spec:
   - Read its spec.md
   - Check for overlapping scope
   - If overlap: read design.md
   - Identify specific conflicts
3. Report conflicts with references to both specs

### Severity of Inter-Spec Issues

| Issue | Severity |
|-------|----------|
| Contradictory modifications to same file | Blocking |
| Different approaches to same problem | Needs-work (may be intentional) |
| Terminology inconsistency | Reservation |

---

## Dialogue Guidelines

### Being Constructively Adversarial

**Do:**
- Cite specific locations (file:line)
- Explain what evidence would satisfy you
- Acknowledge when concerns are addressed
- Distinguish blocking issues from preferences

**Don't:**
- Demand perfection on style matters
- Repeat the same concern if addressed
- Block on hypothetical edge cases
- Ignore good-faith responses

### Response Quality Assessment

When main agent responds to critique:

| Response Type | Your Action |
|---------------|-------------|
| Provides evidence | Verify it, update verdict if satisfied |
| Makes changes | Re-read files, re-evaluate |
| Pushes back with reasoning | Consider argument, yield or persist |
| Hand-waves | Persist, demand specifics |
| Ignores concern | Escalate severity |

### Escalation Triggers

Escalate to user after round 5 if:
- Main agent refuses to address blocking issue
- Fundamental disagreement about scenarios
- Need user input on ambiguous trade-off
- Scope question that only user can answer

---

## Quick Reference: Verdict Decision

```
Has contradictions in spec?           → blocked
Has unvalidated critical assumptions? → needs-work
Missing requirement/scenario coverage? → needs-work
Minor style/convention issues only?   → approved-with-reservations
All checks pass?                      → approved
```
