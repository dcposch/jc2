#!/usr/bin/env python3
"""Desk replay for the all-degree one-node meridional-rank obstruction.

The algebraic genus bridge and the quotient from the infinity-knot group to
the affine complement group are written theorem interfaces.  This script
exhausts transposition-valued representations of the trefoil presentation in
S_d for a deterministic range and verifies the symbolic support census.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json


Permutation = tuple[int, ...]


def compose(left: Permutation, right: Permutation) -> Permutation:
    return tuple(left[right[index]] for index in range(len(left)))


def transposition(degree: int, first: int, second: int) -> Permutation:
    result = list(range(degree))
    result[first], result[second] = result[second], result[first]
    return tuple(result)


def moved_support(permutation: Permutation) -> frozenset[int]:
    return frozenset(index for index, image in enumerate(permutation) if image != index)


def generated_orbit(generators: tuple[Permutation, ...], seed: int) -> frozenset[int]:
    orbit = {seed}
    frontier = [seed]
    while frontier:
        current = frontier.pop()
        for generator in generators:
            candidate = generator[current]
            if candidate not in orbit:
                orbit.add(candidate)
                frontier.append(candidate)
    return frozenset(orbit)


def generated_subgroup(generators: tuple[Permutation, ...]) -> frozenset[Permutation]:
    degree = len(generators[0])
    unit = tuple(range(degree))
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


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mutate-allow-degree-three",
        action="store_true",
        help="incorrectly demand exclusion beginning in degree three",
    )
    args = parser.parse_args()

    minimum_excluded_degree = 3 if args.mutate_allow_degree_three else 4
    degree_census: dict[int, dict[str, int]] = {}
    global_maximum_orbit = 0

    for degree in range(2, 11):
        transpositions = tuple(
            transposition(degree, first, second)
            for first in range(degree)
            for second in range(first + 1, degree)
        )
        equal_count = 0
        overlapping_count = 0
        disjoint_relation_count = 0
        maximum_orbit = 0
        maximum_image_order = 0

        for first, second in itertools.product(transpositions, repeat=2):
            left = compose(compose(first, second), first)
            right = compose(compose(second, first), second)
            if left != right:
                continue

            first_support = moved_support(first)
            second_support = moved_support(second)
            if first == second:
                equal_count += 1
            elif first_support.isdisjoint(second_support):
                disjoint_relation_count += 1
            else:
                overlapping_count += 1

            pair = (first, second)
            maximum_orbit = max(
                maximum_orbit,
                max(len(generated_orbit(pair, seed)) for seed in range(degree)),
            )
            maximum_image_order = max(maximum_image_order, len(generated_subgroup(pair)))

        expected_equal = degree * (degree - 1) // 2
        expected_overlapping = degree * (degree - 1) * (degree - 2)
        require(equal_count == expected_equal, "equal transposition-pair census")
        require(overlapping_count == expected_overlapping, "overlapping transposition-pair census")
        require(disjoint_relation_count == 0, "disjoint transpositions fail the trefoil relation")
        require(maximum_orbit == min(degree, 3), "trefoil transposition orbit bound")
        require(maximum_image_order == (2 if degree == 2 else 6), "trefoil image-order bound")

        if degree >= minimum_excluded_degree:
            require(maximum_orbit < degree, "no connected degree-d transposition cover")

        degree_census[degree] = {
            "equal_pairs": equal_count,
            "overlapping_distinct_pairs": overlapping_count,
            "maximum_orbit": maximum_orbit,
            "maximum_image_order": maximum_image_order,
        }
        global_maximum_orbit = max(global_maximum_orbit, maximum_orbit)

    payload = {
        "status": "PASS-ONE-NODE-ALL-DEGREE-MERIDIONAL-RANK",
        "tested_degrees": [2, 10],
        "symbolic_pair_classification": {
            "equal": "C2 on two letters",
            "overlapping_distinct": "S3 on three letters",
            "disjoint_distinct": "fails aba=bab",
        },
        "maximum_transitive_support": global_maximum_orbit,
        "excluded_connected_degrees": "all d>=4",
        "degree_census": degree_census,
        "degree_three_control": "trefoil knot-group S3 quotient exists; no (2,2) local claim",
        "one_place_A1_sole_ordinary_node_connected_simple_cover_degree_ge_4": False,
        "tangential_unibranch_reducible_horns": "OPEN",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    print(json.dumps(payload, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
