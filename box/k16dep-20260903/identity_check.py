#!/usr/bin/env python3
"""Symbolic (generic-coefficient) proof-check of the two facts used in the lane:
 (I)  For the chart pair Q = U(h) + A R(h) + y B,  P = V(h) + A S(h) + B T(h) + g z  (z = pi-gamma,
      B = pi z + b1 pi + b2, A = pi B + b3, h = pi A + b4; U,R,V,S,T arbitrary polynomials in h):
        pi^3 * J_{gamma,pi}(Q,P) = -( D0 pi^4 + D1 pi^3 + D2 pi^2 + D3 pi + D4 )|_{X=h}
      with D0..D4 the five polynomials of Sol 17(qqq) (2.3) in X (prime = d/dX), and
 (II) D4 = 2 Q2 P3' - 3 Q2' P3 = -y g L identically (Q2 = yL, P3 = gL, L = X - b4).
 Consequence: J(Q,P) == 0 is impossible in the chart (y g != 0), and on the spine
 (D1..D4 imposed with c = -yg) J(Q,P) = c*gamma + pi*E(h), E := -c - D0.
 (III) The explicit t=2, y=1/5 axis family (symbolic b3) has J = (7/625)(pi - gamma) = -c z."""
import sympy as sp
gamma, pi, X = sp.symbols("gamma pi X")
b1, b2, b3, b4, y, g = sp.symbols("b1 b2 b3 b4 y g")
z = pi - gamma
B = sp.expand(pi * z + b1 * pi + b2)
A = sp.expand(pi * B + b3)
h = sp.expand(pi * A + b4)
L = h - b4
LX = X - b4
def gen(name, deg):
    cs = sp.symbols("%s0:%d" % (name, deg + 1))
    return sum(c * X**i for i, c in enumerate(cs))
U, R, V, S, T = gen("u", 2), gen("r", 1), gen("v", 2), gen("s", 1), gen("t", 1)
Q = U.subs(X, h) + A * R.subs(X, h) + y * B
P = V.subs(X, h) + A * S.subs(X, h) + B * T.subs(X, h) + g * z
J = sp.expand(sp.diff(Q, gamma) * sp.diff(P, pi) - sp.diff(Q, pi) * sp.diff(P, gamma))
# Laurent pieces in X (Sol (2.2))
Q1 = LX * R - y * b3; Q2 = y * LX
P0 = V - g * b1; P1 = LX * S - b3 * T - g * b2; P2 = LX * T - g * b3; P3 = g * LX
d = lambda f: sp.diff(f, X)
D0 = Q1 * d(P0) - d(U) * P1
D1 = 2 * Q2 * d(P0) + Q1 * d(P1) - d(Q1) * P1 - 2 * d(U) * P2
D2 = -3 * d(U) * P3 + Q1 * d(P2) - 2 * d(Q1) * P2 + 2 * Q2 * d(P1) - d(Q2) * P1
D3 = Q1 * d(P3) - 3 * d(Q1) * P3 + 2 * (Q2 * d(P2) - d(Q2) * P2)
D4 = 2 * Q2 * d(P3) - 3 * d(Q2) * P3
# chart decomposition controls: Q = U + Q1/pi + Q2/pi^2, P = P0 + P1/pi + P2/pi^2 + P3/pi^3 (with X = h)
print("A == L/pi      :", sp.expand(pi * A - L) == 0)
print("B == L/pi^2 - b3/pi :", sp.expand(pi**2 * B - L + b3 * pi) == 0)
print("z == -b1 - b2/pi - b3/pi^2 + L/pi^3 :", sp.expand(pi**3 * z + b1 * pi**3 + b2 * pi**2 + b3 * pi - L) == 0)
print("Q == U + Q1/pi + Q2/pi^2 :", sp.expand(pi**2 * Q - (pi**2 * U.subs(X, h) + pi * Q1.subs(X, h) + Q2.subs(X, h))) == 0)
print("P == P0 + P1/pi + P2/pi^2 + P3/pi^3 :", sp.expand(pi**3 * P - (pi**3 * P0.subs(X, h) + pi**2 * P1.subs(X, h) + pi * P2.subs(X, h) + P3.subs(X, h))) == 0)
print("J(h,pi) = h_gamma = -pi^3 :", sp.expand(sp.diff(h, gamma) + pi**3) == 0)
pred = -(D0 * pi**4 + D1 * pi**3 + D2 * pi**2 + D3 * pi + D4)
diff = sp.expand(pi**3 * J - pred.subs(X, h))
print("(I)  pi^3 J == -(D0 pi^4 + D1 pi^3 + D2 pi^2 + D3 pi + D4)|_{X=h} :", diff == 0)
print("(II) D4 == -y g L :", sp.expand(D4 + y * g * LX) == 0)
# The requirement J = c*gamma (chart) <=> D0=-c, D1=-c b1, D2=-c b2, D3=-c b3, D4=c L  (Sol (2.3))
c = sp.Symbol("c")
target = sp.expand(pi**3 * c * gamma)
tgt = -(-c * pi**4 - c * b1 * pi**3 - c * b2 * pi**2 - c * b3 * pi + c * LX.subs(X, h))
print("     c*gamma*pi^3 == -(-c pi^4 - c b1 pi^3 - c b2 pi^2 - c b3 pi + c L) :", sp.expand(target - tgt) == 0)
# On the spine: D1=-c b1, D2=-c b2, D3=-c b3, D4=c L, D0 = -c - E  =>  J = c gamma + pi E
E = sp.Symbol("E")
Jspine = -(( -c - E) * pi + (-c * b1) + (-c * b2) / pi + (-c * b3) / pi**2 + c * L / pi**3)
print("     spine: J == c*gamma + pi*E :", sp.simplify(sp.expand(Jspine - (c * gamma + pi * E))) == 0)
# (III) explicit t=2, y=1/5 axis family, symbolic b3 (b1=b2=b4=0)
b3s = sp.Symbol("b3")
sub0 = {b1: 0, b2: 0, b4: 0}
h2 = h.subs(sub0); A2 = A.subs(sub0); B2 = B.subs(sub0)
Q2p = h2**5 - sp.Rational(1, 2) * b3s * h2**2 + A2 * h2**2 + sp.Rational(1, 5) * B2
P2p = h2**7 - sp.Rational(7, 20) * b3s * h2**4 + A2 * (sp.Rational(7, 5) * h2**4 + sp.Rational(7, 25) * b3s * h2) + sp.Rational(14, 25) * B2 * h2**2 + sp.Rational(7, 125) * (pi - gamma)
Q2p = Q2p.subs(b3, b3s); P2p = P2p.subs(b3, b3s)
J2 = sp.expand(sp.diff(Q2p, gamma) * sp.diff(P2p, pi) - sp.diff(Q2p, pi) * sp.diff(P2p, gamma))
print("(III) t=2 y=1/5 axis family: J =", J2, " ; == (7/625)(pi-gamma):", sp.expand(J2 - sp.Rational(7, 625) * (pi - gamma)) == 0)
print("      degrees: deg Q =", sp.Poly(Q2p, gamma, pi).total_degree(), " deg P =", sp.Poly(P2p, gamma, pi).total_degree())
# (IV) literal dependent pair: P = phi(H), Q = psi(H) has J == 0; impossible since the pi^0 coefficient of pi^3 J is -D4 = y g L != 0
print("(IV) pi^0-coefficient of pi^3*J (generic chart pair) =", sp.factor(sp.Poly(sp.expand(pi**3 * J), pi).coeff_monomial(1)), " (must vanish for J==0; it is y*g*L)")
