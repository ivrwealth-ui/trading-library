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
