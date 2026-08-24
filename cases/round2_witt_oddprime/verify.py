#!/usr/bin/env python3
"""Verify hashes and byte-replay both AS3-MIN-W2 implementations."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    manifest = HERE / "MANIFEST.sha256"
    for line in manifest.read_text(encoding="ascii").splitlines():
        if not line.strip():
            continue
        expected, relative = line.split("  ", 1)
        actual = sha256(REPO / relative)
        if actual != expected:
            raise AssertionError(f"hash mismatch for {relative}: {actual} != {expected}")

    producer = subprocess.run(
        [sys.executable, str(HERE / "search.py")], check=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    ).stdout
    if producer != (HERE / "results.json").read_bytes():
        raise AssertionError("producer byte replay differs from results.json")

    reviewer = subprocess.run(
        [sys.executable, str(HERE / "replay.py"),
         "--input", str(HERE / "results.json")], check=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    ).stdout
    if reviewer != (HERE / "replay.json").read_bytes():
        raise AssertionError("independent byte replay differs from replay.json")

    results = json.loads(producer)
    replay = json.loads(reviewer)
    if results["verdict"] != "W2-SURVIVOR" or replay["verdict"] != "PASS":
        raise AssertionError("banked verdicts changed")
    if results["canonical_claim_sha256"] != replay["producer_canonical_claim_sha256"]:
        raise AssertionError("producer/reviewer canonical claim hashes differ")
    print("VERIFY PASS")
    print("  producer:", results["canonical_claim_sha256"])
    print("  independent:", replay["independent_core_sha256"])


if __name__ == "__main__":
    main()
