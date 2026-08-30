#!/usr/bin/env python3
"""Desk replay for the exact R4-CYCLE-0 based-braid escape.

This checks a four-strand quasipositive braid factorization, its Hurwitz
transposition coloring, the disk-normalization permutation data, the unique
disjoint node packet, and the D4/S4 matching dichotomy.  It does not prove
global polynomial-A1 algebraization or existence of a Keller block.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from itertools import permutations


Permutation = tuple[int, ...]
S4_ID: Permutation = (0, 1, 2, 3)
STRAND_ID: Permutation = (0, 1, 2, 3)


def compose(left: Permutation, right: Permutation) -> Permutation:
    return tuple(left[right[index]] for index in range(len(left)))


def inverse(element: Permutation) -> Permutation:
    return tuple(element.index(index) for index in range(len(element)))


def conjugate(by: Permutation, element: Permutation) -> Permutation:
    return compose(compose(by, element), inverse(by))


def generated(generators: tuple[Permutation, ...]) -> frozenset[Permutation]:
    identity = tuple(range(len(generators[0])))
    closure = {identity, *generators}
    while True:
        products = {compose(left, right) for left in closure for right in closure}
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


def support(element: Permutation) -> frozenset[int]:
    return frozenset(index for index in range(len(element)) if element[index] != index)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def braid_inverse(word: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(-letter for letter in reversed(word))


def band(tail: tuple[int, ...], generator: int, power: int = 1) -> tuple[int, ...]:
    return tail + (generator,) * power + braid_inverse(tail)


def hurwitz_generator(
    labels: tuple[Permutation, ...], generator: int
) -> tuple[Permutation, ...]:
    """Right Hurwitz action; negative integers invoke the inverse action."""
    index = abs(generator) - 1
    left = labels[index]
    right = labels[index + 1]
    moved = list(labels)
    if generator > 0:
        moved[index] = conjugate(left, right)
        moved[index + 1] = left
    else:
        moved[index] = right
        moved[index + 1] = conjugate(inverse(right), left)
    return tuple(moved)


def hurwitz(
    labels: tuple[Permutation, ...], word: tuple[int, ...]
) -> tuple[Permutation, ...]:
    for generator in word:
        labels = hurwitz_generator(labels, generator)
    return labels


def strand_permutation(word: tuple[int, ...]) -> Permutation:
    result = list(STRAND_ID)
    for generator in word:
        index = abs(generator) - 1
        result[index], result[index + 1] = result[index + 1], result[index]
    return tuple(result)


def moved_edge(element: Permutation) -> frozenset[int]:
    return frozenset(index for index in range(4) if element[index] != index)


def graph_connected(edges: tuple[frozenset[int], ...]) -> bool:
    seen = {0}
    while True:
        expanded = set(seen)
        for edge in edges:
            if edge & seen:
                expanded |= edge
        if expanded == seen:
            return len(seen) == 4
        seen = expanded


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mutate-force-matching",
        action="store_true",
        help="replace the primitive base color by a matching-preserving one",
    )
    args = parser.parse_args()

    # Sheet labels use 0-based permutations: these are (34),(34),(23),(12)
    # in conventional 1-based notation.
    tau_34 = (0, 1, 3, 2)
    tau_23 = (0, 2, 1, 3)
    tau_12 = (1, 0, 2, 3)
    base_labels = (tau_34, tau_34, tau_23, tau_12)
    if args.mutate_force_matching:
        base_labels = (tau_34, tau_34, tau_12, tau_12)

    require(
        all(cycle_type(element) == (2, 1, 1) for element in base_labels),
        "every fibre meridian is a transposition",
    )
    require(
        len(generated(base_labels)) == 24,
        "the based meridian coloring has full S4 image",
    )

    # Three positive bands are the simple critical packets.  Their underlying
    # transpositions form the star 12,13,14, so the normalization covering is
    # connected.  In each band's local frame its two colors are equal.
    simple_specs = (
        ((), 1),
        ((2, 2, 2), 1),
        ((3, 2, 2, 2), 1),
    )
    simple_bands: list[tuple[int, ...]] = []
    simple_edges: list[frozenset[int]] = []
    local_simple_labels: list[list[list[int]]] = []
    for tail, generator in simple_specs:
        local = hurwitz(base_labels, tail)
        index = generator - 1
        require(
            local[index] == local[index + 1],
            "a simple branch band must collide equal rank-two labels",
        )
        factor = band(tail, generator)
        require(
            hurwitz(base_labels, factor) == base_labels,
            "each simple band is a van Kampen coloring relation",
        )
        edge = moved_edge(strand_permutation(factor))
        require(len(edge) == 2, "a positive band has transposition permutation")
        simple_bands.append(factor)
        simple_edges.append(edge)
        local_simple_labels.append([list(local[index]), list(local[index + 1])])

    require(graph_connected(tuple(simple_edges)), "simple-band graph is connected")
    require(
        frozenset(simple_edges)
        == frozenset(
            (
                frozenset((0, 1)),
                frozenset((0, 2)),
                frozenset((0, 3)),
            )
        ),
        "simple bands form the four-sheet star",
    )

    # One positive full-twist band is the conductor node.  In its local frame
    # the two colors are (34),(12), hence distinct and disjoint.
    node_tail = (2,)
    node_generator = 3
    node_local = hurwitz(base_labels, node_tail)
    node_index = node_generator - 1
    node_left = node_local[node_index]
    node_right = node_local[node_index + 1]
    require(node_left != node_right, "node labels are distinct")
    require(
        support(node_left).isdisjoint(support(node_right)),
        "node labels are disjoint rank-two factors",
    )
    node_band = band(node_tail, node_generator, power=2)
    require(
        hurwitz(base_labels, node_band) == base_labels,
        "the node full twist is a van Kampen coloring relation",
    )
    require(
        strand_permutation(node_band) == STRAND_ID,
        "a node does not branch the normalization projection",
    )

    # The three simple branch points give chi=4-3=1.  Their connected graph
    # and four-cycle boundary permutation make the normalization a disk.
    infinity_word = tuple(
        letter
        for factor in (*simple_bands, node_band)
        for letter in factor
    )
    infinity_permutation = strand_permutation(infinity_word)
    require(
        cycle_type(infinity_permutation) == (4,),
        "one boundary component / one normalization place at infinity",
    )
    require(
        hurwitz(base_labels, infinity_word) == base_labels,
        "the based infinity braid preserves the full coloring tuple",
    )
    normalization_euler = 4 - len(simple_bands)
    require(normalization_euler == 1, "normalization is a disk")

    # The node matching has stabilizer D4.  It is maximal in S4: any element
    # outside it upgrades D4 to S4.  The base color (23) is a literal cross
    # transposition, so this braid packet realizes the primitive overlap.
    matching = frozenset((support(node_left), support(node_right)))
    s4 = tuple(permutations(range(4)))
    d4 = tuple(
        element
        for element in s4
        if frozenset(
            frozenset(element[value] for value in part) for part in matching
        )
        == matching
    )
    require(len(d4) == 8, "perfect-matching stabilizer is D4")
    require(
        all(len(generated((node_left, node_right, element))) == 24 for element in s4 if element not in d4),
        "every outside transporter upgrades the node D4 to S4",
    )
    cross_labels = tuple(
        element
        for element in base_labels
        if support(element) not in matching
    )
    require(cross_labels == (tau_23,), "one exact primitive cross label")

    payload = {
        "status": "PASS-R4-CYCLE-0-BASED-BRAID-ESCAPE",
        "base_labels": [list(element) for element in base_labels],
        "monodromy_order": len(generated(base_labels)),
        "simple_band_words": [list(word) for word in simple_bands],
        "simple_edges": [sorted(edge) for edge in simple_edges],
        "local_simple_labels": local_simple_labels,
        "node_band_word": list(node_band),
        "node_local_labels": [list(node_left), list(node_right)],
        "normalization_euler": normalization_euler,
        "infinity_braid_word": list(infinity_word),
        "infinity_permutation": list(infinity_permutation),
        "matching_stabilizer_order": len(d4),
        "primitive_cross_labels": len(cross_labels),
        "global_polynomial_a1_algebraization_proved": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    print(json.dumps(payload, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
