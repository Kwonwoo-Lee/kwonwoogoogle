---
slug: carry-trade-yen-unwind
title: "Carry Trade Strategy Explained: How the Yen Carry Trade Works (and Why It Unwinds)"
description: "Learn how the carry trade turns interest-rate gaps into profit, why the yen carry trade keeps making headlines, and the leverage math behind its violent unwinds."
order: 93
updated: 2026-10-24
keywords: ["carry trade strategy", "yen carry trade explained", "carry trade unwind", "interest rate differential trading", "AUD/JPY carry trade", "carry trade risk", "forex carry trade", "uncovered interest rate parity"]
---

## The Carry Trade: Turning an Interest Rate Gap Into a Tradeable Asset

Most strategies covered so far in this course trade price direction, trend, or reversion. The **carry trade** is built on a different source of return entirely — it tries to pocket the **interest rate differential** between two currencies even if the exchange rate barely moves.

The mechanics are simple. You borrow (or sell short) a low-interest-rate currency — the **funding currency** — and use the proceeds to buy a higher-yielding currency's assets or interest-bearing instruments, the **target currency**. The gap between the two rates is called the **carry**, and as long as you hold the position, that gap accrues to you day after day. For decades, **the Japanese yen (JPY)** has been the textbook funding currency because Japan has kept policy rates near zero for so long, while typical target currencies include the Australian dollar (AUD), the Mexican peso (MXN), or other relatively high-yield emerging-market and commodity-linked currencies. A carry trade funded in yen is specifically called the **yen carry trade**, and it's remained a recurring market-moving story through 2025 and 2026, resurfacing every time the Bank of Japan (BOJ) signals another rate hike after the large August 2024 unwind.

## Why Does This "Free Money" Exist? Theory vs. Reality

The obvious question: if this is so easy, why doesn't everyone just do it forever? Textbook international finance theory — **uncovered interest rate parity (UIP)** — actually predicts the opposite outcome. It says the higher-yielding currency should depreciate by roughly the amount of the rate gap, so that expected returns end up equal no matter which currency you hold. In other words, carry trades shouldn't offer a persistent edge at all, in theory.

Yet real-world data has repeatedly failed to match that prediction — a gap long documented in academic finance under the name the **forward premium puzzle**. Rather than steadily weakening as the theory implies, high-yield currencies have often stayed flat or even strengthened for extended stretches. Economists offer several competing explanations — risk premia, leverage constraints facing arbitrageurs, differences in central bank credibility — but there's no single, fully agreed-upon cause. What matters for traders is simpler: it's precisely because this "anomaly" can persist for years that carry trades keep getting put on again and again. The flip side, covered below, is that the same persistence is exactly what sets up the violent unwinds.

## How a Carry Trade Is Actually Built

In practice, there are three common ways to structure a carry trade.

| Method | Structure | Notes |
|---|---|---|
| Spot FX + rollover (swap points) | Hold a long position in the high-yield currency and short the low-yield one in a margin FX account | A swap point reflecting the rate gap is credited or debited at each daily rollover. The most accessible route for retail traders |
| Currency futures / FX forwards | Trade a forward contract whose price already prices in the rate differential | No daily swap settlement needed; the structure is cleaner and fixed at entry |
| Direct high-yield bonds or deposits | Borrow in (or convert from) the low-yield currency and invest directly in the target country's bonds or deposits | Involves conversion and transfer costs, but gives a tangible sense of holding a real asset |

The two most commonly cited pairs in carry trade education are **AUD/JPY** (long Australian dollar, short yen) and **MXN/JPY** (long Mexican peso, short yen) — both have satisfied the combination of an ultra-low-rate funding currency and a relatively high-yield target currency for years, which is why they show up constantly as worked examples.

## A Worked Numeric Example

Say you hold an unleveraged $10,000 AUD/JPY carry position for one year. (The rates below are illustrative assumptions for the sake of the math — always check the actual current policy rates before trading, since they move over time.)

- Assumed Australian policy rate: 4.0% per year
- Assumed Japanese policy rate: 0.75% per year
- Rate differential (the carry): 3.25% per year

If the exchange rate doesn't move at all over the year, the simple carry accrued on a $10,000 position is roughly **$325 (3.25%)**. In practice, brokers calculate swap points differently and charge their own markups, so the amount actually credited is often somewhat less than this theoretical figure.

Now apply 5x leverage. With the same capital, your position size grows to $50,000, so the carry income scales up to roughly $1,625 — about 16.25% on your actual capital. This is where the real character of the trade shows up: **without leverage, the raw interest-rate edge is often too small to bother with, but the moment you apply leverage, your exposure to exchange-rate moves scales up by exactly the same multiple.** If the yen strengthens 5% against the Australian dollar while you hold that 5x-leveraged position, you take roughly a -25% loss on your capital — wiping out several years' worth of carry income in one move. This asymmetry — steady small gains against rare but large losses — is exactly why the ATR-based stop-loss discipline from Lesson 13 and the position-sizing logic behind the Kelly criterion in Lesson 42 apply just as directly to carry trades as to any directional strategy.

## Carry Trade vs. Funding Rate Arbitrage: Two Ways to Harvest a Rate Gap

The [funding rate arbitrage](/en/strategies/funding-rate-arbitrage/) strategy from Lesson 62 gets confused with the carry trade often, since both profit from "something that looks like a rate gap." The underlying mechanics and risk profile, though, are genuinely different.

| | Carry Trade | Funding Rate Arbitrage |
|---|---|---|
| Source of profit | The policy rate gap between two countries | The funding rate that keeps perpetual futures anchored to spot price |
| Directional exposure | Yes — exchange-rate moves flow straight through to P&L | No — long spot + short perpetual offsets price moves (delta-neutral) |
| Main risk | A sharp rally in the funding currency (yen strength) | Funding rate flipping sign, exchange risk, approaching liquidation price |
| Typical holding period | Months to years | Days to months |

Funding rate arbitrage is hedged against price moves by construction — it's directionless. The carry trade is not; it's directly exposed to exchange-rate direction. That difference is exactly why carry trades can deliver steady gains during calm markets but face much larger drawdowns the moment volatility spikes.

<figure class="diagram">
  <img src="/static/img/charts/en/carry-trade-yen-unwind.svg" alt="Diagram showing the carry trade's asymmetric return profile: carry income from borrowing a low-yield currency to hold higher-yield assets accrues slowly in a staircase pattern, then a risk-off trigger sends the funding currency sharply higher, forcing margin calls and a liquidation that erases months of gains within days" loading="lazy">
  <figcaption>Left: the carry (rate differential) accrues slowly, day by day, in a staircase pattern. Right: a risk-off trigger sends the funding currency (the yen) sharply higher, forcing margin calls and a liquidation that erases the accumulated return in a matter of days.</figcaption>
</figure>

## Unwind Risk: Up the Stairs, Down the Elevator

The most-quoted line describing the carry trade's return profile is "**up the stairs, down the elevator.**" Carry income accrues slowly and steadily, a little bit every single day — but unwinds tend to happen all at once, compressed into a few days or even hours.

The typical sequence that triggers an unwind looks like this:

1. **The funding currency's rate rises, or risk-off sentiment spreads across markets broadly.** A BOJ rate-hike signal, a sharp global equity selloff, or a shockingly weak U.S. jobs report are all classic triggers.
2. **The funding currency (the yen) rallies sharply.** As carry traders rush simultaneously to buy back yen to repay their positions, that very demand can feed on itself and accelerate the yen's rally further.
3. **Leveraged positions hit margin calls and get force-liquidated.** The resulting wave of selling often spills into the target-currency assets being held — stocks, bonds, and other instruments that otherwise have nothing to do with the carry trade itself — dragging down markets that look, on the surface, unrelated.

This is exactly what played out in August 2024, when a faster-than-expected BOJ rate hike collided with fears of a weakening U.S. labor market, triggering a rapid yen carry trade unwind that shook global equity markets within days — an episode that's been used as the reference point ever since, every time "yen carry trade unwind" risk resurfaces. These unwind episodes also connect directly to the volatility regimes covered in Lesson 28 on [VIX term structure](/en/strategies/vix-term-structure-contango-backwardation/): the more carry positioning has built up, the more easily a spike in volatility (VIX) can cascade into a currency unwind, which in turn spills into broader asset-market selling.

## Risk Management Notes

- **Nobody can tell you exactly how much carry trade positioning is out there.** Estimates of speculative positioning vary widely between institutions, and even after the fact it's hard to pin down a precise number. Rather than trying to quantify "how much unwind risk is built up right now," it's more realistic to track the direction of central bank policy and shifts in broad market risk appetite.
- **Leverage scales carry income and exchange losses by the exact same multiple.** As the worked example above shows, the unleveraged annual return on a carry trade is often modest. Any time leverage is applied, a pre-defined stop-loss based on exchange-rate movement, not just the carry itself, is essential.
- **Watch the funding currency's central bank closely.** For a yen carry trade, BOJ rate decisions and forward guidance are the single most direct trigger to monitor.
- **"There's a rate gap" alone is not a reason to enter.** Rate gaps between countries exist almost all the time, in some form. The real judgment call is whether that gap is large enough, and whether broad market risk appetite looks stable enough, to make holding through the position's lifetime reasonable.

## FAQ

### Can retail traders actually do carry trades?
Yes — margin FX brokers let retail traders build carry-trade-style positions directly. Keep in mind that leverage magnifies exchange-rate risk, and swap points (rollover interest) vary by broker, so the amount actually credited is often smaller than the theoretical rate differential.

### Why does a yen carry trade unwind affect stock markets at all?
Because capital raised through yen carry trades has flowed into a wide range of assets worldwide, not just currency pairs — equities, bonds, and more. When an unwind forces traders to buy back yen, the asset sales needed to raise that yen can hit markets that look completely unrelated to the carry trade on the surface, at least in the short term.

### Which is safer — the carry trade or funding rate arbitrage?
Structurally, funding rate arbitrage is delta-neutral (hedged against price moves), while the carry trade carries direct exchange-rate exposure, so the former is generally described as more defensive against price risk. That said, funding rate arbitrage carries its own risks — exchange/counterparty risk and funding-rate reversals — so it would be an overstatement to call either one unconditionally "safer."

## Summary

- The carry trade profits from the **interest rate gap between two countries**, not exchange-rate direction per se — borrowing a low-yield currency (classically the yen) to fund positions in higher-yield currencies like the AUD or MXN.
- Theory (uncovered interest rate parity) says the rate gap should be offset by currency depreciation, but the real-world "forward premium puzzle" shows that gap can persist for extended periods — which is exactly why the trade keeps getting put on repeatedly.
- Leverage scales both the carry income and the exchange-rate risk by the same multiple, so it's essential to weigh the unleveraged return against the potential loss from a sharp currency move before adding leverage.
- Unlike funding rate arbitrage (Lesson 62), the carry trade carries real directional exposure, which is why it tends to show the "up the stairs, down the elevator" pattern — steady gains in calm markets, sudden violent unwinds when the funding currency spikes during risk-off episodes.
- As the August 2024 yen carry trade unwind showed, the true scale of built-up carry positioning is never precisely knowable in advance, so tracking central bank policy shifts and market risk appetite — combined with a pre-set stop-loss — is the realistic way to manage this risk.
