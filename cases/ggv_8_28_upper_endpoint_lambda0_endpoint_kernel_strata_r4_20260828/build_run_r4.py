#!/usr/bin/env python3
"""Materialize r4 custody runner by counted edits to frozen r3 runner."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


R3_RUN_SHA256 = "73657e5498878c2fb041b8a4e4905c57f9c6c467170c4196b2d8ad19780ad710"
EXPECTED_R4_RUN_SHA256 = "93321dab1959045590ac3a20b1f11fde429b10f99230931e42f80109b2d7b9b1"


def sha_text(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def replace_exact(text: str, old: str, new: str, count: int) -> str:
    if text.count(old) != count:
        raise SystemExit(f"R3_RUN_TRANSFORM_COUNT_DRIFT:{old}:{text.count(old)}")
    return text.replace(old, new)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--r3-run", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    source = args.r3_run.read_text()
    if sha_text(source) != R3_RUN_SHA256:
        raise SystemExit("R3_RUN_SOURCE_DRIFT")
    result = replace_exact(
        source,
        "ggv_8_28_upper_endpoint_lambda0_endpoint_kernel_strata_r3_20260828",
        "ggv_8_28_upper_endpoint_lambda0_endpoint_kernel_strata_r4_20260828",
        1,
    )
    result = replace_exact(result, "build_worker_r3.py", "build_worker_r4.py", 1)
    result = replace_exact(result, "aws_worker_r3.sh", "aws_worker_r4.sh", 1)
    result = replace_exact(result, "R3_WORKER_NARROW_TRANSFORM_PASS", "R4_WORKER_NARROW_TRANSFORM_PASS", 1)
    result = replace_exact(
        result,
        "8c5705b1124efead1649724d3db7eb03f33e8ff44311ce6114d6a3f8efaf90da",
        "4f5439503440bcf69ab00c22d3a75487f0999a4f3b7cb0e2b59e898971307473",
        1,
    )
    result = replace_exact(result, "GGV_ENDPOINT_STRATA_R3_", "GGV_ENDPOINT_STRATA_R4_", 1)
    actual = sha_text(result)
    if EXPECTED_R4_RUN_SHA256 != "TO_BE_FROZEN" and actual != EXPECTED_R4_RUN_SHA256:
        raise SystemExit(f"R4_RUN_HASH_DISAGREEMENT:{actual}")
    args.output.write_text(result)
    print(f"R3_RUN_SHA256={R3_RUN_SHA256}")
    print(f"R4_RUN_SHA256={actual}")
    print("R4_RUN_NARROW_TRANSFORM_PASS")


if __name__ == "__main__":
    main()
