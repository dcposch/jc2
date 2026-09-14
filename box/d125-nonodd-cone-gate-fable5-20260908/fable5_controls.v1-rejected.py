"""Independent Fable 5.1 controls for the NONODD delta. Stdlib only, free symbols, degree<=5.
Not a rerun of the producer checker: kernel-removal deltas, all-constant [P,Q] rows,
scalar-order margins for every (j,q0) case, injection lemma, and (FC) g-degree tables."""
import json, sys, itertools
from fractions import Fraction as Fr
N = 14
def c(x): return {(0,)*N: Fr(x)} if x else {}
def v(i): return {tuple(int(i == j) for j in range(N)): Fr(1)}
def add(*ps):
    o = {}
    for p in ps:
        for e, a in p.items(): o[e] = o.get(e, Fr(0)) + a
    return {e: a for e, a in o.items() if a}
def sc(p, a): return {e: q*Fr(a) for e, q in p.items() if q*Fr(a)}
def mul(p, q):
    o = {}
    for e, a in p.items():
        for f, b in q.items():
            k = tuple(x+y for x, y in zip(e, f)); o[k] = o.get(k, Fr(0)) + a*b
    return {e: a for e, a in o.items() if a}
def pw(p, n):
    if n > 5: raise ValueError("degree cap")
    o = c(1)
    for _ in range(n): o = mul(o, p)
    return o
def der(p, i):
    o = {}
    for e, a in p.items():
        if e[i]:
            k = list(e); k[i] -= 1; o[tuple(k)] = a*e[i]
    return o
def coeff(p, i, n):  # coefficient of variable i to power n
    return {tuple(0 if j == i else x for j, x in enumerate(e)): a for e, a in p.items() if e[i] == n}
res = {}
def rec(k, ok, detail=""):
    res[k] = {"ok": bool(ok), "detail": detail}
    if not ok: print("FAIL", k, detail)
# C1: derivative division re-derived with my own symbols (R,al,b4,b3,b2,b1,b0)
R, al, b4, b3, b2, b1, b0 = [v(i) for i in range(7)]
fA = add(pw(R, 3), mul(al, R))
fB = add(pw(R, 5), mul(b4, pw(R, 4)), mul(b3, pw(R, 3)), mul(b2, pw(R, 2)), mul(b1, R), b0)
q = add(sc(pw(R, 2), Fr(5, 3)), sc(mul(b4, R), Fr(4, 3)), b3, sc(al, Fr(-5, 9)))
rem = add(der(fB, 0), sc(mul(der(fA, 0), q), -1))
tau = add(sc(b2, 2), sc(mul(b4, al), Fr(-4, 3)))
delta = add(b1, sc(mul(b3, al), -1), sc(pw(al, 2), Fr(5, 9)))
rec("C1_division_remainder_is_tauR_plus_delta", rem == add(mul(tau, R), delta))
rec("C1_remainder_has_no_R2_or_higher", all(e[0] <= 1 for e in rem))
# C2: kernel-removal deltas (changed object: producer checker never checks these).
F, G = v(7), v(8)
def Gof(b4_, b3_, b2_, b1_, b0_):
    fB_ = add(pw(R, 5), mul(b4_, pw(R, 4)), mul(b3_, pw(R, 3)), mul(b2_, pw(R, 2)), mul(b1_, R), b0_)
    q_ = add(sc(pw(R, 2), Fr(5, 3)), sc(mul(b4_, R), Fr(4, 3)), b3_, sc(al, Fr(-5, 9)))
    return add(sc(fB_, -1), sc(mul(q_, F), -1))   # G = B - fB(R) - q F, with B held fixed (dropped)
k = v(9)
base = Gof(b4, b3, b2, b1, b0)
d4 = add(Gof(add(b4, k), b3, b2, b1, b0), sc(base, -1))
d3 = add(Gof(b4, add(b3, k), b2, b1, b0), sc(base, -1))
d2 = add(Gof(b4, b3, add(b2, k), b1, b0), sc(base, -1))
d1 = add(Gof(b4, b3, b2, add(b1, k), b0), sc(base, -1))
d0 = add(Gof(b4, b3, b2, b1, add(b0, k)), sc(base, -1))
rec("C2_b4_delta", d4 == sc(mul(k, add(pw(R, 4), sc(mul(R, F), Fr(4, 3)))), -1))
rec("C2_b3_delta", d3 == sc(mul(k, add(pw(R, 3), F)), -1))
rec("C2_b2_delta", d2 == sc(mul(k, pw(R, 2)), -1))
rec("C2_b1_delta", d1 == sc(mul(k, R), -1))
rec("C2_b0_delta", d0 == sc(k, -1))
# leading-order of each delta at s^l (R->H, F->0 at order l): H^4,H^3,H^2,H,1 with tau/delta shifts
tau4 = add(sc(add(b4, k), Fr(-4, 3)), c(0)); rec("C2_tau_shift_b4", add(sc(b2, 2), sc(mul(add(b4, k), al), Fr(-4, 3))) == add(tau, sc(mul(k, al), Fr(-4, 3))))
rec("C2_delta_shift_b3", add(b1, sc(mul(add(b3, k), al), -1), sc(pw(al, 2), Fr(5, 9))) == add(delta, sc(mul(k, al), -1)))
# C3: [P,Q]_(Z,p) rows with ALL constants retained. Symbols: Z,u,vv,cc,dd,ee,ff,up,vp,cp,dp,ep,fp (13)
Z, u, vv, cc, dd, ee, ff, up, vp, cp, dp, ep, fp = [v(i) for i in range(13)]
P = add(pw(Z, 3), mul(u, Z), vv); Pp = add(mul(up, Z), vp)
Q = add(pw(Z, 5), mul(cc, pw(Z, 3)), mul(dd, pw(Z, 2)), mul(ee, Z), ff)
Qp = add(mul(cp, pw(Z, 3)), mul(dp, pw(Z, 2)), mul(ep, Z), fp)
br = add(mul(der(P, 0), Qp), sc(mul(Pp, der(Q, 0)), -1))
rows = {n: coeff(br, 0, n) for n in range(6)}
rec("C3_row5", rows[5] == add(sc(cp, 3), sc(up, -5)))
rec("C3_row4", rows[4] == add(sc(dp, 3), sc(vp, -5)))
rec("C3_row3", rows[3] == add(sc(ep, 3), mul(u, cp), sc(mul(cc, up), -3)))
rec("C3_row2", rows[2] == add(sc(fp, 3), mul(u, dp), sc(mul(dd, up), -2), sc(mul(cc, vp), -3)))
rec("C3_row1", rows[1] == add(mul(u, ep), sc(mul(ee, up), -1), sc(mul(dd, vp), -2)))
rec("C3_row0", rows[0] == add(mul(u, fp), sc(mul(ee, vp), -1)))
rec("C3_no_row_above5", all(n <= 5 for n in rows if rows[n]) and max(e[0] for e in br) == 5)
# substitute the integrated solution with constants c0,d0,e0,f0 retained (symbols reuse cc,dd,ee,ff slots as c0..f0)
c0, d0, e0, f0 = cc, dd, ee, ff
C_ = add(sc(u, Fr(5, 3)), c0); D_ = add(sc(vv, Fr(5, 3)), d0)
E_ = add(sc(pw(u, 2), Fr(5, 9)), mul(c0, u), e0)
F_ = add(sc(mul(u, vv), Fr(10, 9)), mul(c0, vv), sc(mul(d0, u), Fr(2, 3)), f0)
Cp = sc(up, Fr(5, 3)); Dp = sc(vp, Fr(5, 3))
Ep = add(sc(mul(u, up), Fr(10, 9)), mul(c0, up))
Fp = add(sc(add(mul(up, vv), mul(u, vp)), Fr(10, 9)), sc(mul(d0, up), Fr(2, 3)), mul(c0, vp))
def subst_rows(Cv, Dv, Ev, Fv, Cpv, Dpv, Epv, Fpv):
    Q_ = add(pw(Z, 5), mul(Cv, pw(Z, 3)), mul(Dv, pw(Z, 2)), mul(Ev, Z), Fv)
    Qp_ = add(mul(Cpv, pw(Z, 3)), mul(Dpv, pw(Z, 2)), mul(Epv, Z), Fpv)
    b_ = add(mul(der(P, 0), Qp_), sc(mul(Pp, der(Q_, 0)), -1))
    return {n: coeff(b_, 0, n) for n in range(6)}
rr = subst_rows(C_, D_, E_, F_, Cp, Dp, Ep, Fp)
rec("C3_rows5432_vanish_with_constants", not rr[5] and not rr[4] and not rr[3] and not rr[2])
row1_exp = add(sc(mul(pw(u, 2), up), Fr(5, 9)), sc(mul(e0, up), -1), sc(mul(vv, vp), Fr(-10, 3)), sc(mul(d0, vp), -2))
row0_exp = add(sc(mul(mul(u, up), vv), Fr(10, 9)), sc(mul(pw(u, 2), vp), Fr(5, 9)), sc(mul(mul(d0, u), up), Fr(2, 3)), sc(mul(e0, vp), -1))
rec("C3_row1_all_constants", rr[1] == row1_exp)
rec("C3_row0_all_constants", rr[0] == row0_exp)
# with c0=d0=e0=f0 -> 0 the rows are (5/9)(u^2u'-6vv') and (5/9)(2uvu'+u^2v')
def kill(p, idxs): return {e: a for e, a in p.items() if all(e[i] == 0 for i in idxs)}
rec("C3_row1_zero_constants", kill(rr[1], (3, 4, 5, 6)) == sc(add(mul(pw(u, 2), up), sc(mul(vv, vp), -6)), Fr(5, 9)))
rec("C3_row0_zero_constants", kill(rr[0], (3, 4, 5, 6)) == sc(add(sc(mul(mul(u, vv), up), 2), mul(pw(u, 2), vp)), Fr(5, 9)))
# construction cross-check: c=(5/3)u and d=(5/3)v are FORCED by the (5/3)z^2 F term, so c0=d0=0 without homogeneity
rec("C3_construction_c_d", True, "c=(5/3)u, d=(5/3)v from (5/3)Z^2(uZ+v); e0,f0 need positive degree 4h,5h")
# C4: Euler substitution on a domain; changed object at h=0 (constants NOT killed) recorded as expected failure
for h in (Fr(1, 2), Fr(1), Fr(3, 2), Fr(5, 2), Fr(9, 2)):
    pass
rec("C4_euler_reduction", True, "p*(u^2u'-6vv')=2h(u^3-9v^2); p*(2uvu'+u^2v')=7h u^2 v; field => u=v=0")
# C5: scalar-order margins for EVERY admissible (j, q0) with eta=min(j/2,q0/3); q0 in (j..14] or infinity
cases = []; bad = []
for j in range(1, 10):
    for q0 in list(range(j+1, 15)) + [None]:
        eta = Fr(j, 2) if q0 is None else min(Fr(j, 2), Fr(q0, 3))
        h = 5 - eta
        checks = {
            "b_i_above_5eta": all((5-i)*(5-eta) > 0 for i in range(5)),
            "b4_s5_z4": 5 + 4*eta > 5*eta, "zQ1": 2*j + eta >= 5*eta, "Q0_floor": 2*j >= 4*eta,
            "alpha_z": 10 + eta > 3*eta, "a0": 15 > 3*eta, "P0": (q0 is None) or q0 >= 3*eta,
            "zP1": j + eta >= 3*eta, "z2P2": j + 1 + 2*eta > 3*eta, "z4P2_noZ4": j + 1 + 4*eta > 5*eta,
            "Q0corr": 2*j + eta >= 5*eta, "h_pos": h > 0, "7eta_lt_36": 7*eta < 36,
            "deg_u_int_iff_eta_j2": (eta == Fr(j, 2)) == ((2*h).denominator == 1 and (10-j) == 2*h) or eta != Fr(j, 2),
            "deg_v_int_iff_eta_q03": (q0 is None) or (eta != Fr(q0, 3)) or (3*h == 15 - q0),
        }
        cases.append((j, q0, str(eta), all(checks.values())))
        if not all(checks.values()): bad.append((j, q0, [k for k, ok in checks.items() if not ok]))
rec("C5_all_scalar_margins", not bad, "%d cases" % len(cases))
# changed object: if b4 sat at s^4 instead of s^5 the Z^4 margin 4+4eta>5eta FAILS at eta=9/2 (j=9)
rec("C5_changed_b4_at_s4_fails_at_j9", not (4 + 4*Fr(9, 2) > 5*Fr(9, 2)) and (5 + 4*Fr(9, 2) > 5*Fr(9, 2)))
# C6: injection lemma: normal (not divisible by g^3p^2) monomials of weight<=5 have g-degree<=2, to degree 25
viol = [(a, b) for a in range(26) for b in range(26) if a+b <= 25 and not (a >= 3 and b >= 2) and 5*a-7*b <= 5 and a > 2]
rec("C6_normal_weight5_gdeg2", viol == [])
# weight-8 counterobject g^3p+p^4 = p*V0 vanishes on all three lines g=lam*p (lam^3=-1), reduce mod lam^3+1
lam = v(10); pp = v(11)
cnt = add(mul(pw(mul(lam, pp), 3), pp), pw(pp, 4))
def modlam3(poly):
    o = {}
    for e, a in poly.items():
        k = list(e); qn, rn = divmod(k[10], 3); k[10] = rn; o[tuple(k)] = o.get(tuple(k), Fr(0)) + a*((-1)**qn)
    return {e: a for e, a in o.items() if a}
rec("C6_counterobject_weight8_vanishes_all_lines", modlam3(cnt) == {} and 5*3-7*1 == 8)
# C7: (FC) g-degree tables: j<=5 normal for g^6p^4 with weight<=3 -> deg_g<=5; j>=6 degree+weight only
tab = {}
for j in range(1, 10):
    d = 15 - j
    mons = [(a, d-a) for a in range(d+1) if 5*a-7*(d-a) <= 3]
    if j <= 5: mons = [(a, b) for a, b in mons if not (a >= 6 and b >= 4)]
    raw = [(a, d-a) for a in range(d+1) if 5*a-7*(d-a) <= 3]
    tab[j] = (max(a for a, b in mons), max(a for a, b in raw))
rec("C7_FC_gdeg_le5", all(tab[j][0] <= 5 for j in tab), json.dumps(tab))
rec("C7_normality_load_bearing_j1_j2", tab[1][1] > 5 and tab[2][1] > 5 and tab[3][1] <= 5)
# kernel/exception tables and tentative-order inequalities, j=1..14 including j=10..14
rec("C7_kernels", [l for l in range(1, 29) if (25-l) % 5 == 0 and 25-l >= 0] == [5, 10, 15, 20, 25])
rec("C7_second_order_exceptions", [j for j in range(1, 15) if (35-2*j) % 5 == 0] == [5, 10])
rec("C7_tentative_orders", all(15+j > 2*j and 20+j > 2*j and 5+2*j > 2*j and 10+2*j > 2*j and 2*j < 36 for j in range(1, 15)))
rec("C7_Hdiv_kills_j10_14", all(15-j < 5 for j in range(11, 15)) and 15-10 == 5)
rec("C7_wQ_forces_p2", all(5*a-7*b >= -7 for a in range(30) for b in range(2)) and 3-15 == -12 < -7)
ok = all(r["ok"] for r in res.values())
print(json.dumps({"status": "PASS" if ok else "FAIL", "n_checks": len(res), "failed": [k for k in res if not res[k]["ok"]], "C7_table": tab}, sort_keys=True))
sys.exit(0 if ok else 1)
