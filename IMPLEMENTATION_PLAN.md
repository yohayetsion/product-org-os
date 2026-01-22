# Claude Code Product Organization Configuration Package

> **⚠️ HISTORICAL DOCUMENT**
>
> This implementation plan documents the original design and v1.0-v2.0 implementation phases.
> The plugin has evolved significantly and is now at **v2.2.0**.
>
> **For current documentation, see:**
> - `product-org-plugin/README.md` - User documentation
> - `product-org-plugin/PRODUCT-ORG-CLAUDE.md` - Technical reference
> - `product-org-plugin/POOv3.md` - v2.2.0 release summary
>
> **Key changes since this plan:**
> - 41 skills → 56 skills (+15 new skills)
> - Added `/product` gateway as single entry point
> - Added 5 principle validator skills
> - Added 7 context layer skills (including feedback system)
> - All 13 agents now have full skill access
> - V2V phase markers added to all skills
> - Parallel execution patterns implemented
>
> **Last updated**: January 2026

---

## Executive Summary

A portable, self-contained Claude Code **plugin** that enables product organizations to work with AI agents representing their actual org structure. Users install this plugin once and gain access to role-based agents (CPO, VP Product, Director PM, PM, PMM, etc.) who understand their responsibilities, deliverables, processes, and can delegate work to other role agents when appropriate.

**Distribution**: GitHub repository (`github.com/yohay/product-org-plugin`) + Claude Code Plugin Registry

---

## The V2V System Flow

The plugin is structured around the **Vision to Value (V2V) System** - a 6-phase flow that transforms strategic intent into business outcomes:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  1. STRATEGIC FOUNDATION (Input Phase)                              │   │
│  │     • Strategic Intent                                              │   │
│  │     • Market, Competitive & Business Analysis                       │   │
│  │     • Product Mission & Vision                                      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    ↓                                        │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  2. STRATEGIC DECISIONS ("Commercial Filter")                       │   │
│  │     • Business Cases & Financial Analyses                           │   │
│  │     • Pricing & Packaging Strategy                                  │   │
│  │     • Messaging & Positioning Strategy                              │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    ↓                                        │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  3. STRATEGIC COMMITMENTS ("Point of No Return")                    │   │
│  │     • Roadmap Elaboration & Prioritization                          │   │
│  │     • GTM Establishment                                             │   │
│  │     • Strategy Communication                                        │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    ↓                                        │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  4. COORDINATED EXECUTION (The "Doing" Phase)                       │   │
│  │     • Product Development Execution                                 │   │
│  │     • Marketing Activities & Campaigns                              │   │
│  │     • Sales Process Participation                                   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    ↓                                        │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  5. BUSINESS & CUSTOMER OUTCOMES (Output Phase)                     │   │
│  │     • Customer Onboarding                                           │   │
│  │     • Value Realization                                             │   │
│  │     • Buyer/User Behavior                                           │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    ↓                                        │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  6. LEARNING & ADAPTATION LOOP (System's "Brain")                   │   │
│  │     • Outcome Reviews                                               │   │
│  │     • Decision Quality Audits                                       │   │
│  │     • Process Improvements                                          │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    ↑                                        │
│                          (Feeds back to Phase 1)                            │
│                                                                             │
│  ╔═══════════════════════╗              ╔═════════════════════════════╗    │
│  ║  OPERATING PRINCIPLES ║              ║  ORGANIZATIONAL STRUCTURE   ║    │
│  ║  Focus: Decision      ║              ║  Focus: Decision durability ║    │
│  ║  quality under        ║              ║  over time.                 ║    │
│  ║  pressure.            ║              ║  "Who supports the What"    ║    │
│  ║  "Cultural Guardrails"║              ║                             ║    │
│  ╚═══════════════════════╝              ╚═════════════════════════════╝    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Skills Organized by V2V Phase

| Phase | Skills | Primary Agents |
|-------|--------|----------------|
| **1. Strategic Foundation** | `/strategic-intent`, `/market-analysis`, `/competitive-landscape`, `/vision-statement` | CPO, VP Product, CI |
| **2. Strategic Decisions** | `/business-case`, `/pricing-strategy`, `/positioning-statement`, `/decision-record` | BizOps, VP Product, Director PMM |
| **3. Strategic Commitments** | `/product-roadmap`, `/gtm-strategy`, `/strategy-communication`, `/commitment-check` | Director PM, Director PMM, CPO |
| **4. Coordinated Execution** | `/prd`, `/feature-spec`, `/launch-plan`, `/campaign-brief`, `/sales-enablement` | PM, PMM, Product Ops |
| **5. Business Outcomes** | `/onboarding-playbook`, `/value-realization-report`, `/customer-health-scorecard` | Value Realization, CS |
| **6. Learning Loop** | `/outcome-review`, `/decision-quality-audit`, `/maturity-check`, `/retrospective` | PLT, BizOps |

---

## Distribution Strategy: GitHub + Claude Code Plugin

### Why Plugin Format?

The Claude Code Plugin system is the native, recommended way to distribute reusable configurations:
- **Simple installation**: Symlink or copy to `~/.claude/plugins/` directory
- **Automatic discovery**: Claude Code automatically loads plugins from the plugins directory on startup
- **Proper scoping**: Plugin agents, skills, and rules are automatically loaded
- **Development-friendly**: Symlink allows live updates during development
- **Shareable**: Can be published to the Claude Code Plugin Marketplace

### Plugin Structure

```
product-org-plugin/
├── .claude-plugin/
│   └── plugin.json                     # Plugin manifest (required)
├── README.md                           # Documentation
├── PRODUCT-ORG-CLAUDE.md              # Context file loaded by plugin
│
├── agents/                             # All 13 role-based agents
│   └── [agent folders]
│
├── skills/                             # All 23 skills
│   └── [skill folders]
│
├── rules/                              # Path-based rules
│   └── [rule files]
│
├── templates/                          # Document templates
│   └── [template files]
│
├── presentations/                      # HTML presentation templates
│   ├── base-template.html             # Base reveal.js template
│   ├── styles/
│   │   └── product-org-theme.css      # Branded presentation theme
│   └── assets/
│       └── [logos, icons]
│
├── reference/                          # Framework reference docs
│   └── [reference files]
│
└── .mcp.json                          # Optional MCP server configs
```

### plugin.json Manifest

```json
{
  "name": "product-org",
  "version": "1.0.0",
  "description": "Product Organization agents, skills, and workflows based on Vision to Value framework",
  "author": "Yohay Etsion",
  "homepage": "https://github.com/[repo]",
  "keywords": ["product-management", "product-org", "vision-to-value"],

  "agents": {
    "include": ["agents/**/*.md"]
  },

  "skills": {
    "include": ["skills/**/*.md"]
  },

  "rules": {
    "include": ["rules/*.md"]
  },

  "context": {
    "files": ["PRODUCT-ORG-CLAUDE.md"]
  }
}
```

### Installation Options

**Option 1: Local Development (Recommended for Testing)**

Create a symlink from your development folder to Claude's plugins directory:

**Windows (PowerShell as Administrator):**
```powershell
New-Item -ItemType SymbolicLink `
  -Path "$env:USERPROFILE\.claude\plugins\product-org" `
  -Target "C:\path\to\product-org-plugin"
```

**macOS/Linux:**
```bash
ln -s /path/to/product-org-plugin ~/.claude/plugins/product-org
```

**Option 2: Direct Folder Placement**
```bash
cp -r ./product-org-plugin ~/.claude/plugins/product-org
```

**Option 3: From Plugin Marketplace (once published)**

Within Claude Code, use:
```
/plugin install product-org@marketplace-name
```

### After Installation

Restart Claude Code. The plugin is automatically discovered from `~/.claude/plugins/`.

Users immediately have access to:
- All 13 role-based agents (`@cpo`, `@product-manager`, etc.)
- All 23 skills (`/decision-record`, `/gtm-brief`, etc.)
- All rules automatically applied to matching paths
- Templates and reference docs

---

## Connecting Agents to Business Context

Agents work with **your organization's actual documents** via Claude Code's `@file` syntax.

### The Pattern

```
@[agent] [task description].
  See @[path/to/context-doc-1.md] for [what it provides]
  and @[path/to/context-doc-2.md] for [what it provides].
```

### How Agents Process References

1. **Read** each referenced document
2. **Extract** task-relevant context (priorities, constraints, findings, criteria)
3. **Synthesize** across documents
4. **Produce** context-aware deliverables
5. **Cite** sources when incorporating content

### Document Types and Value

| Document Type | What Agents Extract |
|---------------|---------------------|
| Strategy docs | Priorities, bets, constraints |
| Research docs | User needs, pain points, quotes |
| Decision records | Criteria, rationale |
| Competitive analysis | Positioning, gaps, threats |
| Financial docs | Budgets, ROI thresholds |
| Technical docs | Constraints, architecture |

### Example Usage with Document References

```
@product-manager Create a feature spec for user onboarding.
  See @research/onboarding-friction-study.md for user pain points
  and @engineering/auth-system-overview.md for technical constraints.
```

```
@director-product-marketing Develop GTM brief for Q2 launch.
  Positioning: @strategy/differentiation-strategy.md
  Competitive: @competitive/q1-market-analysis.md
  Segments: @gtm/segment-prioritization.md
```

```
@bizops Prepare business case for enterprise tier expansion.
  Market: @competitive/enterprise-market-sizing.md
  Criteria: @finance/investment-hurdle-rates.md
  Costs: @engineering/enterprise-scaling-estimate.md
```

---

## Deliverable Outputs: Markdown + HTML Presentations

### Dual Output Philosophy

Every meaningful deliverable created by an agent produces **two outputs**:
1. **Markdown document** - For version control, collaboration, and editing
2. **HTML presentation** - For stakeholder communication, meetings, and sharing

### How It Works

When an agent creates a deliverable (via a skill or directly), it:
1. Creates the markdown document in the appropriate location
2. Automatically generates an HTML presentation version using the `/present` skill
3. Saves both files with matching names (e.g., `gtm-brief-q2-launch.md` and `gtm-brief-q2-launch.html`)

### Presentation Skill: `/present`

A core skill that converts any deliverable to an HTML presentation:

```yaml
---
name: present
description: Convert a deliverable document to an HTML presentation
argument-hint: [document-path]
---

Convert the specified document into an HTML presentation.

Input: Path to markdown document
Output: HTML presentation file using reveal.js

Presentation structure:
1. Title slide with document name and date
2. Executive summary (if present)
3. Key sections as individual slides
4. Tables converted to clean slide format
5. Metrics/KPIs as visual cards
6. Conclusions/recommendations as summary slide

Style: Professional, clean, suitable for executive audiences
```

### Agent Prompt Addition

Each agent includes this instruction:

```
## Output Format

For every meaningful deliverable you create:
1. Create the markdown document
2. Use the /present skill to generate an HTML presentation
3. Save both files with the same base name

Example:
- Created: strategy/bets/smb-expansion.md
- Also created: strategy/bets/smb-expansion.html (presentation)

This ensures stakeholders can immediately use the deliverable in meetings.
```

### Deliverables That Get Presentations

| Deliverable Type | Presentation Created? |
|------------------|----------------------|
| Strategic Bet | Yes |
| Decision Record | Yes |
| Decision Charter | Yes |
| Product Vision | Yes |
| Roadmap Theme | Yes |
| GTM Brief | Yes |
| Pricing Model | Yes |
| Competitive Analysis | Yes |
| Launch Readiness | Yes |
| Outcome Review | Yes |
| Feature Spec | Optional (on request) |
| User Story | No |
| Maturity Assessment | Yes |

### HTML Presentation Template

Base template using reveal.js for professional, **responsive presentations** (desktop + mobile):

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{title}}</title>

    <!-- Reveal.js Core -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4/dist/reveal.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4/dist/theme/white.css">

    <!-- Custom Responsive Theme -->
    <link rel="stylesheet" href="product-org-theme.css">

    <style>
        /* Responsive Typography */
        .reveal h1 { font-size: clamp(1.5rem, 5vw, 2.5rem); }
        .reveal h2 { font-size: clamp(1.2rem, 4vw, 2rem); }
        .reveal p, .reveal li { font-size: clamp(0.9rem, 2.5vw, 1.2rem); }

        /* Mobile-Friendly Tables */
        .reveal table {
            font-size: clamp(0.7rem, 2vw, 1rem);
            width: 100%;
        }

        /* Responsive Slides */
        @media screen and (max-width: 768px) {
            .reveal .slides section {
                padding: 10px;
            }
            .reveal table { display: block; overflow-x: auto; }
            .reveal .metrics-grid { grid-template-columns: 1fr; }
        }

        /* Desktop Optimizations */
        @media screen and (min-width: 769px) {
            .reveal .slides section { padding: 40px; }
            .reveal .metrics-grid {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 20px;
            }
        }

        /* Metric Cards */
        .metric-card {
            background: linear-gradient(135deg, #f5f7fa 0%, #e4e8ec 100%);
            border-radius: 12px;
            padding: 20px;
            text-align: center;
        }
        .metric-value {
            font-size: clamp(2rem, 6vw, 3rem);
            font-weight: bold;
            color: #2c5aa0;
        }
        .metric-label {
            font-size: clamp(0.8rem, 2vw, 1rem);
            color: #666;
        }

        /* Status Indicators */
        .status-green { color: #28a745; }
        .status-yellow { color: #ffc107; }
        .status-red { color: #dc3545; }

        /* Touch-Friendly Navigation */
        @media (pointer: coarse) {
            .reveal .controls { transform: scale(1.5); }
        }
    </style>
</head>
<body>
    <div class="reveal">
        <div class="slides">
            <!-- Title Slide -->
            <section>
                <h1>{{title}}</h1>
                <p>{{subtitle}}</p>
                <p class="meta">{{date}} | {{owner}}</p>
            </section>

            <!-- Content slides generated from markdown -->
            {{content_slides}}

            <!-- Summary/Next Steps -->
            <section>
                <h2>Summary & Next Steps</h2>
                {{summary}}
            </section>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/reveal.js@4/dist/reveal.js"></script>
    <script>
        Reveal.initialize({
            // Responsive settings
            width: '100%',
            height: '100%',
            margin: 0.1,
            minScale: 0.2,
            maxScale: 2.0,

            // Touch/mobile support
            touch: true,

            // Navigation
            controls: true,
            progress: true,
            hash: true,

            // Presentation features
            transition: 'slide',
            backgroundTransition: 'fade'
        });
    </script>
</body>
</html>
```

### Responsive Design Features

| Feature | Desktop | Mobile/Tablet |
|---------|---------|---------------|
| Typography | Full-size headings and text | Scaled using `clamp()` for readability |
| Tables | Full display | Horizontal scroll enabled |
| Metric cards | 3-column grid | Single column stack |
| Navigation | Mouse/keyboard | Touch gestures + larger controls |
| Slide padding | 40px | 10px |
| Charts/visuals | Full size | Responsive scaling |

### Presentation Output Quality

Every HTML presentation includes:
- **Print-ready CSS** for PDF export
- **High contrast mode** for accessibility
- **Dark mode support** (auto-detects system preference)
- **Offline capable** (CDN assets cached locally)
- **Share-friendly URLs** (hash-based navigation)

### Example: GTM Brief Presentation Output

When `@director-product-marketing` creates a GTM brief:

**Markdown output** (`gtm/q2-launch-brief.md`):
```markdown
# Go-to-Market Brief: Q2 Product Launch

**Product/Feature**: AI Assistant v2.0
**Launch Date**: April 15, 2025
...
```

**HTML presentation output** (`gtm/q2-launch-brief.html`):
- Slide 1: Title + Launch Date
- Slide 2: Target Market & Personas
- Slide 3: Positioning & Value Prop
- Slide 4: Key Messages
- Slide 5: Pricing Strategy
- Slide 6: Sales Motion
- Slide 7: Launch Timeline
- Slide 8: Success Metrics
- Slide 9: Summary & Next Steps

---

## Design Philosophy

### Role-Based, Not Function-Based
Agents represent actual product org roles, not abstract functions. Each agent embodies:
- What they're accountable/responsible for (from RACI matrix)
- What deliverables they own
- What processes they execute
- How they collaborate with other roles
- Their maturity expectations at different org levels
- Which other agents they should delegate to or consult

### Agent-to-Agent Collaboration
Agents can invoke other agents through the Task tool, enabling realistic product org workflows:
- A CPO agent can delegate roadmap elaboration to Director PM
- A Director PMM agent can request competitive analysis from CI agent
- A Product Leadership Team agent can coordinate work across multiple role agents

### Portable Package
Self-contained configuration folder (`.claude-product-org/`) that can be copied to any repository without modification.

### Task-Driven Execution
Agents receive tasks and execute them using:
- Appropriate processes from the frameworks
- Templates for standard deliverables
- Skills (slash commands) for common patterns
- Delegation to other agents when work falls outside their RACI scope

---

## Source Frameworks

| Source | Content | Used For |
|--------|---------|----------|
| **Vision to Value** (V2V) | 8 Operating Principles, Decision Systems, Strategic Process, Decision Interface Charters, Toolkits | Agent decision-making behavior, quality standards |
| **Leading the Charge** (LTC) | Detailed processes (6-step Roadmapping, 11-step GTM, Market Analysis, Pricing, etc.) | Process execution within agents |
| **Product Org Blueprints** | Asset Blueprint (10 assets), Structure Blueprint (RACI), Maturity Blueprint (4 levels), PM Career Blueprint | Role definitions, accountability, maturity context |

---

## Role-Based Agents (13 Total)

### Core Roles (6 agents)

#### 1. CPO / Chief Product Officer (`cpo`)

**RACI Responsibilities**:
- **Accountable**: Product Vision & Roadmap, Pricing Strategy, Stakeholder Intimacy
- **Consulted**: Product Requirements, Business Plan, Go to Market

**Key Deliverables**:
- Product organization strategy and structure
- Vision alignment with company strategy
- Pricing strategy approval
- PLT leadership and coordination
- Executive stakeholder management

**Processes**:
- Strategic planning and portfolio prioritization
- Organization design and scaling decisions
- Executive communication and board materials

**Collaboration Pattern**:
- Delegates roadmap elaboration to `director-product-management`
- Delegates GTM strategy to `director-product-marketing`
- Delegates business planning to `bizops`
- Convenes `product-leadership-team` for portfolio decisions

**Handling Document References**:

When users reference documents using `@file` syntax:

1. **Recognize** all `@path/to/document.md` references
2. **Read** each referenced document using the Read tool
3. **Extract** relevant context:
   - Strategy docs: priorities, constraints, success criteria
   - Research docs: findings, user quotes, data points
   - Decision docs: criteria, options, rationale
   - Competitive docs: positioning, gaps, market dynamics
   - Financial docs: budgets, targets, thresholds
4. **Synthesize** insights across multiple documents
5. **Produce** deliverables that reflect the specific context
6. **Cite** source documents when incorporating their content

**Agent Invocation Behavior**:
```
When given a task that requires roadmap details:
  → Invoke @director-product-management with specific roadmap request

When given a task that requires GTM strategy:
  → Invoke @director-product-marketing with GTM brief request

When given a task that requires portfolio tradeoffs:
  → Invoke @product-leadership-team with tradeoff decision framing
```

---

#### 2. VP Product (`vp-product`)

**RACI Responsibilities**:
- **Accountable**: Product Vision & Roadmap, Pricing Strategy, Stakeholder Intimacy
- **Consulted**: Product Requirements, Business Plan, Go to Market

**Key Deliverables**:
- Product vision documents
- Roadmap accountability and communication
- Pricing strategy development
- Stakeholder relationship management
- Team leadership and development

**Processes**:
- Vision creation (from LTC: Building a Product Vision)
- Roadmap governance
- Pricing strategy development (from LTC: Product Pricing)
- Stakeholder management cadences

**Collaboration Pattern**:
- Works with `director-product-management` on roadmap execution
- Partners with `director-product-marketing` on positioning
- Coordinates with `bizops` on business metrics
- Consults `competitive-intelligence` for market insights

**Handling Document References**:

When users reference documents using `@file` syntax:

1. **Recognize** all `@path/to/document.md` references
2. **Read** each referenced document using the Read tool
3. **Extract** relevant context:
   - Strategy docs: priorities, constraints, success criteria
   - Research docs: findings, user quotes, data points
   - Decision docs: criteria, options, rationale
   - Competitive docs: positioning, gaps, market dynamics
   - Financial docs: budgets, targets, thresholds
4. **Synthesize** insights across multiple documents
5. **Produce** deliverables that reflect the specific context
6. **Cite** source documents when incorporating their content

**Agent Invocation Behavior**:
```
When given a vision creation task:
  → May invoke @competitive-intelligence for market context
  → May invoke @director-product-marketing for positioning input

When given a pricing task:
  → Invoke @competitive-intelligence for competitive pricing data
  → Invoke @bizops for financial modeling
```

---

#### 3. Director of Product Management (`director-product-management`)

**RACI Responsibilities**:
- **Responsible**: Product Vision & Roadmap, Product Delivery Planning, Pricing Strategy, Market & Customer Intimacy, Organizational Processes, Stakeholder Intimacy
- **Accountable**: Product Requirements

**Key Deliverables**:
- Roadmap documents and presentations
- Requirements governance and standards
- Delivery planning oversight
- Team coaching and development
- Cross-functional alignment

**Processes**:
- 6-Step Roadmapping Process (from LTC)
- Requirements prioritization framework
- Delivery planning and tracking
- Team performance management

**Collaboration Pattern**:
- Directs `product-manager` agents on specific product areas
- Partners with `product-operations` on processes and tooling
- Coordinates with `director-product-marketing` on launch alignment
- Works with `ux-lead` on user research priorities

**Handling Document References**:

When users reference documents using `@file` syntax:

1. **Recognize** all `@path/to/document.md` references
2. **Read** each referenced document using the Read tool
3. **Extract** relevant context:
   - Strategy docs: priorities, constraints, success criteria
   - Research docs: findings, user quotes, data points
   - Decision docs: criteria, options, rationale
   - Competitive docs: positioning, gaps, market dynamics
   - Financial docs: budgets, targets, thresholds
4. **Synthesize** insights across multiple documents
5. **Produce** deliverables that reflect the specific context
6. **Cite** source documents when incorporating their content

**Agent Invocation Behavior**:
```
When given a roadmap creation task:
  → May invoke @product-manager for specific product area inputs
  → May invoke @ux-lead for user research insights
  → May invoke @competitive-intelligence for market context

When given a requirements governance task:
  → Invoke @product-manager for specific requirement elaboration
  → Invoke @ux-lead for UX requirements
```

---

#### 4. Product Manager (`product-manager`)

**RACI Responsibilities**:
- **Responsible**: Product Delivery Planning, Product Requirements, Organizational Processes
- **Consulted**: Product Vision & Roadmap, Pricing Strategy

**Key Deliverables**:
- Feature definitions (buyers, users, solved challenges, use cases)
- Elaborated user stories
- Product version planning
- Buy/build decision inputs
- Delivery plan execution

**Processes**:
- Requirements definition (from LTC: Product Requirements)
- Backlog prioritization
- Delivery planning and tracking
- Sprint/iteration management
- Stakeholder coordination

**Collaboration Pattern**:
- Reports to `director-product-management` on roadmap progress
- Partners with `ux-lead` on user research and design
- Works with Engineering on feasibility and delivery
- Coordinates with `product-marketing-manager` on feature positioning

**Handling Document References**:

When users reference documents using `@file` syntax:

1. **Recognize** all `@path/to/document.md` references
2. **Read** each referenced document using the Read tool
3. **Extract** relevant context:
   - Strategy docs: priorities, constraints, success criteria
   - Research docs: findings, user quotes, data points
   - Decision docs: criteria, options, rationale
   - Competitive docs: positioning, gaps, market dynamics
   - Financial docs: budgets, targets, thresholds
4. **Synthesize** insights across multiple documents
5. **Produce** deliverables that reflect the specific context
6. **Cite** source documents when incorporating their content

**Agent Invocation Behavior**:
```
When given a feature spec task:
  → May invoke @ux-lead for user research and design input
  → May invoke @product-marketing-manager for positioning input

When given a delivery planning task:
  → Invoke @product-operations for process and tooling support
```

---

#### 5. Director of Product Marketing (`director-product-marketing`)

**RACI Responsibilities**:
- **Responsible**: Business Plan, Go to Market, Market & Customer Intimacy, Organizational Processes, Stakeholder Intimacy
- **Consulted**: Product Vision & Roadmap, Pricing Strategy

**Key Deliverables**:
- Go-to-market strategy and plans
- Positioning and messaging frameworks
- Competitive intelligence synthesis
- Sales enablement strategy
- Launch coordination

**Processes**:
- 11-Step GTM Process (from LTC)
- Positioning development
- Competitive analysis (from LTC: Competitor Analysis)
- Market segmentation (from LTC: Market Analysis)
- Sales enablement creation

**Collaboration Pattern**:
- Directs `product-marketing-manager` on campaigns and materials
- Partners with `competitive-intelligence` on market insights
- Works with `director-product-management` on launch timing
- Coordinates with `bizdev` on partnership positioning

**Handling Document References**:

When users reference documents using `@file` syntax:

1. **Recognize** all `@path/to/document.md` references
2. **Read** each referenced document using the Read tool
3. **Extract** relevant context:
   - Strategy docs: priorities, constraints, success criteria
   - Research docs: findings, user quotes, data points
   - Decision docs: criteria, options, rationale
   - Competitive docs: positioning, gaps, market dynamics
   - Financial docs: budgets, targets, thresholds
4. **Synthesize** insights across multiple documents
5. **Produce** deliverables that reflect the specific context
6. **Cite** source documents when incorporating their content

**Agent Invocation Behavior**:
```
When given a GTM strategy task:
  → Invoke @competitive-intelligence for competitive analysis
  → Invoke @product-marketing-manager for campaign execution
  → May consult @bizops for business case alignment

When given a positioning task:
  → Invoke @competitive-intelligence for differentiation inputs
  → Invoke @product-marketing-manager for messaging execution
```

---

#### 6. Product Marketing Manager (`product-marketing-manager`)

**RACI Responsibilities**:
- **Responsible**: Market & Customer Intimacy
- **Consulted**: Business Plan, Go to Market

**Key Deliverables**:
- Marketing collateral (brochures, datasheets, whitepapers)
- Campaign execution (email, social, content)
- Customer research and feedback synthesis
- Sales enablement materials
- Competitive battle cards

**Processes**:
- Content creation and management
- Campaign planning and execution
- Customer interview synthesis
- Competitive messaging updates

**Collaboration Pattern**:
- Reports to `director-product-marketing` on campaign performance
- Partners with `competitive-intelligence` on competitive materials
- Works with `product-manager` on feature messaging
- Coordinates with Sales on enablement needs

**Handling Document References**:

When users reference documents using `@file` syntax:

1. **Recognize** all `@path/to/document.md` references
2. **Read** each referenced document using the Read tool
3. **Extract** relevant context:
   - Strategy docs: priorities, constraints, success criteria
   - Research docs: findings, user quotes, data points
   - Decision docs: criteria, options, rationale
   - Competitive docs: positioning, gaps, market dynamics
   - Financial docs: budgets, targets, thresholds
4. **Synthesize** insights across multiple documents
5. **Produce** deliverables that reflect the specific context
6. **Cite** source documents when incorporating their content

**Agent Invocation Behavior**:
```
When given a campaign task:
  → May invoke @competitive-intelligence for competitive talking points

When given a customer research task:
  → May invoke @value-realization for usage data insights
```

---

### Complementary Roles (6 agents)

#### 7. Business Operations (`bizops`)

**RACI Responsibilities**:
- **Accountable**: Business Plan, Go to Market, Market & Customer Intimacy, Organizational Processes
- **Responsible**: Pricing Strategy, Stakeholder Intimacy

**Key Deliverables**:
- Business plans and cases
- Financial projections and models
- KPI dashboards and tracking
- QBR materials
- Data analysis and insights

**Processes**:
- Business planning (from LTC: Business Operations)
- Financial analysis and modeling
- Data analysis and reporting
- Cross-functional process facilitation

**Collaboration Pattern**:
- Partners with `vp-product` on business metrics
- Works with `value-realization` on outcome tracking
- Coordinates with `competitive-intelligence` on market sizing
- Supports all roles with data and analysis

**Handling Document References**:

When users reference documents using `@file` syntax:

1. **Recognize** all `@path/to/document.md` references
2. **Read** each referenced document using the Read tool
3. **Extract** relevant context:
   - Strategy docs: priorities, constraints, success criteria
   - Research docs: findings, user quotes, data points
   - Decision docs: criteria, options, rationale
   - Competitive docs: positioning, gaps, market dynamics
   - Financial docs: budgets, targets, thresholds
4. **Synthesize** insights across multiple documents
5. **Produce** deliverables that reflect the specific context
6. **Cite** source documents when incorporating their content

**Agent Invocation Behavior**:
```
When given a business case task:
  → May invoke @competitive-intelligence for market data
  → May invoke @value-realization for customer success data

When given a financial modeling task:
  → May invoke @value-realization for revenue attribution data
```

---

#### 8. Value Realization (`value-realization`)

**RACI Responsibilities**:
- **Responsible**: Market & Customer Intimacy
- **Consulted**: Product Requirements

**Key Deliverables**:
- Success metrics definition and tracking
- ROI analysis and reporting
- Customer adoption dashboards
- Value realization playbooks
- Outcome-based learning reports

**Processes**:
- Value realization (from LTC: Value Realization)
- Success metrics design
- Adoption tracking
- Customer outcome analysis

**Collaboration Pattern**:
- Partners with `bizops` on business metrics
- Works with `product-manager` on success criteria
- Coordinates with Customer Success teams
- Feeds learnings to `director-product-management`

**Handling Document References**:

When users reference documents using `@file` syntax:

1. **Recognize** all `@path/to/document.md` references
2. **Read** each referenced document using the Read tool
3. **Extract** relevant context:
   - Strategy docs: priorities, constraints, success criteria
   - Research docs: findings, user quotes, data points
   - Decision docs: criteria, options, rationale
   - Competitive docs: positioning, gaps, market dynamics
   - Financial docs: budgets, targets, thresholds
4. **Synthesize** insights across multiple documents
5. **Produce** deliverables that reflect the specific context
6. **Cite** source documents when incorporating their content

**Agent Invocation Behavior**:
```
When given a success measurement task:
  → May invoke @bizops for financial data integration

When given an outcome review task:
  → Compile data and report to requesting agent
```

---

#### 9. Competitive Intelligence (`competitive-intelligence`)

**RACI Responsibilities**:
- **Responsible**: Pricing Strategy, Market & Customer Intimacy, Organizational Processes
- **Consulted**: Business Plan, Go to Market

**Key Deliverables**:
- Competitor analysis reports
- Market research insights
- Win/loss analysis
- Competitive positioning recommendations
- Market trend briefs

**Processes**:
- Competitor Analysis (from LTC: detailed process)
- Market Analysis (from LTC: Market Analysis and Segmentation)
- Win/loss tracking and synthesis
- Trend monitoring

**Collaboration Pattern**:
- Supports `director-product-marketing` with competitive insights
- Feeds `vp-product` with market intelligence
- Partners with `product-marketing-manager` on battle cards
- Works with `bizdev` on partnership landscape

**Handling Document References**:

When users reference documents using `@file` syntax:

1. **Recognize** all `@path/to/document.md` references
2. **Read** each referenced document using the Read tool
3. **Extract** relevant context:
   - Strategy docs: priorities, constraints, success criteria
   - Research docs: findings, user quotes, data points
   - Decision docs: criteria, options, rationale
   - Competitive docs: positioning, gaps, market dynamics
   - Financial docs: budgets, targets, thresholds
4. **Synthesize** insights across multiple documents
5. **Produce** deliverables that reflect the specific context
6. **Cite** source documents when incorporating their content

**Agent Invocation Behavior**:
```
When given a competitor analysis task:
  → Execute analysis and return to requesting agent
  → May invoke web search tools for current data

When given a market sizing task:
  → Execute research and return to requesting agent
```

---

#### 10. Business Development (`bizdev`)

**RACI Responsibilities**:
- **Responsible**: Business Plan, Go to Market, Organizational Processes
- **Consulted**: Pricing Strategy

**Key Deliverables**:
- Partnership strategy and pipeline
- Business development opportunities
- Market expansion plans
- Partnership agreements
- Ecosystem strategy

**Processes**:
- Business Development (from LTC: detailed process)
- Partnership evaluation
- Market opportunity analysis
- Deal structuring

**Collaboration Pattern**:
- Partners with `director-product-marketing` on GTM partnerships
- Works with `competitive-intelligence` on ecosystem mapping
- Coordinates with `bizops` on partnership business cases
- Aligns with `vp-product` on strategic partnerships

**Handling Document References**:

When users reference documents using `@file` syntax:

1. **Recognize** all `@path/to/document.md` references
2. **Read** each referenced document using the Read tool
3. **Extract** relevant context:
   - Strategy docs: priorities, constraints, success criteria
   - Research docs: findings, user quotes, data points
   - Decision docs: criteria, options, rationale
   - Competitive docs: positioning, gaps, market dynamics
   - Financial docs: budgets, targets, thresholds
4. **Synthesize** insights across multiple documents
5. **Produce** deliverables that reflect the specific context
6. **Cite** source documents when incorporating their content

**Agent Invocation Behavior**:
```
When given a partnership evaluation task:
  → May invoke @competitive-intelligence for ecosystem analysis
  → May invoke @bizops for financial modeling

When given a market expansion task:
  → May invoke @competitive-intelligence for market research
```

---

#### 11. Product Operations (`product-operations`)

**RACI Responsibilities**:
- **Responsible**: Product Delivery Planning, Product Requirements, Organizational Processes, Stakeholder Intimacy

**Key Deliverables**:
- Process documentation and improvement
- Tooling and systems management
- Launch execution coordination
- Quality assurance oversight
- Cross-team facilitation

**Processes**:
- Product Operations (from LTC: detailed process)
- Process optimization
- Tooling management
- Launch coordination

**Collaboration Pattern**:
- Supports `director-product-management` on process optimization
- Works with `product-manager` on delivery tooling
- Coordinates launches across all functions
- Manages product org systems and tools

**Handling Document References**:

When users reference documents using `@file` syntax:

1. **Recognize** all `@path/to/document.md` references
2. **Read** each referenced document using the Read tool
3. **Extract** relevant context:
   - Strategy docs: priorities, constraints, success criteria
   - Research docs: findings, user quotes, data points
   - Decision docs: criteria, options, rationale
   - Competitive docs: positioning, gaps, market dynamics
   - Financial docs: budgets, targets, thresholds
4. **Synthesize** insights across multiple documents
5. **Produce** deliverables that reflect the specific context
6. **Cite** source documents when incorporating their content

**Agent Invocation Behavior**:
```
When given a launch coordination task:
  → May invoke @product-manager for delivery status
  → May invoke @product-marketing-manager for marketing readiness
  → May invoke @value-realization for success metrics setup

When given a process improvement task:
  → Analyze and recommend, may consult @director-product-management
```

---

#### 12. UX Lead (`ux-lead`)

**RACI Responsibilities**:
- **Responsible**: Product Requirements

**Key Deliverables**:
- User research insights
- Design specifications and prototypes
- Usability testing results
- Information architecture
- Design system components

**Processes**:
- User research planning and execution
- Design iteration
- Usability testing
- Design system management

**Collaboration Pattern**:
- Partners with `product-manager` on requirements
- Reports to `director-product-management` on research insights
- Works with Engineering on design implementation
- Coordinates with `product-marketing-manager` on customer insights

**Handling Document References**:

When users reference documents using `@file` syntax:

1. **Recognize** all `@path/to/document.md` references
2. **Read** each referenced document using the Read tool
3. **Extract** relevant context:
   - Strategy docs: priorities, constraints, success criteria
   - Research docs: findings, user quotes, data points
   - Decision docs: criteria, options, rationale
   - Competitive docs: positioning, gaps, market dynamics
   - Financial docs: budgets, targets, thresholds
4. **Synthesize** insights across multiple documents
5. **Produce** deliverables that reflect the specific context
6. **Cite** source documents when incorporating their content

**Agent Invocation Behavior**:
```
When given a user research task:
  → Execute research and return insights to requesting agent

When given a design task:
  → May consult @product-manager for requirements clarity
```

---

### Leadership Team (1 agent)

#### 13. Product Leadership Team (`product-leadership-team`)

**Purpose**: Collective agent representing the PLT for cross-functional decisions, portfolio tradeoffs, and strategic alignment.

**Composition Represents**:
- VP Product / CPO
- Director of Product Management
- Director of Product Marketing
- Senior Product Managers
- Product Operations Lead

**Key Functions**:
- Portfolio prioritization and tradeoffs
- Cross-functional decision-making
- Strategic alignment verification
- Decision escalation resolution
- Outcome review and learning

**Decision Types Owned**:
- Stop/continue/re-scope decisions on initiatives
- Portfolio investment rebalancing
- Cross-team resource allocation
- Launch go/no-go decisions
- Strategic pivot decisions

**Processes**:
- Portfolio tradeoff facilitation
- Decision Interface Charter creation
- Outcome review sessions
- Strategic alignment reviews

**Handling Document References**:

When users reference documents using `@file` syntax:

1. **Recognize** all `@path/to/document.md` references
2. **Read** each referenced document using the Read tool
3. **Extract** relevant context:
   - Strategy docs: priorities, constraints, success criteria
   - Research docs: findings, user quotes, data points
   - Decision docs: criteria, options, rationale
   - Competitive docs: positioning, gaps, market dynamics
   - Financial docs: budgets, targets, thresholds
4. **Synthesize** insights across multiple documents
5. **Produce** deliverables that reflect the specific context
6. **Cite** source documents when incorporating their content

**Agent Invocation Behavior**:
```
When given a portfolio tradeoff task:
  → Frame the decision using Decision Interface Charter format
  → May invoke @bizops for financial impact analysis
  → May invoke @competitive-intelligence for market context
  → Synthesize inputs and recommend decision

When given a launch decision task:
  → Invoke @product-operations for launch readiness status
  → Invoke @product-manager for product readiness
  → Invoke @product-marketing-manager for GTM readiness
  → Make go/delay/de-scope recommendation

When given an outcome review task:
  → Invoke @value-realization for outcome data
  → Invoke @bizops for business impact data
  → Conduct review using outcome review framework
  → Document learnings and re-decision recommendations
```

---

## Agent-to-Agent Invocation Mechanism

### How Agents Call Other Agents

Each agent has the ability to invoke other agents using the Task tool. The agent prompt includes explicit guidance on when and how to delegate:

```yaml
---
name: director-product-management
description: Director of Product Management - assign roadmap, requirements, and team coordination tasks
model: sonnet
tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash
  - WebSearch
  - Task  # Enables agent-to-agent invocation
skills:
  - decision-record
  - roadmap-theme
  - commitment-check
---

You are a Director of Product Management...

## When to Delegate to Other Agents

Use the Task tool to invoke other agents when work falls outside your direct responsibilities:

**Invoke @product-manager when:**
- You need detailed feature specifications
- You need delivery status for specific product areas
- You need backlog prioritization for a specific area

**Invoke @ux-lead when:**
- You need user research insights
- You need design input for requirements
- You need usability assessment

**Invoke @competitive-intelligence when:**
- You need market context for roadmap decisions
- You need competitive feature comparisons

**Invoke @product-operations when:**
- You need process optimization support
- You need tooling recommendations

Example delegation:
"I need feature specifications for the new dashboard. Let me invoke the product-manager agent."
→ Use Task tool with subagent_type="product-manager" and prompt describing the specific need
```

### Delegation Patterns

#### Hierarchical Delegation (Manager → Direct Report)
```
@vp-product → @director-product-management → @product-manager
@director-product-marketing → @product-marketing-manager
```

#### Cross-Functional Consultation
```
@product-manager ↔ @ux-lead (on requirements)
@director-product-marketing ↔ @competitive-intelligence (on market insights)
@bizops ↔ @value-realization (on metrics)
```

#### Escalation Path
```
@product-manager → @director-product-management → @vp-product → @cpo
@product-marketing-manager → @director-product-marketing → @vp-product
```

#### PLT Coordination
```
@product-leadership-team can invoke any agent to gather inputs for decisions
Any agent can escalate to @product-leadership-team for cross-functional decisions
```

---

## Skills (Slash Commands) - 41 Total

Skills are shared utilities that any agent can invoke. Each skill produces a specific deliverable or guides a specific process.

### Full Document Deliverables (10)

These skills produce **complete, comprehensive documents** - the actual working deliverables that product organizations create and present to stakeholders.

#### `/prd`
**Purpose**: Create a complete Product Requirements Document
**Owner**: Product Manager
**Output**: Full PRD including:
- Executive summary
- Problem statement and opportunity
- Target users and personas
- Goals and success metrics
- Detailed requirements (functional, non-functional)
- User stories with acceptance criteria
- Design requirements
- Technical considerations
- Dependencies and constraints
- Timeline and milestones
- Risks and mitigations
- Appendices

#### `/product-roadmap`
**Purpose**: Create a complete product roadmap document
**Owner**: Director of Product Management
**Output**: Full roadmap including:
- Executive summary
- Product vision alignment
- Strategic themes with rationale
- Quarterly/annual view
- All initiatives with priorities, effort, owners
- Dependencies map
- Success metrics per theme
- Resource requirements
- Risk assessment
- Stakeholder communication plan

#### `/business-case`
**Purpose**: Create a comprehensive business case
**Owner**: BizOps / Product Manager
**Output**: Full business case including:
- Executive summary
- Problem/opportunity statement
- Proposed solution
- Market analysis
- Competitive landscape
- Financial projections (revenue, costs, ROI)
- Investment requirements
- Risk analysis
- Implementation timeline
- Success criteria
- Recommendation

#### `/business-plan`
**Purpose**: Create a complete business plan
**Owner**: BizOps
**Output**: Full business plan including:
- Executive summary
- Product/market overview
- Market opportunity analysis
- Competitive positioning
- Business model
- Revenue model and projections
- Cost structure
- Go-to-market approach
- Organizational requirements
- Key milestones
- Financial projections (3-5 year)
- Key risks and mitigations

#### `/gtm-strategy`
**Purpose**: Create a comprehensive go-to-market strategy
**Owner**: Director of Product Marketing
**Output**: Full GTM strategy including:
- Executive summary
- Market analysis and segmentation
- Target customer profiles (ICP, personas)
- Positioning and messaging framework
- Competitive differentiation
- Pricing and packaging strategy
- Sales strategy and motion
- Marketing strategy and channels
- Partner/channel strategy
- Launch plan with timeline
- Sales enablement plan
- Success metrics and KPIs
- Budget and resources

#### `/pricing-strategy`
**Purpose**: Create a complete pricing strategy document
**Owner**: VP Product / Pricing Strategist
**Output**: Full pricing strategy including:
- Executive summary
- Market and competitive analysis
- Value proposition alignment
- Pricing model selection and rationale
- Price points and tiers
- Packaging strategy
- Discount policy and governance
- Geographic/segment variations
- Competitive comparison
- Financial impact analysis
- Implementation plan
- Monitoring and adjustment triggers

#### `/competitive-landscape`
**Purpose**: Create a comprehensive competitive analysis report
**Owner**: Competitive Intelligence
**Output**: Full competitive analysis including:
- Executive summary
- Market overview
- Competitor profiles (detailed)
- Feature comparison matrix
- Pricing comparison
- Positioning comparison
- Strengths/weaknesses analysis
- Market share analysis
- Competitive trends
- Win/loss patterns
- Strategic recommendations
- Battle cards summary

#### `/market-analysis`
**Purpose**: Create a comprehensive market analysis
**Owner**: Competitive Intelligence / PMM
**Output**: Full market analysis including:
- Executive summary
- Market definition and scope
- Market size (TAM, SAM, SOM)
- Market segmentation
- Customer needs analysis
- Buying behavior and journey
- Market trends and dynamics
- Regulatory considerations
- Competitive landscape overview
- Growth opportunities
- Market entry/expansion recommendations

#### `/launch-plan`
**Purpose**: Create a complete product launch plan
**Owner**: Product Operations / PMM
**Output**: Full launch plan including:
- Executive summary
- Launch objectives and success criteria
- Target audience and messaging
- Launch timeline (detailed)
- Cross-functional responsibilities (RACI)
- Marketing activities and campaigns
- Sales enablement activities
- Customer success preparation
- Support readiness
- Technical/operations readiness
- Risk mitigation plan
- Budget
- Post-launch activities

#### `/qbr-deck`
**Purpose**: Create a Quarterly Business Review presentation
**Owner**: BizOps / VP Product
**Output**: Full QBR including:
- Executive summary
- Key metrics performance vs targets
- Product delivery highlights
- Customer wins and losses
- Market and competitive updates
- Financial performance
- Key learnings and pivots
- Next quarter priorities
- Resource needs
- Risks and blockers
- Asks and decisions needed

---

### V2V Phase-Specific Skills (8)

These skills align directly to the V2V System flow phases:

#### `/strategic-intent`
**V2V Phase**: 1 - Strategic Foundation
**Purpose**: Document strategic intent and direction
**Owner**: CPO / VP Product
**Output**: Strategic intent document including:
- Vision alignment
- Strategic priorities
- Investment themes
- Success definition
- Constraints and guardrails

#### `/strategy-communication`
**V2V Phase**: 3 - Strategic Commitments
**Purpose**: Create strategy communication package for stakeholders
**Owner**: CPO / Director PM
**Output**: Strategy communication including:
- Executive summary
- Strategic narrative
- Key messages by audience
- Roadmap highlights
- Success metrics
- FAQ document
- Presentation deck

#### `/campaign-brief`
**V2V Phase**: 4 - Coordinated Execution
**Purpose**: Create marketing campaign brief
**Owner**: Product Marketing Manager
**Output**: Campaign brief including:
- Campaign objectives
- Target audience
- Key messages
- Channels and tactics
- Timeline
- Budget
- Success metrics
- Creative requirements

#### `/sales-enablement`
**V2V Phase**: 4 - Coordinated Execution
**Purpose**: Create sales enablement package
**Owner**: Director Product Marketing
**Output**: Sales enablement including:
- Product overview
- Value proposition
- Target customer profile
- Discovery questions
- Objection handling
- Competitive positioning
- Demo script
- Case studies
- Pricing guidance

#### `/onboarding-playbook`
**V2V Phase**: 5 - Business & Customer Outcomes
**Purpose**: Create customer onboarding playbook
**Owner**: Value Realization / CS
**Output**: Onboarding playbook including:
- Onboarding journey map
- Key milestones
- Success criteria
- Common blockers and solutions
- Escalation paths
- Time-to-value targets
- Health indicators
- Handoff procedures

#### `/value-realization-report`
**V2V Phase**: 5 - Business & Customer Outcomes
**Purpose**: Create value realization report
**Owner**: Value Realization
**Output**: Value realization report including:
- Executive summary
- Value delivered vs promised
- Adoption metrics
- Customer health scores
- ROI analysis
- Success stories
- Risk areas
- Recommendations

#### `/customer-health-scorecard`
**V2V Phase**: 5 - Business & Customer Outcomes
**Purpose**: Create customer health scorecard
**Owner**: Value Realization / CS
**Output**: Health scorecard including:
- Overall health score
- Engagement metrics
- Adoption metrics
- Support metrics
- Expansion signals
- Churn risk indicators
- Action recommendations

#### `/retrospective`
**V2V Phase**: 6 - Learning & Adaptation Loop
**Purpose**: Conduct structured retrospective
**Owner**: Product Leadership Team
**Output**: Retrospective document including:
- What went well
- What didn't go well
- What we learned
- Action items
- Process improvements
- Decisions to revisit
- Follow-up owners

---

### Presentation Skill (1)

#### `/present`
**Purpose**: Convert any deliverable document to an HTML presentation
**Input**: Path to markdown document
**Output**: HTML presentation file using reveal.js
**Process**:
1. Parse the markdown document
2. Extract title, sections, tables, and key points
3. Generate slides using the base template
4. Apply product-org theme styling
5. Save as HTML file with same base name

**Automatically invoked by agents** after creating meaningful deliverables.

---

### Decision System Skills (3)

#### `/decision-record`
**Purpose**: Create a structured decision record
**Template Produces**:
```markdown
# Decision Record

**Decision**: [What is being decided]
**Date**: [When decided]
**Accountable Owner**: [Single person/role]

## Context
[Why this decision is needed now]

## Options Considered
1. [Option A] - [Pros/Cons]
2. [Option B] - [Pros/Cons]
3. [Option C] - [Pros/Cons]

## Decision Made
[The choice and rationale]

## Success Criteria
[How we'll know it worked - measurable]

## Re-decision Trigger
[What evidence would reopen this decision]

## Contributors
[Who provided input]
```

#### `/decision-charter`
**Purpose**: Create a Decision Interface Charter for recurring decisions
**Template Produces**:
```markdown
# Decision Interface Charter

**Decision**: [What recurring decision this governs]
**Decision Type**: [Strategic / Portfolio / Execution]
**Accountable Owner**: [Role, not just name]

## Decision Forum & Cadence
[When and where this is decided - e.g., "Weekly PLT meeting, Thursdays 2pm"]

## Required Inputs
| Role | Input Required | Deadline Before Decision |
|------|----------------|-------------------------|
| [Role 1] | [What they must provide] | [When] |
| [Role 2] | [What they must provide] | [When] |

## Decision Criteria
[What "ready to decide" looks like]

## Decision Rules
[How the decision is made when inputs are ready]

## Escalation Rule
[What triggers escalation, to whom, timeline]

## Success Criteria
| Metric | Target | Timeframe |
|--------|--------|-----------|
| [Leading indicator] | [Target] | T+2 weeks |
| [Mid indicator] | [Target] | T+6 weeks |
| [Lagging indicator] | [Target] | T+12 weeks |

## Re-decision Trigger
[What outcome evidence reopens this decision]

## Communication Plan
[Who is informed, how, when]
```

#### `/escalation-rule`
**Purpose**: Define escalation rules for a decision area
**Template Produces**:
```markdown
# Escalation Rule Definition

**Decision Area**: [What type of decisions this covers]
**Default Owner**: [Role who normally decides]

## Escalation Triggers
| Trigger Condition | Escalate To | Timeline |
|-------------------|-------------|----------|
| [Condition 1] | [Role] | [When] |
| [Condition 2] | [Role] | [When] |

## Escalation Process
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Information Required for Escalation
[What must be prepared before escalating]

## Resolution Expectation
[How quickly escalated decisions should be resolved]
```

---

### Strategic Skills (3)

#### `/strategic-bet`
**Purpose**: Formulate a strategic bet with explicit assumptions
**Template Produces**:
```markdown
# Strategic Bet

**Bet Name**: [Descriptive name]
**Owner**: [Single accountable person]
**Date**: [When formulated]

## The Bet
[What we believe will create value - 1-2 sentences]

## Customer Insight
[What we know about customer needs that supports this bet]

## Market Dynamics
[Competitive and market factors that make this bet timely]

## Business Intent
[How this serves company goals]

## Explicit Assumptions
1. [Assumption 1] - [How we'll validate]
2. [Assumption 2] - [How we'll validate]
3. [Assumption 3] - [How we'll validate]

## Opportunity Cost
[What we're NOT doing by choosing this bet]

## Success Criteria
| Metric | Target | Timeframe |
|--------|--------|-----------|
| [Metric 1] | [Target] | [When] |
| [Metric 2] | [Target] | [When] |

## Investment Required
- Resources: [Team/people needed]
- Timeline: [Expected duration]
- Dependencies: [What else must happen]

## Re-decision Points
[When we'll review and potentially pivot]
```

#### `/commitment-check`
**Purpose**: Validate that a commitment is properly hardened

#### `/portfolio-tradeoff`
**Purpose**: Structure a portfolio-level tradeoff decision

---

### Asset Creation Skills (8)

- `/vision-statement` - Draft a product vision statement
- `/roadmap-theme` - Define a roadmap theme with initiatives
- `/roadmap-item` - Define a specific roadmap item
- `/gtm-brief` - Create a go-to-market brief
- `/pricing-model` - Design a pricing model
- `/positioning-statement` - Create a positioning statement
- `/competitive-analysis` - Structure a competitive analysis
- `/market-segment` - Define a market segment

---

### Requirements Skills (3)

- `/feature-spec` - Create a feature specification
- `/user-story` - Write a user story with acceptance criteria
- `/prd-outline` - Create a PRD outline

---

### Operational Skills (3)

- `/launch-readiness` - Launch readiness decision checklist
- `/outcome-review` - Structure an outcome review for learning
- `/stakeholder-brief` - Create a stakeholder communication brief

---

### Assessment Skills (3)

- `/maturity-check` - Assess organizational maturity for a dimension
- `/pm-level-check` - Assess PM competency level
- `/decision-quality-audit` - Audit recent decisions for quality

---

## Rules (Path-Based Guidance) - 6 Files

Rules automatically apply guidance when working with files in specific paths.

| Rule File | Applies to Paths | Enforces |
|-----------|------------------|----------|
| `decision-system.md` | `**/decisions/**`, `**/charters/**` | Single owner, success criteria, re-decision triggers |
| `strategy-documents.md` | `**/strategy/**`, `**/bets/**`, `**/plans/**` | Assumptions documented, opportunity cost, GTM considered |
| `roadmaps.md` | `**/roadmaps/**` | Vision alignment, theme-based, prioritization rationale |
| `gtm-documents.md` | `**/gtm/**`, `**/launch/**` | GTM as strategic choice, positioning early, success criteria |
| `requirements.md` | `**/requirements/**`, `**/prds/**` | Customer-centric problem, success criteria, ownership |
| `maturity-context.md` | `**/*` | Maturity-appropriate guidance |

---

## Reference Documents - 5 Files

| Document | Content |
|----------|---------|
| `operating-principles.md` | 8 Operating Principles from Vision to Value |
| `raci-matrix.md` | Full RACI matrix from Structure Blueprint |
| `maturity-blueprint.md` | 4 maturity levels with criteria |
| `asset-blueprint.md` | 10 product org assets with deliverables |
| `pm-career-blueprint.md` | PM career development levels and competencies |

---

## Plugin File Structure

```
product-org-plugin/
├── .claude-plugin/
│   └── plugin.json                     # Plugin manifest (REQUIRED)
├── README.md                           # Documentation and usage guide
├── LICENSE                             # License file
├── PRODUCT-ORG-CLAUDE.md              # Main context file
│
├── agents/
│   ├── core/
│   │   ├── cpo/SKILL.md
│   │   ├── vp-product/SKILL.md
│   │   ├── director-product-management/SKILL.md
│   │   ├── product-manager/SKILL.md
│   │   ├── director-product-marketing/SKILL.md
│   │   └── product-marketing-manager/SKILL.md
│   │
│   ├── complementary/
│   │   ├── bizops/SKILL.md
│   │   ├── value-realization/SKILL.md
│   │   ├── competitive-intelligence/SKILL.md
│   │   ├── bizdev/SKILL.md
│   │   ├── product-operations/SKILL.md
│   │   └── ux-lead/SKILL.md
│   │
│   └── leadership/
│       └── product-leadership-team/SKILL.md
│
├── skills/
│   ├── core/
│   │   └── present/SKILL.md
│   ├── decisions/
│   │   ├── decision-record/SKILL.md
│   │   ├── decision-charter/SKILL.md
│   │   └── escalation-rule/SKILL.md
│   ├── strategy/
│   │   ├── strategic-bet/SKILL.md
│   │   ├── commitment-check/SKILL.md
│   │   └── portfolio-tradeoff/SKILL.md
│   ├── assets/
│   │   ├── vision-statement/SKILL.md
│   │   ├── roadmap-theme/SKILL.md
│   │   ├── roadmap-item/SKILL.md
│   │   ├── gtm-brief/SKILL.md
│   │   ├── pricing-model/SKILL.md
│   │   ├── positioning-statement/SKILL.md
│   │   ├── competitive-analysis/SKILL.md
│   │   └── market-segment/SKILL.md
│   ├── requirements/
│   │   ├── feature-spec/SKILL.md
│   │   ├── user-story/SKILL.md
│   │   └── prd-outline/SKILL.md
│   ├── operations/
│   │   ├── launch-readiness/SKILL.md
│   │   ├── outcome-review/SKILL.md
│   │   └── stakeholder-brief/SKILL.md
│   └── assessment/
│       ├── maturity-check/SKILL.md
│       ├── pm-level-check/SKILL.md
│       └── decision-quality-audit/SKILL.md
│
├── rules/
│   ├── decision-system.md
│   ├── strategy-documents.md
│   ├── roadmaps.md
│   ├── gtm-documents.md
│   ├── requirements.md
│   └── maturity-context.md
│
├── templates/
│   ├── documents/
│   │   ├── decision-interface-charter.md
│   │   ├── decision-record.md
│   │   ├── strategic-bet.md
│   │   ├── roadmap-theme.md
│   │   ├── gtm-brief.md
│   │   └── launch-readiness-checklist.md
│   └── presentations/
│       ├── base-template.html
│       ├── slide-layouts/
│       │   ├── title-slide.html
│       │   ├── section-slide.html
│       │   ├── metrics-slide.html
│       │   ├── table-slide.html
│       │   └── summary-slide.html
│       └── styles/
│           └── product-org-theme.css
│
├── reference/
│   ├── operating-principles.md
│   ├── raci-matrix.md
│   ├── maturity-blueprint.md
│   ├── asset-blueprint.md
│   └── pm-career-blueprint.md
│
└── hooks/
    ├── settings.json
    └── scripts/
        ├── validate-decision-record.sh
        └── ownership-check.sh
```

---

## Installation Instructions

### Recommended: Local Development Installation

**Option 1: Symlink (Recommended for Active Development)**

Create a symlink from your development folder to Claude's plugins directory:

**Windows (PowerShell as Administrator):**
```powershell
New-Item -ItemType SymbolicLink `
  -Path "$env:USERPROFILE\.claude\plugins\product-org" `
  -Target "C:\path\to\product-org-plugin"
```

**macOS/Linux:**
```bash
ln -s /path/to/product-org-plugin ~/.claude/plugins/product-org
```

**Option 2: Direct Folder Placement**
```bash
cp -r ./product-org-plugin ~/.claude/plugins/product-org
```

**Option 3: From Plugin Marketplace (once published)**

Within Claude Code, use:
```
/plugin install product-org@marketplace-name
```

### After Installation

Restart Claude Code. The plugin is automatically discovered from `~/.claude/plugins/`.

You immediately have access to:
- **13 role-based agents**: `@cpo`, `@vp-product`, `@director-product-management`, `@product-manager`, `@director-product-marketing`, `@product-marketing-manager`, `@bizops`, `@value-realization`, `@competitive-intelligence`, `@bizdev`, `@product-operations`, `@ux-lead`, `@product-leadership-team`
- **41 skills** organized by V2V phase: Full document deliverables (PRD, Roadmap, Business Case, GTM Strategy, etc.) + component skills
- **Responsive HTML presentations**: Every meaningful deliverable also generates desktop + mobile ready presentations

---

## Usage Examples

### Assign Tasks with Document Context

```
@product-manager Create a feature spec for user onboarding.
  See @research/onboarding-friction-study.md for user pain points
  and @engineering/auth-system-overview.md for technical constraints.
```

```
@director-product-marketing Develop GTM brief for Q2 launch.
  Positioning: @strategy/differentiation-strategy.md
  Competitive: @competitive/q1-market-analysis.md
  Segments: @gtm/segment-prioritization.md
```

```
@bizops Prepare business case for enterprise tier expansion.
  Market: @competitive/enterprise-market-sizing.md
  Criteria: @finance/investment-hurdle-rates.md
  Costs: @engineering/enterprise-scaling-estimate.md
```

### Invoke the Product Leadership Team

```
@product-leadership-team We need to make a portfolio tradeoff - should we delay Feature X to accelerate Feature Y?
```

### Use Skills Directly

```
/decision-charter for our weekly launch readiness meetings
```

```
/strategic-bet for entering the SMB market segment
```

### Multi-Agent Workflows

```
@cpo We need to develop the product vision for 2025. Please coordinate with the team to create it.
```
*CPO agent will:*
1. Draft initial vision framework
2. Invoke @competitive-intelligence for market context
3. Invoke @director-product-marketing for positioning input
4. Invoke @bizops for business alignment
5. Synthesize into final vision document + HTML presentation

---

## Implementation Phases

### Implementation Phase 1: Foundation + V2V Phase 1 Skills
**Files: ~20**
- `plugin.json`, `PRODUCT-ORG-CLAUDE.md`, `README.md`
- 6 core role agents (CPO, VP Product, Director PM, PM, Director PMM, PMM)
- V2V Phase 1 skills: `/strategic-intent`, `/market-analysis`, `/competitive-landscape`, `/vision-statement`
- Reference docs (`operating-principles.md`, `raci-matrix.md`, `v2v-system-flow.md`)

### Implementation Phase 2: Complementary Roles + V2V Phase 2 Skills
**Files: ~20**
- 6 complementary role agents + PLT agent
- V2V Phase 2 skills: `/business-case`, `/pricing-strategy`, `/positioning-statement`, `/decision-record`, `/decision-charter`
- Reference docs (`maturity-blueprint.md`, `asset-blueprint.md`)

### Implementation Phase 3: V2V Phase 3 + Presentation System
**Files: ~20**
- V2V Phase 3 skills: `/product-roadmap`, `/gtm-strategy`, `/strategy-communication`, `/commitment-check`
- `/present` skill + responsive HTML templates (desktop + mobile)
- Presentation theme CSS and slide layouts

### Implementation Phase 4: V2V Phase 4 - Execution Skills
**Files: ~20**
- V2V Phase 4 skills: `/prd`, `/feature-spec`, `/launch-plan`, `/campaign-brief`, `/sales-enablement`
- Component skills: `/roadmap-theme`, `/gtm-brief`, `/user-story`

### Implementation Phase 5: V2V Phases 5-6 - Outcomes + Learning Loop
**Files: ~15**
- V2V Phase 5 skills: `/onboarding-playbook`, `/value-realization-report`, `/customer-health-scorecard`
- V2V Phase 6 skills: `/outcome-review`, `/decision-quality-audit`, `/maturity-check`, `/retrospective`
- Rules files for path-based guidance
- Hooks (optional)
- GitHub repository setup and documentation

---

## Summary

| Component | Count |
|-----------|-------|
| Role-based agents | 13 |
| Skills (slash commands) | 41 |
| - Full document deliverables | 10 |
| - V2V phase-specific skills | 8 |
| - Component/template skills | 23 |
| Rules | 6 |
| Document templates | 6 |
| Presentation templates (responsive) | 6 |
| Reference docs | 5 |
| **Total files to create** | **~85** |

**Key differentiators:**
1. **V2V System Flow** - organized around the 6-phase Vision to Value flow
2. **Role-based agents** - mirrors actual product org structure (13 roles)
3. **Agent-to-agent collaboration** - agents can delegate and coordinate
4. **Full deliverables** - creates complete PRDs, Roadmaps, Business Cases, GTM Strategies
5. **Responsive HTML presentations** - every deliverable outputs desktop + mobile ready presentations
6. **One-command install** - GitHub + Claude Code Plugin Registry
7. **Operating Principles embedded** - Decision quality under pressure, cultural guardrails
8. **Learning Loop built-in** - outcome reviews, retrospectives, continuous improvement

---

## GitHub Repository

The plugin will be hosted on GitHub as a public repository:

**Repository**: `github.com/yohay/product-org-plugin` (or your preferred organization)

### Repository Structure
```
product-org-plugin/
├── .github/
│   ├── workflows/
│   │   └── release.yml              # Automated releases
│   └── ISSUE_TEMPLATE/
├── plugin.json
├── README.md                        # Full documentation with examples
├── LICENSE                          # MIT or similar
├── CHANGELOG.md
├── CONTRIBUTING.md
├── agents/
├── skills/
├── rules/
├── templates/
├── reference/
└── examples/                        # Example usage scenarios
    ├── new-product-launch/
    ├── quarterly-planning/
    └── strategic-decision/
```

### Installation from GitHub

```bash
# Clone the repository
git clone https://github.com/yohay/product-org-plugin.git

# Create symlink to Claude's plugins directory
# macOS/Linux:
ln -s $(pwd)/product-org-plugin ~/.claude/plugins/product-org

# Windows (PowerShell as Administrator):
# New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.claude\plugins\product-org" -Target "$(Get-Location)\product-org-plugin"
```

### Versioning and Releases

- Use semantic versioning (v1.0.0, v1.1.0, etc.)
- GitHub Releases for each version
- CHANGELOG.md documenting changes
- Users can checkout specific versions: `git checkout v1.0.0`

---

## Publishing to Plugin Registry

Once stable, publish to the Claude Code Plugin Registry for easier discovery:

1. **Prepare the plugin**:
   - Ensure `.claude-plugin/plugin.json` is complete and valid
   - Test all agents, skills, and rules
   - Write comprehensive README

2. **Publish to registry**:
   - Follow Claude Code Plugin Registry submission guidelines
   - Submit plugin for review via the marketplace portal

3. **Users can then install with**:
   Within Claude Code, use:
   ```
   /plugin install product-org@marketplace-name
   ```

---

## Future Enhancements (Post v1.0)

- **MCP Server**: Optional MCP server for integration with product management tools (Jira, ProductBoard, Aha!, etc.)
- **Custom branding**: Allow organizations to customize presentation templates with their branding
- **Analytics hooks**: Track which agents/skills are most used
- **Team sharing**: Share decisions and deliverables across team members' Claude Code instances
