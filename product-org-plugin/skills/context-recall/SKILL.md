---
name: context-recall
description: Query past decisions, bets, and learnings by topic
argument-hint: [topic or keyword]
---

Recall relevant **past context** before making new decisions or starting strategic work.

## V2V Phase

**Cross-phase** - This skill is used before work in any phase to surface relevant history.

**Prerequisites**: Context registry populated (decisions, bets, learnings saved)
**Outputs used by**: Decision-making at any phase

## Purpose

Before making a decision that may have been made before, or starting work in an area with existing strategic context, query the context registry to surface relevant history.

## When to Use

Invoke `/context-recall [topic]` when:
- Starting work on a new decision
- Beginning strategic planning in an area
- Checking if similar decisions exist
- Understanding constraints from past decisions
- Finding relevant learnings to apply

## Process

### 1. Parse the Query

Accept a topic or keyword from the user:
- `/context-recall pricing` → Search for pricing-related context
- `/context-recall enterprise` → Search for enterprise-related context
- `/context-recall api` → Search for API-related context

### 2. Search All Context Sources

Search across all context indexes:

#### Decisions (`context/decisions/index.md`)
- Search titles and tags
- Return matching decision summaries

#### Strategic Bets (`context/bets/index.md`)
- Search titles and key assumptions
- Return matching bet summaries

#### Assumptions (`context/assumptions/registry.md`)
- Search assumption text
- Return matching assumptions with status

#### Learnings (`context/learnings/index.md`)
- Search learning text and tags
- Return matching learnings

#### Active Portfolio (`context/portfolio/active-bets.md`)
- Check if topic relates to active bets
- Surface current strategic context

### 3. Read Full Records if Needed

For highly relevant matches:
- Read the full decision record or bet document
- Extract key rationale and constraints
- Note re-decision triggers

### 4. Synthesize Results

Present findings in order of relevance:

```markdown
## Context Recall: [Topic]

### Relevant Decisions
| ID | Title | Status | Key Rationale |
|----|-------|--------|---------------|
| DR-2026-001 | [Title] | Accepted | [Why this was decided] |

**Constraints from these decisions:**
- [Constraint 1]
- [Constraint 2]

### Related Strategic Bets
| ID | Title | Status | Relevance |
|----|-------|--------|-----------|
| SB-2026-002 | [Title] | Active | [How it relates] |

### Tracked Assumptions
| ID | Assumption | Status |
|----|------------|--------|
| A-005 | [Assumption text] | Pending |

### Applicable Learnings
| ID | Learning | Confidence |
|----|----------|------------|
| L-012 | [Learning text] | High |

### Recommendations
Based on past context:
- [Recommendation 1]
- [Recommendation 2]
```

### 5. Flag Conflicts or Risks

If the current work might conflict with past decisions:
- Highlight the potential conflict
- Reference the re-decision triggers
- Suggest whether a re-decision process is needed

## Instructions

1. Accept topic/keyword from user (required)
2. Read all context index files
3. Search for matches (case-insensitive, partial match OK)
4. For strong matches, read full records
5. Synthesize and present findings
6. Highlight constraints that apply to current work
7. Note any potential conflicts with past decisions
8. If no matches found, say so clearly

## Example Usage

```
User: /context-recall pricing