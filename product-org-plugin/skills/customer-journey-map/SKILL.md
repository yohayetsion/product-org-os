---
name: customer-journey-map
description: 'Map the end-to-end customer journey across lifecycle stages, identifying touchpoints, emotions, pain points, and opportunities for improvement. Activate when: "journey map", "customer journey",
  "user journey", "touchpoints", "experience map", "pain points along the journey", "map the experience", "lifecycle stages" Do NOT activate for: onboarding playbooks (/onboarding-playbook), customer health
  scorecards (/customer-health-scorecard), user stories (/user-story)'
argument-hint: '[product or persona name] or [update path/to/journey-map.md]'
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: customer-success
  skill_type: task-capability
---
## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "revise", "add stage" in input | UPDATE | 100% |
| File path provided (`@path/to/journey-map.md`) | UPDATE | 100% |
| "create", "new", "map the journey" in input | CREATE | 100% |
| "find", "search", "list journey maps" | FIND | 100% |
| "the journey map", "our journey" | UPDATE | 85% |
| Just a product or persona name | CREATE | 60% |

**Threshold**: >=85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Identify persona and product, walk through each lifecycle stage, populate all dimensions, identify moments of truth.

**UPDATE**:
1. Read existing journey map (search if path not provided)
2. Preserve unchanged stages exactly
3. Update specific stages or dimensions
4. Show diff summary: "Updated: [stages/dimensions]. Unchanged: [stages]."
5. Re-evaluate moments of truth if stages changed

**FIND**:
1. Search paths below for journey map documents
2. Present results: title, persona, product, path
3. Ask: "Update one of these, or create new?"

### Search Locations

- `product/`
- `ux/`
- `research/`
- `customer/`
- `journey/`

---

## Vision to Value Phase

**Phase 1: Strategic Foundation** - Journey maps build deep understanding of the customer experience before defining solutions.

**Prerequisites**: Target persona identified (even loosely)
**Outputs used by**: `/prd` (Phase 3), `/onboarding-playbook` (Phase 5), `/feature-spec`, `/user-story`

## Methodology

<!-- Source: Customer Journey Mapping — Adaptive Path (now part of Capital One), pioneered by Brandon Schauer and team (2007+). The discipline of mapping the full end-to-end customer experience across touchpoints, channels, and time. Key innovation: visualizing the emotional journey alongside functional steps reveals opportunities invisible in feature-centric thinking. -->

<!-- Source: Service Blueprinting — G. Lynn Shostack, "Designing Services That Deliver" (1984), Harvard Business Review. Extended by Mary Jo Bitner et al. (2008). Adds the "line of visibility" concept: what the customer sees vs. what happens backstage. Journey maps are the customer-facing layer of a service blueprint. -->

<!-- Source: Moments of Truth — Jan Carlzon, "Moments of Truth" (1987), originally for SAS Airlines. Any instance where a customer forms an impression of the brand. Extended by A.G. Lafley (P&G) as "First Moment of Truth" (shelf), "Second Moment of Truth" (usage). Google added "Zero Moment of Truth" (ZMOT, 2011) for the research phase before purchase. -->

<!-- Source: Jobs to Be Done — Clayton Christensen, "Competing Against Luck" (2016). Customers "hire" products to make progress in their lives. Journey mapping benefits from JTBD lens: at each stage, what job is the customer trying to get done? -->

### Lifecycle Stages

The default journey framework uses 7 stages. Adapt stages to your product context (B2B, B2C, SaaS, marketplace, etc.):

| Stage | Description | Key Questions |
|-------|-------------|---------------|
| **Awareness** | Customer discovers the problem or your product exists | How do they first hear about you? What triggers the search? |
| **Consideration** | Customer evaluates options and alternatives | What are they comparing? What information do they need? |
| **Acquisition** | Customer decides to buy/sign up | What drives the final decision? What friction exists? |
| **Onboarding** | Customer starts using the product | How do they get to first value? Where do they get stuck? |
| **Adoption** | Customer integrates product into their workflow | When does it become a habit? What features drive stickiness? |
| **Retention** | Customer continues using and renewing | What keeps them? What might cause churn? |
| **Advocacy** | Customer recommends to others | What triggers word-of-mouth? How do you enable referral? |

### Dimensions Per Stage

For each stage, capture:

| Dimension | What to Document |
|-----------|-----------------|
| **Customer Actions** | What the customer does at this stage (observable behaviors) |
| **Thoughts & Feelings** | What the customer thinks and feels (internal state) |
| **Touchpoints** | Where interaction happens (website, email, app, person, etc.) |
| **Pain Points** | Friction, frustration, confusion, gaps |
| **Opportunities** | How to improve the experience at this stage |
| **Metrics** | How to measure success at this stage |

### Moments of Truth

After mapping all stages, identify the critical moments:

| Moment Type | Definition | Example |
|-------------|-----------|---------|
| **Zero Moment of Truth (ZMOT)** | When customer researches before engaging | Reading reviews, comparing alternatives |
| **First Moment of Truth** | First impression of your product | Landing page, first demo, trial signup |
| **Second Moment of Truth** | First meaningful use experience | Completing onboarding, achieving first outcome |
| **Ultimate Moment of Truth** | When customer becomes an advocate | Sharing with peers, writing a review, referring |

### Emotional Journey Curve

Rate the customer's emotional state at each stage:

| Rating | Emoji | Meaning |
|--------|-------|---------|
| +2 | Delighted | Exceeds expectations, creates delight |
| +1 | Positive | Good experience, meets expectations |
| 0 | Neutral | Neither positive nor negative |
| -1 | Frustrated | Below expectations, friction present |
| -2 | Angry | Significantly negative, at risk of abandonment |

## Output Structure

```markdown
# Customer Journey Map: [Product Name]

**Persona**: [Persona name and brief description]
**Date**: [YYYY-MM-DD]
**Owner**: [Who owns this map]
**Scope**: [End-to-end / Specific phase]
**Data sources**: [Research, interviews, analytics, assumptions]

## Persona Summary

**Name**: [Persona name]
**Role**: [Job title / user type]
**Goal**: [What they are trying to achieve]
**Context**: [Environment, constraints, technical comfort]

## Journey Map

### Stage 1: Awareness

| Dimension | Details |
|-----------|---------|
| **Customer Actions** | [What they do] |
| **Thoughts & Feelings** | [What they think/feel] |
| **Touchpoints** | [Where interaction happens] |
| **Pain Points** | [Friction and frustration] |
| **Opportunities** | [How to improve] |
| **Metrics** | [How to measure] |
| **Emotional State** | [+2 to -2] |

### Stage 2: Consideration
[Same table structure]

### Stage 3: Acquisition
[Same table structure]

### Stage 4: Onboarding
[Same table structure]

### Stage 5: Adoption
[Same table structure]

### Stage 6: Retention
[Same table structure]

### Stage 7: Advocacy
[Same table structure]

## Emotional Journey

| Stage | Awareness | Consideration | Acquisition | Onboarding | Adoption | Retention | Advocacy |
|-------|-----------|--------------|-------------|------------|----------|-----------|----------|
| **Rating** | [+2 to -2] | [+2 to -2] | [+2 to -2] | [+2 to -2] | [+2 to -2] | [+2 to -2] | [+2 to -2] |
| **Key Emotion** | [word] | [word] | [word] | [word] | [word] | [word] | [word] |

## Moments of Truth

| Moment | Stage | Description | Current Experience | Desired Experience |
|--------|-------|-------------|-------------------|-------------------|
| **ZMOT** | [Stage] | [Description] | [Current state] | [Ideal state] |
| **First MoT** | [Stage] | [Description] | [Current state] | [Ideal state] |
| **Second MoT** | [Stage] | [Description] | [Current state] | [Ideal state] |
| **Ultimate MoT** | [Stage] | [Description] | [Current state] | [Ideal state] |

## Top Pain Points (Prioritized)

| # | Stage | Pain Point | Severity | Frequency | Opportunity |
|---|-------|-----------|----------|-----------|-------------|
| 1 | [Stage] | [Pain] | High/Med/Low | High/Med/Low | [What to do] |
| 2 | [Stage] | [Pain] | High/Med/Low | High/Med/Low | [What to do] |

## Key Opportunities

| # | Stage | Opportunity | Impact | Effort | Priority |
|---|-------|------------|--------|--------|----------|
| 1 | [Stage] | [Opportunity] | High/Med/Low | High/Med/Low | [P0/P1/P2] |
| 2 | [Stage] | [Opportunity] | High/Med/Low | High/Med/Low | [P0/P1/P2] |

## Assumptions & Gaps

- [Key assumptions made in this map]
- [Data gaps that need research to fill]
- [Stages where confidence is lowest]

## Next Steps

- [ ] Validate pain points with customer interviews
- [ ] Prioritize opportunities via `/prioritize-features`
- [ ] Create requirements for top opportunities via `/prd`
- [ ] Design onboarding improvements via `/onboarding-playbook`
```

## Instructions

1. Ask for the persona and product if not specified
2. If the user has customer research data, incorporate it; if not, note which cells are assumptions vs. evidence-based
3. Walk through stages in order; for each stage, fill all dimensions before moving to the next
4. Adapt the default 7 stages to the product context (B2B SaaS may have "Procurement" between Consideration and Acquisition; marketplace may have separate buyer/seller journeys)
5. Always identify at least 3 moments of truth
6. Rate the emotional journey at each stage to create the emotional curve
7. Prioritize pain points by severity x frequency
8. Save output as markdown file
9. Offer `/prd` for addressing top pain points or `/onboarding-playbook` for onboarding-stage improvements

## Integration

- Links to `/prd` (turn journey pain points into requirements)
- Links to `/onboarding-playbook` (deep dive into onboarding stage)
- Links to `/customer-health-scorecard` (metrics from retention/advocacy stages)
- Links to `/prioritize-features` (rank opportunities from the journey map)
- Links to `/feedback-recall` (incorporate existing customer feedback into the map)
- Links to `/experiment-design` (test assumptions in the journey map)
- Links to `/context-save` (save journey insights for cross-session memory)
