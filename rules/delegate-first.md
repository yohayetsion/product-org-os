# Delegate-First Protocol (MANDATORY)

Before performing ANY substantive work in a specialist domain, you MUST check if a specialist agent or skill exists across all three systems. **Never act as a generic agent when a specialist is available.**

---

## Pre-Flight Check (NON-NEGOTIABLE)

For EVERY user request that involves product, strategy, marketing, design, architecture, finance, legal, operations, or business work:

1. **Parse** the request for domain keywords
2. **Check** the routing table below (all 3 systems)
3. **Decide spawn-vs-inline** per the table below (`/pbaw <task>` is a full Task-tool spawn of the agents the harness selects — pays full ~15-40k Tier-1 cost per agent; `/persona` is inline, no Audit Block, no cost)
4. **If match found + spawn-shaped** → spawn the selected canonical agent(s) through `/pbaw` with the agent identity protocol from `agent-spawn-protocol.md` §2
5. **If match found + inline-shaped** → adopt the persona inline; do NOT emit an Audit Block
6. **If no match** → proceed as generic Claude (this should be rare)

**Do NOT ask** "Should I route this to an agent?" — just do it. The whole point is automatic delegation.

## Spawn-vs-Inline Decision (NEW — v2 spawn protocol 2026-05-27)

Since the strict-mode v2 protocol removes `lightweight_spawn`, every `/pbaw` Task-tool spawn now pays the full ~15-40k token Tier-1 load. For quick creative or analytical tasks where the full load is overkill, use the inline-persona pattern instead.

| Task shape | Pattern | Example |
|---|---|---|
| Producing a deliverable (PRD, spec, decision, analysis to be saved) | `/pbaw` (spawn) | `/pbaw draft the Q3 strategic bet` → `vp-product` |
| Multi-agent synthesis required | `/pbaw` (spawn; the harness selects the canonical agents, one named senior agent owns synthesis) | `/pbaw launch readiness check for feature X` |
| Quick creative tweak (headline rewrite, caption check, subject-line A/B) | `/persona` (inline) | `/copywriter, sharpen this headline: ...` |
| Quick lookup or persona-flavored answer (no deliverable) | `/persona` (inline) | `/cpo, what's the principle behind X?` |
| Status check on past work | `/persona` (inline) | `/pm-dir, summarize my open commitments` |
| Sensitive-skill draft (legal, HR, compliance — needs full scaffolding) | `/pbaw` (spawn) | `/pbaw review this MSA` → `contracts-counsel` |

**Default**: when in doubt, ask "will the user save this output as a file?" If yes → `/pbaw`. If no → `/persona`.

---

## The Three Systems

### System 1: Product Org OS (Vision to Value methodology)

**When to use**: General product management, strategy, GTM, requirements, roadmapping, portfolio management. This is the default for product work.

**Location**: `.claude/skills/` (no prefix) — loaded as Claude Code skills.

**Agents**: `product-manager`, `vp-product`, `cpo`, `director-product-management`, `director-product-marketing`, `product-marketing-manager`, `bizops`, `bizdev`, `competitive-intelligence`, `product-operations`, `value-realization`

**Entry point**: `/pbaw <task>` — the harness selects the canonical agents (Domain Ownership Map and portfolio roster in `agent-spawn-protocol.md` §6); one named senior agent owns synthesis

**Key routing** (see `skill-awareness.md` for full table):
| Keywords | Route To |
|----------|----------|
| PRD, feature, user story, spec, requirements | `product-manager` |
| Vision, portfolio, pricing strategy, strategic bet | `vp-product` |
| GTM, positioning, messaging, campaign, launch | `director-product-marketing` |
| Competitor, market share, win/loss | `competitive-intelligence` |
| Roadmap, planning, prioritization | `director-product-management` |
| Business case, financial analysis, KPIs | `bizops` |
| Launch readiness, process, tooling | `product-operations` |
| Customer outcomes, adoption, health | `value-realization` |
| Partnerships, ecosystem, channel | `bizdev` |
| User research, design, usability | `ext-design` (team route) |

### System 2: Extension Teams

**When to use**: When work requires specialist domains beyond product management — design, architecture, engineering, marketing execution, finance, legal, operations, executive strategy, corp dev, IT governance, or personal assistance.

**Location**: `.claude/skills/` (agent names, no prefix) + `ext-{team}` for gateways. Source SKILL.md files: `agents/{agent}/SKILL.md`

**Teams & routes**:

| Team | Route (internal) | Leadership | Agent Count |
|------|---------|------------|-------------|
| Design | `ext-design` | 🎨 Dir Design | 6 |
| Architecture | `ext-architecture` | 🏗️ Chief Architect | 6 |
| Marketing | `ext-marketing` | 🎙️ CMO | 15 |
| Finance | `ext-finance` | 💰 CFO | 8 |
| Legal | `ext-legal` | ⚖️ General Counsel | 7 |
| Operations | `ext-operations` | 🏢 COO | 7 |
| Executive | `ext-executive` | 🎯 CEO | 1 |
| Corp Dev | `ext-corpdev` | 🏛️ Head of Corp Dev | 4 |
| IT Governance | `ext-it` | 💻 CIO | 5 |
| Personal Staff | `ext-staff` | 🗂️ PA | 3 |
| Development | `ext-dev` | 🛠️ Tech Lead | 6 |
| HR / People Ops | `ext-hr` | 👥 Chief People Officer | 7 |
| Customer Success | `ext-cs` | 🌟 Director of CS | 6 |

**Key routing** (see `agent-spawn-protocol.md` Section 6 for full table):
| Keywords | Route To |
|----------|----------|
| UI, components, interface, design system | `ui-designer` or `ext-design` |
| API design, system architecture, technical strategy | `chief-architect` or `ext-architecture` |
| Security review, auth, threat modeling | `security-architect` |
| Cloud, deployment, scaling | `cloud-architect` |
| AI/ML architecture, LLM, RAG | `ai-architect` |
| Copywriting, landing pages, messaging | `copywriter` |
| SEO, organic search, keywords | `seo-specialist` |
| Paid ads, media buying, ROAS | `paid-media-manager` |
| Email campaigns, sequences | `email-marketer` |
| Social media, LinkedIn posts, content calendar | `social-media-manager` |
| Financial model, budget, forecast | `ext-finance` (team route) |
| Contract review, vendor agreement | `contracts-counsel` |
| Privacy, GDPR, CCPA | `privacy-counsel` |
| IP, patents, licensing | `ip-counsel` |
| Program management, project planning | `program-manager` |
| M&A, due diligence, acquisition | `ma-analyst` |
| IT governance, COBIT, ITIL | `cio` or `ext-it` |
| Daily briefing, task management, scheduling | `pa` |
| Data analysis, research synthesis | `analyst` |
| Code review, implementation, tech debt | `tech-lead` or `ext-dev` |
| Frontend, React, UI code | `frontend-dev` |
| Backend, API routes, database | `backend-dev` |
| CI/CD, deployment, monitoring | `devops` |
| Build tooling, workflow automation, operational scripts | `automation-engineer` |
| Recruiting, hiring, sourcing, interviews, job descriptions | `recruiter` or `ext-hr` |
| Onboarding (employee), 30/60/90, orientation | `onboarding-specialist` or `ext-hr` |
| Performance review, OKR, feedback cycle, PIP | `performance-specialist` or `ext-hr` |
| Compensation, benefits, equity, salary benchmarking | `compensation-analyst` or `ext-hr` |
| People analytics, attrition, engagement, workforce planning | `people-analyst` or `ext-hr` |
| Customer success, account health, retention (CS) | `csm` or `ext-cs` |
| Support ticket, customer issue, SLA, help desk | `support-lead` or `ext-cs` |
| KB article, help documentation, self-service | `kb-specialist` or `ext-cs` |
| Customer onboarding (implementation), time-to-value | `onboarding-csm` or `ext-cs` |
| Sales pipeline, deal management, quota, territory | `sales-dir` or `ext-sales` |
| Technical demo, POC, RFP response, solution architecture | `sales-engineer` or `ext-sales` |
| Outbound prospecting, cold outreach, lead qualification | `sdr` or `ext-sales` |
| Deal negotiation, closing, enterprise sales cycle | `account-exec` or `ext-sales` |
| Sales forecasting, CRM hygiene, pipeline analytics | `sales-ops` or `ext-sales` |
| Proposal, SOW, pricing presentation | `proposal-writer` or `ext-sales` |
| SQL query, data exploration, ad-hoc analysis | `data-analyst` or `ext-data` |
| Dashboard, BI, visualization, reporting, semantic layer | `bi-engineer` or `ext-data` |
| ML model, feature engineering, model evaluation, MLOps | `ml-engineer` or `ext-data` |
| A/B test analysis, experiment results, statistical significance | `experimentation-analyst` or `ext-data` |
| Analytics strategy, metric trees, North Star metric | `data-lead` or `ext-data` |

---

## Cross-System Collaboration

Some tasks benefit from agents across systems:

| Task | Primary System | Supporting |
|------|---------------|------------|
| Write a PRD and get architecture review | OS (`product-manager`) | Extension (`ext-architecture`) |
| GTM strategy with design assets | OS (`director-product-marketing`) | Extension (`ext-design`, `ext-marketing`) |
| Product roadmap with legal review | OS (`director-product-management`) | Extension (`ext-legal`) |

---

## Self-Check (MANDATORY)

Before EVERY substantive response, ask yourself:

- [ ] Does this request match a domain in the routing tables above?
- [ ] If yes, am I spawning the right specialist?
- [ ] If the user typed `/pbaw <task>` or /skill, am I routing immediately?
- [ ] Am I routing product work through Product Org OS and specialist work through the appropriate Extension Team?

**If you catch yourself writing a PRD, strategy doc, business case, competitive analysis, or any product deliverable without spawning an agent → STOP and route it.**

---

## What DOESN'T Need Delegation

- Simple factual questions ("what's in this file?")
- File operations, git, code editing
- System administration, email management
- Context/feedback recalls (these ARE the lookup)
- Conversation, planning, clarification

---

## Shared Skill Orchestrator Pattern (MANDATORY for Multi-Gateway Skills)

Per Chief Architect recommendation during Phase 3 planning. Applies to any specialist skill consumed by more than one gateway across Product Org OS and Extension Teams.

> *Relocated 2026-08-15 (DR-2026-262): shared-skill orchestrator problem statement (rationale; the binding pattern requirements follow below) — full text in the companion delegate-first.md (sibling of this rules directory; imposes nothing, relaxes nothing).*

### The Pattern

Every specialist skill consumed by more than one gateway MUST have:

1. **One owner** — a single agent identity (e.g., `general-counsel`, `chief-architect`). The owner is accountable for correctness, backwards compatibility, and deprecation decisions. Consumer teams cannot merge changes without owner approval.
2. **Explicit consumer list** — declared in the skill's SKILL.md frontmatter. Any gateway that routes to the skill must be on the list. If a new gateway wants to consume the skill, it must be added explicitly by the owner.
3. **Deprecation rules** — if the skill is split, renamed, or retired, the frontmatter declares the transition, the new target skill(s), and a sunset date. Consumer gateways are notified and given a migration window before the old skill archives.

### Frontmatter Schema

Add these fields to the skill's SKILL.md frontmatter (extending the existing `owner:` field):

```yaml
---
name: risk-analysis
owner: general-counsel                    # single accountable agent (REQUIRED)
consumers:                                # explicit list of gateways/agents that invoke this skill
  - ext-legal
  - product
  - ext-corpdev
sensitive: true                           # see sensitive-skill-guardrails.md
deprecation:                              # optional — only when skill is scheduled for retirement/split
  status: active                          # active | deprecated | split
  successor: null                         # or "/risk-analysis-legal, /risk-analysis-corpdev"
  sunset_date: null                       # or "2026-07-01"
  migration_notes: null                   # or pointer to migration doc
---
```

### When to Use

Trigger conditions — apply this pattern if ANY are true:

- Skill is referenced in two or more gateway routing tables
- Skill is imported by specialists on different Extension Teams
- Skill produces output consumed by agents reporting to different leaders
- Skill's underlying domain knowledge is the territory of one specific specialist but the output is useful to many

> *Relocated 2026-08-15 (DR-2026-262): shared-skill orchestrator worked example (hypothetical /risk-analysis case) — full text in the companion delegate-first.md (sibling of this rules directory; imposes nothing, relaxes nothing).*

### Anti-Patterns (DO NOT)

- **Co-drafting** — two agents both editing the skill with no single accountable owner. If both own it, nobody owns it.
- **Silent dependencies** — a gateway routes to a skill without declaring it in the consumer list. The owner has no visibility into who will break when the skill changes.
- **Unversioned changes** — modifying a multi-consumer skill without a deprecation entry for any breaking change. Breaking changes require a deprecation entry + migration window, not a quiet merge.
- **Fork-and-diverge** — a consumer team copies the skill into their own namespace to avoid the ownership conversation. This is how the three-systems problem compounds.

---

## Operating Principle

> "A specialist with domain context, methodology, and identity will always produce better work than a generic response. The delegate-first protocol ensures the right expert handles every task."
