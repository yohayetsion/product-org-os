<!--
This template instantiates a Decision Interface Charter per V2V Standard §3.

The Vision to Value book (V5.2.2) Appendix C documents 8 historical Charters from which Data / Engineering / PMM / Customer-Outcome four were canonicalized per locked decision D10.

The book's Appendix C 8 Charters are preserved book-internally (per R5-L meta-pattern reframe). This substrate template is for AUTHORING NEW Decision Interface Charters; see V2V book Appendix C for historical lineage.

See also: V2V Standard PRINCIPLES.md Move E "Standard-as-Bridge" — Charters are the bridge between strategic intent and execution. Schema binding: ../../standard/v5.0/schemas/charter.schema.json
-->

# Decision Interface Charter: PMM Decisions

**Charter ID**: `pmm-decisions`
**Charter Name**: Product Marketing Decision Interface Charter
**Decision Class**: PMM Decision
**Charter State**: `open`
**Created At**: {ISO-8601 datetime}

## Accountable Owner

```yaml
accountable_owner:
  full_name: "{Named human}"
  role: "{Director of Product Marketing — owns positioning, GTM motion, messaging, and launch decisions}"
  employer: "{Organization}"
```

> Single named human. One and only one.

## Mode Declaration

```yaml
mode_declaration: mode-1-with-embedded-mode-2-summary
```

<!--
Default: mode-1-with-embedded-mode-2-summary — PMM decisions are human-authored (positioning, messaging strategy, GTM motion choices live with the Director PMM), BUT individual marketing collateral records very commonly embed AI-generated content (AI-drafted headlines, AI-generated competitive summaries, AI-translated copy). The embedded mode-2 summary recognizes that reality and attaches per-decision-record Article 50 disclosure obligation to those AI-generated artifacts.

Switch to pure mode-1 if your org does no AI authoring of marketing artifacts under this Charter. Switch to pure mode-2 if AI is AUTHORING the positioning/GTM decisions themselves (rare — typically a Director PMM-level human call).

When mode-2 or mode-1-with-embedded-mode-2-summary is declared, disclosure_metadata_pointer is REQUIRED.
-->

## Scope

**Inside this Charter**:
- {Positioning and category framing}
- {GTM motion (PLG, SLG, hybrid) decisions}
- {Messaging architecture and narrative}
- {Launch strategy and campaign cadence}

**Outside this Charter**:
- {Pricing model and packaging — typically VP Product or BizOps Charter}
- {Product roadmap — see PM/Product Charter}
- {Customer outcome metrics — see Customer-Outcome Charter}

## Cadence

```yaml
cadence:
  frequency: "Campaign-aligned"
  trigger: "Per-campaign launch review; quarterly positioning audit; ad-hoc on competitive-shift events"
```

<!-- Campaign-aligned chosen as default: PMM decisions cluster around launches, quarterly positioning reviews, and reactive competitive events. -->

## Record Location

```yaml
record_location: "{URL or path — must be findable in 30 seconds by someone not in the room}"
```

## Schedule of Records

```yaml
schedule_of_records:
  - "Per-campaign Launch Decisions"
  - "Quarterly Positioning Audit Decisions"
  - "Competitive Response Decisions (event-triggered)"
  - "Messaging Architecture Updates (semi-annual)"
```

## Disclosure Metadata Pointer

```yaml
disclosure_metadata_pointer: "{Path to Article 50 disclosure metadata block — REQUIRED because mode_declaration includes embedded mode-2 summary}"
```

<!-- Required because default mode_declaration is mode-1-with-embedded-mode-2-summary. Article 50 disclosure attaches to the AI-generated content (headlines, summaries, copy) embedded within decision records. -->

## Re-Decision Triggers

```yaml
re_decision_triggers:
  - trigger_type: outcome_evidence
    trigger_description: "{e.g., Campaign conversion rate below threshold for 2+ consecutive launches, or messaging A/B test signals incumbent narrative is losing}"
  - trigger_type: market_evidence
    trigger_description: "{e.g., New entrant repositions the category, or analyst report reframes the buyer; competitive move materially shifts win-rate}"
```

## Escalation Rule

```yaml
escalation_rule: "{Pointer to /escalation-rule skill output for this Charter}"
```

## Peer Reviewer Pool

```yaml
peer_reviewer_pool:
  - { full_name: "{Name 1}", role: "{Product Marketing Manager}", employer: "{Org}" }
  - { full_name: "{Name 2}", role: "{Competitive Intelligence Lead}", employer: "{Org}" }
  - { full_name: "{Name 3}", role: "{Sales / GTM Leader}", employer: "{Org}" }
```

## Conformance Level Declared

```yaml
conformance_level_declared: 1
```
