---
name: decision-quality-audit
description: 'Audit a set of recent decisions for quality, process adherence, and systemic patterns. Activate when: "review our decisions", "decision quality check", "audit decision process", improve decision-making,
  decision patterns Do NOT activate for: documenting individual decisions (/decision-record), decision ownership charters (/decision-charter), outcome reviews (/outcome-review)'
argument-hint: '[team, time period, or decision type] or [update path/to/audit.md]'
user-invocable: true
metadata:
  author: Product Org OS
  version: 3.0.0
  category: decisions
  skill_type: task-capability
  owner: pm-dir
  primary_consumers:
  - pm-dir
---
## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "add decisions", "refresh" in input | UPDATE | 100% |
| File path provided | UPDATE | 100% |
| "create", "new", "run" in input | CREATE | 100% |
| "find", "search", "list" | FIND | 100% |
| "the audit", "last audit" | UPDATE | 85% |
| Just team/period/type | CREATE | 60% |

**Threshold**: ≥85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Generate complete new audit using template below.

**UPDATE**:
1. Check document registry first, then search user's structure
2. Preserve historical scores and trend data
3. Update with new decisions or findings
4. Show diff summary with score changes

**FIND**: Check registry, then search user's folders for audit reports.

---

Audit **Decision Quality** for a set of recent decisions.

## Vision to Value Context
**Phase 6: Learning & Adaptation Loop** - Decision quality is the core metric for product leadership effectiveness.

## Output Structure

```markdown
# Decision Quality Audit: [Scope]

**Audit Date**: [Date]
**Auditor**: [Name]
**Period**: [Timeframe audited]
**Decisions Reviewed**: [Number]

## Executive Summary

**Overall Decision Quality Score**: [X/5]
**Decision Improvability Rate**: [X% of audited decisions had a weak frame, weak alternatives, or weak criteria]
**Key Finding**: [One sentence summary]
**Priority Improvement**: [One area to focus on]

## Decisions Audited

| Decision | Date | Owner | Type | Quality Score |
|----------|------|-------|------|---------------|
| [Decision 1] | [Date] | [Owner] | Strategic/Portfolio/Execution | X/5 |
| [Decision 2] | [Date] | [Owner] | Strategic/Portfolio/Execution | X/5 |

## Quality Criteria Assessment

### 1. Clear Ownership
**Score**: [X/5]
**Finding**: [What we found]
**Evidence**:
- X% of decisions had single accountable owner
- [Other evidence]

### 2. Explicit Options Considered
**Score**: [X/5]
**Finding**: [What we found]
**Evidence**:
- X% documented alternatives
- [Other evidence]

### 3. Success Criteria Defined
**Score**: [X/5]
**Finding**: [What we found]
**Evidence**:
- X% had measurable success criteria
- [Other evidence]

### 4. Re-decision Triggers Defined
**Score**: [X/5]
**Finding**: [What we found]
**Evidence**:
- X% defined when to revisit
- [Other evidence]

### 5. Assumptions Documented
**Score**: [X/5]
**Finding**: [What we found]
**Evidence**:
- X% had explicit assumptions
- [Other evidence]

### 6. Appropriate Input Gathered
**Score**: [X/5]
**Finding**: [What we found]
**Evidence**:
- X% involved right stakeholders
- [Other evidence]

### 7. Timely Decision-Making
**Score**: [X/5]
**Finding**: [What we found]
**Evidence**:
- Average decision time: X days
- [Other evidence]

## Quality Scorecard

| Criterion | Score | Trend | Priority |
|-----------|-------|-------|----------|
| Clear Ownership | X/5 | ↑/↓/→ | High/Med/Low |
| Options Considered | X/5 | ↑/↓/→ | High/Med/Low |
| Success Criteria | X/5 | ↑/↓/→ | High/Med/Low |
| Re-decision Triggers | X/5 | ↑/↓/→ | High/Med/Low |
| Assumptions Documented | X/5 | ↑/↓/→ | High/Med/Low |
| Appropriate Input | X/5 | ↑/↓/→ | High/Med/Low |
| Timely Decision | X/5 | ↑/↓/→ | High/Med/Low |

## Pattern Analysis

### What's Working
| Pattern | Evidence | Impact |
|---------|----------|--------|
| [Pattern] | [Evidence] | [Impact] |

### What Needs Improvement
| Pattern | Evidence | Impact | Recommendation |
|---------|----------|--------|----------------|
| [Pattern] | [Evidence] | [Impact] | [Recommendation] |

## Decision Improvability

**Decision Improvability** is the share of audited decisions where, in hindsight, the decision frame, the alternatives, or the criteria could have been better-formed at the time. A decision is "improvable" if a competent reader of the record concludes the same outcome could have been reached with a stronger frame, or that a different outcome was likely had the frame been stronger. Improvability is not the same as "wrong outcome" — a decision can be improvable in process and right in outcome (lucky), or unimprovable in process and wrong in outcome (unlucky). The dimension tracks the process side, because process is what the organization can actually change.

### Per-class trajectory

Improvability is most informative when grouped by class of decision, not pooled across all decisions. A 30% improvability rate on `pricing` decisions tells a different story than a 30% improvability rate on `hire` decisions, and the corrective action is class-specific. The auditor sources the class assignment for each Decision ID from the sidecar registry at `decision-class-registry.md` (V5.1-37, Path (b)).

| Decision Class | Audited (count) | Improvable (count) | Improvability Rate | Trend vs. Last Audit |
|---|---|---|---|---|
| strategic-bet | [N] | [N] | [%] | ↑/↓/→ |
| portfolio-tradeoff | [N] | [N] | [%] | ↑/↓/→ |
| execution-call | [N] | [N] | [%] | ↑/↓/→ |
| hire | [N] | [N] | [%] | ↑/↓/→ |
| vendor | [N] | [N] | [%] | ↑/↓/→ |
| pricing | [N] | [N] | [%] | ↑/↓/→ |
| partnership | [N] | [N] | [%] | ↑/↓/→ |
| other | [N] | [N] | [%] | ↑/↓/→ |
| **Overall** | [N] | [N] | [%] | ↑/↓/→ |

### Per-decision Improvability assessment

For each audited decision, the auditor records:

| Decision ID | Class (from sidecar) | Improvable? | Frame Issue | Alternatives Issue | Criteria Issue | Note |
|---|---|---|---|---|---|---|
| DR-YYYY-NNN | strategic-bet | Yes/No | [What was missing or weak in the framing of the decision] | [What was missing or weak about the alternatives considered] | [What was missing or weak about the named criteria] | [One-line auditor note] |

**Rules for marking a decision improvable**:
- The decision is improvable if any one of the three (Frame, Alternatives, Criteria) is weak enough that a competent reviewer would push back today.
- "Weak frame" means the decision was stated as a problem, not as a choice between named options.
- "Weak alternatives" means fewer than two real alternatives were considered, or the alternatives were strawmen the recommended option was always going to win against.
- "Weak criteria" means the decision was made without explicit, weighted criteria — typically visible as "we went with the recommended option" without prose explaining why that option won on what dimension.

### Examples to illustrate the dimension

- A `strategic-bet` to enter the EU market that was framed as "should we expand internationally?" with only one named option (EU) is **improvable** even if the EU bet ultimately succeeded — the frame was weak.
- A `pricing` decision to move from per-seat to consumption-based that surfaced four named alternatives, weighted them against named criteria (margin, customer adoption risk, revenue predictability), and explained why consumption-based won is **not improvable** even if the outcome was disappointing — the process was sound; the assumptions just turned out wrong.

### What to do with the Improvability rate

- **Below 20% overall**: Process is healthy. Continue current practice.
- **20% to 40% overall**: Process is leaky in identifiable places. Identify which class drives the rate; coach that class specifically.
- **Above 40% overall**: Decision discipline is below the bar for the organization's scale. Consider mandating `/decision-record` for the affected classes, tightening the `/decision-charter` for the recurring decision types, or requiring explicit Decision Frame at escalation time (`/escalation-rule`).

### Sidecar registry (data dependency)

Class assignments come from the sidecar registry at `decision-class-registry.md` in this skill's folder. The sidecar exists because `decision_class` is intentionally NOT a field on the v5.0 `/decision-record` schema (R-018 preservation). The auditor classifies each decision at audit time using the recommended eight-class taxonomy in the sidecar, and the registry persists across audits so subsequent audits do not re-prompt for already-classified records.

When `/decision-quality-audit` runs Decision Improvability:

1. Walk `context/decisions/` to enumerate records in scope.
2. Read `decision-class-registry.md` (the sidecar in this folder).
3. For each record present in `context/decisions/` but absent in the registry, prompt the auditor to classify it using the eight-class taxonomy. Write the result back to the registry with `classified_by: "auditor"`.
4. Compute Improvability per class and overall.
5. Surface trends against the previous audit's per-class rates if a previous audit exists.

## Recommendations

### Process Improvements
1. [Recommendation]

### Template/Tool Improvements
1. [Recommendation]

### Training/Coaching Needs
1. [Recommendation]

## Follow-up Actions

| Action | Owner | Due Date |
|--------|-------|----------|
| [Action] | [Owner] | [Date] |

## Next Audit

**Scheduled**: [Date]
**Focus Areas**: [What to emphasize]
```

## Instructions

1. Gather recent decision records to audit
2. Reference decision records and charters via @file syntax
3. Score objectively against criteria
4. Identify patterns, not just individual issues
5. Run the Decision Improvability dimension: read the sidecar registry at `decision-class-registry.md`, classify any unclassified records using the eight-class taxonomy, compute per-class Improvability rates, and trend them against the previous audit.
6. Cross-reference `/win-loss-decision-signal` (V5.1-16) when external signals — won deals, lost deals, customer escalations — bear on the audited decisions.
7. Save in audits/ folder
8. Offer to create presentation version using /present
