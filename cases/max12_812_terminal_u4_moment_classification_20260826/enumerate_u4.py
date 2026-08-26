#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from dataclasses import dataclass
from fractions import Fraction
from functools import reduce
from typing import Iterable


@dataclass(frozen=True)
class Quad:
    """a+b*sqrt(d), with d squarefree; d=0 is the rational field."""

    d: int
    a: Fraction
    b: Fraction = Fraction(0)

    def __post_init__(self) -> None:
        if self.d == 0 and self.b != 0:
            raise ValueError("rational Quad cannot have a radical part")

    @staticmethod
    def rational(d: int, value: int | Fraction) -> "Quad":
        return Quad(d, Fraction(value), Fraction(0))

    def _coerce(self, other: int | Fraction | "Quad") -> "Quad":
        if isinstance(other, Quad):
            if other.d != self.d:
                raise ValueError(f"field mismatch {self.d} versus {other.d}")
            return other
        return Quad.rational(self.d, other)

    def __add__(self, other: int | Fraction | "Quad") -> "Quad":
        q = self._coerce(other)
        return Quad(self.d, self.a + q.a, self.b + q.b)

    __radd__ = __add__

    def __neg__(self) -> "Quad":
        return Quad(self.d, -self.a, -self.b)

    def __sub__(self, other: int | Fraction | "Quad") -> "Quad":
        return self + (-self._coerce(other))

    def __rsub__(self, other: int | Fraction | "Quad") -> "Quad":
        return self._coerce(other) - self

    def __mul__(self, other: int | Fraction | "Quad") -> "Quad":
        q = self._coerce(other)
        return Quad(
            self.d,
            self.a * q.a + self.b * q.b * self.d,
            self.a * q.b + self.b * q.a,
        )

    __rmul__ = __mul__

    def inverse(self) -> "Quad":
        norm = self.a * self.a - self.d * self.b * self.b
        if norm == 0:
            raise ZeroDivisionError("zero quadratic element")
        return Quad(self.d, self.a / norm, -self.b / norm)

    def __truediv__(self, other: int | Fraction | "Quad") -> "Quad":
        return self * self._coerce(other).inverse()

    def __rtruediv__(self, other: int | Fraction | "Quad") -> "Quad":
        return self._coerce(other) / self

    def __pow__(self, exponent: int) -> "Quad":
        if exponent < 0:
            return (self.inverse()) ** (-exponent)
        result = Quad.rational(self.d, 1)
        base = self
        power = exponent
        while power:
            if power & 1:
                result = result * base
            base = base * base
            power >>= 1
        return result

    def is_zero(self) -> bool:
        return self.a == 0 and self.b == 0

    def key(self) -> tuple[int, int, int, int, int]:
        return (
            self.d,
            self.a.numerator,
            self.a.denominator,
            self.b.numerator,
            self.b.denominator,
        )

    def text(self) -> str:
        if self.d == 0 or self.b == 0:
            return str(self.a)
        return f"({self.a})+({self.b})*sqrt({self.d})"


Poly = list[Quad]


def qzero(d: int) -> Quad:
    return Quad.rational(d, 0)


def trim(poly: Poly) -> Poly:
    result = poly[:]
    while len(result) > 1 and result[-1].is_zero():
        result.pop()
    return result


def padd(left: Poly, right: Poly) -> Poly:
    d = left[0].d
    out = [qzero(d) for _ in range(max(len(left), len(right)))]
    for i, value in enumerate(left):
        out[i] = out[i] + value
    for i, value in enumerate(right):
        out[i] = out[i] + value
    return trim(out)


def pneg(poly: Poly) -> Poly:
    return [-value for value in poly]


def psub(left: Poly, right: Poly) -> Poly:
    return padd(left, pneg(right))


def pmul(left: Poly, right: Poly) -> Poly:
    d = left[0].d
    out = [qzero(d) for _ in range(len(left) + len(right) - 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = out[i + j] + a * b
    return trim(out)


def ppow(poly: Poly, exponent: int) -> Poly:
    d = poly[0].d
    result = [Quad.rational(d, 1)]
    base = poly
    power = exponent
    while power:
        if power & 1:
            result = pmul(result, base)
        base = pmul(base, base)
        power >>= 1
    return result


def pderiv(poly: Poly) -> Poly:
    if len(poly) == 1:
        return [qzero(poly[0].d)]
    return trim([poly[i] * i for i in range(1, len(poly))])


def pdivmod(numer: Poly, denom: Poly) -> tuple[Poly, Poly]:
    denom = trim(denom)
    if len(denom) == 1 and denom[0].is_zero():
        raise ZeroDivisionError("zero polynomial")
    d = numer[0].d
    rem = trim(numer)
    if len(rem) < len(denom):
        return [qzero(d)], rem
    quot = [qzero(d) for _ in range(len(rem) - len(denom) + 1)]
    while not (len(rem) == 1 and rem[0].is_zero()) and len(rem) >= len(denom):
        shift = len(rem) - len(denom)
        coeff = rem[-1] / denom[-1]
        quot[shift] = quot[shift] + coeff
        subtractor = [qzero(d)] * shift + [coeff * value for value in denom]
        rem = trim(psub(rem, subtractor))
    return trim(quot), trim(rem)


def pmonic(poly: Poly) -> Poly:
    poly = trim(poly)
    if len(poly) == 1 and poly[0].is_zero():
        return poly
    lead = poly[-1]
    return [value / lead for value in poly]


def pgcd(left: Poly, right: Poly) -> Poly:
    a = trim(left)
    b = trim(right)
    while not (len(b) == 1 and b[0].is_zero()):
        _, rem = pdivmod(a, b)
        a, b = b, rem
    return pmonic(a)


def linear_factor(root: Quad) -> Poly:
    return [-root, Quad.rational(root.d, 1)]


def polynomial_from_weighted_roots(
    coordinates: tuple[Quad, ...], weights: tuple[int, ...], positive: bool
) -> Poly:
    d = coordinates[0].d
    result = [Quad.rational(d, 1)]
    for root, weight in zip(coordinates, weights):
        if (weight > 0) == positive:
            result = pmul(result, ppow(linear_factor(root), abs(weight)))
    return trim(result)


def squarefree_decomposition(value: int) -> tuple[int, int]:
    """Return outside,d with sqrt(value)=outside*sqrt(d), d squarefree."""
    if value == 0:
        return 0, 0
    sign = -1 if value < 0 else 1
    remaining = abs(value)
    outside = 1
    squarefree = 1
    prime = 2
    while prime * prime <= remaining:
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        outside *= prime ** (exponent // 2)
        if exponent % 2:
            squarefree *= prime
        prime += 1
    if remaining > 1:
        squarefree *= remaining
    return outside, sign * squarefree


def partitions(total: int, length: int, max_part: int) -> Iterable[tuple[int, ...]]:
    if length == 0:
        if total == 0:
            yield ()
        return
    upper = min(max_part, total - length + 1)
    for first in range(upper, 0, -1):
        for tail in partitions(total - first, length - 1, first):
            yield (first,) + tail


def canonical_configuration(weights: tuple[int, ...], coords: tuple[Quad, ...]) -> tuple:
    candidates = []
    for i in range(4):
        for j in range(4):
            if i == j:
                continue
            denominator = coords[j] - coords[i]
            if denominator.is_zero():
                raise AssertionError("collision in canonicalization")
            normalized = []
            for weight, coord in zip(weights, coords):
                value = (coord - coords[i]) / denominator
                normalized.append((weight, value.key()))
            candidates.append(tuple(sorted(normalized)))
    return min(candidates)


def solve_profile(weights: tuple[int, ...]) -> list[tuple[Quad, ...]]:
    n1, n2, n3, n4 = weights
    assert n1 + n2 + n3 + n4 == 0
    coefficient_a = n3 * (n1 + n2)
    coefficient_b = -2 * n2 * n3
    coefficient_c = n2 * (n1 + n3)
    roots: list[Quad] = []
    if coefficient_a == 0:
        x_rational = Fraction(-coefficient_c, coefficient_b)
        x = Quad(0, x_rational)
        roots.append(x)
    else:
        discriminant = coefficient_b * coefficient_b - 4 * coefficient_a * coefficient_c
        assert discriminant == 4 * n1 * n2 * n3 * n4
        outside, squarefree = squarefree_decomposition(discriminant)
        if squarefree == 1:
            for sign in (-1, 1):
                roots.append(
                    Quad(0, Fraction(-coefficient_b + sign * outside, 2 * coefficient_a))
                )
        else:
            for sign in (-1, 1):
                roots.append(
                    Quad(
                        squarefree,
                        Fraction(-coefficient_b, 2 * coefficient_a),
                        Fraction(sign * outside, 2 * coefficient_a),
                    )
                )

    solutions = []
    for x in roots:
        d = x.d
        zero = Quad.rational(d, 0)
        one = Quad.rational(d, 1)
        y = (n2 + n3 * x) / (n1 + n2 + n3)
        coords = (zero, one, x, y)
        if any(coords[i] == coords[j] for i in range(4) for j in range(i + 1, 4)):
            continue
        solutions.append(coords)
    return solutions


def verify_class(m: int, weights: tuple[int, ...], coords: tuple[Quad, ...]) -> dict:
    d = coords[0].d
    zero = Quad.rational(d, 0)
    moments = []
    for power in range(4):
        value = zero
        for weight, coord in zip(weights, coords):
            value = value + weight * (coord ** power)
        moments.append(value)
    if any(not moments[k].is_zero() for k in range(3)):
        raise AssertionError(f"moment failure {weights}: {moments}")
    if moments[3].is_zero():
        raise AssertionError(f"zero degree-three moment {weights}")

    poly_a = polynomial_from_weighted_roots(coords, weights, True)
    poly_b = polynomial_from_weighted_roots(coords, weights, False)
    if len(pgcd(poly_a, poly_b)) != 1:
        raise AssertionError("A/B collision")
    difference = trim(psub(poly_a, poly_b))
    degree = len(difference) - 1
    total_degree = sum(weight for weight in weights if weight > 0)
    if degree != total_degree - 3:
        raise AssertionError(f"wrong difference degree {degree} versus {total_degree - 3}")
    if degree > 0 and len(pgcd(difference, pderiv(difference))) != 1:
        raise AssertionError("A-B is not squarefree")

    wronskian = psub(pmul(pderiv(poly_a), poly_b), pmul(poly_a, pderiv(poly_b)))
    expected_factor = [Quad.rational(d, 1)]
    for coord, weight in zip(coords, weights):
        expected_factor = pmul(expected_factor, ppow(linear_factor(coord), abs(weight) - 1))
    quotient, remainder = pdivmod(wronskian, expected_factor)
    if not (len(remainder) == 1 and remainder[0].is_zero()):
        raise AssertionError("Wronskian factor remainder")
    if len(quotient) != 1 or quotient[0] != moments[3]:
        raise AssertionError(
            f"Wronskian constant mismatch {quotient[0].text()} versus {moments[3].text()}"
        )

    return {
        "field_squarefree_d": d,
        "coordinates": [coord.text() for coord in coords],
        "kappa": moments[3].text(),
        "difference_degree": degree,
        "radicand_exponents": [m - w if w > 0 else m + abs(w) for w in weights],
        "canonical": canonical_configuration(weights, coords),
    }


def classify(m: int) -> dict:
    profiles = []
    total_classes = 0
    viable_profiles = 0
    rational_classes = 0
    quadratic_classes = 0
    for positive_count in range(1, 4):
        negative_count = 4 - positive_count
        for total_degree in range(3, 3 * m + 1):
            for alpha in partitions(total_degree, positive_count, m):
                for beta in partitions(total_degree, negative_count, total_degree):
                    parts = alpha + beta
                    if math.gcd(m, *parts) != 1:
                        continue
                    weights = alpha + tuple(-value for value in beta)
                    raw_solutions = solve_profile(weights)
                    by_canonical: dict[tuple, dict] = {}
                    for coords in raw_solutions:
                        record = verify_class(m, weights, coords)
                        by_canonical.setdefault(record["canonical"], record)
                    tree_exists = 3 * reduce(math.gcd, parts) <= total_degree
                    if bool(by_canonical) != tree_exists:
                        raise AssertionError(
                            f"tree/moment existence mismatch m={m} alpha={alpha} beta={beta} "
                            f"tree={tree_exists} classes={len(by_canonical)}"
                        )
                    classes = []
                    for canonical in sorted(by_canonical):
                        record = dict(by_canonical[canonical])
                        record.pop("canonical")
                        classes.append(record)
                        if record["field_squarefree_d"] == 0:
                            rational_classes += 1
                        else:
                            quadratic_classes += 1
                    if classes:
                        viable_profiles += 1
                    total_classes += len(classes)
                    profiles.append(
                        {
                            "alpha": alpha,
                            "beta": beta,
                            "D": total_degree,
                            "tree_exists": tree_exists,
                            "class_count": len(classes),
                            "classes": classes,
                        }
                    )
    return {
        "m": m,
        "profiles_tested": len(profiles),
        "viable_profiles": viable_profiles,
        "total_affine_classes": total_classes,
        "rational_classes": rational_classes,
        "quadratic_classes": quadratic_classes,
        "profiles": profiles,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    payload = {
        "scope": "U=4 terminal moment equation only",
        "classification": [classify(2), classify(4)],
    }
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    with open(args.out, "wb") as handle:
        handle.write(encoded + b"\n")
    digest = hashlib.sha256(encoded + b"\n").hexdigest()
    for block in payload["classification"]:
        print(
            "SUMMARY",
            f"m={block['m']}",
            f"profiles={block['profiles_tested']}",
            f"viable={block['viable_profiles']}",
            f"classes={block['total_affine_classes']}",
            f"rational={block['rational_classes']}",
            f"quadratic={block['quadratic_classes']}",
        )
    print(f"payload_sha256={digest}")
    print("U4_TERMINAL_MOMENT_CLASSIFICATION_PASS")


if __name__ == "__main__":
    main()
