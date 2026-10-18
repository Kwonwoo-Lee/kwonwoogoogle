---
slug: post-earnings-announcement-drift-pead
title: "What Is Post-Earnings Announcement Drift (PEAD)? Why Stocks Keep Moving After a Surprise, Not Just On the Day"
description: "Why earnings-surprise reactions don't end on announcement day but keep drifting the same direction for weeks, explained through the SUE measure, underreaction, and limits to arbitrage."
order: 149
updated: 2026-10-18
keywords: ["what is PEAD", "post earnings announcement drift explained", "why do stocks keep rising after earnings beat", "SUE standardized unexpected earnings", "stock price after earnings surprise", "market anomaly PEAD", "efficient market hypothesis anomaly"]
seo_audited: "2026-10-18"
---

## If the Reaction Doesn't End on Announcement Day

As covered in [Analyst Consensus and Price Targets](/en/basics/analyst-consensus-target-price/), the market reacts to the gap between expectations and results, not to the result in isolation. But if markets are truly efficient, that reaction should be over within a day or two of the announcement — the whole point of "efficient" is that prices jump straight to their new equilibrium the instant new information arrives. Yet the data tells a stranger story. Stocks that report earnings surprises tend to keep outperforming the market for days, weeks, even months afterward, while stocks that miss tend to keep underperforming. It's as if the market doesn't fully digest the news on the day it arrives, and instead keeps catching up to it gradually. That pattern has a name: **post-earnings announcement drift (PEAD)**. This lesson covers what PEAD is, how researchers measure it, why it directly contradicts the efficient market hypothesis, and the competing explanations academics have proposed for why it happens.

## What PEAD Is: An Anomaly First Documented in 1968

PEAD is one of the oldest documented anomalies in finance. Ray Ball and Philip Brown first demonstrated it empirically in 1968, and it has been reconfirmed repeatedly across markets and decades since. The core finding is simple: sort companies that just reported earnings into groups (commonly deciles) based on the size of their earnings surprise, and the group with the biggest positive surprises tends to keep outperforming the market average for months afterward, while the group with the biggest negative surprises tends to keep underperforming. Under the semi-strong form of the [efficient market hypothesis](/en/basics/efficient-market-hypothesis-behavioral-finance/), an earnings surprise — public information — should be fully priced in the instant it's announced, leaving no additional return in either direction afterward. The fact that returns keep drifting in the same direction as the original surprise, long after the news is public, is exactly why PEAD gets classified as a market anomaly rather than something the standard theory predicts.

## How It's Measured: SUE (Standardized Unexpected Earnings)

Studies of PEAD don't just ask whether a company beat or missed — they measure the size of the surprise on a standardized scale so it can be compared across companies. The most widely used measure is **SUE (Standardized Unexpected Earnings)**. It's conceptually similar to the simple surprise percentage covered in [Analyst Consensus and Price Targets](/en/basics/analyst-consensus-target-price/), but with one important difference: a raw surprise percentage just measures how far actual results beat or missed the estimate, while SUE divides that gap by the company's own historical forecast-error standard deviation, putting surprises from different companies on the same statistical footing. A company whose results are usually volatile beating estimates by 20% might look impressive on a raw-percentage basis, but a company whose results are usually stable beating estimates by just 5% could actually represent a far more unusual event once scaled by that company's typical variability. Researchers studying PEAD sort stocks into deciles by SUE and track each decile's post-announcement returns to measure both the existence and the size of the drift.

## Why It Happens: Three Competing Explanations

PEAD's existence has been reconfirmed too many times to dismiss, but why it happens is still an open debate. Three broad explanations compete.

**Underreaction**: The most widely accepted explanation is that investors don't fully price in new information all at once. An earnings report carries not just this quarter's number but implications for future profitability, and if the market takes time to fully absorb those implications, price gradually converges toward its "correct" level over the following weeks — and that slow convergence is what shows up as drift. Research on investor disagreement suggests differing interpretations of the same news can slow this convergence further.

**Limits to arbitrage**: Even if some sophisticated investors recognize the pattern, transaction costs, short-selling constraints, and the thin liquidity of small-cap stocks can make it too costly to fully trade the gap away. PEAD is in fact observed to be stronger among smaller, less liquid stocks — consistent with arbitrage costs preventing the gap from closing completely. Investor distraction, where attention gets split across competing news or a flood of simultaneous earnings releases from other companies, falls into a similar category of explanation.

**Risk-based explanations**: A third camp argues the drift isn't a mispricing at all, but fair compensation for risk. Companies that post large positive surprises may be taking on more exposure to growth- or business-cycle-related risk, and the extra return could reflect compensation for bearing that risk rather than market inefficiency. No single explanation has settled the debate, and recent research tends toward a middle ground: decomposing the total return gap into an immediate "jump" component on announcement day and a slower "drift" component afterward, with both contributing meaningfully to the overall pattern.

## Putting Numbers on the Pattern

A simplified, hypothetical example makes the mechanism concrete. Say a study sorts 1,000 companies that just reported earnings into ten SUE-based groups of 100 stocks each, and tracks each group's cumulative excess return (relative to the market) over the 60 trading days following the announcement.

(The figures below are a simplified, hypothetical illustration of the typical pattern found in PEAD research — not real data.)

| SUE group | Excess return on announcement day | Additional cumulative excess return over the next 60 trading days |
|---|---|---|
| Top 10% (largest positive surprise) | +3.5% | An additional +2% to +4% |
| Middle group | Close to 0% | Close to 0% |
| Bottom 10% (largest negative surprise) | −3.2% | An additional −2% to −4% |

The key detail in this table is that the "announcement day" and "next 60 trading days" columns move in the same direction. Under a fully efficient market, only the announcement-day column should matter, and the following-60-days column should sit near zero for every group. The fact that the top group keeps gaining and the bottom group keeps losing, well after the news is public, is the core empirical evidence behind PEAD.

## An Effect That Weakens Over Time — and a Korea-Specific Twist

Two additional facts round out the picture. First, several studies find that PEAD's magnitude has shrunk considerably compared with the 1970s and 1980s. The dominant explanation is that as the anomaly became widely known, more arbitrage capital moved in to exploit it and narrowed the gap — though some research proposes a competing explanation: that earnings news itself has simply become less persistent from one quarter to the next, which mechanically shrinks the drift regardless of how much arbitrage capital is chasing it. Second, research focused on the Korean market links PEAD specifically to retail investor trading behavior. Studies find that individual investors tend to trade against the direction of the surprise after an earnings release — selling into a positive surprise rather than buying it — and that this contrarian trading pattern is what blocks the price from fully adjusting right away, generating the underreaction that produces the drift. As with any such finding, how pronounced PEAD is varies by study, market, and period, and these are statistical tendencies drawn from historical data rather than a fixed rule.

## What to Keep in Mind When Reading About PEAD

PEAD describes a statistical pattern found in historical data, and this lesson doesn't cover specific entry or exit rules for trading around it — that kind of strategy design belongs to the trading-strategies course. Three things are worth keeping in mind here. First, as with the momentum and value effects covered in [the efficient market hypothesis lesson](/en/basics/efficient-market-hypothesis-behavioral-finance/), accounting for transaction costs, taxes, and the psychological discipline needed to sit through periods when the pattern doesn't show up can shrink PEAD's theoretical excess return considerably in practice. Second, since the effect tends to be larger in small, illiquid stocks, those are also the stocks where trading costs and slippage tend to be highest — eating further into any practical edge. Third, as noted above, the effect's overall magnitude appears to have weakened over time. The most useful way to think about PEAD, in the end, isn't as a signal to trade on immediately after a surprise, but as solid empirical evidence that markets don't absorb new information instantly or completely — and a reminder not to judge a stock's reaction to a big earnings surprise by announcement day alone.

## Takeaway

- PEAD (post-earnings announcement drift) is the tendency for stocks with earnings surprises to keep outperforming or underperforming the market in the same direction as the surprise for weeks to months after the announcement.
- First documented by Ball and Brown in 1968, it's treated as a classic market anomaly that directly contradicts the semi-strong form of the efficient market hypothesis.
- SUE (Standardized Unexpected Earnings) scales a surprise by the company's own historical forecast-error volatility, making surprises comparable across different companies.
- The cause is still debated among three competing explanations: investor underreaction, limits to arbitrage (transaction costs and liquidity constraints), and risk-based compensation.
- The effect's magnitude has weakened over time and tends to be larger in small, illiquid stocks — where real-world trading costs eat into much of the theoretical excess return.

## FAQ

### If PEAD is real, should I just buy stocks right after they report an earnings beat?
Not that simply. PEAD is a statistical tendency drawn from historical data, its magnitude varies by stock, period, and market, and several studies find it has weakened overall in recent decades. Factoring in transaction costs and taxes can shrink or erase the theoretical excess return in practice. This lesson isn't recommending any specific trading rule.

### Does a bigger surprise mean a bigger drift?
Research generally finds that a larger SUE value (a bigger standardized surprise) tends to be associated with a larger subsequent drift. That said, the actual size of the drift also depends on how much of the reaction already happened as an immediate "jump" on announcement day, and how much optimism or pessimism was already priced in beforehand.

### How do efficient-market supporters explain PEAD?
Some argue PEAD isn't a true mispricing but fair compensation for risk — companies with larger surprises may carry more exposure to business-cycle or growth-related risk, so the extra return reflects bearing that risk rather than inefficiency. Whether this fully accounts for the drift, however, remains disputed among academics.

> ⚠️ This article is for informational and educational purposes only and does not recommend any specific trading strategy or security. The figures in this lesson are a simplified, hypothetical illustration of the typical pattern found in PEAD research, not real data. Investment decisions and their outcomes are the sole responsibility of the investor.
