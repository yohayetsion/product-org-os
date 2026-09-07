# Companion — sensitive-skill-guardrails (relocated reference)

> Relocated rationale/reference — the binding rule is `.claude/rules/sensitive-skill-guardrails.md`;
> this file imposes nothing and relaxes nothing. Moved VERBATIM 2026-08-15
> (DR-2026-262). Do not edit here
> without the same review the rule itself requires.

---

<!-- from sensitive-skill-guardrails · REFERENCE-MOVE · §1 three-liability-modes narrative -->

A product-organization skill that produces legal, HR, compliance, or regulatory output can create liability in three ways:

1. **Unauthorized Practice of Law / HR / Medicine** (UPL / equivalent) — if output reads like advice and a non-expert acts on it without counsel review, the authoring party may be exposed under state bar rules, EEOC guidance, HIPAA, or equivalent frameworks.
2. **False confidence** — structured, well-formatted skill output is pattern-matched by readers as "authoritative." Without explicit scaffolding that names the limits, readers routinely skip the human-review gate.
3. **Scope drift** — a skill written to triage contracts is used three months later to decide an M&A deal. Without an explicit "Cannot Assess Without" section, scope creep is invisible.

---

<!-- from sensitive-skill-guardrails · REFERENCE-MOVE · §1.4 FCRA/Eightfold filing background narrative -->

A second statutory pathway to AI-hiring liability runs through the **Fair Credit Reporting Act (15 U.S.C. § 1681 et seq.)**, parallel to and independent of Title VII disparate-impact theory. The pathway came into focus with the **Eightfold AI class action, filed 2026-01-20 in California state court**, which named Microsoft and PayPal as customers using Eightfold's AI candidate-scoring outputs. The class theory: an AI candidate-scoring tool's output qualifies as a "consumer report" under 15 U.S.C. § 1681a, furnished by what FCRA calls a "consumer reporting agency" (§ 1681a(f)) — and if it does, every adverse employment action taken in reliance on that output must satisfy FCRA's procedural obligations on the employer using it.

---

<!-- from sensitive-skill-guardrails · REFERENCE-MOVE · §1.4 why-FCRA-matters-beyond-Title-VII rationale -->

**Why FCRA matters even though Title VII already covers AI hiring.** Title VII reaches discriminatory *outcomes* via disparate-impact analysis; FCRA reaches procedural *handling* of the consumer-report-equivalent output regardless of whether the scoring model is itself discriminatory. A skill that produces a perfectly fair, non-discriminatory candidate score can still create FCRA exposure for its user if the user takes adverse action without the four procedural obligations satisfied. The two regimes are independent. Scaffolding must reflect that.

---

<!-- from sensitive-skill-guardrails · REFERENCE-MOVE · §5.5 closing rationale -->

This scoping reinforces rather than carves an exception to this rule's Operating Principle — **"Structure is the review gate"**: the ET named-human sign-off in the persisted output is exactly that structure, and DPS Layer-4 attestation is the *additional* provenance layer available only where a Decision Record already exists.
