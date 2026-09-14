#!/usr/bin/env python3
"""D=108 delta=3 major structure, rebuilt at the Moh Def 5.1(3) D2 radius.

Frozen engine (box/g108gate-20260903/band_engine.py, major_structure) uses
   D2:  t = s^4, z = pi*s^6 ;  W = 4r+6q ;  K3 face weight 42, K2 face weight 168
   D1:  s = e^2, t = e^8, z = e^12*(1+Pi*e)
Moh Def 5.1(3) on Skel(108,72,[81,106],{2:7,3:7}) has delta=(3/8,1/4,-1), so
   D2:  t = s^4, z = pi*s^5 ;  W = 4r+5q ;  K3 face weight 35, K2 face weight 140
   D1:  s = e^2, t = e^8, z = e^10*(1+Pi*e)          (2*W is the D1 e-weight)
This module emits BOTH so every count is a paired old/new measurement.
"""
import json
from fractions import Fraction
from math import comb
from pathlib import Path

OUT = Path(__file__).resolve().parent


def lower_positions(degree, y_cap):
    return {(r, q) for r in range(1, degree + 1)
            for q in range(min(y_cap, degree - r) + 1)}


def determinant(rows):
    work = [[Fraction(v) for v in row] for row in rows]
    result = Fraction(1)
    for col in range(len(work)):
        piv = next((r for r in range(col, len(work)) if work[r][col]), None)
        if piv is None:
            return Fraction(0)
        if piv != col:
            work[col], work[piv] = work[piv], work[col]
            result *= -1
        val = work[col][col]
        result *= val
        for r in range(col + 1, len(work)):
            sc = work[r][col] / val
            for c in range(col, len(work)):
                work[r][c] -= sc * work[col][c]
    return result


def rank(rows):
    work = [[Fraction(v) for v in row] for row in rows]
    r = 0
    ncol = len(work[0]) if work else 0
    for col in range(ncol):
        piv = next((i for i in range(r, len(work)) if work[i][col]), None)
        if piv is None:
            continue
        work[r], work[piv] = work[piv], work[r]
        val = work[r][col]
        for i in range(len(work)):
            if i != r and work[i][col]:
                sc = work[i][col] / val
                for c in range(col, ncol):
                    work[i][c] -= sc * work[r][c]
        r += 1
    return r


def major_structure(wz):
    """wz = ord_s(z) at the D2 generic point.  6 = frozen engine, 5 = source."""
    W = lambda r, q: 4 * r + wz * q
    k3_face = wz * 7          # z^7 is the lowest-weight term of z^7(1+z)^2
    k2_face = wz * 28         # z^28 is the lowest-weight term of z^28(1+z)^8

    h_fixed = {(0, 7), (0, 8), (0, 9)}
    h_all = lower_positions(9, 8)
    h_below = {p for p in h_all if W(*p) < k3_face}
    h_equal = {p for p in h_all if W(*p) == k3_face}
    h_tail = {p for p in h_all if W(*p) > k3_face}
    h_support = h_fixed | h_tail

    c2 = lower_positions(18, 8)
    c3 = lower_positions(27, 8)
    c4 = lower_positions(36, 8)

    h_squared = {(a + c, b + d) for a, b in h_support for c, d in h_support}
    h_fourth = {(a + c, b + d) for a, b in h_squared for c, d in h_squared}
    c2_h2 = {(a + c, b + d) for a, b in c2 for c, d in h_squared}
    c3_h = {(a + c, b + d) for a, b in c3 for c, d in h_support}

    slots = {(r, q) for r in range(1, 37) for q in range(37 - r)
             if W(r, q) <= k2_face}
    strict = {p for p in slots if W(*p) < k2_face}
    equality = {p for p in slots if W(*p) == k2_face}
    identities = slots - c4 - c3_h - c2_h2 - h_fourth - equality

    # Unit-triangular leaders, exactly the frozen selection rule.
    pivots, failures = {}, []
    for row in sorted(slots - identities, key=lambda p: (p[0], -p[1])):
        r, q = row
        if q <= 8:
            piv, cols = ("C4", r, q), {(r, q)}
            ok = (r, q) in c4
        elif q <= 17:
            piv = ("C3", r, q - 9)
            ok = (r, q - 9) in c3
            cols = {(r + a, q - 9 + b) for a, b in h_support
                    if (r + a, q - 9 + b) in slots}
        else:
            piv = ("C2", r, q - 18)
            ok = (r, q - 18) in c2
            cols = {(r + a, q - 18 + b) for a, b in h_squared
                    if (r + a, q - 18 + b) in slots}
        lead = min(cols, key=lambda p: (p[0], -p[1])) == row if cols else False
        if not (ok and lead and piv not in pivots):
            failures.append({"row": list(row), "pivot": [piv[0], piv[1], piv[2]],
                             "in_block": ok, "is_leader": lead,
                             "reused": piv in pivots})
            continue
        pivots[piv] = row
    counts = {n: sum(p[0] == n for p in pivots) for n in ("C4", "C3", "C2")}

    # D1 boundary rows for h2.  e-weight = 2*W; face leading e-exponent is the
    # image of the K2 D2 face under the D1 substitution.
    d1_face_exp = 2 * k2_face + (0 if wz == 6 else 0)
    ambient = len(h_tail) + len(c2) + len(c3) + len(c4)
    return {
        "z_s_order": wz, "weight": f"4*r+{wz}*q",
        "K3_D2_face_weight": k3_face, "K2_D2_face_weight": k2_face,
        "h3_D2": {"lower_ambient": len(h_all), "strict_rows": len(h_below),
                  "face_rows": len(h_equal),
                  "face_sites": sorted(map(list, h_equal)),
                  "surviving": sorted(map(list, h_tail)),
                  "surviving_count": len(h_tail)},
        "h2_D2": {"strict_rows": len(strict), "face_rows": len(equality),
                  "face_sites": sorted(map(list, equality)),
                  "nominal_rows": len(slots),
                  "identity_sites": sorted(map(list, identities)),
                  "identity_count": len(identities),
                  "rank": len(pivots), "unit_pivots": counts,
                  "leader_failures": failures[:20],
                  "leader_failure_count": len(failures)},
        "ambient": {"H": len(h_tail), "C2": len(c2), "C3": len(c3),
                    "C4": len(c4), "total": ambient},
        "free_after_D2": ambient - len(pivots),
    }


if __name__ == "__main__":
    rec = {"frozen_wz6": major_structure(6), "source_wz5": major_structure(5)}
    (OUT / "major-structure-both.json").write_text(json.dumps(rec, indent=2) + "\n")
    for tag, r in rec.items():
        h, k = r["h3_D2"], r["h2_D2"]
        print(f"{tag}: W={r['weight']}  K3face={r['K3_D2_face_weight']} "
              f"K2face={r['K2_D2_face_weight']}")
        print(f"   h3: ambient={h['lower_ambient']} strict={h['strict_rows']} "
              f"face={h['face_rows']}{h['face_sites']} surv={h['surviving_count']}")
        print(f"   h2: slots={k['nominal_rows']} strict={k['strict_rows']} "
              f"face={k['face_rows']}{k['face_sites']} ident={k['identity_count']}"
              f"{k['identity_sites']}")
        print(f"       rank={k['rank']} pivots={k['unit_pivots']} "
              f"leaderfail={k['leader_failure_count']}")
        print(f"   ambient={r['ambient']}  free_after_D2={r['free_after_D2']}")
