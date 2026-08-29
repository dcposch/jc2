#!/usr/bin/env python3
"""Exact sparse multivariate polynomials over Q.

Self-contained, stdlib only, no floats, no caps.  Used to verify the merge
T1 (Prop 8.1(iv)) reduction as a *symbolic identity in the unknown pattern
coefficients*, not by numeric sampling.

Variable 0 is always `eta`; the remaining variables are the symbolic
coefficients of the pattern polynomials.
"""
from fractions import Fraction as Fr


class Poly:
    """Sparse multivariate polynomial: dict {exponent tuple: Fraction}."""

    __slots__ = ("n", "d")

    def __init__(self, n, d=None):
        self.n = n
        self.d = {} if d is None else {k: v for k, v in d.items() if v != 0}

    @staticmethod
    def const(n, c):
        c = Fr(c)
        return Poly(n, {} if c == 0 else {(0,) * n: c})

    @staticmethod
    def var(n, i, power=1):
        e = [0] * n
        e[i] = power
        return Poly(n, {tuple(e): Fr(1)})

    def copy(self):
        return Poly(self.n, dict(self.d))

    def __add__(self, other):
        if not isinstance(other, Poly):
            other = Poly.const(self.n, other)
        out = dict(self.d)
        for k, v in other.d.items():
            nv = out.get(k, Fr(0)) + v
            if nv == 0:
                out.pop(k, None)
            else:
                out[k] = nv
        return Poly(self.n, out)

    def __neg__(self):
        return Poly(self.n, {k: -v for k, v in self.d.items()})

    def __sub__(self, other):
        if not isinstance(other, Poly):
            other = Poly.const(self.n, other)
        return self + (-other)

    def __mul__(self, other):
        if not isinstance(other, Poly):
            other = Poly.const(self.n, other)
        out = {}
        for k1, v1 in self.d.items():
            for k2, v2 in other.d.items():
                k = tuple(a + b for a, b in zip(k1, k2))
                nv = out.get(k, Fr(0)) + v1 * v2
                if nv == 0:
                    out.pop(k, None)
                else:
                    out[k] = nv
        return Poly(self.n, out)

    __radd__ = __add__
    __rmul__ = __mul__

    def __rsub__(self, other):
        return Poly.const(self.n, other) - self

    def __eq__(self, other):
        if not isinstance(other, Poly):
            other = Poly.const(self.n, other)
        return self.d == other.d

    def is_zero(self):
        return not self.d

    def pow(self, k):
        assert k >= 0
        r = Poly.const(self.n, 1)
        b = self
        while k:
            if k & 1:
                r = r * b
            b = b * b
            k >>= 1
        return r

    def diff(self, i):
        out = {}
        for k, v in self.d.items():
            if k[i] == 0:
                continue
            e = list(k)
            c = v * e[i]
            e[i] -= 1
            kk = tuple(e)
            nv = out.get(kk, Fr(0)) + c
            if nv == 0:
                out.pop(kk, None)
            else:
                out[kk] = nv
        return Poly(self.n, out)

    def subst_var_power(self, i, other):
        """Substitute variable i by the polynomial `other` (used for t = eta^nu)."""
        out = Poly(self.n)
        for k, v in self.d.items():
            e = list(k)
            p = e[i]
            e[i] = 0
            term = Poly(self.n, {tuple(e): v})
            out = out + term * other.pow(p)
        return out

    def degree_in(self, i):
        return max((k[i] for k in self.d), default=-1)

    def coeff_in(self, i, power):
        """Coefficient of var_i^power, as a Poly in the remaining variables."""
        out = {}
        for k, v in self.d.items():
            if k[i] == power:
                e = list(k)
                e[i] = 0
                out[tuple(e)] = v
        return Poly(self.n, out)

    def __repr__(self):
        if not self.d:
            return "0"
        return "Poly(%d terms, n=%d)" % (len(self.d), self.n)
