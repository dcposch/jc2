#!/usr/bin/env python3
"""Desk-small exact replay for the genus-three T(3,4), m=0 obstruction.

This script checks only finite permutation-group facts, the displayed
degree-(3,4) coincidence algebra, and the elementary degree-three
multiplicity bound.  The algebro-geometric normalization and the charged
local-monodromy interface remain theorem-layer arguments in the report.
"""

from __future__ import annotations

import argparse
from itertools import product


Permutation = tuple[int, int, int, int]
IDENTITY: Permutation = (0, 1, 2, 3)


def check(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def compose(left: Permutation, right: Permutation) -> Permutation:
    """Return left after right."""

    return tuple(left[right[index]] for index in range(4))  # type: ignore[return-value]


def inverse(value: Permutation) -> Permutation:
    result = [0, 0, 0, 0]
    for index, image in enumerate(value):
        result[image] = index
    return tuple(result)  # type: ignore[return-value]


def conjugate(left: Permutation, right: Permutation) -> Permutation:
    return compose(compose(left, right), inverse(left))


def transposition(first: int, second: int) -> Permutation:
    result = list(IDENTITY)
    result[first], result[second] = result[second], result[first]
    return tuple(result)  # type: ignore[return-value]


TRANSPOSITIONS = tuple(
    transposition(first, second)
    for first in range(4)
    for second in range(first + 1, 4)
)


def subgroup(generators: tuple[Permutation, ...]) -> frozenset[Permutation]:
    seen = {IDENTITY}
    frontier = [IDENTITY]
    while frontier:
        current = frontier.pop()
        for generator in generators:
            candidate = compose(current, generator)
            if candidate not in seen:
                seen.add(candidate)
                frontier.append(candidate)
    return frozenset(seen)


def orbit(group: frozenset[Permutation], point: int) -> frozenset[int]:
    return frozenset(value[point] for value in group)


def hurwitz_forward(
    triple: tuple[Permutation, Permutation, Permutation], index: int
) -> tuple[Permutation, Permutation, Permutation]:
    result = list(triple)
    left, right = result[index], result[index + 1]
    result[index], result[index + 1] = conjugate(left, right), left
    return tuple(result)  # type: ignore[return-value]


def hurwitz_inverse(
    triple: tuple[Permutation, Permutation, Permutation], index: int
) -> tuple[Permutation, Permutation, Permutation]:
    result = list(triple)
    left, right = result[index], result[index + 1]
    result[index], result[index + 1] = right, conjugate(inverse(right), left)
    return tuple(result)  # type: ignore[return-value]


def support_edges(
    triple: tuple[Permutation, Permutation, Permutation]
) -> frozenset[tuple[int, int]]:
    edges: set[tuple[int, int]] = set()
    for value in triple:
        moved = tuple(index for index in range(4) if value[index] != index)
        check(len(moved) == 2, "non-transposition in meridian tuple")
        edges.add((moved[0], moved[1]))
    return frozenset(edges)


def graph_connected(edges: frozenset[tuple[int, int]]) -> bool:
    reached = {0}
    changed = True
    while changed:
        changed = False
        for left, right in edges:
            if left in reached and right not in reached:
                reached.add(right)
                changed = True
            if right in reached and left not in reached:
                reached.add(left)
                changed = True
    return len(reached) == 4


def x_value(t: int, a: int) -> int:
    return t**3 + a * t


def y_value(t: int, b: int, c: int) -> int:
    return t**4 + b * t**2 + c * t


def cubic_coefficients_from_roots(roots: tuple[int, int, int]) -> tuple[int, int, int]:
    r0, r1, r2 = roots
    return (
        -(r0 + r1 + r2),
        r0 * r1 + r0 * r2 + r1 * r2,
        -(r0 * r1 * r2),
    )


def coincidence_checks() -> None:
    for a, b, c, t, u in product(range(-3, 4), repeat=5):
        if t == u:
            continue
        x_quotient = (x_value(t, a) - x_value(u, a)) // (t - u)
        y_quotient = (y_value(t, b, c) - y_value(u, b, c)) // (t - u)
        check(
            x_quotient == t * t + t * u + u * u + a,
            "degree-three divided-difference identity failed",
        )
        check(
            y_quotient
            == t**3 + t * t * u + t * u * u + u**3 + b * (t + u) + c,
            "degree-four divided-difference identity failed",
        )
        s = t + u
        p = t * u
        if x_quotient == 0:
            check(p == s * s + a, "p=s^2+a elimination failed")
            check(
                y_quotient == -s**3 + (b - 2 * a) * s + c,
                "self-pair cubic elimination failed",
            )

    # The four possible root-multiplicity patterns with one admissible
    # unordered pair.  A root is diagonal exactly when -3*s^2-4*a=0.
    patterns = []
    a = 2
    patterns.append(("triple-pair", a, 2 * a, 0, (0, 0, 0), (False, False, False)))

    r = 2
    patterns.append(
        ("double-pair+diagonal", -3 * r * r, -3 * r * r, -2 * r**3,
         (r, r, -2 * r), (False, False, True))
    )

    a = -3
    patterns.append(("pair+two-diagonals", a, 2 * a // 3, 0,
                     (0, 2, -2), (False, True, True)))

    q = 2
    patterns.append(
        ("pair+double-diagonal", -3 * q * q // 4, 3 * q * q // 2, -2 * q**3,
         (-2 * q, q, q), (False, True, True))
    )

    for name, a, b, c, roots, diagonal_flags in patterns:
        square, linear, constant = cubic_coefficients_from_roots(roots)
        check(square == 0, f"{name}: self-pair cubic acquired s^2 term")
        check(linear == 2 * a - b, f"{name}: linear coefficient failed")
        check(constant == -c, f"{name}: constant coefficient failed")
        actual_flags = tuple(-3 * root * root - 4 * a == 0 for root in roots)
        check(actual_flags == diagonal_flags, f"{name}: diagonal classification failed")


def group_checks(mutate_allow_duplicate_s4: bool) -> tuple[int, int]:
    full_s4 = 0
    duplicate = 0
    duplicate_full_s4 = 0
    for triple in product(TRANSPOSITIONS, repeat=3):
        typed = tuple(triple)  # type: ignore[assignment]
        generated = subgroup(typed)
        edges = support_edges(typed)
        is_full = len(generated) == 24 and len(orbit(generated, 0)) == 4
        check(
            is_full == graph_connected(edges),
            "transposition support graph/group mismatch",
        )
        if is_full:
            full_s4 += 1
        if len(edges) < 3:
            duplicate += 1
            if is_full:
                duplicate_full_s4 += 1

        for index in (0, 1):
            moved = hurwitz_forward(typed, index)
            check(subgroup(moved) == generated, "forward Hurwitz move changed subgroup")
            check(hurwitz_inverse(moved, index) == typed, "Hurwitz inverse failed")
            moved_back = hurwitz_inverse(typed, index)
            check(subgroup(moved_back) == generated, "inverse Hurwitz move changed subgroup")
            check(hurwitz_forward(moved_back, index) == typed, "Hurwitz forward failed")

    check(full_s4 == 96, "unexpected number of ordered full-S4 triples")
    check(duplicate == 96, "unexpected number of duplicate-color triples")
    if mutate_allow_duplicate_s4:
        check(duplicate_full_s4 > 0, "mutation rejected: no duplicate triple generates S4")
    else:
        check(duplicate_full_s4 == 0, "duplicate transpositions generated S4")
    return full_s4, duplicate


def multiplicity_checks(mutate_conductor_holds_all_ramification: bool) -> None:
    # If both endpoints of a two-point conductor fibre were critical for a
    # cubic, their two local multiplicities would already total at least 4.
    both_simple_critical_total = 2 + 2
    # If the derivative has a double root at one endpoint, that endpoint has
    # ramification index 3; the other conductor endpoint is still a root.
    one_total_critical_plus_other_total = 3 + 1
    if mutate_conductor_holds_all_ramification:
        check(
            both_simple_critical_total <= 3
            or one_total_critical_plus_other_total <= 3,
            "mutation rejected: a cubic fibre cannot contain all conductor ramification",
        )
    else:
        check(both_simple_critical_total > 3, "two critical endpoints fit in cubic fibre")
        check(
            one_total_critical_plus_other_total > 3,
            "total critical endpoint plus its partner fit in cubic fibre",
        )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutate-allow-duplicate-s4", action="store_true")
    parser.add_argument("--mutate-conductor-holds-all-ramification", action="store_true")
    args = parser.parse_args()

    coincidence_checks()
    full_s4, duplicate = group_checks(args.mutate_allow_duplicate_s4)
    multiplicity_checks(args.mutate_conductor_holds_all_ramification)

    print("T34_M0_PROJECTION_REPLAY=PASS")
    print("NORMAL_FORM=X=t^3+a*t;Y=t^4+b*t^2+c*t")
    print("SELF_PAIR_CUBIC=s^3+(2*a-b)*s-c")
    print("FULL_S4_ORDERED_TRANSPOSITION_TRIPLES=" + str(full_s4))
    print("DUPLICATE_COLOR_TRIPLES=" + str(duplicate))
    print("DUPLICATE_COLOR_FULL_S4=0")
    print("HURWITZ_GENERATED_SUBGROUP=INVARIANT")
    print("CUBIC_CONDUCTOR_RAMIFICATION_CAPACITY=FAILS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
