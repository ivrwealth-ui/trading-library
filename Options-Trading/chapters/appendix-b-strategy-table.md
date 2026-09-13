# Appendix B. Strategy Quick-Reference Table

All figures are at-expiry, per unit, before costs. "Width" = difference between the two strikes of a spread. C/P denote call/put premiums paid or received.

| Strategy | Structure | View | Max profit | Max loss | Breakeven(s) |
|----------|-----------|------|-----------|----------|--------------|
| Long call | Buy call @ K | Bullish | Unlimited | C | K + C |
| Long put | Buy put @ K | Bearish | K − P | P | K − P |
| Short call (naked) | Sell call @ K | Bearish/neutral | C | Unlimited | K + C |
| Short put (naked) | Sell put @ K | Bullish/neutral | P | K − P | K − P |
| Covered call | Long asset + short call @ K | Mildly bullish | (K − entry) + C | Asset downside − C | Entry − C |
| Cash-secured put | Cash + short put @ K | Mildly bullish | P | (K − 0) − P | K − P |
| Bull call spread | Buy call K₁, sell call K₂ | Moderately bullish | (K₂ − K₁) − debit | Debit | K₁ + debit |
| Bear put spread | Buy put K₂, sell put K₁ | Moderately bearish | (K₂ − K₁) − debit | Debit | K₂ − debit |
| Bull put spread | Sell put K₂, buy put K₁ | Mildly bullish | Credit | Width − credit | K₂ − credit |
| Bear call spread | Sell call K₁, buy call K₂ | Mildly bearish | Credit | Width − credit | K₁ + credit |
| Long straddle | Buy call + put @ K | Big move | Unlimited | C + P | K ± (C + P) |
| Long strangle | Buy OTM call K₂ + OTM put K₁ | Big move | Unlimited | C + P | K₁ − (C+P), K₂ + (C+P) |
| Short straddle | Sell call + put @ K | Stillness | C + P | Unlimited | K ± (C + P) |
| Short strangle | Sell OTM call K₂ + OTM put K₁ | Stillness | C + P | Unlimited | K₁ − (C+P), K₂ + (C+P) |
| Iron condor | Bull put spread + bear call spread | Range | Net credit | Width − credit | K₁ − credit, K₃ + credit |
| Long butterfly | Buy K₀, sell 2×K₁, buy K₂ | Pin | Width − debit | Debit | K₀ + debit, K₂ − debit |
| Protective put | Long asset + long put @ K | Hedged | Unlimited | (Entry − K) + P | Entry − P |
| Collar | Long asset + long put K₁ + short call K₂ | Hedged, capped | (K₂ − entry) ± net | (Entry − K₁) ∓ net | (varies) |
| Calendar spread | Sell near option, buy far option @ K | Consolidate | (at expiry) | Debit | Near K |
| Ratio spread | Buy 1, sell >1 (different strikes) | Zone, then flat | At short strike | Naked tail | (varies) |

## Direction, vol, and time at a glance

| Character | Strategies |
|-----------|-----------|
| Long delta (bullish) | Long call, bull call spread, bull put spread, short put, covered call |
| Short delta (bearish) | Long put, bear put spread, bear call spread, short call |
| Long vega / long gamma (likes vol & movement) | Long call/put, straddle, strangle, calendar, debit spreads |
| Short vega / short gamma (likes calm & decay) | Short call/put, covered call, cash-secured put, straddle/strangle (short), condors, credit spreads |

## A rule of thumb for choosing

- **Expect a move, want defined risk + leverage** → long option or debit spread.
- **Expect calm / range, want income** → credit spread or iron condor (defined-risk) before any naked short.
- **Expect a big move, unsure of direction, vol is cheap** → long straddle/strangle.
- **Own an asset, want a floor (or a capped, cost-neutral one)** → protective put (or collar).
