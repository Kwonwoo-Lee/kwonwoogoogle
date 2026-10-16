---
slug: deferred-tax-asset-liability-explained
title: "What Is Deferred Tax? How Deferred Tax Assets and Liabilities Move Net Income"
description: "Why timing differences between accounting income and taxable income create deferred tax assets and liabilities, and how this line distorts income tax expense and the effective tax rate, with a worked numerical example."
order: 144
updated: 2026-10-16
keywords: ["what is deferred tax", "deferred tax asset explained", "deferred tax liability explained", "effective tax rate vs statutory rate", "temporary difference accounting", "income tax expense calculation", "net operating loss deferred tax asset"]
seo_audited: 2026-10-16
---

## Why Income Tax Expense Rarely Matches Pretax Income Times the Statutory Rate

Look closely at an income statement and something odd often shows up: multiply pretax income by the statutory corporate tax rate, and the result rarely matches the "income tax expense" line actually reported. Some years it comes in well below that statutory rate; other years, well above it. Tax authorities aren't arbitrarily raising or lowering what a company owes year to year. The item driving most of that gap is **deferred tax**. This lesson covers why accounting income and taxable income are different numbers to begin with, why that gap shows up on the balance sheet as an "asset" or a "liability," and how it distorts the income tax expense and effective tax rate investors actually see.

## Two Rulebooks, Two Different Numbers

Companies have to satisfy two separate rulebooks at the same time when they close their books. One is the accounting framework used to report results to investors (IFRS, or K-IFRS in Korea's case); the other is the tax code used to calculate what's actually owed to the government. The two frameworks frequently give different answers to questions like "when should this expense be recognized" or "how should this asset be valued." A common case is depreciation: accounting standards typically require spreading an asset's cost evenly over its useful life, while tax codes often allow accelerated depreciation — larger deductions in the early years — specifically to encourage capital investment. Another common case is a warranty reserve: accounting standards require estimating and recognizing expected warranty costs in the same period the related sale happens, while the tax code generally won't allow that expense as a deduction until the cash is actually spent on warranty claims.

The gap this creates between "accounting income" and "taxable income" is called a **temporary difference**, and the word "temporary" is the whole point. The gap doesn't last forever — it eventually reverses and nets out to zero. With accelerated depreciation, the company deducts more for tax purposes than for accounting purposes in the early years, paying less tax now; but in the later years, the tax deduction shrinks below the accounting depreciation, so more tax is owed then. Over the asset's full life, the total tax paid converges to the same number either way — only the timing of when it's paid differs. Deferred tax is the mechanism that gets this timing difference onto the financial statements ahead of when the cash actually moves.

## Deferred Tax Liability: Pay Less Now, Pay More Later

Walk through the accelerated-depreciation case with numbers. Say a company buys ₩10 billion of equipment. For accounting purposes it depreciates the asset evenly over 10 years, ₩1 billion a year. For tax purposes, the tax code lets it depreciate the full amount over just 5 years, ₩2 billion a year. In year one, the accounting depreciation expense is ₩1 billion but the tax depreciation deduction is ₩2 billion, so taxable income comes in ₩1 billion lower than accounting income — meaning less actual cash tax owed this year. But that ₩1 billion gap hasn't disappeared; it's been deferred. By year 6, the tax deduction has run out entirely (fully depreciated for tax purposes in 5 years), while the accounting books still show ₩1 billion of depreciation left to go — so taxable income now runs ₩1 billion higher than accounting income, and more cash tax is owed than the accounting books would suggest.

This effect — pay less tax now, owe more at a specific point in the future — is recorded ahead of time on the balance sheet as a **deferred tax liability**. The cash tax actually paid this year (current tax) goes down, but the income tax expense reported on the income statement adds back the amount expected to be owed later, so income tax expense runs higher than current tax paid, and a deferred tax liability builds up on the balance sheet by exactly that difference. The key distinction for investors: a deferred tax liability isn't cash owed right now — it's an amount the company expects to settle with the tax authority at some future point, once the timing difference reverses.

## Deferred Tax Asset: Pay More Now, Pay Less Later

The reverse case works the same way in the opposite direction. Take the warranty example: accounting rules require recognizing an estimated ₩1 billion warranty expense in the same year as the related sale. The tax code won't allow that ₩1 billion as a deduction until the cash is actually spent fulfilling warranty claims. So this year, accounting income is ₩1 billion lower than it otherwise would be, but taxable income is higher (since that deduction isn't allowed yet) — meaning more cash tax is owed right now than the accounting books alone would suggest.

This creates a right to pay less tax in the future, once the warranty cash actually goes out and the deduction becomes allowable. That expected future tax saving is recorded as a **deferred tax asset**. Deferred tax assets, though, face a stricter recognition test than deferred tax liabilities: realizing that future tax saving requires the company to actually generate enough taxable income in the future to use the deduction against. A company with sustained losses or highly uncertain future profitability may be unable to recognize much of its deferred tax asset at all, or may have to write down one it already booked. The clearest case of this is a deferred tax asset built from accumulated **net operating losses (NOLs)** carried forward — recognizing it as an asset requires genuine confidence that the company will generate enough future taxable profit to actually use those losses.

## A Worked Example: Same Pretax Income, Different Tax Expense

Comparing two years of the same company makes the income-statement effect concrete. Take the accelerated-depreciation equipment above, assume the company earns a steady ₩10 billion of pretax income every year, and use a flat 20% statutory rate for simplicity.

| | Year 1 (accelerated depreciation window) | Year 6 (only accounting depreciation left) |
|---|---|---|
| Pretax income | ₩10bn | ₩10bn |
| Taxable income | ₩9.5bn (tax depreciation ₩0.5bn higher) | ₩10.5bn (tax depreciation is zero; ₩1bn of book depreciation remains) |
| Current tax paid (20%) | ₩1.9bn | ₩2.1bn |
| Change in deferred tax | +₩0.1bn (deferred tax liability grows) | -₩0.1bn (deferred tax liability shrinks) |
| Income tax expense (on the income statement) | ₩2.0bn (₩1.9bn + ₩0.1bn) | ₩2.0bn (₩2.1bn - ₩0.1bn) |
| Effective tax rate (expense ÷ pretax income) | 20% | 20% |

(These figures are simplified and hypothetical, built purely to illustrate the mechanism — they are not real company data.) The key thing to notice: the cash actually paid to the tax authority (current tax) differs between year 1 and year 6, but the income tax expense reported on the income statement comes out identical in both years, because the deferred tax movement is added and subtracted to smooth it out. Deferred tax is effectively the mechanism that separates "tax paid this year" from "the average long-run tax burden" on the income statement. In a real company's financials, many temporary differences move simultaneously across depreciation, reserves, and other items, so income tax expense and current tax paid rarely line up this cleanly even within a single period.

## Why This Matters to Investors: Effective Tax Rate and Earnings Quality

Not understanding deferred tax leads to two common misreadings of financial statements. First, seeing an unusually low income tax expense in a given year and concluding the company has simply become more "tax-efficient." If that low figure came from newly recognizing a deferred tax asset, it's an accounting adjustment rather than an operational improvement, and it can reverse just as easily the following year. The opposite misreading happens too: a sharp jump in income tax expense driven by a growing deferred tax liability can look like a sudden drop in profitability when it isn't one. Whenever the effective tax rate (income tax expense divided by pretax income) departs sharply from the statutory rate, it's worth checking how much of that gap traces back to a non-operating deferred tax swing rather than anything about the underlying business.

Second, deferred tax asset impairment deserves its own attention. If a company with accumulated losses or a newly uncertain outlook concludes it can no longer realistically use a deferred tax asset it previously booked — especially one built from NOL carryforwards — it has to write that asset down all at once. This isn't a cash outflow, but it's a non-cash item that can hit net income hard in a single period, in a way that resembles [goodwill impairment](/en/basics/goodwill-impairment-explained/). The financial statement notes, under "components of income tax expense" or "deferred tax asset/liability movement," break out exactly how much of income tax expense came from current tax versus deferred tax. As covered in [Earnings Quality and Accruals](/en/basics/earnings-quality-accruals/), the habit of separating a swing in reported net income into its core-operating cause versus a non-cash accounting cause pays off repeatedly when reading financial statements, and deferred tax is one of the most common sources of exactly that kind of non-operating swing.

## Balance Sheet Classification: Always Non-Current

Unlike some national accounting standards, IFRS (including K-IFRS) requires that deferred tax assets and liabilities always be classified as **non-current**, regardless of when the underlying temporary difference is actually expected to reverse. Companies are also often permitted to present deferred tax assets and liabilities net of each other on the balance sheet, as long as they hold a legal right to settle them with the same tax authority. Because of this, a single "deferred tax asset" or "deferred tax liability" line on the balance sheet tells you very little about what's actually inside it — the breakdown by temporary-difference category only shows up in the financial statement notes.

In a typical set of filings, the notes under "income tax expense" usually present two tables side by side: one breaking income tax expense into its current-tax and deferred-tax components, and another showing how deferred tax assets and liabilities moved, broken out by category — depreciation, employee benefits, NOL carryforwards, asset impairments, and similar items. That second table lets you trace exactly which category drove a given period's deferred tax movement. When comparing effective tax rates across companies in the same sector, it's more reliable to first screen that movement table for one-off items — a deferred tax recalculation triggered by a tax-law change, or a deferred tax asset swing tied to a large impairment charge — before comparing the headline effective tax rate itself.

## Key Takeaways

- Deferred tax captures timing differences — temporary differences — between when accounting standards and tax law recognize income or expense, and books them onto the financial statements ahead of when cash actually changes hands.
- A deferred tax liability reflects paying less tax now and more later (e.g., accelerated depreciation); a deferred tax asset reflects paying more tax now and less later (e.g., warranty reserves, NOL carryforwards).
- Recognizing a deferred tax asset requires genuine confidence in future taxable income; without it, the asset must be written down as an impairment loss.
- When the effective tax rate departs sharply from the statutory rate, check whether a deferred tax swing — rather than the core business — is the cause.
- IFRS classifies all deferred tax assets and liabilities as non-current, and the category-level breakdown only appears in the financial statement notes.

## FAQ

### Does deferred tax involve actual cash moving?
No. Changes in deferred tax assets and liabilities are non-cash accounting entries. The cash actually paid to the tax authority is "current tax"; deferred tax is simply the adjustment that reconciles current tax paid with the income tax expense shown on the income statement.

### Is a large deferred tax asset automatically a good sign?
No. A large deferred tax asset means a company holds a potential right to pay less tax in the future, but realizing that right requires generating enough future taxable income to use it. A large deferred tax asset built from NOL carryforwards in particular can signal a history of accumulated losses and real uncertainty about future profitability — not necessarily a hidden source of value.

### Is deferred tax the only reason the effective tax rate differs from the statutory rate?
No. Tax-exempt income, tax credits and incentives, and different tax rates on foreign subsidiary income can all push the effective rate away from the statutory one, alongside deferred tax. The notes section covering "components of income tax expense" or an "effective tax rate reconciliation" breaks out exactly which individual items are driving the gap.

> ⚠️ This article is for informational and educational purposes only and is not investment advice. The tax rates and numerical examples here are simplified and hypothetical, created purely to illustrate the mechanism, and do not represent the actual financial results of any real company. Confirm exact tax rates and accounting treatment through the applicable accounting standards and a tax professional. Investment decisions and their outcomes are the sole responsibility of the investor.
