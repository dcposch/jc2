#!/usr/bin/env python3
"""GATE (5): decide the h3-on-D1 probe at FULL h2-only depth by exhibiting a
point (free coords -> 0 under the pin jet1=1, jet2=-1/2, c=1) and checking the
RAW rows directly; also report the residual generators if it fails."""
import sys, json, time
sys.path.insert(0, "box/d108-rekill-20260905/work")
import sympy as sp
from rekill_engine import (SRC, minor_incidence, qstar_reduce, substitute_map,
                           build_major_h2, local_rows, resolve_map)
pi, c, jet1, jet2 = sp.symbols("pi c jet1 jet2"); P = 32; t0 = time.monotonic()
pin = {jet1: sp.Integer(1), jet2: sp.Rational(-1, 2)}
rows0, hvars, h3 = minor_incidence(SRC, SRC.k3_face, False)
resid0, subs0, _, _ = qstar_reduce(rows0, hvars)
h3r = {k: v for k, v in ((k, sp.expand(substitute_map(v, subs0).subs(pin)))
                         for k, v in h3.items()) if v != 0}
k2, k2free, _ = build_major_h2(SRC, h3r, P, False)
hfree = [v for v in hvars if v not in subs0]
tab = local_rows(k2, P, False)
tp = sp.Poly(sp.expand((pi**2 - c)**4), pi)
tgt = {k: tp.coeff_monomial(pi**k) for k in range(9)}
rows = []
for n in range(1, P+1):
    for k in sorted({kk for (m, kk) in tab if m == n} | (set(tgt) if n == P else set())):
        v = sp.expand(tab.get((n, k), sp.Integer(0)))
        if n == P: v = sp.expand(v - tgt.get(k, 0))
        rows.append((f"a{n}_pi{k}", v))
rows = [(l, sp.expand(v.subs(pin)) if hasattr(v, "subs") else v) for l, v in rows]
elig = set(k2free) | set(hfree)
residual, subs, piv, zeros = qstar_reduce(rows, elig)
free_after = sorted(elig - set(subs), key=str)
print("probe full depth: rows", len(rows), "pivots", len(piv), "residual", len(residual),
      "free_after", len(free_after), flush=True)
out = {"pin": "jet1=1, jet2=-1/2, c=1", "rows": len(rows), "pivots": len(piv),
       "dependent_zero": zeros, "residual_rows": len(residual),
       "residual_full": [(l, str(v)) for l, v in residual],
       "n_free_after": len(free_after)}
# try the all-zero point on the residual, then on the RAW rows
for name, val in (("free=0", sp.Integer(0)), ("free=1", sp.Integer(1))):
    pt = {s: val for s in free_after}; pt[c] = sp.Integer(1)
    rz = [(l, sp.expand(v.subs(pt))) for l, v in residual]
    bad = [(l, str(x)[:70]) for l, x in rz if x != 0]
    out[f"residual_at_{name}"] = {"nonzero": len(bad), "sample": bad[:4]}
    print(f"  residual at {name}: nonzero {len(bad)} {bad[:3]}", flush=True)
    if not bad:
        full = dict(subs)
        for _ in range(4):
            full = {v: sp.expand(sp.together(r).subs(pt)) if hasattr(r,"subs") else r
                    for v, r in full.items()}
        full.update(pt); resolve_map(full)
        raw = [(l, sp.expand(v.subs(full))) for l, v in rows]
        rb = [(l, str(x)[:70]) for l, x in raw if x != 0]
        out[f"RAWrows_at_{name}"] = {"nonzero": len(rb), "sample": rb[:4]}
        print(f"  RAW rows at {name}: nonzero {len(rb)} {rb[:3]}", flush=True)
        break
json.dump(out, open("box/cone-vertex-gate-20260905/t9_probe_point.json","w"), indent=1, default=str)
print("secs", round(time.monotonic()-t0,1))
