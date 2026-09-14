#!/usr/bin/env python3
"""Exact current-band Jacobian ranks after both complete boundary faces.

The remaining count is a count of generators after rational graph pivots.
Compatibility equations in older generators are RETAINED, not tested or
discarded here. In particular it is not a dimension or a proper-ideal claim.
"""
from fractions import Fraction as Q
from math import ceil, comb
from pathlib import Path
from hashlib import sha256
import json
import time
import sympy as sp

from boundary_counts import SPECS


def boundary(degree, d, h, pole, scale, physical_degree):
    N = physical_degree
    if N < 0:
        return 0, 0, 0
    M = max(0, ceil(Q(d * N - h, d + 1)))
    L = max(0, ceil((N - pole) / scale))
    M += int(d * N >= h and (d * N - h) % (d + 1) == 0)
    L += int(N >= pole and ((N - pole) / scale).denominator == 1)
    return L, M, max(0, N + 1 - L - M)


def term_polynomial(terms, W, Z):
    """Expand after the same common w^W*(w-1)^Z factor is removed."""
    out = {}
    for scalar, a, b in terms:
        if not scalar:
            continue
        a, b = a - W, b - Z
        assert a >= 0 and b >= 0
        for j in range(b + 1):
            power = a + j
            out[power] = out.get(power, 0) + scalar * comb(b, j) * (-1) ** (b - j)
    return {p: c for p, c in out.items() if c}


def run(Fspec, Gspec):
    name, n, d, hF, poleF, scale = Fspec
    _, m, _, hG, poleG, _ = Gspec
    pF, qF = (24, 84) if n == 108 else (27, 72)
    pG, qG = (16, 56) if n == 108 else (18, 48)
    pP, qP = pF // 3, qF // 3
    radial_period = 9 if n == 108 else 11
    radial_count = n // radial_period
    initial_total = rank_total = remaining_total = 0
    matrix_hash = sha256()
    blocks = []
    for r in range(1, n + 1):
        LF, MF, freeF = boundary(n, d, hF, poleF, scale, n - r)
        LG, MG, freeG = boundary(m, d, hG, poleG, scale, m - r)
        columns, labels = [], []
        for j in range(freeF):
            a, b = LF + j, MF
            columns.append([((n - r) * pG - m * a, a + pG - 1, b + qG),
                            ((n - r) * qG - m * b, a + pG, b + qG - 1)])
            labels.append(["F", j])
        for j in range(freeG):
            a, b = LG + j, MG
            columns.append([(n * a - (m - r) * pF, a + pF - 1, b + qF),
                            (n * b - (m - r) * qF, a + pF, b + qF - 1)])
            labels.append(["G", j])
        actual_terms = [(scalar, a, b) for col in columns for scalar, a, b in col if scalar]
        if actual_terms:
            W = min(a for _, a, _ in actual_terms)
            Z = min(b for _, _, b in actual_terms)
        else:
            W = Z = 0
        polynomials = [term_polynomial(col, W, Z) for col in columns]
        rows = max((max(p, default=-1) for p in polynomials), default=-1) + 1
        data = [[p.get(i, 0) for p in polynomials] for i in range(rows)]
        matrix = sp.Matrix(data) if rows else sp.zeros(0, len(columns))
        reduced, pivots = matrix.rref()
        rank, kernel = len(pivots), len(columns) - len(pivots)
        expected_radial = int(r % radial_period == 0)
        assert kernel == freeG + expected_radial, (name, r, kernel, freeG, expected_radial)
        # Check inclusion of the paired G variations in F's boundary space.
        if freeG:
            assert pP + LG >= LF and qP + MG >= MF
            assert (pP + qP) + (m - r) == n - r
        # Check the extra radial polynomial against both boundary conditions.
        radial_exponents = None
        if expected_radial:
            t = r // radial_period
            ra = pF - (pF // radial_count) * t
            rb = qF - (qF // radial_count) * t
            assert ra + rb == n - r
            assert ra >= LF and rb >= MF
            radial_exponents = [ra, rb]
        initial_total += len(columns)
        rank_total += rank
        remaining_total += kernel
        matrix_hash.update(repr((r, W, Z, labels, data, pivots)).encode())
        blocks.append(dict(depth=r, F_physical_degree=n-r, G_physical_degree=m-r,
                           F_boundary_factor=[LF, MF], G_boundary_factor=[LG, MG],
                           current_F_generators=freeF, current_G_generators=freeG,
                           stripped_common_factor=[W, Z], matrix_rows=rows,
                           matrix_columns=len(columns), rank=rank, kernel=kernel,
                           pivot_columns=list(pivots), radial_exponents=radial_exponents,
                           compatibility_equations_retained=True))
    return dict(client=name.removesuffix("_F"), initial_boundary_generators=initial_total,
                rational_pivots=rank_total, remaining_generators=remaining_total,
                radial_generator_count=radial_count,
                maximum_matrix_rows=max(x["matrix_rows"] for x in blocks),
                maximum_matrix_columns=max(x["matrix_columns"] for x in blocks),
                matrices_and_pivots_sha256=matrix_hash.hexdigest(), blocks=blocks)


def main():
    started = time.monotonic()
    clients = [run(SPECS[i], SPECS[i+1]) for i in (0, 2, 4)]
    out = dict(coefficient_field="Q", method="Exact rational RREF after removal of a common nonzero polynomial factor",
               scope="Generator count after current-band pivots; all residual equations in older generators are retained and unevaluated",
               not_a_dimension_or_properness_claim=True,
               elapsed_seconds=round(time.monotonic()-started, 3), clients=clients)
    Path(__file__).with_suffix(".json").write_text(json.dumps(out, separators=(",", ":")) + "\n")
    print(json.dumps({**{k:v for k,v in out.items() if k != "clients"},
                      "clients":[{k:v for k,v in x.items() if k != "blocks"} for x in clients]}, indent=2))


if __name__ == "__main__":
    main()
