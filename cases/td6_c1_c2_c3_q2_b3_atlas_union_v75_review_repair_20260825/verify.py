#!/usr/bin/env python3
"""Lightweight custody and named-witness audit for the V75 repair."""

from fractions import Fraction
from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V75 = ROOT / "cases/td6_c1_c2_c3_q2_b3_atlas_union_repaired_v75_aws_20260825"
V73R = ROOT / "cases/td6_c1_c2_c3_q2_cminus5_v73_review_repair_20260825"


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def b3(c, v, u):
    return 4*c*c*u*u - 4*c*v*v*u + 24*c*u**4 + v**4 - 20*v*v*u**3 + 20*u**6


def chart(t, w):
    u = w*w*(t-2)**2/(16*t)
    v = w*u
    c = w**4*(t-2)**2*(-5*t*t+20*t-4)/(256*t*t)
    return c, v, u


def standalone_verdict(text, allowed):
    tokens = [line.strip() for line in text.splitlines() if line.strip() in allowed]
    assert tokens and tokens[-1] in allowed
    return tokens[-1]


def main():
    expected = {
        V75 / "MANIFEST.sha256":
            "9e0dcee29ee15f94fc74ec6af000e712775ff20d54a7532fa64acf2e327d0390",
        V75 / "FREEZE.sha256":
            "0baf634707908ade0d5cb620bc79a2e3d047516c91a3107fd176a30bba69ce87",
        V73R / "FREEZE.sha256":
            "372ac71e69e162b50ecc93d41fb5f0e3c343335a14e2ff515c9cd52602205c1f",
        HERE / "evidence/hostile-review-adapter.log":
            "66329499eb2826d35f0acac19228322a1376c879914c8d994246bc5e1425f132",
        HERE / "evidence/v33-u-zero-D-C.stdout":
            "94e2267d62b162f44abaf32d36405440dd213e1efb4f446cc281ace08b47d0da",
        HERE / "evidence/v33-u-zero-review.md":
            "706f6ad408e680de1b0bb1d9b23c10e49829ab803a9bf06553253e4231b2e291",
        HERE / "evidence/v70-u-h-zero.stdout":
            "2431ed0217d8d71dce2929a8581036d0e11921396dff661466288901243f4ebd",
        HERE / "evidence/v70-origin.stdout":
            "90df496c59c8283c85cec26521a2b422d6ca8d658aa0e8802c968052cd505d67",
        HERE / "evidence/v70-review.md":
            "2a3520866a537a80d17d2f66c2433ba7fcf895606027d755993a1c95402853f6",
    }
    for path, value in expected.items():
        assert digest(path) == value, path

    assert standalone_verdict(
        (HERE / "evidence/v33-u-zero-review.md").read_text(),
        {"CONFIRMED_WITH_REPAIRS"},
    ) == "CONFIRMED_WITH_REPAIRS"
    assert standalone_verdict(
        (HERE / "evidence/v70-review.md").read_text(),
        {"CONFIRMED"},
    ) == "CONFIRMED"

    assert b3(Fraction(1), Fraction(0), Fraction(0)) == 0
    assert b3(Fraction(-1), Fraction(0), Fraction(1)) == 0
    assert b3(Fraction(-5), Fraction(0), Fraction(1)) == 0
    for t in (Fraction(1, 2), Fraction(1)):
        assert b3(*chart(t, Fraction(1))) == 0
    assert (Fraction(1)-2)*(2*Fraction(1)-1)*(Fraction(1)**2-4*Fraction(1)+2) != 0

    review = (HERE / "evidence/hostile-review-adapter.log").read_text()
    assert "CONFIRMED_WITH_REPAIRS" in review
    assert "six constructible leaves cover affine `B3=0`" in review
    print("TD6 V75 review repair custody/witness audit PASS")


if __name__ == "__main__":
    main()
