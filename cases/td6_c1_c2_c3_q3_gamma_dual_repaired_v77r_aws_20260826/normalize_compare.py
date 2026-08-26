#!/usr/bin/env python3
"""Lightweight byte comparator; it never imports the exact producer."""

from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent


def normalized(path: Path) -> bytes:
    return b"".join(
        line
        for line in path.read_bytes().splitlines(keepends=True)
        if not line.startswith(b"aws_")
    )


box02 = normalized(HERE / "evidence" / "box02" / "stdout")
r6d = normalized(HERE / "evidence" / "r6d" / "stdout")
assert box02 == r6d
digest = sha256(box02).hexdigest()
assert digest == "f6aaf1c9f4e9f1e6961525a5cf79fd53ac4e3ee226520e34d652a7642fdabf1e"
print(f"normalized_stdout_sha256={digest}")
print("TD6-V77R-NORMALIZED-BYTE-COMPARISON PASS")
