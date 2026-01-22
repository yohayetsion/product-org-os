---
globs:
  - "**/*"
---

# Context Management Rules

The Context Layer provides organizational memory across sessions and agents. Follow these rules to maintain context integrity.

## Core Behaviors

### After Creating Decisions or Bets

When you complete a `/decision-record` or `/strategic-bet`:

1. **Always offer to save**: "Should I save this to the context registry? (`/context-save`)"
2. If user agrees, run `/context-save` to:
   - Add entry to the appropriate index
   - Extract assumptions to the assumption registry
   - Update portfolio if it's an active bet

### Before Making Decisions

When asked to make or analyze a decision:

1. **Check for prior context**: Run `/context-recall [topic]` to find:
   - Related past decisions
   - Active strategic bets that may constrain choices
   - Relevant assumptions and their status
   - Applicable learnings
2. **Reference findings**: Incorporate relevant context into your analysis
3. **Flag conflicts**: If the new direction might conflict with past decisions, highlight this

### Before Delegating to Another Agent

When you need to invoke another agent for work:

1. **Capture context**: Run `/handoff` to create a briefing document
2. **Include in delegation**: Reference `@context/handoffs/current-session.md` in your delegation prompt
3. **Specify what's inherited**: Make clear what constraints and context the receiving agent should honor

### At Start of Strategic Sessions

When beginning strategic planning or portfolio work:

1. **Check portfolio state**: Run `/portfolio-status` to understand:
   - Current active bets
   - Upcoming checkpoints
   - At-risk assumptions
2. **Align new work**: Ensure proposed work fits within or explicitly changes the portfolio

### After Retrospectives and Outcome Reviews

When completing `/retrospective`, `/outcome-review`, or `/decision-quality-audit`:

1. **Extract learnings**: Offer to save learnings with `/context-save`
2. **Update assumptions**: Mark assumptions as validated or invalidated
3. **Flag re-decisions**: If outcomes trigger re-decision criteria, highlight this

### When Encountering Feedback (MANDATORY)

**ALL agents MUST capture feedback immediately when encountered.** Feedback includes:
- Customer quotes or complaints
- Feature requests from any source
- User research findings
- Sales or support feedback
- Competitive mentions
- Stakeholder input
- Market signals

When you encounter feedback:

1. **Immediately run `/feedback-capture`** - Do not continue without capturing
2. **Record complete metadata**: Source, date, channel, segment, version
3. **Capture verbatim**: Preserve exact words when possible
4. **Analyze and categorize**: Type, sentiment, impact, topics
5. **Make connections**: Link to decisions, bets, assumptions
6. **Check for themes**: Does this reinforce an existing pattern?

### Before Starting Work in an Area

When beginning work on a feature, decision, or analysis:

1. **Check feedback history**: Run `/feedback-recall [topic]` to see what customers have said
2. **Identify patterns**: Look for themes that should inform your work
3. **Note gaps**: If no feedback exists, consider whether to gather some

### V2V Phase Awareness

When working on any initiative:

1. **Identify current phase**: Use `/phase-check [initiative]` to assess:
   - Which V2V phase the work belongs to
   - Whether prerequisites from earlier phases exist
   - What deliverables are expected at this phase
2. **Verify prerequisites**: Before Phase 3 (commitments), ensure Phase 1-2 work exists
3. **Use appropriate skills**: Match skills to the current phase (see `reference/v2v-skill-map.md`)

### Before Major Commitments (Phase 2→3)

When crossing the "point of no return":

1. **Run commitment validation**: Use `/commitment-check [initiative]` to verify:
   - Phase 1 and Phase 2 prerequisites complete
   - Ownership chain is clear
   - Assumptions are explicit
2. **Run principle validators**:
   - `/ownership-map` - Is there single accountability end-to-end?
   - `/customer-value-trace` - Does this trace to customer value?
   - `/collaboration-check` - Were stakeholders consulted?
   - `/scale-check` - Will this work at scale?
3. **Document the commitment**: Save with `/context-save`

### Principle Validation Triggers

Use principle validators at these key points:

| Trigger | Run These Validators |
|---------|---------------------|
| Creating commitments | `/ownership-map`, `/commitment-check` |
| Making decisions | `/customer-value-trace`, `/collaboration-check` |
| Committing resources | `/scale-check` |
| Phase transitions | `/phase-check` |

## Context File Locations

| Content Type | Index Location | Full Records |
|--------------|----------------|--------------|
| Decisions | `context/decisions/index.md` | `context/decisions/[YYYY]/` |
| Strategic Bets | `context/bets/index.md` | `context/bets/[YYYY]/` |
| Assumptions | `context/assumptions/registry.md` | (in registry) |
| Portfolio State | `context/portfolio/active-bets.md` | (in file, includes V2V phase tracking) |
| Learnings | `context/learnings/index.md` | (in index) |
| Handoffs | `context/handoffs/current-session.md` | (overwritten) |
| Feedback | `context/feedback/index.md` | `context/feedback/[YYYY]/` |
| Themes | `context/feedback/themes.md` | (in file) |
| Principles | `context/principles/scorecard.md` | (in file) |

## ID Conventions

- **Decisions**: `DR-[YYYY]-[NNN]` (e.g., DR-2026-001)
- **Strategic Bets**: `SB-[YYYY]-[NNN]` (e.g., SB-2026-003)
- **Assumptions**: `A-[NNN]` (sequential, e.g., A-015)
- **Learnings**: `L-[NNN]` (sequential, e.g., L-042)
- **Feedback**: `FB-[YYYY]-[NNN]` (e.g., FB-2026-001)
- **Themes**: `TH-[NNN]` (sequential, e.g., TH-005)

## Quality Standards

### For Decisions
- Single accountable owner (not a team)
- Measurable success criteria
- Specific re-decision triggers
- Tags for searchability

### For Assumptions
- Clear, testable statement
- Defined validation method
- Validation timeline
- Link to source decision/bet

### For Learnings
- One clear insight per learning
- Evidence supporting the learning
- Guidance on when to apply
- Confidence level

### For Feedback
- Raw feedback captured verbatim
- Complete metadata (source, date, channel, segment)
- Analysis with sentiment and impact assessment
- Categorization with searchable topics
- Connections to decisions, bets, assumptions

### For Themes
- Minimum 3 feedback entries to establish
- Clear pattern description
- Status tracking (Emerging → Established → Addressed)
- Linked supporting feedback

## Maintenance

- **Weekly**: No action needed (indexes are updated on save)
- **Quarterly**: Archive completed/invalidated items
- **Annually**: Move old records to `context/archive/[YYYY]/`

## V2V Operating Principle

> "Organizational memory is a competitive advantage. Document decisions not for bureaucracy, but for learning velocity."

The context layer embodies the V2V learning loop: decisions lead to outcomes, outcomes validate assumptions, validated/invalidated assumptions become learnings, learnings improve future decisions.
