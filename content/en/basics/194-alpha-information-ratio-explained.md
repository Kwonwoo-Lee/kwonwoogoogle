---
slug: alpha-information-ratio-explained
title: "What Are Alpha and the Information Ratio? Measuring a Fund Manager's Real Skill"
description: "How Jensen's alpha isolates genuine skill from returns that simply reflect extra risk, and how the information ratio measures whether that edge was consistent — with worked examples and limits."
order: 194
updated: 2026-11-10
keywords: ["what is alpha in investing", "jensen's alpha explained", "what is information ratio", "information ratio formula", "alpha vs information ratio", "active fund manager skill measure", "alpha meaning stock market", "how to evaluate fund manager performance"]
seo_audited: 2026-11-10
---

## "Beat the Index by 5 Points" — Skill or Just More Risk?

Say a fund returned 15% in a year while the broad market index gained 10%. The manager has a pitch ready: "We beat the market by 5 points." But what if that fund was built entirely out of higher-beta stocks — names that move more sharply than the market in both directions? In a year when the market rises, holding a higher beta is itself a built-in tailwind, so it's impossible to tell from the raw numbers whether that 5-point edge came from sharp stock-picking or simply from carrying more risk than the benchmark. [What Is Beta?](/en/basics/beta-and-volatility/) and [CAPM](/en/basics/capital-asset-pricing-model-capm/) already gave us a baseline for "how much return should this amount of risk reasonably produce." **Alpha** is the metric that strips out that baseline and isolates only the return that risk alone can't explain. And the **information ratio** answers a follow-up question: was that extra return a one-time fluke, or a consistent edge?

## What Is Alpha? Actual Return Minus What Risk Alone Would Predict

CAPM says that once you know an asset's beta, you can calculate the return that level of risk alone would reasonably be expected to produce:

```
Expected Return = Risk-Free Rate + Beta × (Market Return − Risk-Free Rate)
```

**Alpha** is the gap between that expected return and the return actually delivered. It's also called **Jensen's alpha**, after economist Michael Jensen, who formalized the measure in a landmark 1968 study.

```
Alpha = Actual Return − [Risk-Free Rate + Beta × (Market Return − Risk-Free Rate)]
```

The logic is straightforward: the bracketed term is "what this level of beta alone should have earned," and subtracting it from the actual return leaves only the portion earned beyond that baseline. An alpha of zero means the fund earned exactly what its risk level implied; positive alpha means it beat that baseline; negative alpha means it didn't even earn the reward its risk level should have produced. Going back to the opening example: if that fund's beta was 1.3 and the risk-free rate was 3%, CAPM's expected return works out to 3% + 1.3 × (10% − 3%) = 12.1%. Subtracting that from the actual 15% return gives an alpha of +2.9 points — far smaller than the headline "beat the market by 5 points." That missing 2.1-point gap wasn't skill; it was simply the reward for carrying more beta in the first place.

Jensen's original 1968 study tested this idea on 115 U.S. mutual fund managers over 1945–1964, recalculating their CAPM-adjusted alpha to see whether they had genuine stock-picking foresight beyond a simple buy-and-hold index strategy. On average, those funds' alphas came out close to zero or negative once fees were factored in — meaning most managers failed to beat a passive benchmark. That finding remains a reference point in every debate about whether active management is worth paying for.

## A Worked Example: Same Excess Return, Different Alpha

Assume a risk-free rate of 3% and a market return of 10%, and compare two funds with different betas.

| | Fund C | Fund D |
|---|---|---|
| Beta | 0.8 | 1.5 |
| Actual return | 11% | 15% |
| CAPM expected return | 3%+0.8×7%=8.6% | 3%+1.5×7%=13.5% |
| Alpha | 11%−8.6%=**+2.4 pts** | 15%−13.5%=**+1.5 pts** |

On the surface, Fund D's 15% return looks more impressive. But because Fund D was built to move 1.5 times as sharply as the market, its "reasonably expected" return was already higher to begin with. Fund C, despite a lower headline return, actually generated more excess return per unit of risk taken. Raw-return ranking (D beats C) and alpha ranking (C beats D) can flip in opposite directions — which is exactly the problem alpha exists to solve. A simple return comparison conflates "the effect of taking on more risk" with "genuine stock-selection skill."

## What Is the Information Ratio? Measuring Consistency, Not Just Size

Alpha (or excess return against a benchmark) tells you the size of the edge, but not whether that edge came from a few lucky bets or from skill repeated consistently. That's the question the **information ratio (IR)** answers.

```
Information Ratio = (Fund Return − Benchmark Return) ÷ Tracking Error
```

The numerator is called **active return**: how much the fund beat its benchmark (typically a broad market index) by. The denominator, **tracking error**, is the standard deviation of that excess return period to period. [ETF Tracking Error vs Premium/Discount](/en/basics/etf-tracking-error-premium-discount/) covered tracking error in a completely different context — as a structural flaw measuring how badly a passive ETF fails to replicate its index. Here, tracking error instead measures the swings that naturally occur whenever an active manager deliberately bets differently from the benchmark. Betting differently is exactly what creates the opportunity for excess return in the first place, but if those bets are hit-or-miss from one period to the next, tracking error balloons and the information ratio drops. If instead the manager beats the benchmark by a similar margin period after period, tracking error stays small and the information ratio climbs.

For instance, say two funds both delivered an average 4-point annual excess return. Fund E won by a similar small margin nearly every month, producing a tracking error of 2%; Fund F swung between big wins and big losses relative to the benchmark, producing a tracking error of 8%. Fund E's information ratio comes out to 4÷2=2, while Fund F's is only 4÷8=0.5 — a fourfold difference despite identical average excess return. The same-sized edge gets evaluated completely differently depending on how consistently it showed up. As a rough guideline, an information ratio above 0.5 is often considered decent and above 1 quite strong, but treat these as loose, comparison-dependent benchmarks rather than hard cutoffs.

## How This Differs From the Sharpe Ratio

[The Sharpe Ratio](/en/basics/sharpe-sortino-ratio-risk-adjusted-return/), along with Sortino and Treynor, all benchmark performance against the **risk-free rate** — an absolute measure of risk-adjusted return. Alpha and the information ratio instead benchmark against **the market (via CAPM) or a specific index**. In other words, the Sharpe ratio asks "was taking on this much risk worth it, compared to just holding risk-free bonds?" while alpha and the information ratio ask "was active management itself worth it, compared to simply buying and holding the benchmark index?" These aren't mutually exclusive — you can apply the Sharpe ratio to assess total risk-adjusted performance and the information ratio to assess the value added by active decisions, on the same fund, to answer two different questions. This is exactly why the information ratio comes up so often in the active-vs-passive debate: a low information ratio on an active fund means its attempts to beat the benchmark added cost and volatility without a consistent payoff.

## Where This Falls Short

A few caveats matter here. First, both measures are backward-looking calculations over a specific historical period; as covered in [Efficient Market Hypothesis vs Behavioral Finance](/en/basics/efficient-market-hypothesis-behavioral-finance/), a positive alpha in the past is no guarantee of the same skill going forward. Widely cited studies, such as S&P Dow Jones Indices' SPIVA scorecards, have at times found that only somewhere in the high-teens percentage of U.S. large-cap active managers beat the S&P 500 over a trailing ten-year window — though that figure moves depending on the period and market measured. Second, the beta used to calculate alpha itself depends on the measurement window and benchmark chosen, so the same fund's alpha can shift depending on those assumptions. Third, because the information ratio's denominator (tracking error) shrinks the ratio's size, a "closet indexing" strategy that hugs its benchmark almost exactly while squeezing out a tiny, barely-there excess return can still post a high information ratio. A high number alone doesn't prove skill — it's worth checking what specific stock or sector bets actually produced that excess return. Fourth, whether the figures are calculated net of fees matters enormously: an active fund with high expenses can show positive alpha before fees while delivering negative alpha to the investor after fees are deducted.

## Practical Takeaway for Investors

When screening active funds, the instinct is to start with "which fund had the highest return last year." Applying what's covered here flips that order. First, check whether the fund's beta runs meaningfully higher than its benchmark's — a high return built on extra beta isn't the same as skill. Second, look at alpha over a 3-to-5-year window to see whether it's stayed positive consistently, not just in one good year. Third, check the information ratio to see whether that alpha came from one outsized bet or showed up repeatedly across periods. Layering these three in this order gets you much closer to separating "a fund that looks good" from "a fund with risk-adjusted skill that's actually been verified." None of this, though, tells you when to buy or sell — it's strictly a backward-looking yardstick for judging past management.

## Takeaway

- Alpha is the gap between CAPM's beta-based expected return and actual return — it strips away the reward for taking on risk and isolates genuine excess return.
- A higher beta raises the expected-return baseline, so a fund with a higher raw return can actually have lower alpha than one with a lower raw return.
- The information ratio divides excess return against a benchmark (active return) by the volatility of that excess return (tracking error), measuring how consistently the edge showed up.
- The Sharpe ratio measures absolute risk-adjusted performance against the risk-free rate; alpha and the information ratio measure whether active management itself was worth it, against the market or a benchmark.
- Both are backward-looking metrics that shift depending on the benchmark, time window, and whether fees are included — none of them guarantee future performance.

## FAQ

### Does positive alpha mean a fund manager is skilled?
It means the fund outperformed what its risk level would predict over that specific period — but a single period of positive alpha doesn't prove lasting skill. Alpha can shift with the measurement window or benchmark chosen, so it's worth checking whether positive alpha has held up repeatedly over longer stretches.

### Should I look at the information ratio or the Sharpe ratio?
They answer different questions. Use the Sharpe ratio to ask "was taking on this risk worth it compared to a risk-free asset?" Use the information ratio to ask "was this active fund actually better than just buying the benchmark index?" The information ratio comes up more often when comparing active funds to passive ETFs; the Sharpe ratio is more common when judging a whole portfolio's risk-adjusted performance.

### Do individual investors need to calculate alpha or the information ratio themselves?
Not usually. Most fund fact sheets and asset manager materials already publish 3-year and 5-year alpha and information ratio figures. It's worth checking whether those numbers are before or after fees, and which benchmark was used, before comparing across funds.

> ⚠️ This article is for informational purposes only and is not investment advice. The fund examples used are hypothetical and do not represent any actual product or figures. You are solely responsible for your own investment decisions.
