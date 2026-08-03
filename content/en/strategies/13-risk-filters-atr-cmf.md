---
slug: risk-filters-atr-cmf
title: "Professionals Don't Generate Signals - They Filter Them: ATR Stops, Net-Profit Filters, and Flow Confirmation"
description: "Analyzes the triple risk filter that all 11 strategies must pass through in common: an ATR-based minimum stop distance, a net-profit filter that accounts for fees and slippage, and a Chaikin Money Flow (CMF) based order-flow confirmation."
order: 13
updated: 2026-08-03
keywords: ["ATR stop loss", "Chaikin money flow", "risk management strategy", "fees slippage net profit", "position sizing"]
---

## The Difference Between a Good Trader and a Professional Trader

Lessons 8 through 12 covered 11 strategies, each generating signals from different evidence. But in a real trading system, there's **one more set of 3 common filters** sitting between "a strategy generated a signal" and "an order actually goes out." These filters apply identically no matter which strategy the signal came from.

This is exactly why this lesson might be the most important one in the whole course. **Amateur traders spend most of their energy on "when should I buy."  Professional traders spend just as much — if not more — on "why should I filter this signal out."** Three filters that reject bad entries protect an account for longer than any single great entry idea ever will.

## Filter 1: The Stop Distance Must Be Wider Than "Noise"

A signal firing doesn't send an order immediately. First, the stop distance (the gap between entry and stop) is checked against two separate thresholds.

**① A fixed minimum**: if the stop distance is less than 0.15% (`min_stop_distance_pct`) of the entry price, the signal is discarded. There's always some lag and slippage between the bar the signal was computed on and the moment the order actually fills. If the stop distance is narrower than that discrepancy, the stop level itself becomes meaningless from execution-timing price differences alone, even when the signal calculation was correct.

**② A minimum relative to the instrument's own typical volatility (ATR)**: if the stop distance is less than 0.5x (`min_stop_atr_mult`) the 14-bar ATR (`atr_period`), it's discarded too. Why isn't the fixed ratio (①) enough on its own? A "flat 0.15%" is too loose for a quiet instrument that barely moves all day, and effectively meaningless for a highly volatile one (especially crypto) that can swing several percent in a single day. For example, put a 0.15% stop on an instrument with an average daily range of 3%, and even a correctly-called direction gets stopped out by ordinary price noise before it has a chance to work. **Using each instrument's own "typical amount of wiggle" as the floor for stop distance is what prevents a correct call from getting cut by noise alone.**

> 💡 These two checks aren't about "making stops tighter" — they're about **"not setting stops so tight they become meaningless."** The goal isn't to widen your stops; it's to filter out signals whose stop, as calculated, was already too tight to mean anything.

## Filter 2: There Must Still Be a Profit After Fees and Slippage

The second filter calculates "the actual net profit you'd pocket if price reaches the target."

```
Cost = (fee rate × (entry + target)) + max(0, slippage) × entry
Net profit = |target - entry| - cost
```

If this net profit is zero or negative, or less than 1.0% (`min_net_profit_pct`) of the entry price, the signal is discarded.

An important detail here: **exit is assumed to fill via a limit order, so exit slippage is not included in the cost.** Entry is assumed to fill at market (so slippage is applied there), but hitting the target is assumed to fill via a limit order placed in advance. Matching the backtest's fill assumptions exactly to how live-trading costs are calculated is done for one specific reason: **to prevent backtest results and live results from diverging simply because they made different assumptions.** This guards against one of the most common mistakes professional quant traders make when building a system — if your backtest is sloppy about fees while live trading uses different fill assumptions, backtest performance and live performance will keep drifting apart for no discernible reason.

**Why this filter matters**: even when a target looks perfectly logical, if the risk/reward ratio only barely clears 1.5R, there may be little to nothing left once fees and slippage are subtracted — or it could even go negative. This filter matters most for high-frequency, scalp-style strategies — the signal itself might be "correct," but filtering out signals with "nothing left to eat" is what actually determines the long-term equity curve.

## Filter 3: Don't Enter When Order Flow Is Flatly Opposed

Candle data (OHLCV) alone can't show you the actual order book. Instead, this uses **the volume-weighted position where a candle closed within its own range** to estimate buying vs. selling pressure — this is Chaikin Money Flow (CMF).

- Closing near the high = buyers won that bar → bullish bias (+)
- Closing near the low = sellers won that bar → bearish bias (−)

The CMF over the last 20 bars (`pressure_period`) is blended 50/50 with the buy/sell bias of the single most recent bar to produce a final score (from −1 to +1). Depending on how strongly this score agrees or disagrees with the signal's direction relative to a threshold (default 0.15, `pressure_threshold`), there are two modes:

| Mode | Behavior | Character |
|---|---|---|
| `confirm` (default) | Entry allowed **only if** the flow score exceeds the threshold **in agreement** with the signal's direction | Strict — requires clear agreement to enter |
| `block` | Entry blocked **only if** the flow score exceeds the threshold **against** the signal's direction | Lenient — blocks only on a clear opposite reading |

The default is `confirm` mode. In other words, if "the price pattern says buy, but the actual tug-of-war within that bar shows sellers winning," entry is held back. If there's no volume data to judge from, or too few bars, the filter doesn't block — it lets the signal through (the same "don't block conservatively when there's no information" policy applied consistently across every filter in this system).

> ⚠️ Be clear-eyed about this filter's limits: it isn't looking at a real order book — it's **an approximation of order flow based on where a single candle happened to close.** If a large institution is quietly accumulating size across several bars, this indicator may not catch it at all.

## What the Three Filters Together Produce: "A Signal Is Necessary, Not Sufficient"

A strategy generating a signal means "a candidate entry has appeared" — not "you should buy right now." To actually reach an order, in sequence:

1. The strategy's own specific conditions (covered in Lessons 8-12) must be satisfied, and
2. The stop distance must be wider than noise level (Filter 1), and
3. It must clear a minimum profit threshold after all costs (Filter 2), and
4. Order flow must not be flatly opposed (Filter 3)

All four must be passed for a real signal to result. The advantage of this structure is that **you never have to rebuild risk-management logic from scratch every time you add a strategy.** Because all 11 strategies inherit this same triple filter automatically, designing a new strategy only requires focusing on "when should this fire a signal" — whether that signal is actually worth trading is already validated by the shared layer.

## Summary

- Filters that reject bad entries protect an account longer than any single good entry idea.
- **ATR-based minimum stop**: a stop tighter than an instrument's typical volatility just gets cut by noise first.
- **Net-profit filter after fees and slippage**: a risk/reward ratio that looks fine on paper can leave nothing once costs are subtracted. Matching backtest and live fill assumptions is also this filter's job.
- **CMF order-flow confirmation filter**: holds back when the estimated buy/sell bias (from where a candle closed) flatly opposes the signal — but always remember this is an approximation, not a real order book.
- No matter which strategy generates it, a signal that fails to clear this triple filter is treated as if it never existed.
