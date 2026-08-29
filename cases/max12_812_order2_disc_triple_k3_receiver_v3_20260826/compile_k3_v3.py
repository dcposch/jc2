#!/usr/bin/env python3
"""Immutable V3 wrapper for two remaining Singular syntax/API repairs."""

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
V2 = ROOT / "cases/max12_812_order2_disc_triple_k3_receiver_v2_20260826/compile_k3_v2.py"
V2_SHA = "6c179683986d2158dae7f5fa0ac11b4827ab2bb284e0a0edd7bdd7cb82a7f284"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only K3 V3 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only K3 V3 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_v2():
    if digest(V2) != V2_SHA:
        fail(("K3 V2 compiler hash mismatch", digest(V2), V2_SHA))
    spec = importlib.util.spec_from_file_location("disc_triple_k3_v2", V2)
    if spec is None or spec.loader is None:
        fail("cannot load frozen K3 V2 compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        fail(("delta anchor count", old, text.count(old)))
    return text.replace(old, new)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 32003), required=True)
    args = parser.parse_args()
    tag = require_aws()
    v2 = load_v2()
    v1 = v2.load_v1()
    for source, expected in v1.EXPECTED.items():
        actual = digest(source)
        if actual != expected:
            fail(("frozen dependency mismatch", str(source), actual, expected))
    tails = json.loads(v1.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != v1.EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    target = output / f"disc_triple_k3_v3_p{args.characteristic}.sing"
    v1.emit(target, args.characteristic, tails, v1.load_v1())
    text = target.read_text()
    text = replace_once(text, "poly dd=-3*b^2/16+rho*jd;", "poly dd=(-3/16)*b^2+rho*jd;")
    text = replace_once(
        text,
        "if (diff(Phi7,J)!=-rho^38/4) { target_typed=0; }",
        "if (diff(Phi7,J)!=(-1/4)*rho^38) { target_typed=0; }",
    )
    text = replace_once(
        text,
        "ideal corrections=ja,jd,jm,jx,jy,jkc,jkr,jns,jnt,jk;\nideal EK3=eliminate(IK3,corrections);",
        "poly correction_product=ja*jd*jm*jx*jy*jkc*jkr*jns*jnt*jk;\nideal EK3=eliminate(IK3,correction_product);",
    )
    text = replace_once(
        text,
        'print("DISC_TRIPLE_K3_ENDPOINT=PASS_CORRECTION_AWARE_K3_NECESSARY_GATE");',
        'print("DISC_TRIPLE_K3_V3_SYNTAX_API_REPAIR=1");\n'
        'print("DISC_TRIPLE_K3_ENDPOINT=PASS_CORRECTION_AWARE_K3_NECESSARY_GATE");',
    )
    target.write_text(text)
    payload = {
        "status": "PASS-DISC-TRIPLE-K3-V3-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "v2_compiler_sha256": digest(V2),
        "input_sha256": digest(target),
        "delta": "TERMINAL_RATIONAL_LITERAL_AND_ELIMINATE_POLY_API",
        "scope": "CORRECTION_AWARE_K3_NECESSARY_GATE_NO_LIFT_TAYLOR_OR_ORDER2_VERDICT",
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
