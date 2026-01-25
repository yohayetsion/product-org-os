# Phase 2 Intelligence Enhancements - Options Analysis

**Date**: 2026-01-25
**Author**: Director of Product Management
**Purpose**: Analyze architectural options for key features based on user feedback

---

## Executive Summary

User feedback has identified significant directional changes from the original PRD:

| Area | Original Direction | Feedback Direction |
|------|-------------------|-------------------|
| ROI Tracking | Aggregate dashboard focus | Individual interaction-level display (like Claude Code) |
| Routing | Confidence-based with clarification questions | Minimum agents, sub-agent spawning, NO questions |
| Context | Manual + auto relevance filtering | Auto-capture everything, indexing, scalable retrieval |
| Planning Mode | Build custom planning mode | Use Claude Code's native planning mode |
| Demo | Not included | Ship with pre-populated demo environment |

This analysis provides options for each major decision area.

---

## 1. ROI Tracking Architecture

### User Requirement
> "Must have individual-level tracking similar to Claude Code's per-interaction display. Should work at individual action level AND team/group level later. Track ROI across interactions."

### Option A: Interaction-Level First (Recommended)

**Description**: Every agent invocation and skill execution shows immediate ROI inline, with progressive aggregation.

**Implementation**:
```
Individual Interaction → Session Summary → Daily/Weekly Roll-up → Dashboard
```

**Display Pattern** (Claude Code style):
```
[Agent completes task]
---
Time saved: ~45 minutes
Estimated manual effort: 2 hours research + 1.5 hours writing
This session: ~3.2 hours saved (4 interactions)
```

**Pros**:
- Immediate value visibility (user sees ROI every time)
- Builds ROI story incrementally
- Matches Claude Code UX pattern users know
- Natural progression to team aggregation

**Cons**:
- More UI surface area to design
- Need baselines per agent AND per skill
- May feel noisy for power users (need dismiss option)

**Effort**: Medium (baseline data + inline display + storage)

### Option B: Dashboard-First with Inline Teaser

**Description**: Full dashboard experience with minimal inline indicator.

**Display Pattern**:
```
[Agent completes task]
+45 min saved (view details →)
```

**Pros**:
- Cleaner inline experience
- Dashboard can be richer
- Easier to build incrementally

**Cons**:
- Less immediate gratification
- User must navigate to see value
- Doesn't match Claude Code pattern

**Effort**: Low-Medium

### Option C: Session-Level Focus

**Description**: Aggregate at session level, show summary at session end.

**Pros**:
- Simplest implementation
- Less noisy UX

**Cons**:
- Delays gratification
- Misses per-interaction feedback user requested
- Harder to attribute value

**Effort**: Low

### Recommendation: Option A

User explicitly referenced Claude Code's per-interaction display. This pattern provides immediate value reinforcement and naturally builds toward team aggregation.

**Key Design Decisions**:
1. Show inline after every skill/agent completion
2. Include session running total
3. Store at interaction level (enables any aggregation later)
4. Provide "quiet mode" toggle for power users

---

## 2. Enhanced Routing Architecture

### User Requirements
> "System should understand user request and determine MINIMUM agents needed. Provide best guidance to agents on what to do. Allow agents to spawn sub-agents to complete work. Goal: Best results with minimum agent spawning. Minimize questions to users."

This is a fundamental shift from the original "clarification-based" routing to "intelligent autonomous routing."

### Option A: Orchestrator Pattern (Recommended)

**Description**: Single orchestrator analyzes request, determines minimal agent set, provides detailed guidance, agents can spawn sub-agents.

**Flow**:
```
User Request
    ↓
Orchestrator Analysis
    ↓
Determine: What needs to be done?
           Who is the minimum set to do it?
           What guidance does each agent need?
    ↓
Spawn Agent(s) with Detailed Briefing
    ↓
Agent works autonomously
    ↓
Agent may spawn sub-agent if needed
    ↓
Synthesize results
```

**Key Principles**:
1. **Minimum agents**: Prefer 1 agent over 2, 2 over 3
2. **Rich guidance**: Each agent gets detailed context about what to do
3. **Sub-agent authority**: Agents can spawn helpers when needed
4. **No user questions** (unless truly ambiguous edge case)

**Question Threshold**: Only ask when:
- Request is truly ambiguous (could mean opposite things)
- Critical information is missing that can't be inferred
- User explicitly asked for options

**Pros**:
- Matches user's "minimum agents" requirement
- Reduces cognitive load on user
- More autonomous operation
- Clean architecture

**Cons**:
- More complex orchestration logic
- Sub-agent spawning adds complexity
- Need to define agent capabilities clearly

**Effort**: Medium-High

### Option B: Smart Gateway Enhancement

**Description**: Enhance existing `/product` gateway with smarter routing logic.

**Changes**:
- Add "minimum agent" heuristic
- Enable agents to call other agents via Task tool
- Reduce clarification prompts

**Pros**:
- Builds on existing architecture
- Lower effort

**Cons**:
- May not achieve "minimum agents" as cleanly
- Gateway already complex

**Effort**: Medium

### Option C: Rule-Based Routing

**Description**: Explicit rules for when to use 1 vs multiple agents.

**Pros**:
- Predictable
- Easy to explain

**Cons**:
- Doesn't scale
- Misses nuance
- Not "intelligent"

**Effort**: Low

### Recommendation: Option A (Orchestrator Pattern)

The user's feedback is clear: they want intelligent, autonomous routing with minimal questioning. The orchestrator pattern provides the cleanest way to achieve this.

**Key Design Decisions**:
1. Orchestrator runs BEFORE any agent spawn
2. Orchestrator outputs: agent(s) to spawn, guidance per agent, confidence level
3. Sub-agents inherit parent context automatically
4. Questions only for true ambiguity (not for choosing between options)

---

## 3. Planning Mode Approach

### User Requirement
> "Don't need separate planning mode - use Claude Code's native planning mode. When building SaaS solution, will need native planning mode."

### Recommendation: Defer Custom Planning Mode

**Rationale**:
- Claude Code already has native planning mode
- Users can invoke it via `--plan` or equivalent
- No need to reinvent
- For future SaaS, we'll need custom planning - but that's Phase 3+

**Action**: Remove any planning mode work from Phase 2 scope.

---

## 4. Context System Scaling Strategy

### User Requirements
> "Make context system MORE SCALABLE. Add indexing capabilities for easy data access by all agents. Easy onboarding: command for new folder/file setup. Auto-capture: Agents should automatically index important folders they encounter. Auto-save: Everything agents create should go to context. Smart filtering: Don't index irrelevant things."

### Option A: Enhanced Markdown + Index Files (Recommended)

**Description**: Keep markdown storage but add structured index files and auto-capture behavior.

**Architecture**:
```
context/
├── index.json              # Master index with metadata
├── documents/
│   ├── index.md           # Document registry
│   └── [documents...]
├── decisions/
│   ├── index.md
│   └── [decisions...]
├── feedback/
│   ├── index.md
│   ├── themes.md
│   └── [feedback...]
├── auto-captured/          # NEW: Auto-indexed content
│   ├── index.json         # Searchable index
│   └── [captured items...]
└── sessions/               # NEW: Session transcripts
    └── [session summaries...]
```

**Auto-Capture Behavior**:
1. **Agent outputs**: Everything agents create → auto-save to context
2. **Important folders**: When agent encounters important folder (e.g., strategy docs), offer to index
3. **Session context**: Key decisions/discussions → session summary

**Indexing**:
```json
{
  "entries": [
    {
      "id": "DOC-2026-001",
      "type": "prd",
      "title": "Authentication PRD",
      "path": "documents/prd-auth.md",
      "topics": ["authentication", "security", "user-identity"],
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

**Smart Filtering Rules**:
- Index: PRDs, decisions, strategies, customer feedback, meeting notes
- Don't index: node_modules, build artifacts, binary files, temporary files

**Pros**:
- Builds on existing markdown system
- Searchable via index
- Human-readable
- Git-friendly

**Cons**:
- Index maintenance overhead
- May need migration for existing contexts

**Effort**: Medium

### Option B: SQLite Backend

**Description**: Replace markdown with SQLite for structured queries.

**Pros**:
- Fast queries
- Proper indexing
- Scales well

**Cons**:
- Not human-readable
- Not git-friendly
- Bigger migration effort
- Overkill for single-user

**Effort**: High

### Option C: Hybrid (Markdown + SQLite Index)

**Description**: Keep markdown files but add SQLite index for fast search.

**Pros**:
- Best of both worlds
- Fast queries + human readable

**Cons**:
- Two systems to maintain
- Sync complexity

**Effort**: Medium-High

### Recommendation: Option A (Enhanced Markdown + Index)

For the Claude Code plugin context (single user, local-first), enhanced markdown with JSON indexes provides the right balance of scalability, readability, and simplicity.

**Key Design Decisions**:
1. Add `index.json` at context root for fast topic lookup
2. Auto-save all agent outputs to appropriate context location
3. Auto-index folders when agents encounter them (with user confirmation)
4. Smart filtering to avoid noise
5. Easy onboarding: `/setup-context` command creates structure

---

## 5. Demo Environment Approach

### User Requirements
> "Ship with pre-existing demo context and files. Let users see system when full of data. Separate demo context + core files + demos. User can investigate plugin capabilities with real data. Easy one-word command to clear demo before first use."

### Option A: Demo-by-Default with Clear Command (Recommended)

**Description**: Plugin ships with demo context populated. User runs `/clear-demo` to reset for production use.

**Structure**:
```
context/
├── demo/                    # Demo context (shipped)
│   ├── decisions/          # Sample decisions
│   ├── bets/               # Sample strategic bets
│   ├── feedback/           # Sample customer feedback
│   └── documents/          # Sample PRDs, roadmaps
├── [production folders]    # User's actual context
```

**Demo Content Includes**:
- 5-10 sample decisions with full structure
- 2-3 strategic bets with assumptions
- 10-15 customer feedback entries with themes
- Sample PRD, roadmap, GTM strategy
- Sample ROI history showing value

**Commands**:
- `/demo-mode` - Switch to viewing demo context
- `/clear-demo` - Remove demo context, keep structure
- `/reset-demo` - Restore demo context (re-download)

**First-Run Experience**:
```
Welcome to Product Org OS!

This plugin ships with demo content so you can explore capabilities.
Try: /context-recall pricing (see demo decisions)
     /portfolio-status (see demo strategic bets)
     /roi-report (see sample ROI data)

Ready to use for real? Run: /clear-demo
```

**Pros**:
- Immediate value visibility
- User can explore before committing
- Easy reset if they want to experiment more
- Shows "full system" experience

**Cons**:
- Slightly larger initial install
- Risk of user confusion (demo vs real)
- Need clear visual indicators

**Effort**: Medium

### Option B: Demo as Separate Profile

**Description**: Demo is a separate "profile" user can switch to.

**Pros**:
- Clean separation
- No risk of mixing

**Cons**:
- More complex UX
- User might never explore demo

**Effort**: Medium-High

### Option C: Interactive Tutorial Instead

**Description**: Guided walkthrough that creates demo content as user follows along.

**Pros**:
- Educational
- User learns by doing

**Cons**:
- Doesn't show "full system"
- Requires user time investment

**Effort**: Medium

### Recommendation: Option A (Demo-by-Default)

The user explicitly wants users to "see system when full of data." Demo-by-default with easy clear command achieves this.

**Key Design Decisions**:
1. Demo context clearly labeled (visual indicator when viewing demo)
2. Demo content is realistic and useful (not lorem ipsum)
3. Single command to clear: `/clear-demo`
4. Demo can be restored: `/reset-demo`
5. Production context never mixes with demo

---

## Summary of Recommendations

| Decision Area | Recommended Option | Effort |
|--------------|-------------------|--------|
| ROI Tracking | Option A: Interaction-Level First | Medium |
| Routing | Option A: Orchestrator Pattern | Medium-High |
| Planning Mode | Defer (use Claude Code native) | None |
| Context Scaling | Option A: Enhanced Markdown + Index | Medium |
| Demo Environment | Option A: Demo-by-Default | Medium |

**Total Phase 2 Scope Impact**:
- Adding: Demo Environment feature
- Changing: ROI (more granular), Routing (orchestrator), Context (indexing)
- Removing: Custom planning mode

**Risk Assessment**:
- Orchestrator routing is the highest-risk change (architectural)
- Demo environment is lowest-risk (additive)
- Context indexing is medium-risk (migration concerns)

---

## Next Steps

1. Update PRD with feedback-aligned requirements
2. Create technical design for orchestrator pattern
3. Design demo content package
4. Create updated presentation

---

*Document prepared by Director of Product Management*
