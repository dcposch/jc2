#!/usr/bin/env python3
"""AWS-only fail-closed wrapper repairing the frozen V10 chart compiler."""

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
V10_COMPILER = (
    ROOT
    / "cases/max12_812_order2_p0_total_rees_t_rs_chart_discovery_v10_20260826"
    / "compile_chart_discovery_v10.py"
)
V10_COMPILER_SHA256 = "6a054f7f567ca3f4ef7f360820b28b3a4fe50ae5aaa5c76bae5cd9422fc503f3"
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
            "max12_812_order2_p0_total_rees_t_rs_chart_discovery_v11_"
        )
    ):
        raise CompileFailure("V11 compiler requires a registered AWS EC2 lane")
    return tag


def load_v10():
    actual = digest(V10_COMPILER)
    if actual != V10_COMPILER_SHA256:
        raise CompileFailure(("V10 compiler hash", actual, V10_COMPILER_SHA256))
    spec = importlib.util.spec_from_file_location("t_rs_chart_v10_frozen", V10_COMPILER)
    if spec is None or spec.loader is None:
        raise CompileFailure("cannot load frozen V10 compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def compile_job(
    output: Path,
    characteristic: int,
    grade: int,
    algorithm: str,
    tag: str,
) -> dict[str, object]:
    v10 = load_v10()
    base = v10.compile_job(output, characteristic, grade, algorithm, tag)
    script = Path(base["script"])
    prepatch_sha256 = digest(script)
    text = script.read_text().replace("V10", "V11")
    old_total = 'print("V11_SAT_TOTAL_EXPONENT="+string(STot[2]));'
    old_zero = 'print("V11_SAT_ZERO_EXPONENT="+string(SZero[2]));'
    if algorithm == "sat":
        if text.count(old_total) != 1 or text.count(old_zero) != 1:
            raise CompileFailure("V10 saturation repair target census")
        text = text.replace(
            old_total,
            'print("V11_SAT_TOTAL_RETURN_LENGTH="+string(size(STot)));',
        ).replace(
            old_zero,
            'print("V11_SAT_ZERO_RETURN_LENGTH="+string(size(SZero)));',
        )
    elif old_total in text or old_zero in text:
        raise CompileFailure("unexpected saturation return access in elimination lane")
    script.write_text(text)
    if (
        "qring " in text
        or "STot[2]" in text
        or "SZero[2]" in text
        or text.count("PASS_T_RS_CHART_DISCOVERY_V11") != 1
    ):
        raise CompileFailure("V11 generated-script sentinel failure")
    result = {
        **base,
        "status": "PASS-T-RS-CHART-DISCOVERY-V11-COMPILER",
        "registered_aws_lane": tag,
        "v10_compiler_sha256": V10_COMPILER_SHA256,
        "v10_prepatch_script_sha256": prepatch_sha256,
        "v11_preregistration_sha256": digest(PREREG),
        "script_sha256": digest(script),
        "software_repairs": [
            "SINGULAR_SAT_ONE_ENTRY_RETURN_LIST",
            "GNU_TIME_RESOURCE_STDERR_VALIDATION",
        ],
    }
    (output / "result.json").write_text(
        json.dumps(result, sort_keys=True, indent=2) + "\n"
    )
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    parser.add_argument("--grade", type=int, choices=(10, 11, 12), required=True)
    parser.add_argument("--algorithm", choices=("sat", "elim"), required=True)
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
