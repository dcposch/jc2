#!/usr/bin/env python3
"""Bounded exact adapter selfcheck; intended for the audited AWS worker."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import subprocess
import tempfile


EXPECTED = {
    "matrix": "56f09440c924ba7c32ca15c74e585533ab79023c8dfaf17bc6abd47077132d7c",
    "fitting": "d9df4dd576ad4219ac24f52196945760a52989b86a888d31e6e09a8adc2a31ec",
    "content": "8359a8d4875e764ea67855dd34614c95d52e5f91f2506f159de0adf22369aa4e",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def singular(script: Path, cwd: Path, timeout: int = 30) -> str:
    process = subprocess.run(
        ["Singular", "-q", str(script)], cwd=cwd, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout,
    )
    if process.returncode or process.stderr.strip():
        raise SystemExit(
            f"SINGULAR_SELFCHECK_FAILURE rc={process.returncode} stderr={process.stderr}"
        )
    return process.stdout


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case-dir", type=Path, required=True)
    parser.add_argument("--matrix", type=Path, required=True)
    parser.add_argument("--fitting", type=Path, required=True)
    parser.add_argument("--content", type=Path, required=True)
    args = parser.parse_args()
    case_dir = args.case_dir.resolve()
    inputs = {
        "matrix": args.matrix.resolve(),
        "fitting": args.fitting.resolve(),
        "content": args.content.resolve(),
    }
    for name, path in inputs.items():
        actual = sha256(path)
        if actual != EXPECTED[name]:
            raise SystemExit(f"SELFCHECK_INPUT_HASH_MISMATCH {name} {actual}")

    with tempfile.TemporaryDirectory(prefix="endpoint-strata-selfcheck-") as raw:
        temp = Path(raw)
        base = temp / "base"
        subprocess.run(
            ["python3", "-B", str(case_dir / "build_strata_scripts.py"),
             "--phase", "base", "--matrix", str(inputs["matrix"]),
             "--fitting", str(inputs["fitting"]), "--content", str(inputs["content"]),
             "--output-dir", str(base)],
            check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            timeout=30,
        )
        p = (base / "P_EXACT.txt").read_text().strip()
        p0 = (base / "P0_EXACT.txt").read_text().strip()
        p1 = (base / "P1_EXACT.txt").read_text().strip()
        if not p or not p0 or not p1 or "c8" in p0 or "c8" in p1:
            raise SystemExit("SELFCHECK_P_LINEAR_TEXT_FAILURE")
        for name in ("p_generic", "c8_q1"):
            script = (base / f"{name}.sing").read_text()
            for fragment in (
                "module K=syz(module(M))", "matrix replay=M*N",
                "N[14,i]*N[72,j]+N[14,j]*N[72,i]",
                "N[1,i]*N[97,j]+N[1,j]*N[97,i]",
                "GENERIC_ENDPOINT_DEAD_RANK_JUMPS_PENDING",
            ):
                if fragment not in script:
                    raise SystemExit(f"SELFCHECK_PULLBACK_FRAGMENT_MISSING {name} {fragment}")
            output = singular(base / f"parse_{name}.sing", temp)
            if f"FULL_MATRIX_PARSE_PASS={name.upper()}" not in output:
                raise SystemExit(f"SELFCHECK_FULL_MATRIX_PARSE_FAILURE {name}")

        census_output = singular(base / "factor_census.sing", temp)
        for marker in (
            "RAW_CONTENT_DISTINCT_FACTOR_COUNT=3",
            "P_IRREDUCIBLE_FACTOR_COUNT=1",
            "P_LINEAR_C8_IDENTITY=1",
            "RAW_CONTENT_DIVISIBLE_P_C8_Q1=1",
            "FACTOR_CENSUS_PASS=1",
        ):
            if marker not in census_output:
                raise SystemExit(f"SELFCHECK_FACTOR_CENSUS_FAILURE {marker}")
        branches = temp / "branches"
        subprocess.run(
            ["python3", "-B", str(case_dir / "build_strata_scripts.py"),
             "--phase", "branches", "--matrix", str(inputs["matrix"]),
             "--census-dir", str(temp), "--output-dir", str(branches)],
            check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            timeout=30,
        )
        manifest = (branches / "BRANCH_MANIFEST.tsv").read_text()
        for family in ("C8P", "Q1P", "TRIPLE"):
            if family + "|" not in manifest:
                raise SystemExit(f"SELFCHECK_BRANCH_FAMILY_MISSING {family}")
        for path in branches.glob("*.sing"):
            if path.name.endswith("_parse.sing"):
                continue
            script = path.read_text()
            for fragment in (
                "module K=syz(module(M))", "N[14,i]*N[72,j]",
                "N[1,i]*N[97,j]", "RANK_JUMP",
            ):
                if fragment not in script:
                    raise SystemExit(f"SELFCHECK_BRANCH_FRAGMENT_MISSING {path.name} {fragment}")

        tiny = temp / "tiny.sing"
        tiny.write_text(
            "ring f=(0,a,b),(z),dp;\n"
            "matrix MF[2][3]=1,0,a/b,0,1,0; module KF=syz(module(MF)); matrix NF=matrix(KF); matrix RF=MF*NF;\n"
            "poly EF=NF[1,1]*NF[2,1]+NF[3,1]^2; number DF=denominator(leadcoef(NF[1,1]));\n"
            "print(\"TINY_FIELD_REPLAY=\"+string(size(module(RF))==0)); print(\"TINY_FIELD_DENOMINATOR_DEFINED=\"+string(DF!=0));\n"
            "ring a=0,(u,v),dp; poly F=u; ideal J=F; qring q=std(J);\n"
            "matrix MQ[2][3]=1,0,v,0,1,0; module KQ=syz(module(MQ)); matrix NQ=matrix(KQ); matrix RQ=MQ*NQ;\n"
            "poly C=NQ[1,1]*NQ[2,1]+NQ[3,1]^2;\n"
            "print(\"TINY_QRING_RELATION=\"+string(F==0)); print(\"TINY_QRING_REPLAY=\"+string(size(module(RQ))==0)); print(\"TINY_QRING_PULLBACK_DEFINED=\"+string(C==C)); quit;\n"
        )
        tiny_output = singular(tiny, temp)
        for marker in (
            "TINY_FIELD_REPLAY=1", "TINY_FIELD_DENOMINATOR_DEFINED=1",
            "TINY_QRING_RELATION=1", "TINY_QRING_REPLAY=1",
            "TINY_QRING_PULLBACK_DEFINED=1",
        ):
            if marker not in tiny_output:
                raise SystemExit(f"SELFCHECK_TINY_ALGEBRA_FAILURE {marker}")
    print("STRATA_ADAPTER_SELFCHECK_PASS")
    print("P_IRREDUCIBILITY_AND_LINEAR_CHART_SELFCHECK_PASS")
    print("FULL_QUADRATIC_DIAGONAL_CROSS_TERM_SELFCHECK_PASS")
    print("QUOTIENT_BRANCH_SELFCHECK_PASS")


if __name__ == "__main__":
    main()
