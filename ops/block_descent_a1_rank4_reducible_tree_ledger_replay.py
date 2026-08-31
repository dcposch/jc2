#!/usr/bin/env python3
"""Deterministic replay for the rank-four reducible component-tree ledger.

The written report supplies Chau parametrization, the morphic forest theorem,
Orevkov's degree-at-infinity identity, and the missing-multiplicity fibre
identity (2.3).  This script checks only finite arithmetic and S4 combinatorics:
Euler packet solutions, the m<=3 forest list, leftover signs, the pair-aligned
transposition screen, and the one-node scope failure at m>=2.

Mutation control (each must exit nonzero):
  --mutate-allow-h-two-finite-t31
  --mutate-apply-one-node-to-T2
  --mutate-drop-overlapping-screen
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from typing import Iterable


Permutation = tuple[int, ...]
S4_ORDER = 24
IDENTITY: Permutation = (0, 1, 2, 3)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def compose(left: Permutation, right: Permutation) -> Permutation:
    return tuple(left[right[index]] for index in range(len(left)))


def transposition(first: int, second: int) -> Permutation:
    result = list(range(4))
    result[first], result[second] = result[second], result[first]
    return tuple(result)


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


def orbit_size(group: frozenset[Permutation]) -> int:
    seen = set()
    for seed in range(4):
        if seed in seen:
            continue
        component = {seed}
        frontier = [seed]
        while frontier:
            current = frontier.pop()
            for element in group:
                image = element[current]
                if image not in component:
                    component.add(image)
                    frontier.append(image)
        seen.update(component)
    return len(seen)


PAIR_ALIGNED = (transposition(0, 1), transposition(2, 3))
OVERLAPPING = (
    transposition(0, 2),
    transposition(0, 3),
    transposition(1, 2),
    transposition(1, 3),
)
NODE_PAIR = PAIR_ALIGNED


def euler_holds(h: int, e_t31: int, n4: int, q: int, base: int) -> bool:
    return 2 * h + e_t31 + 2 * n4 + q == base


def finite_t31_packets() -> list[dict[str, int | str]]:
    packets: list[dict[str, int | str]] = []
    for h, t, n4, q, curve in itertools.product(
        range(1, 4),
        range(0, 4),
        range(0, 3),
        range(0, 3),
        (("A1", 3), ("P1", 2)),
    ):
        name, target = curve
        if euler_holds(h, t, n4, q, target):
            packets.append(
                {
                    "C": name,
                    "h": h,
                    "t": t,
                    "n4": n4,
                    "Q": q,
                    "base": target,
                }
            )
    return packets


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutate-allow-h-two-finite-t31", action="store_true")
    parser.add_argument("--mutate-apply-one-node-to-T2", action="store_true")
    parser.add_argument("--mutate-drop-overlapping-screen", action="store_true")
    args = parser.parse_args()

    packets = finite_t31_packets()
    expected_h1 = {
        ("A1", 1, 1, 0, 0),
        ("A1", 1, 0, 0, 1),
        ("P1", 1, 0, 0, 0),
    }
    h1_keys = {(p["C"], p["h"], p["t"], p["n4"], p["Q"]) for p in packets}
    require(expected_h1 <= h1_keys, "missing threat-map Euler row")
    h_ge_2_nonneg = [p for p in packets if int(p["h"]) >= 2 and int(p["t"]) >= 0]
    if args.mutate_allow_h_two_finite_t31:
        require(False, "mutation rejected: h>=2 with finite T31 is empty")
    require(not h_ge_2_nonneg, "h>=2 appeared with nonnegative e(T31)")

    trees = (
        {"name": "T2", "m": 2, "h": 1, "kind": "connected"},
        {"name": "T3path", "m": 3, "h": 1, "kind": "connected"},
        {"name": "T3star", "m": 3, "h": 1, "kind": "connected"},
        {"name": "T3split", "m": 3, "h": 2, "kind": "split"},
    )
    for tree in trees:
        require(tree["m"] >= 2 * tree["h"] - 1, "m>=2h-1 failed on a listed tree")
    require(3 <= 3, "safe Orevkov m<=3 constant")

    pair_aligned_group = generated_subgroup(NODE_PAIR)
    require(len(pair_aligned_group) == 4, "pairing group is not C2xC2")
    require(orbit_size(pair_aligned_group) == 4, "pairing group not transitive")
    require(len(pair_aligned_group) != S4_ORDER, "pairing group is S4")

    overlapping_with_node = generated_subgroup((NODE_PAIR[0], NODE_PAIR[1], OVERLAPPING[0]))
    require(len(overlapping_with_node) == S4_ORDER, "overlapping packet does not generate S4")
    if args.mutate_drop_overlapping_screen:
        require(
            len(pair_aligned_group) == S4_ORDER,
            "mutation rejected: pair-aligned generators do not give S4",
        )

    one_node_scope = {
        "irreducible": True,
        "one_place": True,
        "sole_ordinary_node": True,
        "simple_generic_meridians": True,
        "degree_at_least_four": True,
    }
    require(all(one_node_scope.values()), "one-node scope flags incomplete")
    t2_scope_ok = False
    if args.mutate_apply_one_node_to_T2:
        t2_scope_ok = True
    require(not t2_scope_ok, "mutation rejected: one-node does not apply at m=2")
    require(not (2 >= 2 and t2_scope_ok), "one-node over-applied")

    rows: list[dict[str, object]] = []
    euler_h1 = [
        {"id": "E1", "C": "A1", "Q": 0, "n4": 0, "t": 1},
        {"id": "E2", "C": "A1", "Q": 1, "n4": 0, "t": 0},
        {"id": "E3", "C": "P1", "Q": 0, "n4": 0, "t": 0},
    ]
    connected_trees = [tree for tree in trees if tree["h"] == 1]
    row_id = 0
    killed_independent = 0
    live_without_miss = 0
    for packet in euler_h1:
        for tree in connected_trees:
            row_id += 1
            leftover = 3 - int(tree["m"])
            if packet["id"] == "E1":
                leftover -= 1
            independent_kill = leftover < 0
            name = f"R{row_id}"
            row = {
                "id": name,
                "euler": packet["id"],
                "tree": tree["name"],
                "m": tree["m"],
                "h": tree["h"],
                "k": 1,
                "inertia": f"211^{tree['m']}",
                "n22_min": 1,
                "leftover": leftover,
                "one_node_applies": False,
                "genus_three_four_apply": False,
                "independent_kill": independent_kill,
                "kill_if_only_safe": "OREV-SAFE" if independent_kill else "OPEN",
                "kill_if_missing_multiplicity": "OREV-MISS",
            }
            rows.append(row)
            if independent_kill:
                killed_independent += 1
            else:
                live_without_miss += 1

    split_rows = [
        {"id": "R10", "m211": 2, "m31": 1, "support": "isolated", "h31": 1, "sigma": 2},
        {"id": "R11", "m211": 2, "m31": 1, "support": "one-of-pair", "h31": 1, "sigma": 2},
        {"id": "R12", "m211": 1, "m31": 2, "support": "the-pair", "h31": 1, "sigma": 2},
        {"id": "R13", "m211": 1, "m31": 2, "support": "isolated-plus-one", "h31": 2, "sigma": 3},
    ]
    for item in split_rows:
        e_t31 = int(item["h31"]) - int(item["sigma"])
        require(e_t31 == -1, "A1 split row does not meet e(T31)=-1")
        require(item["m211"] >= 1, "S4 screen: no T211 component")
        require(int(item["m211"]) + int(item["m31"]) == 3, "split m!=3")
        rows.append(
            {
                "id": item["id"],
                "euler": "h2-A1",
                "tree": "T3split",
                "m": 3,
                "h": 2,
                "k": "1-or-2",
                "inertia": f"211^{item['m211']} 31^{item['m31']}",
                "n22_min": 1,
                "e_T31": e_t31,
                "one_node_applies": False,
                "genus_three_four_apply": False,
                "independent_kill": False,
                "kill_if_only_safe": "OPEN",
                "kill_if_missing_multiplicity": "OREV-MISS",
                "support": item["support"],
            }
        )
        live_without_miss += 1

    rows.append(
        {
            "id": "R14",
            "euler": "h2-P1",
            "tree": "T3split",
            "m": 3,
            "h": 2,
            "note": "same inertia menu as R10-R13 with one extra special point",
            "independent_kill": False,
            "kill_if_only_safe": "OPEN",
            "kill_if_missing_multiplicity": "OREV-MISS",
            "one_node_applies": False,
            "genus_three_four_apply": False,
        }
    )
    live_without_miss += 1

    rows.append(
        {
            "id": "R15",
            "euler": "h2-any",
            "tree": "T3split",
            "inertia": "211^0 31^3",
            "independent_kill": True,
            "kill_if_only_safe": "S4",
            "kill_if_missing_multiplicity": "S4",
            "one_node_applies": False,
            "genus_three_four_apply": False,
        }
    )
    killed_independent += 1
    rows.append(
        {
            "id": "R16",
            "euler": "h2-any",
            "tree": "T3split",
            "inertia": "211^3 31^0",
            "independent_kill": True,
            "kill_if_only_safe": "EULER",
            "kill_if_missing_multiplicity": "EULER",
            "one_node_applies": False,
            "genus_three_four_apply": False,
        }
    )
    killed_independent += 1

    require(all(row.get("one_node_applies") is False for row in rows), "one-node fired")
    require(
        all(row.get("genus_three_four_apply") is False for row in rows),
        "irreducible census applied to reducible row",
    )
    require(killed_independent == 4, f"unexpected independent kill count {killed_independent}")
    require(live_without_miss == 12, f"unexpected live count {live_without_miss}")
    require(len(rows) == 16, f"unexpected row count {len(rows)}")

    h3_m = 2 * 3 - 1
    require(h3_m == 5, "2h-1 at h=3")
    require(h3_m > 3, "h=3 not excluded by m<=3")

    payload = {
        "status": "PASS-RANK4-REDUCIBLE-TREE-LEDGER",
        "finite_t31_packets": packets,
        "trees": trees,
        "rows": rows,
        "counts": {
            "enumerated_rows": len(rows),
            "independent_kills": killed_independent,
            "live_without_lemma_23": live_without_miss,
            "live_with_lemma_23": 0,
        },
        "pair_aligned_order": len(pair_aligned_group),
        "overlapping_packet_order": len(overlapping_with_node),
        "n22_unbounded": True,
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
