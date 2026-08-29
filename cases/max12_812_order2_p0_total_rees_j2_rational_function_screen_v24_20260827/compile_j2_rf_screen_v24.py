#!/usr/bin/env python3
"""Compile the frozen V23R1 charts into a degree-15 coefficient-field screen."""

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
V23 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_typed_census_v23_20260827"
V23_RESULT = V23 / "output_r1/RESULT.json"
V23_RESULT_SHA256 = "ce4d0adbbe94e1337bed5047da0417e3b17cb86530715fb62316086cabd14641"
V23_PARSER = V23 / "census_j2_typed_v23.py"
V23_PARSER_SHA256 = "14f2de22d8cabaea12ac7fc7bf72cca275edbbb6a35dc7c0556a6e18e67c4501"
NAME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_]*$")


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> None:
    if platform.system() != "Linux" or not os.environ.get("JC2_REGISTERED_AWS_LANE"):
        fail("registered AWS lane required")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.exists() or vendor.read_text().strip() != "Amazon EC2":
        fail("Amazon EC2 DMI identity required")


def load_parser():
    if digest(V23_PARSER) != V23_PARSER_SHA256:
        fail(("V23 parser hash", digest(V23_PARSER), V23_PARSER_SHA256))
    spec = importlib.util.spec_from_file_location("v24_frozen_v23_parser", V23_PARSER)
    if spec is None or spec.loader is None:
        fail("cannot load V23 parser")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def singular_script(chart: str, characteristic: int, records: list[tuple[str, int, str]], parser, output: Path) -> tuple[str, list[str], list[int]]:
    parameter_names = ["qa1", "rho"] if chart == "a0_chart" else ["rho"]
    exceptional = "a0" if chart == "a0_chart" else "a1"
    variables: set[str] = {exceptional}
    parsed = []
    grade10_zero = 0
    rho_odd = 0
    for name, grade, text in records:
        polynomial = parser.parse_node(parser.ast.parse(text.replace("^", "**"), mode="eval"))
        if grade == 10 and not polynomial:
            grade10_zero += 1
        for monomial in polynomial:
            if sum(parser.sigma_weight(variable) * exponent for variable, exponent in monomial) != grade:
                fail(("chart sigma homogeneity", chart, name, monomial))
            rho_exponent = next((exponent for variable, exponent in monomial if variable == "rho"), 0)
            rho_odd += rho_exponent % 2
            variables.update(variable for variable, _ in monomial if variable not in parameter_names)
        parsed.append((name, grade, text, bool(polynomial)))
    if grade10_zero != 7 or rho_odd:
        fail(("chart controls", chart, grade10_zero, rho_odd))
    if any(not NAME_RE.match(name) for name in variables | set(parameter_names)):
        fail(("unsafe identifier", sorted(variables | set(parameter_names))))

    ordered = sorted(variables, key=lambda name: (parser.sigma_weight(name), name))
    weights = [parser.sigma_weight(name) for name in ordered]
    if any(weight <= 0 for weight in weights):
        fail(("nonpositive ring weight", chart, list(zip(ordered, weights))))
    nonzero = [(name, grade, text) for name, grade, text, present in parsed if present]
    positive = next((name for name, grade, _ in nonzero if grade == 11), None)
    if positive is None:
        fail(("missing grade-11 positive control", chart))

    coeff = f"({characteristic}," + ",".join(parameter_names) + ")"
    ring_vars = "(" + ",".join(ordered) + ")"
    order = "wp(" + ",".join(map(str, weights)) + ")"
    lines = [
        f"ring R={coeff},{ring_vars},{order};",
        "option(redSB);",
    ]
    for name, _, text in nonzero:
        lines.append(f"poly P_{name}={text};")
    generator_names = [f"P_{name}" for name, _, _ in nonzero]
    lines += [
        "ideal I=" + ",".join(generator_names) + ";",
        "degBound=15;",
        "ideal G=std(I);",
        f"poly negative_control={exceptional}^2;",
        "poly negative_nf=reduce(negative_control,G);",
        "if (negative_nf!=negative_control) { print(\"FAIL_NEGATIVE_CONTROL\"); quit; }",
        f"if (reduce(P_{positive},G)!=0) {{ print(\"FAIL_POSITIVE_CONTROL\"); quit; }}",
        f"poly target={exceptional}^3;",
        "poly target_nf=reduce(target,G);",
        f"print(\"V24_CHART={chart}\");",
        f"print(\"V24_CHARACTERISTIC={characteristic}\");",
        "print(\"V24_GENERATORS=\"+string(size(I)));",
        "print(\"V24_G_SIZE=\"+string(size(G)));",
        "print(\"V24_CONTROLS=1\");",
        "if (target_nf==0)",
        "{",
        "  matrix L=lift(I,ideal(target));",
        "  poly replay=-target;",
        "  int j;",
        "  for (j=1; j<=size(I); j=j+1) { replay=replay+L[j,1]*I[j]; }",
        "  if (replay!=0) { print(\"FAIL_LIFT_REPLAY\"); quit; }",
        f"  write(\":w {output / 'LIFT.txt'}\",string(L));",
        "  print(\"V24_TARGET_RF_MEMBERSHIP=1\");",
        "  print(\"V24_LIFT_REPLAY=1\");",
        "}",
        "else",
        "{",
        f"  write(\":w {output / 'TARGET_NF.txt'}\",string(target_nf));",
        "  print(\"V24_TARGET_RF_MEMBERSHIP=0\");",
        "  print(\"V24_TARGET_NF_NONZERO=1\");",
        "}",
        "print(\"PASS_J2_RF_SCREEN_V24\");",
        "quit;",
    ]
    return "\n".join(lines) + "\n", ordered, weights


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--chart", choices=("a0_chart", "a1_ordered"), required=True)
    ap.add_argument("--characteristic", choices=(0, 65521), type=int, default=0)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    require_aws()
    output = args.output.resolve()
    if output.exists():
        fail(("refuse overwrite", str(output)))
    output.mkdir(parents=True)
    if digest(V23_RESULT) != V23_RESULT_SHA256:
        fail(("V23 result hash", digest(V23_RESULT), V23_RESULT_SHA256))
    parser = load_parser()
    result = json.loads(V23_RESULT.read_text())
    if result.get("status") != "PASS-J2-TYPED-PREFIX-CENSUS-V23R1" or result.get("input_rows") != 42:
        fail("V23 result contract")

    records = []
    input_hashes = {}
    for name, record in sorted(result["records"].items(), key=lambda item: (item[1]["grade"], item[1]["row"])):
        chart_record = record["charts"][args.chart]
        path = V23 / "output_r1" / chart_record["output"]
        expected = chart_record["output_sha256"]
        if digest(path) != expected:
            fail(("chart polynomial hash", name, digest(path), expected))
        records.append((name, int(record["grade"]), path.read_text().strip()))
        input_hashes[str(path.relative_to(ROOT))] = expected

    script_text, variables, weights = singular_script(
        args.chart, args.characteristic, records, parser, output
    )
    script = output / "screen.sing"
    script.write_text(script_text)
    compiled = {
        "status": "PASS-J2-RF-SCREEN-V24-COMPILER",
        "chart": args.chart,
        "characteristic": args.characteristic,
        "v23_result_sha256": V23_RESULT_SHA256,
        "v23_parser_sha256": V23_PARSER_SHA256,
        "input_rows": 42,
        "input_sha256": input_hashes,
        "coefficient_parameters": ["qa1", "rho"] if args.chart == "a0_chart" else ["rho"],
        "ring_variables": variables,
        "ring_weights": weights,
        "target": "a0^3" if args.chart == "a0_chart" else "a1^3",
        "degree_bound": 15,
        "script": str(script),
        "script_sha256": digest(script),
    }
    result_path = output / "compile_result.json"
    result_path.write_text(json.dumps(compiled, sort_keys=True, indent=2) + "\n")
    print("PASS-J2-RF-SCREEN-V24-COMPILER")
    print(f"CHART={args.chart}")
    print(f"SCRIPT_SHA256={digest(script)}")
    print(f"RESULT_SHA256={digest(result_path)}")


if __name__ == "__main__":
    main()

