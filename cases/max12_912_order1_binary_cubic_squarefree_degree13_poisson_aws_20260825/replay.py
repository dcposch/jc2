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
    assert (out / "status.txt").read_text() == "PASS squarefree degree-13 Poisson gate\n"
    for line in (out / "OUTPUT.sha256").read_text().splitlines():
        expected, remote = line.split(maxsplit=1)
        assert digest(out / Path(remote).name) == expected
    stdout = (out / "verifier.stdout").read_text()
    for marker in (
        "RATIONAL_DEGREE13_CLEARED_ORIGINAL_ROW_ZERO",
        "COLLAPSED_DEGREE13_ORIGINAL_ROW_ZERO",
        "DEGREE13_POLE_NUMERATOR_FACTORED",
        "PASS_DEGREE13",
    ):
        assert marker in stdout
    assert not any(t in stdout for t in ("skipping text", "FAIL_"))
    return stdout


for line in (ROOT / "SOURCE.sha256").read_text().splitlines():
    expected, name = line.split(maxsplit=1)
    assert digest(ROOT / name) == expected
assert verify("r6d_v2") == verify("box02_v2")
print("SQUAREFREE_DEGREE13_FROZEN_REPLAY_PASS")
