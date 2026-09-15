---
slug: etf-tracking-error-premium-discount
title: "ETF Tracking Error vs Premium/Discount to NAV — Two Different Ways an ETF Can Drift From Its Index"
description: "Why an ETF's market price can diverge from its net asset value (premium/discount), and why that's a completely different problem from long-run tracking error against the benchmark."
order: 82
updated: 2026-09-15
keywords: ["ETF tracking error explained", "ETF premium discount to NAV", "tracking error vs tracking difference", "what is iNAV", "synthetic ETF swap risk", "authorized participant creation redemption", "ETF replication methods"]
seo_audited: "2026-09-15"
---

## Two Kinds of "Off," Two Different Causes

ETF investors run into more than one way for a fund to fall short of expectations, and two of them get confused constantly because they sound almost identical. One is "the price I'd pay for this ETF right now is higher or lower than what its holdings are actually worth." The other is "over months or years, this ETF's return has quietly drifted away from the index it's supposed to track." The first is called premium/discount to NAV; the second is tracking error. [What Is an ETF](/en/basics/etf-basics/) already introduced the idea that an authorized participant (AP) keeps an ETF's price pinned close to its actual asset value. This lesson pulls that mechanism apart to show exactly why it works, and — just as importantly — why it sometimes doesn't.

## Three Numbers That Get Mixed Up: NAV, iNAV, and Market Price

Untangling the two concepts starts with three terms that look similar but aren't.

- **NAV (net asset value)**: the total value of everything the fund holds, minus liabilities, divided by shares outstanding. Calculated once, officially, after the market closes, using that day's closing prices.
- **iNAV (indicative NAV)**: since no official NAV exists mid-day, exchanges or fund sponsors publish a running estimate every few seconds during trading hours, built from the real-time prices of the underlying holdings. It's a "here's roughly what this should be worth right now" estimate.
- **Market price**: the actual price at which the ETF itself trades on the exchange, set by whoever is buying and selling at that moment.

Premium/discount measures the gap between **market price and iNAV** (or the prior day's official NAV): `(market price − iNAV) / iNAV × 100`. A positive number means the ETF is trading rich; negative means it's trading cheap. Tracking error, by contrast, has nothing to do with iNAV or market price at that instant — it measures how far the **fund's realized return** has diverged from the **index's return** over a stretch of time, typically expressed using daily return differences over a year. One question is "is this the right price right now?" The other is "is this fund actually delivering what it promised over time?" They're not the same question.

## Why Premiums and Discounts Happen — Arbitrage Doesn't Always Fire Instantly

The reason an ETF's market price usually stays close to its iNAV comes down to arbitrage by authorized participants. If the market price falls below iNAV (a discount), an AP can buy the cheap ETF shares on the open market, redeem them with the fund sponsor for the underlying basket of securities (worth more), and sell that basket for a profit. If the price rises above iNAV (a premium), the AP runs it in reverse: deliver a basket of securities to the sponsor, receive newly created ETF shares, and sell them into the market at the richer price. As long as this creation/redemption loop keeps functioning, gaps tend to close quickly.

The catch is that the loop doesn't fire "always, automatically, instantly." A few conditions can widen the gap and keep it open longer than expected:

- **Illiquid underlying assets.** High-yield bonds, small-cap emerging-market stocks, or real estate holdings are hard to actually buy or sell at their last quoted price, so the iNAV itself is really just an estimate built from stale or thin trades. When that happens, the market price often reflects reality faster than iNAV does, and the gap widens.
- **The underlying market is closed.** A U.S.-listed ETF tracking a Korean stock index trades during U.S. hours, while the Korean market it holds is already shut. The iNAV is frozen at a closing price from hours earlier, but the ETF's market price keeps reacting to fresh information (currency moves, overnight futures) in real time — producing a meaningful gap.
- **Markets move violently.** During the March 2020 pandemic crash, several U.S. corporate bond ETFs traded at prices well below their reported NAV. Bond markets themselves had essentially stopped producing reliable quotes, so the iNAV lagged reality, and some analysts argued the ETF's market price was actually the more accurate signal of what those bonds could realistically fetch in a sale.
- **Small assets under management (AUM) or thin trading volume.** Even with a liquidity provider quoting the ETF, thin volume tends to widen bid-ask spreads — and premiums/discounts widen right along with them.

## Why Tracking Error Happens — Different Replication Methods Leak in Different Places

If premium/discount is a momentary pricing gap, tracking error is closer to a slow leak built into how the fund reproduces the index in the first place. There are three broad replication approaches, and each one leaks differently.

**Full physical replication** means buying every constituent of the index at its exact index weight. This works well for large, liquid benchmarks like the S&P 500 or KOSPI 200, where tracking error mostly comes down to the expense ratio and minor cash drag (the lag between receiving a dividend and reinvesting it).

**Sampling (representative replication)** is used when an index has thousands of constituents — a broad bond index, say — making full replication impractical. The fund buys a statistically representative subset instead. Because that sample is never a perfect mirror of the full index, sampling error adds to tracking error on top of the expense ratio.

**Synthetic replication** skips holding the underlying securities directly. Instead, the fund enters a total return swap with a counterparty — typically an investment bank — that contractually agrees to pay the fund the index's return in exchange for a fee, while the fund holds a separate collateral basket. Because the swap counterparty is contractually on the hook for the index return, tracking error itself can, in theory, be managed very tightly. What it adds instead is **counterparty credit risk**: if the swap counterparty defaults, losses depend on how well the collateral basket covers the shortfall. That's exactly why European regulation (under UCITS rules, for instance) caps how much swap exposure a fund can carry relative to its net assets.

## A Number Check — AP Arbitrage in Practice

A concrete example makes the arbitrage mechanism less abstract. Say an ETF's iNAV sits at $100.00, but buying pressure has pushed the market price to $100.50 — a 0.5% premium (`(100.50 − 100.00) / 100.00 × 100`). An AP can deliver roughly $100 worth of the underlying basket to the sponsor, receive one newly created ETF share in return, and sell it into the market at $100.50 — pocketing roughly $0.50 in theoretical profit. Repeated across multiple APs, this creation activity keeps adding new ETF shares to the market, which gradually narrows the premium. Run it in reverse for a discount: if the market price drops to $99.50, an AP buys ETF shares cheaply, redeems them with the sponsor for $100 worth of the underlying basket, and resells that basket for a profit — shrinking the ETF's outstanding share count and pushing its price back up toward iNAV. Because this two-way arbitrage runs more or less continuously, premiums and discounts on liquid, well-arbitraged ETFs typically stay within a narrow band — often well under 0.5% under normal conditions.

## Splitting the Number: Tracking Difference vs. Tracking Error, Strictly Defined

In practice, "tracking error" often gets used loosely to describe two different calculations, and it's worth separating them.

Suppose an index returns exactly 10.00% over a year, while the ETF tracking it returns 9.86% on a NAV basis. That -0.14 percentage-point gap is the **tracking difference** — a single, directional number. It might break down as roughly `-0.15% (expense ratio) + 0.03% (securities-lending income) − 0.02% (sampling drag) = -0.14%`.

**Tracking error**, in its stricter sense, isn't that average gap at all — it's the standard deviation of the day-to-day return differences between fund and index. A fund could post a tiny -0.14% annual tracking difference while its daily gap swings wildly (some days 0.5% ahead, other days 0.4% behind), which would produce a large tracking error even with a small average gap. Conversely, a fund that lags by a nearly identical tiny amount every single day would show a large cumulative tracking difference but a very small tracking error. When reading a fund's disclosures, it's worth checking which of the two — "how far behind, on average" versus "how erratically behind" — a given figure is actually describing.

## What to Actually Check — Verify Against Disclosures, Not Intuition

Both premium/discount and tracking error are things a fund reports, not things to guess at.

- **Replication method**: the prospectus or sponsor's website states whether the fund is physically replicated or synthetic (swap-based). For synthetic funds, it's also worth checking who the swap counterparty is, how the collateral basket is structured, and what the swap exposure cap is.
- **AUM and average trading volume**: smaller and thinner funds tend to run wider, more persistent premiums/discounts.
- **Underlying asset liquidity**: funds holding liquid large-cap domestic equities tend to run tight premiums/discounts; funds holding foreign assets, bonds, or physical commodities are structurally more prone to wider gaps.
- **Reported tracking difference over 3+ years**: most sponsors publish cumulative "return versus index since inception" figures in monthly or annual reports — worth checking directly rather than estimating from the expense ratio alone.
- **For leveraged/inverse products**: on top of the ordinary tracking error covered here, [Leveraged & Inverse ETF Decay](/en/basics/leveraged-inverse-etf-decay/) explains a separate, structural source of divergence that stacks on top of everything discussed above.

## Key Takeaways

- Premium/discount measures a moment-in-time price gap — whether the market price is currently richer or cheaper than the fund's actual asset value (iNAV). Tracking error measures a separate thing: how far the fund's return has drifted from the index's return over time.
- Premium/discount is normally kept tight by authorized participants arbitraging through the creation/redemption process, but that mechanism can loosen — and the gap can widen and persist — when the underlying assets are illiquid, when the underlying market is closed, or when markets move violently.
- Tracking error's source depends on replication method: full physical replication, sampling, and synthetic (swap-based) replication each leak in different places, from expense ratios and cash drag to sampling error and swap counterparty risk.
- "Tracking difference" (the average gap) and stricter "tracking error" (the standard deviation of daily gaps) are different numbers — check which one a disclosure is actually reporting.
- Both figures are best verified against a fund's actual published data rather than estimated from the expense ratio alone.

## Frequently Asked Questions

### Does a wide premium/discount automatically mean a bad ETF?
Not necessarily. It often reflects the underlying assets' liquidity conditions at that moment rather than a flaw in the fund itself. That said, an ETF that repeatedly and persistently trades at a wide gap may be signaling thin AUM or weak liquidity-provider activity, so it's worth checking the premium/discount at the moment of any trade.

### Can an ETF have zero tracking error?
Practically, no — the expense ratio alone leaks a little every single day. That said, physically replicated funds tracking liquid, large-cap indices typically keep tracking error very small, and synthetic (swap-based) funds can, in principle, manage it even tighter given how the swap contract is structured.

### Are synthetic (swap-based) ETFs risky?
On tracking error alone, they're often managed more precisely than physical replication. What they add is counterparty credit risk — the swap counterparty's default. Regulations commonly cap swap exposure and require collateral to limit that risk, so it's worth checking how a specific fund's swap structure is set up in its prospectus.

### When do premiums/discounts tend to widen the most?
Most often during hours when the ETF trades but its underlying market is closed, during sharp market moves when the underlying assets' own quotes dry up, and structurally for funds holding inherently less liquid assets, such as high-yield bonds or small-cap emerging-market stocks.

> ⚠️ This article is for informational and educational purposes only and is not a recommendation to buy or sell any specific ETF. The example figures are simplified for illustration; actual numbers vary by fund and should be verified against the fund's prospectus and sponsor disclosures.
