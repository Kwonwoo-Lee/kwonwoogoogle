---
slug: poor-mans-covered-call-pmcc
title: "Poor Man's Covered Call (PMCC): Trading a Covered Call With a LEAPS Call Instead of 100 Shares"
description: "How the poor man's covered call swaps 100 shares for a deep ITM LEAPS call, cutting capital by roughly 60-80% while still collecting covered-call income."
order: 61
updated: 2026-09-22
keywords: ["poor man's covered call", "PMCC strategy", "PMCC vs covered call", "LEAPS call option strategy", "diagonal spread options", "how does PMCC work", "deep in the money LEAPS delta", "long call diagonal spread"]
seo_audited: 2026-09-22
---

## Covered Calls Without Buying 100 Shares

Lesson 27's [wheel strategy](/en/strategies/wheel-strategy-options/) covered the covered call as half of a repeating income cycle: you own 100 shares, sell a call against them, and collect premium. The problem is right there in the setup — owning 100 shares of anything priced above $100 ties up five figures of capital before you've sold a single option. The **poor man's covered call (PMCC)** solves that specific problem. It replaces the 100 shares with a single long-dated, deep-in-the-money call option (a **LEAPS** — Long-term Equity AnticiPation Security), then sells short-dated calls against that position exactly the way a normal covered call would sell them against stock. The structure is formally called a **long call diagonal spread** — two calls, same underlying, different strikes and different expirations. "Poor man's" is a nickname, not a technical term, but it captures the point accurately: you get covered-call-like exposure and income for a fraction of the capital.

This isn't a fringe idea. It's one of the more actively discussed options structures in retail trading education right now, precisely because it addresses a real, common complaint — that plain covered calls and the wheel lock up too much cash for the average account size. But a PMCC is not a cheaper clone of a covered call. It behaves similarly most of the time and differently at the edges, and those edge cases are where the strategy actually needs to be understood, not just imitated.

## The Two Legs

**Leg one — the long LEAPS call.** Buy a call option that's deep in the money, with 12 months or more until expiration. "Deep in the money" typically means a **delta in the 0.70–0.85 range** — a rough convention, not a fixed rule. Delta approximates how much the option's price moves per $1 move in the stock, so a 0.80-delta call behaves like roughly 80 shares of stock for every 100-share equivalent contract, while costing far less than the shares themselves. The deeper in the money and the further out in time the LEAPS is, the more of its price is **intrinsic value** (the built-in, real value from being in the money) and the less is **extrinsic value** (the time-and-volatility premium that decays to zero at expiration) — and it's the extrinsic portion you want to minimize, since that's the part working against you as a long option holder.

**Leg two — the short call.** Exactly as in a standard covered call, sell a call against the position with a strike above the current price, typically **30–45 days to expiration**, collecting premium up front. The difference is what's "covering" this short call: instead of 100 real shares, it's the long LEAPS call underneath it.

<figure class="diagram">
  <img src="/static/img/charts/en/poor-mans-covered-call-pmcc.svg" alt="Side-by-side comparison showing a traditional covered call requiring $10,000 to buy 100 shares versus a poor man's covered call requiring roughly $3,400 for a deep in-the-money LEAPS call, with the same short call sold on top of both positions" loading="lazy">
  <figcaption>Both structures sell the same short-dated out-of-the-money call on top. The traditional covered call funds that short call with 100 real shares; the PMCC funds it with a much cheaper LEAPS call standing in for the shares.</figcaption>
</figure>

## Why It Works: Renting Delta Instead of Owning It

A deep ITM LEAPS call isn't a coupon or a discount — it's a real trade-off. You're paying for roughly 70–85% of the stock's price exposure (its delta) while putting up only a fraction of the capital, because the option's built-in leverage does the rest of the work. The capital you don't spend on the LEAPS is capital freed up for other positions, which is the entire appeal of the structure — the same logic behind why traders study capital efficiency in position sizing frameworks like Lesson 42's [Kelly criterion](/en/strategies/kelly-criterion-position-sizing/).

The trade-off is that a LEAPS call is not stock. It has its own expiration, its own extrinsic value that decays over time (much more slowly than a short-dated option, but not zero), and — critically — it does not pay dividends. A shareholder collects dividends regardless of what they do with covered calls; a PMCC holder collects none, and dividend-paying stocks price that expected payout into the call's premium in a way that makes deep ITM calls on dividend payers slightly cheaper than a naive delta calculation would suggest. That's a real, structural difference between the two positions, not just a footnote.

## Picking the Legs: Delta, DTE, and the "Broken Diagonal" Mistake

| Leg | Typical convention | What it controls |
|---|---|---|
| LEAPS strike/delta | 0.70–0.85 delta, deep ITM | How closely the LEAPS tracks the stock; higher delta = more stock-like, more capital |
| LEAPS expiration | 12+ months out | More time before extrinsic decay accelerates; rolled well before expiration |
| Short call strike/delta | Often 0.20–0.30 delta, OTM | Premium size vs. how often it gets tested |
| Short call expiration | 30–45 days out | Balances time decay speed against management frequency |

These ranges are conventions cited across options-education material, not statistically validated rules — they're a reasonable starting point to adjust from, not a formula to apply blindly.

The single most-cited beginner mistake with a PMCC is what's sometimes called a **broken diagonal**: selling the short call at or below the LEAPS strike. If the short strike sits below the long strike, the maximum profit on the position is already negative before the stock even moves, because a diagonal spread's ceiling profit is bounded by (short strike − long strike) plus net credit collected — and that first term needs to be positive. Always keep the short call's strike above the LEAPS strike; how far above is a matter of how much premium you want versus how much room you want to leave the trade before it caps out.

## A Worked Example

Say a hypothetical stock trades at $100. A trader wants covered-call-style exposure but doesn't want to tie up $10,000 buying 100 shares outright.

**Setting up the PMCC.** They buy a 12-month LEAPS call at the $70 strike (delta roughly 0.80) for $34.00 ($3,400 per contract) — intrinsic value of $30 plus $4.00 of extrinsic value. That's about 66% less capital than the $10,000 needed to buy 100 shares outright. They then sell a 35-day call at the $105 strike (delta roughly 0.30) for $2.50 ($250), bringing the net cost down to $3,150.

- **If the stock stays roughly flat or drifts modestly, staying below $105 through expiration:** the short call expires worthless, the $250 is banked, and a new short call gets sold — the same repeating income cycle as a standard covered call, just funded by a much smaller capital base. Net cost drifts down cycle over cycle, the same way the wheel's cost basis drifts down in Lesson 27.
- **If the stock rallies hard, say to $110, and the short call goes meaningfully in the money:** this is where a PMCC diverges sharply from a real covered call. A real covered-call holder simply has their shares called away at $105 and pockets the gain. A PMCC holder doesn't own shares to deliver — assignment on the short call would require either exercising the LEAPS (paying the full $7,000 strike to actually acquire the shares, which usually defeats the purpose of the trade) or buying 100 shares on the open market at $110 to deliver at $105, taking a $500 loss on that leg alone. In practice, this is avoided entirely by **closing or rolling the short call before it goes deep in the money** rather than letting it run into assignment — the LEAPS itself still gains from the rally, so the position overall is typically still profitable, but the mechanics of closing it out are more involved than a real covered call's simple "shares get called away."

## PMCC vs. Traditional Covered Call

| | Traditional Covered Call | PMCC (LEAPS Diagonal) |
|---|---|---|
| Capital required | Full share price × 100 | Roughly 20–40% of that, depending on delta |
| Underlying exposure | Exactly 1.0 delta (real shares) | Approximately 0.70–0.85 delta (LEAPS) |
| Dividends | Collected as a shareholder | None — option holders don't receive dividends |
| Max loss | Stock can theoretically fall to zero | Capped at the net debit paid (LEAPS cost minus credits collected) |
| Assignment on short call | Shares simply get called away | Requires closing the position or exercising the LEAPS — more moving parts |
| Time decay on the "stock" leg | None — shares don't expire | LEAPS extrinsic value decays slowly, and it must eventually be rolled or closed |
| Bid-ask spreads | Tight, highly liquid | Often wider on far-dated, deep ITM strikes — worse fill prices |
| Best fit | Investors who want to actually hold the shares long-term | Traders who want covered-call-style income with less capital tied up |

The capped max loss is a genuine advantage over plain stock ownership — a PMCC cannot lose more than what was paid for it net of credits collected, while a covered call position can still ride shares all the way down to zero. That downside protection isn't free, though: it comes at the cost of giving up dividends, taking on wider spreads, and adding real management complexity that a simple "buy shares, sell a call" position doesn't have.

## Managing the Position

- **Roll the short call around 50% of its max profit or 21 days to expiration, whichever comes first** — the same convention covered in Lesson 58's [iron condor and credit spread](/en/strategies/iron-condor-credit-spread/) lesson, since both structures are managing the same accelerating gamma risk as expiration nears.
- **Roll the LEAPS itself once its delta decays below roughly 0.70**, which commonly happens somewhere around 90–120 days before its own expiration. Waiting past that point runs into a steepening extrinsic-value decay curve that works against a long option holder.
- **Never let the short call go deep enough in the money that assignment becomes likely** without a plan — check the position well before expiration, not the week of.
- **Watch the dividend calendar on the underlying.** Short calls near an ex-dividend date carry meaningfully elevated early-assignment risk on American-style options, since the call holder may exercise early specifically to capture the dividend.

## Limitations and Pitfalls

- **It is not a stock substitute in every scenario.** The LEAPS has its own expiration and decaying extrinsic value; a real share position does not. Treating a PMCC as functionally identical to owning stock long-term ignores that structural difference.
- **No dividends, ever.** For dividend-paying stocks, that's a real and recurring cost relative to actually owning shares, not a minor detail.
- **Liquidity is often worse on the LEAPS leg.** Far-dated, deep ITM options frequently have wider bid-ask spreads than near-the-money, front-month options, and a wide spread eats directly into the capital-efficiency advantage the strategy is built around.
- **A sharp drop can wipe out most of the LEAPS's value.** Even at 0.80 delta, a LEAPS call is still an option — a large enough decline can push it out of the money or force an early close at a steep loss, and the capped-loss feature doesn't make that outcome painless, just bounded.
- **Assignment mechanics are genuinely more complex than a plain covered call's.** Underestimating this and getting caught by an ITM short call with no plan is the most common way a PMCC goes wrong in practice.

## FAQ

### How is a PMCC different from just buying a regular covered call?
A traditional covered call requires owning 100 real shares. A PMCC replaces those shares with a single long-dated, deep-in-the-money LEAPS call that approximates the same delta exposure for a fraction of the capital — but that LEAPS eventually expires and pays no dividends, while real shares do neither of those things.

### What happens if the short call gets assigned?
Since a PMCC holder has no shares to deliver, assignment means either exercising the LEAPS to acquire shares at its strike (requiring the full capital outlay) or buying shares on the open market to deliver at the short strike, potentially at a loss on that leg. The standard practice is to close or roll the short call well before it's deep enough in the money for assignment to become likely, rather than dealing with assignment after the fact.

### Can a PMCC be run on any stock?
It works best on stocks with liquid, tightly-spread LEAPS options — typically large, actively-traded names. On thinly-traded stocks, wide bid-ask spreads on the far-dated calls can erode much of the capital-efficiency benefit the strategy is meant to provide.

## Summary

- A PMCC (poor man's covered call) replaces the 100 shares in a traditional covered call with a single deep ITM, long-dated LEAPS call, cutting required capital by roughly 60–80% while approximating the same delta exposure.
- The structure is a long call diagonal spread: a long LEAPS call (typically 0.70–0.85 delta, 12+ months out) paired with a short, near-dated OTM call (typically 30–45 DTE) sold repeatedly for income.
- The most common setup mistake is a "broken diagonal" — selling the short call at or below the LEAPS strike, which caps maximum profit below zero before the trade even starts.
- A PMCC is not a perfect substitute for owning stock: it pays no dividends, its LEAPS leg has its own decaying extrinsic value and must be rolled, and assignment on the short call is more complicated to unwind than simply having shares called away.
- The capped maximum loss (limited to the net debit paid) is a genuine structural advantage over holding shares outright, but it comes bundled with wider bid-ask spreads, added rolling discipline, and more moving parts to manage than a plain covered call.
