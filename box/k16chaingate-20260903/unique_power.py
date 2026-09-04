#!/usr/bin/env python3
"""Lemma UNIQUE-POWER: uniform monomials of weight m(t-r), and the bound.

Residual weights on S_r': t-r,...,t-1,t+1.  Identity-in-t solutions of
sum e_i (t-i) + f(t+1) = m(t-r) are enumerated, then the finite list of t
at which a second monomial appears is scanned up to t=80.
"""
from __future__ import annotations


def uniform(rv: int, mv: int):
    out = []

    def rec(i, e, E, M):
        if i > rv:
            f = mv - E
            if f >= 0 and -M + f == -mv * rv:
                out.append((tuple(e), f))
            return
        for k in range(0, mv + 1 - E):
            rec(i + 1, e + [k], E + k, M + i * k)

    rec(1, [], 0, 0)
    return out


def count_at(rv, mv, tv):
    ws = [tv - i for i in range(1, rv + 1)] + [tv + 1]
    tgt = mv * (tv - rv)
    n = 0

    def rec(i, rem):
        nonlocal n
        if i == len(ws):
            n += rem == 0
            return
        k = 0
        while k * ws[i] <= rem:
            rec(i + 1, rem - k * ws[i])
            k += 1

    rec(0, tgt)
    return n


def main() -> None:
    for mv in (3, 4):
        print("--- m=%d  uniform bound t >= %s ---" % (mv, "m(1+r)"))
        for rv in range(1, 7):
            u = uniform(rv, mv)
            bad = [tv for tv in range(rv + 2, 80) if count_at(rv, mv, tv) > 1]
            bound = mv * (1 + rv)
            above = [tv for tv in bad if tv >= bound]
            att = bound - 1
            print(
                "  r=%d uniform=%s bound=%d attained_at_%d=%s extra_above_bound=%s bad=%s"
                % (
                    rv,
                    u,
                    bound,
                    att,
                    att in bad,
                    above,
                    bad,
                )
            )


if __name__ == "__main__":
    main()
