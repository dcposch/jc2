#!/usr/bin/env python3
"""Compile frozen V7, then isolate r=1 and d=1 in distinct Singular inputs."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import platform
import subprocess
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V7 = ROOT / "cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_v7_20260826/compile_v7.py"
V7_FREEZE = ROOT / "cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_v7_20260826/FREEZE.sha256"
PINS = {
    V7: "85f0e9e45e5d1766b90ba30f34757ea012863830b39617dc0d687dca2b08283f",
    V7_FREEZE: "23be34624e3a39f2e7dac0baf58ce25a9c9186b4f982b1209959f91faef23bc4",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only r1/d1 V8 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only r1/d1 V8 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    for source, expected in PINS.items():
        actual = digest(source)
        if actual != expected:
            fail(("frozen V7 pin mismatch", str(source), actual, expected))

    output = args.output.resolve()
    if output.exists():
        fail("V8 output already exists")
    scratch = output.parent / (output.name + "_frozen_v7")
    subprocess.run(
        [sys.executable, str(V7), str(scratch), "--characteristic", str(args.characteristic)],
        check=True,
        env=os.environ.copy(),
    )
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    v7_input = scratch / f"square_r1_d1_ac_v7_{label}.sing"
    source_text = v7_input.read_text()
    anchor = "ring Rd1="
    if source_text.count(anchor) != 1:
        fail(("V7 split anchor missing or nonunique", source_text.count(anchor)))
    r1_prefix, d1_suffix = source_text.split(anchor, 1)
    r1_text = r1_prefix.rstrip() + "\nquit;\n"
    d1_text = anchor + d1_suffix

    if r1_text.count('LIB "primdec.lib";') != 1:
        fail(("unexpected r1 primdec count", r1_text.count('LIB "primdec.lib";')))
    if d1_text.count('LIB "primdec.lib";') != 0:
        fail("primdec leaked into isolated d1 process")
    r1_required = (
        "R1_SOURCE_HASHES=PASS",
        "R1_ENDPOINT=PASS_R1_LEADING_SECTION_ZERO_ON_DPK",
    )
    d1_required = (
        "D1AC_SOURCE_HASHES=PASS",
        "D1AC_SYMBOLIC_SHIFT_G16_THREE_MODULES=",
        "D1AC_ENDPOINT=PASS_SYMBOLIC_D1_UNIQUE_AC_DOUBLE_POLE_GATE",
        "R1_D1_AC_PACKAGE_ENDPOINT=PASS",
    )
    if not all(token in r1_text for token in r1_required):
        fail("r1 split lost a required marker")
    if any(token in d1_text for token in r1_required):
        fail("r1 markers leaked into d1 split")
    if not all(token in d1_text for token in d1_required):
        fail("d1 split lost a required marker")

    output.mkdir(parents=True)
    r1_target = output / f"square_r1_v8_{label}.sing"
    d1_target = output / f"square_d1_ac_v8_{label}.sing"
    r1_target.write_text(r1_text)
    d1_target.write_text(d1_text)
    payload = {
        "status": "PASS-R1-D1-AC-V8-SPLIT-COMPILER",
        "scope": "PROCESS_ISOLATION_ONLY_R1_AND_D1_UNIQUE_AC_NO_SQUARE_OR_ORDER2_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "v7_compiler_sha256": digest(V7),
        "v7_input_sha256": digest(v7_input),
        "split_anchor_count": source_text.count(anchor),
        "r1_primdec_count": r1_text.count('LIB "primdec.lib";'),
        "d1_primdec_count": d1_text.count('LIB "primdec.lib";'),
        "r1_input_sha256": digest(r1_target),
        "d1_input_sha256": digest(d1_target),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
