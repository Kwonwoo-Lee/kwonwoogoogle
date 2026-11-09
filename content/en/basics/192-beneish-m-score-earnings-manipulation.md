---
slug: beneish-m-score-earnings-manipulation
title: "What Is the Beneish M-Score — Scoring Earnings Manipulation Risk From 8 Financial Ratios"
description: "How the Beneish M-Score combines eight year-over-year financial ratios into a probability score for earnings manipulation, and how it relates to the Altman Z-Score and Piotroski F-Score."
order: 192
updated: 2026-11-09
keywords: ["what is the Beneish M-Score", "Beneish M-Score formula", "earnings manipulation detection model", "how to detect accounting fraud stocks", "M-Score calculation example", "Beneish M-Score vs Altman Z-Score", "financial statement fraud ratios", "M-Score threshold interpretation"]
seo_audited: 2026-11-09
---

## Should You Trust a Company Whose Net Income Just Jumped?

When a company reports net income up several multiples year over year, the natural reaction is relief — the business is doing better. But as [Earnings Quality](/en/basics/earnings-quality-accruals/) explained, net income isn't cash that landed in the bank; it's a number computed under accrual accounting rules. Pull revenue recognition forward, or push a cost that should hit the income statement this quarter onto the balance sheet as an asset instead, and net income rises with no corresponding change in the company's actual cash-generating ability. The [Altman Z-Score](/en/basics/altman-z-score-bankruptcy-risk/) scores "how likely is this company to go bankrupt," and the [Piotroski F-Score](/en/basics/piotroski-f-score/) scores "is this cheap stock's business genuinely improving." This lesson covers a third model built to answer a different question: how likely is it that the earnings a company just reported were artificially manipulated? That's what the **Beneish M-Score** tries to estimate.

## Who Built It, and Why

The Beneish M-Score comes from a 1999 paper, "The Detection of Earnings Manipulation," by Messod Beneish, an accounting professor at Indiana University. His method mirrored Altman's: instead of pairing bankrupt companies with healthy ones, Beneish paired companies the SEC had sanctioned for accounting fraud, or whose manipulation had otherwise been confirmed, with similarly sized, same-industry companies that hadn't manipulated anything. He then identified eight financial ratios that diverged most sharply between the two groups in the years before the fraud came to light, assigned each a statistically estimated weight, and summed them into a single score — the M-Score (M for Manipulation). The scaffolding resembles the Z-Score, but the target question is entirely different: the Z-Score flags companies at risk of failing; the M-Score flags companies whose reported numbers may be dressed up.

## What Each of the Eight Ratios Is Trying to Catch

All eight inputs measure year-over-year change in a ratio, not the ratio's absolute level — the premise is that a sharp, abnormal swing from the prior year is itself a warning sign, even if neither year's number looks extreme on its own.

- **DSRI (Days' Sales in Receivables Index)**: the year-over-year change in receivables divided by sales. If receivables are growing much faster than sales, revenue may have been recognized before the cash was collected, or channel stuffing pushed excess inventory onto distributors just to book the sale.
- **GMI (Gross Margin Index)**: last year's gross margin divided by this year's gross margin. A rising index means margins are deteriorating — and the premise is that a company under margin pressure has more incentive to dress up its numbers.
- **AQI (Asset Quality Index)**: the year-over-year change in the share of total assets that isn't current assets, PP&E, or securities — in other words, "soft" assets. A sudden jump suggests costs that should have been expensed may instead have been capitalized as an intangible or other asset.
- **SGI (Sales Growth Index)**: this year's sales divided by last year's. Fast growth isn't itself a bad sign, but the model treats it as a condition that gives management both the pressure and the opportunity to manage the numbers to keep the growth story alive.
- **DEPI (Depreciation Index)**: whether the depreciation rate relative to PP&E has slowed compared to the prior year. Slowing depreciation lowers this year's expense and inflates net income.
- **SGAI (SG&A Expense Index)**: the year-over-year change in SG&A expense as a share of sales. In Beneish's data, manipulating companies tended to hold SG&A growth down relative to sales growth rather than let it rise — the opposite of what intuition might suggest.
- **LVGI (Leverage Index)**: the year-over-year change in (long-term debt + current liabilities) divided by total assets. Rising leverage raises the risk of breaching debt covenants, which the model treats as another incentive to manipulate.
- **TATA (Total Accruals to Total Assets)**: (income from continuing operations minus operating cash flow) divided by total assets. This carries the largest weight of the eight, and it's the same gap between net income and cash flow covered in [Earnings Quality](/en/basics/earnings-quality-accruals/) — here expressed as a single number.

Notice that not every variable pushes in the direction intuition would suggest. SGAI and LVGI both carry negative coefficients in the actual formula — meaning a rise in either one pulls the score *down*, not up. That's not an error; it reflects that Beneish didn't start from theory and fit the data to match it. He estimated the direction and size of each weight statistically, from how real manipulators actually behaved relative to non-manipulators. The [Altman Z-Score](/en/basics/altman-z-score-bankruptcy-risk/) was built the same way — both models share that empirical, not purely theoretical, design philosophy.

## The Formula and How to Read the Score

The eight variables combine into:

```
M = −4.84 + 0.920×DSRI + 0.528×GMI + 0.404×AQI + 0.892×SGI
      + 0.115×DEPI − 0.172×SGAI + 4.679×TATA − 0.327×LVGI
```

A higher score (closer to zero, or positive) means a higher estimated likelihood of manipulation. Beneish's own cutoff was −1.78: scores above that are grouped with the "likely manipulator" profile. Later research and various screening tools often use a more conservative cutoff around −2.22 instead. Unlike the Z-Score's clean safe/grey/distress zones, there's no single universally agreed threshold here — the number you use to classify a company depends on which source's cutoff you're following.

| Commonly used range | Interpretation |
|---|---|
| Below −2.22 | Lower likelihood of manipulation |
| −2.22 to −1.78 | Ambiguous zone |
| −1.78 and above | Higher likelihood, worth a closer look |

## A Worked Example — Two Hypothetical Companies

Consider two hypothetical same-industry companies. Company T's sales stayed roughly flat year over year, and its operating cash flow tracked its net income closely. Company U's receivables grew far faster than its sales (DSRI rising), it shifted some costs into an intangible asset line (AQI rising), and its net income rose even as its operating cash flow fell (TATA rising). Plugging simplified versions of just those three variables in: Company T's inputs stay close to 1.0 (little change from the prior year), landing its M-Score around −2.5, solidly in the lower-risk range. Company U's three inputs all move sharply, and because TATA and DSRI carry some of the model's larger weights, its M-Score can climb above the −1.78 cutoff. The point of this comparison is that looking only at net income growth or a P/E multiple, Company U would have looked like the stronger story. The M-Score exists specifically to surface the gap between reported earnings and operating cash flow, and the shift in asset composition, sitting underneath that story.

## The Limits — A Probabilistic Signal, Not Proof

The first thing to remember when using the M-Score is that it doesn't prove a company manipulated its earnings. Beneish's own research showed the model's discriminating power fell well short of 100%, and it produces both false positives (flagging honest companies) and false negatives (missing real manipulators). A genuinely fast-growing company can post a high DSRI or SGI with no manipulation at all, simply because receivables and sales are both scaling up quickly. The original model also doesn't translate well to banks or insurers, where "sales" and "receivables" don't mean what they mean for an industrial company. Retrospective studies — including looking back at Enron in 2001 and China's Kangmei Pharmaceutical fraud case uncovered in 2019 — have found the M-Score would have flagged elevated scores before the fraud became public. But those are backward-looking confirmations after the fact, not evidence the model reliably catches fraud in real time. A high score doesn't confirm manipulation, and a low score doesn't rule it out.

## How to Actually Use This as an Investor

The most practical way to use the M-Score is alongside the Z-Score and F-Score as a three-part screen. When a stock looks extremely cheap or its earnings have suddenly jumped, check the [Altman Z-Score](/en/basics/altman-z-score-bankruptcy-risk/) for whether the company has the financial strength to survive, the [Piotroski F-Score](/en/basics/piotroski-f-score/) for whether that improvement is backed by real fundamentals, and the M-Score for whether the reported numbers themselves can be trusted. A single red flag from one model isn't a reason to avoid a stock outright, but several flashing at once is a good reason to dig deeper into the filings. In practice, rather than computing all eight variables precisely, just comparing this year's and last year's balance sheet, income statement, and cash flow statement on three items — receivables growth relative to sales (DSRI), the gap between net income and operating cash flow (TATA), and any sudden shift in asset composition (AQI) — will surface most of the warning signs the full model is built to catch. Either way, this is a first-pass filter for how skeptically to read a report, not a buy-or-sell signal.

## Key Takeaways

- The Beneish M-Score, from a 1999 paper by professor Messod Beneish, scores the likelihood that a company's reported earnings were manipulated by comparing confirmed fraud cases against matched non-manipulating companies.
- It combines the year-over-year change in eight ratios — DSRI, GMI, AQI, SGI, DEPI, SGAI, LVGI, and TATA — with TATA (the gap between net income and operating cash flow) carrying the largest weight.
- A score above roughly −1.78 is commonly treated as higher-risk, and below −2.22 as lower-risk, though the exact cutoff varies by source.
- Pairing it with the Altman Z-Score (bankruptcy risk) and Piotroski F-Score (fundamental quality) lets you screen for three different kinds of risk at once.
- It's a probabilistic warning signal, not proof of fraud — fast-growing honest companies can trigger false positives, and the model doesn't apply well to financial institutions.

## FAQ

### If a company's M-Score is high, does that mean it committed accounting fraud?
No. A high score only means the company's financial ratios moved in ways statistically similar to past confirmed manipulators — it isn't proof of fraud for any specific company. Genuinely fast-growing, honest companies can trigger a high score on some of the inputs and still be clean.

### How is the Beneish M-Score different from the Altman Z-Score?
Both combine several weighted financial ratios into a single score, but they answer different questions. The Z-Score asks how likely a company is to go bankrupt; the M-Score asks how likely it is that reported earnings were manipulated. A financially healthy company (high Z-Score) can still have a high M-Score if it's been inflating its numbers.

### Can an individual investor calculate this themselves?
Yes, in principle — you need two consecutive years of balance sheet, income statement, and cash flow statement data, all of which are in a company's annual filings. Getting all eight variables exactly right requires care with each ratio's precise definition, so a practical starting point is checking just TATA (the income-versus-cash-flow gap) and DSRI (how fast receivables are growing relative to sales) before attempting the full formula.

> ⚠️ This lesson is for informational purposes only and is not investment advice. The companies described are hypothetical examples used to illustrate the concept and do not represent any real company or actual financial figures. Investment decisions and their outcomes are the sole responsibility of the investor.
