#!/usr/bin/env python3
"""
moh_skeleton_N.py -- the geometric degree N on a Moh skeleton.

Lane N-ON-THE-TREE (opus5, 2026-09-02).  Standard library + sympy.  FAIL-CLOSED:
every control must pass before any filter number is printed; any failure aborts
with exit code 1 and no filter output.

WHAT IT COMPUTES
  (1) CONTACT-DEFICIENCY   N = deg_x Res_y(f-c1, g-c2) = -sum_{i,j} ord_t(tau_i-phi_j),
      t = 1/x, for f,g monic in y with deg = deg_y.  Positive + NEGATIVE controls.
  (2) THEOREM FRONTIER-N   N = sum_{i=1..n} max(0, -lambda_f(delta^0_i)) where
      lambda_h^{(i)}(delta) = sum_j min(delta, ord_t(rho_i - (root j of h))) and
      delta^0_i is the level where lambda_g^{(i)} reaches 0.  This is the pairing
      written on the tree of the roots of f*g ALONE (no c-shift).  Verified.
  (3) Moh's tower recursion (Def 5.1(1)-(4), Prop 5.3): delta_i, the root counts
      a_i (of g) and b_i (of f=T_1) in D_i, and the order function
      lambda_g(delta_i) = ord_t g(sigma_i).  Positive control = Moh's sec.6 table.
  (4) THEOREM N-CEILING    N <= U(skeleton) := u*d*(-lambda_g(delta_1))^+ , with
      u = V_s*K/d_s the multiplicity of the major linear factor of the top form.
  (5) The census of numerical skeletons with all admissible V-assignments, and
      the filter U >= 2 (unconditional) / U >= 4 (campaign H2 residual 4<=N<=16).

Moh = T.T. Moh, J. reine angew. Math. 340 (1983) 140-212; text references are to
the pdftotext -layout extraction in box/depth-drivers-20260902/moh.txt.
"""
import sys, time, argparse
from fractions import Fraction as F
from math import gcd

FAILURES = []
def check(name, cond, detail=""):
    if cond: print(f"  [ok]   {name}")
    else:    print(f"  [FAIL] {name}   {detail}"); FAILURES.append(name)

# ===========================================================================
# PART 0.  exact Puiseux roots at t = 1/x, and the ultrametric order
# ===========================================================================
INF = F(10**9)          # stands for +infinity in the order lattice

def ord_diff(r1, r2):
    """ord_t(r1-r2) for roots given as {exponent-in-x : coeff}; ord_t = -exp_x."""
    from sympy import simplify
    for e in sorted(set(r1) | set(r2), reverse=True):
        if simplify(r1.get(e, 0) - r2.get(e, 0)) != 0:
            return -e
    return INF

def lam(delta, ords):
    """lambda(delta) = sum_j min(delta, ord_j)."""
    return sum(min(delta, o) for o in ords)

def frontier(ords):
    """least delta with lam(delta,ords) = 0.  lam is continuous, piecewise linear,
       nondecreasing, lam(-1) = -len(ords) and slope #{o > delta} >= 1 here."""
    lo = F(-1); cur = lam(lo, ords)
    assert cur <= 0
    for nxt in sorted(set(o for o in ords if o < INF)) + [INF]:
        if nxt <= lo: continue
        slope = sum(1 for o in ords if o > lo)
        assert slope > 0, "lambda saturates below 0: g has a repeated root"
        if nxt >= INF or cur + slope*(nxt-lo) >= 0:
            return lo + F(-cur, 1)/slope
        cur += slope*(nxt-lo); lo = nxt
    raise AssertionError("no frontier")

# ---- explicit two-tower families: factor (a,p,b,q) = (y-a*x)^p - b*x^q --------
def _factor(a, p, b, q):
    from sympy import expand, symbols
    x, y = symbols('x y')
    return expand((y - a*x)**p - b*x**q)

def _roots(a, p, b, q):
    from sympy import sympify, Rational, exp, pi, I
    return [{F(1,1): sympify(a), F(q,p): (sympify(b)**Rational(1,p))*exp(2*pi*I*Rational(k,p))}
            for k in range(p)]

def build(spec):
    from sympy import expand
    poly = 1
    for t in spec: poly = expand(poly*_factor(*t))
    return poly, [r for t in spec for r in _roots(*t)]

def deg_x_res(f, g, c1, c2):
    from sympy import symbols, Poly, resultant, expand, degree
    x, y = symbols('x y')
    R = expand(resultant(Poly(expand(f-c1), y), Poly(expand(g-c2), y), y).as_expr())
    return None if R == 0 else int(degree(R, x))

# ===========================================================================
# PART 1 + 2.  controls for CONTACT-DEFICIENCY and FRONTIER-N
# ===========================================================================
TWO_TOWER = [   # (f-spec, g-spec) -- non-Keller, both monic in y with deg = deg_y
    ([(1,1,3,0),(2,1,5,0)],  [(1,2,7,1),(2,1,11,0)]),
    ([(1,2,3,1),(2,1,5,0)],  [(1,2,7,1),(2,2,11,1)]),
    ([(1,2,3,1),(2,2,5,1)],  [(1,3,7,2),(2,1,11,0)]),
    ([(1,1,3,0),(2,2,5,1)],  [(1,2,7,1),(2,2,11,1)]),
    ([(1,3,3,2),(2,1,5,0)],  [(1,3,7,1),(2,1,11,0)]),
    ([(1,2,3,1),(2,2,5,1)],  [(1,4,7,2),(2,2,11,1)]),
    ([(1,2,3,1),(2,2,3,1)],  [(1,3,3,1),(2,3,3,1)]),
]

def controls_pairing():
    from sympy import symbols, Rational, expand
    x, y = symbols('x y')
    c1, c2 = Rational(7,3), Rational(-5,2)
    print("\n-- CONTROL 1: N = deg_x Res_y = -sum ord_t(tau-phi)  (monic, deg=deg_y) --")
    print(f"   {'f-spec':30} {'g-spec':30} {'m':>3} {'n':>3} {'Nres':>5} {'Npair':>6} {'Nfront':>7}")
    for (fs, gs) in TWO_TOWER:
        f, phis = build(fs); g, taus = build(gs)
        m, n = len(phis), len(taus)
        Nres = deg_x_res(f, g, c1, c2)
        Npair = -sum(ord_diff(tt, pp) for tt in taus for pp in phis)
        Nfr = F(0)
        for rho in taus:
            og = [ord_diff(rho, r) for r in taus]
            of = [ord_diff(rho, r) for r in phis]
            Nfr += max(F(0), -lam(frontier(og), of))
        print(f"   {str(fs):30} {str(gs):30} {m:3} {n:3} {Nres:5} {str(Npair):>6} {str(Nfr):>7}")
        check(f"pairing  {fs}/{gs}", F(Nres) == Npair, f"{Nres} vs {Npair}")
        check(f"frontier {fs}/{gs}", F(Nres) == Nfr,  f"{Nres} vs {Nfr}")

    print("\n-- CONTROL 2: gauge hypothesis is load-bearing (positive + NEGATIVE) --")
    rows = [   # (label, f, g, true N, gauge-ok?)
      ("automorphism (y, x+y^k), k=5", y, x+y**5,          1, True),
      ("automorphism (y, x+y^7), k=7", y, x+y**7,          1, True),
      ("(x, x*y^m), m=2",             x, x*y**2,           2, False),
      ("(x, x*y^m), m=5",             x, x*y**5,           5, False),
      ("(x^3, y^2)",                  x**3, y**2,          6, False),
      ("psi_2 o (x,x y^2)  NEGATIVE", x+(x*y**2)**2, x*y**2, 2, False),
      ("psi_3 o (x,x y^3)  NEGATIVE", x+(x*y**3)**3, x*y**3, 3, False),
    ]
    print(f"   {'map':34} {'N(true)':>8} {'deg_x Res':>10}  gauge")
    for (lab, f, g, Ntrue, ok) in rows:
        d = deg_x_res(f, g, c1, c2)
        print(f"   {lab:34} {Ntrue:8} {str(d):>10}  {'deg=deg_y monic' if ok else 'NOT in gauge'}")
        if ok:
            check(f"gauge control {lab}", d == Ntrue, f"{d} vs {Ntrue}")
    dneg = deg_x_res(x+(x*y**2)**2, x*y**2, c1, c2)
    check("NEGATIVE control: resultant identity FAILS off gauge", dneg != 2,
          f"deg_x Res = {dneg}, N = 2")

# ===========================================================================
# PART 3.  Moh's tower recursion
# ===========================================================================
class Skel:
    """A Moh skeleton: (n, m, [M_2..M_s], {i: V_i}).  M_1 = -m, M_s = n-2,
       V_{s+1} = d_{s+1}.  Def 5.1(1)-(3) of Moh 1983 (moh.txt p.179)."""
    def __init__(self, n, m, Ms, Vs):
        self.n, self.m = n, m
        full = [-m] + list(Ms)
        self.s = s = len(full)
        self.M = {i+1: full[i] for i in range(s)}
        d = [n]
        for M in full: d.append(gcd(d[-1], M))
        self.d = {i+1: d[i] for i in range(len(d))}
        self.V = dict(Vs); self.V[s+1] = self.d[s+1]
        self.K = self.d[2]; self.e = n//self.K; self.dd = m//self.K
        self.delta = {i: self._delta(i) for i in range(1, s+1)}
        self.a = {i: n*self.V[i+1]//self.d[i+1] for i in range(1, s+1)}
        self.b = {i: m*self.V[i+1]//self.d[i+1] for i in range(1, s+1)}
        self.u = F(self.V[s]*self.K, self.d[s])       # top form  L_1^u L_2^v
        self.v = self.K - self.u

    def _delta(self, i):                              # Def 5.1(3)
        n, M, d, V, s = self.n, self.M, self.d, self.V, self.s
        num = F(n-M[i]); den = F(n-M[s]-1)
        for j in range(i+1, s+1):
            num *= (V[j]*(n-M[j]) - d[j]); den *= (V[j]*(n-M[j-1]) - d[j])
        return 1 - num/den

    def lam_g(self, r):
        """ord_t g(sigma) at the general point of D_r:  -n + int_{-1}^{delta_r} a."""
        out = F(-self.n)
        for i in range(r, self.s): out += self.a[i]*(self.delta[i]-self.delta[i+1])
        return out

    def lam_g_closed(self, r):
        """closed form  -n + n*sum_{j=r+1}^{s} V_j (M_j-M_{j-1}) R_j / Q_j ."""
        n, M, d, V, s = self.n, self.M, self.d, self.V, self.s
        tot = F(0)
        for j in range(r+1, s+1):
            R = F(1)
            for k in range(j+1, s+1):
                R *= F(V[k]*(n-M[k])-d[k], V[k]*(n-M[k-1])-d[k])
            tot += F(V[j]*(M[j]-M[j-1]), 1)*R/(V[j]*(n-M[j-1])-d[j])
        return -n + n*tot

    def lam_f(self, r): return F(self.m, self.n)*self.lam_g(r)

    def lam_g_radius(self, r):
        """THEOREM RADIUS-ORDER:  lambda_g(delta_r) = -n(1-delta_r)(n-M_s-1)/(n-M_r).
           With M_s = n-2 this is -n(1-delta_r)/(n-M_r): Moh's logarithmic radius and
           the order of g at the general point of D_r are ONE datum."""
        return -F(self.n*(1-self.delta[r])*(self.n-self.M[self.s]-1), self.n-self.M[r])

    def N_upper_closed(self):
        """U = u*d*e*(1-delta_1)/(d+e)  -- N-CEILING in closed form."""
        if self.delta[1] >= 1: return F(0)
        return F(self.u*self.dd*self.e, self.dd+self.e)*(1-self.delta[1])

    def N_upper(self):
        """THEOREM N-CEILING:  N <= a_{s-1} * (-lambda_f(delta_1))^+ = u*d*(-lambda_g(delta_1))^+."""
        lg = self.lam_g(1)
        return self.u*self.dd*(-lg) if lg < 0 else F(0)

    def windows_ok(self):                             # Def 5.1(2) / Prop 5.3
        for i in range(2, self.s+1):
            lo = F(self.d[i], self.n-self.M[i]); hi = F(self.V[i+1]*self.d[i], self.d[i+1])
            if not (self.V[i] > lo and self.V[i] <= hi): return False
        return True

def top_of_window_V(n, m, Ms, Vs_top):
    """The V-assignment with V_s = Vs_top and every lower V_i at the top of its
       Def 5.1(2) window.  MEASURED (control below): -lambda_g(delta_1), hence U,
       is maximised there, so this realises the branch-robust bound U_rob."""
    full = [-m] + list(Ms); s = len(full)
    M = {i+1: full[i] for i in range(s)}
    d = [n]
    for Mi in full: d.append(gcd(d[-1], Mi))
    d = {i+1: d[i] for i in range(len(d))}
    V = {s+1: d[s+1], s: Vs_top}
    for i in range(s-1, 1, -1):
        hi = F(V[i+1]*d[i], d[i+1]); V[i] = hi.numerator//hi.denominator
        if V[i]*(n-M[i]) <= d[i]: return None          # window empty
    return {i: V[i] for i in range(2, s+1)}

def U_robust(n, m, Ms, Vs_top):
    V = top_of_window_V(n, m, Ms, Vs_top)
    if V is None: return None, None
    S = Skel(n, m, list(Ms), V)
    if not S.windows_ok(): return None, None
    return S.N_upper(), S

MOH_SURVIVORS = [
    (64,48,[52,62],{3:3,2:3}, "(64,48)",            (F(1,4), F(9,16))),
    (84,56,[64,82],{3:3,2:2}, "(84,56) M2=64,V2=2", (F(2,7), F(16,21))),
    (84,56,[72,82],{3:3,2:5}, "(84,56) M2=72,V2=5", (F(1,4), F(7,12))),
    (75,50,[55,73],{3:4,2:3}, "(75,50) V2=3",       None),
    (75,50,[55,73],{3:4,2:2}, "(75,50) V2=2",       None),
    (99,66,[77,97],{3:8,2:8}, "(99,66)",            (F(1,3), F(4,9))),
]

def controls_recursion():
    print("\n-- CONTROL 3: Moh sec.6 published delta columns (moh.txt:3325-3340) --")
    print(f"   {'row':22} {'delta_2':>8} {'delta_1':>8} {'published':>18}")
    for (n,m,Ms,Vs,lab,pub) in MOH_SURVIVORS:
        S = Skel(n,m,Ms,Vs)
        got = (S.delta[2], S.delta[1])
        print(f"   {lab:22} {str(got[0]):>8} {str(got[1]):>8} "
              f"{('%s , %s'%pub) if pub else 'OCR illegible (prediction)':>18}")
        if pub: check(f"delta table {lab}", got == pub, f"{got} vs {pub}")
        check(f"Def 5.1(2) windows {lab}", S.windows_ok())
        check(f"lambda_g closed form {lab}",
              all(S.lam_g(r) == S.lam_g_closed(r) for r in range(1, S.s+1)))
        check(f"delta_s = -1 {lab}", S.delta[S.s] == -1)
        check(f"u+v=K, u>v {lab}", S.u+S.v == S.K and S.u > S.v, f"u={S.u} v={S.v} K={S.K}")
        check(f"a_(s-1) = u*e {lab}", S.a[S.s-1] == S.u*S.e)
        check(f"b_i/a_i = m/n {lab}",
              all(F(S.b[i], S.a[i]) == F(m, n) for i in range(1, S.s+1)))
        check(f"lambda_g(delta_1) < 0 {lab}", S.lam_g(1) < 0, str(S.lam_g(1)))
        check(f"RADIUS-ORDER lam_g(d_r) = -n(1-d_r)/(n-M_r) {lab}",
              all(S.lam_g(r) == S.lam_g_radius(r) for r in range(1, S.s+1)))
        check(f"N-CEILING closed form u*d*e*(1-delta_1)/(d+e) {lab}",
              S.N_upper() == S.N_upper_closed(), f"{S.N_upper()} vs {S.N_upper_closed()}")

# ===========================================================================
# PART 4.  the census of numerical skeletons, and the V-assignments
# ===========================================================================
def divisor_chains(K, floor=4):
    out = []
    def rec(cur, ch):
        for dd in range(floor, cur):
            if cur % dd == 0: out.append(ch+[dd]); rec(dd, ch+[dd])
    rec(K, []); return out

def census(n, Kmin=16, with_V=True):
    """Enumerate (n, m, M_2..M_s) and (if with_V) the V-assignments.
       Conditions, all read firsthand from Moh / GGV:
         d_1 = n > d_2 = K > ... > d_s >= 4      Moh search (5) + Cor 6.1
         s >= 3                                  Moh Prop 5.5
         M_1 = -m, M_s = n-2                     Moh search (1),(2) + Prop 5.4/Lem 5.3
         m = K*d, n = K*e, gcd(d,e)=1, 2<=d<e    (LF)+(MIN)
         K >= 16                                 GGV Cor 6.6
         d_s/(n-M_i) < V_i <= V_{i+1} d_i/d_{i+1}, V_{s+1}=d_{s+1}   Def 5.1(2)
         V_s < d_s                               two points at infinity (delta_s = -1)
    """
    for K in range(Kmin, n//3+1):
        if n % K: continue
        e = n//K
        if e < 3: continue
        for ch in divisor_chains(K, 4):
            dfull = [n, K]+ch; dfull.append(gcd(dfull[-1], n-2))
            s = 2+len(ch)
            d = {i+1: dfull[i] for i in range(len(dfull))}
            dlist = ([K]+ch)[:-1]; tg = ch
            for dd in range(2, e):
                if gcd(dd, e) != 1: continue
                m = K*dd
                M = {1: -m, s: n-2}
                def Mrec(i, prev):
                    if i == s:
                        if prev < n-2: yield True
                        return
                    for Mi in range(prev+1, n-2):
                        if gcd(dlist[i-2], Mi) == tg[i-2]:
                            M[i] = Mi; yield from Mrec(i+1, Mi)
                for _ in Mrec(2, -m):
                    Ms = [M[i] for i in range(2, s+1)]
                    if not with_V:
                        yield (m, tuple(Ms), None); continue
                    V = {s+1: d[s+1]}
                    def Vrec(i):
                        if i == 1: yield None; return
                        lo = F(d[i], n-M[i]); hi = F(V[i+1]*d[i], d[i+1])
                        for w in range(lo.numerator//lo.denominator + 1,
                                       hi.numerator//hi.denominator + 1):
                            if w < 1: continue
                            if i == s and w >= d[s]: continue
                            V[i] = w; yield from Vrec(i-1)
                        V.pop(i, None)
                    for _ in Vrec(s):
                        yield (m, tuple(Ms), {i: V[i] for i in range(2, s+1)})

def controls_census():
    print("\n-- CONTROL 4: census calibrated against Moh sec.6 (moh.txt:3341-3344) --")
    cnt = len(set((m, Ms) for (m, Ms, _) in census(75, with_V=False)))
    m2 = len([M for M in range(-50, 73) if gcd(25, M) == 5])
    print(f"   (75,50): admissible M_2 with gcd(25,M_2)=5 : {m2}   "
          f"multiples of d_3=5 in [-50,74) : {len([M for M in range(-50,74) if M%5==0])}"
          f"   (Moh writes '25 possible values for M_2')")
    tot = 0
    for n in range(48, 101):
        tot += len(set((m, Ms) for (m, Ms, _) in census(n, with_V=False)))
    print(f"   (n,m,M) skeletons with n <= 100 : {tot}   (depth lane census2.py: 2410)")
    check("census reproduces the depth lane count 2410 at n<=100", tot == 2410, str(tot))
    check("Moh's 25 values for M_2 at (75,50) recovered as 25 multiples of d_3",
          len([M for M in range(-50, 74) if M % 5 == 0]) == 25)
    # every Moh survivor must appear in the census with its published V's
    for (n, m, Ms, Vs, lab, _) in MOH_SURVIVORS:
        found = any(mm == m and MM == tuple(Ms) and VV == Vs for (mm, MM, VV) in census(n))
        check(f"census contains Moh survivor {lab}", found)

def leading_form(poly):
    from sympy import symbols, Poly, expand
    x, y = symbols('x y')
    P = Poly(expand(poly), x, y); D = P.total_degree()
    return sum(c*x**mx*y**my for ((mx, my), c) in P.terms() if mx+my == D)

def controls_rejection():
    from sympy import symbols, expand, simplify, diff
    x, y = symbols('x y')
    print("\n-- CONTROL 5a: non-Keller two-tower rows at the FIRST Jacobian step --")
    print("   [l(f),l(g)] = 0 is forced by the Jacobian condition ((LF): l(f)=alpha H^d,")
    print("   l(g)=beta H^e).  Rows with [l(f),l(g)] != 0 die there; the rest die at the")
    print("   numerical conditions of the recursion.")
    print(f"   {'f-spec':30} {'g-spec':30} {'[lf,lg]':>9} {'J const?':>9}  first rejection")
    for (fs, gs) in TWO_TOWER:
        f, _ = build(fs); g, _ = build(gs)
        lf, lg = leading_form(f), leading_form(g)
        br = simplify(expand(diff(lf, x)*diff(lg, y) - diff(lf, y)*diff(lg, x)))
        J = simplify(expand(diff(f, x)*diff(g, y) - diff(f, y)*diff(g, x)))
        Jconst = (J.free_symbols == set())
        m = sum(t[1] for t in fs); n = sum(t[1] for t in gs)
        if br != 0: why = "(LF): [l(f),l(g)] != 0"
        elif gcd(n, m) < 16: why = f"K = gcd(m,n) = {gcd(n,m)} < 16 (GGV Cor 6.6)"
        else: why = "-"
        print(f"   {str(fs):30} {str(gs):30} {('0' if br==0 else '!=0'):>9} "
              f"{str(Jconst):>9}  {why}")
        check(f"non-Keller row rejected {fs}/{gs}", (not Jconst) and why != "-")
    """Control (5): automorphisms and non-Keller families are rejected."""
    print("\n-- CONTROL 5: rejection of N=1 (automorphisms) and non-Keller data --")
    rows = []
    for (nn, mm, lab) in [(5,1,"automorphism (y, x+y^5): n=5, m=1"),
                          (7,1,"automorphism (y, x+y^7): n=7, m=1"),
                          (12,1,"automorphism (y, x+y^12)"),
                          (4,2,"(x,y^2)-type n=4,m=2 (non-Keller two-tower)"),
                          (6,4,"non-Keller two-tower n=6, m=4"),
                          (4,4,"non-Keller two-tower n=4, m=4")]:
        K = gcd(nn, mm); reasons = []
        if K < 16: reasons.append(f"K=gcd(n,m)={K} < 16 (GGV Cor 6.6)")
        d2 = gcd(nn, mm)
        if d2 < 4: reasons.append(f"d_2={d2} < 4, so no chain d_2>...>d_s>=4 (Moh Cor 6.1)")
        if d2 <= 1: reasons.append("s = 1 < 3 (Moh Prop 5.5)")
        if mm >= nn: reasons.append("m >= n violates Moh search (1)")
        if K and nn % K == 0 and mm % K == 0:
            ee, ddd = nn//K, mm//K
            if not (2 <= ddd < ee): reasons.append(f"(d,e)=({ddd},{ee}) violates (MIN) 2<=d<e")
        rows.append((lab, reasons))
    for (lab, reasons) in rows:
        print(f"   {lab:44} rejected by: {reasons[0] if reasons else 'NOTHING'}")
        check(f"rejected: {lab}", len(reasons) > 0)

# ===========================================================================
# PART 5.  the filter
# ===========================================================================
def run_filter(nmax, nmin_geom=(2, 4), verbose_upto=100):
    """Two readings of the ceiling per skeleton.

    U_tower : the bound for ONE tower, i.e. for one row of Moh's search table.
    U_rob   : the BRANCH-ROBUST bound.  Only V_s is a global datum of the pair
              (it is the multiplicity split u:v of the top form); V_{s-1},...,V_2
              are per-branch, and a pair may carry several inequivalent major
              branches.  Since the total number of g-roots in bottom-major discs
              is <= a_{s-1} = u*e whatever the branch mix, the branch-robust bound
              is  U_rob(n,m,M_*,V_s) = u*d*max over (V_{s-1}..V_2) of (-lambda_g(delta_1))^+.
    Kills are computed on U_rob (the weaker, safe one).
    """
    print(f"\n== FILTER: N <= U(skeleton) = u*d*(-lambda_g(delta_1))^+ , n <= {nmax} ==")
    print(f"   kills on the BRANCH-ROBUST U_rob:  U_rob < {nmin_geom[0]}"
          f" (N>=2, unconditional: non-invertible)"
          f" | U_rob < {nmin_geom[1]} (N>=4, campaign H2 residual 4<=N<=16)")
    print(f"   {'n=D':>5} {'#(n,m,M)':>9} {'#V-skel':>10} {'#groups':>8} {'kill<2':>7} {'kill<4':>7}"
          f" {'min U_rob':>10} {'max U_tow':>12}")
    G = [0,0,0,0,0,0]; GMAX = F(0); GMIN = None; bigrow = None; smallrow = None
    killed = []
    t0 = time.time()
    for n in range(48, nmax+1):
        seen = set(); cV = 0; mx = F(0)
        groups = {}
        for (m, Ms, V) in census(n):
            cV += 1; seen.add((m, Ms))
            S = Skel(n, m, list(Ms), V)
            U = S.N_upper()
            if U > mx: mx = U; row = (n, m, Ms, tuple(V[i] for i in sorted(V)), U)
            key = (m, Ms, V[S.s])
            if key not in groups or U > groups[key][0]:
                groups[key] = (U, tuple(V[i] for i in sorted(V)))
        if not cV: continue
        k2 = sum(1 for (U, _) in groups.values() if U < nmin_geom[0])
        k4 = sum(1 for (U, _) in groups.values() if U < nmin_geom[1])
        k0 = sum(1 for (U, _) in groups.values() if U <= 0)
        mnr = min(U for (U, _) in groups.values())
        for key, (U, Vt) in groups.items():
            if U < nmin_geom[1]: killed.append((n, key[0], key[1], key[2], Vt, U))
        G[0] += len(seen); G[1] += cV; G[2] += len(groups); G[3] += k0; G[4] += k2; G[5] += k4
        if mx > GMAX: GMAX = mx; bigrow = row
        if GMIN is None or mnr < GMIN: GMIN = mnr; smallrow = (n, mnr)
        if n <= verbose_upto or n % 8 == 0:
            print(f"   {n:5} {len(seen):9} {cV:10} {len(groups):8} {k2:7} {k4:7} "
                  f"{str(mnr):>10} {str(mx):>12}")
    print(f"\n   TOTAL n<={nmax}: (n,m,M)={G[0]}  V-skeletons={G[1]}  "
          f"branch-robust groups (n,m,M,V_s)={G[2]}")
    print(f"   U_rob<=0 (would force N=0, impossible): {G[3]}")
    print(f"   U_rob<2  KILLED unconditionally:        {G[4]}")
    print(f"   U_rob<4  KILLED under H2 (4<=N<=16):    {G[5]}")
    print(f"   surviving groups at U_rob>=4:           {G[2]-G[5]}")
    print(f"   global min U_rob = {GMIN} at n = {smallrow[0] if smallrow else '-'}")
    print(f"   global max U_tower = {GMAX} (= {float(GMAX):.2f}) at {bigrow}")
    print(f"   wall {time.time()-t0:.1f}s")
    if killed:
        killed.sort(key=lambda r: (r[5], r[0]))
        print(f"\n   smallest killed groups (n, m, M_2..M_s, V_s, argmax V, U_rob):")
        for r in killed[:12]:
            print(f"      n={r[0]:4} m={r[1]:4} M={r[2]} V_s={r[3]} Vargmax={r[4]} U_rob={r[5]} ({float(r[5]):.3f})")
    return G, GMAX, GMIN

def survivors_report():
    print("\n== Moh's four n<=100 survivors: the skeleton and its N-ceiling ==")
    print("   U_tower uses Moh's published V (one row of his search table);  U_rob is the")
    print("   branch-robust maximum over the per-branch V_{s-1}..V_2 at fixed V_s.")
    print("   N range = [2, U] unconditional, [4, min(U,16)] under H2 (campaign residual).")
    print(f"   {'row':22} {'K':>3} {'(d,e)':>6} {'(u,v)':>8} {'1-delta_1':>10}"
          f" {'U_tower':>8} {'U_rob':>8} {'N in (H2)':>11} {'(u-v)de/(d+e)':>14}")
    for (n, m, Ms, Vs, lab, _) in MOH_SURVIVORS:
        S = Skel(n, m, Ms, Vs); U = S.N_upper()
        Ur, _s = U_robust(n, m, Ms, Vs[S.s])
        lo, hi = 4, min(int(Ur), 16)
        print(f"   {lab:22} {S.K:3} {'(%d,%d)'%(S.dd,S.e):>6} {'(%s,%s)'%(S.u,S.v):>8} "
              f"{str(1-S.delta[1]):>10} {('%.3f'%float(U)):>8} {('%.3f'%float(Ur)):>8} "
              f"{('[%d,%d]'%(lo,hi)):>11} {('%.3f'%float(F((S.u-S.v)*S.dd*S.e, S.dd+S.e))):>14}")

# ===========================================================================
def control_identities(nmax=100):
    print("\n-- CONTROL 6: RADIUS-ORDER and the closed N-CEILING, census-wide --")
    bad1 = bad2 = bad3 = tot = 0
    for n in range(48, nmax+1):
        for (m, Ms, V) in census(n):
            S = Skel(n, m, list(Ms), V); tot += 1
            if any(S.lam_g(r) != S.lam_g_radius(r) for r in range(1, S.s+1)): bad1 += 1
            if any(S.lam_g(r) != S.lam_g_closed(r) for r in range(1, S.s+1)): bad2 += 1
            if S.N_upper() != S.N_upper_closed(): bad3 += 1
    print(f"   {tot} V-skeletons: RADIUS-ORDER fails {bad1}, product form fails {bad2}, "
          f"closed N-CEILING fails {bad3}")
    check("RADIUS-ORDER holds census-wide", bad1 == 0)
    check("lambda_g product form holds census-wide", bad2 == 0)
    check("closed N-CEILING holds census-wide", bad3 == 0)

def control_fast_path(nmax=100):
    print("\n-- CONTROL 7: top-of-window V realises the branch-robust maximum --")
    bad = 0; tot = 0
    for n in range(48, nmax+1):
        groups = {}
        for (m, Ms, V) in census(n):
            S = Skel(n, m, list(Ms), V)
            key = (m, Ms, V[S.s])
            groups[key] = max(groups.get(key, F(-10**9)), S.N_upper())
        for (m, Ms, Vs), U in groups.items():
            tot += 1
            Uf, _ = U_robust(n, m, list(Ms), Vs)
            if Uf != U: bad += 1
    print(f"   groups compared (brute-force max over V vs top-of-window): {tot}, mismatches {bad}")
    check("fast path = brute-force branch-robust maximum", bad == 0, f"{bad}/{tot}")

def fast_filter(nmax, nmin_geom=(2, 4)):
    print(f"\n== FAST FILTER (branch-robust U_rob only), n <= {nmax} ==")
    print(f"   {'n=D':>5} {'#groups':>8} {'kill<2':>7} {'kill<4':>7} {'min U_rob':>11} {'max U_rob':>11} {'surv':>7}")
    T = [0,0,0]; GMIN = None; GMAX = F(0); minrow = None; maxrow = None
    empty_D = []
    t0 = time.time()
    for n in range(48, nmax+1):
        rows = []
        for (m, Ms, _) in census(n, with_V=False):
            full = [-m]+list(Ms); s = len(full)
            dch = [n]
            for Mi in full: dch.append(gcd(dch[-1], Mi))
            ds = dch[s-1]      # d_s ; dch = [d_1,...,d_{s+1}]
            for Vs in range(ds//2 + 1, ds):
                U, S = U_robust(n, m, list(Ms), Vs)
                if U is None: continue
                rows.append((U, m, Ms, Vs))
        if not rows: continue
        k2 = sum(1 for r in rows if r[0] < nmin_geom[0])
        k4 = sum(1 for r in rows if r[0] < nmin_geom[1])
        mn = min(rows)[0]; mx = max(rows)[0]
        T[0] += len(rows); T[1] += k2; T[2] += k4
        if GMIN is None or mn < GMIN: GMIN = mn; minrow = min(rows)
        if mx > GMAX: GMAX = mx; maxrow = max(rows)
        if k4 == len(rows): empty_D.append(n)
        print(f"   {n:5} {len(rows):8} {k2:7} {k4:7} {str(mn):>11} {str(mx):>11} {len(rows)-k4:7}")
    print(f"\n   TOTAL n<={nmax}: groups={T[0]}  killed(U<2)={T[1]}  killed(U<4)={T[2]}"
          f"  surviving={T[0]-T[2]}")
    print(f"   global min U_rob = {GMIN} ({float(GMIN):.3f}) at {minrow}")
    print(f"   global max U_rob = {GMAX} ({float(GMAX):.3f}) at {maxrow}")
    print(f"   degrees D with EVERY group killed under H2: {empty_D if empty_D else 'NONE'}")
    print(f"   wall {time.time()-t0:.1f}s")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nmax", type=int, default=100)
    ap.add_argument("--skip-pairing", action="store_true",
                    help="skip the sympy resultant controls (slow)")
    a = ap.parse_args()
    print("moh_skeleton_N.py -- N on a Moh skeleton (lane N-ON-THE-TREE)")
    print("=" * 78)
    if not a.skip_pairing: controls_pairing()
    controls_recursion(); controls_census(); controls_rejection()
    control_identities(100)
    control_fast_path(100)
    print("\n" + "=" * 78)
    if FAILURES:
        print(f"CONTROLS FAILED ({len(FAILURES)}): {FAILURES}"); sys.exit(1)
    print(f"ALL CONTROLS PASSED.")
    survivors_report()
    run_filter(min(a.nmax,100))
    fast_filter(a.nmax)

if __name__ == "__main__":
    main()
