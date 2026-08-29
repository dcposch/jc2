#!/usr/bin/env python3
"""Compile AWS-only exact T-rs chart saturation/base-change discovery jobs."""

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
V9 = ROOT / "cases/max12_812_order2_p0_total_rees_t_rs0_coeffexport_v9_20260826"
INPUTS = {
    0: (
        V9 / "aws_q_v9",
        "86c535a370adc2c7fb31b6ec8454128d765f581200a1730c506306d8bfa63c0e",
    ),
    65521: (
        V9 / "aws_p65521_v9",
        "dc7757090bac53482ff674794e4e45cf33ff052d10c34f4e29a1de4133befde4",
    ),
}
PREREG = HERE / "PREREGISTRATION.md"
GRADES = (10, 11, 12)
ALGORITHMS = ("sat", "elim")
SOURCE_NAMES = (
    "rho", "ell1", "ell2", "cs1", "cs2", "rs", "rs1", "rs2",
    "a1", "aa1", "aaa1", "a0", "aa0", "aaa0", "e1", "ee1",
    "e0", "ee0", "k", "k1", "k2c", "qcs", "qc0", "qc1",
)


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
        or not tag.startswith(
            "max12_812_order2_p0_total_rees_t_rs_chart_discovery_v10_"
        )
    ):
        raise CompileFailure("V10 compiler requires a registered AWS EC2 lane")
    return tag


def load_input(characteristic: int) -> tuple[dict[str, object], dict[str, str]]:
    directory, expected_manifest = INPUTS[characteristic]
    manifest_path = directory / "COEFFICIENTS.json"
    actual_manifest = digest(manifest_path)
    if actual_manifest != expected_manifest:
        raise CompileFailure(
            ("input manifest hash", characteristic, actual_manifest, expected_manifest)
        )
    manifest = json.loads(manifest_path.read_text())
    if (
        manifest.get("characteristic") != characteristic
        or manifest.get("status") != "PASS-T-RS0-EXACT-COEFFICIENT-EXPORT-V9"
        or manifest.get("coefficient_file_count") != 42
    ):
        raise CompileFailure(("input manifest fields", characteristic))
    hashes = manifest.get("coefficient_sha256")
    if not isinstance(hashes, dict) or len(hashes) != 42:
        raise CompileFailure(("input coefficient hash census", characteristic))
    expressions: dict[str, str] = {}
    for prefix in ("T", "F"):
        for grade in GRADES:
            for row in range(1, 8):
                key = f"{prefix}g{grade}_{row}"
                path = directory / "compiled" / f"{key}.poly"
                if digest(path) != hashes.get(key):
                    raise CompileFailure(("coefficient hash", characteristic, key))
                expression = path.read_text().strip()
                if not expression or ";" in expression or "qring" in expression:
                    raise CompileFailure(("unsafe coefficient serialization", key))
                expressions[key] = expression
    if len(expressions) != 42:
        raise CompileFailure(("coefficient expression census", len(expressions)))
    return manifest, expressions


def chart_expression(expression: str) -> str:
    replacements = {"cs": "(rs*qcs)", "c0": "(rs*qc0)", "c1": "(rs*qc1)"}
    out = expression
    for name, image in replacements.items():
        out = re.sub(rf"\b{name}\b", image, out)
    forbidden = re.findall(r"\b(?:cs|c0|c1)\b", out)
    if forbidden:
        raise CompileFailure(("chart substitution residue", forbidden, expression))
    return out


def ideal_names(prefix: str, grade: int, suffix: str) -> str:
    return ",".join(
        f"{prefix}{g}_{row}_{suffix}"
        for g in GRADES
        if g <= grade
        for row in range(1, 8)
    )


def compile_job(
    output: Path,
    characteristic: int,
    grade: int,
    algorithm: str,
    tag: str,
) -> dict[str, object]:
    _, exact = load_input(0)
    _, selected = load_input(characteristic)
    output = output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    basis_paths = {
        name: output / f"{name}.ideal"
        for name in (
            "jtot",
            "jzero",
            "kafter",
            "kbefore",
            "after_minus_before",
            "before_minus_after",
            "naive_after_minus_before",
            "before_minus_naive_after",
        )
    }
    variables = ",".join(SOURCE_NAMES)
    if algorithm == "elim":
        ring = (
            f"ring R={characteristic},(u,{variables}),"
            f"(dp(1),dp({len(SOURCE_NAMES)}));"
        )
    else:
        ring = f"ring R={characteristic},({variables}),dp;"
    lines = [
        'LIB "elim.lib";',
        ring,
        "option(redSB);",
        'print("V10_QRING_DISABLED=1");',
        f'print("V10_CHARACTERISTIC={characteristic}");',
        f'print("V10_PREFIX_GRADE={grade}");',
        f'print("V10_ALGORITHM={algorithm}");',
        "proc IsContained(ideal A, ideal GB)",
        "{",
        "  int i;",
        "  for (i=1;i<=size(A);i++)",
        "  {",
        "    if (reduce(A[i],GB)!=0) { return(0); }",
        "  }",
        "  return(1);",
        "}",
        "ideal ToyVertical=rs;",
        "list ToyVerticalSat=sat(ToyVertical,ideal(rs));",
        "ideal GToyVertical=std(ToyVerticalSat[1]);",
        'if (reduce(1,GToyVertical)!=0) { print("FAIL_VERTICAL_SAT_CONTROL"); quit; }',
        "ideal ToyFactor=rs*(qc0+qcs);",
        "list ToyFactorSat=sat(ToyFactor,ideal(rs));",
        "ideal GToyFactor=std(ToyFactorSat[1]);",
        'if (reduce(qc0+qcs,GToyFactor)!=0 || reduce(1,GToyFactor)==0) { print("FAIL_FACTOR_SAT_CONTROL"); quit; }',
        'print("V10_SYNTHETIC_SAT_CONTROLS=PASS");',
    ]
    comparison_count = 0
    source_count = 0
    for prefix in ("T", "F"):
        for current_grade in GRADES:
            if current_grade > grade:
                continue
            for row in range(1, 8):
                key = f"{prefix}g{current_grade}_{row}"
                raw = f"{prefix}{current_grade}_{row}_raw"
                lines.append(f"poly {raw}={chart_expression(exact[key])};")
                if characteristic:
                    independent = f"{prefix}{current_grade}_{row}_independent"
                    lines.append(
                        f"poly {independent}={chart_expression(selected[key])};"
                    )
                    lines.append(
                        f'if ({raw}-{independent}!=0) '
                        f'{{ print("FAIL_MODULAR_INPUT_COMPARISON_{key}"); quit; }}'
                    )
                    comparison_count += 1
                stripped = f"{prefix}{current_grade}_{row}_strip"
                valuation = f"v_{prefix}{current_grade}_{row}"
                lines += [
                    f"poly {stripped}={raw};",
                    f"int {valuation}=0;",
                    f"while ({stripped}!=0 && subst({stripped},rs,0)==0)",
                    "{",
                    f"  {stripped}={stripped}/rs;",
                    f"  {valuation}={valuation}+1;",
                    "}",
                    f'print("V10_RS_VAL_{prefix}{current_grade}_{row}="'
                    f"+string({valuation}));",
                ]
                source_count += 1
    for current_grade in GRADES:
        if current_grade > grade:
            continue
        for row in range(1, 8):
            lines += [
                f"if (subst(T{current_grade}_{row}_raw,rho,0)-"
                f"F{current_grade}_{row}_raw!=0) "
                f'{{ print("FAIL_SOURCE_SPECIALIZATION_{current_grade}_{row}"); quit; }}',
                f"if (subst(T{current_grade}_{row}_raw,rho,-rho)-"
                f"T{current_grade}_{row}_raw!=0) "
                f'{{ print("FAIL_DECK_{current_grade}_{row}"); quit; }}',
            ]
    prefix_count = 7 * (grade - 9)
    lines += [
        f'print("V10_SOURCE_SPECIALIZATION_COUNT={prefix_count}");',
        f'print("V10_DECK_COUNT={prefix_count}");',
        f'print("V10_MODULAR_COMPARISON_COUNT={comparison_count}");',
        f"ideal EtotRaw={ideal_names('T', grade, 'raw')};",
        f"ideal EzeroRaw={ideal_names('F', grade, 'raw')};",
        f"ideal Etot={ideal_names('T', grade, 'strip')};",
        f"ideal Ezero={ideal_names('F', grade, 'strip')};",
        'print("V10_START_SATURATION");',
    ]
    if algorithm == "sat":
        lines += [
            "list STot=sat(std(Etot),ideal(rs));",
            "ideal Jtot=std(STot[1]);",
            "list SZero=sat(std(Ezero),ideal(rs));",
            "ideal Jzero=std(SZero[1]);",
            'print("V10_SAT_TOTAL_EXPONENT="+string(STot[2]));',
            'print("V10_SAT_ZERO_EXPONENT="+string(SZero[2]));',
        ]
    else:
        lines += [
            "ideal Ltot=Etot,1-u*rs;",
            "ideal GLtot=std(Ltot);",
            "ideal Jtot=std(eliminate(GLtot,u));",
            "ideal Lzero=Ezero,1-u*rs;",
            "ideal GLzero=std(Lzero);",
            "ideal Jzero=std(eliminate(GLzero,u));",
            'print("V10_ELIMINATION_INVERSE=1-u*rs");',
        ]
    lines += [
        'if (!IsContained(Etot,Jtot) || !IsContained(Ezero,Jzero)) { print("FAIL_SOURCE_NOT_IN_SATURATION"); quit; }',
        "ideal Kafter=Jtot,rho; Kafter=std(Kafter);",
        "ideal Kbefore=Jzero,rho; Kbefore=std(Kbefore);",
        "ideal AfterMinusBefore=reduce(Kafter,Kbefore);",
        "ideal BeforeMinusAfter=reduce(Kbefore,Kafter);",
        "int afterInBefore=IsContained(Kafter,Kbefore);",
        "int beforeInAfter=IsContained(Kbefore,Kafter);",
        "int basechangeEqual=afterInBefore*beforeInAfter;",
        "ideal NaiveAfter=EtotRaw,rho; NaiveAfter=std(NaiveAfter);",
        "ideal NaiveAfterMinusBefore=reduce(NaiveAfter,Kbefore);",
        "ideal BeforeMinusNaiveAfter=reduce(Kbefore,NaiveAfter);",
        "int naiveAfterInBefore=IsContained(NaiveAfter,Kbefore);",
        "int beforeInNaiveAfter=IsContained(Kbefore,NaiveAfter);",
        "int naiveEqual=naiveAfterInBefore*beforeInNaiveAfter;",
        'print("V10_JTOT_GENERATORS="+string(size(Jtot)));',
        'print("V10_JZERO_GENERATORS="+string(size(Jzero)));',
        'print("V10_KAFTER_GENERATORS="+string(size(Kafter)));',
        'print("V10_KBEFORE_GENERATORS="+string(size(Kbefore)));',
        'print("V10_AFTER_IN_BEFORE="+string(afterInBefore));',
        'print("V10_BEFORE_IN_AFTER="+string(beforeInAfter));',
        'print("V10_BASECHANGE_EQUAL="+string(basechangeEqual));',
        'print("V10_NAIVE_AFTER_IN_BEFORE="+string(naiveAfterInBefore));',
        'print("V10_BEFORE_IN_NAIVE_AFTER="+string(beforeInNaiveAfter));',
        'print("V10_NAIVE_EQUAL="+string(naiveEqual));',
    ]
    singular_objects = {
        "jtot": "Jtot",
        "jzero": "Jzero",
        "kafter": "Kafter",
        "kbefore": "Kbefore",
        "after_minus_before": "AfterMinusBefore",
        "before_minus_after": "BeforeMinusAfter",
        "naive_after_minus_before": "NaiveAfterMinusBefore",
        "before_minus_naive_after": "BeforeMinusNaiveAfter",
    }
    for name, obj in singular_objects.items():
        lines.append(f'write("{basis_paths[name]}",{obj});')
    lines += [
        'print("V10_ARTIFACT_WRITES=8");',
        'print("V10_SCOPE=PREFIX_BASECHANGE_DISCOVERY_ONLY_NO_CHART_OR_ORDER2_VERDICT");',
        'print("PASS_T_RS_CHART_DISCOVERY_V10");',
        "quit;",
    ]
    label = "q" if characteristic == 0 else f"p{characteristic}"
    script = output / f"t_rs_chart_v10_g{grade}_{algorithm}_{label}.sing"
    script.write_text("\n".join(lines) + "\n")
    script_text = script.read_text()
    if "qring " in script_text or script_text.count(
        "PASS_T_RS_CHART_DISCOVERY_V10"
    ) != 1:
        raise CompileFailure("compiled-script sentinel failure")
    result = {
        "status": "PASS-T-RS-CHART-DISCOVERY-V10-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": characteristic,
        "prefix_grade": grade,
        "algorithm": algorithm,
        "source_polynomial_count": source_count,
        "modular_comparison_count": comparison_count,
        "exact_input_manifest_sha256": digest(INPUTS[0][0] / "COEFFICIENTS.json"),
        "selected_input_manifest_sha256": digest(
            INPUTS[characteristic][0] / "COEFFICIENTS.json"
        ),
        "preregistration_sha256": digest(PREREG),
        "script": str(script),
        "script_sha256": digest(script),
        "artifact_paths": {name: str(path) for name, path in basis_paths.items()},
    }
    (output / "result.json").write_text(
        json.dumps(result, sort_keys=True, indent=2) + "\n"
    )
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=tuple(INPUTS), required=True)
    parser.add_argument("--grade", type=int, choices=GRADES, required=True)
    parser.add_argument("--algorithm", choices=ALGORITHMS, required=True)
    args = parser.parse_args()
    print(
        json.dumps(
            compile_job(
                args.output,
                args.characteristic,
                args.grade,
                args.algorithm,
                require_aws(),
            ),
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
