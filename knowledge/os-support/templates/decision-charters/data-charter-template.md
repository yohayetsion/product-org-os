<!--
This template instantiates a Decision Interface Charter per V2V Standard §3.

The Vision to Value book (V5.2.2) Appendix C documents 8 historical Charters from which Data / Engineering / PMM / Customer-Outcome four were canonicalized per locked decision D10.

The book's Appendix C 8 Charters are preserved book-internally (per R5-L meta-pattern reframe). This substrate template is for AUTHORING NEW Decision Interface Charters; see V2V book Appendix C for historical lineage.

See also: V2V Standard PRINCIPLES.md Move E "Standard-as-Bridge" — Charters are the bridge between strategic intent and execution. Schema binding: ../../standard/v5.0/schemas/charter.schema.json
-->

# Decision Interface Charter: Data Decisions

**Charter ID**: `data-decisions` <!-- stable identifier; survives ownership change -->
**Charter Name**: Data Decision Interface Charter
**Decision Class**: Data Decision
**Charter State**: `open` <!-- transitions: open → mode-declared → fields-required → fields-completed → closed -->
**Created At**: {ISO-8601 datetime}

## Accountable Owner

```yaml
accountable_owner:
  full_name: "{Named human}"
  role: "{Data Lead — owns data architecture, model design, and governance decisions}"
  employer: "{Organization}"
```

> Single named human. One and only one. Role title not enough — the schema requires a name.

## Mode Declaration

```yaml
mode_declaration: mode-1
```

<!--
Default: mode-1 (Human-Led, AI-Enforced) — data decisions are typically authored by Data Lead with AI workers checking conformance against schema/governance rules. Switch to mode-2 if AI workers are AUTHORING data architecture choices (e.g., automated schema migration recommendations) and humans review before action. mode-1-with-embedded-mode-2-summary applies when individual decision records contain AI-generated summaries (e.g., AI-drafted query optimization rationale) within a human-authored Charter.

If mode-2 is selected, disclosure_metadata_pointer becomes REQUIRED (Article 50 attaches).
-->

## Scope

**Inside this Charter** (decisions this Charter governs):
- {Data model and schema design}
- {Data pipeline and ETL architecture}
- {Data governance, retention, classification}
- {Query layer, semantic layer, metric definitions}

**Outside this Charter**:
- {Engineering implementation choices — see Engineering Charter}
- {Customer outcome metrics — see Customer-Outcome Charter}

## Cadence

```yaml
cadence:
  frequency: "Monthly cycle"
  trigger: "Standing monthly Data Decision Review; ad-hoc on schema-breaking-change events"
```

<!-- Monthly cycle chosen as default: data decisions are typically less time-sensitive than engineering release decisions but more frequent than quarterly customer-outcome reviews. Adjust to your organization's actual cadence. -->

## Record Location

```yaml
record_location: "{URL or path — must be findable in 30 seconds by someone not in the room}"
```

## Schedule of Records

```yaml
schedule_of_records:
  - "Monthly Data Architecture Decisions"
  - "Schema Change Records (event-triggered)"
  - "Governance Policy Decisions (quarterly)"
```

> Committed enumerated set of decision records this Charter will produce. Used by `commitment-check` to verify Charter is producing actual records.

## Re-Decision Triggers

```yaml
re_decision_triggers:
  - trigger_type: outcome_evidence
    trigger_description: "{e.g., Data quality SLA breached for 2+ consecutive cycles}"
  - trigger_type: market_evidence
    trigger_description: "{e.g., Regulatory change (GDPR/CCPA/ISO 42001) creates new data-handling obligation}"
```

> Minimum: 1 outcome-evidence + 1 market-evidence trigger per V2V Ch. 6.

## Escalation Rule

```yaml
escalation_rule: "{Pointer to /escalation-rule skill output for this Charter}"
```

## Peer Reviewer Pool

```yaml
peer_reviewer_pool:
  - { full_name: "{Name 1}", role: "{Data Architect}", employer: "{Org}" }
  - { full_name: "{Name 2}", role: "{Data Governance Lead}", employer: "{Org}" }
  - { full_name: "{Name 3}", role: "{Senior Data Engineer}", employer: "{Org}" }
```

> Minimum 3 named individuals before transitioning to `fields-completed`. Eligibility: substantive expertise + author exclusion + Charter-owner exclusion when Charter owner authored + recusal carve-out.

## Conformance Level Declared

```yaml
conformance_level_declared: 1
```

<!-- Level 1: Standard signals fire at state transitions. Level 2/3: additional reviewer-attestation and audit-trail obligations attach. -->
