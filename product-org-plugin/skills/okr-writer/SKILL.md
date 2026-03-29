---
name: okr-writer
description: |
  Write and review OKRs (Objectives and Key Results) with quality checks, anti-pattern detection, and alignment mapping.
  Activate when: "OKR", "objectives and key results", "write OKRs", "review OKRs", "quarterly objectives", "key results", "OKR review", "goal setting"
  Do NOT activate for: north star metric (/north-star-metric), commitment check (/commitment-check), roadmap planning (/product-roadmap)
argument-hint: [team or initiative name] or [update path/to/okrs.md]
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: strategy
compatibility: Requires Product Org OS v3+ context layer and rules
---

## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "revise", "score", "grade" in input | UPDATE | 100% |
| File path provided (`@path/to/okrs.md`) | UPDATE | 100% |
| "create", "new", "write OKRs", "draft OKRs" in input | CREATE | 100% |
| "find", "search", "list OKRs" | FIND | 100% |
| "review OKRs", "check OKRs", "grade OKRs" | UPDATE | 90% |
| "the OKRs", "our OKRs", "Q[N] OKRs" | UPDATE | 85% |
| Just team or initiative name | CREATE | 60% |

**Threshold**: >=85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Generate complete OKR set with objectives, key results, quality review, alignment map, and cadence plan using template below.

**UPDATE**:
1. Read existing OKR document (search if path not provided)
2. If "review" or "score" detected: run quality checklist against existing OKRs, flag issues
3. If "update" detected: preserve structure, update specific objectives or key results
4. Show diff summary: "Updated: [sections]. Unchanged: [sections]." or "Review: [N] issues found."
5. Note: Mid-quarter OKR changes should be documented with rationale

**FIND**:
1. Search paths below for OKR documents
2. Present results: title, team/quarter, objective count, path
3. Ask: "Update one of these, or create new?"

### Search Locations for OKRs

- `strategy/`
- `okrs/`
- `planning/`
- `product/`

---
## Gotchas

- Key Results must be outcomes, never tasks -- "Launch feature X" is a task; "Increase activation rate from X% to Y%" is a KR
- Aspirational OKRs scoring 1.0 consistently means the bar is too low -- 0.7 is the target for stretch goals
- OKRs are NOT a task list or project plan -- they define where you want to end up, not how to get there
- Avoid more than 3-5 objectives per team per quarter -- focus beats coverage



Write, review, or score **OKRs (Objectives and Key Results)**: craft well-formed objectives (qualitative, inspirational, time-bound) and key results (quantitative, measurable, ambitious), with quality review and anti-pattern detection.

## Vision to Value Phase

**Phase 1: Strategic Foundation** - OKRs translate strategic intent into measurable quarterly goals that align the organization around outcomes.

**Prerequisites**: Strategic intent or vision defined (Phase 1), or roadmap priorities set (Phase 3)
**Outputs used by**: Phase 3 (roadmap alignment, commitment check), Phase 5 (outcome measurement against OKR targets), Phase 6 (OKR scoring feeds retrospectives)

## Methodology

<!-- Source: OKR methodology -- Andy Grove, Intel (~1970s). Popularized by John Doerr, "Measure What Matters: How Google, Bono, and the Gates Foundation Rock the World with OKRs" (2018, Portfolio/Penguin). Doerr learned OKRs from Grove at Intel and introduced them to Google in 1999. -->

<!-- Source: joelparkerhenderson/objectives-and-key-results -- comprehensive OKR reference with examples, templates, and anti-patterns. -->

<!-- Source: awesome-okr (GitHub) -- curated list of OKR resources. -->

<!-- Source: Committed vs Aspirational -- Christina Wodtke, "Radical Focus" (2016). Wodtke distinguishes between committed OKRs (must hit 100%, fully resourced, failure = postmortem) and aspirational OKRs (stretch goals, 70% = strong performance, signal innovation ambition). Google uses both types. -->

<!-- Source: OKR scoring -- Google's internal OKR system uses a 0.0-1.0 scale. Scoring 0.7-1.0 on aspirational OKRs = green. Consistently scoring 1.0 = sandbagging. Scoring below 0.4 = reassess scope or resourcing. -->

### Objective Rules

| Rule | Description | Test |
|------|-------------|------|
| **Qualitative** | Objectives describe a desired outcome in words, not numbers | Does it read like an aspiration, not a metric? |
| **Inspirational** | Motivates the team toward meaningful change | Would a team rally around this? |
| **Time-bound** | Has a clear deadline (usually quarterly) | Is the timeframe explicit? |
| **Actionable** | The team can influence the outcome | Is it within the team's sphere of influence? |
| **Concise** | Fits in one line, easy to remember | Can you say it in one sentence? |
| **3-5 per team** | Enough to cover priorities; few enough to focus | Count them. More than 5 = diluted focus. |

### Key Result Rules

| Rule | Description | Test |
|------|-------------|------|
| **Quantitative** | Has a number -- a target value with a starting value | Is there a measurable number? |
| **Measurable** | Can be verified with data at the end of the quarter | Do you have a data source? |
| **Ambitious** | Stretch but achievable -- not sandbagged, not impossible | Is 70% achievement realistic but challenging? |
| **Outcome-based** | Describes an end state, not an activity or output | Is it an outcome or a task? |
| **2-4 per Objective** | Enough to cover the objective; few enough to focus | Count them. |
| **Independently valuable** | Each KR delivers value even if others are missed | Does each KR stand alone? |

### Committed vs Aspirational OKRs

| Type | Expectation | Scoring Target | Failure Response | Resource Commitment |
|------|------------|---------------|-----------------|---------------------|
| **Committed** | Must achieve 100% | 1.0 | Postmortem required | Fully resourced |
| **Aspirational** | Stretch goal | 0.7 = strong | Learning opportunity | May need additional resources |

### OKR Scoring (0.0 - 1.0)

| Score Range | Meaning | Signal |
|-------------|---------|--------|
| 0.0 - 0.3 | Failed to make meaningful progress | Scope was wrong, blocked, or under-resourced |
| 0.4 - 0.6 | Progress but fell short | Good effort, execution challenges |
| 0.7 - 0.8 | Strong delivery (aspirational target) | Sweet spot for stretch goals |
| 0.9 - 1.0 | Fully achieved | Great for committed; sandbagging risk for aspirational |

### Anti-Pattern Detection

| Anti-Pattern | Description | Fix |
|-------------|-------------|-----|
| **Binary KR** | "Launch feature X" (yes/no, not measurable) | Rewrite as outcome: "Increase [metric] from X to Y" |
| **Task as KR** | "Complete 10 customer interviews" (activity, not outcome) | Rewrite: "Validate 3 assumptions with >80% confidence" |
| **Metric as Objective** | "Reach 10K DAU" (number, not aspiration) | Rewrite Objective: "Become the daily habit for [segment]" |
| **Sandbagging** | KRs the team knows it will hit without effort | Raise the bar: what would 70% achievement look like? |
| **Too many OKRs** | 6+ objectives or 5+ KRs per objective | Cut to 3-5 objectives, 2-4 KRs each |
| **No baseline** | KR has a target but no starting value | Add "from X to Y" format |
| **Vanity metric** | KR measures activity that doesn't drive outcomes | Replace with outcome that matters to users or business |
| **Unowned KR** | No person or team can influence the metric | Reassign or rewrite within team's control |

### Alignment Patterns

| Alignment Type | Description | Example |
|---------------|-------------|---------|
| **Vertical** | Company OKR cascades to team OKR | Company: "Expand into enterprise" -> Team: "Close 5 enterprise deals" |
| **Horizontal** | Cross-team dependency on a shared KR | Product KR depends on Engineering KR |
| **Contribution** | Team KR contributes to a company KR | Team KR is one input to a company-level metric |

### OKR Cadence

| Activity | Frequency | Owner | Duration |
|----------|-----------|-------|----------|
| Company OKR setting | Annual (with quarterly refresh) | Leadership team | 1-2 weeks |
| Team OKR drafting | Quarterly | Team lead | 1 week |
| OKR review & alignment | Quarterly (start of quarter) | Cross-functional | 2-3 days |
| Weekly check-in | Weekly | Team | 15-30 min |
| Mid-quarter review | Mid-quarter | Team lead + stakeholders | 1 hour |
| Quarterly scoring | End of quarter | Team | 1-2 hours |

## Output Structure

```markdown
# OKRs: [Team or Initiative Name] -- [Quarter/Year]

**Date**: [YYYY-MM-DD]
**Owner**: [OKR owner -- typically team lead or VP]
**Period**: [Q1/Q2/Q3/Q4 YYYY]
**Team**: [Team name]
**Type**: Company / Team / Individual
**Status**: Draft / Active / Scoring / Closed

## Company Context (if applicable)

**Relevant Company Objectives**:
- [Company Objective this team's OKRs support]
- [Additional company objective, if applicable]

---

## Objective 1: [Qualitative, inspirational objective statement]

**Type**: Committed / Aspirational
**Alignment**: [Which company OKR this supports]

| # | Key Result | Baseline | Target | Score | Status |
|---|-----------|----------|--------|-------|--------|
| 1.1 | [Measurable outcome with number] | [Starting value] | [Target value] | [0.0-1.0 or TBD] | [On Track / At Risk / Behind / Scored] |
| 1.2 | [Key result] | [Baseline] | [Target] | [Score] | [Status] |
| 1.3 | [Key result] | [Baseline] | [Target] | [Score] | [Status] |

**Objective Score**: [Average of KR scores or TBD]

---

## Objective 2: [Objective statement]

**Type**: Committed / Aspirational
**Alignment**: [Company OKR]

| # | Key Result | Baseline | Target | Score | Status |
|---|-----------|----------|--------|-------|--------|
| 2.1 | [Key result] | [Baseline] | [Target] | [Score] | [Status] |
| 2.2 | [Key result] | [Baseline] | [Target] | [Score] | [Status] |

**Objective Score**: [TBD]

---

## Objective 3: [Objective statement]

**Type**: Committed / Aspirational
**Alignment**: [Company OKR]

| # | Key Result | Baseline | Target | Score | Status |
|---|-----------|----------|--------|-------|--------|
| 3.1 | [Key result] | [Baseline] | [Target] | [Score] | [Status] |
| 3.2 | [Key result] | [Baseline] | [Target] | [Score] | [Status] |
| 3.3 | [Key result] | [Baseline] | [Target] | [Score] | [Status] |

**Objective Score**: [TBD]

---

## OKR Quality Review

### Per-Objective Check

| # | Objective | Qualitative? | Inspirational? | Time-bound? | Actionable? | Concise? | Pass? |
|---|-----------|-------------|---------------|------------|------------|---------|-------|
| 1 | [Obj 1 short] | [Y/N] | [Y/N] | [Y/N] | [Y/N] | [Y/N] | [Y/N] |
| 2 | [Obj 2 short] | [Y/N] | [Y/N] | [Y/N] | [Y/N] | [Y/N] | [Y/N] |
| 3 | [Obj 3 short] | [Y/N] | [Y/N] | [Y/N] | [Y/N] | [Y/N] | [Y/N] |

### Per-KR Check

| # | Key Result | Quantitative? | Measurable? | Outcome (not task)? | Has Baseline? | Ambitious? | Pass? |
|---|-----------|--------------|------------|-------------------|-------------|-----------|-------|
| 1.1 | [KR short] | [Y/N] | [Y/N] | [Y/N] | [Y/N] | [Y/N] | [Y/N] |
| 1.2 | [KR short] | [Y/N] | [Y/N] | [Y/N] | [Y/N] | [Y/N] | [Y/N] |
| ... | ... | ... | ... | ... | ... | ... | ... |

### Anti-Patterns Detected

| # | Anti-Pattern | Location | Severity | Suggested Fix |
|---|-------------|----------|----------|---------------|
| 1 | [Pattern name] | [Which OKR/KR] | [High/Medium/Low] | [How to fix] |
| 2 | [Pattern] | [Location] | [Severity] | [Fix] |

**Overall Quality**: [Strong / Acceptable / Needs Revision]
**Issues Found**: [Count]

## Alignment Map

### Vertical Alignment (Company -> Team)

| Company Objective | Team Objective | Team KRs Contributing |
|------------------|---------------|----------------------|
| [Company Obj] | [Team Obj N] | [KR N.1, N.2] |

### Horizontal Dependencies (Cross-Team)

| This Team's KR | Depends On | Other Team | Risk Level |
|---------------|-----------|-----------|-----------|
| [KR N.N] | [What is needed] | [Team name] | [High/Medium/Low] |

## Check-In Cadence

| Week | Focus | Format |
|------|-------|--------|
| Week 1-2 | Set OKRs, align | Workshop |
| Week 3-5 | Confidence check (Red/Yellow/Green per KR) | 15-min standup |
| Week 6-7 | Mid-quarter review, adjust if needed | 1-hour review |
| Week 8-11 | Push for results, escalate blockers | 15-min standup |
| Week 12-13 | Score, reflect, feed into next quarter | Scoring session |
```

## Instructions

1. Ask clarifying questions about the team, quarter, company OKRs (if applicable), and strategic priorities
2. **Check prior context**: Run `/context-recall [team/product]` to find related strategic bets, vision statements, and roadmap themes
3. **Check feedback**: Run `/feedback-recall [goals/priorities/objectives]` for relevant signals
4. Reference any strategy documents, roadmaps, or previous OKR cycles provided via @file syntax
5. Write objectives that are qualitative and inspirational -- push back on numeric objectives
6. Write key results that are outcomes, not tasks -- flag and rewrite any task-based KRs
7. Run the quality review checklist on every OKR set, even in CREATE mode
8. Detect and flag anti-patterns explicitly with suggested fixes
9. Include alignment mapping if company-level OKRs are provided
10. Use [TBD] for scores in new OKRs; populate baselines where possible
11. Save in okrs/, strategy/, or planning/ folder
12. Offer to create presentation version using /present

## Context Integration

After generating or reviewing OKRs:

1. **Offer to save**: Ask "Should I save this to the context registry? (`/context-save`)"
2. If yes, extract and save:
   - OKR set and quality review results to context
   - Link to related strategic bets, roadmap themes, and vision statements
   - Cross-team dependencies to `context/decisions/` for tracking
3. Suggest using OKR targets as success criteria in `/strategic-bet` and `/commitment-check`
4. At quarter end, suggest `/outcome-review` and `/retrospective` to close the learning loop
