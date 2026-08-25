#!/usr/bin/env python3
"""Compute the exact two-block multihomogeneous Bezout bound of the six rows."""

from __future__ import annotations

from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
COMPILER = ROOT / "cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py"
COMPILER_SHA256 = "22b0cdc446d1e486d08757df5a3fff83b0506a492f16b9b2cf238966eb947545"


def load_compiler():
    assert sha256(COMPILER.read_bytes()).hexdigest() == COMPILER_SHA256
    spec = importlib.util.spec_from_file_location("q8_multihom_compiler", COMPILER)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    compiler = load_compiler()
    _, rows, imposed, names = compiler.compile_quotient("approx")
    assert names == ["w", "c", "d2", "d4", "x1", "x3", "x5"]
    bidegrees = []
    variable_degrees = []
    support_profiles = {}
    for ell in imposed:
        profile = sorted({
            (sum(monomial[1:4]), sum(monomial[4:7]))
            for monomial in rows[ell]
        })
        normal_degree = max(pair[0] for pair in profile)
        invariant_degree = max(pair[1] for pair in profile)
        bidegrees.append((normal_degree, invariant_degree))
        variable_degrees.append([
            max(monomial[index] for monomial in rows[ell])
            for index in range(1, 7)
        ])
        support_profiles[str(ell)] = profile

    # Coefficients of product_i (a_i*A+b_i*B), truncated to A^3 B^3.
    coefficients = {(0, 0): 1}
    for normal_degree, invariant_degree in bidegrees:
        updated = {}
        for (a_power, b_power), coefficient in coefficients.items():
            if a_power < 3:
                key = (a_power + 1, b_power)
                updated[key] = updated.get(key, 0) + coefficient * normal_degree
            if b_power < 3:
                key = (a_power, b_power + 1)
                updated[key] = updated.get(key, 0) + coefficient * invariant_degree
        coefficients = updated

    # Six one-variable P1 blocks.  The coefficient of X1...X6 is the
    # permanent of the componentwise degree matrix, computed by subset DP.
    permanent_dp = {0: 1}
    for degree_row in variable_degrees:
        updated = {}
        for mask, coefficient in permanent_dp.items():
            for column, degree in enumerate(degree_row):
                if degree and not (mask >> column) & 1:
                    new_mask = mask | (1 << column)
                    updated[new_mask] = updated.get(new_mask, 0) + coefficient * degree
        permanent_dp = updated
    payload = {
        "status": "PASS",
        "variables": names,
        "normal_block": ["c", "d2", "d4"],
        "invariant_block": ["x1", "x3", "x5"],
        "imposed_rows": list(imposed),
        "row_bidegrees": [list(pair) for pair in bidegrees],
        "one_variable_degree_matrix": variable_degrees,
        "coefficient_X1_through_X6": permanent_dp.get((1 << 6) - 1, 0),
        "support_bidegree_profiles": support_profiles,
        "coefficient_A3_B3": coefficients.get((3, 3), 0),
        "interpretation": (
            "ordinary two-block multihomogeneous Bezout upper bound after "
            "bihomogenizing each row to its componentwise maximum bidegree"
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
