---
slug: payment-for-order-flow-pfof-explained
title: "What Is Payment for Order Flow (PFOF)? How 'Commission-Free' Trading Actually Makes Money"
description: "How zero-commission brokers like Robinhood really get paid: the payment for order flow structure, NBBO and best-execution rules, and why the EU banned it while the US didn't."
order: 120
updated: 2026-10-04
keywords: ["what is payment for order flow", "PFOF explained", "how does Robinhood make money with no commission", "what is NBBO", "best execution rule explained", "why did the EU ban PFOF", "price improvement trading", "payment for order flow controversy"]
seo_audited: 2026-10-04
---

## If the Commission Is Zero, Where Does the Broker's Money Come From

Anyone who trades US stocks eventually runs into the same puzzle: brokers like Robinhood or Webull charge nothing to place a trade, yet they still run a business — and some went public. The answer sits somewhere the investor never sees. These brokers don't send a customer's order straight to an exchange. Instead, they hand it to a specific market maker, and get paid for doing so. That arrangement is called **payment for order flow (PFOF)**. [How Market Makers and Dark Pools Work](/en/basics/market-microstructure-basics/) covered how a market maker earns the bid-ask spread. This lesson goes one step further: why a market maker would pay anyone, in the first place, for the privilege of filling a retail investor's order — and whether that arrangement actually leaves the investor better or worse off.

## How PFOF Actually Works: A Path That Skips the Exchange

In the textbook picture, a broker routes a customer's order straight to an exchange's order book, where it matches against someone else's opposing order. PFOF inserts a step in between. Instead of routing to an exchange, the broker sends the order to a large **wholesale market maker** — firms like Citadel Securities or Virtu Financial. That market maker fills the order directly out of its own inventory (a process called **internalization**) and, in exchange, pays the broker a small per-share or per-contract rebate. The broker banks those rebates to fund the "zero commission" it advertises to customers. The investor pays nothing directly, but someone is still paying for that fill — it's just that the market maker is paying the broker, not the investor paying the broker. The money hasn't disappeared; only who pays it, and through which channel, has changed.

## Why Would a Market Maker Pay to Get That Order in the First Place

That leaves the central question: a market maker isn't a charity, so paying out rebates has to leave something behind. The answer is that retail orders are, statistically, "safe" business for a market maker. [What Is a Market Maker?](/en/basics/market-microstructure-basics/) covered inventory risk — the danger a market maker faces from counterparties who already know which way a price is about to move, like hedge funds or high-frequency algorithms. Fill those orders and the price often moves against the market maker right after the trade. A small retail order, by contrast, is classified as **uninformed order flow**: it carries almost none of that directional information. A market maker that captures a steady, high volume of this kind of flow can earn the spread reliably and predictably, which is exactly why it's willing to pay brokers for the right to see it first. PFOF, in other words, only exists because market makers have concluded that retail orders are easy to trade against.

## So Does the Investor Lose Out? NBBO and the Best-Execution Duty

The obvious worry follows naturally: if brokers and market makers are passing money back and forth, doesn't that cost eventually show up as a worse fill price for the retail investor? US regulators built in a safeguard against exactly that. The key reference point is the **National Best Bid and Offer (NBBO)** — the best bid and best ask available across every exchange at that instant. US brokers carry a **best execution duty**, meaning they must fill a customer order at a price no worse than the NBBO. In practice, most wholesale market makers provide **price improvement** — filling slightly better than the NBBO — and that's the core justification the PFOF model leans on: "we internalize the order and collect a rebate, but in exchange we give you a marginally better price than the public market would." The catch is that this improvement is typically tiny, often around a penny per share, leaving an open question that's never fully settled: is that improvement large enough to offset the rebate changing hands behind the scenes, or is it a nominal gesture investors barely notice?

## A Numerical Example

Picture a simplified, hypothetical case. A stock's NBBO shows a bid of $9.98 and an ask of $10.02. An investor places a market order to buy 100 shares, and the market maker internalizes it, filling at $10.01 — a penny better than the $10.02 NBBO ask, counted as price improvement. The investor got a nominally better price. But the market maker may have sourced those shares from inventory bought even cheaper, or matched the order almost simultaneously against another investor's sell order, pocketing the spread on both sides. Out of that total profit, a fraction — say $0.002 per share — flows back to the broker as a PFOF rebate. Looked at as a single trade, the investor, the market maker, and the broker all come away with something. The hard part is that this tiny margin repeats across hundreds of millions of trades, and no individual investor has a practical way to verify whether their specific order would have fared better routed some other way.

## Why the Debate Never Settles: Conflicts of Interest and GameStop

The deepest criticism of PFOF is a structural conflict of interest. A broker's incentive to route orders to whichever market maker pays the most doesn't automatically line up with its duty to find customers the best possible fill. That conflict exploded into public view during the GameStop (GME) frenzy of 2021. When Robinhood temporarily restricted buying in a handful of meme stocks, suspicion immediately turned to its PFOF relationships with market makers, and the episode landed the company in US congressional hearings. In 2022, the SEC proposed a new "order competition rule" that would have forced many retail orders through auction-style venues instead of being routed directly to a wholesale market maker — but industry pushback has kept that rule from being finalized for years. The EU took the opposite path entirely: a revised MiFIR banned PFOF on a phased timeline starting in 2024, and Germany's temporary carve-out — covering PFOF-reliant neobrokers like Trade Republic and Scalable Capital — finally expired on June 30, 2026, meaning investment firms across the entire EU can no longer accept any fee or benefit for routing orders to a specific venue. Two of the world's largest equity markets looked at the same practice and reached opposite conclusions — "ban it" versus "allow it, but disclose it" — which tells you this is less a pure efficiency question than a genuine disagreement about what investor protection actually requires.

## It Matters Even More in Options

Everything above was framed around stock trades, but PFOF plays an even bigger role in options. Because options combine underlying, strike, and expiration into effectively unlimited distinct contracts, liquidity in any single contract tends to be much thinner than in the underlying stock, and bid-ask spreads run wider as a result. Wider spreads mean more profit per fill for a market maker, so PFOF rebates on options orders are typically set far higher, per contract, than the per-share rebates on stock orders. It's common for options flow to generate a larger share of a "free" broker's total PFOF revenue than stock flow does — which means an investor who trades options frequently is more exposed to this structure than one who sticks to plain stock trades.

## A Second Concern: Price Discovery

The price discovery debate covered in [market microstructure basics](/en/basics/market-microstructure-basics/) around dark pools applies here too, in a similar form. If most retail orders never touch the public order book because they're internalized directly by a market maker, the orders that do meet on the public exchange skew more heavily toward institutions and high-frequency traders. Critics argue this gradually weakens the public market's price-discovery function over the long run. Defenders counter that internalized prices are themselves anchored to the public NBBO, and that individual retail orders don't carry much price-discovery-relevant information to begin with. Neither side has settled the argument, but it's one more reason PFOF isn't simply a side payment between a broker and a market maker — it touches the mechanics of how prices get set in the first place.

## Why Korea Doesn't Really Have This

The reason almost no Korean brokerage offers genuinely zero-commission trading traces back to this same structure. The Korea Exchange (KRX) runs on a pure order-driven market where investor orders match directly against each other, so the wholesale-market-maker ecosystem that PFOF depends on in the US never really took root. Domestic brokers still rely on traditional trading commissions as a core revenue line, leaving little incentive to give that up for an unproven alternative like PFOF. That said, Korean investors aren't entirely insulated once they trade US stocks through an overseas brokerage account: many domestic brokers route that order flow through US-based partner brokers or market makers, so PFOF may well be embedded somewhere along the path those orders eventually travel.

## Why This Matters to You as an Investor

There's no need to scrutinize PFOF before every single trade. What matters is not mistaking "zero commission" for "this trade costs nothing to process." Processing a trade always costs something, and someone always pays it. If you trade US stocks regularly, it's worth knowing that brokers disclose quarterly order-routing reports (the SEC's Rule 605 and 606 reports) showing which market makers they route to and how much price improvement they actually deliver. More broadly, the real habit worth building is looking past "free" marketing language to find where a financial service actually earns its money — PFOF is far from the only example of that pattern in the industry.

## Takeaway

- PFOF is the arrangement where a broker routes customer orders to a specific market maker instead of an exchange, in exchange for a rebate — the revenue engine behind "commission-free" trading in the US.
- Market makers pay for this flow because retail orders are statistically "uninformed," making them easier and more predictable to trade against than institutional or algorithmic orders.
- US rules require fills at a price no worse than the NBBO, with most wholesale market makers offering small price improvement — but whether that improvement fully offsets the rebate changing hands remains disputed.
- The 2021 GameStop episode sharpened conflict-of-interest concerns; the US responded with stronger disclosure rules while the EU moved to an outright ban, fully in effect across the bloc since June 30, 2026.
- Korea's order-driven exchange structure never grew a wholesale-market-maker ecosystem, but Korean investors trading US stocks through overseas accounts may still be indirectly exposed through routing partners.

## FAQ

### If PFOF exists, does that mean retail investors lose money?
Not necessarily on any single trade — price improvement often means a fill slightly better than the NBBO. The structural concern is that no individual investor can easily verify whether that improvement fully offsets the rebate paid behind the scenes, or whether the order would have fared even better routed some other way.

### Does trading US stocks through a Korean broker expose me to PFOF?
Not directly in a way you'd notice, but it's possible. Many Korean brokers route overseas orders through US-based partner brokers or market makers, and PFOF may be embedded somewhere in that chain. Disclosures alone don't make the exact impact on your fill easy to trace.

### Why hasn't the SEC banned PFOF outright?
It proposed an order-competition rule in 2022 that would have pushed many retail orders through competitive auctions, but industry and some investor-group pushback has kept it from being finalized. The US has leaned toward stronger Rule 605/606 disclosure instead, putting the burden on investors and researchers to evaluate execution quality themselves.

### Why did the EU ban PFOF entirely?
EU regulators concluded that PFOF creates a structural conflict of interest between brokers and market makers that can work against a client's best interests. A revised MiFIR phased in the ban starting in 2024, and Germany's temporary exemption — carved out mainly for its PFOF-dependent neobrokers — expired on June 30, 2026, making the ban uniform across the entire bloc.

> ⚠️ This article is for informational and educational purposes only and is not investment advice. The numerical example is a simplified hypothetical used to illustrate the mechanism and does not represent the terms of any actual trade. Investment decisions and their outcomes are the investor's own responsibility.
