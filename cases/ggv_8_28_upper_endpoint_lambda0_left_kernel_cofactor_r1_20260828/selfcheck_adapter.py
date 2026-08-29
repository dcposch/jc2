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
        parse_stdout = run_singular(parsed, temp)
        if "FULL_MATRIX_PARSE_PASS ROWS=106 COLS=105" not in parse_stdout:
            raise SystemExit("FULL_MATRIX_PARSE_MARKER_MISSING")
        tiny = temp / "tiny.sing"
        tiny.write_text(
            "ring r=(0,a,b),(z),dp;\n"
            "matrix M[3][2]=1,0,0,1,a,b;\n"
            "module S=syz(module(transpose(M))); matrix SM=matrix(S);\n"
            "int o=3; matrix B[2][2]=1,0,0,1;\n"
            "number Delta=leadcoef(det(B,\"SBareiss\"));\n"
            "number scale=Delta/leadcoef(SM[o,1]); matrix ell[3][1]=scale*SM;\n"
            "matrix replay=transpose(ell)*M;\n"
            "matrix targets[2][2]; targets[2,1]=1; targets[1,2]=1;\n"
            "module row_basis=module(transpose(B)); module target_module=module(targets);\n"
            "matrix C=lift(row_basis,target_module); matrix U[3][2];\n"
            "U[1,1]=C[1,1]; U[1,2]=C[1,2]; U[2,1]=C[2,1]; U[2,2]=C[2,2];\n"
            "matrix dual_target[2][2]; dual_target[1,2]=Delta; dual_target[2,1]=Delta;\n"
            "matrix dual_replay=transpose(U)*M-dual_target;\n"
            "print(\"TINY_VECTOR=\"+string(ell[1,1])+\",\"+string(ell[2,1])+\",\"+string(ell[3,1]));\n"
            "print(\"TINY_REPLAY_ZERO=\"+string(size(module(replay))==0));\n"
            "print(\"TINY_ENDPOINT_DUAL_REPLAY_ZERO=\"+string(size(module(dual_replay))==0));\n"
            "quit;\n"
        )
        tiny_stdout = run_singular(tiny, temp)
        if "TINY_REPLAY_ZERO=1" not in tiny_stdout:
            raise SystemExit("TINY_REPLAY_FAILURE")
        if "TINY_ENDPOINT_DUAL_REPLAY_ZERO=1" not in tiny_stdout:
            raise SystemExit("TINY_ENDPOINT_DUAL_REPLAY_FAILURE")
        if "TINY_VECTOR=(-a),(-b),1" not in tiny_stdout.replace(" ", ""):
            raise SystemExit(f"TINY_VECTOR_MISMATCH {tiny_stdout!r}")
    print("ADAPTER_SELFCHECK_PASS")
    print("MATRIX_PARSE_PASS")
    print("TINY_RAW_COFACTOR_PASS")
    print("TINY_ENDPOINT_DUAL_PASS")


if __name__ == "__main__":
    main()
