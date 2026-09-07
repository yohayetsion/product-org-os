# Stakeholder Management — V2V OS pack on stakeholder mapping, decision rights (RACI/DACI/RAPID), executive communication patterns, and escalation discipline

**Adapted from**:
- RACI (Responsible / Accountable / Consulted / Informed) — origin from PMI / PMBOK; modern variants RASCI, RAPID
- DACI (Driver / Approver / Contributors / Informed) — Intuit / Atlassian operationalization
- Stakeholder Mapping — Mendelow's Power-Interest grid (1991), Stanford "stakeholder theory" R. Edward Freeman 1984
- Crucial Conversations (Patterson / Grenny / McMillan / Switzler) — escalation framing
- "Escalation as a feature, not a failure" (Lara Hogan)
- V2V Vision-to-Value cross-functional decision discipline (Decision Interface Charters per V5.2 Appendix C — when authored)

**Source licence**: Public methodology references
**V2V refinements**: Stakeholder management framed as decision-discipline scaffolding (who decides + who's consulted + when to escalate), not as relationship management; cross-references to decision-charter + escalation-rule + collaboration-check skills

---

## 1. Purpose

This pack equips Product Org agents — primarily `product-manager` and `director-product-management` — to navigate cross-functional initiatives where decision rights are murky, executives are over-asked or under-informed, and escalation is either avoided (decisions don't happen) or abused (everything bubbles up). It covers:

- How to map stakeholders for a specific decision (not as a generic exercise)
- How to allocate decision rights (RACI / DACI / RAPID — when each fits)
- How to communicate to executives in a way that gets a decision rather than a re-meeting
- How to escalate well (Lara Hogan's "escalation as a feature")
- How to spot and remediate the most common stakeholder dysfunctions

Use it whenever you're standing up a cross-functional initiative, drafting a Decision Interface Charter, preparing an exec one-pager, or hitting recurring "we keep re-deciding the same thing" friction.

---

## 2. Framing: stakeholder management as decision discipline, not relationship management

The trap is treating "stakeholder management" as a soft-skill euphemism for "keep everyone happy." That framing produces three predictable failures:

1. **Inflated stakeholder lists** — anyone with a feeling becomes a "stakeholder," so every decision becomes a 12-person sign-off
2. **Optimization for sentiment, not outcome** — the team measures success by "are people happy" rather than "did we make a faster, better decision"
3. **Escalation as failure** — surfacing disagreement reads as "the PM couldn't manage their relationships," so disagreement gets buried instead of resolved

**V2V framing**: stakeholder management = clarity on **decision rights** (who decides what), **input rights** (who's consulted and on what), and **escalation paths** (when disagreement triggers a higher gate).

The deliverable of good stakeholder management is **faster, better decisions** — not warmer relationships. Warmer relationships are a side effect of repeatedly making sound decisions in public; they are not the goal.

A working test: at the end of a stakeholder interaction, can you name (a) what was decided, (b) by whom, (c) what input was incorporated, and (d) what would trigger re-decision? If no — the interaction was relationship work disguised as decision work.

---

## 3. Stakeholder mapping — Mendelow Power-Interest grid

Mendelow's 1991 Power-Interest grid is the canonical 2×2 stakeholder map. It places each stakeholder on two axes:

| | Low Interest | High Interest |
|---|---|---|
| **High Power** | Keep Satisfied — periodic awareness, don't surprise | Manage Closely — co-design, frequent touch |
| **Low Power** | Monitor — minimal effort | Keep Informed — regular updates, advocate enablement |

**V2V refinement: add a third dimension — Decision Stake.**

A stakeholder may have high power and high interest in the *area* but no stake in *this specific decision*. Add a third axis: **Does their decision authority touch THIS decision?** You mentally collapse the 3D map to 2D for the specific decision in front of you. Without this collapse, every senior leader ends up in "Manage Closely" by default, and you spend your week pre-wiring people who have no decision rights on what you're actually deciding.

**Mapping template for one decision**:

| Stakeholder | Role | Power (1-5) | Interest (1-5) | Decision Stake (Y/N) | Engagement |
|---|---|---|---|---|---|
| [Name] | VP Eng | 5 | 4 | Y | Manage Closely — co-design |
| [Name] | GC | 4 | 2 | Y (risk veto) | Keep Satisfied — flag risks early |
| [Name] | CMO | 4 | 3 | N | Monitor — no need to consult on this one |

**Anti-patterns**:

- **Map-everyone** — listing every leader you've ever met. Symptom: the map runs to 20+ rows for a single decision.
- **Permanent map** — treating the map as static. Power and Interest shift with org changes, strategic resets, M&A, and even quarter rollovers. Refresh per decision.
- **Map-as-org-chart** — anyone senior gets High Power by default. The right question is "power over THIS decision," not "power in the org."

**When to invoke `/stakeholder-map` skill**: for a specific initiative where multiple decisions will be made over weeks-to-months, you want a persistent map you refresh. For a single decision, a back-of-envelope grid is sufficient — don't overhead-tax single decisions.

---

## 4. RACI — Responsible / Accountable / Consulted / Informed

The grandparent of decision-rights frameworks. Originated in PMI / PMBOK; widely adopted in cross-functional process design.

| Role | Meaning |
|---|---|
| **R**esponsible | Does the work |
| **A**ccountable | Has final say. One person, not a team. |
| **C**onsulted | Provides input BEFORE the decision is made (two-way) |
| **I**nformed | Is notified AFTER the decision is made (one-way) |

**Strengths**:
- Forces explicit single accountability ("only one A per row")
- Surfaces hidden multi-accountable confusion ("wait, we both thought we owned this")
- Widely understood — most cross-functional partners recognize the framework

**Weaknesses**:
- Degenerates into matrix bloat when applied to every micro-decision
- The R vs A distinction is genuinely confusing — many teams collapse them
- Doesn't distinguish "drives the decision process" from "approves the decision," which DACI handles better
- Says nothing about veto power, which RAPID handles via Agree

**Best use**: cross-functional process design (e.g., "how do we run a launch") — not single-decision allocation. For a one-time decision, DACI is sharper.

**Canonical example**: a release process matrix.

| Activity | Eng | PM | Design | Marketing | CS |
|---|---|---|---|---|---|
| Feature spec | C | A | C | I | I |
| Technical architecture | A | C | I | I | I |
| UI specs | I | C | A | I | I |
| Launch messaging | I | C | C | A | C |
| Customer comms | I | C | I | C | A |

---

## 5. DACI — Driver / Approver / Contributors / Informed

Intuit/Atlassian operationalization. Sharper than RACI for **single decisions** because it explicitly separates the person who orchestrates the decision process from the person who has final say.

| Role | Meaning |
|---|---|
| **D**river | Owns the decision PROCESS (not the decision). Drives to closure. |
| **A**pprover | Single named individual with veto + final say |
| **C**ontributors | Inputs solicited |
| **I**nformed | Needs to know after |

**Why this is sharper than RACI for one-time decisions**: the Driver is often a PM running the decision, but the Approver is a VP or director who owns the call. Conflating them (which RACI invites) means PMs end up "owning" decisions they don't actually have rights to make — and execs avoid named approval because "we have a RACI for that."

**When to use**: any meaningful one-time decision — pricing changes, build-vs-buy, partnership terms, organizational restructures, roadmap commits.

**Authoring workflow**: use the `/daci` skill for any decision worth a formal artifact. For trivial decisions, in-line DACI in the meeting agenda ("Driver: Product Lead, Approver: Executive Sponsor, Contributors: PM team, Informed: leadership") is enough.

**Common DACI failure**: no named Approver. The meeting closes with "let's discuss further" because no single person is named to say yes/no. Fix: before starting the meeting, write the Approver on the board.

---

## 6. RAPID — Recommend / Agree / Perform / Input / Decide (Bain)

Bain & Company's framework. More fine-grained than RACI/DACI; useful for org-design decisions and high-stakes strategic decisions where decision rights themselves are the artifact.

| Role | Meaning |
|---|---|
| **R**ecommend | Proposes the decision (often the analyst/PM doing the work) |
| **A**gree | Has veto. Must agree before it proceeds. |
| **P**erform | Executes after the decision |
| **I**nput | Provides information (non-veto) |
| **D**ecide | Has final authority |

**The killer feature**: separates **Agree (veto)** from **Input (non-veto)** and from **Decide (final say)**. Legal often has Agree on contracts. Engineering often has Agree on feasibility. PMs typically have Recommend; VPs have Decide. Customer Success has Input.

**When to use**: high-stakes decisions where vetos are real — enterprise contracts, M&A, pricing commitments, IP licensing, regulatory strategy. The heavier framework pays off because the decision is itself heavy.

**Anti-pattern**: using RAPID for routine product decisions. The overhead overwhelms the value.

---

## 7. Decision-rights anti-patterns

These are the failure modes V2V Decision Interface Charters are explicitly designed to prevent. If you see any of these, the remedy is a Charter, not another meeting.

| Anti-pattern | What it looks like | Why it's harmful | Remedy |
|---|---|---|---|
| **Decision by committee** | "Let's get the group's view." No single Decide. | Decisions are slow, watered-down, and rarely close | Name an Approver/Decide BEFORE the meeting |
| **Decision by escalation** | Every disagreement bubbles to the exec | Exec layer clogs; decisions don't happen at the right altitude | Clear escalation triggers (only X, Y, Z escalate) |
| **Decision by silence** | No formal sign-off. The org "drifts" into the call. | Plausible deniability. Re-decisions when the wind shifts. | Written DR with named Approver and timestamp |
| **Decision by re-decision** | Same call keeps coming back. "Wait, didn't we decide this?" | Burns team energy; signals decision wasn't actually made | Charter that names re-decision triggers explicitly |
| **Decision by absent stakeholder** | Person not in room blocks at delivery | Wasted weeks of work | Stakeholder map BEFORE work starts, not at the gate |

V2V Decision Interface Charters (per `/decision-charter` and V5.2 Appendix C when authored) capture: decision name, scope, named Decide, named Agree-holders, input rights, escalation triggers, re-decision triggers. Investing in the Charter up front prevents all five failures.

---

## 8. Executive communication patterns

Executives are time-bandwidth-constrained, not intelligence-constrained. They optimize for "did I get the right input to make the call" — not for "did I learn everything." Match that.

### 8.1 The three-line status pattern

For asynchronous exec updates (email, Slack, weekly notes):

> 1. **What I'm doing**: [one sentence on the work]
> 2. **What I need from you**: [one sentence — decision, intro, escalation, nothing]
> 3. **When I need it by**: [explicit date or "no rush"]

If you can't write line 2 in one sentence, you're not ready to send the update. The exec can't help you, because you don't know what help you need.

### 8.2 The three-sentence decision framing

For a decision recommendation:

> "We're choosing between **X** and **Y** because **Z**. I recommend **X** because **[1-2 reasons]**. The biggest risk is **[1 risk]**, mitigated by **[1 mitigation]**."

Four sentences max. Everything else goes in the one-pager. If the exec wants more, they'll ask.

### 8.3 The risk surface pattern

For risk communication:

> "Risks to flag: **[1-3 risks]**. Mitigations in place: **[for each risk]**. Open risk: **[any unresolved]** — would value your view on whether we accept it or invest to mitigate."

This format forces you to surface risks WITH mitigations — eliminates the "PM brings problems, not solutions" anti-pattern.

### 8.4 What to avoid with executives

- **Long context dumps** — the exec already trusts that you've done the work; don't re-explain it
- **Meeting-as-status** — async update preferred; reserve meeting time for decisions
- **Decisions-via-Slack-thread** — Slack is good for "FYI" and "quick question"; bad for sign-off. Sign-off needs a written DR.
- **Pre-meeting surprise** — if a decision needs exec input, pre-wire before the meeting. The meeting is to confirm, not to discover.

### 8.5 The exec one-pager (longer-form)

For a substantive decision, the one-pager template:

| Section | Length |
|---|---|
| Title + date + author | 1 line |
| Recommendation | 2 sentences |
| Context | 3-4 bullets |
| Options considered + tradeoffs | 2-3 options |
| Risks + mitigations | 2-3 bullets |
| Decision needed by | 1 line |
| Appendix (optional) | Separate page |

If it doesn't fit on one page, it's not ready.

---

## 9. Escalation — Lara Hogan's "Escalation as a feature, not a failure"

The cultural default in many product orgs is that "escalation is failure." This produces the worst possible outcome: disagreements get buried, decisions don't happen at the right altitude, and the team grinds through weeks of unresolved tension before someone finally raises it — at which point it's a crisis.

**Lara Hogan's reframe**: escalation is the system working as designed when the right altitude is exceeded. A decision rights framework that has NO escalation triggers is a framework that pretends conflict doesn't happen. Escalation is a feature.

**An escalation framework needs three things**:

1. **Clear trigger conditions** — "X happens, escalate" (not "use your judgment")
2. **Named escalation contact** — singular person, not "leadership"
3. **Timeboxed response** — "respond within 48 hours"

### 9.1 When to escalate

- **Scope changes** — the work expanded materially beyond the original commitment
- **Principle conflicts** — two teams optimizing for legitimate but incompatible principles (e.g., privacy team vs. growth team)
- **Irreconcilable differences after good-faith debate** — you've debated, you've tried alternatives, you're stuck

### 9.2 When NOT to escalate

- **Not-yet-decided things** — if the call is yours to make, make it. Don't escalate to get cover.
- **Avoidable conflicts** — if a 30-minute conversation with the other PM solves it, have the conversation
- **Status updates dressed as escalation** — "FYI we're behind" is not an escalation; it's a status update
- **Permission-seeking** — if you have the decision rights, don't ask for permission

### 9.3 V2V Charter pattern: re-decision triggers ARE escalation rules

A well-authored Decision Interface Charter names re-decision triggers up front: "If the market shifts X way, OR if engineering capacity drops below Y, OR if competitor lands Z, re-open this decision." Those triggers ARE escalation rules — they tell teams when surfacing the decision again is correct behavior, not failure.

Use `/escalation-rule` to author escalation rules formally for decisions worth the artifact.

---

## 10. Cross-functional alignment patterns

The patterns that actually move alignment from theory to practice.

### 10.1 Pre-meeting alignment (1:1s before the group)

For any meeting where a decision will be made, run 1:1s with each Agree-holder and the Decide before the group meeting. Surface concerns privately; resolve what can be resolved; arrive at the group meeting with concerns surfaced and either resolved or named. The group meeting then closes the decision rather than discovering the disagreement.

This is "pre-wiring." It works.

### 10.2 Working backwards from the decision

Open the meeting/document with the decision being made: "We're choosing X over Y." Then provide context to support the choice. Most teams do this in reverse — they spend 80% of the time on context, then run out of time for the decision, and re-meet next week.

Amazon's "Press Release / FAQ" pattern (cross-ref `/press-release-faq` skill) is the disciplined version: write the press release of the launch FIRST, work backwards to what you need to decide today.

### 10.3 Disagree-and-commit (Bezos)

From Jeff Bezos's 2016 shareholder letter. When two senior leaders disagree on a call and one has decision rights, the other says "I disagree but will commit" — explicitly. They don't slow-roll, sandbag, or undermine in private. They commit.

**Why this matters**: most cross-functional friction is not "we disagree on the decision." It's "we disagree on the decision AND I won't commit to it AND I'll act in ways that undermine it." Disagree-and-commit names the failure mode and forbids it.

**How to invoke**: when a decision is made and a senior partner disagrees, ask: "Are you disagree-and-commit on this, or are you genuinely blocked?" The first is fine. The second requires escalation or re-decision.

### 10.4 Pre-mortem before commitment

Cross-ref `/pre-mortem`. Before locking a commitment, run a 30-minute pre-mortem: "It's 12 months from now and this decision failed. Why?" The risks that surface in pre-mortem are the ones to address in mitigation BEFORE commitment, not after.

### 10.5 Meeting cadences and their purposes

| Meeting | Cadence | Purpose | Output |
|---|---|---|---|
| Sprint planning | Biweekly | Commit deliverables | Sprint backlog |
| Product review | Weekly | Decisions + unblock | Decisions, status |
| GTM sync | Biweekly | Align launch | Timeline |
| Stakeholder update | Monthly | Inform | Status report |
| Strategic review | Quarterly | Adjust strategy | Adjustments |

**Rule**: cancel any recurring meeting where the agenda is consistently empty. A standing meeting with no agenda is theatre.

---

## 11. Stakeholder dysfunction patterns

The recurring failure modes you'll see in real orgs. Recognize them by name; don't lump them all into "stakeholder politics."

### 11.1 The secret-veto stakeholder

Says yes in meetings, blocks downstream. Often a senior leader who feels they don't have time to engage upstream but won't accept downstream decisions made without them.

**Remedy**: explicit decision-rights doc at the start of the initiative. Name them as Approver or Agree-holder if they truly have veto; name them as Informed if they don't. The doc removes the ambiguity that enables the secret veto.

### 11.2 The everything-stakeholder

Over-claims decision rights. Wants to be Approver on every decision in the initiative.

**Remedy**: scope their decision rights explicitly. "You're Approver on pricing decisions. You're Informed on UI decisions." Push back politely but firmly. If they escalate, your VP backs the scoping — that's what Charters are for.

### 11.3 The Informed-treated-as-Consulted stakeholder

Was placed on the Informed list (notified after) but treats every notification as a consultation request and tries to veto. Often a senior leader with adjacent responsibility.

**Remedy**: clarify in the moment. "I'm sending this as FYI, not for input — you're Informed on this one. If you think the decision rights should be different, let's talk to [VP] about updating the Charter." Surfaces the scope drift instead of accommodating it.

### 11.4 The absent stakeholder

No input upstream, blocks at delivery. Common with Legal, Security, Compliance, or Finance partners who are over-asked across the org and triage based on what hits their desk last.

**Remedy**: stakeholder mapping AT THE START of the initiative, not at the gate. Identify the four-or-five Approver/Agree-holders early, run a 30-minute pre-wire with each, and document their position. A 30-minute meeting in week 1 prevents a six-week block in week 12.

### 11.5 The escalation-avoiding stakeholder

Knows there's a disagreement but won't surface it. Slow-rolls instead. You discover at the milestone gate that they never agreed.

**Remedy**: name disagree-and-commit explicitly. "I'm hearing concerns. Are you disagree-and-commit, or do we need to escalate?" Forces the choice. If they say neither, escalate yourself — surfacing the dysfunction IS the escalation.

---

## 12. V2V cross-references

| Skill | When to invoke |
|---|---|
| `/decision-charter` | Formal Decision Interface Charter for cross-functional decisions |
| `/escalation-rule` | Author explicit escalation rules and triggers |
| `/collaboration-check` | Periodic cross-team health check (catches dysfunction patterns) |
| `/stakeholder-map` | Visualize stakeholders for a specific initiative |
| `/ownership-map` | Broader org-design ownership mapping |
| `/daci` | Author a DACI for a one-time decision |
| `/commitment-check` | Verify commitments are recorded with named owners |
| `/decision-record` | Persist a decision with reasoning and named Decide |
| `/decision-quality-audit` | Audit a set of past decisions for quality patterns |
| `/pre-mortem` | Risk surfacing before commitment |
| `/press-release-faq` | Working-backwards artifact for high-stakes initiatives |

When in doubt, start with `/stakeholder-map` to clarify who, then `/decision-charter` to clarify what, then `/escalation-rule` to clarify when-it-goes-up. Those three artifacts cover 80% of the cross-functional alignment work.

---

## 13. Operating principle

> "Stakeholder management is the discipline of getting decisions made at the right altitude with the right input. It is not the discipline of managing feelings. Warm relationships are a byproduct of repeatedly making sound decisions in public — they are not the goal."
