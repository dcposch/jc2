#!/usr/bin/env python3
from __future__ import annotations

import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(name: str) -> str:
    run = ROOT / "evidence" / name
    out = run / "out"
    assert (run / "runner.rc").read_text() == "0\n"
    assert (out / "status.txt").read_text() == "PASS squarefree degree-12 Poisson gate\n"
    for line in (out / "OUTPUT.sha256").read_text().splitlines():
        expected, remote = line.split(maxsplit=1)
        assert digest(out / Path(remote).name) == expected
    stdout = (out / "verifier.stdout").read_text()
    for marker in (
        "RATIONAL_DEGREE12_CLEARED_ORIGINAL_ROW_ZERO",
        "DEGREE12_POLE_FACTORIZATION_ZERO",
        "ROOT_ALLOCATION_BRANCH_COUNT 8",
        "PASS_DEGREE12",
    ):
        assert marker in stdout
    assert not any(t in stdout for t in ("skipping text", "FAIL_"))
    return stdout


for line in (ROOT / "SOURCE.sha256").read_text().splitlines():
    expected, name = line.split(maxsplit=1)
    assert digest(ROOT / name) == expected
assert verify("r6d_v1") == verify("box02_v1")
print("SQUAREFREE_DEGREE12_FROZEN_REPLAY_PASS")
