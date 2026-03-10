---
name: interview-synthesis
description: |
  Synthesize customer interview notes or transcripts into themes, patterns, key quotes, and actionable insights. Turns raw research into structured findings.
  Activate when: "interview synthesis", "synthesize interviews", "research findings", "customer interviews", "user research synthesis", "interview notes", "what did we learn"
  Do NOT activate for: feedback capture (/feedback-capture), feedback recall (/feedback-recall)
argument-hint: [interview notes, transcript, or path] or [update path/to/synthesis.md]
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: research
compatibility: Requires Product Org OS v3+ context layer and rules
---

## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "add interviews", "incorporate" in input | UPDATE | 100% |
| File path provided with "update" | UPDATE | 100% |
| "create", "new", "synthesize" in input | CREATE | 100% |
| "find", "search", "list syntheses" | FIND | 100% |
| "the synthesis", "latest research" | UPDATE | 85% |
| Interview notes/transcripts provided directly | CREATE | 90% |

**Threshold**: >=85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Synthesize provided interviews into a complete research findings document.

**UPDATE**:
1. Check document registry first, then search user's structure
2. Preserve existing themes and quotes
3. Integrate new interview data, update pattern counts
4. Show what changed: new themes, strengthened patterns, contradictions
5. Update participant count and coverage metrics

**FIND**: Check registry, then search user's folders for synthesis documents.

### Search Locations

- `{Product}/Product/research/`
- `{Product}/Product/interviews/`
- `context/documents/index.md`
- `context/feedback/`

---

## Vision to Value Phase

**Phase 1: Strategic Foundation** -- Synthesizing customer research into actionable insights that inform strategic decisions and opportunity identification.

## Methodology

### The Synthesis Pipeline

<!-- Source: Thematic analysis methodology from Virginia Braun & Victoria Clarke, "Using Thematic Analysis in Psychology" (2006). Six-phase process: familiarize, generate codes, search themes, review themes, define themes, produce report. Adapted for product management context. -->

<!-- Source: Teresa Torres, "Continuous Discovery Habits" (2021). Weekly interview rhythm, opportunity identification through interview snapshots, and the experience map approach. Key insight: synthesis should happen continuously, not in batches. -->

<!-- Source: Inspired by phuryn/pm-skills `summarize-interview` pattern and Anthropic's knowledge-work-plugins `user-research-synthesis` structure. Also draws from product-on-purpose/pm-skills interview synthesis approach. -->

#### Step 1: Capture Raw Data

For each interview, extract:

| Element | What to Capture |
|---------|----------------|
| **Participant** | Role, segment, tenure, context (anonymize as P1, P2...) |
| **Verbatim quotes** | Exact words, with context. These are gold. |
| **Behaviors** | What they actually DO (not what they say they do) |
| **Pain points** | Frustrations, workarounds, complaints |
| **Goals** | What they're trying to achieve |
| **Surprises** | Anything unexpected or contradicting assumptions |

**Rule**: Preserve exact quotes. Never paraphrase at the capture stage.

#### Step 2: Code the Data

<!-- Source: Affinity diagramming / affinity mapping. Origin: KJ Method (Jiro Kawakita, 1960s). Adapted for product research by Jeff Gothelf & Josh Seiden, "Lean UX" (2013). Group observations by similarity, then name the groups. -->

Tag each observation with codes:

| Code Type | Purpose | Example |
|-----------|---------|---------|
| **Descriptive** | What it's about | "onboarding", "pricing", "reporting" |
| **Emotional** | How they feel | "frustrated", "delighted", "confused" |
| **Behavioral** | What they do | "workaround", "avoidance", "habit" |
| **Evaluative** | Their judgment | "essential", "unnecessary", "broken" |

#### Step 3: Identify Themes

Group coded observations into themes:

- **Strong theme**: 3+ participants mention it independently
- **Emerging theme**: 2 participants mention it
- **Signal**: 1 participant mentions it, but it's notable

<!-- Source: Pattern strength thresholds adapted from Erika Hall, "Just Enough Research" (2013). Hall's pragmatic approach: you don't need statistical significance in qualitative research, but you do need pattern recognition discipline. -->

For each theme, document:
- Theme name and description
- Supporting quotes (verbatim)
- Number of participants who raised it
- Sentiment (positive, negative, neutral, mixed)
- Strength (strong, emerging, signal)

#### Step 4: Extract Insights

<!-- Source: The distinction between observations, patterns, and insights from IDEO's human-centered design methodology. An observation is what you see. A pattern is what recurs. An insight is the "why" that creates design opportunity. Also: Vijay Kumar, "101 Design Methods" (2012). -->

Transform themes into actionable insights:

| Level | Definition | Example |
|-------|-----------|---------|
| **Observation** | What we saw/heard | "3 users mentioned they export data to Excel" |
| **Pattern** | What recurs | "Users don't trust the built-in reporting" |
| **Insight** | Why it matters | "Users need to validate data against their own mental models before sharing with stakeholders" |
| **Opportunity** | What to do | "Build customizable report templates that match existing Excel workflows" |

#### Step 5: Connect to Strategy

<!-- Source: Teresa Torres, "Continuous Discovery Habits" (2021). Opportunity Solution Tree — connect research findings to product opportunities, which connect to desired outcomes, which connect to business objectives. -->

Map insights to:
- Existing assumptions (validate/invalidate from `/assumption-map`)
- Active strategic bets (support/challenge from `/strategic-bet`)
- Opportunity tree branches (from `/opportunity-tree`)
- Known feedback themes (from `/feedback-recall`)

## Output Structure

```markdown
# Interview Synthesis: [Research Topic/Sprint]

**Date**: [YYYY-MM-DD]
**Researcher**: [Name/Role]
**Product**: [Product name]
**Related**: [SB-YYYY-NNN, A-NNN, or initiative name]

## Research Overview

**Interviews conducted**: [N]
**Date range**: [Start] to [End]
**Participant segments**: [Segment 1 (N), Segment 2 (N), ...]
**Research questions**:
1. [Primary question]
2. [Secondary question]
3. [Secondary question]

## Participant Summary

| ID | Segment | Role | Tenure | Key Context |
|----|---------|------|--------|-------------|
| P1 | [Segment] | [Role] | [Time using product/in role] | [Relevant context] |
| P2 | [Segment] | [Role] | [Time] | [Context] |

## Themes

### Theme 1: [Theme Name] -- [Strong/Emerging/Signal]

**Participants**: P1, P3, P5 ([N]/[Total])
**Sentiment**: [Positive / Negative / Neutral / Mixed]

**Key quotes**:
> "Exact quote from participant" -- P1
> "Another exact quote" -- P3

**Observation**: [What we saw]
**Pattern**: [What recurs across participants]
**Insight**: [Why this matters -- the deeper understanding]

### Theme 2: [Theme Name] -- [Strong/Emerging/Signal]

...

## Contradictions & Tensions

| Tension | Side A | Side B | Possible Explanation |
|---------|--------|--------|---------------------|
| [Topic] | [View from some participants] | [Opposing view] | [Why they might differ] |

## Opportunities Identified

| # | Opportunity | From Theme | Confidence | Impact |
|---|------------|------------|------------|--------|
| O-1 | [Opportunity statement] | Theme 1 | High/Med/Low | High/Med/Low |
| O-2 | [Opportunity statement] | Theme 2 | High/Med/Low | High/Med/Low |

## Assumption Validation

| Assumption | Status | Evidence |
|-----------|--------|----------|
| [A-NNN: Assumption text] | Validated / Invalidated / Inconclusive | [What interviews revealed] |

## Recommendations

### Act On (High confidence, high impact)
1. [Recommendation with supporting evidence]

### Investigate Further (Emerging signals)
1. [What needs more research and why]

### Monitor (Weak signals worth tracking)
1. [Signal and what to watch for]

## Raw Quote Bank

[All notable quotes organized by theme, for future reference and stakeholder presentations]

### [Theme 1]
> "Quote" -- P1, [context]
> "Quote" -- P3, [context]

### [Theme 2]
> "Quote" -- P2, [context]

## Methodology Notes

- Interview format: [Structured / Semi-structured / Unstructured]
- Duration: [Average length]
- Recruitment: [How participants were found]
- Known limitations: [Sample bias, missing segments, etc.]
```

## Instructions

1. **Preserve verbatim quotes.** Never paraphrase participant language. Exact words carry meaning that summaries lose.
2. Accept input as: raw notes, transcripts, `@file.md` references, or pasted text. Multiple interviews can be provided at once.
3. Anonymize participants (P1, P2...) unless the user specifies otherwise. Include enough context (segment, role) to make quotes meaningful.
4. Be honest about theme strength. A single mention is a signal, not a theme. Don't over-interpret small samples.
5. The "Contradictions & Tensions" section is critical. Real research always has contradictions. If your synthesis has none, you're not looking hard enough.
6. Connect findings to existing strategic context via `/context-recall` and `/feedback-recall` before finalizing.
7. Run `/feedback-capture` for any strong quotes or insights that should be in organizational memory.
8. Save syntheses to `{Product}/Product/research/` or `{Product}/Product/interviews/`.
9. Offer to create an `/opportunity-tree` from the identified opportunities.
10. When updating an existing synthesis with new interviews, clearly mark what's new vs. what was previously identified.

## Integration

- Feeds from: Raw interview notes/transcripts, `/context-recall` (existing knowledge)
- Feeds into: `/opportunity-tree` (opportunities), `/assumption-map` (validation), `/feedback-capture` (quotes into org memory), `/context-save` (key insights)
- Related to: `/experiment-design` (testing insights), `/prd` (requirements from research)
- Connects to: `/feedback-recall` (finding related existing feedback)

## Vision to Value Operating Principle

> "Customer interviews are the highest-fidelity input a product organization has. A good synthesis turns hours of conversation into minutes of actionable clarity."
