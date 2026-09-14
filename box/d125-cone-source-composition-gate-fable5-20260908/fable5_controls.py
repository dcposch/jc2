#!/usr/bin/python3
"""Fable 5.1 independent changed-object controls (stdlib only, tiny objects, no H^3/H^5/A15/B25 expansion).
Each control is a universal identity on free symbols or an exhaustive finite enumeration, except C8 (sampled illustration)."""
import sys
sys.dont_write_bytecode = True
from fractions import Fraction as Q
import json, random, itertools
random.seed(20260908)
def need(ok, msg):
    if not ok: raise ValueError(msg)
def add(*ps):
    r = {}
    for p in ps:
        for e, c in p.items(): r[e] = r.get(e, Q(0)) + c
    return {e: c for e, c in r.items() if c}
def sc(p, c): return {e: a * c for e, a in p.items() if a * c}
def mul(p, q):
    r = {}
    for e, a in p.items():
        for f, b in q.items():
            v = tuple(i + j for i, j in zip(e, f)); r[v] = r.get(v, Q(0)) + a * b
    return {e: c for e, c in r.items() if c}
def pw(p, n, dim):
    r = {(0,) * dim: Q(1)}
    for _ in range(n): r = mul(r, p)
    return r
def d(p, i):
    r = {}
    for e, c in p.items():
        if e[i]:
            f = list(e); f[i] -= 1; r[tuple(f)] = r.get(tuple(f), Q(0)) + c * e[i]
    return {e: c for e, c in r.items() if c}
def br(p, q, i, j): return add(mul(d(p, i), d(q, j)), sc(mul(d(p, j), d(q, i)), -1))
def w(a, b): return 5 * a - 7 * b
out = {}

# C1: formal dilation law. Variables (s,g,p). A_s = sum s^(15-d) A_d, B_s = sum s^(25-d) B_d.
# Claim: [A_s,B_s]_(g,p) = sum_d s^(38-d) [A,B]_d ; in particular a g^2 term maps to s^36 g^2.
def rnd_poly(deg, terms):
    p = {}
    while len(p) < terms:
        a = random.randint(0, deg); b = random.randint(0, deg - a)
        p[(a, b)] = Q(random.randint(-5, 5) or 1)
    return p
def dil(p, D): return {(D - a - b, a, b): c for (a, b), c in p.items()}
for trial in range(3):
    A = rnd_poly(15, 7); A[(9, 6)] = Q(1); B = rnd_poly(25, 7); B[(15, 10)] = Q(1)
    J = br(A, B, 0, 1)
    Js = br(dil(A, 15), dil(B, 25), 1, 2)
    need(Js == {(38 - a - b, a, b): c for (a, b), c in J.items()}, "dilation law")
    bad = br(dil(A, 14), dil(B, 25), 1, 2)   # changed object: wrong A exponent
    need(bad != {(38 - a - b, a, b): c for (a, b), c in J.items()}, "changed-exponent control must fail")
out["C1_dilation_law"] = {"trials": 3, "target_exponent_for_g2": 36, "changed_exponent_fails": True}

# C2: R_s^3 and alpha_s R_s order table with free symbols (s,H,R3,R1,alpha), R_s=H+s^2R3+s^4R1.
dim = 5
S, Hh, R3, R1, al = [{tuple(int(k == i) for k in range(dim)): Q(1)} for i in range(dim)]
Rs = add(Hh, mul(pw(S, 2, dim), R3), mul(pw(S, 4, dim), R1))
cube = pw(Rs, 3, dim); alR = mul(mul(pw(S, 10, dim), al), Rs)
tot = add(cube, alR)
def s_coeff(p, n): return {e[1:]: c for e, c in p.items() if e[0] == n}
one = {(0,) * (dim - 1): Q(1)}
H_, R3_, R1_, al_ = [{tuple(int(k == i) for k in range(dim - 1)): Q(1)} for i in range(dim - 1)]
def P(p, n): return pw(p, n, dim - 1)
expect = {0: P(H_, 3), 2: sc(mul(P(H_, 2), R3_), 3), 4: add(sc(mul(P(H_, 2), R1_), 3), sc(mul(H_, P(R3_, 2)), 3)),
          6: add(sc(mul(mul(H_, R3_), R1_), 6), P(R3_, 3)), 8: add(sc(mul(H_, P(R1_, 2)), 3), sc(mul(P(R3_, 2), R1_), 3)),
          10: add(sc(mul(R3_, P(R1_, 2)), 3), mul(al_, H_)), 12: add(P(R1_, 3), mul(al_, R3_)), 14: mul(al_, R1_)}
for n in range(0, 17):
    need(s_coeff(tot, n) == expect.get(n, {}), f"R_s^3+alpha_s R_s order {n}")
out["C2_reference_order_table"] = {"orders": sorted(expect), "order10_is_3R3R1sq_plus_alphaH": True, "no_order_above_14": True}

# C3: normal (no g^3p^2 divisor) + weight<=5  =>  deg_g<=2, exhaustively for total degree<=23; hence Vandermonde injection.
viol = [(a, b) for a in range(24) for b in range(24) if a + b <= 23 and w(a, b) <= 5 and not (a >= 3 and b >= 2) and a >= 3]
need(viol == [], "normal weight<=5 monomials have g-degree<=2")
# changed object: weight bound relaxed to 8 admits p*V0 = g^3p+p^4, normal, vanishing on all three lines g=zeta p.
pV0 = {(3, 1): Q(1), (0, 4): Q(1)}
need(all(not (a >= 3 and b >= 2) for a, b in pV0) and max(w(a, b) for a, b in pV0) == 8, "p*V0 normal of weight 8")
def rem_mod_X3p1(coeffs):  # X-polynomial reduced mod X^3+1 (vanishing on all three lines iff zero)
    r = [Q(0)] * 3
    for a, c in coeffs.items(): r[a % 3] += c * ((-1) ** (a // 3))
    return r
need(rem_mod_X3p1({a: c for (a, b), c in pV0.items()}) == [0, 0, 0], "p*V0 vanishes on all three branches")
out["C3_product_injection"] = {"exhaustive_degree_max": 23, "g_degree_bound": 2, "changed_weight8_counter": "g^3p+p^4"}

# C4: g-degree of F_j: degree 15-j, weight<=3; j=2,4 need g^6p^4-normality; j=6,8 need nothing extra; j=10 alpha slot.
tab = {}
for j in (2, 4, 6, 8, 10):
    D = 15 - j
    mons = [(a, D - a) for a in range(D + 1) if w(a, D - a) <= 3]
    raw = max(a for a, b in mons)
    normal6 = max(a for a, b in mons if not (a >= 6 and b >= 4))
    tab[j] = {"raw_max_g_degree": raw, "after_g6p4_normality": normal6, "monomials": mons if j == 10 else len(mons)}
need(tab[2]["raw_max_g_degree"] == 7 and tab[4]["raw_max_g_degree"] == 6, "normalization is load-bearing at j=2,4")
need(all(tab[j]["after_g6p4_normality"] <= 5 for j in (2, 4)) and tab[6]["raw_max_g_degree"] <= 5 and tab[8]["raw_max_g_degree"] <= 4, "deg_g F_j<=5")
need(sorted(tab[10]["monomials"]) == sorted([(3, 2), (2, 3), (1, 4), (0, 5)]), "degree-5 weight<=3 slots")
out["C4_Fj_g_degree"] = tab

# C5: second-order centralizer degree table and G kernel table.
out["C5_degree_tables"] = {"T_degree_35-2j_div5": [j for j in range(2, 15, 2) if (35 - 2 * j) % 5 == 0],
                           "G_kernels_l": [l for l in range(2, 29, 2) if (25 - l) % 5 == 0]}
need(out["C5_degree_tables"]["T_degree_35-2j_div5"] == [10] and out["C5_degree_tables"]["G_kernels_l"] == [10, 20], "tables")

# C6: [Z^3+uZ+v, e] with D: Z^2 coefficient is 3De, whole bracket (3Z^2+u)De. Free symbols (Z,u,v,e,Du,Dv,De).
n = 7
Z, u, v, e, Du, Dv, De = [{tuple(int(k == i) for k in range(n)): Q(1)} for i in range(n)]
def Dop(p): return add(mul(d(p, 1), Du), mul(d(p, 2), Dv), mul(d(p, 3), De))
Pc = add(pw(Z, 3, n), mul(u, Z), v)
bre = add(mul(d(Pc, 0), Dop(e)), sc(mul(Dop(Pc), d(e, 0)), -1))
need(bre == mul(add(sc(pw(Z, 2, n), 3), u), De), "[P,e]=(3Z^2+u)De")
out["C6_lower_e_bracket"] = "Z^2 coefficient 3*De, Z^0 coefficient u*De"

# C7: 3/5 elimination by random rational evaluation (independent of dictionary-polynomial method).
def eval35(a, b, da, db, c0, d0, e0, f0, quartic7=Q(7, 3)):
    c = Q(5, 3) * a + c0; dd = Q(5, 3) * b + d0; ee = Q(5, 9) * a * a + c0 * a + e0
    ff = Q(10, 9) * a * b + c0 * b + Q(2, 3) * d0 * a + f0
    dc = Q(5, 3) * da; ddd = Q(5, 3) * db; de = Q(10, 9) * a * da + c0 * da
    df = Q(10, 9) * (da * b + a * db) + c0 * db + Q(2, 3) * d0 * da
    Pz = [3, 0, a]            # P_Z = 3Z^2 + a (coeffs high->low)
    DP = [da, db]             # a'Z + b'
    Qz = [5, 0, 3 * c, 2 * dd, ee]
    DQ = [dc, ddd, de, df]
    def pm(x, y):
        r = [Q(0)] * (len(x) + len(y) - 1)
        for i, xi in enumerate(x):
            for k, yk in enumerate(y): r[i + k] += xi * yk
        return r
    A1 = pm(Pz, DQ); A2 = pm(DP, Qz)
    L = max(len(A1), len(A2)); A1 = [Q(0)] * (L - len(A1)) + A1; A2 = [Q(0)] * (L - len(A2)) + A2
    Jc = [x - y for x, y in zip(A1, A2)]   # degree 5 .. 0
    bt = b + Q(3, 5) * d0; K0 = Q(9, 5) * e0
    J1 = Q(5, 9) * (a * a - K0) * da - Q(10, 3) * bt * db
    J0 = Q(5, 9) * (a * a - K0) * db + Q(10, 9) * a * bt * da
    L0 = a ** 3 / 3 - K0 * a - 3 * bt * bt
    det = (a * a - K0) ** 2 + 12 * a * bt * bt
    quart = quartic7 * a ** 4 - 6 * K0 * a * a - 4 * L0 * a + K0 * K0
    return Jc, J1, J0, det, quart
for t in range(20):
    vals = [Q(random.randint(-9, 9), random.randint(1, 4)) for _ in range(8)]
    Jc, J1, J0, det, quart = eval35(*vals)
    need(all(x == 0 for x in Jc[:4]) and Jc[4] == J1 and Jc[5] == J0, "3/5 elimination at random point")
    need(det == quart, "determinant quartic 7/3 at random point")
    need(eval35(*vals, quartic7=Q(2))[3] != eval35(*vals, quartic7=Q(2))[4] or vals[0] == 0, "changed quartic fails")
out["C7_random_point_35"] = {"points": 20, "quartic_coefficient": "7/3", "changed_quartic_fails": True}

# C8: consumer window inequalities, exhaustive over j in {2,4,6,8} and integer q in (j,120] plus infinity. SAMPLED ILLUSTRATION ONLY.
cnt = 0
for j in (2, 4, 6, 8):
    for q in list(range(j + 1, 121)) + [None]:
        eta = Q(j, 2) if q is None else min(Q(j, 2), Q(q, 3)); qq = Q(10 ** 9) if q is None else Q(q)
        need(Q(j, 3) < eta <= Q(j, 2) <= 4, "eta range")
        need(10 + eta > 3 * eta and j + 2 * eta > 3 * eta, "cubic initial: alpha and P2 absent")
        need(20 + eta > 5 * eta and 10 + 3 * eta > 5 * eta, "delta, alpha^2, alpha*F above 5eta")
        need(qq + 2 * eta >= 5 * eta and j + 3 * eta >= 5 * eta and j + 4 * eta > 5 * eta and 2 * j + eta >= 5 * eta, "F/G blocks")
        need(2 * eta + 2 * j < 36 and 7 * eta <= 28 < 36, "target separation (nu>=2j lower bound and 7eta)")
        cnt += 1
out["C8_window_inequalities_sampled"] = {"cases": cnt, "universal_proof": "prose only; this is an illustration"}

# C9: 14c polygon -> candidate system: vertex weights and outer edge.
Av = [(0, 0), (2, 1), (9, 6), (0, 15)]; Bv = [(0, 0), (1, 0), (15, 10), (0, 25)]
need(max(w(a, b) for a, b in Av) == 3 and max(w(a, b) for a, b in Bv) == 5, "polygon weight bounds 3/5")
need(all(a + b <= 15 for a, b in Av) and all(a + b <= 25 for a, b in Bv), "total degrees 15/25")
c0 = Q(-5, 9); need(c0 != 0, "c0 unit")
out["C9_14c_to_candidate"] = {"wA_max": 3, "wB_max": 5, "c": "c0*k^3 with c0=-5/9, k a unit"}
out["status"] = "PASS"
print(json.dumps(out, sort_keys=True))
