---
name: phase-check
description: 'Assess which Vision to Value phase an initiative is in and identify gaps for progression. Activate when: "what phase are we in", "phase check", "Vision to Value progress", initiative maturity,
  phase gate, Vision to Value assessment Do NOT activate for: commitment readiness validation (/commitment-check), organizational maturity (/maturity-check), portfolio status (/portfolio-status)'
argument-hint: '[initiative name] [mode=v5.0|v5.1|v5.2]'
user-invocable: true
metadata:
  author: Product Org OS
  version: 5.1.0
  category: assessment
  skill_type: task-capability
  owner: pm-dir
  primary_consumers:
  - pm-dir
  - prodops
  secondary_consumers:
  - vp-product
  - value-realization
  - cpo
  - bizops
---
## Wrapper Pattern — `mode:` Dispatch (v5.1)

This skill is a v5.0-aligned wrapper. Behavior is selected at invocation time by an explicit `mode:` parameter. The default is `v5.0`, which means a caller that does NOT pass `mode:` reaches v5.0 behavior unambiguously and gets v5.0 output byte-for-byte. The v5.1 mode is opt-in by callers who want the Phase 2→3 and Phase 3→4 hard-gate extensions appended below the v5.0 output.

### Dispatch logic

When the user invokes this skill, parse `args:` for an optional `mode=...` token (e.g., `mode=v5.0`, `mode=v5.1`, `mode=v5.2`):

1. If `args:` contains an explicit `mode:` token:
   - Validate against allowed values: `v5.0`, `v5.1`, `v5.2`.
   - If valid → set `selected_mode` to the parsed value.
   - If invalid (e.g., `mode=latest`) → set `selected_mode = v5.0`, prepend a single warning line to the output: `# WARN: unrecognized mode "{value}" — falling back to v5.0 mode.`
2. If `args:` does NOT contain a `mode:` token → set `selected_mode = v5.0` (the default).
3. Always execute the v5.0 logic block below (both modes need v5.0 output).
4. If `selected_mode == v5.1` → also execute the v5.1 hard-gate extensions block. Append its output below the v5.0 block as a strict superset.
5. If `selected_mode == v5.2` → behave identically to `v5.1` for now (V5.2-S43 sub-Series-C parameterization is reserved at v5.2 ship; in this v5.1 wrapper, `mode: v5.2` produces the same output as `mode: v5.1` plus a `# TODO v5.2: sub-Series-C lane reserved by V5.2-S43` note in the v5.1 extension header).
6. Return assembled output.

### Per-mode behavior

| Mode | v5.0 Output | v5.1 Hard-Gate Extensions |
|------|-------------|---------------------------|
| `v5.0` (default — no `mode:` passed) | Yes, byte-identical to v5.0.0 | No |
| `v5.0` (explicit) | Yes, byte-identical to v5.0.0 | No |
| `v5.1` | Yes, unchanged | Appended below v5.0 output |
| `v5.2` | Yes, unchanged | Appended below v5.0 output (with v5.2 reservation note) |
| Unrecognized value | Yes, with warning line | No |

### R-018 attestation — snapshot-diff test plan

R-018 requires that v5.0.0 stays tag-ready: a v5.0 caller (anyone who does not pass `mode:`) MUST get output byte-identical to pre-v5.1 output. The mechanism that makes this hold is the default-to-v5.0 dispatch above plus the unchanged v5.0 logic block.

The mechanical test:

1. **Setup (once, before v5.1 lands)**: at v5.0.0 tag SHA `29e54c3`, invoke `/phase-check` against a fixture initiative (e.g., a mid-Phase-3 initiative) with no `mode:` parameter. Capture the output as `tests/snapshots/v5.0/phase-check-mid-phase-3.md`.
2. **Verification (on `v5.1-prep` after this wrapper lands)**: invoke `/phase-check` against the same fixture with no `mode:` parameter. Capture as `tests/snapshots/v5.1-default/phase-check-mid-phase-3.md`.
3. **Diff**: `diff snapshots/v5.0/...md snapshots/v5.1-default/...md`.
4. **Pass criterion**: empty diff or whitespace-only diff (trailing newlines, indentation that does not change semantic meaning).
5. **Explicit-v5.0 test**: re-invoke with `mode=v5.0` explicitly; diff against the v5.0 snapshot must also be empty / whitespace-only.
6. **Superset test**: invoke with `mode=v5.1`; verify output starts with the full v5.0 snapshot content (substring match), then has the v5.1 hard-gate extension appended.

If the diff is non-empty, the wrapper is non-compliant with R-018 and must not merge until the v5.0 logic block is restored byte-for-byte. Wave 4 will land the pytest harness at `tests/test_wrapper_r018.py` to enforce this on `v5.1-prep` pre-merge.

The skill ID stays `phase-check` (no rename). The v5.0 alignment metadata (the skill's `vision_to_value_standard.aligned: true` posture) is unchanged. Only the `version:` field bumps from `3.0.0` to `5.1.0` to reflect the wrapper extension; the v5.0 logic block below is unchanged.

---

## v5.0 Logic Block (unchanged from v5.0.0)

The block below is the v5.0 behavior — the existing `/phase-check` skill output. This block executes in BOTH `v5.0` mode and `v5.1` mode. In `v5.0` mode it is the entire output. In `v5.1` mode it is the prefix and the hard-gate extensions are appended below it.

## Gotchas

- Phase transitions require exit criteria from previous phase — don't skip phases without acknowledging it
- Phase 2→3 is the commercial filter — not everything passes. Flag questionable viability explicitly.


Assess which **Vision to Value phase** an initiative is currently in and identify what's needed to progress.

## Vision to Value Phase

**Cross-phase** - This skill assesses phase status for any initiative at any time.

## Purpose

The Vision to Value Operating System has 6 phases. This skill determines where an initiative currently sits, what deliverables are complete, what gaps exist, and what's needed to move forward.

## Output Structure

```markdown
# Phase Check: [Initiative Name]

**Date**: [Date]
**Initiative**: [Brief description]
**Assessed By**: [Role]

## Current Phase Determination

**Current Phase**: Phase [1-6]: [Phase Name]

**Phase Status**: [Early/Mid/Late/Complete]

## Phase Progression Summary

```
[✓] Phase 1: Strategic Foundation
[✓] Phase 2: Strategic Decisions
[→] Phase 3: Strategic Commitments  ← CURRENT
[ ] Phase 4: Coordinated Execution
[ ] Phase 5: Business Outcomes
[ ] Phase 6: Learning & Adaptation
```

## Phase-by-Phase Audit

### Phase 1: Strategic Foundation

| Deliverable | Status | Evidence/Location |
|-------------|--------|-------------------|
| Strategic Intent | [Complete/Partial/Missing] | [Link or "Not found"] |
| Market Analysis | [Complete/Partial/Missing] | [Link or "Not found"] |
| Competitive Landscape | [Complete/Partial/Missing] | [Link or "Not found"] |
| Vision Statement | [Complete/Partial/Missing] | [Link or "Not found"] |
| Target Segments | [Complete/Partial/Missing] | [Link or "Not found"] |

**Phase 1 Status**: [Complete/Incomplete]
**Gaps**: [List any missing deliverables]

### Phase 2: Strategic Decisions

| Deliverable | Status | Evidence/Location |
|-------------|--------|-------------------|
| Business Case | [Complete/Partial/Missing] | [Link or "Not found"] |
| Pricing Decision | [Complete/Partial/Missing] | [Link or "Not found"] |
| Positioning | [Complete/Partial/Missing] | [Link or "Not found"] |
| Key Decision Records | [Complete/Partial/Missing] | [Link or "Not found"] |
| Assumptions Documented | [Complete/Partial/Missing] | [Link or "Not found"] |

**Phase 2 Status**: [Complete/Incomplete]
**Gaps**: [List any missing deliverables]

### Phase 3: Strategic Commitments

| Deliverable | Status | Evidence/Location |
|-------------|--------|-------------------|
| Product Roadmap | [Complete/Partial/Missing] | [Link or "Not found"] |
| GTM Strategy | [Complete/Partial/Missing] | [Link or "Not found"] |
| Launch Plan | [Complete/Partial/Missing] | [Link or "Not found"] |
| PRD/Requirements | [Complete/Partial/Missing] | [Link or "Not found"] |
| Commitment Check | [Complete/Partial/Missing] | [Link or "Not found"] |

**Phase 3 Status**: [Complete/Incomplete]
**Gaps**: [List any missing deliverables]

### Phase 4: Coordinated Execution

| Deliverable | Status | Evidence/Location |
|-------------|--------|-------------------|
| Campaign Brief | [Complete/Partial/Missing] | [Link or "Not found"] |
| Sales Enablement | [Complete/Partial/Missing] | [Link or "Not found"] |
| Launch Readiness | [Complete/Partial/Missing] | [Link or "Not found"] |
| Stakeholder Briefs | [Complete/Partial/Missing] | [Link or "Not found"] |

**Phase 4 Status**: [Complete/Incomplete/Not Started]
**Gaps**: [List any missing deliverables]

### Phase 5: Business & Customer Outcomes

| Deliverable | Status | Evidence/Location |
|-------------|--------|-------------------|
| Customers Onboarded | [Yes/No/In Progress] | [Metrics] |
| Value Realization Tracked | [Yes/No/In Progress] | [Link or "Not measured"] |
| Customer Health Monitored | [Yes/No/In Progress] | [Link or "Not measured"] |
| Success Metrics Measured | [Yes/No/In Progress] | [Link or "Not measured"] |

**Phase 5 Status**: [Complete/Incomplete/Not Started]
**Gaps**: [List any missing deliverables]

### Phase 6: Learning & Adaptation

| Deliverable | Status | Evidence/Location |
|-------------|--------|-------------------|
| Outcome Review | [Complete/Partial/Missing] | [Link or "Not conducted"] |
| Assumptions Validated | [Complete/Partial/Missing] | [Link or "Not updated"] |
| Learnings Documented | [Complete/Partial/Missing] | [Link or "Not captured"] |
| Context Registry Updated | [Complete/Partial/Missing] | [Link or "Not updated"] |

**Phase 6 Status**: [Complete/Incomplete/Not Started]
**Gaps**: [List any missing deliverables]

## Critical Gaps

### Blocking Progression
These gaps prevent moving to the next phase:

| Gap | Current Phase | Required For | Impact |
|-----|---------------|--------------|--------|
| [Missing deliverable] | [Phase N] | [Phase N+1] | [What's blocked] |
| [Missing deliverable] | [Phase N] | [Phase N+1] | [What's blocked] |

### Non-Blocking But Important
These gaps should be addressed but don't block progression:

| Gap | Phase | Recommended Action |
|-----|-------|-------------------|
| [Gap description] | [Phase] | [Action] |
| [Gap description] | [Phase] | [Action] |

## Phase Transition Readiness

### Ready for Next Phase?

**Next Phase**: Phase [N+1]: [Phase Name]

**Prerequisites Met**: [Yes/No/Partial]

| Prerequisite | Status | Notes |
|--------------|--------|-------|
| [Prerequisite 1] | [Met/Not Met] | [Details] |
| [Prerequisite 2] | [Met/Not Met] | [Details] |
| [Prerequisite 3] | [Met/Not Met] | [Details] |

**Transition Recommendation**: [Ready to proceed/Address gaps first/Not ready]

## Risk Assessment

| Risk | Phase | Likelihood | Impact | Mitigation |
|------|-------|------------|--------|------------|
| [Risk from skipping deliverable] | [Phase] | High/Med/Low | High/Med/Low | [Action] |
| [Risk from gap] | [Phase] | Likelihood | Impact | [Action] |

## Recommended Actions

### Immediate (To Complete Current Phase)
1. [Action to complete current phase]
2. [Action to complete current phase]

### Next (To Enable Phase Transition)
1. [Action for phase transition]
2. [Action for phase transition]

### Suggested Skills to Run
- `/[skill]` - [Purpose]
- `/[skill]` - [Purpose]

## Vision to Value Flow Visualization

```
Phase 1          Phase 2          Phase 3          Phase 4          Phase 5          Phase 6
Strategic    →   Strategic    →   Strategic    →   Coordinated  →   Business     →   Learning
Foundation       Decisions        Commitments      Execution        Outcomes         Loop

[STATUS]         [STATUS]         [STATUS]         [STATUS]         [STATUS]         [STATUS]
```
```

## Instructions

1. Ask what initiative to assess
2. Review available documentation and context
3. Audit deliverables for each phase
4. Determine current phase and status
5. Identify gaps blocking progression
6. Assess readiness for next phase
7. Provide recommendations and suggested skills

## When to Use

- At the start of work on any initiative
- Before making commitments (to verify Phase 1 & 2 complete)
- When inheriting an initiative from someone else
- During portfolio reviews
- When progress seems blocked

## Related Skills

- `/commitment-check` - Detailed Phase 3 readiness
- `/ownership-map` - Validate ownership across phases
- `/portfolio-status` - See all initiatives and phases

## Phase Descriptions

| Phase | Name | Purpose | Key Question |
|-------|------|---------|--------------|
| 1 | Strategic Foundation | Understand the market and opportunity | "Where should we play?" |
| 2 | Strategic Decisions | Make commercial and positioning choices | "Is this viable?" |
| 3 | Strategic Commitments | Lock in roadmap, GTM, requirements | "Are we committed?" |
| 4 | Coordinated Execution | Execute with cross-functional coordination | "Are we ready to launch?" |
| 5 | Business Outcomes | Realize customer value and track results | "Did it work?" |
| 6 | Learning Loop | Extract learnings and feed back | "What did we learn?" |

## Operating Principle

> "You can't skip phases without accumulating risk debt. Know where you are, know what's missing, close the gaps before moving forward."

---

# v5.1 Hard-Gate Extensions

The block below executes ONLY when `selected_mode == v5.1` (or `selected_mode == v5.2`). In `v5.0` mode this entire section is suppressed and the output ends at the Operating Principle above. In v5.1 mode the section is appended verbatim, and its sub-blocks fire conditionally based on which phase transition the user named.

If `selected_mode == v5.2`, prepend this header line: `# TODO v5.2: sub-Series-C lane reserved by V5.2-S43 — current behavior identical to mode: v5.1.`

## Phase 2 → Phase 3 Hard-Gate (V5.1-23)

This hard-gate fires when the user's invocation names a Phase 2 → Phase 3 transition. Trigger signals: input mentions "Phase 2 to 3", "ready to commit", "advance to commitment", "Phase 3 advance"; OR `args:` contains `transition=2-to-3`. If no Phase 2 → 3 transition is named, output a `Phase 2→3 Hard-Gate Check: Not applicable — no Phase 2→3 transition requested.` line and skip the rest of this section.

### Gate logic

The Phase 2 → 3 advance is gated on a passing Continuation Threshold evaluation. The Continuation Threshold is the affirmative gate the bet must clear before more capital is committed at the next checkpoint. The threshold is DEFINED upstream in the bet's `/business-case` (§11.5, the `continuation_threshold` field) and EVALUATED at gate firing by the standalone `/continuation-threshold` skill. This hard-gate does not re-evaluate the threshold; it consumes the already-produced verdict and the `re_decision_triggers_minimum_met` signal from the bound business case.

Steps:

1. **Resolve the bound `/business-case`**. Search the initiative's documentation set (per `business-case/SKILL.md` search locations: `business/`, `strategy/`, `proposals/`, `cases/`) for a business case bound to this initiative. If no business case is found, the gate FIRES with `Blocker: business case missing — Phase 2 cannot be deemed complete without a /business-case artifact bound to this initiative`.
2. **Read the `continuation_threshold` field** (§11.5 of the business case). If the field is absent or empty, the gate FIRES with `Blocker: business case present but continuation_threshold field unpopulated — invoke /business-case in UPDATE mode to declare next_gate_firing, threshold_criteria, and re_decision_triggers_minimum`.
3. **Read the `continuation_threshold_declared` conformance signal** from the business case's §13. If FALSE, the gate FIRES with `Blocker: continuation_threshold_declared signal is FALSE — the business case is incomplete and cannot be consumed at the gate`.
4. **Read the `re_decision_triggers_minimum_met` signal** (computed at audit time per §13 of `/business-case`). If FALSE, the gate FIRES with `Blocker: too many of the bet's named re-decision triggers have fired — the original commitment is no longer the same commitment; route to /continuation-threshold for a Reopen verdict and back to portfolio review`.
5. **Look for a current `/continuation-threshold` evaluation** in `reviews/threshold-evaluations/` or the bet's folder. If absent, the gate FIRES with `Blocker: no current /continuation-threshold evaluation on file — invoke /continuation-threshold to produce a pass / fail / reopen verdict against the threshold defined in the business case`.
6. **Read the verdict from the most recent evaluation**. If verdict is `Pass` AND the evaluation's `re_decision_triggers_minimum_met` is TRUE → gate OPENS. If verdict is `Fail` → gate FIRES with `Blocker: /continuation-threshold returned Fail — bet thesis disproven at this gate; route to /bet-invalidation-checkpoint for continue / pivot / kill verdict, do not advance Phase 3`. If verdict is `Reopen` → gate FIRES with `Blocker: /continuation-threshold returned Reopen — original commitment no longer the same commitment; route back to portfolio review (/portfolio-tradeoff or /strategic-bet update) before any Phase 3 advance`.

### Output structure (Phase 2 → 3)

Append this section to the v5.0 output verbatim:

```markdown
## Phase 2→3 Hard-Gate Check (v5.1)

**Source artifact**: [Path to bound /business-case, or "Not found"]
**continuation_threshold field**: [Populated / Absent]
**continuation_threshold_declared signal**: [TRUE / FALSE]
**re_decision_triggers_minimum_met signal**: [TRUE / FALSE]
**/continuation-threshold evaluation**: [Path to most recent evaluation, or "Not found"]
**Verdict from /continuation-threshold**: [Pass / Fail / Reopen / Not produced]

**Gate Status**: ✅ OPEN — Phase 2 → Phase 3 advance authorized / ❌ BLOCKED — see specific gap below

**Specific Gap (only if BLOCKED)**: [Name the exact missing artifact / field / signal / verdict]

**Required action**: [Route to /business-case UPDATE, /continuation-threshold CREATE, /portfolio-tradeoff, or /bet-invalidation-checkpoint — pick the correct routing per the gap above]
```

## Phase 3 → Phase 4 Hard-Gate (V5.1-24)

This hard-gate fires when the user's invocation names a Phase 3 → Phase 4 transition. Trigger signals: input mentions "Phase 3 to 4", "ready to execute", "advance to execution", "Phase 4 advance"; OR `args:` contains `transition=3-to-4`. If no Phase 3 → 4 transition is named, output a `Phase 3→4 Hard-Gate Check: Not applicable — no Phase 3→4 transition requested.` line and skip the rest of this section.

### Gate logic

The Phase 3 → 4 advance is gated on a `COMMITTED` Five Signals Verdict from `/commitment-check`. The Five Signals are: Capital envelope named, Continuation threshold named, Re-decision triggers named, Record location and auditable-by named, Exit condition named (per `commitment-check/SKILL.md` Five Signals Checklist Artifact, lines 144-161). A bet missing any signal is a verbal commitment, not a real one — and a verbal commitment is the failure mode this gate is built to catch.

Steps:

1. **Resolve the bound `/commitment-check` artifact** for this initiative. Search `commitment-checks/`, the initiative's documentation set, and `context/decisions/[YYYY]/` for a commitment-check bound to this initiative. If no commitment-check is found, the gate FIRES with `Blocker: /commitment-check missing — Phase 3 cannot be deemed complete without a commitment-check artifact bound to this initiative`.
2. **Read the Five Signals Verdict field** (per `commitment-check/SKILL.md` Five Signals Checklist Artifact). The verdict is read mechanically — do not re-evaluate the signals here, do not infer the verdict from adjacent context. If the field is absent (commitment-check predates V5.1-19 Five Signals enforcement), the gate FIRES with `Blocker: /commitment-check artifact present but Five Signals Verdict field absent — re-run /commitment-check to produce the verdict per V5.1-19 Five Signals enforcement`.
3. **Check the verdict value**:
   - `COMMITTED` (all five signals PASS) → gate OPENS.
   - `NOT COMMITTED` (one or more signals FAIL) → gate FIRES with `Blocker: Five Signals Verdict is NOT COMMITTED — bet remains a verbal commitment until the named signal gap is closed`. Name the specific failed signal(s) by number and the missing field per the commitment-check's `Specific Gaps Named` list.

### Output structure (Phase 3 → 4)

Append this section to the v5.0 output (after the Phase 2→3 section if both gates fired, or directly after the v5.0 Operating Principle if only this gate fires):

```markdown
## Phase 3→4 Hard-Gate Check (v5.1)

**Source artifact**: [Path to bound /commitment-check, or "Not found"]
**Five Signals Verdict field**: [COMMITTED / NOT COMMITTED / Field absent]

**Five Signals breakdown** (only if NOT COMMITTED):
| # | Signal | Status | Specific Gap |
|---|--------|--------|--------------|
| 1 | Capital envelope named | ✅ PASS / ❌ FAIL | [Field missing — floor / envelope / disclosure threshold] |
| 2 | Continuation threshold named | ✅ PASS / ❌ FAIL | [Field missing — class / amount / date] |
| 3 | Re-decision triggers named | ✅ PASS / ❌ FAIL | [Category missing — outcome / market / counterparty] |
| 4 | Record location and auditable-by named | ✅ PASS / ❌ FAIL | [Record absent / Auditor unnamed] |
| 5 | Exit condition named | ✅ PASS / ❌ FAIL | [Path unnamed / Trigger conditions unnamed] |

**Gate Status**: ✅ OPEN — Phase 3 → Phase 4 advance authorized / ❌ BLOCKED — Five Signals not all PASS

**Specific Gap (only if BLOCKED)**: Signal [N]: [exact field missing per commitment-check's Specific Gaps Named list]

**Required action**: Re-run `/commitment-check` to close the named Five Signals gap. A NOT COMMITTED verdict blocks Phase 4 advance independent of any other readiness signal — including a strong supporting-categories scorecard.
```

## Wrapper Cross-References

- **`/business-case`** §11.5 — defines the Continuation Threshold consumed by the Phase 2→3 hard-gate. See `business-case/SKILL.md`.
- **`/continuation-threshold`** — produces the pass / fail / reopen verdict consumed by the Phase 2→3 hard-gate. See `continuation-threshold/SKILL.md`.
- **`/commitment-check`** Five Signals Checklist Artifact — produces the COMMITTED / NOT COMMITTED verdict consumed by the Phase 3→4 hard-gate. See `commitment-check/SKILL.md` lines 144-161.
- **`/strategic-bet`** — upstream artifact carrying the named re-decision triggers and capital envelope that flow through `/business-case` into the Phase 2→3 hard-gate.

## Wrapper Operating Principle

> "Default-to-v5.0 is what makes the wrapper safe. v5.0 callers reach v5.0 behavior unambiguously without specifying any parameter; v5.1 extensions are opt-in by the new code path. The hard-gates are the structural mechanism that turns Phase transitions from soft conventions into auditable gates — but only for callers who opt into v5.1."
