#!/usr/bin/env python3
"""Emit weighted CONE tests for the K=16 terminal family.

The implementation follows the charged coefficient-array recurrence
(2.2)--(2.13) from terminal_array_recurrence.py, but keeps sparse residual
polynomials instead of evaluating at a point.  High spine variables are solved
using the charged closed pivot diagonals.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import pathlib
import random
import time
from fractions import Fraction

import terminal_array_recurrence as point_model
from singular_terminal_driver import h_polynomial, modular_roots, split_roots


HERE = pathlib.Path(__file__).resolve().parent


def frac_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"({value.numerator}/{value.denominator})"


class ModField:
    kind = "mod"

    def __init__(self, prime: int, y_value: int):
        self.prime = prime
        self.y_value = y_value % prime

    def zero(self) -> int:
        return 0

    def one(self) -> int:
        return 1

    def from_int(self, value: int) -> int:
        return value % self.prime

    def from_fraction(self, value: Fraction) -> int:
        return value.numerator % self.prime * pow(value.denominator, -1, self.prime) % self.prime

    def y(self) -> int:
        return self.y_value

    def add(self, left: int, right: int) -> int:
        return (left + right) % self.prime

    def neg(self, value: int) -> int:
        return (-value) % self.prime

    def sub(self, left: int, right: int) -> int:
        return (left - right) % self.prime

    def mul(self, left: int, right: int) -> int:
        return left * right % self.prime

    def inv(self, value: int) -> int:
        value %= self.prime
        if value == 0:
            raise ZeroDivisionError("zero finite-field coefficient")
        return pow(value, -1, self.prime)

    def div(self, left: int, right: int) -> int:
        return self.mul(left, self.inv(right))

    def scale(self, value: int, scalar: Fraction | int) -> int:
        if isinstance(scalar, int):
            return value * (scalar % self.prime) % self.prime
        return self.mul(value, self.from_fraction(scalar))

    def is_zero(self, value: int) -> bool:
        return value % self.prime == 0

    def to_singular(self, value: int) -> str:
        return str(value % self.prime)

    def digest_text(self, value: int) -> str:
        return str(value % self.prime)


class RationalField:
    kind = "rational"

    def __init__(self, y_value: Fraction):
        self.y_value = y_value

    def zero(self) -> Fraction:
        return Fraction(0)

    def one(self) -> Fraction:
        return Fraction(1)

    def from_int(self, value: int) -> Fraction:
        return Fraction(value)

    def from_fraction(self, value: Fraction) -> Fraction:
        return value

    def y(self) -> Fraction:
        return self.y_value

    def add(self, left: Fraction, right: Fraction) -> Fraction:
        return left + right

    def neg(self, value: Fraction) -> Fraction:
        return -value

    def sub(self, left: Fraction, right: Fraction) -> Fraction:
        return left - right

    def mul(self, left: Fraction, right: Fraction) -> Fraction:
        return left * right

    def inv(self, value: Fraction) -> Fraction:
        if value == 0:
            raise ZeroDivisionError("zero rational coefficient")
        return 1 / value

    def div(self, left: Fraction, right: Fraction) -> Fraction:
        return left / right

    def scale(self, value: Fraction, scalar: Fraction | int) -> Fraction:
        return value * scalar

    def is_zero(self, value: Fraction) -> bool:
        return value == 0

    def to_singular(self, value: Fraction) -> str:
        return frac_text(value)

    def digest_text(self, value: Fraction) -> str:
        return frac_text(value)


class QuadraticField:
    kind = "quadratic"

    def __init__(self, t: int):
        self.t = t
        q = 2 * t + 1
        self.A = Fraction(12 * q * q)
        self.B = Fraction(-12 * q * (t + 1))
        self.C = Fraction((t + 1) * (3 * t + 2))

    def zero(self) -> tuple[Fraction, Fraction]:
        return (Fraction(0), Fraction(0))

    def one(self) -> tuple[Fraction, Fraction]:
        return (Fraction(1), Fraction(0))

    def from_int(self, value: int) -> tuple[Fraction, Fraction]:
        return (Fraction(value), Fraction(0))

    def from_fraction(self, value: Fraction) -> tuple[Fraction, Fraction]:
        return (value, Fraction(0))

    def y(self) -> tuple[Fraction, Fraction]:
        return (Fraction(0), Fraction(1))

    def add(
        self, left: tuple[Fraction, Fraction], right: tuple[Fraction, Fraction]
    ) -> tuple[Fraction, Fraction]:
        return (left[0] + right[0], left[1] + right[1])

    def neg(self, value: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
        return (-value[0], -value[1])

    def sub(
        self, left: tuple[Fraction, Fraction], right: tuple[Fraction, Fraction]
    ) -> tuple[Fraction, Fraction]:
        return (left[0] - right[0], left[1] - right[1])

    def mul(
        self, left: tuple[Fraction, Fraction], right: tuple[Fraction, Fraction]
    ) -> tuple[Fraction, Fraction]:
        a, b = left
        c, d = right
        yd = b * d
        return (
            a * c - yd * self.C / self.A,
            a * d + b * c - yd * self.B / self.A,
        )

    def inv(self, value: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
        a, b = value
        det = a * (a - b * self.B / self.A) + b * b * self.C / self.A
        if det == 0:
            raise ZeroDivisionError(f"zero quadratic coefficient {value}")
        return ((a - b * self.B / self.A) / det, -b / det)

    def div(
        self, left: tuple[Fraction, Fraction], right: tuple[Fraction, Fraction]
    ) -> tuple[Fraction, Fraction]:
        return self.mul(left, self.inv(right))

    def scale(
        self, value: tuple[Fraction, Fraction], scalar: Fraction | int
    ) -> tuple[Fraction, Fraction]:
        return (value[0] * scalar, value[1] * scalar)

    def is_zero(self, value: tuple[Fraction, Fraction]) -> bool:
        return value[0] == 0 and value[1] == 0

    def _term_text(self, coeff: Fraction, monomial: str) -> str | None:
        if coeff == 0:
            return None
        if coeff == 1:
            return monomial
        if coeff == -1:
            return f"-{monomial}"
        return f"{frac_text(coeff)}*{monomial}"

    def to_singular(self, value: tuple[Fraction, Fraction]) -> str:
        a, b = value
        if a == 0 and b == 0:
            return "0"
        pieces: list[str] = []
        if a != 0:
            pieces.append(frac_text(a))
        by = self._term_text(b, "yy")
        if by is not None:
            pieces.append(by)
        text = "+".join(pieces).replace("+-", "-")
        return f"({text})"

    def digest_text(self, value: tuple[Fraction, Fraction]) -> str:
        return f"{frac_text(value[0])},{frac_text(value[1])}"


class SparseRing:
    def __init__(self, field, weights: list[int], max_weight: int):
        self.field = field
        self.weights = weights
        self.max_weight = max_weight
        self.nvars = len(weights)
        self.zero_exp = (0,) * self.nvars
        self._weight_cache: dict[tuple[int, ...], int] = {self.zero_exp: 0}

    def weight(self, exp: tuple[int, ...]) -> int:
        cached = self._weight_cache.get(exp)
        if cached is not None:
            return cached
        value = sum(power * weight for power, weight in zip(exp, self.weights))
        self._weight_cache[exp] = value
        return value

    def zero(self) -> dict[tuple[int, ...], object]:
        return {}

    def const(self, coeff) -> dict[tuple[int, ...], object]:
        if self.field.is_zero(coeff):
            return {}
        return {self.zero_exp: coeff}

    def one(self) -> dict[tuple[int, ...], object]:
        return {self.zero_exp: self.field.one()}

    def var(self, index: int) -> dict[tuple[int, ...], object]:
        exp = [0] * self.nvars
        exp[index] = 1
        return {tuple(exp): self.field.one()}

    def add_to(
        self, target: dict[tuple[int, ...], object], source: dict[tuple[int, ...], object]
    ) -> None:
        field = self.field
        for exp, coeff in source.items():
            old = target.get(exp)
            new = coeff if old is None else field.add(old, coeff)
            if field.is_zero(new):
                target.pop(exp, None)
            else:
                target[exp] = new

    def add(
        self, left: dict[tuple[int, ...], object], right: dict[tuple[int, ...], object]
    ) -> dict[tuple[int, ...], object]:
        if len(left) < len(right):
            answer = dict(right)
            self.add_to(answer, left)
        else:
            answer = dict(left)
            self.add_to(answer, right)
        return answer

    def neg(self, poly: dict[tuple[int, ...], object]) -> dict[tuple[int, ...], object]:
        return {exp: self.field.neg(coeff) for exp, coeff in poly.items()}

    def sub(
        self, left: dict[tuple[int, ...], object], right: dict[tuple[int, ...], object]
    ) -> dict[tuple[int, ...], object]:
        answer = dict(left)
        self.add_to(answer, self.neg(right))
        return answer

    def scalar_mul(
        self, poly: dict[tuple[int, ...], object], scalar
    ) -> dict[tuple[int, ...], object]:
        if not poly or self.field.is_zero(scalar):
            return {}
        return {exp: self.field.mul(coeff, scalar) for exp, coeff in poly.items()}

    def scale(
        self, poly: dict[tuple[int, ...], object], scalar: Fraction | int
    ) -> dict[tuple[int, ...], object]:
        return self.scalar_mul(poly, self.field.from_fraction(scalar) if isinstance(scalar, Fraction) else self.field.from_int(scalar))

    def mul_var_power(
        self,
        poly: dict[tuple[int, ...], object],
        index: int,
        power: int,
        scalar=None,
    ) -> dict[tuple[int, ...], object]:
        if not poly:
            return {}
        if scalar is None:
            scalar = self.field.one()
        if self.field.is_zero(scalar):
            return {}
        answer: dict[tuple[int, ...], object] = {}
        added_weight = power * self.weights[index]
        field = self.field
        for exp, coeff in poly.items():
            if self.weight(exp) + added_weight > self.max_weight:
                continue
            new_exp = list(exp)
            new_exp[index] += power
            new_tuple = tuple(new_exp)
            new_coeff = field.mul(coeff, scalar)
            old = answer.get(new_tuple)
            if old is not None:
                new_coeff = field.add(old, new_coeff)
            if field.is_zero(new_coeff):
                answer.pop(new_tuple, None)
            else:
                answer[new_tuple] = new_coeff
        return answer

    def mul(
        self, left: dict[tuple[int, ...], object], right: dict[tuple[int, ...], object]
    ) -> dict[tuple[int, ...], object]:
        if not left or not right:
            return {}
        if len(left) > len(right):
            left, right = right, left
        field = self.field
        answer: dict[tuple[int, ...], object] = {}
        right_weight = {exp: self.weight(exp) for exp in right}
        for exp_left, coeff_left in left.items():
            weight_left = self.weight(exp_left)
            for exp_right, coeff_right in right.items():
                if weight_left + right_weight[exp_right] > self.max_weight:
                    continue
                exp = tuple(a + b for a, b in zip(exp_left, exp_right))
                coeff = field.mul(coeff_left, coeff_right)
                old = answer.get(exp)
                if old is not None:
                    coeff = field.add(old, coeff)
                if field.is_zero(coeff):
                    answer.pop(exp, None)
                else:
                    answer[exp] = coeff
        return answer

    def weighted_degrees(self, poly: dict[tuple[int, ...], object]) -> list[int]:
        return sorted({self.weight(exp) for exp in poly})

    def evaluate_mod(
        self, poly: dict[tuple[int, ...], object], values: list[int], prime: int
    ) -> int:
        total = 0
        for exp, coeff in poly.items():
            term = int(coeff) % prime
            for power, value in zip(exp, values):
                if power:
                    term = term * pow(value, power, prime) % prime
            total = (total + term) % prime
        return total

    def digest(self, poly: dict[tuple[int, ...], object]) -> str:
        h = hashlib.sha256()
        for exp in sorted(poly):
            h.update((",".join(map(str, exp)) + ":" + self.field.digest_text(poly[exp]) + "\n").encode())
        return h.hexdigest()


def coefficient_polynomial_text(
    ring: SparseRing, variable_names: list[str], poly: dict[tuple[int, ...], object]
) -> str:
    if not poly:
        return "0"
    pieces: list[str] = []
    for exp in sorted(poly, key=lambda item: (-ring.weight(item), item)):
        monomials = []
        for name, power in zip(variable_names, exp):
            if power == 1:
                monomials.append(name)
            elif power > 1:
                monomials.append(f"{name}^{power}")
        coeff = ring.field.to_singular(poly[exp])
        if monomials:
            pieces.append(f"({coeff})*" + "*".join(monomials))
        else:
            pieces.append(f"({coeff})")
    return "\n  " + "\n +".join(pieces)


def closed_pivot(t: int, weight: int, field):
    q, e = 2 * t + 1, 3 * t + 1
    d = field.sub(field.scale(field.y(), 2 * q), field.from_int(t + 1))
    if weight < t:
        j = weight
        aa = (
            9 * j * j * t
            + 18 * j * j
            - 54 * j * t * t
            - 81 * j * t
            - 26 * j
            + 72 * t**3
            + 144 * t * t
            + 88 * t
            + 16
        )
        bb = (
            -9 * j * j * t
            - 10 * j * j
            + 24 * j * t * t
            + 33 * j * t
            + 10 * j
            - 12 * t**3
            - 20 * t * t
            - 8 * t
        )
        linear = field.add(field.scale(d, aa), field.from_int(bb))
        return field.scale(
            linear,
            Fraction(3 * t * e, (t + 1) * (3 * t + 2) ** 3 * (4 * t - 2 * j + 1)),
        )
    if weight <= 2 * t:
        j = weight
        aa = 12 * t * t + 16 * t + 4 - j * (3 * t + 4)
        bb = 2 * (t + 1) * (j - t)
        linear = field.add(field.scale(d, aa), field.from_int(bb))
        return field.scale(
            linear,
            Fraction(-3 * t * e * (q - j), (t + 1) * q * (3 * t + 2) ** 2 * (4 * t - 2 * j + 1)),
        )
    g = normalizers(t, field)["g"]
    return field.div(field.mul(g, d), field.scale(field.y(), 2))


def normalizers(t: int, field) -> dict[str, object]:
    q, e = 2 * t + 1, 3 * t + 1
    y = field.y()
    g1 = field.from_fraction(Fraction(e, q))
    g2 = field.add(
        field.scale(y, Fraction(e, q)),
        field.from_fraction(Fraction(e * t, 2 * q * q)),
    )
    g = field.add(
        field.scale(y, Fraction(e * t, q * q)),
        field.from_fraction(Fraction(-e * t * (t + 1), 6 * q**3)),
    )
    c = field.neg(field.mul(y, g))
    return {"g1": g1, "g2": g2, "g": g, "c": c}


def derivative_l(array: list[dict[tuple[int, ...], object]], ring: SparseRing):
    return [ring.scale(array[index + 1], index + 1) for index in range(len(array) - 1)]


def convolution_l(
    left: list[dict[tuple[int, ...], object]],
    right: list[dict[tuple[int, ...], object]],
    degree: int,
    ring: SparseRing,
):
    answer = ring.zero()
    for index in range(degree + 1):
        if index < len(left) and degree - index < len(right):
            ring.add_to(answer, ring.mul(left[index], right[degree - index]))
    return answer


def shift_to_l(
    coefficients: dict[int, dict[tuple[int, ...], object]],
    b4_index: int,
    maximum: int,
    ring: SparseRing,
):
    answer = [ring.zero() for _ in range(maximum + 1)]
    for exponent, coefficient in coefficients.items():
        if not coefficient:
            continue
        for degree in range(exponent + 1):
            scalar = ring.field.from_int(math.comb(exponent, degree))
            term = ring.mul_var_power(coefficient, b4_index, exponent - degree, scalar)
            ring.add_to(answer[degree], term)
    return answer


def l_arrays(
    t: int,
    ring: SparseRing,
    solved_c: dict[int, dict[tuple[int, ...], object]],
    solved_u: dict[int, dict[tuple[int, ...], object]],
    solved_b2: dict[tuple[int, ...], object],
):
    q, e, top = 2 * t + 1, 3 * t + 1, 4 * t + 1
    b4_index = 0
    b3_index = ring.nvars - 1
    q_index = {j: j - 1 for j in range(2, t)}
    norms = normalizers(t, ring.field)
    y = ring.field.y()
    g = norms["g"]

    ux: dict[int, dict[tuple[int, ...], object]] = {q: ring.one()}
    for index in range(2, 2 * t + 1):
        if index < t:
            ux[q - index] = ring.var(q_index[index])
        else:
            ux[q - index] = solved_u.get(index, ring.zero())

    cx: dict[int, dict[tuple[int, ...], object]] = {t - 1: ring.one()}
    for index in range(1, t):
        cx[t - 1 - index] = solved_c.get(index, ring.zero())

    uu = shift_to_l(ux, b4_index, q, ring)
    cc = shift_to_l(cx, b4_index, t - 1, ring)

    bb = [ring.zero() for _ in range(t + 1)]
    for degree in range(t):
        scalar = ring.field.div(
            ring.field.scale(g, Fraction(3 * degree + 5, 2 * (degree + 1))),
            y,
        )
        bb[degree + 1] = ring.scalar_mul(cc[degree], scalar)

    ss = [ring.zero() for _ in range(2 * t + 1)]
    for degree in range(2 * t + 1):
        value = ring.zero()
        if degree + 1 < len(uu):
            ring.add_to(value, ring.scalar_mul(uu[degree + 1], ring.field.scale(g, 3 * (degree + 1))))
        for aa in range(t):
            bb_index = degree - 1 - aa
            if 0 <= bb_index < len(bb):
                ring.add_to(
                    value,
                    ring.scale(ring.mul(cc[aa], bb[bb_index]), 3 + 2 * aa - bb_index),
                )
        if degree < len(cc):
            term = ring.mul_var_power(cc[degree], b3_index, 1, ring.field.scale(g, Fraction(5 * degree + 7, 2)))
            ring.add_to(value, term)
        ss[degree] = ring.scalar_mul(value, ring.field.inv(ring.field.scale(y, 2 * degree + 1)))

    vv = [ring.zero() for _ in range(t + 2)]
    vv[0] = ring.mul_var_power(ring.one(), b3_index, 1, ring.field.neg(y))
    for degree in range(2, t + 2):
        vv[degree] = cc[degree - 2]

    yy = [ring.zero() for _ in range(2 * t + 2)]
    yy[0] = ring.scalar_mul(solved_b2, ring.field.neg(g))
    for degree in range(1, len(yy)):
        yy[degree] = ss[degree - 1]
    for degree in range(min(len(yy), len(bb))):
        yy[degree] = ring.sub(yy[degree], ring.mul_var_power(bb[degree], b3_index, 1))

    zz = [ring.zero() for _ in range(t + 2)]
    zz[0] = ring.mul_var_power(ring.one(), b3_index, 1, ring.field.neg(g))
    for degree in range(1, len(zz)):
        if degree - 1 < len(bb):
            zz[degree] = bb[degree - 1]

    vp = derivative_l(vv, ring)
    yp = derivative_l(yy, ring)
    up = derivative_l(uu, ring)
    nn = [ring.zero() for _ in range(e + 1)]
    for degree in range(e + 1):
        value = ring.neg(convolution_l(vv, yp, degree, ring))
        ring.add_to(value, convolution_l(vp, yy, degree, ring))
        ring.add_to(value, ring.scale(convolution_l(up, zz, degree, ring), 2))
        nn[degree] = value

    pp = [
        ring.scalar_mul(nn[degree + 1], ring.field.inv(ring.field.scale(y, 2)))
        for degree in range(e)
    ]

    rr = [ring.zero() for _ in range(top + 1)]
    for degree in range(top + 1):
        value = convolution_l(vv, pp, degree, ring)
        value = ring.sub(value, convolution_l(up, yy, degree, ring))
        rr[degree] = value
    yg = ring.field.mul(y, g)
    ring.add_to(rr[0], ring.const(ring.field.neg(yg)))

    rx = [ring.zero() for _ in range(top + 1)]
    for degree in range(top + 1):
        value = ring.zero()
        for higher in range(degree, top + 1):
            power = higher - degree
            scalar = math.comb(higher, degree)
            if power % 2:
                scalar = -scalar
            ring.add_to(value, ring.mul_var_power(rr[higher], b4_index, power, ring.field.from_int(scalar)))
        rx[degree] = value
    return rr, rx


def terminal_polynomials(t: int, field):
    top = 4 * t + 1
    weights = [1] + list(range(2, t)) + [t + 1]
    solved_c: dict[int, dict[tuple[int, ...], object]] = {}
    solved_u: dict[int, dict[tuple[int, ...], object]] = {}
    solved_b2: dict[tuple[int, ...], object] = {}
    pivot_terms = []
    for weight in range(1, 2 * t + 2):
        ring = SparseRing(field, weights, weight)
        _rr, rx = l_arrays(t, ring, solved_c, solved_u, solved_b2)
        rho = rx[top - weight]
        pivot = closed_pivot(t, weight, field)
        rhs = ring.scalar_mul(rho, field.neg(field.inv(pivot)))
        degrees = ring.weighted_degrees(rhs)
        if degrees and degrees != [weight]:
            raise AssertionError({"weight": weight, "degrees": degrees})
        if weight < t:
            solved_c[weight] = rhs
            variable = f"C{weight}"
        elif weight <= 2 * t:
            solved_u[weight] = rhs
            variable = f"q{weight}_0"
        else:
            solved_b2 = rhs
            variable = "b2"
        pivot_terms.append(
            {
                "weight": weight,
                "variable": variable,
                "terms": len(rhs),
                "pivot": field.digest_text(pivot),
            }
        )

    final_ring = SparseRing(field, weights, top)
    _rr, rx = l_arrays(t, final_ring, solved_c, solved_u, solved_b2)
    high_nonzero = [degree for degree in range(2 * t, top + 1) if rx[degree]]
    if high_nonzero:
        raise AssertionError(f"nonzero high X bands after solve: {high_nonzero}")
    rows = [final_ring.neg(rx[degree]) for degree in range(2 * t)]
    for degree, row in enumerate(rows):
        degrees = final_ring.weighted_degrees(row)
        if degree == 0:
            allowed = {0, top}
            if not set(degrees).issubset(allowed):
                raise AssertionError({"band": degree, "degrees": degrees})
        elif degrees and degrees != [top - degree]:
            raise AssertionError({"band": degree, "degrees": degrees, "expected": top - degree})
    return final_ring, rows, pivot_terms


def make_field(t: int, mode: str, prime: int | None, branch: int | None):
    if mode == "mod":
        if prime is None or branch is None:
            raise ValueError("mod mode requires --prime and --branch")
        roots = modular_roots(t, prime)
        return ModField(prime, roots[branch]), roots[branch]
    if mode == "split-exact":
        if branch is None:
            raise ValueError("split-exact mode requires --branch")
        roots = split_roots(t)
        return RationalField(Fraction(int(roots[branch].p), int(roots[branch].q))), roots[branch]
    if mode == "exact":
        return QuadraticField(t), None
    raise ValueError(mode)


def singular_header(t: int, mode: str, prime: int | None, branch: int | None, variables: list[str], weights: list[int]) -> list[str]:
    if mode == "mod":
        return [f"ring r={prime},({','.join(variables)}),wp({','.join(map(str, weights))});"]
    if mode == "split-exact":
        return [f"ring r=0,({','.join(variables)}),wp({','.join(map(str, weights))});"]
    yy = "yy"
    H = str(h_polynomial(t, __import__("sympy").Symbol(yy))).replace("**", "^")
    return [f"ring r=(0,{yy}),({','.join(variables)}),wp({','.join(map(str, weights))});", f"minpoly={H};"]


def emit_singular(
    t: int,
    mode: str,
    prime: int | None,
    branch: int | None,
    ring: SparseRing,
    rows: list[dict[tuple[int, ...], object]],
    metadata: dict[str, object],
) -> str:
    variables = ["b4"] + [f"q{j}_0" for j in range(2, t)] + ["b3"]
    weights = [1] + list(range(2, t)) + [t + 1]
    positive = rows[1:]
    tau = dict(rows[0])
    tau.pop(ring.zero_exp, None)
    lines = [
        f"// CONE generated from coefficient-array recurrence; t={t} mode={mode} prime={prime} branch={branch}",
        *singular_header(t, mode, prime, branch, variables, weights),
        "option(noredSB);",
        'print("CONE_JOB_START");',
        f'print("T={t}");',
        f'print("MODE={mode}");',
    ]
    if prime is not None:
        lines.append(f'print("PRIME={prime}");')
    if branch is not None:
        lines.append(f'print("BRANCH={branch}");')
    for index, row in enumerate(rows):
        lines.append(f"poly T{index} = {coefficient_polynomial_text(ring, variables, row)};")
    lines.append(f"poly tau = {coefficient_polynomial_text(ring, variables, tau)};")
    lines.append("ideal Iplus=" + ",".join(f"T{index}" for index in range(1, 2 * t)) + ";")
    lines += [
        'print("STD_START");',
        "timer=1;",
        "ideal G=std(Iplus);",
        'print("STD_TIMER");',
        "timer;",
        'print("CONE_BASIS_SIZE");',
        "size(G);",
        'print("CONE_DIM");',
        "int cone_dim=dim(G);",
        "cone_dim;",
        "if (cone_dim<=0)",
        "{",
        '  print("CONE_VERDICT_DIM0");',
        "}",
        "else",
        "{",
        '  print("RABINOWITSCH_START");',
        f"  ring rr={prime if mode == 'mod' else '0'},(z,{','.join(variables)}),dp;" if mode != "exact" else f"  ring rr=(0,yy),(z,{','.join(variables)}),dp;",
    ]
    if mode == "exact":
        yy = __import__("sympy").Symbol("yy")
        lines.append(f"  minpoly={str(h_polynomial(t, yy)).replace('**', '^')};")
    lines += [
        "  ideal Ir=imap(r,Iplus);",
        "  poly taur=imap(r,tau);",
        "  ideal Rab=Ir,1-z*taur;",
        "  ideal GR=std(Rab);",
        '  print("RAB_BASIS_SIZE");',
        "  size(GR);",
        '  print("TAU_IN_RADICAL");',
        "  int tau_in=(reduce(1,GR)==0);",
        "  tau_in;",
        "  if (tau_in==1) { print(\"CONE_VERDICT_TAU_CRITERION\"); }",
        "  else { print(\"CONE_VERDICT_NOT_REFUTATION_CANDIDATE\"); }",
        "}",
        'print("CONE_JOB_DONE");',
        "quit;",
    ]
    metadata.update(
        {
            "variables": variables,
            "weights": weights,
            "row_terms": {str(index): len(row) for index, row in enumerate(rows)},
            "row_sha256": {str(index): ring.digest(row) for index, row in enumerate(rows)},
            "tau_terms": len(tau),
            "tau_sha256": ring.digest(tau),
        }
    )
    return "\n".join(lines) + "\n"


def validate_modular_points(t: int, prime: int, branch: int, ring: SparseRing, rows, checks: int) -> list[dict[str, object]]:
    if checks <= 0:
        return []
    roots = modular_roots(t, prime)
    y = roots[branch]
    rng = random.Random(9303 + 1000 * t + 10 * prime + branch)
    validations = []
    variables = ["b4"] + [f"q{j}_0" for j in range(2, t)] + ["b3"]
    for check_index in range(checks):
        b4 = rng.randrange(prime)
        residual = {j: rng.randrange(prime) for j in range(2, t)}
        b3 = rng.randrange(prime)
        values = [b4] + [residual[j] for j in range(2, t)] + [b3]
        polynomial_values = [ring.evaluate_mod(row, values, prime) for row in rows]
        point_values, _pivots = point_model.terminal_values(t, prime, y, b3, b4, residual)
        if polynomial_values != point_values:
            raise AssertionError(
                {
                    "t": t,
                    "prime": prime,
                    "branch": branch,
                    "check": check_index,
                    "variables": dict(zip(variables, values)),
                    "polynomial": polynomial_values,
                    "point": point_values,
                }
            )
        validations.append(
            {
                "check": check_index,
                "digest": sum((index + 1) * value for index, value in enumerate(polynomial_values)) % prime,
            }
        )
    return validations


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--t", type=int, required=True)
    parser.add_argument("--mode", choices=("mod", "exact", "split-exact"), required=True)
    parser.add_argument("--prime", type=int)
    parser.add_argument("--branch", type=int, choices=(0, 1))
    parser.add_argument("--stem")
    parser.add_argument("--point-checks", type=int, default=2)
    args = parser.parse_args()

    started = time.monotonic()
    field, y_value = make_field(args.t, args.mode, args.prime, args.branch)
    ring, rows, pivot_terms = terminal_polynomials(args.t, field)
    if args.mode == "mod":
        validations = validate_modular_points(args.t, args.prime, args.branch, ring, rows, args.point_checks)
    else:
        validations = []
    q = 2 * args.t + 1
    if args.mode == "mod":
        d_value = (2 * q * int(y_value) - (args.t + 1)) % int(args.prime)
    elif args.mode == "split-exact":
        d_value = 2 * q * y_value - (args.t + 1)
    else:
        d_value = None

    mode_suffix = args.mode
    if args.prime is not None:
        mode_suffix += f"_p{args.prime}"
    if args.branch is not None:
        mode_suffix += f"_branch{args.branch}"
    stem = args.stem or f"cone_t{args.t}_{mode_suffix}"
    metadata: dict[str, object] = {
        "typing": "weighted CONE I_{t,+} generator",
        "t": args.t,
        "mode": args.mode,
        "prime": args.prime,
        "branch": args.branch,
        "y": str(y_value) if y_value is not None else "yy",
        "d": str(d_value) if d_value is not None else "2*(2t+1)*yy-(t+1)",
        "pivot_terms": pivot_terms,
        "modular_point_validations": validations,
        "generation_elapsed_seconds": time.monotonic() - started,
    }
    source = emit_singular(args.t, args.mode, args.prime, args.branch, ring, rows, metadata)
    source_path = HERE / f"{stem}.sing"
    meta_path = HERE / f"{stem}.json"
    source_path.write_text(source, encoding="utf-8")
    metadata["source"] = str(source_path)
    metadata["source_sha256"] = hashlib.sha256(source.encode()).hexdigest()
    meta_path.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"source": str(source_path), "metadata": str(meta_path), "elapsed": metadata["generation_elapsed_seconds"]}, sort_keys=True))


if __name__ == "__main__":
    main()
