#!/usr/bin/env python3
"""One-line Singular-signature repair for the frozen V14 certificate."""

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
V14_COMPILER = ROOT / "cases/max12_812_order2_p0_total_rees_t_rs_rho_unit_v14_20260826/compile_rho_unit_v14.py"
V14_COMPILER_SHA256 = "809a1d660ee911eaad9c7e73f4f4202755776d79ece3f3d80a1e51630732460c"
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
        or not tag.startswith("max12_812_order2_p0_total_rees_t_rs_rho_unit_v16_")
    ):
        raise CompileFailure("V16 compiler requires a registered AWS EC2 lane")
    return tag


def load_v14():
    if digest(V14_COMPILER) != V14_COMPILER_SHA256:
        raise CompileFailure("V14 compiler hash mismatch")
    spec = importlib.util.spec_from_file_location("rho_unit_v14_frozen", V14_COMPILER)
    if spec is None or spec.loader is None:
        raise CompileFailure("cannot import V14")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def compile_job(output: Path, characteristic: int, algorithm: str, tag: str) -> dict[str, object]:
    v14 = load_v14()
    base = v14.compile_job(output, characteristic, algorithm, tag)
    script = Path(base["script"])
    prepatch_sha256 = digest(script)
    text = script.read_text()
    old = "ideal SpecialDk=std(J,rho,1-v*k);"
    new = "ideal SpecialDk=std(std(J,rho),1-v*k);"
    if text.count(old) != 1 or text.count(new) != 0:
        raise CompileFailure(("SpecialDk repair census", text.count(old), text.count(new)))
    text = text.replace(old, new).replace("V14", "V16")
    script.write_text(text)
    if (
        old in text
        or text.count(new) != 1
        or text.count("PASS_T_RS_RHO_UNIT_V16") != 1
        or "qring " in text
    ):
        raise CompileFailure("V16 script sentinel")
    result = {
        **base,
        "status": "PASS-T-RS-RHO-UNIT-V16-COMPILER",
        "registered_aws_lane": tag,
        "v14_compiler_sha256": V14_COMPILER_SHA256,
        "v14_prepatch_script_sha256": prepatch_sha256,
        "v16_preregistration_sha256": digest(PREREG),
        "special_dk_repair_count": 1,
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

