#!/usr/bin/env python3
"""Exact unit-S first-correction factor and pole-order audit."""

from __future__ import annotations

from fractions import Fraction as Q
import hashlib
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PINS = {
    ROOT / "xmodel/ggv-upper-endpoint-deep-newton-kernel-family-sol-ultra-20260828.md":
        "7eaf108c7ef0ac98ce30d436dcb3db64d17f818a7d34b9dfb9fa9ae1b1f4af9d",
    ROOT / "cases/ggv_8_28_upper_endpoint_deep_newton_kernel_family_20260828/verify_deep_newton_kernel_family.py":
        "0b873f2b4e0cdd4f55312dea6bf2d69d4fcbb3bb03c5725c082028148847c99f",
    ROOT / "xmodel/ggv-upper-endpoint-deep-q1-composition-addendum-r1-sol-ultra-20260828.md":
        "76529aa25dc648e5aab40e20e5426a8c90ec496a4cafbf704c0c2102cd1d9eff",
    ROOT / "cases/ggv_8_28_upper_endpoint_deep_q1_composition_r1_20260828/verify_deep_q1_composition_r1.py":
        "a5e6479f20cd7fcd50b317e174fd192512e5295de9c2126e717c005cb22acf69",
}


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


# Sparse Q[a,s,u,t].
ZERO = (0, 0, 0, 0)


def var(index):
    exponent = [0, 0, 0, 0]
    exponent[index] = 1
    return {tuple(exponent): Q(1)}


def add(*items):
    out = {}
    for item in items:
        for monomial, coefficient in item.items():
            out[monomial] = out.get(monomial, Q(0)) + coefficient
            if not out[monomial]:
                del out[monomial]
    return out


def scale(value, item):
    value = Q(value)
    return {monomial: value * coefficient
            for monomial, coefficient in item.items() if value * coefficient}


def mul(*items):
    out = {ZERO: Q(1)}
    for right in items:
        product = {}
        for monomial1, coefficient1 in out.items():
            for monomial2, coefficient2 in right.items():
                monomial = tuple(a + b for a, b in zip(monomial1, monomial2))
                product[monomial] = (
                    product.get(monomial, Q(0)) + coefficient1 * coefficient2
                )
                if not product[monomial]:
                    del product[monomial]
        out = product
    return out


def power(item, exponent):
    out = {ZERO: Q(1)}
    for _ in range(exponent):
        out = mul(out, item)
    return out


def partitions(total, minimum=1):
    """Nondecreasing positive partitions of total."""
    if total == 0:
        yield ()
        return
    for first in range(minimum, total + 1):
        for tail in partitions(total - first, first):
            yield (first,) + tail


def minimum_l_exponent(total, leading_exponent, mode_delay=0):
    # f_1 is divisible by L^2; no divisibility is assumed for f_i, i>=2.
    values = []
    residual = total - mode_delay
    if residual == 0:
        return leading_exponent
    for partition in partitions(residual):
        factors = len(partition)
        divisibility = 2 * sum(index == 1 for index in partition)
        values.append(leading_exponent - 4 * factors + divisibility)
    return min(values)


def main():
    for path, expected in PINS.items():
        assert sha256(path) == expected, path

    a, s, u, t = (var(index) for index in range(4))
    linear = add(a, scale(Q(1, 4), mul(s, t)))
    r0 = scale(4, mul(s, u))
    f5 = scale(Q(1, 128), mul(power(s, 2), u))

    explicit_first = add(
        scale(Q(1, 8), mul(power(a, 2), u, power(t, 3))),
        scale(Q(1, 64), mul(a, r0, power(t, 4))),
        mul(f5, power(t, 5)),
    )
    factored_first = scale(
        Q(1, 8), mul(u, power(t, 3), power(linear, 2))
    )
    assert explicit_first == factored_first

    # Relative to the leading epsilon^6 of G, the F^(3/2) contribution has
    # no possible denominator in the face factor L through epsilon^3.
    pure = {n: minimum_l_exponent(n, 6) for n in range(1, 5)}
    assert pure == {1: 4, 2: 2, 3: 0, 4: -2}

    # c2*t^2*F^(5/4) is delayed by one epsilon order and is likewise regular
    # through relative order three.  The c4 and c6 leading terms are ordinary
    # powers L^4 and L^3 at delays two and three.
    c2 = {n: minimum_l_exponent(n, 5, mode_delay=1)
          for n in range(1, 5)}
    assert c2 == {1: 5, 2: 3, 3: 1, 4: -1}
    assert minimum_l_exponent(2, 4, mode_delay=2) == 4
    assert minimum_l_exponent(3, 3, mode_delay=3) == 3

    print("unit_S_relations=R0=4*S0*U0;F5(alpha)=S0^2*U0/128")
    print("first_explicit_correction=U0*tau^3*(S0*tau+4*A_prime)^2/128")
    print("first_correction_divisible_by_linear_face_squared=true")
    print("F_three_halves_min_L_exponents_orders_1_to_4=4,2,0,-2")
    print("c2_F_five_fourths_min_L_exponents_orders_1_to_4=5,3,1,-1")
    print("no_unit_S_fractional_pole_through_relative_epsilon_order=3")
    print("first_possible_unit_S_fractional_pole_order=4")
    print("PASS_EXACT_UNIT_S_FIRST_CORRECTION")


if __name__ == "__main__":
    main()
