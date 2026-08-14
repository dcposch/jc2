#!/usr/bin/env python3
"""Exact W_2/Bockstein engine for characteristic-two plane Keller maps.

The basic input is a pair P,Q in F_2[x,y], represented by its support.  The
canonical 0/1 lifts satisfy

    [P~,Q~] = 1 + 2 E  (mod 4).

The unrestricted correction equation is

    E + [A,Q] + [P,B] = 0  in F_2[x,y].

Because [P,Q]=1, (A,B) -> A dQ - B dP identifies the image of the
linearized bracket with exact two-forms.  Thus the obstruction is exactly
the class of E dx^dy in H^2_dR(F_2[x,y]); it vanishes iff E has no monomial
x^i y^j with i,j odd.  When it vanishes, this file constructs A,B and lifts
marked collision points as an exact witness.

The finite search is the registered "Mondello hull plus one shell" stratum
described in xmodel/sol-witt.md.  All arithmetic in the census is exact
bit arithmetic.  Optional generic degrees are exact Groebner-basis vector
space dimensions over F_2(U,V), computed by Singular (no sampling).

Examples:
    python3 cases/witt_check.py self-test
    python3 cases/witt_check.py search --degrees
    python3 cases/witt_check.py relaxed --degrees
    python3 cases/witt_check.py relaxed --json-vanishing
    python3 cases/witt_check.py check \
        --p '1,0;2,1;4,0;6,2' \
        --q '0,1;5,0;6,1;7,2;8,3'
    python3 cases/witt_check.py audit-3d
"""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import re
import shutil
import subprocess
from collections import Counter
from itertools import permutations
from typing import Dict, FrozenSet, Iterable, List, Optional, Sequence, Set, Tuple


Mon2 = Tuple[int, int]
Poly2 = FrozenSet[Mon2]
IntPoly = Dict[Tuple[int, ...], int]

POINTS: Tuple[Mon2, ...] = ((0, 1), (1, 0), (1, 1))
MONDELLO_P: Poly2 = frozenset(((1, 0), (2, 1), (4, 0), (6, 2)))
MONDELLO_Q: Poly2 = frozenset(((0, 1), (5, 0), (6, 1), (7, 2), (8, 3)))


# ---------------------------------------------------------------------------
# Sparse F_2 and integer polynomial arithmetic

def pxor(*polys: Iterable[Mon2]) -> Poly2:
    out: Set[Mon2] = set()
    for poly in polys:
        out.symmetric_difference_update(poly)
    return frozenset(out)


def pmul(a: Poly2, b: Poly2) -> Poly2:
    parity: Dict[Mon2, int] = {}
    for i, j in a:
        for u, v in b:
            mon = (i + u, j + v)
            parity[mon] = parity.get(mon, 0) ^ 1
    return frozenset(mon for mon, bit in parity.items() if bit)


def pder(poly: Poly2, variable: int) -> Poly2:
    out = set()
    for i, j in poly:
        exponent = (i, j)[variable]
        if exponent & 1:
            out.add((i - 1, j) if variable == 0 else (i, j - 1))
    return frozenset(out)


def bracket2(p: Poly2, q: Poly2) -> Poly2:
    return pxor(pmul(pder(p, 0), pder(q, 1)),
                pmul(pder(p, 1), pder(q, 0)))


def bracket_column(p: Poly2, mon: Mon2) -> Poly2:
    """Return [p, x^mon] over F_2."""
    u, v = mon
    out: Set[Mon2] = set()
    for i, j in p:
        if (i * v - j * u) & 1:
            term = (i + u - 1, j + v - 1)
            if term in out:
                out.remove(term)
            else:
                out.add(term)
    return frozenset(out)


def bracket_z_binary(p: Poly2, q: Poly2) -> Dict[Mon2, int]:
    out: Dict[Mon2, int] = {}
    for i, j in p:
        for u, v in q:
            coefficient = i * v - j * u
            if coefficient:
                mon = (i + u - 1, j + v - 1)
                out[mon] = out.get(mon, 0) + coefficient
    return {mon: coefficient for mon, coefficient in out.items() if coefficient}


def eval2(poly: Poly2, point: Mon2) -> int:
    x, y = point
    return sum((x ** i) * (y ** j) for i, j in poly) & 1


def eval_z_binary(poly: Poly2, point: Mon2) -> int:
    x, y = point
    return sum((x ** i) * (y ** j) for i, j in poly)


def poly_string(poly: Poly2) -> str:
    def term(mon: Mon2) -> str:
        i, j = mon
        factors = []
        if i:
            factors.append("x" if i == 1 else f"x^{i}")
        if j:
            factors.append("y" if j == 1 else f"y^{j}")
        return "*".join(factors) or "1"
    return " + ".join(term(mon) for mon in sorted(poly)) or "0"


def singular_string(poly: Poly2) -> str:
    def term(mon: Mon2) -> str:
        i, j = mon
        factors = []
        if i:
            factors.append("x" if i == 1 else f"x{i}")
        if j:
            factors.append("y" if j == 1 else f"y{j}")
        return "*".join(factors) or "1"
    return "+".join(term(mon) for mon in sorted(poly)) or "0"


def support_json(poly: Poly2) -> List[List[int]]:
    return [list(mon) for mon in sorted(poly)]


def bank_digest(data: Sequence[Tuple[Poly2, Poly2]]) -> Tuple[int, str]:
    """Canonical byte length/SHA-256 for a finite support-pair bank."""
    def line(pair: Tuple[Poly2, Poly2]) -> str:
        p, q = pair
        encode = lambda poly: ",".join(f"{i}.{j}" for i, j in sorted(poly))
        return f"P:{encode(p)}|Q:{encode(q)}\n"
    payload = "".join(sorted(line(pair) for pair in data)).encode("ascii")
    return len(payload), hashlib.sha256(payload).hexdigest()


# ---------------------------------------------------------------------------
# The complete unrestricted W_2 obstruction in dimension two

def w2_error(p: Poly2, q: Poly2) -> Poly2:
    """Return E=([P~,Q~]-1)/2 mod 2 for canonical binary lifts."""
    if bracket2(p, q) != frozenset(((0, 0),)):
        raise ValueError("input is not a characteristic-two Keller pair")
    bracket = bracket_z_binary(p, q)
    bracket[(0, 0)] = bracket.get((0, 0), 0) - 1
    if any(coefficient & 1 for coefficient in bracket.values()):
        raise AssertionError("half-Jacobian error is not integral")
    return frozenset(mon for mon, coefficient in bracket.items()
                     if (coefficient // 2) & 1)


def cartier_support(error: Poly2) -> Poly2:
    """Cartier image, with x^(2a+1)y^(2b+1) mapped to x^a y^b."""
    return frozenset(((i - 1) // 2, (j - 1) // 2)
                     for i, j in error if (i & 1) and (j & 1))


def odd_odd_support(error: Poly2) -> Poly2:
    return frozenset((i, j) for i, j in error if (i & 1) and (j & 1))


def exact_primitive(error: Poly2) -> Tuple[Poly2, Poly2]:
    """Find U,V with d(U dx+V dy)=error*dx^dy, if the class vanishes."""
    if cartier_support(error):
        raise ValueError("nonzero Cartier class has no polynomial primitive")
    u: Set[Mon2] = set()
    v: Set[Mon2] = set()
    for i, j in error:
        if not (i & 1):
            v.add((i + 1, j))       # d_x(x^(i+1)y^j)=x^i y^j
        else:
            if j & 1:
                raise AssertionError("Cartier monomial escaped the guard")
            u.add((i, j + 1))       # -d_y is the same sign in F_2
    uu, vv = frozenset(u), frozenset(v)
    recovered = pxor(pder(vv, 0), pder(uu, 1))
    if recovered != error:
        raise AssertionError("primitive construction failed")
    return uu, vv


def correction_witness(p: Poly2, q: Poly2, error: Poly2) -> Tuple[Poly2, Poly2]:
    """Construct A,B with [A,Q]+[P,B]=error when Cartier(error)=0."""
    u, v = exact_primitive(error)
    # U dx+V dy = A dQ-B dP; det J(P,Q)=1.  Minus equals plus in F_2.
    a = pxor(pmul(pder(p, 1), u), pmul(pder(p, 0), v))
    b = pxor(pmul(pder(q, 1), u), pmul(pder(q, 0), v))
    linearized = pxor(bracket2(a, q), bracket2(p, b))
    if linearized != error:
        raise AssertionError("linearized determinant witness failed")
    return a, b


def iadd(a: IntPoly, b: IntPoly) -> IntPoly:
    out = dict(a)
    for mon, coefficient in b.items():
        out[mon] = out.get(mon, 0) + coefficient
        if not out[mon]:
            del out[mon]
    return out


def iscale(a: IntPoly, scalar: int) -> IntPoly:
    return {mon: scalar * coefficient for mon, coefficient in a.items()
            if scalar * coefficient}


def imul(a: IntPoly, b: IntPoly) -> IntPoly:
    out: IntPoly = {}
    for mon, coefficient in a.items():
        for other, value in b.items():
            product = tuple(x + y for x, y in zip(mon, other))
            out[product] = out.get(product, 0) + coefficient * value
    return {mon: coefficient for mon, coefficient in out.items() if coefficient}


def ider(a: IntPoly, variable: int) -> IntPoly:
    out: IntPoly = {}
    for mon, coefficient in a.items():
        if mon[variable]:
            lowered = list(mon)
            lowered[variable] -= 1
            key = tuple(lowered)
            out[key] = out.get(key, 0) + coefficient * mon[variable]
    return {mon: coefficient for mon, coefficient in out.items() if coefficient}


def binary_int(poly: Poly2, correction: Optional[Poly2] = None) -> IntPoly:
    out: IntPoly = {mon: 1 for mon in poly}
    for mon in correction or frozenset():
        out[mon] = out.get(mon, 0) + 2
    return out


def bracket_int(p: IntPoly, q: IntPoly) -> IntPoly:
    return iadd(imul(ider(p, 0), ider(q, 1)),
                iscale(imul(ider(p, 1), ider(q, 0)), -1))


def eval_int(poly: IntPoly, point: Sequence[int], modulus: Optional[int] = None) -> int:
    value = 0
    for mon, coefficient in poly.items():
        product = coefficient
        for coordinate, exponent in zip(point, mon):
            product *= coordinate ** exponent
        value += product
    return value if modulus is None else value % modulus


def verify_mod4_keller(p: Poly2, q: Poly2, a: Poly2, b: Poly2) -> bool:
    bracket = bracket_int(binary_int(p, a), binary_int(q, b))
    keys = set(bracket) | {(0, 0)}
    return all((bracket.get(mon, 0) - (1 if mon == (0, 0) else 0)) % 4 == 0
               for mon in keys)


def collision_point_lifts(
    p: Poly2,
    q: Poly2,
    a: Poly2,
    b: Poly2,
    points: Sequence[Mon2],
) -> Tuple[Mon2, List[Mon2]]:
    """Lift marked points over the canonical lift of their common target."""
    if not points:
        return (0, 0), []
    images = [(eval2(p, point), eval2(q, point)) for point in points]
    if len(set(images)) != 1:
        raise ValueError("marked points are not a collision")
    target = images[0]
    px, py, qx, qy = pder(p, 0), pder(p, 1), pder(q, 0), pder(q, 1)
    lifts: List[Mon2] = []
    for point in points:
        carry_p = ((eval_z_binary(p, point) - target[0]) // 2) & 1
        carry_q = ((eval_z_binary(q, point) - target[1]) // 2) & 1
        rhs_p = carry_p ^ eval2(a, point)
        rhs_q = carry_q ^ eval2(b, point)
        # Inverse of [[P_x,P_y],[Q_x,Q_y]] in characteristic two.
        ux = (eval2(qy, point) * rhs_p) ^ (eval2(py, point) * rhs_q)
        uy = (eval2(qx, point) * rhs_p) ^ (eval2(px, point) * rhs_q)
        lifts.append((point[0] + 2 * ux, point[1] + 2 * uy))
    pp, qq = binary_int(p, a), binary_int(q, b)
    lifted_images = [(eval_int(pp, point, 4), eval_int(qq, point, 4))
                     for point in lifts]
    if len(set(lifted_images)) != 1 or lifted_images[0] != target:
        raise AssertionError("collision lift witness failed")
    return target, lifts


def analyze_datum(p: Poly2, q: Poly2,
                  points: Sequence[Mon2] = POINTS) -> Dict[str, object]:
    error = w2_error(p, q)
    odd = odd_odd_support(error)
    result: Dict[str, object] = {
        "P": support_json(p),
        "Q": support_json(q),
        "P_text": poly_string(p),
        "Q_text": poly_string(q),
        "error_support": support_json(error),
        "odd_odd_support": support_json(odd),
        "cartier_support": support_json(cartier_support(error)),
        "vanishes": not bool(odd),
    }
    if points:
        images = [(eval2(p, point), eval2(q, point)) for point in points]
        result["collision_points"] = [list(point) for point in points]
        result["collision_image"] = list(images[0]) if len(set(images)) == 1 else None
    if not odd:
        a, b = correction_witness(p, q, error)
        if not verify_mod4_keller(p, q, a, b):
            raise AssertionError("constructed correction does not verify modulo 4")
        result["A"] = support_json(a)
        result["B"] = support_json(b)
        if points and result.get("collision_image") is not None:
            target, lifts = collision_point_lifts(p, q, a, b, points)
            result["lifted_target_mod4"] = list(target)
            result["lifted_points_mod4"] = [list(point) for point in lifts]
    return result


# ---------------------------------------------------------------------------
# Finite-support augmented linear obstruction (a stricter diagnostic)

def affine_column_solve(columns: Sequence[int], rhs: int) -> Tuple[Optional[int], List[int], int]:
    """Solve xor(columns[j] for j in support)=rhs; return witness,kernel,rank."""
    basis: Dict[int, Tuple[int, int]] = {}
    kernel: List[int] = []
    for index, column in enumerate(columns):
        vector = column
        combination = 1 << index
        while vector:
            pivot = vector.bit_length() - 1
            if pivot not in basis:
                basis[pivot] = (vector, combination)
                break
            vector ^= basis[pivot][0]
            combination ^= basis[pivot][1]
        if not vector:
            kernel.append(combination)
    vector = rhs
    witness = 0
    while vector:
        pivot = vector.bit_length() - 1
        if pivot not in basis:
            return None, kernel, len(basis)
        vector ^= basis[pivot][0]
        witness ^= basis[pivot][1]
    return witness, kernel, len(basis)


def bounded_fixed_point_obstruction(
    p: Poly2,
    q: Poly2,
    support_p: Sequence[Mon2],
    support_q: Sequence[Mon2],
    points: Sequence[Mon2] = POINTS,
) -> Dict[str, object]:
    """Full finite-support cokernel with the displayed collision points frozen."""
    error = w2_error(p, q)
    collision_error: List[int] = []
    for point in points[1:]:
        collision_error.append(
            ((eval_z_binary(p, point) - eval_z_binary(p, points[0])) // 2) & 1)
        collision_error.append(
            ((eval_z_binary(q, point) - eval_z_binary(q, points[0])) // 2) & 1)
    raw: List[Tuple[Poly2, List[int]]] = []
    for mon in support_p:
        singleton = frozenset((mon,))
        raw.append((bracket2(singleton, q),
                    [eval2(singleton, point) ^ eval2(singleton, points[0])
                     for point in points[1:] for _ in (0,)]))
        # Interleave a zero Q row after each P collision row.
        raw[-1] = (raw[-1][0], [value for value in sum(([v, 0] for v in raw[-1][1]), [])])
    for mon in support_q:
        singleton = frozenset((mon,))
        values = [eval2(singleton, point) ^ eval2(singleton, points[0])
                  for point in points[1:]]
        raw.append((bracket2(p, singleton),
                    [value for value in sum(([0, v] for v in values), [])]))
    monomials = sorted(set(error).union(*(set(poly) for poly, _ in raw)))
    row = {mon: index for index, mon in enumerate(monomials)}
    offset = len(monomials)

    def encode(poly: Poly2, collision: Sequence[int]) -> int:
        vector = 0
        for mon in poly:
            vector ^= 1 << row[mon]
        for index, bit in enumerate(collision):
            if bit:
                vector ^= 1 << (offset + index)
        return vector

    columns = [encode(poly, collision) for poly, collision in raw]
    rhs = encode(error, collision_error)
    witness, kernel, rank = affine_column_solve(columns, rhs)
    return {
        "vanishes": witness is not None,
        "rank": rank,
        "rows": len(monomials) + len(collision_error),
        "variables": len(columns),
        "nullity": len(kernel),
    }


# ---------------------------------------------------------------------------
# Registered hull-plus-one-shell census

P_HULL_VERTICES: Tuple[Mon2, ...] = ((0, 0), (4, 0), (6, 2), (2, 1))
Q_HULL_VERTICES: Tuple[Mon2, ...] = ((0, 0), (5, 0), (8, 3), (0, 1))


def lattice_points(vertices: Sequence[Mon2]) -> Poly2:
    """Lattice points in/on a counterclockwise convex lattice polygon."""
    max_x = max(x for x, _ in vertices)
    max_y = max(y for _, y in vertices)
    out = set()
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            inside = True
            for (a, b), (c, d) in zip(vertices, vertices[1:] + vertices[:1]):
                if (c - a) * (y - b) - (d - b) * (x - a) < 0:
                    inside = False
                    break
            if inside:
                out.add((x, y))
    return frozenset(out)


def one_manhattan_shell(points: Poly2) -> Poly2:
    out = set(points)
    for i, j in points:
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if i + di >= 0 and j + dj >= 0:
                out.add((i + di, j + dj))
    return frozenset(out)


P_HULL = lattice_points(P_HULL_VERTICES)
Q_HULL = lattice_points(Q_HULL_VERTICES)
P_SHELL = one_manhattan_shell(P_HULL)
Q_SHELL = one_manhattan_shell(Q_HULL)

P_FIXED = {(0, 0): 0, (1, 0): 1, (0, 1): 0,
           (2, 1): 1, (4, 0): 1, (6, 2): 1}
Q_FIXED = {(0, 0): 0, (1, 0): 0, (0, 1): 1,
           (5, 0): 1, (8, 3): 1}


def support_from_mask(base: Poly2, free: Sequence[Mon2], mask: int) -> Poly2:
    return frozenset(set(base) | {mon for index, mon in enumerate(free)
                                  if (mask >> index) & 1})


def primary_search() -> Tuple[List[Tuple[Poly2, Poly2]], Dict[str, object]]:
    """Enumerate the exact normalized hull-plus-shell collision stratum."""
    p_free = sorted(set(P_SHELL) - set(P_FIXED))
    q_free = sorted(set(Q_SHELL) - set(Q_FIXED))
    p_base = frozenset(mon for mon, value in P_FIXED.items() if value)
    q_base = frozenset(mon for mon, value in Q_FIXED.items() if value)

    p_candidates = []
    for mask in range(1 << len(p_free)):
        p = support_from_mask(p_base, p_free, mask)
        if [eval2(p, point) for point in POINTS] == [0, 0, 0]:
            p_candidates.append(p)

    data: List[Tuple[Poly2, Poly2]] = []
    affine_dimensions: List[int] = []
    surviving_p: List[Poly2] = []
    for p in p_candidates:
        raw = [(bracket_column(p, mon), [eval2(frozenset((mon,)), point)
                                         for point in POINTS])
               for mon in q_free]
        monomials = sorted(set(bracket2(p, q_base)) | {(0, 0)} |
                           set().union(*(set(poly) for poly, _ in raw)))
        row = {mon: index for index, mon in enumerate(monomials)}
        offset = len(monomials)

        def encode(poly: Poly2, evaluations: Sequence[int]) -> int:
            vector = 0
            for mon in poly:
                vector ^= 1 << row[mon]
            for index, bit in enumerate(evaluations):
                if bit:
                    vector ^= 1 << (offset + index)
            return vector

        columns = [encode(poly, evaluations) for poly, evaluations in raw]
        rhs = encode(pxor(bracket2(p, q_base), ((0, 0),)),
                     [eval2(q_base, point) ^ 1 for point in POINTS])
        witness, kernel, _ = affine_column_solve(columns, rhs)
        if witness is None:
            continue
        surviving_p.append(p)
        affine_dimensions.append(len(kernel))
        for parameter_mask in range(1 << len(kernel)):
            solution = witness
            for index, relation in enumerate(kernel):
                if (parameter_mask >> index) & 1:
                    solution ^= relation
            q = support_from_mask(q_base, q_free, solution)
            if bracket2(p, q) != frozenset(((0, 0),)):
                raise AssertionError("affine Keller solve emitted a false solution")
            if [eval2(q, point) for point in POINTS] != [1, 1, 1]:
                raise AssertionError("affine solve emitted a false collision")
            data.append((p, q))

    expected_p = {
        MONDELLO_P,
        pxor(MONDELLO_P, ((2, 2), (4, 2))),
        pxor(MONDELLO_P, ((2, 0), (4, 1), (5, 0), (6, 1))),
        pxor(MONDELLO_P, ((2, 2), (4, 2), (2, 0), (4, 1), (5, 0), (6, 1))),
    }
    if set(surviving_p) != expected_p:
        raise AssertionError("registered P classification changed")
    if sorted(affine_dimensions) != [6, 6, 9, 9]:
        raise AssertionError("registered Q affine dimensions changed")

    patterns = Counter(tuple(sorted(odd_odd_support(w2_error(p, q)))) for p, q in data)
    vanishing = [(p, q) for p, q in data if not cartier_support(w2_error(p, q))]
    if len(P_HULL) != 10 or len(Q_HULL) != 18:
        raise AssertionError("base hull lattice count changed")
    if len(P_SHELL) != 20 or len(Q_SHELL) != 31:
        raise AssertionError("one-shell lattice count changed")
    if len(p_candidates) != 4096 or len(data) != 1152 or vanishing:
        raise AssertionError("registered census changed")
    if any((1, 2) in q for _, q in data):
        raise AssertionError("q_12 rigidity row changed")

    bank_bytes, bank_sha256 = bank_digest(data)
    meta: Dict[str, object] = {
        "P_hull_points": len(P_HULL),
        "Q_hull_points": len(Q_HULL),
        "P_shell_points": len(P_SHELL),
        "Q_shell_points": len(Q_SHELL),
        "P_free_bits": len(p_free),
        "Q_free_bits": len(q_free),
        "P_masks": 1 << len(p_free),
        "P_collision_masks": len(p_candidates),
        "surviving_P": len(surviving_p),
        "Q_affine_dimensions": sorted(affine_dimensions),
        "data": len(data),
        "bank_bytes": bank_bytes,
        "bank_sha256": bank_sha256,
        "cartier_zero": len(vanishing),
        "cartier_nonzero": len(data) - len(vanishing),
        "odd_odd_patterns": {str(list(pattern)): count
                             for pattern, count in sorted(patterns.items())},
    }
    return data, meta


def collision_candidates(support: Poly2, fixed: Dict[Mon2, int],
                         target: Optional[int] = None) -> List[Poly2]:
    free = sorted(set(support) - set(fixed))
    base = frozenset(mon for mon, value in fixed.items() if value)
    out = []
    for mask in range(1 << len(free)):
        poly = support_from_mask(base, free, mask)
        values = [eval2(poly, point) for point in POINTS]
        if values == [target] * len(POINTS) if target is not None else len(set(values)) == 1:
            out.append(poly)
    return out


def relaxed_hull_search() -> Tuple[List[Tuple[Poly2, Poly2]], Dict[str, object]]:
    """Audit all normalized masks inside the hulls, without core-vertex guards."""
    p_fixed = {(0, 0): 0, (1, 0): 1}
    q_fixed = {(0, 0): 0, (1, 0): 0, (0, 1): 1}
    ps = collision_candidates(P_HULL, p_fixed)
    qs = collision_candidates(Q_HULL, q_fixed)
    data = [(p, q) for p in ps for q in qs
            if bracket2(p, q) == frozenset(((0, 0),))]
    zero = [(p, q) for p, q in data if not cartier_support(w2_error(p, q))]
    bounded_zero = sum(
        bounded_fixed_point_obstruction(p, q,
                                        sorted(set(P_HULL) - set(p_fixed)),
                                        sorted(set(Q_HULL) - set(q_fixed)))["vanishes"]
        for p, q in zero
    )
    if (len(ps), len(qs), len(ps) * len(qs), len(data), len(zero), bounded_zero) != (
            64, 8192, 524288, 288, 48, 4):
        raise AssertionError("relaxed-hull audit changed")
    bank_bytes, bank_sha256 = bank_digest(data)
    zero_bytes, zero_sha256 = bank_digest(zero)
    meta: Dict[str, object] = {
        "P_collision_masks": len(ps),
        "Q_collision_masks": len(qs),
        "pairs_screened": len(ps) * len(qs),
        "keller_collisions": len(data),
        "bank_bytes": bank_bytes,
        "bank_sha256": bank_sha256,
        "cartier_zero": len(zero),
        "cartier_zero_bank_bytes": zero_bytes,
        "cartier_zero_bank_sha256": zero_sha256,
        "cartier_nonzero": len(data) - len(zero),
        "bounded_same_support_fixed_point_zero": bounded_zero,
    }
    return data, meta


def generic_degrees(data: Sequence[Tuple[Poly2, Poly2]]) -> List[int]:
    """Exact generic degrees over F_2(U,V), using Singular's std/vdim."""
    singular = shutil.which("Singular")
    if not singular:
        raise RuntimeError("Singular is required for --degrees")
    indexed = list(enumerate(data))
    worker_count = min(4, max(1, len(indexed)))
    chunks = [indexed[offset::worker_count] for offset in range(worker_count)]

    def run_chunk(chunk: Sequence[Tuple[int, Tuple[Poly2, Poly2]]]) -> Dict[int, int]:
        lines = [
            "ring r=(2,U,V),(x,y),dp;",
            "option(redSB);",
            "proc genericDegree(poly p, poly q)",
            "{",
            "  ideal fiber=p-U,q-V;",
            "  return(vdim(std(fiber)));",
            "}",
        ]
        for index, (p, q) in chunk:
            lines.append(
                f'print("D {index} "+string(genericDegree('
                f'{singular_string(p)},{singular_string(q)})));')
        lines.append("quit;")
        completed = subprocess.run(
            [singular, "-q"], input="\n".join(lines), text=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True,
        )
        if "error occurred" in completed.stdout.lower():
            raise RuntimeError("Singular reported an error:\n" + completed.stdout[:4000])
        return {int(index): int(degree)
                for index, degree in re.findall(r"^D\s+(\d+)\s+(\d+)\s*$",
                                                completed.stdout, re.MULTILINE)}

    parsed: Dict[int, int] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=worker_count) as executor:
        for result in executor.map(run_chunk, chunks):
            parsed.update(result)
    if len(parsed) != len(data):
        raise RuntimeError(f"parsed {len(parsed)} of {len(data)} Singular degrees")
    return [parsed[index] for index in range(len(data))]


# ---------------------------------------------------------------------------
# Literal three-dimensional premise audit

def determinant3(matrix: Sequence[Sequence[IntPoly]]) -> IntPoly:
    out: IntPoly = {}
    for permutation in permutations(range(3)):
        inversions = sum(permutation[i] > permutation[j]
                         for i in range(3) for j in range(i + 1, 3))
        term: IntPoly = {(0, 0, 0): -1 if inversions & 1 else 1}
        for row in range(3):
            term = imul(term, matrix[row][permutation[row]])
        out = iadd(out, term)
    return out


def audit_literal_3d() -> Dict[str, object]:
    """Verify that the Huq-Kuruvilla 3D datum actually lifts modulo 4."""
    g: List[IntPoly] = [
        {(1, 0, 0): 1, (2, 1, 0): 1},
        {(0, 1, 0): 1, (1, 0, 1): 1, (2, 1, 1): 1},
        {(0, 0, 1): 1, (2, 0, 2): 1},
    ]
    h: List[IntPoly] = [
        {(3, 0, 1): 1, (5, 0, 2): 1},
        {(3, 0, 2): 1, (5, 0, 3): 1, (2, 1, 1): 1,
         (3, 2, 1): 1, (6, 1, 3): 1, (7, 2, 3): 1},
        {(1, 1, 1): 1, (5, 1, 3): 1},
    ]
    det_g = determinant3([[ider(g[row], column) for column in range(3)]
                          for row in range(3)])
    error = dict(det_g)
    error[(0, 0, 0)] = error.get((0, 0, 0), 0) - 1
    error_mod2 = sorted(mon for mon, coefficient in error.items()
                        if (coefficient // 2) & 1)
    expected = [(1, 1, 0), (2, 0, 1), (4, 0, 2), (5, 1, 2)]
    if error_mod2 != expected:
        raise AssertionError("literal 3D error calculation changed")
    f = [iadd(g[index], iscale(h[index], 2)) for index in range(3)]
    det_f = determinant3([[ider(f[row], column) for column in range(3)]
                          for row in range(3)])
    keys = set(det_f) | {(0, 0, 0)}
    if any((det_f.get(mon, 0) - (1 if mon == (0, 0, 0) else 0)) % 4
           for mon in keys):
        raise AssertionError("literal 3D correction failed")
    points = [(0, 1, 0), (3, 1, 0), (3, 1, 3)]
    images = [tuple(eval_int(poly, point, 4) for poly in f) for point in points]
    if len(set(images)) != 1:
        raise AssertionError("literal 3D lifted collision failed")
    return {
        "error_support": [list(mon) for mon in error_mod2],
        "top_cartier_support": [],
        "correction_H": [[list(mon) for mon in sorted(poly)] for poly in h],
        "lifted_points_mod4": [list(point) for point in points],
        "common_image_mod4": list(images[0]),
        "determinant_mod4": 1,
    }


# ---------------------------------------------------------------------------
# CLI

def parse_support(text: str) -> Poly2:
    if not text.strip():
        return frozenset()
    out = set()
    for item in text.split(";"):
        pieces = item.strip().split(",")
        if len(pieces) != 2:
            raise argparse.ArgumentTypeError(f"bad monomial {item!r}")
        mon = (int(pieces[0]), int(pieces[1]))
        if min(mon) < 0:
            raise argparse.ArgumentTypeError("exponents must be nonnegative")
        out.add(mon)
    return frozenset(out)


def print_primary(degrees: bool, json_all: bool) -> None:
    data, meta = primary_search()
    degree_list: Optional[List[int]] = None
    if degrees:
        degree_list = generic_degrees(data)
        histogram = dict(sorted(Counter(degree_list).items()))
        odd_indices = [index for index, degree in enumerate(degree_list) if degree & 1]
        meta["generic_degree_histogram"] = histogram
        meta["odd_degree_data"] = len(odd_indices)
        odd_bytes, odd_sha256 = bank_digest([data[index] for index in odd_indices])
        meta["odd_bank_bytes"] = odd_bytes
        meta["odd_bank_sha256"] = odd_sha256
    print("REGISTERED HULL+ONE-SHELL SEARCH")
    print(json.dumps(meta, sort_keys=True, indent=2))
    print("surviving P supports:")
    for p in sorted({p for p, _ in data}, key=lambda poly: tuple(sorted(poly))):
        print("  ", poly_string(p))
    if degree_list is not None:
        print("odd-degree bank:")
        for (p, q), degree in zip(data, degree_list):
            if degree & 1:
                print(f"  degree={degree:2d} P={support_json(p)} Q={support_json(q)} "
                      f"odd-odd={support_json(odd_odd_support(w2_error(p, q)))}")
    print("VERDICT: NEVER-VANISHES-PROVED on the registered stratum")
    if json_all:
        payload = []
        for index, (p, q) in enumerate(data):
            item = analyze_datum(p, q)
            if degree_list is not None:
                item["generic_degree"] = degree_list[index]
            payload.append(item)
        print(json.dumps(payload, sort_keys=True))


def print_relaxed(degrees: bool, json_vanishing: bool) -> None:
    data, meta = relaxed_hull_search()
    degree_list: Optional[List[int]] = None
    if degrees:
        degree_list = generic_degrees(data)
        meta["generic_degree_histogram"] = dict(sorted(Counter(degree_list).items()))
        meta["odd_degree_data"] = sum(degree & 1 for degree in degree_list)
        zero_degrees = [degree for (p, q), degree in zip(data, degree_list)
                        if not cartier_support(w2_error(p, q))]
        meta["cartier_zero_degree_histogram"] = dict(sorted(Counter(zero_degrees).items()))
        if any(degree & 1 for degree in zero_degrees):
            raise AssertionError("an odd-degree relaxed vanishing datum appeared")
    print("RELAXED INSIDE-HULL AUDIT (core vertices not retained)")
    print(json.dumps(meta, sort_keys=True, indent=2))
    if degrees:
        print("SIDE FINDING: 48 unrestricted W2-vanishing data; all have even generic degree")
    else:
        print("SIDE FINDING: 48 unrestricted W2-vanishing data "
              "(use --degrees to recheck their exact degree parity)")
    if json_vanishing:
        payload = []
        for index, (p, q) in enumerate(data):
            if cartier_support(w2_error(p, q)):
                continue
            item = analyze_datum(p, q)
            if degree_list is not None:
                item["generic_degree"] = degree_list[index]
            payload.append(item)
        print(json.dumps(payload, sort_keys=True))


def run_self_test(with_degrees: bool = False) -> None:
    mondello = analyze_datum(MONDELLO_P, MONDELLO_Q)
    expected_odd = [[1, 1], [7, 1], [9, 3]]
    if mondello["odd_odd_support"] != expected_odd:
        raise AssertionError("Mondello pilot obstruction changed")
    data, meta = primary_search()
    if meta["data"] != 1152 or meta["cartier_zero"] != 0:
        raise AssertionError("primary self-test failed")
    _, relaxed = relaxed_hull_search()
    if relaxed["keller_collisions"] != 288 or relaxed["cartier_zero"] != 48:
        raise AssertionError("relaxed self-test failed")
    audit_literal_3d()
    if with_degrees:
        degrees = generic_degrees(data)
        expected_histogram = {
            3: 1, 6: 3, 7: 1, 8: 9, 10: 29, 11: 2, 12: 49,
            14: 84, 15: 4, 16: 70, 18: 171, 20: 126, 22: 271,
            24: 16, 26: 166, 28: 6, 30: 136, 32: 8,
        }
        if dict(sorted(Counter(degrees).items())) != expected_histogram:
            raise AssertionError("generic-degree histogram changed")
    print("SELF-TEST PASS")
    print("  Mondello odd-odd support:", mondello["odd_odd_support"])
    print("  registered stratum: 1152 nonzero / 0 vanishing")
    print("  relaxed hull: 240 nonzero / 48 vanishing")
    print("  literal 3D premise audit: mod-4 Keller+collision lift verified")
    if with_degrees:
        print("  exact registered generic-degree histogram verified; odd count=8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command")

    check = subparsers.add_parser("check", help="check one binary plane datum")
    check.add_argument("--p", required=True, type=parse_support,
                       help="semicolon-separated exponent pairs")
    check.add_argument("--q", required=True, type=parse_support,
                       help="semicolon-separated exponent pairs")
    check.add_argument("--no-collision", action="store_true")

    search = subparsers.add_parser("search", help="run registered shell census")
    search.add_argument("--degrees", action="store_true",
                        help="compute exact generic degrees with Singular")
    search.add_argument("--json-all", action="store_true")

    relaxed = subparsers.add_parser("relaxed", help="run unforced-core hull audit")
    relaxed.add_argument("--degrees", action="store_true",
                         help="compute exact generic degrees with Singular")
    relaxed.add_argument("--json-vanishing", action="store_true")

    audit = subparsers.add_parser("audit-3d", help="audit the literal 3D premise")
    audit.add_argument("--json", action="store_true")

    tests = subparsers.add_parser("self-test", help="run all exact internal controls")
    tests.add_argument("--degrees", action="store_true")

    args = parser.parse_args()
    if args.command is None:
        run_self_test(False)
    elif args.command == "check":
        points: Sequence[Mon2] = () if args.no_collision else POINTS
        print(json.dumps(analyze_datum(args.p, args.q, points), sort_keys=True, indent=2))
    elif args.command == "search":
        print_primary(args.degrees, args.json_all)
    elif args.command == "relaxed":
        print_relaxed(args.degrees, args.json_vanishing)
    elif args.command == "audit-3d":
        result = audit_literal_3d()
        print(json.dumps(result, sort_keys=True, indent=2))
        print("VERDICT: literal Huq-Kuruvilla 3D datum LIFTS modulo 4")
    elif args.command == "self-test":
        run_self_test(args.degrees)
    else:
        raise AssertionError(args.command)


if __name__ == "__main__":
    main()
