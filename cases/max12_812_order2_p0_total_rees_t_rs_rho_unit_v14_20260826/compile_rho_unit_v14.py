#!/usr/bin/env python3
"""V14 packaging repair for the T-rs rho-unit certificate."""

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
V12_COMPILER = ROOT / "cases/max12_812_order2_p0_total_rees_t_rs_rho_unit_v12_20260826/compile_rho_unit_v12.py"
V12_COMPILER_SHA256 = "9805bce184294bfdd3c81797192d9257e17865e4741d0df56bbbd334d6fdb2fd"
V13_COMPILER = ROOT / "cases/max12_812_order2_p0_total_rees_t_rs_rho_unit_v13_20260826/compile_rho_unit_v13.py"
V13_COMPILER_SHA256 = "329bfb0fffcc3bf6587ac800afc577770100fb8e5cba5a2116503c24be396749"
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
        or not tag.startswith("max12_812_order2_p0_total_rees_t_rs_rho_unit_v14_")
    ):
        raise CompileFailure("V14 compiler requires a registered AWS EC2 lane")
    return tag


def load_v12():
    if digest(V12_COMPILER) != V12_COMPILER_SHA256:
        raise CompileFailure("V12 compiler hash mismatch")
    if digest(V13_COMPILER) != V13_COMPILER_SHA256:
        raise CompileFailure("V13 compiler custody hash mismatch")
    spec = importlib.util.spec_from_file_location("rho_unit_v12_frozen", V12_COMPILER)
    if spec is None or spec.loader is None:
        raise CompileFailure("cannot import V12")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def compile_job(output: Path, characteristic: int, algorithm: str, tag: str) -> dict[str, object]:
    v12 = load_v12()
    base = v12.compile_job(output, characteristic, algorithm, tag)
    script = Path(base["script"])
    prepatch_sha256 = digest(script)
    text = script.read_text().replace("V12", "V14")
    repairs = (
        ("poly P3=E_Tg10_3/(rs^2);", "poly P3=E_Tg10_3/rs;", 1),
        ("int mb3=(rs^2*P3-E_Tg10_3==0);", "int mb3=(rs*P3-E_Tg10_3==0);", 1),
        ("8192*rs*qcs*P3", "8192*qcs*P3", 3),
    )
    counts: dict[str, int] = {}
    for old, new, expected in repairs:
        count = text.count(old)
        counts[old] = count
        if count != expected:
            raise CompileFailure(("repair census", old, count, expected))
        text = text.replace(old, new)
    script.write_text(text)
    if (
        "qring " in text
        or "E_Tg10_3/(rs^2)" in text
        or "8192*rs*qcs*P3" in text
        or text.count("PASS_T_RS_RHO_UNIT_V14") != 1
    ):
        raise CompileFailure("V14 script sentinel")
    result = {
        **base,
        "status": "PASS-T-RS-RHO-UNIT-V14-COMPILER",
        "registered_aws_lane": tag,
        "v12_compiler_sha256": V12_COMPILER_SHA256,
        "v13_compiler_sha256": V13_COMPILER_SHA256,
        "v12_prepatch_script_sha256": prepatch_sha256,
        "v14_preregistration_sha256": digest(PREREG),
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
