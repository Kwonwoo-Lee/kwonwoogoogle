---
slug: shiller-pe-cape-ratio
title: "The Shiller PE (CAPE) Ratio Explained — Smoothing Out the Business Cycle With a 10-Year Average"
description: "Why an ordinary PE ratio gets distorted at earnings peaks and troughs, and how the Shiller PE (CAPE) uses an inflation-adjusted 10-year average to correct for it, with a worked example."
order: 84
updated: 2026-09-16
keywords: ["shiller pe ratio explained", "what is cape ratio", "cyclically adjusted pe ratio", "shiller pe calculation", "cape vs pe ratio", "shiller pe ratio limitations", "pe10 ratio", "cape vs buffett indicator"]
seo_audited: "2026-09-16"
---

## Why an Ordinary PE Ratio Breaks Down at Turning Points

As covered in [PER, PBR, PSR](/en/basics/valuation-multiples-per-pbr-psr/), the ordinary price-to-earnings ratio — price divided by earnings per share — is the most widely used valuation tool there is. It has one structural weakness, though: the denominator is a single year of earnings. When the economy is near a cyclical peak, corporate earnings tend to peak alongside it, making the PE ratio look artificially cheap. When a recession hits and earnings collapse, the same ratio can spike to absurd levels almost overnight — not because the stock got more expensive, but because its earnings temporarily cratered. In the immediate aftermath of the 2008 financial crisis, plenty of companies showed triple-digit PE ratios for exactly this reason. In 1988, Yale economist Robert Shiller — who won the Nobel Prize in Economics in 2013 — and John Campbell proposed a fix aimed squarely at this problem. Today it's known as the **Shiller PE**, or more formally the **CAPE ratio** (Cyclically Adjusted Price-Earnings Ratio).

## What CAPE Actually Measures

The formula looks similar to an ordinary PE ratio, but the denominator is different:

```
CAPE = Inflation-Adjusted Price ÷ 10-Year Average of Inflation-Adjusted EPS
```

Instead of dividing price by the last twelve months of earnings, CAPE divides price by a **10-year average of earnings, with every year's figure first converted to today's dollars using the CPI**. Why bother with the inflation adjustment? Because $1 of earnings from ten years ago doesn't buy what $1 of earnings buys today. As explained in [Nominal vs. Real Returns](/en/basics/nominal-vs-real-returns/), the purchasing power of a fixed sum erodes with inflation over time, so comparing a decade-old nominal EPS figure directly against today's price would understate how large that old earnings figure really was in today's terms. CAPE restates both the price and each year of historical EPS in constant, inflation-adjusted dollars before averaging — so the comparison is apples-to-apples.

## Why Ten Years, Specifically

The ten-year window isn't an arbitrary round number. A full business cycle — an expansion followed by a contraction — typically plays out over roughly that span, so a ten-year average captures both the best year of earnings and the worst year within the same window, preventing either extreme from dominating the ratio on its own. An ordinary PE ratio is a single-year snapshot, so its value swings wildly depending on exactly where in the cycle it happens to be measured. A ten-year average blends the inflated earnings of a boom year with the depressed earnings of a bust year into a much steadier baseline.

## A Worked Example — Why a Collapsed Earnings Year Doesn't Wreck CAPE

Take a hypothetical index trading at 3,000 points. Suppose a recession has just hit and this year's EPS has cratered to 50 points. The ordinary PE ratio comes out to 3,000 ÷ 50 = **60x** — a level that looks historically alarming. But if the same index's 10-year inflation-adjusted average EPS is 150 points, CAPE comes out to 3,000 ÷ 150 = **20x**, a far more measured reading. This year's earnings just happened to hit the bottom of a cyclical trough; viewed across a full decade, the valuation isn't nearly as extreme as the headline PE ratio suggests.

The same logic works in reverse. Suppose instead the economy is at a cyclical peak and this year's EPS comes in unusually strong, at 250 points. The ordinary PE ratio is 3,000 ÷ 250 = **12x** — deceptively cheap-looking. But if that 250 happens to be this decade's best year and the 10-year average is still only 150, CAPE again lands at 3,000 ÷ 150 = **20x**, exactly matching the previous scenario. An investor looking only at the ordinary PE would have drawn opposite conclusions in these two cases — one screaming "expensive," the other "cheap" — while CAPE delivered the same, more consistent reading both times. That consistency is the entire point of the metric.

## Interpreting CAPE — the Historical Average and Its Limits as a Signal

Using data Shiller has compiled on the S&P 500 going back to 1881, the long-run average CAPE is commonly cited as somewhere around 16 to 17. Readings well above that average are generally treated as historically expensive, and readings well below it as historically cheap — but this is an empirically derived reference range, not an absolute buy or sell line. As with the [Buffett Indicator](/en/basics/buffett-indicator-market-cap-to-gdp/), elevated CAPE readings can — and routinely do — persist for years before anything resembling a correction shows up. During the late-1990s dot-com run-up, CAPE climbed well past its historical average and the market kept rising for several more years after that. Extended stretches above the long-run average following the 2009 recovery were also common. Academic research generally treats CAPE as far more useful for gauging expected returns over the next decade or two than for predicting what happens next quarter.

CAPE has its critics, too. As covered in [How Interest Rates Affect Stock Valuations](/en/basics/interest-rates-and-stock-valuations/), a structurally lower interest-rate environment justifies a higher valuation multiple for the same earnings stream, so naively comparing today's CAPE against a century-old average that spans very different rate regimes can be misleading. Some economists — Jeremy Siegel among the more prominent — have also argued that accounting rule changes around the 2008 crisis forced unusually large one-time write-downs at several financial firms, temporarily distorting that decade's average earnings in a way that doesn't reflect the underlying economy as cleanly as the metric assumes. None of this makes CAPE useless, but it's worth treating as one input with known blind spots rather than a single number that settles the question on its own.

## CAPE and Long-Run Expected Returns

The reason CAPE keeps showing up in academic and industry research isn't just that it flags whether the market looks expensive today — it's that, starting with Shiller's own research and echoed in later studies, the level of CAPE at the starting point has generally shown an inverse relationship with realized real returns over the following 10 to 20 years. The intuition is straightforward: paying a high multiple relative to a smoothed decade of earnings means most of your future return has to come from earnings growth alone, since the valuation multiple can't keep expanding indefinitely. Starting from a low CAPE, by contrast, means ordinary earnings growth gets an added tailwind if the multiple simply normalizes back toward its historical average. This is a statistical tendency, not a formula that holds precisely every time — there have been periods where markets kept performing well for far longer than a high starting CAPE would have suggested. The right way to use it is as a probabilistic read on whether the next decade or two is likely to be more or less generous than history's long-run average, not as a forecast of next year's return.

## How to Actually Use It

Given all this, CAPE is most useful not as a trading signal but as a sanity check for long-horizon planning — retirement projections, long-term asset allocation — where it's worth asking whether assuming the historical average return is realistic given today's starting valuation. A retirement plan built starting from an unusually high CAPE might reasonably stress-test a somewhat more conservative return assumption rather than defaulting to the long-run historical average. As with any single valuation gauge, CAPE is more reliable when cross-checked against other measures — the Buffett Indicator, ordinary PE/PB ratios, and the prevailing interest-rate environment — than when read in isolation. And as the examples above illustrate, using a high or low CAPE reading alone as a reason to exit or aggressively add to a market position isn't something the evidence supports.

## Key Takeaways

- An ordinary PE ratio relies on a single year of earnings, which can distort valuation readings sharply at cyclical peaks and troughs.
- CAPE (the Shiller PE) divides price by an inflation-adjusted 10-year average of EPS, which dampens the effect of any single extreme earnings year.
- The same CAPE reading of 20x can correctly diagnose both a "looks like 60x" earnings-collapse scenario and a "looks like 12x" earnings-peak scenario that an ordinary PE ratio would read in opposite directions.
- The long-run S&P 500 average is commonly cited around 16–17x, but this is an empirical reference point, not an absolute threshold — and what counts as "normal" can shift with the interest-rate environment.
- CAPE is better understood as a gauge of multi-decade expected returns than as a short-term timing signal measured in weeks.

## Frequently Asked Questions

### Does a CAPE reading above the historical average mean a crash is coming soon?
Not necessarily. During the dot-com run-up, CAPE spent years above its historical average before the market eventually turned, and there have been extended periods where an above-average CAPE didn't precede any sharp decline at all. It's better treated as a multi-year valuation-regime gauge than a short-term timing tool.

### Is there a Shiller PE / CAPE ratio for the KOSPI?
CAPE was built on — and most widely cited figures are still based on — Shiller's own U.S. S&P 500 dataset going back to 1881. Some research providers publish CAPE estimates for a handful of other countries, but in markets like Korea, where the listed history and accounting standards haven't stayed as long or as consistent as the U.S. record, computing a clean 10-year real-earnings average — and getting a widely agreed, authoritative figure for it — isn't as standardized as it is for the S&P 500.

### Should I trust CAPE more than an ordinary PE ratio?
They serve different purposes rather than competing with each other. An ordinary PE ratio reacts quickly to the latest earnings trend, while CAPE filters out cyclical distortion to give a steadier read on long-run valuation. The two are generally considered most useful together — a signal carries more weight when both point in the same direction.

> ⚠️ This article is for informational and educational purposes only and does not recommend entering or exiting any market at a specific time. The figures in the worked examples are simplified hypothetical values used to illustrate the calculation, not real market data. Actual CAPE readings vary by data provider and calculation methodology.
