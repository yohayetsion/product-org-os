---
globs:
  - "**/*"
---

# Sensitive Skill Guardrails (MANDATORY)

Structural human-review enforcement for all legal, HR, compliance, and other liability-adjacent skills. This rule is load-bearing infrastructure: every Phase 3 (Legal Team), bias-sensitive HR, and compliance skill MUST conform before it can be published.

**Owner**: ⚖️ General Counsel (substantive gate) + 📋 Director of Legal Affairs (scaffolding gate)
**Status**: Active as of 2026-04-11 (Sub-phase 3.0)

---

## 1. Why This Rule Exists

> *Relocated 2026-08-15 (DR-2026-262): §1 three-liability-modes narrative (UPL / false confidence / scope drift) — full text in the companion sensitive-skill-guardrails.md (sibling of this rules directory; imposes nothing, relaxes nothing).*

The fix is structural, not per-skill reminders. Every sensitive skill MUST produce output in a shape that makes the review gate impossible to skip.

### 1.4 FCRA Exposure on Candidate-Scoring Outputs

> *Relocated 2026-08-15 (DR-2026-262): §1.4 FCRA/Eightfold filing background narrative — full text in the companion sensitive-skill-guardrails.md (sibling of this rules directory; imposes nothing, relaxes nothing).*

The theory is novel and untested. Whether AI candidate-scoring outputs ultimately qualify as "consumer reports" is open; the case is at pleading stage as of this writing. But the theory is credible enough that the complaint has been allowed to proceed, and credible enough that FCRA must be treated as live exposure on any AI-candidate-scoring skill produced by this product organization. Title VII disparate impact stays the dominant analysis for the underlying scoring model; FCRA layers on top, governing what the *employer-customer* must do procedurally with the output.

**The four discrete FCRA obligations that attach to any adverse employment action based in whole or in part on a consumer report:**

| Obligation | Statutory Source | What It Requires |
|---|---|---|
| **Pre-Adverse Action Notice** | 15 U.S.C. § 1681b(b)(3)(A)(i) | Before taking adverse action based in whole or in part on a consumer report, the user must provide the consumer with notice of the intended adverse action plus a copy of the report |
| **Copy of Consumer Report** | 15 U.S.C. § 1681b(b)(3)(A)(i) | The candidate is entitled to receive a copy of the actual report used in the adverse action — not a summary, not a redacted version |
| **Summary of Rights under FCRA** | 15 U.S.C. § 1681g | Written summary of consumer rights under FCRA, in the form prescribed by the CFPB, delivered with the pre-adverse-action notice |
| **30-Day Dispute Window + Reinvestigation** | 15 U.S.C. § 1681i | The consumer has 30 days to dispute inaccuracies in the report; the furnisher and the consumer reporting agency have reinvestigation obligations within that window before adverse action may proceed |

**Affected skills.** Any V2V OS or Extension Teams skill that produces, evaluates, or relies on AI-based candidate scoring or employment-adverse-decision outputs is in scope. Non-exhaustive examples: `/resume-summarizer`, recruiter-workflow skills that score or rank candidates, performance-review-AI skills that produce termination-supportive output, any skill that scores employees against a retention/PIP rubric. Their `## Cannot Assess Without` sections MUST enumerate the four FCRA obligations explicitly per Section 3.5's updated requirement below.

**Jurisdictional note.** FCRA is U.S. federal law. California (the Eightfold filing jurisdiction) layers state analogs on top — primarily the Investigative Consumer Reporting Agencies Act (ICRAA) and the Consumer Credit Reporting Agencies Act (CCRAA) — which add disclosure and copy-of-report obligations beyond federal FCRA. Other U.S. states (NY, MA, IL, MN, OK, WA) have additional layers. UK/EU jurisdictions operate under entirely different consumer-credit and data-protection regimes (UK Data Protection Act 2018, GDPR, EU AI Act) that produce analogous but non-equivalent obligations — those are addressed under privacy-frameworks coverage, not under FCRA. If a skill output may be acted upon outside U.S. federal jurisdiction, the skill author must declare the operative jurisdiction and the corresponding statutory frame in the skill's disclaimer block.

> *Relocated 2026-08-15 (DR-2026-262): §1.4 "why FCRA matters beyond Title VII" rationale (binding restatement retained inline at the §3.5.1 enforcement paragraph) — full text in the companion sensitive-skill-guardrails.md (sibling of this rules directory; imposes nothing, relaxes nothing).*

---

## 2. What Counts as "Sensitive"

A skill is sensitive if ANY of the following are true:

| Criterion | Example |
|---|---|
| Output could be mistaken for advice by a non-expert reader | `/contract-review`, `/privacy-policy-audit`, `/nda-triage` |
| Touches a regulated activity (UPL, EEOC, HIPAA, GDPR, SOX, FDA) | `/compliance-audit`, `/resume-summarizer`, `/ai-regulatory-audit` |
| Could create liability if the human-review gate is skipped | `/risk-analysis`, `/contract-stress-test`, `/privacy-policy-audit` |
| Produces content a reader might send to a counterparty verbatim | `/nda-triage`, `/contract-review` |
| Explicitly marked `sensitive: true` in its SKILL.md frontmatter | (any skill the author flags) |

**When in doubt, mark it sensitive.** The cost of structural scaffolding is low; the cost of missing it is real exposure.

---

## 3. Required Output Structure

Every sensitive skill MUST produce output that includes, in this order:

### 3.0 Spawn Audit Block — REQUIRED FIRST (v2 as of 2026-05-27; post-ROI schema as of 2026-08-01)

Every sensitive skill output MUST begin with the **Spawn Audit Block** from `agent-spawn-protocol.md` §2.5 BEFORE the disclaimer block. The two surfaces serve independent audit functions: the Audit Block surfaces what the agent loaded + the context injected/used + (for OS agents on deliverable tasks) which DRs were referenced/drafted/updated; the disclaimer surfaces output framing (audit of legal posture). Both are non-negotiable. (Per the 2026-08-01 schema change, agents emit no `[Post-Execution ROI]` section — hours are computed downstream per `agent-spawn-protocol.md` §3.)

Order of output:
1. **Spawn Audit Block** (this §3.0) — `[Pre-Execution Loads]` + `[Context Injected]` + `[Outputs]` (+ `[Decision Records]`/`[Context Records]`, OS-deliverable only)
2. **Disclaimer block** (§3.1) — verbatim "not advice" framing
3. **Jurisdiction Assumed** (§3.2) — scope declaration
4. **Findings** (§3.3) — substantive output
5. **Reviewer Checklist** (§3.4) — sign-off items
6. **Cannot Assess Without** (§3.5) — counsel-required items

The Audit Block is EDITABLE in content (lists what THIS spawn loaded, which DRs apply) but REQUIRED in presence. The disclaimer is verbatim. Both coexist.

> *Relocated 2026-08-15 (DR-2026-262). The §3.0 ordering rationale was retired 2026-08-30 (DR-2026-416); the order-of-output list above is the binding text. Other relocated rationale for this rule is in the companion sensitive-skill-guardrails.md (sibling of this rules directory; imposes nothing, relaxes nothing).*

**Protocol implication for sensitive skills (post-2026-08-01 schema)**: Most sensitive skills (legal, HR, compliance, privacy) live on ET agents, so the `[Decision Records]` section of their Audit Block is OMITTED (ET methodologies have no DR registry). The Audit Block reduces to `[Pre-Execution Loads]` + `[Context Injected]` + `[Outputs]` for those agents; no ROI section is emitted (retired 2026-08-01). Wherever computed hours for sensitive seats are DISPLAYED (dashboard, weekly email, any user-facing surface), the framing MUST be "drafting and triage" per `roi-display.md` → Sensitive Skill ROI Framing (that control is unchanged).

### 3.1 Disclaimer + UPL Guardrail Block (after Telemetry)

The standard block below must appear at the top of every sensitive skill output, **verbatim**, with `{jurisdiction}` filled in:

```markdown
> ⚠️ **Not legal advice.** This output is a drafting and triage aid generated by a product-organization skill, not counsel. No attorney-client relationship is created by its production or use. Jurisdiction-specific questions, contested matters, and any decision with material legal or regulatory consequences require review by a licensed attorney in the relevant jurisdiction. Do not rely on this output as the sole basis for any legal, compliance, or employment decision.
>
> **Jurisdiction Assumed:** {jurisdiction — e.g., "U.S. federal + Delaware," "England & Wales," "Singapore"}. If your jurisdiction differs, treat every finding below as a hypothesis to verify with local counsel.
```

No paraphrasing. No "light" versions. The exact block. For HR and compliance skills, substitute domain-appropriate language ("Not legal/HR advice... requires review by licensed counsel / qualified HR professional") but maintain the structure and the jurisdiction field.

### 3.2 Jurisdiction Assumed (field)

Every output declares the jurisdiction the skill assumed. If the user did not specify, the skill MUST ask before producing output OR must default to a named jurisdiction and flag the assumption explicitly.

### 3.3 `## Findings` section

The substantive output of the skill. Numbered findings. Each finding includes:
- **What** — the issue/observation
- **Why it matters** — the risk or implication
- **Severity** — P0 (blocker) / P1 (important) / P2 (nice-to-have)
- **Suggested next step** — what the human reviewer should do

### 3.4 `## Reviewer Checklist` section

Explicit items the human reviewer MUST sign off on before the output is acted upon. Example items:
- [ ] Jurisdiction confirmed
- [ ] Material facts verified against source documents
- [ ] Counterparty context reviewed (if applicable)
- [ ] All P0 findings addressed or explicitly accepted as risk
- [ ] Counsel engaged for items flagged in "Cannot Assess Without"
- [ ] This sign-off attests **review of the output ONLY** — it is **NOT** the FCRA § 1681b(b)(3) (or equivalent) adverse-action decision. For adverse-action skills, the per-action human decision is a separate act governed by §1.4 / §3.5.1 (see §5.5 gate-separation clause).

This is not decorative. It is the review gate made visible.

### 3.5 `## Cannot Assess Without {...}` section

Explicit list of what the skill DELIBERATELY did not opine on. Format:

```
## Cannot Assess Without Licensed Counsel
- Enforceability of non-compete clauses in {jurisdiction}
- Regulatory exposure under {specific statute}
- Tax treatment of {specific structure}
```

This section makes scope explicit and converts scope drift from invisible to blocking.

#### 3.5.1 Mandatory FCRA Enumeration for Candidate-Scoring Skills

For any skill that produces, evaluates, or relies on AI-based candidate scoring, employment-adverse decisions, or employment-related consumer-report-equivalent outputs (see Section 1.4 for the in-scope skill list), the `## Cannot Assess Without Licensed Counsel` section MUST enumerate the four FCRA obligations explicitly, verbatim or substantively equivalent:

```
## Cannot Assess Without Licensed Counsel
- Pre-adverse action notice obligations under 15 U.S.C. § 1681b(b)(3) — whether the employer-user has provided the consumer with notice of the intended adverse action plus a copy of the report before acting
- Copy of consumer report delivery under 15 U.S.C. § 1681b(b)(3) — whether the candidate has received the actual report used, not a summary or redacted version
- Summary of rights under FCRA per 15 U.S.C. § 1681g — whether the CFPB-prescribed summary has been delivered with the pre-adverse-action notice
- 30-day dispute window with reinvestigation obligations under 15 U.S.C. § 1681i — whether the consumer has been given the statutory 30 days to dispute, and whether the consumer reporting agency and furnisher have satisfied reinvestigation obligations before final adverse action
- Whether the skill output qualifies as a "consumer report" under 15 U.S.C. § 1681a(d) and whether the producing entity qualifies as a "consumer reporting agency" under § 1681a(f) (this is the novel theory at issue in Eightfold AI class litigation; assessment requires counsel)
- State-law layered obligations: ICRAA / CCRAA (California), and analogs in NY, MA, IL, MN, OK, WA
- Title VII disparate-impact exposure on the underlying scoring model (parallel and independent of FCRA — see EEOC guidance on AI in employment decisions)
```

Omission of any of the seven bullets above for an in-scope skill is a Pass 1 (Scaffolding) failure per Section 4. Authors may add additional bullets but may NOT remove the listed ones. The bullets exist because FCRA is independent of Title VII: a skill producing a perfectly fair score can still expose its user to FCRA liability if procedural obligations are not satisfied.

---

## 4. Publication Gate (Two-Pass)

No sensitive skill ships without both passes. The two passes are deliberately split so the substantive reviewer's time is not consumed by structural issues a director-level review can catch in 15 minutes.

### Pass 1 — Scaffolding Check

**Who**: Domain director (Legal → 📋 Director of Legal Affairs; HR bias-sensitive → 👥 CHRO or designate; Compliance → Compliance Officer).

**What gets checked** (~15 min, binary pass/fail on each):
- [ ] Standard disclaimer + UPL block present at top of output template, verbatim
- [ ] "Jurisdiction Assumed" (or equivalent scope field) wired into output
- [ ] `## Findings`, `## Reviewer Checklist`, `## Cannot Assess Without {...}` sections structurally present
- [ ] Delegation pattern cited by name from `delegation-protocol.md` (Patterns 1-5)
- [ ] ROI framing uses "drafting and triage" language, not "review"
- [ ] Frontmatter has `owner:`, `consumers:`, `sensitive: true`, and (if applicable) `deprecation:`
- [ ] Shared skill orchestrator fields correct (if consumed by multiple gateways)
- [ ] No copy-paste from external templates or forked source skills (first-principles authoring)

**SLA**: 48 hours for the initial Sub-phase 3.0 scaffolding pack sign-off. Individual skill scaffolding checks: same-day when the director is available, 48h worst case.

**Outcome**: GO / REWORK. A REWORK verdict returns the skill to the author with a specific numbered list of scaffolding failures. The skill does NOT advance to Pass 2 until Pass 1 is GO.

### Pass 2 — Substantive Check

**Who**: Domain owner (Legal → ⚖️ General Counsel; HR termination/hiring bias → 👔 Employment Counsel; Privacy → 🔒 Privacy Counsel; IP → IP Counsel).

**What gets checked**:
- Legal/policy reasoning in the skill's prompts and output schema
- Risk framing in severity tags (are P0/P1/P2 thresholds defensible?)
- Delegation pattern appropriateness (is Adversarial Review the right pattern here, or is Consultation sufficient?)
- Scope boundary correctness (does "Cannot Assess Without" capture the real edge cases?)
- Jurisdiction defaults defensible
- Edge cases and adversarial inputs (what does the skill do with a truly bad contract? a retaliatory termination? a GDPR-adjacent data flow?)
- First-principles authoring verified (no lifted content, citations are real)

**SLA**:
- **First-of-type skill in a new sub-domain** (e.g., the first contract skill, the first privacy skill): **5 business days**
- **Subsequent similar skills** (next contract skill, next privacy skill): **72 hours**

The longer SLA on first-of-type reflects that the reviewer is implicitly validating the pattern for the whole sub-domain, not just the individual skill.

**Outcome**: GO / GO WITH CHANGES / REWORK.
- **GO** → skill publishes
- **GO WITH CHANGES** → author applies named changes, gate owner acknowledges via comment, skill publishes
- **REWORK** → structural or reasoning issue serious enough that a second substantive review is required after changes

### Escalation

If a skill fails Pass 2 twice:
1. The author (usually a specialist agent) flags to the Director of the originating team
2. Director convenes a 3-way review: author + substantive gate owner + one independent reviewer from a related domain (e.g., Contracts Counsel reviewing a Privacy skill)
3. Decision: rework fundamentally, deprecate, or scope-reduce

If a skill fails Pass 2 three times → the skill is archived, not published. The team writes a learning note and moves on.

### Record Keeping

Every gate pass is logged in `context/decisions/{year}/` as a decision record (`DR-YYYY-NNN`) with:
- Skill name and owning agent
- Pass 1 reviewer + verdict + date
- Pass 2 reviewer + verdict + date
- Any REWORK cycles with a one-line reason
- Final disposition (published / archived / deferred)

---

## 5. ROI Framing Rule (Critical)

Sensitive skills MUST frame ROI as **"time saved on drafting and triage,"** NEVER as "time saved on legal review," "time saved on HR review," or "time saved on compliance review."

The reason is liability framing. "Time saved on legal review" implies the skill substitutes for counsel — which is exactly the UPL claim we cannot make. "Time saved on drafting and triage" correctly describes what the skill does: it produces a structured first pass that a human expert then reviews.

Full rule: see `.claude/rules/roi-display.md` → "Sensitive Skill ROI Framing" section.

---

## 5.5 Human-Driven-via-Standard

Move D of the V5.2.2 thesis names "Human-driven-via-Standard" as a strategic posture, and it stands: sensitive-skill outputs and high-stakes decisions remain **human-driven**. The Reviewer Checklist gate (§3.4) is the human gate. What follows scopes *how that gate is recorded* — because the recording mechanism differs by whether the output is a Decision Record or not, and the original framing over-generalized one mechanism (DPS Layer-4 attestation) to both. Origin of this clarification: **L-174 / DR-2026-129** (a §5.5 scope change to an inherited control).

### The two branches (scope of the attestation mechanism)

**Branch A — DR-backed OS deliverable outputs (Layer-4 attestation is real here).** When a sensitive output IS a Decision Record — i.e., an OS agent produced a deliverable that fired `agent-spawn-protocol.md` Phase-1.5 — the human sign-off at the §3.4 Reviewer Checklist becomes **machine-attestable** through the Decision Provenance Standard reporter: the Standard's Layer-4 attestation schema (`../knowledge/os-support/standard/v5.0/mode-drift/layer-4-attestation.schema.json`) captures the sign-off as a structured attestation event, and the affirming human closes the DR per `dr-affirmation-presentation.md`. Only in this branch does a real DPS Layer-4 event exist.

**Branch B — ET sensitive-skill outputs (the majority per §3.0 — enforced structurally, NOT via DPS).** ET agents are excluded from Phase-1.5 (`agent-spawn-protocol.md`), so their sensitive outputs are **not Decision Records** and have **no DPS Layer-4 attestation event by default**. Their human-review gate is enforced **structurally**: the §3.4 `## Reviewer Checklist` **plus a named-human sign-off recorded in the output itself** — reviewer **name + role + timestamp + an affirmation that the Reviewer Checklist was completed**. This ET sign-off is **NOT a DPS Layer-4 event.** Authors **MUST NOT fabricate a Layer-4 attestation event ID or a `seal_hash`** for an ET output (cross-ref `dr-affirmation-presentation.md` — never fabricate a `seal_hash`; record the affirmation in prose). The absence of a DPS event does **not** mean the ET output is ungated: its production gate is the **§4 two-pass publication gate plus this structural named-human sign-off** — both are required, and together they ARE the gate.

### Downstream verifiability is scoped to Branch A only

The "verifiable downstream **without requiring the human to be in every decision loop**" benefit applies **only** to Branch A (a past DR sign-off is verifiable after the fact) and must **never** be read as "ET human review can be skipped." For FCRA/AEDT skills and any adverse-action skill (§1.4, §3.5.1), the human **IS required in every adverse-action loop**: each adverse action is its own **15 U.S.C. § 1681b(b)(3)** event, and downstream verifiability of a *past* review sign-off never substitutes for the *per-action* human decision. There is no "attest once, skip the loop" path for adverse-action outputs.

### Gate-separation clause (the Reviewer Checklist ≠ the adverse-action decision)

The §3.4 Reviewer-Checklist sign-off — and, in Branch B, the ET Attestation Hook record — attests the **review-of-the-output** gate **ONLY**. It is **NOT** the FCRA § 1681b(b)(3) adverse-action decision, which is a separate human act governed by §1.4 and §3.5.1. **Neither the DPS Layer-4 attestation nor the Reviewer Checklist discharges the adverse-action obligation.** Signing off that the output was reviewed and taking the adverse action against a candidate are two distinct human acts; the first never stands in for the second.

### `## Attestation Hook` — redefined by branch

Sensitive-skill outputs SHOULD include a `## Attestation Hook` subsection, whose content depends on the branch:

- **Branch B (ET sensitive skills):** the Attestation Hook IS the **in-output named-human sign-off record** (reviewer name + role + timestamp + affirmation the §3.4 Reviewer Checklist was completed). It is **NOT** a DPS event and cites **no** Layer-4 event ID / `seal_hash`.
- **Branch A (DR-backed OS outputs):** the Attestation Hook additionally cites the **Layer-4 attestation event ID** once the human review is complete.

In both branches this is **OPTIONAL during drafting and REQUIRED for production publication.** The sign-off record — Branch A or B — MUST be **durable**: it lives in the **persisted deliverable artifact / review log**, never only in an ephemeral agent response.

> *Relocated 2026-08-15 (DR-2026-262): §5.5 closing rationale (Operating-Principle reinforcement) — full text in the companion sensitive-skill-guardrails.md (sibling of this rules directory; imposes nothing, relaxes nothing).*

Cross-references: `agent-spawn-protocol.md` §2.5 (Spawn Audit Block) and §Phase-1.5 (ET-agent DR-check exclusion — the reason Branch B exists); `dr-affirmation-presentation.md` (human affirmation of DRs; never fabricate a `seal_hash`); `roi-display.md` §Sensitive Skill ROI Framing; and — **scoped to Branch A (DR-backed OS outputs) only** — `../knowledge/os-support/standard/v5.0/mode-drift/layer-4-attestation.schema.json` (attestation event schema) and `../knowledge/os-support/standard/v5.0/README.md` (Naming Bridge — substrate ↔ book identifier reconciliation).

---

## 6. Enforcement Scope

This rule applies to:

- **All Legal Team skills**: the installed public legal capabilities
- **HR Team bias-sensitive skills**: hiring, termination, compensation, resume handling, PIP-related skills
- **Compliance Officer skills**: any skill producing regulatory readiness output
- **Any skill with `sensitive: true` in its SKILL.md frontmatter** — regardless of team

Skill authors who believe their skill is NOT sensitive but sits in one of the above teams must get an explicit exemption from the team gate owner and document it in the skill's frontmatter: `sensitive: false, exempted_by: {name}, rationale: {reason}`.

---

## 7. Self-Check Before Publishing a Sensitive Skill

- [ ] Standard disclaimer block present at top of output?
- [ ] "Jurisdiction Assumed" field wired in?
- [ ] `## Findings` section with numbered items and severity tags?
- [ ] `## Reviewer Checklist` with explicit sign-off items?
- [ ] `## Cannot Assess Without {...}` section present and non-empty?
- [ ] ROI framing uses "drafting and triage" language?
- [ ] Delegation pattern cited (Pattern 1-5 from `delegation-protocol.md`)?
- [ ] Scaffolding pass signed off by gate owner?
- [ ] Substantive pass signed off by domain owner?
- [ ] `## Attestation Hook` present (§5.5) — named-human sign-off in the persisted output; **Branch A** (DR-backed OS) also cites the Layer-4 event ID, **Branch B** (ET sensitive skills) does NOT and MUST NOT fabricate one?

If any check fails → not ready to publish.

---

## Operating Principle

> "Structure is the review gate. A disclaimer at the top of a formatted, confident-looking document is wallpaper. Findings / Reviewer Checklist / Cannot Assess Without is scaffolding that forces the human to engage before acting."
