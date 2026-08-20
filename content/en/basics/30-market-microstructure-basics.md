---
slug: market-microstructure-basics
title: "What Is a Market Maker? Order Books, Spreads, and Dark Pools Explained"
description: "How the order book's bid-ask queue turns into a trade, why market makers earn the spread but carry inventory risk, and how dark pools affect price discovery."
order: 30
updated: 2026-08-20
keywords: ["what is a market maker", "what is a dark pool", "how does an order book work", "bid ask spread explained", "market microstructure", "price discovery stock market", "liquidity provider ETF", "why is the bid ask spread wide"]
---

## The Moment You Click "Buy," Who Actually Takes the Other Side?

[How the Stock Market Works](/en/basics/how-the-stock-market-works/) covered the roles exchanges and brokers play, and [Order Types](/en/basics/order-types/) covered the difference between market and limit orders. What neither one answered is who, exactly, is on the other side of your trade the instant you click "buy." Some days a limit order fills within seconds; other days it just sits on the book, unfilled, for minutes. That difference comes down to **market microstructure** — the machinery that sits between an order being placed and an order actually being filled, where the order book, market makers, and increasingly dark pools all shape the price you actually get. This lesson covers how that machinery works, and why understanding it changes how you read an order book and a fill.

## The Order Book Is a Queue — Priority Goes by Price, Then by Time

An order book is a real-time list of every unfilled order for a stock, sorted by price. Sell orders sit on top as the **ask** (or offer), buy orders sit below as the **bid**, and the empty gap between the best ask and the best bid is the **spread**.

Matching follows one simple rule: **price priority, then time priority**. A buy order offering a higher price gets filled before one offering a lower price; at the same price, whichever order arrived first gets filled first. A market order sweeps through the book from the top down — for a buy, starting at the lowest available ask — consuming liquidity level by level until it's filled.

The size of the spread itself is a signal worth reading. A heavily traded large-cap stock typically has a razor-thin spread — sometimes just a single tick between the best bid and best ask. A thinly traded small-cap or an illiquid name can have a spread many times wider. A wide spread means buyers and sellers currently disagree sharply about the "right" price, and it also means a market order eats that gap immediately — you're down the width of the spread the instant your trade fills, before the stock has moved at all.

## What a Market Maker Actually Does — Earning the Spread, Carrying the Risk

An order book doesn't stay populated on its own. Someone has to keep posting both a bid and an ask, even during quiet stretches, so that other investors can trade whenever they want to. The participant that specializes in this job is a **market maker**.

The economics are simple: quote a bid slightly below where you think the "fair" price is and an ask slightly above it, and if both sides get hit, you pocket the spread as profit. Say a market maker posts a bid of $99.90 and an ask of $100.10 on a stock. One trader buys at $100.10, and shortly after, another trader sells at $99.90 — the market maker effectively bought at $99.90 and sold at $100.10, a $0.20 profit. Any single trade like that is tiny, but repeated tens of thousands of times a day, it adds up to real revenue.

The catch is that this isn't free money. Because a market maker is obligated to keep quoting both sides, it ends up holding unwanted inventory whenever the market moves hard in one direction. If bad news hits and everyone wants to sell, the market maker still has to keep buying — and can end up accumulating a falling stock it never wanted to own in the first place. This is called **inventory risk**. In practice, market makers manage it by widening their spreads when conditions get volatile — taking on more risk per trade in exchange for a bigger cushion per trade. If you've ever watched a spread suddenly blow out right after breaking news, that's inventory-risk management playing out in real time.

## Not Every Market Runs on Market Makers

It's worth noting that not every exchange is built the same way. Nasdaq-style markets historically ran on a dealer model, where designated market makers are structurally built into every stock's trading. Order-driven markets — like most of Europe's and much of Asia's exchanges — work differently: investor orders are matched directly against each other, with no designated market maker required for most listings. In practice, exchanges that lean order-driven still add liquidity-provider programs for thinly traded stocks and for products like ETFs, where keeping the market price tracking net asset value closely enough matters — so the underlying need for someone to keep quoting both sides shows up everywhere, even where the market's default design doesn't build it in from the start.

## Dark Pools: Trades That Never Touch the Public Order Book

Everything covered so far assumes a **lit market** — an order book where bids and asks are visible in real time. But a meaningful share of actual trading never touches that visible book at all. These off-exchange venues where trades are matched privately are called **dark pools**.

Dark pools exist because large institutional investors have a real problem to solve. Say a pension fund needs to sell several hundred thousand shares of a stock at once. Dropping that entire order onto the public order book would signal "a huge sell order just showed up" to every other market participant, who would race to sell first or yank their bids lower — leaving the pension fund to unload its position at a much worse price than it started with. A dark pool hides the existence of that large order until after it's filled, letting a big trade execute without moving the visible market against itself.

The execution price in a dark pool is typically pegged to a reference price from the lit market — often the midpoint between the public bid and ask — so a dark pool isn't generating an independent price of its own. It's borrowing the public market's price while concealing who's trading how much.

## Why Dark Pools Are Controversial: The Price Discovery Trade-Off

The central controversy around dark pools is their relationship to **price discovery** — the process by which a stock's price comes to reflect what the market collectively thinks a company is worth, driven by buy and sell orders meeting in the open. If a large share of total trading volume never touches the visible order book, then the volume and price action you actually see on a lit exchange represents only part of the real supply and demand in that stock.

In the U.S. market, estimates commonly cited put the share of total equity trading volume executed off-exchange — dark pools included — at somewhere close to half. That figure moves around depending on how and when it's measured, and it isn't a single fixed official statistic, so it should be read as a rough estimate rather than a hard number. But the direction is clear: what you see in a broker app's order book and tape isn't the complete picture of a stock's real trading activity. That tension is exactly why regulators keep revisiting disclosure rules for dark pool operators — requiring after-the-fact reporting of trades — trying to balance transparency against the legitimate need to execute large orders without moving the market.

## A Numbers Example: Two Stocks, Two Spreads

Here's what spread width actually costs, using two hypothetical stocks.

| | Stock A (large-cap, actively traded) | Stock B (small-cap, thinly traded) |
|---|---|---|
| Best bid | $49.95 | $9.80 |
| Best ask | $50.00 | $10.20 |
| Spread | $0.05 (~0.1%) | $0.40 (~4%) |
| Cost of an immediate market buy-then-sell | ~0.1% | ~4% |

Stock A's spread is small enough relative to its price that trading it at market carries almost no hidden cost. Stock B, by contrast, hands you a nearly 4% loss the instant you buy and sell at market. That gap isn't just about which stock happens to be popular — it's a structural consequence of how tightly a market maker or liquidity provider is quoting both sides of that particular stock, and how much volume normally trades in it.

## What Actually Changes Once You Understand This

Market microstructure isn't a trading signal. It's not "buy when the spread is tight" or "be wary when dark pool volume is high" as an entry or exit rule. What it does change is how accurately you read two things.

First, it explains why a market order on some stocks can move the fill price noticeably, while on others it barely registers. On a thinly traded name, that's the concrete reason a limit order — covered in [Order Types](/en/basics/order-types/) — is the far safer choice: the wider the spread, the more hidden cost you eat by skipping the limit price and trading at market.

Second, it builds the instinct that what you see on a public order book isn't the whole story. Knowing that a meaningful chunk of real trading can happen through dark pools and block trades — invisible to the retail order book — makes it harder to look at thin visible volume and conclude, incorrectly, that "there's no real demand" for a stock.

## Takeaway

- An order book matches buy and sell orders by price priority, then time priority; the gap between the best bid and best ask is the spread.
- Market makers earn the spread by continuously quoting both sides, but take on inventory risk whenever the market moves hard in one direction — which is why spreads widen during volatility.
- Not every market is built around designated market makers the way Nasdaq historically was; order-driven markets rely mostly on investor orders matching directly, with liquidity-provider programs filling the gap for thin stocks and products like ETFs.
- Dark pools let large orders execute without moving the visible market, borrowing their reference price from the lit exchange — but with a meaningful share of trading volume happening off the public book, the debate over their impact on price discovery is ongoing.
- The real value of understanding this isn't a trading signal — it's knowing why a limit order matters more on a wide-spread stock, and why a thin-looking order book doesn't necessarily mean thin real demand.

## FAQ

### Can retail investors trade directly on a dark pool?
Most dark pools are built for institutional block trading, so retail investors typically don't place orders into one directly through a broker app. That said, a retail order can still end up routed through a dark pool indirectly, depending on how a broker handles order execution.

### Should I avoid stocks with a wide bid-ask spread?
A wide spread by itself doesn't mean a company is bad — it's a common feature of small-caps and recent listings that simply trade less. What it does mean is that a limit order, rather than a market order, is the safer way to control the hidden cost that spread creates.

### Is a "market maker" the same thing as a "liquidity provider"?
Conceptually, they play the same role — continuously quoting both sides of the market to keep it liquid. But their institutional footing differs: a Nasdaq-style market maker is built into the market's basic structure, while liquidity-provider programs on order-driven exchanges are typically a targeted add-on for specific thinly traded stocks or products, run under separate exchange agreements.

> ⚠️ This article is for informational purposes only and is not investment advice. You are solely responsible for your own investment decisions.
