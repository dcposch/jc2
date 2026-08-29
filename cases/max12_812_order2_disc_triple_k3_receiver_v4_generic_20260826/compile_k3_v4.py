#!/usr/bin/env python3
"""Compile the generic D(b*t) coefficient-field K3 control."""

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
V3 = ROOT / "cases/max12_812_order2_disc_triple_k3_receiver_v3_20260826/compile_k3_v3.py"
V3_SHA = "9a78c4e6f62993a477edac3798e97ef36e11e85e19d2e042e130fd990d259fc4"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only K3 V4 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only K3 V4 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_module(path: Path, expected: str, name: str):
    if digest(path) != expected:
        fail(("compiler hash mismatch", str(path), digest(path), expected))
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        fail(("cannot load compiler", str(path)))
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
    v3 = load_module(V3, V3_SHA, "disc_triple_k3_v3")
    v2 = v3.load_v2()
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
    target = output / f"disc_triple_k3_v4_generic_p{args.characteristic}.sing"
    v1.emit(target, args.characteristic, tails, v1.load_v1())
    text = target.read_text()
    old_ring = (
        f"ring R={args.characteristic},"
        "(rho,b,t,C,S,ja,jd,jm,jx,jy,jkc,jkr,jns,jnt,jk,k6,k2,mu2,mu4,mu6,J),dp;"
    )
    new_ring = (
        f"ring R=({args.characteristic},b,t,C,S),"
        "(rho,ja,jd,jm,jx,jy,jkc,jkr,jns,jnt,jk,k6,k2,mu2,mu4,mu6,J),dp;"
    )
    text = replace_once(text, old_ring, new_ring)
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
        "EK3=sat(EK3,ideal(b)); EK3=sat(EK3,ideal(t)); EK3=std(EK3);",
        "EK3=std(EK3);",
    )
    text = replace_once(
        text,
        'print("DISC_TRIPLE_K3_ENDPOINT=PASS_CORRECTION_AWARE_K3_NECESSARY_GATE");',
        'print("DISC_TRIPLE_K3_V4_GENERIC_FIELD=1");\n'
        'print("DISC_TRIPLE_K3_ENDPOINT=PASS_CORRECTION_AWARE_K3_NECESSARY_GATE");',
    )
    target.write_text(text)
    payload = {
        "status": "PASS-DISC-TRIPLE-K3-V4-GENERIC-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "v3_compiler_sha256": digest(V3),
        "input_sha256": digest(target),
        "scope": "GENERIC_D_BT_K3_NECESSARY_GATE_NO_PARAMETER_DIVISORS_LIFT_TAYLOR_OR_ORDER2_VERDICT",
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
