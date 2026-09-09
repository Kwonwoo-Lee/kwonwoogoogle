---
slug: stock-index-futures-basis-explained
title: "What Are Stock Index Futures? Basis, Convergence, and Program Trading Explained"
description: "Why KOSPI 200 futures trade above or below the spot index, what basis and convergence-at-expiration mean, and how index arbitrage and hedging actually work — with a worked example."
order: 71
updated: 2026-09-09
keywords: ["what are stock index futures", "KOSPI 200 futures explained", "futures basis meaning", "program trading explained", "convergence at expiration futures", "index arbitrage explained", "hedging with futures", "open interest meaning"]
seo_audited: 2026-09-09
---

## "The Index Barely Moved, but Futures Jumped" — What's Going On

You've probably seen headlines like "KOSPI 200 futures rose faster than the spot index" or "program selling flipped the market negative into the close." In [Options as Insurance](/en/basics/options-as-insurance/), calls and puts were framed as contracts built around a *right* — something the buyer can choose to exercise or not. Futures are a close cousin, but they work differently: whoever buys a futures contract and whoever sells it both take on an **obligation** to settle at a fixed price on a set future date, no opt-out. This lesson focuses on the most heavily traded version — stock index futures, using KOSPI 200 futures as the running example — and covers why the futures price and the spot index diverge in the first place, why that gap is mathematically guaranteed to close by expiration, and how arbitrage trading and hedging actually put that mechanism to work in the market.

## What a Futures Contract Actually Is

A stock index futures contract is a promise to settle, in cash, the difference between an agreed-upon price today and the index's final settlement value at a set future date — no shares of the underlying stocks actually change hands. KOSPI 200 futures settle in March, June, September, and December, with the final trading day generally falling around the second Thursday of each contract month (exact contract specifications can change over time, so always check the exchange's current specs before trading). The side that buys first holds a "long" position; the side that sells first holds a "short" position. Unlike options, neither side collects an upfront premium in exchange for taking on limited risk — both the long and short side absorb losses in full if the price moves against them. Because of that mutual obligation, futures trading requires a margin system to guarantee performance: traders post only a fraction of the contract's full value as margin, which means gains and losses are magnified relative to the capital actually put up. If you've read [Margin Trading and Leverage](/en/basics/margin-trading-leverage/), think of futures as a market where that leverage effect is structurally built in at all times, not something you opt into.

## Why the Futures Price Differs From the Spot Index: The Cost-of-Carry Model

A natural question follows: if a futures contract is ultimately going to settle at the spot index's value anyway, why does it trade at a different price right now? The answer comes from a simple no-arbitrage logic — buying the spot index today and holding it until expiration has to be economically equivalent to buying the futures contract today and settling it at expiration. That equivalence is captured in the **cost-of-carry model**, and the theoretical futures price works out to roughly:

**Theoretical futures price ≈ Spot index × [1 + (interest rate − dividend yield) × days remaining/365]**

Unpacking that: if you buy and hold the spot index until expiration, you give up the interest you could have earned by parking that same cash in a deposit or bond instead — that foregone interest is a cost that pushes the futures price up. On the other hand, holding the actual stocks entitles you to dividends along the way, while holding a futures contract does not — that foregone dividend yield pushes the futures price down. Net it out, and when the interest rate exceeds the dividend yield, the theoretical futures price sits above spot; when the dividend yield exceeds the interest rate, it sits below spot. The first state — futures priced above spot — is called **contango** (a "normal" market); the second — futures priced below spot — is called **backwardation**. In the Korean market specifically, where dividends tend to cluster heavily around fiscal year-end, it isn't unusual to see temporary backwardation show up as the dividend yield effect intensifies near ex-dividend dates.

## Basis: The Gap Between Futures and Spot

That gap between the futures price and the spot index has a name — **basis** — and the formula is simple:

**Basis = Futures price − Spot price**

Under contango, basis is positive (futures trade rich); under backwardation, it's negative (futures trade cheap). The key thing to understand is that basis, in principle, should be explainable almost entirely by the interest-rate-versus-dividend-yield math above — it isn't a sentiment indicator about which direction the market expects to move. In practice, though, the actual traded futures price always drifts a bit from that theoretical value, because real-world frictions — order flow, liquidity, transaction costs, short-selling constraints — pull prices away from the pure formula. When that drift grows large enough, arbitrage trading (the "program trading" covered below) kicks in and pulls the price back toward fair value.

<figure class="diagram">
  <img src="/static/img/charts/en/futures-basis-convergence.svg" alt="Diagram of futures price starting above spot price and converging to it by expiration, illustrating basis" loading="lazy">
  <figcaption>Basis starts wide under contango and narrows steadily as expiration approaches, hitting zero on the settlement day</figcaption>
</figure>

## Convergence: Why Basis Is Guaranteed to Shrink Over Time

Look again at the cost-of-carry formula and notice that the basis scales directly with the days remaining until expiration. A year out, the basis can be sizable; a month out, it's smaller; and on expiration day itself, it hits exactly zero. That has to be true by definition — a futures contract's final settlement price is set to the spot index's value at that exact moment, so futures and spot are forced to converge. This narrowing of the gap as expiration nears is called **convergence**. If the basis is still unusually wide close to expiration, market participants know that gap has to close one way or another before settlement — and that certainty is exactly what triggers arbitrage trading in the first place, which in turn is the very force that pulls basis back toward its fair value.

## Program Trading: Arbitraging the Basis

"Program trading" gets used loosely to describe any batch of orders executed automatically by computer, but the piece that actually moves the market most directly is **index arbitrage** — trading the price gap between the futures contract and a basket of the underlying stocks. The mechanics are straightforward:

- **Buy-side arbitrage (매수차익거래)**: When futures trade richer than fair value, arbitrageurs buy the relatively cheap spot basket (the KOSPI 200 constituent stocks, weighted to match the index) and simultaneously sell the relatively expensive futures contract. As convergence pulls the two prices together by expiration, the spread locks in as a near risk-free profit.
- **Sell-side arbitrage (매도차익거래)**: When futures trade cheap relative to fair value, the arbitrageur sells (or shorts) the spot basket and buys the relatively cheap futures contract instead, capturing the same convergence in reverse.

Because this trade is close to risk-free in theory, institutional programs react almost instantly once the basis drifts wide enough to clear transaction costs, unloading large volumes at once. That means a wave of buy-side arbitrage shows up in the cash market as concentrated buying pressure, and sell-side arbitrage as concentrated selling pressure — flows that have nothing to do with any individual stock's fundamentals and everything to do with closing a pricing gap. This effect is most visible right around expiration, when accumulated arbitrage positions get unwound all at once as contracts settle — a phenomenon widely nicknamed "quadruple witching," known for producing outsized volume and volatility spikes right into the close.

## Hedging: Reducing Risk Without Selling a Single Share

If index arbitrage keeps the market efficiently priced, futures' other core function is letting investors and institutions **reduce market exposure without actually selling their stock holdings**. Take a concrete example: a fund manager runs a ₩10 billion portfolio closely tracking the KOSPI 200 constituents, and worries about a short-term market pullback — but doesn't want to sell the underlying stocks outright because of tax consequences, transaction costs, or timing concerns across dozens of individual names. Instead, the manager can sell (go short) a calculated number of KOSPI 200 futures contracts sized to roughly match the portfolio's exposure. If the index falls, losses on the stock portfolio are offset by gains on the short futures position; if the index rises, gains on the stocks are offset by losses on the futures. Either way, the manager has capped the portfolio's net swing within a narrower range — a direct application of the same principle covered in [Risk Management Basics](/en/basics/risk-management-basics/): giving up some upside in exchange for limiting downside, implemented here through a derivative rather than by trimming the actual holdings. Institutions use this kind of hedge not only ahead of an expected broad market pullback but also whenever they want to temporarily dial down a portfolio's beta exposure without disturbing its underlying stock positions.

## A Worked Example: Contango, Basis, and Convergence in Numbers

Some numbers make this concrete. Say the KOSPI 200 spot index sits at 350.00, 90 days remain until expiration, the short-term interest rate is 3.5% annually, and the dividend yield is 1.5% annually. The theoretical futures price works out to roughly:

350.00 × [1 + (0.035 − 0.015) × 90/365] ≈ 350.00 × 1.00493 ≈ **351.73**

That puts the basis at 351.73 − 350.00 = **+1.73 points** — a normal contango state, since the interest rate exceeds the dividend yield. Now fast-forward 60 days: only 30 days remain until expiration, and assume every other input stays the same. The theoretical futures price recalculates to:

350.00 × [1 + (0.035 − 0.015) × 30/365] ≈ 350.00 × 1.00164 ≈ **350.58**

Notice the basis shrank from +1.73 points to +0.58 points — roughly in proportion to the one-third reduction in days remaining — and it will land exactly at zero on the final settlement day. If the actual traded futures price with 30 days left were sitting at 352.00 instead of the theoretical 350.58, that 1.42-point gap is precisely the kind of mispricing that triggers buy-side arbitrage (buying the spot basket, selling the futures).

## What to Keep in Mind

Futures serve real functions as a hedging tool and a market-efficiency mechanism, but a few cautions matter for anyone trying to understand them as an investor. First, as noted above, the margin structure means gains and losses are magnified well beyond the capital actually posted — getting the direction wrong can produce losses that exceed the initial margin surprisingly quickly. Second, **open interest** — the number of futures contracts still outstanding and not yet closed out — is frequently cited as a gauge of how much positioning has built up in the market, but it says nothing on its own about direction. Rising open interest simply means more new contracts have been created, regardless of whether buyers or sellers are driving that growth; it only becomes meaningful when read alongside price action or other signals. Third, volatility around expiration tends to run higher than usual as accumulated arbitrage positions get unwound into the close — worth keeping in mind if you're watching index or individual-stock price action on those days.

## Takeaway

- Stock index futures are an obligation to settle at a fixed price at expiration, unlike options, which grant only a right — and the margin structure means leverage is always active.
- The theoretical futures price reflects spot plus the net cost of carry (interest rate minus dividend yield): higher rates push futures above spot (contango), higher dividend yields push futures below spot (backwardation).
- Basis — the gap between futures and spot — shrinks in proportion to time remaining and hits exactly zero at expiration, a process called convergence.
- Program trading (index arbitrage) exploits basis mispricing to pull prices back toward fair value, and tends to spike volatility right around expiration as positions unwind.
- Institutions widely use futures to hedge portfolio risk — offsetting stock exposure with a short futures position — without needing to sell any underlying shares.

## FAQ

### If futures trade above the spot index, does that mean the market expects prices to rise?
No. Contango (futures priced above spot) is mostly a mechanical result of interest rates exceeding the dividend yield, not a signal about market sentiment or expected direction. Reading basis as a directional forecast is a common misunderstanding.

### Does heavy program selling mean stock prices are about to fall?
Arbitrage-driven program trading flows are triggered mechanically to close a futures-spot pricing gap, independent of any individual stock's fundamentals. It can move short-term supply and demand, but it isn't, by itself, a signal about where the broader market is headed.

### Can individual investors use futures to hedge their own portfolios?
In theory, yes, but KOSPI 200 futures contracts are large, margin requirements are substantial, and the leverage risk is significant — all of which make this a high barrier-to-entry tool for most individual investors. Approaching futures without fully understanding the leverage risk covered in [Margin Trading and Leverage](/en/basics/margin-trading-leverage/) tends to add risk rather than hedge it away.

> ⚠️ This article is for informational purposes only and is not investment advice. You are solely responsible for your own investment decisions.
