# Product Org Plugin for Claude Code

An AI-powered product organization toolkit providing **69 skills and agents** for product management, strategy, and decision-making based on the **Vision to Value (V2V) System** framework.

## Features

- **`/product` Gateway** - Single entry point that routes to the right owners, collects plans, and orchestrates parallel execution
- **56 Product Skills** - PRDs, roadmaps, business cases, pricing, GTM, and more
- **5 Principle Validators** - Enforce V2V Operating Principles
- **13 Role Agents** - CPO, VP Product, Directors, PMs, and complementary roles with full skill access
- **V2V Phase Tracking** - 6-phase flow with phase prerequisites and transition validation
- **Context Layer** - Persistent organizational memory for decisions, feedback, and learnings
- **Parallel Execution** - Agents can be spawned simultaneously for faster input gathering
- **Feedback System** - Structured capture and analysis of customer/market feedback

## Installation

### Copy Skills to Your Project

Copy the `skills/` folder contents to your project's `.claude/skills/` directory:

```bash
# In your project directory
mkdir -p .claude/skills

# Copy all skills (flat structure - each skill is a folder with SKILL.md)
cp -r /path/to/product-org-plugin/skills/* .claude/skills/
```

**Windows:**
```powershell
mkdir -Force .claude\skills
Copy-Item -Recurse "C:\path\to\product-org-plugin\skills\*" ".claude\skills\"
```

After copying, **restart Claude Code** to discover the new skills.

### Skill Structure

Each skill is a folder containing a `SKILL.md` file:

```
.claude/skills/
├── prd/
│   └── SKILL.md          # /prd command
├── decision-record/
│   └── SKILL.md          # /decision-record command
├── product-manager/
│   └── SKILL.md          # /product-manager agent
└── ...                   # 63 total skills and agents
```

## Quick Start

### 1. Initialize the Plugin

After installation, run the setup skill to create the context folder structure:

```
/setup
```

This creates the `context/` folder in your **current working directory** with all necessary index files.

### 2. Start Using Skills

Try these common skills:

```
/prd [feature name]           # Create a Product Requirements Document
/decision-record [topic]      # Document a decision with rationale
/feedback-capture             # Capture customer feedback
/strategic-bet [initiative]   # Define a strategic bet
```

## Where Files Are Created

After running `/setup`, your project will have:

```
your-project/                  ← Your working directory
├── context/                   ← Created by /setup
│   ├── README.md              # Quick reference
│   ├── decisions/
│   │   └── index.md           # Decision registry
│   ├── bets/
│   │   └── index.md           # Strategic bets
│   ├── assumptions/
│   │   └── registry.md        # Tracked assumptions
│   ├── portfolio/
│   │   └── active-bets.md     # Current portfolio
│   ├── learnings/
│   │   └── index.md           # Accumulated learnings
│   ├── handoffs/
│   │   └── current-session.md # Delegation context
│   └── feedback/
│       ├── index.md           # Feedback registry
│       └── themes.md          # Recurring patterns
└── .claude/
    └── skills/                # Plugin skills (flat structure)
        ├── prd/
        │   └── SKILL.md
        ├── decision-record/
        │   └── SKILL.md
        ├── product-manager/
        │   └── SKILL.md
        └── ...                # 63 total
```

**Important**: The context layer is project-specific. Run `/setup` in each project where you want organizational memory.

## All Skills & Agents (69)

### Gateway (1)

| Skill | Purpose |
|-------|---------|
| `/product` | **Main entry point** - Routes requests to relevant owners, collects plans, gets approval, executes in parallel |

**Example usage:**
```
/product We need to launch a freemium tier for SMBs

→ Analyzes request (V2V Phase 2-3)
→ Identifies owners: @vp-product, @bizops, @director-product-marketing
→ Each proposes a plan
→ You approve (with optional guidance)
→ Executes in parallel
→ Returns synthesized results
```

### Setup & Core (2)

| Skill | Purpose |
|-------|---------|
| `/setup` | Initialize plugin - creates context folders |
| `/present` | Generate HTML presentation from markdown |

### Context Layer (7)

| Skill | Purpose |
|-------|---------|
| `/context-save` | Save decisions, bets, learnings to registry |
| `/context-recall [topic]` | Query past decisions and context |
| `/portfolio-status` | View current strategic bets and health |
| `/handoff` | Capture context for agent delegation |
| `/relevant-learnings [topic]` | Find applicable past learnings |
| `/feedback-capture` | Capture and analyze product feedback |
| `/feedback-recall [topic]` | Query past feedback |

### Documents (10)

| Skill | Purpose |
|-------|---------|
| `/prd` | Full Product Requirements Document |
| `/prd-outline` | PRD outline/structure only |
| `/product-roadmap` | Product roadmap document |
| `/business-case` | Investment business case |
| `/business-plan` | Comprehensive business plan |
| `/gtm-strategy` | Go-to-market strategy document |
| `/pricing-strategy` | Pricing strategy document |
| `/competitive-landscape` | Competitive landscape analysis |
| `/market-analysis` | Market analysis document |
| `/launch-plan` | Product launch plan |
| `/qbr-deck` | Quarterly business review deck |

### V2V Framework (8)

| Skill | Purpose |
|-------|---------|
| `/strategic-intent` | Strategic intent document |
| `/strategy-communication` | Strategy communication package |
| `/campaign-brief` | Marketing campaign brief |
| `/sales-enablement` | Sales enablement materials |
| `/onboarding-playbook` | Customer onboarding playbook |
| `/value-realization-report` | Customer value realization report |
| `/customer-health-scorecard` | Customer health scorecard |
| `/retrospective` | Retrospective facilitation |

### Decisions (3)

| Skill | Purpose |
|-------|---------|
| `/decision-record` | Create decision record with rationale |
| `/decision-charter` | Decision-making charter |
| `/escalation-rule` | Escalation rule definition |

### Strategy (3)

| Skill | Purpose |
|-------|---------|
| `/strategic-bet` | Define strategic bet with assumptions |
| `/commitment-check` | Evaluate readiness for commitment |
| `/portfolio-tradeoff` | Analyze portfolio tradeoffs |

### Assets (8)

| Skill | Purpose |
|-------|---------|
| `/vision-statement` | Product vision statement |
| `/roadmap-theme` | Roadmap theme definition |
| `/roadmap-item` | Individual roadmap item |
| `/gtm-brief` | GTM brief (shorter than strategy) |
| `/pricing-model` | Pricing model definition |
| `/positioning-statement` | Market positioning statement |
| `/competitive-analysis` | Single competitor analysis |
| `/market-segment` | Market segment definition |

### Requirements (3)

| Skill | Purpose |
|-------|---------|
| `/feature-spec` | Feature specification |
| `/user-story` | User story with acceptance criteria |
| `/prd-outline` | PRD structure outline |

### Operations (3)

| Skill | Purpose |
|-------|---------|
| `/launch-readiness` | Launch readiness checklist |
| `/stakeholder-brief` | Stakeholder briefing document |
| `/outcome-review` | Outcome review (post-launch) |

### Assessment (3)

| Skill | Purpose |
|-------|---------|
| `/maturity-check` | Product org maturity assessment |
| `/pm-level-check` | PM competency level assessment |
| `/decision-quality-audit` | Decision quality audit |

### Principle Validators (5)

| Skill | Principle | Purpose |
|-------|-----------|---------|
| `/ownership-map` | #1 End-to-End Ownership | Map accountability across V2V phases |
| `/customer-value-trace` | #3 Customer Obsession | Validate decisions trace to customer value |
| `/collaboration-check` | #6 Collaborative Excellence | Validate RACI and stakeholder consultation |
| `/scale-check` | #8 Scalable Systems | Assess scalability at 2x, 10x, 100x |
| `/phase-check` | V2V Flow | Assess which V2V phase an initiative is in |

### Role Agents (13)

Invoke agents to delegate tasks to specialized product org roles:

#### Core Product Roles (6)

| Agent | Purpose |
|-------|---------|
| `/cpo` | Chief Product Officer - executive strategy, org design |
| `/vp-product` | VP of Product - vision, roadmap accountability, pricing |
| `/director-product-management` | Director PM - roadmap governance, team coordination |
| `/director-product-marketing` | Director PMM - GTM strategy, positioning, launches |
| `/product-manager` | PM - feature specs, user stories, delivery planning |
| `/product-marketing-manager` | PMM - campaigns, collateral, sales enablement |

#### Complementary Roles (6)

| Agent | Purpose |
|-------|---------|
| `/ux-lead` | UX Lead - user research, design specs, usability |
| `/bizops` | BizOps - business cases, financial analysis, KPIs |
| `/bizdev` | BizDev - partnerships, market expansion, deals |
| `/competitive-intelligence` | CI - competitor analysis, win/loss, trends |
| `/product-operations` | ProdOps - processes, tooling, cross-team facilitation |
| `/value-realization` | Value - success metrics, ROI, adoption tracking |

#### Leadership (1)

| Agent | Purpose |
|-------|---------|
| `/product-leadership-team` | PLT - portfolio tradeoffs, cross-functional decisions |

## Context Layer

The plugin includes organizational memory that persists across sessions:

### How It Works

1. **After decisions**: `/context-save` extracts key info to registry
2. **Before new work**: `/context-recall` finds related past context
3. **For feedback**: `/feedback-capture` documents with full analysis
4. **After outcomes**: Reviews update assumptions and extract learnings

### Example: Making a Decision

```
1. /context-recall pricing        # Check past decisions
2. /feedback-recall pricing       # See customer feedback
3. /decision-record pricing model # Create the decision
4. /context-save                  # Save to registry
```

### Example: Capturing Feedback

```
User: "Customer says: Your API limits are too restrictive."

/feedback-capture
→ Records source, date, channel
→ Analyzes sentiment, impact, urgency
→ Links to related decisions/bets
→ Identifies patterns/themes
```

## V2V System Flow

The Vision to Value System is a 6-phase framework:

| Phase | Name | Key Activities | Key Skills |
|-------|------|----------------|------------|
| 1 | Strategic Foundation | Research, vision, market analysis | vision-statement, market-analysis |
| 2 | Strategic Decisions | Business case, pricing, bets | business-case, strategic-bet |
| 3 | Strategic Commitments | Roadmap, GTM, requirements | product-roadmap, gtm-strategy, prd |
| 4 | Coordinated Execution | Launch, campaigns, sales | launch-readiness, campaign-brief |
| 5 | Business Outcomes | Value realization, health | value-realization-report |
| 6 | Learning Loop | Reviews, learnings, audits | outcome-review, context-save |

Use `/phase-check [initiative]` to assess which phase an initiative is in.
Use `/commitment-check [initiative]` to validate readiness before Phase 3 commitments.

## Parallel Execution

Agents can be spawned in parallel for faster input gathering:

```
# Portfolio Review - spawn these in parallel
@bizops, @competitive-intelligence, @value-realization, @product-operations

# Launch Decision - spawn these in parallel
@product-manager, @product-marketing-manager, @product-operations
```

All 13 agents have access to all 55 skills and include:
- Primary skills for their role
- Supporting cross-functional skills
- Principle validators
- Required pre-work checklists

## Documentation

See [PRODUCT-ORG-CLAUDE.md](./PRODUCT-ORG-CLAUDE.md) for complete documentation including:
- Detailed skill reference with usage examples
- Context layer architecture
- ID conventions
- Workflow patterns

## Requirements

- [Claude Code](https://claude.ai/code) CLI
- Write access to your project directory

## License

MIT License

## Author

**Yohay Etsion** - Author of "Vision to Value" and "Leading the Charge"

---

*Built with the Vision to Value framework for world-class product organizations.*
