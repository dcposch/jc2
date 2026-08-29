#!/usr/bin/env python3
"""Independent exact support-certificate replay for Opus5's L43 claim."""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V37 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_graded_ladder_v37_20260827/solve_graded_ladder_v37.py"
V37_SHA256 = "ba034c8cebaa27c5630872b9cf06d152e4577170486ac34ad7f695ead871845b"

FORCED = frozenset(
    "a1 aa0 aa1 e0 e1 ec3 ec4 ee0 ee1 ez3 ez4".split()
)
ZERO_SET = frozenset(
    "a1 aa0 aa1 aaa0 aaa1 cs1 cs2 e0 e1 ec3 ec4 ec5 ec6 "
    "ee0 ee1 ez3 ez4 ez5 ez6 rs1 rs2 rs3".split()
)
DISJOINT_RESIDUAL_EDGES = tuple(
    frozenset(edge.split())
    for edge in (
        "aaa0 ez7",
        "az3 ec6",
        "ac3 ez6",
        "k6_1 rs1",
        "k2c rs2",
        "aaa1 ec7",
        "cs1 k10_3",
        "k rs3",
        "az4 ec5",
        "ac4 ez5",
        "cs2 ell1 k1",
    )
)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> None:
    raise RuntimeError(message)


def load_v37():
    if digest(V37) != V37_SHA256:
        fail(("V37 compiler hash", digest(V37)))
    spec = importlib.util.spec_from_file_location("l43_review_v37", V37)
    if spec is None or spec.loader is None:
        fail("V37 import")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    v37 = load_v37()
    _, rows, row_hashes, variables = v37.load_rows()
    if len(row_hashes) != 70 or len(rows) != 51 or len(variables) != 65:
        fail(("source census", len(row_hashes), len(rows), len(variables)))

    supports = {
        frozenset(name for name, _ in monomial)
        for row in rows
        for monomial in row["polynomial"]
    }
    minimal = {
        support
        for support in supports
        if not any(other < support for other in supports)
    }
    size_census = Counter(map(len, minimal))
    if len(supports) != 4997 or len(minimal) != 88 or size_census != {1: 11, 2: 54, 3: 23}:
        fail(("support census", len(supports), len(minimal), dict(size_census)))

    singleton_vertices = frozenset(next(iter(edge)) for edge in minimal if len(edge) == 1)
    if singleton_vertices != FORCED:
        fail(("forced singleton vertices", sorted(singleton_vertices)))
    if any(edge not in minimal for edge in DISJOINT_RESIDUAL_EDGES):
        fail("lower-bound edge is not minimal")
    if any(edge & FORCED for edge in DISJOINT_RESIDUAL_EDGES):
        fail("lower-bound edge meets forced singleton set")
    for index, edge in enumerate(DISJOINT_RESIDUAL_EDGES):
        if any(edge & other for other in DISJOINT_RESIDUAL_EDGES[index + 1 :]):
            fail(("lower-bound edges not disjoint", sorted(edge)))

    if len(ZERO_SET) != 22 or not all(edge & ZERO_SET for edge in minimal):
        fail("candidate zero set is not a 22-vertex hitting set")
    if any(not (support & ZERO_SET) for support in supports):
        fail("a monomial survives the candidate coordinate restriction")

    maximality_witness = {}
    for variable in sorted(ZERO_SET):
        witnesses = sorted(
            (tuple(sorted(edge)) for edge in minimal if edge & ZERO_SET == {variable}),
            key=lambda edge: (len(edge), edge),
        )
        if not witnesses:
            fail(("no inclusion-maximality witness", variable))
        maximality_witness[variable] = list(witnesses[0])

    # Every hitting set contains the 11 singleton vertices and at least one
    # vertex from each of the 11 pairwise-disjoint residual edges.  Hence its
    # size is at least 22.  ZERO_SET attains 22, so the minimum is exactly 22.
    result = {
        "status": "PASS-L43-SUPPORT-CERTIFICATE-INDEPENDENT-REPLAY",
        "scope": (
            "maximum coordinate-linear zero section of the homogeneous raw "
            "ordered-a1 rho-zero row system through grade19 only"
        ),
        "v37_compiler_sha256": V37_SHA256,
        "named_row_count": len(row_hashes),
        "nonzero_row_count": len(rows),
        "variable_count": len(variables),
        "distinct_monomial_support_count": len(supports),
        "minimal_support_count": len(minimal),
        "minimal_support_size_census": {str(key): size_census[key] for key in sorted(size_census)},
        "forced_singleton_vertices": sorted(FORCED),
        "pairwise_disjoint_residual_edges": [sorted(edge) for edge in DISJOINT_RESIDUAL_EDGES],
        "minimum_hitting_set_size": 22,
        "maximum_coordinate_zero_section_dimension": 43,
        "attaining_zero_set": sorted(ZERO_SET),
        "free_set": sorted(set(variables) - ZERO_SET),
        "contains_free_k": "k" not in ZERO_SET,
        "contains_free_a1": "a1" not in ZERO_SET,
        "inclusion_maximality_witness": maximality_witness,
        "firewalls": [
            "no all-depth claim",
            "no general-rho claim beyond separately available rows",
            "no irreducible-component claim",
            "no saturated-Rees, honest-receiver, chart, Gate-T, or JC2 inference",
        ],
    }
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
