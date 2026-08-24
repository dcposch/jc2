#!/usr/bin/env python3
"""Verify manifest and byte-replay both P4P1 honesty implementations."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
FULL_PYTHON = Path("/opt/homebrew/opt/python@3.14/bin/python3.14")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    for line in (HERE / "MANIFEST.sha256").read_text(encoding="ascii").splitlines():
        if not line.strip():
            continue
        expected, relative = line.split("  ", 1)
        actual = sha256(REPO / relative)
        if actual != expected:
            raise AssertionError(f"hash mismatch for {relative}: {actual} != {expected}")

    python = str(FULL_PYTHON if FULL_PYTHON.exists() else Path(sys.executable))
    producer_bytes = subprocess.run(
        [python, str(HERE / "p4p1_honesty.py")], check=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    ).stdout
    if producer_bytes != (HERE / "results.json").read_bytes():
        raise AssertionError("producer byte replay differs from results.json")

    replay_bytes = subprocess.run(
        [sys.executable, str(HERE / "replay.py"),
         "--input", str(HERE / "results.json")], check=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    ).stdout
    if replay_bytes != (HERE / "replay.json").read_bytes():
        raise AssertionError("independent byte replay differs from replay.json")

    producer = json.loads(producer_bytes)
    replay = json.loads(replay_bytes)
    provenance = json.loads((HERE / "provenance.json").read_text())
    assert producer["provenance"] == provenance
    assert producer["verdict"] == "ORIGIN-ONLY"
    assert replay["verdict"] == "PASS"
    assert replay["classification"] == producer["verdict"]
    assert replay["producer_canonical_claim_sha256"] == \
        producer["canonical_claim_sha256"]
    assert all(value == "PASS" for value in producer["gates"].values())
    assert all(value == "PASS" for value in replay["gates"].values())
    print("VERIFY PASS")
    print("  classification:", producer["verdict"])
    print("  producer:", producer["canonical_claim_sha256"])
    print("  independent:", replay["independent_core_sha256"])


if __name__ == "__main__":
    main()
