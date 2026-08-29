#!/usr/bin/env python3
"""Compile the two F48-null fixed slices from the frozen witness client."""

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
PARENT = ROOT / "cases/max12_812_order2_affine_faber_a_h16_q6_a4_g48_witness_controls_20260826/compile_g48_witness.py"
PARENT_SHA = "9ab43c2eddbc2f175e13796094cd6b67c9d1756a200138c8b4d71827c1535ed0"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only odd-null compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only odd-null compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_parent():
    if digest(PARENT) != PARENT_SHA:
        fail("frozen witness compiler mismatch")
    spec = importlib.util.spec_from_file_location("g48_witness", PARENT)
    if spec is None or spec.loader is None:
        fail("cannot import frozen witness compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def replace_once(source: str, old: str, new: str) -> str:
    if source.count(old) != 1:
        fail({"replacement_count": source.count(old), "old": old})
    return source.replace(old, new)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    parent = load_parent()
    base = parent.load_base()
    if digest(base.TAILS) != base.EXPECTED_TAILS:
        fail("frozen tails mismatch")
    tails = json.loads(base.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != base.EXPECTED_CANONICAL:
        fail("canonical tails mismatch")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    replacements = {
        "x": (("s^2*(16+s^4*d64)", "s^2*(20+s^4*d64)"),
              ("s^2*(7+s^4*d24)", "s^2*(8+s^4*d24)"),
              ("s^2*(-11/16+s^4*dm4)", "s^2*(-23/32+s^4*dm4)")),
        "y": (("s^2*(-74+s^4*d64)", "s^2*(-70+s^4*d64)"),
              ("s^2*(-61/2+s^4*d24)", "s^2*(-59/2+s^4*d24)"),
              ("s^2*(181/64+s^4*dm4)", "s^2*(179/64+s^4*dm4)")),
    }
    for chart in ("x", "y"):
        temporary = output / f"temporary_{chart}_{label}.sing"
        parent.emit(temporary, args.characteristic, chart, base, tails)
        source = temporary.read_text()
        for old, new in replacements[chart]:
            source = replace_once(source, old, new)
        source = source.replace("A_G48W_", "A_G48N_")
        source = source.replace(
            f"FIXED_RATIONAL_{chart.upper()}_CHART_GRADE48_POSITIVE_CONTROL_ONLY",
            f"FIXED_RATIONAL_{chart.upper()}_CHART_GRADE48_ODD_NULL_CONTROL_ONLY",
        )
        target = output / f"affine_faber_a_g48n_{chart}_{label}.sing"
        target.write_text(source)
        temporary.unlink()
        generated = target.read_text()
        for old, _ in replacements[chart]:
            if old in generated:
                fail(("old slice coefficient survived", chart, old))
        if generated.count(f"A_G48N_{chart.upper()}_DONE=1") != 1:
            fail(("endpoint count", chart))
    payload = {
        "status": "PASS-A-H16-G48-ODD-NULL-V5-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "parent_sha256": digest(PARENT),
        "base_sha256": digest(parent.BASE),
        "tails_sha256": digest(base.TAILS),
        "slices": ["x:F48=0", "y:F48=0"],
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()

