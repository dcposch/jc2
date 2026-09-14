#!/usr/bin/env python3
"""Reviewer (Fable) transcription control for the rank-vacuity lemma.

Checks, with explicit exceptions and no assert nodes:
 (1) the polarization det(M-A) = det M + det A - (dr - cs - bt + aw) on symbolic 2x2;
 (2) for a random F with two-line top y^p (y-x)^q (p,q>0) and a random G of lower
     degree, at a random rational basepoint a, the degree-(n-1) homogeneous part of
     the mixed term  -D F_x + C F_y + B G_x - A G_y  equals -D d_x F_n + C d_y F_n
     and is nonzero whenever (C,D) != (0,0);
 (3) the kernel of (vx,vy) -> vx d_x F_n + vy d_y F_n is zero over Q for the four
     exponent pairs, by exact linear algebra on the coefficient matrix.
This is NOT a Keller pair (none with a two-line top is available); it only audits the
degree bookkeeping and the hypothesis, exactly as the lemma's proof uses them.
"""
import json, random
import sympy as S

def require(c, m):
    if not c:
        raise ValueError(m)

r, s, t, w, a, b, c, d = S.symbols("r s t w a b c d")
M, A = S.Matrix([[r, s], [t, w]]), S.Matrix([[a, b], [c, d]])
mixed = d*r - c*s - b*t + a*w
require(S.expand((M-A).det() - (M.det() + A.det() - mixed)) == 0, "polarization")

x, y = S.symbols("x y")
rng = random.Random(20260906)
def rand_poly(deg_max, deg_min=0):
    return sum(rng.randint(-5, 5)*x**i*y**(j-i) for j in range(deg_min, deg_max+1) for i in range(j+1))
def hom_part(P, k):
    P = S.Poly(S.expand(P), x, y)
    return sum(coef*x**i*y**j for (i, j), coef in P.terms() if i + j == k)

results = []
for p, q in ((1, 1), (2, 3), (4, 2), (3, 5)):
    n = p + q
    Fn = y**p*(y-x)**q
    F = Fn + rand_poly(n-1)
    m = rng.randint(1, n-1)
    G = rand_poly(m, 0) + x**m + 3*y**m   # degree exactly m < n
    ax, ay = S.Rational(rng.randint(-7, 7), rng.randint(1, 4)), S.Rational(rng.randint(-7, 7), rng.randint(1, 4))
    Fx, Fy, Gx, Gy = S.diff(F, x), S.diff(F, y), S.diff(G, x), S.diff(G, y)
    Aa, Bb, Cc, Dd = [e.subs({x: ax, y: ay}) for e in (Fx, Fy, Gx, Gy)]
    mixed_term = -Dd*Fx + Cc*Fy + Bb*Gx - Aa*Gy
    top = hom_part(mixed_term, n-1)
    predicted = S.expand(-Dd*S.diff(Fn, x) + Cc*S.diff(Fn, y))
    require(S.expand(top - predicted) == 0, "top-degree part of the mixed term")
    require(S.Poly(S.expand(mixed_term), x, y).total_degree() == n-1, "mixed term degree n-1")
    require((Cc, Dd) != (0, 0), "basepoint with (C,D)=(0,0) drawn; rerun")
    require(top != 0, "top part nonzero at this basepoint")
    # (3) exact kernel of the directional-derivative map on Q^2
    vx, vy = S.symbols("vx vy")
    dirv = S.Poly(S.expand(vx*S.diff(Fn, x) + vy*S.diff(Fn, y)), x, y)
    rows = [[S.Poly(coef, vx, vy).coeff_monomial(vx), S.Poly(coef, vx, vy).coeff_monomial(vy)] for coef in dirv.coeffs()]
    require(S.Matrix(rows).rank() == 2, "constant null direction exists")
    results.append({"p": p, "q": q, "n": n, "m": m, "basepoint": [str(ax), str(ay)], "top_degree_ok": True})
print(json.dumps({"status": "PASS", "polarization": True, "cases": results}, sort_keys=True))
