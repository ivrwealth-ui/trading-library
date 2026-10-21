# 3. The Screener Table and Columns

## The spreadsheet that is the whole market

When you run a screen, Screener.in returns a **table** — one row per company, one column per metric. This table is the entire listed market, viewed through whatever columns you choose. Understanding the table — and the columns — is the first half of mastering the tool.

## Reading the table

- **Rows** are companies (sorted however you choose).
- **Columns** are financial metrics (market cap, P/E, ROCE, growth, debt, and so on).
- **Click any column header** to **sort** by it — ascending or descending. This is arguably the single most-used action in the tool: sorting a screen by P/E to find the cheapest, or by ROCE to find the most profitable.

The table is *interactive and instant*: change a filter in the query, and the table updates immediately; click a column, and the sort changes instantly. This responsiveness is what makes the tool feel powerful — you can iterate a screen in seconds.

## Choosing columns: "Edit columns"

The default table shows a standard set of columns, but the real power is in choosing **your own**. The "Edit Columns" button lets you add or remove any of hundreds of metrics, so the table shows *exactly* what your strategy cares about.

For example, if your strategy is "high-ROCE, low-debt, growing companies", you might build a table with exactly these columns:

- Market Capitalization
- Price to Earning
- Return on Capital Employed (ROCE)
- Return on Equity (ROE)
- Debt to Equity
- Sales Growth 3Years
- Profit Growth 3Years

Now the table *is* your strategy, and sorting by each column answers each part of it.

## The most important columns, grouped

The hundreds of columns fall into a few families. Knowing the families is more useful than memorising every column name:

| Family | Examples | What it tells you |
|--------|----------|-------------------|
| **Size & price** | Market Capitalization, Current Price, Book Value | How big, how expensive in rupees |
| **Valuation** | Price to Earning, Price to Book, Dividend Yield, PEG | Cheap or expensive |
| **Profitability** | ROCE, ROE, Operating Margin | How efficiently it uses capital |
| **Leverage** | Debt to Equity, Interest Coverage, Current Ratio | How safe the balance sheet is |
| **Growth** | Sales Growth (3Y/5Y), Profit Growth, EPS Growth | How fast it is compounding |
| **Ownership** | Promoter Holding, FII, DII, Pledged % | Who owns it, and any red flags |

The master's habit: **never read a company as a single number — always read it across these families.** A high ROE *with* high debt is a different business from a high ROE *with* low debt; the columns only make sense together.

## Custom columns (custom ratios)

Beyond the built-in columns, you can define **your own columns** — custom ratios computed from the data. Screener.in's plan comparison lists it as available on the free plan at the time of writing, and it is powerful: you can define, say, a "5-year average P/E" column (using the average of five years' earnings) that is not available by default, and then sort and filter on *it*.

The syntax for a custom ratio uses simple arithmetic on the available metrics (Chapter 4 covers the operators; Chapter 10 goes deeper). This turns the table from "what the tool gives you" into "exactly what your strategy needs."

## Sorting discipline

A final note on sorting, because it is where the table is most abused:

- **Sorting finds extremes, not truths.** Sorting by P/E shows you the cheapest — and the cheapest are often cheap *for a reason* (a deteriorating business). Sorting by ROCE shows the most profitable — and the most profitable are often *expensive*.
- **The table answers "what?", not "why?".** It tells you *which* companies meet a criterion; it does not tell you *why* a company is cheap or profitable. That answer is on the company page (next chapters).

The table is for *finding candidates*; the company page is for *understanding them*. Keep the two jobs separate, and the tool works as intended.

## Summary

- The screener table is the whole market as a sortable spreadsheet.
- Click columns to sort; use "Edit columns" to build a table that *is* your strategy.
- Columns fall into families: size, valuation, profitability, leverage, growth, ownership.
- Custom ratios turn the table into exactly what your strategy needs.
- The table finds candidates ("what"); the company page explains them ("why").

Next: the query builder — the syntax and power of writing your own screens.
