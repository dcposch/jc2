#!/usr/bin/env python3
"""Fail-closed replay for the two accepted V3 tangent endpoints."""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent

LANES = (
    (
        "aws_box02_v3",
        "68959c2f918990766a27fcfadfd80f2eea8521ddab2bdbbe02f131e68d3e6e63",
        "b31d05c152e5357f80cc3d9c375f53630f37252c0842461421753161d0fb2dff",
        "engine=std",
        "order=dp",
    ),
    (
        "aws_box03_v3",
        "d58fcf95633bad3fd092fc82f215e7ffefcc93fa6a5d28ff0d1a397603154235",
        "83732e0d6d857b687c6bcc650f8da73eed84b0c283fa1ffa2849eef7925b320f",
        "engine=slimgb",
        "order=block",
    ),
)

SOURCE_PINS = (
    "63a8633126a6c16b00fa9f4c615b1297de904c95af86a5f1655a26c57251a5fa",
    "3624d3ee17a85176b45a592434c34c0a16a89cb294897de2d1e4d13fd2c15bf7",
    "9edab6362281613bd0246be47a6156e413e6b197fbc14f62bb0cd29f87a1b915",
    "e4d05121a93e7624b83fc790a70f696b868253c58de226d0890ddc41b27cf892",
    "18f930812e3d249d3c61525304c053e8d1f0e5e5fc4e66c44fb5fc0bffd4d001",
    "9702030d556fd062d65682e048cc1c0cac9fa5bf8ab3bd241a161384e102df25",
    "22b0cdc446d1e486d08757df5a3fff83b0506a492f16b9b2cf238966eb947545",
    "a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf",
)

MARKERS = (
    "Q8-W0-OVERLAP-HORIZONTAL-TANGENT",
    "L2=2/9*d2^2-8/9*d2*d4+2/3*d4^2+4/9*d4",
    "L4=-8/27*d2^2+20/27*d2*d4-4/9*d4^2+4/9*d2-16/27*d4",
    "L24_F24_ideal_identity=1",
    "F24_root_ideal_identity=1",
    "F24_two_point_scheme=1",
    "branch0_linear_ideal_identity=1",
    "branch0_L7=0",
    "branch42_linear_ideal_identity=1",
    "branch42_L7=-16/27",
    "branch42_scaled_L7=-432",
    "branch42_residual_identity=1",
    "GF24[1]=d2-2*d4",
    "GF24[2]=d4^2-2*d4",
    "Q8_W0_OVERLAP_HORIZONTAL_TANGENT_PASS",
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
    print("Q8_W0_OVERLAP_HORIZONTAL_TANGENT_V3_REPLAY_PASS")


if __name__ == "__main__":
    main()

