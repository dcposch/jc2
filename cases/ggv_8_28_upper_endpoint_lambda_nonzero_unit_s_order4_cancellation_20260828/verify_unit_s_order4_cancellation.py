#!/usr/bin/env python3
"""Exact sparse check of the unit-S relative-order-four cancellation.

The calculation uses only fractions and a tiny Laurent-polynomial engine.
It has no CAS dependency.
"""

from __future__ import annotations

from fractions import Fraction as F


NAMES = (
    "eps", "L", "K", "B", "J", "H", "C", "D", "tau",
    "c2", "c4", "c6", "c8", "a", "b", "s", "h", "q",
    "r", "v", "p", "w", "u", "delta",
)
POS = {name: index for index, name in enumerate(NAMES)}
ZERO_KEY = (0,) * len(NAMES)


class Poly:
    def __init__(self, terms=None):
        self.terms = {
            key: F(value) for key, value in (terms or {}).items() if value
        }

    @staticmethod
    def constant(value):
        return Poly({ZERO_KEY: F(value)})

    @staticmethod
    def variable(name, power=1):
        key = list(ZERO_KEY)
        key[POS[name]] = power
        return Poly({tuple(key): F(1)})

    def __add__(self, other):
        other = as_poly(other)
        out = dict(self.terms)
        for key, value in other.terms.items():
            out[key] = out.get(key, F(0)) + value
            if not out[key]:
                del out[key]
        return Poly(out)

    __radd__ = __add__

    def __neg__(self):
        return Poly({key: -value for key, value in self.terms.items()})

    def __sub__(self, other):
        return self + (-as_poly(other))

    def __rsub__(self, other):
        return as_poly(other) - self

    def __mul__(self, other):
        other = as_poly(other)
        out = {}
        for left_key, left_value in self.terms.items():
            for right_key, right_value in other.terms.items():
                key = tuple(x + y for x, y in zip(left_key, right_key))
                out[key] = out.get(key, F(0)) + left_value * right_value
        return Poly(out)

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        return self * (F(1) / F(scalar))

    def __pow__(self, exponent):
        assert isinstance(exponent, int) and exponent >= 0
        out = Poly.constant(1)
        base = self
        count = exponent
        while count:
            if count & 1:
                out = out * base
            base = base * base
            count //= 2
        return out

    def truncate_eps(self, bound):
        index = POS["eps"]
        return Poly({
            key: value for key, value in self.terms.items()
            if key[index] <= bound
        })

    def coefficient(self, name, exponent):
        index = POS[name]
        out = {}
        for key, value in self.terms.items():
            if key[index] == exponent:
                new_key = list(key)
                new_key[index] = 0
                out[tuple(new_key)] = value
        return Poly(out)

    def min_power(self, name):
        index = POS[name]
        return min((key[index] for key in self.terms), default=10**9)

    def __eq__(self, other):
        return self.terms == as_poly(other).terms


def as_poly(value):
    return value if isinstance(value, Poly) else Poly.constant(value)


def var(name, power=1):
    return Poly.variable(name, power)


def binomial(alpha, count):
    out = F(1)
    for index in range(count):
        out *= (alpha - index) / (index + 1)
    return out


def fractional_power(alpha, f1, f2, f3, f4, order=4):
    """(L^4+eps*f1+...+eps^4*f4)^alpha through eps^order."""
    assert (4 * alpha).denominator == 1
    base = var("L", int(4 * alpha))
    z = (
        var("eps") * f1 * var("L", -4)
        + var("eps", 2) * f2 * var("L", -4)
        + var("eps", 3) * f3 * var("L", -4)
        + var("eps", 4) * f4 * var("L", -4)
    )
    out = Poly.constant(0)
    z_power = Poly.constant(1)
    for count in range(order + 1):
        out += binomial(alpha, count) * z_power
        z_power = (z_power * z).truncate_eps(order)
    return (base * out).truncate_eps(order)


def characteristic_order4(f1, f2):
    f3, f4 = var("C"), var("D")
    pure = fractional_power(F(3, 2), f1, f2, f3, f4)
    mode2 = (
        var("c2") * var("tau", 2) * var("eps")
        * fractional_power(F(5, 4), f1, f2, f3, f4)
    )
    mode4 = (
        var("c4") * var("tau", 4) * var("eps", 2)
        * fractional_power(F(1), f1, f2, f3, f4)
    )
    mode6 = (
        var("c6") * var("tau", 6) * var("eps", 3)
        * fractional_power(F(3, 4), f1, f2, f3, f4)
    )
    mode8 = (
        var("c8") * var("tau", 8) * var("eps", 4)
        * fractional_power(F(1, 2), f1, f2, f3, f4)
    )
    return (pure + mode2 + mode4 + mode6 + mode8).coefficient("eps", 4)


def evaluate_tau_times_s_power(poly, power):
    """Return s^power*poly(tau=-4a/s); all tau powers must be <= power."""
    out = Poly.constant(0)
    tau_index = POS["tau"]
    for key, value in poly.terms.items():
        degree = key[tau_index]
        assert 0 <= degree <= power
        new_key = list(key)
        new_key[tau_index] = 0
        new_key[POS["a"]] += degree
        new_key[POS["s"]] += power - degree
        out += Poly({tuple(new_key): value * ((-4) ** degree)})
    return out


def main():
    L, K, B = var("L"), var("K"), var("B")
    J, H, C, D = var("J"), var("H"), var("C"), var("D")
    tau = var("tau")
    c2, c4, c6, c8 = (var(name) for name in ("c2", "c4", "c6", "c8"))

    # First verify the complete abstract order-four formula before imposing
    # the stronger determinant lifts.
    generic = characteristic_order4(L**2 * K, B)
    expected = (
        F(3, 2) * L**2 * D
        + F(3, 4) * K * C
        + F(3, 128) * var("L", -2) * (4 * B - K**2) ** 2
        + c2 * tau**2 * (
            F(5, 4) * L * C
            + F(5, 128) * var("L", -1) * K * (8 * B - K**2)
        )
        + c4 * tau**4 * B
        + F(3, 4) * c6 * tau**6 * L * K
        + c8 * tau**8 * L**2
    )
    assert generic == expected
    assert generic.min_power("L") == -2

    # The reviewed D12 root relations strengthen f1 from L^2*K to L^3*J
    # and make f2=L*H.  Every order-four mode is then regular.
    repaired = characteristic_order4(L**3 * J, L * H)
    assert repaired.min_power("L") >= 0

    # Reconstruct the first two normalized F corrections from the literal
    # F0,...,F6 formulas at one simple root.  Here
    # A=eps*(a+b eps+...), S=s+h eps+..., Q=q+r eps+...,
    # U=-s*q/4+v eps+..., P1=p+..., and F6=w+....
    a, b, s, h, q, r = (var(name) for name in ("a", "b", "s", "h", "q", "r"))
    v, p, w, u = (var(name) for name in ("v", "p", "w", "u"))
    face = a + s * tau / 4
    face1 = b + h * tau / 4
    u_root = -s * q / 4

    raw_f1 = (
        4 * face**3 * face1
        - a**3 * q * tau**2 / 8
        + a**2 * (u_root - s * q / 2) * tau**3 / 8
        + a * (-q * s**2 / 128 + s * u_root / 16) * tau**4
        + s**2 * u_root * tau**5 / 128
    )
    raw_f1_expected = face**3 * (4 * face1 - q * tau**2 / 8)
    assert raw_f1 == raw_f1_expected

    c0 = -q * s**2 / 128 + s * u_root / 16
    c1 = -(r * s**2 + 2 * q * s * h) / 128 + (h * u_root + s * v) / 16
    raw_f2 = (
        -(3 * a**2 * b * q + a**3 * r) * tau**2 / 8
        + (2 * a * b * (u_root - s * q / 2)
           + a**2 * (v - (h * q + s * r) / 2)) * tau**3 / 8
        + (b * c0 + a * c1 + a**2 * q**2 / 256) * tau**4
        + ((2 * s * h * u_root + s**2 * v) / 128
           + a * p / 256) * tau**5
        + w * tau**6
    )

    # E(alpha)=0 gives the displayed value of F6(alpha)=w.
    w_root = s * p / 1024 - s**2 * q**2 / 4096
    raw_f2_e = raw_f2 - w * tau**6 + w_root * tau**6
    assert evaluate_tau_times_s_power(raw_f2_e, 6) == 0

    # Two controls: breaking either load-bearing root relation is detected.
    delta = var("delta")
    broken_e = raw_f2_e + delta * tau**6
    assert evaluate_tau_times_s_power(broken_e, 6) == 4096 * a**6 * delta
    strong_residue = evaluate_tau_times_s_power(
        (u_root + delta) * tau - a * q, 1
    )
    assert strong_residue == -4 * a * delta

    print("generic_order4_polar_part=(3/128)L^-2(4B-K^2)^2"
          "+(5*c2*tau^2/128)L^-1*K(8B-K^2)")
    print("D12_strengthening=f1_in_L^3;f2_in_L")
    print("all_modes_relative_order4_regular=true")
    print("mutations=break_L_relation,break_E_relation:EXPECTED_FAIL")
    print("PASS_EXACT_UNIT_S_ORDER4_CANCELLATION")


if __name__ == "__main__":
    main()
