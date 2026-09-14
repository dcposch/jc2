#!/usr/bin/env python3
"""Two-centre normalisation probes for the (99,66) joint chart (sec 2.4 of
xmodel/g9966-chart-necessity-opus5-20260903.md).

(1) MAJOR: keep the D_2 centre constant w_0 general (w = 1 + w_0 s^3 + pi s^4,
    t = s^3) on all 66 lower h3 slots; impose ord_s K3 >= 32 and [s^32]K3 = pi^8.
(2) MINOR: keep the principal-minor centre constant a_0 general
    (w = a_0 t + u t^2 + z t^3) on the 21-dimensional strict h3 space; impose
    ord_t K3 >= 9.
Both systems are LINEAR in the h3 coefficients; we report row count, rank(A) and
rank([A|b]) for several values of the centre constant.
"""
import sympy as sp

s, pi, t, z = sp.symbols('s pi t z')

def major(bval):
    slots = [(r, q) for r in range(1, 12) for q in range(0, 11) if r + q <= 11]
    H = [sp.Symbol('H_%d_%d' % rq) for rq in slots]
    b = sp.Integer(bval)
    w = 1 + b*s**3 + pi*s**4
    K3 = sp.expand(w**3*(w-1)**8
                   + sum(H[i]*s**(3*slots[i][0])*(w-1)**slots[i][1]
                         for i in range(len(slots))))
    P = sp.Poly(K3, s)
    eqs = []
    for E in range(0, 32):
        c = sp.expand(P.coeff_monomial(s**E))
        if c == 0:
            continue
        eqs += [sp.expand(co) for co in sp.Poly(c, pi).all_coeffs() if co != 0]
    c32 = sp.Poly(sp.expand(P.coeff_monomial(s**32)), pi)
    for k, co in zip(range(c32.degree(), -1, -1), c32.all_coeffs()):
        eqs.append(sp.expand(co - (1 if k == 8 else 0)))
    eqs = [e for e in eqs if e != 0]
    A, rhs = sp.linear_eq_to_matrix(eqs, H)
    return len(H), len(eqs), A.rank(), A.row_join(rhs).rank()

def minor(aval, uval):
    free = [(r, q) for r in range(1, 12) for q in range(0, 11)
            if 3*r + 4*q >= 33 and r + q <= 11]
    H = [sp.Symbol('H_%d_%d' % rq) for rq in free]
    a, u = sp.Integer(aval), sp.Integer(uval)
    w = a*t + u*t**2 + z*t**3
    K3 = sp.expand(w**3*(w-1)**8
                   + sum(H[i]*t**free[i][0]*(w-1)**free[i][1]
                         for i in range(len(free))))
    P = sp.Poly(K3, t)
    eqs = []
    for n in range(0, 9):
        c = sp.expand(P.coeff_monomial(t**n))
        if c == 0:
            continue
        eqs += [sp.expand(co) for co in sp.Poly(c, z).all_coeffs() if co != 0]
    eqs = [e for e in eqs if e != 0]
    A, rhs = sp.linear_eq_to_matrix(eqs, H)
    return len(H), len(eqs), A.rank(), A.row_join(rhs).rank()

print("MAJOR D_2 block with a general centre constant w_0")
print("  (ord_s K3 >= 32 and [s^32]K3 = pi^8; 66 ambient h3 slots)")
for bval in (0, 1, 2, -3):
    n, rows, rA, rAb = major(bval)
    print("   w_0=%-3d : %3d rows ; rank(A)=%2d ; rank([A|b])=%2d ; %s ; free %d"
          % (bval, rows, rA, rAb,
             "CONSISTENT" if rA == rAb else "INCONSISTENT", n - rA))
print()
print("MINOR incidence with a general centre constant a_0")
print("  (ord_t K3 >= 9; 21 strict h3 coordinates)")
for aval, uval in ((0, 0), (0, 1), (1, 0), (1, 1), (2, 3), (1, -1), (3, 0), (5, 7)):
    n, rows, rA, rAb = minor(aval, uval)
    print("   a_0=%-2d u=%-2d : %2d rows ; rank(A)=%2d ; rank([A|b])=%2d ; %s ; free %d"
          % (aval, uval, rows, rA, rAb,
             "CONSISTENT" if rA == rAb else "INCONSISTENT", n - rA))
