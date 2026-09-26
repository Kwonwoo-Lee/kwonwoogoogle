---
slug: circuit-breaker-vi-sidecar-explained
title: "Circuit Breakers Explained — How They Differ From VI and Sidecar Halts"
description: "How Korea's three market-wide trading halts — VI (volatility interruption), sidecar, and the 3-stage circuit breaker — work, what triggers each, and why they're layered the way they are."
order: 105
updated: 2026-09-26
keywords: ["what is a circuit breaker stock market", "circuit breaker trading halt explained", "sidecar trading halt Korea", "KOSPI circuit breaker levels", "volatility interruption VI explained", "static vs dynamic VI", "program trading halt Korea"]
seo_audited: "2026-09-26"
---

## Why the Market Keeps Stopping in 2026

On September 22, 2026, the KOSPI tripped a circuit breaker. It wasn't an isolated event. Through July alone, Korea's benchmark index had already triggered circuit breakers nine times in 2026, setting a record pace, while sidecar halts fired more than 20 times over six straight months — the first such streak since 2002 — putting the year on track to approach the 26 sidecar triggers recorded during the 2008 financial crisis. Add in stock-level volatility interruptions (VI), and the monthly trigger count has run well above 10,000, higher even than the 2020 pandemic peak. A big part of the story is structural: as a handful of mega-cap names like Samsung Electronics and SK Hynix have come to dominate more of the index's weight, order-flow swings in just those stocks now transmit into index-wide swings far more directly than before.

News coverage tends to lump "circuit breaker," "sidecar," and "VI triggered" together, but these are three distinct mechanisms that stop different things for different lengths of time. Once you can tell them apart, a headline saying trading "halted" stops being a vague alarm and becomes something you can actually parse — what exactly stopped, and why.

## Same Goal, Different Scope — What Each One Actually Freezes

All three exist to buy a cooling-off period when a price is moving too fast for the market to process rationally. What separates them is scope. VI pauses order matching for **one single stock**. A sidecar pauses **program trading orders** market-wide. A circuit breaker halts **all trading in every stock** at once. They aren't interchangeable alternatives — they're layered defenses, escalating from the narrowest impact to the broadest. A volatile day might see VI trigger repeatedly on a single name and nothing more; if the shock spreads into the futures market, a sidecar can kick in; and if the damage is severe enough to move the underlying index itself, a circuit breaker shuts the entire market down as the last line.

| Mechanism | What gets paused | Scope |
|---|---|---|
| VI (Volatility Interruption) | Order matching for one stock | Single stock |
| Sidecar | Program trading orders | Market-wide (futures-linked) |
| Circuit Breaker | All trading in every stock | Market-wide |

## VI — The Finest-Grained Safeguard, and the One That Fires Most Often

Introduced in September 2014, VI operates at the individual stock level: when a stock's price jumps too fast, trading in that one name switches to a 2-minute call auction. Instead of matching orders continuously in real time, the exchange collects every order that comes in during those two minutes and settles them all at a single clearing price — which prevents a price from being distorted just because the order book happened to be thin for a moment.

VI comes in two flavors. **Dynamic VI** triggers when a stock moves roughly 3–6% (the exact threshold varies by stock and session) from its last traded price in an instant, targeting a single large order that briefly warps the price. **Static VI** uses a wider band — typically a 10% move from the previous day's closing price — targeting the cumulative price change built up over the course of the day rather than any one moment. Think of dynamic VI as catching "the shock happening right now" and static VI as catching "how far today has drifted overall." There's no daily cap on how many times VI can fire, which is exactly why a single volatile stock can trip it repeatedly in one session — and why the 2026 figures cited above run into the tens of thousands per month.

## Sidecar — Stopping a Futures Shock From Spilling Into the Cash Market

Sidecar's formal name translates to something like "program trading order suspension system." Institutional and foreign investors run large arbitrage programs that exploit the price gap (the basis) between KOSPI 200 futures and the underlying cash-stock basket — the same basis mechanic covered in [Stock Index Futures & Basis Explained](/en/basics/stock-index-futures-basis-explained/). When futures prices move sharply, those programs can all fire in the same direction simultaneously, dumping or buying cash stocks in a way that amplifies the original shock. A sidecar exists to cut that transmission channel, briefly.

It triggers when KOSPI 200 futures move 5% or more (6% for KOSDAQ 150 futures) from the prior close and stay there for a full minute. Once triggered, program trading orders are suspended for five minutes. Crucially, only program orders are frozen — an individual investor placing a regular order through a brokerage app trades exactly as normal throughout that five-minute window. Sidecar can only fire once per day, and it can't trigger at all after 2:50 p.m., 40 minutes before the close — letting it fire right up to the closing bell would leave no time for the market to find a normal price again once the suspension lifted.

## Circuit Breaker — The Final, Market-Wide Stop, in Three Stages

The circuit breaker is the strongest of the three: it halts trading in every single stock market-wide when the index itself is falling hard. Korea introduced it in the aftermath of the 1997–98 Asian financial crisis, borrowing the name directly from the electrical circuit breaker that cuts power entirely when current surges past a safe limit. It escalates through three stages tied to how far the index has fallen.

| Stage | Trigger | Action |
|---|---|---|
| Level 1 | Index down 8%+ from prior close, sustained for 1 minute | All trading halted for 20 minutes, then resumes |
| Level 2 | Down 15%+, and at least 1 additional percentage point below the Level 1 trigger, sustained for 1 minute | All trading halted for 20 minutes, then resumes |
| Level 3 | Down 20%+, and at least 1 additional percentage point below the Level 2 trigger, sustained for 1 minute | Trading ends for the day, immediately |

Levels 1 and 2 pause the market for 20 minutes before letting it reopen; Level 3 simply ends the trading day on the spot. Like the sidecar, the circuit breaker can only fire once per stage per day (though Levels 1, 2, and 3 can each trigger once in sequence on the same brutal day), and it can only activate between 5 minutes after the open and 40 minutes before the close.

Here's a concrete walkthrough. Say the KOSPI opens at a prior close of 2,800 and sells off hard, falling to 2,576 — an 8% drop — and stays there for a full minute. Level 1 fires, and every stock halts for 20 minutes. Trading resumes, but the selling continues and the index slides to 2,380 (down 15%), holding there for another minute — Level 2 fires, and the market halts for another 20 minutes. If it keeps falling to 2,240 (down 20%) after that, Level 3 triggers and the exchange closes for the day right then, with no more trading until the next session.

## Why These Exist — Breaking the Feedback Loop, Not Predicting the Bottom

All three mechanisms target the same underlying problem: a falling price that triggers more selling, which pushes the price down further, in a self-reinforcing loop. A sharp index decline can trigger margin calls that force leveraged accounts into automatic liquidation, algorithmic orders with built-in stop-loss triggers can all fire sell orders in the same direction at once, and panicked retail selling can pile on top of both — pushing the decline far past anything justified by an actual change in underlying value. Even a brief trading halt forcibly breaks that automated selling chain and gives everyone a window to ask whether the drop is really being driven by meaningful new information or just a self-feeding panic. VI, sidecar, and the circuit breaker differ only in scale — they all rest on the same logic of buying a cooling-off period.

## How to Actually Read a Halt Headline

Here's the part that's easy to get backwards: a circuit breaker or VI trigger is not, by itself, a signal that a bottom is in or that a bounce is coming. These mechanisms make no judgment at all about why the price is falling. They fire identically whether the drop reflects a real, fundamental problem or just a temporary imbalance in order flow. A halt tells you the exchange has decided to slow trading down — nothing about the cause. In practice, some halted sessions keep falling once trading resumes, and others see bargain-hunting buyers step in during the cooling-off period and claw back part of the loss; both outcomes happen often enough that neither should be assumed. What actually matters when you see the headline isn't a buy-or-sell call in the moment — it's figuring out what's actually driving the move (earnings, rates, a geopolitical shock) before drawing any conclusion.

Trigger frequency itself, though, is a reasonable gauge of how anxious the broader market has gotten. Much like implied volatility priced into options — covered in [VIX & Implied Volatility Explained](/en/basics/vix-implied-volatility-explained/) — quantifies fear embedded in options prices, a stretch where sidecar and circuit-breaker triggers run well above a typical year, as 2026 has, is itself evidence that overall market volatility has shifted to a structurally higher level. That's still not a timing tool for calling the next move up or down — it's better read as a cue to dial up risk management, not to time an entry or exit.

## The US Version Is Built a Little Differently

US markets run a comparable three-level circuit breaker, but the design differs in a few ways worth knowing if you trade both markets. It triggers off the S&P 500 falling 7% (Level 1), 13% (Level 2), or 20% (Level 3) from the prior close. Levels 1 and 2 halt market-wide trading for 15 minutes before resuming, while Level 3 ends trading for the day immediately — a shorter pause than Korea's 20-minute halts at each of its first two stages. The US system also has no direct equivalent of Korea's sidecar — no separate, intermediate layer that selectively freezes only program trading orders while leaving everything else running. Korea's setup is a tighter three-tier stack (VI at the single-stock level, sidecar at the program-trading level, circuit breaker at the whole-market level), while the US relies on a two-layer approach: single-stock trading pauses (Limit Up-Limit Down, a different individual-stock mechanism) plus the market-wide circuit breaker.

## Key Takeaways

- VI freezes order matching for one stock, a sidecar freezes only program trading orders, and a circuit breaker freezes all trading market-wide — three different scopes, not three versions of the same thing.
- VI splits into dynamic (roughly 3–6% from the last trade) and static (10% from the prior close) triggers, with no daily limit on how many times it can fire.
- A sidecar fires when KOSPI 200 or KOSDAQ 150 futures move 5–6%+ and hold for a minute, freezing program orders for 5 minutes; it can only trigger once per day.
- A circuit breaker escalates through three stages at 8%, 15%, and 20% index declines — Levels 1 and 2 halt trading for 20 minutes each before resuming, Level 3 ends the trading day outright.
- None of these mechanisms judge why a price is falling, so treating a trigger itself as a buy or sell signal is a mistake — check the underlying cause first.

## FAQ

### Can I trade at all during the 2 minutes a VI is active?
Not exactly frozen, but not real-time either. During that window the stock switches to a call auction: orders keep coming in, but instead of matching instantly, they're all collected and settled at one single price once the two minutes end.

### If a circuit breaker triggers, does that mean I can't sell my shares that day?
Levels 1 and 2 resume trading after 20 minutes, so you can trade normally once the halt lifts. Only Level 3 ends the trading day outright — in that case you'd need to wait until the next session.

### Does a sidecar affect my own regular order?
No. A sidecar only suspends program trading orders from institutions and foreign investors. Orders placed the normal way through a brokerage app or platform execute exactly as they would on any other day.

### Can a circuit breaker and sidecar both trigger multiple times in one day?
Sidecar and each circuit breaker level can only fire once per day. But because the three circuit breaker levels are separate triggers, a severe enough sell-off can see Level 1 and Level 2 both fire in sequence within the same session. VI has no such daily cap, so a single volatile stock can trip it repeatedly.

> ⚠️ This article is for informational and educational purposes only and does not constitute investment advice for any specific stock or moment in time. The trigger thresholds and figures described reflect current Korea Exchange rules, which are subject to change — verify the latest requirements through official exchange disclosures.
