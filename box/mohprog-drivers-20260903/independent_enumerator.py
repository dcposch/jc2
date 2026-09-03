#!/usr/bin/env python3
"""Independent arithmetic enumerator for Moh-style numerical skeletons.

This file deliberately does not import the charged ``moh_skeleton_full``
implementation.  It is a second implementation of the finite arithmetic
search used for two checks:

* exhaustive (1)--(7) enumeration at (n,m)=(75,50), including delta_1;
* independent reproduction of the rows passing the printed arithmetic
  conditions (7)--(13) for n <= 100.

Conditions (3) and (4) contain geometric/realizability content that a finite
integer enumeration cannot certify.  Records produced here label that fact
explicitly; "passes" means passes the numerical skeleton interpretation.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import gcd, lcm
from pathlib import Path


OUTDIR = Path(__file__).resolve().parent


def frac_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def divisor_drop_chains(start: int, floor: int = 4):
    """All nonempty strictly decreasing divisor chains starting at ``start``."""
    answer = []

    def visit(current, prefix):
        for nxt in range(floor, current):
            if current % nxt == 0:
                chain = prefix + (nxt,)
                answer.append(chain)
                visit(nxt, chain)

    visit(start, ())
    return answer


def ordered_M_tuples(n: int, m: int, d: dict[int, int], s: int):
    """Enumerate M_2,...,M_s with exact prescribed gcd drops."""
    M = {1: -m, s: n - 2}

    def visit(i: int, previous: int):
        if i == s:
            if previous < n - 2:
                yield tuple(M[j] for j in range(2, s + 1))
            return
        for value in range(previous + 1, n - 2):
            if gcd(d[i], value) == d[i + 1]:
                M[i] = value
                yield from visit(i + 1, value)

    yield from visit(2, -m)


def V_tuples(n: int, m: int, Ms: tuple[int, ...], d: dict[int, int]):
    """Enumerate V_s,...,V_2 from the strict/weak windows in (7)."""
    s = len(Ms) + 1
    M = {1: -m, **{i + 2: value for i, value in enumerate(Ms)}}
    V = {s + 1: d[s + 1]}

    def visit(i: int):
        if i == 1:
            yield {j: V[j] for j in range(2, s + 1)}
            return
        lower = Fraction(d[i], n - M[i])
        upper = Fraction(V[i + 1] * d[i], d[i + 1])
        first = lower.numerator // lower.denominator + 1
        last = upper.numerator // upper.denominator
        for value in range(max(1, first), last + 1):
            # The top equality V_s=d_s is excluded in the charged (1)--(7)
            # core (the proper top multiplicity split).
            if i == s and value >= d[s]:
                continue
            V[i] = value
            yield from visit(i - 1)
        V.pop(i, None)

    yield from visit(s)


def numerical_skeletons(n: int, fixed_m: int | None = None, kmin: int = 2):
    """Yield numerical (1)--(7) skeletons as (n,m,Ms,V,d)."""
    for K in range(kmin, n // 3 + 1):
        if n % K:
            continue
        e = n // K
        if e < 3:
            continue
        for chain in divisor_drop_chains(K):
            s = 2 + len(chain)
            dvals = (n, K) + chain + (gcd(chain[-1], n - 2),)
            d = {i + 1: value for i, value in enumerate(dvals)}
            for reduced_m in range(2, e):
                if gcd(reduced_m, e) != 1:
                    continue
                m = K * reduced_m
                if fixed_m is not None and m != fixed_m:
                    continue
                for Ms in ordered_M_tuples(n, m, d, s):
                    for V in V_tuples(n, m, Ms, d):
                        yield n, m, Ms, V, d


def radii(n: int, m: int, Ms: tuple[int, ...], V: dict[int, int], d: dict[int, int]):
    s = len(Ms) + 1
    M = {1: -m, **{i + 2: value for i, value in enumerate(Ms)}}
    result = {}
    for i in range(1, s + 1):
        numerator = Fraction(n - M[i], 1)
        denominator = Fraction(n - M[s] - 1, 1)
        for j in range(i + 1, s + 1):
            numerator *= V[j] * (n - M[j]) - d[j]
            denominator *= V[j] * (n - M[j - 1]) - d[j]
        result[i] = 1 - numerator / denominator
    return result


def increment_data(delta: dict[int, Fraction], s: int):
    L = {}
    A = {}
    for j in range(1, s):
        base = 1
        for i in range(j + 1, s + 1):
            base = lcm(base, delta[i].denominator)
        L[j] = base
        A[j] = (base * delta[j]).denominator
    return L, A


def printed_arithmetic_ok(n, m, Ms, V, d):
    s = len(Ms) + 1
    delta = radii(n, m, Ms, V, d)
    _, A = increment_data(delta, s)
    for j in range(s - 1, 1, -1):
        Q = V[j + 1] * d[j] // d[j + 1]
        tri, square = divmod(Q, A[j])
        by10 = V[j] <= tri
        by11 = (V[j] - square) % A[j] == 0
        if not (by10 or by11):
            return False
    A1 = A[1]
    nstar, mstar = n // d[2], m // d[2]
    by12 = nstar * V[2] % A1 == 0 and (mstar * V[2] - 1) % A1 == 0
    by13 = mstar * V[2] % A1 == 0 and (nstar * V[2] - 1) % A1 == 0
    return by12 or by13


def key_of(row):
    n, m, Ms, V, _ = row
    return n, m, Ms, tuple(sorted(V.items()))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-full", action="store_true", help="also write the 658-row independent list")
    args = parser.parse_args()

    rows75 = list(numerical_skeletons(75, fixed_m=50))
    delta13 = []
    delta_histogram = {}
    for row in rows75:
        n, m, Ms, V, d = row
        d1 = radii(n, m, Ms, V, d)[1]
        delta_histogram[frac_text(d1)] = delta_histogram.get(frac_text(d1), 0) + 1
        if d1 == Fraction(1, 3):
            delta13.append(key_of(row))

    full75 = [row for row in rows75 if printed_arithmetic_ok(*row)]
    summary75 = {
        "scope": {"n": 75, "m": 50, "kmin": 2},
        "one_to_seven_assignments": len(rows75),
        "one_to_seven_M2": sorted({row[2][0] for row in rows75}),
        "one_to_seven_V3": sorted({row[3][3] for row in rows75}),
        "one_to_seven_V2": sorted({row[3][2] for row in rows75}),
        "delta_1_equals_one_third_count": len(delta13),
        "delta_1_histogram": dict(sorted(delta_histogram.items())),
        "one_to_thirteen_assignments": len(full75),
        "one_to_thirteen_M2": sorted({row[2][0] for row in full75}),
        "one_to_thirteen_V3": sorted({row[3][3] for row in full75}),
        "one_to_thirteen_rows": [
            {"M": list(row[2]), "V": {str(k): v for k, v in sorted(row[3].items())},
             "delta_1": frac_text(radii(*row)[1])}
            for row in full75
        ],
    }
    (OUTDIR / "independent-75-50.json").write_text(json.dumps(summary75, indent=2, sort_keys=True) + "\n")

    full100 = []
    baseline100 = 0
    for n in range(4, 101):
        for row in numerical_skeletons(n):
            baseline100 += 1
            if printed_arithmetic_ok(*row):
                full100.append(row)
    summary100 = {
        "scope": {"n_min": 4, "n_max": 100, "kmin": 2},
        "numerical_one_to_seven_assignments": baseline100,
        "one_to_thirteen_assignments": len(full100),
        "nm_classes": len({(row[0], row[1]) for row in full100}),
    }
    (OUTDIR / "independent-n100-summary.json").write_text(json.dumps(summary100, indent=2, sort_keys=True) + "\n")
    if args.write_full:
        payload = [
            {"n": n, "m": m, "M": list(Ms), "V": {str(k): v for k, v in sorted(V.items())}}
            for n, m, Ms, V, _ in full100
        ]
        (OUTDIR / "independent-n100-rows.json").write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")

    print(json.dumps({"n75_m50": summary75, "n_le_100": summary100}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
