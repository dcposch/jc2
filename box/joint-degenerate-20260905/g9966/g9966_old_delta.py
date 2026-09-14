#!/usr/bin/env python3
"""Delta-subsystem (outer blocks = 0, F = K2^3, G = K2^2, all Jacobian rows
identically zero) on the OLD (99,66) charts, at the stage where the historical
unit was reported: delta2 stage 4 (row stage4_J_d159_k35 = 6264) and delta52
stage 8 (row stage8_G_local16_coord0 = 64).  The cone-vertex theorem predicts
that the old chart's Delta_T must already be EMPTY (a unit from the h2-only
pole rows + chart pins), otherwise a Jacobian row could not reduce to a
nonzero constant.  Engines: pristine = charged 17(pppp)/(tttt) engine
(jet0 = 0, pure pi^8 h3 face); precise = Sol's jet0-free replay.
"""
import argparse, importlib.util, json, subprocess, sys, time
from collections import defaultdict
from pathlib import Path
import sympy as sp
HERE = Path(__file__).resolve().parent
ENG = {"pristine": "/home/ubuntu/jc2/box/g9966band-20260903/band_engine.py",
       "precise": "/home/ubuntu/jc2/box/g9966-d2-precise-20260905/band_engine.py",
       "corrected": "/home/ubuntu/jc2/box/g9966-repair-gate-20260905/corrected_face_engine.py"}
ap = argparse.ArgumentParser(); ap.add_argument("--engine", required=True); ap.add_argument("--branch", required=True)
A = ap.parse_args()
spec = importlib.util.spec_from_file_location("eng_" + A.engine, ENG[A.engine]); m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m; spec.loader.exec_module(m)
sym = m.symbol; branch = A.branch
t0 = time.monotonic()
stage = 4 if branch == "delta2" else 8
# G rows at local powers <= L  <=>  a_p = 0 for p <= floor(L/2)  (K2(sigma)^2 = O(t^(L+1)))
L = m.stage_spec(branch, stage)["pole_local_power"]      # 8 (delta2) or 16 (delta52, tau-units)
P = L // 2
k2, inner_free, meta = m.build_major_h2(branch, P + 2)
k2free = sorted([v for v in inner_free if str(v).startswith("K2c_")], key=str)
hc_free = sorted([v for v in inner_free if str(v).startswith("Hc_")], key=str)
params = sorted([v for v in inner_free if not (str(v).startswith("K2c_") or str(v).startswith("Hc_"))], key=str)
loc_var = sym("rho") if branch == "delta2" else sym("c")
print(f"[{A.engine}/{branch}] stage {stage}: G local <= {L} => a_p = 0 for p <= {P}; K2c free {len(k2free)}, Hc free {hc_free}, params {params}", flush=True)
loc = m.local_rows(k2, branch, P)
rows = [(f"a{n}_k{k}", sp.expand(v)) for (n, k), v in sorted(loc.items())]
# cross-check: these ARE the engine's G rows on Delta up to the square: G_local n = sum_{p+q=n} a_p a_q
residual, subs, piv, zeros = m.qstar_reduce(rows, set(k2free) | set(hc_free))
print("rows", len(rows), "pivots", [str(p.variable) for p in piv], "zero", zeros, "residual", {l: str(v) for l, v in residual}, flush=True)
res = {"engine": A.engine, "branch": branch, "stage": stage, "G_local_max": L, "a_p_depth": P,
       "rows": len(rows), "pivots": [str(p.variable) for p in piv], "residual": {l: str(v) for l, v in residual}}
const_unit = any((not v.free_symbols) and v != 0 for _l, v in residual)
if residual and const_unit:
    res["singular"] = "residual contains a nonzero constant row: unit without localization"
    res["Delta_T_empty"] = True
elif residual:
    vars_ = sorted({str(s) for _l, v in residual for s in v.free_symbols} | {str(loc_var)})
    lines = [f"ring R=0,({','.join(vars_ + ['Zl'])}),dp;"]; gens = []
    for i, (l, v) in enumerate(residual):
        lines.append(f"poly r{i}={str(sp.expand(v)).replace('**','^')};"); gens.append(f"r{i}")
    lines.append(f"poly L=Zl*{loc_var}-1;"); gens.append("L")
    lines.append("ideal I=" + ",".join(gens) + "; ideal S=std(I); print(\"DIM\"); dim(S); print(\"NF1\"); reduce(1,S); quit;")
    script = HERE / f"old_delta_{A.engine}_{branch}.sing"; script.write_text("\n".join(lines) + "\n")
    out = subprocess.run(["Singular", "-q", str(script)], text=True, capture_output=True, timeout=1800)
    (HERE / (script.name + ".out")).write_text(out.stdout + out.stderr)
    o = out.stdout.splitlines()
    res["singular"] = {"dimension": int(o[o.index("DIM") + 1]), "reduce_1": o[o.index("NF1") + 1], "vars": vars_}
    res["Delta_T_empty"] = res["singular"]["dimension"] == -1
else:
    res["Delta_T_empty"] = False
    res["singular"] = "no residual: affine space"
res["wall_seconds"] = round(time.monotonic() - t0, 1)
print(json.dumps({k: res[k] for k in ("engine", "branch", "stage", "a_p_depth", "Delta_T_empty", "singular", "wall_seconds")}, indent=1))
(HERE / f"old_delta_{A.engine}_{branch}.json").write_text(json.dumps(res, indent=1) + "\n")
