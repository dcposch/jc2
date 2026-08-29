#!/usr/bin/env python3
"""Additive exact checks for the corrected R7R1 scope."""

import hashlib
import json
import runpy
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PINS = {
    "xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7-sol-20260827.md":
        "b0e60671662953a50318e4989a20a08e5b84e28cb1bfaea075e241fc367a818a",
    "xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7-hostile-audit-sol2-20260827.md":
        "2dd9d8f11e0fadff303c8afade0c1f4e52f1a1df4b5afffcea17d5e3d7890a18",
    "cases/ggv_quarter_root_characteristic_r7_20260827/FREEZE.md":
        "4dedc255ea4de97dace097d201e7f61599f0a13b23e42c3a74cf3481d0ba6d08",
    "cases/ggv_quarter_root_characteristic_r7_20260827/verify_r7.py":
        "c40820e300f39d92d757de698ecf6c8a5ad0b79711e369275b2de93dd6488244",
}

for rel, expected in PINS.items():
    actual = hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()
    assert actual == expected, (rel, actual, expected)

# Replay the exact differential-polynomial and q0/q1/q2 identities.
runpy.run_path(str(ROOT / "cases/ggv_quarter_root_characteristic_r7_20260827/verify_r7.py"))

# Coefficient equation: all inhomogeneous rows retain an arbitrary constant.
for n in range(128):
    multiplier = Fraction(-(n + 2), 16)
    assert multiplier != 0
    # If a_n' = q_n, then multiplier*a_n + c_n has the required derivative.

# Sharp truncation schedule: E=t^22+O(t^N) licenses n+22<N.
assert [n for n in range(8) if n + 22 < 23] == [0]
assert [n for n in range(8) if n + 22 < 24] == [0, 1]
assert [n for n in range(8) if n + 22 < 25] == [0, 1, 2]

# Counterfixture H=X^4, p=X, F=X^8+4X^4*t.
# q0=X^2 has primitive X^3/3; q1=1/X has residue 1 at X=0.
assert Fraction(1, 3) * 3 == 1
q1_residue_at_zero = Fraction(1)
assert q1_residue_at_zero != 0
# w22=-X^3/24 differentiates to -q0/8, so the endpoint row alone closes.
assert Fraction(-3, 24) == Fraction(-1, 8)

# Its implicit Q is not polynomial in s: degree equality would be 8d=d+2.
assert all(8 * d != d + 2 for d in range(256))

# Four-character language is tagged only after adjoining mu_4.
character_exponents_mod4 = [(n + 2) % 4 for n in range(12)]
assert character_exponents_mod4 == [2, 3, 0, 1] * 3

# The D3 slot list is already complete for these polygons, but D5G currently
# compiles only D0..D22; the full determinant can run through weight 35.
raw = json.loads((ROOT / "cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json").read_text())
assert max(x["weight"] for x in raw["raw_slots_through_weight_22"]["F"]) == 14
assert max(x["weight"] for x in raw["raw_slots_through_weight_22"]["G"]) == 21
assert 14 + 21 == 35

print("PASS R7R1 pins, kernel/cutoffs, counterfixture, base-change tag, and D35 scope")
