---
slug: share-pledge-loan-explained
title: "What Is a Share-Pledge Loan? Why a Controlling Shareholder's Collateral Call Can Crush a Stock"
description: "How controlling shareholders borrow cash by pledging their own shares instead of selling, how the maintenance-ratio margin call works, and how to check a company's pledge disclosures."
order: 130
updated: 2026-10-09
keywords: ["share pledge loan explained", "stock collateral loan forced sale", "controlling shareholder pledged shares", "pledge maintenance ratio", "forced liquidation margin call stock", "major shareholder share pledge disclosure", "stock-backed loan risk", "pledged shares change of control"]
seo_audited: 2026-10-09
---

## Why a Founder Pledges Shares Instead of Just Selling Them

A headline like "Company A's controlling shareholder pledges entire stake as collateral" tends to spook investors. Someone who controls the company has handed their shares over as collateral for a loan — and that detail alone explains why a falling stock price can trigger forced selling that has nothing to do with the founder's own wishes. Understanding why that happens means understanding how a share-pledge loan is actually structured. This lesson isn't about timing trades around a pledged stock — that belongs in a trading-strategy course. It's about how "pledging instead of selling" works as a transaction, and why that structure can amplify a price decline into a forced-selling spiral.

When a controlling shareholder needs cash, the simplest option is to just sell shares. But selling dilutes control, and crossing certain thresholds triggers disclosure obligations like the [5% beneficial ownership rule](/en/basics/beneficial-ownership-report-5-rule/) — a filing the market reads as "the controlling shareholder is cutting their stake," which can itself weigh on the price. A large one-time cash need, like an inheritance tax bill after ownership passes to the next generation, creates the same dilemma: selling shares to pay it reduces control by exactly that much. That's why controlling shareholders often borrow against their shares instead of selling them — a share-pledge loan.

## What "Pledging" Actually Means Legally

At the core of a share-pledge loan is a pledge (질권 in Korean) — a security interest that gives the lender the right to seize and sell the pledged asset if the borrower defaults, in order to recover the loan first. It's the share equivalent of a mortgage lien on real estate, except the collateral is stock instead of property.

When a controlling shareholder takes out a loan against shares, the lender — typically a brokerage or bank — registers a pledge over those shares. Ownership itself doesn't transfer: the borrower keeps dividend rights and, typically, voting rights. But the pledged shares move into an account controlled by the lender and stay locked there, and if the borrower fails to repay, the lender can enforce the pledge — selling the shares on the market to recover what's owed. In effect, the borrower keeps ownership but hands over the right to dispose of the shares as collateral.

## The Numbers: Loan Limits and the Maintenance Ratio

The risk-management framework behind a share-pledge loan looks a lot like ordinary [margin trading](/en/basics/margin-trading-leverage/), though the specific ratios vary by lender and product. A typical structure looks like this:

1. A controlling shareholder pledges shares of Company B worth 10 billion won at current market price.
2. The lender sets the loan limit at roughly 40–50% of collateral value. Here, the shareholder borrows 5 billion won — 50%.
3. Throughout the loan, the account must maintain a **maintenance ratio** — collateral value divided by loan principal — typically set around 140–160% depending on the product. At origination, that's 10 billion ÷ 5 billion = 200%, comfortably above the threshold.
4. If Company B's stock falls 35%, collateral value drops to 6.5 billion won, pulling the ratio down to 6.5 billion ÷ 5 billion = 130% — below the 140–160% threshold. The lender issues a margin call, demanding additional collateral or partial repayment.
5. If the borrower can't post more collateral or repay within the deadline, the lender force-sells the pledged shares on the open market to recover the loan. This is the forced liquidation (반대매매) step.

The critical point: forced liquidation executes mechanically, regardless of what the borrower wants. Even if the controlling shareholder believes "now is the worst time to sell," the lender is contractually obligated to liquidate once the ratio breaches its floor and no additional collateral arrives.

## Why This Gets Dangerous in a Falling Market — The Feedback Loop

What makes forced liquidation genuinely dangerous isn't just that shares get sold involuntarily — it's that the sale itself pushes the price down further. The larger the pledged stake, and the bigger that stake is relative to the stock's total float, the more a forced sale can move the price when it hits the market. A lower price drags the maintenance ratio down again, which can trigger another margin call and another round of forced selling. The feedback runs in the opposite direction of a [short squeeze](/en/basics/short-selling-explained/) — there, losses force buying that pushes the price up — but the underlying mechanic is the same: forced selling that begets more selling.

This dynamic shows up repeatedly in Korean market coverage during broad downturns, such as 2022, when concern about a controlling shareholder's pledged-share liquidation was cited as an added drag on specific stocks already under pressure. It tends to matter most for small- and mid-cap names with a thin float and a high concentration of ownership in the controlling shareholder's hands — a single forced sale of pledged shares can represent an outsized share of a typical day's trading volume and move the price sharply. In extreme cases, a large enough liquidation can even raise the possibility that control of the company itself changes hands.

## How Investors Can Check This — Reading the Disclosures

This risk isn't a complete black box. Listed companies disclose how much of the controlling shareholder's stake is pledged in the "Ownership by the Largest Shareholder and Related Parties" section of their annual report (사업보고서), filed on Korea's DART system. That filing shows the number and percentage of pledged shares and who holds the pledge. The higher the pledge ratio — and especially if the shareholder's overall stake is already thin and a large portion of it is pledged — the more exposed the stock is to both a control change and added downside pressure if the price falls.

Separately, whenever a new pledge contract is signed or an existing one is released, Korean exchanges require a specific ad hoc disclosure titled "Share Pledge Contract Entered Into or Terminated, Potentially Involving a Change of Largest Shareholder." The name alone often alarms investors into thinking control has already changed — but it only flags the possibility that it *could* change if the pledge were ever fully enforced; it doesn't mean a change happened at the time of filing. If the pledge is later enforced and shares actually get force-sold, that sale shows up after the fact as a disposal reason — "sale due to stock pledge forced liquidation and loan repayment" — in the officer/major-shareholder ownership change report.

## How This Differs From Ordinary Margin Trading

A controlling shareholder's share-pledge loan looks structurally similar to [margin trading](/en/basics/margin-trading-leverage/) — both involve borrowing against stock and both can end in forced liquidation — but the purpose and the borrower are different.

| | Margin trading | Controlling shareholder's share-pledge loan |
|---|---|---|
| Who borrows | Ordinary retail investors | Controlling shareholders, major shareholders, executives |
| Purpose of borrowing | To buy more of the same (or another) stock | Personal cash needs unrelated to the company (inheritance tax, business funding, etc.) |
| What's pledged | The shares just purchased | All or part of an existing, long-held stake |
| Disclosure | None — individual margin positions aren't public | Disclosed in annual reports and ad hoc filings |
| Market impact of forced liquidation | Spread across many individual investors | Concentrated in one stock — can meaningfully move the price or control |

Margin trading is a leverage tool for buying more stock. A controlling shareholder's share-pledge loan is a way to raise cash unrelated to the company while keeping the ownership stake intact. But both rest on the same core mechanic: collateral value falling below a set threshold triggers forced liquidation.

## Key Takeaways

- A share-pledge loan lets a controlling shareholder raise cash by pledging shares rather than selling them, preserving control while accessing liquidity.
- If the maintenance ratio — typically 140–160% — falls below the lender's threshold, a margin call follows; if unmet, the lender force-sells the pledged shares on the market.
- Forced liquidation executes mechanically regardless of the borrower's wishes, and the resulting sale can push the price down further, triggering additional rounds of the same cycle.
- Annual-report disclosures on the largest shareholder's pledge ratio, and ad hoc filings about pledge contracts tied to a possible change of control, let investors check this exposure for a given stock.

## FAQ

### Is it automatically a bad sign when a controlling shareholder pledges shares?
Not necessarily. Pledging is often used for ordinary cash needs like inheritance tax or business expansion. That said, a high pledge ratio combined with a thin float makes a stock more vulnerable to a sharp, forced-selling-driven decline if the price falls — a risk factor worth weighing alongside the stated reason for the loan.

### Does pledging shares also transfer voting rights?
Generally no. Voting rights and dividend rights normally stay with the shareholder who pledged the shares. The lender's rights are typically limited to seizing and selling the collateral if the loan isn't repaid, unless a specific contract spells out something different.

### Where can I check a company's pledge ratio?
Korea's DART filing system carries each listed company's annual report, which includes the "Ownership by the Largest Shareholder and Related Parties" section showing pledged share counts and ratios. Ad hoc filings issued whenever a pledge contract is signed or released are also worth checking.

### Can forced liquidation actually change who controls the company?
In theory, yes — if the pledged stake is large enough and gets fully liquidated, the shareholder's ownership can shrink enough to lose control. In practice, pledge ratios are often modest, and shareholders frequently respond to margin calls with more collateral or partial repayment, so a pledge disclosure by itself doesn't mean a change of control is imminent.

> ⚠️ This article is for educational purposes only and is not investment advice. Loan limits, maintenance ratios, and forced-liquidation thresholds vary by lender and product and can change over time. Check a company's latest disclosures and applicable regulations before making any investment decision.
