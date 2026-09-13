# Appendix — Sizing Formulas

## The core formulas, in one place

### The foundation

**Risk = (Entry − Stop) × Position size**

**Position size = (Account equity × Risk%) ÷ (Entry − Stop)**

### The recovery table

| Loss | Gain needed to recover |
|------|------------------------|
| 5% | 5.3% |
| 10% | 11.1% |
| 20% | 25% |
| 30% | 42.9% |
| 50% | 100% |
| 70% | 233% |
| 90% | 900% |

### The sizing methods

| Method | Formula / rule |
|--------|----------------|
| Fixed fraction | size = (Equity × Risk%) ÷ (Entry − Stop) |
| Fixed ratio | grow size by a fixed unit per fixed profit increment |
| Volatility (ATR) | size = (Equity × Risk%) ÷ (k × ATR) |
| Kelly | f = (p·W − q·L) / W |
| Fractional Kelly | size at half- or quarter-Kelly |

### Risk of ruin intuition

Risk of ruin rises steeply with position size, regardless of edge. Fixed-fraction sizing at 1–2% keeps the worst realistic losing streak survivable.

### The load-bearing rules (memorise these)

1. **Risk 1–2% per trade.** Compute it on notional (not cash outlay), from the stop distance.
2. **Set the stop at entry, at the invalidation level, and never move it.**
3. **Size by the tail, not the win rate** — the high-win-rate families carry the sharpest tails.
4. **Cap total open risk and per-driver exposure** — ten correlated positions are one bet.
5. **Keep a margin buffer** — a volatility spike must not force an involuntary exit.
6. **Protect against deep drawdowns** — a 50% loss needs a 100% gain to recover.
