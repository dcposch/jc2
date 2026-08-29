#!/usr/bin/env python3
"""Deployment-only V2 repair for the affine-Faber A half-weight client."""

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
V1_PATH = ROOT / "cases/max12_812_order2_affine_faber_a_halfweight_tau90_20260826/compile_halfweight_tau90.py"
V1_SHA = "fd54ab39fb775af9f9d217525cb19125b5db03878569d613e78c8ea970f65862"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only A half-weight V2 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only A half-weight V2 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_v1():
    if digest(V1_PATH) != V1_SHA:
        fail("frozen V1 compiler mismatch")
    spec = importlib.util.spec_from_file_location("a_halfweight_tau90_v1", V1_PATH)
    if spec is None or spec.loader is None:
        fail("cannot load frozen V1 compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


REPAIRS = {
    "(-cb^2/32+ce/4)": "((-1/32)*cb^2+(1/4)*ce)",
    "(7*cb^4/2048-3*cb^2*ce/128+ce^2/32)": "((7/2048)*cb^4-(3/128)*cb^2*ce+(1/32)*ce^2)",
    "(-cb^3/64+cb*ce/8)": "(-(1/64)*cb^3+(1/8)*cb*ce)",
    "(3*cb^2/32+3*ce/4)": "((3/32)*cb^2+(3/4)*ce)",
    "(5*cb^2/32-ce/4)": "((5/32)*cb^2-(1/4)*ce)",
    "(21*cb^2/32-3*ce/4)": "((21/32)*cb^2-(3/4)*ce)",
    "(-5*cb^3/16+3*cb*ce/4)": "(-(5/16)*cb^3+(3/4)*cb*ce)",
    "(195*cb^4/2048-45*cb^2*ce/128+5*ce^2/32)": "((195/2048)*cb^4-(45/128)*cb^2*ce+(5/32)*ce^2)",
    "(5*BB^2/32-EE/4)": "((5/32)*BB^2-(1/4)*EE)",
    "(21*BB^2/32-3*EE/4)": "((21/32)*BB^2-(3/4)*EE)",
    "(-5*BB^3/16+3*BB*EE/4)": "(-(5/16)*BB^3+(3/4)*BB*EE)",
    "(195*BB^4/2048-45*BB^2*EE/128+5*EE^2/32)": "((195/2048)*BB^4-(45/128)*BB^2*EE+(5/32)*EE^2)",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    v1 = load_v1()
    base = v1.load_base()
    if digest(base.TAILS) != base.EXPECTED_TAILS:
        fail("frozen tails mismatch")
    tails = json.loads(base.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != base.EXPECTED_CANONICAL:
        fail("canonical tails mismatch")

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    target = output / f"affine_faber_a_halfweight_tau90_v2_{label}.sing"
    v1.emit(target, args.characteristic, base, tails)
    text = target.read_text()
    for old, new in REPAIRS.items():
        count = text.count(old)
        if count != 1:
            fail(("V2 rational-spelling repair anchor count", old, count))
        text = text.replace(old, new)
    if any(old in text for old in REPAIRS):
        fail("V2 rational-spelling repair incomplete")
    target.write_text(text)

    payload = {
        "status": "PASS-A-HALFWEIGHT-TAU90-V2-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "v1_compiler_sha256": digest(V1_PATH),
        "base_sha256": digest(v1.BASE_PATH),
        "tails_sha256": digest(base.TAILS),
        "repair_count": len(REPAIRS),
        "scope": "DEPLOYMENT_REPAIR_ONLY_DELAYED_LOAD_REPEATED_A_Q15_OVER_2_THROUGH_TAU90",
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
