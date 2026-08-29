#!/usr/bin/env python3
from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform
import re


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V37 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_graded_ladder_v37_20260827/solve_graded_ladder_v37.py"
V37_SHA = "ba034c8cebaa27c5630872b9cf06d152e4577170486ac34ad7f695ead871845b"
PREREG = HERE / "PREREGISTRATION_CENSUS.md"
STATUS = "PASS-A1-GRADED-LADDER-V38-CENSUS-COMPILER"
LANE_RE = re.compile(r"max12_812_order2_p0_total_rees_j2_a1_graded_ladder_v38_[0-9]{8}T[0-9]{6}Z_census_(r6d|box01)")
TARGETS = {
    17: {"a1": 1, "k": 3},
    18: {"a1": 2, "k": 2},
    19: {"a1": 3, "k": 1},
    20: {"a1": 4},
    21: {"a1": 1, "k": 4},
    22: {"a1": 2, "k": 3},
    23: {"a1": 3, "k": 2},
    24: {"a1": 4, "k": 1},
    25: {"a1": 5},
}
CONTROL_EXPECTED = {
    17: {"products": 217, "support": 1231, "component_products": 0, "component_monomials": 1, "component_nnz": 0},
    18: {"products": 426, "support": 2564, "component_products": 0, "component_monomials": 1, "component_nnz": 0},
    19: {"products": 803, "support": 5078, "component_products": 50, "component_monomials": 696, "component_nnz": 2086},
    20: {"products": 1473, "support": 8536, "component_products": 161, "component_monomials": 982, "component_nnz": 2951},
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_v37():
    if digest(V37) != V37_SHA:
        fail("V37 compiler hash")
    spec = importlib.util.spec_from_file_location("v38_census_v37", V37)
    if spec is None or spec.loader is None:
        fail("V37 compiler import")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def encode_monomial(monomial) -> list[list[object]]:
    return [[name, exponent] for name, exponent in monomial]


def target_monomial(weight: int):
    return tuple(sorted(TARGETS[weight].items()))


def compute_censi(v37, parser, rows, variables):
    censi = {}
    for weight in sorted(TARGETS):
        products = v37.build_products(weight, parser, rows, variables)
        target = target_monomial(weight)
        component_indices, component_monomials = v37.target_component(products, target)
        census = {
            "weight": weight,
            "target": encode_monomial(target),
            "products": len(products),
            "support": len({target} | {monomial for item in products for monomial in item["polynomial"]}),
            "component_products": len(component_indices),
            "component_monomials": len(component_monomials),
            "component_nnz": sum(len(products[index]["polynomial"]) for index in component_indices),
        }
        if weight in CONTROL_EXPECTED:
            actual = {key: census[key] for key in CONTROL_EXPECTED[weight]}
            if actual != CONTROL_EXPECTED[weight]:
                fail(("V37 census control", weight, actual, CONTROL_EXPECTED[weight]))
        censi[str(weight)] = census
        print(f"V38_CENSUS_W{weight}={census['component_products']}x{census['component_monomials']}")
    return censi


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("output", type=Path)
    cli.add_argument("--registered-lane", required=True)
    args = cli.parse_args()
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if (platform.system() != "Linux" or not vendor.is_file()
            or vendor.read_text().strip() != "Amazon EC2"
            or tag != args.registered_lane or LANE_RE.fullmatch(tag) is None):
        fail("registered V38 census AWS EC2 lane required")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    v37 = load_v37()
    parser, rows, row_hashes, variables = v37.load_rows()
    if len(row_hashes) != 70 or len(rows) != 51 or len(variables) != 65:
        fail("source census")
    censi = compute_censi(v37, parser, rows, variables)
    result = {
        "schema_version": 1,
        "status": STATUS,
        "registered_aws_lane": tag,
        "preregistration_sha256": digest(PREREG),
        "v37_compiler_sha256": V37_SHA,
        "row_count_named": len(row_hashes),
        "row_count_nonzero": len(rows),
        "variable_count": len(variables),
        "row_sha256": row_hashes,
        "censi": censi,
        "scope": "combinatorial census of complete fixed-weight products in homogeneous raw ordered-a1 rho-zero row ideal through grade19",
    }
    result_path = output / "census.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(STATUS)
    print(f"RESULT_SHA256={digest(result_path)}")


if __name__ == "__main__":
    main()
