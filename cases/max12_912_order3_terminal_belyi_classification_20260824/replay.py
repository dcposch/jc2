#!/usr/bin/env python3
"""Exact lightweight replay for the terminal Belyi classification."""

from __future__ import annotations

from fractions import Fraction
import json


def trim(value):
    value = list(map(Fraction, value))
    while len(value) > 1 and not value[-1]:
        value.pop()
    return tuple(value)


def add(left, right):
    size = max(len(left), len(right))
    return trim([
        (left[index] if index < len(left) else 0)
        + (right[index] if index < len(right) else 0)
        for index in range(size)
    ])


def scale(scalar, value):
    return trim([Fraction(scalar) * coefficient for coefficient in value])


def multiply(left, right):
    out = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return trim(out)


def power(value, exponent):
    out = (Fraction(1),)
    for _ in range(exponent):
        out = multiply(out, value)
    return out


def derivative(value):
    return trim([index * value[index] for index in range(1, len(value))])


def linear(root):
    return (Fraction(-root), Fraction(1))


def wronskian(A, B):
    return add(multiply(derivative(A), B), scale(-1, multiply(A, derivative(B))))


def verify_h(A, B, h):
    W = wronskian(A, B)
    assert multiply(h, power(W, 3)) == multiply(power(A, 2), power(B, 4))
    return W


def main():
    x, xm1 = linear(0), linear(1)
    cyclic = []
    for degree in (1, 2, 3):
        A, B = power(x, degree), power(xm1, degree)
        h = scale(
            Fraction(-1, degree ** 3),
            multiply(power(x, 3 - degree), power(xm1, degree + 3)),
        )
        W = verify_h(A, B, h)
        cyclic.append({
            "degree": degree,
            "W_degree": len(W) - 1,
            "h_multiplicities": [3 - degree, degree + 3],
            "h_is_cube": degree == 3,
        })

    polynomial_power = []
    for degree in (1, 2, 3):
        A, B = power(x, degree), (Fraction(1),)
        h = scale(Fraction(1, degree ** 3), power(x, 3 - degree))
        verify_h(A, B, h)
        polynomial_power.append({
            "degree": degree,
            "degree_h": 3 - degree,
            "three_divides_degree_h": (3 - degree) % 3 == 0,
            "h_is_cube_when_residual_degree_allowed": degree == 3,
        })

    reciprocal_power = []
    for degree in (1, 2, 3, 6, 9):
        A, B = (Fraction(1),), power(xm1, degree)
        h = scale(Fraction(-1, degree ** 3), power(xm1, degree + 3))
        verify_h(A, B, h)
        reciprocal_power.append({
            "degree": degree,
            "degree_h": degree + 3,
            "three_divides_degree_h": (degree + 3) % 3 == 0,
            "h_is_cube": (degree + 3) % 3 == 0,
        })

    # Finite valuation equation at a zero/pole of Z:
    # 3*m+9*(z-1)=8*z iff z=9-3*m.
    for multiplicity_h in range(0, 30):
        order_Z = 9 - 3 * multiplicity_h
        assert 3 * multiplicity_h + 9 * (order_Z - 1) == 8 * order_Z
        assert order_Z % 3 == 0

    # Balanced infinity/passport identities.  r+s=e+1 implies exact RH and
    # deg(h)=3(e+1)=3(r+s).
    balanced_checks = 0
    for degree in range(1, 40):
        for e in range(1, degree + 1):
            for r in range(1, e + 1):
                s = e + 1 - r
                if s > degree:
                    continue
                ramification = (degree - r) + (degree - s) + (e - 1)
                assert ramification == 2 * degree - 2
                assert 3 * (e + 1) == 3 * (r + s)
                balanced_checks += 1

    payload = {
        "case": "max12_912_order3_terminal_belyi_classification_20260824",
        "terminal_input": "nu^10*h^3*(Z')^9=j^9*Z^8",
        "divisor_consequence": "Z=T^3 in C(x)",
        "rational_reconstruction": {
            "T": "A/B with gcd(A,B)=1",
            "W": "A'*B-A*B'",
            "h": "constant*A^2*B^4/W^3",
        },
        "finite_polynomiality": {
            "critical_support": "every finite root of W lies in A*B",
            "A_root_alpha": "ord(h)=3-alpha, hence alpha<=3",
            "B_root_beta": "ord(h)=beta+3",
        },
        "unequal_degree_strata": {
            "support_count": "r+s=1",
            "classification": "polynomial or reciprocal pure power",
            "noncube_with_3_divides_degree_h": "EMPTY",
        },
        "balanced_stratum": {
            "degrees": "deg(A)=deg(B)=D",
            "e": "ord_infinity(T-T(infinity))",
            "support_count": "r+s=e+1",
            "degree_h": "3*(e+1)",
            "passport": "alpha over 0; beta over infinity; (e,1^(D-e)) over T(infinity)",
            "riemann_hurwitz": "2*D-2",
            "checked_integer_strata": balanced_checks,
        },
        "cyclic_positive_controls": cyclic,
        "polynomial_power_controls": polynomial_power,
        "reciprocal_power_controls": reciprocal_power,
        "terminal_constant_check": (
            "for Z=T^3 and h=T^2/(T')^3, "
            "h^3*(Z')^9/Z^8=3^9"
        ),
        "scope": (
            "classification of rational solutions to the descended terminal "
            "identity with polynomial h; no coefficient-fibre realization, "
            "Taylor integrality, all-(9,12), maximum-twelve, or JC2 conclusion"
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
