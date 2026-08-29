#!/usr/bin/env python3
"""Apply the one-line literal-marker parser fix to frozen r3 worker."""

from __future__ import annotations
import argparse
import hashlib
from pathlib import Path

R3_WORKER_SHA256 = "20e03925d105bba482901643d609a13c6cf4cb74ff450783237e25fda0d859c1"
EXPECTED_R4_WORKER_SHA256 = "2e5f9c116ec77f298224273f95ca73e6623980d07563ea837461a2cfe64afa36"
R3_NAME = "ggv_8_28_upper_endpoint_lambda0_endpoint_kernel_strata_replay_fix_r3_20260828"
R4_NAME = "ggv_8_28_upper_endpoint_lambda0_endpoint_kernel_strata_replay_fix_r4_20260828"

def sha(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()

def main() -> None:
    parser = argparse.ArgumentParser(); parser.add_argument("--r3-worker", type=Path, required=True); parser.add_argument("--output", type=Path, required=True); args = parser.parse_args()
    source = args.r3_worker.read_text()
    if sha(source) != R3_WORKER_SHA256: raise SystemExit("R3_WORKER_SOURCE_DRIFT")
    if source.count(R3_NAME) != 1 or source.count('grep -q "^${marker}$" "$stdout"') != 1: raise SystemExit("R3_TRANSFORM_SITE_DRIFT")
    result = source.replace(R3_NAME, R4_NAME).replace('grep -q "^${marker}$" "$stdout"', 'grep -Fqx -- "$marker" "$stdout"')
    actual = sha(result)
    if EXPECTED_R4_WORKER_SHA256 != "TO_BE_FROZEN" and actual != EXPECTED_R4_WORKER_SHA256: raise SystemExit(f"R4_WORKER_HASH_DISAGREEMENT:{actual}")
    args.output.write_text(result)
    print(f"R4_WORKER_SHA256={actual}"); print("R4_LITERAL_MARKER_PARSER_FIX_PASS")

if __name__ == "__main__": main()
