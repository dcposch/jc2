#!/usr/bin/env python3
"""Compile the selected-cascade total-t dehomogenized eliminant experiment."""

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
TOTAL_COMPILER = HERE / "compile_total_dvr_w30_v43.py"
TOTAL_COMPILER_SHA256 = "0de6a2b279aeeab8c5a635c1d7658958f3f49f0f94f8473355d281cae9438b00"
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


def load_total_compiler():
    if digest(TOTAL_COMPILER) != TOTAL_COMPILER_SHA256:
        fail(("total compiler hash", digest(TOTAL_COMPILER), TOTAL_COMPILER_SHA256))
    spec = importlib.util.spec_from_file_location("v43_total_dehom_source", TOTAL_COMPILER)
    if spec is None or spec.loader is None:
        fail("total compiler import")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def require_aws(mode: str, phase: str) -> str:
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if (platform.system() != "Linux" or not vendor.is_file()
            or vendor.read_text().strip() != "Amazon EC2"
            or not tag.startswith("max12_812_order2_p0_total_rees_j2_a1_total_dvr_w30_v43_")
            or f"_totaldehom_{mode}_{phase}_" not in tag):
        fail("registered V43 total-dehom AWS lane required")
    return tag


def modular_value(value: Fraction, characteristic: int) -> str:
    if not characteristic:
        return (str(value.numerator) if value.denominator == 1
                else f"({value.numerator}/{value.denominator})")
    if value.denominator % characteristic == 0:
        fail(("bad denominator", characteristic, value))
    return str(value.numerator * pow(value.denominator, -1, characteristic) % characteristic)


def dehom_text(polynomial, characteristic: int) -> str:
    pieces = []
    for monomial, tpoly in sorted(polynomial.items()):
        exponents = dict(monomial)
        exponents.pop("a1", None)
        factors = []
        for name, exponent in sorted(exponents.items()):
            factors.append(name if exponent == 1 else f"{name}^{exponent}")
        for degree, coefficient in sorted(tpoly.items()):
            term = [modular_value(coefficient, characteristic), *factors]
            if degree:
                term.append("t" if degree == 1 else f"t^{degree}")
            pieces.append("*".join(term))
    return ("+".join(pieces) if pieces else "0").replace("+-", "-")


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("output", type=Path)
    cli.add_argument("--mode", choices=("exact", "modp"), required=True)
    cli.add_argument("--prime", type=int, choices=(65519, 65521), required=True)
    cli.add_argument("--phase", choices=("eliminate", "lift"), required=True)
    args = cli.parse_args()
    if (args.mode, args.prime) not in (("exact", 65521), ("modp", 65519)):
        fail("mode/prime custody")
    tag = require_aws(args.mode, args.phase)
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    source = load_total_compiler()
    (parser, _, total_rows, frozen_hashes, total_hashes, variables,
     frozen_variables, general_only, nonzero_general) = source.reconstruct_rows()
    by_name = {item["name"]: item for item in total_rows}
    if (len(frozen_hashes) != 70 or nonzero_general != 59
            or len(variables) != 66 or len(frozen_variables) != 65
            or general_only != ["ez9"] or any(name not in by_name for name in SELECTED)):
        fail("literal-total source census")
    selected = [by_name[name] for name in SELECTED]
    active = sorted({name for item in selected for monomial in item["polynomial"]
                     for name, _ in monomial if name != "a1"})
    characteristic = 0 if args.mode == "exact" else args.prime
    script_path = output / f"total_dehom_{args.mode}_{args.phase}.sing"
    unit_path = output / "eliminant_unit.poly"
    eliminant_path = output / "eliminant_ideal.txt"
    multiplier_paths = [output / f"total_multiplier_{index:02d}_{item['name']}.poly"
                        for index, item in enumerate(selected, start=1)]
    blocks = f"(dp({len(active)}),dp(1))" if active else "dp"
    lines = [
        f"ring R={characteristic},({','.join([*active, 't'])}),{blocks};",
        "option(redSB);",
        "ideal I=",
    ]
    for index, item in enumerate(selected):
        lines.append(dehom_text(item["polynomial"], characteristic)
                     + ("," if index + 1 < len(selected) else ";"))
    product = "*".join(active) if active else "1"
    lines += [
        "ideal I0=subst(I,t,0); ideal G0=std(I0); poly specialnf=reduce(1,G0);",
        "if (specialnf!=0) { print(\"FAIL_V43_TOTAL_DEHOM_SPECIAL_CONTROL\"); quit; }",
        "print(\"V43_TOTAL_DEHOM_SPECIAL_UNIT=1\");",
        f"ideal E=eliminate(I,{product});",
        f"write(\"{eliminant_path}\",E);",
        "print(\"V43_TOTAL_DEHOM_ELIMINANT_SIZE=\"+string(size(E)));",
        "int ci; poly candidate; poly unitfactor=0;",
        "for (ci=1;ci<=size(E);ci++)",
        "{",
        "  candidate=E[ci];",
        "  if ((unitfactor==0)&&(candidate!=0)&&(subst(candidate,t,0)!=0))",
        "  { unitfactor=candidate/subst(candidate,t,0); }",
        "}",
        "if (unitfactor==0)",
        "{ print(\"V43_TOTAL_DEHOM_OUTCOME=no-unit-eliminant\"); quit; }",
        "if (subst(unitfactor,t,0)!=1) { print(\"FAIL_V43_TOTAL_DEHOM_UNIT_NORMALIZATION\"); quit; }",
        f"write(\"{unit_path}\",unitfactor);",
        "print(\"V43_TOTAL_DEHOM_OUTCOME=unit-eliminant\");",
        "print(\"V43_TOTAL_DEHOM_UNIT_CONSTANT=1\");",
    ]
    if args.phase == "lift":
        lines += [
            "matrix L=lift(I,ideal(unitfactor));",
            "matrix REPLAY=matrix(I)*L;",
            "if ((nrows(REPLAY)!=1)||(ncols(REPLAY)!=1)||(REPLAY[1,1]!=unitfactor))",
            "{ print(\"FAIL_V43_TOTAL_DEHOM_LIFT_REPLAY\"); quit; }",
        ]
        for index, path in enumerate(multiplier_paths, start=1):
            lines.append(f"write(\"{path}\",L[{index},1]);")
        lines.append("print(\"V43_TOTAL_DEHOM_LIFT_REPLAY=1\");")
    lines += [
        "print(\"PASS_A1_TOTAL_DVR_W30_V43_TOTAL_DEHOM\");",
        "quit;",
    ]
    script_path.write_text("\n".join(lines) + "\n")
    result = {
        "status": "PASS-A1-TOTAL-DVR-W30-V43-TOTAL-DEHOM-COMPILER",
        "registered_aws_lane": tag,
        "mode": args.mode,
        "prime": args.prime,
        "phase": args.phase,
        "scope": "literal regenerated total-t rows; selected seventeen full cascade polynomials; a1=1 elimination of all positive-weight variables",
        "total_compiler_sha256": TOTAL_COMPILER_SHA256,
        "named_row_count": len(frozen_hashes),
        "general_nonzero_rows": nonzero_general,
        "total_positive_variables": len(variables),
        "rho0_positive_variables": len(frozen_variables),
        "general_only_variables": general_only,
        "selected_rows": list(SELECTED),
        "selected_total_t_sha256": {name: total_hashes[name] for name in SELECTED},
        "selected_term_counts": {item["name"]: len(item["polynomial"]) for item in selected},
        "active_variables_after_dehom": active,
        "active_variable_count_after_dehom": len(active),
        "singular_script": str(script_path),
        "singular_script_sha256": digest(script_path),
        "unit_path": str(unit_path),
        "eliminant_path": str(eliminant_path),
        "multiplier_paths": [str(path) for path in multiplier_paths] if args.phase == "lift" else [],
    }
    result_path = output / "compiler_result.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("PASS-A1-TOTAL-DVR-W30-V43-TOTAL-DEHOM-COMPILER")
    print(f"RESULT_SHA256={digest(result_path)}")


if __name__ == "__main__":
    main()
