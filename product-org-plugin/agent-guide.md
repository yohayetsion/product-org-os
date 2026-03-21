# Product Org OS — Agent Guide

**A complete AI product organization as a plugin.** This guide tells any coding agent everything it needs to install, configure, and operate the system.

---

## What This Is

Product Org OS gives you 13 role-based product agents, 103 skills, 2 gateways, 9 knowledge packs, and a persistent context layer. It turns a coding agent into an entire product organization — from strategic intent through execution to learning.

Built on the **Vision to Value** framework: a 6-phase system that flows from strategy to outcomes to learning loops.

**Works with**: Claude Code (primary), Cursor, GitHub Copilot, Gemini CLI, Windsurf, and other Agent Skills-standard tools.

---

## Installation

### Claude Code (Primary)

```bash
claude plugins install github:yohayetsion/product-org-os
```

Then initialize in your project:

```
/setup
```

This creates the `context/` directory structure in your current working directory for organizational memory.

### Cursor

1. Clone or download the plugin to your project
2. Add to `.cursorrules`: point to the plugin's `PRODUCT-ORG-CLAUDE.md` and `agent-guide.md`
3. Run `/setup` to initialize the context layer

### Copilot / Gemini CLI / Other

1. Clone or download the plugin
2. Point your agent's system prompt or rules file to `PRODUCT-ORG-CLAUDE.md`
3. Run `/setup` to initialize context

### Post-Setup

After `/setup`, your project will have:

```
your-project/
├── context/                  # Organizational memory
│   ├── decisions/            # Decision records (DR-YYYY-NNN)
│   ├── bets/                 # Strategic bets (SB-YYYY-NNN)
│   ├── assumptions/          # Tracked assumptions
│   ├── portfolio/            # Portfolio state
│   ├── learnings/            # Accumulated wisdom
│   ├── handoffs/             # Agent delegation context
│   ├── feedback/             # Customer/market feedback (FB-YYYY-NNN)
│   ├── documents/            # Document registry
│   ├── interactions/         # Agent conversation logs
│   ├── roi/                  # Time savings tracking
│   └── preferences/          # Organizational conventions
└── ... your project files
```

---

## How It Works

### Two Invocation Patterns

| Syntax | Purpose | Example |
|--------|---------|---------|
| `@agent` | **Delegate** — spawn autonomous agent | `@pm create a PRD for auth` |
| `/skill` | **Inline** — use template/workflow directly | `/prd authentication` |

Both access the same capabilities. `@agent` spawns an independent agent that returns when done. `/skill` executes inline in the current conversation.

### The 13 Agents

| Agent | Shortcut | Domain |
|-------|----------|--------|
| `@cpo` | — | Executive strategy, portfolio decisions |
| `@vp-product` | `@vpp` | Vision, roadmap accountability, pricing |
| `@director-product-management` | `@pm-dir` | Roadmap governance, team coordination |
| `@director-product-marketing` | `@pmm-dir` | GTM strategy, positioning, launches |
| `@product-manager` | `@pm` | Feature specs, user stories, delivery |
| `@product-marketing-manager` | `@pmm` | Campaigns, collateral, enablement |
| `@product-leadership-team` | `@plt` | Portfolio tradeoffs, strategic alignment |
| `@bizops` | — | Business cases, financial analysis, KPIs |
| `@bizdev` | — | Partnerships, market expansion |
| `@competitive-intelligence` | `@ci` | Competitor analysis, market research |
| `@product-operations` | `@prod-ops` | Process optimization, launch coordination |
| `@value-realization` | — | Success metrics, customer outcomes |
| `@ux-lead` | — | User research, design specs |

### The 2 Gateways

| Gateway | What It Does |
|---------|-------------|
| `@product` | **Main entry point.** Routes your request to the right agents automatically. Use when you're unsure who should handle something, or when it's cross-functional. |
| `@plt` | **Product Leadership Team.** Convenes senior agents for portfolio tradeoffs and strategic decisions. |

### Meeting Mode

When `@product` or `@plt` engages multiple agents, responses come as a **meeting** — each agent speaks in first person with their own perspective, followed by points of agreement, tension, and a synthesis. This isn't a monolithic AI response; it's your product org thinking together.

### Response Depth

Add `+` or `-` to control verbosity:

| Modifier | Effect | Example |
|----------|--------|---------|
| `-` | Brief — executive summary | `@product What's launch status? -` |
| *(none)* | Standard — balanced depth | `@product What's launch status?` |
| `+` | Deep — full analysis | `@product What's launch status? +` |

---

## The 103 Skills

### By Vision to Value Phase

**Phase 1 — Strategic Foundation** (20 skills)
`/strategic-intent` `/market-analysis` `/competitive-landscape` `/competitive-analysis` `/vision-statement` `/market-segment` `/assumption-map` `/opportunity-tree` `/experiment-design` `/lean-canvas` `/business-model-canvas` `/customer-journey-map` `/interview-synthesis` `/pretotype` `/press-release-faq` `/ansoff-matrix` `/pestle-analysis` `/porter-five-forces` `/swot-analysis` `/blue-ocean`

**Phase 2 — Strategic Decisions** (14 skills)
`/business-case` `/business-plan` `/pricing-strategy` `/pricing-model` `/positioning-statement` `/decision-record` `/strategic-bet` `/decision-charter` `/escalation-rule` `/four-risks-check` `/dhm-analysis` `/growth-model` `/bcg-matrix` `/stakeholder-map`

**Phase 3 — Strategic Commitments** (13 skills)
`/product-roadmap` `/roadmap-theme` `/roadmap-item` `/gtm-strategy` `/gtm-brief` `/launch-plan` `/strategy-communication` `/commitment-check` `/prd` `/prd-outline` `/feature-spec` `/user-story` `/prioritize-features`

**Phase 4 — Coordinated Execution** (5 skills)
`/campaign-brief` `/sales-enablement` `/launch-readiness` `/stakeholder-brief` `/competitive-battlecard`

**Phase 5 — Business & Customer Outcomes** (4 skills)
`/onboarding-playbook` `/value-realization-report` `/customer-health-scorecard` `/north-star-metric`

**Phase 6 — Learning & Adaptation** (9 skills)
`/outcome-review` `/retrospective` `/decision-quality-audit` `/relevant-learnings` `/context-save` `/feedback-capture` `/compound` `/product-teardown` `/bias-check`

**Cross-Phase** (15 skills)
`/context-recall` `/feedback-recall` `/interaction-recall` `/portfolio-status` `/portfolio-tradeoff` `/handoff` `/qbr-deck` `/maturity-check` `/pm-level-check` `/phase-check` `/ownership-map` `/customer-value-trace` `/collaboration-check` `/scale-check` `/vision-to-value-document-map`

**Setup & Utility** (4 skills)
`/setup` `/present` `/tour` `/roi-report`

### 21 Strategy Frameworks (New in v3.2)

Built-in implementations of established strategy frameworks, each with full source attribution:

| Skill | Framework | Creator |
|-------|-----------|---------|
| `/porter-five-forces` | Five Forces | Michael Porter (HBR, 1979) |
| `/blue-ocean` | Blue Ocean Strategy | W. Chan Kim & Renee Mauborgne (2005) |
| `/swot-analysis` | SWOT | Albert Humphrey (Stanford Research Institute, 1960s) |
| `/pestle-analysis` | PESTLE | Francis Aguilar (Harvard, 1967) |
| `/business-model-canvas` | Business Model Canvas | Alexander Osterwalder & Yves Pigneur (2010) |
| `/lean-canvas` | Lean Canvas | Ash Maurya (2012) |
| `/ansoff-matrix` | Ansoff Growth Matrix | H. Igor Ansoff (HBR, 1957) |
| `/bcg-matrix` | Growth-Share Matrix | Bruce Henderson / BCG (1970) |
| `/dhm-analysis` | DHM Model | Gibson Biddle (Netflix/Chegg) |
| `/four-risks-check` | Four Big Risks | Marty Cagan / SVPG (2017) |
| `/growth-model` | Growth Loops + Racecar | Brian Balfour / Reforge (2018) |
| `/prioritize-features` | RICE, Kano, MoSCoW, WSJF | Intercom, Noriaki Kano, Dai Clegg |
| `/bias-check` | Cognitive Biases | Daniel Kahneman (2011), Chip & Dan Heath (2013) |
| `/press-release-faq` | Working Backwards / PRFAQ | Jeff Bezos / Amazon (~2004) |
| `/pretotype` | Pretotyping | Alberto Savoia (Google, 2019) |
| `/north-star-metric` | North Star Framework | Sean Ellis / Amplitude (2017) |
| `/product-teardown` | Product Teardown | PM community practice |
| `/stakeholder-map` | Power/Interest Matrix | Aubrey Mendelow (1991) |
| `/interview-synthesis` | Thematic Analysis | Braun & Clarke (2006), Teresa Torres (2021) |
| `/customer-journey-map` | Journey Mapping | Adaptive Path (2007) |
| `/competitive-battlecard` | Battlecards | Klue, Crayon (B2B standard) |

### Document Intelligence

All document-generating skills support three modes:

| Mode | Trigger | Behavior |
|------|---------|----------|
| **Create** | Default, or "create", "new", "draft" | Generate complete new document |
| **Update** | "update", "revise", or file path provided | Find existing doc, update specific sections |
| **Find** | "find", "search", "list" | Search document registry, show matches |

```
/prd authentication                          # CREATE
/prd update the auth PRD with MFA            # UPDATE
/prd find all security-related               # FIND
```

---

## The Vision to Value Framework

Six phases from strategic intent to learning loops. Each phase has specific skills, agents, and exit criteria.

```
Phase 1          Phase 2          Phase 3          Phase 4          Phase 5          Phase 6
Strategic    →   Strategic    →   Strategic    →   Coordinated  →   Business     →   Learning &
Foundation       Decisions        Commitments      Execution        Outcomes         Adaptation
                                                                                        │
└───────────────────────────────────────────────────────────────────────────────────────┘
                                    (feeds back)
```

| Phase | Name | Purpose | Key Transition |
|-------|------|---------|----------------|
| 1 | Strategic Foundation | Market understanding, competitive position | Can articulate target market and vision |
| 2 | Strategic Decisions | Commercial viability, pricing, positioning | Business case approved, pricing defined |
| 3 | Strategic Commitments | Roadmap, GTM, resource allocation | **Point of no return** — resources committed |
| 4 | Coordinated Execution | Launch, campaigns, enablement | Product launched, customers can access |
| 5 | Business Outcomes | Adoption, value realization, health | Outcomes measurable |
| 6 | Learning Loop | Retrospectives, decision audits, learnings | Insights fed back to Phase 1 |

Use `/phase-check [initiative]` to assess which phase you're in.

### 8 Operating Principles

1. **End-to-End Ownership** — Product org accountable from strategy through outcomes
2. **Decision Quality** — Core metric for product leadership effectiveness
3. **Customer Obsession** — Every decision traced to customer value
4. **Strategic Clarity** — Clear bets with explicit assumptions
5. **Outcome Focus** — Success measured by results, not outputs
6. **Collaborative Excellence** — Right people, right inputs, right time
7. **Continuous Learning** — Systematic capture and application of learnings
8. **Scalable Systems** — Processes that work as the organization grows

### Principle Validators

| Skill | Validates | When to Use |
|-------|-----------|-------------|
| `/ownership-map` | End-to-End Ownership | Before major commitments |
| `/customer-value-trace` | Customer Obsession | Before decisions affecting customers |
| `/collaboration-check` | Collaborative Excellence | Cross-functional work |
| `/scale-check` | Scalable Systems | Before committing resources |
| `/phase-check` | V2V Flow | Before phase transitions |

---

## Context Layer — Organizational Memory

The context layer gives agents persistent memory across sessions.

### What Gets Stored

| Type | ID Format | Purpose |
|------|-----------|---------|
| Decisions | `DR-YYYY-NNN` | Strategic choices with rationale, assumptions, re-decision triggers |
| Strategic Bets | `SB-YYYY-NNN` | Bets with explicit assumptions and success criteria |
| Assumptions | `A-NNN` | Testable beliefs extracted from decisions and bets |
| Feedback | `FB-YYYY-NNN` | Customer/market signals with metadata and sentiment |
| Learnings | `L-NNN` | Validated insights from outcomes and retrospectives |
| Documents | `DOC-YYYY-NNN` | All strategic documents produced by skills |
| Interactions | `IX-YYYY-NNNNN` | Agent conversation logs for cross-session continuity |
| Conventions | — | Organizational norms (naming, frameworks, calendar) |

### Key Context Skills

| Skill | Purpose |
|-------|---------|
| `/context-save` | Save a decision, bet, learning, or convention |
| `/context-recall [topic]` | Query past decisions, bets, learnings by topic |
| `/feedback-capture` | Capture customer/market feedback with analysis |
| `/feedback-recall [topic]` | Query past feedback by topic or theme |
| `/interaction-recall [topic]` | Search past agent conversations |
| `/relevant-learnings [topic]` | Surface applicable lessons |
| `/portfolio-status` | View all active strategic bets |
| `/handoff` | Transfer session context when delegating |

### Cross-Reference Graph

Context entries link to each other automatically. When you recall a decision, you also see related bets, feedback, and learnings. The system tracks:
- Decisions ↔ Bets (which decisions support which bets)
- Bets ↔ Assumptions (what must be true for the bet to work)
- Feedback ↔ Decisions (customer signals that inform or challenge decisions)
- Learnings ↔ Decisions (what we learned from past choices)

### Multi-Product Support

For organizations with multiple products, add `product:` filtering:

```
/context-recall pricing product:AXIA
/feedback-recall onboarding product:SKYMOD
/portfolio-status product:AXIA
```

---

## Automatic Context Tracking

Post-agent processing (ROI logging, interaction logging, document registration) is handled automatically by `hooks/os-tracker.py` — a standalone Python CLI with zero dependencies.

**For full setup details, see [`AGENT-INTEGRATION.md`](./AGENT-INTEGRATION.md).**

### What It Does

| When | What | How |
|------|------|-----|
| **Before** agent work | Surfaces related decisions, bets, feedback | `--pre-inject` mode |
| **After** agent work | Logs ROI, interactions, documents | `--hook` or `--agent` mode |
| **On demand** | Health check, index repair | `--diagnose --repair` mode |

### Quick Setup by Platform

**Claude Code**: Automatic — `/setup` configures PostToolUse hooks. Zero manual steps.

**Cursor**: Add to `.cursorrules`:
```
After agent work that produces deliverables, run:
python hooks/os-tracker.py --agent [agent-id] --context-dir ./context
```

**Other agents**: Add equivalent instructions to your system prompt or rules file.

### Organizational Conventions

Define how your org works in `context/preferences/conventions.md`:

```markdown
# Organizational Conventions

## Terminology
- Customer tiers: SMB / Mid-Market / Enterprise
- Pricing tiers: Starter ($29) / Growth ($99) / Scale ($299)

## Processes
- Fiscal year: April 1 - March 31
- Sprint cadence: 2-week sprints, Tuesday start

## Defaults
- Prioritization framework: RICE
- Discovery framework: Jobs-to-be-Done
```

These are automatically included in every agent's context — no keyword matching needed.

---

## 9 Knowledge Packs

Professional frameworks that agents reference when producing deliverables:

| Pack | Key Frameworks |
|------|---------------|
| Prioritization | RICE, ICE, MoSCoW, Kano, Weighted Scoring |
| Pricing | Value-based, Freemium, Usage-based, Van Westendorp |
| Discovery | JTBD, Lean Startup, Continuous Discovery, OSTs |
| Metrics | HEART, North Star, AARRR, OKRs |
| Competitive | Porter's Five Forces, SWOT, Battlecards, Win/Loss |
| GTM Playbooks | PLG, SLG, Channel-led, Launch Tiers |
| Stakeholder Mgmt | Influence Mapping, RACI, Executive Communication |
| User Research | Interviews, Surveys, Usability Testing, A/B Testing |
| Financial Modeling | TAM/SAM/SOM, Unit Economics, LTV/CAC |

---

## Agent Collaboration Patterns

Agents collaborate using four structured patterns:

| Pattern | When | Ownership |
|---------|------|-----------|
| **Consultation** | Need a data point or perspective | Stays with requester |
| **Delegation** | Need specialist to own a sub-deliverable | Transfers to specialist |
| **Review** | Need quality validation | Stays with author |
| **Structured Debate** | Genuine tradeoff with merit on both sides | Senior agent decides |

Agents can also run in **parallel** for faster input gathering:

```
# Portfolio review — all run simultaneously
@bizops financial analysis
@ci competitive update
@value-realization customer outcomes
@prod-ops operational metrics
```

---

## MCP Integrations

Agents auto-detect connected tools and use them when available:

| Category | Examples | What Agents Do |
|----------|----------|----------------|
| Project Management | Jira, Linear, Asana | Create issues from user stories |
| Communication | Slack, Teams | Post launch updates |
| Documents | Notion, Confluence | Publish PRDs to wiki |
| Analytics | Amplitude, Mixpanel | Pull metrics for reviews |
| Repository | GitHub, GitLab | Link specs to issues |

**No MCP? No problem.** Agents fall back to text output with manual action notes. Integrations enhance but never block.

---

## ROI Tracking

Every skill completion shows estimated time saved vs. manual equivalent:

```
⏱️ ~90 min saved in 31s (vs. manual requirements analysis + stakeholder review)
```

- Automatic display after deliverables
- Session totals tracked in `context/roi/session-log.md`
- Historical trends via `/roi-report`
- Baselines for all 103 skills in `hooks/baselines.json`

---

## Example Workflows

### Quick Start — Your First PRD

```
@pm create a PRD for user authentication with SSO support
```

### Strategic Decision with Context

```
/context-recall pricing                    # What did we decide before?
/feedback-recall pricing                   # What are customers saying?
@bizops build a business case for usage-based pricing
/decision-record pricing model change      # Document the decision
/context-save                              # Save to organizational memory
```

### Cross-Functional Launch Planning

```
@product Plan the v2.0 launch. Context: @roadmap.md @customer-feedback/
```
Routes to PM (requirements), PMM (positioning), ProdOps (coordination), with Meeting Mode synthesis.

### Portfolio Review

```
@plt Review portfolio health and recommend resource reallocation. Context: @q2-results.xlsx
```
Convenes CPO, VP Product, Directors for multi-perspective strategic discussion.

---

## Demo Environment

Ships with sample data so you can explore immediately:

- 3 decision records, 2 strategic bets, 7 feedback entries, 1 PRD
- Run `/tour` for a 5-step interactive walkthrough
- Demo data auto-hides once you add your own content
- `/clear-demo` removes demo data when ready

---

## File Reference

| File | Purpose |
|------|---------|
| `PRODUCT-ORG-CLAUDE.md` | Complete skill reference and plugin documentation |
| `AGENT-INTEGRATION.md` | Context tracking setup (hooks, CLI, platform wiring) |
| `agent-guide.md` | This file — top-to-bottom system overview |
| `README.md` | GitHub landing page |
| `rules/` | Behavioral rules for agents |
| `skills/` | Skill definitions (SKILL.md per skill) |
| `reference/knowledge/` | Domain knowledge packs |
| `hooks/os-tracker.py` | Context tracking CLI |
| `hooks/baselines.json` | ROI baselines for all skills/agents |
| `context/` | Organizational memory (created by /setup) |

---

## Cross-Platform Compatibility

| Feature | Claude Code | Cursor | Copilot | Gemini CLI |
|---------|-------------|--------|---------|------------|
| Skills (`/prd`, etc.) | Full | Via Agent Skills | Via Agent Skills | Via Agent Skills |
| Agents (`@pm`, etc.) | Full (Task tool) | Partial | Partial | Partial |
| Gateways (`@product`) | Full (Skill tool) | Limited | Limited | Limited |
| MCP integrations | Full | Full | Expanding | Expanding |
| Context layer | Full | Full | Full | Full |
| Automatic tracking | Full (hooks) | Manual trigger | Manual trigger | Manual trigger |

**Progressive enhancement**: Base features work everywhere. Claude Code gets the fullest experience with automatic hooks and Meeting Mode.

---

## License

MIT — Free and open source. World-class product capabilities shouldn't be locked behind enterprise software.

Based on the Vision to Value Executive Manifesto by Yohay Etsion.
