---
name: launch-narrative-brief
description: 'Author or critique a Launch Narrative Brief — a Product Marketing Manager pre-commitment artifact instantiating the Decision Interface Charter at release altitude across nine fields (bet-fit, message hierarchy, named-alternative competitive frame, proof obligation, success-chain instrumentation, re-decision trigger, Director sign-off, sales handoff, audit rights). Activate when: "launch narrative brief", "release narrative brief", "PMM brief", "narrative brief for [release]", "critique my launch brief", pre-commitment narrative artifact, Appendix A brief Do NOT activate for: positioning statement (/positioning-statement), GTM strategy (/gtm-strategy), launch readiness gate (/launch-readiness), campaign brief (/campaign-brief), sales enablement package (/sales-enablement)'
argument-hint: '[release name] or [update path/to/brief.md] or [critique path/to/draft.md]'
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: product-marketing
  skill_type: task-capability
  owner: director-product-marketing
  sensitive: false
  primary_consumers:
  - pmm
  - pmm-dir
  - product-marketing-manager
  - director-product-marketing
  secondary_consumers:
  - pm
  - product-manager
  - ci
  - competitive-intelligence
  - prodops
  - product-operations
  - cmo
  - marketing-dir
  - sales-dir
  - sales-engineer
---
## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Critique**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "critique", "review my brief", "audit this brief" + draft path | CRITIQUE | 100% |
| "update", "revise" in input + path | UPDATE | 100% |
| File path provided (`@path/to/brief.md`) without critique signal | UPDATE | 100% |
| "create", "new", "draft" in input | CREATE | 100% |
| "the brief", "our narrative brief" | UPDATE | 85% |
| Just release name | CREATE | 60% |

**Threshold**: ≥85% auto-proceed | 70-84% state assumption | <70% ask user.

### Mode Behaviors

**CREATE**: Walk the user field by field through the nine canonical fields below. For each field surface the prompt question, accept the answer (or an explicit deferral with reason), and assess against the quality bar before moving on. Output a structured brief artifact at `launch-narrative-briefs/[release-slug].md` plus a JSON sidecar at `launch-narrative-briefs/[release-slug].json` for downstream skill consumption.

**UPDATE**:
1. Read existing brief at the supplied path.
2. Identify which of the nine fields the user is updating.
3. Preserve unchanged fields exactly.
4. Re-assess updated fields against the quality bar.
5. If Field 7 (Director sign-off) is being modified, require a new reasoning paragraph and date — old sign-off does not survive substantive change.
6. Show diff summary and version bump.

**CRITIQUE**: Read the supplied draft, walk Fields 1–9, return a structured findings list with severity tags (P0 blocker / P1 important / P2 nice-to-have), per-field diagnosis, and the named gap to close. Do not edit the draft; produce findings the author closes themselves.

### Search Locations for Briefs

- `launch-narrative-briefs/`
- `gtm/`
- `marketing/briefs/`
- `releases/`

---

## Vision to Value Phase

**Phase 2: Strategic Decisions** — the Launch Narrative Brief is a strategy formulation artifact, sitting alongside the Product Requirements Document (Product Management's instance) and the partnership architecture artifact (Business Development's instance) as the third primitive of how the organization decides what to ship and how to ship it.

**Prerequisites**: a named portfolio bet on the Product Leadership Team's portfolio record (Field 1 has nothing to trace to without it), a current `/positioning-statement` (Field 2 inherits Tier 1 and Tier 2 frame from it), a current `/gtm-strategy` (Field 1's bet-fit trace inherits the multi-quarter motion).

**Outputs used by**: `/launch-readiness` (gates the release on whether Field 7 is signed and Field 5 instrumentation is live), `/sales-enablement` (produces the Field 8 handoff artifact), `/campaign-brief` (inherits Field 2's message hierarchy and Field 4's proof obligations as constraints), `/launch-plan` (schedules activity sequence against Field 5 cadence). At T+90, the brief is one of the inputs to the Director of Product Marketing's standing PMM Charter review.

**Operating principle**: this artifact operationalises Vision to Value Principle 5 — go-to-market is a strategic choice. A brief that cannot be reconstructed in thirty seconds by a Product Marketing Manager who was not in the room fails the same hygiene rule the Board Bet Review Charter carries.

---

## What this brief is — and what it is not

The Launch Narrative Brief is a Product Marketing Manager's instance of the Decision Interface Charter. It is not a marketing memo, and it is not a positioning statement. It is the pre-commitment artifact that hardens nine specific positioning judgments into a record the organization can be held to ninety days later. The brief sits at strategy formulation altitude. `/positioning-statement` is its upstream input (the category-frame artifact owned independent of any specific release). `/gtm-strategy` is its other upstream input (the multi-quarter motion artifact). The brief is more specific than positioning and more release-shaped than go-to-market strategy; both feed it, and neither replaces it.

The skill walks the user through nine fields in canonical order. Field 1 anchors the brief to the strategic bet. Fields 2 through 6 do the substantive positioning work. Field 7 is the signature authority gate. Fields 8 and 9 are the handoff and audit rails. Skipping a field or filling it weakly is what the quality bar at the end of the field is designed to catch. The fields are authored in the order below, which is not the order they appear in any downstream collateral.

---

## The nine fields

### Field 1 — Bet fit

**What it captures.** One sentence naming the strategic bet from the portfolio record that this release serves. The bet is named by its portfolio identifier, not by descriptive paraphrase. The sentence makes the trace explicit: this release is one of the increments by which the named bet moves. If the release does not trace to a named bet on the portfolio record, this field cannot be filled — the Appendix A signal that the release is a feature announcement rather than an instrumented bet move.

**Why it matters.** Bet-fit is the gating question before any positioning work happens. A release that does not move a named portfolio bet has no business consuming the rest of the brief's apparatus — the message hierarchy work, the proof obligation, the success-chain instrumentation. Field 1 is the cheapest gate in the whole template. Either it holds or it does not, and if it does not, the right move is to stop the brief and route the release decision back to the Product Leadership Team's portfolio record before resuming.

**Prompt question.** "Which named portfolio bet does this release serve, and what is the one-sentence trace from the bet to the release?" Follow-up if the user pushes back: "If you cannot name the bet, the release is a feature announcement rather than a bet increment. Do you want to escalate to portfolio review before continuing?"

**Quality bar.** A strong Field 1 names the bet by its portfolio identifier (e.g., "Bet-2026-Q2-04 — Vertical expansion into mid-market healthcare") and writes one sentence of trace ("This release ships the vertical-specific compliance posture the bet's quarterly increment commits to"). A weak Field 1 names a theme rather than a bet ("aligned with our healthcare strategy"), names a feature rather than a bet ("ships our HIPAA controls"), or paraphrases without a portfolio-record identifier. The fix for weak Field 1 is always the same: pull up the portfolio record, find the bet, name it.

**Example output.**
> Bet-fit: This release moves Bet-[portfolio identifier] — *[bet title from portfolio record]* — by shipping the [specific increment, e.g., "vertical-specific compliance posture"] the bet's Q[quarter] continuation threshold commits to.

---

### Field 2 — Three-tier message hierarchy

**What it captures.** Three layered messages, each with a named owner. Tier 1 is the one sentence the category needs to hear — the message that lands at trade-press altitude and corporate brand altitude, owned by the Chief Marketing Officer's narrative. Tier 2 is the one sentence the buyer needs to hear to shortlist — the message that lands in the buyer's evaluation memo, owned by Product Marketing's positioning. Tier 3 is the three to five product-specific sentences the evaluator needs to hear to choose — the messages that land in the evaluator's hands during the bake-off, owned by Product Marketing with Product Management input. Each tier names its owner explicitly. A tier without a named owner drifts to whoever writes the collateral first, which is the failure mode the field exists to prevent.

**Why it matters.** Three-tier messaging is the structural answer to a recurring Product Marketing failure mode: one message fired at three altitudes simultaneously, hitting none of them well. Tier 1 against an evaluator is too abstract to drive a choice. Tier 3 against trade press is too narrow to drive a category move. The hierarchy makes the audience-altitude commitment explicit at brief stage, before any collateral is written. The owner naming on each tier is the second mechanism: it is the empowerment-tier discipline that keeps Tier 1 from being rewritten by the collateral-writer and keeps Tier 3 from being rewritten by the corporate-narrative team.

**Prompt question.** "What is the one-sentence Tier 1 message (category altitude, CMO-owned), the one-sentence Tier 2 message (buyer altitude, PMM-owned), and the three-to-five-sentence Tier 3 message (evaluator altitude, PMM with Product Management input)? Name an owner on each tier." Follow-up: "If you cannot name an owner on any tier, the tier will drift. Whose name goes on each one?"

**Quality bar.** A strong Field 2 has three distinct messages calibrated to three distinct audiences with a named owner on each. Tier 1 makes a category claim that is specific enough to be defensible (not "we're better at X"). Tier 2 makes a shortlist claim a buyer can carry into their evaluation memo. Tier 3 enumerates three to five concrete capability claims an evaluator can verify. A weak Field 2 collapses to one message repeated three times, lists messages without owners, or assigns an owner to one tier and leaves the others unowned.

**Note.** The three-tier shape is also exposed as a standalone skill, `/messaging-architecture`. Use that skill when the message hierarchy is the only artifact needed; use this brief when the hierarchy is one of nine fields the release commits to.

**Example output.**
> *Tier 1 (Category — owner: [CMO name]).* "[one-sentence category claim, e.g., 'Compliance posture is the new buying criterion in mid-market healthcare software.']"
>
> *Tier 2 (Buyer — owner: [PMM-Dir name]).* "[one-sentence shortlist claim, e.g., '[Product] is the only [category] platform that ships HIPAA-attested controls without a six-week security review cycle.']"
>
> *Tier 3 (Evaluator — owner: [PMM name], with input from [PM name]).*
> 1. [capability claim 1]
> 2. [capability claim 2]
> 3. [capability claim 3]
> (Add up to two more if the release warrants; do not exceed five.)

---

### Field 3 — Named-alternative competitive frame

**What it captures.** The two or three named competitive alternatives the buyer will evaluate this release against, and the differentiation axis Product Marketing owns against each one. "Named" is the load-bearing word. Generic competitive frame — "our market-segment competitors," "the rising challengers in the space," "incumbent platforms" — does not count. The alternative is named by company and product (e.g., "Acme Inc.'s Acme Suite v3.2"), and the differentiation axis is one short sentence ("we own the integration depth axis; they own the price axis").

**Why it matters.** Buyers evaluate against named alternatives, not against abstract market frames. A brief that does not name the alternatives the buyer will carry into their evaluation has no positioning information that survives first contact with the buyer's procurement memo. The named-alternative discipline also forces Product Marketing to commit to which axis they are competing on — and which axis they are conceding. A release that claims to win on every axis against every competitor is a release whose positioning will collapse the first time a buyer asks a comparison question.

**Prompt question.** "Name the two or three competitive alternatives a buyer will shortlist alongside this release. For each, name the differentiation axis Product Marketing is committing to on this release." Follow-up: "If you cannot name a real alternative the buyer will consider, the brief has no competitive frame the field-facing teams can defend. Who do buyers actually evaluate against?"

**Quality bar.** A strong Field 3 names two or three alternatives by company and product, and names a single differentiation axis per alternative in one short sentence. A weak Field 3 names "the competition" without specifics, names alternatives that buyers do not actually shortlist (e.g., a category leader the buyer has already excluded for budget reasons), or claims differentiation on every axis against every alternative. If the brief author cannot name an alternative the buyer is genuinely choosing between, the brief is being authored against an internal narrative, not a buyer reality.

**Example output.**
> *Alternative 1.* [competitor product name, e.g., "Acme Suite v3.2"]. Differentiation axis: [one-sentence axis, e.g., "we own integration depth into hospital electronic health record systems; Acme owns first-cost pricing for greenfield deployments."]
>
> *Alternative 2.* [competitor product name]. Differentiation axis: [one-sentence axis].
>
> *(Optional Alternative 3 if buyer regularly evaluates against three.)*

---

### Field 4 — Proof obligation

**What it captures.** The evidence Product Marketing commits to producing within ninety days of release, traceable to the Tier 1, 2, and 3 messages from Field 2. If the Tier 1 message claims category leadership in X, the proof obligation names the metric that operationalises "category leadership in X," the source system that produces the metric, and the publish date by which the proof artifact will be public. Proof obligations are not aspirational; they are the field by which Product Marketing pre-commits to what it will be held accountable for ninety days after release.

**Why it matters.** Messaging without proof obligation is messaging that drifts. Tier 1 messages in particular tend to be written aspirationally (the category claim sounds good in a press release) and then quietly under-supported (no metric, no source, no publish date) once the release ships. The proof obligation field forecloses that drift by requiring the brief to commit, at pre-commitment altitude, to the artifact that will validate or invalidate the message ninety days later. It is the empowerment-tier mechanism that turns Tier 1 messaging from category aspiration into category commitment.

**Prompt question.** "For each tier of the message hierarchy in Field 2, name the proof obligation: the metric, the source system, and the publish date by which Product Marketing will produce evidence the message holds." Follow-up: "If a tier's message has no proof obligation, the message will not be defensible at T+90. Which message do you want to soften, or which proof do you want to commit to?"

**Quality bar.** A strong Field 4 has one proof obligation per message tier, each with a named metric, a named source system, and a publish date inside the ninety-day window. A weak Field 4 lists qualitative proof ("customer testimonials"), names a metric without a source ("brand-search lift" with no source system), or commits to a publish date outside the ninety-day window. The single most common failure mode is committing to a Tier 1 proof that no team owns the data for; the fix is always to name the data owner explicitly, even if the answer is "Marketing Operations does not produce this metric and we need to either produce it or soften the Tier 1 claim."

**Example output.**
> *Tier 1 proof.* Metric: [e.g., "share of mid-market healthcare requests-for-proposal naming [Product] in shortlist"]. Source: [e.g., "Sales Operations RFP-tracking system, [dataset]"]. Publish date: T+[e.g., "60 days post-release, in the Q[quarter] Product Marketing review"].
>
> *Tier 2 proof.* Metric: [metric]. Source: [system]. Publish date: T+[days].
>
> *Tier 3 proof.* Metric: [metric]. Source: [system]. Publish date: T+[days].

---

### Field 5 — Success chain instrumentation

**What it captures.** Three metrics that together constitute the success chain for this release: an awareness metric (owned by Marketing), an adoption metric (owned by Product Management), and a revenue metric (owned by Sales Operations). Each metric is named with its source system, its cadence of read, and its named owner. The three metrics are not interchangeable; they form a chain — awareness drives consideration, consideration drives adoption, adoption drives revenue — and a release that instruments only one or two breaks the chain at the un-instrumented link.

**Why it matters.** The success chain is the answer to the recurring failure mode where Marketing reports awareness lift, Product reports adoption, and Sales reports bookings, and no one owns the question of whether the awareness-to-adoption-to-revenue chain actually held. Without the three-link instrumentation declared at brief time, the post-release review collapses into three separate function-owned status updates that cannot be reconciled. Naming all three metrics with all three owners at brief time is the structural mechanism that makes the post-release review a chain-integrity review rather than three parallel monologues.

**Prompt question.** "Name the awareness metric (owner: Marketing), the adoption metric (owner: Product), and the revenue metric (owner: Sales Operations). For each: name the source system, the cadence at which the metric is read, and the named owner." Follow-up: "If any of the three metrics is missing, the success chain has an un-instrumented link and the post-release review will not be reconcilable. Which link is breaking?"

**Quality bar.** A strong Field 5 names all three metrics with source system, cadence, and owner. The metrics are causally adjacent (awareness lift drives consideration, which drives adoption, which drives revenue); they are not three parallel surface metrics. A weak Field 5 names one or two metrics, names metrics that do not chain together (e.g., three brand metrics with no adoption or revenue link), or names a metric without an owner. Releases that ship with a broken success chain at brief stage almost always ship with a broken post-release review at T+90.

**Example output.**
> *Awareness.* Metric: [e.g., "qualified-lead volume from healthcare-vertical sources"]. Source: [e.g., "Marketing Automation, attribution model X"]. Cadence: weekly. Owner: [Marketing Manager name].
>
> *Adoption.* Metric: [e.g., "new accounts activating HIPAA-attested workspace within 14 days of signup"]. Source: [e.g., "Product analytics, event Y"]. Cadence: weekly. Owner: [Product Manager name].
>
> *Revenue.* Metric: [e.g., "closed-won annual contract value tagged to the healthcare-vertical campaign"]. Source: [e.g., "Customer Relationship Management system, opportunity-tag Z"]. Cadence: weekly. Owner: [Sales Operations Analyst name].

---

### Field 6 — Re-decision trigger

**What it captures.** The specific signal that would reopen the positioning decision after the release ships. The trigger is named with a quantitative threshold ("if cohort adoption at Week 4 is below 40 percent of target across two consecutive releases"), a time window, and the action it triggers ("reopen the positioning frame in the next quarterly portfolio review"). The trigger is not an alarm; it is a pre-committed decision to revisit the positioning rather than continue defending it when specific evidence accumulates.

**Why it matters.** Re-decision triggers are the empowerment-tier mechanism by which the portfolio review converts from a status forum into a decision forum. A release that ships without a named re-decision trigger is a release whose positioning will be defended past the point where the evidence supports it — because there is no pre-committed trip-wire that gives anyone permission to reopen the positioning conversation. The trigger does not promise the positioning will change; it pre-commits to revisiting the question when the named evidence lands. Field 6 is the field that makes the brief a Decision Interface Charter rather than a marketing memo.

**Prompt question.** "Name the specific signal that would reopen the positioning decision after this release ships. Include the quantitative threshold, the time window, and the action the trigger fires." Follow-up: "If the brief has no re-decision trigger, the positioning will be defended past the evidence. Which signal would tell you to reopen?"

**Quality bar.** A strong Field 6 has a named threshold (a number, not a vibe), a named time window, and a named action. The threshold is calibrated against the success-chain metrics in Field 5, so the trigger is operationalisable from existing instrumentation. A weak Field 6 says "if results are disappointing we will reconsider," names a threshold without a time window, or names an action that does not actually reopen the positioning decision (e.g., "we will run a retrospective"). The retrospective is fine, but a retrospective without a portfolio-review re-decision authority is a conversation, not a decision.

**Example output.**
> *Trigger.* If [success-chain metric, e.g., "Tier 2 buyer-shortlist proof in Field 4"] is below [threshold, e.g., "60 percent of target"] at T+[time window, e.g., "60 days post-release"], the positioning frame is reopened at the next quarterly portfolio review per Appendix A's Decision Provenance Standard, and Product Marketing authors a refreshed Field 2 message hierarchy as the input to that review.

---

### Field 7 — Director of Product Marketing sign-off

**What it captures.** The signature gate. The brief is not approved until the Director of Product Marketing has signed Fields 1 through 6 on the record, with date and reasoning. Sign-off is not a checkbox; the Director writes a short paragraph naming what they are signing for ("I am signing for the buyer-altitude shortlist claim in Tier 2 and the three-link success chain in Field 5, and explicitly accepting the conceded axis named against Alternative 1 in Field 3"). The reasoning is what makes the sign-off auditable later.

**Why it matters.** Field 7 is what converts the brief from a draft into a Decision Interface Charter. Without a named signatory and a recorded reasoning paragraph, the brief is a document anyone can edit later under pressure from the field, the engineering team, or the executive sponsor. The signature gate is the structural mechanism that makes the brief survive the inevitable post-brief pressure to soften the message hierarchy, broaden the competitive frame, weaken the proof obligation, or remove the re-decision trigger. The Director's signature, with reasoning, is what the empowerment-tier review six months later audits against. The Director who signs is the Director who pays the political cost if the brief gets watered down without re-signature.

**Prompt question.** "Name the Director of Product Marketing who is signing this brief, the date of sign-off, and the one-paragraph reasoning that names what they are explicitly committing to." Follow-up: "If the Director has not yet signed, the brief is a draft, not a charter. The downstream skills (`/launch-readiness`, `/sales-enablement`, `/campaign-brief`) should not consume an unsigned brief."

**Quality bar.** A strong Field 7 names the signatory, the date, and a reasoning paragraph that explicitly references the choices in Fields 1 through 6. A weak Field 7 has a name and a date with no reasoning, or has reasoning that paraphrases the brief rather than naming what the Director is committing to. The single most common failure mode is a brief that is signed by Product Marketing's collateral lead rather than the Director of Product Marketing — the empowerment-tier discipline only holds at director altitude or above.

**Example output.**
> *Signatory.* [Director of Product Marketing name]. *Date.* [YYYY-MM-DD].
>
> *Reasoning.* "I am signing for: the bet-fit trace in Field 1; the three-tier message hierarchy in Field 2 with named owners on each tier; the named-alternative competitive frame in Field 3 with the conceded axis explicitly accepted against Alternative [N]; the proof obligation publish dates in Field 4; the three-link success chain in Field 5 with named owners; the re-decision trigger threshold in Field 6. I am not signing for: [any field the Director is consciously deferring on, e.g., 'Tier 1 message ownership remains with the CMO; my signature does not bind the CMO's narrative team']."

---

### Field 8 — Sales enablement handoff

**What it captures.** The named artifact delivered to Sales as a consequence of this brief — battlecard, demo flow, objection handler, discovery guide — with a named owner on the Sales side and a named delivery date. Field 8 is the mechanism by which the brief commits to handing off a usable artifact to the field-facing team rather than leaving Sales to infer the brief's content from collateral. The handoff is a deliverable, not a meeting.

**Why it matters.** A brief that does not produce a Sales-side artifact has not actually closed the loop between positioning altitude and field altitude. The recurring failure mode is a brief that is excellent at brief altitude and absent at field altitude — the battlecard the Sales team actually uses was written by someone else, weeks later, under pressure, without reference to the brief. Field 8 forecloses that drift by naming, at brief time, what is being handed off, who on the Sales side owns it, and when. The named owner on the Sales side is the second mechanism: handoffs without a named recipient land in a shared inbox and never reach a representative.

**Prompt question.** "What artifact is being handed off to Sales as a consequence of this brief? Who on the Sales side owns it? What is the delivery date?" Follow-up: "If the artifact is not named or the Sales-side owner is not named, the brief will not reach the field. Which gap is open?"

**Quality bar.** A strong Field 8 names the artifact (specific, e.g., "named-alternative battlecard for Acme Suite v3.2"), names the Sales-side owner (a person, not a function), and names the delivery date inside the post-release window. A weak Field 8 names "the standard launch package" without specifics, names the function rather than the owner, or names a date that slips after the release ships. The Sales-side owner is the field that most often goes unfilled; the answer is always to name a specific person and accept the political cost of having committed them.

**Example output.**
> *Artifact.* [e.g., "Named-alternative battlecard for Alternative 1 (Acme Suite v3.2), with the integration-depth differentiation axis from Field 3 as the load-bearing claim, and three discovery-call questions tied to Tier 3 messages from Field 2"].
>
> *Sales-side owner.* [Sales Enablement lead or Sales Engineering manager name].
>
> *Delivery date.* [YYYY-MM-DD, no later than release date minus 14 days].

The handoff itself is produced by `/sales-enablement` — Field 8 names what that skill must deliver and to whom.

---

### Field 9 — Auditable-by

**What it captures.** The three functions that can read the brief on demand and audit it against their own instrumentation: Marketing (for awareness integrity, against the Field 5 awareness metric), Product (for adoption integrity, against the Field 5 adoption metric), Sales Operations (for revenue integrity, against the Field 5 revenue metric). All three names are explicit. The brief is one of the inputs to the CPO–CMO interface and to the Director of Product Marketing's standing PMM Charter; Field 9 is what makes the audit rights structural rather than negotiated case-by-case.

**Why it matters.** Audit rights are the empowerment-tier mechanism that prevents the brief from being a Product-Marketing-only artifact that no one outside Product Marketing has standing to challenge. Marketing's audit right against the awareness metric is what catches a Tier 1 message whose proof obligation is unsupported by Marketing's own data. Product's audit right against the adoption metric is what catches a Tier 3 message whose evaluator-altitude claims are not supported by actual usage. Sales Operations' audit right against the revenue metric is what catches a Field 8 sales-enablement artifact that is not actually moving pipeline. Field 9 names the audit relationships at brief time so that none of the three functions has to negotiate access to the brief at the moment they need it.

**Prompt question.** "Name the three audit relationships: Marketing (against the awareness metric in Field 5), Product (against the adoption metric in Field 5), Sales Operations (against the revenue metric in Field 5). For each, name the function lead who has audit rights." Follow-up: "If any of the three audit relationships is unnamed, the brief is not auditable at the relevant function, and the success chain in Field 5 is one-sided."

**Quality bar.** A strong Field 9 names the three audit relationships with a function lead on each. The audit rights are operationalisable — each named lead has access to the source system in Field 5 and standing to read the brief without per-instance permission. A weak Field 9 names the functions without leads ("Marketing audits awareness"), names a lead without source access ("the CMO audits awareness" when the CMO's team does not own the source system), or omits one of the three. The audit rights are not optional; this is the field that makes the brief survive cross-functional disagreement six months later.

**Example output.**
> *Marketing audit (awareness integrity).* [Director of Marketing name]. Standing access to the source system in the Field 5 awareness metric.
>
> *Product audit (adoption integrity).* [Director of Product Management name]. Standing access to the source system in the Field 5 adoption metric.
>
> *Sales Operations audit (revenue integrity).* [Sales Operations Director name]. Standing access to the source system in the Field 5 revenue metric.

---

## Output Structure

```markdown
# Launch Narrative Brief: [Release Name]

**Brief ID**: LNB-[YYYY]-[NNN]
**Release**: [Release name]
**Status**: Draft / In Review / Signed / In Effect / Re-decision Triggered
**Author**: [Product Marketing Manager name]
**Date authored**: [YYYY-MM-DD]
**Date signed**: [YYYY-MM-DD or "Unsigned"]

---

## Field 1 — Bet fit
[One sentence naming the portfolio bet and the trace.]

## Field 2 — Three-tier message hierarchy
**Tier 1 (Category — owner: [name]).** [One sentence.]
**Tier 2 (Buyer — owner: [name]).** [One sentence.]
**Tier 3 (Evaluator — owner: [name], with input from [name]).**
1. [Capability claim 1]
2. [Capability claim 2]
3. [Capability claim 3]

## Field 3 — Named-alternative competitive frame
**Alternative 1.** [Company + product]. Axis: [one sentence].
**Alternative 2.** [Company + product]. Axis: [one sentence].

## Field 4 — Proof obligation
**Tier 1 proof.** Metric / Source / Publish date.
**Tier 2 proof.** Metric / Source / Publish date.
**Tier 3 proof.** Metric / Source / Publish date.

## Field 5 — Success chain instrumentation
**Awareness.** Metric / Source / Cadence / Owner.
**Adoption.** Metric / Source / Cadence / Owner.
**Revenue.** Metric / Source / Cadence / Owner.

## Field 6 — Re-decision trigger
[Threshold / time window / action.]

## Field 7 — Director of Product Marketing sign-off
**Signatory.** [Name]. **Date.** [YYYY-MM-DD].
**Reasoning.** [One paragraph naming exactly what is being signed for and what is not.]

## Field 8 — Sales enablement handoff
**Artifact.** [Specific artifact name.]
**Sales-side owner.** [Person name, not function.]
**Delivery date.** [YYYY-MM-DD, no later than release date minus 14 days.]

## Field 9 — Auditable-by
**Marketing audit.** [Director of Marketing name].
**Product audit.** [Director of Product Management name].
**Sales Operations audit.** [Sales Operations Director name].

---

## Appendix — Quality bar self-check

- [ ] Field 1 names a portfolio bet by identifier
- [ ] Field 2 has three tiers, three named owners, three distinct messages calibrated to three altitudes
- [ ] Field 3 names two or three real alternatives by company and product, with one axis per alternative
- [ ] Field 4 has a metric, source, and publish date for each message tier, all inside T+90
- [ ] Field 5 names three causally adjacent metrics with source, cadence, and owner
- [ ] Field 6 has a quantitative threshold, time window, and named action
- [ ] Field 7 has a Director sign-off with reasoning paragraph
- [ ] Field 8 names a specific artifact, a Sales-side owner (a person), and a date
- [ ] Field 9 names three audit leads with standing access to Field 5 source systems
```

---

## Critique-mode output structure

When invoked in Critique mode against a draft brief, return:

```markdown
# Critique: [Brief title or path]

**Verdict**: GO / GO WITH CHANGES / NEEDS REWORK

## P0 Findings (Blocker — brief cannot be signed without resolving)
- **Field [N]**: [What is missing or weak.] [Why it blocks sign-off.] [The named gap to close.]

## P1 Findings (Important — should be resolved before sign-off; may be accepted-with-risk by Director)
- **Field [N]**: [Diagnosis.] [Suggested close.]

## P2 Findings (Nice-to-have — author's discretion)
- **Field [N]**: [Diagnosis.]

## Quality bar score
- Field 1: pass / weak / missing
- Field 2: pass / weak / missing
- ... (through Field 9)
- **Total**: [N]/9 passing
```

---

## Cross-references

| Skill | Relationship |
|-------|--------------|
| `/positioning-statement` | Upstream input — provides the category-frame Tier 1 and Tier 2 in Field 2 inherit |
| `/messaging-architecture` | Sister skill — exposes Field 2's three-tier shape as a standalone artifact |
| `/gtm-strategy` | Upstream input — provides the multi-quarter motion Field 1 traces to |
| `/launch-readiness` | Downstream consumer — gates the release on whether Field 7 is signed and Field 5 instrumentation is live |
| `/sales-enablement` | Downstream consumer — produces the Field 8 handoff artifact |
| `/campaign-brief` | Downstream consumer — inherits Field 2 message hierarchy and Field 4 proof obligations as constraints |
| `/launch-plan` | Downstream consumer — schedules activity sequence against Field 5 cadence |
| `/decision-record` | Adjacent — used to record the Director sign-off reasoning if the brief sets precedent |
| `/outcome-review` | T+90 — reviews whether the brief held against Field 4 proof obligations and Field 5 metrics |

---

## Instructions

1. **Detect the mode** (Create / Update / Critique) using the table above. If confidence is below 70 percent, ask.
2. **In Create mode**, walk Fields 1 through 9 in canonical order. Surface the prompt question. Accept the answer or an explicit deferral with reason. Assess against the quality bar before moving on.
3. **Stop the brief at Field 1 if bet-fit fails.** A release that does not trace to a named portfolio bet should not consume the rest of the apparatus. Route to portfolio review.
4. **In Update mode**, preserve unchanged fields exactly. If Field 7 is touched, require new signatory + new date + new reasoning paragraph; old sign-off does not survive substantive change.
5. **In Critique mode**, do not edit. Produce a structured findings list with severity tags. Verdict at top.
6. **Save outputs** to `launch-narrative-briefs/[release-slug].md` plus a JSON sidecar `[release-slug].json` with the nine fields as keys for downstream skill consumption.
7. **Tag the brief with a Brief ID** of the form `LNB-[YYYY]-[NNN]` for context-graph linkage.
8. **Cross-reference the upstream artifacts** (`/positioning-statement`, `/gtm-strategy`) by file path or document identifier in the brief's metadata. A brief without upstream traces is a brief without context.

---

## Gotchas

- The brief is not a positioning statement. Do not duplicate `/positioning-statement` output here. Field 2 inherits Tier 1 and Tier 2 frame from the positioning statement; the brief is where it is operationalised at release altitude.
- The brief is not a launch plan. `/launch-plan` schedules activities; this brief commits to the message hierarchy, proof obligations, and audit rails.
- Sign-off is at Director altitude or above. A brief signed by a Product Marketing Manager rather than the Director of Product Marketing fails the empowerment-tier discipline.
- Proof obligations are pre-commitments, not aspirations. A Tier 1 proof committed to without a named source system and publish date inside T+90 is a Tier 1 message that should be softened.
- Re-decision triggers are pre-committed trip-wires, not retrospective topics. A trigger without a quantitative threshold is not a trigger.
- The named-alternative discipline is load-bearing. "The competition" is not a named alternative; "Acme Inc.'s Acme Suite v3.2" is.
