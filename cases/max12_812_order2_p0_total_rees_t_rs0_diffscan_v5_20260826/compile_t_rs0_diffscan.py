#!/usr/bin/env python3
"""AWS-only derivative-support accelerator for frozen streaming T-rs-0."""

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
STREAM = ROOT / "cases/max12_812_order2_p0_total_rees_t_rs0_stream_v2_20260826/compile_t_rs0_stream.py"
STREAM_SHA256 = "5b176dfd0747f3736bc4519077877f4d877b5b726b9701e1b9dcaf56e059a112"
PREREG = HERE / "PREREGISTRATION.md"
CHARACTERISTICS = (0, 32003, 65521, 1000033)
SOURCE_COEFFICIENT_TOTAL_DEGREE_BOUND = 8


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if (
        platform.system() != "Linux"
        or not vendor.is_file()
        or vendor.read_text().strip() != "Amazon EC2"
        or not tag.startswith("max12_812_order2_p0_total_rees_t_rs0_diffscan_v5_")
    ):
        fail("diffscan V5 compiler requires a registered AWS EC2 lane")
    return tag


def load_stream():
    actual = digest(STREAM)
    if actual != STREAM_SHA256:
        fail(("streaming compiler hash mismatch", actual, STREAM_SHA256))
    spec = importlib.util.spec_from_file_location("t_rs0_stream_frozen", STREAM)
    if spec is None or spec.loader is None:
        fail("cannot import frozen streaming compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def derivative_bound(tails: dict[str, list[list[object]]]) -> tuple[int, int, int]:
    max_factors = 0
    max_loads = 0
    exponent_bound = 0
    for row in range(1, 8):
        for raw_monomial, _ in tails[str(row)]:
            monomial = [int(value) for value in raw_monomial]
            if len(monomial) != 10:
                fail(("tail monomial length", row, monomial))
            factors = sum(monomial[:7])
            loads = sum(monomial[7:])
            max_factors = max(max_factors, factors)
            max_loads = max(max_loads, loads)
            exponent_bound = max(
                exponent_bound,
                SOURCE_COEFFICIENT_TOTAL_DEGREE_BOUND * factors + loads,
            )
    if max_factors != 9 or max_loads != 1 or exponent_bound != 72:
        fail(("derivative safety census drift", max_factors, max_loads, exponent_bound))
    return max_factors, max_loads, exponent_bound


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=CHARACTERISTICS, required=True)
    args = parser.parse_args()
    tag = require_aws()
    stream = load_stream()
    old = stream.load_old()
    for source, expected in old.EXPECTED.items():
        actual = digest(source)
        if actual != expected:
            fail(("transitive frozen source mismatch", str(source), actual, expected))
    tails = json.loads(old.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != old.EXPECTED_CANONICAL_TAILS:
        fail("canonical tails mismatch")
    max_factors, max_loads, exponent_bound = derivative_bound(tails)
    if args.characteristic and args.characteristic <= exponent_bound:
        fail(("characteristic does not license derivative support test", args.characteristic, exponent_bound))

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    temporary = output / f"t_rs0_stream_source_{label}.sing"
    manifest = stream.emit(temporary, args.characteristic, tails, old)
    source_text = temporary.read_text()
    text = source_text
    names = manifest["candidate_manifest"] + manifest["inactive_custody"]
    replacement_count = 0
    for name in names:
        before = f"if (subst(TPhi,{name},0)-TPhi!=0) {{ dep_{name}=1; }}"
        after = f"if (diff(TPhi,{name})!=0) {{ dep_{name}=1; }}"
        count = text.count(before)
        if count != 7:
            fail(("old dependency statement count", name, count, 7))
        text = text.replace(before, after)
        if text.count(after) != 7:
            fail(("new dependency statement count", name, text.count(after), 7))
        replacement_count += count
    surviving = [
        name for name in names
        if f"if (subst(TPhi,{name},0)-TPhi!=0) {{ dep_{name}=1; }}" in text
    ]
    if replacement_count != 581 or surviving or text.count("if (diff(TPhi,") != 581:
        fail(("dependency rewrite census", replacement_count, surviving, text.count("if (diff(TPhi,")))
    if source_text == text:
        fail("derivative rewrite made no change")
    singular = output / f"t_rs0_diffscan_{label}.sing"
    singular.write_text(text)
    temporary.unlink()

    result = {
        "status": "PASS-T-RS0-DISCOVERY-COMPILER",
        "scope": "SOURCE_FIDELITY_DISCOVERY_MOD_SIGMA13_ONLY_NO_REES_CHART_OR_ORDER2_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "input_sha256": digest(singular),
        "tails_sha256": digest(old.TAILS),
        "canonical_tails_sha256": old.EXPECTED_CANONICAL_TAILS,
        "reviewed_compiler_sha256": stream.OLD_SHA256,
        "implementation_review_sha256": stream.REVIEW_SHA256,
        "streaming_compiler_sha256": STREAM_SHA256,
        "preregistration_sha256": digest(PREREG),
        "accelerator": "DIFFSCAN_V5",
        "dependency_scan": "FORMAL_DERIVATIVE_WITH_CHARACTERISTIC_BOUND",
        "dependency_replacement_count": replacement_count,
        "max_tail_coefficient_factors": max_factors,
        "max_tail_load_factors": max_loads,
        "tested_atom_exponent_bound": exponent_bound,
        **manifest,
    }
    (output / "result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
