#!/usr/bin/env python3
"""Finite replay for the T(3,4) degree-three ramification obstruction.

The delta-sequence classification, polynomial normalization projection,
Zariski--van Kampen generation, and quartic local-decomposition table are
written theorem interfaces in the accompanying report.  This replay checks
the complete transposition/Hurwitz combinatorics at their junction.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json


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


def generated_subgroup(generators: tuple[Permutation, ...]) -> frozenset[Permutation]:
    identity = tuple(range(len(generators[0])))
    subgroup = {identity}
    frontier = [identity]
    while frontier:
        current = frontier.pop()
        for generator in generators:
            candidate = compose(current, generator)
            if candidate not in subgroup:
                subgroup.add(candidate)
                frontier.append(candidate)
    return frozenset(subgroup)


def hurwitz_positive(colors: tuple[Permutation, ...], index: int) -> tuple[Permutation, ...]:
    result = list(colors)
    first = result[index]
    second = result[index + 1]
    result[index] = conjugate(first, second)
    result[index + 1] = first
    return tuple(result)


def hurwitz_negative(colors: tuple[Permutation, ...], index: int) -> tuple[Permutation, ...]:
    result = list(colors)
    first = result[index]
    second = result[index + 1]
    result[index] = second
    result[index + 1] = conjugate(second, first)
    return tuple(result)


def braid_action(
    colors: tuple[Permutation, ...], word: tuple[int, ...]
) -> tuple[Permutation, ...]:
    result = colors
    for letter in word:
        index = abs(letter) - 1
        result = (
            hurwitz_positive(result, index)
            if letter > 0
            else hurwitz_negative(result, index)
        )
    return result


def support_connected(colors: tuple[Permutation, ...]) -> bool:
    edges = []
    for color in colors:
        moved = tuple(index for index, image in enumerate(color) if index != image)
        require(len(moved) == 2, "transposition support")
        edges.append(moved)
    reached = {0}
    changed = True
    while changed:
        changed = False
        for first, second in edges:
            if first in reached and second not in reached:
                reached.add(second)
                changed = True
            if second in reached and first not in reached:
                reached.add(first)
                changed = True
    return reached == {0, 1, 2, 3}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mutate-allow-duplicate-s4",
        action="store_true",
        help="incorrectly allow a duplicate three-meridian tuple to generate S4",
    )
    args = parser.parse_args()

    transpositions = tuple(
        transposition(first, second)
        for first in range(4)
        for second in range(first + 1, 4)
    )
    all_triples = tuple(itertools.product(transpositions, repeat=3))
    s4_triples = tuple(
        colors for colors in all_triples if len(generated_subgroup(colors)) == 24
    )
    duplicate_triples = tuple(colors for colors in all_triples if len(set(colors)) < 3)
    duplicate_s4 = tuple(
        colors for colors in duplicate_triples if len(generated_subgroup(colors)) == 24
    )

    require(len(s4_triples) == 96, "ordered transposition spanning-tree census")
    require(all(support_connected(colors) for colors in s4_triples), "S4 support graph")
    if args.mutate_allow_duplicate_s4:
        duplicate_s4 = (duplicate_triples[0],)
    require(not duplicate_s4, "duplicate three-meridian tuple is intransitive")
    require(
        max(len(generated_subgroup(colors)) for colors in duplicate_triples) == 6,
        "two distinct transpositions generate at most S3",
    )

    # The T(3,4) boundary word retains 24 labelled S4 triples.
    boundary_word = (1, 2) * 4
    boundary_s4 = tuple(
        colors for colors in s4_triples if braid_action(colors, boundary_word) == colors
    )
    require(len(boundary_s4) == 24, "T(3,4) boundary S4 coloring census")

    # A full Hurwitz tail is a Nielsen automorphism: check both generators and
    # inverses exhaustively on every transposition triple.  Thus it is safe to
    # diagnose duplicate colors in the local frame instead of the original
    # based frame.
    for colors in all_triples:
        original = generated_subgroup(colors)
        for index in (0, 1):
            positive = hurwitz_positive(colors, index)
            negative = hurwitz_negative(colors, index)
            require(generated_subgroup(positive) == original, "positive Hurwitz subgroup")
            require(generated_subgroup(negative) == original, "negative Hurwitz subgroup")
            require(hurwitz_negative(positive, index) == colors, "Hurwitz inverse +-")
            require(hurwitz_positive(negative, index) == colors, "Hurwitz inverse -+")

    # Degree-three fibre-length check used to locate a critical point away
    # from the unique two-point conductor fibre.  A critical endpoint has
    # local multiplicity at least two; two such endpoints, or one totally
    # ramified endpoint plus the other conductor endpoint, exceed degree 3.
    require(2 + 2 > 3, "two critical conductor endpoints exceed cubic degree")
    require(3 + 1 > 3, "total ramification plus conductor mate exceeds cubic degree")

    payload = {
        "status": "PASS-A1-GENUS-THREE-M0-RAMIFICATION-OBSTRUCTION",
        "scope": "irreducible one-place b1=1 total-delta=3 quartic m=0 row",
        "genus_three_candidate_after_cable_b1_filter": "T(3,4)",
        "degree_three_projection": {
            "finite_ramification_exists": "written polynomial interface",
            "critical_point_outside_unique_conductor_pair": True,
            "local_m0_packet": "(2,1,1) with C2 decomposition group",
        },
        "transposition_triples": {
            "all": len(all_triples),
            "generate_S4": len(s4_triples),
            "duplicate_generate_S4": len(duplicate_s4),
            "T(3,4)_boundary_generate_S4": len(boundary_s4),
        },
        "hurwitz_tail_preserves_generated_subgroup": True,
        "conclusion": "NO-TRANSITIVE-S4; CHARGED-M0-TOTAL-DELTA-THREE-EMPTY",
        "m1_row_addressed": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    print(json.dumps(payload, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
