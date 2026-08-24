---
slug: congressional-stock-trading
title: "Congressional Stock Trading: Tracking STOCK Act Disclosures and the Pelosi Trade"
description: "Learn how the STOCK Act's 45-day disclosure rule exposes congressional stock trades, how to screen and follow them via trackers or ETFs, and the real limits."
order: 33
updated: 2026-08-24
keywords: ["congressional stock trading", "Nancy Pelosi stock tracker", "STOCK Act disclosure", "copy congress trades", "NANC ETF", "politician stock trading strategy", "STOCK Act 45 day rule", "insider trading vs congress trading"]
seo_audited: 2026-08-24
---

## Why Politicians' Trades Became a Trading Strategy

A few years ago, disclosures showing that former House Speaker Nancy Pelosi's husband had bought a large block of tech-stock call options went viral, and a wave of investors started trying to mirror the couple's trades directly. Trackers and apps built entirely around **congressional stock trading** disclosures multiplied, Pelosi picked up the nickname "the best-performing hedge fund manager in Congress," and eventually publicly traded ETFs launched that mechanically follow the disclosed trades of one party's members. Data that used to sit in a niche compliance filing became a mainstream trade idea.

This is possible because US law requires members of Congress to publicly disclose their stock trades. What that disclosure actually looks like in practice — and whether trading on it late is a workable edge — is a separate question entirely. This lesson covers exactly how the disclosure system works, and how it differs fundamentally from the "near real-time" signals covered in [Lesson 22 on options sweeps](/en/strategies/unusual-options-activity/) or [Lesson 25 on dark pool prints](/en/strategies/dark-pool-prints/).

## What the STOCK Act Actually Requires

The **STOCK Act (Stock Trading on Congressional Knowledge Act)**, passed in 2012, requires members of Congress and their spouses and dependent children to publicly report any securities transaction over $1,000 within **45 days of the trade**. These filings are called **Periodic Transaction Reports (PTRs)** — senators file with the Senate Office of Public Records, representatives with the House Clerk.

A few practical details matter here:

- **Dollar amounts are reported as ranges, not exact figures** — e.g. "$1,001–$15,000" or "$50,001–$100,000" — so a third party can't precisely reconstruct share count or entry price from the filing alone.
- **Spousal and dependent trades count too**, and in practice a large share of the trades that get media attention are filed under a spouse's name rather than the member's own.
- **Enforcement is relatively weak.** The penalty for filing late is small, and multiple outlets have repeatedly documented members disclosing well after the 45-day window with little consequence.

In other words, the STOCK Act doesn't ban members of Congress from trading — it requires them to disclose if they do. That distinction runs through everything else in this lesson.

<figure class="diagram">
  <img src="/static/img/charts/en/congressional-stock-trading.svg" alt="Diagram comparing the congressional STOCK Act disclosure path, which can take up to 45 days before a trade becomes public, against the corporate insider SEC Form 4 path, which requires disclosure within 2 business days, with a bar chart showing the gap between the two disclosure windows" loading="lazy">
  <figcaption>Top: congressional trades can stay undisclosed for up to 45 days. Bottom: corporate insiders (Form 4) must disclose within 2 business days — a far shorter lag.</figcaption>
</figure>

## The Core Problem: You're Buying 45-Day-Old News

The first thing a trader needs to internalize is that following a congressional trade disclosure means acting on something that happened **up to 45 days ago, and often longer in practice**, since many members file close to the deadline or after it. On top of the legal window, add the time it takes a tracker service to ingest and push out the filing, and the additional days it takes a fund like NANC to actually execute a purchase through its own compliance process.

Compare that to a near-real-time signal like the [volume profile reads covered in Lesson 12](/en/strategies/volume-profile-poc/): those try to capture what's happening in the market right now. Congressional disclosure data, by its very structure, tells you what already happened.

### Congressional Trading vs. Corporate Insider Form 4

The sharpest way to see this lag is to compare it against SEC Form 4 — the disclosure corporate officers, directors, and 10%+ shareholders file when they trade their own company's stock. Both are "follow the public paper trail of a large trader" strategies, but the speed and character of the information are very different.

| Aspect | Congressional Trading (STOCK Act, PTR) | Corporate Insider Trading (SEC Form 4) |
|---|---|---|
| Disclosure deadline | Within 45 days of the trade | Within 2 business days of the trade |
| Typical time-to-file in practice | Often close to, or past, the deadline | Compliance tends to be tighter |
| Dollar detail disclosed | Range only | Exact share count and price |
| Nature of the informational edge | Broad exposure to legislation, policy, budget decisions | Direct knowledge of company performance and operations |
| Cluster-signal convention | Multiple members trading the same name around the same time | 2+ insiders buying within 7 days, or 3+ within 15 days, treated as a stronger signal |
| Accessibility | Many free trackers; also mirrored by publicly traded ETFs | Free direct lookup via SEC EDGAR |

Form 4-based "cluster buying" — multiple insiders purchasing the same stock in a short window — has a comparatively longer track record of academic study behind it. Congressional trading, by contrast, draws from a small pool of roughly 535 members, carries a much longer disclosure lag, and the "edge" itself tends to be closer to policy direction than company-specific knowledge — reasons to treat the two as related but not equivalent techniques.

## Screening in Practice: Which Trades Are Worth Watching

Following every disclosed trade indiscriminately isn't a strategy. Trackers and traders commonly apply filters like these — none of which are official regulatory thresholds, just conventions the community has settled on.

| Screening criterion | Common rule of thumb | What it suggests |
|---|---|---|
| Committee assignment | Trade by a member who sits on the committee that directly oversees that industry | A plausibly larger information gap between the member and the public |
| Trade size | $100,000+ at the top of the disclosed range | Less likely to be an incidental small trade |
| Cluster pattern | Multiple, otherwise-unrelated members trading the same name around the same time | Could reflect a shared signal rather than one person's individual call |
| Options activity | Leveraged bets like call purchases rather than plain stock | Often read as a stronger conviction signal |
| Sell-side checked too | Reviewing disclosed sales, not just buys | Helps separate routine tax/rebalancing sales from conviction-driven exits |

## A Worked Example: Quantifying the Lag

Here's a purely illustrative scenario to make the timing problem concrete — not a real trade, just a walk-through of the mechanics. Say a hypothetical Representative A buys shares of semiconductor equipment maker Stock E on March 2, disclosed in the "$100,001–$250,000" range. The actual PTR isn't filed until April 14 — 43 days later, right at the edge of the legal window — and a tracker service pushes the alert to subscribers the next day, April 15. If Stock E had already risen 12% during those 43 days, anyone acting on the April 15 alert has already missed a meaningful chunk of that move. Add a few more days for an ETF that mirrors this member's trades to clear its own rebalancing process, and the gap between the original trade date and the fund's actual purchase can stretch close to two months.

## Why This Signal Isn't Completely Useless Anyway

Given a lag this large, why do traders keep watching this data at all? Mostly because the more defensible use case isn't short-term entry timing on a single stock — it's reading **policy direction as a slower-moving signal**. Legislative shifts like deregulation of an industry or a budget allocation typically play out over months or years, not days. A 45-day disclosure lag doesn't necessarily erase the relevance of that broader direction. In that framing, the more useful question isn't "exactly when and at what price did this member buy," but "are multiple members of a relevant committee showing sustained interest in a particular sector."

That framing is itself a convention, not a proven fact. Media coverage repeatedly noted that Nancy Pelosi's disclosed returns beat the market average in 2021, but generalizing that into "Congress consistently beats the market" risks **survivorship bias** — a small number of standout members, out of roughly 535 total, get cited over and over in coverage.

## Limitations and Pitfalls

- **The information is structurally stale.** With a legal window of up to 45 days — and real-world filing often slower than that — this data was never built to support fast entries.
- **Vulnerable to survivorship bias.** Trackers and media spotlight the handful of members with standout results; average performance across the full body of Congress, including losing trades, gets far less attention.
- **Small, uneven sample.** Roughly 535 members sit on different committees with different access to information, so treating "Congress" as one homogeneous group overstates how comparable individual members' edges actually are.
- **Enforcement and legislative risk.** Weak penalties for late filing have drawn repeated criticism, and multiple bipartisan bills to ban congressional stock trading outright have been introduced. If any such bill eventually passes, the entire premise of this strategy could disappear — worth checking current legislative status rather than assuming the status quo holds indefinitely.
- **Tracking ETFs inherit the same lag.** Funds like NANC and KRUZ are built on the same disclosure data, so they carry the identical staleness problem, plus a management fee on top.
- **Weak as a standalone signal.** This isn't a precise buy/sell trigger — it's best treated as a supplementary read on sector-level policy sentiment, not a primary entry rule.

## FAQ

### Is it legal to trade based on congressional disclosures?
Yes. Trading on publicly disclosed PTR data is legal — the entire point of the STOCK Act is to make this information public, which is a different matter from trading on non-public information. The catch is that what you're reading is, by design, already old news by the time it's public.

### Does Nancy Pelosi actually beat the market consistently?
Media coverage has repeatedly noted disclosed returns beating the market average in specific years, but generalizing that into consistent outperformance deserves caution. It risks survivorship bias from a small number of standout cases getting repeated coverage, and the disclosed dollar ranges make it difficult for a third party to precisely reconstruct entry price and share count in the first place — which adds uncertainty to any calculated return.

### Do ETFs like NANC or KRUZ solve the disclosure-lag problem?
No. These funds are built on the exact same PTR filings, so they inherit the same fundamental staleness. What they do offer is convenience — spreading exposure across many members' trades without having to screen and buy individual names yourself.

## Summary

- The STOCK Act requires members of Congress and their spouses/dependents to publicly file a PTR within 45 days of any trade over $1,000; it mandates disclosure, not a trading ban.
- Amounts are disclosed as ranges rather than exact figures, and real-world filing often happens close to or past the 45-day deadline, making the effective information lag larger than it looks on paper.
- Compared to SEC Form 4 (corporate insider trading, 2-business-day window), congressional disclosure is far slower and drawn from a much smaller sample, which rules out fast-follow entry strategies.
- Screening by committee relevance, trade size, cluster activity, and options usage is a more defensible approach than blindly copying every disclosed trade.
- Treating this data as a slow-moving read on sector-level policy sentiment — rather than a precise entry signal — while staying aware of survivorship bias, sample limitations, and the risk of future legislative bans, is the more realistic way to use it.
