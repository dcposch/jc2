#!/usr/bin/env python3
"""AWS-only exact replay of proposed constant kernels of frozen K00 A."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess


CASE_REL = "cases/max12_812_order2_u2_62_k00_rank_compressed_atlas_v27_20260827"
V26_REL = "cases/max12_812_order2_u2_62_k00_grade7_fitting_atlas_v26_20260827"
COMPILED_REL = V26_REL + "/aws_box02_r2_held_compile/output"
PINNED_SHA256 = {
    COMPILED_REL + "/ATLAS_EXACT_POLYNOMIALS.json":
        "d7ec6d18d58265421ff315fa00e38cd32992ac12f7d8166cf6c436e23bf06501",
    COMPILED_REL + "/COMPILED_SOURCE.sha256":
        "5de20da0d3501db668fca38db3c678ba4719745e3df7b32d0d0a8d2867e4da32",
    COMPILED_REL + "/RESULT.json":
        "f1a6f1fc988fc77816daaab13b294b1321de7e476d2891cf7fbfa2e033868d97",
    CASE_REL + "/RESULT_V27_BASE3_R2_EXACT_PREPASS.md":
        "c42c0482f0b5861f5099e6e121c60a93d018c87a9619749ee1844f5954545c39",
    CASE_REL + "/REVIEW_PACKET_BASE3_R2.sha256":
        "e3cd6586c2db1b51aabedb613f3de5a18c81a14b26bd8a6f9ae42af4b68626f3",
}
STATUS = "PASS_V27_AUX_CONSTANT_KERNEL_IDENTITIES_EXACT_EXPLANATORY_ONLY"


def fail(message: object) -> "None":
    raise RuntimeError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def poly(item: dict) -> str:
    value = item.get("singular")
    if not isinstance(value, str) or not value:
        fail("exact polynomial serialization missing")
    return value


def qpath(path: Path) -> str:
    value = str(path.resolve())
    if '"' in value or "\n" in value:
        fail("unsafe artifact path")
    return value


def run_singular(executable: str, script: Path, stdout: Path, stderr: Path,
                 timeout: int) -> str:
    completed = subprocess.run(
        [executable, "-q", str(script)], cwd=script.parent, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
    stdout.write_text(completed.stdout)
    stderr.write_text(completed.stderr)
    diagnostics = re.compile(
        r"(?mi)^\s*\?|// \*\*|warning|error occurred|K00_KERNEL_FAIL=")
    if completed.returncode != 0 or completed.stderr or \
            not completed.stdout.strip() or diagnostics.search(completed.stdout):
        fail(("Singular identity replay failed", script.name,
              completed.returncode, completed.stderr[-2000:],
              completed.stdout[-4000:]))
    return completed.stdout


def script_text(atlas: dict, serialized: Path, prefix: str,
                mutations: bool) -> str:
    ring_variables = atlas.get("ring_variables")
    matrix = atlas.get("A")
    vector_b = atlas.get("b")
    if not isinstance(ring_variables, list) or len(ring_variables) != 33 or \
            len(set(ring_variables)) != 33:
        fail("frozen full-ring variable census mismatch")
    if not isinstance(matrix, list) or len(matrix) != 7 or \
            any(not isinstance(row, list) or len(row) != 7 for row in matrix):
        fail("frozen A shape mismatch")
    if not isinstance(vector_b, list) or len(vector_b) != 7:
        fail("frozen b shape mismatch")
    lines = [
        "ring R=0,(" + ",".join(ring_variables) + "),dp;",
        "matrix A[7][7]=" + ",".join(
            f"({poly(entry)})" for row in matrix for entry in row) + ";",
        "matrix b[7][1]=" + ",".join(
            f"({poly(entry)})" for entry in vector_b) + ";",
        "matrix L[1][7]=5/1024,0,3/128,0,1/8,0,1;",
        "matrix V1[7][1]=2,0,1,0,1,0,0;",
        "matrix V2[7][1]=0,1/16,0,1/2,0,1,0;",
        "matrix LA=L*A; matrix AV1=A*V1; matrix AV2=A*V2;",
        "int bad=0; int ii;",
        "for (ii=1;ii<=7;ii++) { if (LA[1,ii]!=0) { bad++; } }",
        "for (ii=1;ii<=7;ii++) { if (AV1[ii,1]!=0) { bad++; } }",
        "for (ii=1;ii<=7;ii++) { if (AV2[ii,1]!=0) { bad++; } }",
        'if (bad) { print("K00_KERNEL_FAIL=PROPOSED_IDENTITY"); quit; }',
        "ideal I6A=minor(A,6); ideal I5A=minor(A,5);",
        'if ((size(I6A)!=0)||(size(I5A)!=90)) { print("K00_KERNEL_FAIL=GENERIC_RANK_CONTROL"); quit; }',
        "matrix Lb=L*b; poly l0b=Lb[1,1]; int l0bterms=size(l0b);",
        'if ((l0b==0)||(l0bterms!=690)) { print("K00_KERNEL_FAIL=L0_B_CONTROL"); quit; }',
    ]
    if mutations:
        lines.extend([
            "matrix LM=L; LM[1,1]=LM[1,1]+1; matrix LMA=LM*A; int lmut=0;",
            "for (ii=1;ii<=7;ii++) { if (LMA[1,ii]!=0) { lmut++; } }",
            'if (lmut==0) { print("K00_KERNEL_FAIL=LEFT_MUTATION"); quit; }',
            "matrix V1M=V1; V1M[1,1]=V1M[1,1]+1; matrix AV1M=A*V1M; int v1mut=0;",
            "for (ii=1;ii<=7;ii++) { if (AV1M[ii,1]!=0) { v1mut++; } }",
            'if (v1mut==0) { print("K00_KERNEL_FAIL=V1_MUTATION"); quit; }',
            "matrix V2M=V2; V2M[2,1]=V2M[2,1]+1; matrix AV2M=A*V2M; int v2mut=0;",
            "for (ii=1;ii<=7;ii++) { if (AV2M[ii,1]!=0) { v2mut++; } }",
            'if (v2mut==0) { print("K00_KERNEL_FAIL=V2_MUTATION"); quit; }',
            'print("K00_KERNEL_MUTATIONS="+string(lmut)+","+string(v1mut)+","+string(v2mut));',
        ])
    lines.extend([
        f'write("{qpath(serialized)}",string(l0b));',
        f'print("K00_KERNEL_{prefix}=PASS");',
        'print("K00_KERNEL_L0B_TERMS="+string(l0bterms));',
        "quit;",
    ])
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_root", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--timeout", type=int, default=540)
    args = parser.parse_args()
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if platform.system() != "Linux" or not vendor.is_file() or \
            vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only constant-kernel replay refused host")
    lane = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not lane.startswith("max12_812_order2_u2_62_k00_v27_kernel_replay_"):
        fail("registered auxiliary lane missing")
    if args.timeout <= 0 or args.timeout > 540:
        fail("inner timeout outside preregistered cap")
    source_root = args.source_root.resolve()
    for relative, expected in PINNED_SHA256.items():
        path = source_root / relative
        if not path.is_file() or digest(path) != expected:
            fail(("pinned source mismatch", relative))
    atlas = json.loads(
        (source_root / (COMPILED_REL + "/ATLAS_EXACT_POLYNOMIALS.json"))
        .read_text())
    compiler = json.loads(
        (source_root / (COMPILED_REL + "/RESULT.json")).read_text())
    if compiler.get("generic_rank_A") != 5:
        fail("frozen compiler generic-rank control mismatch")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    singular = shutil.which("Singular")
    if singular is None:
        fail("Singular missing")
    version = subprocess.run(
        [singular, "--version"], text=True, stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT, timeout=30, check=True).stdout.splitlines()[0]
    artifacts: list[Path] = []
    serialized_paths = []
    for prefix, mutations in (("PRIMARY", True), ("REPLAY", False)):
        lower = prefix.lower()
        serialized = output / f"L0_B_{prefix}.txt"
        script = output / f"constant_kernel_{lower}.sing"
        script.write_text(script_text(atlas, serialized, prefix, mutations))
        stdout = output / f"constant_kernel_{lower}.stdout"
        stderr = output / f"constant_kernel_{lower}.stderr"
        markers = run_singular(singular, script, stdout, stderr, args.timeout)
        if f"K00_KERNEL_{prefix}=PASS" not in markers or \
                "K00_KERNEL_L0B_TERMS=690" not in markers:
            fail(("identity custody marker missing", prefix))
        if not serialized.is_file() or serialized.stat().st_size == 0:
            fail(("serialized l0*b missing", prefix))
        artifacts.extend([script, stdout, stderr, serialized])
        serialized_paths.append(serialized)
    if serialized_paths[0].read_bytes() != serialized_paths[1].read_bytes():
        fail("second-process l0*b byte mismatch")
    payload = {
        "status": STATUS,
        "lifecycle": "AUXILIARY_PRODUCER_UNREVIEWED_EXPLANATORY_ONLY",
        "field": "Q_exact",
        "registered_aws_lane": lane,
        "singular_version": version,
        "identities": {
            "l0_times_A_zero": True,
            "A_times_v1_zero": True,
            "A_times_v2_zero": True,
            "l0": ["5/1024", "0", "3/128", "0", "1/8", "0", "1"],
            "v1": ["2", "0", "1", "0", "1", "0", "0"],
            "v2": ["0", "1/16", "0", "1/2", "0", "1", "0"],
        },
        "generic_rank_A_exact": 5,
        "I6A_stored_nonzero": 0,
        "I5A_stored_nonzero": 90,
        "l0_times_b_zero": False,
        "l0_times_b_exact_terms": 690,
        "l0_times_b_sha256": digest(serialized_paths[0]),
        "independent_second_process_replay": True,
        "coefficient_mutations": "LEFT_V1_V2_ALL_BREAK_THEIR_IDENTITY",
        "interpretation": (
            "GLOBAL_CONSTANT_KERNEL_STRUCTURE_EXPLAINS_GENERIC_RANK_AT_MOST_5_"
            "AND_I6_ZERO_ONLY_NOT_BASE4_OR_BASE3_IDEAL_CONTAINMENTS"
        ),
        "sampled_pencil_claims_consumed": False,
        "source_hashes": PINNED_SHA256,
        "artifacts": {
            path.name: {"sha256": digest(path), "bytes": path.stat().st_size}
            for path in artifacts
        },
        "firewall": (
            "NO_RANK_STRATUM_VERDICT_NO_SAMPLED_PENCIL_NO_RATIONAL_POINT_"
            "NO_FULL_P6_NO_GRADE7_NO_JET_NO_ARC_NO_CLOSURE_NO_JC2"
        ),
    }
    (output / "RESULT.json").write_text(
        json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print("K00_V27_KERNEL_REPLAY=" + STATUS)
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()

