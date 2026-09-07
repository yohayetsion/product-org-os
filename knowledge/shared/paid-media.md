# Paid Media Frameworks

Knowledge pack for paid media agents (Paid Media Manager, Growth Marketer). Contains real frameworks for channel selection, budget allocation, campaign management, and attribution.

---

## Channel Selection Framework

### Choosing the Right Paid Channels

**When to use**: When planning paid media mix. Before allocating budget across channels.

**Decision matrix:**

| Channel | Best For | Audience Intent | Typical CAC (B2B SaaS) | Minimum Budget to Learn |
|---------|----------|----------------|------------------------|------------------------|
| **Google Search** | Capturing existing demand | High (actively searching) | Medium-High | $2K-5K/month |
| **Google Display/YouTube** | Awareness, retargeting | Low (passive) | Low-Medium | $3K-5K/month |
| **Meta (Facebook/Instagram)** | B2C, SMB B2B, lookalikes | Low (discovery) | Low-Medium | $2K-5K/month |
| **LinkedIn** | B2B targeting by title/company | Medium (professional context) | High | $3K-10K/month |
| **Twitter/X** | Tech audiences, thought leadership | Low-Medium | Medium | $1K-3K/month |
| **Reddit** | Technical communities, niche targeting | Medium | Low-Medium | $1K-3K/month |

### Channel-Market Fit Assessment

| Factor | Question | How to Assess |
|--------|----------|---------------|
| **Audience presence** | Is our target audience active on this channel? | Platform demographics, competitor presence |
| **Intent alignment** | Does channel intent match our funnel stage goal? | Search = high intent, social = low intent |
| **Targeting capability** | Can we reach our specific ICP? | Review targeting options per platform |
| **Creative format** | Can we tell our story in this format? | Text ads vs. visual vs. video requirements |
| **Competition intensity** | How saturated is this channel for our keywords/audience? | Auction insights, competitor analysis |

**Limitations**: Channel effectiveness varies dramatically by industry, product, and geography. Benchmarks are directional. The only reliable data is your own test data from your campaigns.

---

## Budget Allocation

### The 70/20/10 Framework

**When to use**: Distributing budget across proven, experimental, and exploratory channels.

| Allocation | Description | Goal |
|-----------|-------------|------|
| **70% — Proven** | Channels with demonstrated positive ROAS | Maintain and optimize |
| **20% — Experimental** | Channels showing promise but not yet proven | Test at scale |
| **10% — Exploratory** | New channels or radical creative approaches | Discover new opportunities |

### Budget Pacing

**Monthly pacing template:**

| Week | Spend Target | Actual Spend | Variance | Action |
|------|-------------|--------------|----------|--------|
| W1 | 25% of budget | [actual] | [+/-] | [adjust bids/budgets] |
| W2 | 50% cumulative | [actual] | [+/-] | [adjust bids/budgets] |
| W3 | 75% cumulative | [actual] | [+/-] | [adjust bids/budgets] |
| W4 | 100% | [actual] | [+/-] | [month-end review] |

**Budget allocation by funnel stage:**

| Funnel Stage | Budget % | Channel Mix | KPI |
|-------------|----------|-------------|-----|
| Awareness (TOFU) | 20-30% | Display, Social, YouTube | Reach, impressions, CPM |
| Consideration (MOFU) | 30-40% | Search, LinkedIn, Retargeting | CTR, CPC, engagement |
| Conversion (BOFU) | 30-40% | Search (high intent), Retargeting | CPA, ROAS, conversions |

**Limitations**: Budget allocation is not a set-and-forget exercise. Rebalance monthly based on performance data. Seasonal effects, competitive dynamics, and platform algorithm changes require ongoing adjustment.

---

## Google Ads Framework

### Campaign Structure

**When to use**: Setting up or restructuring Google Ads campaigns.

**Recommended structure:**

```
Account
├── Brand Campaign (exact match brand terms)
│   └── Ad Group: Brand terms
├── Non-Brand Search Campaign (category terms)
│   ├── Ad Group: [Product Category] terms
│   ├── Ad Group: [Problem/Pain] terms
│   └── Ad Group: [Competitor] terms
├── Performance Max / Display Campaign
│   └── Asset groups by audience segment
└── Retargeting Campaign
    ├── Ad Group: Site visitors (7d)
    ├── Ad Group: Site visitors (30d)
    └── Ad Group: Engaged but not converted
```

### Keyword Match Types

| Match Type | Syntax | Reach | Control | When to Use |
|-----------|--------|-------|---------|-------------|
| Exact | [keyword] | Narrow | High | Proven converters, brand terms |
| Phrase | "keyword" | Medium | Medium | Testing new themes |
| Broad | keyword | Wide | Low | Discovery with smart bidding, sufficient data |

### Ad Copy Template (Responsive Search Ads)

```
Headlines (up to 15):
H1: [Primary keyword + benefit]
H2: [Secondary benefit or differentiator]
H3: [Social proof or credibility]
H4: [CTA variation 1]
H5: [CTA variation 2]
H6: [Feature-specific benefit]
... (add variations pinning key messages to positions 1-2)

Descriptions (up to 4):
D1: [Value proposition — what you do and for whom]
D2: [How it works or key differentiator — with CTA]
D3: [Social proof + CTA]
D4: [Feature details + CTA]
```

**Limitations**: Google Ads' automation (smart bidding, broad match, Performance Max) requires conversion data to optimize. New accounts or campaigns with fewer than 30 conversions per month may perform better with manual or semi-manual bidding.

---

## Meta Ads Framework

### Campaign Objectives and Funnel Mapping

**When to use**: Setting up Meta (Facebook/Instagram) campaigns.

| Objective | Funnel Stage | Optimization Event | When to Use |
|-----------|-------------|-------------------|-------------|
| Awareness | TOFU | Reach, Impressions | Brand building, new market entry |
| Traffic | TOFU/MOFU | Link clicks, Landing page views | Driving to content or landing pages |
| Engagement | MOFU | Post engagement, Page likes | Building social proof |
| Leads | MOFU/BOFU | Lead form submissions | B2B lead generation |
| Conversions | BOFU | Purchase, Signup, Demo request | Direct response |

### Audience Strategy

| Audience Type | Definition | Size Target | When to Use |
|-------------|-----------|------------|-------------|
| **Core** | Interest + demographic targeting | 500K-5M | Cold prospecting |
| **Lookalike** | Similar to existing customers | 1-3% of country | Scaling proven segments |
| **Custom** | Retargeting (website, email list, engagement) | Varies | Re-engaging warm audiences |
| **Broad** | Minimal targeting, algorithm decides | 10M+ | Sufficient conversion data (50+ per week) |

### Creative Best Practices

| Format | Specs | Best For | Key Rule |
|--------|-------|----------|----------|
| Single image | 1:1 or 4:5, < 20% text overlay | Simple offers, clear visual | Hero image must work without reading text |
| Video | 4:5 or 9:16, 15-30s, captions | Storytelling, demos, testimonials | Hook in first 3 seconds, work without sound |
| Carousel | 3-10 cards, each 1:1 | Features, steps, product showcase | First card must stand alone as hook |
| Collection | Hero + product catalog | E-commerce, multiple products | Strong hero image drives exploration |

**Limitations**: Meta's audience targeting has narrowed significantly after iOS 14.5 privacy changes. Broad targeting with strong creative often outperforms detailed interest targeting. Creative quality is now the primary lever.

---

## LinkedIn Ads Framework

### Campaign Types for B2B

**When to use**: B2B marketing targeting by job title, company, seniority, or industry.

| Ad Format | Best For | Cost Range | Minimum Audience |
|-----------|----------|-----------|------------------|
| Sponsored Content (image/video) | Awareness, content promotion | $6-12 CPC | 50K+ |
| Message Ads (InMail) | Direct outreach, event invites | $0.30-0.80 per send | 15K+ |
| Text Ads | Sidebar visibility, budget-friendly | $3-6 CPC | 50K+ |
| Document Ads | Thought leadership, gated content | $6-15 CPC | 50K+ |
| Conversation Ads | Multi-step engagement | $0.30-0.80 per send | 15K+ |

### Targeting Strategy

**Layer targeting for precision:**

```
Company targeting:
  Industry: [select]
  Company size: [select]
  Company name (ABM): [upload list]

Role targeting:
  Job title: [select or upload]
  Job function: [select]
  Seniority: [select]
  Skills: [select]

Exclude:
  Current employees
  Existing customers (via Matched Audiences)
  Competitors (by company name)
```

**Limitations**: LinkedIn CPC is 3-5x more expensive than other platforms. Justify the premium with higher lead quality and conversion rates. If LinkedIn leads do not convert at a higher rate than cheaper channels, the premium is not worth it.

---

## Retargeting Framework

### Audience Segmentation by Engagement

**When to use**: Building retargeting campaigns across any platform.

| Segment | Definition | Message | Creative Approach |
|---------|-----------|---------|-------------------|
| **Hot** (0-7 days) | Recent site visitors, cart abandoners | Direct conversion push | Product-specific, urgency, offer |
| **Warm** (8-30 days) | Past visitors, engaged but not converted | Value reinforcement | Case studies, testimonials, comparison |
| **Cool** (31-90 days) | Older visitors, lapsed users | Re-engagement | New features, updated content, fresh angle |
| **Sequential** | Based on pages visited | Next logical step | If visited pricing → demo CTA. If visited blog → related content. |

### Frequency Caps

| Segment | Max Impressions per Week | Rationale |
|---------|------------------------|-----------|
| Hot | 7-10 | High intent, frequent reminder is acceptable |
| Warm | 4-5 | Balance persistence with annoyance |
| Cool | 2-3 | Light touch to avoid brand fatigue |

**Limitations**: Retargeting audiences shrink as privacy regulations and browser restrictions expand. Cookie-based retargeting is declining. First-party data strategies (email lists, logged-in users) are increasingly important.

---

## Attribution Models

### Understanding Multi-Touch Attribution

**When to use**: Evaluating which channels and campaigns contribute to conversions. Required for budget allocation decisions.

| Model | How It Works | Best For | Weakness |
|-------|-------------|----------|----------|
| **Last click** | 100% credit to final touchpoint | Simple reporting, bottom-funnel channels | Ignores awareness and consideration |
| **First click** | 100% credit to first touchpoint | Valuing discovery channels | Ignores nurture and conversion |
| **Linear** | Equal credit to all touchpoints | Fair overview | Over-credits low-value touches |
| **Time decay** | More credit to recent touchpoints | Balanced view | Undervalues awareness |
| **Position-based (U-shaped)** | 40% first, 40% last, 20% middle | Common compromise | Still somewhat arbitrary |
| **Data-driven** | ML model distributes credit based on actual impact | Most accurate (with data) | Requires significant conversion volume |

### Practical Attribution Approach

For most organizations, use this three-tier approach:

1. **Operational decisions** (daily/weekly): Use last-click for simplicity
2. **Budget allocation** (monthly): Use position-based or data-driven
3. **Strategic evaluation** (quarterly): Use multi-touch with marketing mix modeling

**Limitations**: Perfect attribution is impossible. Every model is a simplification. The goal is to be directionally correct, not precisely wrong. Focus on relative channel performance rather than absolute attribution.

---

## ROAS Benchmarks

### Return on Ad Spend by Channel

**When to use**: Setting targets and evaluating campaign performance.

**General B2B SaaS benchmarks (directional only):**

| Channel | Target ROAS | Break-even ROAS | Notes |
|---------|------------|-----------------|-------|
| Google Search (Brand) | 10-20x | 3x | Should be highly profitable |
| Google Search (Non-brand) | 3-8x | 2x | Varies by keyword competitiveness |
| LinkedIn | 2-5x | 1.5x | Premium CPC requires higher LTV |
| Meta | 3-8x | 2x | Creative quality is the lever |
| Retargeting (all platforms) | 5-15x | 3x | Warm audiences should convert efficiently |

**How to calculate ROAS:**
```
ROAS = Revenue Attributed to Ads / Ad Spend

Example: $50,000 revenue from $10,000 spend = 5.0x ROAS
```

**Limitations**: ROAS benchmarks vary enormously by industry, price point, and sales cycle. B2B with $50K ACV will have different ROAS targets than B2C with $50 average order. Use your own historical data as the primary benchmark, industry data as a secondary reference.

---

## Campaign Measurement Template

### Weekly Performance Report

**When to use**: Weekly review of paid media performance.

| Metric | Google Search | LinkedIn | Meta | Retargeting | Total |
|--------|-------------|----------|------|-------------|-------|
| Spend | | | | | |
| Impressions | | | | | |
| Clicks | | | | | |
| CTR | | | | | |
| CPC | | | | | |
| Conversions | | | | | |
| CPA | | | | | |
| ROAS | | | | | |

**Week-over-week changes to flag:**
- CPA increase > 20% → Investigate (competition, creative fatigue, audience saturation)
- CTR decrease > 15% → Refresh creative or adjust targeting
- Spend significantly under budget → Check campaign health (ad disapprovals, audience too small)
- Spend significantly over budget → Check pacing controls

**Limitations**: Weekly data can be noisy. Look for trends over 2-4 weeks rather than reacting to single-week fluctuations. Day-of-week effects, holidays, and external events create false signals in short timeframes.


## Common Pitfalls

- Ad platform CPCs and CPMs change constantly — never cite specific costs without current data
- ROAS calculations require attribution model specification — different models give different results
- Platform-specific ad policies change frequently — verify before recommending ad formats

---

## Signal-Loss-Era Paid Media (as of 2026-06-24)

<!-- Attribution (2026-06-24 additive delta):
  Adapted from: AZ Big Media "Digital marketing trends 2026: How AI, search and social will reshape growth" (azbigmedia.com, 2026); Google Ads automation documentation (Performance Max / smart bidding conversion-data requirements, publicly documented). Cookie-deprecation trajectory and AI-bidding mechanics are platform-behavioral and publicly documented.
  Source licence: per-source-terms (publicly published trade-press + vendor documentation; cited, not claimed).
  V2V refinements: added the signal-loss / privacy-era layer the pack lacked; framed AI-bidding as conversion-data-gated and creative-as-the-lever consistent with the pack's existing Meta and Google "Limitations" notes; pointed measurement to mmm-modeling.md. GEO / generative-search visibility is OUT of scope here — it is owned by geo-playbook.md (§12). No fabricated metrics.
-->

The paid-media frameworks above (channel selection, ROAS, attribution) were written for a tracking-rich world. Through 2025-2026 the targeting and measurement substrate degraded: iOS App Tracking Transparency broke cross-app signal years ago, third-party-cookie deprecation has stayed on a staged trajectory, and consent-gating under GDPR/ePrivacy removes a growing share of user-level data from the advertiser's view. This section is the privacy-era layer.

### What signal loss changes

| Pressure | Effect on paid media | What to do instead |
|----------|---------------------|--------------------|
| **Cookie / cross-app signal loss** | Retargeting pools shrink; lookalikes degrade; interest targeting narrows (already noted in the Meta and Retargeting "Limitations" above) | Shift weight to first-party data (email lists, logged-in users, server-side conversion APIs) and consented audiences |
| **Consent-gated tracking** | Pixel-attributed conversions undercount; last-click rollups understate non-consenting users | Treat platform-reported conversions as a floor, not truth; triangulate with aggregate measurement |
| **AI / automated bidding (PMax-class)** | Smart bidding and Performance Max optimize *only* with sufficient conversion data; thin-data accounts get unstable results (consistent with the Google Ads "Limitations" note above) | Feed the algorithm clean conversion signal (offline-conversion import, enhanced/server-side conversions); meet the conversion-data minimum before going broad; do not hand a cold account to full automation |
| **Creative as the primary lever** | When targeting precision erodes, creative quality is what the algorithm has left to work with (already true on Meta post-iOS-14.5) | Invest in creative volume + testing; the bid algorithm increasingly finds the audience, so the message and hook are where the marketer adds value |

### Measurement in the signal-loss era

User-level multi-touch attribution (the Attribution Models section above) is structurally degrading for the same reasons. The durable, privacy-safe measurement layer is **Marketing Mix Modeling** (aggregate spend → conversions, no user identifiers, no consent dependency) plus **geo-incrementality experiments** for calibration. See `mmm-modeling.md` (Google Meridian / Meta Robyn) — the pack's existing "strategic evaluation (quarterly): multi-touch with marketing mix modeling" tier becomes the *primary* budget-allocation lever, not just the quarterly check, as click-attribution reliability falls.

### Scope note

Brand visibility inside AI search / generative engines (AI Overviews, ChatGPT citations, generative share of voice) is a real 2026 paid-and-organic frontier, but it is owned by `geo-playbook.md` (§12 "GEO Enforcement & Compliance"), authored in this same wave. This section is deliberately scoped to *paid-channel signal loss and bidding*, not generative-search visibility, to avoid duplicating that pack.
