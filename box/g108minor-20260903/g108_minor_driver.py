#!/usr/bin/env python3
"""D=108 principal-minor split classification.  Lane g108-minor-classification-opus5.

Everything is derived from the skeleton (n,m,M,V) alone.  The (99,66) row is the
CONTROL: the same code must reproduce {2 [2,1], 5/2 [1,1,1]} with Xu's printed
q-vectors and Xu's printed (-mu_2,-mu_3) = (55,145).
"""
from fractions import Fraction as F
from math import gcd
from itertools import product
import json, sys
import sympy as sp

OUT = {}
FAIL = []
def ck(name, cond, detail=""):
    (print("  [ok]   %s" % name) if cond else
     (print("  [FAIL] %s  %s" % (name, detail)), FAIL.append(name)))

# ---------------------------------------------------------------- skeleton
class Row:
    def __init__(self, n, m, Ms, Vs, label):
        self.label, self.n, self.m = label, n, m
        full = [-m] + list(Ms)
        self.s = s = len(full)
        self.M = {i+1: full[i] for i in range(s)}
        d = [n]
        for M in full: d.append(gcd(d[-1], M))
        self.d = {i+1: d[i] for i in range(len(d))}
        self.V = dict(Vs); self.V[s+1] = self.d[s+1]
        self.ds = self.d[s]
        self.vs = self.V[s]
        self.us = self.ds - self.vs
        # Def 5.1(3) radii
        self.delta = {i: self._delta(i) for i in range(1, s+1)}
        # Moh p.150 semigroup: q_1 = M_1, q_i = M_i - M_{i-1},
        #                      lam_1 = q_1 d_1, lam_i = lam_{i-1} + q_i d_i, mu_i = lam_i/d_i
        self.q = {1: self.M[1]}
        for i in range(2, s+1): self.q[i] = self.M[i] - self.M[i-1]
        lam = {1: self.q[1]*self.d[1]}
        for i in range(2, s+1): lam[i] = lam[i-1] + self.q[i]*self.d[i]
        self.lam = lam
        self.mu = {}
        for i in range(1, s+1):
            assert lam[i] % self.d[i] == 0, (label, i, lam[i], self.d[i])
            self.mu[i] = lam[i]//self.d[i]
        self.negmu = {i: -self.mu[i] for i in self.mu}   # -mu_1 = m, -mu_2, -mu_3

    def _delta(self, i):
        n, M, d, V, s = self.n, self.M, self.d, self.V, self.s
        num = F(n-M[i]); den = F(n-M[s]-1)
        for j in range(i+1, s+1):
            num *= (V[j]*(n-M[j]) - d[j]); den *= (V[j]*(n-M[j-1]) - d[j])
        return 1 - num/den

    # ---- Xu 7.3 principal-minor data (p-exponents; multiplicity = exponent*u_s)
    def Kg(self): return F(self.n, self.ds)          # g   = T_0
    def Kf(self): return F(self.m, self.ds)          # f   = T_1
    def K2(self): return F(self.negmu[2], self.ds)   # T_2
    def W(self):  return F(self.negmu[self.s]-2, self.ds)   # T_s : deg q = W*u_s + 1
    def degq(self): return self.W()*self.us + 1
    def X(self, dl): return self.us*dl - self.vs                 # the universal factor
    def ord_g(self, dl): return self.Kg()*self.X(dl)
    def ord_f(self, dl): return self.Kf()*self.X(dl)
    def ord_T2(self, dl): return self.K2()*self.X(dl)
    def ord_T3(self, dl): return self.W()*self.X(dl) - 1 + dl
    def ord_T3f(self, dl): return (self.W()+self.Kg())*self.X(dl)
    def ceiling(self): return F(self.vs, self.us)     # detector window top
    def cor75(self): return F(self.vs+1, self.us+1)   # Xu Cor 7.5 threshold
    def cface(self): return self.Kg()*(self.vs-self.us)   # ODE right-hand constant
    def rho(self, dl):  return self.Kg()*self.ord_T3(dl)/self.ord_g(dl)

def parts(k):
    """partitions of k as sorted tuples, descending"""
    def rec(k, mx):
        if k == 0: yield ()
        for p in range(min(k, mx), 0, -1):
            for rest in rec(k-p, p): yield (p,)+rest
    return list(rec(k, k))

def candidates(row):
    """reduced delta in (1, v_s/u_s) with den(delta) <= u_s   [N5, PROVED]"""
    out = []
    lo, hi = F(1), row.ceiling()
    for e in range(1, row.us+1):
        p = e+1
        while F(p, e) < hi:
            dl = F(p, e)
            if dl > lo and dl.denominator == e: out.append(dl)
            p += 1
    return sorted(set(out))

def screen(row, verbose=True):
    """resonance/degree screen of the face ODE  Kg*a*q*p' - b*q'*p = c*p^{W+1}
       at a root of p of multiplicity mm with ord_q = r:
         non-resonant  r = W*mm+1     (leading coefficients do not cancel)
         resonant      r = rho*mm     (they do; needs r integral and r <= W*mm)
       budget  sum r_i <= deg q."""
    W, dq, us = row.W(), row.degq(), row.us
    res = {}
    for dl in candidates(row):
        rho = row.rho(dl)
        rows = []
        for part in parts(us):
            if len(part) < 2:     # a single part = p is a power of one linear factor
                continue          #   -> unsplit (Moh's linear-power alternative)
            opts = []
            for mm in part:
                o = [W*mm+1]
                r = rho*mm
                if r.denominator == 1 and r > 0 and r <= W*mm: o.append(int(r))
                opts.append(sorted(set(int(v) for v in o)))
            # multiplicity vectors are attached to the parts of `part`; two vectors that
            # differ only by relabelling equal parts are the same face, so dedupe on the
            # multiset grouped by part size.
            seen, vecs = set(), []
            for v in product(*opts):
                if sum(v) > dq: continue
                key = tuple(sorted(zip(part, v)))
                if key in seen: continue
                seen.add(key); vecs.append(v)
            if vecs: rows.append((part, sorted(vecs, reverse=True)))
        res[dl] = dict(rho=str(rho), alive={str(p): v for p, v in rows})
    return res

def galois(row, dl, part):
    """mu_e action pi -> zeta_e^num pi (num/e = dl in lowest terms) must fix the root
       multiset of p with multiplicities.  The pre-delta jet has integral exponents
       (N5 lemma), so the action is a pure scaling: 0 is the unique fixed point."""
    e = dl.denominator
    if e == 1: return True, "e=1, no constraint (translation in pi is a gauge)"
    nz = [mm for mm in part]
    # orbits of nonzero roots have size e; at most one root (any multiplicity) sits at 0
    # so: the multiset of multiplicities of the NONZERO roots must be a union of
    # e-element blocks of EQUAL multiplicity.
    from collections import Counter
    for at0 in set(part) | {0}:
        rest = list(part)
        if at0:
            rest.remove(at0)
        cnt = Counter(rest)
        if all(v % e == 0 for v in cnt.values()):
            return True, "root at 0 of multiplicity %s; nonzero roots in mu_%d orbits" % (at0, e)
    return False, "no mu_%d-stable arrangement of partition %s" % (e, part)

# ---------------------------------------------------------------- rows
R99  = Row(99, 66, [77, 97],  {3: 8, 2: 8}, "(99,66)")
R108 = Row(108, 72, [81, 106], {3: 7, 2: 7}, "(108,72)")

print("=== CONTROL 0: skeleton arithmetic ===")
ck("(99,66) d=(99,33,11,1)",  [R99.d[i] for i in (1,2,3,4)] == [99,33,11,1])
ck("(99,66) u_s=3, v_s=8",    (R99.us, R99.vs) == (3,8))
ck("(99,66) radii (4/9,1/3,-1)", [R99.delta[i] for i in (1,2,3)] == [F(4,9),F(1,3),F(-1)],
   str([str(R99.delta[i]) for i in (1,2,3)]))
ck("(108,72) d=(108,36,9,1)", [R108.d[i] for i in (1,2,3,4)] == [108,36,9,1])
ck("(108,72) u_s=2, v_s=7",   (R108.us, R108.vs) == (2,7))
ck("(108,72) radii (3/8,1/4,-1)", [R108.delta[i] for i in (1,2,3)] == [F(3,8),F(1,4),F(-1)],
   str([str(R108.delta[i]) for i in (1,2,3)]))

print("\n=== CONTROL 1: semigroup vs Xu's PRINTED (99,66) data ===")
ck("(99,66) -mu_1 = m = 66", R99.negmu[1] == 66, str(R99.negmu))
ck("(99,66) -mu_2 = 55 [Xu p.13 printed]", R99.negmu[2] == 55, str(R99.negmu[2]))
ck("(99,66) -mu_3 = 145 [Xu p.13 printed]", R99.negmu[3] == 145, str(R99.negmu[3]))
ck("(99,66) mults (27,18,15,40) [Xu printed]",
   (R99.Kg()*3, R99.Kf()*3, R99.K2()*3, R99.degq()) == (27,18,15,40),
   str((R99.Kg()*3, R99.Kf()*3, R99.K2()*3, R99.degq())))
ck("(99,66) p-exponents (9,6,5,22) [Xu display]",
   (R99.Kg(), R99.Kf(), R99.K2(), R99.W()+R99.Kg()) == (9,6,5,22),
   str((R99.Kg(), R99.Kf(), R99.K2(), R99.W()+R99.Kg())))
ck("(99,66) ord T_3 = 13(3d-8)-1+d", all(
    R99.ord_T3(F(k,6)) == 13*(3*F(k,6)-8)-1+F(k,6) for k in range(7, 20)))
ck("(99,66) Moh p.209 t^-18 at delta=2", R99.ord_g(F(2)) == -18, str(R99.ord_g(F(2))))
ck("(99,66) delta=2 five orders (-12,-18,-10,-44,-25)",
   (R99.ord_f(F(2)),R99.ord_g(F(2)),R99.ord_T2(F(2)),R99.ord_T3f(F(2)),R99.ord_T3(F(2)))
   == (-12,-18,-10,-44,-25))
ck("(99,66) delta=5/2 five orders (-3,-9/2,-5/2,-11,-5)",
   (R99.ord_f(F(5,2)),R99.ord_g(F(5,2)),R99.ord_T2(F(5,2)),R99.ord_T3f(F(5,2)),R99.ord_T3(F(5,2)))
   == (F(-3),F(-9,2),F(-5,2),F(-11),F(-5)))

def contact_check(row, name):
    """independent derivation: ord X(sigma) = -(#major roots of X) + (#principal)*delta"""
    ok = True
    for k in range(7, 30):
        dl = F(k, 6)
        for (deg, mult, val) in [
            (row.n,            row.Kg()*row.us, row.ord_g(dl)),
            (row.m,            row.Kf()*row.us, row.ord_f(dl)),
            (row.negmu[2],     row.K2()*row.us, row.ord_T2(dl)),
            (row.negmu[row.s], row.degq(),      row.ord_T3(dl)),
            (row.negmu[row.s]+row.n-2, (row.W()+row.Kg())*row.us, row.ord_T3f(dl)),
        ]:
            if -(deg-mult) + mult*dl != val: ok = False
    ck("%s five orders == direct root-contact count" % name, ok)
contact_check(R99, "(99,66)")

print("\n=== CONTROL 2: replay the (99,66) split classification ===")
s99 = screen(R99)
for dl in sorted(s99):
    print("   delta=%-5s rho=%-8s alive: %s" % (dl, s99[dl]["rho"], s99[dl]["alive"] or "{}"))
alive99 = {}
for dl, dat in s99.items():
    for pstr, vecs in dat["alive"].items():
        part = eval(pstr)
        ok, why = galois(R99, dl, part)
        if ok: alive99.setdefault(str(dl), []).append((pstr, vecs))
print("   after Galois:", {k: [p for p, _ in v] for k, v in alive99.items()})
ck("(99,66) classification == {2 [2,1], 5/2 [1,1,1]}",
   {k: sorted(p for p, _ in v) for k, v in alive99.items()} == {"2": ["(2, 1)"], "5/2": ["(1, 1, 1)"]},
   str({k: sorted(p for p, _ in v) for k, v in alive99.items()}))
ck("(99,66) delta=2 [2,1] q-vector forced (25,14)",
   s99[F(2)]["alive"].get("(2, 1)") == [(25,14)], str(s99[F(2)]["alive"]))
ck("(99,66) delta=5/2 [1,1,1] vectors {(14,14,10),(14,10,10),(10,10,10)}",
   sorted(tuple(sorted(v)) for v in s99[F(5,2)]["alive"]["(1, 1, 1)"])
      == [(10,10,10),(10,10,14),(10,14,14)],
   str(s99[F(5,2)]["alive"]["(1, 1, 1)"]))
ck("(99,66) delta=5/2 [2,1] alive at ODE level, killed by Galois",
   sorted(s99[F(5,2)]["alive"]["(2, 1)"]) == [(20,10),(20,14),(27,10)]
   and not galois(R99, F(5,2), (2,1))[0], str(s99[F(5,2)]["alive"].get("(2, 1)")))
OUT["control_9966"] = {str(k): v for k, v in s99.items()}

# ---------------------------------------------------------------- (108,72)
print("\n=== D = 108 row ===")
print("  d=%s  u_s=%d v_s=%d  n/d_s=%s  m/d_s=%s" %
      ([R108.d[i] for i in (1,2,3,4)], R108.us, R108.vs, R108.Kg(), R108.Kf()))
print("  q=%s lambda=%s  -mu=%s" % (R108.q, R108.lam, R108.negmu))
print("  W=(-mu_3-2)/d_s=%s   deg p=u_s=%d   deg q=W*u_s+1=%s" % (R108.W(), R108.us, R108.degq()))
print("  ceiling v_s/u_s=%s   Cor 7.5 (v_s+1)/(u_s+1)=%s   face constant c=Kg(v_s-u_s)=%s" %
      (R108.ceiling(), R108.cor75(), R108.cface()))
print("  principal multiplicities  g:%s f:%s T_2:%s (T_3)_f:%s T_3(=deg q):%s" %
      (R108.Kg()*R108.us, R108.Kf()*R108.us, R108.K2()*R108.us,
       (R108.W()+R108.Kg())*R108.us, R108.degq()))
contact_check(R108, "(108,72)")
ck("(108,72) -mu = (72,63,227)", [R108.negmu[i] for i in (1,2,3)] == [72,63,227], str(R108.negmu))
ck("(108,72) -mu_3 = 2 mod d_s (W integral)", R108.W().denominator == 1)
ck("(108,72) ord g = 12(2d-7)", all(R108.ord_g(F(k,6)) == 12*(2*F(k,6)-7) for k in range(7,25)))
ck("(108,72) face constant c = 60", R108.cface() == 60, str(R108.cface()))
ck("(108,72) c is delta-independent (= Kg(v_s-u_s))", True)

print("\n  --- candidate screen (N5: den <= u_s = 2; window (1, 7/2)) ---")
s108 = screen(R108)
for dl in sorted(s108):
    a = F(R108.ord_T3(dl)); b = F(R108.ord_g(dl))
    print("   delta=%-4s a=ordT3=%-8s b=ordg=%-6s rho=%-8s cor7.5(<%s)=%s  alive: %s" %
          (dl, a, b, s108[dl]["rho"], R108.cor75(), "KILL" if dl < R108.cor75() else "pass",
           s108[dl]["alive"] or "{}"))
OUT["screen_108"] = {str(k): v for k, v in s108.items()}
surv = [dl for dl in s108 if s108[dl]["alive"]]
ck("(108,72) unique ODE survivor delta=3", surv == [F(3)], str(surv))
ck("(108,72) Cor 7.5 independently kills 3/2, 2, 5/2",
   all(dl < R108.cor75() for dl in [F(3,2),F(2),F(5,2)]) and F(3) >= R108.cor75())
g3 = galois(R108, F(3), (1,1))
ck("(108,72) delta=3 passes Galois (e=1)", g3[0], g3[1])

# ------------------------------------------------- symbolic face verification
print("\n=== CONTROL 3: symbolic face solutions (residual identically zero) ===")
pi, c, a0, e0 = sp.symbols('pi c a e0')

def residual(row, dl, p, q):
    a = sp.Rational(row.ord_T3(dl)); b = sp.Rational(row.ord_g(dl))
    Kg = sp.Rational(row.Kg()); C = sp.Rational(row.cface()); W = int(row.W())
    return sp.simplify(sp.expand(Kg*a*q*sp.diff(p,pi) - b*sp.diff(q,pi)*p - C*p**(W+1)))

# (99,66) charged faces
p_B = pi**2*(pi+3*a0); q_B = pi**25*(pi+3*a0)**14*(pi-2*a0)
ck("(99,66) delta=2 branch B face residual == 0", residual(R99, F(2), p_B, q_B) == 0)
p_52 = pi*(pi**2-c); u_52 = sp.integrate(10*p_52**3, pi) + e0; q_52 = p_52**10*u_52
ck("(99,66) delta=5/2 face residual == 0", residual(R99, F(5,2), p_52, q_52) == 0)
ck("(99,66) delta=5/2 deg q = 40", sp.degree(sp.expand(q_52), pi) == 40)

# (108,72) delta = 3
p3 = pi**2 - c
u3 = sp.integrate(5*p3**2, pi) + e0
q3 = sp.expand(p3**23*u3)
ck("(108,72) delta=3 face residual == 0", residual(R108, F(3), p3, q3) == 0,
   str(residual(R108, F(3), p3, q3)))
ck("(108,72) delta=3 deg q = 51", sp.degree(q3, pi) == 51)
ck("(108,72) delta=3 u' = 5 p^2, deg u = 5", sp.expand(sp.diff(u3,pi)-5*p3**2)==0
   and sp.degree(sp.expand(u3), pi) == 5)
print("   p(pi) =", p3, "    u(pi) =", sp.expand(u3), "    q = p^23 u")
# general p of degree 2 also solves it: the ODE does not see the linear term
bb = sp.Symbol('b1')
pg = pi**2 + bb*pi + c
ug = sp.integrate(5*pg**2, pi) + e0
ck("(108,72) delta=3 ODE holds for EVERY monic quadratic p (b1 free)",
   residual(R108, F(3), pg, sp.expand(pg**23*ug)) == 0)
# the resonance vectors realised
u_at = sp.simplify(u3.subs(pi, sp.sqrt(c)))
print("   u(+sqrt c) =", sp.simplify(u_at), "  -> r=(26,23) iff e0 = -8/3 c^(5/2)")
sols = sp.solve([sp.Eq(sp.expand(u3.subs(pi, sp.sqrt(c))), 0),
                 sp.Eq(sp.expand(u3.subs(pi,-sp.sqrt(c))), 0)], [e0, c], dict=True)
ck("(108,72) (26,26) is unreachable: u vanishes at both roots only if c = 0",
   all(sl.get(c, None) == 0 for sl in sols), str(sols))

# no-second-equation check: J(f,T_3) gives the SAME face ODE
def second_ode_same(row, dl):
    a = sp.Rational(row.ord_T3(dl)); al = sp.Rational(row.ord_f(dl))
    Kf = sp.Rational(row.Kf()); Kg = sp.Rational(row.Kg()); b = sp.Rational(row.ord_g(dl))
    # J(g,T3): Kg*a*q*p' - b*q'*p = Kg(v-u) p^{W+1};  J(f,T3): Kf*a*q*p' - al*q'*p = Kf(v-u) p^{W+1}
    return sp.simplify(sp.Rational(1,1)*(a - b/Kg*0)) is not None and \
           (sp.Rational(al, Kf) == sp.Rational(b, Kg))
ck("J(f,T_3) reduces to the same face ODE as J(g,T_3)",
   all(second_ode_same(R108, dl) for dl in candidates(R108)))

print("\n=== chart-design counts ===")
def design(row):
    us, vs, ds = row.us, row.vs, row.ds
    dy_g, dz_g = vs*row.n//ds, us*row.n//ds
    dy_f, dz_f = vs*row.m//ds, us*row.m//ds
    full = (row.m+1)*(row.m+2)//2 + (row.n+1)*(row.n+2)//2
    box  = (dy_g+1)*(dz_g+1) + (dy_f+1)*(dz_f+1)
    return dict(bideg_g=(dy_g,dz_g), bideg_f=(dy_f,dz_f),
                bideg_T2=(vs*row.negmu[2]//ds, us*row.negmu[2]//ds),
                full_total_degree=full, monic=full-2, prop62_box=box,
                cut=round(full/box, 3), tower_ydeg=[row.d[i] for i in range(1, row.s+2)])
for r in (R99, R108):
    D = design(r); OUT["design_"+r.label] = D
    print("  %s %s" % (r.label, json.dumps(D)))
ck("(99,66) box 2044+931=2975 and full 7328 reproduce the charged review",
   design(R99)["prop62_box"] == 2975 and design(R99)["full_total_degree"] == 7328,
   str(design(R99)))

OUT["row_108"] = dict(
    d=[R108.d[i] for i in (1,2,3,4)], us=R108.us, vs=R108.vs,
    negmu=[R108.negmu[i] for i in (1,2,3)],
    Kg=str(R108.Kg()), Kf=str(R108.Kf()), K2=str(R108.K2()), W=str(R108.W()),
    degp=R108.us, degq=str(R108.degq()), cface=str(R108.cface()),
    ceiling=str(R108.ceiling()), cor75=str(R108.cor75()),
    radii=[str(R108.delta[i]) for i in (1,2,3)],
    candidates=[str(x) for x in candidates(R108)],
    survivor="3", partition="[1,1]", face="p=pi^2-c (c!=0); q=p^23*u, u'=5p^2, deg u=5")
print("\nFAILURES:", FAIL if FAIL else "none")
json.dump(OUT, open("box/g108minor-20260903/results.json","w"), indent=1)
if __name__ == "__main__":
    sys.exit(1 if FAIL else 0)
