---
slug: ifvg-po3-three-tiers
title: "Splitting IFVG+PO3 Into 3 Tiers Reveals What Actually Matters"
description: "Break down a combined liquidity-sweep + inverted-FVG entry signal into three strength tiers, and dissect exactly which conditions actually drive win rate and R-multiple."
order: 8
updated: 2026-08-03
keywords: ["fair value gap trading", "liquidity sweep strategy", "ICT scalping strategy", "IFVG PO3 strategy", "day trading strategy"]
seo_audited: 2026-08-15
---

## Not All Signals Carry Equal Weight

In the previous lesson, you learned PO3 (Accumulation → Manipulation → Distribution) and the Confirm DOL checklist. When you actually try to build an automated system around this idea, you run into an interesting problem: **how strictly you require the two conditions — "swing sweep" and "inverted FVG (IFVG)" — produces completely different systems.**

Implement this and run a backtest, and here's what happens: requiring **both** conditions **simultaneously** produces rare but well-founded signals. Requiring **either one alone** produces 3-5x more signals, but the extra volume comes mixed with low-conviction entries that drag down the overall win rate. This lesson dissects the three graded versions and explains, from a professional trader's perspective, why each behaves so differently.

## The Exact Definition of Each Tier

| Tier | Name | Requirement | Signal frequency | Strength of evidence |
|---|---|---|---|---|
| Tier 1 | IFVG+PO3 (strict) | Swing sweep **AND** current price sitting inside an FVG that inverted in the same direction | Low | Strongest |
| Tier 2 | PO3 sweep only | Swing sweep only (no FVG confirmation) | Medium | Medium |
| Tier 3 | IFVG re-entry only | Price inside an inverted FVG zone only (no sweep confirmation) | High | Weakest |

### Tier 1: Only Where a Sweep and an IFVG Overlap

The strictest condition. In sequence:

1. Price must wick through a recent swing high or low (over the last `swing_lookback`, default 10 bars) and close back the other way (a sweep).
2. An FVG that was formed in the **opposite** direction of the sweep must have flipped to **inverted** by the time of the sweep. For example, if you got a high sweep (a bearish signal candidate), the FVG that was originally bullish must already be invalidated and now re-flagged as a resistance zone.
3. The current close must sit **inside** that inverted FVG's range (top to bottom) for entry to trigger.

In other words: entry fires only when "the spot where liquidity got swept" and "the spot where a price gap flipped into support/resistance" **land at the same place**. Two independent pieces of evidence pointing to the same conclusion — this is exactly what professional traders call "confluence," coded literally.

> 💡 Practical tip: for a confluence-based strategy, the sheer scarcity of signals is itself a risk-management tool. If you get impatient because nothing's fired all day and loosen the conditions, you've effectively downgraded this strategy to Tier 2 or Tier 3 without realizing it.

### Tier 2: Sweep Confirmation Only (Skip the FVG Check)

Same as Tier 1 minus the FVG requirement — a sweep alone triggers entry. A single candle that wicks through a swing high/low and closes back is the entire basis.

The biggest weakness of this version is that **there's no way to distinguish a genuine liquidity sweep from just one noisy candle.** In high-volatility periods, candles that briefly poke past a swing level and snap back can happen multiple times a day, and this strategy fires every time. The "liquidity freshness filter" covered later partially compensates for this weakness.

### Tier 3: Inside an Inverted FVG Zone (Skip the Sweep Check)

The mirror image: drop the sweep requirement, and enter on the single fact that "price is inside an inverted FVG zone." The entire logic rests on one assumption — "this price gap flipped once, so it'll keep acting as support/resistance going forward."

This is the weakest evidence of the three, because it makes no attempt to distinguish whether price entering that zone represents a "meaningful pullback" or just "passing through." Include this tier in a backtest and it's almost always the one that inflates trade count the most — and check the per-strategy win-rate table, and it's commonly the worst performer of the three.

## Why Split Into Three Instead of One Combined Strategy

If you combine all three conditions with an "OR" in practice (enter if any one is satisfied), it looks like more active trading — which seems appealing on the surface. But this creates a **fatal problem**: the backtest P&L for all three tiers gets mixed together, and you can no longer tell whether the profit came from a handful of Tier 1 signals, or whether Tier 3 signals were quietly eating away at that profit the whole time.

This exact practice — **signal-source attribution** — is something every professional trader does when validating a system. Register the three tiers as separate strategies and run the backtest, and you get win rate, average R, and trade count broken out per tier. That lets you answer questions like:

- Does Tier 1 have a noticeably higher average R despite fewer trades?
- Does turning on Tier 2 in addition improve or worsen the account's overall expectancy?
- Is Tier 3 better left off entirely?

> ⚠️ If all three tiers are enabled, they're checked in registry order (Tier 1 → Tier 2 → Tier 3), and only the first signal found is used. In other words, if the Tier 1 condition is met, Tiers 2 and 3 aren't even checked — the stronger-evidence signal always takes priority.

## Liquidity Freshness Filter: Even Sweeps Have Grades

A separate filter exists to patch Tier 2's weakness (sweep-only). It distinguishes whether the swing level that was just swept is a **"first-touch" spot or one that's already been tested several times**.

- Lookback window: last 50 bars (`liquidity_freshness_lookback`)
- Tolerance for counting as "the same spot": within 0.05% of the level (`liquidity_freshness_tolerance_pct`)
- Touch count still considered "fresh": 1 or fewer (`liquidity_freshness_max_touches`)

With this filter on, sweeps of a swing level that's already been tested twice or more — a "High Resistance" spot — get filtered out. Only sweeps of a "Low Resistance," first-touch spot count as signals.

Worth flagging: professional traders genuinely disagree on this point. Some argue "a first-touch level still has undigested liquidity, so the sweep carries more force," while others argue the opposite — "a level that's been tested multiple times has more participants defending it, so the bounce is stronger." This filter encodes the first interpretation, and it defaults to off (`use_liquidity_freshness_filter=False`) — a signal that it's an unvalidated assumption, and its actual effect needs to be confirmed by backtest before turning it on.

## Summary

- The same "PO3+FVG" idea produces completely different risk/reward profiles depending on how strictly you require the conditions.
- Tier 1 (sweep+IFVG confluence) has rare but well-founded signals; moving toward Tier 3 (IFVG only) increases frequency at the cost of weaker evidence.
- Lumping multiple tiers into one strategy hides which one is actually generating profit — **always attribute by signal source, separately.**
- Filters that are "plausible but unvalidated," like liquidity freshness, should start off by default and only get turned on once you've confirmed their effect with data.
