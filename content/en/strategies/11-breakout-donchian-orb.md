---
slug: breakout-donchian-orb
title: "Breakout Strategies in Practice: Donchian Channel and Opening Range Breakout (ORB)"
description: "Analyzes the exact rules and differing risk structures of two breakout strategies: the Donchian Channel, which breaks out of the recent N-bar range, and ORB, which breaks out of the first few minutes of the trading session."
order: 11
updated: 2026-08-03
keywords: ["Donchian channel strategy", "opening range breakout", "ORB strategy", "volatility breakout strategy", "turtle trading strategy"]
---

## Continuing From Lesson 4: How Do You Define "The Range"?

Lesson 4 covered the basics of support/resistance breakouts. The core question for any breakout strategy ultimately comes down to one thing: **what defines the range that a breakout is measured against?** The two strategies in this lesson answer that question differently. One uses a rolling window of "the most recent N bars"; the other uses a fixed time window — "the first few minutes right after the market opens."

## ① Donchian Channel Breakout: A New High Among "The Recent N Bars"

**Rule**: if the current bar's **close** breaks above the highest high of the previous 20 bars (`donchian_period`, excluding the current bar), buy; if it breaks below the lowest low, sell. The catch: **the previous bar must not have already broken out of that range** — meaning only the "first" breakout counts as a signal, and it doesn't re-fire repeatedly while price continues sitting beyond the range it already broke.

This is the standard form of channel breakout made famous by Turtle Trading in the 1970s-80s. The logic is simple: "breaking above the highest high of the last N bars means everyone who sold at this price over that period is now either underwater or paying an opportunity cost — which tends to invite additional buying pressure."

**The stop is the channel's midline** (the average of the highest high and lowest low). Using the opposite side of the channel (e.g., the lowest low on a buy) as the stop would make the stop distance far too wide and badly hurt the risk/reward ratio, so the midline is used as a compromise.

> 💡 A practical observation: Donchian breakouts **lose the most in range-bound (sideways) markets.** Inside a box range, "false breakouts" — briefly poking past the channel and immediately snapping back — repeat over and over, stopping you out each time. On the flip side, once a direction is established, the channel itself keeps widening, letting you ride the trend for a long time. This is the classic trend-following P&L structure: **small, repeated losses in sideways markets, one big win in a trending market.**

## ② Opening Range Breakout (ORB): The Range Formed by "The Market's First Moment"

**Rule**: take the high/low range formed by the first 15 bars (`orb_bars`) right after the New York regular session opens (09:30) as the "opening range." The first bar after that to close outside this range in either direction triggers entry. Breaking above the top is a buy (stop: the range's bottom); breaking below the bottom is a sell (stop: the range's top). Only **one entry per direction, per day**.

There's a fundamental difference from the Donchian Channel here. Donchian's range slides and updates with every new bar (a rolling window), while ORB's range is **fixed once, right when the market opens, and stays that way for the whole day.** So ORB rests on exactly the same premise as the killzone concept from Lesson 7 — "large orders that set the day's direction concentrate right as the market opens." In fact, the very moment this strategy checks for a signal is hardcoded to right after the open, meaning it's essentially the killzone concept baked directly into the time axis.

For assets without a concept of "market open" (like crypto), midnight (00:00) New York time — when the trading date rolls over — is treated as the start of the day instead.

## Comparing the Two Reveals a Design Philosophy

| | Donchian Channel Breakout | Opening Range Breakout (ORB) |
|---|---|---|
| Range definition | Recent N bars (rolling window) | First 15 bars after open (fixed once per day) |
| Signal frequency | Can occur anytime | At most once per direction, per day |
| Premise | "Breaking a recent extreme invites more buying/selling pressure" | "Orders right after the open encode that day's directional bias" |
| Weakness | Repeated false breakouts in sideways markets | No signal at all if the day's opening itself was just noise |

Even though both wear the "breakout" label, **Donchian is grounded in "price's own recent extremes," while ORB is grounded in "market participation patterns at a specific time of day"** — a fundamentally different basis. This is also exactly why the two strategies tend to show strength in different market regimes in practice. Donchian tends to give more reliable signals in markets with sustained volatility and trending behavior, while ORB tends to do better on stocks with directional gaps or concentrated volume right at the open each morning — though this varies by instrument and market, so it always needs to be confirmed with its own backtest.

## Summary

- Donchian Channel Breakout is a classic trend-following breakout strategy based on "the first new extreme among the recent N bars," using the channel's midline as a compromise stop to manage risk/reward.
- ORB treats "the narrow range formed right after the market opens" as the day's reference line, an event-driven strategy that fires at most once per direction per day.
- Both share the common weakness of being vulnerable to false breakouts in range-bound markets, but the basis for defining the range — price's recent extremes vs. a specific time window — is fundamentally different.
- Don't lump strategies together under the single word "breakout" — always ask specifically **what** the breakout is measured against.
