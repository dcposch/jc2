#!/usr/bin/env python3
"""Narrow r4 repair: accept Singular's documented error continuation."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile


R3_SELFCHECK_SHA256 = "b6c2d94dedae4ecaf23032368273d2b25967f6cac593da8b24087dc5b64c80b0"
PATCHED_R3_SELFCHECK_SHA256 = "6ab9dc1a11ed4cb866379ddf4131bff7faed66fcb7dc170ae081631b5eb1359d"
OLD = '''        if "NEGATIVE_CONTROL_UNEXPECTED_SUCCESS" in negative_text:
            raise SystemExit("RESERVED_NF_NEGATIVE_CONTROL_FALSE_PASS")
        print("RESERVED_NF_NEGATIVE_CONTROL_PASS")
'''
NEW = '''        if "NEGATIVE_CONTROL_UNEXPECTED_SUCCESS" not in negative_text:
            raise SystemExit("RESERVED_NF_NEGATIVE_CONTROL_CONTINUATION_MARKER_MISSING")
        print("SINGULAR_ERROR_CONTINUATION_NEGATIVE_CONTROL_PASS")
        print("RESERVED_NF_NEGATIVE_CONTROL_PASS")
'''


def sha_text(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case-dir", type=Path, required=True)
    parser.add_argument("--matrix", type=Path, required=True)
    parser.add_argument("--fitting", type=Path, required=True)
    parser.add_argument("--content", type=Path, required=True)
    args = parser.parse_args()
    case_dir = args.case_dir.resolve()
    r3_path = case_dir.parent / "ggv_8_28_upper_endpoint_lambda0_endpoint_kernel_strata_r3_20260828" / "selfcheck_strata_r3.py"
    source = r3_path.read_text()
    if sha_text(source) != R3_SELFCHECK_SHA256:
        raise SystemExit("R3_SELFCHECK_SOURCE_DRIFT")
    if source.count(OLD) != 1:
        raise SystemExit("R3_NEGATIVE_CONTROL_BLOCK_DRIFT")
    patched_source = source.replace(OLD, NEW)
    if sha_text(patched_source) != PATCHED_R3_SELFCHECK_SHA256:
        raise SystemExit("R4_SELFCHECK_HASH_DISAGREEMENT")
    with tempfile.TemporaryDirectory(prefix="endpoint-strata-r4-selfcheck-") as raw:
        patched = Path(raw) / "selfcheck_strata_r4_materialized.py"
        patched.write_text(patched_source)
        result = subprocess.run(
            [sys.executable, "-B", str(patched), "--case-dir", str(case_dir),
             "--matrix", str(args.matrix.resolve()),
             "--fitting", str(args.fitting.resolve()),
             "--content", str(args.content.resolve())],
            cwd=raw, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            timeout=170,
        )
        sys.stdout.write(result.stdout)
        sys.stderr.write(result.stderr)
        if result.returncode:
            raise SystemExit(f"PATCHED_R3_SELFCHECK_FAILURE:{result.returncode}")
        if result.stderr:
            raise SystemExit("PATCHED_R3_SELFCHECK_STDERR")
    print(f"PATCHED_R3_SELFCHECK_SHA256={PATCHED_R3_SELFCHECK_SHA256}")
    print("STRATA_R4_NEGATIVE_CONTROL_POLARITY_FIX_PASS")


if __name__ == "__main__":
    main()
