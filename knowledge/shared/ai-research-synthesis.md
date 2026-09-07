---
pack: ai-research-synthesis
consumers:
- user-researcher
- interaction-designer
- product-manager
---
# AI Research Synthesis (V2V Knowledge Pack)

**Version**: 1.0.0
**Owner**: user-researcher (primary) + design-dir (secondary co-owner for research-ops policy)
**Last updated**: 2026-05-18 (Q2-8 Wave 1)
**Consumers**: `user-researcher`, `product-manager`, `product-marketing-manager`, `value-realization`, `competitive-intelligence`, `/interview-synthesis`, `/feedback-capture`, `/customer-health-scorecard`
**Sensitive**: false (NOT formally sensitive; carries privacy obligations when research includes PII — see §8)

---

**Adapted from**:
- Dovetail AI (publicly documented qualitative research platform AI features 2026)
- Reduct AI (publicly documented transcript analysis 2026)
- Industry qualitative-coding patterns (publicly discussed 2025-2026)

**Source licence**: per-source-terms (commercial research platforms; documented patterns; no statute reproduction)

**V2V refinements**:
- Translated AI research synthesis tooling patterns to product-organization User Research adoption (not consultancy practice)
- Named the **voice-flattening risk** as the load-bearing concern for 2026 product-org adoption — not speed, not cost
- Codified **human-in-loop research synthesis** as the 2026 default (NOT autonomous AI synthesis), with explicit handoff points between AI mechanics and human interpretation
- Anti-patterns specific to product orgs (AI summary as substitute for verbatim; theme-clustering without ground-truth check; transcription accuracy assumed not verified; auto-generated personas; synthesis-as-decoration)
- Phase model integration: AI research synthesis maps to V2V Phase 1 (Intent — discovery interviews, opportunity work) and Phase 5 (Outcomes — NPS verbatim, support tickets, customer health interviews)

---

## 1. What AI Research Synthesis Is

The 2026 inflection: qualitative research synthesis is now AI-assisted by default. Auto-transcription, theme tagging, sentiment classification, summarization, cross-corpus search across interviews, NPS verbatim, support tickets, and sales-call recordings ship out-of-the-box. A 60-minute interview that took 90-120 minutes to transcribe, code, and synthesize five years ago is now machine-handled end-to-end in under five minutes.

The time savings are real. The voice-flattening risk is also real. This pack is about adopting the speed without losing the signal. It covers: (1) the tooling landscape; (2) the structural risk that AI summarization flattens user voice; (3) the human-in-loop pattern that captures the speed without ceding interpretation to the machine.

---

## 2. The Tooling Landscape

Three patterns dominate the 2026 market.

### Dovetail AI — Hub-and-Tag

Research repository at the center; AI auto-tags interview clips, theme-clusters across studies, surfaces semantic search across the corpus. Integrates the full research-ops workflow (recruiting, scheduling, recording, transcribing, tagging, sharing).

- **Strengths**: Single integrated workflow. Auto-tagging gets corpus-aware over time. Theme clustering works across studies — where the value compounds. Stakeholder repository access surfaces findings outside the researcher's head.
- **Risks**: Tag quality IS summarization quality. If AI tags collapse "this is the only thing keeping my team from drowning" into `feature_helpful`, the urgency is gone from the repository forever. Hub model encourages stakeholders to skim tags without reading verbatim. Tags become the artifact; voice gets buried.

### Reduct AI — Transcript-First

The transcript is the artifact; AI operates on the transcript with citation back to the source video moment. AI summarization always cites the underlying transcript span.

- **Strengths**: Source-traceable by design. Verbatim is one click away from any summary. Strong for teams sharing research highlights externally (sales enablement, exec briefings) — citations stay intact.
- **Risks**: Transcript accuracy errors compound. Diarization mistakes, acronym mishearing, accent-dependent error rates can corrupt the foundation before synthesis starts. Less workflow integration than Dovetail.

### Notebook / Self-Built AI Pipelines

Custom AI synthesis using OpenAI / Anthropic APIs against transcripts in a notebook (Notion, Obsidian, Drive, research-ops DB). Researcher writes prompts; the LLM synthesizes.

- **Strengths**: Prompt flexibility (e.g., "summarize quotes that contradict the product hypothesis" — not an out-of-the-box question on commercial platforms). No platform licensing. Full researcher control.
- **Risks**: Reproducibility (different prompts → different syntheses → no audit trail). Governance burden — PII exposure to LLM APIs, retention, model versioning, consent compliance all become the researcher's problem. Quality depends entirely on prompt discipline, which doesn't scale.

### Tooling posture for product orgs

For serious continuous discovery, Dovetail or Reduct beat self-built. Dovetail wins when research-ops workflow is the bottleneck; Reduct wins when voice-preservation and source-traceability are load-bearing (exec briefings, regulated-domain research). Self-built is appropriate for one-researcher teams, exploratory R&D, or non-interview corpora.

---

## 3. The Voice-Flattening Risk (Load-Bearing)

This is the section that distinguishes a serious 2026 research practice from a fast one.

AI summarization optimizes for "summary quality" as judged by general-purpose readability — coherent paragraphs, generalizable themes, clean structure. That optimization function privileges **generic themes over specific verbatim**. The customer who said "this is the only thing keeping my team from drowning" reads as `users find the feature helpful` after AI summary. The customer who said "I would pay double if you fixed this one bug" reads as `bug fix requested`.

The verbatim is the texture. The texture is what makes user research actionable. A theme tag tells you what to count; a verbatim tells you what to do. When the verbatim doesn't survive synthesis, the team has shipped the speed and lost the signal.

This is the load-bearing concern for product-org adoption in 2026 — not whether AI synthesis is fast (it is), not whether it's accurate enough (it usually is on tagging mechanics), but whether it preserves the texture that lets the team know which user, in which context, under which pressure, said which exact thing. The texture is irreducible to themes. AI synthesis pulls toward themes. Discipline pushes back toward verbatim.

The mitigation is structural, not exhortatory. See §4.

---

## 4. Human-in-Loop Research Synthesis Pattern (2026 default)

AI does first-pass mechanics; human researcher owns interpretation.

**AI does**: transcription, speaker diarization, first-pass theme tagging, cross-corpus search and clustering, sentiment classification (treated as signal, not truth), draft summary as a starting point.

**Human researcher does**:
- Reviews AI tag assignments against transcript reality (full pass for any study informing a P0 decision, not just spot-checks)
- Reads underlying verbatim before accepting any theme
- Writes synthesis with **verbatim citations preserved** — rule of thumb: at least one direct quote per theme, exact wording, attributed to participant + context
- Owns interpretation: what this means for the product, which decisions it informs, which it doesn't
- Removes (not softens) AI-summarized themes the verbatim doesn't actually support
- Flags transcription errors discovered along the way (compound-error prevention)

**Handoff discipline**: The researcher does NOT publish, share, or cite synthesis output that has not passed the verbatim-read step. AI synthesis is a draft. Always.

**Sample-size discipline**: AI synthesis tempts teams to scale up sample size beyond previously feasible (10 → 50 interviews; 200 support tickets). Scale deliberately as a separate design decision, not a free side-effect of AI speed. More data with thinner interpretation is worse than less data with thicker interpretation.

---

## 5. V2V Phase Integration

### Phase 1 (Intent) — Discovery + Opportunity Work

AI research synthesis applies to discovery interviews, opportunity-tree work, jobs-to-be-done research, and competitive customer research. Output feeds `/opportunity-tree`, `/customer-journey-map`, `/jtbd`, `/interview-synthesis`. Verbatim preservation is highest-stakes here — Phase 1 is where the product decides what to build, and a flattened summary at this stage propagates into committed bets.

### Phase 5 (Outcomes) — Customer Health, NPS, Support, Adoption

AI research synthesis applies to NPS verbatim analysis, support ticket clustering, customer health interviews, churn-reason analysis, and feature-adoption interviews. Output feeds `/customer-health-scorecard`, `/value-realization-report`, `/outcome-review`, `/feedback-capture`. Voice preservation is critical for churn reasons — the customer who told you why they left in specific words is the most actionable signal in the entire research corpus.

### Other phases

AI research synthesis has secondary applicability to Phase 2 (Decisions — decision-record context), Phase 3 (Commitments — pre-commitment user validation), and Phase 6 (Learnings — retrospective qualitative input).

---

## 6. Anti-Patterns / Common Failures

| Anti-Pattern | Why It Fails |
|---|---|
| **AI summary as substitute for verbatim** | Loses texture. Tags become the artifact; specific user voice gets buried. The most actionable research signal is the exact words a user used; if those don't survive synthesis, the synthesis is a generic theme catalog, not user research. |
| **Theme-clustering without ground-truth check** | AI invents themes that aren't actually present. LLMs are biased toward producing coherent thematic structure even when the data doesn't support it. Always read the underlying verbatim for any theme that informs a decision. |
| **Transcription accuracy assumed, not verified** | Errors compound. Speaker diarization mistakes, acronym mishearing, accent-dependent error rates mean the foundation can be wrong before AI synthesis starts. Verify transcript accuracy on the segments that inform conclusions. |
| **Auto-generated personas** | AI-generated personas inherit AI training-data biases without grounding in your actual research participants. They look fluent and feel real, which is exactly the problem — they aren't real. Personas must be grounded in your study population, not the model's. |
| **Synthesis at 100% AI confidence** | No human review = ungrounded conclusions. AI synthesis confidence scoring is a self-report by the model; it has no calibrated meaning. Treat AI as draft-quality regardless of confidence indicator. |
| **Research-as-decoration** | Synthesis cited to support pre-decided answers. AI makes this easier (faster to produce post-hoc justification). The mitigation is upstream: agree on what the research would have to show to change the decision, before reading the synthesis. |
| **Cross-study clustering without cohort discipline** | AI happily clusters quotes across studies that recruited different segments, different time periods, different product states. The themes look stronger than they are. Cohort matters; AI tagging often ignores it. |
| **Sentiment classification treated as truth** | Sentiment models miss sarcasm, technical-domain language, and culturally-loaded phrasing. "This is unbelievable" is positive or negative depending on what came before. Use sentiment as one signal among several; never as a sole basis for a finding. |

---

## 7. V2V Cross-References

**Sibling Q2-8 packs**:
- **`generative-ui.md` (Q2-8.1)** — research synthesis on AI-generated UI variations. Pattern 3 exploratory surfaces benefit from AI research synthesis to interpret user reactions; conversely, the voice-flattening risk in §3 here applies to feedback collected on Pattern 3 outputs.
- `accessibility-audit.md` — research with assistive-tech users carries additional consent + accommodation considerations; pair-read when research informs accessibility decisions.

**Sibling Q2-4 packs**:
- **`value-score-design.md` (Q2-4.1)** — customer-stated value verbatim that feeds Value Score per §3.2 of that pack is the same texture the human-in-loop synthesis pattern here is designed to preserve; AI synthesis that flattens verbatim destroys Value Score input quality.
- **`ai-agent-supervisor.md` (Q2-4.2)** — AI support fleet failures surfaced via support-ticket synthesis feed retraining triggers in that pack; the voice-flattening risk applies — premature theme-clustering hides the specific failure pattern the supervisor needs.
- **`customer-success-methodology.md` (Q2-4.3 refresh)** — QBR / churn-analysis qualitative research consumes this pack's synthesis discipline; CSAT-by-JTBD verbatim capture and explicit value verbatim depend on the human-in-loop pattern here.

**Sibling Q2-6 packs**:
- **`retention-marketing.md` (Q2-6.2)** — churn-reason research that segments win-back campaigns relies on AI-assisted reason coding; the segmentation discipline in that pack consumes synthesis output and depends on verbatim preservation.

**Sibling Q2-5 packs**:
- **`agentic-security.md` (Q2-5.3)** — when AI synthesis tooling itself is an agent system processing PII (transcripts, verbatim), the threat model applies; consent, retention, model-versioning governance interlock.

**Sibling Q2-3 packs**:
- **`agent-identity.md` (Q2-3.1)** — when AI synthesis runs as an agent invoking transcription / coding tools, the identity binding governs which corpus the agent can access.
- **`eu-ai-act-annex-iv.md` (Q2-3.4)** — when AI synthesis informs high-risk decisions (hiring, performance, customer-decisions), Annex IV documentation cites the synthesis methodology and human-in-loop discipline.

**Existing packs**:
- `user-research.md` — core methodology, AI synthesis layered on top.
- `research-methodology.md` — broader research-ops framing.
- `analytics-methodology.md` — quant pair to qual synthesis; triangulation patterns.
- `privacy-frameworks.md` — GDPR / CCPA / consent regimes when research includes PII (see §8).
- jurisdiction-specific GDPR guidance — substantive GDPR coverage when synthesis processes EU data subject data.

**Skill integrations**:
- `/interview-synthesis` — V2V skill consuming this pack for interview-specific synthesis.
- `/feedback-capture` — V2V skill; AI-assisted feedback tagging applies the patterns here.
- `/customer-health-scorecard` — V2V skill; Phase 5 application of AI research synthesis.

---

## 8. Sensitive-Skill Applicability

This pack is **NOT formally sensitive** under `sensitive-skill-guardrails.md` — research synthesis output is not legal, HR, or compliance advice.

However, the pack carries **privacy obligations** when research includes PII:
- **Consent management**: participant consent for recording, transcription, AI processing, and storage. AI processing is often a separate consent surface from human research processing; verify consent language covers it.
- **GDPR Article 6** (lawful basis) and **Article 9** (special-category data — health, ethnic origin, sexual orientation, political views, religious beliefs, trade union, genetic, biometric)
- **Recording-consent layered regimes**: U.S. state law varies (one-party vs all-party consent); EU GDPR layers on top; UK PECR for direct contact; sector overlays for regulated industries
- **AI processing disclosure**: increasingly required in EU and U.S. state regimes — participant must know AI will process their data

When synthesis output is shared externally (analyst briefings, sales enablement, marketing case studies) disclosure obligations layer further. Cross-reference `privacy-frameworks.md` and jurisdiction-specific GDPR guidance; involve privacy counsel for jurisdictional questions.

---

## Operating Principle

> *AI-assisted research synthesis is faster — but if the verbatim doesn't survive the synthesis, you've shipped the speed and lost the signal.*
