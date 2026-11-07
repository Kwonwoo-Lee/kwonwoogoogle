---
slug: bank-duration-mismatch-svb-explained
title: "Bank Duration Mismatch Explained: The Interest Rate Risk Behind SVB's Collapse"
description: "Why a bank funding long-term bonds with short-term deposits becomes dangerous when rates rise fast, explained through held-to-maturity accounting and the SVB collapse."
order: 187
updated: 2026-11-06
keywords: ["what is duration mismatch", "bank duration mismatch explained", "why did SVB collapse", "held-to-maturity vs available-for-sale", "how bank runs happen", "unrealized losses bank bonds", "asset liability management explained", "SVB bank run explained"]
seo_audited: 2026-11-06
---

## How "Safe" Deposits Can Still Bring a Bank Down

In March 2023, Silicon Valley Bank — the 16th-largest bank in the United States — collapsed in roughly 36 hours. It wasn't a bad-loan problem. Most of what SVB held was high-quality, low-default-risk paper: US Treasuries and mortgage-backed securities. The fact that a bank holding mostly risk-free assets still failed confused a lot of people. The real problem wasn't the quality of the assets — it was that the assets and the money used to buy them (the liabilities) had **maturities that didn't line up**. That mismatch has a name: **duration mismatch**, or asset-liability maturity mismatch. [Bond duration](/en/basics/bond-duration-and-convexity/) measures how sensitive a single bond's price is to interest rates. This lesson applies that same idea to an entire bank's balance sheet, to explain why a bank that looks perfectly healthy in calm markets can suddenly become fragile the moment rates move sharply.

## Why Banking Is Built on Borrowing Short and Lending Long

A bank's core business model is "maturity transformation." Depositors hand over money they can withdraw at any time — which makes deposits, functionally, an ultra-short-term liability. The bank pools that short-term money and invests it in longer-term assets: business loans, Treasuries, mortgage-backed securities. Longer-term assets typically pay a higher yield than short-term ones, so the bank pockets that term spread (long-term rate minus short-term rate) as profit. Under normal conditions, this works fine — deposits rarely all leave at once, so a bank only needs to keep enough cash on hand to cover ordinary withdrawals. The catch is that this structure is built on an inherent asymmetry: assets are long, liabilities are short. That asymmetry is the duration mismatch.

## Why Rate Moves Hit That Mismatch So Hard

As the [bond duration](/en/basics/bond-duration-and-convexity/) lesson covers, a long duration means a bond's price swings hard on even small rate moves. The long-term Treasuries and MBS a bank holds carry long durations and react sharply to rates. The bank's deposits, by contrast, have a duration close to zero — they can walk out the door at any moment. When rates rise, the market value of those long-duration assets drops sharply, while the value of deposits barely moves. The wider that duration gap between assets and liabilities, the harder the bank's net worth (assets minus liabilities) gets hit when rates swing. A second factor, **deposit beta**, makes this worse in practice. When the policy rate rises, the rate a bank earns on new loans tends to catch up fairly quickly, but the rate it pays depositors tends to lag and rise by less. That lag can actually widen a bank's net interest margin in the short run — but it does nothing to offset the mark-to-market losses already building up on the long-term assets. Asset losses show up immediately; any liability-side relief shows up slowly. That timing gap is what makes duration mismatch so dangerous.

## The Accounting Rule That Hides the Loss: HTM vs. AFS

Here's where bank accounting enters the picture. Bonds a bank holds fall into one of two buckets. **Available-for-Sale (AFS)** securities are marked to market, with gains and losses flowing into Accumulated Other Comprehensive Income (AOCI) on the balance sheet. **Held-to-Maturity (HTM)** securities, by contrast, are carried at amortized cost — the price paid at purchase — on the premise that the bank intends and is able to hold them until maturity. Even if rates rise and the market value of an HTM bond falls sharply, that loss never touches reported capital; it only shows up in a footnote disclosure. That's exactly what happened at SVB. During the 2021 pandemic liquidity boom, SVB took in a flood of deposits from well-funded tech startups and put most of that money into long-dated, fixed-rate Treasuries and MBS. Because a large share of that portfolio was classified as HTM, when the Fed raised rates sharply through 2022 and the market value of those bonds fell, the loss never showed up in SVB's official capital ratios. On paper, the bank still looked sound.

## The Numbers Behind SVB's Collapse

At the end of 2022, SVB's HTM portfolio had a face value of roughly $91 billion but a market value of only about $76 billion — more than $15 billion in unrealized losses sitting in a footnote, a figure comparable to the bank's entire shareholder equity of about $15.8 billion at the time. A loss large enough to wipe out nearly all of the bank's capital simply wasn't visible on the balance sheet, because none of those bonds had actually been sold. In March 2023, as rate hikes squeezed its startup depositors and withdrawals accelerated, SVB sold roughly $21 billion of its AFS securities to raise cash — realizing about $1.8 billion in actual losses in the process. The real trigger wasn't the loss itself but the capital raise SVB announced alongside it. Depositors read it as a sign the bank was scrambling to plug a hole, and that perception turned into a collective dash for the exits — amplified by mobile banking and social media — that drained tens of billions of dollars in deposits within a single day. California regulators shut the bank down for insolvency, and the entire episode played out in about 36 hours.

## Why the Loss Was Always Going to Surface Eventually

The core mechanism here: HTM accounting doesn't erase a loss, it only defers it off the balance sheet for as long as the bank doesn't actually sell the bond. If deposits had stayed stable, that unrealized loss could have simply faded away by maturity, since holding a bond to term returns its full face value regardless of what happened to its price along the way. But once a liquidity crunch forces a bank to sell before maturity, the deferred loss becomes a real one — and the moment it becomes real and visible, confidence erodes, which triggers more withdrawals, which forces more forced selling. It's a self-reinforcing loop. Duration mismatch itself can sit dormant for years while funding is stable; it only surfaces hidden asset losses once the liability side — deposits — starts shaking first. A National Bureau of Economic Research analysis of the 2022 rate-hike period found that many US banks responded to rising rates not by hedging but by reclassifying a large volume of securities into HTM specifically to keep the losses off their books, and that only a small share of banking-system assets were hedged against rate risk through derivatives at all. Deferring the accounting hit, rather than reducing the underlying risk, was the industry-wide pattern.

## The Pattern Repeated: Signature Bank and First Republic

SVB wasn't an isolated case. Signature Bank failed the same month, and First Republic Bank effectively collapsed two months later before being absorbed by JPMorgan. Both followed nearly the same script: deposits concentrated in a narrow customer base (crypto-adjacent firms in one case, ultra-low-rate mortgages held by wealthy clients in the other), long-dated assets bought when rates were low and now underwater, and an unusually high share of uninsured deposits that accelerated withdrawals the moment confidence cracked. None of the three ranked among the 20 largest US banks by assets, yet together they made up the largest wave of bank failures since the 2008 financial crisis. That points to something structural rather than idiosyncratic: duration mismatch builds up quietly across banks that ran similar playbooks through a long period of low rates, then gets exposed all at once when rates rise sharply in a short window. In the aftermath, US regulators and lawmakers debated raising deposit insurance limits and speeding up liquidity backstops, while banks broadly shifted toward holding less in HTM and hedging more of their rate exposure.

## Does the Same Risk Exist at Korean Banks?

The honest answer is: the structural risk is shared, but the regulatory environment differs. Korean banks run the same maturity-transformation model — funding loans and bonds (long-term assets) with deposits (short-term liabilities) — and the net interest margin covered in [why bank stocks trade on P/B](/en/basics/bank-stock-pbr-nim-valuation/) is itself a product of how that maturity structure interacts with the rate cycle. A few things differ, though. First, major Korean banks are subject to Basel III's Liquidity Coverage Ratio (LCR) and Net Stable Funding Ratio (NSFR) — rules SVB wasn't bound by at its asset size. Second, Korean regulators require banks to regularly measure and report Interest Rate Risk in the Banking Book (IRRBB), a standing check on exactly this kind of duration gap. Third, SVB's depositor base was unusually concentrated in venture-backed startups, and over 90% of its deposits sat above the US insurance cap of $250,000 — a degree of concentration that varies bank by bank elsewhere. Korea's deposit insurance cap, raised from 50 million won to 100 million won per depositor in September 2025, is higher relative to typical account sizes, and how much of any given bank's deposit base sits above that threshold differs from institution to institution. In short, every bank carries some version of this structural exposure — whether it turns into an actual run depends heavily on the regulatory regime and how concentrated the deposit base is.

## What Investors Can Actually Check

A few disclosures help gauge this risk when evaluating a bank. Watch the trend in AOCI on the balance sheet — a deepening negative AOCI during a rate-hike cycle signals growing unrealized losses on AFS securities. Check the footnote disclosure comparing the carrying value and fair value of HTM holdings; the size of that gap relative to shareholder equity shows how much risk is sitting out of view. And look at deposit composition — a high share of uninsured deposits, especially concentrated in one industry or customer type, raises the odds that withdrawals accelerate all at once if confidence wavers. Put together, these three checks can reveal how exposed a bank that looks, on the surface, like it holds nothing but safe government bonds actually is to interest rate risk.

## Key Takeaways

- Banking is built on maturity transformation — funding long-term assets with short-term deposits — which structurally creates a duration mismatch between assets and liabilities.
- When rates rise, the market value of long-duration assets falls sharply while deposits (which can leave almost instantly) barely change in value, hitting the bank's net worth hard.
- Held-to-maturity accounting doesn't eliminate that loss — it defers it off the balance sheet as long as the bonds aren't sold. SVB carried over $15 billion in unrealized losses this way without it touching reported capital.
- A deposit run forced SVB to sell bonds and realize losses, and the news of those losses shattered confidence enough to trigger a full bank run within 36 hours.
- Korean banks share the same structural exposure, but LCR/NSFR requirements, ongoing IRRBB supervision, and a typically less concentrated deposit base mean the actual risk level varies by bank and by country.

## FAQ

### Does having a duration mismatch automatically make a bank dangerous?
No. Some degree of maturity transformation — borrowing short to lend long — is the basic business model of banking and its main source of profit. It becomes a problem when the gap is unusually wide, left unhedged, or funded heavily by flighty money like uninsured deposits.

### Does classifying bonds as held-to-maturity make losses disappear permanently?
No. HTM classification doesn't erase the loss — it defers it off the balance sheet only for as long as the bonds aren't sold. Holding a bond to maturity eventually returns its full face value, but if a liquidity crunch forces an early sale, that deferred loss becomes real.

### Could a bank collapse the same way SVB did happen in Korea?
The underlying structural risk — duration mismatch from maturity transformation — exists at every bank. But major Korean banks operate under Basel III's LCR and NSFR requirements and ongoing IRRBB supervision, and typically don't have SVB's degree of deposit concentration in a single industry, which makes the same chain reaction less likely, though not impossible during a sharp rate-change cycle.

### Can an individual investor check this risk directly?
To some degree, yes. A bank's quarterly or annual report discloses the trend in Accumulated Other Comprehensive Income and the footnote comparing the fair value and carrying value of held-to-maturity securities. These numbers alone don't capture a bank's overall health, though, so they're best read alongside capital ratios and deposit composition.

> ⚠️ This lesson is for educational purposes only and is not investment advice regarding any specific bank or product. Investment decisions and their outcomes are the investor's own responsibility.
