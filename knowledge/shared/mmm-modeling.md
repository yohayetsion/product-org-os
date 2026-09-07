---
pack: mmm-modeling
consumers:
- paid-media-manager
- marketing-dir
- growth-marketer
- cmo
---
# Marketing Mix Modeling (MMM) — V2V Knowledge Pack

**Adapted from**:
  - Google Meridian (Apache-2.0, github.com/google/meridian)
  - Meta Robyn (MIT, github.com/facebookexperimental/Robyn)

**Source licence**: Apache-2.0 (Meridian) + MIT (Robyn)

**V2V refinements**:
- Translated Meridian + Robyn methodology into product-organization marketing-org adoption guidance (not a data-science manual)
- Added cookie-free measurement framing — why MMM matters MORE in 2026 than 2024
- Added V2V Phase 5 (Outcomes) decision-interface integration — how MMM outputs feed marketing-mix decisions, who acts on them, at what cadence
- Added anti-patterns specific to product orgs adopting MMM (MMM-as-MTA-substitute, naive saturation curves, missing geo-experiment validation, refresh cadence too slow for ad-mix volatility)

---

## Why MMM Matters in 2026

Multi-touch attribution (MTA) is collapsing. Chrome's third-party cookie sunset trajectory remains staged through 2026, iOS App Tracking Transparency has already broken cross-app attribution for years, and the EU ePrivacy Directive plus consent-gating mean a growing share of user-level data simply isn't observable to advertisers. The measurement stack that worked in 2022 — pixel firing, click-attributed conversions, last-touch rollups in the ad platform — is structurally degrading.

Marketing Mix Modeling is the cookie-free measurement layer. It works on aggregate spend, impressions, and conversions; no user identifiers, no pixel, no consent dependency. It was always the canonical channel-mix tool — what changed is that, until recently, running an MMM was a six-figure consulting engagement: Nielsen, Analytic Partners, Marketing Evolution, four-to-six month projects, quarterly refreshes by a vendor. In 2024-2025, Google open-sourced Meridian (Apache-2.0) and Meta released Robyn (MIT). The same modeling — Bayesian hierarchical regression, adstock, saturation curves, geo-level estimation — collapsed into Python and R libraries a single operator can run on a laptop or a GPU node. The economic moat that protected the MMM consulting market is gone, and the product-organization marketing function can now own measurement that used to be outsourced.

That's the 2026 shift: not that MMM exists, but that it became operator-level technology at the exact moment cookie-based MTA became unreliable.

---

## The Two OSS Frameworks

### Google Meridian

Bayesian causal-inference framework, Python (3.11-3.13), GPU-accelerated via JAX. Geo-level hierarchical modeling — fits a model per geography and pools information across them, which is statistically stronger than national-level estimation. Native reach-and-frequency modeling for video and YouTube. Built-in geo-experiment integration for calibration. Privacy-safe by design: no user-level data, no cookies.

When it fits: medium-to-large advertisers running multi-geo campaigns, video-heavy mix, teams with a Python-comfortable analyst, organizations that want their MMM stack to be the durable measurement spine post-cookie.

### Meta Robyn

R-based, MIT-licensed, automated EDA, hyperparameter search via Nevergrad (Facebook's evolutionary optimizer). Produces multiple model candidates and Pareto-fronts them on fit-vs-business-plausibility. Lower barrier to entry than Meridian if the team already runs R; faster iteration on small-to-medium datasets.

When it fits: SMB or single-brand advertisers, R-native analytics teams, organizations that want to compare many candidate models and let business plausibility break ties.

### Choosing Between Them

| Criterion | Lean Meridian | Lean Robyn |
|---|---|---|
| Team language | Python | R |
| Data size | Large, multi-geo | Small-to-medium, often national |
| Channel mix | Video + reach/frequency-heavy | Performance-heavy, fewer channels |
| GPU available | Yes | N/A |
| Maturity | New (2024-2025), Google-backed | Established (2020+), Meta-backed |
| Bayesian comfort | High (it's the model) | Optional |

**The 2026 default for new MMM adoptions is Meridian.** Google-backed, Apache-2.0, modern toolchain, geo-experiment integration baked in, active development. Robyn remains excellent for R-native teams and remains the right choice in many shops, but a product organization standing up MMM from scratch in 2026 with no prior tooling commitment should evaluate Meridian first. Most orgs need one, not both.

---

## MMM Modeling Building Blocks

### Saturation Curves

Media response is non-linear. The first dollar of search spend buys a different conversion than the millionth. Saturation curves model diminishing returns — typically Hill curves (S-shape, with a flexible knee) in Meridian, parameterized Hill curves in Robyn. Without saturation, the model thinks doubling Facebook spend doubles Facebook conversions, which is wrong above some channel-specific threshold.

### Adstock

Media impressions today drive conversions over multiple days. Adstock models this carry-over with a decay parameter — geometric decay (simple, one parameter) or Weibull (more flexible, two parameters). Without adstock, the model attributes all credit to the day of impression, missing brand-building lift.

### Geo-Experiment Validation

MMM is regression. Regression on observational data is correlation, not causation. The way you get causal force out of an MMM is geo-experiment validation: turn spend up or down in a treatment geography, hold a comparable control geography flat, observe the differential conversion lift, and check whether the MMM's coefficient for that channel and geography matches the experiment's measured lift. Meridian integrates this natively. Robyn supports it. **An MMM without geo-experiment calibration is just a fitted curve**, and treating its channel coefficients as actionable spend-shift recommendations is a category error.

### Calibration with Holdout

In-sample fit is meaningless. The model can over-fit historical spend patterns and produce a beautiful R² that breaks the moment spend allocation changes. Two validation moves matter: (1) time-series holdout — train on weeks 1-40, validate on weeks 41-52, check MAPE; (2) forward-looking validation — make a recommendation, deploy a budget shift, measure actual lift against predicted, iterate. A backtest alone is not enough; the model has to survive forward-looking deployment.

---

## V2V Phase 5 (Outcomes) Integration

MMM is a Phase 5 instrument. It belongs to the Outcomes phase because its job is to measure whether the marketing portfolio is producing the lift the strategy promised — and to feed mix-decision interfaces with grounded, cookie-free signal.

**Refresh cadence**: quarterly model refresh (re-fit on the trailing 18-24 months of data) plus monthly score (run the existing model against the latest month's actuals, produce updated channel coefficients and recommended mix). Annual refresh is too slow for ad-mix volatility; weekly refresh produces overfit noise.

**Decision interface**: MMM outputs feed the marketing-mix decision in two shapes — (1) channel ROI curve for budget reallocation (which channel saturates first, where the next dollar earns the most), and (2) incremental-lift estimates for spend-on/spend-off decisions (kill, hold, scale). Both shapes go to the CMO and Paid Media Manager as inputs, not as autonomous executors. The model recommends; the human owns the decision.

**Who acts**: Paid Media Manager owns operational mix-shifts within an approved budget envelope. CMO owns budget-envelope decisions and channel-portfolio changes. Growth Marketer owns the geo-experiment design that calibrates the model. Data Lead or analytics partner owns the model itself — the fit, the refresh, the diagnostics. The marketing function consumes MMM; it does not author it alone.

---

## Implementation Guidance

**First-quarter adoption** (read-only deliverable): Stand up Meridian or Robyn against the trailing 18 months of spend + conversion data. Goal is a fitted model with channel coefficients, saturation curves, and adstock estimates — and a documented diagnostic report (in-sample fit, channel-by-channel plausibility check, list of geo-experiments needed for calibration). Do NOT act on the recommendations yet. The first model is a learning artifact.

**Ongoing operation** (decision-input): Once the model has survived one geo-experiment calibration cycle, MMM outputs become an input to monthly mix reviews. Paired with platform-side incrementality tests (Meta/Google holdout-based lift studies), MMM becomes the channel-mix backbone for the quarter. Refresh quarterly, score monthly.

**MMM-mature org** (multi-model ensemble): Run MMM + platform incrementality + server-side first-party tracking (Stape or equivalent) as a three-layer measurement stack. Triangulate. Where MMM and platform incrementality agree, confidence is high. Where they disagree, dig — usually it's a saturation curve issue, an adstock mis-specification, or a geo-experiment that hasn't been run yet.

---

## Anti-Patterns / Common Failures

**MMM-as-MTA-substitute**: Treating MMM channel coefficients as user-level attribution. They're not. MMM answers "what did the marketing mix produce in aggregate" — MTA answered "which touch gets credit for this user's conversion." These are different measurement questions. MMM does not replace MTA; it replaces *the question MTA was trying and failing to answer at the aggregate level*.

**Naive saturation curves**: Shipping a model with default saturation parameters, no business plausibility check, no holdout validation. The model fits; the recommendations are unsafe. Always Pareto-front candidate models on fit + business plausibility (Robyn does this natively; Meridian via posterior diagnostics).

**Missing geo-experiment validation**: Acting on MMM channel coefficients with no experimental calibration. The model has not been told what causal lift looks like. Its recommendations are correlation surfaces, not causal levers. At minimum, run one geo-experiment per major channel per year and re-calibrate.

**Refresh cadence too slow**: Annual refresh in a channel-mix environment that shifts quarterly. The model becomes stale; the recommendations chase historical patterns that no longer hold (e.g., the model still recommending the channel mix from before iOS ATT broke Facebook attribution). Quarterly refresh is the floor; monthly score is the rhythm.

**Single-source data without triangulation**: MMM alone, no platform incrementality, no first-party server-side tracking. Three-layer measurement is the 2026 standard. MMM provides the cookie-free aggregate signal; incrementality provides the channel-specific causal estimate; server-side provides the conversion fidelity. Each covers the others' weaknesses.

---

## V2V Cross-References

**Sibling Q2-6 packs**:
- **`retention-marketing.md` (Q2-6.2)** — downstream consumer of mix decisions. Retention spend is part of the mix MMM evaluates; the per-seat structural-failure framing in that pack interacts with how MMM coefficients should be interpreted when seat-count declines are decoupled from value extracted (channel coefficients should weight value-retention signal, not seat-retention signal).
- **`llm-seo.md` (Q2-6.3)** — channel-mix overlap. AI-citation rate joins paid-channel mix as a measurable surface; the 2026 GEO vs traditional SEO investment decision (per §"GEO vs. Traditional SEO" in that pack) consumes MMM-style channel ROI curves alongside organic-traffic measurement.

**Sibling Q2-7 packs (sales-funnel measurement adjacency)**:
- **`deliverability-engineering.md` (Q2-7.1)** — outbound SDR motion as a measurable channel that MMM may incorporate at the aggregate level; deliverability health (5pp spam-flag gap) bounds the legitimate sending volume MMM can attribute conversions to.

**Existing packs**:
- `paid-media.md` — channel selection + budget allocation frameworks; MMM is the measurement layer for paid-media mix decisions.
- `analytics-methodology.md` — broader measurement stack (MMM + platform incrementality + server-side first-party) operates within that pack's methodology.
- `experimentation-ml.md` — geo-experiment + holdout design that MMM calibration depends on.
- `growth-frameworks.md` — growth-loop framing; MMM informs paid-acquisition leg of the loops.
- `metrics-frameworks.md` §9 — Per-Seat-Pricing Structural Failure framing that reframes "channel ROI" when value extracted decouples from seat count.
- `pricing-frameworks.md` — pricing-side framing of the per-seat collapse that retention-marketing and MMM both need to honor.

**Sensitive-skill applicability**: NOT sensitive. Technical reference pack; no legal, HR, compliance, or regulatory output.

---

## Sensitive-Skill Applicability

NOT sensitive. Technical reference pack. No legal, HR, compliance, or regulatory output. No FCRA / Title VII / UPL exposure. No required disclaimer block per `sensitive-skill-guardrails.md`.

---

## Operating Principle

> *MMM is the measurement layer cookie-deprecation actually leaves intact — but only if you wire geo-experiment validation in from day one. A fitted curve without causal calibration is a confident wrong answer.*
