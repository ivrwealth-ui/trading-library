# Screener.in Masterclass: The Complete Guide to India's Fundamental Research Tool

## A full walkthrough of Screener.in's structure and features — the screener table, the query builder, the company page, ratios, shareholding, peers, and custom screens — with an education-only disclaimer.

---

**Published by StratLab**

---

## Important Disclaimer

This book is provided for **educational purposes only**. It is not investment advice, a recommendation, or a solicitation to buy or sell any security.

- **StratLab is not registered with SEBI** as an investment adviser, research analyst, or portfolio manager, and does not provide investment advisory services.
- Investing involves risk of loss, including the possible loss of principal. Past performance never guarantees future results.
- All examples, figures, and screen criteria are illustrative. A screen is a *filter*, not a recommendation — every result must be independently analysed before any decision.
- **Screener.in is a third-party website operated by Mittal Analytics Private Limited. This book is not affiliated with, endorsed by, or sponsored by Screener.in.** Its features, interface, subscription tiers, and data may change at any time; verify current behaviour on the site.
- Nothing in this book should be read as a promise of return or a guarantee that any screen will identify profitable investments.

By reading this book, you agree that you are solely responsible for your own investment decisions and that you will consult a SEBI-registered adviser where appropriate.

---

## How to Read This Book

This book is a **masterclass on Screener.in**, one of the most widely used fundamental-research tools for Indian equities. It explains the tool's *structure* (how the pieces fit together) and its *features* (what each piece lets you do), and it teaches you to use the whole thing systematically.

- **Chapters 1–2** orient you: what Screener.in is, and how its main areas are organised.
- **Chapters 3–4** cover the two core workflows — the **screener table** and the **query builder** — which is where most of the tool's power lives.
- **Chapters 5–8** walk the **company page** end to end: the financials, the ratios, the shareholding pattern, the peer comparison, and the long-term growth and valuation view.
- **Chapters 9–10** turn it into a repeatable process: building your own techno-funda screens, custom ratios, and exporting for deeper analysis.
- The **appendix** is a query-syntax reference and a set of example screens.

A note on language: this book describes what the tool *shows* and how to use it — never what you "should" buy. Screens shortlist; you decide.

---

## Table of Contents

1. What Is Screener.in?
2. Navigating the Structure
3. The Screener Table and Columns
4. The Query Builder: Syntax and Power
5. The Company Page: Overview and Financials
6. Ratios and How to Read Them
7. Shareholding Pattern, Pledge, and Peers
8. Growth, Valuation, and the Long-Term View
9. Building Your Own Techno-Funda Screens
10. Custom Ratios, Export, and Advanced Tips

Appendix — Query Reference and Example Screens

---


# 1. What Is Screener.in?

## India's fundamental-research workbench

**Screener.in** is a free (with paid upgrades) website that provides **financial data on listed Indian companies**, designed to answer one question efficiently: *"is this a good business, and what is it worth?"* It is, for the Indian retail investor, the closest thing to a professional research terminal for *fundamentals*.

It matters for a simple reason: **fundamental research is data work, and Screener.in organises that data** so you do not have to dig through exchange filings and annual reports one company at a time.

## What it gives you

Screener.in's value can be summarised in five capabilities:

1. **Screening** — filter the entire listed universe by financial criteria (market cap, P/E, ROE, growth, debt, and hundreds more) to produce a shortlist in seconds.
2. **Company pages** — for any listed company, a complete, organised view of its financials: profit & loss, balance sheet, cash flow, ratios, quarterly results, shareholding pattern, and peers — for **a decade or more** of annual history, all in one place.
3. **Query language** — a simple but powerful way to write *your own* screens (e.g., "companies with ROCE > 15% and debt-to-equity < 0.5"), and to build *custom ratios*.
4. **Peer comparison** — side-by-side comparison of a company against its industry competitors.
5. **Export** — download the data to Excel/CSV to build your own models (DCF, projections, custom analysis).

The whole tool is built around a single insight: **most of fundamental analysis is *filtering* — and filtering is what a screen does better and faster than a human can.**

## The two fundamental workflows

Everything in Screener.in reduces to one of two movements:

1. **Top-down (screening):** start from the *whole market*, and use the screener/query builder to *narrow it down* to a shortlist of candidates. You go from thousands of companies to a handful that meet your criteria.
2. **Bottom-up (company page):** start from a *single company*, and use its page to *deep-dive* into its financials, ratios, and peers. You go from "what is this company?" to a complete, organised picture.

The master uses both: screen to *find* candidates, then the company page to *vet* each one. This book teaches both movements, in that order.

## What Screener.in is not

Three honest boundaries, so you use it correctly:

1. **It is a data tool, not an adviser.** It presents financial data; it does not tell you what to buy, and its machine-generated observations ("Pros" and "Cons") are *summaries of the data*, not recommendations.
2. **It is fundamentally oriented.** Screener.in's strength is *fundamentals* (financial statements, ratios, shareholding). Its charts are basic; if you want deep technical analysis, that is a different tool (and a different book in this series).
3. **Data has limits.** Financial data is *historical* and *reported* — it can be restated, delayed, or (for some companies) incomplete. The tool shows you the data; it does not guarantee the data is the whole truth.

## Summary

- Screener.in organises fundamental data for listed Indian companies, a decade or more deep.
- Five capabilities: screening, company pages, query language, peer comparison, export.
- Two workflows: top-down (screen to find) and bottom-up (company page to vet).
- It is a data tool, fundamentally oriented — not an adviser.

Next: navigating the structure — how the tool's pieces fit together.


# 2. Navigating the Structure

## The map before the journey

Screener.in is simple enough that most people *skip* learning its structure and never discover half of what it can do. This chapter is the map: the four main areas, what each is for, and how they connect.

## The four main areas

1. **Home / search** — the search bar where you look up a company by name or ticker.
2. **Screens** — the screening area, including the **query builder** ("Create a stock screen") and saved screens.
3. **Company pages** — the deep-dive page for a single company (the biggest and most important area).
4. **Watchlists / saved screens** — your personal lists of companies and queries (requires a free account).

The mental model: **search finds a company; screens find a shortlist; the company page analyses one company; watchlists hold what you are tracking.**

## Home / search

The homepage is a single search box. Type a company name or ticker (e.g., "Asian Paints" or "RELIANCE") and it drops you onto that company's page. This is the *bottom-up* entry point: you already know *which* company, and you want its full picture.

Below the search, the homepage also surfaces popular pre-made screens and your saved screens — a quick entry into the *top-down* workflow.

## Screens (the screening area)

This is where the *top-down* workflow lives. It has two parts:

1. **Pre-made screens** — thousands of ready-made screens created by other users (and Screener.in itself), categorised by style (high ROE, low debt, small-cap, etc.). You can *run* any of them, and *modify* them to suit yourself.
2. **Create a stock screen (the query builder)** — a text box where you write your *own* query. This is the tool's most powerful feature, and the subject of Chapter 4.

The screening area produces a **table of companies** (the "screener table", Chapter 3) matching your criteria, which you can sort, filter, and export.

## The company page

The company page is the heart of the tool — a long, organised page for a single company, with these sections (roughly top to bottom):

- **Summary numbers** — price, market cap, high/low, P/E, book value, dividend yield, ROCE, ROE — the "first impression" row, next to a short **About** note and curated **Key Points** on the business.
- **Charts** — price and ratio charts over time.
- **Pros and Cons** — machine-generated observations about the company's finances (e.g., "Company has been maintaining a healthy dividend payout").
- **Peer Comparison** — the company side-by-side with its industry peers.
- **Financial statements** — **Quarterly Results**, Profit & Loss, Balance Sheet, and Cash Flow; the annual statements carry a decade or more of history, the quarterly results about three years.
- **Ratios** — dozens of computed ratios (ROCE, ROE, growth, leverage, valuation), with trends.
- **Shareholding Pattern** — promoter, FII, DII, public holdings, plus promoter pledge.
- **Documents** — announcements, filings, and regulatory documents.

The company page is covered in depth across Chapters 5–8.

## Watchlists and saved screens

With a free account, you can:

- **Save screens** — so a query you like can be re-run in one click, and you can set **email alerts** when a new company enters the screen (at the time of writing the free plan allows two screen alerts; more need a paid plan).
- **Build watchlists** — to track a set of companies you are researching.

These are the "personal memory" of the tool — they make your research *repeatable*.

## How the areas connect

The master's loop connects all four:

1. **Screen** (top-down) → get a shortlist.
2. **Open each company page** (bottom-up) → vet each candidate's financials, ratios, and peers.
3. **Add the survivors to a watchlist** → track them.
4. **Re-run the saved screen periodically** → keep the shortlist fresh.

Everything else in this book is detail on top of that loop.

## Summary

- Four areas: search, screens (with query builder), company pages, and watchlists/saved screens.
- Search = find one company; screens = find a shortlist; company page = analyse one; watchlists = track.
- The company page is the heart: summary, Pros and Cons, peers, financials, ratios, shareholding, documents.
- The loop: screen → vet → watchlist → re-screen.

Next: the screener table and its columns.


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


# 5. The Company Page: Overview and Financials

## The deep-dive

The **company page** is where the tool earns its place as a research workbench rather than a data dump. For any single company, it presents — in a clean, organised layout — everything you need to understand the business financially. This chapter covers the top half: the **overview**, the **Pros and Cons**, and the **three financial statements**.

## The overview (summary numbers)

At the top of the page is a row of headline numbers — the "first impression":

- **Current price**, **market cap**, **high/low** (52-week range), **book value**, **P/E**, **dividend yield**, **ROCE**, **ROE**.

These are deliberately *summary* figures: none should be read in isolation, but together they give you a ten-second feel for the company — is it profitable (ROCE/ROE), cheap (P/E, book value), income-yielding (dividend yield), and at what scale (market cap)?

## Pros and Cons

Just below the price chart is a section of **Pros and Cons** — a list of observations machine-generated from the financial data. (The separate **Key Points** beside the summary numbers are curated notes on the business itself.) Examples of the kind of thing the Pros and Cons surface:

- "Company has been maintaining a healthy dividend payout."
- "Company has consistently increased its sales over the last 5 years."
- "Company has a high debt-to-equity ratio."

The Pros and Cons are valuable because they *direct your attention*: they flag the patterns in the data (good and bad) that a human would otherwise have to dig for. But they are a *summary of the data*, not an opinion — treat it as a pointer to "look here", and verify each point against the underlying numbers yourself.

## The three financial statements

The core of the page is the three statements, each with **a decade or more** of history in a clean table:

### 1. Profit & Loss (Income Statement)

The *performance* story: **sales**, **expenses**, **operating profit**, **net profit**, and the resulting **margins**. What to look for:

- **Sales trend** — is the top line growing, and steadily?
- **Margins** — are operating and net margins stable, rising (pricing power), or shrinking (competition)?
- **Profit trend** — is profit growing *with* sales, or is growth coming at the cost of profitability?

### 2. Balance Sheet

The *financial health* story: **assets**, **liabilities**, **equity**, and — critically — **debt** and **reserves**. What to look for:

- **Debt level and trend** — is leverage low and stable, or rising?
- **Reserves/equity growth** — is the company *retaining and compounding* profits (a rising equity base), or eroding it?
- **Asset quality** — current assets vs. current liabilities (can it meet short-term obligations?).

### 3. Cash Flow

The *truth test*: **operating**, **investing**, and **financing cash flows**. Cash flow is the part that catches the companies whose profits are on paper but not in the bank:

- **Operating cash flow** — is the company actually *generating* cash from operations (the most important line: a company whose profits exceed its operating cash flow deserves suspicion)?
- **Free cash flow** — operating cash flow minus capital expenditure: the cash genuinely left over for shareholders.

The master's rule: **profit is an opinion; cash is a fact.** Always cross-check the P&L's "profit" against the cash flow statement's "operating cash flow".

## Reading the trend, not the year

The single most important habit on the company page: **read the trend across years, not any single year.** A single year's numbers are noisy (an exceptional order, a one-off cost, a tax change). The *direction and consistency* over 5–10 years is what reveals the character of the business — and the long history is exactly what Screener.in gives you that a casual glance at "this quarter's results" cannot.

## Summary

- The overview gives a ten-second feel (price, cap, P/E, ROCE, ROE, yield).
- Pros and Cons auto-flag patterns — pointers to "look here", not opinions.
- P&L = performance (sales, margins, profit trend); Balance Sheet = health (debt, equity, assets); Cash Flow = truth (operating cash flow is the cross-check).
- Read the multi-year trend, not any single year.

Next: the ratios — and how to actually read them.


# 6. Ratios and How to Read Them

## The numbers that summarise a business

The company page's **Ratios** section condenses years of financial data into the handful of numbers that actually characterise a business. This chapter teaches the most important ratios — what each *measures*, and, critically, how to read them *together* (a ratio in isolation is misleading).

## Profitability: how good is the business?

### ROCE (Return on Capital Employed)

ROCE = EBIT (profit before interest and tax) ÷ total capital employed (equity + debt). It answers: *how efficiently does this business convert its capital into profit?*

- **High and sustained ROCE (as a rule of thumb, >15–20% over many years)** is the hallmark of a *quality* business — one with a genuine competitive advantage that lets it earn high returns on its capital, year after year.
- **Low or falling ROCE** means the business is capital-hungry or competitive-advantage-less.

The key word is **sustained**: a single year's high ROCE can be luck; ten years of it is a moat. This is why the `Average … 5Years` form matters.

### ROE (Return on Equity)

ROE = net profit ÷ shareholder equity. It answers: *how much profit is generated for the shareholders' capital?*

- **High ROE** is good — but with one critical caveat (below).
- The **DuPont insight**: ROE = (margin) × (asset turnover) × (leverage). A high ROE can come from genuine profitability *or* from high leverage (debt). **Always read ROE next to debt-to-equity** — a 25% ROE with 3× debt is a leveraged bet, not a quality business; a 20% ROE with no debt is the real thing.

## Leverage: how safe is the balance sheet?

### Debt to Equity

Debt-to-equity = total debt ÷ shareholder equity. It answers: *how much of the business is financed by borrowing?*

- **Low (rule of thumb: <0.5, ideally 0)** means the business is financed by its own capital — it can survive downturns.
- **High** means the business carries the risk of interest obligations and refinancing — a danger in a downturn.

The rule of thumb: **a good business with low debt is a completely different investment from a good business with high debt.** Never judge profitability without checking leverage.

### Interest Coverage

Interest coverage = EBIT (profit before interest and tax) ÷ interest expense. It answers: *can the company comfortably pay its interest?* As a rule of thumb, a coverage ratio comfortably above 2–3× is safe; below 1.5× is a warning that a downturn in profit could make the debt unserviceable.

## Valuation: is the price reasonable?

### P/E (Price to Earnings)

P/E = price ÷ earnings per share. It answers: *how many years of earnings am I paying for?*

- **Low P/E** can mean "cheap" — or "the market expects earnings to fall". It is a *comparison* number, not an absolute one: compare against the company's own history and against peers, never in isolation.
- **High P/E** means the market is paying up for expected growth — which may or may not arrive.

### P/B (Price to Book)

P/B = price ÷ book value per share. It answers: *how much am I paying for the net assets?* Useful for asset-heavy businesses (banks, capital-intensive industries), less meaningful for asset-light ones.

### PEG (P/E to Growth)

PEG = P/E ÷ earnings growth rate. It attempts to answer: *is the price justified by the growth?* A PEG near or below 1 is often considered "reasonable value for the growth" — a rough, but useful, tie-breaker between a cheap-but-stagnant company and an expensive-but-fast-growing one.

### Dividend Yield

Dividend yield = annual dividend per share ÷ price. It answers: *what income does this pay me?* High yield is attractive — *if* the dividend is sustainable (check the payout ratio: the dividend should be comfortably covered by earnings, not paid out of debt).

## Reading ratios together: the master's sequence

The single most important lesson of this chapter: **ratios are never read alone; they are read as a *sequence* that tells a consistent story.** The sequence that separates a good business from a risky one:

1. **ROCE/ROE (sustained, 5–10 years)** — is it genuinely profitable? → if low, stop; the story is "weak business".
2. **Debt-to-equity + interest coverage** — is the profitability *real* (unlevered) or *borrowed* (levered)? → a high ROE on high debt is a different, riskier story.
3. **Sales/profit growth** — is the business *compounding*, or stagnating?
4. **Valuation (P/E, P/B, PEG)** — is the market *already pricing in* all that quality? → a wonderful business at a silly price is a poor investment.

Read in this order, the ratios tell one coherent story: *a good business, genuinely profitable, growing, and reasonably priced.* Read out of order (or one at a time), they mislead.

## Summary

- Profitability: ROCE (efficiency) and ROE (return to shareholders) — but read ROE next to debt.
- Leverage: debt-to-equity and interest coverage — a good business on high debt is a different investment.
- Valuation: P/E, P/B, PEG, dividend yield — comparison numbers, never absolute.
- The master reads ratios in sequence: profitability → leverage → growth → valuation.

Next: shareholding pattern, promoter pledge, and peer comparison.


# 7. Shareholding Pattern, Pledge, and Peers

## The parts most people skip

The financial statements and ratios get all the attention; the **shareholding pattern**, **promoter pledge**, and **peer comparison** get almost none — and they are where some of the most important signals live. This chapter covers all three.

## The shareholding pattern

Every company page shows the **shareholding pattern**: who owns the company, broken into categories, with **about three years of quarterly history, and year-end figures going back further**:

- **Promoter holding** — the stake owned by the founders/promoters and their families.
- **FII** — foreign institutional investors.
- **DII** — domestic institutional investors (mutual funds, insurance).
- **Public** — everyone else.

The pattern matters for one reason: **the trend in ownership is a vote of confidence, in numbers.** Specifically:

- **Rising promoter holding** — the promoters are *buying their own company's stock* (often a signal of confidence; they know the business best).
- **Falling promoter holding** — the promoters are *selling* (a signal worth understanding; sometimes it is benign — pledging-related or personal — and sometimes it is not).
- **Rising FII/DII holding** — institutional money is accumulating (a vote of confidence from professional investors).
- **A shift in FII vs. DII** — e.g., DII buying while FII sells — is worth investigating: it tells you *which* professionals believe in the business.

The discipline: **read the trend over quarters, not any single quarter's number.** A one-quarter blip is noise; a multi-year direction is a signal.

## Promoter pledge: the red flag

The **pledged percentage** — how much of the promoter's holding has been *pledged* (used as collateral for a loan) — is a specific, important risk signal, and it is easy to miss.

- **What it means:** the promoters have borrowed money using their own shares as collateral.
- **Why it is dangerous:** if the stock falls sharply, the lenders can *sell those pledged shares* into the market to recover their loan — adding further downward pressure on the price, and potentially diluting/undermining the promoter's control.
- **The threshold worth attention (a rule of thumb, not a regulatory line):** pledge above roughly **50% of the promoter's holding** is a genuine risk flag. Below that, it is usually manageable; above it, the company's fate is partly in the hands of its lenders.

The rule: **check the pledge percentage on every company page** — it is one of the few *binary* risk signals the tool gives you for free.

## Peer comparison

Near the top of the page, just after the Pros and Cons, is a **peer comparison** table: the company side-by-side with its industry competitors, showing the same key metrics (revenue, profit, market cap, P/E, ROCE, operating margin) for each.

This table is where **a ratio stops being an abstract number and becomes a *contextual* judgement**:

- A company's **ROCE of 12%** is meaningless in isolation — but side-by-side with peers, you can see instantly whether it is *above* or *below* its industry, and by how much.
- A company's **P/E of 30** is "expensive" or "cheap" only *relative to its peers* (and its own history) — the peer table gives you that relative context in one glance.
- **Margins** compared to peers reveal *competitive position*: consistently higher margins than the industry suggests a moat; lower margins suggest a cost disadvantage.

The master's habit: **never judge a company's ratios in isolation — always put them next to the peers.** The peer table is what makes that possible without opening a second page.

## Putting it together

The shareholding pattern, the pledge, and the peers are the three "context" sections that turn the raw financials into a *judgement*:

1. **Financials + ratios** tell you *what* the business is (profitable, growing, safe?).
2. **Shareholding** tells you *who believes in it* (and whether the promoters are buying or selling).
3. **Pledge** tells you whether there is a *hidden risk* on the balance sheet of the promoters.
4. **Peers** tell you whether the business is *better or worse than its competition*.

All four together are a complete picture. Miss the last three, and you have judged a business in a vacuum.

## Summary

- Shareholding pattern: promoter/FII/DII/public, quarterly, multi-year — read the *trend* in ownership.
- Rising promoter holding and rising institutional holding are confidence signals.
- Promoter pledge above ~50% of holding is a genuine risk flag — check it every time.
- Peer comparison turns ratios into *relative* judgements — never judge a ratio in isolation.
- Financials = what; shareholding = who; pledge = hidden risk; peers = context.

Next: growth, valuation, and the long-term view.


# 8. Growth, Valuation, and the Long-Term View

## The two questions that decide an investment

Strip away the detail, and every fundamental decision reduces to two questions:

1. **Growth** — is the business *compounding*, and at what rate?
2. **Valuation** — is the *price* reasonable for that compounding?

This chapter covers how to read both on Screener.in, using its greatest asset: **the long-term view.**

## Growth: the engine

Growth is the driver of long-term returns, and Screener.in shows it clearly:

- **Sales growth** — the top line (with `3Years` and `5Years` forms for the trend).
- **Profit growth** — the bottom line (same multi-year forms).
- **EPS growth** — earnings per share, which is what ultimately matters per shareholder.

The discipline in reading growth:

1. **Look at the multi-year trend, not one year.** A 40% growth year followed by two flat years is different from a steady 15% a year. The `5Years` figures (and the charts) reveal the *consistency*, which matters more than the speed.
2. **Check profit growth against sales growth.** If sales grow 20% but profit grows only 5%, the growth is coming at the cost of margins — a warning that the growth is *low-quality* (buying market share by cutting prices).
3. **Cross-check against cash flow.** Growth in *reported* profit that does not show up in *operating cash flow* is growth on paper, not in reality (Chapter 5's rule: profit is an opinion, cash is a fact).

## Valuation: the price of the engine

A wonderful, fast-growing business can still be a poor investment if the market has already priced in a decade of growth. Valuation — the "what am I paying for this?" question — is the brake on enthusiasm:

- **P/E** — how many years of earnings you are paying for; compare against the company's *own* history (the ratio charts show the historical P/E range) and against peers.
- **P/B** — for asset-heavy businesses.
- **PEG** — P/E relative to growth, the tie-breaker between "expensive because fast-growing" and "expensive, period".

The honest principle: **valuation is a *filter*, not a *timing tool*.** It tells you whether the price is in a reasonable range; it does not tell you *when* to buy (a cheap stock can get cheaper; an expensive one can keep rising). Use valuation to *avoid overpaying*, and combine it with the technical timing tools elsewhere in this series for the *when*.

## The long-term view: the tool's superpower

What makes Screener.in genuinely powerful is that it shows **a decade or more of history for almost everything** — not just price, but sales, profit, margins, debt, and ratios, all on the same multi-year scale (shareholding runs about three years quarter by quarter, with year-end figures going back further). This long view is what separates a *judgement* from a *guess*:

- **Business cyclicality** — a 10-year chart of sales and profit reveals whether the business is steady or cyclical (and where in the cycle it is).
- **Margin trend** — a decade of margins shows whether the business's competitive position is *improving* or *deteriorating* — the single most important long-term question.
- **Compounding** — a decade of rising sales, profit, and equity *is* the signature of a compounding machine; a decade of flat or falling figures is the signature of a stagnant one.

The rule: **the longer the horizon you read, the clearer the character of the business.** Screener.in gives you the long horizon for free — the mistake is reading it with a short-term eye.

## The two-question test, made concrete

A master's pass over a company page reduces to checking, in order:

1. **Sales/profit growing over 5–10 years?** (compounding engine)
2. **Margins stable or rising?** (quality of growth)
3. **Operating cash flow ≈ profit?** (real, not paper, growth)
4. **P/E/PEG reasonable vs. history and peers?** (not overpaying)

Answer all four, and you have a genuine fundamental view — not just a collection of numbers.

## Summary

- Growth (sales/profit/EPS) is the engine; read the multi-year trend and cross-check profit vs. sales and cash flow.
- Valuation (P/E, P/B, PEG) is the brake; a filter against overpaying, not a timing tool.
- The decade-plus view reveals cyclicality, margin trend, and whether the business is truly compounding.
- The four-question test: growth, margins, cash flow, valuation.

Next: building your own techno-funda screens.


# 9. Building Your Own Techno-Funda Screens

## From criteria to a repeatable system

The whole point of Screener.in's query builder is to turn your *investment philosophy* into a *repeatable screen*. This chapter shows how — by building the "fundamental" half of a techno-funda strategy (the "what to own" filter), which you then combine with the "technical" half (the "when" — see the Techno-Funda and Charts books in this series).

## The principle: screen for the "what", time for the "when"

Techno-funda (from the companion book) separates two questions:

1. **What** to own — a good, growing, safe, reasonably priced business. → **This is what a Screener.in screen does.**
2. **When** to buy — the technical timing (trend, breakout, reversal). → **This is done on a chart, not in Screener.in.**

So your Screener.in screens are the **fundamental filter** — they produce the *universe of worth-owning businesses* — and your chart work decides *when* to act on them. Keep the two jobs separate, and each tool does what it is best at.

## Five example screens (by philosophy)

Each of the following is a complete, runnable query expressing a different fundamental philosophy. Adapt the thresholds to your own taste and the current market.

### 1. Quality screen (high-return, low-debt businesses)

```
Average return on capital employed 5Years > 15
AND Average return on equity 5Years > 15
AND Debt to equity < 0.5
```

The compounding machines: sustained high returns on capital, financed conservatively.

### 2. Growth screen (fast, consistent growers)

```
Sales growth 5Years > 15
AND Profit growth 5Years > 15
AND Debt to equity < 1
```

Companies compounding the top *and* bottom line — with a debt ceiling to avoid the growth-by-borrowing trap.

### 3. Value screen (cheap, still-profitable)

```
Price to earning < 15
AND Price to book value < 2
AND Return on equity > 10
```

Cheap — but with a profitability floor, to avoid the pure "value traps".

### 4. Income screen (reliable dividends)

```
Dividend yield > 3
AND Return on equity > 12
AND Debt to equity < 0.5
```

Yield that is *sustainable* (backed by profitability and a clean balance sheet), not a yield trap.

### 5. A full techno-funda screen (quality + growth + safety + ownership)

```
Market capitalization > 500
AND Average return on equity 5Years > 12
AND Sales growth 5Years > 10
AND Debt to equity < 1
AND Promoter holding > 30
AND Pledged percentage < 15
```

Quality, growth, safety, and management confidence — a five-way screen that produces a genuinely short list. (This is a *starting point*, not a recommendation.)

## The workflow that turns screens into decisions

1. **Run the screen** → get a shortlist.
2. **Open each company page** → run the four-question test (Chapter 8): growth, margins, cash flow, valuation.
3. **Check the shareholding and pledge** (Chapter 7) → confidence and hidden risk.
4. **Compare peers** → is it genuinely better than its competition?
5. **Move to the chart** → the technical "when" (trend, breakout) decides the actual timing.

The screen is step 1 — the *filter* — and steps 2–5 are where the *judgement* lives. The screen narrows thousands to dozens; the rest narrows dozens to the few you actually act on.

## The discipline

Three rules keep your screening honest:

1. **Write your criteria before you look.** Decide the screen *first* (from your philosophy), then run it — not the reverse (run many screens until you like what you see). The reverse is how screens become rationalisation.
2. **Keep criteria economically sensible, not data-mined.** A screen that only works on the last two years is overfit (the Systematic Trading Framework lesson). Simple, economically motivated criteria survive.
3. **Re-run on a schedule.** A saved screen is a *system*, not a one-off. Re-run it monthly or quarterly, and the shortlist stays fresh — the closest thing a fundamental investor gets to automation.

## Summary

- Screen for the "what"; chart for the "when" — keep the techno-funda halves separate.
- Five example screens: quality, growth, value, income, and a full techno-funda screen.
- The workflow: screen → company page → shareholding → peers → chart.
- Discipline: write criteria before looking, keep them sensible, re-run on a schedule.

Next: custom ratios, export, and advanced tips.


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
