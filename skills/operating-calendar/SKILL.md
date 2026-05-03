---
name: operating-calendar
description: 'Author or update an Operating Calendar — a published, versioned artifact that sequences the canonical rituals of a product organization across a four-layer cadence stack (team weekly, product-line monthly, portfolio quarterly, customer continuous). Produces structured markdown plus a JSON sidecar for downstream consumption. Activate when: "operating calendar", "cadence stack", "ritual calendar", "rhythm of business", "publish our cadence", "ProdOps calendar", Appendix A Operating Calendar Stub Do NOT activate for: portfolio-level review pre-read (/portfolio-status), maturity rubric for cadence (/maturity-check), per-ritual decision record (/decision-record), launch-readiness gating (/launch-readiness), cadence-adherence telemetry (/cadence-adherence-telemetry — deferred Wave 4)'
argument-hint: '[org name] or [update path/to/operating-calendar.md] or [critique path/to/draft.md]'
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: operations
  skill_type: task-capability
  owner: product-operations
  sensitive: false
  primary_consumers:
  - prodops
  - product-operations
  - cpo
  - vp-product
  secondary_consumers:
  - pm-dir
  - director-product-management
  - pmm-dir
  - director-product-marketing
  - pm
  - product-manager
  - bizops
  - value-realization
  - ci
  - competitive-intelligence
  - cs-dir
  - csm
---
## Purpose

The Operating Calendar is the artifact that converts an organization's rhythm of decisions from "when calendars align" into a published, versioned, audited schedule. It sequences the canonical rituals named throughout the Vision to Value framework into a four-layer cadence stack so the organization stops negotiating its rhythm ad-hoc each quarter.

A calendar that lives only in individual leaders' heads is a Product Operations failure. This skill produces the calendar as an artifact: human-readable markdown for the leadership team and a structured JSON sidecar that downstream skills and integrations can consume.

## Vision to Value Phase

**Cross-phase** — the Operating Calendar carries rituals that span Strategic Foundation through Learning Loop. It is itself a Phase 6 (Learning Loop) artifact because a calendar that does not produce reviewable decision artifacts is a calendar that has stopped serving the loop.

**Prerequisites**: Named ritual owners exist at the four altitudes (team / product-line / portfolio / customer). Decision Record Template (Appendix A) is in use, so the calendar can point at where each ritual writes its output.

**Consumed by**: `/portfolio-status` (pulls the next portfolio-review window), `/maturity-check` (assesses cadence stack against the Three Tiers + sub-Series-C lane), `/cadence-adherence-telemetry` (Wave 4 — measures whether scheduled rituals produced their named output artifacts). The JSON sidecar is the integration substrate; concrete calendar-system integrations (Google Calendar sync, Slack reminders, Outlook sync) are out of scope and live in personal config or Extension Teams per master plan §25 Park bucket §5.

## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Critique**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "critique", "review my calendar", "audit this calendar" + draft path | CRITIQUE | 100% |
| "update", "revise", "refresh" in input + path | UPDATE | 100% |
| File path provided (`@path/to/calendar.md`) without critique signal | UPDATE | 100% |
| "create", "new", "publish our calendar" in input | CREATE | 100% |
| "the calendar", "our cadence stack" | UPDATE | 85% |
| Just org name or org-size descriptor | CREATE | 60% |

**Threshold**: ≥85% auto-proceed | 70–84% state assumption | <70% ask user.

### Mode Behaviors

**CREATE**: Walk the user through the configuration questions below — org size, product-line shape, sub-Series-C vs. Three Tiers altitude, named ritual owners — then emit a customised cadence stack across all four layers. Output a structured calendar at `operating-calendars/[org-slug]-operating-calendar.md` and a JSON sidecar at `operating-calendars/[org-slug]-operating-calendar.json`.

**UPDATE**: Read the existing calendar, identify which fields are changing (ritual ownership, cadence window, pre-read deadline, decision-artifact location), preserve unchanged fields exactly, bump the calendar version, and update the annual review date if the user is performing the annual audit.

**CRITIQUE**: Read the supplied draft, walk the four cadence layers and the per-ritual fields, return findings with severity tags (P0 blocker / P1 important / P2 nice-to-have) against the failure modes named in the Canonical Rituals reference. Do not edit the draft; produce findings the author closes themselves.

## The Four-Layer Cadence Stack

A Vision to Value cadence stack has four layers, each with its own altitude, decision authority, and gating relationship to the layer above. All four are required; an organization missing one is running an incomplete loop. The four layers are:

### Layer 1 — Team weekly (30 minutes)

The Team Outcome Review. Owned by the Product Manager. Attendees: the team, Design, Engineering, Data. Cadence: weekly, immutable — does not move for executive schedules. Output: a written "Did outcomes move? What changed in reality? What's next?" note that lives where teams already write.

**Decision authority at this layer**: scope and sequencing inside the bet's committed envelope. The team decides what to do this week to move the named outcome. The team does NOT decide whether the bet continues — that authority lives at Layer 3 (portfolio).

**Inputs that gate the ritual**: the prior week's outcome note (so the team can see whether outcomes moved), the bet's continuation-threshold field (so this week's work traces back to the threshold the bet must hit), and the customer-continuous signals from Layer 4 that touched this team's surface this week.

**Outputs that leave the ritual**: a written outcome note (decision artifact, archived); any escalation to the product-line review (Layer 2) when the team has surfaced a re-decision question it cannot resolve at its altitude.

**Failure mode (per Canonical Rituals)**: collapses into standup; no outcome link. The cure is the immutable cadence and the named output artifact — both gating fields in this calendar.

### Layer 2 — Product-line monthly (60 minutes)

The Product-line Review. Owned by the Group PM or Director PM. Attendees: line PMs, PMM, CS, Data. Cadence: monthly. Output: bet-level re-decision read — over-performing or under-performing vs. expectations — written down and archived.

**Decision authority at this layer**: cross-team prioritisation inside the product line, intake commitments to platform (when paired with the Platform Intake Council), and bet-level revise signals that feed the portfolio review. Authority does NOT include renew / kill calls on bets — those route to Layer 3.

**Inputs that gate the ritual**: the four prior weekly outcome notes from Layer 1 across the line's teams; Joint Product-GTM Forum outputs (positioning and packaging decisions made since last review); customer-continuous adoption-depth and retention-by-cohort signals from Layer 4 mapped to bets in this product line.

**Outputs that leave the ritual**: a written bet-level re-decision read per active bet in the line (continue / revise-recommend / escalate-for-kill); the intake commitment to platform (if paired); any escalation to the portfolio review (Layer 3) when the line has named a kill candidate it cannot decide at its altitude.

**Failure mode (per Canonical Rituals)**: becomes demo day; no re-decisions. The cure is the named bet-level output artifact and the gating relationship to Layer 3 — Layer 3 cannot adjourn with a continue decision on a bet whose Layer 2 read is missing or stale.

### Layer 3 — Portfolio quarterly (90 minutes)

The Portfolio Review. Owned by VP Product or, at scale, the CPO. Attendees: the Product Leadership Team, Business Operations, Competitive Intelligence. Cadence: quarterly — non-negotiable per the Canonical Rituals table. Output: renew / revise / kill decision per bet plus a refreshed re-decision plan for each bet that exits the review in committed state.

**Decision authority at this layer**: the renew / revise / kill call per bet in the portfolio; capital-envelope reconciliation across bets; the disposition mix that feeds the bet-disposition-mix observability signal per Principle 8. This is the load-bearing decision authority the cadence stack carries — it is what converts the rest of the stack from activity into a learning loop.

**Inputs that gate the ritual** (all required per the sensor-compulsion protocol — if any are absent or stale, the review cannot adjourn with a continue decision on the affected bets): the Portfolio-Review Financial Pre-Read from Business Operations (48 hours before the review), the market-evidence pre-read from Competitive Intelligence, the prior-quarter portfolio-review record (so this review can reconcile dispositions against last quarter's calls), and a refreshed continuation-threshold field on every bet.

**Outputs that leave the ritual**: a written renew / revise / kill decision per bet, archived against the bet's Decision Record; a refreshed continuation threshold for every bet that survives in committed state; any re-decision triggers that fired during the review; the disposition-mix telemetry signal that feeds the next quarter's observability dashboard.

**Failure mode (per Canonical Rituals)**: becomes status readout; no stop decisions made. The cure is the gating sensor inputs and the named decision output — without them the review converges on a status default.

### Layer 4 — Customer continuous (always-on, structured QBR + cohort-health cadences)

The customer-listening rhythm. Owned jointly by Customer Success Director and Value Realization. Attendees: rotating — CSMs hold the day-to-day, with structured Quarterly Business Reviews, cohort-health reviews, and customer-visit programs feeding the higher cadences. Cadence: continuous; not gated by other layers.

**Decision authority at this layer**: account-level health calls, expansion / retention plays, customer-visit prioritisation, the question Principle 8 names — "Which customers or segments are reaching the value we promised, at what rate, and what's driving the gap?"

**Inputs that gate the ritual**: structured customer-visit programs, QBR schedules, cohort health scorecards (the customer-health-scorecard skill is a named input pattern).

**Outputs that leave the ritual** (and feed the higher layers): adoption-depth signal by cohort mapped to bet (feeds Layer 2 product-line review and Layer 3 portfolio review); retention and expansion signal by segment (feeds Layer 3 portfolio review); customer-evidence inputs to the GTM-to-P&L Traceability View; reference-willingness signal that closes the value-realization loop. **If this layer is missing, the product-line and portfolio cadences run on self-reported status, not on realized value** — this is the diagnostic Principle 8 names explicitly.

### The cadence stack as a sequenced loop

The four layers are not parallel; they sequence into the learning loop:

- Layer 1 (team weekly) feeds Layer 2 (product-line monthly) by surfacing weekly outcome reads that aggregate to bet-level reads at the monthly cadence.
- Layer 2 feeds Layer 3 (portfolio quarterly) by producing the bet-level re-decision reads the portfolio review consumes as gating inputs.
- Layer 4 (customer continuous) feeds Layer 2 and Layer 3 by surfacing the realized-value signals that turn the higher cadences from status review into outcome review.
- Layer 3 closes the loop back into Layer 1 by setting the continuation thresholds and re-decision triggers each team carries forward into next week's outcome review.

A calendar that publishes the four layers without naming the gating relationships between them is publishing four meeting series, not a cadence stack. The artifact this skill produces names the relationships explicitly.

## Per-Ritual Fields (Appendix A Operating Calendar Stub)

Each ritual the calendar carries — across all four layers — must name these fields. This is the per-row content of the canonical Operating Calendar Stub.

- **Ritual name** (must match the Canonical Rituals reference table verbatim — Launch Readiness Review, Platform Intake Council, Portfolio Review, Team Outcome Review, Product-line Review, Decision Review (post-launch), Joint Product-GTM Forum, Incident / Reliability Tradeoff Review)
- **Layer** (1 / 2 / 3 / 4 — which altitude in the cadence stack)
- **Owner (accountable)** — single named role; not a team
- **Attendees** — the seats present at the ritual
- **Cadence window** — fixed day and time, not "when calendars align"; for Layer 4 rituals, the structured cadence (QBR every quarter at this offset, cohort review monthly on this day)
- **Pre-read deadline** — how long before the ritual the inputs must land (Layer 3 portfolio review: 48 hours; Layer 2: 24 hours; Layer 1: end of prior business day)
- **Decision artifact location** — where the output will be written; must match the path discipline the Decision Record Template enforces, so the artifact is findable in 30 seconds by someone who was not in the room
- **Re-decision trigger** — the conditions that reopen this ritual's prior decisions between scheduled instances
- **Failure mode reference** — the named failure mode from the Canonical Rituals reference, so the calendar carries its own diagnostic

## Sequencing Rules (stated once at the top of the calendar)

The Operating Calendar Stub names four sequencing rules that govern the relationships between rituals. Every calendar this skill produces must carry them verbatim:

1. Portfolio review sits upstream of product-line review (quarterly before monthly), not the reverse.
2. Launch Readiness Review dates are derived from committed ship dates, not negotiated per-launch.
3. Team Outcome Reviews are immutable weekly — they do not move for executive schedules.
4. A ritual that misses its scheduled window twice in a cycle triggers a charter review, not a calendar slip.

These rules are part of the artifact, not advisory text — they appear in both the markdown output and the JSON sidecar.

## Configuration Questions (CREATE mode)

Walk the user through these questions in order. Each question maps to a field in the JSON sidecar so downstream skills can consume the answers without re-asking.

1. **Organisation name and date of calendar publication**. (Drives the artifact filename and the version-1 review date one year out.)
2. **Altitude of the cadence stack**: Three Tiers (Enabling / Established / Company Leading / Market Leading per the Vision to Value Maturity Blueprint) or sub-Series-C lane (Principle 8 sub-Series-C collapse — single analyst-and-CS-lead, often the same person, layer 4 collapsed into Layer 1)? `/maturity-check` is the upstream skill that resolves this; if the user has not run it, recommend they run it first or default to Three Tiers and flag the assumption.
3. **Number of product lines**. Drives whether Layer 2 is one ritual or several; single-line orgs collapse Layer 2 into the portfolio review at altitude.
4. **Named owner per layer**: Layer 1 (Product Manager — one or many), Layer 2 (Group PM / Director PM — one per product line), Layer 3 (VP Product or CPO at scale), Layer 4 (Customer Success Director and Value Realization lead).
5. **Existing rituals already in cadence**. The calendar this skill produces is rarely greenfield; the user usually has some rituals running. Inventory them against the Canonical Rituals reference; flag rituals named in the reference that are missing from the user's current rhythm.
6. **Decision-artifact home**. Where does this organisation write its decision records? The calendar's `decision artifact location` field must point there. If no consistent home exists, that is a Decision Record Template gap to flag — the calendar cannot finish before the artifact home is named.
7. **Annual review date**. Default: one year from publication date. Per the Operating Calendar Stub, the calendar is itself an artifact subject to annual audit.

## Markdown Output Shape

The skill emits a structured markdown artifact with these sections in this order:

```markdown
# Operating Calendar — [Organisation Name]

**Version**: [N.M] | **Published**: [YYYY-MM-DD] | **Annual review due**: [YYYY-MM-DD]
**Owner**: [Product Operations lead name and role] | **Altitude**: [Three Tiers tier name | sub-Series-C lane]

## Sequencing Rules

[The four sequencing rules verbatim, numbered.]

## Cadence Stack

### Layer 1 — Team weekly
[Per-ritual fields for every Team Outcome Review across teams.]

### Layer 2 — Product-line monthly
[Per-ritual fields for every Product-line Review across product lines, plus Joint Product-GTM Forum and Platform Intake Council if monthly.]

### Layer 3 — Portfolio quarterly
[Per-ritual fields for the Portfolio Review.]

### Layer 4 — Customer continuous
[Per-ritual fields for the QBR cadence, cohort-health review cadence, and customer-visit program cadence.]

## Cross-Layer Rituals

[Decision Review (post-launch) — triggered at T+30 by ship date, not by calendar offset; Launch Readiness Review — derived from committed ship dates per Sequencing Rule 2; Incident / Reliability Tradeoff Review — on-incident plus monthly roll-up.]

## Cadence-Adherence Notes

[Where the cadence-adherence-telemetry skill (Wave 4) will read this calendar. Until that skill ships, this section names the rituals whose adherence is most load-bearing — Layer 3 portfolio review, Layer 1 immutability, Layer 2 monthly bet-level read.]

## Annual Review Log

[Empty on version 1. Populated on each annual audit with the date, the rituals that changed, and the reason.]
```

## JSON Sidecar Shape

The JSON sidecar carries the same content in a structured form for downstream consumption. The schema:

```json
{
  "calendar_version": "1.0",
  "organisation": "[Organisation Name]",
  "published_date": "YYYY-MM-DD",
  "annual_review_due": "YYYY-MM-DD",
  "owner": {
    "name": "[Product Operations lead name]",
    "role": "[role title]"
  },
  "altitude": {
    "model": "three-tiers | sub-series-c",
    "tier": "enabling | established | company-leading | market-leading | sub-series-c"
  },
  "sequencing_rules": [
    "Portfolio review sits upstream of product-line review (quarterly before monthly), not the reverse.",
    "Launch Readiness Review dates are derived from committed ship dates, not negotiated per-launch.",
    "Team Outcome Reviews are immutable weekly — they do not move for executive schedules.",
    "A ritual that misses its scheduled window twice in a cycle triggers a charter review, not a calendar slip."
  ],
  "cadence_stack": {
    "layer_1_team_weekly": [ /* one entry per team */ ],
    "layer_2_product_line_monthly": [ /* one entry per product line, plus Joint Forum and Platform Intake if monthly */ ],
    "layer_3_portfolio_quarterly": [ /* the Portfolio Review entry */ ],
    "layer_4_customer_continuous": [ /* QBR, cohort-health, customer-visit program entries */ ]
  },
  "cross_layer_rituals": [
    /* Launch Readiness Review, Decision Review (post-launch), Incident / Reliability Tradeoff Review */
  ],
  "ritual_entry_schema": {
    "ritual_name": "string (must match Canonical Rituals reference verbatim)",
    "layer": "1 | 2 | 3 | 4 | cross-layer",
    "owner_role": "string",
    "owner_name": "string",
    "attendees": ["array of named seats"],
    "cadence_window": {
      "frequency": "weekly | monthly | quarterly | continuous | triggered",
      "fixed_day_time": "string (e.g., 'Tuesdays 10:00 local')",
      "duration_minutes": "integer"
    },
    "pre_read_deadline_hours": "integer",
    "decision_artifact_location": "string (path or system pointer)",
    "re_decision_trigger": "string",
    "failure_mode_reference": "string (from Canonical Rituals)",
    "inputs_gating": ["array of input artifact names"],
    "outputs_leaving": ["array of output artifact names"]
  },
  "annual_review_log": []
}
```

The `ritual_entry_schema` block documents the shape every ritual entry across the four layer arrays must follow; downstream consumers (e.g., `/cadence-adherence-telemetry` in Wave 4) read against this schema.

## Park-Bucket Note (out of scope)

Per the master execution plan §25 Park bucket §5, downstream calendar-system integrations are explicitly out of scope for this skill. The JSON sidecar is the integration substrate — concrete integrations (Google Calendar sync, Outlook sync, Slack reminders against the cadence windows) live in personal config or Extension Teams, not in the Operating Calendar skill itself. The skill's job is to publish the canonical artifact in markdown and JSON; the artifact is then consumed by whatever calendar surface the organisation already uses.

This boundary is deliberate. Calendar-system integration drift across organisations and across personal vs. corporate boundaries; the Operating Calendar artifact does not. Keeping integration parked preserves the skill's portability across the install base.

## Cross-References

- **`/maturity-check`** (V5.1-26 — Director PM owned): resolves whether the cadence stack runs at Three Tiers altitude (Enabling / Established / Company Leading / Market Leading) or sub-Series-C lane. The `altitude` field in the JSON sidecar is the output of `/maturity-check`. If the user runs `/operating-calendar` without having run `/maturity-check`, default to Three Tiers and flag the assumption.
- **`/portfolio-status`**: pulls the next portfolio-review window from the calendar to anchor its "Upcoming Checkpoints" section. The Operating Calendar is the upstream artifact; `/portfolio-status` is downstream.
- **`/cadence-adherence-telemetry`** (V5.1-31, deferred to Wave 4): reads the ritual entries in the JSON sidecar and reports whether each scheduled ritual produced the named output artifact in the named location on the named cadence. This is the observability skill the calendar enables; it does not exist yet.
- **`/decision-record`**: the calendar's `decision_artifact_location` field must point at where decision records are written. The Decision Record Template (Appendix A) is the artifact home this calendar references.
- **`/launch-readiness`**: Launch Readiness Review dates in the calendar are derived from committed ship dates per Sequencing Rule 2; `/launch-readiness` is the per-launch instance of this ritual.
- **`/portfolio-tradeoff`** and the Portfolio-Review Financial Pre-Read: the Layer 3 portfolio-review entry in the calendar names these as gating inputs.

## Failure Modes This Skill Defends Against

- **Calendar-as-individual-knowledge**. The single failure mode the Operating Calendar Stub names — a calendar living only in individual leaders' heads. The artifact-level cure is publication and versioning; this skill produces both.
- **Rituals without gating relationships**. A calendar that lists four meeting series in parallel, without naming the inputs that gate each ritual and the outputs that leave each ritual, is publishing meetings, not a cadence stack. The cure is the per-ritual `inputs_gating` and `outputs_leaving` fields, both required.
- **Layer 4 missing**. The Principle 8 diagnostic — product-line and portfolio cadences running on self-reported status because the customer-continuous layer was never installed. The skill flags Layer 4 absence as a P0 finding in CRITIQUE mode.
- **Annual review skipped**. The Operating Calendar Stub names annual audit explicitly. The skill carries the `annual_review_due` field in version 1 and refuses to update an existing calendar without bumping the review date or recording an audit entry.
- **Pre-read deadlines absent**. A calendar that names rituals without naming the input artifacts and their pre-read deadlines is a calendar that will run rituals on improvised inputs. Every ritual entry requires a pre-read deadline.

## Output

Present the calendar in scannable markdown format. Offer to:

- Convert to a presentation with `/present` for the leadership-team review where the calendar is published.
- Hand off to `/portfolio-status` to anchor the next portfolio-review window.
- Hand off to `/maturity-check` if the altitude assumption was flagged.
- Schedule the annual review one year out (the JSON sidecar already carries the date).
