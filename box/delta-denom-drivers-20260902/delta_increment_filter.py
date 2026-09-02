#!/usr/bin/env python3
"""Moh p.201 denominator-increment filter for Def. 5.1 radii.

This is a local driver for xmodel/delta-denom-gpt55-20260902.md.  It does
not edit ledgers and does not import jc2-lean.
"""
import os
import sys
from math import lcm
from fractions import Fraction as F

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "box"))
from moh_skeleton_N import Skel, census, MOH_SURVIVORS


MOH_SHARP_2 = {105, 108, 112, 117, 120}


def qv(S):
    return (1 - S.delta[1]) * F(S.dd * S.e, S.dd + S.e)


def uni_hits(S, nmin=6):
    q = qv(S)
    v = S.V[2]
    u = S.u
    out = []
    for k in range(1, int(u // v) + 1):
        val = k * v * q
        if val.denominator == 1 and val >= nmin:
            out.append(int(val))
    return out


def denom_increment(S, i):
    """A_i: denominator of L*delta_i, L=lcm denoms(delta_s,...,delta_{i+1})."""
    L = 1
    for j in range(i + 1, S.s + 1):
        L = lcm(L, S.delta[j].denominator)
    return (L * S.delta[i]).denominator


def d1_increment_ok(S):
    """Moh p.201 conditions (12)/(13), the r=2 bottom step."""
    A = denom_increment(S, 1)
    if A == 1:
        return True
    K = S.d[2]
    e = S.n // K
    d = S.m // K
    V2 = S.V[2]
    return (
        (e * V2) % A == 0 and (d * V2 - 1) % A == 0
    ) or (
        (d * V2) % A == 0 and (e * V2 - 1) % A == 0
    )


def higher_increment_ok(S, i):
    """Moh p.201 conditions (10)/(11), used as their necessary union."""
    A = denom_increment(S, i)
    if A == 1:
        return True
    total = S.V[i + 1] * S.d[i] // S.d[i + 1]
    delta, rem = divmod(total, A)
    return S.V[i] <= delta or S.V[i] % A == rem % A


def all_increment_ok(S):
    if not d1_increment_ok(S):
        return False
    for i in range(2, S.s):
        if not higher_increment_ok(S, i):
            return False
    return True


def row():
    return {
        "all": 0,
        "d1_kill": 0,
        "allinc_kill": 0,
        "surv": 0,
        "surv_d1_kill": 0,
        "surv_allinc_kill": 0,
    }


def scan(nmax=120, nmin=48):
    rows = {}
    totals = row()
    killed_examples = []
    for n in range(nmin, nmax + 1):
        R = rows.setdefault(n, row())
        for (m, Ms, V) in census(n):
            S = Skel(n, m, list(Ms), V)
            if not S.windows_ok():
                continue
            hit = bool(uni_hits(S))
            d1_ok = d1_increment_ok(S)
            all_ok = d1_ok and all_increment_ok(S)
            R["all"] += 1
            R["d1_kill"] += not d1_ok
            R["allinc_kill"] += not all_ok
            R["surv"] += hit
            R["surv_d1_kill"] += hit and not d1_ok
            R["surv_allinc_kill"] += hit and not all_ok
            if (not d1_ok or not all_ok) and len(killed_examples) < 8:
                killed_examples.append((n, m, Ms, tuple((k, V[k]) for k in sorted(V)), S.delta, [denom_increment(S, i) for i in range(1, S.s)]))
    for k in totals:
        totals[k] = sum(R[k] for R in rows.values())
    return rows, totals, killed_examples


def print_summary(rows, totals, killed_examples):
    print("== DELTA-INCREMENT FILTER, Moh p.201, D in [48,120] ==")
    print("D1-exact = p.201 (12)/(13); ALL = D1-exact plus p.201 (10)/(11) union for i>=2")
    print("%5s %9s %9s %9s %9s %11s %11s" % ("D", "V-skel", "D1kill", "ALLkill", "UNI>=6", "UNI D1kill", "UNI ALLkill"))
    for n in sorted(rows):
        R = rows[n]
        if R["all"] and (n in MOH_SHARP_2 or n % 10 == 0 or R["surv"]):
            print("%5d %9d %9d %9d %9d %11d %11d" % (
                n, R["all"], R["d1_kill"], R["allinc_kill"],
                R["surv"], R["surv_d1_kill"], R["surv_allinc_kill"]))
    print("-- totals --")
    print("%5s %9d %9d %9d %9d %11d %11d" % (
        "ALL", totals["all"], totals["d1_kill"], totals["allinc_kill"],
        totals["surv"], totals["surv_d1_kill"], totals["surv_allinc_kill"]))
    empty_all = [n for n, R in rows.items() if R["all"] and R["allinc_kill"] == R["all"]]
    empty_uni = [n for n, R in rows.items() if R["surv"] and R["surv_allinc_kill"] == R["surv"]]
    print("degrees emptied among V-skeletons:", empty_all if empty_all else "NONE")
    print("degrees emptied among UNI>=6 survivors:", empty_uni if empty_uni else "NONE")
    print("-- MOH-SHARP-2 --")
    for n in sorted(MOH_SHARP_2):
        R = rows.get(n, row())
        print("D=%d V %d -> %d ; UNI>=6 %d -> %d" % (
            n, R["all"], R["all"] - R["allinc_kill"],
            R["surv"], R["surv"] - R["surv_allinc_kill"]))
    print("-- Moh p.202 rows --")
    for (n, m, Ms, Vs, lab, _) in MOH_SURVIVORS:
        S = Skel(n, m, list(Ms), Vs)
        print("%-24s delta=%s A=%s D1=%s ALL=%s" % (
            lab,
            ",".join("%d:%s" % (i, S.delta[i]) for i in range(1, S.s + 1)),
            [denom_increment(S, i) for i in range(1, S.s)],
            d1_increment_ok(S),
            all_increment_ok(S),
        ))
    print("-- first killed examples --")
    for ex in killed_examples:
        print(ex)


if __name__ == "__main__":
    rows, totals, killed_examples = scan()
    print_summary(rows, totals, killed_examples)
