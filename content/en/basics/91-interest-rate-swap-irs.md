---
slug: interest-rate-swap-irs
title: "What Is an Interest Rate Swap (IRS)? Exchanging Fixed and Floating Payments"
description: "How an interest rate swap lets two parties trade fixed and floating interest payments without ever exchanging principal, why firms use them to hedge or cut funding costs, and what the swap spread signals."
order: 91
updated: 2026-09-19
keywords: ["what is an interest rate swap", "interest rate swap explained", "IRS swap meaning", "swap spread explained", "fixed vs floating rate swap", "how does an interest rate swap work", "swap spread vs treasury yield"]
seo_audited: 2026-09-19
---

## "The Swap Rate Fell Below the Treasury Yield" — What Does That Even Mean?

Bond-market coverage occasionally reports something that sounds backwards: "the swap spread has turned negative," or "the swap rate has dropped below the Treasury yield." At first glance this seems like a contradiction. A government bond is about as close to risk-free as an asset gets, while a swap rate is a price two private financial institutions agree to pay each other. So why would a rate set between private counterparties ever trade *below* the yield on a safer government bond? Answering that requires understanding what an **interest rate swap (IRS)** actually is. This lesson covers the basic mechanics of an interest rate swap, why companies and financial institutions use one, and what the gap between swap rates and government bond yields — the swap spread — actually signals.

## What an Interest Rate Swap Is: Trading Interest, Not Principal

An interest rate swap is a contract between two parties who agree to exchange periodic interest payments, calculated on an agreed **notional principal**, over a set period. One side pays a **fixed rate** locked in at the start of the contract; the other pays a **floating rate** that resets periodically against a reference benchmark plus a spread. The key word is "notional" — the principal itself never actually changes hands, at inception or at maturity. It exists purely as the number both legs' interest payments are calculated against. In practice, rather than each side paying its full interest amount separately, most swaps settle on a net basis: only the difference between the two calculated amounts actually moves on each payment date.

This is the main point of confusion with a currency swap (CRS). A currency swap exchanges principal denominated in two different currencies at both the start and end of the contract. An interest rate swap, by contrast, stays within a single currency and never exchanges principal at all — it only swaps how the interest on an *existing* obligation is calculated. In other words, an IRS doesn't create new debt or retire existing debt; it simply changes the interest-payment style attached to debt that already exists.

## Why Enter One: Hedging and Comparative Advantage

Companies and institutions use interest rate swaps for two broad reasons.

The first is **hedging**. A company that borrowed at a floating rate is exposed to rising rates — its interest expense climbs along with the benchmark. If that company enters a swap where it pays fixed and receives floating, the floating payment it receives offsets the floating payment it owes on its loan, leaving it effectively paying a fixed rate overall. A company that issued fixed-rate bonds but expects rates to fall, wanting to lower its funding cost, can do the reverse — receive fixed, pay floating. As covered in [Bond Duration and Convexity](/en/basics/bond-duration-and-convexity/), a fixed-rate liability's real value shifts as rates move; an interest rate swap is a tool for dialing that duration exposure up or down independently of the underlying loan or bond.

The second reason is cutting funding costs through **comparative advantage**. A highly rated company may get better rates than a lower-rated one in both the fixed and floating markets — but the size of that edge isn't always the same in both markets. If a company's advantage is disproportionately large in the fixed-rate market, it can come out ahead by borrowing fixed — regardless of which type of payment it actually wants — and then using a swap to convert that fixed obligation into the floating exposure it actually prefers, ending up with a better rate than if it had borrowed floating directly. The worked example below shows exactly how this plays out.

## How the Swap Rate Is Set: Benchmarks and the Swap Curve

The floating leg of an interest rate swap resets against a recognized **benchmark rate**. For decades, LIBOR served as the standard benchmark for swaps worldwide, but after the 2012 rate-rigging scandal eroded confidence in it, LIBOR was phased out entirely by the end of 2023 and replaced by risk-free reference rates built from actual overnight transactions — SOFR in the US, SONIA in the UK. Korea's won-denominated IRS market long relied on the 91-day CD rate as its benchmark, a rate compiled from dealer quotes rather than actual trades. Because thin trading volume left that rate a poor reflection of true market conditions, Korean regulators have been rolling out a phased transition to KOFR (Korea Overnight Financing Repo Rate), a transaction-based risk-free rate, as the new standard benchmark.

The fixed leg, by contrast, is set fresh each day by market supply and demand, and the line connecting fixed rates across maturities is called the **swap curve**. Like a government bond yield curve, the swap curve can steepen, flatten, or invert, and — echoing the term-spread logic covered in [Yield Curve Inversion](/en/basics/yield-curve-inversion/) — its shape reflects the market's rate expectations. Because the swap curve is relatively free of the supply distortions that hit specific maturities of government bond issuance, bond traders often read it alongside the Treasury curve to get a cleaner read on rate expectations.

## The Swap Spread: What the Gap to Treasuries Signals

The **swap spread** is the swap's fixed rate at a given maturity minus the government bond yield of the same maturity. Since a swap's counterparty is ultimately a bank or other private institution, intuition suggests the swap rate should always sit above the yield on a bond backed by a government with essentially no default risk. For a long time, that was generally true — swap spreads stayed positive, widening when banking-sector credit stress rose and narrowing when it eased.

Since the 2008 financial crisis, though, swap spreads at longer maturities — particularly in the US Treasury market — have repeatedly turned negative. That's the puzzle from the opening of this lesson. Two explanations come up most often. One is regulatory: post-crisis capital rules under Basel III raised the balance-sheet cost for banks of holding large swap books, dulling their appetite to receive fixed in swaps the way they once did. The other is a supply-and-demand story: pension funds and insurers carrying long-dated liabilities have built up enormous positions paying fixed and receiving floating in swaps — a strategy known as liability-driven investment (LDI) — to match the duration of those liabilities, putting sustained downward pressure on fixed swap rates. Most analysts see these two forces as reinforcing each other, together producing the counterintuitive outcome of private swap rates trading below sovereign bond yields.

## A Worked Example: Comparative Advantage in Action

Consider two hypothetical companies. Highly rated Company A expects rates to fall and wants floating-rate funding. Lower-rated Company B wants to lock in a fixed rate to avoid rate risk. Here's what each can borrow at directly:

| | Company A (wants floating) | Company B (wants fixed) |
|---|---|---|
| Fixed rate available directly | 4.0% | 5.5% |
| Floating rate available directly | Benchmark + 0.3% | Benchmark + 1.0% |
| Gap between the two companies | Fixed market: 1.5pp, floating market: 0.7pp | — |

Company A gets a better rate than Company B in both markets, but the gap is much wider in the fixed market (1.5pp) than in the floating market (0.7pp) — meaning A's comparative advantage is concentrated in fixed-rate borrowing. Instead of each company borrowing directly in the form it wants, both come out ahead if A issues fixed-rate bonds (its stronger market), B takes out a floating-rate loan (its relatively stronger market), and the two then swap their interest obligations.

| | Company A | Company B |
|---|---|---|
| Actual borrowing | Issues fixed-rate bonds at 4.0% | Takes a floating-rate loan at benchmark + 1.0% |
| Swap terms | Pays benchmark rate to counterparty, receives 4.1% fixed | Pays 4.1% fixed to counterparty, receives benchmark rate |
| Final effective funding cost | Benchmark − 0.1% | Fixed 5.1% |
| Savings vs. borrowing directly | 0.4pp (benchmark + 0.3% → benchmark − 0.1%) | 0.4pp (5.5% → 5.1%) |

Together, the two companies split the full 0.8pp gap (1.5pp − 0.7pp) between the two markets — 0.4pp each. In practice, a swap dealer usually sits in the middle, striking separate swap agreements with each company and pocketing a small spread in between, but the underlying mechanism is exactly what's shown here.

## The 2022 UK Pension Crisis: When a Hedge Amplified the Danger It Was Meant to Prevent

One of the most vivid illustrations of how interest rate swaps can amplify risk rather than just manage it is the UK pension market turmoil of September 2022. UK defined-benefit pension funds had widely adopted liability-driven investment (LDI) strategies to match the interest-rate sensitivity of their long-dated liabilities, and interest rate swaps combined with gilt repo financing were among the core tools. By taking leveraged positions that paid fixed and received floating, funds could offset rising liability values with swap gains when rates fell — but the same leverage meant that a sharp rate *increase* would trigger large mark-to-market losses on those swap positions and steep collateral (margin) calls.

When the UK government announced a large, unfunded package of tax cuts on September 23, 2022 (the "mini-budget"), gilt yields spiked, with several maturities seeing weekly increases of more than 100 basis points within days. Leveraged LDI funds facing margin calls on their swap and repo positions had to sell gilts quickly to raise cash — and those sales pushed gilt prices down further, triggering yet more margin calls in a self-reinforcing spiral. The situation stabilized only after the Bank of England stepped in with a temporary emergency gilt-purchase program to restore orderly market conditions; regulators subsequently required LDI funds to hold thicker capital buffers against future rate shocks. The episode wasn't a case of interest rate swaps being inherently dangerous — it showed that even a hedging instrument, once combined with leverage, can turn the very risk it was meant to contain (rising rates) into an amplified liquidity crisis.

## How an IRS Differs from a CDS or a Currency Swap

Several instruments share the word "swap," which invites confusion. A [credit default swap (CDS)](/en/basics/credit-default-swap-cds/) trades a bond issuer's **default risk** — an insurance-like structure where only a premium changes hands in normal times, with a large payout occurring only if a credit event actually happens. An interest rate swap, by contrast, settles on the ongoing **gap between two interest rates** throughout the life of the contract, regardless of whether either party ever defaults — it trades routine rate movement, not a tail event. A currency swap, mentioned earlier, also exchanges interest payments, but because it involves two different currencies, it exchanges principal too — unlike an interest rate swap, which never touches principal at all.

## Key Takeaways

- An interest rate swap exchanges fixed-rate and floating-rate interest payments calculated on a notional principal that itself is never exchanged.
- Companies and financial institutions use swaps either to hedge interest-rate exposure or to lower funding costs by exploiting comparative advantage between the fixed and floating markets.
- The floating leg resets against a risk-free benchmark like SOFR or KOFR; the fixed rates across maturities trace out the swap curve.
- The swap spread (swap rate minus Treasury yield) is usually positive, but bank regulatory capital costs combined with heavy pension-fund hedging demand can push it negative — a signal worth reading, not a sign that Treasuries have become riskier than banks.
- The 2022 UK pension crisis showed that a leveraged interest rate swap hedge can amplify a liquidity crisis rather than simply managing rate risk.

## FAQ

### Can retail investors trade interest rate swaps directly?
Not really. Interest rate swaps are mostly negotiated bilaterally as over-the-counter contracts between institutions, with typical notional sizes running into the tens of millions of dollars — well out of reach for individual investors. That said, swap rates and swap spreads are published as reference data through financial news and bond-market research, and tracking them alongside government bond yields is a useful way to gauge bond-market sentiment.

### Why are interest rate swaps sometimes described as risky?
The contract itself just exchanges interest, so principal loss isn't the immediate danger. The risk shows up when swaps are combined with leverage to build large positions, as in the 2022 UK pension crisis. If rates move sharply against a leveraged position, mark-to-market losses can trigger large, sudden margin calls, and the asset sales needed to meet them can spill over into broader market volatility.

### If the swap spread turns negative, does that mean government bonds are actually riskier than banks?
Not necessarily. A negative swap spread is usually explained by supply-and-demand factors — banks' regulatory capital costs and pension funds' hedging demand — rather than an actual reversal in relative credit risk. It's more accurate to read it as a sign of structural imbalance between the swap market and the government bond market than as a literal statement that government debt has become riskier than private bank credit.

> ⚠️ This article is for informational purposes only and is not investment advice. The numerical example in this lesson is a hypothetical illustration and does not represent the terms of any actual company or financial product. Investment decisions and their outcomes are the sole responsibility of the investor.
