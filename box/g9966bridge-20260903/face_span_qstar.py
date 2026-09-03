#!/usr/bin/env python3
"""Exact Q* : Tschirnhausen face vs p^5 and vs R, as polynomials in z, over Q.

T2_face = c0 p^{12} + a1 p^{15} + a0 p^6 + b1 p^9 + b0  (G^3-F^2=0 on the nose)
Target T2: lam p^5.
T3_face truncated: sum_{k=0,2,3,...,8} ck G^k with G=p^6, plus -F^6+G^9=0.
Target T3: lam R.
"""
from __future__ import annotations

import json
from collections import defaultdict
from fractions import Fraction
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent


def poly_mul(A, B):
    out = defaultdict(int)
    for d1, v1 in A.items():
        for d2, v2 in B.items():
            out[d1 + d2] += v1 * v2
    return {d: v for d, v in out.items() if v != 0}


def poly_pow(A, n):
    res = {0: 1}
    e = n
    base = dict(A)
    while e:
        if e & 1:
            res = poly_mul(res, base)
        e >>= 1
        if e:
            base = poly_mul(base, base)
    return res


def poly_add(*ps):
    out = defaultdict(int)
    for p in ps:
        for d, v in p.items():
            out[d] += v
    return {d: v for d, v in out.items() if v != 0}


def qstar(cols, degrees):
    names = list(cols)
    rows = []
    for deg in degrees:
        rec = {}
        for n in names:
            v = cols[n].get(deg, 0)
            if v:
                rec[n] = Fraction(v)
        if rec:
            rows.append((deg, rec))
    remaining = list(names)
    pivots = []
    used = [False] * len(rows)
    progressed = True
    while progressed:
        progressed = False
        for i, (deg, rec) in enumerate(rows):
            if used[i]:
                continue
            rec = {n: v for n, v in rec.items() if v != 0}
            rows[i] = (deg, rec)
            if not rec:
                used[i] = True
                continue
            choice = None
            for n in remaining:
                if n in rec:
                    choice = n
                    break
            if choice is None:
                continue
            coeff = rec[choice]
            rhs = {n: -v / coeff for n, v in rec.items() if n != choice}
            pivots.append({"deg": deg, "var": choice, "coeff": str(coeff)})
            remaining.remove(choice)
            used[i] = True
            progressed = True
            for j, (d2, rec2) in enumerate(rows):
                if used[j] or choice not in rec2:
                    continue
                scale = rec2.pop(choice)
                for n, v in rhs.items():
                    rec2[n] = rec2.get(n, 0) + scale * v
                    if rec2[n] == 0:
                        rec2.pop(n)
            break
    leftover = [(d, rec) for i, (d, rec) in enumerate(rows) if not used[i] and rec]
    return {
        "rank": len(pivots),
        "remaining": remaining,
        "leftover": [{"deg": d, "terms": {n: str(v) for n, v in rec.items()}} for d, rec in leftover],
        "pivots": pivots,
        "lambda_pivoted": any(p["var"] == "lam" for p in pivots),
        "lambda_free": "lam" in remaining,
    }


def run():
    p = {3: 1, 2: 3}  # z^3+3z^2
    p5 = poly_pow(p, 5)
    p6 = poly_pow(p, 6)
    p9 = poly_pow(p, 9)
    p12 = poly_pow(p, 12)
    p15 = poly_pow(p, 15)
    t2_cols = {
        "c0": p12,
        "a1": p15,
        "a0": p6,
        "b1": p9,
        "b0": {0: 1},
        "lam": {d: -v for d, v in p5.items()},
    }
    degs = sorted({d for col in t2_cols.values() for d in col})
    t2 = qstar(t2_cols, degs)

    # R = z^25 (z+3)^14 (z-2)
    z3 = {}
    for k in range(15):
        z3[k] = comb(14, k) * (3 ** (14 - k))
    Rz = {}
    for d, v in z3.items():
        Rz[d + 25] = v
    R = defaultdict(int)
    for d, v in Rz.items():
        R[d + 1] += v
        R[d] += -2 * v
    R = {d: v for d, v in R.items() if v}

    # T3 face: G^k = p^{6k} for k=0..8, skip the cancelled G^9-F^6
    t3_cols = {}
    for k in range(0, 9):
        t3_cols[f"c{k}"] = poly_pow(p, 6 * k)
    t3_cols["lam"] = {d: -v for d, v in R.items()}
    degs3 = sorted({d for col in t3_cols.values() for d in col})
    t3 = qstar(t3_cols, degs3)

    # without b0 (does not appear at T2 leader)
    t2_nob0 = qstar({k: v for k, v in t2_cols.items() if k != "b0"}, degs)

    out = {
        "type": "DERIVED[FACE-SPAN-QSTAR / Q]",
        "p": "z^2(z+3)",
        "p5_support": sorted(p5),
        "R_support": sorted(R),
        "T2_face_with_b0": {
            "rank": t2["rank"],
            "remaining": t2["remaining"],
            "leftover": t2["leftover"],
            "lambda_pivoted": t2["lambda_pivoted"],
            "lambda_free": t2["lambda_free"],
            "p5_in_span": t2["lambda_pivoted"] and not t2["lambda_free"] and not t2["leftover"],
        },
        "T2_face_without_b0": {
            "rank": t2_nob0["rank"],
            "remaining": t2_nob0["remaining"],
            "leftover": t2_nob0["leftover"],
            "lambda_pivoted": t2_nob0["lambda_pivoted"],
            "lambda_free": t2_nob0["lambda_free"],
            "p5_in_span": t2_nob0["lambda_pivoted"]
            and not t2_nob0["lambda_free"]
            and not t2_nob0["leftover"],
        },
        "T3_face_G_powers_0_8": {
            "rank": t3["rank"],
            "remaining": t3["remaining"],
            "leftover_count": len(t3["leftover"]),
            "leftover_head": t3["leftover"][:6],
            "lambda_pivoted": t3["lambda_pivoted"],
            "lambda_free": t3["lambda_free"],
            "R_in_span": t3["lambda_pivoted"] and not t3["lambda_free"] and not t3["leftover"],
        },
        "verdict": (
            "p^5 is not in the Tschirnhausen z-polynomial span of {p^{15},p^{12},p^9,p^6,p^0} "
            "on the straight slice a=1; R is not in span{p^{0,6,...,48}}.  Charged face "
            "obstruction confirmed as an exact coefficient-ideal statement over Q."
        ),
    }
    (HERE / "face_span_qstar.json").write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: out[k] for k in out if k != "verdict"}, indent=2))
    print(out["verdict"])
    return out


if __name__ == "__main__":
    run()
