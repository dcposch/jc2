#!/usr/bin/env python3
"""Producer-internal exact jet probe for the non-parity Q12 branch.

This scratch file is outside every frozen manifest.  It works in the quotient
Q[v]/(Q12), fixes the normalization p=1 and the local parameter t=a0, and
solves the seven fibre rows through odd order three/even order two.  It then
pulls back r8 through order two.  No trajectory conclusion is made.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
import importlib.util
from itertools import permutations
from math import gcd
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
PARENT = ROOT / "cases/max12_912_order3_fibre_20260824/order3_fibre.py"
GENUS = ROOT / "cases/max12_912_order3_nu_parity_genus5_20260824/replay.py"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


P = load("q12_jet_parent", PARENT)
G = load("q12_jet_genus", GENUS)
M = P.M
MOD = G.pscale(
    Fraction(1, 2893401),
    (
        Fraction(480), Fraction(4688), Fraction(8664), Fraction(4608),
        Fraction(111060), Fraction(391932), Fraction(-503280),
        Fraction(-5322618), Fraction(-12251574), Fraction(-12217797),
        Fraction(-2488077), Fraction(4809213), Fraction(2893401),
    ),
)


def psub(left, right):
    return G.padd(left, G.pscale(-1, right))


def preduce(poly):
    return G.pdivmod(G.trim(poly), MOD)[1]


def pinverse(poly):
    r0, r1 = MOD, preduce(poly)
    s0, s1 = (Fraction(0),), (Fraction(1),)
    while G.trim(r1) != (Fraction(0),):
        quotient, remainder = G.pdivmod(r0, r1)
        r0, r1 = r1, remainder
        s0, s1 = s1, psub(s0, G.pmul(quotient, s1))
    r0 = G.trim(r0)
    if len(r0) != 1 or r0[0] == 0:
        raise ZeroDivisionError(poly)
    return preduce(G.pscale(1 / r0[0], s0))


@dataclass(frozen=True)
class NF:
    poly: tuple[Fraction, ...]

    def __init__(self, value=0):
        if isinstance(value, NF):
            poly = value.poly
        elif isinstance(value, tuple):
            poly = tuple(Fraction(item) for item in value)
        else:
            poly = (Fraction(value),)
        object.__setattr__(self, "poly", preduce(poly))

    def __add__(self, other):
        return NF(G.padd(self.poly, NF(other).poly))

    __radd__ = __add__

    def __neg__(self):
        return NF(G.pscale(-1, self.poly))

    def __sub__(self, other):
        return self + (-NF(other))

    def __rsub__(self, other):
        return NF(other) - self

    def __mul__(self, other):
        return NF(G.pmul(self.poly, NF(other).poly))

    __rmul__ = __mul__

    def inverse(self):
        if not self:
            raise ZeroDivisionError
        return NF(pinverse(self.poly))

    def __truediv__(self, other):
        return self * NF(other).inverse()

    def __rtruediv__(self, other):
        return NF(other) / self

    def __pow__(self, exponent):
        if exponent < 0:
            return (self.inverse()) ** (-exponent)
        out = NF(1)
        base = self
        power = exponent
        while power:
            if power & 1:
                out = out * base
            base = base * base
            power >>= 1
        return out

    def __bool__(self):
        return self.poly != (Fraction(0),)


ZERO = NF(0)
ONE = NF(1)


@dataclass(frozen=True)
class Series:
    coefficients: tuple[NF, ...]

    def __init__(self, coefficients=()):
        values = [NF(value) for value in coefficients]
        values.extend([ZERO] * (4 - len(values)))
        object.__setattr__(self, "coefficients", tuple(values[:4]))

    @staticmethod
    def constant(value):
        return Series((NF(value),))

    def __add__(self, other):
        other = other if isinstance(other, Series) else Series.constant(other)
        return Series(tuple(a + b for a, b in zip(self.coefficients, other.coefficients)))

    __radd__ = __add__

    def __neg__(self):
        return Series(tuple(-value for value in self.coefficients))

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        other = other if isinstance(other, Series) else Series.constant(other)
        out = [ZERO] * 4
        for left_degree, left in enumerate(self.coefficients):
            for right_degree, right in enumerate(other.coefficients):
                if left_degree + right_degree < 4:
                    out[left_degree + right_degree] = (
                        out[left_degree + right_degree] + left * right
                    )
        return Series(tuple(out))

    __rmul__ = __mul__

    def __pow__(self, exponent):
        out = Series.constant(1)
        base = self
        power = exponent
        while power:
            if power & 1:
                out = out * base
            base = base * base
            power >>= 1
        return out


def nf_eval(value, bases):
    total = ZERO
    powers = []
    for index, base in enumerate(bases):
        highest = max((monomial[index] for monomial in value), default=0)
        row = [ONE]
        for _ in range(highest):
            row.append(row[-1] * base)
        powers.append(row)
    for monomial, coefficient in value.items():
        term = NF(coefficient)
        for index, exponent in enumerate(monomial):
            term = term * powers[index][exponent]
        total = total + term
    return total


def series_eval(value, bases):
    total = Series.constant(0)
    powers = []
    for index, base in enumerate(bases):
        highest = max((monomial[index] for monomial in value), default=0)
        row = [Series.constant(1)]
        for _ in range(highest):
            row.append(row[-1] * base)
        powers.append(row)
    for monomial, coefficient in value.items():
        term = Series.constant(coefficient)
        for index, exponent in enumerate(monomial):
            term = term * powers[index][exponent]
        total = total + term
    return total


def solve(matrix, rhs):
    size = len(matrix)
    data = [list(row) + [rhs[index]] for index, row in enumerate(matrix)]
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if data[row][column]),
            None,
        )
        if pivot is None:
            raise RuntimeError(("singular linear system", column))
        data[column], data[pivot] = data[pivot], data[column]
        scale = data[column][column].inverse()
        data[column] = [value * scale for value in data[column]]
        for row in range(size):
            if row == column:
                continue
            factor = data[row][column]
            if factor:
                data[row] = [
                    value - factor * pivot_value
                    for value, pivot_value in zip(data[row], data[column])
                ]
    return [data[index][-1] for index in range(size)]


def nf_determinant(matrix):
    out = ZERO
    size = len(matrix)
    for permutation in permutations(range(size)):
        inversions = sum(
            1 for i in range(size) for j in range(i + 1, size)
            if permutation[i] > permutation[j]
        )
        term = ONE
        for row, column in enumerate(permutation):
            term = term * matrix[row][column]
        out = out + (-term if inversions % 2 else term)
    return out


def canonical_digest(value):
    encoded = ",".join(
        f"{coefficient.numerator}/{coefficient.denominator}"
        for coefficient in value.poly
    )
    return {
        "degree": len(value.poly) - 1,
        "nonzero": bool(value),
        "sha256": sha256(encoded.encode()).hexdigest(),
    }


def make_series(base, n1, unknowns):
    p2, x1_2, x3_2, x5_2, a2_3, a4_3, a6_3 = unknowns
    p = Series((ONE, ZERO, p2))
    values = [
        Series((ZERO, ONE)),
        Series((base[1], ZERO, x1_2)),
        Series((ZERO, n1[1], ZERO, a2_3)),
        Series((base[3], ZERO, 3 * p2 + x3_2)),
        Series((ZERO, n1[2], ZERO, a4_3)),
        Series((base[5], ZERO, 6 * p2 + x5_2)),
        Series((ZERO, n1[3], ZERO, a6_3)),
        3 * p,
        Series.constant(0),
    ]
    return values


def main():
    compiled = P.compile_fibre()
    tails = compiled["tails"]
    v = NF((Fraction(0), Fraction(1)))
    D = 3 * v ** 2 - 2
    A2 = 3 * v ** 2 + 3 * v + 1
    x5 = -36 * v ** 2 * A2 / D
    x3 = x5 * (v + 2)
    x1 = x5 * (v + 1) + x5 ** 2 * (3 * v + 1) / (9 * v)
    base = [ZERO, x1, ZERO, ONE + x3, ZERO, NF(3) + x5, ZERO, NF(3), ZERO]

    assert all(not nf_eval(tails[ell], base) for ell in (1, 2, 3, 4, 5, 7))
    nu = nf_eval(tails[6], base)
    rho0 = nf_eval(tails[8], base)
    assert nu and rho0

    normals = (0, 2, 4, 6)
    full_normal_matrix = [
        [nf_eval(M.cpartial(tails[ell], column), base) for column in normals]
        for ell in (1, 3, 5, 7)
    ]
    determinant_residual = nf_determinant(full_normal_matrix)
    if determinant_residual:
        print("determinant_residual", canonical_digest(determinant_residual))
        print("Q12_at_v", canonical_digest(NF((
            Fraction(480), Fraction(4688), Fraction(8664), Fraction(4608),
            Fraction(111060), Fraction(391932), Fraction(-503280),
            Fraction(-5322618), Fraction(-12251574), Fraction(-12217797),
            Fraction(-2488077), Fraction(4809213), Fraction(2893401),
        ))))
        raise RuntimeError("normal determinant does not vanish")
    selected_odd = (3, 5, 7)
    matrix3 = [
        [nf_eval(M.cpartial(tails[ell], column), base) for column in normals[1:]]
        for ell in selected_odd
    ]
    rhs3 = [
        -nf_eval(M.cpartial(tails[ell], normals[0]), base)
        for ell in selected_odd
    ]
    tail_normal = solve(matrix3, rhs3)
    n1 = [ONE] + tail_normal
    kernel_residuals = []
    for ell in (1, 3, 5, 7):
        kernel_residuals.append(sum(
            (
                nf_eval(M.cpartial(tails[ell], column), base) * direction
                for column, direction in zip(normals, n1)
            ),
            ZERO,
        ))
    if any(kernel_residuals):
        print("kernel_residuals", [canonical_digest(value) for value in kernel_residuals])
        raise RuntimeError("normal-kernel consistency failure")

    zero_unknowns = [ZERO] * 7

    def jet_equations(unknowns):
        values = make_series(base, n1, unknowns)
        return [
            series_eval(tails[ell], values).coefficients[2]
            for ell in (2, 4, 6)
        ] + [
            series_eval(tails[ell], values).coefficients[3]
            for ell in (1, 3, 5, 7)
        ]

    source = jet_equations(zero_unknowns)
    matrix7 = []
    columns = []
    for column in range(7):
        basis = [ZERO] * 7
        basis[column] = ONE
        value = jet_equations(basis)
        columns.append([entry - origin for entry, origin in zip(value, source)])
    matrix7 = [[columns[column][row] for column in range(7)] for row in range(7)]
    solution = solve(matrix7, [-entry for entry in source])
    assert all(not entry for entry in jet_equations(solution))

    final_values = make_series(base, n1, solution)
    r8_series = series_eval(tails[8], final_values)
    assert not r8_series.coefficients[1]
    assert not r8_series.coefficients[3]
    rho2 = r8_series.coefficients[2]
    p2, _, x3_2, x5_2, _, _, _ = solution
    v2 = x3_2 / x5 - (v + 2) * (p2 + x5_2 / x5)

    print("parameter=t=a0, Kummer_character=0, involution_character=odd")
    print("base_nu=", canonical_digest(nu))
    print("base_r8=", canonical_digest(rho0))
    for name, value in zip(("a2_t", "a4_t", "a6_t"), tail_normal):
        print(name, canonical_digest(value))
    for name, value in zip(
        ("p_t2", "x1_t2", "x3_t2", "x5_t2", "a2_t3", "a4_t3", "a6_t3"),
        solution,
    ):
        print(name, canonical_digest(value))
    print("r8_t2=", canonical_digest(rho2))
    print("r8_t2_nonzero=", bool(rho2))
    print("v_t2=", canonical_digest(v2))
    print("v_t2_nonzero=", bool(v2))
    print("seven_row_jet=PASS")


if __name__ == "__main__":
    main()
