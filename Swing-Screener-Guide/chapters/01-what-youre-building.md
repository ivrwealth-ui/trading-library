# 1. What You're Building

## A screener, in one sentence

A **screener** is a program that takes a list of stocks, checks each one against a set of rules, and shows you which stocks currently *match* those rules. By the end of this book you will have written one that:

1. Downloads a year of daily price history for the **NIFTY 50** using a free Python library called **yfinance**,
2. Computes a small set of indicators — moving averages and RSI — for every stock,
3. Reads whether each stock is **trending** or **ranging**,
4. Flags stocks that match two swing-trading setups (one trend-following, one mean-reversion),
5. Writes everything to an **HTML dashboard** you open in a browser, plus a **Markdown report** and a **PDF**.

That final dashboard looks like a table of 50 stocks, with each one labelled by its regime and any setup it matches, and a row of summary numbers along the top.

## Where the rules come from

The rules this program encodes are not invented here. They come from the StratLab *Swing Trading* book — specifically:

- **Chapter 2 ("The Swing Trader's Toolkit")** — defines the moving averages and RSI we use.
- **Chapter 3 ("Reading Trend Structure")** — defines how to tell a trend from a range.
- **Chapter 4 ("Strategy 1 — The Pullback Continuation")** — the first setup we screen for.
- **Chapter 7 ("Strategy 4 — RSI-2 Mean Reversion")** — the second setup we screen for.

Each of those chapters was written to be read by a person — and, because the book ships as clean Markdown, it can also be read by a program. This guide sits on top of that book: you will take a handful of its rules and turn them from prose into runnable code, one line at a time.

## What you will need

- A computer (Windows, macOS, or Linux — all three work the same here).
- An internet connection, because the price data is downloaded live.
- About half an hour, if you follow along without skipping ahead.
- Nothing else. You will install the two free tools in the next chapter.

## What you are *not* building

It is worth being precise, because the word "screener" gets used loosely:

- **Not a trading bot.** The program does not place orders, and it never tells you what to do.
- **Not a backtest.** It looks at *today's* data and flags *today's* conditions; it makes no claim about what would have happened historically.
- **Not financial advice.** A stock that "matches a setup" is not a stock you are being told to trade. The setup is a *description of a condition*, and conditions describe tendencies — they do not promise outcomes.

Keep those three lines in mind and the whole project stays honest. The next chapter gets you started.

## Summary

- A screener = a list of stocks + a set of rules + a display of what matches.
- Ours reads NIFTY 50 daily data, computes indicators, reads the regime, flags two setups, and writes an HTML dashboard.
- The rules come from the *Swing Trading* book's Chapters 2, 3, 4, and 7.
- You need only a computer and an internet connection. You will install the tools next.

Next: install Python, `yfinance`, and `pandas`, and download your first price data.
