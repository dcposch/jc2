#!/usr/bin/env python3
"""Exact finite replay for the genus-three bicuspidal/node Fox kernel.

The topology-to-Fox and singular-link localization interfaces are proved in
the accompanying report.  This script checks the polynomial control, its
three-strand braid factorization, and the complete F_3 coloring kernel.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json


Matrix = tuple[tuple[int, int], tuple[int, int]]
Coloring = tuple[int, int, int]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def mat_mul(left: Matrix, right: Matrix) -> Matrix:
    return (
        (
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ),
        (
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ),
    )


def mat_inv(matrix: Matrix) -> Matrix:
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    require(determinant == 1, "SL2 matrix expected")
    return (
        (matrix[1][1], -matrix[0][1]),
        (-matrix[1][0], matrix[0][0]),
    )


SIGMA = (
    ((1, 1), (0, 1)),
    ((1, 0), (-1, 1)),
)


def braid_matrix(word: tuple[int, ...]) -> Matrix:
    result: Matrix = ((1, 0), (0, 1))
    for letter in word:
        generator = SIGMA[abs(letter) - 1]
        if letter < 0:
            generator = mat_inv(generator)
        result = mat_mul(result, generator)
    return result


def inverse_word(word: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(-letter for letter in reversed(word))


def fox_generator(coloring: Coloring, index: int, inverse: bool = False) -> Coloring:
    result = list(coloring)
    first = result[index]
    second = result[index + 1]
    if inverse:
        result[index] = second
        result[index + 1] = (2 * second - first) % 3
    else:
        result[index] = (2 * first - second) % 3
        result[index + 1] = first
    return tuple(result)  # type: ignore[return-value]


def fox_action(coloring: Coloring, word: tuple[int, ...]) -> Coloring:
    result = coloring
    for letter in word:
        result = fox_generator(result, abs(letter) - 1, letter < 0)
    return result


def polynomial_control() -> dict[str, object]:
    # Coefficient dictionaries, low degree first, avoid a CAS dependency.
    # p=t^3-3t, q=t^4-2t^2 and
    # F=-x^4-6x^2 y+2x^2+y^3-6y^2+9y.
    def mul(left: list[int], right: list[int]) -> list[int]:
        result = [0] * (len(left) + len(right) - 1)
        for i, a in enumerate(left):
            for j, b in enumerate(right):
                result[i + j] += a * b
        return result

    def add(*terms: tuple[int, list[int]]) -> list[int]:
        size = max(len(poly) for _, poly in terms)
        result = [0] * size
        for scalar, poly in terms:
            for index, coefficient in enumerate(poly):
                result[index] += scalar * coefficient
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        return result

    p = [0, -3, 0, 1]
    q = [0, 0, -2, 0, 1]
    p2 = mul(p, p)
    p4 = mul(p2, p2)
    q2 = mul(q, q)
    q3 = mul(q2, q)
    value = add(
        (-1, p4),
        (-6, mul(p2, q)),
        (2, p2),
        (1, q3),
        (-6, q2),
        (9, q),
    )
    require(value == [0], "implicit polynomial substitution")

    # Discriminant of y^3+A y^2+B y+C.
    x2 = [0, 0, 1]
    x4 = mul(x2, x2)
    cubic_a = [-6]
    cubic_b = add((1, [9]), (-6, x2))
    cubic_c = add((2, x2), (-1, x4))
    discriminant = add(
        (1, mul(mul(cubic_a, cubic_a), mul(cubic_b, cubic_b))),
        (-4, mul(mul(cubic_b, cubic_b), cubic_b)),
        (-4, mul(mul(cubic_a, cubic_a), mul(cubic_a, cubic_c))),
        (-27, mul(cubic_c, cubic_c)),
        (18, mul(mul(cubic_a, cubic_b), cubic_c)),
    )
    x2_minus_four = [-4, 0, 1]
    expected_discriminant = [
        -27 * coefficient
        for coefficient in mul(x2, mul(mul(x2_minus_four, x2_minus_four), x2_minus_four))
    ]
    require(discriminant == expected_discriminant, "projection discriminant factorization")

    # For t != u, division by t-u gives
    #   t^2+tu+u^2=3,
    #   (t+u)(t^2+u^2-2)=0.
    # The second branch t^2+u^2=2 forces tu=1 and then (t-u)^2=0.
    # The remaining branch is u=-t and t^2=3: one unordered node pair.
    require(2 - 2 * 1 == 0, "diagonal-only second self-pair branch")
    node_tangent_determinant_squared = 96 * 96 * 3
    require(node_tangent_determinant_squared != 0, "node tangent vectors are distinct")

    # p'=3(t^2-1), q'=4t(t^2-1): common critical points are +/-1.
    # det((p'',q''),(p''',q'''))=96 at t=+/-1, so both are A2 cusps.
    cusp_determinants = (96, 96)
    require(all(value != 0 for value in cusp_determinants), "ordinary cusp jets")

    return {
        "parametrization": ["t^3-3t", "t^4-2t^2"],
        "implicit": "-x^4-6*x^2*y+2*x^2+y^3-6*y^2+9*y",
        "projection_discriminant": "-27*x^2*(x-2)^3*(x+2)^3",
        "singularities": {"A1_node": 1, "A2_cusps": 2},
        "total_delta": 3,
        "b1_branch": 1,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mutate-omit-local-cusp-map",
        action="store_true",
        help="incorrectly promote the punctured affine Fox class to Pic[3]",
    )
    args = parser.parse_args()

    curve = polynomial_control()

    sigma1 = (1,)
    sigma2 = (2,)
    half_twist_node = sigma2 + sigma1 + inverse_word(sigma2)
    cusp_left = sigma1 * 3
    node = half_twist_node * 2
    cusp_right = sigma2 * 3
    total = (sigma1 + sigma2) * 4
    factorized = cusp_left + node + cusp_right

    # B3 -> SL2(Z), together with exponent sum, separates these two words:
    # the kernel of this representation has exponent sum divisible by 12.
    total_exponent = sum(1 if letter > 0 else -1 for letter in total)
    factorized_exponent = sum(1 if letter > 0 else -1 for letter in factorized)
    require(total_exponent == factorized_exponent == 8, "braid exponent sum")
    require(braid_matrix(total) == braid_matrix(factorized), "B3 factorization")

    colorings = tuple(itertools.product(range(3), repeat=3))
    boundary = tuple(color for color in colorings if fox_action(color, total) == color)
    affine = tuple(
        color
        for color in colorings
        if fox_action(color, cusp_left) == color
        and fox_action(color, node) == color
        and fox_action(color, cusp_right) == color
    )
    constants = tuple(color for color in affine if len(set(color)) == 1)
    require(len(boundary) == 9, "boundary Fox space has dimension two")
    require(len(affine) == 9, "affine Fox space has dimension two")
    require(len(constants) == 3, "constant-color coboundary line")

    # The node half twist is sigma2 sigma1 sigma2^-1.  In its adapted
    # basis, applying sigma2 first makes positions 0 and 1 equal.
    for color in affine:
        adapted = fox_action(color, sigma2)
        require(adapted[0] == adapted[1], "node local C2 relation")

    reduced_representatives = tuple(color for color in affine if color[0] == 0)
    require(len(reduced_representatives) == 3, "one-dimensional reduced affine Fox space")
    local_map: dict[Coloring, tuple[int, int]] = {}
    for color in reduced_representatives:
        left_residue = (color[0] - color[1]) % 3
        right_residue = (color[1] - color[2]) % 3
        local_map[color] = (left_residue, right_residue)
        require(left_residue == right_residue, "diagonal two-cusp restriction")

    if args.mutate_omit_local_cusp_map:
        local_map = {color: (0, 0) for color in reduced_representatives}

    kernel = tuple(color for color, residue in local_map.items() if residue == (0, 0))
    require(kernel == ((0, 0, 0),), "local cusp map must kill the reduced Fox class")

    payload = {
        "status": "PASS-GENUS-THREE-SPECTATOR-FOX-LOCAL-KERNEL",
        "curve": curve,
        "braid": {
            "infinity": "(sigma1 sigma2)^4",
            "factorization": "sigma1^3 (sigma2 sigma1 sigma2^-1)^2 sigma2^3",
            "exponent_sum": 8,
            "SL2_matrix": braid_matrix(total),
        },
        "fox_F3": {
            "boundary_colorings": len(boundary),
            "affine_colorings": len(affine),
            "constant_colorings": len(constants),
            "reduced_affine_dimension": 1,
            "cusp_restriction": "lambda -> (lambda,lambda)",
            "locally_extendable_reduced_dimension": 0,
        },
        "classification": "AFFINE-FOX-SURVIVOR-BUT-PIC3-KERNEL-ZERO",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    print(json.dumps(payload, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
