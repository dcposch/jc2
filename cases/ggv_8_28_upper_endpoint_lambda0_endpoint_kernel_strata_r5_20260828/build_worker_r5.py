#!/usr/bin/env python3
"""Materialize r5 worker with the exact runtime compiler path."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


R2_WORKER_SHA256 = "8417b551c251262618fe388b8d92819d5fbb56e548287aee026104564255e718"
EXPECTED_R5_WORKER_SHA256 = "8acf14af1b27476ff8a9134f9ad9e40d3a1a260963cae24835fe33632ac35256"
R2_NAME = "ggv_8_28_upper_endpoint_lambda0_endpoint_kernel_strata_r2_20260828"
R5_NAME = "ggv_8_28_upper_endpoint_lambda0_endpoint_kernel_strata_r5_20260828"


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
    new_case = f'compiler_case="$job_dir/runtime/compiler_r5_case"\ncase_dir="$source_root/{R5_NAME}"'
    if source.count(old_case) != 1:
        raise SystemExit("R2_WORKER_CASE_LINE_DRIFT")
    result = source.replace(old_case, new_case)
    if result.count('$case_dir/build_strata_scripts.py') != 2:
        raise SystemExit("R2_WORKER_COMPILER_CALL_COUNT_DRIFT")
    result = result.replace('$case_dir/build_strata_scripts.py', '$compiler_case/build_strata_scripts.py')
    if result.count('$case_dir/selfcheck_strata.py') != 1:
        raise SystemExit("R2_WORKER_SELFCHECK_CALL_COUNT_DRIFT")
    result = result.replace('$case_dir/selfcheck_strata.py', '$case_dir/selfcheck_strata_r5.py')
    actual = sha_text(result)
    if EXPECTED_R5_WORKER_SHA256 != "TO_BE_FROZEN" and actual != EXPECTED_R5_WORKER_SHA256:
        raise SystemExit(f"R5_WORKER_HASH_DISAGREEMENT:{actual}")
    args.output.write_text(result)
    print(f"R2_WORKER_SHA256={R2_WORKER_SHA256}")
    print(f"R5_WORKER_SHA256={actual}")
    print("R5_WORKER_NARROW_TRANSFORM_PASS")


if __name__ == "__main__":
    main()
