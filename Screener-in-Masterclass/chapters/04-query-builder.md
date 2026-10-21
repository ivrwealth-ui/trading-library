# 4. The Query Builder: Syntax and Power

## The tool's most under-used feature

The **query builder** is the single most powerful feature on Screener.in — and the one most people never learn. It is a text box (under "Create a stock screen") where you write *your own* screening logic in a simple, English-like language. This chapter teaches the syntax, and how to use it to express a real investment philosophy.

## The basic form

A query is one or more conditions, each of the form:

```
Metric operator value
```

Conditions are joined with `AND` (or `OR`); putting each condition on its own line keeps a long query readable. For example:

```
Return on capital employed > 20 AND
Price to earning < 15
```

Run it, and the table shows every company matching all the conditions.

## The operators

### Comparison operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `>` | greater than | `Sales growth > 15` |
| `<` | less than | `Debt to equity < 0.5` |
| `>=` | greater than or equal | `Return on equity >= 20` |
| `<=` | less than or equal | `Price to earning <= 25` |
| `=` | equal to | `Promoter holding = 75` |

### Logical operators

| Operator | Meaning | Use |
|----------|---------|-----|
| `AND` | all conditions must be true | Narrow the list |
| `OR` | at least one condition true | Broaden the list |

`AND` is the default way to build a screen — you stack criteria, and each one narrows the list. `OR` is for "either this or that" (e.g., high sales growth OR high profit growth).

### Arithmetic operators (for custom ratios)

You can do arithmetic *inside* the query, which is how you create ratios that are not built in:

- `+` addition, `-` subtraction, `*` multiplication, `/` division.

For example:

```
Current price < 1.5 * Book value
```

This finds companies trading below 1.5× book value — a custom condition expressed in one line, using the built-in `Current price` and `Book value` metrics.

## The metric names

Screener.in has hundreds of pre-computed metrics, and the query language uses their **exact names** (e.g., `Return on capital employed`, `Debt to equity`, `Sales growth 3Years`). The complete list is available via the "Show all Ratios" link below the query box. Ratio names can change over time, so pick them from that list rather than typing them from memory. The most useful names to know:

- **Size/price:** `Market capitalization`, `Current price`, `Book value`
- **Valuation:** `Price to earning`, `Price to book value`, `Dividend yield`, `PEG Ratio`
- **Profitability:** `Return on capital employed`, `Return on equity`, `OPM` (operating profit margin)
- **Leverage:** `Debt to equity`, `Interest Coverage Ratio`, `Current ratio`
- **Growth:** `Sales growth`, `Sales growth 3Years`, `Sales growth 5Years`, `Profit growth`, `Profit growth 3Years`, `Profit growth 5Years`
- **Averages:** `Average return on equity 5Years`, `Average return on capital employed 5Years`
- **Ownership:** `Promoter holding`, `Pledged percentage`, `Change in promoter holding`
- **Cash flow:** `Cash from operations last year`, `Free cash flow last year`, `Net cash flow last year`

The `5Years` / `3Years` suffixes and `Average … 5Years` forms are how you ask for *multi-year* and *smoothed* figures — which matters, because a single year's ROE is noisy; a 5-year average is a much better signal of a durable business.

## Building a screen, step by step

The master's approach to the query builder is **incremental**: start broad, add criteria one at a time, and watch the list shrink to a meaningful shortlist.

Start with size (market cap in ₹ crore):

```
Market capitalization > 1000 AND Market capitalization < 5000
```

Add profitability:

```
... AND Return on capital employed > 15
```

Add safety:

```
... AND Debt to equity < 0.5
```

Add growth:

```
... AND Sales growth 3Years > 10
```

The result — "small-caps with ROCE above 15%, low debt, and growing sales" — is a complete, testable investment criterion, written in four lines. Each `AND` narrows the list, and the table shows exactly which companies pass.

## Saving and re-running

Once you have a screen you like, **save it** (Screener.in's own guide calls the button "Save Your Query"; labels may differ). From then on it is one click to re-run, and you can set an **email alert** (free accounts get only a few) to be notified when a new company enters the screen. This is what turns a one-off search into a *system*: your screen becomes a permanent, self-updating shortlist.

## The honest caveats

1. **The screen is a filter, not a verdict.** A screen returns companies that *match your criteria* — it does not know whether your criteria are good, or whether the matching companies are good investments. The company page (next chapters) is where you find out.
2. **Garbage in, garbage out.** A screen is only as meaningful as the criteria behind it. A screen tuned to look good on recent data is overfit (the Systematic Trading Framework book's lesson applies to screens too).
3. **One number rarely tells the story.** "ROCE > 15%" is a fine start, but a company with a 15% ROCE *and* 3× debt is different from one with 15% ROCE *and* no debt. Screens set the floor; the company page tells the story.

## Summary

- The query builder uses `Metric operator value`, with `AND`/`OR` and arithmetic (`+ - * /`).
- Metric names are exact (e.g., `Return on capital employed`, `Sales growth 3Years`); `Average … 5Years` gives smoothed figures.
- Build incrementally: size → profitability → safety → growth, watching the list narrow.
- Save and re-run; set email alerts to make it a self-updating system.
- A screen is a filter, not a verdict — the company page explains the results.

Next: the company page — the deep-dive.
