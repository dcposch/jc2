#!/usr/bin/env python3
"""Lighter direct verification of the Delta full-pole witness (D=108): all G
pole rows at local powers 1..64 (leading target (pi^2-1)^8) by direct
substitution, plus a_p (p<=40) and the F leading target via a_32^3.  The F
rows at local <= 95 vanish on Delta as soon as ord K2(sigma) >= 32 (K2^3)."""
import json, sys, time
from collections import defaultdict
from pathlib import Path
import sympy as sp
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from d108_common import build, qstar_reduce, local_rows, symbol, substitute_map
sys.path.insert(0, "/home/ubuntu/jc2/box/d108-rekill-20260905/work")
from rekill_engine import tz_mul, raw_minor_support, jacobian_band
t0 = time.monotonic()
obj = build(); k2, k2free, h3free, h3, subs0 = obj["k2"], obj["k2free"], obj["h3free"], obj["h3"], obj["subs0"]
c, jet1, jet2, pi = symbol("c"), symbol("jet1"), symbol("jet2"), symbol("pi")
loc = local_rows(k2, 32, False); by_p = defaultdict(dict)
for (n, k), v in loc.items(): by_p[n][k] = v
tpoly = sp.Poly(sp.expand((pi**2 - c)**4), pi); tcoef = {k: tpoly.coeff_monomial(pi**k) for k in range(9)}
rows = []
for p in range(1, 33):
    for k in sorted(by_p.get(p, {})):
        rows.append((f"a{p}_pi{k}", sp.expand(by_p[p][k] - (tcoef.get(k, 0) if p == 32 else 0))))
for k, tv in tcoef.items():
    if k not in by_p.get(32, {}) and tv != 0: rows.append((f"a32_pi{k}", -tv))
eligible = set(k2free) | set(h3free)
residual, subs, pivots, zeros = qstar_reduce(rows, eligible); assert not residual
point = {v: sp.Integer(0) for v in eligible}; point[jet1] = point[jet2] = point[c] = sp.Integer(1)
full = dict(point)
for var, rhs in subs.items(): full[var] = sp.expand(sp.together(rhs).subs(point))
for var, rhs in subs0.items(): full[var] = sp.expand(sp.together(rhs).subs(full))
num = lambda tz: {k: sp.Rational(sp.expand(v.subs(full))) for k, v in tz.items() if sp.expand(v.subs(full)) != 0}
K2n, K3n = num(k2), num(h3)
JV = {jet1: 1, jet2: 1}
ev = lambda tab: {kk: sp.expand(vv.subs(JV)) for kk, vv in tab.items() if sp.expand(vv.subs(JV)) != 0}
K2s = ev(local_rows(K2n, 40, False)); a = defaultdict(dict)
for (n, k), v in K2s.items(): a[n][k] = v
ordK2 = min(a); a32 = sp.expand(sum(v * pi**k for k, v in a[32].items()))
print("reduction:", len(rows), "rows", len(pivots), "pivots", zeros, "zero rows; ord_t K2(sigma) at point =", ordK2,
      "; a_32 =", sp.factor(a32), "; a32 == (pi^2-1)^4:", sp.expand(a32 - (pi**2 - 1)**4) == 0, flush=True)
TG = 64
KGn = tz_mul(K2n, K2n, TG); gl = ev(local_rows(KGn, TG, False))
tg = sp.Poly(sp.expand((pi**2 - 1)**8), pi); bad = []; cnt = 0
for n in range(1, TG + 1):
    for k in raw_minor_support("G", False).get(n, ()):
        cnt += 1; want = tg.coeff_monomial(pi**k) if n == TG else 0
        if gl.get((n, k), 0) != want: bad.append((n, k, str(gl.get((n, k), 0)), str(want)))
print("G pole rows local 1..64 checked:", cnt, "failing:", len(bad), bad[:4], flush=True)
F_lead_ok = sp.expand(a32**3 - (pi**2 - 1)**12) == 0
Jz = all(not jacobian_band(tz_mul(tz_mul(K2n, K2n, tp), K2n, tp), tz_mul(K2n, K2n, tp), tp) for tp in range(1, 13))
x, y = sp.symbols("x y")
h2p = sp.Poly(sp.expand(x**36 * sum(v * (1/x)**r * (y/x - 1)**q for (r, q), v in K2n.items())), x, y, domain="QQ")
h3p = sp.Poly(sp.expand(x**9 * sum(v * (1/x)**r * (y/x - 1)**q for (r, q), v in K3n.items())), x, y, domain="QQ")
face = lambda tz, W: sp.factor(sp.expand(sum(v * pi**q for (r, q), v in tz.items() if 4 * r + 5 * q == W)))
rec = {"rows": len(rows), "pivots": len(pivots), "zero_rows": zeros, "free_after": [str(v) for v in sorted(eligible - set(subs), key=str)],
       "point": "jet1=jet2=c=1, remaining free K2c/Hc = 0, pivots resolved", "ord_t_K2_sigma": ordK2, "a32": str(sp.factor(a32)),
       "a32_equals_target": bool(sp.expand(a32 - (pi**2 - 1)**4) == 0), "F_leading_target_via_a32_cubed": bool(F_lead_ok),
       "G_pole_rows_checked": cnt, "G_pole_rows_failing": bad, "jacobian_bands_1_12_zero": bool(Jz),
       "h3_factor_degrees": [(sp.Poly(f, x, y).total_degree(), e) for f, e in sp.factor_list(h3p.as_expr())[1]],
       "h3": str(h3p.as_expr()), "K3_D2_face": str(face(K3n, 35)), "K2_D2_face": str(face(K2n, 140)),
       "Hc_at_point": {str(k): str(v) for k, v in full.items() if str(k).startswith("Hc_")},
       "K2_numeric": {f"{r}_{q}": str(v) for (r, q), v in sorted(K2n.items())},
       "wall_seconds": round(time.monotonic() - t0, 1)}
(HERE / "delta_full_pole_witness_G.json").write_text(json.dumps(rec, indent=1, default=str) + "\n")
print(json.dumps({k: rec[k] for k in ("ord_t_K2_sigma", "a32", "a32_equals_target", "F_leading_target_via_a32_cubed", "G_pole_rows_checked", "G_pole_rows_failing", "jacobian_bands_1_12_zero", "h3_factor_degrees", "K3_D2_face", "K2_D2_face", "free_after", "wall_seconds")}, indent=1, default=str))
