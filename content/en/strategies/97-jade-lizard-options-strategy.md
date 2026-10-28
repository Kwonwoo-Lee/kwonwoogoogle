---
slug: jade-lizard-options-strategy
title: "Jade Lizard Options Strategy: Selling Premium With No Upside Risk"
description: "How the Jade Lizard combines a short put with a call credit spread to remove upside risk entirely, with strike rules and a short strangle comparison."
order: 97
updated: 2026-10-28
keywords: ["jade lizard options strategy", "jade lizard explained", "short put call credit spread", "no upside risk options strategy", "jade lizard vs short strangle", "how to trade jade lizard", "options credit strategy IV rank", "jade lizard strike selection"]
seo_audited: 2026-10-28
---

## Starting From the Short Strangle's Weak Spot

Lesson 58 on the [iron condor and credit spreads](/en/strategies/iron-condor-credit-spread/) covered adding a long leg on both sides so that both upside and downside losses are capped from the start. Plenty of premium sellers skip that and just sell a naked put and a naked call — a **short strangle** — instead. With no long legs to pay for, the credit collected is larger and there are only two legs to manage, so commissions are lower. The catch is that a short strangle has no ceiling on loss in either direction. If the stock makes a big enough move either way, the loss keeps growing.

The **Jade Lizard**, the subject of this lesson, sits between those two extremes. The put side stays a plain short put, same as the short strangle — no long leg underneath it. The call side gets the iron-condor treatment: a long call is added above the short call, turning it into a call credit spread. The result is a deliberately asymmetric structure: downside risk stays wide open exactly like a short strangle, while upside risk can be made to disappear entirely if one condition holds. The options education channel tastylive (then tastytrade) popularized this structure in the mid-2010s, and it keeps showing up in options content built around stocks that have sold off and now carry elevated implied volatility.

## The Structure: One Short Put Plus a Call Credit Spread

A Jade Lizard has three legs.

- **One short put.** Sell a put with a strike below the current price. There's no long put underneath it, so if the stock falls far enough, the loss is open all the way down to zero.
- **One short call.** Sell a call with a strike above the current price.
- **One long call.** Buy a call at a strike above the short call. Looked at on its own, this call leg is the same bear call spread covered in Lesson 58.

There's exactly one condition that makes the structure work: **the total credit collected across all three legs has to exceed the width of the call spread** (the distance between the short call strike and the long call strike). When that holds, the maximum loss the call spread can produce — width minus the credit collected on that spread alone — is more than covered by the premium already banked from the short put. However high the stock goes, the position never loses money on the way up. That's the "no upside risk" in the name. Skip that condition and you've built something that's shaped like a Jade Lizard but still carries real upside risk.

<figure class="diagram">
  <img src="/static/img/charts/en/jade-lizard-options-strategy.svg" alt="Payoff diagram of the Jade Lizard options strategy at expiration, showing unlimited loss below the short put strike, maximum profit flat between the short put and short call strikes, and loss flattening at or above zero past the long call strike" loading="lazy">
  <figcaption>Below the short put, risk stays open exactly like a short strangle. Above the long call strike, loss never goes below zero. That asymmetry is the entire point of the structure.</figcaption>
</figure>

## Why It Can Work: Turning Put-Call Skew Into an Asymmetric Trade

The Jade Lizard leans on the **put-call skew** covered in Lesson 95 on [volatility skew and the 25-delta risk reversal](/en/strategies/volatility-skew-risk-reversal/). In single-stock and index options markets, there's persistent hedging demand for downside protection, so puts at a given delta commonly trade with higher implied volatility — and therefore a richer price — than calls at the same delta. A relatively pricier put side means that, comparing strikes at similar deltas, a single short put is more likely to collect enough credit on its own to cover the entire width of the call spread sitting on the other side.

The setup tends to look most attractive on **a stock that has already sold off hard and now carries elevated implied volatility**. Stocks in that condition often share a few traits at once.

1. Many traders lean toward a view that the stock is more likely to base or bounce than keep falling sharply, which fits a neutral-to-mildly-bullish stance better than an aggressively bearish one.
2. Elevated IV means the short put alone pays a fatter premium.
3. Because the stock has already fallen a long way, a trader who doubts it's about to explode higher can reasonably give up a small amount of credit (the long call) to erase upside risk entirely rather than leave it open.

That's a description of when the setup tends to get used, not proof that it carries a statistical edge in that regime. Put-call skew varies by stock and by moment, and strike combinations that fail the core condition (total credit exceeding the call spread's width) are common.

## A Worked Example: One Cycle in Numbers

Say a hypothetical stock has fallen 30% and now trades at $60, with implied volatility running higher than its recent average. There are 35 days to expiration.

**First attempt at the legs**

| Leg | Strike | Direction | Premium |
|---|---|---|---|
| Short put | $52 (delta ≈ -0.20) | Sell | Collect $1.60 |
| Short call | $68 (delta ≈ 0.18) | Sell | Collect $0.95 |
| Long call | $72 | Buy | Pay $0.45 |

- Call spread net credit = 0.95 − 0.45 = **$0.50**; call spread width = 72 − 68 = **$4**
- Total credit = 1.60 (put) + 0.50 (call spread) = **$2.10 ($210 per contract)**
- Check the condition: is $2.10 greater than the $4 width? **No.** This combination doesn't clear the bar yet.

To satisfy the condition, either pull the short put strike closer to the current price (to collect more premium) or narrow the call spread. Moving the short put to $54 (delta ≈ -0.25) brings in $2.80, for a total credit of 2.80 + 0.50 = **$3.30** — still short of the $4 width. Narrowing the call spread to $3 wide (short call at $68, long call at $71) while keeping the same $0.50 net credit gets total credit to **$3.30**, which now clears a $3 width.

**Final structure (condition satisfied):** short put at $54 ($2.80 collected) plus a $68/$71 call credit spread ($0.50 collected). Total credit = **$3.30 ($330 per contract)**.

- **Stock expires between $54 and $68:** all three legs expire worthless, and the full $330 is profit.
- **Stock expires above $71 (say, $80):** the call spread takes its maximum loss — (width $3 − call spread credit $0.50) × 100 = $250 — but the $280 collected from the short put more than covers it, leaving a $30 profit. No matter how high the stock goes from here, this structure never loses money on the way up — that's the "no upside risk" at work.
- **Stock falls to $45:** the call spread expires worthless, keeping its full $50, but the short put loses (54 − 45) × 100 − 280 = $620. With no long put underneath it, this loss keeps growing the closer the stock gets to zero.
- **Downside breakeven:** 54 − 3.30 = **$50.70**. Below that at expiration, the trade is a net loss.

## Jade Lizard vs. Short Strangle: What You Give Up, What You Get

| | Short Strangle (2 legs, both naked) | Jade Lizard (3 legs) |
|---|---|---|
| Downside risk | Unlimited — no long leg | Unlimited — same short put, unchanged |
| Upside risk | Unlimited — no long leg | Zero, if the core condition holds |
| Credit collected | Larger — nothing paid for a long leg | Smaller — reduced by the cost of the long call |
| Number of legs | 2 | 3 |
| Margin requirement | Priced for unlimited risk on both sides | Lower on the call side, priced as defined risk |
| Best-fit view | Direction-agnostic — stays in range | Neutral to mildly bullish, more worried about downside than a spike up |

As the table makes clear, the Jade Lizard doesn't beat the short strangle for free — erasing upside risk costs part of the credit you'd otherwise collect. That trade-off makes sense when a trader believes a sudden sharp rally is unlikely but still doesn't want to be exposed to one if it happens. If the bigger worry runs the other way — more concern about a sharp drop than a rally — the mirror-image version, the **Reverse Jade Lizard** (one short call plus a put credit spread, erasing downside risk while leaving the upside open), is the structure to reach for instead. This lesson focuses on the standard version, but flipping the legs left-to-right is all it takes to get there.

## Picking Strikes

As with the iron condor in Lesson 58, using **delta** as a rough stand-in for the probability a strike finishes in the money is the common shortcut in practice. Options education content, tastylive's among them, commonly cites a starting range along these lines — worth repeating that it's a convention, not a fixed statistical rule.

- **Short put:** often chosen around -0.20 to -0.30 delta. Thanks to put-call skew, strikes this far out-of-the-money on the put side can still pay a surprisingly rich premium.
- **Call spread (short/long call):** the short call is often chosen around 0.15–0.20 delta, with the long call one or two strikes further out — but the width is frequently worked backward from the requirement that total credit beat it, rather than picked first. Too wide a spread makes the condition hard to clear; too narrow and the call spread's own credit shrinks so much that it's hard to clear for a different reason.
- **Don't force a combination that doesn't clear the bar.** As in the worked example, when the first set of strikes fails the "total credit exceeds call spread width" test, the fix is to narrow the spread or adjust the short put strike — not to pretend the condition is close enough. Squeezing the call spread narrow enough to force the math to work can shrink the call side's credit to almost nothing, at which point the position is barely different from holding the short put alone.

## Managing the Position

- **The 50% profit-take convention.** The same logic from Lesson 58's iron condor applies here: options education commonly cites closing around 50% of max profit rather than holding to expiration, on the view that the gamma risk taken on to capture the remaining half isn't worth it compared to locking in what's already been earned.
- **If the stock drifts toward the short put.** Since downside risk is uncapped, a common response when price approaches the short put strike is to close the call spread first — banking part of the credit it collected — and then reassess the short put on its own, including where the stop-loss level should sit. Rolling the short put to a lower strike and a later expiration is another option, but it only defers the loss rather than solving the underlying problem.
- **If the stock runs toward the short call.** If the core condition held from the start, this is in theory a no-loss zone, so there's less urgency to react — though rolling the call spread to higher strikes to capture more time value is still a reasonable adjustment.
- **Watch for early assignment.** Both the short call and short put are American-style and can be assigned before expiration. A short call sitting near an ex-dividend date carries a meaningfully higher early-assignment risk, so it's worth checking the dividend calendar ahead of time.

## Limitations and Pitfalls

- **Downside risk is still unlimited.** The "no upside risk" framing can make a Jade Lizard sound safer than it is overall, but the put side is an uncovered short put with no floor. A large additional drop — an earnings shock, a broad sector selloff — can keep adding to the loss.
- **Forcing the condition can push strikes into worse territory.** When total credit doesn't clear the call spread's width, the fix involves pulling the short put closer to the money (adding risk) or narrowing the call spread unrealistically. It's worth checking that fixing the math doesn't quietly push the position past the risk level originally intended.
- **The credit collected is smaller than a comparable short strangle's.** That's the cost of removing upside risk, so a bigger raw profit number on the strangle doesn't automatically make it the better trade — the two tools carry genuinely different risk profiles.
- **Gap risk around news.** A sharp overnight gap down on earnings or other news can push the short put's loss well past what its delta implied as a rough probability. As covered in Lesson 38 on [IV crush](/en/strategies/iv-crush-earnings-options/), positions that straddle an earnings date deserve a more conservative approach.
- **Put-call skew doesn't always cooperate.** The relative richness of puts that makes this structure easy to build is an average tendency, not a constant across every stock and every moment.

## FAQ

### Is the Jade Lizard beginner-friendly?
Managing three legs at once, and checking the "total credit exceeds call spread width" condition every single time, makes it a step up from simpler structures. It's worth getting comfortable with credit spreads and iron condors first before adding this one.

### What happens if the condition isn't met?
The position is shaped like a Jade Lizard but still carries real upside risk — it just hasn't been removed. Check the actual numbers every time rather than assuming the structure's name guarantees the outcome.

### What kind of stock is this usually used on?
It tends to show up on stocks that have already sold off and now carry elevated implied volatility, paired with a neutral-to-mildly-bullish view that a sharp rally is unlikely. That describes when the setup gets reached for, not a guarantee that it will be profitable under those conditions.

## Summary

- A Jade Lizard combines one short put with a call credit spread (short call plus long call) into a three-leg structure that removes all upside risk when total credit collected exceeds the width of the call spread.
- Downside risk is unchanged from a plain short strangle, since the put side has no long leg underneath it — that asymmetry is the whole point of the structure.
- Put-call skew tends to make puts relatively more expensive than calls at comparable deltas, which is why the core condition is often easier to clear on stocks that have already sold off and now carry high IV.
- Strikes are picked using delta as a rough probability proxy, and when the first combination fails the credit-versus-width test, the fix is to adjust the short put strike or narrow the call spread — not to force the trade through at a worse risk level.
- Despite the "no upside risk" name, downside risk stays wide open, so gap risk and early-assignment risk still need to be weighed before the picture is complete.
