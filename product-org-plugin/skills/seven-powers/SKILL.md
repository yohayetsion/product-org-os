---
name: seven-powers
description: |
  Analyze competitive moats and strategic power using Hamilton Helmer's 7 Powers framework.
  Activate when: "seven powers", "7 powers", "moat analysis", "competitive moat", "Helmer", "power dynamics", "strategic power", "defensibility analysis"
  Do NOT activate for: Porter's Five Forces (/porter-five-forces), competitive analysis (/competitive-analysis), SWOT (/swot-analysis)
argument-hint: [company or product] or [update path/to/seven-powers.md]
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: strategy
compatibility: Requires Product Org OS v3+ context layer and rules
---

## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "revise", "refresh" in input | UPDATE | 100% |
| File path provided (`@path/to/seven-powers.md`) | UPDATE | 100% |
| "create", "new", "analyze" in input | CREATE | 100% |
| "find", "search", "list power analyses" | FIND | 100% |
| "the power analysis for [company]", "our moat" | UPDATE | 85% |
| Just a company or product name | CREATE | 60% |

**Threshold**: >=85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Assess all seven powers for the subject company/product, evaluate Benefit and Barrier for each, map power availability to lifecycle stage.

**UPDATE**:
1. Read existing 7 Powers analysis (search if path not provided)
2. Preserve company context and lifecycle stage assessment
3. Update individual power evaluations based on new competitive data
4. Show diff summary: "Updated: [powers re-assessed]. Lifecycle stage: [unchanged/shifted]."

**FIND**:
1. Search paths below for 7 Powers documents
2. Present results: company/product, date, strongest power, path
3. Ask: "Update one of these, or create new?"

### Search Locations

- `strategy/`
- `competitive/`
- `product/`
- `analysis/`

---

## Gotchas

- A power requires BOTH a Benefit AND a Barrier. Having a cost advantage (Benefit) without something preventing competitors from replicating it (Barrier) is NOT a power
- Process Power is the hardest to claim honestly — it requires organizational capabilities that evolved over years, not just good engineering. Most companies claiming Process Power actually have a temporary execution lead
- Counter-Positioning only works when the incumbent's EXISTING business model prevents them from responding. If they CAN copy you without cannibalizing their core, it is not Counter-Positioning
- Do not confuse first-mover advantage with a power. Being first is not a power unless it creates one of the seven (e.g., first-mover creating Network Economies or Switching Costs)

## Vision to Value Phase

**Phase 1: Strategic Foundation** - The 7 Powers framework identifies which strategic powers a company possesses or can build, informing where to invest for long-term defensibility.

**Prerequisites**: Understanding of the company's market position, competitive landscape, and business model
**Outputs used by**: `/strategic-intent` (power-informed strategy), `/strategic-bet` (bets to build or strengthen powers), `/competitive-landscape` (moat-aware competitive view), `/positioning-statement` (power-backed positioning)

## Methodology

<!-- Source: "7 Powers: The Foundations of Business Strategy" — Hamilton Helmer (2016, Deep Strategy LLC). Helmer is a Stanford Economics lecturer and strategy advisor. The framework distills strategy to seven fundamental sources of persistent differential returns. Helmer's key insight: strategy is about achieving and maintaining Power — a condition that creates persistent differential returns vs. competitors. -->

<!-- Source: Power Dynamics — Helmer, Chapter 9-10. Different powers become available at different company lifecycle stages. Counter-Positioning and Cornered Resource emerge during Origination (invention). Scale Economies, Network Economies, and Switching Costs emerge during Takeoff (growth). Branding and Process Power emerge during Stability (maturity). This lifecycle mapping prevents companies from pursuing powers that are not yet available to them. -->

<!-- Source: Inspired by wdavidturner/product-skills seven-powers skill. Adapted with full power definitions, lifecycle mapping, and dual Benefit/Barrier test. -->

### The Dual Test

Every power must pass two tests:

| Test | Question | Without It |
|------|----------|-----------|
| **Benefit** | Does this create superior economics (lower cost OR ability to charge more)? | No value capture advantage |
| **Barrier** | What prevents competitors from replicating this? | Advantage is temporary |

**Both are required.** A Benefit without a Barrier is a fleeting advantage. A Barrier without a Benefit is irrelevant.

### The Seven Powers

#### 1. Scale Economies

**Description**: A business in which per-unit cost declines as production volume increases.

| Aspect | Detail |
|--------|--------|
| **Benefit** | Lower per-unit costs at volume, enabling either higher margins or lower prices |
| **Barrier** | Challenger must achieve comparable scale — requires massive upfront investment with uncertain returns |
| **Industry conditions** | Fixed costs are a significant portion of total costs; winner-take-most dynamics |
| **Examples** | Intel (chip fabrication), Netflix (content amortization), AWS (infrastructure) |
| **Warning signs** | Only meaningful when the cost curve is steep enough that scale differences create real cost gaps |

#### 2. Network Economies

**Description**: The value of a product or service increases as more users adopt it.

| Aspect | Detail |
|--------|--------|
| **Benefit** | Each additional user increases the value for all existing users, enabling higher willingness-to-pay or lower churn |
| **Barrier** | A challenger must somehow attract users away from a network that is inherently more valuable due to size |
| **Industry conditions** | Product value is fundamentally tied to number of users or participants |
| **Examples** | LinkedIn (professional network), Visa (merchant/cardholder network), Uber (driver/rider network) |
| **Warning signs** | Multi-homing (users on multiple networks) weakens this power; local vs. global network effects matter |

#### 3. Counter-Positioning

**Description**: A newcomer adopts a superior business model that the incumbent cannot copy because it would damage their existing business.

| Aspect | Detail |
|--------|--------|
| **Benefit** | Superior business model creates better unit economics, customer experience, or value proposition |
| **Barrier** | Incumbent faces collateral damage to existing profitable business if they respond; their rational choice is to NOT copy |
| **Industry conditions** | Incumbent has a profitable business model that would be cannibalized by the new approach |
| **Examples** | Vanguard (low-cost index funds vs. active management fees), Netflix streaming (vs. Blockbuster stores), Tesla (DTC vs. dealer networks) |
| **Warning signs** | Temporary — expires when the incumbent's legacy business erodes enough that they have nothing left to protect |

#### 4. Switching Costs

**Description**: The value loss a customer would experience by switching to an alternative product.

| Aspect | Detail |
|--------|--------|
| **Benefit** | Customers stay even when alternatives exist, enabling pricing power and predictable revenue |
| **Barrier** | Challenger must offer enough incremental value to overcome the customer's switching costs (financial, procedural, relational) |
| **Industry conditions** | Deep integration into customer workflows, data lock-in, retraining costs, or contractual obligations |
| **Examples** | Salesforce (CRM data + workflow integration), SAP (ERP embedded in operations), Apple (ecosystem lock-in) |
| **Warning signs** | Switching costs that rely on artificial lock-in (vs. genuine integration value) breed resentment and eventual churn |

#### 5. Branding

**Description**: A durable attribution of higher value to an objectively identical offering, based on historical information about the seller.

| Aspect | Detail |
|--------|--------|
| **Benefit** | Ability to charge a price premium for an objectively comparable product, or achieve higher conversion at equal price |
| **Barrier** | Brand is built over long periods through consistent delivery; it cannot be quickly replicated by spending money |
| **Industry conditions** | Purchase decisions involve uncertainty, signaling, or emotional factors beyond pure functionality |
| **Examples** | Tiffany (jewelry premium), Apple (consumer electronics premium), McKinsey (consulting premium) |
| **Warning signs** | Brand power is weaker in B2B commodity categories where purchasing decisions are highly rational and specification-driven |

#### 6. Cornered Resource

**Description**: Preferential access at attractive terms to a coveted asset that independently enhances value.

| Aspect | Detail |
|--------|--------|
| **Benefit** | The resource directly creates value that competitors cannot replicate |
| **Barrier** | The resource is scarce and the company has preferential access (talent, patents, licenses, data, relationships) |
| **Industry conditions** | A specific resource is both rare and value-creating; access cannot be easily replicated |
| **Examples** | Pixar (creative talent cluster), De Beers (diamond supply agreements), certain pharma patents |
| **Warning signs** | Resources are only "cornered" if competitors genuinely cannot acquire equivalent resources; talent can leave, patents expire |

#### 7. Process Power

**Description**: Embedded company organization and activity sets that enable lower costs and/or superior product, which can only be matched by an extended commitment.

| Aspect | Detail |
|--------|--------|
| **Benefit** | Superior execution creating either lower costs or better product quality |
| **Barrier** | Process Power emerges from years of organizational learning; it cannot be bought, copied, or shortcut |
| **Industry conditions** | Complex, multi-step processes where organizational learning compounds over time |
| **Examples** | Toyota (Toyota Production System), TSMC (chip fabrication yields), Bridgewater (investment process) |
| **Warning signs** | The rarest and hardest to honestly claim; most "Process Power" claims are actually temporary execution leads |

### Power Availability by Lifecycle Stage

| Lifecycle Stage | Available Powers | Company Phase |
|----------------|-----------------|---------------|
| **Origination** (invention) | Counter-Positioning, Cornered Resource | Pre-product-market fit, early innovation |
| **Takeoff** (growth) | Scale Economies, Network Economies, Switching Costs | Rapid growth, market expansion |
| **Stability** (maturity) | Branding, Process Power | Market leadership, optimization |

**Key insight**: You cannot build Scale Economies before you have scale. You cannot build Branding before sustained market presence. Pursue powers that match your lifecycle stage.

### Helmer's Strategy Equation

> **Strategy = Route to continuing Power in significant markets**

This means:
- **Route**: An executable path, not a wish
- **Continuing**: Durable, not temporary
- **Power**: One of the seven, with both Benefit and Barrier
- **Significant markets**: Large enough to matter

## Output Structure

```markdown
# 7 Powers Analysis: [Company/Product]

**Date**: [YYYY-MM-DD]
**Owner**: [Who owns this analysis]
**Lifecycle Stage**: [Origination / Takeoff / Stability]
**Primary Power**: [Strongest power, if any]

---

## Company Context

**Company**: [Name]
**Market**: [Primary market]
**Stage**: [Origination / Takeoff / Stability]
**Business model**: [Brief description]

---

## Power Assessment

### 1. Scale Economies

| Test | Assessment |
|------|-----------|
| **Benefit present?** | [Yes/No — describe cost advantage from scale] |
| **Barrier present?** | [Yes/No — describe what prevents competitors from achieving same scale] |
| **Power exists?** | [Yes / Emerging / No] |

**Evidence**: [Specific evidence supporting or refuting this power]
**Strength**: [Strong / Moderate / Weak / Absent]

### 2. Network Economies

| Test | Assessment |
|------|-----------|
| **Benefit present?** | [Yes/No — describe value increase from user growth] |
| **Barrier present?** | [Yes/No — describe network advantage competitors cannot replicate] |
| **Power exists?** | [Yes / Emerging / No] |

**Evidence**: [Specific evidence]
**Strength**: [Strong / Moderate / Weak / Absent]

### 3. Counter-Positioning

| Test | Assessment |
|------|-----------|
| **Benefit present?** | [Yes/No — describe superior business model economics] |
| **Barrier present?** | [Yes/No — describe why incumbents cannot respond without self-damage] |
| **Power exists?** | [Yes / Emerging / No] |

**Evidence**: [Specific evidence]
**Strength**: [Strong / Moderate / Weak / Absent]

### 4. Switching Costs

| Test | Assessment |
|------|-----------|
| **Benefit present?** | [Yes/No — describe customer retention advantage] |
| **Barrier present?** | [Yes/No — describe what makes switching costly for customers] |
| **Power exists?** | [Yes / Emerging / No] |

**Evidence**: [Specific evidence]
**Strength**: [Strong / Moderate / Weak / Absent]

### 5. Branding

| Test | Assessment |
|------|-----------|
| **Benefit present?** | [Yes/No — describe pricing premium or conversion advantage] |
| **Barrier present?** | [Yes/No — describe time/effort required to build equivalent brand] |
| **Power exists?** | [Yes / Emerging / No] |

**Evidence**: [Specific evidence]
**Strength**: [Strong / Moderate / Weak / Absent]

### 6. Cornered Resource

| Test | Assessment |
|------|-----------|
| **Benefit present?** | [Yes/No — describe value from the resource] |
| **Barrier present?** | [Yes/No — describe why competitors cannot access equivalent resource] |
| **Power exists?** | [Yes / Emerging / No] |

**Evidence**: [Specific evidence]
**Strength**: [Strong / Moderate / Weak / Absent]

### 7. Process Power

| Test | Assessment |
|------|-----------|
| **Benefit present?** | [Yes/No — describe execution advantage from organizational processes] |
| **Barrier present?** | [Yes/No — describe why competitors cannot replicate the process quickly] |
| **Power exists?** | [Yes / Emerging / No] |

**Evidence**: [Specific evidence]
**Strength**: [Strong / Moderate / Weak / Absent]

---

## Power Summary

| Power | Benefit | Barrier | Exists? | Strength | Lifecycle Match |
|-------|---------|---------|---------|----------|----------------|
| Scale Economies | [Y/N] | [Y/N] | [Y/E/N] | [S/M/W/A] | [Yes/No — available at current stage?] |
| Network Economies | [Y/N] | [Y/N] | [Y/E/N] | [S/M/W/A] | [Yes/No] |
| Counter-Positioning | [Y/N] | [Y/N] | [Y/E/N] | [S/M/W/A] | [Yes/No] |
| Switching Costs | [Y/N] | [Y/N] | [Y/E/N] | [S/M/W/A] | [Yes/No] |
| Branding | [Y/N] | [Y/N] | [Y/E/N] | [S/M/W/A] | [Yes/No] |
| Cornered Resource | [Y/N] | [Y/N] | [Y/E/N] | [S/M/W/A] | [Yes/No] |
| Process Power | [Y/N] | [Y/N] | [Y/E/N] | [S/M/W/A] | [Yes/No] |

---

## Power Progression Plan

### Current Powers (Defend)
| Power | Threat to Power | Defense Strategy |
|-------|----------------|-----------------|
| [Current power] | [What could erode it] | [How to protect] |

### Emerging Powers (Invest)
| Power | Current Gap | Investment Needed | Timeline |
|-------|-----------|-------------------|----------|
| [Emerging power] | [What is missing for full Benefit + Barrier] | [What to invest in] | [Lifecycle-appropriate?] |

### Unavailable Powers (Do Not Pursue Yet)
| Power | Why Unavailable | When It Becomes Available |
|-------|----------------|-------------------------|
| [Power] | [Lifecycle mismatch or structural reason] | [What must change] |

---

## Strategic Implications

### Route to Power
[Based on the analysis, what is the company's most viable route to continuing power in its significant market?]

### Key Risks
| Risk | Impact on Power | Mitigation |
|------|----------------|-----------|
| [Risk 1] | [Which power it threatens] | [How to mitigate] |
| [Risk 2] | [Which power] | [Mitigation] |

### Competitor Power Comparison (Optional)

| Power | Us | Competitor A | Competitor B |
|-------|----|-------------|-------------|
| Scale Economies | [Strength] | [Strength] | [Strength] |
| Network Economies | [Strength] | [Strength] | [Strength] |
| Counter-Positioning | [Strength] | [Strength] | [Strength] |
| Switching Costs | [Strength] | [Strength] | [Strength] |
| Branding | [Strength] | [Strength] | [Strength] |
| Cornered Resource | [Strength] | [Strength] | [Strength] |
| Process Power | [Strength] | [Strength] | [Strength] |

## Assumptions to Validate

| # | Assumption | Power | Validation Method | Impact if Wrong |
|---|-----------|-------|------------------|-----------------|
| 1 | [Assumption] | [Power] | [Method] | High/Med/Low |
| 2 | [Assumption] | [Power] | [Method] | High/Med/Low |

## Next Steps

- [ ] Validate power assessments with competitive data via `/competitive-landscape`
- [ ] Frame power-building initiatives as strategic bets via `/strategic-bet`
- [ ] Build business case for power investments via `/business-case`
- [ ] Map competitive moat comparisons via `/competitive-analysis`
- [ ] Save analysis to context registry via `/context-save`
```

## Instructions

1. Start by understanding the company's lifecycle stage (Origination, Takeoff, or Stability) — this determines which powers are available
2. **Check prior context**: Run `/context-recall [company name]` for existing competitive analysis and strategic decisions
3. Assess ALL seven powers, even those that clearly do not apply — the exercise reveals blind spots and prevents confirmation bias
4. For each power, apply the dual test: does the Benefit exist AND does the Barrier exist?
5. Be rigorous — most companies have 0-2 real powers. Claiming more typically means the bar is too low
6. Map power availability to lifecycle stage — do not recommend building powers that are not yet available
7. Identify the most viable route to continuing power in a significant market
8. Save output as markdown file
9. Offer `/strategic-bet` to frame power-building as a strategic bet

## Integration

- Links to `/strategic-intent` (power analysis informs strategic direction)
- Links to `/strategic-bet` (frame power-building as bets)
- Links to `/competitive-landscape` (moat-aware competitive mapping)
- Links to `/competitive-analysis` (deep competitive comparison)
- Links to `/positioning-statement` (power-backed positioning)
- Links to `/porter-five-forces` (complementary industry structure analysis)
- Links to `/business-case` (investment case for building powers)
- Links to `/context-save` (save power assessment to organizational memory)
