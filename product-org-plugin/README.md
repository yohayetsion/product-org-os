# Product Org OS

**An entire product organization that becomes your superpower.**

> Intent → Decisions → Commitments → Execution → Outcomes → Learning

13 agents • 103 skills • 2 gateways • 9 knowledge packs • Automatic context tracking • MCP integrations

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

> **Coding agents**: Read [`AGENT-INTEGRATION.md`](./AGENT-INTEGRATION.md) for automatic context tracking setup — hooks, CLI usage, and platform-specific wiring.

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

### 13 Role-Based Agents
CPO, VP Product, Director PM, Director PMM, Product Manager, PMM, Product Mentor, BizOps, BizDev, Competitive Intelligence, Product Operations, Value Realization, UX Lead

### 2 Gateways
Product and Product Leadership Team — route to relevant agents automatically

### 103 Skills
PRDs, roadmaps, business cases, GTM strategies, pricing models, launch plans, QBR decks, competitive analyses, decision records, ROI tracking, Porter's Five Forces, Blue Ocean Strategy, SWOT, PESTLE, Business Model Canvas, Lean Canvas, and more

### 9 Knowledge Packs
Prioritization, Pricing, Discovery, Metrics, Competitive, GTM, Stakeholder Management, User Research, Financial Modeling

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
See time savings after every skill completion:
- Automatic display of estimated time saved
- Session totals and historical tracking
- View dashboard with `/roi-report`

### Vision to Value Framework
Six phases from strategic intent to learning loop, with skills mapped to each phase

---

## What's New in v3.2

### 103 Skills — 21 New Strategy Frameworks
The frameworks product leaders reach for daily, now built in with full source attribution:

| Skill | Framework | Creator |
|-------|-----------|---------|
| `/porter-five-forces` | Five Forces | Michael Porter (HBR, 1979) |
| `/blue-ocean` | Blue Ocean Strategy | W. Chan Kim & Renée Mauborgne (2005) |
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

### Automatic Context Tracking
Agents now remember everything automatically — decisions, deliverables, ROI, conventions. Before spawning an agent, the system surfaces related past decisions and feedback. No manual steps needed.

- `hooks/os-tracker.py` — standalone CLI, zero dependencies
- Claude Code hooks for automatic triggering
- Self-diagnosis + repair when indexes drift
- See `AGENT-INTEGRATION.md` for Cursor, Windsurf, Copilot integration

### Organizational Conventions
Define how your org works once — naming conventions, prioritization frameworks, fiscal calendar — and every agent respects it across every session. Saved in `context/preferences/conventions.md`.

### Strategic Asset Map
`/vision-to-value-document-map` shows exactly where your product strategy has coverage and where it has gaps, across all six Vision to Value phases.

## What's in v3.0

### MCP Integrations
Agents auto-detect connected tools (Jira, Slack, Analytics) and use them when available. No MCP? They fall back gracefully to text output with manual action notes.

### 9 Domain Knowledge Packs
Professional PM frameworks that agents reference when producing deliverables. Covers prioritization, pricing, competitive analysis, and 6 more domains.

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

- [Interactive Presentation](https://yohayetsion.github.io/product-org-os) - Visual overview
- [Full Documentation](./PRODUCT-ORG-CLAUDE.md) - Complete skill reference

---

## License

MIT

---

**Free & Open Source.** World-class product capabilities shouldn't be locked behind enterprise software.

Based on the Vision to Value Executive Manifesto by Yohay Etsion.

> Works with Claude Code, Cursor, Copilot, Gemini CLI, and other Agent Skills-compatible tools.
