#!/usr/bin/env python3
"""Exact desk-scale checks for the R7 characteristic/de Rham transform."""

from fractions import Fraction


NAMES = (
    "P", "Px", "Pt", "t", "W", "Wx", "Wt", "s", "Ps",
    "F1", "F2", "B", "Bx", "V", "Vx", "w",
)
NV = len(NAMES)


class LP:
    """Sparse Laurent polynomial over Q in the variables above."""

    def __init__(self, terms=None):
        self.terms = {
            tuple(m): Fraction(c)
            for m, c in (terms or {}).items()
            if c
        }

    @staticmethod
    def const(c):
        return LP({(0,) * NV: Fraction(c)})

    @staticmethod
    def var(i):
        m = [0] * NV
        m[i] = 1
        return LP({tuple(m): Fraction(1)})

    def __add__(self, other):
        other = as_lp(other)
        out = dict(self.terms)
        for m, c in other.terms.items():
            out[m] = out.get(m, Fraction(0)) + c
            if not out[m]:
                del out[m]
        return LP(out)

    __radd__ = __add__

    def __neg__(self):
        return LP({m: -c for m, c in self.terms.items()})

    def __sub__(self, other):
        return self + (-as_lp(other))

    def __rsub__(self, other):
        return as_lp(other) - self

    def __mul__(self, other):
        other = as_lp(other)
        out = {}
        for a, ca in self.terms.items():
            for b, cb in other.terms.items():
                m = tuple(x + y for x, y in zip(a, b))
                out[m] = out.get(m, Fraction(0)) + ca * cb
        return LP(out)

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        scalar = Fraction(scalar)
        return LP({m: c / scalar for m, c in self.terms.items()})

    def __pow__(self, n):
        if n < 0:
            if len(self.terms) != 1:
                raise ValueError("negative powers require a monomial")
            (m, c), = self.terms.items()
            return LP({tuple(n * e for e in m): c ** n})
        out = LP.const(1)
        base = self
        while n:
            if n & 1:
                out = out * base
            base = base * base
            n >>= 1
        return out

    def __eq__(self, other):
        return self.terms == as_lp(other).terms


def as_lp(x):
    return x if isinstance(x, LP) else LP.const(x)


def series_mul(a, b, order):
    out = [LP.const(0) for _ in range(order + 1)]
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            if i + j <= order:
                out[i + j] = out[i + j] + ai * bj
    return out


def series_pow(a, n, order):
    out = [LP.const(1)] + [LP.const(0) for _ in range(order)]
    for _ in range(n):
        out = series_mul(out, a, order)
    return out


P, Px, Pt, t, W, Wx, Wt, s, Ps, F1, F2, B, Bx, V, Vx, w = [
    LP.var(i) for i in range(NV)
]

# Direct differential-polynomial identity with F=P^8 and G=P^12 W.
F = P ** 8
Fx = 8 * (P ** 7) * Px
Ft = 8 * (P ** 7) * Pt
G = (P ** 12) * W
Gx = 12 * (P ** 11) * Px * W + (P ** 12) * Wx
Gt = 12 * (P ** 11) * Pt * W + (P ** 12) * Wt
E = 12 * Fx * G - 8 * F * Gx - t * (Fx * Gt - Ft * Gx)
L = (t * Pt - P) * Wx - t * Px * Wt
assert E == 8 * (P ** 19) * L

# For s=t/P, J(s,W)=L/P^2 and hence E=8P^21 J(s,W).
sx = -t * Px * (P ** -2)
st = P ** -1 - t * Pt * (P ** -2)
J = sx * Wt - st * Wx
assert J == (P ** -2) * L
assert E == 8 * (P ** 21) * J

# In (X,s)-coordinates, t=sP and Q=P^2 give P*t_s=Q+(s/2)Q_s.
Q = P ** 2
Qs = 2 * P * Ps
assert P * (P + s * Ps) == Q + s * Qs / 2

# Exact implicit expansion P(s)^8=F(X,sP(s)) through s^2.
p1 = F1 * (P ** -6) / 8
p2 = F2 * (P ** -5) / 8 - 5 * (F1 ** 2) * (P ** -13) / 128
Pser = [P, p1, p2]
lhs = series_pow(Pser, 8, 2)
Pser2 = series_pow(Pser, 2, 2)
rhs = [P ** 8, F1 * P, F1 * p1 + F2 * Pser2[0]]
assert lhs == rhs

Qser = series_pow(Pser, 2, 2)
q_expected = [
    P ** 2,
    F1 * (P ** -5) / 4,
    F2 * (P ** -4) / 4 - (F1 ** 2) * (P ** -12) / 16,
]
assert Qser == q_expected
q2_mutated = F2 * (P ** -4) / 4 - (F1 ** 2) * (P ** -12) / 15
assert Qser[2] != q2_mutated

# d(V*B*w)=(B*Vx+(3/2)Bx*V)w after using w^2=B.
primitive_derivative_reduced = Vx * B * w + V * Bx * w + V * Bx * w / 2
endpoint_integrand = (B * Vx + 3 * Bx * V / 2) * w
assert primitive_derivative_reduced == endpoint_integrand

for n in range(64):
    assert Fraction(n + 2, 16) != 0

print("PASS R7 exact characteristic identities, q0/q1/q2 expansion, mutation, and endpoint primitive")
