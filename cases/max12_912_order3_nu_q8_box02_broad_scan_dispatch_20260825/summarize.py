#!/usr/bin/env python3
"""Summarize deterministic fixed-fibre msolve lanes without CAS."""

from __future__ import annotations

import argparse
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import re


def fields(path: Path) -> dict[str, str]:
    out = {}
    for line in path.read_text().splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            out[key] = value
    return out


def classify(mode: str, result: str) -> str:
    lines = [line.strip() for line in result.splitlines() if line.strip()]
    if mode == "drl" and "[1]:" in lines:
        return "empty"
    if mode == "fglm" and lines == ["[-1]:"]:
        return "empty"
    return "nonempty"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lanes", type=Path, required=True)
    parser.add_argument("--prime", type=int, required=True)
    parser.add_argument("--start", type=int, required=True)
    parser.add_argument("--stop", type=int, required=True)
    parser.add_argument("--mode", choices=("drl", "fglm"), required=True)
    args = parser.parse_args()

    by_w = {}
    for lane in sorted(args.lanes.iterdir() if args.lanes.exists() else []):
        if not lane.is_dir() or not (lane / "run.meta").is_file():
            continue
        meta = fields(lane / "run.meta")
        try:
            w_value = int(meta["w_value"])
        except (KeyError, ValueError):
            continue
        record = {
            "tag": meta.get("tag", lane.name),
            "rc": int(meta.get("rc", "-999")),
            "input_sha256": meta.get("input_sha256"),
            "result_sha256": meta.get("result_sha256"),
            "stderr_sha256": meta.get("stderr_sha256"),
        }
        if record["rc"] != 0 or not (lane / "result.out").is_file():
            record["class"] = "failed"
        else:
            result = (lane / "result.out").read_text()
            record["class"] = classify(args.mode, result)
            record["result_bytes"] = len(result.encode())
            stderr = (lane / "stderr.log").read_text()
            match = re.search(r"Dimension of quotient:\s*(\d+)", stderr)
            if match:
                record["quotient_degree"] = int(match.group(1))
        by_w[w_value] = record

    for w_value in range(args.start, args.stop + 1):
        by_w.setdefault(w_value, {"class": "missing"})
    histogram = Counter(record["class"] for record in by_w.values())
    degrees = Counter(
        str(record["quotient_degree"])
        for record in by_w.values()
        if "quotient_degree" in record
    )
    payload = {
        "case": "max12_912_order3_nu_q8_box02_broad_scan_dispatch_20260825",
        "prime": args.prime,
        "w_range": [args.start, args.stop],
        "mode": args.mode,
        "histogram": dict(sorted(histogram.items())),
        "quotient_degree_histogram": dict(sorted(degrees.items())),
        "per_w": {str(key): value for key, value in sorted(by_w.items())},
        "scope": (
            "fixed finite-field localized fibres only; empty includes bad or "
            "affine-localization specialization; no generic/char0/component/trajectory claim"
        ),
    }
    canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["payload_sha256_without_this_field"] = sha256(canonical.encode()).hexdigest()
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

