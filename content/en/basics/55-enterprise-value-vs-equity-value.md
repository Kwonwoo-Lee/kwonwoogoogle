---
slug: enterprise-value-vs-equity-value
title: "Enterprise Value vs. Equity Value — Why Market Cap Isn't What It Costs to Buy a Company"
description: "The EV behind EV/EBITDA isn't the same as market cap. Learn the bridge — net debt, preferred stock, non-controlling interest — that turns equity value into the real cost of an acquisition."
order: 55
updated: 2026-09-01
keywords: ["enterprise value vs equity value", "EV calculation formula", "what is net debt", "enterprise value vs market cap", "EV EBITDA explained", "how to calculate enterprise value", "M&A acquisition cost", "non-controlling interest EV"]
seo_audited: "2026-09-01"
---

## Could You Buy a $1 Billion Company for $1 Billion?

If you've already covered [PER, PBR, PSR, and EV/EBITDA](/en/basics/valuation-multiples-per-pbr-psr/), you've seen that EV (Enterprise Value) equals market cap plus net debt. A natural question follows: market cap is already the value of the whole company's equity, so why bother adding debt to get a separate number? The answer is that market cap only measures what belongs to shareholders. Anyone actually trying to buy the entire company faces a much bigger bill — on top of buying out every share, they also inherit whatever debt the company already owes. This lesson walks through how enterprise value differs from equity value, and what net debt, preferred stock, and non-controlling interest each contribute to the bridge connecting the two.

## Equity Value: Only the Shareholders' Slice

**Equity value** is what most people simply call "market cap" — current share price multiplied by shares outstanding. It's the figure you see on every stock app and financial site, and it's the number used as the numerator in PER. But equity value says nothing about how a company finances itself. A debt-free company and one carrying debt roughly equal to its revenue could both show a $1 billion market cap, and looking at equity value alone would make them look like they're "priced the same" — which they're not.

## Enterprise Value: The Real Cost of Buying the Whole Business

**Enterprise Value (EV)** corrects that illusion. Picture actually acquiring a company outright: the buyer has to purchase every outstanding share from existing shareholders, and at the same time takes on whatever debt the company already carries. On the other hand, any cash sitting in the company's accounts can immediately be used to pay down that debt, so it should be credited back against the real cost. That logic translates directly into the formula:

```
EV = Equity Value (Market Cap) + Total Debt − Cash and Cash Equivalents
   = Equity Value + Net Debt
```

If net debt (total debt minus cash) is positive, EV comes out higher than equity value. If a company holds more cash than debt — a "net cash" position — EV can actually be lower than equity value. In M&A negotiations, the price the two sides actually discuss at the table is usually framed in EV terms; net debt is then subtracted back out to arrive at the equity value that gets paid to selling shareholders.

## Two More Pieces of the Bridge: Preferred Stock and Non-Controlling Interest

Debt and cash aren't the whole bridge. Companies with more complex capital structures add two more items. The first is [preferred stock](/en/basics/preferred-vs-common-stock/), which sits ahead of common stock in the claim on assets and is a separate slice of capital altogether — buying the whole company means paying off preferred holders too, so the market value of preferred shares gets added to EV. The second is [non-controlling interest](/en/basics/non-controlling-interest-explained/): when a company crosses the 50% ownership threshold and consolidates a subsidiary, the subsidiary's full results — 100% of them — get folded into the parent's financial statements, regardless of the actual ownership stake. The slice of that subsidiary's net assets the parent doesn't own is also something a full acquirer of the whole group would need to buy out, so it gets added to EV as well. On the flip side, a minority equity-method stake in an associate (20–50% ownership, accounted for without full consolidation) isn't fully reflected in the parent's revenue or assets, so in theory its value should be subtracted from EV rather than added — though in practice many simplified EV calculations skip this adjustment and stick to net debt, preferred stock, and non-controlling interest.

```
EV = Equity Value + Net Debt + Market Value of Preferred Stock + Non-Controlling Interest
```

## Seeing It in Numbers — Same Market Cap, Very Different EV

Consider two hypothetical manufacturers, Company A and Company B, both with a $1 billion market cap.

| Metric | Company A (unlevered) | Company B (highly levered) |
|---|---|---|
| Equity Value (Market Cap) | $1.0B | $1.0B |
| Total Debt | $50M | $600M |
| Cash and Equivalents | $200M | $50M |
| Net Debt | -$150M (net cash) | $550M |
| Non-Controlling Interest | $0 | $100M |
| EV | $850M | $1.65B |

Both companies share the same $1 billion market cap, but the real cost of buying each one outright is $850 million for Company A and $1.65 billion for Company B — nearly double. Company A holds more cash than debt, so an acquirer could immediately use that cash to retire the debt and still have cash left over, making the real burden smaller than market cap suggests. Company B is the opposite: an acquirer inherits its debt and non-controlling interest, pushing the real cost well above market cap. If both companies post identical EBITDA of $100 million, PER (which only reflects market cap) might make them look similarly priced, but EV/EBITDA comes out to 8.5x for Company A versus 16.5x for Company B — a gap that reveals Company B is trading at a far richer price.

The difference becomes clearer from the perspective of an actual acquirer. Suppose you pay Company A's shareholders the full $1 billion market cap to acquire it. The moment the deal closes, you also inherit its $200 million in cash — enough to retire the $50 million in debt with $150 million left over. Your real net cost turns out to be $850 million, not $1 billion. Buy Company B for the same $1 billion, and the moment the deal closes you inherit $600 million in debt and $100 million in non-controlling interest, which its $50 million in cash barely dents — leaving you with a real burden of $1.65 billion, far more than the sticker price you paid. Looking at market cap alone and assuming the two "cost the same" misses this gap entirely.

## Finding the Bridge Components in Financial Filings

The EV bridge requires no special data terminal — anyone can build it from a company's balance sheet and financial filings. Equity value is closing price times shares outstanding. Total debt should include only interest-bearing borrowings — loans and bonds, whether current or long-term — from the balance sheet; accounts payable and accrued expenses, which carry no interest, are generally excluded from net debt, since an acquirer doesn't have to separately pay those off the way they would a loan — they're just part of the ongoing operating cycle. Cash and equivalents come straight off the top of the balance sheet. Preferred stock is calculated the same way as common — price times shares outstanding for the preferred class. Non-controlling interest is disclosed as its own line item within equity on a consolidated balance sheet, as covered in [non-controlling interest explained](/en/basics/non-controlling-interest-explained/), and its book value is usually close enough for this purpose, though more rigorous analysis sometimes estimates it at market value instead. Tracking these five components in a table every quarter turns this into a habit — you can immediately see which piece is driving a change in EV.

## Other Metrics Built on Enterprise Value

EV shows up as the numerator or denominator in metrics well beyond EV/EBITDA. For loss-making growth companies where even EBITDA is negative, EV/Sales is sometimes used instead — and unlike PSR, which uses equity value as its numerator, EV/Sales folds in capital structure too, making it a somewhat more rigorous comparison. In capital-intensive industries, EV/FCF (using free cash flow after actual capital expenditures) is sometimes preferred over EV/EBITDA, since EBITDA adds back depreciation without accounting for the real reinvestment needed to maintain those assets. What all EV-based metrics have in common is that they answer the same underlying question: what is this business, independent of how it's financed, actually worth? PER, PBR, and PSR, by contrast, answer a related but different question — what is the shareholders' slice worth? Keeping that distinction in mind helps avoid confusion when mixing the two families of ratios.

## Why This Distinction Matters for Investors

Without understanding the gap between EV and equity value, it's easy to compare two companies' market caps and assume they're "priced the same" when their debt loads couldn't be more different. This matters especially when reading M&A headlines like "Company worth $1 billion acquired for $500 million" — the interpretation flips entirely depending on whether that $500 million is quoted in equity-value or EV terms. If it's equity value, existing shareholders sold well below market price. But if the target carries $500 million in net debt, pushing its EV to $1 billion, the acquirer is still paying roughly $1 billion in real terms — they're just paying $500 million of it to shareholders and inheriting the rest as debt. As covered in [ROIC vs. WACC](/en/basics/roic-vs-wacc-value-creation/), when you're asking whether a company earns an adequate return on all the capital it has raised — debt and equity combined — the denominator that matches that question is something closer to EV, not equity value alone. Because EV strips out the effect of capital structure, it's a far fairer yardstick than market cap for comparing companies with very different debt levels, or for correctly reading the price tag in an M&A story.

## Key Takeaways

- Equity value (market cap) reflects only the shareholders' claim; enterprise value (EV) reflects the real cost of buying the entire business, debt included.
- EV = Equity Value + Net Debt (Total Debt − Cash) + Market Value of Preferred Stock + Non-Controlling Interest.
- A "net cash" company (more cash than debt) has an EV below its equity value; a heavily indebted one has an EV well above it.
- Two companies can share the same market cap and still trade at very different EV/EBITDA multiples once debt structure is factored in — so check whether a number, especially in an M&A headline, is quoted in equity-value or EV terms before drawing a conclusion.

## FAQ

### Can EV be lower than market cap?
Yes. If a company's cash and equivalents exceed its total debt, net debt turns negative and EV comes out below market cap. This "net cash" pattern shows up often in cash-rich, high-quality companies.

### When should I use EV/EBITDA instead of PER?
As covered in [PER, PBR, PSR, and EV/EBITDA](/en/basics/valuation-multiples-per-pbr-psr/), EV/EBITDA is the fairer comparison when comparing companies with different debt loads, or in capital-intensive industries with heavy depreciation, like telecom, airlines, or heavy industry — because unlike PER, it directly accounts for capital structure.

### What EV figure do M&A headlines usually quote?
It depends on the deal, but negotiations are often framed around EV first, with net debt subtracted afterward to arrive at the equity value actually paid to sellers. If an article doesn't specify which figure it's quoting, checking the target company's debt level is a good way to avoid misreading the price.

### How is treasury stock handled in the EV calculation?
Treasury stock (shares the company holds in itself) carries no voting or dividend rights and isn't publicly traded, so equity value should be based on shares actually outstanding in the market, excluding treasury shares. As covered in [the magic of treasury stock](/en/basics/treasury-stock-magic-explained/), treasury shares matter mainly in specific control-related contexts like spin-offs — for EV purposes, they're simply excluded from market cap rather than treated as a separate line item.

> ⚠️ This article is for informational purposes only and is not investment advice. The company examples in this article are hypothetical illustrations used to explain the concept and do not represent any real company or actual financial figures. Investment decisions and their outcomes are the sole responsibility of the investor.
