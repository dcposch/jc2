#!/usr/bin/env python3
"""Immutable V2 wrapper repairing one Singular rational literal."""

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
V1 = ROOT / "cases/max12_812_order2_disc_triple_k3_receiver_20260826/compile_k3.py"
V1_SHA = "0878fda0e55c55b588e18d6a51b32aa07b52a7a5776ccce3fc3ad347172ba173"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only K3 V2 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only K3 V2 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_v1():
    if digest(V1) != V1_SHA:
        fail(("K3 V1 compiler hash mismatch", digest(V1), V1_SHA))
    spec = importlib.util.spec_from_file_location("disc_triple_k3_v1", V1)
    if spec is None or spec.loader is None:
        fail("cannot load frozen K3 V1 compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 32003), required=True)
    args = parser.parse_args()
    tag = require_aws()
    v1 = load_v1()
    for source, expected in v1.EXPECTED.items():
        actual = digest(source)
        if actual != expected:
            fail(("frozen V1 dependency mismatch", str(source), actual, expected))
    tails = json.loads(v1.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != v1.EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    target = output / f"disc_triple_k3_v2_p{args.characteristic}.sing"
    v1.emit(target, args.characteristic, tails, v1.load_v1())
    text = target.read_text()
    old = "poly dd=-3*b^2/16+rho*jd;"
    new = "poly dd=(-3/16)*b^2+rho*jd;"
    if text.count(old) != 1:
        fail(("V1 delta anchor count", text.count(old)))
    text = text.replace(old, new)
    text = text.replace(
        'print("DISC_TRIPLE_K3_ENDPOINT=PASS_CORRECTION_AWARE_K3_NECESSARY_GATE");',
        'print("DISC_TRIPLE_K3_V2_RATIONAL_LITERAL_REPAIR=1");\n'
        'print("DISC_TRIPLE_K3_ENDPOINT=PASS_CORRECTION_AWARE_K3_NECESSARY_GATE");',
    )
    target.write_text(text)
    payload = {
        "status": "PASS-DISC-TRIPLE-K3-V2-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "v1_compiler_sha256": digest(V1),
        "input_sha256": digest(target),
        "delta": "SINGULAR_RATIONAL_LITERAL_ONLY",
        "scope": "CORRECTION_AWARE_K3_NECESSARY_GATE_NO_LIFT_TAYLOR_OR_ORDER2_VERDICT",
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
