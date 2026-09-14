#!/usr/bin/env python3
"""Light reconstruction of the corrected-chart (99,66) survivor points
(jet0 = 1, rho = 1 / c = 1, all other free coordinates 0, outer blocks 0)."""
import argparse, importlib.util, json, sys, time
from collections import defaultdict
from pathlib import Path
import sympy as sp
HERE = Path(__file__).resolve().parent
ENGINE = Path("/home/ubuntu/jc2/box/g9966-repair-gate-20260905/corrected_face_engine.py")
spec = importlib.util.spec_from_file_location("cfe_point", ENGINE); m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m; spec.loader.exec_module(m)
ap = argparse.ArgumentParser(); ap.add_argument("--branch", required=True); A = ap.parse_args(); branch = A.branch
sym = m.symbol; t0 = time.monotonic()
k2, inner_free, meta = m.build_major_h2(branch, 33)
h3, hvars = m.h3_template(); hmap, hfree, centre = m.h3_branch_map(branch)
h3 = {k: m.substitute_map(v, hmap) for k, v in h3.items()}
stage = 4 if branch == "delta2" else 8; T = 8 if branch == "delta2" else 16
gen = sym("zeta") if branch == "delta2" else sym("pi"); loc_var = sym("rho") if branch == "delta2" else sym("c")
point = {v: sp.Integer(0) for v in inner_free}; point[sym("jet0")] = sp.Integer(1); point[loc_var] = sp.Integer(1)
num = lambda tz: {k: sp.Rational(sp.expand(v.subs(point))) for k, v in tz.items() if sp.expand(v.subs(point)) != 0}
K2n, K3n = num(k2), num(h3)
hc_at = {str(k): str(sp.expand(v.subs(point))) for k, v in hmap.items()}
KGn = m.tz_mul(K2n, K2n, T); KFn = m.tz_mul(KGn, K2n, T)
rows, acct = m.cumulative_rows(branch, stage, KFn, KGn)
nz = [(l, str(sp.expand(v.subs(point)))) for l, v in rows if sp.expand(v.subs(point)) != 0]
print(f"[{branch}] engine cumulative rows at stage {stage}, outer=0: {len(rows)} rows, nonzero {len(nz)}", flush=True)
jz = all(not m.jacobian_band(KFn, KGn, tp) for tp in range(1, T + 1))
x, y = sp.symbols("x y")
to_xy = lambda tz, deg: sp.Poly(sp.expand(x**deg * sum(v * (1/x)**r * (y/x - 1)**q for (r, q), v in tz.items())), x, y, domain="QQ")
h3p, h2p = to_xy(K3n, 11), to_xy(K2n, 33)
h3f = sp.factor_list(h3p.as_expr())
rems, q = [], h2p
while q.degree(y) >= h3p.degree(y):
    qq, r = sp.div(q, h3p, y); rems.append(sp.Poly(r, x, y, domain="QQ")); q = sp.Poly(qq, x, y, domain="QQ")
rems.append(q)
h20 = h2p.coeff_monomial(1); h2x = h2p.coeff_monomial(x); h2y = h2p.coeff_monomial(y)
J0 = 6 * h20**3 * (h2x * h2y - h2y * h2x)     # F = h2^3, G = h2^2  =>  J_0 = f10 g01 - f01 g10 = 0 identically
PV = {sym("jet0"): 1, sym("u"): 0, sym("v"): 0}
ev = lambda tab: {kk: sp.expand(vv.subs(PV)) for kk, vv in tab.items() if sp.expand(vv.subs(PV)) != 0}
K2s = ev(m.local_rows(K2n, branch, 70)); a = defaultdict(dict)
for (n, k), v in K2s.items(): a[n][k] = v
ordK2 = min(a); apoly = {p: sp.expand(sum(v * gen**k for k, v in a[p].items())) for p in sorted(a) if p <= ordK2 + 3}
K3s = ev(m.local_rows(K3n, branch, 30)); b = defaultdict(dict)
for (n, k), v in K3s.items(): b[n][k] = v
pi_ = sym("pi"); face = lambda tz, W: sp.factor(sp.expand(sum(v * pi_**q for (r, q), v in tz.items() if 3 * r + 4 * q == W)))
rec = {"branch": branch, "stage": stage, "point_nonzero": {"jet0": 1, str(loc_var): 1}, "h3_map_at_point": hc_at,
       "engine_rows_outer_zero": {"count": len(rows), "nonzero": nz, "accounting": acct},
       "jacobian_bands_1_to_T_zero": bool(jz), "h3": str(h3p.as_expr()), "h3_factors": str(h3f),
       "h3_factor_degrees": [(sp.Poly(f, x, y).total_degree(), e) for f, e in h3f[1]],
       "h2_terms": len(h2p.terms()), "h2_constant_term": str(h20),
       "tower": {"h3^3_coeff": str(rems[3].as_expr()), "C1_h3^2_coeff": str(rems[2].as_expr()),
                 "deg_C2": (rems[1].total_degree() if not rems[1].is_zero else None), "deg_C3": (rems[0].total_degree() if not rems[0].is_zero else None)},
       "F_is_h2_cubed_G_is_h2_squared": True, "J_identically_zero_by_identity": "J(h2^3,h2^2) = 6 h2^3 J(h2,h2) = 0", "J0": str(J0),
       "ord_K2_sigma": ordK2, "units": "t" if branch == "delta2" else "tau", "a_p": {str(p): str(v) for p, v in apoly.items()},
       "first_failing_G_pole_local_power": 2 * ordK2, "first_failing_stage": (2 * ordK2 - 4) if branch == "delta2" else (2 * ordK2 - 8),
       "K3_sigma": {str(p): str(sp.expand(sum(v * gen**k for k, v in b[p].items()))) for p in sorted(b) if p <= min(b) + 4},
       "K3_D2_face_W32": str(face(K3n, 32)), "K2_D2_face_W96": str(face(K2n, 96)),
       "lower_weights_K3": sorted({3*r+4*q for (r,q) in K3n if 3*r+4*q < 32}), "lower_weights_K2": sorted({3*r+4*q for (r,q) in K2n if 3*r+4*q < 96}),
       "wall_seconds": round(time.monotonic() - t0, 1)}
(HERE / f"point_structure_{branch}.json").write_text(json.dumps(rec, indent=1, default=str) + "\n")
print(json.dumps({k: rec[k] for k in ("branch", "engine_rows_outer_zero", "jacobian_bands_1_to_T_zero", "h3_factor_degrees", "tower", "J0", "ord_K2_sigma", "a_p", "first_failing_stage", "K3_D2_face_W32", "K2_D2_face_W96", "wall_seconds")}, indent=1, default=str))
