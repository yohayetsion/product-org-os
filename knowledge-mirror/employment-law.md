# Employment Law Knowledge Pack

**Version**: 1.0
**Type**: knowledge-pack
**Primary Users**: @employment-counsel, @general-counsel, @legal-dir
---
<!-- Attribution:
  Frameworks and patterns in this knowledge pack were informed by:
  - basecamp/handbook (github.com/basecamp/handbook) — employee handbook and employment policy patterns
  - alexch/clauses (github.com/alexch/clauses) — contract clause library and legal drafting patterns
  Adapted and expanded for Product Org OS agents.
-->

## Employment Lifecycle Compliance Overview

Employment law obligations span every phase of the employee relationship. Gaps at any stage create liability.

| Phase | Key Obligations | Risk if Ignored |
|-------|----------------|-----------------|
| **Hiring** | Anti-discrimination, FCRA, offer letter requirements | Disparate impact claims, FCRA violations |
| **Onboarding** | I-9 verification, tax forms, policy acknowledgments | Immigration liability, tax penalties |
| **Active Employment** | Wage/hour compliance, leave management, safety | Wage claims, ADA/FMLA violations |
| **Performance Management** | Documentation, progressive discipline, PIPs | Wrongful termination, retaliation claims |
| **Termination** | Final pay, WARN Act, severance requirements | Wage theft claims, class actions |
| **Post-Employment** | Non-compete enforcement, references, COBRA | Trade secret risk, discrimination claims |

---

## Hiring Compliance

### Anti-Discrimination Laws Matrix

| Law | Scope | Protected Classes | Applies To |
|-----|-------|------------------|------------|
| **Title VII (Civil Rights Act)** | Federal | Race, color, religion, sex, national origin | 15+ employees |
| **Americans with Disabilities Act (ADA)** | Federal | Disability, perceived disability | 15+ employees |
| **Age Discrimination in Employment Act (ADEA)** | Federal | Age 40+ | 20+ employees |
| **Pregnancy Discrimination Act (PDA)** | Federal | Pregnancy, childbirth, related conditions | 15+ employees |
| **Genetic Information Non-Discrimination Act (GINA)** | Federal | Genetic information, family medical history | 15+ employees |
| **Equal Pay Act (EPA)** | Federal | Sex (pay equity) | All employers |
| **State Fair Employment Laws** | Varies | Often broader (sexual orientation, gender identity, salary history) | Varies by state |

**Key principle**: Disparate impact (facially neutral policies with discriminatory effects) can be as actionable as disparate treatment (intentional discrimination).

### Background Check Requirements (FCRA)

The Fair Credit Reporting Act (FCRA) governs employer use of consumer reports for employment decisions.

**Mandatory FCRA Steps**:

```
Step 1: Disclosure & Authorization
  - Provide standalone written disclosure (separate from application)
  - Obtain signed written authorization
  - Disclosure must be clear and conspicuous — no additional waiver language

Step 2: Order Background Check
  - Use FCRA-compliant Consumer Reporting Agency (CRA)
  - Specify permissible purpose: employment

Step 3: Pre-Adverse Action (if considering adverse decision)
  - Provide copy of the consumer report
  - Provide "Summary of Your Rights Under the FCRA" (A Summary of Your Rights)
  - Allow reasonable time (minimum 5 business days) to dispute

Step 4: Adverse Action Notice
  - Provide final adverse action notice
  - Include CRA name, address, phone number
  - State CRA did not make the hiring decision
  - Advise of right to dispute with CRA
```

**Ban-the-Box Laws**: Over 35 states and 150+ localities restrict when criminal history can be inquired about. Common rules:
- Cannot ask about criminal history on initial application (remove the "box")
- Can only inquire after conditional offer extended
- Must conduct individualized assessment (nature of crime, time elapsed, job relevance)
- Some jurisdictions prohibit certain convictions from consideration entirely

**State-Specific Variations**: California (CCPA), New York City (Fair Chance Act), Illinois, Massachusetts have additional requirements. Always confirm local law.

### Interview Question Legality Matrix

| Topic | Illegal/Risky Questions | Permissible Alternatives |
|-------|------------------------|--------------------------|
| **Age** | "How old are you?" / "What year did you graduate?" | "Are you 18 or older?" (if minimum age requirement exists) |
| **Disability** | "Do you have any disabilities?" / "Have you been hospitalized recently?" | "Can you perform the essential functions of this job with or without accommodation?" |
| **Marital/Family Status** | "Are you married?" / "Do you plan to have children?" | "Are you able to meet the attendance requirements for this role?" |
| **Religion** | "What religion are you?" / "Do you observe any religious holidays?" | "This role requires Saturday availability — is that workable for you?" |
| **National Origin** | "Where are you from originally?" / "What's your native language?" | "Are you authorized to work in the United States?" |
| **Pregnancy** | "Are you pregnant?" / "Do you plan to start a family?" | Not permissible in any form before hire |
| **Criminal History** | "Have you ever been arrested?" (in ban-the-box jurisdictions) | Per jurisdiction — typically only after conditional offer |
| **Salary History** | "What are you currently earning?" | Prohibited in CA, NY, MA, IL, CO, and many localities |
| **Military** | "What branch did you serve in?" (used to infer protected class) | "Are you a veteran? We have a veteran preference program." |

### Offer Letter Requirements

A compliant offer letter should include — and should NOT include — the following:

**Must Include**:
- Position title and department
- Start date (or "on or about" date)
- Compensation (base salary, pay frequency, or hourly rate)
- Employment classification (exempt/non-exempt, full-time/part-time)
- At-will statement (in at-will states): "This offer does not constitute a contract of employment"
- Conditions: background check, drug screen, I-9 verification, reference checks
- Expiration date for the offer
- Benefits summary (reference benefits guide, not a promise of specific benefits)

**Should NOT Include**:
- Language that implies job security ("permanent position," "long-term opportunity")
- Specific benefit commitments (subject to plan documents)
- Overly detailed job descriptions (creates implied duties)
- Non-compete obligations without separate signed agreement with consideration

---

## Employment Classification

### Employee vs. Independent Contractor

Misclassification is one of the highest-risk areas in employment law. Key tests:

**IRS Common Law Test** (Federal tax purposes):

| Factor | Employee Indicators | Contractor Indicators |
|--------|--------------------|-----------------------|
| **Behavioral Control** | Company controls how work is done | Worker controls how work is done |
| **Financial Control** | Set pay, no profit/loss risk | Opportunity for profit/loss, multiple clients |
| **Relationship Type** | Ongoing indefinite relationship, benefits | Project-based, written contract, no benefits |

**ABC Test** (Used in CA, MA, NJ, IL and others — most restrictive):
- A: Worker is free from control and direction in performing work
- B: Work is outside the usual course of the hiring entity's business
- C: Worker is customarily engaged in an independently established trade

**If any ABC prong fails → worker is an employee in ABC-test states.**

**Economic Reality Test** (FLSA standard):
- Degree of permanency of the relationship
- Investment in equipment/materials
- Opportunity for profit or loss
- Degree of skill required
- Integration into employer's business
- Who controls the manner/means of work

### FLSA Exempt vs. Non-Exempt Tests

Non-exempt employees must receive overtime (1.5x for hours over 40/week). Exemptions require meeting BOTH a salary basis test AND a duties test.

**Salary Basis Test** (as of 2024): $684/week ($35,568/year) minimum. Highly compensated: $107,432/year.

**White-Collar Duties Tests**:

| Exemption | Primary Duty | Key Requirements |
|-----------|-------------|------------------|
| **Executive** | Management | Supervises 2+ employees, authority to hire/fire/recommend |
| **Administrative** | Office/non-manual work related to management | Exercises discretion and independent judgment on significant matters |
| **Professional (Learned)** | Advanced knowledge in field of science or learning | Requires advanced knowledge customarily acquired through prolonged course of specialized intellectual instruction |
| **Professional (Creative)** | Invention, imagination, originality, or talent | In a recognized field of artistic or creative endeavor |
| **Computer** | Systems analysis, programming, software engineering | Highly technical computer-related work ($27.63/hour alternative) |
| **Outside Sales** | Making sales or obtaining orders | Customarily and regularly away from employer's place of business |

**Common misclassification traps**:
- Job title alone does not determine exempt status (a "manager" who only manages equipment is likely non-exempt)
- Salary alone does not determine exempt status (must also meet duties test)
- Docking pay for partial-day absences destroys salary basis for most exemptions

---

## Wage & Hour Compliance

### FLSA Core Requirements

| Requirement | Rule | Notes |
|-------------|------|-------|
| **Minimum Wage** | Federal: $7.25/hour | 30+ states have higher minimums; always use higher of federal/state/local |
| **Overtime** | 1.5x regular rate for hours over 40/week | Regular rate includes most compensation (shift differentials, non-discretionary bonuses) |
| **Recordkeeping** | Hours worked, pay records for 3 years | Timekeeping system required for non-exempt employees |
| **Child Labor** | Restrictions on hours/jobs for under-18 | Stricter rules for under-16 |
| **Equal Pay** | Equal pay for substantially equal work | Defenses: seniority, merit, quantity/quality, factor other than sex |

### Regular Rate Calculation

The regular rate must include:
- Base hourly pay
- Shift differentials
- Non-discretionary bonuses (attendance bonuses, productivity bonuses)
- Commissions (if non-exempt)

The regular rate does NOT include:
- Gifts and vacation/holiday pay (at employer's discretion)
- Overtime premiums already paid
- Discretionary bonuses

**Formula**: Regular Rate = Total Remuneration for Workweek / Total Hours Worked

### Meal and Rest Break Requirements

Federal law (FLSA) does not require breaks, but most states do.

| Break Type | Common Rule | Compensability |
|------------|-------------|----------------|
| Rest breaks (5-20 min) | Many states require 10 min per 4 hours | COMPENSABLE — must be paid |
| Meal breaks (30+ min) | Many states require 30 min after 5-6 hours | NON-COMPENSABLE if employee is completely relieved of duties |
| Lactation breaks | Federal law requires reasonable unpaid breaks for nursing up to 1 year | Unpaid unless other breaks are paid |

**High-risk states for meal/rest break compliance**: California, Washington, Oregon, New York. CA requires premium pay (1 additional hour at regular rate) for missed meal or rest periods.

---

## Leave Laws

### FMLA (Family and Medical Leave Act)

**Coverage**: Employers with 50+ employees within 75 miles of worksite. Employees with 12 months of service and 1,250 hours in prior 12 months.

**Entitlement**: Up to 12 weeks unpaid, job-protected leave per year for:
- Birth/adoption/foster placement of child
- Serious health condition of employee
- Care for spouse, child, parent with serious health condition
- Qualifying military exigency

**Military caregiver**: Up to 26 weeks to care for covered servicemember.

**Key FMLA Obligations**:

| Obligation | Requirement |
|------------|-------------|
| **Notice to employee** | Within 5 business days of learning leave may qualify as FMLA |
| **Designation** | Designate leave as FMLA (even if employee doesn't ask) when it qualifies |
| **Certification** | May require medical certification within 15 calendar days |
| **Benefits continuation** | Maintain group health insurance on same terms during leave |
| **Job restoration** | Restore to same or equivalent position on return |
| **Anti-retaliation** | Cannot count FMLA leave in attendance/discipline policies |

### ADA Accommodations

The ADA requires reasonable accommodation for qualified individuals with disabilities unless undue hardship.

**Interactive Process Steps**:
```
Step 1: Employee requests accommodation (or employer becomes aware of need)
Step 2: Engage in good-faith interactive process
  - Request medical certification if needed
  - Identify essential functions of the job
  - Identify possible accommodations
  - Consider cost and operational impact
Step 3: Provide effective accommodation
  - Does not have to be the employee's preferred accommodation
  - Must be effective in removing the barrier
Step 4: Document the process
  - Maintain records of all communications
  - Document reasons if accommodation denied
```

**Common accommodations**: Modified schedules, remote work, leave of absence, ergonomic equipment, restructuring non-essential functions, reassignment to vacant position.

**Undue hardship factors**: Significant difficulty or expense relative to employer's size, financial resources, and nature of operations.

### State-Specific Leave Laws

Many states have leave laws exceeding FMLA minimums:

| State | Notable Leave Laws |
|-------|-------------------|
| **California** | CFRA (covers more conditions than FMLA), PDLL (4 months pregnancy), Paid Family Leave (up to 8 weeks paid) |
| **New York** | NY PFL (up to 12 weeks, partial pay), NY Paid Sick Leave (56 hours/year) |
| **Washington** | PFML (up to 16 weeks, partial pay), WFCA (12 weeks for domestic violence) |
| **Massachusetts** | PFML (26 weeks combined), MPLA |
| **New Jersey** | NJFLA (12 weeks), NJ TDI/FLI (paid) |
| **Oregon** | Paid Leave Oregon (12 weeks, partial pay) |

**Practical rule**: When FMLA and state leave both apply, run concurrently. Employee gets the better of each benefit.

### Parental Leave Considerations

No federal paid parental leave law exists. Employers must:
- Apply parental leave policies equally to similarly situated employees (mothers and fathers, same-sex couples)
- Coordinate with FMLA/state leave
- Document bonding vs. disability/medical portions carefully

---

## Performance Management Legal Framework

### PIP Requirements and Best Practices

A defensible Performance Improvement Plan (PIP) must be:

**Content Requirements**:
```
1. Specific performance deficiencies
   - Cite actual examples with dates
   - Reference specific policy, expectation, or standard not met
   - Avoid vague language ("attitude problem," "not a team player")

2. Clear improvement expectations
   - Measurable, specific goals
   - Defined timeline (30/60/90 days typical)
   - Resources and support provided

3. Consequences
   - Explicit statement that failure may result in termination
   - Intermediate consequences if applicable

4. Employee acknowledgment
   - Signature line with "I acknowledge receipt, not agreement" option
   - Date of meeting

5. Follow-up schedule
   - Regular check-in dates
   - Progress documentation plan
```

**Documentation During PIP**:
- Maintain contemporaneous records of all check-ins
- Document progress (positive and negative)
- If extending PIP, document reason and revised timeline
- If meeting conditions, document successful completion and close PIP formally

### Progressive Discipline Framework

| Step | Purpose | Documentation Required |
|------|---------|----------------------|
| **Verbal Warning** | Alert employee to issue | Note to file (date, issue, expectation, consequence) |
| **Written Warning** | Formal notice of performance/conduct issue | Written warning signed by employee and manager |
| **Final Written Warning / PIP** | Last chance before termination | PIP document with timeline and measurable goals |
| **Termination** | End of employment | Termination letter, final checklist |

**Skipping steps**: Serious misconduct (harassment, violence, fraud, theft) typically allows immediate termination without progressive discipline. Document the reason for bypassing steps.

**Consistency is critical**: Employees in similar situations should receive similar discipline. Disparate treatment of protected class members in discipline is a primary retaliation/discrimination risk.

---

## Termination Compliance

### At-Will vs. Cause Termination

**At-will employment** (default in 49 states; Montana is the exception): Either party can terminate for any reason or no reason, with or without notice, as long as the reason is not illegal (discriminatory, retaliatory, or in violation of public policy).

**Exceptions to at-will**:
- **Discriminatory reason**: Protected class membership influenced the decision
- **Retaliatory reason**: Employee engaged in protected activity (EEOC charge, OSHA complaint, whistleblower)
- **Public policy exception**: Firing for refusing to commit illegal act, exercising legal right
- **Implied contract**: Employee handbook language promising termination only for cause
- **Covenant of good faith and fair dealing**: (California primarily) Cannot terminate to avoid paying benefits/commissions earned

**For-cause termination**: Document the cause thoroughly. Cause typically means material breach of policy, serious misconduct, or inability to perform essential functions after accommodation.

### WARN Act Requirements

The Worker Adjustment and Retraining Notification (WARN) Act requires 60 days advance notice for:
- Plant closings affecting 50+ employees
- Mass layoffs of 500+ employees, or 50-499 employees if they represent 33%+ of the workforce
- Covered employers: 100+ full-time employees or 100+ employees working 4,000+ hours/week combined

**WARN Notice Must Go To**:
1. Affected employees (or their union representative)
2. State dislocated worker unit
3. Chief elected official of local government

**WARN Exceptions** (notice may be reduced or eliminated):
- Faltering company (actively seeking capital/business to avoid shutdown)
- Unforeseeable business circumstances
- Natural disaster

**State mini-WARN laws**: California (75+ employees, 50+ affected), New York (50+ employees), Illinois, New Jersey have broader requirements.

### Severance Agreement Requirements

**Older Workers Benefit Protection Act (OWBPA)** — for employees 40+:

| Requirement | Rule |
|-------------|------|
| **Plain language** | Written in terms the employee can understand |
| **Specific ADEA waiver** | Must specifically reference ADEA rights |
| **21-day consideration period** | Employee has 21 days to consider (45 days if group layoff) |
| **7-day revocation period** | Employee has 7 days to revoke after signing |
| **No waiver of future claims** | Cannot waive ADEA claims that arise after signing |
| **Group layoff disclosure** | Must disclose job titles and ages of those included/excluded in group layoff |

**General best practices for all severance agreements**:
- Release must be supported by consideration (something of value beyond what employee is already owed)
- Cannot release workers' compensation claims in most states
- Cannot release EEOC right to file charge (can waive right to monetary recovery)
- Confidentiality/non-disparagement clauses now restricted by NLRA (cannot prohibit discussing wages/working conditions)

### Final Pay Rules by State

| State | Timing Rule |
|-------|------------|
| **California** | Immediately upon termination (or within 72 hours if voluntary quit without notice) |
| **New York** | Next regular payday |
| **Texas** | Within 6 calendar days of termination |
| **Illinois** | Next regular payday |
| **Florida** | Next regular payday |
| **Federal (FLSA)** | Next regular payday (minimum standard) |

**Deductions from final pay**: Cannot make deductions for unreturned property, overpayments, or advances that would take pay below minimum wage without signed authorization.

**Unused PTO**: Payout required in CA, IL, MT, and other states where PTO is considered earned wages.

### Post-Employment Obligations

**Non-Compete Enforceability by Jurisdiction**:

| Jurisdiction | Status |
|-------------|--------|
| **California** | Void and unenforceable (nearly absolute ban) |
| **Minnesota, North Dakota, Oklahoma** | Largely unenforceable |
| **FTC Rule (2024, contested)** | Federal ban on new non-competes (litigation pending) |
| **Most other states** | Enforceable if reasonable in scope, geography, and duration |

**Reasonableness factors for non-competes**:
- Geographic scope (must match actual competitive territory)
- Duration (typically 6-24 months; longer = higher risk)
- Scope of restricted activities (must protect legitimate business interest)
- Consideration (must be provided at time of signing — some states require fresh consideration for existing employees)

**Garden leave**: Employee paid during non-compete period. Favored in UK/EU; increasingly used in US to support enforceability.

---

## Workplace Safety (OSHA)

### General Duty Clause

All employers must provide a workplace free from recognized hazards likely to cause death or serious physical harm. Even if no specific OSHA standard exists, employers can be cited under the General Duty Clause.

### Key OSHA Requirements

| Obligation | Requirement |
|------------|-------------|
| **Injury/Illness Recording** | OSHA 300 log for employers with 10+ employees in covered industries |
| **Posting** | OSHA "Job Safety and Health — It's the Law" poster in workplace |
| **Reporting** | Fatalities within 8 hours; amputations, eye loss, hospitalizations within 24 hours |
| **Hazard Communication** | SDS sheets, chemical labeling (GHS standard) |
| **Anti-Retaliation** | Cannot discipline employees for reporting injuries or safety concerns |

### Remote Work Considerations

OSHA's general duty clause extends to home offices for work-related injuries. Employer obligations:
- Cannot typically inspect employee's home office
- Should provide ergonomic guidance and home office standards
- Workers' compensation typically covers work-related home office injuries
- Document that remote work conditions were communicated and employee acknowledged responsibility for compliant home workspace

---

## Whistleblower Protections

Over 20 federal statutes protect employees who report violations. Key protections:

| Statute | Protected Activity | Employer Prohibition |
|---------|-------------------|---------------------|
| **FLSA Section 15(a)(3)** | Filing wage/hour complaints | Cannot discharge or discriminate |
| **OSHA Section 11(c)** | Reporting safety violations | Cannot discharge or discriminate |
| **Sarbanes-Oxley (SOX)** | Reporting securities fraud | Cannot take adverse action |
| **Dodd-Frank** | Reporting to SEC | Cannot discharge, demote, suspend, harass |
| **Title VII / ADEA / ADA** | Filing EEOC charges, participating in investigations | Cannot retaliate |
| **FMLA** | Exercising FMLA rights | Cannot interfere or retaliate |
| **NLRA** | Concerted activity (discussing wages, working conditions) | Cannot interfere with Section 7 rights |

**Retaliation red flags**: Adverse action (termination, demotion, schedule change, negative review, increased scrutiny) within close temporal proximity to protected activity is circumstantial evidence of retaliation.

---

## International Employment Considerations

### Employer of Record (EOR) Model

When hiring outside the employer's home country without a local entity, an EOR is the legal employer of record.

| Aspect | Direct Employment (local entity) | EOR Model |
|--------|----------------------------------|-----------|
| **Setup** | Establish local entity (weeks to months) | Deploy in days |
| **Compliance** | Full local HR/legal compliance required | EOR handles local compliance |
| **Cost** | High fixed cost | EOR fee (typically 15-25% of salary) |
| **Control** | Full employer rights | Shared control (EOR = legal employer) |
| **Best for** | Long-term, high-headcount markets | Testing markets, <5 employees |

### Key Local Compliance Areas

| Area | Common International Difference |
|------|--------------------------------|
| **Termination** | Most countries require just cause; notice periods often statutory and lengthy |
| **Mandatory benefits** | Statutory leave, healthcare, pension contributions vary significantly |
| **Working hours** | EU Working Time Directive caps at 48 hours/week; opt-out required |
| **Non-competes** | Enforceability and compensation requirements vary widely (Germany requires full pay during restriction) |
| **Collective bargaining** | Works councils (Germany, Netherlands) have co-determination rights; must consult before workforce changes |
| **Data privacy** | GDPR restricts employee data processing; transfer to US requires Standard Contractual Clauses or adequacy decision |

---

## Common Employment Law Red Flags

### Hiring Red Flags

- [ ] Using application questions that reveal protected class information before conditional offer
- [ ] Conducting background checks without FCRA-compliant disclosure and authorization
- [ ] Asking salary history questions in prohibited jurisdictions
- [ ] Making hiring decisions based on criminal history without individualized assessment (ban-the-box jurisdictions)
- [ ] Job descriptions with age-coded language ("recent graduate," "digital native")

### Active Employment Red Flags

- [ ] Classifying workers as independent contractors using behavioral/financial control typical of employees
- [ ] Treating supervisors as automatically exempt without conducting FLSA duties test
- [ ] Docking exempt employee pay for partial-day absences (destroys salary basis)
- [ ] Failing to designate FMLA leave when employee clearly qualifies
- [ ] Applying attendance policies to FMLA-protected absences
- [ ] Failing to engage in interactive process when accommodation request received

### Termination Red Flags

- [ ] Terminating employee within weeks of filing EEOC charge, OSHA complaint, or workers' comp claim
- [ ] Terminating employee on FMLA leave or shortly after return
- [ ] Group layoff without WARN Act analysis
- [ ] Missing final pay deadlines (especially California)
- [ ] OWBPA-deficient severance agreement tendered to employees 40+
- [ ] Handbook language promising termination only for cause (creates implied contract)

### Documentation Red Flags

- [ ] Verbal warnings not documented contemporaneously
- [ ] Performance reviews inconsistent with eventual termination rationale
- [ ] Different treatment of similarly situated employees in different protected classes
- [ ] PIP issued without measurable goals or follow-up documentation
- [ ] Termination decision made before performance issues adequately documented
