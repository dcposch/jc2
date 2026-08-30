#!/usr/bin/env python3
"""Enumerate capped dominant ADE Cartier data without external packages.

The output contains one representative of every diagram-automorphism orbit
of pairs (m,n) with m>0, n=Cm>=0, and sum(n)<=8 for A1..A8 and
D4..D9.  A dominant Dynkin-label vector n is already the unique dominant
representative of its Weyl orbit.

Physical-germ statistics use the following deliberately separate formal
model on the minimal ADE resolution.  One germ meets either a smooth point
of one exceptional component, contributing k*e_i, or a node of two adjacent
components, contributing u*e_i+v*e_j.  The program counts unordered
multisets of such germs with total vector n.  It does not group local germs
into global carrier curves and does not assert analytic or global
effectivity.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import hashlib
import itertools
import json
from pathlib import Path
from typing import Iterable


MAX_CAP = 8
SMALL_CAP = 4
SCHEMA = "jc2.ade_cartan_pairs.v1"


def exact_compositions(total: int, length: int) -> Iterable[tuple[int, ...]]:
    """Yield nonnegative length-tuples with the stated sum, lexicographically."""
    if length == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in exact_compositions(total - first, length - 1):
            yield (first,) + tail


def edges(kind: str, rank: int) -> tuple[tuple[int, int], ...]:
    if kind == "A":
        return tuple((i, i + 1) for i in range(rank - 1))
    if kind == "D":
        return tuple((i, i + 1) for i in range(rank - 2)) + (
            (rank - 3, rank - 1),
        )
    raise ValueError(kind)


def cartan(kind: str, rank: int) -> tuple[tuple[int, ...], ...]:
    matrix = [[0] * rank for _ in range(rank)]
    for i in range(rank):
        matrix[i][i] = 2
    for i, j in edges(kind, rank):
        matrix[i][j] = matrix[j][i] = -1
    return tuple(tuple(row) for row in matrix)


def matvec(matrix: tuple[tuple[int, ...], ...], vector: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(a * b for a, b in zip(row, vector)) for row in matrix)


def solve_a(n: tuple[int, ...]) -> tuple[int, ...] | None:
    rank = len(n)
    modulus = rank + 1
    if sum((i + 1) * value for i, value in enumerate(n)) % modulus:
        return None
    answer: list[int] = []
    for j0 in range(rank):
        j = j0 + 1
        numerator = (modulus - j) * sum(
            (i + 1) * n[i] for i in range(j)
        )
        numerator += j * sum(
            (modulus - (i + 1)) * n[i] for i in range(j, rank)
        )
        assert numerator % modulus == 0
        answer.append(numerator // modulus)
    return tuple(answer)


def solve_d(n: tuple[int, ...]) -> tuple[int, ...] | None:
    rank = len(n)
    a = n[rank - 2]
    b = n[rank - 1]
    weighted = sum((i + 1) * n[i] for i in range(rank - 2))
    if (a - b) % 2:
        return None
    if (2 * weighted + (rank - 2) * a + rank * b) % 4:
        return None
    answer: list[int] = []
    for j0 in range(rank - 2):
        j = j0 + 1
        value2 = 2 * sum(
            min(i + 1, j) * n[i] for i in range(rank - 2)
        ) + j * (a + b)
        assert value2 % 2 == 0
        answer.append(value2 // 2)
    spin_left4 = 2 * weighted + rank * a + (rank - 2) * b
    spin_right4 = 2 * weighted + (rank - 2) * a + rank * b
    assert spin_left4 % 4 == spin_right4 % 4 == 0
    answer.extend((spin_left4 // 4, spin_right4 // 4))
    return tuple(answer)


def solve(kind: str, n: tuple[int, ...]) -> tuple[int, ...] | None:
    return solve_a(n) if kind == "A" else solve_d(n)


def solve_fraction(
    matrix: tuple[tuple[int, ...], ...], vector: tuple[int, ...]
) -> tuple[Fraction, ...]:
    """Independent exact Gaussian elimination used by --deep-check."""
    rank = len(vector)
    augmented = [
        [Fraction(value) for value in matrix[i]] + [Fraction(vector[i])]
        for i in range(rank)
    ]
    for column in range(rank):
        pivot = next(row for row in range(column, rank) if augmented[row][column])
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        pivot_value = augmented[column][column]
        augmented[column] = [value / pivot_value for value in augmented[column]]
        for row in range(rank):
            if row == column:
                continue
            multiplier = augmented[row][column]
            if multiplier:
                augmented[row] = [
                    left - multiplier * right
                    for left, right in zip(augmented[row], augmented[column])
                ]
    return tuple(augmented[i][-1] for i in range(rank))


def deep_check_all() -> int:
    """Exhaustively compare closed formulas with independent Fraction solves."""
    checked = 0
    specifications = [("A", rank) for rank in range(1, 9)]
    specifications.extend(("D", rank) for rank in range(4, 10))
    for kind, rank in specifications:
        matrix = cartan(kind, rank)
        for weight in range(1, MAX_CAP + 1):
            for n in exact_compositions(weight, rank):
                rational = solve_fraction(matrix, n)
                integral = all(value.denominator == 1 for value in rational)
                formula = solve(kind, n)
                assert (formula is not None) == integral
                if formula is not None:
                    assert formula == tuple(int(value) for value in rational)
                checked += 1
    return checked


def diagram_group(kind: str, rank: int) -> tuple[tuple[int, ...], ...]:
    identity = tuple(range(rank))
    if kind == "A":
        reversal = tuple(reversed(identity))
        return tuple(dict.fromkeys((identity, reversal)))
    if rank == 4:
        # D4 has S3 on the three arms 1,3,4; vertex 2 is fixed.
        arms = (0, 2, 3)
        group = []
        for image in itertools.permutations(arms):
            permutation = list(identity)
            for new_position, old_position in zip(arms, image):
                permutation[new_position] = old_position
            group.append(tuple(permutation))
        return tuple(group)
    spin_swap = list(identity)
    spin_swap[-2], spin_swap[-1] = spin_swap[-1], spin_swap[-2]
    return (identity, tuple(spin_swap))


def permute(vector: tuple[int, ...], permutation: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(vector[old_index] for old_index in permutation)


def orbit(vector: tuple[int, ...], group: tuple[tuple[int, ...], ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(sorted({permute(vector, permutation) for permutation in group}))


def encode(vector: tuple[int, ...], base: int) -> int:
    code = 0
    place = 1
    for value in vector:
        code += value * place
        place *= base
    return code


def physical_atoms(
    rank: int, graph_edges: tuple[tuple[int, int], ...], cap: int
) -> tuple[tuple[tuple[int, ...], dict[str, object]], ...]:
    atoms: list[tuple[tuple[int, ...], dict[str, object]]] = []
    for i in range(rank):
        for order in range(1, cap + 1):
            vector = [0] * rank
            vector[i] = order
            atoms.append(
                (
                    tuple(vector),
                    {"kind": "vertex", "vertex": i + 1, "order": order},
                )
            )
    for i, j in graph_edges:
        for left in range(1, cap):
            for right in range(1, cap - left + 1):
                vector = [0] * rank
                vector[i] = left
                vector[j] = right
                atoms.append(
                    (
                        tuple(vector),
                        {
                            "kind": "edge",
                            "vertices": [i + 1, j + 1],
                            "orders": [left, right],
                        },
                    )
                )
    atoms.sort(key=lambda item: (sum(item[0]), item[0], json.dumps(item[1], sort_keys=True)))
    return tuple(atoms)


def physical_partition_polynomials(
    rank: int,
    graph_edges: tuple[tuple[int, int], ...],
    vectors_by_weight: tuple[tuple[tuple[int, ...], ...], ...],
    cap: int,
) -> tuple[dict[int, list[int]], dict[tuple[int, ...], dict[str, object]]]:
    """Return multiset-germ count polynomials for every vector of weight <= cap."""
    base = cap + 1
    codes_by_weight = tuple(
        tuple(encode(vector, base) for vector in layer) for layer in vectors_by_weight
    )
    dp: dict[int, list[int]] = {0: [1] + [0] * cap}
    atoms = physical_atoms(rank, graph_edges, cap)
    atom_metadata: dict[tuple[int, ...], dict[str, object]] = {}
    for vector, metadata in atoms:
        atom_metadata[vector] = metadata
        atom_weight = sum(vector)
        atom_code = encode(vector, base)
        # Standard unbounded coin-change update in increasing total weight.
        # Each atom type is processed once, so identical germs form a multiset.
        for source_weight in range(cap - atom_weight + 1):
            for source_code in codes_by_weight[source_weight]:
                source_poly = dp.get(source_code)
                if source_poly is None:
                    continue
                target_code = source_code + atom_code
                target_poly = dp.setdefault(target_code, [0] * (cap + 1))
                for germ_count in range(source_weight + 1):
                    count = source_poly[germ_count]
                    if count:
                        target_poly[germ_count + 1] += count
    return dp, atom_metadata


def summarize_physical(
    n: tuple[int, ...],
    polynomial: list[int],
    one_germ_metadata: dict[str, object] | None,
) -> dict[str, object]:
    nonzero = [index for index, count in enumerate(polynomial) if count]
    assert nonzero
    weight = sum(n)
    assert nonzero[-1] == weight
    assert polynomial[weight] == 1  # split into transverse unit vertex germs
    assert (one_germ_metadata is not None) == (nonzero[0] == 1)
    return {
        "count_by_number_of_germs": polynomial[1 : weight + 1],
        "maximum_number_of_germs": nonzero[-1],
        "minimum_number_of_germs": nonzero[0],
        "one_germ_contact": one_germ_metadata,
        "total_partition_count": sum(polynomial),
    }


def enumerate_type(kind: str, rank: int, cap: int) -> dict[str, object]:
    label = f"{kind}{rank}"
    graph_edges = edges(kind, rank)
    group = diagram_group(kind, rank)
    vectors_by_weight = tuple(
        tuple(exact_compositions(weight, rank)) for weight in range(cap + 1)
    )
    physical_dp, atom_metadata = physical_partition_polynomials(
        rank, graph_edges, vectors_by_weight, cap
    )
    base = cap + 1
    matrix = cartan(kind, rank)

    # Independent small controls for the physical-germ generating function.
    if label == "A1":
        assert physical_dp[encode((2,), base)][1:3] == [1, 1]
    elif label == "A2":
        assert physical_dp[encode((1, 1), base)][1:3] == [1, 1]
    elif label == "A4":
        assert physical_dp[encode((0, 1, 1, 0), base)][1:3] == [1, 1]
    elif label == "D4":
        assert physical_dp[encode((0, 1, 0, 0), base)][1:2] == [1]
    records: list[dict[str, object]] = []
    raw_by_weight = [0] * (cap + 1)
    orbit_by_weight = [0] * (cap + 1)
    one_germ_raw_by_weight = [0] * (cap + 1)
    one_germ_orbit_by_weight = [0] * (cap + 1)

    for weight in range(1, cap + 1):
        for n in vectors_by_weight[weight]:
            m = solve(kind, n)
            if m is None:
                continue
            assert all(value > 0 for value in m)
            assert matvec(matrix, m) == n
            raw_by_weight[weight] += 1
            one_germ = atom_metadata.get(n)
            if one_germ is not None:
                one_germ_raw_by_weight[weight] += 1

            n_orbit = orbit(n, group)
            if n != n_orbit[0]:
                continue
            m_orbit = orbit(m, group)
            assert len(m_orbit) == len(n_orbit)
            assert all(solve(kind, image) == permute(m, permutation)
                       for permutation in group
                       for image in (permute(n, permutation),))
            orbit_by_weight[weight] += 1
            if one_germ is not None:
                one_germ_orbit_by_weight[weight] += 1
            polynomial = physical_dp[encode(n, base)]
            records.append(
                {
                    "diagram_orbit_size": len(n_orbit),
                    "diagram_stabilizer_order": len(group) // len(n_orbit),
                    "m": list(m),
                    "n": list(n),
                    "physical_germs": summarize_physical(n, polynomial, one_germ),
                    "under_cap_4": weight <= SMALL_CAP,
                    "weight": weight,
                }
            )

    assert sum(record["diagram_orbit_size"] for record in records) == sum(raw_by_weight)
    for record in records:
        if record["under_cap_4"]:
            assert record["weight"] <= SMALL_CAP

    def cap_summary(limit: int) -> dict[str, object]:
        selected = [record for record in records if record["weight"] <= limit]
        canonical_by_minimum: dict[str, int] = {}
        raw_by_minimum: dict[str, int] = {}
        for record in selected:
            minimum = str(record["physical_germs"]["minimum_number_of_germs"])
            canonical_by_minimum[minimum] = canonical_by_minimum.get(minimum, 0) + 1
            raw_by_minimum[minimum] = raw_by_minimum.get(minimum, 0) + record[
                "diagram_orbit_size"
            ]
        return {
            "canonical_diagram_orbits": len(selected),
            "canonical_orbits_by_minimum_germs": canonical_by_minimum,
            "canonical_one_germ_orbits": sum(
                record["physical_germs"]["one_germ_contact"] is not None
                for record in selected
            ),
            "raw_pairs": sum(raw_by_weight[: limit + 1]),
            "raw_pairs_by_minimum_germs": raw_by_minimum,
            "raw_one_germ_pairs": sum(one_germ_raw_by_weight[: limit + 1]),
        }

    return {
        "cartan_matrix": [list(row) for row in matrix],
        "diagram_group_order": len(group),
        "diagram_group_permutations_zero_based": [list(permutation) for permutation in group],
        "edges_one_based": [[i + 1, j + 1] for i, j in graph_edges],
        "label": label,
        "rank": rank,
        "records": records,
        "summary": {
            "by_weight": {
                "canonical_diagram_orbits": orbit_by_weight[1:],
                "canonical_one_germ_orbits": one_germ_orbit_by_weight[1:],
                "raw_pairs": raw_by_weight[1:],
                "raw_one_germ_pairs": one_germ_raw_by_weight[1:],
            },
            "cap_4": cap_summary(SMALL_CAP),
            "cap_8": cap_summary(cap),
        },
        "type": kind,
    }


def build_payload() -> dict[str, object]:
    types = [enumerate_type("A", rank, MAX_CAP) for rank in range(1, 9)]
    types.extend(enumerate_type("D", rank, MAX_CAP) for rank in range(4, 10))

    def total(cap_key: str, field: str) -> int:
        return sum(entry["summary"][cap_key][field] for entry in types)

    payload: dict[str, object] = {
        "basis": "986427df23c30375b6edfd659ba8a6c6139434ab",
        "caps": [SMALL_CAP, MAX_CAP],
        "conventions": {
            "D_numbering": "chain 1--...--(r-2), fork vertices r-1,r at r-2",
            "canonical_representative": "lexicographically least Dynkin-label vector in its diagram orbit",
            "diagram_symmetry": "A reversal; D_r spin swap for r>=5; D4 full S3 on arms 1,3,4",
            "enumeration_scope": "one connected local exceptional A/D component at a time; totals are a disjoint sum over types",
            "not_enumerated": "disconnected or simultaneous D9 embeddings, global cap allocation, paired infinity data, and carrier labels",
            "physical_germ_atom": "positive contact on one vertex or on both ends of one ADE edge",
            "physical_partition_count": "unordered multisets of germ atoms; not quotiented by the representative stabilizer",
            "physical_partition_scope": "necessary numerical signatures only; no simultaneous analytic or global realizability and no carrier grouping",
            "weyl_scope": "dominance separates Weyl orbits; no Weyl quotient or geometric Weyl equivalence is applied",
        },
        "global_summary": {},
        "max_cap": MAX_CAP,
        "schema": SCHEMA,
        "types": types,
    }
    payload["global_summary"] = {
        "cap_4": {
            "canonical_diagram_orbits": total("cap_4", "canonical_diagram_orbits"),
            "canonical_one_germ_orbits": total("cap_4", "canonical_one_germ_orbits"),
            "raw_pairs": total("cap_4", "raw_pairs"),
            "raw_one_germ_pairs": total("cap_4", "raw_one_germ_pairs"),
        },
        "cap_8": {
            "canonical_diagram_orbits": total("cap_8", "canonical_diagram_orbits"),
            "canonical_one_germ_orbits": total("cap_8", "canonical_one_germ_orbits"),
            "raw_pairs": total("cap_8", "raw_pairs"),
            "raw_one_germ_pairs": total("cap_8", "raw_one_germ_pairs"),
        },
    }
    return payload


def canonical_json(payload: dict[str, object]) -> str:
    return json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, help="write canonical JSON here; default is stdout")
    parser.add_argument("--summary", action="store_true", help="print only the global/type summaries")
    parser.add_argument(
        "--deep-check",
        action="store_true",
        help="exhaustively compare every formula with Fraction Gaussian elimination",
    )
    args = parser.parse_args()

    if args.deep_check:
        print(json.dumps({"deep_check_vectors": deep_check_all()}, sort_keys=True))
    payload = build_payload()
    if args.summary:
        summary = {
            "global_summary": payload["global_summary"],
            "types": [
                {"label": entry["label"], "summary": entry["summary"]}
                for entry in payload["types"]
            ],
        }
        print(json.dumps(summary, indent=2, sort_keys=True))
        return

    rendered = canonical_json(payload)
    if args.output is None:
        print(rendered, end="")
    else:
        logical = rendered.encode("utf-8")
        logical_digest = hashlib.sha256(logical).hexdigest()
        if args.output.suffix == ".gz":
            artifact = gzip.compress(logical, compresslevel=9, mtime=0)
            args.output.write_bytes(artifact)
            compression = "gzip-9-mtime-0"
        else:
            artifact = logical
            args.output.write_bytes(artifact)
            compression = "none"
        print(
            json.dumps(
                {
                    "artifact_bytes": len(artifact),
                    "artifact_sha256": hashlib.sha256(artifact).hexdigest(),
                    "canonical_json_bytes": len(logical),
                    "canonical_json_sha256": logical_digest,
                    "compression": compression,
                    "output": str(args.output),
                },
                sort_keys=True,
            )
        )


if __name__ == "__main__":
    main()
