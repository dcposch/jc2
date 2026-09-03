#!/usr/bin/env python3
"""Exact Prop. 6.3 arithmetic and conditional s'=3 Phi calculations.

The V-copy and Phi-at-height-three outputs are labelled candidates only.  The
degree and characteristic recovery uses Moh Prop. 6.3(2) plus the p.154
mu/M dictionary.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import gcd


def chain(n, m, Ms):
    M = [-m] + list(Ms)
    d = [n]
    for value in M:
        d.append(gcd(d[-1], value))
    return M, d


def mu_data(n, m, Ms):
    M, d = chain(n, m, Ms)
    lam = 0
    mus = []
    for j, value in enumerate(M):
        qj = value if j == 0 else value - M[j - 1]
        lam += qj * d[j]
        mus.append(F(lam, d[j]))
    return M, d, mus


def def51(n, m, Ms, Vs):
    M, d = chain(n, m, Ms)
    s = len(M)
    V = {i + 2: value for i, value in enumerate(Vs)}
    ans = []
    for ii in range(s, 0, -1):
        num = F(n - M[ii - 1])
        den = F(n - M[s - 1] - 1)
        for jj in range(ii + 1, s + 1):
            num *= V[jj] * (n - M[jj - 1]) - d[jj - 1]
            den *= V[jj] * (n - M[jj - 2]) - d[jj - 1]
        ans.append(1 - num / den)
    return tuple(ans)


def show_parent(Ms, Vs):
    n, m = 108, 72
    M, d, mus = mu_data(n, m, Ms)
    ds, vs = d[len(M) - 1], Vs[-1]
    us = ds - vs
    degrees = [F(us * n, ds)] + [F(us * (-mu), ds) for mu in mus[:-1]]
    descended_M = tuple(F(x, ds) for x in Ms[:-1])
    descended_d = tuple(F(x, ds) for x in d[:-1])
    print("parent", tuple(Ms), "V", tuple(Vs))
    print("  full M", tuple(M), "d", tuple(d), "mu", tuple(mus))
    print("  (d_s,v_s,u_s,k)", (ds, vs, us, vs-us-1))
    print("  Prop6.3 pi degrees (P,T1,...)", tuple(degrees))
    print("  recovered n',m',M',d'", (degrees[0], degrees[1], descended_M, descended_d))
    raw = def51(18, 12, [int(x) for x in descended_M], Vs[:-1])
    print("  CANDIDATE V'", tuple(Vs[:-1]), "raw Def51 (s..1)", raw,
          "UNLICENSED Phi", tuple(4*x for x in raw))


def main():
    for Ms, Vs in [
        ((24, 78, 106), (1, 1, 5)),
        ((24, 78, 106), (1, 4, 5)),
        ((48, 90, 106), (1, 1, 5)),
        ((48, 90, 106), (1, 3, 5)),
    ]:
        show_parent(Ms, Vs)
    print("prompt-hypothetical M'=(8,13), V'=(1,1):",
          tuple(4*x for x in def51(18, 12, [8, 13], [1, 1])))
    print("prompt-hypothetical M'=(8,13), V'=(1,4):",
          tuple(4*x for x in def51(18, 12, [8, 13], [1, 4])))


if __name__ == "__main__":
    main()
