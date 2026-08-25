#!/usr/bin/env python3
"""Reconstruct common-denominator coordinate formulas from 123 shape fibres."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path


P = 127
EXPECTED_SAMPLES_SHA256 = "0790e9f8bb6b545e742ca9e723c29b9a8dc0268a93dedd91c2f2a7b48f48f231"


def trim(a: list[int]) -> list[int]:
    while a and a[-1] % P == 0:
        a.pop()
    return [x % P for x in a]


def degree(a: list[int]) -> int:
    return len(trim(a[:])) - 1


def add(a: list[int], b: list[int]) -> list[int]:
    out = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] = (out[i] + x) % P
    for i, x in enumerate(b):
        out[i] = (out[i] + x) % P
    return trim(out)


def sub(a: list[int], b: list[int]) -> list[int]:
    out = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] = (out[i] + x) % P
    for i, x in enumerate(b):
        out[i] = (out[i] - x) % P
    return trim(out)


def scale(a: list[int], scalar: int) -> list[int]:
    return trim([(scalar * x) % P for x in a])


def mul(a: list[int], b: list[int]) -> list[int]:
    if not a or not b:
        return []
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] = (out[i + j] + x * y) % P
    return trim(out)


def divmod_poly(a: list[int], b: list[int]) -> tuple[list[int], list[int]]:
    a = trim(a[:])
    b = trim(b[:])
    if not b:
        raise ZeroDivisionError
    if len(a) < len(b):
        return [], a
    quotient = [0] * (len(a) - len(b) + 1)
    inverse = pow(b[-1], P - 2, P)
    while len(a) >= len(b):
        shift = len(a) - len(b)
        coefficient = a[-1] * inverse % P
        quotient[shift] = coefficient
        if coefficient:
            for j, value in enumerate(b):
                a[shift + j] = (a[shift + j] - coefficient * value) % P
        trim(a)
    return trim(quotient), a


def mod_poly(a: list[int], modulus: list[int]) -> list[int]:
    return divmod_poly(a, modulus)[1]


def gcd_poly(a: list[int], b: list[int]) -> list[int]:
    a, b = trim(a[:]), trim(b[:])
    while b:
        _, remainder = divmod_poly(a, b)
        a, b = b, remainder
    if not a:
        return []
    return scale(a, pow(a[-1], P - 2, P))


def lcm_poly(a: list[int], b: list[int]) -> list[int]:
    if not a or not b:
        return []
    common = gcd_poly(a, b)
    quotient, remainder = divmod_poly(a, common)
    if remainder:
        raise RuntimeError("nonexact lcm division")
    out = mul(quotient, b)
    return scale(out, pow(out[-1], P - 2, P))


def evaluate(a: list[int], x: int) -> int:
    result = 0
    for coefficient in reversed(a):
        result = (result * x + coefficient) % P
    return result


def derivative(a: list[int]) -> list[int]:
    return trim([(i * a[i]) % P for i in range(1, len(a))])


def product_tree_linear(points: list[int]) -> list[int]:
    result = [1]
    for point in points:
        result = mul(result, [(-point) % P, 1])
    return result


def lagrange_basis(points: list[int], modulus: list[int]) -> list[list[int]]:
    derivative_modulus = derivative(modulus)
    basis = []
    for point in points:
        quotient, remainder = divmod_poly(modulus, [(-point) % P, 1])
        if remainder:
            raise RuntimeError(("linear division", point, remainder))
        denominator = evaluate(derivative_modulus, point)
        if denominator == 0:
            raise RuntimeError(("repeated point", point))
        basis.append(scale(quotient, pow(denominator, P - 2, P)))
    return basis


def interpolate(values: list[int], basis: list[list[int]]) -> list[int]:
    result: list[int] = []
    for value, polynomial in zip(values, basis, strict=True):
        if value:
            result = add(result, scale(polynomial, value))
    return result


def normalize_fraction(numerator: list[int], denominator: list[int]) -> tuple[list[int], list[int]]:
    common = gcd_poly(numerator, denominator)
    if common and degree(common) > 0:
        numerator, rem1 = divmod_poly(numerator, common)
        denominator, rem2 = divmod_poly(denominator, common)
        if rem1 or rem2:
            raise RuntimeError("fraction gcd division")
    if not denominator:
        raise RuntimeError("zero denominator")
    inverse = pow(denominator[-1], P - 2, P)
    return scale(numerator, inverse), scale(denominator, inverse)


def rational_candidate(interpolant: list[int], modulus: list[int], points: list[int]) -> tuple[list[int], list[int]]:
    # Extended-Euclidean convergents include every sharply lower-degree Pade
    # candidate needed here.  The original interpolation polynomial Q=1 is
    # retained as a fail-closed fallback.
    candidates = [(interpolant, [1])]
    r0, r1 = modulus[:], interpolant[:]
    t0, t1 = [], [1]
    while r1:
        if all(evaluate(t1, point) != 0 for point in points):
            candidates.append((r1[:], t1[:]))
        quotient, r2 = divmod_poly(r0, r1)
        t2 = sub(t0, mul(quotient, t1))
        r0, r1, t0, t1 = r1, r2, t1, t2
    valid = []
    for numerator, denominator in candidates:
        if degree(numerator) + degree(denominator) >= len(points):
            continue
        if mod_poly(sub(numerator, mul(denominator, interpolant)), modulus):
            # Only congruence-verified pairs are admissible.  Some normalized
            # Euclidean intermediates need not survive cancellation as
            # polynomial congruences, so they are discarded fail-closed.
            continue
        valid.append((numerator, denominator))
    if not valid:
        return normalize_fraction(interpolant, [1])
    numerator, denominator = min(
        valid,
        key=lambda pair: (
            degree(pair[0]) + degree(pair[1]),
            max(degree(pair[0]), degree(pair[1])),
            degree(pair[1]),
        ),
    )
    # Cancel only the single selected convergent.  If cancellation exposes a
    # representation bug, retain the raw congruence-verified pair rather than
    # silently accept it.
    reduced_numerator, reduced_denominator = normalize_fraction(numerator, denominator)
    if not mod_poly(
        sub(reduced_numerator, mul(reduced_denominator, interpolant)), modulus
    ):
        return reduced_numerator, reduced_denominator
    inverse = pow(denominator[-1], P - 2, P)
    return scale(numerator, inverse), scale(denominator, inverse)


def linear_root_inventory(polynomial: list[int]) -> tuple[dict[str, int], list[int]]:
    residual = polynomial[:]
    roots = {}
    for root in range(P):
        multiplicity = 0
        factor = [(-root) % P, 1]
        while residual and evaluate(residual, root) == 0:
            quotient, remainder = divmod_poly(residual, factor)
            if remainder:
                raise RuntimeError("root division")
            residual = quotient
            multiplicity += 1
        if multiplicity:
            roots[str(root)] = multiplicity
    return roots, residual


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--coordinate", choices=("c", "d2", "d4", "x1", "x3", "x5", "inv")
    )
    args = parser.parse_args()
    samples_hash = sha256(args.samples.read_bytes()).hexdigest()
    if samples_hash != EXPECTED_SAMPLES_SHA256:
        raise RuntimeError(("sample hash", samples_hash, EXPECTED_SAMPLES_SHA256))
    payload = json.loads(args.samples.read_text())
    if payload["status"] != "PASS" or payload["prime"] != P:
        raise RuntimeError("sample endpoint")
    points = payload["w_values"]
    if len(points) != 123 or len(set(points)) != 123:
        raise RuntimeError("sample point count")
    modulus = product_tree_linear(points)
    if degree(modulus) != 123:
        raise RuntimeError("interpolation modulus")
    basis = lagrange_basis(points, modulus)

    output_coordinates = {}
    all_denominator = [1]
    selected_names = (
        [args.coordinate] if args.coordinate is not None else payload["coordinate_names"]
    )
    for name in selected_names:
        interpolants = []
        individual = []
        common_denominator = [1]
        for values in payload["samples"][name]:
            interpolant = interpolate(values, basis)
            interpolants.append(interpolant)
            numerator, denominator = rational_candidate(interpolant, modulus, points)
            individual.append((numerator, denominator))
            common_denominator = lcm_poly(common_denominator, denominator)
        numerators = []
        maximum_numerator_degree = -1
        for interpolant in interpolants:
            numerator = mod_poly(mul(common_denominator, interpolant), modulus)
            numerators.append(numerator)
            maximum_numerator_degree = max(maximum_numerator_degree, degree(numerator))
        unique = degree(common_denominator) + maximum_numerator_degree < len(points)
        for v_degree, values in enumerate(payload["samples"][name]):
            for point, value in zip(points, values, strict=True):
                lhs = evaluate(numerators[v_degree], point)
                rhs = value * evaluate(common_denominator, point) % P
                if lhs != rhs:
                    raise RuntimeError(("sample reconstruction", name, v_degree, point))
        roots, residual = linear_root_inventory(common_denominator)
        output_coordinates[name] = {
            "denominator": common_denominator,
            "denominator_degree": degree(common_denominator),
            "denominator_linear_roots": roots,
            "denominator_root_free_residual": residual,
            "denominator_root_free_residual_degree": degree(residual),
            "maximum_numerator_degree": maximum_numerator_degree,
            "degree_sum": degree(common_denominator) + maximum_numerator_degree,
            "unique_from_123_samples": unique,
            "numerators_by_v_degree": numerators,
            "individual_degree_pairs": [
                [degree(numerator), degree(denominator)] for numerator, denominator in individual
            ],
        }
        all_denominator = lcm_poly(all_denominator, common_denominator)
    all_roots, all_residual = linear_root_inventory(all_denominator)
    result = {
        "status": "PASS",
        "scope": "rational reconstruction from 123 exact shape fibres",
        "prime": P,
        "samples_sha256": EXPECTED_SAMPLES_SHA256,
        "point_count": len(points),
        "selected_coordinates": selected_names,
        "interpolation_modulus": modulus,
        "coordinates": output_coordinates,
        "all_coordinate_denominator": all_denominator,
        "all_coordinate_denominator_degree": degree(all_denominator),
        "all_coordinate_denominator_linear_roots": all_roots,
        "all_coordinate_denominator_root_free_residual": all_residual,
        "all_coordinate_denominator_root_free_residual_degree": degree(all_residual),
        "all_coordinates_unique": all(
            item["unique_from_123_samples"] for item in output_coordinates.values()
        ),
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("Q8-P127-RATIONAL-COORDINATE-RECONSTRUCTION")
    print("status=PASS")
    for name, item in output_coordinates.items():
        print(
            f"{name}: numerator_degree_max={item['maximum_numerator_degree']} "
            f"denominator_degree={item['denominator_degree']} "
            f"sum={item['degree_sum']} unique={int(item['unique_from_123_samples'])} "
            f"linear_roots={item['denominator_linear_roots']} "
            f"residual_degree={item['denominator_root_free_residual_degree']}"
        )
    print(
        f"all_denominator_degree={result['all_coordinate_denominator_degree']} "
        f"linear_roots={all_roots} residual_degree={degree(all_residual)}"
    )
    print(f"all_coordinates_unique={int(result['all_coordinates_unique'])}")
    print(f"output_sha256={sha256(args.output.read_bytes()).hexdigest()}")


if __name__ == "__main__":
    main()
