---
slug: elw-equity-linked-warrant-explained
title: "What Is an ELW (Equity-Linked Warrant)? How It Differs From Listed Options"
description: "How conversion ratio and parity set an ELW's price, why it needs a liquidity provider, and the issuer credit risk that makes it fundamentally different from listed options."
order: 108
updated: 2026-09-28
keywords: ["what is an ELW", "equity linked warrant explained", "ELW vs options difference", "ELW conversion ratio parity", "ELW gearing leverage", "liquidity provider ELW", "ELW risk warrant"]
seo_audited: 2026-09-28
---

## A Stock That Moves 50% in a Day — Except It Isn't Actually a Stock

Search for Samsung Electronics on a Korean brokerage app and you'll get a flood of unfamiliar tickers tacked onto the name — things like "Samsung Electronics Call KB" or "Samsung Electronics Put Koreainvest" — priced at a few hundred won each, swinging tens of percent in a single session. That's an **ELW (Equity-Linked Warrant)**. It buys and sells the same basic idea as an option — "the right to buy or sell at a fixed price, at a fixed future date" — which is why the two get confused constantly. But look at who actually creates and stands behind that right, and the products turn out to be built on fundamentally different foundations. Miss that distinction and you can end up carrying a risk that plain listed options simply don't have — which is a large part of why ELWs have such an outsized retail footprint in Korea, and why they've drawn repeated controversy over investor losses.

## What an ELW Actually Is: A Right a Brokerage Manufactures and Sells

An ELW is a security tied to an underlying stock or index — often [the KOSPI 200](/en/basics/index-weighting-methodology/) — that pays out the difference between a preset strike price and the underlying's price at maturity. One designed to profit when the underlying rises past the strike is a **call warrant**; one designed to profit when it falls below the strike is a **put warrant**. So far, this is identical to a call or put option. The real difference is who manufactures the right in the first place. A listed instrument like [KOSPI 200 options](/en/basics/black-scholes-option-pricing-model/) is opened by the Korea Exchange itself, in standardized contract terms, with a central clearinghouse guaranteeing every trade's settlement. An ELW, by contrast, is issued and listed by an individual brokerage — Mirae Asset, KB Securities, whoever — under its own name. If listed options are a public market the exchange operates, an ELW is closer to a private product a brokerage builds and then lists on the exchange's rails.

## How This Changes the Risk: Issuer Credit Risk Options Don't Have

Different issuers means a genuinely different category of risk, not just a paperwork difference. With a listed option, if the counterparty defaults, the exchange's clearinghouse steps in and honors settlement, backed by a margin system built for exactly that. An ELW has no such backstop — it depends entirely on the issuing brokerage's own solvency. The exchange guarantees that trades execute; it does not guarantee that the issuer will actually have the cash to pay out at maturity. In practice, this means that if the issuing brokerage went bankrupt or entered restructuring, a holder of an in-the-money ELW could, in theory, fail to collect the full payout even though the position was profitable on paper. Because only large brokerages meeting minimum capital and credit-rating requirements are allowed to issue ELWs in Korea, this risk rarely materializes in practice — but it's structurally present in a way it simply isn't for listed options. The tradeoff runs the other way, too: KOSPI 200 options only track one index, while ELWs are issued against hundreds of individual stocks, letting investors take a small, directional bet on a specific name that a broad index option can't offer.

## A Name That Confuses People: This Is Not the Same Thing as a Company-Issued Warrant

The word "warrant" invites another mix-up — with the warrants attached to [convertible and warrant-linked bonds (CB/BW)](/en/basics/convertible-bonds-cb-bw/). Those two products serve completely different purposes. A BW's warrant is issued directly by the company itself to raise capital, and exercising it forces the company to print new shares, diluting existing shareholders. An ELW carries no such connection to the underlying company at all — it's a derivative manufactured by an unrelated third-party brokerage, and exercising it changes nothing about the underlying company's share count. Cash simply changes hands between the issuing brokerage and the ELW holder. From the underlying company's perspective, an ELW is essentially a side bet that has nothing to do with it, which is exactly what separates it from a BW warrant's role as a genuine corporate financing tool.

## How the Price Is Set: Conversion Ratio and Parity

The first concept to understand in ELW pricing is the **conversion ratio**. A full right to one share of the underlying would be too expensive to trade conveniently, so issuers slice it up: one ELW share carries only 1/conversion-ratio of the underlying's right. If the conversion ratio is 10, you need 10 ELW shares to equal one full share's worth of the underlying right. A lower conversion ratio makes each ELW share more expensive; a higher one makes it cheaper.

The second concept is **parity**, which tells you whether an ELW is currently in the money (ITM) or out of the money (OTM). For a call warrant, parity is (underlying price ÷ strike price) × 100; for a put, it's (strike price ÷ underlying price) × 100. Above 100%, the warrant already carries intrinsic value if settled right now; below 100%, it doesn't yet. The ELW's price is that intrinsic value plus a time-value component tied to time remaining and volatility — exactly the same structure covered in [options as insurance](/en/basics/options-as-insurance/).

## Gearing and Time Decay: Why It Swings Tens of Percent in a Day

The figure that shows how much an ELW moves for every 1% move in the underlying is called **leverage**, or **gearing**. A gearing of 15 means that if the underlying rises 1%, the ELW's price theoretically moves about 15% in response. That multiplier is exactly why a few-hundred-won ELW can swing tens of percent in a single day off a modest move in the underlying stock. Gearing isn't a fixed number, though — it changes continuously with the underlying price and with parity, in essentially the same way delta and gamma behave, as covered in [option Greeks](/en/basics/option-greeks-delta-gamma-theta-vega/).

And like an option, an ELW's time value erodes automatically as maturity approaches. Reach maturity out of the money, and the ELW is simply delisted, with the full investment lost. A stock has no expiration date — as long as the company survives, there's always a chance to recover a loss. An ELW's clock runs out on a fixed date, and that chance to recover disappears along with it. This is the risk beginners most often underestimate.

## The Liquidity Provider System: The Issuer, Not the Exchange, Stands Behind the Quotes

A heavily traded listed option can generate reasonable liquidity just from buy and sell orders among market participants. ELWs are different: there are simply too many of them, and volume per individual name tends to be thin, making it hard to trade at a fair price whenever you actually want to. To fill that gap, the issuing brokerage takes on the role of **Liquidity Provider (LP)**, continuously quoting both bid and ask prices. That means a trade can happen even with no other counterparty present — but it also means a meaningful share of the price you actually get reflects the issuer's own theoretical valuation model, not a price genuinely negotiated between market participants.

This structure has been a source of real controversy. Around 2010, Korea's ELW trading volume swelled past ₩1 trillion a day, and so-called "scalpers" — ultra-high-frequency traders — were accused of exploiting predictable patterns in LP quoting to gain an edge. In 2012, the exchange responded by restricting LPs to quoting only when the bid-ask spread exceeded a set threshold (15%). That fix created its own side effect — wider quote gaps that made it harder for ordinary investors to trade at all — and the rules have been revised several times since. The mere existence of the LP system is a clear sign that ELW price formation runs on different mechanics than a listed option's order book.

## Investor Protections: Minimum Deposits and Mandatory Education

Given the overlapping risks of gearing, time decay, and issuer credit exposure, ELW trading isn't something anyone with a brokerage account can simply switch on. First-time ELW traders in Korea must deposit a minimum **basic deposit amount** with their broker and typically complete an online investor-education module or simulated-trading exercise first. This mirrors the education and simulated-trading requirements imposed on first-time derivatives traders more broadly, such as those trading KOSPI 200 options — a minimal safeguard against trading a highly leveraged product without actually understanding how it works.

## A Worked Example

Say a stock trades at ₩60,000, and a call ELW with a strike of ₩60,000 (at the money) has a conversion ratio of 10, trades at ₩200, and carries a gearing of 15. Parity here is (60,000 ÷ 60,000) × 100 = 100% — exactly at the money. If the underlying rises to ₩62,000 the next day, a roughly 3.3% move, applying the gearing of 15 naively suggests the ELW could move close to 50% (3.3% × 15). In practice it won't move exactly that much, since gearing itself shifts as the underlying rises and time decay eats into the price simultaneously — but the swing relative to the invested capital is dramatically larger than the underlying's own move. Flip it around: if the stock stays below ₩60,000 all the way to maturity, this call ELW expires below 100% parity, and the entire investment is gone.

## Takeaway

- An ELW is a call or put right that a brokerage manufactures and lists — conceptually identical to an option, but settlement depends on the issuing brokerage's own credit, not a clearinghouse guarantee.
- Conversion ratio determines what fraction of the underlying's right one ELW share represents; parity shows whether it's currently in the money or out of the money.
- Gearing (leverage) measures how many percent the ELW moves for every 1% move in the underlying, which is why its daily swings look so much larger than the underlying stock's own.
- If an ELW stays out of the money through maturity, the entire investment is lost — and unlike a stock, there's no time left to recover, since the clock runs out on a fixed date.
- The issuing brokerage acts as the liquidity provider, quoting both sides of the market, which means the price you trade at is heavily shaped by the issuer's own model, not just supply and demand among investors.
- Because gearing and issuer credit risk stack together, first-time traders must clear a minimum deposit and complete investor education before they can trade.

## FAQ

### Which is safer, an ELW or a listed option?
Structurally, a listed option carries lower credit risk because a clearinghouse guarantees settlement. That said, both products share the same underlying risk of losing the entire investment if the position expires out of the money with high leverage attached — "relatively safer" doesn't mean "safe."

### Does an ELW settle automatically at maturity, or do I have to exercise it myself?
If it's in the money at maturity, exercise happens automatically — no action is required — and the payout is made entirely in cash. Korean ELWs never involve physical delivery of the underlying shares; settlement is paid two trading days after maturity (T+2).

### Why does Korea's ELW market have such a large retail investor footprint?
Small position sizes can generate large leveraged exposure, and the sheer variety of individual-stock ELWs makes the entry barrier feel low. That accessibility doesn't mean the product is low-risk, though — the same ease of entry is a big part of why so many retail losses tied to misunderstanding gearing and time decay have been documented over the years.

### Samsung Electronics also has listed stock options — how is that different from an ELW?
The Korea Exchange runs listed stock options on a limited set of large-cap names, including Samsung Electronics and LG Energy Solution. The concept is the same as an ELW, but a listed stock option is opened in standardized terms by the exchange with clearinghouse-backed settlement, while an ELW's strike, maturity, and conversion ratio are all set by the issuing brokerage — giving it far more variety and easier small-size entry, at the cost of leaving credit risk with the issuer. Since listed stock options only cover a handful of blue chips, ELWs' much wider range of underlying names and contract terms is the practical difference most traders notice.

> ⚠️ This article is for informational and educational purposes only and is not a recommendation to trade any specific product. ELWs are high-risk derivative securities that can result in a total loss of principal — always review the issuer's prospectus and risk disclosure before trading.
