#!/usr/bin/env python3
"""Outer Theorem-1.2 D2/D1 bands for the (108,72) chart, with (99,66) control.

Pure derivation: Moh Thm 1.2 (printed p.149) + Moh (8) A_j/L_j + Prop 6.2
bidegrees.  Specialises the charged (99,66) outer_order_bands recipe.
Field Q, exact Gaussian.  No Singular.  Foreground, under 10 min.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
from math import comb, gcd, lcm
from typing import Iterable
import json
import time

from pathlib import Path

HERE = Path(__file__).resolve().parent


def dim_S(D: int, ycap: int) -> int:
    """dim {A : deg A <= D, deg_y A < ycap} = ycap*(D+1) - ycap*(ycap-1)/2."""
    return ycap * (D + 1) - ycap * (ycap - 1) // 2


def support(D: int, ycap: int) -> list[tuple[int, int]]:
    """(r,q) with r >= 0, 0 <= q < ycap, r+q <= D."""
    return [(r, q) for q in range(ycap) for r in range(D - q + 1)]


def block_count(ydeg_bound: int, totdeg_bound: int) -> int:
    """# monomials x^i y^j with j <= ydeg_bound and i+j <= totdeg_bound."""
    return sum(totdeg_bound - j + 1 for j in range(ydeg_bound + 1))


# ---------------------------------------------------------------------------
# Moh (8): A_j = den(L_j * delta_j), L_j = lcm{den delta_s, ..., den delta_{j+1}}
# Def 5.1(3) radii.  Characteristic data as in Moh p.150.
# ---------------------------------------------------------------------------
class Row:
    def __init__(self, n, m, Ms, Vs, label):
        self.label, self.n, self.m = label, n, m
        full = [-m] + list(Ms)
        self.s = s = len(full)
        self.M = {i + 1: full[i] for i in range(s)}
        d = [n]
        for M in full:
            d.append(gcd(d[-1], M))
        self.d = {i + 1: d[i] for i in range(len(d))}
        self.V = dict(Vs)
        self.V[s + 1] = self.d[s + 1]
        self.ds = self.d[s]
        self.vs = self.V[s]
        self.us = self.ds - self.vs
        self.delta = {i: self._delta(i) for i in range(1, s + 1)}
        self.q = {1: self.M[1]}
        for i in range(2, s + 1):
            self.q[i] = self.M[i] - self.M[i - 1]
        lam = {1: self.q[1] * self.d[1]}
        for i in range(2, s + 1):
            lam[i] = lam[i - 1] + self.q[i] * self.d[i]
        self.lam = lam
        self.mu = {i: lam[i] // self.d[i] for i in range(1, s + 1)}
        self.negmu = {i: -self.mu[i] for i in self.mu}

    def _delta(self, i):
        n, M, d, V, s = self.n, self.M, self.d, self.V, self.s
        num = Fraction(n - M[i])
        den = Fraction(n - M[s] - 1)
        for j in range(i + 1, s + 1):
            num *= V[j] * (n - M[j]) - d[j]
            den *= V[j] * (n - M[j - 1]) - d[j]
        return 1 - num / den

    def L(self, j: int) -> int:
        L = 1
        for i in range(j + 1, self.s + 1):
            L = lcm(L, self.delta[i].denominator)
        return L

    def A(self, j: int) -> int:
        return (self.L(j) * self.delta[j]).denominator

    def major_weight(self) -> dict:
        """D2: t=s^{A2}, w=1+pi s^{Ww}, Ww = A2 L1 delta_1.  D1: t=e^N, N=den(delta_1)."""
        A2, A1 = self.A(2), self.A(1)
        L1, L2 = self.L(1), self.L(2)
        Ww = A2 * L1 * self.delta[1]
        assert Ww.denominator == 1
        N = self.delta[1].denominator
        return {
            "A1": A1,
            "A2": A2,
            "L1": L1,
            "L2": L2,
            "delta_1": str(self.delta[1]),
            "delta_2": str(self.delta[2]),
            "delta_s": str(self.delta[self.s]),
            "Ww": int(Ww),
            "N_D1": N,
            "weight": f"{A2}*r + {int(Ww)}*q",
            "D2_sub": f"t=s^{A2}, w=1+pi*s^{int(Ww)}",
            "D1_sub": f"t=e^{N}, w=1+e^{N * int(Ww) // A2}+Pi*e^{N * int(Ww) // A2 + 1}",
            "E_coeff": N // A2,  # E = (N/A2)*W + k
        }


R99 = Row(99, 66, [77, 97], {3: 8, 2: 8}, "(99,66)")
R108 = Row(108, 72, [81, 106], {3: 7, 2: 7}, "(108,72)")
R64 = Row(64, 48, [52, 62], {3: 3, 2: 3}, "(64,48)")


def outer_block_degrees(n: int, m: int, d2: int, *, fixed_top: bool) -> dict:
    """After (resp. before) fixing the two homogeneous tops of F,G.

    F = h2^{n/d2} + A2 h2 + A3,  G = h2^{m/d2} + B1 h2 + B2
    requires n/d2 = 3 and m/d2 = 2 (the (99,66) and (108,72) shape).
    """
    shift = 1 if fixed_top else 0
    return {
        "A2": {"D": n - d2 - shift, "ycap": d2, "j": 2},
        "A3": {"D": n - shift, "ycap": d2, "j": 3},
        "B1": {"D": m - d2 - shift, "ycap": d2, "j": 1},
        "B2": {"D": m - shift, "ycap": d2, "j": 2},
    }


def exact_q_rref(matrix: list[list[Fraction]]) -> tuple[int, list[int], list[int]]:
    if not matrix:
        return 0, [], []
    n_rows = len(matrix)
    n_cols = len(matrix[0])
    work = [row[:] for row in matrix]
    rank = 0
    pivot_cols: list[int] = []
    pivot_rows: list[int] = []
    used_rows: set[int] = set()
    for col in range(n_cols):
        pivot = None
        for row in range(n_rows):
            if row in used_rows:
                continue
            if work[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            continue
        pivot_val = work[pivot][col]
        inv = Fraction(1, 1) / pivot_val
        work[pivot] = [inv * value for value in work[pivot]]
        for row in range(n_rows):
            if row == pivot:
                continue
            scalar = work[row][col]
            if scalar == 0:
                continue
            work[row] = [
                work[row][c] - scalar * work[pivot][c] for c in range(n_cols)
            ]
        used_rows.add(pivot)
        pivot_cols.append(col)
        pivot_rows.append(pivot)
        rank += 1
        if rank == n_rows:
            break
    for row in range(n_rows):
        if row in used_rows:
            continue
        assert all(value == 0 for value in work[row]), "inhomogeneous D1 obstruction"
    return rank, pivot_cols, pivot_rows


def d1_matrix(
    remain: list[tuple[int, int]], ebound: int, N: int, E_w: int
) -> tuple[list[tuple[int, int]], list[list[Fraction]]]:
    """Rows (e, Pi-power j) with e < ebound; columns the D2-remaining (r,q).

    A term t^r (w-1)^q becomes e^{N r + E_w q} (1+Pi e)^q under the D1 sub.
    """
    slots: list[tuple[int, int]] = []
    slot_index: dict[tuple[int, int], int] = {}
    for r, q in remain:
        base = N * r + E_w * q
        for j in range(q + 1):
            exponent = base + j
            if exponent < ebound:
                key = (exponent, j)
                if key not in slot_index:
                    slot_index[key] = len(slots)
                    slots.append(key)
    matrix = [[Fraction(0)] * len(remain) for _ in slots]
    for col, (r, q) in enumerate(remain):
        base = N * r + E_w * q
        for j in range(q + 1):
            exponent = base + j
            if exponent < ebound:
                matrix[slot_index[(exponent, j)]][col] = Fraction(comb(q, j))
    return slots, matrix


def analyse_block(name: str, spec: dict, wt: dict, *, do_rank: bool = True) -> dict:
    D, ycap, j = spec["D"], spec["ycap"], spec["j"]
    A2, Ww, N = wt["A2"], wt["Ww"], wt["N_D1"]
    positions = support(D, ycap)
    assert len(positions) == dim_S(D, ycap)
    W0 = A2 * (D - j)  # A2*(D + bound_t_D2), bound_t = -j
    ebound = N * D - j  # N*(D + bound_t_D1), bound_t_D1 = -j/N
    vanish = [(r, q) for r, q in positions if A2 * r + Ww * q < W0]
    remain = [(r, q) for r, q in positions if A2 * r + Ww * q >= W0]
    E_w = N * Ww // A2
    d1_support = [(r, q) for r, q in remain if N * r + E_w * q < ebound]
    if do_rank:
        slots, matrix = d1_matrix(remain, ebound, N, E_w)
        rank, pivot_cols, _pivot_rows = exact_q_rref(matrix)
        by_e = Counter(exponent for exponent, _j in slots)
        e_range = [min(by_e), max(by_e)] if by_e else None
        pivot_rq = [list(remain[col]) for col in pivot_cols[:12]]
    else:
        slots, rank, by_e, e_range, pivot_rq = [], None, {}, None, []
        # still count raw slots without building the full matrix
        seen = set()
        for r, q in remain:
            base = N * r + E_w * q
            for jj in range(q + 1):
                exponent = base + jj
                if exponent < ebound:
                    seen.add((exponent, jj))
        slots = list(seen)
        by_e = Counter(e for e, _j in slots)
        e_range = [min(by_e), max(by_e)] if by_e else None
        rank = None
        pivot_rq = []
    return {
        "name": name,
        "D": D,
        "ycap": ycap,
        "thm12_j": j,
        "bound_t_D2": str(-j),
        "bound_t_D1": str(Fraction(-j, N)),
        "D2_s_threshold": W0,
        "D1_e_threshold": ebound,
        "ambient": len(positions),
        "D2_unit_rows": len(vanish),
        "D2_remaining": len(remain),
        "D1_gap_support": len(d1_support),
        "D1_raw_slots": len(slots),
        "D1_rows_by_e": {str(k): by_e[k] for k in sorted(by_e)},
        "D1_Qstar_rank": rank,
        "D1_dependent_slots": (len(slots) - rank) if rank is not None else None,
        "D1_e_range": e_range,
        "remain_r_min": min((r for r, _q in remain), default=None),
        "D1_pivot_columns_rq": pivot_rq,
        "sample_D2_vanish": [list(item) for item in vanish[:5]],
        "sample_D2_remain": [list(item) for item in remain[:5]],
    }


def d1_offsets(blocks: dict[str, dict], wt: dict) -> list[dict]:
    """Engine-style W = W0+offset bands on the D2-remaining support."""
    A2, Ww, N = wt["A2"], wt["Ww"], wt["N_D1"]
    E_coeff = N // A2
    # max offset: any remaining slot with E_base < ebound
    max_off = 0
    for spec in blocks.values():
        W0, ebound, D, ycap, j = (
            spec["D2_s_threshold"],
            spec["D1_e_threshold"],
            spec["D"],
            spec["ycap"],
            spec["thm12_j"],
        )
        for r, q in support(D, ycap):
            W = A2 * r + Ww * q
            if W < W0:
                continue
            if E_coeff * W < ebound:
                max_off = max(max_off, W - W0)
    ledger = []
    for offset in range(max_off + 1):
        raw = 0
        pos_total = 0
        by_block = {}
        # rank of the offset band: build the small binomial matrix on W=W0+offset
        # columns = union of positions at this weight; rows = (block,k)
        cols: list[tuple[str, int, int]] = []
        rows_spec: list[tuple[str, int, list[int]]] = []
        for name, spec in blocks.items():
            W0, ebound, D, ycap = (
                spec["D2_s_threshold"],
                spec["D1_e_threshold"],
                spec["D"],
                spec["ycap"],
            )
            W = W0 + offset
            positions = [
                (r, q)
                for r, q in support(D, ycap)
                if A2 * r + Ww * q == W
            ]
            kmax = max(0, ebound - E_coeff * W)
            # k = 0 .. kmax-1
            n_rows = 0
            for k in range(kmax):
                if any(q >= k for r, q in positions):
                    n_rows += 1
                    col_idx = []
                    for r, q in positions:
                        col_idx.append(comb(q, k) if q >= k else 0)
                    rows_spec.append((name, k, col_idx))
            by_block[name] = {"raw_rows": n_rows, "positions": len(positions)}
            raw += n_rows
            pos_total += len(positions)
            for r, q in positions:
                cols.append((name, r, q))
        # build matrix: one column per (block,r,q) at this offset, one row per (block,k)
        # blocks don't mix, so rank is the sum of per-block ranks
        rank = 0
        for name, spec in blocks.items():
            W0, ebound, D, ycap = (
                spec["D2_s_threshold"],
                spec["D1_e_threshold"],
                spec["D"],
                spec["ycap"],
            )
            W = W0 + offset
            positions = [
                (r, q)
                for r, q in support(D, ycap)
                if A2 * r + Ww * q == W
            ]
            if not positions:
                continue
            kmax = max(0, ebound - E_coeff * W)
            mat = []
            for k in range(kmax):
                row = [Fraction(comb(q, k) if q >= k else 0) for r, q in positions]
                if any(v != 0 for v in row):
                    mat.append(row)
            if mat:
                rk, _, _ = exact_q_rref(mat)
                rank += rk
        ledger.append(
            {
                "offset": offset,
                "raw_rows": raw,
                "Qstar_rank": rank,
                "dependent": raw - rank,
                "positions": pos_total,
                "by_block": by_block,
            }
        )
    return ledger


def h3_strict_space(d3: int, vs: int, wt: dict, *, r_max: int | None = None) -> dict:
    """vmin cut: remaining t^r (w-1)^q after the D2 face of h3.

    Face weight Ww * vs (leading (w-1)^{vs} at r=0).  Theorem 1.2 is >=, so
    the engine keeps W >= face+1.  r runs 1..d3 (unfixed degree-d3 chart,
    r=0 reserved for the fixed top), cap = d3 - r.
    """
    A2, Ww = wt["A2"], wt["Ww"]
    face = Ww * vs
    r_hi = d3 if r_max is None else r_max
    variables = []
    vmin_of = {}
    for r in range(1, r_hi + 1):
        cap = d3 - r
        # ceil((face+1 - A2 r)/Ww)
        num = face + 1 - A2 * r
        vmin = 0 if num <= 0 else (num + Ww - 1) // Ww
        vmin = max(0, vmin)
        vmin_of[r] = vmin
        for d in range(vmin, cap + 1):
            variables.append((r, d))
    # unwanted equality sites on the face, inside the disk, other than the top
    equality = []
    for r in range(0, r_hi + 1):
        # A2 r + Ww q = face, q integer, 0 <= q <= d3-r
        if (face - A2 * r) % Ww == 0:
            q = (face - A2 * r) // Ww
            if 0 <= q <= d3 - r:
                equality.append((r, q, A2 * r + Ww * q))
    below = 0
    for r in range(0, r_hi + 1):
        cap = d3 - r
        for q in range(0, cap + 1):
            if A2 * r + Ww * q < face:
                below += 1
    return {
        "face_weight": face,
        "strict_threshold": face + 1,
        "n_strict_variables": len(variables),
        "vmin": {str(r): vmin_of[r] for r in sorted(vmin_of)},
        "variables_sample": variables[:12],
        "equality_sites_in_disk": [list(x) for x in equality],
        "n_below_face": below,
        "formula_vmin": f"max(0, ceil(({face}+1 - {A2}*r)/{Ww}))",
    }


def h2_D1_window(d2: int, vs: int, d_s: int, wt: dict) -> dict:
    """Projected h2 D2 remaining and the D1 gap (engine W=97 k<=4, W=98 k<=1 at (99,66))."""
    A2, Ww, N = wt["A2"], wt["Ww"], wt["N_D1"]
    maj = vs * d2 // d_s  # major multiplicity of h2 at D2
    face = Ww * maj
    # fixed-top h2 lives in S(d2-1, d2); engine also enumerates r=1..d2, q < d2-r+? 
    # Charged: r in 1..33, q in 0..33-r, W>=97  (D=32 after fixing, plus r=d2 at the top).
    # Use the same convention: r=1..d2, q=0..d2-r (so r+q <= d2), W >= face+1.
    remain = [
        (r, q)
        for r in range(1, d2 + 1)
        for q in range(d2 - r + 1)
        if A2 * r + Ww * q >= face + 1
    ]
    ebound = N * d2 - 1  # ord h2(D1) = -1/N, K2=t^{d2} h2
    E_coeff = N // A2
    E_w = N * Ww // A2
    by_W = Counter(A2 * r + Ww * q for r, q in remain)
    d1_rows = []
    for W in sorted(by_W):
        kmax = max(0, ebound - E_coeff * W)
        if kmax <= 0:
            continue
        positions = [(r, q) for r, q in remain if A2 * r + Ww * q == W]
        d1_rows.append(
            {
                "W": W,
                "k_range": f"0..{kmax-1}",
                "kmax_inclusive": kmax - 1,
                "n_positions": len(positions),
                "n_rows": kmax,
            }
        )
    # low-q K2c count: q <= (k2-1)*d3 wait; charged q<=21 = 33-12? 
    # 21 = 11+10, the C2/C3 y-range.  Left as a count of remain with a q-cap
    # equal to d2 - d3 (the C-block y-room below h2's top).  Not used as a rank.
    return {
        "major_multiplicity_D2": maj,
        "face_weight": face,
        "strict_threshold": face + 1,
        "n_strict_r_ge_1": len(remain),
        "ebound": ebound,
        "D1_active_W": d1_rows,
        "n_D1_rows": sum(item["n_rows"] for item in d1_rows),
        "note": (
            "D1 window is empty iff every remaining W already has "
            f"(N/A2)*W >= ebound, i.e. the D2 cut implies the D1 bound"
        ),
    }


def tower_unfixed(row: Row) -> dict:
    n, m, d2, d3 = row.n, row.m, row.d[2], row.d[3]
    k2, kF, kG = d2 // d3, n // d2, m // d2
    blocks = {"H": block_count(d3 - 1, d3)}
    for i in range(2, k2 + 1):
        blocks[f"C{i}"] = block_count(d3 - 1, i * d3)
    blocks["A2"] = block_count(d2 - 1, (kF - 1) * d2)
    blocks["A3"] = block_count(d2 - 1, kF * d2)
    blocks["B1"] = block_count(d2 - 1, (kG - 1) * d2)
    blocks["B2"] = block_count(d2 - 1, kG * d2)
    tot = sum(blocks.values())
    monic = (n + 1) * (n + 2) // 2 + (m + 1) * (m + 2) // 2 - 2
    return {
        "k_h2": k2,
        "k_F": kF,
        "k_G": kG,
        "blocks": blocks,
        "total": tot,
        "monic_array": monic,
        "exact": tot == monic,
        "after_fixing_tops": tot - (n + m),
    }


def prop62_box(row: Row) -> dict:
    """Moh Prop 6.2: (deg_y, deg_z) = (v_s, u_s) * (degree)/d_s."""
    vs, us, ds = row.vs, row.us, row.ds
    out = {}
    for name, deg in (
        ("F", row.n),
        ("G", row.m),
        ("T2", row.negmu[2]),
        ("h2", row.d[2]),
        ("h3", row.d[3]),
    ):
        dy, dz = vs * deg // ds, us * deg // ds
        out[name] = {
            "deg": deg,
            "deg_y": dy,
            "deg_z": dz,
            "corner": f"y^{dy} z^{dz}",
            "box": (dy + 1) * (dz + 1),
        }
    out["F_plus_G_box"] = out["F"]["box"] + out["G"]["box"]
    return out


def h3_adic_k2_4() -> dict:
    """Theorem 1.2 rows for h2 = h3^4 + C2 h3^2 + C3 h3 + C4, F=h2^3+A2 h2+A3,
    G=h2^2+B1 h2+B2.  Identities F_1=G_1=0 (Tschirnhausen, no h3^3 in h2).
    Floor/attainment: products of >= remain >= ; 0 new outer coordinates.
    """
    import sympy as sp

    h3, C2, C3, C4, A2, A3, B1, B2 = sp.symbols("h3 C2 C3 C4 A2 A3 B1 B2")
    h2 = h3 ** 4 + C2 * h3 ** 2 + C3 * h3 + C4
    F = sp.expand(h2 ** 3 + A2 * h2 + A3)
    G = sp.expand(h2 ** 2 + B1 * h2 + B2)
    # leading F ~ h3^{12}, G ~ h3^8
    Fpoly = sp.Poly(F, h3)
    Gpoly = sp.Poly(G, h3)
    assert Fpoly.degree() == 12 and Gpoly.degree() == 8
    F_j = {12 - deg: str(Fpoly.coeff_monomial(h3 ** deg)) for deg in range(13)}
    G_j = {8 - deg: str(Gpoly.coeff_monomial(h3 ** deg)) for deg in range(9)}
    # identities
    assert Fpoly.coeff_monomial(h3 ** 11) == 0  # F_1
    assert Gpoly.coeff_monomial(h3 ** 7) == 0  # G_1
    return {
        "type": "DERIVED[h3-adic D2 bounds after chart expansion, k2=4]",
        "h2": "h3^4 + C2*h3^2 + C3*h3 + C4",
        "F": "h2^3 + A2*h2 + A3",
        "G": "h2^2 + B1*h2 + B2",
        "F_j": {str(k): F_j[k] for k in sorted(F_j)},
        "G_j": {str(k): G_j[k] for k in sorted(G_j)},
        "identities": ["F_1=0", "G_1=0"],
        "new_outer_pivots": 0,
        "reason": (
            "ord C2>=-1/2, ord C3>=-3/4, ord C4>=-1 follow from Thm 1.2 at D2 "
            "with base h3, ord h3=-1/4; ord A2>=-2, ord A3>=-3, ord B1>=-1, "
            "ord B2>=-2 are the outer D2-h2 unit rows.  Each F_j, G_j is a "
            "polynomial in those blocks; the Thm-1.2 lower bound follows by "
            "addition of lower bounds.  Not independent coordinates."
        ),
    }


def inner_cuts(row: Row, wt: dict, *, fixed_top: bool) -> dict:
    """D2 weight cuts on H, C2, C3, (C4).  ord h3(D2) = -d3/d2 = -1/k2."""
    d2, d3 = row.d[2], row.d[3]
    k2 = d2 // d3
    A2, Ww = wt["A2"], wt["Ww"]
    ord_h3 = Fraction(-1, k2)
    shift = 1 if fixed_top else 0
    # h2 = P^{k2} + C2 P^{k2-2} + ... + C_{k2}
    # C_i multiplies P^{k2-i}, Thm 1.2 j = i, deg <= i*d3 (-shift)
    specs = {"H": {"D": d3 - shift, "ycap": d3, "j_ord": -ord_h3}}  # h3 itself: ord >= ord_h3
    # For H, bound_t = ord_h3 = -1/k2, W0 = A2*(D + bound_t)
    # C_i: j = i, bound = i*ord_h3
    for i in range(2, k2 + 1):
        specs[f"C{i}"] = {
            "D": i * d3 - shift,
            "ycap": d3,
            "j_ord": -i * ord_h3,
        }
    out = {}
    for name, spec in specs.items():
        D, ycap = spec["D"], spec["ycap"]
        bound = -spec["j_ord"] if name != "H" else ord_h3
        # W0 = A2 * (D + bound_t).  bound_t is a Fraction.
        W0_frac = A2 * (D + bound)
        assert W0_frac.denominator == 1, (name, W0_frac)
        W0 = int(W0_frac)
        positions = support(D, ycap)
        vanish = sum(1 for r, q in positions if A2 * r + Ww * q < W0)
        remain = len(positions) - vanish
        out[name] = {
            "D": D,
            "ycap": ycap,
            "bound_t_D2": str(bound),
            "D2_s_threshold": W0,
            "ambient": len(positions),
            "D2_unit_rows": vanish,
            "D2_remaining": remain,
        }
    return out


def h2_equality_sites(row: Row, wt: dict) -> dict:
    """(pi^{k2}-1)^{v_s} face slots that fit in deg <= d2.  Calibrated on (99,66)."""
    d2, d3, vs = row.d[2], row.d[3], row.vs
    k2 = d2 // d3
    A2, Ww = wt["A2"], wt["Ww"]
    # r = (Ww * k2 / A2) * k = (L1 delta_1 k2) k
    step_r = (Ww * k2) // A2
    sites = []
    outside = []
    for k in range(0, vs + 1):
        r = step_r * k
        q = k2 * (vs - k)
        coef = ((-1) ** k) * comb(vs, k)
        rec = {"k": k, "r": r, "q": q, "coeff": coef, "r_plus_q": r + q}
        if r >= 0 and q >= 0 and r + q <= d2:
            sites.append(rec)
        else:
            outside.append(rec)
    return {
        "face_polynomial": f"(pi^{k2} - 1)^{vs}",
        "in_disk": sites,
        "outside_S(d2,d2)": outside,
        "n_in_disk_beyond_leading": max(0, len(sites) - 1),
        "calibration": (
            "reproduces (99,66) equality {(4k, 24-3k): (-1)^k C(8,k), 1<=k<=8}"
            if row.label == "(99,66)"
            else "same rule; out-of-disk k are not ambient coordinates"
        ),
    }


def run_row(row: Row, *, fixed_top: bool, do_rank: bool, expected=None) -> dict:
    assert row.n // row.d[2] == 3 and row.m // row.d[2] == 2, row.label
    wt = row.major_weight()
    specs = outer_block_degrees(row.n, row.m, row.d[2], fixed_top=fixed_top)
    reports = {
        name: analyse_block(name, spec, wt, do_rank=do_rank)
        for name, spec in specs.items()
    }
    d2_total = sum(rep["D2_unit_rows"] for rep in reports.values())
    d1_raw = sum(rep["D1_raw_slots"] for rep in reports.values())
    remain_total = sum(rep["D2_remaining"] for rep in reports.values())
    ambient = sum(rep["ambient"] for rep in reports.values())
    d1_rank = (
        sum(rep["D1_Qstar_rank"] for rep in reports.values())
        if do_rank
        else None
    )
    offsets = d1_offsets(reports, wt) if do_rank else []
    if expected and do_rank:
        assert d2_total == expected["D2_unit_rows"], (d2_total, expected)
        assert d1_rank == expected["D1_Qstar_rank"], (d1_rank, expected)
        assert ambient == expected["outer_ambient"], (ambient, expected)
    h3s = h3_strict_space(row.d[3], row.vs, wt)
    h2w = h2_D1_window(row.d[2], row.vs, row.ds, wt)
    eq = h2_equality_sites(row, wt)
    inner = inner_cuts(row, wt, fixed_top=fixed_top)
    tower = tower_unfixed(row)
    box = prop62_box(row)
    return {
        "label": row.label,
        "n": row.n,
        "m": row.m,
        "d": [row.d[i] for i in range(1, row.s + 2)],
        "us": row.us,
        "vs": row.vs,
        "negmu": {str(i): row.negmu[i] for i in row.negmu},
        "weight": wt,
        "fixed_top": fixed_top,
        "blocks": reports,
        "totals": {
            "outer_ambient": ambient,
            "D2_unit_rows": d2_total,
            "D2_remaining": remain_total,
            "D1_raw_slots": d1_raw,
            "D1_Qstar_rank": d1_rank,
            "D1_dependent_slots": (d1_raw - d1_rank) if d1_rank is not None else None,
            "new_pivots_D2_plus_D1": (d2_total + d1_rank) if d1_rank is not None else None,
        },
        "D1_offsets": offsets,
        "h3_strict": h3s,
        "h2_D1": h2w,
        "h2_equality": eq,
        "inner_D2": inner,
        "tower": tower,
        "prop62": box,
    }


def general_formula() -> dict:
    return {
        "scope": (
            "Outer A,B of the Tschirnhausen tower F=h2^{n/d2}+A2 h2+A3, "
            "G=h2^{m/d2}+B1 h2+B2, which requires n/d2=3, m/d2=2.  "
            "A2,A1,Ww come from Moh (8) on the row's radii, not from (n,m,d2,d3) alone."
        ),
        "S": "S(D,d2) = {deg <= D, deg_y < d2}, dim = d2*(D+1)-d2*(d2-1)/2",
        "fixed_top_degrees": {
            "A2": "D = n-d2-1, j=2",
            "A3": "D = n-1,     j=3",
            "B1": "D = m-d2-1, j=1",
            "B2": "D = m-1,     j=2",
        },
        "Moh8": (
            "L_j = lcm{den delta_s, ..., den delta_{j+1}}, "
            "A_j = den(L_j * delta_j), Ww = A_2 * L_1 * delta_1, "
            "N = den(delta_1).  On the three charged rows N = A1*A2."
        ),
        "weight": "W(r,q) = A2*r + Ww*q",
        "D2_sub": "t=s^{A2}, w=1+pi s^{Ww}",
        "D1_sub": "t=e^N, w=1+e^{N*Ww/A2}+Pi e^{N*Ww/A2+1}",
        "ord_h2_D2": -1,
        "ord_h2_D1": "-1/N",
        "Thm12_outer": "ord A_j >= j * ord h2,  ord B_j >= j * ord h2  (j as above)",
        "D2_W0": "W0 = A2 * (D - j)     [vanish W < W0; equality face is not a row]",
        "D1_E0": "E0 = N*D - j          [E = (N/A2)*W + k < E0 on the D2-remaining]",
        "D2_rank": "rank = count (unit coordinate vanishings)",
        "D1_rank": "Q* rank of the binomial matrix (e,k) vs remaining (r,q)",
        "expected_outer_rank": "D2_unit_rows + D1_Qstar_rank",
        "h3_vmin": "vmin(r) = max(0, ceil((Ww*v_s + 1 - A2*r)/Ww)), r=1..d3, cap=d3-r",
        "inner_ord_h3_D2": "-d3/d2 = -1/k2",
        "h3_in_h2": (
            "h2 = h3^{k2} + C2 h3^{k2-2} + ... + C_{k2} (Tschirnhausen drops h3^{k2-1}); "
            "Thm 1.2: ord C_i >= i * ord h3"
        ),
    }


def row64_statement() -> dict:
    wt = R64.major_weight()
    n, m, d2, d3 = R64.n, R64.m, R64.d[2], R64.d[3]
    return {
        "label": R64.label,
        "d": [R64.d[i] for i in range(1, R64.s + 2)],
        "us": R64.us,
        "vs": R64.vs,
        "k_F": n // d2,
        "k_G": m // d2,
        "k_h2": d2 // d3,
        "weight": wt,
        "tower_shape": (
            "n/d2=4, m/d2=3: F=h2^4+A2 h2^2+A3 h2+A4, G=h2^3+B1 h2+B2 "
            "(not the A2/A3/B1/B2 3+2 chart).  Outer-band naming of (99,66) "
            "does not apply.  u_s=1: T2,T3 bridge trivial (Xu Prop 7.3 / Moh Prop 4.4)."
        ),
        "W0_formula_still": (
            "The same W=A2 r+Ww q, W0=A2*(D-j), E0=N*D-j rules apply to each "
            "Tschirnhausen block of F,G once the (D,j) of that block is named.  "
            "They are not consumed by a (108,72) engine."
        ),
        "N_equals_A1A2": wt["N_D1"] == wt["A1"] * wt["A2"],
    }


def main() -> None:
    t0 = time.perf_counter()
    formula = general_formula()
    expected_9966 = {
        "outer_ambient": 6600,
        "D2_unit_rows": 5598,
        "D1_Qstar_rank": 176,
        "new_pivots_D2_plus_D1": 5774,
    }
    c9966 = run_row(R99, fixed_top=True, do_rank=True, expected=expected_9966)
    # charged D1 offset raw/rank
    off_raw = [item["raw_rows"] for item in c9966["D1_offsets"]]
    off_rk = [item["Qstar_rank"] for item in c9966["D1_offsets"]]
    charged_off_raw = [64, 52, 40, 29, 20, 11, 6, 3]
    charged_off_rk = [41, 38, 33, 25, 19, 11, 6, 3]
    c9966["offset_replay"] = {
        "raw": off_raw,
        "rank": off_rk,
        "raw_matches_charged": off_raw == charged_off_raw,
        "rank_matches_charged": off_rk == charged_off_rk,
    }
    assert off_raw == charged_off_raw, off_raw
    assert off_rk == charged_off_rk, off_rk
    assert c9966["h3_strict"]["n_strict_variables"] == 21
    assert c9966["h2_equality"]["n_in_disk_beyond_leading"] == 8
    assert c9966["tower"]["total"] == 7326
    assert c9966["h2_D1"]["n_D1_rows"] == 7  # k=0..4 at W=97 plus k=0..1 at W=98

    c108 = run_row(R108, fixed_top=True, do_rank=True)
    assert c108["tower"]["total"] == 8694, c108["tower"]
    assert c108["tower"]["exact"]
    h3adic = h3_adic_k2_4()
    s64 = row64_statement()

    # (99,66) inner remaining 21 is the h3_template assert
    out = {
        "type": "EXACT-OUTER-THM12-D2-D1 / (108,72) with (99,66) control",
        "field": "Q",
        "face_policy": "Theorem 1.2 is >= ; equality face is not a row",
        "general_formula": formula,
        "control_9966": {
            "totals": c9966["totals"],
            "weight": c9966["weight"],
            "D1_offsets_raw": off_raw,
            "D1_offsets_rank": off_rk,
            "h3_strict_variables": c9966["h3_strict"]["n_strict_variables"],
            "h2_D1_rows": c9966["h2_D1"]["n_D1_rows"],
            "h2_D1_active_W": c9966["h2_D1"]["D1_active_W"],
            "offset_replay": c9966["offset_replay"],
            "blocks": {
                k: {
                    kk: c9966["blocks"][k][kk]
                    for kk in (
                        "D",
                        "D2_s_threshold",
                        "D1_e_threshold",
                        "ambient",
                        "D2_unit_rows",
                        "D2_remaining",
                        "D1_raw_slots",
                        "D1_Qstar_rank",
                        "D1_dependent_slots",
                        "D1_e_range",
                        "remain_r_min",
                    )
                }
                for k in c9966["blocks"]
            },
            "reproduces_charged": (
                c9966["totals"]["D2_unit_rows"] == 5598
                and c9966["totals"]["D1_Qstar_rank"] == 176
                and c9966["totals"]["new_pivots_D2_plus_D1"] == 5774
                and c9966["offset_replay"]["raw_matches_charged"]
                and c9966["offset_replay"]["rank_matches_charged"]
            ),
        },
        "row_108": {
            "weight": c108["weight"],
            "totals": c108["totals"],
            "blocks": c108["blocks"],
            "D1_offsets": c108["D1_offsets"],
            "h3_strict": c108["h3_strict"],
            "h2_D1": c108["h2_D1"],
            "h2_equality": c108["h2_equality"],
            "inner_D2": c108["inner_D2"],
            "tower": c108["tower"],
            "prop62": c108["prop62"],
            "h3_adic": h3adic,
        },
        "row_64": s64,
        "elapsed_seconds": round(time.perf_counter() - t0, 4),
    }
    path = HERE / "outer_weights.json"
    path.write_text(json.dumps(out, indent=2, sort_keys=True, default=str) + "\n")
    print(json.dumps(
        {
            "elapsed": out["elapsed_seconds"],
            "9966_ok": out["control_9966"]["reproduces_charged"],
            "9966_totals": out["control_9966"]["totals"],
            "108_totals": out["row_108"]["totals"],
            "108_weight": out["row_108"]["weight"],
            "108_h3_strict": out["row_108"]["h3_strict"]["n_strict_variables"],
            "108_h2_D1_rows": out["row_108"]["h2_D1"]["n_D1_rows"],
            "108_D1_offsets_raw": [x["raw_rows"] for x in out["row_108"]["D1_offsets"]],
            "108_D1_offsets_rank": [x["Qstar_rank"] for x in out["row_108"]["D1_offsets"]],
            "108_tower": out["row_108"]["tower"]["total"],
            "64_weight": out["row_64"]["weight"]["weight"],
        },
        indent=2,
    ))


if __name__ == "__main__":
    main()
