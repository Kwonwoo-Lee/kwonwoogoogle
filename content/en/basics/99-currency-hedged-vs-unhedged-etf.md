---
slug: currency-hedged-vs-unhedged-etf
title: "Currency-Hedged (H) vs Unhedged (UH) ETFs — Why the Hedging Cost Is Set by the Rate Gap"
description: "Two ETFs track the same S&P 500, yet post different returns for years. Here's why, and how the hedging cost is set by the two countries' interest-rate gap, not by chance."
order: 99
updated: 2026-09-23
keywords: ["currency hedged vs unhedged ETF", "what is a hedged ETF H share", "ETF currency hedging cost explained", "why do hedged ETFs cost more", "hedged ETF underperformance", "interest rate parity ETF hedging", "unhedged ETF currency risk"]
seo_audited: 2026-09-23
---

## Same S&P 500, Different Returns — Why?

Search for a Korea-listed ETF tracking the US S&P 500 and you'll typically find two versions side by side: one with "(H)" tacked onto the name, and one without. Both hold the same index. Yet compare their multi-year cumulative returns and they often diverge noticeably. It isn't because the fund managers picked different stocks — it's because the two funds handle currency risk between the Korean won and the US dollar in fundamentally different ways. Expense ratios often diverge too: in one real product line tracking the US S&P 500, the unhedged share class carries a 0.11% annual fee versus 0.25% for the hedged share class — a 0.14-percentage-point gap. This lesson covers what "H" (hedged) and "UH" (unhedged) actually do, and where that hedging cost comes from and how it gets set.

## What H and UH Actually Do: Cancel the Currency Move, or Leave It In

When a Korean investor buys a US-tracking ETF, a second variable rides along on top of the price return of the underlying assets: the won-dollar exchange rate. If the S&P 500 rises 10% but the won strengthens 5% against the dollar over the same period, the won-denominated return comes in well below 10%. If the won weakens instead, the currency move adds to the return. An **unhedged (UH)** ETF simply passes this currency swing straight through to the investor. A **hedged (H)** ETF, by contrast, uses a separate derivatives position to offset that currency swing, so the investor's return tracks the underlying index itself, converted at a rate the fund effectively locks in rather than whatever the spot rate happens to do. The distinction between H and UH, in other words, has nothing to do with what's inside the fund — it's about who absorbs the exchange-rate variable, and how.

## Hedging Isn't Free: It's Built From Forward Contracts

The critical point is that currency hedging isn't a costless service a fund manager waves into existence — it's implemented through contracts that trade in real financial markets. The manager rolls an **FX forward** contract, typically monthly or quarterly, locking in today the rate at which dollars will convert back to won at a future date. Because the won isn't a freely traded international currency, this is usually done through a **non-deliverable forward (NDF)**, where only the cash difference between the contracted rate and the actual rate at maturity settles — no principal changes hands. Rolling this forward contract month after month generates transaction costs and a price gap similar in character to the basis covered in [How Stock Index Futures Work](/en/basics/stock-index-futures-basis-explained/), and this is exactly why hedged share classes typically carry a higher expense ratio than their unhedged counterparts. A hedge removes a risk, but keeping that hedge in place isn't free.

## Why the Hedging Cost Isn't Arbitrary — It's Set by the Rate Gap

So who sets the price of that forward contract — the hedging cost itself? Nobody sets it arbitrarily. It's determined, almost mechanically, by a principle called **covered interest rate parity**, the same underlying idea as the interest rate parity concept covered in [What Is the Yen Carry Trade?](/en/basics/yen-carry-trade-explained/) — except here it isn't a force that plays out gradually in the spot market; it's already baked directly into the forward contract's price. The logic: converting won into dollars and earning the US short-term rate should, under a perfect hedge, produce the same result as simply holding won and earning the Korean short-term rate. If US rates run higher than Korean rates, an investor in a hedged ETF is effectively giving up the higher dollar yield in exchange for the lower won yield — and that forgone spread shows up as the hedging cost. When Korean rates run higher instead, the hedging cost can flip negative, meaning the hedge actually adds to returns rather than subtracting from them. The sign and size of the cost is set by the two countries' policy and short-term rate gap, not by market sentiment on any given day.

## Working the Hedging Cost With Numbers

A simple example makes this concrete. Say the won-dollar spot rate is 1,350, the 3-month US rate is 4.5% annualized, and the 3-month Korean rate is 3.0%. Using the same cost-of-carry logic behind [How Stock Index Futures Work](/en/basics/stock-index-futures-basis-explained/), the 3-month forward rate works out to roughly:

**Forward rate ≈ Spot rate × [1 + (KRW rate − USD rate) × 90/365]**

1,350 × [1 + (0.030 − 0.045) × 90/365] ≈ 1,350 × 0.99630 ≈ **1,345.00 KRW**

The contracted rate for buying back dollars three months out sits below today's spot rate — in the direction of a stronger won. That roughly 5-won gap (about -0.37% relative to 1,350) is the three-month hedging cost, and annualized it comes to roughly -1.5 percentage points — almost exactly the 1.5-point rate gap (4.5% − 3.0%) itself. That's not a coincidence; the forward price is set by the market precisely to reflect that gap. Holding a hedged ETF, in other words, means structurally accepting a cost of roughly this size, in exchange for removing currency risk.

## The Direction of the Cost Isn't Fixed

The key thing to take from that math is that hedging isn't always a cost. During stretches like the early-to-mid 2020s, when US rates ran meaningfully above Korean rates, won-denominated hedging costs sat in the rough range of 1–2 percentage points a year — a real drag on hedged products. When that rate gap narrows or flips, the hedging cost shrinks or can disappear entirely. So whether H or UH performs better over any given stretch isn't a fixed answer — it depends on how the US-Korea rate gap evolves over that period. Layer the actual currency move on top, and the final return gap between H and UH comes down to two separate forces: the hedging cost itself, and however the exchange rate actually moved.

## Hedge Ratios and Tracking Error: The Hedge Isn't a Perfect Seal

One more wrinkle is worth knowing. A hedged ETF doesn't eliminate currency exposure with perfect precision. A fund's net assets shift daily with price moves and flows, while its forward contracts typically only roll monthly or quarterly. In between, the actual amount that needs hedging and the amount actually locked in under contract drift slightly apart — a hedge ratio that's not exactly 100% — producing a small additional error similar in nature to what's covered in [ETF Tracking Error vs Premium/Discount](/en/basics/etf-tracking-error-premium-discount/). It's usually negligible, but can spike briefly during sharp currency moves. A hedged ETF, in short, offsets currency risk carefully — it doesn't seal it off completely.

## Checking Your Own Hedging Cost

The most reliable way to see what hedging cost you're actually paying is to compare, not guess. Line up the cumulative returns of the H and UH share classes of the same index over the same period, then subtract the actual currency move (the won-dollar rate change) over that stretch from the return gap between them — what's left approximates the realized hedging cost. Fund managers typically disclose the index return, the won-converted return, and the fund's actual return side by side in monthly reports, so lining those three numbers up gives a reasonably clear read on how effectively the hedge worked and what it cost. Checking this gap around periods when the US-Korea rate differential widens or narrows sharply is a useful habit — it makes the trade-off between H and UH far more concrete than reasoning about it in the abstract.

## What the Choice Is Really For

Rather than hunting for which of H or UH is "correct," it's more useful to understand what each is actually for. A hedged share class is the tool for investors who want their won-denominated return to track the underlying index as closely as possible — stripping out the currency variable entirely. An unhedged share class saves the hedging cost but takes on the currency swing directly, which — as covered in [How Currency Moves Affect Corporate Earnings](/en/basics/currency-effects-on-earnings/) — often means the won tends to weaken during crisis periods, so unhedged foreign exposure can end up cushioning a portfolio's overall drawdown rather than just adding noise. This isn't really a question of maximizing returns; it's a judgment call about how much currency exposure you want left in your portfolio. An investor already heavily weighted toward won-denominated assets (Korean real estate, won deposits, domestic equities) might deliberately keep foreign holdings unhedged for the currency diversification. An investor managing money earmarked for a specific future date in won terms — retirement savings, for instance — might prefer the hedged version to narrow that variability. The same index, held for different purposes, can point toward different rational choices — which is exactly why H versus UH isn't a question with one "better" answer.

## Takeaway

- Hedged (H) and unhedged (UH) ETFs hold identical assets; they differ only in whether the fund offsets won-dollar currency moves (H) or passes them through directly (UH).
- Hedging is implemented through rolling forward (typically NDF) contracts, and the cost of maintaining that position is why hedged share classes usually carry higher expense ratios.
- The hedging cost isn't set arbitrarily — covered interest rate parity means it's determined by the interest-rate gap between the two currencies. When US rates exceed Korean rates, the cost is typically a drag; when the gap reverses, it can add to returns instead.
- Whether H or UH performs better isn't fixed — it depends on how the US-Korea rate gap and the actual exchange rate move over the holding period.

## FAQ

### Is a hedged ETF the safer choice?
It removes one source of volatility — currency risk — but takes on a separate, structural cost in exchange. It's a trade of "less volatility" for "higher cost," not a case where one version is unambiguously better.

### What does a negative hedging cost mean?
When Korean rates run above US rates, the math can flip so that the hedging cost becomes negative — the hedged share class effectively earns extra return from maintaining the hedge. This isn't a fixed feature of any particular fund; it shifts with the prevailing rate environment.

### Should I just pick based on the expense ratio difference?
The expense ratio only captures part of the hedging cost. In practice, the size of the actual currency move usually matters far more to your realized return than the fee gap does. Treat the fee as one input, but decide first whether you want currency exposure left in or stripped out, based on your investment horizon and purpose.

### Does this hedging cost apply if I just buy individual foreign stocks directly?
Buying individual foreign stocks through a brokerage account typically leaves you fully unhedged by default. Individual investors generally can't cost-effectively enter their own forward contracts, which is one reason investors who specifically want currency hedging tend to reach for hedged (H) ETFs or funds rather than trying to replicate it stock by stock.

> ⚠️ This article is for informational and educational purposes only and is not a recommendation to buy or sell any specific product. The example figures are simplified for clarity; actual hedging costs and fees vary by product and by market conditions, so review the fund's prospectus before investing.
