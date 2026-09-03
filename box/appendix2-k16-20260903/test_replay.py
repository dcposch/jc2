#!/usr/bin/env python3
"""python3 -O replay with an assert scan.

Load-bearing checks use require() (not ast.Assert).  A handful of assert
statements exist so `python3 -O` plus a source scan can confirm the
discipline: asserts are documentation of equalities already required().
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))

from shape import gate_moh_shapes, phi_s2, shape_bundle
from fractions import Fraction as F
from descent_core import descend_once, u_s_of
import moh_skeleton_full as MS


def require(name, cond, detail=""):
    if not cond:
        raise SystemExit("FAIL %s %s" % (name, detail))
    print("  [ok]   %s" % name)


def main():
    print("test_replay.py  (python3 -O safe)")
    reports, bundles = gate_moh_shapes()
    for name, ok, detail in reports:
        require(name, ok, str(detail))
    # Phi 10/10
    rows = [
        (16, 12, 13, 3, 1, F(-1), F(1, 4)),
        (21, 14, 16, 2, 1, F(-1, 2), F(7, 6)),
        (21, 14, 18, 5, 1, F(-1), F(1, 3)),
        (15, 10, 11, 3, 2, F(-1), F(1, 2)),
        (15, 10, 11, 2, 2, F(-1), F(4, 3)),
    ]
    for n, m, M2, V2, k, pd2, pd1 in rows:
        d2, d1, *_ = phi_s2(n, m, M2, V2, k)
        require("Phi (%s,%s) V2=%s" % (n, m, V2), d2 == pd2 and d1 == pd1, (d2, d1))
        assert d2 == pd2 and d1 == pd1  # documentation; required() above is load-bearing
    # G2 = 42
    G2 = shape_bundle(15, 10, 4, 1, 4)
    require("G2 n_ord=42", G2["n_ord"] == 42, G2["n_ord"])
    assert G2["n_ord"] == 42
    # descent p.207
    S = MS.Skel(75, 50, [55, 73], {3: 4, 2: 3})
    require("u_s=1 on (75,50) V2=3", u_s_of(S) == 1, u_s_of(S))
    D = descend_once(S)
    require("n'=15", D["n"] == 15, D["n"])
    require("k=2", D["k"] == 2, D["k"])
    require("s'=2", D["s"] == 2, D["s"])
    assert D["n"] == 15 and D["k"] == 2
    # (99,66) u_s>1
    S99 = MS.Skel(99, 66, [77, 97], {3: 8, 2: 8})
    require("(99,66) u_s>1", u_s_of(S99) == 3, u_s_of(S99))
    print("ALL REPLAY CHECKS GREEN.")


if __name__ == "__main__":
    main()
