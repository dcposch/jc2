#!/usr/bin/env python3
"""GATE (3): independent rerun of the D=108 h2-only pole system to full depth.
Rows: a_p = 0 (as polys in pi) for p=1..31 ; a_32 = (pi^2-c)^4.
Then an EXPLICIT WITNESS verified by DIRECT substitution into the raw rows."""
import sys, json, time
sys.path.insert(0, "box/d108-rekill-20260905/work")
import sympy as sp
import rekill_engine as RE
from rekill_engine import (SRC, minor_incidence, qstar_reduce, substitute_map,
                           build_major_h2, local_rows, resolve_map)

t0 = time.monotonic(); P = 32; jet0free = False
rows0, hvars, h3 = minor_incidence(SRC, SRC.k3_face, jet0free)
resid0, subs0, piv0, _ = qstar_reduce(rows0, hvars)
h3r = {k: v for k, v in ((k, substitute_map(v, subs0)) for k, v in h3.items()) if v != 0}
k2, k2free, k2meta = build_major_h2(SRC, h3r, P, jet0free)
hfree = [v for v in hvars if v not in subs0]
print("h3 incidence residual:", len(resid0), "| h3 free:", [str(v) for v in hfree],
      "| K2c free:", len(k2free), flush=True)

pi, c = sp.Symbol("pi"), sp.Symbol("c")
jet1, jet2 = sp.Symbol("jet1"), sp.Symbol("jet2")
tab = local_rows(k2, P, jet0free)          # {(local_power, pi_deg): expr}
target = sp.Poly(sp.expand((pi**2 - c)**4), pi)
tgt = {k: target.coeff_monomial(pi**k) for k in range(9)}

raw_rows = []
for n in range(1, P+1):
    ks = sorted({k for (m, k) in tab if m == n})
    for k in (ks if ks else []):
        v = sp.expand(tab.get((n, k), sp.Integer(0)))
        if n == P: v = sp.expand(v - tgt.get(k, 0))
        raw_rows.append((f"a{n}_pi{k}", v))
    if n == P:
        for k in range(9):
            if k not in ks and tgt.get(k, 0) != 0:
                raw_rows.append((f"a{n}_pi{k}", sp.expand(-tgt[k])))
raw_rows = [(l, v) for l, v in raw_rows]
print("raw rows p=1..32:", len(raw_rows), "| identically zero:",
      sum(1 for _, v in raw_rows if v == 0), flush=True)

eligible = set(k2free) | set(hfree)
residual, subs, pivots, zeros = qstar_reduce(raw_rows, eligible)
print("Q* pivots:", len(pivots), "dependent-zero:", zeros, "RESIDUAL:", len(residual), flush=True)
for l, v in residual[:6]: print("   RESID", l, "=", str(v)[:120], flush=True)

# ---- WITNESS: remaining free -> 0, jet1=jet2=c=1, resolve, DIRECT substitution
free_after = sorted(eligible - set(subs), key=str)
pt = {s: sp.Integer(0) for s in free_after}
pt[jet1] = sp.Integer(1); pt[jet2] = sp.Integer(1); pt[c] = sp.Integer(1)
full = dict(subs)
for _ in range(3):
    full = {v: sp.expand(sp.together(r).subs(pt)) for v, r in full.items()}
full.update(pt)
resolve_map(full)
k2pt = {kq: sp.expand(v.subs(full)) if getattr(v, "free_symbols", set()) else v
        for kq, v in k2.items()}
leftover = set()
for v in k2pt.values():
    if hasattr(v, "free_symbols"): leftover |= (v.free_symbols - {pi})
print("WITNESS unresolved symbols in K2:", sorted(map(str, leftover))[:8], flush=True)
tabw = local_rows(k2pt, P, False)
tabw = {kk: sp.expand(vv.subs({jet1: 1, jet2: 1})) if hasattr(vv, "subs") else vv
        for kk, vv in tabw.items()}
viol = [(n, k, str(v)[:60]) for (n, k), v in sorted(tabw.items()) if n < P and sp.expand(v) != 0]
a32 = sp.expand(sum(tabw.get((P, k), 0) * pi**k for k in range(0, 40)))
print("WITNESS a_p != 0 for p<32:", len(viol), viol[:5], flush=True)
print("WITNESS a_32 =", sp.factor(a32), "| target (pi^2-1)^4 match:",
      sp.expand(a32 - (pi**2-1)**4) == 0, flush=True)
# localizers
hc53 = sp.expand(sp.Symbol("Hc_5_3").subs(full)) if sp.Symbol("Hc_5_3") in full else "not-a-symbol"
print("LOCALIZERS: c =", full.get(c), "| Hc_5_3 =", hc53, flush=True)
json.dump({"h3_incidence_residual": len(resid0), "raw_rows": len(raw_rows),
           "identically_zero_rows": sum(1 for _, v in raw_rows if v == 0),
           "Qstar_pivots": len(pivots), "dependent_zero": zeros,
           "residual": [(l, str(v)[:200]) for l, v in residual],
           "free_after": [str(s) for s in free_after],
           "witness_violations_p_lt_32": viol,
           "witness_a32": str(sp.factor(a32)),
           "witness_a32_matches_target": bool(sp.expand(a32-(pi**2-1)**4)==0),
           "localizer_c": str(full.get(c)), "localizer_Hc_5_3": str(hc53),
           "secs": round(time.monotonic()-t0,1)},
          open("box/cone-vertex-gate-20260905/t3_d108_depth.json","w"), indent=1)
print("secs", round(time.monotonic()-t0,1))
