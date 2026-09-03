#!/usr/bin/env python3
"""Exact-Q extension of the frozen 15-pivot direct prefix, before outer D2/D1.

The probe adds precisely [x^135 y^27]J and the next F95/G62 pole-coordinate
rows.  It uses only the triangular-chart fragments which can contribute to
those slots and independently checks its first 16 rows against the frozen
``first_global_band.py`` result.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from math import factorial
import hashlib
import json
from pathlib import Path
import subprocess
from typing import Iterable

import sympy as sp


FROZEN = Path("/tmp/jc2-lane.cNPqDa/inputs")
FROZEN_DRIVER = FROZEN / "first_global_band.py"
FROZEN_RESULT = FROZEN / "results.json"
EXPECTED_DRIVER_SHA256 = "9c123aaf14c8f52104f7b1ef0f0dac50fe5ae0ed294e6bf9f8a5037c175c68af"
EXPECTED_RESULT_SHA256 = "f4a6f39c81e01f185bc0e6aed74e844639d21ffce3d219b6a539ee110553ae66"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def expr_text(expr: sp.Expr) -> str:
    return str(sp.factor(expr))


x, y = sp.symbols("x y")
u, v = sp.symbols("u v")

# Inner triangular coordinates needed by h2 in global y-degrees zero and one.
H_10_0, H_9_0 = sp.symbols("H_10_0 H_9_0")
C2_21_0, C2_20_0 = sp.symbols("C2_21_0 C2_20_0")
C3_32_0, C3_31_0, C3_30_0, C3_31_1 = sp.symbols(
    "C3_32_0 C3_31_0 C3_30_0 C3_31_1"
)
d32, d31, d30, e31 = sp.symbols("d32 d31 d30 e31")
H2_MAP = {
    d32: C3_32_0,
    d31: C3_31_0 + C2_21_0 * H_10_0,
    d30: (C3_30_0 + C2_20_0 * H_10_0 + C2_21_0 * H_9_0
          + H_10_0**3),
    e31: C3_31_1,
}

# Complete outer fragments that can reach the requested coefficient slots.
A2_65_0, A2_64_0, A2_63_0, A2_64_1 = sp.symbols(
    "A2_65_0 A2_64_0 A2_63_0 A2_64_1"
)
A3_98_0, A3_97_0, A3_96_0, A3_95_0 = sp.symbols(
    "A3_98_0 A3_97_0 A3_96_0 A3_95_0"
)
A3_97_1, A3_96_1 = sp.symbols("A3_97_1 A3_96_1")
A3_J_FACE = {
    degree: sp.Symbol(f"A3_{98-degree}_{degree}") for degree in range(2, 11)
}
B1_32_0, B1_31_0, B1_30_0, B1_31_1 = sp.symbols(
    "B1_32_0 B1_31_0 B1_30_0 B1_31_1"
)
B2_65_0, B2_64_0, B2_63_0, B2_62_0 = sp.symbols(
    "B2_65_0 B2_64_0 B2_63_0 B2_62_0"
)
B2_64_1, B2_63_1 = sp.symbols("B2_64_1 B2_63_1")

P = y**3 * (y - x)**8
h2_fragment = (
    P**3 + d32*x**32 + d31*x**31 + d30*x**30 + e31*x**31*y
)
A2_fragment = (
    A2_65_0*x**65 + A2_64_0*x**64 + A2_63_0*x**63 + A2_64_1*x**64*y
)
A3_fragment = (
    A3_98_0*x**98 + A3_97_0*x**97 + A3_96_0*x**96 + A3_95_0*x**95
    + A3_97_1*x**97*y + A3_96_1*x**96*y
    + sum(variable*x**(98-degree)*y**degree
          for degree, variable in A3_J_FACE.items())
)
B1_fragment = (
    B1_32_0*x**32 + B1_31_0*x**31 + B1_30_0*x**30 + B1_31_1*x**31*y
)
B2_fragment = (
    B2_65_0*x**65 + B2_64_0*x**64 + B2_63_0*x**63 + B2_62_0*x**62
    + B2_64_1*x**64*y + B2_63_1*x**63*y
)
F_POLY = sp.Poly(sp.expand(h2_fragment**3 + A2_fragment*h2_fragment + A3_fragment), x, y)
G_POLY = sp.Poly(sp.expand(h2_fragment**2 + B1_fragment*h2_fragment + B2_fragment), x, y)


def coefficient(poly: sp.Poly, x_degree: int, y_degree: int) -> sp.Expr:
    return sp.expand(poly.coeff_monomial(x**x_degree * y**y_degree))


def chart(expr: sp.Expr) -> sp.Expr:
    return sp.expand(expr.subs(H2_MAP))


# Exact global coefficients required by both local substitutions.
F98_0 = coefficient(F_POLY, 98, 0)
F97_0 = coefficient(F_POLY, 97, 0)
F96_0 = coefficient(F_POLY, 96, 0)
F95_0 = coefficient(F_POLY, 95, 0)
F97_1 = coefficient(F_POLY, 97, 1)
F96_1 = coefficient(F_POLY, 96, 1)
G65_0 = coefficient(G_POLY, 65, 0)
G64_0 = coefficient(G_POLY, 64, 0)
G63_0 = coefficient(G_POLY, 63, 0)
G62_0 = coefficient(G_POLY, 62, 0)
G64_1 = coefficient(G_POLY, 64, 1)
G63_1 = coefficient(G_POLY, 63, 1)

# These assertions are also the fragment-completeness certificate for the new
# pole rows.  Any omitted triangular coefficient has either too low a global
# degree or y-degree at least two and therefore cannot enter these slots.
assert F98_0 == A3_98_0
assert F97_0 == A3_97_0 + A2_65_0*d32
assert F96_0 == A3_96_0 + A2_64_0*d32 + A2_65_0*d31 + d32**3
assert F97_1 == A3_97_1
assert F96_1 == A3_96_1 + A2_64_1*d32 + A2_65_0*e31
assert F95_0 == (
    A3_95_0 + A2_63_0*d32 + A2_64_0*d31 + A2_65_0*d30
    + 3*d31*d32**2
)
assert G65_0 == B2_65_0
assert G64_0 == B2_64_0 + B1_32_0*d32 + d32**2
assert G63_0 == B2_63_0 + B1_31_0*d32 + B1_32_0*d31 + 2*d31*d32
assert G64_1 == B2_64_1
assert G63_1 == (
    B2_63_1 + B1_31_1*d32 + B1_32_0*e31 + 2*d32*e31
)
assert G62_0 == (
    B2_62_0 + B1_30_0*d32 + B1_31_0*d31 + B1_32_0*d30
    + 2*d30*d32 + d31**2
)


def local_rows(poly: sp.Poly, branch: str, normalization: int,
               target: int) -> dict[int, sp.Expr]:
    """Extract one exact local exponent, keyed by z/pi coordinate degree."""
    rows: dict[int, sp.Expr] = defaultdict(lambda: sp.Integer(0))
    for (i, j), value in poly.terms():
        if branch == "delta2":
            for k in range(j + 1):
                exponent = normalization - i + j + k
                if exponent == target:
                    rows[k] += value * sp.binomial(j, k) * u**(j-k)
        else:
            for b in range(j + 1):
                for k in range(j - b + 1):
                    a = j - b - k
                    exponent = normalization - 2*i + 2*j + 2*b + 3*k
                    if exponent == target:
                        multinomial = factorial(j)//(factorial(a)*factorial(b)*factorial(k))
                        rows[k] += value * multinomial * u**a * v**b
    return {key: chart(sp.expand(value)) for key, value in sorted(rows.items()) if value != 0}


# Degree 162 can only be J(F98,G66)+J(F99,G65).  For y^27, F98 terms above
# y^10 and G65 terms above y^1 cannot contribute.
F98 = sum(coefficient(F_POLY, 98-j, j)*x**(98-j)*y**j for j in range(11))
G65 = sum(coefficient(G_POLY, 65-j, j)*x**(65-j)*y**j for j in range(2))
F99, G66 = sp.expand(P**9), sp.expand(P**6)
J162 = sp.Poly(
    sp.diff(F98, x)*sp.diff(G66, y) - sp.diff(F98, y)*sp.diff(G66, x)
    + sp.diff(F99, x)*sp.diff(G65, y) - sp.diff(F99, y)*sp.diff(G65, x),
    x, y,
)
J_ROWS = {
    k: chart(J162.coeff_monomial(x**(162-k)*y**k)) for k in range(17, 28)
}


@dataclass(frozen=True)
class Pivot:
    row: str
    variable: sp.Symbol
    coefficient: sp.Rational
    rhs: sp.Expr


def resolve_map(mapping: dict[sp.Symbol, sp.Expr]) -> dict[sp.Symbol, sp.Expr]:
    result = dict(mapping)
    for _ in range(len(result) + 2):
        changed = False
        for variable, value in list(result.items()):
            image = sp.cancel(sp.expand(value.subs(result, simultaneous=True)))
            if image != value:
                result[variable] = image
                changed = True
        if not changed:
            return result
    raise AssertionError("pivot map did not resolve")


def qstar_reduce(rows: list[tuple[str, sp.Expr]], eligible: Iterable[sp.Symbol]):
    """Eliminate only affine variables with nonzero coefficients in Q*."""
    eligible_set = set(eligible)
    work = [(label, sp.expand(row)) for label, row in rows if row != 0]
    zero_rows = len(rows) - len(work)
    mapping: dict[sp.Symbol, sp.Expr] = {}
    pivots: list[Pivot] = []
    while True:
        choice = None
        for row_index, (label, row) in enumerate(work):
            for variable in sorted(row.free_symbols & eligible_set, key=str):
                derivative = sp.diff(row, variable)
                if derivative.is_Rational is not True or derivative == 0:
                    continue
                remainder = sp.expand(row - derivative*variable)
                if variable in remainder.free_symbols:
                    continue
                choice = (row_index, label, variable, sp.Rational(derivative), remainder)
                break
            if choice is not None:
                break
        if choice is None:
            break
        row_index, label, variable, scalar, remainder = choice
        rhs = sp.cancel(-remainder/scalar)
        mapping[variable] = rhs
        pivots.append(Pivot(label, variable, scalar, rhs))
        eligible_set.remove(variable)
        del work[row_index]
        reduced = []
        for old_label, old_row in work:
            image = sp.expand(old_row.subs(variable, rhs))
            if image == 0:
                zero_rows += 1
            else:
                reduced.append((old_label, image))
        work = reduced
    resolved = resolve_map(mapping)
    residual = []
    for label, row in work:
        image = sp.cancel(sp.expand(row.subs(resolved, simultaneous=True)))
        if image == 0:
            zero_rows += 1
        else:
            residual.append((label, image))
    return residual, resolved, pivots, zero_rows


OUTER_VARIABLES = set(A2_fragment.free_symbols | A3_fragment.free_symbols
                      | B1_fragment.free_symbols | B2_fragment.free_symbols) - {x, y}


def frozen_prefix_rows() -> list[tuple[str, sp.Expr]]:
    direct = [
        ("prefix_F_1", chart(F98_0)),
        ("prefix_F_2", chart(F97_0)),
        ("prefix_F_3", chart(F96_0 + u*F97_1)),
        ("prefix_G_1", chart(G65_0)),
        ("prefix_G_2", chart(G64_0)),
        ("prefix_G_3", chart(G63_0 + u*G64_1)),
    ]
    jacobian = [(f"prefix_J_d162_k{k}", J_ROWS[k]) for k in range(17, 27)]
    return direct + jacobian


def verify_frozen_prefix() -> tuple[dict, list[tuple[str, sp.Expr]]]:
    assert sha256(FROZEN_DRIVER) == EXPECTED_DRIVER_SHA256
    assert sha256(FROZEN_RESULT) == EXPECTED_RESULT_SHA256
    expected_bytes = FROZEN_RESULT.read_bytes()
    completed = subprocess.run(
        ["python3", str(FROZEN_DRIVER)], capture_output=True, check=True
    )
    assert completed.stderr == b""
    replay = completed.stdout
    assert replay == expected_bytes
    expected = json.loads(expected_bytes)
    prefix = frozen_prefix_rows()
    expected_direct = expected["direct_rows"]["F"] + expected["direct_rows"]["G"]
    for (_, actual), wanted in zip(prefix[:6], expected_direct, strict=True):
        assert sp.expand(actual - sp.sympify(wanted)) == 0
    for (_, actual), wanted in zip(
        prefix[6:], expected["jacobian_degree162"]["rows"], strict=True
    ):
        assert sp.expand(actual - sp.sympify(wanted)) == 0
    residual, _mapping, pivots, zero_rows = qstar_reduce(prefix, OUTER_VARIABLES)
    assert len(prefix) == 16 and len(pivots) == 15 and zero_rows == 1 and not residual
    return expected, prefix


def branch_result(branch: str, prefix: list[tuple[str, sp.Expr]]) -> dict:
    if branch == "delta2":
        exponents = {"F": -77, "G": -50}
        next_f = local_rows(F_POLY, branch, 18, -77)
        next_g = local_rows(G_POLY, branch, 12, -50)
        endpoint_dimension = 6689
    else:
        exponents = {"F": -181, "G": -118}
        next_f = local_rows(F_POLY, branch, 9, -181)
        next_g = local_rows(G_POLY, branch, 6, -118)
        endpoint_dimension = 6687
    expected_tags = {"delta2": {"F": [0, 1], "G": [0, 1]},
                     "delta52": {"F": [0], "G": [0]}}
    assert list(next_f) == expected_tags[branch]["F"]
    assert list(next_g) == expected_tags[branch]["G"]
    new_rows = [("next_J_x135_y27", J_ROWS[27])]
    new_rows += [(f"next_F_exp{exponents['F']}_coord{k}", row)
                 for k, row in next_f.items()]
    new_rows += [(f"next_G_exp{exponents['G']}_coord{k}", row)
                 for k, row in next_g.items()]
    residual, mapping, pivots, zero_rows = qstar_reduce(prefix + new_rows, OUTER_VARIABLES)
    pole_first = new_rows[1:] + new_rows[:1]
    alternate_residual, _alternate_map, alternate_pivots, _alternate_zero = qstar_reduce(
        prefix + pole_first, OUTER_VARIABLES
    )
    prefix_residual, _prefix_map, prefix_pivots, _prefix_zero = qstar_reduce(
        prefix, OUTER_VARIABLES
    )
    assert not prefix_residual and len(prefix_pivots) == 15
    incremental = len(pivots) - len(prefix_pivots)
    assert not residual
    assert incremental == (4 if branch == "delta2" else 3)
    assert not alternate_residual and len(alternate_pivots) == len(pivots)
    new_labels = {label for label, _row in new_rows}
    new_pivots = [pivot for pivot in pivots if pivot.row in new_labels]
    assert all(
        sp.cancel(sp.expand(row.subs(mapping, simultaneous=True))) == 0
        for _label, row in prefix + new_rows
    )
    return {
        "branch": branch,
        "endpoint_rank": 15,
        "endpoint_dimension": endpoint_dimension,
        "new_rows": [{"label": label, "expression": expr_text(row)}
                     for label, row in new_rows],
        "new_row_count": len(new_rows),
        "new_Qstar_pivots": [{
            "row": pivot.row,
            "variable": str(pivot.variable),
            "coefficient": str(pivot.coefficient),
            "rhs": expr_text(pivot.rhs),
        } for pivot in new_pivots],
        "incremental_Qstar_rank": incremental,
        "cumulative_Qstar_rank": len(pivots),
        "dependent_or_zero_rows_cumulative": zero_rows,
        "residual_count": len(residual),
        "nonlinear_residue_appears": bool(residual),
        "residual_rows": [{"label": label, "expression": expr_text(row)}
                          for label, row in residual],
        "dimension_after_direct_extension": endpoint_dimension - incremental,
        "controls": {
            "all_rows_reduce_zero": True,
            "unit_triangular_extension_over_endpoint_base": True,
            "J_first_or_poles_first_same_Qstar_rank": True,
            "all_pivot_coefficients_in_Qstar": all(
                pivot.coefficient.is_Rational and pivot.coefficient != 0 for pivot in pivots
            ),
            "resolved_pivot_count": len(mapping),
        },
    }


def main() -> None:
    expected, prefix = verify_frozen_prefix()
    output = {
        "type": "EXACT-Q PRE-OUTER DIRECT NEXT-BAND PROBE",
        "scope": (
            "Frozen 15-pivot direct prefix plus J[x^135 y^27] and the next "
            "F95/G62 pole-coordinate rows; no outer-major D2/D1 preblock."
        ),
        "frozen_prefix": {
            "driver_sha256": EXPECTED_DRIVER_SHA256,
            "result_sha256": EXPECTED_RESULT_SHA256,
            "byte_identical_replay": True,
            "rows_expression_identical": True,
            "row_count": 16,
            "Qstar_rank": expected["rank"]["plus_first_10_J_through_G65"],
            "residual_count": expected["residual_count"],
        },
        "triangular_fragment_certificate": {
            "h2_coefficients": {str(key): expr_text(value) for key, value in H2_MAP.items()},
            "Jacobian_degree162_pairs": ["J(F98,G66)", "J(F99,G65)"],
            "Jacobian_needed_y_degrees": {"F98": [0, 10], "G65": [0, 1]},
            "pole_needed_global_y_degrees": [0, 1],
            "omitted_terms_cannot_reach_requested_slots": True,
        },
        "branches": {
            branch: branch_result(branch, prefix) for branch in ("delta2", "delta52")
        },
        "verdict": "COUNTING-BOUND / DIRECT PRE-OUTER PREFIX ONLY",
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
