# Financial Modeling — Knowledge Pack

**Version**: 1.0.0
**Owner**: 📊 FP&A Analyst
**Last updated**: 2026-04-11
**Consumers**: any Finance Team skill that reviews, audits, or produces financial models; `/compliance-audit` for financial-control compliance; future `/budget-variance-review` (not yet scoped)
**Purpose**: a 7-dimension rubric for scoring financial models against auditability criteria. Pack deliverable, not a skill. Original authoring, no WSP/CFI/McKinsey content lifts.

---

## 1. Purpose and Scope

This pack is a rubric. It scores an existing financial model — a valuation, a forecast, a pricing model, a deal model, a unit-economics workbook — against seven dimensions of auditability. The output is a 1-5 score per dimension plus a pass/fail verdict against a defined threshold. The goal is to answer one question: "If an auditor, board member, or careful reviewer sat down with this model tomorrow, could they reconstruct how every output was produced, challenge any assumption, and arrive at a defensible judgment about the model's integrity?"

What the rubric does NOT do: it does not replace substantive model review by a qualified FP&A human; it does not score the model's predictive accuracy (a model can be rigorously auditable and still be wrong about the world); it does not enforce a particular structural choice (some models should be three-statement, some should be driver-based cash projections, some should be Monte Carlo simulations — the rubric is structure-agnostic); and it does not score the model's presentation quality, only its auditability.

**Explicit scope-out: refresh cadence.** How often a model is updated, who owns the refresh, and what triggers a refresh are governance concerns, not rubric dimensions. Refresh cadence is covered in the `operations-playbooks` governance section. A model can score 5/5 across all seven dimensions and still be stale if nobody refreshes it — that's a governance failure, not a model-quality failure, and conflating the two produces a rubric that tries to score two unrelated things.

---

## 2. The Seven Dimensions

### Dimension 1: Driver Transparency

**Definition**: every output number in the model can be traced back, through a visible chain of formulas, to a named driver. A driver is an input the model treats as an independent variable — revenue growth rate, churn, gross margin, CAC, discount rate, headcount ramp. Drivers are calibrated to a real observable (actual historical data, a benchmark, a negotiated contract, an explicit assumption with source).

**What it measures**: whether a reviewer can point at any cell in the output and ask "where does this come from?" and get a traceable answer that terminates in a named, documented driver — not in a hardcoded constant or an opaque aggregate formula.

**Scoring anchors**:
- **1 (absent)** — output numbers are hardcoded, or formulas terminate in constants with no linked driver. Reviewer asks "where does the $4.2M come from?" and the answer is "that's what was in last year's model." Driver names do not exist or are inconsistent across sheets.
- **3 (partial/manual)** — a driver sheet exists and covers the major inputs, but some outputs bypass the driver sheet (e.g., regional revenue has its own hardcoded overrides). Driver names exist but are not always used consistently. Tracing a number requires reading through 3-5 formula hops.
- **5 (rigorous/automated)** — every input is on a named driver sheet with a single source of truth. Every output formula references drivers by name. A driver tree can be rendered automatically or inspected cell-by-cell. Constants that appear in formulas (e.g., 0.21 for the US corporate tax rate) are themselves named drivers on the driver sheet.

**Common failure modes at levels 1-2**: constants inline in formulas; "fudge factor" cells with no source; drivers copied across sheets with manual edits; the same economic concept named differently in two places (e.g., "churn" on one sheet, "attrition" on another) with slightly different values.

**Typical improvement path from 3 → 5**: (a) consolidate all inputs onto a single driver sheet with named ranges; (b) replace inline constants with driver references; (c) add a driver index that maps every driver to the outputs it feeds; (d) run a "find all hardcoded numbers in formulas" audit and convert each one to a named driver.

---

### Dimension 2: Scenario Flex

**Definition**: the model's structure can support scenario variation (base / upside / downside / stress) without rewriting the model. Scenarios are declared explicitly, named consistently, and driven by a switch or scenario picker — not built as separate sheets or separate files.

**What it measures**: whether a reviewer can add a fourth scenario, or modify an existing scenario, without re-engineering the model's structure. This tests whether the model was built with scenarios in mind or retrofitted with scenarios late.

**Scoring anchors**:
- **1 (absent)** — no scenarios at all, or scenarios implemented as separate copies of the entire model ("MyModel_Base.xlsx", "MyModel_Downside.xlsx"). Changing a driver in one copy does not propagate. Comparing scenarios requires manual reconciliation.
- **3 (partial/manual)** — a scenario switch exists and drives the top-line outputs, but some sections (COGS breakdown, working-capital schedule) still hardcode a single case. Adding a new scenario requires editing those sections by hand. Scenario names exist but are not used consistently across sheets.
- **5 (rigorous/automated)** — a single scenario picker (INDEX/MATCH, CHOOSE, or equivalent) drives every downstream calculation. Adding a fourth scenario is a matter of adding one column to the scenario table. All outputs automatically reflect the active scenario. Scenario-specific outputs (e.g., a downside cash-runway metric) are computed, not hardcoded.

**Common failure modes at levels 1-2**: scenarios as separate sheets; scenarios as separate files; hardcoded "downside" cells that don't respond to driver changes; scenario names that drift between sheets; copy-paste-modify as the scenario-creation pattern.

**Typical improvement path from 3 → 5**: (a) declare the scenario table as a single source of truth; (b) wire the scenario picker into every driver that varies by case; (c) remove duplicated sheets; (d) add a "scenarios cover all drivers" audit that flags any driver not present in the scenario table.

---

### Dimension 3: Audit Trail

**Definition**: changes to the model are tracked — who changed what, when, and why. Version history exists at the file level and ideally at the formula level. A reviewer can reconstruct the model's evolution and identify when a specific number changed.

**What it measures**: whether the model has the institutional memory to answer "this number was $3.8M last week, why is it $4.1M now?"

**Scoring anchors**:
- **1 (absent)** — no version control. Files named "Model_v7_final_FINAL_v2.xlsx". No change log. No way to identify when a number changed or who changed it. "Undo" is the only audit trail and it dies when the file closes.
- **3 (partial/manual)** — file-level versioning exists (Git, SharePoint, Google Drive history). A change log is maintained but irregularly. Major revisions have dated version numbers. Reviewer can answer "what changed between v4 and v5" by diffing files, but cell-level attribution requires manual investigation.
- **5 (rigorous/automated)** — every revision is tracked with author, timestamp, and change reason. Cell-level or range-level audit trail available (either via a modeling platform that tracks this natively, or a disciplined change log that lists every modified range per revision). A reviewer can query "when did the WACC change to 9.5%, who changed it, and why" and get an answer in under two minutes.

**Common failure modes at levels 1-2**: no versioning; versioning via filename; "final" files that keep getting revised; change log abandoned after the first three entries; shared drive with no history retention.

**Typical improvement path from 3 → 5**: (a) move the model into version control (Git for open-format models, a platform with native history for Excel); (b) commit per change with a meaningful message; (c) adopt a change-log tab inside the model that lists revisions; (d) require a change-log entry for any driver modification above a threshold.

---

### Dimension 4: Source Linking

**Definition**: every input data point is linked to a source — a document, a database pull, a regulator filing, a contract, a prior model output, a named expert judgment. A reviewer can click (or trace) from a number to its origin.

**What it measures**: whether the model's inputs are grounded in verifiable external reality or are floating assertions.

**Scoring anchors**:
- **1 (absent)** — inputs have no sources. Numbers appear without attribution. Reviewer asks "where did the 24% gross margin come from?" and the answer is "that's the assumption." No traceability back to financials, contracts, benchmarks, or expert input.
- **3 (partial/manual)** — major inputs have sources cited in a comment or a separate tab. Citations are inconsistent (some have URLs, some have document names, some just say "per management"). Traceability requires hunting through comments and external files.
- **5 (rigorous/automated)** — every input has a structured source record: source type (filing, contract, database, expert judgment), source identifier (URL, document ID, contract number, interview date), retrieval date, and confidence level. A reviewer can pull up the source record for any driver in under one minute. For live-data inputs (e.g., a database pull), the pull itself is reproducible.

**Common failure modes at levels 1-2**: sourceless inputs; "per management" as a universal citation; URLs that 404; document names without version; benchmarks cited without year; expert judgments without attribution.

**Typical improvement path from 3 → 5**: (a) add a source column next to every driver; (b) standardize source types (five categories is enough); (c) for live-data inputs, script the pull and retain the script with the model; (d) add a quarterly "source freshness" audit.

---

### Dimension 5: Assumption Documentation

**Definition**: assumptions are captured separately from calculations, with an author, a date, a confidence level, and a review cadence. Assumptions are treated as first-class objects in the model, not as opinions buried in formulas.

**What it measures**: whether the model makes its judgment calls explicit so they can be challenged, not hidden so they can't.

**Scoring anchors**:
- **1 (absent)** — assumptions are buried in formulas or comments. No separation between "facts" (inputs with sources) and "judgments" (assumptions the modeler made). No author, no date, no confidence level. Reviewer cannot tell which numbers are negotiable and which are observations.
- **3 (partial/manual)** — an assumptions tab exists and lists the major judgments with brief rationale. Author and date are inconsistent. Confidence level is implicit ("we think" vs "we know"). Review cadence is informal.
- **5 (rigorous/automated)** — every assumption is a record with: a unique ID, a plain-English statement, author, date of last review, confidence level (named scale — e.g., high / medium / low, or a 1-5 scale with anchors), source of the judgment (who was consulted), linked drivers, and a review cadence. Assumptions are distinct from facts in the model's structure. The rubric can query "show me all low-confidence assumptions that affect the downside case."

**Common failure modes at levels 1-2**: assumptions as comments; assumptions mixed with facts; no confidence level; "expert judgment" cited as a source without the expert named; assumptions that never get reviewed once entered; assumptions cloned across scenarios with no notion that they might vary.

**Typical improvement path from 3 → 5**: (a) create an assumptions registry tab; (b) migrate buried assumptions into the registry; (c) assign an author and confidence level to each; (d) set a quarterly review cadence; (e) link each assumption to the drivers it affects.

---

### Dimension 6: Internal Consistency / Foot-and-Tie (NEW — replaces refresh cadence)

**Definition**: cross-sheet references hold, totals tie across views, and the three statements (if present) agree. Monthly rolls up to quarterly, quarterly rolls up to annual, and nothing changes when you press F9 twice. Rounding is handled consistently, not introduced at random points.

**What it measures**: whether the model is self-consistent — whether the internal math actually adds up before you even question whether the assumptions are right.

**Scoring anchors**:
- **1 (absent)** — cross-sheet references are broken or point at the wrong ranges. Totals don't tie (annual revenue on the summary tab ≠ sum of quarterly revenue on the forecast tab). Balance sheet doesn't balance. Cash flow doesn't reconcile to the ending cash balance on the balance sheet. Pressing F9 produces different results on successive passes (circular references or volatile functions with no iterative-calc rules).
- **3 (partial/manual)** — totals tie at the top-line level but drift at sub-totals (e.g., segment revenue sums to total revenue but regional breakdowns don't match segment breakdowns). Balance sheet balances but the balancing plug line is "plug" not a real account. Rounding introduces small discrepancies that a reviewer has to manually verify don't mask real errors.
- **5 (rigorous/automated)** — every cross-sheet total reconciles automatically with a visible check cell that reads "OK" or flags a discrepancy. Balance sheet balances without a plug. Cash flow statement derives from and reconciles to the balance sheet movement. Monthly → quarterly → annual rolls are built by formula, not pasted. The model passes a "press F9 twice, nothing changes" test. Rounding is handled at a single documented point, not scattered.

**Common failure modes at levels 1-2**: manual roll-ups; pasted (not formula-linked) aggregates; a "plug" account absorbing balance-sheet discrepancies; circular references masked by iterative calc without documentation; rounding inconsistencies; inconsistent date handling (some sheets use calendar, some use fiscal).

**Typical improvement path from 3 → 5**: (a) add check cells at every cross-sheet aggregate; (b) replace paste-values aggregates with formula links; (c) eliminate plug accounts — if the balance sheet doesn't balance, find the error, don't plug it; (d) document rounding conventions; (e) enforce a single date convention.

---

### Dimension 7: Sensitivity Realism (NEW)

**Definition**: sensitivity ranges reflect realistic plausibility, not the model builder's preferred answer. Ranges are named by a rationale (empirical basis, expert judgment, regulatory requirement) and cover the 80% confidence interval for each driver, not a cosmetic ±10%.

**What it measures**: whether the sensitivity analysis stress-tests the model or decorates it.

**Scoring anchors**:
- **1 (absent)** — no sensitivity analysis, or sensitivity ranges are arbitrary (±5%, ±10% applied to every driver regardless of actual volatility). Ranges are chosen to produce a desired output ("what range makes the IRR still look positive?") rather than to reflect plausible reality. Sensitivity tables exist but don't drive any decision.
- **3 (partial/manual)** — sensitivity ranges exist for major drivers, chosen with some rationale. Ranges are documented but not all are empirically grounded. Coverage is incomplete (some drivers have ranges, others don't). Sensitivity tables exist and are referenced in commentary but don't flag any decision thresholds automatically.
- **5 (rigorous/automated)** — every material driver has a sensitivity range derived from a named basis (historical volatility, expert confidence interval, regulator-mandated range, peer benchmark spread). Ranges cover the 80% confidence interval at minimum. Sensitivity is tested at the output level that matters (IRR, NPV, cash runway, gross margin) and decision thresholds are marked ("below this NPV, the deal doesn't work"). Tornado charts or equivalent rank drivers by sensitivity impact. The analysis is honest about where the model is fragile.

**Common failure modes at levels 1-2**: ±10% as a universal range; sensitivity tuned to produce an acceptable output; cosmetic sensitivity that doesn't change with the scenario; no decision thresholds; no ranking of which drivers matter most; sensitivity on drivers that don't actually vary (tax rate) and none on drivers that do (churn, win rate).

**Typical improvement path from 3 → 5**: (a) list material drivers and classify each by volatility source; (b) derive a defensible range for each (empirical, expert, regulatory); (c) test sensitivity at the decision-relevant output; (d) rank drivers by impact; (e) state the fragility honestly — "this model is 80% driven by win-rate assumption; if win rate is below 18%, the deal doesn't clear hurdle."

---

## 3. Scoring Procedure

1. **Read the model end-to-end once.** Do not score on first pass. Understand the structure, the outputs, the driver layout, the scenario approach.
2. **Score each dimension independently, 1-5.** Use the anchors. Do not average in your head — commit to a number.
3. **Record evidence per score.** For each dimension, capture: one piece of evidence that justified the score (a specific formula, a sheet reference, a screenshot of a driver tree, a quote from the change log). Without evidence, the score is opinion, not an audit.
4. **Compute the aggregate.** Aggregate = mean of the 7 dimension scores. NOT sum. (A 35-point maximum is cognitively misleading; 1-5 with mean 1-5 is the same mental model as the anchor scale, so reviewers don't have to do two conversions.)
5. **Apply the pass threshold.** The model passes the "model-is-auditable" threshold if and only if:
   - **Aggregate ≥ 3.5**, AND
   - **No single dimension scores below 3**.

   The second condition exists because a model with a 1 on audit trail and 5 on everything else still has a fatal weakness: you can't tell when numbers changed. One gating dimension at 1 is not averaged away.
6. **Write the scorecard.** One page: per-dimension scores with one-line rationales, aggregate, pass/fail, and a prioritized fix list for any dimension below 4.

---

## 4. Worked Example — AXIA Bank Discount Deal Model (Synthetic Scoring)

**Context**: AXIA is negotiating an enterprise deal with Bank Discount. The deal is under active negotiation as of 2026-04. The finance team has a deal model covering license revenue, implementation fees, ongoing services, and the discount structure. The model informs the pricing committee's walk-away point.

**Caveat**: I do not have access to the real model. The scoring below is a synthetic exercise that reflects the common patterns of a deal model built under time pressure by a mid-stage company. It is intended to show how the rubric reads a typical financial model, not to make any claim about AXIA's actual model. All numbers in the rationales are qualitative or `[TBD]`.

### Per-dimension scoring

**1. Driver transparency — 4/5**
Deal models at this stage typically have a clean driver sheet (seats, ACV per seat, discount percentage, implementation effort, services rates). AXIA's model probably names these drivers clearly because the deal has been socialized across commercial and finance. Likely gap: one or two hardcoded "override" cells where the commercial team plugged a negotiated number that doesn't flow from a driver. Rationale for 4, not 5: the override cells are an easy slip under negotiation pressure.

**2. Scenario flex — 3/5**
The model almost certainly has base/upside/downside on revenue but may have only a single case on implementation cost. Adding a "what if the bank extends the discount to a second bank" scenario probably requires restructure, not a switch. Rationale for 3: scenarios exist for the commercially visible axis (price) but not for the cost axis.

**3. Audit trail — 3/5**
File-level versioning exists (Drive history or Git, depending on the team). A change log at the model level probably doesn't. When the discount percentage changed three times during negotiation, the reasons are in Slack threads and emails, not in the model. Rationale for 3: versioning yes, cell-level attribution no.

**4. Source linking — 4/5**
Contract-driven inputs (seats, term, discount) have sources in the draft contract. Benchmarks (market pricing for this segment) probably cite a CI report or a competitive-analysis doc. Rationale for 4, not 5: the implementation-effort estimate is probably "per Asaf," without the methodology that produced it.

**5. Assumption documentation — 3/5**
The major assumptions (discount percentage is acceptable because of reference-customer value, services rates are at standard) are probably captured in commentary in the deal memo, not in a structured assumptions registry inside the model. Rationale for 3: assumptions exist and are visible in the deal memo, but not structured inside the model and not tagged with confidence level.

**6. Internal consistency / foot-and-tie — 4/5**
Deal models are usually small enough to foot-and-tie cleanly on first build. Likely gap: when the discount was revised late in negotiation, the summary tab was updated but one of the sub-tabs (e.g., services revenue waterfall) may not have been relinked. Rationale for 4: high base case, small risk of a late-stage paste-over.

**7. Sensitivity realism — 2/5**
This is the most likely weak point. A deal under active negotiation is modeled to support the pricing ask, not to stress-test it. Sensitivity is probably a ±10% band on revenue with no derivation. Sensitivity on win probability (will the bank actually sign) is almost certainly absent because the model assumes the deal closes. Rationale for 2: sensitivity exists but is cosmetic, not grounded in empirical volatility.

### Aggregate and verdict

Aggregate = (4 + 3 + 3 + 4 + 3 + 4 + 2) / 7 ≈ **3.29**

**Verdict: FAIL against the 3.5 / no-dimension-below-3 threshold.**

The model fails on two counts: aggregate below 3.5, and one dimension (sensitivity realism) below 3.

### Honest assessment of why the model is weak where it's weak

A deal model built under negotiation pressure optimizes for the decision the sales team needs to make (accept/reject at this price) and under-invests in the decision the board needs to make (is this deal a net positive given uncertainty). That's not a failure of the model builder; it's a failure of the governance around when to stress-test a deal model.

### Prioritized improvement path

If the team has `[TBD]` hours to raise the model above the threshold, spend them in this order:

1. **Sensitivity realism (2 → 3)**: add a sensitivity table on win probability (even if the team says "we'll close it," a plausible range on close-probability tests whether the deal is still a net positive if commercial optimism is wrong). This alone moves the aggregate above the passing line.
2. **Scenario flex (3 → 4)**: add a switch for "deal scope" covering the three discount tiers currently in negotiation, so the committee can toggle without rebuilding.
3. **Assumption documentation (3 → 4)**: migrate the deal-memo assumptions into an assumptions tab inside the model with author, date, confidence. This makes the next deal-model review faster.

After these three fixes: aggregate ≈ 3.71 with no dimension below 3. **Model passes.**

---

## 5. Anti-Patterns

Each anti-pattern describes a common financial-model failure mode, why the rubric catches it, and how to fix it.

### 5.1 Hardcoded numbers in formulas
**What it looks like**: `=B12*1.05+4200000` in the middle of a revenue formula.
**Why it's a failure**: the 1.05 and the 4,200,000 are drivers hiding in plain sight. Change them, and nobody notices; question them, and nobody can defend them.
**How the rubric catches it**: Dimension 1 (Driver Transparency) score 1 or 2.
**How to fix**: lift every constant to the driver sheet as a named driver. The formula becomes `=B12*(1+growth_rate)+fixed_cost_base`.

### 5.2 Circular references masking logic errors
**What it looks like**: the model uses iterative calculation mode (Excel will "solve" circular references by repeated recalculation). This is legitimate for a few named use cases (interest-on-debt-on-interest, tax-on-pretax-income-after-interest). It is illegitimate when it hides an error.
**Why it's a failure**: iterative calc will converge on any stable answer, not necessarily the right one. A logic error can hide inside a circular reference and produce plausible-looking numbers.
**How the rubric catches it**: Dimension 6 (Internal Consistency) score 1 or 2. The "press F9 twice" test will reveal non-convergence or unstable behavior.
**How to fix**: document every intentional circular reference with a note in the model. For unintentional ones, refactor — break the circularity by moving the dependent calculation into a separate schedule.

### 5.3 Scenarios built as separate sheets
**What it looks like**: "Base_Case", "Upside_Case", "Downside_Case" tabs, each with its own copy of the model.
**Why it's a failure**: structural flex is zero. A change to the model must be made three times. Adding a fourth case means cloning and editing another tab. Drift between sheets is inevitable.
**How the rubric catches it**: Dimension 2 (Scenario Flex) score 1 or 2.
**How to fix**: collapse the three sheets into one driven by a scenario picker. The scenario table lists the cases; the model reads the active case from a single cell.

### 5.4 Unversioned copies
**What it looks like**: `Model_v7_final_FINAL_v2_reviewed.xlsx` in a shared drive.
**Why it's a failure**: no audit trail. You cannot answer "what changed between revisions" without diffing files by hand.
**How the rubric catches it**: Dimension 3 (Audit Trail) score 1.
**How to fix**: move the model into version control with commit messages.

### 5.5 Assumptions in comments
**What it looks like**: a cell with a yellow highlight and a comment that reads "assuming 20% growth per Mark."
**Why it's a failure**: the assumption is invisible to anyone who isn't hovering over the right cell. It cannot be queried, reviewed on a cadence, or tagged with confidence.
**How the rubric catches it**: Dimension 5 (Assumption Documentation) score 1 or 2.
**How to fix**: move the assumption to an assumptions registry tab with ID, author, date, confidence level, source, and linked drivers.

### 5.6 Foot-and-tie broken by rounding
**What it looks like**: the monthly revenue totals to a number that differs from the annual revenue cell by a small amount, because rounding was applied inconsistently.
**Why it's a failure**: the discrepancy is trivial, but the reviewer has to verify that's the only discrepancy and not the tip of a real error. Trust in the model erodes.
**How the rubric catches it**: Dimension 6 (Internal Consistency) score 2 or 3.
**How to fix**: apply rounding at a single documented point (typically the presentation layer, not the calculation layer). Let the calculation layer carry full precision.

### 5.7 Sensitivity tables with false precision
**What it looks like**: a sensitivity table showing IRR at multiple decimal places for cosmetic ±5% / ±10% revenue variations.
**Why it's a failure**: the fine-grained increments imply a precision that doesn't exist, and the narrow range is cosmetic (if real volatility is much wider, the table lies about the risk).
**How the rubric catches it**: Dimension 7 (Sensitivity Realism) score 2.
**How to fix**: derive ranges from empirical volatility (historical data, peer benchmarks) or expert confidence intervals. State the basis. Use fewer increments at wider ranges that reflect real uncertainty.

### 5.8 "The model said so" without driver traceability
**What it looks like**: a deck slide asserts an IRR number and the model spits it out, but nobody can point to the three drivers that got you there.
**Why it's a failure**: the model becomes oracular. Decisions are made based on outputs that cannot be interrogated.
**How the rubric catches it**: Dimension 1 (Driver Transparency) and Dimension 7 (Sensitivity Realism) both low.
**How to fix**: produce a driver-ranking for every headline output. "IRR is X%, of which most variance is driven by revenue growth assumption, then CAC, then terminal multiple."

### 5.9 Plug accounts on the balance sheet
**What it looks like**: a balance-sheet line named "plug" or "reconciliation adjustment" that absorbs whatever is needed to make the statement balance.
**Why it's a failure**: the plug is hiding an error, not fixing one. The model is not self-consistent; it is self-disguising.
**How the rubric catches it**: Dimension 6 (Internal Consistency) score 1 or 2.
**How to fix**: find the error. A balance sheet that does not balance has an actual bug — a misclassified account, a missed entry, a timing mismatch. Fix it. Do not plug.

### 5.10 Driver names that drift between sheets
**What it looks like**: "churn" on the revenue tab, "attrition" on the customer tab, "logo loss" on the summary tab — three names for the same concept with three slightly different values.
**Why it's a failure**: the model has three sources of truth for one driver. A reviewer cannot tell which is authoritative.
**How the rubric catches it**: Dimension 1 (Driver Transparency) score 2 or 3.
**How to fix**: pick one name, one definition, one cell. Every reference reads from that cell.

---

## 6. Integration with C2.4 Agent-Ready SOP Schema

Financial-control SOPs (month-end close, journal-entry review, account reconciliation, flux analysis) use Dimension 6 (Internal Consistency / Foot-and-Tie) as their `verification_test`. An SOP step that reads "confirm monthly rolls up to quarterly" is failing without a verification_test; the rubric supplies it: "Dimension 6 check cells at every cross-sheet aggregate, pass = all check cells OK."

Pointer: `Extension Teams/reference/knowledge/agent-ready-sop-schema.md` (C2.4 deliverable, when published).

---

## 7. Integration with `/compliance-audit`

When a compliance framework requires financial reporting controls (SOX ICFR, SOC 2 CC6, ISO 27001 A.8, etc.), `/compliance-audit` needs evidence that financial models used in reporting are auditable. The rubric produces exactly that evidence: per-model scorecards that an auditor can review, with per-dimension evidence records.

**Boundary (non-negotiable)**: the rubric does NOT attest compliance. It produces the evidence an auditor needs. The auditor — a licensed CPA, a SOC 2 assessor, a SOX PMO lead — interprets the evidence against the framework's requirements and forms the attestation. The rubric is a tool; the attestation is a human judgment.

Pointer: `compliance-audit` skill definition and `compliance-frameworks.md` knowledge pack.

---

## 8. Refresh Cadence Note

Refresh cadence is **NOT a rubric dimension**. How often a model is updated, who owns the refresh, and what triggers a refresh are governance concerns. A model can score 5/5 across all seven dimensions and still be stale if nobody refreshes it; that is a governance failure, not a model-quality failure.

For refresh cadence guidance, see the governance section of `operations-playbooks.md` (once published) or the current `financial-governance.md` pack. Topics covered there: refresh triggers (material transaction, period-end, quarterly review, annual budget, regulatory change), refresh ownership (named owner per model), refresh SLA (how fast a model must be current after a trigger), and refresh audit (who verifies the refresh happened).

---

## 9. Maintenance Cadence

**Annual rubric review** — the 7-dimension structure, the anchors, and the threshold are reviewed once a year by the owner (📊 FP&A Analyst) with input from consumers.

**Earlier-trigger reviews** — the rubric is reviewed off-cycle if any of the following occur:
- **Regulator guidance change** — SEC interpretive release affecting financial modeling practice, PCAOB auditing standard revision, or equivalent.
- **Standard-body revision** — IFRS or GAAP standards that materially change how financial statements are constructed in ways that touch the auditability dimensions.
- **Material model failure discovery** — a financial model scored as "passing" by this rubric is later revealed to have a material error that the rubric should have caught. Triggers a post-mortem and possible rubric revision.

**Version bumps**: patch (typo, clarification), minor (new anti-pattern, refined anchor), major (new dimension, changed threshold, retired dimension).

---

## 10. References (Pointer-Only)

**Public, citable**:
- **SEC financial reporting guidance** — sec.gov Division of Corporation Finance interpretive releases and C&DIs. Used as source of truth for US public-company reporting requirements.
- **PCAOB auditing standards** — pcaobus.org AS 1000-series. Used for external-auditor expectations around financial-statement assertions.
- **IFRS Foundation resources** — ifrs.org. Standard-setter for non-US GAAP financial reporting.
- **FASB resources** — fasb.org. Standard-setter for US GAAP.
- **Damodaran online corporate finance** — pages.stern.nyu.edu/~adamodar/. Existence proof that driver-based valuation is a mature discipline.

**Existence proofs only (NOT content sources)**:
- **Wall Street Prep** — wallstreetprep.com. Training organization. Publishes modeling best-practice guides. Not content-sourced for this pack.
- **Corporate Finance Institute (CFI)** — corporatefinanceinstitute.com. Training organization. Not content-sourced.
- **Training The Street** — trainingthestreet.com. Training organization. Not content-sourced.
- **Koller, Goedhart, Wessels — "Valuation: Measuring and Managing the Value of Companies"** (McKinsey, current edition). Industry-standard valuation reference. Not content-sourced for this pack; cited as existence proof that structured auditability is an established professional practice.

All dimensions, anchors, anti-patterns, and the worked example in this pack are first-principles authoring by the owner. No content is lifted from the sources above.

---

**End of Financial Modeling Knowledge Pack v1.0.0**
