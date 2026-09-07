---
slug: capital-structure-modigliani-miller
title: "Capital Structure Theory: Does Debt Actually Change What a Company Is Worth?"
description: "The counterintuitive Modigliani-Miller answer to whether more debt changes firm value, and why taxes and distress costs create a real optimal capital structure."
order: 67
updated: 2026-09-07
keywords: ["what is capital structure theory", "Modigliani Miller theorem explained", "does debt affect firm value", "optimal capital structure", "capital structure and WACC", "interest tax shield explained", "trade-off theory finance", "leverage and firm value"]
seo_audited: 2026-09-07
---

## Is a Company With More Debt Automatically Riskier — or Just Cheaper to Fund?

As covered in [ROIC vs WACC](/en/basics/roic-vs-wacc-value-creation/), WACC is a weighted average of the minimum returns a company's shareholders and lenders require. Calculating that weighted average raises an obvious follow-up question: if a company changes the mix of debt and equity funding its operations — its **capital structure** — does the company's total value change too? The intuitive answer could go either way. Debt is usually cheaper than equity, so loading up on it should lower the cost of capital and raise firm value. But more debt also means more risk of default, which should lower firm value. The most rigorous attempt to resolve this contradiction is the **Modigliani-Miller theorem (MM theorem)**, published in 1958 by economists Franco Modigliani and Merton Miller. This lesson covers the counterintuitive conclusion MM reached under idealized conditions, and how real-world frictions — taxes and financial distress costs — flip that conclusion into the idea of an "optimal capital structure."

## MM Proposition I: Under Ideal Conditions, Capital Structure Doesn't Matter

MM's starting point is genuinely surprising. Assume a **perfect capital market**: no taxes, no bankruptcy costs, no information asymmetry, and everyone — companies and investors alike — can borrow and lend at the same rate. Under those assumptions, a company's total value is determined entirely by the operating cash flows it generates, completely independent of how much debt it uses to fund itself.

The "pie" analogy makes this concrete. Picture the total cash flow a company generates as one pie. Changing the capital structure just changes how that pie gets sliced between lenders and shareholders — it doesn't change the size of the pie itself. Load up on more debt, and the slice going to lenders grows while the slice left for shareholders shrinks — but the two slices added together, the company's total value (debt plus equity), stays exactly the same. That's the core of MM Proposition I.

Why does this hold? MM proved it using an arbitrage argument called **homemade leverage**. If a leveraged company's shares traded at a premium to an otherwise-identical unleveraged company, an investor could instead buy shares in the unleveraged company and personally borrow money on their own account, replicating the exact same risk-and-return profile at a lower cost. Enough investors doing this would force the two companies' values back into line through arbitrage. The logic: since investors can create their own leverage without the company's help, the company's decision to borrow can't add any value on its own.

## MM Proposition II: Cost of Equity Rises With Leverage

A natural objection follows. If debt is usually cheaper than equity, shouldn't adding more of it lower WACC? MM Proposition II answers this directly: **as the debt-to-equity ratio rises, the cost of equity rises by exactly enough to keep WACC unchanged.**

```
Cost of equity = unlevered cost of equity + (unlevered cost of equity − cost of debt) × (debt / equity)
```

The mechanism is straightforward. Debt holders have a claim on a company's cash flows that comes ahead of shareholders. The more debt a company takes on, the more volatile the residual claim left for shareholders becomes — they only get what's left after interest and principal are paid. As covered in [What Is Beta?](/en/basics/beta-and-volatility/), higher risk means investors demand a higher expected return, so shareholders rationally demand more compensation for that added volatility. The benefit of substituting in cheaper debt is exactly offset by the rising cost of the equity that remains, which is why WACC itself stays flat with respect to capital structure under MM's idealized assumptions.

## So Why Does Capital Structure Actually Matter in Practice?

Everything above holds under idealized assumptions. The reason real CFOs agonize over debt ratios is that MM's perfect capital market doesn't exist. Two key frictions break the idealized result.

**First, the interest tax shield.** Unlike dividends, interest expense is tax-deductible — it's subtracted from pre-tax income before the corporate tax bill is calculated. In effect, the government absorbs part of the cost of a company's debt financing through the tax code. Modigliani and Miller themselves revised their model in 1963 to account for this: in a world with corporate taxes, adding debt raises firm value by the amount of that tax shield.

**Second, financial distress costs.** More debt means a higher probability of missing interest or principal payments — a higher chance of default. Even short of actual bankruptcy, a company perceived as financially stretched pays a real price: direct costs like legal and restructuring fees, plus indirect costs that are often larger — suppliers grow cautious and demand cash upfront, customers worry about the company's staying power, key employees leave for more stable employers, and management passes up good investment opportunities because cash is tight. These indirect costs start accumulating well before an actual default, simply from leverage approaching a risky level.

## Trade-Off Theory: Where the Tax Shield Meets Distress Costs

Balancing these two forces — a tax shield that grows with debt, and distress costs that also grow with debt — produces **trade-off theory**:

```
Levered firm value = Unlevered firm value + (tax rate × debt) − PV(expected financial distress costs)
```

Add debt gradually, and at first the tax shield benefit far outweighs distress costs, so firm value rises. Past a certain leverage level, though, default probability climbs steeply enough that distress costs start outpacing the tax shield — beyond that point, adding more debt actually destroys value. In theory, the point where the marginal tax benefit exactly equals the marginal expected distress cost is the company's **optimal capital structure**.

A simple illustration: a company with a 10% unlevered cost of equity, facing a 25% tax rate and 5% cost of debt, can lower its WACC into roughly the 8-9% range by adding a moderate amount of debt — and firm value rises accordingly. Push leverage further, though, until interest coverage drops to a dangerous level, and distress costs start overtaking the tax benefit — WACC turns back up and firm value starts falling. This is exactly why credit rating agencies weight metrics like the interest coverage ratio (operating profit divided by interest expense) and leverage ratios so heavily when rating corporate bonds: a downgrade raises the interest rate a company pays on new and existing debt alike, which is the market pricing in rising distress costs in real time. That's also why a CFO weighing a new bond issuance or a debt-funded buyback has to ask not just "is the rate attractive right now?" but whether that additional borrowing risks a downgrade that raises the cost of the debt already on the books — a sign that leverage may be pushing past the trade-off theory's optimal point.

## Why "Normal" Leverage Looks So Different Across Industries

Trade-off theory explains a pattern seen across real markets — though this is a general tendency observed in practice, not an absolute rule. Utilities and REITs typically carry conventionally high leverage. Their cash flows are contractual, regulated, and predictable, default probability is structurally low, and they hold plenty of tangible, collateralizable assets — so their distress costs stay small even at high debt levels, pushing their trade-off equilibrium toward a higher leverage point. Software and biotech companies, by contrast, run with very little debt. Their cash flows are volatile and uncertain, most of their value sits in intangible assets like patents and people rather than collateral, and even a modest rise in default risk can trigger outsized distress costs — key researchers leaving, R&D programs stalling. For these companies, staying nearly debt-free is often the safer structural choice.

## Two Other Lenses: Agency Costs and Pecking Order Theory

Trade-off theory isn't the only framework explaining real-world capital structure choices — two complementary views are worth knowing.

The **agency cost** view holds that debt can discipline management. Excess free cash flow gives managers an incentive to waste it on empire-building projects that don't serve shareholders; debt's fixed interest and principal obligations force that cash out the door, curbing this waste. Taken too far, though, heavy debt creates its own problems — shareholders may reject genuinely good, positive-NPV projects because most of the upside would go to creditors (underinvestment), or shift into riskier ventures because shareholders keep the upside while creditors absorb the downside (risk-shifting).

**Pecking order theory** starts from information asymmetry between management and outside investors: announcing a new equity issuance tends to signal that management believes the stock is overvalued, which typically pushes the share price down. So companies default to funding themselves with retained earnings first, debt second, and new equity only as a last resort. Under this view, a company's leverage ratio isn't really aimed at some "optimal" target — it's more the byproduct of financing needs and this pecking order playing out over time.

## Takeaway

- The MM theorem shows that in an idealized market with no taxes, no distress costs, and no information asymmetry, capital structure doesn't affect a company's total value — the benefit of cheaper debt is exactly offset by a rising cost of equity, leaving WACC unchanged.
- Real-world capital structure matters because of two frictions: the interest tax shield raises firm value as debt increases, while financial distress costs lower it as debt increases.
- Trade-off theory treats the point where these two forces balance as a company's optimal capital structure — industries with stable cash flows and strong collateral (utilities, REITs) tend to have that balance point at high leverage, while industries with volatile cash flows and mostly intangible assets (software, biotech) tend to have it at low leverage.
- Agency cost theory and pecking order theory are complementary lenses — in practice, a company's actual leverage reflects all of these forces working together, not any single model.

## FAQ

### Does low debt always mean a safer company?
Not necessarily. From a trade-off theory perspective, a company that barely uses debt may simply be leaving the tax shield benefit on the table. What matters isn't the debt ratio in isolation, but whether that level is sustainable given the company's cash flow stability and industry characteristics.

### Is the MM theorem useless since it assumes a world that doesn't exist?
No — its value isn't in giving a literal answer, but in providing the baseline needed to answer why capital structure matters at all. Establishing that capital structure is irrelevant under idealized conditions makes it far easier to pin down exactly which real-world frictions (taxes, distress costs, information asymmetry) actually drive its effect on value.

### How can an individual investor use this theory?
Rather than judging a high or low debt ratio as automatically good or bad, use it as a lens: is this level of leverage reasonable given how stable this industry's cash flows tend to be? Unusually low leverage in a stable industry may signal a conservative approach to funding growth, while unusually high leverage in a volatile industry can be a sign of real exposure to financial distress costs.

> ⚠️ This article is for informational purposes only and is not investment advice. You are solely responsible for your own investment decisions.
