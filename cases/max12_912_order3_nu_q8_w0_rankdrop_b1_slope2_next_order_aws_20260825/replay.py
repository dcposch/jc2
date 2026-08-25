#!/usr/bin/env python3
"""Fail-closed source/custody replay for the b=1 next-order jet control."""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import subprocess
import sys

CASE = Path(__file__).resolve().parent
B02 = CASE / "aws_box02_std_dp_v2"
B03 = CASE / "aws_box03_slimgb_block_v2"

EXPECTED = {
    CASE / "PREREGISTRATION.md": "79142a0ce2dbe1cbb063ef1a94510abe90a54415ff348e091b9c7f95086efc07",
    CASE / "generate.py": "6fd32c94ddef8ee7a32b0d9ed319e6429d83f9bc7d2bf66bad4a1044283a51bd",
    CASE / "run_remote.sh": "72eaa614f4190db2849b6870f641ae4ce46127e02d4143258d8a24035ff0a0e3",
    B02 / "input.sing": "882f26a8ea0674802909620962e1f92604514d5d18daf5b64c1c646157d14a27",
    B02 / "stdout": "41592eb32803d82b765910bd3a8d66dd0d45027e1f924bfe150fdeb34c048ae1",
    B02 / "stderr": "d571955d14d12084caeabbc33ed3492fc287c4416275be64ee071de2aec815ed",
    B03 / "input.sing": "9119d63ec5f792f70a24de2aa47032505f836e616f35eb065348aca0f8235b31",
    B03 / "stdout": "9045167de5074ebcdaab8e69c66b25d6de653081c1d0a527cbad0cd130961072",
    B03 / "stderr": "e7a69516800a288748315c0fa39d0fe2e0fd4d018dfd6aa5e6be1ce7410fa59f",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def between(text: str, begin: str, end: str) -> str:
    require(text.count(begin) == 1 and text.count(end) == 1, f"marker {begin}")
    return text.split(begin, 1)[1].split(end, 1)[0].strip()


def main() -> None:
    for path, expected in EXPECTED.items():
        require(path.is_file() and digest(path) == expected, f"hash {path}")

    variants = (("std", "dp", B02), ("slimgb", "block", B03))
    coefficient_blocks = []
    for engine, order, out in variants:
        generated = subprocess.check_output([
            sys.executable, str(CASE / "generate.py"),
            "--engine", engine, "--order", order,
        ])
        require(generated == (out / "input.sing").read_bytes(), f"regeneration {engine}")
        require((out / "runner.rc").read_text() == "0\n", f"rc {engine}")
        require((out / "generator.stderr").read_bytes() == b"", f"generator {engine}")
        text = (out / "stdout").read_text()
        for marker in (
            "leading_zero=1", "next_unit=1", "GNext[1]=1", "GEc[1]=1",
            "Q8_W0_RANKDROP_B1_SLOPE2_NEXT_PASS",
        ):
            require(text.splitlines().count(marker) == 1, f"{engine}: {marker}")
        coefficient_blocks.append(between(text, "NEXT_COEFFICIENTS_BEGIN", "NEXT_COEFFICIENTS_END"))
    require(coefficient_blocks[0] == coefficient_blocks[1], "coefficient disagreement")
    print("Q8_W0_RANKDROP_B1_SLOPE2_NEXT_REPLAY_PASS")


if __name__ == "__main__":
    main()
