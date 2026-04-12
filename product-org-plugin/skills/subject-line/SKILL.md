---
name: subject-line
description: 'Context-driven email subject line generator optimized for cold outreach and product communication. Activate when: "subject line", "email subject", "cold email subject", "subject line ideas",
  "email open rate", "subject line optimization" Do NOT activate for: email sequences (/email-sequence), copywriting (/copywriting), campaign briefs (/campaign-brief)'
argument-hint: '[recipient/company + purpose] or [update path/to/subject-lines.md]'
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: marketing
  skill_type: task-capability
---
## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "revise", "improve" in input | UPDATE | 100% |
| File path provided (`@path/to/subject-lines.md`) | UPDATE | 100% |
| "create", "new", "generate", "write" in input | CREATE | 100% |
| "find", "search", "list subject lines" | FIND | 100% |
| "the subject line", "our email subjects" | UPDATE | 85% |
| Just recipient or company name | CREATE | 60% |

**Threshold**: >=85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Generate subject line options using methodology below, tailored to context inputs.

**UPDATE**:
1. Read existing subject lines (search if path not provided)
2. Preserve context and rationale
3. Generate improved alternatives based on feedback or new context
4. Show comparison: "Previous: [old]. New options: [new]. Rationale: [why better]."

**FIND**:
1. Search paths below for subject line documents
2. Present results: campaign/recipient, subject lines used, open rate if tracked, path
3. Ask: "Update one of these, or create new?"

### Search Locations for Subject Lines

- `outreach/`
- `campaigns/`
- `marketing/`
- `emails/`

---
## Gotchas

- Shorter wins in cold outreach — 1-5 words outperform 6+ words; resist the urge to over-explain in the subject
- Personalization means company/name in the subject, not just the body — but avoid being creepy or over-researched
- Never fake "Re:" or "Fwd:" to imply an existing thread — it damages trust and triggers spam filters
- A/B test results require minimum 100 sends per variant — do not draw conclusions from small samples



Generate **email subject lines** optimized for open rates, using research-backed patterns tailored to the recipient, company, purpose, and relationship warmth.

## Vision to Value Phase

**Phase 4: Coordinated Execution** - Subject lines are part of campaign execution, enabling effective outreach for launches, sales, and customer communication.

**Prerequisites**: Phase 3 complete (target audience defined, messaging and positioning established)
**Outputs used by**: Phase 4 (campaign execution, outreach sequences, sales enablement), Phase 5 (measuring campaign effectiveness via open rates)

## Methodology

<!-- Source: Cold email subject line analysis — Daniel Saks (CEO of Landbase), analysis of 52,457 cold emails measuring open rates by subject line characteristics. Key findings: shorter subjects win, personalization adds ~26% lift, lowercase outperforms title case in cold outreach. -->

<!-- Source: Email deliverability best practices — consolidated from Mailchimp, HubSpot, and Lemlist research on spam trigger avoidance and inbox placement optimization. -->

### Research Findings (52,457 Cold Emails)

| Finding | Data Point | Implication |
|---------|-----------|-------------|
| Optimal length | 1-5 words outperform 6+ words | Keep it short — every extra word reduces open rate |
| Personalization | Company or name in subject = +26% open rate | Always include a personalization token when possible |
| Case | Lowercase outperforms Title Case in cold outreach | Use lowercase for cold emails; Title Case for newsletters |
| Questions | 10-15% higher open rate than statements | Frame as a question when natural |
| Numbers | Specificity outperforms vagueness | "3 ideas for [company]" beats "Ideas for you" |
| Spam triggers | ALL CAPS, excessive punctuation, "Re:" faking | Avoid — damages deliverability and trust |

### Subject Line Patterns

| # | Pattern | Example | Best For |
|---|---------|---------|----------|
| 1 | **Direct question** | "quick question about [topic]" | Cold outreach, first touch |
| 2 | **Personalized observation** | "[company] + [specific thing you noticed]" | Research-backed outreach |
| 3 | **Mutual connection** | "[name] suggested I reach out" | Warm introductions |
| 4 | **Value-first** | "[specific number] for [company]" | Data-driven outreach |
| 5 | **Curiosity gap** | "noticed something about [company's thing]" | Cold outreach, engagement |
| 6 | **Relevant event** | "congrats on [recent event]" | Trigger-based outreach |
| 7 | **Problem-aware** | "[specific problem they likely have]" | Solution-selling outreach |

### Pattern Selection by Relationship Warmth

| Warmth | Best Patterns | Avoid |
|--------|--------------|-------|
| **Cold** (no prior contact) | Direct question, Curiosity gap, Problem-aware | Mutual connection (unless real), Value-first (can feel presumptuous) |
| **Warm** (referral, met at event) | Mutual connection, Relevant event, Personalized observation | Generic patterns — warmth demands specificity |
| **Existing** (current customer/contact) | Value-first, Direct question, Relevant event | Curiosity gap (feels manipulative with known contacts) |

### Pattern Selection by Email Type

| Email Type | Best Patterns | Length Guidance |
|------------|--------------|----------------|
| **Cold outreach** | 1, 2, 5, 7 | 1-5 words, lowercase |
| **Follow-up** | 1, 4 | 2-4 words, reference prior touch |
| **Newsletter** | 4, 5, 6 | 5-8 words, Title Case acceptable |
| **Transactional** | Direct and clear | State the purpose plainly |
| **Product launch** | 5, 6, 4 | 3-6 words, build anticipation |

### Spam Triggers to Avoid

| Category | Examples | Why It Hurts |
|----------|---------|--------------|
| **ALL CAPS** | "FREE OFFER", "ACT NOW" | Spam filter trigger, feels aggressive |
| **Excessive punctuation** | "Don't miss this!!!", "Ready???" | Spam filter trigger, unprofessional |
| **Fake threading** | "Re:", "Fwd:" on first touch | Destroys trust immediately |
| **Spam words** | "Free", "Guaranteed", "No obligation" | Inbox placement penalty |
| **Clickbait** | "You won't believe this", "This changes everything" | High open rate but kills trust and reply rate |
| **Emoji overuse** | Multiple emojis in subject | Spam filters; one strategic emoji can work for newsletters only |

## Output Structure

```markdown
# Subject Lines: [Recipient/Company/Campaign]

**Date**: [YYYY-MM-DD]
**Recipient**: [Name, role, company]
**Email Type**: Cold outreach / Follow-up / Newsletter / Transactional / Product launch
**Relationship**: Cold / Warm / Existing
**Purpose**: [What this email aims to achieve]

## Context Inputs

| Input | Value |
|-------|-------|
| Recipient name | [Name] |
| Company | [Company] |
| Role | [Title] |
| Purpose | [What you want] |
| Relationship warmth | [Cold/Warm/Existing] |
| Personalization hook | [Something specific you know about them/company] |
| Email type | [Cold outreach/Follow-up/Newsletter/Transactional/Launch] |

## Recommended Subject Lines

### Primary (Top Pick)

**Subject**: [subject line]
**Pattern**: [Which pattern from methodology]
**Why**: [1-2 sentences on why this works for this context]

### Alternatives

| # | Subject Line | Pattern | Rationale |
|---|-------------|---------|-----------|
| 1 | [option] | [pattern name] | [Why it works] |
| 2 | [option] | [pattern name] | [Why it works] |
| 3 | [option] | [pattern name] | [Why it works] |
| 4 | [option] | [pattern name] | [Why it works] |

## A/B Test Recommendation

**Variant A**: [subject line]
**Variant B**: [subject line]
**Hypothesis**: [What you expect to learn]
**Minimum sample**: 100 sends per variant
**Success metric**: Open rate (primary), reply rate (secondary)

## Anti-Patterns Avoided

| Avoided | Why |
|---------|-----|
| [Thing you deliberately did not do] | [Why it would have hurt performance] |
```

## Instructions

1. Gather context inputs: recipient, company, purpose, relationship warmth, email type — ask if not provided
2. **Check prior context**: Run `/context-recall [company or campaign]` to find related positioning, messaging, or prior outreach
3. **Check feedback**: Run `/feedback-recall [outreach/email/open rates]` for signals on what has worked before
4. Reference any buyer research, prospect data, or campaign briefs provided via @file syntax
5. Generate 5-6 options across different patterns, selecting patterns appropriate to warmth and email type
6. Recommend a primary pick with rationale and an A/B test pair
7. Validate every option against the spam trigger checklist — reject any that fail
8. Save in outreach/ or campaigns/ folder when part of a campaign
9. Offer to integrate with `/email-sequence` or `/campaign-brief` if part of a larger flow

## Integration

- **Inputs from**: `/positioning-statement` (messaging informs subject line angles), `/campaign-brief` (campaign objectives guide tone), buyer research files (personalization hooks)
- **Outputs to**: `/email-sequence` (subject lines feed into sequence steps), `/campaign-brief` (subject line strategy informs campaign planning), `/sales-enablement` (outreach subject lines for sales team)
- **Related**: `/copywriting` (full email body copy), `/email-sequence` (multi-step sequences), `/campaign-brief` (campaign-level planning)

## Context Integration

After generating subject lines:

1. **Offer to save**: Ask "Should I save this to the context registry? (`/context-save`)" — especially if patterns are established for a specific audience
2. If yes, extract and save:
   - Winning patterns and context to inform future outreach
   - Link to related campaigns, positioning statements, and buyer personas
3. Suggest tracking open rates to validate pattern selection over time
