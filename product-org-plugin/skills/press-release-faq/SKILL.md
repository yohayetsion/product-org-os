---
name: press-release-faq
description: 'Write a Working Backwards PRFAQ document — a press release announcing the finished product as if it already shipped, plus internal and external FAQs, and optionally tenets for guiding tradeoff
  decisions. Forces clarity on customer value before building. Activate when: "press release", "PRFAQ", "working backwards", "Amazon PR FAQ", "announce the product", "vision press release", "write the press
  release first", "PR/FAQ" Do NOT activate for: strategy communications (/strategy-communication), stakeholder briefs (/stakeholder-brief), launch plans (/launch-plan), actual media press releases (@pr-comms-specialist)'
argument-hint: '[product or feature name] or [update path/to/prfaq.md]'
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.1.0
  category: strategy
  skill_type: task-capability
  owner: investor-relations
  primary_consumers:
  - pmm-dir
  - pmm
  - investor-relations
  - pr-comms-specialist
  - proposal-writer
  secondary_consumers:
  - ceo
  - cmo
  - marketing-dir
  - content-strategist
  - copywriter
  - presentation-designer
---
## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "revise", "rewrite" in input | UPDATE | 100% |
| File path provided (`@path/to/prfaq.md`) | UPDATE | 100% |
| "create", "new", "write PRFAQ" in input | CREATE | 100% |
| "find", "search", "list PRFAQs" | FIND | 100% |
| "the PRFAQ", "our press release" | UPDATE | 85% |
| Just a product/feature name | CREATE | 60% |

**Threshold**: >=85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Write complete PRFAQ: press release + internal FAQ + external FAQ. Start by clarifying the customer and the problem.

**UPDATE**:
1. Read existing PRFAQ (search if path not provided)
2. Preserve unchanged sections exactly
3. Update specific sections based on new direction or feedback
4. Show diff summary: "Updated: [sections]. Unchanged: [sections]."

**FIND**:
1. Search paths below for PRFAQ documents
2. Present results: title, product, date, path
3. Ask: "Update one of these, or create new?"

### Search Locations

- `product/`
- `strategy/`
- `prfaq/`
- `planning/`
- `vision/`

---
## Gotchas

- The press release is a forcing function for clarity, not actual marketing copy
- Customer quotes must represent what customers would ACTUALLY say, not marketing speak
- FAQs should include the hard questions leadership would ask, not softball questions



## Vision to Value Phase

**Phase 1: Strategic Foundation** - The PRFAQ is a vision-setting exercise that works backwards from the customer to define what success looks like before any building begins.

**Prerequisites**: A product or feature concept with an identified customer problem
**Outputs used by**: `/vision-statement`, `/strategic-bet` (Phase 1-2), `/prd` (Phase 3), `/positioning-statement` (Phase 2)

## Methodology

<!-- Source: Working Backwards / PRFAQ — Amazon internal practice, originated by Jeff Bezos and the Amazon leadership team (~2004). Popularized externally by Ian McAllister (former Amazon Director) in a widely-shared Quora answer and by Colin Bryar & Bill Carr in "Working Backwards: Insights, Stories, and Secrets from Inside Amazon" (2021, St. Martin's Press). The practice requires product teams to write a press release and FAQ BEFORE writing a line of code. The press release is written as if the product has already launched and is being announced to the world. If the press release is not compelling, the product concept needs more work. Key principle: "Start with the customer and work backwards." -->

<!-- Source: The press release format forces several critical clarifications: (1) Who is the customer? (2) What is the customer problem or opportunity? (3) What is the most important customer benefit? (4) How do you know what customers need? (5) What does the customer experience look like? The FAQ section forces teams to confront hard questions from both customers and internal stakeholders before investing resources. -->

<!-- Source: Narrative-driven decision making — Edward Tufte, "The Cognitive Style of PowerPoint" (2003). Amazon's preference for 6-page narratives over slide decks is rooted in the principle that prose forces clearer thinking than bullet points. The PRFAQ is the entry point to Amazon's narrative culture. -->

<!-- Source: Working Backwards process details — Colin Bryar & Bill Carr, "Working Backwards: Insights, Stories, and Secrets from Inside Amazon" (2021, St. Martin's Press). Bryar was Jeff Bezos's Chief of Staff ("shadow") from 2003-2004. The book details the internal mechanisms including the narrative review ritual, bar raiser hiring, and single-threaded leadership. -->

<!-- Source: Inspired by pmprompt/claude-plugin-product-management PRFAQ skill. Enhanced with full Working Backwards process context, tenets, and narrative review ritual. -->

### The Working Backwards Process

The PRFAQ is Step 1 of Amazon's broader Working Backwards process:

| Step | Artifact | Purpose | Time |
|------|----------|---------|------|
| 1 | **PRFAQ** (this skill) | Define the customer experience and value | 1-2 weeks |
| 2 | **Tenets** | Principles that guide tradeoff decisions | During PRFAQ review |
| 3 | **Narrative Review** | 6-page memo read silently in meeting, then discussed | 60-min meeting |
| 4 | **Mock-ups / Wireframes** | Visual representation of the customer experience | 1-2 weeks |
| 5 | **Data & Metrics** | Define how success will be measured | During review |
| 6 | **Resource Ask** | What team/budget is needed | After approval |

**The Narrative Review ritual**:
- No slides. Ever. The PRFAQ is printed as a 6-page narrative.
- Everyone reads silently for 20 minutes at the start of the meeting.
- Discussion follows reading — ensures everyone has the same context.
- Senior leader asks: "Is this worth doing?" and "Is this the best version of this idea?"

**Iteration is expected**: Most PRFAQs go through 3-10 iterations before approval. The first draft is rarely the last. Each review cycle sharpens the customer value proposition.

### Tenets (Optional but Recommended)

Tenets are the principles that will guide tradeoff decisions during execution. They should be:
- **Controversial enough to have an opposite**: "We prioritize user privacy over personalization" (opposite: "We prioritize personalization over privacy"). If nobody would disagree, it's not a tenet.
- **Ordered by priority**: When tenets conflict, higher-ranked tenets win.
- **Specific to this initiative**: Not generic company values.

Example tenets for a payment product:
1. Security over convenience — we will never sacrifice transaction security for faster checkout
2. Merchant experience over internal efficiency — we optimize for merchant UX even if it increases our operational cost
3. Transparency over simplicity — we show all fees even if it makes the interface more complex

### Why Write a Press Release First?

The PRFAQ exercise serves as a forcing function:

| What It Forces | Why It Matters |
|----------------|---------------|
| **Customer clarity** | You must name the customer and their problem in the opening paragraph |
| **Benefit specificity** | Vague value props become obvious when written as press release claims |
| **Scope discipline** | A press release has limited space; it forces prioritization of what matters |
| **Stakeholder alignment** | Reading a concrete announcement is more actionable than debating abstract strategy |
| **Honest FAQ** | Internal FAQ forces teams to confront business risks they might otherwise avoid |

### The Litmus Test

If you cannot write a compelling press release, the product is not ready to build. Specifically:

- If the **headline** does not make a customer care, the value prop needs work
- If the **customer quote** sounds forced, you do not understand the customer well enough
- If the **internal FAQ** has unanswerable questions, there are unresolved strategic decisions
- If the **external FAQ** reveals deal-breaking concerns, the concept needs redesign

### Press Release Structure

The press release follows a specific 10-element structure:

| # | Element | Purpose | Length |
|---|---------|---------|--------|
| 1 | **Headline** | Grab attention, name the customer benefit | 1 line |
| 2 | **Subheadline** | Expand on the headline, name the target customer | 1 line |
| 3 | **Date & Location** | Set the scene (use a future date) | 1 line |
| 4 | **Opening Paragraph** | Who, what, why — the core announcement | 2-3 sentences |
| 5 | **Problem Description** | The customer problem this solves | 1 paragraph |
| 6 | **Solution Description** | How the product solves it (customer language, not technical) | 1 paragraph |
| 7 | **Company Leader Quote** | Why this matters strategically (vision, mission alignment) | 1 paragraph |
| 8 | **How It Works** | Simple description of the customer experience | 1 paragraph |
| 9 | **Customer Quote** | A fictional but realistic customer expressing the value | 1 paragraph |
| 10 | **Call to Action** | How to get started | 1-2 sentences |

### FAQ Structure

| Section | Purpose | Typical Questions |
|---------|---------|-------------------|
| **Internal FAQ** | Address business concerns from leadership and stakeholders | Revenue model, competitive response, resource needs, risks, cannibalization, timeline |
| **External FAQ** | Address questions customers would ask | Pricing, availability, migration, support, compatibility, data security |

## Output Structure

```markdown
# PRFAQ: [Product/Feature Name]

**Date**: [YYYY-MM-DD]
**Owner**: [Who owns this document]
**Status**: [Draft / Reviewed / Approved]
**Iteration**: [1, 2, 3...]

---

## Press Release

### [HEADLINE: Customer benefit in customer language]

#### [SUBHEADLINE: Who this is for and why they should care]

**[CITY, STATE] — [Future Date]** — [Company Name] today announced [product/feature name], a [brief description] that enables [target customers] to [key benefit]. [Product name] is available [starting today / beginning Q_ 20__] at [website/location].

#### The Problem

[Describe the customer problem in vivid, specific terms. What is painful about the current state? What are customers doing today that is inadequate?]

#### The Solution

[Describe what the product does in customer language. Focus on outcomes, not features. What can customers now do that they could not do before? How is their life better?]

#### Quote from [Leader Name], [Title] at [Company]

"[A quote that connects this product to the company's mission and vision. Why does this matter beyond just the product? What does it say about where the company is going?]"

#### How It Works

[Walk through the customer experience in 3-4 simple steps. A customer reading this should be able to picture themselves using the product. No technical jargon.]

1. [Step 1: What the customer does first]
2. [Step 2: What happens next]
3. [Step 3: What the outcome looks like]

#### Quote from [Customer Name], [Title] at [Customer Company]

"[A realistic quote from a customer expressing the value they received. This should sound like something a real person would say, not marketing copy. Reference a specific benefit or outcome.]"

#### Getting Started

[How to start using the product. URL, pricing hint, availability.]

For more information, visit [URL].

---

## Internal FAQ

Questions that leadership, stakeholders, and cross-functional partners would ask:

### Q1: How does this fit our strategy?
**A**: [How this aligns with company vision, strategic bets, and portfolio]

### Q2: What is the revenue model?
**A**: [Pricing approach, revenue expectations — use frameworks and placeholders per no-estimates rule]

### Q3: How will competitors respond?
**A**: [Competitive positioning, defensibility, expected competitive reaction]

### Q4: What resources are required?
**A**: [Team, technology, partnerships needed — avoid specific estimates; describe scope and capabilities]

### Q5: What are the biggest risks?
**A**: [Top 2-3 risks and how they will be mitigated — reference `/four-risks-check` for deeper analysis]

### Q6: Does this cannibalize existing products?
**A**: [Honest assessment of internal impact]

### Q7: How will we measure success?
**A**: [Key metrics and success criteria — what would make this a success at 6 months and 12 months?]

[Add more internal Qs as needed for the specific context]

---

## External FAQ

Questions that customers would ask:

### Q1: How much does it cost?
**A**: [Pricing information or pricing model description]

### Q2: When is it available?
**A**: [Availability timeline]

### Q3: How does it work with my existing [tools/workflow]?
**A**: [Integration and compatibility story]

### Q4: Is my data secure?
**A**: [Security and privacy approach]

### Q5: What if I need help?
**A**: [Support model]

### Q6: How is this different from [competitor/alternative]?
**A**: [Differentiation in customer language]

[Add more external Qs as needed for the specific context]

---

## PRFAQ Quality Check

| Check | Status |
|-------|--------|
| Headline makes a customer care? | [ ] Yes / [ ] Needs work |
| Opening paragraph answers Who, What, Why? | [ ] Yes / [ ] Needs work |
| Solution described in customer language (not technical)? | [ ] Yes / [ ] Needs work |
| Customer quote sounds like a real person? | [ ] Yes / [ ] Needs work |
| Internal FAQ confronts hard business questions? | [ ] Yes / [ ] Needs work |
| External FAQ addresses real customer concerns? | [ ] Yes / [ ] Needs work |
| You would be excited to read this announcement? | [ ] Yes / [ ] Needs work |

## Assumptions Surfaced

| # | Assumption | Category | Confidence |
|---|-----------|----------|------------|
| 1 | [Assumption from writing the PR] | [Customer/Market/Business/Technical] | [High/Med/Low] |

## Next Steps

- [ ] Review PRFAQ with stakeholders for alignment
- [ ] Test assumptions via `/assumption-map` or `/experiment-design`
- [ ] If compelling, develop `/vision-statement` and `/strategic-bet`
- [ ] When ready to commit, write `/prd` based on this PRFAQ
- [ ] Extract positioning via `/positioning-statement`
```

## Instructions

1. Start by asking: Who is the customer? What is their problem? If the user has a clear concept, proceed directly
2. Write the press release FIRST, then the FAQs; the PR forces clarity that makes the FAQ easier
3. The headline is the hardest part; spend time making it customer-centric and compelling
4. The customer quote must sound human, not like marketing; if it sounds like a brochure, rewrite it
5. Internal FAQ must include hard questions the team might avoid (cannibalization, competitive risk, resource reality)
6. External FAQ should reflect genuine customer concerns, not softball questions
7. Never fabricate financial projections in the FAQ; use frameworks and placeholders per the no-estimates rule
8. After completing the PRFAQ, run the quality check and flag any "Needs work" items
9. Save output as markdown file
10. Offer `/assumption-map` for surfaced assumptions or `/vision-statement` to formalize the vision

## Integration

- Links to `/vision-statement` (PRFAQ crystallizes the vision that the vision statement formalizes)
- Links to `/strategic-bet` (PRFAQ can become the narrative core of a strategic bet)
- Links to `/positioning-statement` (extract positioning from the press release)
- Links to `/assumption-map` (surface and validate assumptions revealed during PRFAQ writing)
- Links to `/prd` (translate the PRFAQ into detailed product requirements when ready to build)
- Links to `/experiment-design` (test the riskiest assumptions surfaced by the PRFAQ)
- Links to `/four-risks-check` (assess the four risks highlighted in the internal FAQ)
- Links to `/context-save` (save the PRFAQ as a strategic foundation document)
