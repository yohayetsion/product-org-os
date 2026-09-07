# Experimentation & ML Knowledge Pack

**Version**: 1.0
**Type**: knowledge-pack
**Primary Users**: `experimentation-analyst`, `ml-engineer`
**Secondary Users**: `data-lead`, `data-analyst`, `growth-marketer`

<!-- Attribution:
  Frameworks and patterns in this knowledge pack were informed by:
  - GrowthBook (github.com/growthbook/growthbook, MIT) — experiment design, sequential testing, Bayesian analysis patterns
  - mlflow/mlflow (github.com/mlflow/mlflow, Apache-2.0) — ML experiment tracking, model registry, MLOps lifecycle
  - Evidence (github.com/evidence-dev/evidence, MIT) — analytics reporting patterns
  - Kohavi, Tang, Xu — "Trustworthy Online Controlled Experiments" (public framework summaries)
  - Google "Rules of ML" (public resource) — ML engineering best practices
  2026-06 delta sources:
  - Digital Applied "AI Agent Eval Frameworks Testing Guide 2026" — digitalapplied.com/blog/ai-agent-eval-frameworks-testing-guide-2026 (LLM/agent eval landscape; commercial + OSS tiers; observability/eval gap)
  - OpenAI "OpenAI to acquire Promptfoo" — openai.com/index/openai-to-acquire-promptfoo/ (Promptfoo acquisition, 2026-03-09)
  - Inspect AI — UK AI Security Institute OSS eval framework
  Adapted and expanded for Product Org OS agents.
-->

---

## A/B Testing — Frequentist Approach

### Hypothesis Testing Framework

```
H₀ (Null Hypothesis): Treatment has no effect on the primary metric
H₁ (Alternative Hypothesis): Treatment has an effect on the primary metric

α (Significance Level): Probability of false positive (typically 0.05)
β (Type II Error Rate): Probability of false negative (typically 0.20)
Power (1 - β): Probability of detecting a real effect (typically 0.80)
```

### Test Selection Guide

| Data Type | Groups | Test | Assumptions |
|-----------|--------|------|-------------|
| **Continuous** (mean) | 2 | Two-sample t-test | Normal distribution or large sample |
| **Continuous** (mean) | 2+ | ANOVA + post-hoc | Normal, equal variance |
| **Proportions** | 2 | Chi-squared or Z-test for proportions | n×p ≥ 5, n×(1-p) ≥ 5 |
| **Proportions** | 2+ | Chi-squared test | Expected cell count ≥ 5 |
| **Revenue/skewed** | 2 | Mann-Whitney U or bootstrapped t-test | Non-parametric for skewed data |
| **Time-to-event** | 2 | Log-rank test | Censoring is independent |
| **Count data** | 2 | Poisson regression or negative binomial | Variance ~ mean (Poisson) or overdispersed |

### Power Analysis

```
Required Inputs:
1. Baseline conversion rate (or mean/variance)
2. Minimum Detectable Effect (MDE) — smallest effect worth detecting
3. Significance level (α) — typically 0.05
4. Power (1 - β) — typically 0.80

Output:
→ Required sample size per group
→ Required experiment duration (given daily traffic)
```

### MDE Selection Guidelines

| Metric Type | Typical MDE | Reasoning |
|-------------|-------------|-----------|
| **Conversion rate** (5-10%) | 5-10% relative lift | Smaller effects rarely justify the feature's complexity |
| **Revenue per user** | 2-5% relative lift | Revenue impact compounds, smaller MDE worthwhile |
| **Retention** | 1-3 pp absolute | Retention is high-leverage; even small lifts are valuable |
| **Engagement** (time, actions) | 5-15% relative lift | Engagement metrics are noisy; need larger effects |

### Common Mistakes in Frequentist Testing

| Mistake | Impact | Correct Approach |
|---------|--------|-----------------|
| **Peeking at results** | Inflates false positive rate to 20-30% | Use sequential testing or fixed-horizon |
| **Multiple comparisons** | Finding significance by chance | Bonferroni or Holm-Bonferroni correction |
| **Wrong unit of analysis** | Clustered data violates independence | Cluster-randomized design, clustered standard errors |
| **Ignoring novelty effect** | Short-term lift fades | Run experiments long enough (2+ weeks minimum) |
| **Survivorship bias** | Only analyzing users who stayed | Intent-to-treat analysis |

---

## A/B Testing — Bayesian Approach

### Bayesian Framework

```
Prior: What we believe before seeing data
Likelihood: What the data tells us
Posterior: Updated belief after seeing data

Posterior ∝ Prior × Likelihood

Decision: Based on posterior probability of one variant being better
```

### Bayesian vs. Frequentist Decision Guide

| Criterion | Bayesian | Frequentist |
|-----------|----------|-------------|
| **Interpretation** | "95% probability B is better than A" | "If A=B, 5% chance of seeing this difference" |
| **Early stopping** | Natural — posterior updates continuously | Requires pre-specified sequential testing |
| **Prior knowledge** | Explicitly incorporated | Not incorporated (but sample size implicitly does) |
| **Multiple comparisons** | Handled through hierarchical models | Requires explicit correction |
| **Best for** | Continuous monitoring, many variants, prior data available | Fixed-horizon, regulatory/compliance contexts |

### Bayesian Decision Rules

| Rule | When to Use |
|------|-------------|
| **Probability of being best > 95%** | Standard threshold for shipping |
| **Expected loss < threshold** | When you care about the magnitude, not just direction |
| **Value remaining < threshold** | When the expected gain from continuing is small |
| **Credible interval excludes 0** | Equivalent to significance in Bayesian terms |

---

## Experiment Design Patterns

### Pre-Registration Template

```markdown
## Experiment Design Document

**Name**: [Experiment name]
**Hypothesis**: [Clear, testable hypothesis]
**Owner**: [Decision owner]

### Design
- **Primary metric**: [One metric, clearly defined]
- **Secondary metrics**: [Supporting metrics, clearly labeled as secondary]
- **Guardrail metrics**: [Metrics that must NOT degrade]
- **Randomization unit**: [User / Session / Device / Account]
- **Allocation**: [50/50 or other split, with justification]
- **Targeting**: [All users / Segment / New users only]

### Power Analysis
- **Baseline**: [Current value of primary metric]
- **MDE**: [Minimum detectable effect, with justification]
- **Alpha**: [Significance level, typically 0.05]
- **Power**: [Typically 0.80]
- **Required sample size**: [Per group]
- **Expected duration**: [Days, based on traffic]

### Analysis Plan
- **Statistical test**: [Specified upfront]
- **Segmentation**: [Pre-specified subgroup analyses]
- **Stopping criteria**: [Fixed horizon or sequential testing rules]

### Decision Criteria
- **Ship if**: [Primary metric significant, guardrails hold]
- **Iterate if**: [Partial signal, specific learnings to apply]
- **Kill if**: [No signal or guardrail violation]
```

### Experiment Anti-Patterns

| Anti-Pattern | Description | Impact |
|--------------|-------------|--------|
| **HiPPO** | Highest-Paid Person's Opinion overrides data | Undermines experimentation culture |
| **Twyman's Law** | Surprising results are usually wrong (instrumentation error) | Always validate surprising results before celebrating |
| **Peeking** | Checking results daily, shipping when favorable | Massively inflated false positive rate |
| **Underpowered** | Running tests on tiny traffic with small MDE | Wasted time, inconclusive results |
| **Feature flag leak** | Treatment visible to control via shared resources | Contaminated results, biased estimates |
| **Novelty/primacy** | Short-term behavior change that fades | Run for at least 2 weeks, monitor for effect decay |

---

## Sequential Testing

### When to Use

Sequential testing allows valid early stopping — checking results at multiple points without inflating the false positive rate.

### Methods

| Method | Approach | Best For |
|--------|----------|----------|
| **Group Sequential** | Pre-specified look times with adjusted alpha spending | Fixed number of looks (3-5) |
| **Always Valid** | Confidence sequences that are valid at any time | Continuous monitoring |
| **mSPRT** | Mixture sequential probability ratio test | Bayesian-flavored sequential testing |

### Alpha Spending Functions

```
O'Brien-Fleming: Conservative early, generous late
                 α at 50%: 0.003  α at 100%: 0.048

Pocock: Equal alpha at each look
        α at 50%: 0.029  α at 100%: 0.029

Spending function choice impacts:
  - How aggressively you can stop early
  - Power at the final analysis
  - Total expected sample size
```

---

## Causal Inference (Non-Experimental)

### When Randomization Is Impossible

| Method | Assumption | Use Case |
|--------|-----------|----------|
| **Difference-in-Differences (DiD)** | Parallel trends in absence of treatment | Policy changes, feature rollouts by region |
| **Regression Discontinuity (RDD)** | Assignment based on a threshold | Eligibility cutoffs, score-based targeting |
| **Instrumental Variables (IV)** | Valid instrument exists | When treatment is endogenous |
| **Propensity Score Matching** | No unmeasured confounders | Observational treatment-control comparison |
| **Synthetic Control** | Pre-treatment fit predicts post-treatment counterfactual | Single treated unit, aggregate outcome |
| **Interrupted Time Series** | Stable pre-treatment trend | Sudden interventions with time series data |

### Causal Inference Validity Checks

| Threat | Description | Mitigation |
|--------|-------------|------------|
| **Selection bias** | Treatment and control differ systematically | Matching, weighting, or natural experiment |
| **Confounding** | Third variable drives both treatment and outcome | Control for confounders, use IV |
| **Reverse causation** | Outcome causes treatment, not vice versa | Temporal ordering, experimental design |
| **Measurement error** | Noisy variables attenuate estimates | Better instrumentation, IV |
| **External validity** | Results don't generalize | Replicate across contexts |

---

## ML Lifecycle (MLflow Patterns)

### ML Project Phases

| Phase | Activities | Key Artifacts |
|-------|-----------|---------------|
| **Problem Framing** | Define business problem, success criteria, baseline | Problem statement, evaluation plan |
| **Data Preparation** | Collect, clean, split, feature engineer | Feature store, train/test/validation sets |
| **Experimentation** | Train models, tune hyperparameters, evaluate | Experiment runs, metrics, artifacts |
| **Validation** | Offline evaluation, fairness check, edge cases | Model card, evaluation report |
| **Deployment** | Serve predictions, set up monitoring | Model endpoint, monitoring dashboard |
| **Monitoring** | Track drift, performance degradation, retraining | Alerts, retraining triggers |

### Model Registry Pattern

```
Model Stages:
  None → Staging → Production → Archived

Stage Transitions:
  None → Staging: Model meets offline evaluation criteria
  Staging → Production: Model passes A/B test or shadow mode validation
  Production → Archived: Replaced by better model or deprecated

Registry Metadata:
  - Model name and version
  - Training dataset version
  - Hyperparameters
  - Evaluation metrics
  - Author and date
  - Approval chain
```

### Feature Store Patterns

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Point-in-time correctness** | Features computed as of prediction time, not current time | Prevents data leakage in training |
| **Offline/Online consistency** | Same feature logic for training (batch) and serving (real-time) | Prevents train-serve skew |
| **Feature versioning** | Track changes to feature definitions over time | Reproducibility, debugging |
| **Feature sharing** | Reuse features across models | Reduces duplicated computation |
| **Feature monitoring** | Track feature distributions for drift | Early warning of model degradation |

### Model Evaluation Checklist

```
Offline Evaluation:
  - [ ] Performance metrics (accuracy, precision, recall, F1, AUC)
  - [ ] Performance by segment (geography, plan type, user cohort)
  - [ ] Calibration (predicted probabilities match observed rates)
  - [ ] Feature importance (top drivers interpretable and logical)
  - [ ] Edge case analysis (extreme values, missing data)
  - [ ] Fairness assessment (no discriminatory bias by protected attributes)
  - [ ] Comparison to baseline (does it beat the simple approach?)

Online Evaluation:
  - [ ] Shadow mode (predictions logged but not acted upon)
  - [ ] A/B test (model predictions vs. status quo)
  - [ ] Business impact measurement (not just model accuracy)
  - [ ] Latency and throughput acceptable for serving pattern
```

---

## Model Monitoring

### What to Monitor

| Signal | Description | Action |
|--------|-------------|--------|
| **Data drift** | Input feature distributions change | Alert, investigate root cause, potentially retrain |
| **Prediction drift** | Output distribution changes | Alert, compare with data drift, check model validity |
| **Performance drift** | Model accuracy degrades on new data | Retrain with recent data, review feature relevance |
| **Feature freshness** | Input features are stale or missing | Alert, investigate pipeline, check fallback logic |
| **Latency** | Prediction serving slows down | Optimize model, scale infrastructure |

### Retraining Strategy

| Strategy | Trigger | Best For |
|----------|---------|----------|
| **Calendar-based** | Monthly, quarterly | Stable domains with slow drift |
| **Performance-based** | Accuracy drops below threshold | When ground truth is available with low latency |
| **Drift-based** | Data drift exceeds threshold | When ground truth is delayed |
| **Continuous** | Every new batch of data | High-frequency domains (recommendations, fraud) |

---

## 2026-06 Delta Update — LLM/Agent Eval Landscape (as of 2026-06-06)

This pack historically covered classical experimentation (frequentist/Bayesian A/B) and ML lifecycle (MLflow). The LLM/agent **eval** category is now a distinct, consolidating tooling space and is added here as net-new coverage.

**Confidence note**: Medium on exact version numbers (drawn from secondary sources). Versions are phrased loosely ("~v4", "v0.3.x") and should not be over-asserted.

### Eval tooling consolidation

The eval category is settling into roughly **~5 commercial platforms + 3 OSS standards**:

| Layer | Tools |
|-------|-------|
| **Commercial platforms** | LangSmith, Braintrust, Helicone, Arize Phoenix, Promptfoo |
| **OSS standards** | OpenAI Evals; DeepEval (~v4); **Inspect AI (~v0.3.x), from the UK AI Security Institute** |

- **Inspect AI** is a credible **government-backed OSS eval standard** (UK AI Security Institute) and is the notable addition to track — it gives the OSS tier an institutionally-backed option alongside OpenAI Evals and DeepEval.
- **Promptfoo → OpenAI acquisition** (announced 2026-03-09): Promptfoo remains open-source but is now an OpenAI Frontier asset. This affects any "Promptfoo is neutral OSS" guidance — it is still OSS, but is no longer vendor-neutral in ownership. Weigh that when recommending it as a provider-agnostic harness.

### Observability vs. evals gap (still current)

The May 2026 thesis holds: roughly **89% of teams have LLM observability instrumented but only ~52% run structured evals** — i.e., most teams can see what their LLM/agent did but do not systematically grade whether it was correct. Closing the observability→eval gap remains the higher-leverage investment for teams already logging traces.

Sources: https://www.digitalapplied.com/blog/ai-agent-eval-frameworks-testing-guide-2026 ; https://openai.com/index/openai-to-acquire-promptfoo/

---

## Google "Rules of ML" (Key Principles)

1. **Don't be afraid to launch a product without ML** — Start with heuristics
2. **First, design and implement metrics** — Instrument before modeling
3. **Choose ML over complex heuristics** — But only when heuristics fail
4. **Keep the first model simple** — Get the pipeline right first
5. **Test the infrastructure independently from ML** — Serving bugs != model bugs
6. **Be careful about dropped data** — Missing data is often informative
7. **Turn heuristics into features** — Domain rules make great features
8. **Know the freshness requirements** — How stale can data be?
9. **Don't over-engineer for scale you don't have** — Start simple, iterate
10. **Monitor everything** — If you don't measure it, it will break silently

---

*Last Updated: 2026-06-06 (2026-06 delta: LLM/agent eval landscape)*
*References: GrowthBook, mlflow/mlflow, Evidence, Kohavi/Tang/Xu "Trustworthy Online Controlled Experiments", Google "Rules of ML"; 2026-06 delta: Digital Applied eval-frameworks guide, OpenAI/Promptfoo acquisition, Inspect AI (UK AISI)*
