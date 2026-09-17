---
slug: rcps-redeemable-convertible-preferred-stock
title: "What Is RCPS (Redeemable Convertible Preferred Stock)? Why It Creates 'Capital Impairment' on Paper"
description: "Why startup funding through RCPS often gets booked as a liability under IFRS, how a cash-rich company can show negative equity on paper, and the accounting cliff at IPO."
order: 86
updated: 2026-09-17
keywords: ["what is RCPS", "redeemable convertible preferred stock explained", "why is RCPS a liability", "RCPS capital impairment", "RCPS debt vs equity classification", "startup negative equity accounting", "redemption right vs conversion right", "RCPS conversion at IPO"]
seo_audited: "2026-09-17"
---

## What RCPS Actually Is

Venture capital investors face a structural dilemma. If a startup succeeds, they need to hold equity to capture the upside. If it fails, plain common stockholders sit at the very back of the liquidation line and often recover nothing. **Redeemable Convertible Preferred Stock (RCPS)** — known in Korea as 상환전환우선주 — was designed to resolve exactly that dilemma. As the name suggests, it bundles two separate rights into a single security. The **redemption right** lets the investor demand their principal back, plus a contractually set return, if the company hasn't reached an exit (an IPO or acquisition) by an agreed deadline. The **conversion right** lets the same investor flip those preferred shares into common stock instead, if the company is doing well and heading toward an IPO, so they can capture the full upside rather than settling for a fixed return. In effect, the investor gets to eat like a lender if things go badly and like a shareholder if things go well.

Founders like the structure too, and for symmetric reasons. Unlike a bank loan, RCPS doesn't require servicing principal and interest out of current cash flow, which matters enormously for a pre-revenue or early-revenue company. And compared to selling a large block of plain common stock at a depressed early-stage valuation, RCPS dilutes founder control less, while the downside protection it offers investors makes them willing to accept a higher valuation than they would for unprotected common. That combination is why a large share of Korean venture funding rounds are structured as RCPS rather than plain equity.

## Why It Often Gets Booked as a Liability

This is where the security gets genuinely interesting. RCPS is legally a form of stock, and its name includes "preferred" — but under the accounting standard that governs Korean listed companies and many large private ones (K-IFRS 1032, aligned with IAS 32), it's frequently classified not as equity but as a **financial liability**. The test that decides this has nothing to do with what the instrument is called. It comes down to one question: does the company have a contractual obligation it cannot avoid to deliver cash? If the investor can exercise a redemption right and force the company to pay cash, the instrument behaves exactly like debt with a maturity date, regardless of its legal label — substance governs over form.

A feature common in Korean venture deals sharpens this further: **repricing clauses**. Many RCPS agreements adjust the investor's conversion ratio favorably if a later funding round prices lower than the current one (a down round). Once the number of shares issuable on conversion isn't fixed in advance, the conversion feature fails the "fixed-for-fixed" test that IFRS requires for equity classification, which pushes the whole instrument further toward liability treatment. Worth noting: private companies that follow Korea's local GAAP (K-GAAP) rather than K-IFRS often classify the same RCPS as equity — and that gap between accounting standards is precisely what causes the "accounting cliff" described further below.

Because the classification test hinges on the exact wording of redemption and repricing clauses, companies with similar-looking RCPS structures don't always land on the same answer. Some split a single instrument into a liability component (the redemption obligation) and an equity component (the conversion right) and account for each separately — and disagreements over where exactly to draw that line have occasionally surfaced in the Korean financial press, with two companies that raised similar RCPS amounts around the same time reporting different classifications. The practical takeaway is that there's rarely a single, obvious answer here; it comes down to reading the actual redemption and conversion terms in the contract.

## A Worked Example

Suppose Company B raises ₩30 billion through RCPS in its Series B round. That cash lands on the balance sheet as an asset, but because the redemption right is still live, the same ₩30 billion is simultaneously recorded as a financial liability. If Company B had ₩5 billion in shareholders' equity before the round, the round doesn't simply push equity up to ₩35 billion — instead, equity can stay roughly flat, or even keep shrinking over time as the accrued return owed under the redemption right (a preferred-dividend-like accretion amount) gets recognized as an added liability each year. Now suppose, ahead of an IPO, the company negotiates with its RCPS holders to convert the entire stake into common stock. At that moment, the ₩30 billion (plus whatever has accrued since) shifts from liability to equity in a single stroke, and reported equity jumps. Nothing about the company's actual cash position changed in either direction — only whether the redemption right was still alive.

## RCPS vs. Convertible Bonds vs. Common Stock

Startups raise outside capital through several different instruments, and they differ sharply in legal form, investor protection, and how they get classified.

| Instrument | Legal form | Investor's downside protection | Typical accounting classification |
|---|---|---|---|
| RCPS | Preferred stock (equity security) | Redemption right — can demand principal back | Liability (while redemption right is live) |
| [Convertible bonds](/en/basics/convertible-bonds-cb-bw/) | Bond (fixed maturity, interest) | Contractual claim to principal and interest | Liability (with the embedded conversion option sometimes split out as equity) |
| Common stock | Equity security | None — last in line at liquidation | Equity |

A convertible bond is a bond by legal design, so nobody seriously disputes that it belongs on the liability side. Common stock carries no redemption obligation at all, so it lands cleanly on the equity side with little debate. RCPS sits in the uncomfortable middle: its legal form is equity, but its economic substance — a company that can be forced to hand over cash on a set schedule — behaves like debt. That mismatch between form and substance is exactly why RCPS gets singled out for special accounting treatment that neither convertible bonds nor common stock require.

## Why a Perfectly Healthy Company Can Show "Negative Equity"

This accounting mechanic produces a genuinely confusing outcome for outside observers: a company that just raised tens of billions of won and is sitting on plenty of cash can simultaneously report **negative shareholders' equity** — what's called capital impairment (자본잠식) in Korean. The mechanism is straightforward once you see it. The RCPS proceeds land as cash, an asset — but the same amount lands as a financial liability too. Since equity is defined as assets minus liabilities, adding equal amounts to both sides of that equation doesn't move equity up at all; and once you add the accruing redemption premium each year, equity can drift lower even as the company's actual cash position stays strong. Taken to the extreme, the more capital a fast-growing startup raises through RCPS, the deeper its reported capital impairment can look — the exact opposite of what the raw headline number suggests.

Real Korean examples of this have shown up in the financial press. HeyDealer's operator, for instance, was reported to have deeply negative consolidated equity in one fiscal year, followed by a sharply narrower gap the next — not because operations suddenly turned around, but because RCPS was converted to common stock (or its terms renegotiated) as the company prepared for an IPO process. Same company, same underlying cash position — only the classification of the capital it had already raised changed. That's why, when looking at the financials of a private or pre-IPO company with significant RCPS on its books, the smarter approach is to look past the headline capital-impairment figure and check whether the underlying liability is genuinely at-risk interest-bearing debt or RCPS with a redemption clause, and how much actual usable cash the company is sitting on.

## The "Accounting Cliff" at IPO

RCPS's debt-like nature becomes most consequential exactly when a company prepares to go public. The Korea Exchange (KRX) typically strongly recommends that companies convert their RCPS to common stock before filing for a preliminary listing review, for two overlapping reasons. First, if a complex preferred instrument with a live redemption right remains outstanding after listing, ordinary retail investors have little visibility into its terms (redemption price, exercise window), and it becomes a source of unexpected volatility. Second, and more mechanically: an item that was booked as equity under K-GAAP while the company was private can flip to a liability the moment the company adopts K-IFRS as a mandatory listed issuer — spiking the debt ratio right around the listing date for reasons that have nothing to do with the business itself.

So in the run-up to an IPO, most startups negotiate with RCPS holders to waive the redemption right or convert the entire stake to common stock. The moment that happens, the company's contractual obligation to deliver cash disappears, and the corresponding amount shifts from liability to equity in one step. Nothing about the company's assets or cash changed — yet the reported debt ratio and equity position can improve dramatically right around the listing date. That's the "accounting cliff": a sharp, mechanical shift in the balance sheet driven entirely by a change in legal terms, not operating performance. This isn't unique to Korea, either — U.S. startups that issue redeemable convertible preferred stock commonly write automatic conversion-to-common-stock-at-IPO provisions directly into their charters. What's more pronounced in Korea is the added bite of repricing clauses interacting with K-IFRS's strict liability test.

The stakes get even higher before an IPO in regulated industries. A fintech company subject to capital-adequacy requirements can find that RCPS being classified as a liability pushes it below the regulatory capital threshold it's required to maintain — even though the cash from that same RCPS round is sitting untouched in its bank account. That's a genuinely paradoxical situation: real, spendable cash on hand, but a regulatory capital shortfall driven entirely by how one financing round happens to be classified. It's precisely why fintech and other regulated startups often push harder than most to negotiate common-stock investment or redemption-free terms instead of standard RCPS.

## Key Takeaways

- RCPS combines a redemption right (the investor can demand their principal back) with a conversion right (the investor can convert to common stock to capture upside), letting VCs protect their downside while still participating in the upside.
- K-IFRS 1032 classifies a security based on substance, not legal form: if the company can't avoid a future obligation to pay cash, RCPS with a live redemption right is typically booked as a financial liability rather than equity.
- Repricing clauses that adjust the conversion ratio in a down round can also push the conversion right out of equity treatment, since the number of shares issuable is no longer fixed.
- Because RCPS proceeds land as both an asset and a liability, a cash-rich company can still show negative equity on paper — a result of accounting classification, not necessarily financial distress.
- Converting RCPS to common stock ahead of an IPO removes the liability obligation in one step, producing a dramatic, purely mechanical improvement in reported equity — the "accounting cliff" that follows from the gap between K-GAAP and K-IFRS treatment.

## Frequently Asked Questions

### If a company's RCPS is booked as a liability, does that mean it's actually in financial trouble?
Not necessarily. The liability classification usually stems from the contractual redemption right the investor holds, not from an inability to service debt. Rather than reacting to the capital-impairment headline number alone, it's worth checking how much actual cash the company holds and what the redemption terms (maturity, trigger conditions) on that liability actually are.

### How is RCPS different from ordinary preferred stock?
The [preferred stock covered elsewhere on this site](/en/basics/preferred-vs-common-stock/) usually carries only a dividend priority with no redemption right, which is why it's classified as equity. RCPS adds a redemption right on top of that — the investor can force the company to hand over cash — and it's specifically that redemption right that pushes it into liability treatment.

### Can RCPS still exist after a company goes public?
It's uncommon. The Korea Exchange typically strongly recommends converting RCPS to common stock before a company files for its preliminary listing review, so a normally listed company's outstanding shares rarely include RCPS with a live redemption right. Still, when reviewing the financials of a company in the listing process (or the period just before it), it's worth checking whether RCPS exists and what the conversion plan looks like.

> ⚠️ This article is for informational and educational purposes only and does not recommend investing in any specific stock or company. The examples referenced are based on general, publicly reported information; actual accounting treatment depends on individual contract terms and auditor judgment.
