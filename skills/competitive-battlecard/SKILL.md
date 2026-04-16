---
name: competitive-battlecard
description: 'Create a sales-ready competitive battlecard for use in competitive deals. Activate when: "battlecard", "competitive battlecard", "how to win against", "sales ammunition", "objection handling",
  "compete against" Do NOT activate for: competitive landscape overview (/competitive-landscape), detailed competitive analysis (/competitive-analysis), sales enablement content (/sales-enablement)'
argument-hint: '[competitor name] or [update path/to/battlecard.md]'
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: market-analysis
  skill_type: task-capability
  owner: account-exec
  primary_consumers:
  - pmm
  - ci
  - sales-engineer
  - sdr
  - account-exec
  - proposal-writer
  secondary_consumers:
  - pmm-dir
  - market-researcher
  - sales-dir
---
## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "revise", "refresh" in input | UPDATE | 100% |
| File path provided (`@path/to/battlecard.md`) | UPDATE | 100% |
| "create", "new", "build" in input | CREATE | 100% |
| "find", "search", "list battlecards" | FIND | 100% |
| "the battlecard for [competitor]" | UPDATE | 85% |
| Just competitor name | CREATE | 60% |

**Threshold**: >=85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Generate complete new battlecard using template below.

**UPDATE**:
1. Read existing battlecard (search if path not provided)
2. Preserve unchanged sections exactly
3. Update specific sections (pricing, features, objections, win stories)
4. Show diff summary: "Updated: [sections]. Unchanged: [sections]."
5. Note: Competitive intelligence changes frequently; date-stamp all claims

**FIND**:
1. Search paths below for battlecards
2. Present results: competitor name, last updated, path
3. Ask: "Update one of these, or create new?"

### Search Locations for Battlecards

- `competitive/`
- `sales/`
- `enablement/`
- `battlecards/`
- `marketing/`

---

Create a **Competitive Battlecard**: a concise, sales-ready reference for winning deals against a specific competitor.

## Vision to Value Phase

**Phase 4: Coordinated Execution** - Battlecards are sales enablement tools used during active competitive deals.

**Prerequisites**: Phase 1-2 complete (competitive landscape understood, positioning defined)
**Outputs used by**: Phase 4 (sales conversations, deal support), Phase 2 (positioning refinement)

## Methodology

<!-- Source: Competitive Battlecards - Standard B2B sales enablement practice, formalized by competitive intelligence platforms Klue (founded 2015, Vancouver) and Crayon (founded 2014, Boston). Battlecards are one-page (or few-page) quick-reference documents designed for sales reps to use during competitive deals. They distill competitive intelligence into actionable talking points, objection responses, and positioning guidance. -->

<!-- Source: Battlecard Structure - Industry best practice consolidated from Klue, Crayon, and enterprise sales enablement programs. Core sections: Company Overview (who they are), Strengths & Weaknesses (honest assessment), Common Objections + Responses (what prospects say and how to respond), Landmines (questions to plant that expose competitor weaknesses), Proof Points (customer wins, data, quotes), Win Themes (key messages that resonate), Feature Comparison (side-by-side capability matrix), Pricing Comparison (how pricing models differ). -->

<!-- Source: Win/Loss Analysis Integration - Standard competitive intelligence practice. Battlecards should be informed by actual win/loss data: why we won deals against this competitor, why we lost, and what patterns emerge. Without win/loss data, battlecards are theoretical; with it, they are battle-tested. -->

<!-- Source: Inspired by phuryn/pm-skills competitive-battlecard skill. Adapted and expanded with landmine questions, proof point structure, and win/loss integration. -->

### Battlecard Design Principles

| Principle | Rationale |
|-----------|-----------|
| **Concise** | Sales reps scan during calls; every word must earn its place |
| **Honest** | Acknowledge competitor strengths; reps lose credibility if they dismiss real advantages |
| **Actionable** | Every section should translate directly to something a rep can say or do |
| **Evidence-based** | Claims backed by customer quotes, data, or analyst reports |
| **Date-stamped** | Competitive landscape changes; outdated battlecards are dangerous |

### Objection Response Framework

| Component | Purpose |
|-----------|---------|
| **Acknowledge** | Show you understand the concern (don't dismiss) |
| **Reframe** | Shift the conversation to your strength |
| **Prove** | Provide evidence (customer quote, data point, demo) |
| **Bridge** | Connect back to the prospect's specific needs |

## Output Structure

```markdown
# Competitive Battlecard: [Your Product] vs [Competitor Name]

**Last Updated**: [YYYY-MM-DD]
**Owner**: [Single accountable person - typically PMM or CI]
**Confidence Level**: High / Medium / Low (based on intelligence quality)
**Product**: [Product name - optional, for multi-product organizations]

---

## Quick Reference

**Who they are**: [One-sentence description of competitor]
**Their sweet spot**: [Where they win most often - segment, use case, deal size]
**Our sweet spot**: [Where we win most often against them]
**TL;DR**: [One sentence on how to beat them]

---

## Competitor Overview

**Founded**: [Year]
**HQ**: [Location]
**Funding / Revenue**: [If known, or "Private/Unknown"]
**Key Customers**: [Notable logos]
**Recent Moves**: [Last 2-3 significant product/business updates]

---

## Strengths & Weaknesses

### Their Strengths (Be Honest)
| Strength | Impact on Deals | How to Neutralize |
|----------|----------------|------------------|
| [Strength 1] | [How it hurts us] | [Our counter-strategy] |
| [Strength 2] | [How it hurts us] | [Our counter-strategy] |

### Their Weaknesses (Our Opportunities)
| Weakness | Impact on Customers | How to Exploit |
|----------|-------------------|---------------|
| [Weakness 1] | [Customer pain] | [What to say/ask] |
| [Weakness 2] | [Customer pain] | [What to say/ask] |

---

## Feature Comparison

| Capability | Us | Competitor | Notes |
|-----------|-----|-----------|-------|
| [Capability 1] | [Yes/Partial/No] | [Yes/Partial/No] | [Key difference] |
| [Capability 2] | [Yes/Partial/No] | [Yes/Partial/No] | [Key difference] |
| [Capability 3] | [Yes/Partial/No] | [Yes/Partial/No] | [Key difference] |
| [Capability 4] | [Yes/Partial/No] | [Yes/Partial/No] | [Key difference] |

**Our unique capabilities**: [What we have that they don't]
**Their unique capabilities**: [What they have that we don't]

---

## Pricing Comparison

| Dimension | Us | Competitor |
|-----------|-----|-----------|
| Model | [Per seat / Usage / Flat] | [Their model] |
| Entry price | [Price or TBD] | [Price or TBD] |
| Enterprise price | [Price or TBD] | [Price or TBD] |
| Hidden costs | [What to highlight] | [What to expose] |
| Free tier | [Yes/No, details] | [Yes/No, details] |

**Pricing talking point**: [How to position our pricing favorably]

---

## Objection Handling

### Objection 1: "[Common objection about us vs competitor]"

**Acknowledge**: "[Show understanding]"
**Reframe**: "[Shift to our strength]"
**Prove**: "[Evidence - customer quote, data, or demo point]"
**Bridge**: "[Connect to prospect's specific need]"

### Objection 2: "[Another common objection]"

**Acknowledge**: "[Show understanding]"
**Reframe**: "[Shift to our strength]"
**Prove**: "[Evidence]"
**Bridge**: "[Connect to prospect's need]"

### Objection 3: "[Third objection]"

[Same structure]

---

## Landmine Questions

Questions to plant early in the sales process that expose competitor weaknesses:

| Question | Why It Works | Expected Competitor Gap |
|----------|-------------|----------------------|
| "[Question to ask the prospect]" | [What this exposes] | [Competitor's weakness here] |
| "[Question]" | [What this exposes] | [Competitor's weakness] |
| "[Question]" | [What this exposes] | [Competitor's weakness] |

**When to plant**: [Early in discovery / During demo / In evaluation criteria discussion]

---

## Win Themes

Key messages that resonate when competing against [Competitor]:

1. **[Theme 1]**: [One sentence explaining the theme and why it resonates]
2. **[Theme 2]**: [One sentence]
3. **[Theme 3]**: [One sentence]

---

## Proof Points

| Type | Detail | When to Use |
|------|--------|------------|
| **Customer Win** | [Customer who switched from competitor to us - name if allowed, anonymized if not] | [Relevant scenario] |
| **Data Point** | [Performance benchmark, analyst quote, or metric] | [Relevant scenario] |
| **Quote** | "[Customer quote about why they chose us over competitor]" | [Relevant scenario] |

---

## Win/Loss Patterns

### When We Win Against [Competitor]
| Pattern | Frequency | Key Factor |
|---------|-----------|-----------|
| [Winning pattern 1] | [Common/Occasional] | [What made the difference] |
| [Winning pattern 2] | [Common/Occasional] | [What made the difference] |

### When We Lose to [Competitor]
| Pattern | Frequency | Mitigation |
|---------|-----------|-----------|
| [Losing pattern 1] | [Common/Occasional] | [How to address in future deals] |
| [Losing pattern 2] | [Common/Occasional] | [How to address] |

---

## AI Search Visibility

Track competitor presence across AI search engines as part of the competitive landscape:

| Engine | Our Brand Role | Competitor Role | Notes |
|--------|---------------|----------------|-------|
| ChatGPT | [Primary/Secondary/Mention/Absent] | [Their role] | [Key observation] |
| Claude | [Primary/Secondary/Mention/Absent] | [Their role] | [Key observation] |
| Gemini | [Primary/Secondary/Mention/Absent] | [Their role] | [Key observation] |
| AI Overviews | [Primary/Secondary/Mention/Absent] | [Their role] | [Key observation] |

**AI Search Talking Point**: [How our AI search presence compares to competitor's]

Use `/llm-seo audit` to generate baseline data for this section.

---

## Recommended Demo Focus

When demoing against [Competitor], emphasize:
1. [Demo area 1] - [Why this differentiates us]
2. [Demo area 2] - [Why this differentiates us]
3. [Demo area 3] - [Why this differentiates us]

**Avoid showing**: [Areas where competitor is stronger; steer away from these in demos]

---

## Quick Cheat Sheet (For During the Call)

**Open with**: "[Opening positioning statement against this competitor]"
**Key differentiator**: "[Single most important differentiator]"
**Best proof point**: "[Most compelling evidence]"
**Close with**: "[Closing statement that reinforces our advantage]"
```

## Instructions

1. Ask for the competitor name and any available competitive intelligence
2. **Check prior context**: Run `/context-recall [competitor name]` for existing competitive analysis and past win/loss data
3. **Check feedback**: Run `/feedback-recall [competitor name]` for customer mentions of the competitor
4. Reference any competitive analysis, win/loss reports, or market research provided via @file syntax
5. Be honest about competitor strengths; reps lose credibility with dismissive battlecards
6. Ensure objection responses follow the Acknowledge-Reframe-Prove-Bridge structure
7. Date-stamp the battlecard and note confidence level based on intelligence quality
8. Save in competitive/ or sales/enablement/ folder
9. Offer to create presentation version using /present

## Context Integration

After generating the battlecard:

1. **Offer to save**: Ask "Should I save this to the context registry? (`/context-save`)"
2. If yes, extract and save:
   - Battlecard summary and key competitive insights to context
   - Link to related competitive landscape, positioning decisions, and sales enablement
3. Suggest updating when win/loss patterns change or competitor makes significant moves
