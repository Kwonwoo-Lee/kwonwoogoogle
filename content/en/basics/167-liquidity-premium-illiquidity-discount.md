---
slug: liquidity-premium-illiquidity-discount
title: "Liquidity Premium and the Illiquidity Discount: Why Thinly Traded Stocks Trade Structurally Cheaper"
description: "Why stocks, preferred shares, and unlisted equity with the same fundamentals trade cheaper when they're hard to buy and sell, explained through bid-ask spreads and price-impact costs."
order: 167
updated: 2026-10-27
keywords: ["liquidity premium meaning", "illiquidity discount explained", "why thin stocks trade cheap", "bid ask spread cost", "small cap discount reason", "preferred stock discount liquidity", "marketability discount private stock"]
seo_audited: 2026-10-27
---

## Same Company, Different Price

The lesson on [preferred vs. common stock](/en/basics/preferred-vs-common-stock/) covered why preferred shares of the same company tend to trade persistently below the common. Losing voting rights was one reason, but "lower liquidity" showed up as another — and that liquidity-driven discount isn't unique to preferred shares at all. Unlisted stock trading on [K-OTC](/en/basics/k-otc-market-explained/), shares in [closed-end funds](/en/basics/closed-end-fund-discount-explained/), and thinly traded small-cap names on KOSDAQ all show the same pattern: even holding fundamentals constant, the simple fact that an asset is hard to buy or sell systematically pulls its price down. This lesson covers the two mirror-image concepts behind that pattern — the **liquidity premium** and the **illiquidity discount** — what cost structure actually drives them, and where you'll actually run into this effect.

## One Phenomenon, Two Names — Return on One Side, Price on the Other

These two terms describe the same thing viewed from opposite angles. An investor buying an illiquid asset takes on the risk of not being able to sell it at a fair price whenever they want, and demands a higher expected return to compensate — that extra required return is the **liquidity premium**. But if future cash flows are held fixed, a higher required return (discount rate) mechanically produces a lower present value today. Looked at from the price side, the same fact reads as "this asset's price is already marked down because it's hard to trade" — that's the **illiquidity discount**. The liquidity premium expresses the demand in return terms; the illiquidity discount is what that demand looks like once it's baked into today's price. Same coin, two faces.

## Why Illiquidity Is an Actual Cost, Not Just a Vibe

This isn't a matter of sentiment — "unpopular stocks trade cheap." As covered in [market microstructure basics](/en/basics/market-microstructure-basics/), the gap between the bid and ask price is itself a real transaction cost paid the instant you trade immediately. Spreads on heavily traded large-cap stocks typically run around 0.1% of price; for thinly traded small caps or unlisted shares, spreads of several percent or more are common. Research cited for other markets has found large-cap spreads around 0.5% of price against small-cap spreads exceeding 6% — figures that vary a great deal by market and period, treat them as a rough rule of thumb rather than a fixed number, but the direction of the gap is consistent. The spread widens for a clear structural reason: whoever is quoting both sides of the market faces greater **adverse selection risk** on a thinly traded name (the person selling to you right now might know something you don't) and greater **inventory risk** (it will take longer to find a counterparty to offload the position to). Market makers and liquidity providers compensate for both risks by quoting a wider spread, and that cost ultimately lands on whoever trades the stock.

A second, related cost is **price impact**. A heavily traded stock can absorb a sell order of tens of thousands of shares without much effect on the order book; the same order size in a thin stock has to chew through several price levels to fill, dragging the average execution price down noticeably. Illiquid assets, in other words, carry a structurally larger risk of value destruction at exactly the moment you need to turn them into cash — and investors try to collect compensation for that risk upfront, through a lower everyday price. This logic was first formalized by Yakov Amihud and Haim Mendelson in 1986, and later distilled into a simple proxy for illiquidity — the ratio of a stock's price movement to its trading volume, now known as the Amihud illiquidity measure. Subsequent empirical work has repeatedly found that expected returns rise with illiquidity, though the exact size of that premium is an empirical tendency that's been estimated differently across time periods and markets, not a fixed constant.

## Size Effect or Liquidity Effect? Related, but Not the Same Thing

The lesson on [factor investing](/en/basics/factor-investing-explained/) mentioned that small-cap stocks have historically outperformed large caps over the long run — the so-called "size factor." The liquidity premium and the size effect overlap heavily and get conflated often, but they are conceptually distinct. The size factor is about market capitalization itself being small; the liquidity premium is about being hard to trade. In practice the two are deeply correlated, because small companies usually also have thin float and low trading volume. For decades, academics debated whether small caps really outperform because they're small, or simply because small companies also happen to be illiquid. Research controlling for market cap has repeatedly found that liquidity measures retain explanatory power on their own, which is why liquidity is now generally treated as an independent risk factor rather than a restatement of size. "Cheap because it's small" and "cheap because it's hard to trade" are two separate discounts that happen to stack on top of each other — not one phenomenon wearing two names.

## Putting Numbers to It — Selling the Same $1,000 Position

Picture two hypothetical stocks. Stock A is a heavily traded large-cap with a spread around 0.1%; Stock B is a thinly traded small-cap with a spread around 4%. Needing to urgently unwind a $1,000 position in each: Stock A loses roughly $1 to the spread alone, while Stock B starts out losing roughly $40 under the exact same circumstances. Add price impact on top and Stock B's real cost of selling widens further. None of this gap has anything to do with either company's earnings or growth prospects — it comes purely from how easy each stock is to sell right now. Investors who know this in advance will only buy Stock B at a price that's already discounted enough to absorb that future cost, and that's precisely the channel through which the illiquidity discount gets baked into the price.

## Where You'll Actually Run Into This Discount

The illiquidity discount isn't a textbook abstraction — it shows up across the market. The preferred-share discount mentioned earlier is one example. The [holding company discount](/en/basics/holding-company-discount/) — where a holding company trades below the sum of its subsidiary stakes — is partly attributed to the holding company's own shares trading thinly. Unlisted shares on [K-OTC](/en/basics/k-otc-market-explained/) trade far less frequently than exchange-listed peers and often carry a meaningful discount to comparable listed companies in the same industry for exactly that reason. [Closed-end fund discounts](/en/basics/closed-end-fund-discount-explained/) to net asset value are likewise partly explained by the fund's own shares being thinly traded, separate from whatever is happening inside the fund's portfolio. Valuation professionals formalize the exact same logic for unlisted companies and private equity stakes under the name **marketability discount** — a standard markdown applied when valuing unlisted shares for estate and gift tax purposes or in M&A pricing, precisely because a buyer can't exit the position quickly.

## It Behaves Differently in Calm Markets vs. Crisis

One important caveat: this discount isn't a fixed number. In ordinary conditions, liquid assets trade at a premium and illiquid ones at a discount in a fairly stable pattern. But when markets panic and everyone scrambles for cash at once, that gap tends to widen sharply, because finding a counterparty for an illiquid asset becomes far harder exactly when everyone wants to sell. In extreme fire-sale conditions, research has even found cases where normally liquid assets temporarily have to be dumped at distressed prices too, scrambling the usual discount structure. In short, the illiquidity discount behaves non-linearly — relatively stable most of the time, then suddenly larger when market-wide liquidity dries up.

That non-linearity shows up in its most visible form in situations like the one covered in [fund redemption suspensions](/en/basics/fund-redemption-suspension-liquidity-mismatch/). A fund holding illiquid private bonds or specialty assets can run fine for years as long as redemption requests trickle in one at a time. The moment fear spreads and many investors demand their money back simultaneously, the manager is forced into a rushed sale of those illiquid holdings — and that's exactly when the discount, which had quietly sat baked into the price the whole time, turns into an actual realized loss.

## What This Actually Means for an Investor

Knowing this concept is not a license to buy illiquid stocks and wait for the discount to close — that's not a trading signal. The discount reflects a real cost you'd face on exit, and narrowing it would require the stock's trading volume or market access to structurally improve, which isn't something an individual investor controls. The practical value of understanding this lies elsewhere. First, before treating a thinly traded stock, a preferred share, or an unlisted name as a bargain just because it's cheap, you should account for how much of that discount reflects a structural liquidity cost rather than weak fundamentals. Second, if the money involved might need to come out in a hurry, checking the stock's typical trading volume and order-book depth beforehand is a far more realistic way to estimate the real cost of exiting than looking at the quoted price alone. In the end, the liquidity premium isn't a signal to buy low and sell high — it's a literacy skill for reading what hidden cost is already built into the price tag you're looking at.

## Key Takeaways

- The liquidity premium is the extra expected return investors demand for holding a hard-to-trade asset; the illiquidity discount is the same demand expressed as today's lower price — two views of one phenomenon.
- The underlying cost has two parts: the bid-ask spread, an immediate transaction cost, and price impact, the cost of moving the market when selling in size. Work following Amihud and Mendelson formalized illiquidity as a measurable return driver.
- The discount recurs across preferred shares, holding companies, K-OTC unlisted stock, and closed-end funds, and is formalized for private valuations under the name "marketability discount."
- The discount is relatively stable in calm markets but widens sharply during systemic panics, so it's best treated as a cost to read off the price tag, not a trading signal.

## FAQ

### Does a large liquidity premium mean a stock is undervalued?
Not necessarily. The discounted price may already fully reflect the real transaction cost you'd pay to exit the position later. Unless trading volume or market access structurally improves, there's no guarantee that discount will ever close.

### Does low trading volume always mean a large liquidity premium?
Volume is a common proxy for liquidity, but not the only factor. A thinly traded stock backed by a designated market maker or liquidity provider can still keep a relatively tight spread, while even a moderately liquid stock can suffer a large price-impact cost if a big sell order hits at once.

### Who decides the marketability discount applied to unlisted shares?
In estate, gift-tax, and M&A valuations, appraisers and valuation professionals estimate the discount by referencing comparable listed companies' trading terms, trading frequency, and typical time to sale. There's no single fixed statutory rate — it's determined case by case through professional judgment.

> ⚠️ This lesson is for informational purposes only and is not investment advice. Investment decisions and their outcomes are the sole responsibility of the investor.
