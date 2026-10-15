---
slug: gamma-squeeze-delta-hedging-explained
title: "What Is a Gamma Squeeze? How Market Maker Delta Hedging Pushes Stocks Higher"
description: "Why market makers must buy stock to hedge the calls they sold, how that hedge buying snowballs into a gamma squeeze, and how it differs from a short squeeze."
order: 143
updated: 2026-10-15
keywords: ["what is a gamma squeeze", "delta hedging explained", "gamma exposure GEX meaning", "short gamma vs long gamma", "gamma flip explained", "option pinning explained", "GameStop gamma squeeze mechanism", "max pain theory explained"]
seo_audited: "2026-10-15"
---

## When Call Buying Seems to Push a Stock Up on Its Own

[What Are Option Greeks?](/en/basics/option-greeks-delta-gamma-theta-vega/) covered what delta and gamma measure individually. This lesson covers what happens when those two Greeks collide in a real market. When call-option buying floods into a particular stock, the stock itself can spike sharply in a short window even though ordinary buy orders for the shares haven't picked up much. Stranger still, the rally sometimes accelerates the higher the price climbs. This is called a **gamma squeeze**. It's a different animal from a [short squeeze](/en/basics/short-selling-explained/), where short sellers buy back borrowed shares to close their positions. The buyer driving a gamma squeeze isn't a short seller at all — it's typically the market maker on the *other* side of those option trades. This lesson explains why the party that sold the calls ends up having to buy the stock, and how that buying can turn into a self-reinforcing loop.

## What a Market Maker Does After Selling a Call: Delta Hedging

[What Is a Market Maker?](/en/basics/market-microstructure-basics/) covered how someone has to stand on the other side of every order for a continuous order book to function. The options market works the same way. When an investor buys a call option, the party selling it is usually not another retail trader but a market maker. The moment that market maker sells the call, it takes on directional risk that works against it if the stock rises — the buyer's gain is, almost exactly, the market maker's loss.

A market maker's business isn't making directional bets; it's collecting small, repeatable profits from the bid-ask spread. So immediately after selling a call, it buys shares of the underlying stock equal to that option's delta, offsetting the directional exposure. This is called **delta hedging**. Say a market maker sells 10,000 call contracts (100 shares per contract) with a delta of 0.4. For every $1 the stock rises, the loss on those calls needs offsetting, so the market maker immediately buys 400,000 shares. With that hedge in place, gains and losses on the option leg and the stock leg move in roughly equal and opposite amounts regardless of which way the stock goes, leaving the combined position largely indifferent to price direction — a state called **delta-neutral**.

## Why Gamma Makes the Problem Grow: The Hedge Itself Keeps Changing

If the story stopped there, it would be simple. But as [the Greeks lesson](/en/basics/option-greeks-delta-gamma-theta-vega/) noted, delta isn't fixed — it moves with the stock price, and gamma measures how fast it moves. When the stock rises, a call's delta climbs too, which means the market maker needs to buy *more* shares just to stay delta-neutral. Continuing the example above: if the stock rises further and that call's delta climbs from 0.4 to 0.5, the hedge requirement grows from 400,000 to 500,000 shares. The higher the stock climbs, the more shares the market maker is forced to buy.

This is where the feedback loop forms. The market maker's additional buying itself pushes the price up further, which raises delta again, which triggers yet more buying. When this loop repeats within a short window, the stock can accelerate upward — and that's a gamma squeeze. The critical detail is that this buying isn't demand from investors who believe the company's fundamentals improved; it's mechanical hedge buying aimed purely at restoring a neutral options position. The hand pushing the price up doesn't belong to someone betting on the business — it belongs to a market maker trying to eliminate risk.

## Short Gamma vs. Long Gamma: Dampening Moves vs. Amplifying Them

This feedback doesn't always push prices higher. Its direction depends on whether market makers, in aggregate, are currently **short gamma** or **long gamma**. A market maker holding a large net short position in calls it sold is short gamma — as described above, it has to buy more as the stock rises and sell to trim the hedge as the stock falls, which means it ends up chasing and amplifying the move in whichever direction the stock is already heading.

A market maker that instead holds a large net short position in puts, or a long position in calls, can be long gamma — in that case, the hedging works the opposite way: selling as the price rises and buying as it falls. That dampens swings and tends to anchor the price within a narrower range. Short gamma, in short, amplifies volatility; long gamma dampens it. The metric that attempts to estimate which state dominates across the market is called **gamma exposure (GEX)**, and the price level where aggregate dealer gamma is estimated to flip from one state to the other is called the **gamma flip**. It's worth being explicit that these figures are *estimates* — exchanges don't publish market makers' actual positions, so third-party data providers back these numbers out from publicly visible options volume and open interest, not from the dealers' real books.

## A Real Case Where It Snowballed: GameStop, January 2021

The clearest demonstration of how violently a gamma squeeze can spiral is the GameStop episode of January 2021. A wave of short-dated call buying, concentrated through online retail communities, hit the stock. The market makers on the other side of those trades had to buy shares to delta-hedge their new short-call exposure. As the stock rose, hedge buying grew larger, which pushed the price up further, which grew the hedge requirement again — the loop repeating in a short window. What made the episode especially extreme is that the gamma squeeze wasn't acting alone: it collided with a large pre-existing [short squeeze](/en/basics/short-selling-explained/) in the same stock. As option-hedging buying pushed the price up, short sellers facing margin calls and mounting losses were forced to buy back borrowed shares to cover, and that buying pressure stacked on top of the gamma-driven buying. The two mechanisms have entirely different root causes — one is options hedging, the other is short-position liquidation — but running simultaneously in the same name, they amplified each other and pushed the move to an extreme.

## Pinning and Expiration-Day Quirks

Gamma-driven feedback doesn't only show up as a runaway rally. When expiration is near and a particular strike price has drawn heavy volume and open interest, market-maker hedging can instead pull the stock price *toward* that strike and hold it there. If the price rises above the strike, hedge selling pulls it back down; if it falls below, hedge buying pulls it back up — pressure working from both sides. This is called **pinning**. Some market participants explain it through the **max pain theory** — the idea that the stock tends to settle near the strike price where option buyers, in aggregate, lose the most money. It's worth flagging that max pain theory rests on fairly thin academic support, and many treat it as closer to a widely repeated rule of thumb than an established causal mechanism. Pinning itself isn't a universal rule that fires every expiration either — it's a tendency observed more often when open interest is heavily concentrated at a specific strike.

## A Worked Example: The Feedback Loop in Motion

Here's a simplified, hypothetical walk-through of a short-gamma market maker that sold a large block of calls.

| Stage | Stock price | Average call delta | Hedge shares required (assuming calls covering 10 million shares) |
|---|---|---|---|
| Start | $100 | 0.30 | 3.0 million shares |
| After first rally | $105 | 0.45 | 4.5 million shares (+1.5 million bought) |
| After second rally | $112 | 0.65 | 6.5 million shares (+2.0 million bought) |
| After third rally | $120 | 0.80 | 8.0 million shares (+1.5 million bought) |

(These figures are simplified for illustration and are not real market data.) As the stock rises, delta climbs, and the hedge shares required climb right along with it. That additional buying itself helps produce the next leg of the rally, which drives delta higher again — the recurring structure visible in the table. The loop winds down naturally once those calls expire or implied volatility cools enough that fresh call buying dries up, since the market maker no longer has a reason to keep growing its delta.

## What This Actually Means for an Individual Investor

Gamma squeezes and delta hedging aren't concepts meant to generate trading signals. Treating them as entry or exit rules — "buy when GEX looks like this" or "trade near this pinning level" — runs into two fundamental problems. First, because exchanges don't disclose market makers' actual positions, any publicly available GEX or gamma-flip figure is an *estimate* reverse-engineered from visible options volume and open interest — not a direct read of real hedge flows. Second, gamma squeezes are hard to time: the feedback loop unwinds once call buying cools or the options expire, but predicting exactly when that happens in advance is genuinely difficult.

The real value of understanding this mechanism lies elsewhere. When a stock moves far more sharply than usual with no fundamental news behind it, this concept is a reminder that the buying or selling driving that move isn't necessarily coming from investors who believe in the company. Mechanical hedge flows generated as options positions build and unwind can move a stock's price sharply in the short term on their own. Knowing that gives you a reason to pause before concluding that a sudden, violent price move must mean good news is coming.

## Takeaway

- Delta hedging is how a market maker offsets the directional risk created by the options it buys or sells, using trades in the underlying stock.
- Gamma measures how fast that delta changes as the stock price moves. A short-gamma market maker has to buy more stock to stay hedged the higher the price climbs.
- That additional buying pushes the price higher again, which grows delta further — a feedback loop that defines a gamma squeeze, with a root cause entirely different from a short squeeze's forced short-covering.
- In a long-gamma state, hedging works in the opposite direction from price moves, dampening volatility and sometimes producing pinning near a heavily traded strike.
- GEX, the gamma flip, and max pain are estimates and rules of thumb reverse-engineered from public data — useful for understanding why a sharp move happened, not signals to trade on.

## FAQ

### How is a gamma squeeze different from a short squeeze?
A gamma squeeze comes from market makers buying stock to delta-hedge calls they sold. A short squeeze comes from short sellers buying stock to close out borrowed-share positions. The buyers and their motivations differ, but when both occur in the same stock at the same time, they can reinforce each other.

### Can I trade based on published GEX numbers?
GEX is an estimate of market makers' actual positions — which exchanges don't publish — reverse-engineered from public options data. The number can shift depending on the estimation method used, and it isn't a prediction of a specific price or direction; it's better treated as a rough gauge of where volatility might get amplified or dampened.

### Does pinning happen every expiration?
No. It tends to show up more often when volume and open interest are heavily concentrated at a particular strike price, not as a universal rule that applies to every expiration date.

### When does a gamma squeeze end?
It tends to fade once new call buying cools off or the options expire, since the market maker no longer has a reason to keep growing its hedge. Predicting exactly when that turning point will arrive, however, is difficult to do in advance.

> ⚠️ This article is for informational purposes only and is not investment advice. Investment decisions and their outcomes are the sole responsibility of the investor.
