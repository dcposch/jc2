#!/usr/bin/env python3
"""Fail-closed replay for the exact-Q normal-rank/Fitting endpoints."""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent

LANES = (
    (
        "aws_box02_v1",
        "2e5bf84301ff416c1b1134afd02ccfb81977a96408072416475ca712ede0d485",
        "680aae8ccae647552f8518f41a86a25f4c701b040f1b8e4590084ba655e2ac94",
        "engine=std",
        "order=dp",
    ),
    (
        "aws_box03_v1",
        "90a0b2574116bfa2189e7b8a6d2c6b3ee978b5b3b80cffff6966a11fb72a7e0c",
        "2355ec4a339ebf1b2c1cd229baa951b4221f7b002a88ad43b5576e487ed21efb",
        "engine=slimgb",
        "order=block",
    ),
)

SOURCE_PINS = (
    "d53a9bb6f5b63093d7b623b400ad9717cede8fc49a4f5e359a8966ae3f2d9e65",
    "785683d152bcd23e900700dbce84a50e282886fbc43cb4794b42be344f976d7d",
    "3b3ca106349138f3b918a404e1f9e679fc9c9cd6414856a3e39d84a8f011aedb",
    "5db15af00ec54507d0b9fe79472298b22326c3deb826c6602c61fc4ca59bc9bf",
    "22b0cdc446d1e486d08757df5a3fff83b0506a492f16b9b2cf238966eb947545",
    "a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf",
)

MARKERS = (
    "Q8-W0-OVERLAP-NORMAL-RANK-FITTING",
    "a3_source_rows_zero=1",
    "a3_tangent_columns_zero=1",
    "K3_unit=0",
    "K3_Dd2_empty=1",
    "K3_Dd4_empty=1",
    "GK3[1]=d4",
    "GK3[2]=d2",
    "K2_unit=1",
    "K1_unit=1",
    "K0_unit=1",
    "GM3[1]=d2^2-2*d2*d4+d4^2-2*d2+2*d4+1",
    "Q8_W0_OVERLAP_NORMAL_RANK_FITTING_PASS",
)

BANNED = (
    "redefining",
    "not defined",
    "error occurred",
    "segmentation fault",
    "killed",
    "timed out",
)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def once(text: str, marker: str) -> None:
    assert text.count(marker) == 1, (marker, text.count(marker))


def main() -> None:
    for rel, stdout_sha, input_sha, engine, order in LANES:
        lane = HERE / rel
        stdout = (lane / "stdout").read_text()
        stderr = (lane / "stderr").read_text()
        meta = (lane / "run.meta").read_text()
        source = (lane / "source.sha256").read_text()
        assert (lane / "runner.rc").read_text().strip() == "0"
        assert digest(lane / "stdout") == stdout_sha
        assert digest(lane / "input.sing") == input_sha
        once(meta, "rc=0")
        for marker in MARKERS + (engine, order):
            once(stdout, marker)
        for token in BANNED:
            assert token not in stdout.lower(), (rel, token, "stdout")
            assert token not in stderr.lower(), (rel, token, "stderr")
        for pin in SOURCE_PINS:
            assert pin in source, (rel, pin)
        # Unit bases must appear exactly once for each lower-rank stratum.
        for rank in (2, 1, 0):
            once(stdout, f"K{rank}_BASIS_BEGIN")
            once(stdout, f"GK{rank}[1]=1")
    print("Q8_W0_OVERLAP_NORMAL_RANK_FITTING_REPLAY_PASS")


if __name__ == "__main__":
    main()

