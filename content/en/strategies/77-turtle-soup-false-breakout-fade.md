---
slug: turtle-soup-false-breakout-fade
title: "Turtle Soup Trading Strategy: Fading Failed 20-Day Breakouts for a Reversal"
description: "The Turtle Soup strategy fades failed 20-day breakouts for a reversal trade: entry, stop rules, and its tie to ICT liquidity sweeps."
order: 77
updated: 2026-10-08
keywords: ["turtle soup trading strategy", "false breakout fade strategy", "20-day high breakout failure", "fade the breakout trading", "Linda Raschke turtle soup", "stop hunt reversal trade", "mean reversion breakout failure", "failed breakout reversal trade"]
seo_audited: 2026-10-08
---

## An Idea Born From Flipping Turtle Trading On Its Head

Lesson 11's [Donchian Channel and Opening Range Breakout (ORB)](/en/strategies/breakout-donchian-orb/) covered the Donchian Channel breakout: buy when the close breaks above the highest high of the last 20 bars, sell when it breaks below the lowest low. That rule, taught by Richard Dennis to the original "Turtles" in the 1970s-80s, is the strategy that made channel breakouts famous in the first place.

But trader Linda Bradford Raschke, active through the 1980s and 90s, asked the opposite question. Trend-following breakout systems like the Turtles' naturally have a low win rate and plenty of false signals — so what if you built a strategy around trading *against* the breakouts that fail? That's exactly what Raschke and Larry Connors introduced in their book *Street Smarts*, under a name that's a direct jab at the system it fades: **Turtle Soup** — because the strategy effectively eats the Turtles' lunch. Where a Donchian breakout rides a breakout that succeeds, Turtle Soup fades a breakout that fails. Same raw material — the 20-day high and low — used in exactly opposite directions.

## Why a Failed Breakout Tends to Snap Back: The Mechanics of Where Stops Pile Up

The logic behind Turtle Soup becomes clear once you think about where other traders' orders actually sit. A 20-day high isn't just an arbitrary number on a chart — it's a price level where several different groups of orders happen to cluster at once.

- **Breakout buyers' entry orders**: traders running trend-following systems like the Donchian breakout place buy orders to trigger the instant price clears that 20-day high.
- **Existing short sellers' stop-loss orders**: traders who sold short at lower prices earlier typically park their protective buy-stops just above that same prior high.

Both groups are sitting on the same type of order — buy — clustered at the same level. So when price finally reaches that level, there's a brief burst of real buying pressure strong enough to push price through it. The catch is that this burst isn't fresh demand from new buyers who believe in the move; it's just resting orders getting filled. Once that pool of orders is exhausted, if there's no genuine follow-through demand waiting above, price has nothing left holding it up and snaps back below the level just as fast as it broke above it. At that point, traders who chased the breakout late are immediately underwater, while the short sellers who already got stopped out can only watch the reversal happen without them. That panic unwind from the trapped breakout-chasers adds extra fuel to the snapback, which is often why the move following a failed breakout can be sharper and faster than you'd expect. In ICT terminology this is called a "liquidity sweep" — the same underlying mechanism covered in Lesson 5's [ICT Smart Money Concepts Basics](/en/strategies/ict-smart-money-basics/), just described through a classical, rule-based counter-trend lens decades earlier.

## Entry Rules: Wait for the Failure to Be Confirmed, Not the Breakout Itself

The core of Turtle Soup is that you don't enter at the moment of the breakout — you enter at the moment the breakout is **confirmed to have failed**. The typical rule set looks like this:

1. **Define a valid level**: use the highest high (or lowest low) of the prior 20 trading days as the reference level. Most versions also require that prior extreme to be at least 3-4 trading days old — a "seasoned" level rather than one set just yesterday, since a brand-new high may not yet have enough resting orders stacked against it.
2. **The sweep occurs**: price (usually just the wick — the high or low) briefly trades beyond that level.
3. **Confirm the failure**: the close of that same bar, or the next one, moves back **inside** the range. The wick poking through while the close snaps back in is the whole signal; if the close instead holds beyond the level, that's treated as a genuine breakout and the Turtle Soup signal is invalidated.
4. **Enter**: once the close-back-inside is confirmed, enter in the opposite direction — short after a failed high breakout, long after a failed low breakdown — either on the next bar's open or at the confirming bar's close.

A more conservative variant called "Turtle Soup Plus One" is also widely used. Instead of entering right on the bar that confirms the failure, it waits one additional bar before entering. That filters out a few more false signals, at the cost of a worse entry price and occasionally missing the move entirely — a real tradeoff, not a free upgrade.

<figure class="diagram">
  <img src="/static/img/charts/en/turtle-soup-false-breakout-fade.svg" alt="Short entry structure after a failed 20-day high breakout: price wicks above the prior 20-day high, closes back inside the range, triggering entry with a stop just above the wick and a target or time-based exit within 2-6 bars" loading="lazy">
  <figcaption>The sweep of the prior 20-day high with the wick, followed by a close back inside the range, is the entry trigger; the stop sits just beyond the wick, and the exit is whichever comes first — a price target or a time-based exit within 2-6 bars.</figcaption>
</figure>

## Stops and Exits: A Structurally Tight Stop Is the Appeal

One reason Turtle Soup keeps coming up in trading discussions is the **structurally tight stop** it allows. The stop typically sits just beyond the wick that produced the failure signal — just above the high that got swept (for a short) or just below the low that got swept (for a long). Price has already shown you, once, exactly where it failed to go further, so there's comparatively little reason to give the trade more room than that.

Exits generally follow one of two approaches, often combined:

- **A price target**: the opposite side of the recent range, a prior swing point, or the range's midpoint.
- **A time-based exit**: because Turtle Soup is fundamentally a short-term mean-reversion play, many traders set a hard limit of 2-6 bars after entry. If the reversal hasn't reached its target by then, they exit regardless — the fact that the snapback hasn't shown up quickly is itself a signal that the original "false breakout" read may have been wrong.

## A Worked Numeric Example

Suppose a stock has been ranging between $85 and $98 over the past 60 sessions, and the highest close in the prior 20 trading days was $97.50, set six trading days ago — seasoned enough to qualify.

1. Price rallies back toward $97.50 and prints an intraday high of $98.90 — a $1.40 breach of the 20-day high.
2. That day's close, however, comes in at $97.10 — back **below** the $97.50 level. Breakout failure confirmed: Turtle Soup short signal.
3. Short entry near $97.05 on the next bar's open. Stop placed just above the breakout high at $99.10 (about $2.05, or roughly 2.1% of entry price).
4. Target: the midpoint of the 60-day range, around $91.50, or a 4-bar time exit, whichever comes first.
5. Three bars later, price reaches $92.30 near the target and the position is closed — a gain of roughly $4.75, versus a $2.05 stop distance: about a 2.3:1 reward-to-risk outcome.

What matters here is that the stop distance ($2.05) is small relative to the full range of the move (roughly $13). That's the structural reason Turtle Soup keeps getting cited as attractive on a risk/reward basis — but it comes paired with the fact that a tight stop also means **a higher chance of getting stopped out on any given signal**, which ties directly into the limitations covered below.

## Turtle Soup vs. Donchian Channel Breakout: Same Material, Opposite Read

Both strategies use the same raw ingredient — the 20-day high and low — but interpret a break of that level in exactly opposite ways.

| | Donchian Channel Breakout (Lesson 11) | Turtle Soup |
|---|---|---|
| What a breakout means | A new trend is starting | Resting stop orders just got swept |
| Entry trigger | The close breaks past the level | The close comes back inside the level |
| Entry direction | Same direction as the breakout | Opposite direction to the breakout |
| Favorable regime | A sustained, trending market | Range-bound/overextended conditions with repeated false breakouts |
| Classic weakness | Repeated stop-outs on false breakouts in a sideways market | Loses if a strong trend reversal makes the breakout genuine |
| Stop placement | The channel's midline (relatively wide) | Just beyond the breakout wick (relatively tight) |

The most striking row in that table is "classic weakness." The exact market condition that hurts Donchian the most — a range-bound market full of false breakouts — is the exact condition where Turtle Soup tends to do best. The two strategies are close to mirror images of each other, each one's weak spot being the other's strong suit. That also means they can be used as complements rather than competitors: a trend-strength filter like ADX (see Lesson 55's [ADX/DMI Trend Strength](/en/strategies/adx-dmi-trend-strength/)) can first classify the current regime as trending or ranging, then route trades to the Donchian-style breakout in a trending regime and to a Turtle Soup-style fade in a ranging one — a regime-filter approach commonly suggested for exactly this pairing.

## When Not to Use It: The Strong-Trend Trap

The biggest risk with Turtle Soup is **mistaking a genuine breakout for a failed one during a strong trend change**. If a stock clears a 20-day high on real news — an earnings surprise, a fundamental shift — and the trend simply continues, a Turtle Soup short will keep getting run over as the "failed" breakout turns out to have been real all along. Many practical implementations address this by invalidating the signal if the breakout keeps extending without ever closing back inside the range. Others add a trend-strength filter — RSI readings at an extreme, or ADX confirming the trend is strong — specifically to sit out Turtle Soup signals when the broader trend looks too strong to fade.

## FAQ

### Why is it okay to use such a tight stop with Turtle Soup?
Because the wick that produced the failure signal is itself the market telling you "I pushed this far and no further." If price goes on to clear that same high again for real, the original "false breakout" read was simply wrong — so placing the stop just beyond that point is the logically consistent choice. The flip side to keep in mind: a tight stop doesn't mean smaller losses in some free sense — it comes bundled with a higher frequency of getting stopped out.

### Is Turtle Soup the same thing as an ICT liquidity sweep?
The core mechanism — sweeping a level where stop and entry orders cluster, then reversing — is essentially identical. The difference is lineage: Turtle Soup is a rule-based counter-trend approach from classical technical analysis dating to the 1980s-90s, while the ICT liquidity sweep is a reinterpretation of the same underlying market structure through the smart money concepts framework that emerged in the 2010s. Different names, different theoretical packaging, but the same underlying skeleton — a swept extreme that snaps back once the resting orders behind it are exhausted.

## Limitations and Caveats

- **The fundamental risk of counter-trend trading**: Turtle Soup trades against momentum by design. In a strongly trending market, losses can stack up repeatedly, which makes strict adherence to the stop rule non-negotiable.
- **Loosely defined confirmation criteria**: whether confirmation requires a close back inside the range or a full candle body back inside, and whether the lookback is 20 days or some other window, varies across sources. Define your own precise rules before backtesting rather than trading on a vague version of "the idea."
- **Thin, unverified evidence base**: most public material on this strategy comes from TradingView community scripts and blog posts rather than independently verified, long-horizon backtests. Any specific win-rate or return claim attached to it should be treated as an unverified claim, not an established fact.
- **Slippage and execution risk**: because the entry depends on a brief sweep-and-reverse sequence, actual fills can diverge meaningfully from the planned price in lower-liquidity names.

## Summary

- Turtle Soup is a counter-trend strategy that fades the false breakouts produced by trend-following breakout systems like the Donchian Channel, introduced by Linda Bradford Raschke and Larry Connors in *Street Smarts*.
- A 20-day high or low attracts both breakout buyers' entries and existing short sellers' stop-losses at the same level, which is the structural reason price can snap back quickly once that level is swept and no fresh demand follows through.
- Entry comes not at the breakout itself but at the moment the close moves back inside the range, with a stop placed just beyond the breakout wick — a setup that can produce a favorable reward-to-risk ratio.
- Turtle Soup and the Donchian breakout read the exact same 20-day extreme in opposite ways, and the regime that hurts one (range-bound, false-breakout-prone markets) tends to favor the other, making the two natural complements under a trend-strength filter.
- The strategy's biggest risk is mistaking a genuine breakout for a failed one during a strong trend change, so it's not recommended as a standalone approach without a trend-strength filter and strict stop discipline.
