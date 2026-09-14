#!/usr/bin/env python3
"""(99,66) delta=2 / delta=5/2 corrected-face charts (repair-gate diagnostic
engine, imported read-only): (A) reconstruct the survivor point as polynomials
and compute its Jacobian / root configuration; (B) Delta-depth analysis: on the
algebraically-dependent locus (outer blocks constant, F = h2^3+.., G = h2^2+..,
J == 0) impose a_p := [t^p] K2(sigma) = 0 depth by depth and decide in Singular.

Ring map: t = 1/x, w = t*y, z = w-1; K3 = t^11 h3, K2 = t^33 h2 (top z^24(1+z)^9).
delta2 : y = jet0 + u t + zeta t^2  (w = jet0 t + u t^2 + zeta t^3), local power n = r+d+2a+3k (k = zeta-power)
delta52: t = tau^2, y = jet0 + u t + v t^2 + pi t^(5/2), local power n (tau-units) = 2r+2d+4a+6b+7k
Leading targets on Delta: h2 ~ h3^3 at the minor place, so
delta2 : a_27 = (zeta^2 (zeta+3 rho))^3 ;  delta52: a_63 = (pi (pi^2 - c))^3.
"""
import argparse, importlib.util, json, subprocess, sys, time
from collections import defaultdict
from pathlib import Path
import sympy as sp
HERE = Path(__file__).resolve().parent
ENGINE = Path("/home/ubuntu/jc2/box/g9966-repair-gate-20260905/corrected_face_engine.py")
spec = importlib.util.spec_from_file_location("cfe", ENGINE); m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m; spec.loader.exec_module(m)
ap = argparse.ArgumentParser(); ap.add_argument("--branch", required=True); ap.add_argument("--maxp", type=int, default=None)
ap.add_argument("--skip-depth", action="store_true")
A = ap.parse_args(); branch = A.branch
sym = m.symbol
t0 = time.monotonic()
max_t = 33
k2, inner_free, meta = m.build_major_h2(branch, max_t)
h3, hvars = m.h3_template(); hmap, hfree, centre = m.h3_branch_map(branch)
h3 = {k: m.substitute_map(v, hmap) for k, v in h3.items()}
k2free = sorted([v for v in inner_free if str(v).startswith("K2c_")], key=str)
hc_free = sorted([v for v in inner_free if str(v).startswith("Hc_")], key=str)
params = sorted([v for v in inner_free if not (str(v).startswith("K2c_") or str(v).startswith("Hc_"))], key=str)
print(f"[{branch}] K2 slots {len(k2)}, K2c free {len(k2free)}, Hc free {hc_free}, params {params}", flush=True)
stage = 4 if branch == "delta2" else 8
gen = sym("zeta") if branch == "delta2" else sym("pi")
loc_var = sym("rho") if branch == "delta2" else sym("c")
P = 27 if branch == "delta2" else 63
if branch == "delta2":
    target = sp.expand((gen**2 * (gen + 3 * sym("rho")))**3)
else:
    target = sp.expand((gen * (gen**2 - sym("c")))**3)
tpoly = sp.Poly(target, gen); tcoef = {k: tpoly.coeff_monomial(gen**k) for k in range(tpoly.degree() + 1)}

# ---------------- (A) the survivor point
point = {v: sp.Integer(0) for v in inner_free}
point[sym("jet0")] = sp.Integer(1); point[loc_var] = sp.Integer(1)
num = lambda tz: {k: sp.Rational(sp.expand(v.subs(point))) for k, v in tz.items() if sp.expand(v.subs(point)) != 0}
K2n, K3n = num(k2), num(h3)
hc_at = {str(k): str(sp.expand(v.subs(point))) for k, v in hmap.items()}
print("h3 map at point:", hc_at)
T = 8 if branch == "delta2" else 16
KGn = m.tz_mul(K2n, K2n, T); KFn = m.tz_mul(KGn, K2n, T)
rows, acct = m.cumulative_rows(branch, stage, KFn, KGn)
imgs = [(l, sp.expand(v.subs(point))) for l, v in rows]
nz = [(l, str(v)) for l, v in imgs if v != 0]
print(f"engine cumulative rows at stage {stage} with outer=0: {len(rows)} rows, nonzero: {nz[:5]} (count {len(nz)})")
x, y = sp.symbols("x y")
def to_xy(tz, deg):
    return sp.Poly(sp.expand(x**deg * sum(v * (1/x)**r * (y/x - 1)**q for (r, q), v in tz.items())), x, y, domain="QQ")
h3p, h2p = to_xy(K3n, 11), to_xy(K2n, 33)
assert h3p.total_degree() == 11 and h2p.total_degree() == 33
print("h3 =", h3p.as_expr()); print("h3 factors:", sp.factor_list(h3p.as_expr()))
print("h2 factor degrees:", [(sp.Poly(f, x, y).total_degree(), e) for f, e in sp.factor_list(h2p.as_expr())[1]])
rems, q = [], h2p
while q.degree(y) >= h3p.degree(y):
    qq, r = sp.div(q, h3p, y); rems.append(sp.Poly(r, x, y, domain="QQ")); q = sp.Poly(qq, x, y, domain="QQ")
rems.append(q)
print("h3-adic expansion of h2 (deg of coefficient of h3^i):", [(i, (r.total_degree() if not r.is_zero else None)) for i, r in enumerate(rems)])
C3, C2, C1, C0 = rems[0], rems[1], rems[2], rems[3]
Fp, Gp = h2p**3, h2p**2
Jp = Fp.diff(x) * Gp.diff(y) - Fp.diff(y) * Gp.diff(x)
J0 = Fp.coeff_monomial(x) * Gp.coeff_monomial(y) - Fp.coeff_monomial(y) * Gp.coeff_monomial(x)
print("J(F,G) == 0:", Jp.is_zero, "; J_0 =", J0, "; F^2-G^3 == 0:", (Fp**2 - Gp**3).is_zero)
K2s = m.local_rows(K2n, branch, 80); a = defaultdict(dict)
for (n, k), v in K2s.items(): a[n][k] = v
ordK2 = min(a)
apoly = {p: sp.expand(sum(v * gen**k for k, v in a[p].items())) for p in sorted(a) if p <= ordK2 + 3}
print("K2(sigma): ord =", ordK2, "(units:", "t" if branch == "delta2" else "tau", ") a_p:", apoly)
K3s = m.local_rows(K3n, branch, 30); b = defaultdict(dict)
for (n, k), v in K3s.items(): b[n][k] = v
print("K3(sigma) =", {p: sp.expand(sum(v * gen**k for k, v in b[p].items())) for p in sorted(b) if p <= min(b) + 6})
pi_ = sym("pi")
face = lambda tz, W: sp.factor(sp.expand(sum(v * pi_**q for (r, q), v in tz.items() if 3 * r + 4 * q == W)))
print("K3 D2 face (W=32):", face(K3n, 32), "| lower:", sorted({3*r+4*q for (r,q) in K3n if 3*r+4*q < 32}))
print("K2 D2 face (W=96):", face(K2n, 96), "| lower:", sorted({3*r+4*q for (r,q) in K2n if 3*r+4*q < 96}))
recA = {"branch": branch, "stage": stage, "point_nonzero": {"jet0": 1, str(loc_var): 1},
        "h3_map_at_point": hc_at, "engine_rows_outer_zero": {"count": len(rows), "nonzero": nz, "accounting": acct},
        "h3": str(h3p.as_expr()), "h3_factors": str(sp.factor_list(h3p.as_expr())),
        "h2_factor_degrees": [(sp.Poly(f, x, y).total_degree(), e) for f, e in sp.factor_list(h2p.as_expr())[1]],
        "tower": {"h3^3_coeff": str(C0.as_expr()), "C1_h3^2_coeff": str(C1.as_expr()),
                  "deg_C2": (C2.total_degree() if not C2.is_zero else None), "deg_C3": (C3.total_degree() if not C3.is_zero else None)},
        "J_identically_zero": bool(Jp.is_zero), "J0": str(J0), "F2_minus_G3_zero": bool((Fp**2-Gp**3).is_zero),
        "ord_K2_sigma": ordK2, "a_p": {str(p): str(v) for p, v in apoly.items()},
        "first_failing_G_pole_local_power": 2 * ordK2,
        "first_failing_stage": (2 * ordK2 - 4) if branch == "delta2" else (2 * ordK2 - 8),
        "K3_sigma": {str(p): str(sp.expand(sum(v * gen**k for k, v in b[p].items()))) for p in sorted(b) if p <= min(b) + 6},
        "K3_D2_face": str(face(K3n, 32)), "K2_D2_face": str(face(K2n, 96)), "wall_A": round(time.monotonic() - t0, 1)}
(HERE / f"point_structure_{branch}.json").write_text(json.dumps(recA, indent=1, default=str) + "\n")
if A.skip_depth: sys.exit(0)

# ---------------- (B) Delta-depth
MAXP = A.maxp or P
t1 = time.monotonic()
loc = m.local_rows(k2, branch, MAXP)
print(f"K2(sigma) symbolic rows to {MAXP}: {len(loc)} tags in {time.monotonic()-t1:.1f}s", flush=True)
by_p = defaultdict(dict)
for (n, k), v in loc.items(): by_p[n][k] = v

def singular_dim(residual, tag):
    vars_ = sorted({str(s) for _l, v in residual for s in v.free_symbols})
    lines = [f"ring R=0,({','.join(vars_ + ['Zl'])}),dp;"]; gens = []
    for i, (l, v) in enumerate(residual):
        lines.append(f"poly r{i}={str(sp.expand(v)).replace('**','^')};"); gens.append(f"r{i}")
    lines.append(f"poly L=Zl*{loc_var}-1;"); gens.append("L")
    lines.append("ideal I=" + ",".join(gens) + "; option(redSB); ideal S=std(I);")
    lines.append('print("DIM"); dim(S); print("NF1"); reduce(1,S); print("SIZE"); size(S); quit;')
    script = HERE / f"depth_{branch}_{tag}.sing"; script.write_text("\n".join(lines) + "\n")
    out = subprocess.run(["Singular", "-q", str(script)], text=True, capture_output=True, timeout=3000)
    (HERE / (script.name + ".out")).write_text(out.stdout + out.stderr)
    o = out.stdout.splitlines()
    try:
        d = int(o[o.index("DIM") + 1]); nf = o[o.index("NF1") + 1]; sz = o[o.index("SIZE") + 1]
    except Exception:
        return {"error": (out.stdout + out.stderr)[-600:]}
    return {"dimension": d, "unit_ideal": d == -1, "reduce_1": nf, "gb_size": sz, "active_variables": vars_}

eligible = set(k2free) | set(hc_free)
subs, residual, ledger, first_unit = {}, [], [], None
for p in range(1, MAXP + 1):
    tp = time.monotonic(); new = []
    for k in sorted(by_p.get(p, {})):
        v = by_p[p][k]
        if p == P: v = v - tcoef.get(k, 0)
        new.append((f"a{p}_{gen}{k}", m.substitute_map(sp.expand(v), subs)))
    if p == P:
        for k, tv in tcoef.items():
            if k not in by_p.get(P, {}) and tv != 0: new.append((f"a{P}_{gen}{k}", -tv))
    res, nsubs, piv, zeros = m.qstar_reduce(residual + new, eligible - set(subs))
    for var, rhs in subs.items(): subs[var] = m.substitute_map(rhs, nsubs)
    subs.update(nsubs); m.resolve_map(subs); residual = res
    rec = {"p": p, "new_rows": len(new), "new_pivots": [str(v.variable) for v in piv], "cumulative_pivots": len(subs),
           "residual_rows": len(residual), "residual_vars": sorted({str(s) for _l, v in residual for s in v.free_symbols}), "zero_rows": zeros}
    if residual:
        rec["residual"] = {l: str(v) for l, v in residual}
        rec["singular"] = singular_dim(residual, f"p{p}")
        if rec["singular"].get("unit_ideal") and first_unit is None: first_unit = p
    rec["seconds"] = round(time.monotonic() - tp, 1); ledger.append(rec)
    print(f"p={p:2d} new={len(new)} piv={len(piv)} cum={len(subs)} resid={len(residual)} vars={rec['residual_vars']} "
          f"dim={rec.get('singular',{}).get('dimension','-')} ({rec['seconds']}s)", flush=True)
    (HERE / f"delta_depth_{branch}.json").write_text(json.dumps({"branch": branch, "MAXP": MAXP, "target_depth_P": P,
        "target": str(target), "first_unit_depth_p": first_unit, "ledger": ledger, "K2c_free": len(k2free),
        "Hc_free": [str(v) for v in hc_free], "params": [str(v) for v in params],
        "wall_seconds": round(time.monotonic() - t0, 1)}, indent=1) + "\n")
    if first_unit is not None: break
print("FIRST UNIT DEPTH p* =", first_unit, "; total", round(time.monotonic() - t0, 1), "s")
