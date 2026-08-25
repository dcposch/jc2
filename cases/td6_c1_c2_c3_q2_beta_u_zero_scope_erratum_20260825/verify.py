#!/usr/bin/env python3
"""Lightweight custody and scope check for the V33/V69 U=0 erratum."""

from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


review = ROOT / "xmodel/td6-c1-c2-c3-q2-beta-u-zero-review-grok-20260825.md"
assert digest(review) == (
    "706f6ad408e680de1b0bb1d9b23c10e49829ab803a9bf06553253e4231b2e291"
)
text = review.read_text()
for marker in (
    "transport_chart_denominator=(C^2)",
    "U=0 ∩ D(C)",
    "C=U=0",
    "CONFIRMED_WITH_REPAIRS",
):
    assert marker in text

erratum = ROOT / "xmodel/td6-c1-c2-c3-q2-beta-u-zero-scope-erratum-20260825.md"
erratum_text = erratum.read_text()
for marker in (
    "NONMUTATING THEOREM-SCOPE CORRECTION",
    "U=0,D(C)",
    "u-h-zero",
    "Dependency quarantine",
    "No whole A3",
):
    assert marker in erratum_text

print("TD6-Q2-BETA-U0-SCOPE-ERRATUM VERIFY PASS")
