#!/usr/bin/env python3
"""Exact coefficient jobs for RAY §4.1 ``A2-E1WALL-CELLS``.

The builder is deliberately independent of sympy, qqideal, msolveio, and
msolve.  It expands in ``Z`` using :class:`fractions.Fraction` coefficients
and sparse multivariate coefficient polynomials.  The solver imports are
deferred to :func:`build_qqideal`, so the charged self-checks run on a machine
which has no solver stack.

Source correspondence (frozen charged inputs, one-based lines):

* CELL-32 99--105: EQ1, equation (1.1).
* CELL-32 631--643: EQ2 = E2eq|_{G=0} + Delta_2.
* CELL-32 241--255: EQ3 = eta*Z^2*Xi - 3*(Z*eta^2*G^2)'
  after the licensed a=b=1 normalization.
* CELL-32 583--590 and charged REVIEW 243--251: EQ4 is the O0+E0
  polynomial.  CELL-32 198--203 supplies the C1 substitution used inside it.
* RAY 443--455: degrees, Wall B, T1, E0, and the explicit saturation row.
* RAY 456--461: the five optional accelerator rows (off by default).

There is no ``sat()`` call here.  The generator
``S_sigma*Q_m*R_n*kappa*tt-1`` is part of every system, exactly once.
``S_sigma`` is never normalized.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from typing import Dict, Iterable, List, Mapping, Optional, Sequence, Tuple, Union


Number = Union[int, Fraction]
Monomial = Tuple[Tuple[int, int], ...]


def _merge_monomials(left: Monomial, right: Monomial) -> Monomial:
    """Multiply sparse monomials whose variable indices are sorted."""
    if not left:
        return right
    if not right:
        return left
    out: List[Tuple[int, int]] = []
    i = j = 0
    while i < len(left) and j < len(right):
        li, le = left[i]
        ri, re = right[j]
        if li < ri:
            out.append((li, le))
            i += 1
        elif ri < li:
            out.append((ri, re))
            j += 1
        else:
            out.append((li, le + re))
            i += 1
            j += 1
    out.extend(left[i:])
    out.extend(right[j:])
    return tuple(out)


@dataclass(frozen=True)
class CoefficientRing:
    """A declared coefficient-variable ring over QQ."""

    names: Tuple[str, ...]
    _index: Mapping[str, int] = field(init=False, repr=False, compare=False)

    def __post_init__(self) -> None:
        if not self.names:
            raise ValueError("the coefficient ring must have a variable")
        if len(set(self.names)) != len(self.names):
            raise ValueError("duplicate coefficient variable")
        for name in self.names:
            if not name or not name[0].isalpha() or not name.isalnum():
                raise ValueError(f"msolve-unsafe variable name: {name!r}")
        object.__setattr__(self, "_index", {n: i for i, n in enumerate(self.names)})

    def constant(self, value: Number) -> "MPoly":
        frac = Fraction(value)
        return MPoly(self, {} if frac == 0 else {(): frac})

    def variable(self, name: str) -> "MPoly":
        try:
            index = self._index[name]
        except KeyError as exc:
            raise KeyError(f"{name!r} is not in the declared ring") from exc
        return MPoly(self, {((index, 1),): Fraction(1)})


class MPoly:
    """Sparse multivariate polynomial over QQ in a :class:`CoefficientRing`."""

    __slots__ = ("ring", "terms")

    def __init__(
        self,
        ring: CoefficientRing,
        terms: Optional[Mapping[Monomial, Fraction]] = None,
    ) -> None:
        self.ring = ring
        clean: Dict[Monomial, Fraction] = {}
        if terms:
            for monomial, coefficient in terms.items():
                frac = Fraction(coefficient)
                if frac:
                    clean[tuple(monomial)] = frac
        self.terms = clean

    def _coerce(self, other: object) -> "MPoly":
        if isinstance(other, MPoly):
            if other.ring != self.ring:
                raise ValueError("coefficient-ring mismatch")
            return other
        if isinstance(other, (int, Fraction)) and not isinstance(other, bool):
            return self.ring.constant(other)
        return NotImplemented  # type: ignore[return-value]

    def __add__(self, other: object) -> "MPoly":
        rhs = self._coerce(other)
        if rhs is NotImplemented:
            return NotImplemented
        out = dict(self.terms)
        for monomial, coefficient in rhs.terms.items():
            value = out.get(monomial, Fraction(0)) + coefficient
            if value:
                out[monomial] = value
            else:
                out.pop(monomial, None)
        return MPoly(self.ring, out)

    def __radd__(self, other: object) -> "MPoly":
        return self + other

    def __neg__(self) -> "MPoly":
        return MPoly(self.ring, {m: -c for m, c in self.terms.items()})

    def __sub__(self, other: object) -> "MPoly":
        rhs = self._coerce(other)
        if rhs is NotImplemented:
            return NotImplemented
        return self + (-rhs)

    def __rsub__(self, other: object) -> "MPoly":
        lhs = self._coerce(other)
        if lhs is NotImplemented:
            return NotImplemented
        return lhs - self

    def __mul__(self, other: object) -> "MPoly":
        rhs = self._coerce(other)
        if rhs is NotImplemented:
            return NotImplemented
        if not self.terms or not rhs.terms:
            return self.ring.constant(0)
        out: Dict[Monomial, Fraction] = {}
        for left_monomial, left_coefficient in self.terms.items():
            for right_monomial, right_coefficient in rhs.terms.items():
                monomial = _merge_monomials(left_monomial, right_monomial)
                value = (
                    out.get(monomial, Fraction(0))
                    + left_coefficient * right_coefficient
                )
                if value:
                    out[monomial] = value
                else:
                    out.pop(monomial, None)
        return MPoly(self.ring, out)

    def __rmul__(self, other: object) -> "MPoly":
        return self * other

    def __pow__(self, exponent: int) -> "MPoly":
        if not isinstance(exponent, int) or isinstance(exponent, bool) or exponent < 0:
            raise ValueError("polynomial exponent must be a nonnegative integer")
        result = self.ring.constant(1)
        base = self
        power = exponent
        while power:
            if power & 1:
                result = result * base
            power >>= 1
            if power:
                base = base * base
        return result

    def __eq__(self, other: object) -> bool:
        return isinstance(other, MPoly) and self.ring == other.ring and self.terms == other.terms

    def is_zero(self) -> bool:
        return not self.terms

    def occurs(self, variable: str) -> bool:
        index = self.ring._index[variable]
        return any(any(i == index for i, _ in monomial) for monomial in self.terms)

    def render(self) -> str:
        """Render an expanded unique-monomial sum accepted by qqideal/msolveio."""
        if not self.terms:
            return "0"

        nvars = len(self.ring.names)

        def grevlex_key(item: Tuple[Monomial, Fraction]) -> Tuple[object, ...]:
            monomial = item[0]
            powers = dict(monomial)
            total = sum(powers.values())
            return (-total, tuple(-powers.get(i, 0) for i in range(nvars - 1, -1, -1)))

        pieces: List[str] = []
        for monomial, coefficient in sorted(self.terms.items(), key=grevlex_key):
            negative = coefficient < 0
            absolute = abs(coefficient)
            factors: List[str] = []
            for index, power in monomial:
                name = self.ring.names[index]
                factors.append(name if power == 1 else f"{name}^{power}")
            numerator = absolute.numerator
            denominator = absolute.denominator
            if not factors:
                body = str(numerator) if denominator == 1 else f"{numerator}/{denominator}"
            elif numerator == 1 and denominator == 1:
                body = "*".join(factors)
            else:
                coefficient_body = (
                    str(numerator)
                    if denominator == 1
                    else f"{numerator}/{denominator}"
                )
                body = "*".join([coefficient_body, *factors])
            if not pieces:
                pieces.append(("-" if negative else "") + body)
            else:
                pieces.append(("-" if negative else "+") + body)
        return "".join(pieces)


class ZPoly:
    """Sparse polynomial in Z with :class:`MPoly` coefficients."""

    __slots__ = ("ring", "terms")

    def __init__(
        self,
        ring: CoefficientRing,
        terms: Optional[Mapping[int, MPoly]] = None,
    ) -> None:
        self.ring = ring
        clean: Dict[int, MPoly] = {}
        if terms:
            for degree, coefficient in terms.items():
                if not isinstance(degree, int) or degree < 0:
                    raise ValueError("Z degree must be a nonnegative integer")
                if coefficient.ring != ring:
                    raise ValueError("coefficient-ring mismatch")
                if not coefficient.is_zero():
                    clean[degree] = coefficient
        self.terms = clean

    @classmethod
    def constant(cls, ring: CoefficientRing, value: Number) -> "ZPoly":
        coefficient = ring.constant(value)
        return cls(ring, {} if coefficient.is_zero() else {0: coefficient})

    @classmethod
    def monomial(cls, ring: CoefficientRing, degree: int, coefficient: object = 1) -> "ZPoly":
        if isinstance(coefficient, MPoly):
            coeff = coefficient
        elif isinstance(coefficient, (int, Fraction)) and not isinstance(coefficient, bool):
            coeff = ring.constant(coefficient)
        else:
            raise TypeError(f"unsupported coefficient {type(coefficient).__name__}")
        return cls(ring, {} if coeff.is_zero() else {degree: coeff})

    def _coerce(self, other: object) -> "ZPoly":
        if isinstance(other, ZPoly):
            if other.ring != self.ring:
                raise ValueError("coefficient-ring mismatch")
            return other
        if isinstance(other, MPoly):
            if other.ring != self.ring:
                raise ValueError("coefficient-ring mismatch")
            return ZPoly(self.ring, {} if other.is_zero() else {0: other})
        if isinstance(other, (int, Fraction)) and not isinstance(other, bool):
            return ZPoly.constant(self.ring, other)
        return NotImplemented  # type: ignore[return-value]

    def __add__(self, other: object) -> "ZPoly":
        rhs = self._coerce(other)
        if rhs is NotImplemented:
            return NotImplemented
        out = dict(self.terms)
        for degree, coefficient in rhs.terms.items():
            value = out.get(degree, self.ring.constant(0)) + coefficient
            if value.is_zero():
                out.pop(degree, None)
            else:
                out[degree] = value
        return ZPoly(self.ring, out)

    def __radd__(self, other: object) -> "ZPoly":
        return self + other

    def __neg__(self) -> "ZPoly":
        return ZPoly(self.ring, {d: -c for d, c in self.terms.items()})

    def __sub__(self, other: object) -> "ZPoly":
        rhs = self._coerce(other)
        if rhs is NotImplemented:
            return NotImplemented
        return self + (-rhs)

    def __rsub__(self, other: object) -> "ZPoly":
        lhs = self._coerce(other)
        if lhs is NotImplemented:
            return NotImplemented
        return lhs - self

    def __mul__(self, other: object) -> "ZPoly":
        rhs = self._coerce(other)
        if rhs is NotImplemented:
            return NotImplemented
        if not self.terms or not rhs.terms:
            return ZPoly.constant(self.ring, 0)
        out: Dict[int, MPoly] = {}
        for left_degree, left_coefficient in self.terms.items():
            for right_degree, right_coefficient in rhs.terms.items():
                degree = left_degree + right_degree
                product = left_coefficient * right_coefficient
                value = out.get(degree, self.ring.constant(0)) + product
                if value.is_zero():
                    out.pop(degree, None)
                else:
                    out[degree] = value
        return ZPoly(self.ring, out)

    def __rmul__(self, other: object) -> "ZPoly":
        return self * other

    def __pow__(self, exponent: int) -> "ZPoly":
        if not isinstance(exponent, int) or isinstance(exponent, bool) or exponent < 0:
            raise ValueError("polynomial exponent must be a nonnegative integer")
        result = ZPoly.constant(self.ring, 1)
        base = self
        power = exponent
        while power:
            if power & 1:
                result = result * base
            power >>= 1
            if power:
                base = base * base
        return result

    def derivative(self) -> "ZPoly":
        return ZPoly(
            self.ring,
            {
                degree - 1: degree * coefficient
                for degree, coefficient in self.terms.items()
                if degree
            },
        )

    def coefficient(self, degree: int) -> MPoly:
        return self.terms.get(degree, self.ring.constant(0))

    @property
    def degree(self) -> Optional[int]:
        return max(self.terms) if self.terms else None


