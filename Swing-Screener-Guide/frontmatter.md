# Build Your Own Swing Trading Screener

## A step-by-step guide to turning the StratLab Swing Trading framework into a working yfinance stock screener and HTML dashboard — with no prior coding experience assumed.

---

**Published by StratLab**

---

## Important Disclaimer

This book is provided for **educational purposes only**. It is not investment advice, a recommendation, or a solicitation to buy or sell any security.

- **StratLab is not registered with SEBI** as an investment adviser, research analyst, or portfolio manager, and does not provide investment advisory services.
- Trading involves substantial risk of loss and is not suitable for everyone. You can lose part or all of your trading capital.
- All examples, figures, and historical observations are illustrative. Historical performance never guarantees future results. A screener that flags a setup does **not** mean that setup will be profitable, now or in the future.
- Data from free sources such as Yahoo Finance can be delayed, missing, or wrong — including tickers that change after corporate actions. Always verify before relying on any number.
- Margin, taxes (STT, stamp duty), brokerage, and other regulatory details change over time. Always verify current rules and costs before trading.
- Nothing in this book should be read as a promise of profit or a guarantee that any strategy will be profitable.

By reading this book, you agree that you are solely responsible for your own decisions — including any code you write or run — and that you will consult a SEBI-registered adviser where appropriate.

---

## How to Read This Book

This book teaches you to **build a stock screener** — a small program that downloads price data for a list of stocks and checks each one against a set of rules — and then turns the result into a **dashboard** you can open in a browser. It is a companion to *Swing Trading: Capture Multi-Day Moves with Five Proven Continuation and Reversion Strategies*: where that book teaches the *ideas*, this one teaches you to *compute* a core slice of them yourself.

Two things to know up front:

- **You do not need to know how to code.** Every chapter builds on the last one line by line, and every chapter ends with a program you can actually run. If you can copy, paste, and read one line at a time, you can finish this book.
- **You are building a *screener*, not a trading robot.** The program flags conditions that a swing-trading framework *describes*. It does not trade for you, and it does not tell you what to do. What you do with its output — including deciding to do nothing — is entirely yours.

**How the chapters fit together:**

- **Chapters 1–3** get you set up: what you're building, installing the tools, and downloading your first price data.
- **Chapters 4–5** build the indicator toolbox — moving averages and RSI — the same tools defined in *Swing Trading* Chapter 2.
- **Chapter 6** implements the single most important idea in the book: reading whether a stock is *trending* or *ranging* (from *Swing Trading* Chapter 3).
- **Chapters 7–8** implement two setups — one from each strategy family: the **pullback continuation** (Chapter 4 of *Swing Trading*) and the **RSI-2 mean reversion** (Chapter 7 of *Swing Trading*).
- **Chapters 9–10** turn the results into a styled HTML dashboard, and export them as Markdown and PDF.
- The **appendix** contains the complete, finished program in one place, plus a troubleshooting table.

A note on language: this book describes what a strategy *is* and what conditions it historically aligns with — never what you "should" trade. The dashboard's labels are deliberately neutral ("Pullback setup", "Oversold (RSI-2)") rather than "buy" or "sell". Where results are discussed, they are framed as historical observations, not promises.

---

## Table of Contents

1. What You're Building
2. Setup: Install Python, `yfinance`, and `pandas`
3. Download the NIFTY 50 Universe
4. Indicators I — Moving Averages
5. Indicators II — RSI and RSI-2
6. Reading the Regime: Trending or Ranging?
7. Screen 1 — The Pullback Continuation
8. Screen 2 — RSI-2 Mean Reversion
9. Assemble the Results into an HTML Dashboard
10. Export Markdown and PDF, and Read It Like a Swing Trader

Appendix — The Complete Program and Troubleshooting

---
