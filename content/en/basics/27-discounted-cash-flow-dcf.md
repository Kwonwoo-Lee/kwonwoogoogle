---
slug: discounted-cash-flow-dcf
title: "What Is Discounted Cash Flow (DCF)? Calculating Intrinsic Value From Future Cash"
description: "How the DCF model discounts a company's projected future free cash flow back to today's value, plus the roles WACC and terminal value play, walked through with real numbers."
order: 27
updated: 2026-08-18
keywords: ["what is DCF valuation", "how to calculate DCF", "discounted cash flow explained", "free cash flow calculation", "intrinsic value calculation", "what is WACC", "terminal value explained", "DCF vs PER"]
---

## A Different Kind of Question Than "Is This Cheap?"

The metrics covered in [PER, PBR, PSR, and EV/EBITDA](/en/basics/valuation-multiples-per-pbr-psr/) all share one thing in common: they judge a stock as cheap or expensive relative to other, similar companies. A stock trading at a PER of 10 looks cheap next to a competitor at PER 20 — but that PER of 20 tells you nothing about whether it's actually the right price to begin with. If an entire sector is overvalued, "cheap relative to the sector" can be the wrong conclusion dressed up as a right one.

**Discounted cash flow (DCF)** takes a different approach entirely. Instead of comparing a company to its peers, it estimates the actual cash the company is expected to generate in the future, and asks what that future cash is worth today — arriving at an **intrinsic value** independent of any other company's price. This lesson covers what DCF actually calculates, why future cash gets "discounted" back to a present value in the first place, and why the method is as controversial as it is widely used. The goal isn't handing you a formula for a price target — it's being able to read the phrase "DCF fair value" in an analyst report and know exactly what's underneath it.

## Why a Dollar Tomorrow Is Worth Less Than a Dollar Today

DCF starts from a simple, almost obvious intuition: the time value of money. Offered $1,000 today or $1,000 a year from now, almost everyone takes it today. Two reasons explain why.

First, $1,000 in hand today can be invested and could be worth more than $1,000 a year from now — waiting means giving up that opportunity. Second, a promise of $1,000 a year from now carries real uncertainty: the payer might not follow through, or a company's business might deteriorate in the meantime. That uncertainty compounds the further out you look.

DCF compresses both of these — the time delay and the risk sitting inside it — into a single number applied to every future cash flow: the **discount rate**. A higher discount rate shrinks the present-day value of future cash more aggressively; a lower rate shrinks it less. This is the exact mechanism behind the idea covered in [How Interest Rates Affect Stock Valuations](/en/basics/interest-rates-and-stock-valuations/) — that a rising discount rate compresses the present value of future earnings. DCF is where that principle actually gets computed, line by line.

## The Four Steps DCF Actually Runs Through

DCF sounds intimidating, but broken down, it's four steps.

**Step 1 — Project future free cash flow (FCF).** Estimate the **free cash flow** the company is expected to generate each year for the next 5–10 years. Free cash flow is operating cash generated minus the capital expenditure (CAPEX) needed to sustain and grow the business — unlike accounting net income, it's less distorted by non-cash items like depreciation, making it a closer proxy for cash actually available to shareholders and lenders. This requires building out assumptions year by year: revenue growth, operating margin, capex intensity.

**Step 2 — Discount each year's cash flow to present value.** Each projected year's FCF gets divided down by the discount rate, compounded for however many years out it sits.

```
Present value = expected cash flow in year n ÷ (1 + discount rate)^n
```

**Step 3 — Estimate terminal value.** A company doesn't stop existing after year 5 or 10. The value of everything beyond the explicit forecast period, compressed into a single number, is the **terminal value**. There are two common approaches: the Gordon Growth Model, which assumes the final projected year's cash flow grows at a constant rate forever after (usually something close to long-run inflation, roughly 1–3%), or an exit-multiple approach, which applies an industry-average multiple like EV/EBITDA to the final year's figures. Because terminal value is itself a future number, it gets discounted back to the present using the same formula as step 2.

**Step 4 — Sum everything and convert to per-share value.** Add the discounted explicit-period FCFs to the discounted terminal value, and you get **Enterprise Value**. Subtract net debt (total debt minus cash and equivalents) and you get **Equity Value** — the portion that belongs to shareholders. Divide by shares outstanding, and you have DCF's estimate of intrinsic value per share, which is then compared against the current market price to judge whether the stock looks under- or overvalued by this method.

## Where the Discount Rate Comes From: WACC

The single input that moves a DCF's output the most is the discount rate. For company valuation, that's typically the **Weighted Average Cost of Capital (WACC)** — a blend of what it costs the company to raise money from its two sources, equity and debt, weighted by how much of each it actually uses.

```
WACC = (equity weight × cost of equity) + (debt weight × after-tax cost of debt)
```

Cost of equity is the return shareholders demand for holding the stock, and this is exactly where beta re-enters the picture: [What Is Beta?](/en/basics/beta-and-volatility/) covered how beta feeds into the Capital Asset Pricing Model (CAPM) to estimate that expected return. A higher-beta company — one that swings more than the market — commands a higher required return from shareholders, which pushes WACC up and pulls the present value of every future cash flow down. Cost of debt is roughly the interest rate the company actually pays on its borrowing, adjusted down for the tax benefit of deducting interest. In short, WACC represents the average return the people funding a business require — and a company only creates real value when its returns clear that bar.

## A Simplified Numerical Example

Here's a stripped-down version of the calculation for a hypothetical company. Real DCF models go into far more granular detail, but this is enough to see the mechanics.

| | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
|---|---|---|---|---|---|
| Projected FCF ($M) | 10.0 | 11.0 | 12.1 | 13.3 | 14.6 |
| Present value at 8% discount rate ($M) | 9.3 | 9.4 | 9.6 | 9.8 | 9.9 |

Summing the five years of present value gives roughly $48M. Assuming year-5 FCF grows at a permanent 2% rate thereafter, terminal value works out to (14.6 × 1.02) ÷ (0.08 − 0.02) ≈ $248M, which discounts back to about $169M in today's terms. Add the explicit-period present value ($48M) to the discounted terminal value ($169M), and Enterprise Value comes to roughly $217M. Subtract $20M of net debt, and Equity Value is about $197M. With 10 million shares outstanding, DCF's estimate of intrinsic value per share lands around $19.70.

The part worth sitting with here: terminal value ($169M) dwarfs the explicit-period present value ($48M). In the large majority of real DCF models, terminal value ends up accounting for 60–80% or more of the total. That means most of a DCF's final output rests on a single assumption about the distant future — a perpetual growth rate that's genuinely difficult to know 5 or 10 years out.

## How Much One Assumption Can Move the Result

Keep the same company and the same FCF projections, but nudge only the discount rate and the perpetual growth rate, and it becomes clear just how sensitive DCF is to its own inputs.

| Discount rate | Growth rate | Estimated enterprise value | vs. base case |
|---|---|---|---|
| 8% | 2% (base case) | ~$217M | — |
| 9% | 2% | ~$185M | ~-15% |
| 8% | 1% | ~$191M | ~-12% |
| 7% | 3% | ~$317M | ~+46% |

Same company, same cash flow projections — raising the discount rate by 1 point or lowering the growth rate by 1 point alone swings enterprise value by 10–15%, and moving both assumptions in a favorable direction together can swing it well over 40%. Neither of these two numbers is something you can just read off a financial statement; both are judgment calls made by whoever builds the model. That's exactly why two analysts covering the same stock with the same methodology can arrive at meaningfully different "DCF fair values" — it isn't a sign either one made an error, it's the nature of the inputs. Reading a DCF result means looking past the single price target to the discount-rate and growth assumptions holding it up.

## The Fundamental Limitation of DCF

DCF's biggest strength — valuing a company purely on its own cash-generating power, with no reference to any other company's price — is also its biggest weakness. As the table above shows, a 1-point change in the discount rate or growth rate materially shifts the answer. In practice, it's common for two analysts using the exact same DCF methodology to land tens of percent apart, purely because their growth and discount-rate assumptions differ slightly. This is the basis for a common criticism in finance: DCF looks precise, but a handful of adjustable assumptions can be tuned to produce nearly any conclusion someone wants.

DCF also works better for companies whose future cash flow is at least somewhat predictable. For an early-stage startup without stable revenue, or a business in an industry likely to look completely different in a few years, the margin of error in projecting FCF is so wide that the DCF output carries little reliability. In those cases, the market tends to lean on the relative-valuation (multiples) approach covered in [PER, PBR, PSR, and EV/EBITDA](/en/basics/valuation-multiples-per-pbr-psr/) instead. Conversely, for mature companies with stable cash flow, infrastructure and utility businesses, or full-company acquisitions in M&A, DCF remains a central, widely trusted method.

## Takeaway

- Unlike relative valuation, which compares a company to its peers, DCF is an absolute valuation method: it estimates a company's own future free cash flow directly and works out an intrinsic value from that alone.
- Future cash is worth less than present cash because of opportunity cost and uncertainty — the discount rate compresses both into a single number.
- The calculation runs in four steps: (1) project FCF, (2) discount each year to present value, (3) estimate terminal value, (4) sum everything, subtract net debt, and divide by shares outstanding.
- The discount rate is typically WACC — a blend of cost of equity (informed by beta) and cost of debt, weighted by the company's capital structure.
- Terminal value usually makes up the majority of total enterprise value, meaning DCF's output is disproportionately driven by a small number of assumptions about the distant future.

## FAQ

### Is a DCF-derived fair value accurate?
Not in any precise sense. DCF is an estimation model whose output is highly sensitive to assumptions about growth, discount rate, and terminal value. The same company can produce meaningfully different results depending on those assumptions, so it's safer to treat DCF output as a range that depends on its inputs rather than a single correct number.

### Do individual investors need to calculate WACC themselves?
Rarely. Brokerage research and financial data platforms typically publish sector-average WACC figures or full DCF valuations for individual stocks already calculated. It's still worth checking what growth and discount-rate assumptions went into a given figure before relying on it.

### Which is more accurate — DCF or a multiple like PER?
Neither is reliably better. DCF focuses purely on a company's own cash-generating ability but is highly sensitive to assumptions; multiples are simple to calculate but inherit any mispricing already present across the sector or market. In practice, it's common to run both and use them as a cross-check against each other.

> ⚠️ This article is for informational purposes only and is not investment advice. You are solely responsible for your own investment decisions.
