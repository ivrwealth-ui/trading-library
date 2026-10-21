# 10. Custom Ratios, Export, and Advanced Tips

## Going beyond the built-in data

The previous chapters covered the core workflows. This final chapter covers the *advanced* features — the ones that turn a data-reading tool into a genuine research and modelling workbench — and the tips that separate the expert from the casual user.

## Custom ratios

Screener.in's **custom ratios** let you define *your own* metrics from the underlying data — and then **screen and sort on them**. This matters because some of the most useful numbers are *not* built in.

A custom ratio is an arithmetic expression of the available metrics (using the `+ - * /` operators from Chapter 4). Practical examples:

- **5-year average P/E** — using a 5-year earnings average instead of the single-year figure:
  `Market Capitalization / Average Earnings 5Year` — a smoother valuation that is less distorted by a single exceptional year.
- **Free cash flow** — operating cash flow minus capital expenditure. Screener.in already provides it (`Free cash flow last year`, plus multi-year sums such as `Free cash flow 5years`), so you can screen on it directly or build ratios on top of it.
- **Cash conversion** — how much of profit actually becomes cash:
  `(Cash from operations last year / Net Profit last year) * 100`
- **Debt coverage** — how many years of operating cash flow it would take to repay the debt:
  `Debt / Cash from operations last year`

The power is twofold: you can *sort* the whole market by your custom ratio, and you can *filter* on it in the query builder — so a "quality of earnings" metric you invented becomes a first-class screening criterion.

## Export to Excel

The **Export to Excel** feature downloads a company's (or a screen's) data as a structured Excel file. This is the bridge to *real modelling*:

- **Build a DCF** — discount the projected cash flows to a fair value.
- **Project CAGR** — model what the business might earn and be worth at various growth rates.
- **Track margin/ratio trends** — plot your own charts of the data, beyond what the site shows.
- **Bulk analysis** — export a whole screen (hundreds of companies) and run statistical analysis across them. (Downloading screen results is a paid-plan feature at the time of writing.)

The advanced move: **upload your own Excel template** (Screener.in calls this "Excel Automation"), and Screener.in will remember it and fill it in automatically for any company — turning the tool into a *model-filling* machine, not just a data source.

## The advanced tips

### 1. Read the trend, not the year

Already said, but worth repeating: the long history is the tool's superpower. Always read 5–10 year trends, never a single quarter.

### 2. Click any line item to drill down

On the financial statements, several key line items (such as Sales, Expenses, Other Income, Net Profit, Borrowings, and the cash-flow headings) carry a **+** button — click it and the site shows the breakdown behind the number, year by year. This is how you trace *where* a profit or expense actually came from.

### 3. Check the "Documents" section

The company page's Documents section aggregates announcements, filings, and regulatory documents in one place. For catching *what changed recently* (a pledge increase, a change in ownership, an audit note), it is the fastest check — and it is where you verify that the financial data has not been overtaken by events.

### 4. Use peer comparison before judging any ratio

Never judge a ratio in isolation (Chapter 7). The peer table is one scroll away — use it.

### 5. Use the screens as a starting universe, not an endpoint

A screen is a *filter*. The real work — the company page, the four-question test, the chart timing — happens *after* the screen. The expert uses the screen to *find*, then stops screening and starts *judging*.

### 6. Be aware of the data's limits

Screener.in's data is *reported* and *historical*: it can be restated (a company can revise last year's numbers), delayed, and, for some small companies, incomplete or unaudited. The tool shows you the data faithfully; it does not — and cannot — guarantee the data is the whole truth. For anything material, cross-check against the actual filings.

## The honest close

Screener.in is, at its core, a *filter and organiser of financial data* — and its value is entirely in how you use it. Used casually, it is a convenient way to glance at a company's P/E. Used deliberately — screen to find, company page to vet, custom ratios to deepen, export to model — it is the closest thing an Indian retail investor has to a professional fundamental research terminal. The difference is entirely the *discipline* this book has been teaching.

## Summary

- Custom ratios let you define your own metrics (cash conversion, debt coverage, 5-year P/E) and screen on them.
- Export to Excel — and upload your own template — turns the tool into a modelling workbench.
- Tips: read trends, click to drill down, check Documents, use peers, screen-then-judge, respect data limits.
- The tool's value is in deliberate use: filter, vet, deepen, model.

This completes the main text. The appendix is the query reference and example screens.
