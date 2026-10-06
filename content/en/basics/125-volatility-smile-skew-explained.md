---
slug: volatility-smile-skew-explained
title: "Volatility Smile and Skew: Why Options on the Same Stock Get Priced With Different Volatility"
description: "Why implied volatility differs by strike for options on the same stock and expiration — the mechanics behind volatility smile and skew, and what they reveal about market fear."
order: 125
updated: 2026-10-06
keywords: ["what is volatility smile", "volatility skew explained", "put skew meaning", "why does implied volatility differ by strike", "volatility smile vs skew", "out of the money put volatility", "options volatility surface"]
seo_audited: 2026-10-06
---

## Black-Scholes Assumes One Volatility. Markets Don't Deliver One.

[What Is the Black-Scholes Model?](/en/basics/black-scholes-option-pricing-model/) noted that of the five inputs needed to price an option, volatility is the only one not directly observable in the market. The model also applies that single volatility number uniformly across every strike for a given stock and expiration — whether the strike sits at 50,000 won or 60,000 won, the assumption is that the stock's future swings look the same either way. That's a reasonable starting point: there's only one stock price, so there's no obvious reason the market's expectation of how much it will move should depend on which strike you happen to be pricing.

Yet when you back out [implied volatility](/en/basics/vix-implied-volatility-explained/) from actual traded option prices, that assumption breaks down visibly. At-the-money options and far out-of-the-money options on the same underlying and expiration routinely imply different volatilities, and plotting those values against strike produces a curve, not a flat line. That pattern is what's called the **volatility smile** and the **volatility skew** — both terms describe the same underlying fact (implied volatility varying by strike for an otherwise identical option), distinguished mainly by the shape the curve traces.

## Why Out-of-the-Money Puts Get Priced Rich: The Mechanics of Skew

The shape most commonly seen in equity and index options markets is skew: implied volatility rises steeply for puts struck well below the current price and declines more gently for calls struck well above it. Plotted out, the left side (low strikes) climbs sharply while the right side (high strikes) drifts down gently — closer to a smirk than a smile, which is exactly the informal name traders often use for it.

The most direct driver is supply and demand. [Options as Insurance](/en/basics/options-as-insurance/) framed a put as protection against a decline, and that kind of protection is in near-constant structural demand — pension funds and large asset managers routinely buy out-of-the-money puts to hedge portfolio-wide **tail risk**, crash or no crash in sight. That steady demand keeps put prices, and the implied volatility backed out of them, elevated. Demand for deep out-of-the-money calls exists too (often described as "lottery ticket" buying), but it isn't nearly as structural or persistent, so call-side implied volatility tends to sit lower by comparison.

A second, frequently cited explanation is the **leverage effect**: when a stock's price falls, its debt-to-equity ratio mechanically rises, and higher leverage tends to make the stock itself more volatile going forward. In other words, volatility genuinely tends to pick up as price falls, and the options market prices that relationship in ahead of time by assigning higher implied volatility to lower strikes. The event most often credited with cementing this pattern as a permanent market feature is the October 1987 crash, commonly known as Black Monday, when the S&P 500 fell more than 20% in a single session. After that shock, markets stopped treating a crash of that scale as something that simply couldn't happen, and priced that possibility in going forward — the persistent put skew seen in index options ever since is widely traced back to that repricing.

## Smile or Skew? Why the Shape Differs by Asset Class

Not every options market shows the same lopsided skew. Equity index and single-stock options show the downside-tilted pattern described above, but currency (FX) options more often show a shape closer to a true smile, with both tails elevated roughly symmetrically. That difference comes down to the nature of the underlying risk. A currency spiking up and a currency collapsing can both be genuinely dangerous — to whoever holds it, or to whoever has borrowed in it — so hedging demand tends to be fairly balanced across both directions. Stocks don't share that symmetry: a sharp drop generates far more fear and hedging demand than an equivalent-sized rally, which is exactly what tilts the equity skew in one direction. Either way, the shape itself is really a picture of which direction of tail risk market participants are currently willing to pay more to insure against.

## Skew Also Has a Term Structure

Skew isn't one fixed picture — it changes shape across expirations too. Shorter-dated options tend to show steeper skew, and longer-dated options flatter skew. A worry about an imminent, specific event — earnings, a central bank meeting, a geopolitical headline — gets priced immediately into near-term puts, while a one-year option has to average over many alternating calm and stressful stretches in between, which dilutes how extreme the near-term shape looks. That's why practitioners don't treat skew as a single number but as a full **volatility surface** across strike and time to expiration — the same steep put skew means something different depending on whether it shows up in a one-week option or a one-year option, since it points to a different moment the market is bracing for.

## A Worked Example

Take a simplified, hypothetical illustration of the kind of skew typically seen in index options. Assume the index sits at 350 points, with one-month options backed out across strikes:

| Strike (vs. index) | Option type | Implied volatility (illustrative) |
|---|---|---|
| 320 (−9%, deep OTM) | Put | ≈ 28% |
| 335 (−4%, OTM) | Put | ≈ 22% |
| 350 (at the money) | Call/put common | ≈ 17% |
| 365 (+4%, OTM) | Call | ≈ 15% |
| 380 (+9%, deep OTM) | Call | ≈ 14% |

(These figures are simplified for illustration, not actual market data.) Implied volatility climbs the farther a strike sits from at-the-money — steeply so on the downside — which is the textbook shape of index put skew. The same index, the same expiration, priced with a different volatility depending purely on how far the market is being asked to imagine price falling: a direct contradiction of the single constant volatility Black-Scholes assumes.

## What Skew Tells Investors That VIX Doesn't

[What Is VIX?](/en/basics/vix-implied-volatility-explained/) covered how VIX compresses option prices across many strikes into a single number measuring how much the market overall expects price to move. Skew answers a different question: **which direction** that expected movement is concentrated in. VIX can sit at a calm, low level while the gap between put-side and call-side implied volatility — the skew — steepens on its own. That combination is often read as the market quietly leaning toward "no major shock looks imminent, but if a decline does come, it could run deep." When markets are actually in a panic-driven selloff, VIX and put skew tend to spike together, so watching both side by side shows both how much volatility has grown and which direction the fear is concentrated in.

In the weeks just before the COVID-19 pandemic escalated in early 2020, VIX itself reportedly stayed close to its normal range even as near-term put skew began steepening well ahead of it. That pattern is consistent with some market participants quietly buying protection against a deep decline before the broader market showed any sign of panic. Once the selloff actually arrived, VIX and put skew spiked together to record levels. The episode illustrates why skew sometimes signals ahead of, or differently from, VIX — reading both together gives a fuller picture of market psychology than either alone.

Skew has real limits worth keeping in mind, the same way VIX does. A steep skew means market participants are paying more for downside insurance — it is not a guarantee that a decline is actually coming. Skew is also shaped by structural flows that have little to do with directional fear, such as institutional hedging programs or option-selling flows from products like covered-call ETFs. For that reason, practitioners generally don't treat skew as a standalone trading signal; it's more commonly used by option sellers and hedge fund risk desks as a gauge of how richly the market is currently pricing a given direction of extreme outcome.

## Takeaway

- Volatility smile and skew describe implied volatility differing by strike for options on the same stock and expiration — one of the clearest real-world departures from the single, constant volatility Black-Scholes assumes.
- Equity index and single-stock options typically show an asymmetric "skew," with out-of-the-money puts priced at noticeably higher implied volatility — driven by structural hedging demand and a repricing of crash risk traced back to the 1987 Black Monday crash.
- Assets with two-sided tail risk, like currencies, more often show a flatter, more symmetric "smile" instead.
- VIX measures the overall size of expected volatility; skew measures which direction (up or down) that expectation is concentrated in — a separate piece of information.
- Skew is a gauge of where market fear is concentrated, not a forecast of future price action or a standalone trading signal.

## FAQ

### Are volatility smile and skew the same thing?
Broadly, both terms describe the same phenomenon — implied volatility varying by strike. When people distinguish the shapes specifically, "smile" usually refers to a U-shape with both tails elevated, and "skew" to an asymmetric, one-sided tilt.

### If put skew spikes sharply, does that mean a decline is coming?
Not necessarily. A steep put skew shows how expensive downside protection has become, not whether that decline will actually happen. The price of insurance rising and the insured event occurring are two separate questions.

### Does an individual investor really need to understand this?
Not for day-to-day decisions if you don't trade options directly. But headlines referencing "put skew steepening" as a market-sentiment signal are common enough that knowing what the number actually measures helps in interpreting that kind of coverage.

> ⚠️ This article is for informational purposes only and is not investment advice. You are solely responsible for your own investment decisions.
