---
slug: funding-rate-arbitrage
title: "Funding Rate Arbitrage Explained: Long Spot + Short Perpetual Futures for Direction-Free Yield"
description: "How funding rate arbitrage works: why perpetual futures pay funding, how to build the delta-neutral spot-plus-short-perp trade, and where the risk really hides."
order: 62
updated: 2026-09-23
keywords: ["funding rate arbitrage", "perpetual futures funding rate", "delta neutral strategy", "cash and carry crypto", "basis trade crypto", "what is funding rate", "spot futures arbitrage", "market neutral crypto strategy"]
seo_audited: 2026-09-23
---

## A Strategy That Doesn't Care Which Way Price Moves

Almost every strategy in this course so far has ultimately come down to guessing whether price goes up or down. [Lesson 18](/en/strategies/pairs-trading-stat-arb/) covered pairs trading, a market-neutral approach built on the spread between two correlated stocks. Crypto perpetual futures markets support an even more direct version of that same idea: **funding rate arbitrage**. Buy the spot asset, short an equal notional amount of the perpetual future, and the position's exposure to price direction cancels out almost entirely. What's left is a recurring cash flow — the funding payment — that the exchange transfers between longs and shorts on a fixed schedule. The mechanics are simple, but the word "arbitrage" here is doing more marketing than the risk profile deserves.

## Why Perpetual Futures Pay Funding At All

A standard futures contract has an expiration date, and at expiry its price is forced to converge with spot. A perpetual future, true to its name, never expires. Without that expiry to force convergence, a perpetual's price could in theory drift arbitrarily far from spot. Exchanges solve this with the **funding rate**: a periodic payment between the long and short sides of the market.

When the perpetual trades above the index price (a blended reference price built from spot on major exchanges), funding is positive, and longs pay shorts. That payment makes holding a long less attractive and holding a short more attractive, nudging the perpetual's price back down toward spot over time. When the perpetual trades below spot, funding turns negative and the payment flows the other way. [Lesson 28](/en/strategies/vix-term-structure-contango-backwardation/) covered contango and backwardation — the forces that pull a dated futures contract toward spot as expiry approaches. Funding does a similar job for a contract that has no expiry to do that work for it.

Most major exchanges settle funding every 8 hours (commonly 00:00, 08:00, and 16:00 UTC), though some settle hourly. The rate itself is typically built from a premium index (how far the perpetual has drifted from the index price) plus a small interest-rate component, and the exact formula and any caps vary by exchange.

## Building the Delta-Neutral Position

The basic structure of funding rate arbitrage — also called a basis trade or, in traditional finance terms, a cash-and-carry trade — works like this:

1. **When funding is positive**: buy the spot asset and short an equal notional amount of the perpetual. A price rally produces a gain on spot and an offsetting loss on the short, and a drop produces the reverse — the two legs cancel each other out. What remains is the funding payment the short side collects every settlement period.
2. **When funding is negative**: collecting funding requires the opposite structure — shorting spot and going long the perpetual. Short-selling spot is far less accessible for most retail traders than simply holding it, so in practice the long-spot/short-perp version dominates and traders mostly look for coins and periods where funding runs persistently positive.

The goal is matching notional value closely enough that a price move in either direction produces offsetting gains and losses across the two legs. This state is called **delta-neutral**: in theory, the only thing left on the table is the funding flow, not directional P&L.

<figure class="diagram">
  <img src="/static/img/charts/en/funding-rate-arbitrage.svg" alt="Diagram showing long spot and short perpetual futures price P&L moving in opposite directions so the combined position stays flat, while funding payments transfer from longs to shorts every 8 hours and accumulate in a step pattern" loading="lazy">
  <figcaption>Spot gains and perpetual-short losses (or vice versa) offset each other so the combined position stays flat, while the 8-hour funding settlement accumulates in a step pattern regardless of price direction.</figcaption>
</figure>

## A Worked Example

This is a hypothetical walk-through meant to illustrate the mechanics, not a guaranteed real-world return.

Assume Bitcoin trades at $80,000.

- **Spot leg**: buy 1 BTC for $80,000
- **Perpetual leg**: short $80,000 notional, using 5x leverage (20% initial margin) requires $16,000 in margin
- **Total capital deployed**: $80,000 + $16,000 = $96,000
- **Funding rate**: assume 0.02% per 8-hour period

Each settlement pays $80,000 × 0.0002 = $16. Three settlements a day gives $48 daily, and simply multiplying by 365 gives roughly $17,520 a year — about 18.25% annualized on the $96,000 deployed. That figure hasn't yet subtracted trading fees on both legs' entries and exits, any slippage, or transfer costs, all of which eat into the real return.

In practice, funding rates swing widely with market conditions. During strongly bullish stretches with heavy long positioning, 8-hour funding on major coins has been reported climbing to 0.05–0.1% or more, which annualizes well above 50%. In flat or bearish stretches, funding often compresses toward zero or flips negative, turning the trade into a cost rather than an income source. Various exchange and data-provider write-ups commonly cite a rough range spanning high-single-digit to several-tens-of-percent annualized — a reference range that depends heavily on the specific coin, exchange, and moment, not a guaranteed return.

## Funding Rate Arbitrage vs. Traditional Cash-and-Carry Basis Trades

Funding rate arbitrage shares its conceptual roots with the traditional cash-and-carry trade used in dated futures markets (CME Bitcoin futures, commodity futures, and index futures), but the two differ structurally in ways that matter for risk.

| | Perpetual Funding Rate Arbitrage | Traditional Dated-Futures Cash-and-Carry |
|---|---|---|
| Contract expiry | None (perpetual) | Fixed expiration date |
| Source of return | Recurring funding settlements, typically every 8 hours | Convergence of futures price to spot at expiry |
| When return is locked in | Never fully locked in — future funding isn't guaranteed to stay positive | Effectively locked in at entry if held to expiry |
| Holding the position | Can be closed at any time | Held to expiry, or actively rolled forward |
| Typical venue | Crypto exchanges (Binance, Bybit, OKX, etc.) | CME Bitcoin futures, commodity and index futures markets |
| Main risk | Funding reversal, liquidation risk, exchange counterparty risk | Price risk if unwound before expiry; comparatively lower counterparty risk on regulated venues |

The traditional trade locks in a known return at entry as long as the position is held to expiry. Funding rate arbitrage trades away that certainty for the flexibility of no expiry — funding can compress, flatten, or flip negative at any point, and nothing forces it to stay favorable. Calling this "arbitrage" is common industry shorthand, but it's really a position that needs ongoing monitoring, not a locked-in profit.

## Why Delta-Neutral Doesn't Mean Risk-Free

- **Funding reversal risk.** A sudden shift toward bearish sentiment can flip funding negative. From that point, the position starts costing money instead of earning it, and holding on too long can give back accumulated gains.
- **Liquidation risk.** Delta-neutral means net P&L offsets across the two legs — it does not mean margin balances stay flat. A sharp rally produces a mark-to-market loss on the short perpetual leg even though the spot leg is gaining, and if that loss breaches the maintenance margin requirement, the perpetual leg can be liquidated regardless of the unrealized gain sitting on spot. Using low leverage and keeping a wide margin buffer is essentially the only real defense.
- **Exchange counterparty risk.** Holding capital on an exchange exposes the trade to that exchange's solvency, security, and withdrawal availability — a market-neutral position doesn't neutralize exchange risk. The 2022 FTX collapse is the case most commonly cited as a reminder that this risk exists independently of the trade's directional structure.
- **Execution risk across venues.** Running the spot and perpetual legs on different exchanges makes it harder to keep notional values matched exactly, and transfer delays or slippage can leave the hedge imperfect for stretches of time.
- **Fee drag.** Because funding itself is often a modest annualized figure, trading fees and spread on both legs' entries and exits can consume a meaningful share of the return — especially on lower-liquidity altcoins.

## Practical Rules of Thumb

The figures below are commonly cited conventions in the space, not fixed rules — treat them as a starting point to adjust for current conditions.

- Check whether funding has stayed positive consistently over recent days to weeks rather than reacting to a single spike.
- Keep leverage low (2–3x or less) so a margin buffer survives a sharp price move without triggering liquidation on the perpetual leg.
- Favor large, liquid coins (Bitcoin, Ethereum) to minimize slippage on entry and exit.
- Review the position regularly and consider closing it once funding compresses or turns negative.

## FAQ

### Is funding rate arbitrage actually risk-free?
No. Directional price risk cancels out in theory, but funding-reversal risk, liquidation risk, and exchange counterparty risk all remain. "Direction-free" and "risk-free" are not the same thing, and treating them as equivalent is the most common mistake traders make with this strategy.

### How often is funding paid, and how is the rate set?
It varies by exchange, but every 8 hours (three times a day) is the most common schedule, with some venues settling hourly. The rate is typically built from a premium index — how far the perpetual has drifted from the index price — plus a small interest-rate component, with the exact formula and any rate caps varying by exchange.

### Does the hedge need to be exactly 1:1 between spot and the perpetual?
Matching notional value as closely as possible gets the position closer to true delta-neutral. Because even small price moves shift the relative value of the two legs slightly, traders typically rebalance position sizes periodically rather than setting the hedge once and leaving it untouched.

## Summary

- Funding rate arbitrage pairs a long spot position with an equal-notional short perpetual futures position, canceling directional P&L and leaving only the recurring funding payment.
- Funding exists because perpetual futures have no expiry to force convergence with spot; when the perpetual trades above spot, longs pay shorts on a recurring schedule (commonly every 8 hours) to pull the price back down.
- Unlike a traditional cash-and-carry trade, the return isn't locked in at entry — there's no expiry, but also no guarantee that funding stays positive going forward.
- Delta-neutral means net P&L offsets, not that margin balances stay flat, so low leverage and a wide margin buffer are essential to managing liquidation risk on the perpetual leg.
- Between funding reversal, exchange counterparty risk, and cross-venue execution risk, the accurate way to describe this trade is "direction risk removed, other risks retained" rather than genuinely risk-free.
