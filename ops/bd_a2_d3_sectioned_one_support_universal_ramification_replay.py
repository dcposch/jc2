#!/usr/bin/env python3
"""Desk replay for the D3 one-support universal ramification strata.

This checks the finite linear-algebra and degree/genus ledgers in
``bd-a2-d3-sectioned-one-support-universal-ramification-strata``.  It does
not prove the cited cubic-block, one-place, rational-forest, or conductor
theorems, and it does not search the finite successor parameter space.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys

import sympy as sp


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError("FAIL:" + message)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutate-cfs-exponent", action="store_true")
    parser.add_argument("--mutate-genus-class", action="store_true")
    parser.add_argument("--mutate-infinity-row", action="store_true")
    args = parser.parse_args()

    x, X, y, z, t = sp.symbols("x X y z t")
    monomials: list[tuple[int, int, int, sp.Expr]] = []
    for i in range(4):
        for j in range(4 - i):
            k = 3 - i - j
            monomials.append((i, j, k, x**i * y**j * z**k))

    variables: list[sp.Symbol] = []
    generic_raw = sp.Integer(0)
    for t_order in range(4):
        for i, j, k, monomial in monomials:
            coefficient = sp.symbols(f"c{t_order}_{i}{j}{k}")
            variables.append(coefficient)
            generic_raw += coefficient * t**t_order * monomial

    sheared = sp.Poly(sp.expand(generic_raw.subs(x, X - t * z)), t, X, y, z)
    exponent_multiplier = 1 if args.mutate_cfs_exponent else 2
    drop_equations = [
        coefficient
        for (valuation, _i, _j, z_order), coefficient in sheared.terms()
        if valuation < exponent_multiplier * z_order
    ]
    section_equations = sp.Poly(
        sp.expand(generic_raw.subs({x: -t, y: 0, z: 1})), t
    ).all_coeffs()
    drop_matrix, _ = sp.linear_eq_to_matrix(drop_equations, variables)
    section_matrix, _ = sp.linear_eq_to_matrix(
        drop_equations + section_equations, variables
    )
    drop_rank = drop_matrix.rank()
    section_rank = section_matrix.rank()
    require(
        (drop_rank, len(variables) - drop_rank) == (20, 20),
        "two-drop chart must have vector dimension twenty before the section",
    )
    require(
        (section_rank, len(variables) - section_rank) == (21, 19),
        "moving-section chart must have vector dimension nineteen",
    )

    basis = [
        y**3,
        t * y**2 * z + x * y**2,
        t * y**3,
        t * x * y**2,
        t**2 * y * z**2 + 2 * t * x * y * z + x**2 * y,
        t**2 * y**2 * z,
        t**2 * y**3,
        t**2 * x * y * z + t * x**2 * y,
        t**2 * x * y**2,
        t**2 * x**2 * y,
        t**3 * z**3 + 3 * t**2 * x * z**2 + 3 * t * x**2 * z + x**3,
        t**3 * y * z**2 - t * x**2 * y,
        t**3 * y**2 * z,
        t**3 * y**3,
        t**3 * x * z**2 + 2 * t**2 * x**2 * z + t * x**3,
        t**3 * x * y * z,
        t**3 * x * y**2,
        t**3 * x**2 * z + t**2 * x**3,
        t**3 * x**2 * y,
    ]
    require(len(basis) == 19, "explicit chart basis length changed")
    for form in basis:
        transformed = sp.Poly(sp.expand(form.subs(x, X - t * z)), t, X, y, z)
        require(
            all(
                valuation >= 2 * z_order
                for (valuation, _i, _j, z_order), _coefficient in transformed.terms()
            ),
            "basis vector violates the two-drop divisibility",
        )
        require(
            sp.expand(form.subs({x: -t, y: 0, z: 1})) == 0,
            "basis vector violates the moving section",
        )

    raw_reductions = [sp.expand(form.subs(t, 0)) for form in basis]
    terminal_reductions: list[sp.Expr] = []
    for form in basis:
        terminal = sp.cancel(
            sp.expand(
                form.subs(x, X - t * z).subs(
                    {X: t**2 * X, y: t**2 * y}, simultaneous=True
                )
            )
            / t**6
        )
        terminal_reductions.append(sp.expand(terminal.subs(t, 0)))

    spatial_raw = [
        x**i * y**j * z ** (3 - i - j)
        for i in range(4)
        for j in range(4 - i)
    ]
    raw_matrix = sp.Matrix(
        [
            [sp.Poly(form, x, y, z).coeff_monomial(monomial) for monomial in spatial_raw]
            for form in raw_reductions
        ]
    )
    spatial_terminal = [
        X**i * y**j * z ** (3 - i - j)
        for i in range(4)
        for j in range(4 - i)
    ]
    terminal_matrix = sp.Matrix(
        [
            [
                sp.Poly(form, X, y, z).coeff_monomial(monomial)
                for monomial in spatial_terminal
            ]
            for form in terminal_reductions
        ]
    )
    require(raw_matrix.rank() == 4, "central binary-cubic coverage changed")
    require(
        terminal_matrix.rank() == 9,
        "terminal cubics through the marked point no longer span dimension nine",
    )

    example_coefficients = [
        -2,
        -1,
        2,
        -2,
        -2,
        3,
        3,
        1,
        3,
        1,
        -2,
        -1,
        2,
        3,
        3,
        3,
        1,
        3,
        3,
    ]
    example = sp.expand(
        sum(
            coefficient * form
            for coefficient, form in zip(example_coefficients, basis)
        )
    )
    terminal_example = sp.cancel(
        sp.expand(
            example.subs(x, X - t * z).subs(
                {X: t**2 * X, y: t**2 * y}, simultaneous=True
            )
        )
        / t**6
    )
    terminal_zero = sp.expand(terminal_example.subs(t, 0))
    jacobian = [sp.diff(terminal_zero, variable) for variable in (X, y, z)]
    for chart in (X, y, z):
        chart_variables = tuple(variable for variable in (X, y, z) if variable != chart)
        basis_chart = sp.groebner(
            [derivative.subs(chart, 1) for derivative in jacobian],
            *chart_variables,
        )
        require(
            any(polynomial.as_expr() == 1 for polynomial in basis_chart.polys),
            "terminal smooth-control cubic became singular",
        )
    central_univariate = sp.Poly(
        sp.expand(example.subs({t: 0, y: 1, z: 0})), x
    )
    require(
        sp.discriminant(central_univariate.as_expr(), x) != 0,
        "central binary cubic lost its three distinct roots",
    )

    a_squared, a_times_b, b_squared = 3, 3, 0
    ramification_a_coefficient = 2 if args.mutate_genus_class else 3
    ramification_square = (
        ramification_a_coefficient**2 * a_squared
        + 2 * ramification_a_coefficient * a_times_b
        + b_squared
    )
    ramification_canonical = ramification_a_coefficient * a_times_b + b_squared
    ramification_genus = 1 + (
        ramification_square + ramification_canonical
    ) // 2
    require(
        (ramification_square, ramification_canonical, ramification_genus)
        == (45, 9, 28),
        "clean ramification class/genus ledger changed",
    )
    branch_genus = (12 - 1) * (12 - 2) // 2
    require(branch_genus == 55, "degree-twelve branch genus changed")
    require(branch_genus - ramification_genus == 27, "27 conductor defect changed")

    degree_rows = [(12, 9, 18), (11, 9, 15), (11, 8, 17), (10, 7, 16)]
    if args.mutate_infinity_row:
        degree_rows[-1] = (10, 7, 15)
    require(
        all(3 * branch_degree - 2 * root_degree == residual_degree
            for branch_degree, root_degree, residual_degree in degree_rows),
        "an infinity row violates 3b=2d+e",
    )

    payload = {
        "branch_arithmetic_genus": branch_genus,
        "cfs_drop_rank": drop_rank,
        "clean_conductor_defect": branch_genus - ramification_genus,
        "clean_ramification_arithmetic_genus": ramification_genus,
        "explicit_basis_dimension": len(basis),
        "infinity_degree_rows": degree_rows,
        "moving_section_rank": section_rank,
        "raw_central_span": raw_matrix.rank(),
        "result": "D3_ONE_SUPPORT_UNIVERSAL_RAMIFICATION_STRATA_PASS",
        "terminal_marked_cubic_span": terminal_matrix.rank(),
        "terminal_smooth_control": True,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    print(json.dumps(payload, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(1)
