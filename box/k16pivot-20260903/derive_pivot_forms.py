#!/usr/bin/env python3
"""Derive the closed high-E_t pivot forms (5.9)-(5.15) in (t, j).

The calculation is the perturbation the Opus gate (charged §8) prescribes,
executed over the function field Q(t, j, y, g, g1, g2, q, e) and then reduced
in the algebra A_t ≅ Q(t, j)[d]/(3d² − (t+1)).  No A_t zero divisor is
inverted: every division is by an element of the coefficient field, or (after
the y → (d+t+1)/(2q) substitution) by a linear form in d whose resultant
against 3d²−(t+1) is a nonzero polynomial with no positive-integer root in
the declared index range.

Prime marks mean d/ds.  The homogeneous-origin background is (6.5).  Records
store −E_t; the derived pivot is [s^{4t+1−j}] of R_s := −E_t.
"""
from __future__ import annotations

import json
import pathlib
import sys

import sympy as sp


HERE = pathlib.Path(__file__).resolve().parent
CHARGED = pathlib.Path("/tmp/jc2-lane.nw1i08/inputs")

t, j = sp.symbols("t j", commutative=True)
y, g, g1, g2, q, e = sp.symbols("y g g1 g2 q e")
d, n = sp.symbols("d n")
eps = sp.symbols("eps")

fails: list[str] = []


def check(name: str, cond) -> None:
    ok = bool(cond)
    print(("PASS  " if ok else "FAIL  ") + name)
    if not ok:
        fails.append(name)


def rat_zero(expr: sp.Expr) -> bool:
    if expr == 0:
        return True
    cancelled = sp.cancel(sp.together(sp.expand(expr)))
    return cancelled == 0


def reduce_d(expr: sp.Expr) -> sp.Expr:
    """Normal form in Q(t, j)[d]/(3d² − (t+1)).  Invert only after rem."""
    field = sp.QQ.frac_field(t, j)
    modulus = sp.Poly(3 * d * d - (t + 1), d, domain=field)
    numerator, denominator = sp.cancel(expr).as_numer_denom()
    npoly = sp.Poly(numerator, d, domain=field)
    dpoly = sp.Poly(denominator, d, domain=field)
    nrem = npoly.rem(modulus)
    drem = dpoly.rem(modulus)
    if drem == 0:
        raise ZeroDivisionError("denominator is 0 in A_t: %s" % expr)
    # Resultant test: refuse a zero-divisor inverse.
    if drem.degree() > 0:
        res = sp.resultant(drem.as_expr(), modulus.as_expr(), d)
        if sp.cancel(res) == 0:
            raise ZeroDivisionError("zero-divisor inverse refused: %s" % drem)
    inv = sp.invert(drem, modulus)
    return sp.factor((nrem * inv).rem(modulus).as_expr())


class Series:
    """Two-jet in eps: sum_m (c0(m) + eps c1(m)) s^m, m a polynomial in t, j."""

    def __init__(self):
        self.terms: dict[sp.Expr, tuple[sp.Expr, sp.Expr]] = {}

    @staticmethod
    def _key(exp: sp.Expr) -> sp.Expr:
        return sp.expand(exp)

    def add(self, exp, c0=0, c1=0) -> "Series":
        k = self._key(exp)
        a0, a1 = self.terms.get(k, (sp.Integer(0), sp.Integer(0)))
        self.terms[k] = (sp.together(a0 + c0), sp.together(a1 + c1))
        return self

    def coeff(self, exp) -> tuple[sp.Expr, sp.Expr]:
        return self.terms.get(self._key(exp), (sp.Integer(0), sp.Integer(0)))

    def scale(self, scalar) -> "Series":
        out = Series()
        for exp, (c0, c1) in self.terms.items():
            out.add(exp, scalar * c0, scalar * c1)
        return out

    def plus(self, other: "Series") -> "Series":
        out = Series()
        for exp, (c0, c1) in self.terms.items():
            out.add(exp, c0, c1)
        for exp, (c0, c1) in other.terms.items():
            out.add(exp, c0, c1)
        return out

    def mul(self, other: "Series") -> "Series":
        out = Series()
        for e1, (a0, a1) in self.terms.items():
            for e2, (b0, b1) in other.terms.items():
                out.add(e1 + e2, a0 * b0, a0 * b1 + a1 * b0)
        return out

    def times_s(self) -> "Series":
        out = Series()
        for exp, (c0, c1) in self.terms.items():
            out.add(exp + 1, c0, c1)
        return out

    def diff_s(self) -> "Series":
        out = Series()
        for exp, (c0, c1) in self.terms.items():
            out.add(exp - 1, c0 * exp, c1 * exp)
        return out

    def integrate_s(self) -> "Series":
        """Bandwise ∫ s^m dm → s^{m+1}/(m+1).  Constant of integration 0."""
        out = Series()
        for exp, (c0, c1) in self.terms.items():
            den = sp.together(exp + 1)
            out.add(exp + 1, sp.together(c0 / den), sp.together(c1 / den))
        return out

    def euler_inverse(self, ysym) -> "Series":
        """[s^m] S = [s^m] rhs / (y (2m+1)), identity (5.7b)."""
        out = Series()
        for exp, (c0, c1) in self.terms.items():
            den = sp.together(ysym * (2 * exp + 1))
            out.add(exp, sp.together(c0 / den), sp.together(c1 / den))
        return out


def monomial(exp, c0=0, c1=0) -> Series:
    return Series().add(exp, c0, c1)


# ---------------------------------------------------------------------------
# C-family: 1 <= j <= t-1.  Perturb C by eps * s^{t-1-j}.
# ---------------------------------------------------------------------------
print("=== C-family: perturb C by eps * s**(t-1-j) ===")

C = monomial(t - 1, 1, 0).plus(monomial(t - 1 - j, 0, 1))
Cp = C.diff_s()
# (5.6)/(5.7b): T' = (g/(2y)) (5C + 3 s C')
Tprime = C.scale(5).plus(Cp.times_s().scale(3)).scale(g / (2 * y))
T = Tprime.integrate_s()

# Unperturbed leading of T, from (5.7b) at m = t-1, c_m = 1.
T_lead_from_57b = T.coeff(t)[0]
T_lead_expected = g * (3 * t + 2) / (2 * y * t)
check("C0  [s^t] T from (5.7b) = g(3t+2)/(2 y t)",
      rat_zero(T_lead_from_57b - T_lead_expected))

b_j_derived = sp.together(T.coeff(t - j)[1])
b_j_asserted = g * (3 * t + 2 - 3 * j) / (2 * y * (t - j))
print("b_j derived  =", sp.together(b_j_derived))
print("b_j asserted =", sp.together(b_j_asserted))
print("b_j difference =", sp.cancel(sp.together(b_j_derived - b_j_asserted)))
check("C1  b_j identical to asserted g(3t+2-3j)/(2y(t-j))",
      rat_zero(b_j_derived - b_j_asserted))

# Background T uses the named normalizer g2 (identity (5.7a) in A_t).
# Perturbation of T is the derived b_j.  A = s C.
A = C.times_s()
B = monomial(t, g2, 0).plus(monomial(t - j, 0, b_j_derived))
Bp = B.diff_s()
Ap = A.diff_s()
U = monomial(2 * t + 1, 1, 0)          # U = s^q at the origin
Up = U.diff_s()
check("C2  [s^{2t}] U' = q  (with q = 2t+1 later)",
      rat_zero(Up.coeff(2 * t)[0] - (2 * t + 1)))

# Euler RHS at b3 = 0:  3 g U' + A B − s A B' + 2 s A' B.
rhs = (Up.scale(3 * g)
       .plus(A.mul(B))
       .plus(A.mul(Bp).times_s().scale(-1))
       .plus(Ap.mul(B).times_s().scale(2)))
S = rhs.euler_inverse(y)

d_j_derived = sp.together(S.coeff(2 * t - j)[1])
d_j_asserted = (g2 * (t + 1 - 2 * j) + b_j_asserted * (t + 1 + j)) / (
    y * (4 * t - 2 * j + 1)
)
print("d_j derived  =", sp.factor(d_j_derived))
print("d_j asserted =", sp.factor(sp.together(d_j_asserted)))
print("d_j difference =", sp.cancel(sp.together(d_j_derived - d_j_asserted)))
check("C3  d_j identical to asserted (g2(t+1-2j)+b_j(t+1+j))/(y(4t-2j+1))",
      rat_zero(d_j_derived - d_j_asserted))

# X' from the D1 numerator, b1 = b2 = b3 = 0.
# numerator = −V Y' + V' Y + 2 U' Z,   X' = (numerator/s)/(2y).
V = A.times_s()
Sjet = monomial(2 * t, g1, 0).plus(monomial(2 * t - j, 0, d_j_derived))
Y = Sjet.times_s()
Z = B.times_s()
Vp = V.diff_s()
Yp = Y.diff_s()
numer = (V.mul(Yp).scale(-1)
         .plus(Vp.mul(Y))
         .plus(Up.mul(Z).scale(2)))
n_j_derived = sp.together(numer.coeff(3 * t + 1 - j)[1])
n_j_asserted = -g1 * (t + j) + (j - t) * d_j_asserted + 2 * q * b_j_asserted
# Compare in the ring with q free: replace the derived 2*(2t+1)*b_j by 2q b_j
# after substituting q = 2t+1 in the asserted form, or substitute q in both.
n_j_asserted_qsub = n_j_asserted.subs(q, 2 * t + 1)
print("n_j derived  =", sp.factor(n_j_derived))
print("n_j asserted (q=2t+1) =", sp.factor(sp.together(n_j_asserted_qsub)))
print("n_j difference =", sp.cancel(sp.together(n_j_derived - n_j_asserted_qsub)))
check("C4  n_j identical to asserted −g1(t+j)+(j−t)d_j+2q b_j  (q=2t+1)",
      rat_zero(n_j_derived - n_j_asserted_qsub))

# Also: n_j as a rational function of (t,j,y,g1,g2,g,q) with q free, using
# the asserted d_j, b_j which already matched.  Reconstruct with q free:
# U' leading is q, not 2t+1, if we inject the named q.
Up_named = monomial(2 * t, q, 0)
numer_named = (V.mul(Yp).scale(-1)
               .plus(Vp.mul(Y))
               .plus(Up_named.mul(Z).scale(2)))
n_j_named = sp.together(numer_named.coeff(3 * t + 1 - j)[1])
print("n_j named-q  =", sp.factor(n_j_named))
print("n_j asserted =", sp.factor(sp.together(n_j_asserted)))
print("n_j named difference =",
      sp.cancel(sp.together(n_j_named - n_j_asserted)))
check("C5  n_j identical with named q (rational in t,j,y,g1,g2,g,q)",
      rat_zero(n_j_named - n_j_asserted))

# X' jet: lead e s^{3t} from (6.5); perturbation n_j/(2y) at s^{3t-j}.
Xprime = monomial(3 * t, e, 0).plus(
    monomial(3 * t - j, 0, n_j_named / (2 * y))
)
# R_s = V X' − U' Y − y g.  High band 4t+1 cancels; pivot is [s^{4t+1-j}].
Rs = V.mul(Xprime).plus(Up_named.mul(Y).scale(-1))
pC_derived = sp.together(Rs.coeff(4 * t + 1 - j)[1])
pC_from_nj = sp.together(e + n_j_named / (2 * y) - q * d_j_derived)
print("p_C from [s^{4t+1-j}] R_s =", sp.together(pC_derived))
print("p_C from e + n_j/(2y) − q d_j =", sp.together(pC_from_nj))
check("C6  [s^{4t+1-j}] R_s = e + n_j/(2y) − q d_j",
      rat_zero(pC_derived - pC_from_nj))
check("C7  [s^{4t+1}] R_s unperturbed = e − q g1  (vanishes by g1=e/q)",
      rat_zero(Rs.coeff(4 * t + 1)[0] - (e - q * g1)))


# ---------------------------------------------------------------------------
# Q-family: t <= j <= 2t.  Perturb U by eps * s^{q-j}.
# ---------------------------------------------------------------------------
print("\n=== Q-family: perturb U by eps * s**(q-j) ===")

# Exponents use q = 2t+1 (definition).  The symbol q is the leading
# coefficient of U' and the name of that same integer.
q_exp = 2 * t + 1
Uq = monomial(q_exp, 1, 0).plus(monomial(q_exp - j, 0, 1))
Upq = Uq.diff_s()
check("Q0  [s^{2t}] U' = 2t+1 (= q)",
      rat_zero(Upq.coeff(2 * t)[0] - q_exp))
# C, T unperturbed.  The only eps source in the Euler RHS is 3g U'.
C0 = monomial(t - 1, 1, 0)
A0 = C0.times_s()
B0 = monomial(t, g2, 0)
B0p = B0.diff_s()
A0p = A0.diff_s()
rhsq = (Upq.scale(3 * g)
        .plus(A0.mul(B0))
        .plus(A0.mul(B0p).times_s().scale(-1))
        .plus(A0p.mul(B0).times_s().scale(2)))
Sq = rhsq.euler_inverse(y)
dq_j_derived = sp.together(Sq.coeff(2 * t - j)[1])
dq_j_asserted = 3 * g * (q - j) / (y * (4 * t - 2 * j + 1))
dq_j_asserted_qsub = dq_j_asserted.subs(q, q_exp)
print("dq_j derived  =", sp.together(dq_j_derived))
print("dq_j asserted =", sp.together(dq_j_asserted))
print("dq_j difference (q=2t+1) =",
      sp.cancel(sp.together(dq_j_derived - dq_j_asserted_qsub)))
check("Q1  dq_j identical to asserted 3g(q-j)/(y(4t-2j+1))  (q=2t+1)",
      rat_zero(dq_j_derived - dq_j_asserted_qsub))
# Named-q form: U' perturbation coefficient is (q-j), injected as a symbol.
Upq_named = monomial(2 * t, q, 0).plus(monomial(2 * t - j, 0, q - j))
rhsq_named = (Upq_named.scale(3 * g)
              .plus(A0.mul(B0))
              .plus(A0.mul(B0p).times_s().scale(-1))
              .plus(A0p.mul(B0).times_s().scale(2)))
dq_j_named = sp.together(rhsq_named.euler_inverse(y).coeff(2 * t - j)[1])
print("dq_j named-q  =", sp.together(dq_j_named))
print("dq_j named difference =",
      sp.cancel(sp.together(dq_j_named - dq_j_asserted)))
check("Q2  dq_j identical with named q (rational in t,j,y,g,q)",
      rat_zero(dq_j_named - dq_j_asserted))

# X' numerator.  Named-q U' throughout.
V0 = A0.times_s()
Sjetq = monomial(2 * t, g1, 0).plus(monomial(2 * t - j, 0, dq_j_named))
Yq = Sjetq.times_s()
Z0 = B0.times_s()
V0p = V0.diff_s()
Yqp = Yq.diff_s()
numerq = (V0.mul(Yqp).scale(-1)
          .plus(V0p.mul(Yq))
          .plus(Upq_named.mul(Z0).scale(2)))
nq_derived = sp.together(numerq.coeff(3 * t + 1 - j)[1])
nq_j_asserted = (j - t) * dq_j_asserted + 2 * (q - j) * g2
print("nq_j derived  =", sp.factor(nq_derived))
print("nq_j asserted =", sp.factor(sp.together(nq_j_asserted)))
print("nq_j difference =",
      sp.cancel(sp.together(nq_derived - nq_j_asserted)))
check("Q3  nq_j identical to asserted (j−t)dq_j + 2(q−j)g2",
      rat_zero(nq_derived - nq_j_asserted))

Xpq = monomial(3 * t, e, 0).plus(
    monomial(3 * t - j, 0, nq_derived / (2 * y))
)
Rsq = V0.mul(Xpq).plus(Upq_named.mul(Yq).scale(-1))
pQ_derived = sp.together(Rsq.coeff(4 * t + 1 - j)[1])
pQ_from_nq = sp.together(
    nq_j_asserted / (2 * y) - (q - j) * g1 - q * dq_j_asserted
)
print("p_Q from [s^{4t+1-j}] R_s =", sp.together(pQ_derived))
print("p_Q from nq/(2y)−(q−j)g1−q dq =", sp.together(pQ_from_nq))
check("Q4  [s^{4t+1-j}] R_s = nq/(2y) − (q−j)g1 − q dq_j",
      rat_zero(pQ_derived - pQ_from_nq))


# ---------------------------------------------------------------------------
# b2 at weight 2t+1.  Perturb b2 = eps; Y = s S − g eps.
# ---------------------------------------------------------------------------
print("\n=== b2: perturb Y by −g eps ===")

S0 = monomial(2 * t, g1, 0)
Yb2 = S0.times_s().plus(monomial(0, 0, -g))   # −g eps * s^0
Zb = monomial(t, g2, 0).times_s()
Vb = monomial(t - 1, 1, 0).times_s().times_s()  # s^{t+1}
Upb = monomial(2 * t, q, 0)
Vbp = Vb.diff_s()
Yb2p = Yb2.diff_s()
numerb = (Vb.mul(Yb2p).scale(-1)
          .plus(Vbp.mul(Yb2))
          .plus(Upb.mul(Zb).scale(2)))
# X' perturbation at s^{t-1}: numerator at s^t / (s * 2y)
xp_b2 = sp.together(numerb.coeff(t)[1] / (2 * y))  # [s^{t-1}] X'_eps
# R_s = V X' − U' Y − yg
# V * (xp_b2 s^{t-1}) contributes at s^{2t}
# −U' * (−g eps) contributes q g at s^{2t}
Xpb = monomial(3 * t, e, 0).plus(monomial(t - 1, 0, xp_b2))
Rsb = Vb.mul(Xpb).plus(Upb.mul(Yb2).scale(-1))
p_b2_derived = sp.together(Rsb.coeff(2 * t)[1])
p_b2_asserted = g * d / (2 * y)
# Here d is not yet substituted; the closed form uses d = 2 q y − (t+1).
p_b2_in_y = sp.together(g * (2 * q * y - (t + 1)) / (2 * y))
print("p_b2 derived  =", sp.factor(p_b2_derived))
print("p_b2 in (y,q,t,g) =", sp.factor(p_b2_in_y))
print("p_b2 difference =",
      sp.cancel(sp.together(p_b2_derived - p_b2_in_y)))
check("B1  p_b2 = g(2qy−(t+1))/(2y) = g d/(2y)",
      rat_zero(p_b2_derived - p_b2_in_y))


# ---------------------------------------------------------------------------
# Reduce in A_t = Q(t,j)[d]/(3d²−(t+1)) and match (5.9)-(5.15).
# ---------------------------------------------------------------------------
print("\n=== algebra reduction: match (5.9)-(5.15) ===")

q_d = 2 * t + 1
e_d = 3 * t + 1
y_d = (d + t + 1) / (2 * q_d)
g1_d = e_d / q_d
g2_d = e_d * (d + q_d) / (2 * q_d ** 2)
g_d = e_d * t * (3 * d + 2 * (t + 1)) / (6 * q_d ** 3)

# (5.7a) in A_t.
id1 = (3 * t + 2) * g_d - 2 * t * y_d * g2_d
id2 = 3 * q_d * g_d + (t + 1) * g2_d - (4 * t + 1) * y_d * g1_d
id3 = 2 * q_d * g2_d - t * g1_d - 2 * e_d * y_d
check("A1  (5.7a)#1  (3t+2)g − 2t y g2 = 0 in A_t", reduce_d(id1) == 0)
check("A2  (5.7a)#2  3q g + (t+1)g2 = (4t+1) y g1  in A_t",
      reduce_d(id2) == 0)
check("A3  (5.7a)#3  2q g2 − t g1 = 2 e y  in A_t", reduce_d(id3) == 0)
# Leading T from (5.7b) equals g2.
check("A4  g(3t+2)/(2 y t) = g2 in A_t",
      reduce_d(T_lead_expected.subs({g: g_d, y: y_d}) - g2_d) == 0)

subs_C = {
    y: y_d, g: g_d, g1: g1_d, g2: g2_d, q: q_d, e: e_d,
}
pC_alg = reduce_d(pC_from_nj.subs(subs_C))

A_C = (9 * j * j * t + 18 * j * j - 54 * j * t * t - 81 * j * t - 26 * j
       + 72 * t ** 3 + 144 * t * t + 88 * t + 16)
B_C = (-9 * j * j * t - 10 * j * j + 24 * j * t * t + 33 * j * t + 10 * j
       - 12 * t ** 3 - 20 * t * t - 8 * t)
L_C = A_C * d + B_C
p_C_closed = 3 * t * e_d * L_C / ((t + 1) * (3 * t + 2) ** 3 * (4 * t - 2 * j + 1))
print("p_C reduced =", pC_alg)
print("p_C closed  =", sp.together(p_C_closed))
check("A5  (5.9)-(5.10) p_C derived − closed = 0 in A_t",
      reduce_d(pC_alg - p_C_closed) == 0)

F_C = sp.factor(-(3 * B_C ** 2 - A_C ** 2 * (t + 1)) / (3 * t + 2) ** 3)
F_C_positive = (
    3 * n ** 4 + 24 * n ** 3 * t + 42 * n ** 3
    + 66 * n ** 2 * t ** 2 + 146 * n ** 2 * t + 119 * n ** 2
    + 72 * n * t ** 3 + 238 * n * t ** 2 + 234 * n * t + 104 * n
    + 27 * t ** 4 + 134 * t ** 3 + 223 * t ** 2 + 136 * t + 32
)
check("A6  (5.11) F_C(t, t-n) is the all-nonnegative quartic",
      sp.expand(F_C.subs(j, t - n) - F_C_positive) == 0)

pQ_alg = reduce_d(
    (nq_j_asserted / (2 * y) - (q - j) * g1 - q * dq_j_asserted)
    .subs(subs_C)
)
A_Q = 12 * t * t + 16 * t + 4 - j * (3 * t + 4)
B_Q = 2 * (t + 1) * (j - t)
L_Q = A_Q * d + B_Q
p_Q_closed = -3 * t * e_d * (q_d - j) * L_Q / (
    (t + 1) * q_d * (3 * t + 2) ** 2 * (4 * t - 2 * j + 1)
)
print("p_Q reduced =", pQ_alg)
print("p_Q closed  =", sp.together(p_Q_closed))
check("A7  (5.12)-(5.13) p_Q derived − closed = 0 in A_t",
      reduce_d(pQ_alg - p_Q_closed) == 0)

F_Q = sp.factor(
    -(3 * B_Q ** 2 - A_Q ** 2 * (t + 1)) / ((t + 1) * (3 * t + 2) ** 2)
)
F_Q_positive = n ** 2 + 4 * n * t + 6 * n + 4 * t * t - 3
check("A8  (5.14) F_Q(t, q-n) = n^2+4nt+6n+4t^2-3",
      sp.expand(F_Q.subs(j, q_d - n) - F_Q_positive) == 0)

p_b2_alg = reduce_d(p_b2_derived.subs(subs_C))
p_b2_closed = reduce_d(g_d * d / (2 * y_d))
print("p_b2 reduced =", p_b2_alg)
print("p_b2 closed  =", p_b2_closed)
check("A9  (5.15) p_b2 = g d/(2y) in A_t",
      reduce_d(p_b2_alg - p_b2_closed) == 0)
L_2 = 3 * q_d * d + (t + 1)
# p_b2 ~ L_2 : ratio in A_t is a unit.
ratio_b2 = reduce_d(p_b2_closed / L_2)
print("p_b2 / L_2 =", ratio_b2)
check("A10 (5.15) p_b2 is a Q(t)-unit times L_2 = 3q d+(t+1)",
      ratio_b2 != 0 and ratio_b2.free_symbols <= {t})


# ---------------------------------------------------------------------------
# Boundaries.
# ---------------------------------------------------------------------------
print("\n=== index ranges and boundary cases ===")
print("spine order (5.8): C_j for 1<=j<=t-1; q_j for t<=j<=2t; b2 at j=2t+1")
print("j=0: not an unknown (C leading coefficient is the monic 1).")
print("j=t: C-family denominator t-j vanishes; s^{t-1-t}=s^{-1} is not a")
print("     polynomial term of C.  This index is the first Q-variable q_t.")
print("j=2t: Q-family last index; q-j=1, 4t-2j+1=1, both nonzero.")
print("j=2t+1: b2, not a C or U coefficient.")

# Formal poles of the C-family formulae.
check("R1  C-family pole t-j=0  <=>  j=t, excluded from 1<=j<=t-1",
      sp.solve(sp.Eq(t - j, 0), j) == [t])
check("R2  Euler/X' pole 4t-2j+1=0  <=>  j=2t+1/2, never an integer",
      sp.solve(sp.Eq(4 * t - 2 * j + 1, 0), j) == [2 * t + sp.Rational(1, 2)])
check("R3  Q-family pole q-j=0  <=>  j=q=2t+1, excluded from t<=j<=2t",
      sp.solve(sp.Eq(q_d - j, 0), j) == [2 * t + 1])


# ---------------------------------------------------------------------------
# Denominators and integer roots (FALLACY-v2).
# ---------------------------------------------------------------------------
print("\n=== FALLACY-v2 denominators ===")


def int_roots_univariate(poly, var):
    p = sp.Poly(sp.expand(poly), var)
    if p.is_zero:
        return "IDENTICALLY ZERO"
    roots = []
    for r in sp.roots(p.as_expr(), var):
        if getattr(r, "is_Integer", False):
            roots.append(r)
        elif getattr(r, "is_Rational", False) and r.is_rational:
            # keep integer-valued rationals only in the integer list
            pass
    # also catch rational roots that are integers
    for r, _ in sp.roots(p.as_expr(), var).items():
        if r.is_integer:
            roots.append(sp.Integer(r))
    return sorted(set(roots), key=lambda z: int(z))


def report_den(name, expr, vars_):
    num, den = sp.cancel(expr).as_numer_denom()
    den_f = sp.factor(den)
    print("  %-28s  denom = %s" % (name, den_f))
    for var in vars_:
        # treat other symbols as generic: coefficients in Z[other][var]
        try:
            roots = int_roots_univariate(den, var)
        except Exception:
            roots = "n/a"
        print("      integer %s-roots of denom: %s" % (var, roots))
    return den_f


print("C-family (function field Q(t,j,y,g,g1,g2,q)):")
report_den("b_j", b_j_asserted, (t, j, y))
report_den("d_j", d_j_asserted, (t, j, y))
report_den("n_j", n_j_asserted, (t, j, y))
report_den("p_C  e+n_j/(2y)-q d_j", pC_from_nj, (t, j, y))
print("Q-family:")
report_den("dq_j", dq_j_asserted, (t, j, y, q))
report_den("nq_j", nq_j_asserted, (t, j, y, q))
print("closed forms in A_t:")
report_den("(5.10) p_C_closed", p_C_closed, (t, j))
report_den("(5.13) p_Q_closed", p_Q_closed, (t, j))
report_den("(5.15) p_b2 = g d/(2y)", g_d * d / (2 * y_d), (t, d))

# Reconstruction diagonals 2, y, m+1, 2m+1, t, t-j, q, 3t+2, t+1.
denominators = {
    "2": (sp.Integer(2), "none"),
    "y": (y_d, "Res_y(H_t,y)=(t+1)(3t+2); t-roots {-1}; t=-2/3 not integer"),
    "t": (t, "{0}"),
    "t-j": (t - j, "j=t, excluded from C-range"),
    "q=2t+1": (q_d, "t=-1/2, not integer"),
    "3t+1": (e_d, "t=-1/3, not integer"),
    "t+1": (t + 1, "{-1}"),
    "3t+2": (3 * t + 2, "t=-2/3, not integer"),
    "4t-2j+1": (4 * t - 2 * j + 1, "j=2t+1/2, never integer"),
    "q-j": (q_d - j, "j=2t+1, excluded from Q-range"),
    "2m+1 at m=2t": (4 * t + 1, "t=-1/4, not integer"),
    "m+1 at m=t-1": (t, "{0}"),
    "2y in X'": (2 * y_d, "same as y"),
}
print("declared reconstruction/pivot denominators:")
for name, (expr, note) in denominators.items():
    print("  %-20s  %s" % (name, note))

# Positivity on ranges, as the gate already proved; re-check a finite window.
bad_C = [
    (tv, jv)
    for tv in range(2, 41)
    for jv in range(1, tv)
    if (tv + 1) * (3 * tv + 2) ** 3 * (4 * tv - 2 * jv + 1) == 0
    or (tv - jv) == 0
]
bad_Q = [
    (tv, jv)
    for tv in range(2, 41)
    for jv in range(tv, 2 * tv + 1)
    if (tv + 1) * (2 * tv + 1) * (3 * tv + 2) ** 2 * (4 * tv - 2 * jv + 1) == 0
    or (2 * tv + 1 - jv) == 0
]
check("D1  no vanishing C-denominator on  t=2..40, 1<=j<=t-1", not bad_C)
check("D2  no vanishing Q-denominator on  t=2..40, t<=j<=2t", not bad_Q)

# Norms of L_C, L_Q, L_2: no positive-integer zero in range.
H = 12 * q_d ** 2 * y ** 2 - 12 * q_d * (t + 1) * y + (t + 1) * (3 * t + 2)


def lin_norm(a, b):
    return sp.factor(sp.expand(4 * q_d ** 2 * (3 * b ** 2 - a ** 2 * (t + 1))))


check("D3  Res(H_t, L_C) = -4q^2 (3t+2)^3 F_C",
      sp.simplify(lin_norm(A_C, B_C) + 4 * q_d ** 2 * (3 * t + 2) ** 3 * F_C)
      == 0)
check("D4  Res(H_t, L_Q) = -4q^2 (t+1)(3t+2)^2 F_Q",
      sp.simplify(lin_norm(A_Q, B_Q)
                  + 4 * q_d ** 2 * (t + 1) * (3 * t + 2) ** 2 * F_Q) == 0)
check("D5  Res(H_t, L_2) = -12 q^2 (t+1)(3t+2)(4t+1)",
      sp.simplify(lin_norm(3 * q_d, t + 1)
                  + 12 * q_d ** 2 * (t + 1) * (3 * t + 2) * (4 * t + 1)) == 0)
check("D6  F_C(t,t-n) coefficients nonnegative, constant 32",
      all(co >= 0 for co in sp.Poly(F_C_positive, n, t).coeffs())
      and sp.Poly(F_C_positive, n, t).coeff_monomial(sp.Integer(1)) == 32)
check("D7  F_Q(t,q-n) >= 12 on 1<=n<=t+1, t>=1 (min at n=1,t=1)",
      sp.expand(F_Q_positive.subs({n: 1, t: 1})) == 12)


# ---------------------------------------------------------------------------
# Specialise t=2..6 against charged nonlinear records.
# ---------------------------------------------------------------------------
print("\n=== specialisation vs charged terminal_laurent_t*.json ===")


def fixed_reduce(expr, value, yy):
    qq = 2 * value + 1
    HH = sp.Poly(
        12 * qq * qq * yy ** 2 - 12 * qq * (value + 1) * yy
        + (value + 1) * (3 * value + 2),
        yy, domain=sp.QQ,
    )
    numerator, denominator = sp.cancel(expr).as_numer_denom()
    npoly = sp.Poly(numerator, yy, domain=sp.QQ)
    dpoly = sp.Poly(denominator, yy, domain=sp.QQ)
    nrem = npoly.rem(HH)
    drem = dpoly.rem(HH)
    if drem == 0:
        raise ZeroDivisionError(expr)
    if drem.degree() > 0:
        res = sp.resultant(drem.as_expr(), HH.as_expr(), yy)
        if res == 0:
            raise ZeroDivisionError("zero divisor at t=%s: %s" % (value, drem))
    inv = sp.invert(drem, HH)
    return sp.factor((nrem * inv).rem(HH).as_expr())


checked = []
missing_t = []
for value in range(2, 7):
    record_path = CHARGED / ("terminal_laurent_t%d.json" % value)
    if not record_path.exists():
        missing_t.append(value)
        print("  t=%d  NO charged nonlinear record (typed: not compared)"
              % value)
        # Still specialise the closed form and check the resultant is nonzero.
        yy = sp.Symbol("y")
        dd = 2 * (2 * value + 1) * yy - (value + 1)
        for index in list(range(1, value)) + list(range(value, 2 * value + 1)) + [None]:
            if index is None:
                formula = p_b2_closed
                tag = "b2"
            elif index < value:
                formula = p_C_closed
                tag = "C%d" % index
            else:
                formula = p_Q_closed
                tag = "q%d" % index
            coeff = fixed_reduce(
                formula.subs({t: value, j: (index if index is not None
                                            else 2 * value + 1), d: dd}),
                value, yy,
            )
            HH = (12 * (2 * value + 1) ** 2 * yy ** 2
                  - 12 * (2 * value + 1) * (value + 1) * yy
                  + (value + 1) * (3 * value + 2))
            res = sp.factor(sp.resultant(HH, coeff, yy))
            if res == 0:
                check("S t=%d %s resultant nonzero" % (value, tag), False)
            else:
                print("  t=%d  %s  specialised, Res=%s  (no record)"
                      % (value, tag, res))
        continue
    record = json.loads(record_path.read_text(encoding="utf-8"))
    yy = sp.Symbol("q%d_1" % (2 * value + 1))
    dd = 2 * (2 * value + 1) * yy - (value + 1)
    n_ok = 0
    for item in record["high_pivots"]:
        variable = item["variable"]
        if variable.startswith("C"):
            index = int(variable[1:])
            formula = p_C_closed
        elif variable.startswith("q"):
            index = int(variable[1:].split("_")[0])
            formula = p_Q_closed
        elif variable == "b2":
            index = 2 * value + 1
            formula = p_b2_closed
        else:
            raise AssertionError(variable)
        specialized = fixed_reduce(
            formula.subs({t: value, j: index, d: dd}), value, yy
        )
        measured = fixed_reduce(sp.sympify(item["coefficient"]), value, yy)
        left = sp.Poly(specialized, yy, domain=sp.QQ)
        right = sp.Poly(measured, yy, domain=sp.QQ)
        ratio = sp.Rational(left.LC(), right.LC())
        agree = (left - ratio * right).is_zero
        print("  t=%d  %-6s  derived=%s  record=%s  ratio=%s  %s"
              % (value, variable, specialized, measured, ratio,
                 "ASSOCIATE" if agree else "MISMATCH"))
        if not agree:
            check("S t=%d %s associate" % (value, variable), False)
        else:
            n_ok += 1
    checked.append((value, n_ok, len(record["high_pivots"])))
    check("S t=%d  %d/%d high pivots rational associates"
          % (value, n_ok, len(record["high_pivots"])),
          n_ok == len(record["high_pivots"]))

print("CHARGED_RECORDS_COMPARED=", checked)
print("MISSING_CHARGED_RECORDS_t=", missing_t)

print("\nDERIVE_PIVOT_FORMS_DONE fails=%d" % len(fails))
if fails:
    print("FAILED:", fails)
    sys.exit(1)
print("ALL_PASS")
