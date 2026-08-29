#!/usr/bin/env python3
"""Exact first-window obstruction for the Q=X odd-tail mutation."""

from __future__ import annotations

from fractions import Fraction as Q
import hashlib
import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
UPSTREAM_REPORT = ROOT / "xmodel/ggv-upper-endpoint-deep-q1-lambda0-even-subbranch-origin-coupling-independent-sol-ultra-20260828.md"
UPSTREAM_REPORT_SHA256 = "c940ba048f5edf60b3018670c8914acc469f55f30101f211a6aedb5d591b6714"
UPSTREAM_CHECKER = ROOT / "cases/ggv_8_28_upper_endpoint_deep_q1_lambda0_even_subbranch_20260828/verify_even_subbranch_reduction.py"
UPSTREAM_CHECKER_SHA256 = "23f46a95170fb77f2f5c340b1c6fb570881062d67102fca6dfdeae2f5ea37c4d"


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_upstream():
    assert sha256(UPSTREAM_REPORT) == UPSTREAM_REPORT_SHA256
    assert sha256(UPSTREAM_CHECKER) == UPSTREAM_CHECKER_SHA256
    spec = importlib.util.spec_from_file_location("even_origin_frozen", UPSTREAM_CHECKER)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def characteristic(up, A, normalized, modes, maximum):
    out = [{} for _ in range(maximum + 1)]
    trajectories = [(0, 6, Q(3, 2), Q(1))]
    trajectories.extend(
        (2 * k, 6 - k, Q(6 - k, 4), value)
        for k, value in enumerate(modes, 1) if value and 2 * k <= maximum
    )
    for shift, a_power, exponent, scalar in trajectories:
        powered = up.la_series_power_one(A, normalized, exponent, maximum - shift)
        prefactor = up.la(A, [Q(1)], a_power)
        for degree, value in enumerate(powered):
            out[degree + shift] = up.la_add(
                A, out[degree + shift],
                up.la_scale(A, scalar, up.la_mul(A, prefactor, value)),
            )
    return out


def polynomial(up, A, element):
    assert not element or min(element) >= 0, element
    out = []
    for exponent, coefficient in element.items():
        out = up.add(out, up.mul(up.power(A, exponent), coefficient))
    return out


def main():
    up = load_upstream()
    A = [Q(-1), Q(0), Q(0), Q(0), Q(1)]
    q = [Q(0), Q(1)]
    f = [Q(-2**29, 75), Q(0), Q(0), Q(0), Q(11 * 2**29, 75)]
    f9 = [Q(0), Q(7 * 2**23, 75), Q(0), Q(0), Q(0), Q(-27 * 2**23, 75)]
    maximum = 21
    normalized = [{} for _ in range(maximum + 1)]
    normalized[0] = up.la(A, [Q(1)])
    normalized[2] = up.la(A, up.scale(Q(-1, 8), q), -1)
    normalized[4] = up.la(A, up.scale(Q(1, 256), up.mul(q, q)), -2)
    normalized[7] = up.la(A, f, -3)
    normalized[9] = up.la(A, f9, -4)

    # Frozen mutation has c2=c6=1 and all other displayed modes zero.
    modes = [Q(1), Q(0), Q(1)] + [Q(0)] * 7
    G = characteristic(up, A, normalized, modes, maximum)
    raw_G = {}
    for weight in range(14):
        raw_G[weight] = polynomial(up, A, G[weight])
    for weight in range(8, 13):
        support = {degree for degree, value in enumerate(raw_G[weight]) if value}
        assert support <= set(up.g_window(weight)), (weight, support)
    expected_g13 = [
        Q(-2**27, 25), Q(0), Q(-2**17, 5), Q(0),
        Q(11 * 2**27, 25), Q(0), Q(2**20, 15),
    ]
    assert raw_G[13] == expected_g13
    assert set(up.g_window(13)) == set(range(1, 12))
    assert raw_G[13][0] == Q(-2**27, 25)
    assert {degree for degree, value in enumerate(raw_G[13]) if value and degree} <= set(up.g_window(13))

    # At this fixed raw F, only the c6 trajectory has an X^0 load in G13.
    labels = ("base", "c2", "c4", "c6", "c8", "c10", "c12")
    constants = {}
    for index, label in enumerate(labels):
        unit_modes = [Q(0)] * 10
        if index:
            unit_modes[index - 1] = Q(1)
        unit_G = characteristic(up, A, normalized, unit_modes, 13)
        unit_g13 = polynomial(up, A, unit_G[13])
        constants[label] = unit_g13[0] if unit_g13 else Q(0)
    assert constants == {
        "base": Q(0), "c2": Q(0), "c4": Q(0),
        "c6": Q(-2**27, 25), "c8": Q(0),
        "c10": Q(0), "c12": Q(0),
    }

    # Characteristic coefficients make every determinant row through D13
    # vanish even though the literal receiver floor rejects G13[X^0].
    raw_F = {
        0: up.power(A, 4),
        1: [],
        2: up.scale(Q(-1, 8), up.mul(up.power(A, 3), q)),
        3: [],
        4: up.scale(Q(1, 256), up.mul(up.power(A, 2), up.mul(q, q))),
        5: [], 6: [], 7: up.mul(A, f), 8: [], 9: f9,
        10: [], 11: [], 12: [], 13: [],
    }
    rows = up.original_rows(raw_F, raw_G)
    assert all(not rows[weight] for weight in range(14))

    # The only scalar-mode repair at G13 is c6=0.  It repairs G13 but the
    # unchanged even tail then meets a genuine A^-1 pole at G14.
    repaired_modes = [Q(1)] + [Q(0)] * 9
    repaired = characteristic(up, A, normalized, repaired_modes, maximum)
    repaired_g13 = polynomial(up, A, repaired[13])
    assert {degree for degree, value in enumerate(repaired_g13) if value} <= set(up.g_window(13))
    assert min(repaired[14]) == -1
    assert repaired[14][-1] == [Q(0)] * 6 + [Q(-5, 2**34)]

    # Mutation controls.
    restore_c6 = characteristic(up, A, normalized, modes, 13)
    assert polynomial(up, A, restore_c6[13])[0] == Q(-2**27, 25)
    assert Q(-5, 2**34) != 0

    print("G8_G12_polynomial_literal_windows=PASS")
    print("earliest_failure=G13_X0=-2^27/25")
    print("G13_X0_mode_decomposition=sole_c6")
    print("D0_D13_characteristic_rows=0")
    print("c6_zero_repairs_G13_but_next_failure=G14_A^-1*(-5*X^6/2^34)")
    print("PASS_EXACT_QX_G13_OBSTRUCTION")


if __name__ == "__main__":
    main()
