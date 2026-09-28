---
slug: etn-exchange-traded-note-explained
title: "What Is an ETN (Exchange-Traded Note)? How It Differs From an ETF"
description: "Why an ETN is an unsecured bond backed by the issuer's credit rather than a fund, how indicative value and tracking gaps form, and the 2020 leveraged oil ETN blowup."
order: 109
updated: 2026-09-28
keywords: ["what is an ETN", "ETN vs ETF difference", "ETN risk explained", "indicative value tracking gap", "leveraged oil ETN Korea", "ETN issuer credit risk", "ETN maturity early redemption"]
seo_audited: 2026-09-28
---

## Same Three-Letter Cousin of ETF — Except It Can Be Delisted Overnight

In April 2020, as COVID-19 sent global oil prices into unprecedented negative territory, a handful of leveraged crude-oil products on the Korean exchange started behaving strangely. The underlying oil index itself hadn't moved anywhere near that much, yet the market price of these products and their "true value" benchmark diverged by more than 1,000% at the extreme. Korea's Financial Supervisory Service issued its highest-level "danger" consumer alert for the first time since the alert system began in 2012. The product name carried a familiar three-letter tag — but it wasn't [ETF](/en/basics/etf-basics/). It was **ETN**. Both trade on the exchange in real time, just like a stock, and both track an index. So why did only the ETN blow up this badly? The answer is that an ETN isn't really a fund at all — it's closer to a securities firm's IOU.

## What an ETN Actually Is: An "Index-Linked Bond" a Brokerage Issues

An ETN (Exchange-Traded Note) is a **derivative-linked security** issued by a brokerage that promises to pay an index's return at maturity. Structurally, it's essentially the same as an unsecured, uncollateralized corporate bond that happens to settle based on an index rather than a fixed coupon. It can track something as mainstream as the KOSPI 200 or a sector index, or something as inconvenient to physically own as crude oil or natural gas futures. Korea Exchange listing rules require only 5 constituent components for an ETN's underlying index, versus 10 or more for an ETF, which lets ETNs cover far narrower and more exotic indices. That's exactly why products built on futures that are hard to physically hold, or on indices like volatility where "ownership" doesn't even conceptually apply, tend to end up as ETNs rather than ETFs. In practice, Korean-listed ETNs skew heavily toward commodity futures (oil, natural gas, gold), government bond yields, and packaged strategies (covered calls, buffer structures) rather than plain domestic sector indices — precisely because indices too awkward to fit an ETF's fund structure end up here instead.

## How It Differs From an ETF: Segregated Trust Assets vs. a Credit Promise

On the surface, an ETN and an ETF are nearly indistinguishable — both trade in real time on the exchange, both track an index, and their names often look alike. Underneath, the legal structures are entirely different. An ETF is a **fund**: the asset manager actually buys stocks, bonds, or other assets and holds them in a segregated trust account. If the manager goes bankrupt, the trust assets are ring-fenced from the manager's other liabilities and still flow back to investors. An ETN has no such segregated pool. The issuing brokerage runs internal hedging trades to track the index, but those are the brokerage's own assets — not property held separately on the investor's behalf. What an ETN holder actually owns is the brokerage's credit promise: "we will pay you the index's return at maturity." If the issuer runs into financial trouble, an ETN holder can, in theory, fail to fully collect gains even if the index performed well. This issuer credit risk is the single defining difference between an ETN and an ETF.

## Indicative Value (IV) and Tracking Gap: Why Market Price Can Drift From "True Value"

An ETN's real-time theoretical price is called its **Indicative Value (IV)** — the equivalent of an ETF's net asset value (NAV). The problem is that since an ETN isn't a basket of real assets but a brokerage's promise, its market price can diverge from that indicative value by an arbitrary amount. That gap is called the **tracking (premium/discount) gap**, calculated as (market price − indicative value) ÷ indicative value. ETFs can theoretically drift too, but an arbitrage mechanism — creation and redemption, where authorized participants swap a physical basket of assets for ETF shares — pulls the price back quickly. ETNs have no such physical-basket arbitrage channel, so when volume spikes or markets panic, the gap can open far wider and stay open far longer. In April 2020's oil-price collapse, several domestic leveraged and inverse crude-oil ETNs saw their tracking gap surge to between 35.6% and 95.4%, briefly exceeding 1,000% on some products. Investors who bought at the inflated market price without realizing how far it had drifted from indicative value took sharp losses the moment the gap corrected back toward fair value. Korea Exchange later introduced a rule suspending trading in any ETN whose gap exceeds 30% for five consecutive trading days.

## The Liquidity Provider System: A Structural Dilemma When the Issuer Is Also the Market Maker

Behind how wide this gap can get is the ETN-specific liquidity provider structure. [Thinly traded products like ETFs, ETNs, and ELWs](/en/basics/market-microstructure-basics/) are required by the exchange to have a brokerage continuously quoting both bid and ask prices — and for ETNs, that Liquidity Provider (LP) role is usually filled by the issuing brokerage itself. In other words, the same firm that manufactured and sold the product is effectively managing its market price too. Under normal conditions, the LP quotes tightly around indicative value and keeps the gap narrow. But in a volatility spike, that same LP may pull back its quoting or widen its spread for its own risk-management reasons — and Korean rules impose no immediate, meaningful penalty on an LP or issuer simply for letting the gap widen. That's widely cited as the ETN structure's core vulnerability. Unlike an ETF's LP system, which is backstopped by a separate physical-basket arbitrage channel through creation and redemption, an ETN's LP has to rely on its own quotes alone to keep the gap in check — a structural limit that simply doesn't exist for ETFs.

## A Cautionary Tale From Abroad: The Credit Suisse XIV Collapse

Issuer credit risk actually materializing into investor losses happened first in the US market. Credit Suisse's VelocityShares XIV, an ETN designed to move inversely to the [VIX](/en/basics/vix-implied-volatility-explained/) volatility index, lost over 90% of its value in a single day during the so-called "Volmageddon" of February 2018, when the VIX spiked violently. Credit Suisse invoked an acceleration (early-redemption) clause written into the note's terms and delisted the product, and holders were paid out at that already-collapsed price. This wasn't a case of the product tracking its index incorrectly — it happened because the issuer held a contractual right to terminate the product on its own terms. It's a clear illustration of what holding an ETN actually means: you're operating under conditions the issuer defined in advance.

## Maturity and Early Redemption: The "Expiration Date" an ETF Doesn't Have

An ETF, in principle, has no maturity date and simply continues to exist unless the manager decides to wind it down. An ETN is different — it's a bond-like security issued with a fixed **maturity**, typically somewhere between 1 and 20 years, set from the day it's issued. At maturity, it's cash-settled based on the indicative value at that point and the product ceases to exist. Most ETN terms also include an **early redemption** clause, allowing the issuer to force redemption before maturity if the indicative value falls below a set threshold or if the issuer determines its hedging has become impractical. From an investor's standpoint, that means the investment can end on the issuer's timeline, not yours, without much warning — another structural feature an ETF simply doesn't have.

## Is Taxation the Same as an ETF?

Even though the legal structure differs, the tax treatment Korean investors face largely mirrors ETFs. An ETN tracking a domestic stock price index is exempt from tax on trading profit, exactly like a domestic-index ETF. An ETN tracking overseas indices, commodities, or bonds, on the other hand, has its trading profit taxed at 15.4% withheld as [dividend income tax](/en/basics/dividend-income-tax-explained/) — again, the same treatment as an overseas or commodity ETF. On top of that, ETNs are subject to holding-period taxation, meaning taxable income can be assessed on the annual rise in indicative value even if you never sell — a detail investors frequently overlook. These specifics vary by product and by whether the underlying index is domestic or overseas, so always check the prospectus's tax section before trading.

## A Worked Example: How a Tracking Gap Actually Opens Up

Here's a simplified example to make this concrete. Say a leveraged ETN tracking 2x an oil futures index has an indicative value of ₩10,000. Under normal conditions, the LP quotes tightly, keeping the market price around ₩9,950–₩10,050 — roughly a ±0.5% gap. Now suppose oil prices crash in a single day, buy orders from investors pile up on one side, and the LP simultaneously pulls back its ask-side quoting for its own risk management. The indicative value might fall to ₩9,000, reflecting the oil price drop — but the market price, pushed by lopsided demand, could actually climb to ₩12,000. The tracking gap here is (12,000 − 9,000) ÷ 9,000 × 100 ≈ 33%, meaning the product is trading more than a third above its indicative value. An investor who bought based on the market price alone, unaware of that gap, ends up absorbing a loss unrelated to the index itself the moment LP quoting normalizes and the market price snaps back toward indicative value. This is essentially the mechanism behind Korea's 2020 leveraged oil ETN blowup.

## Takeaway

- An ETN is an unsecured, uncollateralized bond-like security issued by a brokerage promising an index's return — fundamentally different from an ETF, which holds real assets in a segregated trust.
- An ETF's trust assets stay protected even if the manager goes bankrupt; an ETN depends entirely on the issuing brokerage's own credit, and a struggling issuer can leave gains uncollected.
- Indicative Value (IV) is an ETN's theoretical price, and without a physical-basket arbitrage mechanism, its tracking gap versus market price can open far wider and last far longer than an ETF's.
- Korea's 2020 leveraged oil ETN gap blowout and Credit Suisse's 2018 XIV delisting are both real-world cases of this structural risk materializing.
- The issuer often doubles as the liquidity provider, and a fixed 1-to-20-year maturity plus an early redemption clause adds an "expiration date" risk that ETFs simply don't carry.

## FAQ

### Is an ETN always riskier than an ETF?
It's true that issuer credit risk and early-redemption risk are structurally present in a way they aren't for ETFs. That said, only large brokerages meeting minimum capital and credit-rating requirements are permitted to issue ETNs in Korea, so this risk rarely materializes under normal conditions. The risk is different in kind from an ETF's, not automatically greater in every case.

### How can I tell if an ETN has a wide tracking gap?
Most trading platforms display indicative value alongside market price on an ETN's quote screen, and Korea Exchange also publishes tracking-gap disclosure data. This matters most for [leveraged and inverse products](/en/basics/leveraged-inverse-etf-decay/), which track more volatile underlyings — checking the gap before trading becomes especially important when markets are moving fast.

### Do ETNs pay dividends or distributions?
It depends on the underlying index's structure. Some ETNs track indices designed to automatically reinvest dividends, while others do make distributions. Because an ETN is fundamentally a bond-like security, its range of distribution structures tends to be narrower than an ETF's — always check the prospectus for the specific product.

### What's different about an ETN with "2x" or "3x" in its name?
That's a leveraged ETN designed to track double or triple the index's daily move. These carry the same structural trap covered in [leveraged and inverse ETF decay](/en/basics/leveraged-inverse-etf-decay/), stacked on top of the issuer credit risk and tracking-gap risk already discussed here. The higher the multiple, the larger the indicative value's own swings — and the larger the potential loss if the market price drifts away from that indicative value.

> ⚠️ This article is for informational and educational purposes only and is not a recommendation to trade any specific product. ETNs are derivative-linked securities that carry issuer credit risk and early-redemption risk — always review the issuer's prospectus and risk disclosure before trading.
