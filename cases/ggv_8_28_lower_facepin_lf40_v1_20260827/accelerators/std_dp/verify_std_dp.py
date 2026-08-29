#!/usr/bin/env python3
"""Verify that the LF40 std/dp accelerator changes only the exact GB engine."""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import sys


CASE = Path("cases/ggv_8_28_lower_facepin_lf40_v1_20260827")
BASE_SHA256 = "435c350f8a5be062d9b1e1b7cf57e9483dcf2648400fe250d4edbd13ccf846f7"
STD_SHA256 = "7256fcaddcdc2875ca6c31b2033f0e6950a598b8a22d3cc338c92069a89f21a5"
ROW17 = "ideal ROW_17=1+f_0_1*g_1_0-f_1_0*g_0_1,"


def digest(payload: bytes) -> str:
    return sha256(payload).hexdigest()


def fail(message: object) -> None:
    raise SystemExit(f"LF40_STD_DP_VERIFY_FAIL: {message}")


def main() -> int:
    if len(sys.argv) != 2:
        fail("usage: verify_std_dp.py SOURCE_ROOT")
    root = Path(sys.argv[1]).resolve()
    base = (root / CASE / "compiled/lf40_sequential_QQ.sing").read_bytes()
    derived = (root / CASE / "accelerators/std_dp/lf40_sequential_QQ_std_dp.sing").read_bytes()

    if digest(base) != BASE_SHA256:
        fail(("base program hash", digest(base)))
    if digest(derived) != STD_SHA256:
        fail(("derived program hash", digest(derived)))
    if base.count(b"slimgb(") != 41:
        fail(("base slimgb call census", base.count(b"slimgb(")))

    expected = base.replace(b"slimgb(", b"std(")
    if derived != expected:
        fail("derived program differs from the literal 41-call engine substitution")
    if derived.count(b"slimgb(") != 0 or derived.count(b"std(") != 43:
        fail(("derived engine census", derived.count(b"std("), derived.count(b"slimgb(")))
    if b"ring R=0," not in derived or b"),dp;" not in derived:
        fail("exact QQ/dp ring declaration missing")
    if derived.count(ROW17.encode()) != 1:
        fail(("row-17 target count", derived.count(ROW17.encode())))

    omission = derived.replace(b"ideal ROW_17=1+", b"ideal ROW_17=", 1)
    opposite = derived.replace(b"ideal ROW_17=1+", b"ideal ROW_17=-1+", 1)
    if omission.count(ROW17.encode()) or opposite.count(ROW17.encode()):
        fail("target mutations were not independently rejected")

    print("PASS_LF40_STD_DP_EXACT_ENGINE_SUBSTITUTION")
    print(f"base_sha256={BASE_SHA256}")
    print(f"std_dp_sha256={STD_SHA256}")
    print("changed_calls=41")
    print("target_mutations=OMISSION_REJECTED,OPPOSITE_SIGN_REJECTED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
