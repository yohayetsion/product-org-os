---
name: ai-agent-supervisor
version: 1.0
owner: support-lead
co_owners: [cs-ops]
consumers: [support-lead, cs-ops, cs-dir, csm, onboarding-csm, kb-specialist, ai-architect, ml-engineer]
sensitive: false
sensitive_applicability: "NOT formally sensitive per .claude/rules/sensitive-skill-guardrails.md §2 (does not produce legal/HR/compliance advice). HOWEVER, deploying an AI support fleet carries customer-transparency obligations under state-level AI disclosure laws (California SB 243 / Colorado SB 205 / Utah AI Policy Act) and EU AI Act Article 50 (transparency obligations for AI systems interacting with natural persons). Sector-specific regimes (HIPAA, FCRA, FINRA suitability) layer on top when AI handles regulated content. Cross-reference compliance-frameworks.md and ai-act-readiness.md for the regulatory scaffolding."
v2v_wave: q2-4.2
related_packs_status: TBC-after-wave-2-stitching-pass
token_budget_variance_rationale: "D14 case (a) — joint-authored pack covering an emerging operating role spanning two domains (customer-facing support discipline + CS-Ops instrumentation), plus the operational definition of a new canonical KPI (Resolution Durability) replacing the legacy ticket-deflection metric. The pack is reference material consulted during AI-support-fleet deployment decisions, not preload."
---

# AI Agent Supervisor (V2V Knowledge Pack)

**Adapted from**:
  - HBR February 2026 — "The AI Agent Fleet Supervisor: A New Role Emerging from the AI-Support Frontier" (publicly documented executive framing)
  - Fin Operator (Intercom 2026 — fin.ai) — pioneered the supervisor pattern at production scale; publicly documented operator workflow
  - Anthropic Customer Support plugin (Q1 2026 — claude.com/plugins/customer-support) — 5 SKILLs + 5 slash commands + MCP connector patterns for AI-assisted support workflows
  - Gainsight "Agentic Stack for Customer Retention" announcement (2026-05-28, globenewswire.com/news-release/2026/05/28/3303094) — Agent Studio + Gainsight CLI + Gainsight MCP, the canonical CS-platform vendor formalizing the human-on-the-loop agent-management architecture

**Source licence**: per-source-terms (publicly documented patterns; HBR article framing, Intercom Fin Operator product documentation, Anthropic plugin public documentation, Gainsight press-release public announcement)

**V2V refinements**:
- Translated the emerging "AI agent fleet supervisor" role into a product-organization joint operating pattern between 🎟️ Support Lead (customer-facing discipline) and 📊 CS Ops (instrumentation and signal pipeline), rather than presenting it as a single new headcount
- Codified **Resolution Durability** (7-10 day reopen window) as the canonical AI-support KPI, explicitly replacing ticket deflection per HBR Feb 2026 framing
- Added the operational definition of Resolution Durability with the gameability analysis that motivated the metric change
- Cross-referenced Q2-4.1 `value-score-design.md` as load-bearing: the supervisor uses Value Score signals to interpret Resolution Durability (a reopen on a high-value account is a different escalation than a reopen on a low-value one), and that connection is what makes the metric operationally durable
- Added the supervisor-vs-AI-engineer boundary (supervisor owns operational discipline; AI eng owns model and prompt artifacts), to prevent the failure mode where AI-support deployments have no operational owner
- Added anti-patterns drawn from publicly documented AI-support failures: deflection-as-success-metric, no-supervisor pattern, reopen-window too short, missing customer transparency, retraining cadence vs drift mismatch
- Mapped the supervisor's 5 disciplines to V2V Phase 4 (Execution) operating rhythms — daily, weekly, monthly cadences
- **2026-06 delta**: added the build-vs-buy-vs-managed three-tier sourcing model and MCP-as-CS-substrate, grounding the abstract Agent-Manager thesis in the Gainsight Agentic Stack (2026-05-28) as a concrete dated vendor instantiation

---

## What an AI Agent Fleet Supervisor Is

The AI Agent Fleet Supervisor is the operating role that emerged in 2025-2026 at the intersection of CS-Ops and Support-Lead, as production support orgs deployed AI agents (Intercom Fin, Anthropic-assisted custom agents, Decagon, Sierra, Ada) at scale and discovered that **deploying the AI is not the hard part — supervising the deployment is**.

The supervisor owns the operational discipline of an AI support agent fleet across five domains: routing, escalation, quality, reopen monitoring, and retraining triggers. The supervisor does **not** build, train, or fine-tune the AI agent — that work belongs to AI engineering, MLOps, or a third-party vendor's deployment team. The supervisor owns the **operating envelope** the fleet runs within: which tickets the AI agent is allowed to handle, what triggers handoff to a human, how quality is sampled, when the fleet is degrading, and what the customer sees about the AI's involvement.

In product-organization terms, the supervisor role lands jointly on 🎟️ Support Lead (customer-facing discipline: routing thresholds, escalation policy, customer transparency, voice and tone of AI responses) and 📊 CS Ops (instrumentation: Resolution Durability pipeline, quality sampling protocol, retraining trigger detection, dashboard ownership). Per HBR Feb 2026, some larger orgs spin this up as a dedicated full-time role; in V2V-scale product organizations, the joint Support Lead + CS Ops pattern works through the equivalent maturity stages without adding headcount.

---

## Why the Role Emerged in 2026

Pre-2026, support organizations deployed AI chatbots and AI ticket-assist tools, and measured them on **ticket deflection** — the percentage of tickets the AI closed without human escalation. This metric is intuitive (every deflected ticket is a saved seat-minute) and easy to instrument, which is why every AI-support vendor's marketing page reported it.

The metric is also gameable, and the gameability became visible at production scale once AI agents were handling double-digit-percent ticket volume in 2025. The dominant failure mode: the AI closes a ticket prematurely with a confident-sounding response, the customer's actual issue isn't resolved, the customer reopens the conversation 3-7 days later — and because the reopen is filed as a new ticket, the deflection metric stays high while customer satisfaction degrades silently. A second failure mode: the AI deflects the ticket by routing it to a self-service article that doesn't actually answer the question; the customer's friction is invisible to the metric because the ticket "closed."

HBR Feb 2026 named this pattern and named the operational fix: **Resolution Durability replaces deflection as the canonical AI-support KPI**. Did the issue stay resolved over a defined reopen window — typically 7-10 days — without the customer coming back? The metric is harder to game because it requires the AI's resolution to actually solve the problem, not just close the ticket. Intercom's Fin Operator framework operationalized this at scale, exposing reopen-window dashboards as the primary supervisor surface. Anthropic's Customer Support plugin (Q1 2026) shipped slash commands oriented around the same model: `/triage`, `/escalate`, `/quality-sample`, `/draft-response`, `/customer-context` — none of which optimize for closing fast, all of which optimize for resolving correctly.

The role emerged because the metric changed. When the metric was deflection, an engineer could deploy the bot and walk away — the bot's autonomous closure rate was the dashboard. When the metric is Resolution Durability, **someone has to watch what happens 7-10 days after closure**, and that someone is the supervisor.

---

## 2026-06 Delta Update (as of 2026-06-06)

### Gainsight Agentic Stack — the Agent-Manager thesis, dated and instantiated (2026-05-28)

On 2026-05-28 Gainsight announced its entire platform is now agentic ("The Agentic Stack for Customer Retention"). This is the canonical CS-platform vendor formalizing the human-on-the-loop agent-management architecture this pack describes abstractly. It supplies a concrete dated instantiation of the supervisor / Agent-Manager thesis: the supervisor does not disappear when the platform goes agentic — it is renamed and made first-class.

**Announced components**:

| Component | What it is | Status (as of announcement) |
|---|---|---|
| **Gainsight Agent Studio** | Agentic workspace "powered by Claude"; plain-language workflow design for CS agents | Waitlist |
| **Gainsight CLI** | Admins build CS workflows via coding agents (Claude Code / Codex / Gemini) | Summer 2026 |
| **Gainsight MCP** | MCP server exposing Gainsight as agent-callable substrate | Live for CS + Staircase (175,000+ tool calls, 96,000+ queries); open beta for Skilljar / Communities / Product Experience |

**Pre-built agents** shipped or framed: Staircase Handoff Analyst, Risk Analyst, Expansion Analyst, Community Moderation Agent, Skilljar AI Tutor. Gainsight also announced strategic Salesforce integration and inclusion in the Salesforce Agentforce MCP beta at launch. The CEO framed the posture as "build AND buy."

### Build-vs-Buy-vs-Managed: the three-tier sourcing model

The Gainsight announcement makes the supervisor's first structural decision explicit — **how the AI support fleet is sourced** — and that decision now has three tiers, not two. The supervisor (Support Lead policy + CS Ops instrumentation) owns the tier choice; the choice changes who holds Resolution Durability accountability but never removes the supervisor discipline.

| Tier | What it is | Who owns the operating envelope | Supervisor implication |
|---|---|---|---|
| **Build** | Custom agents on a platform's agentic primitives (e.g., Gainsight Agent Studio / CLI, or first-party LLM + MCP) | Internal supervisor (Support Lead + CS Ops) fully | Maximum control; supervisor owns routing, escalation, quality, reopen, retraining end-to-end |
| **Buy** | Pre-built vendor agents (e.g., Gainsight's Risk / Expansion / Handoff analysts, Intercom Fin, Decagon, Sierra) | Internal supervisor owns the envelope; vendor owns the model | Supervisor still sets thresholds, samples quality, monitors Resolution Durability; vendor owns model artifacts |
| **Managed** | Vendor owns the OUTCOME end-to-end as a managed service (see `value-score-design.md` 2026-06 delta on Gainsight Atlas AI-Native Services) | Vendor's Renewal/Agent Managers own the envelope; internal supervisor governs the contract + outcome SLA | Supervisor discipline shifts to vendor-governance: outcome-metric audit (GRR/NRR, Resolution Durability), escalation-path verification, transparency-obligation flow-down |

"Build AND buy" (and increasingly "managed") is the honest 2026 read: most production CS orgs run a mix. The supervisor's job is not to pick one tier forever but to assign each ticket class to the right tier and hold Resolution Durability accountability across the mix.

### MCP-as-CS-substrate

Gainsight MCP being live at production scale (175,000+ tool calls) is the dated proof that **MCP is becoming the CS data/action substrate**, not just an experiment. For the supervisor this matters in two places already in this pack: escalation routing and reopen response both depend on the AI reaching customer-context tools, and when those tools are MCP servers, the governance posture (`mcp-governance.md` Q2-3.2) and the transport/capability-negotiation patterns (`mcp-architecture.md` Q2-5.1) apply directly. The 2026-06 addition: treat the MCP layer as a first-class supervisor surface — registry, approval, and audit of which CS tools the agent fleet can call is now part of the operating envelope, not a separate IT concern.

**Cross-reference**: the managed-service tier above is the reciprocal of the `value-score-design.md` 2026-06 delta (Gainsight Atlas AI-Native Services, 2026-05-27) — the "CS-as-outcome-service" commercial model where the vendor owns the renewal outcome tied to GRR/NRR.

---

## The Supervisor's 5 Operating Disciplines

### 1. Resolution Durability Monitoring

The new canonical KPI. The supervisor (CS Ops as instrument owner, Support Lead as policy owner) defines the reopen window (typically 7-10 days), instruments the pipeline to flag reopens against original AI-closed tickets (not new tickets from the same customer), and reports Resolution Durability as the headline AI-support metric.

The non-trivial decisions: the window length (see "Resolution Durability" section below for the honest read on 7-10 days), the reopen-attribution rule (a reopen by the same customer on the same issue counts; a reopen on a new issue does not), and the escalation rule when Resolution Durability degrades (what threshold triggers a retraining cycle, a prompt revision, or a deployment rollback).

### 2. Escalation Routing

When the AI agent should hand off to a human. The supervisor sets the policy; AI engineering implements it. Three routing patterns dominate:

- **Confidence-driven**: the AI's own confidence score against the response. Below threshold → human. Brittle because confidence is poorly calibrated on novel cases — the AI is most confident when wrong about an out-of-distribution issue.
- **Sentiment-driven**: customer frustration signal (escalation language, repeat questions, ALL-CAPS, profanity). Reliable for catching frustration; misses calm customers with hard problems.
- **Complexity-driven**: ticket-feature heuristics (multi-account, billing-dispute, security-adjacent, regulated-content) auto-route to human regardless of AI confidence. Slowest but safest; the right default for high-stakes ticket classes.

Production deployments combine all three. The supervisor owns the threshold and the policy mix; the AI engineering team owns the implementation.

### 3. Quality Sampling

Random sampling protocol for AI-handled tickets. The supervisor (Support Lead policy, CS Ops execution) defines sample size, review cadence, and reviewer panel. Industry pattern: 2-5% of AI-closed tickets sampled weekly, scored against a rubric (resolution correctness, tone, brand voice, hallucination risk, handoff appropriateness). The sampling is not statistical sampling for quality estimation alone — its second purpose is **training-data generation**: high-quality AI responses become canonical examples; failures become retraining inputs.

Larger orgs separate sampling-for-quality (random) from sampling-for-retraining (failure-weighted). V2V-scale orgs typically combine them, with explicit annotation when a sampled ticket is being routed to the retraining pipeline.

### 4. Retraining Triggers

What signals trigger model retraining versus prompt revision versus KB augmentation. The cost ordering matters: prompt revision is cheap and same-day; KB augmentation is cheap and weekly; retraining is expensive and quarterly-or-slower. The supervisor's job is to route the failure to the right intervention level.

Typical decision rule:
- **Single failure, content gap**: KB augmentation (add the missing article; AI agent picks it up).
- **Pattern failure, instruction gap**: prompt revision (update system prompt to handle the pattern).
- **Pattern failure, capability gap**: retraining or model upgrade (the model itself can't do the task).
- **Distribution shift** (Resolution Durability degrading across categories): full retraining cycle.

The supervisor doesn't do the retraining; the supervisor calls when retraining is needed and accepts the cost.

### 5. Customer Transparency

Disclosure protocols. When the customer should know they're talking to AI, what wording, and how handoff to human is announced. This discipline carries regulatory weight: California SB 243 (chatbot disclosure), Colorado SB 205 (AI Act disclosure), Utah AI Policy Act, and EU AI Act Article 50 (transparency obligations for AI systems interacting with natural persons) all impose disclosure requirements. Sector-specific regimes (HIPAA for health, FCRA for credit-adjacent, FINRA suitability for financial advice) layer additional obligations when the AI handles regulated content.

The supervisor's discipline is to define the disclosure pattern (when AI identifies itself, what the disclosure says, whether handoff to human is explicitly announced, what records are retained), to honor jurisdiction-specific obligations, and to update the pattern as regulation evolves. Cross-reference `compliance-frameworks.md` for the regulatory layer and `ai-act-readiness.md` for EU AI Act specifics.

---

## Resolution Durability (the canonical KPI)

**Formal definition**: For an AI-closed ticket at time T, Resolution Durability = 1 if the same customer does not reopen a substantively similar issue within the window [T, T+N days], else 0. The org-level metric is the rolling N-day average across all AI-closed tickets. The window N is typically 7-10 days.

**Why 7-10 days, our honest read**: HBR Feb 2026 cites 7-10 days because that range captures most genuine reopens (customer tries the AI's resolution, finds it doesn't work, comes back) without catching unrelated re-engagements (customer comes back about a different issue 3 weeks later). The empirical case for 7 days is that 80%+ of legitimate reopens land within a week. The case for 10 days is that some intermittent issues (billing cycles, sync-on-next-login, edge-case workflows) only manifest once-per-week, and a 7-day window misses them. **Our read**: 10 days is the safer default for V2V-scale orgs because the cost of a false negative (missing a real failure) is higher than the cost of a false positive (catching an unrelated reopen). Start at 10, tighten to 7 once your reopen-attribution rules are mature enough to discriminate same-issue from different-issue reopens cleanly.

**Instrumentation requirements** (CS Ops scope):
- Ticket-level join: every reopen must carry a pointer back to the original AI-closed ticket if it's a same-issue reopen
- Same-issue classification: either heuristic (same customer, same product area, within window) or model-assisted (embedding similarity between original and reopen issue text). Heuristic is fine to start; model-assisted is the maturity upgrade
- Reopen-window enforcement: the metric is calculated as a moving window, not at end-of-quarter
- Dashboard surfaces: daily Resolution Durability number, 7-day moving average, weekly drill-down by ticket category and (load-bearing per cross-ref below) by customer Value Score band

**Target-setting without optimizing the wrong thing**: do not set a Resolution Durability target that the supervisor cannot influence. If the target is set as "Resolution Durability ≥ 90%," the supervisor optimizes for the metric by being increasingly conservative about which tickets the AI handles in the first place — pushing all hard tickets to humans, achieving the target by reducing AI scope. This is the new gameability. The right framing is a **paired target**: Resolution Durability AND AI ticket coverage (% of total tickets the AI handles), targeted together. The supervisor's job is to push both up, not one at the expense of the other.

---

## Cross-References to Q2-4.1 Value Score (load-bearing)

The connection between Resolution Durability and customer Value Score (Q2-4.1 `value-score-design.md`) is what makes the supervisor metric operationally durable. A reopen on a top-quartile-by-Value-Score customer is not the same event as a reopen on a low-Value-Score customer:

- **High-Value-Score customer reopen**: surface immediately to Support Lead and CSM, treat as P0 for the Value Realization function, root-cause within 48h, and feed the failure into retraining as a high-weight example
- **Low-Value-Score customer reopen**: aggregate into the weekly Resolution Durability dashboard, root-cause if the pattern repeats, but do not pull Support Lead attention on the single instance

This is not "we care less about low-value customers" — it's "the resolution failure on a high-value customer is an enterprise-account-risk signal, and the resolution failure on a low-value customer is a product-quality signal, and the two failures require different operational responses."

The supervisor uses Value Score signals at two surfaces:
1. **Routing escalation**: high-Value-Score customer tickets get more conservative routing (lower AI-confidence threshold for handoff to human, complexity-driven routing tightened)
2. **Reopen response**: Resolution Durability dashboard breaks down by Value Score band, and degradation in the top-quartile band is the alarm condition

Cross-reference Q2-4.1 `value-score-design.md` for the Value Score definition, signal architecture, and the data pipeline that feeds these decisions. Without that pack's Value Score, Resolution Durability is a single org-wide number that conflates the strategic-account signal with the volume-customer signal. With Value Score, it's a banded metric that drives differentiated operational response.

---

## V2V Phase 4 (Execution) Integration

The supervisor's five disciplines map to V2V Phase 4 (Execution) operating rhythms:

**Daily** (CS Ops owns the dashboard, Support Lead reviews exceptions)
- Resolution Durability rolling number (yesterday's AI-closed tickets that reopened today; today's reopens against the 7-10 day prior window)
- High-Value-Score customer reopens (immediate Support Lead + CSM surfacing)
- Escalation-rate trend (% of AI tickets escalating to human; a sudden spike is a degradation signal)

**Weekly** (jointly owned)
- Quality sample review (2-5% of AI-closed tickets scored against rubric)
- Resolution Durability by category and Value Score band
- New failure patterns surfaced from sampling and reopens

**Monthly** (Support Lead and CS Ops jointly, CS Dir consulted)
- Retraining trigger review: which failure patterns have accumulated enough volume to justify retraining vs. prompt revision vs. KB augmentation
- Coverage review: which ticket categories should the AI handle that it doesn't, and which should it not handle that it does
- Customer transparency audit: disclosure pattern current with regulatory landscape

**Quarterly** (CS Dir owns, supervisor reports)
- Resolution Durability target review against AI ticket coverage target (paired targets per "Resolution Durability" section)
- Vendor or model upgrade evaluation
- Regulatory disclosure review (jurisdiction additions, sector regimes)

---

## Anti-Patterns / Common Failures

| Anti-pattern | Why harmful | What V2V does instead |
|---|---|---|
| **Ticket deflection treated as success metric** | Gameable (premature closure, reopens as new tickets, self-service routing without resolution); customer-hostile; silently degrades CSAT | Resolution Durability as canonical KPI; deflection retained as a secondary throughput metric only |
| **No supervisor pattern** | AI deployed by engineering, no operational owner, silent drift, no one watching Resolution Durability after launch | Explicit joint Support Lead + CS Ops ownership before any AI fleet goes to production |
| **Reopen window too short** (e.g., 3 days) | Catches false positives (customers reopening on unrelated issues), misses real failures on intermittent-issue categories (billing cycles, weekly sync, edge-case workflows) | Start at 10 days, tighten to 7 once reopen-attribution rules are mature |
| **Missing customer transparency** | Regulatory exposure (California SB 243, Colorado SB 205, Utah AI Policy Act, EU AI Act Article 50, sector regimes); customer-trust degradation when AI involvement is discovered after the fact | Explicit disclosure pattern as part of supervisor discipline 5; cross-reference compliance-frameworks.md |
| **Retraining cadence too slow vs. drift rate** | The AI's training data ages out of distribution (new product features, new customer language, new edge cases), Resolution Durability degrades, supervisor doesn't have authority to call retraining | Supervisor has explicit retraining-trigger authority; CS Dir or VP CS accepts the cost when supervisor calls it |
| **Conflating supervisor role with AI engineering role** | Supervisor without engineering authority can't fix model issues; AI engineer without operational signal optimizes for the wrong metric (technical accuracy, not Resolution Durability) | Clean separation: supervisor owns operational discipline (routing, escalation, quality, reopen, retraining triggers); AI eng owns model artifacts and implementation |
| **Resolution Durability target without paired AI-coverage target** | Supervisor optimizes by reducing AI scope — pushing every hard ticket to human, achieving target by abandoning AI value | Paired targets: Resolution Durability AND % AI ticket coverage, moved up together |
| **Single org-wide Resolution Durability number** | High-value-customer reopens hide inside the average; volume-customer reopens dominate the signal | Banded reporting by Value Score (cross-ref Q2-4.1); differentiated operational response by band |
| **Quality sampling without rubric** | Reviewer reports inconsistent; sampled tickets don't feed retraining pipeline; sampling becomes performative | Explicit rubric (resolution correctness, tone, brand voice, hallucination risk, handoff appropriateness); sampled failures annotated for retraining |

---

## V2V Cross-References

**Sibling Q2-4 packs**:
- **`value-score-design.md` (Q2-4.1)** — **load-bearing reciprocal**. The supervisor uses Value Score signals to interpret Resolution Durability per §"Cross-References to Q2-4.1 Value Score" above; high-value customer reopens vs. volume-customer reopens require differentiated operational response. Banded Resolution Durability requires Value Score as the band axis.
- **`customer-success-methodology.md` (Q2-4.3 refresh)** — supervisor disciplines integrate with broader CS health and renewal motion. Resolution Durability is the AI-support KPI in that pack's CS Metrics table, replacing ticket deflection.

**Sibling Q2-5 packs**:
- **`agentic-security.md` (Q2-5.3)** — security and threat model for AI support agents: prompt injection from customer messages (OWASP LLM01 with full agent-system blast radius), data-exfiltration risk in tool calls (CSA Agentic Trust Framework Risk Class 1), agent-to-agent authentication when the support AI invokes other agents (Q2-3.1 patterns).
- **`mcp-architecture.md` (Q2-5.1)** — when AI support agents reach customer-context tools via MCP (CRM lookups, account-state queries), the transport variants and capability negotiation in that pack apply.
- **`agent-identity.md` (Q2-3.1)** — the support-AI agent's system identity governs its capability scope; lifecycle management (provisioning, deactivation) applies to AI support agent fleets.

**Sibling Q2-3 packs**:
- **`mcp-governance.md` (Q2-3.2)** — when support AI invokes MCP servers (knowledge base, ticket system, customer data), the governance posture (registry, approval, audit) applies.
- **`eu-ai-act-annex-iv.md` (Q2-3.4)** — AI support fleets interacting with EU data subjects fall under Article 50 (transparency); Annex IV §3 (monitoring) documentation cites Resolution Durability instrumentation.

**Sibling Q2-6 + Q2-7 packs**:
- **`retention-marketing.md` (Q2-6.2)** — silent customer disengagement caused by AI-resolution failures becomes a re-engagement-marketing problem if Resolution Durability degrades on engaged-but-frustrated customers.

**Existing packs**:
- `customer-success-methodology.md` — current CS methodology pack (refresh integrated 2026-05-18 per Q2-4.3).
- `support-operations.md` — tiered support model, SLA framework, ticket lifecycle; the AI agent supervisor sits at Tier 0/Tier 1 boundary.
- `ai-act-readiness.md` — EU AI Act Article 50 transparency obligations apply directly to AI support fleets interacting with EU data subjects.
- `compliance-frameworks.md` — state-level AI disclosure laws (California SB 243, Colorado SB 205, Utah AI Policy Act), FCRA / HIPAA / FINRA sector regimes when AI handles regulated content.
- `privacy-frameworks.md` — GDPR coverage when AI support handles EU customer data.

---

## Sensitive-skill applicability

This pack is **NOT formally sensitive** under `.claude/rules/sensitive-skill-guardrails.md` §2 — it does not produce legal, HR, or compliance advice. The supervisor disciplines are operational, not advisory.

**However**, deploying an AI support fleet carries customer-transparency obligations and sector-specific regulatory layers that the supervisor must honor:

- **State-level AI disclosure laws**: California SB 243 (chatbot disclosure), Colorado SB 205 (AI Act), Utah AI Policy Act, and the growing patchwork of state-level analogs in 2026
- **EU AI Act Article 50**: transparency obligations for AI systems interacting with natural persons (notify the customer they are interacting with an AI system unless it is obvious from context)
- **Sector regimes**: HIPAA when AI handles PHI in support tickets; FCRA when AI output supports adverse-action decisions; FINRA suitability when AI provides financial-product guidance; sector-specific frames apply in health, finance, credit, and employment-adjacent contexts

Supervisor decisions about disclosure pattern, retention of AI-conversation logs, and routing of regulated-content tickets to human-only handling carry compliance weight. Cross-reference `compliance-frameworks.md` (state-level + sector regimes) and `ai-act-readiness.md` (EU AI Act specifics) before finalizing the customer-transparency discipline.

---

## Operating Principle

> *The supervisor isn't the AI agent — and the metric isn't deflection. The supervisor owns Resolution Durability, and Resolution Durability is the only AI-support KPI that doesn't game.*
