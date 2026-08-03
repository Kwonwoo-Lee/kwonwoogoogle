---
slug: mean-reversion-four-ways
title: "Four Flavors of Mean Reversion: RSI, RSI(2), Bollinger Bands, and VWAP Compared"
description: "Four pullback strategies that all sit under the 'mean reversion' umbrella but anchor to completely different baselines - trend EMA, long-term EMA, a band, and VWAP. Compares their exact entry rules and risk character."
order: 10
updated: 2026-08-03
keywords: ["RSI oversold bounce", "Connors RSI2 strategy", "Bollinger band reversion", "VWAP deviation reversion"]
---

## One Step Further Than Lesson 3: Reverting "From What," Exactly?

Lesson 3 covered the core idea of mean reversion — "price eventually reverts to the mean." In practice, how you define "the mean" produces entirely different strategies. This lesson lines up four strategies that each anchor to a different baseline, side by side.

| Strategy | Baseline | Trigger | Trend filter |
|---|---|---|---|
| RSI oversold bounce | RSI(7) | Drops below oversold (35), then crosses back up | Slope of EMA(50) |
| RSI(2) short-term pullback | RSI(2) | Fires the instant it hits an extreme (10/90) | Above/below EMA(200) |
| Bollinger band reversion | Bollinger Bands(20, 2σ) | Exits the band, then re-enters | None (the band itself reflects trend) |
| VWAP deviation reversion | Session VWAP | Deviates by a set %, then reverses | None (intraday only) |

## ① RSI Oversold/Overbought Bounce (The Textbook Mean-Reversion Play)

**Rule**: in an uptrend (EMA(50) rising), when RSI(7) drops below the oversold line of 35 and then crosses back above 35 on the next bar, buy **at that exact moment**. In a downtrend, when RSI crosses back below the overbought line of 65 from above, sell.

There's an interesting implementation detail here worth noting. **Trend isn't judged by "is the close above the EMA" — it's judged by "is the EMA itself rising (its slope)."** Why? By the time RSI has dropped to oversold, price has almost always already fallen below the EMA — that's the definition of a pullback. If trend were judged by close position relative to the EMA, you'd misjudge the trend as having flipped bearish right at the moment you should be buying, and miss the signal entirely. Testing this with a close-position-based trend filter instead produces literally zero signals across 3,000 bars of synthetic data. This is a lesson worth remembering when designing any mean-reversion strategy: **trying to measure trend and pullback with the same yardstick (close position) makes them contradict each other.**

The stop is the recent swing low/high.

## ② RSI(2) Short-Term Pullback (Larry Connors' Style)

Popularized by Larry Connors, this uses an extremely short RSI period (2 bars). RSI(2) is a highly sensitive indicator that can swing to near 0 or 100 after just a couple of strongly-moving bars.

**Rule**: only look for buys when price is **above** a long-term moving average (EMA 200) — i.e., the premise is that the big picture is an uptrend. In that state, enter **the instant** RSI(2) drops to 10 or below (without waiting for it to bounce back up). Selling requires price below EMA(200) and RSI(2) at 90 or above.

Two fundamentally different points versus strategy ①:

1. **It enters at the extreme itself, without waiting for a bounce** — the RSI oversold bounce waits for confirmation that RSI has crossed back above 35, while RSI(2) enters the moment it hits the extreme. That's an earlier entry, but also one made without confirming "is this actually the bottom."
2. **The trend baseline is much longer and looser** (above/below EMA 200, not the slope of EMA 50). This strategy leans on the assumption that "within a big-picture uptrend, short pullbacks end quickly" — so if the bigger trend itself breaks down, this assumption collapses entirely.

## ③ Bollinger Band Exit and Re-Entry

**Rule**: if the previous bar's low broke below the lower Bollinger Band (20 bars, 2 standard deviations), and the current bar closes back inside the band while closing higher than the previous close, buy. An upper-band breach followed by re-entry is a sell. The stop sits just outside the extreme reached at the time of the breach (the previous/current bar's low or high).

The difference from the RSI family lies in "what counts as oversold." RSI defines oversold based on **the speed/momentum of price change**, while Bollinger Bands define it based on **price's position relative to recent volatility (standard deviation)**. That means in periods of sharply rising volatility, the bands themselves widen, so even fairly large moves don't easily breach them — while in quiet, low-volatility periods, even small moves can breach the bands easily.

## ④ Intraday VWAP Deviation Reversion

**Rule**: when the previous bar's close deviates from the day's cumulative VWAP (volume-weighted average price) by at least `vwap_dev_pct` (default 0.3%), and the current bar bounces back in that direction while closing above (or below) its open, enter.

What's unique to this strategy is **how the target is computed**. It uses whichever is **closer**: the default risk/reward target (1.5R) or VWAP itself. This is because VWAP reversions often stop reverting right around the session's average execution price — using this rule prevents holding out for a full 1.5R target when the reversion has already run its course near VWAP.

Because VWAP resets fresh every session (it's inherently an "intraday-only" concept), this strategy is necessarily day-trading-only — it doesn't translate to swing holding periods.

## What Lining Up All Four Reveals

**What they share**: all four follow the same 3-stage structure — "extreme → confirm reversal → enter." Without exception, they all try to catch **the moment reversal has already begun**, rather than entering early just because "this seems cheap enough already" purely on reaching the extreme (RSI(2) is the sole exception — it enters right at the extreme itself, making its signals earlier, and correspondingly riskier).

**Where they differ comes down to what baseline you anchor to**:

- The RSI family (①②) = **momentum-based** (how fast has price moved)
- Bollinger (③) = **volatility-based** (how far has price strayed relative to recent range)
- VWAP (④) = **volume-weighted average price-based** (how far has price strayed from where most of today's volume traded)

This is exactly why professional traders backtest multiple mean-reversion strategies side by side. Which baseline works best depends on the specific instrument and market regime, and clinging to a single baseline means taking continuous losses whenever that baseline stops fitting.

> ⚠️ Mean-reversion strategies typically show high win rates (bouncing off oversold is a common phenomenon), but **in a strong trending regime, "I thought it was oversold but it just kept falling" can repeat and cause serious drawdowns.** This is the exact opposite risk structure from the trend-following strategy covered in the previous lesson — low win rate but big wins (trend-following) vs. high win rate but occasional big losses (mean reversion). Blending both characters into a single account is itself a risk-management technique.

## Summary

- RSI oversold bounce: momentum-based, enters on confirmed reversal, trend judged by EMA slope
- RSI(2): a shorter, more sensitive indicator that enters right at the extreme, relying instead on a much longer trend filter (EMA 200)
- Bollinger reversion: volatility-based, watches for "exit the band, then re-enter"
- VWAP deviation reversion: volume-weighted average price-based, day-trading only, conservatively targets whichever is closer between the R-multiple target and VWAP
- All four try to catch "the moment reversal has already started" rather than "when it will reverse" — and they diverge on what they treat as "the mean."
