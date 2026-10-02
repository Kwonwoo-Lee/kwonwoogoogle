---
slug: short-swing-profit-rule-korea
title: "Korea's Short-Swing Profit Rule: Why Insiders Must Return Gains Even Without Using Inside Information"
description: "Why executives and major shareholders who buy and sell their own company's stock within six months must hand back the profit regardless of intent, how it's calculated, and how it differs from the US's Section 16(b)."
order: 117
updated: 2026-10-02
keywords: ["short-swing profit rule Korea", "what is short swing profit", "insider must return stock profit", "section 16b vs Korea insider rule", "six month stock trading rule executives", "short swing profit calculation"]
seo_audited: "2026-10-02"
---

## A Notice to Return Profit — Even on a Trade That Lost Money Overall

A listed company's finance director buys 1,000 shares of his own employer's stock. Two months later, needing cash, he sells 500 of them. The stock happened to tick up slightly in between, so that sale shows a small gain — but the 500 shares he still holds later drop in value, leaving him net negative across the whole position. He never touched any non-public information. Yet a few days later, the company sends him a formal notice demanding he return the profit from the sale. That outcome sounds unfair, but it isn't a misapplication of the rule — it's the rule working exactly as designed. The mechanism behind it is Korea's **short-swing profit rule**, set out in Article 172 of the Financial Investment Services and Capital Markets Act. Where [insider trading and fair disclosure rules](/en/basics/insider-trading-fair-disclosure-explained/) require proving that someone actually used non-public information before any penalty applies, the short-swing rule skips that proof entirely — the mere fact of buying and selling within six months is enough to trigger disgorgement.

## What the Rule Actually Says

Article 172 requires that when an executive, employee, or major shareholder of a listed company buys that company's stock and sells it within six months — or sells first and buys back within six months — and profits from the round trip, the company can demand that profit be returned. The "major shareholder" threshold here is different from the one used in [beneficial ownership (5%) reporting](/en/basics/beneficial-ownership-report-5-rule/): for the short-swing rule, it means someone who, combined with related parties, holds 10% or more of the company, or who otherwise exercises effective control over decisions like appointing or removing executives. The securities covered go beyond common stock to include convertible instruments like [convertible bonds and bonds with warrants](/en/basics/convertible-bonds-cb-bw/) that can be turned into shares. If the company itself doesn't pursue the claim, the law also gives shareholders a path to file a **derivative suit** on the company's behalf, closing off the obvious workaround where a company simply declines to go after its own insider.

## Why It Ignores Whether Non-Public Information Was Actually Used

The part of this rule people misunderstand most often is assuming that proof of using inside information must exist somewhere for it to apply. It's the opposite. Korean regulators and courts have consistently treated this as a rule of **strict liability** — one that applies mechanically regardless of intent or whether non-public information played any role. The design logic becomes clear once you see what the alternative would require. Ordinary insider trading enforcement needs a regulator or prosecutor to prove that a specific executive knew specific bad news and traded ahead of its release — and proving what was inside someone's head at the moment of a trade is genuinely hard to do. The short-swing rule sidesteps that evidentiary problem by design. Once someone holding insider or major-shareholder status buys and sells within six months and the transaction shows a profit, the obligation to return that profit arises automatically, with no inquiry into intent at all. That's exactly how the finance director in the opening example ends up owing money despite having used no inside information and having lost money on his position overall — and that apparent harshness is the point. By removing any incentive to even test the waters with short-term trades, the rule prevents insiders from ever reaching the stage where information advantage could be exploited in the first place. It's a preventive, mechanical backstop rather than a punishment aimed at proven wrongdoing.

## How the Profit Is Actually Calculated

The amount owed isn't estimated loosely — it follows a formula fixed in the implementing regulation. For a single buy and a single sell, the math is straightforward:

> Short-swing profit = (sale price − purchase price) × matched quantity − (trading commissions + securities transaction tax + related levies)

The "matched quantity" is whichever is smaller: the number of shares bought or the number sold. When there are multiple transactions, Korea applies **first-in, first-out (FIFO)** matching — the earliest purchase is paired against the earliest sale, and the process repeats down the remaining balance. Take an executive who buys 1,000 shares at ₩10,000 in January, buys another 500 shares at ₩12,000 in March, then sells 800 shares at ₩15,000 in May. Under FIFO, the 800 shares sold in May are matched against the first 800 of the 1,000 shares bought in January. The profit is (₩15,000 − ₩10,000) × 800 = ₩4,000,000, with trading costs subtracted from that to get the final amount owed. The 500 shares bought in March at a higher price remain unmatched and carry forward to be paired against any future sale.

## What's Exempt — Not Every Trade Is Caught

The rule doesn't mechanically apply to every possible buy-sell combination. The implementing regulation carves out transactions that either don't really count as discretionary "trading" or carry little realistic risk of information abuse. The main exemptions include acquiring shares by exercising a stock option already granted, converting an already-held convertible bond or bond-with-warrant into shares, receiving an allocation through a public offering subscription, and acquiring shares through an employee stock ownership plan. What these all share is that the price and timing aren't something the insider can freely choose — there's structurally little room to time a trade around non-public information. Ordinary trades placed freely on the open market, by contrast, are never exempt, even when the trade was prompted by a broker's recommendation or routine tax-related portfolio rebalancing rather than any intent to exploit information.

## How It Compares to the US's Section 16(b)

Korea's short-swing rule wasn't invented from scratch — it was introduced in 1976, modeled on **Section 16(b)** of the US Securities Exchange Act of 1934. Both share the same core structure: officers and major shareholders who profit from buying and selling their own company's stock within six months must return that profit, applied as strict liability regardless of whether non-public information was involved. Where the two diverge is in how the profit gets calculated. Korea, as covered above, matches the earliest purchase against the earliest sale (FIFO). US courts instead apply **"lowest-in, highest-out" matching** — regardless of the actual chronological order of trades, the lowest purchase price within the six-month window is paired against the highest sale price first, then the next-lowest purchase against the next-highest sale, and so on. That method is deliberately built to produce the largest possible disgorgement amount, which can mean an executive who lost money overall across all trades in the period still owes a "paper profit" calculated from one cherry-picked pair of transactions. Korea's FIFO method can produce similarly harsh results, as the opening example showed, but the US's profit-maximizing matching rule is generally viewed as the more aggressive of the two in practice. Both countries pursue the same underlying goal — making sure insiders never have a reason to even consider trading on a short-term information edge — but they differ in exactly how unfavorably the math is stacked against the insider to get there.

## How Violations Get Caught, and What Happens If Nobody Pays Up

This rule isn't enforced through investigations that hunt for hidden trades — detection is built into a routine reporting requirement. Executives and major shareholders of listed companies must report every change in their holdings through an "officer and major shareholder ownership report" filed with regulators and the exchange. Using that filing data, the Financial Supervisory Service runs an annual, systematic check across all listed companies for any buy-sell pair that falls within a six-month window, then notifies the company when one is found. The company is then obligated to demand the profit back from the insider — and because a company and its own executive are often effectively on the same side, the law doesn't leave that obligation purely to goodwill. If the company fails to make the demand within two months of being notified, shareholders can step in and file a **derivative suit** to pursue the claim directly on the company's behalf. That right isn't open-ended, though: the claim is subject to a **two-year statute of limitations** from the date the profit arose, after which it can no longer be recovered no matter how clear-cut the case is. In practice, then, this isn't an absolute rule that always collects — it's a system built from three interlocking pieces: a disclosure network that surfaces the trades, a two-year clock, and overlapping rights for both the company and its shareholders to act.

## How Often This Actually Comes Up

The rule rarely makes headlines, but it's applied routinely. Korea's Financial Supervisory Service runs this cross-check across every listed company each year, and a meaningful share of flagged cases involve people who simply didn't realize their trade qualified — thinking a stock-option grant exempted the whole position, not realizing that open-market purchases layered on top of it did not, or trading through a spouse's or minor child's account without accounting for the related-party aggregation rule. The pattern itself says something important about how the rule works: neither good faith nor a plausible personal explanation changes the outcome. Once the two formal conditions — insider or major-shareholder status, and a profit from a buy-sell pair inside six months — are both met, the obligation to return the money is automatic.

## Takeaway

- Korea's short-swing profit rule (Capital Markets Act Article 172) requires executives, employees, and major shareholders of listed companies to return any profit from buying and selling (or selling and buying) their own company's stock within six months.
- It's strict liability — whether non-public information was actually used is irrelevant; only the insider's status and the trading outcome matter.
- Profit is calculated using FIFO matching, based on whichever is smaller between the buy and sell quantities.
- Stock option exercises, conversions of convertible bonds or bonds with warrants, public offering allocations, and employee stock ownership plan purchases are exempt.
- Modeled on the US's Section 16(b) from 1976, Korea uses FIFO matching while the US uses "lowest-in, highest-out" matching, making the calculation methods meaningfully different between the two systems.

## FAQ

### If I lost money on my overall position, do I still have to return anything?
Yes. What matters isn't your overall account performance — it's the profit calculated on the specific buy-sell pair matched within the six-month window. Losses on other, unmatched trades don't offset that figure; only the matched pair's profit is subject to return.

### If I can prove I never used any non-public information, does that remove the obligation?
No. The short-swing rule is a strict-liability mechanism that applies regardless of whether non-public information was used, so proving you didn't use any doesn't eliminate the obligation. This is the single biggest difference from [insider trading liability](/en/basics/insider-trading-fair-disclosure-explained/), which does require proving information was actually misused.

### If an executive resigns and then sells shortly after, does that avoid the rule?
Not necessarily. If someone held insider status at the time of the purchase, a sale that happens within six months of that purchase can still be caught even if they had already resigned by the time they sold. That said, the exact application can depend on status and ownership stake at each specific point in time, so specific cases are worth confirming with a legal professional.

### Does this apply to unlisted companies or Korea's KONEX market?
The rule applies to companies listed on the KOSPI and KOSDAQ markets. Purely unlisted, over-the-counter companies fall outside its scope, and the KONEX market may carry different coverage and conditions worth checking separately.

> ⚠️ This article is for informational and educational purposes only and is not legal or investment advice. The exact scope, exemptions, and calculation method under Korea's short-swing profit rule can change with amendments to the Capital Markets Act, so confirm the current standard through the Financial Supervisory Service or a legal professional before relying on it for a specific situation.
