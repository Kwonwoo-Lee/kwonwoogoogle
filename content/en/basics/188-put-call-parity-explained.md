---
slug: put-call-parity-explained
title: "Put-Call Parity Explained: Why Call and Put Prices Are Locked Together"
description: "Why calls and puts on the same underlying, strike, and expiry can't be priced independently — the no-arbitrage logic, formula, and synthetic positions behind put-call parity."
order: 188
updated: 2026-11-07
keywords: ["put call parity explained", "put call parity formula", "why are call and put prices related", "synthetic long futures options", "options arbitrage explained", "put call parity example", "risk free arbitrage options", "put call parity violation"]
seo_audited: 2026-11-07
---

## Calls and Puts Don't Move Independently

[What options actually are](/en/basics/options-as-insurance/) explained calls and puts as insurance that pays off in opposite directions — a call pays when the price rises, a put pays when it falls. They look like opposite bets, but a call and a put on the same underlying, same strike price, and same expiry aren't priced independently of each other at all. Once one price is set, the other is almost fully determined. The relationship that locks them together is called **put-call parity**. [Option Greeks](/en/basics/option-greeks-delta-gamma-theta-vega/) and the [Black-Scholes model](/en/basics/black-scholes-option-pricing-model/) are tools for calculating what an option's price should be. Put-call parity is different: it's a relationship that must hold between a call and a put no matter what that price turns out to be. This lesson covers why that relationship exists, using nothing more than the logic that two ways of producing the same outcome must cost the same.

## Two Different Routes to the Same Payoff

Put-call parity starts from a simple thought experiment. Buying a stock today and holding it to a future date produces the same payoff, at that future date, as holding a futures contract that commits you to buy the same stock at a fixed price (the strike) on that date. You can build the exact same payoff out of options, too. Buy a call at a given strike and simultaneously sell a put at that same strike. If the stock ends up above the strike at expiry, the call you bought finishes in the money and pays off the difference; if it ends up below the strike, the put you sold finishes in the money and you owe that difference. Either way, the combined payoff of "long call + short put" is, strike for strike, identical to the payoff of a futures position locked in at that strike. Building a combination of options that replicates another instrument's payoff this way is called a **synthetic position** — here, a "synthetic long" in the underlying.

## The Formula

Written out, for European options on a non-dividend-paying underlying, the relationship is:

```
Call price - Put price = Current stock price - Present value of the strike
C - P = S - K × e^(-rT)
```

Here C is the call price, P is the put price, S is the current stock price, K is the strike, r is the risk-free rate, and T is time to expiry. The K × e^(-rT) term just converts "a promise to pay K at expiry" into today's money — the same discounting logic covered in [discounted cash flow basics](/en/basics/discounted-cash-flow-dcf/): a fixed future cash flow is worth less today than its face amount, discounted at the risk-free rate. Stripped down, the formula says one thing: the price gap between a call and a put has to equal the value gap between holding the stock outright today and holding a promise to receive the strike price later.

## What Happens When It Breaks: Risk-Free Arbitrage

This relationship holds not because of some elaborate model assumption, but because markets can't sustain **risk-free arbitrage**. Suppose C - P comes in noticeably higher than S - K×e^(-rT) — the call is priced rich relative to the put. In theory, selling the expensive side (the call), buying the cheap side (the put), and shorting the stock creates a combination whose payoff cancels out exactly no matter where the stock ends up at expiry, while locking in today's mispricing as pure profit. The moment such a gap appears, arbitrageurs pile into that trade, selling the rich side down and bidding the cheap side up until the gap closes. This logic is often traced to Hans Stoll's 1969 paper, which first formalized it, and in today's markets, algorithmic trading typically closes any visible gap faster than a human ever could. Put-call parity is therefore both a requirement for an efficient market and, at the same time, the mechanism that actively enforces it.

## A Worked Example

Say a call and put share a strike of $500, one year to expiry, and the risk-free rate is 3%, with the stock currently at $520. The present value of the strike is 500 × e^(-0.03×1) ≈ $485.22. Parity says the call price minus the put price should equal 520 - 485.22 ≈ $34.78. If the market is quoting the call at $40 and the put at $3, the actual gap is $37 — about $2.22 richer than the theoretical value. That tells you the call is priced rich relative to the put. In theory, selling the call, buying the put, and shorting the stock (a combination traders call a "reversal," the mirror image of a "conversion") locks in that $2.22 gap as profit regardless of where the stock lands at expiry, before costs. In practice, transaction costs, stock-borrow fees, and bid-ask spreads usually eat most of a gap this small before a retail trader could capture it — but the example makes the underlying mechanism clear: call and put prices are held to each other by this no-arbitrage relationship, not by coincidence.

## How This Shows Up in Practice: Pricing One Side Off the Other

The most common real-world use of put-call parity isn't grand arbitrage — it's the much more mundane job of price inference. Options market makers typically price whichever side (call or put) trades more actively using their full pricing model, then derive the other side directly from the parity formula rather than running an independent calculation for it. Pulling one price out of the other, the stock price, the rate, and the dividend estimate is simpler and faster than pricing both sides from scratch through Black-Scholes. The same logic extends to implied volatility: for European options on a non-dividend-paying underlying, a call and put sharing the same strike and expiry should, when run through Black-Scholes, produce essentially the same implied volatility. If the two look meaningfully different in the real market, that's more often a sign of a dividend-estimate mismatch, early-exercise value on an American-style contract, or thin liquidity on one side, than a genuine feature of the [volatility smile](/en/basics/volatility-smile-skew-explained/). Put-call parity, in that sense, functions as the internal plumbing that keeps prices inside the options market from contradicting each other.

## Where the Formula Breaks Down

This formula rests on a couple of assumptions, and dropping either one changes how it applies. The most important is that the options are **European-style** — exercisable only at expiry, so only the terminal payoff needs to match. **American-style** options, which can be exercised any time before expiry, carry extra value from that early-exercise flexibility, so the relationship becomes an inequality rather than a clean equality. The second assumption is **no dividends** on the underlying. If the stock pays a dividend before expiry, the formula needs to account for the fact that the stock price effectively drops by the dividend amount on the ex-date — typically handled by subtracting the present value of expected dividends from the S term. Plugging raw American-style, dividend-paying single-stock option prices into the bare formula and concluding "parity is broken" is a common mistake; most of the time, what's missing is the early-exercise adjustment or the dividend correction, not an actual arbitrage opportunity. This is also why index options on European-style, non-dividend-adjusted underlyings tend to fit the formula far more cleanly than American-style single-stock options on dividend payers — checking which type of contract you're looking at, and whether the underlying pays dividends, is the first step before applying the formula at all.

## Why This Actually Matters for an Individual Investor

Trading put-call parity directly for arbitrage profit is largely institutional and algorithmic territory, but understanding the relationship is still useful in two concrete ways. First, it's a quick sanity check on whether an option's quoted price makes sense — if the gap between a call and put is wildly off from the theoretical value, that's a flag to check for a pricing error or for thin liquidity distorting the quotes rather than a real opportunity. Second, understanding synthetic positions clarifies that options can be combined to replicate other instruments' payoffs — for example, that a short put plus a long stock position produces much the same payoff shape as buying a call outright. That's a structural insight about how positions can be built, not a claim that any particular combination is guaranteed to be profitable.

## Key Takeaways

- Put-call parity is the relationship C - P = S - K×e^(-rT) that must hold between a call and put sharing the same underlying, strike, and expiry.
- It holds not because of a complex pricing model, but because two routes to the same payoff (long call + short put, versus a long futures position) can't be priced differently without creating risk-free arbitrage.
- When the relationship breaks temporarily, arbitrageurs sell the rich side and buy the cheap side until the gap closes — today, mostly handled by algorithms within moments.
- The formula assumes European-style options and no dividends; American-style contracts and dividend-paying underlyings need adjustments for early-exercise value and dividends before the equality holds.
- For individual investors, it's less a trading edge and more an analytical tool — for sanity-checking option prices and understanding how synthetic positions can be built from calls and puts.

## FAQ

### If put-call parity breaks, can I profit from the arbitrage myself?
In theory, yes, but in practice it's difficult. Most visible gaps shrink to nothing once you account for transaction costs, stock-borrow fees, and bid-ask spreads, and larger gaps tend to get closed by algorithmic trading far faster than a retail trader could act.

### Is a synthetic long futures position exactly the same as an actual futures contract?
The payoff at expiry is essentially identical, but they're not fully interchangeable. Options carry different counterparty risk, margin requirements, and liquidity characteristics than futures, and for American-style options, the possibility of early exercise can make the value diverge slightly before expiry.

### Why does the formula become an inequality for American-style options?
Because American-style options carry an additional right to exercise at any point before expiry. That early-exercise right is optional and generally can't have negative value, so instead of an exact equality, the relationship holds as a range: the call price minus the put price must fall within certain bounds.

### How does the formula change for dividend-paying stocks?
If the underlying is expected to pay a dividend before expiry, you subtract the present value of that expected dividend from the current stock price (S) term before applying the formula. This reflects the fact that the stock is expected to drop by roughly the dividend amount, which lowers a call's relative value and raises a put's relative value.

> ⚠️ This lesson is for educational purposes only and is not investment advice regarding any specific product. Options trading carries significant risk of loss; investment decisions and their outcomes are the investor's own responsibility.
