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
