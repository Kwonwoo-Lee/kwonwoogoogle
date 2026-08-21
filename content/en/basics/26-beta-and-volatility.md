---
slug: beta-and-volatility
title: "What Is Beta? Measuring Risk Relative to the Market"
description: "Why beta, not standard deviation, is how analysts compare risk across stocks — what beta above 1, below 1, and negative actually mean, and the risk beta never captures."
order: 26
updated: 2026-08-18
keywords: ["what is beta in stocks", "stock beta meaning", "high beta vs low beta stocks", "systematic vs unsystematic risk", "how is beta calculated", "beta coefficient explained", "limitations of beta", "beta vs standard deviation"]
seo_audited: 2026-08-21
---

## What Does "This Stock Is Volatile" Actually Mean?

Financial reports and news headlines constantly describe stocks as "high-beta" or "volatile." If you've read [Risk Management Basics](/en/basics/risk-management-basics/), you already have position sizing and stop-loss discipline down — but there's a layer beneath that: how do you actually compare how risky two stocks are? Volatility itself isn't a single number. A stock swinging 5% in a day isn't automatically "risky," and a stock barely moving 1% a day isn't automatically "safe." A far more useful question, most of the time, is: on a day the overall market swings hard, does this particular stock swing more than the market, or less? This lesson covers **beta (β)**, the metric built to answer exactly that question — what it measures, and just as importantly, what it doesn't. The goal isn't a buy or sell signal on any specific stock; it's being able to read a beta number in a report and know what it's actually telling you.

## What Beta Measures: Sensitivity to Market Moves

**Beta** measures how sensitively a stock's returns move relative to the returns of the overall market — typically a broad index like the S&P 500 or, in Korea, the KOSPI or KOSPI 200. It's calculated as the **covariance between the stock's returns and the market's returns, divided by the variance of the market's returns**.

```
Beta = Covariance(stock returns, market returns) ÷ Variance(market returns)
```

The formula looks technical, but the idea behind it is simple: run a regression of the stock's historical returns against the index's historical returns, and beta is the slope of that line — roughly, "on average, how many percent did this stock move for every 1% move in the market?" You'll almost never calculate this by hand — every brokerage platform and financial data site pre-computes it for you. What matters isn't the arithmetic, it's knowing the question beta is answering: "When the market shakes, does this stock shake more, or less?"

## Reading a Beta Value: Everything Is Relative to 1

Beta is interpreted against a baseline of 1.

- **Beta = 1**: The stock tends to move roughly in line with the market. A 10% market rally tends to come with roughly a 10% move in the stock, and a 10% market drop tends to come with a similar drop.
- **Beta > 1**: The stock tends to move more than the market. A stock with a beta of 1.5 tends to rise about 15% when the market rises 10% — and tends to fall about 15% when the market falls 10%. Semiconductor, biotech, and growth stocks, where a large share of the price reflects expectations about distant future earnings, tend to cluster here.
- **Beta < 1**: The stock tends to move less than the market. A stock with a beta of 0.6 tends to move only about 6% for every 10% market move. Utilities, telecoms, and consumer staples — businesses whose earnings hold up regardless of the economic cycle — tend to cluster here.
- **Negative beta**: The stock tends to move in the opposite direction of the market. Genuinely negative-beta assets are rare, but gold in certain periods, or some inverse products, can fall into this category.

One thing worth flagging clearly: a high beta doesn't mean "goes up more." It means "moves more in both directions." High-beta stocks tend to outperform in bull markets, but they carry the same amplification on the way down in bear markets. Beta measures sensitivity, not direction.

## What Beta Misses: Systematic vs. Unsystematic Risk

Using beta correctly requires knowing exactly what category of risk it's measuring. Finance generally splits risk into two buckets.

**Systematic risk** is risk tied to the entire market — interest rates, recessions, wars, inflation — the kind no amount of careful stock-picking can avoid, because it hits everything at once. This is the piece beta actually measures.

**Unsystematic risk** (also called idiosyncratic risk) is specific to one company: an embezzlement scandal, a failed drug trial, a product recall, an accounting fraud discovery. As covered in [Correlation and Diversification](/en/basics/correlation-and-diversification/), this kind of risk can be substantially reduced by holding a diversified basket of stocks with low correlation to each other.

Beta only captures systematic risk. That means a stock with a low beta of 0.5 can still crash on its own bad news — a fraud disclosure, a lawsuit, an earnings collapse — completely independent of what beta says. A low beta means "moves less when the market shakes," not "nothing is wrong with this company."

The relationship between the two comes together in the idea of total risk. A stock's overall volatility is the sum of its systematic risk and its unsystematic risk. Hold one stock, and you're carrying both in full. Spread your money across several stocks with low correlation to each other, and the unsystematic piece largely cancels out, leaving a portfolio whose remaining risk is mostly the systematic piece — the part beta describes. No amount of diversification eliminates systematic risk itself, which is exactly why stocks that looked uncorrelated in calm markets often drop together when the broader market sells off hard.

## A Concrete Example

Say the KOSPI rose 10% over the past year, and you're comparing three stocks.

| | Stock A (telecom, beta 0.5) | Stock B (index-tracking, beta 1.0) | Stock C (semiconductor growth stock, beta 1.8) |
|---|---|---|---|
| Beta | 0.5 | 1.0 | 1.8 |
| Expected return if market is +10% | roughly +5% | roughly +10% | roughly +18% |
| Expected return if market is -10% | roughly -5% | roughly -10% | roughly -18% |

The word "expected" carries the weight here. Beta is an average historical tendency, not a promise of how a stock will move on any given day. In reality, Stock C could just as easily jump or crash 20% in a single day purely on its own earnings release, entirely independent of what the market did. Beta tells you how connected a stock has been to the market on average — it is not a tool for predicting day-to-day price action.

This becomes more useful at the portfolio level. Weight A, B, and C equally, and the portfolio's beta lands near the average of the three — about 1.1 ((0.5 + 1.0 + 1.8) ÷ 3). Ahead of a period where you expect heavy market turbulence, tilting the portfolio toward the low-beta name pulls that overall beta down; wanting more upside exposure to a rally means tilting toward the high-beta name instead. Either way, adjusting beta only dials your exposure to broad market moves up or down — it's never a substitute for judging the fundamentals of the individual stocks themselves.

## What to Watch Out For

A few limitations of beta are easy to overlook once it becomes a familiar number.

First, **beta isn't fixed — it depends on the time window used to calculate it.** Beta computed on the last year of data often differs from beta computed on the last five years, and it genuinely drifts over time as a company's business mix or debt load changes. Because data providers use different benchmark indices and lookback periods, the same stock can show noticeably different beta values on different platforms.

Second, **when the regression's explanatory power (R²) is low, the beta number itself is less trustworthy.** For some stocks, most of the day-to-day price action is driven by company-specific news rather than the broader market, in which case beta exists as a number but does a poor job of actually explaining that stock's real behavior.

Third, **beta doesn't distinguish upside risk from downside risk.** A beta of 1.5 working in your favor during a rally doesn't mean the risk shrinks during a downturn — it means the exact same multiplier applies in reverse, and the stock falls harder too. If you want an actual cushion against a downturn, beta alone won't provide it; that's where hedging concepts like the ones covered in [Options as Insurance](/en/basics/options-as-insurance/), or genuine diversification, come in.

Fourth, beta is just one of several ways to measure volatility. Standard deviation measures how much a stock's own returns bounce around, full stop, with no reference to the market at all. Beta isolates only the portion of that bounce that moves together with the market. They answer different questions, so treat them as complementary rather than interchangeable. A stock can have high standard deviation but low beta — its price swings are driven by company-specific news (a drug trial result, a commodity price swing) that has little to do with the broader market. The reverse is also possible: a stock with fairly modest standard deviation but a beta above 1, because whatever movement it does have tracks the market closely. Reading both together is what actually explains why a stock is volatile.

Fifth, theoretical models like the Capital Asset Pricing Model (CAPM) plug beta into expected-return calculations, but that only works if beta has a stable linear relationship with future returns. A substantial body of empirical research finds that assumption doesn't hold consistently in real markets. Beta is safer treated as one reference point describing a slice of risk, not as a formula that precisely computes a stock's expected return.

## Takeaway

- Beta measures how sensitively a stock's returns move relative to the overall market's returns.
- A beta of 1 means market-level sensitivity; above 1 means the stock moves more than the market; below 1 means it moves less.
- Beta only captures systematic risk — the risk tied to the whole market. It says nothing about company-specific (unsystematic) risk.
- Beta is a historical, average tendency, not a fixed constant — it's an estimate that shifts with the calculation window and data source.
- A low beta doesn't guarantee a "safe" stock, and a high beta doesn't automatically mean a "dangerous" one. Read it as sensitivity that amplifies both gains and losses, not a verdict on quality.

## FAQ

### Does a low beta automatically mean a stock is safe?
No. Beta only measures risk tied to the overall market — it says nothing about company-specific risk like lawsuits, accounting problems, or an earnings shock. A low-beta stock can still crash hard on bad news specific to that company.

### Where can I look up a stock's beta?
Most brokerage apps and financial data sites display it directly on a stock's detail page. Because the benchmark index and lookback period used in the calculation differ by provider, the same stock can show a somewhat different beta number depending on where you check.

### Will a portfolio of high-beta stocks always outperform?
Not necessarily. A portfolio built entirely from high-beta names has a better shot at beating the market during a rally, but it takes proportionally larger losses during a downturn too. Beta is a dial for adjusting risk exposure, not a metric that promises higher returns.

> ⚠️ This article is for informational purposes only and is not investment advice. You are solely responsible for your own investment decisions.
