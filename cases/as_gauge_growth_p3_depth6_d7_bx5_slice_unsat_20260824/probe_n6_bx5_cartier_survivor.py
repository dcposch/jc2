#!/usr/bin/env python3
"""Probe the full depth-six support conditions for the fixed b=x^5 slice.

The candidate is the exact SAT output of solve_d7_bx5_n6necessary_bv.py.
All polynomial operations reduce coefficientwise modulo 3^6=729 after every
addition/multiplication, so the calculation remains sparse and deterministic.
"""
from __future__ import annotations

Monomial = tuple[int, int]
Poly = dict[Monomial, int]
MOD = 3**6
CAP = 7
X: Poly = {(1, 0): 1}
Y: Poly = {(0, 1): 1}
ONE: Poly = {(0, 0): 1}


def norm(p: Poly, modulus: int = MOD) -> Poly:
    return {m: c % modulus for m, c in p.items() if c % modulus}


def add(*ps: Poly) -> Poly:
    out: Poly = {}
    for p in ps:
        for m, c in p.items():
            out[m] = (out.get(m, 0) + c) % MOD
    return norm(out)


def scale(k: int, p: Poly) -> Poly:
    return norm({m: (k * c) % MOD for m, c in p.items()})


def mul(p: Poly, q: Poly) -> Poly:
    out: Poly = {}
    for (i, j), c in p.items():
        for (k, ell), d in q.items():
            m = (i + k, j + ell)
            out[m] = (out.get(m, 0) + c * d) % MOD
    return norm(out)


def power(p: Poly, exponent: int) -> Poly:
    out = ONE
    base = norm(p)
    while exponent:
        if exponent & 1:
            out = mul(out, base)
        exponent //= 2
        if exponent:
            base = mul(base, base)
    return out


def derivative(p: Poly, variable: int) -> Poly:
    out: Poly = {}
    for (i, j), c in p.items():
        exponent = i if variable == 0 else j
        if exponent:
            m = (i - 1, j) if variable == 0 else (i, j - 1)
            out[m] = (exponent * c) % MOD
    return norm(out)


def jacobian(p: Poly, q: Poly) -> Poly:
    return add(mul(derivative(p, 0), derivative(q, 1)),
               scale(-1, mul(derivative(p, 1), derivative(q, 0))))


def high(p: Poly) -> Poly:
    return {m: c for m, c in norm(p).items() if sum(m) > CAP}


def degree(p: Poly) -> int:
    return max((sum(m) for m in norm(p)), default=-1)


def ordered(p: Poly) -> list[tuple[Monomial, int]]:
    return sorted(norm(p).items(), key=lambda item: (sum(item[0]), item[0]))


b: Poly = {(5, 0): 1}
c: Poly = {(0, 1): 1, (1, 0): 2, (2, 0): 2, (2, 1): 2, (3, 0): 1}
d: Poly = {
    (0, 1): 1, (1, 0): 2, (1, 1): 2, (2, 0): 2, (0, 3): 2,
    (1, 2): 1, (3, 0): 1, (4, 0): 2, (5, 0): 2, (7, 0): 2,
}
e: Poly = {
    (0, 1): 2, (1, 0): 2, (0, 2): 2, (1, 1): 1, (2, 0): 2,
    (0, 3): 1, (1, 2): 1, (2, 1): 2, (4, 0): 2, (4, 1): 1,
    (5, 0): 1,
}
f: Poly = {
    (0, 2): 1, (2, 0): 2, (0, 3): 1, (2, 1): 2, (3, 0): 1,
    (1, 3): 1, (3, 1): 1, (4, 0): 2, (3, 2): 1, (6, 1): 1,
    (7, 0): 1,
}
g: Poly = {
    (1, 0): 1, (1, 1): 2, (2, 0): 2, (1, 2): 2, (3, 0): 2,
    (2, 2): 1, (4, 0): 2, (2, 3): 2, (3, 3): 1, (6, 0): 1,
    (6, 1): 2, (7, 0): 1,
}
h: Poly = {
    (0, 1): 1, (0, 2): 1, (1, 1): 2, (0, 3): 2, (1, 2): 1,
    (2, 1): 1, (3, 1): 2, (1, 4): 2, (2, 3): 1, (3, 2): 2,
    (4, 1): 2, (0, 6): 2, (3, 3): 1, (4, 2): 1, (1, 6): 2,
    (4, 3): 2, (5, 2): 2, (6, 1): 1,
}

A = add(X, scale(9, c), scale(27, e), scale(81, g))
B = add(Y, scale(3, b), scale(9, d), scale(27, f), scale(81, h))
S6: Poly = {}
for j in range(6):
    S6 = add(S6, scale(3**j, power(A, 2*j)))
P = add(A, scale(-1, power(A, 3)))
Q = mul(B, S6)
# Independent p-adic Taylor formulas used by the bounded solver.
x2, x3 = power(X, 2), power(X, 3)
P_taylor = add(
    X, scale(-1, x3), scale(9, c), scale(27, e), scale(81, g),
    scale(-27, mul(x2, c)), scale(-81, mul(x2, e)),
    scale(-243, mul(x2, g)), scale(-243, mul(X, mul(c, c))),
)
Sbase: Poly = {}
for j in range(6):
    Sbase = add(Sbase, scale(3**j, power(X, 2*j)))
Q_taylor = mul(B, Sbase)
Q_taylor = add(
    Q_taylor,
    scale(54, mul(Y, mul(X, c))), scale(162, mul(Y, mul(X, e))),
    scale(486, mul(Y, mul(X, g))), scale(243, mul(Y, mul(c, c))),
    scale(324, mul(Y, mul(x3, c))), scale(243, mul(Y, mul(x3, e))),
    scale(162, mul(b, mul(X, c))), scale(486, mul(b, mul(X, e))),
    scale(243, mul(b, mul(x3, c))), scale(486, mul(d, mul(X, c))),
)
assert norm(P_taylor) == norm(P)
assert norm(Q_taylor) == norm(Q)
J = add(jacobian(A, B), {(0, 0): -1})
assert all(coefficient % 243 == 0 for coefficient in J.values())
R = {m: (coefficient // 243) % 3 for m, coefficient in J.items()
     if (coefficient // 243) % 3}
cartier = {m: coefficient for m, coefficient in R.items()
           if m[0] % 3 == 2 and m[1] % 3 == 2}

print("A_degree_mod729", degree(A))
print("B_degree_mod729", degree(B))
print("P_degree_mod729", degree(P))
print("Q_degree_mod729", degree(Q))
print("R", ordered(R))
print("Cartier", ordered(cartier))
print("P_high", ordered(high(P)))
print("Q_high", ordered(high(Q)))
print("det_mod243", ordered(norm(add(J, ONE), 243)))
