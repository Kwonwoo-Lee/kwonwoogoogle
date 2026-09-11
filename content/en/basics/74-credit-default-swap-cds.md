---
slug: credit-default-swap-cds
title: "What Is a Credit Default Swap (CDS)? Insurance Against Bond Default, Explained"
description: "How a CDS works like an insurance contract against bond default, why the CDS premium reflects creditworthiness, and why Korea's sovereign CDS premium makes headlines as a country-risk gauge."
order: 74
updated: 2026-09-11
keywords: ["what is a credit default swap", "CDS explained", "CDS premium meaning", "Korea sovereign CDS premium", "CDS vs credit spread", "naked CDS meaning", "how does a CDS work", "credit default swap example"]
seo_audited: 2026-09-11
---

## What Does "Korea's CDS Premium Hit a Record Low" Actually Mean?

Financial headlines periodically report that "Korea's sovereign CDS premium has fallen to its lowest level since the global financial crisis," or the opposite — that it spiked after some geopolitical shock. Most readers pick up that this has something to do with national creditworthiness without ever learning what a CDS actually is. [Credit Spreads Explained](/en/basics/credit-spreads-explained/) covered how the bond market prices a company's default risk into the gap between its corporate bond yield and the risk-free government bond yield. A **credit default swap (CDS)** takes that same default risk and turns it into a tradable contract in its own right. Where a credit spread is a byproduct — evidence of default risk baked into a bond's yield — a CDS is a tool built specifically to buy and sell that risk directly.

## What a CDS Actually Is: Insurance on a Bond

The mechanics of a CDS resemble a fire insurance policy more than they resemble a typical financial security. An investor holding a bond (the protection buyer) pays a recurring fee to a third party (the protection seller) in exchange for protection against the bond issuer (the reference entity) defaulting. That fee is the **CDS premium** (or CDS spread), usually quoted as an annual percentage of the bond's face value, in practice measured in basis points (bp; 1bp = 0.01 percentage point). If the reference entity actually defaults, misses a payment, or triggers another contractually defined credit event, the protection seller compensates the buyer for the loss. If nothing happens over the life of the contract, the seller simply keeps the premiums and the contract expires worthless to the buyer — exactly like a homeowner who pays years of fire insurance premiums and never files a claim.

It's easy to confuse this with the put option "insurance" analogy from [Options as Insurance](/en/basics/options-as-insurance/), but the two protect against different things. A put option protects against a stock's *price* falling below a certain level — a continuous, graded outcome. A CDS protects against a bond issuer's outright *failure to pay* — closer to a binary, all-or-nothing event. That's why a CDS payout structure looks much more like life or fire insurance than like an option.

## What Sets the Premium: Pricing Creditworthiness Directly

A CDS premium size mirrors how risky the market judges the reference entity to be. A borrower seen as financially sound can buy protection cheaply; one with weak finances or serious political uncertainty has to pay a much higher premium for the same coverage. Because of this, market participants often invert the premium to back out an implied default probability, using a widely used rule-of-thumb approximation:

```
Approximate annual default probability ≈ CDS premium ÷ (1 − recovery rate)
```

For example, if a CDS premium is 200bp (2.0%) and the assumed recovery rate on the bond in default is 40%, the implied annual default probability works out to roughly 2.0% ÷ (1 − 0.4) ≈ 3.33%. This is a simplified approximation, not a precise forecasting model, but it illustrates concretely why the CDS premium functions as a live gauge of creditworthiness. Because it's repriced in the market every day, it often reacts to changing risk perceptions far faster than credit rating agencies, which typically review and adjust formal ratings only every few months.

## What Counts as a "Credit Event"

For a CDS to pay out, a **credit event** as defined in the contract has to actually occur. The International Swaps and Derivatives Association (ISDA) maintains standardized definitions, the most common being outright bankruptcy, failure to pay interest or principal on time, and restructuring — a change to payment terms (extended maturity, reduced interest) imposed on creditors on unfavorable terms. Notably, a restructuring alone, well short of full bankruptcy, can trigger a payout, which is why disputes sometimes arise when a company negotiates softer terms with creditors rather than filing for bankruptcy outright. Whether a credit event has occurred isn't decided unilaterally by either party — ISDA's Credit Derivatives Determinations Committee makes that call — and settlement happens either by physically delivering the defaulted bond in exchange for face value, or through a cash auction that sets the recovery rate used to settle the claim.

## CDS Indices: Trading a Whole Market's Credit Risk at Once

Beyond single-name contracts tied to one company, the market also trades **CDS indices** that bundle many reference entities into one tradable instrument. CDX.NA.IG tracks 125 North American investment-grade names, CDX.NA.HY tracks North American high-yield names, and iTraxx Europe covers European corporates. These indices compress the credit risk sentiment of an entire market segment into a single number, playing a role in the credit market similar to what the [VIX](/en/basics/vix-implied-volatility-explained/) plays for equity volatility. During periods of broad market stress, moves in these indices often make headlines before — and more dramatically than — moves in any single company's CDS. Retail investors can't easily trade these indices directly, but understanding what they represent helps in reading financial news about credit-market stress.

## A Worked Example

Say Asset Manager A holds ₩10 billion face value of bonds issued by Company E, and grows concerned about E's deteriorating finances. A buys 5-year CDS protection from Bank B, which quotes an annual premium of 150bp (1.5%).

| Item | Detail |
|---|---|
| Notional protected | ₩10 billion |
| CDS premium | 1.5% annually (150bp) |
| A's annual payment | ₩150 million |
| If Company E repays normally | A pays ₩750 million in total premiums over 5 years, contract expires |
| If Company E defaults | B compensates A for the loss (e.g., ₩6 billion, assuming a 40% recovery rate) |

If Company E repays its debt without issue, A has simply paid for insurance it never needed to use — the intended, unremarkable outcome, just like unclaimed fire insurance. If E actually defaults, A — who would otherwise have absorbed most of the bond's principal loss — recovers the bulk of that loss from B instead. A CDS lets a bondholder keep the bond itself while shifting just the default risk elsewhere.

## Sovereign CDS: Why Korea's CDS Premium Makes the News

CDS contracts aren't written only on corporate debt — countries can be reference entities too. For Korea, the figure commonly cited as a gauge of sovereign default risk is the CDS premium on 5-year Foreign Exchange Stabilization Fund Bonds — dollar-denominated bonds the government issues to maintain foreign-currency liquidity. A lower premium signals that international markets trust the government's repayment capacity more; a higher one signals the opposite. That's why headlines about Korea's CDS premium spiking tend to appear during episodes of geopolitical tension or global financial stress, and why record lows get reported during periods of improving external confidence. Part of what makes this figure notable is that, unlike a sovereign credit rating that agencies review only periodically, it's a continuously traded market price that reacts to political and economic developments almost immediately. That said, like the [VIX](/en/basics/vix-implied-volatility-explained/), sovereign CDS premiums often move together with broad risk-off sentiment across all markets, so a spike shouldn't automatically be read as a proportional jump in actual default probability — it's more useful as a background gauge of market anxiety than a precise forecast.

## The 2008 Crisis: When Insurance Became a Problem

CDS entered public awareness during the 2008 global financial crisis. Insurer AIG had sold enormous volumes of CDS protection on bonds tied to subprime mortgages, collecting premium income without holding anywhere near enough capital to cover the losses it had implicitly promised to absorb. When the housing market collapsed and those underlying bonds soured en masse, AIG turned out to be unable to pay out on its commitments, forcing a massive U.S. government bailout.

What made this especially controversial was that a large share of the CDS outstanding at the time were **naked CDS** — contracts bought by investors who didn't actually own the underlying bonds and were simply betting on default. To extend the insurance analogy: it's like taking out a fire insurance policy on someone else's house and hoping it burns down. CDS used by an actual bondholder to hedge real exposure serves a legitimate purpose; large volumes of naked CDS stacked on top of that, however, mean the total payout owed if a company defaults can vastly exceed the amount of debt that company actually issued — amplifying systemic risk far beyond the underlying market. In response, reforms including the U.S. Dodd-Frank Act pushed CDS trading toward greater transparency and mandatory central clearing, and the European Union went further, restricting naked CDS trading on sovereign debt outright.

## Key Takeaways

- A CDS is a contract where a protection buyer pays a premium and a protection seller compensates the buyer if the reference entity defaults or triggers another defined credit event — structurally similar to fire insurance.
- The CDS premium reflects the market's assessed default probability for the reference entity; the rough formula "CDS premium ÷ (1 − recovery rate)" gives an approximate implied default probability.
- Countries can be reference entities too — Korea's 5-year sovereign CDS premium is widely cited as a real-time gauge of national default risk and external creditworthiness.
- AIG's oversized CDS exposure and the buildup of naked CDS bets during the 2008 crisis exposed how CDS can amplify systemic risk, prompting stricter transparency and clearing rules afterward.
- A CDS lets a bondholder keep holding the bond while transferring just the default risk elsewhere — the same underlying information a [credit spread](/en/basics/credit-spreads-explained/) reveals, shown through a different market mechanism.

## Frequently Asked Questions

### Is a CDS the same thing as a credit spread?
They're distinct but reflect the same underlying information. A credit spread is the yield gap between a corporate bond and a government bond — a byproduct that reveals default risk. A CDS premium is the price of a standalone contract built specifically to trade that default risk. The two tend to move together, and practitioners often use the CDS premium as a proxy for the credit spread.

### Can retail investors trade CDS directly?
Not really. Most CDS contracts are negotiated bilaterally as over-the-counter (OTC) agreements between institutions, and contract sizes typically run into the millions of dollars, putting direct CDS trading out of reach for individual investors. Sovereign CDS figures like Korea's premium are available as reference data through financial news and research sources, and high-yield bond ETFs or credit funds offer an indirect way to gauge broad credit-market sentiment.

### Does a rising CDS premium mean the stock will fall too?
Not necessarily and not automatically. The CDS premium reflects how bond-market participants assess default risk, while equity markets also price in growth expectations, so the two markets don't always move in lockstep or at the same speed. That said, as with a widening credit spread, a sharply rising CDS premium is worth treating as a signal that credit-market participants have started viewing that company's finances more negatively.

> ⚠️ This article is for informational purposes only and is not investment advice. Investment decisions and their outcomes are the sole responsibility of the investor.
