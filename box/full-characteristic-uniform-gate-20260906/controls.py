#!/usr/bin/env python3
"""Desk controls for the uniform full-characteristic Keller criterion gate.
Exact integer / sympy checks only; no Groebner, no fleet.
J(F,G) := F_x*G_y - F_y*G_x throughout."""
from sympy import symbols, diff, expand, factor, Poly
from math import gcd as g
x, y = symbols('x y')
def J(F, G): return expand(diff(F, x)*diff(G, y) - diff(F, y)*diff(G, x))

def charchain(n, Ms):
    """Moh p150 arithmetic. Returns d, q, Lambda, D=-mu, gcd(n,D_1..D_i) chain.
    Asserts: strict gcd drop (M_i not divisible by d_i), the p154 identity
    Lambda_i = sum_{j<i}(d_j-d_{j+1})M_j + d_i M_i, D_i = -M_i mod d_i,
    gcd(n,D_1..D_i) = d_{i+1}, and D_{i+1} = n_i D_i + M_i - M_{i+1}."""
    d = [n]; q = []; lam = []; D = []
    for i, M in enumerate(Ms):
        assert M % d[i] != 0, f"M_{i+1}={M} divisible by d_{i+1}={d[i]}: not a characteristic exponent"
        q.append(M if i == 0 else M - Ms[i-1])
        L = sum(q[j]*d[j] for j in range(i+1)); lam.append(L)
        assert L % d[i] == 0; D.append(-L//d[i])
        d.append(g(d[i], M))
    for i in range(len(Ms)):
        assert lam[i] == sum((d[j]-d[j+1])*Ms[j] for j in range(i)) + d[i]*Ms[i]
        assert (D[i] + Ms[i]) % d[i] == 0
    G = [n]
    for i in range(len(Ms)):
        G.append(g(G[-1], D[i])); assert G[-1] == d[i+1]
    nvec = [d[i]//d[i+1] for i in range(len(Ms))]
    for i in range(len(Ms)-1):
        assert D[i+1] == nvec[i]*D[i] + Ms[i] - Ms[i+1]
    return dict(d=d, n_i=nvec, q=q, Lambda=lam, D=D, gcd_chain=G,
                jac_bound=[n-M-2 for M in Ms], final_gcd=g(d[-2], 2) if Ms[-1] == n-2 else None)

print("== clients (M_s = n-2, odd d_s -> final gcd 1)")
for n, Ms in [(99, [-66, 77, 97]), (108, [-72, 81, 106])]:
    r = charchain(n, Ms); print(n, Ms, r)
    assert r['gcd_chain'][-1] == 1 and r['final_gcd'] == 1
    assert r['D'] == ([66, 55, 145] if n == 99 else [72, 63, 227])
print("== even final gcd examples (d_s even >= 4, M_s = n-2 even; d_{s+1}=2 so a terminal M=n-1 exists)")
for n, Ms in [(12, [-8, 10]), (20, [-12, 18]), (24, [-16, 22])]:
    r = charchain(n, Ms); print(n, Ms, 'd=', r['d'], 'D=', r['D'], 'gcd chain', r['gcd_chain'])
    assert r['gcd_chain'][-1] == 2 and r['final_gcd'] == 2
print("== invalid datum rejected: n=8, M=(-6,6) has d_2=2 | M_2")
try: charchain(8, [-6, 6]); print("NOT REJECTED (bug)")
except AssertionError as e: print("rejected:", e)

print("== dropped-endpoint control: G=y^2+x, F=G^2-x^3, T2=U^2-V")
G_ = y**2 + x; F_ = expand(G_**2 - x**3)
H2 = expand(G_**2 - F_)
jf = J(F_, G_); print(" J(F,G) =", factor(jf), "; J(G,F) =", factor(J(G_, F_)))
assert jf == expand(-6*x**2*y)
print(" deg F =", Poly(F_, x, y).total_degree(), " deg_y F =", Poly(F_, y).degree(),
      " deg G =", Poly(G_, x, y).total_degree(), " H2 = T2(G,F) =", H2,
      " total deg", Poly(H2, x, y).total_degree(), " y-deg", Poly(H2, y).degree())
n, D1, D2 = 4, 2, 3; M1 = -D1; n1 = 4 // g(4, 2); M2 = n1*D1 + M1 - D2
print(" n=%d n1=%d M=(%d,%d) D=(%d,%d) bound n-M2-2=%d degJ=%d" % (n, n1, M1, M2, D1, D2, n-M2-2, Poly(jf, x, y).total_degree()))
assert (M1, M2) == (-2, -1) and n - M2 - 2 == 3 == Poly(jf, x, y).total_degree()
dU = expand(2*G_); print(" (d_U T2)(G,F) = 2G, deg", Poly(dU, x, y).total_degree(), "= D2+M2 =", D2+M2)
assert expand(J(F_, H2) - dU*jf) == 0; print(" chain rule J(F,T2(G,F)) = (d_U T2)(G,F)*J(F,G) OK")
print(" NOTE: y not in k(x,F,G) here (G^2-F=x^3 is quadratic in G); this is an abstract-theorem control only")

print("== zero-exclusion control: F=(xy)^2, G=xy (gcd 2, equal top multiplicities)")
F0 = (x*y)**2; G0 = x*y; print(" J =", J(F0, G0), " gcd(deg F,deg G) =", g(4, 2), " top of F = x^2 y^2 (multiplicities 2,2 equal)")
assert J(F0, G0) == 0
print("ALL CONTROLS PASSED")
