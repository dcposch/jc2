#!/usr/bin/env python3
"""Tiny replay for the total-delta-two knot-at-infinity obstruction.

The Neumann--Rudolph goodness bridge, the nearby-fibre delta formula,
Neumann's rooted splice construction, Schubert's genus/prime results, and the
double-branched-cover determinant lemma are written theorem interfaces.  This
script checks the finite genus-two cable census and the exact S4 controls.
"""

from __future__ import annotations

import argparse
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


def transposition(first: int, second: int, degree: int = 4) -> Permutation:
    result = list(range(degree))
    result[first], result[second] = result[second], result[first]
    return tuple(result)


def conjugate(left: Permutation, right: Permutation) -> Permutation:
    return compose(compose(left, right), inverse(left))


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


def braid_relation(first: Permutation, second: Permutation) -> bool:
    return compose(compose(first, second), first) == compose(
        compose(second, first), second
    )


def artin_generator(
    colors: tuple[Permutation, ...], index: int
) -> tuple[Permutation, ...]:
    """Apply sigma_index with x_i -> x_i x_(i+1) x_i^-1."""

    result = list(colors)
    first = result[index]
    second = result[index + 1]
    result[index] = conjugate(first, second)
    result[index + 1] = first
    return tuple(result)


def braid_action(
    colors: tuple[Permutation, ...], word: tuple[int, ...]
) -> tuple[Permutation, ...]:
    result = colors
    for index in word:
        result = artin_generator(result, index)
    return result


def semigroup_gaps(generators: tuple[int, ...]) -> tuple[int, ...]:
    cutoff = 80
    represented = {0}
    for value in range(cutoff + 1):
        if value in represented:
            for generator in generators:
                if value + generator <= cutoff:
                    represented.add(value + generator)
    conductor = next(
        value
        for value in range(cutoff)
        if all(later in represented for later in range(value, cutoff + 1))
    )
    return tuple(value for value in range(conductor) if value not in represented)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mutate-exclude-delta-three",
        action="store_true",
        help="incorrectly demand that the genus-only obstruction extend to delta three",
    )
    args = parser.parse_args()

    # Schubert's formulas reduce the genus-two graph-knot census to these
    # elementary Diophantine equations after trivial cablings are removed.
    torus_solutions = {
        tuple(sorted((winding, meridional)))
        for winding in range(2, 10)
        for meridional in range(2, 10)
        if math.gcd(winding, meridional) == 1
        and (winding - 1) * (meridional - 1) // 2 == 2
    }
    cable_solutions = {
        (winding, meridional, companion_genus)
        for winding in range(2, 8)
        for meridional in range(1, 10)
        for companion_genus in range(1, 3)
        if (winding - 1) * (meridional - 1) % 2 == 0
        and winding * companion_genus
        + (winding - 1) * (meridional - 1) // 2
        == 2
    }
    connected_sum_partitions = {
        tuple(sorted((first, second)))
        for first in range(1, 3)
        for second in range(1, 3)
        if first + second == 2
    }
    require(torus_solutions == {(2, 5)}, "genus-two torus-knot census")
    require(cable_solutions == {(2, 1, 1)}, "genus-two nontrivial cable census")
    require(connected_sum_partitions == {(1, 1)}, "genus-two composite census")

    # The double-branched-cover lemma requires determinant divisible by three.
    determinants = {
        "T(2,5)": 5,
        "C(2,+/-1)(trefoil_or_mirror)": 1,
        "trefoil_or_mirror#trefoil_or_mirror": 9,
    }
    determinant_survivors = tuple(
        sorted(name for name, determinant in determinants.items() if determinant % 3 == 0)
    )
    require(
        determinant_survivors == ("trefoil_or_mirror#trefoil_or_mirror",),
        "only the composite graph knot survives the determinant filter",
    )

    # The composite survivor genuinely has a meridian-transposition S4 quotient.
    common = transposition(1, 2)  # (23)
    left = transposition(0, 1)  # (12)
    right = transposition(2, 3)  # (34)
    require(braid_relation(common, left), "left trefoil relation")
    require(braid_relation(common, right), "right trefoil relation")
    require(len(generated_subgroup((left, common, right))) == 24, "composite S4 image")
    require(compose(left, right) == compose(right, left), "a disjoint node pair can commute")

    # Sharp delta-three control: T(3,4)=closure((sigma_1 sigma_2)^4).
    transpositions = tuple(
        transposition(first, second)
        for first in range(4)
        for second in range(first + 1, 4)
    )
    torus_word = (0, 1) * 4
    fixed_s4_colorings = []
    for colors in itertools.product(transpositions, repeat=3):
        if braid_action(colors, torus_word) != colors:
            continue
        if len(generated_subgroup(colors)) == 24:
            fixed_s4_colorings.append(colors)

    explicit_coloring = (
        transposition(0, 1),  # (12)
        transposition(0, 2),  # (13)
        transposition(0, 3),  # (14)
    )
    require(explicit_coloring in fixed_s4_colorings, "explicit T(3,4) S4 coloring")
    require(len(fixed_s4_colorings) == 24, "T(3,4) labeled S4 coloring census")
    require(semigroup_gaps((3, 4)) == (1, 2, 5), "delta of C[t^3,t^4] is three")
    if args.mutate_exclude_delta_three:
        require(not fixed_s4_colorings, "false delta-three exclusion")

    payload = {
        "status": "PASS-A1-TOTAL-DELTA-TWO-S4-OBSTRUCTION",
        "nearby_fibre_genus_interface": "sum of affine delta invariants",
        "genus_two_graph_knots": {
            "torus": ["T(2,+/-5)"],
            "prime_satellite": ["C(2,+/-1)(trefoil_or_mirror)"],
            "composite": ["trefoil_or_mirror#trefoil_or_mirror"],
        },
        "one_place_polynomial_knot_interface": "iterated cable, hence prime or unknot",
        "determinants": determinants,
        "determinant_survivors_before_one_place_prime_filter": list(determinant_survivors),
        "connected_simple_degree_four_with_total_delta_at_most_two": False,
        "composite_control_image_order": 24,
        "bare_disjoint_node_commutator_compatible_with_composite_control": True,
        "delta_three_control": {
            "curve": "(x,y)=(t^3,t^4), y^3=x^4",
            "semigroup_gaps": [1, 2, 5],
            "knot_at_infinity": "T(3,4)",
            "braid": "(sigma1 sigma2)^4",
            "explicit_colors": ["(12)", "(13)", "(14)"],
            "labeled_S4_colorings": len(fixed_s4_colorings),
        },
        "total_delta_threshold_is_sharp_for_group_obstruction": True,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    print(json.dumps(payload, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
