#!/usr/bin/env python3
"""Primitive-monodromy census for topological degrees 6 through 9.

This is the pure-Python fallback requested by APPROACHES.md, because GAP is
not installed on the machine used for the banked run.  The group list, GAP
IDs, names, orders, and available generator data come from the GAP PrimGrp
library (data/gps1.g, commit eac1e8cf43a9e20240397db00344f97fd24c0955,
file blob 9f8efb2cc5ef6baee485bed87004e66ce1f4410f).  Equivalent standard natural
generators are supplied where that file uses a family sentinel:

  https://github.com/gap-packages/primgrp/blob/eac1e8cf43a9e20240397db00344f97fd24c0955/data/gps1.g

No network access or third-party Python package is needed at run time.

Formalization
-------------
The merged survey leaves its bound N and the translation of a sheet-book
critical-value vertex into branch cycles unspecified.  This program therefore
does not silently set N = td-1.  It performs the strongest unambiguous finite
test available from the stated data:

* G is one of all primitive permutation groups of degree n = 6,7,8,9;
* the inertia at g-hat = infinity has one of the exact pole partitions derived
  from Sigray Props. 5.4--5.6 and the td-uniform pole-row arithmetic;
* G contains an element of that cycle type;
* the remaining inertia is unrestricted inside G.

The last condition is enough for a Hurwitz completion: append generators of G
and the inverse of the accumulated product.  The resulting product-one tuple
generates G, and Riemann existence gives a connected cover.  Its genus is
checked by Riemann--Hurwitz.  The reported support is an explicit witness
upper bound, NOT a minimum and NOT a proved sheet-frame cap.  The main table
also applies the proved singleton-pole b=1 entry kill; raw profiles are printed
separately.  The optional H5a/N1 gcd filter is not imposed.

The Orevkov/Moh (48,64), td=9 control has no generic-fibre g-hat passport in
the repository.  Orevkov's actual degree-9 boundary-component passport is
tested separately: (3^3), (4^2,1), (5,1^4), with an explicit genus-zero A9
tuple.  This boundary cover is an adjacent negative control, not silently
identified with g-hat.  We also give S_n completions for every surviving
sheet-derived infinity profile and replay the residue-A S6 control.

Usage:
  python3 cases/monodromy_td.py
  python3 cases/monodromy_td.py --details
  python3 cases/monodromy_td.py --json
  python3 cases/monodromy_td.py --check
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass
from functools import lru_cache
from itertools import combinations
from typing import Iterable, Iterator, Sequence


Perm = tuple[int, ...]
Profile = tuple[int, ...]

PRIMGRP_SOURCE = (
    "gap-packages/primgrp data/gps1.g commit "
    "eac1e8cf43a9e20240397db00344f97fd24c0955, file blob "
    "9f8efb2cc5ef6baee485bed87004e66ce1f4410f"
)


def identity(n: int) -> Perm:
    return tuple(range(n))


def compose(left: Perm, right: Perm) -> Perm:
    """Left-to-right page product: (left * right)(i) = right(left(i))."""
    assert len(left) == len(right)
    return tuple(right[left[i]] for i in range(len(left)))


def product(perms: Iterable[Perm], n: int) -> Perm:
    out = identity(n)
    for perm in perms:
        out = compose(out, perm)
    return out


def inverse(perm: Perm) -> Perm:
    out = [0] * len(perm)
    for i, image in enumerate(perm):
        out[image] = i
    return tuple(out)


def from_cycles(n: int, *cycles: Sequence[int]) -> Perm:
    """Construct a permutation from disjoint 1-based cycles."""
    out = list(range(n))
    used: set[int] = set()
    for raw_cycle in cycles:
        cycle = tuple(x - 1 for x in raw_cycle)
        assert len(cycle) >= 2
        assert all(0 <= x < n for x in cycle)
        assert not (used & set(cycle))
        used.update(cycle)
        for i, point in enumerate(cycle):
            out[point] = cycle[(i + 1) % len(cycle)]
    return tuple(out)


def cycle_type(perm: Perm, *, reduced: bool = False) -> Profile:
    seen = [False] * len(perm)
    lengths: list[int] = []
    for start in range(len(perm)):
        if seen[start]:
            continue
        point = start
        length = 0
        while not seen[point]:
            seen[point] = True
            point = perm[point]
            length += 1
        if not reduced or length > 1:
            lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def index(perm: Perm) -> int:
    """Riemann--Hurwitz contribution sum(e_p-1)."""
    return len(perm) - len(cycle_type(perm))


def ramified_points(perm: Perm) -> int:
    """Number of nontrivial cycles, i.e. ramified source points over a value."""
    return len(cycle_type(perm, reduced=True))


def closure(generators: Sequence[Perm]) -> frozenset[Perm]:
    assert generators
    n = len(generators[0])
    assert all(len(g) == n for g in generators)
    ident = identity(n)
    gens = tuple(dict.fromkeys((*generators, *(inverse(g) for g in generators))))
    elements = {ident}
    frontier = [ident]
    while frontier:
        current = frontier.pop()
        for gen in gens:
            nxt = compose(current, gen)
            if nxt not in elements:
                elements.add(nxt)
                frontier.append(nxt)
    return frozenset(elements)


def orbit(generators: Sequence[Perm], start: int = 0) -> frozenset[int]:
    gens = tuple((*generators, *(inverse(g) for g in generators)))
    seen = {start}
    frontier = [start]
    while frontier:
        point = frontier.pop()
        for gen in gens:
            image = gen[point]
            if image not in seen:
                seen.add(image)
                frontier.append(image)
    return frozenset(seen)


def is_transitive(generators: Sequence[Perm]) -> bool:
    return len(orbit(generators)) == len(generators[0])


def is_primitive(generators: Sequence[Perm]) -> bool:
    """Exact small-degree block test.

    A nontrivial block can be translated to contain point 0.  We enumerate
    all such subsets whose sizes divide n and test the block condition.
    """
    n = len(generators[0])
    if not is_transitive(generators):
        return False
    elements = closure(generators)
    points = tuple(range(1, n))
    for size in range(2, n):
        if n % size:
            continue
        for tail in combinations(points, size - 1):
            block = frozenset((0, *tail))
            valid = True
            for perm in elements:
                image = frozenset(perm[x] for x in block)
                if image != block and image & block:
                    valid = False
                    break
            if valid:
                return False
    return True


def affine_perm(p: int, dim: int, matrix: Sequence[Sequence[int]], shift: Sequence[int] | None = None) -> Perm:
    """Column-vector affine action x |-> matrix*x + shift over F_p."""
    points = list(_vectors(p, dim))
    numbering = {point: i for i, point in enumerate(points)}
    b = tuple(shift or (0,) * dim)
    out = []
    for vector in points:
        image = tuple(
            (sum(matrix[row][col] * vector[col] for col in range(dim)) + b[row]) % p
            for row in range(dim)
        )
        out.append(numbering[image])
    return tuple(out)


def _vectors(p: int, dim: int) -> Iterator[tuple[int, ...]]:
    for number in range(p**dim):
        digits = []
        value = number
        for _ in range(dim):
            digits.append(value % p)
            value //= p
        yield tuple(digits)


def affine_generators(p: int, dim: int, matrices: Sequence[Sequence[Sequence[int]]]) -> tuple[Perm, ...]:
    ident_matrix = tuple(tuple(int(i == j) for j in range(dim)) for i in range(dim))
    translations = []
    for i in range(dim):
        shift = [0] * dim
        shift[i] = 1
        translations.append(affine_perm(p, dim, ident_matrix, shift))
    linear = [affine_perm(p, dim, matrix) for matrix in matrices]
    return tuple((*translations, *linear))


def mobius_perm(p: int, matrix: tuple[tuple[int, int], tuple[int, int]]) -> Perm:
    """Action of a 2x2 matrix on P^1(F_p), numbered 0,...,p-1,infinity."""
    (a, b), (c, d) = matrix
    out = []
    for x in range(p):
        numerator = (a * x + b) % p
        denominator = (c * x + d) % p
        if denominator == 0:
            out.append(p)
        else:
            out.append((numerator * pow(denominator, -1, p)) % p)
    if c % p == 0:
        out.append(p)
    else:
        out.append((a * pow(c, -1, p)) % p)
    return tuple(out)


def alternating_generators(n: int) -> tuple[Perm, ...]:
    three_cycle = from_cycles(n, (1, 2, 3))
    long_even = (
        from_cycles(n, tuple(range(1, n + 1)))
        if n % 2 == 1
        else from_cycles(n, tuple(range(2, n + 1)))
    )
    return three_cycle, long_even


def symmetric_generators(n: int) -> tuple[Perm, ...]:
    return (
        from_cycles(n, tuple(range(1, n + 1))),
        from_cycles(n, (1, 2)),
    )


@dataclass(frozen=True)
class PrimitiveGroupSpec:
    degree: int
    gap_id: int
    name: str
    expected_order: int
    generators: tuple[Perm, ...]


@dataclass(frozen=True)
class PoleRow:
    """One Sigray pole vertex in the td-uniform arithmetic.

    With global type (alpha,beta), the row has
      (D,Dg)=a(alpha,beta), (P,Pg)=b(alpha,beta),
      Lambda=a*b*alpha*beta/nu.
    For nu>1, case A has nu|alpha and nu|(b*beta-1), while case B has
    nu|beta and nu|(b*alpha-1).  At nu=1 their puncture formulas coincide.
    Props. 5.4--5.6 then turn the row into the displayed full cycle partition
    above infinity (1-cycles included).
    """

    alpha: int
    beta: int
    a: int
    b: int
    nu: int
    case: str
    pole_mass: int
    profile: Profile


def primitive_group_specs() -> tuple[PrimitiveGroupSpec, ...]:
    specs: list[PrimitiveGroupSpec] = []

    def add(n: int, gap_id: int, name: str, order: int, gens: Sequence[Perm]) -> None:
        specs.append(PrimitiveGroupSpec(n, gap_id, name, order, tuple(gens)))

    # Degree 6: natural projective-line actions for PSL(2,5), PGL(2,5).
    psl_5 = (
        mobius_perm(5, ((1, 1), (0, 1))),
        mobius_perm(5, ((0, -1), (1, 0))),
    )
    add(6, 1, "PSL(2,5)", 60, psl_5)
    add(6, 2, "PGL(2,5)", 120, (*psl_5, mobius_perm(5, ((2, 0), (0, 1)))))
    add(6, 3, "A(6)", math.factorial(6) // 2, alternating_generators(6))
    add(6, 4, "S(6)", math.factorial(6), symmetric_generators(6))

    # Degree 7: affine prime-degree groups plus L(3,2), A7, S7.
    translation_7 = from_cycles(7, (1, 2, 3, 4, 5, 6, 7))

    def multiplier_7(a: int) -> Perm:
        return tuple((a * x) % 7 for x in range(7))

    add(7, 1, "C(7)", 7, (translation_7,))
    add(7, 2, "D(2*7)", 14, (translation_7, multiplier_7(6)))
    add(7, 3, "7:3", 21, (translation_7, multiplier_7(2)))
    add(7, 4, "AGL(1,7)", 42, (translation_7, multiplier_7(3)))
    add(
        7,
        5,
        "L(3,2)",
        168,
        (
            from_cycles(7, (1, 4), (6, 7)),
            from_cycles(7, (1, 3, 2), (4, 7, 5)),
        ),
    )
    add(7, 6, "A(7)", math.factorial(7) // 2, alternating_generators(7))
    add(7, 7, "S(7)", math.factorial(7), symmetric_generators(7))

    # Degree 8 affine groups; matrices are the PrimGrp gps1.g matrices.
    a8 = ((0, 1, 0), (0, 0, 1), (1, 1, 0))
    b8 = ((1, 0, 0), (0, 0, 1), (0, 1, 1))
    c8 = ((1, 0, 0), (0, 0, 1), (0, 1, 0))
    add(8, 1, "AGL(1,8)", 56, affine_generators(2, 3, (a8,)))
    add(8, 2, "AGammaL(1,8)", 168, affine_generators(2, 3, (a8, b8)))
    add(8, 3, "ASL(3,2)", 1344, affine_generators(2, 3, (a8, c8)))
    add(
        8,
        4,
        "PSL(2,7)",
        168,
        (
            from_cycles(8, (1, 2, 3, 4, 5, 6, 7)),
            from_cycles(8, (2, 3, 5), (4, 7, 6)),
            from_cycles(8, (1, 8), (2, 7), (3, 4), (5, 6)),
        ),
    )
    add(
        8,
        5,
        "PGL(2,7)",
        336,
        (
            from_cycles(8, (1, 2, 3, 4, 5, 6, 7)),
            from_cycles(8, (2, 4, 3, 7, 5, 6)),
            from_cycles(8, (1, 8), (2, 7), (3, 4), (5, 6)),
        ),
    )
    add(8, 6, "A(8)", math.factorial(8) // 2, alternating_generators(8))
    add(8, 7, "S(8)", math.factorial(8), symmetric_generators(8))

    # Degree 9 affine groups; in F_3, GAP's Z(3) is 2 and Z(3)^0 is 1.
    a9 = ((0, 1), (2, 0))
    b9 = ((1, 0), (0, 2))
    c9 = ((2, 2), (2, 1))
    d9 = ((0, 1), (1, 1))
    e9 = ((1, 0), (1, 2))
    f9 = ((1, 0), (1, 1))
    add(9, 1, "3^2:4", 36, affine_generators(3, 2, (a9,)))
    add(9, 2, "3^2:D(2*4)", 72, affine_generators(3, 2, (a9, b9)))
    add(9, 3, "3^2:Q(8)=M(9)", 72, affine_generators(3, 2, (a9, c9)))
    add(9, 4, "3^2:8=AGL(1,9)", 72, affine_generators(3, 2, (d9,)))
    add(9, 5, "AGammaL(1,9)", 144, affine_generators(3, 2, (e9, d9)))
    add(9, 6, "3^2:(2'A(4))", 216, affine_generators(3, 2, (a9, f9)))
    add(9, 7, "AGL(2,3)", 432, affine_generators(3, 2, (d9, f9)))
    add(
        9,
        8,
        "PSL(2,8)",
        504,
        (
            from_cycles(9, (1, 2, 3, 4, 5, 6, 7)),
            from_cycles(9, (1, 8), (2, 4), (3, 7), (5, 6)),
            from_cycles(9, (2, 7), (3, 6), (4, 5), (8, 9)),
        ),
    )
    add(
        9,
        9,
        "PGammaL(2,8)",
        1512,
        (
            from_cycles(9, (1, 2, 3, 4, 5, 6, 7)),
            from_cycles(9, (2, 3, 5), (4, 7, 6)),
            from_cycles(9, (1, 8), (2, 4), (3, 7), (5, 6)),
            from_cycles(9, (2, 7), (3, 6), (4, 5), (8, 9)),
        ),
    )
    add(9, 10, "A(9)", math.factorial(9) // 2, alternating_generators(9))
    add(9, 11, "S(9)", math.factorial(9), symmetric_generators(9))
    return tuple(specs)


def pole_rows(max_mass: int) -> tuple[PoleRow, ...]:
    """Enumerate exact Prop. 5.4--5.6 pole rows of mass <= max_mass."""
    rows: set[PoleRow] = set()
    for alpha in range(2, max_mass + 1):
        for beta in range(alpha + 1, max_mass + 1):
            if math.gcd(alpha, beta) != 1:
                continue
            for a in range(1, max_mass + 1):
                for b in range(1, max_mass + 1):
                    numerator = a * b * alpha * beta
                    for nu in range(1, beta + 1):
                        if numerator % nu:
                            continue
                        mass = numerator // nu
                        if mass > max_mass:
                            continue
                        pole_order = a * beta
                        p_degree = b * alpha
                        # Prop. 5.4 states its dichotomy for nu != 1.  At
                        # nu=1 both displayed puncture formulas reduce to P
                        # punctures of pole order Dg, so bank the row once.
                        if nu == 1:
                            profile = (pole_order,) * p_degree
                            rows.add(PoleRow(alpha, beta, a, b, nu, "nu=1", mass, profile))
                            continue
                        # Case A: p(eta)=p_star(eta^nu).  There are P/nu
                        # punctures, each of pole order Dg.
                        if alpha % nu == 0 and (b * beta - 1) % nu == 0:
                            assert p_degree % nu == 0
                            profile = (pole_order,) * (p_degree // nu)
                            rows.add(PoleRow(alpha, beta, a, b, nu, "A", mass, profile))
                        # Case B: p(eta)=eta*p_star(eta^nu).  The zero root
                        # gives pole order Dg/nu and the other orbits order Dg.
                        if beta % nu == 0 and (b * alpha - 1) % nu == 0:
                            assert (p_degree - 1) % nu == 0
                            assert pole_order % nu == 0
                            profile = (
                                (pole_order,) * ((p_degree - 1) // nu)
                                + (pole_order // nu,)
                            )
                            rows.add(
                                PoleRow(
                                    alpha,
                                    beta,
                                    a,
                                    b,
                                    nu,
                                    "B",
                                    mass,
                                    tuple(sorted(profile, reverse=True)),
                                )
                            )
    return tuple(
        sorted(
            rows,
            key=lambda row: (
                row.alpha,
                row.beta,
                row.pole_mass,
                row.a,
                row.b,
                row.nu,
                row.case,
                row.profile,
            ),
        )
    )


@lru_cache(maxsize=None)
def sheet_profile_configurations(n: int) -> dict[Profile, tuple[tuple[PoleRow, ...], ...]]:
    """All same-global-type pole configurations of total mass n, by profile."""
    rows = pole_rows(n)
    found: dict[Profile, list[tuple[PoleRow, ...]]] = {}

    def extend(candidates: tuple[PoleRow, ...], start: int, remaining: int, picked: tuple[PoleRow, ...]) -> None:
        if remaining == 0:
            profile = tuple(
                sorted(
                    (part for row in picked for part in row.profile),
                    reverse=True,
                )
            )
            assert sum(profile) == n
            found.setdefault(profile, []).append(picked)
            return
        for i in range(start, len(candidates)):
            row = candidates[i]
            if row.pole_mass <= remaining:
                extend(candidates, i, remaining - row.pole_mass, (*picked, row))

    types = sorted({(row.alpha, row.beta) for row in rows})
    for alpha, beta in types:
        candidates = tuple(row for row in rows if (row.alpha, row.beta) == (alpha, beta))
        extend(candidates, 0, n, ())
    return {profile: tuple(configs) for profile, configs in found.items()}


def configuration_survives_entry_filter(config: Sequence[PoleRow]) -> bool:
    """Apply only Prop. 8.4's proved singleton-pole b=1 kill.

    There is no promoted multi-pole analogue, so b=1 vertices in a multi-pole
    configuration remain.  The optional H5a/N1 condition gcd(a,nu)=1 is not
    imposed here.
    """
    return not (len(config) == 1 and config[0].b == 1)


def sheet_profiles(n: int, *, entry_filtered: bool = True) -> tuple[Profile, ...]:
    configs = sheet_profile_configurations(n)
    profiles = (
        profile
        for profile, choices in configs.items()
        if not entry_filtered or any(configuration_survives_entry_filter(choice) for choice in choices)
    )
    return tuple(sorted(profiles, reverse=True))


def hurwitz_genus(branch_cycles: Sequence[Perm]) -> int:
    n = len(branch_cycles[0])
    ramification = sum(index(perm) for perm in branch_cycles)
    numerator = ramification - 2 * n + 2
    assert numerator % 2 == 0
    return numerator // 2


def database_witness(spec: PrimitiveGroupSpec, sigma_infinity: Perm) -> tuple[Perm, ...]:
    """Deterministic product-one generating tuple containing sigma_infinity."""
    prefix = [sigma_infinity, *spec.generators]
    closing = inverse(product(prefix, spec.degree))
    if closing != identity(spec.degree):
        prefix.append(closing)
    witness = tuple(prefix)
    assert product(witness, spec.degree) == identity(spec.degree)
    return witness


def transpositions_for_cycle_inverse(perm: Perm) -> list[Perm]:
    """Transposition factorization whose left-to-right product is perm^-1."""
    n = len(perm)
    out: list[Perm] = []
    seen: set[int] = set()
    for start in range(n):
        if start in seen:
            continue
        cycle = []
        point = start
        while point not in seen:
            seen.add(point)
            cycle.append(point)
            point = perm[point]
        # Under the page-product convention, the reversed star factors
        # multiply to cycle^-1.
        for point in reversed(cycle[1:]):
            out.append(from_cycles(n, (cycle[0] + 1, point + 1)))
    assert product(out, n) == inverse(perm)
    return out


def symmetric_genus_zero_witness(profile: Profile) -> tuple[Perm, ...]:
    """Explicit primitive S_n Hurwitz tuple for any pole partition.

    Decompose sigma_infinity^-1 into transpositions.  If sigma_infinity has
    several orbits, insert identical crossing-transposition pairs; they do not
    change the product but connect the generated orbits.  Total RH index is
    exactly 2n-2, so the cover has genus zero.
    """
    n = sum(profile)
    cycles = []
    first = 1
    representatives = []
    for length in profile:
        cycle = tuple(range(first, first + length))
        if length > 1:
            cycles.append(cycle)
        representatives.append(first)
        first += length
    sigma = from_cycles(n, *cycles)
    finite = transpositions_for_cycle_inverse(sigma)
    for representative in representatives[1:]:
        crossing = from_cycles(n, (representatives[0], representative))
        finite.extend((crossing, crossing))
    witness = (sigma, *finite)
    assert product(witness, n) == identity(n)
    assert all(cycle_type(perm, reduced=True) == (2,) for perm in finite)
    # A transitive permutation group generated by transpositions is S_n.
    assert is_transitive(finite)
    assert hurwitz_genus(witness) == 0
    return witness


def orevkov_boundary_control() -> dict[str, object]:
    """Replay Orevkov's degree-9 boundary-component negative control.

    Orevkov 2001, Sec. 2.4, equations (11)--(13),(17), gives three branch
    partitions for L_tilde_1 -> L_1:
        (3,3,3), (4,4,1), (5,1,1,1,1).
    The displayed cycles below are a standard right-to-left ABC=1 tuple;
    reversed here because this engine uses left-to-right page products.
    """
    a = from_cycles(9, (1, 2, 3), (4, 5, 6), (7, 8, 9))
    b = from_cycles(9, (2, 5, 4, 3), (6, 7, 9, 8))
    c = from_cycles(9, (1, 4, 8, 6, 2))
    witness = (c, b, a)
    expected_types = ((5, 1, 1, 1, 1), (4, 4, 1), (3, 3, 3))
    assert tuple(cycle_type(perm) for perm in witness) == expected_types
    assert product(witness, 9) == identity(9)
    assert all(index(perm) % 2 == 0 for perm in witness)
    order = len(closure(witness))
    assert order == math.factorial(9) // 2
    assert is_transitive(witness)
    assert is_primitive(witness)
    assert hurwitz_genus(witness) == 0
    return {
        "cover": "Orevkov boundary component L_tilde_1 -> L_1 (not generic-fibre g-hat)",
        "degree": 9,
        "branch_profiles": expected_types,
        "product_one": True,
        "transitive": True,
        "primitive": True,
        "generated_group": "A(9)",
        "generated_order": order,
        "genus": 0,
        "why_forced": (
            "a degree-9 block system would have 3 blocks of size 3, impossible "
            "for the 5-cycle; Jordan then gives A9, and all cycles are even"
        ),
    }


def residue_a_s6_control() -> dict[str, object]:
    """Replay the full-S6 extremal residue-A g-hat witness.

    GROK-MONODROMY.md gives sigma_infinity=(3,3), a four-transposition core,
    and 19 identical connecting pairs, for the passport (2)^42.
    """
    sigma = from_cycles(6, (1, 2, 3), (4, 5, 6))
    finite = [
        from_cycles(6, (1, 3)),
        from_cycles(6, (1, 2)),
        from_cycles(6, (4, 6)),
        from_cycles(6, (4, 5)),
    ]
    connecting = from_cycles(6, (1, 4))
    finite.extend((connecting, connecting) * 19)
    witness = (sigma, *finite)
    assert len(finite) == 42
    assert product(witness, 6) == identity(6)
    order = len(closure(witness))
    assert order == math.factorial(6)
    assert hurwitz_genus(witness) == 18
    return {
        "cover": "residue-A generic-fibre g-hat, extremal passport (2)^42",
        "degree": 6,
        "infinity_profile": (3, 3),
        "finite_profiles": ((2, 1, 1, 1, 1),) * 42,
        "product_one": True,
        "generated_group": "S(6)",
        "generated_order": order,
        "genus": 18,
        "companion_sweep": "cases/grok_monodromy.py: all 169 passports pass",
    }


@dataclass(frozen=True)
class CensusRow:
    degree: int
    gap_id: str
    name: str
    order: int
    profile: Profile
    infinity_places: int
    branch_values_witness: int
    ramified_points_witness: int
    genus_witness: int
    cycle_types_witness: tuple[Profile, ...]


def run_census(*, full_checks: bool = False) -> tuple[list[CensusRow], dict[str, object]]:
    specs = primitive_group_specs()
    expected_counts = {6: 4, 7: 7, 8: 7, 9: 11}
    counts = {n: sum(spec.degree == n for spec in specs) for n in expected_counts}
    assert counts == expected_counts
    expected_raw_profiles = {
        6: ((6,), (5, 1), (4, 2), (3, 3)),
        7: ((7,), (3, 3, 1)),
        8: ((8,), (7, 1), (6, 2), (4, 4), (3, 3, 1, 1)),
        9: ((9,), (8, 1), (6, 3), (4, 4, 1), (3, 3, 3)),
    }
    expected_filtered_profiles = {
        6: ((5, 1), (3, 3)),
        7: ((3, 3, 1),),
        8: ((7, 1), (6, 2), (4, 4), (3, 3, 1, 1)),
        9: ((8, 1), (6, 3), (4, 4, 1), (3, 3, 3)),
    }
    assert {n: sheet_profiles(n, entry_filtered=False) for n in range(6, 10)} == expected_raw_profiles
    assert {n: sheet_profiles(n) for n in range(6, 10)} == expected_filtered_profiles

    rows: list[CensusRow] = []
    group_type_sets: dict[tuple[int, int], set[Profile]] = {}
    minimum_moved_points: dict[tuple[int, int], int] = {}
    checked_groups = 0
    for spec in specs:
        elements = closure(spec.generators)
        assert len(elements) == spec.expected_order, (spec, len(elements))
        assert is_transitive(spec.generators), spec
        assert is_primitive(spec.generators), spec
        checked_groups += 1
        by_type: dict[Profile, Perm] = {}
        # Sorting makes the representative selected for each cycle type, and
        # therefore the JSON witnesses, deterministic across hash seeds.
        for element in sorted(elements):
            by_type.setdefault(cycle_type(element), element)
        group_type_sets[(spec.degree, spec.gap_id)] = set(by_type)
        minimum_moved_points[(spec.degree, spec.gap_id)] = min(
            sum(cycle_type(element, reduced=True))
            for element in elements
            if element != identity(spec.degree)
        )
        for profile in sheet_profiles(spec.degree):
            sigma = by_type.get(profile)
            if sigma is None:
                continue
            witness = database_witness(spec, sigma)
            genus = hurwitz_genus(witness)
            assert genus >= 0, (spec, profile, genus)
            if full_checks:
                assert len(closure(witness)) == spec.expected_order
            rows.append(
                CensusRow(
                    degree=spec.degree,
                    gap_id=f"{spec.degree}P{spec.gap_id}",
                    name=spec.name,
                    order=spec.expected_order,
                    profile=profile,
                    infinity_places=len(profile),
                    branch_values_witness=len(witness),
                    ramified_points_witness=sum(ramified_points(x) for x in witness),
                    genus_witness=genus,
                    cycle_types_witness=tuple(cycle_type(x) for x in witness),
                )
            )

    # With finite inertia unrestricted, S_n admits every surviving infinity
    # profile.  These genus-zero tuples are uniform, explicit counterwitnesses
    # to a degree exclusion based only on the current filters.
    controls = {}
    for n in range(6, 10):
        for profile in sheet_profiles(n):
            witness = symmetric_genus_zero_witness(profile)
            controls[f"td={n} {profile}"] = {
                "degree": n,
                "infinity_profile": profile,
                "group": f"S({n})",
                "branch_values": len(witness),
                "ramified_points": sum(ramified_points(x) for x in witness),
                "genus": hurwitz_genus(witness),
                "cycle_types": [cycle_type(x) for x in witness],
            }

    raw_profile_groups = {
        n: {
            str(profile): [
                f"{n}P{spec.gap_id}"
                for spec in specs
                if spec.degree == n
                and profile in group_type_sets[(n, spec.gap_id)]
            ]
            for profile in sheet_profiles(n, entry_filtered=False)
        }
        for n in range(6, 10)
    }

    entry_profile_groups = {
        n: {
            str(profile): [
                f"{n}P{spec.gap_id}"
                for spec in specs
                if spec.degree == n
                and profile in group_type_sets[(n, spec.gap_id)]
            ]
            for profile in sheet_profiles(n)
        }
        for n in range(6, 10)
    }

    hits_by_group = {
        (spec.degree, spec.gap_id): sum(
            row.degree == spec.degree and row.gap_id == f"{spec.degree}P{spec.gap_id}" for row in rows
        )
        for spec in specs
    }
    raw_hits_by_group = {
        (spec.degree, spec.gap_id): len(
            set(sheet_profiles(spec.degree, entry_filtered=False))
            & group_type_sets[(spec.degree, spec.gap_id)]
        )
        for spec in specs
    }
    expected_minimum_moved = {
        6: (4, 4, 3, 2),
        7: (7, 6, 6, 6, 4, 3, 2),
        8: (7, 6, 4, 6, 6, 3, 2),
        9: (8, 6, 8, 8, 6, 6, 6, 7, 6, 3, 2),
    }
    assert {
        n: tuple(
            minimum_moved_points[(n, spec.gap_id)]
            for spec in specs
            if spec.degree == n
        )
        for n in range(6, 10)
    } == expected_minimum_moved
    assert sum(raw_hits_by_group.values()) == 80
    assert len(rows) == 63
    assert sum(value > 0 for value in raw_hits_by_group.values()) == 29
    assert sum(value > 0 for value in hits_by_group.values()) == 27
    assert len(controls) == 11
    for n in range(6, 10):
        symmetric_id = max(spec.gap_id for spec in specs if spec.degree == n)
        symmetric_types = group_type_sets[(n, symmetric_id)]
        assert set(sheet_profiles(n)) <= symmetric_types

    sheet_examples: dict[int, dict[str, object]] = {}
    for n in range(6, 10):
        profile_data: dict[str, object] = {}
        for profile, choices in sheet_profile_configurations(n).items():
            surviving = tuple(choice for choice in choices if configuration_survives_entry_filter(choice))
            example = surviving[0] if surviving else choices[0]
            profile_data[str(profile)] = {
                "raw_configurations": len(choices),
                "entry_surviving_configurations": len(surviving),
                "example": [asdict(row) for row in example],
            }
        sheet_examples[n] = profile_data

    metadata: dict[str, object] = {
        "engine": "pure Python stdlib; GAP executable absent",
        "primitive_group_source": PRIMGRP_SOURCE,
        "primitive_group_counts": counts,
        "groups_checked": checked_groups,
        "raw_group_profile_rows": sum(raw_hits_by_group.values()),
        "entry_filtered_group_profile_rows": len(rows),
        "raw_distinct_groups": sum(value > 0 for value in raw_hits_by_group.values()),
        "entry_filtered_distinct_groups": sum(value > 0 for value in hits_by_group.values()),
        "minimum_moved_points_by_group": {
            f"{n}P{gap_id}": value
            for (n, gap_id), value in minimum_moved_points.items()
        },
        "entry_filtered_profile_hits_by_group": {
            f"{n}P{gap_id}": value for (n, gap_id), value in hits_by_group.items()
        },
        "raw_profile_hits_by_group": {
            f"{n}P{gap_id}": value for (n, gap_id), value in raw_hits_by_group.items()
        },
        "raw_sheet_profiles": {n: sheet_profiles(n, entry_filtered=False) for n in range(6, 10)},
        "entry_filtered_sheet_profiles": {n: sheet_profiles(n) for n in range(6, 10)},
        "raw_profile_groups": raw_profile_groups,
        "entry_filtered_profile_groups": entry_profile_groups,
        "sheet_profile_derivations": sheet_examples,
        "symmetric_all_surviving_profile_controls": controls,
        "orevkov_boundary_control": orevkov_boundary_control(),
        "residue_a_s6_control": residue_a_s6_control(),
        "scope_warning": (
            "N, genus, and finite inertia are unspecified. Witness support is "
            "an upper bound, not a minimum or a justified sheet-frame cap. "
            "Profiles are generic-a infinity partitions from Props 5.4--5.6; "
            "the main census applies only the singleton b=1 entry kill and "
            "does not impose the optional H5a/N1 gcd filter."
        ),
    }
    return rows, metadata


def profile_text(profile: Profile) -> str:
    return "(" + ",".join(map(str, profile)) + ")"


def print_summary(rows: Sequence[CensusRow], metadata: dict[str, object], *, details: bool) -> None:
    print("primitive-monodromy td=6..9 census")
    print(f"engine: {metadata['engine']}")
    print(f"source: {metadata['primitive_group_source']}")
    print(f"primitive group counts: {metadata['primitive_group_counts']}")
    minimum_moved = metadata["minimum_moved_points_by_group"]
    assert isinstance(minimum_moved, dict)
    print(
        "minimum moved points: "
        + "; ".join(
            f"td={n} "
            + ",".join(
                str(minimum_moved[f"{n}P{gap_id}"])
                for gap_id in range(1, metadata["primitive_group_counts"][n] + 1)
            )
            for n in range(6, 10)
        )
    )
    print(
        "incidences: "
        f"raw={metadata['raw_group_profile_rows']} rows/"
        f"{metadata['raw_distinct_groups']} groups; "
        f"entry-filtered={metadata['entry_filtered_group_profile_rows']} rows/"
        f"{metadata['entry_filtered_distinct_groups']} groups"
    )
    print(f"scope: {metadata['scope_warning']}")
    print()
    for n in range(6, 10):
        profiles = sheet_profiles(n)
        raw = sheet_profiles(n, entry_filtered=False)
        dropped = tuple(profile for profile in raw if profile not in profiles)
        print(
            f"td={n}: raw generic infinity profiles="
            f"{','.join(profile_text(x) for x in raw)}; "
            f"entry-filtered={','.join(profile_text(x) for x in profiles)}"
        )
        if dropped:
            print(f"  singleton-b=1-only profiles removed: {','.join(profile_text(x) for x in dropped)}")
            raw_groups = metadata["raw_profile_groups"]
            assert isinstance(raw_groups, dict)
            degree_raw_groups = raw_groups[n]
            assert isinstance(degree_raw_groups, dict)
            for profile in dropped:
                labels = ", ".join(degree_raw_groups[str(profile)])
                print(f"    raw-only {profile_text(profile):11s} groups: {labels}")
        for profile in profiles:
            hits = [row for row in rows if row.degree == n and row.profile == profile]
            labels = ", ".join(f"{row.gap_id} {row.name}" for row in hits)
            print(f"  {profile_text(profile):11s} {len(hits):2d} groups: {labels}")
            if details:
                for row in hits:
                    print(
                        f"    {row.gap_id:4s} order={row.order:<6d} "
                        f"B<={row.branch_values_witness} P<={row.ramified_points_witness} "
                        f"g={row.genus_witness} types="
                        + " ".join(profile_text(x) for x in row.cycle_types_witness)
                    )
    print()
    print("surviving-profile envelope (explicit S(td) genus-zero tuples):")
    controls = metadata["symmetric_all_surviving_profile_controls"]
    assert isinstance(controls, dict)
    for key, value in controls.items():
        assert isinstance(value, dict)
        print(
            f"  {key:22s} {value['group']}, B={value['branch_values']}, "
            f"P={value['ramified_points']}, genus={value['genus']}"
        )
    orevkov = metadata["orevkov_boundary_control"]
    assert isinstance(orevkov, dict)
    print(
        "Orevkov (48,64) adjacent boundary control: "
        f"profiles={orevkov['branch_profiles']}, group={orevkov['generated_group']}, "
        f"order={orevkov['generated_order']}, genus={orevkov['genus']} (PASS)"
    )
    residue = metadata["residue_a_s6_control"]
    assert isinstance(residue, dict)
    print(
        "residue-A g-hat control: "
        f"profile={residue['infinity_profile']}, group={residue['generated_group']}, "
        f"genus={residue['genus']} (PASS; companion 169-passport sweep)"
    )
    print("verdict: no td in 6..9 is forbidden; S(td) survives every retained profile")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--details", action="store_true", help="print witness bounds and cycle types")
    parser.add_argument("--json", action="store_true", help="print the complete census as JSON")
    parser.add_argument("--check", action="store_true", help="re-close every Hurwitz witness group")
    args = parser.parse_args()
    rows, metadata = run_census(full_checks=args.check)
    if args.json:
        print(json.dumps({"metadata": metadata, "rows": [asdict(row) for row in rows]}, indent=2))
    else:
        print_summary(rows, metadata, details=args.details)
        print(f"checks: {len(rows)} admissible group/profile rows; PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
