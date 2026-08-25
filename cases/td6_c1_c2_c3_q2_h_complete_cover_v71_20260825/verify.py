#!/usr/bin/env python3
"""Lightweight custody and set-cover gate for the reviewed V71 composition."""

from fractions import Fraction
from hashlib import sha256
from itertools import product
from pathlib import Path


HERE = Path(__file__).resolve().parent


def check_dependencies():
    for line in (HERE / "DEPENDENCIES.sha256").read_text().splitlines():
        expected, relative = line.split("  ", 1)
        path = (HERE / relative).resolve()
        assert path.is_file(), path
        assert sha256(path.read_bytes()).hexdigest() == expected, path


def check_verdicts():
    reviews = (
        "../../xmodel/td6-c1-c2-c3-q2-h-source-dag-repaired-v64-review-grok-20260825.md",
        "../../xmodel/td6-c1-c2-c3-q2-v-h-zero-source-unit-v62d-review-grok-20260825.md",
        "../../xmodel/td6-c1-c2-c3-q2-p3-qh-source-dag-v65-review-grok-20260825.md",
        "../../xmodel/td6-c1-c2-c3-q2-beta-u-h-zero-v70-review-grok-20260825.md",
    )
    for relative in reviews:
        text = (HERE / relative).resolve().read_text().rstrip()
        assert text.endswith("CONFIRMED"), relative


def check_cover():
    # Booleans mean that U,V,P3,QH are nonzero at a putative H=0 point.
    for u, v, p3, qh in product((False, True), repeat=4):
        leaves = (
            not u,                  # V70: U=0
            u and not v,            # V62D: D(U), V=0
            u and not p3,           # V65: D(U), P3=0
            u and not qh,           # V65: D(U), QH=0
            u and v and p3 and qh,  # V64: D(U V P3 QH)
        )
        assert any(leaves), (u, v, p3, qh)


def multiply(left, right):
    out = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def check_bezout_control():
    # Coefficients are low-to-high powers of T.
    qh = [Fraction(-64), Fraction(8), Fraction(1)]
    p3 = [Fraction(128), Fraction(-32), Fraction(1)]
    left = multiply([Fraction(-136), Fraction(5)], qh)
    right = multiply([Fraction(64), Fraction(5)], p3)
    difference = [a - b for a, b in zip(left, right)]
    assert difference == [Fraction(512), Fraction(0), Fraction(0), Fraction(0)]


def main():
    check_dependencies()
    check_verdicts()
    check_cover()
    check_bezout_control()
    print("TD6-A3-Q2-H-COMPLETE-COVER-V71 CUSTODY PASS")
    print("exact_scope=whole H=0 inside fixed source-typed A3 q2-beta")
    print("whole_A3_or_TD6_or_SP2=false")


if __name__ == "__main__":
    main()
