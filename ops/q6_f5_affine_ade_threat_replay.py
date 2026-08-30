#!/usr/bin/env python3
"""Exact desk replay for the q=6 F5 affine-ADE lattice threat map.

This is deliberately a necessary-lattice calculation.  It works in the
orthogonal total-transform basis of the ninefold F_2 blowup and does not turn
an integral survivor into an effective surface, an incidence, or a map.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import sys
from functools import lru_cache
from fractions import Fraction


L = 0
O = (1, 2)
I = (3, 4, 5, 6, 7, 8)
BASE_C = (0, 1, 1, 2, 2, 2, 2, 2, 2)
TAU0_C = (0, 2, 0, 2, 2, 2, 2, 2, 2)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def compositions(total: int, length: int):
    if length == 1:
        if total >= 1:
            yield (total,)
        return
    for first in range(1, total - length + 2):
        for tail in compositions(total - first, length - 1):
            yield (first,) + tail


def weighted_positive_compositions(total, weights):
    for values in itertools.product(range(1, total + 1), repeat=len(weights)):
        if sum(weight * value for weight, value in zip(weights, values)) == total:
            yield values


def weighted_unit_contacts(weights):
    out = []
    for owner, weight in enumerate(weights):
        if weight != 1:
            continue
        out.append(tuple(1 if index == owner else 0 for index in range(len(weights))))
    return tuple(out)


def component_patterns(rank: int, base: int, support_cap: int):
    """All positive A_rank Cartier vectors with the requested forest support.

    Put delta_0=m_1, delta_i=m_(i+1)-m_i, delta_rank=-m_rank.
    The condition C_A m >= 0 says that delta is nonincreasing.  Effectivity
    of the residual total says base+delta_i>=0.  Hence
    -base<=delta_i<=rank*base, making this enumeration complete without an
    arbitrary coefficient cutoff.
    """
    values = range(-base, rank * base + 1)
    out = []
    for delta in itertools.product(values, repeat=rank + 1):
        if sum(delta) != 0:
            continue
        if any(delta[j] < delta[j + 1] for j in range(rank)):
            continue
        partial = []
        running = 0
        for j in range(rank):
            running += delta[j]
            partial.append(running)
        if any(value <= 0 for value in partial):
            continue
        n = tuple(delta[j] - delta[j + 1] for j in range(rank))
        if sum(value > 0 for value in n) > support_cap:
            continue
        if any(base + value < 0 for value in delta):
            continue
        out.append((tuple(partial), n, tuple(delta)))
    return tuple(sorted(out))


def component_specs(max_rank: int, support_cap: int):
    specs = []
    for rank in range(1, max_rank + 1):
        for m, n, delta in component_patterns(rank, 2, support_cap):
            specs.append((rank, m, n, delta))
    return tuple(sorted(specs))


def allocation_orbits(max_rank: int, support_cap: int):
    """One representative per S_6 x S_2 orbit of directed A-block data."""
    specs = component_specs(max_rank, support_cap)
    i_multisets = []

    def extend(start, chosen, used_rank, used_coords):
        i_multisets.append(tuple(chosen))
        for index in range(start, len(specs)):
            spec = specs[index]
            rank = spec[0]
            if used_rank + rank > max_rank or used_coords + rank + 1 > len(I):
                continue
            extend(index, chosen + [spec], used_rank + rank, used_coords + rank + 1)

    extend(0, [], 0, 0)
    o_patterns = component_patterns(1, 1, support_cap)
    allocations = []
    for i_specs in i_multisets:
        rank_i = sum(spec[0] for spec in i_specs)
        o_choices = (None,) + tuple((1, m, n, delta) for m, n, delta in o_patterns)
        for o_spec in o_choices:
            if rank_i + (0 if o_spec is None else 1) > max_rank:
                continue
            components = []
            cursor = I[0]
            for spec in i_specs:
                rank, m, n, delta = spec
                coords = tuple(range(cursor, cursor + rank + 1))
                cursor += rank + 1
                components.append(make_component("I", coords, m, n, delta))
            if o_spec is not None:
                _, m, n, delta = o_spec
                components.append(make_component("O", O, m, n, delta))
            allocations.append(tuple(components))
    # The construction is canonical: ordered coordinate chains encode root
    # orientation; repeated identical I-blocks are a multiset; unused labels
    # are forgotten.  A final serialization check guards accidental repeats.
    keys = [allocation_key(allocation) for allocation in allocations]
    require(len(keys) == len(set(keys)), "duplicate canonical allocation orbit")
    return tuple(allocations)


def make_component(group, coords, m, n, delta):
    roots = tuple((coords[j], coords[j + 1]) for j in range(len(coords) - 1))
    return {
        "group": group,
        "rank": len(roots),
        "coords": tuple(coords),
        "roots": roots,
        "m": tuple(m),
        "n": tuple(n),
        "delta": tuple(delta),
    }


def allocation_key(allocation):
    return tuple(
        (component["group"], component["rank"], component["m"], component["n"])
        for component in allocation
    )


def allocation_rank(allocation):
    return sum(component["rank"] for component in allocation)


def shifted_total(allocation, base_c):
    c = list(base_c)
    for component in allocation:
        for coordinate, delta in zip(component["coords"], component["delta"]):
            c[coordinate] += delta
    if min(c) < 0:
        return None
    require(sum(c) == 14, "affine roots changed total multiplicity sum")
    return tuple(c)


def root_edge_map(allocation):
    result = {}
    for component in allocation:
        for root, coefficient in zip(component["roots"], component["m"]):
            require(root not in result, "root repeated across components")
            result[root] = coefficient
    return result


@lru_cache(maxsize=None)
def permutations_i():
    return tuple(itertools.permutations(I))


def carrier_representatives(allocation):
    """Three-I-coordinate carrier choices modulo allocation automorphisms."""
    edge_map = root_edge_map(allocation)
    i_edges = {edge: value for edge, value in edge_map.items() if edge[0] in I}
    automorphisms = []
    for image in permutations_i():
        mapping = dict(zip(I, image))
        moved = {(mapping[p], mapping[q]): value for (p, q), value in i_edges.items()}
        if moved == i_edges:
            automorphisms.append(mapping)
    require(automorphisms, "identity missing from allocation automorphisms")
    seen = set()
    reps = []
    for subset in itertools.combinations(I, 3):
        orbit = {
            tuple(sorted(mapping[index] for index in subset)) for mapping in automorphisms
        }
        canonical = min(orbit)
        if canonical in seen:
            continue
        seen.update(orbit)
        reps.append(canonical)
    return tuple(sorted(reps))


def component_contacts(allocation, carrier_i):
    """Return (Z contacts, residual strict contacts) or None if impossible."""
    carrier = set(O + tuple(carrier_i)) if carrier_i is not None else set()
    data = []
    for component in allocation:
        z_contact = []
        for parent, child in component["roots"]:
            z_contact.append((1 if parent in carrier else 0) - (1 if child in carrier else 0))
        if any(value < 0 for value in z_contact):
            return None
        if sum(value > 0 for value in z_contact) > 1:
            return None
        residual = tuple(n - z for n, z in zip(component["n"], z_contact))
        if any(value < 0 for value in residual):
            return None
        if sum(value > 0 for value in residual) > 1:
            return None
        data.append((tuple(z_contact), residual))
    return tuple(data)


def total_after_carrier(c, carrier_i):
    if carrier_i is None:
        return tuple(c)
    carrier = set(O + tuple(carrier_i))
    result = tuple(value - (1 if index in carrier else 0) for index, value in enumerate(c))
    if min(result) < 0:
        return None
    require(sum(result) == 9, "simple q6 carrier did not remove five multiplicities")
    return result


def energy_lower_bound(c, a_values, epsilon_owner):
    pair_a = sum(
        a_values[j] * a_values[k]
        for j in range(len(a_values))
        for k in range(j)
    )
    total_a = sum(a_values)
    correction = Fraction(sum(value * value - value for value in c), 2)
    return 2 * pair_a + total_a - a_values[epsilon_owner] - correction


def aggregate_cross_lower_bound(c, a_values, epsilon, weights, group):
    """Integer lower bound for the intersection of two Cartier sub-divisors."""
    chosen = set(group)
    a_left = sum(
        weights[index] * a_values[index] for index in range(len(a_values))
        if index in chosen
    )
    epsilon_left = sum(
        weights[index] * epsilon[index] for index in range(len(epsilon))
        if index in chosen
    )
    a_total = sum(weight * value for weight, value in zip(weights, a_values))
    epsilon_total = sum(
        weight * value for weight, value in zip(weights, epsilon)
    )
    a_right = a_total - a_left
    epsilon_right = epsilon_total - epsilon_left
    require(a_left > 0 and a_right > 0, "aggregate separation lost positivity")
    correction = Fraction(sum(value * value - value for value in c), 2)
    return (
        2 * a_left * a_right
        + a_left * epsilon_right
        + a_right * epsilon_left
        - correction
    )


def connected_coordinate_blocks(allocation, differences, group):
    blocks = []
    used = set()
    for component, values in zip(allocation, differences):
        if component["group"] != group:
            continue
        coords = component["coords"]
        offsets = [0]
        for value in values:
            offsets.append(offsets[-1] - value)
        blocks.append((coords, tuple(offsets)))
        used.update(coords)
    universe = I if group == "I" else O
    for coordinate in universe:
        if coordinate not in used:
            blocks.append(((coordinate,), (0,)))
    return tuple(blocks)


def block_options(block, bounds):
    coords, offsets = block
    low = max(-offset for offset in offsets)
    high = min(bounds[coordinate] - offset for coordinate, offset in zip(coords, offsets))
    out = []
    for anchor in range(low, high + 1):
        values = tuple(anchor + offset for offset in offsets)
        out.append((coords, values, sum(values)))
    return tuple(out)


def group_vectors(blocks, bounds, target_sum):
    out = []

    def extend(index, vector, running):
        if index == len(blocks):
            if running == target_sum:
                out.append(tuple(vector))
            return
        for coords, values, subtotal in block_options(blocks[index], bounds):
            if running + subtotal > target_sum:
                continue
            new_vector = list(vector)
            for coordinate, value in zip(coords, values):
                new_vector[coordinate] = value
            extend(index + 1, new_vector, running + subtotal)

    extend(0, [0] * 9, 0)
    return tuple(out)


@lru_cache(maxsize=None)
def branch_candidates(c, allocation_serial, differences, a, degree, epsilon, t_contact):
    allocation = deserialize_allocation(allocation_serial)
    total_sum = 5 * a + 2 * epsilon - degree
    i_sum = 3 * a + epsilon - t_contact
    o_sum = total_sum - i_sum
    if total_sum < 0 or i_sum < 0 or o_sum < 0:
        return ()
    i_blocks = connected_coordinate_blocks(allocation, differences, "I")
    o_blocks = connected_coordinate_blocks(allocation, differences, "O")
    i_vectors = group_vectors(i_blocks, c, i_sum)
    o_vectors = group_vectors(o_blocks, c, o_sum)
    result = []
    for iv in i_vectors:
        for ov in o_vectors:
            x = tuple(iv[index] + ov[index] for index in range(9))
            if any(x[index] > c[index] for index in range(9)):
                continue
            square_sum = sum(value * value for value in x)
            adjunction_numerator = 2 * a * a + 2 * a * epsilon - square_sum + a - degree
            if adjunction_numerator % 2:
                continue
            delta = 1 + adjunction_numerator // 2
            if delta < 0:
                continue
            result.append((x, delta))
    return tuple(result)


def serialize_allocation(allocation):
    return tuple(
        (
            component["group"],
            component["coords"],
            component["roots"],
            component["m"],
            component["n"],
            component["delta"],
        )
        for component in allocation
    )


def deserialize_allocation(serial):
    return tuple(
        {
            "group": entry[0],
            "rank": len(entry[2]),
            "coords": entry[1],
            "roots": entry[2],
            "m": entry[3],
            "n": entry[4],
            "delta": entry[5],
        }
        for entry in serial
    )


def branch_differences(allocation, contact_data, owner_map, branch, weight):
    values = []
    for index, component in enumerate(allocation):
        residual = contact_data[index][1]
        if any(residual) and owner_map[index] == branch:
            require(
                all(value % weight == 0 for value in residual),
                "weighted affine contact was not divisible by Cartier weight",
            )
            values.append(tuple(value // weight for value in residual))
        else:
            values.append(tuple(0 for _ in component["roots"]))
    return tuple(values)


def pair_intersection(a, epsilon, x, j, k):
    return (
        2 * a[j] * a[k]
        + a[j] * epsilon[k]
        + a[k] * epsilon[j]
        - sum(x[j][index] * x[k][index] for index in range(9))
    )


def pair_condition(pair_mode, j, k, value):
    pair = tuple(sorted((j, k)))
    if pair_mode == "zero":
        return value == 0
    require(pair_mode.startswith("tangent:"), "unknown local pair condition")
    tangent = tuple(sorted(int(value) for value in pair_mode.split(":", 1)[1].split(",")))
    if pair == tangent:
        return value >= 1
    return value == 0


def carrier_forest_profile(
    xs, a, epsilon, carrier_i, allocation, contact_data, owner_map
):
    if carrier_i is None:
        return {"status": "NO_CARRIER", "z_intersections": ()}
    carrier = set(O + tuple(carrier_i))
    z_intersections = tuple(
        2 * a[j] + epsilon[j] - sum(xs[j][index] for index in carrier)
        for j in range(len(xs))
    )
    if any(value < 0 for value in z_intersections):
        return {"status": "NEGATIVE_Z_INTERSECTION", "z_intersections": z_intersections}
    direct_owners = tuple(index for index, value in enumerate(z_intersections) if value > 0)
    bridge_owners = []
    for index in range(len(allocation)):
        z_edge = any(contact_data[index][0])
        b_edge = any(contact_data[index][1])
        if z_edge and b_edge:
            require(owner_map[index] is not None, "affine bridge has no strict owner")
            bridge_owners.append(owner_map[index])

    # Z is an affine carrier, hence every direct Z--strict intersection is
    # away from the charged F5 cluster.  Distinct positive strict owners, or
    # two disconnected affine trees, give two genuinely labelled B--Z paths.
    # One direct edge and one affine bridge on different strict owners do so
    # as well.  A direct edge and bridge on the *same* owner may be one
    # unresolved triple contact; the lattice cannot decide that incidence,
    # so it is retained and explicitly flagged instead of being killed by an
    # unlabelled graph contraction.
    if len(direct_owners) > 1 or len(bridge_owners) > 1:
        status = "FOREST_REJECT_MULTIPLE_LABELLED_PATHS"
    elif direct_owners and bridge_owners and direct_owners[0] != bridge_owners[0]:
        status = "FOREST_REJECT_DISTINCT_OWNER_PATHS"
    elif direct_owners and bridge_owners:
        status = "FOREST_UNRESOLVED_SAME_OWNER_TRIPLE"
    elif direct_owners and z_intersections[direct_owners[0]] > 1:
        status = "FOREST_UNRESOLVED_DIRECT_CONTACT_DEPTH"
    else:
        status = "FOREST_LABEL_COMPATIBLE"
    return {
        "status": status,
        "z_intersections": z_intersections,
        "direct_owners": direct_owners,
        "bridge_owners": tuple(bridge_owners),
    }


def join_candidates(
    candidates,
    c,
    a,
    epsilon,
    weights,
    pair_mode,
    carrier_i,
    allocation,
    contact_data,
    owner_map,
):
    """Join two through four physical-prime candidate lists exactly.

    The equality is weighted: sum_j weights[j] x_j = c.  Pair conditions
    are imposed on reduced physical classes, never on repeated Cartier
    copies.  The final branch is reconstructed from the residual vector,
    so every emitted tuple is exact and no Cartesian product over it occurs.
    """
    count = len(candidates)
    require(2 <= count <= 4, "only two- through four-prime q6 cells are registered")
    require(len(weights) == count, "Cartier-weight arity mismatch")
    final_lookup = {entry[0]: entry[1] for entry in candidates[-1]}
    survivors = []
    stats = {
        "pair_condition_matches_before_carrier": 0,
        "forest_rejected": 0,
        "forest_ambiguous_retained": 0,
    }

    def extend(branch, xs, deltas, partial):
        if branch == count - 1:
            remaining = tuple(c[index] - partial[index] for index in range(9))
            weight = weights[branch]
            if any(value < 0 or value % weight for value in remaining):
                return
            x_final = tuple(value // weight for value in remaining)
            if x_final not in final_lookup:
                return
            all_x = tuple(xs) + (x_final,)
            for earlier in range(branch):
                value = pair_intersection(a, epsilon, all_x, earlier, branch)
                if not pair_condition(pair_mode, earlier, branch, value):
                    return
            stats["pair_condition_matches_before_carrier"] += 1
            profile = carrier_forest_profile(
                all_x,
                a,
                epsilon,
                carrier_i,
                allocation,
                contact_data,
                owner_map,
            )
            if profile["status"].startswith("NEGATIVE_") or profile["status"].startswith(
                "FOREST_REJECT"
            ):
                stats["forest_rejected"] += 1
                return
            if profile["status"].startswith("FOREST_UNRESOLVED"):
                stats["forest_ambiguous_retained"] += 1
            pair_values = {
                f"{left},{right}": pair_intersection(
                    a, epsilon, all_x, left, right
                )
                for right in range(count)
                for left in range(right)
            }
            survivors.append(
                (
                    all_x,
                    tuple(deltas) + (final_lookup[x_final],),
                    pair_values,
                    profile,
                )
            )
            return

        weight = weights[branch]
        for x_value, delta_value in candidates[branch]:
            new_partial = tuple(
                partial[index] + weight * x_value[index] for index in range(9)
            )
            if any(new_partial[index] > c[index] for index in range(9)):
                continue
            proposed = tuple(xs) + (x_value,)
            if any(
                not pair_condition(
                    pair_mode,
                    earlier,
                    branch,
                    pair_intersection(a, epsilon, proposed, earlier, branch),
                )
                for earlier in range(branch)
            ):
                continue
            extend(branch + 1, proposed, tuple(deltas) + (delta_value,), new_partial)

    extend(0, (), (), (0,) * 9)
    return survivors, stats


def allocation_description(allocation, contact_data, carrier_i):
    parts = []
    for index, component in enumerate(allocation):
        parts.append(
            {
                "group": component["group"],
                "type": "A" + str(component["rank"]),
                "m": component["m"],
                "n": component["n"],
                "z_contact": contact_data[index][0],
                "strict_contact": contact_data[index][1],
            }
        )
    return {"components": parts, "carrier_i": carrier_i}


def analyze_cell(
    name,
    degrees,
    weights,
    max_rank,
    with_carrier,
    pair_mode,
    base_c,
    local_rank,
    separation_group=None,
    rank_filter="positive",
):
    k = len(degrees)
    require(len(weights) == k, "degree/Cartier-weight arity mismatch")
    require(sum(weight * degree for weight, degree in zip(weights, degrees)) == 8,
            "local weighted A-degree must be eight")
    expected_cap = 8 - local_rank - k - (1 if with_carrier else 0)
    require(max_rank == expected_cap, "Euler affine-rank cap mismatch")
    require(rank_filter in ("positive", "zero"), "unknown affine-rank filter")
    total_a = 3 if with_carrier else 4
    support_cap = 2 if with_carrier else 1
    allocations = allocation_orbits(max_rank, support_cap)
    a_partitions = tuple(weighted_positive_compositions(total_a, weights))
    epsilon_patterns = weighted_unit_contacts(weights)
    t_patterns = weighted_unit_contacts(weights)
    energy_licensed = all(weight == 1 for weight in weights) and pair_mode == "zero"
    require(a_partitions, "cell has no positive weighted B-degree partition")
    require(epsilon_patterns and t_patterns, "cell cannot carry unit S/T contact")
    summary = {
        "degrees": degrees,
        "weights": weights,
        "pair_mode": pair_mode,
        "base_c": base_c,
        "local_rank": local_rank,
        "euler_affine_rank_cap": max_rank,
        "top_rank_requires_base_A1": True,
        "rank_filter": rank_filter,
        "energy_pruning_licensed": energy_licensed,
        "energy_pruning_applied": False,
        "separation_group": separation_group,
        "minimum_feasible_aggregate_cross_bound": None,
        "minimum_chronology_feasible_aggregate_cross_bound": None,
        "allocation_orbits": 0,
        "root_rank_counts": {},
        "root_type_counts": {},
        "positive_minimum_energy_allocations": 0,
        "contact_degree_dead": 0,
        "branch_feasible_allocations": 0,
        "branch_feasible_metas": 0,
        "minimum_branch_feasible_energy": None,
        "minimum_chronology_branch_feasible_energy": None,
        "positive_energy_metas": 0,
        "exact_join_metas": 0,
        "adjunction_candidate_tuples": 0,
        "pair_condition_matches_before_carrier": 0,
        "forest_rejected": 0,
        "forest_ambiguous_retained": 0,
        "survivors": 0,
        "chronology_survivors": 0,
        "chronology_forbidden_O_root_survivors": 0,
        "root_type_survivor_counts": {},
        "root_coefficient_survivor_counts": {},
        "lambda_counts": {},
        "forest_status_counts": {},
        "euler_base_survivor_counts": {},
        "survivor_signatures": [],
        "inventory_sha256": None,
    }
    seen_survivor_signatures = set()
    inventory = []
    for allocation in allocations:
        rank = allocation_rank(allocation)
        if rank_filter == "positive" and rank == 0:
            # The no-affine cell is replayed separately as a baseline control.
            continue
        if rank_filter == "zero" and rank != 0:
            continue
        pre_carrier = shifted_total(allocation, base_c)
        if pre_carrier is None:
            continue
        carrier_choices = carrier_representatives(allocation) if with_carrier else (None,)
        for carrier_i in carrier_choices:
            c = total_after_carrier(pre_carrier, carrier_i)
            if c is None:
                continue
            contact_data = component_contacts(allocation, carrier_i)
            if contact_data is None:
                continue
            summary["allocation_orbits"] += 1
            rank_key = str(allocation_rank(allocation))
            summary["root_rank_counts"][rank_key] = (
                summary["root_rank_counts"].get(rank_key, 0) + 1
            )
            type_key = "+".join(
                sorted("A" + str(component["rank"]) for component in allocation)
            )
            summary["root_type_counts"][type_key] = (
                summary["root_type_counts"].get(type_key, 0) + 1
            )
            inventory.append(allocation_description(allocation, contact_data, carrier_i))
            if energy_licensed:
                minimum_energy = min(
                    energy_lower_bound(c, a_values, epsilon.index(1))
                    for a_values in a_partitions
                    for epsilon in epsilon_patterns
                )
                if minimum_energy > 0:
                    summary["positive_minimum_energy_allocations"] += 1
            allocation_has_feasible_meta = False
            owner_options = []
            for index in range(len(allocation)):
                residual = contact_data[index][1]
                if any(residual):
                    eligible = tuple(
                        branch
                        for branch, weight in enumerate(weights)
                        if all(value % weight == 0 for value in residual)
                    )
                    owner_options.append(eligible)
                else:
                    owner_options.append((None,))
            if any(not values for values in owner_options):
                summary["contact_degree_dead"] += 1
                continue
            for owner_map in itertools.product(*owner_options):
                for a_values in a_partitions:
                    for epsilon in epsilon_patterns:
                        energy = (
                            energy_lower_bound(c, a_values, epsilon.index(1))
                            if energy_licensed
                            else None
                        )
                        for t_contact in t_patterns:
                            candidate_lists = []
                            serial = serialize_allocation(allocation)
                            for branch in range(k):
                                differences = branch_differences(
                                    allocation,
                                    contact_data,
                                    owner_map,
                                    branch,
                                    weights[branch],
                                )
                                bounds = tuple(
                                    value // weights[branch] for value in c
                                )
                                candidate_lists.append(
                                    branch_candidates(
                                        bounds,
                                        serial,
                                        differences,
                                        a_values[branch],
                                        degrees[branch],
                                        epsilon[branch],
                                        t_contact[branch],
                                    )
                                )
                            if any(not values for values in candidate_lists):
                                continue
                            allocation_has_feasible_meta = True
                            summary["branch_feasible_metas"] += 1
                            if energy is not None:
                                old_minimum = summary["minimum_branch_feasible_energy"]
                                if old_minimum is None or energy < Fraction(old_minimum):
                                    summary["minimum_branch_feasible_energy"] = str(energy)
                                if not any(
                                    component["group"] == "O"
                                    for component in allocation
                                ):
                                    old_chronology = summary[
                                        "minimum_chronology_branch_feasible_energy"
                                    ]
                                    if (
                                        old_chronology is None
                                        or energy < Fraction(old_chronology)
                                    ):
                                        summary[
                                            "minimum_chronology_branch_feasible_energy"
                                        ] = str(energy)
                            if separation_group is not None:
                                aggregate_bound = aggregate_cross_lower_bound(
                                    c,
                                    a_values,
                                    epsilon,
                                    weights,
                                    separation_group,
                                )
                                old_aggregate = summary[
                                    "minimum_feasible_aggregate_cross_bound"
                                ]
                                if (
                                    old_aggregate is None
                                    or aggregate_bound < Fraction(old_aggregate)
                                ):
                                    summary[
                                        "minimum_feasible_aggregate_cross_bound"
                                    ] = str(aggregate_bound)
                                if not any(
                                    component["group"] == "O"
                                    for component in allocation
                                ):
                                    old_chronology_aggregate = summary[
                                        "minimum_chronology_feasible_aggregate_cross_bound"
                                    ]
                                    if (
                                        old_chronology_aggregate is None
                                        or aggregate_bound
                                        < Fraction(old_chronology_aggregate)
                                    ):
                                        summary[
                                            "minimum_chronology_feasible_aggregate_cross_bound"
                                        ] = str(aggregate_bound)
                            if energy_licensed and energy > 0:
                                summary["positive_energy_metas"] += 1
                            summary["exact_join_metas"] += 1
                            summary["adjunction_candidate_tuples"] += sum(
                                len(values) for values in candidate_lists
                            )
                            joined, join_stats = join_candidates(
                                candidate_lists,
                                c,
                                a_values,
                                epsilon,
                                weights,
                                pair_mode,
                                carrier_i,
                                allocation,
                                contact_data,
                                owner_map,
                            )
                            for key, value in join_stats.items():
                                summary[key] += value
                            for xs, deltas, pair_values, forest_profile in joined:
                                has_forbidden_o_root = any(
                                    component["group"] == "O" for component in allocation
                                )
                                rank = allocation_rank(allocation)
                                base_requirement = (
                                    "A1" if rank > 0 and rank == max_rank else "A1_OR_P1"
                                )
                                record = {
                                    "cell": name,
                                    "root_data": allocation_description(
                                        allocation, contact_data, carrier_i
                                    ),
                                    "c": c,
                                    "a": a_values,
                                    "weights": weights,
                                    "epsilon": epsilon,
                                    "t_contact": t_contact,
                                    "affine_owner": owner_map,
                                    "x": xs,
                                    "delta": deltas,
                                    "pair_intersections": pair_values,
                                    "carrier_forest": forest_profile,
                                    "chronology_forbidden_O_root": has_forbidden_o_root,
                                    "euler_base_requirement": base_requirement,
                                }
                                key = json.dumps(record, sort_keys=True, separators=(",", ":"))
                                if key in seen_survivor_signatures:
                                    continue
                                seen_survivor_signatures.add(key)
                                summary["survivor_signatures"].append(record)
            if allocation_has_feasible_meta:
                summary["branch_feasible_allocations"] += 1
            else:
                summary["contact_degree_dead"] += 1
    summary["survivor_signatures"].sort(
        key=lambda value: json.dumps(value, sort_keys=True, separators=(",", ":"))
    )
    summary["survivors"] = len(summary["survivor_signatures"])
    for record in summary["survivor_signatures"]:
        if record["chronology_forbidden_O_root"]:
            summary["chronology_forbidden_O_root_survivors"] += 1
        else:
            summary["chronology_survivors"] += 1
        components = record["root_data"]["components"]
        root_type = "+".join(sorted(component["type"] for component in components))
        summary["root_type_survivor_counts"][root_type] = (
            summary["root_type_survivor_counts"].get(root_type, 0) + 1
        )
        coefficient_key = "+".join(
            sorted(component["type"] + ":" + ",".join(map(str, component["m"]))
                   for component in components)
        )
        summary["root_coefficient_survivor_counts"][coefficient_key] = (
            summary["root_coefficient_survivor_counts"].get(coefficient_key, 0) + 1
        )
        if pair_mode.startswith("tangent:"):
            tangent_pair = tuple(
                sorted(int(value) for value in pair_mode.split(":", 1)[1].split(","))
            )
            lambda_key = str(
                record["pair_intersections"][f"{tangent_pair[0]},{tangent_pair[1]}"]
            )
            summary["lambda_counts"][lambda_key] = (
                summary["lambda_counts"].get(lambda_key, 0) + 1
            )
        forest_key = record["carrier_forest"]["status"]
        summary["forest_status_counts"][forest_key] = (
            summary["forest_status_counts"].get(forest_key, 0) + 1
        )
        base_key = record["euler_base_requirement"]
        summary["euler_base_survivor_counts"][base_key] = (
            summary["euler_base_survivor_counts"].get(base_key, 0) + 1
        )
    inventory_bytes = json.dumps(
        sorted(inventory, key=lambda value: json.dumps(value, sort_keys=True)),
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    summary["inventory_sha256"] = hashlib.sha256(inventory_bytes).hexdigest()
    return summary


def validate_marking(c, expected_norm):
    require(len(c) == 9, "q6 total must have nine exceptional coordinates")
    require(c[L] == 0, "q6 strict total must be disjoint from L")
    require(sum(c) == 14, "q6 baseline multiplicity sum must be fourteen")
    require(
        sum(value * value for value in c) == expected_norm,
        "q6 baseline norm mismatch",
    )
    # In the F_2 basis C=4S+9F-sum c_iP_i and
    # T=S+3F-sum_(I)P_i.
    require(9 - 2 * 4 == 1, "q6 S contact reconstruction failed")
    require(4 + 9 - sum(c[index] for index in I) == 1, "q6 T contact failed")


def negative_control():
    bad = list(BASE_C)
    bad[I[0]] -= 1
    rejected = False
    try:
        validate_marking(tuple(bad), 26)
    except RuntimeError:
        rejected = True
    require(rejected, "mutated q6 contact vector was accepted")


def run_failing_mutation():
    bad = list(BASE_C)
    bad[I[0]] -= 1
    # This path must terminate through the ordinary fail-closed wrapper in
    # every interpreter mode.  It is intentionally not caught here.
    validate_marking(tuple(bad), 26)


def main():
    validate_marking(BASE_C, 26)
    validate_marking(TAU0_C, 28)
    negative_control()
    # Each tuple is
    # (name, reduced-prime A-degrees, Cartier weights, affine-rank cap,
    #  carrier present, local pair rule, strict total, local ADE rank).
    # A tangent:i,j rule retains exactly C_i.C_j=lambda>=1 and forces every
    # other pair intersection to zero.  Tau=0 rows are conditional on the
    # sealed local analytic classification; no carrier is numerically
    # possible there.
    jobs = (
        ("U3_A3", (4, 4), (1, 1), 3, False, "zero", BASE_C, 3),
        ("U3_A3_plus_Z", (4, 4), (1, 1), 2, True, "zero", BASE_C, 3),
        ("B3_tau_ne0_Delta_ne0", (4, 2, 2), (1, 1, 1), 3, False,
         "zero", BASE_C, 2),
        ("B3_tau_ne0_Delta_ne0_plus_Z", (4, 2, 2), (1, 1, 1), 2, True,
         "zero", BASE_C, 2),
        ("B3_tau_ne0_Delta0_split", (4, 2, 2), (1, 1, 1), 3, False,
         "tangent:1,2", BASE_C, 2, (1, 2)),
        ("B3_tau_ne0_Delta0_split_plus_Z", (4, 2, 2), (1, 1, 1), 2, True,
         "tangent:1,2", BASE_C, 2, (1, 2)),
        ("B3_tau_ne0_Delta0_odd", (4, 4), (1, 1), 4, False,
         "zero", BASE_C, 2),
        ("B3_tau_ne0_Delta0_odd_plus_Z", (4, 4), (1, 1), 3, True,
         "zero", BASE_C, 2),
        ("B3_tau_ne0_Delta0_doubled", (4, 2), (1, 2), 4, False,
         "zero", BASE_C, 2, (1,)),
        ("B3_tau_ne0_Delta0_doubled_plus_Z", (4, 2), (1, 2), 3, True,
         "zero", BASE_C, 2, (1,)),
        ("B3_tau0_distinct_residual", (4, 2, 1, 1), (1, 1, 1, 1), 2,
         False, "zero", TAU0_C, 2),
        ("B3_tau0_split_residual", (4, 2, 1, 1), (1, 1, 1, 1), 2,
         False, "tangent:2,3", TAU0_C, 2, (2, 3)),
        ("B3_tau0_odd_residual", (4, 2, 2), (1, 1, 1), 3, False,
         "zero", TAU0_C, 2),
        ("B3_tau0_doubled_residual", (4, 2, 1), (1, 1, 2), 3, False,
         "zero", TAU0_C, 2, (2,)),
    )
    results = {}
    baseline_controls = {}
    for job in jobs:
        results[job[0]] = analyze_cell(*job)
        baseline_controls[job[0]] = analyze_cell(*job, rank_filter="zero")
    require(
        all(data["survivors"] == 0 for data in results.values()),
        "q6 affine-ADE necessary lattice survivor found",
    )
    require(
        all(data["survivors"] == 0 for data in baseline_controls.values()),
        "q6 no-affine baseline/control survivor found",
    )
    compact = {
        name: {key: value for key, value in data.items() if key != "survivor_signatures"}
        for name, data in results.items()
    }
    compact_controls = {
        name: {key: value for key, value in data.items() if key != "survivor_signatures"}
        for name, data in baseline_controls.items()
    }
    survivor_payload = {
        "affine": {
            name: data["survivor_signatures"] for name, data in results.items()
        },
        "baseline_controls": {
            name: data["survivor_signatures"]
            for name, data in baseline_controls.items()
        },
    }
    survivor_bytes = json.dumps(
        survivor_payload, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    output = {
        "schema": "Q6-AFFINE-ADE-THREAT/v1",
        "marking": {
            "baseline_c": BASE_C,
            "tau0_c": TAU0_C,
            "I": I,
            "O": O,
            "L": L,
            "S_contact": 1,
            "T_contact": 1,
            "O_root_chronology": (
                "P_o1-P_o2 is an occupied local root; its reverse is anti-effective"
            ),
        },
        "results": compact,
        "baseline_controls": compact_controls,
        "survivor_payload_bytes": len(survivor_bytes),
        "survivor_payload_sha256": hashlib.sha256(survivor_bytes).hexdigest(),
        "negative_control": "PASS",
    }
    print(json.dumps(output, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    try:
        if sys.argv[1:] == ["--mutate-contact"]:
            run_failing_mutation()
        else:
            require(not sys.argv[1:], "unknown command-line argument")
            main()
    except RuntimeError as error:
        print("FAIL:" + str(error), file=sys.stderr)
        raise SystemExit(1)
