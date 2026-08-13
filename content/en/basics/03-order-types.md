---
slug: order-types
title: "Order Types — Market, Limit, and Stop Orders"
description: "Market orders, limit orders, stop (stop-loss) orders, and trailing stops — the essential order types every trader needs to tell apart, explained with real examples."
order: 3
updated: 2026-08-02
keywords: ["market order vs limit order", "stop loss order", "trailing stop", "order types explained"]
seo_audited: 2026-08-13
---

## Why Order Types Actually Matter

Open a brokerage app for the first time and you'll run into unfamiliar terms like "market order" and "limit order." Gloss over them, and you risk getting filled at a price you didn't want — or missing your exit during a sharp drop because you didn't set a stop. Let's go through each one precisely.

## 1. Market Order

**"Fill this immediately, at whatever the current price is."**

- Pro: Execution is nearly guaranteed (assuming the stock is liquid).
- Con: You don't know exactly what price you'll get. On a thinly traded stock, you can get filled at a worse price than expected (slippage).

> 💡 For high-volume, liquid large-cap stocks, market orders are usually fine because the spread is tight. For low-volume small caps, market orders can be genuinely risky.

## 2. Limit Order

**"Only buy at this price or lower / only sell at this price or higher"** — you specify the exact price yourself.

- Pro: You'll never get filled at a worse price than you specified.
- Con: If the price never reaches your level, your order might never fill at all.

For example, if a stock is trading at $50 and you place a limit buy order at $49.50, it only fills once the price drops to $49.50 or below. If it never gets there, your order just sits unfilled.

## 3. Stop (Stop-Loss) Order

A conditional order that **automatically triggers a market (or limit) order once a specific price is hit.** As the name suggests, it's most commonly used to cap losses.

Example: You bought a stock at $50, and you set a stop-sell order at $48. If the price drops to $48, a sell order fires automatically, preventing further losses.

- **Stop market**: Once the stop price is hit, it fires as a market order — execution is nearly guaranteed, but during a sharp drop you might get filled below your stop price.
- **Stop limit**: Once the stop price is hit, a limit order is placed instead — you get price certainty, but during a sharp drop it might not fill at all.

> ⚠️ **A stop order has to become a habit.** Many beginner investors, once a loss starts growing, hold onto the hope that "it'll bounce back soon" and keep delaying their stop, letting a small loss snowball into a large one. Deciding your stop price before you enter a trade is one of the most important habits for surviving long term.

## 4. Trailing Stop

An order where your stop price automatically moves up as the price rises. For example, set a trailing stop at "5% below the current price":

- Buy at $50 → stop set at $47.50 (-5%)
- Price rises to $55 → stop automatically moves up to $52.25 (-5%)
- If price then drops below $52.25 → automatic sell

This is commonly used in trend-following strategies where the goal is to **let profits run while capping losses.**

## Order Types at a Glance

| Order type | Fill certainty | Price certainty | Typically used when |
|---|---|---|---|
| Market | High | Low | Speed matters more than price |
| Limit | Low | High | You only want to trade at a specific price |
| Stop (stop-loss) | Conditional | Varies | Limiting losses, risk management |
| Trailing stop | Conditional | Varies | Protecting profits in an uptrend |

## Practical Tip: Decide Your Stop Before You Buy

One principle experienced traders consistently emphasize: **decide, before you click buy, exactly how far the price has to fall for you to admit you were wrong and get out.** Doing this:

1. Reduces the chance you'll emotionally delay a stop-loss.
2. Fixes the maximum amount you can lose on any single trade, in advance.
3. Lets you calculate the ratio between your target and your stop (risk/reward) and judge upfront whether the trade is even worth taking.

We'll go deeper into risk/reward in the final lesson of the strategies course.

## Putting a Number on Slippage

Slippage is the difference between the price you placed an order at and the price you actually got filled at. For example, say a stock is trading at $100 and you place a market order to buy 500 shares, but the order book only has 100 shares available at $99.95, with the next levels at $100.10 and $100.20:

```
100 shares × $99.95 + 400 shares × $100.10 = $9,995 + $40,040 = $50,035
Average fill price = $50,035 ÷ 500 = $100.07
```

You thought you were buying a "$100 stock," but your actual average fill was $100.07. That $0.07 difference is slippage. For high-volume stocks, the order book is deep enough that slippage is negligible. For low-volume stocks, placing a large market order can make this gap noticeably larger.

## Fill Conditions: IOC and FOK

Limit orders also support options that specify "how immediately" and "how completely" they need to fill.

- **IOC (Immediate or Cancel)**: Fills whatever quantity it can immediately, and cancels the rest.
- **FOK (Fill or Kill)**: Cancels the entire order if it can't be filled completely, immediately. Used when you don't want a partial fill.

These conditions are mostly used when large quantities need to be executed quickly (like in algorithmic trading), and retail investors don't typically need them day to day — but understanding them helps explain why an order sometimes fills partially and the rest gets canceled.

## Summary

- **Market orders** are fast but the price is uncertain; **limit orders** guarantee price but fill is uncertain.
- **Stop (stop-loss) orders** automatically cap your losses, and deciding your stop level before entering is a critical habit.
- **Trailing stops** are useful for protecting gains while following an uptrend.

In the next lesson, we'll learn to read the **candlestick chart** that sits right next to every order screen.
