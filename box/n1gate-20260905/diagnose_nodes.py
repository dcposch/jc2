#!/usr/bin/env python3
"""Per-b dissection of the unique s=3 node, imports unmodified."""
from __future__ import annotations

import json
import os
import sys
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
CENTRE = os.path.abspath(os.path.join(HERE, "..", "centre-gate-20260903"))
sys.path.insert(0, CENTRE)

import moh_skeleton_full_frozen as B  # noqa: E402
from opus5_probe import Tree  # noqa: E402

S_IDS = {
    (-22, 9, 1): "S1",
    (22, 7, 1): "S2",
    (22, 7, 5): "S3",
    (22, 8, 1): "S4",
    (22, 10, 1): "S5",
    (55, 10, 2): "S6",
    (77, 7, 8): "S7",
    (77, 8, 8): "S8",
}


def bottom_and_free(T, v, V3):
    nh = (v, V3)
    good, A1, c12, c13 = T.bottom(nh)
    free = [str(x) for x in T.free_exponents(nh)]
    return {
        "V2": v,
        "bottom_ok": good,
        "A1": A1,
        "c12": c12,
        "c13": c13,
        "free": free,
    }


def main():
    out = []
    for m, Ms, V in B.census(99, Kmin=2, full=True):
        if m != 66:
            continue
        sid = S_IDS[(Ms[0], V[3], V[2])]
        T = Tree(99, m, Ms)
        j = T.s - 1
        high = (V[T.s],)
        dl, L, A, P, Q, lo = T.node(j, high)
        V2, V3 = V[2], V[3]
        print(f"\n==== {sid} A={A} P={P} Q={Q} lo={lo} V2={V2} V3={V3} ====")
        rec = {
            "id": sid,
            "A": A, "P": P, "Q": Q, "lo": str(lo),
            "V2": V2, "V3": V3, "delta2": str(dl),
            "bs": [],
        }
        for b in range(P % A, P + 1, A):
            zmaj = F(b) > lo
            total = (P - b) // A
            cap = (Q - (1 if b > 0 else 0)) // A
            zb = bottom_and_free(T, b, V3)
            # Prop 5.6 ungated at D1 on the zero child of this b
            p56_ungated = bool(zmaj)  # danger incoming True at s=3; is_zero True
            p56_gated = bool(zmaj) and (len(zb["free"]) == 0)
            hosts_V2_zero = (b == V2) and zmaj
            hosts_V2_nz = (V2 <= total) and (V2 != b) and (F(V2) > lo)
            print(
                f"  b={b:3d} zmaj={str(zmaj):5s} total={total:2d} cap={cap:2d}"
                f"  zero_bottom={zb['bottom_ok']} (12)={zb['c12']} (13)={zb['c13']}"
                f"  zero_free={zb['free'] or '∅'}"
                f"  hosts_V2_zero={hosts_V2_zero} hosts_V2_nz={hosts_V2_nz}"
                f"  p56_ungated_kills_zero_child={p56_ungated}"
                f"  p56_gated_kills_zero_child={p56_gated}"
            )
            rec["bs"].append({
                "b": b, "zmaj": zmaj, "total": total, "cap": cap,
                "zero_bottom": zb,
                "hosts_V2_zero": hosts_V2_zero,
                "hosts_V2_nz": hosts_V2_nz,
                "p56_ungated_kills_zero_child": p56_ungated,
                "p56_gated_kills_zero_child": p56_gated,
            })
        sel = bottom_and_free(T, V2, V3)
        print(f"  selected V2={V2} bottom={sel['bottom_ok']} free={sel['free'] or '∅'}")
        rec["selected"] = sel
        out.append(rec)
    dest = os.path.join(HERE, "diagnose_nodes.json")
    with open(dest, "w") as f:
        json.dump(out, f, indent=2, sort_keys=True)
        f.write("\n")
    print("\nwrote", dest)


if __name__ == "__main__":
    main()
