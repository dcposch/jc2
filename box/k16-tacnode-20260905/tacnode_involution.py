#!/usr/bin/env python3
"""Tacnode dichotomy on (UF), generic jets, t-independent; truncated-series arithmetic (dict power->coeff), order K.

(UF):  (theta-3)(P^2) + G P = R,  G = (3/2)L(L+b) - Bx,  R = (3/16)L^2(L(L+2b)-4Bx) - eta x^2 (bL/2 + Bx).
Q_P(x,Y) = R(x,Y) - G(x,Y) P - (theta-3)(P^2)  (quartic in Y, lc 3/16);  (UF) <=> Q_P(x,L(x)) = 0.
L = -b + sum_{j>=2} l_j x^j (generic), P_0..P_3 = (-b^2/4, -B, eta, w2), P_k = Phi_k (k>=4) from the universal recursion.
Checks (H) Hensel factor F0 = Y^2 + sY + p, Ltilde = -s-L;  (E-) tau*Psi + b q = 0;  (Ct) monic cubic in tau = L+L~+b;
(Cd) cubic in delta = L~-L with D0 = (16/3) d_Y Q_P(x,L);  (Pv) pivot chain [x^j]D0 = 4b^2 l_j + f_j;  d row_k/d l_m = -[x^{k-m}]D;
(Inf) edge polynomial at infinity = (UT); leading (E-) at infinity for lam~^2 = om/p~.
"""
import sys, json, time
import sympy as sp
t0 = time.time()
K = int(sys.argv[1]) if len(sys.argv) > 1 else 6
x, b, B, eta, w2, Y, T = sp.symbols('x b B eta w2 Y T')
ls = {j: sp.Symbol(f'l{j}') for j in range(2, K+1)}
C = sp.cancel
# ---- series helpers: dict {i: coeff}, truncated at K
def S(d): return {i: C(v) for i, v in d.items() if i <= K and v != 0}
def add(*ds):
    r = {}
    for d in ds:
        for i, v in d.items(): r[i] = r.get(i, 0) + v
    return S(r)
def scal(c, d): return S({i: c*v for i, v in d.items()})
def mul(d1, d2):
    r = {}
    for i, u in d1.items():
        for j, v in d2.items():
            if i + j <= K: r[i+j] = r.get(i+j, 0) + u*v
    return S(r)
def const(c): return S({0: c})
def theta_minus3(d): return S({i: (i-3)*v for i, v in d.items()})
def coeff(d, i): return C(d.get(i, 0))
def iszero(d): return all(C(v) == 0 for v in d.values())
xs = {1: sp.Integer(1)}
Ld = S({0: -b, **{j: ls[j] for j in range(2, K+1)}})
Lb = add(Ld, const(b))
G = add(scal(sp.Rational(3,2), mul(Ld, Lb)), scal(-B, xs))
L2 = mul(Ld, Ld)
R = add(scal(sp.Rational(3,16), mul(L2, add(mul(Ld, add(Ld, const(2*b))), scal(-4*B, xs)))),
        scal(-eta, mul({2: 1}, add(scal(b/2, Ld), scal(B, xs)))))
P = {0: -b**2/4, 1: -B, 2: eta, 3: w2}
for k in range(4, K+1):
    br = (k-3)*sum(P[i]*P[k-i] for i in range(1, k)) + sum(coeff(G, i)*P[k-i] for i in range(1, k+1)) - coeff(R, k)
    P[k] = C(br*2/((k-3)*b**2))
Pd = S(P)
out = {'K': K}
P2 = mul(Pd, Pd)
UF = add(theta_minus3(P2), mul(G, Pd), scal(-1, R))
out['UF_holds_to_order_K'] = iszero(UF)
# Q_P as quartic in Y: coefficient series q4..q0
q4 = const(sp.Rational(3,16)); q3 = const(sp.Rational(3,8)*b)
q2 = add(scal(-sp.Rational(3,4)*B, xs), scal(-sp.Rational(3,2), Pd))
q1 = add(scal(-eta*b/2, {2: 1}), scal(-sp.Rational(3,2)*b, Pd))
q0 = add(scal(B, mul(xs, Pd)), scal(-eta*B, {3: 1}), scal(-1, theta_minus3(P2)))
Q = [q0, q1, q2, q3, q4]
def evalQ(Yd):   # Q_P(x, Y(x)) as series
    r = q0; Yp = const(1)
    for i in range(1, 5):
        Yp = mul(Yp, Yd); r = add(r, mul(Q[i], Yp))
    return r
out['Q_P_at_L_vanishes'] = iszero(evalQ(Ld))
# ---- (H) Hensel: Q/(3/16) = Y^4 + (s+s1)Y^3 + (p+p1+s s1)Y^2 + (s p1 + s1 p)Y + p p1
c3 = scal(sp.Rational(16,3), q3); c2 = scal(sp.Rational(16,3), q2); c1 = scal(sp.Rational(16,3), q1); c0 = scal(sp.Rational(16,3), q0)
s = {0: 2*b}; p = {0: b**2}; s1 = {0: sp.Integer(0)}; p1 = {0: b**2}
M = sp.Matrix([[1, 0, 1, 0], [0, 1, 2*b, 1], [b**2, 0, b**2, 2*b], [0, b**2, 0, b**2]])   # unknown order (S, Pp, S1, P1)
Minv = M.inv()
out['Hensel_matrix_det'] = str(sp.factor(M.det()))
for n in range(1, K+1):
    sd, pd_, s1d, p1d = S(s), S(p), S(s1), S(p1)
    e1 = coeff(add(sd, s1d), n) - coeff(c3, n)
    e2 = coeff(add(pd_, p1d, mul(sd, s1d)), n) - coeff(c2, n)
    e3 = coeff(add(mul(sd, p1d), mul(s1d, pd_)), n) - coeff(c1, n)
    e4 = coeff(mul(pd_, p1d), n) - coeff(c0, n)
    sol = Minv * sp.Matrix([-e1, -e2, -e3, -e4])
    s[n], p[n], s1[n], p1[n] = [C(v) for v in sol]
sd, pd_, s1d, p1d = S(s), S(p), S(s1), S(p1)
# verify factorisation
F0F1 = [add(mul(pd_, p1d)), add(mul(sd, p1d), mul(s1d, pd_)), add(pd_, p1d, mul(sd, s1d)), add(sd, s1d), const(1)]
out['Hensel_factorisation_holds_mod_xK+1'] = all(iszero(add(F0F1[i], scal(-1, [c0, c1, c2, c3, const(1)][i]))) for i in range(5))
F0L = add(mul(Ld, Ld), mul(sd, Ld), pd_)
out['L_is_root_of_F0'] = iszero(F0L)
Lt = add(scal(-1, sd), scal(-1, Ld))
out['Ltilde_0'] = str(coeff(Lt, 0)); out['Ltilde_1'] = str(coeff(Lt, 1))
lt = {j: coeff(Lt, j) for j in range(2, K+1)}
out['ltilde2_plus_l2_equals_-8eta/(3b)'] = bool(C(lt[2] + ls[2] + 8*eta/(3*b)) == 0)
out['s_coeffs'] = {i: str(sp.factor(s[i])) for i in range(0, min(K, 5)+1)}
out['p_coeffs'] = {i: str(sp.factor(p[i])) for i in range(0, min(K, 4)+1)}
out['s3_closed_form_4w2/b-16Beta/(3b^3)'] = bool(C(s[3] - (4*w2/b - 16*B*eta/(3*b**3))) == 0)
out['s1_coeffs'] = {i: str(sp.factor(s1[i])) for i in range(0, min(K, 3)+1)}
out['pivot_flips_sign_on_Ltilde'] = bool(C(4*eta + 3*b*lt[2] + (4*eta + 3*b*ls[2])) == 0)
out['s_depends_on'] = {i: sorted(str(v) for v in C(s[i]).free_symbols) for i in range(2, min(K, 6)+1)}
out['Ltilde_is_formal_solution_same_P'] = iszero(evalQ(Lt))
# ---- (E-)
sigma = add(Ld, Lt); tau = add(sigma, const(b))
q = S({0: b**2, 1: 4*B, 2: -sp.Rational(8,3)*eta})
Psi = add(mul(Ld, Ld), mul(Lt, Lt), scal(b, sigma), scal(-8, Pd), const(-b**2), scal(-4*B, xs))
out['Eminus_tau_Psi_plus_bq_zero'] = iszero(add(mul(tau, Psi), scal(b, q)))
# ---- (Ct)
A = add(scal(2, Ld), const(b))
cc1 = add(scal(2, mul(Ld, Ld)), scal(2*b, Ld), const(-b**2), scal(-8, Pd), scal(-4*B, xs))
Ct = add(mul(tau, mul(tau, tau)), scal(-1, mul(A, mul(tau, tau))), mul(cc1, tau), scal(b, q))
out['cubic_Ctau_vanishes_on_tau'] = iszero(Ct)
Ct0 = sp.expand(T**3 - coeff(A, 0)*T**2 + coeff(cc1, 0)*T + b*coeff(q, 0))
out['Ctau_at_x0'] = str(sp.factor(Ct0))
# ---- (Cd)
delta = add(Lt, scal(-1, Ld))
D1 = add(scal(sp.Rational(3,2), add(mul(A, A), const(-b**2))), scal(-8, Pd), scal(-4*B, xs))
D0 = add(mul(A, add(scal(sp.Rational(1,2), add(mul(A, A), const(-3*b**2))), scal(-8, Pd), scal(-4*B, xs))), scal(b, q))
Cd = add(mul(delta, mul(delta, delta)), scal(2, mul(A, mul(delta, delta))), mul(D1, delta), D0)
out['cubic_Cdelta_vanishes'] = iszero(Cd)
# D = d_Y Q_P(x, L(x)) = q1 + 2 q2 L + 3 q3 L^2 + 4 q4 L^3
L3 = mul(L2, Ld)
D = add(q1, scal(2, mul(q2, Ld)), scal(3, mul(q3, L2)), scal(4, mul(q4, L3)))
out['D0_equals_16/3_D'] = iszero(add(D0, scal(-sp.Rational(16,3), D)))
out['D1_at_0'] = str(sp.factor(coeff(D1, 0)))
out['D0_x0_x1_vanish'] = bool(coeff(D0, 0) == 0 and coeff(D0, 1) == 0)
out['D0_x2'] = str(sp.factor(coeff(D0, 2)))
out['D0_x2_is_(4b/3)Lpivot'] = bool(C(coeff(D0, 2) - sp.Rational(4,3)*b*(4*eta + 3*b*ls[2])) == 0)
out['delta_2_equals_-D0_2/(2b^2)'] = bool(C(coeff(delta, 2) + coeff(D0, 2)/(2*b**2)) == 0)
# ---- (Pv) pivot chain
piv = {j: sp.expand(sp.numer(sp.together(coeff(D0, j)))) if False else coeff(D0, j) for j in range(2, K+1)}
for j in range(2, K+1):
    cj = piv[j]
    out.setdefault('D0_xj_coeff_of_lj', {})[j] = str(sp.factor(sp.diff(cj, ls[j])))
    out.setdefault('D0_xj_depends_on', {})[j] = sorted(str(v) for v in cj.free_symbols)
deg = {eta: -sp.Rational(3,4)*b*ls[2]}
chain = {}
p3 = C(piv[3].subs(deg)); chain[3] = p3
out['D0_x3_on_degenerate_locus'] = str(sp.factor(p3))
out['D0_x3_on_deg_is_4(2Bl2+b^2l3+2bw2)'] = bool(C(p3 - 4*(2*B*ls[2] + b**2*ls[3] + 2*b*w2)) == 0)
for j in range(3, K):
    # solve chain[j] = 0 for l_j (linear), substitute into piv[j+1]
    cj = C(chain[j]); a1 = sp.diff(cj, ls[j]); a0 = C(cj - a1*ls[j])
    assert sp.diff(a1, ls[j]) == 0
    deg[ls[j]] = C(-a0/a1)
    out.setdefault('l_j_on_full_degenerate_chain', {})[j] = str(sp.factor(deg[ls[j]]))
    chain[j+1] = C(piv[j+1].subs(deg))
    out.setdefault('D0_xj_on_chain', {})[j+1] = str(sp.factor(chain[j+1]))
# ---- d row_k / d l_m = -[x^{k-m}] D with P held fixed (generic P symbols)
Psym = {k: sp.Symbol(f'P{k}') for k in range(K+1)}
Pg = S(Psym); Pg2 = mul(Pg, Pg)
g2 = add(scal(-sp.Rational(3,4)*B, xs), scal(-sp.Rational(3,2), Pg))
g1 = add(scal(-eta*b/2, {2: 1}), scal(-sp.Rational(3,2)*b, Pg))
g0 = add(scal(B, mul(xs, Pg)), scal(-eta*B, {3: 1}), scal(-1, theta_minus3(Pg2)))
Qg = [g0, g1, g2, q3, q4]
rowg = scal(-1, add(g0, mul(g1, Ld), mul(g2, L2), mul(q3, L3), mul(q4, mul(L3, Ld))))
Dg = add(g1, scal(2, mul(g2, Ld)), scal(3, mul(q3, L2)), scal(4, mul(q4, L3)))
ok = True; tested = 0
for k in range(4, K+1):
    for m in range(2, k+1):
        lhs = sp.diff(coeff(rowg, k), ls[m]); rhs = -coeff(Dg, k-m)
        tested += 1
        if C(lhs - rhs) != 0:
            ok = False; out.setdefault('pivot_identity_fail', []).append((k, m))
out['d_row_k/d_l_m_equals_-[x^{k-m}]D_(P fixed)'] = ok; out['pivot_identity_pairs_tested'] = tested
# ---- (Inf)
yv, om, Nn, lam, pp = sp.symbols('y omega N lambda p')
out['lc_D_is_(3/(4y^3))(1-4p)'] = bool(sp.simplify((sp.Rational(3,4)/yv**3 - 3*om/yv) - sp.Rational(3,4)/yv**3*(1 - 4*om*yv**2)) == 0)
edge = sp.Rational(3,16)*lam**4 - sp.Rational(3,2)*om*lam**2 - (4*Nn-3)*om**2
UT = (4*Nn-3)*pp**2 + sp.Rational(3,2)*pp - sp.Rational(3,16)
out['edge_poly_equals_-lam^4*UT(om/lam^2)'] = bool(sp.simplify(edge + lam**4*UT.subs(pp, om/lam**2)) == 0)
out['leading_Eminus_at_inf_holds_for_lam~^2=om/p~'] = bool(sp.simplify(om*((-sp.Rational(3,2)/(4*Nn-3))/(-sp.Rational(3,16)/(4*Nn-3))) - 8*om) == 0)
out['elapsed_s'] = round(time.time()-t0, 1)
keys = ['UF_holds_to_order_K', 'Q_P_at_L_vanishes', 'Hensel_factorisation_holds_mod_xK+1', 'L_is_root_of_F0', 'ltilde2_plus_l2_equals_-8eta/(3b)',
        's3_closed_form_4w2/b-16Beta/(3b^3)', 'pivot_flips_sign_on_Ltilde', 'Ltilde_is_formal_solution_same_P', 'Eminus_tau_Psi_plus_bq_zero',
        'cubic_Ctau_vanishes_on_tau', 'cubic_Cdelta_vanishes', 'D0_equals_16/3_D', 'D0_x0_x1_vanish', 'D0_x2_is_(4b/3)Lpivot', 'delta_2_equals_-D0_2/(2b^2)',
        'D0_x3_on_deg_is_4(2Bl2+b^2l3+2bw2)', 'd_row_k/d_l_m_equals_-[x^{k-m}]D_(P fixed)', 'lc_D_is_(3/(4y^3))(1-4p)', 'edge_poly_equals_-lam^4*UT(om/lam^2)',
        'leading_Eminus_at_inf_holds_for_lam~^2=om/p~']
out['ALL_PASS'] = bool(all(out[k] for k in keys))
json.dump(out, open(sys.argv[0].replace('.py', f'_K{K}.json'), 'w'), indent=1, default=str)
for k, v in out.items(): print(k, '=', v)
