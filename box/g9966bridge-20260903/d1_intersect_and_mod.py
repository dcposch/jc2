#!/usr/bin/env python3
"""Intersect D1 pivot columns with linearized remaining; emit modular face std."""
from __future__ import annotations

import json
from collections import defaultdict
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
    e, base = n, dict(A)
    while e:
        if e & 1:
            res = poly_mul(res, base)
        e >>= 1
        if e:
            base = poly_mul(base, base)
    return res


def run():
    rem = json.loads((HERE / "residual_linear.json").read_text())["union_remaining_vars"]
    rem_set = set(rem)
    bands = json.loads(
        Path("/tmp/jc2-lane.tJWSjH/inputs/outer_order_bands.json").read_text()
    )
    d1_hits = {}
    total_d1 = 0
    in_rem = 0
    for name, blk in bands["blocks"].items():
        cols = [tuple(x) for x in blk.get("D1_pivot_columns_rq", [])]
        present = []
        missing = []
        for r, q in cols:
            key = f"{name}_{r}_{q}"
            total_d1 += 1
            if key in rem_set:
                in_rem += 1
                present.append(key)
            else:
                missing.append(key)
        d1_hits[name] = {
            "D1_pivots": len(cols),
            "still_remaining_after_linear_bridge": len(present),
            "already_pivoted_by_FG_or_T2": len(missing),
            "present_head": present[:8],
        }
    # extra D1 rank at most in_rem
    lin_rem = len(rem)
    lower_after_d1 = max(0, lin_rem - in_rem)

    p = {3: 1, 2: 3}
    cols = {
        "c0": poly_pow(p, 12),
        "a1": poly_pow(p, 15),
        "a0": poly_pow(p, 6),
        "b1": poly_pow(p, 9),
        "b0": {0: 1},
        "lam": {d: -v for d, v in poly_pow(p, 5).items()},
    }
    names = list(cols)
    degs = sorted({d for c in cols.values() for d in c})
    # write Singular coefficient ideal
    lines = []
    for pr in (32003, 104729, 1299709):
        body = [f"option(redSB);", f"ring R = {pr},(c0,a1,a0,b1,b0,lam),dp;", "ideal I ="]
        polys = []
        for deg in degs:
            terms = []
            for n in names:
                v = cols[n].get(deg, 0)
                if v:
                    terms.append(f"({v})*{n}")
            if terms:
                polys.append("  " + "+".join(terms))
        body.append(",\n".join(polys) + ";")
        body += ["ideal Gstd = std(I);", "Gstd;", "size(Gstd);", "exit;"]
        (HERE / "work" / f"face_lin_p{pr}.sing").write_text("\n".join(body) + "\n")

    # T3 R vs G powers
    z3 = {k: comb(14, k) * (3 ** (14 - k)) for k in range(15)}
    R = defaultdict(int)
    for d, v in z3.items():
        R[d + 26] += v
        R[d + 25] += -2 * v
    t3names = [f"c{k}" for k in range(9)] + ["lam"]
    t3cols = {f"c{k}": poly_pow(p, 6 * k) for k in range(9)}
    t3cols["lam"] = {d: -v for d, v in R.items() if v}
    degs3 = sorted({d for c in t3cols.values() for d in c})
    for pr in (32003, 104729, 1299709):
        vs = ",".join(t3names)
        body = [f"option(redSB);", f"ring R = {pr},({vs}),dp;", "ideal I ="]
        polys = []
        for deg in degs3:
            terms = []
            for n in t3names:
                v = t3cols[n].get(deg, 0)
                if v:
                    terms.append(f"({int(v)})*{n}")
            if terms:
                polys.append("  " + "+".join(terms))
        body.append(",\n".join(polys) + ";")
        body += ["ideal Gstd = std(I);", "size(Gstd);", "Gstd;", "exit;"]
        (HERE / "work" / f"t3_lin_p{pr}.sing").write_text("\n".join(body) + "\n")

    out = {
        "type": "DERIVED[D1-INTERSECT + FACE-MODULAR-SCRIPTS]",
        "union_remaining": lin_rem,
        "D1_pivot_columns_total": total_d1,
        "D1_still_in_remaining": in_rem,
        "D1_already_used": total_d1 - in_rem,
        "counting_bound_after_D1_if_independent": lower_after_d1,
        "blocks": d1_hits,
        "note": (
            "If all D1 pivot columns still remaining are independent of the "
            "linear bridge, remaining drops by that count.  Independence not "
            "re-proved here; this is a floor."
        ),
    }
    (HERE / "d1_intersect.json").write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    run()
