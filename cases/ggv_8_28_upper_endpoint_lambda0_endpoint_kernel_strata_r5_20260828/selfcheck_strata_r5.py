#!/usr/bin/env python3
"""Full r5 check of reserved-name and post-qring symbol repairs."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import re
import subprocess
import sys
import tempfile


R2_SELFCHECK_SHA256 = "4582e1784e3acc69878fdd3649d18f8ec7d64804b4968536ff7e2aedf19c1888"
PATCHED_SELFCHECK_SHA256 = "10da4b9658d40a25679386f6600f9d113f417f38b6cf85ffa78cffd97a5b60b4"
R5_COMPILER_SHA256 = "575f0f34065bf06b76311a51fa71622d42d2e9a75fbb85979f79d9da97f3c06e"


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
    if len(re.findall(r"\bNF\b", source)) != 6 or source.count("string(F==0)") != 1:
        raise SystemExit("R2_SELFCHECK_MUTATION_SITE_DRIFT")

    with tempfile.TemporaryDirectory(prefix="endpoint-strata-r5-selfcheck-") as raw:
        temp = Path(raw)
        negative = temp / "reserved_nf_negative.sing"
        negative.write_text(
            "ring f=(0,a,b),(z),dp;\n"
            "matrix MF[2][3]=1,0,a/b,0,1,0; module KF=syz(module(MF));\n"
            "matrix NF=matrix(KF); print(\"NEGATIVE_CONTROL_CONTINUED\"); quit;\n"
        )
        mutation = subprocess.run(
            ["Singular", "-q", str(negative)], cwd=temp, text=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=20,
        )
        negative_text = mutation.stdout + mutation.stderr
        if "last reserved name was `NF`" not in negative_text:
            raise SystemExit("RESERVED_NF_NEGATIVE_CONTROL_NOT_DETECTED")
        if "NEGATIVE_CONTROL_CONTINUED" not in negative_text:
            raise SystemExit("SINGULAR_ERROR_CONTINUATION_NOT_DETECTED")
        print("RESERVED_NF_AND_CONTINUATION_NEGATIVE_CONTROL_PASS")
        print(f"RESERVED_NF_NEGATIVE_SHA256={sha_text(negative_text)}")

        shadow = temp / "shadow_case"
        shadow.mkdir()
        compiler = shadow / "build_strata_scripts.py"
        build = subprocess.run(
            [sys.executable, "-B", str(case_dir / "build_compiler_r5.py"),
             "--r2-compiler", str(r2_case / "build_strata_scripts.py"),
             "--output", str(compiler)],
            cwd=temp, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            timeout=30,
        )
        if build.returncode or build.stderr or sha_text(compiler.read_text()) != R5_COMPILER_SHA256:
            sys.stdout.write(build.stdout); sys.stderr.write(build.stderr)
            raise SystemExit("R5_COMPILER_MATERIALIZATION_FAILURE")
        sys.stdout.write(build.stdout)

        patched_source = re.sub(r"\bNF\b", "NFIELD", source).replace(
            "string(F==0)", "string(u==0)"
        )
        if sha_text(patched_source) != PATCHED_SELFCHECK_SHA256:
            raise SystemExit("PATCHED_SELFCHECK_HASH_DISAGREEMENT")
        patched = temp / "selfcheck_strata_r5_materialized.py"
        patched.write_text(patched_source)
        replay = subprocess.run(
            [sys.executable, "-B", str(patched), "--case-dir", str(shadow),
             "--matrix", str(args.matrix.resolve()),
             "--fitting", str(args.fitting.resolve()),
             "--content", str(args.content.resolve())],
            cwd=temp, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            timeout=170,
        )
        sys.stdout.write(replay.stdout); sys.stderr.write(replay.stderr)
        if replay.returncode:
            raise SystemExit(f"PATCHED_R2_SELFCHECK_FAILURE:{replay.returncode}")
        if replay.stderr:
            raise SystemExit("PATCHED_R2_SELFCHECK_STDERR")
    print(f"PATCHED_SELFCHECK_SHA256={PATCHED_SELFCHECK_SHA256}")
    print("STRATA_R5_ADAPTER_FIX_PASS")


if __name__ == "__main__":
    main()
