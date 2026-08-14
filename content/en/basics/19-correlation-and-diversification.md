---
slug: correlation-and-diversification
title: "Correlation and Diversification: Why Owning More Stocks Isn't the Same as Being Diversified"
description: "What a correlation coefficient between -1 and +1 actually means, why adding more stocks alone doesn't cut risk, and how the stock-bond correlation can flip depending on the rate environment."
order: 19
updated: 2026-08-14
keywords: ["what is correlation coefficient investing", "diversification explained", "portfolio correlation", "stock bond correlation", "how does diversification reduce risk", "correlation and diversification", "asset allocation correlation", "true diversification"]
---

## "I Own 10 Stocks — So Why Did My Whole Account Drop Together?"

[Risk Management Basics](/en/basics/risk-management-basics/) covered spreading capital across stocks, sectors, and time as the core of diversification. But something odd shows up in practice all the time: an investor holds 10 different stocks, and on a rough day the whole account drops as one, almost as if it were a single position. Ten tickers, zero diversification benefit — why? The answer has nothing to do with the number of positions and everything to do with how similarly those positions move relative to each other. That "how similarly" has a name — the correlation coefficient — and it, not the position count, is what actually determines how much diversification you're getting.

## The Correlation Coefficient: One Number Between -1 and +1

Correlation measures how closely two assets' prices move together, expressed as a value between -1 and +1.

- **Close to +1**: The two assets move in nearly lockstep. When A rises, B almost always rises too; when A falls, B almost always falls too.
- **Close to 0**: There's no meaningful relationship between the two. Knowing what A did tells you almost nothing about what B did.
- **Close to -1**: The two assets move in nearly opposite directions. When A rises, B tends to fall.

Two large-cap semiconductor stocks are a good example of the high end — they respond to the same demand cycle and the same supply-chain headlines, so their correlation typically lands somewhere around 0.7 to 0.9. A defensive consumer-staples company and a semiconductor maker, by contrast, tend to show a much lower correlation, since their earnings respond to different drivers. You don't need to compute this yourself — brokerage platforms and financial data sites calculate it from historical daily returns — but knowing what the number means is what lets you actually use it.

One caveat worth flagging: correlation tells you *how much* two assets have moved together, not *why*. It's a statistical summary of past price data, not proof of any underlying causal link. Two completely unrelated stocks can show a temporarily high correlation just by coincidence over a given stretch. So rather than reading the number in isolation, it helps to ask why two assets move similarly (or differently) — are they in the same sector, do they respond to the same macro variable — before leaning on that number.

## Why Low Correlation Is What Actually Delivers Diversification

Here's the mechanism. Mix two assets with a correlation of +1 in equal parts, and the combined portfolio's volatility is simply the average of the two individual volatilities — no reduction at all. Add as many tickers as you want; if they all move together, risk doesn't budge. Mix two assets with low or negative correlation, on the other hand, and on days when one falls the other tends to hold up or even rise, so the combined portfolio swings less than either asset would on its own. You keep both assets' expected returns intact while cutting the volatility you have to sit through to earn them — which is why mixing low-correlation assets is often described as one of the only genuinely "free lunches" in investing.

A quick numeric example makes this concrete. Say assets A and B each carry 20% annualized volatility.

| Correlation between A and B | Volatility of a 50/50 blend |
|---|---|
| +1.0 (perfectly aligned) | 20% (no reduction) |
| +0.5 | ~17.3% |
| 0 (unrelated) | ~14.1% |
| -0.5 | ~10% |
| -1.0 (perfectly opposite) | 0% (theoretical) |

Neither asset's expected return changed at all — only the correlation number moved, and that alone is what drags the blended portfolio's volatility down. A real asset pair almost never holds a clean -1 correlation for long, but the direction this table shows — lower correlation buys you the same expected return for less volatility — is the core idea diversification theory is built on.

## How Many Positions Is "Enough"? The Limits of Adding More Names

Does simply owning more names help, regardless of how correlated they are? To a point, yes. Even assets that aren't fully unrelated still let idiosyncratic, company-specific risk (a lawsuit, a bad earnings print, a factory fire) cancel out somewhat as you add more of them, which trims overall portfolio volatility. But that effect has a clear ceiling. A well-known late-1960s study by Evans and Archer found that owning just 10 to 15 randomly chosen stocks eliminated most single-stock risk; later studies using different methodologies and time periods have pushed that estimate as high as 20, 40, or more. The exact number is debated, but the conclusion researchers converge on is consistent: the risk you can eliminate purely by adding more positions (unsystematic risk) has a limit, and beyond that limit, more tickers barely move the needle — while the lower the correlation among what you already hold, the fewer positions it takes to reach that same diversification benefit. In short, *how many* positions you hold matters far less than *how differently* they move from each other.

## The Classic Pairing: Stocks and Bonds

The asset pair this principle has been applied to most is stocks and bonds. When investors expect the economy to weaken, they've historically tended to sell stocks and rotate into relatively safe government bonds — pushing bond prices up (yields down) as stock prices fall. That recurring pattern is why the traditional "60% stocks, 40% bonds" allocation became so widely used: it worked because the two asset classes' correlation was usually low or negative.

That relationship isn't fixed, though. In a stretch like 2022, when central banks raised policy rates rapidly to fight inflation, the usual pattern broke down. Higher rates pushed stock valuations down through the discount-rate mechanism covered in [how interest rates affect stock valuations](/en/basics/interest-rates-and-stock-valuations/) — and at the same time, existing bonds became less attractive next to newly issued bonds paying higher yields, so bond prices fell too. The correlation between U.S. Treasuries and stocks (the S&P 500) climbed from negative territory during the zero-rate era into positive territory that year, and with both asset classes posting double-digit losses simultaneously, commentators openly described it as "the 60/40 portfolio breaking down." Correlation, in other words, isn't a fixed property of an asset class — it's a value that shifts with the macro regime dominating the market at the time, especially the direction of rates and inflation.

## Why Correlations Converge Toward 1 in a Crisis

There's another trap worth building into how you think about diversification. Assets that normally show low correlation to each other tend to see that correlation spike toward 1 all at once during a genuine market panic. Stocks, commodities, emerging-market currencies — investors dumping different assets simultaneously to raise cash pulls all of them down together. During the 2008 global financial crisis and the initial COVID-19 crash in 2020, domestic stocks, international stocks, and even some assets normally classified as safe havens fell in tandem repeatedly. In moments like that, a portfolio that looked genuinely diversified on paper can end up with nearly every holding falling at once. The lesson isn't that mixing low-correlation assets is a flawed strategy — it's that "normal-times correlation" and "crisis correlation" are two different numbers, and risk management needs to account for both.

## Adding More Names Isn't the Same as Real Diversification

Put all of this together and the opening question answers itself. Ten large-cap semiconductor stocks is ten tickers, but because they're all highly correlated with each other, it's functionally closer to one concentrated bet on the semiconductor industry cycle than to a diversified portfolio. Splitting exposure across sectors (semiconductors, financials, healthcare), across asset classes (stocks, bonds, commodities), and across geography (domestic, international) mixes assets with genuinely different supply-and-demand drivers and different macro sensitivities — so the same number of holdings buys you a much bigger real reduction in risk.

Geographic diversification follows the same logic. A domestic market is often concentrated in a handful of industries and sensitive to the local currency, while foreign markets respond to their own industry mix and their own rate and currency environment. The two aren't fully unrelated — when U.S. markets sell off hard, other markets often follow — but the correlation is still typically lower than holding only domestic names, which makes geography its own diversification axis. It's also part of why ETFs are held up as a go-to diversification tool: as covered in [what is an ETF](/en/basics/etf-basics/), a single purchase can give you exposure to hundreds of stocks with wildly different correlations to each other, all in one trade.

## Takeaway

- The correlation coefficient measures how similarly two assets move, on a scale from -1 (perfectly opposite) to +1 (perfectly aligned).
- Grouping only highly correlated assets doesn't meaningfully reduce risk no matter how many you add; risk actually falls once you mix in assets with low or negative correlation.
- Even a pairing with a long history of low correlation, like stocks and bonds, can see that relationship flip when the rate or inflation regime changes.
- Correlations that look low in calm markets tend to converge toward 1 during a genuine crisis, so "low correlation" should never be treated as a permanently fixed number.

## FAQ

### Where can I actually check a correlation coefficient?
Most brokerage platforms have a stock-comparison tool, and financial data sites like Yahoo Finance or portfolio-analytics tools will calculate correlation from historical daily or monthly returns for you. Keep in mind the number will shift depending on what time window you use.

### Is it enough to just hold two assets with low correlation?
No — two assets aren't enough on their own. Even a genuinely low-correlation pair can both be vulnerable to the same specific shock, and two positions can't represent an entire asset class. Splitting exposure across sector, asset class, and geography is more robust than leaning on a single pair's correlation number.

### Does low correlation automatically make something a good investment?
No. Correlation only measures whether an asset helps smooth out your overall portfolio's swings — it says nothing about that asset's expected return or growth prospects on its own. Low correlation alone isn't a reason to hold something with weak fundamentals.

### Does a correlation coefficient stay the same once it's calculated?
No. Correlation shifts depending on the time period used to calculate it, and it changes with the market regime — the direction of rates, inflation, and whether markets are calm or in crisis. Treat a historically calculated correlation as a snapshot to revisit periodically, not a fixed constant you can rely on indefinitely.

> ⚠️ This article is for informational purposes only and is not investment advice. You are solely responsible for your own investment decisions.
