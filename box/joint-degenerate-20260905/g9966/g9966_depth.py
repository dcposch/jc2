#!/usr/bin/env python3
"""Delta-depth analysis on the CORRECTED (99,66) charts (repair-gate engine).
On Delta (outer blocks constant; F = h2^3+.., G = h2^2+..; J == 0) the pole
rows reduce to a_p := [t^p]K2(sigma) = 0 for p < P and a_P = leading target,
P = 27 (delta2, t-units; target (zeta^2(zeta+3rho))^3 from h2 ~ h3^3) and
P = 63 (delta52, tau-units; target (pi(pi^2-c))^3).  Q* pivots on K2c/Hc only;
residual decided in Singular over Q with the branch localizer."""
import argparse, importlib.util, json, subprocess, sys, time
from collections import defaultdict
from pathlib import Path
import sympy as sp
HERE = Path(__file__).resolve().parent
ENGINE = Path("/home/ubuntu/jc2/box/g9966-repair-gate-20260905/corrected_face_engine.py")
spec = importlib.util.spec_from_file_location("cfe_depth", ENGINE); m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m; spec.loader.exec_module(m)
ap = argparse.ArgumentParser(); ap.add_argument("--branch", required=True); ap.add_argument("--maxp", type=int, default=None)
A = ap.parse_args(); branch = A.branch; sym = m.symbol; t0 = time.monotonic()
k2, inner_free, meta = m.build_major_h2(branch, 33)
k2free = sorted([v for v in inner_free if str(v).startswith("K2c_")], key=str)
hc_free = sorted([v for v in inner_free if str(v).startswith("Hc_")], key=str)
params = sorted([v for v in inner_free if not (str(v).startswith("K2c_") or str(v).startswith("Hc_"))], key=str)
gen = sym("zeta") if branch == "delta2" else sym("pi"); loc_var = sym("rho") if branch == "delta2" else sym("c")
P = 27 if branch == "delta2" else 63
target = sp.expand((gen**2 * (gen + 3 * sym("rho")))**3) if branch == "delta2" else sp.expand((gen * (gen**2 - sym("c")))**3)
tpoly = sp.Poly(target, gen); tcoef = {k: tpoly.coeff_monomial(gen**k) for k in range(tpoly.degree() + 1)}
MAXP = A.maxp or P
print(f"[{branch}] K2c free {len(k2free)}, Hc free {hc_free}, params {params}; depth to {MAXP} (target at {P})", flush=True)
t1 = time.monotonic(); loc = m.local_rows(k2, branch, MAXP)
print(f"K2(sigma) symbolic rows to {MAXP}: {len(loc)} tags in {time.monotonic()-t1:.1f}s", flush=True)
by_p = defaultdict(dict)
for (n, k), v in loc.items(): by_p[n][k] = v
def singular_dim(residual, tag):
    if any((not v.free_symbols) and v != 0 for _l, v in residual):
        return {"dimension": -1, "unit_ideal": True, "note": "nonzero constant residual row"}
    vars_ = sorted({str(s) for _l, v in residual for s in v.free_symbols} | {str(loc_var)})
    lines = [f"ring R=0,({','.join(vars_ + ['Zl'])}),dp;"]; gens = []
    for i, (l, v) in enumerate(residual):
        lines.append(f"poly r{i}={str(sp.expand(v)).replace('**','^')};"); gens.append(f"r{i}")
    lines.append(f"poly L=Zl*{loc_var}-1;"); gens.append("L")
    lines.append("ideal I=" + ",".join(gens) + "; option(redSB); ideal S=std(I);")
    lines.append('print("DIM"); dim(S); print("NF1"); reduce(1,S); print("SIZE"); size(S); quit;')
    script = HERE / f"depth_{branch}_{tag}.sing"; script.write_text("\n".join(lines) + "\n")
    out = subprocess.run(["Singular", "-q", str(script)], text=True, capture_output=True, timeout=3000)
    (HERE / (script.name + ".out")).write_text(out.stdout + out.stderr); o = out.stdout.splitlines()
    try: d = int(o[o.index("DIM") + 1]); nf = o[o.index("NF1") + 1]; sz = o[o.index("SIZE") + 1]
    except Exception: return {"error": (out.stdout + out.stderr)[-600:]}
    return {"dimension": d, "unit_ideal": d == -1, "reduce_1": nf, "gb_size": sz, "active_variables": vars_}
eligible = set(k2free) | set(hc_free); subs, residual, ledger, first_unit = {}, [], [], None
for p in range(1, MAXP + 1):
    tp = time.monotonic(); new = []
    for k in sorted(by_p.get(p, {})):
        v = by_p[p][k] - (tcoef.get(k, 0) if p == P else 0)
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
        rec["residual"] = {l: str(v) for l, v in residual}; rec["singular"] = singular_dim(residual, f"p{p}")
        if rec["singular"].get("unit_ideal") and first_unit is None: first_unit = p
    rec["seconds"] = round(time.monotonic() - tp, 1); ledger.append(rec)
    print(f"p={p:2d} new={len(new)} piv={len(piv)} cum={len(subs)} resid={len(residual)} vars={rec['residual_vars']} dim={rec.get('singular',{}).get('dimension','-')} ({rec['seconds']}s)", flush=True)
    (HERE / f"delta_depth_{branch}.json").write_text(json.dumps({"branch": branch, "MAXP": MAXP, "target_depth_P": P, "target": str(target),
        "first_unit_depth_p": first_unit, "ledger": ledger, "K2c_free": len(k2free), "Hc_free": [str(v) for v in hc_free],
        "params": [str(v) for v in params], "free_after": [str(v) for v in sorted(eligible - set(subs), key=str)],
        "wall_seconds": round(time.monotonic() - t0, 1)}, indent=1) + "\n")
    if first_unit is not None: break
print("FIRST UNIT DEPTH p* =", first_unit, "; total", round(time.monotonic() - t0, 1), "s")
