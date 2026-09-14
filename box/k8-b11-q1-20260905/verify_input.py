#!/usr/bin/env python3
"""Fail-closed custody check for the K=8, b=11, q1 emitted msolve file."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


EXPECTED = {
    "sha256": "66bb78cfec123e11c5b9c780056b5949aa1c5c198caeb3c668aab1973d6697eb",
    "bytes": 65_003_245,
    "variables": 97,
    "generators": 330,
    "characteristic": "0",
}


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {Path(sys.argv[0]).name} INPUT.ms")
    path = Path(sys.argv[1])
    payload = path.read_bytes()
    lines = payload.decode("utf-8").splitlines()
    actual = {
        "sha256": hashlib.sha256(payload).hexdigest(),
        "bytes": len(payload),
        "variables": len(lines[0].split(",")) if lines else None,
        "generators": len(lines) - 2 if len(lines) >= 2 else None,
        "characteristic": lines[1] if len(lines) >= 2 else None,
    }
    result = {
        "path": str(path.resolve()),
        "expected": EXPECTED,
        "actual": actual,
        "match": actual == EXPECTED,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["match"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
