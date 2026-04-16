# Program Management Knowledge Pack

**Version**: 1.0
**Type**: knowledge-pack
**Primary Users**: @program-manager, @coo, @operations-dir, @project-manager

---
<!-- Attribution:
  Frameworks and patterns in this knowledge pack were informed by:
  - Anthropic knowledge-work-plugins (operations domain reference)
  - PMI PMBOK Guide — program and project management frameworks
  - SAFe (Scaled Agile Framework) — scaled agile delivery patterns
  Adapted and expanded for Product Org OS agents.
-->

## Program vs Project Management

### Fundamental Distinction

| Dimension | Project | Program | Portfolio |
|-----------|---------|---------|-----------|
| **Focus** | Delivering a specific output | Achieving a strategic outcome through coordinated projects | Optimizing investment across programs/projects |
| **Scope** | Defined, controlled via change management | Evolving, adapts as component projects deliver | Organization-wide, strategy-driven |
| **Duration** | Defined start and end | May span years, outlive component projects | Ongoing, aligned to strategy cycles |
| **Success Metric** | On time, on budget, to spec | Benefits realized, strategic objectives achieved | Portfolio ROI, strategic alignment |
| **Change** | Managed via change control board | Expected and continuous; program adapts | Rebalancing and reprioritization |
| **Governance** | Project board / sponsor | Steering committee / program board | Portfolio review board |
| **Leader** | Project Manager | Program Manager | Portfolio Manager / CPO |
| **Deliverables** | Products, services, results | Benefits, capabilities, organizational change | Strategic value, balanced investment |

### When to Use Program Management (vs Just Projects)

| Signal | Indicates Program |
|--------|-------------------|
| Multiple projects share a strategic objective | Yes |
| Cross-project dependencies create risk | Yes |
| Benefits only materialize when multiple projects deliver together | Yes |
| Shared resources across projects create conflicts | Yes |
| Stakeholders need consolidated visibility | Yes |
| A single project with clear deliverables | No -- use project management |

---

## Program Lifecycle

### Five Phases

```
Phase 1: INITIATION
├── Define program vision and strategic alignment
├── Identify component projects and high-level scope
├── Secure executive sponsorship
├── Establish initial governance structure
└── Develop program charter

Phase 2: PLANNING
├── Develop program management plan
├── Define benefits realization framework
├── Map cross-project dependencies
├── Establish resource allocation model
├── Design stakeholder engagement plan
├── Create program-level risk register
└── Define program metrics and KPIs

Phase 3: EXECUTION
├── Initiate and coordinate component projects
├── Manage cross-project dependencies actively
├── Facilitate resource sharing and conflict resolution
├── Run governance cadences (steering committees, reviews)
├── Track benefits delivery against plan
└── Manage program-level change requests

Phase 4: MONITORING & CONTROLLING
├── Consolidated program status reporting
├── Benefits tracking and variance analysis
├── Cross-project risk management
├── Dependency status and critical path updates
├── Stakeholder satisfaction monitoring
├── Program health dashboard maintenance
└── Escalation management

Phase 5: CLOSURE & TRANSITION
├── Confirm all benefits realized or transitioned
├── Close remaining component projects
├── Transition deliverables to operations
├── Capture lessons learned
├── Archive program artifacts
├── Release resources
└── Final stakeholder communication
```

### Phase Gate Criteria

| Gate | From - To | Key Questions |
|------|-----------|---------------|
| G1 | Initiation - Planning | Is strategic alignment confirmed? Sponsor committed? Charter approved? |
| G2 | Planning - Execution | Is the program plan approved? Dependencies mapped? Governance in place? Resources allocated? |
| G3 | Execution - Monitoring | Are all component projects initiated? Initial baselines established? |
| G4 | Monitoring - Closure | Are all benefits realized or have transition plans? All projects complete or closed? |

---

## Benefits Realization Management

### The Benefits Lifecycle

```
Identify Benefits → Define Measures → Plan Realization → Execute & Track → Sustain & Optimize
```

### Benefits Map Template

| Benefit ID | Benefit Description | Type | Measure | Baseline | Target | Realization Timeline | Owner | Status |
|------------|---------------------|------|---------|----------|--------|---------------------|-------|--------|
| B-001 | [Description] | Financial / Non-financial | [KPI] | [Current] | [Target] | [When expected] | [Name] | Not started / In progress / Realized |

### Benefit Types

| Type | Examples | Measurement Approach |
|------|----------|---------------------|
| **Financial** | Revenue increase, cost reduction, avoided cost | Direct measurement against baseline |
| **Operational** | Efficiency gain, cycle time reduction, error reduction | Process metrics before/after |
| **Strategic** | Market position, competitive advantage, capability building | Qualitative assessment + proxy metrics |
| **Compliance** | Regulatory adherence, risk reduction, audit readiness | Compliance scores, audit findings |

### Benefits Realization Pitfalls

- Benefits defined at program start but never tracked after launch
- No baseline measurement established before the program begins
- Benefits "claimed" by the program that would have occurred anyway (attribution error)
- Operational teams not engaged in sustaining benefits after program closure
- Benefits measured at project level but not aggregated to program outcome level

---

## Stakeholder Engagement at Program Level

### Program Stakeholder Tiers

| Tier | Who | Engagement Level | Cadence |
|------|-----|-----------------|---------|
| **Tier 1: Decision Makers** | Executive sponsor, steering committee, C-suite | Active management, co-ownership | Weekly 1:1, monthly steering committee |
| **Tier 2: Influencers** | Department heads, functional leaders, senior architects | Regular consultation, input on direction | Bi-weekly updates, quarterly reviews |
| **Tier 3: Contributors** | Project managers, team leads, subject matter experts | Operational coordination | Weekly program syncs, daily as needed |
| **Tier 4: Affected Parties** | End users, support teams, partner organizations | Communication and change management | Monthly newsletters, milestone announcements |

### Stakeholder Engagement Matrix

| Stakeholder Group | Current State | Desired State | Strategy |
|-------------------|--------------|---------------|----------|
| [Group] | Unaware / Resistant / Neutral / Supportive / Champion | [Target] | [Specific actions to move from current to desired] |

### Communication Framework

| Audience | Content | Format | Frequency | Owner |
|----------|---------|--------|-----------|-------|
| Steering committee | Strategic status, decisions needed, escalations | Formal presentation | Monthly | Program Manager |
| Executive sponsor | Risks, blockers, political issues | 1:1 meeting | Weekly | Program Manager |
| Project managers | Dependencies, resource changes, priorities | Working session | Weekly | Program Manager |
| Functional leaders | Impact on their teams, resource asks | Targeted briefing | Bi-weekly | Program Manager |
| Broader organization | Milestones, wins, upcoming changes | Newsletter / intranet | Monthly | Comms lead |

---

## Cross-Project Dependency Management

### Dependency Types

| Type | Description | Risk Level | Management Approach |
|------|-------------|-----------|---------------------|
| **Mandatory (hard)** | Technically or logically required | High | Critical path management, buffer allocation |
| **Discretionary (soft)** | Preferred sequence, based on best practice | Medium | Negotiate sequence, consider parallel execution |
| **External** | Depends on vendor, partner, or outside team | High | Contractual SLAs, escalation protocols, contingency plans |
| **Resource** | Same person/team needed by multiple projects | High | Capacity planning, resource leveling, skill cross-training |
| **Technical** | Shared platform, API, infrastructure | Medium-High | Architecture alignment, integration testing, API contracts |

### Dependency Register Template

| Dep ID | From Project | To Project | Type | Description | Owner | Due Date | Status | Risk if Late |
|--------|-------------|-----------|------|-------------|-------|----------|--------|-------------|
| D-001 | [Source] | [Target] | [Type] | [What is needed] | [Name] | [Date] | On track / At risk / Blocked | [Impact description] |

### Dependency Management Process

```
1. IDENTIFY: Map all cross-project dependencies during planning (and continuously)
2. CLASSIFY: Hard vs soft, internal vs external, resource vs technical
3. ASSIGN: Every dependency has a single owner and a consumer
4. TRACK: Weekly dependency review with all project leads
5. ESCALATE: Trigger escalation when dependency is at risk (not when it fails)
6. RESOLVE: Options -- resequence, add resources, descope, accept delay
7. LEARN: Post-dependency retrospectives for chronic issues
```

### Dependency Visualization

```
Project A ──[API contract]──► Project B ──[data migration]──► Project C
     │                                                           ▲
     └──────────[shared infrastructure]──────────────────────────┘
                        │
                   Project D (platform)
```

Use dependency maps (not just lists) to reveal systemic risks and circular dependencies.

---

## Program Governance Structures

### Three-Tier Governance Model

```
STRATEGIC TIER: Steering Committee / Program Board
├── Membership: Executive sponsor, senior leaders, external advisors
├── Decision rights: Strategic direction, major budget changes, program continuation/termination
├── Cadence: Monthly (or quarterly for stable programs)
├── Escalation to: Executive committee / board
│
MANAGEMENT TIER: Program Manager + PMO
├── Membership: Program Manager, project managers, key functional leads
├── Decision rights: Cross-project priorities, resource conflicts, dependency resolution, risk mitigation
├── Cadence: Weekly program review, bi-weekly cross-project sync
├── Escalation to: Steering committee
│
DELIVERY TIER: Project Teams
├── Membership: Project managers, team leads, individual contributors
├── Decision rights: Within-project scope, technical decisions, task assignment
├── Cadence: Daily standups, sprint reviews, retrospectives
├── Escalation to: Program Manager
```

### Steering Committee Agenda Template

| Time | Item | Purpose | Owner |
|------|------|---------|-------|
| 5 min | Program health summary (RAG) | Orientation | Program Manager |
| 10 min | Key achievements since last meeting | Celebrate progress | Program Manager |
| 15 min | Risks and issues requiring committee input | Seek decisions | Program Manager |
| 15 min | Benefits realization update | Track value delivery | Benefits Owner |
| 10 min | Decisions needed | Get commitment | Program Manager |
| 5 min | Actions and next steps | Align on follow-up | Program Manager |

### Decision Rights Matrix (Program Level)

| Decision Type | Project Manager | Program Manager | Steering Committee |
|---------------|----------------|-----------------|-------------------|
| Task assignment within project | Decides | Informed | -- |
| Cross-project resource reallocation | Consulted | Recommends | Decides |
| Scope change within project | Recommends | Decides | Informed |
| Scope change affecting program | Consulted | Recommends | Decides |
| Budget reallocation (<10%) | -- | Decides | Informed |
| Budget reallocation (>10%) | -- | Recommends | Decides |
| Project addition/removal | Consulted | Recommends | Decides |
| Dependency conflict resolution | Consulted | Decides | Informed |
| Program continuation/termination | Informed | Recommends | Decides |

---

## Resource Allocation Across Projects

### Resource Allocation Models

| Model | Description | Best For | Risk |
|-------|-------------|---------|------|
| **Dedicated** | Resources assigned full-time to one project | Critical/complex projects | Underutilization during low-activity periods |
| **Shared** | Resources split across projects (e.g., 60/40) | Steady-state programs | Context switching tax, conflicting priorities |
| **Pool** | Central resource pool assigned to projects on demand | Organizations with many small projects | Lack of ownership, shallow expertise |
| **Matrix** | Functional home + project assignment | Large organizations | Dual reporting, priority conflicts |

### Resource Conflict Resolution Framework

```
Step 1: Quantify the conflict (which projects, what resource, what timeframe)
Step 2: Assess impact of each option (delay Project A vs delay Project B)
Step 3: Apply decision criteria:
   - Strategic alignment (which project is more strategic?)
   - Dependency impact (which delay causes more downstream damage?)
   - Benefits impact (which delay costs more in unrealized benefits?)
   - Contractual obligations (any hard external deadlines?)
Step 4: Decide at the appropriate governance level
Step 5: Communicate decision and rationale to all affected teams
```

### Capacity Planning Template

| Resource / Skill | Available Capacity | Project A | Project B | Project C | Total Demand | Gap |
|-----------------|-------------------|-----------|-----------|-----------|-------------|-----|
| [Role/Person] | [Hours/FTE] | [Hours/FTE] | [Hours/FTE] | [Hours/FTE] | [Sum] | [Demand - Available] |

---

## Risk Management at Program Level

### Risk Aggregation Model

Program risk is NOT simply the sum of project risks. Three categories:

| Category | Description | Examples |
|----------|-------------|---------|
| **Aggregated project risks** | Individual project risks rolled up and assessed for program-level impact | A delay in Project A cascading to Projects B, C, D |
| **Inter-project risks** | Risks that exist only because projects interact | Integration failures, conflicting architectures, resource contention |
| **Program-level risks** | Risks to the program as a whole, not attributable to any single project | Strategic shift making program obsolete, executive sponsor departure, funding reduction |

### Program Risk Register Template

| Risk ID | Category | Description | Probability | Impact | Score | Affected Projects | Owner | Mitigation Strategy | Status |
|---------|----------|-------------|-------------|--------|-------|-------------------|-------|-------------------|--------|
| PR-001 | [Aggregated / Inter-project / Program-level] | [Description] | H/M/L | H/M/L | [PxI] | [List] | [Name] | [Strategy] | Open / Mitigated / Closed |

### Risk Response Strategies

| Strategy | When to Use | Program Application |
|----------|-------------|---------------------|
| **Avoid** | Eliminate the threat by changing scope or approach | Remove a component project, change technical approach |
| **Mitigate** | Reduce probability or impact | Add buffers, cross-train resources, add integration testing |
| **Transfer** | Shift risk to a third party | Insurance, outsourcing, contractual penalties |
| **Accept** | Risk is within tolerance or cost of response exceeds impact | Document and monitor, establish contingency reserve |
| **Escalate** | Risk is beyond program authority | Escalate to steering committee or portfolio level |

### Risk Heat Map

```
          IMPACT
          Low    Med    High   Critical
PROB  ┌───────┬───────┬───────┬──────────┐
High  │ Med   │ High  │ Crit  │ Crit     │
Med   │ Low   │ Med   │ High  │ Crit     │
Low   │ Low   │ Low   │ Med   │ High     │
      └───────┴───────┴───────┴──────────┘
```

---

## Program Metrics and KPIs

### Metric Categories

| Category | Metrics | Purpose |
|----------|---------|---------|
| **Schedule** | Schedule Performance Index (SPI), milestone hit rate, dependency on-time rate | Are we delivering on time? |
| **Cost** | Cost Performance Index (CPI), budget burn rate, forecast at completion | Are we delivering within budget? |
| **Benefits** | Benefits realization rate, time-to-benefit, benefit variance | Are we delivering value? |
| **Quality** | Defect density, rework rate, acceptance criteria pass rate | Are we delivering well? |
| **Stakeholder** | Stakeholder satisfaction score, escalation frequency, decision cycle time | Are stakeholders engaged? |
| **Risk** | Risk burn-down, top risks trend, issues resolution time | Are we managing uncertainty? |

### Key Program KPIs

| KPI | Formula / Measure | Target | Red Flag |
|-----|-------------------|--------|----------|
| **Schedule Variance (SV)** | EV - PV | >= 0 | Negative and trending worse |
| **Cost Performance Index (CPI)** | EV / AC | >= 1.0 | < 0.9 (will likely not recover) |
| **Milestone Hit Rate** | Milestones on time / total milestones | > 80% | < 60% |
| **Dependency Health** | Dependencies on track / total dependencies | > 90% | < 70% |
| **Benefits Realization %** | Benefits delivered / benefits planned | Per timeline | > 20% variance from plan |
| **Resource Utilization** | Actual hours / available hours | 75-85% | > 95% (burnout) or < 60% (waste) |
| **Escalation Rate** | Escalations per month | Stable or declining | Increasing trend |
| **Stakeholder Confidence** | Survey score (1-5) | >= 4.0 | < 3.0 |

### RAG Status Definitions (Program Level)

| Status | Schedule | Budget | Benefits | Dependencies |
|--------|----------|--------|----------|-------------|
| **Green** | On track, SPI >= 0.95 | CPI >= 0.95 | Benefits on track to plan | All dependencies on track |
| **Amber** | Minor slippage, recoverable | 5-10% variance, mitigation planned | Benefits at risk, actions in place | 1-2 dependencies at risk |
| **Red** | Significant delay, escalation needed | >10% variance, recovery plan required | Benefits will not be realized without intervention | Critical path dependencies blocked |

---

## Change Management Integration

### Program Change vs Project Change

| Dimension | Project Change | Program Change |
|-----------|---------------|----------------|
| **Scope** | Within a single project | Affects multiple projects or program objectives |
| **Approval** | Project change control board | Program steering committee |
| **Impact analysis** | Schedule, cost, quality for one project | Cascade analysis across all component projects |
| **Stakeholders** | Project team and sponsor | All affected project teams, program stakeholders |

### Organizational Change Management (OCM) in Programs

Programs often deliver organizational change, not just technical outputs. The program manager must integrate OCM:

| OCM Element | Program Manager's Role |
|-------------|----------------------|
| **Awareness** | Ensure stakeholders understand why the change is happening |
| **Desire** | Engage sponsors to motivate participation |
| **Knowledge** | Coordinate training across component projects |
| **Ability** | Ensure transition support is planned and resourced |
| **Reinforcement** | Build sustainability into benefits realization |

### ADKAR Model Application to Programs

```
A - Awareness:   "Why is this program happening?" → Executive communications
D - Desire:      "What's in it for me?" → Stakeholder engagement plan
K - Knowledge:   "How do I work in the new way?" → Training program (across projects)
A - Ability:     "Can I do it?" → Support structures, coaching, pilot groups
R - Reinforcement: "Will this stick?" → Benefits tracking, recognition, feedback loops
```

---

## PMI Standard for Program Management (PgMP) Key Concepts

### Five Performance Domains (PMI PgMP)

| Domain | Focus | Key Activities |
|--------|-------|---------------|
| **Program Strategy Alignment** | Ensuring program delivers strategic value | Strategic fit analysis, program charter, business case maintenance |
| **Program Benefits Management** | Defining, delivering, and sustaining benefits | Benefits register, benefits realization plan, transition to operations |
| **Program Stakeholder Engagement** | Managing stakeholder expectations | Stakeholder analysis, engagement plan, communication strategy |
| **Program Governance** | Decision-making framework | Governance plan, steering committee, escalation procedures |
| **Program Life Cycle Management** | Managing the program through its phases | Phase gates, component management, program closure |

### Program Charter vs Project Charter

| Element | Program Charter | Project Charter |
|---------|----------------|-----------------|
| Vision | Strategic vision for the outcome | Project objectives |
| Scope | High-level program scope, component projects | Detailed project scope |
| Benefits | Expected benefits with measures | Deliverables |
| Governance | Governance structure, decision rights | Reporting structure |
| Assumptions | Strategic and organizational assumptions | Project-level assumptions |
| Risks | Program-level risks | Project-level risks |
| Budget | Program budget envelope | Project budget |
| Timeline | Program timeline with major milestones | Detailed project schedule |

### Program Roadmap vs Project Schedule

The program roadmap shows:
- Component project timelines at a high level
- Key integration points and milestones
- Benefits realization milestones
- Governance events (steering committees, phase gates)
- External dependencies and constraints

The program roadmap is NOT a Gantt chart. It is a strategic communication tool.

---

## Portfolio-Program Alignment

### Strategic Alignment Framework

```
Organizational Strategy
    │
    ├── Strategic Objective 1
    │   ├── Program A (delivers capability for Objective 1)
    │   │   ├── Project A1
    │   │   ├── Project A2
    │   │   └── Project A3
    │   └── Standalone Project B
    │
    ├── Strategic Objective 2
    │   └── Program C
    │       ├── Project C1
    │       └── Project C2
    │
    └── Strategic Objective 3
        └── Program D (cross-cutting)
```

### Portfolio-Program Interface

| Portfolio Provides to Program | Program Provides to Portfolio |
|------------------------------|------------------------------|
| Strategic direction and priorities | Benefits realization reports |
| Funding authorization | Resource utilization data |
| Cross-program dependency visibility | Risk escalations |
| Resource allocation decisions | Lessons learned |
| Go/no-go at phase gates | Capacity forecasts |

### Alignment Health Check

| Question | Green | Amber | Red |
|----------|-------|-------|-----|
| Does the program still align to a current strategic objective? | Directly aligned | Partially aligned, adaptation possible | Strategy has shifted, program may be obsolete |
| Are the expected benefits still relevant? | Fully relevant | Partially relevant, some benefits deprecated | Benefits no longer strategic |
| Is the program receiving adequate investment? | Fully funded | Minor gaps, workarounds in place | Underfunded, benefits at risk |
| Are cross-program dependencies managed? | All tracked and on schedule | Some at risk, mitigation underway | Critical dependencies unresolved |

---

## Agile at Scale

### SAFe Program Increment (PI) Planning

| Element | Description |
|---------|-------------|
| **What** | 2-day event aligning all teams in an Agile Release Train (ART) to a shared plan |
| **Who** | All ART members (50-125 people), business owners, product management, architects |
| **Cadence** | Every 8-12 weeks (start of each PI) |
| **Duration** | 2 days (Day 1: vision + team planning, Day 2: draft plans + confidence vote) |
| **Output** | PI objectives per team, program board with dependencies, ROAM'd risks |

### PI Planning Agenda

| Day 1 | Day 2 |
|-------|-------|
| Business context and vision (1 hr) | Planning adjustments (1 hr) |
| Architecture vision (0.5 hr) | Team breakout 2 (2 hrs) |
| Planning context and lunch (1 hr) | Draft plan review (2 hrs) |
| Team breakout 1 (3 hrs) | Program risks and ROAM (0.5 hr) |
| Draft plan review (1 hr) | Confidence vote (0.25 hr) |
| Management review (1 hr) | Planning retrospective (0.5 hr) |

### ROAM Risk Management (SAFe)

| Category | Meaning | Action |
|----------|---------|--------|
| **R**esolved | Risk no longer exists | Remove from board |
| **O**wned | Assigned to someone, mitigation in progress | Track with owner |
| **A**ccepted | Risk acknowledged, no further action planned | Monitor |
| **M**itigated | Actions taken to reduce probability/impact | Track effectiveness |

### LeSS (Large-Scale Scrum) Key Concepts

| Concept | Description |
|---------|-------------|
| **LeSS** | 2-8 teams on one product, one Product Backlog, one Product Owner |
| **LeSS Huge** | 8+ teams, Area Product Owners, Requirement Areas |
| **Sprint** | All teams share one Sprint, one Sprint Review |
| **Coordination** | Prefer informal/voluntary over formal coordination |
| **Communities of Practice** | Cross-team learning and standards |
| **Overall Retrospective** | System-level retrospective after team retrospectives |

### Agile at Scale Comparison

| Dimension | SAFe | LeSS | Spotify Model |
|-----------|------|------|---------------|
| **Structure** | Hierarchical (Portfolio > ART > Team) | Minimal (Product > Teams) | Squads, Tribes, Chapters, Guilds |
| **Prescriptiveness** | High -- detailed roles, ceremonies, artifacts | Low -- descale, simplify | Low -- cultural model, not framework |
| **Planning** | PI Planning every 8-12 weeks | Sprint Planning (shared) | Tribe-level quarterly planning |
| **Coordination** | RTE, System Demo, ART Sync | Communities of Practice, multi-team meetings | Chapter leads, guild meetups |
| **Best for** | Large organizations needing structure | Product-focused organizations wanting simplicity | Culture-driven organizations |

---

## Program Health Dashboard

### Dashboard Components

| Section | Content | Update Frequency |
|---------|---------|-----------------|
| **Program Summary** | One-line status, overall RAG, key message | Weekly |
| **Milestone Tracker** | Upcoming milestones with status | Weekly |
| **Component Project Status** | RAG per project, key risks per project | Weekly |
| **Dependency Map** | Visual dependency status, blocked items highlighted | Weekly |
| **Benefits Tracker** | Benefits realization progress vs plan | Monthly |
| **Risk Heatmap** | Top 5 risks with trend arrows | Weekly |
| **Resource Utilization** | Capacity vs demand by skill/team | Bi-weekly |
| **Financials** | Budget vs actual, forecast at completion | Monthly |
| **Decisions Log** | Recent decisions and pending decisions | Weekly |
| **Escalations** | Open escalations with status | Weekly |

### Status Report Template (One-Pager)

```
PROGRAM STATUS: [Name] | Period: [Date Range] | Overall: [RAG]

KEY MESSAGE: [One sentence -- what leadership needs to know]

ACHIEVEMENTS THIS PERIOD:
- [Achievement 1]
- [Achievement 2]

UPCOMING MILESTONES (Next 30 Days):
| Milestone | Project | Due | Status |
|-----------|---------|-----|--------|

TOP RISKS:
| Risk | Impact | Trend | Mitigation |
|------|--------|-------|------------|

DECISIONS NEEDED:
| Decision | Context | Options | Deadline |
|----------|---------|---------|----------|

BENEFITS TRACKING:
| Benefit | Target | Actual | Variance |
|---------|--------|--------|----------|
```

### Health Indicators -- Trend Analysis

Track these monthly to detect patterns:

| Indicator | Healthy Trend | Warning Signal |
|-----------|--------------|----------------|
| Milestone hit rate | Stable > 80% | Declining over 2+ months |
| Dependency resolution time | Stable or improving | Increasing average |
| Escalation frequency | Stable or declining | Spike or sustained increase |
| Stakeholder confidence | Stable > 4/5 | Drop of 0.5+ in one period |
| Resource utilization | 75-85% | Consistently > 90% or < 60% |
| Benefits variance | Within 10% of plan | > 20% behind plan |

---

## Transition Planning and Handoff

### Transition Planning Framework

| Phase | Activities | Deliverables |
|-------|-----------|-------------|
| **Prepare** | Identify receiving teams, assess readiness, document current state | Transition plan, readiness assessment |
| **Transfer** | Knowledge transfer sessions, documentation handover, shadowing | Training materials, runbooks, SOPs |
| **Support** | Hypercare period, escalation support, defect resolution | Support agreement, SLA for transition period |
| **Sustain** | Steady-state operations, benefits monitoring, continuous improvement | Operational handoff complete, benefits owner assigned |

### Transition Checklist

| Category | Item | Status |
|----------|------|--------|
| **Documentation** | All program documentation archived and accessible | |
| **Knowledge** | Knowledge transfer sessions completed with receiving teams | |
| **Systems** | System access transferred, program-specific tools decommissioned or handed over | |
| **Benefits** | Benefits ownership transferred to operational teams with tracking mechanisms | |
| **Support** | Hypercare period defined with escalation paths | |
| **Resources** | All program resources released or reassigned | |
| **Contracts** | Vendor contracts transferred or closed | |
| **Stakeholders** | Final communication sent, stakeholder expectations reset | |
| **Lessons** | Lessons learned captured and shared | |
| **Governance** | Steering committee formally closed, ongoing governance defined | |

### Hypercare Model

| Period | Support Level | Escalation Path | Exit Criteria |
|--------|-------------|-----------------|---------------|
| Weeks 1-2 | Full program team available | Direct to program manager | No critical issues open |
| Weeks 3-4 | Reduced team, key leads available | Through operations manager | Issue rate declining |
| Weeks 5-8 | On-call only | Standard support channels | Steady-state metrics achieved |
| Post-hypercare | None (program closed) | Standard operations | Benefits tracking transferred |

### Lessons Learned Template

| Dimension | What Worked | What Didn't | Recommendation |
|-----------|------------|-------------|----------------|
| Governance | [Example] | [Example] | [Actionable recommendation] |
| Stakeholder management | [Example] | [Example] | [Actionable recommendation] |
| Dependency management | [Example] | [Example] | [Actionable recommendation] |
| Resource management | [Example] | [Example] | [Actionable recommendation] |
| Risk management | [Example] | [Example] | [Actionable recommendation] |
| Benefits realization | [Example] | [Example] | [Actionable recommendation] |
| Communication | [Example] | [Example] | [Actionable recommendation] |

---

## Common Pitfalls

- Treating a program as a big project -- managing tasks instead of managing the connections between projects
- Benefits defined at the outset but never measured or tracked through delivery
- Governance that is too heavy for program size, creating process overhead that slows teams
- Dependency management by assumption -- "they know we need it" is not dependency management
- Resource conflicts resolved by whoever shouts loudest instead of strategic prioritization criteria
- Status theater -- all projects report green while the program is failing at the integration points
- Stakeholder engagement that is broadcast-only (newsletters) without genuine two-way dialogue
- Closing the program before benefits are realized or without assigning benefits ownership
- Aggregating project risks without identifying the inter-project and program-level risks that only exist at the program layer
- Confusing program roadmaps with detailed Gantt charts -- the roadmap is a strategic tool, not a task tracker

---

*Last Updated: 2026-03-28*
*References: PMI Standard for Program Management 4th Edition (PMI, 2017), SAFe 6.0 (Scaled Agile, 2023), Managing Successful Programmes (MSP, AXELOS), LeSS Framework (Larman & Vodde)*
