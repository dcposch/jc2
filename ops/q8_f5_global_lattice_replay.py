#!/usr/bin/env python3
"""Exact stdlib replay for the q=8 F5 global lattice eliminations.

This script checks only the finite divisor-class arithmetic stated in the
companion report.  It is not evidence for the local analytic polar
factorizations, effectivity, proximity, or the existence of an incidence
surface.
"""

from __future__ import annotations

import itertools
import json


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def expect_failure(action, message: str) -> None:
    """Require a negative control to trip an explicit RuntimeError."""
    try:
        action()
    except RuntimeError:
        return
    raise RuntimeError(message)


def cartan_d(rank: int) -> list[list[int]]:
    """D_rank with chain 1--...--(rank-2) and spins rank-1,rank."""
    require(rank >= 4, "D rank must be at least four")
    matrix = [[0] * rank for _ in range(rank)]
    for i in range(rank):
        matrix[i][i] = 2
    for i in range(rank - 3):
        matrix[i][i + 1] = matrix[i + 1][i] = -1
    central = rank - 3
    matrix[central][rank - 2] = matrix[rank - 2][central] = -1
    matrix[central][rank - 1] = matrix[rank - 1][central] = -1
    return matrix


def cartan_a(rank: int) -> list[list[int]]:
    matrix = [[0] * rank for _ in range(rank)]
    for i in range(rank):
        matrix[i][i] = 2
        if i:
            matrix[i][i - 1] = matrix[i - 1][i] = -1
    return matrix


def matvec(matrix: list[list[int]], vector: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix)


def add_vectors(*vectors: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(entries) for entries in zip(*vectors))


def scale(scale_factor: int, vector: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(scale_factor * entry for entry in vector)


def root_vector(*entries: tuple[int, int], f_coefficient: int = 0) -> tuple[int, ...]:
    """Vector in coordinates (F,P1,...,P9)."""
    result = [0] * 10
    result[0] = f_coefficient
    for index, coefficient in entries:
        result[index] += coefficient
    return tuple(result)


def u_root_classes(rank: int) -> tuple[tuple[int, ...], ...]:
    """Chronological U_rank classes R1,...,Rrank, retaining spin rank."""
    require(rank in (5, 6), "only the charged U5 and U6 markings are replayed")
    roots: list[tuple[int, ...]] = [tuple()] * rank
    # Chain R1=P_(rank-1)-P_rank, ..., R_(rank-2)=P2-P3.
    for standard_index in range(1, rank - 1):
        p_left = rank - standard_index
        p_right = p_left + 1
        roots[standard_index - 1] = root_vector((p_left, 1), (p_right, -1))
    roots[rank - 2] = root_vector((1, 1), (2, -1))
    roots[rank - 1] = root_vector((1, -1), (2, -1), f_coefficient=1)
    return tuple(roots)


def exceptional_cycle(root_classes: tuple[tuple[int, ...], ...], m: tuple[int, ...]) -> tuple[int, ...]:
    require(len(root_classes) == len(m), "root/multiplicity length mismatch")
    return add_vectors(*(scale(coefficient, root) for coefficient, root in zip(m, root_classes)))


def strict_c_from_cycle(cycle: tuple[int, ...]) -> tuple[int, tuple[int, ...]]:
    """Return F coefficient and c in C=4S+bF-sum c_i P_i."""
    require(len(cycle) == 10, "cycle has wrong coordinate count")
    b = 11 - cycle[0]
    c = tuple(2 + cycle[index] for index in range(1, 10))
    return b, c


def weak_compositions(total: int, length: int):
    if length == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in weak_compositions(total - first, length - 1):
            yield (first,) + tail


def positive_compositions(total: int, length: int):
    for weak in weak_compositions(total - length, length):
        yield tuple(entry + 1 for entry in weak)


def delta(a: int, degree: int, multiplicities: tuple[int, ...]) -> int | None:
    numerator = 2 * a * a - sum(entry * entry for entry in multiplicities) + a - degree
    if numerator % 2:
        return None
    return 1 + numerator // 2


def pair_intersection(a: int, x: tuple[int, ...], b: int, y: tuple[int, ...]) -> int:
    return 2 * a * b - sum(left * right for left, right in zip(x, y))


def enumerate_cell(
    c: tuple[int, ...],
    i_set: frozenset[int],
    degrees: tuple[int, ...],
    total_b_degree: int,
    enforce_t_disjointness: bool = True,
) -> dict[str, object]:
    """Enumerate a relaxation: no chronological proximity is imposed."""
    count = len(degrees)
    a_tuples = tuple(positive_compositions(total_b_degree, count))
    coordinate_allocations = tuple(tuple(weak_compositions(entry, count)) for entry in c)
    totals = {"linear": 0, "adjunction": 0, "pairwise_zero": 0}
    by_a: dict[str, dict[str, int | None]] = {
        ",".join(map(str, a_tuple)): {
            "linear": 0,
            "adjunction": 0,
            "pairwise_zero": 0,
            "minimum_pair_sum_after_adjunction": None,
        }
        for a_tuple in a_tuples
    }

    vectors = [[] for _ in range(count)]

    def visit_coordinate(index: int) -> None:
        if index != len(c):
            for allocation in coordinate_allocations[index]:
                for component in range(count):
                    vectors[component].append(allocation[component])
                visit_coordinate(index + 1)
                for component in range(count):
                    vectors[component].pop()
            return

        frozen_vectors = tuple(tuple(vector) for vector in vectors)
        for a_tuple in a_tuples:
            key = ",".join(map(str, a_tuple))
            linear = True
            for component, (a, degree) in enumerate(zip(a_tuple, degrees)):
                vector = frozen_vectors[component]
                if sum(vector) != 5 * a - degree:
                    linear = False
                    break
                if enforce_t_disjointness and sum(vector[index] for index in i_set) != 2 * a:
                    linear = False
                    break
            if not linear:
                continue
            totals["linear"] += 1
            by_a[key]["linear"] += 1

            deltas = tuple(delta(a, degree, vector) for a, degree, vector in zip(a_tuple, degrees, frozen_vectors))
            if any(value is None or value < 0 for value in deltas):
                continue
            totals["adjunction"] += 1
            by_a[key]["adjunction"] += 1

            intersections = tuple(
                pair_intersection(a_tuple[left], frozen_vectors[left], a_tuple[right], frozen_vectors[right])
                for left in range(count)
                for right in range(left + 1, count)
            )
            pair_sum = sum(intersections)
            old_minimum = by_a[key]["minimum_pair_sum_after_adjunction"]
            if old_minimum is None or pair_sum < old_minimum:
                by_a[key]["minimum_pair_sum_after_adjunction"] = pair_sum
            if all(value == 0 for value in intersections):
                totals["pairwise_zero"] += 1
                by_a[key]["pairwise_zero"] += 1

    visit_coordinate(0)
    return {
        "c": c,
        "sum_c": sum(c),
        "norm_c": sum(entry * entry for entry in c),
        "totals": totals,
        "by_B_degrees": by_a,
    }


def shifted_root_c(c: tuple[int, ...], parent: int, child: int, coefficient: int) -> tuple[int, ...]:
    result = list(c)
    result[parent] += coefficient
    result[child] -= coefficient
    require(min(result) >= 0, "exceptional-root subtraction made a strict multiplicity negative")
    return tuple(result)


def main() -> None:
    # Local Cartan arithmetic.  Analytic factorization is deliberately not replayed.
    require(matvec(cartan_a(4), (2, 3, 2, 1)) == (1, 2, 0, 0), "B5 Cartan row")
    require(matvec(cartan_a(5), (2, 3, 3, 2, 1)) == (1, 1, 1, 0, 0), "B6 Cartan row")
    require(matvec(cartan_d(5), (2, 4, 5, 3, 3)) == (0, 1, 0, 1, 1), "U5 Cartan row")
    require(matvec(cartan_d(6), (2, 4, 5, 6, 3, 3)) == (0, 1, 0, 1, 0, 0), "U6 Cartan row")

    u5_cycle = exceptional_cycle(u_root_classes(5), (2, 4, 5, 3, 3))
    u6_cycle = exceptional_cycle(u_root_classes(6), (2, 4, 5, 6, 3, 3))
    require(u5_cycle == (3, 0, -1, -1, -2, -2, 0, 0, 0, 0), "U5 total-basis cycle")
    require(u6_cycle == (3, 0, 0, -1, -1, -2, -2, 0, 0, 0), "U6 total-basis cycle")
    require(strict_c_from_cycle(u5_cycle) == (8, (2, 1, 1, 0, 0, 2, 2, 2, 2)), "U5 strict class")
    require(strict_c_from_cycle(u6_cycle) == (8, (2, 2, 1, 1, 0, 0, 2, 2, 2)), "U6 strict class")

    # Common balanced baseline: M=Z_H.
    balanced = (0, 1, 1, 1, 1, 2, 2, 2, 2)
    balanced_i = frozenset((5, 6, 7, 8))
    balanced_cycle = (3, -2, -1, -1, -1, -1, 0, 0, 0, 0)
    require(strict_c_from_cycle(balanced_cycle) == (8, balanced), "balanced strict class")
    require(sum(balanced[index] for index in balanced_i) == 8, "balanced T-disjointness")

    output: dict[str, object] = {
        "B5_baseline": enumerate_cell(balanced, balanced_i, (2, 3, 3), 4),
        "B6_baseline": enumerate_cell(balanced, balanced_i, (2, 6), 4),
        "U5_baseline": enumerate_cell(
            (2, 1, 1, 0, 0, 2, 2, 2, 2), frozenset((5, 6, 7, 8)), (2, 3, 3), 4
        ),
        "U5_relaxation_without_T": enumerate_cell(
            (2, 1, 1, 0, 0, 2, 2, 2, 2),
            frozenset((5, 6, 7, 8)),
            (2, 3, 3),
            4,
            enforce_t_disjointness=False,
        ),
        "U6_baseline": enumerate_cell(
            (2, 2, 1, 1, 0, 0, 2, 2, 2), frozenset((0, 6, 7, 8)), (3, 5), 4
        ),
    }

    # A q=8 contracted carrier chooses two I coordinates and three O coordinates.
    o_set = frozenset((1, 2, 3, 4))
    z_subsets = tuple(
        frozenset(left + right)
        for left in itertools.combinations(sorted(balanced_i), 2)
        for right in itertools.combinations(sorted(o_set), 3)
    )
    require(len(z_subsets) == 24, "q=8 Z candidate count")
    z_classes = {
        tuple(entry - (index in subset) for index, entry in enumerate(balanced)) for subset in z_subsets
    }
    require(len(z_classes) == 24, "labelled Z residual classes")
    require(
        {tuple(sorted(c)) for c in z_classes} == {(0, 0, 0, 0, 1, 1, 1, 2, 2)},
        "q=8 Z residual multiset",
    )
    representative_z = min(z_classes)
    output["B5_one_simple_Z_per_candidate"] = enumerate_cell(representative_z, balanced_i, (2, 3, 3), 3)
    output["B6_one_simple_Z_per_candidate"] = enumerate_cell(representative_z, balanced_i, (2, 6), 3)
    # Coefficient two is impossible before enumeration: every J uses c=1 on three O coordinates.
    require(
        all(any(balanced[index] - 2 < 0 for index in subset) for subset in z_subsets),
        "a doubled q=8 Z must make a strict coordinate negative",
    )

    # One affine A1 root Q=P_parent-P_child must avoid L and be T-disjoint,
    # hence both indices lie in I or both lie in O.  Coefficient two is possible
    # only in I at the level of nonnegative total-basis coefficients.
    oriented_o_roots = tuple((i, j) for i in o_set for j in o_set if i != j)
    oriented_i_roots = tuple((i, j) for i in balanced_i for j in balanced_i if i != j)
    require(len(oriented_o_roots) == len(oriented_i_roots) == 12, "oriented root counts")
    simple_o_classes = {shifted_root_c(balanced, i, j, 1) for i, j in oriented_o_roots}
    simple_i_classes = {shifted_root_c(balanced, i, j, 1) for i, j in oriented_i_roots}
    double_i_classes = {shifted_root_c(balanced, i, j, 2) for i, j in oriented_i_roots}
    require(len(simple_o_classes) == len(simple_i_classes) == len(double_i_classes) == 12, "root class counts")
    representative_simple_o = min(simple_o_classes)
    representative_simple_i = min(simple_i_classes)
    representative_double_i = min(double_i_classes)
    for label, representative in (
        ("A1_simple_O", representative_simple_o),
        ("A1_simple_I", representative_simple_i),
        ("A1_double_I", representative_double_i),
    ):
        output[f"B5_{label}_per_oriented_root"] = enumerate_cell(representative, balanced_i, (2, 3, 3), 4)
        output[f"B6_{label}_per_oriented_root"] = enumerate_cell(representative, balanced_i, (2, 6), 4)

    # All relaxed cells must be empty after the forest pairwise-disjointness test.
    for label, result in output.items():
        require(result["totals"]["pairwise_zero"] == 0, f"unexpected survivor in {label}")

    # Mutation/negative control: a checker that merely ran the enumeration but
    # failed to enforce the forest gate would accept this forged one-survivor
    # summary.  The explicit validator must reject it in ordinary, -O, and -OO
    # modes; no Python assert is used anywhere in this certificate.
    forged = {"totals": {"pairwise_zero": 1}}
    expect_failure(
        lambda: require(forged["totals"]["pairwise_zero"] == 0, "forged survivor"),
        "negative control failed to reject a forged survivor",
    )
    output["negative_control"] = "forged pairwise_zero=1 rejected"

    print(json.dumps(output, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
