#!/usr/bin/env python3
"""Deterministic replay for the R1 two-component splice-colouring census at n22=1.

The written report supplies Chau's unique infinite point, the one-place
genus identity on each component, Eisenbud--Neumann splice form, and the
Zariski--van Kampen quotient from the link at infinity to the affine
complement.  This script checks only finite group arithmetic: trefoil
transposition pairs, closed-braid colourings of the bounded splice
families, the charged (12)|(34) node pairing, and the V4->S4->S3 lift
cross-check on the surviving 3-braid.

Mutation control (must exit nonzero):
  --mutate-kill-trefoil-unknot
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from typing import Iterable


Permutation = tuple[int, ...]
BraidWord = tuple[int, ...]
S4_ORDER = 24
IDENTITY: Permutation = (0, 1, 2, 3)


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


TRANSPOSITIONS: tuple[Permutation, ...] = tuple(
    transposition(first, second)
    for first in range(4)
    for second in range(first + 1, 4)
)
PAIR_ALIGNED: tuple[Permutation, Permutation] = (
    transposition(0, 1),
    transposition(2, 3),
)
PAIR_SET = frozenset(PAIR_ALIGNED)


def generated_subgroup(generators: Iterable[Permutation]) -> frozenset[Permutation]:
    gens = tuple(generators)
    require(len(gens) > 0, "empty generator list")
    subgroup = {IDENTITY}
    frontier = [IDENTITY]
    while frontier:
        current = frontier.pop()
        for generator in gens:
            candidate = compose(current, generator)
            if candidate not in subgroup:
                subgroup.add(candidate)
                frontier.append(candidate)
    return frozenset(subgroup)


def cycle_type(permutation: Permutation) -> tuple[int, ...]:
    unseen = set(range(len(permutation)))
    lengths: list[int] = []
    while unseen:
        current = min(unseen)
        length = 0
        while current in unseen:
            unseen.remove(current)
            current = permutation[current]
            length += 1
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def overlapping(first: Permutation, second: Permutation) -> bool:
    return first != second and cycle_type(compose(first, second)) == (3, 1)


def disjoint_pair(first: Permutation, second: Permutation) -> bool:
    return first != second and compose(first, second) == compose(second, first)


def permutation_name(permutation: Permutation) -> str:
    moved = [index for index in range(len(permutation)) if permutation[index] != index]
    if len(moved) == 2:
        return f"({moved[0] + 1}{moved[1] + 1})"
    return str(permutation)


def artin_generator(colors: tuple[Permutation, ...], generator: int) -> tuple[Permutation, ...]:
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


def braid_action(colors: tuple[Permutation, ...], word: BraidWord) -> tuple[Permutation, ...]:
    result = colors
    for generator in word:
        result = artin_generator(result, generator)
    return result


def signed_power(word: BraidWord, exponent: int) -> BraidWord:
    if exponent >= 0:
        return word * exponent
    return tuple(-generator for generator in reversed(word)) * abs(exponent)


def strand_permutation(strands: int, word: BraidWord) -> Permutation:
    result = tuple(range(strands))
    for generator in word:
        index = abs(generator) - 1
        adjacent = list(range(strands))
        adjacent[index], adjacent[index + 1] = adjacent[index + 1], adjacent[index]
        if generator > 0:
            result = compose(result, tuple(adjacent))
        else:
            result = compose(result, inverse(tuple(adjacent)))
    return result


def cycle_decomposition(permutation: Permutation) -> tuple[tuple[int, ...], ...]:
    unseen = set(range(len(permutation)))
    cycles: list[tuple[int, ...]] = []
    while unseen:
        current = min(unseen)
        cycle: list[int] = []
        while current in unseen:
            unseen.remove(current)
            cycle.append(current)
            current = permutation[current]
        cycles.append(tuple(cycle))
    return tuple(sorted(cycles, key=lambda cycle: (len(cycle), cycle)))


def block_switch_word(winding: int) -> BraidWord:
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


def two_cable_of_two_braid_word(companion_exponent: int, meridional: int) -> BraidWord:
    switch = block_switch_word(2)
    companion = signed_power(switch, companion_exponent)
    correction = meridional - 2 * companion_exponent
    return companion + signed_power((1,), correction)


# --- Fox / V4 lift, used as a 3-strand cross-check ---

PARTITIONS = (
    frozenset((frozenset((0, 1)), frozenset((2, 3)))),
    frozenset((frozenset((0, 2)), frozenset((1, 3)))),
    frozenset((frozenset((0, 3)), frozenset((1, 2)))),
)


def quotient_action(permutation: Permutation) -> Permutation:
    images = []
    for partition in PARTITIONS:
        image = frozenset(
            frozenset(permutation[value] for value in pair) for pair in partition
        )
        images.append(PARTITIONS.index(image))
    return tuple(images)


def fox_action_vector(colors: tuple[int, ...], generator: int) -> tuple[int, ...]:
    index = abs(generator) - 1
    result = list(colors)
    first, second = result[index], result[index + 1]
    if generator > 0:
        result[index], result[index + 1] = (2 * first - second) % 3, first
    else:
        result[index], result[index + 1] = second, (2 * second - first) % 3
    return tuple(result)


def fox_action(colors: tuple[int, ...], word: BraidWord) -> tuple[int, ...]:
    result = colors
    for generator in word:
        result = fox_action_vector(result, generator)
    return result


def transposition_to_fox(permutation: Permutation) -> int:
    quotient = quotient_action(permutation)
    fixed = [index for index, image in enumerate(quotient) if index == image]
    require(len(fixed) == 1, "transposition Fox colour is not a transposition of S3")
    return fixed[0]


def count_closed_colorings(
    strands: int, word: BraidWord
) -> tuple[int, int, tuple[tuple[Permutation, ...], ...]]:
    closed = 0
    full_s4 = 0
    witnesses: list[tuple[Permutation, ...]] = []
    for colors in itertools.product(TRANSPOSITIONS, repeat=strands):
        if braid_action(colors, word) != colors:
            continue
        closed += 1
        if len(generated_subgroup(colors)) == S4_ORDER:
            full_s4 += 1
            if len(witnesses) < 8:
                witnesses.append(colors)
    return closed, full_s4, tuple(witnesses)


def f1_word(cusp_sign: int, link_sign: int, linking: int) -> BraidWord:
    require(linking >= 0, "linking is a nonnegative integer")
    require(cusp_sign in (-1, 1) and link_sign in (-1, 1), "signs are +/-1")
    return signed_power((1,), 3 * cusp_sign) + signed_power((2,), 2 * linking * link_sign)


def f3_word(cusp_sign: int, link_sign: int, linking: int) -> BraidWord:
    return signed_power((1,), 5 * cusp_sign) + signed_power((2,), 2 * linking * link_sign)


def f1_stage_b_counts(word: BraidWord) -> dict[str, int | str | list[str]]:
    """Infinity closed + individual cusp factor + ordinary mixed twist + pairing."""

    cusp = tuple(generator for generator in word if abs(generator) == 1)
    mixed = tuple(generator for generator in word if abs(generator) == 2)
    twist = mixed[:2] if mixed else ()
    closed = 0
    full_s4 = 0
    overlapping_s4 = 0
    charged = 0
    charged_s4 = 0
    witness: tuple[Permutation, ...] | None = None
    for colors in itertools.product(TRANSPOSITIONS, repeat=3):
        if braid_action(colors, word) != colors:
            continue
        closed += 1
        if twist and braid_action(colors, twist) != colors:
            continue
        if cusp and braid_action(colors, cusp) != colors:
            continue
        if not overlapping(colors[0], colors[1]):
            continue
        is_s4 = len(generated_subgroup(colors)) == S4_ORDER
        if is_s4:
            full_s4 += 1
            overlapping_s4 += 1
        charged_here = any(frozenset((arm, colors[2])) == PAIR_SET for arm in colors[:2])
        if charged_here:
            charged += 1
            if is_s4:
                charged_s4 += 1
                if witness is None:
                    witness = colors
    payload: dict[str, int | str | list[str]] = {
        "closed_and_affine": closed,
        "overlapping_s4": overlapping_s4,
        "charged_pairing": charged,
        "charged_pairing_s4": charged_s4,
    }
    if witness is not None:
        payload["witness"] = [permutation_name(item) for item in witness]
        payload["full_s4"] = int(len(generated_subgroup(witness)) == S4_ORDER)
    return payload


def trefoil_pair_census() -> dict[str, int]:
    equal = 0
    overlap = 0
    disjoint_rel = 0
    disjoint_fail = 0
    for first, second in itertools.product(TRANSPOSITIONS, repeat=2):
        left = compose(compose(first, second), first)
        right = compose(compose(second, first), second)
        if left != right:
            if disjoint_pair(first, second):
                disjoint_fail += 1
            continue
        if first == second:
            equal += 1
        elif overlapping(first, second):
            overlap += 1
        elif disjoint_pair(first, second):
            disjoint_rel += 1
    return {
        "equal": equal,
        "overlapping": overlap,
        "disjoint_satisfying_relation": disjoint_rel,
        "disjoint_failing_relation": disjoint_fail,
    }


def fox_s4_count(strands: int, word: BraidWord) -> int:
    """Labelled full-S4 count via Fox S3 colourings and transposition lifts."""

    buckets: dict[int, list[Permutation]] = {0: [], 1: [], 2: []}
    for item in TRANSPOSITIONS:
        buckets[transposition_to_fox(item)].append(item)
    require(all(len(bucket) == 2 for bucket in buckets.values()), "two lifts per Fox colour")
    ordered: dict[int, tuple[Permutation, Permutation]] = {
        colour: (bucket[0], bucket[1]) if bucket[0] <= bucket[1] else (bucket[1], bucket[0])
        for colour, bucket in buckets.items()
    }
    total = 0
    for fox in itertools.product(range(3), repeat=strands):
        if len(set(fox)) == 1:
            continue
        if fox_action(fox, word) != fox:
            continue
        for bits in itertools.product(range(2), repeat=strands):
            colors = tuple(ordered[fox[index]][bits[index]] for index in range(strands))
            if braid_action(colors, word) != colors:
                continue
            if len(generated_subgroup(colors)) == S4_ORDER:
                total += 1
    return total


def action_order(strands: int, word: BraidWord) -> int:
    """Order of a braid word acting on transposition tuples."""

    states = tuple(itertools.product(TRANSPOSITIONS, repeat=strands))
    index_of = {state: index for index, state in enumerate(states)}
    perm = tuple(index_of[braid_action(state, word)] for state in states)
    unseen = set(range(len(perm)))
    order = 1
    while unseen:
        start = min(unseen)
        length = 0
        current = start
        while current in unseen:
            unseen.remove(current)
            current = perm[current]
            length += 1
        order = order * length // gcd_int(order, length)
    return order


def gcd_int(left: int, right: int) -> int:
    while right:
        left, right = right, left % right
    return abs(left)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mutate-kill-trefoil-unknot",
        action="store_true",
        help="incorrectly demand that every F1 trefoil-unknot colouring is empty",
    )
    args = parser.parse_args()

    # Lemma: trefoil transposition meridians are equal or overlapping, never
    # a disjoint (2,2) pairing.  This kills charging (1,1).
    trefoil = trefoil_pair_census()
    require(trefoil["equal"] == 6, "six equal transposition pairs on the trefoil")
    require(trefoil["overlapping"] == 24, "twenty-four ordered overlapping trefoil pairs")
    require(trefoil["disjoint_satisfying_relation"] == 0, "a disjoint pair cannot colour a trefoil")
    require(trefoil["disjoint_failing_relation"] == 6, "six ordered disjoint pairs exist in S4")

    pair_group = generated_subgroup(PAIR_ALIGNED)
    require(len(pair_group) == 4, "pairing group is C2xC2")
    overlapping_with_node = generated_subgroup(
        (PAIR_ALIGNED[0], PAIR_ALIGNED[1], transposition(0, 2))
    )
    require(len(overlapping_with_node) == S4_ORDER, "cusp packet plus pairing generates S4")

    # Two transpositions never generate S4, so every 2-strand diagram dies.
    two_strand_orders = set()
    for first, second in itertools.product(TRANSPOSITIONS, repeat=2):
        two_strand_orders.add(len(generated_subgroup((first, second))))
    require(S4_ORDER not in two_strand_orders, "two transpositions generated S4")
    require(two_strand_orders <= {1, 2, 4, 6}, "unexpected two-generator image")

    torus_link_rows: list[dict[str, object]] = []
    for linking in range(1, 5):
        word = signed_power((1,), 2 * linking)
        closed, full_s4, _ = count_closed_colorings(2, word)
        perm = strand_permutation(2, word)
        require(full_s4 == 0, "T(2,2n) acquired an S4 colouring")
        torus_link_rows.append(
            {
                "id": f"T(2,{2 * linking})",
                "strands": 2,
                "components": [list(cycle) for cycle in cycle_decomposition(perm)],
                "closed": closed,
                "s4": full_s4,
                "verdict": "empty",
            }
        )

    # F1: trefoil cup unknot.  Linking n is unbounded, but sigma2 acts on the
    # finite set of 6^3 transposition triples, so only finitely many distinct
    # colouring problems.  Stage B imposes the ordinary mixed twist sigma2^{+/-2}
    # and is therefore independent of n.
    sigma2_order = action_order(3, (2,))
    require(sigma2_order >= 1, "sigma2 action order")
    require(sigma2_order <= 6 ** 3, "sigma2 order exploded")
    # sigma2^{2n} depends on 2n mod sigma2_order.  Residues n=1..sigma2_order
    # cover every even exponent.
    f1_residues = tuple(range(1, sigma2_order + 1))
    require(len(f1_residues) <= 216, "F1 residue list too long")

    f1_summary_rows: list[dict[str, object]] = []
    f1_witness: list[str] | None = None
    charged_values: list[int] = []
    overlapping_values: list[int] = []
    for cusp_sign, link_sign in itertools.product((-1, 1), (-1, 1)):
        stage_b_n1 = f1_stage_b_counts(f1_word(cusp_sign, link_sign, 1))
        charged_s4 = int(stage_b_n1["charged_pairing_s4"])
        overlapping_s4 = int(stage_b_n1["overlapping_s4"])
        if args.mutate_kill_trefoil_unknot:
            require(charged_s4 == 0, "mutation rejected: F1 trefoil-unknot is colourable")
        require(charged_s4 == 8, f"F1 charged S4 count drifted at signs={(cusp_sign, link_sign)}")
        require(overlapping_s4 == 24, "F1 overlapping S4 count drifted")
        charged_values.append(charged_s4)
        overlapping_values.append(overlapping_s4)
        if f1_witness is None and "witness" in stage_b_n1:
            f1_witness = list(stage_b_n1["witness"])  # type: ignore[arg-type]
        stage_a_by_residue: list[int] = []
        for linking in f1_residues:
            word = f1_word(cusp_sign, link_sign, linking)
            perm = strand_permutation(3, word)
            require(len(cycle_decomposition(perm)) == 2, "F1 braid is not two-component")
            _closed, stage_a_s4, _ = count_closed_colorings(3, word)
            stage_b = f1_stage_b_counts(word)
            require(int(stage_b["charged_pairing_s4"]) == charged_s4, "F1 stage B depended on n")
            stage_a_by_residue.append(stage_a_s4)
        require(min(stage_a_by_residue) >= 24, "F1 stage A emptied on a residue")
        f1_summary_rows.append(
            {
                "id": f"F1[c={cusp_sign},lk={link_sign}]",
                "charging": "(1,0)-mixed",
                "strands": 3,
                "stage_a_s4_by_residue": stage_a_by_residue,
                "stage_b_charged_s4": charged_s4,
                "verdict": "colourable",
            }
        )
    require(f1_witness == ["(13)", "(12)", "(34)"], f"unexpected F1 witness {f1_witness}")
    fox_n1 = fox_s4_count(3, f1_word(1, 1, 1))
    require(fox_n1 == 24, "Fox/V4 lift disagrees with the F1 n=1 stage-A S4 count")

    # F3: pentafoil cup unknot, charging (2,0).  Empty at stage A.
    f3_rows: list[dict[str, object]] = []
    f3_residues = tuple(range(1, min(sigma2_order, 6) + 1))
    for cusp_sign, link_sign, linking in itertools.product((-1, 1), (-1, 1), f3_residues):
        word = f3_word(cusp_sign, link_sign, linking)
        closed, full_s4, _ = count_closed_colorings(3, word)
        require(full_s4 == 0, "F3 acquired an S4 colouring")
        f3_rows.append(
            {
                "id": f"F3[c={cusp_sign},lk={link_sign},n={linking}]",
                "charging": "(2,0)",
                "stage_a_closed": closed,
                "stage_a_s4": full_s4,
                "verdict": "empty",
            }
        )

    # C(2,+/-1) of a trefoil, union an unknot.  Charging (2,0).  Empty at stage A.
    satellite_rows: list[dict[str, object]] = []
    for companion, meridional, linking in itertools.product((3, -3), (1, -1), (1, 2)):
        knot_word = two_cable_of_two_braid_word(companion, meridional)
        word = knot_word + signed_power((4,), 2 * linking)
        closed, full_s4, _ = count_closed_colorings(5, word)
        require(full_s4 == 0, "C(2,+/-1)(trefoil) cup unknot acquired S4")
        satellite_rows.append(
            {
                "id": f"C(2,{meridional})(T(2,{companion}))U[n={linking}]",
                "charging": "(2,0)",
                "strands": 5,
                "stage_a_closed": closed,
                "stage_a_s4": full_s4,
                "verdict": "empty",
            }
        )

    # T(4,+/-6): two trefoils.  Stage A has S4, but no cusp-on-one plus
    # pairing-on-the-other.  Lemma B already kills (1,1); this is the
    # explicit torus-link control.
    t46_rows: list[dict[str, object]] = []
    for exponent in (6, -6):
        word = signed_power((1, 2, 3), exponent)
        perm = strand_permutation(4, word)
        components = cycle_decomposition(perm)
        require(len(components) == 2, "T(4,6) is not two-component")
        closed, full_s4, _ = count_closed_colorings(4, word)
        left, right = components
        cusp_node = 0
        for colors in itertools.product(TRANSPOSITIONS, repeat=4):
            if braid_action(colors, word) != colors:
                continue
            if len(generated_subgroup(colors)) != S4_ORDER:
                continue
            left_pair = (colors[left[0]], colors[left[1]])
            right_pair = (colors[right[0]], colors[right[1]])
            if overlapping(*left_pair) and disjoint_pair(*right_pair):
                cusp_node += 1
            if overlapping(*right_pair) and disjoint_pair(*left_pair):
                cusp_node += 1
        require(full_s4 == 72, "T(4,6) stage-A S4 count drifted")
        require(cusp_node == 0, "T(4,6) realized cusp-plus-pairing on opposite components")
        t46_rows.append(
            {
                "id": f"T(4,{exponent})",
                "charging": "(1,1)",
                "strands": 4,
                "stage_a_closed": closed,
                "stage_a_s4": full_s4,
                "cusp_plus_pairing": cusp_node,
                "verdict": "empty",
            }
        )

    # T(4,+/-10): two pentafoils, overfills the delta budget and is empty.
    t410_rows: list[dict[str, object]] = []
    for exponent in (10, -10):
        word = signed_power((1, 2, 3), exponent)
        closed, full_s4, _ = count_closed_colorings(4, word)
        require(full_s4 == 0, "T(4,10) acquired S4")
        t410_rows.append(
            {
                "id": f"T(4,{exponent})",
                "charging": "overfill-(2,2)",
                "stage_a_s4": full_s4,
                "verdict": "empty",
            }
        )

    colourable = [row["id"] for row in f1_summary_rows]
    empty_ids = (
        [row["id"] for row in torus_link_rows]
        + [row["id"] for row in f3_rows]
        + [row["id"] for row in satellite_rows]
        + [row["id"] for row in t46_rows]
        + [row["id"] for row in t410_rows]
    )
    require(len(colourable) == 4, "F1 sign-combination count")
    require(all(row["verdict"] == "colourable" for row in f1_summary_rows), "F1 verdict")
    require(len(empty_ids) > 0, "empty list vanished")

    payload = {
        "status": "PASS-RANK4-R1-SPLICE-COLORING",
        "provisional_row": "R1",
        "n22": 1,
        "trefoil_pair_census": trefoil,
        "two_transposition_orders": sorted(two_strand_orders),
        "sigma2_action_order_on_triples": sigma2_order,
        "f1_charged_pairing_s4": 8,
        "f1_overlapping_s4": 24,
        "f1_witness": f1_witness,
        "f1_fox_v4_s4_n1": fox_n1,
        "colourable_family": "F1-trefoil-unknot",
        "colourable_sign_rows": len(colourable),
        "empty_count": len(empty_ids),
        "families": {
            "T(2,2n)": torus_link_rows,
            "F1": f1_summary_rows,
            "F3": f3_rows,
            "C21_union_unknot": satellite_rows,
            "T(4,6)": t46_rows,
            "T(4,10)": t410_rows,
        },
        "charging_verdicts": {
            "(1,0)-mixed": "colourable",
            "(1,1)-self-node-on-trefoil": "empty",
            "(2,0)-cusp-and-node-on-one-component": "empty",
        },
        "unbounded_direction": "linking_n_of_F1_core_T(2,2n)",
        "bounded_slice": "transposition_colouring_types_modulo_sigma2_action",
    }
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    digest = hashlib.sha256(encoded.encode("utf-8")).hexdigest()
    print(encoded)
    print(f"payload_sha256={digest}")
    print(f"status={payload['status']}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as error:
        print(f"FAIL:{error}")
        raise SystemExit(1)
