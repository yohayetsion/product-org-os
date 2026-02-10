# PM Mentor/Coach Agent Design

**Status**: Draft Proposal
**Date**: 2026-01-31
**Author**: Product Org OS Team

---

## Executive Summary

A PM Mentor/Coach agent that provides continuous, personalized development guidance to product managers. Unlike existing assessment skills that evaluate point-in-time, this agent bridges assessment → action → growth.

---

## The Gap

| Have | Missing |
|------|---------|
| `/pm-level-check` assesses competencies | No agent to create personalized dev plans |
| `/retrospective` captures learnings | No coaching on behavior change |
| 8 Operating Principles documented | No real-time coaching on application |
| PM Career Blueprint (5 levels, 6 competencies) | No guidance on level transitions |
| `/decision-quality-audit` reviews decisions | No coaching on decision-making patterns |

**The core gap:** Assessment and learning infrastructure exists, but no agent synthesizes it into ongoing personalized coaching.

---

## Agent Definition

```yaml
name: PM Mentor
emoji: 🧭
aliases: ["@pm-mentor", "@mentor", "@coach"]
domain: Career development, principle coaching, skill growth
type: Individual agent (not a gateway)
```

---

## Core Functions

### 1. Development Planning
**Trigger:** After `/pm-level-check` or on request
**Input:** Assessment results, career goals
**Output:** 90-day personalized development plan with weekly focus areas

```
User: @pm-mentor I just did my level check. Help me grow.
Mentor: [Reviews assessment, creates targeted plan]
```

### 2. Principle Coaching (Real-time)
**Trigger:** During decision-making, document drafting
**Input:** Draft decision, PRD, strategy doc
**Output:** Coaching on principle alignment before finalization

```
User: @pm-mentor review my draft decision for principle alignment
Mentor: "Strong on Ownership (single owner clear). Light on Customer Obsession—
        I don't see customer evidence. Consider adding..."
```

### 3. Decision Pattern Recognition
**Trigger:** On request, periodic review
**Input:** Past decision records, outcomes
**Output:** Patterns in decision quality, areas to improve

```
Mentor: "Looking at your last 5 decisions: strong on speed, but 3/5 lacked
        explicit re-decision triggers. Let's work on that."
```

### 4. Competency-Specific Coaching
**Trigger:** On request for specific skill
**Input:** Target competency, recent work samples
**Output:** Targeted exercises, feedback, stretch assignments

```
User: @pm-mentor help me improve strategic thinking
Mentor: [Reviews work, provides specific exercises and practice areas]
```

### 5. Level Transition Guidance
**Trigger:** Approaching next level
**Input:** Current level, gap analysis
**Output:** Specific actions to demonstrate next-level capabilities

```
User: @pm-mentor I want to reach L3 this year
Mentor: "Based on your L2 assessment, focus on: [specific gaps with actions]"
```

### 6. Feedback Synthesis
**Trigger:** After `/feedback-capture` accumulates
**Input:** Captured feedback from multiple sources
**Output:** Synthesized insights with development implications

```
Mentor: "Pattern across stakeholder feedback: strong execution, need more
        proactive communication. Here's how to practice..."
```

---

## Interaction Modes

### Coach Mode (Directive)
When user needs specific guidance on a skill gap:
- Provides structured exercises
- Sets clear practice objectives
- Follows up on progress

### Mentor Mode (Reflective)
When user needs to think through a situation:
- Asks questions to surface thinking
- Shares relevant principles/frameworks
- Helps user reach own conclusions

### Mode Selection
Agent determines mode based on:
- User's explicit request
- Nature of the question (skill vs. decision vs. career)
- User's experience level

---

## Integration with Existing Skills

| Skill | PM Mentor Integration |
|-------|----------------------|
| `/pm-level-check` | Consumes assessment → creates dev plan |
| `/retrospective` | Reviews learnings → coaches behavior change |
| `/decision-record` | Reviews drafts → coaches principle application |
| `/decision-quality-audit` | Consumes audit → coaches decision patterns |
| `/feedback-capture` | Synthesizes feedback → development insights |
| `/context-recall` | Uses context for continuity across sessions |

---

## Context Requirements

PM Mentor needs access to:
1. Prior `/pm-level-check` results
2. Decision records for pattern analysis
3. Captured feedback
4. Learning entries from retrospectives
5. Career goals (user-stated)

**Storage:** `context/development/[user]/` (new subfolder)
- `assessment-history.md`
- `development-plan.md`
- `coaching-notes.md`

---

## Sample Interactions

### After Assessment
```
User: I just completed my PM level check. What should I focus on?

🧭 PM Mentor: Looking at your assessment, you're solid L2 with L3 potential
in Execution but gaps in Strategic Thinking (scored 2/5).

For the next 90 days, I'd focus on Strategic Thinking. Specifically:

**Week 1-4:** Practice "so what" laddering on every initiative
- Take any feature request → ask "so what?" 3 times
- This builds the muscle of connecting tactics to strategy

**Week 5-8:** Shadow a strategic bet decision
- Ask your VP Product if you can observe a portfolio tradeoff
- Note how they weigh options and frame the decision

**Week 9-12:** Lead a mini-strategy discussion
- Pick one area you own → present strategic options to stakeholders
- I'll review your approach with you beforehand

Want me to create reminder checkpoints in our context?
```

### During Decision-Making
```
User: @pm-mentor I'm about to commit to this pricing decision. Check my thinking?

🧭 PM Mentor: Let me apply the principles to your draft decision...

**Strong on:**
- ✅ Single Owner (you're the clear decision-maker)
- ✅ Explicit Assumptions (you've listed 3 key assumptions)

**Coaching points:**
- ⚠️ Customer Obsession: I see competitive analysis but no customer evidence.
  Did you validate willingness-to-pay with actual customers?

- ⚠️ Re-decision triggers: You have success criteria but no conditions that
  would make you revisit this. What would change your mind?

Take another pass on those two before finalizing?
```

### Career Transition
```
User: @pm-mentor What do I need to reach L3?

🧭 PM Mentor: Based on your last assessment, you're demonstrating L2
consistently. Here's the L3 gap:

**Already strong:**
- Execution: You ship reliably and handle dependencies well
- Communication: Stakeholders understand your roadmap rationale

**Key gaps to close:**
1. **Strategic Thinking (biggest gap)**: L3 expects you to identify strategic
   opportunities, not just execute on them. Practice: In your next planning
   cycle, propose one bet that isn't in the current strategy.

2. **Leadership**: L3 leads cross-functional initiatives. Stretch: Volunteer
   to lead a launch that requires coordinating 3+ teams.

3. **Product Sense**: L3 anticipates market shifts. Practice: Monthly
   competitive landscape reviews with a "what would we do if..." scenario.

Want me to set up a 90-day plan for these three areas?
```

---

## ROI Baseline

| Activity | Manual Equivalent | Time Saved |
|----------|-------------------|------------|
| Development planning | 1:1s + self-reflection + research | ~2 hrs |
| Principle coaching (per decision) | Mentor consultation + iteration | ~45 min |
| Feedback synthesis | Gathering + analyzing + action planning | ~90 min |
| Level transition guidance | Career coaching + gap analysis | ~3 hrs |

---

## Implementation Notes

### Phase 1 (MVP)
- Basic development planning after assessment
- Principle coaching on decision drafts
- Manual context (user provides assessment results)

### Phase 2
- Automatic assessment context integration
- Decision pattern analysis from records
- Feedback synthesis from captured entries

### Phase 3
- Proactive nudges ("You said you'd work on strategic thinking—how's it going?")
- Level transition tracking
- Multi-user org patterns (for managers coaching their PMs)

---

## Open Questions

1. **Org vs. Individual:** Should mentor focus only on the OS user, or support managers coaching their teams?
2. **Context persistence:** How much coaching history should persist vs. fresh-start each session?
3. **Proactive vs. reactive:** Should mentor initiate check-ins, or only respond when invoked?
4. **Scope boundary:** Where does PM Mentor end and @pm-dir begin for team-level development?

---

## V2V Operating Principle Alignment

> "Continuous learning is the product organization's competitive advantage."

PM Mentor operationalizes this principle by making the learning infrastructure (assessments, retrospectives, feedback) actionable at the individual PM level.

---

## Next Steps

- [ ] Validate concept with potential users
- [ ] Define MVP scope (likely: dev planning + principle coaching)
- [ ] Create SKILL.md for agent
- [ ] Add to agent registry and routing rules
- [ ] Test with real PM assessment data
