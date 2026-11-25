---
slug: synthetic-etf-swap-explained
title: "What Is a Synthetic ETF? How Swap-Based ETFs Track an Index Without Holding Its Stocks"
description: "How synthetic ETFs use swap contracts instead of real holdings to deliver an index's return, how counterparty risk arises, and how collateral is used to contain it."
order: 225
updated: 2026-11-25
keywords: ["what is a synthetic ETF", "synthetic ETF explained", "swap-based ETF risk", "synthetic ETF counterparty risk", "synthetic ETF vs physical ETF", "synthetic ETF collateral"]
seo_audited: "2026-11-25"
---

## An ETF That Tracks an Index Without Holding Any of It

Read enough ETF prospectuses and eventually you'll run into a line like this: "the fund does not directly purchase the index's constituent securities; instead, it receives the index return through a swap agreement." [What Is an ETF](/en/basics/etf-basics/) described an ETF, at its core, as a fund that holds a basket of real securities. This line breaks that assumption outright. If the basket is empty, how does the fund still deliver the index's return? The answer: it holds a contract instead of the holdings. Funds built this way are called **synthetic ETFs**, and the path their returns travel is fundamentally different from an ordinary ETF's. Synthetic structures have grown steadily in Korea too, especially for commodities, niche overseas indices, and leveraged/inverse products — which makes it worth understanding exactly how the mechanism works and what new risk it brings with it.

## What a Synthetic ETF Actually Is: Buying and Selling Returns Through a Swap

An ordinary physical ETF takes investor money and uses it to actually buy the index's constituent stocks. When the index rises, the value of what the fund holds rises right along with it — a relationship that's completely intuitive. A synthetic ETF skips that step. The fund enters into a **total return swap (TRS)** with a bank or securities firm, agreeing to exchange "the return on whatever the fund actually holds" for "the return on the target index." That counterparty is called the **swap counterparty**. The fund takes the money it raised from investors and buys a different set of assets entirely unrelated to the index — a so-called **substitute basket** — then hands the return on that substitute basket over to the swap counterparty, and in exchange receives the index's return, delivered in full. In other words, what the fund actually owns and what the investor is paid have no direct relationship to each other; a swap contract is the only thing connecting the two. This adds a new party to the chain. A physical ETF runs on three links — investor, fund, underlying assets — but a synthetic ETF inserts a fourth: the swap counterparty. And ultimately, the investor's return now depends on whether that counterparty makes good on its promise.

## Why Some Indexes Can Only Be Tracked This Way

The synthetic structure looks like an unnecessary complication, so why use it at all? Because some indexes genuinely can't be replicated physically — or doing so would be prohibitively expensive. Crude oil futures can't be stored as physical barrels. Some emerging-market indexes restrict direct foreign ownership of the underlying stocks. Leveraged and inverse products need to deliver exactly 2x or -1x the daily index return, which requires rebalancing a position every single day. For indexes like these, buying and holding the actual constituents either fails to track the index accurately or drives transaction costs and operational complexity through the roof. If a swap counterparty is willing to guarantee "I'll deliver that exact return," the fund can hand off the entire headache of physical replication and simply collect a clean return instead. [ETF Tracking Error vs Premium/Discount to NAV](/en/basics/etf-tracking-error-premium-discount/) explained how different replication methods leak tracking error at different points. Synthetic replication is best understood as a trade: it squeezes that tracking error down to near zero through a single contract, in exchange for taking on a different kind of risk entirely.

## Counterparty Risk: What Happens If the Swap Counterparty Fails

That different risk is **counterparty risk**, and it's the most fundamental consequence of this structure. If the swap counterparty can't deliver the agreed index return on time, the fund can't pass that return through to investors either. The worse scenario is outright default or bankruptcy of the counterparty. In that case, the size of the fund's loss isn't determined by how much the index gained — it's determined by how much of what's owed by the counterparty can actually be recovered at that moment. The index itself could have performed perfectly well, and investors could still take a loss purely because of the counterparty's credit problems. This is the fundamental line separating synthetic ETFs from physical ones. A physical ETF investor only has to worry about the businesses that make up the index. A synthetic ETF investor takes on an entirely separate layer of risk on top of that: the financial health of the institution on the other side of the contract.

## How Collateral Contains the Risk: Funded vs. Unfunded Swaps

Leaving that risk unmanaged would make synthetic ETFs a non-starter as an investment product, so **collateral** is built into the structure specifically to cap the exposure. There are two broad structures.

In a **funded swap**, the fund hands the entire pool of investor money over to the swap counterparty, and in return the counterparty posts collateral back to the fund. Because the full principal crosses over to the counterparty under this model, how much collateral is posted — and what it's made of — matters enormously. In an **unfunded swap**, the fund instead uses investor money to buy the substitute basket directly and holds it itself, settling only the *difference* between the substitute basket's return and the index's return with the counterparty on a regular basis. Because the fund holds real assets from the start here, overall exposure to the counterparty stays comparatively small. In Europe, the 2008 financial crisis drove home the hard truth that even large financial institutions can fail, and regulators responded by tightening rules (such as the UCITS framework) that cap swap exposure as a percentage of net asset value and require collateral to be marked to market daily, with any shortfall topped up immediately. Synthetic ETFs in Korea likewise operate under requirements around counterparty exposure and collateral levels, and fund managers disclose swap-counterparty details and collateral composition in periodic reports. That said, exact collateral ratios and disclosure standards vary by product and over time, so checking the prospectus and the latest fund report directly is the only reliable way to confirm the details for any specific ETF.

## A Worked Example: Why Collateral Ratios Run Above 100%

Here's how the numbers play out. Say a synthetic ETF raises $100 million from investors and enters a funded swap with a securities firm. As part of the deal, that firm posts collateral back to the fund, agreeing to maintain it at 110% of net asset value — so $110 million in high-quality, liquid assets (government bonds, large-cap blue chips, and the like) sits with the fund as collateral. If the index rises 10%, the swap counterparty owes the fund $110 million ($100 million principal plus $10 million in gains). If the counterparty happens to default at exactly that moment, the fund can't collect the full $110 million it's owed under the contract — but it can liquidate the $110 million in collateral it was already holding, covering most of that loss. The reason the collateral ratio is set above 100% — say, at 110% rather than exactly 100% — is to build in a cushion for the price slippage and timing lag involved in actually selling off that collateral, plus the possibility that the collateral's own value drops during the kind of market turmoil that triggers a counterparty default in the first place. A synthetic ETF with a thinner collateral cushion, or one whose collateral composition is opaque, leaves investors exposed to a correspondingly larger potential loss in that same scenario.

## Physical vs. Synthetic ETFs: What to Compare

| | Physical ETF | Synthetic ETF |
|---|---|---|
| Source of return | Actual constituent holdings | Contract with a swap counterparty |
| Tracking error | Can grow with large constituent counts or low liquidity | Often kept tight by the contract itself |
| New risk introduced | None beyond the underlying assets | Counterparty risk (swap counterparty's creditworthiness) |
| Best suited for | Liquid indexes that are cheap and easy to buy directly | Indexes that are hard or costly to replicate physically (commodities, some overseas indexes, leveraged/inverse) |
| What to check | Holdings, expense ratio | Swap counterparty, collateral ratio and composition, collateral revaluation frequency |

Neither structure is categorically better. For a liquid, easy-to-replicate index like the KOSPI 200 or the S&P 500, there's little reason to reach for a synthetic structure in the first place. But for an index that would otherwise produce large tracking error or is nearly impossible to manage physically, a synthetic structure can be a reasonable choice that delivers a more precise return — provided the investor accepts the counterparty risk that comes with it. The real question to ask is twofold: why is this particular index hard to replicate physically, and what new risk am I taking on in exchange for sidestepping that difficulty?

## What Investors Should Check

Before investing in a synthetic ETF, the prospectus and periodic fund reports are worth checking for at least the following:

- **Replication method**: Confirm whether the fund is physically or synthetically replicated. The ticker or fund name alone often won't tell you — you need to check the prospectus directly.
- **Swap counterparty**: Find out who the counterparty is, and whether exposure is concentrated with one institution or spread across several. More diversified counterparties mean one firm's credit trouble does less damage to the fund as a whole.
- **Collateral ratio and composition**: Check what percentage of net asset value the collateral represents, and whether it consists of liquid, high-quality assets like government bonds and blue-chip stocks.
- **Collateral revaluation frequency**: How often (daily, weekly) the collateral's value gets marked to market and topped up if it falls short is itself a signal of how seriously risk is being managed.
- **Relationship between the fund manager and the swap counterparty**: If an affiliated securities firm within the same financial group serves as the swap counterparty, the two sides' interests may not be fully independent — worth factoring into your assessment.

## Key Takeaways

- A synthetic ETF doesn't hold the index's constituent securities directly; it delivers the index's return through a contract with a swap counterparty instead.
- This structure is mainly used for indexes that are difficult or expensive to replicate physically — commodities, certain overseas or emerging-market indexes, and leveraged/inverse products.
- The key difference from a physical ETF is counterparty risk: even when the index itself performs fine, a credit problem at the swap counterparty can produce a loss.
- That risk is contained through collateral, typically set above 100% of net asset value and revalued periodically to cover any shortfall.
- Before investing, check the replication method, swap counterparty structure, and collateral ratio and revaluation frequency directly in the prospectus and fund reports.

## FAQ

### Should I avoid synthetic ETFs altogether?
Not necessarily. When an index is hard to replicate physically and you want tight tracking with minimal error, a synthetic structure can actually be the more precise choice. The key is recognizing that it introduces counterparty risk that a physical ETF simply doesn't have, and checking the collateral structure and counterparty details before investing.

### If the swap counterparty goes bankrupt, do I lose my entire investment?
That outcome is designed to be very unlikely. Collateral is typically held at or above the fund's net asset value in advance, so even if the counterparty defaults, liquidating that collateral can cover most of the loss. That said, the time lag involved in actually selling the collateral, and the possibility that the collateral's own value drops at the same time, mean the risk of some loss isn't reduced all the way to zero.

### How can I tell if an ETF is synthetic or physical?
Check the fund details provided on the asset manager's website or your broker's app, or look for the "replication method" section of the prospectus. Two ETFs tracking the exact same index can use different replication methods depending on the manager, so it's worth confirming directly rather than guessing from the ticker or fund name.

### Are synthetic ETFs the same thing as ETNs?
They look similar on the surface, but the legal structure is different. A synthetic ETF is a fund with a collateral buffer specifically designed to limit counterparty risk. An [ETN (Exchange-Traded Note)](/en/basics/etn-exchange-traded-note-explained/), by contrast, is closer to an unsecured debt obligation issued directly by a securities firm. Both carry risk tied to an issuing or contracting institution's creditworthiness, but how much that risk is cushioned by collateral differs substantially between the two.

> ⚠️ This article is for informational and educational purposes only and is not investment advice regarding any specific ETF or asset manager. The figures used here are simplified, hypothetical examples meant to illustrate the structure. Actual collateral ratios, counterparty arrangements, and regulations vary by product and over time, so always confirm the current details in the prospectus and the latest disclosures from the fund manager before investing.
