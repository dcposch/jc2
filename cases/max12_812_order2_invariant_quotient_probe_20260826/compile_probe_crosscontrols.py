#!/usr/bin/env python3
"""AWS-only shared compiler for invariant-quotient prime/load controls."""

from __future__ import annotations

import argparse
from contextlib import redirect_stdout
from hashlib import sha256
import importlib.util
import io
import json
import os
from pathlib import Path
import platform
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BASE = HERE / "compile_probe.py"
DESIGN = ROOT / "xmodel/max12-812-order2-invariant-quotient-crosscontrols-design-20260826.md"
EXPECTED_BASE = "9c3a8e049321d71e5b29b571624bcac6889f06e7317a78ef163b25941271609b"
EXPECTED_DESIGN = "8ea031adee174f7ecceb8195d36386f6264c2ab4cb156fb09b4e3ef7ed525e71"
CONFIGS = {
    "A65521": (65521, (2, 3, 5, 7, 11, 13)),
    "B32003": (32003, (17, 19, 23, 29, 31, 37)),
    "C32003": (32003, (41, 43, 47, 53, 59, 61)),
    "C65521": (65521, (41, 43, 47, 53, 59, 61)),
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only cross-control compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only cross-control compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        fail(("specialization site count", old, text.count(old)))
    return text.replace(old, new)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--config", choices=tuple(CONFIGS), required=True)
    args = parser.parse_args()
    tag = require_aws()
    if digest(BASE) != EXPECTED_BASE or digest(DESIGN) != EXPECTED_DESIGN:
        fail("cross-control frozen source mismatch")
    characteristic, values = CONFIGS[args.config]
    k10, k6, k2, mu2, mu4, mu6 = values

    spec = importlib.util.spec_from_file_location("order2_quotient_probe_base", BASE)
    if spec is None or spec.loader is None:
        fail("cannot load frozen base compiler")
    base = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(base)
    base.LOADS = {"k10": k10, "k6": k6, "k2": k2}
    base.TARGETS = {1: 0, 2: mu2, 3: 0, 4: mu4, 5: 0, 6: mu6}

    output = args.output.resolve()
    saved_argv = sys.argv
    capture = io.StringIO()
    try:
        sys.argv = [str(BASE), str(output)]
        with redirect_stdout(capture):
            base.main()
    finally:
        sys.argv = saved_argv

    old_input = output / "order2_invariant_quotient_p32003.sing"
    source = old_input.read_text()
    source = replace_once(source, "ring R=32003,", f"ring R={characteristic},")
    source = replace_once(
        source,
        "ORDER2_QUOTIENT_LOADS=2,3,5,7,11,13",
        "ORDER2_QUOTIENT_LOADS=" + ",".join(str(value) for value in values),
    )
    source = replace_once(
        source,
        "ideal I=r1,r2-7,r3,r4-11,r5,r6-13;",
        f"ideal I=r1,r2-{mu2},r3,r4-{mu4},r5,r6-{mu6};",
    )
    new_input = output / f"order2_invariant_quotient_p{characteristic}.sing"
    new_input.write_text(source)
    if new_input != old_input:
        old_input.unlink()

    result_path = output / "result.json"
    payload = json.loads(result_path.read_text())
    payload.update(
        {
            "status": "PASS-ORDER2-INVARIANT-QUOTIENT-CROSSCONTROL-COMPILER",
            "registered_aws_lane": tag,
            "config": args.config,
            "characteristic": characteristic,
            "loads": list(values),
            "base_compiler_sha256": digest(BASE),
            "crosscontrol_design_sha256": digest(DESIGN),
            "input_sha256": digest(new_input),
            "scope": "MODULAR_NAVIGATION_CONTROL_ONLY_NO_GENUS_NO_SOURCE_ELIMINATION",
        }
    )
    result_path.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
