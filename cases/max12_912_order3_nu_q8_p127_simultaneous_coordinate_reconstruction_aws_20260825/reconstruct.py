#!/usr/bin/env python3
"""Common-denominator reconstruction from 123 exact coordinate fibres."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path


P = 127
EXPECTED_SAMPLES_SHA256 = "0790e9f8bb6b545e742ca9e723c29b9a8dc0268a93dedd91c2f2a7b48f48f231"
COORDINATES = ("c", "d2", "d4", "x1", "x3", "x5", "inv")


def trim(a: list[int]) -> list[int]:
    while a and a[-1] % P == 0:
        a.pop()
    return [x % P for x in a]


def degree(a: list[int] | bytearray) -> int:
    for index in range(len(a) - 1, -1, -1):
        if a[index] % P:
            return index
    return -1


def mul(a: list[int], b: list[int]) -> list[int]:
    if not a or not b:
        return []
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    out[i + j] = (out[i + j] + x * y) % P
    return trim(out)


def evaluate(a: list[int] | bytearray, x: int) -> int:
    result = 0
    for coefficient in reversed(a):
        result = (result * x + coefficient) % P
    return result


def modulus_for_points(points: list[int]) -> list[int]:
    result = [1]
    for point in points:
        result = mul(result, [(-point) % P, 1])
    if len(result) != len(points) + 1 or result[-1] != 1:
        raise RuntimeError("point modulus")
    return result


def derivative(a: list[int]) -> list[int]:
    return [(index * a[index]) % P for index in range(1, len(a))]


def divide_linear(monic: list[int], root: int) -> list[int]:
    n = len(monic) - 1
    quotient = [0] * n
    quotient[n - 1] = monic[n]
    for index in range(n - 1, 0, -1):
        quotient[index - 1] = (monic[index] + root * quotient[index]) % P
    if (monic[0] + root * quotient[0]) % P:
        raise RuntimeError(("linear division", root))
    return quotient


def lagrange_basis(points: list[int], modulus: list[int]) -> list[bytearray]:
    derivative_modulus = derivative(modulus)
    result = []
    for point in points:
        quotient = divide_linear(modulus, point)
        denominator = evaluate(derivative_modulus, point)
        if denominator == 0:
            raise RuntimeError(("repeated point", point))
        inverse = pow(denominator, P - 2, P)
        result.append(bytearray((inverse * value) % P for value in quotient))
    return result


def interpolate(values: list[int], basis: list[bytearray]) -> bytearray:
    result = bytearray(len(basis))
    for value, polynomial in zip(values, basis, strict=True):
        if value:
            for index, coefficient in enumerate(polynomial):
                result[index] = (result[index] + value * coefficient) % P
    return result


def shifted_remainders(polynomial: bytearray, modulus: list[int]) -> list[bytearray]:
    """Return w^ell*polynomial mod modulus for 0<=ell<123."""
    n = len(polynomial)
    if len(modulus) != n + 1 or modulus[-1] != 1:
        raise RuntimeError("shift modulus")
    shifts = [bytearray(polynomial)]
    for _ in range(1, n):
        old = shifts[-1]
        lead = old[-1]
        new = bytearray(n)
        new[0] = (-lead * modulus[0]) % P
        for index in range(1, n):
            new[index] = (old[index - 1] - lead * modulus[index]) % P
        shifts.append(new)
    return shifts


def echelon_add(echelon: dict[int, list[int]], row: list[int]) -> bool:
    columns = len(row)
    for column in range(columns):
        value = row[column] % P
        if value == 0:
            continue
        if column in echelon:
            pivot = echelon[column]
            for index in range(column, columns):
                row[index] = (row[index] - value * pivot[index]) % P
            continue
        inverse = pow(value, P - 2, P)
        for index in range(column, columns):
            row[index] = row[index] * inverse % P
        echelon[column] = row
        return True
    return False


def nullspace_basis(echelon: dict[int, list[int]], columns: int) -> list[list[int]]:
    free = [column for column in range(columns) if column not in echelon]
    result = []
    for free_column in free:
        vector = [0] * columns
        vector[free_column] = 1
        for pivot_column in sorted(echelon, reverse=True):
            row = echelon[pivot_column]
            vector[pivot_column] = (-sum(
                row[index] * vector[index] for index in range(pivot_column + 1, columns)
            )) % P
        result.append(vector)
    return result


def reconstruct_coordinate(
    name: str,
    values_by_v_degree: list[list[int]],
    points: list[int],
    modulus: list[int],
    basis: list[bytearray],
    maximum_denominator_degree: int,
) -> dict:
    interpolants = [interpolate(values, basis) for values in values_by_v_degree]
    shifts = [shifted_remainders(polynomial, modulus) for polynomial in interpolants]
    chosen = None
    tested_pairs = 0
    full_rank_pairs = 0
    rejected_nonunit_pairs = 0
    # Search by increasing total degree.  Searching only the boundary
    # numerator_bound=122-d would accept the tautological degree-122
    # polynomial interpolant at d=0 and learn nothing.  The first passing
    # pair below is the minimal simultaneous rational complexity.
    for total_bound in range(len(points)):
        for denominator_degree in range(min(total_bound, maximum_denominator_degree) + 1):
            numerator_bound = total_bound - denominator_degree
            columns = denominator_degree + 1
            echelon: dict[int, list[int]] = {}
            rows_seen = 0
            for v_degree in range(len(shifts)):
                table = shifts[v_degree]
                for coefficient_degree in range(numerator_bound + 1, len(points)):
                    row = [table[power][coefficient_degree] for power in range(columns)]
                    rows_seen += 1
                    echelon_add(echelon, row)
                    if len(echelon) == columns:
                        break
                if len(echelon) == columns:
                    break
            tested_pairs += 1
            nullity = columns - len(echelon)
            if nullity == 0:
                full_rank_pairs += 1
                continue
            if nullity != 1:
                continue
            denominator = nullspace_basis(echelon, columns)[0]
            if degree(denominator) != denominator_degree:
                continue
            if any(evaluate(denominator, point) == 0 for point in points):
                rejected_nonunit_pairs += 1
                continue
            leading_inverse = pow(denominator[-1], P - 2, P)
            denominator = [value * leading_inverse % P for value in denominator]
            numerators = []
            maximum_numerator_degree = -1
            for table in shifts:
                numerator = bytearray(len(points))
                for power, scalar in enumerate(denominator):
                    if scalar:
                        shifted = table[power]
                        for index, coefficient in enumerate(shifted):
                            numerator[index] = (numerator[index] + scalar * coefficient) % P
                this_degree = degree(numerator)
                if this_degree > numerator_bound:
                    raise RuntimeError((name, denominator_degree, this_degree, numerator_bound))
                maximum_numerator_degree = max(maximum_numerator_degree, this_degree)
                numerators.append(list(numerator[: this_degree + 1]))
            if denominator_degree + maximum_numerator_degree >= len(points):
                raise RuntimeError((name, "uniqueness inequality"))
            for v_degree, sample_values in enumerate(values_by_v_degree):
                numerator = numerators[v_degree]
                for point, expected in zip(points, sample_values, strict=True):
                    lhs = evaluate(numerator, point)
                    rhs = expected * evaluate(denominator, point) % P
                    if lhs != rhs:
                        raise RuntimeError((name, v_degree, point, lhs, rhs))
            chosen = {
                "denominator": denominator,
                "denominator_degree": denominator_degree,
                "numerators_by_v_degree": numerators,
                "maximum_numerator_degree": maximum_numerator_degree,
                "degree_sum": denominator_degree + maximum_numerator_degree,
                "searched_total_bound": total_bound,
                "unique_from_123_samples": True,
                "denominator_values": {str(point): evaluate(denominator, point) for point in points},
            }
            break
        if chosen is not None:
            break
    if chosen is None:
        return {
            "status": "NO_UNIQUE_RECONSTRUCTION",
            "coordinate": name,
            "maximum_denominator_degree": maximum_denominator_degree,
            "tested_pairs": tested_pairs,
            "full_rank_pairs": full_rank_pairs,
            "rejected_nonunit_pairs": rejected_nonunit_pairs,
        }
    roots = {}
    for root in range(P):
        if evaluate(chosen["denominator"], root) == 0:
            roots[str(root)] = True
    chosen.update(
        {
            "status": (
                "PASS"
                if chosen["degree_sum"] < len(points) - 1
                else "ALIAS_CEILING"
            ),
            "coordinate": name,
            "denominator_linear_roots": roots,
            "tested_pairs": tested_pairs,
            "full_rank_pairs": full_rank_pairs,
            "rejected_nonunit_pairs": rejected_nonunit_pairs,
        }
    )
    return chosen


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=Path, required=True)
    parser.add_argument("--coordinate", choices=COORDINATES, required=True)
    parser.add_argument("--maximum-denominator-degree", type=int, default=122)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not 0 <= args.maximum_denominator_degree <= 122:
        raise RuntimeError("maximum denominator degree")
    samples_hash = sha256(args.samples.read_bytes()).hexdigest()
    if samples_hash != EXPECTED_SAMPLES_SHA256:
        raise RuntimeError(("sample hash", samples_hash, EXPECTED_SAMPLES_SHA256))
    payload = json.loads(args.samples.read_text())
    if payload["status"] != "PASS" or payload["prime"] != P:
        raise RuntimeError("sample endpoint")
    points = payload["w_values"]
    if len(points) != 123 or len(set(points)) != 123:
        raise RuntimeError("sample points")
    values = payload["samples"][args.coordinate]
    if len(values) != 190 or any(len(row) != 123 for row in values):
        raise RuntimeError("sample matrix")
    modulus = modulus_for_points(points)
    basis = lagrange_basis(points, modulus)
    result = reconstruct_coordinate(
        args.coordinate,
        values,
        points,
        modulus,
        basis,
        args.maximum_denominator_degree,
    )
    result.update(
        {
            "prime": P,
            "samples_sha256": EXPECTED_SAMPLES_SHA256,
            "point_count": len(points),
            "interpolation_modulus": modulus,
            "scope": "simultaneous common-denominator reconstruction on 123 exact fibres only",
        }
    )
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("Q8-P127-SIMULTANEOUS-COORDINATE-RECONSTRUCTION")
    print(f"coordinate={args.coordinate}")
    print(f"status={result['status']}")
    if result["status"] in ("PASS", "ALIAS_CEILING"):
        print(f"denominator_degree={result['denominator_degree']}")
        print(f"maximum_numerator_degree={result['maximum_numerator_degree']}")
        print(f"degree_sum={result['degree_sum']}")
        print(f"denominator_linear_roots={result['denominator_linear_roots']}")
    print(f"output_sha256={sha256(args.output.read_bytes()).hexdigest()}")


if __name__ == "__main__":
    main()
