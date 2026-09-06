---
slug: value-at-risk-var-explained
title: "What Is Value at Risk (VaR)? How Banks Compress Risk Into One Number"
description: "How VaR turns a portfolio's risk into a single dollar figure, why confidence level and time horizon both matter, and what VaR quietly fails to tell you."
order: 65
updated: 2026-09-06
keywords: ["what is value at risk", "VaR formula explained", "value at risk calculation example", "VaR confidence level meaning", "VaR vs CVaR", "value at risk limitations", "how banks measure risk", "expected shortfall vs VaR"]
seo_audited: 2026-09-06
---

## "How Much Could This Portfolio Lose Tomorrow?"

It's one of the first numbers a bank's or asset manager's risk desk checks every morning. Not how much of each asset they hold, but a single dollar figure that answers: under normal market conditions, what's the most this portfolio is likely to lose over the next day? [The Sharpe Ratio](/en/basics/sharpe-sortino-ratio-risk-adjusted-return/) looks backward, grading a return that already happened against the volatility it took to earn it. **Value at Risk (VaR)** does the opposite — it's a forward-looking estimate of how bad losses could get over some future period, stated at a chosen level of confidence. JPMorgan built and popularized VaR internally in the 1990s, and it has since become a pillar of bank capital regulation (the Basel framework) and a daily fixture at hedge funds and asset managers alike.

## The Question VaR Actually Answers

The cleanest way to understand VaR is to fill in this sentence:

> "At a 95% confidence level, this portfolio's loss over the next 1 day will not exceed $X."

That X is the VaR figure. If a portfolio's 1-day VaR at 95% confidence is $50,000, it means there's only a 5% chance tomorrow's loss exceeds $50,000. Flip it around: across roughly 100 normal trading days, losses should stay within $50,000 on about 95 of them, and exceed it on around 5.

What makes VaR useful is that it packs three pieces of information into one number: the **loss amount**, the **time horizon** (one day? ten days?), and the **confidence level** (95%? 99%?). A VaR number without all three attached is meaningless — "our VaR is $50,000" tells you nothing until you know it's "1-day, 95% confidence." Raise the confidence level from 95% to 99% on the same portfolio and the VaR figure grows, because covering a rarer, more extreme event requires reaching further into the loss distribution.

## Three Ways to Calculate It

VaR isn't computed one fixed way — there are three common approaches, and they can produce noticeably different numbers for the same portfolio.

**The variance-covariance (parametric) method** assumes returns follow a normal distribution, then multiplies the portfolio's standard deviation by the z-score matching the chosen confidence level (about 1.65 for 95%, about 2.33 for 99%). It's fast and simple, but real markets tend to produce extreme moves more often than a normal distribution predicts (so-called "fat tails"), which means this method can understate true risk.

**Historical simulation** skips the distributional assumption entirely. It takes a stretch of actual past returns (say, the last 500 trading days), sorts them from worst to best, and reads the VaR straight off the bottom 5% (for 95% confidence) or bottom 1% (for 99%). It reflects real market behavior rather than a theoretical curve, but if the historical window happened to miss a major shock, the model won't see it coming either.

**Monte Carlo simulation** generates thousands of randomized hypothetical price paths and pulls the loss distribution from those. It handles complex portfolios — including options and other instruments that move non-linearly with the underlying asset — better than the other two methods, but it's computationally heavy and the result depends heavily on the assumptions baked into how those simulated paths are generated.

None of the three is simply "correct" — each answers the same question under different assumptions. In practice, risk teams often run more than one and compare the results, treating large gaps between them as a signal that a given model's assumptions no longer fit current market conditions.

## Why Compress Risk Into One Number in the First Place

VaR's rise to standard practice wasn't accidental. A large bank holds thousands of distinct positions across stocks, bonds, currencies, and derivatives. There's no realistic way for a management team or board to review each position's risk individually every morning. JPMorgan's 1994 release of its RiskMetrics methodology was, at its core, an attempt to solve exactly that problem: compress risk scattered across wildly different asset classes into a single figure that executives could actually check daily. Bank regulators later built VaR-based models directly into capital requirements under the Basel framework, turning it from a useful internal tool into a mandatory regulatory metric.

## Backtesting — Checking Whether the Model Was Right

Building a VaR model isn't the end of the process. Risk teams track, day after day, how the day's actual profit or loss compared to the VaR figure calculated that morning, logging every day the loss exceeded VaR — called an "exception." At 95% confidence, roughly 12 to 13 exceptions out of 250 trading days (about a year) is expected and normal. If exceptions start showing up far more often than that, it's a warning sign that the model is underestimating current risk — and under Basel rules, banks that breach their expected exception rate too often are required to hold more regulatory capital as a result.

## A Worked Example

Take a $10 million equity portfolio whose daily returns had a standard deviation of 1.5% over the past year. Using the variance-covariance method for a 95%-confidence, 1-day VaR:

```
1-Day VaR = Portfolio Value × Standard Deviation × Confidence Z-Score
          = $10,000,000 × 1.5% × 1.65
          ≈ $247,500
```

That means: under normal conditions, there's roughly a 5% chance tomorrow's loss exceeds $247,500. Push the confidence level to 99% on the same portfolio and the z-score rises from 1.65 to about 2.33, pushing VaR up to roughly $349,500 — covering a rarer 1%-probability event requires reaching further into the tail. In practice, banks reporting VaR to regulators typically use 99% confidence, while asset managers monitoring risk day-to-day more often use 95% — the two contexts call for different safety margins. To extend the horizon from 1 day to 10 days, a common shortcut multiplies the 1-day figure by the square root of 10 (about 3.16) — the so-called "square-root-of-time rule." That approximation assumes daily returns are independent and identically distributed, so it can drift noticeably from the true 10-day figure during turbulent markets.

## What VaR Doesn't Tell You

VaR's biggest strength — compressing risk into one clean number — is exactly where it loses information that matters.

The most important gap: **VaR says nothing about how bad a loss gets once it exceeds the threshold.** A 95%-confidence VaR of $250,000 means there's a 5% chance of losing more than that — but whether that 5% scenario means a loss of $260,000 or $20 million is completely invisible in the VaR number itself. In both the 2008 financial crisis and the 1998 collapse of Long-Term Capital Management, the damage came not from losses VaR models failed to anticipate on an ordinary day, but from tail events sitting entirely outside the confidence interval VaR was ever designed to describe. **Conditional VaR (CVaR)**, also called **Expected Shortfall**, exists specifically to close this gap — it calculates the average loss across scenarios where the loss already exceeds VaR, capturing the severity of the tail that VaR itself leaves blank.

A second limitation: every calculation method rests on historical data or a statistical assumption. The variance-covariance method assumes normally distributed returns; historical simulation assumes the past is a reasonable guide to the future. When market structure shifts or a genuinely new kind of shock arrives, VaR calculated any of the three ways can fail to capture it.

Third, VaR can behave in a technically counterintuitive way: combining two positions is supposed to reduce risk through diversification, but under certain conditions the VaR of a combined portfolio can actually exceed the sum of the two positions' individual VaRs — a property called non-subadditivity. CVaR is mathematically free of this problem, which is one more reason it's often paired with VaR rather than replacing it.

Finally, VaR was built to manage and report risk across large, multi-asset portfolios and institutions as a whole — much like [beta](/en/basics/beta-and-volatility/) or the [Sharpe ratio](/en/basics/sharpe-sortino-ratio-risk-adjusted-return/), it's best treated as one input among several, understood alongside what it assumes and what it leaves out, rather than as a complete picture on its own.

## Key Takeaways

- VaR compresses risk into a single figure: "at X% confidence, losses over Y days won't exceed $Z."
- Interpreting a VaR number correctly requires all three pieces — loss amount, time horizon, and confidence level — stated together.
- The three main calculation methods (variance-covariance, historical simulation, Monte Carlo) rest on different assumptions and can produce different results for the same portfolio.
- VaR's core limitation is that it says nothing about how severe losses get once they cross the threshold; Conditional VaR (Expected Shortfall) was built to fill that gap.
- VaR is a risk-management input, not a trading signal — it's meant to gauge how much a portfolio stands to lose under normal market conditions, not to time entries or exits.

## FAQ

### Does a low VaR mean a portfolio is safe?
A low VaR means the expected loss range under normal market conditions is small — it says nothing about how the portfolio would behave in an extreme, low-probability event. For that, look at a complementary measure like CVaR (Expected Shortfall), which captures the severity of losses beyond the VaR threshold.

### Do individual investors need to calculate VaR themselves?
Not really — VaR was designed for banks and asset managers to manage and report risk across large, multi-asset portfolios. That said, getting a rough sense of "how much could my account realistically swing in a single bad day" applies the same underlying logic on a personal scale.

### How is VaR different from maximum drawdown (MDD)?
Maximum drawdown is a backward-looking measure — the largest peak-to-trough decline that actually happened over a given period. VaR is forward-looking: a statistical estimate, at a chosen confidence level and horizon, of how large a loss could be. One describes what already happened; the other describes a probabilistic range of what could happen next.

### Does a higher VaR always mean a worse portfolio?
Not necessarily. VaR scales with a portfolio's size and volatility, so a larger portfolio can carry a bigger dollar VaR even with excellent risk-adjusted returns. VaR is more meaningful as a share of portfolio value, or compared against another portfolio calculated under the same assumptions, than as a standalone verdict on quality.

> ⚠️ This article is for informational purposes only and is not investment advice. Investment decisions and their outcomes are the sole responsibility of the investor.
