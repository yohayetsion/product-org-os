# Product Org OS

A product organization as code. Product Org OS ships a full product team — Chief Product Officer, VP Product, PMs, PMMs, BizOps, specialists — as Claude Code agents, skills, and knowledge packs. Clone it, run `install.py`, invoke `@pm` or `/prd` in any project.

Built on the Vision to Value methodology. ~400 skills across three systems (Product Org OS, Extension Teams, PMTK). Runs in Claude Code.

---

## Quick Start

```bash
git clone https://github.com/yohayetsion/product-org-os.git
cd product-org-os
python install.py
```

New to Claude Code skills? See [Anthropic's skills docs](https://docs.claude.com/en/docs/claude-code/skills).

---

## What's in this repo

| Path | Purpose |
|------|---------|
| `agent-guide.md` | Invocation patterns (`@agent`, `/skill`, gateways) |
| `PRINCIPLES.md` | Vision to Value methodology principles |
| `skills/` | 133 skills — the product-org workflows |
| `rules/` | 20 behavioral rules injected into Claude Code sessions |
| `reference/` | Knowledge packs and templates |
| `install.py` | Portable installer — copies skills into `~/.claude/skills/` |
| `CHANGELOG.md` | Release history |

---

## Two Invocation Patterns

| Syntax | Purpose | Example |
|--------|---------|---------|
| `@agent` | **Delegate** — spawn autonomous agent | `@pm create a PRD for auth` |
| `/skill` | **Inline** — use template/workflow directly | `/prd` `/decision-record` |

### @product Gateway

The single entry point. Routes requests to the right agents automatically.

```
@product Launch freemium for SMBs. Context: @pricing-research.md
@product Q2 planning. Inputs: @customer-interviews/ @eng-capacity.md
```

**Response Depth** (`+`/`-` modifiers):

| Modifier | Effect | Example |
|----------|--------|---------|
| `-` | Brief — executive summary | `@product What's launch status? -` |
| *(none)* | Standard — balanced depth | `@product What's launch status?` |
| `+` | Deep — full analysis | `@product What's launch status? +` |

**Meeting Mode**: `@product` and `@plt` return responses from individual agents speaking in their own voice, with attribution, points of agreement, tension, and synthesis. Not a monolithic AI response — a product org thinking together.

**Multi-Product Organizations**: Filter context by product.

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

## Use Cases

| Who | What You Get |
|-----|--------------|
| **Solo PM** | Senior-level guidance on every deliverable |
| **Product Team** | Consistent standards, shared memory |
| **Product Org** | Decision frameworks, institutional knowledge |

---

## Documentation

- [**Agent Guide**](./agent-guide.md) — complete system overview for any coding agent
- [Interactive Presentation](https://yohayetsion.github.io/product-org-os) — visual overview
- [Full Documentation](./PRODUCT-ORG-CLAUDE.md) — skill reference
- [Context Tracking Setup](./AGENT-INTEGRATION.md) — hooks, CLI, platform wiring

---

## License

MIT

Based on the Vision to Value Executive Manifesto by Yohay Etsion.

---

> *Previously installed as a Claude Code plugin. v4.0.1 repositions as a framework with a portable installer. Previous `claude plugins install` commands no longer apply — use `git clone` + `python install.py` above.*
