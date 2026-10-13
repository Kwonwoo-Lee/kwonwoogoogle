---
slug: collar-strategy-protective-hedge
title: "The Collar Strategy: Using a Zero-Cost Hedge to Protect Stock Gains"
description: "How pairing a protective put with a covered call locks in a floor and ceiling on a stock position at near-zero cost, how to pick strikes, and how it differs from a covered call."
order: 82
updated: 2026-10-13
keywords: ["collar strategy options", "zero cost collar", "what is an options collar", "collar vs covered call", "protective put and covered call", "how to hedge a stock position", "protect stock gains options", "costless collar explained"]
seo_audited: 2026-10-13
---

## The Problem That Shows Up After a Big Run

Say a stock you've held for years has run up hard, and your account is sitting on a large unrealized gain. Sell now and you lock in the profit — but you trigger a tax bill and give up any further upside. Hold and do nothing, and you keep full exposure to the next leg up, but a sharp drawdown could erase a meaningful chunk of that paper gain in a matter of days. There's a third option that's neither "sell" nor "do nothing": the **collar strategy**, the subject of this lesson.

Lesson 27's [wheel strategy](/en/strategies/wheel-strategy-options/) and Lesson 58's [iron condor](/en/strategies/iron-condor-credit-spread/) were both income-seeking approaches built around selling options for premium. A collar is a different animal entirely. The goal isn't to collect premium — it's to **cap the downside on a position you already own, at close to zero net cost.** That's why a collar is usually filed under hedging rather than income generation. It's gotten renewed attention lately among investors sitting on concentrated, highly appreciated positions — think mega-cap tech or semiconductor names — as a way to cut tail risk without triggering a taxable sale.

## The Structure: A Put Bought, A Call Sold, Two Legs on a Leash

The name comes from the way the strategy puts a leash on price movement in both directions, like a collar on a dog. Assuming you already hold 100 shares, it opens two option legs at once — structurally similar to the iron condor, but with half the legs.

- **Buy a protective put.** Buy a put with a strike below the current price. If the stock falls below that strike, you can exercise the put and sell at that price regardless of how far it's fallen — a pre-set floor under your position.
- **Sell a call.** Sell a call with a strike above the current price, and use the premium collected to offset what you just paid for the put. If the stock rises above that strike, you're obligated to sell at that price — a pre-set ceiling on the upside too.

Pick strikes where the premium paid for the put and the premium received for the call land close to each other, and the net cost approaches zero — hence the term **zero-cost collar.** Worth flagging up front: "zero cost" refers only to the two option premiums offsetting each other. Commissions, bid-ask spread, and margin requirements are separate costs that don't disappear.

<figure class="diagram">
  <img src="/static/img/charts/en/collar-strategy-protective-hedge.svg" alt="Payoff diagram showing a collar strategy on held stock, where a long put caps losses at the put strike and a short call caps gains at the call strike, with the position tracking the stock only between the two strikes" loading="lazy">
  <figcaption>Below the put strike, losses stop growing. Above the call strike, gains stop growing. In between, the position moves one-for-one with the stock.</figcaption>
</figure>

## Why It Works: Trading One Insurance Premium for Another

A collar works because puts and calls are priced off the same underlying ingredient: implied volatility. Buying a put is buying insurance against a decline, and that insurance gets more expensive as implied volatility rises. Selling a call is selling insurance to someone else against the stock running higher, and that premium also rises with implied volatility.

So a collar is, in effect, a trade: you pay to remove downside risk you don't want, and you fund that payment by selling off upside you've decided you're fine living without. For the trade to make sense, you have to first decide your own priorities — how much upside you're willing to give up versus how much downside you absolutely need to avoid. The strategy isn't about betting on volatility itself; it's about swapping volatility exposure on each side to shrink the net cost to close to nothing.

## Choosing Strikes

Picking collar strikes means answering two questions at once: how far can the stock fall before it actually hurts (the put strike), and how much upside are you comfortable giving up (the call strike)?

A common rule of thumb, the same one from Lesson 27, is to use **delta** as a rough proxy for the odds an option finishes in the money. Traders often reach for puts around 0.15–0.30 delta (roughly 5–15% below the current price) and calls in the same 0.15–0.30 delta range (roughly 5–15% above). These aren't statistically validated fixed rules, just a commonly cited starting point.

| Goal | Put strike | Call strike | Result |
|---|---|---|---|
| Maximize room to run on the upside | Further out (lower) | Further out (higher) | Net cost rises — call premium doesn't fully cover the put |
| True zero cost | Solve for where the two premiums match | Solve for where the two premiums match | Near-zero cost, but upside room narrows |
| Maximize downside protection | Closer to current price (higher) | Closer to current price (lower) | Wider protection, but upside room shrinks sharply |

Pull the put strike closer to the current price and your floor gets higher (better protection), but that put also costs more — so funding it means pulling the call strike closer too, which squeezes your upside room hard. Push for more upside room instead, and the put has to move further out, weakening the floor itself. A collar doesn't give you both for free; it's a genuine trade-off between the two, not a free lunch on either side.

## A Worked Example

Say you hold 100 shares of a hypothetical stock, currently at $200, with a cost basis of $100 (a $10,000 unrealized gain). You build a collar using options 90 days out.

- **Buy the put**: strike $180 (roughly 0.25 delta), paying $4.50 in premium ($450 per contract).
- **Sell the call**: strike $230 (roughly 0.22 delta), collecting $4.30 in premium ($430).
- **Net cost**: 450 − 430 = **$20** for 100 shares — close to zero.

**Scenario A — the stock drops to $150.** Without the put, the loss would be (200−150)×100 = $5,000. With the $180 put exercised, the actual loss is capped at (200−180)×100 + $20 (net cost) = **$2,020**.

**Scenario B — the stock rallies to $260.** Without the call, the gain would be (260−200)×100 = $6,000. With the $230 call exercised, shares are sold at $230, capping the gain at (230−200)×100 − $20 (net cost) = **$2,980**.

**Scenario C — the stock stays between $200 and $230.** Neither option finishes in the money, both expire worthless, and your P&L simply tracks the stock's move minus the $20 net cost.

The pattern holds in general: a collar locks both the downside and the upside into a defined band for close to no cost, at the clear price of giving up any gains beyond the call strike.

## Collar vs. Covered Call: What Actually Changes

A collar shares its short-call leg with Lesson 27's covered call, but adding the long put changes the character of the position entirely.

| | Collar (long put + short call) | Covered call (short call only) |
|---|---|---|
| Purpose | Hedge an existing position against downside | Generate extra premium income on shares you hold |
| Downside | Capped at the put strike | Only cushioned by the premium collected — full exposure below that |
| Upside | Capped at the call strike | Capped at the call strike (same) |
| Net cost | Put cost offset by call premium — near zero | Call premium collected outright — net cash inflow up front |
| Best fit | Protecting an already-large gain you don't want to sell yet | Generating cash flow from shares in a flat-to-mildly-bullish market |

The key distinction: a covered call still carries the full downside risk, just cushioned slightly by the premium collected, while a collar gives up that premium (or uses it to fund the put) in exchange for actually removing the downside risk itself. In a mild decline, the covered call's premium absorbs some of the loss; in a sharp decline, only the collar provides a hard floor. Both give up the same thing on the upside — any move above the call strike belongs to whoever bought it from you.

## Limitations and Pitfalls

- **The opportunity cost in a strong rally is real.** If the stock blows well past the call strike while collared, every dollar of that move above the strike is gone. Keep rolling tight collars onto a stock you genuinely expect to keep compounding, and the cumulative drag versus simply holding it can be substantial.
- **Having the call exercised can force an unwanted sale.** If the whole point of the collar was deferring a taxable event, having the call exercised defeats that purpose — it forces a sale and triggers the tax consequence you were trying to avoid. Rolling the call out in time can delay this, but rolling adds its own transaction costs and tax complexity.
- **"Zero cost" rarely lands at exactly zero.** Finding strikes where the two premiums match to the penny is uncommon, and once bid-ask spread and commissions are factored in, there's usually some small net cost either way.
- **Tax and accounting treatment varies by jurisdiction and account type.** How the short call, the long put, and any resulting sale from exercise are each taxed differs significantly by country and account structure — confirm with a tax professional or your broker's documentation before putting one on.
- **A collar isn't a one-time setup.** Once the chosen expiration arrives, you have to rebuild it with new strikes, and the net cost of that new collar can come out meaningfully different depending on where implied volatility sits at the time.

## FAQ

### Can I run a collar without already owning the stock?
No. A collar is built on top of shares (or futures) you already hold. Buying the put and selling the call without the underlying position creates an entirely different payoff — closer to a synthetic short — so it only works as a hedge when the underlying shares are already in your account.

### How is this different from an iron condor?
Lesson 58's iron condor is a four-leg, direction-neutral income strategy built without owning the underlying, betting that price stays within a range. A collar is a two-leg hedge layered on top of shares you already hold, built to protect against a decline rather than to collect premium — different purpose, different starting assumption.

### What if the put I want is too expensive for the call premium to fully offset?
You can rebalance by selling a call closer to the current price (giving up more upside) or buying a put with a lower strike (loosening the floor slightly) until the two roughly match. Some traders instead swap the single put for a put spread — buying one put and selling a further out-of-the-money put to lower the net cost — though that leaves the position exposed again below the lower strike in a severe crash.

## Summary

- A collar pairs a protective put with a short call on shares you already own, putting a pre-set floor and ceiling on the position in both directions.
- When the put's cost and the call's premium roughly offset, the structure is called a zero-cost collar — though commissions and bid-ask spread mean it's rarely a true zero.
- Strike selection is a trade-off between how much downside you're protecting and how much upside you're giving up; you can't maximize both legs at the same time.
- The short call overlaps with a plain covered call, but the added put is what turns a collar into a genuine hedge rather than an income play — covered calls still carry full downside exposure beyond the premium collected.
- Account for the opportunity cost in a strong rally, the tax event an exercised call can trigger, and jurisdiction-specific tax treatment before putting a collar on.
