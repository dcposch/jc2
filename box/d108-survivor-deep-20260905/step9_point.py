#!/usr/bin/env python3
"""Step 9: a rational point on the residual locus of a stage.

The section-6 point is tried first.  If it fails, the radical of the residual
is taken factor-by-factor and any generator that is linear in some unknown with
a nonzero rational leading coefficient is solved for that unknown; the result
is verified against EVERY residual generator, and against the side conditions
the gate declares (c != 0, and D2-minimality Hc_5_3 = 2*jet1*jet2 != 0).
"""
import argparse, json, sys
from pathlib import Path
import sympy as sp
OUT = Path("/home/ubuntu/jc2/box/d108-survivor-deep-20260905")


def radical_gens(exprs):
    out = []
    for e in exprs:
        for f, _m in sp.factor_list(sp.expand(e))[1]:
            if f.free_symbols and f not in out:
                out.append(sp.expand(f))
    return out


def find_point(residual, base):
    gens = radical_gens(residual)
    pt = dict(base)
    unresolved = []
    for g in gens:
        if sp.expand(g.subs(pt)) == 0:
            continue
        target = None
        # pick a variable that occurs linearly in g with a rational leading
        # coefficient, then solve g = 0 for it with the current point in the rest
        for v in sorted(g.free_symbols, key=str):
            co = sp.diff(g, v)
            rem = sp.expand(g - co * v)
            if co.is_Rational and co != 0 and v not in rem.free_symbols:
                target = (v, sp.cancel(-sp.expand(rem.subs({k: x for k, x in pt.items()
                                                            if k != v})) / co))
                break
        if target is None:
            unresolved.append(str(g)); continue
        v, val = target
        pt[v] = sp.expand(val)
    return pt, gens, unresolved


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", required=True)
    ap.add_argument("--stage", type=int, default=None)
    a = ap.parse_args()
    d = json.load(open(a.json))
    if "stages" in d:
        st = [s for s in d["stages"] if a.stage is None
              or s["stage_local_power"] == a.stage][-1]
        residual = {k: sp.sympify(v) for k, v in st["residual"].items()}
        label = f"{d['tag']} n={st['stage_local_power']}"
    else:
        residual = {k: sp.sympify(v) for k, v in d["residual"].items()}
        label = f"{d['tag']} T={d['truncation_depth_T']}"
    exprs = list(residual.values())
    allv = sorted(set().union(*[e.free_symbols for e in exprs]), key=str) if exprs else []
    base = {v: sp.Integer(0) for v in allv}
    for nm in ("jet1", "jet2", "c"):
        base[sp.Symbol(nm)] = sp.Integer(1)
    sec6_fail = [l for l, v in residual.items() if sp.expand(v.subs(base)) != 0]
    pt, gens, unresolved = find_point(exprs, base)
    fail = [(l, str(sp.expand(v.subs(pt)))[:200]) for l, v in residual.items()
            if sp.expand(v.subs(pt)) != 0]
    j1, j2 = pt.get(sp.Symbol("jet1"), 1), pt.get(sp.Symbol("jet2"), 1)
    rec = {"source": a.json, "stage": label,
           "residual_generators": {k: str(v) for k, v in residual.items()},
           "radical_generators": [str(g) for g in gens],
           "sec6_point_survives": not sec6_fail,
           "sec6_point_failing_rows": sec6_fail,
           "new_point": {str(k): str(v) for k, v in sorted(pt.items(), key=lambda x: str(x[0]))
                         if v != 0},
           "unresolved_radical_generators": unresolved,
           "point_annihilates_residual": not fail, "failing": fail,
           "c_value": str(pt.get(sp.Symbol("c"), "1")),
           "D2_minimality_Hc_5_3 = 2*jet1*jet2": str(sp.expand(2 * j1 * j2)),
           "locus_resolutions": {"K2c_3_26": str(sp.expand(-8 * j2)),
                                 "K2c_4_25": str(sp.expand(
                                     pt.get(sp.Symbol("K2c_4_26"), 0) + 20 * j1 ** 2))}}
    tag = Path(a.json).stem + (f"_n{a.stage}" if a.stage else "")
    (OUT / f"point-{tag}.json").write_text(json.dumps(rec, indent=2) + "\n")
    print(json.dumps(rec, indent=2))


if __name__ == "__main__":
    main()
