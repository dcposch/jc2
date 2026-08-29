#!/usr/bin/env python3
"""Fail-closed validator for the symbolic K00 quadratic replay."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("stdout", type=Path)
    parser.add_argument("result", type=Path)
    parser.add_argument("quadratics", type=Path)
    args = parser.parse_args()
    lines = [line.strip() for line in args.stdout.read_text().splitlines()]
    required = [
        "K00_QUADRATIC_SOURCE_HASHES=PASS",
        "K00_QUADRATIC_CONSTANT_ZERO=PASS",
        "K00_QUADRATIC_LINEAR_ZERO=PASS",
        "K00_QUADRATIC_SYMBOLIC_C6=PASS",
        "K00_QUADRATIC_Q5_SYZYGY=PASS",
        "K00_QUADRATIC_Q6_ZERO=PASS",
        "K00_QUADRATIC_Q7_SYZYGY=PASS",
        "K00_QUADRATIC_ENDPOINT=PASS_REPLAY_ONLY",
    ]
    for marker in required:
        if sum(line == marker for line in lines) != 1:
            raise RuntimeError(("missing or nonunique marker", marker))
    result = json.loads(args.result.read_text())
    if result.get("status") != "PASS-K00-SYMBOLIC-QUADRATIC-REPLAY":
        raise RuntimeError("wrong result status")
    for field in ("constant_terms_zero", "linear_normal_terms_zero", "symbolic_C6", "Q5_syzygy", "Q6_zero", "Q7_syzygy"):
        if result.get(field) is not True:
            raise RuntimeError(("failed result field", field))
    if result.get("quadratic_rows_sha256") != digest(args.quadratics):
        raise RuntimeError("quadratic row hash mismatch")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
