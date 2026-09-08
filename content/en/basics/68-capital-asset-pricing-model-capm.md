---
slug: capital-asset-pricing-model-capm
title: "What Is CAPM? The Formula Behind Expected Return"
description: "How the Capital Asset Pricing Model turns a risk-free rate, beta, and equity risk premium into an expected return, what the Security Market Line means, and where the model breaks down in practice."
order: 68
updated: 2026-09-08
keywords: ["what is CAPM", "capital asset pricing model explained", "CAPM formula", "how to calculate expected return", "risk-free rate equity risk premium", "security market line explained", "cost of equity calculation", "CAPM limitations"]
seo_audited: 2026-09-08
---

## "What Return Should I Reasonably Expect From This Stock?"

[What Is Beta?](/en/basics/beta-and-volatility/) covered beta as a number describing how sensitively a stock moves relative to the market. But knowing that number alone leaves one question unanswered: given this much risk, what return is it actually reasonable to expect? [ROIC vs. WACC](/en/basics/roic-vs-wacc-value-creation/) and [DCF Intuition](/en/basics/discounted-cash-flow-dcf/) both leaned on the idea of "cost of equity" — the minimum return shareholders require — without explaining how that number is actually derived. Filling in that gap is exactly what the **Capital Asset Pricing Model (CAPM)**, developed in the 1960s by William Sharpe and others building on Harry Markowitz's portfolio theory, was built to do. This lesson covers how CAPM links risk and expected return into a single formula, and the limitations you need to know before leaning on it.

## The CAPM Formula: Three Inputs, One Expected Return

Here's where CAPM lands:

```
Expected Return = Risk-Free Rate + Beta × (Expected Market Return − Risk-Free Rate)
```

The term in parentheses — expected market return minus the risk-free rate — is called the **equity risk premium (ERP)**, so the formula is usually written more compactly as:

```
Expected Return = Risk-Free Rate + Beta × Equity Risk Premium
```

The logic behind this is more intuitive than the notation suggests. What an investor expects to earn from any asset splits into two pieces. The first is **compensation for time**: the minimum return you can lock in by taking essentially no risk at all, typically proxied by a long-term government bond yield (the 10-year Treasury in the U.S., the 10-year KTB in Korea). The second is **compensation for risk**: putting money into the stock market as a whole is riskier than holding government bonds, so investors demand extra return above the risk-free rate — the equity risk premium — for taking that on. And as covered in [What Is Beta?](/en/basics/beta-and-volatility/), if an individual stock moves more sharply than the overall market (beta > 1), that risk premium gets scaled up by a larger multiplier; if it moves less (beta < 1), the multiplier shrinks. In short, CAPM takes the common-sense idea that higher risk should demand higher return and turns it into a number you can actually compute — specifying exactly how to measure that risk and exactly how much more return it should command.

## Why Beta, Specifically? The Security Market Line

A natural question follows: there are other ways to measure risk, like standard deviation — so why does CAPM insist on beta? The answer goes back to the systematic-versus-unsystematic risk distinction from the beta lesson. Unsystematic risk — lawsuits, accounting problems, anything specific to one company — can largely be cancelled out by holding a diversified basket of stocks. CAPM assumes the market doesn't pay you extra for carrying a risk you didn't need to carry in the first place: if diversification could have eliminated it for free, there's no reason the market should reward you for holding it anyway. Systematic risk — the piece beta measures, the part that moves together with the whole market — is different. No amount of diversification removes it. CAPM's core assumption is that the market only compensates investors for this undiversifiable risk, and it scales that compensation proportionally to beta.

Plot this relationship with beta on the x-axis and expected return on the y-axis, and you get a straight line called the **Security Market Line (SML)** — starting at the risk-free rate when beta is zero, and passing through the expected market return when beta equals 1. In CAPM theory, every asset should sit exactly on this line. A stock whose actual expected return sits above the line looks underpriced for its risk level; one below the line looks overpriced. That said, this reading assumes the model's theoretical equilibrium actually holds — and, as the limitations section below covers, real markets deviate from it often enough that treating the SML as a literal mispricing detector is risky.

## A Concrete Example

Suppose the 10-year Treasury yield (risk-free rate) is 4%, and the long-run expected return on the S&P 500 is 9%. That puts the equity risk premium at 9% − 4% = 5%. Applying CAPM to three stocks with different betas:

| | Stock A (utility, beta 0.5) | Stock B (index-tracking, beta 1.0) | Stock C (semiconductor growth stock, beta 1.8) |
|---|---|---|---|
| Beta | 0.5 | 1.0 | 1.8 |
| Calculation | 4% + 0.5 × 5% | 4% + 1.0 × 5% | 4% + 1.8 × 5% |
| CAPM Expected Return | 6.5% | 9.0% | 13.0% |

Stock A, with lower systematic risk, carries a lower required return; Stock C, carrying more of that risk, carries a higher one. The key thing to keep in mind is that this number is not a forecast of what you'll actually earn by buying the stock. What CAPM computes is the minimum return market participants require in exchange for bearing this level of systematic risk — the actual stock price can rise far more or far less than this figure regardless.

## Where CAPM Actually Gets Used

CAPM's most common real-world use isn't as a buy/sell signal — it's as the standard method for estimating the **cost of equity** that feeds into [WACC](/en/basics/roic-vs-wacc-value-creation/). The discount rate used to value future cash flows in a [DCF model](/en/basics/discounted-cash-flow-dcf/) is that same WACC, and computing WACC requires not just the cost of debt but also the return shareholders require — which is almost always estimated with CAPM. When an analyst publishes a valuation report, a CAPM calculation is buried somewhere in the discount-rate derivation even when it isn't spelled out explicitly. The same logic — that beta links directly to expected return — also underlies the practice, mentioned in the beta lesson, of tilting a portfolio's overall beta up or down to adjust exposure to market swings.

## Where CAPM Breaks Down

CAPM has been the backbone of finance theory for decades, but an equally large body of empirical research finds its real-world predictive power to be fairly weak. A few of the well-known cracks:

First, CAPM rests on assumptions — perfectly competitive markets, identical information for all investors, unlimited short-selling — that don't hold in the real world to begin with. Second, as covered in the beta lesson, beta itself is an unstable estimate that shifts depending on the calculation window and benchmark index, so the model's core input is shaky from the start. Third, there's a well-documented pattern researchers call the **low-volatility anomaly**: low-beta stocks have repeatedly delivered higher returns than CAPM predicts, while very high-beta stocks have repeatedly delivered lower returns than predicted, across multiple markets and time periods. Findings like this convinced much of academia and practice that beta alone doesn't fully explain the spread in stock returns, leading to multi-factor extensions like the Fama-French model covered in [What Is Factor Investing?](/en/basics/factor-investing-explained/), which adds value, size, and momentum factors on top of beta. CAPM remains the starting point those models build on and still the most widely used baseline in practice — but it's safer to treat the number it produces as the simplest possible starting point for thinking about risk and return, not as a precise answer.

## Takeaway

- CAPM states that Expected Return = Risk-Free Rate + Beta × Equity Risk Premium, tying risk directly to expected return in a single equation.
- It assumes the market pays no extra reward for unsystematic risk, which diversification can eliminate for free, and rewards only systematic risk (beta) in proportion to how much of it you carry.
- In practice, it's used far more often to estimate the cost of equity that feeds into WACC than as a stock-picking signal.
- Its predictive power is limited by unrealistic market assumptions, unstable beta estimates, and empirical anomalies like low-volatility stocks outperforming — which is why multi-factor models like Fama-French were built to extend it.

## FAQ

### What numbers should I actually use for the risk-free rate and equity risk premium?
There's no single correct answer. The risk-free rate is usually a long-term government bond yield, and the equity risk premium is typically estimated from decades of historical excess stock market returns. Because the choice of time period and benchmark index changes the estimate, different analysts can arrive at meaningfully different CAPM figures for the same stock.

### If a stock's actual return comes in below its CAPM expected return, was it a bad investment?
CAPM computes a required return set in advance, not a report card on what actually happened. A lower realized return usually means the market's broader expectations or the company's own results came in weaker than anticipated during that period — it doesn't mean the CAPM calculation itself was wrong.

### Is CAPM or the Fama-French model more accurate?
Empirically, multi-factor models like Fama-French — which add value, size, and other factors — tend to explain historical return differences better than CAPM alone. Even so, CAPM's simplicity and minimal data requirements keep it the standard starting point for estimating cost of equity in practice.

> ⚠️ This article is for informational purposes only and is not investment advice. You are solely responsible for your own investment decisions.
