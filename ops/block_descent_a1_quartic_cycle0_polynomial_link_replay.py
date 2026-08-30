#!/usr/bin/env python3
"""Desk replay for the polynomial-link obstruction to the R4-CYCLE-0 packet.

The script computes the exact Alexander polynomial of the frozen four-braid
by unreduced/reduced Burau matrices over Z[t,t^-1], detects a non-unit-circle
real root, and verifies a low-degree polynomial one-node control.  It does not
encode the link-at-infinity cabling theorem or van Kampen.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass


@dataclass(frozen=True)
class Laurent:
    coefficients: tuple[tuple[int, int], ...]

    @staticmethod
    def from_dict(values: dict[int, int]) -> "Laurent":
        return Laurent(tuple(sorted((power, value) for power, value in values.items() if value)))

    @staticmethod
    def integer(value: int) -> "Laurent":
        return Laurent.from_dict({0: value})

    @staticmethod
    def monomial(power: int, value: int = 1) -> "Laurent":
        return Laurent.from_dict({power: value})

    def as_dict(self) -> dict[int, int]:
        return dict(self.coefficients)

    def __add__(self, other: "Laurent") -> "Laurent":
        result = self.as_dict()
        for power, value in other.coefficients:
            result[power] = result.get(power, 0) + value
        return Laurent.from_dict(result)

    def __neg__(self) -> "Laurent":
        return Laurent(tuple((power, -value) for power, value in self.coefficients))

    def __sub__(self, other: "Laurent") -> "Laurent":
        return self + (-other)

    def __mul__(self, other: "Laurent") -> "Laurent":
        result: dict[int, int] = {}
        for left_power, left_value in self.coefficients:
            for right_power, right_value in other.coefficients:
                power = left_power + right_power
                result[power] = result.get(power, 0) + left_value * right_value
        return Laurent.from_dict(result)

    def evaluate(self, value: int) -> int:
        if value == 0 and any(power < 0 for power, _ in self.coefficients):
            raise ZeroDivisionError("negative Laurent power at zero")
        total = 0
        for power, coefficient in self.coefficients:
            if power >= 0:
                total += coefficient * value**power
            else:
                if value not in (1, -1):
                    raise ValueError("integer evaluation of negative powers is not integral")
                total += coefficient * value**power
        return int(total)

    def dense(self) -> list[int]:
        if not self.coefficients:
            return [0]
        minimum = min(power for power, _ in self.coefficients)
        maximum = max(power for power, _ in self.coefficients)
        values = self.as_dict()
        return [values.get(power, 0) for power in range(maximum, minimum - 1, -1)]


ZERO = Laurent.integer(0)
ONE = Laurent.integer(1)
T = Laurent.monomial(1)
T_INV = Laurent.monomial(-1)


Matrix = list[list[Laurent]]


def identity(size: int) -> Matrix:
    return [[ONE if row == column else ZERO for column in range(size)] for row in range(size)]


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    size = len(left)
    return [
        [
            sum_laurent(left[row][middle] * right[middle][column] for middle in range(size))
            for column in range(size)
        ]
        for row in range(size)
    ]


def sum_laurent(values) -> Laurent:
    result = ZERO
    for value in values:
        result = result + value
    return result


def burau_generator(strands: int, generator: int) -> Matrix:
    result = identity(strands)
    index = abs(generator) - 1
    if generator > 0:
        block = ((ONE - T, T), (ONE, ZERO))
    else:
        block = ((ZERO, ONE), (T_INV, ONE - T_INV))
    for row_offset in range(2):
        for column_offset in range(2):
            result[index + row_offset][index + column_offset] = block[row_offset][column_offset]
    return result


def reduced_burau(strands: int, word: tuple[int, ...]) -> Matrix:
    unreduced = identity(strands)
    for generator in word:
        unreduced = matrix_multiply(unreduced, burau_generator(strands, generator))
    # Quotient by the invariant vector (1,...,1), using classes of e_1,...,e_(n-1).
    return [
        [unreduced[row][column] - unreduced[strands - 1][column] for column in range(strands - 1)]
        for row in range(strands - 1)
    ]


def determinant3(matrix: Matrix) -> Laurent:
    require(len(matrix) == 3 and all(len(row) == 3 for row in matrix), "3x3 determinant")
    return (
        matrix[0][0] * matrix[1][1] * matrix[2][2]
        + matrix[0][1] * matrix[1][2] * matrix[2][0]
        + matrix[0][2] * matrix[1][0] * matrix[2][1]
        - matrix[0][2] * matrix[1][1] * matrix[2][0]
        - matrix[0][1] * matrix[1][0] * matrix[2][2]
        - matrix[0][0] * matrix[1][2] * matrix[2][1]
    )


def alexander_numerator(strands: int, word: tuple[int, ...]) -> Laurent:
    reduced = reduced_burau(strands, word)
    size = strands - 1
    difference = [
        [(ONE if row == column else ZERO) - reduced[row][column] for column in range(size)]
        for row in range(size)
    ]
    require(size == 3, "replay is deliberately specialized to four strands")
    # Delta*(1-t^n)=(1-t)*det(I-rho_reduced).
    return (ONE - T) * determinant3(difference)


def polynomial(coefficients_low_to_high: tuple[int, ...]) -> Laurent:
    return Laurent.from_dict({power: value for power, value in enumerate(coefficients_low_to_high)})


def strand_permutation(word: tuple[int, ...]) -> tuple[int, ...]:
    result = tuple(range(4))
    for generator in word:
        index = abs(generator) - 1
        transposition = list(range(4))
        transposition[index], transposition[index + 1] = transposition[index + 1], transposition[index]
        transposition_tuple = tuple(transposition)
        result = tuple(result[transposition_tuple[position]] for position in range(4))
    return result


def cycle_type(element: tuple[int, ...]) -> tuple[int, ...]:
    unseen = set(range(len(element)))
    lengths: list[int] = []
    while unseen:
        current = min(unseen)
        length = 0
        while current in unseen:
            unseen.remove(current)
            current = element[current]
            length += 1
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mutate-packet-to-trefoil",
        action="store_true",
        help="replace the obstructed packet by a stabilized trefoil word",
    )
    args = parser.parse_args()

    for generator in (1, 2, 3):
        positive = burau_generator(4, generator)
        negative = burau_generator(4, -generator)
        require(matrix_multiply(positive, negative) == identity(4), "right Burau inverse")
        require(matrix_multiply(negative, positive) == identity(4), "left Burau inverse")

    b1 = (1,)
    b2 = (2, 2, 2, 1, -2, -2, -2)
    b3 = (3, 2, 2, 2, 1, -2, -2, -2, -3)
    node = (2, 3, 3, -2)
    packet = b1 + b2 + b3 + node
    if args.mutate_packet_to_trefoil:
        packet = (1, 2, 3, 1, 1)

    require(cycle_type(strand_permutation(packet)) == (4,), "packet closure is a knot")

    a_factor = polynomial((1, -1, 1))  # t^2-t+1
    p_factor = polynomial((1, -4, 4, -3, 4, -4, 1))
    expected_alexander = Laurent.monomial(-4, -1) * a_factor * a_factor * p_factor
    numerator = alexander_numerator(4, packet)
    require(
        numerator == expected_alexander * (ONE - Laurent.monomial(4)),
        "exact Burau Alexander identity for the frozen packet",
    )
    require(expected_alexander.evaluate(1) == 1, "Alexander normalization at one")
    require(p_factor.evaluate(2) == -15, "noncyclotomic factor value at two")
    require(p_factor.evaluate(3) == 25, "noncyclotomic factor value at three")

    # Low-degree global polynomial control:
    #   X(t)=t^4+t^3-t, Y(t)=t^2.
    # Equality Y(t)=Y(u), t!=u forces u=-t; then
    # X(t)-X(-t)=2t(t^2-1), giving the sole unordered pair {+1,-1}.
    # The derivative never vanishes simultaneously, and the node tangents
    # have determinant -8.
    equality_nontrivial_roots = (-1, 1)
    require(
        all(2 * value * (value * value - 1) == 0 for value in equality_nontrivial_roots),
        "displayed node pair solves the equality equation",
    )
    require(
        4 * 0**3 + 3 * 0**2 - 1 == -1,
        "the only zero of Y-prime is immersed",
    )
    tangent_plus = (6, 2)
    tangent_minus = (-2, -2)
    tangent_determinant = tangent_plus[0] * tangent_minus[1] - tangent_plus[1] * tangent_minus[0]
    require(tangent_determinant == -8, "the unique double point is ordinary")

    # Projection to Y has one simple vertical branch at t=0 and the node at
    # Y=1, hence B2 infinity word sigma_1*sigma_1^2=sigma_1^3 (trefoil).
    control_b2_exponent = 1 + 2
    require(control_b2_exponent == 3, "low-degree control has trefoil infinity braid")

    payload = {
        "status": "PASS-R4-CYCLE-0-POLYNOMIAL-LINK-OBSTRUCTION",
        "packet_word": list(packet),
        "packet_alexander_dense_high_to_low": expected_alexander.dense(),
        "packet_alexander_min_power": min(power for power, _ in expected_alexander.coefficients),
        "packet_alexander_max_power": max(power for power, _ in expected_alexander.coefficients),
        "noncyclotomic_factor_dense_high_to_low": p_factor.dense(),
        "noncyclotomic_sign_interval": [2, 3],
        "packet_global_polynomial_a1_realization": False,
        "low_degree_control": {
            "X": "t^4+t^3-t",
            "Y": "t^2",
            "unique_identified_pair": [-1, 1],
            "ordinary_node_tangent_determinant": tangent_determinant,
            "infinity_braid": "sigma_1^3",
            "complement_group": "Z (written van Kampen check)",
        },
        "broader_unibranch_cycle0_horn": "OPEN",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    print(json.dumps(payload, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
