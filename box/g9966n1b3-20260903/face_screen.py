#!/usr/bin/env python3
"""Exhaustive mechanical split-face screen for the (99,66) remainder skeletons.

The charged batch-2 triage only VERIFIED a hardcoded survivor list.  This screen
ENUMERATES every (delta, root-multiplicity partition) pair in the Prop 6.1
detector window and decides each one exactly, then reconstructs q for survivors
and checks the face residual is exactly zero.

Face identity (charged: batch-2 report, "Exact face equation and
parametrizations"; Xu 2016 Cor 7.5 face level):

    X = u_s*delta - v_s,  a = W*X - 1 + delta,
    a*q*p' - X*p*q' = (v_s-u_s)*p^(W+1),
    deg p = u_s  (root multiplicities = the split partition),  deg q = W*u_s+1.

W = (3n - 2*M2)/d_3 = (297-2*M2)/11 at n=99, d_3=11 (fits every charged chart).

Two exact necessary conditions are enumerated:

(G) GALOIS.  delta=P/Q in lowest terms.  Substituting x^(1/Q) -> zeta_Q x^(1/Q)
    permutes the u_s minor roots, so the multiset of face roots is stable under
    z -> zeta_Q^P z, i.e. under multiplication by a primitive Q-th root of 1.
    Nonzero roots therefore lie in orbits of size exactly Q with equal
    multiplicity; only z=0 may be fixed.

(L) LOCAL EXPONENT.  At a root of p of multiplicity lam, matching the lowest
    order of both sides of the face identity forces the multiplicity nu of q to
    satisfy either  X*nu = a*lam  (nu = k*lam, needs k*lam in Z), or exactly
    nu = lam*W + 1.  Summing over roots with deg q = W*u+1 gives
        #(high roots) <= t*(sum of low multiplicities) + 1,   t = W - k.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import gcd
import itertools, json
from pathlib import Path
import sympy as sp

z = sp.Symbol("z")
HERE = Path("/home/ubuntu/jc2/box/g9966n1b3-20260903")


def partitions(total, cap=None):
    if total == 0:
        yield ()
        return
    high = total if cap is None else min(total, cap)
    for first in range(high, 0, -1):
        for tail in partitions(total - first, first):
            yield (first,) + tail


def detector_orders(u, v):
    if u < 2:
        return []
    ceiling = F(v, u)
    out = set()
    for den in range(1, u + 1):
        for num in range(den + 1, 10 * v + 1):
            val = F(num, den)
            if val >= ceiling:
                break
            if gcd(num, den) == 1:
                out.add(val)
    return sorted(out)


def galois_patterns(part, Q):
    """All ways the multiplicity multiset `part` can arise from a zeta_Q-stable
    root multiset.  Returns a list of (mult_at_zero, [orbit multiplicities])."""
    rest = sorted(part, reverse=True)
    found = []
    for zero_choice in ({None} | set(rest)):
        pool = list(rest)
        if zero_choice is not None:
            pool.remove(zero_choice)
        # the remaining multiplicities must group into orbits of Q equal values
        pool_sorted = sorted(pool)
        if len(pool_sorted) % Q:
            continue
        ok, orbits, i = True, [], 0
        while i < len(pool_sorted):
            block = pool_sorted[i:i + Q]
            if len(set(block)) != 1:
                ok = False
                break
            orbits.append(block[0])
            i += Q
        if ok:
            found.append((zero_choice, sorted(orbits, reverse=True)))
    uniq = []
    for f in found:
        if f not in uniq:
            uniq.append(f)
    return uniq


def local_exponent_ok(part, k, t, W, u):
    """Enumerate low/high assignments; return the admissible ones."""
    D = W * u + 1
    good = []
    for mask in itertools.product([0, 1], repeat=len(part)):   # 1 = high
        nus, ok = [], True
        for lam, hi in zip(part, mask):
            if hi:
                nus.append(lam * W + 1)
            else:
                val = k * lam
                if val.denominator != 1 or val < 0:
                    ok = False
                    break
                nus.append(int(val))
        if ok and sum(nus) <= D:
            good.append({"mask": list(mask), "nu": nus, "sum_nu": sum(nus), "deg_q": D})
    return good


def build_p(part, zero_mult, orbits, Q, cvals):
    """Canonical zeta_Q-stable p with the requested multiplicity pattern."""
    p = sp.Integer(1)
    if zero_mult is not None:
        p *= z ** zero_mult
    for mult, c in zip(orbits, cvals):
        p *= (z ** Q - c) ** mult
    return sp.expand(p)


def face_residual(u, v, W, delta, p, q):
    X = F(u) * delta - F(v)
    a = F(W) * X - 1 + delta
    aq = sp.Rational(a.numerator, a.denominator)
    Xq = sp.Rational(X.numerator, X.denominator)
    return sp.expand(aq * q * sp.diff(p, z) - Xq * p * sp.diff(q, z)
                     - sp.Integer(v - u) * sp.expand(p ** (W + 1)))


def construct_q(u, v, W, delta, p, Q):
    """Explicit face solution when it exists: q = w^A*(C + c0*int w^B dz) with
    p = w^g, g = den(k) (g=1 covers the integral-exponent case)."""
    X = F(u) * delta - F(v)
    a = F(W) * X - 1 + delta
    k = a / X
    t = F(W) - k
    g = k.denominator
    if t.denominator != g:
        return None, {"note": "k and t denominators disagree"}
    root = sp.Poly(p, z)
    if g > 1:
        try:
            w = sp.Poly(sp.real_root(1, 1), z)                   # placeholder
        except Exception:
            w = None
        # exact g-th root of the monic polynomial p, by factorisation
        facs = sp.factor_list(p)
        w = sp.Integer(facs[0])
        for base, expo in facs[1]:
            if expo % g:
                return None, {"note": f"p is not a perfect {g}-th power"}
            w = w * base ** (expo // g)
        w = sp.expand(w)
    else:
        w = p
    A = int(k * g)
    B = int(t * g)
    if A < 0 or B < 0:
        return None, {"note": "negative exponent"}
    c0 = -sp.Rational((v - u), 1) / sp.Rational(X.numerator, X.denominator)
    C = sp.Symbol("Cface")
    integ = sp.integrate(sp.expand(w ** B), z)
    q = sp.expand(sp.expand(w ** A) * (C + c0 * integ))
    return q, {"w": str(sp.factor(w)), "A": A, "B": B, "c0": str(c0)}


SKELETONS = {
    "S1": {"u": 2, "v": 9, "M2": -22},
    "S2": {"u": 4, "v": 7, "M2": 22},
    "S3": {"u": 4, "v": 7, "M2": 22},
    "S4": {"u": 3, "v": 8, "M2": 22},
    "S7": {"u": 4, "v": 7, "M2": 77},
}


def W_of(M2):
    num = 297 - 2 * M2
    assert num % 11 == 0, M2
    return num // 11


def main():
    out = {"schema": "jc2.g9966n1b3.face-screen/v2",
           "face_identity": "a*q*p' - X*p*q' = (v-u)*p^(W+1); X=u*delta-v; a=W*X-1+delta",
           "W_closed_form": "W=(3n-2*M2)/d_3=(297-2*M2)/11",
           "necessary_conditions": ["G: zeta_Q-stable root multiset (Q=den(delta))",
                                    "L: nu=k*lam or nu=lam*W+1 at each root, sum nu <= W*u+1"],
           "rows": {}}
    for name, dat in SKELETONS.items():
        u, v, W = dat["u"], dat["v"], W_of(dat["M2"])
        rec = {"u_s": u, "v_s": v, "W": W, "ceiling": str(F(v, u)),
               "candidate_orders": [str(d) for d in detector_orders(u, v)], "charts": []}
        for delta in detector_orders(u, v):
            X = F(u) * delta - F(v)
            a = F(W) * X - 1 + delta
            k = a / X
            t = F(W) - k
            Q = delta.denominator
            for part in partitions(u):
                if len(part) < 2:
                    continue                     # one block is not a separation
                gal = galois_patterns(part, Q)
                loc = local_exponent_ok(part, k, t, W, u)
                entry = {"delta": str(delta), "partition": list(part), "Q": Q,
                         "k": str(k), "t": str(t),
                         "galois_patterns": [[p0, o] for p0, o in gal],
                         "local_assignments": loc}
                if not gal:
                    entry.update(verdict="DEAD", reason="no zeta_Q-stable root multiset (G)")
                elif not loc:
                    entry.update(verdict="DEAD",
                                 reason="local exponent count exceeds deg q (L)")
                else:
                    zero_mult, orbits = gal[0]
                    cvals = [sp.Rational(i + 1) for i in range(len(orbits))]
                    p = build_p(part, zero_mult, orbits, Q, cvals)
                    q, info = construct_q(u, v, W, delta, p, Q)
                    if q is None:
                        entry.update(verdict="OPEN_FACE",
                                     reason="G and L pass; no closed-form q built",
                                     build=info)
                    else:
                        res = face_residual(u, v, W, delta, p, q)
                        res = sp.expand(res)
                        entry.update(verdict="SOLVABLE" if res == 0 else "RESIDUAL_NONZERO",
                                     p=str(sp.factor(p)), q_shape=info,
                                     deg_q=int(sp.degree(sp.Poly(q, z))),
                                     residual="0" if res == 0 else str(res)[:200])
                rec["charts"].append(entry)
                print(f"{name} d={delta} lam={part} Q={Q} k={k} t={t} -> "
                      f"{entry['verdict']}", flush=True)
        rec["survivors"] = [{"delta": c["delta"], "partition": c["partition"]}
                            for c in rec["charts"] if c["verdict"] == "SOLVABLE"]
        rec["undecided"] = [{"delta": c["delta"], "partition": c["partition"]}
                            for c in rec["charts"] if c["verdict"] not in ("SOLVABLE", "DEAD")]
        out["rows"][name] = rec
    charged = {"S1": [("4", [1, 1])],
               "S2": [("3/2", [2, 2]), ("3/2", [2, 1, 1]), ("5/3", [1, 1, 1, 1])],
               "S3": [("3/2", [2, 2]), ("3/2", [2, 1, 1]), ("5/3", [1, 1, 1, 1])],
               "S4": [("2", [2, 1]), ("5/2", [1, 1, 1])],
               "S7": [("3/2", [2, 2]), ("3/2", [2, 1, 1]), ("5/3", [1, 1, 1, 1])]}
    out["charged_comparison"] = {}
    for name, rec in out["rows"].items():
        mine = sorted((s["delta"], tuple(s["partition"])) for s in rec["survivors"])
        theirs = sorted((d, tuple(p)) for d, p in charged[name])
        out["charged_comparison"][name] = {
            "mechanical": [[d, list(p)] for d, p in mine],
            "charged_hardcoded": [[d, list(p)] for d, p in theirs],
            "identical": mine == theirs}
    (HERE / "face-screen.json").write_text(json.dumps(out, indent=1, sort_keys=True) + "\n",
                                           encoding="utf-8")
    print(json.dumps(out["charged_comparison"], indent=1))


if __name__ == "__main__":
    main()
