#!/usr/bin/env python3
"""Full r6 check of ambient reduction and quotient-ideal introspection."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import re
import subprocess
import sys
import tempfile


R2_SELFCHECK_SHA256 = "4582e1784e3acc69878fdd3649d18f8ec7d64804b4968536ff7e2aedf19c1888"
PATCHED_SELFCHECK_SHA256 = "8850f6fa2eff28731a511f52da633f949835ce4f1a8dd36365e0700081411b93"
R6_COMPILER_SHA256 = "a5587996f3d9de7049fe5de790d9bd16a53fa389732016bc4642e2c02a7d0d11"
OLD_QRING_LINE = '"ring a=0,(u,v),dp; poly F=u; ideal J=F; qring q=std(J);\\n"'
NEW_QRING_LINE = '"ring a=0,(u,v),dp; poly F=u; ideal J=F; ideal JSB=std(J); poly REM=reduce(F,JSB); print(\\"TINY_QRING_AMBIENT_REPLAY=\\"+string(REM==0)); qring q=JSB;\\n"'
OLD_MARKERS = '            "TINY_QRING_RELATION=1", "TINY_QRING_REPLAY=1",\n'
NEW_MARKERS = '            "TINY_QRING_AMBIENT_REPLAY=1", "TINY_QRING_RELATION=1", "TINY_QRING_REPLAY=1",\n'


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
    source = (r2_case / "selfcheck_strata.py").read_text()
    if sha_text(source) != R2_SELFCHECK_SHA256:
        raise SystemExit("R2_SELFCHECK_SOURCE_DRIFT")
    if (len(re.findall(r"\bNF\b", source)) != 6
            or source.count(OLD_QRING_LINE) != 1
            or source.count("string(F==0)") != 1
            or source.count(OLD_MARKERS) != 1):
        raise SystemExit("R2_SELFCHECK_MUTATION_SITE_DRIFT")

    with tempfile.TemporaryDirectory(prefix="endpoint-strata-r6-selfcheck-") as raw:
        temp = Path(raw)
        negative = temp / "reserved_nf_negative.sing"
        negative.write_text(
            "ring f=(0,a,b),(z),dp; matrix MF[2][3]=1,0,a/b,0,1,0;\n"
            "module KF=syz(module(MF)); matrix NF=matrix(KF);\n"
            "print(\"NEGATIVE_CONTROL_CONTINUED\"); quit;\n"
        )
        mutation = subprocess.run(
            ["Singular", "-q", str(negative)], cwd=temp, text=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=20,
        )
        negative_text = mutation.stdout + mutation.stderr
        if ("last reserved name was `NF`" not in negative_text
                or "NEGATIVE_CONTROL_CONTINUED" not in negative_text):
            raise SystemExit("RESERVED_NF_CONTINUATION_NEGATIVE_CONTROL_FAILURE")
        print("RESERVED_NF_AND_CONTINUATION_NEGATIVE_CONTROL_PASS")
        print(f"RESERVED_NF_NEGATIVE_SHA256={sha_text(negative_text)}")

        shadow = temp / "shadow_case"
        shadow.mkdir()
        compiler = shadow / "build_strata_scripts.py"
        build = subprocess.run(
            [sys.executable, "-B", str(case_dir / "build_compiler_r6.py"),
             "--r2-compiler", str(r2_case / "build_strata_scripts.py"),
             "--output", str(compiler)],
            cwd=temp, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            timeout=30,
        )
        if build.returncode or build.stderr or sha_text(compiler.read_text()) != R6_COMPILER_SHA256:
            sys.stdout.write(build.stdout); sys.stderr.write(build.stderr)
            raise SystemExit("R6_COMPILER_MATERIALIZATION_FAILURE")
        sys.stdout.write(build.stdout)

        patched_source = re.sub(r"\bNF\b", "NFIELD", source)
        patched_source = patched_source.replace(OLD_QRING_LINE, NEW_QRING_LINE)
        patched_source = patched_source.replace(
            "string(F==0)", "string(size(ideal(basering))>0)"
        ).replace(OLD_MARKERS, NEW_MARKERS)
        if sha_text(patched_source) != PATCHED_SELFCHECK_SHA256:
            raise SystemExit("PATCHED_SELFCHECK_HASH_DISAGREEMENT")
        patched = temp / "selfcheck_strata_r6_materialized.py"
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
    print("STRATA_R6_ADAPTER_FIX_PASS")


if __name__ == "__main__":
    main()
