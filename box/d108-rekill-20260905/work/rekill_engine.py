#!/usr/bin/env python3
"""D=108 delta=3 split-branch band engine at the Moh Def 5.1(3) D2 radius.

Architecture is a port of the (99,66) sibling driver
box/g9966band-20260903/band_engine.py (stages 0..n: prior local bands + ten
J rows, then per-stage F/G pole bands and Jacobian bands), instantiated on
Skel(108,72,[81,106],{2:7,3:7}) with the corrected radius

Leading-row repair 2026-09-05 (cone-vertex gate §6–§7 / rekill §7):
``pole_coeff`` subtracts the forced face p^12 at F local 96 and p^8 at G
local 64. Every strictly-lower pole row is byte-identical to the old
homogeneous emission. Canonical helper: box/band-leading-fix-20260905/leading_pole.py.

    D2:  t = s^4,  z = pi*s^5          W = 4r+5q     (frozen engine: 4r+6q)
    D1:  s = e^2,  t = e^8, z = e^10*(1+Pi*e)        (frozen: e^12*(1+Pi*e))

Radius-independent data (minor series, pole schedule, Jacobian schedule) is
taken verbatim from the frozen charged engine's continuation_schedule().

FALLACY-v2: qstar_reduce inverts only rationals; nothing is dropped by a floor
except ROWS that are identically absent; every normalization is named in
GAUGE_LEDGER.
"""
from __future__ import annotations
import argparse, hashlib, json, subprocess, time
from collections import defaultdict
from dataclasses import dataclass
from functools import lru_cache
from math import comb, factorial
from pathlib import Path
from typing import Iterable
import sympy as sp

OUT = Path(__file__).resolve().parent
TZ = dict[tuple[int, int], sp.Expr]

# ----------------------------------------------------------------- row datum
N_F, N_G, D2DEG, D3DEG = 108, 72, 36, 9
V2, V3 = 7, 7
DELTA = {1: sp.Rational(3, 8), 2: sp.Rational(1, 4), 3: sp.Integer(-1)}

GAUGE_LEDGER = [
    {"normalization": "major_coordinate z = w-1 (D3 cluster leading coeff 1)",
     "group_element": "y -> lambda*y", "status": "SPENT"},
    {"normalization": "top_K3 = z^7*(1+z)^2, second cluster at w=0",
     "group_element": "y -> y + mu*x", "status": "SPENT"},
    {"normalization": "D2 centre a_1 = 0 (Lemma C: the sole centre exponent)",
     "group_element": "y -> y + a_1", "status": "SPENT (Repair R)"},
    {"normalization": "minor constant jet0", "group_element": "none left",
     "status": "FREE (released by Repair R)"},
    {"normalization": "p = pi^2 - c (no linear term in pi)",
     "group_element": "child generic-point reparametrisation, not in the "
                      "degree<=1 affine group", "status": "SPENT; hostile-tested by the gate"},
    {"normalization": "D1 centre pi = 1 (one of the A_2 = 4 conjugates)",
     "group_element": "choice of Galois conjugate, no group parameter",
     "status": "FREE CHOICE"},
]


def symbol(name): return sp.Symbol(name)


def tz_add(*items):
    out = defaultdict(lambda: sp.Integer(0))
    for it in items:
        for k, v in it.items():
            out[k] += v
    return {k: sp.expand(v) for k, v in out.items() if sp.expand(v) != 0}


def tz_scale(item, scalar):
    return {k: sp.expand(v * scalar) for k, v in item.items() if sp.expand(v * scalar) != 0}


def tz_mul(left, right, max_t):
    out = defaultdict(lambda: sp.Integer(0))
    for (r1, q1), v1 in left.items():
        if r1 > max_t: continue
        for (r2, q2), v2 in right.items():
            if r1 + r2 > max_t: continue
            out[(r1 + r2, q1 + q2)] += v1 * v2
    return {k: sp.expand(v) for k, v in out.items() if sp.expand(v) != 0}


def tz_dt(item):
    return {(r - 1, q): sp.expand(v * r) for (r, q), v in item.items() if r >= 1}


def tz_dz(item):
    return {(r, q - 1): sp.expand(v * q) for (r, q), v in item.items() if q >= 1}


def tz_times_t(item, max_t):
    return {(r + 1, q): v for (r, q), v in item.items() if r + 1 <= max_t}


def substitute_map(expr, subs):
    if not subs or not getattr(expr, "free_symbols", ()): return expr
    if not (expr.free_symbols & subs.keys()): return expr
    return sp.expand(expr.subs(subs, simultaneous=True))


def resolve_map(subs):
    for _ in range(len(subs) + 2):
        changed = False
        for var, rhs in list(subs.items()):
            others = {k: v for k, v in subs.items() if k != var}
            img = substitute_map(rhs, others)
            if img != rhs:
                subs[var] = img; changed = True
        if not changed: break
    return subs


@dataclass
class Pivot:
    label: str; variable: sp.Symbol; coefficient: sp.Rational; rhs: sp.Expr


def qstar_reduce(rows, eligible):
    """Rational-pivot Gauss elimination.  Inverts only elements of QQ*."""
    work = [(l, sp.expand(r)) for l, r in rows if sp.expand(r) != 0]
    zero_rows = len(rows) - len(work)
    available = set(eligible)
    subs, pivots = {}, []
    while True:
        sel = None
        for idx, (label, row) in enumerate(work):
            for var in sorted(row.free_symbols & available, key=str):
                co = sp.diff(row, var)
                rem = sp.expand(row - co * var)
                if co.is_Rational and co != 0 and var not in rem.free_symbols:
                    sel = (idx, label, var, sp.Rational(co), rem); break
            if sel is not None: break
        if sel is None: break
        idx, label, var, co, rem = sel
        rhs = sp.cancel(-rem / co)
        for old in list(subs):
            subs[old] = sp.expand(subs[old].subs(var, rhs))
        subs[var] = rhs
        pivots.append(Pivot(label, var, co, rhs))
        available.discard(var)
        del work[idx]
        reduced = []
        for lb, rw in work:
            img = sp.expand(rw.subs(var, rhs))
            if img == 0: zero_rows += 1
            else: reduced.append((lb, img))
        work = reduced
    resolve_map(subs)
    residual = []
    for label, row in work:
        img = substitute_map(row, subs)
        if img == 0: zero_rows += 1
        else: residual.append((label, img))
    return residual, subs, pivots, zero_rows


# ------------------------------------------------------------ radius profile
class Radius:
    def __init__(self, wz):
        self.wz = wz                       # ord_s(z) at the D2 generic point
        self.W = lambda r, q: 4 * r + wz * q
        self.k3_face = wz * V3             # z^7 is the lowest-weight top term
        self.k2_face = wz * 28             # z^28 likewise
        self.d1_mult = 2                   # e-order = 2*W  (s = e^2, t = e^8)
        # D1 centre is at pi = 1; the K2 D2 face is (pi^A - 1)^V2 with A the
        # Galois orbit size, so its e-order excess is A*... = mult of the face
        # root, i.e. eps = V2 for A_2 = 4 (source) and 8 for the frozen A_2 = 2.
        self.A2gal = 4 if wz == 5 else 2
        self.k2_mult = V2 if wz == 5 else 8
        self.eps = self.k2_mult            # ord_e((pi^A-1)^m at pi=1+Pi*e) = m
        self.k2_d1 = self.d1_mult * self.k2_face + self.eps
        self.tshift = 4                    # (r,q) -> (r+1,q) adds 4 to W

    def k2_face_sites(self):
        """(r,q) with r>=1 on the K2 D2 face, and the forced face values."""
        out = {}
        step = self.wz // 2 if self.wz == 6 else 5
        # solve 4r+wz*q = k2_face with r>=1, q<=36-r
        for r in range(1, 37):
            rem = self.k2_face - 4 * r
            if rem < 0 or rem % self.wz: continue
            q = rem // self.wz
            if q <= 36 - r: out[(r, q)] = None
        # forced values: the face must equal (pi^A - 1)^m * pi^(28-A*m)
        A, m = self.A2gal, self.k2_mult
        for k in range(m + 1):
            q = 28 - A * k
            r = (self.k2_face - self.wz * q) // 4
            if k == 0: continue
            assert (r, q) in out, (r, q)
            out[(r, q)] = sp.Integer((-1) ** k * comb(m, k))
        assert all(v is not None for v in out.values()), out
        return out


SRC = Radius(5)      # Moh Def 5.1(3)
FRZ = Radius(6)      # frozen engine


# -------------------------------------------------------------- h3 and minor
def h3_template(R, cutoff):
    """h3 chart in z=w-1 truncated at D2 weight >= cutoff."""
    out = {(0, 7): sp.Integer(1), (0, 8): sp.Integer(2), (0, 9): sp.Integer(1)}
    variables = []
    for r in range(1, 10):
        vmin = 0 if cutoff is None else max(0, -((-(cutoff - 4 * r)) // R.wz))
        for degree in range(vmin, 10 - r):
            v = symbol(f"Hc_{r}_{degree}"); variables.append(v)
            for q in range(vmin, degree + 1):
                out[(r, q)] = out.get((r, q), sp.Integer(0)) + v * comb(degree - vmin, q - vmin)
    return {k: sp.expand(v) for k, v in out.items()}, variables


def z_to_w(item):
    out = defaultdict(lambda: sp.Integer(0))
    for (r, q), co in item.items():
        for j in range(q + 1):
            out[(r, j)] += co * comb(q, j) * (-1) ** (q - j)
    return {k: sp.expand(v) for k, v in out.items() if sp.expand(v) != 0}


def minor_local_rows(item, max_power, jet0free):
    """w = jet0*t + jet1*t^2 + jet2*t^3 + pi*t^4 (jet0 pinned to 0 if not free).
    Returns {(local_power, pi_degree): coefficient}."""
    wb = z_to_w(item)
    j0, j1, j2 = symbols_jet()
    out = defaultdict(lambda: sp.Integer(0))
    for (r, j), co in wb.items():
        for d in (range(j + 1) if jet0free else [0]):
            for a in range(j - d + 1):
                for b in range(j - d - a + 1):
                    k = j - d - a - b
                    lp = r + d + 2 * a + 3 * b + 4 * k
                    if lp > max_power: continue
                    mn = factorial(j) // (factorial(d) * factorial(a) * factorial(b) * factorial(k))
                    out[(lp, k)] += co * mn * j0 ** d * j1 ** a * j2 ** b
    return {k: sp.expand(v) for k, v in out.items() if sp.expand(v) != 0}


@lru_cache(maxsize=None)
def symbols_jet():
    return sp.symbols("jet0 jet1 jet2")


def minor_incidence(R, cutoff, jet0free):
    """Stage-0 common-h3 incidence: K3 = -t^8*(pi^2-c) + O(t^9)."""
    h3, hvars = h3_template(R, cutoff)
    coll = defaultdict(lambda: sp.Integer(0))
    for key, val in minor_local_rows(h3, 8, jet0free).items():
        coll[key] += val
    c = symbol("c")
    coll[(8, 0)] -= c
    coll[(8, 2)] += 1
    rows = [(f"minor_n{p}_pi{k}", sp.expand(v)) for (p, k), v in sorted(coll.items())]
    return rows, hvars, h3


# ------------------------------------------------------------- major h2 / D1
def build_major_h2(R, h3_reduced, max_t, jet0free):
    """K2 = t^36*h2 with h2 = h3^4 + c2*h3^2 + c3*h3 + c4.

    The free C2/C3/C4 directions are replaced by the OUTPUT coordinates of K2
    at D2 weight > k2_face (a unit-triangular change certified by the
    major-tower pivot pattern; see major_corrected.py leader_failures = 0).
    """
    h3sq = tz_mul(h3_reduced, h3_reduced, max_t)
    h3quad = tz_mul(h3sq, h3sq, max_t)
    face = R.k2_face_sites()
    dvars = {}
    for r in range(1, 37):
        for q in range(37 - r):
            if R.W(r, q) > R.k2_face and q <= 26:
                dvars[(r, q)] = symbol(f"K2c_{r}_{q}")

    def raw(r, q):
        if (r, q) in face: return face[(r, q)]
        if (r, q) in dvars: return dvars[(r, q)]
        if R.W(r, q) <= R.k2_face: return sp.Integer(0)     # D2 strict rows
        return h3quad.get((r, q), sp.Integer(0))

    # h2 D1 rows: e-exponent 2*W+k must vanish for 2*W+k < R.k2_d1.
    rows = []
    weights = sorted({R.W(r, q) for r in range(1, 37) for q in range(37 - r)
                      if R.W(r, q) > R.k2_face and 2 * R.W(r, q) < R.k2_d1})
    for W in weights:
        positions = [(r, q) for r in range(1, 37) for q in range(37 - r) if R.W(r, q) == W]
        for k in range(R.k2_d1 - R.d1_mult * W):
            row = sum(comb(q, k) * raw(r, q) for r, q in positions if q >= k)
            rows.append((f"h2_D1_W{W}_k{k}", sp.expand(row)))
    residual, h2map, pivots, zeros = qstar_reduce(rows, set(dvars.values()))
    k2 = {}
    for j in range(9):          # top_K2 = z^28*(1+z)^8, total degree 36
        k2[(0, 28 + j)] = sp.Integer(comb(8, j))
    for r in range(1, max_t + 1):
        for q in range(37 - r):
            val = substitute_map(sp.expand(raw(r, q)), h2map)
            if val != 0: k2[(r, q)] = val
    meta = {"K2c_count": len(dvars), "h2_D1_raw_rows": len(rows),
            "h2_D1_weights": weights, "h2_D1_pivots": len(pivots),
            "h2_D1_residual": [(l, str(v)) for l, v in residual],
            "h2_D1_zero_rows": zeros,
            "h2_D1_pivot_vars": [str(p.variable) for p in pivots],
            "K2_face_sites": {f"{r}_{q}": str(v) for (r, q), v in sorted(face.items())},
            "K2_D1_leading_e_exponent": R.k2_d1}
    free = set(dvars.values()) - set(h2map)
    return k2, free, meta


if __name__ == "__main__":
    pass


# ------------------------------------------------------------------- outer
def outer_specs(R, nF=N_F, nG=N_G, degh2=D2DEG):
    kf_w, kg_w = 3 * R.k2_face, 2 * R.k2_face
    kf_d1, kg_d1 = 3 * R.k2_d1, 2 * R.k2_d1
    sh, dsh = R.tshift, R.d1_mult * R.tshift
    return {
        "A2": {"degree": nF - degh2 - 1, "W0": kf_w - R.k2_face - sh,
               "threshold": kf_d1 - R.k2_d1 - dsh},
        "A3": {"degree": nF - 1, "W0": kf_w - sh, "threshold": kf_d1 - dsh},
        "B1": {"degree": nG - degh2 - 1, "W0": kg_w - R.k2_face - sh,
               "threshold": kg_d1 - R.k2_d1 - dsh},
        "B2": {"degree": nG - 1, "W0": kg_w - sh, "threshold": kg_d1 - dsh},
    }


def outer_state(R, max_offset):
    specs = outer_specs(R)
    coords, preblock_raw, preblock_rank = {}, 0, 0
    for block, s in specs.items():
        allpos = [(r, q) for r in range(s["degree"] + 1)
                  for q in range(min(D2DEG - 1, s["degree"] - r) + 1)]
        kept = {(r, q): symbol(f"{block}c_{r}_{q}") for r, q in allpos
                if R.W(r, q) >= s["W0"]}
        coords[block] = kept
        preblock_rank += len(allpos) - len(kept)
        labels = set()
        for r, q in allpos:
            if R.W(r, q) >= s["W0"]: continue
            for k in range(q + 1):
                exp = R.d1_mult * R.W(r, q) + k
                if exp < s["threshold"]: labels.add((exp, k))
        preblock_raw += len(labels)

    subs, ledger, all_rows = {}, [], []
    for offset in range(max_offset + 1):
        band_rows, band_vars, by_block = [], set(), {}
        for block, s in specs.items():
            W = s["W0"] + offset
            positions = [p for p in coords[block] if R.W(*p) == W]
            rows = []
            for k in range(max(0, s["threshold"] - R.d1_mult * W)):
                row = sum(comb(q, k) * coords[block][(r, q)]
                          for r, q in positions if q >= k)
                row = substitute_map(sp.expand(row), subs)
                if row != 0:
                    rows.append((f"{block}_D1_s{offset}_k{k}", row))
                    band_vars |= row.free_symbols
            band_rows.extend(rows)
            by_block[block] = {"raw_rows": len(rows), "positions": len(positions)}
        residual, band_map, pivots, zeros = qstar_reduce(band_rows, band_vars)
        assert not residual, residual
        subs.update(band_map); resolve_map(subs)
        all_rows.extend(band_rows)
        ledger.append({"offset": offset, "raw_rows": len(band_rows),
                       "Qstar_pivots": len(pivots), "dependent_zero": zeros,
                       "by_block": by_block,
                       "pivot_variables": [str(p.variable) for p in pivots]})
    resolved = {b: {p: substitute_map(v, subs) for p, v in vals.items()}
                for b, vals in coords.items()}
    allv = set().union(*(set(v.values()) for v in coords.values()))
    return resolved, allv - set(subs), {
        "specs": specs, "weight": f"W={4}*r+{R.wz}*q", "D1_e_weight": f"{R.d1_mult}*W+k",
        "preblock": {"imposed_D2_coordinate_rows": preblock_rank,
                     "redundant_D1_labels_on_deleted_coordinates": preblock_raw,
                     "kept_by_block": {b: len(v) for b, v in coords.items()}},
        "D1_offsets": ledger,
        "D1_cumulative_pivots": sum(x["Qstar_pivots"] for x in ledger),
        "outer_free_count": len(allv - set(subs))}


def outer_effective_tz(coords, block, max_t):
    return {(r + 1, q): v for (r, q), v in coords[block].items()
            if r + 1 <= max_t and v != 0}


def build_FG(k2, outer, max_t):
    k2sq = tz_mul(k2, k2, max_t)
    k2cube = tz_mul(k2sq, k2, max_t)
    KF = tz_add(k2cube, tz_mul(outer_effective_tz(outer, "A2", max_t), k2, max_t),
                outer_effective_tz(outer, "A3", max_t))
    KG = tz_add(k2sq, tz_mul(outer_effective_tz(outer, "B1", max_t), k2, max_t),
                outer_effective_tz(outer, "B2", max_t))
    return KF, KG


def z_band_to_w(item, t_power):
    out = defaultdict(lambda: sp.Integer(0))
    for (r, q), v in item.items():
        if r != t_power: continue
        for k in range(q + 1):
            out[k] += v * comb(q, k) * (-1) ** (q - k)
    return {k: sp.expand(v) for k, v in out.items() if sp.expand(v) != 0}


def jacobian_band(KF, KG, t_power):
    m = t_power
    return z_band_to_w(tz_add(
        tz_scale(tz_mul(KF, tz_dz(KG), m), N_F),
        tz_scale(tz_mul(tz_times_t(tz_dt(KF), m), tz_dz(KG), m), -1),
        tz_scale(tz_mul(tz_dz(KF), KG, m), -N_G),
        tz_mul(tz_dz(KF), tz_times_t(tz_dt(KG), m), m)), t_power)


def jacobian_normalization_control():
    """Frozen record: J[t^1,w^15] = 1712*f0 = (108-1)*16*f0."""
    f = [symbol(f"cf{j}") for j in range(11)]
    g = [symbol(f"cg{j}") for j in range(2)]
    k20 = {(0, 28 + j): sp.Integer(comb(8, j)) for j in range(9)}
    F0 = tz_mul(tz_mul(k20, k20, 1), k20, 1)
    G0 = tz_mul(k20, k20, 1)
    F1, G1 = {}, {}
    for j, var in enumerate(f):
        for q in range(j + 1):
            F1[(1, q)] = F1.get((1, q), 0) + var * comb(j, q)
    for j, var in enumerate(g):
        for q in range(j + 1):
            G1[(1, q)] = G1.get((1, q), 0) + var * comb(j, q)
    J = jacobian_band(tz_add(F0, F1), tz_add(G0, G1), 1)
    lowest = min(J)
    return {"lowest_w_power": lowest, "value": str(J[lowest]),
            "expected": "1712*cf0", "MATCH": sp.expand(J.get(15, 0) - 1712 * f[0]) == 0
                        and lowest == 15}


def all_w_bands(item):
    return {r: z_band_to_w(item, r) for r in sorted({r for r, _ in item})}


def local_rows(item, max_power, jet0free):
    """Minor substitution y = jet0+jet1*t+jet2*t^2+pi*t^3, i.e.
    w = jet0*t+jet1*t^2+jet2*t^3+pi*t^4.  Returns {(local_power, pi_deg): coeff}."""
    j0, j1, j2 = symbols_jet()
    out = defaultdict(lambda: sp.Integer(0))
    for r, poly in all_w_bands(item).items():
        for j, co in poly.items():
            for d in (range(j + 1) if jet0free else [0]):
                for b in range(j - d + 1):
                    for k in range(j - d - b + 1):
                        a = j - d - b - k
                        n = r + d + 2 * a + 3 * b + 4 * k
                        if n > max_power: continue
                        mn = factorial(j) // (factorial(d) * factorial(a) * factorial(b) * factorial(k))
                        out[(n, k)] += co * mn * j0 ** d * j1 ** a * j2 ** b
    return {t: sp.expand(v) for t, v in out.items() if sp.expand(v) != 0}


@lru_cache(maxsize=None)
def raw_minor_support(name, jet0free=False):
    """Frozen charged schedule (band_engine.py:627), extended for jet0 free."""
    degree, pole, shift = (108, 12, 96) if name == "F" else (72, 8, 64)
    tags = set()
    for i in range(degree):
        for j in range(degree - i):
            for d in (range(j + 1) if jet0free else [0]):
                for b in range(j - d + 1):
                    for k in range(j - d - b + 1):
                        a = j - d - b - k
                        e = pole - i + a + 2 * b + 3 * k
                        if e <= 0: tags.add((e + shift, k))
    grouped = defaultdict(list)
    for n, k in sorted(tags): grouped[n].append(k)
    return {n: tuple(v) for n, v in grouped.items()}


# Leading-row repair 2026-09-05. Keep in sync with
# box/band-leading-fix-20260905/leading_pole.py (d108_*).
def leading_pole_power(name):
    if name == "F":
        return 96
    if name == "G":
        return 64
    raise ValueError(name)


@lru_cache(maxsize=None)
def leading_pole_target_table(name):
    """[π^k] of p^12 (F) or p^8 (G), p = π²−c. Gate §6 / rekill §7."""
    pi, c = sp.symbols("pi c")
    p = pi**2 - c
    poly = sp.Poly(sp.expand(p ** (12 if name == "F" else 8)), pi)
    return {int(mon[0]): sp.expand(cf) for mon, cf in poly.terms()}


def pole_coeff(table, n, k, name):
    """F/G pole entry: coefficient minus target at the leading local power."""
    value = table.get((n, k), sp.Integer(0))
    if n != leading_pole_power(name):
        return value
    return sp.expand(value - leading_pole_target_table(name).get(k, 0))


def stage_spec(stage):
    """Frozen continuation_schedule(), D=108 delta=3."""
    pole_power = 4 + stage
    if stage == 0:
        jac = {"t_power": 1, "degree": 177, "w_powers": [25]}
    elif stage == 1:
        jac = {"t_power": 1, "degree": 177, "w_powers": list(range(26, 178))}
    else:
        jac = {"t_power": stage, "degree": 178 - stage,
               "w_powers": list(range(179 - stage))}
    return {"stage": stage, "D1_offset": stage, "pole_local_power": pole_power,
            "pole_exponents": {"F": pole_power - 108, "G": pole_power - 72},
            "jacobian": jac}
