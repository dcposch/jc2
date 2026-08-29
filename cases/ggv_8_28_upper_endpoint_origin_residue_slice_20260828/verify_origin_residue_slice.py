#!/usr/bin/env python3
"""Exact fixed-slice q/characteristic residue obstruction at D22[X0]."""

from __future__ import annotations

from fractions import Fraction as Q
import hashlib
import importlib.util
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BASE = ROOT / "cases/ggv_8_28_upper_endpoint_branch_p_20260827/compile_endpoint.py"
BASE_SHA256 = "7f840af57695eb0f4e124885a39eabdd0059dad984c917b826d077c77d396be1"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_base():
    assert sha256(BASE) == BASE_SHA256
    spec = importlib.util.spec_from_file_location("origin_residue_base", BASE)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main():
    ce = load_base()
    MV = ce.MV
    z = MV.zero()
    A = (MV.const(-1), z, z, z, MV.const(1))
    Ap = ce.xder(A)

    def varpoly(names):
        return tuple(MV.var(name) if name else z for name in names)

    def t5(poly):
        return ce.xscale(
            ce.xadd(
                ce.xscale(ce.xmul(Ap, poly), 5),
                ce.xscale(ce.xmul(A, ce.xder(poly)), 2),
            ),
            Q(1, 2),
        )

    def div_monic(poly, divisor):
        quotient, remainder = [], list(poly)
        while remainder and not remainder[-1].terms:
            remainder.pop()
        quotient = [z] * max(0, len(remainder) - len(divisor) + 1)
        while len(remainder) >= len(divisor):
            degree = len(remainder) - len(divisor)
            coefficient = remainder[-1]
            quotient[degree] = quotient[degree] + coefficient
            for index, item in enumerate(divisor):
                remainder[degree + index] = remainder[degree + index] - coefficient * item
            while remainder and not remainder[-1].terms:
                remainder.pop()
        return ce.xtrim(quotient), ce.xtrim(remainder)

    # Complete q7/q9/q11/q13 parameterization on
    # A=X^4-1, Q=e=F8=0, r=0.  Literal floors force the omitted primitive
    # coefficients (d9[X1] and k[X1]) to zero.
    d7 = varpoly(("a0", "a1", "a2"))
    d9 = varpoly(("b0", None, "b2", "b3", "b4"))
    k11 = varpoly(("k0", None, "k2"))
    ell13 = MV.var("ell13")

    f = ce.xscale(t5(d7), 4)
    F7 = ce.xmul(A, f)
    F9 = ce.xscale(t5(d9), 4)
    d11 = ce.xmul(A, k11)
    numerator11 = ce.xscale(t5(d11), 4)
    F11, remainder11 = div_monic(numerator11, A)
    assert not remainder11
    d13 = tuple(coefficient * ell13 for coefficient in ce.xpow(A, 2))
    numerator13 = ce.xscale(t5(d13), 4)
    F13, remainder13 = div_monic(numerator13, ce.xpow(A, 2))
    assert not remainder13

    def support(poly):
        return [degree for degree, coefficient in enumerate(poly) if coefficient.terms]

    assert support(F7) == [0, 1, 3, 4, 5, 7, 8, 9]
    assert support(F9) == [1, 2, 3, 5, 6, 7]
    assert support(F11) == [1, 3, 5]
    assert support(F13) == [3]

    c2, c4, c6, c8 = (MV.var(name) for name in ("c2", "c4", "c6", "c8"))

    def scalar(poly, value):
        return tuple(coefficient * value for coefficient in poly)

    def l_add(*items):
        out = {}
        for item in items:
            for exponent, poly in item.items():
                out[exponent] = ce.xadd(out.get(exponent, ()), poly)
                if not out[exponent]:
                    del out[exponent]
        return out

    def l_scale_q(item, value):
        return {
            exponent: ce.xscale(poly, value)
            for exponent, poly in item.items()
            if ce.xscale(poly, value)
        }

    def l_scale_mv(item, value):
        return {
            exponent: scalar(poly, value)
            for exponent, poly in item.items()
            if scalar(poly, value)
        }

    def l_mul(left, right):
        out = {}
        for left_exponent, left_poly in left.items():
            for right_exponent, right_poly in right.items():
                exponent = left_exponent + right_exponent
                out[exponent] = ce.xadd(
                    out.get(exponent, ()), ce.xmul(left_poly, right_poly)
                )
                if not out[exponent]:
                    del out[exponent]
        return out

    def l_shift(item, amount):
        return {exponent + amount: poly for exponent, poly in item.items()}

    F = {weight: {} for weight in range(16)}
    F[0] = {4: (MV.const(1),)}
    F[7], F[9], F[11], F[13] = ({0: item} for item in (F7, F9, F11, F13))

    def fractional_power(exponent):
        out = {0: {int(4 * exponent): (MV.const(1),)}}
        for weight in range(1, 16):
            numerator = {}
            for index in range(1, weight + 1):
                if not F[index]:
                    continue
                numerator = l_add(
                    numerator,
                    l_scale_q(
                        l_mul(F[index], out[weight - index]),
                        (exponent + 1) * index - weight,
                    ),
                )
            out[weight] = l_scale_q(l_shift(numerator, -4), Q(1, weight))
        return out

    powers = {
        exponent: fractional_power(exponent)
        for exponent in (Q(3, 2), Q(5, 4), Q(1), Q(3, 4), Q(1, 2))
    }
    reconstructed_G11 = l_add(
        powers[Q(3, 2)][11],
        l_scale_mv(powers[Q(5, 4)][9], c2),
        l_scale_mv(powers[Q(1)][7], c4),
        l_scale_mv(powers[Q(3, 4)][5], c6),
        l_scale_mv(powers[Q(1, 2)][3], c8),
    )
    reconstructed_G15 = l_add(
        powers[Q(3, 2)][15],
        l_scale_mv(powers[Q(5, 4)][13], c2),
        l_scale_mv(powers[Q(1)][11], c4),
        l_scale_mv(powers[Q(3, 4)][9], c6),
        l_scale_mv(powers[Q(1, 2)][7], c8),
    )
    assert reconstructed_G11 == {
        2: ce.xscale(F11, Q(3, 2)),
        1: ce.xscale(scalar(F9, c2), Q(5, 4)),
        0: scalar(F7, c4),
    }
    assert reconstructed_G15 == {
        1: ce.xscale(scalar(F13, c2), Q(5, 4)),
        0: scalar(F11, c4),
        -1: ce.xscale(scalar(F9, c6), Q(3, 4)),
        -2: ce.xscale(scalar(F7, c8), Q(1, 2)),
    }

    # Complete characteristic coefficients at weights 11 and 15.  Modes
    # c10,c12,c14 do not contribute because F5=F3=F1=0; later modes are
    # unborn.  G15 has one possible A^-1 numerator R.
    G11 = ce.xadd(
        ce.xscale(ce.xmul(ce.xpow(A, 2), F11), Q(3, 2)),
        ce.xadd(
            ce.xscale(scalar(ce.xmul(A, F9), c2), Q(5, 4)),
            scalar(F7, c4),
        ),
    )
    G15_regular = ce.xadd(
        ce.xscale(scalar(ce.xmul(A, F13), c2), Q(5, 4)),
        scalar(F11, c4),
    )
    pole_numerator = ce.xadd(
        ce.xscale(scalar(F9, c6), Q(3, 4)),
        ce.xscale(scalar(f, c8), Q(1, 2)),
    )
    pole_quotient, pole_remainder = div_monic(pole_numerator, A)

    # If G15 is polynomial then pole_remainder=0.  The legal quotient is
    # G15_regular+pole_quotient.  Form the raw origin endpoint before using
    # that divisibility and compare it with the X coefficient of the pole
    # remainder.
    G15 = ce.xadd(G15_regular, pole_quotient)
    endpoint = (
        F11[1] * G11[0]
        - F7[0] * G15[1]
    )
    remainder_x1 = pole_remainder[1]
    identity = endpoint.scale(5) + (F7[0] * remainder_x1).scale(6)
    assert not identity.terms

    expected_factor = ce.MV.var("a1") * (
        ce.MV.var("b2") * c6.scale(3)
        + ce.MV.var("a2") * c8.scale(2)
    )
    assert endpoint == expected_factor.scale(-48)
    assert remainder_x1 == (
        ce.MV.var("b2") * c6.scale(3)
        + ce.MV.var("a2") * c8.scale(2)
    ).scale(10)

    # Polynomiality is coefficientwise pole_remainder=0, hence in
    # particular remainder_x1=0; the identity then forces endpoint=0,
    # contradicting the required target endpoint=1.
    print("q7_q9_q11_q13_parameterization=PASS")
    print("G15_pole_remainder_X1=10*(3*c6*b2+2*c8*a2)")
    print("5*D22_X0+6*F7_X0*G15_pole_remainder_X1=0")
    print("G15_polynomial_implies_D22_X0=0_not_1")
    print("PASS_EXACT_ORIGIN_RESIDUE_SLICE_EXCLUSION")


if __name__ == "__main__":
    main()
