#!/usr/bin/env python3
"""Light exact adapter checks; no full 106-by-105 kernel is computed here."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import subprocess
import tempfile


EXPECTED = {
    "input/symbolic_quadratic_q_rankdrop.sing": "56f09440c924ba7c32ca15c74e585533ab79023c8dfaf17bc6abd47077132d7c",
    "input/FITTING_STRATA_RAW.sing": "d9df4dd576ad4219ac24f52196945760a52989b86a888d31e6e09a8adc2a31ec",
    "input/LEFT_KERNEL_RAW.sing": "a6ec975c07bfc27fd7e383bb3afbdee2cc87d009a1361499e94542e42416391d",
    "input/COFACTOR_CONTENT.txt": "8359a8d4875e764ea67855dd34614c95d52e5f91f2506f159de0adf22369aa4e",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_singular(path: Path, cwd: Path) -> str:
    proc = subprocess.run(
        ["Singular", "-q", str(path)], cwd=cwd, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30,
    )
    if proc.returncode or proc.stderr.strip():
        raise SystemExit(f"SINGULAR_FAILURE rc={proc.returncode} stderr={proc.stderr}")
    return proc.stdout


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case-dir", type=Path, required=True)
    args = parser.parse_args()
    case_dir = args.case_dir.resolve()
    for relative, expected in EXPECTED.items():
        actual = sha256(case_dir / relative)
        if actual != expected:
            raise SystemExit(f"HASH_MISMATCH {relative} {actual}")
    with tempfile.TemporaryDirectory(prefix="endpoint-kernel-selfcheck-") as raw:
        temp = Path(raw)
        built = temp / "built"
        subprocess.run(
            ["python3", "-B", str(case_dir / "build_component_scripts.py"),
             "--source", str(case_dir / "input/symbolic_quadratic_q_rankdrop.sing"),
             "--fitting", str(case_dir / "input/FITTING_STRATA_RAW.sing"),
             "--output-dir", str(built)],
            check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            timeout=30,
        )
        for name in ("c8", "q1", "p"):
            output = run_singular(built / f"parse_{name}.sing", temp)
            if f"FULL_MATRIX_PARSE_PASS COMPONENT={name.upper()}" not in output:
                raise SystemExit(f"FULL_MATRIX_PARSE_FAILURE {name}")
        c8_text = (built / "component_c8.sing").read_text()
        q1_text = (built / "component_q1.sing").read_text()
        if "c8" in c8_text.split("matrix M[106][105]=", 1)[1].split(";", 1)[0]:
            raise SystemExit("C8_TOKEN_REMAINS")
        if "q1" in q1_text.split("matrix M[106][105]=", 1)[1].split(";", 1)[0]:
            raise SystemExit("Q1_TOKEN_REMAINS")
        for script in (c8_text, q1_text):
            for fragment in (
                "module K=syz(module(M))",
                "matrix right_replay=M*KM",
                "x14*x72+x1*x97",
                "COMPONENT_GENERIC_ENDPOINT_SURVIVOR",
            ):
                if fragment not in script:
                    raise SystemExit(f"GENERIC_COMPONENT_FRAGMENT_MISSING {fragment}")
        for sample_id in ("01", "02", "03", "04", "05", "06"):
            sample_text = (built / f"p_sample_{sample_id}.sing").read_text()
            for fragment in (
                "factorize(RAW_CONTENT,1)",
                "PF!=P0+c8*P1",
                "m81check==0 && m93check==0",
                "P_SAMPLE_ENDPOINT_SURVIVOR",
            ):
                if fragment not in sample_text:
                    raise SystemExit(f"P_SAMPLE_FRAGMENT_MISSING {sample_id} {fragment}")
        tiny = temp / "tiny.sing"
        tiny.write_text(
            "ring r=(0,a),(z),dp;\n"
            "matrix M[3][4]=1,0,0,0,0,1,0,0,0,0,0,0;\n"
            "module K=syz(module(M)); matrix KM=matrix(K); matrix replay=M*KM;\n"
            "int kd=ncols(KM); int i; int j; int nonzero=0; number qc;\n"
            "for(i=1;i<=kd;i=i+1){ qc=leadcoef(KM[1,i])*leadcoef(KM[2,i])+leadcoef(KM[3,i])*leadcoef(KM[4,i]); if(qc!=0){nonzero=nonzero+1;} for(j=i+1;j<=kd;j=j+1){ qc=leadcoef(KM[1,i])*leadcoef(KM[2,j])+leadcoef(KM[1,j])*leadcoef(KM[2,i])+leadcoef(KM[3,i])*leadcoef(KM[4,j])+leadcoef(KM[3,j])*leadcoef(KM[4,i]); if(qc!=0){nonzero=nonzero+1;} } }\n"
            "print(\"TINY_RIGHT_KERNEL_DIMENSION=\"+string(kd));\n"
            "print(\"TINY_RIGHT_KERNEL_REPLAY_ZERO=\"+string(size(module(replay))==0));\n"
            "print(\"TINY_FULL_QUADRATIC_NONZERO_COEFFICIENTS=\"+string(nonzero));\n"
            "ring P=0,(q0,q1,c8),dp; poly G=c8*q1*(q0+c8); list L=factorize(G,1); ideal F=L[1]; matrix FM=matrix(F); poly PF=0; for(i=1;i<=ncols(FM);i=i+1){if(deg(FM[1,i])>1){PF=FM[1,i];}} poly P0=subst(PF,c8,0); poly P1=subst(PF,c8,1)-P0;\n"
            "print(\"TINY_P_LINEAR_IDENTITY=\"+string(PF==P0+c8*P1));\n"
            "quit;\n"
        )
        output = run_singular(tiny, temp)
        for marker in (
            "TINY_RIGHT_KERNEL_DIMENSION=2",
            "TINY_RIGHT_KERNEL_REPLAY_ZERO=1",
            "TINY_FULL_QUADRATIC_NONZERO_COEFFICIENTS=1",
            "TINY_P_LINEAR_IDENTITY=1",
        ):
            if marker not in output:
                raise SystemExit(f"TINY_KERNEL_OR_P_FAILURE {marker} {output!r}")
    print("COMPONENT_ADAPTER_SELFCHECK_PASS")
    print("FULL_MATRIX_PARSE_PASS_C8_Q1_P")
    print("TINY_FULL_QUADRATIC_PULLBACK_PASS")
    print("TINY_P_FACTOR_CHART_PASS")


if __name__ == "__main__":
    main()

