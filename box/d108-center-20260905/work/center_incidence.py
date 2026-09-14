#!/usr/bin/env python3
"""D=108 delta=3 stage-0 common-h3 incidence, re-emitted under

  (a) the D2 z-radius actually used by the frozen engine  (z ~ s^6, weight 4r+6q)
  (b) the D2 z-radius forced by Moh Def 5.1(3)            (z ~ s^5, weight 4r+5q)

and with the minor generic point either centred (jet0 = 0, the frozen
convention) or carrying its Def 5.1(4) constant term (jet0 free).

Written independently of box/d108-center-20260905/replay_incidence.py; only
`qstar_reduce` is imported from the frozen charged engine.
"""
import importlib.util, json, sys, time
from collections import defaultdict
from math import comb, factorial
from pathlib import Path
import sympy as sp

import sys as _s; _s.path.insert(0, "/home/ubuntu/jc2/box/g108gate-20260903")
FROZEN = "/tmp/jc2-lane.nD5MyA/inputs/band_engine.py"
spec = importlib.util.spec_from_file_location("frozen_band_engine", FROZEN)
eng = importlib.util.module_from_spec(spec); sys.modules[spec.name] = eng
spec.loader.exec_module(eng)

OUT = Path(__file__).resolve().parent


def h3_template(wz, cutoff):
    """h3 chart in z=w-1.  wz = ord_s(z); cutoff = D2 s-weight floor (None = free)."""
    h = {(0, 7): sp.Integer(1), (0, 8): sp.Integer(2), (0, 9): sp.Integer(1)}
    variables = []
    for r in range(1, 10):
        vmin = 0 if cutoff is None else max(0, -((-(cutoff - 4 * r)) // wz))
        for degree in range(vmin, 10 - r):
            v = sp.Symbol(f"Hc_{r}_{degree}"); variables.append(v)
            for q in range(vmin, degree + 1):
                h[(r, q)] = h.get((r, q), sp.Integer(0)) + v * comb(degree - vmin, q - vmin)
    return {k: sp.expand(v) for k, v in h.items()}, variables


def z_to_w(item):
    out = defaultdict(lambda: sp.Integer(0))
    for (r, q), co in item.items():
        for j in range(q + 1):
            out[(r, j)] += co * comb(q, j) * (-1) ** (q - j)
    return {k: sp.expand(v) for k, v in out.items() if v != 0}


def incidence(h, jet0=False):
    """w = jet0*t + jet1*t^2 + jet2*t^3 + pi*t^4 through local power 8; target
    K3 = -t^8*(pi^2 - c) + O(t^9).  jet0=False pins the frozen jet0 = 0."""
    wb = z_to_w(h)
    j0, j1, j2, c = sp.symbols("jet0 jet1 jet2 c")
    coll = defaultdict(lambda: sp.Integer(0))
    for (r, j), co in wb.items():
        for d in (range(j + 1) if jet0 else [0]):
            for a in range(j - d + 1):
                for b in range(j - d - a + 1):
                    k = j - d - a - b
                    lp = r + d + 2 * a + 3 * b + 4 * k
                    if lp > 8:
                        continue
                    mn = factorial(j) // (factorial(d) * factorial(a) * factorial(b) * factorial(k))
                    coll[(lp, k)] += co * mn * j0 ** d * j1 ** a * j2 ** b
    coll[(8, 0)] -= c
    coll[(8, 2)] += 1
    return [(f"minor_n{p}_pi{k}", sp.expand(v)) for (p, k), v in sorted(coll.items())]


def run(tag, wz, cutoff, jet0=False):
    t0 = time.monotonic()
    h, hv = h3_template(wz, cutoff)
    rows = incidence(h, jet0)
    resid, subs, piv, zeros = eng.qstar_reduce(rows, hv)
    c, Zc = sp.symbols("c Zc")
    gens = [v for _l, v in resid] + [Zc * c - 1]
    rv = sorted(set().union(*(g.free_symbols for g in gens)), key=str)
    G = sp.groebner(gens, *rv, order="grevlex")
    unit = list(G.exprs) == [sp.Integer(1)]
    rec = {"tag": tag, "z_s_order": wz, "weight": f"4*r+{wz}*q", "cutoff": cutoff,
           "minor_jet0_free": jet0, "coefficient_field": "QQ",
           "h3_coordinates": [str(v) for v in hv], "h3_coordinate_count": len(hv),
           "raw_rows": {l: str(v) for l, v in rows},
           "Qstar_pivots": [{"row": p.label, "variable": str(p.variable),
                             "coefficient": str(p.coefficient),
                             "resolved_value": str(subs[p.variable])} for p in piv],
           "zero_rows": zeros, "residual": {l: str(v) for l, v in resid},
           "ring_variables": [str(v) for v in rv], "groebner_order": "grevlex",
           "groebner_basis": [str(g) for g in G.exprs], "localized_unit": unit,
           "seconds": round(time.monotonic() - t0, 2)}
    (OUT / f"{tag}.json").write_text(json.dumps(rec, indent=2) + "\n")
    print(f"{tag:34s} w=(4,{wz}) cut={str(cutoff):4s} jet0={int(jet0)} "
          f"coords={len(hv):2d} pivots={len(piv):2d} resid={len(resid)} "
          f"UNIT={unit}  GB={[str(g) for g in G.exprs][:3]}", flush=True)
    return rec


CASES = [
    ("A_engine_cut43_jet0pinned",  6, 43,  False),   # frozen 17(ddddd) baseline
    ("B_engine_cut42_jet0pinned",  6, 42,  False),   # frozen robustness control
    ("C_engine_nofloor_jet0pinned",6, None,False),   # support-regression probe
    ("D_engine_cut43_jet0free",    6, 43,  True),    # centre lemma + gauge transfer
    ("E_engine_cut42_jet0free",    6, 42,  True),
    ("F_moh_cut35_jet0pinned",     5, 35,  False),   # Def 5.1(3) radius, face retained
    ("G_moh_cut36_jet0pinned",     5, 36,  False),   # Def 5.1(3) radius, face fixed
    ("H_moh_cut35_jet0free",       5, 35,  True),    # Def 5.1(3) radius + centre repair
]

if __name__ == "__main__":
    sel = set(sys.argv[1:])
    for args in CASES:
        if not sel or args[0] in sel:
            run(*args)
