---
slug: sharpe-sortino-ratio-risk-adjusted-return
title: "What Is the Sharpe Ratio? Measuring Risk-Adjusted Return, Plus Sortino and Treynor"
description: "Why raw returns alone can't rank two investments fairly, how the Sharpe ratio is calculated, and how the Sortino and Treynor ratios fix its blind spot for upside volatility."
order: 64
updated: 2026-09-06
keywords: ["what is sharpe ratio", "sharpe ratio formula explained", "risk-adjusted return meaning", "sortino ratio vs sharpe ratio", "what is a good sharpe ratio", "treynor ratio explained", "risk-free rate sharpe ratio", "how to compare fund performance"]
seo_audited: 2026-09-06
---

## A 20% Return vs. a 30% Return — Which Fund Actually Did Better?

Fund A returned 20% last year. Fund B returned 30%. On the surface, Fund B looks like the clear winner. But what if Fund A climbed steadily the whole year, while Fund B plunged 25% at one point before rebounding hard enough to finish at 30%? Both funds ended up in positive territory, but the ride to get there was completely different. [What Is Beta?](/en/basics/beta-and-volatility/) covered how sensitively a stock moves relative to the market. This lesson goes a step further: how do you compress "was this really a good result, once you account for how much risk it took to get there?" into a single number you can use to compare investments? The **Sharpe ratio** — a fixture of every fund fact sheet and ETF comparison tool — is the standard answer.

## Why Return Alone Isn't Enough

Comparing investments on return alone hides real information. Two strategies can both post a 10% annual return, but one gets there by grinding out small steady gains month after month, while the other bounces between +15% and -20% along the way. Holding the second strategy through those swings takes far more psychological tolerance and far more careful cash management than the first. This matters even more for money with a fixed withdrawal date, like retirement savings — if that withdrawal happens to land in the middle of a -20% month, the loss you actually feel is worse than the headline number suggests. That's why institutional investors and fund evaluators don't just look at return; they pair it with a **risk-adjusted return** measure — how much volatility was taken on to earn that return. The Sharpe ratio is the most widely used of these.

Think about how you'd evaluate two portfolio managers. One took an aggressive, leveraged, concentrated approach and posted a high return; the other ran a conservative, well-diversified book and posted a lower one. Comparing final returns alone tempts you to call the first manager the better one. But that comparison is only fair if both managers were actually running similar risk. A risk-adjusted metric exists precisely to test that assumption — to separate "got a high return because of luck and leverage" from "generated more efficient return for the same amount of risk taken."

## The Sharpe Ratio: Excess Return Divided by Volatility

The Sharpe ratio, developed by Nobel laureate William Sharpe, is calculated as:

```
Sharpe Ratio = (Portfolio Return − Risk-Free Rate) ÷ Standard Deviation of Portfolio Returns
```

The **risk-free rate** is typically the return on an asset with essentially no default risk, like a government bond. The numerator — "portfolio return minus the risk-free rate" — is called **excess return**: the portion of your return that came specifically from taking on risk, after stripping out what you could have earned just by holding government bonds and taking no risk at all. The denominator, standard deviation, measures how much the portfolio's returns actually bounced around period to period — in other words, how much volatility was taken on to earn that excess return.

So the question the Sharpe ratio answers is: "For every unit of risk taken, how many units of excess return did this investment deliver?" A higher Sharpe ratio means more excess return for the same amount of risk; a lower one means the payoff was thin relative to how bumpy the ride was. As a rough rule of thumb, a Sharpe ratio above 1 is often considered decent and above 2 quite strong — but treat that as a loose, market-dependent benchmark rather than a hard cutoff.

## A Concrete Example: A Lower Return Can Still Win on Sharpe

Back to Fund A and Fund B. Assume the risk-free rate (government bond yield) was 3% over the period.

| | Fund A | Fund B |
|---|---|---|
| Annual return | 20% | 30% |
| Standard deviation of returns | 10% | 35% |
| Excess return (return − risk-free rate) | 17 points | 27 points |
| Sharpe ratio | 17 ÷ 10 = **1.7** | 27 ÷ 35 ≈ **0.77** |

Fund B's return is 10 points higher, but it took more than three times the volatility to get there — so Fund A's Sharpe ratio is over double Fund B's. In other words, Fund A converted risk into return far more efficiently, while Fund B's headline number looks good mainly because the outcome happened to work out. When judging which manager actually did the better job, a risk-adjusted measure like the Sharpe ratio is a far fairer yardstick than the final return alone.

## The Sharpe Ratio's Blind Spot: It Punishes Upside Swings Too

The Sharpe ratio has one structural flaw. Standard deviation, its denominator, treats an above-average month and a below-average month as equally "volatile" — it doesn't distinguish direction at all. A sudden +15% month inflates the denominator by exactly as much as a -15% month would. But what investors actually want to avoid is downside loss, not an unexpected rally. Strategies that grind along steadily most of the time but occasionally spike sharply — an option-selling strategy, or a solid dividend stock that jumps on rare good news — can end up with an inflated standard deviation purely because of those upside spikes, making the Sharpe ratio understate how comfortable the ride actually felt. This asymmetry — treating good surprises and bad surprises as the same kind of "risk" — is worth keeping in mind any time you lean on the Sharpe ratio.

## The Sortino Ratio: Only Downside Volatility Counts

The **Sortino ratio** was built to fix exactly this blind spot. The calculation mirrors the Sharpe ratio, but the denominator swaps in **downside deviation** — volatility measured only from periods that fell short of a target return (often the risk-free rate) — instead of total standard deviation.

```
Sortino Ratio = (Portfolio Return − Target Return) ÷ Downside Deviation
```

An asset with large upside swings will typically show a higher Sortino ratio than Sharpe ratio, since those upside moves no longer inflate the denominator. Because of this, the Sortino ratio is often used alongside — or instead of — the Sharpe ratio by investors who treat losses as the only "real" risk, particularly in evaluating downside-focused retirement portfolios or hedge fund performance.

## The Treynor Ratio: Stripping Out Diversifiable Risk

A third commonly cited metric is the **Treynor ratio**. Both the Sharpe and Sortino ratios use the asset's own standard deviation (total risk) in the denominator, but the Treynor ratio uses [beta](/en/basics/beta-and-volatility/) instead:

```
Treynor Ratio = (Portfolio Return − Risk-Free Rate) ÷ Beta
```

Because beta captures only systematic risk — the portion diversification can't eliminate — the Treynor ratio better answers a specific question: "If I add this asset to a portfolio that's already well diversified, how much excess return does it deliver per unit of market risk?" When evaluating a single stock in isolation, on the other hand, the Sharpe ratio's use of total risk, including that stock's own company-specific risk, gives a more conservative and realistic picture. None of the three is the "correct" one across the board — Sharpe (total risk), Sortino (downside risk), and Treynor (market risk after diversification) are tools that answer different questions, and the right one depends on which question you're actually asking.

Consider an investor who already holds most of their portfolio in a broad index ETF, diversified along the lines covered in [Correlation and Diversification](/en/basics/correlation-and-diversification/), and is now deciding whether to add one individual stock on top. The Treynor ratio is the more appropriate yardstick here, because within an already-diversified portfolio, much of that stock's company-specific risk gets offset by the other holdings — evaluating it on total risk via the Sharpe ratio would overstate how risky the addition really is. If instead that one stock were going to be the investor's entire portfolio, its company-specific risk stays fully exposed, and the Sharpe ratio becomes the more accurate picture.

## What to Watch Out For in Practice

A few pitfalls are easy to miss when using these ratios.

First, **the time period and risk-free rate assumption used both change the result significantly.** A Sharpe ratio calculated over the last year can differ meaningfully from one calculated over five years, and the choice of which government bond maturity to use as the risk-free rate shifts the number too. Before comparing Sharpe ratios from different sources, confirm they were calculated on comparable terms.

Second, **standard deviation assumes returns are roughly normally distributed.** Real-world returns — especially from strategies involving derivatives — often deviate sharply from that assumption, with extreme losses (tail risk) showing up far more often than a standard deviation figure would imply. A high Sharpe ratio doesn't rule out the possibility of a severe loss in an extreme scenario.

Third, these are **historical, backward-looking figures**, with no guarantee that the same risk-adjusted performance continues going forward. Treating a strong Sharpe ratio from one lucky stretch as a forecast of future returns stretches these metrics well past what they were designed to do — fairly comparing performance that has already happened.

Fourth, **a short track record can produce a distorted number purely by chance.** A brand-new fund with less than a year of history showing an unusually high Sharpe ratio might just have launched during an unusually calm stretch for markets overall. As a general guideline, figures calculated over at least three to five years hold up better than ones based on a short window.

## Takeaway

- Return alone can't fully judge investment performance — the same return achieved with very different amounts of volatility reflects very different quality of results.
- The Sharpe ratio divides excess return (return minus the risk-free rate) by total volatility (standard deviation), showing how much excess return was earned per unit of risk.
- Its blind spot is that it penalizes upside volatility exactly as much as downside volatility.
- The Sortino ratio fixes this by using only downside deviation in the denominator; the Treynor ratio uses beta (systematic risk) instead of total risk, which suits evaluating an asset within an already-diversified portfolio.
- All three are backward-looking comparison tools for judging risk-adjusted performance fairly — none of them is a timing signal for when to buy or sell.

## FAQ

### Does a high Sharpe ratio always mean a good investment?
Generally, a higher Sharpe ratio means better risk-adjusted performance over the period measured — but it's a historical calculation, not a guarantee of future results. It also penalizes upside volatility along with downside, so it's safer to view alongside other measures like the Sortino ratio rather than in isolation.

### Where can I find a fund's Sharpe ratio?
Most fund fact sheets, asset manager product pages, and ETF comparison tools publish 3-year and 5-year Sharpe ratios. Be aware that the calculation period and risk-free rate assumption can differ between providers, so direct comparisons require checking those details first.

### Do individual investors need to calculate this themselves?
Not necessarily. But instead of only tracking "how much did I make this month," reviewing how much your account actually swung to get there applies the same underlying idea the Sharpe ratio is built around — just informally.

> ⚠️ This article is for informational purposes only and is not investment advice. You are solely responsible for your own investment decisions.
