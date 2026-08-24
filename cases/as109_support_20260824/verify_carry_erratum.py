#!/usr/bin/env python3
"""Standalone exact replay for the AS109 base-109 carry erratum.

This program does not import the producer replay.  It checks the frozen
producer/reviewer hashes, the five-slot countercontrol, and the fact that the
parametric triangular-gauge obstruction has zero first-layer carry over Z.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


P = 109
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
Exponent = tuple[int, int]
Polynomial = dict[Exponent, int]

ORIGINAL_HASHES = {
    "xmodel/as109-support-gate-20260824.md":
        "b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5",
    "xmodel/as109-support-review-grok-20260824.md":
        "1448985c259d2adb9b7e982fee233e802100fa8a0fd2eb32822b617e0a4632e8",
    "cases/as109_support_20260824/PREREGISTRATION.md":
        "be9138a90b661f069197a4c22235ee1caa4e03fcecd2dab8c980e8934f2d6301",
    "cases/as109_support_20260824/manifest.json":
        "c69d70805bdba5793f385fca9c289f9a12a8c58c45e1625e1c2f69a9632f0364",
    "cases/as109_support_20260824/FREEZE.sha256":
        "0a535ca2877ec3672044faa5c5f20878c4b95adddf4087b89f772d030d6e140e",
    "cases/as109_support_20260824/verify_spec_obstruction.py":
        "1bb8f86596b75bd43e467dc84b569e8fb2bb2744c198c40f5244f0b054634165",
    "cases/as109_support_20260824/spec_obstruction.json":
        "b95ad244da3ea75100c61143dc9c0026ac567c8acfc2398a86ce1623a101131e",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def clean(poly: Polynomial) -> Polynomial:
    return {exponent: coefficient for exponent, coefficient in poly.items() if coefficient}


def add(*polys: Polynomial) -> Polynomial:
    out: Polynomial = {}
    for poly in polys:
        for exponent, coefficient in poly.items():
            out[exponent] = out.get(exponent, 0) + coefficient
    return clean(out)


def scale(poly: Polynomial, scalar: int) -> Polynomial:
    return clean({exponent: scalar * coefficient for exponent, coefficient in poly.items()})


def multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    out: Polynomial = {}
    for (a, b), c1 in left.items():
        for (c, d), c2 in right.items():
            exponent = (a + c, b + d)
            out[exponent] = out.get(exponent, 0) + c1 * c2
    return clean(out)


def derivative(poly: Polynomial, axis: int) -> Polynomial:
    out: Polynomial = {}
    for (a, b), coefficient in poly.items():
        power = (a, b)[axis]
        if not power:
            continue
        exponent = (a - 1, b) if axis == 0 else (a, b - 1)
        out[exponent] = out.get(exponent, 0) + coefficient * power
    return clean(out)


def reduce_mod(poly: Polynomial, modulus: int) -> Polynomial:
    return clean({exponent: coefficient % modulus for exponent, coefficient in poly.items()})


def divide_coefficients(poly: Polynomial, divisor: int) -> Polynomial:
    assert all(coefficient % divisor == 0 for coefficient in poly.values())
    return clean({exponent: coefficient // divisor for exponent, coefficient in poly.items()})


def delta_marked(poly: Polynomial) -> int:
    at_one = sum(coefficient for (a, b), coefficient in poly.items() if b == 0)
    at_zero = poly.get((0, 0), 0)
    return at_one - at_zero


def linear(A: Polynomial, B: Polynomial) -> Polynomial:
    return add(derivative(A, 0), derivative(B, 1))


def nonlinear(A: Polynomial, B: Polynomial) -> Polynomial:
    seed = {(P - 1, 0): 1}
    return add(
        multiply(add(derivative(A, 0), scale(seed, -1)), derivative(B, 1)),
        scale(multiply(derivative(A, 1), derivative(B, 0)), -1),
    )


def jacobian(first: Polynomial, second: Polynomial) -> Polynomial:
    return add(
        multiply(derivative(first, 0), derivative(second, 1)),
        scale(multiply(derivative(first, 1), derivative(second, 0)), -1),
    )


def check_original_hashes() -> None:
    for relative, expected in ORIGINAL_HASHES.items():
        actual = digest(REPO / relative)
        assert actual == expected, (relative, expected, actual)


def check_five_slot_countercontrol() -> dict[str, object]:
    x = {(1, 0): 1}
    y = {(0, 1): 1}
    one = {(0, 0): 1}
    seed_power = {(P, 0): 1}
    s = {(P - 1, 0): 1}

    A0 = {(P, 0): 1, (1, 0): -1}
    B0 = {(0, 1): 1, (P - 1, 1): 1}
    A1: Polynomial = {}
    B1 = {(0, 1): 1, (P - 1, 1): 2, (2 * P - 2, 1): 1}

    C1 = add(linear(A0, B0), scale(s, -1))
    N0 = nonlinear(A0, B0)
    second_uncarried = add(linear(A1, B1), N0)
    assert C1 == {(P - 1, 0): P}
    assert reduce_mod(C1, P) == {}
    assert reduce_mod(second_uncarried, P) == {}

    carry = divide_coefficients(C1, P)
    corrected_second = reduce_mod(add(carry, second_uncarried), P)
    assert corrected_second == s

    assert all(delta_marked(poly) == 0 for poly in (A0, B0, A1, B1))
    slots = (
        {("P", exponent) for exponent in A0 | A1}
        | {("Q", exponent) for exponent in B0 | B1}
    )
    assert len(slots) == 5

    first = add(x, scale(seed_power, -1), scale(A0, P), scale(A1, P**2))
    second = add(y, scale(B0, P), scale(B1, P**2))
    determinant_residual = add(jacobian(first, second), scale(one, -1))
    residual_mod_p3 = reduce_mod(determinant_residual, P**3)
    expected_residual = {(P - 1, 0): P**2}
    assert residual_mod_p3 == expected_residual

    return {
        "slot_count": len(slots),
        "frozen_E1_mod_109": "PASS",
        "frozen_uncarried_E2_mod_109": "PASS",
        "marked_collision_over_Z": "PASS",
        "carry_K": "x^108",
        "corrected_E2_residual_mod_109": "x^108",
        "determinant_minus_one_mod_109_cubed": "109^2*x^108",
    }


def check_parametric_zero_carry() -> list[dict[str, object]]:
    s = {(P - 1, 0): 1}
    records: list[dict[str, object]] = []
    for m in (1, 2, 108, 109, 110, 1000):
        A0 = {(0, m): 1}
        B0 = {(P - 1, 1): 1}
        A1 = {(P - 1, m): -1}
        B1 = {(2 * P - 2, 1): 1, (P - 2, m + 1): P - 1}

        C1 = add(linear(A0, B0), scale(s, -1))
        N0 = nonlinear(A0, B0)
        expected_N = {
            (2 * P - 2, 0): -1,
            (P - 2, m): -m * (P - 1),
        }
        assert C1 == {}
        assert N0 == expected_N
        assert add(linear(A1, B1), N0) == {}
        assert all(delta_marked(poly) == 0 for poly in (A0, B0, A1, B1))
        assert reduce_mod(N0, P) == reduce_mod(
            {(2 * P - 2, 0): -1, (P - 2, m): m}, P
        )
        records.append(
            {
                "m": m,
                "C1_over_Z": "0",
                "carry_K": "0",
                "L1_plus_N_over_Z": "0",
                "marked_collision_over_Z": "PASS",
            }
        )
    return records


def check_closed_support_controls() -> None:
    canonical_N = nonlinear({}, {(P - 1, 1): 1})
    counterresidual = nonlinear({}, {(2 * P - 2, 1): 1})
    assert canonical_N == {(2 * P - 2, 0): -1}
    assert counterresidual == {(3 * P - 3, 0): -1}


def main() -> None:
    check_original_hashes()
    control = check_five_slot_countercontrol()
    parametric = check_parametric_zero_carry()
    check_closed_support_controls()
    print(
        json.dumps(
            {
                "verdict": "PASS-CARRY-ERRATUM",
                "original_hashes": "PASS",
                "generic_E2_without_carry": "QUARANTINED",
                "five_slot_countercontrol": control,
                "parametric_gauge_obstruction": parametric,
                "no_enumeration_run": True,
                "existence_inference": False,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
