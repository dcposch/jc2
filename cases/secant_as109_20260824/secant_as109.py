#!/usr/bin/env python3
"""Exact SECANT-IDEMPOTENT x AS109 cross-connection discriminator.

Replay with:

    uv run --no-project --with sympy==1.14.0 \
      python3 cases/secant_as109_20260824/secant_as109.py

The script writes nothing.  It checks the characteristic-109 seed secant
factorization, all 108 Chinese-remainder off-sector projectors, their unique
Teichmueller root lifts through 109^3, the universal localized redundancy of
the secant equation, exact tame controls, and the growing-support all-Witt
mechanism control.
"""

from __future__ import annotations

import hashlib
import json
from typing import Any

import sympy as sp


PRIME = 109
OFF_DEGREE = PRIME - 1
x, y, u, v = sp.symbols("x y u v")
VARS = (x, y, u, v)


def mod_poly(expr: sp.Expr, modulus: int = PRIME) -> sp.Poly:
    return sp.Poly(sp.expand(expr), *VARS, modulus=modulus)


def qq_poly(expr: sp.Expr) -> sp.Poly:
    return sp.Poly(sp.expand(expr), *VARS, domain=sp.QQ)


def exact_quotient(expr: sp.Expr, divisor: sp.Expr) -> sp.Expr:
    quotient, remainder = sp.div(qq_poly(expr), qq_poly(divisor))
    if not remainder.is_zero:
        raise AssertionError(f"nonexact division by {divisor}: {remainder}")
    return sp.expand(quotient.as_expr())


def at_second(expr: sp.Expr) -> sp.Expr:
    return sp.expand(expr.subs({x: u, y: v}, simultaneous=True))


def secant_matrix(first: sp.Expr, second: sp.Expr) -> tuple[sp.Expr, ...]:
    def row(poly: sp.Expr) -> tuple[sp.Expr, sp.Expr]:
        at_u_y = sp.expand(poly.subs(x, u))
        at_u_v = sp.expand(at_u_y.subs(y, v))
        return (
            exact_quotient(poly - at_u_y, x - u),
            exact_quotient(at_u_y - at_u_v, y - v),
        )

    return (*row(first), *row(second))


def eval_coefficients(coefficients: list[int], value: int) -> int:
    result = 0
    power = 1
    for coefficient in coefficients:
        result = (result + coefficient * power) % PRIME
        power = power * value % PRIME
    return result


def crt_projector(root: int) -> list[int]:
    # In F_p[t]/(t^(p-1)-1), this is
    # (p-1)^(-1) sum_{k=0}^{p-2} (t/root)^k.
    inverse_order = pow(OFF_DEGREE, -1, PRIME)
    return [
        inverse_order * pow(root, -power, PRIME) % PRIME
        for power in range(OFF_DEGREE)
    ]


def hensel_lift_root(root: int, levels: int = 3) -> int:
    """Lift a nonzero F_109 root of t^108-1 uniquely modulo 109^levels."""
    current = root
    modulus = PRIME
    for _ in range(1, levels):
        next_modulus = modulus * PRIME
        candidates = [
            current + digit * modulus for digit in range(PRIME)
        ]
        lifts = [
            candidate
            for candidate in candidates
            if (pow(candidate, OFF_DEGREE, next_modulus) - 1)
            % next_modulus
            == 0
        ]
        if len(lifts) != 1:
            raise AssertionError((root, modulus, lifts))
        current = lifts[0]
        modulus = next_modulus
    return current


def seed_and_crt_checks() -> dict[str, Any]:
    difference = x - u
    secant_sum = sum(
        x ** (OFF_DEGREE - index) * u**index
        for index in range(PRIME)
    )
    e0 = sp.expand(1 - secant_sum)
    seed_first_delta = sp.expand(
        (x - x**PRIME) - (u - u**PRIME)
    )

    checks: dict[str, bool] = {
        "freshman_dream": mod_poly(
            x**PRIME - u**PRIME - difference**PRIME
        ).is_zero,
        "secant_sum_is_difference_power": mod_poly(
            secant_sum - difference**OFF_DEGREE
        ).is_zero,
        "seed_collision_factorization": mod_poly(
            seed_first_delta
            - difference * (1 - difference**OFF_DEGREE)
        ).is_zero,
        "seed_projector_formula": mod_poly(
            e0 - (1 - difference**OFF_DEGREE)
        ).is_zero,
        "projector_at_diagonal": int(
            mod_poly(e0).eval({x: 0, y: 0, u: 0, v: 0})
        )
        % PRIME
        == 1,
    }

    projector_hash = hashlib.sha256()
    evaluation_checks = 0
    projectors: list[list[int]] = []
    for root in range(1, PRIME):
        coefficients = crt_projector(root)
        projectors.append(coefficients)
        projector_hash.update(bytes(coefficients))
        for value in range(1, PRIME):
            expected = 1 if value == root else 0
            if eval_coefficients(coefficients, value) != expected:
                raise AssertionError((root, value))
            evaluation_checks += 1

    summed = [
        sum(projector[power] for projector in projectors) % PRIME
        for power in range(OFF_DEGREE)
    ]
    checks["crt_projectors_sum_to_one"] = summed == [1] + [0] * (
        OFF_DEGREE - 1
    )
    checks["all_off_roots_simple"] = all(
        (OFF_DEGREE * pow(root, OFF_DEGREE - 1, PRIME)) % PRIME
        != 0
        for root in range(1, PRIME)
    )

    lifted_roots = [hensel_lift_root(root, levels=3) for root in range(1, PRIME)]
    modulus = PRIME**3
    checks["all_teichmueller_lifts_valid_mod_p3"] = all(
        pow(root, OFF_DEGREE, modulus) == 1
        for root in lifted_roots
    )
    checks["all_teichmueller_lifts_distinct_mod_p3"] = (
        len(set(lifted_roots)) == OFF_DEGREE
    )
    checks["all_teichmueller_lifts_reduce_correctly"] = all(
        lifted % PRIME == residue
        for residue, lifted in zip(range(1, PRIME), lifted_roots)
    )

    if not all(checks.values()):
        raise AssertionError(checks)

    root_payload = ",".join(str(root) for root in lifted_roots).encode()
    return {
        "name": "as109_seed_off_algebra",
        "mod_109_change_of_variables": "t=x-u; I=(t*(1-t^108),y-v)",
        "diagonal_projector": "e0=1-t^108",
        "off_algebra": "F_109[u,y,t]/(t^108-1)",
        "off_crt_split": "product over r in F_109^* of F_109[u,y]",
        "off_rank_over_second_source": OFF_DEGREE,
        "target_fiber_ordered_pairs": PRIME * PRIME,
        "target_fiber_off_ordered_pairs": PRIME * OFF_DEGREE,
        "crt_evaluation_checks": evaluation_checks,
        "crt_projector_payload_sha256": projector_hash.hexdigest(),
        "teichmueller_p3_payload_sha256": hashlib.sha256(root_payload).hexdigest(),
        "checks": checks,
    }


def universal_redundancy_checks() -> dict[str, Any]:
    t, w = sp.symbols("t w")
    a11, a12, a21, a22 = sp.symbols("a11 a12 a21 a22")
    first_delta = a11 * t + a12 * w
    second_delta = a21 * t + a22 * w
    determinant = a11 * a22 - a12 * a21

    pp, c, alpha, beta, gamma, delta = sp.symbols(
        "p c alpha beta gamma delta"
    )
    lifted_det = sp.expand(
        (c + pp * alpha) * (1 + pp * delta)
        - pp**2 * beta * gamma
    )
    expected_lifted_det = sp.expand(
        c
        + pp * (alpha + c * delta)
        + pp**2 * (alpha * delta - beta * gamma)
    )

    checks = {
        "adjugate_dx_identity": sp.expand(
            determinant * t - a22 * first_delta + a12 * second_delta
        )
        == 0,
        "adjugate_dy_identity": sp.expand(
            determinant * w + a21 * first_delta - a11 * second_delta
        )
        == 0,
        "generic_p_adic_secant_expansion": sp.expand(
            lifted_det - expected_lifted_det
        )
        == 0,
    }
    if not all(checks.values()):
        raise AssertionError(checks)

    return {
        "name": "localized_off_equation_redundancy",
        "exact_identity": "e*(x-u)=a22*f1-a12*f2",
        "off_sector_consequence": (
            "x-u is a unit, so e lies in the localized collision ideal"
        ),
        "tangent_consequence": (
            "at e=f1=f2=0, de=(x-u)^-1*(a22*df1-a12*df2)"
        ),
        "generic_secant_expansion": (
            "e=c+p(alpha+c*delta)+p^2(alpha*delta-beta*gamma)"
        ),
        "checks": checks,
    }


def tame_controls() -> dict[str, Any]:
    # Exact triangular source gauge, with m=7 as a nontrivial representative.
    m = 7
    first = x + PRIME * y**m
    second = y
    a11, a12, a21, a22 = secant_matrix(first, second)
    triangular_det = sp.expand(a11 * a22 - a12 * a21)

    # The nontrivial two-step tame automorphism used by the parent gate.
    first2 = x + (y + x**2) ** 2
    second2 = y + x**2
    b11, b12, b21, b22 = secant_matrix(first2, second2)
    determinant2 = sp.expand(b11 * b22 - b12 * b21)
    first2_delta = sp.expand(first2 - at_second(first2))
    second2_delta = sp.expand(second2 - at_second(second2))
    off_gb = sp.groebner(
        [first2_delta, second2_delta, determinant2],
        *VARS,
        order="grevlex",
        domain=sp.QQ,
    )

    checks = {
        "triangular_gauge_jacobian": sp.expand(
            sp.diff(first, x) * sp.diff(second, y)
            - sp.diff(first, y) * sp.diff(second, x)
        )
        == 1,
        "triangular_gauge_secant_projector": triangular_det == 1,
        "two_step_tame_jacobian": sp.expand(
            sp.diff(first2, x) * sp.diff(second2, y)
            - sp.diff(first2, y) * sp.diff(second2, x)
        )
        == 1,
        "two_step_tame_off_ideal_unit": (
            len(off_gb.polys) == 1 and off_gb.polys[0].is_one
        ),
    }
    if not all(checks.values()):
        raise AssertionError(checks)

    return {
        "name": "exact_tame_controls",
        "triangular_source_gauge": "(x+109*y^7,y)",
        "triangular_secant_determinant": str(triangular_det),
        "two_step_tame_secant_terms": len(qq_poly(determinant2).terms()),
        "two_step_tame_off_groebner_basis": [
            str(poly.as_expr()) for poly in off_gb.polys
        ],
        "checks": checks,
    }


def all_witt_mechanism_control() -> dict[str, Any]:
    # Exact finite-level maps from the banked unrestricted-support control.
    # Here z is x^108; the determinant telescope is checked symbolically for
    # n=1..6, while the displayed formula proves it for every n.
    z = sp.symbols("z")
    records: list[dict[str, Any]] = []
    checks: dict[str, bool] = {}
    marked_seed_secant = 1 - sum(
        0 ** (OFF_DEGREE - index) * 1**index
        for index in range(PRIME)
    )
    for level in range(1, 7):
        multiplier = sum((PRIME * z) ** index for index in range(level))
        determinant = sp.expand((1 - PRIME * z) * multiplier)
        expected = sp.expand(1 - (PRIME * z) ** level)
        key = f"level_{level}_determinant_telescope"
        checks[key] = sp.expand(determinant - expected) == 0
        marked_key = f"level_{level}_marked_secant_projector"
        checks[marked_key] = marked_seed_secant * sum(
            PRIME**index for index in range(level)
        ) == 0
        records.append(
            {
                "level": level,
                "q_support_size": level,
                "determinant_residual_p_adic_order": level,
                "marked_secant_projector": 0,
            }
        )

    if not all(checks.values()):
        raise AssertionError(checks)
    return {
        "name": "growing_support_all_witt_control",
        "maps": (
            "(x-x^109, y*sum_{j=0}^{n-1}(109*x^108)^j) mod 109^n"
        ),
        "determinant": "1-109^n*x^(108n)",
        "marked_pair": "(0,0),(1,0)",
        "interpretation": (
            "compatible secant off projectors coexist with linearly growing support"
        ),
        "records": records,
        "checks": checks,
    }


def main() -> None:
    sections = [
        seed_and_crt_checks(),
        universal_redundancy_checks(),
        tame_controls(),
        all_witt_mechanism_control(),
    ]
    output = {
        "schema": "JC2-SECANT-AS109-v1",
        "parent": "SECANT-IDEMPOTENT / PROVISIONAL",
        "prime": PRIME,
        "sections": sections,
        "total_boolean_checks": sum(len(section["checks"]) for section in sections),
        "constraint_rank_added_on_off_sectors": 0,
        "enumeration_run": False,
        "aws_used": False,
        "lift_found": False,
        "verdict": "COSTUME / NEED-GLOBAL-BOUNDED-ALGEBRAIC-OFF-DATUM",
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
