#!/usr/bin/env python3
"""Fail-closed custody/source replay for the two exact-Q b=1 elimination PASS lanes."""

from __future__ import annotations

import hashlib
from pathlib import Path
import subprocess
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]

PINS = {
    "PREREGISTRATION.md": "04385277a9eb846856288be71ade9d263a481a74b1c4f31b0916057c979b33e2",
    "ELIM_PREREGISTRATION.md": "a3be2d8ef07c3658ed5f80b753bbd89632d2356592f46573b20d9db9c4384c71",
    "generate_elim.py": "25f3f2b27200c48e60432392c14c8631540274e63c4e0d3f64aa10ea0dbb3a5a",
    "run_elim_remote.sh": "828c6617a50bc52dcc3baeee6b2bb3340d6d8cf167d9876c4f074291e25d68bb",
    "AWS_R6D_SINGULAR_VERSION.txt": "5647a1d759fcd2992dfcad94179960bc700a89e0d6be8b3ba8004d4a7193aafe",
    "aws_r6d_elim_std_v1/input.sing": "5e43ebd1a4a9c57c539da4ff0ffaa7a2dab5efd4106e1179afcd67ca4c98a403",
    "aws_r6d_elim_std_v1/stdout": "24f566bfdea08c47dec320b14ebecf0faa1f32abd191d05cd88227a6992db1fd",
    "aws_r6d_elim_std_v1/stderr": "f3315c9f40e30db59650d1d5379b4cccc912384608c79f63aac0a2ddf27e43cb",
    "aws_r6d_elim_std_v1/generator.stderr": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "aws_r6d_elim_std_v1/runner.rc": "9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa",
    "aws_r6d_elim_std_v1/run.meta": "0bd3b55519a47baf1e1e069da411283de6cd32a49d580ae62d954bd2b4f7b9ce",
    "aws_r6d_elim_std_v1/source.sha256": "f6e4c68aecacf688ca1f96e7b29313ac4bc3def83d147665a6d5d36a382715b5",
    "aws_r6d_elim_slimgb_v1/input.sing": "600b1ae7240838f625c1779ba130627966a0615dbcc217abb7c2a7fe33e0d01d",
    "aws_r6d_elim_slimgb_v1/stdout": "ed77831623587d8f90bdfc77239f561571731ee03a727e2a28bb57d1e265f895",
    "aws_r6d_elim_slimgb_v1/stderr": "4f6c92d7ccfa605a5c1c1022418690b10bc763ac71fc71e8f00272c51ad84d0f",
    "aws_r6d_elim_slimgb_v1/generator.stderr": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "aws_r6d_elim_slimgb_v1/runner.rc": "9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa",
    "aws_r6d_elim_slimgb_v1/run.meta": "60f10f33e30af1142d466d60f598544c8298fed2ec4c664c58139d3a14bc7a16",
    "aws_r6d_elim_slimgb_v1/source.sha256": "07b02ab04f0d3f1411fa99c5ce8d02731468af61f4dba799e39034f3cf6c3082",
}

TRANSITIVE = {
    ROOT / "cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py":
        "22b0cdc446d1e486d08757df5a3fff83b0506a492f16b9b2cf238966eb947545",
    ROOT / "cases/max12_912_order3_fibre_20260824/order3_fibre.py":
        "a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf",
}

BANNED = (
    "redefining", "not defined", "error occurred", "segmentation fault",
    "killed", "timed out", "no standard basis", "// **",
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    for rel, expected in PINS.items():
        path = HERE / rel
        got = digest(path)
        if got != expected:
            raise RuntimeError((rel, got, expected))
    for path, expected in TRANSITIVE.items():
        got = digest(path)
        if got != expected:
            raise RuntimeError((str(path), got, expected))

    for engine, lane in (
        ("std", HERE / "aws_r6d_elim_std_v1"),
        ("slimgb", HERE / "aws_r6d_elim_slimgb_v1"),
    ):
        regenerated = subprocess.run(
            [sys.executable, str(HERE / "generate_elim.py"), "--engine", engine],
            check=True, capture_output=True, text=False,
        ).stdout
        frozen = (lane / "input.sing").read_bytes()
        if regenerated != frozen:
            raise RuntimeError((engine, "regeneration mismatch"))
        text = frozen.decode()
        required_source = (
            "ideal SI=se1,se3,se5,se7,se2,se4;",
            "ring R=(0,c),(inv,w,u,x1,x3,x5),(dp(1),dp(5));",
            "map phi=S,w,c,2+u,1,x1,x3,x5;",
            "ideal J=I,inv*w*x5*A-1;",
            "ideal C=eliminate(GJ,inv);",
            "ideal Landing=GC,w,u,x1,x3,x5;",
        )
        for marker in required_source:
            if text.count(marker) != 1:
                raise RuntimeError((engine, marker, text.count(marker)))
        stdout = (lane / "stdout").read_text()
        required_output = (
            f"engine={engine}",
            "landing_empty=1",
            "GL[1]=1",
            "GC[1]=1",
            "Q8_W0_RANKDROP_B1_LOCALIZER_ELIMINATION_PASS",
        )
        for marker in required_output:
            if stdout.count(marker) != 1:
                raise RuntimeError((engine, marker, stdout.count(marker)))
        if (lane / "runner.rc").read_text() != "0\n":
            raise RuntimeError((engine, "nonzero rc"))
        diagnostics = (stdout + "\n" + (lane / "stderr").read_text()).lower()
        for token in BANNED:
            if token in diagnostics:
                raise RuntimeError((engine, "banned diagnostic", token))

    print("Q8_W0_RANKDROP_B1_LOCALIZER_ELIMINATION_REPLAY_PASS")


if __name__ == "__main__":
    main()
