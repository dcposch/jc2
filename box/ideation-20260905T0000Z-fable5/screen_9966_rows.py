#!/usr/bin/env python3
"""Run the charged whole-tree screens (box/centre-gate-20260903/rerun_screens.py
machinery, unmodified imports) on the EIGHT (1)-(13)-admissible (99,66) rows.
Read-only; prints one line per row per screen."""
import sys, os, time
HERE = "/home/ubuntu/jc2/box/centre-gate-20260903"
sys.path.insert(0, HERE)
import moh_skeleton_full_frozen as B
from opus5_probe import Tree

rows = [(99, m, Ms, V) for m, Ms, V in B.census(99, Kmin=2, full=True) if m == 66]
print("rows at (99,66):", len(rows))
def surv(n, m, Ms, V, danger, gate, ode=False, passport=False):
    T = Tree(n, m, Ms, gate=gate, ode=ode, capacity=passport, passport=passport)
    T._memo = {}
    if not (T.d[T.s] > V[T.s] > (T.d[T.s] / 2)):
        return "FAIL-window"
    need = tuple(V[i] for i in range(T.s - 1, 1, -1))
    r = T.ok(T.s - 1, (V[T.s],), danger, need)
    return "SURVIVES" if r is not None else "DEAD"
screens = [("PARTITION", dict(danger=False, gate=False)),
           ("PARTITION_ODE", dict(danger=False, gate=False, ode=True)),
           ("UNGATED", dict(danger=True, gate=False)),
           ("UNGATED_ODE", dict(danger=True, gate=False, ode=True)),
           ("UNGATED_PASS", dict(danger=True, gate=False, ode=True, passport=True))]
for (n, m, Ms, V) in sorted(rows, key=lambda r: (r[2][1], r[3].get(3), r[3].get(2))):
    Vt = tuple(sorted(V.items()))
    out = []
    for name, kw in screens:
        t0 = time.time()
        try:
            res = surv(n, m, Ms, V, **kw)
        except Exception as e:
            res = "ERR:" + repr(e)[:60]
        out.append(f"{name}={res}")
    print(f"M={tuple(Ms)} V={Vt} :: " + " ".join(out), flush=True)
