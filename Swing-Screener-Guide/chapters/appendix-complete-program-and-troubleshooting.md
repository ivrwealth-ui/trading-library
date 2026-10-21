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
