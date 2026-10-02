---
slug: calendar-spread-options
title: "Calendar Spread Options Strategy: Trading the IV Term Structure Around Earnings"
description: "How selling a near-term option and buying a longer-dated one at the same strike turns theta and volatility term-structure gaps into profit, with a step-by-step earnings setup."
order: 71
updated: 2026-10-02
keywords: ["calendar spread strategy", "what is a calendar spread", "options calendar spread explained", "earnings calendar spread", "time spread options", "double calendar spread", "front month back month options", "how to trade calendar spreads"]
seo_audited: 2026-10-02
---

## What a Calendar Spread Is: Trading the Same Strike Across Two Expirations

A **calendar spread** (also called a time spread) combines two options on the same stock, at the same strike, and of the same type — both calls or both puts — that differ only in expiration. You **sell the near-term contract (the front month)** and **buy the longer-dated contract (the back month)**. Since the back-month option almost always costs more than the front-month one, the position opens for a **net debit**, and that debit is also the maximum you can lose.

At first glance it can look like a wash — why sell and buy an option at the same strike? The answer is that the two legs lose value at very different speeds as time passes. Lesson 38 on [IV crush](/en/strategies/iv-crush-earnings-options/) covered how implied volatility collapses at a single moment — the earnings print. A calendar spread goes a step further: it's built to profit from the broader fact that options with different expirations decay at different rates, with or without an earnings catalyst.

## Engine One: Theta Decay — the Front Month Burns Faster Than the Back Month

An option's time value doesn't erode at a constant rate — it decays slowly at first and then accelerates sharply as expiration approaches. Theta (the dollar amount an option loses per day, all else equal) is small for an option with 30 days left and much larger for one with just 7 days left.

A calendar spread is built directly on that asymmetry. The short front-month option you sold bleeds value quickly day to day; the long back-month option you bought bleeds much more slowly. As long as the stock stays roughly near the strike, the front month's faster decay outpaces the back month's slower decay, and the net value of the spread rises over time. This is the core engine that makes a calendar spread work even with no earnings report or other catalyst anywhere nearby.

## Engine Two: Vega Skew — How an Earnings Report Distorts the Volatility Term Structure

Add an earnings report to the mix and a second engine kicks in. Under normal conditions, implied volatility (IV) across different expirations of the same stock sits at roughly similar levels, forming a gently sloped term structure. But when an earnings report falls inside — or right at the edge of — the front month's life, the market prices "this stock could move a lot on the print" almost entirely into the front-month contract, pushing its IV noticeably above the back month's. This is called an **inverted (or distorted) volatility term structure**.

After the report, the IV crush covered in Lesson 38 hits the front month hardest. Because the event itself is now fully resolved within the front month's remaining life, front-month IV snaps back down to a normal level fast, while the back month — still with weeks to go before its own next catalyst — gives up much less of its IV. The short leg loses value from both theta and vega at once, while the long leg holds up comparatively well, and both effects stack in the same direction, working in the calendar-spread seller's favor.

<figure class="diagram">
  <img src="/static/img/charts/en/calendar-spread-options.svg" alt="Diagram showing front-month implied volatility spiking above back-month IV before an earnings report, creating an inverted term structure that flattens back to normal right after the print, paired below with the tent-shaped payoff curve of a calendar spread against the stock price at front-month expiration" loading="lazy">
  <figcaption>Top: front-month IV spikes above back-month IV heading into earnings, inverting the term structure, then collapses back to a normal slope right after the report. Bottom: the tent-shaped payoff of a calendar spread at front-month expiration — maximum profit near the strike, shrinking as price moves away in either direction.</figcaption>
</figure>

## Plain Calendar Spread vs. Earnings Calendar Spread

Which engine you're relying on changes how you should structure the trade. Splitting the two use cases apart makes the setup choices much clearer.

| | Plain (non-event) calendar spread | Earnings calendar spread |
|---|---|---|
| Primary profit driver | Theta decay gap (front month burns faster) | Theta gap plus vega gap (inverted term structure unwinding) |
| Expiration choice | Front month 2-5 weeks out, back month another 4-8 weeks beyond that | Front month expiring within 2-3 days after the report, back month 1-2 weeks further out |
| Core assumption | Stock will trade sideways near the strike | Front-month IV is priced "irrationally" high relative to the back month |
| Holding period | Weeks, harvesting theta gradually | A few days, concentrated right around the print |
| Main risk | Slow exposure to the stock drifting away from the strike | A sharp earnings-day gap blowing price well past the strike |

## Worked Example 1: Plain Calendar Spread — Harvesting Theta in a Sideways Market

Say a $100 stock is trading in a range with no strong directional bias. You build a calendar spread with the $100 call.

- Sell the 30-day $100 call: collect $2.00 premium
- Buy the 60-day $100 call: pay $3.50 premium
- Net debit (maximum loss): $1.50 ($150 per contract, at a 100 multiplier)

If, 30 days later at front-month expiration, the stock is still sitting near $100 (say, between $99 and $101), the front-month call expires worthless or close to it. The back-month call, still carrying roughly 30 days of time value, commonly holds a value in the $2.50-$3.00 range if IV hasn't shifted much. Closing the position at that point nets whatever the back-month leg sells for, minus the original $150 paid — a profit. If the stock instead drifts well away from $100, to $85 or $115, both legs move away from the strike together and the spread's value typically shrinks, risking a partial or total loss of the $150 paid.

## Worked Example 2: Earnings Calendar Spread — Trading the Term-Structure Inversion

Now say the same $100 stock has an earnings report in 3 days.

- Sell the front-month $100 call (expiring 2 days after the report): IV at 70%, collect $4.00 premium
- Buy the back-month $100 call (2 weeks further out than the front month): IV at 45%, pay $5.20 premium
- Net debit: $1.20 ($120)

That 70% vs. 45% IV gap exists because the market is pricing earnings uncertainty almost entirely into the front-month contract. Say the stock reports and barely moves, closing around $101. Front-month IV typically snaps back to a normal level near 30%, while back-month IV eases only slightly, say from 45% to 40%. The front-month option loses value sharply from both theta and vega and might fall to around $1, while the back-month option — with less IV lost and far more time remaining — commonly holds near $4. The spread's value has grown to roughly $3, a solid gain against the $120 paid.

The picture changes if the stock instead gaps to $112 on the report. Both legs now sit deep in the money, where intrinsic value dominates over time value, and the calendar spread's characteristic "width compression" effect can actually shrink the position's value below the $120 originally paid. The takeaway is important: an earnings calendar spread is a bet on IV collapsing, but it's also an implicit bet that the stock stays reasonably close to the strike — it isn't purely a volatility trade.

## Calendar Spread vs. Iron Condor: Both Bet on a Range, But Shaped Differently

Calendar spreads get compared often to the [iron condor](/en/strategies/iron-condor-credit-spread/) from Lesson 58. Both are range-bound trades rather than directional ones, but their payoff shapes and risk profiles differ in important ways.

| | Calendar spread | Iron condor |
|---|---|---|
| Payoff shape | "Tent" — maximum profit right at the strike | "Box" — flat maximum profit across a wide range |
| Maximum loss | Limited to the net debit paid | Spread width minus premium collected |
| Position type | Opens for a net debit | Opens for a net credit |
| Volatility bet | Bets on the **gap** between front- and back-month IV (term structure) | Bets on overall IV being **absolutely** rich relative to the stock's actual historical move |
| Width of the profit zone | Relatively narrow, clustered near the strike | Can be designed wider by spacing the strikes further apart |

Neither structure is simply "better." An iron condor profits across a wider band but carries its own tail-risk exposure; a calendar spread caps the loss strictly at the premium paid, but its profit zone is narrower and shrinks quickly once the stock moves meaningfully away from the strike.

## Double Calendar Spread: Widening the Profit Zone

If a single calendar spread's tent-shaped profit zone feels too narrow, a **double calendar spread** is one way to widen it — running a call calendar at a strike slightly above the current price and a put calendar at a strike slightly below it, simultaneously. This extends the zone of profitability across the range between the two strikes. The tradeoff is a larger upfront net debit, since you're funding two spreads instead of one, and four option legs to manage instead of two, which adds commission cost and execution slippage on both sides of the trade.

## Limitations and Pitfalls

- **Pin risk and early assignment.** If the front-month option lands exactly at the strike at expiration, assignment becomes uncertain, and American-style deep in-the-money calls carry early-assignment risk right before an ex-dividend date. Getting assigned unexpectedly leaves you holding stock alongside a now-unhedged back-month leg.
- **Gap risk.** An earnings calendar spread needs two things to align for maximum profit: IV collapsing as expected, and the stock staying reasonably near the strike. A large earnings-day gap can erode or reverse the profit even if IV behaves exactly as predicted, simply because of the tent-shaped payoff.
- **Back-month IV can fall too.** The assumption that "only the front month crushes while the back month holds steady" doesn't always hold. In a broader volatility regime shift — a Fed decision, a market-wide risk-off move — back-month IV can drop along with the front month, narrowing the gap you were counting on.
- **Liquidity and the bid-ask spread.** Both legs need to fill together, and on a thinly traded name the combined bid-ask spread on the front and back legs can push your actual fill price meaningfully away from the theoretical value.
- **Margin rules vary by broker.** As a debit spread, margin treatment is generally simpler than an iron condor's, but the exact requirement and how early assignment gets handled differ by broker — worth confirming before putting the trade on.

## FAQ

### How is a calendar spread different from a diagonal spread?
A calendar spread uses the **same strike** for both the front- and back-month legs. A diagonal spread uses **different strikes** across the two expirations as well as different dates, which layers in a mild directional view — for instance, setting the back-month strike higher than the front-month strike if you have a modest bullish lean.

### What happens when the front-month option expires first?
Once the front-month leg expires worthless (or gets assigned), only the back-month leg remains. From there you can hold the back month outright, sell it to close the position, or sell a fresh front-month option against it to "roll" the calendar structure forward. That third option — rolling repeatedly to keep harvesting theta — is a common way traders run this strategy over a longer stretch.

### Is a calendar spread a good strategy for beginners?
It's a two-legged position with more moving parts to track than a simple long call or put — theta, vega, term structure, and assignment risk all interact. Getting comfortable with more basic strategies like iron condors or covered calls first is the generally recommended path before taking this one on.

## Summary

- A calendar spread sells a near-term option and buys a longer-dated one at the same strike, converting the gap in how fast time value and implied volatility decay into profit.
- A plain calendar spread relies on theta decay alone; an earnings calendar spread adds a second engine — the term-structure inversion an earnings report creates between front- and back-month IV.
- Its payoff is a "tent" peaking right at the strike, a different shape from the iron condor's wide, flat profit zone.
- Maximum loss is capped at the net debit paid, but realizing a profit needs two things to hold at once: IV collapsing as expected, and the stock staying near the strike.
- Pin risk, early assignment, the possibility that back-month IV falls too, and thin liquidity are structural limitations worth checking before putting the trade on.
