---
name: ai-assisted-resolution-strategy
description: Design AI-assisted first-contact resolution strategy with hard CSAT floors, escape hatches, and a never-deflect list.
argument-hint: '[--segmentation FILE] [--health-score FILE] [--languages LIST] [--timezones LIST]'
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: customer-success-operations
  skill_type: task-capability
  owner: support-lead
  primary_consumers:
  - ext-cs
  - cs-tool-selection
  - value-realization
  sensitive: false
aliases:
- ai-deflection-strategy
---
# /ai-assisted-resolution-strategy

> **Alias note.** This skill was previously scoped as `/ai-deflection-strategy`. The alias is still recognized so older plans and context records resolve, but do not use it going forward. "Deflection" framing optimizes for the wrong metric (volume reduction) and is hostile to customers; "assisted resolution" correctly positions AI as a first-contact tool that escalates honestly when it hits its limits. The whole point of this skill is to enforce that honest-escalation posture structurally, not as a reminder.

## Purpose

`/ai-assisted-resolution-strategy` produces a first-contact AI resolution strategy that treats the AI as the junior team member of a support org, not as a cost-reduction device. It bakes in a hard CSAT floor per segment, a three-trigger escape hatch that immediately hands off to a human, a never-deflect list of categories the AI may not attempt at all, and a mandatory rollback plan that fires automatically if the CSAT floor is breached.

The skill's one-sentence job: make sure the customer always has a clean, visible path to a human, and make sure the AI is measured against resolution quality rather than deflection volume.

---

## When to Use

Invoke `/ai-assisted-resolution-strategy` when you need to:

- Launch AI-assisted support for the first time and you need the strategy document before picking a tool
- Trigger a quarterly CSAT review that has surfaced a degradation and you need to refresh the strategy (floors, escape hatches, rollback threshold)
- Add new languages to an existing AI resolution footprint (which reopens the multilingual detection rules for the escape hatch)
- Expand AI-assisted resolution into a new segment, especially a regulated or high-touch one where the previous floors were set for a different customer mix

## When NOT to Use

Do NOT use `/ai-assisted-resolution-strategy` when:

- You need a **single-touch chatbot spec** (scripted decision tree, non-learning) → use a chatbot spec skill, the optimization target is different
- You need to design a **sales chatbot or lead-qualification bot** → optimization target is conversion, not resolution quality
- You need an **AI-authored KB article generator** → that is a content-generation skill, not a live-interaction strategy
- You need a **voice IVR redesign** → channel-specific, different handoff physics, different escape hatch mechanics
- You are looking for **vendor selection** between Intercom Fin / Ada / Zendesk AI / Gladly / Kustomer → that is `/cs-tool-selection`, which this skill feeds

This skill is the strategy layer. Tool selection, vendor evaluation, and prompt-authoring all live in other skills that consume this skill's output.

---

## Inputs

### Required (skill rejects if missing)

1. **Segmentation output** — a `/cs-segmentation-model` artifact or equivalent with at minimum: primary segments and the tier definitions. Segment-specific CSAT floors depend on this. Without it, the skill cannot differentiate enterprise floors from PLG floors.
2. **Health-score baseline** — either a `/health-score-design` artifact or a human-handled CSAT baseline per segment. The skill uses this to compute the per-segment floor (see Step 1). If neither exists, the skill falls back to the 90% absolute floor across all segments and flags this as a low-confidence assumption.
3. **Language list** — every customer-facing language the AI will operate in. Drives the multilingual escape-hatch rules in Step 3.
4. **Timezone list** — every timezone in which human handoff must be available, which constrains the time-boxed escape hatch in Step 3 and the handoff protocol in Step 4.

If any of these is missing, the skill MUST emit an explicit rejection in this shape:

```
ERROR: /ai-assisted-resolution-strategy requires {missing_field}.
Rationale: {why this field is load-bearing}
Provide: {example}
```

No silent defaults for missing inputs beyond the health-score fallback above.

### Optional (improves fidelity)

- **Current AI tool and its telemetry** — if there is a deployed tool, its baseline deflection rate, CSAT, and escape-hatch trigger rate can be used to calibrate the floors more tightly
- **Channel mix** — chat vs. email vs. in-app; escape-hatch mechanics differ (chat is synchronous, email is queued, in-app has session context)
- **Regulatory context** — HIPAA, GDPR, consumer-protection rules that expand the never-deflect list beyond the mandatory four

---

## Method

### Step 1 — Establish CSAT Floors Per Segment

The floor is not a single number. It is computed per segment, and the per-segment floor is the HIGHER of:

- **90% absolute floor** (the non-negotiable global floor for AI-assisted resolution)
- **Human-handled CSAT baseline minus 2 points** (if the segment's human-handled CSAT is 95%, the floor is 93%)
- **Segment-specific floor tied to `/health-score-design`** (if the High-Touch Enterprise segment has a 95% human baseline, their AI floor is 93% regardless of the overall number — enterprise customers earn a higher bar)

Produce a floor table with one row per primary segment:

| Segment | Human baseline | Floor rule | Resulting floor |
|---|---|---|---|
| High-Touch Enterprise | {from input} | max(90, baseline-2) | {computed} |
| Mid-Touch | {from input} | max(90, baseline-2) | {computed} |
| Tech-Touch Pooled | {from input} | max(90, baseline-2) | {computed} |
| PLG Self-Serve | {from input} | max(90, baseline-2) | {computed} |

If no segment baseline exists, fall back to 90 across the board and flag the gap in the output's confidence section. Do NOT invent a baseline.

The floor is the measurement target for Step 5 and the trigger for the rollback plan in Step 6. It is not a soft goal — it is the hard line that forces rollback if breached.

### Step 2 — Define the Never-Deflect List

Four categories are mandatory. The AI may not attempt resolution in any of them; hard refusal with immediate human handoff:

1. **Accessibility requests** — anything touching ADA/WCAG, screen reader support, disability accommodation, hearing-impaired needs, cognitive-load accommodation. Classification rule: keyword match (screen reader, JAWS, NVDA, VoiceOver, accessibility, disability, ADA, WCAG, deaf, blind, low vision, motor, cognitive) + intent classifier flagged as "accessibility" + any mention of an assistive technology. Rationale: missing an accessibility request creates an ADA exposure event and signals the wrong thing to the population that relies on these requests being handled with care.
2. **Billing disputes** — charge disputes, refund requests, payment failures, subscription billing questions, plan-change billing implications, duplicate charges, tax questions. Classification rule: keyword match (refund, dispute, charge, chargeback, overcharge, double-charged, credit, invoice, billing, payment failed, card declined, tax, VAT) + intent classifier flagged as "billing". Rationale: billing disputes are retention-critical, often legally sensitive, and the customer almost always wants a human to own the outcome.
3. **Cancellations and downgrades** — anything that signals retention risk. Classification rule: keyword match (cancel, cancellation, downgrade, delete account, close account, churn, leaving, unsubscribe from the product itself) + intent classifier flagged as "cancellation" + sentiment classifier flagged as frustrated-or-worse. Rationale: this is CSM territory; an AI attempting to "save" the cancellation often makes things worse, and the retention playbook requires a human to judge what to offer.
4. **Safety, legal, and vulnerable customer** — self-harm indicators, legal threats, minors, users in crisis, credible threats to others, safeguarding issues. Classification rule: keyword match against a curated safeguarding vocabulary (maintained by the safety team, not in the skill output) + sentiment classifier output + a hardcoded route to a human-first team regardless of any other signal. Rationale: this category is where "time saved on deflection" becomes actively harmful. The AI cannot be the first line of response under any circumstances. See the handoff protocol in Step 4 for the specific routing rules.

For each category, the output documents:
- The classification rule (keyword + intent + sentiment hybrid)
- The user-visible message the AI produces when it refuses to attempt resolution
- The routing target (which human team / which queue / which priority)
- The escalation SLA for that category

The never-deflect list is a hard refusal. The user cannot override it. If the user explicitly asks for "the AI agent" or "I want the bot to answer this" while in a never-deflect category, the AI politely declines and proceeds with the handoff anyway. An exception to this rule can only be filed via a documented governance change, not a conversation override.

### Step 3 — Design the Three-Trigger Escape Hatch

Any of three triggers, fired independently, immediately stops AI resolution and hands off to a human:

**Trigger 1 — Explicit request.** The user asks for a human, in any supported language. Detection rule: case-insensitive match of the explicit-request vocabulary in the language the user is currently detected to be speaking. Mandatory terms per language (augment as needed):

- English: agent, human, representative, rep, supervisor, manager, person, someone real, real person, real human, escalate, talk to a human, live agent
- Hebrew: נציג, אדם, מישהו אמיתי, מנהל, לדבר עם נציג, לעבור לנציג
- German: Mitarbeiter, Mensch, Vertreter, echter Mensch, Vorgesetzter, mit einem Mitarbeiter sprechen

For each new language added to the AI's footprint, Step 3 MUST be revisited; the output explicitly lists per-language vocabulary. A missing language in the detection table aborts Step 3 and returns to input collection.

**Trigger 2 — Implicit distress.** Either of the following fires the handoff:

- **Sentiment drop** — the sentiment classifier's score drops by ≥X points (default X = 20 on a 0–100 scale) in a single turn compared to the conversation's rolling baseline. This is the "user got visibly angry in the last reply" signal.
- **Loop detection** — more than 2 consecutive turns on the same intent without resolution progress (defined as: no new information surfaced, no action taken, no clarifying question answered). This is the "we're going in circles" signal.

Both sub-triggers are implemented as classifier outputs, not keyword rules. The classifier thresholds are configurable per deployment and MUST be documented in the output.

**Trigger 3 — Time-boxed ceiling.** Either of:

- **4 minutes elapsed** since first AI response in the session
- **6 turns exchanged** (3 user, 3 AI) in the session

whichever fires first. Rationale: past the 4-minute / 6-turn mark the probability of resolution drops sharply and the cost of continuing is measured in the user's frustration. Hand off.

The output includes:
- A table of all 3 triggers with thresholds and exact detection rules
- A per-language explicit-vocabulary block
- The configured X value for the sentiment drop
- The timeout configuration (can be overridden per segment — enterprise floor may be 6 minutes / 8 turns; PLG self-serve may be 3 minutes / 5 turns)

All three triggers are OR-ed. Any one of them immediately stops AI resolution.

### Step 4 — Design the Handoff Protocol

Handoff is customer-visible. The AI does not silently transfer the user — the user is told, clearly, that they are being routed to a human. Required elements:

1. **Context transfer.** The full conversation transcript plus the AI's current interpretation (intent, attempted resolutions, classified category, sentiment trajectory) is attached to the human agent's view of the ticket. The human does not ask the customer to re-explain.
2. **User-visible message.** "I'm connecting you to a human teammate now. Your context is being forwarded so you won't need to repeat yourself. {queue_position}." The `queue_position` field is populated from the routing target's queue depth at hand-off time, OR from an estimated wait time if queue position is not meaningful for the channel.
3. **Queue communication.** If the wait is expected to exceed the channel norm (> 60 seconds for chat, > 4 hours for email), the customer is offered a callback / reply-later option explicitly.
4. **Channel fall-through.** For synchronous channels (chat, in-app), if the human handoff wait exceeds a per-segment SLA, the AI offers to continue the conversation via email / ticket. For asynchronous channels (email), the handoff is a silent routing change (but the customer sees a human signature on the reply).
5. **Never-deflect routing target per category.** Accessibility → specialized accessibility team. Billing → billing ops / billing desk. Cancellations → retention / CSM queue. Safety → hardcoded human-first queue with highest-priority SLA.

The output documents each of these as a specific protocol, not a principle.

### Step 5 — Measurement Instrumentation

The rollback plan depends on measurement. Every deployment of AI-assisted resolution MUST instrument:

1. **CSAT capture at resolution** — the customer is asked to rate the interaction immediately after the AI reports resolution. Capture is segment-tagged.
2. **CSAT follow-up at 7 days** — a second pass captures whether the "resolution" held. Segment-tagged.
3. **Sentiment classifier output per turn** — the scores are logged per session and roll up to session-level sentiment trajectories.
4. **Escape-hatch trigger logging** — every escape-hatch fire is logged with: which trigger, at what turn/timestamp, the conversation state, and the downstream outcome (did the human resolve it, did it escalate further, did the customer churn).
5. **Category-level resolution rate** — resolution is defined as CSAT ≥ floor AND no reopen in 7 days, rolled up by detected intent category. This is NOT "deflection rate" — deflection is the hostile metric. We measure real resolution.
6. **Daily rollup for rollback trigger** — the CSAT daily mean per segment vs. the segment's floor. This daily rollup is what the rollback plan in Step 6 evaluates against.
7. **Never-deflect list compliance rate** — percentage of conversations in a never-deflect category that were correctly routed to the never-deflect path. Target: 100%. Any miss is a governance event.

All seven instruments are required before launch, not optional. A deployment that cannot measure one of them cannot use this strategy.

### Step 6 — Write the Rollback Plan

The rollback plan is NOT optional. Every output includes it.

**Trigger.** If the daily CSAT mean for any segment falls below that segment's floor for **N consecutive days** (default N = 3), automatic routing to human-first mode is triggered for that segment. The AI may continue to answer non-sensitive, low-intent-complexity queries but the default path becomes "route to human" rather than "route to AI".

Rationale for N=3: one bad day is noise (a weird product incident, a PR event, a weekend anomaly). Two bad days is a signal worth investigating but not yet worth an automatic rollback. Three bad days in a row is a durable degradation that should not wait for a weekly review.

**Notification.** When the trigger fires, the following happen in parallel:
- @support-lead and @cs-dir receive a notification with the segment, the daily means, and the floor
- A rollback incident ticket is created with severity "S2" (customer-impacting but not outage-level)
- A 72-hour post-rollback review is scheduled

**Manual override.** If the support org wants to NOT rollback despite the trigger, a manual override can be filed by @support-lead + @cs-dir jointly. The override must be in writing, must name the reason, must name a stop-date, and is logged as a governance event. Override cannot be unilateral.

**Post-rollback review (mandatory, 72 hours).** The review examines:
- Root cause of the CSAT degradation (model drift, prompt drift, new intent not in training, upstream product issue surfacing as support volume)
- Whether the floor was set correctly
- Whether the trigger N should be tightened or loosened based on this event
- What specific change is required before the AI returns to default routing
- Sign-off to exit rollback mode by @support-lead

The rollback plan is listed in the output as a separate section, not buried inside measurement.

---

## Output Structure

The skill produces one markdown file at a company-appropriate location (e.g., `{Company}/Product/ai-assisted-resolution-strategy-{date}.md`) with these sections:

1. **Strategy Summary** — one paragraph including: customer segments covered, languages, timezones, channel mix, current or planned tool
2. **Framing Note** — the paragraph explaining why this is an assisted-resolution strategy, not a deflection strategy (naming rationale)
3. **CSAT Floor Table** — per-segment floor with the computation shown (baseline, rule, resulting floor)
4. **Never-Deflect List** — all four mandatory categories with classification rule, user-visible message, routing target, escalation SLA per row
5. **Escape-Hatch Rules** — all three triggers with thresholds, the per-language explicit-vocabulary block, the sentiment drop X, the timeout configuration per segment
6. **Handoff Protocol** — context transfer spec, user-visible messages, queue communication, channel fall-through, never-deflect category routing
7. **Measurement Dashboard Spec** — all seven instrumentation items with thresholds, alerting path, daily rollup definition
8. **Rollback Plan** — trigger, N-days threshold, notification path, manual-override rules, post-rollback review requirements
9. **Deployment Checklist** — the pre-launch gate: every quality-gate item below must be checked, signed off, and logged
10. **Confidence and Open Gaps** — any inputs that were thin (missing baselines, languages without full escape-hatch vocabulary, segments without human comparators)

---

## Quality Gates

The skill applies these 8 checks before emitting the final output. A failure aborts and routes back to the relevant step.

1. **CSAT floor enforced per segment** — every primary segment from the input has a floor, computed with the max(90, baseline-2) rule, and the floor is documented in the output
2. **Never-deflect list covers all 4 mandatory categories** — accessibility, billing disputes, cancellations/downgrades, safety/legal/vulnerable customer. Missing any one is a hard fail.
3. **All 3 escape-hatch triggers defined** — explicit, implicit, time-boxed. Each with thresholds and detection rules.
4. **Multilingual rules cover every language in input** — every language listed in the input has explicit-request vocabulary in Trigger 1. No language may be skipped.
5. **Rollback plan present with defined N days + alerting path** — N is explicit (default 3), notification routes are named, the manual-override rule is documented.
6. **Measurement instrumentation defined before launch** — all 7 instruments named with thresholds. A deployment that cannot measure one of them is not allowed to ship.
7. **Segment-specific differentiation exists** — floors, timeout configuration, or handoff protocols differ across segments. If every segment has identical settings, the skill failed to use the segmentation input and routes back to Step 1.
8. **Handoff protocol is customer-visible** — the user-visible message is present in the output, the silent-transfer anti-pattern is explicitly forbidden.

Any failure aborts shipping the strategy.

---

## Rollback Plan (Detail)

This section intentionally duplicates Step 6 as its own top-level reference, because the rollback plan is the single most load-bearing part of this skill.

**Breach definition.** A segment's daily CSAT mean < the segment's floor, computed on a rolling 24-hour window ending at 00:00 UTC.

**Trigger.** 3 consecutive days of breach on any single segment.

**Automatic action.** Segment-specific routing flips from AI-first to human-first. AI still answers but is no longer the default path; the default route becomes "human queue".

**Notification.** @support-lead and @cs-dir receive a same-day notification. A rollback incident ticket is created at severity S2. A post-rollback review is scheduled at T+72h.

**Manual override.** Requires joint written sign-off from @support-lead and @cs-dir. Must name the reason, a stop-date, and is logged. Unilateral override is forbidden.

**Post-rollback review.** Mandatory, 72 hours after rollback. Reviewed items:
- Root cause of CSAT degradation
- Whether the floor was set correctly or was too aggressive
- Whether N (days) should be tightened or loosened based on the event's noise vs. signal character
- Specific change required before AI returns to default routing
- Sign-off to exit rollback by @support-lead

**Exit criteria.** CSAT daily mean > segment floor for 5 consecutive days AND the root cause has been addressed AND @support-lead signs off.

---

## Related Skills + Hand-Off

This skill sits between segmentation and tool selection in the CS operations flow:

- **Required inputs**:
  - `/cs-segmentation-model` — provides the segments that drive per-segment floors and per-segment timeouts
  - `/health-score-design` OR a human-handled CSAT baseline — provides the baselines that drive the max(90, baseline-2) rule
- **Output feeds**:
  - `/cs-tool-selection` — the tool choice depends on the strategy. A strategy with strict never-deflect classification, multilingual detection, and fine-grained sentiment scoring constrains the vendor list. The strategy comes first; the tool is picked to fit, not the other way around.
  - `/value-realization` — resolution quality is a value-delivery signal. CSAT floor compliance per segment is an input to the VR scorecard.
- **Alias**: `/ai-deflection-strategy` (discouraged naming — use `/ai-assisted-resolution-strategy`)

Default delegation pattern is **Pattern 1 Consultation** (see `rules/delegation-protocol.md`). Common consultations:

- `@csm` — for segment-specific CSAT realities. ("What does the High-Touch Enterprise segment actually tolerate from AI, given what they expect from a named CSM?")
- `@kb-specialist` — for the never-deflect category taxonomy. ("Is our accessibility category complete? What keywords are we missing?")
- `@privacy-counsel` — for the self-harm / vulnerable-customer category. ("Are there jurisdiction-specific rules we should be catching here beyond the general safeguarding vocabulary?")

Pattern 5 Adversarial Review is NOT required for this skill. The design constraints are already adversarial (hard floors, hard refusals, mandatory rollback); a second-pass adversarial review adds noise without catching new risks.

---

## Birth Test

Every new skill must be birth-tested against a real or synthetic context before it is declared v1.0.0 ready. For `/ai-assisted-resolution-strategy`, the birth test was run against the **Legionis** context:

- 4-tier segmentation from the `/cs-segmentation-model` birth test (High-Touch Enterprise, Mid-Touch, Tech-Touch Pooled, PLG Self-Serve)
- Early-stage product with no human-handled CSAT baseline yet → fallback to 90% absolute floor across all segments
- 3 languages: English, Hebrew, German
- 2 timezones: Europe/Jerusalem, America/New_York
- Particular attention to the safety / vulnerable-customer category because Legionis is an AI product and users may project distress onto the tool itself

The birth test output lives at: `Legionis/Product/ai-assisted-resolution-strategy-birth-test-2026-04-11.md`

The birth test validates:
- Per-segment floor table (with fallback to 90% absolute where baselines were missing)
- Never-deflect list with Legionis-specific framing
- Per-language escape-hatch vocabulary for English, Hebrew, German
- Segment-specific timeout differentiation (enterprise 6m/8t, PLG 3m/5t)
- Rollback plan with N=3 and the S2 incident path
- One edge case the skill handled and one it punted on

See the birth test file for the full walkthrough.

---

## Re-Run Cadence

Re-run the skill when any of these fire:

1. **CSAT floor breach that survives a post-rollback review** — if the rollback plan fired, the review identified a root cause, and the remediation requires a floor or trigger change, the strategy is re-run with the new inputs
2. **New language added to the AI footprint** — any new language reopens Trigger 1 vocabulary and forces a re-run of at least Step 3. Skipping this creates a silent gap where non-English-speakers cannot reach a human.
3. **New segment enters AI-assisted resolution** — a new primary segment requires a new row in the floor table, potentially new timeout configuration, and a review of whether the never-deflect list needs category expansion for that segment
4. **Regulatory change affecting the never-deflect list** — a new jurisdiction, a new safeguarding framework, a new consumer-protection rule (especially for billing or cancellations) triggers a re-examination of Step 2
5. **Classifier drift** — if the sentiment classifier or intent classifier changes model version, the thresholds in Trigger 2 must be revalidated, and the strategy is re-run to recalibrate

Do NOT re-run more often than quarterly in steady state. A thrashing strategy — where floors, triggers, and routes keep moving — destroys the measurement baseline that the rollback plan depends on.

---

## Anti-Patterns to Watch For

These are failure modes that the skill structure is trying to prevent. If your output drifts into any of them, abort and re-examine the relevant step.

- **Using deflection rate as the headline metric.** Deflection rate goes up when the AI answers more questions; resolution rate goes up when customers' actual problems are solved. They are NOT the same. This skill measures resolution, not deflection. If an output presents deflection rate as the primary KPI, it is using the wrong framing and Step 5 has been skipped.
- **Silent handoff.** Moving the customer from AI to human without telling them, without forwarding context, or without an estimate of wait time. This destroys trust and makes the escape hatch worse than no escape hatch at all.
- **Soft CSAT floor.** Describing the floor as a "target" or "goal" rather than a hard line. The whole point of the floor is that it triggers the rollback plan. If it is soft, the rollback plan is decorative.
- **Never-deflect list as a content filter.** The never-deflect list is not a blocklist of topics the AI cannot discuss. It is a routing rule: in these categories, the AI does not attempt resolution. It may still acknowledge, it may still capture context, it may still thank the customer — but resolution is handed to a human immediately. Treating the list as a blocklist produces cold, unhelpful AI responses in sensitive moments, which is worse than a human handoff with context.
- **Single floor for all segments.** If the skill emits one floor across the board in the presence of segmentation input, Step 1 was not executed. Re-run.
- **Escape hatch that requires the user to know the magic word.** Trigger 1 must include common variants in every supported language. If the user has to guess "representative" vs. "human" vs. "agent" to reach a human, the trigger is not working. The vocabulary should over-match, not under-match.

---

## ROI

Time saved on drafting and triage: the skill produces in ~20 minutes what a Support Lead working with CS Ops would typically draft across 6–8 hours of working sessions — floor computation per segment, the multilingual vocabulary for the escape hatch, the never-deflect taxonomy with classification rules, the handoff protocol detail, and the rollback plan. Blended Support Lead + CS Ops rate: $175/hr.

Standard output after skill invocation:

> ⏱️ ~[X] hrs saved on drafting and triage in [Y] min, [Z]k tkns ~$[C] cost, Value ~$[V]

---

## Operating Principle

> "The AI is the junior team member, not the firewall. Its job is to resolve what it can quickly and to fail honestly — escalating the rest to humans with context, clarity, and a visible path. Deflection is hostile; assisted resolution is the discipline of making first-contact AI support actually worth the customer's time."
