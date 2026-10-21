# TradingView Screeners with Pine Script v6: Recognised-Strategy Scanners, Fully Coded

## Valuation, earnings power, momentum, stage analysis, outperformance, price contraction, Dow Theory, and multi-timeframe screeners — each a complete Pine v6 script — with clear disclaimers.

---

**Published by StratLab**

---

## Important Disclaimer

This book is provided for **educational purposes only**. It is not investment advice, a recommendation, or a solicitation to buy or sell any security.

- **StratLab is not registered with SEBI** as an investment adviser, research analyst, or portfolio manager, and does not provide investment advisory services.
- Trading and investing involve substantial risk of loss, including the possible loss of principal. Past performance never guarantees future results.
- The strategies encoded here are well-known, widely discussed approaches; they are described and coded for *education*, not as a claim that any of them will be profitable.

## Code Disclaimer

The Pine Script® code in this book is **illustrative and provided "as is", without warranty of any kind.** Specifically:

- It has **not been guaranteed to compile on every TradingView plan or version**, and TradingView's language, functions, and data availability change over time. Always paste into the Pine Editor and resolve any warnings or errors before relying on it.
- **Fundamental-data functions (`request.financial()`, `request.earnings()`) require the relevant data subscription/plan** and may return `na` (no data) for many symbols — especially on NSE/BSE names. Scripts are written to fail *silently* (no signal) when data is unavailable.
- A **screener is a filter, not a trade signal.** Every result must be reviewed independently; the screen merely shortlists candidates for *your own* analysis and decision.
- **Test on paper or demo before any live use.** Screener output is not a recommendation to buy or sell.
- Pine Screener availability, the one-indicator-per-screen limit, the 40-request-call limit, and the 500-bar lookback limit are TradingView features that may change; verify current behaviour in your account.

"Pine Script" and "TradingView" are trademarks of TradingView, Inc. This book is not affiliated with, endorsed by, or sponsored by TradingView.

By reading this book, you agree that you are solely responsible for your own trading decisions and that you will consult a SEBI-registered adviser where appropriate.

---

## How to Read This Book

This book teaches you to build **TradingView screeners** using **Pine Script v6**, encoding strategies that are widely considered *substantive* — valuation, earnings power, momentum, stage analysis, outperformance, price contraction, Dow Theory, and multi-timeframe analysis — rather than trivial moving-average crossovers.

- **Chapters 1–2** explain the *types* of TradingView screeners and the Pine v6 essentials (including how to pull fundamental data) that every script uses.
- **Chapters 3–10** are eight screener scripts, each a complete, copy-pasteable Pine v6 script. Every chapter follows the same pattern: the strategy's idea, the exact logic, the full code, and how to read its columns.
- **Chapters 11–12** cover how to load and use the screeners, and the code best practices and disclaimers that govern them.
- The **appendix** indexes all eight scripts and points to the consolidated eight-factor script.

A note on language: this book describes what a screen *is* and what a strategy has historically been understood to do — never what you "should" buy. Screeners are filters; decisions are yours.

---

## Table of Contents

1. TradingView Screener Types
2. Pine Script v6 Essentials
3. Screener 1 — Valuation (P/E, P/B)
4. Screener 2 — Earnings Power (EPS & Revenue Growth)
5. Screener 3 — Momentum (12-Month Return, 52-Week High)
6. Screener 4 — Stage Analysis (Weinstein Stage 2)
7. Screener 5 — Outperformance (Relative Strength vs. Benchmark)
8. Screener 6 — Price Contraction (VCP)
9. Screener 7 — Dow Theory (Trend Structure + Volume)
10. Screener 8 — Multi-Timeframe (Weekly Trend + Daily Trigger)
11. Loading and Using Your Screeners
12. Code Best Practices and Disclaimers

Appendix — Consolidated Scripts

---
