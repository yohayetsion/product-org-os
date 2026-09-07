<!--
This template instantiates a Decision Interface Charter per V2V Standard §3.

The Vision to Value book (V5.2.2) Appendix C documents 8 historical Charters from which Data / Engineering / PMM / Customer-Outcome four were canonicalized per locked decision D10.

The book's Appendix C 8 Charters are preserved book-internally (per R5-L meta-pattern reframe). This substrate template is for AUTHORING NEW Decision Interface Charters; see V2V book Appendix C for historical lineage.

See also: V2V Standard PRINCIPLES.md Move E "Standard-as-Bridge" — Charters are the bridge between strategic intent and execution. Schema binding: ../../standard/v5.0/schemas/charter.schema.json
-->

# Decision Interface Charter: Engineering Decisions

**Charter ID**: `engineering-decisions`
**Charter Name**: Engineering Decision Interface Charter
**Decision Class**: Engineering Decision
**Charter State**: `open`
**Created At**: {ISO-8601 datetime}

## Accountable Owner

```yaml
accountable_owner:
  full_name: "{Named human}"
  role: "{Tech Lead / Chief Architect — owns technical architecture, release, and tech debt decisions}"
  employer: "{Organization}"
```

> Single named human. One and only one.

## Mode Declaration

```yaml
mode_declaration: mode-1
```

<!--
Default: mode-1 (Human-Led, AI-Enforced) — engineering decisions are typically authored by Tech Lead / Chief Architect with AI workers (e.g., CI checks, dependency scanners, architecture-conformance bots) enforcing the decisions. Switch to mode-2 if AI workers are AUTHORING architecture or release decisions (e.g., autonomous auto-merge of certain dependency updates) and humans review before action — disclosure_metadata_pointer becomes REQUIRED. mode-1-with-embedded-mode-2-summary covers Mode 1 Charters where individual records contain AI-generated content (e.g., AI-drafted RFCs reviewed by a human).
-->

## Scope

**Inside this Charter**:
- {Technical architecture and stack decisions}
- {Release cadence, branching strategy, deployment process}
- {Tech debt prioritization and retirement}
- {Security architecture, dependency management}

**Outside this Charter**:
- {Product feature decisions — see PM/Product Charter}
- {Data architecture — see Data Charter}
- {GTM and launch decisions — see PMM Charter}

## Cadence

```yaml
cadence:
  frequency: "Release-aligned"
  trigger: "Per-release-cycle architecture review; ad-hoc on tech-debt-emergency or security-event"
```

<!-- Release-aligned chosen as default: engineering decisions are most naturally tied to release boundaries (sprint, train, milestone). Cadence frequency reflects your release model (continuous, sprint-based, quarterly train). -->

## Record Location

```yaml
record_location: "{URL or path — must be findable in 30 seconds by someone not in the room}"
```

## Schedule of Records

```yaml
schedule_of_records:
  - "Per-release Architecture Decision Records"
  - "Tech Debt Prioritization Decisions (quarterly)"
  - "Security Architecture Decisions (event-triggered)"
```

## Re-Decision Triggers

```yaml
re_decision_triggers:
  - trigger_type: outcome_evidence
    trigger_description: "{e.g., Release failure rate exceeds threshold for 2+ cycles, or P0 production incident traced to architectural choice}"
  - trigger_type: market_evidence
    trigger_description: "{e.g., Major framework/runtime EOL announcement, or new security regulation imposing technical constraint}"
```

## Escalation Rule

```yaml
escalation_rule: "{Pointer to /escalation-rule skill output for this Charter}"
```

## Peer Reviewer Pool

```yaml
peer_reviewer_pool:
  - { full_name: "{Name 1}", role: "{Senior Engineer / Staff Engineer}", employer: "{Org}" }
  - { full_name: "{Name 2}", role: "{Architect (different domain)}", employer: "{Org}" }
  - { full_name: "{Name 3}", role: "{Security or SRE Lead}", employer: "{Org}" }
```

## Conformance Level Declared

```yaml
conformance_level_declared: 1
```
