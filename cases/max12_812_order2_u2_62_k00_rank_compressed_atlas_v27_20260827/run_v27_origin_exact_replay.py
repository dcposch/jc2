#!/usr/bin/env python3
"""AWS-only exact verification that frozen B+I5(A) vanishes at the origin."""

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


V26_REL = "cases/max12_812_order2_u2_62_k00_grade7_fitting_atlas_v26_20260827"
ATLAS_REL = V26_REL + "/aws_box02_r2_held_compile/output/ATLAS_EXACT_POLYNOMIALS.json"
ATLAS_SHA = "d7ec6d18d58265421ff315fa00e38cd32992ac12f7d8166cf6c436e23bf06501"
STATUS = "PASS_V27_AUX_ORIGIN_B_I5_EXACT_TRIVIAL_Q_POINT"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def poly(item: dict) -> str:
    value = item.get("singular")
    if not isinstance(value, str) or not value:
        fail("missing exact polynomial")
    return value


def definitions(atlas: dict) -> list[str]:
    matrix = atlas.get("A")
    qlist = atlas.get("Q1_to_Q6")
    if not isinstance(matrix, list) or len(matrix) != 7 or \
            any(not isinstance(row, list) or len(row) != 7 for row in matrix):
        fail("A shape mismatch")
    if not isinstance(qlist, list) or len(qlist) != 6:
        fail("B source census mismatch")
    return [
        "ring R=0,(d0_1,d1_1,d2_1,d3_1,d4_1,d5_1),dp;",
        "matrix A[7][7]=" + ",".join(
            f"({poly(entry)})" for row in matrix for entry in row) + ";",
        "ideal B=" + ",".join(f"({poly(item)})" for item in qlist) +
        f",({poly(atlas['F10'])});",
        "ideal I5A=minor(A,5);",
        "ideal M0=d0_1,d1_1,d2_1,d3_1,d4_1,d5_1; ideal G0=std(M0);",
        "ideal AE=" + ",".join(f"A[{row},{column}]"
            for row in range(1, 8) for column in range(1, 8)) + ";",
        'if ((size(B)!=7)||(size(I5A)!=90)) { print("K00_ORIGIN_FAIL=CENSUS"); quit; }',
        "ideal B0=reduce(B,G0); ideal I50=reduce(I5A,G0); ideal A0=reduce(AE,G0);",
        "int bad=0; int ii;",
        "for (ii=1;ii<=size(B0);ii++) { if (B0[ii]!=0) { bad++; } }",
        "for (ii=1;ii<=size(I50);ii++) { if (I50[ii]!=0) { bad++; } }",
        "for (ii=1;ii<=size(A0);ii++) { if (A0[ii]!=0) { bad++; } }",
        'if (bad) { print("K00_ORIGIN_FAIL=NONZERO_EVALUATION"); quit; }',
    ]


def run(executable: str, script: Path, stdout: Path, stderr: Path,
        timeout: int) -> str:
    completed = subprocess.run(
        [executable, "-q", str(script)], cwd=script.parent, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
    stdout.write_text(completed.stdout)
    stderr.write_text(completed.stderr)
    diagnostics = re.compile(r"(?mi)^\s*\?|// \*\*|warning|error occurred|K00_ORIGIN_FAIL=")
    if completed.returncode or completed.stderr or not completed.stdout.strip() or \
            diagnostics.search(completed.stdout):
        fail(("origin exact replay failed", completed.returncode,
              completed.stderr[-2000:], completed.stdout[-4000:]))
    return completed.stdout


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_root", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--timeout", type=int, default=540)
    args = parser.parse_args()
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if platform.system() != "Linux" or not vendor.is_file() or \
            vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only origin replay refused host")
    lane = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not lane.startswith("max12_812_order2_u2_62_k00_v27_origin_replay_"):
        fail("registered origin lane missing")
    if args.timeout <= 0 or args.timeout > 540:
        fail("inner timeout outside cap")
    source_root = args.source_root.resolve()
    atlas_path = source_root / ATLAS_REL
    if not atlas_path.is_file() or digest(atlas_path) != ATLAS_SHA:
        fail("frozen atlas hash mismatch")
    atlas = json.loads(atlas_path.read_text())
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    singular = shutil.which("Singular")
    if singular is None:
        fail("Singular missing")
    version = subprocess.run(
        [singular, "--version"], text=True, stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT, timeout=30, check=True).stdout.splitlines()[0]
    artifacts: list[Path] = []
    base = definitions(atlas)
    for name, mutate in (("primary", True), ("replay", False)):
        extra = []
        if mutate:
            extra = [
                "ideal BM=B; BM[1]=BM[1]+1; ideal BM0=reduce(BM,G0);",
                'if (BM0[1]==0) { print("K00_ORIGIN_FAIL=B_MUTATION"); quit; }',
                "ideal I5M=I5A; I5M[1]=I5M[1]+1; ideal I5M0=reduce(I5M,G0);",
                'if (I5M0[1]==0) { print("K00_ORIGIN_FAIL=I5_MUTATION"); quit; }',
                'print("K00_ORIGIN_MUTATIONS=PASS");',
            ]
        script = output / f"origin_{name}.sing"
        script.write_text("\n".join(base + extra + [
            f'print("K00_ORIGIN_{name.upper()}=PASS");',
            'print("K00_ORIGIN_B_COUNT=7"); print("K00_ORIGIN_I5_COUNT=90"); quit;',
        ]) + "\n")
        stdout = output / f"origin_{name}.stdout"
        stderr = output / f"origin_{name}.stderr"
        markers = run(singular, script, stdout, stderr, args.timeout)
        if f"K00_ORIGIN_{name.upper()}=PASS" not in markers or \
                "K00_ORIGIN_B_COUNT=7" not in markers or \
                "K00_ORIGIN_I5_COUNT=90" not in markers:
            fail("origin replay custody marker missing")
        artifacts.extend([script, stdout, stderr])
    payload = {
        "status": STATUS,
        "field": "Q_exact",
        "registered_aws_lane": lane,
        "singular_version": version,
        "origin": {name: 0 for name in
                   ("d0_1", "d1_1", "d2_1", "d3_1", "d4_1", "d5_1")},
        "B_generators_checked": 7,
        "I5A_stored_nonzero_generators_checked": 90,
        "A_entries_checked": 49,
        "all_vanish_at_origin": True,
        "independent_second_process_replay": True,
        "mutations": "ADD_ONE_TO_B1_AND_I5A1_BOTH_BREAK_ORIGIN_VANISHING",
        "corrected_useful_target": (
            "NONZERO_OR_PROJECTIVE_OR_SOURCE_OPEN_OR_FULL_P6_COMPATIBLE_POINT"
        ),
        "mere_rational_point_target_is_trivial": True,
        "artifacts": {
            path.name: {"sha256": digest(path), "bytes": path.stat().st_size}
            for path in artifacts
        },
        "source_hashes": {ATLAS_REL: ATLAS_SHA},
        "firewall": "NO_NONZERO_POINT_NO_SOURCE_OPEN_POINT_NO_FULL_P6_NO_JET_NO_ARC_NO_JC2",
    }
    (output / "RESULT.json").write_text(
        json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print("K00_V27_ORIGIN=" + STATUS)
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
