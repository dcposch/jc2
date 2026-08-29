#!/usr/bin/env python3
"""Compile the frozen rootwise client with collision-free Singular names."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import re
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V2 = ROOT / "cases/max12_812_order2_square_owner_lowcontact_c1_c2_v2_rootwise_20260826/compile_lowcontact_rootwise.py"
V2_FREEZE = ROOT / "cases/max12_812_order2_square_owner_lowcontact_c1_c2_v2_rootwise_20260826/FREEZE.sha256"
PINS = {
    V2: "cbeab15363b2d6743ec8c509ea724082058e0a33e3d9a315692eb227bb22e5ee",
    V2_FREEZE: "d7333dd0114e6c074bc534369a97bc800f0b81f0d1fcf1db455dd58b260dfc57",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_v2():
    spec = importlib.util.spec_from_file_location("square_rootwise_v2", V2)
    if spec is None or spec.loader is None:
        fail("cannot load frozen V2 compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def rename_segment(segment: str, prefix: str) -> str:
    # First repair the single analytic/source bridge typo.
    segment = segment.replace(f"{prefix}h", f"{prefix}ah")
    generic = (
        "sp", "AA", "EE", "BB", "kk", "Inv1", "Inv2", "Hshift",
        "Ls", "Az", "Ez", "Bz", "Num", "L0", "L02", "GL2",
        "R11", "P11", "C12", "E1z", "R12", "P12", "C13",
        "R13", "P13", "C14", "A0z", "E2z",
    )
    for name in generic:
        segment = re.sub(rf"\b{re.escape(name)}\b", f"{prefix}_{name}", segment)
    return segment


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    for source, expected in PINS.items():
        if digest(source) != expected:
            fail(("frozen V2 pin mismatch", str(source)))
    v2 = load_v2()
    tag = v2.require_aws()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    nested = output / "frozen_v2"
    saved = sys.argv
    try:
        sys.argv = [str(V2), str(nested), "--characteristic", str(args.characteristic)]
        v2.main()
    finally:
        sys.argv = saved
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    old = nested / f"square_lowcontact_rootwise_{label}.sing"
    text = old.read_text()
    c1_start = text.find("poly sp=p/2+sigma*ell1;")
    c2_ring = text.find(f"ring Rc2full={args.characteristic},")
    c2_start = text.find("poly sp=p/2+sigma*ell1+sigma^2*ell2;", c2_ring)
    if min(c1_start, c2_ring, c2_start) < 0 or not (c1_start < c2_ring < c2_start):
        fail(("analytic segment anchors invalid", c1_start, c2_ring, c2_start))
    c1 = rename_segment(text[c1_start:c2_ring], "c1")
    c2 = rename_segment(text[c2_start:], "c2")
    text = text[:c1_start] + c1 + text[c2_ring:c2_start] + c2
    for forbidden in ("c1h11_1", "c1h12_1", "c2h12_1", "c2h13_1", "c2h14_1"):
        if forbidden in text:
            fail(("unrepaired Laurent bridge name", forbidden))
    target = output / f"square_lowcontact_rootwise_v3_{label}.sing"
    target.write_text(text)
    payload = {
        "status": "PASS-SQUARE-LOWCONTACT-ROOTWISE-V3-COMPILER",
        "scope": "C1_C2_ROOTWISE_GENERIC_SQUARE_ONLY_NO_SQUARE_OR_ORDER2_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "v2_compiler_sha256": digest(V2),
        "v2_input_sha256": digest(old),
        "input_sha256": digest(target),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()

