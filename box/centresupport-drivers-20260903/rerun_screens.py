#!/usr/bin/env python3
"""n<=100 gated vs ungated screens, after LEMMA[ZERO-FACTOR-CENTRE].

Ungated Prop 5.6 is the charged C_FULL_TREE (danger flag, kill every still-
centred major zero child at D1).  Gated Prop 5.6 is the Opus §7.4 repair
(kill only when the selected chain's free set is empty).  The lemma says
the free coefficients on a still-centred zero child vanish, so ungated is
the justified screen and 204 -> 55 is the restoration.
"""
from __future__ import annotations

import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import moh_skeleton_full_frozen as B
from opus5_probe import Tree


def collect_rows():
    rows = [(n, m, Ms, V) for n in range(4, 101)
            for m, Ms, V in B.census(n, Kmin=2, full=True)]
    printed = {(n, m, tuple(Ms), tuple(sorted(V.items())))
               for n, m, Ms, V, *_ in B.MOH_TABLE}
    return rows, printed


def run_one(name, rows, printed, *, danger, gate, ode=False, passport=False):
    t0 = time.time()
    surv = set()
    for n, m, Ms, V in rows:
        T = Tree(n, m, Ms, gate=gate, ode=ode,
                 capacity=passport, passport=passport)
        T._memo = {}
        if not (T.d[T.s] > V[T.s] > (T.d[T.s] / 2)):
            continue
        need = tuple(V[i] for i in range(T.s - 1, 1, -1))
        r = T.ok(T.s - 1, (V[T.s],), danger, need)
        if r is not None:
            surv.add((n, m, tuple(Ms), tuple(sorted(V.items()))))
    classes = {(k[0], k[1]) for k in surv}
    kept = surv & printed
    dt = time.time() - t0
    print(f"{name:22s} rows={len(surv):5d} classes={len(classes):3d} "
          f"printed={len(kept)}/6 excess={len(surv - printed):4d} ({dt:.1f}s)",
          flush=True)
    return {
        "name": name, "rows": len(surv), "classes": len(classes),
        "printed": len(kept), "excess": len(surv - printed), "sec": round(dt, 2),
    }


def main():
    rows, printed = collect_rows()
    print("input rows:", len(rows), "printed:", len(printed), flush=True)
    out = []
    # gap-free partition (no Prop 5.6)
    out.append(run_one("PARTITION", rows, printed, danger=False, gate=False))
    out.append(run_one("PARTITION_ODE", rows, printed, danger=False, gate=False, ode=True))
    out.append(run_one("PARTITION_PASS", rows, printed, danger=False, gate=False,
                       ode=True, passport=True))
    # gated Prop 5.6 (Opus §7.4)
    out.append(run_one("GATED", rows, printed, danger=True, gate=True))
    out.append(run_one("GATED_ODE", rows, printed, danger=True, gate=True, ode=True))
    out.append(run_one("GATED_PASS", rows, printed, danger=True, gate=True,
                       ode=True, passport=True))
    # ungated Prop 5.6 (C_FULL_TREE); lemma-justified
    out.append(run_one("UNGATED", rows, printed, danger=True, gate=False))
    out.append(run_one("UNGATED_ODE", rows, printed, danger=True, gate=False, ode=True))
    out.append(run_one("UNGATED_PASS", rows, printed, danger=True, gate=False,
                       ode=True, passport=True))
    print("\nrestoration check: GATED_PASS rows -> UNGATED_PASS rows  "
          "(charged 204 -> 55 if lemma accepted)", flush=True)
    gp = next(x for x in out if x["name"] == "GATED_PASS")
    up = next(x for x in out if x["name"] == "UNGATED_PASS")
    print(f"  GATED_PASS  = {gp['rows']}/{gp['classes']}")
    print(f"  UNGATED_PASS= {up['rows']}/{up['classes']}")
    print(f"  restored 204->55? {gp['rows']==204 and up['rows']==55}", flush=True)
    return out


if __name__ == "__main__":
    main()
