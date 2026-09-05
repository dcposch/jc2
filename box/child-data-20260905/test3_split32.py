#!/usr/bin/env python3
"""TEST 3 -- OPEN[UNEG-192-144-SPLIT-3/2].

Exclude delta* = 3/2 for the four u_s=2 U-NEGATIVE rows at (192,144) using the
BANKED split-face screen (G)+(L) of box/g9966n1b3-20260903/face_screen.py.
Functions are IMPORTED, not retyped, so the instrument is the banked one.

The banked report proves the screen is W-free: (G) depends only on delta and
(L) only on (u_s, v_s, delta) via  t = (delta-1)/(v_s - u_s*delta),  k = W - t.
That algebraic fact is re-verified HERE for (u,v)=(2,4) by sweeping W, because
the banked w-independence sweep was run at the (99,66) (u,v) values only.
"""
import json, sys
from fractions import Fraction as F
sys.path.insert(0, "/home/ubuntu/jc2/box/g9966n1b3-20260903")
import face_screen as FS
import sympy as sp

ROWS = [
    {"tag": "R1", "n": 192, "m": 144, "M": [-120, -12, 18, 190], "V2": 23},
    {"tag": "R2", "n": 192, "m": 144, "M": [-72, 12, 78, 190],   "V2": 22},
    {"tag": "R3", "n": 192, "m": 144, "M": [-72, 12, 78, 190],   "V2": 31},
    {"tag": "R4", "n": 192, "m": 144, "M": [-24, 132, 174, 190], "V2": 23},
]
U, V = 2, 4                      # u_s = d_s - V_s = 6-4 ; v_s = V_s = 4
DELTA = F(3, 2)                  # the sole survivor of the charged radius window

out = {"schema": "jc2.child-data.test3-split32/v1",
       "instrument": "box/g9966n1b3-20260903/face_screen.py (imported)",
       "u_s": U, "v_s": V, "delta_star": str(DELTA), "rows": [], "w_sweep": {}}

# ---- control A: reproduce the banked (99,66) verdicts from the import -------
ctrlA = {}
for name, dat in FS.SKELETONS.items():
    u, v, W = dat["u"], dat["v"], FS.W_of(dat["M2"])
    surv = []
    for delta in FS.detector_orders(u, v):
        X = F(u) * delta - F(v); a = F(W) * X - 1 + delta
        k = a / X; t = F(W) - k; Q = delta.denominator
        for part in FS.partitions(u):
            if len(part) < 2:
                continue
            if FS.galois_patterns(part, Q) and FS.local_exponent_ok(part, k, t, W, u):
                surv.append([str(delta), list(part)])
    ctrlA[name] = surv
banked = json.load(open("/home/ubuntu/jc2/box/g9966n1b3-20260903/face-screen.json"))
ctrlA_ok = True
for name, rec in banked["rows"].items():
    gl_alive = [[c["delta"], c["partition"]] for c in rec["charts"] if c["verdict"] != "DEAD"]
    if sorted(map(str, gl_alive)) != sorted(map(str, ctrlA[name])):
        ctrlA_ok = False
out["control_A_replay_9966"] = {"pass": ctrlA_ok, "gl_survivors": ctrlA}

# ---- the (192,144) screen ---------------------------------------------------
def screen(u, v, delta, W):
    X = F(u) * delta - F(v)
    a = F(W) * X - 1 + delta
    k = a / X
    t = F(W) - k
    Q = delta.denominator
    charts = []
    for part in FS.partitions(u):
        if len(part) < 2:
            continue                      # one block is not a separation
        gal = FS.galois_patterns(part, Q)
        loc = FS.local_exponent_ok(part, k, t, W, u)
        if not gal:
            verdict, reason = "DEAD", "no zeta_Q-stable root multiset (G)"
        elif not loc:
            verdict, reason = "DEAD", "local exponent count exceeds deg q (L)"
        else:
            verdict, reason = "ALIVE_GL", "survives (G) and (L)"
        charts.append({"partition": list(part), "Q": Q, "k": str(k), "t": str(t),
                       "X": str(X), "a": str(a), "deg_q": W * u + 1,
                       "galois_patterns": [[p0, o] for p0, o in gal],
                       "local_assignments": loc, "verdict": verdict, "reason": reason})
    return charts

W_REF = 47                       # arbitrary; the sweep below shows W is inert
for row in ROWS:
    charts = screen(U, V, DELTA, W_REF)
    alive = [c for c in charts if c["verdict"] != "DEAD"]
    row_rec = dict(row)
    row_rec.update({"d_s": 6, "u_s": U, "v_s": V, "ceiling_v_over_u": str(F(V, U)),
                    "window": [str(DELTA)],
                    "partitions_of_u_s_with_ge2_blocks": [list(p) for p in FS.partitions(U)
                                                          if len(p) >= 2],
                    "charts": charts,
                    "delta_3_2_EXCLUDED": len(alive) == 0})
    out["rows"].append(row_rec)

# ---- control B: W-independence at (u,v)=(2,4) -------------------------------
sweep = {}
for W in range(5, 60):
    charts = screen(U, V, DELTA, W)
    sweep[W] = sorted(c["verdict"] for c in charts)
vals = {tuple(v) for v in sweep.values()}
out["w_sweep"] = {"W_range": "5..59", "distinct_verdict_vectors": [list(v) for v in vals],
                  "constant": len(vals) == 1,
                  "t_closed_form": str(F(DELTA - 1, F(V) - F(U) * DELTA)),
                  "k_minus_W": str(-F(DELTA - 1, F(V) - F(U) * DELTA))}

# ---- control C: the screen must NOT kill everything (positive control) ------
# delta=3/2 at (u,v)=(4,7) [S2] survives G+L in the banked run; re-check here.
posc = screen(4, 7, F(3, 2), FS.W_of(22))
out["control_C_positive"] = {"case": "(u,v)=(4,7) delta=3/2 (banked S2)",
                             "alive": [c["partition"] for c in posc if c["verdict"] != "DEAD"],
                             "pass": any(c["verdict"] != "DEAD" for c in posc)}

killed = all(r["delta_3_2_EXCLUDED"] for r in out["rows"])
out["VERDICT"] = ("EXCLUDED: delta*=3/2 dies at (u_s,v_s)=(2,4) for all four rows"
                  if killed else "NOT EXCLUDED")
open("/home/ubuntu/jc2/box/child-data-20260905/test3-split32.json", "w").write(
    json.dumps(out, indent=1, sort_keys=True) + "\n")
print("control A (replay 99,66 G+L):", out["control_A_replay_9966"]["pass"])
print("control C (positive):", out["control_C_positive"])
print("W-sweep constant:", out["w_sweep"]["constant"], out["w_sweep"]["distinct_verdict_vectors"])
print("t =", out["w_sweep"]["t_closed_form"])
for r in out["rows"]:
    print(r["tag"], "M=", r["M"], "V2=", r["V2"], "->",
          [(c["partition"], c["verdict"], c["reason"]) for c in r["charts"]])
print("VERDICT:", out["VERDICT"])
