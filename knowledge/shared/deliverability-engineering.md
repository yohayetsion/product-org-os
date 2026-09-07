---
pack: deliverability-engineering
consumers:
- sdr
- sales-ops
---
# Deliverability Engineering — V2V Knowledge Pack

**Version**: 1.0
**Type**: knowledge-pack
**Primary Users**: `sdr`, `sales-ops`, `sales-dir`, `account-exec`
**Secondary Users**: `email-marketer`, `growth-marketer`, `product-operations`
**Joint authors**: SDR + Sales Ops (D15 joint-authoring lens)
**Token budget variance rationale**: D14 case (a) + (b) — joint-authored deliverability discipline + multi-seat consumer base across sales-team + sdr

---

**Adapted from**:
  - Smartlead deliverability patterns (publicly documented vendor playbooks, smartlead.ai)
  - DMARC (RFC 7489), SPF (RFC 7208), DKIM (RFC 6376), BIMI draft RFC, ARC (RFC 8617)
  - Google Postmaster Tools + Microsoft SNDS (publicly documented sender-reputation surfaces)
  - 11x AI-SDR scandal post-mortem (public coverage 2025-2026, Q1 2025 reputational collapse; Artisan billboard backlash Q2 2025; Salesloft-Clari consolidation Q3 2025)
  - Gmail / Yahoo sender requirements (Feb 2024 enforcement: DMARC mandatory for bulk senders >5K/day, one-click unsubscribe RFC 8058, 0.3% spam-rate threshold)
  - Microsoft sender requirements (2024-2025 tightening; SNDS Yellow/Red thresholds)
  - Microsoft sender enforcement, Feb + Apr 2026 waves (per vendor/agency reporting: litemail.ai, leadhaste, scaledmail) — NOT a primary Microsoft sender-guidelines source; see 2026-06 delta caveat

**Source licence**: per-source-terms; IETF RFCs are public; Gmail/Yahoo/Microsoft sender requirements are public technical specifications; the Feb/Apr 2026 Microsoft figures are vendor/agency-reported, not Microsoft-confirmed (see 2026-06 delta)

**V2V refinements**:
- Translated deliverability discipline to product-organization SDR + Sales Ops adoption (the operating discipline, NOT vendor selection — vendor procurement belongs to `procurement-specialist` + `sales-ops` jointly)
- Codified the 5pp spam-flag gap as a campaign-killer threshold for product-org SDR ops (the only sender-reputation metric a regulator can actually subpoena)
- Cross-referenced `sdr` SKILL.md update (Q2-7.3) — anti-patterns codify the lessons from 11x scandal without naming-and-shaming
- Added V2V Phase 4 (Execution) gate definitions — deliverability-health pre-send checks, who acts on alerts, block-and-redirect protocol
- Separated authentication (binary, set-and-monitor) from engagement (continuous, the actual lever) — most teams over-invest in the first, under-invest in the second
- 2026-06 delta: added Microsoft Feb + Apr 2026 sender-enforcement reporting with an explicit confidence caveat (vendor/agency-sourced, not Microsoft-confirmed; verify against SNDS / official guidelines before hard-coding thresholds)

---

## 2026-06 Delta Update (as of 2026-06-06)

> ⚠️ **Confidence caveat (read first).** The specific Microsoft numbers in this section come from **vendor/agency blogs (litemail.ai, leadhaste, scaledmail), NOT a primary Microsoft sender-guidelines page**. They are directionally consistent with the broader Gmail/Yahoo/Microsoft tightening trend, but they are **per vendor/agency reporting; verify against Microsoft's official SNDS / sender guidelines before hard-coding any threshold into a send-gate.** Do NOT present these numbers as Microsoft-confirmed.

Microsoft tightened cold-email / outbound enforcement in two reported 2026 waves (February and April 2026). Reported changes:

| Reported change | Reported figure | Prior state | Note |
|---|---|---|---|
| **Spam-complaint auto-flag threshold** | cut to **0.10%** | reported 0.30% | Now reportedly matches Google's 0.10% Green→Yellow boundary (see §"The 5pp Spam-Flag Gap"). If accurate, the Microsoft headroom that existed at 0.30% is gone. |
| **New-domain daily send limit** | ~**200/day with a 30-day ramp** | reported 500/day after a 7-day ramp | If accurate, slows new-domain warmup materially; tighten the Layer 4 volume-ramp schedule for Microsoft-heavy recipient bases. |
| **Minimum domain age** | raised **7 → 14 days** | reported 7 days | Aligns with the existing 14-30 day domain-warmup rule (Layer 2); no change to V2V guidance, which already requires 14-30 days. |
| **DMARC `p=reject` enforcement** | enforced on flagged domains | — | Consistent with the DMARC progression rule (Layer 1); flagged domains reportedly pushed to `p=reject`. |
| **NEW engagement-signal monitor** | open rate under ~**8% over 72h** reportedly triggers review | did not exist | If accurate, this is a new *engagement* (not just authentication) gate on the Microsoft side — reinforces Layer 5 (reply-rate engineering) as the actual lever. Note open-rate is itself an unreliable signal (Apple MPP); treat any open-rate-based gate skeptically. |

### How to treat these in send-gates

Until confirmed against a primary Microsoft source (SNDS dashboard documentation or Microsoft's published sender guidelines):

- **Do NOT hard-code 0.10% / 200-per-day / 8%-open as Microsoft block thresholds.** Keep them as *investigate* signals, not *block* signals, in the Layer 4 / Phase-4-gate tables.
- The existing V2V thresholds (Layer 3 list-hygiene ceilings; the 2pp-investigate / 3pp-block spam-flag posture in §"The 5pp Spam-Flag Gap") already operate at or below these reported Microsoft figures, so V2V's conservative posture is unaffected even if the reports are accurate.
- Assign a human to confirm against SNDS before any threshold is promoted from "investigate" to "block."

**Sources (vendor/agency — NOT Microsoft-primary)**: https://litemail.ai/blog/microsoft-cold-email-policy-2026 ; https://leadhaste.com/blog/google-microsoft-sender-guidelines ; https://www.scaledmail.com/blogs/email-deliverability-news

---

## Why Deliverability Engineering Matters in 2026

The 2024-2025 AI-SDR pure-play category collapsed under three converging forces. **11x** (the highest-profile AI-SDR pure-play, Series B 2024, claimed "AI digital workers replacing your SDR team") hit reputational crisis in Q1 2025 after public coverage of inflated customer counts, ghost-customer testimonials, and — most relevant here — deliverability collapse across the customer base when autonomous sending volumes outran sender reputation. **Artisan's** 2024 billboard campaign ("Stop hiring humans") triggered Q2 2025 backlash that converted what was a positioning controversy into a buyer-side conversation about whether the underlying outbound was even landing in inboxes. By Q3 2025, **Salesloft-Clari** consolidation signaled that the standalone-outbound-tool category was collapsing into the broader revenue-operations stack, with deliverability moving from a vendor feature to a platform capability.

The consensus 2026 outbound playbook that emerged from that collapse is unambiguous: **human-in-loop send approval + deliverability discipline**. AI assists with drafting, prioritization, personalization research, and sequence design — but a human approves the send, the volume ramps slowly, and the sender-reputation telemetry is monitored continuously. The structural reason is not philosophical: it's that **the 5-percentage-point spam-flag gap between AI-autonomous-sent and human-approved-sent campaigns is the threshold at which Gmail Postmaster flips a domain from Green to Yellow reputation, and Yellow-reputation campaigns lose roughly 60-80% of inbox placement to spam folders.** A 5pp gap kills the campaign; the campaign just doesn't know it for 7-14 days because the bounce path is silent.

The 2024 Gmail/Yahoo sender requirements (effective Feb 2024) made this structural. Bulk senders (>5K messages/day to Gmail) MUST publish DMARC, MUST honor one-click unsubscribe (RFC 8058), and MUST stay below a 0.3% spam-complaint rate or face progressive throttling. Microsoft followed with comparable SNDS Yellow/Red thresholds in 2024-2025. The regulatory and platform pressure means deliverability is no longer a marketing-ops concern hidden inside a vendor's dashboard — it is a product-organization governance concern with regulatory exposure (CAN-SPAM 15 U.S.C. §7701, GDPR Article 6(1)(a) marketing consent, UK PECR Regulation 22) and a board-level reputational tail.

This pack codifies the engineering discipline. It is operational reference, not legal advice. The regulatory layer lives in `compliance-frameworks.md` and `privacy-frameworks.md`.

---

## The Deliverability Stack

Five layers, ordered by what most teams get wrong:

```
┌─────────────────────────────────────────────────┐
│ 5. Reply-Rate Engineering    (the only lever)  │
├─────────────────────────────────────────────────┤
│ 4. Send-Pattern Discipline   (volume + variance)│
├─────────────────────────────────────────────────┤
│ 3. List Hygiene              (input quality)   │
├─────────────────────────────────────────────────┤
│ 2. Sending Infrastructure    (IP + domain)     │
├─────────────────────────────────────────────────┤
│ 1. Authentication            (DMARC/SPF/DKIM)  │
└─────────────────────────────────────────────────┘
```

Most teams invest top-to-bottom (authentication is the most-documented and easiest to "complete"). The actual lever is reverse — reply-rate engineering and send-pattern discipline drive sender reputation; authentication is necessary but binary.

### Layer 1 — Authentication: DMARC + SPF + DKIM

| Standard | RFC | Purpose | What "configured correctly" means |
|---|---|---|---|
| **SPF** | RFC 7208 | Declares which IPs may send mail "From" your domain | TXT record published; `~all` (softfail) acceptable, `-all` (hardfail) preferred once stable; <10 DNS lookups (SPF flattening if needed) |
| **DKIM** | RFC 6376 | Cryptographic signature on outbound mail | 2048-bit key minimum (1024-bit deprecated); rotated quarterly; selector per sending service |
| **DMARC** | RFC 7489 | Policy on how receivers handle SPF/DKIM failures + aggregate reporting | Published at `_dmarc.{domain}`; `p=none` during ramp → `p=quarantine` → `p=reject`; `rua=` aggregate reports parsed weekly minimum |
| **BIMI** | Draft RFC | Logo display in supported clients | Requires `p=reject` DMARC + VMC certificate; nice-to-have, not a deliverability lever |
| **ARC** | RFC 8617 | Authentication chain for forwarded mail | Set by receivers; consumer side, not sender side |

**The DMARC progression rule (NON-NEGOTIABLE)**: never start at `p=reject`. Sequence is `p=none` (monitor only, learn what's failing) → `p=quarantine` (failures to spam folder) → `p=reject` (failures bounced). Skipping stages causes legitimate mail (forwarded, mailing-list-mediated, marketing-platform-routed) to bounce silently. Minimum 30 days per stage; aggregate reports MUST be parsed before progressing.

**Aggregate reports (the part most teams skip)**: DMARC `rua=` reports arrive as XML, typically once per day per receiver. Without parsing them, you have no visibility into the authentication failures that are silently killing your campaigns. Parsers: Postmark DMARC Digests (free for low volume), dmarcian, Valimail, Easydmarc — pick one and assign a human to read the weekly digest.

### Layer 2 — Sending Infrastructure

| Decision | Default | When to deviate |
|---|---|---|
| **Dedicated IP vs shared** | Shared for <50K msgs/month; dedicated for >150K/month | High-volume senders need IP isolation to control reputation; small senders need pooled-reputation lift |
| **IP warmup** | 30-45 day ramp on a dedicated IP | Cannot be skipped; ESPs that claim "no warmup needed" are routing through pre-warmed shared pools and you are inheriting reputation risk you don't see |
| **Domain warmup** | 14-30 days for a new sending domain | More important than IP warmup; receivers track domain reputation as primary signal post-2022 |
| **Subdomain strategy** | Send cold outbound from a subdomain (`outreach.company.com`), NOT main domain | Protects main-domain reputation if cold campaign tanks; allows separate DMARC policy; segregates aggregate reports |
| **Reply domain** | Match sending subdomain | Mismatched reply domains trigger receiver heuristics; Gmail flags as suspicious |

**The subdomain rule (LOAD-BEARING)**: cold outbound NEVER sends from your main corporate domain. The reputational tail of a failed cold campaign is 60-90 days of degraded transactional-email deliverability if you commingle. Use `outreach.yourcompany.com` or `mail.yourcompany.com` with isolated DMARC policy. Transactional mail stays on the main domain with `p=reject` DMARC; outbound stays on the subdomain with its own progression.

### Layer 3 — List Hygiene

| Metric | Hard Ceiling | Where measured |
|---|---|---|
| **Bounce rate (Gmail)** | 0.3% | Google Postmaster |
| **Bounce rate (Microsoft)** | 0.5% | SNDS |
| **Spam complaint rate** | 0.3% (Gmail enforcement Feb 2024) | Google Postmaster, Yahoo CFL, Microsoft JMR |
| **Unsubscribe rate** | <0.5% per send (warning sign at >0.5%) | ESP dashboard |
| **Inactive contact pruning** | 90-day no-open → suppression | Internal CRM + ESP sync |

**The validation pre-send rule**: every list runs through email validation (NeverBounce, ZeroBounce, Hunter Verifier, Smartlead-built-in) before send. Disposable-address filtering, catch-all detection, role-address flagging (`info@`, `sales@` get downweighted). Lists from PDL / Apollo / cold scraping have 8-15% invalid rate at acquisition; sending unvalidated lists is the fastest way to a bounce-rate spike that flips reputation Red.

**Engagement-based pruning (the part most teams skip)**: contacts who never open in 90 days are not "future converts you haven't reached yet" — they are dead-weight that drags your engagement metrics below the threshold receivers use to classify sender reputation. Suppress them. Re-engagement campaigns (`email-marketing.md` §re-engagement) can attempt revival, but a contact that doesn't open the re-engagement either gets hard-suppressed.

### Layer 4 — Send-Pattern Discipline

| Pattern | Human-like | Robotic (kills reputation) |
|---|---|---|
| **Volume ramp** | 20-50 emails/day from new infrastructure, doubling weekly until target volume | 500/day from day one |
| **Time-of-day** | 9am-11am + 2pm-4pm recipient-local time, with ±15min jitter | Cron-batched at :00:00 of every hour |
| **Day-of-week** | Tue/Wed/Thu primary; Mon/Fri secondary; weekend NEVER for cold outbound | All 7 days |
| **Per-recipient cadence** | One email per recipient per sequence step; sequence steps spaced 3-5 days minimum | Multiple touches per day to same recipient |
| **Sequence length** | 3-5 touches over 2-3 weeks, then stop | 12+ touches over 2 months |
| **Inter-send jitter** | 30-180 seconds between sends from same IP | Burst-sent batches |

**The volume-ramp rule (NON-NEGOTIABLE)**: receivers measure sender reputation in part by send-volume velocity. A new domain going from 0 → 500/day in week one will trip Gmail's volume-anomaly heuristic and land in spam regardless of authentication. Smartlead's documented warmup pattern (20 → 40 → 80 → 160 over four weeks) is approximately right; the exact curve matters less than the discipline of staying under 2x week-over-week growth during warmup.

**The Sat/Sun rule**: the operator's own outreach guardrails should enforce no-weekend-send on the operational side. Deliverability adds the engineering rationale: weekend-sent cold outbound has 2-3x higher spam-complaint rate because the recipient is in personal-time mindset, not work-mindset, and treats the inbox differently. Saturday-sent campaigns measurably damage sender reputation.

### Layer 5 — Reply-Rate Engineering

**Reply rate is the only deliverability lever you can actually pull post-send.** Open rates are unreliable (Apple Mail Privacy Protection 2021+ inflates them); click rates are useful but lagged; bounce and complaint rates are damage-already-done. Reply rate is what receivers most heavily weight in sender reputation, and it is what your copy and targeting actually control.

| Cold outbound segment | Reply-rate floor | Reply-rate target | Reply-rate ceiling (real) |
|---|---|---|---|
| Cold prospecting (B2B SaaS) | <2% = spam risk | 3-8% | 10-15% is exceptional, not normal |
| Warm prospecting (referral/intent) | <5% = audit copy | 8-15% | 20%+ achievable |
| Nurture sequence (opted-in) | <8% = sequence broken | 10-20% | — |

**Below 2% reply rate, your spam-flag rate will be above 0.3% within 2-4 weeks regardless of authentication and infrastructure quality.** The mechanism: low-engagement mail accumulates as "not-spam-but-not-engaged" in receiver classifiers, which over time fold it into the spam-folder default for that sender. Once it's spam-foldered, complaint rate spikes (users mark from spam folder), and the reputation degrades further. The only fix is to stop sending until copy/targeting are diagnosed.

**Reply-rate diagnosis ladder** (when reply rate is below floor):
1. Targeting: is the list actually ICP-fit? (Most common root cause; rare to admit.)
2. Subject line: is it pattern-matched to spam? (`Quick question`, `Following up`, `RE:` prefix on first send — all degraded in 2025-2026.)
3. First-line personalization: is the opener obviously templated?
4. Ask: is the ask too big for first touch? (Demo request on email 1 is usually too big.)
5. Length: is it over 90 words? (Mobile-read cold outbound caps at 90.)

---

## The 5pp Spam-Flag Gap

The structural threshold for product-organization SDR ops. Stated precisely:

> **If your AI-assisted or AI-autonomous cold outbound shows a spam-complaint rate more than 5 percentage points above your human-approved baseline, the campaign is structurally broken and continuing to send accelerates reputation damage.**

### Why 5pp

The 5pp number is not arbitrary. It maps to three independent mechanics:

1. **Gmail Postmaster reputation transitions**: the Green → Yellow boundary sits at approximately 0.1% complaint rate; Yellow → Red at 0.3%. A 5pp gap (e.g., human-sent at 0.1%, AI-autonomous-sent at 5.1%) is two reputation tiers separated, not "a bit worse." The gap is the categorical signal.
2. **Microsoft SNDS Yellow threshold**: Yellow status at 0.3% complaint-equivalent, Red at 0.5%. Same categorical-transition mechanic.
3. **2025 published data from Smartlead, Lemlist, Instantly aggregate dashboards** (vendor-published, public): AI-autonomous campaigns averaged ~5-7pp higher spam-flag rate vs human-approved campaigns across the cohort. This was the data point that drove the consensus 2026 playbook shift to human-in-loop.

### Honest read: is 5pp actually the right threshold?

5pp is the *campaign-killer* threshold. It is not the *invest-in-fixing* threshold. **The investigate threshold is 2pp.** Once the gap exceeds 2pp, the campaign is degrading even if it's not yet flipped Yellow on Postmaster. Most teams find this out only at 5-7pp because that's when the absolute spam rate crosses Postmaster's display threshold and they get notified. By then, reputation recovery takes 30-60 days.

For 2026, with Gmail / Yahoo / Microsoft enforcement tightening and DMARC-mandatory now baseline, **a stricter operating threshold of 2pp investigate / 3pp block is the right product-organization SDR ops posture.** 5pp remains the documented "structural killer" — but a product organization that waits for 5pp is leading from behind.

### How to measure

| Source | What it gives you | Cadence |
|---|---|---|
| **Google Postmaster Tools** | Domain reputation (Green/Yellow/Red), IP reputation, spam-rate %, authentication pass rate, encryption rate, delivery error rate | Daily check; weekly review |
| **Microsoft SNDS** | IP-level data: complaint rate, trap hits, sample volume, color (Green/Yellow/Red) | Daily check; weekly review |
| **Yahoo CFL (Complaint Feedback Loop)** | Per-message complaint stream | Real-time webhook |
| **DMARC aggregate reports (rua)** | Authentication-failure XML from all major receivers | Daily ingest; weekly digest review |
| **ESP / Smartlead / Instantly dashboards** | Reply rate, open rate (proxy), bounce rate, sequence-level engagement | Per-send + weekly trend |

The 5pp (or 2pp) gap is computed as: `(AI-assisted-spam-rate) - (human-approved-baseline-spam-rate)` across a comparable 14-day window with comparable send volumes and recipient cohorts. Not comparable cohorts = not a valid comparison.

---

## V2V Phase 4 (Execution) Gates

V2V Phase 4 is where campaigns actually ship. Deliverability-engineering Phase 4 gates are pre-send health checks owned by Sales Ops, with SDR as the execution agent. Block-and-redirect protocol activates when health degrades.

### Pre-send gates (every campaign, every send)

| Gate | Owner | Block-on-fail |
|---|---|---|
| DMARC published at `p=quarantine` minimum on sending subdomain | `sales-ops` | YES |
| SPF + DKIM passing on sending IP (verified via test send to seed inbox before campaign) | `sales-ops` | YES |
| List validated within 7 days (NeverBounce / equivalent), <2% invalid retained | `sdr` | YES |
| Volume ramp respected (per warmup schedule; no >2x week-over-week increase) | `sales-ops` | YES |
| Sending day NOT Saturday/Sunday | `sdr` | YES |
| Reply-to address active and monitored (not `noreply@`) | `sdr` | YES |
| One-click unsubscribe (RFC 8058) implemented for any send >100 recipients | `sales-ops` | YES |
| Human-approved send (per `sdr` SKILL.md anti-pattern: no autonomous sending) | `sdr` + human reviewer | YES |

### Post-send health monitoring (weekly minimum)

| Signal | Threshold | Action |
|---|---|---|
| Gmail Postmaster spam-rate | >0.1% | INVESTIGATE: copy/targeting audit |
| Gmail Postmaster spam-rate | >0.3% | BLOCK: pause campaign, run reply-rate diagnosis ladder |
| Gmail Postmaster reputation | Yellow | BLOCK: pause new sequence starts; let in-flight sequences complete |
| Gmail Postmaster reputation | Red | EMERGENCY BLOCK: pause everything; 30-60 day reputation recovery |
| SNDS color | Yellow | INVESTIGATE: IP-level audit |
| SNDS color | Red | EMERGENCY BLOCK |
| Reply rate, week-over-week | Drop >30% | INVESTIGATE: targeting/copy degradation |
| 5pp gap (AI vs human-approved baseline) | >2pp | INVESTIGATE |
| 5pp gap (AI vs human-approved baseline) | >5pp | BLOCK |
| Hard bounce rate | >1% on a single send | BLOCK: list quality compromised |
| DMARC aggregate authentication-pass rate | <95% | INVESTIGATE: misconfigured sender or spoofing |

### Block-and-redirect protocol

When a gate triggers BLOCK:

1. **Pause sending on the affected sending subdomain immediately** (not "tomorrow," not "after this week's campaign").
2. **Notify**: `sales-ops` opens an incident; `sdr` owns root-cause investigation; `sales-dir` is informed; if reputation hits Red, `vp-product` is informed.
3. **Diagnose** using reply-rate ladder + list-hygiene audit + Postmaster trend review.
4. **Redirect** in-flight engaged conversations to a clean sending subdomain (`outreach2.yourcompany.com` with its own warmup) only if the in-flight conversation is high-value and at risk of dying during recovery. Otherwise let in-flight sequences complete on the affected subdomain (they're already in inboxes; adding new sends is what compounds damage).
5. **Recover**: 30-60 days minimum at reduced volume (10-20% of prior baseline) with continuous monitoring. Reputation recovery is not linear; expect 14-21 days before any signal change.
6. **Post-mortem**: documented in `context/learnings/` per `context-management.md`.

---

## Anti-Patterns / Common Failures (the 11x lesson, generalized)

The 2025 AI-SDR pure-play collapse was not a single failure — it was a pattern. Codifying without naming-and-shaming:

| Anti-Pattern | What goes wrong | The lesson |
|---|---|---|
| **Autonomous AI-SDR with no human approval gate** | AI generates draft → AI sends → no human reviews copy, targeting, or send timing. Volumes scale faster than reputation; spam-flag gap opens to 5-10pp; reputation flips Red across the customer base. | Human approval is not theatrical. It is the only mechanism that catches the targeting/copy degradation that drives the spam-flag gap. |
| **Spray-and-pray volume scaling** | Vendor claims "send 10x more with AI"; team enables it; volume goes 500 → 5000/day in week two. Receivers trip volume-anomaly heuristics regardless of authentication. | Volume scaling is bounded by reputation, not infrastructure. Authentication + IP isolation do not buy you a free volume ramp. |
| **Main-domain cold outbound** | Cold campaign sent from `yourcompany.com` (not a subdomain). Campaign tanks; transactional email deliverability degrades for 60-90 days; SOC2 audit notices that customer-facing emails are landing in spam. | Subdomain isolation is load-bearing. Reputational tail of a failed cold campaign on main domain is months. |
| **Missing DMARC aggregate monitoring** | DMARC published as `p=reject` from day one; nobody parses the `rua=` reports; legitimate mail (forwarded, mailing-list-routed) silently bounces for months; campaigns and partner notifications both broken. | DMARC reports are not optional. Parse them weekly minimum. |
| **Reply rate treated as "soft metric"** | Dashboard shows 1.2% reply rate; team focuses on "lift open rate"; spam-flag rate accumulates silently; campaign tanks 3 weeks later. | Reply rate is the leading indicator. Below 2%, you are 2-4 weeks from a reputation event. |
| **Spam-flag rate treated as recoverable** | Reputation hits Yellow; team assumes "we'll fix it next quarter"; volume continues; reputation hits Red; recovery takes 60-90 days during which all outbound is degraded. | Spam-flag rate is sticky. The longer it persists, the longer recovery takes. Treat Yellow as a hard pause. |
| **Outsourced deliverability to the vendor** | "Smartlead handles deliverability." Team never opens Postmaster Tools, never parses DMARC reports, never owns the metric. Vendor delivers technically but reputation lives on customer domains, not vendor IPs. | Vendor manages infrastructure. You own reputation. The metric responsibility cannot be outsourced. |
| **Cold outbound from a personal/founder mailbox** | Founder sends "personal" cold outbound from `founder@yourcompany.com` to scale founder-led outbound. Founder's email reputation tanks; founder can no longer reach investors, customers, board. | Founder mailbox is irreplaceable. Never use it for cold outbound. Use a sending subdomain. |
| **No warmup on a new sending domain** | New `outreach.yourcompany.com` set up Friday; 1000-message campaign sent Monday. Domain has zero reputation history; receivers default to spam folder; campaign tanks. | Domain warmup is 14-30 days minimum. No exceptions. |

**The 11x lesson, stated cleanly**: the AI-SDR pure-play model failed not because the AI couldn't write reasonable copy (it could), but because **autonomous-sending volume outran sender reputation**, and the spam-flag gap that opened was invisible until it was structural. The 2026 playbook puts a human in the approval loop specifically to catch the targeting, copy, and send-pattern issues that AI-only loops cannot self-diagnose because the failure signal (sender reputation) arrives 7-14 days after the bad send and is invisible to the AI itself.

---

## V2V Cross-References

**Sibling Q2-7 packs**:
- **`ai-native-rfp.md` (Q2-7.2)** — parallel sales-funnel discipline. Both packs share the input-quality + auditability + cadence pattern. Deliverability infrastructure is a procurement criterion in AI-native RFP scoring when RFPs evaluate outbound-tooling vendors.
- **Q2-7.3 `sdr` SKILL.md update** — consumes this pack's anti-patterns. Autonomous-send-without-human-approval is codified Anti-Pattern #1 in the SDR update; 5pp spam-flag gap is the SDR's operational threshold.

**Sibling Q2-6 packs**:
- **`mmm-modeling.md` (Q2-6.1)** — outbound SDR motion measured as a channel at the aggregate MMM level; deliverability health (5pp spam-flag gap) bounds the legitimate send volume MMM can attribute conversions to.
- **`retention-marketing.md` (Q2-6.2)** — lifecycle re-engagement and win-back sequences (Discipline 3 in that pack) inherit deliverability discipline; re-engagement sends to disengaged contacts carry elevated spam-flag risk and require the same 5pp-gap monitoring.

**Sibling Q2-4 packs**:
- **`customer-success-methodology.md` (Q2-4.3 refresh)** — transactional customer-facing email reputation is protected by the §"Sending Infrastructure" subdomain rule; commingling cold outbound with main-domain transactional mail damages CS communication paths.

**Existing packs**:
- `/outreach-frameworks` — cadence design, sequence structure (upstream of this pack).
- `/sales-frameworks` — pipeline mechanics (where deliverability KPIs roll up to).
- `email-marketing.md` — lifecycle, nurture, re-engagement campaign design (sister pack for marketing-owned email).
- `sales-operations.md` — instrumentation, dashboard design, ops cadence (where deliverability gates live operationally).
- `compliance-frameworks.md` — CAN-SPAM, regulatory layer.
- `privacy-frameworks.md` — GDPR Article 6(1)(a), UK PECR, marketing consent.

**Rule files**: this pack assumes the operator maintains two rules of their own — one
for operational outreach guardrails (weekend block, send-script discipline) and one for
the human approval gate before any send. Both are operator-specific and are deliberately
not shipped with this bundle; the engineering rationale above stands without them.

---

## Sensitive-skill applicability

This pack is **NOT formally sensitive** under `sensitive-skill-guardrails.md` § 2 (no UPL exposure, no advice framing, no regulated-activity output). It is operational/engineering reference for product-organization SDR + Sales Ops adoption.

**However, it carries adjacent regulatory exposure that the consuming agents MUST surface:**

| Regulation | Source | Relevance |
|---|---|---|
| **CAN-SPAM Act** | 15 U.S.C. §7701 et seq. | Header accuracy, no deceptive subject lines, working unsubscribe, postal address, opt-out honored within 10 business days |
| **GDPR marketing consent** | GDPR Article 6(1)(a) + Recital 47 (legitimate interest narrow path) | EU recipients require explicit opt-in OR documented legitimate-interest basis with opt-out; cold B2B outbound to EU requires careful legal basis analysis |
| **UK PECR** | Privacy and Electronic Communications Regulations 2003, Regulation 22 | UK soft opt-in narrower than GDPR legitimate interest; B2B exception exists but is constrained |
| **Gmail/Yahoo sender requirements** | Feb 2024 enforcement | DMARC mandatory for bulk senders >5K/day, one-click unsubscribe RFC 8058, 0.3% spam-rate threshold (platform requirement, not regulatory, but enforced as if regulatory) |
| **Israeli Spam Law (Communications Law Amendment 40)** | 2008 | Opt-in required; B2B exception narrower than UK |

When deliverability work intersects with any of the above — particularly EU/UK recipients, large-volume sends, or any campaign where consent basis is unclear — the consuming agent MUST cross-reference `compliance-frameworks.md` and `privacy-frameworks.md` and route to `compliance-officer` (compliance) or `privacy-counsel` (GDPR/PECR) for the regulatory layer. **This pack does not opine on legal basis for marketing communications.**

---

## Operating Principle

> *Deliverability is engineering, not marketing — and the spam-flag gap is the only sender-reputation metric a regulator can subpoena, the only one a receiver weighs in reputation, and the only one that tells you the campaign is dead 14 days before the dashboard catches up.*
