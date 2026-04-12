# Product Org OS

**An entire product organization that becomes your superpower.**

> Intent → Decisions → Commitments → Execution → Outcomes → Learning

12 agents • 150+ skills • 38 knowledge packs • Structured metadata • Enforcement-first runtime • MCP integrations

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

### 12 Role-Based Agents
CPO, VP Product, Director PM, Director PMM, Product Manager, PMM, Product Mentor, BizOps, BizDev, Competitive Intelligence, Product Operations, Value Realization

### 2 Gateways
Product and Product Leadership Team — route to relevant agents automatically

### 130+ Skills
PRDs, roadmaps, business cases, GTM strategies, pricing models, launch plans, QBR decks, competitive analyses, decision records, ROI tracking, plus 31 strategy frameworks including Porter's Five Forces, Blue Ocean, SWOT, PESTLE, Business Model Canvas, Lean Canvas, Shape Up, Wardley Maps, Seven Powers, Kano Analysis, OKR Writer, and more. Plus CRO skills, marketing psychology, programmatic SEO, email sequences, and GEO/LLM SEO. Includes 20 cross-domain specialist skills in legal, HR, design, CS, and architecture.

### 10 Knowledge Packs
Prioritization, Pricing, Discovery, Metrics, Competitive, GTM, Stakeholder Management, User Research, Financial Modeling, GEO Playbook

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

## What's New in v4.0

**Agents that know their own job.** v4.0 restructures every agent as a self-describing skill under the Agent Skills Specification standard. Every agent declares what skills it uses, what knowledge it reads, and when — with mandatory enforcement that grounds every response in authoritative sources.

- Every agent declares core and supporting skills with structured `metadata:`
- Three-tier knowledge pack enforcement: always-loaded, conditional, on-demand
- MANDATORY FIRST ACTIONS + Self-Check enforcement sections on all agents
- Mandatory skill invocations with task-type triggers and escape valves
- Vision to Value methodology consolidated into single PRINCIPLES.md
- UX Lead agent retired (full design coverage via @design-dir)
- 20 cross-domain specialist skills added (legal, HR, design, CS, architecture)
- 100% metadata coverage across all 12 agents

[**What's New in v4.0 →**](../whats-new-v4.html)

### Structured Agent Architecture (v4.0)
Every agent declares what skills it uses, what knowledge it reads, and when — with mandatory enforcement. No more agents winging it from training data.

- **`metadata:` schema**: core_skills, supporting_skills, mandatory_skill_invocations, knowledge packs, RACI, delegation patterns — all under the Agent Skills Specification standard
- **Three-tier knowledge enforcement**: always-loaded (Tier 1), conditional (Tier 2), on-demand (Tier 3) — agents consult authoritative sources before producing output
- **MANDATORY FIRST ACTIONS**: blocking reads and skill invocations before substantive work
- **Self-check before output**: every response verified against context loading and skill invocation requirements

> **Upgrading from v3?** No breaking changes to invocation syntax. Deprecated frontmatter fields (`supporting-skills:`, `knowledge-packs:`, `primary-skills:`, `validator-skills:`) migrated automatically to `metadata:`. Install and go.

### Automatic Context Tracking
Decisions, deliverables, ROI, conventions — all tracked automatically across sessions.

- `hooks/os-tracker.py` — standalone CLI, zero dependencies
- Claude Code hooks for automatic triggering
- Self-diagnosis + repair when indexes drift
- See [`agent-guide.md`](./agent-guide.md) for full setup across all platforms

### MCP Integrations
Agents auto-detect connected tools (Jira, Slack, Analytics) and use them when available. Graceful fallback to text output.

### Agent Delegation Patterns
Five structured collaboration patterns: Consultation, Delegation, Review, Structured Debate, and Adversarial Review.

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
