---
slug: iron-butterfly-options-strategy
title: "Iron Butterfly Options Strategy: The Narrower, Higher-Payout Cousin of the Iron Condor"
description: "How the iron butterfly turns a short straddle into a defined-risk trade, how it differs from the iron condor, and how to pick strikes and wings."
order: 98
updated: 2026-10-29
keywords: ["iron butterfly options strategy", "iron butterfly vs iron condor", "iron butterfly explained", "short straddle with wings", "defined risk options strategy", "how to trade iron butterfly", "iron butterfly strike selection", "iron butterfly payoff"]
seo_audited: 2026-10-29
---

## Turning the Iron Condor's Flat Roof Into a Pointed One

Lesson 58 covered the [iron condor and credit spreads](/en/strategies/iron-condor-credit-spread/): four legs, four different strikes, built from a bull put spread and a bear call spread sold together so that staying anywhere between the two short strikes at expiration locks in the full credit. The **iron butterfly**, the subject of this lesson, uses the same four-leg skeleton but collapses the two inner short strikes onto exactly one price — almost always the strike closest to the current stock price (at-the-money). Keep those two short strikes apart and you have an iron condor; stack them on top of each other and you have an iron butterfly.

That one structural tweak completely changes the shape of the payoff. An iron condor's payoff is a flat-topped trapezoid — full profit anywhere between the two short strikes. An iron butterfly's payoff is a sharp triangle — maximum profit at exactly one point, declining in a straight line the moment price moves away from it in either direction. Search around and it's easy to find people asking what actually separates the two, and the answer always comes back to that shape.

## The Structure: An At-the-Money Short Straddle Plus Two Wings

It helps to split an iron butterfly into two pieces.

- **The body — an at-the-money short straddle.** Sell one put and one call at the strike closest to the current price. On its own, with no long legs underneath, this is a short straddle with unlimited loss potential on both sides.
- **The wings — protective long legs.** Buy one put below the body and one call above it. Those two long legs cap the otherwise-unlimited loss on each side at "wing width minus total credit collected."

Because the body collects premium on two options sold right at the money — where extrinsic value is richest — the net credit collected on an iron butterfly usually comes in well above a comparable iron condor's. When both wings sit the same distance from the body, it's called a **balanced (symmetric) iron butterfly**; when they don't, it's a **skewed (asymmetric) iron butterfly**.

<figure class="diagram">
  <img src="/static/img/charts/en/iron-butterfly-options-strategy.svg" alt="Side-by-side payoff diagram comparing the iron condor and iron butterfly at expiration, showing the iron condor's flat-topped trapezoid profit zone between two separate short strikes versus the iron butterfly's sharp triangular peak at a single center strike" loading="lazy">
  <figcaption>The iron condor (left) holds maximum profit flat across the whole range between its two short strikes. The iron butterfly (right) hits maximum profit at only one center strike, falling off in a straight line on either side.</figcaption>
</figure>

## Why It Can Work: Aiming Directly at the Richest Point on the Chain

An option's extrinsic value — the time premium, stripped of intrinsic value — peaks at the money and shrinks quickly as a strike moves further out of the money. That's a direct consequence of uncertainty: an at-the-money option is the one whose fate (finishing in or out of the money) is least certain at the moment it's priced, so the market pays the most time premium for exactly that uncertainty. Lesson 58's iron condor sells strikes that are already out of the money (commonly in the 0.10–0.20 delta range), collecting a smaller but comparatively safer premium. An iron butterfly does the opposite — it sells the single richest point on the entire option chain.

That larger premium comes with a cost on the other side of the ledger. An iron condor's short strikes start out of the money, so the trade is built with reasonable room for the stock to miss those strikes entirely. An iron butterfly's short strikes sit exactly at today's price, so the stock has to stay close to right where it is now for the position to approach its maximum profit. In short, an iron butterfly trades a higher payout for a lower probability of hitting it — the same win-rate-versus-payoff tension covered in Lesson 6 on [risk-reward ratio and money management](/en/strategies/risk-reward-money-management/). That tension is a direct consequence of the structure, not a backtested statistic.

## A Worked Example: One Cycle in Numbers

Say a hypothetical stock trades at $100 with 35 days to expiration — the same price level used in Lesson 58's iron condor example, so the two structures can sit side by side.

**Iron butterfly (balanced, $10-wide wings)**

| Leg | Strike | Direction | Premium |
|---|---|---|---|
| Short put (body) | $100 | Sell | Collect $3.20 |
| Short call (body) | $100 | Sell | Collect $3.00 |
| Long put (wing) | $90 | Buy | Pay $0.80 |
| Long call (wing) | $110 | Buy | Pay $0.70 |

- Net credit = (3.20 + 3.00) − (0.80 + 0.70) = **$4.70 ($470 per contract)**
- Wing width (same on both sides) = $10
- Maximum loss = (wing width $10 − credit $4.70) × 100 = **$530**
- Maximum profit zone: the full $470 only if the stock expires at exactly $100.
- Breakevens: $100 − 4.70 = **$95.30** on the downside, $100 + 4.70 = **$104.70** on the upside.

Lesson 58's iron condor on the same $100 stock (short strikes at $90/$110, wings at $85/$115, net credit $230, max loss $270, breakevens at $87.70–$112.30) makes the contrast concrete.

| | Iron Condor (Lesson 58) | Iron Butterfly (this example) |
|---|---|---|
| Maximum profit | $230 | $470 |
| Maximum loss | $270 | $530 |
| Where max profit occurs | $90–$110 (flat zone) | Exactly $100 (one point) |
| Breakeven range | $87.70–$112.30 ($24.60 wide) | $95.30–$104.70 ($9.40 wide) |
| Theoretical return on margin | 230÷270 ≈ 85.2% | 470÷530 ≈ 88.7% |
| Precision required | Stay anywhere in a wide range | Stay close to one center price |

The table makes the trade-off explicit: the iron butterfly collects a bigger credit and posts a higher theoretical return on margin, but its breakeven range is less than half as wide. An iron condor fits a view of "it'll probably stay somewhere in this broad range." An iron butterfly fits a much more specific, higher-conviction view: "this stock is barely going to move at all."

## Iron Butterfly vs. Iron Condor: Which One, and When

- **Right after an earnings report, when implied volatility is expected to collapse.** As covered in Lesson 38 on [IV crush](/en/strategies/iv-crush-earnings-options/), if the view is that the stock won't make a big post-earnings move and will instead settle near where the short straddle priced it, the iron butterfly captures that view more directly than a condor does.
- **When implied volatility is unusually rich, inflating the at-the-money premium itself.** Selling the body directly captures that inflated premium.
- **A less pointed view — "no strong directional call, but it probably won't leave this range" — favors the wider breakeven range of an iron condor instead.**
- **Skewed iron butterflies** keep the body at the money but set one wing closer and the other further out, leaning the structure slightly toward a direction without abandoning the neutral core. A mildly bullish lean, for example, might widen the call wing relative to the put wing to leave more room on the upside.

## Picking Strikes and Wing Width

- **The body (short strikes).** The common choice is the strike closest to the current price, or the point where the put and call trade at nearly the same premium. Because both legs must sit at the same strike, there's less flexibility here than the delta-based range an iron condor offers.
- **Wing width.** Wider wings mean a smaller net credit (the long legs cost more) and a smaller maximum loss; narrower wings move both in the opposite direction. The same principle from Lesson 42 on [Kelly criterion position sizing](/en/strategies/kelly-criterion-position-sizing/) — decide the maximum loss the account can absorb first, then size backward from there — applies directly here.
- **Compare the credit to the market's own expected move.** The premium collected on the body is itself a rough market estimate of the expected move by expiration. A smaller credit implies a narrower breakeven range, so it's worth checking whether that level of stability is actually a reasonable expectation before entering.

## Managing the Position and Its Pitfalls

- **Consider taking profit earlier and more often than with an iron condor.** Because the body starts at the money, gamma reacts to even small price moves much faster than it does in an iron condor. Closing at 25–50% of max profit — on the more conservative end of that range — is common practice.
- **Adjustments usually start with one wing.** If the stock starts drifting toward one side, a common response is pulling the opposite wing in toward the body, or rolling the threatened wing further out to widen the defense. Either move only delays the loss — it doesn't undo the fact that price has moved away from center.
- **Transaction costs accumulate across four legs.** Entering, adjusting, and closing can each touch all four legs, so the real credit after commissions and slippage — the same net-of-cost view from Lesson 13 on [ATR and CMF risk filters](/en/strategies/risk-filters-atr-cmf/) — is what matters, not the gross number.
- **"Stocks usually don't move much" is not a guarantee this time.** A narrow breakeven range is a reasonable baseline expectation in calm conditions, but unexpected news or a gap pushes an iron butterfly past its breakevens far more easily than an iron condor's wider range would allow.
- **Early assignment is still a factor.** If the short legs are American-style, either can be assigned before expiration — a short call near an ex-dividend date carries a meaningfully higher risk of that, so it's worth checking the dividend calendar.

## FAQ

### Is the iron butterfly riskier than the iron condor?
The dollar amount at risk depends on the wing width and credit collected, so it isn't automatically "riskier" in dollar terms. But because the short strikes start at the money, the breakeven range is narrower and a small move is more likely to push the position out of its maximum-profit zone — so the probability of winning is lower even when the dollar risk is comparable.

### When does a skewed iron butterfly make sense?
When the body stays at the money but there's a mild directional lean, widening the wing on the favored side gives the trade more room in that direction. The trade-off is added complexity: an asymmetric structure has more variables to track than a balanced one.

### Should a beginner start with the iron condor or the iron butterfly?
The common recommendation is to get comfortable with the iron condor from Lesson 58 first, then move to the iron butterfly once its narrower breakeven range and faster gamma shifts feel manageable. Starting the body at the money makes timing the management decisions more sensitive than it is with a condor.

## Summary

- An iron butterfly combines an at-the-money short straddle (the body) with two protective long legs (the wings) into a four-leg structure — the key difference from Lesson 58's iron condor is that the two inner short strikes collapse onto the same price.
- Its payoff is a sharp triangle with maximum profit at one center strike, rather than the iron condor's flat-topped trapezoid spanning a whole range.
- Selling at-the-money options — the richest point on the option chain for time premium — means a bigger credit and higher theoretical return on margin than a comparable iron condor, at the cost of a much narrower breakeven range: a higher payout for a lower probability of reaching it.
- Wing width should be sized backward from the maximum loss the account can tolerate, and the credit collected on the body itself works as a rough proxy for the market's priced-in expected move.
- Because the structure starts at the money, gamma risk builds faster than in an iron condor, so profit-taking thresholds should generally be set more conservatively and adjustments managed with closer attention to timing.
