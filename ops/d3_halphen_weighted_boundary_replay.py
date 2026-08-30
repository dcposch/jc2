#!/usr/bin/env python3
"""Weighted-boundary gate for the D3 one-point Halphen survivor.

The script derives the weight-15 surface face from the raw degree-three
coefficient model and checks the genus-one/Hesse degeneration ledger.  The
geometric use of a weighted blowup and the rational-forest theorem is proved
in the accompanying report.
"""

from __future__ import annotations

import ast
import json
import sys

import sympy as sp


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def derive(mutate_t5_sign: bool = False):
    x, y, t = sp.symbols("x y t")
    xi, upsilon = sp.symbols("xi upsilon")
    a, ell, s, q0 = sp.symbols("a ell s q0")
    q1, q2 = sp.symbols("q1 q2")
    A2, B2, C2, P2, T2 = sp.symbols("A2 B2 C2 P2 T2")
    V2, M2, Q2, R2, U2 = sp.symbols("V2 M2 Q2 R2 U2")
    A3, B3, C3, P3, T3 = sp.symbols("A3 B3 C3 P3 T3")
    V3, M3, Q3, R3, U3 = sp.symbols("V3 M3 Q3 R3 U3")

    f1 = (
        a * x**3
        + ell * x**2 * y
        + 3 * s * x**2
        + x * (q0 * y**2 + q1 * y + q2)
        + y**3
    )
    f2 = (
        A2 * x**3
        + B2 * y**3
        + C2
        + P2 * x**2 * y
        + T2 * x * y**2
        + V2 * x**2
        + M2 * x * y
        + Q2 * y**2
        + R2 * x
        + U2 * y
    )
    f3 = (
        A3 * x**3
        + B3 * y**3
        + C3
        + P3 * x**2 * y
        + T3 * x * y**2
        + V3 * x**2
        + M3 * x * y
        + Q3 * y**2
        + R3 * x
        + U3 * y
    )
    raw = sp.expand(x**3 + t * f1 + t**2 * f2 + t**3 * f3)

    # CFS state-machine equations on the triple-root branch.  Work on s!=0,
    # already forced by eta!=0 in the predecessor theorem.
    b = sp.expand(Q2 - s * q0)
    lam = b / 3
    first_cube = {
        q2: 0,
        C2: 0,
        q1: 0,
        U2: 0,
        R2: 3 * s**2,
        C3: s**3,
    }
    u3_solution = sp.expand(b**2 / 3 - s**2 * ell + s * M2)
    r3_from_d = sp.expand(-s**2 * a + s * V2 - b**3 / (27 * s))
    kappa = sp.expand(
        3 * a * s**2
        + 2 * ell * s * lam
        + q0 * lam**2
        - 2 * V2 * s
        - M2 * lam
        + R3
    )
    a_solution_list = sp.solve(sp.expand(kappa.subs(R3, r3_from_d)), a)
    require(len(a_solution_list) == 1, "kappa equation did not solve uniquely on s!=0")
    a_solution = sp.expand(a_solution_list[0])
    r3_solution = sp.expand(r3_from_d.subs(a, a_solution))
    critical_subs = {
        **first_cube,
        U3: u3_solution,
        a: a_solution,
        R3: r3_solution,
    }

    eta = sp.expand(
        -A2 * s**3
        - P2 * s**2 * lam
        - T2 * s * lam**2
        - B2 * lam**3
        + V3 * s**2
        + M3 * s * lam
        + Q3 * lam**2
    )
    shifted = sp.expand(
        raw.subs(critical_subs).subs({x: xi - s * t, y: upsilon - lam * t})
    )
    shifted_poly = sp.Poly(shifted, xi, upsilon, t)
    weighted_terms: dict[int, list[tuple[tuple[int, ...], sp.Expr]]] = {}
    for monomial, coefficient_value in shifted_poly.terms():
        weight = 5 * monomial[0] + 4 * monomial[1] + 3 * monomial[2]
        weighted_terms.setdefault(weight, []).append((monomial, coefficient_value))
    minimum_weight = min(weighted_terms)
    higher_weights = sorted(weight for weight in weighted_terms if weight > 15)
    weight_15 = sp.expand(
        sum(
            coefficient_value
            * xi ** monomial[0]
            * upsilon ** monomial[1]
            * t ** monomial[2]
            for monomial, coefficient_value in weighted_terms.get(15, [])
        )
    )
    alpha = sp.factor(shifted_poly.coeff_monomial(xi * upsilon * t**2))
    expected_alpha = sp.factor(
        (3 * M2 - 2 * Q2 * q0 - 6 * ell * s + 2 * q0**2 * s) / 3
    )
    intrinsic_alpha = sp.factor(M2 - 2 * s * ell - 2 * lam * q0)
    expected_t5 = -eta if mutate_t5_sign else eta
    expected_face = sp.expand(
        xi**3 + t * upsilon**3 + expected_alpha * t**2 * xi * upsilon + expected_t5 * t**5
    )
    require(minimum_weight == 15, "a term appeared below weighted degree 15")
    require(sp.expand(alpha - expected_alpha) == 0, "mixed face coefficient drifted")
    require(
        sp.expand(expected_alpha - intrinsic_alpha) == 0,
        "intrinsic alpha formula drifted",
    )
    require(higher_weights and higher_weights[0] >= 16, "higher-weight gap drifted")
    require(sp.expand(weight_15 - expected_face) == 0, "weighted face identity failed")

    # Weighted P(5,4,3), degree 15, is well formed.  The standard Hilbert
    # series genus formula gives 2p_a=2.
    weights = (5, 4, 3)
    degree = 15
    require(
        all(sp.gcd(weights[i], weights[j]) == 1 for i in range(3) for j in range(i + 1, 3)),
        "weighted plane is not well formed",
    )
    twice_genus = sp.expand(
        sp.Rational(degree**2, weights[0] * weights[1] * weights[2])
        - degree
        * (
            sp.Rational(1, weights[0] * weights[1])
            + sp.Rational(1, weights[0] * weights[2])
            + sp.Rational(1, weights[1] * weights[2])
        )
        + sum(sp.Rational(sp.gcd(degree, weight), weight) for weight in weights)
        - 1
    )
    require(twice_genus == 2, "weighted arithmetic-genus ledger drifted")

    # On t!=0, pass to the index-three chart.  The residual mu_3 quotient of
    # the affine Hesse cubic is smooth exactly off alpha^3+27*eta=0.
    X, Y, alpha_symbol, eta_symbol = sp.symbols("X Y alpha eta")
    hesse = X**3 + Y**3 + alpha_symbol * X * Y + eta_symbol
    hesse_x = sp.diff(hesse, X)
    hesse_y = sp.diff(hesse, Y)
    require(hesse_x == 3 * X**2 + alpha_symbol * Y, "Hesse X derivative drifted")
    require(hesse_y == 3 * Y**2 + alpha_symbol * X, "Hesse Y derivative drifted")
    zeta = sp.symbols("zeta")
    singular_candidate = {
        X: -alpha_symbol * zeta / 3,
        Y: -alpha_symbol * zeta**2 / 3,
    }
    candidate_value = sp.rem(
        sp.Poly(sp.expand(hesse.subs(singular_candidate)), zeta),
        sp.Poly(zeta**3 - 1, zeta),
    ).as_expr()
    require(
        sp.expand(candidate_value - (eta_symbol + alpha_symbol**3 / 27)) == 0,
        "Hesse singular discriminant drifted",
    )
    candidate_dx = sp.rem(
        sp.Poly(sp.expand(hesse_x.subs(singular_candidate)), zeta),
        sp.Poly(zeta**3 - 1, zeta),
    ).as_expr()
    candidate_dy = sp.rem(
        sp.Poly(sp.expand(hesse_y.subs(singular_candidate)), zeta),
        sp.Poly(zeta**3 - 1, zeta),
    ).as_expr()
    require(
        sp.expand(candidate_dx) == 0 and sp.expand(candidate_dy) == 0,
        "Hesse singular-gradient candidate drifted",
    )
    discriminant_gate = alpha_symbol**3 + 27 * eta_symbol

    # The residual action has only the three projective coordinate vertices
    # as fixed points; eta!=0 keeps every one off the projective Hesse cubic.
    Z = sp.symbols("Z")
    hesse_projective = X**3 + Y**3 + alpha_symbol * X * Y * Z + eta_symbol * Z**3
    fixed_vertex_values = (
        hesse_projective.subs({X: 1, Y: 0, Z: 0}),
        hesse_projective.subs({X: 0, Y: 1, Z: 0}),
        hesse_projective.subs({X: 0, Y: 0, Z: 1}),
    )
    require(
        fixed_vertex_values == (1, 1, eta_symbol),
        "projective fixed-point ledger drifted",
    )

    # At the special gate, alpha=3a and eta=-a^3.  On the cubic-root chart
    # the Hesse cubic is a triangle.  The residual mu_3 action cyclically
    # permutes its three lines and its three nodes, so the coarse weighted
    # curve is irreducible rational with one node.
    U, V, omega = sp.symbols("U V omega")
    hesse_triangle = U**3 + V**3 + 3 * U * V - 1
    lines = (
        U + V - 1,
        U + omega * V - omega**2,
        U + omega**2 * V - omega,
    )
    product_lines = sp.expand(lines[0] * lines[1] * lines[2])
    product_remainder = sp.rem(
        sp.Poly(product_lines - hesse_triangle, omega),
        sp.Poly(omega**2 + omega + 1, omega),
    ).as_expr()
    require(sp.expand(product_remainder) == 0, "Hesse triangle factorization failed")
    sigma_l0 = sp.expand(lines[0].subs({U: omega**2 * U, V: omega * V}, simultaneous=True))
    sigma_l1 = sp.expand(lines[1].subs({U: omega**2 * U, V: omega * V}, simultaneous=True))
    sigma_l2 = sp.expand(lines[2].subs({U: omega**2 * U, V: omega * V}, simultaneous=True))
    cycle_remainder = sp.rem(
        sp.Poly(sigma_l0 - omega**2 * lines[2], omega),
        sp.Poly(omega**2 + omega + 1, omega),
    ).as_expr()
    cycle_remainder_1 = sp.rem(
        sp.Poly(sigma_l1 - omega**2 * lines[0], omega),
        sp.Poly(omega**2 + omega + 1, omega),
    ).as_expr()
    cycle_remainder_2 = sp.rem(
        sp.Poly(sigma_l2 - omega**2 * lines[1], omega),
        sp.Poly(omega**2 + omega + 1, omega),
    ).as_expr()
    require(
        all(
            sp.expand(remainder) == 0
            for remainder in (cycle_remainder, cycle_remainder_1, cycle_remainder_2)
        ),
        "mu3 line-cycle certificate failed",
    )

    # The only t=0 point is [0:1:0].  In the Y=1 orbifold chart, the partial
    # derivative in t is one, so resolution of the ambient quotient adds only
    # rational trees and does not alter the curve's genus/cycle invariant.
    face_local_y1 = X**3 + t + alpha_symbol * t**2 * X + eta_symbol * t**5
    require(
        sp.diff(face_local_y1, t).subs({X: 0, t: 0}) == 1,
        "t=0 weighted-curve regularity certificate failed",
    )

    source_tree = ast.parse(open(__file__, encoding="utf-8").read())
    assert_count = sum(isinstance(node, ast.Assert) for node in ast.walk(source_tree))
    require(assert_count == 0, "replay contains optimization-sensitive asserts")

    return {
        "schema": "D3-HALPHEN-WEIGHTED-BOUNDARY/v1",
        "sympy_version": sp.__version__,
        "analytic_shift": ["xi=x+s*t*z", "upsilon=y+lambda*t*z"],
        "weights": {"xi": 5, "upsilon": 4, "t": 3},
        "minimum_weight": minimum_weight,
        "next_weight": higher_weights[0],
        "weighted_face": "xi^3+t*upsilon^3+alpha*t^2*xi*upsilon+eta*t^5",
        "alpha": str(intrinsic_alpha),
        "eta_nonzero_input": True,
        "weighted_plane": "P(5,4,3)",
        "weighted_degree": degree,
        "arithmetic_genus": int(twice_genus / 2),
        "curve_strata": {
            "smooth_genus_one": str(discriminant_gate) + "!=0",
            "rational_one_node": str(discriminant_gate) + "=0",
            "boundary_tau": 1,
        },
        "rational_forest_compatible": False,
        "ast_assert_nodes": assert_count,
        "status": "PASS",
    }


def main() -> None:
    mutate = sys.argv[1:] == ["--mutate-t5-sign"]
    require(mutate or not sys.argv[1:], "unknown command-line argument")
    result = derive(mutate_t5_sign=mutate)
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    try:
        main()
    except RuntimeError as error:
        print("FAIL:" + str(error), file=sys.stderr)
        raise SystemExit(1)
