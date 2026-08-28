---
slug: insider-cluster-buying
title: "Insider Cluster Buying: Reading SEC Form 4 Filings for Real Conviction"
description: "Learn to filter SEC Form 4 filings for real insider conviction: spot cluster buying by executives and screen out routine option grants."
order: 37
updated: 2026-08-28
keywords: ["insider cluster buying", "SEC Form 4 filing", "insider buying signal", "Form 4 transaction codes", "how to read Form 4", "insider trading screener", "corporate insider buying strategy", "cluster buy stocks"]
seo_audited: 2026-08-28
---

## Selling Is Noisy. Buying Is Not.

Corporate officers and directors sell their own company's stock for dozens of reasons that have nothing to do with pessimism about the business — a kid's tuition, a house down payment, a tax bill, portfolio diversification, cashing out a vested option. That's why experienced investors mostly ignore insider selling as a signal.

Buying is different. When an insider spends their own cash to purchase shares on the open market, there is really only **one plausible reason**: they believe the stock is undervalued at the current price. Nobody is paying them to do it, and nothing forces them to. That asymmetry is why **insider buying** — and especially **cluster buying**, where several insiders independently buy within a short window — has long been treated as a worthwhile supplementary signal. This lesson walks through where to find this data and how to filter it properly. It's often compared with [the congressional trading disclosures covered in Lesson 33](/en/strategies/congressional-stock-trading/), so we'll draw that comparison directly as well.

## What SEC Form 4 Actually Requires

**Form 4** is the filing that officers, directors, and holders of 10%+ of a US public company's stock — collectively called "insiders" — must submit to the SEC whenever they trade shares of their own company. The defining feature is speed: filings are due **within 2 business days of the trade**, a far tighter window than [the 45-day deadline Congress works under](/en/strategies/congressional-stock-trading/). And unlike congressional disclosures, which report only a dollar range, Form 4 discloses the **exact share count and execution price**.

Every Form 4 filing also carries a **transaction code**, and reading that code correctly matters more than most people assume — treating any Form 4 filing as "insider buying" without checking the code leads to bad conclusions.

| Code | Meaning | Value as a signal |
|---|---|---|
| **P** | Open-market purchase with the insider's own cash | Strongest signal — the focus of this lesson |
| S | Open-market sale | Close to noise; too many unrelated motives |
| A | Award or grant (options, RSUs) | Routine compensation, not a conviction bet |
| M | Exercise of a previously granted option | Routine by itself; what matters is whether it's followed by an immediate S |
| G | Gift | Not a trading signal at all |

In practice, the only transactions worth screening for are **code P — open-market purchases made with the insider's own money.** Calling a stock-grant or an option exercise "insider buying" is one of the most common ways this signal gets misread.

<figure class="diagram">
  <img src="/static/img/charts/en/insider-cluster-buying.svg" alt="Diagram with a left panel filtering SEC Form 4 transaction codes into a strong signal (open-market purchase, code P) versus weak signals (award grants and option exercises, codes A and M), and a right panel showing a timeline where three different executives buy independently within a 15-day window to form a cluster-buy signal" loading="lazy">
  <figcaption>Left: signal strength depends heavily on the transaction code. Right: multiple insiders buying independently within a short window forms a cluster-buy signal.</figcaption>
</figure>

## What the Academic Research Actually Found

Insider trading's informational value has been studied for decades. One of the most frequently cited papers is Josef Lakonishok and Inmoo Lee's 2001 study, "Are Insider Trades Informative?", published in the *Review of Financial Studies*. It examined insider transactions across the full US market from 1975 to 1995, and the qualitative findings are worth knowing:

- The market barely reacted, on average, at the moment an insider trade was disclosed.
- Looking forward, though, **insider purchases carried meaningful predictive power for subsequent stock returns.**
- **Insider sales, by contrast, showed essentially no predictive power** — consistent with the "too many unrelated motives" problem described above.
- That predictive power was **considerably stronger in smaller companies** than in large ones, which lines up with the intuition that information asymmetry — thinner analyst coverage, less public disclosure — is where an insider's private knowledge matters most.

Keep in mind this data runs through 1995. Since then, free tracker sites and wider internet access have made Form 4 data far easier to find, and more market participants now react to the same filings almost immediately — which plausibly compresses whatever edge existed in the original study. That's a reasonable inference the industry makes, not a verified, up-to-date statistic.

## Why a Cluster Beats a Single Insider's Buy

One executive's purchase can still be a personal call — maybe they're simply an optimist, or the tax timing happened to work out. It reads very differently when **several insiders with different reporting lines and different personal finances independently make the same decision within a short window.** Nobody coordinated it; each person looked at the same internal reality and arrived at a similar conclusion on their own. That's the core logic behind treating **cluster buying** as a comparatively more reliable signal than any single filing.

The screening conventions traders and trackers commonly use are rules of thumb, not official regulatory thresholds:

| Screening criterion | Common rule of thumb | What it suggests |
|---|---|---|
| Cluster size | 2+ insiders within 7 days, or 3+ within 15 days | Less likely to be coincidence, more likely a shared read |
| Transaction code | Only count code P (open-market purchase) | Codes A and M are compensation events, not bets |
| Seniority | Weight CEO/CFO purchases above outside directors | Convention that they likely see more internal detail |
| Trade size | Meaningful relative to the insider's salary or existing stake | Separates token gestures from real commitments |
| Timing | Right after earnings, or after a sharp price drop | Purchases right after a blackout lifts likely reflect fresh information |
| Market cap | Signal tends to be more meaningful in small/mid-caps | Matches the academic finding that information asymmetry drives the effect |

The timing criterion matters operationally. Public-company insiders are legally barred from trading during a "blackout period" ahead of earnings. So when several executives buy within days of that blackout lifting — right after the numbers come out — it's a reasonable inference that they're reacting to information they just confirmed, not to something stale.

## A Worked Example: Putting Numbers to a Cluster

Here's a purely illustrative scenario. Mid-cap semiconductor equipment maker Stock F drops 18% after issuing weak guidance alongside earnings. Once the post-earnings blackout lifts, three Form 4 filings land over the following 8 days:

- Day 3: the CFO buys 40,000 shares at $22, code P — roughly $880,000
- Day 5: an independent director buys 10,000 shares at $21.50, code P — roughly $215,000
- Day 8: the COO buys 15,000 shares at $23, code P — roughly $345,000

All three are code P, and three insiders at different levels of the company bought independently within an 8-day window — meeting the cluster criteria laid out above. Total purchase value comes to roughly $1.44 million, and the fact that the CFO — the person closest to the company's actual financial picture — put in the largest amount right after the blackout lifted is the kind of detail that tends to raise confidence in the cluster. None of this guarantees the stock recovers. It's qualitative evidence that management is confident enough in the current price to commit personal capital, nothing more.

## Insider Buying vs. Congressional Trading

As covered in [Lesson 33](/en/strategies/congressional-stock-trading/), congressional STOCK Act disclosures get compared to insider Form 4 filings often, since both fall under "follow the public paper trail of people with an information edge." But the character and speed of the two are quite different.

| Aspect | Corporate Insider (SEC Form 4) | Congress (STOCK Act) |
|---|---|---|
| Disclosure deadline | Within 2 business days | Within 45 days |
| Dollar detail | Exact share count and price | Range only |
| Nature of the edge | Direct knowledge of company operations and results | Indirect exposure to legislation, policy, budget |
| Sample size | Thousands of public companies' worth of insiders | Roughly 535 members |
| Depth of academic research | Studied since the 1970s | Comparatively short and limited |

Both sit in the same broad category of "publicly disclosed information about people with an edge," but Form 4 insider buying has a stronger case on disclosure speed, precision, and research depth. The conclusion for both, though, is identical: treat either one as a supplementary input, never a standalone buy trigger.

## Where to Check This for Free

Raw Form 4 filings are available to anyone, for free, through the SEC's **EDGAR** system. Filtering a company's EDGAR page to "Form 4" surfaces the latest filings directly, and a number of free and paid tracker sites aggregate this data into screens that surface cluster-buy activity automatically. Trusting a tracker's summary alone is riskier than it looks — checking the transaction code (confirming it's actually P) and glancing at the original filing takes a minute and catches most misreads before they matter.

## Limitations and Pitfalls

- **Insiders are wrong sometimes too.** A purchase doesn't guarantee the stock goes up — even the people closest to a business can't dodge a macro shock or an industry-wide downturn.
- **Two business days is fast, but still not real-time.** Some of the price move may already be baked in by the time a filing hits EDGAR.
- **The signal weakens at mega-cap scale.** When a company's market cap runs into the hundreds of billions, an individual executive's purchase is a rounding error relative to the total float, which dilutes the signal's meaning.
- **Wider awareness may have compressed the edge.** As free trackers made this data easier to access, more market participants now react to the same filings quickly, plausibly shrinking whatever excess return the older academic research measured.
- **Watch for 10b5-1 pre-scheduled plans.** A large share of insider sales execute automatically under pre-arranged 10b5-1 plans. Purchases are less commonly pre-scheduled this way, which is part of why they tend to read as more discretionary — but it's worth checking the filing's footnotes to confirm.
- **Not a standalone thesis.** This belongs alongside valuation work, financial statement review, and sector context — not in place of them.

## FAQ

### Where can I check Form 4 filings for free?
The SEC's EDGAR system (sec.gov) lets you search by company name or ticker and pull up every Form 4 filing for free. A number of free and paid tracker services also aggregate this data and offer built-in cluster-buy screening.

### Is a corporate buyback the same thing as insider buying?
No. A buyback is **the company** repurchasing its own shares with corporate cash; Form 4 insider buying is **an individual officer or director** purchasing shares with personal money. Both can read as a positive signal from management, but the disclosure mechanics, scale, and underlying motive differ enough that they're worth analyzing separately.

### Is every insider purchase a strong signal?
No. The weight of the signal depends heavily on whether the transaction code is P (open-market purchase), whether multiple insiders bought independently within a short window (a cluster), and how senior the buyer is relative to the size of the trade. Reading a single code-A grant, or one small purchase, as "strong management conviction" overstates what the filing actually shows.

## Summary

- Form 4 requires officers, directors, and 10%+ holders to disclose trades within 2 business days — far faster and more precise than congressional disclosures.
- Insider selling is too noisy to read reliably, but open-market purchases under transaction code P are a comparatively cleaner signal of genuine conviction.
- Lakonishok and Lee (2001) found insider purchases carried real predictive power for future returns, especially in smaller companies, though that data runs through 1995 and today's much wider data access may have narrowed the effect.
- Cluster buying — 2+ insiders within 7 days, or 3+ within 15 days, buying independently — is conventionally treated as more reliable than any single filing.
- Checking the transaction code, weighting seniority, watching post-earnings timing, and favoring small/mid-caps makes for a more defensible screen than following every filing blindly, and this should always stay a supplementary signal rather than a standalone trigger.
