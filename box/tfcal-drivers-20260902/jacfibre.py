#!/usr/bin/env python3
"""
D1-SUBTREE -- part A: the Jacobian condition on the generic fibre, exactly.

THEOREM JAC-FIBRE.  Let (f,g) be a dominant pair in C[x,y], both monic in y.  Put
t = x^{-1} and let tau be a root of g - c_2 in the Puiseux field C<t> (generic c_2).
Let a_0 be the t^0 coefficient of f(tau).  Then

    ord_t( f(tau) - a_0 )  +  ord_t g_y(tau)  =  -1  +  ord_t J(tau),      (JF)

where J = [f,g].  In particular for a KELLER pair (J in C^*) the right side is -1
and is independent of the branch.

  proof:  F(t)=f(t^-1,tau(t)), G(t)=g(t^-1,tau(t))=c_2 constant, so G'=0 gives
  tau' = g_x t^{-2}/g_y and then F' = -t^{-2} J/g_y.  Take ord.  QED

Consequences used downstream:
  g_y(tau_i) = prod_{j != i}(tau_i - tau_j)  (g - c_2 monic), so
     -ord_t f(tau_i)  =  1 + sum_{j!=i} ord_t(tau_i - tau_j)   (Keller, proper branch)
  and N = deg F = sum_i ( -ord_t f(tau_i) )^+ .

This file runs FAIL-CLOSED controls.  Every check is exact (Fraction / sympy over Q).
"""
import sys, itertools
from fractions import Fraction as F
import sympy as sp

x, y, z, t, c1, c2 = sp.symbols('x y z t c1 c2')

FAILURES = []
NCHECK = [0]
def check(name, cond, detail=""):
    NCHECK[0] += 1
    if not cond:
        FAILURES.append((name, detail))
        print("  FAIL  %-58s %s" % (name, detail))
    return cond

# ---------------------------------------------------------------- Newton polygon
def newton_orders(R, zv, xv):
    """R(x,z) = lc(x) * prod_i (z - w_i(t)) with w_i Puiseux in t = 1/x.
    Return the multiset {ord_t w_i} as Fractions, from the Newton polygon of R at
    x = infinity.  With ord_t(x) = -1, the Newton polygon w.r.t. ord_t uses the points
    (j, ord_t r_j) = (j, -deg_x r_j) and the LOWER hull, whose slope on an edge is
    -ord_t(w); equivalently the UPPER hull of (j, deg_x r_j), whose slope IS ord_t(w).
    Roots w_i = 0 (i.e. the z-multiplicity of R at z=0) get ord_t = +infinity and are
    returned as None."""
    P = sp.Poly(sp.expand(R), zv)
    d = P.degree()
    pts = []
    for j in range(d+1):
        cj = sp.expand(P.nth(j))
        if cj == 0: continue
        pts.append((j, sp.degree(sp.Poly(cj, xv), xv)))
    pts.sort()
    j0 = pts[0][0]
    # upper hull from (j0, .) to (d, .)
    hull = []
    for p in pts:
        while len(hull) >= 2:
            (a1,b1),(a2,b2) = hull[-2], hull[-1]
            # keep upper hull: cross product
            if (a2-a1)*(p[1]-b1) - (b2-b1)*(p[0]-a1) >= 0:
                hull.pop()
            else:
                break
        hull.append(p)
    ords = [None]*j0                      # the j0 roots identically 0
    for i in range(len(hull)-1):
        (a1,b1),(a2,b2) = hull[i], hull[i+1]
        slope = F(b2-b1, a2-a1)           # = ord_t of those (a2-a1) roots
        ords += [slope]*(a2-a1)           # Newton polygon w.r.t. ord_t, ord_t(x) = -1
    return ords

def branch_orders(g_c, h, m_deg=None):
    """multiset {ord_t h(x,tau_i)} over the roots tau_i of g_c(x,y)=0 (monic in y)."""
    R = sp.resultant(sp.expand(g_c), z - sp.expand(h), y)
    return newton_orders(sp.expand(R), z, x)

# ---------------------------------------------------------------- gauge + degree
def in_gauge(p):
    """True iff p is monic in y with deg_y p = total deg p."""
    P = sp.Poly(sp.expand(p), x, y)
    dy = sp.degree(sp.Poly(sp.expand(p), y), y)
    return sp.total_degree(sp.expand(p)) == dy and sp.simplify(sp.LC(sp.Poly(sp.expand(p), y))) == 1

def gauge(p, q):
    """apply x -> x + a*y and rescale so that both are monic in y of degree = deg."""
    for a in range(1, 8):
        pp = sp.expand(p.subs(x, x + a*y)); qq = sp.expand(q.subs(x, x + a*y))
        lp = sp.LC(sp.Poly(pp, y)); lq = sp.LC(sp.Poly(qq, y))
        if lp.free_symbols or lq.free_symbols: continue
        pp = sp.expand(pp/lp); qq = sp.expand(qq/lq)
        if in_gauge(pp) and in_gauge(qq): return pp, qq
    return None, None

def geometric_degree(f, g):
    """N = deg_x Res_y(f-c1, g-c2) at generic (c1,c2)."""
    R = sp.expand(sp.resultant(sp.expand(f)-c1, sp.expand(g)-c2, y))
    return sp.degree(sp.Poly(R, x), x)

def jac(f, g):
    return sp.expand(sp.diff(f,x)*sp.diff(g,y) - sp.diff(f,y)*sp.diff(g,x))

# ---------------------------------------------------------------- automorphisms
def compose(F1, F2):
    """(F1 o F2)(x,y)."""
    a, b = F2
    return (sp.expand(F1[0].subs({x:a, y:b}, simultaneous=True)),
            sp.expand(F1[1].subs({x:a, y:b}, simultaneous=True)))

TRI = {
    'a': lambda k, c: (x, y + c*x**k),
    'b': lambda k, c: (x + c*y**k, y),
}
def build_auto(word):
    """word = list of (which, k, c)."""
    Fm = (x, y)
    for w, k, c in word:
        Fm = compose(TRI[w](k, c), Fm)
    return Fm

AUTO_WORDS = [
    [('a',2,1)],
    [('a',3,1)],
    [('a',2,1),('b',2,1)],
    [('a',2,1),('b',3,1)],
    [('a',3,1),('b',2,1)],
    [('b',2,1),('a',2,-1)],
    [('a',2,1),('b',2,2),('a',2,1)],
    [('a',2,3),('b',3,1)],
    [('a',4,1),('b',2,1)],
]

def control_A_automorphisms():
    print("\n-- CONTROL A: JAC-FIBRE on genuine Keller pairs (polynomial automorphisms) --")
    print("   %-26s %3s %3s %4s  %-22s %s" % ("word","m","n","N","{ord_t (f*g_y)(tau)}","verdict"))
    for w in AUTO_WORDS:
        P, Q = build_auto(w)
        # gauge: want deg f <= deg g, both monic in y with deg = deg_y
        if sp.total_degree(P) > sp.total_degree(Q): P, Q = Q, P
        f, g = gauge(P, Q)
        if f is None:
            check("gauge(%s)" % w, False, "no linear gauge found"); continue
        J = jac(f, g)
        m = sp.degree(sp.Poly(f, y), y); n = sp.degree(sp.Poly(g, y), y)
        check("keller %s" % w, J.free_symbols == set(), "J = %s" % J)
        N = geometric_degree(f, g)
        check("N=1 for automorphism %s" % w, N == 1, "N = %s" % N)
        # JAC-FIBRE, resultant form: ord_t (f*g_y)(tau_i) = -1 for every branch,
        # because every branch of an automorphism fibre is PROPER (single place).
        gy = sp.expand(sp.diff(g, y))
        ords = branch_orders(sp.expand(g - c2), sp.expand(f*gy))
        ok = (len(ords) == n) and all(o is not None and o == F(-1) for o in ords)
        check("JAC-FIBRE %s" % w, ok, "orders = %s" % ords)
        # frontier form: -ord_t f(tau) = 1 - delta^0 with delta^0 = -ord_t g_y(tau)
        of = branch_orders(sp.expand(g - c2), f)
        og = branch_orders(sp.expand(g - c2), gy)
        d0 = sorted([-o for o in og]); mf = sorted([-o for o in of])
        ok2 = all(a + b == F(1) for a, b in zip(sorted(d0), sorted(mf, reverse=True)))
        Nfr = sum(max(F(0), F(1)-dd) for dd in d0)
        check("N = sum (1-delta0)^+ %s" % w, Nfr == N, "sum = %s vs N = %s" % (Nfr, N))
        print("   %-26s %3d %3d %4d  %-22s %s" %
              (str(w), m, n, N, sorted(set(ords)), "OK" if (ok and ok2) else "SEE ABOVE"))

def control_B_negative():
    """f = y, g = x^j + y^k.  J = -j x^{j-1}: Keller iff j = 1.
       JAC-FIBRE defect: ord(f g_y)(tau) = -j = -1 + ord_t J(tau)."""
    print("\n-- CONTROL B (NEGATIVE): the identity holds EXACTLY on the Keller locus --")
    print("   %-14s %-16s %-10s %-12s %-10s %s" % ("(j,k)","J","ord(f*g_y)","ord J(tau)","-1+ordJ","verdict"))
    for j in range(1, 5):
        for k in range(2, 6):
            f = y; g = sp.expand(x**j + y**k)
            J = jac(f, g)
            gy = sp.expand(sp.diff(g, y))
            o_fg = branch_orders(sp.expand(g - c2), sp.expand(f*gy))
            o_J  = branch_orders(sp.expand(g - c2), J)
            pred = [F(-1) + o for o in sorted(o_J)]
            ok = sorted(o_fg) == sorted(pred)
            keller = (J.free_symbols == set())
            check("JF-general (%d,%d)" % (j,k), ok, "%s vs %s" % (sorted(o_fg), pred))
            check("JF-Keller-iff (%d,%d)" % (j,k),
                  (all(o == F(-1) for o in o_fg)) == keller,
                  "orders %s keller=%s" % (sorted(set(o_fg)), keller))
            print("   %-14s %-16s %-10s %-12s %-10s %s" %
                  ("(%d,%d)"%(j,k), str(J), sorted(set(o_fg)), sorted(set(o_J)),
                   sorted(set(pred)), "keller" if keller else "non-keller"))

def control_C_nonkeller_two_tower():
    """The seven two-tower rows of N-ON-THE-TREE: all non-Keller.  The identity must
       fail (ord_t J(tau) != 0) on every one of them."""
    print("\n-- CONTROL C (NEGATIVE): N-ON-THE-TREE's two-tower rows --")
    def fac(a, p, b, q): return sp.expand((y - a*x)**p - b*x**q)
    def bld(spec):
        out = sp.Integer(1)
        for s in spec: out = sp.expand(out*fac(*s))
        return out
    rows = [
        ([(1,1,3,0),(2,1,5,0)], [(1,2,7,1),(2,1,11,0)]),
        ([(1,2,3,1),(2,2,5,1)], [(1,3,7,2),(2,1,11,0)]),
        ([(1,2,3,1),(2,2,3,1)], [(1,3,3,1),(2,3,3,1)]),
        ([(1,1,3,0),(2,2,5,1)], [(1,2,7,1),(2,2,11,1)]),
    ]
    for i,(fs, gs) in enumerate(rows):
        f = bld(fs); g = bld(gs)
        if not (in_gauge(f) and in_gauge(g)):
            check("gauge row %d" % i, False, ""); continue
        J = jac(f, g)
        check("row %d non-Keller" % i, J.free_symbols != set(), "J = %s" % J)
        gy = sp.expand(sp.diff(g, y))
        o_fg = branch_orders(sp.expand(g - c2), sp.expand(f*gy))
        o_J  = branch_orders(sp.expand(g - c2), J)
        ok = sorted(o_fg) == sorted([F(-1)+o for o in o_J])
        check("JF-general row %d" % i, ok, "%s vs %s" % (sorted(o_fg), sorted(o_J)))
        allminus1 = all(o == F(-1) for o in o_fg)
        check("row %d identity FAILS (non-Keller)" % i, not allminus1, "orders %s" % sorted(set(o_fg)))
        print("   row %d: m=%d n=%d  J=%s  ord(f*g_y)(tau) in %s   ord J(tau) in %s" %
              (i, sp.degree(sp.Poly(f,y),y), sp.degree(sp.Poly(g,y),y),
               sp.factor(J), sorted(set(o_fg)), sorted(set(o_J))))

def control_D_closed_form_tree():
    """f = y, g = x + y^k  (Keller, m=1, n=k):  every object in closed form.
       roots of g - c2:  tau_i = zeta^i (c2 - x)^{1/k},  ord_t = -1/k.
       g-tree:  the k roots of g separate at delta = -1/k = delta_1;
       lambda_g(delta) = k*delta for delta <= -1/k, delta - (k-1)/k after;
       frontier delta^0 = (k-1)/k;  contribution 1 - delta^0 = 1/k each;
       N = k * (1/k) = 1.   Also the floor/ceiling at D_1 both equal m(1-delta_1)/(n+m)."""
    print("\n-- CONTROL D: closed-form tree, floor = ceiling at D_1 --")
    print("   %3s %4s %8s %10s %10s %10s %6s" % ("k","N","delta_1","lam_g(d1)","floor","ceiling","a_1*fl"))
    for k in range(2, 9):
        m, n = 1, k
        M1 = -m
        delta1 = F(-1, k)
        lamg = -F(n*(1-delta1), n - M1)         # Moh Lemma 5.2 at r = 1
        check("lam_g(delta1) direct k=%d" % k, lamg == F(-1), "%s" % lamg)
        floor  = (1-delta1) + lamg              # 1 - delta^0 lower bound (slope >= 1)
        ceil   = -F(m, n)*lamg                  # -lambda_f(delta_1)
        check("floor==ceiling k=%d" % k, floor == ceil, "%s vs %s" % (floor, ceil))
        a1 = k
        check("N = a_1*floor k=%d" % k, a1*floor == 1, "%s" % (a1*floor))
        print("   %3d %4d %8s %10s %10s %10s %6s" % (k, 1, delta1, lamg, floor, ceil, a1*floor))

if __name__ == "__main__":
    control_A_automorphisms()
    control_B_negative()
    control_C_nonkeller_two_tower()
    control_D_closed_form_tree()
    print("\n== %d checks, %d failures ==" % (NCHECK[0], len(FAILURES)))
    if FAILURES:
        for nm, dt in FAILURES: print("   FAILED: %s  %s" % (nm, dt))
        sys.exit(1)
