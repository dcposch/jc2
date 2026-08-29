#!/usr/bin/env python3
"""Extract and independently replay the exact W-in-(Q1,Q3,Q4) identity."""

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
ROOT = HERE.parents[1]
QUADRICS = ROOT / "cases/max12_812_order2_u2_62_k00_weighted_first_stratum_v22_20260827/aws_r6b_r1_pass/output/UNLOADED_QUADRATIC_INITIALS.txt"
WITNESS = ROOT / "cases/max12_812_order2_u2_62_k00_grade7_newest_block_v23_20260827/aws_r6b_pass/output/GENERIC_RANK_WITNESS_MINOR.txt"
HARVEST = HERE / "aws_box02_r6r1_unit/output"
RESULT = HARVEST / "RESULT.json"
REPORT = HERE / "RESULT_V24R6R1_LEADING_BASE_DW.md"
CERTS = [HARVEST / f"LEADING_BASE_CERT_{index:02d}.txt"
         for index in range(1, 9)]
EXPECTED = {
    QUADRICS: "fd90f064ca43715c37fd7b02c99c842b0b21a6ecd7f5f2eeaf7b8645f95e62a2",
    WITNESS: "957181065328c7ef930c6c400272f45ab93a055ff1069ced7f3cca8b3c89bbde",
    RESULT: "b0a537864954b95f5c5893cee998e46b73f30b4a20443fee749297b0f18487ce",
    REPORT: "8da4f616bba29b03522458e4b0c1c4ff42301264c16c293553d1833307cbd747",
    CERTS[0]: "e570129629517e9dd8eb14ae9545fca95381298cd86f0bb60c084fceeb98315f",
    CERTS[1]: "9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa",
    CERTS[2]: "9e1a2829d8ab82ab0ab983af38e07a5c8530f4cc4ffa98bf016d68dea4fe55b0",
    CERTS[3]: "57ea69e9a5977dc17e7a2b37ac2feb05aa164b60851738c77fbae3a5e244f992",
    CERTS[4]: "9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa",
    CERTS[5]: "9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa",
    CERTS[6]: "9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa",
    CERTS[7]: "ee3aa64bb94a50845d5024cd4bd20202a4567aed5cd5328c0d97e9920775fc28",
}


def fail(message: object) -> "None":
    raise RuntimeError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def qpath(path: Path) -> str:
    value = str(path.resolve())
    if '"' in value or "\n" in value:
        fail(("unsafe path", value))
    return value


def run_singular(singular: str, script: Path, stdout: Path,
                 stderr: Path) -> str:
    completed = subprocess.run(
        [singular, "-q", str(script)], cwd=script.parent, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=600)
    stdout.write_text(completed.stdout)
    stderr.write_text(completed.stderr)
    if completed.returncode or completed.stderr or \
            re.search(r"(?m)^\s*\?", completed.stdout) or \
            "K00_V24R6R1_SYZ_FAIL=" in completed.stdout:
        fail(("exact syzygy replay failure", script.name,
              completed.returncode, completed.stderr[-1000:],
              completed.stdout[-2000:]))
    return completed.stdout


def assignments(path: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    for line in path.read_text().splitlines():
        if "=" not in line:
            fail(("malformed assignment", line[:100]))
        name, value = line.split("=", 1)
        result[name] = value
    if set(result) != {f"Q{index}" for index in range(1, 7)}:
        fail("quadratic census mismatch")
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    if platform.system() != "Linux" or \
            Path("/sys/class/dmi/id/sys_vendor").read_text().strip() != "Amazon EC2":
        fail("AWS-only exact syzygy replay refused host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("registered AWS lane missing")
    for path, wanted in EXPECTED.items():
        if digest(path) != wanted:
            fail(("frozen byte mismatch", str(path), digest(path), wanted))
    result = json.loads(RESULT.read_text())
    if result.get("status") != \
            "PASS_EXACT_LEADING_BASE_DW_UNIT_WITH_FULL_36_GENERATOR_EMBEDDED_IDENTITY":
        fail("producer status mismatch")
    values = [path.read_text().strip() for path in CERTS]
    if any(not value or ";" in value for value in values) or \
            [values[index] for index in (1, 4, 5, 6)] != ["0"] * 4 or \
            values[7] != "-1":
        fail("certificate support/profile mismatch")
    quadrics = assignments(QUADRICS)
    witness = "".join(WITNESS.read_text().split())
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    a_paths = {index: output / f"W_SYZYGY_A{index}.txt"
               for index in (1, 3, 4)}
    definitions = ["ring R=0,(x0,x1,x2,x3,x4,x5,z),dp;"]
    definitions.extend(
        f"poly Q{index}=({quadrics[f'Q{index}']});" for index in (1, 3, 4))
    definitions.extend([
        f"poly W=({witness});", f"poly C1=({values[0]});",
        f"poly C3=({values[2]});", f"poly C4=({values[3]});",
    ])
    derive = output / "derive_w_syzygy.sing"
    derive.write_text("\n".join(definitions + [
        'if ((subst(C1,z,0)!=0)||(subst(C3,z,0)!=0)||(subst(C4,z,0)!=0)) { print("K00_V24R6R1_SYZ_FAIL=NOT_Z_DIVISIBLE"); quit; }',
        "poly A1=C1/z; poly A3=C3/z; poly A4=C4/z;",
        'if ((C1-z*A1!=0)||(C3-z*A3!=0)||(C4-z*A4!=0)) { print("K00_V24R6R1_SYZ_FAIL=QUOTIENT_REPLAY"); quit; }',
        'if ((subst(A1,z,0)!=A1)||(subst(A3,z,0)!=A3)||(subst(A4,z,0)!=A4)) { print("K00_V24R6R1_SYZ_FAIL=QUOTIENT_HAS_Z"); quit; }',
        'if (A1*Q1+A3*Q3+A4*Q4-W!=0) { print("K00_V24R6R1_SYZ_FAIL=IDENTITY"); quit; }',
        'if (A3*Q3+A4*Q4-W==0) { print("K00_V24R6R1_SYZ_FAIL=DROP_MUTATION"); quit; }',
        'if ((A1+1)*Q1+A3*Q3+A4*Q4-W==0) { print("K00_V24R6R1_SYZ_FAIL=ADD_MUTATION"); quit; }',
        f'write("{qpath(a_paths[1])}",A1);',
        f'write("{qpath(a_paths[3])}",A3);',
        f'write("{qpath(a_paths[4])}",A4);',
        'print("K00_V24R6R1_W_SYZYGY_DERIVED=1"); quit;',
    ]) + "\n")
    singular = shutil.which("Singular")
    if singular is None:
        fail("Singular missing")
    derive_stdout = output / "derive_w_syzygy.stdout"
    derive_stderr = output / "derive_w_syzygy.stderr"
    markers = run_singular(singular, derive, derive_stdout, derive_stderr)
    if "K00_V24R6R1_W_SYZYGY_DERIVED=1" not in markers or \
            not all(path.is_file() for path in a_paths.values()):
        fail("derived syzygy custody missing")

    replay = output / "replay_w_syzygy.sing"
    replay.write_text("\n".join(definitions[:5] + [
        f"poly A1=({a_paths[1].read_text().strip()});",
        f"poly A3=({a_paths[3].read_text().strip()});",
        f"poly A4=({a_paths[4].read_text().strip()});",
        'if (A1*Q1+A3*Q3+A4*Q4-W!=0) { print("K00_V24R6R1_SYZ_FAIL=SERIALIZED_IDENTITY"); quit; }',
        'if (A3*Q3+A4*Q4-W==0) { print("K00_V24R6R1_SYZ_FAIL=SERIALIZED_DROP_MUTATION"); quit; }',
        'if ((A1+1)*Q1+A3*Q3+A4*Q4-W==0) { print("K00_V24R6R1_SYZ_FAIL=SERIALIZED_ADD_MUTATION"); quit; }',
        'print("K00_V24R6R1_W_SYZYGY_SECOND_PROCESS_REPLAY=1"); quit;',
    ]) + "\n")
    replay_stdout = output / "replay_w_syzygy.stdout"
    replay_stderr = output / "replay_w_syzygy.stderr"
    replay_markers = run_singular(
        singular, replay, replay_stdout, replay_stderr)
    if "K00_V24R6R1_W_SYZYGY_SECOND_PROCESS_REPLAY=1" not in replay_markers:
        fail("serialized syzygy replay marker missing")
    artifacts = [derive, derive_stdout, derive_stderr, *a_paths.values(),
                 replay, replay_stdout, replay_stderr]
    payload = {
        "status": "PASS_EXACT_Q_W_IN_IDEAL_Q1_Q3_Q4_REPLAYED",
        "registered_aws_lane": tag,
        "identity": "W=A1*Q1+A3*Q3+A4*Q4",
        "z_division_replayed": True,
        "fresh_serialized_process_replay": True,
        "drop_and_add_mutations": True,
        "artifacts": {path.name: {"sha256": digest(path),
                                    "bytes": path.stat().st_size}
                      for path in artifacts},
        "input_sha256": {str(path.relative_to(ROOT)): digest(path)
                         for path in EXPECTED},
        "scope": "GLOBAL_EXACT_Q_POLYNOMIAL_IDENTITY_FOR_FROZEN_V23_W_AND_V22_QUADRICS",
        "firewall": "NO_W_ZERO_COMPLEMENT_NO_FULL_JET_NO_ARC_NO_CLOSURE_NO_JC2",
    }
    (output / "RESULT.json").write_text(
        json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print("K00_V24R6R1_SYZYGY=" + payload["status"])
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
