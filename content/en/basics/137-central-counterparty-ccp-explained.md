---
slug: central-counterparty-ccp-explained
title: "What Is a Central Counterparty (CCP)? How Clearinghouses Erase Counterparty Risk by Standing Between Every Trade"
description: "Repo, CDS, and interest rate swap lessons all mentioned a 'CCP' absorbing settlement risk in passing. Here's what a clearinghouse actually does — novation, netting, margin, and the default waterfall — through the 2008 Lehman and 2018 Aas cases."
order: 137
updated: 2026-10-12
keywords: ["what is a central counterparty", "CCP clearinghouse explained", "what is novation in clearing", "default waterfall explained", "initial margin vs variation margin", "OTC derivatives central clearing mandate", "how does a clearinghouse reduce risk"]
seo_audited: "2026-10-12"
---

## The 'Clearinghouse' That Kept Showing Up in Repo, CDS, and Swap Lessons

Across this course — [the repo market](/en/basics/repo-market-explained/), [credit default swaps](/en/basics/credit-default-swap-cds/), [interest rate swaps](/en/basics/interest-rate-swap-irs/), and [settlement cycles](/en/basics/settlement-cycle-t2-explained/) — one sentence kept recurring almost unchanged: "an exchange or clearing body acts as a central counterparty (CCP) to cushion settlement risk." Each time, that sentence moved on without explaining exactly what a CCP does to a trade that makes the risk shrink. This lesson opens that box. We'll walk through the actual mechanics — novation, netting, margin, and the default waterfall — and why the honest description of what a CCP does isn't "eliminates risk" but "relocates and concentrates it."

## Turning Two Counterparties Into One: Novation

Picture a trade with no CCP involved. Bank A enters an interest rate swap with Dealer B. A now has to worry about whether B will honor its side, and B has to worry about A the same way. Scale that up to hundreds of counterparties, and you get a tangled web of **bilateral risk**, where every participant has to independently track the creditworthiness of everyone it trades with. A CCP steps into that web and splits each contract in two. Through a legal process called **novation**, the original A-to-B contract is extinguished and replaced by two new ones: "A versus the CCP" and "the CCP versus B." From that moment on, A no longer cares about B's credit at all — A's only counterparty is the CCP, and the CCP stands as buyer to every seller and seller to every buyer across the entire market. Collapsing hundreds of separate bilateral credit relationships into one central hub is the CCP's most basic function.

## The Power of Netting: Why One Counterparty Beats Many

Once everyone's counterparty is the same CCP, a second effect kicks in: **netting** — collapsing offsetting positions down to the single net exposure that actually matters. A simple illustration: say three members, A, B, and C, each owe $100 million to a different counterparty in a circular chain — A owes B, B owes C, and C owes A. In a purely bilateral world, that's three separate $100 million credit relationships, $300 million of gross exposure that has to be managed independently. Once all three trades run through the same CCP, though, the CCP nets what it owes and is owed from each of A, B, and C, leaving only the residual exposure. If the chain happens to cancel out perfectly, the CCP's actual net exposure collapses toward zero. Real markets never net out quite that cleanly, but when thousands of trades flow through a single CCP, offsetting positions cancel out enough that the system's total gross exposure drops dramatically. This is the same logic behind the netting described in [the T+2 settlement lesson](/en/basics/settlement-cycle-t2-explained/), where an exchange compresses a day's trades by security and by member before settling — except a derivatives CCP handles contracts with much longer maturities and constantly shifting market values, which is a harder risk to manage than a single day's stock trades.

## Two Layers of Collateral: Initial Margin and Variation Margin

Netting shrinks exposure, but it doesn't erase what's left. CCPs cover that residual risk with two distinct types of collateral. **Variation margin** is cash exchanged at the end of every trading day (or more often, in volatile markets) to settle that day's mark-to-market price move — the losing side pays the winning side immediately. Because this happens daily, if a member defaults, everything through the prior settlement is already paid; the CCP is only exposed to the price movement from that one day (or however long it takes to close out the position) forward. **Initial margin** is the collateral posted upfront, sized specifically to cover that remaining close-out-period price risk. CCPs calculate initial margin using statistical models built on historical volatility — essentially asking "how bad could this get before we can fully exit the position" — and they raise that requirement quickly when markets turn volatile. Together, these two layers mean a CCP can typically absorb a defaulting member's losses using collateral that member itself already posted, without needing anyone else's money.

## When Collateral Isn't Enough: The Default Waterfall

The problem is that markets sometimes move further than any historical model predicted. For the rare case where collateral alone can't cover a loss, CCPs run a strictly ordered sequence of loss-absorbing layers known as the **default waterfall**. The order commonly described by the Bank for International Settlements and similar bodies looks like this:

| Step | Resource | What it is |
|---|---|---|
| 1 | Defaulter's own margin | Initial and variation margin posted by the member that failed |
| 2 | Defaulter's default fund contribution | That same member's share of the mutualized guarantee fund |
| 3 | CCP's own capital ("skin in the game") | Capital the CCP itself puts at risk before anyone else's |
| 4 | Non-defaulting members' default fund | The mutualized fund contributed by every other, uninvolved member |
| 5 | Further CCP assessments | A last-resort call for additional contributions from members |

The key detail is that steps 1 through 3 only use money belonging to the defaulting member and the CCP itself. Step 4 is where things get controversial: only at that point does a loss start being absorbed by **mutualization** — other members who did nothing wrong watching their pre-funded contribution get drawn down because of someone else's bad trade.

## Stress-Tested in Reality, Case 1: Lehman Brothers, 2008 — Contained Entirely by Margin

The clearest real-world test of this structure came during the 2008 Lehman Brothers bankruptcy. A Lehman subsidiary's interest rate swap book cleared through LCH's SwapClear service spanned roughly 66,000 trades across five currencies, with a notional value of about $9 trillion. When Lehman defaulted on September 15, 2008, LCH immediately hedged the book to neutralize its market risk, then auctioned off the five currency portfolios to other SwapClear members between September 24 and October 3. The entire close-out was absorbed within the margin Lehman had already posted, and LCH stated publicly that it never touched its default fund. In waterfall terms, the loss never got past step 1 — a result still cited today as proof that a CCP's margin model can hold up even in an extreme, systemic crisis.

## Stress-Tested in Reality, Case 2: The Aas Default, 2018 — When the Mutualized Fund Got Used

The opposite case — one that actually reached deep into the waterfall — happened a decade later. Einar Aas, a Norwegian individual power trader, had built a large position betting that the spread between Nordic and German power prices would narrow. In September 2018, heavy rainfall boosted Nordic hydropower output and pushed Nordic prices down, while a surge in carbon and coal prices pushed German prices up — the spread moved sharply the wrong way. Aas failed to meet a margin call and was declared in default. When Nasdaq Clearing AB auctioned off his portfolio, the loss exceeded his posted collateral by roughly €114 million. According to the Bank for International Settlements, that shortfall ran through Nasdaq Clearing's own capital (about €7 million — step 3) and still wasn't fully covered, so a substantial share had to come out of the mutualized default fund contributed by the other, uninvolved clearing members (step 4) — after which Nasdaq asked members to replenish the fund. Unlike the Lehman case, this was a real instance of other members paying for someone else's failed trade, exactly the scenario the mutualized layer of the waterfall exists to handle.

## Central Clearing in Korea: KRX's Role

In the aftermath of the 2008 crisis, G20 leaders agreed at the 2009 Pittsburgh summit to require standardized OTC derivatives to clear through CCPs. As part of implementing that commitment, the Korea Exchange (KRX) received authorization from Korea's Financial Services Commission in 2013 to act as a domestic CCP for both exchange-traded and OTC derivatives. Mandatory central clearing of won-denominated interest rate swaps was the first product brought under that mandate, and KRX has since signaled plans to expand clearing to other OTC products such as non-deliverable forwards (NDFs). The CCP role described in [the T+2 settlement lesson](/en/basics/settlement-cycle-t2-explained/) — KRX standing as the central counterparty for listed stock trades — is the exact same institution and the exact same underlying principle covered in this lesson; only the specific rules and margin models differ depending on whether the product is a listed stock or an OTC derivative.

## The Takeaway: CCPs Don't Eliminate Risk, They Concentrate It

The point worth holding onto is that a CCP doesn't erase risk from the financial system — it gathers up what used to be a sprawling web of bilateral credit exposures and manages it more efficiently from one place. Thanks to the layered defenses of netting, margin, and the default waterfall, individual trading relationships feel almost risk-free day to day. But that comes at the cost of a new kind of risk: a meaningful share of global financial risk now sits concentrated inside a small number of systemically critical CCPs. That's exactly why the Bank for International Settlements and national regulators scrutinize CCP capital adequacy, default fund sizing, and recovery-and-resolution planning so closely — if a major CCP itself ever faced a loss it couldn't absorb, the shock wouldn't stay contained to two counterparties; it would radiate out through every member connected to that CCP at once.

## Key Takeaways

- A CCP uses **novation** to split a single bilateral contract into two — "trader versus CCP" on each side — becoming the single counterparty that stands between every buyer and every seller in the market.
- **Netting** compresses offsetting positions to shrink total system-wide exposure, while **initial margin and variation margin** — collateral posted upfront and settled daily — cover whatever exposure remains.
- If losses exceed available collateral, the **default waterfall** absorbs them in order: the defaulter's own margin, then its default fund contribution, then the CCP's own capital, then the mutualized fund from non-defaulting members, and only as a last resort further assessments.
- The 2008 Lehman Brothers close-out never got past step 1 (margin alone covered it); the 2018 Aas default is a rare case that reached step 4, drawing on other members' mutualized default fund.
- KRX has operated as Korea's authorized CCP since 2013, covering both listed securities settlement and mandatory clearing of products like won-denominated interest rate swaps.
- A CCP is not a machine that deletes risk — it's a machine that relocates and concentrates it, which is exactly why the CCP's own financial health matters to the stability of the whole market.

## FAQ

### Do individual investors ever interact with a CCP directly?
Almost never. Retail investors place orders through a brokerage, and that brokerage — as a clearing member of the relevant exchange (KRX, in Korea's case) — is the one that actually faces the CCP. Still, the reason your trade settles safely and your shares actually transfer into your name rests entirely on this CCP structure operating underneath it.

### Can a CCP itself fail?
In theory, yes — but the multiple layers of the default waterfall, combined with capital and liquidity requirements imposed by regulators, make an actual CCP failure extremely rare in practice. That said, the possibility is exactly why CCPs are treated as institutions that are "too systemically important to fail," and why regulators require major CCPs to maintain separate recovery and resolution plans.

### Does netting only work because the CCP can see every counterparty's full position?
Exactly. In a bilateral world, if A trades separately with B, C, and D, there's no single place to add those positions together and offset them. Once everything runs through a CCP, though, all of A's trades become positions against that one same counterparty — so the CCP can see A's entire book at once and net it down to a single residual exposure.

> ⚠️ This article is for informational and educational purposes only and is not investment advice. Figures from the historical cases described here reflect official statements and reporting available at the time; the specific structure and thresholds of a default waterfall vary by clearinghouse and product.
