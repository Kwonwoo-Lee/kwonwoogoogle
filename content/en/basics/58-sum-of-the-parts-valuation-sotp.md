---
slug: sum-of-the-parts-valuation-sotp
title: "What Is Sum-of-the-Parts (SOTP) Valuation? — Grading Each Business Unit on Its Own Curve"
description: "Why applying one P/E multiple to a multi-segment conglomerate misprices it, and how SOTP values each business unit separately before adding them back together, shown with numbers."
order: 58
updated: 2026-09-03
keywords: ["sum of the parts valuation", "SOTP valuation explained", "how to value a conglomerate", "conglomerate discount", "SOTP price target", "valuing multi-segment companies", "SOTP vs DCF", "holding company SOTP"]
seo_audited: 2026-09-03
---

## Why Do Analyst Reports Say "SOTP Price Target"?

Read enough equity research on a diversified conglomerate — one company running, say, semiconductors, batteries, telecom, and content businesses under one roof — and you'll keep running into the phrase "SOTP price target." Something feels off about slapping a single P/E multiple on the combined earnings of a company that stable and volatile businesses at once. A cash-generating mature division and a still-unprofitable growth division simply don't deserve the same yardstick. **Sum-of-the-Parts (SOTP) valuation** turns that intuition into an actual calculation method. Instead of treating the company as one blob, you split it into its business segments, value each one with whatever method fits it best, and add those values back together to get the whole company's worth. This lesson covers why SOTP exists, how the math actually works, and the traps that trip people up when they try it.

## The Problem With One Multiple for Everything

As covered in [PER, PBR, PSR, and EV/EBITDA](/en/basics/valuation-multiples-per-pbr-psr/), the multiple a business deserves depends heavily on its growth rate, margin profile, and risk. But a multi-segment company's consolidated financial statements blend every segment's revenue and profit into one set of numbers. If an analyst applies one industry-average P/E to that combined net income, they're implicitly assuming every segment inside the company shares the same growth and risk profile — which is almost never true. A mature, cash-generative segment deserves a lower multiple, while a fast-growing segment often deserves a much higher one even with thin or negative current profits. Blending them into one average multiple distorts both: the mature segment's value gets inflated and the growth segment's gets buried. In theory these distortions might offset at the company level, but in practice the larger segment's multiple tends to dominate the blended number, swallowing whatever value the smaller, faster-growing segment actually has.

## How SOTP Actually Works: A Different Ruler for Each Piece, Added at the End

The logic behind SOTP is straightforward. First, break the company down into the units disclosed in its segment reporting. Then value each segment with whatever method genuinely fits its characteristics — a stable, cash-generative segment gets an industry-average EV/EBITDA or P/E multiple, while an unprofitable or volatile high-growth segment is usually better served by projecting its own cash flows directly with [discounted cash flow (DCF)](/en/basics/discounted-cash-flow-dcf/). If a segment happens to be a separately listed subsidiary, there's no need to estimate a multiple at all — just take that subsidiary's market cap and multiply by the parent's ownership stake. Once every segment has a value, add them all up to get the combined enterprise value (EV) for the whole company. From there, apply the same bridge logic covered in [enterprise value vs. equity value](/en/basics/enterprise-value-vs-equity-value/): subtract company-level net debt and non-controlling interest, and add back non-operating assets like excess cash, investment real estate, or equity-method stakes. SOTP adds one more item this bridge doesn't usually need: unallocated corporate overhead. Each segment's own operating costs are already baked into its profit figure, but headquarters costs that never get allocated down to any segment — executive salaries, listing and compliance costs, and the like — don't show up in any segment's value either. A careful SOTP model discounts that unallocated overhead to present value and subtracts it as its own line item.

```
Segment A value (EV/EBITDA multiple)
+ Segment B value (DCF)
+ Segment C value (listed-subsidiary stake at market value)
+ Non-operating assets (excess cash, investment property, etc.)
= Combined enterprise value (EV)
− Net debt
− Non-controlling interest
− Present value of unallocated corporate overhead
= SOTP equity value
```

## Seeing It in Numbers: Hypothetical Conglomerate T Corp

Consider a hypothetical diversified company, T Corp, with three pieces. ① A stable consumer-goods segment generates $80 million in annual EBITDA and trades in line with an industry-average EV/EBITDA of 6x. ② A fast-growing battery-materials segment is still unprofitable, but a DCF model puts its intrinsic value at $1.2 billion. ③ T Corp also owns a 40% stake in a separately listed telecom-equipment subsidiary with a $1 billion market cap. T Corp itself carries $300 million in net debt, $50 million of non-controlling interest, and an estimated $70 million present value of unallocated headquarters overhead.

| Item | Calculation | Value |
|---|---|---|
| Consumer-goods segment | $80M EBITDA × 6x | $480M |
| Battery-materials segment | DCF-implied intrinsic value | $1,200M |
| Telecom-equipment stake | $1,000M market cap × 40% | $400M |
| **Combined EV** | | **$2,080M** |
| Net debt | | −$300M |
| Non-controlling interest | | −$50M |
| Unallocated overhead | | −$70M |
| **SOTP equity value** | | **$1,660M** |

With 100 million shares outstanding, that works out to $16.60 of SOTP value per share. If T Corp's stock is actually trading at $11.00, the market is pricing it roughly 34% below the sum of its parts. This gap is called a **conglomerate discount**, and its causes overlap heavily with the [holding company discount](/en/basics/holding-company-discount/) covered elsewhere in this course: the added complexity makes each segment harder for outside investors to value separately, investors who want exposure to just the stable segment can simply buy a pure-play competitor instead, and there's a lingering worry that management might allocate capital inefficiently across such different businesses — all of which push the market price below the sum-of-the-parts figure.

## Common Mistakes When Building an SOTP Model

The logic is simple, but real-world SOTP models fall into a few recurring traps. The most common is forgetting to subtract unallocated corporate overhead — sum up every segment's value without a separate deduction for it, and you've inflated the whole-company value by exactly the cost that never showed up anywhere. A second mistake is picking segment multiples lazily, using whatever multiple happens to fit the whole company rather than the true peer group for that specific segment — which defeats the entire purpose of splitting the company apart in the first place. A third is being too optimistic about the value of unlisted segments or minority stakes: unlike a listed stock, an unlisted stake can't be turned into cash quickly, so real-world transactions typically apply some liquidity discount to it. A fourth is ignoring intercompany transactions or cross-holdings between segments and valuing each one as though it were fully independent — if the consumer-goods segment buys raw materials from the battery-materials segment, for instance, netting that out matters; otherwise money that's just circulating inside the company gets counted twice, as though it were newly created value flowing in from outside. A fifth is treating stale segment disclosures as current: segment-level results in filings are usually reported with a quarter or two of lag, so applying today's multiple to a segment whose underlying business has shifted meaningfully since that filing can understate or overstate its real value. Given these pitfalls, an SOTP figure is best treated as a reasoned reference range built on a specific set of assumptions, not a precise, single "correct" answer.

## When SOTP Helps — and When It Doesn't

SOTP isn't a universal tool. For a company with a single business, or with several segments similar enough in growth and risk that one multiple already captures them reasonably well, splitting things apart adds little and mostly adds complexity. Forcing SOTP onto a company whose segment lines are arbitrary or whose segment disclosure is too thin just produces a number built on shaky assumptions. It earns its keep, on the other hand, for holding companies, diversified conglomerates spanning unrelated industries, and companies where segments sit at clearly different growth stages — a mature cash cow paired with an early-stage new business, for example. This is also why the market often reacts sharply to spin-off or carve-out announcements: a jump in share price on that news is frequently read as the market already suspecting, in SOTP terms, that a piece of the company is worth more standing alone than it's being credited for inside the combined structure.

## Key Takeaways

- SOTP values a multi-segment company by applying the method that best fits each segment individually (EV/EBITDA, DCF, listed-subsidiary market value, etc.), then adding the results together — rather than applying one multiple to the whole company.
- The calculation sums each segment's value into a combined EV, then subtracts net debt, non-controlling interest, and unallocated corporate overhead to arrive at equity value.
- When the market price trades below the SOTP-implied value, that gap is called the conglomerate discount, and its drivers overlap heavily with the holding company discount.
- The most common mistakes are forgetting unallocated overhead, applying the wrong multiple to a segment, and ignoring the liquidity discount that unlisted stakes typically deserve.
- SOTP earns its keep for conglomerates and holding companies with genuinely distinct segments, but forcing it onto a single-business company or one with vague segment reporting undermines its own credibility.

## FAQ

### Is SOTP the same thing as the holding company discount?
They're closely related but not the same. The [holding company discount](/en/basics/holding-company-discount/) refers to the phenomenon itself — the market price trading below the sum of a company's parts. SOTP is the methodology used to actually calculate that baseline (sum-of-the-parts) value. You need an SOTP figure before you can even say how large the discount is.

### Should I take an SOTP price target at face value?
Better to treat it as a reference range than a precise answer. Segment multiples and DCF assumptions vary from analyst to analyst, so the same company can get noticeably different SOTP price targets across different reports. It's worth checking which method and multiple was applied to each segment before putting much weight on the final number.

### Can an individual investor build a rough SOTP model themselves?
With segment-level revenue and operating profit from a company's disclosures and average multiples for comparable listed peers, a rough SOTP estimate isn't out of reach. That said, a precise DCF for an unlisted segment or an accurate allocation of unassigned overhead usually relies on detail that sell-side research has better access to, so a retail-level SOTP calculation is best used as a directional gut check rather than a precise valuation.

> ⚠️ This article is for informational purposes only and is not investment advice. The company examples in this article are hypothetical illustrations used to explain the concept and do not represent any real company or actual financial figures. Investment decisions and their outcomes are the sole responsibility of the investor.
