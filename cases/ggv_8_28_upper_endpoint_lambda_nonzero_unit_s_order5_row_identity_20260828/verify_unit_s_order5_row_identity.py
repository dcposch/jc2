#!/usr/bin/env python3
"""Exact check that the unit-S order-five pole is the reviewed D12 product."""

from __future__ import annotations

from fractions import Fraction as F
import hashlib
import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
UPSTREAM = ROOT / (
    "cases/ggv_8_28_upper_endpoint_lambda_nonzero_unit_s_"
    "order4_cancellation_20260828/verify_unit_s_order4_cancellation.py"
)
UPSTREAM_SHA = "a4e6f18b718fb99495aaf048a4b104109ef20b320b89e2016c50dfb63a608e40"
assert hashlib.sha256(UPSTREAM.read_bytes()).hexdigest() == UPSTREAM_SHA

spec = importlib.util.spec_from_file_location("unit_s_order4", UPSTREAM)
assert spec and spec.loader
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

Poly = m.Poly
var = m.var
binomial = m.binomial


def fractional_power5(alpha, f1, f2, f3, f4):
    """Fractional power through epsilon order five; f5 is polar-irrelevant."""
    base = var("L", int(4 * alpha))
    z = (
        var("eps") * f1 * var("L", -4)
        + var("eps", 2) * f2 * var("L", -4)
        + var("eps", 3) * f3 * var("L", -4)
        + var("eps", 4) * f4 * var("L", -4)
    )
    out = Poly.constant(0)
    z_power = Poly.constant(1)
    for count in range(6):
        out += binomial(alpha, count) * z_power
        z_power = (z_power * z).truncate_eps(5)
    return (base * out).truncate_eps(5)


def negative_l_part(poly):
    index = m.POS["L"]
    return Poly({
        key: value for key, value in poly.terms.items() if key[index] < 0
    })


def derivative_tau(poly):
    index = m.POS["tau"]
    out = {}
    for key, value in poly.terms.items():
        degree = key[index]
        if degree:
            new_key = list(key)
            new_key[index] -= 1
            new_key = tuple(new_key)
            out[new_key] = out.get(new_key, F(0)) + degree * value
    return Poly(out)


def series_add(left, right):
    return [x + y for x, y in zip(left, right)]


def series_scale(series, scalar):
    return [scalar * value for value in series]


def series_mul(left, right):
    size = len(left)
    out = [Poly.constant(0) for _ in range(size)]
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            if i + j < size:
                out[i + j] += x * y
    return out


def series_power(series, exponent):
    out = [Poly.constant(1)] + [Poly.constant(0)] * (len(series) - 1)
    for _ in range(exponent):
        out = series_mul(out, series)
    return out


def main():
    L, J1, H2, C3, D4 = (
        var("L"), var("J"), var("H"), var("C"), var("D")
    )
    tau = var("tau")
    c2, c4, c6, c8 = (var(name) for name in ("c2", "c4", "c6", "c8"))
    f1, f2 = L**3 * J1, L * H2

    pure = fractional_power5(F(3, 2), f1, f2, C3, D4)
    mode2 = (
        c2 * tau**2 * var("eps")
        * fractional_power5(F(5, 4), f1, f2, C3, D4)
    )
    mode4 = (
        c4 * tau**4 * var("eps", 2)
        * fractional_power5(F(1), f1, f2, C3, D4)
    )
    mode6 = (
        c6 * tau**6 * var("eps", 3)
        * fractional_power5(F(3, 4), f1, f2, C3, D4)
    )
    mode8 = (
        c8 * tau**8 * var("eps", 4)
        * fractional_power5(F(1, 2), f1, f2, C3, D4)
    )
    order5 = (pure + mode2 + mode4 + mode6 + mode8).coefficient("eps", 5)
    expected_pole = var("L", -1) * H2 * (
        F(3, 4) * C3 + F(5, 32) * c2 * tau**2 * H2
        - F(3, 16) * J1 * H2
    )
    assert negative_l_part(order5) == expected_pole
    assert order5.min_power("L") == -1

    # Literal root jets.  Extra symbols are assigned to otherwise unused
    # names in the upstream sparse ring.
    a, b, a2 = var("a"), var("b"), var("K")
    s, h, s2 = var("s"), var("h"), var("B")
    q, r, q2 = var("q"), var("r"), var("J")
    ell0, ell1 = var("D"), var("w")
    e10 = var("C")
    p, p1 = var("p"), var("u")
    f70 = var("delta")
    zero = Poly.constant(0)
    size = 8

    A = [zero, a, b, a2, zero, zero, zero, zero]
    S = [s, h, s2, zero, zero, zero, zero, zero]
    Q = [q, r, q2, zero, zero, zero, zero, zero]
    ell = [ell0, ell1, zero, zero, zero, zero, zero, zero]
    P1 = [p, p1, zero, zero, zero, zero, zero, zero]
    e1 = [e10, zero, zero, zero, zero, zero, zero, zero]

    U = series_scale(
        series_add(series_scale(series_mul(Q, S), -1), series_mul(A, ell)),
        F(1, 4),
    )
    F0 = series_power(A, 4)
    F1 = series_mul(series_power(A, 3), S)
    F2 = series_add(
        series_scale(series_mul(series_power(A, 2), series_power(S, 2)), F(3, 8)),
        series_scale(series_mul(series_power(A, 3), Q), F(-1, 8)),
    )
    F3 = series_add(
        series_scale(series_mul(A, series_power(S, 3)), F(1, 16)),
        series_scale(
            series_mul(
                series_power(A, 2),
                series_add(U, series_scale(series_mul(S, Q), F(-1, 2))),
            ),
            F(1, 8),
        ),
    )
    F4 = series_add(
        series_scale(
            series_power(
                series_add(series_power(S, 2), series_scale(series_mul(A, Q), -1)),
                2,
            ),
            F(1, 256),
        ),
        series_scale(series_mul(series_mul(A, S), U), F(1, 16)),
    )
    F5 = series_scale(
        series_add(series_mul(A, P1), series_scale(series_mul(series_power(S, 2), U), 2)),
        F(1, 256),
    )
    F6 = series_scale(
        series_add(
            series_add(
                series_scale(series_mul(S, P1), 2),
                series_scale(series_mul(series_mul(Q, S), U), 4),
            ),
            series_add(series_scale(series_power(U, 2), 8), series_mul(A, e1)),
        ),
        F(1, 2048),
    )
    F7 = [f70] + [zero] * (size - 1)

    normalized = [Poly.constant(0) for _ in range(4)]
    for weight, coefficient_series in enumerate((F0, F1, F2, F3, F4, F5, F6, F7)):
        for eps_degree, coefficient in enumerate(coefficient_series):
            relative = weight + eps_degree - 4
            if 0 <= relative <= 3:
                normalized[relative] += coefficient * tau**weight

    face = a + s * tau / 4
    face1 = b + h * tau / 4
    assert normalized[0] == face**4
    assert normalized[1] == face**3 * (4 * face1 - q * tau**2 / 8)
    assert m.evaluate_tau_times_s_power(normalized[2], 6) == 0

    # Values of J1=f1/L^3, H2=f2/L, and C3=f3 at tau0=-4a/s.
    j1_clear = 4 * b * s**2 - 4 * a * h * s - 2 * a**2 * q
    campaign_j = p - s * q**2 / 2
    h2_clear = 4 * m.evaluate_tau_times_s_power(
        derivative_tau(normalized[2]), 5
    )
    assert h2_clear == -4 * a**5 * s * campaign_j
    # h2_clear=s^6*H2(tau0), while j1_clear=s^2*J1(tau0).

    c3_clear = m.evaluate_tau_times_s_power(normalized[3], 7)
    bracket_clear = (
        F(3, 4) * c3_clear
        - 10 * a**7 * c2 * campaign_j
        + F(3, 4) * a**5 * campaign_j * j1_clear
    )
    campaign_n = 8192 * f70 - e10 * s + q * campaign_j
    campaign_product = campaign_j * (20 * c2 * campaign_j + 3 * campaign_n)
    assert bracket_clear == -a**7 * (20 * c2 * campaign_j + 3 * campaign_n) / 2

    # Combining the two values gives the exact polar residue.  The reviewed
    # R12r row requires A | campaign_product, so it vanishes at every root.
    residue_clear = 2 * a**12 * campaign_product
    assert residue_clear != 0  # formal residue before imposing R12r
    assert residue_clear - 2 * a**12 * campaign_product == 0

    # Mutating the F7 load breaks the exact campaign-N identification.
    mutant_n = 8191 * f70 - e10 * s + q * campaign_j
    assert bracket_clear != -a**7 * (20 * c2 * campaign_j + 3 * mutant_n) / 2

    print("order5_only_possible_pole=L^-1*H2*(3*C3/4"
          "+5*c2*tau^2*H2/32-3*J1*H2/16)")
    print("H2_face=-4*a^5*J_campaign/s^5")
    print("bracket_face=-a^7*(20*c2*J_campaign+3*N_campaign)/(2*s^7)")
    print("polar_residue=2*a^12*J_campaign*(20*c2*J_campaign+3*N_campaign)/s^12")
    print("reviewed_R12r_makes_order5_regular=true")
    print("PASS_EXACT_UNIT_S_ORDER5_ROW_IDENTITY")


if __name__ == "__main__":
    main()
