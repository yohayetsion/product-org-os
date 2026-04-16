---
name: comp-benchmark
description: Public-source compensation benchmarking via SOC code mapping with jurisdiction-aware pay-transparency compliance. Drafting and triage aid, not HR or employment-law advice.
argument-hint: --role NAME --jurisdiction CODE [--seniority LEVEL] [--geography METRO]
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: compensation
  skill_type: task-capability
  owner: compensation-analyst
  primary_consumers:
  - ext-hr
  - job-description-generator
  - interview-guide
  sensitive: true
inherits_pack: hr-ai-governance
---
# /comp-benchmark

## Purpose

`/comp-benchmark` produces a public-source compensation reference grid for a role by mapping the role to a Standard Occupational Classification (SOC) code, querying whitelisted public wage sources (BLS OEWS, BLS QCEW, OPM, O*NET, US Census ACS, state/city pay-transparency disclosures, municipal pay schedules), applying documented geography and seniority adjustments, and checking jurisdiction pay-transparency obligations. It produces a **market reference grid + methodology worksheet**, not a recommended offer. It is a **drafting and triage aid**, not HR advice, not employment-law advice, not pay equity analysis.

What it IS: a structured first pass that produces a market reference grid (10th / 25th / 50th / 75th / 90th percentile base pay bands) a human compensation analyst or HR leader can review, interrogate, and own, with every source, SOC code, adjustment factor, and data quality flag surfaced explicitly.

What it is NOT: a pay equity audit (see hard-scoped-out section below and future `/pay-equity-audit`), a recommended offer, an individual offer construction tool, an internal equity analysis, a retention risk assessment, a variable-comp modeler (bonus / equity / commission), or a substitute for employment counsel on jurisdiction-specific pay-transparency obligations.

This skill is governed by `hr-ai-governance` pack v1.0.1. Every benchmark run inherits the proxy register (Section 3.2), audit log schema (Section 4.1), jurisdiction matrix (Section 8.1), and review cadence (Section 11.1 subsequent-similar 72h) from the pack. See the Pack Inheritance section below for the exact dependency map.

---

## When to Use

Invoke `/comp-benchmark` when you need to:

- Open a new role and build a market reference grid before setting an internal comp band
- Refresh an existing comp band during annual review using current public data
- Check jurisdictional exposure when expanding a role into a new state / city / country with pay-transparency rules
- Provide competitive-offer context (public-data reference) for an open requisition
- Feed a reference grid into `/job-description-generator` for a jurisdiction that requires pay-range-on-posting

## When NOT to Use

Do NOT use `/comp-benchmark` when:

- You need a **pay equity audit** — out of scope, HARD block; use `/pay-equity-audit` (future phase, requires attorney-client privilege and documented `@employment-counsel` engagement)
- You need an individual offer (base + bonus + equity + sign-on) — that's a hiring manager + HR leadership decision involving internal equity, capability differentiation, and budget, not a market data pull
- You need internal equity analysis (existing team bands vs. new hire) — out of scope, separate workflow with confidential HR leadership
- You need retention risk assessment for a specific individual — out of scope, confidential HR
- You need variable compensation modeling (bonus targets, equity refresh math, commission plans) — out of scope, separate future skill
- You need market data from a vendor survey (Radford, Mercer, Willis Towers Watson, Payscale, Salary.com, Glassdoor, Levels.fyi, H1B wage DB) — deliberately excluded; the skill's entire point is public-source-only discipline
- You need a legal opinion on whether a specific pay-transparency obligation applies — use `@employment-counsel`

The skill deliberately sits UPSTREAM of `/job-description-generator` (the grid feeds the JD's pay range when pay transparency applies) and is OUT OF SCOPE for pay equity (a separate privileged workflow).

---

## Source Whitelist (MANDATORY)

This is the complete list of sources `/comp-benchmark` is permitted to use. Any source not on this list is a quality gate failure. The whitelist discipline is load-bearing: it is the skill's core constraint, adopted specifically to prevent vendor-survey leakage that would misrepresent the skill's data provenance.

| # | Source | URL | Used for |
|---|---|---|---|
| 1 | **BLS OEWS** (Occupational Employment and Wage Statistics) | https://www.bls.gov/oes/ | Primary anchor. SOC-coded, federally maintained, annual updates. Wage distribution (10th / 25th / 50th / 75th / 90th percentile) by SOC + geography (national, state, MSA, non-metropolitan area). This is the backbone of every reference grid. |
| 2 | **BLS QCEW** (Quarterly Census of Employment and Wages) | https://www.bls.gov/cew/ | Industry + geography granularity. Used when OEWS coverage is thin at the target geography; QCEW gives employer-count and average-wage context by NAICS industry + county. |
| 3 | **BLS ECI** (Employment Cost Index) | https://www.bls.gov/eci/ | Cost-of-labor adjustment factor when geography granularity mismatches (e.g., target metro has no SOC-level OEWS data; use ECI metro series to adjust a national wage). |
| 4 | **OPM federal pay tables** (General Schedule + Special Pay Systems) | https://www.opm.gov/policy-data-oversight/pay-leave/salaries-wages/ | Clean reference for federal-equivalent roles (GS grades, locality pay areas). Useful for government-adjacent roles and as a sanity check for public-sector titles. |
| 5 | **O*NET OnLine** | https://www.onetonline.org/ | Occupational characteristics and SOC crosswalks. Primary tool when role title is ambiguous and a SOC code must be chosen from multiple candidates. Every SOC is linked to tasks, knowledge areas, and related SOCs. |
| 6 | **US Census ACS** (American Community Survey) | https://www.census.gov/programs-surveys/acs | Occupational wage data at metro / county granularity. Used for geography adjustment when BLS OEWS coverage is absent at the target metro level. ACS 5-year estimates are the workhorse; 1-year estimates only for large metros. |
| 7 | **State / city pay-transparency job board disclosures** | (per-jurisdiction; see jurisdiction section below) | Direct observed pay ranges from posted jobs in jurisdictions that require pay-range-on-posting: NY, CO, WA, CA, HI, RI, IL, CT, MD, DC, plus EU member states that have transposed Directive 2023/970. These are the most current market data available and the only market data the skill treats as direct evidence (vs. BLS survey inference). |
| 8 | **Municipal pay scale disclosures** | (per-municipality, e.g., NYC municipal pay schedules; SF city employee pay; state university system pay scales) | City and state employee pay schedules where published. Useful for public-sector and public-sector-adjacent roles, and as ground-truth calibration for private-sector grids in the same metro. |

**Explicitly EXCLUDED (any appearance in a run is a quality gate failure):**

Radford, Mercer, Willis Towers Watson (WTW), Payscale, Salary.com, Glassdoor, Levels.fyi, H1B Wage Database, Comparably, Indeed Salary, Built In, LinkedIn Salary Insights, any other vendor compensation survey, any scraped job board data, any "what I've seen at similar companies" recollection, any "industry knowledge" not tied to one of the eight whitelisted sources.

The H1B Wage Database is specifically called out because it is free and public but has known systematic bias (selection effect: only visa-sponsored roles, skewed toward tech, skewed toward larger employers) that makes it unsafe as a general reference. It is deliberately excluded.

Every source used in a run MUST be cited by name, URL, date accessed, SOC code queried, and geography queried in the methodology worksheet.

---

## Required Inputs

The skill MUST collect the following before producing output. If any required input is missing, it asks the user rather than guessing.

| Input | Required | Example |
|---|---|---|
| Role name / working title | Yes | "Customer Success Lead" / "Senior Backend Engineer" / "Payroll Specialist" |
| Jurisdiction | Yes | `US-DE`, `US-NYC`, `US-CA`, `US-CO`, `US-WA`, `US-IL`, `EU-DE`, `UK`, `IL` |
| Seniority level | Yes | Junior / IC2 / IC3 / IC4 / IC5 / Lead / Manager / Senior Manager / Director |
| Target geography | Yes | Metro area (MSA), state, country, or "remote-national" |
| Existing comp band (to validate) | No | `$130,000-$170,000` base — the skill validates against public data without revealing the internal number outside the audit trail |
| Anonymized internal range | No | For calibration; treated as context, never mixed into the public-data grid |
| Industry | If known (helps QCEW query) | NAICS code or sector name |

**Jurisdiction is never defaulted.** If the user does not supply it, the skill asks. The jurisdiction determines pay-transparency disclosure obligations, applicable runtime warnings, and audit log retention per `hr-ai-governance` Section 4.3.

**SOC code is never assumed from title.** Role → SOC mapping is Method Step 1; the skill walks the O*NET crosswalk deterministically where possible and flags ambiguity as a data quality finding when the role does not have a clean SOC.

---

## Output Structure

Every `/comp-benchmark` output conforms to `sensitive-skill-guardrails.md` Section 3. Structure is non-negotiable.

### 1. Disclaimer + UPL Guardrail Block (top)

```
> ⚠️ **Not HR or employment-law advice.** This output is a drafting and triage aid generated by a product-organization skill, not HR counsel, compensation counsel, or employment counsel. No attorney-client relationship is created by its production or use. Jurisdiction-specific questions on pay-transparency obligations, pay equity compliance, protected-class pay analysis, or enforceability of compensation commitments require review by a licensed employment attorney in the relevant jurisdiction and by a qualified compensation professional. Compensation decisions involving individual offers, internal equity, pay equity, or retention require HR leadership review. Do not rely on this output as the sole basis for setting any pay band, making any individual offer, or responding to any pay-transparency obligation.
>
> **Jurisdiction Assumed:** {jurisdiction from the required input}. If your jurisdiction differs, treat every finding below as a hypothesis to verify with local counsel.
```

### 2. Benchmark Metadata block

A labeled block under the disclaimer with:

- **Role**: title as input
- **SOC Code Assigned**: primary SOC code chosen in Method Step 1 (e.g., `11-2021 Marketing Managers`) + any candidate SOCs considered
- **SOC Assignment Method**: `deterministic` / `O*NET crosswalk` / `ambiguous-analyst-choice`
- **Jurisdiction**: as input (no default)
- **Target Geography**: MSA / state / national / remote-national
- **Seniority Level**: as input
- **Pay Transparency Required**: `yes` / `no` (derived from Section 8.1 jurisdiction matrix + Section 5 of this skill)
- **Pack Inheritance**: `hr-ai-governance v{version}` (read at runtime)
- **Generation Timestamp**: ISO 8601 UTC
- **Governance Pack Version**: `hr-ai-governance v1.0.1+`
- **Data Freshness Window**: youngest source date and oldest source date across all queried sources

### 3. The Reference Grid

A table with the stated SOC code and target geography, reporting base pay only (no variable comp):

| Percentile | Annual Base | Source | Adjustment Applied |
|---|---|---|---|
| 10th | $X | BLS OEWS {year} {geography} | none / +N% ECI / etc. |
| 25th | $X | BLS OEWS {year} {geography} | none / +N% ECI / etc. |
| 50th (median) | $X | BLS OEWS {year} {geography} | none / +N% ECI / etc. |
| 75th | $X | BLS OEWS {year} {geography} | none / +N% ECI / etc. |
| 90th | $X | BLS OEWS {year} {geography} | none / +N% ECI / etc. |

Every value in the grid is the skill's structured extraction from whitelisted public sources. The skill does NOT invent values, does NOT interpolate across SOCs without documentation, and does NOT apply "professional judgment" adjustments. If a percentile cannot be sourced, the row is populated with `[cannot-source]` and a finding is raised.

**Variable compensation (bonus, equity, commission) is EXPLICITLY excluded from the grid.** The public data sources do not cleanly report variable comp; attempting to benchmark variable comp from public sources would produce misleading numbers. Variable comp is a separate future skill.

### 4. `## Methodology Worksheet`

A structured worksheet documenting every step the skill took to produce the grid. This is the audit-trail output — it is the most important section for a human reviewer.

Fields:

- **SOC Assignment**:
  - Primary SOC chosen: code + title
  - Alternate SOCs considered: list
  - Rationale for choice: one-paragraph explanation tied to role description
  - Ambiguity flag: `clean` / `ambiguous-primary-chosen` / `no-clean-match`
- **Sources Queried** (one row per source):
  - Source name (from whitelist)
  - URL accessed
  - Date accessed
  - SOC code queried
  - Geography queried
  - Data year (source vintage)
  - Result summary
- **Geography Adjustment**:
  - Was adjustment applied: yes / no
  - If yes: adjustment factor + source (BLS ECI metro ratio or ACS-derived metro wage ratio)
  - Documented reasoning
- **Seniority Adjustment**:
  - SOC-wide wage distribution captures an occupation, not a seniority level. Seniority within SOC requires a differentiation factor. The skill documents how the seniority adjustment was derived (e.g., "percentile position within SOC: Lead corresponds to 75th+ percentile within management SOC codes per BLS OEWS distribution notes") and flags the reliability of the adjustment
  - Method: percentile-banding / direct-match-from-pay-transparency-disclosures / cannot-derive
- **Assumptions**: numbered list of every assumption the skill made to produce the grid
- **Excluded Sources**: confirmed list of which whitelisted sources were NOT used for this run and why (e.g., "OPM: role is private-sector, not federal-equivalent")

### 5. `## Jurisdiction Compliance Report`

- **Jurisdiction**: as input
- **Pay Transparency Framework**: the specific rule(s) in force (e.g., "US-NYC: NYC DCWP pay-transparency law — range on posting required"; "US-CO: Colorado Equal Pay for Equal Work Act + Colorado AI Act SB24-205 deployer obligations; range on posting required; SB24-205 applies if AI substantial factor in consequential decision"; "US-DE: no pay-transparency rule in force as of 2026-04-11")
- **Disclosure Obligation**: `range-on-posting` / `range-on-request` / `range-at-interview` / `not-applicable`
- **Illinois HB 3773 trigger check**: applied if jurisdiction includes IL, flags adverse-impact check obligation per `hr-ai-governance` Section 2
- **Colorado AI Act trigger check**: applied if jurisdiction includes CO, flags deployer obligations per `hr-ai-governance` F11 / Section 8.1
- **EU pay-transparency directive (2023/970) check**: applied if jurisdiction is EU, flags member-state transposition status and applicable date
- **Compliance Posture**: `ready-to-disclose` / `requires-band-construction-before-posting` / `not-applicable` / `consult-employment-counsel`

### 6. `## Data Quality Flags`

Numbered findings covering data quality and reliability. Each flag gets a row with:

- Finding #
- Category — `thin-SOC-coverage` / `outdated-source` / `geography-extrapolation` / `seniority-adjustment-low-reliability` / `SOC-ambiguity` / `whitelist-gap` / `freshness-warning`
- What: specific issue
- Why it matters: impact on the grid's reliability
- Severity: P0 / P1 / P2
- Verdict: `address` / `accept-with-risk` / `cannot-address-within-whitelist`
- Suggested next step: what a human reviewer should do

### 7. `## Findings` (substantive)

Numbered findings beyond data quality. Examples:

- "SOC coverage thin for this geography (ACS 5-year not available at this MSA level); national BLS OEWS used with ECI metro ratio; reliability: moderate"
- "Latest source vintage is 18 months old for seniority-matched percentile; data within freshness window but nearing edge"
- "Jurisdiction requires pay-range disclosure at posting; grid supports compliant range construction at P25-P75"
- "Role title 'Customer Success Lead' does not have a clean SOC match; three candidate SOCs considered (see methodology worksheet); primary choice documented with rationale"

### 8. `## Reviewer Checklist`

Eight mandatory sign-off items before the grid is acted upon:

- [ ] Jurisdiction confirmed against role posting location and the employer's presence
- [ ] SOC code choice reviewed and accepted by compensation analyst
- [ ] Geography adjustment method reviewed and accepted (or corrected)
- [ ] Seniority adjustment method reviewed and accepted (or corrected)
- [ ] Every P0 data quality flag addressed or explicitly accepted-with-risk
- [ ] Jurisdiction compliance posture reviewed; employment counsel engaged if required
- [ ] No vendor-survey leakage in sources (grep check passed)
- [ ] Pay equity analysis explicitly confirmed out of scope (this skill does not produce a pay equity audit)

### 9. `## Cannot Assess Without`

Minimum 7 items. This section makes scope explicit:

- **Internal equity** — existing team comp bands. Separate workflow; confidential HR leadership.
- **Individual capability differentiation** — hiring manager judgment on a specific candidate's value to the role. Not a market data question.
- **Budget constraints** — finance input; depends on headcount plan, runway, organizational priorities. Out of scope.
- **Variable compensation modeling** — bonus targets, equity refresh math, commission plans. Separate future skill; public data does not support clean variable comp benchmarking.
- **Retention risk for a specific individual** — confidential HR leadership; depends on attrition signals, manager feedback, career conversations.
- **Pay equity compliance** — requires `/pay-equity-audit` (future phase) under attorney-client privilege with documented `@employment-counsel` engagement. Hard-scoped out of this skill. See the Pay Equity Rejection section below.
- **Non-whitelisted vendor survey data** — Radford, Mercer, WTW, Payscale, Salary.com, Glassdoor, Levels.fyi, H1B Wage DB. Deliberately excluded by source whitelist discipline. If the user wants vendor data, they must obtain it separately and this skill is not the tool.
- **Enforceability of compensation commitments** — offer letters, employment agreements, equity vesting clauses. Requires `@contracts-counsel` + `@employment-counsel`.

### 10. Audit Log Entry

Emitted per `hr-ai-governance` Section 4.1 schema, with the fields relevant to this skill:

- `run_id`, `timestamp`, `skill_name`, `skill_version`, `governance_pack_version`
- `jurisdiction`
- `inputs_hash` — SHA-256 of the canonicalized role-input object (role, jurisdiction, seniority, geography, SOC choice). NEVER raw candidate data — this skill doesn't see candidate data.
- `input_type: comp_record`
- `proxies_detected` — from Method Step 3 proxy scan; if the combination of geography + title + industry + company size triggers a proxy flag per `hr-ai-governance` Section 3.2, each flagged proxy becomes an entry
- `redactions_applied` — N/A for this skill (compensation data inputs are not candidate data)
- `hitl_reviewer` — authenticated identity of the compensation analyst or HR leader who will review
- `hitl_decision`, `hitl_timestamp`, `hitl_rationale` — populated at HITL gate
- `downstream_action` — e.g., `band-approved`, `band-rejected`, `band-sent-to-jd-generator`
- `signoff_path: standard`
- `retention_expiry` — computed from jurisdiction per Section 4.3

The skill refuses to run if the deployer's auth system cannot supply an authenticated `hitl_reviewer`.

---

## Method

The skill's benchmark flow is a 7-step pipeline. Order matters because later steps depend on earlier ones.

### Step 1 — Map Role to SOC Code

The SOC (Standard Occupational Classification, BLS-maintained) is the neutral, machine-consumable, jurisdiction-neutral taxonomy the skill uses to anchor every benchmark run. Role → SOC mapping is the most consequential step because every downstream query uses the SOC code.

Procedure:

1. Read the role title and any description text the user supplied
2. Query O*NET OnLine crosswalk for the title → SOC candidate list
3. If exactly one clean SOC matches, set primary SOC and set `SOC Assignment Method = deterministic`
4. If multiple SOCs are plausible, enumerate candidates (up to 5), assess each against the role description, and choose the primary SOC with a one-paragraph rationale; set `SOC Assignment Method = O*NET crosswalk`
5. If no clean SOC exists (novel role, hybrid function, emerging job category), document the three closest candidate SOCs, pick the primary with rationale, set `SOC Assignment Method = ambiguous-analyst-choice`, and flag a `SOC-ambiguity` finding at P1 severity
6. For ambiguous cases, consultation with `@recruiter` is available (Pattern 1 Consultation) — the recruiter sees role titles every day and has practical SOC-mapping intuition

The SOC choice and the alternates considered are ALWAYS documented in the methodology worksheet. There is no "silent SOC choice."

### Step 2 — Query BLS OEWS for Primary Grid

Using the primary SOC code from Step 1 and the target geography from the inputs:

1. Query BLS OEWS at the finest geography granularity that has data for this SOC (MSA → state → national fallback)
2. Extract the 10th / 25th / 50th / 75th / 90th percentile annual wages
3. Record the OEWS data year (vintage)
4. Record geography granularity actually used (e.g., "MSA data available" vs. "fell back to state data" vs. "fell back to national data")

If OEWS has no data for this SOC at any geography, the skill blocks and routes to Step 3 for secondary sources before continuing.

### Step 3 — Fill Gaps from Secondary Whitelist Sources + Proxy Scan

If OEWS coverage is thin or absent:

1. Query ACS for the target metro / county with the primary SOC
2. Query QCEW for industry + geography context
3. If role is federal-equivalent, query OPM GS tables for the target locality pay area
4. If jurisdiction has pay-transparency rules, query state/city pay-transparency job board disclosures and municipal pay scales for directly observed pay ranges in the target metro
5. Run the `hr-ai-governance` Section 3.2 proxy scanner on the input combination: does (geography + title + industry + company size) create a proxy for age / race / gender / national origin? E.g., a highly gender-skewed SOC in a racially-skewed metro with a small company filter can surface proxies that need to be controlled. Each detected proxy becomes a `proxies_detected` entry in the audit log and a finding in the Data Quality Flags section.

All secondary source queries are documented in the methodology worksheet row-by-row.

### Step 4 — Apply Geography Adjustment (if needed)

If OEWS or ACS has the SOC at the target geography at clean granularity, no geography adjustment is applied. Otherwise:

1. Query BLS ECI metro series for the target metro — ECI gives a cost-of-labor index
2. If ECI is not available for the target metro, derive an ACS metro wage ratio (target metro average wage / reference geography average wage)
3. Apply the adjustment factor to the reference grid percentiles
4. Document the adjustment factor, its source, and the reasoning in the methodology worksheet
5. The user can override the adjustment with explicit reasoning; the override is recorded in the audit log

Geography adjustment is one of the two most reviewer-scrutinized parts of the grid. Every adjustment is documented, not silent.

### Step 5 — Apply Seniority Adjustment

SOC codes capture an occupation, not a seniority level within the occupation. A "Marketing Manager" SOC includes everyone from entry-level manager to VP-level manager; the BLS OEWS percentile distribution captures that full range. Seniority within a SOC requires a differentiation factor.

Procedure:

1. Read the stated seniority level
2. Map seniority to a percentile position within the SOC wage distribution:
   - Junior / IC2 → 10th-25th percentile range
   - IC3 / Mid → 25th-50th percentile range
   - IC4 / Senior → 50th-75th percentile range
   - IC5 / Lead / Staff → 75th-90th percentile range
   - Principal / Director+ → 90th+ percentile range (and note that BLS reports "90th percentile" as a single value, not a distribution above it)
3. If pay-transparency job board disclosures provide direct seniority-labeled pay observations at the target geography, those override the percentile-banding method (direct evidence wins)
4. Document the seniority adjustment method and reliability level in the methodology worksheet
5. If the seniority adjustment cannot be defensibly derived (e.g., the SOC is too broad, the role's seniority doesn't map cleanly to a percentile band, the direct evidence doesn't exist), flag `seniority-adjustment-low-reliability` at P1

Seniority adjustment reliability is the second most reviewer-scrutinized part of the grid. The skill is conservative here: low reliability is flagged, not smoothed over.

### Step 6 — Run Jurisdiction Compliance Check

Per the jurisdiction loaded in the input:

1. Look up the row in `hr-ai-governance` Section 8.1
2. Determine the pay-transparency obligation (range-on-posting / range-on-request / range-at-interview / not-applicable)
3. If the jurisdiction is US-IL, trigger the HB 3773 adverse-impact check flag (per pack Section 2) as the grid may feed a JD or hiring pipeline
4. If the jurisdiction is US-CO, trigger the Colorado AI Act deployer obligations flag (pre-use notice, right to correct, annual impact assessment, 90-day algorithmic-discrimination notification to Colorado AG) per pack F11
5. If the jurisdiction is EU, check if the target member state has transposed Directive 2023/970 (transposition deadline was June 7, 2026, varying by member state) and flag applicable obligations
6. If the jurisdiction is not in the matrix, block and route to `@employment-counsel`

The compliance report surfaces obligations; the skill does not execute them. The deployer / HR leader is responsible for compliance actions.

### Step 7 — Generate Reference Grid + Methodology Worksheet

Assemble the grid, the methodology worksheet, the jurisdiction compliance report, and the data quality flags into the output structure defined above.

Run the 9-check quality gate (below) before emitting.

---

## Pay Equity Rejection (Hard Scope-Out)

Pay equity analysis is **out of scope** for `/comp-benchmark`. This is a hard boundary, not a soft preference.

If a user asks the skill to perform pay equity analysis — including but not limited to: "is our pay equitable?", "are women at our company paid fairly?", "do we have a gender pay gap?", "check for racial pay disparities in engineering," "audit our comp bands for protected-class pay gaps," "is our pay band fair under the Equal Pay Act?" — the skill:

1. **Refuses to proceed**
2. Returns a routing note:

   > "Pay equity analysis is out of scope for `/comp-benchmark`. Pay equity is legally and methodologically distinct from market benchmarking. It requires:
   > - Attorney-client privilege (so the analysis and its findings are protected from disclosure in litigation)
   > - Documented `@employment-counsel` engagement (so the privilege attaches)
   > - A different methodology: regression analysis on internal compensation data controlling for legitimate factors (tenure, performance, role, geography), with sensitivity analysis for protected-class variables
   > - A different data source: internal compensation records, not public BLS data
   > - A different audit log posture: privileged, attorney-work-product
   >
   > Use `/pay-equity-audit` (future phase — not yet available) and engage `@employment-counsel` BEFORE running any pay equity analysis. Running an unprivileged pay equity analysis can create discoverable evidence in litigation, which is the precise outcome the privileged path is designed to prevent."

3. Logs the rejection in the audit log as `downstream_action: pay-equity-refused-scope`
4. Does NOT produce a grid or any output that could be repurposed as pay equity analysis

The rejection is mandatory. There is no "express mode" that skips it. The reason is liability: a market benchmark grid that gets used in litigation as evidence of pay equity analysis is precisely the discoverable-exposure pattern the privileged path prevents. The skill defends the boundary.

---

## Quality Gates

The skill performs a 9-item self-check BEFORE emitting output. If any check fails, the output does not publish — it produces a structural finding instead, asking the user to fix the gap.

1. **SOC code assigned and justified** — every run has a primary SOC code with a documented rationale in the methodology worksheet
2. **All sources in whitelist (grep-able)** — every source cited in the methodology worksheet matches one of the eight whitelisted sources exactly; any unknown source is a gate failure
3. **At least one BLS source present** — BLS OEWS or QCEW must anchor the grid; a run that relies only on secondary sources (ACS, OPM, pay-transparency disclosures, municipal pay) without any BLS anchor is a gate failure
4. **Data freshness: every source dated within 24 months** — sources older than 24 months are flagged as a `freshness-warning`; sources older than 36 months are a gate failure unless explicitly accepted-with-risk by the reviewer
5. **Geography adjustment documented if applied** — if any adjustment factor was applied, its source, value, and reasoning must appear in the methodology worksheet; silent adjustments are a gate failure
6. **Seniority adjustment documented with method** — the method used to derive the seniority position within the SOC is documented; "analyst judgment" without a method reference is a gate failure
7. **Jurisdiction compliance surfaced** — the jurisdiction compliance report is present and the pay-transparency obligation is named (even if "not-applicable")
8. **No vendor-source leakage** — grep check for Radford, Mercer, Willis Towers Watson, WTW, Payscale, Salary.com, Glassdoor, Levels.fyi, H1B wage database, Comparably, Indeed Salary, Built In, LinkedIn Salary. Any hit is a gate failure.
9. **Pay equity analysis explicitly rejected if requested** — if the user's input asked for pay equity, the Pay Equity Rejection above MUST have fired and the skill MUST NOT have produced a grid

These 9 checks are the quality gates. They run every invocation. There is no "express mode" that skips them.

---

## Pack Inheritance

This skill inherits the following from `hr-ai-governance` pack v1.0.1. Each dependency is a contract between the skill and the pack; if the pack updates, the skill re-validates against the updated version on next run.

| Section | What the skill inherits |
|---|---|
| **3.2 non-obvious proxy register** | Method Step 3 runs a proxy scan on the input combination (geography + title + industry + company size → age / race / gender / national origin proxies). The scanner is seeded from the pack's proxy register. Any proxy added to Section 3.2 automatically becomes a new scanner trigger in the next run. |
| **4.1 audit log schema** | Every benchmark run emits a log record conforming to the canonical schema. `inputs_hash`, `jurisdiction`, `hitl_reviewer`, `signoff_path`, and `retention_expiry` are computed per the pack's rules, not per this skill. `input_type: comp_record`. |
| **8.1 jurisdiction matrix** | Pay-transparency obligations, retention periods, runtime warnings, HITL requirements, and specific framework triggers (Illinois HB 3773, Colorado AI Act SB24-205, EU Directive 2023/970) are all pulled from Section 8.1. The skill does NOT hard-code jurisdiction rules. |
| **10 HITL enforcement** | Gate placement per Section 10.3: HITL gate sits before the grid is saved or emitted for use. The compensation analyst or HR leader is the reviewer. Data quality flags and findings are shown inline at the gate. |
| **11.1 review cadence** | Subsequent-similar 72-hour substantive review under the Employment Counsel SLA. This is NOT first-of-type — the pack and `/resume-summarizer` carry first-of-type. `/job-description-generator` established the subsequent-similar precedent for HR skills. This skill inherits the established pattern. |

This skill is NOT an AEDT. It produces a market reference grid, not a candidate decision. The AEDT wall from `hr-ai-governance` Section 6 applies by inheritance only — no novel AEDT surface is added. The skill cannot screen candidates, rank candidates, make hiring decisions, make compensation offers, or perform pay equity analysis.

---

## Delegation Patterns Available

### Default: Pattern 1 Consultation

When a specific element of the grid needs specialist input, the skill spawns a consultation per `delegation-protocol.md` Pattern 1:

| Trigger | Spawn |
|---|---|
| Jurisdiction-specific pay-transparency interpretation (e.g., "does NYC DCWP apply to this remote role?"; "does Colorado AI Act deployer obligation attach here?"; "which EU member state's transposition applies?") | 👔 Employment Counsel |
| SOC mapping when role title is genuinely ambiguous (multiple plausible SOCs, novel role, hybrid function) | 🎯 Recruiter |
| Geography-adjustment methodology when ECI and ACS both miss the target metro | 🧮 BizOps (for financial-methodology validation of the adjustment factor) |
| Existing comp band validation against public data, when the user supplies an internal band to check | 💵 Compensation Analyst (self-consultation at a higher scrutiny level — "am I confident in this verdict?") |
| Public-sector role with federal-equivalent pay table ambiguity | 👔 Employment Counsel (for federal / state government role classification) |
| Any pay equity adjacent question | 👔 Employment Counsel (followed by hard refusal per the Pay Equity Rejection section) |

Consultations are attributed in the Data Quality Flags or Findings sections: "I consulted `@recruiter`, who noted that 'Customer Success Lead' most commonly maps to SOC 11-2021 Marketing Managers in their recent role-posting sample, though SOC 43-1011 First-Line Supervisors of Office Workers is a partial fit for the team-lead component. Primary SOC set to 11-2021 with ambiguity flagged." Ownership of the grid stays with Compensation Analyst.

### Adversarial Review

**NOT applicable at this version.** Adversarial Review (Pattern 5) is reserved for near-final deliverables with high-stakes, uncapped exposure (enterprise contracts, M&A documents, pricing commitments). A compensation reference grid is neither near-final nor uncapped-exposure at the generation stage; it is a draft going to a human compensation analyst who will review, interrogate, and potentially reject.

If a specific benchmark becomes high-stakes (e.g., a public-company executive comp disclosure, a class-action pay-transparency matter, a SEC-filed NEO compensation benchmark), the requester should use a different tool and engage `@employment-counsel` and external compensation consultants. This skill is deliberately scoped below that bar.

---

## ROI Framing

ROI for `/comp-benchmark` is reported as **"time saved on drafting and triage of a public-source compensation reference grid with methodology worksheet and jurisdiction compliance check"** — NEVER "time saved on compensation analysis," "time saved on pay-equity review," or "time saved on HR review."

HR-analytics blended rate: $200/hr (senior compensation analyst or HR-analytics specialist rate; higher than the standard HR $150/hr because the role combines BLS data literacy, jurisdictional compliance, and SOC mapping expertise).

Time-saved baseline: a careful, public-source-disciplined compensation reference grid with SOC mapping, geography adjustment documentation, seniority adjustment methodology, jurisdiction compliance check, and data quality flags is ~3-4 hours of manual drafting and triage time for a compensation analyst working with a hiring manager. Simpler refreshes (same SOC, same geography, updated BLS OEWS vintage) are ~1-1.5 hours baseline. Complex roles (ambiguous SOC, multi-jurisdiction posting, thin public data requiring multiple secondary source gap-fills) are 5+ hours baseline.

The ROI tracks ONLY the time the skill saves on drafting and triage of the structured artifact, not the substantive compensation review time. The substantive review by the compensation analyst, HR leader, and (where needed) employment counsel still happens in full.

Example ROI line for a standard benchmark run:

```
⏱️ ~3.5 hrs saved on drafting and triage in 55s, 18k tkns ~$1.1 cost, Value ~$700
```

---

## Related Skills + Hand-off

### Input

- **`/job-description-generator`** (bi-directional) — when a hiring manager runs comp-benchmark first to get a market grid, the grid output feeds JD-generator as the comp band input for pay-transparency jurisdictions. Conversely, when JD-generator runs first and needs a comp band, it can invoke comp-benchmark with the role + jurisdiction from its own inputs. The two skills are co-owned in spirit (JD-generator has compensation-analyst as co-owner for the Comp Band Alignment Report; comp-benchmark has job-description-generator as a consumer for the grid → JD pay range hand-off).

### Output feeds

- **`/job-description-generator`** — comp band for pay-transparency-required JDs; the grid's 25th-75th percentile range typically seeds the JD's compensation section
- **`/interview-guide`** (downstream) — seniority alignment check (does the stated seniority match what the SOC + comp band implies?)

### Future / deferred

- **`/pay-equity-audit`** — HARD scoped out. Different privilege posture (attorney-client privileged), different methodology (regression on internal data), different data source (internal comp records not public BLS), different audit log posture. Requires `@employment-counsel` engagement before running. Not in Phase 4A; not in this skill.
- **Variable comp benchmark skill** — future, separate skill. Public data does not support clean variable comp benchmarking; attempting to benchmark bonus / equity / commission from BLS data would produce misleading numbers.

### Pack

- **`hr-ai-governance` v1.0.1** — every run inherits proxy register (3.2), audit log schema (4.1), jurisdiction matrix (8.1), HITL enforcement (10), review cadence (11.1)

---

## Attribution and Maintenance

**Owner**: 💵 Compensation Analyst. The skill's SOC mapping, source whitelist discipline, BLS query logic, geography and seniority adjustment methodology, and pay equity scope-out are Compensation Analyst's accountability.

**Consumers** (skills / gateways that invoke this skill):

- `ext-hr` — HR team gateway, primary user
- `job-description-generator` — bi-directional; comp band input/output hand-off
- `interview-guide` — downstream; seniority alignment check

New consumers require a frontmatter update and a one-line note in the consuming gateway's or skill's dependency list.

**Authoring**: First-principles. This skill was authored from scratch during Phase 4A as the second HR skill under the `hr-ai-governance` pack (after `/job-description-generator`). Source whitelist was constructed directly from the execution plan's Round 2 constraints — specifically the Employment Counsel near-block that required public-source-only discipline. SOC mapping methodology is sourced from O*NET OnLine's public crosswalk and the BLS SOC system documentation, not from any vendor taxonomy. No content lifted from Radford, Mercer, Willis Towers Watson, Payscale, Salary.com, Glassdoor, Levels.fyi, H1B Wage Database, Comparably, Indeed Salary, Built In, or LinkedIn Salary Insights.

**Dependency on the pack**: The skill reads from `hr-ai-governance` at every invocation. When the pack's Section 3.2 proxy register, Section 4.1 audit log schema, or Section 8.1 jurisdiction matrix is updated, the skill picks up the new content on the next run. The pack version is recorded in every audit log entry.

**Updates**: Via the two-pass publication gate defined in `sensitive-skill-guardrails.md` Section 4. Pass 1 (scaffolding check) — 📋 Director of HR, 15 minutes, binary GO / REWORK. Pass 2 (substantive check) — 👔 Employment Counsel, **72-hour subsequent-similar SLA** (this is NOT first-of-type; the pack and `/resume-summarizer` carry the first-of-type burden; `/job-description-generator` established subsequent-similar precedent for HR skills).

Minor edits (typos, formatting, jurisdiction matrix syncs with pack updates) can bypass Pass 2. Any edit touching: the source whitelist (adding or removing a source), the SOC mapping method, the geography adjustment methodology, the seniority adjustment methodology, the pay equity rejection boundary, or the HITL gate placement — requires a full Pass 2 substantive review by Employment Counsel.

**Changelog**: Maintained at the bottom of this file.

---

## Example Invocation

```
User: /comp-benchmark --role "Customer Success Lead" --jurisdiction US-DE --seniority Lead --geography "remote-national, timezone overlap IL + US-Eastern"

/comp-benchmark v1.0.0 — loading:
  - Jurisdiction: US-DE (no pay-transparency rule; grid produced for reference only)
  - Governance pack: hr-ai-governance v1.0.1
  - Source whitelist: BLS OEWS, BLS QCEW, BLS ECI, OPM, O*NET, US Census ACS, state/city pay-transparency disclosures, municipal pay scales
  - Seniority: Lead (75th-90th percentile within SOC distribution)
  - Target geography: remote-national, coastal-metro-adjustment assumed

Running pipeline:
  Step 1: SOC mapping — role is ambiguous; 3 candidate SOCs considered (11-2021, 13-1111, 43-1011); primary = 11-2021 Marketing Managers with documented rationale; SOC-ambiguity flag raised (P1)
  Step 2: BLS OEWS query — national data retrieved for 11-2021 at 10th/25th/50th/75th/90th percentile
  Step 3: Secondary sources — ACS metro wage ratios retrieved for reference metros; pay-transparency disclosures sampled for CSM Lead postings in NY/CO/CA; proxy scan run (no flags)
  Step 4: Geography adjustment — national → coastal-metro adjustment applied using BLS ECI; +8% factor documented
  Step 5: Seniority adjustment — Lead mapped to 75th-90th percentile band with percentile-banding method; seniority-adjustment-reliability: moderate (no direct seniority-labeled observations for this exact role + geography)
  Step 6: Jurisdiction compliance — US-DE: no pay-transparency rule; compliance posture: not-applicable
  Step 7: Grid + methodology worksheet + jurisdiction report + data quality flags assembled

Producing output at:
  Legionis/Product/comp-benchmark-birth-test-2026-04-11.md

9/9 quality gates passed (with SOC-ambiguity flag surfaced for reviewer decision).

⏱️ ~3.5 hrs saved on drafting and triage in 55s, 18k tkns ~$1.1 cost, Value ~$700
```

---

## Changelog

- **1.0.0 (2026-04-11)** — Initial authoring. First-principles during Phase 4A as the second HR skill under the `hr-ai-governance` pack (after `/job-description-generator`). Owned by 💵 Compensation Analyst. Source whitelist constructed directly from the execution plan's Round 2 constraints following the Employment Counsel near-block on vendor-data sourcing. SOC mapping methodology sourced from BLS SOC system + O*NET OnLine public crosswalk; no vendor taxonomy used. Pay equity analysis hard-scoped out with mandatory rejection routine. Subsequent-similar 72-hour Pass 2 review under Employment Counsel SLA (the pack carries first-of-type status; `/resume-summarizer` carries first-of-type for skills; `/job-description-generator` established subsequent-similar precedent). Scaffolding review by 📋 Director of HR. Birth-tested against the same Legionis Customer Success Lead role used for `/job-description-generator` birth test, with explicit SOC ambiguity documented (see `Legionis/Product/comp-benchmark-birth-test-2026-04-11.md`).
