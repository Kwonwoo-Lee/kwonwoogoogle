---
slug: trend-pullback-ma
title: "Trend-Following Done Right: A Full Breakdown of the MA Pullback Re-Entry Strategy"
description: "A rules-based trend-following strategy that defines trend via EMA(9)/EMA(21) alignment and enters only when a pullback resumes in the trend direction — analyzed through the lens of win rate vs. R-multiple."
order: 9
updated: 2026-08-03
keywords: ["moving average pullback strategy", "trend following strategy", "EMA crossover strategy", "trend pullback strategy", "R multiple"]
---

## How This Differs From the Golden Cross in Lesson 1

Lesson 1 covered the basics of moving-average crossovers (golden cross / death cross). The strategy in this lesson turns that concept into an actual trading rule, and there's one key difference.

- Lesson 1's golden cross: enter "the moment the fast MA crosses **above** the slow MA"
- This strategy: with the trend already confirmed, enter "the moment a pullback (retracement) resumes in the trend direction"

Why does this distinction matter? The moment a cross just happened, the trend hasn't really been "confirmed" yet. A pullback re-entry, on the other hand, rides a trend that's already well-established, while still getting in at a **relatively favorable price** (the pullback) rather than chasing an already-extended high or low. This is the coded version of what professional traders mean when they say "confirm the trend, then enter on the pullback."

## The Exact Entry Rules

This strategy has two stages: **trend determination** and the **re-entry trigger**.

### Stage 1: Trend Determination (EMA 9 vs. EMA 21)

- `EMA(9) > EMA(21)` → uptrend (bullish)
- `EMA(9) < EMA(21)` → downtrend (bearish)
- If they're equal, the trend is considered unclear, and no signal is generated at all.

The specific numbers — fast EMA 9, slow EMA 21 — aren't magic; they're simply a widely-used combination in practice. What matters isn't the numbers but **the principle: define trend direction from the alignment of two EMAs, and only trade in that direction.**

### Stage 2: The Pullback Re-Entry Trigger

Using an uptrend as the example:

1. **Pullback confirmation**: the previous bar's low must have touched or dipped below EMA(9) at that time (`previous low <= previous EMA(9)`).
2. **Resumption confirmation**: the current bar's close must be above the current EMA(9), and also close higher than the previous close.

If both conditions are met, buy. A downtrend mirrors this exactly (previous high touched or rose above EMA(9), then current close below EMA(9) and below the previous close) → sell.

> 💡 Why "the low touched" rather than "the close touched"? A pullback typically produces a candle that briefly wicks into the moving average before closing back in the trend direction. If you require the close to touch the EMA, you'd miss most of these normal pullbacks entirely.

### Stop and Target

The stop is the recent swing low (for buys) or swing high (for sells) over the lookback window (default 10 bars, excluding the current bar). The target uses the default risk/reward ratio of 1.5R (`rr_min`) — 1.5 times the stop distance — the shared default rule applied whenever a strategy doesn't compute its own target directly.

## Why It's Fine for This Strategy to Have a Low Win Rate

The thing that surprises people the most when they first backtest this strategy: **a trend-following strategy hitting only a 35-50% win rate is entirely normal.** The reason is straightforward.

- It often looks like the trend has resumed and you enter, only for that trend to actually be running out of steam (which stops you out).
- But on the entries where the trend genuinely does resume, the stop sits close to the tight pullback zone, while the target often rides the trend much further out — meaning **the R-multiple gets stretched wide.**

For example, a 40% win rate with an average winner of +2.5R and an average loser of -1R gives an expectancy of:

```
Expectancy = (0.40 × 2.5R) + (0.60 × -1R) = 1.0R - 0.6R = +0.4R
```

Even though this looks like "a strategy that loses 6 times out of 10" by win rate alone, it's positive-expectancy over the long run. This is the precise meaning behind the warning in the code comments: **"this doesn't guarantee win rate — you must look at both the win rate and the average R in the backtest results."**

> ⚠️ Conversely, the mean-reversion strategies (covered in the next lesson), which tend to have high win rates, usually win small and occasionally lose big. Don't conclude "this strategy is better" just by comparing win rates — these two families of strategies make money in fundamentally different ways.

## Interaction With the HTF Filter

Like every other strategy, this one must also pass the shared common gates. When the HTF (higher-timeframe) filter is on (the default, `use_htf_filter=True`), a signal only fires when the higher-timeframe trend direction agrees with the LTF trend this strategy determined. In other words, entry is blocked entirely in a situation like "the 5-minute chart looks like a bullish pullback, but the 1-hour chart is in a downtrend" — a safeguard that filters out counter-trend trades against the higher-timeframe bias from the start.

## Summary

- This strategy is a 3-stage structure: "define trend from MA alignment → wait for a pullback → confirm trend resumption → enter."
- The key difference from Lesson 1's simple crossover strategy is that entry happens on a pullback within an **already-confirmed trend**, not the moment a cross just occurred.
- Even with a low win rate (35-50%), a sufficiently large R-multiple can produce positive long-term expectancy — always evaluate a trend-following strategy by looking at win rate and average R together.
- The HTF filter acts as a safety net, blocking entries that run counter to the higher-timeframe trend.
