---
slug: altman-z-score-bankruptcy-risk
title: "What Is the Altman Z-Score — Calculating Bankruptcy Risk From 5 Financial Ratios"
description: "How the Altman Z-Score formula combines five financial ratios to flag companies at risk of bankruptcy, what its safe/grey/distress zones mean, and where the model breaks down."
order: 60
updated: 2026-09-04
keywords: ["what is the Altman Z-Score", "Altman Z-Score formula", "bankruptcy risk indicator stocks", "Z-Score calculation ratios", "value trap financial statements", "Altman Z-Score interpretation", "distress zone grey zone stocks"]
seo_audited: 2026-09-04
---

## A Cheap-Looking Stock Can Be a Company That's Quietly Dying

A stock trading at 3x earnings and 0.3x book value looks like an obvious bargain — so why isn't everyone buying it? Often, the market has a good reason for leaving a stock that cheap alone, and the most common one is that the company is genuinely at risk of going bankrupt. A ratio like price-to-earnings only tells you what the market pays for a dollar of current earnings or assets — it says nothing about whether those earnings or assets will still exist next year. [Financial Statement Basics](/en/basics/financial-statement-basics/) covered how EPS, P/E, P/B, and ROE let you read a company's profitability. This lesson asks the opposite question: how likely is this company to fail within the next year or two? In 1968, NYU finance professor Edward Altman built a model to answer exactly that using nothing but numbers already sitting in a company's financial statements. Called the **Altman Z-Score**, it's still referenced today by credit analysts and equity investors alike, more than half a century later. The goal here isn't to hand you a buy-or-sell signal on any stock — it's to understand why these five particular ratios were chosen and combined, and how far you should actually trust the result.

## Why No Single Ratio Can Catch Bankruptcy Risk Alone

A high debt ratio doesn't automatically mean a company is in danger — a business with strong cash flow can service a heavy debt load without issue. Conversely, a company with almost no debt can still run out of cash fast if sales collapse and inventory piles up. Bankruptcy isn't triggered by one metric turning bad; it's what happens when liquidity, profitability, capital structure, and market confidence all deteriorate at once. Altman's question was simple: if you take a set of companies that actually went bankrupt and pair each one with a similarly sized company that didn't, which ratios in the financial statements filed one or two years before the bankruptcy diverge most sharply between the two groups? He statistically identified five such ratios, assigned each a different weight based on how strongly it separated the two groups, and summed them into a single score — the Z-Score. The idea is that combining five different lenses on a company catches warning signs that any single ratio, viewed alone, would miss.

## The Formula and What Each of the Five Ratios Measures

The original formula, built for publicly traded manufacturers, is:

```
Z = 1.2×X1 + 1.4×X2 + 3.3×X3 + 0.6×X4 + 1.0×X5
```

Each ratio (expressed as a decimal, e.g. 20% → 0.2) captures a different dimension of the balance sheet and income statement:

- **X1 = Working Capital / Total Assets**: working capital is current assets minus current liabilities, so this measures short-term liquidity — how much cushion the company has between what it can turn into cash within a year and what it owes within a year.
- **X2 = Retained Earnings / Total Assets**: the share of total assets funded by profits the company has accumulated internally since it was founded. Older, consistently profitable companies score high here; young companies and chronically unprofitable ones score low or even negative.
- **X3 = EBIT / Total Assets**: a profitability measure of how efficiently the company generates operating profit from its asset base. It carries the largest weight (3.3) of the five, making it the single biggest driver of the final score.
- **X4 = Market Value of Equity / Total Liabilities (book value)**: compares what the stock market currently thinks the company's equity is worth against its total debt load. Because it moves with the stock price, it's the one input that reflects market sentiment in real time, before it shows up anywhere else in the accounting.
- **X5 = Sales / Total Assets**: an asset turnover ratio measuring how much revenue the company generates per dollar of assets. A company that can't generate sales from the assets it holds is losing competitiveness.

Put together, the Z-Score compresses five distinct angles — liquidity (X1), accumulated profitability (X2), current profitability (X3), market confidence (X4), and operating efficiency (X5) — into one number.

## What the Score Zones Mean

The zone a company's score falls into matters more than the exact number. The original model's cutoffs are:

| Zone | Score Range | Interpretation |
|---|---|---|
| Safe Zone | 2.99 and above | Low probability of bankruptcy over the next 1-2 years |
| Grey Zone | 1.81 to 2.99 | Ambiguous — warrants a closer look |
| Distress Zone | Below 1.81 | Elevated bankruptcy risk |

In Altman's original validation, the model is widely reported to have correctly flagged a large majority of companies that actually went bankrupt as being in the distress zone one year ahead of time. That result, though, came from a sample of American manufacturers in the 1950s and 60s, and later research generally finds the model's predictive power has weakened as economies and industries have changed since then. The Z-Score is best treated not as a tool that definitively tells you a company will or won't go bankrupt, but as a screening tool for flagging relative financial fragility.

## A Worked Example — Two Hypothetical Manufacturers

Compare two hypothetical manufacturers in the same industry, Company P and Company Q.

| | Company P (healthy) | Company Q (fragile) |
|---|---|---|
| X1 = Working Capital / Total Assets | 0.25 | 0.02 |
| X2 = Retained Earnings / Total Assets | 0.35 | −0.10 |
| X3 = EBIT / Total Assets | 0.15 | 0.01 |
| X4 = Market Value of Equity / Total Liabilities | 1.8 | 0.4 |
| X5 = Sales / Total Assets | 1.2 | 0.9 |
| **Z-Score calculation** | 1.2(0.25)+1.4(0.35)+3.3(0.15)+0.6(1.8)+1.0(1.2) | 1.2(0.02)+1.4(−0.10)+3.3(0.01)+0.6(0.4)+1.0(0.9) |
| **Z-Score** | **3.57 (Safe Zone)** | **1.06 (Distress Zone)** |

Company P has ample working capital and a large cushion of accumulated retained earnings, so its liquidity and financial flexibility aren't in question, and the market is pricing its equity well above its total liabilities — putting it comfortably in the safe zone. Company Q, by contrast, has almost no working capital, negative retained earnings (meaning it has accumulated losses over time rather than profits), and a stock price so depressed that its entire market equity value is less than half its total liabilities. Nearly every one of the five ratios is weak at once — exactly the pattern that lands a company in the distress zone. Looking at P/E or P/B alone for either company would have missed this gap entirely, which is precisely the gap the Z-Score is designed to catch.

## Where the Z-Score Breaks Down — Know the Limits

To use the Z-Score in practice, you need to remember the sample it was built on. The original formula was calibrated on publicly traded American manufacturers in the 1960s, and applying it outside that context without adjustment can produce distorted results.

First, **it doesn't apply to banks or insurers at all.** For financial companies, deposits and policy liabilities themselves show up as liabilities, so total assets and total liabilities mean something fundamentally different than they do for a manufacturer — and the concept of "working capital" doesn't really translate either.

Second, **asset-light growth companies — platforms, software, biotech — tend to score worse than their actual risk warrants.** Both X3 and X5 are calculated relative to total assets, and a company whose core value sits in people, brand, and code rather than factories and inventory will show a small total-asset base on its balance sheet, distorting both ratios. An early-stage biotech or platform company that hasn't turned profitable yet will often post a low Z-Score for this reason — a reflection of its business model, not necessarily of real bankruptcy risk.

Third, **the original formula doesn't work cleanly for private companies or emerging-market firms.** X4 requires a market value of equity, which simply doesn't exist for a company with no publicly traded stock. To address these gaps, Altman later published several variants: the Z'-Score, which substitutes book value of equity for market value so it works for private companies; the Z''-Score, which drops X5 (asset turnover) entirely so it applies more broadly across non-manufacturing industries; and an EM Score calibrated for emerging-market companies. In other words, "the Altman Z-Score" isn't one formula but a family of them, and which version fits depends on the type of company you're analyzing.

## How an Investor Might Actually Use This

Two things are worth keeping in mind when applying the Z-Score in practice. First, this isn't a buy-or-sell signal — it's more useful as a check you run specifically when a stock's valuation looks extremely cheap, to ask whether the cheapness might reflect real financial fragility rather than simple market neglect. [Earnings Quality (Accruals)](/en/basics/earnings-quality-accruals/) covered how accrual analysis checks whether a company's reported profit is genuine; the Z-Score is a complementary check on whether the company will remain around long enough to keep earning it. Second, it helps to compare what the Z-Score implies against how the bond market is already pricing the same risk. [What Is a Credit Spread](/en/basics/credit-spreads-explained/) covered how the bond market prices a company's default risk through credit ratings and spreads — a different lens on the exact same question the Z-Score is trying to answer through financial ratios. When the two point in the same direction, that's a more reliable warning sign; when they diverge, that divergence itself is worth investigating. Calculating a Z-Score yourself just requires numbers from the balance sheet, income statement, and current market capitalization, and isn't hard to do by hand. But mechanically flagging a low score and concluding "this company is about to fail" — without accounting for the industry it's in — misses the point of what the model was actually built to do.

## Takeaways

- The Altman Z-Score combines five weighted ratios — liquidity (working capital), accumulated profitability (retained earnings), current profitability (EBIT), market confidence (equity value vs. liabilities), and operating efficiency (asset turnover) — into a single bankruptcy-risk score.
- Scores of 2.99 or above fall in the safe zone, 1.81-2.99 in the grey zone, and below 1.81 in the distress zone.
- Because the original formula was built on 1960s American manufacturers, it doesn't apply to financial companies and tends to overstate risk for asset-light growth companies.
- Variants exist for private companies (Z'-Score), non-manufacturers (Z''-Score), and emerging-market firms (EM Score).
- Rather than a trading signal, it's most useful as a screening check on why a stock might be trading at an unusually low valuation — as a possible sign of real financial fragility.

## FAQ

### If a company's Z-Score lands in the distress zone, does that mean it's about to go bankrupt?
Not necessarily. The Z-Score is a statistical tool for flagging companies with relatively elevated bankruptcy risk, not a definitive prediction for any single company. Some companies in the distress zone survive through restructuring or new financing, while some in the safe zone get blindsided by a sudden shock.

### Can the original formula be applied directly to companies outside the U.S.?
Some caution is needed because of differences in industry mix and accounting conventions. Asset-light platform and biotech companies, along with financial firms, are especially prone to distorted results if you apply the original manufacturing-based formula without adjustment. Altman himself published several country- and industry-specific variants for exactly this reason, so it's safer to use a version adjusted for the relevant industry when one is available.

### How is this different from just looking at P/E or a debt ratio?
P/E and debt ratios are single-dimension metrics that each show only one slice of the picture. The Z-Score combines five distinct dimensions — liquidity, profitability, market confidence, and efficiency — at once, so it can catch compound fragility that no single ratio would reveal on its own. The tradeoff is that it needs more inputs to calculate and carries its own industry-specific blind spots.

> ⚠️ This article is for informational purposes only and is not investment advice. The company examples in this article are hypothetical and do not represent any real company or actual financial figures. You are solely responsible for your own investment decisions and their outcomes.
