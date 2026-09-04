#!/usr/bin/env python3
"""Eagon-Northcott Hilbert numerator of P_t/I_2(N) for the (t-1)x2 matrix N=(C_r,B_r),
wt C_r=2t+2+r, wt B_r=t+1+r, i.e. phi: (+)_r P(-(2t+2+r)) -> P(0)(+)P(-(t+1)),
valid when I_2(N) has the generic grade t-2 (then P_t/I_2(N) is CM of dim 1).
Weighted degree d_Gamma(t) := lim_{s->1} (1-s) Hilb = number of weighted-projective
points of the rank-1 curve counted with multiplicity and 1/gcd(weights) convention.
Compared with the closed form [binom(3t+1,t-1)-binom(2t,t-1)]/(t+1) (LENGTH-SPLIT)."""
import sympy as sp, itertools, sys
s = sp.symbols('s')
def HN(t):
    n = t-1; delta = {r: 2*t+2+r for r in range(1, t)}
    expr = sp.Integer(1)
    for k in range(0, n-1):
        for R in itertools.combinations(range(1, t), k+2):
            base = sum(delta[r] for r in R)
            for j in range(0, k+1):
                expr += (-1)**(k+1) * s**(base - (j+1)*(t+1))
    return sp.expand(expr)
def wdeg(t):
    hn = HN(t)
    ser = sp.series(hn.subs(s, 1-sp.Symbol('e')), sp.Symbol('e'), 0, t).removeO()
    e = sp.Symbol('e')
    coeffs = [ser.coeff(e, i) for i in range(t)]
    assert all(c == 0 for c in coeffs[:t-2]), coeffs
    return sp.Rational(coeffs[t-2], sp.factorial(t-1)), hn
for t in range(3, 13):
    d, hn = wdeg(t)
    closed = sp.Rational(sp.binomial(3*t+1, t-1) - sp.binomial(2*t, t-1), t+1)
    print(f"t={t}: d_Gamma(EN)={d}  closed=[C(3t+1,t-1)-C(2t,t-1)]/(t+1)={closed}  match={d==closed}  HN_deg={sp.degree(hn,s)} nterms={len(hn.as_ordered_terms())}")
    if t <= 5: print("   HN =", hn)

# ---- closed form of the EN numerator (derived by the e_m generating-function identity) ----
def HN_closed(t):
    num = sp.prod([1 - s**(2*t+2+r) for r in range(1, t)]) - s**(t+1) * sp.prod([1 - s**(t+1+r) for r in range(1, t)])
    q, rem = sp.div(sp.Poly(sp.expand(num), s), sp.Poly(1 - s**(t+1), s))
    assert rem.is_zero, ("division not exact", t)
    return sp.expand(q.as_expr())
if __name__ == '__main__' and len(sys.argv) > 1 and sys.argv[1] == 'closed':
    for t in range(3, 16):
        print(f"t={t}: HN_EN - HN_closed = {sp.expand(HN(t) - HN_closed(t))}")
