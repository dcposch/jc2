#!/usr/bin/env python3
"""AWS-only target-first ordering wrapper for frozen K00 g-open V2."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V2 = ROOT / "cases/max12_812_order2_u2_62_k00_closure_gopen_v2_20260827/compile_k00_gopen.py"
V2_SHA = "cf038f10fe97fe71bc11c903d03cd472c15a8274542acf60f8097f7c1e143577"
PROOF = HERE / "PREREGISTRATION.md"
PROOF_SHA = "b2f582f2f591ae09318bc9429fcff0db2855aa56e35f1d25b9fe957476e38966"
OLD_VARIABLES = "Lambda,C0,C1,C2,C3,C4,C5,C6,k10,k6,k2,mu2,mu4,mu6,Jdet"
NEW_VARIABLES = "mu2,mu4,mu6,Jdet,k10,k6,k2,Lambda,C0,C1,C2,C3,C4,C5,C6"
ORDER = "(lp(4),dp(3),wp(1,8,7,6,5,4,3,2))"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def main() -> None:
    if platform.system() != "Linux":
        fail("AWS-only target-first compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only target-first compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65519, 65521), default=65519)
    args = parser.parse_args()
    if digest(V2) != V2_SHA or digest(PROOF) != PROOF_SHA:
        fail("frozen V2/preregistration mismatch")
    output = args.output.resolve()
    if output.exists():
        fail("output already exists")
    baseline = output.with_name(output.name + ".gopen_baseline")
    completed = subprocess.run(
        [sys.executable, str(V2), str(baseline), "--characteristic", str(args.characteristic)],
        check=True,
        capture_output=True,
        text=True,
    )
    baseline_input = baseline / f"k00_gopen_char{args.characteristic}.sing"
    source = baseline_input.read_text()
    old_ring = f"ring R={args.characteristic},({OLD_VARIABLES}),dp;"
    new_ring = f"ring R={args.characteristic},({NEW_VARIABLES}),{ORDER};"
    if source.count(old_ring) != 1:
        fail("baseline ring declaration not found uniquely")
    source = source.replace(
        old_ring,
        new_ring + '\nprint("K00_ORDER=TARGETS_LOWERLOADS_FABER_GLOBAL");',
    )
    for code in range(81, 86):
        source = source.replace(f"quit({code});", f"exit({code});")
    if "quit(8" in source:
        fail("unsupported coded quit survived transformation")
    output.mkdir()
    singular = output / f"k00_targetfirst_char{args.characteristic}.sing"
    singular.write_text(source)
    base_result = json.loads((baseline / "compiler_result.json").read_text())
    payload = {
        **base_result,
        "status": "PASS-K00-TARGETFIRST-COMPILER",
        "registered_aws_lane": tag,
        "singular_input_sha256": digest(singular),
        "v2_compiler_sha256": digest(V2),
        "preregistration_sha256": digest(PROOF),
        "variable_order": NEW_VARIABLES.split(","),
        "monomial_order": ORDER,
        "all_loads_retained_as_polynomial_variables": True,
        "fail_fast_coded_exit_repair": True,
        "algorithm": "V2_GOPEN_WITH_AFFINE_TARGET_FIRST_GLOBAL_BLOCKS",
    }
    (output / "compiler_result.json").write_text(
        json.dumps(payload, sort_keys=True, indent=2) + "\n"
    )
    shutil.rmtree(baseline)
    print(completed.stdout.strip())
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
