#!/usr/bin/env python3
"""Mechanically compare the frozen charged chart with the independent rebuild."""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import sympy as sy


HERE = Path(__file__).resolve().parent
FROZEN = Path("/tmp/jc2-lane.QNRa2r/inputs/order_chart.py")


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    charged = load("row2515_charged", FROZEN)
    rebuilt = load("row2515_rebuilt", HERE / "independent_order_gate.py")
    source_row = charged.ROWS["25_15_21_2_k2"]
    independent_row = rebuilt.DATA["open_25_15"]
    results = []
    for part in charged.allowed_partitions(source_row):
        old = charged.build_chart(source_row, part, gauged=True)
        new = rebuilt.build_chart(independent_row, part, "sparse", "identity")
        old_rows = {(item["h_power"], tuple(item["monomial"])): sy.expand(expr)
                    for item, expr in zip(old["tagged"], old["eqs"])}
        new_rows = {(item["h_power"], (item["x_power"], item["y_power"])): sy.expand(item["expr"])
                    for item in new["rows"]}
        same_keys = old_rows.keys() == new_rows.keys()
        disagreements = []
        if same_keys:
            disagreements = [key for key in old_rows if sy.expand(old_rows[key] - new_rows[key]) != 0]
        target = (0, (source_row.k, 0))
        checks = {
            "unknown_count": old["meta"]["unknowns"] == new["meta"]["unknowns_excluding_T"],
            "equation_count": old["meta"]["equations"] == new["meta"]["equations"],
            "alpha_dims": old["meta"]["alpha_dims"] == new["meta"]["alpha_dims"],
            "beta_dims": old["meta"]["beta_dims"] == new["meta"]["beta_dims"],
            "same_tag_keys": same_keys,
            "same_all_equations": same_keys and not disagreements,
            "same_saturation": sy.expand(old["sat"] - new["sat"]) == 0,
            "target_is_minus_c_charged": sy.expand(old_rows[target] + sy.Symbol("c")) == 0,
            "target_is_minus_c_rebuilt": sy.expand(new_rows[target] + sy.Symbol("c")) == 0,
        }
        if not all(checks.values()):
            raise AssertionError({"part": part, "checks": checks, "disagreements": disagreements})
        results.append({"partition": list(part), "checks": checks,
                        "unknowns": old["meta"]["unknowns"], "equations": old["meta"]["equations"],
                        "target_row": str(old_rows[target])})
    print(json.dumps(results, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
