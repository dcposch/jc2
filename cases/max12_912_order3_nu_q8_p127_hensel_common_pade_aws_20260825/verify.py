#!/usr/bin/env python3
"""Verify the frozen order16/order32 simultaneous Padé negative result."""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
RUN = HERE / "aws_box03_v1"
EXPECTED = {
    "common_pade.py": "acc005c798d966297bb3b1a5a9fa64f3e83d71a164f6c2b4d7806473f841e3b5",
    "run_remote.sh": "3f5ed92c22c8721e49fb474b8c5619bef14be1307af4696c60e584431ec299f8",
    "reconstruction.json": "63f7fbb230117bd68f1b7ad7af99cf079377428055910b67344efebfac5b44af",
    "result.out": "c373d3c38586abd2ec467aabeff083553e0ab99242475c171a01c1b926789088",
    "run.meta": "7b09e67f51342e7fa7a16e37bf0c8fd42556ef982f2e313760c0f5c5591cd0d0",
    "stderr.log": "79f478fd8a4f834b50d9f41dcab44db946c03a5feb6b95fc6bd5512957ae2083",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    for name in ("common_pade.py", "run_remote.sh"):
        got = digest(HERE / name)
        if got != EXPECTED[name]:
            raise AssertionError((name, got, EXPECTED[name]))
    for name in ("reconstruction.json", "result.out", "run.meta", "stderr.log"):
        got = digest(RUN / name)
        if got != EXPECTED[name]:
            raise AssertionError((name, got, EXPECTED[name]))

    payload = json.loads((RUN / "reconstruction.json").read_text())
    expected_subset = {
        "status": "PASS",
        "prime": 127,
        "sequence_count": 1330,
        "prefix_match": True,
        "synthetic_positive": True,
        "synthetic_negative": True,
        "fit16": None,
        "fit16_order32_holdout": [],
        "fit32": None,
        "selected": None,
        "selected_source": None,
        "order16_sha256": "d4a00d5f5922022fa6de0e2e32398e923128b297100a37e1b688f067b4bfc1cb",
        "order32_sha256": "a2934a4f02f8e5fad42154dcd69a80cb953db8666761945b9282f45326c92eaa",
    }
    for key, expected in expected_subset.items():
        if payload.get(key) != expected:
            raise AssertionError((key, payload.get(key), expected))

    output = (RUN / "result.out").read_text().splitlines()
    for line in (
        "Q8-P127-HENSEL-SIMULTANEOUS-COMMON-PADE",
        "status=PASS",
        "sequence_count=1330",
        "prefix_match=1",
        "fit16_total=None",
        "fit16_holdout_passes=0",
        "fit32_total=None",
        "selected=NONE",
        "output_sha256=" + EXPECTED["reconstruction.json"],
    ):
        if output.count(line) != 1:
            raise AssertionError((line, output.count(line)))
    meta = (RUN / "run.meta").read_text().splitlines()
    for line in (
        "rc=0",
        "endpoint=PASS",
        "stdout_sha256=" + EXPECTED["result.out"],
        "stderr_sha256=" + EXPECTED["stderr.log"],
        "reconstruction_sha256=" + EXPECTED["reconstruction.json"],
    ):
        if meta.count(line) != 1:
            raise AssertionError((line, meta.count(line)))
    print("PASS-Q8-P127-HENSEL-COMMON-PADE-ORDER16-32-CUSTODY")


if __name__ == "__main__":
    main()

