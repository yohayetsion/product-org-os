---
name: decision-charter
description: 'Create a Decision Interface Charter defining ownership and process for recurring decision types, aligned with the Vision to Value Standard charter mechanism (Section 3). Activate when: "who decides what", "decision rights", "decision charter", decision ownership,
  RACI for decisions, recurring decision governance. Do NOT activate for: documenting individual decisions (/decision-record), escalation triggers (/escalation-rule), decision quality audits (/decision-quality-audit)'
argument-hint: '[decision type] or [update path/to/charter.md]'
user-invocable: true
metadata:
  author: Product Org OS
  category: decisions
  skill_type: task-capability
  owner: ceo
  primary_consumers:
  - pm-dir
  - general-counsel
  - ceo
  secondary_consumers:
  - prodops
  vision_to_value_standard:
    aligned: true
    section: "Section 3 (Charter Mechanism)"
    state_machine: "../../standard/v5.0/state-machines/charter-state-machine.md"
    schema: "../../standard/v5.0/schemas/charter.schema.json"
    emits_signals:
    - charter_state_is_fields_completed
    - mode_declaration_populated
    - schedule_of_records_committed
    - record_location_resolvable
    - accountable_owner_named
    - re_decision_triggers_minimum_met
---
## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "revise", "modify" in input | UPDATE | 100% |
| File path provided | UPDATE | 100% |
| Charter ID mentioned (e.g., DIC-2026-001) | UPDATE | 100% |
| "create", "new", "draft" in input | CREATE | 100% |
| "find", "search", "list" | FIND | 100% |
| "the charter", "our charter" | UPDATE | 85% |
| Just decision type | CREATE | 60% |

**Threshold**: ≥85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: If creating a new Decision Interface Charter, choose from named starting points (Data, Engineering, PMM, Customer-Outcome — see "Named Starting Points" section below) OR start from the generic template embedded in this skill for novel decision domains. Named starting points instantiate the 4 canonical Decision Interface Charter classes per V2V book V5.2.2 locked decision D10.

**UPDATE**:
1. Check document registry first, then search user's structure
2. Preserve charter ID and version history
3. Update decision rules, criteria, or escalation paths
4. Show diff summary

**FIND**: Check registry, then search user's folders for charters.

## Named Starting Points

The V2V Standard canonicalizes 4 Decision Interface Charter classes per book V5.2.2 locked decision D10. When creating a new Charter, prefer a named starting point if your decision domain matches one of these four:

| Charter | Template | Decision Class | Default Mode | Default Cadence |
|---|---|---|---|---|
| **Data Decision Interface Charter** | `templates/decision-charters/data-charter-template.md` | Data architecture, model design, governance, query/semantic layer | `mode-1` | Monthly cycle |
| **Engineering Decision Interface Charter** | `templates/decision-charters/engineering-charter-template.md` | Technical architecture, release, tech debt, security architecture | `mode-1` | Release-aligned |
| **PMM Decision Interface Charter** | `templates/decision-charters/pmm-charter-template.md` | Positioning, GTM motion, messaging, launch strategy | `mode-1-with-embedded-mode-2-summary` | Campaign-aligned |
| **Customer-Outcome Decision Interface Charter** | `templates/decision-charters/customer-outcome-charter-template.md` | Value realization, retention, expansion, customer health model | `mode-1` | Quarterly |

**Lineage**: The V2V book V5.2.2 Appendix C documents 8 historical Charters from which these 4 were canonicalized per D10. The 8 are preserved book-internally (per R5-L meta-pattern reframe); the 4 above are the substrate's working set for authoring new Charters.

**Cross-reference**: See PRINCIPLES.md → "Standard-as-bridge" for the conceptual frame. The Decision Interface Charter is the **decision instrument** — the single artifact that governs how a recurring decision is made. It is NOT the bridge: the Standard's affirmable/auditable/resumable **records** are the bridge, between the Product Organization's human custodianship of the decision system and the AI tooling participating in it.

**For decision domains outside the 4 canonical classes**: use the generic Output Structure template embedded in this skill (below) and document the rationale for why a new Charter class is warranted.

---

Create a **Decision Interface Charter** to govern how a recurring type of decision is made.

## Vision to Value Phase

**Phase 2: Strategic Decisions** - Decision charters establish governance for recurring decisions at any phase.

**Prerequisites**: Decision patterns identified, need for consistency recognized
**Outputs used by**: All phases (provides decision governance)

## Purpose
Decision Interface Charters establish the "rules of engagement" for recurring decisions, ensuring consistent quality and accountability.

## Output Structure

```markdown
# Decision Interface Charter: [Decision Type]

**Charter ID**: DIC-[YYYY]-[NNN]
**Version**: 1.0
**Last Updated**: [Date]
**Charter Owner**: [Role responsible for this charter]
**Dispatch Mode** (DPS): mode-1 / mode-2 / mode-1-with-embedded-mode-2-summary

## Decision Scope

**Decision Type**: [What recurring decision this governs]
**Examples**:
- [Example decision 1]
- [Example decision 2]
- [Example decision 3]

**Out of Scope**:
- [What this charter does NOT cover]

## Decision Classification

**Type**: Strategic / Portfolio / Execution
**Frequency**: [How often this decision typically occurs]
**Reversibility**: Low / Medium / High
**Impact**: Low / Medium / High

## Accountable Owner

**Role**: [Role, not person name]
**Authority**: [What they can decide unilaterally]
**Constraints**: [What requires escalation or consultation]

## Decision Forum & Cadence

**Forum**: [Where this is decided - e.g., "Weekly PLT meeting"]
**Cadence**: [When - e.g., "Thursdays 2pm"]
**Quorum**: [Who must be present]
**Duration**: [Expected time allocation]

## Required Inputs

| Role | Input Required | Format | Deadline |
|------|----------------|--------|----------|
| [Role 1] | [What they provide] | [Format] | [When before decision] |
| [Role 2] | [What they provide] | [Format] | [When before decision] |
| [Role 3] | [What they provide] | [Format] | [When before decision] |

## Decision Criteria

**Ready to Decide When:**
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

**Quality Threshold**: [What "good enough" looks like]

## Decision Rules

**How the decision is made:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Tiebreaker**: [How to resolve if no clear answer]

## Escalation Rule

| Trigger | Escalate To | Timeline | Information Required |
|---------|-------------|----------|---------------------|
| [Trigger 1] | [Role] | [When] | [What to provide] |
| [Trigger 2] | [Role] | [When] | [What to provide] |

## Success Criteria

| Metric | Target | Timeframe | Measurement |
|--------|--------|-----------|-------------|
| Leading indicator | [Target] | T+2 weeks | [How measured] |
| Mid indicator | [Target] | T+6 weeks | [How measured] |
| Lagging indicator | [Target] | T+12 weeks | [How measured] |

## Re-decision Trigger

This decision should be revisited when:
- [Trigger 1]
- [Trigger 2]
- [Trigger 3]

## Communication Plan

| Audience | Channel | Timing | Owner |
|----------|---------|--------|-------|
| [Who needs to know] | [How] | [When] | [Who tells them] |

## Peer Reviewer Pool (DPS Layer 3 — minimum 3 named individuals)

| Reviewer | Role | Eligibility (substantive expertise + not the record author) |
|----------|------|------------------------------------------------------------|
| [Name 1] | [Role] | [why eligible] |
| [Name 2] | [Role] | [why eligible] |
| [Name 3] | [Role] | [why eligible] |

*Pool < 3 fails commitment-check (Layer 3 designation rule).*

## Charter Review

**Review Frequency**: [How often to review this charter]
**Next Review**: [Date]
**Review Owner**: [Role]
```

## Instructions

1. Ask about the specific decision type if not clear
2. Reference any governance documents provided via @file syntax
3. Ensure accountable owner is a role, not a person
4. Include specific escalation triggers
5. Define measurable success criteria
6. Save in charters/ folder
7. Offer to create presentation version using /present

## Vision to Value Standard Alignment (v5.0)

This skill is one of the 8 named structural-primitive skills aligned with the Vision to Value Standard charter mechanism. When producing a Charter, the output is structurally compatible with the Standard's Section 3 schema and emits the corresponding Level 1 conformance signals.

### Required mode declaration

Every Charter authored under v5.0 alignment MUST declare its dispatch mode:

| `mode_declaration` value | When to use |
|---|---|
| `mode-1` | Human-Led, AI-Enforced — human authors decisions; AI worker checks against Charter |
| `mode-2` | AI-Led, Human-Reviewed — AI worker authors decisions; human reviews before action (Article 50 disclosure attaches) |
| `mode-1-with-embedded-mode-2-summary` | Mode 1 Charter where individual decisions may embed AI-generated summaries (per-decision-record Article 50 disclosure) |

The enum is exhaustive. No fourth mode. If a fourth mode seems needed, escalate to `general-counsel` + Standard amendment, never a runtime workaround.

### Required peer reviewer pool

Charters MUST populate `peer_reviewer_pool` with at least 3 named individuals before transitioning to `fields-completed`. Pool < 3 fails commitment-check (per Layer 3 designation rule). Eligibility: substantive expertise + author-exclusion + Charter-owner-exclusion when Charter owner authored + recusal carve-out.

### Conformance signals emitted

When a Charter authored via this skill transitions through its lifecycle states, the following Level 1 conformance signals fire (per `../../standard/v5.0/conformance/signal-vocabulary.md`):

`charter_state_is_fields_completed`, `mode_declaration_populated`, `schedule_of_records_committed`, `record_location_resolvable`, `accountable_owner_named`, `re_decision_triggers_minimum_met`.

### State machine reference

See `../../standard/v5.0/state-machines/charter-state-machine.md` for the 5 forward-only states and the `review-required` RECORD-state interrupt.

### Schema reference

See `../../standard/v5.0/schemas/charter.schema.json` for the JSON Schema Draft 2020-12 binding.
