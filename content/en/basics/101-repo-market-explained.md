---
slug: repo-market-explained
title: "What Is the Repo Market? How Overnight Treasury-Backed Loans Set Short-Term Rates and Drive Market Liquidity"
description: "Repurchase agreements let dealers borrow cash overnight against Treasury collateral — and set SOFR in the process. Here's how the plumbing works, and what the 2019 repo spike revealed."
order: 101
updated: 2026-09-24
keywords: ["what is the repo market", "reverse repo explained", "what is a repurchase agreement", "Fed reverse repo facility", "what is SOFR", "2019 repo rate spike", "ON RRP explained"]
seo_audited: 2026-09-24
---

## What Exactly Trades in the 'Repo Market'?

Financial headlines keep mentioning it: "the Fed's reverse repo balance has nearly drained to zero," or "repo rates spiked in overnight funding markets." In [How QE and QT Move Stock Prices](/en/basics/quantitative-easing-tightening-stock-market/), we covered how a central bank's balance sheet transmits into equity valuations. The repo market — short for repurchase agreements — is the plumbing that channel runs through. Banks, dealers, hedge funds, and money market funds (MMFs) borrow and lend trillions of dollars overnight in this market, every single night. Retail investors almost never touch it directly, but when it seizes up, short-term rates, Treasury yields, and eventually stock market liquidity all feel it. This lesson covers how a repo trade is actually structured, and why it became such a central tool of monetary policy.

## A Sale on Paper, a Collateralized Loan in Substance

A repo trade is legally structured as a sale of securities, but economically it functions as a short-term collateralized loan. Here's how it works: the party that needs cash — typically a dealer sitting on a large Treasury inventory — hands over Treasuries to a counterparty in exchange for cash today, and simultaneously agrees to buy those same securities back at a slightly higher price on an agreed date, usually the next business day. That price difference is, in effect, the interest — the repo rate. From the lender's side (an MMF or any institution with idle cash), the trade looks exactly like a one-day secured loan against Treasury collateral. Because that collateral is high quality, credit risk is minimal, which is why repo trades clear at rates well below unsecured borrowing. Lenders typically demand collateral worth slightly more than the cash they're lending — that cushion is called a **haircut**. Lend $100 million and take $105 million of Treasuries as collateral, and the haircut is 5%. Haircuts widen when the collateral is lower quality or longer-dated, or when the borrower's own credit looks shakier.

## Why Banks and Dealers Rely on This Market Every Single Day

Treasury dealers carry enormous bond inventories as a normal part of doing business, and funding all of that with their own capital isn't realistic. So every day, they pledge that inventory as collateral to borrow short-term cash in the repo market and keep their books running. On the other side sit MMFs, asset managers, and corporate treasuries with idle cash they want parked safely, even if only overnight. They favor repo over bank deposits because Treasury-backed lending is close to risk-free while still paying a better rate than a deposit account. This nightly meeting of dealers needing funding and cash-rich lenders wanting a safe overnight return sets the market-clearing rate known as **SOFR** (Secured Overnight Financing Rate), which replaced LIBOR as the US benchmark for short-term rates starting in 2022.

## Putting Numbers on an Overnight Trade

A concrete example helps. Say a dealer holds $100 million of Treasuries and wants to borrow against them overnight. With a 2% haircut, the counterparty only advances roughly $98 million in cash against that $100 million of collateral. At a repo rate of 5.30% annualized, one night's interest comes to about $98 million × 5.30% ÷ 365 — roughly $14,200. The dealer repays that principal plus interest the next business day and gets its Treasuries back. The dollar amount looks trivial, but multiply this by the trillions of dollars that roll over in the US repo market every single night, and a move of just a few basis points in this rate reflects — and can trigger — enormous shifts in where cash wants to sit across the entire financial system.

## Where the Leverage Comes From: Reusing the Same Collateral

Repo becomes more than a funding tool and turns into a leverage machine because collateral can be reused. A hedge fund buys Treasuries, pledges them in repo to borrow cash, uses that cash to buy more Treasuries, pledges those too, and repeats — building a position many times the size of its actual equity without adding a dollar of its own capital. This is the mechanism behind the so-called **basis trade**: borrowing cheaply via repo to exploit tiny price gaps between cash Treasuries and Treasury futures, a trade whose per-dollar return looks small but whose total profit scales up with the leverage applied. The catch is that this structure works smoothly right up until collateral values wobble or repo funding costs jump — at which point positions can get forced into a rapid, simultaneous unwind. The 2022 UK LDI crisis, mentioned in [Interest Rate Swaps (IRS)](/en/basics/interest-rate-swap-irs/), was exactly this: leveraged swap-and-repo positions unwound together as collateral values fell and margin calls piled up. Repo itself is a low-risk trade backed by quality collateral, but the longer the chain of reused collateral behind it, the faster a shock in one corner of that chain can ripple through the whole system.

## The Fed's 'Reverse Repo': Same Tool, Opposite Direction

This is where the terminology trips people up. Whether something counts as "repo" or "reverse repo" is always defined from the central bank's side. When the Fed lends cash to banks against Treasury collateral, that's a **repo (RP)** — it injects cash into the system. When the Fed instead takes in cash from a counterparty (an MMF, a bank) and hands out Treasuries as collateral, that's a **reverse repo (RRP)** — it drains cash out of the system. The Fed has run a standing **Overnight Reverse Repo Facility (ON RRP)** since 2013, letting a broad set of institutions — MMFs especially — park cash directly at the Fed overnight at a set rate. Its real function is to put a floor under short-term rates: if the private repo market ever offered a rate below what the Fed pays on ON RRP, cash would simply flow to the Fed instead, which is exactly why short-term rates rarely fall below that floor.

## September 2019: The Day Repo Rates Spiked to Near 10%

The clearest illustration of what happens when this plumbing clogs is the repo spike of September 2019. SOFR, which had been sitting quietly around 2%, jumped intraday to nearly 10% on September 17. The trigger was a pile-up of cash demands hitting the system on the same day: corporate quarterly tax payments and a large Treasury settlement both drained cash from the banking system simultaneously, right as bank reserves happened to be running lower than expected. Post-crisis regulations also made banks more reluctant to lend out their spare reserves into the repo market, so demand for cash outran the willing supply. The New York Fed stepped in immediately, injecting up to $75 billion a day in repo operations, and rates settled back down within days. In the aftermath, the Fed resumed outright Treasury purchases for reserve-management purposes — Chair Jerome Powell was explicit that this was "not QE" — and in 2021 it stood up a permanent **Standing Repo Facility (SRF)**, giving banks an always-available backstop to borrow against collateral whenever they need to.

## Why This Matters for Stocks: A Clogged Pipe Hits Risk Assets First

The repo market doesn't trade stocks directly, but it's the cash plumbing that the rest of the financial system, including equities, runs on. Banks, hedge funds, and asset managers fund a meaningful share of their Treasury and equity holdings through short-term repo borrowing. When that plumbing runs smoothly, funding stays cheap and institutions have ample room to hold risk assets; when it clogs, as in 2019, institutions scramble to cut leverage and build up cash instead. That reaction pushes in a similar direction to the portfolio-rebalancing dynamics covered in [How QE and QT Move Stock Prices](/en/basics/quantitative-easing-tightening-stock-market/), pulling money out of risk assets beyond just Treasuries. In practice, the Fed's ON RRP balance is one of the most closely watched liquidity gauges precisely because it tracks how bank reserves are shrinking as QT runs its course. A balance approaching zero signals that the system's spare cash cushion is being used up — which is why market participants worry that crossing that threshold raises the odds of another 2019-style squeeze in short-term funding.

## Takeaway

- A repo trade is structured as a bond sale but functions as an overnight loan collateralized by Treasuries; the market-clearing rate it sets is SOFR.
- Direction is always defined from the central bank's side: the Fed lending cash against Treasury collateral is repo (adds liquidity); the Fed taking in cash and handing out Treasuries is reverse repo (drains liquidity).
- The Fed's standing reverse repo facility (ON RRP) puts a floor under short-term rates, and its balance is widely tracked as a gauge of how much spare liquidity remains in the system.
- The September 2019 spike happened when reserve scarcity collided with a large tax and settlement date, briefly jamming the funding market's plumbing — the Fed's Standing Repo Facility (SRF) was built afterward to prevent a repeat.
- When repo markets seize up, institutions cut leverage and hoard cash, which can pull funding away from risk assets — including stocks — well beyond the Treasury market itself.

## FAQ

### Can individual investors trade in the repo market directly?
Almost never directly. But holding an MMF or short-term bond fund connects your cash to this market indirectly, since those funds typically invest a large share of their assets in repo to earn interest on idle cash.

### Is the repo rate the same as the Fed's policy rate?
No. The policy rate is set directly by the central bank, while the repo rate (SOFR) is a market rate determined by real supply and demand for Treasury-collateralized cash. The two stay closely aligned in practice because the Fed's reverse repo rate effectively acts as a floor under SOFR.

### Could a repo spike like 2019 happen again?
Many analysts think a repeat as extreme as 2019 is less likely now that the Fed's Standing Repo Facility gives banks a reliable backstop. Still, as ongoing QT continues to shrink bank reserves, short-term funding markets can grow more sensitive again — which is exactly why the Fed's ON RRP balance and reserve levels remain closely watched indicators.

### Are banks the only participants in the repo market?
No. Primary dealers (large broker-dealers), hedge funds, MMFs, pension funds, and even government-sponsored enterprises like Fannie Mae and Freddie Mac all borrow or lend in the repo market. Banks are just one participant among many — a large share of volume actually runs between MMFs and primary dealers.

> ⚠️ This article is for informational and educational purposes only and is not investment advice. Conditions in short-term funding markets change with many variables, so don't base investment decisions on this explanation alone.
