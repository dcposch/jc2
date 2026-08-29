#!/usr/bin/env python3
"""Exact replay of the labelled one-P0 U2 td12 budget obstruction."""

from __future__ import annotations

from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
CLOSURE_PATH = (
    ROOT
    / "cases/m2_finite_reduced_chain_skeleton_r2_20260829"
    / "finite_chain_skeleton_r2.py"
)
EXPECTED_CLOSURE_SHA256 = (
    "b6f363407af9ea16f83bb5c0b7ff5c659e0e69b372ef2ace47d1f53b8b768afb"
)
EXPECTED_STATE_TABLE_SHA256 = (
    "c2835aaf8450ab938170ae3808b5852d53f2c7b1ae29b14ca77b7965bf37f1ad"
)


def require(condition: bool, label: str) -> None:
    if not condition:
        raise RuntimeError(f"CHECK_FAILED:{label}")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_closure_module():
    require(sha256_file(CLOSURE_PATH) == EXPECTED_CLOSURE_SHA256,
            "closure-source-hash")
    spec = importlib.util.spec_from_file_location("finite_chain_r2_frozen",
                                                  CLOSURE_PATH)
    require(spec is not None and spec.loader is not None,
            "closure-import-spec")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    closure = load_closure_module()
    seed_w = Fraction(3, 2)
    seed_M = 2

    payload = closure.close_reduced_skeleton(seed_w, seed_M, 5)
    require(payload["cap_free"] is True, "closure-cap-free")
    require(payload["state_count"] == 69, "closure-state-count")
    require(payload["state_table_sha256"] == EXPECTED_STATE_TABLE_SHA256,
            "closure-state-table-hash")
    require(payload["zero_cost_reduced_nonincrease"] is True,
            "zero-cost-monotonicity")

    inner_targets = sorted(
        (row["w"], row["M"], row["lambda_min"])
        for row in payload["states"]
        if Fraction(row["w"]) == 1 and row["M"] % 3 == 0
    )
    require(inner_targets == [("1", 3, 5)],
            "inner-w1-multiple3-minimum")

    predecessor = payload["first_predecessor"]
    require(predecessor["3/4|4"]["step"]["lambda"] == 2,
            "inner-witness-first-price")
    require(predecessor["1|3"]["parent"] ==
            {"w": "3/4", "M": 4, "lambda": 2},
            "inner-witness-parent")
    require(predecessor["1|3"]["step"]["lambda"] == 3,
            "inner-witness-second-price")

    zero_payload = closure.close_reduced_skeleton(seed_w, seed_M, 0)
    require(all(Fraction(row["w"]) <= seed_w
                for row in zero_payload["states"]),
            "zero-price-cannot-increase-weight")
    require(not any(Fraction(row["w"]) == 2
                    for row in zero_payload["states"]),
            "outer-sibling-not-zero-price")

    alpha, beta = 2, 3
    pole_a, pole_b, pole_nu = 1, 2, 3
    pole_mass = pole_a * pole_b * alpha * beta // pole_nu
    entry_kbar = pole_a * (alpha + beta)
    entry_rho = Fraction(pole_a, pole_b)
    entry_w = Fraction(entry_kbar, 1) - entry_rho
    entry_w /= pole_nu
    require(pole_mass == 4 and entry_w == seed_w and pole_b == seed_M,
            "forced-pole-entry")

    inner_dp, inner_dq, inner_kbar, arrival_mu = 6, 3, 3, 3
    inner_X = Fraction(inner_kbar * inner_dp, inner_dq)
    required_inner_w = Fraction(inner_kbar, 1) - inner_X / arrival_mu
    require(required_inner_w == 1, "corrected-inner-arrival-weight")

    required_outer_sibling_w = Fraction(2)
    require(required_outer_sibling_w > entry_w,
            "outer-sibling-needs-positive-price")

    td = 3 * pole_mass
    global_budget = td - 2
    inner_pair_floor = 2 * inner_targets[0][2]
    sibling_floor = 1
    route_floor = inner_pair_floor + sibling_floor
    require(td == 12 and global_budget == 10, "td12-global-budget")
    require(route_floor == 11 and route_floor > global_budget,
            "labelled-route-budget-contradiction")

    result = {
        "schema": "M2-U2-ONE-P0-TD12-BUDGET-KILL/v1",
        "scope": "LABELLED_ROUTE_ACTUAL_LANDING_ONLY",
        "closure": {
            "input": {"w": "3/2", "M": 2, "budget": 5},
            "state_count": payload["state_count"],
            "state_table_sha256": payload["state_table_sha256"],
            "inner_target": {"w": "1", "M": 3, "lambda_min": 5},
        },
        "forced_entry": {"a": 1, "b": 2, "nu": 3,
                         "mass": 4, "w": "3/2", "M": 2},
        "prices": {"inner_1": 5, "inner_2": 5,
                   "outer_sibling": 1, "total_floor": 11},
        "global_budget": {"td": 12, "upper_bound": 10},
        "verdict": "LABELLED_ONE_P0_U2_TD12_ROUTE_DEAD_CONDITIONAL",
        "firewall": {"other_u2_routes": False, "all_td12": False,
                     "landing": False, "realizability": False,
                     "jc2": False},
    }
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
