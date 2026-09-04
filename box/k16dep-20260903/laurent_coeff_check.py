import sympy as sp
gamma, pi, X, H = sp.symbols("gamma pi X H")
b1, b2, b3, b4, y, g = sp.symbols("b1 b2 b3 b4 y g")
z = pi - gamma; B = sp.expand(pi * z + b1 * pi + b2); A = sp.expand(pi * B + b3); h = sp.expand(pi * A + b4)
LX = X - b4
def gen(name, deg):
    cs = sp.symbols("%s0:%d" % (name, deg + 1)); return sum(c * X**i for i, c in enumerate(cs))
U, R, V, S, T = gen("u", 2), gen("r", 1), gen("v", 2), gen("s", 1), gen("t", 1)
Q = U.subs(X, h) + A * R.subs(X, h) + y * B
P = V.subs(X, h) + A * S.subs(X, h) + B * T.subs(X, h) + g * z
J = sp.expand(sp.diff(Q, gamma) * sp.diff(P, pi) - sp.diff(Q, pi) * sp.diff(P, gamma))
# change variables (gamma,pi) -> (H,pi): gamma = (pi^4 + b1 pi^3 + b2 pi^2 + b3 pi + b4 - H)/pi^3  (h = H)
gsub = (pi**4 + b1 * pi**3 + b2 * pi**2 + b3 * pi + b4 - H) / pi**3
JH = sp.expand(sp.cancel(sp.expand((pi**3 * J).subs(gamma, gsub))))
Q1 = LX * R - y * b3; Q2 = y * LX; P0 = V - g * b1; P1 = LX * S - b3 * T - g * b2; P2 = LX * T - g * b3; P3 = g * LX
d = lambda f: sp.diff(f, X)
D = [Q1 * d(P0) - d(U) * P1,
     2 * Q2 * d(P0) + Q1 * d(P1) - d(Q1) * P1 - 2 * d(U) * P2,
     -3 * d(U) * P3 + Q1 * d(P2) - 2 * d(Q1) * P2 + 2 * Q2 * d(P1) - d(Q2) * P1,
     Q1 * d(P3) - 3 * d(Q1) * P3 + 2 * (Q2 * d(P2) - d(Q2) * P2),
     2 * Q2 * d(P3) - 3 * d(Q2) * P3]
D = [sp.expand(Di.subs(X, H)) for Di in D]
pred = -(D[0] * pi**4 + D[1] * pi**3 + D[2] * pi**2 + D[3] * pi + D[4])
print("pi^3 J in K[H][pi^{+-1}] equals -(D0 pi^4 + D1 pi^3 + D2 pi^2 + D3 pi + D4)(H):", sp.expand(JH - pred) == 0)
Jpoly = sp.Poly(JH, pi)
print("min/max pi-degree of pi^3 J in K[H][pi]:", min(Jpoly.monoms())[0] if Jpoly.monoms() else None, Jpoly.degree())
c0 = Jpoly.coeff_monomial(1)
print("pi^0 coefficient of pi^3 J =", sp.factor(c0), " ; equals y*g*(H-b4) = -D4(H):", sp.expand(c0 - y * g * (H - b4)) == 0)
print("=> J == 0 is impossible for any chart pair (y g != 0): the literal dependent-pair system is inconsistent identically.")
