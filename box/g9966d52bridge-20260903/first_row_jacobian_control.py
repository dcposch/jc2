#!/usr/bin/env python3
"""Exact common-point control for the first T2 row and Jacobian localization."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp

import bridge_engine as bridge


HERE = Path(__file__).resolve().parent


def main() -> None:
    custody = bridge.verify_frozen()
    band = bridge.load_charged_module()
    _stage, free_names, joint_map, k2, outer, endpoint = bridge.load_endpoint(band)
    jacobian = sp.expand(bridge.jacobian_scalar(band, k2, outer, joint_map))
    names = set(map(sp.Symbol, free_names))
    assert jacobian.free_symbols <= names

    row = -sp.Integer(98304) * sum(
        (-1) ** (index - 19) * sp.Symbol(f"B1c_7_{index}")
        for index in range(19, 26)
    )
    point = {symbol: sp.Integer(0) for symbol in names}
    point[sp.Symbol("c")] = 1
    point[sp.Symbol("A3c_97_1")] = -1
    point[sp.Symbol("B2c_64_0")] = 1
    row_value = sp.expand(row.xreplace(point))
    jacobian_value = sp.expand(jacobian.xreplace(point))
    assert row_value == 0
    assert jacobian_value == 1

    prefix_ledger = HERE / "t2-prefix-s63-pivots.jsonl"
    prefix_values = []
    if prefix_ledger.exists():
        for line in prefix_ledger.read_text(encoding="utf-8").splitlines():
            entry = json.loads(line)
            relation = sp.Symbol(entry["variable"]) - sp.sympify(entry["rhs"])
            prefix_values.append(sp.expand(relation.xreplace(point)))
        assert len(prefix_values) == 5
        assert all(value == 0 for value in prefix_values)

    result = {
        "type": "EXACT COMMON-POINT CONTROL / s<=63 T2 PREFIX AND JACOBIAN",
        "status": "PASS",
        "custody": {"all_match": custody["all_match"], "count": custody["count"]},
        "stage7_free": endpoint["free_count"],
        "assignment_nonzero": {"c": 1, "A3c_97_1": -1, "B2c_64_0": 1},
        "all_other_stage7_free_generators": 0,
        "first_T2_row_value": str(row_value),
        "s63_Qstar_relation_values": list(map(str, prefix_values)),
        "J0_value": str(jacobian_value),
        "J0_sha256_srepr": hashlib.sha256(sp.srepr(jacobian).encode()).hexdigest(),
        "consequence": "The five-pivot s<=63 quotient meets c*J0!=0; localization does not empty this necessary subsystem."
    }
    output = HERE / "first-row-jacobian-control.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
