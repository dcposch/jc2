"""Property + regression tests for the core library and Generator A."""
import random
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from jc import (bracket, padd, pmul, pneg, lattice_points, SystemA)

def num():
    """random numeric BiPoly with constant coefficients"""
    r = {}
    for _ in range(random.randint(2, 6)):
        r[(random.randint(0, 4), random.randint(0, 4))] = {(): random.randint(-5, 5)}
    return {k: v for k, v in r.items() if v[()] != 0}

def test_lattice_counts():
    # hand-computed via Pick's theorem
    assert len(lattice_points([(0, 0), (1, 0), (0, 1)])) == 3
    assert len(lattice_points([(0, 0), (2, 0), (2, 2), (0, 2)])) == 9
    # Prop 4.2 subcase (3)  (solved case (66,99))
    assert len(lattice_points([(0, 0), (1, 1), (6, 16), (6, 18)])) == 19
    assert len(lattice_points([(0, 0), (1, 0), (9, 24), (9, 27)])) == 37
    # Prop 4.3 (open case) subcase (2)
    assert len(lattice_points([(0, 0), (1, 0), (8, 14), (8, 16)])) == 25
    assert len(lattice_points([(0, 0), (2, 1), (12, 21), (12, 24)])) == 47
    # Prop 4.3 subcase (1)
    assert len(lattice_points([(0, 0), (1, 0), (8, 14), (8, 16), (0, 8)])) == 61
    assert len(lattice_points([(0, 0), (2, 1), (12, 21), (12, 24), (0, 12)])) == 125
    print("lattice counts OK")

def test_bracket_props():
    x = {(1, 0): {(): 1}}
    y = {(0, 1): {(): 1}}
    assert bracket(x, y) == {(0, 0): {(): 1}}, "[x,y] must be 1"
    random.seed(7)
    for _ in range(50):
        P, Q, R = num(), num(), num()
        # antisymmetry
        assert bracket(P, Q) == pneg(bracket(Q, P))
        # Leibniz: [PQ, R] = P[Q,R] + [P,R]Q
        lhs = bracket(pmul(P, Q), R)
        rhs = padd(pmul(P, bracket(Q, R)), pmul(bracket(P, R), Q))
        assert lhs == rhs
    print("bracket properties OK")

def test_generator_substitution():
    # Known solution of [P,Q] = x with these polygons:
    #   P = 2x + 3,  Q = (1/2)... use integer-friendly: P = x + 1, Q = x*y  gives
    #   [P,Q] = 1*(x) - 0 = x. Polygons: P in hull{(0,0),(1,0)}, Q in hull{(0,0),(1,1)}.
    S = SystemA("toy", [(0, 0), (1, 0)], [(0, 0), (1, 1)], (1, 0), nonvanish="nonorigin")
    vals = {}
    for name, key in [(S.varnames[i], k) for k, i in S.varof.items()]:
        pass
    # assign: P coeffs: (0,0)->1, (1,0)->1 ; Q coeffs: (0,0)->0, (1,0)->0? (1,1)->1, (0,1)->0
    for k, idx in S.varof.items():
        kind, pt = k
        if kind == "P":
            vals[S.varnames[idx]] = 1 if pt in [(0, 0), (1, 0)] else 0
        elif kind == "Q":
            vals[S.varnames[idx]] = 1 if pt == (1, 1) else 0
    vals["t"] = 1  # t * a_(1,0) * b_(1,1) = 1*1*1 = 1
    res = S.substitute(vals)
    assert all(v == 0 for v in res), f"toy solution fails: {res}"
    print("generator substitution OK")

if __name__ == "__main__":
    test_lattice_counts()
    test_bracket_props()
    test_generator_substitution()
    print("ALL TESTS PASS")
