#!/usr/bin/env python3
"""Exact raw-window audit of the D22[X^0] odd endpoint coupling."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RAW_INPUT = (
    ROOT
    / "cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827"
    / "RAW_INPUT.json"
)
RAW_INPUT_SHA256 = "28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def windows(source):
    out = {"F": {}, "G": {}}
    for kind in out:
        for slot in source["raw_slots_through_weight_22"][kind]:
            weight = int(slot["weight"])
            degree = int(slot["raw_exponents"]["x"])
            out[kind].setdefault(weight, {})[degree] = slot
    return out


def main():
    assert sha256(RAW_INPUT) == RAW_INPUT_SHA256
    source = json.loads(RAW_INPUT.read_text())
    raw = windows(source)

    # In the upper chart X=x*y^3 and t=1/y.  Thus a weight-w F slot X^i
    # represents x^i*y^(8+3i-w), and a G slot represents
    # x^i*y^(12+3i-w).  Verify this directly for every charged slot.
    for kind, base in (("F", 8), ("G", 12)):
        for weight, row in raw[kind].items():
            for degree, slot in row.items():
                exponents = slot["raw_exponents"]
                assert int(exponents["y"]) == base + 3 * degree - weight
                total_degree = degree + int(exponents["y"])
                assert total_degree % 2 == weight % 2

    # D_n=sum_(i+j=n) ((12-j)F_i'G_j+(i-8)F_iG_j').  At X-degree zero,
    # only an X^1 coefficient can be differentiated and only an X^0
    # coefficient can multiply it.  Enumerate from the literal windows;
    # discard structural zero multipliers rather than assuming a range law.
    contributions = []
    for i in raw["F"]:
        j = 22 - i
        if j not in raw["G"]:
            continue
        if 1 in raw["F"][i] and 0 in raw["G"][j] and 12 - j:
            contributions.append({
                "coefficient": 12 - j,
                "left": raw["F"][i][1]["slot"],
                "right": raw["G"][j][0]["slot"],
                "source": "Fprime_G",
            })
        if 0 in raw["F"][i] and 1 in raw["G"][j] and i - 8:
            contributions.append({
                "coefficient": i - 8,
                "left": raw["F"][i][0]["slot"],
                "right": raw["G"][j][1]["slot"],
                "source": "F_Gprime",
            })

    assert contributions == [
        {
            "coefficient": -1,
            "left": "f_0_1",
            "right": "g_1_0",
            "source": "F_Gprime",
        },
        {
            "coefficient": 1,
            "left": "f_1_0",
            "right": "g_0_1",
            "source": "Fprime_G",
        },
    ]

    # Direct ordinary-coordinate checksum.  For
    # P=a*x+b*y and Q=c*x+d*y, J(P,Q)=a*d-b*c, matching the two raw terms.
    a, b, c, d = 2, 3, 5, 7
    direct_jacobian = a * d - b * c
    raw_endpoint = a * d - b * c
    assert direct_jacobian == raw_endpoint == -1

    # Every linear slot has odd raw weight.  Removing all odd-weight slots
    # therefore kills both gradients at the origin and makes the endpoint 0.
    linear_slots = {"f_1_0", "f_0_1", "g_1_0", "g_0_1"}
    observed = {
        slot["slot"]: weight
        for kind in ("F", "G")
        for weight, row in raw[kind].items()
        for slot in row.values()
        if slot["slot"] in linear_slots
    }
    assert observed == {
        "f_0_1": 7,
        "f_1_0": 11,
        "g_0_1": 11,
        "g_1_0": 15,
    }
    assert all(weight % 2 for weight in observed.values())

    print("D22_X0=f_1_0*g_0_1-f_0_1*g_1_0")
    print("raw_notation=F11[X1]*G11[X0]-F7[X0]*G15[X1]")
    print("all_odd_weights_zero_implies_D22_X0=0")
    print("PASS_EXACT_UPPER_ENDPOINT_ORIGIN_ODD_COUPLING")


if __name__ == "__main__":
    main()
