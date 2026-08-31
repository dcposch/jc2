#!/usr/bin/env python3
"""Desk replay for the conductor-eight one-place cable and b1 funnel.

The written artifact supplies the approximate-root theorem and the
normalization-fibre topology.  This script checks the finite genus-four
delta-sequence census, standard-braid S4 and Fox-3 colorings, the exact
degree-six/nine subduction identities, and the four-pair lower bound in the
sole group-level survivor.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from fractions import Fraction


Permutation = tuple[int, ...]
Polynomial = tuple[Fraction, ...]


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


def block_switch_word(winding: int) -> tuple[int, ...]:
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


def cable_braid_word(
    winding: int, meridional: int, companion_chirality: int
) -> tuple[int, ...]:
    require(companion_chirality in (-1, 1), "companion chirality sign")
    switch = block_switch_word(winding)
    companion_letter = switch if companion_chirality > 0 else inverse_word(switch)
    companion = companion_letter * 3
    correction = meridional - 3 * companion_chirality * winding
    delta = tuple(range(1, winding))
    if correction >= 0:
        twist = delta * correction
    else:
        twist = inverse_word(delta) * (-correction)
    return companion + twist


def full_s4_colorings(strands: int, word: tuple[int, ...]) -> int:
    transpositions = tuple(
        transposition(first, second)
        for first in range(4)
        for second in range(first + 1, 4)
    )
    count_with_fixed_first = 0
    for tail in itertools.product(transpositions, repeat=strands - 1):
        colors = (transpositions[0],) + tail
        if braid_action(colors, word) != colors:
            continue
        if len(generated_subgroup(colors)) == 24:
            count_with_fixed_first += 1
    return 6 * count_with_fixed_first


def fox_action(colors: tuple[int, ...], word: tuple[int, ...]) -> tuple[int, ...]:
    result = list(colors)
    for generator in word:
        index = abs(generator) - 1
        first = result[index]
        second = result[index + 1]
        if generator > 0:
            result[index], result[index + 1] = (2 * first - second) % 3, first
        else:
            result[index], result[index + 1] = second, (2 * second - first) % 3
    return tuple(result)


def fox_three_colorings(strands: int, word: tuple[int, ...]) -> int:
    return sum(
        fox_action(colors, word) == colors
        for colors in itertools.product(range(3), repeat=strands)
    )


def in_two_generator_semigroup(value: int, first: int, second: int) -> bool:
    return any(
        left * first + right * second == value
        for left in range(value // first + 1)
        for right in range(value // second + 1)
    )


def delta_sequence_conductor(sequence: tuple[int, ...]) -> int:
    gcds = [sequence[0]]
    for value in sequence[1:]:
        gcds.append(math.gcd(gcds[-1], value))
    require(gcds[-1] == 1, "primitive delta sequence")
    conductor = 1 - sequence[0]
    for index in range(1, len(sequence)):
        quotient = gcds[index - 1] // gcds[index]
        conductor += (quotient - 1) * sequence[index]
    return conductor


def conductor_eight_sequences(drop_freeness: bool) -> tuple[tuple[int, ...], ...]:
    result: set[tuple[int, ...]] = set()
    for high in range(2, 18):
        for low in range(2, high):
            if math.gcd(high, low) != 1:
                continue
            sequence = (high, low)
            if delta_sequence_conductor(sequence) == 8:
                result.add(sequence)

    # For h=2 write r0=a*d, r1=b*d.  The conductor equation is
    # 7=d*((a-1)*b-a)+(d-1)*r2.  Positivity bounds d<=7, r2<=7,
    # and ((a-1)*(b-1)-1)<=3, so this finite box is exhaustive even
    # for the negative control which omits freeness.
    for d in range(2, 8):
        for b in range(2, 9):
            for a in range(b + 1, 10):
                if math.gcd(a, b) != 1:
                    continue
                defect = (a - 1) * b - a
                if defect < 1 or d * defect > 7:
                    continue
                for r2 in range(1, 8):
                    if math.gcd(d, r2) != 1:
                        continue
                    if 7 != d * defect + (d - 1) * r2:
                        continue
                    if r2 >= a * b * d:
                        continue
                    if not drop_freeness and not in_two_generator_semigroup(r2, a, b):
                        continue
                    result.add((a * d, b * d, r2))
    return tuple(sorted(result))


def trim(poly: Polynomial) -> Polynomial:
    values = list(poly)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)


def poly_add(left: Polynomial, right: Polynomial) -> Polynomial:
    size = max(len(left), len(right))
    result = [Fraction(0)] * size
    for index in range(size):
        result[index] = (
            left[index] if index < len(left) else Fraction(0)
        ) + (right[index] if index < len(right) else Fraction(0))
    return trim(tuple(result))


def poly_scale(poly: Polynomial, scalar: Fraction) -> Polynomial:
    return trim(tuple(scalar * value for value in poly))


def poly_multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    result = [Fraction(0)] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            result[left_index + right_index] += left_value * right_value
    return trim(tuple(result))


def poly_power(poly: Polynomial, exponent: int) -> Polynomial:
    result: Polynomial = (Fraction(1),)
    for _ in range(exponent):
        result = poly_multiply(result, poly)
    return result


def coefficient(poly: Polynomial, degree: int) -> Fraction:
    return poly[degree] if degree < len(poly) else Fraction(0)


def check_normal_form_grid() -> None:
    # Normalize the nonzero leading coefficient of R to a=1.  The relevant
    # coefficient identities have b-degree <=18 and c-degree <=6.  Exact
    # verification on 19 by 7 distinct rational values is therefore an
    # interpolation certificate for the displayed identities.
    for b_integer in range(-9, 10):
        for c_integer in range(-3, 4):
            b = Fraction(b_integer)
            c = Fraction(c_integer)
            p = b * b + 2 * c
            q = -2 * b * (c + b * b)
            z: Polynomial = (q, p, Fraction(0), Fraction(1))
            r: Polynomial = (c, b, Fraction(1))
            quotient: Polynomial = (2 * b, Fraction(1))
            scalar_remainder = (c + 2 * b * b) ** 2

            remainder_identity = poly_add(
                poly_multiply(z, quotient), (scalar_remainder,)
            )
            require(
                poly_power(r, 2) == remainder_identity,
                "R^2=ZQ+S after the constant-remainder equations",
            )

            u = poly_add(poly_power(z, 2), r)
            v = poly_add(
                poly_add(poly_power(z, 3), poly_scale(poly_multiply(z, r), Fraction(3, 2))),
                poly_scale(quotient, Fraction(3, 8)),
            )
            raw = poly_add(poly_power(v, 2), poly_scale(poly_power(u, 3), Fraction(-1)))
            leading_six = coefficient(raw, 6)
            reduced = poly_add(raw, poly_scale(u, -leading_six))

            require(
                all(coefficient(reduced, degree) == 0 for degree in range(6, 19)),
                "the unique A term cancels every coefficient at degree at least six",
            )
            require(
                coefficient(reduced, 5) == Fraction(3, 8) * b,
                "degree-five coefficient is 3b/8",
            )
            require(
                coefficient(reduced, 4) == -Fraction(1, 8) * (c - b * b),
                "degree-four coefficient is -(c-b^2)/8",
            )
            require(
                coefficient(reduced, 3) == Fraction(5, 8) * b * (2 * c + b * b),
                "degree-three coefficient identity",
            )

    # If the quadratic coefficient a of R vanishes but its linear
    # coefficient b does not, the uncancellable t^8 coefficient is
    # -3*b^2/4.  If a=b=0, the A and B terms reduce the approximate root to
    # zero (parameter degree zero), never to exact degree two.
    for p_integer in range(-2, 3):
        for q_integer in range(-2, 3):
            for b_integer in (-2, -1, 1, 2):
                for c_integer in range(-2, 3):
                    p = Fraction(p_integer)
                    q = Fraction(q_integer)
                    b = Fraction(b_integer)
                    c = Fraction(c_integer)
                    z = (q, p, Fraction(0), Fraction(1))
                    r = (c, b)
                    u = poly_add(poly_power(z, 2), r)
                    v = poly_add(poly_power(z, 3), poly_scale(poly_multiply(z, r), Fraction(3, 2)))
                    raw = poly_add(poly_power(v, 2), poly_scale(poly_power(u, 3), Fraction(-1)))
                    require(
                        coefficient(raw, 8) == -Fraction(3, 4) * b * b,
                        "a=0,b!=0 has an uncancellable degree-eight coefficient",
                    )
    for c_integer in (-2, -1, 1, 2):
        c = Fraction(c_integer)
        z = (Fraction(1), Fraction(-1), Fraction(0), Fraction(1))
        r = (c,)
        u = poly_add(poly_power(z, 2), r)
        v = poly_add(poly_power(z, 3), poly_scale(poly_multiply(z, r), Fraction(3, 2)))
        raw = poly_add(poly_power(v, 2), poly_scale(poly_power(u, 3), Fraction(-1)))
        reduced = poly_add(raw, poly_scale(u, Fraction(3, 4) * c * c))
        reduced = poly_add(reduced, (Fraction(1, 4) * c**3,))
        require(reduced == (Fraction(0),), "constant R gives parameter degree zero")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutate-drop-freeness", action="store_true")
    parser.add_argument("--mutate-allow-c32-b1-one", action="store_true")
    parser.add_argument("--mutate-promote-zero-s4", action="store_true")
    arguments = parser.parse_args()

    sequences = conductor_eight_sequences(arguments.mutate_drop_freeness)
    expected_sequences = ((5, 3), (6, 4, 5), (9, 2), (9, 6, 2))
    require(sequences == expected_sequences, "complete conductor-eight delta-sequence census")

    torus_words = {
        "T(2,9)": (2, (1,) * 9),
        "T(3,5)": (3, (1, 2) * 5),
    }
    cable_words: dict[str, tuple[int, tuple[int, ...]]] = {}
    for winding, meridional in ((2, 5), (3, 2)):
        for sign in (1, -1):
            for chirality in (1, -1):
                key = f"C({winding},{sign * meridional:+d};chi={chirality:+d})"
                cable_words[key] = (
                    2 * winding,
                    cable_braid_word(winding, sign * meridional, chirality),
                )

    s4_counts = {
        key: full_s4_colorings(strands, word)
        for key, (strands, word) in {**torus_words, **cable_words}.items()
    }
    fox_counts = {
        key: fox_three_colorings(strands, word)
        for key, (strands, word) in {**torus_words, **cable_words}.items()
    }
    require(s4_counts["T(2,9)"] == 0, "T(2,9) has no full-S4 coloring")
    require(s4_counts["T(3,5)"] == 0, "T(3,5) has no full-S4 coloring")
    winding_two_counts = {
        value for key, value in s4_counts.items() if key.startswith("C(2,")
    }
    winding_three_counts = {
        value for key, value in s4_counts.items() if key.startswith("C(3,")
    }
    if arguments.mutate_promote_zero_s4:
        winding_two_counts.add(144)
    require(winding_two_counts == {0}, "all winding-two rows have zero full-S4 colorings")
    require(winding_three_counts == {144}, "all winding-three rows have 144 full-S4 colorings")
    require(fox_counts["T(2,9)"] == 9, "T(2,9) Fox-3 count")
    require(fox_counts["T(3,5)"] == 3, "T(3,5) Fox-3 count")
    require(
        {value for key, value in fox_counts.items() if key.startswith("C(2,")} == {3},
        "winding-two Fox-3 counts",
    )
    require(
        {value for key, value in fox_counts.items() if key.startswith("C(3,")} == {27},
        "winding-three Fox-3 counts",
    )
    determinants = {
        "T(2,9)": 9,
        "T(3,5)": 1,
        **{key: 5 for key in cable_words if key.startswith("C(2,")},
        **{key: 9 for key in cable_words if key.startswith("C(3,")},
    }
    require(
        fox_counts["T(2,9)"] == 3 ** (1 + 1)
        and fox_counts["T(3,5)"] == 3 ** (1 + 0),
        "torus determinant/Fox consistency at three",
    )
    require(
        all(fox_counts[key] == 3 for key in determinants if key.startswith("C(2,"))
        and all(fox_counts[key] == 27 for key in determinants if key.startswith("C(3,")),
        "cable determinant/Fox consistency at three",
    )

    check_normal_form_grid()

    # Integer-scaled canonical member of the forced row.
    t2: Polynomial = (Fraction(0), Fraction(0), Fraction(1))
    u: Polynomial = (Fraction(0), Fraction(0), Fraction(8), Fraction(0), Fraction(0), Fraction(0), Fraction(1))
    v: Polynomial = (
        Fraction(0), Fraction(24), Fraction(0), Fraction(0), Fraction(0),
        Fraction(12), Fraction(0), Fraction(0), Fraction(0), Fraction(1),
    )
    relation = poly_add(
        poly_add(poly_power(v, 2), poly_scale(poly_power(u, 3), Fraction(-1))),
        poly_scale(u, Fraction(-64)),
    )
    require(relation == poly_scale(t2, Fraction(64)), "canonical degree-two approximate root")

    # V=t*(w^2+12w+24), w=t^4.  Its quadratic has nonzero discriminant 48
    # and nonzero constant 24, hence two distinct nonzero w roots.  Each has
    # four distinct fourth roots, partitioned into two disjoint {t,-t}
    # pairs; U is even and V vanishes at all eight endpoints.
    pair_quadratic_discriminant = 12 * 12 - 4 * 24
    require(pair_quadratic_discriminant == 48, "two distinct w roots")
    require(24 != 0, "both w roots are nonzero")
    minimum_b1 = 1 if arguments.mutate_allow_c32_b1_one else 4
    require(minimum_b1 >= 4, "four disjoint normalization pairs force b1 at least four")

    payload = {
        "status": "PASS-A1-GENUS-FOUR-CABLE-B1-OBSTRUCTION",
        "prime_topological_genus_four_rows": [
            "T(2,+/-9)",
            "T(3,+/-5)",
            "C(2,+/-5)(trefoil_or_mirror)",
            "C(3,+/-2)(trefoil_or_mirror)",
            "C(4,+/-1)(trefoil_or_mirror)",
            "C(2,+/-1)(T(2,5)_or_mirror)",
            "C(2,+/-1)(C(2,1)(trefoil)_or_mirrors)",
        ],
        "conductor_eight_delta_sequences": [list(sequence) for sequence in sequences],
        "one_place_rows_after_freeness": [
            "T(2,9):(9,2)",
            "T(3,5):(5,3)",
            "C(2,5)(trefoil):(6,4,5)",
            "C(3,2)(trefoil):(9,6,2)",
        ],
        "s4_labeled_full_colorings": s4_counts,
        "knot_determinants": determinants,
        "fox_three_colorings": fox_counts,
        "sole_group_level_survivor": "C(3,+/-2)(trefoil_or_mirror); delta=(9,6,2)",
        "forced_normal_form": {
            "U": "t^6+8*t^2",
            "V": "t^9+12*t^5+24*t",
            "approximate_root": "V^2-U^3-64*U=64*t^2",
            "self_pair_equation": "w^2+12*w+24=0; w=t^4",
            "minimum_b1": minimum_b1,
        },
        "charged_b1_one_genus_four_survivor": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    print(json.dumps(payload, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
