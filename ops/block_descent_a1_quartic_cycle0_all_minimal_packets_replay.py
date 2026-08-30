#!/usr/bin/env python3
"""Desk replay for the universal minimal B4 cycle-zero packet obstruction.

The topology theorem (one-place polynomial links are graph knots) and the
Schubert genus formula are written interfaces, not encoded here.  This replay
checks the band-surface census and exhausts meridional transposition images of
the unknot/trefoil, the only graph knots of genus at most one.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math


Permutation = tuple[int, ...]


def compose(left: Permutation, right: Permutation) -> Permutation:
    """Return left after right."""

    return tuple(left[right[index]] for index in range(len(left)))


def identity(size: int) -> Permutation:
    return tuple(range(size))


def transposition(size: int, first: int, second: int) -> Permutation:
    result = list(range(size))
    result[first], result[second] = result[second], result[first]
    return tuple(result)


def generated_subgroup(generators: tuple[Permutation, ...]) -> frozenset[Permutation]:
    size = len(generators[0])
    subgroup = {identity(size)}
    frontier = [identity(size)]
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
        "--mutate-drop-full-s4",
        action="store_true",
        help="weaken the forbidden image threshold from S4 to S3",
    )
    args = parser.parse_args()

    strand_count = 4
    normalization_band_count = 3
    node_positive_band_count = 2
    total_positive_band_count = normalization_band_count + node_positive_band_count
    boundary_component_count = 1
    surface_euler_characteristic = strand_count - total_positive_band_count
    twice_genus = 2 - boundary_component_count - surface_euler_characteristic
    require(surface_euler_characteristic == -1, "five-band Euler characteristic")
    require(twice_genus == 2, "one-boundary band surface has genus one")

    transpositions = tuple(
        transposition(4, first, second)
        for first in range(4)
        for second in range(first + 1, 4)
    )
    require(len(transpositions) == 6, "S4 transposition count")
    unknot_image_orders = {len(generated_subgroup((meridian,))) for meridian in transpositions}
    require(unknot_image_orders == {2}, "unknot meridional transposition image")

    trefoil_representations: list[tuple[Permutation, Permutation, int]] = []
    image_order_census: dict[int, int] = {}
    for first in transpositions:
        for second in transpositions:
            left = compose(compose(first, second), first)
            right = compose(compose(second, first), second)
            if left != right:
                continue
            order = len(generated_subgroup((first, second)))
            trefoil_representations.append((first, second, order))
            image_order_census[order] = image_order_census.get(order, 0) + 1

    require(image_order_census == {2: 6, 6: 24}, "complete trefoil transposition census")
    maximum_trefoil_image_order = max(order for _, _, order in trefoil_representations)
    forbidden_threshold = 6 if args.mutate_drop_full_s4 else 24
    require(
        maximum_trefoil_image_order < forbidden_threshold,
        "no trefoil meridional transposition representation reaches the required image",
    )

    full_s4_tuple_count = 0
    for coloring in itertools.product(transpositions, repeat=4):
        if len(generated_subgroup(coloring)) == 24:
            full_s4_tuple_count += 1
    require(full_s4_tuple_count > 0, "full S4 transposition coloring is nonvacuous")

    # Schubert's cable-genus formula reduces a genus-one cable of the unknot
    # to (p-1)(|q|-1)=2.  Enumerate the positive factor pairs exactly.
    genus_one_torus_parameters = []
    for divisor in range(1, 3):
        if 2 % divisor:
            continue
        p = divisor + 1
        q = 2 // divisor + 1
        if math.gcd(p, q) == 1:
            genus_one_torus_parameters.append((p, q))
    require(genus_one_torus_parameters == [(2, 3), (3, 2)], "genus-one torus census")

    payload = {
        "status": "PASS-R4-CYCLE-0-ALL-MINIMAL-B4-PACKETS",
        "packet_surface": {
            "strands": strand_count,
            "normalization_positive_bands": normalization_band_count,
            "node_positive_bands": node_positive_band_count,
            "total_positive_bands": total_positive_band_count,
            "boundary_components": boundary_component_count,
            "euler_characteristic": surface_euler_characteristic,
            "genus": twice_genus // 2,
            "scope": "quasipositive surface in B4; not an asserted Seifert surface in S3",
        },
        "global_seifert_genus_bridge": "corrected Neumann-Rudolph good fiber plus node smoothing",
        "graph_knots_genus_at_most_one": ["unknot", "right_trefoil", "left_trefoil"],
        "graph_knot_alexander_candidates": ["1", "t^2-t+1"],
        "genus_one_torus_parameter_pairs_up_to_sign": genus_one_torus_parameters,
        "trefoil_transposition_image_order_census": image_order_census,
        "maximum_trefoil_transposition_image_order": maximum_trefoil_image_order,
        "unknot_transposition_image_orders": sorted(unknot_image_orders),
        "required_full_s4_order": 24,
        "s4_generating_ordered_transposition_4tuples": full_s4_tuple_count,
        "minimal_packet_polynomial_globalization": False,
        "broader_nonminimal_or_tangential_horn": "OPEN",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    print(json.dumps(payload, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
