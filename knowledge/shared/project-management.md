# Project Management Knowledge Pack

**Version**: 1.0
**Type**: knowledge-pack
**Primary Users**: `program-manager`, `project-manager`, `operations-dir`, `coo`

---

## PMBoK 7th Edition — Principles-Based Approach

### 12 Project Management Principles

| # | Principle | Application |
|---|-----------|-------------|
| 1 | **Stewardship** | Act responsibly, with integrity, care for resources |
| 2 | **Team** | Build collaborative, high-performing teams |
| 3 | **Stakeholders** | Engage stakeholders proactively, understand needs |
| 4 | **Value** | Focus on value delivery, not just deliverables |
| 5 | **Systems Thinking** | Recognize project interactions within broader systems |
| 6 | **Leadership** | Adapt leadership style to context |
| 7 | **Tailoring** | Adapt approach based on project context |
| 8 | **Quality** | Build quality into processes and deliverables |
| 9 | **Complexity** | Navigate complexity through adaptation |
| 10 | **Risk** | Optimize risk responses for opportunities and threats |
| 11 | **Adaptability & Resilience** | Build in ability to respond to change |
| 12 | **Change** | Enable change to achieve envisioned future state |

### 8 Performance Domains

| Domain | Focus | Key Activities |
|--------|-------|---------------|
| **Stakeholder** | Engagement throughout lifecycle | Identify, analyze, plan, manage, monitor |
| **Team** | Team performance and development | Culture, leadership, team development |
| **Development Approach** | How the project delivers value | Predictive, adaptive, hybrid selection |
| **Planning** | Organizing and coordinating | Scope, schedule, cost, quality planning |
| **Project Work** | Establishing processes, managing resources | Physical/virtual processes, procurement, knowledge |
| **Delivery** | Requirements, scope, quality | Value delivery, deliverable quality |
| **Measurement** | Evaluating project performance | Metrics, dashboards, forecasting |
| **Uncertainty** | Risks, ambiguity, complexity | Risk management, uncertainty response |

---

## Agile Portfolio Management

### SAFe Essentials (Scaled Agile Framework)

| Level | Focus | Key Roles | Cadence |
|-------|-------|-----------|---------|
| **Portfolio** | Strategy, investment, governance | Lean Portfolio Mgmt, Epic Owners | Quarterly PI Planning |
| **Large Solution** | Coordinating multiple ARTs | Solution Train Engineer | PI cadence |
| **Essential (ART)** | Agile Release Train alignment | RTE, Product Management, Architects | 8-12 week PI |
| **Team** | Delivery within sprint | Scrum Master, PO, Dev Team | 2-week sprints |

### Agile vs Predictive Decision Framework

| Factor | Agile Favored | Predictive Favored |
|--------|--------------|-------------------|
| Requirements clarity | Low — will evolve | High — well understood |
| Technology maturity | New — needs experimentation | Proven — well understood |
| Stakeholder engagement | Available for frequent feedback | Limited availability |
| Team experience | Experienced, self-organizing | Mixed, needs structure |
| Regulatory constraints | Flexible compliance | Strict documentation requirements |
| Risk tolerance | Higher — can pivot | Lower — need predictability |
| Delivery model | Incremental value delivery | Big-bang delivery acceptable |

---

## Project Planning Frameworks

### Work Breakdown Structure (WBS)

```
Level 1: Project Name
├── Level 2: Phase / Deliverable Area
│   ├── Level 3: Work Package
│   │   ├── Level 4: Activity
│   │   └── Level 4: Activity
│   └── Level 3: Work Package
└── Level 2: Phase / Deliverable Area
    └── Level 3: Work Package
```

**WBS Rules:**
- 100% rule: WBS must capture 100% of project scope
- Work packages should be 8-80 hours of effort
- Each element should have a single owner
- Decompose until estimatable and assignable

### Estimation Methods

| Method | Best For | Accuracy | Effort |
|--------|---------|----------|--------|
| **Analogous** | Early stage, similar past projects | Low (±50%) | Low |
| **Parametric** | Repetitive work, historical data available | Medium (±25%) | Medium |
| **Three-Point** | Tasks with uncertainty | Medium-High (±15%) | Medium |
| **Bottom-Up** | Detailed planning phase | High (±10%) | High |
| **Planning Poker** | Agile teams, relative sizing | Medium | Low |

### Three-Point Estimate Formula

```
PERT Estimate = (Optimistic + 4 × Most Likely + Pessimistic) / 6
Standard Deviation = (Pessimistic - Optimistic) / 6
```

---

## Program Management

### Program vs Project

| Dimension | Project | Program |
|-----------|---------|---------|
| Focus | Specific deliverable | Strategic outcome |
| Duration | Defined start/end | May be ongoing |
| Scope | Fixed (with change control) | Evolving |
| Benefits | Outputs (deliverables) | Outcomes (business value) |
| Management | Project Manager | Program Manager |
| Governance | Project board | Program steering committee |

### Program Governance Framework

```
Steering Committee
├── Decision rights: Strategic direction, budget approval, risk escalation
├── Cadence: Monthly
│
Program Manager
├── Decision rights: Cross-project priorities, resource conflicts, dependency management
├── Cadence: Weekly status, bi-weekly program review
│
Project Managers
├── Decision rights: Within-project scope, task assignment
├── Cadence: Daily standups, sprint reviews
```

### Dependency Management

| Dependency Type | Description | Management Approach |
|-----------------|-------------|-------------------|
| **Finish-to-Start** | B can't start until A finishes | Critical path management |
| **Start-to-Start** | B can't start until A starts | Parallel tracking |
| **Finish-to-Finish** | B can't finish until A finishes | Completion coordination |
| **External** | Depends on outside team/vendor | Escalation protocol |
| **Resource** | Same resource needed by multiple projects | Capacity planning |

---

## Critical Chain Method

### Theory of Constraints Applied to Projects

| Concept | Traditional PM | Critical Chain |
|---------|---------------|---------------|
| Task estimates | Padded by individuals | Remove padding, use project buffer |
| Critical path | Longest sequence of tasks | Longest chain considering resources |
| Buffer | Hidden in each task | Explicit project and feeding buffers |
| Multi-tasking | Expected | Minimized (one task at a time) |
| Progress tracking | % complete | Buffer consumption rate |

### Buffer Types

| Buffer | Purpose | Size |
|--------|---------|------|
| **Project buffer** | Protects delivery date | ~50% of critical chain duration |
| **Feeding buffer** | Protects critical chain from non-critical paths | ~50% of feeding chain duration |
| **Resource buffer** | Alerts resources they'll be needed soon | Warning system, not time |

---

## Stakeholder Management

### Power-Interest Grid

```
HIGH POWER
│ Manage Closely │ Keep Satisfied │
│ (Key Players)  │ (Sponsors)     │
├────────────────┼────────────────┤
│ Keep Informed  │ Monitor        │
│ (Allies)       │ (Crowd)        │
LOW POWER        LOW              HIGH
                 INTEREST
```

### RACI Matrix Template

| Activity | Project Sponsor | PM | Tech Lead | Team |
|----------|----------------|-----|-----------|------|
| Charter approval | A | R | C | I |
| Requirements | C | A | R | R |
| Architecture | I | C | A/R | R |
| Sprint planning | I | A | R | R |
| Risk review | C | A/R | C | I |
| Go/no-go | A | R | C | I |

---

## Project Metrics

### Earned Value Management (EVM)

| Metric | Formula | Interpretation |
|--------|---------|---------------|
| **PV** (Planned Value) | Budget for planned work | What we planned to spend |
| **EV** (Earned Value) | Budget for completed work | What we've earned |
| **AC** (Actual Cost) | Actual expenditure | What we've spent |
| **SPI** (Schedule Performance Index) | EV / PV | >1 = ahead, <1 = behind |
| **CPI** (Cost Performance Index) | EV / AC | >1 = under budget, <1 = over |
| **EAC** (Estimate at Completion) | BAC / CPI | Projected total cost |
| **TCPI** (To-Complete Performance Index) | (BAC - EV) / (BAC - AC) | Required efficiency to finish on budget |

### Agile Metrics

| Metric | What It Measures | Healthy Range |
|--------|-----------------|---------------|
| **Velocity** | Story points per sprint | Stable (±20%) |
| **Sprint Burndown** | Remaining work in sprint | Trending to zero |
| **Release Burnup** | Cumulative scope completed | Approaching target |
| **Cycle Time** | Time from start to done | Decreasing or stable |
| **Lead Time** | Time from request to delivery | Decreasing |
| **WIP** | Work in progress | Within WIP limits |
| **Escaped Defects** | Bugs found in production | Decreasing |

---

*Last Updated: 2026-02-14*
*References: PMBoK 7th Edition (PMI, 2021), SAFe 6.0 (Scaled Agile, 2023), Theory of Constraints (Goldratt)*


## Common Pitfalls

- Project timelines are estimates, not commitments — flag assumptions explicitly
- Resource allocation recommendations need actual team capacity data
- Dependencies between workstreams must be identified before scheduling
