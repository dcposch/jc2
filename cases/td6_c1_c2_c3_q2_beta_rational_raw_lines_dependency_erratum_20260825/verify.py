#!/usr/bin/env python3
"""Lightweight custody/scope check for the rational-line erratum."""

from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


PINS = {
    "xmodel/td6-c1-c2-c3-q2-beta-rational-raw-lines-aws-20260825.md":
        "0101a2f249e914af6e413bb2a9d8d7dd9ac46ffc1282fc31c67e7fe271b84b58",
    "xmodel/td6-c1-c2-c3-q2-beta-rational-raw-lines-review-grok-20260825.md":
        "2e76f499895c34f0532f09b44e865ffdfb9acad6ebf896ce1d0fc55477830555",
    "xmodel/td6-c1-c2-c3-q2-beta-u-h-zero-v70-aws-20260825.md":
        "9013ec370a4d5651c08afa921a0b56e799651f1f490908208221240baddd8c45",
    "xmodel/td6-c1-c2-c3-q2-beta-u-h-zero-v70-review-grok-20260825.md":
        "2a3520866a537a80d17d2f66c2433ba7fcf895606027d755993a1c95402853f6",
    "xmodel/td6-c1-c2-c3-q2-n13-localization-scope-erratum-20260825.md":
        "4f6e2bf34cc7c4ea04f66e57a949fb04d4356941ee3762642ca050840f25e1b9",
    "xmodel/td6-c1-c2-c3-q2-b3-boundary-factor-routes-v68-review-grok-20260825.md":
        "b9ac3c7c0748ec5b75ad1e7b2bee063a30b864c470eb80863a65deeb0f93b048",
}

for rel, expected in PINS.items():
    assert digest(ROOT / rel) == expected, rel

review = (ROOT / "xmodel/td6-c1-c2-c3-q2-beta-rational-raw-lines-review-grok-20260825.md").read_text()
for marker in (
    "CONFIRMED_WITH_REPAIRS",
    "V=0, C=-U^2     empty as a whole line",
    "N13_full_source_lift_in_this_file=false",
    "V70 origin leaf restores each line",
):
    assert marker in review, marker

v70 = (ROOT / "xmodel/td6-c1-c2-c3-q2-beta-u-h-zero-v70-review-grok-20260825.md").read_text()
for marker in (
    "source_center=C=V=U=0",
    "v70_transport_complete_certificate_denominator=(1)",
    "CONFIRMED",
):
    assert marker in v70, marker

erratum = (ROOT / "xmodel/td6-c1-c2-c3-q2-beta-rational-raw-lines-dependency-erratum-20260825.md").read_text()
for marker in (
    "NONMUTATING DEPENDENCY AND SCOPE REPAIR",
    "C=-5U^2,D(U)",
    "precise remaining staged-N13 source-DAG debt",
    "No whole-B3 original-source theorem",
    "No whole `H=0`",
):
    assert marker in erratum, marker

print("TD6-Q2-BETA-RATIONAL-LINES-DEPENDENCY-ERRATUM VERIFY PASS")
