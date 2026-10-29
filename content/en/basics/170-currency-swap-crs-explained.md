---
slug: currency-swap-crs-explained
title: "What Is a Currency Swap (CRS)? Why Principal Changes Hands, Unlike an Interest Rate Swap"
description: "How a currency swap exchanges principal at both the start and maturity, why the cross-currency basis breaks covered interest parity, and how central bank currency swap lines backstop a currency under stress."
order: 170
updated: 2026-10-29
keywords: ["what is a currency swap", "currency swap vs interest rate swap", "cross-currency basis explained", "covered interest parity", "Korea US currency swap line", "CRS rate meaning", "central bank dollar swap line"]
seo_audited: 2026-10-29
---

## Why a "Currency Swap Line" Keeps Coming Up When a Currency Is Under Pressure

Whenever a currency comes under heavy depreciation pressure, commentary often turns to whether the central bank will arrange — or already has — a currency swap line with a major counterpart like the US Federal Reserve. As covered in [What Is an Interest Rate Swap (IRS)?](/en/basics/interest-rate-swap-irs/), an interest rate swap stays within a single currency and never exchanges principal. A **currency swap (CRS)**, despite the similar name, is built around exactly the opposite feature: exchanging principal is the whole point of the contract. Why does one type of swap leave principal untouched while the other moves it twice, and how does that feature turn into a defense against currency pressure? This lesson walks through the mechanics of a currency swap, why its market price can diverge sharply from textbook theory, and why central-bank-to-central-bank currency swap lines are treated as an emergency backstop.

## What a Currency Swap Is: Principal at Both Ends, Interest in Between

A currency swap is a contract between two parties holding different currencies who exchange principal at the current spot exchange rate when the contract begins, and exchange it back at maturity — at **the same exchange rate agreed at inception**, not whatever the market rate happens to be by then. During the life of the contract, each side pays interest on the currency it's holding, calculated as fixed-for-fixed, floating-for-floating, or a mix of both. A party that lent out its home currency and received dollars, for instance, pays dollar interest for the life of the swap and receives interest in its home currency in return.

The critical design choice is that the exchange rate for unwinding the deal is locked in at inception. If the final re-exchange used the market rate prevailing at maturity, whatever the exchange rate did over the life of the contract would leave one side better off and the other worse off — the currency exposure on the principal itself would still be live. Fixing the unwind rate up front removes that exposure entirely at the moment the contract is signed; only the gap between the interest payments made and received over the life of the swap remains as the real economic outcome. This is the structural difference from the FX forward and non-deliverable forward (NDF) contracts covered in [Currency-Hedged vs. Unhedged ETFs](/en/basics/currency-hedged-vs-unhedged-etf/). A forward or NDF settles once, at maturity, against a rate fixed in advance, without principal ever actually changing hands — and it's typically used in short, sub-one-year contracts rolled over month after month. A currency swap, by contrast, physically exchanges principal at the start, exchanges interest throughout, and commonly runs for several years, making it the tool of choice for longer-term cross-border funding rather than short-dated hedging.

## Why Use One: Raising Foreign Currency Without Taking on Currency Risk

The most common corporate use of a currency swap extends the comparative-advantage logic from [interest rate swaps](/en/basics/interest-rate-swap-irs/) across currencies. A company that issues bonds directly in a foreign market often pays a premium simply for being an unfamiliar name to that market's investors. The same company may be a well-known, highly rated borrower at home, able to issue local-currency debt far more cheaply. By issuing in its home currency and then swapping both the principal and the interest obligation into the foreign currency it actually needs, the company can end up with a lower effective funding cost than issuing foreign-currency debt directly — a route Korean companies and banks commonly use to fund overseas plant construction or asset acquisitions in dollars.

Demand on the other side of the market often comes from exporters. A shipbuilder or heavy-industry firm with large, multi-year dollar receivables locked in typically wants to sell those dollars forward to eliminate its currency exposure. The bank taking the other side of that forward is left holding a short-dollar position of its own — one that rises in value if the won weakens and falls if it strengthens — and needs to offset it. Banks commonly do this by entering a currency swap that receives dollars and pays won. In other words, the currency swap market exists at the intersection of corporate long-term foreign-funding demand and banks hedging the forward positions they absorb from exporters.

## A Worked Example: Principal Moves Twice

Consider a simplified case. Korean Bank A needs roughly $74 million (at a won-dollar spot rate of 1,350) for five years. Issuing dollar bonds directly overseas would cost it 5.5% annually as an unfamiliar foreign issuer, but it can issue won-denominated bonds domestically at 4.0% as a well-known local borrower. Bank A issues the won bonds, then enters a currency swap with a foreign counterparty to convert that won principal into dollars.

| | At inception | Each year of the contract | At maturity |
|---|---|---|---|
| Bank A pays | ₩100 billion | Won interest (4.0%/yr) | — |
| Bank A receives | $74 million | Dollar interest (around 3.0%/yr) | — |
| At unwind | — | — | Bank A returns $74 million, receives back ₩100 billion, at the original 1,350 rate |

Combining the 4.0% won bond cost with the swap's terms, Bank A ends up funding its dollar need more cheaply than the 5.5% it would have paid issuing dollar bonds directly. Because the unwind rate was fixed at 1,350 from the outset, however the won-dollar rate moves over those five years, the principal itself carries no currency exposure for Bank A. Only the gap between the won interest it pays and the dollar interest it receives is the real cost or benefit of the arrangement.

## The CRS Rate and the Basis: Where Theory and Reality Diverge

The fixed rate exchanged in a currency swap is called the **CRS rate**. In theory, borrowing dollars by swapping out of won should cost exactly the same as borrowing won directly, once fully hedged — a relationship known as **covered interest parity (CIP)**, the same principle underlying the forward-pricing logic covered in [Currency-Hedged vs. Unhedged ETFs](/en/basics/currency-hedged-vs-unhedged-etf/). If CIP held exactly, the CRS rate would match the interest-rate gap between won and dollars, no more and no less.

In practice, that equality breaks down regularly. The gap between the actual CRS rate and what CIP would predict is called the **cross-currency basis**. A negative basis means it actually costs more to obtain dollars through a swap than the plain interest-rate differential alone would suggest. Research from the Bank for International Settlements (BIS) finds that this basis has been a persistent, structural feature across multiple currencies since the global financial crisis, and traces much of it to **balance-sheet constraints at banks**. Since Basel III raised the capital cost of holding large swap books, dealers who might otherwise arbitrage away the basis now demand compensation for tying up balance-sheet capacity, and that compensation shows up as the basis itself. In other words, a persistently nonzero basis isn't necessarily a sign of market inefficiency — it reflects regulatory and balance-sheet constraints left over from the post-crisis financial system, now baked directly into the price.

Korea's own market offered a dramatic illustration of this during the 2008 financial crisis. Shipbuilders had accumulated years of forward dollar sales, and the banks absorbing those forwards rushed simultaneously to receive dollars and pay won through currency swaps to hedge their own exposure. That surge in demand hit just as the global dollar funding squeeze cut off the arbitrage capital that normally keeps the basis in check, and Korea's CRS rate briefly collapsed into negative territory. Under normal conditions, the side receiving won interest should always receive a positive rate — but with demand for dollars overwhelming supply, lenders of won effectively had to pay extra just to attract dollars into the market. That episode is still cited today as a textbook leading indicator of acute dollar shortages in the domestic financial system.

## The Korea-US Currency Swap Line: A Central Bank Backstop, Not a Market Trade

Everything discussed so far describes market transactions between private banks and companies. What gets called the "Korea-US currency swap" is a different animal entirely: a **central-bank-to-central-bank currency swap** between the Bank of Korea (BOK) and the US Federal Reserve. Where private swaps serve routine funding and hedging needs, a central bank swap line exists as an emergency backstop for moments when a country's dollar liquidity dries up sharply. The structure has the Bank of Korea posting won and receiving dollars from the Fed, then auctioning those dollars out to domestic banks that need them. Korea has entered this arrangement with the Fed twice — first during the 2008 global financial crisis, then again during the 2020 COVID-19 shock.

The arrangement is often compared to an IMF bailout, but the two are fundamentally different. An IMF rescue package comes with conditionality — austerity measures or structural reforms attached to the funds. A central bank swap line is closer to two central banks exchanging each other's currency as mutual collateral, carrying no such policy conditions. It also works to ease the very basis deterioration described above: when a central bank supplies dollars directly, it reduces the scramble for dollars in the private market, which in turn eases the pressure pushing the local currency down. That said, the facility only operates within pre-agreed limits on amount and duration, and whether one gets arranged — and on what terms — depends entirely on the policy judgment of both central banks at the time.

## Key Takeaways

- A currency swap exchanges principal in two different currencies at both the start and maturity of the contract, with interest paid in each currency throughout — unlike an interest rate swap, which never exchanges principal at all.
- The exchange rate used to unwind the principal at maturity is fixed at inception, which removes currency exposure on the principal itself for the life of the contract; only the interest-payment gap remains as real economic exposure.
- Companies use currency swaps to raise foreign currency more cheaply by exploiting comparative advantage, while banks use them to hedge the dollar exposure they absorb from exporters' forward sales.
- Covered interest parity predicts the CRS rate should match the interest-rate gap between two currencies, but bank balance-sheet constraints and dollar supply-demand imbalances create a persistent cross-currency basis — as seen when Korea's CRS rate turned negative during the 2008 crisis.
- The Korea-US currency swap line is a central bank emergency liquidity facility, distinct from private CRS trading and from an IMF bailout, that directly supplies dollars to ease depreciation pressure without policy conditions attached.

## FAQ

### Isn't a currency swap basically the same thing as an FX forward or NDF?
They move in the same direction but are built differently. A forward or NDF settles once, at maturity, against a pre-agreed rate, without principal ever changing hands — and is usually used for short, sub-one-year hedges rolled over repeatedly. A currency swap physically exchanges principal at inception, pays interest throughout, and typically runs for several years, making it better suited to long-term foreign-currency funding than to short-term hedging.

### Does a widening cross-currency basis affect retail investors at all?
Direct exposure is rare, but the indirect effects matter. A sharply widening basis signals that dollars have become relatively harder to obtain in the domestic financial system, which can feed into the hedging cost of [currency-hedged ETFs](/en/basics/currency-hedged-vs-unhedged-etf/) and into won-dollar volatility more broadly. It's not a number most investors track directly, but it's a useful secondary gauge of financial-market stress.

### Does arranging a Korea-US currency swap line immediately stabilize the exchange rate?
Not automatically. The facility expands the dollar supply domestic banks can draw on, easing one root cause of a currency sell-off — a dollar shortage — but the exchange rate also responds to trade flows, foreign investment flows, and other factors the swap line doesn't touch directly. Historically, though, the announcement itself has often calmed market anxiety even before any dollars were actually drawn down.

> ⚠️ This article is for informational purposes only and is not investment advice. The historical cases and figures cited are for illustrating the underlying concepts; current terms and figures should be verified against official sources such as the Bank of Korea. Investment decisions and their outcomes are the sole responsibility of the investor.
