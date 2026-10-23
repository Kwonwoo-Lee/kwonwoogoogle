---
slug: ebitda-explained
title: "What Is EBITDA? Why Companies Add Depreciation Back, and Why Buffett Hates It"
description: "How EBITDA adds depreciation back to operating income, why it's used to compare companies, and the capex and leverage it quietly hides from investors."
order: 159
updated: 2026-10-23
keywords: ["what is EBITDA", "EBITDA meaning", "how to calculate EBITDA", "EBITDA vs EBIT", "EBITDA margin explained", "adjusted EBITDA meaning", "EV EBITDA difference"]
seo_audited: "2026-10-23"
---

## "Operating Income Fell, But EBITDA Rose" — How Is That Possible?

During earnings season you'll occasionally see headlines like "operating income declined year-over-year, but EBITDA actually rose." Same company, same quarter — so how can two numbers move in opposite directions? The answer comes down to how each one treats a single line item: depreciation. In capital-intensive industries like telecom, airlines, semiconductors, and shipbuilding, earnings reports and analyst notes often lead with **EBITDA** rather than operating income. This lesson walks through exactly what EBITDA adds and strips out, why it's considered useful for comparing companies, and why critics — Warren Buffett chief among them — have called it a genuinely dangerous number.

## What EBITDA Actually Is — The Formula

EBITDA stands for Earnings Before Interest, Taxes, Depreciation, and Amortization. The most common way to calculate it starts from operating income (EBIT):

```
EBITDA = Operating income (EBIT) + Depreciation + Amortization
```

Depreciation spreads the cost of acquiring tangible assets — factories, equipment, buildings — over their useful life rather than expensing them all at once. Amortization applies the same logic to intangible assets like goodwill or patents. In other words, the entire difference between EBITDA and EBIT is just these two line items. You get the same result working backward from net income:

```
EBITDA = Net income + Tax expense + Interest expense + Depreciation + Amortization
```

Both routes land on the same underlying idea: start with what the business earned from its core operations, then strip out costs that involve no current cash outflow (depreciation and amortization) along with costs that depend heavily on financing choices and jurisdiction (interest and taxes).

## Why It's Used — The Comparability Argument

The case for EBITDA starts with the observation that depreciation isn't an actual cash outflow in the period it's recorded. The cash left the building back when the equipment was purchased; depreciation is just the accounting procedure that spreads that past spending across the asset's assumed useful life. On top of that, depreciation method (straight-line vs. accelerated), assumed useful life, tax rates, and how much debt a company carries all vary widely across companies and countries. Strip all four out, the argument goes, and what's left is the number closest to "what this business earns from its core operations alone." That's why EBITDA became the standard yardstick for comparing competitors with very different capital structures and tax rates, for valuing capital-heavy businesses using [EV/EBITDA](/en/basics/valuation-multiples-per-pbr-psr/), and for private equity firms sizing up a target company's underlying earning power during a deal.

## A Numerical Example — Same EBITDA, Very Different Reality

Comparing two hypothetical companies with identical EBITDA makes the metric's blind spot obvious.

| | Company A (telecom, capital-intensive) | Company B (software, asset-light) |
|---|---|---|
| Revenue | $1.0B | $1.0B |
| Operating income (EBIT) | $100M | $170M |
| Depreciation & amortization | $80M | $10M |
| EBITDA | $180M | $180M |
| Annual capex to maintain operations | $90M | $5M |
| Real cash left after capex | $90M | $175M |

Both companies post identical EBITDA of $180 million. But Company A needs nearly $90 million a year just to keep its network running, while Company B can maintain its business with a handful of servers. The actual cash each company generates after reinvesting in its own operations differs by nearly a factor of two. Judging both companies as "equally profitable" based on EBITDA alone completely misses that gap.

EBITDA margin (EBITDA divided by revenue) comes out to an identical 18% for both companies, which makes them look equally profitable on the surface too. But calculate a "real margin" instead — EBITDA minus maintenance capex, divided by revenue — and Company A comes out to 9% while Company B comes out to roughly 17.5%, nearly double. Comparing EBITDA margins across industries where capex eats up very different shares of revenue makes exactly this kind of reinvestment gap disappear from the numbers entirely.

## Why Buffett Hates It — "Does the Tooth Fairy Pay for Capex?"

Warren Buffett has publicly criticized EBITDA for decades. His most quoted line asks whether management thinks "the tooth fairy pays for capital expenditures" — a jab at how EBITDA treats depreciation as a cost that can essentially be ignored because it's "non-cash." Buffett's point is straightforward: depreciation reflects real cash that was already spent, and the underlying equipment will eventually need to be replaced or repaired, meaning that cash will go back out the door sooner or later. In capital-intensive industries, this reinvestment burden is exactly the "real cost" that EBITDA papers over.

EBITDA also strips out interest expense, which means a heavily leveraged company's EBITDA can look perfectly healthy regardless of how much debt it's actually carrying. As the [interest coverage ratio](/en/basics/interest-coverage-ratio-zombie-company/) lesson shows, it isn't unusual for a company that can barely cover its interest payments out of operating income alone to still post a comfortable-looking ratio once EBITDA is used instead. Finally, because EBITDA isn't a standardized GAAP or IFRS measure but a figure companies construct at their own discretion, IPO prospectuses and high-yield bond offerings have repeatedly drawn scrutiny for presenting "Adjusted EBITDA" that strips out one-time charges, restructuring costs, and even stock-based compensation — making profitability look considerably rosier than it actually is.

The clearest example of how far this "adjusting" can go is WeWork. Ahead of its planned 2019 IPO, the co-working office company's prospectus featured a metric of its own invention called "Community-Adjusted EBITDA," which added back not just interest, taxes, and depreciation, but general and administrative expenses, marketing costs, and even the cost of opening new locations. Wall Street and the financial press tore into the metric as effectively designed so that the more money the company spent, the better it looked — and the IPO was ultimately withdrawn. It's a useful reminder that every time a qualifier gets tacked onto the front of "EBITDA," it's worth asking exactly what that qualifier is hiding.

## Why Lenders and Credit Ratings Rely on EBITDA Too

EBITDA isn't just a number equity investors watch. Banks writing loan agreements and the agencies assigning [credit ratings](/en/basics/credit-rating-agencies-explained/) both lean heavily on net debt divided by EBITDA as their go-to measure of leverage. Loan agreements commonly build in a covenant: if that ratio crosses some threshold — say, 4x or 5x — the lender can demand immediate repayment or raise the interest rate. That creates an obvious incentive problem: a company staring down a covenant breach has every reason to inflate the EBITDA in the denominator. The more aggressively it classifies routine costs as "one-time" and adds them back, the larger EBITDA gets and the safer the leverage ratio looks — which is exactly why it's worth checking whether the EBITDA definition written into a credit agreement matches the plainer EBITDA investors typically calculate, especially for heavily leveraged companies.

## An Unexpected Trap: How Lease Accounting Changes Inflate EBITDA

The rollout of [IFRS 16 lease accounting](/en/basics/ifrs16-lease-accounting-explained/) around 2019 produced another instructive case. Under the old rules, rent paid on leased stores or aircraft was recorded as a single operating expense above the operating-income line. Under the new standard, that same lease cost is split into depreciation on a right-of-use asset and interest on a lease liability — both of which sit below EBITDA. Nothing about the business actually changed, but operating income and EBITDA rose mechanically simply because rent, as an operating expense, shrank on paper. The effect was especially pronounced for retailers and airlines that lease heavily, and it's a clean illustration of how EBITDA can move purely from an accounting rule change rather than any real operational improvement.

## What to Check Alongside EBITDA

None of this makes EBITDA useless — it just means it rarely tells the full story on its own. When it's paired with [enterprise value](/en/basics/enterprise-value-vs-equity-value/) in an EV/EBITDA multiple, it's genuinely useful for comparing companies with different debt loads, but a low multiple doesn't necessarily mean a company's reinvestment needs are also low. Subtracting actual capex from EBITDA gets you closer to free cash flow and fills the gap Buffett pointed to; checking the [interest coverage ratio](/en/basics/interest-coverage-ratio-zombie-company/) based on operating income separately exposes interest burdens that leverage can hide inside a healthy-looking EBITDA figure. And whenever "Adjusted EBITDA" shows up in an earnings presentation, it's worth reading the footnotes to see exactly what's been added back or excluded — if the same type of expense gets excluded quarter after quarter, it's fair to ask whether it's really "one-time."

## Key Takeaways

- EBITDA adds depreciation and amortization back to operating income, and is used to compare companies with different capital structures, tax rates, and depreciation methods.
- Depreciation isn't a current cash outflow, but the underlying equipment still eventually needs replacing or repairing — the reinvestment burden doesn't actually disappear.
- Warren Buffett has long criticized EBITDA for masking both capital expenditures and interest burden (leverage) at the same time.
- Because EBITDA isn't a standardized GAAP/IFRS measure, companies have discretion to construct "Adjusted EBITDA" figures that exclude costs at will — always check what's been adjusted out.
- Pairing EBITDA with EV/EBITDA, actual capex, and the interest coverage ratio keeps you from missing the reinvestment needs and leverage risk that EBITDA alone can't show.

## FAQ

### What is EBITDA margin?
EBITDA margin is EBITDA divided by revenue — it shows how much cash-like operating profit a company generates per dollar of sales. It's commonly used to compare cost structures and profitability within the same industry, but it's not well suited to comparisons across industries with very different capital-intensity profiles.

### Should I trust EBITDA or net income more?
They answer different questions. Net income reflects what's actually left for shareholders after interest, taxes, and depreciation are all accounted for. EBITDA shows something closer to core operating cash generation before those are deducted. Rather than relying on just one, it's more useful to look at where the gap between them comes from — is it interest burden, or is it the size of depreciation?

### Should EBITDA be applied the same way across every industry?
No. In asset-light businesses like software and services, where capex and depreciation are minor, the gap between EBITDA and operating income is small and distortion is limited. In capital-intensive industries like telecom, airlines, semiconductors, and shipbuilding, where capex is large relative to revenue, EBITDA can meaningfully mask reinvestment needs and should be interpreted with more caution.

> ⚠️ This article is for informational purposes only and is not investment advice. The company examples in this article are hypothetical illustrations used to explain the concept and do not represent any real company or actual financial figures. Investment decisions and their outcomes are the sole responsibility of the investor.
