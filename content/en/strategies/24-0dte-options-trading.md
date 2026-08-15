---
slug: 0dte-options-trading
title: "0DTE Options Trading: Handling Gamma and Theta on Same-Day Expiration"
description: "How 0DTE options compress theta decay and gamma risk into a single trading day, and how long calls, credit spreads, and iron condors trade that compression differently."
order: 24
updated: 2026-08-15
keywords: ["0DTE options", "zero days to expiration", "0DTE trading strategy", "0DTE iron condor", "SPX 0DTE options", "options theta gamma", "0DTE credit spread", "same day expiration options risk"]
---

## Why "Expires Today" Changes Everything About an Option

A standard option carries weeks or months of time value, so its price responds fairly gently to small moves in the underlying. A **0DTE option — zero days to expiration** — is a different animal entirely: it expires at the close of the same trading day it's traded, which means every bit of remaining time value has to burn off within hours. Two contracts with identical strikes and identical underlying can behave in completely different ways depending on how much time is left, and 0DTE sits at the far edge of that spectrum.

Since the CBOE rolled out daily expirations on SPX index options and later extended them to SPY, QQQ, and IWM, 0DTE trading has gone from an institutional niche to a genuinely retail product — volume in same-day SPX options now regularly makes up a large share of total SPX options activity. Lesson 15 on [gamma exposure (GEX)](/en/strategies/gamma-exposure-gex/) looked at how the aggregate options positioning across the whole market pushes and pulls on price. This lesson flips the lens: how does an individual trader actually structure a 0DTE trade, and what does that compressed-time environment do to the risk?

## Theta and Gamma: The Two Forces That Dominate 0DTE

Every option price responds to several Greeks, but two of them come to dominate everything else once expiration is measured in hours rather than weeks.

- **Theta (the rate of time-value decay)**: since whatever time value remains has to vanish before the closing bell, theta accelerates non-linearly as expiration approaches. For a seller, that means premium can be collected fast. For a buyer, it means being directionally right isn't enough — you also have to be right in time.
- **Gamma (the rate of change of delta)**: near-the-money options with almost no time left carry extreme gamma. A tiny move in the underlying can swing an option's delta dramatically, which is why 0DTE option prices can move in a way that looks almost nothing like a linear function of the underlying's move.

A common way traders describe it: theta is the friction that works against you every second you hold the position, while gamma is the engine that can suddenly amplify gains or losses the moment price moves. Both forces operating at their most extreme, compressed into a single session, is what makes 0DTE structurally different from trading a monthly option.

<figure class="diagram">
  <img src="/static/img/charts/en/0dte-options-trading.svg" alt="Diagram showing theta decay and gamma sensitivity both accelerating sharply as time to expiration shrinks toward zero, alongside the payoff structure of a 0DTE iron condor" loading="lazy">
  <figcaption>Left: theta and gamma both accelerate exponentially as expiration nears — 0DTE sits at the very end of that curve. Right: the payoff diagram of a 0DTE iron condor — a narrow profit zone bracketed by defined losses on either side.</figcaption>
</figure>

## Three Ways Traders Structure a 0DTE Position

0DTE trades generally fall into one of three structures, and each carries a distinctly different risk profile.

| Approach | Position | Payoff shape | Character |
|---|---|---|---|
| Directional buy (long call/put) | Buy one call or put | Loss capped at premium paid; gain theoretically uncapped if right on direction | Low win rate, occasional large win — a "lotto" profile |
| Credit spread | Sell a near strike, buy a farther strike for protection | Gain capped at premium received; loss capped at spread width minus premium | Higher win rate, but risk usually exceeds reward per trade |
| Iron condor | Sell a call credit spread and a put credit spread simultaneously | Profits if the underlying stays inside both spreads; loses if it breaks out either side | A bet on staying range-bound, built to collect theta |

A **directional buy** is the easiest to understand: buy a call if you expect the underlying to rise, a put if you expect it to fall. The catch is that even a correct directional call can lose money if you're too late entering or the move doesn't outrun theta decay fast enough. Buying deeply out-of-the-money contracts cheaply in hopes of catching an outsized move — commonly called a "lotto play" — usually expires worthless, but the occasional hit can pay off many multiples of the premium, an asymmetric structure some traders build small allocations around.

A **credit spread** turns theta decay into an ally when you have a directional view. If you expect the market to hold above a level, you might sell a put below the current price and buy a further-out put for protection (a bull put spread) — if the underlying settles above the strike you sold, you keep the full premium collected.

An **iron condor** takes no directional stance at all — it's a bet that today simply won't move much. Selling a call credit spread and a put credit spread at the same time collects premium on both sides if the underlying stays inside the range those two spreads define; a move past either boundary produces a loss on that side.

## A Worked Example: The Iron Condor in Numbers

Say a hypothetical index is trading at 5,000 points, and a trader expects it to stay between 4,950 and 5,050 through the close. They build the following iron condor:

- Call credit spread: sell the 5,050 call, buy the 5,060 call (10-point width)
- Put credit spread: sell the 4,950 put, buy the 4,940 put (10-point width)
- Total premium collected across both spreads: 2.5 points ($250 per contract, at a 100 multiplier)

If the index settles anywhere between 4,950 and 5,050 at the close, both spreads expire worthless and the trader keeps the full $250 collected. If the index instead rallies past 5,060, the call spread produces its maximum loss: the spread width (10 points) minus the premium received (2.5 points), or 7.5 points — $750.

That example prices out to roughly a 3:1 risk-to-reward ratio against the trader — $750 at risk to make $250. A rule of thumb that circulates widely among 0DTE traders puts it starkly: a typical 0DTE iron condor risks something on the order of $9 to make $1, which implies needing a win rate near 90% just to break even. That figure is a commonly repeated approximation, not a validated industry constant — the actual ratio moves with strike width, premium collected, and the day's realized volatility.

> ⚠️ A win rate near 90% does not automatically mean the strategy is safe. Because a single large loss can offset many small wins at once, win rate on its own tells you almost nothing about expected value — you have to look at both together.

## Why Trade Iron Condors at All: The Logic of Selling Theta

The appeal of the iron condor comes down to one structural fact: option sellers benefit as time passes, and the iron condor pushes that edge to its extreme by operating entirely within 0DTE's compressed decay window. Viewed through the lens of Lesson 6 on [risk/reward and position sizing](/en/strategies/risk-reward-money-management/), this is a strategy that sits firmly in the "high win rate, poor risk/reward" quadrant. A high win rate feels psychologically comfortable, but a strategy where losses are structurally larger than gains can still lose money over time if even a small fraction of trades go the wrong way — the math has to be run on expected value, not on how often the trade "works."

## Entry Timing and Strike Selection

Approaches commonly discussed among 0DTE traders include the following — treat these as widely repeated conventions, not fixed rules, and adjust for actual market conditions:

- **Wait for the opening volatility to settle.** The first 30 minutes to an hour of the session often carries gap risk and elevated volatility, so many traders wait for that window to pass before entering.
- **Anchor strike selection to the expected move.** The price of an at-the-money option implies a market-estimated range for where the underlying is likely to land by the close; traders commonly place their short strikes outside that implied range with some buffer.
- **Adjust spread width to the volatility regime.** Wider spreads when implied volatility (as read from something like the VIX) is elevated, narrower spreads when it's low, is a frequently mentioned adjustment — again, a convention that varies trader to trader rather than a fixed formula.

## Limitations and Pitfalls

- **Gamma risk is extreme in the final hours.** In the last hour or even the last few minutes before the close, a tiny move in the underlying can swing option values dramatically — sometimes faster than a trader can react to close or adjust a position.
- **Liquidity isn't guaranteed everywhere.** Even heavily traded index options like SPX and SPY can see wider bid-ask spreads at certain strikes or times of day, and the resulting slippage eats directly into realized returns.
- **A high win rate can be misleading.** Credit spreads and iron condors post small wins most of the time, but an infrequent large loss can wipe out a long streak of gains or worse. Judging the strategy by win rate alone is a common and costly mistake.
- **Regulatory and broker policy can shift.** Rising retail participation in 0DTE has drawn regulatory scrutiny, and margin requirements or position limits can tighten depending on the broker and market. Always confirm current rules with your broker before trading.
- **Tax and account treatment vary.** Depending on where you're based and what instrument you're trading (index options vs. ETF options, for example), tax treatment can differ meaningfully from regular equity trading — worth confirming before you start.

## FAQ

### Is 0DTE trading suitable for beginners?
Starting with 0DTE before understanding basic options mechanics — calls, puts, delta, gamma, theta, in-the-money vs. out-of-the-money — is not recommended. 0DTE compresses the risks of ordinary options trading into a single session, so it's safer to first build intuition on the Greeks and payoff structures using contracts with weeks of time left before narrowing that window down.

### How does 0DTE relate to gamma squeezes and gamma exposure (GEX)?
When open interest concentrates in same-day contracts, the delta-hedging flows dealers have to run on expiration day get larger and more sensitive to price, feeding directly into the gamma exposure and pin-risk dynamics covered in Lesson 15. In other words, individual traders' 0DTE activity is itself one of the inputs into the market-wide gamma structure — the two lessons describe the same phenomenon from opposite ends, one from the trader's entry decision, the other from the market's aggregate positioning.

### Why not just buy calls or puts instead of running an iron condor?
Neither is inherently better — they're built for different views. A directional buy has a low win rate but caps the loss at the premium paid, with theoretically open upside if the direction is right. An iron condor has a high win rate but a loss that's usually larger than the gain on any single trade. The right choice depends on whether you actually expect a big move or a quiet range, and how much of a single-trade loss you can tolerate.

## Summary

- 0DTE options expire the same day they're traded, so all remaining time value has to decay within hours — pushing theta and gamma to their most extreme values.
- The three common structures — directional buys, credit spreads, and iron condors — sit at nearly opposite ends of the win-rate-versus-risk/reward spectrum.
- Iron condors monetize theta decay and typically post a high win rate, but the risk-to-reward ratio usually runs against the trader, so win rate alone says little about whether the strategy is actually profitable over time.
- Entry timing (after opening volatility settles), strike selection (anchored to the expected move), and spread-width adjustments (based on volatility regime) are widely used conventions, not fixed formulas.
- Gamma risk, liquidity gaps, shifting regulation, and tax treatment all need to be weighed, and 0DTE is not the place to learn options mechanics for the first time.
