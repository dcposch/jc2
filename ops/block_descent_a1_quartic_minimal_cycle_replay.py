#!/usr/bin/env python3
"""Desk replay for the minimal connected-cycle quartic branch horn.

This checks only finite group, integer-ledger, and displayed spectator-family
identities.  It does not encode van Kampen, normalization, finite flatness,
the proper-block ruling theorem, or existence of a Keller first leg.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from itertools import permutations


Permutation = tuple[int, ...]
S4_ID: Permutation = (0, 1, 2, 3)
S3_ID: Permutation = (0, 1, 2)


def compose(left: Permutation, right: Permutation) -> Permutation:
    return tuple(left[right[index]] for index in range(len(left)))


def inverse(element: Permutation) -> Permutation:
    return tuple(element.index(index) for index in range(len(element)))


def conjugate(by: Permutation, element: Permutation) -> Permutation:
    return compose(compose(by, element), inverse(by))


def generated(identity: Permutation, generators: tuple[Permutation, ...]) -> frozenset[Permutation]:
    closure = {identity, *generators}
    while True:
        products = {
            compose(left, right) for left in closure for right in closure
        }
        if products <= closure:
            return frozenset(closure)
        closure |= products


def cycle_type(element: Permutation) -> tuple[int, ...]:
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


Quadratic = tuple[Fraction, Fraction]


def q_add(left: Quadratic, right: Quadratic) -> Quadratic:
    return (left[0] + right[0], left[1] + right[1])


def q_mul(left: Quadratic, right: Quadratic) -> Quadratic:
    """Multiply a+b*r with r^2=1/3."""
    return (
        left[0] * right[0] + left[1] * right[1] / 3,
        left[0] * right[1] + left[1] * right[0],
    )


def polynomial_product(
    left: tuple[Quadratic, ...], right: tuple[Quadratic, ...]
) -> tuple[Quadratic, ...]:
    coefficients = [(Fraction(0), Fraction(0))] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            index = left_index + right_index
            coefficients[index] = q_add(
                coefficients[index], q_mul(left_value, right_value)
            )
    return tuple(coefficients)


PAIRINGS = (
    (frozenset((0, 1)), frozenset((2, 3))),
    (frozenset((0, 2)), frozenset((1, 3))),
    (frozenset((0, 3)), frozenset((1, 2))),
)


def canonical_pairing(parts: tuple[frozenset[int], frozenset[int]]) -> frozenset[frozenset[int]]:
    return frozenset(parts)


PAIRING_INDEX = {
    canonical_pairing(parts): index for index, parts in enumerate(PAIRINGS)
}


def resolvent_image(element: Permutation) -> Permutation:
    image: list[int] = []
    for parts in PAIRINGS:
        moved = tuple(
            frozenset(element[value] for value in part) for part in parts
        )
        image.append(PAIRING_INDEX[canonical_pairing(moved)])
    return tuple(image)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mutate-resolvent-separates-node",
        action="store_true",
        help="inject the false claim that the cubic resolvent separates a node matching",
    )
    args = parser.parse_args()

    s4 = tuple(permutations(range(4)))
    transpositions = tuple(
        element for element in s4 if cycle_type(element) == (2, 1, 1)
    )
    require(len(transpositions) == 6, "S4 transposition census")

    # A (2,2) node is one perfect matching: two commuting, disjoint
    # transpositions.  There are three unlabelled matchings.
    matchings_set: set[frozenset[Permutation]] = set()
    for left in transpositions:
        for right in transpositions:
            if left == right:
                continue
            if compose(left, right) == compose(right, left):
                matchings_set.add(frozenset((left, right)))
    matchings = tuple(
        tuple(sorted(matching)) for matching in sorted(matchings_set, key=lambda row: sorted(row))
    )
    require(len(matchings) == 3, "three perfect matchings on four sheets")

    # The S4 -> S3 cubic-resolvent quotient identifies the two
    # transpositions in every perfect matching.
    resolvent_node_rows: list[dict[str, object]] = []
    for index, matching in enumerate(matchings):
        left, right = matching
        q_left = resolvent_image(left)
        q_right = resolvent_image(right)
        if args.mutate_resolvent_separates_node and index == 0:
            q_right = S3_ID
        require(q_left == q_right, "a disjoint node pair has one resolvent transposition")
        require(cycle_type(q_left) == (2, 1), "node resolvent inertia type")
        resolvent_node_rows.append(
            {"quartic_matching": [list(left), list(right)], "resolvent": list(q_left)}
        )

    # A single transporter carrying a transposition to its disjoint mate
    # preserves the corresponding two-block system and generates D4, never
    # S4.  This is a conditional one-stable-letter calculation, not a
    # presentation theorem for an arbitrary curve complement.
    tau = (1, 0, 2, 3)
    tau_disjoint = (0, 1, 3, 2)
    transporters = tuple(
        element for element in s4 if conjugate(element, tau) == tau_disjoint
    )
    transporter_orders = sorted(
        len(generated(S4_ID, (tau, element))) for element in transporters
    )
    require(len(transporters) == 4, "node-pair transporter census")
    require(transporter_orders == [8, 8, 8, 8], "node-only transport stays D4")

    # A cusp packet is an ordered pair of overlapping transpositions.  Each
    # satisfies the braid relation and generates S3.  Combining any such
    # packet with any node perfect matching generates S4: 24*3=72 packets.
    cusp_packets: list[tuple[Permutation, Permutation]] = []
    for left in transpositions:
        for right in transpositions:
            if left == right:
                continue
            if cycle_type(compose(left, right)) != (3, 1):
                continue
            require(
                compose(left, compose(right, left))
                == compose(right, compose(left, right)),
                "overlapping transpositions satisfy the cusp braid relation",
            )
            require(
                len(generated(S4_ID, (left, right))) == 6,
                "cusp packet generates S3",
            )
            cusp_packets.append((left, right))
    require(len(cusp_packets) == 24, "ordered cusp packet census")

    combined_orders: list[int] = []
    for cusp in cusp_packets:
        q_cusp = tuple(resolvent_image(element) for element in cusp)
        require(q_cusp[0] != q_cusp[1], "resolvent retains two cusp transpositions")
        require(
            len(generated(S3_ID, q_cusp)) == 6,
            "cusp gives transitive cubic-resolvent monodromy",
        )
        for matching in matchings:
            combined_orders.append(
                len(generated(S4_ID, cusp + matching))
            )
    require(len(combined_orders) == 72, "combined packet census")
    require(set(combined_orders) == {24}, "every cusp-plus-node packet generates S4")

    # The nodal cubic control has pi_1 = Z by the written van Kampen proof.
    # A meridian-transposition image is therefore one of six intransitive C2
    # images; equality of its two node meridians is incompatible with a
    # quartic (2,2) matching.
    cyclic_control_orders = sorted(
        len(generated(S4_ID, (element,))) for element in transpositions
    )
    require(cyclic_control_orders == [2] * 6, "nodal-control transposition images")
    require(
        not any(left == right for left, right in matchings),
        "equal node meridians cannot realize a quartic perfect matching",
    )

    # Generic and conductor sheet budgets are both saturated, not
    # contradictory: 4=2+1+1 and 4=2+2.
    generic_budget = 2 + 1 + 1
    node_budget = 2 + 2
    require(generic_budget == node_budget == 4, "quartic sheet-budget equality")

    # For h=1 and n4=0, e(U)=2-m where m=#T31 when T31 is finite.  Compare
    # with e(U)=e(C)+Q, Q>=0.
    ruling_rows: list[dict[str, int | str]] = []
    for m_t31 in range(0, 5):
        e_u = 2 - m_t31
        for base, e_base in (("A1", 1), ("P1", 2)):
            q_value = e_u - e_base
            if q_value >= 0:
                ruling_rows.append(
                    {"base": base, "m_t31": m_t31, "Q": q_value, "e_U": e_u}
                )
    require(
        ruling_rows
        == [
            {"base": "A1", "m_t31": 0, "Q": 1, "e_U": 2},
            {"base": "P1", "m_t31": 0, "Q": 0, "e_U": 2},
            {"base": "A1", "m_t31": 1, "Q": 0, "e_U": 1},
        ],
        "exact minimal-cycle ruling rows",
    )

    # Spectator family: (s,w) |-> (s, w^4-2w^2+sw).  Its ramification is
    # s=4w-4w^3 and branch parametrization is
    # (s,y)=(4t-4t^3, 2t^2-3t^4).
    # Node t=+/-1: w^4-2w^2+1=(w-1)^2(w+1)^2.
    rational = lambda value: (Fraction(value), Fraction(0))
    node_coefficients = tuple(
        rational(value) for value in (1, 0, -2, 0, 1)
    )
    node_factor_coefficients = polynomial_product(
        (rational(-1), rational(1)),
        polynomial_product(
            (rational(-1), rational(1)),
            polynomial_product(
                (rational(1), rational(1)),
                (rational(1), rational(1)),
            ),
        ),
    )
    require(node_coefficients == node_factor_coefficients, "spectator node factorization")

    # At either cusp r^2=1/3:
    # w^4-2w^2+(8r/3)w-1/3=(w-r)^3(w+3r).
    # Coefficients are represented as a+b*r with r^2=1/3.
    cusp_left = (
        (Fraction(-1, 3), Fraction(0)),
        (Fraction(0), Fraction(8, 3)),
        (Fraction(-2), Fraction(0)),
        (Fraction(0), Fraction(0)),
        (Fraction(1), Fraction(0)),
    )
    minus_r = (Fraction(0), Fraction(-1))
    plus_three_r = (Fraction(0), Fraction(3))
    cusp_right = polynomial_product(
        (minus_r, rational(1)),
        polynomial_product(
            (minus_r, rational(1)),
            polynomial_product(
                (minus_r, rational(1)),
                (plus_three_r, rational(1)),
            ),
        ),
    )
    require(cusp_left == cusp_right, "spectator cusp factorization coefficients")

    # The written difference-factor proof gives exactly one node and the
    # derivative determinant gives exactly two ordinary cusps.  These counts
    # imply e(U)=2-2=0, agreeing with U=A1 x Gm.
    spectator = {
        "h": 1,
        "k": 1,
        "beta1_B": 1,
        "n22": 1,
        "n4": 0,
        "n31": 2,
        "e_U": 0,
        "monodromy_order": 24,
        "unit_rank_at_least": 1,
    }
    require(spectator["e_U"] == 2 - spectator["n31"], "spectator Euler ledger")
    require(spectator["e_U"] < 1, "spectator fails the proper-block ruling gate")

    payload = {
        "status": "PASS-QUARTIC-MINIMAL-CYCLE-THREAT-MAP",
        "s4_transpositions": len(transpositions),
        "node_matchings": len(matchings),
        "node_transporter_group_orders": transporter_orders,
        "resolvent_node_rows": resolvent_node_rows,
        "ordered_cusp_packets": len(cusp_packets),
        "cusp_node_s4_packets": len(combined_orders),
        "nodal_control_meridian_images_transitive": False,
        "generic_sheet_budget": generic_budget,
        "node_sheet_budget": node_budget,
        "proper_block_ruling_rows": ruling_rows,
        "spectator": spectator,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    print(json.dumps(payload, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
