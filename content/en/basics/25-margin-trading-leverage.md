---
slug: margin-trading-leverage
title: "What Is Margin Trading? How Leverage Amplifies Gains and Losses Together"
description: "How borrowing to buy stocks multiplies your return on capital, how maintenance margin and margin calls force liquidation, and what makes leverage costly to hold over time."
order: 25
updated: 2026-08-17
keywords: ["what is margin trading", "margin call meaning", "how does leverage work in investing", "maintenance margin explained", "buying on margin risk", "forced liquidation stocks", "margin trading vs cash account", "leverage investing risk"]
---

## What "I Bought Double on Margin" Actually Means

Investor forums are full of people describing a trade as "fully leveraged" or "bought on margin." What that means in practice is buying more stock than your own cash could cover, using money borrowed from your broker. Unlike the derivatives covered in [Options as Insurance](/en/basics/options-as-insurance/), the mechanism behind margin trading itself is simple: you just borrow money and buy more shares. The complexity hides in the arithmetic that follows. The moment borrowed money enters the picture, your return calculation changes shape — and so does the size of the loss you can actually absorb. This lesson isn't about when to open or close a margin position; that's trading-strategy territory. It's about why leverage amplifies gains and losses by the exact same multiple, and what it actually costs to keep that leverage running.

## The Basic Structure: Borrowing Against Your Own Stock as Collateral

In margin trading, your broker lends you part of the purchase price, and the shares you buy with that combined capital become the collateral for the loan. Say a stock has a 40% initial margin requirement: with $4,000 of your own cash, you can buy $10,000 worth of shares. The other $6,000 is a loan from your broker, and interest accrues on it daily. The key detail is that the shares you just bought are, in full, the collateral backing that loan. It might look like you owe nothing until you sell — but because the collateral's value falls right along with the stock price, your broker monitors that collateral value continuously, in real time. **Leverage** is simply the act of controlling a larger position than your own capital alone would allow — in this example, $4,000 of equity is controlling a $10,000 position, a leverage ratio of 2.5x. Stocks with lower margin requirements let you reach a higher ratio with the same equity, but that also means a smaller price move eats through your cushion above the loan balance that much faster. Margin requirements and eligibility vary by stock, based on volatility, market cap, and the exchange's own risk classification — highly volatile or distressed stocks are often excluded from margin eligibility entirely.

## Why the Same 10% Move Produces a Different Number

The mechanism boils down to one sentence: profit and loss apply to the full position, but your return is calculated against your own capital alone. Compare buying $4,000 of stock outright with no leverage, against buying $10,000 of the same stock using $4,000 of equity plus a $6,000 margin loan.

| | Cash account ($4,000) | Margin account ($4,000 equity + $6,000 loan = $10,000) |
|---|---|---|
| Stock +10% | Value $4,400, gain $400 (+10% return) | Value $11,000, equity after repaying loan: $5,000 (+25% return) |
| Stock -10% | Value $3,600, loss $400 (-10% return) | Value $9,000, equity after repaying loan: $3,000 (-25% return) |

A 10% move in the stock produces a 25% swing in the margin account's return on equity. That's because the $6,000 loan has to be repaid at a fixed dollar amount regardless of where the stock ends up, so the entire result of the price move lands squarely on your $4,000 of equity. This table doesn't even include interest yet — in practice, daily interest charges tilt the math slightly further against you. Leverage feels great when the multiplier works in your favor, but it's worth remembering the calculator doesn't care about direction: losses get amplified by exactly the same factor as gains.

## Maintenance Margin and Forced Liquidation: Why Your Broker Can Sell Without Asking

To protect the money they've lent, brokers set a **maintenance margin** — a floor requirement, commonly in the range of 25-30% of position value under regulatory minimums (though many brokers set their own house requirements higher), below which the ratio of your equity to the loan can't be allowed to fall. In the example above, if your $6,000 loan requires the position to stay above roughly $8,000-8,400 in value depending on the exact requirement, dropping under that line puts your account below maintenance.

Once that happens, the broker issues a **margin call** demanding more collateral, and if you can't meet it within the deadline, the broker sells your shares without asking — a **forced liquidation**. Two things make this especially unforgiving. First, it fires exactly when you'd least want to sell: when the price has fallen hard and your loss is already at its worst. Second, brokers typically calculate the liquidation using a price meaningfully below the prior close (the exact discount and buffer vary by firm), so the actual number of shares sold often exceeds what would be strictly needed to just clear the shortfall. In practice, your position gets closed on the broker's schedule and the broker's terms — not the stop-loss level you would have chosen — which is the exact opposite of the controlled exit described in [Risk Management Basics](/en/basics/risk-management-basics/).

## How This Differs in Korea: Misu Trading vs. Margin Trading

Korean brokers offer a second borrowing mechanism alongside standard margin trading, called *misu* trading. Both let you buy more than your cash covers, but the structure isn't the same.

| | Misu (unsettled) trading | Margin trading |
|---|---|---|
| Collateral | None — effectively unsecured buying ahead of settlement | Yes — the purchased shares serve as collateral |
| Deadline | Full payment due within 2 business days of the trade | Interest accrues over a loan term, repaid by maturity |
| If the deadline is missed | Forced liquidation | Forced liquidation once equity falls below maintenance |
| Nature of the arrangement | A short-term gap financed by the settlement cycle itself | A formal, interest-bearing loan backed by collateral |

Because misu trading has no collateral concept at all, it runs on a much tighter, faster clock than margin trading, and the window before forced liquidation kicks in is often shorter. Both let you take a bigger position than your cash alone allows, but the deadline pressure and forced-liquidation triggers attached to each are meaningfully different, and worth knowing apart.

## The Cost That Grows Quietly Over Time: Interest

Leverage doesn't only cost you in the extreme case of a forced liquidation. As long as you're carrying a margin loan, interest accrues every single day you hold the position. Margin interest rates vary by broker and loan term, but they commonly sit well above savings-account rates. That means a stock going nowhere is still a losing position on margin, purely from interest. The stock doesn't just need to rise — it needs to rise by more than the accumulated interest before the trade beats what a cash purchase would have returned. The longer you hold, the higher that break-even bar climbs, which is why leverage tends to reward short holding periods and punish long ones.

That interest cost also connects back to [How Interest Rates Affect Stock Valuations](/en/basics/interest-rates-and-stock-valuations/). When a central bank raises rates, brokers' own funding costs rise too, and that typically flows straight through into higher margin interest rates. In other words, a rate-hike cycle stacks two effects in the same direction at once: a higher discount rate that lowers the theoretical fair value of stocks, and a higher cost of carrying leverage on top of it. It's no coincidence that margin balances tend to feel especially painful during periods of rising rates.

## When Leverage Spreads Beyond One Account: The Margin Call Cascade

Everything above describes what happens inside a single account, but leverage's real danger shows up when many investors have built up similar margin positions at the same time. The mechanism scales up exactly as you'd expect. A falling price triggers margin calls across many accounts at once, the forced selling that follows pushes the price down further, and that further decline breaks the maintenance requirement on the next batch of accounts, triggering another round of forced selling. This self-reinforcing spiral is especially dangerous in stocks or sectors where margin balances have built up unusually high. That's part of why exchanges and regulators track aggregate margin balances as a standalone risk indicator — a period of rapidly rising margin debt is often read as a sign that structural fragility is building, one that can deepen any eventual pullback. This isn't a signal for timing any individual trade; it's a structural fact about how leverage, as a tool, can spill risk from one account into market-wide volatility.

## Takeaway

- Margin trading means borrowing from your broker to buy more stock than your own cash covers, with the purchased shares serving as collateral for the loan.
- Leverage concentrates the entire gain or loss on your equity, amplifying your return on capital — in both directions, by the exact same factor.
- Falling below the maintenance margin triggers a margin call; failing to meet it leads to forced liquidation on the broker's timeline and terms, not yours.
- Misu trading is short-term, uncollateralized buying against the settlement cycle, while margin trading is a formal, interest-bearing, collateral-backed loan — different mechanics with different deadlines.
- Margin interest accrues daily, so a stock needs to rise by more than the accumulated interest just to beat what a cash purchase would have returned.

## FAQ

### Can beginner investors use margin trading?
Brokers commonly set eligibility requirements — minimum account balance, trading experience, or a credit check — before approving a margin account. Confirm the specific requirements with your own broker before assuming you qualify.

### How do I avoid forced liquidation?
The most reliable approach is acting before your equity gets close to the maintenance threshold — adding collateral or trimming the position yourself to restore a safer ratio. Once a margin call actually arrives, the window to respond is much shorter.

### Is a leveraged ETF the same thing as margin trading?
Both amplify returns, but the mechanics differ. Margin trading is a loan you take out directly, carrying account-level risks like maintenance margin and forced liquidation. A leveraged ETF builds its multiplier internally using derivatives, so your account itself is never subject to a margin call. It carries a separate risk instead: because it resets its leverage daily, long-term holding returns can diverge meaningfully from what the stated multiple would suggest.

### Does using leverage always mean more risk?
A higher leverage ratio means the same price move produces a bigger swing in your return on equity, so risk grows unless you've worked out in advance how much loss you can absorb and how much cushion you have before hitting a forced liquidation. Leverage itself isn't the problem — using it without accounting for that amplification is.

### Why is maintenance margin calculated on my whole account instead of just the position I bought on margin?
If a margin account holds several different stocks, brokers typically calculate maintenance margin against the account's total equity and total loan balance, not stock by stock. That means a decline in an unrelated holding in the same account can also push your overall ratio below maintenance and trigger a margin call. Exact calculation methods vary by broker, so check your own account terms.

> ⚠️ This article is for informational purposes only and is not investment advice. Margin trading is a high-risk activity that can produce losses exceeding your original investment. You are solely responsible for your own investment decisions.
