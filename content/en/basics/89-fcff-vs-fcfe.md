---
slug: fcff-vs-fcfe
title: "FCFF vs FCFE — Why Valuing the Firm and Valuing Equity Use Different Cash Flows"
description: "DCF's free cash flow actually splits into FCFF and FCFE, each paired with a different discount rate. How to calculate each, and why the two results can diverge."
order: 89
updated: 2026-09-18
keywords: ["FCFF vs FCFE", "free cash flow to firm vs equity", "how to calculate FCFF", "how to calculate FCFE", "enterprise value vs equity value", "DCF free cash flow types", "WACC vs cost of equity discount rate"]
seo_audited: 2026-09-18
---

## One Layer Deeper Than the DCF Lesson

[What Is Discounted Cash Flow (DCF)](/en/basics/discounted-cash-flow-dcf/) walked through discounting free cash flow (FCF) at WACC to get enterprise value, then subtracting net debt to arrive at equity value — the shareholders' slice. Look closely at that sequence and something seems roundabout. Why not just calculate "the cash flow that belongs to shareholders" directly and discount it at the return shareholders themselves require, instead of discounting "the cash flow that belongs to everyone" and then backing out debt afterward?

Both approaches actually exist, and both are used in practice. The direct shareholder-only version is called **FCFE (Free Cash Flow to Equity)**, and the everyone-together version used in the earlier DCF lesson is called **FCFF (Free Cash Flow to Firm)**. This lesson covers exactly what each one measures, why each needs its own matching discount rate, and why two methods that should theoretically land on the same answer often don't in practice.

## FCFF — The Cash Flow That Belongs to Both Lenders and Shareholders

FCFF captures the cash a business generates from operations *before* any interest gets paid to lenders — the total pool that both creditors and shareholders, everyone who financed the company, have a claim on. The formula:

```
FCFF = EBIT × (1 − tax rate) + D&A − CapEx − increase in working capital
```

Starting from EBIT (operating income), it subtracts taxes, adds back the non-cash depreciation and amortization charge, then subtracts capital expenditures and the increase in working capital. Notice interest expense never appears anywhere in this formula. That's deliberate — FCFF is built to represent what the operating business itself generates, regardless of whether it happens to be financed with 100% debt or 100% equity. Discount FCFF at WACC and you get **enterprise value**; subtract net debt from that and only then do you arrive at equity value. That four-step sequence is exactly what the earlier DCF lesson walked through.

## FCFE — What's Left for Shareholders After Lenders Are Paid

FCFE takes it one step further: after interest and principal repayments to lenders are already accounted for, what's left over belongs to **shareholders alone**. The most intuitive version starts from net income:

```
FCFE = Net income + D&A − CapEx − increase in working capital + net borrowing
```

Net income already has interest expense subtracted out, so from there you add back D&A, subtract CapEx and the working capital increase, then add **net borrowing** — new debt raised during the year minus debt repaid. The logic for adding net borrowing is straightforward: cash raised from new debt is (for now) extra cash shareholders can effectively access, while cash used to pay down existing debt is cash that no longer reaches shareholders. You can also connect FCFF and FCFE directly through interest expense:

```
FCFE = FCFF − after-tax interest expense + net borrowing
```

Because FCFE has already stripped out the creditors' claim, discounting it produces **equity value** directly — no separate step of subtracting net debt afterward.

## Why the Discount Rate Has to Change Too

Since the two cash flows represent claims belonging to different groups, the discount rate applied to each must represent the return required by whichever group actually receives that cash flow — otherwise the math doesn't line up.

FCFF belongs to lenders and shareholders together, so it's discounted at **WACC**, the capital-structure-weighted average of what both groups require. FCFE belongs to shareholders alone, so it's discounted using only the **cost of equity**, typically estimated through [CAPM](/en/basics/capital-asset-pricing-model-capm/). That cost of equity is always higher than WACC, which matches the underlying logic: shareholders bear more risk than lenders and demand a higher return, and a pure cost-of-equity discount rate no longer blends in debt's comparatively cheap financing cost. Mixing these up — discounting FCFF at the cost of equity, or FCFE at WACC — is a common mistake that produces a value that's systematically too low or too high.

It helps to remember the pairing as one rule: whoever the cash flow belongs to, the discount rate must belong to the same group. FCFF's numerator mixes lenders and shareholders together, so its denominator (WACC) must too. FCFE's numerator is shareholders only, so its denominator (cost of equity) must be too. Break that rule and mix the wrong pair, and the number that comes out looks plausible but no longer represents anything real — numerator and denominator are pointing at two different claims.

## A Worked Example — Same Company, Two Methods

Take a hypothetical company: EBIT of ₩20 billion, a 25% tax rate, D&A of ₩3 billion, CapEx of ₩4 billion, a ₩1 billion increase in working capital, ₩50 billion in debt at a 5% interest rate, and a ₩150 billion market cap.

**FCFF**: ₩20B × 0.75 + ₩3B − ₩4B − ₩1B = **₩13 billion**

**FCFE**: After-tax interest expense is ₩50B × 5% × 0.75 = ₩1.875 billion. Assuming no net borrowing this year, FCFE = ₩13B − ₩1.875B + 0 = **₩11.125 billion**

For discount rates, assume a beta of 1.1, a 3.5% risk-free rate, and a 6% equity risk premium, giving a cost of equity of 3.5% + 1.1 × 6% = **10.1%**. After-tax cost of debt is 5% × 0.75 = 3.75%, and with equity and debt weights of 75% and 25%, WACC = 0.75 × 10.1% + 0.25 × 3.75% ≈ **8.5%**. Assuming both cash flows grow at a 2% perpetual rate and applying the Gordon growth formula, the FCFF method gives enterprise value of ₩13B × 1.02 ÷ (8.5% − 2%) ≈ ₩204 billion, minus ₩50 billion in net debt, for **equity value of about ₩154 billion**. The FCFE method gives ₩11.125B × 1.02 ÷ (10.1% − 2%) ≈ **equity value of about ₩140 billion**.

## They Should Converge in Theory — So Why the Gap in Practice

In theory, the FCFF/WACC method and the FCFE/cost-of-equity method should converge on exactly the same equity value. Yet the example above showed roughly a 10% gap. The cause is hiding in the assumption that net borrowing was zero. If total firm value grows 2% a year while debt never grows at all, the debt-to-value ratio quietly drifts lower every year — but the 75:25 capital structure weights used to compute WACC assume that ratio stays constant forever. The two assumptions contradict each other.

To fix this, debt needs to grow at the same 2% rate as firm value, meaning net borrowing should be ₩50B × 2% = ₩1 billion, not zero. Recalculating with that adjustment: FCFE = ₩13B − ₩1.875B + ₩1B = ₩12.125 billion, and equity value becomes ₩12.125B × 1.02 ÷ 8.1% ≈ **₩153 billion** — much closer to the FCFF method's ₩154 billion. In other words, the two methods diverge not because of arithmetic errors but because the assumption that capital structure stays constant throughout the forecast period wasn't applied consistently to both models. As covered in [Capital Structure (Modigliani-Miller)](/en/basics/capital-structure-modigliani-miller/), leverage itself is a variable that affects firm value, so when that assumption slips, the two calculation methods drift apart along with it.

## When to Use FCFF, and When FCFE

FCFF/WACC tends to be the more commonly used method largely for practical convenience. When capital structure shifts substantially over the forecast period — as in a [leveraged buyout (LBO)](/en/basics/leveraged-buyout-lbo-explained/) — the FCFF approach can adapt relatively cleanly by recalculating WACC against the target capital structure at each point in time. That's generally easier to manage than FCFE, which requires estimating net borrowing separately every year.

FCFE tends to fit better for financial companies like banks and insurers. For a bank, debt — customer deposits, policyholder liabilities — isn't a financing choice; it's closer to a raw material the business runs on. In a bank earning its income from the spread between lending and deposit rates, the whole idea of an operating cash flow "with debt stripped out" barely makes sense, and CapEx or working capital don't map onto a bank's business the way they do for a manufacturer. That's why analysts valuing financial institutions more often skip the FCFF-to-enterprise-value route and estimate FCFE directly, or go a step further and use a [dividend discount model (DDM)](/en/basics/dividend-discount-model-ddm/), treating dividends themselves as the shareholder cash flow and discounting them straight at the cost of equity.

FCFE is generally considered trickier in practice largely because of that net borrowing line. CapEx and working capital changes tend to follow fairly consistent patterns tied to a company's operations, but net borrowing can swing sharply year to year depending on financing decisions — whether management funds dividends with new debt, or pays down debt ahead of buybacks. In the example above, equity value moved by nearly 10% depending on whether net borrowing was assumed to be zero or ₩1 billion — FCFE models are unusually sensitive to that single line item. That's why analysts try to anchor net borrowing assumptions to something concrete, like a company's disclosed payout policy, debt repayment schedule, or credit rating targets, rather than picking a number arbitrarily.

## Takeaways

- FCFF is the cash flow claimed jointly by lenders and shareholders — discount it at WACC to get enterprise value, then subtract net debt to get equity value. FCFE already excludes the lenders' claim, so discounting it at the cost of equity gives equity value directly.
- FCFF = EBIT × (1 − tax rate) + D&A − CapEx − increase in working capital. FCFE = net income + D&A − CapEx − increase in working capital + net borrowing.
- The two methods converge to the same equity value in theory only when the assumption that capital structure stays constant is applied consistently across both models.
- FCFF fits situations where leverage changes substantially, like an LBO. FCFE or a dividend discount model fits better for financial companies where debt functions as a raw material rather than financing.
- If the two methods give noticeably different answers in practice, the more likely culprit is a capital-structure assumption that isn't consistent between the two models, not an arithmetic mistake.

## FAQ

### Do individual investors need to calculate FCFF and FCFE themselves?
Not usually. Most investors work from DCF valuations that brokerages or financial data platforms have already calculated. But if a report specifies whether its target price is built on an "enterprise value" or "equity value" basis, understanding the FCFF/FCFE distinction from this lesson lets you judge which method likely produced that number.

### Which method is more accurate?
Neither is inherently more accurate. When the capital structure assumption is applied consistently, the two are designed to arrive at the same theoretical answer — they're just two different routes to the same destination. In practice, analysts often pick whichever is easier to model given how stable the company's capital structure is.

### Can FCFF or FCFE come out negative?
Yes, especially for high-CapEx growth companies or companies running losses. When that happens, the negative year is typically modeled alongside the future years where cash flow is expected to normalize, as part of the full multi-year DCF forecast rather than in isolation.

### Which method do most analyst "fair value" targets actually use?
For ordinary operating businesses — manufacturers, platform companies — most reports discount FCFF at WACC to get enterprise value, then subtract net debt. For banks and insurers, reports more often use FCFE or a dividend discount model, discounting the shareholder cash flow directly at the cost of equity. Even when a report doesn't state its method explicitly, the industry alone is usually a decent clue to which one it used.

> ⚠️ This article is for informational purposes only and is not investment advice. The company examples in this article are hypothetical and do not represent any real company or actual financial figures. You are solely responsible for your own investment decisions and their outcomes.
