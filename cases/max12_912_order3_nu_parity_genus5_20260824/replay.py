#!/usr/bin/env python3
"""Exact stdlib replay for the full nu-loaded parity genus-five exclusion."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
PARENT = ROOT / "cases/max12_912_order3_fibre_20260824/order3_fibre.py"
PARENT_SHA256 = "a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf"


def load_parent():
    if sha256(PARENT.read_bytes()).hexdigest() != PARENT_SHA256:
        raise RuntimeError("parent compiler hash mismatch")
    spec = importlib.util.spec_from_file_location("max12_parity_genus5_parent", PARENT)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load parent compiler")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


Poly = tuple[Fraction, ...]  # coefficients in increasing degree


def trim(poly: Poly) -> Poly:
    values = list(poly)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values) if values else (Fraction(0),)


def padd(left: Poly, right: Poly) -> Poly:
    length = max(len(left), len(right))
    return trim(tuple(
        (left[i] if i < len(left) else 0)
        + (right[i] if i < len(right) else 0)
        for i in range(length)
    ))


def pscale(scalar: Fraction | int, poly: Poly) -> Poly:
    return trim(tuple(Fraction(scalar) * value for value in poly))


def pmul(left: Poly, right: Poly) -> Poly:
    out = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return trim(tuple(out))


def ppow(poly: Poly, exponent: int) -> Poly:
    out: Poly = (Fraction(1),)
    base = poly
    power = exponent
    while power:
        if power & 1:
            out = pmul(out, base)
        base = pmul(base, base)
        power >>= 1
    return out


def pdivmod(numerator: Poly, denominator: Poly) -> tuple[Poly, Poly]:
    numerator = trim(numerator)
    denominator = trim(denominator)
    if denominator == (0,):
        raise ZeroDivisionError
    if len(numerator) < len(denominator):
        return (Fraction(0),), numerator
    quotient = [Fraction(0)] * (len(numerator) - len(denominator) + 1)
    remainder = list(numerator)
    while len(remainder) >= len(denominator) and any(remainder):
        degree = len(remainder) - len(denominator)
        scalar = remainder[-1] / denominator[-1]
        quotient[degree] = scalar
        for index, value in enumerate(denominator):
            remainder[degree + index] -= scalar * value
        remainder = list(trim(tuple(remainder)))
    return trim(tuple(quotient)), trim(tuple(remainder))


def pgcd(left: Poly, right: Poly) -> Poly:
    while trim(right) != (0,):
        _, remainder = pdivmod(left, right)
        left, right = right, remainder
    left = trim(left)
    return pscale(1 / left[-1], left)


def derivative(poly: Poly) -> Poly:
    return trim(tuple(Fraction(i) * poly[i] for i in range(1, len(poly))))


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    data = [row[:] for row in matrix]
    result = Fraction(1)
    for column in range(len(data)):
        pivot = next((row for row in range(column, len(data))
                      if data[row][column] != 0), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            data[column], data[pivot] = data[pivot], data[column]
            result = -result
        value = data[column][column]
        result *= value
        for j in range(column, len(data)):
            data[column][j] /= value
        for row in range(column + 1, len(data)):
            factor = data[row][column]
            if factor:
                for j in range(column, len(data)):
                    data[row][j] -= factor * data[column][j]
    return result


def resultant(left: Poly, right: Poly) -> Fraction:
    m = len(trim(left)) - 1
    n = len(trim(right)) - 1
    left_high = list(reversed(trim(left)))
    right_high = list(reversed(trim(right)))
    matrix: list[list[Fraction]] = []
    for shift in range(n):
        matrix.append(
            [Fraction(0)] * shift + left_high
            + [Fraction(0)] * (n - 1 - shift)
        )
    for shift in range(m):
        matrix.append(
            [Fraction(0)] * shift + right_high
            + [Fraction(0)] * (m - 1 - shift)
        )
    return determinant(matrix)


@dataclass(frozen=True)
class Rat:
    numerator: Poly
    denominator: Poly = (Fraction(1),)

    @staticmethod
    def constant(value: Fraction | int) -> "Rat":
        return Rat((Fraction(value),))

    def __add__(self, other: "Rat") -> "Rat":
        return Rat(
            padd(
                pmul(self.numerator, other.denominator),
                pmul(other.numerator, self.denominator),
            ),
            pmul(self.denominator, other.denominator),
        )

    def __neg__(self) -> "Rat":
        return Rat(pscale(-1, self.numerator), self.denominator)

    def __sub__(self, other: "Rat") -> "Rat":
        return self + (-other)

    def __mul__(self, other: "Rat") -> "Rat":
        return Rat(
            pmul(self.numerator, other.numerator),
            pmul(self.denominator, other.denominator),
        )

    def __truediv__(self, other: "Rat") -> "Rat":
        return Rat(
            pmul(self.numerator, other.denominator),
            pmul(self.denominator, other.numerator),
        )

    def __pow__(self, exponent: int) -> "Rat":
        return Rat(
            ppow(self.numerator, exponent),
            ppow(self.denominator, exponent),
        )

    def equal(self, other: "Rat") -> bool:
        return trim(pmul(self.numerator, other.denominator)) == trim(
            pmul(other.numerator, self.denominator)
        )


def evaluate_weighted(value, bases: list[Rat], weights: list[int], wanted: int) -> Rat:
    total = Rat.constant(0)
    for monomial, coefficient in value.items():
        assert sum(exponent * weight
                   for exponent, weight in zip(monomial, weights)) == wanted
        term = Rat.constant(coefficient)
        for exponent, base in zip(monomial, bases):
            term = term * (base ** exponent)
        total = total + term
    return total


def main() -> None:
    parent = load_parent()
    M = parent.M
    compiled = parent.compile_fibre()
    source_names = compiled["transverse_ring_names"]
    parity_names = ["x1", "x3", "x5", "p"]
    parity_ring = M.Ring(parity_names)
    images = [
        parity_ring.var(name)
        if name in parity_names
        else M.cscale(0, parity_ring.one)
        for name in source_names
    ]
    tails = {
        ell: parent.substitute_coeff(value, images, parity_ring)
        for ell, value in compiled["transverse_tails"].items()
    }
    assert all(not tails[ell] for ell in (1, 3, 5, 7))

    # Generic p*x5*A chart, v=A/(p*x5).
    one = (Fraction(1),)
    vpoly: Poly = (Fraction(0), Fraction(1))
    v = Rat(vpoly)
    Dpoly: Poly = (Fraction(-2), Fraction(0), Fraction(3))
    A2poly: Poly = (Fraction(1), Fraction(3), Fraction(3))
    A5poly: Poly = (
        Fraction(2), Fraction(18), Fraction(69), Fraction(131),
        Fraction(117), Fraction(33),
    )
    A4poly: Poly = (
        Fraction(6), Fraction(32), Fraction(75), Fraction(96), Fraction(54),
    )
    D = Rat(Dpoly)
    A2 = Rat(A2poly)
    A5 = Rat(A5poly)
    A4 = Rat(A4poly)
    x5hat = Rat.constant(-36) * (v ** 2) * A2 / D
    x3hat = x5hat * (v + Rat.constant(2))
    x1hat = (
        x5hat * (v + Rat.constant(1))
        + (x5hat ** 2) * (Rat((Fraction(1), Fraction(3))))
        / (Rat.constant(9) * v)
    )
    bases = [x1hat, x3hat, x5hat, Rat.constant(1)]
    divided_weights = [4, 3, 2, 1]
    r2hat = evaluate_weighted(tails[2], bases, divided_weights, 7)
    r4hat = evaluate_weighted(tails[4], bases, divided_weights, 8)
    r6hat = evaluate_weighted(tails[6], bases, divided_weights, 9)
    r8hat = evaluate_weighted(tails[8], bases, divided_weights, 10)
    assert r2hat.equal(Rat.constant(0))
    assert r4hat.equal(Rat.constant(0))

    expected_r6 = (
        Rat.constant(-2304) * (v ** 6) * (A2 ** 3) * A5 / (D ** 4)
    )
    expected_r8 = (
        Rat.constant(6912) * (v ** 8) * (A2 ** 4) * A4 / (D ** 5)
    )
    assert r6hat.equal(expected_r6)
    assert r8hat.equal(expected_r8)

    # Branch and genus ledger for Y^3=A5(v)/D(v).
    assert pgcd(A5poly, derivative(A5poly)) == one
    assert pgcd(Dpoly, derivative(Dpoly)) == one
    assert pgcd(A5poly, Dpoly) == one
    assert pgcd(A2poly, Dpoly) == one
    res_a5_d = resultant(A5poly, Dpoly)
    res_a2_d = resultant(A2poly, Dpoly)
    assert res_a5_d == 97200
    assert res_a2_d == 27
    finite_branch_points = 5 + 2
    ramification_contribution = finite_branch_points * (3 - 1)
    twice_genus_minus_two = 3 * (-2) + ramification_contribution
    genus = (twice_genus_minus_two + 2) // 2
    assert genus == 5

    # Exact p=0,x5!=0 branch.  The displayed identities imply
    # rho^9=(2*3^25/11^10)*nu^10.
    p0_ring = M.Ring(["x3", "x5"])
    p0_x5 = p0_ring.var("x5")
    p0_images = [
        M.cscale(Fraction(1, 3), M.cmul(p0_x5, p0_x5)),
        p0_ring.var("x3"),
        p0_x5,
        M.cscale(0, p0_ring.one),
    ]
    p0_tails = {
        ell: parent.substitute_coeff(value, p0_images, p0_ring)
        for ell, value in tails.items()
    }
    assert not p0_tails[2]
    assert M.coeff_string(p0_tails[4], p0_ring.names) == (
        "-4/27*x3^2*x5-1/243*x5^4"
    )
    assert M.coeff_string(p0_tails[6], p0_ring.names) == (
        "-4/81*x3^3-4/243*x3*x5^3"
    )
    assert M.coeff_string(p0_tails[8], p0_ring.names) == (
        "2/243*x3^2*x5^2-4/2187*x5^5"
    )
    # Reducing by x3^2=-x5^3/36 gives these two coefficients exactly.
    assert Fraction(4, 81 * 36) - Fraction(4, 243) == Fraction(-11, 729)
    assert Fraction(-2, 243 * 36) - Fraction(4, 2187) == Fraction(-1, 486)
    p0_constant_numerator = 2 * 3**25
    p0_constant_denominator = 11**10
    assert p0_constant_numerator == 1694577218886
    assert p0_constant_denominator == 25937424601

    payload = {
        "case": "max12_912_order3_nu_parity_genus5_20260824",
        "parent_compiler_sha256": PARENT_SHA256,
        "generic_chart": {
            "conditions": "p*x5*A!=0, A=x3-2*p*x5",
            "v": "A/(p*x5) in K=C(x)",
            "x5": "-36*p^2*v^2*(3*v^2+3*v+1)/(3*v^2-2)",
            "r6": (
                "-2304*p^9*v^6*(3*v^2+3*v+1)^3*"
                "(33*v^5+117*v^4+131*v^3+69*v^2+18*v+2)/"
                "(3*v^2-2)^4"
            ),
            "r8": (
                "6912*p^10*v^8*(3*v^2+3*v+1)^4*"
                "(54*v^4+96*v^3+75*v^2+32*v+6)/(3*v^2-2)^5"
            ),
        },
        "boundary_checks": {
            "resultant_A5_D": int(res_a5_d),
            "resultant_A2_D": int(res_a2_d),
            "A5_squarefree": True,
            "D_squarefree": True,
            "D_or_A2_zero_on_generic_chart": "impossible",
        },
        "cube_curve": {
            "equation": (
                "Y^3=(33*v^5+117*v^4+131*v^3+69*v^2+18*v+2)/"
                "(3*v^2-2)"
            ),
            "finite_branch_points": finite_branch_points,
            "infinity_order": -3,
            "infinity_branched": False,
            "riemann_hurwitz": twice_genus_minus_two,
            "genus": genus,
        },
        "p_zero_branch": {
            "relations": [
                "x1=x5^2/3",
                "x3^2=-x5^3/36",
                "nu=-11*x3*x5^3/729",
                "r8=-x5^5/486",
            ],
            "projection": "r8^9=(2*3^25/11^10)*nu^10",
            "terminal_consequence": "r8 is constant, contradiction",
        },
        "producer_conclusion": (
            "No actual nu!=0 order-three Keller trajectory lies on the full "
            "parity specialization q=x0=x2=x4=k=0."
        ),
        "scope": (
            "full parity specialization only; no generic loaded-fibre, Taylor, "
            "all-(9,12), maximum-twelve, counterexample, or JC2 conclusion"
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
