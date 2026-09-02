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


@dataclass(frozen=True)
class GeneratorBlock:
    """One named coefficient family, ordered from highest Z degree to zero."""

    name: str
    z_degrees: Tuple[Optional[int], ...]
    polynomials: Tuple[MPoly, ...] = field(repr=False)

    @property
    def generators(self) -> Tuple[str, ...]:
        return tuple(poly.render() for poly in self.polynomials)


@dataclass(frozen=True)
class CellSystem:
    """An exact finite coefficient system ready for qqideal/msolveio."""

    e: int
    U: int
    g: int
    m: int
    n: int
    sigma: int
    phi_degree: int
    pprime_degree: int
    wall_value: int
    wall_sign: int
    accelerators: bool
    variables: Tuple[str, ...]
    blocks: Tuple[GeneratorBlock, ...]

    @property
    def generators(self) -> Tuple[str, ...]:
        return tuple(g for block in self.blocks for g in block.generators)

    @property
    def generator_polynomials(self) -> Tuple[MPoly, ...]:
        return tuple(p for block in self.blocks for p in block.polynomials)

    @property
    def unknown_count(self) -> int:
        return len(self.variables)

    @property
    def generator_count(self) -> int:
        return sum(len(block.polynomials) for block in self.blocks)

    @property
    def block_counts(self) -> Dict[str, int]:
        return {block.name: len(block.polynomials) for block in self.blocks}

    def block(self, name: str) -> GeneratorBlock:
        for block in self.blocks:
            if block.name == name:
                return block
        raise KeyError(name)


FROZEN_INPUT_SHA256 = {
    "ray-kill-opus5-20260902.md": (
        "3d08b8996227e292d76e0ba3901cfad16099f347f97129d27b6bf5b3bc253f0a"
    ),
    "cell-32-termination-opus5-20260901.md": (
        "d1b5dc55f850c7b4215ba16a7143a52b96185574ed3c721c44da47b5e427b94b"
    ),
    "ray-kill-review-gpt55-20260902.md": (
        "df5612152d60496bb81311ee9183d3c580759a2549d6ea8945a487d284976fcf"
    ),
}


def _series(
    ring: CoefficientRing,
    prefix: str,
    degree: int,
    *,
    top: Optional[Number] = None,
) -> ZPoly:
    """Generic coefficient series, optionally replacing the leading variable."""
    if degree < 0:
        raise ValueError("series degree must be nonnegative")
    last_variable_degree = degree if top is None else degree - 1
    terms = {
        i: ring.variable(f"{prefix}{i}")
        for i in range(last_variable_degree + 1)
    }
    if top is not None:
        terms[degree] = ring.constant(top)
    return ZPoly(ring, terms)


def _coefficient_block(
    name: str,
    polynomial: ZPoly,
    expected_count: int,
) -> GeneratorBlock:
    """Extract all dense nonzero slots and fail closed on a degree mismatch."""
    if expected_count <= 0:
        raise AssertionError(f"{name}: nonpositive expected coefficient count")
    expected_top = expected_count - 1
    if polynomial.degree != expected_top:
        raise AssertionError(
            f"{name}: top degree {polynomial.degree}, expected {expected_top}"
        )
    degrees = tuple(range(expected_top, -1, -1))
    coefficients = tuple(polynomial.coefficient(degree) for degree in degrees)
    vanished = [degree for degree, coefficient in zip(degrees, coefficients) if coefficient.is_zero()]
    if vanished:
        raise AssertionError(f"{name}: identically zero coefficient slots {vanished}")
    return GeneratorBlock(name, tuple(degrees), coefficients)


def _scalar_block(name: str, polynomials: Iterable[MPoly]) -> GeneratorBlock:
    values = tuple(polynomials)
    if not values or any(value.is_zero() for value in values):
        raise AssertionError(f"{name}: scalar generator vanished")
    return GeneratorBlock(name, (None,) * len(values), values)


def expected_unknown_count(e: int, U: int) -> int:
    """RAY §4 table count after a=b=A_e=1 and the Wall-B substitution."""
    return (9 * U + 5 * e) // 2 + 6


def expected_generator_count(e: int, U: int, *, accelerators: bool = False) -> int:
    """Corrected coefficient count; RAY:406 omits e T1 slots and SAT."""
    base = (15 * U + 19 * e) // 2 + 5
    return base + (5 if accelerators else 0)


def build_cell(
    e: int,
    U: int,
    *,
    accelerators: bool = False,
    wall_sign: int = -1,
) -> CellSystem:
    """Construct the exact A2-E1WALL-CELLS coefficient system.

    ``wall_sign=-1`` is the only decisive setting and gives
    ``G_g=-(1+2e)``.  ``wall_sign=+1`` is exposed only for the charged broken-
    wall self-check; the runner refuses to solve that variant.  Optional
    accelerator rows are off by default.

    The boundary gate ``(1,3)`` and residual cells ``U>=3e+2`` both satisfy
    the accepted domain ``U>=3e``.  The wider domain also permits the measured
    boundary rows in RAY §4's count table.
    """
    for label, value in (("e", e), ("U", U)):
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{label} must be an integer")
    if e < 1:
        raise ValueError("A2-E1WALL-CELLS has e>=1")
    if U < 3 * e:
        raise ValueError("cell must satisfy U>=3e (gate) or U>=3e+2 (residual)")
    if (U - e) % 2:
        raise ValueError("cell must satisfy U congruent to e modulo 2")
    if wall_sign not in (-1, 1):
        raise ValueError("wall_sign must be -1 (charged) or +1 (broken control)")
    if not isinstance(accelerators, bool):
        raise TypeError("accelerators must be bool")
    if accelerators and U < 3 * e + 2:
        raise ValueError(
            "accelerator pins are scoped to surviving residual cells U>=3e+2, "
            "not the inhomogeneous item-0 boundary"
        )

    g = 2 * e
    m = U
    n = U - e
    sigma = (U + e) // 2
    phi_degree = sigma + e
    pprime_degree = 3 * n // 2 - 1
    if n % 2 or pprime_degree < 0:
        raise AssertionError("parity/domain did not make p' degree integral")

    variables = tuple(
        [f"A{i}" for i in range(e)]
        + [f"S{i}" for i in range(sigma + 1)]
        + [f"Q{i}" for i in range(m + 1)]
        + [f"R{i}" for i in range(n + 1)]
        + [f"G{i}" for i in range(g)]
        + [f"F{i}" for i in range(phi_degree + 1)]
        + [f"P{i}" for i in range(pprime_degree + 1)]
        + ["kappa", "tt"]
    )
    ring = CoefficientRing(variables)
    Z = ZPoly.monomial(ring, 1)
    d = Fraction(3, 2)

    # RAY:443--447: a=b=1, A_e=1, and Wall B G_g=-(1+2e).
    eta = _series(ring, "A", e, top=1)
    s = _series(ring, "S", sigma)
    q = _series(ring, "Q", m)
    r = _series(ring, "R", n)
    wall_value = wall_sign * (1 + 2 * e)
    G = _series(ring, "G", g, top=wall_value)
    Phi = _series(ring, "F", phi_degree)
    pprime = _series(ring, "P", pprime_degree)
    kappa = ZPoly.monomial(ring, 0, ring.variable("kappa"))

    derivative = ZPoly.derivative
    etap = derivative(eta)
    etapp = derivative(etap)
    sp = derivative(s)
    qp = derivative(q)
    rp = derivative(r)
    Gp = derivative(G)
    Phip = derivative(Phi)

    eta2 = eta ** 2
    eta3 = eta ** 3
    s2 = s ** 2
    G2 = G ** 2
    psi = eta + Z * etap
    chi = eta + 2 * Z * etap
    phi = eta + 3 * Z * etap
    E1 = eta * chi + G
    D1 = eta2 * phi + d * eta * G
    # C32:198--203 (C1 substitution); this is not itself EQ4.
    C1 = d * (psi * s + Fraction(1, 2) * Phi)

    # C32 (1.1), lines 99--105.
    EQ1 = (
        6 * D1 * rp
        - 4 * qp * E1
        + 2 * q * derivative(E1)
        + 4 * C1 * sp
        - 2 * derivative(C1) * s
        + 2 * kappa * Z
    )

    # C32:631--639, E2eq at G=0, with a=b=1 and d=3/2.
    E2G0 = (
        6 * Z * eta2 * (3 * eta + 4 * Z * etap) * rp
        + 2
        * (
            eta2 * q
            + 10 * Z * eta * etap * q
            + 4 * (Z ** 2) * (etap ** 2 + eta * etapp) * q
            - 6 * Z * eta2 * qp
            - 4 * (Z ** 2) * eta * etap * qp
        )
        + 12
        * Z
        * eta2
        * etap
        * (eta * etap - Z * (etap ** 2) + Z * eta * etapp)
        + 2
        * d
        * Z
        * (3 * eta * s * sp - 2 * (2 * etap + Z * etapp) * s2)
    )

    # C32:640--643, the complete live Delta_2; no leader/cap replacement.
    Delta2 = (
        6 * Z * eta2 * etap * Gp
        + 6 * eta * (eta * etap - 3 * Z * (etap ** 2) + Z * eta * etapp) * G
        + d * (eta * derivative(G2) - 4 * etap * G2)
        + 8 * d * Z * eta * G * rp
        + 4 * Z * (q * Gp - qp * G)
        + d * (Phi * s + 2 * Z * (Phi * sp - Phip * s))
    )
    EQ2 = E2G0 + Delta2

    # C32 T2, lines 249--255: all five families in the displayed order.
    Xi = (
        12 * eta3 * etap * (etap + 2 * Z * etapp)
        + 4 * d * s * (eta * sp - etap * s)
        + 8 * eta * (q * etap - qp * eta)
        + 12 * eta3 * rp
        + 12
        * eta
        * ((eta * etapp - etap ** 2) * G + eta * etap * Gp)
    )
    EQ3 = eta * (Z ** 2) * Xi - 3 * derivative(Z * eta2 * G2)

    # C32:583--590, the spec-(2.2) O0+E0 identity, resolved by REVIEW:247.
    EQ4 = 2 * (s * C1 - q * E1) * rp + kappa * E1 + q * s * sp - qp * s2

    # RAY:448--455.  Phi clears T1's divisibility without division by eta.
    T1 = eta * Phi - s * G
    E0 = 2 * (q * rp - pprime * s) - kappa

    expected_counts = {
        "EQ1": U + 2 * e,
        "EQ2": U + 2 * e + 1,
        "EQ3": 3 * e + U + 2,
        "EQ4": 2 * U + e,
        "T1": sigma + 2 * e + 1,
        "E0": 2 * U - e,
    }
    blocks: List[GeneratorBlock] = [
        _coefficient_block("EQ1", EQ1, expected_counts["EQ1"]),
        _coefficient_block("EQ2", EQ2, expected_counts["EQ2"]),
        _coefficient_block("EQ3", EQ3, expected_counts["EQ3"]),
        _coefficient_block("EQ4", EQ4, expected_counts["EQ4"]),
        _coefficient_block("T1", T1, expected_counts["T1"]),
        _coefficient_block("E0", E0, expected_counts["E0"]),
    ]

    # Explicit saturation: mandatory and unique; never wrap the ideal in sat().
    sat = (
        ring.variable(f"S{sigma}")
        * ring.variable(f"Q{m}")
        * ring.variable(f"R{n}")
        * ring.variable("kappa")
        * ring.variable("tt")
        - 1
    )
    blocks.append(_scalar_block("SAT", (sat,)))

    if accelerators:
        # RAY:456--461.  These five proved rows add no variables.
        Ssigma = ring.variable(f"S{sigma}")
        Sprev = ring.variable(f"S{sigma - 1}")
        Qm = ring.variable(f"Q{m}")
        Qprev = ring.variable(f"Q{m - 1}")
        Rn = ring.variable(f"R{n}")
        Rprev = ring.variable(f"R{n - 1}")
        Aprev = ring.variable(f"A{e - 1}")
        Gprev = ring.variable(f"G{g - 1}")
        pins = (
            4 * Rn - Ssigma ** 2,
            4 * Qm - 3 * (Ssigma ** 2),
            Gprev + 4 * e * Aprev,
            2 * Ssigma * Rn * Aprev - (2 * Sprev * Rn - Ssigma * Rprev),
            2 * Ssigma * Rn * Qprev
            - Qm * (2 * Sprev * Rn + Ssigma * Rprev),
        )
        blocks.append(_scalar_block("ACCEL", pins))

    system = CellSystem(
        e=e,
        U=U,
        g=g,
        m=m,
        n=n,
        sigma=sigma,
        phi_degree=phi_degree,
        pprime_degree=pprime_degree,
        wall_value=wall_value,
        wall_sign=wall_sign,
        accelerators=accelerators,
        variables=variables,
        blocks=tuple(blocks),
    )
    if system.unknown_count != expected_unknown_count(e, U):
        raise AssertionError(
            f"unknown count {system.unknown_count} != {expected_unknown_count(e, U)}"
        )
    if system.generator_count != expected_generator_count(e, U, accelerators=accelerators):
        raise AssertionError(
            f"generator count {system.generator_count} != "
            f"{expected_generator_count(e, U, accelerators=accelerators)}"
        )
    tt_rows = sum(poly.occurs("tt") for poly in system.generator_polynomials)
    if tt_rows != 1:
        raise AssertionError(f"saturation variable occurs in {tt_rows} generators")
    if f"S{sigma}" not in system.variables:
        raise AssertionError("illegal S_sigma normalization detected")
    return system


def build_qqideal(system: CellSystem, *, characteristic: int = 0):
    """Map a built system into an exact qqideal ring and ideal.

    This is a plain ideal because SAT is already a generator.  Calling
    ``Ideal.saturate`` or passing ``opens=`` here would change the system and is
    intentionally not offered.
    """
    if system.wall_sign != -1:
        raise ValueError("refusing to map the deliberately broken wall to a solve job")
    try:
        from qqideal import Ideal, Ring
    except ImportError as exc:
        raise RuntimeError(
            "qqideal 0.1.0 is required only for solver execution; "
            "build_cell and run_self_checks need no solver stack"
        ) from exc
    ring = Ring(*system.variables, characteristic=characteristic)
    ideal = Ideal(system.generators, ring=ring)
    if tuple(ideal.ring.names) != system.variables:
        raise AssertionError("qqideal ring-map name/order mismatch")
    if len(ideal.gens) != system.generator_count:
        raise AssertionError("qqideal generator-map count mismatch")
    if any(generator.ring != ring for generator in ideal.gens):
        raise AssertionError("qqideal generator image escaped the declared ring")
    return ideal


RAY_COUNT_TABLE: Tuple[Tuple[int, int, int, int], ...] = (
    # e, U, unknowns, equations -- RAY:412--420
    (1, 3, 22, 37),
    (1, 5, 31, 52),
    (1, 9, 49, 82),
    (2, 8, 47, 84),
    (3, 11, 63, 116),
    (4, 12, 70, 133),
    (5, 15, 86, 165),
)


RUN_CELLS: Tuple[Tuple[str, int, int], ...] = (
    ("item-0", 1, 3),
    ("item-1", 1, 5),
    ("item-1", 1, 7),
    ("item-1", 1, 9),
    ("item-1", 1, 11),
    ("item-1", 1, 13),
    ("item-2", 2, 8),
    ("item-2", 2, 10),
    ("item-2", 2, 12),
    ("item-3", 3, 11),
    ("item-3", 3, 13),
    ("item-4", 4, 14),
)


def run_self_checks() -> Tuple[bool, List[str]]:
    """Run the three charged checks with Fraction algebra and no msolve.

    Checks are intentionally made on the builder's coefficient slots, before
    qqideal is allowed to drop zero rows.  Any exception is typed as FAIL and
    returned to the runner; solver execution must not continue after a failure.
    """
    lines: List[str] = [
        "=== A2-E1WALL-CELLS self-checks (Fraction only; no msolve) ==="
    ]
    overall = True

    # (i) Measured RAY §4 table, including the exceptional (1,3) gate.
    count_ok = True
    lines.append("[i] charged unknown/generator counts")
    for e, U, expected_variables, expected_generators in RAY_COUNT_TABLE:
        try:
            system = build_cell(e, U)
            got = (system.unknown_count, system.generator_count)
            wanted = (expected_variables, expected_generators)
            match = got == wanted
            count_ok = count_ok and match
            lines.append(
                f"  ({e},{U}) vars/gens={got[0]}/{got[1]} "
                f"expected={wanted[0]}/{wanted[1]}: {'PASS' if match else 'FAIL'}"
            )
        except Exception as exc:  # noqa: BLE001 -- self-check records, then refuses solve
            count_ok = False
            lines.append(f"  ({e},{U}) EXCEPTION {type(exc).__name__}: {exc}")
    lines.append(f"CHECK(i) COUNTS: {'PASS' if count_ok else 'FAIL'}")
    overall = overall and count_ok

    # (ii) Flip only G_g.  The top T1 coefficient has a simple exact witness.
    wall_ok = False
    lines.append("[ii] deliberately broken wall G_g=+(1+2e)")
    try:
        good = build_cell(1, 3)
        broken = build_cell(1, 3, wall_sign=1)
        if good.variables != broken.variables:
            raise AssertionError("wall control changed the coefficient ring")
        if len(good.generator_polynomials) != len(broken.generator_polynomials):
            raise AssertionError("wall control changed the generator slot count")
        differences = tuple(
            left - right
            for left, right in zip(good.generator_polynomials, broken.generator_polynomials)
        )
        nonzero_differences = sum(not difference.is_zero() for difference in differences)
        top_difference = good.block("T1").polynomials[0] - broken.block("T1").polynomials[0]
        witness = 2 * (1 + 2 * good.e) * top_difference.ring.variable(f"S{good.sigma}")
        wall_ok = nonzero_differences > 0 and top_difference == witness
        lines.append(f"  nonzero generator-slot differences: {nonzero_differences}")
        lines.append(f"  top T1 good-broken: {top_difference.render()}")
        lines.append(f"  expected witness:   {witness.render()}")
    except Exception as exc:  # noqa: BLE001
        lines.append(f"  EXCEPTION {type(exc).__name__}: {exc}")
        wall_ok = False
    lines.append(f"CHECK(ii) BROKEN-WALL-DIFF: {'PASS' if wall_ok else 'FAIL'}")
    overall = overall and wall_ok

    # (iii) tt occurs in exactly the explicit saturation row.
    saturation_ok = False
    lines.append("[iii] saturation variable occurrence and exact row")
    try:
        system = build_cell(1, 3)
        occurrences = [
            (block.name, index)
            for block in system.blocks
            for index, polynomial in enumerate(block.polynomials)
            if polynomial.occurs("tt")
        ]
        ring = system.block("SAT").polynomials[0].ring
        expected_sat = (
            ring.variable(f"S{system.sigma}")
            * ring.variable(f"Q{system.m}")
            * ring.variable(f"R{system.n}")
            * ring.variable("kappa")
            * ring.variable("tt")
            - 1
        )
        sat_poly = system.block("SAT").polynomials[0]
        saturation_ok = occurrences == [("SAT", 0)] and sat_poly == expected_sat
        lines.append(f"  tt-bearing rows: {occurrences}")
        lines.append(f"  SAT: {sat_poly.render()}")
    except Exception as exc:  # noqa: BLE001
        lines.append(f"  EXCEPTION {type(exc).__name__}: {exc}")
        saturation_ok = False
    lines.append(
        f"CHECK(iii) SATURATION-EXACTLY-ONCE: {'PASS' if saturation_ok else 'FAIL'}"
    )
    overall = overall and saturation_ok

    # Accelerator policy and illegal S-normalization guard.
    policy_ok = False
    lines.append("[policy] accelerators default off; S_sigma remains a variable")
    try:
        base = build_cell(1, 5)
        accelerated = build_cell(1, 5, accelerators=True)
        policy_ok = (
            not base.accelerators
            and "ACCEL" not in base.block_counts
            and accelerated.block_counts.get("ACCEL") == 5
            and accelerated.generator_count == base.generator_count + 5
            and accelerated.variables == base.variables
            and f"S{base.sigma}" in base.variables
        )
        lines.append(
            f"  base/accelerated generators={base.generator_count}/"
            f"{accelerated.generator_count}; variables={base.unknown_count}"
        )
        lines.append(f"  S_sigma name retained: S{base.sigma}")
    except Exception as exc:  # noqa: BLE001
        lines.append(f"  EXCEPTION {type(exc).__name__}: {exc}")
        policy_ok = False
    lines.append(f"CHECK(policy): {'PASS' if policy_ok else 'FAIL'}")
    overall = overall and policy_ok

    lines.append(
        "SELF-CHECKS OVERALL: PASS" if overall else "SELF-CHECKS OVERALL: FAIL"
    )
    return overall, lines


if __name__ == "__main__":
    ok, transcript = run_self_checks()
    print("\n".join(transcript))
    raise SystemExit(0 if ok else 1)
