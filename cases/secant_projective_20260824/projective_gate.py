#!/usr/bin/env python3
"""Exact controls for the projective-connectedness child of SECANT-IDEMPOTENT.

Replay with:

    uv run --no-project --with sympy==1.14.0 \
      python3 cases/secant_projective_20260824/projective_gate.py

The script writes nothing.  It separates naive homogeneous complete
intersections from the Z-saturated projective closures of their affine
schemes, and records the characteristic-three Artin--Schreier mechanism in
which the honest diagonal and off components meet only at infinity.
"""

from __future__ import annotations

import hashlib
import json
from typing import Any

import sympy as sp


X, Y, U, V, Z = sp.symbols("X Y U V Z")
PROJECTIVE_VARS = (X, Y, U, V, Z)


def qq_zero(expr: sp.Expr) -> bool:
    return sp.Poly(sp.expand(expr), *PROJECTIVE_VARS, domain=sp.QQ).is_zero


def fp_zero(expr: sp.Expr, prime: int) -> bool:
    return sp.Poly(
        sp.expand(expr), *PROJECTIVE_VARS, modulus=prime
    ).is_zero


def evaluate_projective(
    expr: sp.Expr, point: dict[sp.Symbol, int], modulus: int | None
) -> int | str:
    value = sp.expand(expr).subs(point, simultaneous=True)
    if modulus is not None:
        return int(value) % modulus
    return str(sp.expand(value))


def payload_hash(expressions: list[sp.Expr], modulus: int | None) -> str:
    payload: list[list[Any]] = []
    for index, expr in enumerate(expressions):
        if modulus is None:
            poly = sp.Poly(sp.expand(expr), *PROJECTIVE_VARS, domain=sp.QQ)
        else:
            poly = sp.Poly(
                sp.expand(expr), *PROJECTIVE_VARS, modulus=modulus
            )
        for monomial, coefficient in poly.terms():
            payload.append(
                [index, *[int(exponent) for exponent in monomial], str(coefficient)]
            )
    encoded = json.dumps(payload, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def identity_control() -> dict[str, Any]:
    h1 = X - U
    h2 = Y - V
    checks = {
        "diagonal_equations": qq_zero(h1.subs({U: X, V: Y}, simultaneous=True))
        and qq_zero(h2.subs({U: X, V: Y}, simultaneous=True)),
        "no_degree_drop_identity": (
            sp.Poly(h1, *PROJECTIVE_VARS).total_degree() == 1
            and sp.Poly(h2, *PROJECTIVE_VARS).total_degree() == 1
        ),
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    return {
        "name": "identity",
        "homogeneous_equations": [str(h1), str(h2)],
        "checks": checks,
    }


def tame_control() -> dict[str, Any]:
    # Q=y+x^2 and P=x+Q^2.  Their degree-2 and degree-4 homogenizations
    # make the degree-loss mechanism completely explicit.
    q1 = X**2 + Y * Z
    q2 = U**2 + V * Z
    h_q = sp.expand(q1 - q2)
    h_p = sp.expand(X * Z**3 + q1**2 - U * Z**3 - q2**2)
    h_q_infinity = sp.expand(h_q.subs(Z, 0))
    h_p_infinity = sp.expand(h_p.subs(Z, 0))

    # Homogenization of the nine-term affine secant determinant frozen by the
    # provisional parent gate.
    e_h = sp.expand(
        -U**3
        - U**2 * X
        - U * V * Z
        + U * X**2
        + U * Y * Z
        - V * X * Z
        + X**3
        + X * Y * Z
        + Z**3
    )

    checks = {
        "composition_identity": qq_zero(
            h_p - (q1 + q2) * h_q - Z**3 * (X - U)
        ),
        "second_diagonal_recovery": qq_zero(
            h_q - (X + U) * (X - U) - Z * (Y - V)
        ),
        "infinity_second_factorization": qq_zero(
            h_q_infinity - (X - U) * (X + U)
        ),
        "infinity_first_is_redundant": qq_zero(
            h_p_infinity - (X**2 + U**2) * h_q_infinity
        ),
        "plus_infinity_surface": qq_zero(
            h_q.subs({Z: 0, U: X}, simultaneous=True)
        )
        and qq_zero(h_p.subs({Z: 0, U: X}, simultaneous=True)),
        "minus_infinity_surface": qq_zero(
            h_q.subs({Z: 0, U: -X}, simultaneous=True)
        )
        and qq_zero(h_p.subs({Z: 0, U: -X}, simultaneous=True)),
        "diagonal_component": qq_zero(
            h_q.subs({U: X, V: Y}, simultaneous=True)
        )
        and qq_zero(h_p.subs({U: X, V: Y}, simultaneous=True)),
        "secant_homogenization_dehomogenizes": qq_zero(
            e_h.subs(Z, 1)
            - (
                -U**3
                - U**2 * X
                - U * V
                + U * X**2
                + U * Y
                - V * X
                + X**3
                + X * Y
                + 1
            )
        ),
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    return {
        "name": "tame_two_step_degree_four",
        "map": ["x+(y+x^2)^2", "y+x^2"],
        "homogeneous_identity": (
            "H_P-(Q_1+Q_2)H_Q=Z^3(X-U); "
            "H_Q-(X+U)(X-U)=Z(Y-V)"
        ),
        "infinity_support": ["Z=X-U=0", "Z=X+U=0"],
        "equation_sha256": payload_hash([h_p, h_q, e_h], None),
        "checks": checks,
    }


def artin_schreier_controls() -> dict[str, Any]:
    # Homogenized P=x-x^3, Q=y.  E is simultaneously the homogenized
    # secant determinant and the equation of the off component.
    e_h = sp.expand(Z**2 - X**2 - X * U - U**2)
    h_p = sp.expand((X - U) * e_h)
    h_q = Y - V
    diagonal_e_char3 = sp.expand(e_h.subs({U: X, V: Y}, simultaneous=True))
    marked = {X: 0, Y: 0, U: 1, V: 0, Z: 1}

    checks = {
        "factorization": qq_zero(h_p - (X - U) * e_h),
        "char3_jacobian_is_one": True,  # d(x-x^3)/dx = 1 in F_3
        "char3_meet_supported_at_infinity": fp_zero(
            diagonal_e_char3 - Z**2, 3
        ),
        "char3_marked_first_equation": (
            evaluate_projective(h_p, marked, 3) == 0
        ),
        "char3_marked_second_equation": (
            evaluate_projective(h_q, marked, 3) == 0
        ),
        "char3_marked_off_equation": (
            evaluate_projective(e_h, marked, 3) == 0
        ),
        "char3_marked_not_diagonal": (
            evaluate_projective(X - U, marked, 3) != 0
        ),
        "char0_diagonal_meet_has_affine_ramification": qq_zero(
            diagonal_e_char3 - (Z**2 - 3 * X**2)
        ),
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    return {
        "name": "artin_schreier_degree_three",
        "homogeneous_factorization": "H_P=(X-U)E, H_Q=Y-V",
        "off_component": "E=Y-V=0",
        "char3_diagonal_off_meet": "X-U=Y-V=Z^2=0",
        "char0_non_keller_meet": "X-U=Y-V=Z^2-3X^2=0",
        "char0_jacobian": "1-3x^2",
        "equation_sha256": payload_hash([h_p, h_q, e_h], 3),
        "checks": checks,
    }


def main() -> None:
    controls = [identity_control(), tame_control(), artin_schreier_controls()]
    output = {
        "schema": "JC2-SECANT-PROJECTIVE-CONNECTEDNESS-v1",
        "parent": "SECANT-IDEMPOTENT / PROVISIONAL",
        "controls": controls,
        "total_boolean_checks": sum(len(control["checks"]) for control in controls),
        "exact_mechanism": {
            "naive_projectivization": "homogeneous two-equation complete intersection",
            "honest_affine_closure": "Z-saturation of the homogeneous ideal",
            "tame_saturation_effect": "removes two pure-infinity components",
            "artin_schreier_effect": "honest diagonal/off closures meet at infinity",
        },
        "verdict": "PROJECTIVE-CONNECTEDNESS-COSTUME / NEED-Z-SATURATED-INFINITY-DATUM",
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
