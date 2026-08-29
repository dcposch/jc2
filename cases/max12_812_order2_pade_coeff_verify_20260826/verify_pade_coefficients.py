#!/usr/bin/env python3
"""AWS-only exact verifier for the three Laurent coefficients in the Padé lemma."""

from __future__ import annotations

from fractions import Fraction
import os
from pathlib import Path
import platform


Exponent = tuple[int, int, int]  # p,c,r
Poly = dict[Exponent, Fraction]
ZERO: Poly = {}
ONE: Poly = {(0, 0, 0): Fraction(1)}


def clean(poly: Poly) -> Poly:
    return {monomial: coefficient for monomial, coefficient in poly.items() if coefficient}


def add(*polys: Poly) -> Poly:
    out: Poly = {}
    for poly in polys:
        for monomial, coefficient in poly.items():
            out[monomial] = out.get(monomial, Fraction(0)) + coefficient
    return clean(out)


def scale(coefficient: Fraction | int, poly: Poly) -> Poly:
    value = Fraction(coefficient)
    return clean({monomial: value * entry for monomial, entry in poly.items()})


def multiply(left: Poly, right: Poly) -> Poly:
    out: Poly = {}
    for lm, lc in left.items():
        for rm, rc in right.items():
            monomial = tuple(a + b for a, b in zip(lm, rm))
            out[monomial] = out.get(monomial, Fraction(0)) + lc * rc
    return clean(out)


def power(poly: Poly, exponent: int) -> Poly:
    if exponent < 0:
        raise ValueError(exponent)
    out = ONE
    base = poly
    value = exponent
    while value:
        if value & 1:
            out = multiply(out, base)
        base = multiply(base, base)
        value >>= 1
    return out


def require_zero(label: str, poly: Poly) -> None:
    if clean(poly):
        raise RuntimeError((label, clean(poly)))
    print(f"{label}=PASS")


def require_aws() -> str:
    if platform.system() != "Linux":
        raise RuntimeError("AWS-only verifier refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        raise RuntimeError("AWS-only verifier refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        raise RuntimeError("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def main() -> None:
    tag = require_aws()
    p: Poly = {(1, 0, 0): Fraction(1)}
    c: Poly = {(0, 1, 0): Fraction(1)}
    r: Poly = {(0, 0, 1): Fraction(1)}
    d = add(power(p, 2), scale(-4, r))

    # If Y=(1+p*t^2+c*t^3+r*t^4)^(7/2)=sum a_n*t^n, then
    # S*Y'=(7/2)S'*Y gives this exact recurrence.
    coeff: list[Poly] = [ZERO for _ in range(18)]
    coeff[0] = ONE
    for n in range(1, 18):
        numerator = ZERO
        if n >= 2:
            numerator = add(numerator, scale(9 - n, multiply(p, coeff[n - 2])))
        if n >= 3:
            numerator = add(
                numerator,
                scale(Fraction(27, 2) - n, multiply(c, coeff[n - 3])),
            )
        if n >= 4:
            numerator = add(numerator, scale(18 - n, multiply(r, coeff[n - 4])))
        coeff[n] = scale(Fraction(1, n), numerator)

    c2 = power(c, 2)
    c4 = power(c, 4)
    d2 = power(d, 2)
    d3 = power(d, 3)
    d4 = power(d, 4)
    p2 = power(p, 2)

    A0 = add(scale(-5, d3), scale(40, multiply(multiply(p, c2), d)), scale(-8, c4))
    C0 = add(
        d4,
        scale(-48, multiply(multiply(p, c2), d2)),
        scale(32, multiply(c4, add(d, scale(2, p2)))),
    )
    B0 = add(
        scale(5, multiply(p, d3)),
        scale(-10, multiply(multiply(c2, d), add(d, scale(4, p2)))),
        scale(24, multiply(p, c4)),
    )

    require_zero("PADE_T15_FACTOR", add(coeff[15], scale(Fraction(-7, 2048), multiply(c, A0))))
    require_zero("PADE_T16_FACTOR", add(coeff[16], scale(Fraction(-35, 32768), C0)))
    require_zero("PADE_T17_FACTOR", add(coeff[17], scale(Fraction(-7, 4096), multiply(c, B0))))

    e1 = add(scale(8, multiply(p, c2)), scale(-5, d2))
    e2 = add(scale(2, c4), scale(-5, d3))
    require_zero(
        "PADE_B_PLUS_P_A",
        add(B0, multiply(p, A0), scale(-2, multiply(c2, add(scale(-5, d2), scale(8, multiply(p, c2)))))),
    )
    require_zero(
        "PADE_C_REDUCTION_76",
        add(
            C0,
            scale(-76, d4),
            scale(-1, power(e1, 2)),
            scale(-4, multiply(d2, e1)),
            scale(-16, multiply(d, e2)),
        ),
    )

    print(f"PADE_REGISTERED_TAG={tag}")
    print("PADE_EXACT_COEFFICIENT_VERIFIER=PASS")
    print("PADE_SCOPE=COEFFICIENT_IDENTITIES_ONLY_NO_SCHEME_OR_ORDER2_VERDICT")


if __name__ == "__main__":
    main()
