#!/usr/bin/env python3
"""Direct exact-Q lift of the target 1 for the V24 localized prior ideal."""

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


HERE = Path(__file__).resolve().parent
ORIGINAL = HERE / "aws_r6b_pass/output/modular_prior_reduction_v24.sing"
V24_RESULT = HERE / "aws_r6b_pass/output/RESULT.json"
R1_RESULT = HERE / "aws_r6b_r1_unit/output/RESULT.json"
PREREG = HERE / "PREREGISTRATION_R5_DIRECT_EXACT_LIFT.md"
EXPECTED = {
    ORIGINAL: "6f5e8fac9d8f1d06c5a06a3b3f67b1bce776418d977bf6ea80ca064c9fc5b96a",
    V24_RESULT: "22cbd6acb79fc5788afc4b1220cc9eaa19d0a987a2126a49eace67e89ce7921b",
    R1_RESULT: "10cfdfea0c20554d6a65bac99a009bad23fee9babcb62c80f11ed86ee8a96ea4",
    PREREG: "d10861eb320b205e98711fc1c4b51308fd58d51a13f0195db1b6a2cf6ae46094",
}


class ResourceCap(RuntimeError):
    pass


def fail(message: object) -> "None":
    raise RuntimeError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only V24R5 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only V24R5 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def qpath(path: Path) -> str:
    value = str(path.resolve())
    if '"' in value or "\n" in value:
        fail(("unsafe output path", value))
    return value


def run_singular(singular: str, script: Path, stdout: Path, stderr: Path,
                 timeout: int) -> str:
    try:
        completed = subprocess.run([singular, "-q", str(script)],
                                   cwd=script.parent, text=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, timeout=timeout)
    except subprocess.TimeoutExpired as error:
        stdout.write_text(error.stdout or "")
        stderr.write_text(error.stderr or "")
        raise ResourceCap((script.name, timeout)) from error
    stdout.write_text(completed.stdout)
    stderr.write_text(completed.stderr)
    if completed.returncode or completed.stderr or "K00_V24R5_FAIL=" in completed.stdout:
        fail(("exact direct lift/replay failure", script.name,
              completed.returncode, completed.stderr[-2000:],
              completed.stdout[-3000:]))
    return completed.stdout


def emit_cap(output: Path, tag: str, stage: str, script: Path) -> None:
    payload = {
        "status": "RESOURCE_CAP_NO_VERDICT",
        "registered_aws_lane": tag,
        "stage": stage,
        "script_sha256": digest(script),
        "scope": "NO_EXACT_Q_UNIT_IDENTITY_OR_CHART_VERDICT",
        "firewall": "NO_W_ZERO_NO_STRATUM_NO_JET_NO_ARC_NO_CLOSURE_NO_JC2",
    }
    (output / "RESULT.json").write_text(
        json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print("K00_V24R5=RESOURCE_CAP_NO_VERDICT")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    tag = require_aws()
    for path, wanted in EXPECTED.items():
        got = digest(path)
        if got != wanted:
            fail(("frozen input mismatch", str(path), got, wanted))
    r1 = json.loads(R1_RESULT.read_text())
    if r1.get("status") != "F65521_LOCALIZED_PRIOR_IDEAL_IS_UNIT_NO_MEMBERSHIP_CONCLUSION":
        fail("V24R1 dependency mismatch")
    original = ORIGINAL.read_text().splitlines()
    if len(original) != 11 or not original[0].startswith("ring R=65521,"):
        fail("frozen source shape mismatch")
    if not original[1].startswith("ideal P=") or not re.fullmatch(
            r"P=P,zinv\*k10_0\*\(.+\)-1;", original[2]):
        fail("frozen generator declarations mismatch")
    ring_q = original[0].replace("ring R=65521,", "ring R=0,", 1)
    if not ring_q.startswith("ring R=0,") or "65521" in ring_q:
        fail("exact-Q ring conversion failed")

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    coefficient_paths = [output / f"EXACT_DIRECT_CERT_{index:02d}.txt"
                         for index in range(1, 37)]
    first_script = output / "exact_q_direct_lift.sing"
    first_lines = [
        ring_q, original[1], original[2],
        'if (size(P)!=36) { print("K00_V24R5_FAIL=GENERATOR_CENSUS"); quit; }',
        "matrix U; matrix C=lift(P,ideal(1),U,\"slimgb\");",
        'if ((nrows(C)!=36)||(ncols(C)!=1)) { print("K00_V24R5_FAIL=LIFT_SHAPE"); quit; }',
        'if ((nrows(U)!=1)||(ncols(U)!=1)||(U!=matrix(ideal(1)))) { print("K00_V24R5_FAIL=NONIDENTITY_UNIT_MATRIX"); quit; }',
        "matrix RES=matrix(P)*C-matrix(ideal(1));",
        'if (RES!=0) { print("K00_V24R5_FAIL=DIRECT_IDENTITY"); quit; }',
        "int pick=0; int jj;",
        "for (jj=1;jj<=36;jj++) { if ((pick==0)&&(P[jj]!=0)&&(C[jj,1]!=0)) { pick=jj; } }",
        'if (pick==0) { print("K00_V24R5_FAIL=NO_NONZERO_MUTATION_ENTRY"); quit; }',
        "matrix CDROP=C; CDROP[pick,1]=0;",
        'if (matrix(P)*CDROP-matrix(ideal(1))==0) { print("K00_V24R5_FAIL=DROP_MUTATION"); quit; }',
        "matrix CADD=C; CADD[pick,1]=CADD[pick,1]+1;",
        'if (matrix(P)*CADD-matrix(ideal(1))==0) { print("K00_V24R5_FAIL=ADD_MUTATION"); quit; }',
    ]
    for index, path in enumerate(coefficient_paths, 1):
        first_lines.append(f'write("{qpath(path)}",C[{index},1]);')
    first_lines.extend([
        'print("K00_V24R5_DIRECT_IDENTITY_REPLAY=1");',
        'print("K00_V24R5_PRODUCER_MUTATIONS=1");',
        'print("K00_V24R5_PICK="+string(pick));',
        "quit;",
    ])
    first_script.write_text("\n".join(first_lines) + "\n")
    singular = shutil.which("Singular")
    if singular is None:
        fail("Singular missing")
    first_stdout = output / "exact_q_direct_lift.stdout"
    first_stderr = output / "exact_q_direct_lift.stderr"
    try:
        markers = run_singular(singular, first_script, first_stdout,
                               first_stderr, 21000)
    except ResourceCap:
        emit_cap(output, tag, "DIRECT_TARGET_LIFT", first_script)
        return
    if "K00_V24R5_DIRECT_IDENTITY_REPLAY=1" not in markers or \
            "K00_V24R5_PRODUCER_MUTATIONS=1" not in markers:
        fail("producer markers missing")
    match = re.search(r"K00_V24R5_PICK=(\d+)", markers)
    if match is None or not (1 <= int(match.group(1)) <= 36):
        fail("producer mutation index missing")
    pick = int(match.group(1))
    if not all(path.is_file() for path in coefficient_paths):
        fail("serialized direct-lift coefficient missing")

    second_script = output / "exact_q_direct_lift_replay.sing"
    second_lines = [ring_q, original[1], original[2],
                    'if (size(P)!=36) { print("K00_V24R5_FAIL=REPLAY_GENERATOR_CENSUS"); quit; }',
                    "matrix C[36][1];"]
    second_lines.extend(
        f"C[{index},1]={path.read_text().strip()};"
        for index, path in enumerate(coefficient_paths, 1))
    second_lines.extend([
        "matrix RES=matrix(P)*C-matrix(ideal(1));",
        'if (RES!=0) { print("K00_V24R5_FAIL=SERIALIZED_IDENTITY"); quit; }',
        f"matrix CDROP=C; CDROP[{pick},1]=0;",
        'if (matrix(P)*CDROP-matrix(ideal(1))==0) { print("K00_V24R5_FAIL=REPLAY_DROP_MUTATION"); quit; }',
        f"matrix CADD=C; CADD[{pick},1]=CADD[{pick},1]+1;",
        'if (matrix(P)*CADD-matrix(ideal(1))==0) { print("K00_V24R5_FAIL=REPLAY_ADD_MUTATION"); quit; }',
        'print("K00_V24R5_SERIALIZED_SECOND_PROCESS_REPLAY=1");',
        'print("K00_V24R5_SECOND_PROCESS_MUTATIONS=1");',
        "quit;",
    ])
    second_script.write_text("\n".join(second_lines) + "\n")
    second_stdout = output / "exact_q_direct_lift_replay.stdout"
    second_stderr = output / "exact_q_direct_lift_replay.stderr"
    try:
        replay_markers = run_singular(singular, second_script, second_stdout,
                                      second_stderr, 1800)
    except ResourceCap:
        emit_cap(output, tag, "SERIALIZED_SECOND_PROCESS_REPLAY", second_script)
        return
    if "K00_V24R5_SERIALIZED_SECOND_PROCESS_REPLAY=1" not in replay_markers or \
            "K00_V24R5_SECOND_PROCESS_MUTATIONS=1" not in replay_markers:
        fail("serialized replay markers missing")

    artifact_paths = [first_script, first_stdout, first_stderr,
                      second_script, second_stdout, second_stderr,
                      *coefficient_paths]
    payload = {
        "status": "PASS_EXACT_Q_DIRECT_UNIT_LIFT_REPLAYED_36_ENTRY_IDENTITY",
        "registered_aws_lane": tag,
        "field": "Q_exact",
        "algorithm": "lift(P,ideal(1),U,slimgb)_direct_target_not_full_liftstd",
        "generator_count": 36,
        "coefficient_count": 36,
        "unit_matrix_identity": True,
        "producer_exact_identity_replay": True,
        "serialized_second_process_exact_identity_replay": True,
        "drop_and_add_mutations_both_processes": True,
        "mutation_index": pick,
        "artifacts": {path.name: {"sha256": digest(path),
                                  "bytes": path.stat().st_size}
                      for path in artifact_paths},
        "input_sha256": {str(path.relative_to(HERE.parents[1])): digest(path)
                         for path in EXPECTED},
        "scope": "EXACT_Q_NORMALIZED_VALUATION_ONE_PREFIX_THROUGH_GRADE6_ON_D_K10_0_W",
        "firewall": "NO_W_ZERO_NO_GRADES7TO19_NO_FULL_JET_NO_ARC_NO_CLOSURE_NO_JC2",
    }
    (output / "RESULT.json").write_text(
        json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print("K00_V24R5=" + payload["status"])
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
