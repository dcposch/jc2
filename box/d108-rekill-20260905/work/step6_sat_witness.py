#!/usr/bin/env python3
"""Step 6: witness + negative control on the SATURATED system (all rows the
chart expresses at truncation depth T, strictly more than stage 4)."""
import json, sys, time
from pathlib import Path
import sympy as sp
sys.path.insert(0, str(Path(__file__).resolve().parent))
from rekill_engine import (SRC, minor_incidence, qstar_reduce, symbol, build_major_h2,
                           substitute_map, outer_state, build_FG, jacobian_band,
                           local_rows, raw_minor_support, pole_coeff)
OUT = Path(__file__).resolve().parent
T, jet0free, offsets = 8, False, 7
t0 = time.monotonic()
rows0, hvars, h3 = minor_incidence(SRC, SRC.k3_face, jet0free)
resid0, subs0, piv0, _ = qstar_reduce(rows0, hvars)
h3r = {k: v for k, v in ((k, substitute_map(v, subs0)) for k, v in h3.items()) if v != 0}
k2, k2free, _ = build_major_h2(SRC, h3r, 40, jet0free)
outer, outer_free, _ = outer_state(SRC, offsets)
KF, KG = build_FG(k2, outer, T)
f_local, g_local = local_rows(KF, T, jet0free), local_rows(KG, T, jet0free)
rows = [(f"h3_incidence_{l}", v) for l, v in resid0]
for name, table in (("F", f_local), ("G", g_local)):
    for n in range(1, T + 1):
        for k in raw_minor_support(name, jet0free).get(n, ()):
            rows.append((f"{name}_local{n}_coord{k}", pole_coeff(table, n, k, name)))
for tp in range(1, T + 1):
    J = jacobian_band(KF, KG, tp)
    rows += [(f"J_t{tp}_d{178-tp}_k{k}", J.get(k, sp.Integer(0))) for k in range(179 - tp)]
free = set(k2free) | set(outer_free) | {v for v in hvars if v not in subs0}
residual, subs, pivots, zeros = qstar_reduce(rows, free)
sol = {symbol("K2c_3_26"): -8 * symbol("jet2"),
       symbol("K2c_4_25"): symbol("K2c_4_26") + 20 * symbol("jet1") ** 2}
sym = {l: sp.expand(sp.expand(v).subs(sol, simultaneous=True)) for l, v in residual}
point = {v: sp.Integer(0) for v in sorted(free, key=str)}
for v, x in (("jet1", 1), ("jet2", 1), ("c", 1)): point[symbol(v)] = sp.Integer(x)
for var, rhs in sol.items(): point[var] = sp.expand(rhs.subs(point))
full = dict(point)
for var, rhs in subs.items(): full[var] = sp.expand(sp.together(rhs).subs(point))
for var, rhs in subs0.items(): full[var] = sp.expand(sp.together(rhs).subs(full))
bad = [(l, str(sp.expand(sp.expand(v).subs(full)))[:150]) for l, v in rows
       if sp.expand(sp.expand(v).subs(full)) != 0]
rec = {"truncation_depth_T": T, "raw_row_count": len(rows),
       "outer_D1_offsets": offsets, "Qstar_pivots": len(pivots),
       "residual": {l: str(v) for l, v in residual},
       "residual_factored": {l: str(sp.factor(v)) for l, v in residual},
       "solve_substitution": {str(k): str(v) for k, v in sol.items()},
       "residual_vanishes_symbolically_on_solve": all(v == 0 for v in sym.values()),
       "point_free_nonzero": {str(k): str(v) for k, v in point.items() if v != 0},
       "raw_rows_failing": bad,
       "NEGATIVE_CONTROL_all_raw_rows_vanish": not bad,
       "D2_minimality_Hc_5_3": str(sp.expand(sp.together(subs0[symbol("Hc_5_3")]).subs(full))),
       "c_value": str(point[symbol("c")]),
       "wall_seconds": round(time.monotonic() - t0, 1)}
(OUT / "witness-saturated-T8.json").write_text(json.dumps(rec, indent=2, default=str) + "\n")
print(json.dumps({k: rec[k] for k in ("truncation_depth_T", "raw_row_count",
      "residual_vanishes_symbolically_on_solve", "point_free_nonzero",
      "NEGATIVE_CONTROL_all_raw_rows_vanish", "raw_rows_failing",
      "D2_minimality_Hc_5_3", "wall_seconds")}, indent=2))
