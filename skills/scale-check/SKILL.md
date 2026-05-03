---
name: scale-check
description: 'Assess scalability of a process, system, or initiative at 2x, 10x, and 100x growth. Activate when: "will this scale", "scalability check", "what breaks at scale", growth readiness, scaling
  bottlenecks Do NOT activate for: organizational maturity assessment (/maturity-check), commitment readiness (/commitment-check), architecture review (@chief-architect)'
argument-hint: '[process, system, or initiative] or [update path/to/check.md]'
user-invocable: true
metadata:
  author: Product Org OS
  version: 3.0.0
  category: validation
  skill_type: task-capability
  owner: ai-architect
  primary_consumers:
  - prodops
  - chief-architect
  - ai-architect
  - api-architect
  - cloud-architect
  - data-architect
  - tech-lead
  - backend-dev
  - devops
  - coo
  - cio
  - it-dir
  - enterprise-systems
  - operations-dir
  - process-engineer
  secondary_consumers:
  - security-architect
  - bi-engineer
  - ml-engineer
  - frontend-dev
  - program-manager
  - risk-manager
---
## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "reassess", "refresh" in input | UPDATE | 100% |
| File path provided | UPDATE | 100% |
| "create", "new", "assess" in input | CREATE | 100% |
| "find", "search", "list" | FIND | 100% |
| "the scale check", "our assessment" | UPDATE | 85% |
| Just process/system/initiative | CREATE | 60% |

**Threshold**: ≥85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Generate complete new scale check using template below.

**UPDATE**:
1. Check document registry first, then search user's structure
2. Preserve investment roadmap and historical assessments
3. Update scale readiness or bottleneck analysis
4. Show diff summary

**FIND**: Check registry, then search user's folders for scale checks.

---
## Gotchas

- Process recommendations must match organizational maturity — Level 1 orgs need lightweight processes
- Scalability is not about size — it's about whether processes work as the organization grows



Assess **scalability** of a process, system, or initiative at 2x, 10x, and 100x scale, validating Principle #7 (Scalable Systems).

## Vision to Value Phase

**Cross-phase** - This skill validates scalability when designing processes, systems, or operational approaches at any phase.

## Purpose

Scalable Systems means processes that work as the organization grows. This skill stress-tests approaches at multiple scale levels to identify breaking points before they become problems.

## Output Structure

```markdown
# Scale Check: [Subject]

**Date**: [Date]
**Subject**: [Process/System/Initiative being assessed]
**Current Scale**: [Baseline metrics - team size, volume, etc.]

## Scale Dimensions

Define what "scale" means for this subject:

| Dimension | Current | 2x | 10x | 100x |
|-----------|---------|-----|------|------|
| [Users/Customers] | [N] | [2N] | [10N] | [100N] |
| [Team size] | [N] | [2N] | [10N] | [100N] |
| [Transaction volume] | [N] | [2N] | [10N] | [100N] |
| [Product lines] | [N] | [2N] | [10N] | [100N] |
| [Markets/Regions] | [N] | [2N] | [10N] | [100N] |

## 2x Scale Assessment

**Scenario**: [Describe what 2x looks like]

### What Works at 2x
- [Element that scales well]
- [Element that scales well]

### What Strains at 2x
| Element | Current State | 2x Impact | Severity |
|---------|---------------|-----------|----------|
| [Process/System] | [How it works now] | [What happens at 2x] | Low/Med/High |
| [Process/System] | [Current] | [2x impact] | Severity |

### 2x Verdict
**Status**: [Ready/Minor Adjustments/Significant Changes Needed]

**Immediate actions required**:
- [Action 1]
- [Action 2]

## 10x Scale Assessment

**Scenario**: [Describe what 10x looks like]

### What Works at 10x
- [Element that still scales]
- [Element that still scales]

### What Breaks at 10x
| Element | Current State | 10x Impact | Severity |
|---------|---------------|------------|----------|
| [Process/System] | [How it works now] | [What breaks at 10x] | Low/Med/High |
| [Process/System] | [Current] | [10x impact] | Severity |

### 10x Redesign Required
- [Major change needed]
- [Major change needed]

### 10x Verdict
**Status**: [Ready/Partial/Requires Fundamental Redesign]

**Medium-term investments required**:
- [Investment 1]
- [Investment 2]

## 100x Scale Assessment

**Scenario**: [Describe what 100x looks like - may be hypothetical]

### What Survives at 100x
- [Core principle that endures]
- [Fundamental approach that scales]

### What's Completely Different at 100x
| Element | Current Approach | 100x Approach |
|---------|------------------|---------------|
| [Process] | [Manual/Semi-auto] | [Fully automated/AI-driven] |
| [Structure] | [Current] | [Required at 100x] |

### 100x Vision
[Describe what success looks like at 100x scale]

## Hero Dependency Analysis

"Heroes" are individuals whose personal effort makes a non-scalable process work.

| Process | Hero Dependency | Impact if Hero Unavailable | Scale Limit |
|---------|-----------------|---------------------------|-------------|
| [Process 1] | [Name/Role] | [What breaks] | [When it breaks] |
| [Process 2] | [Name/Role] | [What breaks] | [When it breaks] |

**Hero-dependent processes must be systematized before scaling.**

## Bottleneck Analysis

| Bottleneck | Current Capacity | Scale at Which It Breaks | Mitigation |
|------------|------------------|--------------------------|------------|
| [Bottleneck 1] | [Capacity] | [2x/10x/100x] | [How to address] |
| [Bottleneck 2] | [Capacity] | [Scale] | [Mitigation] |

## Director-Span Constraint

When the subject of a scale check is an organizational structure (a team, a function, a Director's reporting line), apply the Director-span sanity check before approving the structure for the next scale level. The constraint is a managerial-leverage band on direct reports per Director. Outside the band, the Director role becomes structurally compromised even when individual performance is strong.

| Direct Reports per Director | Verdict | Failure Mode |
|---|---|---|
| < 6 | **Concern** | Overhead. The Director's calendar gets eaten by 1:1s with too few people; managerial leverage is low; the Director drifts back into IC work to feel useful. |
| 6 to 10 | **Pass** | Real coaching and calibration time per report; Director can hold quality without compressing into ratification. |
| 11 to 12 | **Pass with watch** | Still workable, but coaching time per report is compressing. Watch for signs the Director is moving from coaching to ratification. |
| > 12 | **Fail** | Calibration only. The Director cannot do real coaching at this span; reviews compress into ratify-the-recommendation; growth of individual reports stalls. Restructure or add a layer. |

### How to apply

1. For each Director-level role inside the subject (existing or planned at the target scale level), record the count of direct reports.
2. Compare to the band above and produce a per-Director verdict.
3. For Directors below 6 reports: name the IC-creep risk and propose either consolidation (merge two thin reporting lines) or expansion of scope (give the Director more reports or more functions).
4. For Directors above 12 reports: name the coaching-collapse risk and propose either an additional management layer (promote a senior IC to manager) or a split (carve the function into two Director-level reporting lines).
5. Cross-reference to the relevant RACI artefact when one exists. The Director-span verdict is a precondition for the structure passing the broader scale check at the assessed level.

| Director / Role | Direct Reports (Current) | Direct Reports (at Target Scale) | Band | Verdict | Action |
|---|---|---|---|---|---|
| [Director name/role 1] | [N] | [N] | [< 6 / 6-10 / 11-12 / > 12] | [Concern/Pass/Pass with watch/Fail] | [Action] |
| [Director name/role 2] | [N] | [N] | [Band] | [Verdict] | [Action] |

**Why this constraint sits inside `/scale-check`**: a process or system that "scales" on paper but routes through a Director with 18 reports does not actually scale — it just moves the breaking point from process to person. Director span is a structural bottleneck, identical in shape to the bottlenecks tracked in the analysis above.



## Complexity vs. Maturity Match

| Org Maturity Level | Appropriate Complexity | Current Complexity | Match? |
|--------------------|------------------------|-------------------|--------|
| Enabling | Low | [Current] | Yes/No |
| Established | Medium | [Current] | Yes/No |
| Company Leading | High | [Current] | Yes/No |
| Market Leading | Variable | [Current] | Yes/No |

**Assessment**: [Is current complexity appropriate for current maturity?]

## Investment Roadmap

### Immediate (Enable 2x)
| Investment | Cost | Impact | Priority |
|------------|------|--------|----------|
| [Investment 1] | [Effort/Cost] | [Scale enabled] | High/Med/Low |
| [Investment 2] | [Effort/Cost] | [Scale enabled] | Priority |

### Medium-term (Enable 10x)
| Investment | Cost | Impact | Priority |
|------------|------|--------|----------|
| [Investment 1] | [Effort/Cost] | [Scale enabled] | High/Med/Low |
| [Investment 2] | [Effort/Cost] | [Scale enabled] | Priority |

### Long-term (Enable 100x)
| Investment | Cost | Impact | Priority |
|------------|------|--------|----------|
| [Investment 1] | [Effort/Cost] | [Scale enabled] | High/Med/Low |

## Scalability Score

| Scale Level | Readiness |
|-------------|-----------|
| 2x | [Ready/Partial/Not Ready] |
| 10x | [Ready/Partial/Not Ready] |
| 100x | [Ready/Partial/Not Ready] |

**Overall Scalability Assessment**: [Highly Scalable/Moderately Scalable/Scale-Limited]

## Recommendations

### Do Now (2x enablement)
1. [Action]
2. [Action]

### Plan For (10x enablement)
1. [Action]
2. [Action]

### Keep in Mind (100x vision)
1. [Principle to preserve]
2. [Direction to head]
```

## Instructions

1. Ask what process, system, or initiative to assess
2. Define the relevant scale dimensions
3. Assess what works and what breaks at 2x
4. Assess what works and what breaks at 10x
5. Envision what 100x looks like
6. Identify hero dependencies and bottlenecks
7. If the subject includes organizational structure or Director-level reporting lines, run the Director-Span Constraint check
8. Match complexity to maturity level
9. Provide investment roadmap and recommendations

## Validation Questions

- Does this work at 2x current scale?
- What breaks at 10x?
- What's fundamentally different at 100x?
- Are we dependent on heroes?
- Is complexity appropriate for our maturity?

## Red Flag Triggers

Immediately flag if:
- Process requires specific individuals to function
- No path to automation exists
- Complexity exceeds current maturity level
- Breaking point is before 2x scale
- Any Director in the structure has fewer than 6 direct reports (overhead / IC-creep risk) or more than 12 direct reports (coaching collapse / calibration-only management)

## When to Use

- When designing new processes
- When evaluating operational approaches
- Before making infrastructure decisions
- During strategic planning
- When assessing readiness for growth

## Related Skills

- `/maturity-check` - Assess current maturity level
- `/commitment-check` - Includes scalability consideration
- `/strategic-bet` - Should consider scale implications
- `/raci-builder` - Pair the Director-Span Constraint with explicit RACI assignments when restructuring reporting lines (when this skill is available; expected as a v5.2 pairing)

## Operating Principle

> "Design for 10x, deliver for 2x, dream about 100x. Don't over-engineer for today, but don't paint yourself into a corner either."
