#!/usr/bin/env python3
"""Fast exact Laurent/Euler terminal constructor for the K=16 ray.

This is a compatibility backend for ``terminal_laurent_model.py``.  It uses
the same recurrence and the proved descending Laurent/Euler pivot spine, but
does not ask a general CAS to cancel and reduce every intermediate expression.
Instead it computes directly in

    A_t = Q[y]/(12(2t+1)^2 y^2 - 12(2t+1)(t+1)y
                 + (t+1)(3t+2))

as exact pairs ``a+b*y`` and represents all other polynomials sparsely.

The output JSON has the fields consumed by the existing terminal summarizer
and saturation emitter.  Every division, recurrence identity, affine pivot,
terminal support condition, and terminal top degree is checked exactly.

Examples (run in the foreground, with an outer timeout for t=6):

    python3 terminal_laurent_fast.py 2 --self-test
    timeout 3600 python3 -u terminal_laurent_fast.py 6
"""

from __future__ import annotations

import argparse
import ast
import dataclasses
from fractions import Fraction
import json
import math
import pathlib
import resource
import time
from typing import Dict, Iterable, Mapping, Optional, Sequence, Tuple


HERE = pathlib.Path(__file__).resolve().parent
REFERENCE_DIR = pathlib.Path("/home/ubuntu/jc2/box/k16spine-20260903")

Rat = Fraction
QElt = Tuple[Rat, Rat]              # a + b*y
Monomial = Tuple[int, ...]


class QuadraticField:
    """The fixed two-dimensional Q-algebra A_t, known to be a field here."""

    __slots__ = ("t", "q", "mu", "nu", "zero", "one", "y", "hA", "hB", "hC")

    def __init__(self, t: int):
        self.t = t
        self.q = 2*t+1
        # y^2 = mu*y + nu.
        self.mu = Rat(t+1, self.q)
        self.nu = -Rat((t+1)*(3*t+2), 12*self.q*self.q)
        self.zero = (Rat(0), Rat(0))
        self.one = (Rat(1), Rat(0))
        self.y = (Rat(0), Rat(1))
        self.hA = 12*self.q*self.q
        self.hB = -12*self.q*(t+1)
        self.hC = (t+1)*(3*t+2)

    @staticmethod
    def coerce(value) -> QElt:
        if isinstance(value, tuple):
            return value
        return (Rat(value), Rat(0))

    @staticmethod
    def add(left: QElt, right: QElt) -> QElt:
        return (left[0]+right[0], left[1]+right[1])

    @staticmethod
    def neg(value: QElt) -> QElt:
        return (-value[0], -value[1])

    @staticmethod
    def sub(left: QElt, right: QElt) -> QElt:
        return (left[0]-right[0], left[1]-right[1])

    def mul(self, left: QElt, right: QElt) -> QElt:
        a, b = left
        c, d = right
        bd = b*d
        return (a*c+bd*self.nu, a*d+b*c+bd*self.mu)

    def pow(self, value: QElt, exponent: int) -> QElt:
        if exponent < 0:
            return self.pow(self.inv(value), -exponent)
        answer = self.one
        base = value
        while exponent:
            if exponent & 1:
                answer = self.mul(answer, base)
            exponent >>= 1
            if exponent:
                base = self.mul(base, base)
        return answer

    def inv(self, value: QElt) -> QElt:
        a, b = value
        # Multiplication by a+b*y has matrix
        # [[a, b*nu], [b, a+b*mu]].
        determinant = a*(a+b*self.mu)-b*b*self.nu
        if determinant == 0:
            raise ZeroDivisionError(value)
        answer = ((a+b*self.mu)/determinant, -b/determinant)
        if self.mul(value, answer) != self.one:
            raise AssertionError("quadratic inverse check failed")
        return answer

    def div(self, left: QElt, right: QElt) -> QElt:
        return self.mul(left, self.inv(right))

    def resultant(self, value: QElt) -> Rat:
        """Resultant of the displayed quadratic H and a+b*y (b != 0)."""
        a, b = value
        if b == 0:
            return a*a
        return self.hA*a*a-self.hB*a*b+self.hC*b*b

    @staticmethod
    def _rat_text(value: Rat) -> str:
        if value.denominator == 1:
            return str(value.numerator)
        return f"{value.numerator}/{value.denominator}"

    def text(self, value: QElt, yname: str) -> str:
        a, b = value
        if b == 0:
            return self._rat_text(a)
        if a == 0:
            if b == 1:
                return yname
            if b == -1:
                return "-"+yname
            return self._rat_text(b)+"*"+yname
        bpart = yname if abs(b) == 1 else self._rat_text(abs(b))+"*"+yname
        sign = "+" if b > 0 else "-"
        return f"{self._rat_text(a)} {sign} {bpart}"


class SparseRing:
    __slots__ = ("field", "names", "index", "zero_monomial")

    def __init__(self, field: QuadraticField, names: Sequence[str]):
        self.field = field
        self.names = tuple(names)
        self.index = {name: position for position, name in enumerate(self.names)}
        self.zero_monomial = (0,)*len(self.names)

    def zero(self) -> "SparsePoly":
        return SparsePoly(self, {})

    def const(self, value=0) -> "SparsePoly":
        coefficient = self.field.coerce(value)
        if coefficient == self.field.zero:
            return self.zero()
        return SparsePoly(self, {self.zero_monomial: coefficient})

    def variable(self, name: str) -> "SparsePoly":
        monomial = [0]*len(self.names)
        monomial[self.index[name]] = 1
        return SparsePoly(self, {tuple(monomial): self.field.one})


class SparsePoly:
    """Sparse multivariate polynomial over QuadraticField."""

    __slots__ = ("ring", "terms")

    def __init__(self, ring: SparseRing, terms: Mapping[Monomial, QElt]):
        self.ring = ring
        zero = ring.field.zero
        self.terms: Dict[Monomial, QElt] = {
            monomial: coefficient for monomial, coefficient in terms.items()
            if coefficient != zero
        }

    def _coerce(self, other) -> "SparsePoly":
        if isinstance(other, SparsePoly):
            if other.ring is not self.ring:
                raise TypeError("polynomial rings differ")
            return other
        return self.ring.const(other)

    def __bool__(self) -> bool:
        return bool(self.terms)

    def __eq__(self, other) -> bool:
        try:
            other = self._coerce(other)
        except (TypeError, ValueError):
            return False
        return self.terms == other.terms

    def __neg__(self) -> "SparsePoly":
        return SparsePoly(self.ring, {
            monomial: self.ring.field.neg(coefficient)
            for monomial, coefficient in self.terms.items()
        })

    def __add__(self, other) -> "SparsePoly":
        other = self._coerce(other)
        if not self.terms:
            return other
        if not other.terms:
            return self
        field = self.ring.field
        answer = dict(self.terms)
        for monomial, coefficient in other.terms.items():
            new = field.add(answer.get(monomial, field.zero), coefficient)
            if new == field.zero:
                answer.pop(monomial, None)
            else:
                answer[monomial] = new
        return SparsePoly(self.ring, answer)

    __radd__ = __add__

    def __sub__(self, other) -> "SparsePoly":
        return self+(-self._coerce(other))

    def __rsub__(self, other) -> "SparsePoly":
        return self._coerce(other)-self

    def scale(self, scalar) -> "SparsePoly":
        scalar = self.ring.field.coerce(scalar)
        field = self.ring.field
        if scalar == field.zero or not self.terms:
            return self.ring.zero()
        if scalar == field.one:
            return self
        return SparsePoly(self.ring, {
            monomial: field.mul(coefficient, scalar)
            for monomial, coefficient in self.terms.items()
        })

    def __mul__(self, other) -> "SparsePoly":
        other = self._coerce(other)
        if not self.terms or not other.terms:
            return self.ring.zero()
        if len(self.terms) == 1 and self.ring.zero_monomial in self.terms:
            return other.scale(self.terms[self.ring.zero_monomial])
        if len(other.terms) == 1 and self.ring.zero_monomial in other.terms:
            return self.scale(other.terms[self.ring.zero_monomial])
        field = self.ring.field
        answer: Dict[Monomial, QElt] = {}
        for lm, lc in self.terms.items():
            for rm, rc in other.terms.items():
                monomial = tuple(a+b for a, b in zip(lm, rm))
                product = field.mul(lc, rc)
                new = field.add(answer.get(monomial, field.zero), product)
                if new == field.zero:
                    answer.pop(monomial, None)
                else:
                    answer[monomial] = new
        return SparsePoly(self.ring, answer)

    __rmul__ = __mul__

    def __truediv__(self, other) -> "SparsePoly":
        other = self._coerce(other)
        if set(other.terms) != {self.ring.zero_monomial}:
            raise TypeError("division only by an A_t scalar")
        return self.scale(self.ring.field.inv(other.terms[self.ring.zero_monomial]))

    def __rtruediv__(self, other) -> "SparsePoly":
        if set(self.terms) != {self.ring.zero_monomial}:
            raise TypeError("division only by an A_t scalar")
        return self.ring.const(other).scale(
            self.ring.field.inv(self.terms[self.ring.zero_monomial]))

    def __pow__(self, exponent: int) -> "SparsePoly":
        if not isinstance(exponent, int) or exponent < 0:
            raise ValueError("polynomial exponent must be a nonnegative integer")
        answer = self.ring.const(1)
        base = self
        while exponent:
            if exponent & 1:
                answer = answer*base
            exponent >>= 1
            if exponent:
                base = base*base
        return answer

    def derivative(self, variable: str) -> "SparsePoly":
        index = self.ring.index[variable]
        field = self.ring.field
        answer = {}
        for monomial, coefficient in self.terms.items():
            power = monomial[index]
            if not power:
                continue
            changed = list(monomial)
            changed[index] -= 1
            answer[tuple(changed)] = field.mul(coefficient, (Rat(power), Rat(0)))
        return SparsePoly(self.ring, answer)

    def affine_parts(self, variable: str) -> Optional[Tuple["SparsePoly", "SparsePoly"]]:
        """Return coefficient,remainder, or None if degree in variable exceeds 1."""
        index = self.ring.index[variable]
        coefficient = {}
        remainder = {}
        for monomial, value in self.terms.items():
            power = monomial[index]
            if power > 1:
                return None
            if power:
                changed = list(monomial)
                changed[index] = 0
                coefficient[tuple(changed)] = value
            else:
                remainder[monomial] = value
        return SparsePoly(self.ring, coefficient), SparsePoly(self.ring, remainder)

    def scalar_value(self) -> QElt:
        if not self.terms:
            return self.ring.field.zero
        if set(self.terms) != {self.ring.zero_monomial}:
            raise ValueError("not an A_t scalar")
        return self.terms[self.ring.zero_monomial]

    def substitute(self, variable: str, rhs: "SparsePoly") -> "SparsePoly":
        """Exact sparse substitution, with powers of rhs shared across terms."""
        index = self.ring.index[variable]
        maximum = max((monomial[index] for monomial in self.terms), default=0)
        if maximum == 0:
            return self
        if any(monomial[index] for monomial in rhs.terms):
            raise ValueError("recursive substitution")
        powers = [self.ring.const(1)]
        for _ in range(maximum):
            powers.append(powers[-1]*rhs)
        groups: Dict[int, Dict[Monomial, QElt]] = {}
        for monomial, coefficient in self.terms.items():
            power = monomial[index]
            changed = list(monomial)
            changed[index] = 0
            groups.setdefault(power, {})[tuple(changed)] = coefficient
        answer = self.ring.zero()
        for power, terms in groups.items():
            part = SparsePoly(self.ring, terms)
            answer = answer+(part if power == 0 else part*powers[power])
        return answer

    def multiply_variable_power(self, variable: str, power: int,
                                scalar=1) -> "SparsePoly":
        if not self.terms:
            return self
        index = self.ring.index[variable]
        scalar = self.ring.field.coerce(scalar)
        field = self.ring.field
        answer = {}
        for monomial, coefficient in self.terms.items():
            changed = list(monomial)
            changed[index] += power
            answer[tuple(changed)] = field.mul(coefficient, scalar)
        return SparsePoly(self.ring, answer)

    def variables_used(self) -> set[str]:
        used = set()
        for monomial in self.terms:
            used.update(name for name, power in zip(self.ring.names, monomial) if power)
        return used

    def total_degrees(self) -> set[int]:
        return {sum(monomial) for monomial in self.terms}

    def text(self, yname: str) -> str:
        if not self.terms:
            return "0"
        field = self.ring.field
        pieces = []
        # Descending lexicographic order is deterministic and agrees with the
        # residual-variable order used by the saturation scripts.
        for monomial in sorted(self.terms, reverse=True):
            coefficient = self.terms[monomial]
            factors = []
            for name, power in zip(self.ring.names, monomial):
                if power == 1:
                    factors.append(name)
                elif power:
                    factors.append(f"{name}**{power}")
            monomial_text = "*".join(factors)
            if not monomial_text:
                pieces.append(field.text(coefficient, yname))
            elif coefficient == field.one:
                pieces.append(monomial_text)
            elif coefficient == (Rat(-1), Rat(0)):
                pieces.append("-"+monomial_text)
            else:
                ctext = field.text(coefficient, yname)
                if coefficient[0] and coefficient[1]:
                    ctext = "("+ctext+")"
                pieces.append(ctext+"*"+monomial_text)
        return " + ".join(pieces).replace(" + -", " - ")


class UniPoly:
    """Sparse univariate polynomial in s (or h), with SparsePoly coefficients."""

    __slots__ = ("ring", "coeff")

    def __init__(self, ring: SparseRing, coeff: Mapping[int, SparsePoly]):
        self.ring = ring
        self.coeff = {degree: value for degree, value in coeff.items() if value}

    @classmethod
    def zero(cls, ring: SparseRing) -> "UniPoly":
        return cls(ring, {})

    @classmethod
    def constant(cls, value: SparsePoly) -> "UniPoly":
        return cls(value.ring, {0: value})

    def __bool__(self) -> bool:
        return bool(self.coeff)

    def __eq__(self, other) -> bool:
        return isinstance(other, UniPoly) and self.ring is other.ring and self.coeff == other.coeff

    def __neg__(self) -> "UniPoly":
        return UniPoly(self.ring, {degree: -value for degree, value in self.coeff.items()})

    def __add__(self, other) -> "UniPoly":
        if not isinstance(other, UniPoly):
            other = UniPoly.constant(self.ring.const(other))
        answer = dict(self.coeff)
        for degree, value in other.coeff.items():
            new = answer.get(degree, self.ring.zero())+value
            if new:
                answer[degree] = new
            else:
                answer.pop(degree, None)
        return UniPoly(self.ring, answer)

    __radd__ = __add__

    def __sub__(self, other) -> "UniPoly":
        return self+(-other)

    def __mul__(self, other) -> "UniPoly":
        if isinstance(other, SparsePoly):
            return UniPoly(self.ring, {
                degree: coefficient*other for degree, coefficient in self.coeff.items()
            })
        if not isinstance(other, UniPoly):
            return self.scale(other)
        answer: Dict[int, SparsePoly] = {}
        for ld, lc in self.coeff.items():
            for rd, rc in other.coeff.items():
                degree = ld+rd
                new = answer.get(degree, self.ring.zero())+lc*rc
                if new:
                    answer[degree] = new
                else:
                    answer.pop(degree, None)
        return UniPoly(self.ring, answer)

    __rmul__ = __mul__

    def scale(self, scalar) -> "UniPoly":
        return UniPoly(self.ring, {
            degree: coefficient.scale(scalar) for degree, coefficient in self.coeff.items()
        })

    def derivative(self) -> "UniPoly":
        return UniPoly(self.ring, {
            degree-1: coefficient.scale(degree)
            for degree, coefficient in self.coeff.items() if degree
        })

    def shift(self, amount: int) -> "UniPoly":
        if any(degree+amount < 0 for degree in self.coeff):
            raise ValueError("negative univariate degree")
        return UniPoly(self.ring, {
            degree+amount: coefficient for degree, coefficient in self.coeff.items()
        })

    def substitute(self, variable: str, rhs: SparsePoly) -> "UniPoly":
        return UniPoly(self.ring, {
            degree: coefficient.substitute(variable, rhs)
            for degree, coefficient in self.coeff.items()
        })

    def coefficient(self, degree: int) -> SparsePoly:
        return self.coeff.get(degree, self.ring.zero())

    def leading_coefficient(self) -> SparsePoly:
        if not self.coeff:
            return self.ring.zero()
        return self.coeff[max(self.coeff)]


@dataclasses.dataclass
class BandRow:
    band: int
    expr: SparsePoly


def shifted_power(ring: SparseRing, variable: str, exponent: int) -> UniPoly:
    """Return (s+variable)^exponent without polynomial multiplication."""
    one = ring.const(1)
    return UniPoly(ring, {
        power: one.multiply_variable_power(
            variable, exponent-power, math.comb(exponent, power))
        for power in range(exponent+1)
    })


def integrate_zero(poly: UniPoly) -> UniPoly:
    return UniPoly(poly.ring, {
        degree+1: coefficient.scale(Rat(1, degree+1))
        for degree, coefficient in poly.coeff.items()
    })


def euler_inverse(rhs: UniPoly, yinv: QElt) -> UniPoly:
    answer = UniPoly(rhs.ring, {
        degree: coefficient.scale(yinv).scale(Rat(1, 2*degree+1))
        for degree, coefficient in rhs.coeff.items()
    })
    # y*(D+2sD') = rhs; equivalently (D+2sD')/yinv = rhs.
    check = answer+answer.derivative().shift(1).scale(2)
    if check.scale(rhs.ring.field.y) != rhs:
        raise AssertionError("Euler inverse check failed")
    return answer


def h_coefficient(poly_s: UniPoly, band: int, b4: str) -> SparsePoly:
    """Coefficient of h^band after s=h-b4."""
    answer = poly_s.ring.zero()
    for degree, coefficient in poly_s.coeff.items():
        if degree < band:
            continue
        shift = degree-band
        scalar = math.comb(degree, band) * (-1 if shift & 1 else 1)
        answer = answer+coefficient.multiply_variable_power(b4, shift, scalar)
    return answer


def all_h_coefficients(poly_s: UniPoly, maximum: int, b4: str) -> list[BandRow]:
    return [BandRow(band, h_coefficient(poly_s, band, b4))
            for band in range(maximum+1)]


def affine_scalar(poly: SparsePoly, variable: str) -> Tuple[QElt, SparsePoly]:
    parts = poly.affine_parts(variable)
    if parts is None:
        raise AssertionError(f"row is not affine in {variable}")
    coefficient, remainder = parts
    scalar = coefficient.scalar_value()
    if scalar == poly.ring.field.zero:
        raise AssertionError(f"zero pivot coefficient for {variable}")
    return scalar, remainder


def parse_exact(text: str, ring: SparseRing, yname: str) -> SparsePoly:
    """Parse the small arithmetic language emitted by SymPy, without floats."""
    names = {name: ring.variable(name) for name in ring.names}
    names[yname] = ring.const(ring.field.y)

    def visit(node) -> SparsePoly:
        if isinstance(node, ast.Expression):
            return visit(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, int):
            return ring.const(node.value)
        if isinstance(node, ast.Name) and node.id in names:
            return names[node.id]
        if isinstance(node, ast.UnaryOp):
            value = visit(node.operand)
            if isinstance(node.op, ast.USub):
                return -value
            if isinstance(node.op, ast.UAdd):
                return value
        if isinstance(node, ast.BinOp):
            left = visit(node.left)
            right = visit(node.right)
            if isinstance(node.op, ast.Add):
                return left+right
            if isinstance(node.op, ast.Sub):
                return left-right
            if isinstance(node.op, ast.Mult):
                return left*right
            if isinstance(node.op, ast.Div):
                return left/right
            if isinstance(node.op, ast.Pow):
                exponent_poly = right
                exponent_q = exponent_poly.scalar_value()
                if exponent_q[1] or exponent_q[0].denominator != 1:
                    raise ValueError("nonintegral exponent")
                return left**int(exponent_q[0])
        raise ValueError(f"unsupported expression node: {ast.dump(node)}")

    return visit(ast.parse(text, mode="eval"))


def _scalar_text(field: QuadraticField, value: QElt, yname: str) -> str:
    return field.text(value, yname)


def build(t: int, progress: bool = True) -> dict:
    if t < 2:
        raise ValueError("stable model begins at t=2")
    started = time.monotonic()
    e, q, N = 3*t+1, 2*t+1, 4*t+1
    yname = f"q{q}_1"
    names = (["b1", "b2", "b3", "b4", "B0"]
             + [f"q{j}_0" for j in range(2, 2*t+1)]
             + [f"C{j}" for j in range(1, t)])
    field = QuadraticField(t)
    ring = SparseRing(field, names)
    var = {name: ring.variable(name) for name in names}
    y = field.y
    yinv = field.inv(y)

    def say(message: str) -> None:
        if progress:
            print(f"FAST_LAURENT t={t} {message}", flush=True)

    say("stage=recurrence_start")
    g1 = (Rat(e, q), Rat(0))
    g2 = (Rat(e*t, 2*q*q), Rat(e, q))
    g = (-Rat(e*t*(t+1), 6*q**3), Rat(e*t, q*q))
    c = field.neg(field.mul(y, g))

    U = shifted_power(ring, "b4", q)
    for j in range(2, 2*t+1):
        U = U+shifted_power(ring, "b4", q-j)*var[f"q{j}_0"]

    C = shifted_power(ring, "b4", t-1)
    for j in range(1, t):
        C = C+shifted_power(ring, "b4", t-1-j)*var[f"C{j}"]
    A = C.shift(1)

    Bprime = (C.scale(5)+C.derivative().shift(1).scale(3)).scale(
        field.mul(g, yinv)).scale(Rat(1, 2))
    B = integrate_zero(Bprime)+UniPoly.constant(var["B0"])
    if B.derivative() != Bprime:
        raise AssertionError("B recurrence failed")
    if B.leading_coefficient() != ring.const(g2):
        raise AssertionError("B leading coefficient disagrees with normalizer")

    rhs_D = (U.derivative().scale(field.mul((Rat(3), Rat(0)), g))
             + A*B
             - A.shift(1)*B.derivative()
             + A.derivative().shift(1)*B.scale(2)
             + (A.shift(-1)+A.derivative().scale(Rat(5, 2)))
               * var["b3"] * ring.const(g))
    D = euler_inverse(rhs_D, yinv)
    if D.leading_coefficient() != ring.const(g1):
        raise AssertionError("D leading coefficient disagrees with normalizer")

    V = A.shift(1)-UniPoly.constant(var["b3"].scale(y))
    Y = D.shift(1)-B*var["b3"]-UniPoly.constant(var["b2"].scale(g))
    Z = B.shift(1)-UniPoly.constant(var["b3"].scale(g))

    numerator = (UniPoly.constant(var["b1"].scale(field.mul(y, g)))
                 - V*Y.derivative()+V.derivative()*Y
                 + U.derivative()*Z.scale(2))
    b1_coefficient, b1_remainder = affine_scalar(numerator.coefficient(0), "b1")
    b1_inverse = field.inv(b1_coefficient)
    b1_rhs = (-b1_remainder).scale(b1_inverse)
    numerator = numerator.substitute("b1", b1_rhs)
    if numerator.coefficient(0):
        raise AssertionError("r^1 numerator is not divisible by s")
    Xprime = numerator.shift(-1).scale(field.mul(yinv, (Rat(1, 2), Rat(0))))
    if Xprime.leading_coefficient() != ring.const(e):
        raise AssertionError("X' leading coefficient disagrees")

    gauge = h_coefficient(Xprime, q-1, "b4")
    B0_coefficient, B0_remainder = affine_scalar(gauge, "B0")
    B0_inverse = field.inv(B0_coefficient)
    B0_rhs = (-B0_remainder).scale(B0_inverse)

    B = B.substitute("B0", B0_rhs)
    D = D.substitute("B0", B0_rhs)
    Y = Y.substitute("B0", B0_rhs)
    Z = Z.substitute("B0", B0_rhs)
    Xprime = Xprime.substitute("B0", B0_rhs)
    b1_rhs = b1_rhs.substitute("B0", B0_rhs)
    if gauge.substitute("B0", B0_rhs):
        raise AssertionError("X gauge substitution failed")

    say(f"stage=recurrence_done seconds={time.monotonic()-started:.3f}")
    R_s = V*Xprime-U.derivative()*Y-UniPoly.constant(ring.const(field.mul(y, g)))
    rows = all_h_coefficients(R_s, N, "b4")
    say("stage=h_bands_done terms="+str(sum(len(row.expr.terms) for row in rows)))

    eliminate = ([f"C{j}" for j in range(1, t)]
                 + [f"q{j}_0" for j in range(t, 2*t+1)]
                 + ["b2"])
    pivot_bands = list(range(N-1, 2*t-1, -1))
    if len(eliminate) != len(pivot_bands):
        raise AssertionError("pivot spine length mismatch")

    active = {row.band: row.expr for row in rows if row.expr}
    pivot_record = []
    for variable, band in zip(eliminate, pivot_bands):
        # The proved spine is triangular in descending h-band order.
        if any(high > band for high in active):
            raise AssertionError(f"unresolved row above pivot band {band}")
        row = active.get(band, ring.zero())
        coefficient, remainder = affine_scalar(row, variable)
        inverse = field.inv(coefficient)
        rhs = (-remainder).scale(inverse)
        if row.substitute(variable, rhs):
            raise AssertionError(f"high pivot substitution failed at band {band}")
        del active[band]
        for lower in sorted(list(active)):
            if lower < band:
                active[lower] = active[lower].substitute(variable, rhs)
                if not active[lower]:
                    del active[lower]
        pivot_record.append({
            "band": band,
            "variable": variable,
            "coefficient": _scalar_text(field, coefficient, yname),
            "inverse": _scalar_text(field, inverse, yname),
            "resultant": field._rat_text(field.resultant(coefficient)),
            "rhs": rhs.text(yname),
        })
        say(f"stage=pivot band={band} variable={variable} "
            f"rows={len(active)} terms={sum(len(value.terms) for value in active.values())} "
            f"seconds={time.monotonic()-started:.3f}")

    if any(band >= 2*t for band in active):
        raise AssertionError("unresolved high rows")
    if sorted(active) != list(range(2*t)):
        raise AssertionError(f"terminal bands differ: {sorted(active)}")
    residual_variables = ["b3", "b4"]+[f"q{j}_0" for j in range(2, t)]
    allowed = set(residual_variables)
    terminal = []
    for band in range(2*t):
        expression = active[band]
        unexpected = expression.variables_used()-allowed
        if unexpected:
            raise AssertionError(f"band {band}: eliminated variables remain: {unexpected}")
        degrees = expression.total_degrees()
        if not degrees or max(degrees) != N-band:
            raise AssertionError(
                f"band {band}: degrees {degrees}, expected maximum {N-band}")
        terminal.append({"band": band, "expr": expression.text(yname)})

    elapsed = time.monotonic()-started
    rss_kib = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    H = f"{field.hA}*{yname}**2"
    if field.hB < 0:
        H += f" - {-field.hB}*{yname}"
    else:
        H += f" + {field.hB}*{yname}"
    H += f" + {field.hC}"
    record = {
        "typing": "exact Laurent/Euler recurrence in A_t (fast sparse backend)",
        "backend": {
            "name": "terminal_laurent_fast",
            "exact": True,
            "quadratic_representation": "a+b*y",
            "self_checks": [
                "all coefficient inverses multiplied back",
                "B/D/Euler recurrences",
                "b1 divisibility and B0 gauge",
                "every affine pivot row vanishes after substitution",
                "no high rows or eliminated variables remain",
                "terminal top degrees",
            ],
            "max_rss_kib": rss_kib,
        },
        "t": t,
        "H": H,
        "d": f"{2*q}*{yname} - {t+1}",
        "normalizer": {
            "g1": _scalar_text(field, g1, yname),
            "g2": _scalar_text(field, g2, yname),
            "g3": _scalar_text(field, g, yname),
            "c": _scalar_text(field, c, yname),
        },
        "b1_divisibility_pivot": {
            "coefficient": _scalar_text(field, b1_coefficient, yname),
            "inverse": _scalar_text(field, b1_inverse, yname),
            "rhs": b1_rhs.text(yname),
        },
        "B0_gauge_pivot": {
            "coefficient": _scalar_text(field, B0_coefficient, yname),
            "inverse": _scalar_text(field, B0_inverse, yname),
            "rhs": B0_rhs.text(yname),
        },
        "high_pivots": pivot_record,
        "terminal_variables": residual_variables,
        "terminal": terminal,
        "elapsed_seconds": elapsed,
    }
    say(f"stage=complete rows={len(terminal)} pivots={len(pivot_record)+2} "
        f"seconds={elapsed:.3f} max_rss_kib={rss_kib}")
    return record


def compare_reference(record: dict, path: pathlib.Path) -> None:
    """Exact coefficientwise comparison to a charged small-t record."""
    reference = json.loads(path.read_text(encoding="utf-8"))
    t = int(record["t"])
    if int(reference["t"]) != t:
        raise AssertionError("reference t differs")
    q = 2*t+1
    yname = f"q{q}_1"
    field = QuadraticField(t)
    names = (["b1", "b2", "b3", "b4", "B0"]
             + [f"q{j}_0" for j in range(2, 2*t+1)]
             + [f"C{j}" for j in range(1, t)])
    ring = SparseRing(field, names)

    def same(left: str, right: str, label: str) -> None:
        if parse_exact(left, ring, yname) != parse_exact(right, ring, yname):
            raise AssertionError(f"reference mismatch: {label}")

    for key in ("g1", "g2", "g3", "c"):
        same(record["normalizer"][key], reference["normalizer"][key],
             "normalizer."+key)
    for family in ("b1_divisibility_pivot", "B0_gauge_pivot"):
        for key in ("coefficient", "inverse", "rhs"):
            same(record[family][key], reference[family][key], family+"."+key)
    if [(row["band"], row["variable"]) for row in record["high_pivots"]] != [
            (row["band"], row["variable"]) for row in reference["high_pivots"]]:
        raise AssertionError("high pivot order differs")
    for number, (left, right) in enumerate(zip(record["high_pivots"],
                                               reference["high_pivots"])):
        for key in ("coefficient", "inverse", "rhs"):
            same(left[key], right[key], f"high_pivots[{number}].{key}")
    if record["terminal_variables"] != reference["terminal_variables"]:
        raise AssertionError("terminal variable order differs")
    if [row["band"] for row in record["terminal"]] != [
            row["band"] for row in reference["terminal"]]:
        raise AssertionError("terminal band order differs")
    for left, right in zip(record["terminal"], reference["terminal"]):
        same(left["expr"], right["expr"], f"terminal band {left['band']}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("t", type=int, nargs="+", help="stable parameters (t >= 2)")
    parser.add_argument("--output-dir", type=pathlib.Path, default=HERE)
    parser.add_argument(
        "--self-test", action="store_true",
        help="compare each generated t to terminal_laurent_t<t>.json when present")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for t in args.t:
        record = build(t, progress=not args.quiet)
        if args.self_test:
            reference = REFERENCE_DIR/f"terminal_laurent_t{t}.json"
            if not reference.exists():
                raise FileNotFoundError(reference)
            compare_reference(record, reference)
            print(f"FAST_LAURENT_REFERENCE_PASS t={t} reference={reference}", flush=True)
        path = args.output_dir/f"terminal_laurent_fast_t{t}.json"
        path.write_text(json.dumps(record, indent=2, sort_keys=True)+"\n",
                        encoding="utf-8")
        print(json.dumps({
            "t": t,
            "pivots": len(record["high_pivots"])+2,
            "terminal_rows": len(record["terminal"]),
            "terminal_variables": record["terminal_variables"],
            "elapsed_seconds": record["elapsed_seconds"],
            "max_rss_kib": record["backend"]["max_rss_kib"],
            "path": str(path),
        }, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
