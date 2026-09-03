#!/usr/bin/env python3
"""δ=5/2 linearized T2/T3 on the slice u=v=0, c=1.

x=s^{-2}, y=π s^5.  Slot x^{D-r-q}(y-x)^q = (-1)^q s^{-2(D-r)} (1-π s^7)^q.
p=π(π^2-1).  T2 target p^5 at s^{-5}; T3 target p^{10} q1 at s^{-10}.
q1 = -2 ∫ p^3  (Xu), monic rescaling as design (2.7) with b0=0.
"""
from __future__ import annotations

import json
import time
from collections import defaultdict
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
ZCAP = 30
SMIN, SMAX = -80, 12


def slot_u0(D, r, q):
    out = {}
    base = -2 * (D - r)
    for k in range(q + 1):
        s_exp = base + 7 * k
        if s_exp < SMIN or s_exp > SMAX or k > ZCAP:
            continue
        coeff = ((-1) ** (q + k)) * comb(q, k)
        if coeff:
            out.setdefault(s_exp, {})[k] = coeff
    return out


def poly_p():
    # π(π^2-1) = π^3 - π
    return {3: 1, 1: -1}


def poly_pow(poly, n, zcap=ZCAP):
    res = {0: 1}
    base = dict(poly)
    e = n
    while e:
        if e & 1:
            nxt = defaultdict(int)
            for d1, v1 in res.items():
                for d2, v2 in base.items():
                    d = d1 + d2
                    if d <= zcap:
                        nxt[d] += v1 * v2
            res = {d: v for d, v in nxt.items() if v != 0}
        e >>= 1
        if e:
            nxt = defaultdict(int)
            for d1, v1 in base.items():
                for d2, v2 in base.items():
                    d = d1 + d2
                    if d <= zcap:
                        nxt[d] += v1 * v2
            base = {d: v for d, v in nxt.items() if v != 0}
    return res


def q1_monic():
    # design (2.7) c=1 b0=0: π^10 - (15/4)π^8 + 5 π^6 - (5/2) π^4
    # keep over Q as fractions via integers *4: 4 q1 = 4π^10 - 15 π^8 + 20 π^6 - 10 π^4
    return {10: 1, 8: -15 / 4, 6: 5, 4: -5 / 2}


def support_rq(D, ycap):
    return [(r, q) for q in range(ycap) for r in range(D - q + 1)]


def d2_remain(D, ycap, sbound):
    return [(r, q) for r, q in support_rq(D, ycap) if 3 * r + 4 * q >= sbound]


def run():
    t0 = time.perf_counter()
    p = poly_p()
    p5 = poly_pow(p, 5, zcap=40)
    p10 = poly_pow(p, 10, zcap=40)
    q1 = q1_monic()
    # p^{10} q1
    target_T3 = defaultdict(float)
    for d1, v1 in p10.items():
        for d2, v2 in q1.items():
            target_T3[d1 + d2] += v1 * v2
    # orders
    # F_lead s^{-9}, G_lead s^{-6}, T2 s^{-5}, T3 s^{-10}
    # G^3-F^2 face: s^{-18}
    # T2 linear: 3 G0^2 dG - 2 F0 dF ~ 3 p^{12} s^{-12} dG - 2 p^9 s^{-9} dF
    # T2 at s^{-5} from dG at s^{7} or dF at s^{4} (high).
    # Count which remaining slots can feed T2 window s^{-18}..s^{-5}
    # A3 k0 s-order = -2(98-r); T2 via -2 F0 dA3: -9 + that.
    blocks = {
        "A3": (98, 33, 285, -9),
        "A2": (65, 33, 189, -15),  # extra h2 ~ s^{-3} because h2~p^3 t^{-3}? 
        # t=s^2, h2 ~ p^3 t^{-6} wait t^{-6}=s^{-12}? NO
        # F ~ h2^3 ~ s^{-9} so h2 ~ s^{-3}.  Yes t=s^2, t^{-6}=s^{-12} is WRONG for δ=5/2.
        # F_lead = 9(-8+7.5)=-4.5 in t, = s^{-9}. h2^3 = F so h2 ~ s^{-3}.
        "B2": (65, 33, 189, -12),  # 3 h2^4 ~ 4*(-3)=-12 times dB2
        "B1": (32, 33, 93, -15),
    }
    # Recompute shifts from δ=5/2:
    # h2 ~ s^{-3}, F0 ~ s^{-9}, G0 ~ s^{-6}
    # dT2 = 3 G0^2 dG - 2 F0 dF
    # A3: dF=A3, dT2 ~ -2 s^{-9} * A3  so T2 order = -9 + e_A3, e_A3=-2(98-r)
    # A2: dF=A2*h2, e = e_A2 + (-3), T2 = -9-3+e_A2 = -12 + e_A2
    # B2: dG=B2, dT2 ~ 3 s^{-12} * B2, T2 order = -12 + e_B2
    # B1: dG=B1*h2, T2 = -12-3+e_B1 = -15 + e_B1
    shifts = {"A3": -9, "A2": -12, "B2": -12, "B1": -15}
    Ds = {"A3": 98, "A2": 65, "B2": 65, "B1": 32}
    bounds = {"A3": (33, 285), "A2": (33, 189), "B2": (33, 189), "B1": (33, 93)}
    t2_win = (-18, -5)
    hits = {}
    for name in shifts:
        D = Ds[name]
        ycap, sb = bounds[name]
        slots = d2_remain(D, ycap, sb)
        n = 0
        ords = []
        for r, q in slots:
            e0 = -2 * (D - r)
            t2e = e0 + shifts[name]
            if t2_win[0] <= t2e <= t2_win[1]:
                n += 1
                ords.append(t2e)
        hits[name] = {
            "D2_remain": len(slots),
            "T2_window_k0": n,
            "T2_orders_min_max": (min(ords), max(ords)) if ords else None,
            "shift": shifts[name],
            "k0_min": min(-2 * (D - r) for r, q in slots) if slots else None,
        }
    # Tschirnhausen entry in s: G^2 ~ s^{-12}, FG ~ s^{-15}, F~s^{-9}, G~s^{-6}, const 0
    tsch = {
        "a1_FG": {"first_s": -15, "in_T2_window": True},
        "c0_G2": {"first_s": -12, "in_T2_window": True},
        "b1_F": {"first_s": -9, "in_T2_window": True},
        "a0_G": {"first_s": -6, "in_T2_window": True},
        "b0": {"first_s": 0, "in_T2_window": False},
        "T2_target_s": -5,
    }
    # q1 check: q1' + 2 p^3 = 0 for Xu's -2∫; monic (2.7)' = 10 p^3
    # p=π^3-π, p^3 degree 9.  Record degrees.
    result = {
        "type": "DERIVED[DELTA-5/2-LINEAR-SUPPORT / u=v=0 c=1]",
        "p": "pi(pi^2-1)",
        "T2_target": {"s_order": -5, "shape": "p^5", "deg": max(p5)},
        "T3_target": {"s_order": -10, "shape": "p^{10} q1", "deg_p10q1": max(target_T3) if target_T3 else None},
        "q1_monic_c1_b0": {str(k): v for k, v in q1.items()},
        "h2_order_s": -3,
        "outer_T2_window": hits,
        "Tschirnhausen_entry_s": tsch,
        "linearity": {
            "T2_s_window": "s^{-18}..s^{-5}; N=1 relative to face s^{-18} is linear; N>=2 quadratic",
            "T3_leader_s_-10": "face G^9-F^6 at s^{-54}; leader not a face multiple of 6 in t, same residual phenomenon",
            "p10q1_deg": 40,
        },
        "elapsed_seconds": round(time.perf_counter() - t0, 3),
    }
    (HERE / "residual_d52.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result["outer_T2_window"], indent=2))
    return result


if __name__ == "__main__":
    run()
