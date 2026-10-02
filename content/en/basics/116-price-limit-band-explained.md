---
slug: price-limit-band-explained
title: "Korea's Daily Price Limit Explained: Why Stocks Can't Move More Than 30% a Day"
description: "How Korea's ±30% daily price limit works, why two straight limit-up days isn't a 60% gain, why trading doesn't actually halt at the limit, and how it compares abroad."
order: 116
updated: 2026-10-02
keywords: ["Korea stock price limit", "limit up limit down Korea 30%", "what is daily price limit stock", "KOSPI KOSDAQ price band", "Korea IPO first day price limit", "circuit breaker vs price limit difference"]
seo_audited: "2026-10-02"
---

## Two Straight Limit-Up Days Isn't a 60% Gain

When a stock hits its daily upper limit two days in a row, the easy mental math is "30% plus 30%, so it's up 60%." Run the actual numbers and that's wrong. A stock priced at 10,000 won that hits its limit (+30%) closes at 13,000 won. The next day, another limit-up adds 30% of 13,000 won — 3,900 won — bringing it to 16,900 won. That's a 69% gain from the original price, not 60%. Run the same math downward and two straight limit-down days (-30% each) produce a 51% loss, not 60%. Because each day's move is compounded off the previous day's closing price rather than the original price, gains snowball faster than simple addition would suggest, while losses shrink more slowly. That one arithmetic quirk is a useful entry point into a mechanism with real logic behind it. Where a [circuit breaker or VI](/en/basics/circuit-breaker-vi-sidecar-explained/) works by halting trading outright, Korea's daily price limit operates on a completely different layer: it never stops trading at all — it just fences in how far a price is allowed to travel in a single day.

## What the Price Limit Actually Is: A ±30% Wall Around Yesterday's Close

On both the KOSPI and KOSDAQ markets, every ordinary stock is confined to a band running from 30% below to 30% above its previous closing price (the "base price") during a single trading day. The price 30% above base is the limit-up price; 30% below is limit-down. Anything in between trades freely. ETFs, ETNs, and depositary receipts are held to the exact same ±30% band as ordinary shares. Derivatives like ELWs (equity-linked warrants) and listed options are the notable exception — they carry no price limit at all, because their entire structure is built to amplify the underlying asset's move several times over, so large swings in a short window are the expected, normal behavior of the product rather than something to be capped.

## Why Trading Doesn't Actually Stop There

The single most common misunderstanding about the price limit is the assumption that hitting it freezes the stock. It doesn't. Reaching the limit-up or limit-down price does not halt trading — the stock keeps trading right at that price. Being "stuck at the limit" just means buy orders are piled up with almost no sellers willing to match them; the moment someone places a sell order at that exact price, it executes immediately. The same logic runs in reverse at the limit-down price. This is the key way the price limit differs from [circuit breakers, VI, and the sidecar](/en/basics/circuit-breaker-vi-sidecar-explained/): VI freezes a stock into a 2-minute batch auction, and a full circuit breaker stops the entire market outright, but the price limit never needs a "halt" step in the first place — it's simply built so that a price outside the band can't exist to begin with. A circuit breaker is like pulling a speeding car over; the price limit is more like a speed-limit sign bolted permanently onto the road itself.

Picture the order book directly. Say Company B, trading around a 10,000-won base price, gets hit with a wave of buying on good news and climbs to its 13,000-won limit-up price. At that price, 500,000 shares of buy orders are stacked up, with almost no matching sell orders. If a shareholder looking to take profit then places a sell order for 1,000 shares at 13,000 won, it fills instantly against whichever buy order has been waiting longest. "Stuck at the limit" doesn't describe a frozen price — it describes one-sided order flow slowing down how fast fills actually happen.

## The Compounding Math Behind Consecutive Limit Days

The question that comes up constantly — "if a stock hits limit-up n days running, what's the total gain?" — resolves to the formula (1.3)ⁿ − 1. Consecutive limit-down days follow 1 − (0.7)ⁿ.

| Consecutive days | Cumulative limit-up gain | Cumulative limit-down loss |
|---|---|---|
| 1 | +30% | -30% |
| 2 | +69% | -51% |
| 3 | +120% | -65.7% |
| 4 | +185.6% | -76.0% |

As the table shows, the same number of consecutive days produces a far larger cumulative move on the upside than on the downside. That's because every limit-up day adds 30% on top of an already-larger number, while every limit-down day subtracts 30% from an already-smaller one. Same percentage, different base each time — a textbook compounding trap. The next time a headline reads "three straight limit-up days, up 120%," this formula lets you verify the number on the spot. It also explains why, mathematically, no amount of consecutive limit-down days can ever wipe a stock out entirely: each day only removes 30% of whatever is left, so the price approaches zero without theoretically ever reaching it.

## Why Small-Caps Hit the Limit Far More Often

The price limit doesn't bite every stock equally. Large-caps with heavy trading volume and a wide float have deep enough standing order books that, for most news, counter-orders arrive and rebalance the price long before it travels the full 30%. Small-caps with a thin float are the opposite: a comparatively small burst of buying or selling is enough to tip the order book entirely to one side and push the stock straight to its limit. That's a big part of why small, thinly-traded names are the ones that repeatedly hit limit-up on thematic news. As covered in [the basics of risk management](/en/basics/risk-management-basics/), thinner liquidity makes a stock more prone to sharp price swings in general — the price limit caps how far that swing can go in a single day, but a stock that regularly reaches its 30% band is also flagging itself as a genuinely high-volatility name.

## From 6% to 30%: A Band That Only Ever Widened

The 30% band wasn't always the rule — it was widened in stages over several decades.

| Year | KOSPI | KOSDAQ |
|---|---|---|
| 1995–1996 | 6% → 8% | - |
| 1998 | 12% → 15% | 12% |
| 2005 | 15% | 15% |
| June 15, 2015 | 30% | 30% |

KOSPI started at 6% in 1995, widened to 8% in 1996, jumped to 12% amid the 1998 Asian financial crisis, then to 15% later that same year; KOSDAQ followed a similar path, and both markets landed on today's 30% on the same day, June 15, 2015. The direction of travel has been consistently one way, and the logic is straightforward: a narrower band offers more investor protection in the moment, but it also delays genuine price discovery by days at a time. When a single day's 15% cap couldn't absorb either good or bad news in one go, the result was the stock simply hitting the limit again the next day, and the day after — a pattern regulators came to see as worse than letting more information get priced in within a single session, which is why the band kept widening rather than shrinking.

## A Newly Listed Stock's First Day Works Differently

Since June 26, 2023, the price range for a stock's first trading day after an IPO has been rebuilt from scratch. Under the old rules, the opening reference price was set somewhere between 90% and 200% of the IPO offer price, and the ordinary ±30% band was then applied on top of that reference — which meant the stock could rise, at most, to 260% of the offer price on day one. Today there's no separate opening-reference step at all: the IPO offer price itself becomes the day's base price, and the trading range runs from 60% to 400% of that base. A stock offered at 10,000 won can trade anywhere between 6,000 and 40,000 won on its first day.

The goal behind that change sounds paradoxical at first — how does widening the range to 400% strengthen investor protection? Under the old system, the opening reference itself was capped at 200% of the offer price, so stocks routinely rode straight from that reference to a same-day limit-up, locking trading at 260% of the offer price before the market had any real chance to test whether that price reflected genuine value — and once buy orders piled up at the limit, more buying kept arriving without any such test. Letting the opening price form freely around the offer price, with headroom all the way to 400%, gives real supply and demand more room to meet within a single session and find a more realistic price, weakening the mechanical "lock at the limit, sell higher tomorrow" pattern that short-term speculators had been exploiting.

## How Other Markets Handle This: Japan's Halt-Based System, America's No-Limit Approach

A fixed daily price limit isn't a universal feature of stock markets. Japan sets a different limit band (値幅制限) for every stock depending on its price level, and when a stock hits that band, trading actually halts — switching into a special quote (特別気配) that waits until buy and sell interest comes back into balance, unlike Korea's continued trading at the limit. The US goes the opposite direction entirely: individual stocks carry no fixed upper or lower price limit at all. Instead, [circuit breakers](/en/basics/circuit-breaker-vi-sidecar-explained/) halt the entire market only when the S&P 500 falls 7%, 13%, or 20%, while at the single-stock level, a mechanism called LULD (Limit Up-Limit Down) — functionally similar to Korea's dynamic VI — briefly pauses trading in a stock that moves outside a defined band. Korea and Japan both draw a hard line directly on price; the US instead puts no wall on price itself but briefly pauses trading when a move gets too fast — two genuinely different design philosophies for the same underlying problem.

## Key Takeaways

- Korea's daily price limit confines every KOSPI and KOSDAQ stock to a band from 30% below to 30% above the previous close.
- Hitting the limit-up or limit-down price does not halt trading — unlike VI and circuit breakers, which do stop trading outright.
- Cumulative moves over n consecutive limit days follow (1.3)ⁿ − 1 on the upside and 1 − (0.7)ⁿ on the downside, and the upside always compounds to a larger number than the downside for the same number of days.
- The band widened in stages from 6% in 1995 to 30% in 2015.
- Since June 2023, newly listed stocks trade in a 60%–400% range of the IPO offer price on their first day.

## FAQ

### If a stock is stuck at limit-up, can I still sell it?
Yes, but your order may not fill. A limit-up stock has a huge backlog of buy orders and almost no sellers, so a sell order placed at the limit price can sit unfilled until the queue ahead of it clears — sometimes until the close. The reverse holds at limit-down: selling is easy, buying is hard.

### Are any stocks exempt from the price limit?
Derivatives like ELWs and listed options carry no price limit. Because their entire payoff structure is designed to amplify the underlying asset's move through leverage, large, fast price swings are simply normal behavior for those products, not something to be capped.

### Is there debate about widening or scrapping the price limit entirely?
Yes, on both sides. Some argue Korea should drop the fixed band altogether and rely on circuit breakers and LULD-style mechanisms the way the US does; others argue the current 30% should stay or even tighten for investor protection. So far, regulators have chosen to leave the general 30% framework alone and instead adjust specific situations — like the IPO first-day rules — on their own.

### Can VI or a circuit breaker trigger on the same day a stock hits its limit?
Yes, they're not mutually exclusive. As a stock races toward limit-up, its price swing relative to the last trade can cross the threshold for dynamic VI (roughly 3–6%) well before it reaches the 30% band, triggering a 2-minute batch auction first. Once that auction sets a new price, the stock can keep climbing and still end up at limit-up. VI is a brief pause along the road to the limit; the price limit is the wall at the end of that road.

> ⚠️ This article is for educational purposes only and does not constitute investment advice for any specific stock or point in time. The rules and figures described here follow current Korea Exchange regulations, which can change — verify the latest requirements through official exchange disclosures.
