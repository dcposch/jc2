#!/usr/bin/env python3
"""Source-frozen repair of the V12 T-rs rho-unit compiler."""

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
V12_COMPILER = (
    ROOT
    / "cases/max12_812_order2_p0_total_rees_t_rs_rho_unit_v12_20260826"
    / "compile_rho_unit_v12.py"
)
V12_COMPILER_SHA256 = "9805bce184294bfdd3c81797192d9257e17865e4741d0df56bbbd334d6fdb2fd"
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
        or not tag.startswith("max12_812_order2_p0_total_rees_t_rs_rho_unit_v13_")
    ):
        raise CompileFailure("V13 compiler requires a registered AWS EC2 lane")
    return tag


def load_v12():
    if digest(V12_COMPILER) != V12_COMPILER_SHA256:
        raise CompileFailure("V12 compiler hash mismatch")
    spec = importlib.util.spec_from_file_location("rho_unit_v12_frozen", V12_COMPILER)
    if spec is None or spec.loader is None:
        raise CompileFailure("cannot import frozen V12 compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def compile_job(output: Path, characteristic: int, algorithm: str, tag: str) -> dict[str, object]:
    v12 = load_v12()
    base = v12.compile_job(output, characteristic, algorithm, tag)
    script = Path(base["script"])
    prepatch_sha256 = digest(script)
    text = script.read_text().replace("V12", "V13")
    repairs = (
        ("poly P3=E_Tg10_3/(rs^2);", "poly P3=E_Tg10_3/rs;"),
        ("int mb3=(rs^2*P3-E_Tg10_3==0);", "int mb3=(rs*P3-E_Tg10_3==0);"),
        ("8192*rs*qcs*P3", "8192*qcs*P3"),
    )
    counts: dict[str, int] = {}
    for old, new in repairs:
        count = text.count(old)
        counts[old] = count
        if count < 1:
            raise CompileFailure(("repair target missing", old, count))
        text = text.replace(old, new)
    if counts["8192*rs*qcs*P3"] != 2:
        raise CompileFailure(("certificate multiplier census", counts))
    script.write_text(text)
    if (
        "qring " in text
        or "E_Tg10_3/(rs^2)" in text
        or "8192*rs*qcs*P3" in text
        or text.count("PASS_T_RS_RHO_UNIT_V13") != 1
    ):
        raise CompileFailure("V13 script sentinel")
    result = {
        **base,
        "status": "PASS-T-RS-RHO-UNIT-V13-COMPILER",
        "registered_aws_lane": tag,
        "v12_compiler_sha256": V12_COMPILER_SHA256,
        "v12_prepatch_script_sha256": prepatch_sha256,
        "v13_preregistration_sha256": digest(PREREG),
        "repair_target_counts": counts,
        "script_sha256": digest(script),
    }
    (output / "result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    parser.add_argument("--algorithm", choices=("sat", "elim"), required=True)
    args = parser.parse_args()
    print(json.dumps(compile_job(args.output, args.characteristic, args.algorithm, require_aws()), sort_keys=True))


if __name__ == "__main__":
    main()
