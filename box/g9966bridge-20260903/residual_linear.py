#!/usr/bin/env python3
"""Linearized T2/T3 bridge on the straight slice u=0, a=1, plus F/G leaders.

Base point: common-h3 leader with free h3 tails set to 0, C2=C3=A=B=0,
rho=a=1, u=0.  Then F0=h3^9, G0=h3^6.  Remaining D2 outer slots and remaining
C2/C3 are first-order perturbations.  Tschirnhausen coefficients of T2 (4 after
alpha1=0, or 5 including c0) are extra columns.

At u=0, y=z t^2, x=t^{-1}:
    x^{D-r-q}(y-x)^q = (-1)^q t^{r-D} (1 - z t^3)^q.

T2 linearization (T-coeffs at 0, then their own columns):
    dT2 = 3 G0^2 dG - 2 F0 dF
T3:
    dT3 = 9 G0^8 dG - 6 F0^5 dF   (alpha_i=0 except monic -F^6)

Q* over Q on the sparse (t-order, z-degree) matrix.  Then dump leftover
quadratic generators for modular standard bases.

Caps: this process should finish in a few minutes; Singular jobs are separate.
"""
from __future__ import annotations

import json
import sys
import time
from collections import defaultdict
from fractions import Fraction
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent

A1 = 1  # torus slice rho=a=1
ZCAP = 40
# series t-exponents retained
TMIN, TMAX = -120, 12


def binom(n, k):
    if k < 0 or k > n:
        return 0
    return comb(n, k)


# --- sparse series: dict[t] -> dict[zdeg] -> Fraction ---

def series_add(A, B, c=1):
    out = {t: dict(zs) for t, zs in A.items()}
    for t, zs in B.items():
        bucket = out.setdefault(t, {})
        for d, v in zs.items():
            bucket[d] = bucket.get(d, 0) + c * v
            if bucket[d] == 0:
                del bucket[d]
        if not bucket:
            del out[t]
    return out


def series_scale(A, c):
    if c == 0:
        return {}
    return {t: {d: c * v for d, v in zs.items()} for t, zs in A.items()}


def series_shift(A, dt):
    return {t + dt: zs for t, zs in A.items()}


def series_mul(A, B, tmin=TMIN, tmax=TMAX, zcap=ZCAP):
    out = defaultdict(lambda: defaultdict(int))
    for t1, zs1 in A.items():
        for t2, zs2 in B.items():
            t = t1 + t2
            if t < tmin or t > tmax:
                continue
            for d1, v1 in zs1.items():
                for d2, v2 in zs2.items():
                    d = d1 + d2
                    if d > zcap:
                        continue
                    out[t][d] += v1 * v2
    # drop zeros
    clean = {}
    for t, zs in out.items():
        nz = {d: v for d, v in zs.items() if v != 0}
        if nz:
            clean[t] = nz
    return clean


def series_pow(A, n, tmin=TMIN, tmax=TMAX, zcap=ZCAP):
    if n == 0:
        return {0: {0: 1}}
    if n == 1:
        return A
    # binary power
    result = {0: {0: 1}}
    base = A
    e = n
    while e:
        if e & 1:
            result = series_mul(result, base, tmin, tmax, zcap)
        e >>= 1
        if e:
            base = series_mul(base, base, tmin, tmax, zcap)
    return result


def series_from_poly_z(coeffs_by_deg, t_exp):
    """coeffs_by_deg: dict zdeg -> Fraction, placed at a single t_exp."""
    nz = {d: v for d, v in coeffs_by_deg.items() if v != 0}
    return {t_exp: nz} if nz else {}


def poly_p():
    # p = z^2 (z+3) = z^3 + 3 z^2   (a=1)
    return {3: 1, 2: 3}


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


def poly_R():
    # R = z^25 (z+3)^14 (z-2) at a=1
    # (z+3)^14 via binomial, times z^25, times (z-2)
    a = {}  # (z+3)^14
    for k in range(15):
        a[k] = binom(14, k) * (3 ** (14 - k))  # (z+3)^14 = sum C(14,k) z^k 3^{14-k}
    # wait: (z+3)^14 = sum C(14,j) z^j 3^{14-j}, deg j
    b = {}  # z^25 * (z+3)^14
    for j, v in a.items():
        b[j + 25] = v
    # times (z-2)
    out = defaultdict(int)
    for d, v in b.items():
        out[d + 1] += v
        out[d] += -2 * v
    return {d: v for d, v in out.items() if v != 0}


def slot_series_u0(D, r, q, tmin=TMIN, tmax=TMAX, zcap=ZCAP):
    """x^{D-r-q}(y-x)^q at u=0: (-1)^q t^{r-D} (1-z t^3)^q."""
    out = {}
    base = r - D
    for k in range(q + 1):
        t = base + 3 * k
        if t < tmin or t > tmax:
            continue
        if k > zcap:
            continue
        coeff = ((-1) ** (q + k)) * binom(q, k)
        # (1 - z t^3)^q term k is C(q,k) (-z t^3)^k = C(q,k) (-1)^k z^k t^{3k}
        # times (-1)^q : (-1)^{q+k} C(q,k) z^k
        if coeff:
            out.setdefault(t, {})[k] = out.get(t, {}).get(k, 0) + coeff
    return {t: zs for t, zs in out.items() if zs}


def support_rq(D, ycap):
    return [(r, q) for q in range(ycap) for r in range(D - q + 1)]


def d2_remain(D, ycap, sbound):
    return [(r, q) for r, q in support_rq(D, ycap) if 3 * r + 4 * q >= sbound]


def c2_c3_remaining():
    def positions(D, y_cap):
        return {(rr, qq) for rr in range(1, D + 1) for qq in range(min(y_cap, D - rr) + 1)}

    c2 = positions(22, 10)
    c3 = positions(33, 10)
    d2_slots = {
        (rr, qq)
        for rr in range(1, 34)
        for qq in range(34 - rr)
        if 3 * rr + 4 * qq <= 96
    }
    identities = {(1, 23), (1, 22), (2, 22)}
    ordered_rows = sorted(d2_slots - identities, key=lambda p: (p[0], -p[1]))
    pivots = set()
    for rr, qq in ordered_rows:
        if qq <= 10:
            pivots.add(("C3", rr, qq))
        else:
            pivots.add(("C2", rr, qq - 11))
    c2_piv = {(p[1], p[2]) for p in pivots if p[0] == "C2"}
    c3_piv = {(p[1], p[2]) for p in pivots if p[0] == "C3"}
    d1_taken = {
        ("C2", 11, 8),
        ("C2", 15, 5),
        ("C2", 19, 2),
        ("C3", 23, 7),
        ("C3", 27, 4),
        ("C2", 10, 9),
        ("C2", 14, 6),
    }
    c2_rem = sorted(pq for pq in (c2 - c2_piv) if ("C2",) + pq not in d1_taken)
    c3_rem = sorted(pq for pq in (c3 - c3_piv) if ("C3",) + pq not in d1_taken)
    return c2_rem, c3_rem


def build_base_h3():
    """Straight u=0, a=1, free h3 tails 0.

    Leader H=z^2(z+3).  Charged joint_probe:
      W3 = -8 z^4 - 18 a z^3
      W6 = 28 z^5 + 45 a z^4
    K/x^9 = H + W3 x^3 + W6 x^6 + (higher from the 21-term major filter;
    with free c_7_4=c_10_1=c_11_0=0 the displayed bands vanish at x^1,x^2).
    h3 = t^{-2} (H + W3 t^3 + W6 t^6 + ...)
    """
    H = {3: 1, 2: 3}  # z^3+3z^2
    W3 = {4: -8, 3: -18}
    W6 = {5: 28, 4: 45}
    h3 = {}
    h3[-2] = dict(H)
    h3[1] = dict(W3)
    h3[4] = dict(W6)
    return h3


def series_coeff_vec(S, t_lo, t_hi, zcap=ZCAP):
    """Flatten S on t in [t_lo,t_hi], zdeg 0..zcap to a dict (t,d)->Fraction."""
    vec = {}
    for t, zs in S.items():
        if t_lo <= t <= t_hi:
            for d, v in zs.items():
                if 0 <= d <= zcap and v != 0:
                    vec[(t, d)] = v
    return vec


def qstar_sparse(columns, row_order, col_names):
    """columns: name -> {(t,d): Fraction}.  Exact Q* unit-or-rational pivots.

    Affine-linear homogeneous (targets subtracted already).  Returns
    rank, pivot list, remaining column names, leftover row dicts.
    """
    # Build row -> {col: coeff}
    rows = []
    for key in row_order:
        rec = {}
        for j, name in enumerate(col_names):
            v = columns[name].get(key)
            if v:
                rec[name] = Fraction(v)
        if rec:
            rows.append((key, rec))

    remaining = list(col_names)
    pivots = []
    used = [False] * len(rows)
    progressed = True
    while progressed:
        progressed = False
        for i, (key, rec) in enumerate(rows):
            if used[i]:
                continue
            rec = {n: v for n, v in rec.items() if v != 0}
            rows[i] = (key, rec)
            if not rec:
                used[i] = True
                continue
            choice = None
            for name in remaining:
                if name in rec and rec[name] != 0:
                    choice = name
                    break
            if choice is None:
                continue
            coeff = rec[choice]
            rhs = {n: -v / coeff for n, v in rec.items() if n != choice}
            pivots.append({"row": list(key), "var": choice, "coeff": str(coeff)})
            remaining.remove(choice)
            used[i] = True
            progressed = True
            for j, (k2, rec2) in enumerate(rows):
                if used[j] or choice not in rec2:
                    continue
                scale = rec2.pop(choice)
                for n, v in rhs.items():
                    rec2[n] = rec2.get(n, Fraction(0)) + scale * v
                    if rec2[n] == 0:
                        rec2.pop(n)
            break
    leftover = [(k, rec) for i, (k, rec) in enumerate(rows) if not used[i] and rec]
    return {
        "rank": len(pivots),
        "n_columns": len(col_names),
        "n_remaining": len(remaining),
        "n_leftover_rows": len(leftover),
        "pivots_head": pivots[:12],
        "pivots_count": len(pivots),
        "remaining_head": remaining[:20],
        "remaining_count": len(remaining),
        "leftover_head": [
            {"row": list(k), "terms": len(rec), "sample": {n: str(v) for n, v in list(rec.items())[:6]}}
            for k, rec in leftover[:8]
        ],
        "pivots": pivots,
        "remaining": remaining,
        "leftover": leftover,
    }


def run():
    t0 = time.perf_counter()
    log = []
    def stamp(msg):
        log.append(f"{time.perf_counter()-t0:7.2f}s  {msg}")
        print(log[-1], flush=True)

    stamp("base h3")
    h3 = build_base_h3()
    stamp("h2 = h3^3")
    h2 = series_pow(h3, 3, tmin=-40, tmax=8, zcap=ZCAP)
    stamp(f"h2 terms {sum(len(z) for z in h2.values())} at t={sorted(h2)}")
    stamp("F0 = h2^3 = h3^9")
    F0 = series_pow(h2, 3, tmin=-60, tmax=8, zcap=ZCAP)
    stamp("G0 = h2^2 = h3^6")
    G0 = series_pow(h2, 2, tmin=-50, tmax=8, zcap=ZCAP)
    stamp(f"F0 t={sorted(F0)[:8]}... G0 t={sorted(G0)[:8]}...")

    p = poly_p()
    p9 = poly_pow(p, 9)
    p6 = poly_pow(p, 6)
    p5 = poly_pow(p, 5)
    R = poly_R()
    # check leaders
    def lead_poly(S, t_exp):
        return dict(S.get(t_exp, {}))

    Flead = lead_poly(F0, -18)
    Glead = lead_poly(G0, -12)
    stamp(f"F0[-18] deg keys {sorted(Flead)} p9 keys {sorted(p9)}")
    stamp(f"G0[-12] deg keys {sorted(Glead)} p6 keys {sorted(p6)}")

    # scale check: F0[-18] should be H^9 = p^9
    def poly_eq(A, B):
        keys = set(A) | set(B)
        return all(A.get(k, 0) == B.get(k, 0) for k in keys)

    stamp(f"F_lead==p^9 {poly_eq(Flead, p9)}  G_lead==p^6 {poly_eq(Glead, p6)}")

    G0sq = series_mul(G0, G0, tmin=-50, tmax=8, zcap=ZCAP)
    F0G0 = series_mul(F0, G0, tmin=-50, tmax=8, zcap=ZCAP)
    G0_8 = series_pow(G0, 8, tmin=-110, tmax=8, zcap=min(ZCAP, 48))
    F0_5 = series_pow(F0, 5, tmin=-110, tmax=8, zcap=min(ZCAP, 48))
    stamp("powers of F0,G0 ready")

    columns_F = {}  # name -> dF series
    columns_G = {}

    # Outer remaining
    outer_spec = {
        "A3": (98, 33, 285, "F"),
        "A2": (65, 33, 189, "F"),
        "B2": (65, 33, 189, "G"),
        "B1": (32, 33, 93, "G"),
    }
    for name, (D, ycap, sbound, which) in outer_spec.items():
        slots = d2_remain(D, ycap, sbound)
        stamp(f"{name} D2-remain {len(slots)}")
        for r, q in slots:
            S = slot_series_u0(D, r, q)
            key = f"{name}_{r}_{q}"
            if name == "A3":
                columns_F[key] = S
            elif name == "A2":
                columns_F[key] = series_mul(S, h2, tmin=TMIN, tmax=TMAX, zcap=ZCAP)
            elif name == "B2":
                columns_G[key] = S
            else:
                columns_G[key] = series_mul(S, h2, tmin=TMIN, tmax=TMAX, zcap=ZCAP)

    c2_rem, c3_rem = c2_c3_remaining()
    stamp(f"C2 rem {len(c2_rem)} C3 rem {len(c3_rem)}")
    # C3 in S(32,11) design; structure uses D=33 face-excluded.
    # dh2 = slot of C3 (D=32 in design, but positions(33,10) with r>=1).
    # Use D=32 for (y-x) pullback of C3?  Chart: C3 in S(32,11),
    # K_C3 = t^{32} C3(t^{-1},w/t).  Slot t^r (w-1)^q -> x^{32-r-q}(y-x)^q.
    # major_tower positions(33,10) is the h2-degree-33 chart of C3 as a
    # degree-32 polynomial plus?  We follow the structure file's (r,q) as
    # the K2 coordinates of C3, D=32 matching S(32,11) after dropping r=0.
    for r, q in c3_rem:
        if r > 32:
            continue
        S = slot_series_u0(32, r, q)
        dh2 = S
        dF = series_mul(series_scale(series_mul(h2, h2), 3), dh2, tmin=TMIN, tmax=TMAX)
        dG = series_mul(series_scale(h2, 2), dh2, tmin=TMIN, tmax=TMAX)
        columns_F[f"C3_{r}_{q}"] = dF
        columns_G[f"C3_{r}_{q}"] = dG
    for r, q in c2_rem:
        if r > 21:
            continue
        S = slot_series_u0(21, r, q)
        dh2 = series_mul(S, h3, tmin=TMIN, tmax=TMAX)
        dF = series_mul(series_scale(series_mul(h2, h2), 3), dh2, tmin=TMIN, tmax=TMAX)
        dG = series_mul(series_scale(h2, 2), dh2, tmin=TMIN, tmax=TMAX)
        columns_F[f"C2_{r}_{q}"] = dF
        columns_G[f"C2_{r}_{q}"] = dG

    # free h3 tails: K/x^9 has x^1: -c_10_1 - c_7_4 z, x^2: c_11_0
    # h3 += c_7_4 * ( -z t^{-1} ) + c_10_1 * ( - t^{-1} ) + c_11_0 * t^{0}
    # because t^{-2} * (t * (...)) = t^{-1}.
    def from_dh3(dh3):
        dh2 = series_mul(series_scale(series_mul(h3, h3), 3), dh3, tmin=TMIN, tmax=TMAX)
        dF = series_mul(series_scale(series_mul(h2, h2), 3), dh2, tmin=TMIN, tmax=TMAX)
        dG = series_mul(series_scale(h2, 2), dh2, tmin=TMIN, tmax=TMAX)
        return dF, dG

    dF, dG = from_dh3({-1: {1: -1}})  # -z t^{-1}
    columns_F["c_7_4"], columns_G["c_7_4"] = dF, dG
    dF, dG = from_dh3({-1: {0: -1}})
    columns_F["c_10_1"], columns_G["c_10_1"] = dF, dG
    dF, dG = from_dh3({0: {0: 1}})
    columns_F["c_11_0"], columns_G["c_11_0"] = dF, dG
    stamp(f"columns F {len(columns_F)} G {len(columns_G)}")

    all_names = sorted(set(columns_F) | set(columns_G))

    def dT2_of(name):
        dF = columns_F.get(name, {})
        dG = columns_G.get(name, {})
        termG = series_mul(series_scale(G0sq, 3), dG, tmin=-40, tmax=5, zcap=ZCAP)
        termF = series_mul(series_scale(F0, -2), dF, tmin=-40, tmax=5, zcap=ZCAP)
        return series_add(termG, termF)

    def dT3_of(name):
        dF = columns_F.get(name, {})
        dG = columns_G.get(name, {})
        termG = series_mul(series_scale(G0_8, 9), dG, tmin=-110, tmax=5, zcap=min(ZCAP, 48))
        termF = series_mul(series_scale(F0_5, -6), dF, tmin=-110, tmax=5, zcap=min(ZCAP, 48))
        return series_add(termG, termF)

    # Tschirnhausen T2 columns (alpha1 = c0 on G^2 is kept; Tschirnhausen-zero of G^2
    # in f is a different normalisation).  After alpha1=0: c0, a1, a0, b1, b0.
    t2_tsch = {
        "T2_c0": G0sq,
        "T2_a1": F0G0,
        "T2_a0": G0,
        "T2_b1": F0,
        "T2_b0": {0: {0: 1}},
    }

    stamp("build T2 linear matrix")
    t2_cols = {}
    for name in all_names:
        t2_cols[name] = series_coeff_vec(dT2_of(name), -36, -10)
    for name, S in t2_tsch.items():
        t2_cols[name] = series_coeff_vec(S, -36, -10)

    # F/G leader rows linearized: [t^e] dF = 0 for e < -18; [t^{-18}] dF = 0
    # (homogeneous, face already matched by F0); same for G below -12.
    fg_cols = {}
    for name in all_names:
        v = {}
        for (t, d), c in series_coeff_vec(columns_F.get(name, {}), -80, -18).items():
            v[("F", t, d)] = c
        for (t, d), c in series_coeff_vec(columns_G.get(name, {}), -60, -12).items():
            v[("G", t, d)] = c
        fg_cols[name] = v
    for name in t2_tsch:
        fg_cols[name] = {}

    # T2 target: p^5 at t=-10, zeros on -35..-11.  Homogeneous matrix for
    # the vanishing window; separately test whether p^5 lies in the t=-10 image.
    t2_van_rows = [(t, d) for t in range(-35, -10) for d in range(ZCAP + 1)]
    t2_lead_rows = [(-10, d) for d in range(ZCAP + 1)]
    t2_names = all_names + list(t2_tsch)

    stamp("Q* T2 vanishing window")
    q_t2 = qstar_sparse(t2_cols, t2_van_rows, t2_names)
    stamp(f"T2 van rank {q_t2['rank']} rem {q_t2['n_remaining']} leftover {q_t2['n_leftover_rows']}")

    # image at t=-10: stack remaining columns' (-10,*) after substituting pivots
    # Simpler: Q* on vanishing+ask whether target is consistent.
    # Build augmented vanishing with a dummy 'LAMBDA' column for -p^5 at -10,
    # and include -10 rows.
    t2_aug = {n: dict(t2_cols[n]) for n in t2_names}
    t2_aug["LAMBDA"] = {(-10, d): -v for d, v in p5.items()}
    t2_all_rows = t2_van_rows + t2_lead_rows
    stamp("Q* T2 vanishing+leader (augmented lambda)")
    q_t2_aug = qstar_sparse(t2_aug, t2_all_rows, t2_names + ["LAMBDA"])
    lambda_pivoted = any(p["var"] == "LAMBDA" for p in q_t2_aug["pivots"])
    lambda_free = "LAMBDA" in q_t2_aug["remaining"]
    stamp(f"T2+leader rank {q_t2_aug['rank']} lambda_pivoted={lambda_pivoted} lambda_free={lambda_free}")

    stamp("Q* F/G leader")
    fg_row_order = sorted({k for col in fg_cols.values() for k in col})
    q_fg = qstar_sparse(fg_cols, fg_row_order, t2_names)
    stamp(f"FG leader rank {q_fg['rank']} rem {q_fg['n_remaining']} leftover {q_fg['n_leftover_rows']}")

    stamp("build T3 linear matrix")
    t3_cols = {}
    for name in all_names:
        t3_cols[name] = series_coeff_vec(dT3_of(name), -108, -25)
    # T3 Tschirnhausen: alpha_i(F) G^{9-i}, linearized at base as
    # alpha_i(F0) G0^{9-i}  (the T-coeff columns; products with dF,dG are quadratic)
    # alpha_i = sum_{m=0}^{floor(2i/3)} c_{i,m} F^m, except i=1 Tschirnhausen 0,
    # i=9 leading F^6 already in G^9-F^6.
    t3_tsch_names = []
    for i in range(2, 10):
        degb = (66 * i) // 99  # floor(2i/3)
        for m in range(degb + 1):
            if i == 9 and m == 6:
                continue  # monic leading
            nm = f"T3_a{i}_m{m}"
            t3_tsch_names.append(nm)
            Fm = series_pow(F0, m, tmin=-110, tmax=5, zcap=min(ZCAP, 48)) if m else {0: {0: 1}}
            Gpow = series_pow(G0, 9 - i, tmin=-110, tmax=5, zcap=min(ZCAP, 48)) if (9 - i) else {0: {0: 1}}
            t3_cols[nm] = series_coeff_vec(series_mul(Fm, Gpow, tmin=-110, tmax=5), -108, -25)

    t3_names = all_names + t3_tsch_names
    t3_van_rows = [(t, d) for t in range(-107, -25) for d in range(0, min(ZCAP, 48) + 1)]
    stamp(f"T3 van rows {len(t3_van_rows)} cols {len(t3_names)}")
    # Restrict T3 vanishing to a coarser z-sample if huge: keep all, Q* may be heavy.
    # Cap: only orders that can be reached linearly from remaining slots, but
    # try full first with a time check.
    q_t3 = qstar_sparse(t3_cols, t3_van_rows, t3_names)
    stamp(f"T3 van rank {q_t3['rank']} rem {q_t3['n_remaining']} leftover {q_t3['n_leftover_rows']}")

    t3_aug = {n: dict(t3_cols[n]) for n in t3_names}
    t3_aug["LAMBDA3"] = {(-25, d): -v for d, v in R.items()}
    t3_lead_rows = [(-25, d) for d in range(0, min(ZCAP, 48) + 1)]
    q_t3_aug = qstar_sparse(t3_aug, t3_van_rows + t3_lead_rows, t3_names + ["LAMBDA3"])
    lam3_piv = any(p["var"] == "LAMBDA3" for p in q_t3_aug["pivots"])
    lam3_free = "LAMBDA3" in q_t3_aug["remaining"]
    stamp(f"T3+leader rank {q_t3_aug['rank']} lambda_pivoted={lam3_piv} lambda_free={lam3_free}")

    # Union: FG leader + T2 van + T3 van on shared columns (chart + T2 tsch + T3 tsch)
    stamp("union Q*")
    union_cols = {}
    union_names = sorted(set(t2_names) | set(t3_names))
    for n in union_names:
        v = {}
        for k, c in fg_cols.get(n, {}).items():
            v[("FG",) + (k if isinstance(k, tuple) else (k,))] = c
        # flatten fg keys already tuples
        v = {}
        for k, c in fg_cols.get(n, {}).items():
            v[("FG",) + tuple(k)] = c
        for k, c in t2_cols.get(n, {}).items():
            v[("T2",) + k] = c
        for k, c in t3_cols.get(n, {}).items():
            v[("T3",) + k] = c
        union_cols[n] = v
    union_rows = sorted({k for col in union_cols.values() for k in col})
    stamp(f"union rows {len(union_rows)} cols {len(union_names)}")
    q_un = qstar_sparse(union_cols, union_rows, union_names)
    stamp(f"union rank {q_un['rank']} rem {q_un['n_remaining']} leftover {q_un['n_leftover_rows']}")

    # Which columns actually fire in T2 vanishing (support)
    t2_support = [n for n in t2_names if t2_cols.get(n)]
    fg_support = [n for n in t2_names if fg_cols.get(n)]
    t3_support = [n for n in t3_names if t3_cols.get(n)]

    # Write Singular leftover of T2 linear (should be empty or tiny) plus a
    # quadratic sample: (dF)^2 and (dG)^2 contractions at the first N>=2.
    # For modular GB we emit the linear leftover (if any) and the statement
    # that the simultaneous system is nonlinear for N>=2.
    elapsed = time.perf_counter() - t0

    def slim(q):
        return {
            k: q[k]
            for k in (
                "rank",
                "n_columns",
                "n_remaining",
                "n_leftover_rows",
                "pivots_count",
                "remaining_count",
                "pivots_head",
                "remaining_head",
                "leftover_head",
            )
            if k in q
        }

    result = {
        "type": "DERIVED[LINEARIZED-T2-T3-BRIDGE / STRAIGHT-u=0-a=1]",
        "slice": {"u": 0, "a": 1, "free_h3_tails": 0, "C_A_B_base": 0},
        "base_checks": {
            "F_lead_equals_p9": poly_eq(Flead, p9),
            "G_lead_equals_p6": poly_eq(Glead, p6),
            "p5_deg": max(p5) if p5 else None,
            "R_deg": max(R) if R else None,
            "R_support_head": sorted(R)[:8],
        },
        "column_counts": {
            "chart_all_names": len(all_names),
            "T2_tsch": len(t2_tsch),
            "T3_tsch": len(t3_tsch_names),
            "T2_support_nonzero": len(t2_support),
            "FG_support_nonzero": len(fg_support),
            "T3_support_nonzero": len(t3_support),
        },
        "Qstar": {
            "T2_vanishing_-35_-11": slim(q_t2),
            "T2_vanishing_plus_leader_lambda": slim(q_t2_aug)
            | {"lambda_pivoted": lambda_pivoted, "lambda_free": lambda_free},
            "FG_leaders": slim(q_fg),
            "T3_vanishing": slim(q_t3),
            "T3_vanishing_plus_leader_lambda": slim(q_t3_aug)
            | {"lambda_pivoted": lam3_piv, "lambda_free": lam3_free},
            "union_FG_T2_T3_linear": slim(q_un),
        },
        "linearity": {
            "N_le_1_T2": "linear in chart after T-coeffs fixed (T-coeffs absent)",
            "N_ge_2_T2": "quadratic/cubic in jets; sequential Newton still affine in new jets",
            "p5_in_linear_image": bool(lambda_pivoted) and not lambda_free,
            "R_in_linear_image": bool(lam3_piv) and not lam3_free,
            "interpretation": (
                "If LAMBDA pivots, the linearized (straight) map hits p^5 and the "
                "leader is a linear row on this slice.  If LAMBDA stays free and "
                "leftover rows remain, p^5 is not in the linear image and the "
                "identification is genuinely nonlinear.  If leftover rows exist "
                "with LAMBDA forced to 0, the linearization obstructs the leader "
                "and quadratic jets are required or the slice is empty."
            ),
        },
        "elapsed_seconds": round(elapsed, 3),
        "log": log,
    }

    # persist remaining names for GB / report
    result["T2_remaining_vars"] = q_t2["remaining"]
    result["union_remaining_vars"] = q_un["remaining"]
    result["union_rank"] = q_un["rank"]
    result["union_leftover"] = q_un["n_leftover_rows"]

    (HERE / "residual_linear.json").write_text(
        json.dumps(result, indent=2, sort_keys=True, default=str) + "\n"
    )

    # Singular: linear leftover of the union, if any, plus a small quadratic
    # probe ring.  If leftover is empty, emit a 1-variable dummy that stds to 0
    # (consistent) plus the nonlinear generators we can write in T-coeffs × jets.
    write_singular(q_un, t2_tsch, HERE)
    stamp("done")
    return result


def write_singular(q_un, t2_tsch, here: Path):
    """Emit a Singular script for leftover linear rows (mod p) and a quadratic
    control ideal in the T2 Tschirnhausen face (should not contain p^5).
    """
    # Face-span quadratic control: ring Q[z,c0,a1,a0,b1] / (the face T2 + not p^5)
    # This is a cheap standard-basis job, not the 930-var system.
    # The 930-var nonlinear GB is emitted only if leftover linear rows exist
    # with a small remaining set.
    rem = q_un["remaining"][:80]
    leftover = q_un["leftover"][:200]
    script = here / "work" / "bridge_mod.sing"
    here.joinpath("work").mkdir(exist_ok=True)
    # Face obstruction replay over three primes: T2_face in span of
    # p^{18},p^{15},p^{12},p^9,p^6,p^0 vs target p^5.  Groebner of
    # <face - lambda p^5> in the coeff ring should give lambda=0.
    body = r"""
// Face-span control: T2(p^6,p^9) Tschirnhausen cannot hit p^5.
// Ring: GF(p)[z,c0,a1,a0,b1,lam].
option(redSB);
int pr = PRIME;
ring R = pr,(z,c0,a1,a0,b1,lam),dp;
poly p = z^2*(z+3);
poly F = p^9;
poly G = p^6;
poly T2 = G^3 - F^2 + c0*G^2 + (a1*F + a0)*G + b1*F;
poly target = lam*p^5;
ideal I = T2 - target;
ideal Gstd = std(I);
Gstd;
ideal Elim = eliminate(Gstd, z*c0*a1*a0*b1);
Elim;
exit;
"""
    for prime, name in [(32003, "p32003"), (104729, "p104729"), (1299709, "p1299709")]:
        pth = here / "work" / f"face_{name}.sing"
        pth.write_text(body.replace("PRIME", str(prime)))
    # leftover linear, if small
    if leftover and rem:
        vars_ = ["x" + str(i) for i in range(len(rem))]
        idx = {n: i for i, n in enumerate(rem)}
        lines = [
            "option(redSB);",
            f"int pr = PRIME;",
            f"ring R = pr,({','.join(vars_)}),dp;",
            "ideal I =",
        ]
        polys = []
        for key, rec in leftover[:80]:
            terms = []
            for n, v in rec.items():
                if n not in idx:
                    continue
                num, den = Fraction(v).numerator, Fraction(v).denominator
                terms.append(f"({num})*({den})**(-1)*{vars_[idx[n]]}")
            if terms:
                polys.append("  " + "+".join(terms))
        if not polys:
            polys = ["  0"]
        lines.append(",\n".join(polys) + ";")
        lines += ["ideal Gstd = std(I);", "Gstd;", "exit;"]
        text = "\n".join(lines)
        for prime, name in [(32003, "p32003"), (104729, "p104729"), (1299709, "p1299709")]:
            (here / "work" / f"leftover_{name}.sing").write_text(
                text.replace("PRIME", str(prime))
            )
    (here / "work" / "README.txt").write_text(
        "face_*.sing: Tschirnhausen face vs p^5 (must force lam=0 or 1 in elim).\n"
        "leftover_*.sing: linearized leftover rows if any.\n"
    )


if __name__ == "__main__":
    run()
