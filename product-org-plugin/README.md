# Product Org OS

**An entire product organization that becomes your superpower.**

> Intent → Decisions → Commitments → Execution → Outcomes → Learning

110 agents • 346 skills • 18 gateways • 95 knowledge packs • 15 teams • Automatic context tracking • MCP integrations

[**View the Interactive Presentation →**](https://yohayetsion.github.io/product-org-os)

---

## Quick Start

```bash
# Install in Claude Code (primary platform)
claude plugins install github:yohayetsion/product-org-os

# Initialize in your project
/setup

# Start using
@product Launch freemium tier for SMBs. Context: @pricing-research.md
```

> **Cross-platform**: Also compatible with Cursor, GitHub Copilot, Gemini CLI, and other [Agent Skills](https://github.com/anthropics/agent-skills)-standard tools.

> **New here?** Read [`agent-guide.md`](./agent-guide.md) — a complete top-to-bottom guide for any coding agent to understand, install, and operate the system.

---

## Two Invocation Patterns

| Syntax | Purpose | Example |
|--------|---------|---------|
| `@agent` | **Delegate** - spawn autonomous agent | `@pm create a PRD for auth` |
| `/skill` | **Inline** - use template/workflow directly | `/prd` `/decision-record` |

### @product Gateway
Your single entry point. Routes requests to the right agents automatically.
```
@product Launch freemium for SMBs. Context: @pricing-research.md
@product Q2 planning. Inputs: @customer-interviews/ @eng-capacity.md
```

**Response Depth** (`+`/`-` modifiers):
| Modifier | Effect | Example |
|----------|--------|---------|
| `-` | Brief - executive summary | `@product What's launch status? -` |
| *(none)* | Standard - balanced depth | `@product What's launch status?` |
| `+` | Deep - full analysis | `@product What's launch status? +` |

**Meeting Mode**: When you use `@product` or `@plt`, you'll see responses from *individual agents* speaking in their own voice - like walking into a meeting room. You'll see who's engaged, their perspectives, agreements, and tensions. This isn't a monolithic AI response - it's your product org thinking together.

**Multi-Product Organizations**: Filter context by product:
```
/context-recall pricing product:AXIA
/feedback-recall onboarding product:SKYMOD
/portfolio-status product:AXIA
```

### Delegate to Agents (`@agent`)
Spawn autonomous agents to handle tasks. Each agent reasons independently and returns results.
```
@cpo review @board-feedback.pdf and update strategic intent
@pm break down @epic.md into user stories
@plt review @portfolio-health.md - should we pivot?
@bizops analyze @pricing-data.xlsx and create pricing model
```

**Agent Shortcuts:**
| Shortcut | Full Agent | Domain |
|----------|------------|--------|
| `@pm` | `@product-manager` | PRDs, specs, user stories |
| `@plt` | `@product-leadership-team` | Portfolio decisions |
| `@pm-dir` | `@director-product-management` | Roadmap governance |
| `@pmm-dir` | `@director-product-marketing` | GTM strategy |
| `@pmm` | `@product-marketing-manager` | Campaigns, enablement |
| `@ci` | `@competitive-intelligence` | Market analysis |
| `@prod-ops` | `@product-operations` | Launch, process |
| `@mentor` | `@product-mentor` | Career coaching, PM development |

### Use Skills Directly (`/skill`)
Create, update, or find specific deliverables inline.
```
Create a /prd for SSO integration - see @slack-thread.md
Run /competitive-analysis on Acme - @their-demo-notes.md
Update the /roadmap-theme for Growth with mobile initiatives
Find all authentication PRDs using /prd find
```

### Mix Both Patterns
Combine agents and skills naturally.
```
@pm-dir review @launch-data.xlsx and update the /gtm-strategy
@cpo review @board-feedback.pdf and update /strategic-intent
@vp-product review @sales-feedback.md and run /pricing-strategy
```

---

## What's Included

### 110 Agents Across 15 Teams

**Product Org (13 agents)**: CPO, VP Product, Director PM, Director PMM, Product Manager, PMM, Product Mentor, BizOps, BizDev, Competitive Intelligence, Product Operations, Value Realization, UX Lead

**Extension Teams (91 agents across 15 teams)**:

| Team | Agents | Examples |
|------|--------|----------|
| Design | 6 | UI Designer, Visual Designer, User Researcher, Motion Designer |
| Architecture | 6 | Chief Architect, API Architect, Cloud Architect, AI/ML Architect, Security Architect |
| Marketing | 15 | CMO, SEO Specialist, Copywriter, Growth Marketer, Paid Media Manager |
| Finance | 8 | CFO, FP&A Analyst, Revenue Analyst, Tax Planning, Treasury |
| Legal | 7 | General Counsel, Contracts, Privacy, IP, Employment, Compliance |
| Operations | 7 | COO, Program Manager, Project Manager, Risk Manager, Procurement |
| HR / People Ops | 7 | CHRO, Recruiter, Onboarding, Performance, Compensation, People Analytics |
| Customer Success | 6 | CS Director, CSM, Support Lead, KB Specialist, Onboarding CSM, CS Ops |
| Sales Engineering | 6 | Sales Director, Sales Engineer, SDR, Account Exec, Sales Ops, Proposal Writer |
| Data Science | 5 | Data Lead, Data Analyst, BI Engineer, ML Engineer, Experimentation Analyst |
| Dev | 5 | Tech Lead, Frontend Dev, Backend Dev, DevOps, QA Engineer |
| Executive | 1 | CEO |
| Corp Dev | 4 | Head of Corp Dev, M&A Analyst, Strategic Partnerships, Corporate Venture |
| IT Governance | 5 | CIO, IT Director, Data Governance, Enterprise Systems, IT Security Policy |
| Personal Staff | 3 | PA, Analyst, Coach |

**PMTK OS (6 agents)**: Product Planner, Product Marketer, Product Architect, Sales Engineer, MarCom Manager, Director of Products

### 18 Gateways
Product, PLT, PMTK, Design, Architecture, Marketing, Finance, Legal, Operations, Executive, Corp Dev, IT Governance, Personal Staff, Development, HR, Customer Success, Sales, Data Science

### 346 Skills
PRDs, roadmaps, business cases, GTM strategies, pricing models, launch plans, QBR decks, competitive analyses, decision records, ROI tracking, plus 31 strategy frameworks including Porter's Five Forces, Blue Ocean, SWOT, PESTLE, Business Model Canvas, Lean Canvas, Shape Up, Wardley Maps, Seven Powers, Kano Analysis, OKR Writer, and more

### GEO / LLM SEO
`/llm-seo` — optimize brand visibility across ChatGPT, Claude, Gemini, and AI Overviews

### 95 Knowledge Packs
Domain expertise across security, compliance, contracts, SaaS metrics, coaching, cloud architecture, API design, user research, accessibility, email marketing, content strategy, financial modeling, and 80+ more professional domains

### Context Layer
Organizational memory that persists across sessions:
- **Auto-registration**: All skill outputs automatically tracked in `context/documents/`
- **Decisions & Bets**: Strategic choices with assumptions and re-decision triggers
- **Feedback**: Customer and market signals linked to decisions
- **Learnings**: Accumulated wisdom from retrospectives and outcomes
- **Cross-reference graph**: Decisions, bets, feedback, and learnings linked automatically
- **Interaction History**: Full conversation logging across sessions — query with `/interaction-recall [topic]`

Query anytime with `/context-recall [topic]`

### Demo Environment
Ships with pre-populated sample data so you can explore immediately:
- 3 decision records, 2 strategic bets, 7 feedback entries, 1 PRD
- Run `/tour` for a 5-step interactive walkthrough
- **Auto-filtering**: Demo data hides automatically once you add your own content
- Demo coexists safely—use `--include-demo` flag to see it alongside production data
- `/clear-demo` removes demo entirely when ready

### ROI Tracking
Full cost-value transparency after every skill completion:
```
⏱️ ~1.5hrs saved in 31s, 19k tkns ~$0.1 cost, Value ~$150
```
- Time saved, token usage, estimated cost, and dollar value per deliverable
- Per-agent breakdown for multi-agent sessions
- Session totals and historical tracking with `/roi-report`

### Vision to Value Framework
Six phases from strategic intent to learning loop, with skills mapped to each phase

---

## What's New in v3.2

### 4 New Agent Teams (24 Agents)
The system grew from 11 to 15 specialist teams:
- **HR / People Ops** (7 agents) — Recruiting, onboarding, performance management, compensation, people analytics
- **Customer Success** (6 agents) — Account health, support triage, KB content, customer onboarding, CS ops
- **Sales Engineering** (6 agents) — Pipeline management, technical demos, proposals, prospecting, deal management
- **Data Science** (5 agents) — SQL analysis, dashboards, ML models, A/B test analysis, analytics strategy

### 10 New Strategy Frameworks
Shape Up, Wardley Maps, Seven Powers, AARRR/Pirate Metrics, HEART Metrics, OKR Writer, Kano Analysis, Design Sprint, DACI, Pre-mortem — each with full source attribution.

### GEO: AI Search Visibility
New `/llm-seo` skill for Generative Engine Optimization — optimize brand presence across ChatGPT, Claude, Gemini, and Google AI Overviews.

### 95 Knowledge Packs (was 9)
From product-focused packs to full organizational coverage: security, compliance, contracts, SaaS metrics, coaching, cloud architecture, API design, user research, accessibility, email marketing, and 80+ more.

### 31 Strategy Frameworks
The frameworks product leaders reach for daily:

| Skill | Framework | Creator |
|-------|-----------|---------|
| `/porter-five-forces` | Five Forces | Michael Porter (HBR, 1979) |
| `/blue-ocean` | Blue Ocean Strategy | W. Chan Kim & Renée Mauborgne (2005) |
| `/swot-analysis` | SWOT | Albert Humphrey (Stanford Research Institute, 1960s) |
| `/business-model-canvas` | Business Model Canvas | Alexander Osterwalder & Yves Pigneur (2010) |
| `/lean-canvas` | Lean Canvas | Ash Maurya (2012) |
| `/wardley-map` | Wardley Maps | Simon Wardley (2005) |
| `/seven-powers` | Seven Powers | Hamilton Helmer (2016) |
| `/shape-up` | Shape Up | Ryan Singer / Basecamp (2019) |
| `/kano-analysis` | Kano Model | Noriaki Kano (1984) |
| `/okr-writer` | OKRs | Andy Grove / John Doerr |
| `/design-sprint` | Design Sprint | Jake Knapp / Google Ventures (2016) |
| `/daci` | DACI | Intuit decision framework |
| `/pre-mortem` | Pre-mortem | Gary Klein (2007) |
| `/pirate-metrics` | AARRR | Dave McClure (2007) |
| `/heart-metrics` | HEART | Kerry Rodden / Google (2010) |
| `/saas-health-check` | SaaS Metrics | David Skok, Jason Lemkin |
| `/theory-of-constraints` | TOC | Eliyahu Goldratt (1984) |
| ...and 14 more | | |

### Typed Skill Relationships
Agents declare `primary-skills`, `supporting-skills`, `validator-skills`, and `knowledge-packs`. They know exactly which tools to use.

### Automatic Context Tracking
Decisions, deliverables, ROI, conventions — all tracked automatically across sessions.

- `hooks/os-tracker.py` — standalone CLI, zero dependencies
- Claude Code hooks for automatic triggering
- Self-diagnosis + repair when indexes drift
- See [`agent-guide.md`](./agent-guide.md) for full setup across all platforms

## What's in v3.0

### MCP Integrations
Agents auto-detect connected tools (Jira, Slack, Analytics) and use them when available. Graceful fallback to text output.

### Agent Delegation Patterns
Four structured collaboration patterns: Consultation, Delegation, Review, and Structured Debate.

### Cross-Platform via Agent Skills Standard
Works in Claude Code, Cursor, Copilot, Gemini CLI, and expanding.

---

## Use Cases

| Who | What You Get |
|-----|--------------|
| **Solo PM** | Senior-level guidance on every deliverable |
| **Product Team** | Consistent standards, shared memory |
| **Product Org** | Decision frameworks, institutional knowledge |

---

## Documentation

- [**Agent Guide**](./agent-guide.md) - Start here — complete system overview for any coding agent
- [Interactive Presentation](https://yohayetsion.github.io/product-org-os) - Visual overview
- [Full Documentation](./PRODUCT-ORG-CLAUDE.md) - Complete skill reference
- [Context Tracking Setup](./AGENT-INTEGRATION.md) - Hooks, CLI, platform wiring

---

## License

MIT

---

**Free & Open Source.** World-class product capabilities shouldn't be locked behind enterprise software.

Based on the Vision to Value Executive Manifesto by Yohay Etsion.

> Works with Claude Code, Cursor, Copilot, Gemini CLI, and other Agent Skills-compatible tools.
