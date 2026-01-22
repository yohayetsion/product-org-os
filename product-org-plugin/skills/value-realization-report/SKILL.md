---
name: value-realization-report
description: Create value realization report
argument-hint: [customer, cohort, or product]
---

Create a **Value Realization Report** for the specified customer, cohort, or product.

## V2V Phase
**Phase 5: Business & Customer Outcomes** - This skill measures whether customers achieved value.

## Output Structure

### 1. Executive Summary
- Scope of analysis
- Key findings
- Overall value realization score
- Priority recommendations

### 2. Value Delivered vs. Promised

| Value Promise | Promised Outcome | Actual Outcome | Gap |
|---------------|------------------|----------------|-----|
| [Promise 1] | [Promised] | [Actual] | +/-X% |
| [Promise 2] | [Promised] | [Actual] | +/-X% |
| [Promise 3] | [Promised] | [Actual] | +/-X% |

### 3. Adoption Metrics

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Active users | X | X | 🟢/🟡/🔴 |
| Feature adoption | X% | X% | 🟢/🟡/🔴 |
| Usage frequency | X/week | X/week | 🟢/🟡/🔴 |
| Use cases activated | X | X | 🟢/🟡/🔴 |

### 4. Customer Health Scores

| Customer/Segment | Health Score | Trend | Risk Level |
|------------------|--------------|-------|------------|
| [Customer 1] | X/100 | ↑/↓/→ | Low/Med/High |
| [Customer 2] | X/100 | ↑/↓/→ | Low/Med/High |

### 5. ROI Analysis

**For Customer:**
- Investment: $X (license + implementation + training)
- Value realized: $X (cost savings + revenue impact)
- ROI: X%
- Payback period: X months

**Calculation methodology:**
- [How value was calculated]

### 6. Success Stories

#### [Customer Name]
- **Challenge:** [What problem they had]
- **Solution:** [How they used the product]
- **Results:** [Quantified outcomes]
- **Quote:** "[Customer quote]"

### 7. Risk Areas

| Risk | Customers Affected | Impact | Mitigation |
|------|-------------------|--------|------------|
| Low adoption | X customers | High/Med/Low | [Action] |
| Missing use case | X customers | High/Med/Low | [Action] |
| Champion left | X customers | High/Med/Low | [Action] |

### 8. Recommendations

**Immediate (This Week):**
1. [Action item]

**Short-term (This Month):**
1. [Action item]

**Long-term (This Quarter):**
1. [Action item]

### 9. Learnings for Product

| Learning | Evidence | Recommended Action |
|----------|----------|-------------------|
| [Learning 1] | [Data/feedback] | [Action] |
| [Learning 2] | [Data/feedback] | [Action] |

## Instructions

1. Ask about scope (customer, cohort, product) if not specified
2. Reference any customer data or success criteria documents via @file syntax
3. Be honest about gaps in value delivery
4. Include actionable recommendations
5. Save as markdown file
6. Offer to create presentation version using /present
