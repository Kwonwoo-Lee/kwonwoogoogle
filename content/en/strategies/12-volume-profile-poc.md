---
slug: volume-profile-poc
title: "Volume Profile and POC Reversion: Reading the Market by Volume, Not Price"
description: "Analyzes Volume Profile, a concept that defines support/resistance by 'which price level traded the most volume' rather than by price itself, and the POC reversion strategy built on it."
order: 12
updated: 2026-08-03
keywords: ["volume profile analysis", "volume profile POC", "value area high low VAH VAL", "volume-based support resistance"]
---

## A Different Question From Everything So Far: Not "How Often," But "How Much"

Every strategy covered so far in this course has been based on **price movement** — highs and lows, moving averages, RSI, Bollinger Bands. Volume Profile, covered in this lesson, asks a completely different question: not "where was price," but **"at which price level did the most volume actually trade."**

> ⚠️ Let's be upfront about this one first: the POC reversion strategy in this lesson isn't a technique validated and published by a specific trader — it's a **reconstruction** of a Volume-Profile-based idea that circulates in trading communities, turned into code. The exact rules may differ from the original technique, and it hasn't been thoroughly validated. The goal of this lesson is to explain precisely how this way of thinking exists and how it can be turned into code — not to suggest you trade these exact rules.

## What Is Volume Profile?

Volume Profile slices a period of candle data into price bins and builds a histogram of how much volume traded at each price level. Three key values come out of it.

- **POC (Point of Control)**: the price level where the most volume traded. "The most buyers and sellers transacted at this price" — in other words, **the level where the largest concentration of cost basis sits.**
- **VAH / VAL (Value Area High/Low)**: expanding outward from the POC on both sides, these mark the top and bottom of the price range that contains 70% (`vp_value_area`) of total volume. This range is called the "value area" — the range the market has effectively agreed is a "fair" price.

How it's computed (per the code): each of the last 120 bars (`vp_lookback`) contributes its volume to the price bin containing its typical price ((high+low+close)/3), split across 30 bins (`vp_bins`). Then, starting from the bin with the most volume (the POC), the value area expands outward, always including whichever adjacent bin has more volume first.

> 💡 Why simplify to a single point (typical price) rather than distributing volume across the bar's entire high-to-low range? In a backtesting/live-trading environment that has to repeat this calculation on every single bar, computation speed often matters more than precision. On shorter timeframes, where a single bar's own price range is narrow to begin with, the error from this simplification is considered small — a deliberate trade-off. A more precise approach would distribute a bar's volume across its full high-to-low range, but that comes at a much higher computational cost.

## The POC Reversion Strategy's Entry Rules

The idea: **"the POC is where the largest cluster of cost basis sits, so if price leaves that level and comes back, the people who bought there will buy more near their own cost basis, producing support."**

**Buy conditions (all must be met)**:
1. Over the last 20 bars (`vp_away_bars`), price must have strayed at least 0.4% (`vp_excursion_pct`) above the POC — confirming "it had already traveled far enough away."
2. The previous bar must have retraced back near the POC (within 0.1%, `vp_touch_pct`).
3. The current bar must close back above the POC — confirming "it came back, then got rejected upward again."

Selling mirrors all of this in the opposite direction. **The stop sits on the opposite side of the value area** (VAL for buys, VAH for sells) — if price fully leaves the value area, the entire premise of "support will appear here" is considered broken, so the position exits.

## Why All Three Conditions Are Required

There's a trap you have to be especially careful of when designing this strategy: **you must not enter on the single fact that "price is near the POC."** By definition, the POC is where the most volume has traded, so price naturally tends to spend a lot of time near it. Trading purely because price is "near the POC" would fire several times a day and end up being a meaningless filter in practice.

That's why the three conditions are required **in sequence**: price must first have strayed far enough away (①), then come back (②), then confirm it's rejecting again (③) before entry triggers. To borrow the phrasing from the code comments — "setups like this don't come around often." Requiring all three conditions naturally keeps signal frequency low; if this strategy were firing as often as the others, that would actually be a red flag that the filter isn't working properly.

## Comparing It to the Other Reversion Strategies

The four mean-reversion strategies from the previous lesson (RSI, RSI(2), Bollinger, VWAP) all anchor to **"price itself, or some statistic derived from price movement."** POC reversion is the only one that anchors to **"structural support/resistance created by volume"** — a fundamentally different source of information.

This difference carries real implications in practice. In markets where volume data is inaccurate or unavailable (certain crypto exchanges, OTC markets, etc.), POC reversion simply can't be computed at all, while RSI or Bollinger only need closing prices. Conversely, on a stock where a genuinely large amount of size has piled up at a specific price level (say, from a large institutional accumulation), POC reversion can offer far more compelling support/resistance evidence than RSI ever could.

## Summary

- Volume Profile is a fundamentally different lens that defines support/resistance not by price, but by **where volume concentrated.**
- POC (the most-traded price level) and the value area (VAH/VAL, the 70%-of-volume range) are the core concepts.
- The POC reversion strategy requires "strayed far enough → returned → confirmed rejection again" — all three, in sequence — trading low signal frequency for the tightest possible evidence.
- Remember again that this isn't a validated technique but a community-idea reconstruction — always backtest it against your own data before drawing conclusions.
