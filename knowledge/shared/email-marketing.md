# Email Marketing Knowledge Pack

**Version**: 1.0
**Type**: knowledge-pack
**Primary Users**: `email-marketer`, `marketing-dir`, `cmo`, `growth-marketer`

---
<!-- Attribution:
  Frameworks and patterns in this knowledge pack were informed by:
  - Anthropic knowledge-work-plugins (marketing domain reference)
  - Dittofeed (github.com/dittofeed/dittofeed) — email marketing automation patterns
  Adapted and expanded for Product Org OS agents.
-->

## Email Campaign Types

### When to Use Each Type

| Campaign Type | Purpose | Trigger | Typical Length |
|---------------|---------|---------|----------------|
| **Drip** | Time-based education or onboarding | Signup, purchase, event | 3-7 emails over 1-4 weeks |
| **Nurture** | Move leads through funnel stages | Lead score threshold, content download | 5-12 emails over 4-8 weeks |
| **Onboarding** | Activate new users, reduce churn | Account creation, trial start | 4-7 emails over 7-14 days |
| **Re-engagement** | Win back inactive subscribers | Inactivity period (30-90 days) | 2-4 emails over 1-2 weeks |
| **Lifecycle** | Retention and expansion across customer journey | Stage transitions, usage milestones | Ongoing, event-triggered |
| **Promotional** | Drive immediate action (sale, event, launch) | Calendar date, product launch | 1-3 emails over 1-5 days |
| **Transactional** | Confirm actions, deliver information | User action (purchase, password reset) | Single email, immediate |
| **Newsletter** | Build authority, maintain engagement | Regular cadence | 1 per week or month |

### Campaign Selection Framework

```
Lead just entered? ────────────────→ Onboarding / Welcome
Lead engaged but not converting? ──→ Nurture sequence
Lead went cold? ───────────────────→ Re-engagement
Customer hit a milestone? ─────────→ Lifecycle trigger
Time-sensitive offer? ─────────────→ Promotional
Ongoing relationship? ─────────────→ Newsletter
```

### Common Pitfalls
- Running drip and nurture simultaneously to the same contact (causes fatigue and confusion)
- Onboarding sequences that focus on features instead of outcomes
- Re-engagement campaigns that offer discounts before trying value-based messaging
- Lifecycle emails with no behavioral triggers (sending purely on schedule)
- Treating newsletters as promotional blasts instead of value delivery

---

## Subject Line Optimization

### Frameworks

| Framework | Pattern | Example | Best For |
|-----------|---------|---------|----------|
| **Curiosity Gap** | Hint at value without revealing it | "The metric most teams ignore" | Newsletters, content |
| **Benefit-First** | Lead with the outcome | "Cut your onboarding time by half" | Product, promotional |
| **Urgency/Scarcity** | Create time pressure | "Last 24 hours: early pricing ends" | Promotional, events |
| **Question** | Provoke thought | "Is your checkout flow leaking revenue?" | Nurture, re-engagement |
| **Personalization** | Use recipient data | "{FirstName}, your Q2 results are in" | Lifecycle, reports |
| **Social Proof** | Leverage credibility | "Why 500 product teams switched this month" | Nurture, promotional |
| **How-To** | Promise practical value | "How to run a pricing review in 30 minutes" | Content, educational |
| **Contrast** | Challenge assumptions | "Stop A/B testing your homepage" | Thought leadership |

### Subject Line Rules

| Rule | Rationale |
|------|-----------|
| Keep under 50 characters | Mobile truncation starts at ~40-50 chars |
| Front-load the value | Scanning behavior favors first 3-4 words |
| Avoid ALL CAPS and excessive punctuation | Spam filter triggers |
| Test emoji sparingly | Can lift open rates 3-5% but brand-dependent |
| Preview text is part of the subject | Treat the first 40-90 chars of preview text as a subject line extension |
| Never mislead | CAN-SPAM violation and trust destroyer |

### A/B Testing Subject Lines

Test one variable at a time:

| Variable | Test Example |
|----------|-------------|
| Length | Short (4 words) vs. long (10 words) |
| Tone | Formal vs. conversational |
| Personalization | With {FirstName} vs. without |
| Format | Question vs. statement |
| Specificity | "Improve your emails" vs. "3 subject line fixes that doubled opens" |

Minimum sample: 1,000 recipients per variant for statistical significance. Run for at least 2-4 hours before picking a winner.

---

## Email Deliverability

### Authentication Protocols

| Protocol | What It Does | Record Type | Priority |
|----------|-------------|-------------|----------|
| **SPF** | Declares which servers can send on your behalf | TXT on domain DNS | Must-have |
| **DKIM** | Cryptographically signs emails to prove authenticity | TXT on domain DNS | Must-have |
| **DMARC** | Tells receivers what to do when SPF/DKIM fail | TXT on domain DNS | Must-have |
| **BIMI** | Displays brand logo in inbox | TXT + SVG hosted | Nice-to-have |

### DMARC Policy Progression

```
Phase 1: p=none        (monitor only, collect reports)
Phase 2: p=quarantine  (failed emails go to spam)
Phase 3: p=reject      (failed emails are blocked)
```

Start at `p=none` and progress only after reviewing DMARC reports for 2-4 weeks at each stage.

### Domain Warm-Up Schedule

For a new sending domain or IP:

| Week | Daily Volume | Notes |
|------|-------------|-------|
| 1 | 20-50 | Send only to most engaged contacts |
| 2 | 50-150 | Expand to recent openers |
| 3 | 150-500 | Include broader engaged segment |
| 4 | 500-1,500 | Monitor bounce and spam rates |
| 5 | 1,500-5,000 | Scale if metrics are healthy |
| 6+ | Full volume | Gradual ramp to full list |

**Stop and investigate** if bounce rate exceeds 5% or spam complaint rate exceeds 0.1% at any stage.

### Reputation Factors

| Factor | Impact | How to Manage |
|--------|--------|---------------|
| Bounce rate | High | Clean list regularly, validate before sending |
| Spam complaint rate | Critical | Easy unsubscribe, relevant content, proper segmentation |
| Engagement rate | High | Remove unengaged after 90 days inactivity |
| Spam trap hits | Critical | Never use purchased lists, clean regularly |
| Sending consistency | Medium | Maintain regular cadence, avoid sudden volume spikes |
| Content quality | Medium | Avoid spam trigger words, maintain good text-to-image ratio |

### Common Pitfalls
- Skipping warm-up on a new domain (immediate volume = immediate blacklist)
- Setting DMARC to `p=reject` without monitoring phase
- Ignoring Google Postmaster Tools and Microsoft SNDS data
- Using a shared IP when volume is high enough to justify dedicated
- Not separating transactional and marketing sending domains

---

## Segmentation Strategies

### Segmentation Dimensions

| Dimension | Segments | Use Case |
|-----------|----------|----------|
| **Behavioral** | Opened last 30 days, clicked last 7 days, visited pricing page, downloaded whitepaper | Most predictive; use for targeting and suppression |
| **Lifecycle Stage** | Lead, MQL, SQL, Customer, Churned | Different messaging per stage |
| **Engagement Level** | Highly engaged (opens >50%), Moderate (20-50%), Low (<20%), Dormant (no opens 90+ days) | Frequency and content variation |
| **Firmographic** (B2B) | Company size, industry, revenue, tech stack | Personalization and relevance |
| **Demographic** (B2C) | Age, location, gender, preferences | Content and offer targeting |
| **Purchase History** | First purchase, repeat buyer, high-value, lapsed | Retention and cross-sell |
| **Source/Channel** | Organic, paid, referral, event, content download | Attribution and messaging alignment |

### Segmentation Maturity Model

```
Level 1: Batch and blast (one list, same message)
Level 2: Basic segments (customers vs. prospects)
Level 3: Behavioral segments (engagement-based)
Level 4: Dynamic segments (real-time behavior + predictive)
Level 5: 1:1 personalization (individual-level content)
```

### Common Pitfalls
- Over-segmenting to the point where segments are too small to test
- Segmenting on demographics alone without behavioral data
- Static segments that are never refreshed
- Not suppressing recent converters from nurture campaigns

---

## A/B Testing for Email

### What to Test (Priority Order)

| Element | Impact on Results | Ease of Testing |
|---------|-------------------|-----------------|
| Subject line | High | Easy |
| Send time | Medium-High | Easy |
| Sender name | Medium-High | Easy |
| CTA text and placement | High | Medium |
| Email length | Medium | Medium |
| Content format (text vs. HTML) | Medium | Medium |
| Personalization depth | Medium | Medium |
| Offer/value prop | High | Harder (requires variants) |

### Testing Framework

```
1. Hypothesis: "Changing [X] from [A] to [B] will increase [metric] by [amount]"
2. Variable: ONE change per test
3. Sample size: Minimum 1,000 per variant (use sample size calculator for precision)
4. Duration: 2-4 hours for subject line; 24-48 hours for send time
5. Winner criteria: Define before sending (e.g., open rate for subject, CTR for CTA)
6. Significance: 95% confidence level minimum
7. Document: Log result, apply learning to future sends
```

### Common Pitfalls
- Testing multiple variables simultaneously (confounds results)
- Declaring a winner too early (insufficient sample or time)
- Not documenting test results (same tests get repeated)
- Testing trivial changes (button color) before impactful ones (value proposition)
- Ignoring downstream metrics (higher open rate but lower conversion = false win)

---

## Key Metrics and Benchmarks

### Primary Metrics

| Metric | Formula | B2B Benchmark | B2C Benchmark | Alert Threshold |
|--------|---------|---------------|---------------|-----------------|
| **Open rate** | Opens / Delivered | 20-25% | 15-22% | Below 15% |
| **Click-through rate (CTR)** | Clicks / Delivered | 2.5-3.5% | 2-3% | Below 1.5% |
| **Click-to-open rate (CTOR)** | Clicks / Opens | 10-15% | 10-14% | Below 8% |
| **Conversion rate** | Conversions / Delivered | 1-3% | 1-2% | Below 0.5% |
| **Unsubscribe rate** | Unsubs / Delivered | <0.3% | <0.5% | Above 0.5% |
| **Spam complaint rate** | Complaints / Delivered | <0.05% | <0.08% | Above 0.1% |
| **Bounce rate** | Bounces / Sent | <2% | <2% | Above 3% |
| **List growth rate** | (New - Unsubs - Bounces) / Total | 2-5% monthly | 3-8% monthly | Negative |

*Benchmarks are general industry ranges. Actual benchmarks vary significantly by industry, audience, and list quality. Use your own historical data as the primary comparison.*

### Diagnostic Framework

| Symptom | Likely Cause | Investigation |
|---------|-------------|---------------|
| Low open rate | Subject line, sender reputation, send time, list quality | Test subject lines; check deliverability |
| High opens, low clicks | Weak CTA, content mismatch, poor layout | Test CTA placement and copy |
| High clicks, low conversions | Landing page disconnect, wrong audience | Audit landing page alignment |
| Rising unsubscribes | Over-sending, irrelevant content, wrong segment | Survey unsubs; review frequency |
| Increasing spam complaints | Bad list hygiene, misleading subjects, no easy unsub | Audit list source; simplify opt-out |

---

## Sequence Design Patterns

### Timing and Frequency

| Sequence Type | Email Spacing | Rationale |
|---------------|--------------|-----------|
| Onboarding (SaaS) | Day 0, 1, 3, 5, 7, 14 | Front-loaded to drive activation |
| Nurture (B2B) | Every 3-5 days | Enough time to consume content |
| Re-engagement | Day 0, 3, 7, 14 (then suppress) | Escalating urgency, then stop |
| Post-purchase (B2C) | Day 0, 3, 7, 30 | Confirm, educate, cross-sell |
| Cold outreach | Day 0, 3, 7, 14, 21 | Persistent without being aggressive |
| Event/webinar | -14d, -7d, -3d, -1d, +1d | Build anticipation, follow up |

### Sequence Architecture Template

```
Email 1: VALUE FIRST
  Purpose: Deliver immediate value, establish trust
  Tone: Helpful, no ask
  CTA: Soft (read, watch, explore)

Email 2: EDUCATE
  Purpose: Teach something relevant to their problem
  Tone: Expert, practical
  CTA: Content consumption (guide, video, case study)

Email 3: SOCIAL PROOF
  Purpose: Show others succeeding
  Tone: Credible, specific
  CTA: Medium (see results, read case study)

Email 4: OVERCOME OBJECTION
  Purpose: Address the main reason they have not acted
  Tone: Empathetic, direct
  CTA: Medium-hard (start trial, book demo)

Email 5: DIRECT ASK
  Purpose: Clear call to action
  Tone: Confident, concise
  CTA: Hard (buy, sign up, schedule call)

Email 6: BREAK-UP (optional)
  Purpose: Last attempt, create urgency through finality
  Tone: Respectful, final
  CTA: Hard (last chance) or opt-down (change preferences)
```

### Branching Logic

| Trigger | Branch Action |
|---------|---------------|
| Opens but does not click | Send alternative CTA or different content format |
| Clicks but does not convert | Retarget with objection-handling content |
| No opens after 3 emails | Move to re-engagement or suppress |
| Converts mid-sequence | Exit sequence, move to post-conversion flow |
| Replies | Alert sales (B2B) or trigger human follow-up |

### Common Pitfalls
- No exit conditions (contacts get stuck in sequences forever)
- All emails have the same tone and CTA intensity
- Not suppressing contacts who are already in a sales conversation
- Sending sequence emails on top of broadcast emails (overload)
- No behavioral branching (purely time-based)

---

## Template Structure Best Practices

### Email Anatomy

```
┌─────────────────────────────────┐
│ FROM: Recognizable sender name  │
│ SUBJECT: Compelling, <50 chars  │
│ PREVIEW: Extends the subject    │
├─────────────────────────────────┤
│                                 │
│ HEADER: Logo or minimal brand   │
│                                 │
│ OPENING: 1-2 sentences          │
│ (personalized, relevant)        │
│                                 │
│ BODY: Core value / message      │
│ (scannable, short paragraphs)   │
│                                 │
│ CTA: Single, clear button       │
│                                 │
│ FOOTER: Unsub link, address,    │
│ social links, preference center │
│                                 │
└─────────────────────────────────┘
```

### Design Guidelines

| Guideline | Rationale |
|-----------|-----------|
| Single-column layout, max 600px width | Consistent rendering across clients |
| System-safe fonts (Arial, Georgia, Helvetica) or web-safe stacks | Email clients strip custom fonts |
| Minimum 14px body text, 22px headlines | Mobile readability |
| CTA button min 44x44px tap target | Mobile usability |
| Alt text on all images | Images often blocked by default |
| Text-to-image ratio of 60:40 or higher | Spam filter consideration |
| Dark mode compatible colors | Growing dark mode usage |
| Inline CSS only | Many clients strip `<style>` blocks |
| Test in Litmus or Email on Acid | Rendering varies wildly across clients |

### Plain Text vs. HTML

| Use Plain Text When | Use HTML When |
|---------------------|--------------|
| 1:1 sales outreach / cold email | Marketing campaigns and newsletters |
| Personal follow-ups | Product announcements with visuals |
| High-deliverability priority | Brand-heavy communications |
| Executive-level outreach | Transactional emails with layout needs |

---

## Compliance

### CAN-SPAM (United States)

| Requirement | Detail |
|-------------|--------|
| Accurate header information | From, To, Reply-To must be truthful |
| Non-deceptive subject lines | Subject must reflect email content |
| Identify as advertisement | If commercial, must be identifiable as ad |
| Physical mailing address | Valid postal address required in every email |
| Opt-out mechanism | Clear, conspicuous, functional unsubscribe |
| Honor opt-outs within 10 business days | Process unsubscribes promptly |
| Monitor third-party senders | You are responsible for emails sent on your behalf |

### GDPR (European Union)

| Requirement | Detail |
|-------------|--------|
| Lawful basis for processing | Consent (opt-in) or legitimate interest |
| Explicit consent for marketing | Pre-checked boxes are NOT valid consent |
| Right to be forgotten | Must delete data upon request |
| Data portability | Must provide data in machine-readable format |
| Record of consent | Must prove when and how consent was obtained |
| Privacy policy link | Required in emails |
| Double opt-in recommended | Not legally required but strongly recommended |

### CASL (Canada)

| Requirement | Detail |
|-------------|--------|
| Express consent required | Implied consent allowed only in limited cases |
| Identification of sender | Name, address, contact info |
| Unsubscribe mechanism | Must process within 10 business days |
| Record-keeping | Maintain proof of consent |

### Common Pitfalls
- Assuming "legitimate interest" covers cold email in the EU (it rarely does for marketing)
- No double opt-in for EU subscribers (not required but risky without it)
- Missing physical address in email footer
- Unsubscribe link that requires login or multiple steps
- No consent record (burden of proof is on the sender)

---

## Cold Email vs. Warm Email

### Key Distinctions

| Dimension | Cold Email | Warm Email |
|-----------|-----------|------------|
| **Relationship** | No prior contact or opt-in | Existing relationship or opt-in |
| **Legal basis** | Varies by jurisdiction (risky in EU) | Consent or legitimate interest |
| **Sending domain** | Separate domain to protect main reputation | Primary brand domain |
| **Volume** | Low (50-100/day during warm-up) | Higher (list-dependent) |
| **Personalization** | Must be high (1:1 feel) | Can be segment-level |
| **Format** | Plain text, short, conversational | HTML or plain text depending on type |
| **CTA** | Soft (reply, quick question) | Can be direct (sign up, buy, book) |
| **Tracking** | Minimal (pixel tracking can hurt deliverability) | Standard open/click tracking |
| **Follow-up** | 2-4 manual-feeling follow-ups | Automated sequences acceptable |
| **List source** | Prospected, researched | Opted-in, imported with consent |
| **Unsubscribe** | Required (but can be reply-based) | Required (link in footer) |

### Cold Email Best Practices

| Practice | Rationale |
|----------|-----------|
| Use a separate sending domain (e.g., `company.co` not `company.com`) | Protects main domain reputation |
| Warm up the domain for 2-4 weeks before outreach | Builds sender reputation gradually |
| Keep under 150 words | Busy people skim; shorter emails get more replies |
| One CTA per email (usually a question) | Reduces cognitive load |
| Personalize the first line with research | Shows effort, avoids spam perception |
| Send from a real person, not `team@` or `noreply@` | Personal sender names get higher opens |
| Space follow-ups 3-7 days apart | Persistent without being aggressive |
| Stop after 3-4 touches if no engagement | Respect the signal |
| Verify email addresses before sending | Reduces bounce rate, protects reputation |
| Rotate subject lines across sequences | Avoids pattern-based spam filtering |

### Cold Email Anti-Patterns

| Anti-Pattern | Why It Fails |
|--------------|-------------|
| Sending 500+ cold emails on day one | Instant reputation damage |
| Generic "I noticed your company..." openings | Screams template, gets deleted |
| Long emails with company history | Nobody reads them |
| HTML-heavy cold emails with images | Triggers spam filters, feels impersonal |
| No follow-up sequence | Most replies come on follow-up 2-4 |
| Buying email lists | Destroys deliverability, potential legal liability |
| Same email to everyone in a company | Looks like spam; one per company is the ceiling |

---

## Deliverability Checklist

Before every campaign send:

- [ ] SPF, DKIM, and DMARC records configured and passing
- [ ] Sending domain is warmed up (or volume is within warm-up schedule)
- [ ] List cleaned within last 30 days (bounces and inactive removed)
- [ ] Spam complaint rate below 0.1%
- [ ] Unsubscribe link present and functional
- [ ] Physical address in footer
- [ ] Subject line tested (no spam trigger words, appropriate length)
- [ ] HTML renders correctly in major clients (Gmail, Outlook, Apple Mail)
- [ ] Plain text version included
- [ ] Tracking links are not blacklisted
- [ ] Test email sent and reviewed before broadcast

---

## Quick Reference: Email Timing

| Audience | Best Send Days | Best Send Times | Avoid |
|----------|---------------|-----------------|-------|
| B2B | Tuesday-Thursday | 9-11 AM recipient's timezone | Weekends, Monday AM, Friday PM |
| B2C | Tuesday, Thursday, Saturday | 10 AM, 1 PM, 8 PM recipient's timezone | Monday, late night |
| SaaS/Tech | Tuesday-Thursday | 10-11 AM | Friday afternoon |

*These are starting points. Always test send times with your specific audience and optimize from your own data.*

---

## 2026 Inbox-Experience Shift (as of 2026-06-24)

<!-- Attribution (2026-06-24 additive delta):
  Adapted from: MarTech "What Apple and Google's 2025 updates mean for email and SMS in 2026" (martech.org, 2026-01-28); DemandGen Report / Validity (Guy Hanson) on AI, authentication and engagement reshaping B2B email (demandgenreport.com, 2026-06).
  Source licence: per-source-terms (publicly published trade-press analysis; cited, not claimed).
  V2V refinements: translated the 2025-2026 inbox-experience changes into product-org email-ops guidance; reframed the primary KPI from open-rate to engagement consistent with this pack's existing diagnostic framework; cross-referenced deliverability-engineering.md for the sender-reputation layer. No fabricated metrics — all figures are directional and platform-behavioral, not performance claims.
-->

The Feb-2024 Gmail/Yahoo sender rules (above) are about *getting to* the inbox. A second, distinct shift through 2025 into 2026 changed what happens *inside* the inbox — how messages are displayed, grouped, and engaged with. These are platform-behavioral changes, not deliverability changes, and they alter strategy independently of authentication.

### What changed

| Change | What it does | Strategy implication |
|--------|-------------|----------------------|
| **Apple iOS 18.2 inbox tabs** | New tabs reduce Primary-inbox exposure (similar to Gmail's promotions tab) | Plan content calendars for send-succession and visual differentiation; assume marketing mail competes in a tabbed/grouped view |
| **Apple AI-generated previews** | Apple Intelligence summaries replace marketer-written preheaders in some views; render better from HTML + live text than from image-heavy email | Prioritize live text over images; you no longer fully control the first-impression snippet, so the body's opening must carry the message |
| **Gmail "Manage subscriptions"** | Centralized unsubscribe view that sorts senders by email volume, then alphabetically | Frequency is now the single most-visible unsubscribe driver. Align cadence to engagement: reduce frequency for low-engagement/at-risk segments, reserve higher cadence for the highly engaged |
| **Apple iOS 26 SMS "unknown sender" filter** | Diverts brand SMS from unsaved numbers out of the primary message view (SMS analog of the promotions tab) | Adoption is muted so far but rising; prompt "known sender" actions (save-the-contact) post-purchase and in welcome flows; shift SMS from volume to high-utility (order/shipping/back-in-stock) |

### The KPI reframe: engagement, not opens

Apple Mail Privacy Protection (2021+) already inflated open rates; the 2026 AI-summary and inbox-grouping layer compounds it (grouped emails, untrackable "See more" clicks). **Open rate is no longer a reliable primary KPI.** Optimize for downstream engagement — clicks, replies, conversions, and journey progression — and use behavior-based segmentation (per the Segmentation section above) as the lever. This is consistent with this pack's existing Diagnostic Framework: when opens are unreadable, you diagnose from CTR/CTOR/conversion and list-health trend, not from open rate. Treat subscribers who self-unsubscribe via Gmail's feature as a list-hygiene signal (they would likely have churned anyway), not as a failure.

### Cross-reference

The sender-reputation / authentication layer (DMARC, warm-up, the 5pp spam-flag gap, the Microsoft Feb/Apr 2026 enforcement waves) lives in `deliverability-engineering.md` and is unchanged by this inbox-experience shift. This section covers display and engagement; that pack covers placement.

---

## Operating Principle

> "The inbox is sacred ground. Every email is a withdrawal from the trust account. Deliver value first, ask second, and never forget that unsubscribe is one click away."
