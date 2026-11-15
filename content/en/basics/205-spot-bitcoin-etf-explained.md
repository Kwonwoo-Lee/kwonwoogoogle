---
slug: spot-bitcoin-etf-explained
title: "What Is a Spot Bitcoin ETF: How It Trades Crypto Through a Stock Brokerage Account"
description: "How spot Bitcoin ETFs custody, create, and redeem shares to track crypto's price, how they differ from futures ETFs and holding coins directly, and the regulatory questions Korean investors face."
order: 205
updated: 2026-11-15
keywords: ["what is a spot bitcoin etf", "spot bitcoin etf vs futures etf", "how does a bitcoin etf work", "bitcoin etf custodian", "bitcoin etf tracking error", "bitcoin etf creation redemption", "IBIT explained", "buy bitcoin etf"]
seo_audited: 2026-11-15
---

## A Crypto Asset, Traded Like a Stock

When the SEC approved spot Bitcoin ETFs like BlackRock's IBIT and Fidelity's FBTC in January 2024, buying bitcoin through an ordinary brokerage account stopped being a hypothetical. There's no wallet to set up, no private key to protect, no crypto-exchange account to open — just a ticker symbol in the same app investors already use for stocks. But calling it an "ETF" doesn't mean it behaves exactly like [the ETFs covered earlier in this course](/en/basics/etf-basics/). The underlying asset here trades 24 hours a day on crypto markets, not during stock-exchange hours, and that single difference changes both how the fund's price tracks its value and what risks an investor actually takes on. This lesson covers what a spot Bitcoin ETF actually holds, the mechanism that keeps its price pinned to bitcoin's spot price, and how it differs from a futures ETF or holding the coin directly.

## Three Ways to Get Exposure: Direct Holding, Futures ETF, Spot ETF

There are three broad routes to bitcoin exposure, and each carries a different kind of risk.

**Holding the coin directly** is the most literal approach: open an account on a crypto exchange, buy bitcoin, and store it in an exchange wallet or a personal one. It tracks the coin's price most purely, but the investor personally bears the risk of an exchange hack or bankruptcy, or losing their own private key.

**Futures ETFs** don't buy bitcoin at all — they hold bitcoin futures contracts listed on the Chicago Mercantile Exchange (CME). The U.S. approved futures ETFs first, back in 2021, on the reasoning that the futures market was already regulated by the CFTC. The catch is that futures contracts expire and have to be rolled into the next month's contract, which creates the same kind of problem covered in [the lesson on leveraged and inverse ETF decay](/en/basics/leveraged-inverse-etf-decay/) for oil ETFs. When longer-dated futures trade persistently above near-term ones — a contango market — rolling means selling the expiring contract cheap and buying the next one expensive, bleeding a little value every month. Held long enough, a futures ETF can noticeably lag the actual price gain in bitcoin.

**Spot ETFs** actually buy bitcoin and hold it with a custodian, then let investors trade a share that represents a claim on that holding. Because there's no futures contract to roll, a spot ETF can in principle track bitcoin's price more cleanly than a futures ETF. For most investors, the appeal is that everything — the trade, the tax reporting, inheritance — happens inside the same brokerage framework used for any other listed security, with no separate wallet or exchange account required.

## How the Price Stays Pinned to Bitcoin: Creation, Redemption, and Custody

The mechanism that keeps a spot Bitcoin ETF's price close to its underlying value is essentially the authorized-participant (AP) creation-and-redemption process covered in [the lesson on ETF tracking error and premium/discount](/en/basics/etf-tracking-error-premium-discount/). When the ETF's market price trades above the value of the bitcoin it holds (its NAV), an AP delivers assets to the issuer in exchange for new shares and sells those shares into the market at a profit. When the price trades below NAV, the AP buys cheap shares, redeems them for the underlying assets, and sells those assets at a profit. Repeated enough times by enough participants, this arbitrage keeps the market price anchored near NAV.

How that creation and redemption actually happens has changed since launch. At approval in early 2024, nearly all U.S. spot Bitcoin ETFs used "cash creation": an AP hands the issuer dollars, and the issuer (or its custodian) uses that cash to buy bitcoin and add it to the fund's holdings. That's an extra transaction layered into the process, adding cost and timing friction. In July 2025, the SEC approved "in-kind creation and redemption" across U.S. spot Bitcoin and Ethereum ETFs, letting an AP deliver bitcoin itself directly to the issuer in exchange for shares, skipping the intermediate cash-to-bitcoin trade. That shortens the arbitrage loop, making it faster and cheaper to execute — and in principle lets the market price track NAV more tightly.

The other essential party in this structure is the custodian — the entity that physically safeguards the bitcoin the fund has purchased. Most U.S. spot Bitcoin ETFs use Coinbase Custody Trust Company; Fidelity is a notable exception, using its own Fidelity Digital Assets subsidiary. Buying a share of the ETF means trusting that this custodian actually holds the bitcoin it claims to — and if that trust breaks down, through a hack or custodian insolvency, the entire value proposition of the fund is compromised in a way that doesn't apply to an ordinary equity ETF holding shares of real companies.

## Why Premiums and Discounts Stand Out More in a Crypto ETF

As covered in [the lesson on ETF tracking error and premium/discount](/en/basics/etf-tracking-error-premium-discount/), any ETF's market price can drift from its NAV, but spot Bitcoin ETFs have one extra condition that makes this more visible. Bitcoin trades globally, around the clock, every day of the week. The ETF itself only trades during regular stock-exchange hours. If bitcoin moves sharply while U.S. markets are closed, the ETF's NAV — calculated off the previous close — stays frozen while the underlying asset has already moved, and the ETF's market price tries to reflect that overnight move the instant trading resumes, producing a premium or discount that can look unusually wide for a moment. Authorized-participant arbitrage usually narrows this gap quickly, but during periods of sharp crypto volatility, that narrowing can itself slow down.

A simple example: suppose one ETF share represents 0.0005 bitcoin, and bitcoin closed the previous day at $65,000, putting the prior NAV at $32.50 per share. If bitcoin rallies 5% to $68,250 overnight while U.S. markets are closed, the ETF's market price at the next open will try to jump toward roughly $34.13 to reflect that move — while the officially published NAV may still reference the prior close, making the gap look larger than it structurally is. Issuers typically publish a real-time estimated value (iNAV) throughout the trading day specifically to narrow this visible gap, so it isn't a permanent distortion — but it's a dynamic investors in crypto ETFs encounter more often than holders of ordinary equity ETFs.

## Fees and Tracking Difference: What Holding One Actually Costs

Spot Bitcoin ETFs charge an expense ratio just like any other ETF. Major U.S. issuers competed aggressively on fees at launch, and many of these funds now charge somewhere around 0.19% to 0.25% annually. Holding bitcoin directly in a personal wallet avoids that recurring fee, but trades it for exchange fees and the ongoing burden of securing the asset yourself. To put the fee in concrete terms: a $10,000 investment in a fund charging 0.25% a year loses roughly $25 to fees over a year even if bitcoin's price doesn't move at all. Add in custody costs and the transaction costs baked into the creation-redemption cycle, and a spot Bitcoin ETF's realized return tends to run slightly below bitcoin's actual spot-price return — the same tracking-difference concept covered in [the ETF tracking error lesson](/en/basics/etf-tracking-error-premium-discount/).

## The Regulatory and Tax Picture for Korean Investors

As of late 2026, Korean brokerages still cannot intermediate trades in U.S.-listed spot Bitcoin ETFs for domestic clients. Financial regulators have historically restricted both domestic listing and brokerage access on the grounds that crypto doesn't qualify as a conventional underlying asset under capital markets law. That said, the government's 2026 growth strategy has reportedly tied the introduction of a domestic digital asset framework and capital markets law amendments to exploring a path toward domestic spot crypto ETFs, so the policy direction appears to be shifting. No confirmed approval or listing timeline exists as of this writing, so anyone considering this should check the latest notices from Korea's Financial Services Commission and their own brokerage before assuming access.

Taxes add another layer of uncertainty. Direct crypto income taxation in Korea — delayed three times since it was first announced in 2020 — is currently scheduled to take effect January 1, 2027, applying a 22% rate (20% income tax plus 2% local tax) to gains above an annual 2.5 million won exemption. Separately, capital gains from trading U.S.-listed ETFs as foreign stocks already fall under the existing overseas-stock capital gains framework, which uses the same 22% rate above the same 2.5 million won annual exemption. Whether a spot crypto ETF held through a Korean brokerage would be taxed as a foreign-listed ETF or folded into the crypto-specific tax regime isn't yet settled, so this is worth confirming with current tax authority guidance at the time of any actual investment.

## The Risks That Don't Go Away

Wrapping bitcoin in an ETF removes the hassle of managing a wallet, but it doesn't eliminate risk. Custody risk tops the list: an ETF investor is ultimately relying on the custodian actually holding the bitcoin it claims to, and a security breach or operational failure there is outside the investor's control. Regulatory risk is next — even an approved structure can be affected by future policy shifts in any jurisdiction that change trading conditions or the product's design. And underlying volatility doesn't disappear just because the wrapper changed: an ETF passes through bitcoin's price swings largely unchanged, plus whatever its fees take off the top.

## Takeaways

- A spot Bitcoin ETF holds actual bitcoin with a custodian and lets investors trade a share representing that holding, just like an ordinary stock.
- Unlike a futures ETF, it has no roll or contango decay; unlike holding coins directly, it needs no private key management or exchange account.
- Its price tracks bitcoin's value through authorized-participant creation and redemption arbitrage, which became faster and cheaper after the SEC approved in-kind creation in July 2025.
- Because bitcoin trades 24/7 while the ETF only trades during market hours, premium/discount gaps tend to look more pronounced than in a typical equity ETF.
- Korean brokerages still can't intermediate U.S.-listed spot Bitcoin ETF trades as of this writing, and both a domestic ETF framework and the applicable tax treatment remain unsettled.

## FAQ

### Does a spot ETF track bitcoin's price better than a futures ETF?
Generally, yes. A futures ETF has to roll contracts at each expiration, which bleeds value during contango markets. A spot ETF holds the actual coin, so it has no equivalent roll cost.

### Can Korean investors buy a spot Bitcoin ETF right now?
As of this writing, Korean brokerages cannot intermediate trades in U.S.-listed spot Bitcoin ETFs. The government has reportedly been reviewing a framework for domestic crypto ETFs, but no confirmed approval or launch date exists, so check current notices from regulators and your brokerage before assuming access.

### Do spot Bitcoin ETFs have tracking error like other ETFs?
Yes. Expense ratios and custody-related costs chip away at returns daily, producing a small negative tracking difference relative to bitcoin's spot-price return — though usually nowhere near the scale of a futures ETF's roll losses.

> ⚠️ This lesson is for educational purposes only and does not recommend any specific ETF or cryptocurrency. Fee levels, policy status, and tax rates cited here are simplified summaries based on public reporting and common understanding as of the writing date; verify current figures and regulations through official issuer and regulator disclosures.
