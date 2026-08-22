---
slug: wheel-strategy-options
title: "The Wheel Strategy: Selling Cash-Secured Puts and Covered Calls for Options Income"
description: "How the wheel strategy cycles cash-secured puts into covered calls, how to pick strikes with delta, and the real risk behind the premium."
order: 27
updated: 2026-08-18
keywords: ["wheel strategy options", "cash secured puts", "covered call strategy", "options income strategy", "how does the wheel strategy work", "selling puts for income", "wheel strategy risk", "assigned shares covered call"]
seo_audited: 2026-08-22
---

## Selling Instead of Buying

Most of the options material in this course has been about reading someone else's footprint. Lesson 15 on [gamma exposure (GEX)](/en/strategies/gamma-exposure-gex/) covered dealer hedging pressure, Lesson 22 on [unusual options activity](/en/strategies/unusual-options-activity/) covered large directional bets, and Lesson 24 covered the extreme Greeks of same-day expiration. This lesson takes a different angle entirely. Instead of tracking what other participants are doing, it's about building a structure where **you sell options and collect premium on a repeating basis.** The most common version of that structure is **the wheel strategy.**

The wheel isn't a new invention — it's two long-established option-selling techniques, the cash-secured put and the covered call, chained together into one cycle. It's become a fixture of retail options education content over the past few years, usually pitched as a way to generate recurring premium income, and enough brokers walk beginners through it as an entry-level options strategy that the mechanics themselves are well understood and legitimate. The gap worth closing is between that "steady income" framing and what the strategy's risk actually looks like — which is the focus of this lesson.

## Two Legs, One Cycle: Cash to Stock and Back

The strategy is named for the way it rotates — cash becomes stock, stock becomes cash, and the cycle repeats. It has two legs.

**Leg one — the cash-secured put.** Pick a stock you'd genuinely be comfortable owning, and sell a put with a strike below the current price. You set aside cash equal to strike × 100 shares (one contract covers 100 shares) so you can cover the purchase if assigned. If the stock stays above the strike through expiration, the put expires worthless (out of the money), and the premium you collected is yours to keep — you sell a new put and repeat leg one. If the stock falls below the strike, you get assigned and buy 100 shares at that strike using the cash you set aside.

**Leg two — the covered call, once you own shares.** With 100 shares in hand, you sell a call with a strike above the current price. If the stock stays below that strike through expiration, the call expires worthless, the premium is yours, and you keep the shares — sell a new call and repeat leg two. If the stock rises above the strike, the call gets exercised, your shares are sold at that strike, you're back in cash, and the cycle restarts at leg one.

<figure class="diagram">
  <img src="/static/img/charts/en/wheel-strategy-options.svg" alt="Diagram showing the wheel strategy cycle: selling a cash-secured put, being assigned into 100 shares, selling covered calls against those shares, and returning to cash once the call is exercised" loading="lazy">
  <figcaption>Leg one (cash-secured put) moves into leg two (covered call) upon assignment; leg two moves back to leg one once the call is exercised. When an option expires worthless at either leg, that leg simply repeats and collects another premium.</figcaption>
</figure>

## The Premium Is Banked Either Way

The single most important thing to understand about the wheel is that **you collect the premium the moment you sell the option, regardless of what happens afterward.** Selling the put credits your account immediately, and that money is yours whether or not you end up getting assigned. Assignment isn't a loss — it's buying the stock you already wanted, at your chosen price, minus the premium you already banked. The same logic runs the other direction: having your shares called away isn't a loss either — it's selling at your target price, plus the premium you collected for selling the call.

That framing matters because the whole strategy rests on a premise: you have to actually be willing to own the stock at the put strike, and willing to part with it at the call strike. The wheel is, at its core, a premium-collection strategy that happens to let the options market set your entry and exit prices for a stock you already wanted to trade.

## Picking Strikes: Using Delta as a Rough Guide

How far you set your strikes from the current price is a trade-off between premium size and the odds of assignment (or of the call getting exercised). Strikes closer to the current price pay more premium but get hit more often; strikes further away pay less but get hit less often.

A widely used rule of thumb is to treat an option's **delta** as a rough proxy for the probability it finishes in the money. Delta technically measures how much an option's price moves per $1 move in the underlying, but for out-of-the-money options it's commonly used as an approximate stand-in for assignment probability. The ranges below are conventions traders cite informally, not statistically validated fixed rules, and should be read as a starting point rather than a formula.

| Delta range | Rough meaning | Character |
|---|---|---|
| 0.30–0.40 | ~30–40% odds of assignment/exercise | Bigger premium, frequent assignment — aggressive income posture |
| 0.16–0.30 | ~16–30% odds | The most commonly cited middle ground |
| 0.10–0.16 | ~10–16% odds | Smaller premium, infrequent assignment — conservative posture |

The 0.16–0.30 delta band (sometimes called "roughly one standard deviation out") is the range traders reach for most often in practice. Even so, the same delta implies a different real-world risk on a low-volatility blue chip versus a volatile small-cap, so the number alone shouldn't be applied mechanically without weighing what kind of stock you're selling options on.

## A Worked Example: One Full Cycle

Say a hypothetical stock trades at $50, and you've decided you'd be fine owning it long-term. You start running the wheel.

**Leg one — sell the put.** You sell a put with a $47 strike (roughly 0.25 delta), 30 days to expiration, and collect $1.20 in premium ($120 per contract). You set aside $47 × 100 shares = $4,700 in cash in case you're assigned.

- **Scenario A (not assigned):** The stock closes above $47 at expiration. The put expires worthless, and you keep the full $120. Against the $4,700 you had set aside, that's roughly **2.55%** over 30 days — an annualized figure would look much higher if this repeated every month, but there's no guarantee future premiums come in at the same level.
- **Scenario B (assigned):** The stock drops to $45 and you get assigned, buying 100 shares at $47 for $4,700. Netting out the $120 premium already collected, your effective cost basis is 47 − 1.20 = **$45.80** — still above the current $45 price, but better than simply placing a $47 limit order with no premium involved.

**Leg two — sell the covered call (continuing from Scenario B).** Holding 100 shares, you sell a call with a $48 strike (about 0.25 delta), 30 days out, and collect $1.00 in premium ($100).

- **Scenario A′ (not exercised):** The stock closes below $48. The call expires worthless, you keep the $100, and your effective cost basis drops further to 45.80 − 1.00 = **$44.80**. You sell a new call and continue leg two.
- **Scenario B′ (exercised):** The stock rises to $49 and the call gets exercised, selling your 100 shares at $48. Realized profit is (48 − 45.80) × 100 + $100 (call premium) = $220 + $100 = **$320**, and you're back in cash — $4,800 of it — ready to restart leg one.

As assignment and exercise repeat, your effective cost basis keeps drifting down by whatever premium you've collected, and each completed cycle locks in a small realized gain. These numbers are illustrative, though — real premiums depend heavily on the stock's implied volatility, the expiration chosen, and prevailing market conditions.

## The Wheel vs. Buy and Hold

If you're planning to hold the same stock long-term anyway, how does running the wheel actually compare to just buying and holding it outright?

| | The Wheel | Buy and Hold |
|---|---|---|
| Entry | Sells a put for premium while trying to buy lower | Buys immediately at the current price |
| Rising market | Upside capped at the call strike plus premium collected | Captures the full move |
| Sideways market | Collects premium repeatedly — relatively favorable | No price movement means no return |
| Falling market | Premium collected cushions losses somewhat, but large declines still hurt | Fully exposed to the decline |
| Ongoing management | Requires picking strikes and expirations every cycle, handling assignment/exercise | Essentially none after the initial purchase |
| Capital efficiency | Cash sits tied up as collateral for potential assignment (lower leverage) | Capital required equals the purchase amount only |

The core trade-off: the wheel tends to do relatively better in flat-to-mildly-bullish markets, but can lag plain buy-and-hold in a strong rally, since selling the call caps your upside the moment the strike is set. In a slow decline, the collected premium partially offsets losses, so the wheel can come out relatively ahead of holding shares outright with no options overlay.

## Why It Can Work: The Volatility Risk Premium

The case for the wheel having a positive expected value over time comes down to how options are priced. An option's price — specifically its implied volatility — reflects what the market currently expects future volatility to be. Across many markets and time periods, realized volatility has tended, on average, to come in lower than the implied volatility the options market had priced in ahead of time. This tendency is commonly referred to as the **volatility risk premium.**

Option sellers are structurally positioned to collect that premium. Selling puts and calls is, in effect, selling insurance against future price swings — and just as an insurer typically prices in a margin above expected claims, option sellers are, on average, positioned to collect somewhat more premium than the risk they're taking on turns out to cost. That's an average tendency, though, not a guarantee for any individual cycle. In periods where volatility spikes far beyond what was priced in — a sharp sell-off, an earnings shock — the premium collected can be nowhere near enough to offset the resulting loss.

## Limitations and Pitfalls

- **You can end up catching a falling knife.** If an assigned stock keeps declining, you can be left holding a much larger unrealized loss than the premium collected ever covered. The wheel only works if you're genuinely selective about which stocks you'd be comfortable owning at that strike — mechanically applying it to any high-premium name is risky.
- **Strong rallies create real opportunity cost.** Once you've sold a call, upside above that strike is gone. In a sustained bull run, plain buy-and-hold can meaningfully outperform the wheel.
- **Capital efficiency is low.** Holding strike × 100 shares in cash (or margin) as collateral ties up capital that could otherwise be deployed elsewhere.
- **Frequent trading means recurring costs.** Selling and managing a new option every cycle generates commissions and slippage repeatedly, and per the net-profit framing from Lesson 6 on [risk/reward and money management](/en/strategies/risk-reward-money-management/), those costs need to be netted against the premium collected, not ignored.
- **"Steady monthly income" oversells it.** Collecting premium every month doesn't mean locking in profit every month. A single sharp drawdown can erase several months of accumulated premium at once, and content that markets the wheel as passive fixed income often glosses over that asymmetry.
- **Check the tax and account implications first.** How option premium and assigned-share gains/losses are treated varies by jurisdiction and account type, so confirm the tax treatment before trading options on a foreign underlying through a local broker.

## FAQ

### Is the wheel strategy beginner-friendly?
Starting the wheel without a solid grasp of calls, puts, what assignment actually means, and the capital implications of the 100-share contract multiplier isn't advisable. You also need enough capital to actually buy 100 shares of the underlying if assigned, which meaningfully narrows the stock universe available in a smaller account.

### How is this different from just running covered calls on their own?
A standalone covered call is selling a call against stock you already own — that's leg two of the wheel. The wheel adds a systematic entry leg in front of it: instead of simply buying the stock outright, you sell a cash-secured put first and let assignment (if it happens) be your entry, collecting premium along the way. Run covered calls alone and your entry is a plain purchase; run the wheel and even the entry step is designed to collect premium.

### What if I don't want to get assigned?
A common approach is to "roll" the position before expiration — buying it back and selling a new option further out in time and/or further from the current price. Rolling repeatedly has its own costs, though, and mainly defers the outcome rather than avoiding it. It's usually more robust to pick strikes and underlyings you'd be fine getting assigned on in the first place, rather than treating assignment-avoidance as the goal.

## Summary

- The wheel strategy chains a cash-secured put (leg one) and a covered call (leg two) into a repeating cycle, and the key mechanic is that premium is collected up front at the moment of selling, regardless of whether assignment or exercise happens later.
- Strikes are commonly chosen using delta as a rough proxy for assignment probability, with the 0.16–0.30 delta range being the most widely cited middle ground between premium size and assignment frequency.
- Repeated cycles of assignment and exercise steadily lower your effective cost basis by the premium collected, though the exact numbers depend heavily on volatility and market conditions rather than following a fixed formula.
- The wheel tends to outperform plain buy-and-hold in flat-to-mildly-bullish markets, but lags in strong rallies (capped upside) and can still produce real losses in sharp declines that outrun the premium collected.
- The volatility risk premium is the usual explanation for why option selling has positive expected value on average, but it's an average tendency rather than a per-cycle guarantee, and "steady monthly income" framing tends to understate the downside risk.
