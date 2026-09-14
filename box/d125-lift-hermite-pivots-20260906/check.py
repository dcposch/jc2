#!/usr/bin/env python3
"""Tiny exact DESK controls only; no full source/Jacobian construction or CAS.
Run under timeout30, CPU25s, AS512MiB. Deterministic standard library.
"""
from fractions import Fraction as Q
from math import comb
import sys


def require(value, name):
    if not value:
        raise RuntimeError('FAIL ' + name)
    print('PASS ' + name)


def determinant(matrix):
    a = [[Q(x) for x in row] for row in matrix]
    out = Q(1)
    for col in range(len(a)):
        pivot = next((r for r in range(col, len(a)) if a[r][col]), None)
        if pivot is None:
            return Q(0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            out = -out
        v = a[col][col]
        out *= v
        for r in range(col + 1, len(a)):
            factor = a[r][col] / v
            for k in range(col, len(a)):
                a[r][k] -= factor*a[col][k]
    return out


POLYGONS = {
    'unequal': ([(0, 0), (0, 15), (9, 6), (2, 1)],
                [(0, 0), (0, 25), (15, 10), (1, 0)]),
    'common3': ([(0, 0), (0, 15), (9, 6), (3, 0)],
                [(0, 0), (0, 25), (15, 10), (5, 0)]),
    'common4': ([(0, 0), (0, 15), (9, 6), (9, 0)],
                [(0, 0), (0, 25), (15, 10), (15, 0)])}
INNER = {'unequal': (5, -7), 'common3': (1, -1), 'common4': (1, 0)}


def inside(vertices, point):
    signs = []
    x, y = point
    for (a, b), (c, d) in zip(vertices, vertices[1:] + vertices[:1]):
        signs.append((c-a)*(y-b) - (d-b)*(x-a))
    return all(v >= 0 for v in signs) or all(v <= 0 for v in signs)


for name, polygons in POLYGONS.items():
    counts = []
    for degree, vertices in zip((15, 25), polygons):
        nx, ny = INNER[name]
        boundary = max(nx*i + ny*j for i, j in vertices)
        count = 0
        for s in range(1, degree):
            r = (s+4)//5
            points = [(i, s-i) for i in range(r)]
            free = all(inside(vertices, p) and sum(p) < degree
                       and nx*p[0]+ny*p[1] != boundary and p != (0, 0)
                       for p in points)
            require(free, f'{name} D{degree} s{s}: all {r} pivots are free slots')
            matrix = [[(-1)**(s-i-t)*comb(s-i, t) for i in range(r)]
                      for t in range(r)]
            if '--mutate-matrix' in sys.argv and r == 2:
                matrix[0] = list(matrix[1])
            require(determinant(matrix) == (-1)**(r*s+r*(r-1)//2),
                    f'{name} D{degree} s{s}: determinant is signed unit')
            count += r
        counts.append(count)
    require(counts == [27, 70], f'{name}: exactly 97 pivots')
require([269-97, 295-97, 371-97] == [172, 198, 274], 'remaining variable counts')


def multiply(a, b):
    out = {}
    for (i, j), c in a.items():
        for (k, l), d in b.items():
            e = (i+k, j+l)
            out[e] = out.get(e, Q(0)) + c*d
    return {e: c for e, c in out.items() if c}


def lift(a, l2, l3):
    """Independent repeated multiplication, numeric lambdas, toy D6 only."""
    image = {(1, 4): Q(1), (0, 2): -Q(l2), (0, 1): -Q(l3), (0, -1): Q(-1)}
    powers = [{(0, 0): Q(1)}]
    for _ in range(6):
        powers.append(multiply(powers[-1], image))
    out = {}
    for (i, j), c in a.items():
        if i+j > 6:
            raise ValueError('toy degree cap')
        for (t, e), v in powers[j].items():
            key = (t, e-i)
            out[key] = out.get(key, Q(0)) + c*v
    return {e: c for e, c in out.items() if c}


for l2, l3 in ((0, 0), (2, -3)):
    # degree-six fixed top z^3*(z+1)^3 has a triple root at -1;
    # all other nonselected coefficients are arbitrary small integers.
    a = {(6-j, j): Q(comb(3, j-3)) for j in range(3, 7)}
    for s in range(1, 6):
        for i in range(1, s+1):
            a[(i, s-i)] = Q((i+2*s) % 7-3)
    for s in range(5, 0, -1):
        residual = lift(a, l2, l3).get((0, -s), Q(0))
        a[(0, s)] = -residual / ((-1)**s)
    negative = {e: c for e, c in lift(a, l2, l3).items() if e[1] < 0}
    require(not negative, f'toy6 lambda{l2,l3}: all negative rows vanish after descending pivots')
    changed = dict(a)
    changed[(0, 1)] += 1
    bad = {e: c for e, c in lift(changed, l2, l3).items() if e[1] < 0}
    require(bad == {(0, -1): Q(-1)}, 'changed actual coefficient fails exactly one negative row')
    if '--mutate-drop-row' in sys.argv:
        bad.pop((0, -1))
    require(bool(bad), 'complete checker rejects changed coefficient; dropping actual row is unsound')
print('ALL PASS: DESK pivots and toy6 only; no production input or nonemptiness')
