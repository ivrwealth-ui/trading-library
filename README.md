# StratLab Trading Library

Free, open reference books on Indian (NSE) markets — options, momentum, swing trading, techno-funda investing, quant trading, risk management, chart types, and how to use TradingView and build a systematic trading framework. Built by [StratLab](https://stratlab.in).

Every book ships in three formats: a styled **PDF** to read, a styled **HTML** for the web, and clean, chapter-addressable **Markdown** with none of the other two formats' styling or markup — built specifically to be pasted or loaded into an LLM's context window (ChatGPT, Claude, Cursor, a local RAG pipeline, whatever you're using to help you design or backtest a strategy), not just to be read by a person. See [`llms.txt`](./llms.txt) for a machine-readable index of every book and chapter.

---

## ⚠️ Read this before anything else

**This is education, not advice.** StratLab is not registered with SEBI as an investment adviser, research analyst, or portfolio manager. Nothing here is a recommendation to buy or sell anything, and no strategy described is a promise of profit. Trading and investing involve real risk of loss, including total loss of capital. Every book carries its own full disclaimer in its opening pages — read it.

**This content is AI-drafted and human-reviewed — not exhaustively fact-checked.** Each book was generated with LLM assistance, then reviewed by StratLab for tone (no imperative "buy/sell" language, no invented certainty) and spot-checked for factual, citation, and arithmetic errors. That review already caught and fixed real mistakes (see **Editorial Notes** below) — which is exactly why we're telling you this instead of presenting it as flawless. It is **not** a guarantee that everything remaining is correct. Treat every specific number, formula, and worked example as illustrative until you've verified it yourself, and please report anything wrong — see **Found an error?** below.

---

## What's here

| Book | Chapters | Formats | Horizon |
|---|---|---|---|
| [The Complete Options Trader](./Options-Trading/) | 30 + 3 appendices | md · html · pdf | Foundations → advanced volatility strategies |
| [Momentum Trading](./Momentum-Trading/) | 10 + appendix | md · html · pdf | Weeks to a few months |
| [Momentum Investing](./Momentum-Investing/) | 10 + appendix | md · html · pdf | Months to years |
| [Swing Trading](./Swing-Trading/) | 10 + appendix | md · html · pdf | Days to a few weeks |
| [Techno-Funda](./Techno-Funda/) | 10 + appendix | md · html · pdf | Fuses fundamental screens with technical timing |
| [Risk Management and Position Sizing](./Risk-Management/) | 9 + appendix | md · html · pdf | Sizing, stops, drawdown, and ruin math — applies across every other book |
| [Quant Trading: Strategies and Ideas](./Quant-Trading/) | 10 + appendix | md · html · pdf | Systematic strategies, backtesting pitfalls, backtest-to-live |
| [How to Build a Framework for Systematic Trading](./Systematic-Trading-Framework/) | 10 + appendix | md · html · pdf | The end-to-end process, not a single strategy |
| [Charts and Chart Types](./Charts-and-Chart-Types/) | 11 + appendix | md · html · pdf | Line to Renko, P&F, Kagi, and the log scale — what each chart shows and hides |
| [TradingView Masterclass](./TradingView-Masterclass/) | 10 + appendix | md · html · pdf | Workspace, templates, alerts, bar replay, and the platform's actual workflow |

Each book's folder also has a `chapters/` directory with every chapter as its own file — useful if you only want to load one chapter (say, just the Greeks, or just RSI-2 mean reversion) into a model's context instead of the whole book.

## Why Markdown, why this matters

Most trading education online is written to be read by a human, on a web page, wrapped in ads, scripts, and paywalls — which makes it slow and messy to extract if you actually want to *use* it as reference material for something you're building. These books ship as flat Markdown specifically so that doesn't matter: drop a chapter straight into your AI tool of choice and ask it to explain a concept, quiz you on it, or ground a strategy or backtest in the actual text — instead of whatever the model half-remembers from its training data.

## License

The text of these books is licensed under **[CC BY 4.0](./LICENSE.md)** — free to read, share, adapt, translate, or build on (including commercially), as long as you credit StratLab. Fork it, fine-tune on it, embed it in your own tool — just say where it came from.

## Editorial notes (fixes made during review)

Being transparent about mistakes we've already caught is part of the point of saying this content is AI-drafted:

- **2026-09-13** — *Swing Trading*, Chapter 4 worked example stated a "~3:1 reward-to-risk" that didn't match its own numbers (₹15 reward against ₹17 risk is ≈0.9:1). Corrected to the accurate ratio, with an added note on why real pullback trades often do better than the nearest target suggests.
- **2026-09-13** — *Momentum Investing*, Chapter 9 stated a specific LTCG exemption figure that changes across budgets and may already be out of date. Removed the specific number in favour of a direct instruction to check the current Income Tax Act figure.
- **2026-09-13** — *The Complete Options Trader*, Chapter 21 described a strangle's required move as "350 points beyond the strikes," which wasn't accurate (each strangle breakeven sits only 150 points — its own premium — beyond the nearer strike; 350 is the move needed from spot). Reworded for precision; the number itself was always correct, only the description of what it measured was off.
- **2026-09-14** — *Risk Management and Position Sizing*, Chapter 2 stated a 50%-drawdown recovery time of "~3.5 years" at a 20% annual return; solving it properly (`1.2^t = 2.0`) gives **~3.8 years**. Corrected.
- **2026-09-14** — *TradingView Masterclass* stated specific keyboard shortcuts ("Space" for symbol search, "Alt+T"/"Alt+L" for panel toggles) that don't match TradingView's own current documentation, which we checked directly rather than trust from memory. Corrected the symbol-search claim to the behaviour that's actually reliable ("just start typing"), and replaced the two contested panel-toggle shortcuts with a pointer to the platform's own live shortcut reference, since TradingView changes these across versions and independent sources disagreed on the current bindings.

All four original books have been read in full and checked for arithmetic (breakevens, payoffs, position sizing, reward-to-risk), formula correctness (Greeks, Black-Scholes, IV rank/percentile), and citation accuracy against known sources (Jegadeesh & Titman 1993, George & Hwang 2004, Moskowitz/Ooi/Pedersen 2012, Antonacci 2014, Connors & Alvarez). *Techno-Funda*, *Risk Management*, *Quant Trading*, *Systematic Trading Framework*, *Charts and Chart Types*, and *TradingView Masterclass* have since had the same full read-and-check pass — recovery-table arithmetic, Kelly-criterion algebra, Sharpe/Sortino/profit-factor/expectancy formulas, pairs-trading z-score logic, and real charting-methodology conventions (Heikin-Ashi's averaging formula, Renko/P&F reversal rules, P&F's price-target formula) all checked out, with only the two fixes above. That review found and fixed the five issues logged here and nothing else that failed a check — which is a statement about what was checked, not a guarantee nothing was missed.

## Found an error?

Please open an [Issue](../../issues) — a wrong formula, an outdated number, a citation that doesn't check out, anything. This library gets more trustworthy the more people who use it also help verify it, which is the actual reason it's open source and not just a PDF on a landing page.

## About StratLab

[stratlab.in](https://stratlab.in) — market intelligence tools for Indian equity markets (Nifty/BankNifty). These books are the theory; the platform is where you'd see the same ideas computed against live data.
