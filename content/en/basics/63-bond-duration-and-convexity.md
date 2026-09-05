---
slug: bond-duration-and-convexity
title: "What Is Bond Duration? Why Small Rate Moves Can Swing Bond Prices So Much"
description: "How duration measures a bond's price sensitivity to interest rates, the difference between Macaulay and modified duration, and why convexity is the correction duration alone misses."
order: 63
updated: 2026-09-05
keywords: ["what is bond duration", "duration meaning bonds", "macaulay vs modified duration", "how do interest rates affect bond prices", "duration formula explained", "what is convexity in bonds", "long term vs short term bond rate sensitivity", "bond etf duration explained"]
seo_audited: 2026-09-05
---

## Why Does a "Safe Asset" Like a Bond Swing This Much?

Bonds are usually pitched as "a bit more than a savings account, but still safe." Yet anyone who has actually held a long-term Treasury ETF knows the underlying price can swing almost as violently as a stock when interest rates move just a little. [How interest rates affect stock valuations](/en/basics/interest-rates-and-stock-valuations/) covered how rates move stock prices through the discount rate. This lesson looks at why rate changes hit bond prices even more directly and mechanically — and at the single number that summarizes that sensitivity: **duration**. The goal isn't to tell you which bond or bond ETF to buy, but to make sense of a number that shows up in every bond news story and every fund fact sheet.

## Why Bond Prices and Interest Rates Move in Opposite Directions

Before duration makes sense, you need the basic mechanism behind the inverse relationship between bond prices and rates. A bond is a promise: a fixed coupon until maturity, plus the return of principal at maturity. Say you hold a bond with a 3% coupon on 1,000,000 won of face value. If market rates rise and newly issued bonds now pay 5%, nobody will pay full face value for your 3% bond when a 5% bond is available for the same price. So your existing bond can only be sold at a discount — a discount just large enough that, held to maturity, its effective yield converges toward that 5%. The opposite happens when rates fall: your 3% coupon suddenly looks attractive, and the bond trades above face value. That's the root of the inverse relationship, and duration is the ruler that measures how large that swing actually is for a given bond.

## Duration: A Sensitivity Measure Rooted in Weighted Average Timing

The original version of duration — **Macaulay duration** — is defined as the present-value-weighted average time until a bond's cash flows (coupons and principal) are received. That sounds abstract, but the intuition is simple. A bond that pays a small coupon each year and returns the bulk of its value as a lump sum at maturity has most of its cash flow concentrated at the far end, so its duration sits close to its maturity. A bond with a high coupon, by contrast, returns a meaningful chunk of value well before maturity — so even at the same maturity date, its duration is shorter.

The number that actually gets used in practice is **modified duration**, which adjusts Macaulay duration by the bond's yield. Modified duration answers a much more practical question: "if rates move by 1 percentage point, roughly how much does this bond's price move?" A modified duration of 5 means a 1-point rise in rates knocks the price down roughly 5%, and a 1-point drop pushes it up roughly 5%. As a formula:

```
% change in bond price ≈ -Modified Duration × change in rates (percentage points)
```

When a headline or fact sheet just says "duration" with no qualifier, it's almost always this modified-duration, price-sensitivity number being referenced.

## What Sets Duration — Maturity and Coupon

Two factors decide how long or short a bond's duration is.

**Longer maturity means longer duration.** A 30-year Treasury takes far longer to return its cash flows than a 2-year note, so at the same coupon rate its duration is substantially higher. The farther out a cash flow sits, the more uncertain the rate path between now and then, and the more that distant cash flow's present value reacts to changes in the discount rate.

**Lower coupons mean longer duration.** A low coupon means less cash comes back before maturity, so more of the bond's total value sits in that one lump-sum repayment at the end. The extreme case is a **zero-coupon bond**, which pays nothing until maturity — its duration exactly equals its time to maturity. Conversely, a higher coupon at the same maturity shortens duration, because a meaningful share of value has already been returned to the holder along the way, making the bond less sensitive to rate changes.

## A Numerical Example: Same Rate Move, Very Different Price Shocks

Suppose rates rise by 1 percentage point across three bonds with different modified durations:

| | Short-term (2-year, duration 1.9) | Medium-term (10-year, duration 8.5) | Long-term (30-year, duration 18) |
|---|---|---|---|
| Modified duration | 1.9 | 8.5 | 18 |
| Price change if rates +1pt | about -1.9% | about -8.5% | about -18% |
| Price change if rates -1pt | about +1.9% | about +8.5% | about +18% |

The same rate move produces a price shock nearly ten times larger on the long bond than on the short one. This is exactly why a long-term Treasury ETF can look nothing like the "safe asset" its name suggests: even with negligible default risk, a long duration alone can make a bond's interest rate risk rival that of stocks.

## What Duration Misses: The Correction Called Convexity

The modified-duration formula is a straight-line approximation — it assumes price moves exactly in proportion to duration for any rate change. In reality, the relationship between bond prices and rates isn't a perfectly straight line; it curves slightly. That curvature is captured by **convexity**.

Most plain-vanilla bonds have **positive convexity**: when rates fall, the price rises by slightly more than duration alone predicts, and when rates rise, the price falls by slightly less than duration predicts. Convexity works in the bondholder's favor — a bit of extra cushion. For small rate moves, this curvature barely matters and duration alone gives a good approximation. But for larger rate moves, the gap between a duration-only estimate and the actual price widens, which is why institutional investors add a convexity term to the formula for bigger swings:

```
% change in bond price ≈ -Modified Duration × rate change + ½ × Convexity × (rate change)²
```

Not every bond enjoys this favorable curvature, though. Callable bonds — where the issuer can redeem the bond early — and some mortgage-backed securities (MBS) can exhibit **negative convexity**: falling rates increase the odds of early prepayment, which caps how much the price can rise. In these cases, a rate decline doesn't automatically translate into the price gain duration alone would suggest, so checking the sign of convexity matters.

## Why This Number Matters — A Risk Language, Not a Trading Signal

Duration doesn't tell you to buy or sell a bond today. What it does is give you a common unit for comparing how exposed a bond — or a bond fund — is to interest rate changes. Most bond ETF fact sheets list an "average duration," and a higher number means the fund has more upside if rates fall, but also more downside if rates rise. As covered in [Yield Curve Inversion](/en/basics/yield-curve-inversion/), long-term rates often move first as the market reprices its expectations for the future path of rates — and a longer-duration bond reflects that repricing in its price faster and more sharply. It's also worth keeping duration separate from what [Credit Spreads](/en/basics/credit-spreads-explained/) measure: credit risk and interest rate risk are different axes. A high-quality government bond with low default risk can still swing hard on interest rate risk alone if its duration is long, while a short-duration bond can still swing on credit risk if the issuer's creditworthiness is weak. Duration by itself never tells the whole risk story for a bond.

## Not Just a Bond Concept — "Long-Duration Stocks"

The reason duration is worth understanding even outside fixed income is that the same logic shows up in equities. As [How Interest Rates Affect Stock Valuations](/en/basics/interest-rates-and-stock-valuations/) explained, a stock's value is also just future cash flows discounted back to the present. A company generating profit right now has most of its value tied to nearer-term cash flows, while a company still burning cash today in exchange for growth promised years out has most of its value sitting far in the future. Just as a bond's duration lengthens when its cash flows are concentrated near maturity, a growth stock whose value depends heavily on distant future earnings tends to react more sharply to changes in the discount rate (interest rates). That's why market commentary sometimes borrows the term and calls such stocks "long-duration assets." A stock has no fixed maturity or guaranteed cash flow, so you can't compute its duration the way you can for a bond — but the underlying principle, that value concentrated further in the future is more sensitive to rates, runs through both bonds and stocks alike. Duration turns out to be a useful mental model for interest rate sensitivity well beyond the bond market.

## Key Takeaways

- Bond prices and interest rates move in opposite directions: when new bonds are issued at higher yields, existing lower-coupon bonds can only be sold at a discount.
- Duration measures how large that inverse relationship is. In practice, modified duration tells you roughly what percentage a bond's price will move for a 1-point change in rates.
- Longer maturities and lower coupons both lengthen duration, increasing a bond's price sensitivity to rate changes.
- The duration formula is a linear approximation; convexity is the correction for the actual curve. Most bonds have favorable positive convexity, but callable bonds and some MBS can have negative convexity instead.
- Duration isn't a timing signal — it's a common yardstick for comparing how exposed a bond or bond fund is to interest rate risk.

## FAQ

### Does a longer duration always mean a worse bond?
No. Duration measures sensitivity to rate changes, not quality. In a rate-cutting environment, a longer-duration bond can see larger price gains; in a rate-hiking environment, the reverse is true.

### Should I look at Macaulay duration or modified duration?
When a bond fact sheet or news article just says "duration," it's almost always referring to modified duration — the number that directly estimates price sensitivity. Macaulay duration is more of a conceptual starting point for that calculation.

### Do bond ETFs have a duration too?
Yes. A bond ETF holds many bonds, so its fact sheet or the fund manager's website typically lists an "average duration" — a weighted average of the durations of its holdings — which shows how sensitive the whole fund is to rate changes.

> ⚠️ This article is for informational purposes only and is not investment advice. Investment decisions and their outcomes are the sole responsibility of the investor.
