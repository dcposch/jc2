#!/usr/bin/env python3
"""AWS-only independent-specialization wrapper for quotient tuple B."""

from __future__ import annotations

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
DESIGN_B = ROOT / "xmodel/max12-812-order2-invariant-quotient-probe-tupleb-design-20260826.md"
EXPECTED_BASE = "9c3a8e049321d71e5b29b571624bcac6889f06e7317a78ef163b25941271609b"
EXPECTED_DESIGN_B = "1cdfc659280144eec05597331a4528240d01a894d30e77dc24909419f5541fe2"
CHARACTERISTIC = 65521
LOAD_VALUES = {
    "k10": 17,
    "k6": 19,
    "k2": 23,
}
TARGET_VALUES = {
    1: 0,
    2: 29,
    3: 0,
    4: 31,
    5: 0,
    6: 37,
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only tuple-B compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only tuple-B compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        fail(("specialization site count", old, text.count(old)))
    return text.replace(old, new)


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: compile_probe_tupleb.py OUTPUT_DIRECTORY")
    tag = require_aws()
    if digest(BASE) != EXPECTED_BASE or digest(DESIGN_B) != EXPECTED_DESIGN_B:
        fail("tuple-B frozen source mismatch")

    spec = importlib.util.spec_from_file_location("order2_quotient_probe_base", BASE)
    if spec is None or spec.loader is None:
        fail("cannot load frozen base compiler")
    base = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(base)
    base.LOADS = dict(LOAD_VALUES)
    base.TARGETS = dict(TARGET_VALUES)

    output = Path(sys.argv[1]).resolve()
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
    source = replace_once(source, "ring R=32003,", "ring R=65521,")
    source = replace_once(
        source,
        "ORDER2_QUOTIENT_LOADS=2,3,5,7,11,13",
        "ORDER2_QUOTIENT_LOADS=17,19,23,29,31,37",
    )
    source = replace_once(
        source,
        "ideal I=r1,r2-7,r3,r4-11,r5,r6-13;",
        "ideal I=r1,r2-29,r3,r4-31,r5,r6-37;",
    )
    new_input = output / "order2_invariant_quotient_p65521.sing"
    new_input.write_text(source)
    old_input.unlink()

    result_path = output / "result.json"
    payload = json.loads(result_path.read_text())
    payload.update(
        {
            "status": "PASS-ORDER2-INVARIANT-QUOTIENT-TUPLEB-COMPILER",
            "registered_aws_lane": tag,
            "characteristic": CHARACTERISTIC,
            "loads": [17, 19, 23, 29, 31, 37],
            "base_compiler_sha256": digest(BASE),
            "tupleb_design_sha256": digest(DESIGN_B),
            "input_sha256": digest(new_input),
            "scope": "NAVIGATION_CONTROL_ONLY_NO_GENUS_NO_SOURCE_ELIMINATION",
        }
    )
    result_path.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
