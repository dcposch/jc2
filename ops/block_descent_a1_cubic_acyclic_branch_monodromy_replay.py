#!/usr/bin/env python3
"""Desk replay for the acyclic-branch cubic monodromy obstruction.

The geometric input is external: the Lin--Zaidenberg reduced acyclic-curve
classification leaves a comb or a weighted-homogeneous cone.  This script
checks only the finite S3 consequences used after that classification:

* in a comb, the spine meridian is central in the product complement group;
  its transposition image therefore confines the full image to its order-two
  centralizer;
* in a cone, the one local companion-fixing image has order two;
* two independently labelled companion neighborhoods can instead generate
  S3, reproducing the charged disconnected-branch warning.

No curve classification, complement presentation, or cover realization is
encoded here.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from itertools import product, permutations


Permutation = tuple[int, int, int]
IDENTITY: Permutation = (0, 1, 2)


def compose(left: Permutation, right: Permutation) -> Permutation:
    return tuple(left[right[index]] for index in range(3))  # type: ignore[return-value]


def generated(generators: tuple[Permutation, ...]) -> set[Permutation]:
    closure = {IDENTITY}
    changed = True
    while changed:
        changed = False
        for left in tuple(closure | set(generators)):
            for right in tuple(closure | set(generators)):
                value = compose(left, right)
                if value not in closure:
                    closure.add(value)
                    changed = True
    return closure


def orbit(group: set[Permutation], point: int) -> set[int]:
    return {element[point] for element in group}


def cycle_type(perm: Permutation) -> tuple[int, ...]:
    unseen = set(range(3))
    lengths: list[int] = []
    while unseen:
        current = min(unseen)
        length = 0
        while current in unseen:
            unseen.remove(current)
            current = perm[current]
            length += 1
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mutate-drop-comb-centrality",
        action="store_true",
        help="deliberately allow tooth images not commuting with the spine",
    )
    args = parser.parse_args()

    s3 = tuple(permutations(range(3)))
    transpositions = tuple(p for p in s3 if cycle_type(p) == (2, 1))
    require(len(transpositions) == 3, "S3 must contain exactly three transpositions")

    comb_counts: dict[str, int] = {}
    for tooth_count in range(1, 7):
        admissible = []
        for spine in transpositions:
            for teeth in product(transpositions, repeat=tooth_count):
                centrality = all(
                    compose(spine, tooth) == compose(tooth, spine)
                    for tooth in teeth
                )
                if args.mutate_drop_comb_centrality:
                    centrality = True
                if centrality:
                    admissible.append((spine, teeth))

        require(
            len(admissible) == 3,
            f"comb with {tooth_count} teeth must have one common transposition label",
        )
        for spine, teeth in admissible:
            image = generated((spine, *teeth))
            require(len(image) == 2, "an admissible comb image must have order two")
            require(
                len(orbit(image, 0)) < 3,
                "an admissible comb image cannot act transitively on three sheets",
            )
        comb_counts[str(tooth_count)] = len(admissible)

    for transposition in transpositions:
        cone_image = generated((transposition,))
        require(len(cone_image) == 2, "a cone-local companion image must have order two")
        require(
            len(orbit(cone_image, 0)) < 3,
            "a cone-local companion image cannot be transitive",
        )

    disconnected_control = generated((transpositions[0], transpositions[1]))
    require(
        len(disconnected_control) == 6,
        "two distinct independently based transpositions must generate S3",
    )
    require(
        len(orbit(disconnected_control, 0)) == 3,
        "the disconnected warning control must be transitive",
    )

    payload = {
        "status": "PASS-CUBIC-ACYCLIC-BRANCH-MONODROMY",
        "s3_order": len(s3),
        "transposition_count": len(transpositions),
        "comb_admissible_counts_by_teeth": comb_counts,
        "cone_image_order": 2,
        "acyclic_images_transitive": False,
        "disconnected_control_image_order": len(disconnected_control),
        "disconnected_control_transitive": True,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    print(json.dumps(payload, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
