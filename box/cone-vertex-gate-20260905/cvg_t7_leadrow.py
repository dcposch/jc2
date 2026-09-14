#!/usr/bin/env python3
"""GATE (5) crux: the engines' tag schedules INCLUDE the leading local power
(D=108 F n=96 / G n=64; (99,66) d2 F n=81 / G n=54) and step3/step4 emit those
rows as '=0', with NO target subtraction.  Reading (A) = Fable: a_P = target.
Reading (B) = engine as coded: a_P = 0.  Decide whether Delta survives (B)."""
import sys, json, time
sys.path.insert(0, "box/d108-rekill-20260905/work")
import sympy as sp
import rekill_engine as RE
from rekill_engine import (SRC, minor_incidence, qstar_reduce, substitute_map,
                           build_major_h2, local_rows)
pi, c = sp.symbols("pi c")
t0 = time.monotonic(); res = {}

rows0, hvars, h3 = minor_incidence(SRC, SRC.k3_face, False)
resid0, subs0, _, _ = qstar_reduce(rows0, hvars)
h3r = {k: v for k, v in ((k, substitute_map(v, subs0)) for k, v in h3.items()) if v != 0}
DEEP = 40
k2, k2free, _ = build_major_h2(SRC, h3r, DEEP, False)
hfree = [v for v in hvars if v not in subs0]
tab = local_rows(k2, DEEP, False)
elig = set(k2free) | set(hfree)

for P, name in ((32, "B_a32_eq_0"), (33, "B_a33_too"), (36, "B_a36_too")):
    rows = []
    for n in range(1, P+1):
        for k in sorted({kk for (m, kk) in tab if m == n}):
            rows.append((f"a{n}_pi{k}", sp.expand(tab[(n, k)])))
    residual, subs, piv, zeros = qstar_reduce(rows, elig)
    const = [(l, str(v)) for l, v in residual if sp.expand(v).is_number]
    res[name] = {"depth": P, "rows": len(rows), "pivots": len(piv), "dependent_zero": zeros,
                 "residual_rows": len(residual), "CONSTANT_residual": const,
                 "residual": [(l, str(v)[:110]) for l, v in residual[:5]],
                 "n_free_after": len(elig - set(subs))}
    print(f"D108 reading-B a_p=0 for p<= {P}: rows={len(rows)} piv={len(piv)} "
          f"resid={len(residual)} CONST={const} free={len(elig-set(subs))}", flush=True)

json.dump(res, open("box/cone-vertex-gate-20260905/t7_leadrow.json","w"), indent=1, default=str)
print("secs", round(time.monotonic()-t0,1))
