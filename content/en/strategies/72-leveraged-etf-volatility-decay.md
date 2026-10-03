---
slug: leveraged-etf-volatility-decay
title: "Leveraged ETF Volatility Decay: Why TQQQ and SOXL Underperform Long-Term"
description: "Why daily rebalancing in leveraged ETFs causes volatility decay, and why holding 3x funds like TQQQ or SOXL for months rarely delivers the expected multiple."
order: 72
updated: 2026-10-03
keywords: ["leveraged etf decay", "volatility decay etf", "why do leveraged etfs lose value", "TQQQ long term hold", "3x leveraged etf risk", "leveraged etf daily rebalancing", "SOXL long term", "beta slippage leveraged etf"]
seo_audited: 2026-10-03
---

## "The Index Was Up — So Why Is My 3x Fund Down?"

Anyone who has held TQQQ, SOXL, or one of the newer single-stock 2x/3x ETFs for more than a few weeks has probably run into this: the underlying index closed the period in the green, yet the leveraged fund sitting in the account is flat or even red. With single-stock leveraged ETFs now drawing aggressive retail buying — including a wave of Korean investors piling into 2x and 3x single-name products on US tickers — the question of why long-term holding quietly erodes value keeps resurfacing.

The answer sits in one structural fact: a leveraged ETF is not built to track a multiple of the index's *cumulative* return. It's built to track a multiple of the index's return on each individual *day*, re-set every single trading session. That daily reset is what produces **volatility decay** — also called negative compounding or beta slippage. This lesson walks through exactly why and how much that decay occurs, using worked numbers rather than hand-waving, and then lays out when leveraged ETFs can still be used with some discipline.

## The Mechanism: Why Daily Resetting Is the Real Culprit

To maintain a constant multiple (say, 3x) of the index's *daily* return, a leveraged ETF's manager adjusts its derivatives exposure (futures or swaps) at the close of every trading day. The problem is structural: when the index rises and the fund's dollar exposure grows along with it, the fund must buy more to restore the 3x ratio for the next day. When the index falls and exposure shrinks, it must sell more. In other words, the product itself is mechanically forced to buy high and sell low, every single day, regardless of what any individual investor wants to do.

In a choppy, range-bound market — one that moves up and down but ends up roughly where it started — this daily buy-high-sell-low cycle compounds into a steady erosion of value. In a smooth, low-volatility uptrend, the exact same mechanism works in reverse and actually produces a compounding *bonus*. That's the part that gets missed in the oversimplified "leveraged ETFs always lose value over time" framing. The real driver isn't direction — it's volatility.

### A Worked Example: Two Round Trips Through a Range

The clearest way to see this is to run the numbers. Suppose the underlying index drops 10% one day and rallies 10% the next, and repeats that cycle twice — a market that's essentially chopping sideways. Both the index and a 3x leveraged fund start at 100.

| Trading Day | Index Daily Return | Index Level | 3x Fund Daily Return (index × 3) | 3x Fund Level |
|---|---|---|---|---|
| Day 0 | — | 100.00 | — | 100.00 |
| Day 1 | -10% | 90.00 | -30% | 70.00 |
| Day 2 | +10% | 99.00 | +30% | 91.00 |
| Day 3 | -10% | 89.10 | -30% | 63.70 |
| Day 4 | +10% | 98.01 | +30% | 82.81 |

After four trading days, the index has only dropped from 100 to 98.01 — a loss of 1.99%. The 3x fund, which tracked exactly 3x the *daily* return every single day with no error, has fallen from 100 to 82.81 — a loss of **17.19%**. A naive "3 times the index's return" estimate would put the fund near 94.03 (three times -1.99%), not 82.81. That roughly 11-point gap between the naive estimate and what actually happened is volatility decay in action: the index is essentially back where it started, but the fund has lost real, permanent value through the mechanics of daily rebalancing alone.

<figure class="diagram">
  <img src="/static/img/charts/en/leveraged-etf-volatility-decay.svg" alt="Chart showing that over four trading days of two -10%/+10% round trips, the underlying index (blue line) ends nearly flat at 98.01, while the 3x leveraged ETF (red line) falls to 82.81 — well below the naive expectation of 94.03 (dashed orange line) obtained by simply multiplying the index return by three" loading="lazy">
  <figcaption>The index ends two round trips of -10%/+10% almost exactly where it started, at 98.01. The daily-reset 3x ETF, tracking the same moves, falls to 82.81 over the same period — well below the naive estimate of 94.03 you'd get by just multiplying the index's return by three. That gap is volatility decay.</figcaption>
</figure>

### The Mirror Image: Trending Markets Give Leverage a Compounding Bonus

The same mechanism runs in reverse when there's no chop, just a steady move in one direction. Suppose the index grinds up exactly 1% a day for 10 straight trading days.

- Index: 1.01 raised to the 10th power ≈ 1.1046, a cumulative gain of +10.46%
- Naive "3x" estimate: 10.46% × 3 = 31.38%
- Actual 3x fund (compounding +3% daily): 1.03 raised to the 10th power ≈ 1.3439, a cumulative gain of **+34.39%**

Here the actual 3x fund (+34.39%) *beats* the naive estimate (+31.38%). In a low-volatility trend, daily compounding works in the leveraged fund's favor. So volatility decay isn't a flaw unique to leveraged ETFs — it's the two-sided consequence of daily compounding, which turns into a bonus in calm trending markets and a drag in choppy or crashing ones.

## What Drives the Size of the Decay: Leverage and Volatility

A commonly cited approximation from the finance literature for the expected drag from daily resetting, under continuous compounding, is:

```
Expected daily drag (continuous approximation) ≈ 0.5 × k × (k - 1) × σ²
```

- **k**: the leverage multiple (2x, 3x, etc.)
- **σ**: the underlying index's daily volatility (standard deviation of returns)

This formula is a continuous-compounding approximation, not an exact match for extreme discrete moves like the ±10% example above — but its direction is unambiguous and worth internalizing:

1. **Decay scales roughly with the square of the leverage multiple**, because of the k(k-1) term. A 2x fund has a coefficient of 1, but a 3x fund jumps to a coefficient of 3 — three times higher, not just 1.5x higher. A 3x product isn't "50% riskier" than a 2x one in terms of decay; it's structurally far more exposed to it.
2. **Decay scales with the square of volatility**, because of the σ² term. Double the underlying's volatility and the decay roughly quadruples. That's exactly why 3x products tracking already-volatile assets — crypto, semiconductors, individual high-beta stocks — tend to decay far faster than a 3x fund on a broad index.

The practical rule of thumb traders often repeat is that suitability for anything beyond short-term holding deteriorates much faster than linearly as leverage or underlying volatility rises. It's worth stressing this is an approximation — the actual decay over any real holding period depends heavily on the specific price path (trending vs. choppy) that period actually took, which the formula alone can't tell you in advance.

## Leveraged ETFs vs. Options or Futures: Comparing Ways to Get Leverage

A leveraged ETF isn't the only way to put on a leveraged directional bet — buying calls or buying futures gets you leveraged exposure too, just through a completely different cost structure and risk profile.

| | Leveraged ETF (e.g. 3x) | Buying Calls | Buying Futures |
|---|---|---|---|
| Cost of leverage | Volatility decay from daily resetting — structural, compounds the longer you hold | Time decay (theta); falling implied volatility also hurts, as covered in the [IV crush lesson](/en/strategies/iv-crush-earnings-options/) | Roll costs at expiration; contango/backwardation effects (see the [VIX term structure lesson](/en/strategies/vix-term-structure-contango-backwardation/)) |
| Expiration | None — can be held indefinitely in theory | Yes — value decays to zero at expiration if OTM | Yes — contracts must be rolled periodically |
| Max loss | Full principal in theory, but no margin calls (fully paid, long-only structure) | Limited to the premium paid | Can exceed the posted margin given the embedded leverage |
| Access | Buyable in any standard brokerage account | Requires options trading approval | Requires a futures account and margin |
| Relationship to volatility | Benefits from calm trends, hurt by choppy/high-volatility regimes | Rising implied volatility generally helps the position's value | Reacts to direction; volatility itself isn't a direct source of gain or loss |

None of these is categorically "better" — the right tool depends on intended holding period. For a bet measured in hours or a few days, the leveraged ETF's decay hasn't had much time to compound, so it's a reasonably practical choice. For anything measured in weeks or months, calls or futures are generally considered the structurally more appropriate instruments.

## A Practical Checklist If You Still Want to Use Leveraged ETFs

- **Decide the holding period before you buy, not after.** Most leveraged ETF prospectuses explicitly describe the fund as targeting a daily objective. Using it as a short tactical trade — hours to a few days — is standard guidance; these products are not built to be bought and forgotten for months.
- **Check the volatility regime first.** As covered in the [VIX term structure lesson](/en/strategies/vix-term-structure-contango-backwardation/), whether the market is in a calm, trending regime or a choppy, high-VIX one completely changes how a leveraged ETF behaves over any given holding period. Shorter holds make more sense the higher and choppier realized volatility gets.
- **Don't size the position as if it weren't already leveraged.** When applying something like the [Kelly Criterion](/en/strategies/kelly-criterion-position-sizing/) or any account-percentage cap, the real exposure is the dollar amount invested multiplied by the fund's leverage factor, not the dollar amount alone. Putting 10% of an account into a 3x fund means the effective exposure is close to 30%.
- **Inverse leveraged ETFs share the exact same mechanics.** A -1x, -2x, or -3x fund resets daily in the same way, so even a correct directional call on a decline can still underperform if the path down includes enough chop along the way.
- **Single-stock leveraged ETFs carry sharper decay.** A 2x or 3x fund on an individual high-beta stock, rather than a diversified index, is tracking a much higher σ — and since decay scales with σ², that difference compounds fast relative to an index-based leveraged product.

## FAQ

### Do inverse ETFs suffer from the same volatility decay?

Yes. Whether it's a -1x fund or a -2x/-3x inverse leveraged fund, the underlying mechanism — resetting to a multiple of the index's *daily* return every session — is identical to a long leveraged fund. Being right about the overall direction isn't enough; if the decline includes enough up-and-down chop rather than a smooth drop, an inverse ETF can still underperform what the raw move would suggest.

### If the market is in a calm, steady uptrend, is it safe to hold a leveraged ETF for the long run?

As the second worked example above shows, a low-volatility trending market can actually make a leveraged ETF outperform the naive multiple. The catch is that there's no reliable way to know in advance that a calm trend will continue — past low volatility is no guarantee of future low volatility. Most practitioners treat continuous monitoring of the volatility regime, paired with short holding periods, as the safer default rather than designing a position around an assumed long-term hold.

### Is there a specific number of days after which holding a leveraged ETF becomes dangerous?

There's no universal fixed threshold. "Day trading to at most a few weeks" is the commonly repeated guideline, but it's a rule of thumb tied to volatility, not a fixed calendar rule. In an unusually calm, strongly trending stretch, holding longer may not cause much damage; in a volatility spike, meaningful decay can accumulate in as little as a day or two.

## Summary

- Leveraged ETFs reset daily to track a multiple of the underlying's *daily* return, not its cumulative return — and that daily rebalancing structurally forces the fund to buy high and sell low, producing volatility decay.
- In choppy, range-bound markets, this decay shows up as a loss even when the underlying ends up roughly flat; in calm, low-volatility trends, the same mechanism works in reverse as a compounding bonus. The key variable is volatility, not direction.
- Decay scales roughly with the square of the leverage multiple and the square of the underlying's volatility, which is why 3x funds and leveraged products on already-volatile assets (crypto, semiconductors, single high-beta stocks) decay far faster than a 2x index-tracking fund.
- Compared with calls or futures, leveraged ETFs trade a different cost structure (volatility decay vs. time decay vs. roll cost) and a different loss profile, so the right instrument depends heavily on intended holding period.
- If you do use leveraged ETFs, fix a short holding period in advance, check the volatility regime using tools like the [VIX term structure](/en/strategies/vix-term-structure-contango-backwardation/), and size positions by real exposure (dollars invested × leverage factor) the way the [Kelly Criterion](/en/strategies/kelly-criterion-position-sizing/) framework recommends.
