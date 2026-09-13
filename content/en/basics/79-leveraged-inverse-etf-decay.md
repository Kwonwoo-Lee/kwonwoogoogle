---
slug: leveraged-inverse-etf-decay
title: "Leveraged & Inverse ETF Decay Explained — Why You Can Lose Money Even When the Index Is Flat"
description: "Why leveraged and inverse ETFs can post a loss even after the underlying index round-trips back to its starting price, and the compounding math behind volatility decay."
order: 79
updated: 2026-09-13
keywords: ["leveraged ETF decay explained", "why leveraged ETFs lose money long term", "inverse ETF volatility decay", "daily reset leveraged ETF", "TQQQ long term risk", "leveraged ETF compounding effect", "volatility drag leveraged funds"]
seo_audited: "2026-09-13"
---

## The Index Is Flat. Why Is the Account Red?

An index closes exactly where it stood a month ago, yet an account holding a leveraged ETF on that same index shows a loss for the period. Given the label "2x," the intuitive assumption is that if the index round-trips back to where it started, the leveraged fund should too. It doesn't. Forums and finance blogs often summarize this as "leveraged ETFs always lose money if you hold them long enough," but that framing gets the cause wrong — what erodes the return isn't time, it's **volatility**. Unlike the plain-vanilla funds covered in [What Is an ETF](/en/basics/etf-basics/), leveraged and inverse ETFs are built around a fundamentally different target, and that's exactly what produces this result.

## What a Leveraged ETF Actually Tracks — a Multiple of the Daily Return, Not the Cumulative One

Open the prospectus of any leveraged ETF and you'll find a specific phrase: it seeks to deliver a multiple — say, 2x — of the underlying index's **daily** return. That single sentence explains everything that follows. A leveraged ETF never promises to double the index's return over a month or a year; it promises to double **today's** move, and then, after the market closes, rebalance its exposure back to the target multiple for tomorrow. It repeats that daily reset every single trading day.

The reset exists for a mechanical reason. If the index rises 10% today, the fund's net assets grow by roughly 20%. Left alone, that larger asset base would leave the fund's exposure ratio drifting away from its stated 200% target for the next day. So after the close, the fund manager buys or sells additional futures or swap contracts to bring exposure back to exactly 200%. The daily reset itself isn't the problem — the problem is that returns keep compounding on top of that freshly reset base, day after day, and that compounding path increasingly diverges from what the index itself actually did.

## Why a Loss Survives Even When the Index Returns to Its Starting Point

Start with the simplest case. Say the underlying index opens at 1,000, falls 2.5% on day one (to 975), then rises 2.56% on day two, landing back exactly at 1,000. Over the two days, the index's own return is precisely 0%.

Now track a 2x leveraged ETF over the same two days:

- Day 1: index -2.5% → leveraged ETF -5.0% (100 → 95)
- Day 2: index +2.56% → leveraged ETF +5.13% (95 → 95 × 1.0513 ≈ 99.87)

The index is back exactly where it started, but the leveraged fund sits at 99.87 — a **-0.13%** loss. The wider the swing, the larger this gap grows. Take a bigger round trip: the index rises 20% (100 → 120) and then falls 16.67% back to 100. A 2x leveraged fund moves 100 → 140 (+40%) → 93.3 (-33.3%), ending down **-6.7%**. A -1x inverse fund over the identical path moves 100 → 80 (-20%) → 93.3 (+16.7%), also landing at **-6.7%**. A -2x inverse fund moves 100 → 60 (-40%) → 80 (+33.3%), a **-20%** loss. Regardless of direction, the pattern is the same: the wider the swing and the higher the multiple, the faster this loss compounds.

## The Real Variable Is Volatility, Not Time

This effect has a name: volatility decay (also called volatility drag). The mechanism is simpler than it sounds. In any sequence where a gain is followed by a loss, or a loss by a gain, the daily reset means **the loss after an up day gets applied to a larger base, while the recovery after a down day gets applied to a smaller one.** Losses get multiplied against a bigger number; recoveries get multiplied against a smaller one. The same percentage swing in each direction ends up costing more in absolute terms than it gives back. This is exactly the concept covered in [Beta and Volatility](/en/basics/beta-and-volatility/), except here volatility isn't just a risk gauge — it's a direct mechanical drag on the return itself.

The flip side matters just as much. In a market that trends steadily in one direction without much back-and-forth, the same compounding works in the fund's favor: gains keep compounding on a growing base, and cumulative returns can actually come in above a simple "index return × multiple" calculation. Volatility decay isn't a flaw baked into leveraged ETFs — it's the two-sided consequence of daily compounding, favorable when a trend is smooth and low-volatility, unfavorable when the market just oscillates without going anywhere.

## Why Decay Grows Explosively With Volatility

In the earlier examples, widening the swing from 2.5% to 20% took the decay from -0.13% to -6.7%, and moving to a -2x product pushed it to -20%. None of that is a coincidence — it follows directly from the math. If r is the size of the daily move, the loss on a two-day round trip for an n-times fund scales approximately with `n(n-1) × r²` (this approximation holds best for small moves; at the larger swings used above, the actual figures diverge somewhat from it). Two things follow from that formula. First, the loss scales with the **square** of the daily move — double the swing and the decay quadruples; a tenfold larger swing multiplies decay by a hundred. That's why decay is barely noticeable in a calm, gently drifting market but can snowball fast once sharp drops and rebounds start alternating. Second, the coefficient n(n-1) grows faster than n itself, so a 3x fund (coefficient 3×2=6) carries three times the decay of a 2x fund (coefficient 2×1=2) under the same volatility — not 1.5 times, three times. Together, these two properties explain why decay complaints cluster specifically around volatile markets and specifically around the highest-multiple products.

The same logic holds over longer stretches. Because decay compounds multiplicatively rather than adding up linearly, extending the choppy period from days to months or years compounds the effect further. A commonly cited case is 3x Nasdaq-100 funds during the sharp swings of the early COVID-19 period in 2020: even after the index itself recovered a substantial portion of its drawdown within months, the 3x fund's cumulative recovery lagged well behind that pace. Conversely, during a stretch like the sustained uptrend later in 2020 with few sharp reversals, the same 3x funds outpaced a simple 3x multiple of the index's return. Long-run performance of a leveraged ETF, in other words, depends far less on where the index ended up than on how smooth the road was getting there.

## Leveraged and Inverse ETFs Carry Extra Costs Beyond Decay

Separate from volatility decay, most leveraged and inverse funds — including what Korean investors commonly call "gopbeoseu" (leveraged/inverse products) — build their multiple using derivatives such as index futures rather than holding the underlying stocks directly. Futures contracts expire, so as expiration approaches the fund must roll its position into the next contract, a process that generates transaction costs and can add further cost from the price gap (basis) between futures and the spot index. Layer that on top of the higher expense ratios these funds typically carry compared with plain index ETFs, and meaningful additional wear can accumulate over a long holding period even in periods when volatility decay itself is modest.

## Checking How Much Decay Has Built Up in a Fund You Hold

Rather than guessing, it's worth checking directly. The simplest approach is to pull the fund's net asset value (NAV) history from the issuer's website or an exchange data platform and place it side by side with the underlying index's cumulative return over the same period. However far the ratio between the two has drifted from the fund's stated multiple (2x, -1x, and so on) is exactly the decay that has accumulated over that stretch. Most prospectuses already disclose, in some form, that the fund tracks a multiple of daily returns and that cumulative performance can diverge from a simple multiple of the index's cumulative return the longer the holding period runs — worth checking that stated gap against the actual numbers on a periodic basis rather than skimming past it. It's especially worth rechecking right after a stretch of unusually high volatility — earnings season, a rate decision, a geopolitical shock — since that's exactly when decay tends to have built up the fastest.

## Key Takeaways

- Leveraged and inverse ETFs are built to track a multiple of the index's **daily** return, not its cumulative return, and they reset their exposure back to that target every trading day to hold to it.
- That daily reset compounds over time, so even when the underlying index round-trips back to its starting price, a leveraged or inverse fund over the same period can be left showing a loss — volatility decay.
- What drives decay isn't how long a position is held, but how much volatility occurs during that holding period; higher multiples (3x versus 2x) suffer proportionally larger decay under the same volatility.
- In a smooth, low-volatility uptrend, the same compounding mechanism can work in the fund's favor instead — decay is a two-sided consequence of the fund's design, not a flaw.
- Funds built on futures contracts also carry rollover costs and typically higher expense ratios on top of volatility decay, adding further wear over a long holding period.

## Frequently Asked Questions

### Do leveraged ETFs always lose money if you hold them long enough?
No. What causes the loss is volatility during the holding period, not the length of the period itself. In a steady, low-volatility uptrend, holding longer can actually produce returns above a simple index multiple. But in a choppy, range-bound market, decay tends to build up the longer the position is held — which is why leveraged ETFs are generally introduced as tools for short-term directional conviction rather than long-term holdings.

### Is a 3x leveraged ETF always riskier than a 2x one?
Under the same volatility conditions, a higher multiple means proportionally larger volatility decay, so a 3x product is structurally more exposed than a 2x one. Regulatory caps on the maximum multiple mean 3x products (like U.S.-listed TQQQ) aren't common in every market, but the same underlying mechanism applies wherever they trade.

### Is there any way to avoid volatility decay?
Not entirely — the daily reset is structural and can't be removed. Since decay accumulates with both higher volatility and longer holding periods, these funds are generally best used only when there's conviction about a short-term direction. For longer-term exposure, a plain index ETF or another leverage mechanism that isn't reset daily — such as [margin trading](/en/basics/margin-trading-leverage/) — is usually worth comparing instead.

### Does this make leveraged ETFs bad products?
Not inherently. The issue isn't the product itself — it's a mismatch between what the product is designed to do and what an investor expects from it. A leveraged ETF is built as a tool for expressing short-term directional conviction with amplified exposure over a period of days to weeks, not as a vehicle that reliably delivers a multiple of the index's return over months or years. Holding it long-term while expecting that multiple to hold is exactly the scenario where volatility decay extracts its cost.

> ⚠️ This article is for informational and educational purposes only and is not a recommendation to buy or sell any security. The example figures are simplified for illustration; actual fund returns depend on expense ratios, rollover costs, and tracking error, so review the fund's prospectus before investing.
