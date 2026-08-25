#!/usr/bin/env python3
"""Audit the two harvested breadth shards and freeze exact lane custody."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent
BOX02 = tuple(w for w in range(1, 43) if w not in (25, 39))
BOX03 = tuple(w for w in range(43, 84) if w != 56)
ALL = tuple(sorted(BOX02 + BOX03))
FIRST68 = tuple(w for w in range(1, 72) if w not in (25, 39, 56))
SOURCES = {
    "run_one": "0318b213599d158588a12947bdaf69ab89b7a5a5b473c432ba349d3bd67683b2",
    "generator": "6b33f1c6ca57422fc229441059402b3f1908420023aeb6a2095eb3aa1545b2af",
    "parent": "4d075593a3e4e6566cb68a0fc6accc1cd6cb38e7539ed1829c2558b7e6d4bd2d",
    "samples": "0790e9f8bb6b545e742ca9e723c29b9a8dc0268a93dedd91c2f2a7b48f48f231",
    "candidate": "9061726295086f58f74f3751b2f7c2d59c5cb86de5e53ecd636687fd54daa7ce",
    "compiler": "22b0cdc446d1e486d08757df5a3fff83b0506a492f16b9b2cf238966eb947545",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def integer_field(text: str, key: str) -> int:
    match = re.search(rf"(?m)^{re.escape(key)}=(\d+)$", text)
    if not match:
        raise RuntimeError(("missing integer field", key))
    return int(match.group(1))


def audit_lane(root: Path, w: int) -> dict:
    tag = f"q8_p127_breadth_w{w:03d}_order8_v1"
    lane = root / tag
    if not lane.is_dir():
        raise RuntimeError(("missing lane", lane))
    meta = (lane / "run.meta").read_text()
    required_meta = [
        f"tag={tag}", f"base_w={w}", "hensel_order=8", "generator_rc=0",
        "rc=0", "endpoint=PASS", "coefficient_marker_count=7",
    ]
    for marker in required_meta:
        if meta.splitlines().count(marker) != 1:
            raise RuntimeError((lane, "meta marker", marker))
    for source in SOURCES.values():
        if meta.count("source_sha256=" + source + "  ") != 1:
            raise RuntimeError((lane, "source hash", source))
    if (lane / "generator.stderr").read_bytes():
        raise RuntimeError((lane, "generator stderr"))
    output = (lane / "result.out").read_text()
    exact = [
        "Q8-P127-HENSEL-BASE", "base_fail=0", "H0_degree=190",
        "gcd_detJ_H0_degree=0", "gcd_Hv_H0_degree=0",
        "Q8-P127-BREADTH-MOVING-BASIS", f"base_w={w}",
        "moving_dimension=0", "moving_vdim=1520",
        "Q8-P127-BREADTH-ORDER8", "order=8", "final_fail=0",
    ]
    for marker in exact:
        if output.splitlines().count(marker) != 1:
            raise RuntimeError((lane, "output marker", marker))
    if [integer_field(output, "coefficient_order")]:
        coefficient_orders = [
            int(value) for value in re.findall(r"(?m)^coefficient_order=(\d+)$", output)
        ]
        if coefficient_orders != list(range(1, 8)):
            raise RuntimeError((lane, coefficient_orders))
    if "\n   ?" in "\n" + output:
        raise RuntimeError((lane, "Singular diagnostic"))
    stderr = (lane / "stderr.log").read_text()
    if "Exit status: 0" not in stderr or "Swaps: 0" not in stderr:
        raise RuntimeError((lane, "resource endpoint"))
    rss_match = re.search(r"(?m)^\s*Maximum resident set size \(kbytes\): (\d+)$", stderr)
    if not rss_match:
        raise RuntimeError((lane, "missing RSS"))
    rss = int(rss_match.group(1))
    input_sha = digest(lane / "input.sing")
    if f"input_sha256={input_sha}" not in meta:
        raise RuntimeError((lane, "input custody"))
    stdout_sha = digest(lane / "result.out")
    stderr_sha = digest(lane / "stderr.log")
    if "stdout_sha256=" + stdout_sha not in meta or "stderr_sha256=" + stderr_sha not in meta:
        raise RuntimeError((lane, "output custody"))
    return {
        "w": w,
        "tag": tag,
        "input_sha256": input_sha,
        "stdout_sha256": stdout_sha,
        "stderr_sha256": stderr_sha,
        "meta_sha256": digest(lane / "run.meta"),
        "input_bytes": (lane / "input.sing").stat().st_size,
        "maximum_rss_kib": rss,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    records = []
    for directory, values in (("aws_box02_v1", BOX02), ("aws_box03_v1", BOX03)):
        root = HERE / directory
        dispatch = (root / "dispatch.meta").read_text()
        if f"lane_count={len(values)}" not in dispatch or "order=8" not in dispatch:
            raise RuntimeError((root, "dispatch endpoint"))
        records.extend(audit_lane(root, w) for w in values)
    passed = tuple(record["w"] for record in records)
    if tuple(sorted(passed)) != ALL or len(set(passed)) != 80:
        raise RuntimeError("passing fibre set")
    if not set(FIRST68).issubset(passed):
        raise RuntimeError("first 68 subset")
    contact_sum_first68 = 123 + (64 - 1) + len(FIRST68) * (8 - 1)
    if contact_sum_first68 != 662 or contact_sum_first68 <= 658:
        raise RuntimeError("strict contact inequality")
    payload = {
        "status": "PASS",
        "prime": 127,
        "order": 8,
        "pass_count": 80,
        "fail_count": 0,
        "all_passing_w": list(ALL),
        "lexicographically_first_68": list(FIRST68),
        "baseline_good_fibre_count": 123,
        "separate_w25_order": 64,
        "contact_sum_first_68": contact_sum_first68,
        "sparse_degree_bound": 658,
        "strict_component_inequality": "662>658",
        "maximum_rss_kib": max(record["maximum_rss_kib"] for record in records),
        "source_sha256": SOURCES,
        "lanes": records,
        "scope": (
            "exact mod-127 truncated source contact; component conclusion uses the "
            "separately frozen sparse contact-to-component lemma"
        ),
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print("Q8-P127-BREADTH-ORDER8-SUMMARY")
    print("status=PASS")
    print("pass_count=80")
    print("fail_count=0")
    print("first68_contact_sum=662")
    print("sparse_bound=658")
    print("output_sha256=" + digest(args.output))


if __name__ == "__main__":
    main()
