#!/usr/bin/env python3
"""Algebraic equality of derived r=1 scalars vs the charged Opus closed forms."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys_path_note = str(HERE)
import sys

sys.path.insert(0, sys_path_note)
import sq_engine as S  # noqa: E402
from sq_engine import d, t  # noqa: E402

Q4 = 27 * t**4 + 206 * t**3 + 527 * t**2 + 540 * t + 300
claimed = {
    "c1": (t + 2)
    * (
        -9 * d * t**3
        - 12 * d * t**2
        - 9 * d * t
        + 30 * d
        + 27 * t**4
        + 153 * t**3
        + 283 * t**2
        + 247 * t
        + 90
    )
    / ((2 * t + 1) * Q4),
    "c2": -(6 * d * t - 3 * d + 9 * t**2 + 2 * t - 1) / (6 * t * (3 * t - 1)),
    "A1": t
    * (3 * t + 1)
    * ((27 * t**3 - 30 * t**2 + t - 2) * d + (6 * t**3 + 13 * t**2 - 3 * t + 2))
    / (12 * (2 * t + 1) ** 2 * (3 * t - 1) ** 2 * (3 * t + 2)),
    "A5": -t * (t - 2) * (3 * t + 1) * (6 * d * t - t - 1) / (72 * (2 * t + 1) ** 3 * (3 * t - 1)),
}

core = json.loads((HERE / "qplane_core_r1.json").read_text())
got = {
    "c1": sp.sympify(core["c"]["c1"], locals={"d": d, "t": t}),
    "c2": sp.sympify(core["c"]["c2"], locals={"d": d, "t": t}),
    "A1": sp.sympify(core["rows"]["A1"]["coeff"], locals={"d": d, "t": t}),
    "A5": sp.sympify(core["rows"]["A5"]["coeff"], locals={"d": d, "t": t}),
}


def eq(a, b):
    diff = S.sred(a - b)
    return diff == 0, diff


ok = True
for name in ("c1", "c2", "A1", "A5"):
    hit, diff = eq(got[name], claimed[name])
    ok &= hit
    print("%s %s" % (name, "EQUAL" if hit else "DIFF " + str(diff)))

# A2: compare N(Du) to (3.5)
A2 = sp.sympify(core["rows"]["A2"]["coeff"], locals={"d": d, "t": t})
Nn = sp.sympify(core["rows"]["A2"]["N"], locals={"t": t})
claimedN = (
    3
    * t**2
    * (t - 1) ** 6
    * (t + 1)
    * (t + 2) ** 6
    * (3 * t + 1) ** 2
    * (4 * t + 1)
    * (t**2 + 3 * t + 6)
    * (25 * t**2 + 12 * t - 12)
    * Q4**3
)
print("A2_N", "EQUAL" if sp.expand(Nn - claimedN) == 0 else "DIFF")
ok &= sp.expand(Nn - claimedN) == 0
print("FORM_EQ", "PASS" if ok else "FAIL")
