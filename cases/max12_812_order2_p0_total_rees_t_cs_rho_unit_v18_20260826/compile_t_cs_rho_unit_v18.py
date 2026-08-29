#!/usr/bin/env python3
"""Compile the exact ordered T-cs special-fiber unit test."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import platform
import re


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V9 = {
    0: (
        ROOT / "cases/max12_812_order2_p0_total_rees_t_rs0_coeffexport_v9_20260826/aws_q_v9",
        "86c535a370adc2c7fb31b6ec8454128d765f581200a1730c506306d8bfa63c0e",
    ),
    65521: (
        ROOT / "cases/max12_812_order2_p0_total_rees_t_rs0_coeffexport_v9_20260826/aws_p65521_v9",
        "dc7757090bac53482ff674794e4e45cf33ff052d10c34f4e29a1de4133befde4",
    ),
}
V17 = {
    0: (
        ROOT / "cases/max12_812_order2_p0_total_rees_t_cs_row5_g14_export_v17_20260826/aws_q",
        "25d40556618983a350eda99d4fb6aae8d1e5cd2cf328041963b46d61729af543",
        "91d96924696ab19a59cd8661fdd778559ce8dc9c1bc0fbc886dbdf4956e838f7",
    ),
    65521: (
        ROOT / "cases/max12_812_order2_p0_total_rees_t_cs_row5_g14_export_v17_20260826/aws_p65521",
        "5ec8fece264a6076c5536f3c2cbb7d9d8f485316036e7e10adf0a7209e2ce166",
        "760d4f3b155decdf0e847a587254ae701f2b5948d8dd6135c52f5f213c10835b",
    ),
}
PREREG = HERE / "PREREGISTRATION.md"
KEYS = tuple(f"Tg{grade}_{row}" for grade in (10, 11, 12) for row in range(1, 8))


class CompileFailure(RuntimeError):
    pass


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def require_aws() -> str:
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if (
        platform.system() != "Linux"
        or not vendor.is_file()
        or vendor.read_text().strip() != "Amazon EC2"
        or not tag.startswith("max12_812_order2_p0_total_rees_t_cs_rho_unit_v18_")
    ):
        raise CompileFailure("V18 compiler requires a registered AWS EC2 lane")
    return tag


def load_v9(characteristic: int) -> tuple[dict[str, str], str]:
    directory, expected_manifest = V9[characteristic]
    manifest_path = directory / "COEFFICIENTS.json"
    if digest(manifest_path) != expected_manifest:
        raise CompileFailure(("V9 manifest hash", characteristic))
    manifest = json.loads(manifest_path.read_text())
    hashes = manifest.get("coefficient_sha256")
    if (
        manifest.get("status") != "PASS-T-RS0-EXACT-COEFFICIENT-EXPORT-V9"
        or manifest.get("characteristic") != characteristic
        or not isinstance(hashes, dict)
    ):
        raise CompileFailure(("V9 manifest fields", characteristic))
    expressions: dict[str, str] = {}
    for key in KEYS:
        path = directory / "compiled" / f"{key}.poly"
        if digest(path) != hashes.get(key):
            raise CompileFailure(("V9 coefficient hash", characteristic, key))
        expression = path.read_text().strip()
        if not expression or ";" in expression or "qring" in expression:
            raise CompileFailure(("unsafe V9 expression", characteristic, key))
        expressions[key] = expression
    return expressions, expected_manifest


def load_v17(characteristic: int) -> tuple[str, str, str]:
    directory, expected_result, expected_coefficient = V17[characteristic]
    result_path = directory / "RESULT.json"
    if digest(result_path) != expected_result:
        raise CompileFailure(("V17 result hash", characteristic))
    result = json.loads(result_path.read_text())
    label = "q" if characteristic == 0 else f"p{characteristic}"
    coefficient = directory / "compiled" / f"Tg14_5_{label}.poly"
    if (
        result.get("status") != "PASS-T-CS-ROW5-G14-EXPORT-V17"
        or result.get("characteristic") != characteristic
        or result.get("coefficient_sha256") != expected_coefficient
        or digest(coefficient) != expected_coefficient
    ):
        raise CompileFailure(("V17 coefficient contract", characteristic))
    expression = coefficient.read_text().strip()
    if not expression or ";" in expression or "qring" in expression:
        raise CompileFailure(("unsafe V17 expression", characteristic))
    return expression, expected_result, expected_coefficient


def chart_expression(expression: str) -> str:
    replacements = {"rs": "(cs*qrs)", "c0": "(cs*qc0)", "c1": "(cs*qc1)"}
    answer = expression
    for name, image in replacements.items():
        answer = re.sub(rf"\b{name}\b", image, answer)
    if re.findall(r"\b(?:rs|c0|c1)\b", answer):
        raise CompileFailure("chart-substitution residue")
    return answer


def expression_names(expressions: list[str]) -> list[str]:
    names = set()
    for expression in expressions:
        names.update(re.findall(r"\b[A-Za-z_][A-Za-z0-9_]*\b", expression))
    names.update(("qrs", "qc0", "qc1", "rho", "cs", "k"))
    forbidden = {"ideal", "poly", "std", "ring"}
    if names & forbidden:
        raise CompileFailure(("unexpected identifier", sorted(names & forbidden)))
    return sorted(names)


def compile_job(output: Path, characteristic: int, tag: str) -> dict[str, object]:
    exact12, exact_manifest = load_v9(0)
    selected12, selected_manifest = load_v9(characteristic)
    exact14, exact_v17_result, exact_v17_coefficient = load_v17(0)
    selected14, selected_v17_result, selected_v17_coefficient = load_v17(characteristic)
    exact = {**exact12, "Tg14_5": exact14}
    selected = {**selected12, "Tg14_5": selected14}
    keys = KEYS + ("Tg14_5",)
    charted_exact = {key: chart_expression(exact[key]) for key in keys}
    charted_selected = {key: chart_expression(selected[key]) for key in keys}
    variables = expression_names(list(charted_exact.values()) + list(charted_selected.values()))
    output = output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    label = "q" if characteristic == 0 else f"p{characteristic}"
    script = output / f"t_cs_rho_unit_v18_{label}.sing"
    lines = [
        'LIB "elim.lib";',
        f"ring R={characteristic},(u,v,{','.join(variables)}),(dp(2),dp({len(variables)}));",
        "option(redSB);",
        'print("V18_QRING_DISABLED=1");',
        f'print("V18_CHARACTERISTIC={characteristic}");',
        'print("V18_CHART=V_QRS_INTERSECT_DPLUS_CS_INTERSECT_DK");',
    ]
    for index, key in enumerate(keys, start=1):
        lines.append(f"poly E{index}={charted_exact[key]};")
        if characteristic:
            lines += [
                f"poly I{index}={charted_selected[key]};",
                f'if (E{index}-I{index}!=0) {{ print("FAIL_MODULAR_INPUT_{key}"); quit; }}',
            ]
    lines += [
        f'print("V18_INPUT_COUNT={len(keys)}");',
        f"ideal E12={','.join(f'E{i}' for i in range(1, len(KEYS) + 1))};",
        f"ideal E=E12,E{len(keys)};",
        "ideal Localizers=ideal(qrs,rho,1-u*cs,1-v*k);",
        "ideal Special=std(E+Localizers);",
        "int specialUnit=(reduce(1,Special)==0);",
        'if (specialUnit!=1) { print("FAIL_SPECIAL_FIBRE_NOT_UNIT"); quit; }',
        'print("V18_SPECIAL_FIBRE_UNIT=1");',
        "ideal NoG14=std(E12+Localizers);",
        "int noG14Unit=(reduce(1,NoG14)==0);",
        'if (noG14Unit!=0) { print("FAIL_DROP_G14_CONTROL_UNIT"); quit; }',
        'print("V18_DROP_G14_NONUNIT=1");',
        f'write("{output / "special.ideal"}",Special);',
        f'write("{output / "drop_g14.ideal"}",NoG14);',
        f'write("{output / "charted_inputs.polys"}",E);',
        'print("V18_ARTIFACT_WRITES=3");',
        'print("V18_RHO_UNIT_LOGIC=EMPTY_SPECIAL_FIBRE_IN_ACTUAL_LOCALIZED_TOTAL_CHART");',
        'print("V18_SCOPE=T_CS_ORDERED_COMPLEMENT_DK_PREFIX_G10_G11_G12_G14_ONLY");',
        'print("PASS_T_CS_RHO_UNIT_V18");',
        "quit;",
    ]
    script.write_text("\n".join(lines) + "\n")
    text = script.read_text()
    if "qring " in text or text.count("PASS_T_CS_RHO_UNIT_V18") != 1:
        raise CompileFailure("V18 script sentinel")
    result = {
        "status": "PASS-T-CS-RHO-UNIT-V18-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": characteristic,
        "input_count": len(keys),
        "input_keys": list(keys),
        "exact_v9_manifest_sha256": exact_manifest,
        "selected_v9_manifest_sha256": selected_manifest,
        "exact_v17_result_sha256": exact_v17_result,
        "selected_v17_result_sha256": selected_v17_result,
        "exact_v17_coefficient_sha256": exact_v17_coefficient,
        "selected_v17_coefficient_sha256": selected_v17_coefficient,
        "preregistration_sha256": digest(PREREG),
        "ring_variable_count": len(variables) + 2,
        "script": str(script),
        "script_sha256": digest(script),
        "artifacts": [str(output / name) for name in ("special.ideal", "drop_g14.ideal", "charted_inputs.polys")],
    }
    (output / "result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    print(json.dumps(compile_job(args.output, args.characteristic, require_aws()), sort_keys=True))


if __name__ == "__main__":
    main()

