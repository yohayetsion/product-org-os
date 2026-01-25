# Phase 2 Intelligence Enhancements PRD

**Product**: Product Org OS
**Version**: 2.0 (Phase 2B Head Start)
**Date**: 2026-01-24
**Owner**: Product Manager
**Status**: Draft - Revision 2
**V2V Phase**: Phase 3 - Strategic Commitments

---

## 1. Executive Summary

The Phase 2 Intelligence Enhancements bundle delivers three interconnected capabilities that transform the Product Org OS from a "toolkit of skills" into an intelligent operating system. This release introduces: (1) **ROI Tracker** to prove and quantify time-savings, (2) **Enhanced Agent Routing** with semantic intent detection, and (3) **Automatic Context Sharing** that eliminates manual handoffs between agents.

These features directly address the top three user pain points identified in market research:
- "I can't prove the ROI to my CFO"
- "I don't know which agent to invoke"
- "Context doesn't carry between agents"

**Target Launch**: Phase 2B Month 3 (follows Phase 2A validation)

**Key Value Proposition**: Users describe their problem, not diagnose which agent solves it. Context flows automatically. And they can show stakeholders exactly how much time the system saved.

---

## 2. Problem Statement & Opportunity

### The Problems We're Solving

**Problem 1: Invisible ROI**
Product leaders investing time in the Product Org OS cannot quantify the return to stakeholders. When budget conversations happen, they have no data to justify continued investment or team-wide adoption. The CFO asks "what do we get for this?" and the PM shrugs.

**Problem 2: Routing Friction**
Users must memorize 55 skills and 13 agents, then diagnose which one solves their problem. This creates cognitive overhead on every invocation. New users especially struggle - they know WHAT they need but not WHICH agent handles it. The current pattern-based routing requires explicit @agent or /skill invocation.

**Problem 3: Context Loss**
When work spans multiple agents (common for strategic initiatives), context must be manually passed via `/handoff`. Users forget to do this, leading to agents that lack critical context. The result: repeated information, inconsistent outputs, and frustrated users who feel like they're training the system repeatedly.

### Market Opportunity

Based on V2.0 market research:
- 87% of product leaders cite "proving AI ROI" as a top-3 concern
- Time-savings quantification is the #1 missing feature in competing tools
- Context continuity is a major differentiator opportunity - no competitor does this well

### Business Justification

These features directly support V2.0 conversion goals:
- ROI Tracker is the primary **Free → Pro conversion driver** (target: 8% conversion)
- Enhanced Routing reduces onboarding friction, improving **week-over-week retention** (target: 70%+)
- Automatic Context justifies **Team tier pricing** where shared context matters most

### Strategic Alignment

From the V2.0 Product Plan:
> "V2.0 is about removing friction. Users should describe their problem, not diagnose which agent solves it. They shouldn't have to manage context handoffs. And they should be able to show their CFO 'this saved me 40 hours last quarter.'"

---

## 3. Scope

### In Scope

**ROI Tracker**
- Individual user time-savings tracking and reporting
- Skill-level baseline estimates with complexity modifiers
- Personal ROI dashboard with export capabilities
- User calibration for personal estimate adjustments

**Enhanced Agent Routing**
- Natural language intent detection for agent/skill selection
- Confidence-based routing (auto-route vs. clarify)
- User override capability
- Basic routing explanation

**Automatic Context Sharing**
- Topic-based context retrieval within sessions
- Cross-session context persistence for individual users
- Relevance filtering and token budget management
- Context visibility and exclusion controls

### Out of Scope

The following are explicitly **NOT** included in this release:

| Item | Rationale | Potential Future Phase |
|------|-----------|----------------------|
| Team-level ROI aggregation | Requires Team tier infrastructure | Phase 3 |
| ROI comparison across users | Privacy complexity; requires Team tier | Phase 3 |
| ROI targets/goals/gamification | Anti-gamification design principle | Not planned |
| Integration with time-tracking tools (Toggl, Harvest, etc.) | External dependency; limited value | Evaluate Phase 3 |
| Custom baseline creation by users | Complex UX; calibration covers use case | Evaluate based on feedback |
| Routing model fine-tuning/training | Start with Claude native; evaluate later | If accuracy <80% |
| Team/org context sharing | Requires multi-tenancy | Phase 3 |
| Real-time collaborative context | Significant infrastructure | Phase 3+ |
| Automated context cleanup/archival | Nice-to-have; manual for now | Phase 3 |
| Voice/audio input for routing | Different modality | Not planned |

---

## 4. Target Users & Personas

### Primary Persona: The Justifying PM Lead

**Profile**: Senior PM or PM Lead managing 2-5 product areas, reports to VP/CPO
**Pain**: Needs to justify AI tooling spend to skeptical leadership
**Need**: Quantifiable proof of time savings to defend budget
**Job to be Done**: "Show my boss that this tool pays for itself"

### Secondary Persona: The Overwhelmed New User

**Profile**: PM who just installed the plugin, exploring capabilities
**Pain**: Doesn't know which of 55 skills or 13 agents to use
**Need**: Natural language interface that routes intelligently
**Job to be Done**: "Get help with my problem without becoming an expert in this tool"

### Tertiary Persona: The Strategic Operator

**Profile**: Senior PM or VP Product running complex, multi-phase initiatives
**Pain**: Context gets lost when switching between agents
**Need**: Automatic context continuity across agent interactions
**Job to be Done**: "Pick up where I left off without re-explaining everything"

---

## 5. Goals & Success Metrics

| Metric | Target | Timeframe | Measurement Method |
|--------|--------|-----------|-------------------|
| ROI estimate accuracy (user feedback) | 80%+ confirm "accurate" or "close" | T+4 weeks | In-product feedback prompt |
| Routing accuracy (measured by override rate) | 85%+ (override <15%) | T+6 weeks | Log analysis: suggested vs. accepted |
| Explicit `/handoff` invocation reduction | 50% decrease | T+8 weeks | Usage telemetry comparison |
| Time-to-first-value for new users | Decrease by 40% | T+8 weeks | Onboarding completion tracking |
| Free → Pro conversion rate | 8%+ | T+12 weeks | Stripe conversion data |
| NPS improvement | +10 points | T+12 weeks | In-product NPS survey |

---

## 6. Functional Requirements

### Feature 1: ROI Tracker

| ID | Requirement | Priority | Description |
|----|-------------|----------|-------------|
| ROI-001 | Inline time-savings display | Must Have | After each skill execution, display estimated time saved in subtle, single-line format |
| ROI-002 | Time-savings dashboard | Must Have | Aggregate view showing total time saved (30/90 day), top skills, ROI multiple |
| ROI-003 | Skill baseline estimates | Must Have | Pre-configured time estimates per skill (benchmarked from manual equivalents). **Note**: Baselines are initial hypotheses to be validated and refined via user calibration feedback in Phase 2A. |
| ROI-004 | Complexity modifiers | Should Have | Adjust estimates based on output complexity (word count, sections, references) |
| ROI-005 | Export report (PDF/CSV) | Should Have | Generate shareable ROI report for stakeholder presentations |
| ROI-006 | Optional user calibration | Should Have | Allow users to adjust estimates based on their actual experience |
| ROI-007 | Privacy-first local storage | Must Have | ROI data stored locally by default, no cloud transmission without consent |

**Prioritization Rationale**:
- **Must Have**: Core value proposition. Without inline display and dashboard, there's no ROI story. Local storage is non-negotiable for trust.
- **Should Have**: Enhance accuracy and shareability. Export and calibration improve value but aren't blocking.
- **If 30% scope cut**: Drop ROI-004 (complexity modifiers) and ROI-005 (export). Inline display + dashboard + basic estimates still deliver core value. Export can be manual (copy-paste) initially.

### Feature 2: Enhanced Agent Routing

| ID | Requirement | Priority | Description |
|----|-------------|----------|-------------|
| RTR-001 | Natural language intent detection | Must Have | Parse user problem descriptions to determine appropriate agent/skill |
| RTR-002 | Confidence-based routing | Must Have | Three-tier system: >70% auto-route, 40-70% suggest with options, <40% request clarification |
| RTR-003 | User override capability | Must Have | Allow users to reject suggestion and manually specify agent |
| RTR-004 | Pattern + semantic hybrid | Must Have | Enhance (not replace) existing pattern matching with semantic layer |
| RTR-005 | Domain classification | Must Have | Classify requests into domains: strategy, requirements, GTM, operations, etc. |
| RTR-006 | Multi-agent detection | Should Have | Detect when request spans multiple domains and suggest @plt or parallel routing |
| RTR-007 | Learning from overrides | Nice to Have | Track override patterns to improve routing accuracy over time |
| RTR-008 | Routing explanation | Should Have | Briefly explain why a particular agent was suggested |

**Prioritization Rationale**:
- **Must Have**: Natural language routing is the headline feature. Confidence tiers prevent bad auto-routing. Override maintains user control.
- **Should Have**: Multi-agent detection and explanation improve experience but aren't essential for basic routing.
- **Nice to Have**: Learning from overrides is valuable long-term but complex to implement correctly.
- **If 30% scope cut**: Drop RTR-006 (multi-agent detection), RTR-007 (learning), RTR-008 (explanation). Basic routing still works; users can manually invoke @plt.

### Feature 3: Automatic Context Sharing

| ID | Requirement | Priority | Description |
|----|-------------|----------|-------------|
| CTX-001 | Topic-based context retrieval | Must Have | Automatically retrieve relevant context based on current conversation topic |
| CTX-002 | Context relevance filtering | Must Have | Score and filter context by relevance, don't pass everything |
| CTX-003 | Context budget enforcement | Must Have | Limit context to max 10K tokens per agent invocation |
| CTX-004 | Session context inheritance | Must Have | New agent invocations inherit relevant context from current session |
| CTX-005 | Context source attribution | Should Have | Show users what context was shared and from where |
| CTX-006 | Context override | Should Have | Allow users to exclude specific context from sharing |
| CTX-007 | Multi-tenancy foundation | Must Have | Architecture supports future team context isolation |
| CTX-008 | Context summarization | Should Have | Summarize old/long context entries to stay within budget |

**Prioritization Rationale**:
- **Must Have**: Core context sharing functionality. Budget enforcement prevents context pollution. Multi-tenancy foundation avoids Phase 3 rework.
- **Should Have**: Attribution and override improve trust and control. Summarization optimizes token usage.
- **If 30% scope cut**: Drop CTX-005 (attribution), CTX-006 (override), CTX-008 (summarization). Basic context sharing still works; users lose visibility and fine-grained control.

---

## 7. Non-Functional Requirements

### Performance

| Requirement | Target |
|-------------|--------|
| Inline ROI display latency | <100ms after skill completion |
| Routing decision time | <500ms from user input |
| Context retrieval time | <1s for up to 1000 context entries |
| Dashboard load time | <2s for 90-day data |

### Security & Privacy

| Requirement | Description |
|-------------|-------------|
| ROI data locality | Stored locally by default; cloud sync opt-in only |
| Context isolation | No context leakage between users (foundation for multi-tenancy) |
| Telemetry anonymization | Any collected telemetry must be anonymized and aggregated |
| GDPR compliance | Users can export and delete all their data |

### Scalability

| Requirement | Target |
|-------------|--------|
| Context entries | Handle 1000+ entries without degradation |
| Concurrent users | Architecture supports 1000+ users (Phase 3 prep) |
| ROI history | Store 1 year of history per user |

### Accessibility

- ROI dashboard meets WCAG 2.1 AA standards
- Inline displays work with screen readers
- All interactions keyboard-navigable

---

## 8. Constraints & Limitations

### Technical Constraints

| Constraint | Impact | Mitigation |
|------------|--------|------------|
| Claude Code architecture | Must work within existing patterns; no external service dependencies | Design for local-first; leverage Claude native capabilities |
| Local-first requirement | ROI and context data must function offline | Use IndexedDB/file storage; cloud sync optional |
| Token limits | Agent context windows have limits | Budget enforcement (10K tokens); relevance filtering |
| No persistent server | Cannot run background processes | All computation triggered by user actions |

### Business Constraints

| Constraint | Impact | Mitigation |
|------------|--------|------------|
| Phase 2A budget ($25K) | Limited scope for validation MVP | Focus on core validation; defer polish |
| Phase 2B timeline (5 months) | Must ship three features | Staged rollout; feature flags |
| Single developer assumption | No parallel workstreams | Sequential feature development |

### Known Limitations

| Limitation | User Impact | Communication |
|------------|-------------|---------------|
| ROI estimates are approximations | May not match actual time for all users | Use "~" prefix; calibration available |
| Routing accuracy will vary | Some requests will misroute initially | Override always available; learning improves over time |
| Context relevance is heuristic | May include/exclude imperfectly | User can view and override context |
| No team context sharing | Individual users only | Team tier in Phase 3 |

---

## 9. User Stories

### Feature 1: ROI Tracker

#### US-ROI-001: View Inline Time Savings

```
As a product manager
I want to see time-savings estimates after each skill execution
So that I understand the value I'm getting in real-time

Acceptance Criteria:
- Given I complete a skill execution (e.g., /prd)
- When the output is displayed
- Then I see a subtle line: "~3.5 hours saved vs. manual creation"
- And the display uses gray text, positioned after skill output
- And the estimate uses "~" to indicate approximation

Boundary Conditions:
- Empty state: If skill produces no output (error or cancelled), no ROI line displayed
- Error state: If ROI calculation fails, silently skip display (don't interrupt UX)
- Edge case: If baseline doesn't exist for skill, show "Time savings tracked" without estimate
- Edge case: If output is unusually short (<100 chars), apply minimum floor (50% of baseline)
```

#### US-ROI-002: View ROI Dashboard

```
As a product leader
I want to see an aggregate view of time saved
So that I can report ROI to stakeholders

Acceptance Criteria:
- Given I invoke /roi-report
- When the dashboard loads
- Then I see: total time saved (30-day and 90-day views)
- And I see: ROI multiple (time saved / time using plugin)
- And I see: top 5 skills by time saved
- And I see: breakdown by V2V phase
- And the data reflects my actual usage history

Boundary Conditions:
- Empty state: New user with no history sees "No data yet" with guidance on first skill to try
- Error state: If data corrupted, offer to reset with warning about data loss
- Edge case: If only 1 skill used, show that skill without "top 5" framing
- Edge case: If usage is <7 days, show "Early results" caveat
```

#### US-ROI-003: Export ROI Report

```
As a product leader
I want to export an ROI report
So that I can share it with my CFO/stakeholders

Acceptance Criteria:
- Given I'm viewing the ROI dashboard
- When I click "Export Report"
- Then I can choose PDF or CSV format
- And the export includes: summary metrics, skill breakdown, date range
- And the PDF is professionally formatted for presentations

Boundary Conditions:
- Empty state: If no data, export button disabled with tooltip "Complete at least one skill to generate report"
- Error state: If export fails (e.g., disk full), show actionable error message
- Edge case: Very large history (1000+ entries) - show progress indicator, chunk processing
- Edge case: Date range with no activity shows "No activity in selected period" in report
```

#### US-ROI-004: Dismiss Inline Display

```
As a power user who knows the value
I want to optionally hide inline time-savings displays
So that my interface stays clean

Acceptance Criteria:
- Given I prefer not to see inline ROI displays
- When I access settings
- Then I can toggle off "Show time-savings inline"
- And the setting persists across sessions
- And I can still access the full dashboard via /roi-report

Boundary Conditions:
- Error state: If settings storage fails, default to showing (fail-open)
- Edge case: Setting changed mid-session applies immediately
```

### Feature 2: Enhanced Agent Routing

#### US-RTR-001: Describe Problem in Natural Language

```
As a new user unfamiliar with agents
I want to describe my problem in plain language
So that the system routes me to the right agent

Acceptance Criteria:
- Given I type "I need to figure out how to price our new feature"
- When the system processes my input
- Then it detects "pricing" domain
- And suggests: "I'll route this to BizOps and Product Marketing for pricing strategy. Proceed? [Y/n]"
- And if I confirm, the appropriate agent(s) are invoked

Boundary Conditions:
- Empty state: Empty or whitespace-only input prompts "What would you like help with?"
- Error state: If classification service unavailable, fall back to "I couldn't parse that. Try @agent or /skill directly."
- Confidence tie (40%/40%/20%): Present top two options as equal choices: "This could be handled by @bizops (pricing analysis) or @pmm-dir (pricing strategy). Which fits better?"
- Confidence tie (33%/33%/33%): List all three: "I see multiple options: [list]. Can you tell me more about what you're trying to accomplish?"
- Edge case: Very short input (<3 words) triggers clarification request
- Edge case: Input contains explicit @agent - use that, don't re-route
```

#### US-RTR-002: Automatic High-Confidence Routing

```
As a returning user
I want clear requests to route automatically
So that I don't have to confirm obvious choices

Acceptance Criteria:
- Given I type "create a PRD for the authentication feature"
- When confidence is >70% for a single agent
- Then the system routes directly to @pm without asking
- And shows: "Routing to Product Manager for PRD creation..."
- And the agent begins work immediately

Boundary Conditions:
- Empty state: N/A (requires input)
- Error state: If agent spawn fails, show error and suggest manual invocation
- Edge case: Confidence exactly 70% - treat as auto-route (threshold is inclusive)
- Edge case: Two agents both >70% (e.g., 75% and 72%) - treat as medium confidence, ask for clarification between the two
- Edge case: Auto-route disabled in settings - always show confirmation
```

#### US-RTR-003: Override Routing Suggestion

```
As an experienced user
I want to override the system's routing suggestion
So that I maintain control over agent selection

Acceptance Criteria:
- Given the system suggests "Routing to @pm..."
- When I want a different agent
- Then I can type "no, use @vp-product" or press 'n'
- And the system routes to my specified agent instead
- And the override is logged for routing improvement

Boundary Conditions:
- Error state: If override target doesn't exist, show "Agent not found. Available: [list]"
- Edge case: Override to same agent that was suggested - proceed normally
- Edge case: Override during auto-route (>70%) - respect override, log for analysis
```

#### US-RTR-004: Ambiguous Request Clarification

```
As a user with a complex request
I want the system to ask clarifying questions
So that I get routed correctly

Acceptance Criteria:
- Given I type "help me with the launch"
- When the system confidence is 40-70%
- Then it asks: "I see a few options: Launch planning (@prod-ops), GTM strategy (@pmm-dir), or Launch readiness checklist (/launch-readiness). Which fits best?"
- And I can select or provide more context
- And it routes based on my response

Boundary Conditions:
- Error state: If user's clarification is still ambiguous after 2 rounds, offer: "Let's try a specific command. Would you like to see available options?"
- Edge case: User responds with number ("2") - interpret as selection from list
- Edge case: User responds with new context - re-analyze with additional context
- Edge case: User responds "all of them" for multi-domain - route to @plt
```

#### US-RTR-005: Understand Routing Rationale

```
As a learning user
I want to understand why a particular agent was chosen
So that I can learn the system's capabilities

Acceptance Criteria:
- Given the system routes my request
- When I ask "why this agent?" or it's my first time
- Then it explains: "Product Manager handles requirements and PRDs. For pricing, I'd route to BizOps."
- And the explanation is brief (1-2 sentences)

Boundary Conditions:
- Error state: If explanation generation fails, skip (non-critical feature)
- Edge case: Multi-agent routing - explain each agent's role briefly
```

### Feature 3: Automatic Context Sharing

#### US-CTX-001: Automatic Context Inheritance

```
As a user working on a multi-step initiative
I want new agent invocations to automatically receive relevant context
So that I don't have to repeat myself

Acceptance Criteria:
- Given I've been discussing "Q3 pricing strategy" with @bizops
- When I then invoke @pmm-dir for GTM planning
- Then @pmm-dir automatically receives relevant context about the pricing discussion
- And @pmm-dir references this context in their response: "Based on the pricing direction you discussed earlier..."

Boundary Conditions:
- Empty state: No prior context - agent proceeds normally without context injection
- Error state: Context retrieval fails - proceed without context, log error
- Context contradiction: If prior context contains decisions that conflict with current request, agent should note: "I see context from earlier suggesting X, but you're now asking about Y. Should I proceed with Y or reconcile these?"
- Edge case: Very old context (>30 days) - include with lower relevance weight, note age
- Edge case: Context from different product (multi-product org) - apply product filter
```

#### US-CTX-002: View Shared Context

```
As a user who wants transparency
I want to see what context was shared with an agent
So that I understand what they know

Acceptance Criteria:
- Given an agent receives automatic context
- When I ask "what context did you receive?" or expand a "Context" disclosure
- Then I see: list of context sources (e.g., "DR-2026-015: Pricing Decision", "Session: Q3 pricing discussion")
- And for each, I see: source, date, relevance score

Boundary Conditions:
- Empty state: No context shared - show "No prior context was used for this response"
- Error state: Context metadata missing - show source without score
- Edge case: Many context sources (>10) - show top 10, offer "show all"
```

#### US-CTX-003: Exclude Specific Context

```
As a user with sensitive context
I want to exclude specific items from sharing
So that I control what agents see

Acceptance Criteria:
- Given I'm about to invoke an agent
- When I want to exclude context
- Then I can say "without context from [topic/decision]"
- Or I can access context settings to exclude specific items
- And the excluded context is not shared with the agent

Boundary Conditions:
- Error state: Exclusion pattern doesn't match anything - warn "No matching context found to exclude"
- Edge case: Exclude all context - proceed with no context, confirm "Proceeding without prior context"
- Edge case: Excluded context is highly relevant - proceed with exclusion (user intent overrides relevance)
```

#### US-CTX-004: Context Relevance Filtering

```
As a user
I want only relevant context shared
So that agents aren't overwhelmed with irrelevant information

Acceptance Criteria:
- Given I have 50+ decisions/bets in my context store
- When I invoke an agent about "authentication"
- Then only context related to authentication, security, or user identity is shared
- And unrelated context (e.g., pricing decisions) is filtered out
- And total shared context stays under 10K tokens

Boundary Conditions:
- Empty state: No relevant context found - proceed with no injection
- Error state: Relevance scoring fails - fall back to recency-based selection
- Edge case: All context scores below threshold - inject nothing, note "No directly relevant prior context found"
- Edge case: Single high-relevance item exceeds budget - summarize and include
```

#### US-CTX-005: Cross-Session Context Persistence

```
As a user returning after a break
I want relevant context from previous sessions
So that I can pick up where I left off

Acceptance Criteria:
- Given I worked on "API strategy" yesterday
- When I return today and mention "API"
- Then relevant context from yesterday's session is retrieved
- And I see: "Continuing from your previous API strategy work..."
- And the agent has the relevant prior context

Boundary Conditions:
- Empty state: No prior sessions on topic - proceed normally
- Error state: Session storage corrupted - log, proceed without (graceful degradation)
- Edge case: Prior session was with different agent - context still shared if relevant
- Edge case: Topic mentioned casually vs. as main focus - weight by usage intensity
```

---

## 10. Design Requirements

### UX Principles

1. **Subtle, Not Intrusive**: ROI displays should inform, not distract. Gray text, positioned after content.
2. **Progressive Disclosure**: Show summary first, details on demand (context sources, routing rationale).
3. **User Control**: Every automatic behavior has an override. Users are never locked out of manual control.
4. **Transparency**: Users can always see what the system "knows" and why it made decisions.
5. **Anti-Gamification**: Frame ROI as "investment recovery," not scores or achievements.

### Key User Flows

#### Flow 1: First-Time User with Natural Language

```
User types: "I need help figuring out our pricing"
  ↓
System: Semantic analysis detects "pricing" domain
  ↓
System: Checks confidence (75% - above threshold)
  ↓
System: "I'll route this to BizOps for pricing analysis. [Proceed]"
  ↓
User confirms
  ↓
@bizops receives request + any relevant context
  ↓
@bizops responds with pricing analysis
  ↓
Inline: "~2.5 hours saved vs. manual analysis"
```

#### Flow 2: Multi-Agent Strategic Work

```
User: @plt "Should we pursue the enterprise tier?"
  ↓
System: Detects PLT gateway, spawns multiple agents
  ↓
Context bus: Retrieves relevant decisions (pricing), bets (enterprise), feedback
  ↓
Each agent receives filtered, relevant context automatically
  ↓
Agents respond with context-informed perspectives
  ↓
Meeting Mode synthesis
  ↓
Inline: "~6 hours saved vs. coordinating this meeting manually"
```

#### Flow 3: ROI Dashboard Review

```
User: /roi-report
  ↓
Dashboard loads with 90-day data
  ↓
Shows: "142 hours saved | ROI: 12x | Top skill: /prd (48 hours)"
  ↓
User clicks "Export"
  ↓
PDF generated with stakeholder-ready formatting
```

### Wireframe References

- ROI inline display: Single line, 12px gray text, positioned below skill output
- ROI dashboard: Card-based layout, primary metric prominent, breakdown secondary
- Routing suggestion: Inline prompt with clear [Y/n] options
- Context disclosure: Expandable section showing context sources

### Design System Components

- Use existing inline notification patterns for ROI display
- Dashboard follows standard metric card patterns
- Routing prompts use existing confirmation dialog patterns

---

## 11. Technical Considerations

### Architecture Implications

#### ROI Tracker

**Data Model**:
```
ROI_Event {
  id: uuid
  timestamp: datetime
  skill: string
  estimated_hours_saved: float
  complexity_factors: json (word_count, sections, references)
  user_calibration: float (optional multiplier)
}
```

**Storage**:
- MVP: Local storage (IndexedDB or file-based)
- Phase 3: Cloud sync with user consent

**Estimation Engine**:
```
base_estimate = skill_baseline_hours[skill]
adjusted_estimate = base_estimate * complexity_modifier(output)
display_estimate = adjusted_estimate * user_calibration (if set)
```

#### Enhanced Agent Routing

**Approach**: Hybrid pattern + semantic

1. **Pattern Layer** (existing): Keyword detection, @mentions, /commands
2. **Semantic Layer** (new): Intent classification using embeddings

**Implementation Options**:
- Option A: Fine-tuned sentence-transformer model on agent domain vocabulary
- Option B: Few-shot classification using Claude's native capabilities
- Recommendation: Start with Option B (lower complexity), evaluate Option A if accuracy <80%

**Confidence Scoring** (aligned with requirements):
```
confidence = max(domain_scores)
if confidence > 0.7:
    route_automatically()
elif confidence > 0.4:
    ask_clarification(top_options)  # Show top 2-3 options
else:
    request_more_context()  # Ask user to elaborate
```

**Tie-Breaking**:
- If top two scores within 5% of each other, present both as options
- If three or more within 10% of each other, ask for clarification

**Fallback**: If semantic layer fails, fall back to pattern matching + user clarification

#### Automatic Context Sharing

**Context Bus Architecture**:
```
Request → Topic Extraction → Context Query → Relevance Scoring → Token Budgeting → Agent Invocation
```

**Relevance Scoring**:
- Topic match (keyword overlap): 40%
- Recency: 30%
- Type priority (decision > bet > learning): 20%
- Explicit references: 10%

**Token Budget Management**:
```
MAX_CONTEXT_TOKENS = 10000
context_items.sort_by(relevance_score, descending)
included_context = []
total_tokens = 0
for item in context_items:
    if total_tokens + item.tokens < MAX_CONTEXT_TOKENS:
        included_context.append(item)
        total_tokens += item.tokens
    else:
        break
```

**Multi-Tenancy Foundation**:
- Context storage keyed by tenant_id (user_id for now, org_id in Phase 3)
- Query layer enforces tenant isolation
- No cross-tenant queries possible at the data layer

### Integration Requirements

| System | Integration |
|--------|-------------|
| Context Layer | Read/write to existing context markdown files |
| Skill Execution | Hook into skill completion to log ROI events |
| Agent Spawning | Inject context into agent prompts |
| Claude API | Leverage native classification capabilities for routing |

### Data Requirements

**ROI Data**:
- Skill execution logs with timestamps
- Output metrics (word count, section count)
- User calibration preferences

**Routing Data**:
- Request → agent mapping (for training/evaluation)
- Override events (for accuracy measurement)
- Clarification patterns (for improvement)

**Context Data**:
- Existing context layer (decisions, bets, learnings, feedback)
- Session transcript summaries
- Topic index for fast retrieval

### Migration Path

**Existing Context Data**:
- No migration required - existing context markdown files are read-compatible
- New metadata fields (relevance scores, topic tags) added non-destructively
- First-time use triggers background indexing of existing context (progress indicator shown)

**User Settings**:
- New settings initialized with sensible defaults
- No action required from users

**Historical Data**:
- No ROI history exists pre-launch - clean start
- Context layer data preserved and enhanced

### Build vs Buy

| Component | Decision | Rationale |
|-----------|----------|-----------|
| Semantic Classification | Build (leverage Claude) | Claude's native capabilities sufficient; no external model needed |
| ROI Storage | Build (local-first) | Simple data model; no benefit from external service |
| Context Retrieval | Build (enhance existing) | Already have context layer; enhance, don't replace |

---

## 12. Dependencies

### Internal Dependencies

| Dependency | Owner | Status | Risk |
|------------|-------|--------|------|
| Context Layer (markdown storage) | Director PM | Complete | Low |
| Skill execution hooks | Director PM | Needs enhancement | Medium |
| Agent spawning mechanism | Director PM | Complete | Low |
| Phase 2A SaaS infrastructure | Director PM | In progress | Medium |

### External Dependencies

| Dependency | Owner | Status | Risk |
|------------|-------|--------|------|
| Claude API | Anthropic | Stable | Low |
| Local storage APIs | Browser/Node | Stable | Low |

### Third-Party Integrations

None required for MVP. Future: optional cloud sync for Team tier.

---

## 13. Timeline & Milestones

### Phase Split: 2A vs 2B

#### Phase 2A: Validation MVP (8 weeks, $25K)

**Scope**: Minimal viable features to validate core hypotheses before full investment.

| Feature | Phase 2A Scope | What's Deferred to 2B |
|---------|----------------|----------------------|
| ROI Tracker | Inline display + basic dashboard (no export) | Export, calibration, complexity modifiers |
| Routing | Intent detection + clarification (no auto-route) | Auto-routing, learning, explanation |
| Context | Session context inheritance only | Cross-session, attribution, override |

**2A Success Criteria** (must validate before 2B investment):
- [ ] ROI estimates: 80%+ users confirm "roughly accurate"
- [ ] Routing: 80%+ requests correctly classified (with clarification allowed)
- [ ] Context: Measurable reduction in repeated information

**2A Deliverables**:
- Working inline ROI display with 10 skill baselines
- Basic routing with clarification prompts (no auto-route)
- Session context passing between agents
- 10 beta user feedback collection

#### Phase 2B: Full Build (5 months, $100K)

**Scope**: Complete feature set with polish, based on 2A learnings.

| Feature | Phase 2B Additions |
|---------|-------------------|
| ROI Tracker | Export (PDF/CSV), complexity modifiers, user calibration |
| Routing | Confidence-based auto-routing, learning from overrides, explanation |
| Context | Cross-session persistence, attribution, user override |
| Polish | Performance optimization, accessibility audit, documentation |

### Detailed Timeline

| Phase | Week | Milestone | Deliverable | Buffer Notes |
|-------|------|-----------|-------------|--------------|
| **2A** | 1 | PRD Approved | This document signed off | |
| **2A** | 2 | Technical Design | Architecture doc, API contracts | |
| **2A** | 4-5 | ROI Inline Display | Working inline display after skill execution | +1 week buffer |
| **2A** | 6-7 | Basic Routing | Intent detection with clarification prompts | +1 week buffer |
| **2A** | 8-9 | Session Context | Context inheritance within session | +1 week buffer |
| **2A** | 10 | 2A Complete + Beta | MVP features testable, beta recruitment | |
| *Checkpoint* | 11-12 | **2A Validation** | User feedback analysis, go/no-go for 2B | **Critical gate** |
| **2B** | 13-14 | ROI Dashboard | Aggregate view with export | |
| **2B** | 15-16 | Enhanced Routing | Confidence scoring, auto-route | |
| **2B** | 17-18 | Cross-Session Context | Persistent context retrieval | |
| **2B** | 19-20 | Calibration + Learning | User calibration, routing learning | |
| **2B** | 21-22 | Attribution + Override | Context visibility and control | |
| **2B** | 23-24 | Polish | Performance, accessibility, edge cases | |
| **2B** | 25-26 | User Testing | Feedback from 20+ beta users | |
| **2B** | 27-28 | Launch Prep | Documentation, rollout, monitoring | |

**Total: 28 weeks** (vs. original 16 weeks - added 12 weeks of buffer and explicit 2A/2B split)

### Checkpoint Criteria

**2A → 2B Gate** (Week 11-12):
- ROI accuracy validated (80%+ "accurate" feedback)
- Routing classification accuracy measured (80%+ correct)
- Context inheritance working without critical bugs
- No fundamental architecture issues discovered
- Stakeholder approval to proceed

If checkpoint criteria NOT met:
- Extend 2A by 4 weeks for fixes
- Re-evaluate 2B scope based on learnings
- Worst case: pivot or descope significantly

---

## 14. Rollout Strategy

### Feature Flags

All features launch behind feature flags for controlled rollout:

| Flag | Controls | Default |
|------|----------|---------|
| `roi_inline_display` | Inline time-savings display | OFF |
| `roi_dashboard` | /roi-report command availability | OFF |
| `routing_semantic` | Semantic intent detection | OFF |
| `routing_autoroute` | Automatic high-confidence routing | OFF |
| `context_session` | Session context inheritance | OFF |
| `context_crosssession` | Cross-session context | OFF |

### Rollout Phases

**Phase R1: Internal (Week 25)**
- Enable all flags for internal team
- 1 week of dogfooding
- Bug fixes and adjustments

**Phase R2: Beta Users (Week 26-27)**
- Enable for 20 opted-in beta users
- Collect structured feedback
- Monitor for issues

**Phase R3: Gradual Rollout (Week 27-28)**
- Enable ROI features for all Pro users (least risky)
- Enable routing for 25% → 50% → 100% over 1 week
- Enable context features for 25% → 50% → 100% over 1 week

**Phase R4: General Availability (Week 28)**
- All features enabled for all users
- Blog post / changelog announcement
- Documentation updated

### Rollback Triggers

Immediate rollback if:
- Error rate >5% for any feature
- User-reported critical bugs >3 in 24 hours
- Performance degradation >50% from baseline
- Security concern identified

---

## 15. Telemetry & Analytics Plan

### ROI Tracker Events

| Event | Trigger | Data Collected |
|-------|---------|----------------|
| `roi.skill_completed` | After skill execution | skill_name, estimated_hours (anonymized), has_calibration |
| `roi.dashboard_viewed` | /roi-report invoked | date_range_selected |
| `roi.export_generated` | Export clicked | format (pdf/csv) |
| `roi.inline_dismissed` | User hides inline | method (setting vs. X) |
| `roi.calibration_set` | User adjusts calibration | direction (up/down), magnitude_bucket |

### Routing Events

| Event | Trigger | Data Collected |
|-------|---------|----------------|
| `routing.request_classified` | Intent detection complete | confidence_bucket (high/med/low), domain_detected |
| `routing.auto_routed` | Automatic routing occurred | confidence_bucket, agent_target |
| `routing.clarification_shown` | Clarification prompt shown | num_options, user_response_type |
| `routing.override` | User overrode suggestion | suggested_agent, chosen_agent, was_autoroute |
| `routing.fallback` | Fell back to pattern matching | reason |

### Context Events

| Event | Trigger | Data Collected |
|-------|---------|----------------|
| `context.retrieved` | Context injected into agent | num_items, total_tokens, relevance_score_avg |
| `context.viewed` | User viewed context disclosure | num_items_shown |
| `context.excluded` | User excluded context | exclusion_type (topic/specific) |
| `context.contradiction_detected` | Conflicting context identified | resolution (user_chose/agent_reconciled) |

### Privacy & Anonymization

- No PII in telemetry
- No actual content/text captured
- User IDs hashed before transmission
- Aggregated daily, raw data deleted after 30 days
- Users can opt out entirely

### Dashboards (Internal)

| Dashboard | Purpose | Key Metrics |
|-----------|---------|-------------|
| ROI Health | Monitor estimate accuracy | Calibration rate, feedback scores |
| Routing Performance | Monitor accuracy | Override rate, clarification rate, fallback rate |
| Context Quality | Monitor relevance | Avg relevance score, exclusion rate |
| Feature Adoption | Track usage | DAU per feature, feature retention |

---

## 16. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| ROI estimates feel inaccurate to users | Medium | High | Conservative baselines; user calibration; "~" prefix to signal approximation |
| Routing accuracy below 85% | Medium | High | Fallback to clarification; hybrid approach; golden dataset for evaluation |
| Context retrieval too slow | Low | Medium | Token budget limits; relevance filtering; lazy loading |
| Users feel "watched" by ROI tracking | Low | Medium | Local-first default; clear privacy messaging; opt-out for inline |
| Routing overrides hurt UX | Medium | Medium | Learn from overrides; don't route if confidence <70%; always allow override |
| Context pollution (irrelevant context shared) | Medium | Medium | Aggressive relevance scoring; token budget; user override capability |
| Phase 3 multi-tenancy requires rework | Low | High | Design context bus with tenant_id from day 1; architect for isolation |
| Timeline slippage | Medium | Medium | Buffer weeks built in; 2A/2B gate allows scope adjustment |
| 2A validation fails | Low | High | Clear success criteria; early feedback; pivot options defined |

---

## 17. Appendices

### Appendix A: Skill Baseline Time Estimates

**Note**: These baselines are initial hypotheses based on benchmarking against manual equivalents. They will be validated and refined through user calibration feedback in Phase 2A. Expect 20-30% of estimates to require adjustment based on real-world usage.

| Skill | Baseline (hours) | Confidence | Rationale |
|-------|------------------|------------|-----------|
| /prd | 4-6 | Medium | Full PRD manually: research, write, review |
| /strategic-bet | 3-5 | Medium | Strategy work requires significant thought |
| /decision-record | 1-2 | High | Documentation of existing decision |
| /user-story | 0.5-1 | High | Single story with acceptance criteria |
| /business-case | 4-6 | Medium | Financial analysis, market research |
| /competitive-analysis | 2-4 | Medium | Competitor research and synthesis |
| /launch-plan | 3-5 | Medium | Cross-functional coordination planning |
| /gtm-strategy | 5-8 | Low | Comprehensive go-to-market planning |
| /market-analysis | 4-6 | Low | Market sizing, segmentation |
| /pricing-strategy | 3-5 | Medium | Pricing research and modeling |

**Confidence Levels**:
- **High**: Based on direct benchmarking or strong user research
- **Medium**: Based on PM judgment and comparable tasks
- **Low**: Rough estimate, needs validation

*Full skill baseline table (55 skills) to be completed in Technical Design*

### Appendix B: Domain Classification Taxonomy

| Domain | Keywords/Signals | Primary Agent | Backup Agents |
|--------|------------------|---------------|---------------|
| Strategy | vision, strategy, bet, direction | @vp-product | @cpo |
| Requirements | PRD, feature, user story, spec | @pm | @pm-dir |
| Pricing | pricing, price, monetization, revenue model | @bizops | @pmm-dir |
| GTM | launch, go-to-market, positioning, messaging | @pmm-dir | @pmm |
| Competitive | competitor, competitive, market share | @ci | @pmm-dir |
| Operations | process, launch readiness, coordination | @prod-ops | @pm-dir |
| Customer | customer success, onboarding, value | @value-realization | @pm |
| Multi-stakeholder | tradeoff, portfolio, prioritization | @plt | @cpo |

### Appendix C: Related Documents

- [V2.0 Product Plan](v2-product-plan.md) - Strategic context and phasing
- [V2.0 Market Research Assessment](v2-market-research-assessment.md) - User research findings
- [Context Management Rules](../../.claude/rules/context-management.md) - Current context layer design
- [Skill Awareness](../../.claude/rules/skill-awareness.md) - Current routing patterns

### Appendix D: Success Criteria Checklist

**Before Launch**:
- [ ] ROI estimates validated with 10+ users (80%+ confirm accuracy)
- [ ] Routing accuracy tested with 200+ query golden dataset (85%+ correct)
- [ ] Context retrieval tested with 1000+ context entries (<2s response)
- [ ] Privacy review complete (no PII in telemetry)
- [ ] User documentation updated
- [ ] Accessibility audit passed (WCAG 2.1 AA)

**At Launch**:
- [ ] Inline ROI display enabled by default
- [ ] Routing suggestions active for natural language inputs
- [ ] Session context sharing active
- [ ] /roi-report skill available
- [ ] Feature flags ready for quick rollback

**Post-Launch (T+4 weeks)**:
- [ ] In-product feedback collected
- [ ] Override rate measured
- [ ] Retention impact measured
- [ ] Telemetry dashboards operational

---

## Document Control

**Created**: 2026-01-24
**Last Updated**: 2026-01-24
**Version**: 2.0
**Status**: Draft

**Revision History**:
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-01-24 | PM | Initial draft |
| 2.0 | 2026-01-24 | PM | Director PM feedback: added Out of Scope, edge cases, 2A/2B split, prioritization rationale, constraints, rollout strategy, telemetry plan, timeline buffer |

**Reviewers**:
- Director of Product Management
- VP Product
- UX Lead

**Approval History**:
| Version | Date | Approver | Notes |
|---------|------|----------|-------|
| 1.0 | TBD | Director PM | Initial approval |
| 2.0 | TBD | Director PM | Revised approval |

---

*End of PRD*
