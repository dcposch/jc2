#!/usr/bin/env python3
"""Parentheses-only repair of the a9 recursive source census; AWS only."""

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
V2 = ROOT / "cases/max12_812_order2_square_owner_d1_a9_source_support_census_v2_recursive_grades_20260826/compile_a9_recursive.py"
V2_FREEZE = ROOT / "cases/max12_812_order2_square_owner_d1_a9_source_support_census_v2_recursive_grades_20260826/FREEZE.sha256"
V2_QUARANTINE = ROOT / "cases/max12_812_order2_square_owner_d1_a9_source_support_census_v2_recursive_grades_20260826/QUARANTINE.md"
PINS = {
    V2: "8a36f5edee279964f547a5ce0d2bbe0511e9cfaf6c5261cce6d115f4b3fcf46f",
    V2_FREEZE: "214fbbe32a483fde80563d4f0987796fae5750aecdea5e4075cdb97dfdfab2f0",
    V2_QUARANTINE: "43cf33ff4ef59b6f0341fa5941baf00e8f916191f1445fc3ec78e81f88aa9bcb",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only a9 V3 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only a9 V3 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_v2():
    spec = importlib.util.spec_from_file_location("a9_parentheses_v2", V2)
    if spec is None or spec.loader is None:
        fail("cannot import frozen V2 compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    for source, expected in PINS.items():
        actual = digest(source)
        if actual != expected:
            fail(("frozen V2 ancestry mismatch", str(source), actual, expected))

    v2 = load_v2()
    original_load_v1 = v2.load_v1

    def repaired_load_v1():
        module = original_load_v1()
        original_series = module.series

        def repaired_series(prefix: str, count: int) -> str:
            value = original_series(prefix, count)
            return f"({value})" if prefix in {"k0", "k60", "k20"} else value

        module.series = repaired_series
        return module

    v2.load_v1 = repaired_load_v1
    old_argv = sys.argv
    try:
        sys.argv = [str(V2), str(args.output), "--characteristic", str(args.characteristic)]
        v2.main()
    finally:
        sys.argv = old_argv

    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    old_target = args.output.resolve() / f"square_d1_a9_recursive_source_grades_{label}.sing"
    text = old_target.read_text()
    series = {
        "k10": "k0+sigma^1*k0_1+sigma^2*k0_2",
        "k6": "k60+sigma^1*k60_1+sigma^2*k60_2+sigma^3*k60_3+sigma^4*k60_4",
        "k2": "k20+sigma^1*k20_1+sigma^2*k20_2+sigma^3*k20_3+sigma^4*k20_4",
    }
    expected = {"k10": (2, 190), "k6": (6, 72), "k2": (10, 27)}
    counts: dict[str, int] = {}
    for name, (weight, count) in expected.items():
        pattern = f"({series[name]})*(sigma^2)^{weight}"
        actual = text.count(pattern)
        counts[name] = actual
        if actual != count:
            fail(("load distributivity count", name, actual, count, pattern))
        bare = f"*{series[name]}*(sigma^2)^{weight}"
        if bare in text:
            fail(("unparenthesized load survived", name))
    target = args.output.resolve() / f"square_d1_a9_recursive_source_grades_v3_{label}.sing"
    old_target.rename(target)
    payload = {
        "status": "PASS-A9-V3-PARENTHESIZED-LOAD-COMPILER",
        "scope": "GRADES_0_31_NAVIGATION_ONLY_NO_ROW_OR_ARC_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "input_sha256": digest(target),
        "load_weight_counts": counts,
    }
    (args.output.resolve() / "result.json").write_text(
        json.dumps(payload, sort_keys=True, indent=2) + "\n"
    )
    print("A9V3_LOAD_WEIGHT_DISTRIBUTIVITY_K10=190")
    print("A9V3_LOAD_WEIGHT_DISTRIBUTIVITY_K6=72")
    print("A9V3_LOAD_WEIGHT_DISTRIBUTIVITY_K2=27")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()

