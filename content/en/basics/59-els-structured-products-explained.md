---
slug: els-structured-products-explained
title: "What Is an ELS (Equity-Linked Security)? — Knock-in Barriers, Step-Down Redemption, and Why Losses Happen"
description: "ELS notes look like a fixed 6% return, but they're economically a sold put option. Here's how step-down early redemption and knock-in barriers actually determine your payout."
order: 59
updated: 2026-09-03
keywords: ["what is an ELS", "equity-linked securities explained", "ELS knock-in barrier", "ELS step-down redemption", "ELS vs DLS", "structured note principal loss", "Hong Kong HSCEI ELS", "worst-of structured product"]
seo_audited: 2026-09-03
---

## Be Skeptical the Moment You Hear "Fixed 6% Return"

When bank deposit rates sit at 3-4%, brokerages and bank counters often pitch a product promising a "fixed 6% return" — as long as an index like the KOSPI 200 or S&P 500 doesn't fall "too much." Most of the time, that product is an **ELS (Equity-Linked Security)**. Framed that way, it sounds like a slightly riskier cousin of a deposit that pays a bit more for the extra risk. But an ELS is a fundamentally different kind of instrument. Principal isn't protected, deposit insurance doesn't cover it, and once the underlying index falls past a certain level, losses track the index's decline almost one-for-one. This lesson covers what an ELS actually is under the hood, how its two defining mechanisms — early redemption and the knock-in barrier — work, and what actually happens when that structure breaks.

## What an ELS Really Is: You're Selling a Put Option

As covered in [what an option is](/en/basics/options-as-insurance/), a put option seller promises to buy the underlying at a set price if it falls below a certain level, and collects a premium up front for taking on that obligation. If the price stays above that level, the seller simply pockets the premium; if it falls hard, the seller has to buy at the agreed price and absorbs the loss. That's exactly the economic substance of an ELS. Buying an ELS effectively means selling a put option on the underlying asset(s) to the issuing brokerage, and receiving that option premium back in installments labeled a "fixed coupon." As long as the underlying doesn't fall past the agreed level, the investor just collects the coupon. If it does fall past that level, the investor absorbs the decline directly. The reason a "fixed 6% return" sounds so appealing is precisely because that coupon is compensation for downside risk the investor has taken on. There's no such thing as a return with no risk attached to it.

## Step-Down Early Redemption: A Bar That Gets Lower Every Six Months

The most common structure sold domestically is a three-year, "step-down" note with early-redemption checks every six months. At issuance, the underlying's starting price is set as 100%, and each subsequent evaluation date carries a redemption barrier the price must stay at or above — a barrier that gets progressively lower over time. Here's a hypothetical example.

```
Hypothetical 3-year ELS (underlyings: Index A, B, C; six-month evaluation intervals)

Check 1 (month 6)   redemption barrier 95%
Check 2 (month 12)  redemption barrier 90%
Check 3 (month 18)  redemption barrier 85%
Check 4 (month 24)  redemption barrier 80%
Check 5 (month 30)  redemption barrier 75%
Maturity (month 36) redemption barrier 70%  ← decides the payoff if it goes the distance
Knock-in barrier: 50%  ← did any underlying ever touch this line during the note's life?
```

If, on any evaluation date, all three underlyings sit at or above that date's barrier, the note redeems early: the investor gets back their principal plus the coupon accrued to that point (1 year elapsed at an assumed 6% annual coupon means a 6% payout). The barrier steps down over time because a longer stretch gives the index more room to recover toward its starting price, which raises the odds of early redemption. In practice, most ELS notes redeem at the first or second check rather than running to maturity — a natural outcome as long as markets don't crash. The trouble starts when the market does crash and the note keeps missing every early-redemption window.

## The Knock-in Barrier: Where Principal Loss Actually Begins

Suppose the note never redeems early and runs all the way to maturity. What decides the outcome now is a single binary question: did any of the three underlyings ever touch the knock-in barrier (50% in the example above) at any point before maturity? If knock-in never happened, most note structures pay the investor the promised coupon and full principal back at maturity even if the final price sits below the starting price. If knock-in did happen at any point, everything changes. No matter how much prices recover afterward, the payout at maturity is set by the decline of the single worst-performing underlying — full stop. If, say, the worst-performing underlying closes at 65% of its starting value at maturity after a knock-in event earlier in the note's life, the investor gets back 65% of principal with no coupon, locking in a 35% loss. Because knock-in is a "did it ever touch that line" condition, not a "where does it end up" condition, a sharp plunge followed by a sharp rebound a few days before maturity doesn't undo an already-triggered knock-in. That's the coldest feature of this structure.

## Why More Underlyings Means More Risk: The Worst-Of Structure

As covered in [correlation and diversification](/en/basics/correlation-and-diversification/), the core logic of diversification is that combining assets with low correlation to each other reduces a portfolio's overall volatility. An ELS with multiple underlyings flips that logic on its head. Whether the note redeems early or triggers knock-in is judged on a worst-of basis — the single worst-performing underlying decides the outcome for everyone. With one underlying, that asset alone has to hold the barrier. Add a second or third, and any one of them breaching the barrier is enough to trigger the whole note. Counterintuitively, mixing in underlyings with lower correlation to each other actually raises the odds that at least one of them falls hard. Issuers can offer a higher coupon precisely because adding more, less-correlated underlyings increases the risk the investor is absorbing — the value of the put option being sold gets bigger. The rule worth internalizing here is that a higher-coupon ELS isn't safer; it's compensating for more risk taken on, not less.

## How ELS Payoffs Differ From Simply Holding the Index

Buy and hold the index directly, and you capture 100% of the upside and 100% of the downside, symmetrically. An ELS breaks that symmetry. No matter how far the index rallies above the barrier, the investor's payout is capped at the predetermined coupon — there's effectively a ceiling on the upside. On the downside, once knock-in has occurred and never recovers by maturity, the investor's loss tracks the index almost exactly, just like holding it outright. That "capped coupon on the upside, near-full exposure on the downside" shape is the same payoff curve as the put-selling structure described earlier. It also resembles a covered call (selling a call option against shares you already own, trading away upside for premium income) in its broad "limited up, exposed down" shape — though a covered call is written against an underlying you actually hold, while an ELS is closer to selling a put with no underlying position at all. Because of this asymmetry, an ELS performs best in a range-bound, gently drifting market, and performs worst in a market that moves sharply in either direction.

## A Real-World Case: The Hong Kong H-Share Index ELS Losses

How this structure actually breaks is well illustrated by the Hong Kong H-Share Index (HSCEI)-linked ELS losses of 2021-2024. The HSCEI climbed to around 12,000 points in early 2021, then fell sharply, retreating to the 5,000-point range within about two years. Many step-down notes issued with the HSCEI as an underlying around that period missed one early-redemption window after another, and as the index sank well past knock-in barriers, large-scale principal losses were locked in at maturity for many investors. South Korea's Financial Supervisory Service investigated whether these notes were mis-sold and, in 2024, published dispute-resolution guidelines directing sellers to compensate a portion of losses depending on how clearly the product's risks had been explained and factors like the investor's experience and age. What makes this case instructive isn't that the product was fraudulent or the situation exceptional — it's that a scenario the step-down/knock-in structure could always produce in principle collided with an actual index crash and became real. The "50% knock-in" figure printed in a term sheet isn't an abstract probability; this episode confirmed it can be a genuinely short distance away in certain market conditions.

## What to Check in an ELS Term Sheet

Before buying an ELS, there are several structural questions worth understanding, at minimum. First, how many underlyings does the note have, and how different are they from each other? More underlyings with lower correlation typically mean a higher coupon, but also more risk through the worst-of mechanism described above. Second, does the note have a knock-in barrier at all (knock-in type) or not (no-knock-in type)? No-knock-in notes decide the payoff purely on the final price at maturity, without tracking any "did it ever touch" condition — simpler, generally with more favorable worst-case terms, but typically a lower coupon. Third, is the knock-in barrier evaluated only at maturity, or continuously throughout the note's life? A continuously monitored barrier means even a single day's dip below the line locks in knock-in, which structurally raises the odds of triggering it compared to a maturity-only evaluation. Fourth, since principal isn't guaranteed, an ELS is a debt obligation of the issuing brokerage — if the issuer becomes insolvent, investors can lose money regardless of how the underlying performed, a separate issuer credit risk layered on top of market risk. It also follows that ELS notes aren't covered by deposit insurance. Fifth, cashing out before maturity typically means a substantial early-redemption fee is deducted from the note's current valuation, so it's worth confirming upfront whether the money can stay locked up until maturity.

## Key Takeaways

- Economically, buying an ELS means selling the issuing brokerage a put option on the underlying(s) and receiving the premium back as a "fixed coupon."
- The common step-down structure lowers its early-redemption barrier every six months; if every check is missed and the note runs to maturity, whether a knock-in barrier was ever touched decides the payoff.
- Once knock-in occurs, the loss at maturity tracks the worst-performing underlying's decline almost exactly, regardless of any later recovery.
- Multi-underlying, worst-of structures work against diversification — mixing in less-correlated underlyings raises both the coupon and the odds of triggering knock-in.
- The 2021-2024 Hong Kong H-Share Index ELS losses show what this structure can produce in scale when it collides with a real market crash.
- ELS notes carry no deposit insurance, carry issuer credit risk, and lock up capital until maturity — understand the full structure in the term sheet before deciding.

## FAQ

### What's the difference between an ELS and a DLS?
Only the underlying asset differs; the early-redemption and knock-in mechanics work the same way. An ELS (Equity-Linked Security) uses stock indices or individual equities as its underlying, while a DLS (Derivative-Linked Security) uses non-equity underlyings — interest rates, commodities, currencies, or credit events like a bond default. Understanding the structure of one effectively means understanding the other.

### Are there principal-protected ELS products?
Yes — principal-protected versions (sometimes called ELB, equity-linked bonds) exist. They substantially reduce the risk of principal loss, but in exchange the expected return also drops closer to deposit-rate territory, and the same issuer credit risk still applies: if the issuer becomes insolvent, "principal protection" means little. Whenever a product advertises "principal protection," it's worth confirming exactly under what conditions that protection holds and whether deposit insurance applies.

### If knock-in occurs, can a later rebound still avoid a loss?
Under a continuously monitored knock-in structure, a barrier touch can't be undone once it happens. That said, most structures still allow early redemption after a knock-in event — if the underlying clears that period's redemption barrier at any later evaluation date, the note redeems early with principal and coupon regardless of the earlier knock-in. So there's still a path to avoiding a loss after knock-in occurs, but if every remaining redemption check is also missed through maturity, the knock-in history is what determines the final payout.

> ⚠️ This article is for informational purposes only and is not investment advice. The product structure and figures in this article are hypothetical illustrations used to explain the concept and do not represent the terms of any actual ELS product currently offered. ELS notes carry the risk of principal loss — always review the actual term sheet and prospectus before investing. Investment decisions and their outcomes are the sole responsibility of the investor.
