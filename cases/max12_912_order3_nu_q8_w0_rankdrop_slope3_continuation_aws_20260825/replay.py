#!/usr/bin/env python3
"""Fail-closed replay for the two accepted V3 slope-three endpoints."""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent
LANES = (
    ("aws_box02_v3", "598a2e9c1f02b48101e9c4d8c77208af9134603ef219be1363ff17b2c3eff4a8", "303590394dd4df74c46cf6cf09c50beab32141703a740098c187f07774f47d82", "engine=std", "order=dp"),
    ("aws_box03_v3", "f31cc2861dfc6458b15dc2776ef6c6f9d5f5efa6edcd97802665fac080f2576c", "45da37167d5624219feeb40f9227d95c6e166c3c1ee5e30275c6a0a4010a57de", "engine=slimgb", "order=block"),
)
PINS = (
    "38c412c4b2c28a76df5db79b3b3d9fc54241cb4e9ff5a898532c48eedc36c7b6",
    "49e5d96b4f8dd48e53d91fba8129ba9d6af734222437b87f8a13cb418e9cc420",
    "acb68c7c1f9ab5d36e396504bb3cf265f96a2b098db419ab78c93cd9eeccfcaf",
    "90cc2fccdd43f6ecd696e58b6321dfb225ada8c4014a827f76befd59651c209e",
    "35f90eb30adb5f04f53835b99a5476e64ca275f1b7ba50964abb4c92ef681b19",
    "22b0cdc446d1e486d08757df5a3fff83b0506a492f16b9b2cf238966eb947545",
    "a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf",
)
MARKERS = (
    "LEADING_CHART_BEGIN",
    "leading_ideal_identity=1",
    "GLead[1]=U2",
    "GLead[2]=b-1",
    "3*c*z-z-3*Q1",
    "z^2+3*X2-3*Z2",
    "Q8-W0-RANKDROP-SLOPE3-CONTINUATION",
    "actual_expected_ideal_identity=1",
    "continuation_unit=1",
    "third_residual=-108",
    "Q8_W0_RANKDROP_SLOPE3_CONTINUATION_PASS",
)
BANNED = ("redefining", "not defined", "error occurred", "segmentation fault", "killed", "timed out")


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    for rel, out_hash, input_hash, engine, order in LANES:
        lane = HERE / rel
        out = (lane / "stdout").read_text()
        err = (lane / "stderr").read_text()
        src = (lane / "source.sha256").read_text()
        assert (lane / "runner.rc").read_text().strip() == "0"
        assert digest(lane / "stdout") == out_hash
        assert digest(lane / "input.sing") == input_hash
        for marker in MARKERS + (engine, order):
            assert out.count(marker) == 1, (rel, marker, out.count(marker))
        for pin in PINS:
            assert pin in src, (rel, pin)
        for token in BANNED:
            assert token not in out.lower(), (rel, token, "stdout")
            assert token not in err.lower(), (rel, token, "stderr")
    print("Q8_W0_RANKDROP_SLOPE3_CONTINUATION_V3_REPLAY_PASS")


if __name__ == "__main__":
    main()

