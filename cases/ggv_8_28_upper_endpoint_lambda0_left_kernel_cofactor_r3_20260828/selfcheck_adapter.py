#!/usr/bin/env python3
"""Small exact desk/AWS self-check for the cofactor adapter."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import subprocess
import tempfile


EXPECTED = {
    "input/symbolic_quadratic_q_rankdrop.sing": "56f09440c924ba7c32ca15c74e585533ab79023c8dfaf17bc6abd47077132d7c",
    "input/equation_names.txt": "8d476d225af6c9c35f737d858dfc613913c727fc71ddb9e275d9509cfde86dd5",
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
    with tempfile.TemporaryDirectory(prefix="left-cofactor-selfcheck-") as raw:
        temp = Path(raw)
        built = temp / "left.sing"
        parsed = temp / "parse.sing"
        subprocess.run(
            ["python3", "-B", str(case_dir / "build_left_kernel_script.py"),
             "--source", str(case_dir / "input/symbolic_quadratic_q_rankdrop.sing"),
             "--output", str(built), "--parse-output", str(parsed)],
            check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            timeout=30,
        )
        built_text = built.read_text()
        for fragment in (
            "matrix ellP=imap(r,ell)",
            "matrix UP=imap(r,U)",
            "RAW_PARAMETER_DENOMINATORS_ABSENT",
            "LEFT_KERNEL_REPLAY_QPARAMS_ZERO",
            "RAW_ZERO_PATTERN_PRESERVED",
            "write(rawtsv,string(i)+\"\\t\"+string(liP))",
        ):
            if fragment not in built_text:
                raise SystemExit(f"GENERATED_ADAPTER_FRAGMENT_MISSING {fragment}")
        for forbidden in ("string(numerator(Delta))", "string(numerator(li))"):
            if forbidden in built_text:
                raise SystemExit(f"RAW_RATIONAL_SCALAR_STRIPPED {forbidden}")
        parse_stdout = run_singular(parsed, temp)
        if "FULL_MATRIX_PARSE_PASS ROWS=106 COLS=105" not in parse_stdout:
            raise SystemExit("FULL_MATRIX_PARSE_MARKER_MISSING")
        tiny = temp / "tiny.sing"
        tiny.write_text(
            "ring r=(0,a,b),(z),dp;\n"
            "matrix M[3][2]=(1/4),0,0,(1/3),a,0;\n"
            "module S=syz(module(transpose(M))); matrix SM=matrix(S);\n"
            "int o=3; matrix B[2][2]=(1/4),0,0,(1/3);\n"
            "number Delta=leadcoef(det(B,\"SBareiss\"));\n"
            "number scale=Delta/leadcoef(SM[o,1]); matrix ell[3][1]=scale*SM;\n"
            "matrix replay=transpose(ell)*M;\n"
            "string zero_pattern=\"\"; int i;\n"
            "for(i=1;i<=3;i=i+1){ if(ell[i,1]==0){ zero_pattern=zero_pattern+\"0\"; } else { zero_pattern=zero_pattern+\"1\"; } }\n"
            "number constant_rational=(a+1)/12; number bad_rational=(a+1)/(b+1);\n"
            "string dc=string(denominator(constant_rational)); string db=string(denominator(bad_rational));\n"
            "int constant_accept=(find(dc,\"a\")==0 && find(dc,\"b\")==0); int parameter_reject=(find(db,\"b\")>0);\n"
            "matrix targets[2][2]; targets[2,1]=1; targets[1,2]=1;\n"
            "module row_basis=module(transpose(B)); module target_module=module(targets);\n"
            "matrix C=lift(row_basis,target_module); matrix Craw=Delta*C; matrix U[3][2];\n"
            "U[1,1]=Craw[1,1]; U[1,2]=Craw[1,2]; U[2,1]=Craw[2,1]; U[2,2]=Craw[2,2];\n"
            "matrix dual_target[2][2]; dual_target[1,2]=Delta; dual_target[2,1]=Delta;\n"
            "matrix dual_replay=transpose(U)*M-dual_target;\n"
            "int field_replay=(size(module(replay))==0); int field_dual_replay=(size(module(dual_replay))==0);\n"
            "ring P=0,(a,b),dp;\n"
            "matrix MP=imap(r,M); matrix ellP=imap(r,ell); matrix UP=imap(r,U); poly DeltaP=imap(r,Delta);\n"
            "matrix replayP=transpose(ellP)*MP; matrix dual_targetP[2][2]; dual_targetP[1,2]=DeltaP; dual_targetP[2,1]=DeltaP;\n"
            "matrix dual_replayP=transpose(UP)*MP-dual_targetP; string zero_patternP=\"\";\n"
            "for(i=1;i<=3;i=i+1){ if(ellP[i,1]==0){ zero_patternP=zero_patternP+\"0\"; } else { zero_patternP=zero_patternP+\"1\"; } }\n"
            "int exact_values=(ellP[1,1]==(-1/3)*a && ellP[2,1]==0 && ellP[3,1]==1/12);\n"
            "print(\"TINY_EXACT_SIGNED_MINORS=\"+string(exact_values));\n"
            "print(\"TINY_ZERO_PATTERN=\"+zero_patternP);\n"
            "print(\"TINY_ZERO_PATTERN_PRESERVED=\"+string(zero_patternP==zero_pattern));\n"
            "print(\"TINY_CONSTANT_RATIONAL_ACCEPT=\"+string(constant_accept));\n"
            "print(\"TINY_PARAMETER_DENOMINATOR_REJECT=\"+string(parameter_reject));\n"
            "print(\"TINY_REPLAY_ZERO=\"+string(field_replay && size(module(replayP))==0));\n"
            "print(\"TINY_ENDPOINT_DUAL_REPLAY_ZERO=\"+string(field_dual_replay && size(module(dual_replayP))==0));\n"
            "quit;\n"
        )
        tiny_stdout = run_singular(tiny, temp)
        if "TINY_REPLAY_ZERO=1" not in tiny_stdout:
            raise SystemExit("TINY_REPLAY_FAILURE")
        if "TINY_ENDPOINT_DUAL_REPLAY_ZERO=1" not in tiny_stdout:
            raise SystemExit("TINY_ENDPOINT_DUAL_REPLAY_FAILURE")
        for marker in (
            "TINY_EXACT_SIGNED_MINORS=1",
            "TINY_ZERO_PATTERN=101",
            "TINY_ZERO_PATTERN_PRESERVED=1",
            "TINY_CONSTANT_RATIONAL_ACCEPT=1",
            "TINY_PARAMETER_DENOMINATOR_REJECT=1",
        ):
            if marker not in tiny_stdout:
                raise SystemExit(f"TINY_RATIONAL_POLYNOMIAL_FAILURE {marker} {tiny_stdout!r}")
    print("ADAPTER_SELFCHECK_PASS")
    print("MATRIX_PARSE_PASS")
    print("TINY_RAW_COFACTOR_PASS")
    print("TINY_ENDPOINT_DUAL_PASS")
    print("TINY_QPARAMS_RECOMPOSITION_PASS")
    print("TINY_PARAMETER_DENOMINATOR_GATE_PASS")


if __name__ == "__main__":
    main()
