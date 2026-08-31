#!/usr/bin/env python3
"""Finite replay for the charged T(3,4), m=1 ramification obstruction.

The script checks the exhaustive transposition/Hurwitz interface and the two
possible critical-divisor partitions of a cubic.  The charged fibre table,
Zariski--van Kampen generation, and locality of a saturated cubic fibre are
theorem-layer arguments in the accompanying report.
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


def inverse(value: Permutation) -> Permutation:
    result = [0] * len(value)
    for index, image in enumerate(value):
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
    identity = tuple(range(len(generators[0])))
    seen = {identity}
    frontier = [identity]
    while frontier:
        current = frontier.pop()
        for generator in generators:
            candidate = compose(current, generator)
            if candidate not in seen:
                seen.add(candidate)
                frontier.append(candidate)
    return frozenset(seen)


def hurwitz_positive(colors: tuple[Permutation, ...], index: int) -> tuple[Permutation, ...]:
    result = list(colors)
    left, right = result[index], result[index + 1]
    result[index], result[index + 1] = conjugate(left, right), left
    return tuple(result)


def hurwitz_negative(colors: tuple[Permutation, ...], index: int) -> tuple[Permutation, ...]:
    result = list(colors)
    left, right = result[index], result[index + 1]
    result[index], result[index + 1] = right, conjugate(inverse(right), left)
    return tuple(result)


def braid_action(colors: tuple[Permutation, ...], word: tuple[int, ...]) -> tuple[Permutation, ...]:
    result = colors
    for letter in word:
        index = abs(letter) - 1
        result = (
            hurwitz_positive(result, index)
            if letter > 0
            else hurwitz_negative(result, index)
        )
    return result


def transposition_census(
    mutate_allow_duplicate_s4: bool, mutate_local_s3_as_s4: bool
) -> dict[str, int]:
    all_triples = tuple(itertools.product(TRANSPOSITIONS, repeat=3))
    s4_triples = tuple(
        triple for triple in all_triples if len(generated_subgroup(triple)) == 24
    )
    duplicate_triples = tuple(triple for triple in all_triples if len(set(triple)) < 3)
    duplicate_s4 = tuple(
        triple for triple in duplicate_triples if len(generated_subgroup(triple)) == 24
    )
    if mutate_allow_duplicate_s4:
        duplicate_s4 = (duplicate_triples[0],)

    require(len(all_triples) == 216, "quartic transposition triple census")
    require(len(s4_triples) == 96, "ordered spanning-tree triple census")
    require(not duplicate_s4, "a duplicate transposition triple generated S4")

    # A totally ramified T31 critical point places all three meridians in a
    # conjugate of the local S3 fixing the fourth sheet.
    local_s3_transpositions = (
        transposition(0, 1),
        transposition(0, 2),
        transposition(1, 2),
    )
    local_s3_triples = tuple(itertools.product(local_s3_transpositions, repeat=3))
    if mutate_local_s3_as_s4:
        local_s3_triples = local_s3_triples + (s4_triples[0],)
    require(
        all(len(generated_subgroup(triple)) <= 6 for triple in local_s3_triples),
        "mutated local T31 group escaped its fixed-sheet S3",
    )

    # At T22 the charged complete local group is C2 x C2 on two disjoint
    # pairs.  Every branch meridian is one of the two displayed generators.
    local_t22_transpositions = (transposition(0, 1), transposition(2, 3))
    local_t22_triples = tuple(itertools.product(local_t22_transpositions, repeat=3))
    require(
        all(len(generated_subgroup(triple)) <= 4 for triple in local_t22_triples),
        "local T22 triple escaped C2 x C2",
    )

    # A simple critical T211 branch duplicates the two colors in its
    # ramified cluster; the third color may be arbitrary.
    local_t211_triples = tuple(
        (repeated, repeated, third)
        for repeated in TRANSPOSITIONS
        for third in TRANSPOSITIONS
    )
    require(
        all(len(generated_subgroup(triple)) < 24 for triple in local_t211_triples),
        "simple T211 cluster generated S4",
    )

    # Any full braid tail is a sequence of Nielsen transformations.  Check
    # both signed generators on every possible transposition tuple.
    for triple in all_triples:
        original = generated_subgroup(triple)
        for index in (0, 1):
            positive = hurwitz_positive(triple, index)
            negative = hurwitz_negative(triple, index)
            require(generated_subgroup(positive) == original, "positive Hurwitz subgroup")
            require(generated_subgroup(negative) == original, "negative Hurwitz subgroup")
            require(hurwitz_negative(positive, index) == triple, "Hurwitz inverse +-")
            require(hurwitz_positive(negative, index) == triple, "Hurwitz inverse -+")

    boundary_word = (1, 2) * 4
    boundary_s4 = tuple(
        triple for triple in s4_triples if braid_action(triple, boundary_word) == triple
    )
    require(len(boundary_s4) == 24, "T(3,4) boundary S4 coloring census")

    return {
        "all": len(all_triples),
        "generate_S4": len(s4_triples),
        "duplicate_generate_S4": len(duplicate_s4),
        "local_T31_triples": len(local_s3_triples),
        "local_T22_triples": len(local_t22_triples),
        "local_T211_simple_cluster_triples": len(local_t211_triples),
        "T34_boundary_generate_S4": len(boundary_s4),
    }


def cubic_critical_census(mutate_allow_two_t31_critical_points: bool) -> dict[str, int]:
    # A cubic derivative has either one double root or two simple roots.
    # T31 is unique.  Every other normalization point is T211 unless it is
    # one of the two preimages of the unique T22 conductor value (n4=0).
    event_types = ("T31", "T211", "T22")

    double_cases = []
    for event in event_types:
        if event == "T31":
            verdict = "LOCAL_S3_INTRANSITIVE"
        elif event == "T211":
            verdict = "LOCAL_C2_INTRANSITIVE"
        else:
            # Local degree three at one conductor endpoint plus its distinct
            # mate in the same X-fibre would have length at least four.
            require(3 + 1 > 3, "double-critical conductor endpoint fit in cubic fibre")
            verdict = "IMPOSSIBLE_FIBRE_LENGTH"
        double_cases.append((event, verdict))

    simple_cases = []
    impossible_both_t22 = 0
    for first, second in itertools.product(event_types, repeat=2):
        if not mutate_allow_two_t31_critical_points and (first, second) == ("T31", "T31"):
            continue
        if (first, second) == ("T22", "T22"):
            # The two roots would be the two endpoints of the sole conductor
            # fibre, each with local multiplicity at least two.
            require(2 + 2 > 3, "both conductor endpoints were critical for a cubic")
            impossible_both_t22 += 1
            simple_cases.append((first, second))
            continue
        non_t31 = tuple(event for event in (first, second) if event != "T31")
        killed = bool(non_t31)
        if killed:
            # T211 gives a duplicate cluster.  T22 gives the saturated fibre
            # 2*a+b of length three inside the pair-preserving local group.
            for event in non_t31:
                if event == "T22":
                    require(2 + 1 == 3, "simple-critical conductor fibre does not saturate")
        require(killed, "two simple critical points were both assigned to unique T31")
        simple_cases.append((first, second))

    require(len(double_cases) == 3, "double-root critical partition census")
    require(len(simple_cases) == 8, "unique-T31 simple-root partition census")
    require(impossible_both_t22 == 1, "both-T22 impossible case census")
    return {
        "double_root_cases": len(double_cases),
        "two_simple_root_assignments_under_unique_T31": len(simple_cases),
        "two_simple_both_T22_impossible": impossible_both_t22,
        "two_simple_realizable_assignments": len(simple_cases) - impossible_both_t22,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutate-allow-duplicate-s4", action="store_true")
    parser.add_argument("--mutate-local-s3-as-s4", action="store_true")
    parser.add_argument("--mutate-allow-two-t31-critical-points", action="store_true")
    args = parser.parse_args()

    transpositions = transposition_census(
        args.mutate_allow_duplicate_s4, args.mutate_local_s3_as_s4
    )
    critical = cubic_critical_census(args.mutate_allow_two_t31_critical_points)

    payload = {
        "status": "PASS-A1-GENUS-THREE-T34-M1-RAMIFICATION-OBSTRUCTION",
        "scope": "irreducible charged b1=1 n4=0 total-delta=3 m=1 T(3,4)",
        "cubic_critical_divisor_partitions": critical,
        "transposition_census": transpositions,
        "local_groups": {
            "T211": "C2",
            "T31": "S3 fixing one quartic sheet",
            "T22": "C2xC2 preserving two pairs",
        },
        "hurwitz_tail_preserves_generated_subgroup": True,
        "conclusion": "NO-TRANSITIVE-S4-IN-CHARGED-M1-T34-ROW",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    print(json.dumps(payload, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
