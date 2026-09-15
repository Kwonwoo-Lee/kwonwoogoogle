---
slug: ict-silver-bullet-strategy
title: "ICT Silver Bullet Strategy: Trading the 3 Daily Killzones With Sweep + FVG Entries"
description: "Learn the exact Silver Bullet killzone times, the sweep-to-FVG entry sequence, and the Stand Down rule versus Confirm DOL."
order: 54
updated: 2026-09-15
keywords: ["ICT Silver Bullet strategy", "silver bullet trading", "ICT killzone times", "silver bullet FVG entry", "ICT silver bullet 10am killzone", "smart money trading strategy", "futures trading strategy", "silver bullet stand down"]
seo_audited: 2026-09-15
---

## What the Silver Bullet Actually Adds to Lessons 5 and 7

Lesson 5's [ICT Smart Money Concepts Basics](/en/strategies/ict-smart-money-basics/) introduced liquidity sweeps and Fair Value Gaps (FVGs). Lesson 7's [PO3 and Confirm DOL](/en/strategies/po3-confirm-dol/) bundled those ideas into a four-step higher-timeframe checklist plus the broad New York AM killzone (9:30–11:00). The **ICT Silver Bullet** reuses the same underlying building blocks, but answers a much narrower version of one question: *exactly when, during the trading day, is a setup even worth looking for?* Widely attributed to ICT's creator, Michael J. Huddleston, the model restricts new entries to just three fixed one-hour windows out of the full 24-hour day — everything outside those windows is simply not traded.

Think of it this way: if Confirm DOL is "a checklist of conditions that must all line up before you act," the Silver Bullet bolts on a stricter time filter on top of that checklist — **outside these three windows, you don't even look, no matter how good a setup appears to be.** There isn't much new mechanics to learn here. What's worth digging into is why narrowing "when" this aggressively has become so popular, and exactly where that narrowness starts costing you.

## The Three Daily Killzones: Exact Times

The Silver Bullet's defining feature is that it names exactly three one-hour windows as tradeable time, all quoted in **New York time (ET)**.

| Killzone | Time (ET) | Market it lines up with |
|---|---|---|
| London Open Silver Bullet | 3:00–4:00 AM | Right after the London FX session opens |
| AM Session Silver Bullet | 10:00–11:00 AM | 30 minutes after the NYSE cash open at 9:30 |
| PM Session Silver Bullet | 2:00–3:00 PM (some sources extend to 4:00 PM) | Late-day flows ahead of the close |

<figure class="diagram">
  <img src="/static/img/charts/en/ict-silver-bullet-strategy.svg" alt="Top: a New York time daily timeline highlighting the London Open (3-4am), AM session (10-11am), and PM session (2-3pm) Silver Bullet killzones. Bottom: inside a killzone, price sweeps a prior low, a displacement candle forms an FVG used as the entry zone, targeting session-high liquidity" loading="lazy">
  <figcaption>Only three one-hour windows a day (New York time) are treated as tradeable; inside each one, the sequence runs sweep → displacement → FVG entry.</figcaption>
</figure>

The AM session is the one most commonly used. It sits half an hour after the cash open, late enough to skip the roughest opening-bell chop but still early enough to catch the large flows that tend to set the day's direction. The London Open window sees little U.S. participation and is used mostly by futures and forex traders working overnight hours. The PM window targets the late-day repositioning and rebalancing flows institutions often run ahead of the close. **It's worth flagging that Lesson 7's "NY AM killzone" (9:30–11:00) and the Silver Bullet's "AM session" (10:00–11:00) are not the same window.** The Silver Bullet's AM slot deliberately excludes the first 30 minutes after the open — it's a narrower, later-starting subset.

## The Entry Logic: HTF Bias → Sweep → Displacement → FVG

Once the killzone defines *when*, four steps define *what* has to happen inside it before you act.

1. **Lock in an HTF bias first**: before the killzone even opens, the higher timeframe — daily or 4-hour — needs to already show a clear direction. A bullish HTF structure means longs only; a bearish one means shorts only. Walking into a killzone with no pre-formed directional bias is not the intended use of the model.
2. **Wait for a liquidity sweep**: once the window opens, wait for price to briefly poke through a recent, meaningful high or low and snap back — the same sweep mechanic from Lesson 5.
3. **Confirm displacement**: right after the sweep, price needs to move sharply and decisively in the direction of the HTF bias — a strong, wide-range candle. Without that follow-through, the sweep was probably just noise.
4. **Enter on the FVG**: the displacement candle typically leaves behind a Fair Value Gap — the three-candle price gap from Lesson 5. That gap becomes the entry zone; you enter as price returns to it, with a stop just beyond the sweep's extreme (the high or low it poked through).

These four steps are essentially the same sequence as Lesson 7's Confirm DOL checklist (sweep → displacement → FVG → no invalidation). The only real difference is that the Silver Bullet pre-restricts **when you're even allowed to look for that sequence** to three one-hour slots instead of the full trading day.

## The Stand Down Principle: Some Days You Just Don't Trade

Every write-up on the Silver Bullet strategy converges on the same rule: the **Stand Down principle**. If the HTF bias is unclear, if no sweep shows up inside the window, if a sweep happens but displacement never follows, or if no FVG forms — any single missing piece means **you skip that killzone for the day, full stop**. Having three windows doesn't obligate three trades; on a quiet day, the correct outcome can be zero trades across all three. Treat this as the model's built-in guardrail against the common misreading that a fixed time window means a trade is owed.

## Target Sizing: A Rule of Thumb, Not a Guarantee

Write-ups on the Silver Bullet commonly cite an expected move of roughly **5 to 15 points (handles) on index futures** like ES or NQ, and **around 15 pips on major forex pairs**. It's worth being direct about what this number is: it's a frequently-repeated community rule of thumb, not a statistic verified by any published backtest, and actual moves vary a great deal by instrument and by the day's volatility regime. In practice, the more defensible approach is to set the actual target using Lesson 7's DOL priority ladder (today's session high/low → yesterday's high/low → last week's high/low), treating the 5–15 handle figure only as a rough sanity check on what kind of move is realistic, not as the target itself.

## A Worked Example

Say you're trading Nasdaq futures (NQ) long during the AM Session Silver Bullet (10:00–11:00 AM ET).

1. **HTF bias**: both the daily and 4-hour charts show a sequence of higher highs and higher lows — bullish bias confirmed.
2. **9:45 AM**: ahead of the killzone, price is chopping around the overnight low near 18,420.
3. **10:12 AM**: price dips slightly below that low to 18,412, then snaps back immediately — a liquidity sweep.
4. **10:14–10:18 AM**: within four minutes, price rips from 18,412 to 18,468 on a strong bullish candle — displacement confirmed, leaving an FVG between roughly 18,438 and 18,446.
5. **10:31 AM**: price retraces into the upper half of that FVG around 18,444; you enter long there, with a stop just below the sweep's extreme at 18,405 — a 39-point risk.
6. **Target**: the top DOL priority — today's overnight session high at 18,510 — sets the target, roughly 66 points away, for about a 1.7:1 reward-to-risk ratio.
7. **10:52 AM**: price reaches 18,505; with the killzone closing at 11:00, you take partial profit near target and move the stop on the remainder to breakeven.

If step 3's sweep had never produced the displacement candle in step 4, the correct response under the Stand Down principle would have been to skip the AM killzone entirely that day.

## Silver Bullet vs. Confirm DOL: What Actually Differs

Placing the two frameworks side by side makes the relationship clearer.

| | Lesson 7's Confirm DOL | Silver Bullet |
|---|---|---|
| Tradeable hours | Centered on the NY AM killzone (9:30–11:00), extendable | Three fixed one-hour windows only (London Open, AM, PM) |
| Liquidity grading | Splits into low-resistance vs. high-resistance liquidity | Just checks whether a sweep happened (grading is optional) |
| FVG handling | Tracks three ongoing states: respected, invalidated, inverted | Uses the displacement candle's FVG purely as an entry zone |
| Entry confirmation | Four HTF conditions plus a lower-timeframe re-check (double confirmation) | HTF bias plus one in-window sweep/FVG sequence (single confirmation) |
| Target setting | Session → prior-day → prior-week priority ladder | Same priority ladder, plus a 5–15 handle / 15-pip rule of thumb |
| Overall character | A more flexible, more granular filter set | A simpler, more time-boxed execution rule |

The short version: **Confirm DOL is a refined filter for deciding *what* qualifies as a real signal; the Silver Bullet is an execution layer that decides *when* you're even allowed to apply that filter.** In practice, the two aren't mutually exclusive — the Silver Bullet's three-window schedule works well as the base timing framework, while Confirm DOL's liquidity grading and FVG-state tracking can sit inside it as the quality filter for whatever setup shows up in the window.

## FAQ

### What markets does the Silver Bullet work best on?
It's most commonly discussed for index futures (ES, NQ, YM) and major forex pairs. Individual stocks trade on a different liquidity and session structure than futures or FX, so rather than importing the three killzone times as-is, it's worth checking a given stock's own actual volume pattern first.

### Can I just focus on one of the three killzones instead of all three?
Yes — in fact, most people do. Monitoring all three windows every day is a lot to sustain, so many traders pick the single window (often the AM session) that fits their schedule and the market they trade, and specialize in it. Whichever one you pick, it's worth backtesting how often the four conditions actually line up during that specific window before relying on it.

### Why do different sources give different end times for the PM session — 3 PM or 4 PM?
Because there's no single official definition. Some write-ups use 2:00–3:00 PM, others extend it to 2:00–4:00 PM. This kind of variation is expected for a framework that was never formally standardized — it developed through observation and shared practice inside the ICT/SMC trading community rather than through an official specification. Pick a definition from a source you trust and apply it consistently.

## Limitations and Caveats

- **An unvalidated framework**: as flagged repeatedly in Lessons 5 and 7, ICT/SMC concepts broadly are not academically validated methodology, and the Silver Bullet is no exception. The premise that these specific hours are "special" is an observation-based rule of thumb, not a proven statistical edge.
- **The time restriction is itself an opportunity cost**: deliberately ignoring strong trends or clean signals that happen to fall outside the three windows means giving up real opportunities on days when the market moves outside them.
- **The target rule of thumb has real limits**: the 5–15 handle / 15-pip figures are frequently cited but not backtest-verified statistics. Actual moves can run far larger or smaller depending on the volatility regime — earnings season and FOMC days being obvious examples.
- **Overlap with scheduled news**: the AM window in particular can overlap with the lingering effects of 8:30 AM ET U.S. economic data releases, which can blur the line between a genuine liquidity sweep/displacement and plain news-driven volatility.
- **No standardization**: as the PM session's fuzzy end time shows, the fine print varies from source to source. Define your own precise rules, backtest them against historical data, and only then bring them into live trading.

## Summary

- The ICT Silver Bullet restricts new entries to three fixed one-hour windows per day — **London Open (3–4 AM), AM Session (10–11 AM), and PM Session (2–3 PM, New York time)** — and treats every other hour as off-limits.
- Inside a killzone, the sequence is **lock in HTF bias → wait for a liquidity sweep → confirm a displacement candle → enter on the FVG it leaves behind** — functionally the same logic as Lesson 7's Confirm DOL checklist.
- The **Stand Down principle** is the model's core discipline: if any one of the four conditions is missing, you don't trade that killzone that day, even if that means skipping all three windows.
- The commonly cited 5–15 handle (futures) or 15-pip (forex) target is a rule of thumb, not a validated statistic — the DOL priority ladder for actual liquidity levels should take priority over it.
- Confirm DOL refines *what* counts as a valid signal; the Silver Bullet narrows *when* you're allowed to look for one — and combining both is a natural, common approach.
- Like the rest of the ICT/SMC toolkit, this is an observation-based framework without academic validation, so pair it with independent stop-loss placement and position-sizing rules rather than trading it in isolation.
