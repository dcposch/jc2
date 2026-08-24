#!/usr/bin/env python3
"""Exact secant-idempotent discriminator for the JC2 collision route.

Replay with:

    uv run --no-project --with sympy==1.14.0 \
      python3 cases/fresh_connection_20260824/secant_idempotent.py

The computation is deterministic and writes nothing.  It checks the explicit
cofactor proof that the determinant of a divided-difference Jacobian is the
diagonal idempotent in the self-fiber-product of a Keller map.  It also checks
three characteristic-zero automorphism controls, the characteristic-three
Artin--Schreier collision, and one non-Keller rejection control.
"""

from __future__ import annotations

import hashlib
import json
from typing import Any

import sympy as sp


x, y, u, v = sp.symbols("x y u v")
VARS = (x, y, u, v)


def as_poly(expr: sp.Expr, modulus: int | None) -> sp.Poly:
    expr = sp.expand(expr)
    if modulus is None:
        return sp.Poly(expr, *VARS, domain=sp.QQ)
    return sp.Poly(expr, *VARS, modulus=modulus)


def is_zero(expr: sp.Expr, modulus: int | None) -> bool:
    return as_poly(expr, modulus).is_zero


def exact_quotient(
    numerator: sp.Expr, denominator: sp.Expr, modulus: int | None
) -> sp.Expr:
    quotient, remainder = sp.div(
        as_poly(numerator, modulus), as_poly(denominator, modulus)
    )
    if not remainder.is_zero:
        raise AssertionError(f"nonexact quotient by {denominator}: {remainder}")
    return sp.expand(quotient.as_expr())


def at_second_point(expr: sp.Expr) -> sp.Expr:
    return sp.expand(expr.subs({x: u, y: v}, simultaneous=True))


def canonical_payload(expr: sp.Expr, modulus: int | None) -> list[list[Any]]:
    poly = as_poly(expr, modulus)
    payload: list[list[Any]] = []
    for monomial, coefficient in poly.terms():
        payload.append([*[int(e) for e in monomial], str(coefficient)])
    return payload


def payload_hash(expr: sp.Expr, modulus: int | None) -> str:
    encoded = json.dumps(
        canonical_payload(expr, modulus), separators=(",", ":")
    ).encode()
    return hashlib.sha256(encoded).hexdigest()


def secant_matrix(
    first: sp.Expr, second: sp.Expr, modulus: int | None
) -> tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr]:
    """Use the fixed x-then-y telescoping divided-difference convention."""

    def row(poly: sp.Expr) -> tuple[sp.Expr, sp.Expr]:
        at_u_y = sp.expand(poly.subs(x, u))
        at_u_v = sp.expand(at_u_y.subs(y, v))
        return (
            exact_quotient(poly - at_u_y, x - u, modulus),
            exact_quotient(at_u_y - at_u_v, y - v, modulus),
        )

    a11, a12 = row(first)
    a21, a22 = row(second)
    return a11, a12, a21, a22


def is_unit_ideal(groebner: sp.GroebnerBasis) -> bool:
    return len(groebner.polys) == 1 and groebner.polys[0].is_one


def check_keller_case(
    name: str,
    first: sp.Expr,
    second: sp.Expr,
    *,
    modulus: int | None = None,
    expect_off_empty: bool,
    marked_collision: dict[sp.Symbol, int] | None = None,
) -> dict[str, Any]:
    first_delta = sp.expand(first - at_second_point(first))
    second_delta = sp.expand(second - at_second_point(second))
    a11, a12, a21, a22 = secant_matrix(first, second, modulus)
    determinant = sp.expand(a11 * a22 - a12 * a21)
    jacobian = sp.expand(
        sp.diff(first, x) * sp.diff(second, y)
        - sp.diff(first, y) * sp.diff(second, x)
    )

    checks: dict[str, bool] = {}
    checks["jacobian_is_one"] = is_zero(jacobian - 1, modulus)
    checks["first_secant_row"] = is_zero(
        a11 * (x - u) + a12 * (y - v) - first_delta, modulus
    )
    checks["second_secant_row"] = is_zero(
        a21 * (x - u) + a22 * (y - v) - second_delta, modulus
    )
    checks["determinant_on_diagonal_is_one"] = is_zero(
        at_second_point(determinant) - 1, modulus
    )

    # Adjugate(A) A delta = det(A) delta gives these two explicit ideal
    # memberships.  No Groebner reduction is used for this part.
    det_dx_cofactor = sp.expand(
        determinant * (x - u) - a22 * first_delta + a12 * second_delta
    )
    det_dy_cofactor = sp.expand(
        determinant * (y - v) + a21 * first_delta - a11 * second_delta
    )
    checks["det_annihilates_dx"] = is_zero(det_dx_cofactor, modulus)
    checks["det_annihilates_dy"] = is_zero(det_dy_cofactor, modulus)

    # det(A)-1 vanishes on the diagonal.  Divide it explicitly by the two
    # diagonal generators, then combine with the adjugate identities to get
    # a closed cofactor certificate for det(A)^2-det(A) in the collision
    # ideal.
    det_at_u_y = sp.expand(determinant.subs(x, u))
    c_x = exact_quotient(determinant - det_at_u_y, x - u, modulus)
    c_y = exact_quotient(det_at_u_y - 1, y - v, modulus)
    checks["det_minus_one_in_diagonal_ideal"] = is_zero(
        determinant - 1 - c_x * (x - u) - c_y * (y - v), modulus
    )
    first_cofactor = sp.expand(c_x * a22 - c_y * a21)
    second_cofactor = sp.expand(-c_x * a12 + c_y * a11)
    checks["explicit_idempotent_cofactor"] = is_zero(
        determinant * determinant
        - determinant
        - first_cofactor * first_delta
        - second_cofactor * second_delta,
        modulus,
    )

    groebner_kwargs: dict[str, Any] = {"order": "grevlex"}
    if modulus is None:
        groebner_kwargs["domain"] = sp.QQ
    else:
        groebner_kwargs["modulus"] = modulus
    collision_gb = sp.groebner(
        [first_delta, second_delta], *VARS, **groebner_kwargs
    )
    idempotent_remainder = collision_gb.reduce(
        sp.expand(determinant * determinant - determinant)
    )[1]
    checks["independent_groebner_idempotence"] = is_zero(
        idempotent_remainder, modulus
    )
    off_gb = sp.groebner(
        [first_delta, second_delta, determinant], *VARS, **groebner_kwargs
    )
    checks["off_ideal_expected_emptiness"] = (
        is_unit_ideal(off_gb) == expect_off_empty
    )

    marked_values: dict[str, str] | None = None
    if marked_collision is not None:
        def marked(expr: sp.Expr) -> str:
            value = as_poly(expr, modulus).eval(marked_collision)
            if modulus is not None:
                value = int(value) % modulus
            return str(value)

        marked_values = {
            "first_delta": marked(first_delta),
            "second_delta": marked(second_delta),
            "secant_determinant": marked(determinant),
        }
        checks["marked_off_diagonal_collision"] = (
            marked_values
            == {
                "first_delta": "0",
                "second_delta": "0",
                "secant_determinant": "0",
            }
        )

    if not all(checks.values()):
        raise AssertionError(f"{name} failed: {checks}")

    return {
        "name": name,
        "characteristic": 0 if modulus is None else modulus,
        "jacobian": str(as_poly(jacobian, modulus).as_expr()),
        "secant_determinant": str(as_poly(determinant, modulus).as_expr()),
        "secant_determinant_sha256": payload_hash(determinant, modulus),
        "secant_determinant_terms": len(as_poly(determinant, modulus).terms()),
        "off_ideal_is_unit": is_unit_ideal(off_gb),
        "off_groebner_basis": [str(poly.as_expr()) for poly in off_gb.polys],
        "marked_values": marked_values,
        "checks": checks,
    }


def check_non_keller_rejection() -> dict[str, Any]:
    first = x**2
    second = y
    first_delta = sp.expand(first - at_second_point(first))
    second_delta = sp.expand(second - at_second_point(second))
    a11, a12, a21, a22 = secant_matrix(first, second, None)
    determinant = sp.expand(a11 * a22 - a12 * a21)
    jacobian = sp.expand(sp.diff(first, x) * sp.diff(second, y))
    collision_gb = sp.groebner(
        [first_delta, second_delta], *VARS, order="grevlex", domain=sp.QQ
    )
    remainder = sp.expand(
        collision_gb.reduce(determinant * determinant - determinant)[1]
    )
    checks = {
        "jacobian_not_one": not is_zero(jacobian - 1, None),
        "diagonal_determinant_not_one": not is_zero(
            at_second_point(determinant) - 1, None
        ),
        "idempotence_rejected": not is_zero(remainder, None),
    }
    if not all(checks.values()):
        raise AssertionError(f"non-Keller rejection failed: {checks}")
    return {
        "name": "non_keller_square_control",
        "jacobian": str(jacobian),
        "secant_determinant": str(determinant),
        "idempotence_remainder": str(remainder),
        "checks": checks,
    }


def main() -> None:
    cases = [
        check_keller_case(
            "identity",
            x,
            y,
            expect_off_empty=True,
        ),
        check_keller_case(
            "triangular_degree_four",
            x,
            y + x**4,
            expect_off_empty=True,
        ),
        check_keller_case(
            "tame_two_step_degree_four",
            x + (y + x**2) ** 2,
            y + x**2,
            expect_off_empty=True,
        ),
        check_keller_case(
            "artin_schreier_p3",
            x - x**3,
            y,
            modulus=3,
            expect_off_empty=False,
            marked_collision={x: 0, y: 0, u: 1, v: 0},
        ),
    ]
    output = {
        "schema": "JC2-SECANT-IDEMPOTENT-v1",
        "theorem_checks": {
            "secant_rows": True,
            "adjugate_annihilation": True,
            "diagonal_normalization": True,
            "explicit_idempotent_cofactor": True,
            "saturation_replacement": "I:(dx,dy)^infinity = I+(det A)",
        },
        "cases": cases,
        "negative_control": check_non_keller_rejection(),
        "total_boolean_checks": sum(
            len(case["checks"]) for case in cases
        )
        + 3,
        "verdict": "SECANT-IDEMPOTENT / EXACT-SATURATION-REMOVAL",
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
