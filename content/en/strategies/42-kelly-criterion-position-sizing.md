---
slug: kelly-criterion-position-sizing
title: "Kelly Criterion Position Sizing: Why Traders Use Half Kelly Instead of Full Kelly"
description: "Learn how the Kelly Criterion turns win rate and reward-to-risk into an optimal bet size, and why most traders scale it down to half or quarter Kelly."
order: 42
updated: 2026-09-02
keywords: ["kelly criterion", "kelly criterion trading", "position sizing calculator", "half kelly vs full kelly", "optimal bet size formula", "kelly criterion stock trading", "fractional kelly", "money management formula"]
seo_audited: 2026-09-02
---

## What the Kelly Criterion Actually Answers

[Lesson 6 on risk/reward and money management](/en/strategies/risk-reward-money-management/) covered how to set a stop and target and calculate risk/reward. But even with a great risk/reward ratio, one question is still left unanswered: **how much of your account should you actually risk on this trade?**

That's the exact question the Kelly Criterion tries to answer mathematically. John Kelly Jr. derived it at Bell Labs in 1956 — not for trading, but for information theory, describing how fast a signal could be transmitted reliably over a noisy channel. Edward Thorp later carried the same math into blackjack card counting and, eventually, hedge fund management, which is how it ended up as a staple of trading and betting theory.

The formula answers one thing: **given a known win rate and reward-to-risk ratio, what fraction of capital, bet repeatedly, maximizes long-run compound growth?** It's explicitly a long-run, repeated-bet framework — not a rule for sizing any single trade in isolation.

## The Formula and How to Use It

The trading-adapted version of the Kelly formula is:

```
f* = W - (1-W) / R
```

- **f\*** — the fraction of capital to risk per trade (the "Kelly fraction")
- **W** — win rate, expressed as a decimal (e.g. 55% → 0.55)
- **R** — reward-to-risk ratio (average win ÷ average loss)

Here's a worked example. Say a strategy wins 55% of the time with a 2:1 reward-to-risk ratio (win +2, lose -1):

```
f* = 0.55 - (1 - 0.55) / 2
f* = 0.55 - 0.225 = 0.325 (32.5%)
```

The math says this strategy's optimal bet size is 32.5% of capital per trade. Notice how sensitive that number is to small changes in the inputs: drop the win rate to 45% and f* falls to 17.5%; drop it to 40% and f* falls to just 10%. **A small error in your win-rate or reward-to-risk estimate swings the recommended bet size dramatically** — which turns out to be the formula's biggest practical weakness, covered below.

<figure class="diagram">
  <img src="/static/img/charts/en/kelly-criterion-position-sizing.svg" alt="A curve showing expected compound growth rate rising as bet fraction increases, peaking at the full Kelly fraction, then falling back to zero growth at twice the full Kelly fraction and turning negative beyond that. Half Kelly sits before the peak, retaining most of the growth rate at much lower volatility" loading="lazy">
  <figcaption>As bet size increases, expected growth peaks at full Kelly (f*) and turns negative past 2×f*. Half Kelly sacrifices only a modest amount of growth for a much smoother ride.</figcaption>
</figure>

## Why This Works: Compounding, Not Simple Averaging

The insight behind Kelly is that an account compounds **geometrically**, not arithmetically. Bet too little and you leave growth on the table; bet too much and growth actually gets worse — or the account risks ruin — because of a basic asymmetry: a 50% loss requires a 100% gain just to recover, and that math gets more punishing the larger the bet size gets. Push your bet fraction far enough past the optimum and one large loss can erase the gains from many previous wins, even if your win rate stays exactly the same.

This is a different layer from [Lesson 6's risk/reward](/en/strategies/risk-reward-money-management/) or [Lesson 13's risk filters](/en/strategies/risk-filters-atr-cmf/). Risk/reward tells you whether a trade is statistically worth taking at all; Kelly tells you how much to put behind a trade you've already decided is worth taking. The two are complements, not substitutes.

## Full Kelly vs. Half Kelly vs. Quarter Kelly

Almost no one trades the raw, calculated Kelly fraction ("full Kelly") in practice. Instead, **fractional Kelly** — betting some fraction of what the formula recommends — is the far more common convention. The comparison shows why:

| Approach | Bet size | Growth rate (vs. peak) | Volatility / drawdown |
|---|---|---|---|
| Full Kelly (100%) | f* (e.g. 32.5%) | 100% (theoretical maximum) | Very high — deep, uncomfortable drawdowns are commonly reported |
| Half Kelly (50%) | f*/2 (e.g. 16.25%) | ~75% (approximate) | Substantially lower than full Kelly |
| Quarter Kelly (25%) | f*/4 (e.g. 8.1%) | ~56% (approximate) | Noticeably steadier than half Kelly |

Those "~75%" and "~56%" figures come from a well-known, widely cited property of the Kelly growth curve — it's roughly parabolic near its peak, so cutting the bet size in half costs you proportionally less growth than volatility. They're commonly repeated rules of thumb from simulation and practitioner experience, not exact constants that hold for every strategy. But the direction is consistent enough that even Edward Thorp — who actually deployed Kelly sizing in card counting and later in options arbitrage — is widely reported to have used half Kelly rather than full Kelly in practice.

## The Real Danger: Estimating the Inputs Wrong

The formula's biggest risk isn't the math — it's the assumption that you actually know your true win rate and reward-to-risk. Both are estimates pulled from past trades or backtests, and nothing guarantees they'll hold going forward.

Kelly is unusually sensitive to that estimation error. A commonly cited illustration: if your true win rate is 44% but you assume 55% and size accordingly, your risk of eventual ruin can jump sharply — far more than the small input error would suggest. That risk gets worse with a small sample size, where it's genuinely hard to tell a real, durable edge apart from a lucky recent stretch.

Kelly also assumes each bet is independent and identically distributed. Real portfolios rarely work that way — holding several stocks in the same sector, or getting hit across the board in a broad market selloff, means your trades are correlated. The formula doesn't account for that correlation, so applying a full Kelly fraction independently to several positions at once can understate your real combined risk.

## Applying It in Practice

1. **Build a real sample first.** Estimate win rate and average reward-to-risk from dozens to hundreds of actual trades — tracking everything in R-multiples, as covered in [Lesson 6](/en/strategies/risk-reward-money-management/), makes this far easier.
2. **Don't use the raw f\*.** Most practitioners start at half Kelly or lower, and drop to quarter Kelly when conviction or sample size is thin.
3. **Set a hard cap regardless of what Kelly says.** Many traders cap any single position at a fixed ceiling (say, 20-25% of the account) no matter how high the calculation comes out.
4. **Recalculate periodically.** As a strategy's real performance shifts, its Kelly fraction should shift with it — if the win rate is trending down, the bet size should come down too.

## FAQ

### Can Kelly sizing be used for options or futures?
The underlying logic doesn't care about asset class, but options have a more non-linear payoff (loss capped at the premium, gains that can spike sharply), and leveraged instruments mean your effective bet size can be much larger than the margin you post — both need to be folded into the calculation explicitly.

### If I don't know my true win rate and reward-to-risk, is Kelly useless?
Not knowing the exact values is the normal situation, not an exception — that's precisely why fractional Kelly exists. If your estimate is uncertain, sizing more conservatively (quarter Kelly or lower) is the reasonable response to that uncertainty, not a reason to abandon the framework.

### Should beginners apply Kelly sizing right away?
No. Kelly assumes you already have a strategy with a validated win rate and reward-to-risk. If you haven't confirmed your approach has a real statistical edge yet, the priority is building that sample size with small, fixed risk per trade (say 1-2% of the account, per [Lesson 6](/en/strategies/risk-reward-money-management/)) — not computing a Kelly fraction for an edge you haven't proven exists.

## Summary

- The Kelly Criterion (f\* = W - (1-W)/R) calculates the bet size that maximizes long-run compound growth, given a win rate and reward-to-risk ratio.
- The optimum exists because of compounding asymmetry: bet too little and growth is slow; bet too much and a single large loss can erase many prior wins.
- Full Kelly is extremely volatile in practice, so fractional Kelly — usually half or quarter Kelly — is the far more common real-world approach, trading a modest amount of growth for a much smoother ride.
- The biggest risk is estimation error in the inputs, not the math itself: overestimating win rate even slightly can sharply raise the risk of ruin, and the formula ignores correlation across positions.
- In practice: estimate from a real sample, scale down to fractional Kelly, and set a hard position cap regardless of what the raw calculation suggests.
