---
globs:
  - "**/*"
---

# Skill Awareness & Routing

Skill catalog, invocation syntax, routing rules, and agent selection for the Vision to Value Product Org Plugin.

---

## Invocation Syntax (MANDATORY)

| Notation | Tool | Purpose | Example |
|----------|------|---------|---------|
| `/skill-name` | Skill tool | Invoke template/workflow **inline** | `/prd`, `/decision-record` |
| `@agent-name` | Task tool | Spawn **individual autonomous agent** | `@pm`, `@vp-product` |
| `@product`, `@plt` | Skill tool | Trigger **gateway protocol** (Meeting Mode) | `@product launch feature` |
| `@file.md` | Context | Include file contents in conversation | `@strategy.md` |

**Individual Agents** (`@pm`, `@vp-product`): Spawn a single agent via Task tool. One perspective, one voice.
**Gateways** (`@product`, `@plt`): Trigger multi-agent Meeting Mode via Skill tool. Multiple perspectives + synthesis.

### Dual-Mode Invocation

| Mode | Syntax | Behavior | Use Case |
|------|--------|----------|----------|
| **Inline** | `/pm` | Skill tool — Claude adopts persona, continues conversation | Quick back-and-forth |
| **Autonomous** | `@pm` | Task tool — Spawns agent, returns when done | Delegating work |

---

## Automatic Routing (MANDATORY)

When user mentions `@agent` or `@gateway`, **immediately invoke without asking**. When user uses `/skill`, **execute immediately**.

**Do NOT** ask "would you like me to route this?" — just do it.

### Routing Decision Process

1. Explicit `@` or `/` mention → Route to that agent/skill immediately
2. Clear domain keywords → Route to domain owner (see `agent-spawn-protocol.md` Section 6)
3. Multi-domain / ambiguous → Use `/product` gateway
4. Portfolio/strategic tradeoff → Use `/plt` gateway

**Always prefer fewer agents**: 1 over 2, 2 over 3, 3 over PLT.

### Enhanced Decision Matrix

| Intent Pattern | Keywords | Route To |
|----------------|----------|----------|
| Requirements | PRD, feature, user story, spec | `@pm` |
| Pricing/Business | pricing, business case, ROI, financial, lean canvas, business model canvas | `@bizops` |
| GTM/Positioning | launch, positioning, messaging, campaign, battlecard | `@pmm-dir` |
| Competitive | competitor, market share, win/loss, Porter, five forces, blue ocean | `@ci` |
| Strategy/Vision | vision, strategy, portfolio, bet, DHM, press release FAQ, PRFAQ, Ansoff, BCG matrix | `@vp-product` |
| Discovery/Validation | assumption, experiment, opportunity tree, hypothesis, validate, pretotype, four risks, interview synthesis | `@pm` |
| Prioritization | prioritize, RICE, Kano, MoSCoW, WSJF, rank features, what to build | `@pm-dir` |
| Roadmap | roadmap, planning | `@pm-dir` |
| Launch Ops | readiness, coordination, process | `@prod-ops` |
| Customer Outcomes | adoption, success, health, churn, north star metric, customer journey | `@value-realization` |
| Partnerships | partner, ecosystem, channel | `@bizdev` |
| Design/UX | user research, usability, design, journey map | `@ux-lead` |
| Macro Analysis | PESTLE, SWOT, macro environment, external factors, industry analysis | `@ci` |
| Decision Quality | bias check, cognitive bias, decision quality, blind spots | `@vp-product` |
| Stakeholder Management | stakeholder map, influence grid, RACI, power interest | `@pm-dir` |
| Growth Strategy | growth model, growth loops, viral, PLG, product-led, Racecar | `@bizops` |
| Product Learning | teardown, reverse engineer, analyze product | `@pm` |
| Productivity | daily briefing, task list, meeting notes, schedule | `@pa` |
| Research/Analysis | data analysis, research brief, trend report, comparison | `@analyst` |
| Coaching/Career | career, coaching, skill assessment, development plan, growth | `@coach` |
| Multi-stakeholder | "help me decide", portfolio tradeoff | `@plt` |

### Question Threshold

**ONLY ask when**: Truly ambiguous (could mean opposite things), critical info missing (no topic specified), or user explicitly requested options.

**NEVER ask because**: Multiple agents could handle it, confidence is "medium", or you want confirmation.

---

## Document Intelligence

68 document-generating skills support three modes:
- **CREATE**: Default — `/prd authentication`
- **UPDATE**: When using "update", "revise", or providing a path
- **FIND**: When using "find", "search", or "list"

14 context/retrieval skills (context-save, context-recall, portfolio-status, relevant-learnings, handoff, feedback-capture, feedback-recall, interaction-recall, maturity-check, pm-level-check, setup, present, phase-check, interaction-recall) operate differently.

---

## Skills by Vision to Value Phase

| Phase | Skills |
|-------|--------|
| **1. Foundation** | `/strategic-intent`, `/market-analysis`, `/competitive-landscape`, `/competitive-analysis`, `/vision-statement`, `/market-segment`, `/assumption-map`, `/opportunity-tree`, `/experiment-design`, `/lean-canvas`, `/business-model-canvas`, `/customer-journey-map`, `/interview-synthesis`, `/pretotype`, `/press-release-faq`, `/ansoff-matrix`, `/pestle-analysis`, `/porter-five-forces`, `/swot-analysis`, `/blue-ocean` |
| **2. Decisions** | `/business-case`, `/business-plan`, `/pricing-strategy`, `/pricing-model`, `/positioning-statement`, `/decision-record`, `/strategic-bet`, `/decision-charter`, `/escalation-rule`, `/four-risks-check`, `/dhm-analysis`, `/growth-model`, `/bcg-matrix`, `/stakeholder-map` |
| **3. Commitments** | `/product-roadmap`, `/roadmap-theme`, `/roadmap-item`, `/gtm-strategy`, `/gtm-brief`, `/launch-plan`, `/strategy-communication`, `/commitment-check`, `/prd`, `/prd-outline`, `/feature-spec`, `/user-story`, `/prioritize-features` |
| **4. Execution** | `/campaign-brief`, `/sales-enablement`, `/launch-readiness`, `/stakeholder-brief`, `/competitive-battlecard` |
| **5. Outcomes** | `/onboarding-playbook`, `/value-realization-report`, `/customer-health-scorecard`, `/north-star-metric` |
| **6. Learning** | `/outcome-review`, `/retrospective`, `/decision-quality-audit`, `/relevant-learnings`, `/context-save`, `/feedback-capture`, `/compound`, `/product-teardown`, `/bias-check` |
| **Cross-Phase** | `/context-recall`, `/feedback-recall`, `/interaction-recall`, `/portfolio-status`, `/portfolio-tradeoff`, `/handoff`, `/qbr-deck`, `/maturity-check`, `/pm-level-check`, `/phase-check`, `/ownership-map`, `/customer-value-trace`, `/collaboration-check`, `/scale-check`, `/vision-to-value-document-map` |

---

## Skill Selection by Task Type

**Strategic planning**: `/strategic-intent`, `/strategic-bet`, `/vision-statement`, `/dhm-analysis`, `/press-release-faq`
**Discovery & validation**: `/assumption-map`, `/opportunity-tree`, `/experiment-design`, `/pretotype`, `/interview-synthesis`, `/four-risks-check`
**Market understanding**: `/market-analysis`, `/competitive-landscape`, `/market-segment`, `/porter-five-forces`, `/pestle-analysis`, `/blue-ocean`
**Business modeling**: `/lean-canvas`, `/business-model-canvas`, `/ansoff-matrix`, `/bcg-matrix`
**Commercial decisions**: `/business-case`, `/pricing-strategy`, `/decision-record`, `/growth-model`
**Prioritization**: `/prioritize-features` (RICE, Kano, MoSCoW, WSJF)
**Execution planning**: `/product-roadmap`, `/gtm-strategy`, `/launch-plan`, `/stakeholder-map`
**Requirements**: `/prd`, `/feature-spec`, `/user-story`
**Go-to-market**: `/campaign-brief`, `/sales-enablement`, `/launch-readiness`, `/competitive-battlecard`
**Customer success**: `/onboarding-playbook`, `/value-realization-report`, `/north-star-metric`
**Customer understanding**: `/customer-journey-map`, `/customer-health-scorecard`
**Decision quality**: `/bias-check`, `/decision-quality-audit`
**Learning**: `/outcome-review`, `/retrospective`, `/compound`, `/product-teardown`
**Assessment frameworks**: `/swot-analysis`, `/pestle-analysis`, `/porter-five-forces`, `/ansoff-matrix`, `/bcg-matrix`, `/blue-ocean`

**Strategic asset overview**: `/vision-to-value-document-map`
**Before decisions**: `/context-recall`, `/feedback-recall`, `/customer-value-trace`, `/bias-check`
**Before commitments**: `/commitment-check`, `/ownership-map`, `/phase-check`, `/four-risks-check`
**After outcomes**: `/outcome-review`, `/scale-check`, `/context-save`

---

## Vision to Value Operating Principle

> "Every skill exists for a reason. Choose the right skill for the task, not the task for the skill you know."

> "Routing is invisible when done well. Users should feel like they're talking to a team that just gets things done."
