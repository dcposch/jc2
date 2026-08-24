#!/usr/bin/env python3
"""Exact replay for the AS109 natural closed-support no-go gate.

This is not a search for a lift.  It uses a tiny sparse polynomial engine,
including a formal coefficient ring, to replay:

1. the determinant split for corrections affine in y;
2. the x^108 divisibility obstruction after the forced factorization;
3. the nonlinear induction identities for full independent monomial slots;
4. a coupled rank-one countercontrol outside the literal-slot theorem.
"""

from __future__ import annotations

import json
from collections.abc import Iterable


P = 109
S_EXP = P - 1

# A formal coefficient is a polynomial over Z in named indeterminates.  A
# monomial is stored as a sorted tuple, so ("a", "k") represents a*k.
SymbolMonomial = tuple[str, ...]
Symbolic = dict[SymbolMonomial, int]
Exponent = tuple[int, int]
Polynomial = dict[Exponent, Symbolic]


def sym_clean(value: Symbolic) -> Symbolic:
    return {monomial: coefficient for monomial, coefficient in value.items() if coefficient}


def sym_const(value: int) -> Symbolic:
    return {} if not value else {(): value}


def sym_var(name: str) -> Symbolic:
    return {(name,): 1}


def sym_add(*values: Symbolic) -> Symbolic:
    out: Symbolic = {}
    for value in values:
        for monomial, coefficient in value.items():
            out[monomial] = out.get(monomial, 0) + coefficient
    return sym_clean(out)


def sym_scale(value: Symbolic, scalar: int) -> Symbolic:
    return sym_clean({monomial: scalar * coefficient for monomial, coefficient in value.items()})


def sym_multiply(left: Symbolic, right: Symbolic) -> Symbolic:
    out: Symbolic = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            monomial = tuple(sorted(left_monomial + right_monomial))
            out[monomial] = out.get(monomial, 0) + left_coefficient * right_coefficient
    return sym_clean(out)


def poly_clean(poly: Polynomial) -> Polynomial:
    return {exponent: sym_clean(coefficient) for exponent, coefficient in poly.items() if sym_clean(coefficient)}


def poly_add(*polys: Polynomial) -> Polynomial:
    out: Polynomial = {}
    for poly in polys:
        for exponent, coefficient in poly.items():
            out[exponent] = sym_add(out.get(exponent, {}), coefficient)
    return poly_clean(out)


def poly_scale(poly: Polynomial, scalar: int) -> Polynomial:
    return poly_clean({exponent: sym_scale(coefficient, scalar) for exponent, coefficient in poly.items()})


def poly_multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    out: Polynomial = {}
    for (a, b), left_coefficient in left.items():
        for (c, d), right_coefficient in right.items():
            exponent = (a + c, b + d)
            product = sym_multiply(left_coefficient, right_coefficient)
            out[exponent] = sym_add(out.get(exponent, {}), product)
    return poly_clean(out)


def derivative(poly: Polynomial, axis: int) -> Polynomial:
    out: Polynomial = {}
    for (a, b), coefficient in poly.items():
        power = (a, b)[axis]
        if not power:
            continue
        exponent = (a - 1, b) if axis == 0 else (a, b - 1)
        out[exponent] = sym_add(out.get(exponent, {}), sym_scale(coefficient, power))
    return poly_clean(out)


def monomial(a: int, b: int, coefficient: int = 1) -> Polynomial:
    return {} if not coefficient else {(a, b): sym_const(coefficient)}


def named_univariate(prefix: str, exponents: Iterable[int]) -> Polynomial:
    return {(exponent, 0): sym_var(f"{prefix}{exponent}") for exponent in exponents}


def times_y(poly: Polynomial) -> Polynomial:
    return {(a, b + 1): coefficient for (a, b), coefficient in poly.items()}


def linear(A: Polynomial, B: Polynomial) -> Polynomial:
    return poly_add(derivative(A, 0), derivative(B, 1))


def nonlinear(A: Polynomial, B: Polynomial) -> Polynomial:
    seed = monomial(S_EXP, 0)
    return poly_add(
        poly_multiply(poly_add(derivative(A, 0), poly_scale(seed, -1)), derivative(B, 1)),
        poly_scale(poly_multiply(derivative(A, 1), derivative(B, 0)), -1),
    )


def jacobian(first: Polynomial, second: Polynomial) -> Polynomial:
    return poly_add(
        poly_multiply(derivative(first, 0), derivative(second, 1)),
        poly_scale(poly_multiply(derivative(first, 1), derivative(second, 0)), -1),
    )


def check_affine_y_split() -> dict[str, object]:
    # The sparse exponent set includes the only coefficient relevant to the
    # final x^108 obstruction (x^109), together with low and mixed controls.
    exponents = (0, 1, 2, 7, 53, 108, 109, 110)
    a = named_univariate("a", exponents)
    b = named_univariate("b", exponents)
    c = named_univariate("c", exponents)
    d = named_univariate("d", exponents)
    A = poly_add(a, times_y(c))
    B = poly_add(d, times_y(b))

    x = monomial(1, 0)
    y = monomial(0, 1)
    xp = monomial(P, 0)
    one = monomial(0, 0)
    first = poly_add(x, poly_scale(xp, -1), poly_scale(A, P))
    second = poly_add(y, poly_scale(B, P))
    determinant_residual = poly_add(jacobian(first, second), poly_scale(one, -1))

    seed = monomial(S_EXP, 0)
    packed = poly_scale(
        poly_add(linear(A, B), poly_scale(seed, -1), poly_scale(nonlinear(A, B), P)),
        P,
    )
    assert determinant_residual == packed

    h = poly_add(one, poly_scale(b, P))
    constant_part = poly_add(
        poly_multiply(h, poly_add(one, poly_scale(seed, -P), poly_scale(derivative(a, 0), P))),
        poly_scale(poly_multiply(c, derivative(d, 0)), -(P**2)),
        poly_scale(one, -1),
    )
    y_coefficient = poly_scale(
        poly_add(
            poly_multiply(h, derivative(c, 0)),
            poly_scale(poly_multiply(c, derivative(b, 0)), -P),
        ),
        P,
    )
    expected_split = poly_add(constant_part, times_y(y_coefficient))
    assert determinant_residual == expected_split
    assert all(y_power in (0, 1) for _, y_power in determinant_residual)

    # Once the y coefficient forces c=k(1+p*b), the constant determinant is
    # h*g=1.  The coefficient below is [x^108]g.  Dividing by p and reducing
    # its formal integer coefficients modulo p leaves the nonzero constant -1.
    k = sym_var("k")
    g = poly_add(
        one,
        poly_scale(seed, -P),
        poly_scale(derivative(a, 0), P),
        {
            exponent: sym_scale(sym_multiply(k, coefficient), -(P**2))
            for exponent, coefficient in derivative(d, 0).items()
        },
    )
    obstruction = g[(S_EXP, 0)]
    expected_obstruction = sym_add(
        sym_const(-P),
        sym_scale(sym_var(f"a{P}"), P**2),
        sym_scale(sym_multiply(k, sym_var(f"d{P}")), -(P**3)),
    )
    assert obstruction == expected_obstruction
    assert all(coefficient % P == 0 for coefficient in obstruction.values())
    divided_mod_p = {
        monomial_key: (coefficient // P) % P
        for monomial_key, coefficient in obstruction.items()
        if (coefficient // P) % P
    }
    assert divided_mod_p == {(): P - 1}

    return {
        "packed_determinant_identity": "PASS",
        "affine_y_constant_and_linear_split": "PASS-FORMAL-SPARSE",
        "forced_factor_x108_coefficient": "-109 + 109^2*a_109 - 109^3*k*d_109",
        "coefficient_divided_by_109_mod_109": -1,
        "exact_lift_affine_in_y": "IMPOSSIBLE",
    }


def integer_coefficient(poly: Polynomial) -> dict[Exponent, int]:
    out: dict[Exponent, int] = {}
    for exponent, coefficient in poly.items():
        assert all(not key for key in coefficient), coefficient
        out[exponent] = coefficient.get((), 0)
    return {exponent: coefficient for exponent, coefficient in out.items() if coefficient}


def check_literal_slot_induction() -> dict[str, object]:
    samples = list(range(1, 2 * P + 3))
    q1_A: Polynomial = {}
    q1_B = monomial(S_EXP, 1)
    assert integer_coefficient(linear(q1_A, q1_B)) == {(S_EXP, 0): 1}
    assert integer_coefficient(nonlinear(q1_A, q1_B)) == {(2 * S_EXP, 0): -1}

    p_divisible_indices: list[int] = []
    for k in samples:
        qk_A: Polynomial = {}
        qk_B = monomial(k * S_EXP, 1)
        rk_A = monomial(k * S_EXP + 1, 0)
        rk_B: Polynomial = {}
        multiplier = k * S_EXP + 1

        assert integer_coefficient(linear(qk_A, qk_B)) == {(k * S_EXP, 0): 1}
        assert integer_coefficient(nonlinear(qk_A, qk_B)) == {((k + 1) * S_EXP, 0): -1}
        assert integer_coefficient(linear(rk_A, rk_B)) == {(k * S_EXP, 0): multiplier}

        polarized = poly_add(
            nonlinear(poly_add(rk_A, q1_A), poly_add(rk_B, q1_B)),
            poly_scale(nonlinear(rk_A, rk_B), -1),
            poly_scale(nonlinear(q1_A, q1_B), -1),
        )
        assert integer_coefficient(polarized) == {((k + 1) * S_EXP, 0): multiplier}
        assert (multiplier % P == 0) == (k % P == 1)
        if multiplier % P == 0:
            p_divisible_indices.append(k)

    # Coupled-section scope control.  Its raw support contains P*x^109 and
    # Q*x^108*y, but neither literal slot is independently variable.
    coupled_A = monomial(P, 0)
    coupled_B = monomial(S_EXP, 1, 1 - P)
    assert integer_coefficient(linear(coupled_A, coupled_B)) == {(S_EXP, 0): 1}
    assert integer_coefficient(nonlinear(coupled_A, coupled_B)) == {
        (2 * S_EXP, 0): -((P - 1) ** 2)
    }

    return {
        "induction_identity_samples": [1, 2 * P + 2],
        "all_induction_identities": "PASS",
        "p_divisible_P_slot_multipliers_at_k": p_divisible_indices,
        "base_Q_slot_forced_by_unit_right_inverse": True,
        "full_independent_literal_slot_certificate": "IMPOSSIBLE",
        "coupled_scope_control": {
            "generator": "(x^109, (1-109)*x^108*y)",
            "L": "x^108",
            "N": "-108^2*x^216",
            "Q_slot_independently_variable": False,
            "closure_on_W=span(x^108)": "FAIL",
        },
    }


def main() -> None:
    print(
        json.dumps(
            {
                "verdict": "PASS-AS109-NATURAL-NOGO",
                "prime": P,
                "affine_y": check_affine_y_split(),
                "literal_slot": check_literal_slot_induction(),
                "enumeration_run": False,
                "lift_found": False,
                "characteristic_zero_inference": False,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
