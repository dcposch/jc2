#!/usr/bin/env python3
"""Compile the AWS-only exact T-rs rho-unit certificate."""

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
KEYS = ("Tg10_1", "Tg10_2", "Tg10_3", "Tg12_6")
ALGORITHMS = ("sat", "elim")
PREREG = HERE / "PREREGISTRATION.md"


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
            "max12_812_order2_p0_total_rees_t_rs_rho_unit_v12_"
        )
    ):
        raise CompileFailure("V12 compiler requires a registered AWS EC2 lane")
    return tag


def load_input(characteristic: int) -> tuple[dict[str, object], dict[str, str]]:
    directory, expected_manifest = INPUTS[characteristic]
    manifest_path = directory / "COEFFICIENTS.json"
    if digest(manifest_path) != expected_manifest:
        raise CompileFailure(("manifest hash", characteristic, digest(manifest_path)))
    manifest = json.loads(manifest_path.read_text())
    hashes = manifest.get("coefficient_sha256")
    if (
        manifest.get("characteristic") != characteristic
        or manifest.get("status") != "PASS-T-RS0-EXACT-COEFFICIENT-EXPORT-V9"
        or not isinstance(hashes, dict)
    ):
        raise CompileFailure(("manifest fields", characteristic))
    expressions: dict[str, str] = {}
    for key in KEYS:
        path = directory / "compiled" / f"{key}.poly"
        if digest(path) != hashes.get(key):
            raise CompileFailure(("coefficient hash", characteristic, key))
        expression = path.read_text().strip()
        if not expression or ";" in expression or "qring" in expression:
            raise CompileFailure(("unsafe expression", characteristic, key))
        expressions[key] = expression
    return manifest, expressions


def chart_expression(expression: str) -> str:
    replacements = {"cs": "(rs*qcs)", "c0": "(rs*qc0)", "c1": "(rs*qc1)"}
    out = expression
    for name, image in replacements.items():
        out = re.sub(rf"\b{name}\b", image, out)
    if re.findall(r"\b(?:cs|c0|c1)\b", out):
        raise CompileFailure(("chart substitution residue", expression))
    return out


def compile_job(
    output: Path, characteristic: int, algorithm: str, tag: str
) -> dict[str, object]:
    _, exact = load_input(0)
    _, selected = load_input(characteristic)
    output = output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    variables = "rho,rs,qcs,qc0,qc1,a0,a1,k"
    ring = f"ring R={characteristic},(u,v,{variables}),(dp(2),dp(8));"
    lines = [
        'LIB "elim.lib";',
        ring,
        "option(redSB);",
        'print("V12_QRING_DISABLED=1");',
        f'print("V12_CHARACTERISTIC={characteristic}");',
        f'print("V12_ALGORITHM={algorithm}");',
    ]
    for key in KEYS:
        lines.append(f"poly E_{key}={chart_expression(exact[key])};")
        if characteristic:
            lines.append(f"poly I_{key}={chart_expression(selected[key])};")
            lines.append(
                f'if (E_{key}-I_{key}!=0) '
                f'{{ print("FAIL_MODULAR_INPUT_{key}"); quit; }}'
            )
    lines += [
        "poly P1=E_Tg10_1/rs;",
        "poly P2=E_Tg10_2/rs;",
        "poly P3=E_Tg10_3/(rs^2);",
        "poly P126=E_Tg12_6/(rs^2);",
        "int mb1=(rs*P1-E_Tg10_1==0);",
        "int mb2=(rs*P2-E_Tg10_2==0);",
        "int mb3=(rs^2*P3-E_Tg10_3==0);",
        "int mb126=(rs^2*P126-E_Tg12_6==0);",
        'if (mb1*mb2*mb3*mb126!=1) { print("FAIL_MULTIPLICATION_BACK"); quit; }',
        'print("V12_MULTIPLICATION_BACK_COUNT=4");',
        "poly Delta=32768*E_Tg12_6-35*k*rs^4+4096*rs*E_Tg10_2+8192*rs*qcs*E_Tg10_3;",
        "poly B=5120*rho^2*rs^2*qcs^4*k+2640*rs^2*qcs^2*k-4608*qcs*(a0*qc1+a1*qc0);",
        "poly DeltaResidual=Delta-rho^2*rs^2*B;",
        'if (DeltaResidual!=0) { print("FAIL_FOUR_TERM_DELTA"); quit; }',
        'print("V12_FOUR_TERM_DELTA=1");',
        "poly V=8*rho^2*qcs^2+3;",
        "poly BResidual=B+12288*qcs*P1-1120*rs^2*qcs^2*k*V;",
        'if (BResidual!=0) { print("FAIL_B_DECOMPOSITION"); quit; }',
        'print("V12_B_DECOMPOSITION=1");',
        "poly U=1+32*rho^2*qcs^2*V;",
        "poly CertResidual=35*rs^2*k*U-(32768*P126+4096*P2+8192*rs*qcs*P3+12288*rho^2*qcs*P1);",
        'if (CertResidual!=0) { print("FAIL_CERTIFICATE_IDENTITY"); quit; }',
        'print("V12_CERTIFICATE_IDENTITY=1");',
        "poly NegativeDropP1=35*rs^2*k*U-(32768*P126+4096*P2+8192*rs*qcs*P3);",
        "poly UWrong=1+31*rho^2*qcs^2*V;",
        "poly NegativeWrongU=35*rs^2*k*UWrong-(32768*P126+4096*P2+8192*rs*qcs*P3+12288*rho^2*qcs*P1);",
        'if (NegativeDropP1==0 || NegativeWrongU==0) { print("FAIL_NEGATIVE_CONTROL"); quit; }',
        'print("V12_NEGATIVE_CONTROL_COUNT=2");',
        "ideal E=P1,P2,P3,P126;",
    ]
    if algorithm == "sat":
        lines += [
            "list Sat=sat(std(E),ideal(rs));",
            "ideal J=std(Sat[1]);",
            'print("V12_SAT_RETURN_LENGTH="+string(size(Sat)));',
        ]
    else:
        lines += [
            "ideal Lift=E,1-u*rs;",
            "ideal J=std(eliminate(std(Lift),u));",
            'print("V12_ELIMINATION_INVERSE=1-u*rs");',
        ]
    lines += [
        "int containsKU=(reduce(35*k*U,J)==0);",
        'if (containsKU!=1) { print("FAIL_SATURATED_KU_MEMBERSHIP"); quit; }',
        'print("V12_SATURATED_KU_MEMBERSHIP=1");',
        "ideal Special=std(J,rho);",
        "int specialK=(reduce(k,Special)==0);",
        'if (specialK!=1) { print("FAIL_SPECIAL_CONTAINS_K"); quit; }',
        'print("V12_SPECIAL_CONTAINS_K=1");',
        "ideal Dk=std(J,1-v*k);",
        "int dkU=(reduce(U,Dk)==0);",
        'if (dkU!=1) { print("FAIL_DK_CONTAINS_U"); quit; }',
        "poly RhoInverse=-32*rho*qcs^2*V;",
        "int rhoInverse=(reduce(rho*RhoInverse-1,Dk)==0);",
        'if (rhoInverse!=1) { print("FAIL_RHO_INVERSE"); quit; }',
        'print("V12_RHO_INVERSE=1");',
        "ideal SpecialDk=std(J,rho,1-v*k);",
        "int specialDkUnit=(reduce(1,SpecialDk)==0);",
        'if (specialDkUnit!=1) { print("FAIL_SPECIAL_DK_NOT_UNIT"); quit; }',
        'print("V12_SPECIAL_DK_UNIT=1");',
        f'write("{output / "jactual.ideal"}",J);',
        f'write("{output / "dk.ideal"}",Dk);',
        f'write("{output / "special_dk.ideal"}",SpecialDk);',
        f'write("{output / "certificate.polys"}",ideal(U,V,RhoInverse,CertResidual,BResidual,NegativeDropP1,NegativeWrongU));',
        'print("V12_ARTIFACT_WRITES=4");',
        'print("V12_SCOPE=T_RS_ACTUAL_CHART_DK_RHO_UNIT_PREFIX_ONLY");',
        'print("PASS_T_RS_RHO_UNIT_V12");',
        "quit;",
    ]
    label = "q" if characteristic == 0 else f"p{characteristic}"
    script = output / f"t_rs_rho_unit_v12_{algorithm}_{label}.sing"
    script.write_text("\n".join(lines) + "\n")
    text = script.read_text()
    if "qring " in text or text.count("PASS_T_RS_RHO_UNIT_V12") != 1:
        raise CompileFailure("compiled-script sentinel")
    result = {
        "status": "PASS-T-RS-RHO-UNIT-V12-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": characteristic,
        "algorithm": algorithm,
        "input_keys": list(KEYS),
        "exact_manifest_sha256": digest(INPUTS[0][0] / "COEFFICIENTS.json"),
        "selected_manifest_sha256": digest(
            INPUTS[characteristic][0] / "COEFFICIENTS.json"
        ),
        "preregistration_sha256": digest(PREREG),
        "script": str(script),
        "script_sha256": digest(script),
        "artifacts": [
            str(output / name)
            for name in ("jactual.ideal", "dk.ideal", "special_dk.ideal", "certificate.polys")
        ],
    }
    (output / "result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    parser.add_argument("--algorithm", choices=ALGORITHMS, required=True)
    args = parser.parse_args()
    tag = require_aws()
    print(json.dumps(compile_job(args.output, args.characteristic, args.algorithm, tag), sort_keys=True))


if __name__ == "__main__":
    main()
