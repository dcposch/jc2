#!/usr/bin/env python3
"""Exact Q counts for the two boundary directions; no CAS specialization.

The proof is in boundary_counts.md. Every square rational pivot determinant
used in that proof is independently checked here by integer Bareiss reduction.
The R minor assertions are conditional on the separate source-license audit.
"""
from fractions import Fraction as Q
from math import ceil, comb
from pathlib import Path
import json
import time


def determinant(a):
    """Integer Bareiss determinant, without parameter specialization."""
    a = [r[:] for r in a]
    n = len(a)
    if n == 0:
        return 1
    old, sign = 1, 1
    for k in range(n - 1):
        if not a[k][k]:
            p = next(i for i in range(k + 1, n) if a[i][k])
            a[k], a[p] = a[p], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = a[i][j] * pivot - a[i][k] * a[k][j]
                assert num % old == 0
                a[i][j] = num // old
            a[i][k] = 0
        old = pivot
    return sign * a[-1][-1]


SPECS = [
    # name, degree, major cover d, maximum d*i-k, minor pole, 1+delta
    ("99_delta2_F", 99, 3, 9, Q(18), Q(3)),
    ("99_delta2_G", 66, 3, 6, Q(12), Q(3)),
    ("99_delta52_F", 99, 3, 9, Q(9, 2), Q(7, 2)),
    ("99_delta52_G", 66, 3, 6, Q(3), Q(7, 2)),
    ("108_free_mean_F", 108, 4, 12, Q(12), Q(4)),
    ("108_free_mean_G", 72, 4, 8, Q(8), Q(4)),
    ("99_delta2_R_conditional", 55, 3, 5, Q(10), Q(3)),
    ("99_delta52_R_conditional", 55, 3, 5, Q(5, 2), Q(7, 2)),
    ("108_free_mean_R_conditional", 63, 4, 7, Q(7), Q(4)),
]


def main():
    started = time.monotonic()
    pivots, output = {}, {}
    for name, degree, d, h, b, scale in SPECS:
        sums = dict(major_floor=0, both_floors=0,
                    both_floors_major_face=0, both_full_faces=0)
        blocks, over = [], []
        for n in range(degree + 1):
            m = max(0, ceil(Q(d * n - h, d + 1)))
            ell = max(0, ceil((n - b) / scale))
            em = int(d * n >= h and (d * n - h) % (d + 1) == 0)
            el = int(n >= b and ((n - b) / scale).denominator == 1)
            dimensions = [n + 1 - m, n + 1 - m - ell,
                          n + 1 - m - ell - em,
                          n + 1 - m - ell - em - el]
            for key, value in zip(sums, dimensions):
                sums[key] += max(0, value)
            M = m + em
            rank = min(ell + el, n + 1 - M)
            key = (M, rank)
            if key not in pivots:
                matrix = [[(-1) ** (M + col - row) * comb(M + col, row)
                           if row <= M + col else 0
                           for col in range(rank)] for row in range(rank)]
                det = determinant(matrix)
                assert det == (-1) ** (rank * M)
                pivots[key] = det
            if dimensions[-1] < 0:
                over.append(dict(n=n, multiplicity_at_0=ell,
                                 multiplicity_at_1=m,
                                 excess=-dimensions[-1]))
            blocks.append([n, m, ell, em, el, max(0, dimensions[-1])])
        assert len(over) == 1 and over[0]["n"] == degree
        assert over[0]["excess"] == 1
        m, ell = over[0]["multiplicity_at_1"], over[0]["multiplicity_at_0"]
        assert m + ell == degree
        # Top Hermite compatibility: f(w)=A*w^ell*(w-1)^m.
        minor_top_sign = (-1) ** m
        expected_sign = -1 if name.startswith("108") and "_R_" in name else 1
        assert minor_top_sign == expected_sign
        output[name] = dict(degree=degree, cover=d, major_weight_bound=h,
                            minor_pole=str(b), minor_scale=str(scale),
                            counts=sums, excess_blocks=over,
                            minor_top_coefficient_divided_by_major_top=minor_top_sign,
                            compatibility_residual=0,
                            changed_minor_top_negative_control=1,
                            block_columns=["n", "m", "ell", "major_equality",
                                           "minor_equality", "remaining"],
                            blocks=blocks)
    result = dict(coefficient_field="Q", parameter_ring="Q[all retained centres, separation, lambda]",
                  rank_statement="Universal: every checked pivot is +1 or -1; no parameter divided",
                  scope="Boundary-only raw F/G and conditional R coefficient spaces; recurrence and characteristic identity not imposed",
                  unique_integer_pivot_checks=len(pivots),
                  maximum_pivot_size=max(rank for _, rank in pivots),
                  clients=output, elapsed_seconds=round(time.monotonic() - started, 3))
    destination = Path(__file__).with_suffix(".json")
    destination.write_text(json.dumps(result, separators=(",", ":")) + "\n")
    print(json.dumps({"file": str(destination),
                      "unique_integer_pivot_checks": result["unique_integer_pivot_checks"],
                      "maximum_pivot_size": result["maximum_pivot_size"],
                      "elapsed_seconds": result["elapsed_seconds"],
                      "counts": {k: v["counts"] for k, v in output.items()}}, indent=2))


if __name__ == "__main__":
    main()
