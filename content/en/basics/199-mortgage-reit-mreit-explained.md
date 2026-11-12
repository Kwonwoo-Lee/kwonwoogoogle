---
slug: mortgage-reit-mreit-explained
title: "What Is a Mortgage REIT (mREIT): How Double-Digit Dividends Come From a Leveraged Spread"
description: "How mortgage REITs hold MBS instead of buildings, borrow short-term through repo to fund them, and why rising rates can trigger margin calls that wipe out book value fast."
order: 199
updated: 2026-11-12
keywords: ["what is a mortgage REIT", "mREIT explained", "why do mortgage REITs pay high dividends", "mREIT dividend cut risk", "equity REIT vs mortgage REIT", "mortgage REIT leverage risk", "AGNC mortgage REIT explained", "mortgage REIT margin calls"]
seo_audited: 2026-11-12
---

## A REIT With No Buildings

[REIT FFO explained](/en/basics/reit-ffo-valuation/) covered equity REITs — the kind that buy actual buildings and collect rent. But US markets also list REITs that own zero physical property and still pay dividend yields in the double digits. AGNC and Annaly (NLY) are the best-known names. Instead of buildings, they hold mortgage-backed securities (MBS) — bonds built from pools of home loans — or mortgage loans themselves. Because the underlying asset is a claim on real estate debt rather than real estate itself, these are called mortgage REITs, or mREITs. They get the same legal tax treatment as any REIT (no corporate tax if at least 90% of taxable income is distributed as dividends), but the business underneath is completely different. An equity REIT earns money from rent. A mortgage REIT earns money from an interest-rate spread. This lesson covers how that spread business actually works, and why it can come apart violently the moment rates move fast.

## The Mechanism: Borrow Short Through Repo, Hold Long in MBS

The basic formula is simple: buy a long-term asset (MBS), and fund that purchase with short-term borrowing. The short-term funding tool is the [repo market](/en/basics/repo-market-explained/). The mREIT pledges its MBS holdings as collateral and borrows cash for terms as short as overnight to a month, then rolls that borrowing over again and again as it matures. The core profit metric in this setup is net interest margin (NIM) — the interest income the MBS portfolio generates, minus the interest expense paid on the repo borrowing, scaled to average assets. Companies report this number every earnings season.

The catch is that this spread is never very wide. The gap between high-quality MBS yields and ultra-short repo rates typically sits within a percentage point or two. A spread that thin can't by itself produce the double-digit dividend yields investors expect from these stocks. So mREITs lean hard on leverage: funding assets many times the size of their own equity through repo. Annaly, one of the sector's largest names, has disclosed GAAP leverage around 8 times equity. Multiply a thin spread by 8x leverage and the return on equity gets large fast — which is exactly what produces the high dividend. It's also exactly what turns any small miscalculation into an outsized loss.

## Why It's Risky: Duration Mismatch, Amplified by Leverage

This setup shares its core vulnerability with the one covered in [bank duration mismatch, explained through SVB](/en/basics/bank-duration-mismatch-svb-explained/): assets (long-term MBS) and funding (short-term repo) sit at mismatched maturities. The difference is that an mREIT runs this same mismatch with money borrowed from capital markets rather than depositors, at leverage ratios banks would never be allowed to carry — which concentrates the risk even further. When rates rise, the hit lands from two directions at once. First, every time repo funding rolls over, the borrowing cost resets higher immediately, squeezing NIM. Second, the market price of the MBS already on the books falls, exactly as described in [bond duration and convexity](/en/basics/bond-duration-and-convexity/), dragging down book value per share.

Repo's collateral mechanics then make things worse. A repo lender holds collateral worth more than the cash lent (a "haircut"), and if the MBS's market price drops, the lender issues a margin call demanding more collateral or cash. mREITs typically hedge against future rate moves with tools like interest rate swaps — as covered in [interest rate swaps explained](/en/basics/interest-rate-swap-irs/), often positioned to receive fixed if rates rise. But those hedge positions can themselves trigger margin calls based on their own mark-to-market losses, meaning falling asset prices and hedge-related margin calls can hit simultaneously. In a fast-moving rate environment, profitability (a shrinking NIM) and capital adequacy (falling book value, margin calls) get attacked at the same time.

## March 2020: Two Weeks of Cascading Margin Calls

The clearest real-world example of this risk materializing is the March 2020 COVID shock. As the Fed slashed rates, Treasury yields collapsed — but at the same moment, a broader liquidity crunch and forced selling across markets pushed MBS and other credit-sensitive asset prices sharply the other way. Repo counterparties re-marked collateral and fired off margin calls across the sector almost simultaneously, compressing months' worth of calls into about two weeks. MFA Financial, for instance, received roughly $800 million in margin calls during that stretch while starting the year with only about $70 million in unrestricted cash. Firms that couldn't meet the calls had to sell MBS at whatever price the market offered, which pushed MBS prices down further and triggered the next round of margin calls elsewhere — a feedback loop. MFA's book value per share fell from $7.04 to $4.34 during the quarter; AG Mortgage Investment Trust's fell from $17.61 to $2.63.

AGNC held up noticeably better. Its portfolio consists almost entirely of agency MBS — securities whose credit risk is effectively guaranteed by Fannie Mae, Freddie Mac, or Ginnie Mae, meaning borrower default risk is close to zero to begin with. AGNC chose to hold its portfolio through the crisis rather than force-sell, and its book value per share fell roughly 25–30% for the quarter — painful, but far milder than peers. That said, the hit wasn't zero: some analysts attribute much of AGNC's loss not to the MBS itself but to mark-to-market losses on its swap and futures hedges. The lesson is that even near-zero-credit-risk assets can produce real losses once the position is carried on heavy leverage with hedges attached.

## How It Differs From an Equity REIT

Both carry the "REIT" label, but investors measure them with entirely different yardsticks. Equity REITs use FFO and AFFO to strip out the accounting distortion of depreciation. Mortgage REITs have no buildings and no depreciation to strip out. Instead, investors watch book value per share and price-to-book (P/B), since book value directly reflects the mark-to-market value of the MBS portfolio and its hedges — which is exactly why it can swing sharply quarter to quarter when rates move. The dividend itself works differently too: an equity REIT's high payout generally reflects steady rental cash flow, while an mREIT's double-digit yield is the product of a thin spread multiplied by leverage, which means it can be cut quickly the moment the rate environment turns unfavorable. Nearly every major mREIT cut its dividend during the 2020 shock. A high headline yield on an mREIT is not, by itself, evidence of safety.

## Key Takeaways

- A mortgage REIT holds MBS or mortgage loans rather than buildings, funding them with short-term borrowing (mainly repo) — a leveraged spread (net interest margin) business rather than a rental business.
- A thin yield spread gets multiplied by leverage, often several times equity, to produce double-digit dividend yields — and that same leverage amplifies losses just as sharply.
- A sharp rate move hits funding costs (squeezing NIM) and asset values (hitting book value) at the same time, and repo margin calls on top of that can trigger a forced-selling spiral, as happened in March 2020.
- Valuation works differently from equity REITs too: book value per share and P/B, not FFO/AFFO, are the metrics that matter for mortgage REITs.

## FAQ

### Is a mortgage REIT's high dividend a safe source of income?
Understand first that the payout comes from a leveraged interest-rate spread, not steady rental income. When that spread compresses or asset values swing, the dividend can be cut fast — and most of the sector actually did cut dividends in March 2020. A high headline yield alone isn't evidence of safety.

### Do falling rates help mortgage REITs?
Generally yes. Repo funding costs reprice almost immediately when short-term rates fall, while income from the existing MBS portfolio adjusts more slowly, which tends to widen NIM. But if rate cuts arrive alongside recession fears, credit spreads can widen at the same time, so the direction of rates alone doesn't guarantee the outcome.

### Is holding only agency MBS safe?
Credit risk (borrower default risk) is close to zero thanks to the government-agency guarantee — that part is accurate. But as AGNC's 2020 experience shows, even credit-risk-free assets can produce real losses from rate-driven price swings and the hedge positions used to manage them. The risk in a mortgage REIT comes from interest-rate exposure and the leveraged structure itself, not credit risk.

### How can investors outside the US get exposure to mortgage REITs?
Most individual mortgage REITs trade on US exchanges and can be bought directly through a brokerage account with US market access, or accessed indirectly through an ETF that holds a basket of mortgage REITs. Either way, checking the leverage level and the type of assets held (agency vs. non-agency) matters more than the headline yield.

> ⚠️ This lesson is for educational purposes only and is not investment advice. Mortgage REITs carry significant leverage and interest-rate sensitivity, so this lesson alone should not be the basis for an investment decision.
