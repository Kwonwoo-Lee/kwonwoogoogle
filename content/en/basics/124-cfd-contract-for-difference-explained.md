---
slug: cfd-contract-for-difference-explained
title: "What Is a CFD? How Contracts for Difference Let You Profit Without Owning the Stock"
description: "Why a CFD is a swap-like OTC derivative that settles only the price difference, how 2.5x leverage and margin calls work, and what South Korea's SG Securities scandal exposed."
order: 124
updated: 2026-10-06
keywords: ["what is a CFD", "contract for difference explained", "CFD leverage margin call", "CFD vs margin trading", "CFD vs short selling", "SG Securities CFD scandal", "why CFD banned in US"]
seo_audited: 2026-10-06
---

## Making Money Off a Stock You Never Owned

"Buying stock" usually means exactly what it sounds like: you pay money, you become a shareholder on the company's books, and if the price rises, you sell and pocket the difference. In April 2023, eight Korean-listed stocks hit their daily limit-down simultaneously, seemingly out of nowhere, in what became known as the SG Securities scandal. The investigation that followed revealed that the people behind it had made tens of billions of won in profit on those stocks without ever once appearing on a shareholder registry. The vehicle was a **CFD — Contract for Difference**. Understanding how someone can profit from a stock's price without ever owning a share, and how that position stayed invisible to the market for years, starts with understanding exactly what a CFD legally is. This lesson isn't about timing CFD entries or exits — that belongs in a trading-strategy course — it's about how the contract itself is structured.

## The Core Idea: You're Trading a Price Difference, Not a Stock

A CFD is, as the name says, a contract that settles only the difference in price. When an investor opens "a CFD on 100 shares of Company A" with a broker, no actual shares change hands between investor and broker. Instead, the broker buys and holds 100 real shares in its own name to hedge its exposure, while the investor holds nothing but an over-the-counter (OTC) derivative contract: a promise that cash will change hands between investor and broker equal to the difference between the opening price and the closing price.

Walking through actual numbers makes this concrete.

1. Company A trades at 100,000 won. An investor opens a CFD position on 100 shares — a notional 10 million won — but only deposits a 40% margin, or 4 million won. The remaining 6 million won is, in effect, financed by the broker.
2. The broker buys 100 real shares of Company A in its own name to hedge the client's exposure.
3. A few weeks later, the price rises to 130,000 won.
4. The investor closes the position. The difference — 30,000 won × 100 shares = 3 million won — is settled in cash. Against the original 4 million won margin, that's a 75% return.

This can look a lot like [margin trading](/en/basics/margin-trading-leverage/), but there's a critical difference. Margin trading borrows money to buy real shares, so the investor's name ends up on the shareholder registry. A CFD investor never owns the underlying stock at any point — legal title sits with the broker throughout, and all the investor ever holds is a contractual right and obligation to settle a price difference in cash.

## Why the Leverage Caps Out Around 2.5x

The main reason CFDs draw attention is leverage. Korean CFD providers typically set margin requirements around 40%, which works out to roughly 2.5x leverage (1 ÷ 0.4) on the investor's capital — a 40-million-won margin deposit can control price exposure on a 100-million-won position. That multiplier cuts both ways. In the example above, a 30% price gain turns into a 75% return on margin, but a 30% decline produces an equally amplified 75% loss. Once losses eat deeply enough into the margin, the broker issues a margin call demanding more collateral; if the investor can't meet it, the broker force-liquidates the real shares it's holding as a hedge, locking in the loss. That forced liquidation mechanism is exactly what triggered the SG Securities scandal: once CFD positions concentrated in the same handful of stocks started losing money, simultaneous margin calls set off a cascade of forced selling that fed on itself, dragging all eight stocks down to limit-down in the same session.

## The Cost of Just Holding a Position: Overnight Financing and Dividend Adjustments

CFDs aren't free to hold even when the trade is working. Because the investor only puts up 40% margin and the broker effectively finances the rest, that financed portion accrues an overnight financing charge every day the position stays open. It's small day to day, but for a position held for months, that carrying cost eats meaningfully into returns — the same mechanic behind the stock-borrowing fee that piles up on a prolonged [short sale](/en/basics/short-selling-explained/). Dividends work the same way, mirrored. If a stock underlying a long CFD position pays a dividend, the investor — despite not being an actual shareholder — receives a cash adjustment equal to that dividend. Hold a short CFD position instead, and the investor owes that same amount to the broker. Legal ownership of the shares stays with the broker throughout, but the economic effects that ownership produces — price moves and dividends alike — are passed through to the investor via the contract.

## How Other Markets Treat CFDs — and Why the US Banned Them Outright

Korea restricts CFDs behind a high "professional investor only" wall, but other markets treat them very differently. In the UK, the EU, and Australia — markets where retail CFD trading has existed for a long time — an ordinary retail investor can open a CFD account without much friction. What changed in 2018 was leverage: the European Securities and Markets Authority (ESMA) capped the maximum leverage retail brokers could offer on CFDs, and the UK's FCA and Australia's ASIC both followed with comparable rules. Individual-equity CFDs, for instance, are typically capped at 5x leverage for retail clients under these regimes — actually higher than Korea's roughly 2.5x. The US takes a fundamentally different approach. The SEC and CFTC effectively prohibit CFDs from being offered to retail investors at all, which means a US resident has no way to trade a CFD through a US-regulated broker. Where Europe manages the risk by capping leverage, the US manages it by banning the product outright — a telling contrast in just how risky regulators consider this instrument to be. Korea's "professional investor only" design sits between these two extremes: rather than capping leverage or banning the product, it screens out everyone except investors deemed able to absorb the risk.

## Not Open to Everyone: Korea's Professional Investor Requirement

Because of this risk profile, ordinary retail investors in Korea cannot trade CFDs directly — access requires registering as a "professional investor" under the Financial Consumer Protection Act. To qualify, an individual needs an average month-end balance of financial investment products above a set threshold (typically 50 million won) for at least one year within the past five, plus at least one of: income (100 million won individually, or 150 million won combined with a spouse), net assets excluding one's primary residence above 500 million won, or a relevant financial certification. After the SG Securities scandal, the registration process itself was tightened — video-call identity verification, for instance, became mandatory. The logic behind the barrier is straightforward: only let in investors who have the financial capacity and risk literacy to absorb losses amplified by roughly 2.5x leverage.

## Why Wealthy Investors Gravitated to CFDs: A Tax and Disclosure Gap

Leverage alone doesn't explain why CFDs grew the way they did in Korea. Gains on Korean-listed shares are generally exempt from capital gains tax — except for investors who cross a "major shareholder" threshold (roughly 1% ownership, or a set holding value), who do owe tax on those gains. Korea's income tax law taxes financial instruments on an enumerated basis — only products explicitly listed are taxable — and for a long time CFDs simply weren't on that list, making them a way to realize large stock gains without tripping the major-shareholder tax. The reasoning was that a CFD investor doesn't technically "hold" the underlying shares, so the ownership threshold that triggers the tax never gets crossed. On top of that, because legal title never leaves the broker, a CFD position of any size never counts as "ownership" for purposes of Korea's [5% beneficial ownership disclosure rule](/en/basics/beneficial-ownership-report-5-rule/) — a gap investors could exploit to accumulate large, invisible stakes. That's exactly what happened in the SG Securities case: the accounts used to manipulate stock prices built up substantial positions over several years without ever showing up on a public filing. Since the scandal, regulators have tightened CFD taxation and raised margin requirements, but the underlying gap — concentrated economic exposure with no corresponding ownership disclosure — remains the single most important thing to understand about how this instrument works.

## A Closer Look at the SG Securities Case

The 2023 incident, at its core, was a years-long scheme in which the head of an investment consulting firm used CFD accounts at multiple brokerages to artificially prop up the share prices of eight listed companies. From 2019 through April 2023, the group opened dozens of CFD accounts under the names of associates and investors, repeatedly buying the same stocks to push prices up gradually — a scheme prosecutors say generated illicit profits in the hundreds of billions of won. The scheme worked precisely because CFDs don't register as ownership: accumulating the same size stake in real shares would have triggered the 5% disclosure rule and surfaced the activity far earlier, but CFDs carried no such obligation. The whole structure unraveled on April 24, 2023, when selling in one of the stocks triggered a cascade of margin calls and forced liquidations that took all eight names to limit-down in a single session — and only then did the scale of the underlying CFD accounts become public. A key legal question that followed was whether buying pressure built purely through CFD orders, with no underlying share ownership changing hands, could still count as market manipulation. Korea's Supreme Court ruled that it could: a CFD order moves the market price just as a real purchase does, so it falls within the scope of market manipulation law. The ruling closed off the defense that "there's no ownership, so there's no manipulation."

## How CFDs Compare to Similar-Looking Trades

| | Buying real shares | Margin trading | CFD |
|---|---|---|---|
| Legal ownership | Investor | Investor | Broker |
| On shareholder registry | Yes | Yes | No |
| Subject to 5% disclosure rule | Yes | Yes | No (the gap) |
| Who can access it | Anyone | Anyone (some credit restrictions) | Professional investors only (Korea) |
| Typical max leverage | 1x | ~2–2.5x | ~2.5x (Korea); up to 5x (EU/UK/Australia) |

CFDs are often confused with [options](/en/basics/options-as-insurance/) and [index futures](/en/basics/stock-index-futures-basis-explained/). All three are derivatives that give price exposure without the underlying asset, but the mechanics diverge sharply. An option caps losses at the premium paid. A futures contract is standardized and traded on an exchange, so prices and open positions are publicly visible. A CFD is neither: it's a bilateral OTC contract between broker and investor with no standardized terms, no floor on losses, and — because it never touches an exchange — no public visibility into the position at all.

## Key Takeaways

- A CFD doesn't involve buying or selling real shares — it's an OTC derivative contract that settles the cash difference between the entry and exit price.
- Legal ownership stays with the broker and the investor holds only a contractual claim, which is why roughly 2.5x leverage amplifies gains and losses equally and can trigger forced liquidation via margin call.
- In Korea, only investors who meet specific financial asset, income, or net-worth thresholds can register as "professional investors" and trade CFDs.
- For years, CFDs offered a way around both Korea's major-shareholder capital gains tax and its 5% ownership disclosure rule — a gap that enabled the large, undisclosed stock accumulation and manipulation behind the 2023 SG Securities scandal.

## FAQ

### Can you bet on a stock falling using a CFD?
Yes. Opening a short CFD position creates a payoff similar to [short selling](/en/basics/short-selling-explained/) — profiting if the price falls. The difference is that short selling involves actually borrowing and selling real shares, while a short CFD never involves borrowing or owning anything; the same economic effect is produced entirely through the derivative contract.

### Can an ordinary retail investor access CFDs at all in Korea?
Direct trading requires registering as a professional investor first. Even without direct access, understanding the leverage, margin-call mechanics, and disclosure gap covered here is useful background for making sense of CFD-related stories that show up in the news.

### How did Korea's CFD rules change after the SG Securities scandal?
Video-call identity verification became mandatory for professional investor registration, and CFD-related taxation was tightened. The specific margin requirements, tax rates, and eligibility thresholds can continue to change as regulators issue further rules, so check current broker disclosures before relying on any specific figure.

> ⚠️ This article is for educational purposes only and is not investment advice. CFDs are high-risk OTC derivatives where leverage can substantially magnify losses, and related tax and regulatory rules can change. Investment decisions and their consequences are the investor's own responsibility.
