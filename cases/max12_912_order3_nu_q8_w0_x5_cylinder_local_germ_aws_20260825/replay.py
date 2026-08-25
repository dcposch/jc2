#!/usr/bin/env python3
"""Fail-closed replay for the two independent V3 cylinder certificates."""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent

LANES = (
    (
        "aws_box02_v3/q8_w0_x5_cylinder_local_germ_Q_std_dp_box02_v3",
        "0b12669b9faa754325966a0ed9d07b6ae0b0365db361455d0dea2728bfc76b69",
        "engine=std",
        "order=dp",
        "c089ea4f4800716578c73ff8f9fbd78a6bd5a59297bbdf34b11f0620fe6ee76a",
    ),
    (
        "aws_box03_v3/q8_w0_x5_cylinder_local_germ_Q_slimgb_block_box03_v3",
        "2ccb5db3d8cde38dcb959996e4c2fe7713763895c199d015dae9f0b06c6ed1b8",
        "engine=slimgb",
        "order=block",
        "e7a647537e4d065bebde46ccedd15a761071b8ae6914725e71583ab92b9c30d7",
    ),
)

SOURCE_PINS = (
    "d9577a096b2817929656028787698bc7a7c9e0706ea1a10ccecc0a956289c2bd",
    "b8701038a53486deac7d648cc8c23d9097d543900093ea660d1daf137d1ec638",
    "44b830c06e1bf783dc3c8ddcd25c9b0d10ae8acfd2d7e89a648c1c9f7c60a4de",
    "4d56ab3008e070e4b53dcdd890a39e8071dde2dfee030599bfae930f6628b9bb",
    "22e43c11572ff6be285d9b357ea90dad140ded989a6452dff83196712072c18f",
    "22b0cdc446d1e486d08757df5a3fff83b0506a492f16b9b2cf238966eb947545",
    "a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf",
)

MARKERS = (
    "Q8-W0-X5-CYLINDER-LOCAL-GERM",
    "cylinder_dim=2",
    "source_rows_zero=1",
    "Fw_zero=1",
    "all_6x6_minors_zero=1",
    "rank5_minor_identity=1",
    "rank5_minor_normal_form=1024/1594323*x3^6",
    "a_kernel_zero=1",
    "e6_normal_form=-4/81*x3^3",
    "e8_normal_form=0",
    "CYLINDER_BASIS_BEGIN",
    "CYLINDER_BASIS_END",
    "Q8_W0_X5_CYLINDER_LOCAL_GERM_PASS",
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


def require_once(text: str, marker: str) -> None:
    assert text.count(marker) == 1, (marker, text.count(marker))


def main() -> None:
    for rel, stdout_sha, engine, order, input_sha in LANES:
        lane = HERE / rel
        stdout = (lane / "stdout").read_text()
        stderr = (lane / "stderr").read_text()
        meta = (lane / "run.meta").read_text()
        source = (lane / "source.sha256").read_text()

        assert (lane / "runner.rc").read_text().strip() == "0"
        assert digest(lane / "stdout") == stdout_sha
        assert digest(lane / "input.sing") == input_sha
        require_once(meta, "rc=0")
        for marker in MARKERS + (engine, order):
            require_once(stdout, marker)
        for token in BANNED:
            assert token not in stdout.lower(), (rel, token, "stdout")
            assert token not in stderr.lower(), (rel, token, "stderr")
        for pin in SOURCE_PINS:
            assert pin in source, (rel, pin)

    # The cylinder ideals can print in different Groebner-basis orders, but
    # both must exhibit every defining generator.
    for rel, *_ in LANES:
        stdout = (HERE / rel / "stdout").read_text()
        for generator in ("x5", "x1-x3", "d4", "d2", "c-ib", "x3*ib-1"):
            assert generator in stdout, (rel, generator)

    print("Q8_W0_X5_CYLINDER_LOCAL_GERM_V3_REPLAY_PASS")


if __name__ == "__main__":
    main()
