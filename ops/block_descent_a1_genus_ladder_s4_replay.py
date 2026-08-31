#!/usr/bin/env python3
"""Exact replay for the conductor-10/16 one-place S4 genus-ladder gate.

The written artifact supplies the one-place-at-infinity and knot-group
interfaces.  This script independently implements the recursive fixed-genus
delta-sequence construction of Assi--Garcia-Sanchez, checks it against their
published conductor-14 example and the campaign conductor-6/8 rows, validates
the satellite braid convention by exact Alexander polynomials, and counts all
meridian-transposition colorings with full image S4.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
import functools
import hashlib
import itertools
import json
import math


Permutation = tuple[int, ...]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def compose(left: Permutation, right: Permutation) -> Permutation:
    return tuple(left[right[index]] for index in range(len(left)))


def inverse(permutation: Permutation) -> Permutation:
    result = [0] * len(permutation)
    for index, image in enumerate(permutation):
        result[image] = index
    return tuple(result)


def conjugate(left: Permutation, right: Permutation) -> Permutation:
    return compose(compose(left, right), inverse(left))


def transposition(first: int, second: int, degree: int = 4) -> Permutation:
    result = list(range(degree))
    result[first], result[second] = result[second], result[first]
    return tuple(result)


TRANSPOSITIONS = tuple(
    transposition(first, second)
    for first in range(4)
    for second in range(first + 1, 4)
)


def generated_subgroup(generators: tuple[Permutation, ...]) -> frozenset[Permutation]:
    unit = tuple(range(len(generators[0])))
    subgroup = {unit}
    frontier = [unit]
    while frontier:
        current = frontier.pop()
        for generator in generators:
            candidate = compose(current, generator)
            if candidate not in subgroup:
                subgroup.add(candidate)
                frontier.append(candidate)
    return frozenset(subgroup)


def artin_generator(
    colors: tuple[Permutation, ...], generator: int
) -> tuple[Permutation, ...]:
    index = abs(generator) - 1
    result = list(colors)
    first = result[index]
    second = result[index + 1]
    if generator > 0:
        result[index] = conjugate(first, second)
        result[index + 1] = first
    else:
        result[index] = second
        result[index + 1] = conjugate(inverse(second), first)
    return tuple(result)


def braid_action(
    colors: tuple[Permutation, ...], word: tuple[int, ...]
) -> tuple[Permutation, ...]:
    result = colors
    for generator in word:
        result = artin_generator(result, generator)
    return result


def inverse_word(word: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(-generator for generator in reversed(word))


def signed_power(word: tuple[int, ...], exponent: int) -> tuple[int, ...]:
    return (word if exponent >= 0 else inverse_word(word)) * abs(exponent)


def block_switch_word(winding: int) -> tuple[int, ...]:
    """Positive permutation braid interchanging two winding-sized blocks."""

    labels = list(range(2 * winding))
    target = list(range(winding, 2 * winding)) + list(range(winding))
    rank = {label: index for index, label in enumerate(target)}
    word: list[int] = []
    while labels != target:
        for index in range(2 * winding - 1):
            if rank[labels[index]] > rank[labels[index + 1]]:
                labels[index], labels[index + 1] = labels[index + 1], labels[index]
                word.append(index + 1)
    return tuple(word)


def two_cable_of_two_braid_word(
    companion_exponent: int, meridional: int
) -> tuple[int, ...]:
    """Zero-framed C_(2,meridional)(T(2,companion_exponent))."""

    require(companion_exponent % 2 != 0, "the two-braid companion closes to a knot")
    require(meridional % 2 != 0, "the winding-two cable closes to a knot")
    switch = block_switch_word(2)
    companion = signed_power(switch, companion_exponent)
    correction = meridional - 2 * companion_exponent
    return companion + signed_power((1,), correction)


def torus_two_word(exponent: int) -> tuple[int, ...]:
    require(exponent % 2 != 0, "T(2,q) is a knot")
    return signed_power((1,), exponent)


def strand_permutation(strands: int, word: tuple[int, ...]) -> Permutation:
    result = tuple(range(strands))
    for generator in word:
        index = abs(generator) - 1
        adjacent = list(range(strands))
        adjacent[index], adjacent[index + 1] = adjacent[index + 1], adjacent[index]
        result = compose(result, tuple(adjacent))
    return result


def cycle_lengths(permutation: Permutation) -> tuple[int, ...]:
    unseen = set(range(len(permutation)))
    result: list[int] = []
    while unseen:
        current = min(unseen)
        length = 0
        while current in unseen:
            unseen.remove(current)
            current = permutation[current]
            length += 1
        result.append(length)
    return tuple(sorted(result, reverse=True))


def full_s4_colorings(strands: int, word: tuple[int, ...]) -> int:
    # Simultaneous conjugation is transitive on the six possible first
    # transpositions.  Fixing (12) and multiplying by six is exact.
    fixed_first = 0
    for tail in itertools.product(TRANSPOSITIONS, repeat=strands - 1):
        colors = (TRANSPOSITIONS[0],) + tail
        if braid_action(colors, word) != colors:
            continue
        if len(generated_subgroup(colors)) == 24:
            fixed_first += 1
    return 6 * fixed_first


def action_order(strands: int, word: tuple[int, ...]) -> int:
    states = tuple(itertools.product(TRANSPOSITIONS, repeat=strands))
    state_index = {state: index for index, state in enumerate(states)}
    permutation = tuple(state_index[braid_action(state, word)] for state in states)
    unseen = set(range(len(states)))
    order = 1
    while unseen:
        current = min(unseen)
        length = 0
        while current in unseen:
            unseen.remove(current)
            current = permutation[current]
            length += 1
        order = math.lcm(order, length)
    return order


def semigroup_contains(generators: tuple[int, ...], value: int) -> bool:
    represented = {0}
    for current in range(value + 1):
        if current not in represented:
            continue
        for generator in generators:
            if current + generator <= value:
                represented.add(current + generator)
    return value in represented


def delta_gcds(sequence: tuple[int, ...]) -> tuple[int, ...]:
    result = [sequence[0]]
    for value in sequence[1:]:
        result.append(math.gcd(result[-1], value))
    return tuple(result)


def delta_sequence_conductor(sequence: tuple[int, ...]) -> int:
    gcds = delta_gcds(sequence)
    require(gcds[-1] == 1, "primitive delta sequence")
    return 1 - sequence[0] + sum(
        (gcds[index - 1] // gcds[index] - 1) * sequence[index]
        for index in range(1, len(sequence))
    )


def is_delta_sequence(
    sequence: tuple[int, ...], *, drop_freeness: bool, drop_ordering: bool
) -> bool:
    if len(sequence) < 2 or any(value <= 0 for value in sequence):
        return False
    gcds = delta_gcds(sequence)
    # This is the exact reduced delta-sequence condition in the primary
    # source: r0 > r1 > d2 > d3 > ... > d_(h+1)=1.
    if gcds[-1] != 1 or not (sequence[0] > sequence[1] > gcds[1]):
        return False
    if any(gcds[index - 1] <= gcds[index] for index in range(1, len(gcds))):
        return False
    for index in range(1, len(sequence)):
        quotient = gcds[index - 1] // gcds[index]
        if not drop_freeness and not semigroup_contains(
            sequence[:index], quotient * sequence[index]
        ):
            return False
    if not drop_ordering:
        for index in range(1, len(sequence) - 1):
            if sequence[index] * gcds[index - 1] <= sequence[index + 1] * gcds[index]:
                return False
    return True


@functools.lru_cache(maxsize=None)
def delta_sequences_with_conductor(
    conductor: int, drop_freeness: bool, drop_ordering: bool
) -> tuple[tuple[int, ...], ...]:
    """Recursive construction from Assi--Garcia-Sanchez, Section 5."""

    result: set[tuple[int, ...]] = set()
    # One-stage case: conductor=(r0-1)(r1-1).
    for divisor in range(1, math.isqrt(conductor) + 1):
        if conductor % divisor:
            continue
        for left, right in ((conductor // divisor, divisor), (divisor, conductor // divisor)):
            candidate = (left + 1, right + 1)
            if is_delta_sequence(
                candidate,
                drop_freeness=drop_freeness,
                drop_ordering=drop_ordering,
            ):
                result.add(candidate)

    # For h>1, C=d_h*C(prefix)+(d_h-1)(r_h-1), with
    # 2<=r_h<=C-2 and 2<=d_h<=C/(r_h-1)+1.
    for last in range(2, max(2, conductor - 1)):
        upper_gcd = conductor // (last - 1) + 1
        for last_gcd in range(2, upper_gcd + 1):
            if math.gcd(last_gcd, last) != 1:
                continue
            remainder = conductor - (last_gcd - 1) * (last - 1)
            if remainder <= 0 or remainder % last_gcd:
                continue
            prefix_conductor = remainder // last_gcd
            if not 0 < prefix_conductor < conductor:
                continue
            for prefix in delta_sequences_with_conductor(
                prefix_conductor, drop_freeness, drop_ordering
            ):
                candidate = tuple(last_gcd * value for value in prefix) + (last,)
                if not is_delta_sequence(
                    candidate,
                    drop_freeness=drop_freeness,
                    drop_ordering=drop_ordering,
                ):
                    continue
                if delta_sequence_conductor(candidate) == conductor:
                    result.add(candidate)
    return tuple(sorted(result))


@dataclass(frozen=True)
class Laurent:
    coefficients: tuple[tuple[int, Fraction], ...]

    @staticmethod
    def from_dict(values: dict[int, Fraction | int]) -> "Laurent":
        return Laurent(
            tuple(sorted((power, Fraction(value)) for power, value in values.items() if value))
        )

    @staticmethod
    def monomial(power: int, value: int = 1) -> "Laurent":
        return Laurent.from_dict({power: value})

    def as_dict(self) -> dict[int, Fraction]:
        return dict(self.coefficients)

    def __add__(self, other: "Laurent") -> "Laurent":
        values = self.as_dict()
        for power, value in other.coefficients:
            values[power] = values.get(power, Fraction(0)) + value
        return Laurent.from_dict(values)

    def __neg__(self) -> "Laurent":
        return Laurent(tuple((power, -value) for power, value in self.coefficients))

    def __sub__(self, other: "Laurent") -> "Laurent":
        return self + (-other)

    def __mul__(self, other: "Laurent") -> "Laurent":
        values: dict[int, Fraction] = {}
        for left_power, left_value in self.coefficients:
            for right_power, right_value in other.coefficients:
                power = left_power + right_power
                values[power] = values.get(power, Fraction(0)) + left_value * right_value
        return Laurent.from_dict(values)


ZERO = Laurent.from_dict({})
ONE = Laurent.monomial(0)
T = Laurent.monomial(1)
T_INV = Laurent.monomial(-1)
Matrix = list[list[Laurent]]


def sum_laurent(values) -> Laurent:
    result = ZERO
    for value in values:
        result = result + value
    return result


def identity(size: int) -> Matrix:
    return [[ONE if row == column else ZERO for column in range(size)] for row in range(size)]


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    size = len(left)
    return [
        [
            sum_laurent(
                left[row][middle] * right[middle][column] for middle in range(size)
            )
            for column in range(size)
        ]
        for row in range(size)
    ]


def burau_generator(strands: int, generator: int) -> Matrix:
    result = identity(strands)
    index = abs(generator) - 1
    block = (
        ((ONE - T, T), (ONE, ZERO))
        if generator > 0
        else ((ZERO, ONE), (T_INV, ONE - T_INV))
    )
    for row_offset in range(2):
        for column_offset in range(2):
            result[index + row_offset][index + column_offset] = block[row_offset][column_offset]
    return result


def reduced_burau(strands: int, word: tuple[int, ...]) -> Matrix:
    unreduced = identity(strands)
    for generator in word:
        unreduced = matrix_multiply(unreduced, burau_generator(strands, generator))
    return [
        [unreduced[row][column] - unreduced[strands - 1][column] for column in range(strands - 1)]
        for row in range(strands - 1)
    ]


def determinant(matrix: Matrix) -> Laurent:
    size = len(matrix)
    result = ZERO
    for permutation in itertools.permutations(range(size)):
        inversions = sum(
            permutation[left] > permutation[right]
            for left in range(size)
            for right in range(left + 1, size)
        )
        term = ONE
        for row, column in enumerate(permutation):
            term = term * matrix[row][column]
        result = result - term if inversions % 2 else result + term
    return result


def alexander_numerator(strands: int, word: tuple[int, ...]) -> Laurent:
    burau = reduced_burau(strands, word)
    difference = [
        [(ONE if row == column else ZERO) - burau[row][column] for column in range(strands - 1)]
        for row in range(strands - 1)
    ]
    return (ONE - T) * determinant(difference)


def unit_normalized(value: Laurent) -> tuple[Fraction, ...]:
    coefficients = value.as_dict()
    minimum = min(coefficients)
    maximum = max(coefficients)
    sign = 1 if coefficients[minimum] > 0 else -1
    return tuple(sign * coefficients.get(power, Fraction(0)) for power in range(minimum, maximum + 1))


def torus_two_alexander(exponent: int) -> Laurent:
    require(exponent > 0 and exponent % 2, "positive odd T(2,q) exponent")
    return Laurent.from_dict({power: 1 if power % 2 == 0 else -1 for power in range(exponent)})


def substitute_power(value: Laurent, exponent: int) -> Laurent:
    return Laurent.from_dict({exponent * power: coefficient for power, coefficient in value.coefficients})


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutate-drop-freeness", action="store_true")
    parser.add_argument("--mutate-drop-ordering", action="store_true")
    parser.add_argument("--mutate-promote-cable-coloring", action="store_true")
    arguments = parser.parse_args()

    expected_censuses = {
        6: ((4, 3), (6, 4, 3), (7, 2)),
        8: ((5, 3), (6, 4, 5), (9, 2), (9, 6, 2)),
        10: ((6, 4, 7), (11, 2)),
        # This ten-row list is printed in Example 18 of the primary source.
        14: (
            (6, 4, 11),
            (8, 3),
            (8, 6, 3),
            (9, 6, 5),
            (10, 4, 7),
            (12, 8, 3),
            (12, 8, 6, 3),
            (15, 2),
            (15, 6, 2),
            (15, 10, 2),
        ),
        16: ((10, 4, 9), (17, 2)),
    }
    censuses = {
        conductor: delta_sequences_with_conductor(
            conductor,
            arguments.mutate_drop_freeness,
            arguments.mutate_drop_ordering,
        )
        for conductor in expected_censuses
    }
    require(censuses == expected_censuses, "exact recursive delta-sequence censuses")

    # A two-meridian generating set can never generate transitive S4 from
    # transpositions: two edges do not connect four vertices.  The explicit
    # finite control checks the stronger order statement.
    require(
        max(
            len(generated_subgroup((first, second)))
            for first in TRANSPOSITIONS
            for second in TRANSPOSITIONS
        )
        == 6,
        "two transpositions generate a subgroup of order at most six",
    )

    torus_counts: dict[str, int] = {}
    for exponent in (11, -11, 17, -17):
        word = torus_two_word(exponent)
        require(cycle_lengths(strand_permutation(2, word)) == (2,), "T(2,q) braid is a knot")
        torus_counts[f"T(2,{exponent:+d})"] = full_s4_colorings(2, word)
    require(set(torus_counts.values()) == {0}, "conductor-10/16 torus rows have zero full-S4 colorings")

    cable_counts: dict[str, int] = {}
    for companion_absolute, meridional_absolute in ((3, 7), (5, 9)):
        expected_alexander = torus_two_alexander(meridional_absolute) * substitute_power(
            torus_two_alexander(companion_absolute), 2
        )
        expected_numerator = expected_alexander * (ONE - Laurent.monomial(4))
        for companion in (companion_absolute, -companion_absolute):
            for meridional in (meridional_absolute, -meridional_absolute):
                word = two_cable_of_two_braid_word(companion, meridional)
                require(
                    cycle_lengths(strand_permutation(4, word)) == (4,),
                    "winding-two satellite braid closes to a knot",
                )
                require(
                    unit_normalized(alexander_numerator(4, word))
                    == unit_normalized(expected_numerator),
                    "satellite braid has the cable Alexander polynomial",
                )
                key = f"C(2,{meridional:+d})(T(2,{companion:+d}))"
                cable_counts[key] = full_s4_colorings(4, word)
    if arguments.mutate_promote_cable_coloring:
        cable_counts["C(2,+7)(T(2,+3))"] = 72
    require(set(cable_counts.values()) == {0}, "all conductor-10/16 cable sign rows have zero full-S4 colorings")

    # The winding-two family admits a finite all-exponent theorem.  On all
    # 6^4 transposition states the block switch X has order 12 and sigma_1
    # has order 6.  Thus odd companion/cable exponents reduce exactly to the
    # following 6-by-3 residue table.
    switch = block_switch_word(2)
    delta = (1,)
    switch_order = action_order(4, switch)
    delta_order = action_order(4, delta)
    require((switch_order, delta_order) == (12, 6), "finite Hurwitz action orders")
    residue_table: dict[str, int] = {}
    for companion_mod_12 in (1, 3, 5, 7, 9, 11):
        for meridional_mod_6 in (1, 3, 5):
            correction_mod_6 = (meridional_mod_6 - 2 * companion_mod_12) % 6
            word = switch * companion_mod_12 + delta * correction_mod_6
            count = full_s4_colorings(4, word)
            expected = (
                72
                if companion_mod_12 % 3 == 0 and meridional_mod_6 % 3 == 0
                else 0
            )
            require(count == expected, "winding-two residue theorem")
            residue_table[f"n={companion_mod_12}:q={meridional_mod_6}"] = count

    payload = {
        "status": "PASS-A1-GENUS-LADDER-CONDUCTOR-10-16-S4-OBSTRUCTION",
        "delta_sequence_source_control": {
            "published_conductor_14_example_reproduced": True,
            "censuses": {
                str(conductor): [list(sequence) for sequence in sequences]
                for conductor, sequences in censuses.items()
            },
        },
        "conductor_10_rows": {
            "(11,2)": "T(2,11)",
            "(6,4,7)": "C(2,7)(T(2,3))",
        },
        "conductor_16_rows": {
            "(17,2)": "T(2,17)",
            "(10,4,9)": "C(2,9)(T(2,5))",
        },
        "torus_labeled_full_S4_colorings": torus_counts,
        "cable_labeled_full_S4_colorings": cable_counts,
        "two_transposition_maximum_generated_order": 6,
        "winding_two_family": {
            "braid": "X^n*sigma1^(q-2n), X=sigma2 sigma3 sigma1 sigma2",
            "X_action_order": switch_order,
            "sigma1_action_order": delta_order,
            "residue_table": residue_table,
            "full_S4_iff": "3 divides n and 3 divides q",
            "labeled_count_when_nonzero": 72,
        },
        "irreducible_one_place_A1_delta_aff_5_is_quartic_S4_boundary_compatible": False,
        "irreducible_one_place_A1_delta_aff_8_is_quartic_S4_boundary_compatible": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    print(json.dumps(payload, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
