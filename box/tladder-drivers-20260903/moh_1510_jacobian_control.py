#!/usr/bin/env python3
"""Moh Appendix II pp.210--211, post-simplification (15,10) control.

Exact ring: Q[a1,...,a12,C,x,y], with x=gamma and y=pi.  The pair is
ordered (f,g), so (deg f,deg g)=(10,15), while Moh's table is (n,m)=(15,10).
The Jacobian convention is J(f,g)=f_x*g_y-f_y*g_x.

The source shape has 12 scalar parameters already: eight in h and four in
beta.  Consequently it cannot reproduce the earlier source-only count
22 [15 or 13].  This limitation is printed deliberately.
"""
import sympy as sp

x, y = sp.symbols("x y")
a = sp.symbols("a1:13")
C = sp.symbols("C")
(a1, a2, a3, a4, a5, a6, a7, a8,
 a9, a10, a11, a12) = a

B = (y**2 - x**2 + a1*y + a2*x + a3)*y + (a4*x + a5)
A = sp.expand(B*y + (a6*x + a7))
h = sp.expand(A*y + a8)
beta = sp.expand(a9*A + a10*y + a11*x + a12)

# Canonical Euclidean quotient in Q[a_i,x][y].  It is the alpha on p.210.
alpha_poly, gamma_poly = sp.div(sp.Poly(beta**2, y), sp.Poly(h, y), y)
alpha = sp.expand(alpha_poly.as_expr())
gamma = sp.expand(gamma_poly.as_expr())
assert sp.expand(alpha - (a9**2*B + 2*a9*a10)) == 0
assert sp.degree(gamma, y) < 5

f = sp.expand(h**2 + 2*beta)
g = sp.expand(h**3 + 3*beta*h + sp.Rational(3, 2)*alpha)
J = sp.expand(sp.diff(f, x)*sp.diff(g, y) - sp.diff(f, y)*sp.diff(g, x))
R = sp.Poly(J - C*x**2, x, y)

assert sp.degree(f, y) == sp.Poly(f, x, y).total_degree() == 10
assert sp.degree(g, y) == sp.Poly(g, x, y).total_degree() == 15

def coeff(ix, iy):
    return sp.factor(R.coeff_monomial(x**ix*y**iy))

print("SOURCE_SHAPE: Moh pp.210-211 equations (5),(6), post-simplification")
print("RING: Q[a1,...,a12,C,x,y]; coefficient comparison in Q[a_i,C][x,y]")
print("ORIENTATION: table (n,m)=(15,10); actual pair (f,g) has degrees (10,15)")
print("PARAMETER_COUNT_FROM_DISPLAYED_SHAPE: 8(h)+4(beta)=12")
print("EARLIER_22_[15_OR_13]_RECONSTRUCTIBLE_FROM_THIS_SHAPE: False")
print("  reason: p.208 only states those earlier counts; pp.210-211 have already")
print("  applied the second simplification (p.209 says 22[...] -> 12[...]).")
print("H_ADIC_SLOTS:")
print("  f = h^2 + 0*h + 2beta")
print("  g = h^3 + 0*h^2 + 3beta*h + (3/2)alpha")
print("  nonconstant slots = 3; deg_x(beta)=%s, deg_x(alpha)=%s; k+1=3" %
      (sp.degree(beta, x), sp.degree(alpha, x)))
print("J_EQ_Cx2: equations=%d, J_bidegree=(%d,%d), J_total_degree=%d" %
      (len(R.terms()), sp.degree(J, x), sp.degree(J, y),
       sp.Poly(J, x, y).total_degree()))

# A compact exact no-solution certificate for J=C*x^2 with C != 0.
# Branch a9=0: alpha=0 but g still contains 3*beta*h.  The corrected
# identity gives J=6*beta*J(beta,h), not 6*h^2*J(beta,h).
J_a9_zero = sp.factor(J.subs(a9, 0))
divisor_check = sp.factor(
    J_a9_zero - 6*beta.subs(a9, 0) * (
        sp.diff(beta.subs(a9, 0), x)*sp.diff(h, y)
        - sp.diff(beta.subs(a9, 0), y)*sp.diff(h, x)
    )
)
assert divisor_check == 0
print("BRANCH_a9_EQ_0: J=6*beta*J(beta,h), beta=a10*y+a11*x+a12")
print("  If J=C*x^2 with C!=0, beta divides x^2; hence a10=0.")
print("  If beta is constant then J=0.  Otherwise divisibility forces")
print("  beta=a11*x, but J=6*a11^2*x*h_y has y-degree 4: contradiction.")

# Branch a9 != 0.  Read five coefficients successively.
e_a6 = coeff(4, 4)
assert sp.factor(e_a6 - 15*a9*(2*a11+a6*a9)) == 0
subs1 = {a6: -2*a11/a9}
e_a7 = sp.factor(coeff(3, 4).subs(subs1))
assert sp.factor(e_a7 - 6*a9*(2*a12+a7*a9)) == 0
subs2 = {**subs1, a7: -2*a12/a9}
e_a8 = sp.factor(coeff(3, 3).subs(subs2))
assert sp.factor(e_a8 + 12*a8*a9**2) == 0
subs3 = {**subs2, a8: 0}
e1 = sp.factor(coeff(3, 2).subs(subs3) / -6)
e2 = sp.factor(coeff(2, 3).subs(subs3) / -6)
e3 = sp.factor(coeff(1, 4).subs(subs3) / 6)
assert e1 == 3*a11**2 + a9**3
assert e2 == a10*a11
assert e3 == 2*a10**2 + 5*a11**2 + a9**3

print("BRANCH_a9_NE_0 coefficient certificate:")
print("  [x^4 y^4]=0 => a6=-2*a11/a9")
print("  [x^3 y^4]=0 => a7=-2*a12/a9")
print("  [x^3 y^3]=0 => a8=0")
print("  [x^3 y^2]=0 => 3*a11^2+a9^3=0")
print("  [x^2 y^3]=0 => a10*a11=0")
print("  [x^1 y^4]=0 => 2*a10^2+5*a11^2+a9^3=0")
print("  last three imply a10=a11=0, then a9=0: contradiction")
print("SATURATED_CONCLUSION: no solution with C != 0 in this 12-parameter family")
