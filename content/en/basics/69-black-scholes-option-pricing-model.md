---
slug: black-scholes-option-pricing-model
title: "What Is the Black-Scholes Model? How Option Prices Get Calculated"
description: "The replicating-portfolio logic behind an option's price, what N(d1) and N(d2) actually mean, put-call parity, and where the model's assumptions break down in the real world."
order: 69
updated: 2026-09-08
keywords: ["what is the Black-Scholes model", "option pricing model explained", "Black-Scholes formula", "put-call parity explained", "how are option premiums calculated", "Black-Scholes model limitations", "implied volatility calculation", "N(d1) N(d2) meaning"]
seo_audited: 2026-09-08
---

## Who Actually Sets the Option Premium?

[Option Greeks](/en/basics/option-greeks-delta-gamma-theta-vega/) mentioned that delta, gamma, theta, and vega are all "calculated under a pricing model like Black-Scholes." [Options as Insurance](/en/basics/options-as-insurance/) compared a premium to insurance, but an insurer prices off decades of claims data — there's no equivalent loss table for an option. Yet the exchange puts a specific number on every strike and expiration, every moment. Fischer Black and Myron Scholes worked out how that number gets derived mathematically in 1973, with Robert Merton supplying much of the theoretical machinery; Scholes and Merton won the 1997 Nobel Prize in Economics for it (Black died in 1995 and was ineligible). This lesson covers the logic behind the **Black-Scholes(-Merton) model** — what each term in the formula actually represents — as a way to understand pricing, not as a trading signal.

## The Core Idea: If You Can Replicate It, the Price Is Pinned Down

Instead of forecasting what an option will be worth, the model asks: can a mix of the underlying stock and a risk-free bond recreate the option's exact payoff? Yes — matching a call's payoff means holding a specific fraction of the stock, exactly the delta from the [Greeks lesson](/en/basics/option-greeks-delta-gamma-theta-vega/), funded partly by borrowing at the risk-free rate. That fraction shifts as the stock moves, so the position needs continuous rebalancing ("dynamic hedging").

Here's the decisive step: if the call's market price ever diverges from what this replicating portfolio costs to build, buying the cheaper side and selling the pricier one locks in a risk-free profit. Assume such arbitrage can't persist (the **no-arbitrage principle**), and the option's price is forced to equal the replication cost — which is exactly what Black-Scholes computes. Because the logic runs through arbitrage rather than opinion, one theoretical price falls out regardless of how bullish or bearish any given investor feels. This is **risk-neutral valuation**: the same price emerges even assuming every participant is indifferent to risk. That name is easy to misread, though — investors' actual risk aversion isn't ignored, it's already baked into the volatility input, since a more risk-averse market tends to produce wider price swings, and wider swings push the option price up directly.

## Unpacking the Formula: What N(d1) and N(d2) Mean

For a European-style call (exercisable only at expiration) on a non-dividend stock:

```
Call Price = S × N(d1) − K × e^(−rT) × N(d2)
```

S is the stock price, K the strike, T the time to expiration in years, r the risk-free rate, and N() the cumulative standard normal distribution — it converts a value into a probability of landing at or below it. d1 and d2 combine price, strike, volatility, and time. **N(d2)** is the risk-neutral probability the option finishes in the money; **N(d1)** is exactly the delta hedge ratio from the Greeks lesson. Read together, the call's price is "the present value of the stock you'd receive if it finishes in the money, minus the present value of the strike you'd pay to get it" — the e^(−rT) term simply discounts that future strike payment to today.

## Put-Call Parity: The Put Price Comes for Free

A related identity, **put-call parity**, holds for any call and put sharing the same strike and expiration:

```
Call Price − Put Price = Stock Price − Present Value of Strike
```

It follows from the same no-arbitrage logic: "long a call, short a bond" produces the identical payoff at expiration as "long a put, long the stock," so mispricing either combination would open an arbitrage. In practice, this means pricing a call with Black-Scholes hands you the matching put price for free.

## A Worked Example

Take a stock at 50,000 won, a 3-month at-the-money call (strike 50,000 won), a 3% risk-free rate, and 25% annualized volatility:

| Item | Value |
|---|---|
| N(d1) (hedge ratio) | ≈ 0.55 |
| N(d2) (in-the-money probability) | ≈ 0.50 |
| Theoretical call price | ≈ 2,674 won |
| Theoretical put price (via parity) | ≈ 2,300 won |

Even at the money, N(d1) sits near 0.55 rather than 0.5, since log-normal returns tilt slightly more probability toward the upside. What matters most here is the 25% volatility input — change that one number and everything downstream shifts with it.

## In Practice, It Runs Backward: Solving for Implied Volatility

Of the five inputs, only volatility isn't directly observable — it's a forecast of future swings. So practitioners typically run the formula in reverse: given an option's actual traded price, hold the other four inputs fixed and solve for whatever volatility makes that price consistent. That backed-out number is the **implied volatility** covered in [What Is VIX?](/en/basics/vix-implied-volatility-explained/). Black-Scholes is therefore as much a way to read what volatility the market currently expects as it is a forward-pricing tool. Implied volatility is often compared against **historical volatility** — simply how much the stock has already moved. The two look in opposite directions, and ahead of earnings or other events, implied volatility often jumps well before the stock itself moves, pricing in uncertainty about what's coming.

## Where the Model Breaks Down

The model's assumptions create real gaps with the market. It assumes constant volatility through expiration, yet implied volatility backed out across different strikes on the same stock routinely differs — the well-known **volatility smile** or **skew**, most visible in index options where out-of-the-money puts often carry noticeably higher implied volatility, reflecting hedging demand against sudden drops. It also assumes continuous, log-normal price movement, while real stocks routinely gap on earnings or news. And the original formula covers only European-style, non-dividend stocks — it doesn't directly apply to American-style options (exercisable any time) or dividend payers, where practitioners lean on binomial trees or dividend-adjusted variants instead.

Despite this, Black-Scholes remains the industry standard — not for perfect accuracy, but because it organizes the factors driving an option's price into one comparable framework. Delta, gamma, theta, and vega are, in fact, this same formula differentiated with respect to each variable.

## Takeaway

- Black-Scholes prices an option as the cost of replicating its payoff with a stock-and-bond portfolio, under no-arbitrage logic.
- N(d1) is the replicating portfolio's hedge ratio (delta); N(d2) is the risk-neutral probability of finishing in the money.
- Put-call parity means the call price alone hands you the matching put price, with no separate calculation.
- In practice, the formula runs mostly backward, used to back out implied volatility from an option's market price.
- Constant-volatility and continuous-movement assumptions create real gaps (the volatility smile among them); American options and dividend payers typically need adjusted approaches like binomial trees.

## FAQ

### Do individual investors need to calculate the Black-Scholes formula themselves?
No. Nearly every brokerage platform computes each option's theoretical price, implied volatility, and Greeks in real time. What matters more is understanding that changing one input — volatility — reshapes the entire price.

### If the Black-Scholes price and the market price disagree, which one is "right"?
Neither is automatically wrong. The gap usually reflects how well assumptions like constant volatility and European exercise fit that specific option — in practice it's used less to call a mispricing and more to read implied volatility off the market price.

### Why doesn't Black-Scholes apply directly to American-style options?
The formula assumes exercise only at expiration. Early exercise, allowed on American-style options, can occasionally be optimal — a call right before a stock goes ex-dividend, for example — so practitioners use methods like binomial trees that evaluate the exercise decision at each point in time.

> ⚠️ This article is for informational purposes only and is not investment advice. You are solely responsible for your own investment decisions.
