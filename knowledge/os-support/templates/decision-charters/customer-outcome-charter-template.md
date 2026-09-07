<!--
This template instantiates a Decision Interface Charter per V2V Standard §3.

The Vision to Value book (V5.2.2) Appendix C documents 8 historical Charters from which Data / Engineering / PMM / Customer-Outcome four were canonicalized per locked decision D10.

The book's Appendix C 8 Charters are preserved book-internally (per R5-L meta-pattern reframe). This substrate template is for AUTHORING NEW Decision Interface Charters; see V2V book Appendix C for historical lineage.

See also: V2V Standard PRINCIPLES.md Move E "Standard-as-Bridge" — Charters are the bridge between strategic intent and execution. Schema binding: ../../standard/v5.0/schemas/charter.schema.json
-->

# Decision Interface Charter: Customer-Outcome Decisions

**Charter ID**: `customer-outcome-decisions`
**Charter Name**: Customer-Outcome Decision Interface Charter
**Decision Class**: Customer-Outcome Decision
**Charter State**: `open`
**Created At**: {ISO-8601 datetime}

## Accountable Owner

```yaml
accountable_owner:
  full_name: "{Named human}"
  role: "{VP Customer Success / Value Realization Lead — owns value realization, retention, and expansion decisions}"
  employer: "{Organization}"
```

> Single named human. One and only one.

## Mode Declaration

```yaml
mode_declaration: mode-1
```

<!--
Default: mode-1 (Human-Led, AI-Enforced) — customer-outcome decisions are typically authored by VP CS / Value Realization Lead based on customer health data, with AI workers enforcing health-score thresholds and surfacing accounts needing attention. Switch to mode-2 if AI workers are AUTHORING retention/expansion play decisions (e.g., automated playbook assignment based on health score) and humans review before action — disclosure_metadata_pointer becomes REQUIRED.

mode-1-with-embedded-mode-2-summary applies when individual customer-outcome decision records embed AI-generated content (e.g., AI-drafted QBR summaries, AI-generated churn-risk rationale).
-->

## Scope

**Inside this Charter**:
- {Value realization measurement and instrumentation decisions}
- {Retention play / save motion decisions}
- {Expansion / upsell motion decisions}
- {Customer health score model and threshold decisions}

**Outside this Charter**:
- {Product feature priorities driven by customer feedback — see PM/Product Charter}
- {Pricing changes — typically VP Product or BizOps Charter}
- {Support process and SLA — typically CS-Ops Charter}

## Cadence

```yaml
cadence:
  frequency: "Quarterly"
  trigger: "Quarterly Customer Outcome Review (QBR cycle); ad-hoc on churn-spike or expansion-opportunity events"
```

<!-- Quarterly chosen as default: customer-outcome decisions align naturally with QBR cycles, renewal windows, and quarterly value-realization reporting. -->

## Record Location

```yaml
record_location: "{URL or path — must be findable in 30 seconds by someone not in the room}"
```

## Schedule of Records

```yaml
schedule_of_records:
  - "Quarterly Customer Outcome Review Decisions"
  - "Retention Play Decisions (event-triggered)"
  - "Expansion Motion Decisions (per opportunity)"
  - "Health Score Model Updates (semi-annual)"
```

## Re-Decision Triggers

```yaml
re_decision_triggers:
  - trigger_type: outcome_evidence
    trigger_description: "{e.g., Net Revenue Retention drops below target for 2+ consecutive quarters, or value-realization metric stalls across cohort}"
  - trigger_type: market_evidence
    trigger_description: "{e.g., Competitor introduces value-guarantee that changes buyer outcome expectations, or analyst publishes new outcome benchmark}"
```

## Escalation Rule

```yaml
escalation_rule: "{Pointer to /escalation-rule skill output for this Charter}"
```

## Peer Reviewer Pool

```yaml
peer_reviewer_pool:
  - { full_name: "{Name 1}", role: "{Customer Success Director}", employer: "{Org}" }
  - { full_name: "{Name 2}", role: "{Value Realization Lead or Account Executive}", employer: "{Org}" }
  - { full_name: "{Name 3}", role: "{Product Operations or Data Lead}", employer: "{Org}" }
```

## Conformance Level Declared

```yaml
conformance_level_declared: 1
```
