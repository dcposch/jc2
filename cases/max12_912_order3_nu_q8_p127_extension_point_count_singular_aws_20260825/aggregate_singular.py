#!/usr/bin/env python3
"""Fail-closed aggregate for the independent Singular F_(127^2) census."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


GENERATOR_SHA256 = "9b4333f6beac564aa40e53e3e88c91fe67465a5bb3c477669532faadf5978266"
RUNNER_SHA256 = "fd4bbbcefa6abd97ff62e60e8c21c5fd7399fcaaed5a9f32743ea03843f5ad73"
CANDIDATE_SHA256 = "9061726295086f58f74f3751b2f7c2d59c5cb86de5e53ecd636687fd54daa7ce"
EXPECTED_TOTALS = (16174, 16168, 6)
RECORD = re.compile(
    r"^RECORD\|index=(\d+)\|total=(\d+)\|smooth=(\d+)\|singular=(\d+)$"
)
BAD = re.compile(
    r"error occurred|not defined|wrong type|parse error|"
    r"SINGULAR_COUNT_MISMATCH|FAILURE",
    re.IGNORECASE,
)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def meta_values(path: Path) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for line in path.read_text().splitlines():
        if "=" in line and not re.match(r"^[0-9a-f]{64}  ", line):
            key, value = line.split("=", 1)
            result.setdefault(key, []).append(value)
    return result


def pinned_hash_present(text: str, digest: str, suffix: str) -> bool:
    return any(line.startswith(digest + "  ") and line.endswith(suffix) for line in text.splitlines())


def audit_lane(directory: Path) -> dict:
    required = ("input.sing", "run.meta", "singular.stdout", "singular.stderr")
    for name in required:
        if not (directory / name).is_file():
            raise SystemExit(f"missing {name}: {directory}")
    meta_text = (directory / "run.meta").read_text()
    meta = meta_values(directory / "run.meta")
    if meta.get("mode") != ["shard"]:
        raise SystemExit(f"mode mismatch: {directory}")
    if meta.get("rc") != ["0"]:
        raise SystemExit(f"Singular rc mismatch: {directory}")
    if not pinned_hash_present(meta_text, GENERATOR_SHA256, "generate_singular.py"):
        raise SystemExit(f"generator pin mismatch: {directory}")
    if not pinned_hash_present(meta_text, RUNNER_SHA256, "run_remote.sh"):
        raise SystemExit(f"runner pin mismatch: {directory}")
    if not pinned_hash_present(meta_text, CANDIDATE_SHA256, "interpolation_candidate.json"):
        raise SystemExit(f"candidate pin mismatch: {directory}")
    for name in ("input.sing", "singular.stdout", "singular.stderr"):
        digest = sha256(directory / name)
        if not pinned_hash_present(meta_text, digest, name):
            raise SystemExit(f"{name} hash missing/mismatch: {directory}")

    stdout = (directory / "singular.stdout").read_text()
    stderr = (directory / "singular.stderr").read_text()
    if BAD.search(stdout) or BAD.search(stderr):
        raise SystemExit(f"error token: {directory}")
    if stdout.splitlines().count("SINGULAR_FQ2_SHARD_PASS") != 1:
        raise SystemExit(f"terminal marker mismatch: {directory}")
    if "Exit status: 0" not in stderr:
        raise SystemExit(f"time exit status missing: {directory}")

    start = int(meta["start"][0])
    stop = int(meta["stop"][0])
    rows = []
    for line in stdout.splitlines():
        match = RECORD.match(line)
        if match:
            rows.append(tuple(map(int, match.groups())))
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
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("--prefix", default="q8_p127_fq2_singular_full_r6a_v1_i")
    args = parser.parse_args()
    lanes = sorted(path for path in args.root.glob(args.prefix + "*") if path.is_dir())
    if len(lanes) != 16:
        raise SystemExit(f"expected 16 lanes, found {len(lanes)}")
    audits = [audit_lane(path) for path in lanes]
    if [(row["start"], row["stop"]) for row in audits] != [
        (i * 16129 // 16, (i + 1) * 16129 // 16) for i in range(16)
    ]:
        raise SystemExit("partition mismatch")
    totals = (
        sum(row["total"] for row in audits),
        sum(row["smooth"] for row in audits),
        sum(row["singular"] for row in audits),
    )
    if totals != EXPECTED_TOTALS:
        raise SystemExit(f"aggregate mismatch: {totals}")
    result = {
        "status": "PASS",
        "scope": "independent Singular 4.3.2 cross-engine F_127^2 census",
        "candidate_sha256": CANDIDATE_SHA256,
        "generator_sha256": GENERATOR_SHA256,
        "runner_sha256": RUNNER_SHA256,
        "field_order": 16129,
        "field_modulus": "a^2-a+3",
        "lane_count": len(audits),
        "w_count": sum(row["record_count"] for row in audits),
        "rational_affine_point_count": totals[0],
        "smooth_rational_affine_point_count": totals[1],
        "singular_rational_affine_point_count": totals[2],
        "p1_rational_point_count": 16130,
        "smooth_count_exceeds_p1": totals[1] > 16130,
        "lanes": audits,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

