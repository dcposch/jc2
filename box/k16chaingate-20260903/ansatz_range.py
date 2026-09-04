#!/usr/bin/env python3
"""Ansatz (5.1) failure list for R_r = {q_{t-r,0}, b3}, r=1..5."""
from __future__ import annotations
import sys


def mons(w, tv, rv):
    out = []
    wx, wb = tv - rv, tv + 1
    if wx <= 0:
        return out
    a = 0
    while a * wx <= w:
        rem = w - a * wx
        if rem % wb == 0:
            out.append((a, rem // wb))
        a += 1
    return out


def main(rs):
    for rv in rs:
        bad = []
        for tv in range(rv + 2, 60):
            why = []
            if mons(2 * tv + 1, tv, rv):
                why.append("b2")
            if mons(tv, tv, rv):
                why.append("T(0)")
            if len(mons(3 * tv + 1, tv, rv)) != (1 if rv == 1 else 0):
                why.append("b1")
            C = [j for j in range(1, tv) if mons(j, tv, rv)]
            Q = [j for j in range(tv, 2 * tv + 1) if mons(j, tv, rv)]
            pred = {tv + 1, 2 * tv - 2 * rv, 2 * tv - rv + 1} & set(range(tv, 2 * tv + 1))
            if C != [tv - rv]:
                why.append("C=%s" % C)
            if sorted(Q) != sorted(pred):
                why.append("q=%s" % Q)
            if why:
                bad.append((tv, why, 3 * rv + 3))
        print("r=%d : fails at t=%s ; CHAIN-STEP bound t>=%d"
              % (rv, [b[0] for b in bad], 3 * rv + 3))
        for tv, why, bnd in bad:
            flag = "BELOW_BOUND" if tv < bnd else "AT_OR_ABOVE_BOUND"
            print("        t=%2d %s : %s" % (tv, flag, ",".join(why)))


if __name__ == "__main__":
    rs = [int(a) for a in sys.argv[1:]] or [1, 2, 3, 4, 5]
    main(rs)
