---
slug: liquidity-coverage-ratio-lcr-explained
title: "What Is the LCR (Liquidity Coverage Ratio)? Why Well-Capitalized Banks Still Fail"
description: "How the Liquidity Coverage Ratio divides high-quality liquid assets by 30-day stressed outflows, why SVB wasn't required to hold one, and how Korea's won and FX LCR rules differ."
order: 209
updated: 2026-11-17
keywords: ["what is LCR", "liquidity coverage ratio explained", "LCR formula", "high-quality liquid assets HQLA", "bank liquidity risk explained", "LCR vs NSFR", "SVB liquidity coverage ratio", "Korea bank LCR requirement"]
seo_audited: 2026-11-17
---

## Capital Was Fine. The Bank Still Collapsed.

[What Is the BIS Capital Ratio?](/en/basics/bis-ratio-cet1-bank-capital-adequacy/) covered CET1 as the measure of a bank's loss-absorbing capacity — whether its capital cushion is thick enough. Yet when Silicon Valley Bank (SVB) collapsed in March 2023, its capital ratios were comfortably above the regulatory minimum right up until the end. As [What Is Duration Mismatch?](/en/basics/bank-duration-mismatch-svb-explained/) explained, what actually killed SVB wasn't the size of its capital — it was the speed at which it could turn assets into cash. Capital adequacy and liquidity sound similar but answer entirely different questions. "Does this bank have enough capital to absorb losses?" and "can this bank survive money leaving fast over the next 30 days?" are separate problems, and the second one has its own international standard: the **Liquidity Coverage Ratio (LCR)**.

## The 2008 Lesson: Banks That Weren't Insolvent, Just Out of Cash

The LCR entered the Basel III framework after the 2008 financial crisis specifically to address this gap. Many banks that failed or nearly failed during the crisis weren't technically insolvent — their balance sheets, on paper, looked reasonable. What broke them was that short-term funding markets froze overnight, and banks that relied on rolling over short-term borrowing simply couldn't find anyone willing to lend. Asset quality and book capital were beside the point; the problem was converting assets into cash fast enough. Regulators responded by building that specific risk — a bank running out of liquidity even while solvent — directly into the rulebook. The LCR, published in 2010 and phased in starting 2015, asks one blunt question: if a severe stress scenario ran for 30 straight days, does this bank hold enough assets it can turn into cash right now to cover what's likely to walk out the door?

## The Formula: High-Quality Liquid Assets ÷ 30-Day Net Cash Outflow

The core structure:

```
LCR = High-Quality Liquid Assets (HQLA) ÷ Expected net cash outflows over the next 30 days
```

Basel III's baseline requirement is that this ratio stay at or above 100% — meaning the assets a bank could convert to cash immediately must exceed what a severe stress scenario says will leave the building over the coming month. The critical thing to understand about both sides of this equation is that neither is a normal-times number. Both the numerator and denominator are calculated under conservative, crisis-grade assumptions — the kind that would hold up even if markets were in a panic, not the kind that describe an ordinary Tuesday.

## The Numerator: Not All Liquid Assets Are Equal

HQLA isn't a blanket category — Basel III tiers assets by how fast and how cleanly they can be sold without moving the price.

- **Level 1 assets**: central bank reserves, domestic government bonds — essentially no credit risk, deep markets, sellable at face value any time. These count toward HQLA at full value, with no cap.
- **Level 2A assets**: public-sector debt, high-grade corporate bonds. Slightly less liquid than Level 1, so a 15% haircut applies before they count.
- **Level 2B assets**: lower-rated corporate bonds, certain equities. Haircuts run 25–50%, and there's also a cap on how much of total HQLA this tier can make up.

The practical effect: holding a large pile of assets means little if most of it isn't the kind that sells instantly. This is where the held-to-maturity accounting issue from [What Is Duration Mismatch?](/en/basics/bank-duration-mismatch-svb-explained/) resurfaces. Long-dated Treasuries and MBS can qualify as Level 1 or 2A on credit grounds, but if rates have spiked and their market value has fallen sharply, HQLA counts them at that depressed market price — not book value. A bank can hide an unrealized loss on its balance sheet under HTM accounting, but the LCR calculation doesn't let it hide at all.

## The Denominator: "Run-Off Rates" Decide the Number

The denominator — net cash outflow — is where the real substance of the LCR lives. Rather than assuming all deposits leave at the same pace, regulators assign different **run-off rates** by funding type, modeling what fraction of each category would plausibly flee during the worst 30 days imaginable.

- **Stable retail deposits** (an individual's everyday, insured transaction account): roughly a 5% run-off rate. A regular depositor with an established relationship isn't assumed to pull everything even under stress.
- **Less stable retail deposits** (large balances chasing rate, with no operational relationship): roughly 10%. Money that moved in for yield moves out just as easily.
- **Operational corporate deposits** (payroll, clearing, and similar accounts a business actually needs to keep running): roughly 25%. The assumption is a company can't drain the account it depends on to operate.
- **Non-operational wholesale funding** (institutional cash parked for no operational reason, unsecured short-term borrowing): 40–100%. This is modeled as the money that leaves first and fastest at the slightest sign of trouble.
- **Undrawn credit commitments**: a portion of unused lines (typically 5–10%) is assumed to get drawn down during the stress window and added to outflows.

The underlying logic: deposit size alone tells you little — **whose money it is and why it's sitting there** matters far more. SVB's deposit base skewed heavily toward venture-backed startups holding large, uninsured, non-operational balances — exactly the profile the LCR model treats as the most run-off-prone. Two banks can both report "$10 billion in deposits," but the composition behind that number determines how much of it would actually still be there 30 days into a crisis.

## A Numerical Example

Say hypothetical Bank C holds $3 billion in HQLA (mostly Level 1 government bonds) and estimates 30-day outflows as follows:

- Stable retail deposits: $20B × 5% = $1.0B
- Non-operational wholesale funding: $5B × 60% = $3.0B
- Undrawn credit commitments: $10B × 10% = $1.0B
- Estimated total outflow: $5.0B (any modeled inflows would normally be netted against this; we'll simplify and assume zero inflows)

```
LCR = $3.0B ÷ $5.0B = 60%
```

That's well short of the 100% minimum — Bank C fails the standard as it stands. Closing the gap runs in two directions: grow the numerator by holding more Level 1 assets (which usually means shrinking loan or investment books), or shrink the denominator by reducing reliance on high-run-off wholesale funding and growing the stable retail deposit base instead. Both routes tend to cost something in profitability — a bank earns more lending money out than parking it in government bonds. That trade-off between "holding enough liquidity" and "maximizing earnings" is a constant tension for every bank balance sheet.

## Why SVB Was Never Required to Hold an LCR

Here's the genuinely interesting detail in the SVB story: the bank was never required to comply with the LCR at all. A 2018 U.S. deregulation law raised the asset threshold for the strictest "enhanced prudential standards" from $50 billion to $250 billion, and a 2019 implementing rule went further — "Category IV" banks, generally those between $100 billion and $250 billion in assets, were exempt from LCR and Net Stable Funding Ratio (NSFR) compliance entirely, as long as their short-term wholesale funding stayed below roughly $50 billion on average. SVB, with roughly $200 billion in assets and wholesale funding under that threshold, fell cleanly into this exempt category — no LCR disclosure, no LCR compliance obligation. Yale's Program on Financial Stability later estimated that had SVB been subject to the LCR, its ratio would have stood at roughly 75% at the end of 2022 — well under the 100% minimum. Whether an earlier warning sign under a binding LCR requirement would have changed the outcome is debatable, but the episode became a frequently cited case study in the subsequent U.S. debate over whether asset-size tiering had drawn the liquidity-regulation line in the wrong place.

## Korea's Two Separate LCR Regimes: Won and Foreign Currency

Korea runs its LCR regulation as two distinct tracks — one for won-denominated liquidity, one for foreign-currency liquidity — each with its own minimum. The won LCR's baseline requirement is 100%, though it was temporarily eased to 85% in 2020 to ease credit conditions during the pandemic shock, then normalized in stages — 95%, then 97.5% — before returning fully to 100% starting January 2025. The foreign-currency LCR is managed separately, typically held at a minimum around 80%, on the logic that unlike won, foreign currency isn't something the Bank of Korea can supply without limit — it needs a more conservative buffer. Recent reporting has noted Korean commercial banks' FX LCR slipping year-over-year during periods of elevated corporate dollar demand, even while won-denominated liquidity looked comfortable. The takeaway for anyone reading a Korean bank's disclosures: checking only the won LCR and concluding "liquidity looks fine" can miss a separate squeeze building on the foreign-currency side.

## LCR and NSFR: A 30-Day Buffer and a One-Year Buffer

The LCR has a companion regulation under the same Basel III umbrella: the **Net Stable Funding Ratio (NSFR)**. Where the LCR asks whether a bank survives a 30-day storm, the NSFR looks a full year out, asking whether the bank's overall funding structure is stable over a longer horizon. Put simply, the LCR measures short-term survival; the NSFR measures whether the underlying business model — how much it leans on short-term wholesale money versus stable, longer-term funding — is sound to begin with. The two are meant to work together: short-term shocks and structurally fragile funding are different failure modes, and a bank can pass one test while failing the other. SVB, notably, was exempt from both.

## What Investors Can Check

An investor gauging a bank's liquidity risk has a few concrete things to look for in quarterly filings. First, the LCR level itself and the trend in its buffer above the 100% minimum — a shrinking cushion over time signals mounting liquidity pressure even before the ratio breaches the floor. Second, check won and foreign-currency LCR together, since the two can deteriorate for entirely different reasons (exchange rates, exporter funding needs, the cost of issuing debt abroad). Third, watch the cost side: rebuilding an LCR buffer by shedding high-run-off wholesale funding and leaning more on retail deposits or bank bonds tends to raise funding costs, which flows straight into the net interest margin (NIM) discussed in [Why Bank Stocks Trade on P/B](/en/basics/bank-stock-pbr-nim-valuation/). The LCR answers "is this bank safe right now" and, in the same breath, "how much profitability is it giving up to stay that way."

## Takeaways

- The **LCR** divides high-quality liquid assets (HQLA) by the net cash outflow expected over a 30-day stress scenario, with Basel III's baseline requirement set at 100% or higher.
- Capital adequacy (CET1, the BIS ratio) asks whether a bank has enough capital to absorb losses; the LCR asks a completely different question — can it survive money leaving fast, right now.
- The numerator (HQLA) gets haircut by liquidity tier, and the denominator (net outflow) applies different run-off rates by funding type — retail, operational, and non-operational — and those assumptions are what actually drive the number.
- SVB was exempt from LCR compliance under asset-size and wholesale-funding thresholds; Yale's Program on Financial Stability estimated its LCR would have been roughly 75% had the rule applied.
- Korea runs separate won (minimum 100%) and foreign-currency (typically 80%+) LCR regimes that can move for unrelated reasons, so both are worth checking.

## FAQ

### Is a higher LCR always better?
It's safer, yes, but holding an unusually high LCR also means parking more funds in lower-yielding liquid assets like government bonds, which can weigh on ROE and net interest margin. Banks typically target a buffer somewhat above the regulatory minimum rather than maximizing the ratio outright.

### Can a bank have a strong CET1 ratio and a weak LCR at the same time?
Yes. Capital adequacy and liquidity are independent risks. A bank can be well-capitalized against long-dated, high-quality assets and still have a weak LCR if those assets can't be converted to cash quickly and the bank leans heavily on short-term funding. That combination is exactly what SVB had.

### Where can I find a Korean bank's LCR?
It's disclosed in the liquidity risk management section of quarterly and annual filings, broken out by won and foreign currency. The Bank of Korea's financial stability reports also track industry-wide LCR trends.

> ⚠️ This article is for informational purposes only and is not investment advice. Investment decisions and their outcomes are the sole responsibility of the investor.
