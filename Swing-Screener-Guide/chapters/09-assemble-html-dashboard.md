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
