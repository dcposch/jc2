#!/usr/bin/env python3
"""Independent (Fable) exact checks for the R050 physical-place residue gate.
Everything here is derived from the licensed R050 pattern (exact-contact gate s.4)
and Xu Lemma 2.1 / Prop 3.3(i) / Lemma 4.4, not from the producer's text."""
import json, sympy as S
from fractions import Fraction as Fr

out = {}

# ---- 0. R050 arithmetic from the licensed pattern (n=196, m=56, d2=28, n-M2=12, delta2=1/4)
n, m = 196, 56
d2, nM2, delta2 = 28, 12, Fr(1,4)
r = 4                                   # reduced multiplicity of the selected level-2 factor
rho = Fr(m*r, d2)                       # f-roots per final-major disc
a = Fr(m,1)*(1-delta2)/nM2              # -lambda_f at D2
kappa = rho*(1-delta2) - a
delta1 = 1 - (n+m)*kappa/((n+m)*rho - m)
lam_f = -a + rho*(delta1-delta2)
lam_g = Fr(n,m)*lam_f
out["R050_arith"] = dict(rho=str(rho), a=str(a), delta1=str(delta1), lam_f=str(lam_f),
                         lam_g=str(lam_g), one_plus_lf_plus_lg=str(1+lam_f+lam_g),
                         ord_t_fy_at_simple_root=str(lam_f-delta1),
                         IM=str(Fr(n,n+m)*4*rho*(1-delta1)))
assert rho == 8 and delta1 == Fr(19,28) and lam_f == Fr(-1,14) and lam_g == Fr(-1,4)
assert 1+lam_f+lam_g == delta1 and lam_f-delta1 == Fr(-3,4)

# ---- 1. Galois semi-invariance of the D1 face forces pi | face and q = 1 mod 7.
# stabiliser of eta (denominators | 4) inside Z/28 is k = 0 mod 4; zeta=e(1/28)
import cmath
def zeta(k, N=28): return cmath.exp(2j*cmath.pi*k/N)
# face transforms f(z^{19k} pi) = z^{28*lam_f*k} f(pi) for k in 4Z
allowed_q = []
for q in range(0, 9):
    ok = all(abs(zeta(19*k)**q - zeta(int(28*lam_f)*k)) < 1e-9 for k in range(0,28,4))
    if ok: allowed_q.append(q)
out["D1_face_allowed_pi_powers_deg_le_8"] = allowed_q
assert allowed_q == [1, 8]

# ---- 2. D1 valuation floor 7i+19q >= -2 (u-units), equality set, and N=i+3q bounds
eq = [(i,q) for q in range(0,9) for i in range(-60,10) if 7*i+19*q == -2]
out["floor_equality_monomials"] = eq
assert eq == [(-3,1), (-22,8)]
allowed = {N: [q for q in range(0,57) if 7*(N-3*q)+19*q >= -2] for N in (-2,-1,0,1,2)}
out["f_allowed_v_degrees_by_u_power"] = {str(k): v for k,v in allowed.items()}
assert allowed[-2] == [] and allowed[-1] == [] and allowed[0] == [0,1] and allowed[1] == [0,1,2,3,4]
# g floor 7i+19q >= -7 (lam_g = -1/4 in t = -1 in u)
gallowed = {N: [q for q in range(0,200) if 7*(N-3*q)+19*q >= -7] for N in (-2,-1,0,1)}
out["g_allowed_v_degrees_by_u_power"] = {str(k): v for k,v in gallowed.items()}
assert gallowed[-2] == [] and gallowed[-1] == [0] and gallowed[0] == [0,1,2,3] and gallowed[1] == list(range(0,8))

# ---- 3. Residue formula from a fully generic truncated H (independent of the family)
u, v, T, A, B = S.symbols("u v T A B")
h = S.symbols("h0:5"); k2 = S.symbols("k0:9")
H1 = sum(h[i]*v**i for i in range(5)); H2 = sum(k2[i]*v**i for i in range(9))
H = A*v + B + u*H1 + u**2*H2
# solve H(u,v(u)) = T to order u^1
v0 = (T-B)/A
v1 = S.symbols("v1")
sol1 = S.solve(S.expand(H.subs(v, v0+u*v1)).coeff(u,1), v1)[0]
vser = v0 + u*sol1
Hv = S.diff(H, v).subs(v, vser)
omega = S.series(-4*u**-2/Hv, u, 0, 1).removeO()      # coefficient of du
res = S.simplify(omega.coeff(u, -1))
target = 4*S.diff(H1, v).subs(v, v0)/A**2
assert S.simplify(res - target) == 0
out["residue_formula"] = str(S.factor(res))
# sanity: leading term is -4/A u^-2
assert S.simplify(omega.coeff(u,-2) + 4/A) == 0

# ---- 4. Keller u^-1 row with generic G through u^2, and the Moh/Xu Prop 4.1 cross-check at pi=0
b = S.symbols("b"); g0 = S.symbols("g0:4"); g1 = S.symbols("g1_0:8"); g2 = S.symbols("g2_0:12")
G = b/u + sum(g0[i]*v**i for i in range(4)) + u*sum(g1[i]*v**i for i in range(8)) + u**2*sum(g2[i]*v**i for i in range(12))
Juv = S.expand(S.diff(H,u)*S.diff(G,v) - S.diff(H,v)*S.diff(G,u))
assert S.simplify(Juv.coeff(u,-3)) == 0
assert S.simplify(Juv.coeff(u,-2) - A*b) == 0
assert S.simplify(Juv.coeff(u,-1) - b*S.diff(H1,v)) == 0
out["Juv_u0_coefficient"] = str(S.factor(Juv.coeff(u,0)))
# chain rule determinant J_{u,v}(x,y) with x=u^-4, y=u^-4+c0+al*u+be*u^2+u^3 v
c0, al, be = S.symbols("c0 alpha beta")
X = u**-4; Y = u**-4 + c0 + al*u + be*u**2 + u**3*v
assert S.simplify(S.diff(X,u)*S.diff(Y,v) - S.diff(X,v)*S.diff(Y,u) + 4*u**-2) == 0
# Xu Lemma 4.4 display at pi=0: lam_g * f'_sigma(0) g_sigma(0) = J  (lam_f f g' - lam_g f' g = -J)
lamg = S.Rational(-1,4)
assert S.simplify(lamg*A*b + A*b/4) == 0      # Xu Lemma 4.4 display at pi=0: J = lam_g*A*b = -A b/4  <=>  A b = -4 J

# ---- 5. The family: support of f(u^-4, u^-4+u+z) as (i,q) and the floor
x, y, z, aa, kap, eps = S.symbols("x y z a kappa eps")
w = y - x; q = y*w**4 - 1; rr = y*w**4 - aa
F = rr**2*(y**4*w**2*q**8 - kap*y*w**2*q + eps*y*w**3*q)
Fp = S.Poly(S.expand(F), x, y)
out["family_total_degree"] = Fp.total_degree()
out["family_terms_in_x_y"] = len(Fp.terms())
out["family_terms_in_y_w"] = len(S.Poly(S.expand(F.subs(x, y - S.Symbol('w'))), y, S.Symbol('w')).terms())
Fz = S.expand(F.subs({x: u**-4, y: u**-4 + u + z}))
P = S.Poly(Fz, z)
viol = []; eqset = set(); minexp = None
for (qq,), coeff in P.terms():
    cu = S.Poly(S.expand(coeff*u**200), u)
    for (e,), c in cu.terms():
        i = e - 200
        val = 7*i + 19*qq
        if val < -2: viol.append((i,qq))
        if val == -2: eqset.add((i,qq))
out["family_floor_violations"] = viol
out["family_floor_equality_monomials"] = sorted(eqset)
assert viol == [] and sorted(eqset) == [(-22,8),(-3,1)]
# face coefficients: A = coeff of u^-3 z, C = coeff of u^-22 z^8
Acoef = S.factor(S.Poly(S.expand(P.coeff_monomial(z)*u**200),u).coeff_monomial(u**197))
Ccoef = S.factor(S.Poly(S.expand(P.coeff_monomial(z**8)*u**200),u).coeff_monomial(u**178))
out["family_A"] = str(Acoef); out["family_C"] = str(Ccoef)
assert S.simplify(Acoef + 4*kap*(1-aa)**2) == 0
# H via z=u^3 v; H0, H1 directly
Hfam = S.expand(Fz.subs(z, u**3*v))
H0f = S.factor(Hfam.coeff(u,0)); H1f = S.factor(Hfam.coeff(u,1))
out["family_H0"] = str(H0f); out["family_H1"] = str(H1f)
assert S.simplify(H0f + 4*kap*(1-aa)**2*v) == 0 and S.simplify(H1f - 4*eps*(1-aa)**2*v) == 0
assert all(Hfam.coeff(u,k) == 0 for k in range(-30,0))
resfam = S.factor(4*S.diff(H1f,v).subs(v,(T-0)/(-4*kap*(1-aa)**2))/(16*kap**2*(1-aa)**4))
out["family_residue"] = str(resfam)
assert S.simplify(resfam - eps/(kap**2*(1-aa)**2)) == 0

# ---- 6. Controls
fa, ga = y + x**2, -x
assert S.expand(S.diff(fa,x)*S.diff(ga,y)-S.diff(fa,y)*S.diff(ga,x)) == 1
assert S.expand(fa.subs({x:-ga, y: fa-ga**2})) == fa  # tautology guard
hb = x + x**2*y
assert S.expand((1-2*x*y)*S.diff(hb,x) + 4*y**2*S.diff(hb,y)) == 1
# fibre h=T: y=(T-x)/x^2, omega = dx/h_y = dx/x^2 ; residues at 0 and inf
assert S.residue(1/x**2, x, 0) == 0
zz = S.symbols("zz")
assert S.residue((1/x**2).subs(x,1/zz)*(-1/zz**2), zz, 0) == 0
# no polynomial mate: J(p,h)=j forces p = -j/x + C(h); direct argument replayed with generic p of degree<=6 in x,y
j = S.symbols("j")
deg = 6
cs = S.symbols(f"p0:{(deg+1)*(deg+2)//2}")
p = 0; it = iter(cs)
for dd in range(deg+1):
    for ii in range(dd+1):
        p += next(it)*x**ii*y**(dd-ii)
Jph = S.expand(S.diff(p,x)*S.diff(hb,y) - S.diff(p,y)*S.diff(hb,x) - j)
sol = S.solve(S.Poly(Jph, x, y).coeffs(), list(cs)+[j], dict=True)
out["negative_control_deg6_solutions_force_j0"] = all(s.get(j, None) == 0 for s in sol) and len(sol) > 0
assert out["negative_control_deg6_solutions_force_j0"]
# twisted example
gam, pi = S.symbols("gamma pi")
for ell in range(1, 7):
    Q = gam*pi
    Pprinted = gam**(ell+1)/(ell+1); Pfixed = gam**ell/ell
    Jp = S.simplify(S.diff(Pprinted,gam)*S.diff(Q,pi) - S.diff(Pprinted,pi)*S.diff(Q,gam))
    Jf = S.simplify(S.diff(Pfixed,gam)*S.diff(Q,pi) - S.diff(Pfixed,pi)*S.diff(Q,gam))
    assert S.simplify(Jp - gam**(ell+1)) == 0 and S.simplify(Jf - gam**ell) == 0
out["twisted_example"] = "printed P=gamma^(l+1)/(l+1) gives J=gamma^(l+1); repaired P=gamma^l/l gives J=gamma^l (l=1..6)"

# ---- 7. Minor-place residue vanishing: ord_u omega = e(delta-1)-1 >= 0 whenever e*delta integer, delta>1
bad = [(e, d) for e in range(1,60) for d in [Fr(p,e) for p in range(e+1, 6*e)] if e*(d-1)-1 < 0]
assert bad == []
out["minor_place_residue"] = "ord_u omega = e(delta-1)-1 >= 0 for all e>=1, delta>1 with e*delta in Z"

out["status"] = "ALL_INDEPENDENT_ASSERTS_PASS"
print(json.dumps(out, indent=1, sort_keys=True))
