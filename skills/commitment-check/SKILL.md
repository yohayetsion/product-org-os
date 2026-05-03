---
name: commitment-check
description: 'Validate commitment readiness before the point of no return on resources. Activate when: "are we ready to commit", "commitment check", "go/no-go", before locking resources, Phase 3 gate Do
  NOT activate for: Vision to Value phase assessment (/phase-check), launch readiness check (/launch-readiness), decision records (/decision-record)'
argument-hint: '[commitment or initiative name] or [update path/to/check.md]'
user-invocable: true
metadata:
  author: Product Org OS
  version: 3.1.0
  category: strategy
  skill_type: task-capability
  owner: coo
  primary_consumers:
  - pm-dir
  - prodops
  - legal-dir
  - coo
  - operations-dir
  - program-manager
  - project-manager
  - vp-product
  - cpo
  secondary_consumers:
  - ceo
  - finance-dir
  - bizops
---
## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "recheck", "refresh" in input | UPDATE | 100% |
| File path provided | UPDATE | 100% |
| "create", "new", "validate" in input | CREATE | 100% |
| "find", "search", "list" | FIND | 100% |
| "the commitment check", "our check" | UPDATE | 85% |
| Just initiative name | CREATE | 60% |

**Threshold**: ≥85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Generate complete new commitment check using template below.

**UPDATE**:
1. Check document registry first, then search user's structure
2. Preserve prior assessments and gap tracking
3. Update readiness status and close gaps
4. Show diff summary

**FIND**: Check registry, then search user's folders for commitment checks.

---
## Gotchas

- Never approve a commitment without verifying Phase 1-2 deliverables actually exist — check file paths
- Single accountable owner is mandatory — escalate if ownership is shared or unclear
- Resource commitment without capacity verification is a promise that can't be kept



Validate that a **Commitment is Properly Hardened** before proceeding.

## Purpose
The commitment check ensures decisions are thoroughly vetted before crossing the "point of no return" where reversal becomes costly.

## Vision to Value Phase

**Phase 3: Strategic Commitments** - This is the "point of no return" gate. Once passed, resources are committed and reversal is expensive.

**Prerequisites**: Phase 1 and Phase 2 complete
**Outputs used by**: Phase 4 execution, resource allocation

## Output Structure

```markdown
# Commitment Check: [Initiative Name]

**Date**: [Date]
**Reviewed By**: [Name/Role]
**Status**: ✅ Ready to Commit / ⚠️ Needs Work / ❌ Not Ready

## Commitment Overview

**What**: [What we're committing to]
**Investment**: [Resources/budget being committed]
**Timeline**: [Commitment duration]
**Point of No Return**: [What happens after commitment]

## Vision to Value Phase Prerequisites

### Phase 1: Strategic Foundation ✅/⚠️/❌

| Deliverable | Status | Evidence/Location |
|-------------|--------|-------------------|
| Strategic intent documented | ✅/⚠️/❌ | [Link] |
| Market analysis complete | ✅/⚠️/❌ | [Link] |
| Competitive landscape understood | ✅/⚠️/❌ | [Link] |
| Target segments defined | ✅/⚠️/❌ | [Link] |

**Phase 1 Assessment**: Complete / Gaps Exist

### Phase 2: Strategic Decisions ✅/⚠️/❌

| Deliverable | Status | Evidence/Location |
|-------------|--------|-------------------|
| Business case approved | ✅/⚠️/❌ | [Link] |
| Pricing defined | ✅/⚠️/❌ | [Link] |
| Positioning clear | ✅/⚠️/❌ | [Link] |
| Key assumptions documented | ✅/⚠️/❌ | [Link] |

**Phase 2 Assessment**: Complete / Gaps Exist

**Phase Prerequisite Status**: ✅ Ready / ⚠️ Gaps to Close / ❌ Not Ready

## Ownership Chain (Principle #1)

| Vision to Value Phase | Accountable Owner | Status |
|-----------|-------------------|--------|
| Phase 1: Strategic Foundation | [Name] | ✅/⚠️/❌ |
| Phase 2: Strategic Decisions | [Name] | ✅/⚠️/❌ |
| Phase 3: This Commitment | [Name] | ✅/⚠️/❌ |
| Phase 4: Execution | [Name] | ✅/⚠️/❌ |
| Phase 5: Outcomes | [Name] | ✅/⚠️/❌ |

**End-to-End Owner**: [Single person accountable from strategy to outcome]
**Ownership Chain Status**: ✅ Clear / ⚠️ Gaps / ❌ Broken

---

## Five Signals of a Committed Bet (Hard Gate)

Source: Vision to Value, Figure 5.1 — *Five Signals of a Committed Bet*.

A **committed bet** is a bet that carries all five signals on the record. A bet missing any signal is a bet that cannot be reopened with discipline, and will instead be reopened on political cost. This section enforces the structural test: each of the five signals must be **present, named, and verifiable** before the commitment is hardened. Any missing signal blocks the commitment regardless of how strong the rest of the readiness assessment looks. A confident-looking business case with no continuation threshold, or a roadmap with no exit condition, is exactly the failure mode this gate is built to catch.

The five signals are not seven categories of comfort. They are the five places a verbal commitment quietly becomes a real one. Capital that is not envelope-named is capital the CFO can rebudget without a conversation. A continuation threshold that is not class-amount-and-date-named is a threshold no one will recognize when it is crossed. Re-decision triggers that are not named are triggers that fire on quarterly drift instead of evidence. A record location that is not named is a record that does not exist. An exit condition that is not named is the path by which the organization keeps shipping a bet it has already lost confidence in.

### Five Signals Checklist Artifact

This is the structured artifact downstream consumers (the Phase 3→4 hard-gate, portfolio reviews, decision audits) read mechanically. Each signal is **PASS / FAIL** with named rationale. Overall verdict: **COMMITTED** only if all five PASS.

| # | Signal | Required Fields | Status | Rationale / Gap |
|---|--------|-----------------|--------|-----------------|
| 1 | **Capital envelope named** | Committed floor, envelope, disclosure threshold | ✅ PASS / ❌ FAIL | [Cite the record. If FAIL: which field is missing — floor, envelope, or disclosure threshold?] |
| 2 | **Continuation threshold named** | Evidence class, amount, date | ✅ PASS / ❌ FAIL | [Cite the threshold and the `/continuation-threshold` artifact. If FAIL: which of class / amount / date is unnamed?] |
| 3 | **Re-decision triggers named** | Outcome trigger(s), market trigger(s), counterparty-specific trigger(s) | ✅ PASS / ❌ FAIL | [Cite each trigger by category. If FAIL: which category has no named trigger?] |
| 4 | **Record location and auditable-by named** | Record location (path/system), named auditor (role + person) | ✅ PASS / ❌ FAIL | [Cite the record location and the auditable-by name. If FAIL: is the record absent, or is the auditor unnamed?] |
| 5 | **Exit condition named** | One of {commit, cancel, migrate} with evidence-and-date triggering it | ✅ PASS / ❌ FAIL | [Cite the exit condition and what evidence triggers it. If FAIL: is the path unnamed, or are the trigger conditions unnamed?] |

**Five Signals Verdict**: ✅ COMMITTED (all five PASS) / ❌ NOT COMMITTED (one or more FAIL — bet remains a verbal commitment until gaps are closed)

**Specific Gaps Named** (only if NOT COMMITTED):
- Signal [N]: [exact field missing and what would close the gap]
- Signal [M]: [exact field missing and what would close the gap]

**Bound to**: This Five Signals artifact is the hand-off to `/phase-check` for the Phase 3 → Phase 4 transition. `/phase-check` reads the **Five Signals Verdict** field mechanically. A NOT COMMITTED verdict blocks Phase 4 transition independent of any other readiness signal.

---

## Readiness Assessment

### 1. Strategic Alignment ✅/⚠️/❌

| Criteria | Status | Evidence |
|----------|--------|----------|
| Connects to strategic goals | ✅/⚠️/❌ | [Evidence] |
| Fits within portfolio priorities | ✅/⚠️/❌ | [Evidence] |
| Approved by appropriate authority | ✅/⚠️/❌ | [Evidence] |

**Assessment**: [Summary]

### 2. Problem Validation ✅/⚠️/❌

| Criteria | Status | Evidence |
|----------|--------|----------|
| Customer problem is validated | ✅/⚠️/❌ | [Evidence] |
| Market opportunity is sized | ✅/⚠️/❌ | [Evidence] |
| Timing is right | ✅/⚠️/❌ | [Evidence] |

**Assessment**: [Summary]

### 3. Solution Clarity ✅/⚠️/❌

| Criteria | Status | Evidence |
|----------|--------|----------|
| Solution approach is defined | ✅/⚠️/❌ | [Evidence] |
| Technical feasibility confirmed | ✅/⚠️/❌ | [Evidence] |
| Key risks identified | ✅/⚠️/❌ | [Evidence] |

**Assessment**: [Summary]

### 4. Business Case ✅/⚠️/❌

| Criteria | Status | Evidence |
|----------|--------|----------|
| Financial projections complete | ✅/⚠️/❌ | [Evidence] |
| ROI meets threshold | ✅/⚠️/❌ | [Evidence] |
| Assumptions documented | ✅/⚠️/❌ | [Evidence] |

**Assessment**: [Summary]

### 5. Resource Readiness ✅/⚠️/❌

| Criteria | Status | Evidence |
|----------|--------|----------|
| Team identified and available | ✅/⚠️/❌ | [Evidence] |
| Budget approved | ✅/⚠️/❌ | [Evidence] |
| Dependencies resolved | ✅/⚠️/❌ | [Evidence] |

**Assessment**: [Summary]

### 6. GTM Readiness ✅/⚠️/❌

| Criteria | Status | Evidence |
|----------|--------|----------|
| Positioning defined | ✅/⚠️/❌ | [Evidence] |
| Launch plan drafted | ✅/⚠️/❌ | [Evidence] |
| Sales enablement planned | ✅/⚠️/❌ | [Evidence] |

**Assessment**: [Summary]

### 7. Success Criteria ✅/⚠️/❌

| Criteria | Status | Evidence |
|----------|--------|----------|
| Success metrics defined | ✅/⚠️/❌ | [Evidence] |
| Measurement plan in place | ✅/⚠️/❌ | [Evidence] |
| Re-decision triggers defined | ✅/⚠️/❌ | [Evidence] |

**Assessment**: [Summary]

## Overall Assessment

| Gate | Status |
|------|--------|
| **Five Signals Verdict** (hard gate) | ✅ COMMITTED / ❌ NOT COMMITTED |
| Phase 1 + Phase 2 Prerequisites | ✅/⚠️/❌ |
| Ownership Chain | ✅/⚠️/❌ |
| Strategic Alignment | ✅/⚠️/❌ |
| Problem Validation | ✅/⚠️/❌ |
| Solution Clarity | ✅/⚠️/❌ |
| Business Case | ✅/⚠️/❌ |
| Resource Readiness | ✅/⚠️/❌ |
| GTM Readiness | ✅/⚠️/❌ |
| Success Criteria | ✅/⚠️/❌ |

**Overall Status**: [Ready / Needs Work / Not Ready]

**Gate logic**: A NOT COMMITTED Five Signals verdict forces Overall Status to **Not Ready** regardless of how the supporting categories score. The Five Signals are necessary; the supporting categories are how the bet earns confidence inside that envelope.

## Gaps to Close

| Gap | Owner | Due Date | Blocking? |
|-----|-------|----------|-----------|
| [Gap 1] | [Owner] | [Date] | Yes/No |
| [Gap 2] | [Owner] | [Date] | Yes/No |

## Recommendation

[Clear recommendation: Proceed / Proceed with conditions / Delay / Do not proceed]

**Conditions (if applicable)**:
- [Condition 1]
- [Condition 2]
```

## Instructions

1. Ask about the initiative if context is incomplete
2. Reference any relevant documents provided via @file syntax
3. **Run the Five Signals checklist first.** Each of the five signals is a structural test, not an opinion. For each signal, cite the record where the field lives. If the field is not on the record, mark FAIL — do not infer the field from adjacent context.
4. Be rigorous — this is the last gate before significant investment
5. Identify specific gaps and owners. For Five Signals FAILs, name the exact missing field, not a generic gap.
6. Make a clear recommendation. **A NOT COMMITTED Five Signals verdict means "do not proceed" regardless of how strong the rest of the assessment looks.**
7. Save assessment with the initiative documents

## Cross-References

- **`/decision-record`** — the commitment must reference the Decision Record where the Five Signals fields are recorded. If no Decision Record exists, Signal 4 (Record location) cannot pass.
- **`/strategic-bet`** — the bet artifact carries the Capital envelope (Signal 1) and Re-decision triggers (Signal 3). The bet artifact is upstream of this commitment check.
- **`/continuation-threshold`** — the artifact that names Signal 2 (Continuation threshold: evidence class, amount, date). This commitment check does not duplicate the threshold authoring; it verifies the artifact exists and is named on the record. `/continuation-threshold` and `/commitment-check` are the front and back of the bet-management discipline: `/continuation-threshold` arms the AFFIRMATIVE-continuation gate that fires post-commit; `/commitment-check` enforces the structural test that must pass before the bet is committed in the first place.
- **`/phase-check`** — consumes the **Five Signals Verdict** field from this skill's output to hard-gate the Phase 3 → Phase 4 transition. The verdict is read mechanically; a NOT COMMITTED verdict blocks the transition.
