#!/usr/bin/env python3
"""Dependency-free formal check of the 2x2 adjugate identities."""
from __future__ import annotations


class Poly:
    names = ("A", "B", "H", "X", "Y")

    def __init__(self, terms=None):
        self.terms = {m: c for m, c in (terms or {}).items() if c}

    @classmethod
    def var(cls, index):
        m = [0] * len(cls.names)
        m[index] = 1
        return cls({tuple(m): 1})

    def __add__(self, other):
        if not isinstance(other, Poly):
            other = Poly({(0,) * len(self.names): other})
        out = dict(self.terms)
        for m, c in other.terms.items():
            out[m] = out.get(m, 0) + c
            if not out[m]:
                del out[m]
        return Poly(out)

    def __neg__(self):
        return Poly({m: -c for m, c in self.terms.items()})

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        if not isinstance(other, Poly):
            other = Poly({(0,) * len(self.names): other})
        out = {}
        for m, c in self.terms.items():
            for n, d in other.terms.items():
                mn = tuple(x+y for x, y in zip(m, n))
                out[mn] = out.get(mn, 0) + c*d
        return Poly(out)

    def __eq__(self, other):
        if not isinstance(other, Poly):
            other = Poly({(0,) * len(self.names): other})
        return self.terms == other.terms


A, B, H, X, Y = (Poly.var(i) for i in range(5))
Delta = A*A + H*B
u = -A*X + B*Y
v = -H*X - A*Y

# These are exactly M^# M = Delta I, coefficient-free over Z and hence over
# every field after specialization.
assert -A*u - B*v == Delta*X
assert H*u - A*v == Delta*Y

print("PASS-FORMAL-ADJUGATE-IDENTITY")
print("Delta_nonzero: divide both adjugate numerators, then enforce deg X<=2, deg Y<=1")
print("Delta_zero_H_unit: Hu-Av=0 is necessary; Y=0, X=-H^-1*v is sufficient")
print("Delta_zero_H_zero: A^2=0 in k[z] gives A=0; require v=0 and u=B*Y with deg Y<=1")
