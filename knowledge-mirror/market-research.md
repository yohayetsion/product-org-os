# Market Research Knowledge Pack

Knowledge pack for research-facing agents (Market Researcher, CMO, Marketing Director, Growth Marketer). Contains real frameworks for competitive analysis, market sizing, customer research, and insight synthesis.

**Version**: 1.0
**Type**: knowledge-pack
**Primary Users**: @market-researcher, @cmo, @marketing-dir, @growth-marketer

---
<!-- Attribution:
  Frameworks and patterns in this knowledge pack were informed by:
  - Anthropic knowledge-work-plugins (marketing/competitive-brief)
  Adapted and expanded for Product Org OS agents.
-->

## Market Research Methods Matrix

### Qualitative vs. Quantitative

**When to use which:**

| Method Type | Use When | Output | Limitation |
|-------------|---------|--------|-----------|
| **Qualitative** | You don't know what to ask yet; need to discover language, motivations, or unexpected themes | Rich narratives, hypotheses, "why" explanations | Not statistically generalizable; researcher bias risk |
| **Quantitative** | You have a hypothesis to test; need to measure prevalence, size, or statistical confidence | Numbers, percentages, statistical significance | Tells you what, not why; survey design heavily influences results |

**Mixed methods — best of both:**
```
Phase 1 (Qualitative): 8-12 in-depth interviews → discover themes and language
Phase 2 (Quantitative): 150-500 respondent survey → test prevalence of themes
Phase 3 (Qualitative): Follow-up sessions → explain surprising quantitative findings
```

### Method Selection by Research Question

| Research Question | Best Method | Alternatives |
|-----------------|-------------|-------------|
| What problems do customers actually have? | Customer interviews | Ethnography, job-to-be-done sessions |
| How large is this market? | Secondary research + top-down modeling | Bottom-up estimation, analyst reports |
| Why did we lose that deal? | Win/loss interview | Sales debrief, CRM analysis |
| Which message resonates more? | A/B test | Survey, focus group |
| What features do users want? | Contextual inquiry | Survey, usability testing |
| How are we perceived vs. competitors? | Brand perception survey | Social listening, review mining |
| What is the competitive landscape? | Competitive analysis | Analyst reports, customer interviews |
| How satisfied are customers? | NPS survey + follow-up interviews | CSAT, CES, retention analysis |

---

## Competitive Analysis Framework

### Competitor Classification

**When to use**: Mapping the competitive landscape before any competitive analysis. Not all competitors warrant the same attention.

| Tier | Definition | Analysis Depth | Review Frequency |
|------|-----------|----------------|-----------------|
| **Tier 1 — Direct** | Same product, same market, same buyer | Deep: full feature, pricing, GTM, positioning review | Monthly |
| **Tier 2 — Adjacent** | Similar product or overlapping buyers, different core use case | Medium: positioning, messaging, customer overlap | Quarterly |
| **Tier 3 — Indirect** | Alternative approach to the same problem (including "do nothing") | Light: awareness, strategic monitoring | Semi-annually |
| **Tier 4 — Emerging** | New entrants or adjacent players showing early signals | Watch list: news alerts, funding announcements | As news occurs |

### Competitive Analysis Dimensions

**For each Tier 1/2 competitor, analyze:**

| Dimension | What to Research | Sources |
|-----------|-----------------|---------|
| **Product** | Feature set, strengths/weaknesses, recent releases, roadmap signals | Product website, G2/Capterra, customer reviews, trial |
| **Pricing** | Model, tiers, packaging, discounting signals | Pricing page, sales intel, customer conversations |
| **Positioning** | Value prop, target segment, messaging pillars | Homepage, ads, content marketing |
| **GTM motion** | PLG vs. SLG, channels, sales cycle length | Job postings, press releases, partner ecosystem |
| **Traction** | Revenue signals, customer count, growth rate | Funding press, analyst reports, employee count |
| **Team** | Leadership, hiring patterns, org structure signals | LinkedIn, job postings |
| **Weaknesses** | Customer complaints, missing features, support issues | G2 reviews (1-3 stars), Reddit, sales call notes |
| **Differentiators** | What they genuinely do better than anyone else | Honest internal assessment |

---

### Competitive Brief Template

**When to use**: Creating a structured competitive brief for a specific competitor or product category.

```
COMPETITIVE BRIEF

Competitor: [Company name]
Date: [YYYY-MM-DD]
Author: [Name / Team]
Review cycle: [Monthly / Quarterly]

--- OVERVIEW ---
What they do: [1-2 sentence description of their product]
Target buyer: [Role, company size, industry]
Founded / Funded: [Year founded, last funding round and amount]
Employee count: [Approximate, from LinkedIn]
Estimated ARR / Revenue: [If known or estimable from public signals]

--- POSITIONING ---
Primary value proposition: [Their headline claim — verbatim from homepage if possible]
Target segment emphasis: [Who they claim to serve / who they actually serve]
Key differentiators (their claims):
  1. [Claim 1]
  2. [Claim 2]
  3. [Claim 3]
Messaging tone: [Technical / Accessible / Enterprise / Startup]

--- PRODUCT ---
Core capabilities:
  - [Feature/capability 1]
  - [Feature/capability 2]
  - [Feature/capability 3]
Notable strengths (validated by customer evidence):
  - [Strength + source]
Notable weaknesses (validated by customer evidence):
  - [Weakness + source]
Recent product news: [Last 2-3 releases or announcements]
Roadmap signals: [Any public hints about direction]

--- PRICING ---
Model: [Per seat / Usage-based / Flat rate / Freemium / etc.]
Tiers: [Describe tiers with prices if public]
Free tier / trial: [Yes/No — details]
Typical deal size (if known): [SMB / Mid-market / Enterprise range]
Discounting signals: [Any known patterns from sales intel]

--- GTM ---
Primary sales motion: [PLG / SLG / Partner-led / Channel]
Key channels: [Paid search, content, events, partnerships, etc.]
Content strategy: [What they write about, how frequently]
Partnerships: [Key integration or reseller partners]
Events: [Conferences they sponsor or speak at]
Job postings insight: [What hiring patterns reveal about strategy]

--- CUSTOMER PROFILE ---
Known customers: [Notable logos or categories]
Customer reviews summary (G2/Capterra):
  - What customers love: [Top 2-3 themes from positive reviews]
  - What customers complain about: [Top 2-3 themes from negative reviews]
  - Rating: [Overall score / category rank]

--- OUR ASSESSMENT ---
Where we win against them:
  1. [Win condition 1]
  2. [Win condition 2]
Where they win against us:
  1. [Their advantage 1]
  2. [Their advantage 2]
Battlecard summary: [2-3 sentence positioning vs. this competitor]
Win rate vs. this competitor: [% if tracked in CRM]
```

---

## Market Sizing Methods

### TAM / SAM / SOM Framework

**When to use**: Business cases, fundraising, strategic planning, market entry decisions.

**Definitions:**

| Term | Definition | How to Estimate |
|------|-----------|----------------|
| **TAM** (Total Addressable Market) | The full revenue opportunity if you captured 100% of the market | Top-down: analyst reports × price. Bottom-up: total potential customers × ARPU |
| **SAM** (Serviceable Addressable Market) | The portion of TAM your product/GTM can actually reach | TAM × (% of customers you can serve with current product and channels) |
| **SOM** (Serviceable Obtainable Market) | Realistic market share you can capture in 3-5 years | SAM × realistic market share (5-15% is typical early-stage target) |

### Top-Down vs. Bottom-Up Sizing

**Top-down (analyst-sourced):**
```
Method:
  1. Find an analyst report on the market size (Gartner, IDC, Forrester, IBISWorld)
  2. Apply filters to narrow to your segment (geography, company size, use case)
  3. Apply your ARPU to derive revenue potential
  4. Apply realistic market share assumptions for SOM

Limitation: Analyst definitions rarely match your exact product. Often overstates TAM.
Best for: Board decks, fundraising (investors expect it)
```

**Bottom-up (demand-sourced):**
```
Method:
  1. Define your ICP precisely (company size, industry, geography, role)
  2. Count the number of ICP companies (e.g., LinkedIn Sales Navigator, Clearbit, ZoomInfo)
  3. Estimate penetration rate (what % of ICP would buy your product)
  4. Multiply by expected ARPU

Limitation: Requires accurate ICP definition and reliable company data
Best for: Go-to-market planning, sales territory sizing, channel investment decisions
```

**Best practice:** Run both methods and reconcile. If they diverge significantly, investigate why.

---

## Customer Research Methods

### Interviews

**When to use**: Understanding motivations, decision-making processes, pain points, and language. Best for discovery and hypothesis generation.

**Interview design principles:**

| Principle | Rule |
|-----------|------|
| **Open questions first** | Ask "Tell me about..." before "Do you...?" |
| **No leading questions** | "How painful is X?" implies X is painful. Ask "What's your experience with X?" |
| **Follow the energy** | When respondents get animated, go deeper |
| **5 Whys technique** | Ask "why" 4-5 times to reach root causes |
| **Silence is data** | Don't fill pauses — let respondents finish their thought |
| **Avoid confirming bias** | Record and analyze before concluding, not during |

**Interview guide template:**

```
INTERVIEW GUIDE — [Topic]
Duration: 45-60 minutes

Opening (5 min):
  - Thank respondent and set expectations
  - "I'm trying to learn, not sell. There are no right answers."
  - Confirm recording permission

Background (5-10 min):
  - Walk me through your role and what a typical [day/week] looks like.
  - What's the biggest challenge your team faces right now?

Problem exploration (20-25 min):
  - Tell me about the last time you dealt with [problem area].
  - What triggered that? What happened next?
  - What did you try? What worked, what didn't?
  - What would an ideal outcome look like?

Current solutions (10-15 min):
  - What tools or approaches do you currently use for [problem]?
  - What do you like most about how you handle it today?
  - If you could change one thing about your current approach, what would it be?

Decision process (5-10 min, if applicable):
  - When you evaluate new solutions in this area, who's involved?
  - What's most important to you when making a decision like that?

Closing (5 min):
  - Is there anything I should have asked but didn't?
  - Who else should I talk to about this?
```

**Sample sizes:**
- Discovery / Generative: 8-15 interviews (patterns emerge quickly)
- Validation: 15-25 interviews (more confidence in findings)
- Niche or rare audience: 5-8 may be sufficient if access is limited

---

### Surveys

**When to use**: Validating hypotheses at scale, measuring satisfaction, sizing preferences.

**Survey design best practices:**

| Best Practice | Detail |
|--------------|--------|
| **Start with the goal** | Define what decision this survey must inform before writing a single question |
| **Keep it under 10 minutes** | Response quality degrades sharply after 10 minutes |
| **One question per question** | "How useful and easy to use is X?" = two questions |
| **Use established scales** | Likert (1-7), NPS (0-10), or semantic differential for consistency |
| **Randomize answer orders** | For multiple choice, rotate options to avoid primacy/recency bias |
| **Neutral midpoint** | Include "Neither agree nor disagree" to avoid forcing opinions |
| **Screen early** | Put qualifying questions first; don't waste qualified respondents' time |
| **Test the survey** | Run a 5-person pilot before full deployment |

**Question type guide:**

| Question Type | Use For | Example |
|--------------|---------|---------|
| **Open text** | Discovering unexpected themes, quotes | "What is the biggest challenge you face with X?" |
| **Likert scale** | Measuring attitudes and agreement | "I find X easy to use: 1 (Strongly disagree) → 7 (Strongly agree)" |
| **NPS** | Measuring loyalty, benchmarking | "How likely are you to recommend X to a colleague? (0-10)" |
| **Ranking** | Prioritizing features or attributes | "Rank these 5 factors from most to least important" |
| **Multiple choice (single)** | Categorical classification | "Which best describes your role?" |
| **Multiple choice (multi)** | Non-exclusive options | "Which of these tools do you currently use? (Select all that apply)" |
| **Matrix** | Rating multiple items on same scale | Rating 5 features on the same 1-5 scale |

**Sample size guidelines (for ±5% margin of error at 95% confidence):**

| Population Size | Required Sample |
|----------------|----------------|
| < 1,000 | ~278 |
| 1,000-10,000 | ~370 |
| 10,000-100,000 | ~383 |
| 100,000+ | ~384 |

**Limitations**: Survey responses reflect stated preferences, not actual behavior. Behavioral data (product analytics, A/B tests) is more reliable for understanding what people actually do.

---

### Focus Groups

**When to use**: Exploring reactions to concepts, messages, or prototypes in a social setting where group dynamics surface issues interviews might miss.

**When NOT to use**: Measuring prevalence of opinions (group dynamics bias individual responses), or validating specific hypotheses (not statistically valid).

**Best practices:**
- 6-8 participants per group (smaller = more depth, larger = harder to manage)
- Homogeneous groups (same role, company size) produce richer discussion
- Use a trained moderator — group dynamics require active management
- Run 2-3 groups minimum before drawing conclusions (one group = anecdote)
- Separate concept reaction from feature prioritization (different session goals)

---

## Win/Loss Analysis Framework

**When to use**: Understanding competitive win and loss patterns. One of the highest-ROI research activities for B2B companies.

### Win/Loss Interview Process

**When to interview:**
- Within 2-4 weeks of close (when memory is fresh)
- Target: 20-30 win/loss interviews per quarter for meaningful patterns

**Who to interview:**
- Decision maker and/or champion (not just the deal contact)
- For losses: interview even if they chose a competitor (especially if they chose a competitor)

**Win/Loss interview guide:**

```
Opening:
  - Thank them; clarify this is for product improvement, not re-selling
  - Confirm this is off the record (encourages candor)

Decision context:
  - Walk me through your evaluation process from the start.
  - Who was involved in the decision? What did each person care about most?
  - What problem were you ultimately trying to solve?

Evaluation criteria:
  - What were the 3-5 most important factors in your decision?
  - How did you weight them? (Not all criteria are equal)
  - Were there any must-haves that were non-negotiable?

Competitive comparison:
  - Which other solutions did you evaluate seriously?
  - How did you perceive the differences between [our product] and [competitor]?
  - Where did [our product] stand out? Where did others?

Decision moment:
  - What was the decisive factor? What tipped it?
  - Was price a significant factor? How so?
  - Were there any concerns that almost changed your decision?

Feedback:
  - What would you tell our product team about what matters most to buyers like you?
  - Is there anything we didn't do well in the sales process?
```

**Win/Loss analysis output:**

| Dimension | Questions to Answer |
|-----------|-------------------|
| Win rate by competitor | Where do we win and lose consistently? |
| Win criteria | What 3-5 factors drive wins most often? |
| Loss criteria | What 3-5 factors drive losses most often? |
| Segment patterns | Do patterns differ by company size, industry, or deal size? |
| Sales process issues | Do losses reflect product gaps or process/message failures? |
| Pricing sensitivity | How often does price appear in loss reasons? |

---

## Industry Analysis Template (Porter's Five Forces Application)

**When to use**: Assessing structural attractiveness of a market before major investment or entry.

```
INDUSTRY ANALYSIS — [Industry/Market Name]
Date: [YYYY-MM-DD]

--- FORCE 1: COMPETITIVE RIVALRY ---
Intensity: [Low / Medium / High]
Evidence:
  - Number of direct competitors: [N]
  - Market share distribution: [Fragmented / Concentrated / Duopoly]
  - Growth rate: [Market growing / flat / declining]
  - Product differentiation: [High / Low — commoditized?]
  - Exit barriers: [High (sticky, high switching costs) / Low]
Implication: [What does rivalry level mean for your strategy?]

--- FORCE 2: THREAT OF NEW ENTRANTS ---
Intensity: [Low / Medium / High]
Barriers to entry (assess each):
  - Capital requirements: [High / Low]
  - Regulatory requirements: [Significant / Minimal]
  - Switching costs for customers: [High / Low]
  - Network effects: [Strong / Weak]
  - Brand loyalty / established relationships: [Strong / Weak]
  - Access to distribution: [Difficult / Easy]
Implication: [Are new entrants a material threat?]

--- FORCE 3: THREAT OF SUBSTITUTES ---
Intensity: [Low / Medium / High]
Key substitutes:
  - [Substitute 1]: [How it competes; switching cost]
  - [Substitute 2]: [How it competes; switching cost]
"Do nothing" option: [How often and why buyers choose status quo]
Implication: [How easily could buyers replace your product category?]

--- FORCE 4: BUYER POWER ---
Intensity: [Low / Medium / High]
Evidence:
  - Buyer concentration: [Few large buyers / Many small buyers]
  - Switching costs: [High (buyers are locked in) / Low]
  - Price sensitivity: [High / Low]
  - Buyer information: [Well-informed / Limited visibility]
  - Backward integration risk: [Build vs. buy risk]
Implication: [How much pricing power do you have?]

--- FORCE 5: SUPPLIER POWER ---
Intensity: [Low / Medium / High]
Key suppliers: [Cloud providers, data vendors, key technology partners]
Evidence:
  - Concentration of suppliers: [Few / Many alternatives]
  - Switching costs from supplier: [High / Low]
  - Unique/differentiated inputs: [Yes / No]
  - Forward integration risk: [Could supplier become a competitor?]
Implication: [Do suppliers constrain your margins or operations?]

--- OVERALL ASSESSMENT ---
Industry attractiveness: [Attractive / Neutral / Unattractive]
Primary structural advantages: [2-3 forces working in your favor]
Primary structural risks: [2-3 forces working against you]
Strategic implications: [3-5 bullets on what this means for positioning and investment]
```

---

## Trend Analysis Methodology

**When to use**: Identifying and evaluating macro trends that could affect market dynamics, customer behavior, or competitive landscape.

### STEEP Framework (Macro Trends)

| Dimension | What to Scan | Example Signals |
|-----------|-------------|----------------|
| **Social** | Demographics, workforce trends, cultural shifts | Remote work adoption, generational preferences, trust in institutions |
| **Technological** | Emerging tech, platform shifts, automation | AI/ML adoption curves, API economy, IoT, blockchain |
| **Economic** | Macro conditions, budget cycles, investment trends | Interest rates, VC funding cycles, enterprise software spending |
| **Environmental** | Sustainability requirements, regulations, resource constraints | ESG reporting mandates, carbon requirements, supply chain resilience |
| **Political / Regulatory** | Policy changes, trade shifts, data privacy | GDPR/CCPA expansion, antitrust enforcement, data localization laws |

### Trend Evaluation Matrix

For each trend identified:

| Criterion | Scale | Assessment |
|-----------|-------|------------|
| **Impact if true** | Low / Medium / High | How much does this change the market if it plays out? |
| **Probability** | Low / Medium / High | How likely is this to materialize in 3-5 years? |
| **Time to impact** | < 1yr / 1-3yr / 3-5yr / 5yr+ | When does this become relevant? |
| **Directional indicator** | Positive / Neutral / Negative | Does this help or hurt our position? |

**Prioritize for action:** High impact × High probability → Track closely and scenario plan
**Monitor only:** High impact × Low probability → Watch list

---

## Research Synthesis Template

**When to use**: Transforming raw research data (interview notes, survey results, secondary research) into actionable insights and recommendations.

### Synthesis Process (4 Steps)

**Step 1 — Organize the raw data**
- Gather all notes, transcripts, and data in one place
- Tag each data point with: source, respondent type, topic, sentiment

**Step 2 — Find themes**
```
Affinity mapping process:
  1. Write each distinct observation on a separate card/sticky
  2. Group cards that express similar ideas (resist pre-defined categories)
  3. Name each cluster with a theme (use the data's language, not your hypotheses)
  4. Note frequency: how many sources support each theme?
  5. Note strength: are signals weak/anecdotal or strong/consistent?
```

**Step 3 — Distinguish findings from insights**

| Level | Definition | Example |
|-------|-----------|---------|
| **Observation** | Raw data point | "7 of 12 interviewees mentioned manual data export" |
| **Finding** | Pattern across observations | "Manual data workflows are a major pain point for operations teams" |
| **Insight** | The "so what" — the implication | "Automating export workflows could reduce time-on-task by ~40% for a core use case" |
| **Recommendation** | The action to take | "Prioritize API-based export in Q3 roadmap; test with 5 beta customers" |

**Step 4 — Structure the output**

### Research Synthesis Report Template

```
RESEARCH SYNTHESIS — [Topic]
Date: [YYYY-MM-DD]
Method(s): [Interviews / Survey / Secondary / Mix]
Sample: [N=X; [description of respondents]]
Conducted by: [Name / Team]

--- EXECUTIVE SUMMARY ---
[3-5 bullets: most important insights and their implications]

--- METHODOLOGY ---
  - What we did: [Research methods used]
  - Who we talked to / surveyed: [Respondent profile]
  - Dates: [When research was conducted]
  - Limitations: [What this research cannot tell us]

--- KEY FINDINGS ---

Finding 1: [Headline — finding stated as a fact]
Evidence: [Data points, quotes, or stats that support this]
Insight: [What this means]
Recommendation: [What to do about it]
Confidence: [High / Medium / Low] — based on sample size and consistency

Finding 2: [Headline]
[Same structure...]

Finding 3: [Headline]
[Same structure...]

--- THEMES MAP ---
[Visual or table showing theme clusters and supporting evidence counts]

--- VERBATIM HIGHLIGHTS ---
"[Quote from respondent — role, no identifying info]"
"[Quote from respondent]"
"[Quote from respondent]"

--- OPEN QUESTIONS ---
What this research did not answer:
  1. [Unanswered question 1]
  2. [Unanswered question 2]
Recommended follow-up research:
  - [Suggested next step]
```

---

## Data Sources Reference

**When to use**: Identifying sources for secondary research, market sizing, and competitive intelligence.

### Public & Free Sources

| Source | What's Available | Best For |
|--------|-----------------|---------|
| **Google Trends** | Search volume trends over time | Demand trends, seasonality, topic growth |
| **US Census / Eurostat** | Demographic and economic data | TAM sizing, geographic analysis |
| **BLS (Bureau of Labor Statistics)** | Employment, wage, industry data | Workforce trends, B2B market sizing |
| **SEC EDGAR** | Public company filings (10-K, 10-Q) | Competitor financial data, market sizing |
| **Crunchbase (free tier)** | Startup funding, founding dates | Competitive landscape mapping |
| **LinkedIn** | Company employee counts, hiring trends | Competitor growth signals, buyer targeting |
| **G2 / Capterra** | Software reviews | Competitive strengths/weaknesses, buyer language |
| **ProductHunt** | Product launches, upvotes, comments | Early-stage competitor discovery |
| **Reddit / Quora** | Organic customer discussions | Authentic pain points, competitor perception |
| **Hacker News** | Tech community discourse | Technical trends, startup competitive intel |

### Paid / Gated Sources

| Source | What's Available | Typical Use |
|--------|-----------------|------------|
| **Gartner / IDC / Forrester** | Market size reports, vendor rankings, buyer guides | TAM estimates, Magic Quadrant positioning |
| **Ahrefs / SEMrush** | Competitor traffic, keyword rankings, backlinks | SEO competitive analysis |
| **SimilarWeb** | Website traffic estimates | Competitor traffic benchmarks |
| **Bombora / G2 Buyer Intent** | Purchase intent signals | ICP identification, sales prioritization |
| **ZoomInfo / Apollo** | Company and contact data | ICP sizing, prospect lists |
| **PitchBook / CB Insights** | Private company data, VC trends | M&A research, competitive funding analysis |
| **Exploding Topics** | Emerging trends before they peak | Early market signal identification |

### Social Listening Sources

| Tool | What to Monitor | Use Case |
|------|----------------|---------|
| **Google Alerts** | Brand name, competitor names, keywords | Competitor announcements, press coverage |
| **Twitter/X Advanced Search** | Brand mentions, competitor mentions | Real-time sentiment, launch reactions |
| **Reddit Search** | Subreddit discussions by topic | Organic customer pain points |
| **LinkedIn feed monitoring** | Industry leaders, competitor employees | Strategic signals, talent movement |
| **Review platforms** | G2, Capterra, Trustpilot | Ongoing product perception tracking |

**Limitations**: Secondary research is always a starting point, never a conclusion. Analyst market sizes are estimates with wide confidence intervals. Customer review sentiment is self-selected and skews negative (dissatisfied customers review more). Triangulate across multiple sources before drawing conclusions.
