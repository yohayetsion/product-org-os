# Phase 2 Intelligence Enhancements PRD

**Product**: Product Org OS
**Version**: 3.0
**Date**: 2026-01-25
**Owner**: Product Manager
**Status**: Draft - Revision 3
**V2V Phase**: Phase 3 - Strategic Commitments

---

## 1. Executive Summary

Phase 2 Intelligence Enhancements transform the Product Org OS from a "toolkit of skills" into an **intelligent, autonomous operating system**. This release introduces four interconnected capabilities:

1. **ROI Tracker** - Per-interaction time-savings display with progressive aggregation
2. **Intelligent Routing** - Minimum-agent orchestration with sub-agent spawning
3. **Scalable Context System** - Auto-capture, indexing, and smart retrieval
4. **Demo Environment** - Pre-populated context for immediate capability exploration

**Core Philosophy**: Users describe their problem. The system figures out the minimum agents needed, provides them detailed guidance, and agents work autonomously - spawning sub-agents if needed. Context flows automatically. ROI is visible on every interaction.

**Target Launch**: Phase 2B Month 3 (follows Phase 2A validation)

---

## 2. Problem Statement & Opportunity

### The Problems We're Solving

**Problem 1: Invisible ROI**
Users can't prove value to stakeholders. The CFO asks "what do we get for this?" and the user has no data. Need immediate, per-interaction ROI visibility like Claude Code provides.

**Problem 2: Agent Overhead**
Current routing requires users to understand 55 skills and 13 agents. Even with suggestions, users face unnecessary questions. Goal: System determines the MINIMUM agents needed and provides them rich guidance - no questions unless truly ambiguous.

**Problem 3: Context Doesn't Scale**
Current context system requires manual management. Users want: auto-capture of agent outputs, auto-indexing of important folders, easy onboarding, and smart retrieval.

**Problem 4: Cold Start Problem**
New users see an empty system and don't understand capabilities. Need a demo environment with realistic data so users can explore the "full system" immediately.

### Strategic Alignment

From user feedback:
> "System should understand user request and determine MINIMUM agents needed. Provide best guidance to agents on what to do. Allow agents to spawn sub-agents to complete work. Minimize questions to users."

> "Most/all conversation should be saved in context. Make context system MORE SCALABLE. Add indexing capabilities."

> "Ship with pre-existing demo context and files. Let users see system when full of data."

---

## 3. Scope

### In Scope

**Feature 1: ROI Tracker**
- Per-interaction time-savings display (Claude Code style)
- Session running totals
- Interaction-level storage for any aggregation
- User dashboard with export
- Quiet mode for power users

**Feature 2: Intelligent Routing (Orchestrator Pattern)**
- Request analysis to determine minimum agent set
- Rich guidance generation for each agent
- Sub-agent spawning capability
- Autonomous operation (minimal user questions)
- Override capability for experienced users

**Feature 3: Scalable Context System**
- Auto-save all agent outputs to context
- Folder indexing (agent discovers important folders)
- JSON index for fast topic-based retrieval
- Easy onboarding command (`/setup-context`)
- Smart filtering (index useful things, skip noise)

**Feature 4: Demo Environment**
- Pre-populated demo context shipped with plugin
- Realistic sample decisions, bets, feedback, documents
- Sample ROI history
- `/clear-demo` command for production use
- `/reset-demo` to restore demo content

### Out of Scope

| Item | Rationale | Potential Future Phase |
|------|-----------|----------------------|
| Custom planning mode | Use Claude Code native planning mode | SaaS (Phase 3+) |
| Team-level ROI aggregation | Requires Team tier infrastructure | Phase 3 |
| Team/org context sharing | Requires multi-tenancy | Phase 3 |
| Real-time collaborative context | Significant infrastructure | Phase 3+ |
| Voice/audio input | Different modality | Not planned |
| ROI gamification/targets | Anti-gamification design principle | Not planned |

---

## 4. Target Users & Personas

### Primary: The Justifying PM Lead
- **Pain**: Can't justify AI spend
- **Need**: Per-interaction ROI visibility to build the case
- **JTBD**: "Show my boss this tool pays for itself - with data"

### Secondary: The Overwhelmed New User
- **Pain**: Doesn't know where to start or what's possible
- **Need**: Demo environment to explore capabilities
- **JTBD**: "See what this thing can do before I commit"

### Tertiary: The Efficient Operator
- **Pain**: Too many questions, too much manual routing
- **Need**: Autonomous system that just works
- **JTBD**: "Describe my problem once and let the system figure it out"

---

## 5. Goals & Success Metrics

| Metric | Target | Timeframe | Measurement |
|--------|--------|-----------|-------------|
| Per-interaction ROI display | 100% of skill/agent completions | Launch | Feature verification |
| User confirms ROI "accurate" | 80%+ | T+4 weeks | In-product feedback |
| Routing: questions asked | <10% of requests | T+6 weeks | Telemetry |
| Routing: correct first attempt | 90%+ | T+6 weeks | Override rate |
| Context auto-save rate | 100% agent outputs | Launch | Feature verification |
| Demo exploration before clear | 60%+ new users | T+4 weeks | Telemetry |
| Free to Pro conversion | 8%+ | T+12 weeks | Stripe data |

---

## 6. Functional Requirements

### Feature 1: ROI Tracker

| ID | Requirement | Priority | Description |
|----|-------------|----------|-------------|
| ROI-001 | Per-interaction display | Must Have | After EVERY skill/agent completion, show time saved inline |
| ROI-002 | Session running total | Must Have | Show cumulative time saved in current session |
| ROI-003 | Interaction-level storage | Must Have | Store at individual interaction level for any aggregation |
| ROI-004 | Skill/agent baselines | Must Have | Pre-configured estimates per skill AND per agent type |
| ROI-005 | User dashboard | Must Have | Aggregate view: 30/90 day, top skills, ROI multiple |
| ROI-006 | Export (PDF/CSV) | Should Have | Shareable report for stakeholders |
| ROI-007 | Quiet mode toggle | Should Have | Option to minimize inline display for power users |
| ROI-008 | Privacy-first local | Must Have | All data local by default |

**Display Pattern** (Claude Code style):
```
[Agent completes task]
---
Time saved: ~45 minutes
Estimated manual: 2h research + 1.5h writing
This session: ~3.2 hours saved (4 interactions)
```

### Feature 2: Intelligent Routing (Orchestrator)

| ID | Requirement | Priority | Description |
|----|-------------|----------|-------------|
| RTR-001 | Orchestrator analysis | Must Have | Analyze request before any agent spawn |
| RTR-002 | Minimum agent determination | Must Have | Prefer 1 agent over 2, 2 over 3 |
| RTR-003 | Rich guidance generation | Must Have | Provide detailed briefing to each spawned agent |
| RTR-004 | Sub-agent spawning | Must Have | Agents can spawn other agents when needed |
| RTR-005 | Autonomous operation | Must Have | No questions unless truly ambiguous |
| RTR-006 | Context inheritance | Must Have | Sub-agents inherit parent context |
| RTR-007 | User override | Should Have | Experienced users can direct routing |
| RTR-008 | Routing explanation | Should Have | Brief explanation of why agents were chosen |

**Question Threshold** - Only ask when:
- Request is truly ambiguous (could mean opposite things)
- Critical information missing that can't be inferred
- User explicitly requested options

**NOT a reason to ask**:
- Multiple agents could handle it (pick the best one)
- Confidence is "medium" (make a decision)
- Want user to confirm (just do it)

### Feature 3: Scalable Context System

| ID | Requirement | Priority | Description |
|----|-------------|----------|-------------|
| CTX-001 | Auto-save agent outputs | Must Have | Everything agents create goes to context automatically |
| CTX-002 | JSON master index | Must Have | `index.json` at context root for fast topic lookup |
| CTX-003 | Topic-based retrieval | Must Have | Agents can query context by topic efficiently |
| CTX-004 | Folder indexing | Should Have | When agent encounters important folder, offer to index |
| CTX-005 | Smart filtering | Must Have | Index useful items, skip noise (node_modules, etc.) |
| CTX-006 | Easy onboarding | Must Have | `/setup-context` creates full structure |
| CTX-007 | Session summaries | Should Have | Auto-summarize sessions for cross-session continuity |
| CTX-008 | Token budget | Must Have | Limit context injection to 10K tokens |

**Index Structure**:
```json
{
  "entries": [
    {
      "id": "DOC-2026-001",
      "type": "prd",
      "title": "Authentication PRD",
      "path": "documents/prd-auth.md",
      "topics": ["authentication", "security"],
      "created": "2026-01-15",
      "lastAccessed": "2026-01-25"
    }
  ],
  "topicIndex": {
    "authentication": ["DOC-2026-001", "DR-2026-005"],
    "pricing": ["DR-2026-003", "SB-2026-001"]
  }
}
```

**Auto-Index Rules**:
- DO index: PRDs, decisions, strategies, feedback, meeting notes, roadmaps
- DON'T index: node_modules, build/, dist/, .git, binaries, temp files

### Feature 4: Demo Environment

| ID | Requirement | Priority | Description |
|----|-------------|----------|-------------|
| DEMO-001 | Pre-populated context | Must Have | Ship with realistic demo decisions, bets, feedback |
| DEMO-002 | Sample documents | Must Have | Demo PRD, roadmap, GTM strategy |
| DEMO-003 | Sample ROI history | Must Have | Show what dashboard looks like with data |
| DEMO-004 | Clear command | Must Have | `/clear-demo` removes demo content |
| DEMO-005 | Reset command | Should Have | `/reset-demo` restores demo content |
| DEMO-006 | Visual indicator | Must Have | Clear indicator when viewing demo vs production |
| DEMO-007 | First-run guidance | Must Have | Welcome message explaining demo and how to clear |

**Demo Content Package**:
- 5-10 decision records (variety of types)
- 2-3 strategic bets with assumptions
- 10-15 customer feedback entries with themes
- 1 complete PRD
- 1 product roadmap
- 1 GTM strategy brief
- 30-day ROI history showing realistic usage

**First-Run Experience**:
```
Welcome to Product Org OS!

This plugin ships with demo content so you can explore capabilities.

Try these commands:
  /context-recall pricing    - See sample decisions
  /portfolio-status          - See strategic bets
  /roi-report               - See ROI dashboard with data

Ready for real work? Run: /clear-demo
```

---

## 7. Non-Functional Requirements

### Performance

| Requirement | Target |
|-------------|--------|
| Per-interaction ROI display | <100ms after completion |
| Orchestrator routing decision | <1s |
| Context index query | <500ms for 1000+ entries |
| Full context retrieval | <2s |

### Scalability

| Requirement | Target |
|-------------|--------|
| Context entries | 5000+ without degradation |
| ROI history | 1 year per user |
| Index size | 10MB+ supported |

### Privacy

- All data local by default
- No cloud transmission without consent
- User can export/delete all data

---

## 8. User Stories

### ROI Tracker

**US-ROI-001: See Per-Interaction ROI**
```
As a product manager
I want to see time saved after every skill/agent interaction
So that I understand value in real-time

Acceptance Criteria:
- Every skill completion shows inline: "Time saved: ~X minutes"
- Every agent completion shows inline time saved
- Display includes estimated manual effort breakdown
- Session running total is visible
- Display is subtle (not intrusive) but always present
- "Quiet mode" available in settings
```

**US-ROI-002: View ROI Dashboard**
```
As a product leader
I want to see aggregate ROI data
So I can report to stakeholders

Acceptance Criteria:
- /roi-report shows 30/90 day summaries
- Shows top skills by time saved
- Shows ROI multiple (time saved / time using)
- Export to PDF/CSV available
```

### Intelligent Routing

**US-RTR-001: Autonomous Routing**
```
As a user describing a problem
I want the system to route to minimum agents without asking
So I can get results quickly

Acceptance Criteria:
- I type "I need a pricing strategy for our new feature"
- System determines: this needs @bizops (analysis) and routes there
- NO question asked - just routes
- Agent receives rich guidance about what I need
- If agent needs help, it can spawn sub-agent
```

**US-RTR-002: No Unnecessary Questions**
```
As a user
I want the system to make decisions, not ask me
So I'm not interrupted constantly

Acceptance Criteria:
- System only asks when request is truly ambiguous
- "Could be handled by X or Y" is NOT a reason to ask
- Make a decision, execute, let user override if wrong
- Questions limited to <10% of requests
```

**US-RTR-003: Sub-Agent Spawning**
```
As a PM agent working on a complex task
I want to spawn a sub-agent for specialized work
So I can deliver complete results

Acceptance Criteria:
- Agent can spawn another agent via Task tool
- Sub-agent inherits relevant context from parent
- Results flow back to parent agent
- User sees unified response
```

### Scalable Context

**US-CTX-001: Auto-Save Agent Outputs**
```
As a user
I want everything agents create to be saved automatically
So I don't have to manage context manually

Acceptance Criteria:
- PRDs created by /prd go to context/documents automatically
- Decisions from /decision-record go to context/decisions
- All outputs are indexed for retrieval
- No manual /context-save required for standard outputs
```

**US-CTX-002: Easy Onboarding**
```
As a new user
I want a simple command to set up context structure
So I can get started quickly

Acceptance Criteria:
- /setup-context creates full folder structure
- Includes index.json at root
- Creates all subdirectories
- Works idempotently (safe to run multiple times)
```

### Demo Environment

**US-DEMO-001: Explore with Demo Data**
```
As a new user
I want to see the system with realistic data
So I understand what's possible

Acceptance Criteria:
- First run shows demo content
- Can run /context-recall and see results
- Can run /portfolio-status and see bets
- Can run /roi-report and see dashboard
- Clear indicator when viewing demo
```

**US-DEMO-002: Clear Demo for Production**
```
As a user ready to use for real
I want a simple command to remove demo content
So I start fresh

Acceptance Criteria:
- /clear-demo removes all demo content
- Preserves folder structure
- Preserves any user-created content
- Confirms before clearing
```

---

## 9. Technical Considerations

### Orchestrator Architecture

```
User Request
    |
    v
+-------------------+
|   Orchestrator    |
|-------------------|
| 1. Parse intent   |
| 2. Identify scope |
| 3. Select agents  |
| 4. Generate brief |
+-------------------+
    |
    v
+-------------------+
| Agent Selection   |
| - Minimum needed  |
| - Rich guidance   |
| - Context package |
+-------------------+
    |
    v
+-------------------+     +-------------------+
| Primary Agent     |---->| Sub-Agent (if    |
| - Works task      |     | needed)          |
| - May delegate    |     | - Inherits ctx   |
+-------------------+     +-------------------+
    |
    v
+-------------------+
| Result Synthesis  |
| - Combine outputs |
| - Show ROI        |
+-------------------+
```

### Context Index Architecture

```
context/
├── index.json              # Master index
├── demo/                   # Demo content (removable)
│   └── [demo items...]
├── documents/
│   ├── index.md
│   └── [user documents...]
├── decisions/
│   ├── index.md
│   └── [decisions...]
├── bets/
│   ├── index.md
│   └── [strategic bets...]
├── feedback/
│   ├── index.md
│   ├── themes.md
│   └── [feedback items...]
└── sessions/
    └── [session summaries...]
```

### ROI Storage Model

```
ROI_Interaction {
  id: uuid
  timestamp: datetime
  type: "skill" | "agent"
  name: string
  estimated_minutes_saved: float
  manual_effort_breakdown: {
    research: float
    writing: float
    review: float
  }
  session_id: string
}

ROI_Session {
  id: string
  date: date
  total_minutes_saved: float
  interaction_count: int
}
```

---

## 10. Timeline & Milestones

### Phase 2A: Validation MVP (10 weeks)

| Week | Milestone | Deliverable |
|------|-----------|-------------|
| 1-2 | Design | Technical design, API contracts |
| 3-4 | ROI Inline | Per-interaction display working |
| 5-6 | Orchestrator MVP | Basic minimum-agent routing |
| 7-8 | Context Index | Auto-save + JSON index |
| 9-10 | Demo Package | Demo content + commands |

**2A Validation Criteria**:
- [ ] Per-interaction ROI displays correctly
- [ ] Routing questions <20% of requests (relaxed for MVP)
- [ ] Auto-save working for standard outputs
- [ ] Demo environment explorable

### Phase 2B: Full Build (16 weeks)

| Week | Milestone |
|------|-----------|
| 11-14 | ROI dashboard + export |
| 15-18 | Sub-agent spawning + rich guidance |
| 19-22 | Folder indexing + session summaries |
| 23-26 | Polish, testing, rollout |

**Total: 26 weeks**

---

## 11. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Orchestrator makes wrong routing decisions | Medium | High | Override capability, learning from corrections |
| ROI estimates feel inaccurate | Medium | High | User calibration, "~" prefix, conservative baselines |
| Auto-save creates clutter | Medium | Medium | Smart filtering, folder organization |
| Demo confuses users (real vs demo) | Low | Medium | Clear visual indicators, first-run guidance |
| Context index becomes slow | Low | Medium | Pagination, lazy loading, index optimization |

---

## 12. Appendices

### Appendix A: Demo Content Specification

**Decisions (5-10)**:
- DR-001: Pricing model decision (value-based vs. tiered)
- DR-002: API versioning strategy
- DR-003: Mobile-first vs. responsive approach
- DR-004: Authentication provider selection
- DR-005: Analytics platform choice

**Strategic Bets (2-3)**:
- SB-001: Enterprise tier expansion
- SB-002: Self-serve onboarding

**Feedback (10-15)**:
- Mix of feature requests, complaints, compliments
- Various sources: sales, support, direct customer
- Emerging themes identified

**Documents**:
- Sample PRD for "Dashboard Redesign"
- Product roadmap with 3 themes
- GTM brief for enterprise launch

### Appendix B: Orchestrator Decision Matrix

| Request Pattern | Agent Selection | Guidance Focus |
|-----------------|-----------------|----------------|
| "Create PRD for X" | @pm | Feature scope, user stories |
| "Pricing for X" | @bizops | Market analysis, models |
| "Launch plan for X" | @pmm-dir + @prod-ops | GTM + operational |
| "Strategic decision about X" | @vp-product | Options, tradeoffs |
| "Customer feedback about X" | @pm + @value-realization | Analysis + action |

### Appendix C: Skill Baseline Estimates (ROI)

| Skill/Agent | Time Saved | Manual Equivalent |
|-------------|------------|-------------------|
| /prd | 3-5 hours | Research + writing + review |
| /decision-record | 45-90 min | Documentation + formatting |
| /strategic-bet | 2-4 hours | Analysis + assumption mapping |
| /user-story | 15-30 min | Writing + acceptance criteria |
| @pm (general) | 1-2 hours | Varies by task |
| @plt (meeting) | 4-6 hours | Coordinating multiple stakeholders |

---

## Document Control

**Version**: 3.0
**Created**: 2026-01-24
**Last Updated**: 2026-01-25

**Revision History**:
| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-24 | Initial draft |
| 2.0 | 2026-01-24 | Director PM feedback incorporated |
| 3.0 | 2026-01-25 | User feedback: per-interaction ROI, orchestrator routing, context indexing, demo environment |

**Key Changes in V3**:
- ROI: Changed from aggregate-first to per-interaction-first (Claude Code style)
- Routing: Changed from clarification-based to orchestrator/minimum-agents
- Removed: Custom planning mode (use Claude Code native)
- Added: Scalable context with indexing
- Added: Demo environment feature
- Philosophy: Autonomous operation, minimize questions

---

*End of PRD*
