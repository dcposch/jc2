#!/usr/bin/env python3
"""Nonmutating retry of the moving-p source-row addendum.

V3 failed closed before emitting its modified script because its wrapper
searched for the shortened `APROL` endpoint while the frozen owner-v2
emitter uses `APROLONG`.  This retry changes only that wrapper anchor.
"""

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
V3 = ROOT / "cases/max12_812_order2_square_a_prolongation_owner_v3_ptangent_20260826/compile_square_a_ptangent.py"
V3_FREEZE = ROOT / "cases/max12_812_order2_square_a_prolongation_owner_v3_ptangent_20260826/FREEZE.sha256"
EXPECTED = {
    V3: "322f20ae93c98fe6373cf36e2c5f359646a4de44ea14188c38a4f8b0b3df6488",
    V3_FREEZE: "2bcf3b7f060632e69080101c9c4b2ecb84dd89c56e01db356cc03e0f68281537",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only square p-tangent V4 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only square p-tangent V4 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_v3():
    spec = importlib.util.spec_from_file_location("square_aprol_ptangent_v3", V3)
    if spec is None or spec.loader is None:
        fail("cannot load frozen V3 wrapper")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    for source, expected in EXPECTED.items():
        actual = digest(source)
        if actual != expected:
            fail(("frozen V3 dependency mismatch", str(source), actual, expected))
    v3 = load_v3()
    for source, expected in v3.EXPECTED.items():
        actual = digest(source)
        if actual != expected:
            fail(("frozen owner dependency mismatch", str(source), actual, expected))
    owner = v3.load_owner()
    for source, expected in owner.EXPECTED_STATIC.items():
        actual = digest(source)
        if actual != expected:
            fail(("frozen transitive dependency mismatch", str(source), actual, expected))
    tails = json.loads(owner.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != owner.EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    target = output / f"square_a_ptangent_v4_{label}.sing"
    owner.source_coefficients = v3.moving_source_coefficients
    owner.emit(target, args.characteristic, tails)
    text = target.read_text()
    ring_old = ",mu2,mu4,mu6,J,t,z),dp;"
    ring_new = ",mu2,mu4,mu6,J,ell,t,z),dp;"
    if text.count(ring_old) != 1:
        fail("owner ring anchor missing or nonunique")
    text = text.replace(ring_old, ring_new)
    analytic_start = text.find("poly ss=p/2;")
    endpoint = text.find('print("SQUARE_APROLONG_ENDPOINT=PASS_EXACT_SOURCE_G14_G15_A_ZERO_GATE");')
    if analytic_start < 0 or endpoint < 0 or endpoint <= analytic_start:
        fail("corrected owner analytic/end anchor missing")
    text = text[:analytic_start] + "\n".join(v3.analytic_block()) + "\n"
    target.write_text(text)
    payload = {
        "status": "PASS-SQUARE-A-PTANGENT-V4-COMPILER",
        "scope": "MOVING_P_ADDENDUM_TO_HIGH_CONTACT_CONE_ONLY_NO_FAN_OR_ORDER2_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "v3_compiler_sha256": digest(V3),
        "input_sha256": digest(target),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
