#!/usr/bin/env python3.14
"""Verify D-STATE-GATE manifest and byte-replay both implementations."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    for line in (HERE / "MANIFEST.sha256").read_text(encoding="ascii").splitlines():
        if not line:
            continue
        expected, relative = line.split("  ", 1)
        actual = digest(REPO / relative)
        if actual != expected:
            raise AssertionError(f"hash mismatch {relative}: {actual} != {expected}")

    producer = subprocess.run(
        [sys.executable, str(HERE / "dstate_gate.py")], check=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    ).stdout
    if producer != (HERE / "results.json").read_bytes():
        raise AssertionError("producer byte replay differs")

    reviewer = subprocess.run(
        [sys.executable, str(HERE / "replay.py"),
         "--input", str(HERE / "results.json")], check=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    ).stdout
    if reviewer != (HERE / "replay.json").read_bytes():
        raise AssertionError("independent replay differs")

    result = json.loads(producer)
    replay = json.loads(reviewer)
    if result["verdict"] != "NO-TYPED-STATIONARITY":
        raise AssertionError("producer verdict changed")
    if replay["review_verdict"] != "PASS":
        raise AssertionError("independent verdict changed")
    if replay["producer_core_sha256"] != result["core_sha256"]:
        raise AssertionError("producer/reviewer core hash mismatch")
    print("VERIFY PASS")
    print("  producer:", result["core_sha256"])
    print("  independent:", replay["core_sha256"])


if __name__ == "__main__":
    main()
