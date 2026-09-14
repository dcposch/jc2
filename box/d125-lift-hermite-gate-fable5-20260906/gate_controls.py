#!/usr/bin/env python3
"""Fable 5.1 gate controls for the 97-pivot Hermite theorem. Standard library only.
Distinct from the producer: integer Bareiss determinants, unit x anti-triangular
factorisation of every block, own half-plane polygon census reproducing the
consumed 71/196/77/214/98/269 baseline, exponent law by repeated multiplication,
and a degree-12 symbolic-lambda fixture whose blocks are 1x1, 2x2 AND 3x3.
Run under timeout 30 / ulimit -t 25 -v 524288.  Negative controls via flags.
"""
import sys
from fractions import Fraction as Q
from math import comb

FLAGS = set(sys.argv[1:])
N = 0
def req(ok, name):
    global N
    if not ok:
        raise RuntimeError('FAIL ' + name)
    N += 1
    print('PASS', name)

# ---------- C1 exponent law by repeated multiplication, symbolic lambdas ----------
# lambda-polynomial: {(b,d): Fraction}; Laurent in (u,v): {(t,e): lampoly}
def lp_add(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, Q(0)) + v
    return {k: v for k, v in out.items() if v}
def lp_mul(a, b):
    out = {}
    for (b1, d1), c1 in a.items():
        for (b2, d2), c2 in b.items():
            k = (b1+b2, d1+d2)
            out[k] = out.get(k, Q(0)) + c1*c2
    return {k: v for k, v in out.items() if v}
def lp_scale(a, c):
    return {k: v*c for k, v in a.items() if v*c}
def L_mul(A, B):
    out = {}
    for (t1, e1), p1 in A.items():
        for (t2, e2), p2 in B.items():
            k = (t1+t2, e1+e2)
            out[k] = lp_add(out.get(k, {}), lp_mul(p1, p2))
    return {k: v for k, v in out.items() if v}
IMAGE = {(1, 4): {(0, 0): Q(1)}, (0, 2): {(1, 0): Q(-1)},
         (0, 1): {(0, 1): Q(-1)}, (0, -1): {(0, 0): Q(-1)}}
DTOY = 12
PIPOW = [{(0, 0): {(0, 0): Q(1)}}]
for _ in range(DTOY):
    PIPOW.append(L_mul(PIPOW[-1], IMAGE))
def phi_mono(i, j):
    return {(t, e-i): p for (t, e), p in PIPOW[j].items()}
law_ok = True
for i in range(DTOY+1):
    for j in range(DTOY+1-i):
        for (t, e), p in phi_mono(i, j).items():
            for (b, d), c in p.items():
                if e != 5*t+3*b+2*d-i-j:
                    law_ok = False
                if b == d == 0 and c != (-1)**(j-t)*comb(j, t):
                    law_ok = False
        # lambda-free negative part is exactly the derivative functional
        for t in range(j+1):
            e = 5*t-i-j
            got = phi_mono(i, j).get((t, e), {}).get((0, 0), Q(0))
            if got != (-1)**(j-t)*comb(j, t):
                law_ok = False
req(law_ok, 'C1 exponent e=5t+3b+2d-i-j and lambda-free coefficient (-1)^(j-t)C(j,t), all i+j<=12')

# ---------- C2 row bijection ----------
for D, want in ((15, 30), (25, 75)):
    st = {(s, t) for s in range(1, D+1) for t in range((s-1)//5+1)}
    te = {(t, e) for t in range((D-1)//5+1) for e in range(5*t-D, 0)}
    req(len(st) == want and {(t, 5*t-s) for (s, t) in st} == te,
        f'C2 D{D}: (s,t) rows biject with negative support, {want} rows')
req(sum((s+4)//5 for s in range(1, 15)) == 27 and sum((s+4)//5 for s in range(1, 25)) == 70,
    'C2 27+70 lower pivots, 3+5 top rows, total 105')

# ---------- C3 own polygon census (hand-written half planes) ----------
def poly_pts(case, D):
    pts = []
    for i in range(D+1):
        for j in range(D+1-i):
            if case == 'unequal':
                ok = (5*i-7*j <= 3 and 2*j >= i) if D == 15 else (5*i-7*j <= 5)
            elif case == 'common3':
                ok = i-j <= (3 if D == 15 else 5)
            else:
                ok = i <= (9 if D == 15 else 15)
            if ok:
                pts.append((i, j))
    return pts
def inner_val(case, i, j):
    return {'unequal': 5*i-7*j, 'common3': i-j, 'common4': i}[case]
INNERMAX = {('unequal', 15): 3, ('unequal', 25): 5, ('common3', 15): 3, ('common3', 25): 5,
            ('common4', 15): 9, ('common4', 25): 15}
BASE = {'unequal': (71, 196), 'common3': (77, 214), 'common4': (98, 269)}
RAW = {'unequal': (83, 215), 'common3': (94, 241), 'common4': (115, 296)}
TOTAL = {'unequal': 269, 'common3': 295, 'common4': 371}
for case in ('unequal', 'common3', 'common4'):
    frees = []
    for D in (15, 25):
        pts = poly_pts(case, D)
        req(len(pts) == RAW[case][0 if D == 15 else 1], f'C3 {case} D{D}: raw lattice count')
        outer = {p for p in pts if sum(p) == D}
        inner = {p for p in pts if inner_val(case, *p) == INNERMAX[(case, D)]}
        free = set(pts) - outer - inner - {(0, 0)}
        frees.append(len(free))
        pivots = {(i, s-i) for s in range(1, D) for i in range((s+4)//5)}
        if '--mutate-pivot' in FLAGS:
            pivots.add((D-1, 1) if case != 'common4' else (9, 1))
        req(pivots <= free, f'C3 {case} D{D}: all pivots are free unknowns (not face/origin/outside)')
        # face lattice points fully fixed, incl. zero positions: pivots never touch the face lines
        req(all(inner_val(case, *p) < INNERMAX[(case, D)] and sum(p) < D and p[0] >= 0 for p in pivots),
            f'C3 {case} D{D}: pivots strictly between inner and outer face lines')
    req(tuple(frees) == BASE[case], f'C3 {case}: free baseline {BASE[case]} reproduced')
    extra = 2 + (2 if case != 'unequal' else 0)
    req(sum(frees)+extra == TOTAL[case] and TOTAL[case]-97 == {'unequal': 172, 'common3': 198, 'common4': 274}[case],
        f'C3 {case}: {TOTAL[case]} incl. lambdas(+c,z) and {TOTAL[case]-97} after 97 pivots')

# ---------- C4 determinants: Bareiss + unit x antitriangular factorisation ----------
def bareiss(M):
    a = [row[:] for row in M]; n = len(a); sign = 1; prev = 1
    for k in range(n-1):
        if a[k][k] == 0:
            sw = next((r for r in range(k+1, n) if a[r][k] != 0), None)
            if sw is None:
                return 0
            a[k], a[sw] = a[sw], a[k]; sign = -sign
        for i in range(k+1, n):
            for j in range(k+1, n):
                a[i][j] = (a[i][j]*a[k][k] - a[i][k]*a[k][j]) // prev
        prev = a[k][k]
    return sign*a[n-1][n-1]
def matmul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def taylor_pow(k, r):
    """coefficients of (w-1)^k mod w^r, i.e. z^k expanded at z=-1 (w=z+1), by Horner."""
    c = [1] + [0]*(r-1)
    for _ in range(k):
        c = [(c[t-1] if t else 0) - c[t] for t in range(r)]
    return c
def Mmat(s, r):
    return [[(-1)**(s-i-t)*comb(s-i, t) for i in range(r)] for t in range(r)]
def Minv(s, r):
    M = Mmat(s, r); det = bareiss(M)
    n = r; inv = []
    # adjugate via cofactors
    for i in range(n):
        inv.append([])
        for j in range(n):
            minor = [[M[a][b] for b in range(n) if b != i] for a in range(n) if a != j]
            cof = (-1)**(i+j) * (bareiss(minor) if minor else 1)
            inv[i].append(cof*det)   # det = +-1 so inverse = adj/det = adj*det
    return inv
for s in range(1, 25):
    r = (s+4)//5
    M = Mmat(s, r)
    if '--mutate-sign' in FLAGS:
        M = [[comb(s-i, t) for i in range(r)] for t in range(r)]
    want = (-1)**(r*s + r*(r-1)//2)
    # (a) column i is the Taylor expansion of z^(s-i) at -1: independent Horner shift
    col_ok = all(taylor_pow(s-i, r)[t] == M[t][i] for i in range(r) for t in range(r))
    # (b) M = U * T with U = multiplication by z^(s-r+1) in Z[w]/(w^r) (unit, lower-triangular
    #     Toeplitz, diagonal (-1)^(s-r+1)) and T = Taylor matrix of z^(r-1-i) (anti-triangular, 1s)
    u = taylor_pow(s-r+1, r)
    U = [[u[t-k] if t >= k else 0 for k in range(r)] for t in range(r)]
    T = [[taylor_pow(r-1-i, r)[t] for i in range(r)] for t in range(r)]
    fac_ok = matmul(U, T) == M and all(U[t][t] == (-1)**(s-r+1) for t in range(r)) \
        and all(T[t][i] == (1 if t == r-1-i else 0) for i in range(r) for t in range(r) if t >= r-1-i)
    detU = (-1)**((s-r+1)*r); detT = (-1)**(r*(r-1)//2)
    d = bareiss(M)
    inv = Minv(s, r)
    ident = [[1 if i == j else 0 for j in range(r)] for i in range(r)]
    req(col_ok and fac_ok and d == want == detU*detT and matmul(M, inv) == ident
        and all(isinstance(x, int) for row in inv for x in row),
        f'C4 s={s} r={r}: Bareiss det={d}=(-1)^(rs+r(r-1)/2), U*T factorisation, integer inverse')

# ---------- C5 top faces: exact root order at z=-1, both fields ----------
# Z[rho] pairs (a,b) = a+b*rho, rho^2 = 3rho-1
def rm(x, y):
    a, b = x; c, d = y
    return (a*c - b*d, a*d + b*c + 3*b*d)
def ra(x, y): return (x[0]+y[0], x[1]+y[1])
def pmul(f, g):
    out = [(0, 0)]*(len(f)+len(g)-1)
    for i, x in enumerate(f):
        for j, y in enumerate(g):
            out[i+j] = ra(out[i+j], rm(x, y))
    return out
def ppow(f, k):
    out = [(1, 0)]
    for _ in range(k):
        out = pmul(out, f)
    return out
def shift_m1(f):   # coefficients in w = z+1
    out = [(0, 0)]*len(f)
    for k, c in enumerate(f):
        for t in range(k+1):
            out[t] = ra(out[t], rm(c, ((-1)**(k-t)*comb(k, t), 0)))
    return out
Z = [(1, 0)]
h_rat = pmul([(0, 0), (0, 0), (1, 0)], [(1, 0), (0, 0), (0, 0), (1, 0)])          # z^2(z^3+1)
h_gold = pmul(pmul([(0, 0), (0, 0), (1, 0)], [(1, 0), (1, 0)]), ppow([(1, -1), (1, 0)], 2))  # z^2(z+1)(z+1-rho)^2
for name, h in (('rational', h_rat), ('golden', h_gold)):
    if '--mutate-top' in FLAGS:
        h = pmul([(0, 0), (0, 0), (1, 0)], [(1, 0), (0, 0), (1, 0)])  # z^2(z^2+1): no root at -1
    for k, D in ((3, 15), (5, 25)):
        f = ppow(h, k)
        req(len(f) == D+1, f'C5 {name} h^{k} has degree {D}')
        w = shift_m1(f)
        req(all(w[t] == (0, 0) for t in range(k)) and w[k] != (0, 0),
            f'C5 {name} h^{k} vanishes to order exactly {k} at -1: top {k} rows identically zero')

# ---------- C6 degree-12 symbolic-lambda fixture, blocks 1x1/2x2/3x3 ----------
def lift(coef):
    """coefficients may be Fractions or lambda-polynomial dicts (solved pivots)."""
    out = {}
    for (i, j), c in coef.items():
        cp = c if isinstance(c, dict) else {(0, 0): c}
        for k, p in phi_mono(i, j).items():
            out[k] = lp_add(out.get(k, {}), lp_mul(p, cp))
    return {k: v for k, v in out.items() if v}
def neg_rows(coef):
    return {k: v for k, v in lift(coef).items() if k[1] < 0}
def rng(seed):
    x = seed
    while True:
        x = (1103515245*x + 12345) % 2**31
        yield x % 11 - 5
def fixture(seed, top=None):
    coef = {}
    # fixed top: z^9 (z+1)^3, triple root at -1  (r_12 = 3 top rows)
    topc = top or {(12-j, j): Q(comb(3, j-9)) for j in range(9, 13)}
    coef.update(topc)
    g = rng(seed)
    for s in range(1, DTOY):
        r = (s+4)//5
        for i in range(r, s+1):
            coef[(i, s-i)] = Q(next(g))
    return coef
def solve_pivots(coef, sign_mut=False):
    coef = dict(coef)
    for s in range(DTOY-1, 0, -1):
        r = (s+4)//5
        for i in range(r):
            coef[(i, s-i)] = Q(0)
        rows = neg_rows(coef)
        rhs = [rows.get((t, 5*t-s), {}) for t in range(r)]
        inv = Minv(s, r)
        if sign_mut:
            inv = [[abs(x) for x in row] for row in inv]
        for i in range(r):
            val = {}
            for t in range(r):
                val = lp_add(val, lp_scale(rhs[t], Q(-inv[i][t])))
            coef[(i, s-i)] = val    # lambda-polynomial pivot value
    return coef
lift_lp = lift
base = fixture(7)
sol = solve_pivots(base, sign_mut='--mutate-inverse' in FLAGS)
neg = {k: v for k, v in lift_lp(sol).items() if k[1] < 0}
req(not neg, 'C6 D12 fixture: all 21 negative rows vanish identically in K[lambda2,lambda3]')
piv = {k: v for k, v in sol.items() if isinstance(v, dict)}
req(len(piv) == sum((s+4)//5 for s in range(1, 12)) == 18, 'C6 D12: 18 pivots eliminated (1x1,2x2,3x3 blocks)')
req(all(c.denominator == 1 for v in piv.values() for c in v.values()),
    'C6 D12: pivot graph values are polynomials in lambdas with INTEGER coefficients (no denominators)')
req(any(len(v) > 1 for v in piv.values()) and any((b, d) != (0, 0) for v in piv.values() for (b, d) in v),
    'C6 D12: graph values are genuinely lambda-dependent (nontrivial F_{s,t})')
# affine-linearity in the retained coefficients: pivot(N1+N2)-pivot(N1)-pivot(N2)+pivot(0)=0
f1, f2 = fixture(7), fixture(19)
f0 = {k: (v if sum(k) == 12 else Q(0)) for k, v in f1.items()}
f12 = {k: (v if sum(k) == 12 else v + f2[k]) for k, v in f1.items()}
p0, p1, p2, p12 = (solve_pivots(f) for f in (f0, f1, f2, f12))
lin_ok = all(lp_add(lp_add(p12[k], lp_scale(p1[k], Q(-1))), lp_add(lp_scale(p2[k], Q(-1)), p0[k])) == {}
             for k in piv)
req(lin_ok, 'C6 D12: graph is affine-linear in retained coefficients over Z[lambda2,lambda3]')
# top rows identically zero with the fixed top, independent of lower data
top_only = {k: v for k, v in base.items() if sum(k) == 12}
tr = neg_rows(top_only)
req(all((t, 5*t-12) not in tr for t in range(3)) and all(e > 5*t-12 for (t, e) in tr) and tr,
    'C6 D12: three top rows (s=12,t=0,1,2) vanish identically; top lambda-terms land only at rows with s<12')
bad_top = fixture(7, top={(12-j, j): Q(comb(2, j-10)) for j in range(10, 13)})  # z^10(z+1)^2: double root only
trb = neg_rows({k: v for k, v in bad_top.items() if sum(k) == 12})
req((2, -2) in trb and (0, -12) not in trb and (1, -7) not in trb,
    'C6 negative control: double-root top leaves exactly the t=2 top row nonzero among the three')
# actual-object mutation: perturb one retained coefficient after solving
mut = dict(sol); mut[(3, 5)] = mut[(3, 5)] + 1
negm = {k: v for k, v in lift_lp(mut).items() if k[1] < 0}
req(negm and min(k[1] for k in negm) >= -8 and (0, -8) in negm,
    'C6 negative control: changing retained (3,5) by 1 breaks negative rows at levels <= 8 only')
mut1 = dict(sol); mut1[(1, 0)] = mut1[(1, 0)] + 1      # retained degree-1 coefficient
neg1 = {k: v for k, v in lift_lp(mut1).items() if k[1] < 0}
req(neg1 == {(0, -1): {(0, 0): Q(1)}}, 'C6 negative control: changing retained (1,0) by 1 breaks exactly the row (s,t)=(1,0)')
if '--mutate-drop-row' in FLAGS:
    neg1.pop((0, -1))
req(bool(neg1), 'C6 complete verifier rejects the mutated object; dropping that actual row would accept it (drop-row control)')
print(f'ALL {N} PASS: gate controls only; no production expansion, point, properness or JC2 claim')
