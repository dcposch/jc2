#!/usr/bin/env python3
"""Narrow r3 repair: reject Singular's reserved NF name, then replay r2."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import re
import subprocess
import sys
import tempfile


R2_SELFCHECK_SHA256 = "4582e1784e3acc69878fdd3649d18f8ec7d64804b4968536ff7e2aedf19c1888"
PATCHED_SELFCHECK_SHA256 = "de8be7ab8b715a7487166283178142ca4e039a4f05c266703ba5823fb523b9cb"


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
    r2_case = case_dir.parent / "ggv_8_28_upper_endpoint_lambda0_endpoint_kernel_strata_r2_20260828"
    r2_selfcheck = r2_case / "selfcheck_strata.py"
    source = r2_selfcheck.read_text()
    if sha_text(source) != R2_SELFCHECK_SHA256:
        raise SystemExit("R2_SELFCHECK_SOURCE_DRIFT")
    if len(re.findall(r"\bNF\b", source)) != 6:
        raise SystemExit("R2_RESERVED_TOKEN_COUNT_DRIFT")

    with tempfile.TemporaryDirectory(prefix="endpoint-strata-r3-selfcheck-") as raw:
        temp = Path(raw)
        negative = temp / "reserved_nf_negative.sing"
        negative.write_text(
            "ring f=(0,a,b),(z),dp;\n"
            "matrix MF[2][3]=1,0,a/b,0,1,0;\n"
            "module KF=syz(module(MF));\n"
            "matrix NF=matrix(KF);\n"
            "print(\"NEGATIVE_CONTROL_UNEXPECTED_SUCCESS\");\n"
            "quit;\n"
        )
        mutation = subprocess.run(
            ["Singular", "-q", str(negative)], cwd=temp, text=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=20,
        )
        negative_text = mutation.stdout + mutation.stderr
        if "last reserved name was `NF`" not in negative_text:
            raise SystemExit("RESERVED_NF_NEGATIVE_CONTROL_NOT_DETECTED")
        if "NEGATIVE_CONTROL_UNEXPECTED_SUCCESS" in negative_text:
            raise SystemExit("RESERVED_NF_NEGATIVE_CONTROL_FALSE_PASS")
        print("RESERVED_NF_NEGATIVE_CONTROL_PASS")
        print(f"RESERVED_NF_NEGATIVE_STDOUT_SHA256={sha_text(negative_text)}")

        patched_source = re.sub(r"\bNF\b", "NFIELD", source)
        if sha_text(patched_source) != PATCHED_SELFCHECK_SHA256:
            raise SystemExit("PATCHED_SELFCHECK_HASH_DISAGREEMENT")
        patched = temp / "selfcheck_strata_r3_materialized.py"
        patched.write_text(patched_source)
        replay = subprocess.run(
            [sys.executable, "-B", str(patched), "--case-dir", str(r2_case),
             "--matrix", str(args.matrix.resolve()),
             "--fitting", str(args.fitting.resolve()),
             "--content", str(args.content.resolve())],
            cwd=temp, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            timeout=150,
        )
        if replay.returncode:
            sys.stdout.write(replay.stdout)
            sys.stderr.write(replay.stderr)
            raise SystemExit(f"PATCHED_R2_SELFCHECK_FAILURE:{replay.returncode}")
        sys.stdout.write(replay.stdout)
        if replay.stderr:
            sys.stderr.write(replay.stderr)
            raise SystemExit("PATCHED_R2_SELFCHECK_STDERR")
    print(f"PATCHED_SELFCHECK_SHA256={PATCHED_SELFCHECK_SHA256}")
    print("STRATA_R3_NARROW_ADAPTER_FIX_PASS")


if __name__ == "__main__":
    main()
