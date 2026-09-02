---
slug: reit-ffo-valuation
title: "What Is FFO for REITs? — Why P/E Fails and P/FFO/AFFO Works"
description: "Why REIT net income understates real cash generation because of depreciation, how to calculate FFO and AFFO, and how P/FFO and cap rates are used to value REITs instead of P/E."
order: 57
updated: 2026-09-02
keywords: ["what is FFO", "FFO REIT", "FFO vs AFFO", "REIT valuation", "REIT P/E ratio", "cap rate REIT", "capitalization rate explained", "REIT net asset value NAV"]
seo_audited: "2026-09-02"
---

## The Dividend Yield Looks Great — So Why Is the P/E So Ugly

If you've been screening for [dividend portfolios](/en/basics/dividend-portfolio-criteria/), REITs (Real Estate Investment Trusts) show up constantly, often with dividend yields of 5–7% or more. But pull up the P/E ratio on the same stock and it can read 30, 40, sometimes 50-plus — numbers that would look alarmingly expensive on an ordinary company. Is the REIT overpaying its dividend relative to what it actually earns, or is something wrong with the P/E itself? The answer is the P/E. A REIT's GAAP net income is structurally designed to understate its real cash-generating power. This lesson covers why that distortion happens, and why — if you've already covered [P/E, P/B, P/S, and EV/EBITDA](/en/basics/valuation-multiples-per-pbr-psr/) — REITs need an entirely different set of metrics: FFO (Funds From Operations) and AFFO (Adjusted FFO).

## Depreciation: A "Phantom Expense"

When a manufacturer buys factory equipment, that equipment wears out and eventually needs replacing, so accounting rules require depreciating its cost over its useful life — a reasonable proxy for real value loss. REITs, though, mostly hold buildings. Real estate does age physically, but well-located, well-maintained property often holds its value or even appreciates over time, unlike a straight-line depreciation schedule assumes. Accounting rules nonetheless require REITs to depreciate buildings the same way factories depreciate machinery. The result is a large annual expense on the income statement that doesn't correspond to any actual cash leaving the business. NAREIT, the U.S. REIT industry association, calls this a "phantom expense" — recurring, but disconnected from the company's real operating performance. Since depreciation is typically a REIT's single largest expense line, unadjusted net income (and EPS) can badly understate — sometimes even turn negative — what is otherwise a healthy, cash-generative business. That's the root cause of the abnormally high P/E ratios REITs often show.

## FFO: Adding the Phantom Expense Back

To correct this distortion, the U.S. REIT industry standardized a metric in the early 1990s called **FFO (Funds From Operations)**:

```
FFO = Net Income
    + Depreciation & amortization of real estate assets
    − Gains on property sales
    + Losses on property sales
```

The logic is straightforward: start from net income, add back the non-cash depreciation charge, and strip out one-time gains or losses from property sales, since those don't recur. What's left is much closer to the cash a REIT's core leasing business generates year after year. FFO is a recognized non-GAAP metric under SEC rules, and nearly every REIT reports it alongside net income in its earnings releases.

One common point of confusion: FFO is not the same figure as "cash flow from operations" on the cash flow statement. Cash flow from operations is a formal accounting line that reflects many more adjustments, including working-capital changes. FFO is a REIT-specific, non-GAAP reconciliation that starts from net income and adjusts only for real estate depreciation and property-sale gains/losses. The two numbers serve different purposes and rarely match.

## AFFO: Refining FFO One Step Further

FFO isn't perfect either. Two further adjustments produce **AFFO (Adjusted FFO)**.

The first is recurring capital expenditure. Separate from depreciation, buildings need ongoing real spending — roof replacements, HVAC repairs, tenant-improvement costs — just to stay competitive. FFO ignores this entirely, so AFFO subtracts it back out.

The second is a straight-line rent adjustment. Accounting rules require multi-year leases with built-in annual rent escalations to be recognized evenly across the lease term, even though the actual cash received is lower in early years and higher in later years. AFFO removes the portion of straight-lined rent that hasn't actually been collected yet in cash, bringing the number closer to real cash received during the period.

Unlike FFO, there's no single industry-standard formula for AFFO — the exact adjustments vary by company, so comparing AFFO across REITs means checking each company's earnings materials for what it actually adjusted. Even so, because AFFO tracks distributable cash more closely than FFO does, it's often the metric analysts lean on first when judging whether a REIT's dividend is sustainable.

## Why P/FFO Replaces P/E

Back to the opening question. If net income is systematically distorted by depreciation, then P/E — which uses net income as its denominator — inherits that distortion. So the industry compares REITs using **P/FFO** (share price ÷ FFO per share) instead of P/E, or more precisely **P/AFFO**. The logic is identical to P/E — "how many years of annual earnings does the price represent" — just with the earnings figure corrected for real estate accounting.

A quick illustration with a hypothetical REIT. Say EPS is $0.50 and the share price is $20 — that's a P/E of 40, which looks expensive. But suppose $1.20 per share of real estate depreciation was already subtracted to get that EPS, and there were no property-sale gains this year. FFO per share is then $0.50 + $1.20 = $1.70, and P/FFO is $20 ÷ $1.70 ≈ 11.8x — a completely different picture from the P/E of 40. That gap is exactly why P/E misleads for REITs. Subtract another $0.30 per share of recurring capex and AFFO comes to $1.40, putting P/AFFO around 14.3x. These multiples matter less as absolute numbers and more when compared against a REIT's own historical range or against peers in the same property sector.

## A Second Check: Cap Rate and NAV

FFO and AFFO evaluate the REIT as a stock. The **capitalization rate (cap rate)**, a much older real estate industry tool, evaluates the underlying properties themselves as assets:

```
Cap Rate = Net Operating Income (NOI) ÷ Property Value
```

If an office building generates $1 million in annual NOI and comparable buildings in that market are trading at a 5% cap rate, the implied value of the building is $1M ÷ 5% = $20 million. A lower cap rate means the market is pricing that income stream as safer or more premium (paying more per dollar of income); a higher cap rate implies more perceived risk or a cheaper valuation.

Applying an assumed cap rate to a REIT's total portfolio NOI produces an estimate of what the real estate would be worth in the private market. Subtract liabilities and divide by shares outstanding, and you get **Net Asset Value (NAV) per share**. Comparing NAV to the actual trading price tells you whether the REIT trades at a premium or discount to what its properties would fetch privately. As with [Enterprise Value vs. Equity Value](/en/basics/enterprise-value-vs-equity-value/), this reflects the same underlying idea as [DCF](/en/basics/discounted-cash-flow-dcf/) or the [dividend discount model](/en/basics/dividend-discount-model-ddm/): an asset's value ultimately traces back to the cash flow it produces. Small changes in the assumed cap rate can swing estimated NAV substantially, so this figure is always a range, not a precise number.

## Why Interest Rates Hit REIT Valuations So Hard

As covered in [how interest rates affect stock valuations](/en/basics/interest-rates-and-stock-valuations/), a higher discount rate shrinks the present value of future cash flows — and REITs feel this unusually strongly, for two reasons. First, cap rates themselves tend to move with government bond yields: when bond yields rise, investors demand a higher income return from real estate too, which pushes cap rates up and, for the same NOI, pulls implied property values down. Second, because REITs are required to distribute most of their taxable income as dividends, they typically fund new acquisitions with external borrowing rather than retained earnings. Rising rates raise the interest cost on existing debt and make new borrowing more expensive at the same time. Together, these forces tend to widen REIT discounts to NAV in rising-rate environments and narrow them — sometimes into a premium — when rates fall. FFO and AFFO themselves aren't directly tied to interest rates, but the P/FFO multiple and cap rate assumptions built on top of them are very sensitive to the rate environment.

## Take This With You

An abnormally high P/E on a REIT usually isn't a red flag about the business — it's an artifact of a non-cash expense mechanically depressing net income. FFO corrects for that by adding depreciation back and removing one-time property-sale gains and losses; AFFO goes further, netting out real maintenance spending and straight-line rent distortions to get closer to what's actually distributable as dividends. When comparing REITs, look at P/FFO and P/AFFO instead of P/E, and cross-check with cap-rate-based NAV to see how the share price compares to what the underlying real estate would be worth privately. None of these are formulas for deciding whether to buy or sell a specific REIT — they're tools for making sure you don't judge an entire asset class by a yardstick built for ordinary companies.

## FAQ

### If a REIT pays out more in dividends than its net income, is that a red flag?
Not necessarily. A payout ratio over 100% of net income often looks perfectly sustainable once measured against FFO or AFFO instead. REITs are generally required to distribute most of their taxable income to keep their tax-advantaged status, so paying out more than accounting net income is common and expected for this asset class. What's worth watching is a payout ratio that gets uncomfortably close to, or exceeds, 100% of AFFO — that's a tighter signal of real dividend strain.

### Does looking at FFO alone settle a REIT valuation?
No. FFO and AFFO are a starting point for earnings power, not the whole picture. Asset quality (location, tenant mix, lease maturities), leverage, and interest-rate sensitivity all need separate attention. Checking cap-rate-based NAV alongside FFO multiples helps confirm whether the share price and the underlying real estate value are actually in line.
