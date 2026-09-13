# 9. Risk Management and Governance

## The layer that keeps the system alive

A systematic framework is a machine, and machines need **governance** — rules about the rules. This chapter covers the risk and governance layer: the discipline that protects the system from its two greatest enemies — **its own over-betting** and **its own operator.**

## Risk management: wired into the rules

Risk management is not a separate step; it is **baked into the framework** at every layer (and explored in depth in the Risk Management book). In the framework's terms, risk shows up as:

- **Per-trade risk** — the 1–2% rule, with size derived from the stop (Chapter 6).
- **Portfolio risk** — the cap on total at-risk and total exposure, and diversification across drivers.
- **Leverage/margin discipline** — risk computed on notional, a margin buffer, and a preference for defined-risk structures.
- **Tail risk** — sizing for the gap, avoiding oversized positions through binary events, capping aggregate short-vol exposure.

The framework's contribution is to make these **rules, not intentions** — written down, checked every rebalance, and impossible to override in the heat of the moment.

## Governance: rules about the rules

Governance answers a different question: **who decides when to change the system, and under what conditions?** Without governance, the operator *is* the system's weakest link — they will tweak it mid-drawdown, abandon it at the bottom, and over-bet it when it is working.

Three governance rules matter most:

### 1. The pre-commitment rule

Decide — *in advance* — the conditions under which you will change or stop the system. For example:

- "If the drawdown exceeds X, I reduce size by half."
- "If live diverges from backtest by Y% for Z months, I stop and investigate."
- "Parameter changes happen only at a scheduled quarterly review, never mid-trade."

The point of pre-commitment is that these decisions are made in a **calm state**, before the drawdown or the euphoria arrives — because in the emotional state, the decision will be wrong.

### 2. The no-override rule

The system's outputs are followed **unless** a pre-committed condition (above) triggers. "I overrode it because it felt wrong" is the death of systematic trading — it is the moment the framework stops being systematic. Overrides are allowed only through the governance process, never in the moment.

### 3. The separation of roles

Where possible, separate the roles that conflict:

- The person who **generates** the signal should not be the one who **decides whether to follow it**.
- The person who **writes** the backtest should not be the only one who **reviews** it.

Even for a solo trader, *writing the rules down and treating them as binding* creates a crude separation between "designer me" (calm) and "operator me" (emotional) — which is the point.

## The governance document

Governance lives in a written **governance document** — a short set of rules covering:

- **Change control** — when and how the system's rules may be changed.
- **Drawdown policy** — what happens at each drawdown level.
- **Stop conditions** — the kill switch (Chapter 8).
- **Review cadence** — how often the system is reviewed, and against what.

A system with a governance document is a *system*. Without one, it is a discretionary trader who occasionally uses a spreadsheet.

## The honest bottom line

The framework's entire risk-and-governance apparatus exists for one reason: **to keep the operator from destroying the system.** The market will not destroy a well-sized, well-governed system quickly; the operator will — by over-betting in euphoria, abandoning in drawdown, or tweaking in panic. Governance is the firewall between the system and its own creator.

## Summary

- Risk is baked into every layer as *rules*, not intentions.
- Governance is rules about the rules: who changes the system, and when.
- Pre-commit, no-override, and separation of roles are the three key governance rules.
- A written governance document is what makes a system a *system*.
- The framework's biggest risk is its own operator; governance is the firewall.

Next: the final chapter — a working framework template.
