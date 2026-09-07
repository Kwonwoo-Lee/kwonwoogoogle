---
slug: option-greeks-delta-gamma-theta-vega
title: "What Are Option Greeks? Reading Delta, Gamma, Theta, and Vega"
description: "How delta, gamma, theta, and vega measure an option's sensitivity to the underlying price, time, and volatility, and how they interact in practice."
order: 66
updated: 2026-09-07
keywords: ["what are option greeks", "delta gamma theta vega explained", "option delta meaning", "option theta decay", "option vega volatility", "options greeks for beginners", "how do option greeks work", "IV crush explained"]
seo_audited: 2026-09-07
---

## Why an Option's Price Can Move Several Times a Day

If you've read [Options as Insurance](/en/basics/options-as-insurance/), you already think of a call or put's price as an insurance premium. This lesson breaks down exactly what makes that premium move. The same stock can rise 1% and one option barely reacts while another jumps sharply. An option can lose value on a day when the stock doesn't move at all, simply because time passed. And a stock can sit perfectly flat while its options still swing in price purely because the market's expectation of future volatility — the same concept behind the [VIX](/en/basics/vix-implied-volatility-explained/) — shifted. The variables that drive an option's price are the underlying price, time, and volatility, and the measures that describe how sensitive an option's price is to each of them are called the **Greeks**. Delta (Δ), gamma (Γ), theta (Θ), and vega (ν) are named after the Greek letters used to denote them. This lesson treats them as tools for understanding why an option's price moves the way it does — not as trading signals.

## Delta: How Much the Option Moves When the Underlying Does

Delta is the most intuitive of the four. It measures how much an option's price is expected to move for every one-unit move in the underlying asset's price. A call option's delta runs between 0 and 1; a put option's delta runs between -1 and 0. A call with a delta of 0.5 means that if the stock rises by $1, the option's price is expected to rise by roughly $0.50. A put with a delta of -0.3 means the same $1 stock rise is expected to knock roughly $0.30 off the put's price.

Delta moves in predictable directions. As a stock rises well above a call's strike price (deep in the money), that call's delta drifts toward 1 — at that point the option starts behaving almost like the stock itself. As the stock falls well below the strike (out of the money), delta drifts toward 0, and the option barely reacts to further moves in the stock. Traders often use delta as a rough stand-in for "the approximate probability this option expires in the money" — but that's a convenient shorthand, not an actual probability calculation. A delta of 0.30 doesn't guarantee a 30% chance of finishing profitable at expiration.

## Gamma: How Fast Delta Itself Changes

If delta describes sensitivity at this exact moment, gamma describes how quickly that sensitivity itself changes as the underlying moves. Gamma is, in effect, the rate of change of delta. High gamma means delta shifts sharply with even a small move in the stock; low gamma means delta stays fairly stable.

Gamma peaks for at-the-money options — where the strike sits close to the current stock price — and gets even sharper as expiration approaches. That's because a near-expiration, at-the-money option is genuinely on a knife's edge: a small stock move can flip the outcome from finishing in the money to finishing out of the money. Deep in-the-money or deep out-of-the-money options, by contrast, have outcomes that are already largely settled, so their gamma stays low. Holding a high-gamma position means that a fast move in the underlying can rapidly change how much directional exposure you actually have — gamma is best understood as a preview of how unstable delta itself could become.

## Theta: The Value That Erodes Just by the Clock Ticking

Theta measures how much an option's value shrinks purely from the passage of one day, holding everything else constant. For an option buyer, theta is usually shown as a negative number — a reminder that time value decays on its own. This ties directly back to the insurance analogy from [Options as Insurance](/en/basics/options-as-insurance/): just as an insurance policy is worth a little less once one fewer day remains for a claim to occur, an option is worth a little less once one fewer day remains for the underlying price to move favorably.

Theta decay isn't linear. Early on, with plenty of time left before expiration, a day or two of theta erosion is fairly mild. As expiration approaches — especially for at-the-money options — theta-driven decay accelerates noticeably. That asymmetry is why an option buyer effectively has time working against the position, while an option seller has time working in their favor.

## Vega: What Happens When Volatility Expectations Shift

Vega measures how much an option's price changes for every one-percentage-point move in implied volatility. As covered in [What Is the VIX?](/en/basics/vix-implied-volatility-explained/), an option's price embeds the market's expectation of how much the underlying will swing before expiration — its implied volatility. All else equal, when implied volatility rises, both calls and puts get more expensive; when it falls, both get cheaper. Direction doesn't matter here — the expectation of a bigger move, in either direction, is what raises the price of that "insurance."

Vega runs highest for options with more time left before expiration and for options near the money. This shows up most vividly around earnings announcements. Ahead of an earnings release, implied volatility often rises simply because the outcome is unknown, and once the results come out and that uncertainty resolves, implied volatility frequently collapses fast — regardless of which way the stock moves — pulling option prices down with it. This effect is commonly known as **IV crush**, and options with higher vega are more exposed to it.

## Rho: The Fifth, Rarely-Mentioned Greek

Less discussed than the other four, **rho** measures how much an option's price moves for every one-percentage-point change in interest rates. As covered in [How Interest Rates Affect Stock Valuations](/en/basics/interest-rates-and-stock-valuations/), rates influence stock valuations by changing the discount rate applied to future cash flows — and they affect option prices through a related mechanism. All else equal, rising rates tend to modestly raise call prices and modestly lower put prices. For short-dated stock options, this effect is usually too small to notice in practice, which is why rho rarely gets much attention. It becomes meaningfully larger for long-dated options (LEAPS expiring a year or more out) — much the way [bond duration](/en/basics/bond-duration-and-convexity/) makes longer-maturity bonds more sensitive to rate changes, a longer-dated option discounts a larger stream of future value, making rho more consequential the further out expiration sits.

## A Concrete Example: Four Greeks Working at Once

Suppose a stock trades at $50, and an at-the-money call (strike $50) has a delta of 0.5, a gamma of 0.05, a theta of -$0.80 per day, and a vega of +$0.60 per one-point move in implied volatility. Over one day, the stock rises $1 to $51, implied volatility rises 2 percentage points, and a full day passes. The option's price change can roughly be broken down like this:

```
Delta effect: 0.5 x $1 = +$0.50
Theta effect: -$0.80 (one day of time decay)
Vega effect: $0.60 x 2 = +$1.20
Approximate total: 0.50 - 0.80 + 1.20 = +$0.90
```

On top of that, because the stock rose, delta itself climbs by roughly the gamma amount (0.05), so the option becomes slightly more sensitive to the next dollar of stock movement. The takeaway here is that an option's daily price change is never explained by direction alone. Delta (direction), gamma (how fast that direction is accelerating), theta (the passage of time), and vega (shifting volatility expectations) are all pulling in different directions simultaneously to produce the final price. It's common to see a stock rise while its call option's price actually falls — usually because theta or vega losses outweighed the delta gain.

## Common Misreadings of the Greeks

The Greeks are approximations of sensitivity at a single instant — not fixed constants. Every one of delta, gamma, theta, and vega keeps changing as the stock price moves, time passes, and volatility shifts. Assuming yesterday's delta is still valid today is one of the most common mistakes. The Greeks are also derived from a specific pricing model — typically Black-Scholes — which rests on simplifying assumptions, such as volatility staying constant and prices moving smoothly rather than jumping. When real markets gap sharply or liquidity dries up, the Greeks a model calculates can diverge meaningfully from how the option's price actually behaves. The Greeks are best treated as an after-the-fact tool for understanding why an option's price moved the way it did, or as a way to gauge which of price, time, or volatility a position is currently most exposed to — not as a "buy when this number hits X" signal.

One more property worth knowing: Greeks add up. If you hold several option positions in the same underlying, you can sum each position's delta, gamma, theta, and vega to see, in a single set of numbers, what your entire account is currently most exposed to. Buying an equal number of calls and puts on the same stock, for instance, largely cancels out directional (delta) exposure — but theta and vega exposure from both legs stack together rather than offset, leaving the combined position more exposed to time decay and volatility swings even though its directional exposure sits near zero. Looking at aggregated, account-level Greeks rather than just one option at a time reveals risk structure that examining each position in isolation would miss.

## Takeaway

- The Greeks measure how sensitive an option's price is to three separate variables: the underlying price, time, and volatility.
- Delta measures sensitivity to the underlying's price; gamma measures how quickly delta itself changes.
- Theta measures how much an option's value erodes purely from time passing, and that decay accelerates as expiration nears.
- Vega measures sensitivity to implied volatility, and is directly behind the IV crush pattern often seen around earnings.
- Rho measures interest-rate sensitivity — negligible for short-dated options, but meaningful for long-dated ones (LEAPS).
- All the Greeks are constantly-shifting approximations, useful for understanding why an option's price moved — not signals for when to trade.

## FAQ

### If I buy an option with a delta of 0.5, am I guaranteed a profit when the stock rises?
No. Delta only measures sensitivity to the stock's price. If theta-driven time decay or a drop in implied volatility (vega) happens over the same period, the option's price can fall even while the stock rises.

### Is high gamma always a good thing?
It depends on which side of the trade you're on. For an option buyer, high gamma means gains accelerate faster when the stock moves favorably. For an option seller, that same gamma accelerates losses instead. Gamma itself isn't good or bad — its effect depends on the position's direction.

### Where can I see an option's Greeks?
Most options trading platforms and brokerage apps calculate and display delta, gamma, theta, and vega for each option contract in real time. There's no need to compute the Black-Scholes formula yourself — the platform's displayed values are sufficient for understanding a position's exposure.

### Why is rho rarely discussed?
For typical short-dated stock options, a one-percentage-point change in interest rates has a negligible effect on the option's price compared with the other Greeks. It becomes worth watching mainly for options with a year or more left until expiration, where interest-rate sensitivity is meaningfully larger.

> ⚠️ This article is for informational purposes only and is not investment advice. Investment decisions and their outcomes are the sole responsibility of the investor.
