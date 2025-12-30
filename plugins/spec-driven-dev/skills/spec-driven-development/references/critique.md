# Critique Reference

Detailed checklists and exploration patterns for the spec-critic agent.

## Intra-Spec Mode: Coherence Within the Spec

Checks for contradictions and coherence within a single spec.

### Requirements Checklist

| Check | What to Look For |
|-------|-----------------|
| EARS syntax | Every acceptance criterion uses WHEN/IF/WHILE/WHERE + SHALL |
| No ambiguity | Avoid: should, could, might, usually, quickly, properly |
| Testability | Each criterion is specific and verifiable |
| Completeness | Every FR-NNN has acceptance criteria |
| Edge cases | Error conditions and boundaries documented |
| Internal consistency | FR-001 doesn't contradict FR-003 |
| Terminology | Same concept uses same term throughout |

### Design Checklist

| Check | What to Look For |
|-------|-----------------|
| Coverage | All requirements are addressed |
| Rationale | Decisions have documented reasoning |
| Alignment | Decisions don't contradict requirements |
| Risks | Potential issues identified with mitigations |
| Feasibility | Proposed approach is technically sound |

### Tasks Checklist

| Check | What to Look For |
|-------|-----------------|
| Traceability | Every task references requirement(s) it satisfies |
| Coverage | All requirements appear in at least one task |
| Sequencing | Dependencies are respected (can't use X before creating X) |
| Completeness | Verification item exists at end |
| [NEXT] marker | Present if tasks are incomplete |

### Cross-File Checklist

| Check | What to Look For |
|-------|-----------------|
| Scope alignment | requirements → design → tasks tell consistent story |
| No drift | Tasks don't add features not in requirements |
| Terminology | "user" vs "customer" used consistently |
| References | No orphaned refs (task mentions FR-005 that doesn't exist) |

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
# Extract paths from tasks.md
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
Grep: pattern from tasks
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

- Tasks reference files that don't exist
- Design assumes behavior that code doesn't have
- Plan ignores existing implementation of same feature
- Proposed changes conflict with CLAUDE.md rules
- No tests planned but codebase has test coverage

---

## Inter-Spec Mode: Consistency Across Specs

Checks for conflicts between this spec and other active specs.

### Finding Other Specs

```
# Directory format specs
Glob: specs/*/requirements.md

# Compact format specs
Glob: specs/*.md

# Filter by status (check frontmatter)
# Only consider: status: active
# Ignore: status: stale, archived, superseded
```

### Conflict Types

| Conflict | Example |
|----------|---------|
| **Contradictory requirements** | Spec A: "[system] SHALL use REST" / Spec B: "[system] SHALL use GraphQL" |
| **Shared component collision** | Both specs modify same file differently |
| **Terminology divergence** | Spec A calls it "user", Spec B calls it "customer" |
| **Sequencing conflict** | Spec A depends on X, Spec B removes X |
| **Resource contention** | Both specs need same limited resource |

### Conflict Detection Process

1. List all active specs
2. For each active spec:
   - Read its requirements.md
   - Check for overlapping scope
   - If overlap: read design.md and tasks.md
   - Identify specific conflicts
3. Report conflicts with references to both specs

### Severity of Inter-Spec Issues

| Issue | Severity |
|-------|----------|
| Same requirement number (FR-001 in two specs) | Blocking (namespace collision) |
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
- Fundamental disagreement about requirements
- Need user input on ambiguous trade-off
- Scope question that only user can answer

---

## Quick Reference: Verdict Decision

```
Has contradictions in spec?           → blocked
Has unvalidated critical assumptions? → needs-work
Missing requirement traceability?     → needs-work
Minor style/convention issues only?   → approved-with-reservations
All checks pass?                      → approved
```
