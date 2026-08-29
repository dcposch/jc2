#!/usr/bin/env python3
"""Compile the immutable V12 tracked-basis repair, on registered AWS only."""

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
PREREG = HERE / "PREREGISTRATION.md"
EXPECTED = {
    V11: "44c3ace63a1b5875934be5db92b4f4866ed5ceddb72d3d5c26a4796239ff5f8d",
    V11_PREREG: "4d4c9569aec1f8776c9099da9f86d0fa998ee6aace409c870efa66c9410afd6f",
    V11_VALIDATOR: "6e842224f451dffb7b2aa2316628f86b80185ba71d09abba74ede0d90ba8c586",
    PREREG: "b2067c08be15beea3cc89bc2a51728b4c0cfb214f8535dff7afcbb425c148335",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only V12 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only V12 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_v11():
    spec = importlib.util.spec_from_file_location("k00_v11_frozen", V11)
    if spec is None or spec.loader is None:
        fail("cannot load frozen V11 compiler")
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

    v11 = load_v11()
    for path, expected in v11.EXPECTED.items():
        if digest(path) != expected:
            fail(("V11 transitive source mismatch", str(path), digest(path), expected))
    tails = json.loads(v11.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != v11.EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    singular = output / "k00_local_membership_v12_q.sing"
    v7 = v11.load_v7()
    v11.emit(singular, tails, v7)
    text = singular.read_text()
    needle = "option(redSB);\n"
    if text.count(needle) != 1:
        fail(("expected unique V11 redSB directive", text.count(needle)))
    text = text.replace(
        needle,
        "// V12 tracked liftstd basis: option(redSB) deliberately absent.\n",
        1,
    )
    singular.write_text(text)
    if "option(redSB)" in text:
        fail("redSB directive survived V12 repair")

    result = {
        "status": "PASS-K00-LOCAL-MEMBERSHIP-V12-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": 0,
        "order": "ds",
        "repair": "REMOVE_UNIQUE_REDSB_BEFORE_TRACKED_LIFTSTD",
        "v11_compiler_sha256": digest(V11),
        "v11_preregistration_sha256": digest(V11_PREREG),
        "v11_validator_sha256": digest(V11_VALIDATOR),
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
