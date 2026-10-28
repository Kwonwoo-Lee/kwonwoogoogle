---
slug: call-auction-opening-closing-price
title: "What Is a Call Auction? How Korea's Opening and Closing Stock Prices Are Actually Set"
description: "Why orders don't fill instantly at the market open and close, and how a call auction converges on one clearing price through an indicative price and a randomized end time."
order: 168
updated: 2026-10-28
keywords: ["call auction stock market", "how opening price is determined", "how closing price is set", "indicative matching price", "random end auction", "single price auction korea", "KRX opening closing auction"]
seo_audited: 2026-10-28
---

## The Open and Close Aren't Just "the First and Last Trade"

The lesson on [how the stock market works](/en/basics/how-the-stock-market-works/) covered how the regular session matches orders — continuously, the instant they arrive, against whatever sits on the opposite side of the book. But the two prices everyone treats as the most important of the day, the open and the close, aren't produced that way at all. The "first trade" at 9:00 a.m. and the "last trade" at 3:30 p.m. come out of a completely different mechanism: a **call auction**, formally called single-price matching (단일가매매), and colloquially known in Korean as 동시호가 ("simultaneous quotes"). If you've ever wondered why your order sits unfilled for several minutes right after the market opens or right before it closes, this is the mechanism behind that pause.

## Continuous Matching vs. the Call Auction — Fill Instantly, or Pile Up First

In continuous matching, an order tries to fill the second it arrives. During a call auction window, by contrast, every order placed in that window **sits in the book without filling at all**. The Korea Exchange runs a call auction from 08:30 to 09:00 to determine the opening price, and again from 15:20 to 15:30 to determine the closing price — identical rules on both KOSPI and KOSDAQ. For that entire 30-minute or 10-minute stretch, no matter how many buy and sell orders investors submit, nothing executes. Instead, the exchange looks at the entire accumulated book of buy and sell orders and calculates the single price that would maximize the matched (executable) volume between them. At the exact close of the window, every order that qualifies fills simultaneously at that one price. Because every order placed during the window is treated, in effect, as having arrived at the same moment, Korean market participants call this period 동시호가 — literally, "simultaneous quotes."

## The Indicative Price Is a Running Estimate, Not a Confirmed Number

During the call auction window, the quote screen still shows a number where the price would normally be. This is the **indicative matching price** — a real-time estimate of "if the auction ended right now, this is the price it would clear at," calculated purely from the orders accumulated so far. It is not an actual trade. New orders keep arriving and existing ones keep getting canceled or amended right up until the window closes, so the indicative price can shift meaningfully throughout the window — especially in the opening auction, where the price implied early in the 08:30–09:00 window can look very different from the price implied just before 9:00 if overnight news or disclosures are still being digested. Treat this number as a snapshot of where buyers and sellers currently balance out, not as a locked-in price you can count on.

## Why the Overnight Gap Tends to Be Structurally Larger

Stocks often open with a visible gap from the prior close on days when U.S. markets moved sharply overnight or a major disclosure drops before the bell — and that gap being larger than a typical intraday move isn't a coincidence. It's a direct consequence of how the call auction compresses information. In continuous trading, new information gets absorbed gradually, one fill at a time, as the price nudges along. During the 08:30–09:00 window, by contrast, every order and every piece of overnight information accumulates without a single trade occurring, and all of it is released at once in a single price jump when the auction clears. Information that would normally be digested across dozens of small trades in continuous trading instead gets compressed into one discrete repricing — which is exactly why the gap between yesterday's close and today's open tends to run wider than almost any single intraday move, and why that gap itself gets watched as a read on the day's prevailing sentiment.

## How a Single Clearing Price Gets Chosen — A Numeric Example

The price a call auction settles on is whichever one maximizes matched volume between the buy and sell sides — commonly called the **equilibrium price**. Suppose the following orders accumulate during a call auction window for a hypothetical stock:

| Price | Cumulative buy volume willing to pay this price or more | Cumulative sell volume willing to accept this price or less | Volume that can actually fill (the smaller of the two) |
|---|---|---|---|
| $10.10 | 500 | 4,000 | 500 |
| $10.05 | 1,200 | 3,200 | 1,200 |
| $10.00 | 2,000 | 2,000 | 2,000 |
| $9.95 | 3,000 | 1,000 | 1,000 |
| $9.90 | 4,000 | 400 | 400 |

As price rises, cumulative buy demand shrinks while cumulative sell supply grows. At any given price, the volume that can actually execute is capped by whichever side is smaller — and in this table, $10.00 is where both sides match exactly at 2,000 shares, the highest fillable volume of any price level. At $9.95 or $10.05, one side runs short and less volume clears. So the exchange sets $10.00 as this auction's clearing price and fills every qualifying buy and sell order there at once. Real order books have far finer price increments and vastly more orders, but the underlying logic is identical: find the one price that produces the maximum matched volume.

## When Orders Tie at the Clearing Price, Who Gets Filled First?

In continuous trading, if multiple orders sit at the same price, the one submitted earlier fills first — strict time priority. Inside a call auction window, "who arrived first" doesn't carry the same weight, because every order submitted during that window is formally treated as one batch settled all at once, regardless of whether it technically arrived at 08:31 or 08:58. Among orders tied at the clearing price, price still governs first; beyond that, allocation follows the exchange's own detailed matching rules (which can include volume-proportional allocation), rather than continuous trading's simple "first in, first filled." The practical takeaway is that during a call auction, what price you quote matters far more than what minute you submitted it.

## The Random End — Closing the Window Without Letting Anyone Game the Last Second

If the call auction window cut off at exactly 9:00:00 or 15:30:00 sharp, it would create an obvious exploit: slam in a large order, or yank one out, in the final fraction of a second to nudge the clearing price in your favor. To prevent that, the exchange uses a **random end** mechanism. Once the scheduled close time arrives, the auction doesn't stop immediately — instead, the exact closing moment is chosen at random within a short window just after the scheduled time. Because no one can know the precise second it will actually end, the payoff from trying to manipulate the very last moment collapses. The same randomized-end logic also applies to the call auctions used to resume trading after a halt, discussed next.

## Not Just Open and Close — the Call Auction Is a General Restart Mechanism

The call auction isn't a ceremony reserved for bookending the trading day — it's the exchange's general-purpose tool for restarting orderly trading after any kind of gap or interruption. As covered in [circuit breakers and VI](/en/basics/circuit-breaker-vi-sidecar-explained/), when a single stock trips a Volatility Interruption, that one stock switches into a call auction for a couple of minutes before returning to continuous trading. A stock resuming after an extended trading halt goes through the same process to rediscover its first price. The logic is the same every time: restarting continuous matching immediately after a gap or a shock risks letting a handful of orders distort the price, while a call auction first pools accumulated orders to find a balanced price before handing control back to continuous trading. Note that this is distinct from [after-hours trading](/en/basics/after-hours-trading-aftermarket-explained/) before and after the regular session, which trades at an already-fixed price (the prior or same-day close) under ordinary time priority — a different mechanism built for a different purpose.

## Why the Close Isn't "the Last Trade" — and Why That Matters

It matters in practice that continuous trading stops at 15:20 and the following ten minutes belong to the closing call auction. The price officially recorded as that day's close — the one used to calculate the KOSPI and KOSDAQ indices, [ETF net asset value](/en/basics/etf-tracking-error-premium-discount/), and margin/mark-to-market thresholds — is not the last trade from continuous trading at 15:20, but the price that comes out of the ten-minute call auction that follows. That's exactly why flows that need to track the official close — [index fund and ETF rebalancing trades](/en/basics/index-rebalancing-effect/) chief among them — tend to concentrate heavily in this window. Program trading tied to settling the day's final [futures basis](/en/basics/stock-index-futures-basis-explained/) often piles into the same ten minutes, sometimes pushing volume there above what the preceding continuous session saw. The closing call auction, in other words, isn't "the moment trading quietly stopped" — it's the single window where the largest share of mechanical, rules-driven demand converges. A spike in closing-auction volume on a given day often reflects index and fund mechanics rather than active investor decision-making, so it's worth reading with that context in mind.

## Key Takeaways

- The regular session's open and close aren't set by continuous matching — they come from a separate call auction (08:30–09:00 for the open, 15:20–15:30 for the close), during which orders accumulate without filling at all.
- The exchange calculates the single price that maximizes matched volume across all accumulated buy and sell orders and fills everything at once when the window closes; the indicative price shown on screen beforehand is only a running estimate.
- A randomized end time prevents last-second order manipulation, and the same call-auction mechanism is used generally — including after a Volatility Interruption or a trading halt — any time orderly trading needs to restart.
- Because the official close used for index calculation, ETF NAV, and margin thresholds comes from the closing call auction rather than the last continuous trade, institutional flows that track the close concentrate heavily in that final ten-minute window.

## FAQ

### Should I trade off the indicative price shown during a call auction?
The indicative price is a provisional estimate based only on orders accumulated so far, and it keeps shifting as new orders arrive and old ones get canceled or amended, particularly right before the random end. Treating it as a locked-in number and timing a trade around it is risky.

### Can I cancel or amend an order during the call auction window?
Yes. Only execution is paused during the window — placing, canceling, or amending an order works exactly as it does the rest of the day. Whatever you do feeds immediately into the indicative price everyone else sees.

### How is this different from after-hours trading at the fixed closing price?
After-hours trading at a fixed price settles trades at an already-determined price (the prior or same-day close) under ordinary time priority. A call auction is the opposite case: the price itself hasn't been set yet, and the whole point of the window is to discover it from the accumulated orders — a fundamentally different mechanism.

### Why doesn't a market order fill immediately during a call auction?
A market order asks to fill "at whatever price is currently available," but during a call auction window there is no confirmed price yet — nothing has traded. So market orders sit in the book along with everything else and fill together, at the single clearing price, only once the window ends.

> ⚠️ This lesson is for informational purposes only and is not investment advice. Investment decisions and their outcomes are the sole responsibility of the investor.
