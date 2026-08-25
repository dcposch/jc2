#!/usr/bin/env python3
"""Fail-closed aggregate for reusable extension-field Singular shards."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


RECORD = re.compile(
    r"^RECORD\|index=(\d+)\|total=(\d+)\|smooth=(\d+)\|singular=(\d+)$"
)
BAD = re.compile(
    r"error occurred|not defined|wrong type|parse error|FAILURE", re.IGNORECASE
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def meta_values(path: Path) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for line in path.read_text().splitlines():
        if "=" in line and not re.match(r"^[0-9a-f]{64}  ", line):
            key, value = line.split("=", 1)
            result.setdefault(key, []).append(value)
    return result


def pinned_hash_present(text: str, digest: str, suffix: str) -> bool:
    return any(
        line.startswith(digest + "  ") and line.endswith(suffix)
        for line in text.splitlines()
    )


def audit_lane(
    directory: Path,
    generator_sha256: str,
    runner_sha256: str,
    curve_sha256: str,
    modulus: str,
) -> dict:
    required = ("input.sing", "run.meta", "singular.stdout", "singular.stderr")
    for name in required:
        if not (directory / name).is_file():
            raise SystemExit(f"missing {name}: {directory}")
    meta_text = (directory / "run.meta").read_text()
    meta = meta_values(directory / "run.meta")
    for key, expected in (("rc", "0"), ("curve_sha256", curve_sha256), ("modulus", modulus)):
        if meta.get(key) != [expected]:
            raise SystemExit(f"{key} mismatch: {directory}")
    if not pinned_hash_present(meta_text, generator_sha256, "generate_singular.py"):
        raise SystemExit(f"generator pin mismatch: {directory}")
    if not pinned_hash_present(meta_text, runner_sha256, "run_remote.sh"):
        raise SystemExit(f"runner pin mismatch: {directory}")
    if not any(line.startswith(curve_sha256 + "  ") for line in meta_text.splitlines()):
        raise SystemExit(f"curve pin mismatch: {directory}")
    for name in ("input.sing", "singular.stdout", "singular.stderr"):
        digest = sha256(directory / name)
        if not pinned_hash_present(meta_text, digest, name):
            raise SystemExit(f"{name} hash mismatch: {directory}")

    stdout = (directory / "singular.stdout").read_text()
    stderr = (directory / "singular.stderr").read_text()
    if BAD.search(stdout) or BAD.search(stderr):
        raise SystemExit(f"error token: {directory}")
    if stdout.splitlines().count("EXTENSION_SMOOTH_POINT_ORACLE_SHARD_PASS") != 1:
        raise SystemExit(f"terminal marker mismatch: {directory}")
    if "Exit status: 0" not in stderr:
        raise SystemExit(f"time exit status missing: {directory}")

    start = int(meta["start"][0])
    stop = int(meta["stop"][0])
    rows = [tuple(map(int, match.groups())) for line in stdout.splitlines() if (match := RECORD.match(line))]
    if [row[0] for row in rows] != list(range(start, stop)):
        raise SystemExit(f"index coverage mismatch: {directory}")
    for index, total, smooth, singular in rows:
        if total != smooth + singular:
            raise SystemExit(f"count identity mismatch at {index}: {directory}")
    return {
        "tag": directory.name,
        "start": start,
        "stop": stop,
        "record_count": len(rows),
        "total": sum(row[1] for row in rows),
        "smooth": sum(row[2] for row in rows),
        "singular": sum(row[3] for row in rows),
        "input_sha256": sha256(directory / "input.sing"),
        "stdout_sha256": sha256(directory / "singular.stdout"),
        "stderr_sha256": sha256(directory / "singular.stderr"),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True, type=Path)
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("--prefix", required=True)
    parser.add_argument("--curve", required=True, type=Path)
    parser.add_argument("--curve-sha256", required=True)
    parser.add_argument("--modulus", required=True)
    parser.add_argument("--lanes", required=True, type=int)
    parser.add_argument("--generator-sha256", required=True)
    parser.add_argument("--runner-sha256", required=True)
    args = parser.parse_args()

    generator = args.repo / "cases/reusable_plane_curve_extension_smooth_point_oracle_aws_20260825/generate_singular.py"
    runner = args.repo / "cases/reusable_plane_curve_extension_smooth_point_oracle_aws_20260825/run_remote.sh"
    for path, expected in ((generator, args.generator_sha256), (runner, args.runner_sha256), (args.curve, args.curve_sha256)):
        if sha256(path) != expected:
            raise SystemExit(f"source pin mismatch: {path}")
    data = json.loads(args.curve.read_text())
    p = int(data["prime"])
    degree = len(args.modulus.split(",")) - 1
    field_order = p**degree
    lanes = sorted(path for path in args.root.glob(args.prefix + "*") if path.is_dir())
    if len(lanes) != args.lanes:
        raise SystemExit(f"expected {args.lanes} lanes, found {len(lanes)}")
    audits = [
        audit_lane(path, args.generator_sha256, args.runner_sha256, args.curve_sha256, args.modulus)
        for path in lanes
    ]
    expected_intervals = [
        (index * field_order // args.lanes, (index + 1) * field_order // args.lanes)
        for index in range(args.lanes)
    ]
    if [(row["start"], row["stop"]) for row in audits] != expected_intervals:
        raise SystemExit("partition mismatch")
    totals = {
        key: sum(row[key] for row in audits) for key in ("total", "smooth", "singular")
    }
    if totals["total"] != totals["smooth"] + totals["singular"]:
        raise SystemExit("aggregate count identity mismatch")
    result = {
        "status": "PASS",
        "scope": "standalone sparse plane-curve extension-field smooth-point census",
        "curve_sha256": args.curve_sha256,
        "generator_sha256": args.generator_sha256,
        "runner_sha256": args.runner_sha256,
        "prime": p,
        "extension_degree": degree,
        "field_order": field_order,
        "modulus": args.modulus,
        "lane_count": args.lanes,
        "w_count": sum(row["record_count"] for row in audits),
        "rational_affine_point_count": totals["total"],
        "smooth_rational_affine_point_count": totals["smooth"],
        "singular_rational_affine_point_count": totals["singular"],
        "p1_rational_point_count": field_order + 1,
        "smooth_count_exceeds_p1": totals["smooth"] > field_order + 1,
        "lanes": audits,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

