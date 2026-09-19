---
slug: iron-condor-credit-spread
title: "Iron Condor and Credit Spread Strategy: Selling Options Premium With Defined Risk"
description: "How credit spreads and iron condors cap your max loss up front, how to pick strikes with delta, and the 50% profit-take rule, with a worked example."
order: 58
updated: 2026-09-19
keywords: ["iron condor strategy", "credit spread options", "defined risk options selling", "bull put spread explained", "bear call spread", "how to pick option strikes with delta", "IV rank trading", "iron condor 50 percent rule"]
seo_audited: 2026-09-19
---

## Why Cap the Loss Before You Even Enter

Lesson 27 on the [wheel strategy](/en/strategies/wheel-strategy-options/) covered collecting option premium by selling cash-secured puts. The catch is that if you get assigned and the stock keeps falling, there's no hard ceiling on how much you can lose — you're holding real shares. **Credit spreads** and **iron condors**, the subject of this lesson, start from the same idea of selling options for premium, but they're built differently: the worst-case loss is a fixed number you know before you place the trade. However far the stock moves, the amount that can leave your account is capped the moment you open the position.

Lesson 24 on [0DTE options](/en/strategies/0dte-options-trading/) mentioned the iron condor briefly, but that lesson was about running the structure under the extreme time pressure of same-day expiration. This lesson covers the far more common version — credit spreads and iron condors built with roughly 30–45 days to expiration — and goes deep on the structure itself, how to pick strikes, and how to manage the position once it's on. It's a staple of retail options education for a reason: it's one of the more accessible ways to harvest time decay without needing a strong directional call.

## Credit Spreads: Capping a Directional Bet

A credit spread is a two-leg structure built from two options with the same expiration, sold and bought at the same time. The most common version is the **bull put spread**.

- Sell a put with a strike below the current price (you collect premium).
- Buy a put with an even lower strike at the same time (you pay a smaller premium, which caps your downside).

The difference between the two premiums is your net credit, and that's the maximum you can make on the trade. Because you own the lower-strike put, your loss can never exceed the width between the two strikes minus the credit you collected, no matter how far the stock falls. The mirror-image version is the **bear call spread** — selling a call above the current price and buying a further-out call to cap the risk on the upside.

A bull put spread is really a bet that the stock won't fall below a certain level; a bear call spread is a bet it won't rise above one. Either way, a single credit spread is still a directional trade — the difference from a plain naked put or call sale is that the loss if you're wrong has a hard ceiling.

## Iron Condor: Two Credit Spreads at Once

An **iron condor** combines a bull put spread and a bear call spread on the same underlying and the same expiration — a four-leg structure. That means four distinct strikes: a long put below a short put, and a short call below a long call.

The combined credit from both spreads is the maximum profit, and it's fully realized if the stock stays between the short put strike and the short call strike through expiration — both spreads then expire worthless. If the stock instead moves far enough in one direction to push through the long strike on that side, that side's spread takes its maximum loss (width minus total credit collected). Critically, the two spreads can never both lose at the same time — a stock can only move in one direction — so the worst case is bounded by the loss on whichever single side gets breached.

<figure class="diagram">
  <img src="/static/img/charts/en/iron-condor-credit-spread.svg" alt="Comparison diagram showing a bull put spread's payoff, which is only profitable above the short put strike, next to an iron condor's payoff, which is profitable across the range between the short put and short call strikes" loading="lazy">
  <figcaption>Left: a bull put spread is directional — it profits only if price stays above the short put strike. Right: an iron condor is range-bound — it profits anywhere between the two short strikes. Both have their maximum loss fixed from the start.</figcaption>
</figure>

A credit spread is a bet on direction; an iron condor is a bet on range. If you have a real directional view, a single credit spread is the more natural tool. If you're not sure which way price will go but think volatility is priced too rich relative to how far the stock is likely to actually move, an iron condor lets you collect premium on both sides at once.

## Why It Can Work: Probability and the Volatility Risk Premium

Two things put these structures on statistically favorable ground.

First, there's an asymmetry between win rate and payoff size. Credit spreads and iron condors are typically built so the probability of winning is high, but the loss when you're wrong is larger than the gain when you're right — the credit collected is always smaller than the spread width by design. That's not inherently bad; it's the same tradeoff covered in Lesson 6 on [risk/reward and money management](/en/strategies/risk-reward-money-management/), where a high enough win rate can produce a positive expected value even with an unfavorable payoff ratio. The reverse framing applies here: these structures lean on a high win rate to offset a payoff ratio that's working against you, and it's worth being deliberate about that trade rather than treating a high win rate alone as a green light.

Second, there's the **volatility risk premium** covered in Lesson 27. An option's implied volatility reflects what the market currently expects future volatility to be, and across many markets and time periods, realized volatility has tended, on average, to come in lower than what was priced in ahead of time. Option sellers are structurally positioned to collect that gap, and credit spreads and iron condors are a way of collecting it with a hard cap on how much you can lose if that tendency doesn't hold in a given instance.

## Picking Strikes and Width: Delta and IV Rank

As with the wheel strategy, a widely used shortcut is to treat an option's **delta** as a rough proxy for the probability it finishes in the money at expiration. For the short strikes of an iron condor (the short put and short call), traders commonly cite a delta range around 0.10–0.20 — roughly implying an 80–90% chance of that strike finishing out of the money. Worth repeating: this is a convention traders reach for informally, not a statistically validated fixed rule.

The **width** of each spread (the distance between the strike you sell and the strike you buy) is the other major lever. A wider spread pays more credit and risks a larger max loss; a narrower one pays less and risks less. A more disciplined approach is to decide the maximum dollar loss you're willing to take relative to your account size first, then work backward to a width that fits — the same "size the position around a pre-set risk" logic covered in Lesson 42 on [Kelly criterion position sizing](/en/strategies/kelly-criterion-position-sizing/).

**When** you enter matters just as much. Since this is fundamentally a strategy of selling volatility, it's commonly argued that entries work better when implied volatility is elevated relative to that stock's own recent range — often described using **IV rank** or IV percentile. Higher IV means fatter premium for the same delta. That said, elevated IV can also be the market's way of flagging that a large move might actually be coming, so treating a high IV rank alone as a mechanical green light is risky.

## A Worked Example: One Cycle in Numbers

Say a hypothetical stock trades at $100, with 35 days to expiration.

**Bull put spread alone.** Sell the $90 put, buy the $85 put. The net credit on the $5-wide spread comes to $1.20 ($120 per contract).

- If the stock closes above $90 at expiration, both puts expire worthless and you keep the full $120.
- If it closes below $85, you take the maximum loss: (width $5 − credit $1.20) × 100 = **$380**.
- Your breakeven is 90 − 1.20 = **$88.80** — anywhere above that at expiration and you're in profit.

**Adding the iron condor.** On top of that same 90/85 put spread, you also sell the $110 call and buy the $115 call — a bear call spread on the same expiration. That leg brings in another $1.10 ($110), for a total credit of 1.20 + 1.10 = **$2.30 ($230)**.

- If the stock closes anywhere between $90 and $110, both spreads expire worthless and you keep the full $230.
- If it breaks hard in either direction — below $85 or above $115 — only that side's spread takes its max loss: (width $5 − total credit $2.30) × 100 = **$270**.
- Breakevens widen to 90 − 2.30 = **$87.70** on the downside and 110 + 2.30 = **$112.30** on the upside — a wider margin of safety on the put side than the standalone put spread had, thanks to the extra credit from the call side.

In terms of margin, both structures tie up roughly their maximum loss amount. The bull put spread risks $380 to make $120, a theoretical max return of 120 ÷ 380 ≈ 31.6%. The iron condor risks $270 to make $230, or 230 ÷ 270 ≈ 85.2%. The iron condor's higher theoretical return on capital comes from the extra credit collected on the call side shrinking the margin requirement itself. That said, both figures assume holding to expiration and capturing the full max profit — in practice, the early-exit rules covered next mean those exact numbers rarely get realized as-is.

## Managing the Position: The 50% Rule and Early Exits

Holding a credit spread or iron condor all the way to expiration is often discouraged in practice, because the character of the position changes as time passes.

- **Most of the profit comes early; the rest comes much more slowly.** Time decay (theta) accelerates as expiration nears, but gamma is climbing at the same time, so squeezing out the last bit of profit means taking on a rapidly growing risk that a small price move erases what you've already banked. That's why a widely cited convention in options education is to **close the position once it hits roughly 50% of max profit**, rather than holding for the rest. In the iron condor example above, that means buying to close around $115 in profit rather than waiting for the full $230 — and handing off the remaining risk in the process.
- **Gamma risk climbs sharply near expiration.** From roughly three weeks out, small price moves start swinging the position's P&L much more violently. Even if the 50% target hasn't been hit, a time-based rule — closing or rolling somewhere around 2–3 weeks before expiration — is commonly paired with the profit target for that reason.
- **Roll the threatened side if it's under pressure.** If price approaches one of your short strikes, a common response is to buy back just that side's spread and roll it out to a further strike and/or a later expiration to rebuild the buffer. Rolling has its own cost, though — commissions again, and it defers rather than eliminates risk — so rolling indefinitely just to avoid locking in a loss isn't a real fix.
- **Check for early assignment risk.** The short legs of American-style options can be assigned before expiration regardless of theoretical value. A short call near an ex-dividend date carries meaningfully elevated early-assignment risk, so it's worth checking the dividend calendar ahead of time.

## Credit Spread vs. Iron Condor: When to Use Each

| | Credit Spread (2 legs) | Iron Condor (4 legs) |
|---|---|---|
| Market view needed | Directional (bullish or bearish with limits) | Direction-agnostic — a "stays in range" view |
| Number of legs | 2 (one short, one long) | 4 (two short, two long) |
| Max profit | Credit from one spread | Combined credit from both spreads (usually larger) |
| Return on margin | Comparatively lower | Often comparatively higher for similar risk |
| Commissions/slippage | Lower — fewer legs | Higher — more legs mean more round-trip costs |
| Management load | Monitor one side | Monitor both sides at once |
| Best fit | A real directional conviction | Direction unclear, but IV looks rich |

Both structures share the same skeleton — a defined maximum loss — but they answer different questions. Reach for a credit spread when you actually have a directional view; reach for an iron condor when the direction is unclear but the options themselves look expensive relative to how far the stock is likely to actually move.

## Limitations and Pitfalls

- **Tail risk.** Option pricing models often assume price moves that roughly resemble a normal distribution, but real markets produce sharp gaps and crashes more often than that assumption would predict — the well-known "fat tail" problem. The higher the advertised win rate on a structure like this, the more it matters that a single rare large loss can wipe out the gains from many small wins that came before it.
- **More legs mean more execution cost.** An iron condor can involve up to four legs of trading at entry, exit, and every roll, and commissions plus bid-ask slippage accumulate with each one. As with the net-profit framing in Lesson 13 on [ATR and CMF risk filters](/en/strategies/risk-filters-atr-cmf/), judge the strategy by what's left after those costs, not the gross premium collected.
- **IV rank doesn't always mean-revert.** This is a strategy that sells when volatility looks elevated, but there are regimes — genuine crises, structural shifts — where volatility stays elevated or climbs further instead of reverting. Treating "IV rank is high, so sell" as a rule that applies in every market environment is risky.
- **Early assignment risk.** Short legs on American-style options can be assigned early regardless of theoretical value, and that risk rises meaningfully around dividend-related events.
- **A high win rate doesn't automatically mean positive expected value.** Marketing that touts an 80–90% win rate is only half the picture — it needs to be read alongside the fact that the payoff ratio is deliberately working against you. What matters is win rate multiplied by payoff, and that number moves a lot depending on market conditions and how disciplined the exit rules actually are, not a fixed figure you can bank on.

## FAQ

### Which is better for beginners, credit spreads or iron condors?
The two-leg credit spread is simpler to understand and manage. Either way, it's worth getting comfortable with the mechanics first — the risk that legs don't fill at the same time, early assignment, margin requirements — and starting with small position sizes before scaling up.

### Why close at 50% of max profit instead of just holding to expiration?
The time and gamma risk needed to capture the remaining half of the profit is generally seen as less attractive than simply locking in what's already been earned. It's a convention grounded in a risk/reward judgment, not a proven fixed rule, so it's reasonable to adjust it to your own risk tolerance.

### Are iron condors useful around earnings?
As covered in Lesson 38 on [IV crush](/en/strategies/iv-crush-earnings-options/), implied volatility tends to collapse sharply right after an earnings release, so some traders enter just before the report specifically to capture that post-earnings IV drop quickly. Overnight gap risk is substantially larger in that setup, though, so it usually calls for narrower widths and smaller position sizes than a standard non-earnings entry.

## Summary

- Credit spreads (two legs) and iron condors (four legs) both pair a short option with a long option to fix the maximum possible loss up front while collecting premium — unlike the wheel strategy, there's no need to actually take ownership of shares.
- Bull put spreads and bear call spreads are directional tools; combining both into an iron condor turns the position into a neutral bet that price stays within a range, regardless of direction.
- Strikes are commonly chosen using delta as a probability proxy, often in the 0.10–0.20 range for the short strikes, and width is safest when sized backward from a pre-decided maximum dollar loss rather than chosen arbitrarily.
- In the worked example, the iron condor's theoretical return on margin came out higher than the standalone put spread's — but that number assumes holding to expiration, and in practice traders commonly close around 50% of max profit instead.
- These structures are built to win often, but fat-tail risk, early assignment, and accumulating transaction costs mean a rare large loss can offset many small wins — understanding that tradeoff is what completes the picture, not the win rate alone.
</content>
