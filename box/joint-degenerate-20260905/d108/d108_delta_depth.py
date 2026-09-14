#!/usr/bin/env python3
"""Delta-depth analysis for D=108 delta=3 (corrected chart, SRC radius).

On the algebraically-dependent locus Delta = {A2=b, A3=c', B1=d, B2=e constants}
(outer blocks constant, hence F = h2^3 + b h2 + c', G = h2^2 + d h2 + e,
J(F,G) == 0), every Jacobian row of positive degree vanishes identically and the
F/G minor pole rows reduce to conditions on K2(sigma) alone:
    a_p := [t^p] K2(sigma) in Q[pi]  must vanish for p = 1..31,
    a_32 = (pi^2 - c)^4                (leading targets p^12 at F, p^8 at G).
This driver imposes a_p = 0 depth by depth (p = 1,2,...,32) on the corrected
h2 chart (116 free K2c + Hc_5_4, Hc_9_0, jet1, jet2, c), Q*-reducing on the
K2c/Hc coordinates only, and decides the residual in Singular over Q with the
localizer Zc*c-1 (and, separately, with D2-minimality Zm*jet1*jet2-1).
The first depth p* with a UNIT is where Delta dies; if none, Delta survives the
whole pole system and only the degree-0 Jacobian row (KJ t-power 178) kills.
"""
import json, subprocess, sys, time
from collections import defaultdict
from pathlib import Path
import sympy as sp
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from d108_common import build, qstar_reduce, local_rows, symbol, substitute_map
sys.path.insert(0, "/home/ubuntu/jc2/box/d108-rekill-20260905/work")
from rekill_engine import resolve_map

MAXP = int(sys.argv[1]) if len(sys.argv) > 1 else 32
t0 = time.monotonic()
obj = build()
k2, k2free, h3free = obj["k2"], obj["k2free"], obj["h3free"]
c = symbol("c"); jet1, jet2 = symbol("jet1"), symbol("jet2")
print(f"K2 built ({obj['build_seconds']}s cached); computing K2(sigma) to t^{MAXP} ...", flush=True)
t1 = time.monotonic()
loc = local_rows(k2, MAXP, False)          # {(n,k): coeff} = [t^n pi^k] K2(sigma)
print(f"K2(sigma) rows: {len(loc)} tags in {time.monotonic()-t1:.1f}s", flush=True)
# a_p rows
by_p = defaultdict(dict)
for (n, k), v in loc.items():
    by_p[n][k] = v
target = sp.Poly(sp.expand((symbol("pi")**2 - c)**4), symbol("pi"))
tcoef = {k: target.coeff_monomial(symbol("pi")**k) for k in range(9)}

def singular_dim(residual, tag, minimality=False):
    if not residual:
        return {"dimension": "no residual (affine space)", "unit_ideal": False}
    vars_ = sorted({str(s) for _l, v in residual for s in v.free_symbols})
    extra = ["Zc"] + (["Zm"] if minimality else [])
    ring = ",".join(vars_ + extra)
    lines = [f"ring R=0,({ring}),dp;"]
    gens = []
    for i, (l, v) in enumerate(residual):
        lines.append(f"poly r{i}={str(sp.expand(v)).replace('**','^')};"); gens.append(f"r{i}")
    lines.append("poly L=Zc*c-1;"); gens.append("L")
    if minimality:
        lines.append("poly M=Zm*jet1*jet2-1;"); gens.append("M")
    lines.append("ideal I=" + ",".join(gens) + ";")
    lines.append("option(redSB); ideal S=std(I);")
    lines.append('print("DIM"); dim(S); print("NF1"); reduce(1,S); print("SIZE"); size(S); quit;')
    script = HERE / f"depth_{tag}{'_min' if minimality else ''}.sing"
    script.write_text("\n".join(lines) + "\n")
    out = subprocess.run(["Singular", "-q", str(script)], text=True, capture_output=True, timeout=3000)
    (HERE / (script.name + ".out")).write_text(out.stdout + out.stderr)
    o = out.stdout.splitlines()
    def after(m):
        i = o.index(m); return o[i + 1].strip()
    try:
        d = int(after("DIM")); nf = after("NF1"); sz = after("SIZE")
    except Exception:
        return {"error": out.stdout[-500:] + out.stderr[-500:]}
    return {"dimension": d, "unit_ideal": (d == -1), "reduce_1": nf, "gb_size": sz,
            "active_variables": vars_}

eligible = set(k2free) | set(h3free)
subs, residual, ledger = {}, [], []
first_unit = None
for p in range(1, MAXP + 1):
    tp = time.monotonic()
    new = []
    for k in sorted(by_p.get(p, {})):
        v = by_p[p][k]
        if p == 32: v = v - tcoef.get(k, 0)
        new.append((f"a{p}_pi{k}", substitute_map(sp.expand(v), subs)))
    if p == 32:   # target rows absent from loc (zero coefficient) still count
        for k in range(9):
            if k not in by_p.get(32, {}) and tcoef.get(k, 0) != 0:
                new.append((f"a32_pi{k}", -tcoef[k]))
    rows = residual + new
    res, nsubs, piv, zeros = qstar_reduce(rows, eligible - set(subs))
    # compose substitutions
    for var, rhs in subs.items():
        subs[var] = substitute_map(rhs, nsubs)
    subs.update(nsubs); resolve_map(subs)
    residual = res
    rec = {"p": p, "new_rows": len(new), "new_pivots": [str(x.variable) for x in piv],
           "cumulative_pivots": len(subs), "residual_rows": len(residual),
           "residual_vars": sorted({str(s) for _l, v in residual for s in v.free_symbols}),
           "zero_rows": zeros}
    if residual:
        rec["residual"] = {l: str(v) for l, v in residual}
        rec["singular_c"] = singular_dim(residual, f"p{p}")
        rec["singular_c_min"] = singular_dim(residual, f"p{p}", minimality=True)
        if rec["singular_c"].get("unit_ideal") and first_unit is None:
            first_unit = p
    rec["seconds"] = round(time.monotonic() - tp, 1)
    ledger.append(rec)
    print(f"p={p:2d} new={len(new)} piv={len(piv)} cum={len(subs)} resid={len(residual)} "
          f"vars={rec['residual_vars']} dim={rec.get('singular_c',{}).get('dimension','-')} "
          f"dim_min={rec.get('singular_c_min',{}).get('dimension','-')} ({rec['seconds']}s)", flush=True)
    (HERE / "delta_depth_ledger.json").write_text(json.dumps(
        {"MAXP": MAXP, "first_unit_depth_p": first_unit, "ledger": ledger,
         "free_K2c": len(k2free), "h3_free": [str(v) for v in h3free],
         "eligible_pivot_coordinates": len(eligible),
         "wall_seconds": round(time.monotonic() - t0, 1)}, indent=1) + "\n")
    if first_unit is not None and p >= first_unit:
        break
print("FIRST UNIT DEPTH p* =", first_unit, "; total", round(time.monotonic() - t0, 1), "s")
