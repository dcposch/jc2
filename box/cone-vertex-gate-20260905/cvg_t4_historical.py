#!/usr/bin/env python3
"""GATE (4): on the OLD charged engines, run the Delta-subsystem (h2-only pole
rows, no Jacobian rows, no outer coordinates) to the depth of the reported
kill stage, and report the residual."""
import sys, json, time, importlib.util
import sympy as sp

def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec); sys.modules[name] = m
    spec.loader.exec_module(m); return m

ENGINES = {
 "pristine": "/tmp/jc2-lane.zr6VVM/inputs/band_engine.py",
 "precise":  "box/g9966-d2-precise-20260905/band_engine.py",
 "corrected":"box/g9966-repair-gate-20260905/corrected_face_engine.py",
}
# depth of K2 local rows corresponding to the reported kill stage
DEPTH = {"delta2": 4, "delta52": 8}
out, t0 = {}, time.monotonic()
for ename, epath in ENGINES.items():
    try: E = load(epath, f"eng_{ename}")
    except Exception as ex:
        out[ename] = {"LOAD_ERROR": str(ex)[:200]}; print(ename, "LOAD ERROR", ex); continue
    for branch, P in DEPTH.items():
        try:
            sig = E.build_major_h2.__code__.co_varnames[:E.build_major_h2.__code__.co_argcount]
            k2, inner_free, major = E.build_major_h2(branch, P)
            tab = E.local_rows(k2, branch, P) if "branch" in E.local_rows.__code__.co_varnames \
                  else E.local_rows(k2, P)
            rows = [(f"a{n}_pi{k}", sp.expand(v)) for (n, k), v in sorted(tab.items()) if n <= P]
            loc = sp.Symbol("rho" if branch == "delta2" else "c")
            elig = set(inner_free) - {loc}
            residual, subs, pivots, zeros = E.qstar_reduce(rows, elig)
            const = [(l, v) for l, v in residual if sp.expand(v).is_number]
            out.setdefault(ename, {})[branch] = {
                "depth_K2_local": P, "rows": len(rows), "pivots": len(pivots),
                "dependent_zero": zeros, "residual_rows": len(residual),
                "residual": [(l, str(v)[:100]) for l, v in residual[:8]],
                "CONSTANT_residual_rows": [(l, str(v)) for l, v in const],
                "Delta_T_EMPTY_by_constant_row": bool(const),
                "eligible": len(elig), "localizer_excluded": str(loc)}
            print(f"{ename:10s} {branch:7s} rows={len(rows):3d} piv={len(pivots):3d} "
                  f"resid={len(residual):2d} CONST={[(l,str(v)) for l,v in const]}", flush=True)
        except Exception as ex:
            out.setdefault(ename, {})[branch] = {"ERROR": f"{type(ex).__name__}: {str(ex)[:200]}"}
            print(ename, branch, "ERROR", type(ex).__name__, str(ex)[:160], flush=True)
json.dump(out, open("box/cone-vertex-gate-20260905/t4_historical.json","w"), indent=1, default=str)
print("secs", round(time.monotonic()-t0,1))
