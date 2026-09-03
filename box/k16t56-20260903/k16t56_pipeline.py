#!/usr/bin/env python3
"""Canonical-order normalisation of the gauged K=16 order chart at a fixed t.

Pipeline (proof-preserving quotient-ring maps only):
  gauged chart (t_order_system.py)
  -> Q*-constant triangular pivots (triangular_preprocess.py)
  -> weighted x=1 slice, H_t, A_t = Q[y]/(H_t)
  -> affine unit pivots in CANONICAL order
       (band index descending, then original chart-parameter order)
  -> terminal system in A_t[remaining] and its Q[y] section
  -> Singular emitters (modular F_p[y,vars]+H, exact A_t extension, Q[y]+H)

Every A_t pivot records Res_y(H_t, coefficient); a zero resultant is refused.
This program may invoke Singular when --run-singular is given.
"""

from __future__ import annotations

import argparse
import dataclasses
import hashlib
import importlib.util
import json
import os
import pathlib
import subprocess
import sys
import time
from typing import Iterable

import sympy as sp


os.environ.setdefault("OMP_NUM_THREADS", "1")

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
LANE_INPUTS = pathlib.Path("/tmp/jc2-lane.AdwiWa/inputs")
EXPECTED = {
    "t_order_system.py":
        "e115d576e850523f8796008d1b9d7899382cbac918ac2e74419207d9e7e7dc28",
    "triangular_preprocess.py":
        "f2defb76d36172c541431b2fff04b34770438eef81167210fec404344fefbf93",
    "t4_order_system.py":
        "db5e54450444f27c56f00bbec287aea284c8dc190e0e549c2fea51e0dbdd6cee",
}

# Default modular primes.  Characteristic 2 is excluded (actual-pair uses 1/2).
DEFAULT_PRIMES = (32003, 32009, 32027)


def sha256_file(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_module(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot import %s" % path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def log(msg: str) -> None:
    print(msg, flush=True)


# ---------------------------------------------------------------------------
# Uniform formulas
# ---------------------------------------------------------------------------

def H_polynomial(t: int, y: sp.Symbol) -> sp.Expr:
    q = 2 * t + 1
    return 12 * q**2 * y**2 - 12 * q * (t + 1) * y + (t + 1) * (3 * t + 2)


def c_polynomial(t: int, y: sp.Symbol) -> sp.Expr:
    q = 2 * t + 1
    e = 3 * t + 1
    return t * e * y * ((t + 1) - 6 * q * y) / (6 * q**3)


def Hhat_polynomial(t: int, x: sp.Symbol, y: sp.Symbol) -> sp.Expr:
    q = 2 * t + 1
    return (12 * q**2 * y**2
            - 12 * q * (t + 1) * x**2 * y
            + (t + 1) * (3 * t + 2) * x**4)


def cimage_homogeneous(t: int, x: sp.Symbol, y: sp.Symbol) -> sp.Expr:
    q = 2 * t + 1
    e = 3 * t + 1
    return t * e * x * y * ((t + 1) * x**2 - 6 * q * y) / (6 * q**3)


def intrinsic_weight(basis: sp.Expr, data: dict) -> int:
    if basis == 1:
        return 0
    if basis == data["A"]:
        return 3
    if basis == data["B"]:
        return 2
    if basis == data["z"] or basis == sp.Symbol("gamma"):
        return 1
    raise AssertionError("unknown basis element %s" % basis)


def natural_weights(data: dict) -> dict[sp.Symbol, int]:
    weights: dict[sp.Symbol, int] = {}
    for index, b in enumerate(sp.symbols("b1:5"), start=1):
        weights[b] = index
    for prefix, spaces in (("a", data["alpha_spaces"]),
                           ("q", data["beta_spaces"])):
        for deficit, basis_space in spaces.items():
            for coordinate, basis in enumerate(basis_space):
                variable = sp.Symbol("%s%d_%d" % (prefix, deficit, coordinate))
                weights[variable] = 4 * deficit - intrinsic_weight(basis, data)
    weights[data["c"]] = 20 * data["t"] + 5
    return weights


def row_weight(expr: sp.Expr, variables: list[sp.Symbol],
               weights: dict) -> int:
    seen = {
        sum(power * weights[variable]
            for power, variable in zip(monomial, variables))
        for monomial, _coefficient in sp.Poly(expr, *variables, domain=sp.QQ).terms()
    }
    if len(seen) != 1:
        raise AssertionError("inhomogeneous row: %s" % sorted(seen))
    return seen.pop()


# ---------------------------------------------------------------------------
# A_t arithmetic: coefficients a + b y, with y^2 reduced by H
# ---------------------------------------------------------------------------

@dataclasses.dataclass(frozen=True)
class AtCoeff:
    a: sp.Rational
    b: sp.Rational

    def __bool__(self) -> bool:
        return self.a != 0 or self.b != 0

    def as_expr(self, y: sp.Symbol) -> sp.Expr:
        return sp.expand(self.a + self.b * y)

    def is_rational(self) -> bool:
        return self.b == 0


class AtAlgebra:
    """Separable rank-two algebra A_t = Q[y]/(H_t)."""

    def __init__(self, t: int, y: sp.Symbol):
        self.t = t
        self.y = y
        self.H = sp.expand(H_polynomial(t, y))
        self.hpoly = sp.Poly(self.H, y, domain=sp.QQ)
        if self.hpoly.degree() != 2:
            raise AssertionError("H_t is not quadratic")
        self.p2 = sp.Rational(self.hpoly.nth(2))
        self.p1 = sp.Rational(self.hpoly.nth(1))
        self.p0 = sp.Rational(self.hpoly.nth(0))
        self.content, primitive = self.hpoly.primitive()
        self.H_primitive = primitive.as_expr()
        self.disc = sp.discriminant(self.H, y)
        self.irreducible = bool(sp.Poly(self.H, y, domain=sp.QQ).is_irreducible)

    def reduce_poly(self, expr: sp.Expr) -> AtCoeff:
        """Reduce a Q(y) element to a + b y in A_t."""
        expr = sp.together(sp.expand(expr))
        if expr == 0:
            return AtCoeff(sp.Rational(0), sp.Rational(0))
        num, den = sp.fraction(expr)
        num_poly = sp.Poly(sp.expand(num), self.y, domain=sp.QQ)
        den_poly = sp.Poly(sp.expand(den), self.y, domain=sp.QQ)
        if den_poly == 0:
            raise ZeroDivisionError("zero denominator in A_t coefficient")
        num_red = num_poly.rem(self.hpoly)
        den_red = den_poly.rem(self.hpoly)
        if den_red.degree() < 0 or den_red == 0:
            raise ZeroDivisionError("denominator vanishes in A_t")
        inv = sp.invert(den_red, self.hpoly)
        prod = (num_red * inv).rem(self.hpoly)
        a = sp.Rational(prod.nth(0)) if prod.degree() >= 0 else sp.Rational(0)
        b = sp.Rational(prod.nth(1)) if prod.degree() >= 1 else sp.Rational(0)
        return AtCoeff(a, b)

    def mul(self, u: AtCoeff, v: AtCoeff) -> AtCoeff:
        # (a+by)(c+dy) = ac + (ad+bc)y + bd y^2, y^2 = -(p1 y + p0)/p2
        ac = u.a * v.a
        cross = u.a * v.b + u.b * v.a
        bd = u.b * v.b
        const = ac - bd * self.p0 / self.p2
        lin = cross - bd * self.p1 / self.p2
        return AtCoeff(sp.Rational(const), sp.Rational(lin))

    def add(self, u: AtCoeff, v: AtCoeff) -> AtCoeff:
        return AtCoeff(u.a + v.a, u.b + v.b)

    def sub(self, u: AtCoeff, v: AtCoeff) -> AtCoeff:
        return AtCoeff(u.a - v.a, u.b - v.b)

    def neg(self, u: AtCoeff) -> AtCoeff:
        return AtCoeff(-u.a, -u.b)

    def scale(self, u: AtCoeff, q: sp.Rational) -> AtCoeff:
        return AtCoeff(u.a * q, u.b * q)

    def resultant(self, coeff: AtCoeff) -> sp.Expr:
        poly = sp.Poly(coeff.as_expr(self.y), self.y, domain=sp.QQ)
        return sp.resultant(self.hpoly, poly)

    def inverse(self, coeff: AtCoeff) -> AtCoeff:
        if not coeff:
            raise ZeroDivisionError("zero coefficient in A_t")
        res = self.resultant(coeff)
        if res == 0:
            raise ZeroDivisionError("nonunit coefficient in A_t: resultant 0")
        inv_poly = sp.invert(
            sp.Poly(coeff.as_expr(self.y), self.y, domain=sp.QQ),
            self.hpoly,
        )
        a = sp.Rational(inv_poly.nth(0)) if inv_poly.degree() >= 0 else sp.Rational(0)
        b = sp.Rational(inv_poly.nth(1)) if inv_poly.degree() >= 1 else sp.Rational(0)
        product = self.mul(coeff, AtCoeff(a, b))
        if product != AtCoeff(sp.Rational(1), sp.Rational(0)):
            raise AssertionError("inverse identity failed in A_t")
        return AtCoeff(a, b)


def drop_index(exponents: tuple[int, ...], index: int) -> tuple[int, ...]:
    return exponents[:index] + exponents[index + 1:]


class SparseAtPoly:
    """Sparse polynomial in remaining chart variables with coefficients in A_t."""

    __slots__ = ("gens", "terms")

    def __init__(self, gens: list[sp.Symbol],
                 terms: dict[tuple[int, ...], AtCoeff] | None = None):
        self.gens = list(gens)
        self.terms: dict[tuple[int, ...], AtCoeff] = {}
        if terms:
            for exponents, coeff in terms.items():
                if coeff:
                    self.terms[exponents] = coeff

    def is_zero(self) -> bool:
        return not self.terms

    def copy(self) -> "SparseAtPoly":
        return SparseAtPoly(self.gens, dict(self.terms))

    def as_expr(self, y: sp.Symbol) -> sp.Expr:
        acc = sp.Integer(0)
        for exponents, coeff in self.terms.items():
            monomial = sp.Integer(1)
            for variable, power in zip(self.gens, exponents):
                if power:
                    monomial *= variable**power
            acc += coeff.as_expr(y) * monomial
        return sp.expand(acc)

    def total_degree(self) -> int:
        if not self.terms:
            return -1
        return max(sum(exponents) for exponents in self.terms)

    def support_variables(self) -> set[sp.Symbol]:
        seen: set[sp.Symbol] = set()
        for exponents in self.terms:
            for variable, power in zip(self.gens, exponents):
                if power:
                    seen.add(variable)
        return seen

    def nterms(self) -> int:
        return len(self.terms)

    def add_inplace(self, other: "SparseAtPoly", algebra: AtAlgebra) -> None:
        for exponents, coeff in other.terms.items():
            current = self.terms.get(exponents)
            if current is None:
                self.terms[exponents] = coeff
            else:
                summed = algebra.add(current, coeff)
                if summed:
                    self.terms[exponents] = summed
                else:
                    del self.terms[exponents]

    def scale_inplace(self, scalar: AtCoeff, algebra: AtAlgebra) -> None:
        if not scalar:
            self.terms.clear()
            return
        updated: dict[tuple[int, ...], AtCoeff] = {}
        for exponents, coeff in self.terms.items():
            product = algebra.mul(coeff, scalar)
            if product:
                updated[exponents] = product
        self.terms = updated

    def drop_variable(self, index: int) -> "SparseAtPoly":
        gens = self.gens[:index] + self.gens[index + 1:]
        terms: dict[tuple[int, ...], AtCoeff] = {}
        for exponents, coeff in self.terms.items():
            if exponents[index] != 0:
                raise AssertionError("cannot drop a variable still in support")
            terms[drop_index(exponents, index)] = coeff
        return SparseAtPoly(gens, terms)


def from_sympy(expr: sp.Expr, gens: list[sp.Symbol],
               algebra: AtAlgebra) -> SparseAtPoly:
    expr = sp.expand(expr)
    if expr == 0:
        return SparseAtPoly(gens)
    if not gens:
        return SparseAtPoly(gens, {(): algebra.reduce_poly(expr)})
    poly = sp.Poly(expr, *gens, domain=sp.QQ.frac_field(algebra.y))
    terms: dict[tuple[int, ...], AtCoeff] = {}
    for exponents, coeff in poly.terms():
        reduced = algebra.reduce_poly(coeff)
        if reduced:
            terms[tuple(int(e) for e in exponents)] = reduced
    return SparseAtPoly(gens, terms)


def try_affine(poly: SparseAtPoly, index: int
               ) -> tuple[AtCoeff, SparseAtPoly] | None:
    """Return (coeff in A_t, remainder) if poly = coeff * gens[index] + remainder."""
    coeff_acc: AtCoeff | None = None
    remainder_terms: dict[tuple[int, ...], AtCoeff] = {}
    for exponents, coeff in poly.terms.items():
        power = exponents[index]
        if power == 0:
            remainder_terms[exponents] = coeff
        elif power == 1:
            rest = drop_index(exponents, index)
            if any(rest):
                return None
            coeff_acc = coeff if coeff_acc is None else AtCoeff(
                coeff_acc.a + coeff.a, coeff_acc.b + coeff.b)
        else:
            return None
    if coeff_acc is None or not coeff_acc:
        return None
    remainder = SparseAtPoly(poly.gens, remainder_terms)
    return coeff_acc, remainder


def substitute_linear(poly: SparseAtPoly, index: int, rhs: SparseAtPoly,
                      algebra: AtAlgebra) -> SparseAtPoly:
    """Replace gens[index] by rhs.  rhs must not involve gens[index]."""
    n = len(poly.gens)
    out = SparseAtPoly(poly.gens)
    # Precompute powers of rhs up to the max exponent of gens[index].
    max_exp = 0
    for exponents in poly.terms:
        if exponents[index] > max_exp:
            max_exp = exponents[index]
    powers = [SparseAtPoly(poly.gens, {tuple(0 for _ in range(n)):
                                       AtCoeff(sp.Rational(1), sp.Rational(0))})]
    for _ in range(max_exp):
        powers.append(mul_sparse(powers[-1], rhs, algebra))
    for exponents, coeff in poly.terms.items():
        k = exponents[index]
        base_exp = list(exponents)
        base_exp[index] = 0
        base = SparseAtPoly(poly.gens, {tuple(base_exp): coeff})
        piece = mul_sparse(base, powers[k], algebra)
        out.add_inplace(piece, algebra)
    return out


def mul_sparse(left: SparseAtPoly, right: SparseAtPoly,
               algebra: AtAlgebra) -> SparseAtPoly:
    out = SparseAtPoly(left.gens)
    for e1, c1 in left.terms.items():
        for e2, c2 in right.terms.items():
            exponents = tuple(a + b for a, b in zip(e1, e2))
            product = algebra.mul(c1, c2)
            if not product:
                continue
            current = out.terms.get(exponents)
            if current is None:
                out.terms[exponents] = product
            else:
                summed = algebra.add(current, product)
                if summed:
                    out.terms[exponents] = summed
                else:
                    del out.terms[exponents]
    return out


@dataclasses.dataclass
class SliceRow:
    source_index: int
    h_power: int
    monomial: tuple[int, int]
    poly: SparseAtPoly
    expr_Q: sp.Expr  # degree-<2 section, as a Q[y] polynomial


@dataclasses.dataclass
class APivot:
    step: int
    source_index: int
    h_power: int
    monomial: tuple[int, int]
    variable: str
    coefficient: str
    inverse: str
    resultant: str
    resultant_factorization: str
    band: int
    rows_after: int
    vars_after: int
    terms_after: int


def row_sort_key(row: SliceRow, position: int):
    return (-row.h_power, row.monomial[0], row.monomial[1],
            row.source_index, position)


def choose_canonical(rows: list[SliceRow], remaining: list[sp.Symbol],
                     algebra: AtAlgebra):
    """First affine unit pivot in canonical order.

    Row order: band (h-power) descending, then (gamma, pi) ascending,
    then original source index.  Variable order: the surviving original
    gauged-chart parameter order (remaining list).
    """
    for position, row in sorted(enumerate(rows),
                                key=lambda item: row_sort_key(item[1], item[0])):
        for index, _variable in enumerate(remaining):
            affine = try_affine(row.poly, index)
            if affine is None:
                continue
            coeff, remainder = affine
            resultant = algebra.resultant(coeff)
            if resultant == 0:
                continue
            return position, index, coeff, remainder, resultant
    return None


def choose_heuristic(rows: list[SliceRow], remaining: list[sp.Symbol],
                     algebra: AtAlgebra):
    """Banked t=2/3/4 score: short remainder and rare variable, then source."""
    occurrences = []
    for index, variable in enumerate(remaining):
        count = 0
        for row in rows:
            for exponents in row.poly.terms:
                if exponents[index]:
                    count += 1
                    break
        occurrences.append(count)
    best = None
    for position, row in enumerate(rows):
        for index, _variable in enumerate(remaining):
            affine = try_affine(row.poly, index)
            if affine is None:
                continue
            coeff, remainder = affine
            resultant = algebra.resultant(coeff)
            if resultant == 0:
                continue
            score = (
                remainder.nterms() * occurrences[index],
                remainder.nterms(),
                occurrences[index],
                row.poly.nterms(),
                row.source_index,
                index,
            )
            candidate = (score, position, index, coeff, remainder, resultant)
            if best is None or candidate[0] < best[0]:
                best = candidate
    if best is None:
        return None
    _score, position, index, coeff, remainder, resultant = best
    return position, index, coeff, remainder, resultant


def deduplicate(rows: list[SliceRow]) -> tuple[list[SliceRow], list[dict]]:
    kept: list[SliceRow] = []
    dropped: list[dict] = []
    seen: dict[tuple, int] = {}
    for row in rows:
        if row.poly.is_zero():
            dropped.append({"source_index": row.source_index,
                            "reason": "zero_mod_H"})
            continue
        key = tuple(sorted(
            (exponents, (str(coeff.a), str(coeff.b)))
            for exponents, coeff in row.poly.terms.items()
        ))
        if key in seen:
            dropped.append({
                "source_index": row.source_index,
                "reason": "literal_duplicate_mod_H",
                "representative_source_index": seen[key],
            })
        else:
            seen[key] = row.source_index
            kept.append(row)
    return kept, dropped


def eliminate_over_at(rows: list[SliceRow], remaining: list[sp.Symbol],
                      algebra: AtAlgebra, order: str,
                      max_seconds: float, max_terms: int):
    started = time.monotonic()
    remaining = list(remaining)
    rows, dropped = deduplicate(rows)
    pivots: list[APivot] = []
    terminal_unit = None
    chooser = choose_canonical if order == "canonical" else choose_heuristic

    while True:
        elapsed = time.monotonic() - started
        if elapsed > max_seconds:
            raise RuntimeError("A_t elimination exceeded %.1fs" % max_seconds)
        constants = [row for row in rows
                     if not row.poly.support_variables()]
        unit_constant = None
        for row in sorted(constants, key=lambda r: (r.poly.nterms(),
                                                    r.source_index)):
            coeff = row.poly.terms.get(
                tuple(), AtCoeff(sp.Rational(0), sp.Rational(0)))
            try:
                inverse = algebra.inverse(coeff)
            except ZeroDivisionError:
                continue
            unit_constant = (row, coeff, inverse)
            break
        if unit_constant is not None:
            row, coeff, inverse = unit_constant
            terminal_unit = {
                "source_index": row.source_index,
                "constant": str(coeff.as_expr(algebra.y)),
                "inverse": str(inverse.as_expr(algebra.y)),
                "resultant": str(algebra.resultant(coeff)),
            }
            break
        choice = chooser(rows, remaining, algebra)
        if choice is None:
            break
        position, index, coeff, remainder, resultant = choice
        pivot_row = rows[position]
        variable = remaining[index]
        inverse = algebra.inverse(coeff)
        # rhs = -inverse * remainder
        rhs = remainder.copy()
        rhs.scale_inplace(algebra.neg(inverse), algebra)
        # Kill the pivot row by construction; still verify the sparse identity.
        check = substitute_linear(pivot_row.poly, index, rhs, algebra)
        if not check.is_zero():
            raise AssertionError("A_t pivot does not kill its row")
        del rows[position]
        next_rows: list[SliceRow] = []
        for row in rows:
            if any(exponents[index] for exponents in row.poly.terms):
                new_poly = substitute_linear(row.poly, index, rhs, algebra)
            else:
                new_poly = row.poly.copy()
            new_poly = new_poly.drop_variable(index)
            next_rows.append(SliceRow(
                row.source_index, row.h_power, row.monomial, new_poly,
                sp.Integer(0),
            ))
        remaining = remaining[:index] + remaining[index + 1:]
        rows, newly = deduplicate(next_rows)
        dropped.extend(newly)
        terms_after = sum(row.poly.nterms() for row in rows)
        if terms_after > max_terms:
            raise RuntimeError("A_t residual exceeded term bound %d" % max_terms)
        pivots.append(APivot(
            step=len(pivots) + 1,
            source_index=pivot_row.source_index,
            h_power=pivot_row.h_power,
            monomial=pivot_row.monomial,
            variable=str(variable),
            coefficient=str(coeff.as_expr(algebra.y)),
            inverse=str(inverse.as_expr(algebra.y)),
            resultant=str(resultant),
            resultant_factorization=str({
                "numer": {str(p): int(e) for p, e in
                          sp.factorint(int(sp.numer(sp.together(resultant)))).items()},
                "denom": {str(p): int(e) for p, e in
                          sp.factorint(int(sp.denom(sp.together(resultant)))).items()},
            }),
            band=pivot_row.h_power,
            rows_after=len(rows),
            vars_after=len(remaining),
            terms_after=terms_after,
        ))
        log("A_PIVOT step=%d source=%d band=%d var=%s rows=%d vars=%d terms=%d res=%s"
            % (len(pivots), pivot_row.source_index, pivot_row.h_power,
               variable, len(rows), len(remaining), terms_after, resultant))
    return rows, remaining, pivots, dropped, terminal_unit, time.monotonic() - started


# ---------------------------------------------------------------------------
# Singular emitters
# ---------------------------------------------------------------------------

def actual_pair_lines(characteristic: int | str = 0) -> list[str]:
    field = str(characteristic)
    return [
        "ring RAC=%s,(gamma,pi),dp;" % field,
        "poly FAC=pi;",
        "poly GAC=pi-(gamma^2)/2;",
        "poly JAC=diff(FAC,gamma)*diff(GAC,pi)-diff(FAC,pi)*diff(GAC,gamma);",
        'if (JAC==gamma) { print("CONTROL_ACTUAL_PAIR_PASS J=gamma"); }'
        ' else { print("CONTROL_ACTUAL_PAIR_FAIL"); }',
        'if (nameof(basering)=="RAC") { print("CONTROL_RAC_RING_PASS"); }'
        ' else { print("CONTROL_RAC_RING_FAIL"); }',
    ]


def wrapper_controls(ring_name: str, unit_var: str, tag: str) -> list[str]:
    T = "W" if unit_var != "T" else "S"
    return [
        "ideal %sE=%s,%s*%s-1;" % (tag, unit_var, T, unit_var),
        "ideal %sGE=std(%sE);" % (tag, tag),
        'if (typeof(%sGE)=="ideal" && nameof(basering)=="%s")'
        ' { print("CONTROL_%s_EMPTY_EXTRACT_RING_PASS"); }'
        ' else { print("CONTROL_%s_EMPTY_EXTRACT_RING_FAIL"); }' % (
            tag, ring_name, tag, tag),
        'if (reduce(1,%sGE)==0) { print("CONTROL_%s_EMPTY_PASS"); }'
        ' else { print("CONTROL_%s_EMPTY_FAIL"); }' % (tag, tag, tag),
        "ideal %sN=%s-1,%s*%s-1;" % (tag, unit_var, T, unit_var),
        "ideal %sGN=std(%sN);" % (tag, tag),
        'if (typeof(%sGN)=="ideal" && nameof(basering)=="%s")'
        ' { print("CONTROL_%s_NONEMPTY_EXTRACT_RING_PASS"); }'
        ' else { print("CONTROL_%s_NONEMPTY_EXTRACT_RING_FAIL"); }' % (
            tag, ring_name, tag, tag),
        'if (reduce(1,%sGN)!=0) { print("CONTROL_%s_NONEMPTY_PASS"); }'
        ' else { print("CONTROL_%s_NONEMPTY_FAIL"); }' % (tag, tag, tag),
    ]


def emit_qhy(t: int, H: sp.Expr, y: sp.Symbol, remaining: list[sp.Symbol],
             generators: list[str], cbar: str, characteristic: int,
             method: str) -> str:
    """Ideal (H, terminal gens) in F[y, remaining], F = Q or GF(p)."""
    field = "0" if characteristic == 0 else str(characteristic)
    variables = [str(y)] + [str(v) for v in remaining] + ["W"]
    H_text = str(H).replace("**", "^")
    lines = [
        "// t=%d terminal + H_t in %s[y, remaining]; method=%s"
        % (t, "Q" if characteristic == 0 else "GF(%d)" % characteristic, method),
        'LIB "elim.lib";',
        *actual_pair_lines(field),
        "ring R=%s,(%s),dp;" % (field, ",".join(variables)),
        "option(redSB);",
        'if (nameof(basering)=="R") { print("CONTROL_RING_PASS R"); }'
        ' else { print("CONTROL_RING_FAIL"); }',
        *wrapper_controls("R", str(y), "R"),
        "// cbar=%s  (unit check lives in the A_t extension ring)"
        % cbar.replace("**", "^"),
        'print("MAIN_START t=%d char=%s rows=%d vars=%d plus_H=1 method=%s");'
        % (t, field, len(generators), len(remaining), method),
        "ideal I=%s;" % ",\n".join([H_text] + generators),
        "ideal G=%s(I);" % method,
        'print("MAIN_DONE basis_size=");',
        "size(G);",
        'if (typeof(G)=="ideal" && nameof(basering)=="R")'
        ' { print("MAIN_EXTRACT_RING_PASS"); }'
        ' else { print("MAIN_EXTRACT_RING_FAIL"); }',
        'if (reduce(1,G)==0) { print("MAIN_SATURATED_EMPTY"); G; }'
        ' else { print("MAIN_NONTRIVIAL");'
        ' print("BASIS_OUTPUT_TRUNCATED_TO_10");'
        ' int basis_cap=size(G); if (basis_cap>10) { basis_cap=10; }'
        ' for (int basis_i=1; basis_i<=basis_cap; basis_i++)'
        ' { G[basis_i]; } }',
        "quit;",
    ]
    return "\n".join(lines) + "\n"


def emit_extension(t: int, H: sp.Expr, y: sp.Symbol, remaining: list[sp.Symbol],
                   generators: list[str], cbar: str, method: str) -> str:
    """std / nfmodStd over the algebraic extension Q(y)/(H)."""
    H_text = str(H).replace("**", "^")
    varlist = ",".join([str(v) for v in remaining] + ["W"]) if remaining else "dummy,W"
    lines = [
        "// t=%d exact over A_t=Q[%s]/(%s); method=%s"
        % (t, y, H_text, method),
        'LIB "resources.lib";',
        "setcores(1);",
        'LIB "nfmodstd.lib";' if method == "nfmodStd" else 'LIB "elim.lib";',
        *actual_pair_lines(0),
        "ring RC=(0,%s),(u,W),dp;" % y,
        "minpoly=%s;" % H_text,
        "number cbar=%s;" % cbar.replace("**", "^"),
        "number cbar_inverse=1/cbar;",
        'if (cbar*cbar_inverse==1) { print("CONTROL_C_UNIT_PASS"); }'
        ' else { print("CONTROL_C_UNIT_FAIL"); }',
        'if (nameof(basering)=="RC") { print("CONTROL_RC_RING_PASS"); }'
        ' else { print("CONTROL_RC_RING_FAIL"); }',
        *wrapper_controls("RC", "u", "RC"),
        "ring RK=(0,%s),(%s),dp;" % (y, varlist),
        "minpoly=%s;" % H_text,
        "option(redSB);",
        'if (nameof(basering)=="RK") { print("CONTROL_RK_RING_PASS"); }'
        ' else { print("CONTROL_RK_RING_FAIL"); }',
        *wrapper_controls("RK", str(remaining[0]) if remaining else "dummy", "RK"),
        'print("MAIN_START t=%d field=At rows=%d vars=%d method=%s");'
        % (t, len(generators), len(remaining), method),
        "ideal I=%s;" % (",\n".join(generators) if generators else "0"),
        "ideal G=%s(I);" % method,
        'print("MAIN_DONE basis_size=");',
        "size(G);",
        'if (typeof(G)=="ideal" && nameof(basering)=="RK")'
        ' { print("MAIN_EXTRACT_RING_PASS"); }'
        ' else { print("MAIN_EXTRACT_RING_FAIL"); }',
        'if (reduce(1,G)==0) { print("MAIN_EXACT_UNIT"); G; }'
        ' else { print("MAIN_NONUNIT");'
        ' print("BASIS_OUTPUT_TRUNCATED_TO_10");'
        ' int basis_cap=size(G); if (basis_cap>10) { basis_cap=10; }'
        ' for (int basis_i=1; basis_i<=basis_cap; basis_i++)'
        ' { G[basis_i]; } }',
        "quit;",
    ]
    return "\n".join(lines) + "\n"


def emit_actual_pair_classifier() -> str:
    """Standalone negative classifier: (pi, pi-gamma^2/2) fails the K=16 tuple."""
    return "\n".join([
        "// semantic negative classifier; not a chart point",
        *actual_pair_lines(0),
        'print("TUPLE_CHECK n=deg_pi(F) m=deg_pi(G) J=gamma");',
        "deg(FAC,pi);",
        "deg(GAC,pi);",
        'print("K16_TUPLE_FAIL pi_degrees_are_1_1_not_12t+4_8t+4");',
        "quit;",
    ]) + "\n"


def run_singular(path: pathlib.Path, out_path: pathlib.Path,
                 err_path: pathlib.Path, timeout: int) -> dict:
    started = time.monotonic()
    try:
        proc = subprocess.run(
            ["/usr/bin/time", "-v", "Singular", "-q", str(path)],
            capture_output=True, text=True, timeout=timeout, check=False,
        )
        out_path.write_text(proc.stdout)
        err_path.write_text(proc.stderr)
        elapsed = time.monotonic() - started
        unit = "MAIN_SATURATED_EMPTY" in proc.stdout or "MAIN_EXACT_UNIT" in proc.stdout \
            or "MAIN_QUADRATIC_FIELD_EMPTY" in proc.stdout
        nontrivial = "MAIN_NONTRIVIAL" in proc.stdout or "MAIN_NONUNIT" in proc.stdout \
            or "MAIN_QUADRATIC_FIELD_NONTRIVIAL" in proc.stdout
        return {
            "input": path.name,
            "input_sha256": sha256_file(path),
            "exit": proc.returncode,
            "elapsed_seconds": round(elapsed, 3),
            "stdout_bytes": len(proc.stdout),
            "stderr_bytes": len(proc.stderr),
            "unit": unit,
            "nontrivial": nontrivial,
            "actual_pair_pass": "CONTROL_ACTUAL_PAIR_PASS" in proc.stdout,
            "timeout": False,
        }
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout or b""
        stderr = exc.stderr or b""
        if isinstance(stdout, bytes):
            stdout = stdout.decode("utf-8", "replace")
        if isinstance(stderr, bytes):
            stderr = stderr.decode("utf-8", "replace")
        out_path.write_text(stdout)
        err_path.write_text(stderr + "\nTIMEOUT\n")
        return {
            "input": path.name,
            "input_sha256": sha256_file(path),
            "exit": 124,
            "elapsed_seconds": timeout,
            "unit": False,
            "nontrivial": False,
            "timeout": True,
        }


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def rational_associate(left: sp.Expr, right: sp.Expr,
                       variables: list[sp.Symbol]):
    L = sp.Poly(left, *variables, domain=sp.QQ)
    R = sp.Poly(right, *variables, domain=sp.QQ)
    if L.is_zero or R.is_zero:
        return None
    ratio = sp.Rational(L.LC(), R.LC())
    return ratio if (L - ratio * R).is_zero else None


def write_tsv(path: pathlib.Path, header: str, rows: Iterable[str]) -> None:
    path.write_text(header + "\n" + "\n".join(rows) + "\n", encoding="utf-8")


def run_pipeline(t: int, order: str, out_dir: pathlib.Path,
                 max_q_seconds: float, max_a_seconds: float,
                 max_expression_bytes: int, max_terms: int,
                 primes: tuple[int, ...], run_singular: bool,
                 singular_timeout: int, skip_a: bool) -> dict:
    out_dir.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()

    for name, expected in EXPECTED.items():
        path = LANE_INPUTS / name
        if not path.is_file():
            raise RuntimeError("missing frozen input %s" % name)
        actual = sha256_file(path)
        if actual != expected:
            raise RuntimeError("hash mismatch %s: %s" % (name, actual))
        log("HASH_OK %s %s" % (name, actual))

    generic = load_module(LANE_INPUTS / "t_order_system.py",
                          "k16t56_generic_%d" % t)
    tp = load_module(LANE_INPUTS / "triangular_preprocess.py",
                     "k16t56_tp_%d" % t)

    log("BUILD_CHART t=%d" % t)
    t0 = time.monotonic()
    data = generic.build(t=t, gauged=True)
    build_seconds = time.monotonic() - t0
    e, q = data["e"], data["q"]
    n_eq = len(data["tagged"])
    n_unk = len(data["params"]) + 1
    log("CHART t=%d tuple=(%d,%d;%d,3) (e,q)=(%d,%d) unknowns=%d equations=%d"
        % (t, 12 * t + 4, 8 * t + 4, 12 * t + 1, e, q, n_unk, n_eq))
    log("PHI radii=(-1,%d/%d) gauges=%s build_s=%.3f"
        % (t, e, data["gauged"], build_seconds))
    if n_unk != 9 * t + 9 or n_eq != 14 * t + 9:
        raise AssertionError("unexpected chart dimensions")

    if t == 4:
        dedicated = load_module(LANE_INPUTS / "t4_order_system.py",
                                "k16t56_t4_dedicated")
        tp.assert_same_chart(data, dedicated.build(gauged=True),
                             "generic t=4 vs dedicated t=4")
        log("T4_GENERIC_EQUALS_DEDICATED")

    # Actual-pair semantic control, independent of the chart.
    gamma, pi = sp.symbols("gamma pi")
    f, g = pi, pi - gamma**2 / 2
    actual_j = sp.expand(generic.jac(f, g))
    actual_ok = actual_j == gamma
    tuple_fail = (
        sp.degree(f, pi) == 1 and sp.degree(g, pi) == 1
        and (sp.degree(f, pi), sp.degree(g, pi)) != (12 * t + 4, 8 * t + 4)
    )
    log("ACTUAL_PAIR J=gamma %s; K16_TUPLE_FAIL %s" % (actual_ok, tuple_fail))
    assert actual_ok and tuple_fail

    log("Q_PIVOTS t=%d" % t)
    t0 = time.monotonic()
    reduction = tp.reduce_chart(
        data, max_pivots=512, max_seconds=max_q_seconds,
        max_expression_bytes=max_expression_bytes,
    )
    q_seconds = time.monotonic() - t0
    expected_q = 3 * t + 4
    log("Q_PIVOTS count=%d expected=%d residual_rows=%d residual_unknowns=%d s=%.3f"
        % (len(reduction.pivots), expected_q, len(reduction.rows),
           len(reduction.remaining_variables) + 1, q_seconds))
    if len(reduction.pivots) != expected_q:
        raise AssertionError("Q-pivot count is not 3t+4")
    q_bands = [p.h_power for p in reduction.pivots]
    log("Q_PIVOT_BANDS %s .. %s vars=%s"
        % (max(q_bands), min(q_bands),
           [str(p.variable) for p in reduction.pivots]))
    if max(q_bands) != 4 * t + 1 or min(q_bands) != 2 * t:
        raise AssertionError("Q-pivot bands are not 4t+1 down to 2t")

    weights = natural_weights(data)
    residual_variables = reduction.remaining_variables + [reduction.c]
    for variable in residual_variables:
        if variable not in weights:
            raise AssertionError("missing weight for %s" % variable)
    degrees = [row_weight(row.expr, residual_variables, weights)
               for row in reduction.rows]
    x = sp.Symbol("q%d_1" % (t + 1))
    y = sp.Symbol("q%d_1" % (2 * t + 1))
    if x not in residual_variables or y not in residual_variables:
        raise AssertionError("normalizer coordinates absent")
    log("GRADING x=%s wt=%d y=%s wt=%d c wt=%d homogeneous_rows=%d"
        % (x, weights[x], y, weights[y], weights[reduction.c], len(degrees)))
    if weights[x] != 4 * t + 1 or weights[y] != 8 * t + 2 \
            or weights[reduction.c] != 20 * t + 5:
        raise AssertionError("weight formulas failed")
    if min(weights.values()) <= 0:
        raise AssertionError("grading not positive")

    Hhat = Hhat_polynomial(t, x, y)
    H = H_polynomial(t, y)
    cimage = cimage_homogeneous(t, x, y)
    cbar = c_polynomial(t, y)

    c_rows = [row for row in reduction.rows if reduction.c in row.expr.free_symbols]
    if len(c_rows) != 1:
        raise AssertionError("expected one c row, got %d" % len(c_rows))
    c_row = c_rows[0]
    cc = sp.diff(c_row.expr, reduction.c)
    solved = sp.expand(-(c_row.expr - cc * reduction.c) / cc)
    if sp.expand(solved - cimage) != 0:
        raise AssertionError("c image differs from uniform formula")
    log("C_ROW source=%d band=%d image_ok" % (c_row.source_index, c_row.h_power))

    hmatches = []
    all_vars = residual_variables
    for row in reduction.rows:
        if row is c_row:
            continue
        if row.expr.free_symbols <= {x, y}:
            assoc = rational_associate(row.expr, Hhat, all_vars)
            if assoc is not None:
                hmatches.append((row, assoc))
    if len(hmatches) != 1:
        raise AssertionError("expected one H row, got %d" % len(hmatches))
    hrow, hassoc = hmatches[0]
    log("H_ROW source=%d band=%d associate=%s" % (
        hrow.source_index, hrow.h_power, hassoc))
    if sp.expand(Hhat.subs(x, 1) - H) != 0:
        raise AssertionError("H slice identity failed")

    algebra = AtAlgebra(t, y)
    log("H_t=%s primitive=%s disc=%s irreducible=%s content=%s"
        % (algebra.H, algebra.H_primitive, algebra.disc,
           algebra.irreducible, algebra.content))
    # Unit checks for y and the linear factor of c_t.
    for label, element in (
        ("y", AtCoeff(sp.Rational(0), sp.Rational(1))),
        ("linear", algebra.reduce_poly((t + 1) - 6 * (2 * t + 1) * y)),
        ("cbar", algebra.reduce_poly(cbar)),
    ):
        res = algebra.resultant(element)
        inv = algebra.inverse(element)
        log("UNIT %s res=%s inv=%s" % (label, res, inv.as_expr(y)))
        if res == 0:
            raise AssertionError("%s is not a unit in A_t" % label)

    auxiliary = [v for v in reduction.remaining_variables if v not in (x, y)]
    # Original chart-parameter order, minus Q-pivots, minus {x,y}.
    remaining_order = [v for v in reduction.remaining_variables if v not in (x, y)]

    # Slice x=1, drop c, primitive-associate over Q, then pass to A_t.
    sliced: list[SliceRow] = []
    q_dropped = []
    q_seen: dict[str, int] = {}
    for row in reduction.rows:
        if row is c_row:
            continue
        expr = sp.expand(row.expr.subs({x: 1, reduction.c: cbar},
                                       simultaneous=True))
        primitive, multiplier, _den, _content = tp.primitive_integer_polynomial(
            expr, [y] + remaining_order,
        )
        key = str(primitive.as_expr())
        if key in q_seen:
            q_dropped.append({"source_index": row.source_index,
                              "reason": "rational_associate_duplicate_over_Q",
                              "representative": q_seen[key],
                              "multiplier": str(multiplier)})
            continue
        q_seen[key] = row.source_index
        poly = from_sympy(primitive.as_expr(), remaining_order, algebra)
        sliced.append(SliceRow(row.source_index, row.h_power, row.monomial,
                               poly, poly.as_expr(y)))

    log("SLICE q_rows=%d auxiliaries=%d q_duplicates=%d"
        % (len(sliced), len(remaining_order), len(q_dropped)))

    if skip_a:
        audit = {
            "t": t, "stage": "slice",
            "chart": {"equations": n_eq, "unknowns": n_unk,
                      "build_seconds": build_seconds},
            "q_pivots": len(reduction.pivots),
        }
        (out_dir / ("t%d_partial.json" % t)).write_text(
            json.dumps(audit, indent=2, sort_keys=True) + "\n")
        return audit

    log("A_ELIM t=%d order=%s auxiliaries=%d rows=%d" % (
        t, order, len(remaining_order), len(sliced)))
    rows, remaining, pivots, dropped, terminal_unit, a_seconds = eliminate_over_at(
        sliced, remaining_order, algebra, order=order,
        max_seconds=max_a_seconds, max_terms=max_terms,
    )
    log("A_ELIM done pivots=%d residual_rows=%d residual_vars=%s unit=%s s=%.3f"
        % (len(pivots), len(rows), [str(v) for v in remaining],
           terminal_unit is not None, a_seconds))

    # Terminal polynomials over A_t and as Q[y] section (deg_y < 2).
    qy_variables = [y] + remaining
    terminal_records = []
    generator_lines = [
        "source_index\th_power\tgamma_power\tpi_power\ttotal_degree"
        "\tnterms\tprimitive_Q[y]\tA_t_section"
    ]
    generators_sing = []
    generators_qy = []
    for row in sorted(rows, key=lambda r: (r.h_power, r.monomial, r.source_index)):
        expr = row.poly.as_expr(y)
        degree = row.poly.total_degree()
        primitive, multiplier, _den, _content = tp.primitive_integer_polynomial(
            expr, qy_variables,
        )
        prim_expr = primitive.as_expr()
        sing = tp.singular_polynomial(prim_expr, qy_variables)
        # For the extension ring the generators live in A_t[remaining],
        # so emit the same primitive polynomial (y is the minpoly generator).
        generators_sing.append(sing)
        generators_qy.append(sing)
        terminal_records.append({
            "source_index": row.source_index,
            "h_power": row.h_power,
            "monomial": list(row.monomial),
            "total_degree": degree,
            "nterms": row.poly.nterms(),
            "support": [str(v) for v in sorted(row.poly.support_variables(),
                                               key=str)],
            "multiplier": str(multiplier),
            "primitive": str(prim_expr),
            "At_section": str(expr),
            "text_bytes": len(str(prim_expr)),
        })
        generator_lines.append(
            "%d\t%d\t%d\t%d\t%d\t%d\t%s\t%s"
            % (row.source_index, row.h_power, row.monomial[0], row.monomial[1],
               degree, row.poly.nterms(), prim_expr, expr)
        )

    gen_path = out_dir / ("t%d_%s_terminal.tsv" % (t, order))
    write_tsv(gen_path, generator_lines[0], generator_lines[1:])

    pivot_lines = [
        "step\tsource\tband\tgamma\tpi\tvariable\tcoefficient\tinverse"
        "\tresultant\tresultant_factorization\trows_after\tvars_after\tterms_after"
    ]
    pivot_rows = []
    for p in pivots:
        pivot_rows.append(
            "%d\t%d\t%d\t%d\t%d\t%s\t%s\t%s\t%s\t%s\t%d\t%d\t%d"
            % (p.step, p.source_index, p.band, p.monomial[0], p.monomial[1],
               p.variable, p.coefficient, p.inverse, p.resultant,
               p.resultant_factorization, p.rows_after, p.vars_after,
               p.terms_after)
        )
    pivot_path = out_dir / ("t%d_%s_A_pivots.tsv" % (t, order))
    write_tsv(pivot_path, pivot_lines[0], pivot_rows)

    q_pivot_lines = [
        "step\tsource\tband\tgamma\tpi\tvariable\tcoefficient"
    ]
    q_pivot_rows = [
        "%d\t%d\t%d\t%d\t%d\t%s\t%s"
        % (p.step, p.source_index, p.h_power, p.monomial[0], p.monomial[1],
           p.variable, p.coefficient)
        for p in reduction.pivots
    ]
    q_pivot_path = out_dir / ("t%d_Q_pivots.tsv" % t)
    write_tsv(q_pivot_path, q_pivot_lines[0], q_pivot_rows)

    cbar_sing = str(cbar).replace("**", "^")
    H_for_sing = algebra.H  # non-primitive is OK; content is a unit in Q
    exact_std = out_dir / ("t%d_%s_exact_At_std.sing" % (t, order))
    exact_nf = out_dir / ("t%d_%s_exact_At_nfmodStd.sing" % (t, order))
    exact_qhy = out_dir / ("t%d_%s_exact_QHy_std.sing" % (t, order))
    exact_std.write_text(emit_extension(
        t, H_for_sing, y, remaining, generators_sing, cbar_sing, "std"))
    exact_nf.write_text(emit_extension(
        t, H_for_sing, y, remaining, generators_sing, cbar_sing, "nfmodStd"))
    exact_qhy.write_text(emit_qhy(
        t, H_for_sing, y, remaining, generators_qy, cbar_sing, 0, "std"))

    mod_files = []
    for prime in primes:
        path = out_dir / ("t%d_%s_mod_p%d_std.sing" % (t, order, prime))
        path.write_text(emit_qhy(
            t, H_for_sing, y, remaining, generators_qy, cbar_sing, prime, "std"))
        mod_files.append(path)

    classifier = out_dir / "actual_pair_classifier.sing"
    classifier.write_text(emit_actual_pair_classifier())

    singular_results = []
    if run_singular:
        jobs = [(classifier, 30)]
        for path in mod_files:
            jobs.append((path, singular_timeout))
        # Exact Q[y]+H first (no minpoly irreducibility), then extension.
        jobs.append((exact_qhy, singular_timeout))
        if algebra.irreducible:
            jobs.append((exact_std, singular_timeout))
            jobs.append((exact_nf, singular_timeout))
        for path, timeout in jobs:
            outp = path.with_suffix(".out")
            errp = path.with_suffix(".err")
            log("SINGULAR %s timeout=%d" % (path.name, timeout))
            result = run_singular(path, outp, errp, timeout)
            log("SINGULAR_DONE %s exit=%s unit=%s elapsed=%.3f"
                % (path.name, result["exit"], result.get("unit"),
                   result["elapsed_seconds"]))
            singular_results.append(result)

    degrees_list = [rec["total_degree"] for rec in terminal_records]
    bands_list = [rec["h_power"] for rec in terminal_records]
    expected_terminal_rows = 2 * t
    expected_terminal_vars = t
    expected_degrees = list(range(4 * t + 1, 2 * t + 1, -1))
    expected_bands = list(range(0, 2 * t))
    pattern = {
        "terminal_rows": len(rows),
        "terminal_vars": len(remaining),
        "matches_2t_by_t": (
            len(rows) == expected_terminal_rows
            and len(remaining) == expected_terminal_vars
        ),
        "degrees": degrees_list,
        "degrees_sorted_desc": sorted(degrees_list, reverse=True),
        "expected_degrees_4t+1_down_to_2t+2": expected_degrees,
        "degrees_match_in_order": degrees_list == expected_degrees,
        "degrees_match_as_multiset": sorted(degrees_list, reverse=True) == expected_degrees,
        "bands": bands_list,
        "bands_sorted": sorted(set(bands_list)),
        "expected_bands_0_to_2t-1": expected_bands,
        "bands_match_in_order": bands_list == expected_bands,
        "all_tags_0_1": all(rec["monomial"] == [0, 1] for rec in terminal_records),
    }

    audit = {
        "t": t,
        "order": order,
        "tuple": [12 * t + 4, 8 * t + 4, 12 * t + 1, 3],
        "phi": [-1, "%d/%d" % (t, 3 * t + 1)],
        "gauges": ["alpha_t=0", "const(beta_q)=0", "const(alpha_e)=0"],
        "chart": {
            "equations": n_eq,
            "unknowns_including_c": n_unk,
            "expected_equations": 14 * t + 9,
            "expected_unknowns": 9 * t + 9,
            "build_seconds": round(build_seconds, 6),
            "h_powers": [int(k) for k in sorted(data["by_power"])],
        },
        "actual_pair": {
            "J_equals_gamma": True,
            "K16_tuple_fail": True,
            "pi_degrees": [1, 1],
        },
        "q_pivots": {
            "count": len(reduction.pivots),
            "expected": expected_q,
            "variables": [str(p.variable) for p in reduction.pivots],
            "coefficients": [str(p.coefficient) for p in reduction.pivots],
            "bands": q_bands,
            "highest": max(q_bands),
            "lowest": min(q_bands),
            "residual_rows": len(reduction.rows),
            "residual_unknowns_including_c": len(reduction.remaining_variables) + 1,
            "elapsed_seconds": round(q_seconds, 6),
            "all_Qstar": True,
        },
        "grading": {
            "x": str(x), "wt_x": weights[x],
            "y": str(y), "wt_y": weights[y],
            "wt_c": weights[reduction.c],
            "homogeneous_rows": len(degrees),
            "positive": True,
        },
        "normalizer": {
            "H": str(algebra.H),
            "H_primitive": str(algebra.H_primitive),
            "content": str(algebra.content),
            "disc": int(algebra.disc),
            "irreducible_over_Q": algebra.irreducible,
            "cbar": str(cbar),
            "square_free_part_of_3_t_plus_1": int(
                sp.Mul(*[p for p, e in sp.factorint(3 * (t + 1)).items()
                         if e % 2])
                if any(e % 2 for e in sp.factorint(3 * (t + 1)).values())
                else 1
            ),
            "H_row_source": hrow.source_index,
            "c_row_source": c_row.source_index,
        },
        "slice": {
            "q_rows": len(sliced) + len(q_dropped),
            "q_rows_after_dedup": len(sliced),
            "q_duplicates": q_dropped,
            "auxiliaries": [str(v) for v in remaining_order],
        },
        "a_pivots": {
            "order": order,
            "order_documentation": (
                "canonical: rows by (-h_power, gamma, pi, source_index); "
                "variables in surviving original gauged-chart parameter order. "
                "A pivot is accepted only if it is affine in that variable with "
                "coefficient in A_t and Res_y(H_t, coefficient) != 0."
                if order == "canonical" else
                "heuristic: banked short-remainder / rare-variable score"
            ),
            "count": len(pivots),
            "pivots": [dataclasses.asdict(p) for p in pivots],
            "dropped": dropped,
            "terminal_unit": terminal_unit,
            "elapsed_seconds": round(a_seconds, 6),
            "every_resultant_nonzero": all(p.resultant != "0" for p in pivots),
        },
        "terminal": {
            "variables": [str(v) for v in remaining],
            "rows": terminal_records,
            "pattern": pattern,
        },
        "artifacts": {
            gen_path.name: sha256_file(gen_path),
            pivot_path.name: sha256_file(pivot_path),
            q_pivot_path.name: sha256_file(q_pivot_path),
            exact_std.name: sha256_file(exact_std),
            exact_nf.name: sha256_file(exact_nf),
            exact_qhy.name: sha256_file(exact_qhy),
            **{p.name: sha256_file(p) for p in mod_files},
        },
        "singular": singular_results,
        "elapsed_seconds": round(time.monotonic() - started, 6),
        "canonical_pivot_order": {
            "row_key": "(-h_power, gamma_power, pi_power, source_index)",
            "variable_key": "original gauged chart parameter order, survivors only",
            "unit_test": "Res_y(H_t, coefficient) != 0",
        },
    }
    audit_path = out_dir / ("t%d_%s_audit.json" % (t, order))
    audit_path.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n",
                          encoding="utf-8")
    log("AUDIT %s sha256=%s" % (audit_path.name, sha256_file(audit_path)))
    summary = {
        "t": t, "order": order,
        "q_pivots": len(reduction.pivots),
        "a_pivots": len(pivots),
        "terminal_rows": len(rows),
        "terminal_vars": [str(v) for v in remaining],
        "degrees": degrees_list,
        "bands": bands_list,
        "pattern": pattern,
        "H_irreducible": algebra.irreducible,
        "terminal_unit": terminal_unit is not None,
        "singular_units": [s.get("unit") for s in singular_results],
        "elapsed": audit["elapsed_seconds"],
        "audit": audit_path.name,
        "audit_sha256": sha256_file(audit_path),
    }
    log("SUMMARY " + json.dumps(summary, sort_keys=True))
    return audit


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--t", type=int, required=True)
    parser.add_argument("--order", choices=("canonical", "heuristic"),
                        default="canonical")
    parser.add_argument("--out-dir", type=pathlib.Path, default=HERE)
    parser.add_argument("--max-q-seconds", type=float, default=900.0)
    parser.add_argument("--max-a-seconds", type=float, default=2400.0)
    parser.add_argument("--max-expression-bytes", type=int, default=80_000_000)
    parser.add_argument("--max-terms", type=int, default=2_000_000)
    parser.add_argument("--primes", type=int, nargs="+", default=list(DEFAULT_PRIMES))
    parser.add_argument("--run-singular", action="store_true")
    parser.add_argument("--singular-timeout", type=int, default=180)
    parser.add_argument("--skip-a", action="store_true")
    args = parser.parse_args()
    if args.t < 1:
        parser.error("t must be positive")
    run_pipeline(
        t=args.t, order=args.order, out_dir=args.out_dir,
        max_q_seconds=args.max_q_seconds, max_a_seconds=args.max_a_seconds,
        max_expression_bytes=args.max_expression_bytes, max_terms=args.max_terms,
        primes=tuple(args.primes), run_singular=args.run_singular,
        singular_timeout=args.singular_timeout, skip_a=args.skip_a,
    )


if __name__ == "__main__":
    main()
