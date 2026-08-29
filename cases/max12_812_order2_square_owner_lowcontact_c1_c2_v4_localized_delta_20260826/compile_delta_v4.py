#!/usr/bin/env python3
"""Compile localized c2 delta printer from frozen rootwise V3."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V3 = ROOT / "cases/max12_812_order2_square_owner_lowcontact_c1_c2_v3_namespaced_20260826/compile_rootwise_v3.py"
V3_FREEZE = ROOT / "cases/max12_812_order2_square_owner_lowcontact_c1_c2_v3_namespaced_20260826/FREEZE.sha256"
PINS = {
    V3: "2fa4cabd58fd22560cd0b084cf2272a13fa522a126cb8bc6a2f60e28eb097ad5",
    V3_FREEZE: "676f97810cc0c758ba864efe3463c2798f3c5d8f3fd70d57dee8ba0fb7457b57",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only c2 delta compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only c2 delta compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_v3():
    spec = importlib.util.spec_from_file_location("square_rootwise_v3", V3)
    if spec is None or spec.loader is None:
        fail("cannot load frozen rootwise V3 compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    tag = require_aws()
    for source, expected in PINS.items():
        if digest(source) != expected:
            fail(("frozen V3 pin mismatch", str(source)))
    v3 = load_v3()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    nested = output / "frozen_v3"
    saved = sys.argv
    try:
        sys.argv = [str(V3), str(nested), "--characteristic", "0"]
        v3.main()
    finally:
        sys.argv = saved
    old_input = nested / "square_lowcontact_rootwise_v3_q.sing"
    text = old_input.read_text()
    old = "int c2root=(reduce(c2_C14-(3/8)*c2_E2z^2,c2G)==0);"
    new = """poly c2DeltaRaw=reduce(c2_C14-(3/8)*c2_E2z^2,c2G);
ideal c2Gpk=std(sat(c2G,ideal(p*k0)));
int c2proper=(reduce(1,c2Gpk)!=0);
poly c2DeltaLocal=reduce(c2_C14-(3/8)*c2_E2z^2,c2Gpk);
int c2raw=(c2DeltaRaw==0); int c2root=(c2DeltaLocal==0);
print("SQUARE_ROOTWISE_C2_RAW_MEMBERSHIP="+string(c2raw));
print("SQUARE_ROOTWISE_C2_LOCALIZED_IDEAL_PROPER="+string(c2proper));
print("SQUARE_ROOTWISE_C2_RAW_DELTA_BEGIN"); print(c2DeltaRaw); print("SQUARE_ROOTWISE_C2_RAW_DELTA_END");
print("SQUARE_ROOTWISE_C2_LOCALIZED_DELTA_BEGIN"); print(c2DeltaLocal); print("SQUARE_ROOTWISE_C2_LOCALIZED_DELTA_END");"""
    if text.count(old) != 1:
        fail(("V3 c2 root anchor missing or nonunique", text.count(old)))
    text = text.replace(old, new)
    target = output / "square_lowcontact_c2_localized_delta_v4_q.sing"
    target.write_text(text)
    payload = {
        "status": "PASS-SQUARE-LOWCONTACT-C2-LOCALIZED-DELTA-V4-COMPILER",
        "scope": "DIAGNOSTIC_D_P_K0_ONLY_NO_SQUARE_OR_ORDER2_VERDICT",
        "registered_aws_lane": tag,
        "v3_compiler_sha256": digest(V3),
        "v3_input_sha256": digest(old_input),
        "input_sha256": digest(target),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()

