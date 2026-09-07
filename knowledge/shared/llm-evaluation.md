# LLM Evaluation Knowledge Pack

**Version**: 1.0.0
**Type**: knowledge-pack (CONDITIONAL-tier — never preload)
**Authored**: 2026-06-24 (PBAW Full-Workforce Refresh, Wave 1 — Data lane net-new)
**Primary Users**: `data-lead`, `data-architect`, `ml-engineer`, `experimentation-analyst`
**Secondary Users**: `ai-architect` (consult), `bi-engineer`
**Owner**: `data-lead` (content) / `data-architect` (co-owner)

**Adapted from**:
  - DeepEval (github.com/confident-ai/deepeval, Apache-2.0) — metric taxonomy (G-Eval, DAG, RAG/agent/conversational metrics), pytest-style eval-in-CI pattern
  - RAGAS — Retrieval-Augmented Generation Assessment (github.com/explodinggradients/ragas, Apache-2.0) — faithfulness / answer-relevancy / context-precision / context-recall metric definitions
  - Braintrust autoevals (github.com/braintrustdata/autoevals, MIT) — TypeScript/JS scorer pattern; the offline-eval → scorer → CI-gate lifecycle framing (braintrust.dev)
  - Promptfoo (promptfoo.dev, MIT) — YAML/CLI eval + red-team harness. **Note: acquired by OpenAI, announced 2026-03-09 (openai.com/index/openai-to-acquire-promptfoo/). Both parties stated the core OSS project remains MIT + model-agnostic — track this as a vendor-risk assumption, re-verify each refresh cycle.**
  - Langfuse (langfuse.com, MIT core) — trace-linked / observation-level eval pattern (v4 Preview announced 2026-03-10)
**Source licence**: per-source as listed above (DeepEval Apache-2.0; RAGAS Apache-2.0; Braintrust autoevals MIT; Promptfoo MIT; Langfuse MIT core)
**V2V refinements**:
- **Discipline-level, toolchain-agnostic framing.** The existing dev-team pack toolchain-neutral implementation guidance deliberately binds eval practice to a concrete TypeScript/Vitest/CI toolchain and its own Scope note states it does NOT close the long-open OS/ET-wide `llm-evaluation.md` ticket. This pack is that OS/ET-wide home: it owns the *methodology and metric standards* a data team governs, independent of any one language or harness.
- **Eval-driven development (EDD) framed as a workflow discipline** the way A/B rigor is governed — not as CI plumbing (that register lives in the dev pack).
- **Judge-tier floor** absorbed from the dev cycle's check-tier principle and stated as a methodology rule: the judging model is never a weaker tier than the model that produced the work under test.
- **Clean boundary drawn three ways**: vs toolchain-neutral implementation guidance (implementation register — Vitest, OTel, Langfuse wiring), vs `ai-ml-patterns.md` (RAG/agent *architecture*), and vs `experimentation-ml.md` (classic-ML offline metrics + online A/B statistics — a distinct discipline, not duplicated here).
- Every vendor/benchmark specific is date-stamped and flagged **verify** — the LLM-eval tool landscape moves fast.

> **Boundary note (read first).** This pack governs the *evaluation of LLM/generative-AI outputs* as a data-science discipline. It is NOT:
> - the **implementation register** for a specific repo — that is toolchain-neutral implementation guidance (Vitest harness, the two CI gates, OTel GenAI instrumentation, per-run cost attribution, Langfuse v4 wiring).
> - **classic-ML evaluation statistics** (offline precision/recall/AUC, calibration) or **online A/B / causal-inference rigor** — that is `knowledge/shared/experimentation-ml.md`. Use that pack for model-comparison and experiment statistics; use this one for judging probabilistic *generative* output quality.
> - **RAG or agent system architecture** — that is `ai-ml-patterns.md`. This pack measures those systems; it does not design them.

---

## 1. Eval Taxonomy & the Eval-Driven-Development (EDD) Loop

### 1.1 Why LLM eval is its own discipline

A generative model's output is probabilistic and open-ended. "Did the test pass?" is not a boolean — it is a graded judgment against criteria. That is why classic test assertions (`experimentation-ml.md` covers the statistical side) are necessary but not sufficient: you also need *graded* evaluation of free-form output. LLM evaluation is the governed practice of producing that graded judgment reliably, repeatably, and cheaply enough to run continuously.

### 1.2 The three eval modes

| Mode | What it answers | Typical method | When |
|------|-----------------|----------------|------|
| **Reference-based** | "Does the output match a known-good answer?" | Exact/fuzzy match, semantic similarity, BLEU/ROUGE (legacy), embedding distance | When ground-truth answers exist (closed-form Q&A, extraction) |
| **Reference-free (criteria-based)** | "Does the output satisfy these quality criteria?" | Rubric-scored LLM-as-judge (G-Eval style), heuristic scorers | When there is no single right answer (summaries, chat, generation) |
| **Deterministic asserts** | "Is the output structurally valid / safe?" | Schema/JSON parse, regex/banned-content checks, tool-call shape | Always — cheapest layer, catches most regressions |

> **Discipline rule:** run deterministic asserts first. A schema-parse failure or a banned-content hit should never cost a judge call. Spend graded-eval budget only on what deterministic checks cannot catch.

### 1.3 The EDD loop (workflow, not plumbing)

Eval-driven development treats the eval set as the behavior contract, the same way test-driven development treats the test as the spec:

```
1. DEFINE     Write/curate eval cases for the behavior you want (before or alongside the prompt/agent).
2. BASELINE   Run the current system against the eval set → record scores. This is the contract's current state.
3. CHANGE     Modify prompt / retrieval / model / agent logic.
4. RE-EVAL    Re-run the eval set. Compare to baseline: regressions block, improvements ship.
5. GATE       A change that drops a governed score below its floor does not ship (the gate is owned, not advisory).
6. MINE       Sample production; triage failures; backfill new cases into the eval set (§2.4). The contract grows.
```

The data team owns steps 1, 2, 5, and 6 as *standards*; engineering owns the harness that runs them (the dev pack). Keep that split clean — this pack does not specify CI mechanics.

---

## 2. Building & Versioning Golden / Eval Datasets

The eval set is the most valuable and most neglected asset in LLM evaluation. A judge is only as good as the cases it scores.

### 2.1 Composition

| Slice | Purpose | Sizing guidance (verify against your variance) |
|-------|---------|------------------------------------------------|
| **Happy-path** | Core expected behavior | Majority of the set |
| **Edge cases** | Boundary inputs, rare-but-valid requests | Enough to cover known boundaries |
| **Adversarial / failure** | Inputs that previously broke the system; injection/jailbreak probes | Grows from production incidents |
| **Regression anchors** | Specific past bugs, one case each | One per fixed bug — never let a fixed bug silently return |

Start small and real (a curated set on the order of tens-to-low-hundreds of cases is a workable starting point — **verify** the floor against the score variance you observe; too few cases makes scores noisy). Grow from production, not from imagination.

### 2.2 Case structure

Each case minimally carries: an **input**, an **expected** (a reference answer OR a rubric OR a set of must/must-not assertions), **metadata** (source, date, slice, the bug/incident it anchors), and a **version**. Reference-free cases carry the rubric, not an answer.

### 2.3 Versioning as a behavior contract

- **The eval set lives in version control and is reviewed in PRs like code.** A change to an eval case is a change to the behavior contract and gets the same scrutiny.
- **Never edit a case to make a failing system pass.** That launders a regression into a "spec change." If the desired behavior genuinely changed, change the case *and* say so in the PR.
- **Pin the set version on every eval run** so a historical score is reproducible against the cases that produced it.

### 2.4 Production mining (the backfill discipline)

Production is the source of truth for what real inputs look like. Sample real runs, score them async with the same judges, triage the failures, and **backfill representative failures into the eval set**. This is what keeps the set from drifting away from reality. The mined cases are the highest-signal additions you will ever get — they are real failures, not hypothesized ones.

---

## 3. LLM-as-Judge Methodology

LLM-as-judge is the workhorse of reference-free evaluation: an LLM scores an output against criteria. Done well it scales human judgment; done badly it manufactures confident noise. The methodology is what separates the two.

### 3.1 Rubric / criteria scoring (G-Eval style)

Score against **explicit, written criteria**, not "rate this 1-10." A defensible judge prompt states the criteria, asks for chain-of-thought reasoning against each, then emits a structured score. Criteria-based scoring (the G-Eval pattern, and DeepEval's DAG/decision-tree variant for multi-step rubrics) is reproducible and auditable; vibe-scoring is neither.

### 3.2 Known judge biases (mitigate, do not ignore)

| Bias | Effect | Mitigation |
|------|--------|------------|
| **Verbosity / length bias** | Judges prefer longer, more elaborate answers | Normalize for length; reference-anchor where possible |
| **Self-preference / style bias** | A judge favors its own provider's style | Use a different provider family for the judge than the work model where feasible; spot-audit |
| **Position bias** | In pairwise comparison, order affects the verdict | Randomize/swap positions; average both orderings |
| **Leniency / score compression** | Judges cluster scores in the middle | Use discrete rubric bands with explicit anchors, not a raw 1-10 |
| **Anchoring on the reference** | Judge over-weights surface match to a reference | Score against criteria, not literal overlap |

### 3.3 The judge-tier floor (V2V methodology rule)

> **The judging model is never a weaker tier than the model that produced the output under test.** Putting the judge on the cheap tier because "judging looks easy" is the canonical mistake — a weak judge cannot reliably catch a strong model's subtle failures. This floor is the eval-side application of the dev cycle's check-tier principle (toolchain-neutral implementation guidance §1, the private implementation register).

### 3.4 Calibration — the judge is a signal, not ground truth

Periodically have humans score a sample of the same cases the judge scored, and measure judge-vs-human agreement. If agreement drifts, the judge prompt or model needs work *before* you trust its verdicts on a gate. A judge you have never calibrated against a human is an unvalidated instrument. (Verify your agreement threshold against your domain's stakes — high-stakes domains demand tighter agreement.)

---

## 4. RAG Evaluation Metrics

RAG systems fail in two separable places: retrieval (wrong/missing context) and generation (the model ignores or contradicts the context it was given). Evaluate them separately — an aggregate "answer quality" score hides which half is broken. (RAG *architecture* — chunking, hybrid search, reranking — lives in `ai-ml-patterns.md`; this section is the measurement standard.)

### 4.1 The core RAG metric set (RAGAS taxonomy)

| Metric | Measures | Failure it catches |
|--------|----------|--------------------|
| **Faithfulness / Groundedness** | Are the answer's claims supported by the retrieved context? | Hallucination — model asserts facts not in context |
| **Answer Relevancy** | Does the answer actually address the question? | On-topic-but-useless / evasive answers |
| **Context Precision** | Of the retrieved chunks, how many are relevant (and are they ranked well)? | Retriever pulls noise; reranking is broken |
| **Context Recall** | Did retrieval fetch all the context needed to answer? | The right chunk was never retrieved (the unfixable-by-prompting failure) |

### 4.2 Reading the metrics together

- **Low context recall** → a *retrieval* problem. No prompt tweak fixes a chunk that was never fetched. Invest in retrieval (hybrid search, reranking, chunking) per `ai-ml-patterns.md`.
- **High recall + low faithfulness** → a *generation* problem. The context was there; the model ignored or contradicted it. Fix the prompt, the model, or add a groundedness guardrail.
- **High faithfulness + low answer relevancy** → the model is faithfully answering the wrong question. Check query understanding / routing.

Set per-metric floors appropriate to the use case (a medical/legal knowledge assistant demands far higher faithfulness than an internal brainstorming tool). **Do not import benchmark numbers as targets** — set floors from your own baseline and stakes.

---

## 5. Agent / Trajectory Evaluation

Agents add a dimension that single-turn eval cannot capture: the **path**, not just the destination. An agent can reach a correct final answer through a broken, expensive, or unsafe trajectory — and that trajectory will eventually produce a wrong answer.

### 5.1 What to evaluate beyond the final output

| Dimension | Question | Method |
|-----------|----------|--------|
| **Task completion / goal success** | Did the agent achieve the user's actual goal? | Outcome-based judge or assertion against a success condition |
| **Tool-call correctness** | Did it call the right tools, with valid arguments, in a sensible order? | Deterministic asserts on the tool-call trace + judge on appropriateness |
| **Trajectory quality** | Was the path efficient, or did it loop / wander / retry needlessly? | Step-count / loop detection + judge on the reasoning trace |
| **Tool-selection precision/recall** | Did it use the tools it needed and avoid ones it didn't? | Compare called-tools vs expected-tools set |
| **Cost / step budget adherence** | Did it stay within a sane step and token budget? | Deterministic — cost/step is a measurable quantity (attribution lives in the dev pack) |

### 5.2 Methodology notes

- **Trace-link every eval to the span it scored** (the dev pack's OTel/Langfuse observation-level eval is the mechanism). An agent eval that cannot point at *which step* failed is hard to act on.
- **A correct final answer does not excuse a broken trajectory.** A runaway loop that happens to land on the right answer is a latent cost-and-reliability incident; score the path.
- **Multi-turn / conversational eval** scores coherence and goal-retention across turns, not just per-turn quality — track whether the agent holds context and makes progress.

### 5.3 Enterprise operating-dimension cross-check

Use CLEAR as a coverage cross-check for enterprise-agent evaluation, not as an adopted external standard or a source of universal thresholds.

| Dimension | Measure |
|---|---|
| Cost | per-run cost and step-budget adherence |
| Latency | end-to-end completion time and critical-tool latency |
| Efficacy | task success against an explicit success condition |
| Assurance | policy and tool-authorisation compliance plus deterministic safety checks |
| Reliability | repeatability and failure-recovery across representative runs |

Set evidence-based deployment thresholds by use case and stakes; do not import a universal numeric floor from this research source.

---

## 6. Tool Landscape (dated 2026-06-24 — verify before relying)

> All entries are point-in-time as of 2026-06-24. The LLM-eval tooling space moves fast (the Promptfoo acquisition below landed mid-cycle). **Re-verify license, ownership, and capability at each refresh.**

| Tool | License (verify) | Strength | Notes / register |
|------|------------------|----------|------------------|
| **DeepEval** | Apache-2.0 | Broad metric library (G-Eval, DAG, RAG, agent, conversational); pytest-style, code-first | Python-native; best when evals live in an engineering CI workflow |
| **RAGAS** | Apache-2.0 | The reference RAG metric definitions (faithfulness, relevancy, context precision/recall) | Use for the §4 metric set; pairs with other harnesses |
| **Braintrust** (+ `autoevals`) | autoevals MIT (platform commercial) | End-to-end lifecycle: dataset mgmt → scoring → CI enforcement → production monitoring; TS/JS scorers | The lifecycle-platform option; `autoevals` is the open TS scorer library |
| **Promptfoo** | MIT | YAML/CLI eval + red-team harness; 40+ attack-plugin classes; CI-native | **Acquired by OpenAI, announced 2026-03-09.** Stated to remain MIT + model-agnostic — **track as vendor-risk assumption**; pattern survives a harness swap if it changes |
| **Langfuse** | MIT core (self-host option) | Trace-linked + observation-level evals; agent-graph view | Implementation/wiring detail is in the dev pack (toolchain-neutral implementation guidance §5); here it is the trace-linking mechanism for §5 |
| **LangSmith / Arize / others** | commercial | Human-annotation workflows, regression dashboards at scale | Graduate to a commercial platform when human-annotation + regression dashboards become the bottleneck |

**Selection guidance (not an endorsement):** start with an open, code-first harness (DeepEval-class) for automated CI evals; add RAGAS metrics if the system is RAG; add a red-team harness (Promptfoo-class) for the adversarial/safety layer; graduate to a commercial lifecycle platform when human annotation and regression dashboards are the constraint. Choose by where your team's eval workflow lives (Python vs TS, code vs UI), not by metric-count marketing. **Verify** every license and ownership claim above at use time.

Sources (verify): DeepEval — github.com/confident-ai/deepeval, confident-ai.com ; RAGAS — github.com/explodinggradients/ragas ; Braintrust — braintrust.dev/articles/deepeval-alternatives-2026 ; Promptfoo acquisition — openai.com/index/openai-to-acquire-promptfoo/ (announced 2026-03-09) ; Langfuse v4 — langfuse.com/changelog/2026-03-10-simplify-for-scale ; LLM-as-judge methodology survey — deepeval.com/guides/guides-llm-as-a-judge.

---

## 7. Cross-References & Boundaries

| Pack | Relationship | Use it for (not this pack) |
|------|--------------|----------------------------|
| toolchain-neutral implementation guidance | **Implementation register** of this discipline | The concrete harness: Vitest three-layer model, the two CI gates, OTel GenAI instrumentation + attribute pinning, per-run cost attribution, Langfuse v4 wiring. This pack is the methodology; that pack is the wiring. |
| `knowledge/shared/ai-ml-patterns.md` | **System architecture** being measured | RAG tiers, agent orchestration patterns, embedding/retrieval design, prompt engineering. This pack evaluates those systems; it does not design them. (See that pack's 2026-06 Currency Addendum.) |
| `knowledge/shared/experimentation-ml.md` | **Distinct discipline** — classic-ML + online statistics | Offline ML metrics (precision/recall/AUC, calibration), A/B test design, power analysis, causal inference. Use it for model-comparison and online-impact rigor; use *this* pack for graded generative-output quality. |
| `knowledge/shared/analytics-methodology.md` | Sibling methodology pack | Metric trees, North Star, cohort/funnel analysis, data quality. Eval scores are metrics too — govern them with the same discipline. |
| `knowledge/shared/data-visualization-bi.md` | Downstream consumer | Surfacing eval scores / drift on dashboards (a governed metric like any other). |

> Operating rule: **evaluate generative output as a governed discipline, not an afterthought.** Deterministic checks first, graded eval where they can't reach; the eval set is a versioned behavior contract; the judge is a calibrated instrument, never ground truth; and the path matters as much as the answer for agents.
