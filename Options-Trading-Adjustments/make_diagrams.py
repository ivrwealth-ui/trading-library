#!/usr/bin/env python3
"""Generate payoff diagrams for the Options Adjustments book (illustrative Nifty-style strikes)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "diagrams")
os.makedirs(OUT, exist_ok=True)

TEAL = "#0f5c8c"
GREEN = "#1a7f4b"
RED = "#b3261e"
GREY = "#5a6472"

plt.rcParams.update({
    "font.size": 10,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
})


def call(S, K, prem, sign=+1):
    return sign * (np.maximum(S - K, 0) - prem)


def put(S, K, prem, sign=+1):
    return sign * (np.maximum(K - S, 0) - prem)


def annotate(ax, x, y, text, color=GREY, dy=0):
    ax.annotate(text, (x, y), xytext=(x, y + dy), color=color,
                ha="center", fontsize=9, arrowprops=dict(arrowstyle="-", color=color, lw=0.6))


def style(ax, xlabel="Underlying at expiry (points)", ylabel="P&L (points)"):
    ax.axhline(0, color="#cccccc", lw=0.8, zorder=0)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True, alpha=0.25, lw=0.4)


def save(fig, name):
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print("wrote", name)


# 1. Covered Call
def covered_call():
    S0, K, prem = 22000, 22300, 120
    S = np.linspace(21200, 23200, 500)
    pnl = (S - S0) + call(S, K, prem, sign=-1)
    fig, ax = plt.subplots(figsize=(8, 4.6))
    ax.plot(S, pnl, color=TEAL, lw=2)
    ax.fill_between(S, pnl, 0, where=(pnl > 0), color=GREEN, alpha=0.12)
    ax.fill_between(S, pnl, 0, where=(pnl <= 0), color=RED, alpha=0.12)
    be = S0 - prem
    ax.scatter([be], [0], color=GREY, zorder=5)
    annotate(ax, be, 0, f"Breakeven {be:,}", GREY, dy=60)
    annotate(ax, K, (K - S0) + prem, f"Max profit +{(K - S0) + prem:,}", GREEN, dy=50)
    ax.set_title("Covered Call — long stock @ 22,000 + short 22,300 call @ 120")
    ax.set_ylim(-900, 900)
    style(ax)
    save(fig, "covered_call.png")


# 2. Bull Call Spread
def bull_call_spread():
    K1, K2, p1, p2 = 22000, 22300, 250, 120
    debit = p1 - p2
    S = np.linspace(21600, 22800, 500)
    pnl = call(S, K1, p1) + call(S, K2, p2, sign=-1)
    fig, ax = plt.subplots(figsize=(8, 4.6))
    ax.plot(S, pnl, color=TEAL, lw=2)
    ax.fill_between(S, pnl, 0, where=(pnl > 0), color=GREEN, alpha=0.12)
    ax.fill_between(S, pnl, 0, where=(pnl <= 0), color=RED, alpha=0.12)
    be = K1 + debit
    mx = (K2 - K1) - debit
    ax.scatter([be], [0], color=GREY, zorder=5)
    annotate(ax, be, 0, f"Breakeven {be:,}", GREY, dy=45)
    annotate(ax, 22650, mx, f"Max profit +{mx:,}", GREEN, dy=-40)
    annotate(ax, 21800, -debit, f"Max loss -{debit:,}", RED, dy=-30)
    ax.set_title("Bull Call Spread — buy 22,000 call @ 250, sell 22,300 call @ 120")
    style(ax)
    save(fig, "bull_call_spread.png")


# 3. Iron Condor
def iron_condor():
    K1p, K2p, K1c, K2c = 21500, 21700, 22300, 22500
    pp1, pp2, pc1, pc2 = 35, 110, 120, 40
    # short 21,700 put @ 110, long 21,500 put @ 35; short 22,300 call @ 120, long 22,500 call @ 40
    credit = (pc1 - pc2) + (pp2 - pp1)  # 80 + 75 = 155
    width = K2c - K1c  # 200
    S = np.linspace(21000, 23000, 500)
    pnl = (call(S, K1c, pc1, -1) + call(S, K2c, pc2)
           + put(S, K2p, pp2, -1) + put(S, K1p, pp1))
    fig, ax = plt.subplots(figsize=(8, 4.6))
    ax.plot(S, pnl, color=TEAL, lw=2)
    ax.fill_between(S, pnl, 0, where=(pnl > 0), color=GREEN, alpha=0.12)
    ax.fill_between(S, pnl, 0, where=(pnl <= 0), color=RED, alpha=0.12)
    be_low = K2p - credit
    be_hi = K1c + credit
    ml = width - credit
    ax.scatter([be_low, be_hi], [0, 0], color=GREY, zorder=5)
    annotate(ax, be_low, 0, f"BE {be_low:,}", GREY, dy=45)
    annotate(ax, be_hi, 0, f"BE {be_hi:,}", GREY, dy=45)
    annotate(ax, 22000, credit, f"Max profit +{credit:,}", GREEN, dy=-30)
    annotate(ax, 21250, -ml, f"Max loss -{ml:,}", RED, dy=-30)
    ax.set_title("Iron Condor — short 21,700/22,300, long 21,500/22,500 (net credit 155)")
    style(ax)
    save(fig, "iron_condor.png")


# 4. Short Strangle
def short_strangle():
    Kp, Kc, pp, pc = 21700, 22300, 110, 120
    credit = pp + pc
    S = np.linspace(20800, 23400, 500)
    pnl = put(S, Kp, pp, -1) + call(S, Kc, pc, -1)
    fig, ax = plt.subplots(figsize=(8, 4.6))
    ax.plot(S, pnl, color=TEAL, lw=2)
    ax.fill_between(S, pnl, 0, where=(pnl > 0), color=GREEN, alpha=0.12)
    ax.fill_between(S, pnl, 0, where=(pnl <= 0), color=RED, alpha=0.12)
    be_low = Kp - credit
    be_hi = Kc + credit
    ax.scatter([be_low, be_hi], [0, 0], color=GREY, zorder=5)
    annotate(ax, be_low, 0, f"BE {be_low:,}", GREY, dy=50)
    annotate(ax, be_hi, 0, f"BE {be_hi:,}", GREY, dy=50)
    annotate(ax, 22000, credit, f"Max profit +{credit:,}", GREEN, dy=-80)
    annotate(ax, 21000, pnl[0] - 60, "Loss grows beyond BEs", RED, dy=-40)
    ax.set_title("Short Strangle — sell 21,700 put @ 110, sell 22,300 call @ 120 (credit 230)")
    style(ax)
    save(fig, "short_strangle.png")


# 5. Long Straddle
def long_straddle():
    K, pc, pp = 22000, 250, 240
    debit = pc + pp
    S = np.linspace(20800, 23200, 500)
    pnl = call(S, K, pc) + put(S, K, pp)
    fig, ax = plt.subplots(figsize=(8, 4.6))
    ax.plot(S, pnl, color=TEAL, lw=2)
    ax.fill_between(S, pnl, 0, where=(pnl > 0), color=GREEN, alpha=0.12)
    ax.fill_between(S, pnl, 0, where=(pnl <= 0), color=RED, alpha=0.12)
    be_low = K - debit
    be_hi = K + debit
    ax.scatter([be_low, be_hi], [0, 0], color=GREY, zorder=5)
    annotate(ax, be_low, 0, f"BE {be_low:,}", GREY, dy=50)
    annotate(ax, be_hi, 0, f"BE {be_hi:,}", GREY, dy=50)
    annotate(ax, K, -debit, f"Max loss -{debit:,}", RED, dy=-40)
    annotate(ax, 22950, 950, "Profit grows beyond BEs", GREEN, dy=40)
    ax.set_title("Long Straddle — buy 22,000 call @ 250 + 22,000 put @ 240 (debit 490)")
    style(ax)
    save(fig, "long_straddle.png")


# 6. Iron Condor adjustment: roll up the untested put side
def iron_condor_adjust():
    # Original: shorts 21700p / 22300c, wings 21500/22500, credit 155
    S = np.linspace(21000, 23000, 500)
    orig = (call(S, 22300, 120, -1) + call(S, 22500, 40)
            + put(S, 21700, 110, -1) + put(S, 21500, 35))
    # Adjusted after a rally toward the call side: buy back the 21,700/21,500 put spread
    # for 25 (locks in 75 - 25 = 50), sell a new 21,900/21,700 put credit spread for 40
    # (short 21,900 put @ 75, long 21,700 put @ 35). Call side unchanged.
    # Total credit = 80 (calls) + 50 (closed puts) + 40 (new puts) = 170.
    adj = (call(S, 22300, 120, -1) + call(S, 22500, 40)
           + put(S, 21900, 75, -1) + put(S, 21700, 35) + 50)
    fig, ax = plt.subplots(figsize=(8, 4.6))
    ax.plot(S, orig, color=GREY, lw=1.8, ls="--", label="Original condor")
    ax.plot(S, adj, color=TEAL, lw=2, label="After rolling put side up (credit 170)")
    ax.axhline(0, color="#cccccc", lw=0.8)
    ax.set_title("Iron Condor adjustment — roll the untested put side up to re-centre")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.14), ncol=2, frameon=False)
    style(ax)
    save(fig, "iron_condor_adjust.png")


# 7. Short Strangle adjustment: after a rally, roll the untested put side up
def short_strangle_adjust():
    S = np.linspace(20800, 23400, 500)
    orig = put(S, 21700, 110, -1) + call(S, 22300, 120, -1)
    # Buy back the 21,700 put for 30 (locks in 110 - 30 = 80), sell a 21,900 put @ 90.
    # Total credit = 120 (call) + 80 (closed put) + 90 (new put) = 290.
    adj = put(S, 21900, 90, -1) + call(S, 22300, 120, -1) + 80
    fig, ax = plt.subplots(figsize=(8, 4.6))
    ax.plot(S, orig, color=GREY, lw=1.8, ls="--", label="Original strangle")
    ax.plot(S, adj, color=TEAL, lw=2, label="After rolling put side up (credit 290)")
    ax.axhline(0, color="#cccccc", lw=0.8)
    ax.set_title("Short Strangle adjustment — roll the untested side toward the move")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.14), ncol=2, frameon=False)
    style(ax)
    save(fig, "short_strangle_adjust.png")


if __name__ == "__main__":
    covered_call()
    bull_call_spread()
    iron_condor()
    short_strangle()
    long_straddle()
    iron_condor_adjust()
    short_strangle_adjust()
    print("done")
