# Appendix — Query Reference and Example Screens

## The query syntax, at a glance

```
Metric operator value [AND|OR Metric operator value ...]
```

- **Operators:** `>` `<` `>=` `<=` `=`
- **Logic:** `AND` (narrow) · `OR` (broaden) — every condition is joined to the next by one of these
- **Arithmetic (custom ratios):** `+` `-` `*` `/`

## The most useful metric names

| Family | Metrics |
|--------|---------|
| Size / price | `Market capitalization`, `Current price`, `Book value` |
| Valuation | `Price to earning`, `Price to book value`, `Dividend yield`, `PEG Ratio` |
| Profitability | `Return on capital employed`, `Return on equity`, `OPM` |
| Leverage | `Debt to equity`, `Interest Coverage Ratio`, `Current ratio` |
| Growth | `Sales growth`, `Sales growth 3Years`, `Sales growth 5Years`, `Profit growth`, `Profit growth 3Years`, `Profit growth 5Years` |
| Smoothed | `Average return on equity 5Years`, `Average return on capital employed 5Years` |
| Ownership | `Promoter holding`, `Pledged percentage`, `Change in promoter holding` |
| Cash flow | `Cash from operations last year`, `Free cash flow last year`, `Net cash flow last year` |

Ratio names can change over time; pick them from Screener.in's "Show all Ratios" list rather than typing them from memory.

## Five example screens

**Quality:**
```
Average return on capital employed 5Years > 15
AND Average return on equity 5Years > 15
AND Debt to equity < 0.5
```

**Growth:**
```
Sales growth 5Years > 15
AND Profit growth 5Years > 15
AND Debt to equity < 1
```

**Value:**
```
Price to earning < 15
AND Price to book value < 2
AND Return on equity > 10
```

**Income:**
```
Dividend yield > 3
AND Return on equity > 12
AND Debt to equity < 0.5
```

**Full techno-funda:**
```
Market capitalization > 500
AND Average return on equity 5Years > 12
AND Sales growth 5Years > 10
AND Debt to equity < 1
AND Promoter holding > 30
AND Pledged percentage < 15
```

## The reminder

Every screen is a **filter, not a verdict**. It produces a shortlist of companies that *match your criteria*; whether those are good investments is for the company page, the peers, the shareholding, and your own judgement to decide. Screens find; you decide.
