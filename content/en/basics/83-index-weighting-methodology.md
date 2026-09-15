---
slug: index-weighting-methodology
title: "Index Weighting Methods Explained — Why the Dow, S&P 500, and Equal-Weight Indexes Move Differently"
description: "The S&P 500 is cap-weighted, the Dow is price-weighted, and equal-weight funds like RSP use yet another rule. Here's why the same market can produce three different index returns on the same day."
order: 83
updated: 2026-09-15
keywords: ["how are stock indexes calculated", "Dow Jones vs S&P 500 difference", "price weighted vs market cap weighted index", "what is equal weight index", "Nasdaq 100 weighting rule", "Dow Jones divisor explained", "S&P 500 float adjusted market cap"]
seo_audited: "2026-09-15"
---

## Same Market, Different Numbers

It's a familiar headline pattern: "the Dow rose 0.8% while the S&P 500 gained 1.5%" — same trading day, same US market, different results. The cause isn't that individual stocks behaved differently depending on which index you're reading about. It's that **the two indexes are built with different math**. An index compresses the prices of hundreds or thousands of stocks into a single number, and the rule that decides "how much weight does each stock get" varies from index to index. That rule is called the weighting methodology, and it falls into three main types: market-cap weighting, price weighting, and equal weighting. [What Is Market Capitalization](/en/basics/market-capitalization/) covered how to calculate one company's market cap; this lesson covers the three different ways indexes turn that number — and others — into a stock's share of influence over the whole index.

## Market-Cap Weighting: Bigger Companies Move the Index More

This is the most common approach. The KOSPI, KOSPI 200, S&P 500, and Nasdaq Composite all use it. The mechanics are straightforward: add up the market capitalization (share price × shares outstanding) of every constituent, then compare that total to the same total at a fixed base date. The larger a company's market cap, the more its price move shifts the whole index. If the largest company in an index rises 5%, it pulls the index up far more than a company with one-hundredth its market cap rising the same 5%.

In practice, most cap-weighted indexes don't use raw shares outstanding — they use **free float**: shares actually available to trade, excluding founder or controlling-shareholder stakes, treasury shares, and government holdings that rarely change hands. Indexes with heavy ETF tracking, like the S&P 500 or KOSPI 200, apply this float adjustment strictly, because if untradeable shares were counted toward a stock's index weight, a fund trying to replicate that weight wouldn't be able to actually buy enough shares to match it.

## Price Weighting: A Higher Share Price Moves the Index More

The Dow Jones Industrial Average is the textbook example. Regardless of company size, the Dow simply adds up the **share prices** of its 30 components and divides by a number called the divisor. Here, weight is determined by dollars-per-share, not total company value. A $500 stock moving 5% swings the Dow far more than a $50 stock moving the same 5% — even if the cheaper stock's issuer is ten times larger by market cap. This produces real mismatches: a component with a modest share price but a massive market cap can carry less influence over the Dow than a component with a high share price but a much smaller company behind it.

The key mechanism here is the **divisor**. Simply summing 30 prices and dividing by 30 would work only until the first stock split or index reshuffle. When a component splits 2-for-1, its price is cut in half even though the company's value hasn't changed — so index administrators lower the divisor by a matching amount to keep the index level continuous across the split. A century of these adjustments has pushed the Dow's divisor far below 1, nowhere near the original count of 30 components. Price weighting survives mainly because of its 1896 origins and the Dow's brand recognition; almost no index designed today uses it, precisely because letting an arbitrary share price — rather than company size — decide index influence is a structural weakness for something meant to represent "the market."

## Equal Weighting: Every Stock Gets the Same Vote

This method ignores both market cap and share price and assigns every constituent the **exact same weight**. The best-known example is the equal-weight version of the S&P 500, tracked by funds like Invesco's RSP. In the standard cap-weighted S&P 500, a handful of mega-cap technology names can account for a large share of the index. In the equal-weight version, all 500 stocks each get roughly 1/500 of the weight. That means small- and mid-cap movements matter proportionally far more to the equal-weight index's return, and the index is structurally less exposed to a rally or selloff concentrated in a few giant names.

Equal weighting isn't free, though. A cap-weighted index self-adjusts — a stock that rises automatically gets a bigger weight, one that falls automatically gets smaller, with no action required. An equal-weight index drifts out of balance every time prices move, so it needs periodic rebalancing (typically quarterly) that sells whatever has outperformed and buys whatever has lagged, just to reset every stock back to the same weight. That turnover means higher trading costs than a cap-weighted fund typically incurs.

## A Modified Version: Capping Concentration Within Cap Weighting

Pure cap weighting has its own failure mode: if a handful of giant companies in one sector grow fast enough, the whole index can end up moving almost entirely on their moves. Some indexes address this by keeping cap weighting as the base rule but adding a **cap on individual weights**. The Nasdaq-100 is the clearest example: no single stock's weight may exceed 24%, and if stocks weighted 4.5% or more collectively exceed 48% of the index, a special rebalance brings that combined weight down to 40%. This limits — without eliminating — how dependent the index becomes on its largest names during periods when a few stocks are growing much faster than the rest. The tradeoff is that forcibly trimming a capped stock's weight and redistributing it elsewhere creates rebalancing trades that a pure cap-weighted index never needs.

## Comparing the Three

| Method | What sets the weight | Example index | Trait |
|---|---|---|---|
| Market-cap weighted | Free-float market cap | KOSPI, S&P 500, Nasdaq Composite | Tilts toward mega-caps, needs little rebalancing |
| Price weighted | Price per share | Dow Jones Industrial Average | Divisor-adjusted, overweights high-priced stocks |
| Equal weighted | Equal split across constituents | S&P 500 Equal Weight (RSP, etc.) | More small-cap exposure, regular rebalancing |

## Worked Example

Imagine a three-stock index. Stock A has a $900B market cap and trades at $90/share. Stock B has a $90B market cap and trades at $900/share. Stock C has a $10B market cap and trades at $10/share. Say Stock A rises 10% today.

- **Cap-weighted**: A is 90% of the combined $1T market cap, so its 10% gain lifts the index roughly 9%.
- **Price-weighted**: A's $90 price is only 9% of the combined share price total ($90+$900+$10=$1,000), so its 10% move contributes only about 0.9% to the index. If Stock B moved 10% instead, its price makes up 90% of the total, so it would swing the index far more.
- **Equal-weighted**: each stock carries a flat one-third weight, so A's 10% move contributes about 3.3%.

Same event, same percentage move, three different index outcomes. Stock B — small by market cap but expensive per share — dominates the price-weighted index in a way it never would under the other two methods, which is the clearest illustration of price weighting's distortion.

## Why This Matters for You

Whether "the US market was up today" feels true to you depends on which index the headline means. The Dow can rise while a handful of large tech names outside it drag the S&P 500 or Nasdaq lower — or the reverse: a handful of mega-caps can push a cap-weighted index sharply higher while most individual stocks are flat or down, which a cap-weighted headline number alone won't tell you but an equal-weight index would. This gap has shown up repeatedly in recent years, as concentration in a small number of large tech stocks widened the return difference between the cap-weighted and equal-weight versions of the S&P 500 — a pattern often cited as evidence that an index's headline gain is being carried by very few names. It matters for fund selection too: two ETFs both described as "tracking the S&P 500" can hold very different weights and carry different risk depending on whether the underlying index is cap-weighted or equal-weighted, so it's worth checking exactly which benchmark an ETF replicates, a point [What Is an ETF](/en/basics/etf-basics/) touched on from the replication side.

There's a diversification angle too. [Correlation and Diversification](/en/basics/correlation-and-diversification/) explained why adding more names to a portfolio doesn't automatically reduce risk as much as it seems to. A cap-weighted "500-stock index" can, in practice, have its volatility dominated by a handful of mega-caps, so the diversification it delivers can be thinner than the headline count suggests. An equal-weight index spreads that single-name risk out — at the cost of taking on more exposure to broad small- and mid-cap volatility instead.

## Takeaways

- Indexes turn the same market into different numbers depending on their weighting methodology — the rule for how much each stock counts.
- Market-cap weighting (KOSPI, S&P 500) favors bigger companies; price weighting (the Dow) favors higher-priced shares; equal weighting (RSP and similar) splits influence evenly across every constituent.
- Price-weighted indexes rely on a divisor, adjusted at every split or reshuffle, to keep the index level continuous — and that same mechanism means a high share price, not company size, drives influence.
- Equal-weight indexes reduce mega-cap concentration but require regular rebalancing, which costs more in turnover than cap-weighted indexes typically incur.
- When reading an index headline or comparing ETFs, it's worth checking which weighting method the underlying benchmark actually uses.

## FAQ

### Why does the Dow still use price weighting?
It was adopted in 1896 for practical simplicity and has stuck around for over a century largely because of the index's name recognition and long history. Almost no index designed today uses this method — most new indexes are cap-weighted or equal-weighted.

### Was the KOSPI always market-cap weighted?
No. Before 1983, the KOSPI used a price-average method similar to the Dow's. As the number of listed companies grew and a more accurate measure of overall market size became necessary, it switched to market-cap weighting with a base value of 100 set on January 4, 1983.

### Does an equal-weight ETF always outperform a cap-weighted one?
No. Cap-weighted indexes tend to outperform when a small number of large stocks drive the market, while equal-weight indexes tend to outperform when gains are broad-based across small- and mid-caps. Neither is consistently better — which one leads depends on the market environment.

> ⚠️ This lesson is for educational purposes only and is not investment advice regarding any specific index or ETF. The example figures are simplified hypothetical numbers used to illustrate the calculation methods.
