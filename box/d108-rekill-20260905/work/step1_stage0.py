#!/usr/bin/env python3
"""Step 1: stage-0 common-h3 incidence at both radii + the two mandated controls.

CONTROL 1 (old radius must reproduce [1]).
CONTROL 2 (the frozen d108-center witness must satisfy the rebuilt engine).
"""
import json, sys
from pathlib import Path
import sympy as sp
sys.path.insert(0, str(Path(__file__).resolve().parent))
from rekill_engine import SRC, FRZ, minor_incidence, qstar_reduce, symbol

OUT = Path(__file__).resolve().parent
CASES = [
    ("ctl_frozen_cut43_jet0pinned", FRZ, 43, False),
    ("ctl_frozen_cut42_jet0pinned", FRZ, 42, False),
    ("ctl_frozen_cut43_jet0free",   FRZ, 43, True),
    ("src_cut36_jet0pinned",        SRC, 36, False),
    ("src_cut35_jet0pinned",        SRC, 35, False),
    ("src_cut35_jet0free",          SRC, 35, True),
    ("src_cut36_jet0free",          SRC, 36, True),
]
rec = {}
for tag, R, cutoff, jet0free in CASES:
    rows, hvars, _h3 = minor_incidence(R, cutoff, jet0free)
    resid, subs, piv, zeros = qstar_reduce(rows, hvars)
    c, Zc = symbol("c"), symbol("Zc")
    gens = [v for _l, v in resid] + [Zc * c - 1]
    rv = sorted(set().union(*(g.free_symbols for g in gens)), key=str)
    G = sp.groebner(gens, *rv, order="grevlex")
    unit = list(G.exprs) == [sp.Integer(1)]
    rec[tag] = {"weight": f"4*r+{R.wz}*q", "cutoff": cutoff, "jet0_free": jet0free,
                "coords": [str(v) for v in hvars], "coord_count": len(hvars),
                "raw_rows": {l: str(v) for l, v in rows},
                "nonzero_rows": sum(1 for _l, v in rows if v != 0),
                "pivots": [{"row": p.label, "var": str(p.variable),
                            "coeff": str(p.coefficient), "value": str(subs[p.variable])}
                           for p in piv],
                "residual": {l: str(v) for l, v in resid},
                "zero_rows": zeros, "localized_unit": unit,
                "groebner": [str(g) for g in G.exprs][:8]}
    print(f"{tag:32s} coords={len(hvars):2d} nz_rows={rec[tag]['nonzero_rows']:2d} "
          f"piv={len(piv):2d} resid={len(resid)} UNIT={unit}", flush=True)

# CONTROL 2: the frozen d108-center witness against the rebuilt raw rows.
wit = json.loads(Path("/home/ubuntu/jc2/box/d108-center-20260905/work/"
                      "witness-minimal.json").read_text())["point"]
point = {symbol(k): sp.Rational(v) for k, v in wit.items()}
rows, hvars, _ = minor_incidence(SRC, 35, False)
images = {l: str(sp.expand(v.subs(point))) for l, v in rows}
allzero = all(sp.expand(v.subs(point)) == 0 for _l, v in rows)
rec["control_center_witness"] = {"point": {str(k): str(v) for k, v in point.items()},
                                 "images": images, "all_rows_vanish": allzero,
                                 "chart": "src_cut35_jet0pinned"}
print(f"CONTROL center-witness on src_cut35_jet0pinned: all_rows_vanish={allzero}")
(OUT / "step1-stage0.json").write_text(json.dumps(rec, indent=2) + "\n")
