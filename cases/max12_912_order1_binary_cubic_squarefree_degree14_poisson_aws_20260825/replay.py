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
    assert (out / "status.txt").read_text() == "PASS squarefree degree-14 Poisson gate\n"
    for line in (out / "OUTPUT.sha256").read_text().splitlines():
        expected, remote = line.split(maxsplit=1)
        assert digest(out / Path(remote).name) == expected
    stdout = (out / "verifier.stdout").read_text()
    for marker in (
        "ORIGINAL_DEGREE14_PACKAGE_ZERO",
        "CORRECT_CLEARED_Q7_FORMULA_ZERO",
        "OLD_LAMBDA_V_FORMULA_NONZERO",
        "FACTOR_IDENTITY 729*R=324*C*W MOD Z10",
        "PASS_DEGREE14",
    ):
        assert marker in stdout
    assert not any(t in stdout for t in ("skipping text", "FAIL_"))
    return stdout


for line in (ROOT / "SOURCE.sha256").read_text().splitlines():
    expected, name = line.split(maxsplit=1)
    assert digest(ROOT / name) == expected

assert verify("r6d_v2") == verify("box02_v2")
negative = ROOT / "evidence/r6d_v1_diagnostic_negative"
assert (negative / "runner.rc").read_text() == "96\n"
assert "REFUSE_SINGULAR_DIAGNOSTIC" in (negative / "runner.stderr").read_text()
assert "expected `poly` ^ `int`" in (negative / "out/verifier.stderr").read_text()
print("SQUAREFREE_DEGREE14_FROZEN_REPLAY_PASS")
