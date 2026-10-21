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


# 2. Setup: Install Python, `yfinance`, and `pandas`

## The three tools

Everything in this book uses just three pieces of software:

1. **Python** — the programming language itself. It is almost certainly already on your computer if you use macOS or Linux; on Windows you install it once.
2. **`pandas`** — a Python library for working with tables of numbers. It does the moving-average and RSI arithmetic.
3. **`yfinance`** — a Python library that downloads stock price history from Yahoo Finance. This is where the data comes from.

A "library" is just a bundle of code someone else wrote, that you can call from your own program. You install both libraries with one command.

## Step 1 — Check that Python is installed

Open a **terminal** (on macOS: the "Terminal" app; on Windows: "PowerShell" or "Command Prompt"; on Linux: any terminal). Type this and press Enter:

```bash
python3 --version
```

You should see something like `Python 3.12.4`. Any version `3.10` or newer is fine.

- If you get `command not found` (macOS/Linux) or `'python3' is not recognized` (Windows), install Python from [python.org](https://www.python.org/downloads/) — during installation on Windows, tick the box that says **"Add Python to PATH"**. Then open a *new* terminal and try again.
- If `python3 --version` works, move on.

## Step 2 — Install the two libraries

In the same terminal, run:

```bash
python3 -m pip install yfinance pandas
```

You will see a lot of text scroll past as it downloads the libraries and everything they depend on. The last line should include something like `Successfully installed`. (If you already have them installed, it will say `Requirement already satisfied` — that is also fine.)

> If `pip` refuses with an "externally-managed-environment" or permissions error (common on macOS and Linux), create a *virtual environment* — a private copy of Python just for this project — in the folder where you will keep this book's files, and install into that instead:
>
> ```bash
> python3 -m venv .venv
> source .venv/bin/activate
> python3 -m pip install yfinance pandas
> ```
>
> On Windows, the middle line is `.venv\Scripts\activate`. Run the activate line again each time you open a new terminal for this project.

## Step 3 — Download your first price history

Now write your very first program. Create a new file called `hello.py` in a folder of your choice, using any plain-text editor (Notepad, TextEdit, or VS Code — anything that saves plain text, *not* a word processor). Put this inside:

```python
import yfinance as yf

ticker = yf.Ticker("RELIANCE.NS")
history = ticker.history(period="1y", interval="1d", auto_adjust=False)

print(history.tail())
```

Four things to read, line by line:

- `import yfinance as yf` loads the library and gives it the short nickname `yf`, so the rest of the program can write `yf.Ticker(...)` instead of `yfinance.Ticker(...)`.
- `yf.Ticker("RELIANCE.NS")` creates an object that represents one stock. The `.NS` suffix means "National Stock Exchange" — it tells Yahoo Finance that "RELIANCE" is the Indian listing, not some other company with the same ticker elsewhere.
- `.history(period="1y", interval="1d", auto_adjust=False)` downloads one year of **daily** bars and hands back a table. `auto_adjust=False` keeps the `Close` column free of dividend adjustments (the dividend-adjusted series goes in a separate `Adj Close` column), which is what we want for this kind of screen. Yahoo still adjusts `Close` for splits and bonus issues, so a bonus does not show up as a false crash in the averages.
- `print(history.tail())` shows the last five rows of that table.

## Step 4 — Run it

In the terminal, navigate to the folder where you saved `hello.py`, then run:

```bash
python3 hello.py
```

You should see a table ending in something like this (numbers will differ by the day you run it):

```
                                  Open         High  ...        Close    Volume
Date                                                 ...
2026-09-16 00:00:00+05:30  1243.000000  1255.000000  ...  1240.000000  10023997
2026-09-17 00:00:00+05:30  1244.800049  1253.400024  ...  1243.900024   7752895
2026-09-18 00:00:00+05:30  1245.000000  1247.300049  ...  1226.400024  15122715
```

Each row is one trading day; the `Close` column is the official closing price that day. That single number — the **daily close** — is the foundation of everything else in this book. Moving averages and RSI are all computed from a series of closes.

If you see that table, you have Python, `yfinance`, and `pandas` all working. That is the entire setup.

## A word about free data

Yahoo Finance's free data is genuinely free, but it is not perfect. Occasionally a single ticker will fail to download (you will see how the program handles that in the next chapter), and after corporate actions a ticker can change — for example, when Tata Motors demerged in late 2025 its NSE symbol changed from `TATAMOTORS` to `TMPV`. This is exactly why a screener must be written to *skip gracefully* rather than crash, and why the watchlist is one editable list rather than something buried in the middle of the program.

## Summary

- Python runs your program; `pandas` does the arithmetic; `yfinance` downloads the data.
- Install with `python3 -m pip install yfinance pandas`.
- `yf.Ticker("RELIANCE.NS").history(...)` returns a table of daily prices; `.NS` means the NSE listing.
- The daily **close** is the number every indicator in this book is built from.

Next: turn one ticker into fifty, and teach the program to handle a stock that fails to download.


# 3. Download the NIFTY 50 Universe

## From one stock to fifty

Last chapter you downloaded one stock. A screener is only useful when it looks at a *list*. This chapter replaces the single ticker with a list of fifty — the **NIFTY 50**, the fifty largest and most liquid names on the National Stock Exchange — and teaches the program to keep going when one of them fails.

## The watchlist

Create a new file called `screener.py` (you will keep growing this same file for the rest of the book). Start with the list and a small bit of setup:

```python
import time

import yfinance as yf

WATCHLIST = [
    "ADANIENT", "ADANIPORTS", "APOLLOHOSP", "ASIANPAINT", "AXISBANK",
    "BSE", "BAJAJ-AUTO", "BAJFINANCE", "BAJAJFINSV", "BEL",
    "BHARTIARTL", "CIPLA", "COALINDIA", "DRREDDY", "EICHERMOT",
    "ETERNAL", "GRASIM", "HCLTECH", "HDFCBANK", "HDFCLIFE",
    "HINDALCO", "HINDUNILVR", "ICICIBANK", "ITC", "INFY",
    "INDIGO", "JSWSTEEL", "JIOFIN", "KOTAKBANK", "LT",
    "M&M", "MARUTI", "MAXHEALTH", "NTPC", "NESTLEIND",
    "ONGC", "POWERGRID", "RELIANCE", "SBILIFE", "SHRIRAMFIN",
    "SBIN", "SUNPHARMA", "TCS", "TATACONSUM", "TMPV",
    "TATASTEEL", "TECHM", "TITAN", "TRENT", "ULTRACEMCO",
]

PERIOD = "1y"
INTERVAL = "1d"
```

This is the NIFTY 50 as of October 2026. NSE rebalances the index twice a year, so before you rely on it, refresh the list from the index constituents file on niftyindices.com.

Three things worth noticing:

- The list is **one place**, at the very top. If you want to screen your own ten stocks instead of fifty, you edit this list and nothing else in the program changes.
- `TMPV` is there, not `TATAMOTORS` — because Tata Motors was renamed Tata Motors Passenger Vehicles in late 2025 and the exchange changed its symbol. Tickers are not set in stone, which is the whole reason the next section exists.
- `import time` gives us `time.sleep`, which we use below.

## Download in a loop

Add a loop that walks down the list and prints each stock's last close:

```python
def fetch(symbol):
    """Download one year of daily history for a symbol. Returns None on failure."""
    ticker = symbol + ".NS"
    try:
        df = yf.Ticker(ticker).history(
            period=PERIOD, interval=INTERVAL, auto_adjust=False
        )
    except Exception:
        return None
    if df is None or len(df) < 201:
        return None
    return df[["Close"]]


for symbol in WATCHLIST:
    df = fetch(symbol)
    if df is None:
        print(f"{symbol}: no data, skipped")
        continue
    last_close = df["Close"].iloc[-1]
    print(f"{symbol}: {last_close:.2f}")
    time.sleep(0.4)
```

Read the new pieces:

- **`def fetch(symbol):`** defines a *function* — a named block of code we can call again and again. Anything indented under it belongs to that function.
- **`try:` / `except:`** is error handling. If anything inside `try` raises an error (say the network drops, or the ticker no longer exists), the program runs the `except` block instead of crashing, and returns `None`.
- **`if df is None or len(df) < 201:`** guards against two things at once: a totally failed download, and a download so short it could not even compute a 200-day moving average later. `len(df)` counts the rows. We require at least 201 rows because Chapter 8 needs a 200-day average *plus* the current day.
- **`continue`** jumps to the next item in the loop, so a bad stock is skipped rather than breaking everything.
- **`df["Close"].iloc[-1]`** picks the `Close` column and takes its last row — the most recent close.
- **`f"{symbol}: {last_close:.2f}"`** is a formatted string: it inserts the symbol, then the price rounded to two decimals.
- **`time.sleep(0.4)`** pauses for four-tenths of a second between downloads. It makes the whole run a few seconds slower, but it is polite to the free data source and makes failures less likely.

## Run it

```bash
python3 screener.py
```

You should see fifty lines, one per stock, something like this (illustrative — your prices will differ):

```
ADANIENT: 3020.00
ADANIPORTS: 1824.00
APOLLOHOSP: 8944.50
...
ULTRACEMCO: 10826.00
```

Occasionally one line will instead read `SYMBOL: no data, skipped`. That is the program working as intended — a free data feed hiccup, handled quietly rather than crashing the whole run. (If *most* of the list says "no data", your internet connection is the likely culprit, not the program.)

## Summary

- A watchlist is one editable list at the top of the file.
- `def` defines a reusable function; `try`/`except` stops one bad download from crashing the run; `continue` skips it.
- `df["Close"].iloc[-1]` is "the most recent close".
- `time.sleep(0.4)` is politeness to the free data source.

Next: compute moving averages from that series of closes — the first real indicator.


# 4. Indicators I — Moving Averages

## Why moving averages

From *Swing Trading*, Chapter 2: a **moving average** is the average of the last *N* closes, and it acts as *dynamic* support and resistance. In this framework we use three, and each has one specific job:

| Average | Window | Job |
|---|---|---|
| EMA-20 | 20 days | dynamic support in an uptrend (the "pullback magnet") |
| MA-50 | 50 days | the trend context — its *slope* is the regime tell |
| MA-200 | 200 days | the long-term trend context |

Two of these are **simple** moving averages (the plain average of the last N closes) and one is an **exponential** moving average (which weights recent days more heavily). Both are two lines of code with `pandas`.

## The two functions

Add these to `screener.py`, right after the `WATCHLIST` and `PERIOD`/`INTERVAL` lines:

```python
import pandas as pd


def sma(series, window):
    """Simple moving average: the plain average of the last `window` closes."""
    return series.rolling(window).mean()


def ema(series, span):
    """Exponential moving average. `adjust=False` matches most charting tools."""
    return series.ewm(span=span, adjust=False).mean()
```

- `series.rolling(50).mean()` takes the close series and, at every point, averages the previous 50 closes. That is an MA-50.
- `series.ewm(span=20, adjust=False).mean()` does the exponential version — same idea, but each day is weighted so the most recent day matters most. The `adjust=False` detail is what makes the number match TradingView and most charting platforms.

## Compute them for one stock

Replace the loop at the bottom of `screener.py` with a version that fetches **one** stock and prints its three averages. This is easier to check by eye before we scale back up to fifty:

```python
df = fetch("RELIANCE")
close = df["Close"]

ema20 = ema(close, 20)
ma50 = sma(close, 50)
ma200 = sma(close, 200)

price = close.iloc[-1]
print(f"last close:    {price:.2f}")
print(f"20-day EMA:    {ema20.iloc[-1]:.2f}")
print(f"50-day MA:     {ma50.iloc[-1]:.2f}")
print(f"200-day MA:    {ma200.iloc[-1]:.2f}")
```

Run it:

```bash
python3 screener.py
```

You should see four numbers, like:

```
last close:    1226.40
20-day EMA:    1249.10
50-day MA:     1251.30
200-day MA:    1300.50
```

These are the raw ingredients. Notice what you can *already* read from them, using nothing but the book: the price is below all three averages, which in *Swing Trading* Chapter 3 is the textbook signature of a downtrend. Two chapters from now you will teach the program to read that automatically.

## A first look at the arithmetic

To trust the tool, it helps to see that a moving average really is "the average of the last N closes". For a 3-day simple average of the closes `101, 103, 105`, the value is `(101 + 103 + 105) / 3 = 103`. `rolling(3).mean()` does exactly that, sliding the window forward one day at a time. The EMA is the same sliding idea, but with the newest close weighted most heavily — which is why the 20-day EMA sits *closer* to today's price than a 20-day SMA would after a sharp move.

You do not need to memorise the weighting formula. What matters is the *behaviour*: a rising average means the recent trend is up, a flat average means no trend, a falling average means down. That slope — not the level — is the whole basis of the next two chapters.

## Summary

- `rolling(window).mean()` = simple moving average; `ewm(span, adjust=False).mean()` = exponential moving average.
- We use EMA-20 (dynamic support), MA-50 (trend context), MA-200 (long-term context).
- Price above/below these averages is a first, rough regime read.
- The *slope* of an average — rising, flat, falling — matters more than its level.

Next: the second half of the toolkit — RSI and the short RSI-2 oscillator.


# 5. Indicators II — RSI and RSI-2

## Oscillators measure the extreme

From *Swing Trading*, Chapter 2: an **oscillator** measures whether price is stretched too far to one side. The one this framework uses is the **Relative Strength Index (RSI)**, which is bounded between 0 and 100. Readings near the top are "overbought", near the bottom "oversold".

Crucially — and the book is blunt about this — overbought/oversold only reliably means "likely to pause" **in a range**. In a strong trend, RSI can stay extreme for a long time. That is why RSI is the engine of the *reversion* family, not the trend family, and why our reversion screen (Chapter 8) adds a second filter to keep it out of downtrends.

## The one function

Add this function to `screener.py`:

```python
def rsi(series, period):
    """
    Relative Strength Index over `period` bars, using simple averages.
    RSI-2 (period=2) is the Connors & Alvarez short-reversion oscillator.
    """
    delta = series.diff()
    gain = delta.clip(lower=0.0)
    loss = -delta.clip(upper=0.0)
    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()
    rs = avg_gain / avg_loss
    rsi_vals = 100.0 - (100.0 / (1.0 + rs))
    return rsi_vals.replace([float("inf")], 100.0).fillna(50.0)
```

Read it line by line — this is the most "mathematical" block in the whole book, and it is only eight lines:

- **`series.diff()`** is the day-over-day change: today's close minus yesterday's. A list of moves.
- **`delta.clip(lower=0.0)`** keeps only the *up* moves (any negative change is set to zero) — these are the "gains". **`-delta.clip(upper=0.0)`** keeps only the *down* moves, made positive — the "losses".
- **`gain.rolling(period).mean()`** and its loss twin are the average gain and average loss over the last `period` days.
- **`rs = avg_gain / avg_loss`** is the "relative strength": how much the stock rose, on average, versus how much it fell.
- **`100 - (100 / (1 + rs))`** squeezes that ratio onto the 0–100 scale. If gains and losses are equal (`rs = 1`), RSI is 50. If there are no losses at all, RSI is 100.
- The last line handles two edge cases: no losses at all gives `rs` of infinity (RSI should read 100), and a completely flat two days gives 0 ÷ 0 (we call that neutral 50).

For **RSI-2** you call the same function with `period=2`. A two-day window makes it jump to its extremes fast, which is exactly what makes it useful for spotting short-term stretch — and exactly why the reversion screen uses it. A conventional RSI-14 is the same function with `period=14`, and we compute it too, as a gentler reference value. (Because this function uses simple averages rather than Wilder's smoothing, its readings will not exactly match the RSI on TradingView or your broker's charts.)

## Compute them for one stock

Replace the bottom of `screener.py` again, this time to print both RSIs alongside the close:

```python
df = fetch("RELIANCE")
close = df["Close"]

rsi2 = rsi(close, 2)
rsi14 = rsi(close, 14)

print(f"last close:   {close.iloc[-1]:.2f}")
print(f"RSI-2:        {rsi2.iloc[-1]:.1f}")
print(f"RSI-14:       {rsi14.iloc[-1]:.1f}")
```

Run it:

```bash
python3 screener.py
```

You should see something like:

```
last close:   1226.40
RSI-2:        18.2
RSI-14:       42.0
```

Notice the difference in *behaviour* between the two windows: RSI-2 moves far more than RSI-14. A stock down three days in a row can push RSI-2 into the single digits while RSI-14 stays near the middle. That volatility is a feature for the reversion setup and a nuisance elsewhere — which is why the book's discipline is to use RSI at *extremes in ranges*, not as a free-floating signal.

## Summary

- RSI maps recent gains versus losses onto a 0–100 scale; 50 is neutral, high is overbought, low is oversold.
- RSI-2 is the same formula with a 2-day window — a fast, sensitive short-term oscillator.
- Overbought/oversold is meaningful in ranges; in trends it can simply mean "strong".
- The function is one general formula called with different `period` values.

Next: the concept that ties the whole framework together — is the stock trending or ranging?


# 6. Reading the Regime: Trending or Ranging?

## The decision that precedes every trade

From *Swing Trading*, Chapter 3: before any setup, the swing trader answers one question — **is this market trending or ranging?** The answer chooses the strategy family, because the two families are optimised for opposite conditions and using the wrong one is the fastest way to lose money.

This chapter teaches the program to answer that question automatically, stock by stock, using the **50-day MA slope** — one of the three tests the book names.

## The rule, in plain English

The book gives three ways to read the regime (structure, moving-average slope, and time). We implement the moving-average test because it is the one that translates cleanly into a few lines of code:

- **Uptrend** — price is *above* a *rising* 50-day MA.
- **Downtrend** — price is *below* a *falling* 50-day MA.
- **Range** — everything else: a flat MA, or price and slope disagreeing.

"Sloping" means the MA has moved by more than a tiny amount over the last few days. We measure that as a percentage: if the 50-day MA is **more than 0.5% higher** today than it was 10 days ago, it is rising; **more than 0.5% lower**, falling; anything in between, flat.

## The code

Add these two constants up with the other config (next to `PERIOD` and `INTERVAL`), and the function below:

```python
SLOPE_LOOKBACK = 10        # compare the 50-day MA to itself 10 days ago
SLOPE_THRESHOLD = 0.005    # a 0.5% move over that window = "sloping"


def detect_regime(close, ma50):
    """Label a stock UPTREND, DOWNTREND, or RANGE from its 50-day MA."""
    price = close.iloc[-1]
    ma50_now = ma50.iloc[-1]
    ma50_then = ma50.iloc[-1 - SLOPE_LOOKBACK]

    slope = ma50_now / ma50_then - 1.0
    rising = slope > SLOPE_THRESHOLD
    falling = slope < -SLOPE_THRESHOLD
    above = price > ma50_now

    if above and rising:
        return "UPTREND"
    if (not above) and falling:
        return "DOWNTREND"
    return "RANGE"
```

Read it:

- **`ma50.iloc[-1 - SLOPE_LOOKBACK]`** is the 50-day MA *ten days ago*. Comparing today's MA to that one tells us its slope.
- **`slope = ma50_now / ma50_then - 1.0`** turns that into a fraction: `+0.01` means "1% higher", `-0.01` means "1% lower".
- **`rising` / `falling`** are `True`/`False` flags against the 0.5% threshold.
- The three-way `if` is the plain-English rule above, written as code. The final `return "RANGE"` is the catch-all — when price and slope disagree, or the MA is flat, we refuse to call it a trend.

## Wire it into the run

Replace the bottom of `screener.py` with a version that computes the regime for every stock in the list:

```python
for symbol in WATCHLIST:
    df = fetch(symbol)
    if df is None:
        print(f"{symbol}: no data, skipped")
        continue

    close = df["Close"]
    ma50 = sma(close, 50)
    regime = detect_regime(close, ma50)

    print(f"{symbol}: {regime}")
    time.sleep(0.4)
```

Run it:

```bash
python3 screener.py
```

You should see fifty lines like these (illustrative — the labels change from day to day):

```
ADANIENT: DOWNTREND
ADANIPORTS: RANGE
APOLLOHOSP: RANGE
ASIANPAINT: UPTREND
...
```

## Two honest notes from the book

The book makes two points worth keeping in view before you start *acting* on these labels:

1. **Downtrends are asymmetric in India.** Retail investors can *sell* what they own or use index instruments, but a clean, liquid short side is harder to access than the long side. Many Indian swing traders therefore simply stand aside in downtrends — which is itself a valid decision. A "DOWNTREND" label is information, not an instruction to do anything.
2. **Regimes change.** The single most dangerous moment is the *transition* — a range about to break out, or a trend about to reverse. A stock that has sat in RANGE for weeks is exactly the one to watch for a breakout, not the one to assume will stay quiet.

Our screener reports the label; it does not act on it. The next two chapters add the setups that *interpret* the label — and note how each setup only fires inside the regime it was designed for.

## Summary

- The regime test is price-vs-50-day-MA *plus* the slope of that MA.
- Uptrend = above a rising MA; downtrend = below a falling MA; range = anything else.
- Slope is measured as the MA's % change over 10 days, against a 0.5% threshold.
- The label is information, not an instruction — the book itself says standing aside is valid.

Next: the first setup — the pullback continuation, which only ever fires in an uptrend.


# 7. Screen 1 — The Pullback Continuation

## Trade *with* the trend

From *Swing Trading*, Chapter 4: the **pullback continuation** is the classic trend-following entry. In an uptrend, price occasionally dips back toward its rising 20-day EMA before resuming higher. The setup is "reversal off the rising 20-day EMA in an uptrend" — the pause, not the top.

Screens are mechanical versions of that idea. We want to flag a stock when three things are true at once:

1. The stock is in an **uptrend** (from Chapter 6).
2. Its **20-day EMA is rising** (the trend is still alive).
3. Price has pulled back **close to** that EMA (the "pause" moment), rather than running far above it.

## The code

Add the tolerance constant up with the config, and the screen below:

```python
PULLBACK_TOLERANCE = 0.02   # "close to" the EMA = within +/-2% of it


def pullback_setup(close, ema20, regime):
    """True when an uptrending stock has pulled back to its rising 20-day EMA."""
    if regime != "UPTREND":
        return False

    ema20_rising = ema20.iloc[-1] > ema20.iloc[-6]
    dist = close.iloc[-1] / ema20.iloc[-1] - 1.0

    return ema20_rising and abs(dist) <= PULLBACK_TOLERANCE
```

Read it:

- **`if regime != "UPTREND": return False`** is the regime gate — the whole point of Chapter 6. The pullback setup only exists in an uptrend, so anything else is an immediate "no".
- **`ema20.iloc[-1] > ema20.iloc[-6]`** asks whether the 20-day EMA is higher today than it was five days ago — i.e. *rising*. A flat or falling EMA is not a valid pullback magnet.
- **`dist = close / ema20 - 1`** is how far price sits from the EMA, as a fraction. `dist = 0` means price is exactly on the EMA; `dist = +0.05` means 5% above it.
- **`abs(dist) <= PULLBACK_TOLERANCE`** is "within ±2%". We use `abs` (absolute value) because a stock can pull back slightly *through* the EMA and still count — the book treats levels as zones, not exact lines.

## Wire it into the run

Extend the loop so it computes the EMA and calls the screen for every stock:

```python
for symbol in WATCHLIST:
    df = fetch(symbol)
    if df is None:
        continue

    close = df["Close"]
    ema20 = ema(close, 20)
    ma50 = sma(close, 50)

    regime = detect_regime(close, ma50)
    match = pullback_setup(close, ema20, regime)

    flag = "Pullback setup" if match else "—"
    print(f"{symbol}: {regime:10s} {flag}")
    time.sleep(0.4)
```

Run it:

```bash
python3 screener.py
```

Most lines will read `—`; a few (usually only a handful) will read `Pullback setup`. That scarcity is the point — a screen is only useful because it *filters*. If every stock matched, the list would be the whole market again.

## Why so few, and why that is good

On the single day this book's example was generated (an anecdote, not a statistic), exactly one NIFTY 50 stock matched the pullback setup. That is normal, not a bug. For a stock to qualify it must be in a genuine uptrend *and* currently sitting within 2% of a rising 20-day EMA — a narrow window in time. Most of the time a stock is either not trending up, or already extended well above the EMA (in which case the "pause" already happened and chasing it is late).

Notice what the screen has *not* said: it has not said anything is cheap, or good, or going up. It has only reported a *condition* — an uptrending stock currently near its dynamic support. That is a description, and it is yours to interpret or ignore.

## Summary

- The pullback setup = uptrend + rising 20-day EMA + price within a tolerance band of that EMA.
- The `regime` gate means the screen can only ever fire in an uptrend.
- The band uses `abs()` so a small dip through the EMA still counts — levels are zones, not lines.
- Scarcity of matches is a feature: a screen that filters nothing has no value.

Next: the mirror image from the other family — RSI-2 mean reversion.


# 8. Screen 2 — RSI-2 Mean Reversion

## Fade the extreme, but only in a healthy stock

From *Swing Trading*, Chapter 7: the **RSI-2 mean reversion** is the opposite of the pullback. Instead of favouring strength, it looks for a stock that has been *punished* — pushed down so hard, so fast, that the short-term move is stretched — but which is still healthy over the long term. The book's two rules are:

1. **RSI-2 closes below 5** — the short-term stretch, measured with the fast oscillator from Chapter 5.
2. **Price above the 200-day MA** — the long-term filter that keeps the setup out of broken, downtrending stocks.

The second rule is the one beginners miss, and the one that matters. An oversold reading on a stock that is also *below* its 200-day MA is not a dip — it is a downtrend. The 200-day filter is what separates "stretched within a long-term uptrend" (the setup) from "falling knife" (not the setup).

## The code

Add the threshold constant up with the config, and the screen below:

```python
RSI2_OVERSOLD = 5           # RSI-2 below this = the reversion setup


def rsi2_setup(close, rsi2, ma200):
    """True when a stock is short-term oversold but still above its 200-day MA."""
    price = close.iloc[-1]
    oversold = rsi2.iloc[-1] < RSI2_OVERSOLD
    above_long_term = price > ma200.iloc[-1]
    return oversold and above_long_term
```

Read it — it is deliberately short, because the idea is two filters and nothing else:

- **`rsi2.iloc[-1] < RSI2_OVERSOLD`** is the stretch test: today's RSI-2 is below 5.
- **`price > ma200.iloc[-1]`** is the health test: price is still above its 200-day moving average.
- Both must be true (`and`), or the screen returns `False`.

Notice there is **no regime check here**, unlike the pullback. That is faithful to the book: RSI-2 reversion is a *range and healthy-uptrend* play, not a trend play. The 200-day MA filter does the same job the regime gate did for the pullback — it keeps the setup out of the wrong conditions — just expressed differently.

## Wire it into the run

Extend the loop to compute RSI-2, the 200-day MA, and this second screen:

```python
for symbol in WATCHLIST:
    df = fetch(symbol)
    if df is None:
        continue

    close = df["Close"]
    ema20 = ema(close, 20)
    ma50 = sma(close, 50)
    ma200 = sma(close, 200)
    rsi2 = rsi(close, 2)

    regime = detect_regime(close, ma50)
    pullback = pullback_setup(close, ema20, regime)
    oversold = rsi2_setup(close, rsi2, ma200)

    flags = []
    if pullback:
        flags.append("Pullback setup")
    if oversold:
        flags.append("Oversold (RSI-2)")
    flag = " · ".join(flags) if flags else "—"

    print(f"{symbol}: {regime:10s} {flag}")
    time.sleep(0.4)
```

Run it:

```bash
python3 screener.py
```

Now each stock can show one of three outcomes: a single flag, *both* flags (a stock can, in principle, be both in a pullback *and* short-term oversold), or `—`. A stock flagged "Oversold (RSI-2)" is one the book's reversion family would describe as stretched-but-healthy — nothing more.

## What the two screens together mean

You now have one screen from each family, which is the whole point of the framework:

- **Pullback continuation** fires in **uptrends** — it trades *with* the trend.
- **RSI-2 reversion** fires on **stretched, healthy dips** — it fades the *extreme*.

Both are gated so they can only fire in the conditions the book says they belong in. The regime read from Chapter 6 is what keeps them apart: the pullback needs an uptrend; the reversion needs long-term health regardless of the short-term label. That one-two structure — read the regime, then pick the matching setup — *is* the framework, and it is now running.

## Summary

- RSI-2 reversion = RSI-2 below 5 **and** price above the 200-day MA.
- The 200-day filter is what stops an oversold reading from being mistaken for a "dip" inside a downtrend.
- No regime gate here — the 200-day MA does the equivalent filtering job.
- The two screens are one from each family: trend-following and mean-reversion.

Next: stop printing to the terminal and build the actual dashboard.


# 9. Assemble the Results into an HTML Dashboard

## From printed lines to a page

So far the program prints one line per stock to the terminal. That works, but a dashboard should *look* like one. This chapter changes two things:

1. Instead of printing as we go, we **collect each stock's results** into a list of dictionaries — one tidy record per stock.
2. We **render** that list into a single self-contained HTML page, with styling and a results table, and write it to a file.

Nothing in the *analysis* changes — the indicators, the regime, and the two screens are exactly the code you already wrote. This chapter is about *presentation*.

## Step 1 — Collect the results

Replace the loop's `print(...)` with a list you append to:

```python
def analyze(symbol, df):
    """Run every step for one stock and return a dict of results."""
    close = df["Close"]
    ema20 = ema(close, 20)
    ma50 = sma(close, 50)
    ma200 = sma(close, 200)
    rsi2 = rsi(close, 2)

    regime = detect_regime(close, ma50)
    pullback = pullback_setup(close, ema20, regime)
    oversold = rsi2_setup(close, rsi2, ma200)

    price = close.iloc[-1]
    change_pct = (price / close.iloc[-2] - 1.0) * 100.0
    dist_ema_pct = (price / ema20.iloc[-1] - 1.0) * 100.0

    return {
        "symbol": symbol,
        "close": price,
        "change_pct": change_pct,
        "regime": regime,
        "dist_ema_pct": dist_ema_pct,
        "rsi2": rsi2.iloc[-1],
        "pullback": pullback,
        "oversold": oversold,
    }


results = []
for symbol in WATCHLIST:
    df = fetch(symbol)
    if df is None:
        continue
    results.append(analyze(symbol, df))
    time.sleep(0.4)

results.sort(key=lambda r: r["symbol"])
```

Two new ideas:

- A **dictionary** (the `{...}` blocks) is a labelled bag of values — `results[0]["symbol"]` is the first stock's name. A list of dictionaries is the natural shape for "fifty records, each with the same fields".
- `results.sort(key=lambda r: r["symbol"])` sorts the list alphabetically by symbol. The `lambda` is just a tiny throwaway function that says "the thing to sort by is this field".

## Step 2 — Write a render function

Now add a function that takes that list and returns a complete HTML page as a string. There are two parts: the **styling** (a block of CSS) and the **body** (a table built row by row).

First the CSS — this is presentation, not logic, so you can copy it as-is rather than memorise it:

```python
CSS = """
:root { --bg:#0a0b0d; --surface:#12161a; --border:#1f2624;
  --text:#e8f0ee; --text-muted:#9fb5ae; --text-faint:#6c817b;
  --accent:#2dd4bf; --pos:#2dd4bf; --neg:#f87171; --warn:#fbbf24; }
* { box-sizing: border-box; }
html { color-scheme: dark; }
body { margin:0; background:var(--bg); color:var(--text);
  font-family:"Instrument Sans",-apple-system,"Segoe UI",sans-serif;
  line-height:1.55; -webkit-font-smoothing:antialiased; }
.wrap { max-width:1080px; margin:0 auto; padding:32px 20px 48px; }
h1 { font-family:Georgia,serif; font-size:30px; margin:0 0 4px; }
.sub { color:var(--text-muted); margin:0 0 24px; }
.stats { display:grid; grid-template-columns:repeat(2,1fr); gap:1px;
  background:var(--border); border:1px solid var(--border); border-radius:10px;
  overflow:hidden; margin-bottom:28px; }
@media (min-width:640px) { .stats { grid-template-columns:repeat(5,1fr); } }
.stat { background:var(--surface); padding:16px; }
.stat .num { display:block; font-size:24px; font-variant-numeric:tabular-nums; }
.stat .lbl { display:block; font-size:12px; color:var(--text-muted); margin-top:2px; }
h2 { font-size:18px; margin:28px 0 12px; font-family:Georgia,serif; }
table { width:100%; border-collapse:collapse; font-size:14px; }
th, td { padding:9px 12px; text-align:right; border-bottom:1px solid var(--border); }
th { color:var(--text-muted); font-weight:600; }
th:first-child, td:first-child { text-align:left; }
tbody tr:hover { background:var(--surface); }
.tag { display:inline-block; padding:2px 8px; border-radius:5px;
  font-size:12px; border:1px solid var(--border); color:var(--text-muted); }
.tag.ut { color:var(--pos); border-color:var(--pos); }
.tag.rng { color:var(--warn); border-color:var(--warn); }
.tag.dn { color:var(--neg); border-color:var(--neg); }
.flag { color:var(--accent); font-weight:600; }
.setup-list { list-style:none; padding:0; margin:0; }
.setup-list li { padding:8px 0; border-bottom:1px solid var(--border); }
.disclaimer { margin-top:40px; padding-top:20px; border-top:1px solid var(--border);
  color:var(--text-faint); font-size:12.5px; }
@media print { body { background:#fff; color:#111; } }
"""
```

A quick tour of what matters, so it is not just a wall of text:

- The `:root { --bg: … }` block defines **variables** — named colours used everywhere else. The palette is StratLab's dark theme (near-black background, teal accent `#2dd4bf`).
- `.tag.ut / .tag.rng / .tag.dn` colour the regime label — teal for uptrend, amber for range, red for downtrend. Colour is *reinforcing* a written word here, never the only signal.
- `.stats` turns the summary numbers into a strip of boxes.
- The `@media print { … }` rule at the end makes the page print cleanly, which Chapter 10 relies on for the PDF.

Now the body. This function builds the rows and returns the full page:

```python
def render_html(results):
    n = len(results)
    n_up = sum(1 for r in results if r["regime"] == "UPTREND")
    n_rng = sum(1 for r in results if r["regime"] == "RANGE")
    n_dn = sum(1 for r in results if r["regime"] == "DOWNTREND")
    n_pull = sum(1 for r in results if r["pullback"])
    n_os = sum(1 for r in results if r["oversold"])

    rows = []
    for r in results:
        flags = []
        if r["pullback"]:
            flags.append("Pullback setup")
        if r["oversold"]:
            flags.append("Oversold (RSI-2)")
        flag_txt = " · ".join(flags) if flags else "—"
        tag = {"UPTREND": "ut", "RANGE": "rng", "DOWNTREND": "dn"}[r["regime"]]
        rows.append(
            "<tr>"
            f'<td>{r["symbol"]}</td>'
            f'<td>{r["close"]:.2f}</td>'
            f'<td>{r["change_pct"]:+.2f}%</td>'
            f'<td><span class="tag {tag}">{r["regime"]}</span></td>'
            f'<td>{r["dist_ema_pct"]:+.2f}%</td>'
            f'<td>{r["rsi2"]:.1f}</td>'
            f'<td class="flag">{flag_txt}</td>'
            "</tr>"
        )

    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<title>Swing Trading Screener</title>
<style>{CSS}</style></head>
<body><div class="wrap">
<h1>Swing Trading Screener</h1>
<p class="sub">Regime + two setups from the StratLab Swing Trading guide · {n} symbols scanned</p>
<div class="stats">
  <div class="stat"><span class="num">{n_up}</span><span class="lbl">uptrend</span></div>
  <div class="stat"><span class="num">{n_rng}</span><span class="lbl">range</span></div>
  <div class="stat"><span class="num">{n_dn}</span><span class="lbl">downtrend</span></div>
  <div class="stat"><span class="num">{n_pull}</span><span class="lbl">pullback setups</span></div>
  <div class="stat"><span class="num">{n_os}</span><span class="lbl">oversold (RSI-2)</span></div>
</div>
<h2>All results</h2>
<table><thead><tr>
  <th>Symbol</th><th>Close</th><th>Change</th><th>Regime</th>
  <th>vs 20 EMA</th><th>RSI-2</th><th>Setup</th>
</tr></thead><tbody>{''.join(rows)}</tbody></table>
<p class="disclaimer">Educational content only — not investment advice. StratLab is not
registered with SEBI as an investment adviser, research analyst, or portfolio manager.
This screener surfaces setups that a swing-trading framework describes; it does not
recommend buying or selling any security. Consult a SEBI-registered adviser where appropriate.</p>
</div></body></html>"""
```

The interesting line is the **f-string** (the `f"""..."""` block): anything in `{braces}` gets replaced with its value. So `{n}` becomes the number of stocks, and `{''.join(rows)}` splices in all fifty table rows. The `f'…'` strings inside the row loop work the same way, one row at a time.

## Step 3 — Write the file

Finally, write the string to disk and tell the user where it went:

```python
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent   # the folder this script lives in

html_path = OUTPUT_DIR / "swing_dashboard.html"
html_path.write_text(render_html(results), encoding="utf-8")
print(f"Wrote {html_path.name} — open it in a browser")
```

Run it:

```bash
python3 screener.py
```

Then open `swing_dashboard.html` (double-click it, or drag it into a browser). You should see the full dashboard: the title, a strip of summary numbers, and a table of all fifty stocks with each one's regime and setup flags coloured in.

## Summary

- Collect results into a list of dictionaries — one record per stock — instead of printing as you go.
- A CSS block with `:root` variables gives the page the StratLab dark theme; the `@media print` rule prepares it for PDF.
- F-strings (`f"…"` / `f"""…"""`) splice values into the HTML template.
- `Path.write_text(...)` saves the finished page next to the script.

Next: add the Markdown report and the PDF, and learn to read the result the way the book teaches.


# 10. Export Markdown and PDF, and Read It Like a Swing Trader

## One dashboard, three formats

You have a dashboard. This final chapter adds the two other output formats you were promised — a **Markdown report** and a **PDF** — and then, more importantly, teaches you how to *read* the result the way *Swing Trading* teaches, rather than treating it as a list of instructions.

## Step 1 — The Markdown report

Markdown is plain text with light formatting (the same language this book is written in). Add a function that writes a summary file:

```python
from datetime import date


def render_md(results):
    n_up = sum(1 for r in results if r["regime"] == "UPTREND")
    n_rng = sum(1 for r in results if r["regime"] == "RANGE")
    n_dn = sum(1 for r in results if r["regime"] == "DOWNTREND")
    pull = [r["symbol"] for r in results if r["pullback"]]
    os = [r["symbol"] for r in results if r["oversold"]]

    lines = [
        "# Swing Trading Screener — Report",
        "",
        f"Date: {date.today().isoformat()} · Universe: {len(results)} symbols",
        "",
        f"- **Uptrend:** {n_up}",
        f"- **Range:** {n_rng}",
        f"- **Downtrend:** {n_dn}",
        "",
        "## Pullback setup matches",
        "",
        "- " + (", ".join(pull) if pull else "None today"),
        "",
        "## Oversold (RSI-2) matches",
        "",
        "- " + (", ".join(os) if os else "None today"),
        "",
        "---",
        "",
        "Educational content only — not investment advice. StratLab is not SEBI-registered.",
        "",
    ]
    return "\n".join(lines)
```

Then write it in the same place you write the HTML:

```python
md_path = OUTPUT_DIR / "swing_report.md"
md_path.write_text(render_md(results), encoding="utf-8")
print(f"Wrote {md_path.name}")
```

Run the program, and you now get two files: `swing_dashboard.html` and `swing_report.md`. The Markdown version is deliberately tiny — just the headline numbers and the two lists of matches — because that is what you might want to paste into an AI tool, or version-control, or read on a phone.

## Step 2 — The PDF (via the browser)

The dashboard was written to be print-ready, so the PDF needs no extra library. Open `swing_dashboard.html` in your browser, then:

1. Choose **File → Print** (or press `Ctrl+P` / `Cmd+P`).
2. Set the destination to **"Save as PDF"** instead of a printer.
3. Optionally set margins to "Default", and leave "Background graphics" off for a light printout.
4. Click **Save**.

That is it — a styled PDF of the same dashboard. The `@media print` rule from Chapter 9 is what switches the page to a white background with dark text, so it reads cleanly on paper.

> If you want the program to produce the PDF *automatically* (no browser step), you can later add a `playwright`-based step — the same tool StratLab uses to generate these books' PDFs. For a first screener, the browser's "Save as PDF" is simpler and has zero extra dependencies.

## Step 3 — Read it like the book teaches

Now the important part, which has nothing to do with code. The dashboard gives you three layers of information, and *Swing Trading* tells you how to weigh each one.

**First, read the regime, not the flags.** The strip at the top — how many stocks are uptrending, ranging, downtrending — is the market-level read. If most of the list is `DOWNTREND`, the book's Chapter 3 guidance applies: downtrends are asymmetric in India, and standing aside is itself a valid decision. The setups are only meaningful inside the regime they were built for.

**Second, treat a flag as a *condition*, never an instruction.** "Pullback setup" means an uptrending stock is sitting near its rising 20-day EMA — the condition the continuation family describes. "Oversold (RSI-2)" means short-term stretch inside a long-term healthy stock — the condition the reversion family describes. Neither is a recommendation to do anything. The book is explicit: overbought/oversold only means "likely to pause" in a range, and a flag is a starting point for your own analysis, not a conclusion.

**Third, apply the book's universal rules *before* any flag means anything to you.** From the appendix of *Swing Trading*, the book's rules are:

- Risk 1–2% per trade; size from the stop distance.
- Aim for a favourable reward-to-risk; a 3:1 trade breaks even at 25% wins.
- Honour the stop; hold to the target.
- Account for gap risk; never size for the best case.

A screener that surfaces ten setups has given you ten *candidates to study*, not ten things to do. The framework's job is to shrink the whole market into a short list of conditions worth a second look — which is precisely what you have built.

## Where you are now

You started with a single price download and finished with a tool that, every time you run it, reads fifty stocks, labels their regimes, flags the setups your framework describes, and writes a browser-ready dashboard plus a Markdown report and a PDF. The complete program is in the appendix, in one piece, if you want to read it top to bottom.

## Summary

- `render_md` writes a plain-text summary; the PDF is just the dashboard printed via the browser.
- Read the *regime* first, then the flags — a flag is a condition, not an instruction.
- The book's universal rules (1–2% risk, favourable reward-to-risk, honour the stop) apply before any flag means anything.
- A screener's job is to shrink the market into a short list worth a second look — nothing more.

Next: the complete program, in one place, plus a troubleshooting table.


# Appendix — The Complete Program and Troubleshooting

## The finished program, in one piece

The chapters built this program up piece by piece. This appendix is the finished, polished version in a single listing — the same file shipped alongside this book as `screener.py`. It does everything the chapters built, with a little consolidation — the regime and the two screens are folded into a single `analyze()` function, the RSI-2 flag is stored as `rsi2_setup`, RSI-14 is computed alongside RSI-2, and symbols that fail to download are listed at the end of the run — plus a few extras: a **sortable table** (click a column header to sort), **per-setup match lists** above the table, and the **`data-sort`** attributes that make numeric columns sort as numbers rather than text.

Copy it into a file named `screener.py`, make sure `yfinance` and `pandas` are installed (Chapter 2), and run `python3 screener.py`.

```python
#!/usr/bin/env python3
"""
Swing Trading Screener (educational).

Fetches daily price history for a watchlist (NIFTY 50 by default) using
yfinance, computes the indicators and the two setups from the StratLab
"Build Your Own Swing Trading Screener" guide, and writes two files:

    swing_dashboard.html   -- a self-contained dashboard you open in a browser
    swing_report.md        -- a plain-text summary of the same results

Educational content only. This is NOT investment advice and StratLab is not
SEBI-registered. See the disclaimer at the bottom of the generated page.

Run it with:

    python3 screener.py
"""

import time
from pathlib import Path

import pandas as pd
import yfinance as yf

# ----------------------------------------------------------------------------
# 1. CONFIG -- the only part you normally edit
# ----------------------------------------------------------------------------

# The stocks to scan: the NIFTY 50 as of October 2026. NSE rebalances the
# index twice a year, so refresh this list from niftyindices.com
# (IndexConstituent/ind_nifty50list.csv). The list is editable -- swap in
# your own symbols and the rest of the script keeps working.
WATCHLIST = [
    "ADANIENT", "ADANIPORTS", "APOLLOHOSP", "ASIANPAINT", "AXISBANK",
    "BSE", "BAJAJ-AUTO", "BAJFINANCE", "BAJAJFINSV", "BEL",
    "BHARTIARTL", "CIPLA", "COALINDIA", "DRREDDY", "EICHERMOT",
    "ETERNAL", "GRASIM", "HCLTECH", "HDFCBANK", "HDFCLIFE",
    "HINDALCO", "HINDUNILVR", "ICICIBANK", "ITC", "INFY",
    "INDIGO", "JSWSTEEL", "JIOFIN", "KOTAKBANK", "LT",
    "M&M", "MARUTI", "MAXHEALTH", "NTPC", "NESTLEIND",
    "ONGC", "POWERGRID", "RELIANCE", "SBILIFE", "SHRIRAMFIN",
    "SBIN", "SUNPHARMA", "TCS", "TATACONSUM", "TMPV",
    "TATASTEEL", "TECHM", "TITAN", "TRENT", "ULTRACEMCO",
]

PERIOD = "1y"             # how much history to fetch (enough for the 200-day MA)
INTERVAL = "1d"           # daily bars -- swing trading is a daily-chart game

# Moving-average windows (the toolkit from the guide's Chapter 2)
EMA_FAST = 20             # 20-day EMA -- dynamic support in an uptrend
MA_MEDIUM = 50            # 50-day MA   -- trend context
MA_SLOW = 200             # 200-day MA  -- long-term trend context

# Regime detection (guide Chapter 3: read the slope of the 50-day MA)
SLOPE_LOOKBACK = 10       # how many days back to compare the 50-day MA to itself
SLOPE_THRESHOLD = 0.005   # 0.5% rise/fall over that window = "sloping"

# Screens (guide Chapters 7 and 8)
PULLBACK_TOLERANCE = 0.02  # pullback = close within +/-2% of the 20-day EMA
RSI2_OVERSOLD = 5          # RSI-2 below this = the reversion setup

OUTPUT_DIR = Path(__file__).parent  # write the dashboard next to this script


# ----------------------------------------------------------------------------
# 2. INDICATORS
# ----------------------------------------------------------------------------

def ema(series, span):
    """Exponential moving average. `adjust=False` matches most charting tools."""
    return series.ewm(span=span, adjust=False).mean()


def sma(series, window):
    """Simple moving average."""
    return series.rolling(window).mean()


def rsi(series, period):
    """
    Relative Strength Index over `period` bars, using simple averages.
    RSI-2 (period=2) is the Connors & Alvarez short-reversion oscillator used
    in the guide's reversion screen.
    """
    delta = series.diff()
    gain = delta.clip(lower=0.0)
    loss = -delta.clip(upper=0.0)
    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()
    rs = avg_gain / avg_loss
    rsi_vals = 100.0 - (100.0 / (1.0 + rs))
    # No losses -> RSI is 100 (max strength). No moves at all -> neutral 50.
    rsi_vals = rsi_vals.replace([float("inf")], 100.0).fillna(50.0)
    return rsi_vals


# ----------------------------------------------------------------------------
# 3. FETCH
# ----------------------------------------------------------------------------

def fetch(symbol):
    """Download daily history for one symbol. Returns None on any failure."""
    ticker = symbol + ".NS"  # the ".NS" suffix means National Stock Exchange
    try:
        df = yf.Ticker(ticker).history(
            period=PERIOD, interval=INTERVAL, auto_adjust=False
        )
    except Exception:
        return None
    if df is None or len(df) < MA_SLOW + 1:
        # Not enough history to compute the 200-day MA.
        return None
    return df[["Close"]]


# ----------------------------------------------------------------------------
# 4. ANALYSIS
# ----------------------------------------------------------------------------

def analyze(symbol, df):
    """Compute indicators, regime, and setup flags for one stock."""
    close = df["Close"]

    ema20 = ema(close, EMA_FAST)
    ma50 = sma(close, MA_MEDIUM)
    ma200 = sma(close, MA_SLOW)
    rsi2 = rsi(close, 2)
    rsi14 = rsi(close, 14)

    price = close.iloc[-1]
    price_prev = close.iloc[-2]
    ema20_now = ema20.iloc[-1]
    ma50_now = ma50.iloc[-1]
    ma200_now = ma200.iloc[-1]
    rsi2_now = rsi2.iloc[-1]
    rsi14_now = rsi14.iloc[-1]

    # Regime: slope of the 50-day MA + price's position against it.
    ma50_then = ma50.iloc[-1 - SLOPE_LOOKBACK]
    slope = ma50_now / ma50_then - 1.0
    rising = slope > SLOPE_THRESHOLD
    falling = slope < -SLOPE_THRESHOLD
    above = price > ma50_now

    if above and rising:
        regime = "UPTREND"
    elif (not above) and falling:
        regime = "DOWNTREND"
    else:
        regime = "RANGE"

    # Screen 1 -- pullback continuation: uptrend, rising EMA, close near the EMA.
    ema20_rising = ema20_now > ema20.iloc[-6]
    dist_ema = price / ema20_now - 1.0
    pullback = regime == "UPTREND" and ema20_rising and abs(dist_ema) <= PULLBACK_TOLERANCE

    # Screen 2 -- RSI-2 mean reversion: short-term oversold, long-term healthy.
    rsi2_setup = (rsi2_now < RSI2_OVERSOLD) and (price > ma200_now)

    change_pct = (price / price_prev - 1.0) * 100.0

    return {
        "symbol": symbol,
        "close": price,
        "change_pct": change_pct,
        "regime": regime,
        "dist_ema_pct": dist_ema * 100.0,
        "rsi2": rsi2_now,
        "rsi14": rsi14_now,
        "pullback": pullback,
        "rsi2_setup": rsi2_setup,
    }


# ----------------------------------------------------------------------------
# 5. RENDER
# ----------------------------------------------------------------------------

CSS = """
:root { --bg:#0a0b0d; --surface:#12161a; --surface-raised:#171d21;
  --border:#1f2624; --border-strong:#2a3330; --text:#e8f0ee;
  --text-muted:#9fb5ae; --text-faint:#6c817b; --accent:#2dd4bf;
  --pos:#2dd4bf; --neg:#f87171; --warn:#fbbf24; }
* { box-sizing: border-box; }
html { color-scheme: dark; }
body { margin:0; background:var(--bg); color:var(--text);
  font-family:"Instrument Sans",-apple-system,"Segoe UI",sans-serif;
  line-height:1.55; -webkit-font-smoothing:antialiased; }
.wrap { max-width:1080px; margin:0 auto; padding:32px 20px 48px; }
h1 { font-family:Georgia,"Times New Roman",serif; font-size:30px; margin:0 0 4px; }
.sub { color:var(--text-muted); margin:0 0 24px; }
.stats { display:grid; grid-template-columns:repeat(2,1fr); gap:1px;
  background:var(--border); border:1px solid var(--border); border-radius:10px;
  overflow:hidden; margin-bottom:28px; }
@media (min-width:640px) { .stats { grid-template-columns:repeat(5,1fr); } }
.stat { background:var(--surface); padding:16px; }
.stat .num { display:block; font-size:24px; font-variant-numeric:tabular-nums; }
.stat .lbl { display:block; font-size:12px; color:var(--text-muted); margin-top:2px; }
h2 { font-size:18px; margin:28px 0 12px; font-family:Georgia,serif; }
table { width:100%; border-collapse:collapse; font-size:14px; }
th, td { padding:9px 12px; text-align:right; border-bottom:1px solid var(--border); }
th { cursor:pointer; user-select:none; color:var(--text-muted); font-weight:600; }
th:hover { color:var(--text); }
th:first-child, td:first-child { text-align:left; }
th:nth-child(2), td:nth-child(2) { text-align:left; }
tbody tr:hover { background:var(--surface); }
.tag { display:inline-block; padding:2px 8px; border-radius:5px;
  font-size:12px; border:1px solid var(--border-strong); color:var(--text-muted); }
.tag.ut { color:var(--pos); border-color:var(--pos); }
.tag.rng { color:var(--warn); border-color:var(--warn); }
.tag.dn { color:var(--neg); border-color:var(--neg); }
.flag { color:var(--accent); font-weight:600; }
.setup-list { list-style:none; padding:0; margin:0; }
.setup-list li { padding:8px 0; border-bottom:1px solid var(--border); }
.disclaimer { margin-top:40px; padding-top:20px; border-top:1px solid var(--border);
  color:var(--text-faint); font-size:12.5px; }
@media print { body { background:#fff; color:#111; } th,td { color:#111; } }
"""

SORT_JS = """
function sortTable(n) {
  var table = document.getElementById("results");
  var rows = Array.prototype.slice.call(table.querySelectorAll("tbody tr"));
  var th = table.querySelectorAll("th")[n];
  var asc = th.getAttribute("data-dir") !== "asc";
  table.querySelectorAll("th").forEach(function(h){ h.setAttribute("data-dir",""); });
  th.setAttribute("data-dir", asc ? "asc" : "desc");
  rows.sort(function(a, b) {
    var av = a.cells[n].getAttribute("data-sort") || a.cells[n].textContent;
    var bv = b.cells[n].getAttribute("data-sort") || b.cells[n].textContent;
    var an = parseFloat(av), bn = parseFloat(bv);
    if (!isNaN(an) && !isNaN(bn)) { return asc ? an - bn : bn - an; }
    return asc ? av.localeCompare(bv) : bv.localeCompare(av);
  });
  rows.forEach(function(r){ table.querySelector("tbody").appendChild(r); });
}
"""


def render_html(results):
    """Build the full HTML page as a string."""
    n = len(results)
    n_up = sum(1 for r in results if r["regime"] == "UPTREND")
    n_rng = sum(1 for r in results if r["regime"] == "RANGE")
    n_dn = sum(1 for r in results if r["regime"] == "DOWNTREND")
    n_pull = sum(1 for r in results if r["pullback"])
    n_rsi2 = sum(1 for r in results if r["rsi2_setup"])

    rows = []
    for r in results:
        flags = []
        if r["pullback"]:
            flags.append("Pullback setup")
        if r["rsi2_setup"]:
            flags.append("Oversold (RSI-2)")
        flag_txt = " · ".join(flags) if flags else "—"
        regime_tag = {"UPTREND": "ut", "RANGE": "rng", "DOWNTREND": "dn"}[r["regime"]]
        rows.append(
            "<tr>"
            f'<td>{r["symbol"]}</td>'
            f'<td data-sort="{r["close"]:.2f}">{r["close"]:.2f}</td>'
            f'<td data-sort="{r["change_pct"]:.2f}">{r["change_pct"]:+.2f}%</td>'
            f'<td><span class="tag {regime_tag}">{r["regime"]}</span></td>'
            f'<td data-sort="{r["dist_ema_pct"]:.2f}">{r["dist_ema_pct"]:+.2f}%</td>'
            f'<td data-sort="{r["rsi2"]:.1f}">{r["rsi2"]:.1f}</td>'
            f'<td class="flag">{flag_txt}</td>'
            "</tr>"
        )
    rows_html = "\n".join(rows)

    pull_names = [r["symbol"] for r in results if r["pullback"]]
    rsi2_names = [r["symbol"] for r in results if r["rsi2_setup"]]

    pull_items = "".join(f"<li>{s}</li>" for s in pull_names) or "<li>None today</li>"
    rsi2_items = "".join(f"<li>{s}</li>" for s in rsi2_names) or "<li>None today</li>"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Swing Trading Screener</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;600&display=swap">
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
  <h1>Swing Trading Screener</h1>
  <p class="sub">Regime + two setups from the StratLab Swing Trading guide · {len(results)} of {len(WATCHLIST)} symbols scanned</p>

  <div class="stats">
    <div class="stat"><span class="num">{n_up}</span><span class="lbl">uptrend</span></div>
    <div class="stat"><span class="num">{n_rng}</span><span class="lbl">range</span></div>
    <div class="stat"><span class="num">{n_dn}</span><span class="lbl">downtrend</span></div>
    <div class="stat"><span class="num">{n_pull}</span><span class="lbl">pullback setups</span></div>
    <div class="stat"><span class="num">{n_rsi2}</span><span class="lbl">oversold (RSI-2)</span></div>
  </div>

  <h2>Pullback setup matches</h2>
  <ul class="setup-list">{pull_items}</ul>

  <h2>Oversold (RSI-2) matches</h2>
  <ul class="setup-list">{rsi2_items}</ul>

  <h2>All results (click a column to sort)</h2>
  <table id="results">
    <thead><tr>
      <th onclick="sortTable(0)">Symbol</th>
      <th onclick="sortTable(1)">Close</th>
      <th onclick="sortTable(2)">Change</th>
      <th onclick="sortTable(3)">Regime</th>
      <th onclick="sortTable(4)">vs 20 EMA</th>
      <th onclick="sortTable(5)">RSI-2</th>
      <th>Setup</th>
    </tr></thead>
    <tbody>{rows_html}</tbody>
  </table>

  <p class="disclaimer">Educational content only — not investment advice. StratLab is not
  registered with SEBI as an investment adviser, research analyst, or portfolio manager.
  This screener surfaces setups that a swing-trading framework describes; it does not
  recommend buying or selling any security. Historical observations are illustrative and
  do not guarantee future results. Consult a SEBI-registered adviser where appropriate.</p>
</div>
<script>{SORT_JS}</script>
</body>
</html>"""


def render_md(results):
    """Build the plain-text Markdown report."""
    from datetime import date

    n = len(results)
    n_up = sum(1 for r in results if r["regime"] == "UPTREND")
    n_rng = sum(1 for r in results if r["regime"] == "RANGE")
    n_dn = sum(1 for r in results if r["regime"] == "DOWNTREND")

    pull = [r["symbol"] for r in results if r["pullback"]]
    rsi2 = [r["symbol"] for r in results if r["rsi2_setup"]]

    lines = [
        "# Swing Trading Screener — Report",
        "",
        f"Date: {date.today().isoformat()} · Universe: {n} symbols",
        "",
        f"- **Uptrend:** {n_up}",
        f"- **Range:** {n_rng}",
        f"- **Downtrend:** {n_dn}",
        "",
        "## Pullback setup matches",
        "",
        "- " + (", ".join(pull) if pull else "None today"),
        "",
        "## Oversold (RSI-2) matches",
        "",
        "- " + (", ".join(rsi2) if rsi2 else "None today"),
        "",
        "---",
        "",
        "Educational content only — not investment advice. StratLab is not SEBI-registered.",
        "",
    ]
    return "\n".join(lines)


# ----------------------------------------------------------------------------
# 6. MAIN
# ----------------------------------------------------------------------------

def main():
    results = []
    failed = []

    for symbol in WATCHLIST:
        df = fetch(symbol)
        if df is None:
            failed.append(symbol)
            continue
        results.append(analyze(symbol, df))
        time.sleep(0.4)  # small pause to be polite to the data source

    results.sort(key=lambda r: r["symbol"])

    html_path = OUTPUT_DIR / "swing_dashboard.html"
    md_path = OUTPUT_DIR / "swing_report.md"
    html_path.write_text(render_html(results), encoding="utf-8")
    md_path.write_text(render_md(results), encoding="utf-8")

    print(f"Scanned {len(results)} symbols.")
    if failed:
        print(f"Skipped (no data): {', '.join(failed)}")
    print(f"Wrote {html_path.name}  (open this in a browser)")
    print(f"Wrote {md_path.name}")


if __name__ == "__main__":
    main()
```

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `python3: command not found` | Python not installed, or not on PATH | Install from python.org; on Windows tick "Add Python to PATH", then open a new terminal |
| `ModuleNotFoundError: No module named 'yfinance'` | Library not installed | Run `python3 -m pip install yfinance pandas` |
| Most or all symbols print `no data, skipped` | No internet, or a proxy/VPN blocking Yahoo | Check your connection; disable VPN and retry |
| One specific symbol always skips | Its ticker changed after a corporate action | Look up the current NSE symbol and update `WATCHLIST` (the book's `TATAMOTORS` → `TMPV` is a real example) |
| `Wrote swing_dashboard.html` never appears | The script stopped with an error before it reached the last step | Read the last few lines of the error message (the traceback) — they name the problem, which is often one of the rows in this table |
| Dashboard opens but has no styling | Google Fonts blocked (offline) | The page still works — it just falls back to system fonts |
| The report shows today's date but the prices have not changed since your last run | Ran on a weekend or NSE holiday | Markets are closed Sat/Sun and on holidays; the program simply shows the last session's data |
| Prices look wrong (no decimals, strange values) | You changed `.NS` or `auto_adjust` | Keep the `.NS` suffix and `auto_adjust=False` exactly as shown |

A final reminder that belongs in every appendix of every book in this library: this is education, not advice. The screener is a way to practise turning a framework's rules into code — and the moment it feels like more than that, you are reading it too literally.

---
