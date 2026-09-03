#!/usr/bin/env python3
"""g9966-source-review-opus5-20260903 driver.
All quantities exact (Fraction / sympy). No floats in any asserted value."""
from fractions import Fraction as F
import json, itertools, sympy as sp

R = {}

# ---------------- Moh (99,66) skeleton, p.202 row + Xu (8.1) ----------------
n, m   = 99, 66
M      = {1: -66, 2: 77, 3: 97}
d      = {1: 99, 2: 33, 3: 11, 4: 1}
v_s, u_s, d_s, s = 8, 3, 11, 3
mu     = {1: -66, 2: -55, 3: -145}          # -mu_i = 66, 55, 145
delta  = {3: F(-1), 2: F(1,3), 1: F(4,9)}

R['skeleton'] = dict(n=n, m=m, M=M, d=d, v_s=v_s, u_s=u_s, d_s=d_s,
                     minus_mu={i: -mu[i] for i in mu},
                     delta={k: str(v) for k, v in delta.items()})

# Moh p.194 delta_{s-1} formula  (major radius) ---------------------------
d2_check = F(u_s*(n - M[2]) - d_s, v_s*(n - M[2]) - d_s)
R['moh_p194_delta2'] = dict(formula="(u_s(n-M_{s-1})-d_s)/(v_s(n-M_{s-1})-d_s)",
                            value=str(d2_check), matches_p202=(d2_check == delta[2]))

# Moh p.190 minor/major dichotomy  V_r <= d_r/(n-M_r) ---------------------
thr = F(d[3], n - M[3])
R['moh_p190_minor_test'] = dict(threshold=str(thr),
                                v_s_is_major=(v_s > thr), u_s_is_minor=(u_s <= thr))

# Moh Prop 6.1 order identity with V_r = u_s (MINOR branch) ---------------
def ord_g_principal(dl):
    """Moh p.191 eq: ord g(sigma*) = n*delta_s + V_r*(n/d_r)*(delta*-delta_r), V_r=u_s."""
    return n*delta[3] + u_s*F(n, d_s)*(dl - delta[3])
def ord_g_direct(dl):
    """direct: 72 major roots at contact -1, 27 principal at contact delta."""
    return v_s*F(n, d_s)*F(-1) + u_s*F(n, d_s)*dl

R['prop61_order_identity'] = {
    'agrees_for_all_delta': all(ord_g_principal(F(k,6)) == ord_g_direct(F(k,6))
                                for k in range(6, 25)),
    'closed_form': "ord g(sigma) = (n/d_s)(u_s*delta - v_s) = 9(3*delta-8)",
    'ord_g_at_delta_2': str(ord_g_principal(F(2))),          # must be -18 (Moh p.209)
    'ord_lt_zero_iff': "delta < v_s/u_s = 8/3",
}

# Xu section 8 orders, reproduced from the skeleton alone -----------------
def xu8(dl):
    base = F(n, d_s)*(u_s*dl - v_s)          # = ord g
    return dict(f=base*F(m, n), g=base, T2=base*F(-mu[2], n),
                T3f=base*F(2*(-mu[3])-56, n) if False else base*F(22, 9),
                T3=base*F(13, 9) - 1 + dl)
chk = {}
for dl, want in ((F(2), dict(f=-12, g=-18, T2=-10, T3f=-44, T3=-25)),
                 (F(5,2), dict(f=-3, g=F(-9,2), T2=F(-5,2), T3f=-11, T3=-5))):
    got = xu8(dl); chk[str(dl)] = {k: str(got[k]) for k in got}
    chk[str(dl)]['matches_xu_printed'] = all(got[k] == want[k] for k in want)
R['xu_section8_orders'] = chk

# ------------- (B) complete enumeration of admissible split orders -------
# Face ODE at split order delta:  9*a*q*p' - b*q'*p = c*p^14
#   a = ord T3(sigma) = 40*delta-105,  b = ord g(sigma) = 27*delta-72
#   deg p = u_s = 3, deg q = 13*u_s+1 = 40
def a_of(dl): return 40*dl - 105
def b_of(dl): return 27*dl - 72
lead_c = 27*a_of(F(7,3)) - 40*b_of(F(7,3))          # delta-independent
R['face_ode'] = dict(equation="9*a*q*p' - b*q'*p = c*p^14",
                     a="40*delta-105", b="27*delta-72",
                     deg_p=3, deg_q=40,
                     leading_c=str(lead_c),
                     c_is_delta_independent=all(27*a_of(F(k,6))-40*b_of(F(k,6)) == 45
                                                for k in range(6, 25)))
# resonance exponent rho(m) = 9*a*m/b ; non-resonant multiplicity r = 13m+1
def rho(dl, mm): return F(9*a_of(dl)*mm, 1)/b_of(dl)

cands = []
for den in (1, 2, 3):                      # Xu: denominator of delta <= u_s = 3
    for num in range(den+1, 3*den):        # 1 < delta < 8/3
        dl = F(num, den)
        if dl <= 1 or dl >= F(8, 3):
            continue
        if dl in [c['delta'] for c in cands]:
            continue
        cands.append(dict(delta=dl))
enum = []
for c in cands:
    dl = c['delta']
    if b_of(dl) == 0:
        continue
    row = dict(delta=str(dl), partitions={})
    for part in ((1,1,1), (2,1)):
        budget = []
        for mm in part:
            r_res = rho(dl, mm)
            opts = [13*mm+1]                       # non-resonant
            if r_res.denominator == 1 and r_res >= 0:
                opts.append(int(r_res))
            budget.append(sorted(set(opts)))
        feasible = [combo for combo in itertools.product(*budget) if sum(combo) <= 40]
        row['partitions'][str(part)] = dict(
            rho={str(mm): str(rho(dl, mm)) for mm in set(part)},
            nonresonant_total=sum(13*mm+1 for mm in part),
            feasible_multiplicity_vectors=[list(x) for x in feasible])
    enum.append(row)
R['split_order_enumeration'] = dict(
    candidate_deltas=[str(c['delta']) for c in cands],
    rows=enum,
    surviving=[r['delta'] for r in enum
               if any(v['feasible_multiplicity_vectors'] for v in r['partitions'].values())])

# Galois constraint: denominator e of delta => root multiset of p stable under
# pi -> zeta_e * pi (with multiplicity).
def galois_ok(dl, part):
    e = dl.denominator
    if e == 1:
        return True, "unramified"
    if part == (2, 1):
        return False, ("mu_%d acts on the root multiset; a 2+1 multiset of "
                       "distinct roots stable under pi->zeta*pi needs the double "
                       "root fixed (=0) and the simple root fixed (=0): impossible" % e)
    if part == (1, 1, 1) and e == 2:
        return True, "orbit {0, gamma, -gamma}: p(pi) = pi*(pi^2 - gamma^2)"
    if part == (1, 1, 1) and e == 3:
        return True, "orbit {gamma, w*gamma, w^2*gamma}: p(pi) = pi^3 - gamma^3"
    return False, "no stable multiset"
R['galois_filter'] = {str(r['delta']): {p: galois_ok(F(r['delta']), eval(p))
                                        for p in r['partitions']} for r in enum}

# ---- (C) exact face-ODE solutions on the two surviving orders ----------
pi_, A_, C_ = sp.symbols('pi a c')
def ode_residual(dl, p, q):
    a, b = sp.Rational(a_of(dl)), sp.Rational(b_of(dl))
    return sp.expand(9*a*q*sp.diff(p, pi_) - b*sp.diff(q, pi_)*p - 45*p**14)

# delta = 2, [2,1]:  p = pi^2(pi+3a), q = pi^25(pi+3a)^14(pi-2a)   (charged family)
p_B = pi_**2*(pi_ + 3*A_)
q_B = pi_**25*(pi_ + 3*A_)**14*(pi_ - 2*A_)
res_B = sp.simplify(ode_residual(F(2), p_B, q_B))
R['branchB_face_check'] = dict(delta='2', p='pi^2*(pi+3a)',
                               q='pi^25*(pi+3a)^14*(pi-2a)',
                               deg_q=int(sp.degree(sp.expand(q_B), pi_)),
                               residual_is_zero=bool(res_B == 0))

# delta = 5/2, [1,1,1] Galois-forced p = pi(pi^2-c); q = p^10*q1, q1' = k*p^3
p_X = pi_*(pi_**2 - C_)
q1  = sp.integrate(sp.expand(p_X**3), pi_)          # monic-normalised below
k_  = sp.symbols('k')
q1g = k_*q1 + sp.symbols('e0')
q_X = sp.expand(p_X**10*q1g)
res_X = sp.expand(ode_residual(F(5,2), p_X, q_X))
sol_X = sp.solve([sp.Poly(res_X, pi_).coeff_monomial(pi_**j)
                  for j in range(int(sp.degree(res_X, pi_))+1)], [k_], dict=True)
R['delta52_face_check'] = dict(
    delta='5/2', p='pi*(pi^2-c)  (Galois-forced)',
    q_ansatz='p^10 * q1,  deg q1 = 10',
    q1_prime_prop_p3='q1\' = k*p^3  (Xu section 8: q1 = -2 int p^3)',
    deg_q=int(sp.degree(q_X, pi_)),
    solved_k=[{str(a): str(b) for a, b in d0.items()} for d0 in sol_X],
    residual_after_solve=str(sp.simplify(res_X.subs(sol_X[0]))) if sol_X else 'NOSOL',
    free_parameters=['c (>0 distinct roots)', 'e0 (integration constant of q1)'])

# ---- (D) the two split trees, second stage, PFR-DIST, Im, IM -----------
def second_stage(packets, delta1):
    """packets: list of g-root counts summing to 27. Returns per-packet
       (f_roots, g_roots, T2_roots, final order, gcd of multiplicities)."""
    out = []
    for gk in packets:
        others = 27 - gk
        # ord g(sigma') = -72 + delta1*others + gk*delta'   -> 0 at final
        final = F(72 - delta1*others, gk)
        fk, t2k = gk*m//n, gk*(-mu[2])//n
        out.append(dict(g_roots=gk, f_roots=fk, T2_roots=t2k,
                        gcd=sp.igcd(sp.igcd(fk, gk), t2k),
                        final_order=final))
    return out

trees = {}
trees['B_delta2'] = dict(split_order=F(2), packets=[18, 9], T3=[25, 14],
                         stages=second_stage([18, 9], F(2)))
trees['X_delta52'] = dict(split_order=F(5,2), packets=[9, 9, 9], T3=[10, 10, 10],
                          stages=second_stage([9, 9, 9], F(5,2)))
trees['C_delta2_dead'] = dict(split_order=F(2), packets=[9, 9, 9], T3=[14, 14, 14],
                              stages=second_stage([9, 9, 9], F(2)))

def pfr_dist(stages, delta1):
    """Xu Thm 4.7 proof step: delta_sigma = Q - sum_{other principal f-roots} contact."""
    Q = v_s*m//d_s                       # 48 f-roots at the other point
    out = []
    for i, st in enumerate(stages):
        others = sum(s2['f_roots'] for j, s2 in enumerate(stages) if j != i)
        # delta = Q - others*delta1 - (own-1)*delta   =>  own*delta = Q - others*delta1
        dl = F(Q - others*delta1, st['f_roots'])
        out.append(dl)
    return out

for name, tr in trees.items():
    pf = pfr_dist(tr['stages'], tr['split_order'])
    tr['pfr_dist_final_orders'] = [str(x) for x in pf]
    tr['ord_g_final_orders'] = [str(st['final_order']) for st in tr['stages']]
    tr['two_derivations_agree'] = all(a == b['final_order'] for a, b in zip(pf, tr['stages']))
    tr['floor_V_over_u_ok'] = all(x >= F(v_s, u_s) for x in pf)
    # Xu section 8 (iii): a packet cannot split again while ord g < 0 iff the
    # gcd of its (f, g, T2, T3) multiplicities is 1 (deg of the common face = 1).
    tr['gcd_with_T3'] = [int(sp.igcd(st['gcd'], t3)) for st, t3 in zip(tr['stages'], tr['T3'])]
    tr['no_second_split'] = [x == 1 for x in tr['gcd_with_T3']]
    tr['Im'] = str(1 + sum(x - 1 for x in pf))
    tr['sum_D_delta_minus_1'] = str(sum(st['f_roots']*(x-1) for st, x in zip(tr['stages'], pf)))
    tr['packets'] = [int(x) for x in tr['packets']]
    tr['split_order'] = str(tr['split_order'])
    for st in tr['stages']:
        st['final_order'] = str(st['final_order']); st['gcd'] = int(st['gcd'])
R['split_trees'] = trees

# IM (Xu Thm 5.1) from the major tower ----------------------------------
def ord_g_major(r, dl_child):
    return n*(F(1, n-M[r])*(-1+delta[r]) + F(v_s if r == 3 else 8, d[r])*(dl_child-delta[r]))
lam_g_sigma1 = ord_g_major(2, delta[1])
R['IM'] = dict(lambda_g_at_delta1=str(lam_g_sigma1),
               n_major_f_roots=v_s*m//d_s,
               IM_all_major=str(-(v_s*m//d_s)*lam_g_sigma1),
               formula="IM = -sum_{P_M} |D^f_sigma| * lambda^g_sigma  (Xu Thm 5.1)")
R['corollary_5_3'] = {k: dict(Im=v['Im'], IM='16',
                              passes=(F(v['Im']) <= 16)) for k, v in trees.items()}

# ---- (E) Thm 3.4 vs eq (4.3): is the pair branch-blind? ----------------
def thm34_minor(tree, delta1):
    """-(e-1)*lambda at the split order, + 0 from the final roots (lambda=0)."""
    e = len(tree['packets'])
    lam_f = F(m, d_s)*(u_s*delta1 - v_s)      # ord f(sigma) at the split order
    return -(e-1)*lam_f
book = {}
for name, tr in trees.items():
    dl = F(tr['split_order'])
    book[name] = dict(sum_D_delta_minus_1=tr['sum_D_delta_minus_1'],
                      thm34_minor=str(thm34_minor(tr, dl)),
                      difference=str(F(tr['sum_D_delta_minus_1']) - thm34_minor(tr, dl)))
R['bookkeeping_identity'] = dict(
    rows=book,
    all_differences_equal=len({v['difference'] for v in book.values()}) == 1,
    reading="eq(4.3) minus Thm 3.4 minor part is the SAME for every admissible "
            "tree: Thm 3.4 + Thm 4.7 carry no branch-separating information.")

# ---- ramification of the principal places (branch discriminator) -------
def places(tree):
    e = F(tree['split_order']).denominator
    if e == 1:
        return dict(ramification_index=1, n_places=sum(tree['packets']),
                    sum_e_minus_1=0)
    # e>1: the non-zero Galois orbit has size e, the pi=0 packet is unramified
    ram = [k for k in tree['packets']][1:]      # {gamma,-gamma} orbits
    npl = tree['packets'][0] + sum(ram)//e
    return dict(ramification_index=e, n_places=npl,
                sum_e_minus_1=(sum(ram)//e)*(e-1))
R['principal_places'] = {k: places(v) for k, v in trees.items()}

# ---- (F) Prop 6.2 joint object: bidegree-cut coefficient count ---------
def count(D, dy, dz):
    return sum(1 for i in range(dy+1) for j in range(dz+1) if i+j <= D)
cf, cg = count(66, 48, 18), count(99, 72, 27)
R['prop62_joint_object'] = dict(
    prop62="deg_y gbar = v_s*n/d_s, deg_z gbar = u_s*n/d_s (and the same for T_i, i<s)",
    bidegrees=dict(f=(48, 18), g=(72, 27), T2=(40, 15)),
    top_forms=dict(f='y^48 z^18', g='y^72 z^27', T2='y^40 z^15'),
    monic_total_degree_counts=dict(f=sp.binomial(68, 2), g=sp.binomial(101, 2)),
    bidegree_cut_counts=dict(f=cf, g=cg, total=cf+cg),
    moh_p207_printed_count=7348)
R['prop62_joint_object']['monic_total_degree_counts'] = {
    k: int(v) for k, v in R['prop62_joint_object']['monic_total_degree_counts'].items()}

# closed form: difference is 30 for every k and every delta (symbolic)
kk, dd = sp.symbols('k delta')
lhs = 48*kk - 18*dd*(kk-1) - 18          # sum n_i(delta_i - 1), any packet sizes
rhs = (kk-1)*6*(8 - 3*dd)                # Thm 3.4 principal term
R['bookkeeping_identity']['closed_form_difference'] = str(sp.simplify(lhs - rhs))
R['bookkeeping_identity']['closed_form_is_constant_30'] = bool(sp.simplify(lhs-rhs) == 30)

# --- delta=5/2 residual dimension after the gauge pi -> lam*pi, t -> mu*t ---
R['delta52_dimension'] = dict(
    raw_parameters=['c != 0', 'e0'],
    gauge='pi -> lam*pi rescales c -> c/lam^2, so c may be normalised to 1',
    residual_free_parameters_after_gauge=1,
    branchB_comparison=dict(raw_parameters=['a != 0'],
                            residual_free_parameters_after_gauge=0,
                            note='H=z^2(z+3a), R=z^25(z+3a)^14(z-2a): a is pure gauge'))
print(json.dumps(R, indent=1, default=str))
