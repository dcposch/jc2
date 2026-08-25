#!/usr/bin/env python3
"""Fail-closed custody/source replay for the frozen r6d modStd endpoint.

This does not rerun Singular.  It regenerates the exact input, checks the
frozen endpoint hashes and required source/output markers, and preserves the
important limitation that the printed lift is for Landing after GC=(1), not a
cofactor identity in the original six rows plus localizer.
"""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import subprocess
import sys


CASE = Path(__file__).resolve().parent
ROOT = CASE.parents[1]
OUT = CASE / "aws_r6d_modstd_v1"

EXPECTED = {
    CASE / "PREREGISTRATION.md": "597ed4c5e86f7f1509a5bf016f4dfcbd2a6061dc99ee2fc77bccb01c59ee1c74",
    CASE / "generate.py": "e03ae4db2e53767b1d624c9b7ee3de5512cbbceb2c8dc89e86550afd9b0517b0",
    CASE / "run_remote.sh": "f9b759dd4883a077576060dbf4ab6afb1667c250ae5d9ffab80cb387382822b1",
    OUT / "generator.stderr": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    OUT / "input.sing": "b42f85f48b9e4f480267c1ce39955877a54c4862697043e9ff17ff25664c1d6b",
    OUT / "run.meta": "afa4679f45999c8dc2b8fafbe246c1d4feb8cc834f27d84f17188f88c942bdd0",
    OUT / "runner.rc": "9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa",
    OUT / "source.sha256": "af0dee6ec951c801ed3dfadffffcfd0ddc21f2e14c8b09e8391bd7a40299e063",
    OUT / "stderr": "664748453136b23c57352bc774ef70fc1342eecf274f4a78b001d682dac41d53",
    OUT / "stdout": "603d866150a08dda98298b755f41718c48cc2075a6b47ff5741ffa8e3a413481",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> None:
    for path, expected in EXPECTED.items():
        require(path.is_file(), f"missing {path}")
        require(digest(path) == expected, f"hash mismatch {path}")

    generated = subprocess.check_output([sys.executable, str(CASE / "generate.py")])
    require(generated == (OUT / "input.sing").read_bytes(), "input regeneration mismatch")

    source = (OUT / "input.sing").read_text()
    for marker in (
        "ideal SI=se1,se3,se5,se7,se2,se4;",
        "map phi=S,w,c,2+u,1,x1,x3,x5;",
        "ideal J=I,inv*w*x5*A-1;",
        "ideal GJ=modStd(J,1);",
        "ideal C=eliminate(GJ,inv);",
        "ideal Landing=GC,w,u,x1,x3,x5;",
        "matrix LT=lift(Landing,ONE,U);",
    ):
        require(source.count(marker) == 1, f"source marker mismatch: {marker}")

    stdout = (OUT / "stdout").read_text()
    expected_lines = (
        "control_original_remainders_zero=1",
        "original_remainders_zero=1",
        "contraction_remainders_zero=1",
        "landing_remainders_zero=1",
        "landing_empty=1",
        "lift_residual_zero=1",
        "GJ[1]=1",
        "GC[1]=1",
        "GL[1]=1",
        "Q8_W0_RANKDROP_B1_MODSTD_PASS",
    )
    for line in expected_lines:
        require(stdout.splitlines().count(line) == 1, f"output marker mismatch: {line}")

    require((OUT / "runner.rc").read_text() == "0\n", "runner rc")
    require((OUT / "generator.stderr").read_bytes() == b"", "generator stderr")
    stderr = (OUT / "stderr").read_text().lower()
    require("exit status: 0" in stderr, "time exit status")
    require("elapsed (wall clock) time (h:mm:ss or m:ss): 10:40.20" in stderr, "time record")
    for bad in ("killed", "timed out", "segmentation fault", "error occurred", "not defined"):
        require(bad not in (stdout.lower() + stderr), f"diagnostic: {bad}")

    print("Q8_W0_RANKDROP_B1_MODSTD_CUSTODY_REPLAY_PASS")


if __name__ == "__main__":
    main()
