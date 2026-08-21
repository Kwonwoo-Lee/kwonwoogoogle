---
slug: roic-vs-wacc-value-creation
title: "ROIC vs WACC: How to Tell If a Company Is Actually Creating Value"
description: "Why a company's return on invested capital (ROIC) has to clear its cost of capital (WACC) to create real value, the economic spread concept behind it, and why ROE can mislead."
order: 32
updated: 2026-08-21
keywords: ["what is ROIC", "ROIC vs WACC", "what is WACC", "return on invested capital explained", "economic value added EVA", "how to calculate ROIC", "value creation vs value destruction", "ROIC vs ROE"]
---

## A Profitable Company Isn't Automatically a Value-Creating One

As covered in [Financial Statement Basics](/en/basics/financial-statement-basics/), rising net income and a strong ROE usually get read as "this company is doing well." But there's a question missing from that read: how much capital did it take to produce that profit in the first place? A company that puts $10 billion to work and earns $1 billion back has a 10% return. A company that puts $20 billion to work and earns the same $1 billion has a 5% return — half as good. Looking only at the size of the profit, both companies look identical: "a company that earned $1 billion." How efficiently each one used its capital to get there is a completely different story.

There's a deeper question underneath that one, too: how do you know whether that 5% or 10% return is actually good enough? [What Is Discounted Cash Flow (DCF)?](/en/basics/discounted-cash-flow-dcf/) introduced **WACC (Weighted Average Cost of Capital)** as the discount rate used to value future cash flows — and it turns out WACC is exactly the benchmark that answers this question too. This lesson covers **ROIC (Return on Invested Capital)**, the metric that shows how efficiently a company actually turns capital into profit, and why lining ROIC up against WACC is how you answer the question "is this company creating value, or quietly destroying it?"

## What ROIC Measures: Profit Per Dollar Actually Put to Work

**ROIC (Return on Invested Capital)** measures after-tax operating profit relative to the capital a company has actually deployed in its operations.

```
ROIC = Net Operating Profit After Tax (NOPAT) ÷ Invested Capital
```

The numerator, **NOPAT**, is operating profit after tax — calculated before interest expense. That's deliberate: it isolates how much the operating business itself earns, independent of how much debt the company carries. The denominator, **Invested Capital**, is the capital actually raised to fund operations — generally interest-bearing debt plus shareholders' equity, minus non-operating cash the business isn't actually using. In short, ROIC compresses "however this business is funded — debt or equity — what after-tax return did the capital sunk into it actually generate?" into a single number.

Say a manufacturer has $1 billion invested across plants, equipment, and working capital, and generates $120 million in NOPAT. Its ROIC is 12%. That figure isn't distorted by how the capital was raised or by one-off accounting items — it's a clean read on how efficiently the operating business itself compounds capital.

## Revisiting WACC: The Bar That Return Has to Clear

A 12% ROIC doesn't tell you, on its own, whether that's good or bad. Judging that requires a benchmark — and that benchmark is the same **WACC (Weighted Average Cost of Capital)** covered as the discount rate in [What Is DCF?](/en/basics/discounted-cash-flow-dcf/).

```
WACC = (equity weight × cost of equity) + (debt weight × after-tax cost of debt)
```

WACC is the minimum return the people funding the company — shareholders and lenders — require on average. As covered in [What Is Beta?](/en/basics/beta-and-volatility/), shareholders demand a return that reflects the stock's volatility relative to the market (its beta), while lenders require roughly the interest rate the company actually pays, adjusted for the tax benefit. Blend the two by capital structure weight, and WACC is the break-even bar: the minimum a company has to earn before it stops shortchanging the people who financed it. Assume this manufacturer's WACC works out to 8%.

## Why ROIC Has to Clear WACC for Value to Actually Be Created

This is the core idea of the lesson. The gap between ROIC and WACC is called the **economic spread**.

```
Economic spread = ROIC − WACC
```

- **ROIC > WACC**: the company earns more than it costs to fund itself. In this state, every additional dollar reinvested into growing the business adds more shareholder value.
- **ROIC < WACC**: the company's return doesn't even cover what it costs to raise capital. It can still show an accounting profit — but economically, it's destroying value. A company in this state that keeps pouring capital into expansion destroys more value the more it grows.

This is exactly what a positive net income figure alone can't tell you. A company can be profitable on paper and still be losing money in the economic sense, if that profit falls short of what its capital actually costs. This idea has a formal name in practice: **Economic Value Added (EVA)** — the economic spread multiplied by invested capital, expressing in dollar terms how much new value a company actually created after accounting for the cost of the capital it used.

```
EVA = (ROIC − WACC) × Invested Capital
```

## Comparing Two Companies, Side by Side

Take two companies, A and B, in the same industry, both profitable, with similar headline net income.

| | Company A | Company B |
|---|---|---|
| Invested capital | $1.0B | $1.0B |
| NOPAT | $150M | $70M |
| ROIC | 15% | 7% |
| WACC | 8% | 8% |
| Economic spread | +7pp | -1pp |
| EVA | +$70M | -$10M |

Company A's ROIC of 15% clears its 8% WACC comfortably, generating roughly $70M a year in genuine new value after covering its cost of capital. Company B's ROIC of 7% falls short of its 8% WACC — meaning that even though it's profitable on the income statement, it's quietly destroying about $10M of shareholder value every year. If Company B announces a big new capex program to expand capacity, that can sound like a growth story on the surface — but if that spread holds, expansion just destroys value faster. This is exactly why institutional investors and analysts checking a company's "quality" of earnings look at the relationship between ROIC and WACC as closely as they look at the net income growth rate itself.

## Why ROIC and ROE Can Tell Different Stories

**ROE**, covered in [Financial Statement Basics](/en/basics/financial-statement-basics/), and ROIC both look like "return" metrics, but they use different denominators. ROE divides net income by shareholders' equity alone; ROIC divides NOPAT by total invested capital — equity plus debt. That difference creates a real distortion.

Taking on more debt — increasing leverage — shrinks the equity denominator, which can push ROE up arithmetically even if the underlying operating business hasn't gotten any more efficient. As covered in [Margin Trading and Leverage](/en/basics/margin-trading-leverage/), leverage amplifies returns for an individual investor — and the exact same mechanism plays out inside a company's own balance sheet. ROIC, by contrast, includes both debt and equity in its denominator, so leverage alone can't inflate the number. A highly leveraged company posting an impressive ROE isn't automatically running an efficient operation — it may just be a leverage illusion. Checking ROIC alongside ROE is how you tell whether that profitability is real operating strength or simply more borrowed money at work.

## A High ROIC Isn't the Whole Story — How Long Does the Spread Last?

There's a piece of this that's easy to miss: what matters more for long-term company value than today's spread is how long that spread can be sustained. A company can post a 30% ROIC temporarily on the back of some new technology or patent — but if the industry has low barriers to entry, competitors pile in, price competition erupts, and that spread often collapses back toward WACC within a few years. Companies with a strong brand, network effects, or high switching costs — the ingredients of what's commonly called an "economic moat" — can defend a wide spread for much longer. Recall from [What Is DCF?](/en/basics/discounted-cash-flow-dcf/) that most of a company's valuation rests on distant future cash flows captured in terminal value — which means the real question for long-term valuation isn't "what's ROIC today?" but "how long can this spread hold up against competition?"

It's also worth remembering that a "normal" ROIC level varies a lot by industry. Software and branded consumer goods businesses, which need relatively little capital investment, structurally tend to run high ROIC. Capital-intensive industries like semiconductors, steel, or airlines — which require constant, heavy reinvestment just to keep operating — structurally run lower. That makes ROIC most useful for comparing companies within the same industry, or tracking how one company's ROIC trends over time, rather than comparing it directly across industries with very different capital needs.

## Takeaway

- ROIC divides after-tax operating profit (NOPAT) by invested capital (debt plus equity), measuring how efficiently a company turns capital into profit.
- WACC is the minimum return the company's shareholders and lenders require — the benchmark that tells you whether an ROIC is actually "good enough."
- When ROIC exceeds WACC (a positive economic spread), the company creates value; when ROIC falls short (a negative spread), it's destroying value economically even while showing an accounting profit.
- ROE can rise purely from added leverage with no improvement in operating efficiency — checking it alongside ROIC separates real profitability from a leverage illusion.
- A high ROIC alone isn't the full picture; what matters more for long-term value is how long that spread can survive competition — a function of the company's economic moat.

## FAQ

### How is ROIC different from ROA?
ROA (Return on Assets) divides net income by total assets, including non-operating assets like excess cash or investment holdings. ROIC's denominator includes only capital actually deployed in operations, which makes it a more precise read on how efficiently the core business itself uses capital.

### Where can I find ROIC and WACC figures for a stock?
Brokerage research and financial data platforms often publish calculated ROIC figures for individual companies. WACC isn't a standardized disclosure item — it's an estimate, so figures can differ across data providers depending on the beta and cost-of-debt assumptions each one uses.

### Is it safe to assume a company is fine as long as ROIC is even slightly above WACC?
The size and durability of the spread matter more than the fact that it's positive. A very thin spread can flip negative with even a mild downturn in the business, and in a highly competitive industry, today's spread may not last. It's worth weighing both the size of the spread and whether the company has a structural advantage that can keep competitors from eroding it.

> ⚠️ This article is for informational purposes only and is not investment advice. You are solely responsible for your own investment decisions.
