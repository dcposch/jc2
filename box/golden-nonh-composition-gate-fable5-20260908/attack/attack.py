"""Independent bounded attacks (Fable gate). Only exact scalars, exponent
projections and monomial-pair bracket coefficients. No H/R powers, no
degree-6/10 initial polynomials expanded, no CAS."""
import json, sys
from fractions import Fraction as Q
INF = None  # infinite order
def le(a, b):  # a <= b with None = +infinity
    if b is None: return True
    if a is None: return False
    return a <= b
def lt(a, b):
    if a is None: return False
    if b is None: return True
    return a < b
def mn(a, b): return b if a is None else (a if b is None else min(a, b))
report = {}
# ---------- Attack 1: exhaustive order arithmetic for the two regimes ----------
# For each (j,kappa,q0) with 1<=j<=12, kappa in 1..40 or inf, q0 in j+1..60 or inf,
# recompute every inequality the source uses and record which triples survive.
survivors = []; violations = []
KAPPAS = list(range(1, 41)) + [INF]; QS = lambda j: list(range(j + 1, 61)) + [INF]
count = 0
for j in range(1, 13):
    for kappa in KAPPAS:
        for q0 in QS(j):
            count += 1
            regimeA = le(Q(2 * j, 5), kappa)  # kappa >= 2j/5 (inf counts)
            if regimeA:
                r = mn(Q(j, 5), None if q0 is None else Q(q0, 6))
                checks = {
                  'r_pos': r > 0, 'r_lt_5_2': r < Q(5, 2), 'kappa_ge_2r': le(2 * r, kappa),
                  'F_initial_6r': (Q(j) + r >= 6 * r) and le(6 * r, q0) and ((Q(j) + r == 6 * r) or (q0 is not None and Q(q0) == 6 * r)),
                  'd_n_later': Q(j) + 2 * r > 6 * r, 'RP1_later': 2 * r + j > 6 * r,
                  'alphaR_later': 10 + 2 * r > 6 * r, 'a0_later': 15 > 6 * r,
                  'kernels_later': all((5 - i) * (5 - 2 * r) > 0 for i in range(5)),
                  'b4RF_later': 5 + 8 * r > 10 * r, 'b3F_alphaF_later': 10 + 6 * r > 10 * r,
                  'G_ge_10r': 2 * j >= 10 * r, 'Y_weight_pos': Q(5, 2) - r > 0,
                }
                bad = [k for k, v in checks.items() if not v]
                if bad: violations.append((j, kappa, q0, 'A', bad))
                if 15 * r < 36: continue  # commuting initial -> Euler kill
                survivors.append((j, kappa, q0, 'A', str(r)))
            else:
                # regime B; kappa finite here
                if q0 is not None and q0 <= 3 * kappa:
                    r = Q(q0, 6)
                    checks = {'kappa_ge_2r': le(2 * r, kappa), 'r_lt_j5': r < Q(j, 5), 'ell_later': j + r > 6 * r,
                              'd_n_later': j + 2 * r > 6 * r, 'RP1_later': 2 * r + j > 6 * r, 'alphaR_later': 10 + 2 * r > 6 * r,
                              'a0_later': 15 > 6 * r, 'G_strictly_later': 2 * j > 10 * r,
                              'kernels_later': all((5 - i) * (5 - 2 * r) > 0 for i in range(5)),
                              'bracket_below_36': 15 * r < 36}
                    bad = [k for k, v in checks.items() if not v]
                    if bad: violations.append((j, kappa, q0, 'B1', bad))
                    continue
                nu = mn(q0, Q(j) + Q(kappa, 2)); eta = nu / 3
                checks = {'nu_gt_3kappa': nu > 3 * kappa, 'eta_gt_kappa': eta > kappa, 'eta_lt_5': eta < 5,
                          'RP1_later': eta + j > 3 * eta, 'd_n_later': j + kappa > nu,
                          'ell_linear_corr_later': Q(j) - Q(kappa, 2) + eta > 3 * eta,
                          'alphaR_later': 10 + eta > 3 * eta, 'a0_later': 15 > 3 * eta,
                          'G_later': 5 * eta < 2 * j, 'kernels_later': all((5 - i) * (5 - eta) > 0 for i in range(5)),
                          'b4RF_later': 5 + 4 * eta > 5 * eta, 'b3F_later': 10 + 3 * eta > 5 * eta,
                          'bracket_strict': 7 * eta < 36 - Q(kappa, 2), 'Z_weight_pos': 5 - eta > 0}
                bad = [k for k, v in checks.items() if not v]
                if bad: violations.append((j, kappa, q0, 'B2', bad))
report['attack1_triples_checked'] = count
report['attack1_violations'] = violations[:20]
report['attack1_violation_count'] = len(violations)
surv_ok = all(j == 12 and (k is None or k >= 5) and (q is None or q >= 15) for (j, k, q, _, _) in survivors)
cover_ok = all(any((12, k, q) == (s[0], s[1], s[2]) for s in survivors) for k in KAPPAS if (k is None or k >= 5) for q in QS(12) if (q is None or q >= 15))
report['attack1_survivor_count'] = len(survivors)
report['attack1_survivors_exactly_resonant_set'] = surv_ok and cover_ok
# Endpoint sanity: r at the resonant point and the two strict subwindows
report['attack1_endpoints'] = {'15r_at_j12_q0ge15': str(15 * Q(12, 5)), '15r_j11': str(15 * Q(11, 5)), '15r_j12_q0_14': str(15 * Q(14, 6)),
                               'B2_j12_kappa4_q0_13_7eta': str(7 * mn(13, Q(12) + Q(4, 2)) / 3), 'B2_target_j12_kappa4': str(36 - Q(4, 2))}
# ---------- Attack 2: monomial-pair Jacobians with free symbols (no power expansion) ----------
# coefficient ring: dict {(deg_k, deg_e, deg_u, deg_v): Fraction}; monomial (Y-exponent, p-exponent as Fraction)
def padd(a, b):
    o = dict(a)
    for m, c in b.items():
        o[m] = o.get(m, Q(0)) + c
        if o[m] == 0: del o[m]
    return o
def pmul(a, b):
    o = {}
    for m1, c1 in a.items():
        for m2, c2 in b.items():
            m = tuple(x + y for x, y in zip(m1, m2)); o[m] = o.get(m, Q(0)) + c1 * c2
            if o[m] == 0: del o[m]
    return o
def psc(a, c): return {m: v * c for m, v in a.items() if v * c != 0}
K, E, U, V = {(1, 0, 0, 0): Q(1)}, {(0, 1, 0, 0): Q(1)}, {(0, 0, 1, 0): Q(1)}, {(0, 0, 0, 1): Q(1)}
ONE = {(0, 0, 0, 0): Q(1)}
def bracket(P, Qp):
    """P,Q: dict {(i, alpha): coeffpoly}; [Y^i p^a, Y^j p^b] = (i b - j a) Y^(i+j-1) p^(a+b-1)."""
    out = {}
    for (i, a), c1 in P.items():
        for (j, b), c2 in Qp.items():
            d = i * b - j * a
            if d == 0: continue
            m = (i + j - 1, a + b - 1)
            out[m] = padd(out.get(m, {}), psc(pmul(c1, c2), d))
            if not out[m]: del out[m]
    return out
def show(br): return {f"Y^{i} p^{a}": {str(m): str(c) for m, c in poly.items()} for (i, a), poly in sorted(br.items())}
half = Q(1, 2)
q = Q(5, 3)
P = {(6, Q(0)): ONE, (1, half): K}
Qres = {(10, Q(0)): ONE, (5, half): psc(K, q), (0, Q(1)): E}
brPQ = bracket(P, Qres)
report['attack2_resonant_bracket'] = show(brPQ)
# expected: (6e - 10/3 k^2) Y^5 p^0 + e k Y^0 p^(1/2)
exp = {(5, Q(0)): padd(psc(E, 6), psc(pmul(K, K), Q(-10, 3))), (0, half): pmul(E, K)}
report['attack2_resonant_matches_consumer'] = (brPQ == exp)
# generic quintic factor q': Y^10 coefficient is (3q'-5) k p^(-1/2)
for qq in (Q(4, 3), Q(5, 3), Q(2)):
    br = bracket(P, {(10, Q(0)): ONE, (5, half): psc(K, qq), (0, Q(1)): E})
    report[f'attack2_Y10_coeff_q={qq}'] = show({m: c for m, c in br.items() if m[0] == 10})
# Regime B: [Z^3 + v p^(3h), Z^5 + (5/3) v p^(3h) Z^2] with h symbolic-free: use h=1/2 and h=7/3 samples
for h in (Q(1, 2), Q(7, 3), Q(2, 3)):
    PB = {(3, Q(0)): ONE, (0, 3 * h): V}
    QB = {(5, Q(0)): ONE, (2, 3 * h): psc(V, Q(5, 3))}
    br = bracket(PB, QB)
    report[f'attack2_regimeB_bracket_h={h}'] = show(br)  # expect -(10/3)*(3h) v^2 Z p^(6h-1) = -10h v^2 Z p^(6h-1)
# Regime A with b=0: [Y^6 + u p^(5h) Y + v p^(6h), Y^10 + (5/3)(u p^(5h) Y^5 + v p^(6h) Y^4) + e p^(10h)]
for h in (Q(1, 10), Q(1, 2)):
    PA = {(6, Q(0)): ONE, (1, 5 * h): U, (0, 6 * h): V}
    QA = {(10, Q(0)): ONE, (5, 5 * h): psc(U, Q(5, 3)), (4, 6 * h): psc(V, Q(5, 3)), (0, 10 * h): E}
    report[f'attack2_regimeA_b0_bracket_h={h}'] = show(bracket(PA, QA))
# ---------- Attack 3: weight slots and the R_s component weights ----------
def slots(wt, degmax): return [(i, j) for i in range(0, degmax + 1) for j in range(0, degmax + 1 - i) if 5 * i - 7 * j == wt]
report['attack3_slots'] = {'w1_deg<=5': slots(1, 5), 'w3_deg<=15': slots(3, 15), 'w5_deg<=25': slots(5, 25), 'w3_deg<=12_only_lower_A': slots(3, 12)}
# max weight of a degree-(5-i) component with weight<=1 (i>=1): monomials g^a p^(5-i-a)
comp = {}
for i in range(1, 6):
    ws = [5 * a - 7 * (5 - i - a) for a in range(0, 6 - i) if 5 * a - 7 * (5 - i - a) <= 1]
    comp[f'rho_{i} (deg {5-i})'] = {'allowed_g_degrees': [a for a in range(0, 6 - i) if 5 * a - 7 * (5 - i - a) <= 1], 'max_weight': max(ws)}
report['attack3_component_weights'] = comp
# s^12 coefficient of R_s^3: index triples i+j+k=12, i,j,k in 0..5; all indices >=2?
triples = [(i, j, k) for i in range(6) for j in range(6) for k in range(6) if i + j + k == 12]
report['attack3_s12_triples_all_ge2'] = all(min(t) >= 2 for t in triples)
report['attack3_s12_triple_count'] = len(triples)
# ---------- Attack 4: face determinant and golden identities in both embeddings ----------
def fk(a=0, b=0): return (Q(a), Q(b))
def fadd(x, y): return (x[0] + y[0], x[1] + y[1])
def fmul(x, y): return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0] + 3 * x[1] * y[1])
def fneg(x): return (-x[0], -x[1])
def fsc(x, n): return (x[0] * n, x[1] * n)
rows = []
for rho in (fk(0, 1), fk(3, -1)):
    one = fk(1); t = fadd(one, fneg(rho)); tm1 = fadd(t, fk(-1)); rinv = fadd(fk(3), fneg(rho))
    # face: e_f = 5 a rho^2/3, d_f = 5 a^2/(9 rho), c = -a d = -5 a^3/(9 rho); with a = lambda t, rho = t^2
    rho2 = fmul(rho, rho)
    e_over_a = fsc(rho2, Q(5, 3)); d_over_a2 = fsc(rinv, Q(5, 9)); c_face_over_l3 = fneg(fsc(fmul(fmul(t, fmul(t, t)), rinv), Q(5, 9)))
    # check the g16p10 and g9p5 rows with these solutions (divide by a, a^2 resp.)
    row16 = fadd(fsc(fmul(rho, fmul(rho2, rho2)), 5), fneg(fsc(fmul(fmul(rho, rho2), e_over_a), 3)))  # 5 rho^5 - 3 rho^3 (e/a)
    row9 = fadd(fsc(e_over_a, 2), fneg(fsc(fmul(fmul(rho, rho2), d_over_a2), 6)))  # 2 e/a - 6 rho^3 d/a^2
    c_res_over_l3 = fsc(fmul(t, fmul(tm1, tm1)), Q(5, 9))
    disc = fadd(fmul(tm1, tm1), one)
    rows.append({'rho': [str(x) for x in rho], 'row_g16p10_residual': [str(x) for x in row16], 'row_g9p5_residual': [str(x) for x in row9],
                 'c_face/lambda3': [str(x) for x in c_face_over_l3], 'c_face_equals_-5t/9': c_face_over_l3 == fsc(t, Q(-5, 9)),
                 'c_res/lambda3': [str(x) for x in c_res_over_l3], 'ratio_check_(t-1)^2+1': [str(x) for x in disc], 'disc_is_3rho': disc == fsc(rho, 3),
                 't2_is_rho': fmul(t, t) == rho, 'rho_nonzero': rho != fk(0), 'tm1_nonzero': tm1 != fk(0),
                 'sum_c_face_plus_c_res_over_(5t lambda3/9)': [str(x) for x in fadd(fmul(tm1, tm1), one)]})
report['attack4_rows'] = rows
# ---------- Attack 5: transverse coefficient and critical cubic via degree<=3 factors ----------
# D(g0+w,p) g-derivative at w=0 is (t-1)p^2; H(g0+w)/w^2 = t(t-1)p^3 + rho p^2 w: check via coefficient identities in Q[rho]
for rho in (fk(0, 1), fk(3, -1)):
    one = fk(1); t = fadd(one, fneg(rho)); tm1 = fadd(t, fk(-1)); tinv = fadd(fk(2), fneg(rho))
    g0 = fneg(tinv)  # g0/p = -1/t
    Lg0 = fadd(one, g0); Mg0 = fadd(one, fmul(t, g0))  # L/p, M/p at g0
    # d/dg (L M) at g0 = M + t L = 0 + t*(1 - 1/t) = t - 1
    dLM = fadd(Mg0, fmul(t, Lg0))
    # H(g0+w)/p^2 = (L0 + w)(M0 + t w)^2 with M0=0: = (L0 + w) t^2 w^2 -> w^2 coeff t^2 L0, w^3 coeff t^2
    report[f'attack5_rho={rho}'] = {'M(g0)=0': Mg0 == fk(0), 'L(g0)/p': [str(x) for x in Lg0], 'dLM/dg at g0': [str(x) for x in dLM],
        'equals_t-1': dLM == tm1, 'w2_coeff/p3': [str(x) for x in fmul(fmul(t, t), Lg0)], 'equals_t(t-1)': fmul(fmul(t, t), Lg0) == fmul(t, tm1),
        'w3_coeff/p2_is_rho': fmul(t, t) == rho}
print(json.dumps(report, indent=1, sort_keys=True, default=str))
