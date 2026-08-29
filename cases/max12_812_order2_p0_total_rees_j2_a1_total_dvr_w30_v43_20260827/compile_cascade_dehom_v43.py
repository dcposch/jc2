#!/usr/bin/env python3
"""Compile a small exact a1=1 unit/lift problem from the V42 cascade rows."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V37 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_graded_ladder_v37_20260827/solve_graded_ladder_v37.py"
V37_SHA256 = "ba034c8cebaa27c5630872b9cf06d152e4577170486ac34ad7f695ead871845b"
SELECTED = (
    "Tg11_1",
    "Tg12_1", "Tg12_2",
    "Tg13_1", "Tg13_2", "Tg13_4",
    "Tg14_1", "Tg14_2", "Tg14_3", "Tg14_4",
    "Tg15_3", "Tg15_4",
    "Tg16_5", "Tg16_6",
    "Tg17_5", "Tg18_6", "Tg19_7",
)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_v37():
    if digest(V37) != V37_SHA256:
        fail(("V37 hash", digest(V37), V37_SHA256))
    spec = importlib.util.spec_from_file_location("v43_dehom_v37", V37)
    if spec is None or spec.loader is None:
        fail("V37 import")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def require_aws(order: str) -> str:
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if (platform.system() != "Linux" or not vendor.is_file()
            or vendor.read_text().strip() != "Amazon EC2"
            or not tag.startswith("max12_812_order2_p0_total_rees_j2_a1_total_dvr_w30_v43_")
            or f"_dehom_{order}_" not in tag):
        fail("registered V43 dehom AWS lane required")
    return tag


def canonical_polynomial(polynomial) -> bytes:
    value = [
        {
            "monomial": [[name, exponent] for name, exponent in monomial],
            "coefficient": [coefficient.numerator, coefficient.denominator],
        }
        for monomial, coefficient in sorted(polynomial.items())
    ]
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("output", type=Path)
    cli.add_argument("--order", choices=("dp", "lp"), required=True)
    cli.add_argument("--method", choices=("separate", "tracked"), default="tracked")
    args = cli.parse_args()
    tag = require_aws(args.order)
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)

    v37 = load_v37()
    parser, row_items, row_hashes, _ = v37.load_rows()
    by_name = {item["name"]: item for item in row_items}
    if len(row_hashes) != 70 or any(name not in by_name for name in SELECTED):
        fail("selected source census")
    selected = []
    for name in SELECTED:
        item = by_name[name]
        dehom = parser.specialize(item["polynomial"], frozenset(), {"a1": ()})
        if not dehom:
            fail(("zero dehom row", name))
        selected.append({**item, "dehom": dehom})
    variables = sorted({name for item in selected for monomial in item["dehom"]
                        for name, _ in monomial})
    if "a1" in variables or any(parser.sigma_weight(name) <= 0 for name in variables):
        fail(("dehom variable census", variables))

    singular_path = output / f"cascade_dehom_{args.order}.sing"
    multiplier_paths = [output / f"multiplier_{index:02d}_{item['name']}.poly"
                        for index, item in enumerate(selected, start=1)]
    lines = [
        f"ring R=0,({','.join(variables)}),{args.order};",
        "option(redSB);",
        "ideal I=",
    ]
    for index, item in enumerate(selected):
        lines.append(parser.polynomial_text(item["dehom"])
                     + ("," if index + 1 < len(selected) else ";"))
    basis_lines = (["ideal G=std(I);"] if args.method == "separate"
                   else ["matrix L; ideal G=liftstd(I,L);"])
    lines += basis_lines + [
        "print(\"V43_DEHOM_GB_SIZE=\"+string(size(G)));",
        "poly nfcheck=reduce(1,G);",
        "if (nfcheck!=0) { print(\"V43_DEHOM_OUTCOME=nonunit\"); print(nfcheck); quit; }",
    ]
    if args.method == "separate":
        lines.append("matrix L=lift(I,ideal(1));")
    lines += [
        "matrix REPLAY=matrix(I)*L;",
        "if ((size(G)!=1)||(G[1]!=1)||(nrows(REPLAY)!=1)||(ncols(REPLAY)!=1)||(REPLAY[1,1]!=1))",
        "{ print(\"FAIL_V43_DEHOM_LIFT_REPLAY\"); quit; }",
    ]
    for index, path in enumerate(multiplier_paths, start=1):
        lines.append(f"write(\"{path}\",L[{index},1]);")
    lines += [
        "print(\"V43_DEHOM_OUTCOME=unit\");",
        "print(\"V43_DEHOM_LIFT_REPLAY=1\");",
        "print(\"PASS_A1_TOTAL_DVR_W30_V43_DEHOM\");",
        "quit;",
    ]
    singular_path.write_text("\n".join(lines) + "\n")
    result = {
        "status": "PASS-A1-TOTAL-DVR-W30-V43-DEHOM-COMPILER",
        "registered_aws_lane": tag,
        "order": args.order,
        "method": args.method,
        "scope": "exact rho-zero a1=1 unit test on the full raw polynomials of the seventeen V42 cascade rows",
        "v37_sha256": V37_SHA256,
        "named_row_count": len(row_hashes),
        "selected_rows": list(SELECTED),
        "selected_source_sha256": {name: row_hashes[name] for name in SELECTED},
        "selected_polynomial_sha256": {
            item["name"]: sha256(canonical_polynomial(item["polynomial"])).hexdigest()
            for item in selected
        },
        "selected_term_counts": {item["name"]: len(item["polynomial"]) for item in selected},
        "dehom_term_counts": {item["name"]: len(item["dehom"]) for item in selected},
        "active_variables": variables,
        "active_variable_count": len(variables),
        "singular_script": str(singular_path),
        "singular_script_sha256": digest(singular_path),
        "multiplier_paths": [str(path) for path in multiplier_paths],
    }
    result_path = output / "compiler_result.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("PASS-A1-TOTAL-DVR-W30-V43-DEHOM-COMPILER")
    print(f"RESULT_SHA256={digest(result_path)}")


if __name__ == "__main__":
    main()
