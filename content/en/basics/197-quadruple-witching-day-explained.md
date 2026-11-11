---
slug: quadruple-witching-day-explained
title: "What Is Quadruple Witching Day? Why Four Expirations Colliding Shake the Market"
description: "Why KOSPI200 futures, index options, and single-stock futures and options all expiring on the same day spike volume and volatility — and how the name evolved from double to quadruple witching."
order: 197
updated: 2026-11-11
keywords: ["what is quadruple witching day", "triple witching day explained", "futures options expiration day", "day of the four witches Korea", "why does quadruple witching move stocks", "program trading unwind expiration", "KOSPI200 options expiration date", "witching day volatility"]
seo_audited: 2026-11-11
---

## A Volume Spike With No News Behind It

On the second Thursday of March, June, September, or December, you may have noticed something odd near the closing auction: no earnings surprise, no economic data release, nothing newsworthy — yet trading value jumps well above normal and the index abruptly reverses direction in the final minutes before the close. [What Is a Stock Index Future?](/en/basics/stock-index-futures-basis-explained/) touched on this briefly as "quadruple witching day," and this is exactly that day. Four different derivatives contracts expire simultaneously, forcing large positions built up over weeks or months to unwind or roll over all at once. None of it has anything to do with any single company's earnings or outlook — it's a purely mechanical supply-and-demand shock that happens because today, specifically, is expiration day. Understanding that mechanism means you don't have to read unusual volatility on these days as a signal about something fundamental changing.

## The Four "Witches" — Which Contracts Expire Together

The name makes more sense once you see what's actually expiring. In Korea's derivatives market, the four contracts are:

- **KOSPI200 index futures** — a futures contract on the basket of stocks that make up the KOSPI200 index
- **KOSPI200 index options** — options to buy or sell at a set price, based on the same index
- **Single-stock options** — options on individual names like Samsung Electronics or SK Hynix
- **Single-stock futures** — futures contracts on those same individual names

Normally these four run on different clocks. The two option contracts expire monthly, on the second Thursday of every month. The two futures contracts expire only quarterly, on the second Thursday of March, June, September, and December. Four times a year, those quarterly Thursdays line up exactly with that month's option expiration — and on that one day, all four contract types settle at once. That's the day the market calls "quadruple witching," or in Korean, "the day of the four witches" (네 마녀의 날).

## Why the Name Keeps Changing — and Why Korea and the US Disagree

The term itself was imported from US markets, where it originally described index futures, index options, and single-stock options expiring together on the third Friday of March, June, September, and December — later extended to "quadruple" once single-stock futures joined the mix. But US single-stock futures trading effectively disappeared around 2020, so today's accurate US term is back to **"triple witching,"** even though "quadruple" still gets used out of habit in some coverage.

Korea's story ran the opposite direction — the count went up over time, not down. KOSPI200 futures listed in 1996 and KOSPI200 options followed in 1997, and the day their expirations overlapped was called "double witching." When single-stock options launched in 2002, a third contract joined and it became "triple witching." Then in May 2008, single-stock futures launched too, completing the set of four and giving Korea its current name: "quadruple witching," or the day of the four witches. In other words, "triple witching" was Korea's accurate term specifically between 2002 and 2008 — using it for today's Korean market is dated. Articles translated loosely from US coverage sometimes mix the terms up, so it's worth keeping straight which market and which era a given reference is actually describing. The calendar convention differs too: the US uses the third Friday, Korea the second Thursday.

## Why Volume and Volatility Spike on This Specific Day

The core reason is that a meaningful share of what expires that day doesn't just vanish quietly — it forces action. Unless a position is unwound ahead of time, expiration triggers either a cash settlement or an actual purchase or sale of shares, whether the holder wants it that day or not. Three distinct flows tend to converge:

First, **arbitrage program-trading unwinds**, covered in [Stock Index Futures Explained](/en/basics/stock-index-futures-basis-explained/). Positions built to exploit a pricing gap between futures and the underlying stock basket converge to a theoretical spread of zero at expiration, so the offsetting trades built up over the contract's life all have to be closed out — often concentrated right in the [closing call auction](/en/basics/call-auction-opening-closing-price/) window.

Second, **option exercise and market-maker hedge unwinds**. Options that finish in-the-money get exercised or cash-settled, and as covered in [What Is a Gamma Squeeze?](/en/basics/gamma-squeeze-delta-hedging-explained/), market makers have to unwind the stock positions they built up for delta hedging as that expiration approaches. When open interest is heavily concentrated near one strike price, the unwind flow around that strike can be large enough to pull the closing price toward it — a pattern often called "pin risk" or "max pain." This isn't a reliable, repeatable formula, though; how strongly it shows up varies with the actual distribution of open interest and the day's broader order flow.

Third, **rollover demand**. Investors who want to keep a hedge or an exposure running past expiration close out the expiring near-month contract and simultaneously open a new position in the next quarterly contract. That pair of trades landing at the same moment adds further volume on top of everything else.

## When It Collides With Index Rebalancing, It Gets Louder Still

Quadruple witching days tend to be especially noisy in years when they fall close to a scheduled [index rebalancing](/en/basics/index-rebalancing-effect/). KOSPI200 and MSCI indexes reset their constituent weights on a quarterly or semiannual cycle, and that reset date often lands near a witching day. Passive funds tracking those indexes then have to buy and sell large blocks to match the new weights, and when that flow lands on the same day as derivatives expiration unwinds and rollovers, trading value can spike even further. The two events are entirely independent in origin, but in years when their schedules happen to converge, "why is volume unusually high today" can't be fully answered by witching day alone — it's worth checking whether a rebalancing date is also in play.

## A Concrete Example

Suppose Asset Manager A runs a ₩1 trillion equity portfolio and has a short hedge on using KOSPI200 futures. As the quarterly expiration approaches, the manager faces a choice: if the hedge is no longer needed, the position simply expires and closes out. If the hedge needs to continue, the manager has to buy back the expiring near-month contract (closing the short) and simultaneously sell a new far-month contract (opening a fresh short) — a near-simultaneous pair of trades known as a roll. Manager A isn't the only one making this call; dozens of institutions running similar hedging programs tend to roll on the same day, for the same reason. What would otherwise be an ordinary day's trading volume in futures gets compressed into a few hours, spilling over into the related cash market. US estimates commonly cited for trading-volume increases on these expiration days run around 50% above normal, though that figure comes from specific studies over specific periods — it isn't a fixed constant, and there's no equivalent official Korean statistic to cite with the same confidence.

The same logic applies to individual retail investors holding single-stock options or futures. If you've written an option for premium income, whether it expires in- or out-of-the-money at settlement determines whether you have to deliver or buy shares, or whether the position simply disappears with no further action. With many traders unwinding similar positions around the same strike near expiration, it's common to see unusually large order flow concentrated at specific price levels on the order book in the run-up to the date.

## How to Actually Treat This Day as an Investor

The most important principle is that quadruple witching day, by itself, is not a buy or sell signal. Most of the volume it generates has nothing to do with any company's fundamentals — it's mechanical settlement and rollover flow that happens because today is the expiration date. [Circuit Breakers Explained](/en/basics/circuit-breaker-vi-sidecar-explained/) covers volatility interruptions (VI) that trigger on individual stocks; these also tend to cluster on witching days, and that clustering reflects a temporary supply-demand shock rather than new bad or good news about anything. So if you see an unusual swing into the close on one of these days, the more useful question isn't "what does this mean" but "does the next trading session carry this move forward, or does price simply revert to its prior trend." Even that isn't a guaranteed pattern — macro conditions and stock-specific flows still vary from one witching day to the next.

## Takeaways

- **Quadruple witching day** is when four derivatives — KOSPI200 index futures, KOSPI200 index options, single-stock futures, and single-stock options — all expire on the same day: the second Thursday of March, June, September, or December.
- The name evolved from "double witching" (1996-97, futures and index options) to "triple witching" (2002, single-stock options added) to today's "quadruple witching" (2008, single-stock futures added). The US, having lost single-stock futures trading around 2020, now accurately calls its own version "triple witching" and uses the third Friday as its date.
- Volume and volatility spike because arbitrage unwinds, option-exercise hedge unwinds, and rollover trades all converge on the same day — not because of any new information about the market.
- Open interest concentrated near one strike can create a "pin risk" or "max pain" pull toward that price into the close, but it isn't a dependable, repeatable pattern.
- Because this volatility is mostly mechanical and fundamentals-independent, treat it as a day to watch rather than a signal to trade on — and check whether the next session carries the move forward before drawing any conclusion.

## FAQ

### How many times a year does quadruple witching day happen, and when?
Four times — the second Thursday of March, June, September, and December, matching the final trading day for KOSPI200 index futures and options. Exact dates can shift slightly around holidays, so check the Korea Exchange's official quarterly expiration calendar for the precise date.

### I've seen articles call this "triple witching day" — is that wrong?
Not entirely. It was Korea's accurate term between 2002 and 2008, and it remains the accurate term for the US market today, since US single-stock futures trading has effectively disappeared. For Korea's market since 2008, though, "quadruple witching" (or "day of the four witches") is the more accurate name, since a fourth contract — single-stock futures — is also part of the mix.

### Does the market always fall on quadruple witching day?
No. The flow generated that day has no built-in direction. More buy-side arbitrage unwinding pushes sell flow into the market; more sell-side unwinding pushes buy flow in — and the actual outcome depends on the day's broader macro backdrop and stock-specific supply and demand. The one reliable takeaway isn't direction, but that volume and volatility can spike temporarily.

### Are there trading strategies built around quadruple witching day?
Some traders do try to exploit the predictable pattern of expiration-day flows, but that kind of specific entry-and-exit technique isn't the focus of this lesson. What matters here is understanding that the volatility on this day doesn't guarantee any particular strategy's success — it's simply a day when more mechanical, hard-to-predict order flow than usual converges at once. Specific trading techniques belong in a dedicated trading-strategy course, not this conceptual overview.

> ⚠️ This article is for informational purposes only and is not investment advice. Investment decisions and their outcomes are the sole responsibility of the investor.
