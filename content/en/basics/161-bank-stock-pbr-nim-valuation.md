---
slug: bank-stock-pbr-nim-valuation
title: "Why Bank Stocks Trade on P/B, Not P/E — How ROE and NIM Drive the Discount"
description: "Why bank stocks trade at 0.3-0.5x book value instead of on P/E, explained through the ROE-vs-cost-of-equity relationship and how net interest margin (NIM) drives a bank's ROE."
order: 161
updated: 2026-10-24
keywords: ["why do bank stocks trade below book value", "bank stock P/B ratio explained", "what is NIM", "net interest margin explained", "bank stock valuation", "ROE vs cost of equity", "P/B ratio of 1", "bank valuation metrics"]
seo_audited: 2026-10-24
---

## Why Analysts Lead With P/B, Not P/E, on Bank Stocks

Open an analyst note on a major bank and P/B almost always comes before P/E. Headlines like "bank stocks near record-low 0.4x book value" are common. As the [P/E, P/B, and P/S](/en/basics/valuation-multiples-per-pbr-psr/) lesson explained, P/B divides the share price by book value per share, so a P/B of 0.4x means the market is pricing the bank's equity at just 40% of what its balance sheet says it's worth. That's the market marking down the same dollar of capital by 60% simply because a commercial bank, rather than some other business, happens to hold it. Why does this discount show up so persistently, and specifically in banking? The answer starts with the fact that a bank's underlying balance sheet works fundamentally differently from a typical manufacturer or service company.

## Why Banks Are Valued on Book, Not Enterprise Value

As the [enterprise value vs. equity value](/en/basics/enterprise-value-vs-equity-value/) lesson explained, a normal company's enterprise value is market cap plus net debt — debt treated as just one financing choice among several. That framework breaks down for banks. A bank's "liabilities" are mostly customer deposits, and deposits function less like financing and more like raw material the bank buys in order to manufacture its real product: loans. Much like a manufacturer buys raw materials and sells finished goods, a bank gathers deposits at a funding cost and converts them into loans at a lending rate, pocketing the spread. Under this structure, enterprise value stops meaning anything useful — adding tens of billions of dollars of deposits into an "enterprise value" calculation has nothing to do with how a bank actually generates profit. That's why banks and insurers are valued through P/B and ROE directly, rather than through EV/EBITDA or EV/Revenue multiples built for ordinary operating businesses.

## The Bridge Between P/B and ROE: Cost of Equity

So why does P/B vary so much across banks and across time? The key is that P/B is really a compressed signal of whether a bank earns more than its cost of equity. Extending the logic from the [dividend discount model](/en/basics/dividend-discount-model-ddm/) to the whole equity base gives a rough approximation:

```
Fair P/B ≈ 1 + (ROE − Cost of Equity) / (Cost of Equity − Long-run Growth Rate)
```

Cost of equity (COE), typically estimated with [CAPM](/en/basics/capital-asset-pricing-model-capm/), is the minimum return shareholders demand for bearing that level of risk. If a bank's ROE exactly equals its cost of equity, the term in parentheses collapses to zero and fair P/B falls to exactly 1x — holding the capital outright and deploying it in the business create identical value for shareholders. When ROE exceeds cost of equity, fair P/B rises above 1x; when ROE falls short of cost of equity, fair P/B drops below 1x. In other words, a P/B below 1 isn't necessarily the market "leaving a bargain on the table" — it can be a blunt signal that the bank isn't even clearing the minimum return shareholders require. Many bank holding companies post ROE in the high single digits to low teens, below commonly estimated costs of equity for bank equity risk, and that gap alone explains much of why bank P/B ratios have structurally sat under 1x for extended stretches.

## What Actually Drives a Bank's ROE: Net Interest Margin (NIM)

So what determines a bank's ROE? Using the [DuPont](/en/basics/dupont-analysis-roe-decomposition/) framework, ROE breaks down into net margin, asset turnover, and leverage (assets relative to equity). For a bank, the single biggest driver of that net margin is **Net Interest Margin (NIM)** — the spread between interest earned on assets like loans and bonds and interest paid on funding like deposits, scaled to the size of the interest-earning asset base:

```
NIM = (Interest Income − Interest Expense) / Average Interest-Earning Assets
```

In plain terms, it's the "spread" between what a bank pays depositors and what it charges borrowers, divided by how much of that spread-earning business it's running. Because banks apply this narrow spread to an enormous asset base — often 10 to 30 times the size of their equity — even a 0.1 percentage point move in NIM gets amplified into a much larger swing in net income. That's why the interest rate cycle is one of the most direct levers on bank stock valuation. When policy rates rise, loan rates typically reprice faster and sooner than deposit rates, which tends to widen NIM — pushing ROE up and, through the formula above, fair P/B up with it. When rates fall sharply or deposit competition intensifies, NIM compresses and both ROE and P/B come under pressure.

## A Worked Example: How Much Does 0.1 Points of NIM Move ROE and P/B?

A hypothetical bank makes the amplification concrete. Say Bank A holds $7 billion of equity and $210 billion of interest-earning assets — a 30x ratio that reflects how deposit funding lets a bank run assets far larger than its own capital base. Compare NIM at 1.80% versus a 0.1-point drop to 1.70%:

| | NIM 1.80% | NIM 1.70% |
|---|---|---|
| Interest-earning assets | $210B | $210B |
| Net interest income (NIM × assets) | $3.78B | $3.57B |
| Net income after other costs (simplified) | $2.10B | $1.99B |
| Equity | $7B | $7B |
| ROE | 30.0% | 28.4% |

The net income figures here simplify away a real bank's staffing, overhead, and credit-loss costs, but even in this simplified version, a NIM drop of just 0.1 points — roughly a 5.6% relative decline — translates almost one-for-one into a 5.6% decline in net interest income and the net income tied to it. That's the 30x leverage transmitting a small NIM move almost undiluted into the bottom line. If this bank's cost of equity is 9%, plugging ROE of 28.4% versus 30% into the fair-P/B formula above produces a meaningfully different multiple from a change that, on its face, looks tiny. That amplification is exactly why bank analysts obsess over NIM to two decimal places every quarter, often before they even get to net income.

## Why Korean Bank Stocks Trade Even Lower

The same framework applies worldwide, but Korean bank holding companies have tended to trade at notably lower P/B than their U.S., Japanese, or U.K. peers. A few factors stack on top of the basic ROE-versus-COE math. First, Korean banks skew unusually heavily toward net interest income, with fee and wealth-management income making up a smaller share than at many global peers — leaving earnings more exposed to the rate cycle and perceived as lower quality by the market. Second, during downturns like the COVID-19 period, banks themselves often aren't hit directly; instead the market prices in the risk that the businesses and households that borrowed from them will struggle, hitting banks with heavier exposure to small-business and household lending especially hard, ahead of any actual deterioration in the bank's own numbers. Third, the chronically low shareholder returns (dividends plus buybacks) discussed in the [Korea discount](/en/basics/korea-discount-value-up-program/) lesson apply directly to banks too — a bank that retains most of its earnings as capital rather than returning it gets discounted more heavily even at a similar ROE. That said, Korean bank holding companies have increasingly announced plans to raise shareholder returns under the government's Value-Up Program in recent years, and part of the market's current re-rating reflects expectations that this gap will narrow going forward.

## Does the Same Logic Apply to Insurers and Brokers?

Not identically, but with a similar underlying reason. Insurers also get valued on P/B and ROE, because premiums collected from policyholders — recorded as liabilities like reserves and contractual service margins — function as raw material the insurer invests, much like a bank's deposits. The mechanism differs, though: instead of NIM, an insurer's ROE is driven mainly by its loss ratio and expense ratio — essentially, whether claims and costs come in lower than priced for. Brokers sit at the other extreme, running trading and lending books with proportionally more of their own capital and less deposit-style leverage, which makes their ROE swing more with fee income (brokerage and investment banking) tied to market activity than with a spread metric. The shared thread across all three — liabilities that function as the raw material of the business — is why financials as a sector share the P/B-and-ROE framework, even though the specific driver behind that ROE differs by business line.

## What to Actually Check as an Investor

Applying this framework well means looking past the P/B number itself. Start by checking how many basis points NIM moved quarter-over-quarter and year-over-year in the latest earnings release, and whether that direction matches the broader rate cycle. Next, track whether ROE is converging toward the bank's own stated medium-term target or toward a reasonable cost-of-equity estimate — a P/B persistently below 1x while ROE sits below cost of equity is the structurally expected outcome, not necessarily a bargain, so it's worth asking whether there's a credible path (NIM expansion, fee income growth, cost discipline) for ROE to actually close that gap. Finally, track the trend in shareholder returns (payout ratio plus buybacks): at a comparable ROE, a bank raising its payout has more room for its discount to narrow than one that isn't.

## Key Takeaways

- Because a bank's deposits function as raw material for its business rather than financing, enterprise value doesn't apply cleanly — banks are valued through P/B tied directly to ROE instead of EV/EBITDA.
- Fair P/B is driven by the gap between ROE and cost of equity: P/B equals roughly 1x when ROE matches cost of equity, and falls below 1x when ROE falls short.
- Net interest margin (NIM) is the single biggest driver of a bank's ROE, and because deposit funding lets banks run highly leveraged balance sheets, small NIM moves amplify into much larger ROE and P/B swings.
- Korean bank stocks have traded at a deeper discount than global peers due to heavy reliance on net interest income, high sensitivity to credit-sensitive lending in downturns, and historically low shareholder returns.
- A low P/B isn't automatically a bargain — it matters whether ROE can realistically exceed cost of equity and whether shareholder return policy is improving.

## FAQ

### Does a P/B below 1 always mean a bank stock is undervalued?
Not necessarily. If ROE is below cost of equity, a P/B under 1x can be a rational price rather than a bargain. Rather than looking at P/B alone, check whether that bank's ROE is clearing (or has a credible path to clearing) its cost of equity.

### Can bank stocks be compared using P/E instead?
It's possible but typically only as a secondary check. Because banking's income statement — driven by net interest income and loan-loss provisions — differs structurally from ordinary businesses, comparing banks to other sectors purely on P/E can be misleading. P/E is still used for comparisons within the sector, but P/B paired with ROE remains the more common lens for capturing capital efficiency.

### If NIM rises, does the stock always go up?
NIM expansion is generally positive for ROE but it isn't the only variable. Rate hikes that widen NIM often coincide with slowing loan demand or rising delinquencies, and the resulting increase in loan-loss provisions can offset some or all of the NIM benefit.

### Are bank holding companies valued the same way as the bank itself?
Broadly similar, but not identical. A financial holding company bundles in non-bank subsidiaries — brokerage, insurance, card lending — so its overall ROE depends on more than just the banking subsidiary's NIM. A more precise read of a holding company's P/B separates out how much of its ROE comes from the banking arm versus the non-bank subsidiaries.

> ⚠️ This article is for informational purposes only and is not investment advice. Any company names mentioned are illustrative examples only, not buy or sell recommendations. Investment decisions and their outcomes are the sole responsibility of the investor.
