#!/usr/bin/env python3
"""Compile the syntax-safe V13 tracked-basis repair, on AWS only."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V11 = ROOT / "cases/max12_812_order2_u2_62_k00_local_membership_v11_20260827/compile_local_membership.py"
V11_PREREG = ROOT / "cases/max12_812_order2_u2_62_k00_local_membership_v11_20260827/PREREGISTRATION.md"
V11_VALIDATOR = ROOT / "cases/max12_812_order2_u2_62_k00_local_membership_v11_20260827/validate_local_membership.py"
V12 = ROOT / "cases/max12_812_order2_u2_62_k00_local_membership_v12_20260827/compile_local_membership_v12.py"
PREREG = HERE / "PREREGISTRATION.md"
EXPECTED = {
    V11: "44c3ace63a1b5875934be5db92b4f4866ed5ceddb72d3d5c26a4796239ff5f8d",
    V11_PREREG: "4d4c9569aec1f8776c9099da9f86d0fa998ee6aace409c870efa66c9410afd6f",
    V11_VALIDATOR: "6e842224f451dffb7b2aa2316628f86b80185ba71d09abba74ede0d90ba8c586",
    V12: "93d01386a625db8e1762580f9b33442fc7ee6056fcd681d7de11e9ee21cf314b",
    PREREG: "7d19ca1667494a1d0d98357fbfd7a2bfb56667657a82551a41bd55665766425a",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only V13 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only V13 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        fail(("cannot load frozen module", str(path)))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    tag = require_aws()
    for path, expected in EXPECTED.items():
        if expected == "TO_BE_FROZEN" or digest(path) != expected:
            fail(("frozen source mismatch", str(path), digest(path), expected))

    v11 = load_module(V11, "k00_v11_frozen_for_v13")
    for path, expected in v11.EXPECTED.items():
        if digest(path) != expected:
            fail(("V11 transitive source mismatch", str(path), digest(path), expected))
    tails = json.loads(v11.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != v11.EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    singular = output / "k00_local_membership_v13_q.sing"
    v11.emit(singular, tails, v11.load_v7())
    text = singular.read_text()
    directive = "option(redSB);\n"
    if text.count(directive) != 1:
        fail(("expected unique V11 redSB directive", text.count(directive)))
    text = text.replace(
        directive,
        "// V13 tracked liftstd basis; optional post-reduction is absent.\n",
        1,
    )
    singular.write_text(text)
    if text.count(directive) != 0:
        fail("executable redSB directive survived V13 repair")

    result = {
        "status": "PASS-K00-LOCAL-MEMBERSHIP-V13-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": 0,
        "order": "ds",
        "repair": "REMOVE_UNIQUE_REDSB_EXACT_DIRECTIVE",
        "v11_compiler_sha256": digest(V11),
        "v11_preregistration_sha256": digest(V11_PREREG),
        "v11_validator_sha256": digest(V11_VALIDATOR),
        "v12_failed_compiler_sha256": digest(V12),
        "preregistration_sha256": digest(PREREG),
        "input_sha256": digest(singular),
        "scope": "NORMALIZED_K00_LOCAL_RING_UNLOADED_MEMBERSHIP_ONLY",
    }
    (output / "compiler_result.json").write_text(
        json.dumps(result, sort_keys=True, indent=2) + "\n"
    )
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
