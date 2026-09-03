#!/usr/bin/env python3
"""Minor-jet support: which chart coefficients of F, G appear at each t-order.

Chart (2.1).  Outer D2 remaining slots live in the t^r (w-1)^q basis, which
pulls back as x^{D-r-q}(y-x)^q.  At the second point x=t^{-1},
y = u t + z t^2 (δ=2) or y = u s^2 + v s^4 + π s^5 with t=s^2 (δ=5/2).

SOURCE: design (2.1)(2.4)(2.6); outer_order_bands.py BLOCKS / thresholds;
major_tower_structure.py C2/C3 D2 pivots.
"""
from __future__ import annotations

import json
from collections import defaultdict
from fractions import Fraction
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent

BLOCKS = {
    "A2": {"D": 65, "ycap": 33, "sbound": 189, "role": "F via A2*h2"},
    "A3": {"D": 98, "ycap": 33, "sbound": 285, "role": "F via A3"},
    "B1": {"D": 32, "ycap": 33, "sbound": 93, "role": "G via B1*h2"},
    "B2": {"D": 65, "ycap": 33, "sbound": 189, "role": "G via B2"},
}


def support_rq(D: int, ycap: int):
    return [(r, q) for q in range(ycap) for r in range(D - q + 1)]


def d2_remain(name: str):
    b = BLOCKS[name]
    return [(r, q) for r, q in support_rq(b["D"], b["ycap"]) if 3 * r + 4 * q >= b["sbound"]]


def d2_vanish(name: str):
    b = BLOCKS[name]
    return [(r, q) for r, q in support_rq(b["D"], b["ycap"]) if 3 * r + 4 * q < b["sbound"]]


def delta2_orders(r: int, D: int, q: int):
    """t-exponents of x^{D-r-q}(y-x)^q at y=u t + z t^2, x=t^{-1}.

    Expand (y-x)^q = sum_k C(q,k) y^k (-x)^{q-k}.  Each k contributes
    t^{-(D-r-k)} * t^k  from x^{D-r-k} y^k if the leading y~t term is taken,
    i.e. orders -D+r+2k through -D+r+3k (k factors of z t^2 vs u t).
    Lowest (most singular) is k=0: r-D.  Highest is k=q, all z: -D+r+3q.
    """
    lowest = r - D  # k=0
    highest = r - D + 3 * q  # k=q, all t^2
    # generic-u lowest is still k=0; with u≠0 the k-term lowest is r-D+2k
    lowest_u = r - D  # same
    highest_u = r - D + 2 * q  # k=q, all u t  (no extra t from z)
    return {
        "lowest_u_generic": lowest_u,
        "highest_u_generic": highest_u,
        "lowest_u0": lowest,  # same k=0
        "highest_u0": r - D + 3 * q,
        "k0_order": r - D,
    }


def delta52_orders(r: int, D: int, q: int):
    """s-exponents at x=s^{-2}, y=u s^2 + v s^4 + π s^5.

    x^{D-r-k} y^k ~ s^{-2(D-r-k)} * (s^2)^k * (leading u) = s^{-2D+2r+2k+2k}
    wait: y^k ~ s^{2k} (u + ...), x^{D-r-k} ~ s^{-2(D-r-k)}.
    Total s^{-2D+2r+2k + 2k} = s^{-2D+2r+4k} for all-u.
    All-π: y^k ~ s^{5k}, total s^{-2(D-r-k)+5k} = s^{-2D+2r+2k+5k} = s^{-2D+2r+7k}.
    k=0: s^{-2(D-r)} = s^{-2D+2r}.
    """
    return {
        "lowest": -2 * D + 2 * r,
        "highest_u": -2 * D + 2 * r + 4 * q,
        "highest_pi": -2 * D + 2 * r + 7 * q,
    }


def c2_c3_remaining():
    """D2 unit pivots from major_tower_structure.py; remaining C2/C3 (r,q).

    C2 positions: r=1..22, q=0..min(10,22-r)  — 187 slots (no r=0 face).
    C3 positions: r=1..33, q=0..min(10,33-r)  — 308 slots.
    D2 slots with 3r+4q<=96, minus 3 identities, 389 unit pivots.
    """

    def positions(D, y_cap):
        return {(r, q) for r in range(1, D + 1) for q in range(min(y_cap, D - r) + 1)}

    c2 = positions(22, 10)
    c3 = positions(33, 10)
    d2_slots = {
        (r, q)
        for r in range(1, 34)
        for q in range(34 - r)
        if 3 * r + 4 * q <= 96
    }
    # identities
    identities = {(1, 23), (1, 22), (2, 22)}
    ordered_rows = sorted(d2_slots - identities, key=lambda p: (p[0], -p[1]))
    pivots = set()
    for r, q in ordered_rows:
        if q <= 10:
            pivots.add(("C3", r, q))
        else:
            pivots.add(("C2", r, q - 11))
    c2_piv = {(p[1], p[2]) for p in pivots if p[0] == "C2"}
    c3_piv = {(p[1], p[2]) for p in pivots if p[0] == "C3"}
    c2_rem = sorted(c2 - c2_piv)
    c3_rem = sorted(c3 - c3_piv)
    d1_taken = {
        ("C2", 11, 8),
        ("C2", 15, 5),
        ("C2", 19, 2),
        ("C3", 23, 7),
        ("C3", 27, 4),
        ("C2", 10, 9),
        ("C2", 14, 6),
    }
    c2_after_d1 = [pq for pq in c2_rem if ("C2",) + pq not in d1_taken]
    c3_after_d1 = [pq for pq in c3_rem if ("C3",) + pq not in d1_taken]
    return {
        "C2_ambient": len(c2),
        "C3_ambient": len(c3),
        "C2_D2_pivots": len(c2_piv),
        "C3_D2_pivots": len(c3_piv),
        "C2_remain_D2": len(c2_rem),
        "C3_remain_D2": len(c3_rem),
        "C2_remain_after_D1": len(c2_after_d1),
        "C3_remain_after_D1": len(c3_after_d1),
        "inner_remain_after_D1": len(c2_after_d1) + len(c3_after_d1),
        "C2_remain_rq": c2_after_d1,
        "C3_remain_rq": c3_after_d1,
    }


def h3_free():
    return ["c_7_4", "c_10_1", "c_11_0"]


def t2_t3_windows(delta: str):
    """Xu p.13 orders."""
    if delta == "2":
        d = 2
        return {
            "delta": 2,
            "F_lead": 9 * (-8 + 3 * d),  # -18
            "G_lead": 6 * (-8 + 3 * d),  # -12
            "T2_lead": 5 * (-8 + 3 * d),  # -10
            "T3_lead": 13 * (-8 + 3 * d) - 1 + d,  # -25
            "G3_F2_face": 18 * (-8 + 3 * d),  # -36
            "G9_F6_face": 54 * (-8 + 3 * d),  # -108
            "p": "z^2 (z+3a)",
            "T2_shape": "p^5 = z^{10}(z+3a)^5",
            "T3_shape": "R = z^{25}(z+3a)^{14}(z-2a)",
            "packets_F": "18+9",
            "H": "z^2(z+3a)",
        }
    d = Fraction(5, 2)
    def qstr(x):
        return str(x)
    return {
        "delta": "5/2",
        "F_lead": qstr(9 * (-8 + 3 * d)),
        "G_lead": qstr(6 * (-8 + 3 * d)),
        "T2_lead": qstr(5 * (-8 + 3 * d)),
        "T3_lead": qstr(13 * (-8 + 3 * d) - 1 + d),
        "G3_F2_face": qstr(18 * (-8 + 3 * d)),
        "G9_F6_face": qstr(54 * (-8 + 3 * d)),
        "p": "pi (pi^2 - c)",
        "T2_shape": "p^5",
        "T3_shape": "p^{10} q1, q1=-2∫p^3",
        "packets_F": "9+9+9",
        "H": "pi(pi^2-c)",
    }


def classify_block(name: str):
    b = BLOCKS[name]
    remain = d2_remain(name)
    vanish = d2_vanish(name)
    by_k0 = defaultdict(list)
    in_t2_window = []
    in_t3_window = []
    # T2: contrib of a direct summand S at order e, after multiplying by
    # h2-powers, lands in [-36,-10] (δ=2).  For A3, multiplier h2^0 so e itself;
    # but T2 contains -2 F0 dA3 with F0 ~ t^{-18}, so T2 order = -18 + e.
    # Record raw e = r-D (k=0) and the T2/T3 translated orders.
    t2_mult = {"A3": -18, "A2": -18 - 6, "B2": -24, "B1": -24 - 6}
    # A2 * h2 ~ e + (-6); then * (-2 F0) wait: dF includes A2*h2_0, then
    # dT2 includes -2 F0 dF = -2 t^{-18} * (A2 * t^{-6}) = t^{-24} * A2.
    # Let me use the G^3-F^2 expansion:
    #  -2 h2^3 ε_F, ε_F = A2 h2 + A3, h2~t^{-6}
    #  A3: T2 order = -18 + e_A3
    #  A2: T2 order = -18 + (e_A2 - 6) = e_A2 - 24
    #  B2: 3 h2^4 ε_G, ε_G=B2: T2 order = -24 + e_B2
    #  B1: ε_G = B1 h2: T2 order = -24 + e_B1 - 6 = e_B1 - 30
    t2_shift = {"A3": -18, "A2": -24, "B2": -24, "B1": -30}
    t3_shift = {
        # 9 G0^8 dG - 6 F0^5 dF; G0~t^{-12}, F0~t^{-18}
        # dF=A3: T3 ~ -18*5 + e?  F^6 linear: 6 F0^5 dF ~ t^{-90} * dF
        # F0^5 ~ t^{-90}, * A3: t^{-90+e}
        "A3": -90,
        "A2": -96,  # A2*h2, extra -6
        "B2": -96,  # 9 G0^8 dG, G0^8 ~ t^{-96}
        "B1": -102,
    }
    t2_win = (-36, -10)
    t3_win = (-108, -25)
    for r, q in remain:
        info = delta2_orders(r, b["D"], q)
        e0 = info["k0_order"]
        by_k0[e0].append((r, q))
        t2e = e0 + t2_shift[name]
        t3e = e0 + t3_shift[name]
        rec = {
            "rq": [r, q],
            "ij": [b["D"] - r - q, q],
            "k0_order": e0,
            "T2_k0_order": t2e,
            "T3_k0_order": t3e,
            "delta2": info,
            "delta52": delta52_orders(r, b["D"], q),
        }
        if t2_win[0] <= t2e <= t2_win[1]:
            in_t2_window.append(rec)
        if t3_win[0] <= t3e <= t3_win[1]:
            in_t3_window.append(rec)
    k0_counts = {str(e): len(v) for e, v in sorted(by_k0.items())}
    return {
        "name": name,
        "ambient": len(support_rq(b["D"], b["ycap"])),
        "D2_vanish": len(vanish),
        "D2_remain": len(remain),
        "k0_order_min": min(by_k0) if by_k0 else None,
        "k0_order_max": max(by_k0) if by_k0 else None,
        "k0_counts_head": dict(list(k0_counts.items())[:8]),
        "k0_counts_tail": dict(list(k0_counts.items())[-6:]),
        "T2_window_slots_k0": len(in_t2_window),
        "T3_window_slots_k0": len(in_t3_window),
        "T2_shift": t2_shift[name],
        "T3_shift": t3_shift[name],
        "sample_T2": in_t2_window[:5],
        "sample_T2_tail": in_t2_window[-3:] if len(in_t2_window) > 5 else [],
        "role": b["role"],
    }


def t_coeff_entry_N():
    """N-index of Tschirnhausen terms in T2 relative to t^{-36} at δ=2.

    G^2 ~ t^{-24} enters at N=12; FG ~ t^{-30} at N=6; G ~ t^{-12} at N=24;
    F ~ t^{-18} at N=18; const at N=36 (after the T2 leader N=26).
    """
    return {
        "c0_G2": {"first_N": 12, "first_order": -24, "in_T2_vanishing_window": True},
        "a1_FG": {"first_N": 6, "first_order": -30, "in_T2_vanishing_window": True},
        "b1_F": {"first_N": 18, "first_order": -18, "in_T2_vanishing_window": True},
        "a0_G": {"first_N": 24, "first_order": -12, "in_T2_vanishing_window": True},
        "b0": {"first_N": 36, "first_order": 0, "in_T2_vanishing_window": False},
        "T2_target_N": 26,
        "T2_target_order": -10,
        "note": "b0 does not appear in the T2 leader at δ=2; a0 first appears at order -12, two steps before the leader.",
    }


def linearity_by_N():
    """Simultaneous vs sequential linearity of T2 coefficient of t^{-36+N}."""
    rows = []
    for N in range(0, 37):
        # G^3: sum_{i+j+k=N} g_i g_j g_k, F^2: sum_{i+j=N} f_i f_j
        cubic = N >= 3  # g1^3
        quadratic = N >= 2  # g1^2 g0, f1^2
        tsch = []
        if N >= 6:
            tsch.append("a1")
        if N >= 12:
            tsch.append("c0")
        if N >= 18:
            tsch.append("b1")
        if N >= 24:
            tsch.append("a0")
        if N >= 36:
            tsch.append("b0")
        simultaneous = "linear_in_chart" if N <= 1 and not tsch else "nonlinear_in_chart"
        if N == 0:
            simultaneous = "identity_cancel"
        sequential = "affine_in_new_jets_fN_gN"
        rows.append(
            {
                "N": N,
                "t_order_delta2": -36 + N,
                "is_T2_leader": N == 26,
                "in_vanishing_window": 1 <= N <= 25,
                "simultaneous_in_chart_after_T_fixed": simultaneous
                if N != 0
                else "identity_cancel",
                "T_coeffs_that_entered": tsch,
                "has_quadratic_jets": quadratic,
                "has_cubic_jets": cubic,
                "sequential_Newton": sequential,
            }
        )
    return rows


def run() -> dict:
    inner = c2_c3_remaining()
    blocks = {name: classify_block(name) for name in BLOCKS}
    outer_remain = sum(blocks[n]["D2_remain"] for n in BLOCKS)
    # D1 takes 176 more; 1002-176=826
    t2w = sum(blocks[n]["T2_window_slots_k0"] for n in BLOCKS)
    t3w = sum(blocks[n]["T3_window_slots_k0"] for n in BLOCKS)
    # h3 free tails: joint_probe x^1, x^2 of K/x^9
    return {
        "type": "DERIVED[MINOR-JET-SUPPORT]",
        "windows": {"delta2": t2_t3_windows("2"), "delta52": t2_t3_windows("52")},
        "h3_free_after_common_leader": h3_free(),
        "inner_C2_C3": {
            k: inner[k]
            for k in inner
            if k not in ("C2_remain_rq", "C3_remain_rq")
        },
        "outer_blocks": {
            n: {k: v for k, v in blocks[n].items() if k not in ("sample_T2", "sample_T2_tail")}
            for n in BLOCKS
        },
        "outer_T2_window_samples": {n: blocks[n]["sample_T2"] for n in BLOCKS},
        "counts": {
            "outer_D2_remain": outer_remain,
            "outer_after_D1_expected": 826,
            "inner_after_D1": inner["inner_remain_after_D1"],
            "h3_free": 3,
            "joint_inner_plus_centre_charged": 104,
            "T2_k0_slots_all_four_blocks": t2w,
            "T3_k0_slots_all_four_blocks": t3w,
            "T2_unknowns_Tschirnhausen_after_alpha1": 4,
            "T3_unknowns_Tschirnhausen_after_alpha1": 34,
        },
        "T2_Tschirnhausen_entry": t_coeff_entry_N(),
        "linearity_by_N_delta2_T2": linearity_by_N(),
        "pullback": (
            "D2 remaining (r,q) is t^r (w-1)^q, i.e. the (x,y) polynomial "
            "x^{D-r-q}(y-x)^q.  At the minor line this is NOT a pure x^i y^j "
            "pole: (y-x)^q ~ (-x)^q plus y-corrections, so the k=0 term has "
            "t-order r-D, which for remaining A3 starts at -45 (more singular "
            "than F_lead=-18).  Those slots are genuine subleading-to-the-top "
            "jets and must cancel in (2.4) before T2 is matched."
        ),
        "inner_remain_rq_counts_only": True,
        "C2_remain_rq_head": inner["C2_remain_rq"][:8],
        "C3_remain_rq_head": inner["C3_remain_rq"][:8],
    }


if __name__ == "__main__":
    data = run()
    out = HERE / "jet_support.json"
    out.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: data[k] for k in ("type", "counts", "pullback")}, indent=2))
    print("wrote", out)
