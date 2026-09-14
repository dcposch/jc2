#!/usr/bin/env python3
"""GATE (5): reading (B) on the corrected (99,66) delta2 chart -- impose
a_p = 0 for p <= 27 (the engine's literal row set through F local 81 / G 54)."""
import sys, json, time, importlib.util
import sympy as sp
spec = importlib.util.spec_from_file_location("cfe", "box/g9966-repair-gate-20260905/corrected_face_engine.py")
E = importlib.util.module_from_spec(spec); sys.modules["cfe"] = E; spec.loader.exec_module(E)
t0 = time.monotonic(); P = 27; branch = "delta2"
k2, inner_free, _ = E.build_major_h2(branch, P)
tab = E.local_rows(k2, branch, P)
loc = sp.Symbol("rho")
rows = [(f"a{n}_z{k}", sp.expand(v)) for (n, k), v in sorted(tab.items()) if n <= P]
elig = set(inner_free) - {loc}
residual, subs, piv, zeros = E.qstar_reduce(rows, elig)
const = [(l, str(v)) for l, v in residual if sp.expand(v).is_number]
print(f"delta2 reading-B a_p=0 for p<=27: rows={len(rows)} piv={len(piv)} zeros={zeros} "
      f"resid={len(residual)} CONST={const}", flush=True)
for l, v in residual[:6]: print("   RESID", l, "=", str(v)[:140], flush=True)
json.dump({"branch": branch, "depth": P, "rows": len(rows), "pivots": len(piv),
           "dependent_zero": zeros, "residual_rows": len(residual),
           "CONSTANT_residual": const,
           "residual": [(l, str(v)[:160]) for l, v in residual[:10]],
           "n_free_after": len(elig - set(subs)), "secs": round(time.monotonic()-t0,1)},
          open("box/cone-vertex-gate-20260905/t8_g9966_leadrow.json","w"), indent=1)
print("secs", round(time.monotonic()-t0,1))
