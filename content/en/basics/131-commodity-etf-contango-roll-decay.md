---
slug: commodity-etf-contango-roll-decay
title: "What Is Contango? Why Oil ETFs Don't Actually Track the Price of Oil"
description: "Why futures-based commodity ETFs like oil funds lose money on every roll in a contango market, and how backwardation flips that dynamic in the investor's favor."
order: 131
updated: 2026-10-09
keywords: ["what is contango", "oil etf losing money", "contango vs backwardation", "futures roll yield explained", "why oil etf tracking error", "WTI futures rollover cost", "commodity etf decay"]
seo_audited: 2026-10-09
---

## Oil Is Up, So Why Is My Oil ETF Flat?

Oil rallies, you buy an oil ETF on the strength of that headline, and months later spot crude is clearly higher — but your position is flat, or even down. "It's supposed to track oil, so why isn't it tracking oil?" is the natural question. The answer is that most oil ETFs don't actually hold barrels of oil — they hold **oil futures contracts**, and the process of constantly rolling those contracts forward runs into a market structure called contango that eats into returns. This lesson isn't about whether now is a good time to buy or sell an oil ETF — that's a trading-strategy question. It's about why a futures-based fund can structurally drift away from the spot price it's supposed to track, and about the contango/backwardation mechanics that cause that drift.

## What an Oil ETF Actually Holds — Futures, Not Barrels

Some commodity ETFs, like the well-known physically-backed gold funds, hold the actual metal in a vault and sell fractional ownership of it. Oil is a different animal. A market that trades millions of barrels a day would require enormous storage capacity, insurance, and transport costs to hold physically. So funds like the United States Oil Fund (USO) and most other major oil ETFs instead buy WTI crude oil futures contracts listed on the NYMEX to replicate the price movement of oil. Unlike the ordinary stock ETFs covered in [What Is an ETF?](/en/basics/etf-basics/), these funds are built on a different premise from the start: not "hold the underlying asset," but "replicate the underlying asset's price using futures contracts."

## Rolling the Contract — Why the Fund Must Keep Switching

The catch is that futures contracts expire. Oil futures typically expire monthly, and since the fund has no interest in actually taking delivery of crude, it has to sell the "near-month" contract (the one closest to expiration) and buy the "next-month" contract before expiration hits, to keep the same price exposure going. This swap is called a **roll**, or **rollover**. Doing this every month isn't the problem in itself. The problem shows up when the two contracts being swapped don't trade at the same price.

## Contango and Backwardation — Two Shapes of the Futures Curve

Why would two contracts on the same barrel of oil, just with different expiration dates, trade at different prices? A futures price embeds the cost of buying the commodity today and carrying it until the contract's expiration — the **cost of carry**: storage, insurance, and the interest the money could have earned elsewhere in the meantime. The farther out the expiration, the longer that cost has to be carried, so under normal conditions the later-dated contract trades above the near-month one. **A futures curve where longer-dated contracts cost more than near-dated ones is called contango.**

The reverse also happens. When oil is scarce right now — supply disruptions, production cuts, a war disrupting shipments — the value of holding the physical barrel immediately (called the **convenience yield**) can outweigh the cost of carry, pushing the near-month contract above the later-dated one. **A futures curve where near-dated contracts cost more than longer-dated ones is called backwardation.** Backwardation tends to show up whenever headlines point to an immediate supply crunch.

## Doing the Math — Losses Pile Up Even When the Spot Price Doesn't Move

Here's the roll mechanism in numbers. Say the near-month contract trades at $70 a barrel and the next-month contract trades at $71.40 — a gap of $1.40, or about 2%, which is contango.

1. The fund sells its expiring near-month contract at $70.
2. It uses that cash to buy the next-month contract at $71.40.
3. To maintain the same amount of oil exposure, it had to pay a higher price for the new contract — locking in roughly a 2% loss on that single roll.

The critical detail: this loss has nothing to do with whether the spot price of oil goes up or down. Even if spot crude sits at exactly the same level a month later, if the curve is still showing the same 2% contango between near- and next-month contracts, the fund loses another 2% on that roll. Assume a 2% monthly contango persists for twelve straight months: a simple sum gives roughly 24% a year, and once the losses are allowed to compound, the figure lands closer to the low-20% range (this is a simplified, illustrative estimate assuming a constant monthly contango — the real gap and curve shape shift from month to month, so actual results can run higher or lower). WTI futures actually traded in contango for more than 700 trading days between November 2014 and November 2017, and oil-futures-based ETFs over that stretch are widely cited as having lagged the cumulative move in spot crude by a noticeable margin. Backwardation runs in exactly the opposite direction: selling an expensive near-month contract to buy a cheaper next-month one locks in a gain — a positive roll yield — on every swap.

## Why Contango Happens — A Cost Calculation, Not a Price Forecast

A common misunderstanding is worth clearing up here. Contango and backwardation are not signals that the market "expects" prices to rise or fall. As covered in [Stock Index Futures and the Basis](/en/basics/stock-index-futures-basis-explained/), the gap between a futures price and the spot price — the basis — is, in principle, explained by a calculable cost-of-carry figure. But there's one crucial difference between stock index futures and commodity futures. An index futures basis is guaranteed to converge to zero as expiration approaches, because the contract settles against the spot price at expiry. An investor who holds a single index futures contract to expiration eventually sees that gap disappear entirely, whether it started in contango or backwardation.

An oil ETF never gets that benefit, because it never holds any single contract to expiration — it always has to roll before expiry. So it never gets to collect the "gap converges to zero" payoff that an index futures holder gets; instead, it buys and sells a brand-new contango (or backwardation) gap every single month. In other words, an index future's contango is a temporary gap that vanishes on its own if you hold to expiry, while a continuously-rolled fund's contango is a recurring cost that renews itself every month.

## A Different Problem From Leveraged ETF Decay

It's easy to confuse this roll loss with the [volatility decay in leveraged and inverse ETFs](/en/basics/leveraged-inverse-etf-decay/), but the two are separate phenomena with different causes. Volatility decay comes from the daily-reset compounding structure in leveraged products, and in theory it shouldn't occur at all in an unleveraged, 1x product when the index just goes up and down. Roll decay from contango, by contrast, has nothing to do with leverage ratio — it hits even a plain 1x fund, as long as the fund's structure forces it to keep rolling futures contracts forward. In practice, leveraged or inverse oil futures products stack both kinds of drag on top of each other, which is why long-term holders of those products tend to notice losses accumulating even faster.

## Physically-Backed Funds Don't Have This Problem — The Gold ETF Contrast

The clearest way to see this structure is to compare it against a physically-backed gold ETF. Gold is compact and relatively cheap to store, so funds that simply hold the metal in a vault are common and widely used. Because those funds never touch a futures contract, there's no roll to perform and no contango-driven roll loss to worry about — the fund's value tracks the gold price almost one-for-one, up or down. Oil, by contrast, is expensive enough to store and transport that a futures-based design is close to unavoidable, and that design comes with roll losses baked in whenever the curve sits in contango. The same label — "commodity ETF" — can hide two very different risk structures depending on whether the underlying asset is held physically or replicated through futures.

## How to Check This Yourself

Rather than relying on a vague sense that "oil ETFs have been underperforming lately," a few concrete checks make the picture much clearer. First, check the fund's prospectus to see whether it holds the physical commodity or futures contracts. Second, if it's futures-based, check the disclosed roll schedule — some funds swap the entire position on a single day shortly before expiration, while others spread the roll across several days or hold contracts further out the curve (three or six months, rather than the near month) specifically to dampen contango's bite. Third, look at the futures curve itself on the relevant exchange — whether it slopes upward (contango) or downward (backwardation) gives a rough sense of whether the next several rolls are likely to help or hurt. Fourth, compare the ETF's cumulative return against the cumulative return of the spot price (or a spot-tracking index) over the same period; the gap between the two is exactly the roll gain or loss that's accumulated.

## Key Takeaways

- Futures-based commodity ETFs for expensive-to-store assets like oil hold futures contracts, not the physical commodity, and must roll those contracts forward every month before they expire.
- When longer-dated contracts cost more than near-dated ones, that's contango; the reverse is backwardation — and both reflect cost-of-carry (or scarcity-driven convenience yield), not a price forecast.
- In contango, every roll means selling a cheaper near-month contract and buying a pricier next-month one, locking in a loss; backwardation reverses that, locking in a gain on every roll.
- A stock index future's contango disappears on its own at expiration; a continuously-rolled commodity ETF's contango never gets that benefit and renews itself as a recurring cost every month.
- Physically-backed funds like most gold ETFs skip this problem entirely, while leveraged or inverse futures-based commodity products stack roll decay on top of volatility decay.

## FAQ

### Does contango always mean an oil ETF loses money?
Not necessarily. If spot oil rises by more than the roll loss, the fund can still post a positive overall return — it just lags the spot price's gain. But if spot oil is flat or only modestly lower, the roll loss by itself can steadily erode the fund's value even without any dramatic price crash.

### Why don't gold ETFs or other commodity ETFs have this problem as often?
Compact, cheap-to-store assets like gold are usually held in ETFs as the physical metal, which means there's no futures contract to roll in the first place. Oil, natural gas, and other assets that are expensive to store or transport are far more likely to be structured around futures, which exposes them to contango- or backwardation-driven roll gains and losses.

### Is backwardation always a good time to buy?
Backwardation does give the roll itself a structural tailwind, but whether that tailwind is big enough to offset any adverse move in the spot price depends on the specific situation. The shape of the futures curve can also change quickly — backwardation at the moment of purchase is no guarantee it stays that way for the whole holding period.

### Is this the same thing as an ETF's expense ratio or tracking error?
No, and it's worth keeping the three separate. The expense ratio is a fixed annual fee the fund manager deducts. [ETF tracking error and premium/discount](/en/basics/etf-tracking-error-premium-discount/) refers to the gap between NAV, market price, and the benchmark index. Roll loss from contango is a separate, additional drag that comes specifically from the mechanics of swapping one futures contract for another.

> ⚠️ This article is for educational purposes only and is not a recommendation to buy or sell any specific product. The example figures are simplified for illustration; actual roll mechanics and returns vary by fund, product structure, and market conditions, so review the prospectus carefully before investing.
