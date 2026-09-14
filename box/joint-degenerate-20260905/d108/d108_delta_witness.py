#!/usr/bin/env python3
"""Explicit point of Delta satisfying EVERY F/G minor pole row of the D=108
delta=3 corrected chart, including the leading targets (pi^2-c)^12 at F local
96 and (pi^2-c)^8 at G local 64, verified by DIRECT SUBSTITUTION (never through
pivots).  Outer blocks 0 (F = h2^3, G = h2^2), so all Jacobian rows of positive
degree vanish identically; the degree-0 row J_0 = f10*g01 - f01*g10 = 0 != 1.
"""
import json, sys, time
from collections import defaultdict
from pathlib import Path
import sympy as sp
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from d108_common import build, qstar_reduce, local_rows, symbol, substitute_map
sys.path.insert(0, "/home/ubuntu/jc2/box/d108-rekill-20260905/work")
from rekill_engine import resolve_map, tz_mul, raw_minor_support, jacobian_band
t0 = time.monotonic()
obj = build(); k2, k2free, h3free, h3, subs0 = obj["k2"], obj["k2free"], obj["h3free"], obj["h3"], obj["subs0"]
c, jet1, jet2, pi = symbol("c"), symbol("jet1"), symbol("jet2"), symbol("pi")
loc = local_rows(k2, 32, False)
by_p = defaultdict(dict)
for (n, k), v in loc.items(): by_p[n][k] = v
tpoly = sp.Poly(sp.expand((pi**2 - c)**4), pi); tcoef = {k: tpoly.coeff_monomial(pi**k) for k in range(9)}
rows = []
for p in range(1, 33):
    for k in sorted(by_p.get(p, {})):
        v = by_p[p][k] - (tcoef.get(k, 0) if p == 32 else 0)
        rows.append((f"a{p}_pi{k}", sp.expand(v)))
for k, tv in tcoef.items():
    if k not in by_p.get(32, {}) and tv != 0: rows.append((f"a32_pi{k}", -tv))
eligible = set(k2free) | set(h3free)
residual, subs, pivots, zeros = qstar_reduce(rows, eligible)
print("Delta full pole system: rows", len(rows), "pivots", len(pivots), "zero rows", zeros, "residual", len(residual), flush=True)
assert not residual
free_left = sorted(eligible - set(subs), key=str)
print("free K2c/Hc after all pole rows:", [str(v) for v in free_left], "count", len(free_left))
point = {v: sp.Integer(0) for v in eligible}; point[jet1] = point[jet2] = point[c] = sp.Integer(1)
full = dict(point)
for var, rhs in subs.items(): full[var] = sp.expand(sp.together(rhs).subs(point))
for var, rhs in subs0.items(): full[var] = sp.expand(sp.together(rhs).subs(full))
num = lambda tz: {k: sp.Rational(sp.expand(v.subs(full))) for k, v in tz.items() if sp.expand(v.subs(full)) != 0}
K2n, K3n = num(k2), num(h3)
# ---- direct verification of K2(sigma)
JV = {jet1: 1, jet2: 1}
ev = lambda tab: {kk: sp.expand(vv.subs(JV)) for kk, vv in tab.items() if sp.expand(vv.subs(JV)) != 0}
K2s = ev(local_rows(K2n, 40, False)); a = defaultdict(dict)
for (n, k), v in K2s.items(): a[n][k] = v
ordK2 = min(a); a32 = sp.expand(sum(v * pi**k for k, v in a[32].items()))
print("ord_t K2(sigma) =", ordK2, "; a_32 =", sp.factor(a32), "; equals (pi^2-1)^4:", sp.expand(a32 - (pi**2 - 1)**4) == 0)
# ---- direct verification of ALL F/G pole rows with leading targets (never through pivots)
TG, TF = 64, 96
KGn = tz_mul(K2n, K2n, TG); KFn = tz_mul(tz_mul(K2n, K2n, TF), K2n, TF)
gl, fl = ev(local_rows(KGn, TG, False)), ev(local_rows(KFn, TF, False))
tg = sp.Poly(sp.expand((pi**2 - 1)**8), pi); tf = sp.Poly(sp.expand((pi**2 - 1)**12), pi)
bad, cnt = [], {"F": 0, "G": 0}
for name, table, T, tgt in (("F", fl, TF, tf), ("G", gl, TG, tg)):
    for n in range(1, T + 1):
        for k in raw_minor_support(name, False).get(n, ()):
            cnt[name] += 1
            want = tgt.coeff_monomial(pi**k) if n == T else 0
            got = table.get((n, k), 0)
            if got != want: bad.append((f"{name}_local{n}_coord{k}", str(got), str(want)))
print("F/G pole rows checked:", cnt, "failing:", bad[:5], "count", len(bad))
# ---- Jacobian bands at the point (outer = 0): all t-powers 1..20 shown zero; J_0 row
Jz = all(not jacobian_band(tz_mul(tz_mul(K2n, K2n, tp), K2n, tp), tz_mul(K2n, K2n, tp), tp) for tp in range(1, 21))
x, y = sp.symbols("x y")
h2p = sp.Poly(sp.expand(x**36 * sum(v * (1/x)**r * (y/x - 1)**q for (r, q), v in K2n.items())), x, y, domain="QQ")
Fp, Gp = h2p**3, h2p**2
J0 = Fp.coeff_monomial(x) * Gp.coeff_monomial(y) - Fp.coeff_monomial(y) * Gp.coeff_monomial(x)
h2_0 = h2p.coeff_monomial(1)
print("Jacobian bands t=1..20 all zero:", Jz, "; J_0 =", J0, "; h2(0,0) =", h2_0)
pi_ = pi
face = lambda tz, W: sp.factor(sp.expand(sum(v * pi_**q for (r, q), v in tz.items() if 4 * r + 5 * q == W)))
print("K3 D2 face:", face(K3n, 35), "; K2 D2 face:", face(K2n, 140))
rec = {"rows": len(rows), "pivots": len(pivots), "zero_rows": zeros, "residual": len(residual),
       "free_after_all_pole_rows": [str(v) for v in free_left], "point": "jet1=jet2=c=1, all remaining free K2c/Hc = 0, pivots resolved",
       "ord_t_K2_sigma": ordK2, "a32": str(sp.factor(a32)), "a32_equals_target": bool(sp.expand(a32 - (pi**2 - 1)**4) == 0),
       "pole_rows_checked": cnt, "pole_rows_failing": bad, "jacobian_bands_1_20_zero": bool(Jz), "J0": str(J0),
       "K3_D2_face": str(face(K3n, 35)), "K2_D2_face": str(face(K2n, 140)),
       "K2_numeric": {f"{r}_{q}": str(v) for (r, q), v in sorted(K2n.items())},
       "K3_numeric": {f"{r}_{q}": str(v) for (r, q), v in sorted(K3n.items())},
       "wall_seconds": round(time.monotonic() - t0, 1)}
(HERE / "delta_full_pole_witness.json").write_text(json.dumps(rec, indent=1, default=str) + "\n")
print("done", rec["wall_seconds"], "s")
