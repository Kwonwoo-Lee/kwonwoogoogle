---
slug: risk-parity-all-weather-portfolio
title: "Risk Parity Explained: Why Ray Dalio's All Weather Portfolio Splits Risk, Not Dollars"
description: "Why a 60/40 stock-bond portfolio still gets over 90% of its risk from stocks, how risk parity uses leverage to equalize risk contribution, and what 2022 exposed about its weak point."
order: 136
updated: 2026-10-12
keywords: ["what is risk parity", "risk parity strategy explained", "all weather portfolio explained", "Ray Dalio all weather portfolio", "risk parity vs 60/40", "risk contribution asset allocation", "Bridgewater all weather portfolio", "risk parity leverage"]
seo_audited: "2026-10-12"
---

## You Split Your Money 60/40 — But Does Your Risk Split That Way Too?

In the lesson on [correlation and diversification](/en/basics/correlation-and-diversification/), we covered how a 60% stock / 40% bond mix became the default template for a balanced portfolio. There's a catch most investors never notice: splitting your dollars 60/40 doesn't mean your portfolio's actual risk (volatility) splits that way. Stocks are simply far more volatile than bonds, so in practice something like 90% or more of a 60/40 portfolio's total swings in value trace back to the stock sleeve alone. The money is diversified; the risk isn't. **Risk parity** is the allocation approach built specifically to confront that gap, and the best-known real-world implementation of it is the **All Weather Portfolio**, created by Ray Dalio's Bridgewater Associates.

## Why Dollar Weight and Risk Weight Diverge

How much each asset contributes to a portfolio's overall volatility depends not just on its dollar weight, but on how volatile that asset is on its own and how it correlates with everything else you're holding. Here's a simplified illustration. Say stocks run about 16% annualized volatility and bonds run about 6%, with a correlation near zero between them. In a portfolio split 60/40 by dollars, the approximate risk contribution of each looks like this:

| Asset | Dollar weight | Volatility | Approx. risk contribution |
|---|---|---|---|
| Stocks | 60% | 16% | ~94% |
| Bonds | 40% | 6% | ~6% |

The dollars are split 60/40, but because stock volatility runs more than double that of bonds, almost all of the portfolio's bumpiness still comes from the stock side alone. An investor who believes this portfolio is "diversified" is, in risk terms, sitting on something close to an all-stock position. The exact numbers shift with the volatility and correlation of the moment, but the underlying pattern — dollar weight and risk contribution are two very different numbers — shows up consistently across market regimes.

## The Risk Parity Fix: Set Risk Contribution First, Back Into the Dollar Weights

Risk parity flips the question around. Instead of starting with "how do I split the dollars," it starts with "what dollar weights make each asset contribute equally (or in some chosen ratio) to total portfolio risk?" A low-volatility asset like bonds needs a much bigger dollar allocation to match the risk contribution of a high-volatility asset like stocks, so the math tends to push bond weights up and stock weights down. Reworking the table above under risk parity, getting stocks and bonds to each contribute roughly 50% of total risk pushes the dollar split toward something like 25% stocks and 75% bonds.

That creates an obvious problem: putting 75% of your capital into bonds and only 25% into stocks drags expected returns down hard. Risk parity funds typically close that gap with **leverage**. Scale the bond allocation up from 75% of capital to, say, 150% (borrowing to buy more bonds than your own capital alone would cover), and you can restore the portfolio's expected return to a target level while keeping the risk contributions balanced. Risk parity, in other words, bundles two moves into one strategy: equalizing risk contribution, and using leverage to buy back the return that move gives up. As covered in [margin trading and leverage](/en/basics/margin-trading-leverage/), leverage amplifies gains and losses together — risk parity is that same amplification effect, deliberately aimed at the "safer" asset to reshape how risk is distributed across the whole portfolio.

Running the numbers makes this concrete. Starting with 100 of your own capital and splitting it unlevered 25 stocks / 75 bonds typically leaves you with a lower expected return than the 60/40 version had. Borrow an extra 50 and put it into bonds too (pushing the bond allocation from 75% to 125% of your own capital), and the portfolio now deploys 150 in total — 100 of your own money plus 50 borrowed — even though you only put up 100. That borrowed money carries interest, and if the bond price move ends up worse than the interest cost, the loss comes back scaled against your original 100, not against the full 150. That's the part of risk parity that matters most to understand: leverage looks like "buying more of the safe asset," but if that asset moves against you, it pulls the full size of the borrowed position's risk back onto the portfolio.

## The All Weather Portfolio: Built for Every Season of the Business Cycle

Bridgewater's All Weather Portfolio extends the risk-parity idea across the entire business cycle. Dalio's framework splits the macro environment along two axes — growth (rising or falling) and inflation (rising or falling) — producing four "seasons":

- **Rising growth, rising inflation**: commodities and emerging-market assets tend to do well
- **Rising growth, falling inflation**: stocks tend to do well
- **Falling growth, rising inflation (stagflation)**: inflation-linked bonds and gold tend to do well
- **Falling growth, falling inflation (deflation)**: long-term government bonds tend to do well

The All Weather Portfolio doesn't try to forecast which of these four seasons is coming next. Instead, it holds assets that tend to do well in each one — stocks, short- and long-term government bonds, gold and other commodities — and sizes those holdings using the same risk-parity logic, so each piece contributes a comparable share of total portfolio risk. The name reflects the goal: whichever economic season actually shows up, some piece of the portfolio is positioned to hold up. The strategy traces back to Bridgewater's internal capital in 1996 before later opening to outside investors, and it remains one of the oldest and most widely cited risk-parity portfolios in the industry.

## What 2022 Exposed: When Both "Safe Legs" Wobble at Once

Risk parity's logic rests on the assumption that stocks, bonds, and other asset classes tend to do well in different macro environments — in other words, that correlations between them stay low. When that assumption breaks, the leveraged bond position that was supposed to be the "safe" leg can end up amplifying losses instead. 2022 broke that assumption head-on. As covered in [how interest rates affect stock valuations](/en/basics/interest-rates-and-stock-valuations/), central banks raised rates sharply to fight inflation, and stocks and bonds fell together by double digits in the same year. Risk parity strategies, with their leveraged bond exposure, took that joint decline at full force — in some cases harder than unlevered portfolios did. Industry reporting at the time noted that one widely tracked US-listed risk-parity ETF lost more than 20% for the year, while a comparable traditional 60/40 allocation ETF held up noticeably better over the same period. The lesson here cuts both ways: the traditional "stocks and bonds balance each other out" formula and the risk-parity "equalize the risk contributions" formula both depend on correlations behaving the way they normally do — and both can get hit hard in the moment that assumption fails.

## 60/40 vs. Risk Parity, Side by Side

| | Traditional 60/40 | Risk Parity |
|---|---|---|
| Allocation basis | Dollar weight | Risk (volatility) contribution |
| Bond weight | Relatively small (40%) | Relatively large, often scaled up with leverage |
| Leverage | Typically none | Typically used |
| Risk structure | Effectively close to all-stock risk | Risk spread more evenly across asset classes |
| Performance in strong equity bull markets | Captures most of the upside | Tends to lag, since stock weight is lower |
| Rate-shock / joint sell-off regime | Takes a hit, but no leverage to amplify it | Leveraged bond exposure can amplify the hit |

## What Investors Should Keep in Mind

It's tempting to treat risk parity as a silver bullet that works even when the old stock-bond relationship breaks down. That's the wrong lesson. Leverage genuinely spreads risk more evenly as long as the usual correlation pattern holds — but the moment that pattern breaks, the same leverage turns into a loss amplifier. A few things worth checking before leaning on this approach:

- **Whether and how much leverage is actually used.** Check a risk-parity fund or ETF's actual leverage ratio in its disclosures rather than assuming from the name alone.
- **How dependent the strategy is on correlation assumptions.** As covered in [the efficient frontier](/en/basics/efficient-frontier-modern-portfolio-theory/), correlations across assets tend to converge toward 1 during a crisis — exactly the moment risk parity is supposed to help the most.
- **The opportunity cost in a sustained equity bull market.** A structure with meaningful bond and commodity weight will tend to lag a pure-equity portfolio when stocks are the dominant winner for an extended stretch.
- **The difficulty of DIY implementation.** Calculating risk contributions and managing a leverage ratio isn't something most individual investors replicate by hand, which is why most exposure to this approach comes through a fund or ETF built around it.

## Key Takeaways

- Splitting a portfolio 60/40 by dollars still leaves most of its actual volatility concentrated in the stock sleeve, because stocks are far more volatile than bonds.
- Risk parity sets each asset's risk contribution first, then uses leverage to restore the expected return that a bond-heavy, risk-balanced allocation would otherwise give up.
- Ray Dalio's All Weather Portfolio extends this idea across four macro "seasons" (growth and inflation, each rising or falling), aiming to hold something that performs in any environment rather than forecasting which one is coming.
- In a regime like 2022, where stocks and bonds fall together, the leveraged bond exposure that usually balances risk parity can instead amplify losses — risk parity is not a universal hedge against every kind of downturn.
- Leverage size, dependence on correlation assumptions, and opportunity cost during equity bull markets are the key limitations to weigh before treating this approach as a default solution.

## FAQ

### Is risk parity always safer than a traditional 60/40?
No. When asset-class correlations behave as they usually do, risk parity spreads risk more evenly and can come out ahead. But in a regime like 2022, when stocks and bonds fall together, the leveraged bond position can amplify losses beyond what a traditional 60/40 experiences. It's more accurate to say risk parity distributes risk differently, not that it's categorically safer.

### Can an individual investor replicate the All Weather Portfolio?
You can approximate the asset mix with ETFs covering stocks, government bonds, inflation-linked bonds, and gold, but replicating the actual strategy's risk-contribution calculations and leverage adjustments by hand is difficult. A simplified, unlevered version built from asset-class weights alone will have a different risk and return profile than the original strategy.

### Why use leverage on bonds at all — doesn't that make things riskier?
Because bonds are so much less volatile than stocks, reaching a meaningful risk contribution from bonds without leverage would mean holding so much bond weight that overall expected returns drop too far. Leverage is the mechanism that lets a low-volatility asset "punch above its weight" so the portfolio can balance risk contributions and target a reasonable expected return at the same time. That mechanism isn't free, though — it amplifies losses just as readily if the correlation assumptions behind it break down.

> ⚠️ This article is for informational and educational purposes only and does not constitute a recommendation of any specific strategy or product. Volatility and loss figures cited here are simplified illustrative examples or summaries of ranges reported in industry commentary; verify actual figures against each fund's own disclosures.
