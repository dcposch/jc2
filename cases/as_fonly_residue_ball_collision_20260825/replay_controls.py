#!/usr/bin/env python3
"""Exact finite-ring controls for the AS residue-ball collision theorem."""

from __future__ import annotations

import hashlib
import json
from itertools import product


Monomial = tuple[int, int]
Polynomial = dict[Monomial, int]
Point = tuple[int, int]


def add(*polynomials: Polynomial) -> Polynomial:
    out: Polynomial = {}
    for polynomial in polynomials:
        for monomial, coefficient in polynomial.items():
            out[monomial] = out.get(monomial, 0) + coefficient
    return {monomial: coefficient for monomial, coefficient in out.items()
            if coefficient}


def scale(scalar: int, polynomial: Polynomial) -> Polynomial:
    return {monomial: scalar * coefficient
            for monomial, coefficient in polynomial.items()
            if scalar * coefficient}


def multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    out: Polynomial = {}
    for (i, j), a in left.items():
        for (k, ell), b in right.items():
            monomial = (i + k, j + ell)
            out[monomial] = out.get(monomial, 0) + a * b
    return {monomial: coefficient for monomial, coefficient in out.items()
            if coefficient}


def derivative(polynomial: Polynomial, variable: int) -> Polynomial:
    out: Polynomial = {}
    for (i, j), coefficient in polynomial.items():
        exponent = i if variable == 0 else j
        if not exponent:
            continue
        monomial = (i - 1, j) if variable == 0 else (i, j - 1)
        out[monomial] = out.get(monomial, 0) + exponent * coefficient
    return {monomial: coefficient for monomial, coefficient in out.items()
            if coefficient}


def jacobian(left: Polynomial, right: Polynomial) -> Polynomial:
    return add(multiply(derivative(left, 0), derivative(right, 1)),
               scale(-1, multiply(derivative(left, 1),
                                  derivative(right, 0))))


def evaluate(polynomial: Polynomial, point: Point, modulus: int) -> int:
    x, y = point
    return sum(coefficient * pow(x, i, modulus) * pow(y, j, modulus)
               for (i, j), coefficient in polynomial.items()) % modulus


def map_value(left: Polynomial, right: Polynomial, point: Point,
              modulus: int) -> Point:
    return (evaluate(left, point, modulus),
            evaluate(right, point, modulus))


def matrix_at(left: Polynomial, right: Polynomial, point: Point,
              modulus: int) -> tuple[tuple[int, int], tuple[int, int]]:
    return ((evaluate(derivative(left, 0), point, modulus),
             evaluate(derivative(left, 1), point, modulus)),
            (evaluate(derivative(right, 0), point, modulus),
             evaluate(derivative(right, 1), point, modulus)))


def matvec(matrix: tuple[tuple[int, int], tuple[int, int]], vector: Point,
           modulus: int) -> Point:
    return ((matrix[0][0] * vector[0] + matrix[0][1] * vector[1]) % modulus,
            (matrix[1][0] * vector[0] + matrix[1][1] * vector[1]) % modulus)


def hensel_preimage(left: Polynomial, right: Polynomial, residue: Point,
                    target: Point, depth: int) -> tuple[Point, list[dict]]:
    """Lift one prescribed source residue to F(x)=target modulo 3^depth."""
    assert depth >= 1
    assert map_value(left, right, residue, 3) == (target[0] % 3,
                                                  target[1] % 3)
    current = (residue[0] % 3, residue[1] % 3)
    trace = []
    for level in range(1, depth):
        modulus = 3 ** (level + 1)
        step = 3 ** level
        candidates = []
        for digit in product(range(3), repeat=2):
            lifted = ((current[0] + step * digit[0]) % modulus,
                      (current[1] + step * digit[1]) % modulus)
            if map_value(left, right, lifted, modulus) == (
                    target[0] % modulus, target[1] % modulus):
                candidates.append((digit, lifted))
        assert len(candidates) == 1, (level, residue, candidates)

        # Replay the first-order source row used by the induction.
        error = map_value(left, right, current, modulus)
        divided_error = (((target[0] - error[0]) // step) % 3,
                         ((target[1] - error[1]) // step) % 3)
        reduced_matrix = matrix_at(left, right, current, 3)
        assert matvec(reduced_matrix, candidates[0][0], 3) == divided_error
        trace.append({
            "from_level": level,
            "digit": list(candidates[0][0]),
            "lifted_point": list(candidates[0][1]),
            "reduced_jacobian": [list(row) for row in reduced_matrix],
            "divided_error": list(divided_error),
            "unique_digit_count": 1,
        })
        current = candidates[0][1]
    return current, trace


def ordered(polynomial: Polynomial) -> list[list[int | list[int]]]:
    return [[list(monomial), coefficient]
            for monomial, coefficient in sorted(
                polynomial.items(), key=lambda item: (sum(item[0]), item[0]))]


def main() -> None:
    # Frozen cap-seven triangular point.  Its determinant is one modulo 3^6,
    # far beyond the two control precisions consumed here.
    left: Polynomial = {
        (1, 0): 1,
        (3, 0): 2,
        (5, 0): 441,
        (7, 0): 108,
    }
    right: Polynomial = {
        (0, 1): 1,
        (2, 1): -6,
        (4, 1): 18,
        (6, 1): -27,
    }
    determinant = jacobian(left, right)
    expected = {
        (0, 0): 1,
        (4, 0): 2187,
        (6, 0): -12393,
        (8, 0): 34992,
        (10, 0): -45927,
        (12, 0): -20412,
    }
    assert determinant == expected

    records = []
    explicit = {9: ((0, 0), (7, 0), 5),
                27: ((0, 0), (7, 0), 23)}
    for depth in (2, 3):
        modulus = 3 ** depth
        reduced_det = {monomial: coefficient % modulus
                       for monomial, coefficient in determinant.items()
                       if coefficient % modulus}
        assert reduced_det == {(0, 0): 1}
        first, first_trace = hensel_preimage(left, right, (0, 0), (0, 0),
                                             depth)
        second, second_trace = hensel_preimage(left, right, (1, 0), (0, 0),
                                               depth)
        third, third_trace = hensel_preimage(left, right, (2, 0), (0, 0),
                                             depth)
        assert [first[0] % 3, second[0] % 3, third[0] % 3] == [0, 1, 2]
        for point in (first, second, third):
            assert map_value(left, right, point, modulus) == (0, 0)
        unit = pow((first[0] - second[0]) % modulus, -1, modulus)
        assert unit * (first[0] - second[0]) % modulus == 1
        assert (first, second, unit) == explicit[modulus]
        pairwise_units = {}
        for name, left_point, right_point in (
                ("first-second", first, second),
                ("first-third", first, third),
                ("second-third", second, third)):
            difference = (left_point[0] - right_point[0]) % modulus
            inverse = pow(difference, -1, modulus)
            assert difference * inverse % modulus == 1
            pairwise_units[name] = {
                "x_difference": difference,
                "inverse": inverse,
                "unit_equation": difference * inverse % modulus,
            }
        records.append({
            "depth": depth,
            "modulus": modulus,
            "first_source_point": list(first),
            "second_source_point": list(second),
            "third_source_point": list(third),
            "common_target": [0, 0],
            "x_difference_unit_inverse": unit,
            "unit_equation": (unit * (first[0] - second[0])) % modulus,
            "first_hensel_trace": first_trace,
            "second_hensel_trace": second_trace,
            "third_hensel_trace": third_trace,
            "pairwise_x_unit_equations": pairwise_units,
            "full_determinant_modulus": ordered(reduced_det),
        })

    # Load-bearing negative control: its reduction has singular Jacobian.
    bad_left: Polynomial = {(1, 0): 1, (3, 0): -1}
    bad_right: Polynomial = {(0, 1): 3}
    target = (0, 3)
    bad_hits = [
        point for point in product(range(9), repeat=2)
        if point[0] % 3 == 0 and point[1] % 3 == 0
        and map_value(bad_left, bad_right, point, 9) == target
    ]
    assert not bad_hits

    payload = {
        "status": "PASS-AS-RESIDUE-BALL-COLLISION-CONTROLS",
        "control_map": {
            "P": ordered(left),
            "Q": ordered(right),
            "integer_determinant": ordered(determinant),
            "special_fibre": ["x-x^3", "y"],
        },
        "finite_hensel_records": records,
        "negative_control": {
            "map": ["x-x^3", "3y"],
            "modulus": 9,
            "source_ball": "(0,0)+3R_2^2",
            "missing_target": list(target),
            "hit_count": len(bad_hits),
            "reason": "Jacobian is not a unit modulo 3",
        },
        "scope": (
            "finite-ring positive controls only; no all-depth existence, "
            "fixed-support lift, Qbar point, or JC2 inference"),
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["canonical_payload_sha256"] = hashlib.sha256(
        canonical.encode()).hexdigest()
    print(json.dumps(payload, indent=2, sort_keys=True))
    print("PASS-AS-RESIDUE-BALL-COLLISION-CONTROLS")


if __name__ == "__main__":
    main()
