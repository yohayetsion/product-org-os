# IP Strategy Knowledge Pack

**Version**: 1.0
**Type**: knowledge-pack
**Primary Users**: @ip-counsel, @general-counsel, @legal-dir

---
<!-- Attribution:
  OSS license compliance section informed by:
  - GitHub Open Source Guides (opensource.guide) — license compliance, SBOM standards, contributor licensing
  Adapted and expanded for Product Org OS agents.
-->

## IP Protection Mechanisms

### Four Pillars of IP Protection

| Mechanism | What It Protects | Duration | Cost | Strength |
|-----------|-----------------|----------|------|----------|
| **Patents** | Inventions, processes, methods | 20 years from filing | High ($10K-$50K+ per patent) | Strong if enforceable |
| **Trademarks** | Brand names, logos, slogans | Indefinite (with use/renewal) | Medium ($1K-$5K per mark) | Strong with consistent use |
| **Copyrights** | Creative works, code, content | Life + 70 years / 95 years (work for hire) | Low (automatic; registration $35-$85) | Moderate |
| **Trade Secrets** | Confidential business information | Indefinite (while secret) | Low (operational cost) | Strong if properly maintained |

### IP Protection Decision Framework

```
Is this IP valuable to the business?
  └─ No → Don't protect (waste of resources)
  └─ Yes → Is it an invention/method/process?
       └─ Yes → Consider patent (if novel, non-obvious, useful)
            └─ Would disclosure (required for patent) harm us? → Trade secret instead
       └─ No → Is it a brand identifier?
            └─ Yes → Trademark
            └─ No → Is it creative/expressive work?
                 └─ Yes → Copyright (automatic, register for enforcement)
                 └─ No → Is it confidential business info?
                      └─ Yes → Trade secret program
```

---

## Patent Strategy

### Patent vs. Trade Secret Decision

| Factor | Favors Patent | Favors Trade Secret |
|--------|--------------|-------------------|
| Independent discovery risk | High (others likely to invent) | Low (unique to our process) |
| Reverse engineering risk | High (product reveals method) | Low (not discoverable) |
| Duration needed | <20 years | Indefinite |
| Enforcement budget | Available | Limited |
| Defensive value | Need to block competitors | Internal process advantage |
| Publication tolerance | Acceptable | Disclosure would destroy value |

### Software Patent Considerations (Post-Alice)

| Patentable | Not Patentable |
|-----------|----------------|
| Novel algorithm with specific technical improvement | Abstract idea implemented on a computer |
| Hardware-software integration | Mathematical formula applied generically |
| Specific technical solution to technical problem | Business method without technical innovation |
| Improvement to computer functionality | Conventional activity with "apply it on a computer" |

### Patent Filing Strategy

| Strategy | When to Use | Cost Profile |
|----------|------------|-------------|
| **Provisional** | Early-stage, establish priority date, buy 12 months | Low ($2K-$5K) |
| **Non-provisional (US)** | Primary market is US, clear claims | Medium ($10K-$20K) |
| **PCT (international)** | Multi-market protection needed | High ($15K-$30K initial, $5K-$15K per country) |
| **Continuation** | Broaden claims on existing patent | Medium ($8K-$15K) |
| **Defensive publication** | Prevent others from patenting, no enforcement intent | Low ($1K-$3K) |

### Freedom to Operate (FTO) Analysis

```
1. Define the product/feature to be analyzed
2. Search relevant patent databases (USPTO, EPO, WIPO)
3. Identify potentially relevant patents
4. Analyze claims for overlap with your product
5. Assess risk level:
   - Green: No relevant patents found
   - Yellow: Patents exist but claims don't cover our implementation
   - Red: High overlap, need to design around or license
6. Document findings and recommendations
7. Review with counsel before proceeding
```

---

## Open Source License Compliance

### License Categories

| Category | Examples | Key Obligation | Commercial Impact |
|----------|---------|----------------|-------------------|
| **Permissive** | MIT, BSD, Apache 2.0 | Attribution only | Low — can use in proprietary software |
| **Weak copyleft** | LGPL, MPL 2.0 | Share modifications to OSS component only | Medium — keep modifications open, proprietary code separate |
| **Strong copyleft** | GPL v2, GPL v3 | Share all linked/combined code | High — "viral" effect on proprietary code |
| **Network copyleft** | AGPL v3 | Share code even for network services (SaaS) | Very High — SaaS use triggers obligations |
| **Public domain** | CC0, Unlicense, WTFPL | None | None |

### OSS Compliance Checklist

| Step | Action | Responsible |
|------|--------|-------------|
| 1 | Maintain Software Bill of Materials (SBOM) | Engineering |
| 2 | Scan for licenses on every dependency | CI/CD pipeline |
| 3 | Categorize by license type | Legal/Engineering |
| 4 | Flag copyleft licenses for review | Automated |
| 5 | Verify compliance obligations met | Legal review |
| 6 | Generate attribution notices | Automated |
| 7 | Review new dependencies before adoption | PR review process |

### OSS License Compatibility Matrix

| Combining | MIT | Apache 2.0 | LGPL | GPL v2 | GPL v3 | AGPL |
|-----------|-----|-----------|------|--------|--------|------|
| **MIT** | OK | OK | OK | OK | OK | OK |
| **Apache 2.0** | OK | OK | OK | Complicated | OK | OK |
| **LGPL** | OK | OK | OK | OK | OK | OK |
| **GPL v2** | OK | Complicated | OK | OK | No | No |
| **GPL v3** | OK | OK | OK | No | OK | OK |
| **AGPL** | OK | OK | OK | No | OK | OK |

*Note: "OK" means the less restrictive license can be included in a project under the more restrictive license. The combined work is distributed under the more restrictive license's terms.*

### High-Risk OSS Scenarios

| Scenario | Risk | Mitigation |
|----------|------|------------|
| GPL library linked to proprietary code | Must open-source proprietary code | Use permissive alternative or keep separate |
| AGPL component in SaaS product | Must provide source for entire service | Avoid or isolate behind API boundary |
| Modified LGPL library | Must share modifications (not your code) | Document modifications clearly |
| Apache 2.0 patent clause | Triggers patent retaliation clause | Understand patent implications before suing |
| No license specified | Default copyright = cannot use | Request license from author or avoid |

---

## Trade Secret Program

### Trade Secret Requirements (Defend Trade Secrets Act / DTSA)

To qualify as a trade secret, information must be:
1. **Not generally known** or readily ascertainable
2. **Derives economic value** from being secret
3. **Subject to reasonable measures** to maintain secrecy

### Reasonable Measures Checklist

| Measure | Implementation |
|---------|---------------|
| NDAs/Confidentiality agreements | All employees, contractors, partners sign NDAs |
| Access controls | Need-to-know basis, role-based access |
| Physical security | Locked areas, clean desk policy |
| Digital security | Encryption, DLP, audit logs |
| Marking | Documents labeled "Confidential" or "Trade Secret" |
| Exit procedures | Return of materials, exit interview, reminder of obligations |
| Training | Regular training on what constitutes trade secrets |
| Audit | Periodic review of who has access to what |

### Common Trade Secrets in Tech Companies

| Category | Examples |
|----------|---------|
| **Algorithms** | Recommendation engines, pricing models, fraud detection |
| **Customer data** | Customer lists, usage patterns, buying behavior |
| **Business processes** | Sales playbooks, operations workflows, vendor relationships |
| **Financial information** | Pricing formulas, cost structures, margin data |
| **Technical know-how** | Configuration expertise, optimization techniques, debugging approaches |
| **Strategic plans** | Product roadmaps, M&A targets, market entry plans |

---

## AI-Generated Content IP

### Current Legal Landscape (2024-2026)

| Issue | Current Position | Trend |
|-------|-----------------|-------|
| **AI-generated content copyright** | US Copyright Office: No copyright for purely AI-generated works | May evolve with legislation |
| **AI-assisted content copyright** | Copyrightable if human provides sufficient creative control | Case-by-case analysis |
| **AI training data** | Active litigation (NYT v. OpenAI, etc.) | Fair use defense being tested |
| **AI model output ownership** | Contractual (see terms of service) | Depends on AI provider ToS |
| **AI inventorship (patents)** | USPTO: AI cannot be named inventor (Thaler v. Vidal) | Consistent globally |

### AI IP Risk Mitigation

| Risk | Mitigation Strategy |
|------|-------------------|
| AI output not copyrightable | Ensure sufficient human creative contribution |
| Training data infringement claims | Document data provenance, use licensed/public domain data |
| Employee using AI tools | Clear policy on AI tool usage and IP ownership |
| AI vendor IP claims | Review vendor ToS for output ownership provisions |
| Trade secret exposure to AI | Policy against inputting trade secrets into external AI tools |

### AI Usage Policy Framework

```
1. Approved AI Tools
   - List approved tools by category (code, writing, design)
   - Prohibited tools and why

2. Data Handling
   - Never input: trade secrets, PII, confidential business data
   - Allowed to input: public information, de-identified data
   - Check vendor data retention policies

3. Output Ownership
   - Company owns AI-assisted work product
   - Document human creative contribution
   - Review vendor IP terms

4. Disclosure Requirements
   - When to disclose AI use (customer-facing content, patents)
   - Internal documentation of AI involvement

5. Quality Review
   - All AI-generated content must be human-reviewed
   - Fact-check AI outputs before publishing
   - Check for potential IP infringement in outputs
```

---

## Trademark Strategy

### Trademark Selection Strength Spectrum

| Strength | Type | Example | Registrability |
|----------|------|---------|----------------|
| **Fanciful** | Invented word | Xerox, Kodak | Strongest |
| **Arbitrary** | Real word, unrelated to product | Apple (computers) | Strong |
| **Suggestive** | Suggests quality/characteristic | Netflix, Airbnb | Moderate |
| **Descriptive** | Describes the product | "Best Buy" | Weak (needs secondary meaning) |
| **Generic** | Common name for the product | "Computer Store" | Unregistrable |

### Trademark Protection Checklist

| Step | Action | Timeline |
|------|--------|----------|
| 1 | Clearance search (USPTO TESS + common law) | Before brand launch |
| 2 | File intent-to-use application | Before public use |
| 3 | File in key international markets (Madrid Protocol) | Within 6 months of US filing |
| 4 | Monitor for infringement | Ongoing |
| 5 | Enforce against infringers | As discovered |
| 6 | Maintain registrations (renewals, use) | Every 5-10 years |
| 7 | Domain name protection | At trademark filing |

---

*Last Updated: 2026-02-14*
*References: 35 U.S.C. §§ 101-103 (Patents), 17 U.S.C. § 102 (Copyright), Defend Trade Secrets Act (18 U.S.C. § 1836), Lanham Act (15 U.S.C. § 1051 et seq.), EU AI Act*
*Disclaimer: This is informational guidance, not legal advice. Consult qualified legal counsel for binding decisions.*


## Common Pitfalls

- Patent filing deadlines are jurisdiction-specific and often non-extendable
- Open source license compatibility must be checked before incorporating libraries
- Trade secret protection requires documented reasonable measures

---

## Open Source License Compliance (Extended)

*Sources: GitHub Open Source Guides, choosealicense.com, SPDX License List, FOSSA documentation, Linux Foundation SBOM standards*

### License Category Matrix (Detailed)

#### Permissive Licenses

| License | Key Obligations | Patent Grant | Compatible With | Commercial Use |
|---------|----------------|--------------|-----------------|----------------|
| **MIT** | Attribution in code/docs | No | All OSS licenses | Yes |
| **Apache 2.0** | Attribution + NOTICE file preservation | Yes (express) | All except GPL v2 | Yes |
| **BSD 2-Clause** | Attribution | No | All OSS licenses | Yes |
| **BSD 3-Clause** | Attribution + no endorsement clause | No | All OSS licenses | Yes |
| **ISC** | Attribution | No | All OSS licenses | Yes |

**Permissive Compliance Checklist**:
- [ ] Include original copyright notice in all copies
- [ ] Include license text (usually in NOTICES or LICENSE file)
- [ ] For Apache 2.0: preserve NOTICE file contents; do not use contributor names for endorsement
- [ ] Attribution in documentation or about screens (if binary distribution)

#### Weak Copyleft Licenses

| License | Copyleft Scope | Key Obligation | Commercial Impact |
|---------|---------------|----------------|-------------------|
| **LGPL v2.1** | Library/component only | Allow relinking; modifications to LGPL code must be open; proprietary application code stays private | Medium — keep component boundary clean |
| **LGPL v3** | Library/component only | Same as v2.1 plus anti-tivoization clause (allow user modification on hardware) | Medium-High — hardware products more affected |
| **MPL 2.0** | File-level copyleft | Modified MPL files must be open; files you create stay proprietary | Low-Medium — clean file boundaries required |
| **EPL 2.0** | Module-level copyleft | Module modifications open; "compatible" linking provisions for larger works | Medium |
| **CDDL 1.0** | File-level copyleft | Modified files open; can combine with proprietary in same executable | Medium |

**Weak Copyleft Compliance Checklist**:
- [ ] Identify exact version of library used (LGPL v2 vs v3 matters significantly)
- [ ] Ensure modifications to the OSS component are documented and releasable
- [ ] LGPL: Provide ability to relink the library (static linking may require full source)
- [ ] MPL: Do not commingle MPL and proprietary code in same file
- [ ] Notify users how to obtain modified source code

#### Strong Copyleft Licenses

| License | Copyleft Scope | Key Trigger | SaaS Trigger |
|---------|---------------|-------------|--------------|
| **GPL v2** | All linked code | Distribution of binary triggers source release | No (SaaS loophole) |
| **GPL v3** | All linked code | Distribution triggers source; anti-tivoization added | No (SaaS loophole) |
| **AGPL v3** | All linked code + network use | **Network access = distribution** — SaaS fully triggered | Yes |
| **EUPL v1.2** | All linked code | Distribution; compatible with GPL v2 | Partial |
| **SSPL** | Service code | If you offer software as a service, must open entire service stack | Yes |

**Strong Copyleft Compliance Checklist**:
- [ ] NEVER statically link GPL code into proprietary software that will be distributed
- [ ] GPL v2: Provide or offer written source code with binary distribution
- [ ] GPL v3: Same as v2 plus include installation instructions and anti-tivoization compliance
- [ ] AGPL v3: If running AGPL code as a service, you MUST offer source code to all network users
- [ ] Document all GPL/AGPL dependencies in SBOM before any distribution decision

#### Creative Commons (For Content and Data — Not Code)

| License | Use Case | Can Use Commercially? | Share-Alike Required? |
|---------|----------|----------------------|----------------------|
| **CC0** | Public domain dedication | Yes | No |
| **CC-BY 4.0** | Attribution-only content | Yes | No |
| **CC-BY-SA 4.0** | Wikipedia-style content | Yes | Yes (derivatives under CC-BY-SA) |
| **CC-BY-NC 4.0** | Non-commercial only | No | No |
| **CC-BY-ND 4.0** | No derivatives | Yes | N/A — no modifications |
| **CC-BY-NC-SA 4.0** | Non-commercial + share-alike | No | Yes |

**Note**: Creative Commons licenses are not appropriate for software code. Use only for documentation, datasets, training data, artwork, and written content.

---

### License Compatibility Matrix (Combining Licenses)

When a project incorporates code under multiple licenses, the combined work must satisfy all licenses simultaneously:

| Incorporating | Into MIT | Into Apache 2.0 | Into LGPL | Into GPL v2 | Into GPL v3 | Into AGPL v3 |
|--------------|----------|-----------------|-----------|-------------|-------------|--------------|
| **MIT** | OK | OK | OK | OK | OK | OK |
| **Apache 2.0** | OK | OK | OK | Incompatible* | OK | OK |
| **LGPL v2.1** | OK | OK | OK | OK | OK | OK |
| **LGPL v3** | OK | OK | OK | Incompatible | OK | OK |
| **GPL v2** | OK | Incompatible* | OK | OK | Incompatible | Incompatible |
| **GPL v3** | OK | OK | OK | Incompatible | OK | OK |
| **AGPL v3** | OK | OK | OK | Incompatible | OK | OK |

*Apache 2.0 + GPL v2: Apache 2.0's patent retaliation clause conflicts with GPL v2's "no additional restrictions" rule. Incompatible for combined distribution. Apache 2.0 is compatible with GPL v3.

**Decision rule**: The combined work must be distributed under the most restrictive license present (if compatible). If two copyleft licenses are incompatible, the combination cannot legally be distributed.

---

### Per-License Compliance Checklists

#### MIT License Compliance
- [ ] Retain copyright notice in all copies and substantial portions
- [ ] Include MIT license text with source and binary distributions
- [ ] No additional obligations

#### Apache 2.0 License Compliance
- [ ] Include Apache 2.0 license text
- [ ] Include any NOTICE file and preserve its contents
- [ ] State changes made to any Apache-licensed files
- [ ] Do not use contributor names/trademarks for endorsement
- [ ] Note: contains express patent grant — understand patent retaliation clause

#### LGPL v2.1 Compliance
- [ ] Include LGPL v2.1 license text
- [ ] Provide mechanism for users to relink (avoid static linking or provide object files)
- [ ] Any modifications to LGPL files must be released under LGPL
- [ ] Original copyright notices preserved

#### GPL v3 Compliance
- [ ] Provide complete corresponding source code
- [ ] Include GPLv3 license text
- [ ] Include installation instructions for user-installed products
- [ ] Prominent notice of modifications with date
- [ ] No additional restrictions beyond GPL v3

#### AGPL v3 Compliance
- [ ] All GPL v3 obligations apply
- [ ] If running as network service: prominently offer source code download to all users interacting with the service
- [ ] Preferred: link to source in footer/about of the service

---

### SBOM (Software Bill of Materials)

#### Why SBOMs Matter

| Use Case | Value |
|----------|-------|
| License compliance | Know every license in your dependency tree |
| Security vulnerability management | Rapidly identify affected components (e.g., Log4Shell) |
| M&A due diligence | Buyers expect SBOM in data rooms |
| Regulatory compliance | US Executive Order 14028 requires SBOM for federal software suppliers |
| Customer contracts | Enterprise customers increasingly require SBOM delivery |

#### SBOM Standards

| Standard | Maintained By | Format | Best For |
|----------|--------------|--------|----------|
| **SPDX** (Software Package Data Exchange) | Linux Foundation | JSON, YAML, RDF, tag-value | Compliance-focused; ISO/IEC 5962:2021 |
| **CycloneDX** | OWASP | JSON, XML | Security-focused; VEX support |
| **SWID** | NIST | XML | Enterprise IT asset management |

#### SBOM Generation Tools

| Tool | Format | Language/Ecosystem | Notes |
|------|--------|-------------------|-------|
| **Syft** (Anchore) | SPDX, CycloneDX | Multi-language, containers | CLI, free, OSS |
| **FOSSA** | SPDX, CycloneDX | Multi-language | Commercial; policy enforcement |
| **Snyk** | CycloneDX | Multi-language | Combines license + security scanning |
| **Trivy** | SPDX, CycloneDX | Containers, filesystems | Free; good CI/CD integration |
| **Black Duck** | Proprietary | Multi-language | Enterprise; comprehensive |
| **GitHub Dependency Graph** | CycloneDX | GitHub repos | Built-in; export via API |

#### Required SBOM Fields (NTIA Minimum)

1. Supplier name
2. Component name
3. Component version
4. Other unique identifiers (PURL, CPE)
5. Dependency relationships
6. Author of SBOM data
7. Timestamp

---

### OSS Policy Template

```
Open Source Software Policy — [Company Name]

1. Purpose
   This policy governs the use, contribution to, and distribution of
   open source software at [Company].

2. Approved License Categories
   GREEN (approved for use without review):
   - MIT, BSD 2/3-Clause, ISC, Apache 2.0, CC0

   YELLOW (legal review required before use):
   - LGPL, MPL 2.0, EPL 2.0, EUPL
   - Any license not on this list

   RED (prohibited without explicit legal approval):
   - GPL v2, GPL v3, AGPL v3, SSPL, BUSL
   - Any license with field-of-use restrictions
   - "Non-commercial" licenses (CC-BY-NC, etc.)

3. Compliance Process
   a. Developer identifies OSS component and license
   b. Check against approved list (GREEN = proceed)
   c. YELLOW/unknown = submit for legal review via [process]
   d. RED = do not use; seek alternative or get exception
   e. Approved components added to SBOM

4. Contribution Policy
   Employees may contribute to OSS projects subject to:
   - Manager approval
   - Legal review if contribution involves company IP
   - Not during company time without manager approval
   - CLA/DCO signed if required by project

5. AI-Generated Code
   See Section 7 (AI-Generated Code IP Considerations).

6. Obligations Tracking
   All OSS dependencies tracked in company SBOM.
   License obligations documented in NOTICES file.
   SBOM updated on every release.
```

---

### AI-Generated Code IP Considerations

#### Copyright Status of AI-Generated Code

| Jurisdiction | Current Position | Key Cases/Guidance |
|-------------|-----------------|-------------------|
| **United States** | No copyright for purely AI-generated works; requires human authorship | US Copyright Office: Thaler v. Perlmutter (2023); Copyright Guidance (2023) |
| **European Union** | Human authorship required; AI tool treated like camera | No specific legislation yet; default copyright principles apply |
| **United Kingdom** | "Computer-generated works" provision (CDPA s.9(3)) — uncertain if it applies to modern LLMs | UKIPO consultation ongoing |
| **China** | Courts have found copyright in AI-assisted works where human creativity is evident | Beijing Internet Court, 2023 |
| **Practical implication** | Code with significant human contribution (prompting, editing, selection) likely protectable | Document human creative involvement |

#### Training Data License Implications

| Concern | Status | Risk Level |
|---------|--------|-----------|
| Model trained on GPL/LGPL code | Pending — GitHub Copilot litigation | Medium-High for verbatim reproduction |
| Model reproducing copyrighted code | Active litigation (GitHub Copilot class action) | Medium — verbatim copying riskier than influenced code |
| Training data scraping | Multiple lawsuits (NYT v. OpenAI; Getty v. Stability AI) | Medium — fair use defense being tested |
| Indemnification by AI vendors | GitHub Copilot, Amazon CodeWhisperer offer limited indemnification | Read terms carefully |

#### AI Code Assistant Usage Policies

```
AI Code Assistant Policy

Approved Tools: [List approved tools — e.g., GitHub Copilot (Enterprise), Amazon CodeWhisperer]
Prohibited: [List prohibited tools — e.g., tools without enterprise agreements]

Rules:
1. NEVER input trade secrets, proprietary algorithms, or confidential data as prompts
2. NEVER input customer data or PII as context
3. Review all AI-generated code before committing — treat as untrusted input
4. For GPL/copyleft license-sensitive areas: disable AI suggestions or use tools with indemnification
5. Document significant AI contributions in commit messages for IP tracking
6. AI-generated code must pass same code review and testing as human-written code
7. Company owns all work product including AI-assisted code (employment agreement applies)
```

#### Best Practices for AI-Assisted Development

| Practice | Why |
|----------|-----|
| Treat AI output as starting point, not final code | Reduces verbatim reproduction risk |
| Materially modify AI-generated code | Increases human authorship contribution |
| Use AI tools with enterprise agreements | Access to vendor indemnification |
| Disable AI in highly proprietary/sensitive modules | Reduce exposure of trade secrets via prompts |
| Log significant AI contributions | Supports IP ownership claims and audit trails |

---

### Open Source Contribution Guidelines

#### CLA vs DCO

| Mechanism | CLA (Contributor License Agreement) | DCO (Developer Certificate of Origin) |
|-----------|-------------------------------------|---------------------------------------|
| **What it is** | Legal agreement transferring or licensing IP to the project | Developer's certification that they have the right to submit code |
| **How it works** | Signed document (often via GitHub bot) | `Signed-off-by:` tag in commit message |
| **IP transfer** | Can require IP assignment to foundation/company | No IP transfer — certifies original authorship |
| **Employer obligations** | Check employment contract — employer may own IP and need to sign | Employee certifies right to contribute on their own |
| **Common examples** | Apache Software Foundation CLA, Google CLA | Linux kernel, GitLab, CNCF projects |
| **Friction** | Higher — separate document signing | Lower — just a commit message line |

**Before contributing to OSS from a company context**:
1. Review employment agreement — does it assign IP created during employment?
2. Get manager/legal approval if using company time or resources
3. If project requires CLA and contribution is company IP — company representative may need to sign
4. Use DCO where possible to minimize friction

---

### OSS Risk Assessment Framework

| Risk Dimension | Assessment Criteria | Risk Level |
|----------------|---------------------|-----------|
| **License risk** | Permissive = Low; Weak copyleft = Medium; Strong copyleft/AGPL = High | Score each dependency |
| **Community health** | Active maintainers, recent commits, >1 maintainer, responsive to issues | Check GitHub metrics |
| **Maintenance risk** | Last commit date, open critical issues, number of dependents | Abandoned = High risk |
| **Security history** | CVE count, time-to-patch, security policy existence | Review OSV.dev |
| **Popularity/adoption** | Download count, stars, used by known companies | Proxy for quality |
| **Upstream dependency risk** | Depth of dependency tree; transitive license risks | Use SBOM tool |

**Risk Decision Matrix**:
- High license risk + High maintenance risk = **Avoid or architect around**
- High license risk + Low maintenance risk = **Legal review required**
- Low license risk + High maintenance risk = **Find alternative or fork**
- Low license risk + Low maintenance risk = **Proceed with standard SBOM tracking**
