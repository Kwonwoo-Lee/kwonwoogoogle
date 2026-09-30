---
slug: credit-rating-agencies-explained
title: "What Is a Credit Rating? How Moody's and S&P Actually Score Default Risk"
description: "The AAA-to-D rating scale, why notching gives a single issuer's bonds different grades, the issuer-pays conflict of interest, and how the US lost AAA from all three raters."
order: 111
updated: 2026-09-29
keywords: ["what is a credit rating", "moody's vs s&p rating difference", "investment grade vs junk bond cutoff", "what is sovereign credit rating", "credit rating notching explained", "how to read a corporate bond rating", "credit rating agency conflict of interest"]
seo_audited: 2026-09-30
---

## The First Time Since 1917: The US Loses AAA From All Three Raters

The US Treasury hadn't lost a top rating since 1917 — until S&P cut it in 2011, Fitch followed in 2023, and Moody's, the last holdout, finally downgraded it in May 2025. None of the three was calling US default likely. Their shared reason was that government debt and interest-payment ratios had been climbing faster, for longer, than those of other countries holding similarly high ratings. Watching the world's supposedly safest borrower get marked down by all three major raters raises an obvious question: what exactly are those letter grades measuring, who decides them, and through what process?

## What a Credit Rating Actually Measures: Default Probability Times Recovery

A credit rating scores the likelihood that a specific borrower — a company or a government — will repay what it owes, on time and in full. The most common misunderstanding to clear up first: a credit rating says nothing about whether a company's stock will go up, or whether its business is thriving. It answers exactly one question — will the holder of this bond get their principal and interest back? — and that question actually splits into two components. One is **probability of default**: how likely is it that this borrower actually fails to pay. The other is **recovery rate**: even if default happens, what fraction of the money can bondholders still recoup through collateral or liquidation. Because recovery rates differ depending on whether a specific bond is senior or subordinated, secured or unsecured, ratings can — and often do — differ across different bonds from the very same issuer, which is the notching mechanic covered further down.

## The Rating Scale: 22 Alphabetic Notches, 21 Numeric-Suffix Notches

The three major agencies — Moody's, S&P, and Fitch — use different notation but a similar underlying structure. S&P and Fitch top out at AAA and step down through AA, A, BBB, BB, B, and CCC to D (default, meaning an actual missed payment), adding a "+" or "−" from AA through CCC for 22 total notches. Moody's tops out at Aaa instead, stepping down through Aa, A, Baa, Ba, B, and Caa to C, adding a 1/2/3 numeric suffix from Aa through Caa for 21 notches (Aa1 sits one notch above Aa2, for instance). The notation differs, but in practice S&P's BBB+ is treated as equivalent to Moody's Baa1, and BBB- as equivalent to Baa3.

The single most consequential line on this whole scale sits right at **BBB-/Baa3**. Everything at or above that line is **investment grade**; everything below it is **speculative grade** — commonly called high-yield or junk. That one-notch gap matters far more in practice than the raw rating number suggests. Pension funds, insurers, and many bond funds operate under mandates or regulatory rules that restrict them to investment-grade holdings only, so when a bond drops from BBB- to BB+ — becoming what the market calls a "fallen angel" — those institutions are often forced to sell all at once just to stay compliant, regardless of what they personally think the bond is worth. That's exactly what happened to Ford: Moody's cut it to junk (Ba1) in September 2019, and S&P followed with its own cut to BB+ in March 2020 as COVID slammed the auto industry, making Ford the largest fallen angel on record at the time — funds restricted to investment-grade paper dumped Ford bonds en masse, and the price fell by more than the single-notch downgrade alone would suggest. As covered in [credit spreads](/en/basics/credit-spreads-explained/), lower ratings also structurally widen the interest-rate premium investors demand.

## How a Rating Actually Gets Built: Hard Numbers Plus Judgment Calls

Rating agencies combine quantitative metrics pulled straight from the financial statements with qualitative judgment that doesn't reduce cleanly to a number. On the quantitative side, they look at things like the [interest coverage ratio](/en/basics/interest-coverage-ratio-zombie-company/), debt-to-equity, debt relative to operating cash flow, and earnings volatility versus industry peers — a set of inputs that overlaps heavily with what the [Altman Z-Score](/en/basics/altman-z-score-bankruptcy-risk/) uses. The difference is that the Z-Score is a published formula that spits out a number mechanically, while a credit rating layers judgment on top: how structurally competitive is the industry, how aggressive is management's appetite for debt-funded M&A versus conservative balance-sheet management, what governance risks exist, and whether a parent company or government might step in with implicit support. An analyst committee weighs all of this before settling on a final rating — which is exactly why two companies that look nearly identical on paper can still land on different ratings.

A rating is also built **through-the-cycle** rather than reacting to any single data point. Rather than cutting a rating the moment one quarter disappoints, agencies ask whether the borrower can still support that rating across a few years of normal economic ups and downs. That's why rating changes move far more slowly and deliberately than daily market prices like a stock or a [CDS premium](/en/basics/credit-default-swap-cds/) — typically on a cadence of months to a year, not days.

## Notching: Why One Company's Bonds Can Carry Different Ratings

Everything above describes "the issuer's rating," but a single company issuing several kinds of bonds ends up with several different ratings, one per instrument. The mechanic governing that spread is called **notching**. It starts from a baseline rating — usually the senior unsecured rating — and adjusts up or down depending on how early and how completely each specific instrument would get paid back in a default. Under a simplified version of Moody's public guidelines, if senior unsecured debt sits at the baseline, senior secured debt (backed by collateral) sits one notch above it, subordinated debt sits one notch below it, and preferred stock sits two notches below. So a company with a baseline rating of A might see its secured bonds land at A+, its unsecured senior bonds at A, and its subordinated bonds around A-. The notch spread is usually capped near ±2, though it can widen further when the gap in expected recovery is unusually large. The practical takeaway: when a headline says "this company's rating is A," it's worth checking which specific instrument that refers to, since the same issuer can carry several different ratings at once.

## Sovereign Ratings: Often a Ceiling on Corporate Ratings

A sovereign rating scores a government's ability to repay its own domestic- and foreign-currency debt, built from fiscal health, growth prospects, political stability, foreign-exchange reserves, and the structure of external debt — and, as the US case shows, it can be downgraded too. The key related concept here is the **sovereign ceiling**: in many emerging markets, even a company with an unusually strong balance sheet typically can't be rated above its own government, because it shares exposure to country-level risks like capital controls or a currency crisis that would hit every domestic issuer at once. That ceiling isn't absolute, though — a small number of multinational companies with overwhelmingly foreign revenue, or foreign assets and cash flows capable of servicing debt independent of the home country, do get rated above their sovereign as an exception.

## The Conflict of Interest: Why the Rated Company Pays for Its Own Rating

The rating industry runs on a structural conflict of interest. Under the **issuer-pays model** — the industry standard — the company or government being rated is the one paying the agency's fee, not the investors who rely on the rating. That arrangement creates an obvious incentive: a more generous rating keeps the issuer happier and more likely to come back for the next bond deal. This dynamic showed up most dramatically in the 2008 financial crisis, when a large share of mortgage-backed structured products built from subprime loans carried ratings far higher than their actual risk warranted — and when the housing market collapsed, the resulting wave of downgrades and investor losses became one of the crisis's central amplifying mechanisms. Regulators tightened oversight afterward — the US through Dodd-Frank, Korea through a 2009 overhaul of its Credit Information Act — but the underlying structure, where the rated party foots the bill, remains largely intact today. That history is exactly why it's safer to treat a rating as one input rather than the whole picture, cross-checking it against a market-priced signal like the [CDS premium](/en/basics/credit-default-swap-cds/) that updates continuously rather than periodically.

## Korea's Domestic Bond Market: Its Own Set of Raters

Korean-listed companies issuing won-denominated corporate bonds or commercial paper rely mainly on domestic agencies — Korea Ratings, NICE Investors Service, and Korea Investors Service — rather than Moody's or S&P. Their notation (AAA through D, with +/- refinements from AA through B) closely mirrors the global three, but because they're rating domestic won-denominated obligations, they operate independently of the foreign-currency sovereign-ceiling logic that applies to Moody's and S&P ratings. As covered in [capital structure theory (Modigliani-Miller)](/en/basics/capital-structure-modigliani-miller/), a single-notch downgrade immediately raises the rate a company pays on its next bond issuance — which means a domestic rating action feeds directly into financing costs for anything from routine corporate refinancing to a heavily leveraged deal like an [LBO](/en/basics/leveraged-buyout-lbo-explained/).

## Takeaway

- A credit rating measures whether a borrower will repay on time, combining default probability and recovery rate — it says nothing about a company's stock or business prospects.
- S&P and Fitch use a 22-notch AAA-to-D scale; Moody's uses a 21-notch Aaa-to-C scale, with the BBB-/Baa3 line separating investment grade from speculative grade (junk).
- Ratings combine quantitative metrics like the interest coverage ratio with qualitative judgment on industry risk and management behavior, assessed through-the-cycle rather than off any single data point.
- Notching means a single issuer's bonds can carry different ratings depending on seniority and collateral — Ford's 2019-2020 fall to junk shows how a single-notch cut can trigger forced institutional selling.
- The issuer-pays model creates a structural conflict of interest that contributed to the 2008 crisis, and Korean won-denominated bonds are rated mainly by domestic agencies rather than the global three.

## FAQ

### Does a high credit rating mean the stock is a good investment too?
No. A credit rating only measures the likelihood that bondholders get repaid. A company can carry a very high rating because its balance sheet is rock-solid while its stock goes nowhere for lack of growth, and a lower-rated growth company's stock can still perform very well. Bond investors and equity investors are evaluating fundamentally different things.

### Do Moody's, S&P, and Fitch ever disagree on the same issuer?
Yes — this is called a "split rating," and it happens when the agencies weigh industry risk or financial policy differently. Split ratings show up most often for issuers sitting right at the investment-grade/junk boundary, which is exactly why it's worth checking more than one agency's rating rather than relying on a single source.

### Should I avoid junk-rated (speculative-grade) bonds entirely?
Not necessarily. Speculative-grade bonds carry higher default risk but compensate with a higher yield (spread), and some institutional investors deliberately allocate to this segment as its own diversified asset class. For an individual investor, though, picking single junk bonds directly carries meaningful principal-loss risk if a default hits — checking repayment capacity with a metric like the [interest coverage ratio](/en/basics/interest-coverage-ratio-zombie-company/), or using a diversified high-yield fund instead of individual bonds, is generally the safer route.

> ⚠️ This article is for informational and educational purposes only and is not a recommendation to buy or hold any specific bond or security. Rating scales and methodologies vary by agency and change over time — check the latest disclosures from the relevant rating agency and issuer before making any investment decision.
