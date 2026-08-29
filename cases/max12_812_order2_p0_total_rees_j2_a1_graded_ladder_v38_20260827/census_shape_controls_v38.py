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
PRIMARY = HERE / "census_graded_ladder_v38.py"
PRIMARY_SHA = "55892916a5f561e6b71ab1ccbb233480ff6dabc96c0ee828ddf0ec8e74e08a14"
PREREG = HERE / "PREREGISTRATION_CONTROL_ADDENDUM.md"
STATUS = "PASS-A1-GRADED-LADDER-V38-CONTROL-CENSUS-COMPILER"
SCOPE = "complete combinatorial censi for a1^i*k^j with i>=1 and sigma weight<=25 in homogeneous raw ordered-a1 rho-zero row ideal through grade19"
LANE_RE = re.compile(r"max12_812_order2_p0_total_rees_j2_a1_graded_ladder_v38_[0-9]{8}T[0-9]{6}Z_control_census_(r6d|box01)")
TARGETS = {
    f"i{i}_j{j}": {"weight": 5 * i + 4 * j, "a1_exponent": i, "k_exponent": j}
    for i in range(1, 6) for j in range(0, 6) if 5 * i + 4 * j <= 25
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_primary():
    if digest(PRIMARY) != PRIMARY_SHA:
        fail("primary census compiler hash")
    spec = importlib.util.spec_from_file_location("v38_control_primary", PRIMARY)
    if spec is None or spec.loader is None:
        fail("primary census compiler import")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def target_monomial(label: str):
    record = TARGETS[label]
    entries = [("a1", record["a1_exponent"])]
    if record["k_exponent"]:
        entries.append(("k", record["k_exponent"]))
    return tuple(sorted(entries))


def compute_censi(primary, v37, parser, rows, variables):
    products_by_weight = {}
    censi = {}
    for label in sorted(TARGETS):
        weight = TARGETS[label]["weight"]
        products = products_by_weight.setdefault(weight, v37.build_products(weight, parser, rows, variables))
        target = target_monomial(label)
        component_indices, component_monomials = v37.target_component(products, target)
        census = {
            "label": label,
            "weight": weight,
            "a1_exponent": TARGETS[label]["a1_exponent"],
            "k_exponent": TARGETS[label]["k_exponent"],
            "target": primary.encode_monomial(target),
            "products": len(products),
            "support": len({target} | {monomial for item in products for monomial in item["polynomial"]}),
            "component_products": len(component_indices),
            "component_monomials": len(component_monomials),
            "component_nnz": sum(len(products[index]["polynomial"]) for index in component_indices),
        }
        censi[label] = census
        print(f"V38_CONTROL_{label}_W{weight}={census['component_products']}x{census['component_monomials']}")
    if len(censi) != 16:
        fail("target census")
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
        fail("registered V38 control-census AWS EC2 lane required")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    primary = load_primary()
    v37 = primary.load_v37()
    parser, rows, row_hashes, variables = v37.load_rows()
    if len(row_hashes) != 70 or len(rows) != 51 or len(variables) != 65:
        fail("source census")
    censi = compute_censi(primary, v37, parser, rows, variables)
    result = {
        "schema_version": 1,
        "status": STATUS,
        "registered_aws_lane": tag,
        "preregistration_sha256": digest(PREREG),
        "primary_census_compiler_sha256": PRIMARY_SHA,
        "row_count_named": len(row_hashes),
        "row_count_nonzero": len(rows),
        "variable_count": len(variables),
        "row_sha256": row_hashes,
        "censi": censi,
        "scope": SCOPE,
    }
    result_path = output / "census.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(STATUS)
    print(f"RESULT_SHA256={digest(result_path)}")


if __name__ == "__main__":
    main()
