#!/usr/bin/env python3
"""Compile the exact ordered T-cs unit-ideal lift certificate."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V18 = ROOT / "cases/max12_812_order2_p0_total_rees_t_cs_rho_unit_v18_20260826"
BASE = V18 / "compile_t_cs_rho_unit_v18.py"
BASE_SHA256 = "50596db3a7009fa887e1679a8dbbc636afd68af66f923bfe13e7b5c3599548e6"
V18R1 = V18 / "compile_t_cs_rho_unit_v18r1.py"
V18R1_SHA256 = "c23c67a7f6f3e3071f384db229fe3ab4ba5578e0166dead85177a6923ef08ef6"
PREREG = HERE / "PREREGISTRATION.md"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def require_aws() -> str:
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if (
        platform.system() != "Linux"
        or not vendor.is_file()
        or vendor.read_text().strip() != "Amazon EC2"
        or not tag.startswith("max12_812_order2_p0_total_rees_t_cs_certificate_v19_")
    ):
        raise RuntimeError("V19 compiler requires a registered AWS EC2 lane")
    return tag


def load_base():
    if digest(BASE) != BASE_SHA256 or digest(V18R1) != V18R1_SHA256:
        raise RuntimeError("frozen V18/V18R1 compiler hash mismatch")
    spec = importlib.util.spec_from_file_location("jc2_t_cs_v18_base", BASE)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def compile_job(output: Path, characteristic: int, tag: str) -> dict[str, object]:
    base = load_base()
    result = base.compile_job(output, characteristic, tag)
    script = Path(result["script"])
    before = script.read_text()

    input_names = ",".join(f"E{i}" for i in range(1, 22))
    repairs = (
        (f"ideal E12={input_names};", f"ideal Prefix12={input_names};"),
        ("ideal E=E12,E22;", "ideal E=Prefix12,E22;"),
        ("ideal NoG14=std(E12+Localizers);", "ideal NoG14=std(Prefix12+Localizers);"),
    )
    repaired = before
    for old, new in repairs:
        if repaired.count(old) != 1 or new in repaired:
            raise RuntimeError(("V18R1 repair occurrence contract", old))
        repaired = repaired.replace(old, new)

    old_special = "ideal Special=std(E+Localizers);"
    new_special = "ideal RawSpecial=E+Localizers;\nideal Special=std(RawSpecial);"
    if repaired.count(old_special) != 1 or "ideal RawSpecial=" in repaired:
        raise RuntimeError("raw-special transform occurrence contract")
    repaired = repaired.replace(old_special, new_special)

    tail_marker = "ideal NoG14=std(Prefix12+Localizers);"
    if repaired.count(tail_marker) != 1:
        raise RuntimeError("negative-control tail occurrence contract")
    head, old_tail = repaired.split(tail_marker, 1)
    if (
        old_tail.count("PASS_T_CS_RHO_UNIT_V18") != 1
        or old_tail.count("V18_DROP_G14_NONUNIT=1") != 1
    ):
        raise RuntimeError("unexpected V18 tail")

    artifacts = {
        "certificate": output / "unit_certificate.matrix",
        "unit": output / "lift_unit.matrix",
        "raw": output / "raw_special.ideal",
    }
    lift_tail = [
        "ideal ONE=ideal(1);",
        "matrix LiftUnit;",
        "matrix LiftCertificate=lift(RawSpecial,ONE,LiftUnit);",
        "matrix LiftResidual=matrix(ONE)*LiftUnit-matrix(RawSpecial)*LiftCertificate;",
        'if (LiftResidual!=0) { print("FAIL_V19_LIFT_RESIDUAL"); quit; }',
        'print("V19_LIFT_RESIDUAL_ZERO=1");',
        "poly LiftScalar=LiftUnit[1,1];",
        'if (LiftScalar==0) { print("FAIL_V19_LIFT_SCALAR_ZERO"); quit; }',
        'if (deg(LiftScalar)!=0) { print("FAIL_V19_LIFT_SCALAR_NONCONSTANT"); quit; }',
        'print("V19_LIFT_SCALAR_NONZERO_CONSTANT=1");',
        f'write("{artifacts["certificate"]}",LiftCertificate);',
        f'write("{artifacts["unit"]}",LiftUnit);',
        f'write("{artifacts["raw"]}",RawSpecial);',
        'print("V19_ARTIFACT_WRITES=3");',
        'print("V19_RAW_GENERATOR_COUNT=26");',
        'print("V19_SCOPE=T_CS_ORDERED_COMPLEMENT_DK_PREFIX_G10_G11_G12_G14_ONLY");',
        'print("PASS_T_CS_EXPLICIT_UNIT_CERTIFICATE_V19");',
        "quit;",
    ]
    after = head + "\n".join(lift_tail) + "\n"
    if (
        after == before
        or "ideal E12=" in after
        or "NoG14" in after
        or "qring " in after
        or after.count("PASS_T_CS_EXPLICIT_UNIT_CERTIFICATE_V19") != 1
    ):
        raise RuntimeError("V19 script sentinel")
    script.write_text(after)

    result.update(
        {
            "status": "PASS-T-CS-EXPLICIT-UNIT-CERTIFICATE-V19-COMPILER",
            "characteristic": characteristic,
            "base_compiler_sha256": BASE_SHA256,
            "v18r1_compiler_sha256": V18R1_SHA256,
            "base_script_sha256": sha256(before.encode()).hexdigest(),
            "script_sha256": digest(script),
            "preregistration_sha256": digest(PREREG),
            "raw_generator_count": 26,
            "artifacts": [str(path) for path in artifacts.values()],
        }
    )
    (output / "result.json").write_text(
        json.dumps(result, sort_keys=True, indent=2) + "\n"
    )
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    print(json.dumps(compile_job(args.output, args.characteristic, require_aws()), sort_keys=True))


if __name__ == "__main__":
    main()
