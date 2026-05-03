---
name: win-loss-decision-signal
description: 'Produce a Win/Loss Decision Signal — the Competitive Intelligence side of the two-track win/loss split, focused on the decision quality of buyer choices (decision frame, named alternatives considered, success criteria, decision-quality assessment, recurring patterns, strategic implication) as the upstream gating signal that feeds the portfolio-review gate. Distinct from the Product Marketing deal-level enablement track (battlecards, sales testimonials, objection handling) which lives on a separate gate. Activate when: "win/loss decision signal", "decision-quality read on deals", "why did buyers decide that way", "win/loss as gating signal", "portfolio review competitive read", "buyer decision frame analysis", win/loss for portfolio gate. Do NOT activate for: deal-level battlecards or sales enablement (/competitive-battlecard, /sales-enablement — those are PMM-side artifacts), market-share or category-motion reads (/competitive-landscape), individual decision documentation (/decision-record), competitive feature comparison (/competitive-analysis).'
argument-hint: '[deal cohort or quarter or product line] or [update path/to/signal.md]'
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: competitive-intelligence
  skill_type: task-capability
  owner: competitive-intelligence
  sensitive: false
  primary_consumers:
  - ci
  - competitive-intelligence
  secondary_consumers:
  - vp-product
  - cpo
  - pm-dir
  - director-product-management
  - bizops
  - pmm-dir
  - director-product-marketing
---
## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "refresh", "revise", "add deals" + path | UPDATE | 100% |
| File path provided (`@path/to/signal.md`) | UPDATE | 100% |
| "create", "new", "produce", "build the signal" | CREATE | 100% |
| "find", "search", "list signals" | FIND | 100% |
| "the signal", "our last decision-signal read" | UPDATE | 85% |
| Just cohort or quarter | CREATE | 60% |

**Threshold**: ≥85% auto-proceed | 70-84% state assumption | <70% ask user.

### Mode Behaviors

**CREATE**: Produce a complete decision-signal artifact across the six canonical sections below. Output to `win-loss-signals/[cohort-slug].md` plus a JSON sidecar at `win-loss-signals/[cohort-slug].json` for downstream gate consumption.

**UPDATE**:
1. Read existing signal at the supplied path.
2. Identify which sections the user is updating (typically Section 5 patterns or Section 6 strategic implication when new deals close).
3. Preserve historical per-deal entries.
4. Re-derive aggregate patterns and re-score the decision-quality assessment.
5. Show diff summary of which patterns shifted and which strategic implications updated.

**FIND**: Search for prior decision-signal artifacts in the locations below; return paths, cohorts covered, and last-updated dates.

### Search Locations for Signals

- `win-loss-signals/`
- `competitive-intelligence/win-loss/`
- `context/decisions/win-loss/`
- `gtm/win-loss/`

---

## Vision to Value Phase

**Phase 6: Learning & Adaptation Loop** — the Win/Loss Decision Signal is a structured Competitive Intelligence read on the decision quality of buyer choices, fed back into Phase 1 (Strategic Foundation) and Phase 2 (Strategic Decisions) as input to the next portfolio-review gate. It is a Phase 6 artifact whose consumer is the portfolio-review gate that opens the next strategic cycle.

**Prerequisites**: a closed-deal cohort with enough deals to surface patterns (typically a quarter, a product line, or a named segment with at least five deals across won and lost outcomes); access to the qualitative record of each deal (sales notes, prospect interviews where available, the buyer's stated decision frame); a current portfolio record so the strategic implication in Section 6 traces back to a named bet.

**Outputs used by**: the portfolio-review gate at quarterly cadence (consumes Section 5 patterns and Section 6 strategic implication as input to portfolio re-decision questions); `/decision-quality-audit` (consumes the decision-quality assessments in Section 4 as evidence for the wider audit); `/positioning-statement` and `/gtm-strategy` updates downstream when the strategic implication names a positioning or GTM-motion change. The signal does NOT feed deal-level enablement; that track is owned by Product Marketing Management and produces a different artifact (`/competitive-battlecard`, `/sales-enablement`).

**Operating principle**: this artifact operationalises the Vision to Value Empowerment-layer Glossary's "sensor" framing. The seat fires; the sensor surfaces; the gate consumes. A Win/Loss Decision Signal that is not on the table at the portfolio-review gate is a portfolio-review gate operating without competitive reality. Decision-quality framing — not deal-narrative framing — is what makes the signal consumable by leadership making portfolio calls rather than by sales reps closing the next deal.

---

## What this signal is — and what it is not

The Win/Loss Decision Signal asks one question: was the buyer's decision well-formed? The signal reads each deal — won and lost — through the decision-quality lens. Did the buyer have a coherent decision frame? Did they consider the right named alternatives? Did they have specified success criteria, or were the criteria implicit and only legible after the fact? Was the decision well-formed enough that we would expect the buyer to be a successful customer (if we won) or to revisit us (if we lost)? Across a cohort of deals, what patterns recur, and what one-offs are not patterns?

This is structurally different from the Product Marketing Manager's deal-level enablement track. The PMM track produces battlecards, objection handlers, demo flows, and sales enablement collateral — deal-level artifacts that help individual sales reps win the next deal in front of them. The Win/Loss Decision Signal does not produce any of those artifacts. It produces an upstream gating signal that feeds the portfolio-review gate, where the question on the table is whether the offering, the qualification model, or the strategic positioning needs to change at all.

The two tracks exist because they answer different questions and feed different gates. Conflating them is the recurring failure mode that produces "win/loss is just a sales artifact" — the framing the Vision to Value Empowerment-layer Glossary is reframing. The Competitive Intelligence side feeds the portfolio gate; the Product Marketing side feeds the sales-enablement gate; both gates fire on different cadences, and neither replaces the other.

---

## The six canonical sections

### Section 1 — Decision frame the buyer used

**What it captures.** For each deal in the cohort, one short paragraph describing the decision frame the buyer brought to the evaluation. Was it a structured framework (e.g., a written evaluation rubric with weighted criteria, a procurement scorecard, a category-defining requirements document)? Was it implicit (e.g., the buyer was solving a specific operational pain and assembled criteria as they went)? Was it political (e.g., the decision was made to ratify a champion's preference and the evaluation was performative)? The frame is named honestly. A decision frame is not the same as the buyer's stated criteria; it is the deeper question of how the buyer was structuring the choice.

**Why it matters.** Decision-frame quality varies systematically across markets, segments, and buyer roles. A category where most buyers use structured frames produces a different competitive-intelligence read than a category where most buyers use political or implicit frames. Naming the frame for each deal is what makes the cohort-level patterns in Section 5 legible. A cohort where 80 percent of buyers used implicit frames is telling us something about the category that no battlecard can address — it is telling us the qualification model needs to change because we are spending sales effort on buyers whose decision frames cannot accommodate the offering's strengths.

**Prompt question.** "For each deal in the cohort, name the decision frame the buyer used. Was it structured, implicit, or political? What evidence supports that read?" Follow-up: "If the frame is unclear, that itself is a signal — many buyers in this category may not be making well-formed decisions, which has portfolio-level implications."

**Quality bar.** A strong Section 1 names the frame for every deal in the cohort with one or two sentences of evidence. The frames are honestly assessed — political frames are named as political, not laundered as "executive sponsorship." A weak Section 1 paraphrases the buyer's stated criteria as the frame, omits frames for the deals that are hardest to read, or assumes a structured frame in cases where the evidence does not support it.

---

### Section 2 — Named alternatives the buyer considered

**What it captures.** For each deal, the named alternatives the buyer evaluated alongside the offering. "Named" is load-bearing here in exactly the sense the Launch Narrative Brief uses it: the alternatives are named by company and product (e.g., "Acme Inc.'s Acme Suite v3.2"), not by abstract market frame. The section also captures whether the alternatives were the right shortlist — whether the buyer was considering the actual competitive set the offering competes against, or a misaligned shortlist that produced a flawed comparison.

**Why it matters.** Two distinct signals come out of this section. First, the named-alternatives list across the cohort is the most accurate competitive landscape the organization can produce — far more accurate than analyst landscapes, because it reflects who buyers actually shortlist rather than who analysts include. Second, the right-shortlist read tells us whether the offering's positioning is reaching the buyers it should be reaching. A cohort where most buyers shortlisted us against an irrelevant competitor (e.g., a category leader they could not have afforded) is telling us the positioning is mis-targeting the buyer altitude.

**Prompt question.** "For each deal, name the alternatives the buyer considered. Were these the right shortlist for the offering's positioning? If not, what was the misalignment?" Follow-up: "If the buyer did not consider any named alternative, the deal was either a sole-source procurement or a misqualified opportunity — name which."

**Quality bar.** A strong Section 2 names alternatives by company and product for every deal. The right-shortlist read is honest — when the buyer's shortlist was misaligned with the offering's positioning, the section names the misalignment rather than rationalising it. A weak Section 2 names "the competition" without specifics, omits the right-shortlist read, or treats every shortlist as appropriate when the cohort evidence shows systematic mis-targeting.

---

### Section 3 — Success criteria the buyer had

**What it captures.** For each deal, the success criteria the buyer carried into the evaluation. Were the criteria specified — written down, weighted, communicated to the evaluation team? Or were they implicit — only legible after the fact in the buyer's stated reasoning? The section also captures whether the criteria were criteria the offering competes well on (regardless of win or loss outcome). A deal won against criteria the offering does not actually compete on is a fragile win; a deal lost against criteria the offering does compete on is a positioning or qualification failure, not a product failure.

**Why it matters.** The success-criteria read is the most direct signal about whether the offering is being evaluated on the axes that actually matter to its strengths. Deals lost against criteria the offering competes well on point at a positioning or messaging gap. Deals won against criteria the offering does not compete well on are fragile wins — typically driven by champion preference or relationship, and likely to churn or contract at renewal. Across a cohort, the criteria distribution tells us whether the strengths-to-criteria mapping is healthy or whether the qualification model is letting the wrong opportunities through.

**Prompt question.** "For each deal, name the success criteria the buyer used and whether they were specified or implicit. Were the criteria axes the offering actually competes well on?" Follow-up: "If a deal was won against criteria the offering does not compete on, the win is fragile. If a deal was lost against criteria the offering does compete on, the failure is positioning, not product."

**Quality bar.** A strong Section 3 names the criteria for every deal, distinguishes specified from implicit, and assesses each deal's criteria-to-strengths mapping. A weak Section 3 lists generic criteria without distinguishing specified from implicit, or assumes the criteria the buyer stated were the criteria the buyer actually used.

---

### Section 4 — Per-deal decision-quality assessment

**What it captures.** For each deal in the cohort, a high / medium / low decision-quality rating with one paragraph of rationale. High-quality decisions are well-framed, considered the right named alternatives, used specified criteria, and produced an outcome traceable back to the criteria. Medium-quality decisions hold one or two of those properties. Low-quality decisions are politically driven, unframed, or used misaligned shortlists. The rating is independent of win or loss — a low-quality decision that produced a win is still a low-quality decision, and the win is fragile.

**Why it matters.** Decision quality is the upstream variable; outcome (win or loss) is the downstream consequence. A win that came out of a low-quality decision is not the same as a win that came out of a high-quality decision; the former does not generalise. A loss that came out of a high-quality decision tells us something specific about the offering's competitive position; a loss that came out of a low-quality decision is either a qualification miss (if the deal should never have been pursued) or a positioning miss (if the deal was viable but the buyer never engaged the offering's actual strengths). Per-deal decision-quality assessment is what lets the cohort-level patterns in Section 5 distinguish signal from noise.

**Prompt question.** "Rate each deal's decision quality high / medium / low, with rationale. The rating is independent of win/loss — name explicitly when a win came out of a low-quality decision (fragile) or a loss came out of a high-quality decision (genuine competitive signal)." Follow-up: "If most deals in the cohort are rated low-quality, the signal is about the qualification model, not about competitive position."

**Quality bar.** A strong Section 4 has a per-deal rating with rationale, calls out fragile wins and genuine competitive losses explicitly, and stays honest when the cohort skews low-quality. A weak Section 4 rates every deal medium, conflates outcome with decision quality, or omits ratings for the deals that are hardest to assess.

---

### Section 5 — Patterns across the cohort

**What it captures.** What recurs across deals, and what is a one-off. Patterns are claims supported by multiple deals (typically three or more in a cohort of five-plus). One-offs are deal-specific findings that do not warrant cohort-level conclusions. The section names patterns explicitly: recurring frame types, recurring named alternatives, recurring success-criteria axes, recurring decision-quality skews. Each pattern is named with the evidence (which deals support it) and the strength (how many deals across the cohort exhibit it).

**Why it matters.** The portfolio-review gate consumes patterns, not anecdotes. A pattern across deals is what justifies a portfolio-level move — a positioning shift, a qualification-model change, a product investment. An anecdote is what one battlecard or sales conversation can address. The section's discipline is to be ruthless about distinguishing the two: if a finding is supported by one deal, it is an anecdote and does not surface to portfolio review (it can still feed the PMM-side enablement track). If a finding is supported by three or more deals, it is a pattern and does surface.

**Prompt question.** "What recurs across the cohort? For each candidate pattern, name the deals that support it and the strength (how many deals exhibit it). What is a one-off and not a pattern?" Follow-up: "If a finding is supported by one deal, it is an anecdote. The portfolio-review gate consumes patterns, not anecdotes. Demote the anecdote and surface only patterns to Section 6."

**Quality bar.** A strong Section 5 names patterns supported by named deals with named strength, and explicitly demotes one-off findings to a separate "anecdotes — for PMM-side track" subsection. A weak Section 5 lists every observation as a pattern, fails to name supporting deals, or conflates patterns with anecdotes.

---

### Section 6 — Strategic implication for portfolio review

**What it captures.** The one or two strategic implications the cohort surfaces, framed as questions or claims for the next portfolio-review gate. Each implication traces back to a Section 5 pattern (no implication is allowed without a pattern) and forward to a named portfolio bet (the implication has consequences for a specific bet on the portfolio record). The implication is not a recommendation to sales; it is a claim or question for portfolio leadership to take into the gate. Examples: "The qualification model is letting buyers with implicit decision frames through; the offering's strengths cannot be evaluated by buyers without structured frames, so we are spending sales effort on a buyer profile we do not convert. Recommend re-scoping the qualification model to filter for structured frames." Or: "Across won deals, 4 of 6 used Acme Suite v3.2 as the named alternative, and the differentiation axis we won on was integration depth in 3 of 4 cases. The category positioning is converging on integration depth; the next positioning iteration should make this load-bearing."

**Why it matters.** The strategic implication is the artifact's deliverable to the portfolio gate. Without Section 6, the signal is a research report; with Section 6, the signal is a gating input. The discipline of forcing the implication to trace back to a Section 5 pattern (no patterns, no implications) and forward to a named portfolio bet (no bet linkage, no portfolio-level implication) is what keeps the signal honest and decision-shaped.

**Prompt question.** "What are the one or two strategic implications the cohort surfaces? For each, name the Section 5 pattern it traces back to and the named portfolio bet it has consequences for." Follow-up: "If an implication does not trace back to a pattern, it is opinion. If it does not trace forward to a bet, it does not belong on the portfolio gate."

**Quality bar.** A strong Section 6 names one or two strategic implications, each traced back to a Section 5 pattern and forward to a named portfolio bet, with the recommended portfolio-review action stated explicitly. A weak Section 6 lists generic recommendations, fails to trace back to patterns, or fails to name the portfolio bet the implication bears on.

---

## Output Structure

```markdown
# Win/Loss Decision Signal: [Cohort name]

**Signal ID**: WLD-[YYYY]-[NNN]
**Cohort**: [e.g., "Q1 2026 mid-market healthcare deals"]
**Cohort size**: [N deals — M won, L lost]
**Author**: [Competitive Intelligence lead name]
**Date authored**: [YYYY-MM-DD]
**Status**: Draft / In Review / Filed for Portfolio Gate / Consumed by Gate
**Next portfolio-review gate**: [YYYY-MM-DD]

---

## Section 1 — Decision frames the buyers used

| Deal | Outcome | Decision frame | Evidence |
|------|---------|----------------|----------|
| [Deal 1] | Won / Lost | Structured / Implicit / Political | [One or two sentences] |
| [Deal 2] | Won / Lost | Structured / Implicit / Political | [One or two sentences] |

## Section 2 — Named alternatives considered

| Deal | Outcome | Named alternatives (company + product) | Right shortlist? |
|------|---------|----------------------------------------|------------------|
| [Deal 1] | Won / Lost | [Acme Suite v3.2; Beta Platform v2.1] | Yes / No — [why] |

## Section 3 — Success criteria

| Deal | Outcome | Specified or implicit | Criteria | Strengths-to-criteria mapping |
|------|---------|----------------------|----------|-------------------------------|
| [Deal 1] | Won / Lost | Specified / Implicit | [Listed criteria] | Healthy / Misaligned — [why] |

## Section 4 — Per-deal decision-quality assessment

| Deal | Outcome | Decision quality (H/M/L) | Rationale |
|------|---------|--------------------------|-----------|
| [Deal 1] | Won / Lost | H / M / L | [One paragraph; flag fragile wins and genuine-signal losses explicitly] |

## Section 5 — Patterns across the cohort

### Patterns (supported by 3+ deals)

**Pattern 1.** [Claim]. Supporting deals: [Deal 1, Deal 3, Deal 5]. Strength: [3 of 6].

**Pattern 2.** [Claim]. Supporting deals: [...]. Strength: [...].

### Anecdotes (one-offs — for PMM-side enablement track, not portfolio gate)

**Anecdote 1.** [Deal-specific finding, demoted from pattern.] Supporting deal: [Deal 4].

## Section 6 — Strategic implication for portfolio review

**Implication 1.** [Claim or question for portfolio gate.]
- **Traces back to**: Pattern [N] in Section 5.
- **Traces forward to**: [Named portfolio bet, e.g., "Bet-2026-Q2-04 — Vertical expansion into mid-market healthcare"].
- **Recommended portfolio-review action**: [Specific action — re-scope qualification, shift positioning, defer bet, accelerate bet, etc.]

**Implication 2.** [Optional second implication.]
- **Traces back to**: Pattern [N].
- **Traces forward to**: [Named portfolio bet].
- **Recommended portfolio-review action**: [Specific action.]

---

## Appendix — Quality bar self-check

- [ ] Section 1 names a decision frame for every deal with evidence
- [ ] Section 2 names alternatives by company and product, with right-shortlist read
- [ ] Section 3 distinguishes specified from implicit criteria, and assesses strengths-to-criteria mapping
- [ ] Section 4 has a per-deal H/M/L rating with rationale; fragile wins and genuine-signal losses explicit
- [ ] Section 5 patterns are supported by 3+ deals; anecdotes demoted explicitly
- [ ] Section 6 implications trace back to Section 5 patterns AND forward to named portfolio bets
- [ ] Recommended portfolio-review action named for each implication
- [ ] Signal is shaped to feed the portfolio-review gate, not the deal-level enablement track
```

---

## Cross-references

| Skill | Relationship |
|-------|--------------|
| `/decision-quality-audit` | Adjacent — the audit consumes Section 4 per-deal decision-quality assessments as evidence for the wider decision-quality audit. The audit also extends with Decision Improvability framing (V5.1-37); the signal feeds that framing on the win/loss side. |
| `/positioning-statement` | Downstream consumer — when Section 6 names a positioning implication, the next iteration of the positioning statement is the artifact that operationalises it. |
| `/gtm-strategy` | Downstream consumer — when Section 6 names a GTM-motion implication (e.g., qualification-model change), the GTM strategy is the artifact that operationalises it. |
| `/competitive-battlecard` | Sister-track artifact owned by Product Marketing Management — produces deal-level enablement from the same underlying win/loss data. The two-track split is non-negotiable: this signal feeds the portfolio gate; battlecards feed the sales gate. |
| `/sales-enablement` | Sister-track artifact owned by Product Marketing Management — produces deal-level enablement collateral. Anecdotes from Section 5 may surface to that track; patterns from Section 5 stay with this signal. |
| `/competitive-landscape` | Adjacent — Section 2 named-alternatives data informs the competitive landscape. |
| `/portfolio-tradeoff` | Downstream consumer at the portfolio-review gate — Section 6 implications are inputs to portfolio-tradeoff decisions. |
| `/decision-record` | Adjacent — when the portfolio-review gate fires a re-decision based on Section 6, the resulting decision is captured as a decision record. |
| `/outcome-review` | Adjacent — quarterly outcome review consumes the signal as evidence for whether prior portfolio bets are tracking. |

---

## Instructions

1. **Detect the mode** (Create / Update / Find) using the table above. If confidence is below 70 percent, ask which mode.
2. **In Create mode**, walk Sections 1 through 6 in canonical order. Surface the prompt question for each section. Walk every deal in the cohort through Sections 1 through 4 (per-deal). Section 5 (patterns) and Section 6 (implications) are aggregate and authored after the per-deal reads are complete.
3. **Hold the discipline at Section 5.** A finding supported by one deal is an anecdote, not a pattern. Anecdotes are demoted to a separate subsection and routed to the PMM-side enablement track; only patterns surface to Section 6.
4. **Hold the discipline at Section 6.** No implication is allowed without (a) a Section 5 pattern it traces back to and (b) a named portfolio bet it traces forward to. An implication that fails either trace is opinion, not a gating signal.
5. **In Update mode**, preserve historical per-deal entries; re-derive aggregate patterns when new deals land in the cohort. Surface a diff summary of which patterns shifted in strength and which strategic implications updated.
6. **Save outputs** to `win-loss-signals/[cohort-slug].md` plus a JSON sidecar `[cohort-slug].json` with the six sections as keys for downstream gate consumption.
7. **Tag the signal with a Signal ID** of the form `WLD-[YYYY]-[NNN]` for context-graph linkage.
8. **Cross-reference the portfolio bets** named in Section 6 by portfolio identifier in the signal's metadata. A signal whose Section 6 cannot trace forward to a named bet is a signal that does not belong on the portfolio gate.

---

## Gotchas

- The signal is not a battlecard. Battlecards are Product Marketing Management's deal-level enablement artifact and feed the sales gate; this signal is Competitive Intelligence's portfolio-level read and feeds the portfolio gate. Do not produce battlecard content here.
- The signal is not a sales-narrative artifact. The decision-frame and decision-quality reads are honest assessments — including when wins were fragile and losses were positioning-driven. Laundering political wins as "executive sponsorship" or losses as "we did not have feature X" defeats the signal's purpose.
- The two-track split is non-negotiable. If a finding is one-off and deal-specific, it is an anecdote and goes to PMM. If a finding is cohort-wide and pattern-shaped, it is a signal and goes to portfolio review. Both tracks exist; both are legitimate; conflating them is the failure mode the signal is reframing.
- Patterns require 3+ supporting deals in a typical cohort of five-plus. Smaller cohorts can use lower thresholds with explicit caveat; the discipline is to be transparent about strength.
- Section 6 implications require both traces (back to a pattern, forward to a bet). Implications without traces are opinion and do not belong in a gating signal.
- Decision quality is independent of outcome. A low-quality decision that produced a win is a fragile win; a high-quality decision that produced a loss is a genuine competitive signal. The signal stays honest about this distinction.
- The signal feeds the portfolio-review gate. Cadence is gate-driven, not calendar-driven. Produce a signal when a portfolio-review gate is firing; do not produce one as routine reporting.
