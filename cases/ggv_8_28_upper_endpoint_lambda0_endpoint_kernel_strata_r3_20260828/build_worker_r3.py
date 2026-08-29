#!/usr/bin/env python3
"""Materialize the narrow r3 worker from the immutable r2 worker."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


R2_WORKER_SHA256 = "8417b551c251262618fe388b8d92819d5fbb56e548287aee026104564255e718"
EXPECTED_R3_WORKER_SHA256 = "8c5705b1124efead1649724d3db7eb03f33e8ff44311ce6114d6a3f8efaf90da"
R2_NAME = "ggv_8_28_upper_endpoint_lambda0_endpoint_kernel_strata_r2_20260828"
R3_NAME = "ggv_8_28_upper_endpoint_lambda0_endpoint_kernel_strata_r3_20260828"


def sha_text(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--r2-worker", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    source = args.r2_worker.read_text()
    if sha_text(source) != R2_WORKER_SHA256:
        raise SystemExit("R2_WORKER_SOURCE_DRIFT")
    old_case = f'case_dir="$source_root/{R2_NAME}"'
    new_case = (
        f'compiler_case="$source_root/{R2_NAME}"\n'
        f'case_dir="$source_root/{R3_NAME}"'
    )
    if source.count(old_case) != 1:
        raise SystemExit("R2_WORKER_CASE_LINE_DRIFT")
    result = source.replace(old_case, new_case)
    old_compiler = '$case_dir/build_strata_scripts.py'
    if result.count(old_compiler) != 2:
        raise SystemExit("R2_WORKER_COMPILER_CALL_COUNT_DRIFT")
    result = result.replace(old_compiler, '$compiler_case/build_strata_scripts.py')
    old_selfcheck = '$case_dir/selfcheck_strata.py'
    if result.count(old_selfcheck) != 1:
        raise SystemExit("R2_WORKER_SELFCHECK_CALL_COUNT_DRIFT")
    result = result.replace(old_selfcheck, '$case_dir/selfcheck_strata_r3.py')
    actual = sha_text(result)
    if EXPECTED_R3_WORKER_SHA256 != "TO_BE_FROZEN" and actual != EXPECTED_R3_WORKER_SHA256:
        raise SystemExit(f"R3_WORKER_HASH_DISAGREEMENT:{actual}")
    args.output.write_text(result)
    print(f"R2_WORKER_SHA256={R2_WORKER_SHA256}")
    print(f"R3_WORKER_SHA256={actual}")
    print("R3_WORKER_NARROW_TRANSFORM_PASS")


if __name__ == "__main__":
    main()
