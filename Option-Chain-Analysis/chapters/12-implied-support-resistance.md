# 12. Option-Implied Support and Resistance

## Where the market's own positioning says price will be held

Traditional support and resistance are drawn by hand (*Charts and Chart Types*, in this series). The option chain offers a *quantitative* alternative: **support and resistance levels derived from the market's own option positioning** — the strikes where capital is concentrated, and where the market's behaviour is most likely to change. This chapter builds that model.

## The three sources of option-implied levels

The chain provides three distinct, quantitative sources of levels:

### 1. OI walls

From Chapter 2: strikes with unusually heavy open interest. A **call OI wall above spot** is where many call writers are positioned (profiting if price stays below) — read as **resistance**. A **put OI wall below spot** is where put writers sit — read as **support**. The heaviest walls are the levels the market is most "defending".

### 2. Gamma walls and the flip level

From Chapter 8: the strikes where **gamma** concentrates, and where **GEX flips sign**. A large *positive-gamma* wall acts as a **magnet** (dealer hedging pins price near it); the **flip level** is where behaviour changes from dampened to amplified — a level where a break can accelerate. These are *dynamic* levels, computed from the Greeks rather than from OI alone.

### 3. The implied distribution's kinks

From Chapter 9: the **bumps and kinks** in the implied probability distribution — the strikes where option demand is unusual. A bump at a particular level is the market's fingerprint of a *specific* level it is watching (a psychological round number, a prior high/low, an expected event level).

## How to use option-implied levels

The power of these levels is that they are **objective and self-updating** — computed from the chain, they do not depend on where an analyst *chooses* to draw a line:

1. **Read the levels before the market reaches them.** The OI walls, gamma walls, and distribution kinks tell you *in advance* where the market is likely to be held, drawn, or accelerated.
2. **Treat them as zones, not points** (the same discipline as hand-drawn levels). A wall at 25,000 is really the "24,950–25,050 zone."
3. **Combine the sources.** A strike that is *simultaneously* a heavy OI wall, a positive-gamma wall, and a distribution kink is a *much* stronger level than any one of those alone — the three sources are *confirming* each other.
4. **Watch for their *break*.** An option-implied level that *breaks* is especially meaningful, because it means the positioning that was defending it has been overwhelmed — often the start of an accelerated move (the GEX-negative dynamic of Chapter 8).

## Option-implied vs. hand-drawn: the complement

The two approaches are complementary, not competing:

- **Hand-drawn levels** (charts) capture *historical* price structure — prior highs/lows, trendlines, chart patterns. They are *where price has turned before*.
- **Option-implied levels** capture *forward-looking* positioning — where capital is committed *now*, and where dealer hedging will act. They are *where the market expects price to be held*.

The strongest levels are the ones where the two **agree**: a prior chart resistance that is *also* a heavy call wall, a prior support that is *also* a put wall and a gamma magnet. When chart structure and option positioning coincide, the level is at its most meaningful.

## The honest caveats

1. **Walls break.** An OI wall is a *tendency*, not a guarantee — and it is most reliable in calm, range-bound expiries, and least reliable in strongly trending markets (the same caveat as max pain, Chapter 5).
2. **Levels expire.** Option-implied levels are tied to the *expiry* they come from. A wall in the current weekly expiry ceases to matter when that expiry passes; the *monthly* expiry's levels are the more persistent ones.
3. **The sign assumptions apply.** Gamma-based levels inherit the dealer-short assumption (Chapter 6, Rule 4).

## Summary

- Three quantitative level sources: OI walls (writers' stakes), gamma walls + the GEX flip, and the implied distribution's kinks.
- Option-implied levels are objective and self-updating — computed, not drawn.
- Combine sources; a multi-confirmed level is the strongest; a broken one often accelerates.
- They complement hand-drawn levels — strongest when chart structure and option positioning agree.
- Walls break, and levels expire with their expiry.

Next: combining the signals into a composite model.
