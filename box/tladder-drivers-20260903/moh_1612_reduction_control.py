#!/usr/bin/env python3
"""Moh Appendix II pp.208--209, (16,12) count and Jacobian controls.

Rings:
  source-shape check: Q[b1..b4,u1,c1,c2,c3,c4,c5,c7,c8,c9,c10,
                         c11,c12,c13,C,x,y]
  normalized check:   Q[b1..b4,c3,c4,c8,c9,c10,a2,C,x,y]
Here x=gamma, y=pi and J(f,g)=f_x*g_y-f_y*g_x.  The pair order is
(f,g), degrees (12,16), while Moh's table order is (n,m)=(16,12).

The p.208 line is taken literally: alpha3=c5*A+c5*B+c7.  We also explain
the equally dimension-17 editorial/gauge interpretation with an independent
c6 and the removable constant alpha1 suppressed.
"""
import sympy as sp

x, y = sp.symbols("x y")
b1, b2, b3, b4 = sp.symbols("b1:5")
C = sp.symbols("C")

h = sp.expand(y**3*(y-x) + b1*y**3 + b2*y**2 + b3*y + b4)
A = sp.expand((h-b4)/y)
B = sp.expand((h-b3*y-b4)/y**2)
assert h == sp.expand(y*A+b4) == sp.expand(y**2*B+b3*y+b4)


def jac(u, v):
    return sp.diff(u, x)*sp.diff(v, y) - sp.diff(u, y)*sp.diff(v, x)


def hadic_digits(poly):
    """Low-to-high canonical h-adic digits in Q[parameters,x][y], deg_y<4."""
    cur = sp.Poly(poly, y)
    hp = sp.Poly(h, y)
    out = []
    while cur.degree() >= 4:
        quo, rem = sp.div(cur, hp)
        out.append(sp.expand(rem.as_expr()))
        cur = quo
    out.append(sp.expand(cur.as_expr()))
    return out


# -------------------------------------------------------------------------
# Literal p.208 source shape and the 17 count.
u1 = sp.symbols("u1")                 # constant alpha1
c1, c2, c3L, c4L, c5, c7, c8L, c9L, c10L, c11, c12, c13 = sp.symbols(
    "c1 c2 c3 c4 c5 c7 c8 c9 c10 c11 c12 c13"
)
alpha2L = c1*A+c2
beta2L = c3L*A+c4L
alpha3L = c5*A+c5*B+c7                # literal repeated c5 on p.208
beta3L = c8L*A+c9L*B+c10L
alpha4L = c11*A+c12*B+c13*(y-x)
fL = h**3+beta2L*h+beta3L
gL = h**4+u1*h**3+alpha2L*h**2+alpha3L*h+alpha4L
JL = jac(fL, gL)
RL = sp.Poly(JL-C*x, x, y)
literal_parameters = (
    b1, b2, b3, b4, u1,
    c1, c2, c3L, c4L, c5, c7, c8L, c9L, c10L, c11, c12, c13,
)
assert len(literal_parameters) == 17
assert sp.degree(fL, y) == sp.Poly(fL, x, y).total_degree() == 12
assert sp.degree(gL, y) == sp.Poly(gL, x, y).total_degree() == 16

literal_digits = [beta2L, beta3L, u1, alpha2L, alpha3L, alpha4L]
literal_xdegrees = [sp.degree(z, x) for z in literal_digits]

print("SOURCE_READ p.208 literal alpha3 = c5*A+c5*B+c7")
print("LITERAL_PRENORMALIZED_COUNT: 4(h)+1(alpha1)+12(distinct displayed c's)=17")
print("LITERAL_H_DIGIT_x_DEGREES:", literal_xdegrees, "(all <= 1)")
print("LITERAL_J_EQ_Cx: equations=%d, J_bidegree=(%d,%d), J_total_degree=%d" %
      (len(RL.terms()), RL.degree(x), RL.degree(y), sp.Poly(JL, x, y).total_degree()))
print("LITERAL_SYSTEM_SOLVED_HERE: False (count/degree control only)")
print("EDITORIAL_GAUGE_ALTERNATIVE: replace second c5 by independent c6 and")
print("  remove constant alpha1 by g -> g-alpha1*f; count remains 4+13=17")


# -------------------------------------------------------------------------
# Moh p.209 normalized ten-parameter family.
c3, c4, c8, c9, c10, a2 = sp.symbols("c3 c4 c8 c9 c10 a2")
beta2 = sp.expand(c3*A+c4)
beta3 = sp.expand(c8*A+c9*B+c10)

gamma_q, gamma_star = sp.div(sp.Poly(beta2*beta3, y), sp.Poly(h, y), y)
delta_q, delta_star = sp.div(sp.Poly(beta2**3, y), sp.Poly(h**2, y), y)
gamma = sp.expand(gamma_q.as_expr())
delta = sp.expand(delta_q.as_expr())
assert sp.degree(gamma_star.as_expr(), y) < 4
assert sp.degree(delta_star.as_expr(), y) < 8

f = sp.expand(h**3+beta2*h+beta3)
g_before_constant_gauge = sp.expand(
    h**4
    + sp.Rational(4, 3)*(beta2*h**2+beta3*h)
    + sp.Rational(2, 9)*(beta2**2+2*gamma)
    - sp.Rational(4, 81)*delta
    + a2*h**2
)

# Its canonical low H-digit has one scalar constant K.  Moh's target change
# g -> g-a4 removes it.  Since K is independent of x,y, J is unchanged.
K = (
    -sp.Rational(4, 81)*b1*c3**3
    + sp.Rational(4, 9)*b1*c3*c9
    + sp.Rational(2, 9)*c4**2
)
g = sp.expand(g_before_constant_gauge-K)
fd = hadic_digits(f)
gd = hadic_digits(g)
assert len(fd) == 4 and len(gd) == 5
assert fd[3] == 1 and fd[2] == 0 and fd[1] == beta2 and fd[0] == beta3
assert gd[4] == 1 and gd[3] == 0

# Embedding of the ten-parameter family in the independent-c6/gauged-alpha1
# reading of the p.208 family.  Eight old c's satisfy relations, but the new
# residual a2 parametrizes one of them: dimension 17+1-8=10.
relations = {
    "c1": sp.Rational(4, 3)*c3,
    "c2": a2+sp.Rational(4, 3)*c4,
    "c5": sp.Rational(4, 3)*c8,
    "c6": sp.Rational(2, 9)*c3**2+sp.Rational(4, 3)*c9,
    "c7": sp.Rational(4, 3)*c10,
    "c11": sp.Rational(2, 9)*b3*c3**2+sp.Rational(4, 9)*c3*c4,
    "c12": -sp.Rational(2, 9)*b4*c3**2+sp.Rational(4, 9)*c3*c8,
    "c13": -sp.Rational(4, 81)*c3**3+sp.Rational(4, 9)*c3*c9,
}
assert gd[2] == sp.expand(relations["c1"]*A+relations["c2"])
assert gd[1] == sp.expand(
    relations["c5"]*A+relations["c6"]*B+relations["c7"]
)
assert gd[0] == sp.expand(
    relations["c11"]*A+relations["c12"]*B+relations["c13"]*(y-x)
)

normalized_parameters = (b1, b2, b3, b4, c3, c4, c8, c9, c10, a2)
assert len(normalized_parameters) == 10
nonconstant_digits = [fd[1], fd[0], gd[2], gd[1], gd[0]]
assert all(sp.degree(z, x) <= 1 for z in nonconstant_digits)

print("NORMALIZED_COUNT: 4(h)+2(beta2)+3(beta3)+1(a2)=10")
print("NORMALIZED_EMBEDDING_RELATIONS (8 relations, one new residual a2):")
for name, value in relations.items():
    print(" ", name, "=", value)
print("CANONICAL_H_DIGITS_f low-to-high x-degrees:",
      [sp.degree(z, x) for z in fd])
print("CANONICAL_H_DIGITS_g low-to-high x-degrees:",
      [sp.degree(z, x) for z in gd])
print("NONCONSTANT_DIGITS: 5; max deg_x=1 <= k+1=2")


# -------------------------------------------------------------------------
# Exact coefficient certificate: normalized family has no J=C*x, C != 0.
J = sp.expand(jac(f, g))
R = sp.Poly(J-C*x, x, y)
assert len(R.terms()) == 36
assert (sp.degree(J, x), sp.degree(J, y), sp.Poly(J, x, y).total_degree()) == (3, 13, 13)

def rc(ix, iy):
    return sp.factor(R.coeff_monomial(x**ix*y**iy))

# [x y^0] gives C explicitly, hence c3,c9,D are all nonzero at C!=0.
D = c3**2-9*c9
assert sp.factor(81*rc(1, 0) - (-81*C+4*c3*c9*D)) == 0
assert sp.factor(rc(3, 10) - 2*a2*c3) == 0

# Consequences valid on the C!=0 branch.
sub_a2 = {a2: 0}
assert sp.factor(rc(1, 1).subs(sub_a2) - sp.Rational(8, 81)*c3*D*(b4*c3+c8)) == 0
sub_c8 = {a2: 0, c8: -b4*c3}
E0 = 5*c3**4-36*c3**2*c9+54*c9**2
assert sp.factor(rc(2, 4).subs(sub_c8) + sp.Rational(4, 81)*E0) == 0
assert sp.factor(
    rc(2, 5).subs(sub_c8) + sp.Rational(4, 9)*b4*c3*(5*c3**2-18*c9)
) == 0

# E0 and 5*c3^2-18*c9 have no common zero with c3!=0, so b4=0.
r = sp.symbols("r")
E = 54*r**2-36*r+5
assert sp.gcd(E, 5-18*r) == 1
assert sp.gcd(E, 1-3*r) == 1
sub_zero4 = {a2: 0, c8: 0, b4: 0}
e6 = sp.factor(rc(2, 6).subs(sub_zero4))
e7 = sp.factor(rc(2, 7).subs(sub_zero4))
assert sp.factor(
    e6-sp.Rational(8, 27)*(b3*c3**3+3*c3**2*c4-9*c4*c9)
) == 0
assert sp.factor(
    e7-sp.Rational(4, 27)*c3*(b2*c3**2-9*b2*c9-9*c10)
) == 0

# Put c9=r*c3^2 and solve e6=e7.  Denominator 1-3r is nonzero modulo E.
sub_rat = {
    a2: 0,
    b4: 0,
    c8: 0,
    c9: r*c3**2,
    c4: -b3*c3/(3*(1-3*r)),
    c10: b2*c3**2*(1-9*r)/9,
}

def numerator_remainder(ix, iy):
    z = sp.cancel(rc(ix, iy).subs(sub_rat))
    numerator = sp.together(z).as_numer_denom()[0]
    return sp.factor(sp.rem(sp.Poly(numerator, r), sp.Poly(E, r)).as_expr())

rem_b3 = numerator_remainder(1, 4)
rem_b2 = numerator_remainder(1, 3)
assert rem_b3 == -6*b3**2*c3**3*(6*r-1)
assert rem_b2 == -12*b2*c3**4*(4*r-1)
assert sp.gcd(E, 6*r-1) == 1
assert sp.gcd(E, 4*r-1) == 1
# Thus b3=0, then b2=0.  The last coefficient contradicts E=0.
rem_final = sp.factor(numerator_remainder(0, 1).subs({b3: 0, b2: 0}))
assert rem_final == sp.Rational(10, 3)*c3**5*(9*r-2)
assert sp.gcd(E, 9*r-2) == 1

print("NORMALIZED_J_EQ_Cx: equations=36, J_bidegree=(3,13), J_total_degree=13")
print("SATURATED_C_NE_0_CERTIFICATE:")
print("  C=(4/81)c3*c9*(c3^2-9c9), so c3,c9,c3^2-9c9 are nonzero")
print("  successive coefficients give a2=0, c8=-b4*c3")
print("  E(r)=54r^2-36r+5=0 for r=c9/c3^2")
print("  gcd(E,5-18r)=1 gives b4=0")
print("  next two equations solve c4,c10 (gcd(E,1-3r)=1)")
print("  gcd(E,6r-1)=gcd(E,4r-1)=1 gives b3=b2=0")
print("  final coefficient forces 9r-2=0, but gcd(E,9r-2)=1")
print("SATURATED_CONCLUSION: no solution with C != 0 in normalized family")
