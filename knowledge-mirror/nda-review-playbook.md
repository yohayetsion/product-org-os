# NDA Review Playbook Knowledge Pack

> Informational reference for drafting and triage, not legal advice. No attorney-client relationship is created by its use. Engage licensed counsel before relying on any clause, template, or position herein.

**Version**: 1.0
**Type**: knowledge-pack
**Primary Users**: @contracts-counsel, @general-counsel, @legal-dir

---
<!-- Attribution:
  Frameworks and patterns in this knowledge pack were informed by:
  - Anthropic knowledge-work-plugins (github.com/anthropics/anthropic-cookbook) — legal/triage-nda
  - IACCM (International Association for Contract & Commercial Management) — NDA benchmarks
  - World Commerce & Contracting — mutual NDA standard positions
  Adapted and expanded for Product Org OS agents.
-->

---

## NDA Triage Workflow

Process every inbound NDA through four sequential gates before legal review begins.

```
STEP 1: ACCEPT
  ├── Confirm NDA relates to a legitimate business purpose (diligence, partnership, vendor, employment)
  ├── Verify requesting party is identified (company name, signatory name)
  ├── Confirm urgency / requested turnaround from business owner
  └── Log in NDA tracker (parties, date received, requested date, purpose)

STEP 2: CLASSIFY
  ├── Mutual (MNDA) vs. Unilateral (one-way NDA)?
  ├── Standard form vs. custom/negotiated?
  ├── Which party's paper? (Ours / Counterparty / Third-party template)
  └── Transaction type: M&A diligence | Vendor / Supplier | Strategic partnership | Employment | Research

STEP 3: SCREEN
  ├── Run 12-point screening checklist (see below)
  ├── Identify clause-level risk: Green / Yellow / Red
  └── Determine routing: Auto-approve | Standard review | Senior review | Negotiation required

STEP 4: ROUTE
  ├── Green → Associate Counsel auto-approve with standard comments
  ├── Yellow → Contracts Counsel review (standard 48-hour SLA)
  ├── Red → General Counsel involvement required before counter or execution
  └── Unknown party / regulated industry → Compliance Officer consult before proceeding
```

---

## NDA Classification Matrix

| Dimension | Option A | Option B | Impact on Review |
|-----------|----------|----------|-----------------|
| **Directionality** | Mutual (MNDA) — both parties disclose | Unilateral — only one party discloses | Mutual = higher scrutiny; our obligations mirror counterparty's |
| **Form** | Our standard form | Counterparty's form | Their form = full clause review required; our form = check for unauthorized edits |
| **Transaction type** | M&A / Investment diligence | Vendor / Supplier / Partner | M&A = broader scope, longer term, stricter residuals needed |
| **Scope of information** | Technical IP heavy | Business / commercial only | IP heavy = tighter definition of CI, stronger return/destruction |
| **Governing jurisdiction** | Domestic | Cross-border | Cross-border = check enforceability, data transfer restrictions |
| **Regulated industry** | Healthcare, Finance, Defense | General commercial | Regulated = check sector-specific obligations (HIPAA, ITAR, etc.) |

---

## 12-Point Standard Screening Criteria

Check every NDA against all 12 criteria before routing.

| # | Criterion | Check |
|---|-----------|-------|
| 1 | **CI Definition** — Is Confidential Information defined precisely? Not over-broad ("all information") or under-defined. | |
| 2 | **Exclusions** — Standard exclusions present? (Public domain, independently developed, required by law, received from third party without restriction) | |
| 3 | **Standard of Care** — "Reasonable care" or stronger. Watch for "best efforts" (too onerous) or no standard specified. | |
| 4 | **Permitted Disclosures** — Employees, affiliates, advisors on need-to-know with equivalent obligations. No open-ended sharing rights. | |
| 5 | **Term** — Defined start and end date for disclosure period. Survival clause for obligations after expiry. | |
| 6 | **Return / Destruction** — Explicit obligation to return or certify destruction. Reasonable timeframe (typically 30 days). | |
| 7 | **Remedies** — Injunctive relief available (standard). Indemnification scope reasonable. Liquidated damages (flag if present). | |
| 8 | **Governing Law / Jurisdiction** — Specified and acceptable to our entity. Dispute resolution mechanism defined. | |
| 9 | **Residuals Clause** — Absent (preferred) or narrowly scoped. Broad residuals effectively nullify the NDA. | |
| 10 | **Non-Solicitation Rider** — If present: duration, scope, carve-outs for general recruitment. Absence is fine. | |
| 11 | **Non-Compete Rider** — If present: flag immediately for senior review. Duration, geography, scope must be reasonable. | |
| 12 | **Authority** — Signatory has authority to bind the entity. Corporate entity clearly identified (not individual only). | |

---

## Clause-by-Clause Review Checklist

### 1. Definition of Confidential Information

**What to check:**
- [ ] Does the definition capture what we actually need to protect? (Technical specs, code, customer lists, financial data, business plans)
- [ ] Is oral/visual information included? If yes, is there a written-confirmation requirement within [X] days?
- [ ] Are standard exclusions explicitly stated?
- [ ] Is "Confidential Information" definition symmetric in a mutual NDA?

**Standard Exclusions (all four must be present):**
```
Information is not Confidential if it:
  (a) Is or becomes publicly available through no breach of this Agreement;
  (b) Was already known to Receiving Party at time of disclosure (with evidence);
  (c) Is independently developed by Receiving Party without use of CI; or
  (d) Is received from a third party without restriction on disclosure.
```

**Red flags:**
- "All information shared" with no carve-outs
- Oral CI without written confirmation requirement (creates scope ambiguity)
- Definition excludes company's most sensitive categories
- Asymmetric definition in an MNDA

---

### 2. Obligations of the Receiving Party

**What to check:**
- [ ] Care standard: "Reasonable care" (acceptable) | "Same care as own CI, no less than reasonable care" (preferred) | "Best efforts" (negotiate down)
- [ ] Use restriction: Limited to stated purpose only. Purpose should be specifically defined, not "evaluating a potential relationship."
- [ ] Permitted personnel: Need-to-know employees and advisors only. Affiliates should require equivalent obligations.
- [ ] Sub-disclosure: Counterparty representatives bound by equivalent terms before access.
- [ ] Legal compulsion carve-out: If required by law or court order, prompt notice to disclosing party to seek protective order.

**Acceptable position:**
```
Receiving Party shall: (i) protect CI with at least the same degree of care used to protect
its own confidential information, but in no event less than reasonable care; (ii) use CI
solely for [Stated Purpose]; and (iii) limit disclosure to employees and advisors with a
need to know who are bound by confidentiality obligations at least as protective as this
Agreement.
```

---

### 3. Term and Survival

**What to check:**
- [ ] Disclosure period: When does the right to share CI begin and end?
- [ ] Obligation term: How long after expiry of the disclosure period do confidentiality obligations survive?
- [ ] Survival for trade secrets: Obligations for trade secrets should survive indefinitely (separate from general CI).

**Standard positions:**

| Scenario | Disclosure Period | Obligation Survival |
|----------|------------------|---------------------|
| Vendor evaluation | 1–2 years | 3 years post-expiry |
| Strategic partnership | 2–3 years | 5 years post-expiry |
| M&A diligence | Duration of process + 1 year | 5 years post-expiry |
| Employment | Duration of employment | 2–3 years post-termination |
| Trade secrets | N/A | Indefinite |

**Red flags:**
- No survival clause (obligations die with the NDA)
- Obligation term < 2 years for sensitive technical information
- No distinction between general CI and trade secrets

---

### 4. Return and Destruction of Information

**What to check:**
- [ ] Trigger: Upon request by disclosing party OR expiry/termination of NDA.
- [ ] Scope: Includes copies, notes, extracts, and electronic files.
- [ ] Timeframe: 10–30 days is standard.
- [ ] Certification: Written certification of destruction from authorized officer.
- [ ] Carve-outs: Legal hold / regulatory retention exemption (acceptable). Automated backup retention with enhanced security (acceptable with time limit).

**Red flags:**
- No return/destruction obligation
- No certification requirement
- Carve-out for "reasonably practicable" with no time limit (indefinite retention)

---

### 5. Remedies

**What to check:**
- [ ] Injunctive relief: Receiving party acknowledges that breach may cause irreparable harm and agrees injunctive relief is appropriate (standard — include).
- [ ] Indemnification: Scope reasonable (losses from breach). Not unlimited consequential damages.
- [ ] Liquidated damages: If present, flag for senior review. Pre-agreed amounts can be difficult to negotiate post-breach.
- [ ] Attorney's fees: One-way fee-shifting to disclosing party (negotiate to remove or make mutual).

---

### 6. Governing Law and Jurisdiction

**What to check:**
- [ ] Governing law: Preferred — jurisdiction where your entity is domiciled.
- [ ] Courts: Exclusive jurisdiction in specified courts. Check if counterparty's preferred courts are inconvenient.
- [ ] Arbitration: If present, check institution (ICC/AAA/JAMS), seat, language, number of arbitrators.
- [ ] Cross-border: If parties in different countries, confirm NDA enforceability under local law (especially re: injunctive relief, non-solicitation, non-compete).

---

### 7. Residuals Clause

**What it is:** A residuals clause allows a party to use information retained in unaided human memory (without deliberate memorization) without obligation — effectively allowing "walk-away" knowledge.

**Risk assessment:**

| Residuals Scope | Risk | Action |
|-----------------|------|--------|
| Absent | Low | Acceptable |
| Unaided human memory only | Medium | Acceptable with technical IP carve-out |
| Any retained knowledge (broad) | High | Negotiate to remove or narrow |
| Express right to compete using retained knowledge | Critical | Escalate to GC; likely dealbreaker |

**Counter-position:** "The residuals clause shall not apply to any Confidential Information that constitutes a trade secret under applicable law."

---

### 8. Non-Solicitation and Non-Compete Riders

**Non-Solicitation — review checklist:**
- [ ] Duration: 12–24 months is standard; > 36 months is aggressive.
- [ ] Scope: Specific named employees vs. any employee exposed to CI vs. all employees (escalating scrutiny).
- [ ] Carve-out: General recruitment advertising not targeted at specific individuals (must be present).
- [ ] Enforceability: Check local law (California and some EU jurisdictions restrict non-solicitation).

**Non-Compete — review checklist:**
- [ ] Flag immediately for General Counsel review.
- [ ] Duration: > 12 months is unusual in a standalone NDA context.
- [ ] Geography: Global restriction is likely unenforceable in many jurisdictions.
- [ ] Scope: Must be narrowly tailored to the specific disclosed CI or business purpose.
- [ ] Enforceability: Many US states (California, North Dakota, Minnesota, FTC rule) and EU countries restrict or ban employee non-competes. Business-to-business non-competes have wider enforceability.

---

## Risk Classification and Routing

### Green — Standard Processing (Auto-approve or Associate review)
- Our standard form with no material changes
- Counterparty form with only standard positions on all 12 criteria
- Mutual NDA for a routine vendor evaluation, all terms within market range
- Turnaround: Same day or 24 hours

### Yellow — Contracts Counsel Review Required
- Counterparty's form with 1–3 clauses outside standard range
- Non-standard obligation term or survival period
- Residuals clause present (unaided memory scope)
- Non-solicitation rider present
- Cross-border with unfamiliar governing law
- IP-heavy disclosure scope
- Turnaround: 48 hours

### Red — General Counsel Involvement Required Before Proceeding
- Broad residuals clause or residuals + right to compete
- Non-compete rider of any kind
- Uncapped indemnification or liquidated damages
- Governing law in jurisdiction with poor NDA enforceability
- M&A diligence NDA (transaction materiality)
- Regulated industry context (HIPAA, ITAR, FINRA)
- Party is a known competitor
- Turnaround: 72–96 hours (or as negotiated)

---

## Standard NDA Positions Table

| Clause | Company-Favorable | Market Standard | Counterparty-Favorable |
|--------|-------------------|-----------------|------------------------|
| CI Definition | Narrowly defined; includes oral with written confirmation | Broad but with exclusions | "All information" without exclusions |
| Care standard | Same care as own CI, no less than reasonable care | Reasonable care | Commercially reasonable (weaker) |
| Obligation term | 5 years survival | 3 years survival | 1–2 years survival |
| Return/destruction | 10 days + certification | 30 days + certification | Reasonable efforts, no certification |
| Governing law | Our jurisdiction | Mutual choice | Counterparty's jurisdiction |
| Residuals | Absent | Absent | Unaided memory or broader |
| Non-solicitation | Absent | Absent or 12 months targeted | 24 months, all employees |
| Non-compete | Absent | Absent | Present (any scope) |
| Injunctive relief | Expressly agreed by both parties | Agreed by receiving party | Absent |

---

## Common NDA Red Flags

10 patterns that require immediate escalation or negotiation:

| # | Red Flag | Why It Matters |
|---|----------|----------------|
| 1 | **No mutual confidentiality obligations in an MNDA** — obligations clearly asymmetric despite "mutual" label | Receiving party has no obligations; one-sided risk |
| 2 | **CI definition includes "all information in any form"** without exclusions | Effectively turns casual conversation into an obligation |
| 3 | **Residuals clause with right to compete** — receiving party may use retained knowledge to compete | NDA is effectively unenforceable for competitive purposes |
| 4 | **Non-compete with global geography** — particularly in individual / employment context | Likely unenforceable; signals aggressive counterparty |
| 5 | **No return/destruction obligation** — counterparty can retain CI indefinitely after purpose ends | CI lives forever; exposure never closes |
| 6 | **Obligation term shorter than confidential relationship** — e.g., 1-year NDA for a 3-year project | CI shared late in the project is unprotected at expiry |
| 7 | **No legal compulsion notice carve-out** — receiving party may be required to disclose by court without notice | No ability to seek protective order |
| 8 | **"Authorized disclosures" to subsidiaries without equivalent obligations** — affiliate can receive and not be bound | Effectively neutralizes protection in corporate groups |
| 9 | **Unilateral NDA where mutual is appropriate** — diligence context where both parties are sharing | Our disclosures have no protection |
| 10 | **Unknown signatory authority** — individual signs without evidence of authority to bind entity | NDA may not be enforceable against the company |

---

## Negotiation Playbook

Fallback positions by clause when counterparty pushes back:

| Clause | Our Opening | First Fallback | Final Fallback | Escalate If |
|--------|-------------|----------------|----------------|-------------|
| CI Definition | Precisely defined categories | Add catch-all with written confirmation for oral CI | Accept broad with all four standard exclusions | No exclusions at all |
| Care Standard | Same care as own CI, no less than reasonable | Reasonable care + specific technical measures | Reasonable care only | "Best efforts" — negotiate down |
| Obligation Survival | 5 years | 3 years + trade secret carve-out | 2 years with separate indefinite trade secret clause | < 2 years with no trade secret carve-out |
| Return/Destruction | 10 days + written certification | 30 days + written certification | 30 days + reasonable efforts | No obligation / no certification |
| Residuals | Remove entirely | Unaided human memory only with trade secret carve-out | Unaided human memory only | Broad residuals or right-to-compete |
| Non-Solicitation | Remove | 12 months, named individuals only, general recruitment carve-out | 12 months all exposed personnel with general recruitment carve-out | > 24 months or no general recruitment carve-out |
| Non-Compete | Remove | N/A — escalate to GC | N/A | Any non-compete in NDA context without GC sign-off |

---

## NDA Tracking Template

Maintain this registry for all executed NDAs:

```
NDA REGISTRY ENTRY

Reference:      [NDA-YYYY-NNN]
Status:         [Active | Expired | Terminated]

PARTIES
  Our entity:              [Legal name]
  Counterparty:            [Legal name + jurisdiction of incorporation]
  Counterparty signatory:  [Name + title]
  Our signatory:           [Name + title]

CLASSIFICATION
  Type:                    [Mutual | Unilateral (we receive) | Unilateral (we disclose)]
  Form:                    [Our form | Counterparty form | Negotiated]
  Purpose:                 [M&A diligence | Vendor eval | Partnership | Employment | Research]

DATES
  Date signed:             [YYYY-MM-DD]
  Disclosure period end:   [YYYY-MM-DD]
  Obligation expiry:       [YYYY-MM-DD]
  Trade secret expiry:     [Indefinite | YYYY-MM-DD]
  Return/destroy deadline: [YYYY-MM-DD after expiry]

KEY TERMS
  Governing law:           [Jurisdiction]
  Residuals clause:        [Yes — scope: ___ | No]
  Non-solicitation:        [Yes — duration: ___ | No]
  Non-compete:             [Yes — scope: ___ | No]
  Non-standard terms:      [List any deviations from market standard]

REVIEW HISTORY
  Reviewed by:             [Name]
  Review date:             [YYYY-MM-DD]
  Risk rating:             [Green | Yellow | Red]
  GC approval:             [Name + date, or N/A]

NOTES
  [Any ongoing obligations, renewal triggers, or monitoring notes]
```

---

## Special Considerations

### IP-Heavy Deals (Technology, Pharma, Biotech)

Additional review required beyond standard checklist:

- [ ] Source code, algorithms, formulas, and technical specifications explicitly included in CI definition
- [ ] No implied license granted by disclosure (confirm "disclosure does not confer any rights")
- [ ] Background IP / Foreground IP separation clause if any joint development anticipated
- [ ] Residuals clause explicitly excludes technical trade secrets
- [ ] Return/destruction covers all test environments, copies, and derivative analyses

### Cross-Border NDAs

Additional considerations for multi-jurisdiction agreements:

| Issue | Check |
|-------|-------|
| **Data privacy** | Does CI disclosure constitute personal data transfer? If yes, DPA or SCCs may be required alongside NDA |
| **Enforceability** | Is injunctive relief available in counterparty's jurisdiction? (Some civil law countries require specific performance proceedings) |
| **Translation** | Is a translated version required? Which version controls in case of conflict? |
| **Non-compete enforceability** | Many EU countries, Canada, and US states restrict or prohibit non-competes even for business-to-business agreements |
| **Export control** | Does shared information include export-controlled technology (ITAR, EAR, EU dual-use)? If yes, separate export control provisions required |

### Regulated Industry Considerations

| Industry | Additional Requirements |
|----------|------------------------|
| **Healthcare / HIPAA** | If CI includes PHI: HIPAA BAA required in addition to NDA; NDA alone is insufficient |
| **Financial Services** | Check applicable securities laws on material non-public information (MNPI); may require insider trading policy acknowledgment |
| **Defense / Government** | ITAR / EAR controls may apply; government may require security clearances; standard NDA may be insufficient |
| **Pharma / Biotech** | Clinical trial data subject to FDA confidentiality requirements; patent prosecution privilege considerations |
