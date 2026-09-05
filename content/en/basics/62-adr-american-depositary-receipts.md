---
slug: adr-american-depositary-receipts
title: "What Is an ADR? Why It Can Trade at a Different Price Than the Local Stock"
description: "How an American Depositary Receipt is actually structured, why its price can drift from the local shares it represents, and what the SK Hynix Nasdaq ADR premium reveals about arbitrage frictions."
order: 62
updated: 2026-09-05
keywords: ["what is an ADR", "American depositary receipt explained", "ADR vs ordinary shares", "why does an ADR trade at a premium", "SK Hynix ADR premium", "ADR ratio explained", "ADR dividend currency conversion", "foreign stock ADR investing"]
seo_audited: 2026-09-05
---

## How Can Americans Trade a Korean Stock Without a Korean Brokerage Account

Buying shares in a company listed on the Korea Exchange normally means opening an account with a Korean brokerage, converting dollars to won, and trading during Korean market hours. Yet companies like SK Hynix, KT, and POSCO Holdings can be bought and sold by American investors in New York or on Nasdaq, in dollars, during US trading hours, through an ordinary US brokerage account. How is that possible without a second full listing? The answer is that the shares trading in the US aren't a duplicate listing of the same stock — they're a separate instrument called an **American Depositary Receipt (ADR)**. This lesson covers exactly how an ADR is constructed, and why a security meant to represent the same company can end up trading at a meaningfully different price than the local shares it's built on. The goal isn't to tell you when to buy or sell a particular ADR — it's to understand the mechanics of the instrument itself.

## An ADR Isn't a New Share — It's a Receipt for One Already Held in Custody

The word "depositary" is the key to the whole structure. A US depositary bank — typically a large custody bank like Citibank, JPMorgan, or BNY Mellon — buys or receives actual shares of the foreign company on its home exchange, and has those shares held by a local custodian bank in that country. Against those deposited shares, the depositary bank issues a separate certificate that trades in the US. That certificate is the ADR. Buying one ADR doesn't create new equity in the company — it buys a claim on shares that are already sitting in custody somewhere else. An ADR holder gets essentially the same economic rights as someone holding the local shares directly — dividends, and exposure to price gains — but what they legally hold is the receipt, not the underlying share itself.

How many local shares one ADR represents is set by the **ADR ratio**. It can be 1:1, or one ADR might represent four local shares, or one local share might be split across several ADRs. The ratio exists purely to put the ADR's price in a range US investors find familiar — usually somewhere in the tens of dollars per share — and doesn't change the company's underlying value or any shareholder's actual stake. If a local share trades at 200,000 won and the ratio is one ADR to four local shares, the ADR's theoretical value is those four shares' combined won value converted into dollars.

## Why Companies Bother Setting One Up

For a foreign company, an ADR is a far lighter lift than a full dual listing. A genuine second listing on a US exchange would mean satisfying the SEC's full registration and disclosure requirements from scratch. An ADR, issued through a depositary bank against shares that already trade at home, carries a comparatively simpler process. The company gains exposure to a much broader pool of US institutional and retail investors, along with added liquidity and visibility, while US investors get to buy a foreign company without opening a foreign brokerage account or converting currency themselves.

ADRs also come in tiers. A **sponsored ADR** is set up cooperatively with the company, which pays the setup costs and typically stays involved in its disclosures — in that case, the company usually has one unified ADR program. An **unsponsored ADR**, by contrast, can be issued by a depositary bank on its own initiative, without the company's cooperation, against shares already trading publicly — and it's possible for more than one bank to issue separate, competing unsponsored ADRs for the same company at once. Sponsored programs are further split into levels based on how formally they trade in the US, from Level 1 (over-the-counter only) up to Level 3 (a full listing on an exchange like the NYSE or Nasdaq, which can also be used to raise new capital). None of this shows up on a typical trading screen, where the ADR just looks like "a US-listed stock" — but the structure behind it varies considerably.

## In Theory, the ADR Should Just Track the Local Share

If an ADR is nothing more than a claim on the local share, its price should, in theory, always equal the local share's price times the ADR ratio, converted at the current exchange rate:

**ADR price (USD) = (local share price × shares per ADR) ÷ exchange rate (local currency per USD)**

Say the local share trades at 200,000 won, the won-dollar rate is 1,300, and the ratio is one ADR per four local shares. The theoretical ADR price works out to roughly (200,000 × 4 ÷ 1,300) ≈ $615. If that relationship held exactly, arbitrageurs would instantly buy whichever side was cheaper and sell the other, closing any gap. In liquid programs where converting freely between local shares and ADRs is straightforward, this relationship generally does hold up well in practice.

## Why the Gap Doesn't Always Close

The catch is that "buy the cheap side, sell the expensive side" is harder than it sounds. SK Hynix's Nasdaq ADR, listed in 2026, is a recent, well-documented example. After listing, the ADR repeatedly traded at a substantial premium to the local Korean shares — sometimes reported as high as roughly 50% above parity at points — even though arbitrage should, in theory, close that gap almost immediately.

The reason lies in the friction that blocks arbitrage from actually happening. First, converting between local shares and ADRs — depositing local shares with the custodian to create new ADRs, or canceling ADRs to redeem local shares — takes time, carries fees, and runs into each country's foreign-exchange rules. In Korea's case, structural limits on how freely foreign investors can source and hold won still make it cumbersome for an investor who bought the Nasdaq ADR to unwind that position back into won-denominated local shares. Second, when the ADR's actual float in the US represents only a small slice of total shares outstanding, scarcity alone can keep a premium from closing. Third, once an investor has already paid up for the ADR, they have little incentive to give up that premium by converting back to local shares — so the arbitrage never gets the offsetting demand it needs on the other side. The bridge between local shares and ADRs exists in theory, but the cost, friction, and lack of incentive to cross it can keep the gap open far longer, and far wider, than the simple pricing formula would suggest.

## A Numerical Look at What a Premium Actually Means

Continuing the earlier example: if the theoretical ADR price is about $615, but the ADR actually trades at $700, that's roughly a 13.8% premium over parity.

| | No gap (baseline) | With a premium |
|---|---|---|
| Local share price | 200,000 won | 200,000 won |
| Exchange rate (won/USD) | 1,300 | 1,300 |
| Theoretical ADR price (1:4 ratio) | ~$615 | ~$615 |
| Actual ADR trading price | ~$615 | $700 |
| Gap vs. local shares | 0% | ~+13.8% |

Notice that neither the local share price nor the exchange rate changed between these two columns. The $700 price isn't the market pricing in stronger fundamentals — it's a premium generated entirely inside the US market, by an imbalance between demand for the ADR and the float actually available, combined with the friction that keeps investors from converting it back into local shares. If new ADR supply were issued, or conversion between the two suddenly got easier, that premium could compress quickly. As long as the conversion path stays blocked, though, the gap is a real, ongoing risk that sits on top of whatever happens to the underlying stock — a variable an ADR buyer carries that a local-share buyer doesn't.

## Currency Shows Up Twice for ADR Holders

One thing ADR investors often overlook is how much currency does. Since the ADR's price formula already runs the local share price through the exchange rate, the ADR's dollar value moves with the currency even if the local share price doesn't budge — a weaker local currency drags the ADR's dollar value down, and a stronger one lifts it. The same applies to dividends: a company paying dividends in its home currency has the depositary bank convert them into dollars before passing them to ADR holders, and the fees and exchange rate at that moment both affect what actually lands in an investor's account. In other words, an ADR holder carries the underlying company's business risk plus the currency exposure covered in [How Exchange Rates Affect Corporate Earnings](/en/basics/currency-effects-on-earnings/) — twice over, once inside the company's own results and once again in how the ADR itself is priced and paid out.

## Takeaway

- An ADR isn't a new share of stock — it's a certificate a US depositary bank issues against local shares it holds in custody abroad, giving the holder a claim on those shares rather than the shares themselves.
- The ADR ratio sets how many local shares one ADR represents; it's a price-scaling convention, not a change to the company's underlying value or shareholders' stakes.
- In theory, an ADR's price should equal the local share price times the ratio, converted at the exchange rate — but conversion friction, regulation, and limited float can keep a real premium or discount in place for a long time.
- SK Hynix's Nasdaq ADR shows this in practice: arbitrage exists on paper, but when converting freely between local shares and ADRs is hard, the price gap doesn't close on its own.
- ADR investors carry the underlying company's business risk, the risk that the local-share/ADR gap moves against them, and currency exposure both in the company's results and in how dividends get converted.

## FAQ

### Should I buy the ADR or the local shares?
Neither is categorically better. Local shares trade in the home currency through a local brokerage; ADRs trade in dollars through a US brokerage, with different trading hours, liquidity, and the price-gap risk described above. Which makes sense depends on your account access, tax treatment, and how much currency-conversion convenience is worth to you.

### If an ADR trades at a premium, am I overpaying?
You are paying more than the parity value implied by the local shares, but that doesn't automatically mean a loss. The premium can reflect a genuine liquidity or access advantage, and conversion friction can keep it in place for a long time. What's worth watching is that if the premium compresses suddenly, the ADR can move by more than the underlying local shares do over that same period.

### Do all foreign companies use ADRs specifically in the US?
The US-specific version is called an ADR, but the same structure exists outside the US under the name **GDR (Global Depositary Receipt)**, letting shares trade through depositary banks in markets like Europe. The mechanics are essentially identical — only the market where the receipt trades differs.

### Is an unsponsored ADR riskier to hold?
Not inherently — the main difference is that the company itself is less involved in an unsponsored program's disclosures. The added burden is that when multiple depositary banks issue separate unsponsored ADRs for the same company, an investor needs to check which bank issued the one they're buying and how its ratio and fees compare, since these details aren't always uniform across programs.

> ⚠️ This article is for informational purposes only and is not investment advice. You are solely responsible for your own investment decisions.
