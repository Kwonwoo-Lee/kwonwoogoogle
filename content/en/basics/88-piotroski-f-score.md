---
slug: piotroski-f-score
title: "What Is the Piotroski F-Score — A 9-Point Checklist for Picking Quality Value Stocks"
description: "How the Piotroski F-Score's 9 yes/no tests separate improving companies from deteriorating ones among cheap stocks, with a worked example and a contrast against the Altman Z-Score."
order: 88
updated: 2026-09-18
keywords: ["what is the Piotroski F-Score", "Piotroski F-Score explained", "F-Score calculation", "how to pick value stocks", "avoiding value traps", "Piotroski F-Score vs Altman Z-Score", "financial statement quality screen"]
seo_audited: 2026-09-18
---

## Not All Cheap Stocks Are Cheap for the Same Reason

Pick ten stocks trading at 0.4x book value and wait a few years, and a handful will turn around as earnings recover and the market re-rates them, while the rest keep drifting lower or get worse. As [PER·PBR·PSR·EV/EBITDA Compared](/en/basics/valuation-multiples-per-pbr-psr/) covered, a low valuation multiple only tells you a stock is cheap — it says nothing about whether the underlying business is improving or deteriorating. That's a hard distinction to make because the group of cheap, high book-to-market stocks is inherently a mix of two very different kinds of companies: genuinely undervalued businesses the market has temporarily mispriced, and struggling businesses left cheap for good reason. In 1968, the Altman Z-Score set out to answer a survival question — how likely is this company to go bankrupt? In 2000, University of Chicago (later Stanford) accounting professor Joseph Piotroski asked a different question: short of bankruptcy, is this cheap company's financial position actually getting better or worse? The **Piotroski F-Score** he built answers that question using nothing but numbers already disclosed in the financial statements, scored on a simple 9-point checklist.

## Why Nine Yes/No Questions Instead of One Ratio

Piotroski's approach is fundamentally different from Altman's. The Z-Score multiplies five ratios by statistically derived weights and combines them into one continuous number. The F-Score is much simpler: it asks nine yes/no questions across profitability, financial structure, and operating efficiency — each one asking "did this get better than last year?" — and awards one point per "yes," for an integer score from 0 to 9. No weighting, no statistical model. The simplicity is deliberate. Each test has an unambiguous direction (more profitable, more liquid, more efficient is always the "good" answer), so it's hard to distort by industry norms or accounting quirks the way a single continuous ratio can be. And summing nine independent signals cancels out some of the noise that any one metric carries on its own. In his 2000 paper, Piotroski found that when applied specifically to cheap, high book-to-market stocks, companies with high F-Scores went on to substantially outperform those with low F-Scores. That result comes from a specific sample of U.S. stocks between 1976 and 1996, and the size of the gap can vary across different periods and markets — worth keeping in mind as a commonly cited finding rather than a guaranteed edge.

## The 9 Criteria — 4 Points for Profitability, 3 for Financial Structure, 2 for Efficiency

The F-Score compares the current year's financial statements against the prior year across nine tests, one point each.

**Profitability (4 points)**

- **Is ROA positive?** 1 point if net income for the year is positive. A company running a loss starts at zero here.
- **Is operating cash flow (CFO) positive?** 1 point if cash actually generated from operations, not just accounting profit, was positive for the year.
- **Did ROA improve year over year?** 1 point if return on assets is higher than the prior year — a check on whether profitability is trending up.
- **Is CFO greater than net income?** 1 point if operating cash flow exceeds reported net income. This lines up directly with the accrual concept covered in [Earnings Quality (Accruals)](/en/basics/earnings-quality-accruals/) — it checks whether reported profit is backed by real cash rather than inflated on paper alone.

**Financial Structure and Liquidity (3 points)**

- **Did long-term debt ratio fall?** 1 point if long-term debt relative to total assets declined from the prior year — a sign the company is paying down debt rather than piling it on.
- **Did the current ratio improve?** 1 point if current assets divided by current liabilities rose from the prior year, reflecting improved short-term liquidity.
- **Was there no new share issuance?** 1 point if the company did not issue new common shares during the year, meaning existing shareholders weren't diluted to raise cash.

**Operating Efficiency (2 points)**

- **Did gross margin improve?** 1 point if gross margin — (revenue − cost of goods sold) / revenue — rose from the prior year.
- **Did asset turnover improve?** 1 point if revenue divided by average total assets rose from the prior year.

Put the ROA-improvement test together with the gross margin and asset turnover tests, and a pattern emerges: profitability (ROA) splits into margin (gross margin) times turnover (asset turnover). That's the same logic behind [DuPont Analysis](/en/basics/dupont-analysis-roe-decomposition/), which decomposes ROE into net margin, asset turnover, and financial leverage. The F-Score essentially turns that same decomposition into a set of simple yes/no improvement checks.

## A Worked Example — Two Hypothetical Cheap Manufacturers

Compare two hypothetical manufacturers both trading at 0.5x book value, Company R and Company S.

| Test | Company R | Company S |
|---|---|---|
| ROA positive | Profitable (1 pt) | Loss (0 pt) |
| CFO positive | Positive (1 pt) | Positive (1 pt) |
| ROA improved YoY | Improved (1 pt) | Worsened (0 pt) |
| CFO > net income | Yes (1 pt) | No (0 pt) |
| Long-term debt ratio fell | Yes (1 pt) | No, rose instead (0 pt) |
| Current ratio improved | Yes (1 pt) | No (0 pt) |
| No new share issuance | Yes (1 pt) | No, issued new shares (0 pt) |
| Gross margin improved | Yes (1 pt) | No (0 pt) |
| Asset turnover improved | Yes (1 pt) | Yes (1 pt) |
| **F-Score total** | **9 (perfect score)** | **2** |

At the same 0.5x book value, the two companies look identical from the outside. But Company R isn't just profitable — its profitability is improving, that profit is backed by real cash, and it's paying down debt while improving liquidity without diluting shareholders to do it. Company S, by contrast, is losing money, its financial structure is deteriorating, and it's plugging the gap with a new share issuance — the classic early stage of a downward spiral. A single P/B number couldn't tell these two "cheap stocks" apart; breaking the financial statements into nine directional checks tells a completely different story for each.

## How This Differs From the Altman Z-Score

The two models look similar on the surface — both combine financial statement numbers into a single score — but they're answering different questions. The [Altman Z-Score](/en/basics/altman-z-score-bankruptcy-risk/) multiplies five ratios by statistically fitted weights to answer a survival question: is this company at elevated risk of bankruptcy within the next year or two? The F-Score weighs nine tests equally (one point each) to answer a trend question: is this cheap company's financial position better than it was last year? Think of the Z-Score as a floor check — making sure the ground isn't collapsing — and the F-Score as a quality filter applied within a universe of stocks that are already cheap, to separate the ones actually getting better from the ones getting worse. In practice, the two work well layered together: use the Z-Score first to screen out companies at real bankruptcy risk, then apply the F-Score to the remaining cheap stocks to find the ones showing genuine improvement.

## Limitations — Know What This Screen Is Actually For

Using the F-Score well means remembering the sample and assumptions it was built on.

First, **it was designed specifically for cheap, high book-to-market value stocks.** A high-growth company deliberately running losses to fund expansion may show a low F-Score even though nothing is actually wrong — the checklist wasn't built with that kind of business in mind, and applying it there can produce a misleadingly low score.

Second, **it requires at least two years of financial statements.** Five of the nine tests are year-over-year comparisons, so it can't be computed for a company that just went public.

Third, **it is not a buy or sell timing signal.** The F-Score ignores valuation and price entirely — it's a pure financial-statement screen. A high or low score doesn't tell you when to act; it's a filter for finding improving companies within an already-cheap universe, nothing more.

Fourth, **every test is weighted identically at one point each.** A test that barely improved and one that improved dramatically both count the same, so companies sitting right at a threshold can be classified differently by a single marginal item. And because one test (CFO versus net income) is accrual-based, the F-Score carries the same vulnerability to earnings manipulation that any accrual-based metric does.

## How an Investor Might Actually Use This

Every number the F-Score needs is already sitting in a company's balance sheet, income statement, and cash flow statement. That's its real practical advantage — no paid data feed or complex modeling required, just a table you can score by hand. If you've narrowed your list down to a handful of names, walking through two years of filings and scoring all nine tests by hand does more than just produce a number — it forces you to actually read the statement: comparing net income against cash flow, checking debt and liquidity against the prior year, tracking how margin and turnover moved. That process alone builds a more complete picture of the company's financial health than the final score does on its own. Still, it's best used alongside other questions about why the stock is cheap in the first place, rather than as a standalone decision tool. [Financial Statement Basics](/en/basics/financial-statement-basics/) covers the ROE and P/E fundamentals for checking current profitability; layering the Altman Z-Score for survival risk and the F-Score for improvement trend on top gives you a staged screen rather than a single point of failure. Remember that a perfect F-Score doesn't mean "this stock will definitely go up," and that it was built for a specific context — cheap value stocks — and it becomes a genuinely useful tool for reading financial statements systematically.

## Takeaways

- The Piotroski F-Score is a 0-9 financial health score built from nine yes/no tests across profitability (4 points), financial structure (3 points), and operating efficiency (2 points).
- It was designed to separate improving companies from deteriorating ones within a universe of cheap, high book-to-market value stocks.
- Where the Altman Z-Score asks "is this company at risk of bankruptcy," the F-Score asks "is this company's financial position better than it was last year?"
- It doesn't fit high-growth, loss-funding companies well, needs at least two years of financial statements, and isn't a buy/sell timing signal.
- It's most useful layered with valuation metrics and the Z-Score as a staged screening process, not as a standalone signal.

## FAQ

### If a stock scores a perfect 9, is it automatically a good buy?
Not necessarily. A perfect F-Score only means the financial statement direction improved across all nine tests — it says nothing about whether the valuation is reasonable, the industry outlook is favorable, or management is competent. Applying it mechanically outside its intended context (cheap value stocks) and treating a perfect score as a buy signal misses what the tool was built for.

### Can the F-Score be applied to growth stocks?
It can be calculated, but interpret it carefully. An early-stage company deliberately running losses to fund R&D or market expansion may see its ROA or gross margin tests fail without that reflecting its actual competitive position. Keep in mind the F-Score was validated specifically on cheap value stocks.

### Does it work with financial statements from companies outside the U.S.?
Yes. All nine tests only need basic figures that are standard in any company's filings — net income, operating cash flow, total assets, current assets and liabilities, revenue and cost of goods sold, and share issuance activity. Just stay consistent about whether you're using consolidated or standalone financial statements, since mixing the two across years will throw off the year-over-year comparisons.

> ⚠️ This article is for informational purposes only and is not investment advice. The company examples in this article are hypothetical and do not represent any real company or actual financial figures. You are solely responsible for your own investment decisions and their outcomes.
