#!/usr/bin/env python3
"""Step 5: the surviving locus of the staged elimination -- structure, an
explicit rational point, and a NEGATIVE CONTROL that substitutes the point into
every RAW row (never through the pivots)."""
import json, sys, time
from pathlib import Path
import sympy as sp
sys.path.insert(0, str(Path(__file__).resolve().parent))
from rekill_engine import (SRC, minor_incidence, qstar_reduce, symbol, build_major_h2,
                           substitute_map, outer_state, build_FG, jacobian_band,
                           local_rows, raw_minor_support, stage_spec, pole_coeff)

OUT = Path(__file__).resolve().parent
STAGE = int(sys.argv[1]) if len(sys.argv) > 1 else 4
jet0free = "--jet0free" in sys.argv
R = SRC
t0 = time.monotonic()

rows0, hvars, h3 = minor_incidence(R, R.k3_face, jet0free)
resid0, subs0, piv0, _ = qstar_reduce(rows0, hvars)
h3r = {k: v for k, v in ((k, substitute_map(v, subs0)) for k, v in h3.items()) if v != 0}
k2, k2free, k2meta = build_major_h2(R, h3r, 40, jet0free)
outer, outer_free, outer_meta = outer_state(R, STAGE)
max_pole = max(stage_spec(i)["pole_local_power"] for i in range(STAGE + 1))
max_t = max(max_pole, STAGE, 3)
KF, KG = build_FG(k2, outer, max_t)
f_local, g_local = local_rows(KF, max_pole, jet0free), local_rows(KG, max_pole, jet0free)

rows = [(f"h3_incidence_{l}", v) for l, v in resid0]
for name, table in (("F", f_local), ("G", g_local)):
    for n in (1, 2, 3):
        for k in raw_minor_support(name, jet0free).get(n, ()):
            rows.append((f"prior_{name}_local{n}_coord{k}", pole_coeff(table, n, k, name)))
J1 = jacobian_band(KF, KG, 1)
rows += [(f"prior_J_d177_k{k}", J1.get(k, sp.Integer(0))) for k in range(15, 25)]
for cur in range(STAGE + 1):
    sc = stage_spec(cur); n = sc["pole_local_power"]
    for name, table in (("F", f_local), ("G", g_local)):
        for k in raw_minor_support(name, jet0free).get(n, ()):
            rows.append((f"stage{cur}_{name}_local{n}_coord{k}", pole_coeff(table, n, k, name)))
    js = sc["jacobian"]; J = jacobian_band(KF, KG, js["t_power"])
    rows += [(f"stage{cur}_J_d{js['degree']}_k{k}", J.get(k, sp.Integer(0))) for k in js["w_powers"]]

free = set(k2free) | set(outer_free) | {v for v in hvars if v not in subs0}
residual, subs, pivots, zeros = qstar_reduce(rows, free)

# ---- structure of the residual ideal
res_exprs = [sp.expand(v) for _l, v in residual]
factored = {l: str(sp.factor(v)) for l, v in residual}
rvars = sorted(set().union(*(e.free_symbols for e in res_exprs)), key=str)
Gb = sp.groebner(res_exprs, *rvars, order="grevlex")
rad_gen = symbol("K2c_3_26") + 8 * symbol("jet2")
in_radical = all(sp.rem(sp.expand(e), rad_gen, symbol("K2c_3_26")) == 0 for e in res_exprs)

# ---- explicit rational point.  Solve the residual for two designated
# unknowns with everything else pinned; no unknown is inverted, the solve is
# a substitution checked symbolically and then instantiated over Q.
sol = {symbol("K2c_3_26"): -8 * symbol("jet2"),
       symbol("K2c_4_25"): symbol("K2c_4_26") + 20 * symbol("jet1") ** 2}
sym_images = {l: sp.expand(sp.expand(v).subs(sol, simultaneous=True)) for l, v in residual}
sym_ok = all(v == 0 for v in sym_images.values())
point = {v: sp.Integer(0) for v in sorted(free, key=str)}
point[symbol("jet1")] = sp.Integer(1)
point[symbol("jet2")] = sp.Integer(1)
point[symbol("c")] = sp.Integer(1)
if jet0free: point[symbol("jet0")] = sp.Integer(0)
for var, rhs in sol.items():
    point[var] = sp.expand(rhs.subs(point))
resid_images = {l: sp.expand(v.subs(point)) for l, v in residual}
resid_ok = all(v == 0 for v in resid_images.values())

# ---- resolve the pivoted unknowns at the point, then hit EVERY raw row.
full = dict(point)
for var, rhs in subs.items():
    full[var] = sp.expand(sp.together(rhs).subs(point))
for var, rhs in subs0.items():
    full[var] = sp.expand(sp.together(rhs).subs(full))
bad = []
for l, v in rows:
    img = sp.expand(sp.expand(v).subs(full))
    if img != 0: bad.append((l, str(img)[:200]))
rec = {"stage": STAGE, "jet0_free": jet0free,
       "residual_row_count": len(residual),
       "residual": {l: str(v) for l, v in residual},
       "residual_factored": factored,
       "residual_groebner": [str(g) for g in Gb.exprs],
       "radical_generator": "K2c_3_26 + 8*jet2",
       "every_residual_generator_divisible_by_radical_generator": in_radical,
       "solve_substitution": {str(k): str(v) for k, v in sol.items()},
       "residual_vanishes_symbolically_on_solve": sym_ok,
       "symbolic_images": {l: str(v) for l, v in sym_images.items()},
       "point_free_nonzero": {str(k): str(v) for k, v in point.items() if v != 0},
       "point_free_zero_count": sum(1 for v in point.values() if v == 0),
       "residual_images_all_zero": resid_ok,
       "raw_rows_checked": len(rows),
       "raw_rows_failing": bad,
       "NEGATIVE_CONTROL_all_raw_rows_vanish": not bad,
       "c_nonzero": str(point[symbol("c")]),
       "D2_minimality_Hc_5_3": str(sp.expand(sp.together(subs0[symbol("Hc_5_3")]).subs(full))),
       "wall_seconds": round(time.monotonic() - t0, 1)}
(OUT / f"witness-stage{STAGE}{'-jet0free' if jet0free else ''}.json").write_text(
    json.dumps(rec, indent=2, default=str) + "\n")
print(json.dumps({k: rec[k] for k in
                  ("stage", "jet0_free", "residual_row_count", "residual_factored",
                   "solve_substitution", "residual_vanishes_symbolically_on_solve",
                   "point_free_nonzero",
                   "residual_images_all_zero", "raw_rows_checked",
                   "NEGATIVE_CONTROL_all_raw_rows_vanish", "raw_rows_failing",
                   "D2_minimality_Hc_5_3", "wall_seconds")}, indent=2)[:2500])
