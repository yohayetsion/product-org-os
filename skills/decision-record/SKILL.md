---
name: decision-record
description: 'Create or update a structured record for a specific individual decision, aligned with the Vision to Value Standard decision-record schema (Section 5). Activate when: "document this decision", "create decision record", "record the choice we made", formal decision documentation,
  DR. Do NOT activate for: recurring decision type charters (/decision-charter), decision quality audits (/decision-quality-audit), escalation rules (/escalation-rule)'
argument-hint: '[decision topic] or [update DR-2026-001]'
user-invocable: true
metadata:
  author: Product Org OS
  category: decisions
  skill_type: task-capability
  owner: bizops
  primary_consumers:
  - cpo
  - vp-product
  - pm-dir
  - pm
  - bizops
  - bizdev
  - general-counsel
  - legal-dir
  - contracts-counsel
  - privacy-counsel
  - ip-counsel
  - compliance-officer
  - employment-counsel
  - chief-architect
  - ai-architect
  - api-architect
  - cloud-architect
  - data-architect
  - security-architect
  - head-corpdev
  - ma-analyst
  - corporate-venture
  - strategic-partnerships
  - cs-dir
  - data-lead
  - data-analyst
  - bi-engineer
  - ml-engineer
  - experimentation-analyst
  - design-dir
  - tech-lead
  - frontend-dev
  - backend-dev
  - devops
  - qa-engineer
  - ceo
  - cmo
  - cfo
  - chro
  - coo
  - cio
  - finance-dir
  - fpa-analyst
  - revenue-analyst
  - financial-controller
  - treasury-analyst
  - tax-planning
  - investor-relations
  - hr-dir
  - recruiter
  - compensation-analyst
  - performance-specialist
  - people-analyst
  - onboarding-specialist
  - it-dir
  - enterprise-systems
  - data-governance
  - it-security-policy
  - marketing-dir
  - content-strategist
  - cro-specialist
  - email-marketer
  - growth-marketer
  - infographic-designer
  - market-researcher
  - paid-media-manager
  - pr-comms-specialist
  - presentation-designer
  - seo-specialist
  - social-media-manager
  - video-producer
  - operations-dir
  - program-manager
  - project-manager
  - process-engineer
  - procurement-specialist
  - risk-manager
  - sales-dir
  - sales-engineer
  - account-exec
  - sales-ops
  - proposal-writer
  - pa
  - analyst
  secondary_consumers:
  - pmm-dir
  - pmm
  - ci
  - prodops
  - value-realization
  - cs-ops
  - csm
  - onboarding-csm
  - support-lead
  - kb-specialist
  - ui-designer
  - interaction-designer
  - visual-designer
  - user-researcher
  - motion-designer
  - copywriter
  - sdr
  vision_to_value_standard:
    aligned: true
    section: "Section 5 (Required Artifact Set)"
    state_machine: "../../standard/v5.0/state-machines/decision-record-state-machine.md"
    schema: "../../standard/v5.0/schemas/decision-record.schema.json"
    additional_required_fields:
    - dispatch_mode
    - disclosure_metadata_pointer
    - mode_classification_attestation
    - layer_2_audit_trail
    layer_2_hard_gate_at_close: true
    layer_4_attestation_required_at_close: true
    emits_signals:
    - every_record_carries_mode_declaration
    - every_mode_2_record_has_disclosure_block
    - every_mode_1_edge_case_record_has_disclosure_block
    - disclosure_block_required_fields_populated
    - escalation_rule_records_present_when_invoked
    - disclosure_review_cadence_current
---
## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "revise", "modify" in input | UPDATE | 100% |
| File path provided (`@path/to/decision.md`) | UPDATE | 100% |
| Decision ID mentioned (`DR-2026-001`) | UPDATE | 100% |
| "create", "new", "record" in input | CREATE | 100% |
| "find", "search", "list decisions" | FIND | 100% |
| "the decision", "that decision" | UPDATE | 85% |
| Just decision topic | CREATE | 60% |

**Threshold**: ≥85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Generate complete new decision record using template below.

**UPDATE**:
1. Read existing decision (search if path not provided)
2. Preserve unchanged sections exactly
3. Update status, add new context, modify rationale
4. Show diff summary: "Updated: [sections]. Unchanged: [sections]."
5. Consider: Should status change (e.g., Proposed → Accepted)?

**FIND**:
1. Search paths below AND context registry for decisions
2. Present results: ID, title, date, status, owner
3. Ask: "Update one of these, or create new?"

### Search Locations for Decision Records

- `decisions/`
- `context/decisions/`
- `docs/decisions/`
- `adr/` (architecture decision records)

---
## Gotchas

- Always document at least 2-3 alternatives considered — a decision with no alternatives wasn't a decision
- Single accountable owner required — never 'the team' or 'leadership'
- Re-decision triggers must be specific events or thresholds, not calendar dates



Create a **Decision Record** to document a specific decision.

## Vision to Value Phase

**Phase 2: Strategic Decisions** - Decision records document choices made during the commercial filter phase.

**Prerequisites**: Context understood, options identified
**Outputs used by**: Phase 3 (roadmap, GTM commitments), context registry

## Purpose
Decision records capture the context, options, and rationale for important decisions, enabling future teams to understand why decisions were made.

## Minting the Decision ID (do this FIRST)

**Reserve the ID with the allocator — never by reading the context decision index for the highest number and adding one:**

```bash
python tools/allocate-id.py --ns DR --note "<short reason>"
```

Use the printed id verbatim. **If it exits non-zero, do NOT guess a number** — re-run it; it refuses exactly when it cannot prove the id is free. Read-the-index-and-add-one is what collided five ids across five namespaces on 2026-08-02 — two of them *during* the cleanup fixing the first three — because two concurrent sessions read the same maximum before either wrote. The allocator makes read-max and claim-it a single atomic step, and records the reservation before any file exists.

(Collision-safe across concurrent sessions on one machine, not across machines. If `tools/allocate-id.py` is absent from this workspace, fall back to reading the index — and verify the id is still free immediately before **and after** the write.)

## Output Structure

```markdown
# Decision Record: [Decision Title]

**Decision ID**: DR-[YYYY]-[NNN]   ← from `allocate-id.py --ns DR`, not hand-picked
**Charter ID**: [charter_id this DR dispatches under, or "unchartered" if none]
**Date**: [Date decided]
**Record State** (DPS): dispatched / drafted / review-required / closed   (agents may set up to `drafted`; only a named human affirms `closed`)
**Status**: Proposed / Accepted / Superseded / Deprecated
**Dispatch Mode** (DPS): mode-1 / mode-2 / mode-1-with-embedded-mode-2-summary
**Accountable Owner**: [Single person/role who can say yes/no]
**Product**: [Product name - optional, for multi-product organizations]

## Context

[Why this decision is needed now. What problem or opportunity prompted this decision? What constraints exist?]

## Decision Drivers

- [Driver 1]: [Description]
- [Driver 2]: [Description]
- [Driver 3]: [Description]

## Options Considered

### Option A: [Name]
**Description**: [What this option entails]

| Pros | Cons |
|------|------|
| [Pro 1] | [Con 1] |
| [Pro 2] | [Con 2] |

**Effort**: Low / Medium / High
**Risk**: Low / Medium / High

### Option B: [Name]
**Description**: [What this option entails]

| Pros | Cons |
|------|------|
| [Pro 1] | [Con 1] |
| [Pro 2] | [Con 2] |

**Effort**: Low / Medium / High
**Risk**: Low / Medium / High

### Option C: [Name]
**Description**: [What this option entails]

| Pros | Cons |
|------|------|
| [Pro 1] | [Con 1] |
| [Pro 2] | [Con 2] |

**Effort**: Low / Medium / High
**Risk**: Low / Medium / High

## Decision Made

**Selected Option**: [Option name]

**Rationale**: [Why this option was chosen over others. What were the key factors that tipped the decision?]

## Customer Value Link (Principle #3)

**Customer Problem**: [What customer problem does this decision address?]
**Customer Benefit**: [How will customers benefit from this decision?]
**Evidence**: [What customer evidence supports this direction?]

*If this decision has no customer value link, document why (internal efficiency, technical debt, etc.)*

## Stakeholders Consulted (Principle #6)

| Stakeholder | Role | Input Provided | Input Incorporated? |
|-------------|------|----------------|---------------------|
| [Name] | [Role] | [Summary of input] | Yes/Partial/No |
| [Name] | [Role] | [Summary of input] | Yes/Partial/No |

**Who should have been consulted but wasn't?** [Names or "None"]
**Why?** [Reason if applicable]

## Key Assumptions

| Assumption | Confidence | Validation Method | If Wrong |
|------------|------------|-------------------|----------|
| [Assumption 1] | High/Med/Low | [How we'll know] | [Impact] |
| [Assumption 2] | High/Med/Low | [How we'll know] | [Impact] |

## Success Criteria

| Metric | Target | Timeframe | How Measured |
|--------|--------|-----------|--------------|
| [Metric 1] | [Target] | [When] | [Method] |
| [Metric 2] | [Target] | [When] | [Method] |

## Re-decision Trigger

This decision should be revisited if:
- [Condition 1]
- [Condition 2]
- [Condition 3]

## Implementation Notes

[Any specific guidance for implementing this decision]

## Contributors

| Name | Role | Contribution |
|------|------|--------------|
| [Name] | [Role] | Accountable |
| [Name] | [Role] | Input provided |
| [Name] | [Role] | Consulted |

## Decision Provenance Standard — Close Block

> This block is what the Decision Provenance Standard captures and attests on. A DR is not `closed` until a named human completes it. An AI agent may populate the draft and leave the human-gated fields as `[PENDING HUMAN AFFIRMATION]`; it must NOT self-populate them.

**Disclosure (required when Dispatch Mode = mode-2 or mode-1-with-embedded-mode-2-summary):**
- **Drafting Authority**: [deployer role / AI system name + version that drafted, or "human-authored" for clean mode-1]
- **Disclosure Metadata Pointer**: [pointer to disclosure block, or "n/a (mode-1)"]

**Layer 2 — Substantive-Authorship Challenge** (Mode-1 close gate; the human declaring authority answers Yes/No/Uncertain):
- Q1 Did AI worker output materially shape the options framing? [ ]
- Q2 Did AI worker output materially shape the recommended/rejected options or criteria? [ ]
- Q3 Is AI-drafted prose reproduced verbatim/near-verbatim in this record? [ ]
- Q4 If all AI contributions were removed, would the conclusion stand unchanged? [ ]

**Layer 4 — Named Human Attestation (REQUIRED to reach `closed`):**
- **Attestor Full Name**: [PENDING HUMAN AFFIRMATION]
- **Role / Title**: [PENDING HUMAN AFFIRMATION]
- **Employer**: [PENDING HUMAN AFFIRMATION]
- **Capacity**: employee / contractor / officer / director
- **Jurisdiction**: US-DE / US-FED / UK / EU / IL / OTHER
- **Attestation Timestamp**: [system-stamped at human affirmation]
- **Accountable Owner Sign-off**: [PENDING HUMAN AFFIRMATION]

**Re-decision Trigger** (DPS-required at close): [specific event or threshold — not a calendar date]
**Record Location** (DPS-required at close): [resolvable path/URL where this record lives]

## Related Decisions

- [Link to related decision record]
```

## Instructions

1. Ask clarifying questions about the decision if context is unclear
2. **Check prior context**: Run `/context-recall [topic]` to find related past decisions
3. Reference any relevant documents provided via @file syntax
4. Ensure there's a single accountable owner
5. Include measurable success criteria
6. Define clear re-decision triggers
6a. **Set Record State to `drafted`, never `closed`.** Leave all Layer-4 attestation and accountable-owner-signoff fields as `[PENDING HUMAN AFFIRMATION]`. Per the Decision Provenance Standard, only a named human can affirm a record to `closed`. Do not set Status to "Accepted" on the agent's own authority — that reads as a closed record and bypasses the human gate.
7. Save in decisions/ folder
8. Offer to create presentation version using /present

## Context Integration

After generating the decision record:

1. **Offer to save**: Ask "Should I save this to the context registry? (`/context-save`)"
2. If yes, extract and save:
   - Decision ID, title, date, owner, status to `context/decisions/index.md`
   - Tags (auto-generate 3-5 keywords from content)
   - Assumptions to `context/assumptions/registry.md`
   - Full record to `context/decisions/[YYYY]/[DR-ID].md`
3. Link to related decisions if mentioned
