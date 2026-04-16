---
name: privacy-policy-audit
description: Produces a disclosure-sufficiency and regulatory-fit audit of a public-facing privacy policy against a stated processing context, as a drafting and triage aid for human review, not a legal
  opinion or a DPIA.
argument-hint: '[privacy policy path or product name] or [update path/to/audit.md]'
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: legal-privacy
  skill_type: task-capability
  owner: privacy-counsel
  primary_consumers:
  - ext-legal
  - product
  - ext-corpdev
  sensitive: true
---
# /privacy-policy-audit

## Purpose

`/privacy-policy-audit` audits a public-facing privacy policy (a website's `/privacy` page, a product's in-app notice, an app store disclosure) against a stated processing context and the disclosure requirements of the major privacy regimes. For each audit dimension, it asks: what do the regs require the policy to disclose, what does this specific policy actually say, and where are the disclosure gaps? It is a **disclosure-sufficiency and regulatory-fit drafting and triage aid**, not a DPIA, not a data-flow archaeology, not a cookie scan, not a processor DPA review, not a legal opinion, and not a compliance attestation.

What it IS: an analytical ground-truth pass that reads the actual policy text, maps it against the disclosure obligations of GDPR (Art. 13/14 and adjacent), UK GDPR, CCPA/CPRA, LGPD (where LatAm is in play), COPPA (where children are in play), and ePrivacy cookie/tracker rules, and surfaces the gaps between what the regs require and what the policy actually discloses — framed as disclosure gaps vs Article requirements, never as legal conclusions about compliance.

What it is NOT: legal advice, a substitute for licensed counsel, a data inventory, a DPIA, a cookie scanner, a DPA review tool, a breach response plan, or a go/no-launch recommendation. Every finding is a hypothesis grounded in specific text (or specific absence) in a specific policy, for a human to verify against the real underlying processing.

The skill deliberately sits at **the document** (what the policy says) against **the regs** (what must be disclosed), given **a stated processing context** (what the product actually does, provided by the user). It does not audit the underlying processing itself. That job belongs to the sibling skills listed in "When NOT to Use."

---

## When to Use

Invoke `/privacy-policy-audit` when you need to:

- Ground-truth a product's public-facing privacy policy against the disclosure requirements of GDPR Art. 13/14, CCPA/CPRA notice-at-collection, LGPD Art. 9, and adjacent regimes
- Audit a pre-launch privacy policy before a product goes live (catch disclosure gaps before the first user signs up)
- Re-audit a privacy policy after a material change to the underlying product (new data source, new third party, new jurisdiction, new processing purpose, new AI/ML use)
- Prepare a privacy-policy-level triage for Privacy Counsel or General Counsel before a substantive review
- Stress-test a privacy policy before a Series A/B diligence, before a vendor DPA negotiation, or before a partner integration
- Audit an updated privacy policy in Update mode after revisions from the drafter
- Run an adversarial pass (`--mode adversarial`) on a near-final policy for a product with material regulatory exposure

## When NOT to Use

Do NOT use `/privacy-policy-audit` when:

- You need a **data inventory** / record-of-processing-activities (ROPA) — what data actually flows where, in what volumes, under what retention. This is `/data-mapping` (future sibling skill). `/privacy-policy-audit` audits the **document**; `/data-mapping` audits the **underlying processing**.
- You need a **DPIA** (Data Protection Impact Assessment) for a high-risk processing activity under GDPR Art. 35 — this is `/dpia` (future sibling skill)
- You need to **scan the live site for actual cookies and trackers** against what the policy declares — this is `/cookie-tracker-audit` (future sibling skill). The present skill can verify the policy's cookie disclosures are structurally complete against ePrivacy/GDPR consent requirements, but it cannot run a live crawl of the site.
- You need to **review a processor DPA** (Data Processing Agreement) from a vendor or sub-processor — this is `/dpa-review` (future sibling skill)
- You need a **breach response procedure** or an incident-response playbook — outside this skill, outside Phase 3 sub-phase scope
- You need to **triage a specific contract** clause by clause — use `/contract-review` (Phase 3 A1)
- You need an **NDA-specific triage** — use `/nda-triage` (Phase 3 A2)
- You need an **initiative-level risk landscape** across six domains — use `/risk-analysis` (Phase 3 A5)
- You need a **licensed legal opinion** on enforceability, litigation posture, or regulator exposure — engage outside counsel
- You need a **negotiation strategy** with a regulator, data subject, or counterparty — out of scope

The three sibling skills that ship in a future Phase 3 sub-phase — `/data-mapping`, `/dpia`, `/cookie-tracker-audit`, `/dpa-review` — are named here by design. Making the boundary explicit converts scope drift from invisible to blocking. When a user asks this skill to "check whether our real cookies match what we declare," the answer is "that is `/cookie-tracker-audit`, not this skill; I can verify the disclosure is structurally complete, but not that it is factually accurate against a live site."

---

## Modes

### Create (default)

Run a full disclosure-sufficiency and regulatory-fit audit of a specific privacy policy. Produces a new audit output file following the structure in the Output section.

```
/privacy-policy-audit legionis.ai/privacy
/privacy-policy-audit "AXIA public privacy policy draft"
/privacy-policy-audit path/to/src/app/(legal)/privacy/page.tsx
```

### Update

Re-audit an existing privacy policy after a drafter revision. Pass the path to the existing audit output.

```
/privacy-policy-audit update Legionis/Product/privacy-policy-audit-2026-04-11.md
```

Update mode preserves the finding numbering (adds 7a, 7b rather than renumbering), marks resolved findings with `~~strikethrough~~` plus a one-line reason, and keeps a `## Changelog` at the bottom of the file noting what the drafter moved on.

### `--mode adversarial`

Invokes Pattern 5 Adversarial Review from `delegation-protocol.md`. A fresh-context adversarial agent (typically `@general-counsel` or a peer `@privacy-counsel` instance, or — for multi-jurisdictional products — an agent spawned with a specific regional specialization) stress-tests the current audit findings without seeing the drafter's rationale. The pattern caps at two iterations. A named human tiebreaker must be specified BEFORE the review starts.

Use adversarial sub-mode ONLY when:

- The product is pre-launch or post-launch with material regulatory exposure (EU users, CA users, children, sensitive data, AI training)
- The cost of a missed disclosure gap is material (regulator attention, data-subject complaint, press risk, investor diligence)
- A named human tiebreaker is available
- The policy draft is near-final, not still evolving in shape

```
/privacy-policy-audit legionis.ai/privacy --mode adversarial --tiebreaker "Yohay Etsion"
```

For early-stage drafts, routine audits, and low-stakes triage, use default Create mode with Pattern 1 Consultation to pull in specialists (General Counsel for jurisdiction-specific enforceability, Compliance Officer for sector-specific regs like HIPAA/GLBA, IP Counsel for AI training data IP angles) for the dimensions that need their view.

---

## Inputs Required

The skill MUST collect the following before producing output. If any are missing, it asks the user rather than guessing. **The processing context is mandatory**: without it, any privacy policy audit hallucinates.

| Input | Required | Example |
|---|---|---|
| Privacy policy document (path, URL, or pasted text) | Yes | `C:/dev/legionis/src/app/(legal)/privacy/page.tsx` |
| **Processing context paragraph** | **Yes — skill refuses without it** | See below |
| Jurisdiction(s) in scope | Yes (may be multi) | "EEA/UK + US + Israel" |
| Stage | Yes | "Pre-launch" / "Live, beta" / "GA" |
| Known issues the user wants examined | If any | "We recently added PostHog; does the policy cover it?" |
| Tiebreaker (adversarial mode only) | Yes if adversarial | "Yohay Etsion" |

### The Processing Context (mandatory, one paragraph)

The user MUST supply (or the invoker MUST pass) a one-paragraph processing context covering:

1. **What the product does** — one sentence
2. **Primary user geographies** — EEA, UK, US, LatAm, Israel, APAC; B2B vs B2C
3. **AI/ML training on user data** — yes/no; if yes, is there an opt-out
4. **Child users** — yes/no/age-gated; under-16 exposure
5. **Sensitive data (GDPR Art. 9)** — health, biometric, political, religious, sexual orientation, trade union, genetic
6. **Key third parties** — auth provider, hosting, database, analytics, AI providers, payment, enrichment vendors
7. **Data residency** — where is data stored and processed
8. **Stage** — pre-launch, beta, GA

The skill uses this context as a **frame** for the audit. It does NOT validate the underlying processing against the context; that is `/data-mapping`. It verifies whether the **policy text** correctly discloses what the **context implies** — and flags anything the policy says that the context does NOT mention (e.g., policy names a processor not in the context → "disclosure gap in the context, or an undisclosed processor").

If the processing context is missing, the skill asks for it and produces no output until it is supplied. This is non-negotiable.

---

## Output Structure

Every `/privacy-policy-audit` output conforms to `sensitive-skill-guardrails.md` Section 3. Structure is non-negotiable; substantive findings vary per policy.

### 1. Disclaimer + UPL Guardrail Block (top)

Verbatim block from `sensitive-skill-guardrails.md` Section 3.1, with `{jurisdiction}` filled in from the user-supplied input. For privacy-specific framing, the block is adapted as follows (same structure, privacy-appropriate language):

> **Not legal advice.** This output is a drafting and triage aid generated by a product-organization skill, not counsel. No attorney-client relationship is created by its production or use. Privacy-regulatory questions are jurisdiction-specific and fact-specific; findings below are disclosure-gap hypotheses against published regulatory requirements, not legal conclusions about compliance. Do not rely on this output as the sole basis for any privacy, data protection, or regulatory decision. Any contested matter, any regulator-facing submission, and any material decision with privacy-regulatory consequences require review by a licensed attorney qualified in the relevant jurisdiction.
>
> **Jurisdiction Assumed:** {jurisdictions — e.g., "EEA/UK GDPR + US (CCPA/CPRA) + Israel (PPL)"}. Findings framed against disclosure requirements in the named regimes. If your product operates in additional jurisdictions, treat every finding below as a hypothesis to re-verify with local counsel for each regime.

### 2. Audit Metadata Block

A small labeled block under the disclaimer with:

- **Policy Audited**: title and last-updated date as written on the policy
- **Source**: path or URL
- **Audit Date**: today
- **Jurisdictions In Scope**: from the user input
- **Stage**: pre-launch / beta / GA
- **Audit Version**: 1.0.0 initial; 1.1, 1.2 etc. for updates

### 3. Processing Context Block

Echoes back the user-supplied processing context verbatim, so the audit is auditable against the frame it was run against. This also makes it visible when a later revision of the policy is run against a different context.

### 4. `## Findings`

Numbered list. Each finding has:

- **Dimension**: one of the 15 audit dimensions (see Method below), or contract-type-specific (e.g., AI-specific, Children's, Sensitive)
- **Regulatory anchor**: the specific Article/Section requirement (e.g., "GDPR Art. 13(1)(c) — purposes and legal basis", "CCPA §1798.100(b) — notice at collection", "CPRA §1798.130(a)(5) — right to limit use of sensitive PI", "COPPA 16 CFR §312.4 — parental notice")
- **What the policy says (or doesn't say)**: a grounded quote from the actual policy text, or `[ABSENT]` if the disclosure is not present, with a precise location (Section number, paragraph number)
- **The disclosure gap**: the specific gap between the regulatory requirement and the policy text
- **Severity**: `P0` (material disclosure gap — should be addressed before policy publishes or before next regulator-facing touchpoint), `P1` (important — should be addressed in the next revision), `P2` (nice-to-have — track)
- **Suggested remediation**: specific proposed disclosure text or a pointer to a library pattern. The skill does NOT author novel policy language. It suggests disclosures grounded in the regs themselves and flags what must go to Privacy Counsel to author.

Findings are tagged by dimension. Missing-disclosure findings (things the regs require that are not in the policy) are tagged `[ABSENT]` and are often more important than present-but-incomplete disclosures. Cross-dimension findings (e.g., the retention statement in Section 5 conflicts with the legal basis in Section 3) are tagged `[CROSS-DIMENSION]`.

**Framing rule (non-negotiable)**: Findings are framed as **"disclosure gap vs Art. N requirements"** — never as **"your policy is non-compliant with GDPR Art. 13."** The former is a drafting-and-triage observation; the latter is a legal conclusion the skill is not authorized to make. Example:

- CORRECT: "Disclosure gap vs GDPR Art. 13(1)(c): Section 3 lists processing purposes but does not identify a legal basis (consent / contract / legitimate interests / legal obligation) for each. Suggest adding a legal-basis column or sub-clause per purpose. Confirm with Privacy Counsel for jurisdictions of operation."
- INCORRECT: "This policy is non-compliant with GDPR Art. 13(1)(c) because it fails to identify legal bases."

### 5. `## Mandatory Escalate-to-Counsel Items`

Separate from the main Findings list. Two categories of finding ALWAYS escalate to a human reviewer and are never "auto-resolved" by the skill:

- **Children's data (COPPA / GDPR Art. 8)** — any indication the product may have under-16 users (or under-13 for COPPA), or that the policy's age-gate language is weak
- **Sensitive data (GDPR Art. 9)** — any indication the product processes health, biometric, political, religious, sexual orientation, trade union, or genetic data

If either is flagged, the skill produces the finding AND lists it separately under Mandatory Escalate-to-Counsel, with the specific reviewer (Privacy Counsel as default, with General Counsel and Compliance Officer as escalation) named.

### 6. `## Reviewer Checklist`

Explicit sign-off items. Minimum checklist:

- [ ] Processing context confirmed to match the underlying product (not just the policy)
- [ ] Jurisdictions in scope confirmed against actual user base
- [ ] Every P0 finding addressed in revision or explicitly accepted-with-risk by named approver
- [ ] Every P1 finding triaged (addressed, accepted, or escalated)
- [ ] Every `[ABSENT]` finding either added as a disclosure or explicitly waived with documented reason
- [ ] Every `[CROSS-DIMENSION]` finding verified — the interaction works in both directions
- [ ] Mandatory Escalate-to-Counsel items routed to named human reviewer
- [ ] Privacy Counsel engagement noted for each jurisdiction of operation
- [ ] Every third party named in the policy exists in the real vendor list; every real vendor processing personal data is disclosed
- [ ] Cross-border transfer mechanisms named in the policy match the real data flows
- [ ] AI-specific disclosures reviewed against actual training/eval/fine-tuning practices
- [ ] Retention statements match real deletion cadence (verify with engineering)
- [ ] Contact channel (privacy@ or equivalent) is monitored and has a response SLA

### 7. `## Cannot Assess Without Licensed Counsel`

Explicit list of what the skill deliberately did NOT opine on. Minimum 5 items for any privacy policy; more for multi-jurisdiction or regulated-industry products.

Format each as a single line: "Enforceability of {clause} in {jurisdiction}" / "Regulator position on {novel question}" / "Sector-specific regulation under {statute}" / etc.

### 8. (Optional) Changelog (update mode only)

If update mode, a `## Changelog` section at the bottom listing what the drafter moved on since the prior audit, which findings were resolved, which became moot, and which new findings appeared.

---

## Method

The skill's disclosure-sufficiency pass follows this sequence. Order matters because later dimensions depend on the output of earlier ones.

### Step 1 — Extract the Policy Text

Read the policy end-to-end. If the source is a JSX/TSX component, extract the rendered text content from the JSX (ignoring styling, layout, and interactive-element wrapping). If the source is a URL, fetch the rendered HTML and extract the text. If the text cannot be extracted (technical limitation, PDF with images, encoded content), flag that explicitly and audit only what can be read — never fabricate findings about content that was not read.

Build an internal map of:

- The sections that ARE present (by heading and sub-heading)
- The last-updated date as written on the policy
- The controller identity (who is the named data controller?)
- The contact mechanism (email, web form, postal address)
- Any data processor addendum, cookie notice, or linked sub-policies referenced

### Step 2 — Apply the 15 Audit Dimensions, In Order

For each dimension, pull the regulatory requirement and the disclosure checklist, then run it against the actual policy text. The 15 dimensions are listed in Step-order below; each becomes one or more Findings if gaps exist.

#### Dimension 1 — Identification & metadata

Regulatory anchors: GDPR Art. 13(1)(a)-(b) (controller identity, contact); UK GDPR same; CCPA §1798.130 (business identity); LGPD Art. 9(I); ePrivacy "in clear and comprehensive information" requirement.

Checklist:
- Is the named data controller identified with a legal entity name (not a brand name alone)?
- Is a contact mechanism specified (email minimum; postal address for regulated sectors)?
- Is a DPO contact identified if one is appointed (required under GDPR Art. 37 for certain controllers)?
- Is there a last-updated date?
- If the company operates in multiple jurisdictions, is there a mechanism for jurisdiction-specific questions (e.g., EEA representative under GDPR Art. 27 if the controller is outside the EEA)?

#### Dimension 2 — Data categories

Regulatory anchors: GDPR Art. 13(1)(c) and Art. 14(1)(d) (categories of personal data); CCPA §1798.130(a)(5)(B) (categories of personal information); LGPD Art. 9(II).

Checklist:
- Are the categories of data enumerated (not just "personal data")?
- Are sensitive categories (Art. 9) called out separately if applicable?
- Are inferred/derived data and AI-generated outputs mentioned if applicable?
- Is biometric, health, location, or other high-risk data identified?

#### Dimension 3 — Sources

Regulatory anchors: GDPR Art. 14(2)(f) (source of personal data when not collected from the data subject); CCPA §1798.130(a)(5)(B) (categories of sources).

Checklist:
- Is "from the data subject" (direct collection) distinguished from "from third parties" (indirect collection)?
- Are third-party sources named (e.g., an enrichment vendor like People Data Labs, Clearbit, Fullcontact)?
- Is observed data (analytics, device telemetry) distinguished from inferred data (AI-derived)?

#### Dimension 4 — Processing purposes

Regulatory anchors: GDPR Art. 13(1)(c) and Art. 14(1)(c); CCPA §1798.100(a)-(b); LGPD Art. 9(III).

Checklist:
- Are processing purposes enumerated specifically (not just "to provide the service")?
- Is each purpose distinct enough that a data subject can decide which they object to?
- Are secondary purposes (analytics, improvement, marketing) separated from primary ones?

#### Dimension 5 — Legal bases (GDPR Art. 6 & 9) — the heart of the audit

Regulatory anchors: GDPR Art. 6(1) (lawful bases — consent, contract, legal obligation, vital interests, public task, legitimate interests); Art. 9(2) (conditions for processing special categories); Art. 13(1)(c); Art. 14(1)(c).

Checklist:
- Is EACH processing purpose mapped to a specific legal basis (not a generic "we process lawfully")?
- If legitimate interests is claimed, is the interest identified (so a data subject can exercise Art. 21 objection rights)?
- Are consent-based processing purposes identified as such, with consent being distinguishable from contract or legitimate interests?
- For Art. 9 sensitive categories, is the specific Art. 9(2) condition named?
- Are AI training purposes (if any) mapped to a legal basis that can actually support them — increasingly contested (EDPB, CNIL positions evolving)?

This dimension is the heart of the audit. A privacy policy that lists purposes without legal bases is not making the disclosures GDPR Art. 13(1)(c) requires.

#### Dimension 6 — Data subject rights (Art. 13/14/15-22)

Regulatory anchors: GDPR Art. 13(2)(b), Art. 14(2)(c), Art. 15-22; UK GDPR same; CCPA §1798.100-130 (access, deletion, correction, opt-out, limit); CPRA sensitive-PI rights; LGPD Art. 17-22.

Checklist:
- Are Art. 15 access rights disclosed?
- Art. 16 rectification?
- Art. 17 erasure / right to be forgotten?
- Art. 18 restriction?
- Art. 20 portability?
- Art. 21 objection (including specifically for direct marketing and legitimate-interest-based processing)?
- Art. 22 automated decision-making, including right to human review?
- Right to lodge a complaint with a supervisory authority (Art. 13(2)(d))?
- CCPA: right to know, right to delete, right to correct (CPRA addition), right to opt-out of sale/sharing, right to limit use of sensitive PI (CPRA addition)?
- How does the data subject exercise these rights (contact channel, timeline to respond)?
- Is the 1-month GDPR response timeline or the 45-day CCPA timeline named?

#### Dimension 7 — Retention

Regulatory anchors: GDPR Art. 13(2)(a) and Art. 14(2)(a) (retention period or criteria for determining it); CCPA §1798.100(a)(3); LGPD Art. 15 and Art. 16.

Checklist:
- Is a retention period stated for each category of data, OR criteria for determining the period?
- Is the basis for the retention period disclosed (e.g., "7 years for billing records as required by tax law")?
- Is the deletion cadence described (e.g., "within 30 days of account deletion")?
- Are there explicit exceptions (e.g., "we retain backups for 90 days beyond deletion")?

#### Dimension 8 — Third-party recipients & processors

Regulatory anchors: GDPR Art. 13(1)(e) and Art. 14(1)(e) (recipients or categories of recipients); CCPA §1798.130(a)(5)(C)(i) (categories of third parties); LGPD Art. 9(V).

Checklist:
- Are third-party processors named (or at least categories disclosed)?
- Is the purpose of each processor disclosed?
- Is the data shared with each processor disclosed?
- If the policy names specific vendors (good practice but creates update burden), are they all still current?
- Are sub-processors disclosed or at least the mechanism for notice-of-new-sub-processor?

#### Dimension 9 — Cross-border transfer mechanisms

Regulatory anchors: GDPR Art. 13(1)(f) and Art. 14(1)(f) (transfer to third country, transfer mechanism, availability of safeguards); GDPR Chapter V (Art. 44-50); UK IDTA; EU-U.S. Data Privacy Framework (DPF); Swiss-U.S. DPF; EDPB 05/2021 guidance on international transfers.

Checklist:
- Is a transfer outside the EEA/UK identified?
- Is the transfer mechanism named (SCCs, IDTA, adequacy decision, BCRs, DPF certification)?
- Is the recipient country/region named?
- Is the data subject given a way to obtain a copy of the safeguards?
- If the controller relies on adequacy, is the specific adequacy decision cited (e.g., "Israel has an adequacy finding from the European Commission under Decision 2011/61/EU")?
- If data flows through a U.S. processor (almost universal for SaaS), is the post-Schrems II transfer analysis reflected?

#### Dimension 10 — Children's data (COPPA / Art. 8) — mandatory escalate

Regulatory anchors: GDPR Art. 8 (child's consent under 16, or lower down to 13 per Member State); COPPA 16 CFR Part 312 (under 13 in the US); CCPA §1798.120(c) (opt-in sale/share for minors 13-16, verifiable parental consent for under 13).

Checklist:
- Does the policy state an age threshold (minimum age of users)?
- Is the age threshold appropriate for the product and the user base (e.g., a consumer product should not say "not for under 18" without age-gating)?
- If the product may have under-16 users, are COPPA/Art. 8 parental consent and notice requirements addressed?
- Does the policy provide a mechanism for a parent to request deletion of a child's data?

**Children's data findings ALWAYS escalate to counsel** and are listed in the Mandatory Escalate-to-Counsel section in addition to the main Findings.

#### Dimension 11 — Sensitive data (Art. 9) — mandatory escalate

Regulatory anchors: GDPR Art. 9 (special categories); CPRA §1798.121 (right to limit use of sensitive PI); LGPD Art. 11 (sensitive personal data).

Checklist:
- Does the product process any Art. 9 categories (health, biometric, genetic, political, religious, sexual orientation, trade union)?
- If yes, is the specific Art. 9(2) condition named (consent, employment law, vital interests, substantial public interest, etc.)?
- Are the CPRA sensitive-PI categories (precise geolocation, race/ethnicity, religious beliefs, union membership, communications contents, genetic data, biometric for unique ID, health, sex life, SSN, DL, financial account, account login) addressed with the right-to-limit disclosure?

**Sensitive-data findings ALWAYS escalate to counsel** and are listed in the Mandatory Escalate-to-Counsel section in addition to the main Findings.

#### Dimension 12 — Cookies/trackers consistent with ePrivacy / GDPR consent

Regulatory anchors: ePrivacy Directive 2002/58/EC Art. 5(3) (consent for non-essential storage); GDPR Art. 7 (conditions for consent); EDPB 01/2020 guidelines on targeted advertising and 05/2020 on consent.

Checklist:
- Is there a cookie disclosure (either inside the policy or in a linked cookie notice)?
- Are cookies categorized (strictly necessary, functional, analytics, marketing)?
- Is consent required before non-essential cookies fire (via a consent banner), and does the policy describe this mechanism?
- Is a withdrawal mechanism described?
- Does the policy's cookie list align with what the context says is actually deployed? (The skill flags gaps but cannot verify against a live site — that is `/cookie-tracker-audit`.)

#### Dimension 13 — CCPA/CPRA disclosures

Regulatory anchors: Cal. Civ. Code §1798.100 et seq.; CCPA regs 11 CCR §7000 et seq.; CPRA amendments.

Checklist:
- Is a notice-at-collection disclosure present or linked at the point of collection?
- Is the list of categories collected in the last 12 months present?
- Is "Do Not Sell or Share My Personal Information" available as a disclosure AND a mechanism if the product sells or shares PI?
- Is "Limit the Use of My Sensitive Personal Information" available if sensitive PI is collected?
- Are the consumer rights (know, delete, correct, opt-out, limit, non-discrimination) disclosed?
- Is the authorized-agent mechanism described?
- Is the financial-incentives disclosure required (if any loyalty/referral programs involve PI)?

Note: CCPA/CPRA only applies to businesses meeting size/revenue/data-volume thresholds. If the product is unlikely to meet thresholds, the audit flags this as a scope note but still checks the disclosures (since the thresholds can be crossed).

#### Dimension 14 — LGPD disclosures (if LatAm exposure)

Regulatory anchors: LGPD (Law 13,709/2018) Art. 9 (disclosure at collection); ANPD resolutions.

Checklist:
- Is there a legal basis named under LGPD Art. 7 for each processing purpose (separate from GDPR Art. 6 — the lists differ)?
- Are LGPD-specific data subject rights (Art. 18) disclosed?
- Is a DPO identified (Art. 41 — encarregado)?
- Is international transfer addressed under LGPD Art. 33 criteria?

If the product has no Brazilian/LatAm users, LGPD dimension is noted but not audited in depth. Flag as a future re-audit trigger if the product launches in LatAm.

#### Dimension 15 — AI-specific disclosures

Regulatory anchors: EDPB Opinion 28/2024 on models trained with personal data; CNIL 2024-2025 positions on generative AI; Italian Garante 2023-2024 enforcement; GDPR Art. 22 (automated decision-making); EU AI Act (where the product is an in-scope AI system); Colorado AI Act; various state-level AI regulations.

Checklist:
- Is AI/ML model training on user data disclosed?
- If yes, is the legal basis for training named? (This is increasingly contested — legitimate interests claims are being rejected in several jurisdictions.)
- Is an opt-out of training disclosed if training occurs?
- If inputs/outputs are routed to third-party AI providers (OpenAI, Anthropic, Google), is the routing disclosed and is the legal basis for the data sharing named?
- Are automated decisions with legal or similarly significant effects disclosed under Art. 22, including the right to human review?
- Is "we do NOT use your data to train AI models" a claim the policy makes? If so, it is a strong commitment that should be verified against engineering reality (not this skill's job — flag for reviewer).

AI-specific disclosures are a rapidly evolving area. The skill flags gaps but explicitly notes that the regulatory landscape is in flux and final positions require counsel input.

### Step 3 — Surface Missing Disclosures (`[ABSENT]`)

For each dimension, ask:

- Should this disclosure be present given the processing context?
- What is the downstream risk of its absence?
- Is the absence deliberate (e.g., no need to discuss COPPA for a strict B2B product with employee verification) or an omission?

Missing-disclosure findings are often the most important. Reviewers pattern-match on what they SEE and miss what is absent.

### Step 4 — Surface Cross-Dimension Interactions (`[CROSS-DIMENSION]`)

Once all dimensions have been read, look at them together:

- Does the retention statement (Dimension 7) align with the deletion commitment in data subject rights (Dimension 6)?
- Does the third-party list (Dimension 8) match the cross-border transfer disclosures (Dimension 9)? Every non-EEA processor needs a transfer mechanism.
- Does the controller identity (Dimension 1) match the entity named in the Stripe/payment/billing flow (Dimension 8)?
- Does the AI disclosure (Dimension 15) align with the "we don't train on your data" commitment in Dimension 4?
- Does the CCPA disclosure (Dimension 13) align with the EEA legal bases (Dimension 5) — the two regimes demand different framings for the same processing?

Cross-dimension findings are the ones a single-pass checklist misses.

### Step 5 — Assign Severity

Severity thresholds are defensible, not decorative:

- **P0 (material disclosure gap)** — if unaddressed, the policy does not disclose something a reasonable regulator or data subject would expect. Examples: no legal basis named for any processing; processor list omits a named AI provider that receives user content; cross-border transfer to the U.S. with no mechanism named; children's data handling absent for a consumer product; Art. 9 sensitive data processed without the specific Art. 9(2) condition named; AI training on user data undisclosed.
- **P1 (important)** — should be addressed in the next revision. Examples: data subject rights listed but response timeline not stated; retention described generically but not by category; DPO appointed but contact mechanism missing; CCPA rights listed without authorized-agent mechanism.
- **P2 (nice-to-have)** — track but does not block. Examples: last-updated date present but version history absent; some processor names outdated but categories still correct; language could be clearer but the disclosure is substantively present.

When in doubt, escalate one level (P2 → P1, P1 → P0). The cost of being overly cautious is a longer reviewer conversation; the cost of under-severity is a regulator finding or a complaint.

### Step 6 — Suggest Remediation

Each finding MUST include a specific next step. Acceptable forms:

- `Add disclosure: {specific text grounded in the regs}`
- `Revise Section N to state: {specific clarification}`
- `Engage Privacy Counsel to author {specific language} given jurisdictional sensitivity`
- `Verify {X} with engineering before revising` (when the question is factual about real processing)
- `Escalate to General Counsel for {strategic framing question}`
- `Confirm {X} with the processor's own privacy notice before disclosing`

The skill does NOT author novel privacy-policy language for contested questions. It suggests disclosures grounded in the regs themselves and flags what must go to Privacy Counsel.

### Step 7 — Write "Cannot Assess Without"

Written BEFORE finalizing findings. If an item goes here, it cannot also appear as a confident finding. The section is how the skill makes its scope explicit.

Typical items:

- Enforceability of {clause} under {specific regulator's current position}
- Sector-specific privacy regulation (HIPAA, GLBA, FERPA) and its interaction with the disclosures
- Multi-jurisdictional enforcement prioritization (which regulator would move first on {gap})
- Novel questions where EDPB / CNIL / ICO guidance is still evolving
- Whether the processing context matches the actual data flows (that is `/data-mapping`)
- Whether the cookie list in the policy matches the live site (that is `/cookie-tracker-audit`)
- Whether processor DPAs actually contain the commitments the policy implies (that is `/dpa-review`)

---

## Delegation Patterns Available

### Default: Pattern 1 Consultation

When a specific audit dimension needs specialist input, `/privacy-policy-audit` spawns a consultation per `delegation-protocol.md` Pattern 1:

| Trigger | Spawn |
|---|---|
| Jurisdiction-specific enforceability or regulator position | ⚖️ General Counsel |
| Sector-specific regulation (HIPAA, GLBA, FERPA, PCI-DSS) | ⚖️ Compliance Officer |
| AI training data and IP angles | 📜 IP Counsel |
| Employment-adjacent processing (monitoring, performance, HR data) | 👔 Employment Counsel |
| Contract-level DPA, order-of-precedence, processor terms | 📄 Contracts Counsel |
| Multi-jurisdictional strategic framing | ⚖️ General Counsel |
| Real-world data flow verification | → defer to `/data-mapping` (future sibling skill) |
| Live cookie inventory verification | → defer to `/cookie-tracker-audit` (future sibling skill) |
| Processor DPA substantive review | → defer to `/dpa-review` (future sibling skill) |

Consultations are attributed in the Findings section: "I consulted ⚖️ Compliance Officer, who noted that if health-related AI agents are used (Dimension 11), HIPAA applicability depends on whether the company is a covered entity or business associate under 45 CFR 160.103 — confirm with counsel before relying on the current disclosure." Ownership of the audit stays with Privacy Counsel.

### On Request: Pattern 5 Adversarial Review (`--mode adversarial`)

Use for privacy policies where the cost of a missed disclosure gap is material. Requires all four Pattern 5 guardrails: named human tiebreaker before the review starts, fresh-context spawn of the adversarial agent, maximum two iterations, and role separation (drafter does not see adversarial findings until after they are produced).

Do NOT use Pattern 5 for early-stage drafts, routine audits, or deliverables where one "correct" answer exists. Use default Create mode with Pattern 1 Consultation for those cases.

---

## Quality Gates

`/privacy-policy-audit` is a sensitive skill. It ships only after passing the two-pass publication gate defined in `sensitive-skill-guardrails.md` Section 4:

- **Pass 1 — Scaffolding Check** — 📋 Director of Legal Affairs verifies the structure (disclaimer, audit metadata, processing context block, Findings with regulatory anchors, Mandatory Escalate-to-Counsel section, Reviewer Checklist, Cannot Assess Without, frontmatter, ROI framing, delegation citation, first-principles authoring, 15-dimension coverage). 15 minutes, binary GO / REWORK.
- **Pass 2 — Substantive Check** — 🔒 Privacy Counsel (substantive owner) verifies the regulatory reasoning, severity thresholds, dimension coverage, escalate-to-counsel triggers, delegation-pattern appropriateness, scope boundary correctness (the four sibling-skill boundaries), jurisdiction handling, and edge cases. **72-hour SLA** for this subsequent-similar Phase 3 legal skill; the template pattern was validated by A5 `/risk-analysis` and A1 `/contract-review` publication earlier in the sub-phase, so A3 inherits the subsequent-similar timeline rather than the 5-business-day first-of-type SLA.

On every invocation, the skill self-checks against Section 7 of `sensitive-skill-guardrails.md` BEFORE producing output. If the self-check fails on any item, the output does not publish.

---

## ROI Framing

ROI for `/privacy-policy-audit` is reported as **"time saved on drafting and triage of a privacy policy audit"** — NEVER "time saved on privacy review" or "time saved on compliance review."

Legal rate: $300-400/hr blended per `feedback_roi_rates.md`. Default $350/hr for a Phase 3 privacy audit across 15 dimensions on a multi-jurisdiction B2C product.

Time-saved baseline: a structured 15-dimension audit of a pre-launch or live privacy policy (2,000-5,000 words, 10-15 sections, multi-jurisdiction), producing 10-20 findings grounded in actual policy text with specific regulatory anchors, is ~3-4 hours of manual drafting and triage time for a senior privacy practitioner. Simpler audits (single-jurisdiction, minimal processing, no sensitive or child data) are 1.5-2 hours baseline. Multi-jurisdictional audits with AI training, sensitive data, or regulated-sector overlays are 5-6+ hours baseline.

The ROI tracks ONLY the time the skill saves on drafting the structured artifact, not the substantive privacy review time. The substantive review by Privacy Counsel (and General Counsel for cross-jurisdictional questions) still happens in full.

Example ROI line for a standard multi-jurisdictional privacy audit:

```
⏱️ ~3.5 hrs saved in 85s, 28k tkns ~$1.7 cost, Value ~$1,225
```

---

## Attribution and Maintenance

**Owner**: 🔒 Privacy Counsel. The skill's 15-dimension reasoning is Privacy Counsel's accountability. The severity thresholds and the regulatory anchors are jointly owned with ⚖️ General Counsel.

**Consumers** (gateways that invoke this skill):
- `ext-legal` — legal team gateway, primary user
- `product` — product gateway when PM/VP Product receives a draft policy from engineering or marketing and needs a disclosure triage before engaging counsel
- `ext-corpdev` — corp dev gateway for diligence on partnership, acquisition, or investment targets where the target's privacy posture matters

New consumers require a frontmatter update and a one-line note in the consuming gateway's skill list.

**Authoring**: First-principles. This skill was authored from scratch during Phase 3 Sub-phase 3.0, inheriting the structural pattern from A1 `/contract-review` and A5 `/risk-analysis` but with entirely original content for privacy-regulatory dimensions. A3 is the first privacy-specific skill; subsequent privacy skills (`/data-mapping`, `/dpia`, `/cookie-tracker-audit`, `/dpa-review`) will inherit the 15-dimension-style pattern from here where appropriate.

**Sibling-skill dependency**: `/privacy-policy-audit` explicitly names the four future sibling skills whose scope it does NOT cover: `/data-mapping`, `/dpia`, `/cookie-tracker-audit`, `/dpa-review`. This boundary is load-bearing; any ambiguous request is routed to whichever sibling owns the underlying question.

**Updates**: Via the two-pass publication gate. Minor edits (typos, formatting, new regulatory citations as they emerge) can bypass Pass 2. Any edit touching severity thresholds, dimension list, delegation patterns, escalate-to-counsel triggers, or the output structure requires a full Pass 2 substantive review by Privacy Counsel.

**Changelog**: Maintained at the bottom of this file. Version 1.0.0 — initial authoring 2026-04-11.

---

## Example Invocation

```
User: /privacy-policy-audit C:/dev/legionis/src/app/(legal)/privacy/page.tsx

/privacy-policy-audit v1.0.0 — reading:
  - C:/dev/legionis/src/app/(legal)/privacy/page.tsx (Next.js JSX source)
  - Last updated: March 3, 2026
  - 11 sections, approx 1,200 words rendered text

Collecting inputs:
  - Policy: Legionis Privacy Policy (v2026-03-03)
  - Source: Next.js JSX source file
  - Jurisdictions: EEA/UK + US (CCPA/CPRA) + Israel (PPL)
  - Stage: Pre-launch / B2C beta
  - Processing context: B2C AI workforce platform, global user base, BYOT AI model
    (user-supplied API keys), child users gated at 16+, third parties include Clerk/
    Stripe/Neon/Vercel/PostHog/People Data Labs/AI providers, data processed in
    Israel + US, controller is Etsion Brands Ltd.

Producing output at:
  Legionis/Product/privacy-policy-audit-2026-04-11.md

[output follows standard structure: disclaimer → audit metadata → processing context →
 findings with regulatory anchors → mandatory escalate-to-counsel → reviewer checklist →
 cannot assess without]

⏱️ ~3.5 hrs saved in 85s, 28k tkns ~$1.7 cost, Value ~$1,225
```

---

## Changelog

- **1.0.0 (2026-04-11)** — Initial authoring. First-principles during Phase 3 Sub-phase 3.0. First privacy-specific skill. Birth-tested against the Legionis public privacy policy (v2026-03-03) as a real pre-launch artifact; bootstrapped the initial 15-dimension audit pattern from the review. Substantive review passed by 🔒 Privacy Counsel on the 72-hour subsequent-similar SLA (A5 `/risk-analysis` and A1 `/contract-review` validated the template pattern earlier in the sub-phase); scaffolding review passed by 📋 Director of Legal Affairs.
