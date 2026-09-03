#!/usr/bin/env python3
"""SQ engine: the second affine spine restricted to a coordinate sub-chart,
symbolically in t (and in the offset r), following box/k16terminal-opus-
20260903/c1_b3axis.py but with two residual variables.

Sub-chart   S_r = { b4 = 0, q_{i,0} = 0 for i != t-r },  residual (x, b3)
            x = q_{t-r,0},  wt(x) = t-r ;   wt(b3) = t+1 ;  wt(h) = 1.

Polynomials in h are carried as dictionaries keyed by the exponent triple
(a,b,c) standing for a*t + b*r + c; coefficients live in Q(t,r)[d]/(3d^2-(t+1)).
Two exponent triples are treated as distinct symbols: the (t,r) pairs at which
two of them collide are enumerated afterwards by collisions() and reported, so
the closed forms below are valid exactly outside that finite list.
"""
import sympy as sp

t, r = sp.symbols("t r")
x, b3, d = sp.symbols("x b3 d")
c1, c2, c3, c4, c5 = sp.symbols("c1 c2 c3 c4 c5")

q = 2*t+1
e = 3*t+1
MIN = 3*d**2 - (t+1)


GENS = (x, b3, c1, c2, c3, c4, c5)
_SC = {}

R_VALUE = None


def set_t(val):
    """Specialise t to an integer: exponents become numbers, A_t=Q[d]/(3d^2-t-1)."""
    global t, MIN, y, g, g1, g2, cc, q, e
    t = sp.Integer(val)
    q, e = 2*t+1, 3*t+1
    MIN = 3*d**2 - (t+1)
    _SC.clear()
    y = red((d+t+1)/(2*q))
    g = red(e*t*(3*d+2*(t+1))/(6*q**3))
    g1 = sp.Rational(e, q)
    g2 = red(g*(3*t+2)/(2*t*y))
    cc = red(-y*g)


def set_r(val):
    """Fix the offset r to an integer: exponents fold and coefficients specialise."""
    global R_VALUE
    R_VALUE = None if val is None else sp.Integer(val)
    _SC.clear()




def _dred(p):
    """reduce d-degree modulo 3d^2 = t+1"""
    P = sp.Poly(sp.expand(p), d)
    tot = 0
    for (k,), co in P.terms():
        pw, kk = sp.Integer(1), k
        while kk >= 2:
            pw = pw*(t+1)/sp.Integer(3)
            kk -= 2
        tot += co*pw*d**kk
    return sp.expand(tot)


def sred(co):
    """normal form of a scalar of A_t = Q(t,r)[d]/(3d^2-(t+1)), as u + v*d"""
    key = sp.srepr(co)
    hit = _SC.get(key)
    if hit is not None:
        return hit
    co = co if R_VALUE is None else co.subs(r, R_VALUE)
    e = sp.together(co)
    n, den = sp.fraction(e)
    n, den = _dred(n), sp.expand(den)
    if den.has(d):
        den = _dred(den)
        P = sp.Poly(den, d)
        A, B = P.nth(1), P.nth(0)
        n = _dred(sp.expand(n*(B - A*d)))
        den = sp.expand(B**2 - A**2*(t+1)/sp.Integer(3))
    P = sp.Poly(n, d)
    u = sp.cancel(P.nth(0)/den)
    v = sp.cancel(P.nth(1)/den)
    out = u + v*d
    _SC[key] = out
    return out


def red(expr):
    """Normal form in Q(t,r)[d]/(3d^2-(t+1)), monomial-wise in GENS."""
    expr = sp.expand(expr)
    if expr == 0:
        return sp.Integer(0)
    P = sp.Poly(expr, *GENS)
    out = 0
    for mon, co in P.terms():
        s = sred(co)
        if s == 0:
            continue
        out += s*sp.prod([gg**a for gg, a in zip(GENS, mon)])
    return out


y  = red((d+t+1)/(2*q))
g  = red(e*t*(3*d+2*(t+1))/(6*q**3))
g1 = sp.Rational(1, 1)*e/q
g2 = red(g*(3*t+2)/(2*t*y))
cc = red(-y*g)                                     # band-zero unit c = -y g


# ---------------------------------------------------------------- h-algebra
def E(a, b, c):
    if R_VALUE is None:
        return (a, b, c)
    return (a, 0, b*int(R_VALUE) + c)


def ex(k):
    return k[0]*t + k[1]*r + k[2]


def hclean(P):
    return {k: red(v) for k, v in P.items() if red(v) != 0}


def hadd(*Ps):
    out = {}
    for P in Ps:
        for k, v in P.items():
            out[k] = out.get(k, 0) + v
    return hclean(out)


def hscal(a, P):
    return hclean({k: a*v for k, v in P.items()})


def hmul(P, Q):
    out = {}
    for k1, v1 in P.items():
        for k2, v2 in Q.items():
            k = (k1[0]+k2[0], k1[1]+k2[1], k1[2]+k2[2])
            out[k] = out.get(k, 0) + v1*v2
    return hclean(out)


def hdiff(P):
    return hclean({(k[0], k[1], k[2]-1): v*ex(k) for k, v in P.items()})


def hshift(P, n):
    return {(k[0], k[1], k[2]+n): v for k, v in P.items()}


def hint(P):
    """antiderivative with zero constant term"""
    return hclean({(k[0], k[1], k[2]+1): v/(ex(k)+1) for k, v in P.items()})


def heuler(P):
    """solve y*(D + 2 h D') = P coefficientwise: [h^m]D = [h^m]P/(y(2m+1))"""
    return hclean({k: v/(y*(2*ex(k)+1)) for k, v in P.items()})


def hcoeff(P, k):
    return red(P.get(k, 0))


def hsubs(P, sub):
    return hclean({k: v.subs(sub) for k, v in P.items()})


# ---------------------------------------------------------------- the spine
def spine(has_b1):
    """Build the restricted spine.  Returns (bands, unknowns, extra_eqs)."""
    # C = h^{t-1} + c1 x h^{r-1}                      (C_{t-r} = c1 x)
    C = {E(1, 0, -1): sp.Integer(1), E(0, 1, -1): c1*x}
    A = hshift(C, 1)                                  # A = h*C
    # U = h^q + x h^{t+r+1} + c2 b3 h^t + c3 x^2 h^{2r+1} + c4 x b3 h^r
    U = {E(2, 0, 1): sp.Integer(1), E(1, 1, 1): x, E(1, 0, 0): c2*b3,
         E(0, 2, 1): c3*x**2, E(0, 1, 0): c4*x*b3}
    # B' = (g/2y)(5C + 3 h C'),  B(0)=B0=0
    Bp = hscal(g/(2*y), hadd(hscal(5, C), hscal(3, hshift(hdiff(C), 1))))
    B = hint(Bp)
    # rhs_D = 3g U' + A B - h A B' + 2 h A' B + g b3 (C + (5/2) A')
    Up, Ap = hdiff(U), hdiff(A)
    rhsD = hadd(hscal(3*g, Up), hmul(A, B),
                hscal(-1, hshift(hmul(A, Bp), 1)),
                hscal(2, hshift(hmul(Ap, B), 1)),
                hscal(g*b3, hadd(C, hscal(sp.Rational(5, 2), Ap))))
    D = heuler(rhsD)
    V = hadd(hshift(A, 1), {E(0, 0, 0): -y*b3})       # V = hA - y b3
    Y = hadd(hshift(D, 1), hscal(-b3, B))             # Y = hD - b3 B - g b2, b2=0
    Z = hadd(hshift(B, 1), {E(0, 0, 0): -g*b3})       # Z = hB - g b3
    b1val = c5*x*b3**2 if has_b1 else sp.Integer(0)
    num = hadd({E(0, 0, 0): y*g*b1val},
               hscal(-1, hmul(V, hdiff(Y))), hmul(hdiff(V), Y),
               hscal(2, hmul(Up, Z)))
    const = hcoeff(num, E(0, 0, 0))                   # divisibility condition
    extra = []
    if has_b1:
        sol = sp.solve(sp.Eq(sp.expand(const/(x*b3**2)), 0), c5)
        assert len(sol) == 1, sol
        C5 = red(sol[0])
        num = hsubs(num, {c5: C5})
        extra.append(("b1", C5))
        assert hcoeff(num, E(0, 0, 0)) == 0
    else:
        extra.append(("b1_condition", const))
    Xp = hscal(1/(2*y), hshift(num, -1))              # X' = num/(2 y h)
    Phi = hadd(hmul(V, Xp), hscal(-1, hmul(Up, Y)), {E(0, 0, 0): cc})
    return dict(C=C, A=A, U=U, B=B, D=D, V=V, Y=Y, Z=Z, Xp=Xp, Phi=Phi,
                extra=dict(extra))


def collisions(P, lo=2, hi=40, rfix=None):
    """(t,r) pairs at which two distinct exponent triples of P coincide."""
    keys = sorted(P)
    bad = {}
    for i in range(len(keys)):
        for j in range(i+1, len(keys)):
            diff = sp.expand(ex(keys[i]) - ex(keys[j]))
            if rfix is not None:
                diff = sp.expand(diff.subs(r, rfix))
            sols = sp.solve(sp.Eq(diff, 0), t)
            for s in sols:
                if s.is_Integer and lo <= s <= hi:
                    bad.setdefault(int(s), []).append((keys[i], keys[j]))
    return bad


def spec_r(P, rval):
    out = {}
    for k, v in P.items():
        kk = (k[0], 0, k[1]*rval + k[2])
        out[kk] = out.get(kk, 0) + v.subs(r, rval)
    return hclean(out)


def bands(Phi):
    """dict  exponent-triple -> coefficient, sorted by (a,b,c)."""
    return {k: red(v) for k, v in sorted(Phi.items()) if red(v) != 0}
