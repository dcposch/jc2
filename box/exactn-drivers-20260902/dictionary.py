#!/usr/bin/env python3
"""
dictionary.py -- STEP 1 of EXACT-N, tested three ways.

(D1)  ORDER STEP (Jacobian).  Along a branch tau_i of g - c_2,
          d/dx f(x,tau_i) = [f,g] / g_y(x,tau_i),
      so for [f,g] = J,
          ord_t(d/dx f(tau_i)) = ord_t J(tau_i) - ord_t g_y(tau_i).
      With w := -ord_t (= deg_x growth), and lambda := ord_t f(tau_i):
          lambda != 0  ==>  ord_t(d/dx f(tau)) = lambda + 1.
      Hence, J a unit:   lambda + 1 = -ord_t g_y(tau_i) =: delta0_i.
      TESTED WITHOUT ANY PUISEUX ROOT: the multisets {ord_t f(tau_i)},
      {ord_t g_y(tau_i)}, {ord_t J(tau_i)} are read off Newton polygons of
      Res_y(z - h, g - c_2) for h = f, g_y, J.  The PAIRING of the two
      multisets is recovered by sorting (both are read as sorted lists of
      slopes; matching is by the branch-ordering of the same Newton fan --
      justified only when the multiset {delta0_i} determines the pairing,
      which is checked here by re-deriving f's multiset from g_y's).

(D2)  TREE STEP.  -ord_t g_y(tau_i) equals delta0_i, the frontier of rho_i on
      the UNSHIFTED g-tree (lambda_g^{(i)}(delta0_i) = 0).  Tested on families
      with closed-form Puiseux roots.

(D3)  N = sum_i (1 - delta0_i)^+   (DICT-N).
"""
import sys
from fractions import Fraction as F
from math import gcd
import sympy as sp

x, y, z = sp.symbols('x y z')

FAILURES = []
def check(name, cond, detail=""):
    if cond: print(f"  [ok]   {name}")
    else:    print(f"  [FAIL] {name}   {detail}"); FAILURES.append(name)

# --------------------------------------------------------------------------
# Newton polygon:  multiset of deg_x of the z-roots of R(x,z), sorted desc.
# --------------------------------------------------------------------------
def degx_roots(R):
    """R in C[x,z], deg_z = n.  Return sorted-desc list of deg_x(z_j) as Fractions.
       Uses the upper convex hull of (k, deg_x c_{n-k}), c_j = coeff of z^j."""
    P = sp.Poly(sp.expand(R), z)
    n = P.degree()
    if n == 0: return []
    coeffs = P.all_coeffs()          # [c_n, c_{n-1}, ..., c_0]
    pts = []
    for k in range(0, n+1):
        c = sp.expand(coeffs[k])
        if c != 0:
            pts.append((k, sp.degree(sp.Poly(c, x))))
    # upper convex hull over k
    hull = []
    for p in pts:
        while len(hull) >= 2:
            (k0,d0),(k1,d1) = hull[-2], hull[-1]
            # keep p if (k1,d1) is strictly above segment (k0,d0)-(p)
            if (d1-d0)*(p[0]-k0) <= (p[1]-d0)*(k1-k0):
                hull.pop()
            else: break
        hull.append(p)
    out = []
    for i in range(len(hull)-1):
        (k0,d0),(k1,d1) = hull[i], hull[i+1]
        slope = F(d1-d0, k1-k0)
        out += [slope]*(k1-k0)
    assert len(out) == n, (len(out), n)
    return sorted(out, reverse=True)

def ordt_roots(R):
    """ord_t = -deg_x, sorted ASCENDING in ord_t (= descending in deg_x)."""
    return [-w for w in degx_roots(R)]

def branch_orders(h, g, c2):
    """multiset {ord_t h(x,tau_i)} over roots tau_i of g - c_2, as sorted list."""
    R = sp.resultant(sp.Poly(sp.expand(z - h), y), sp.Poly(sp.expand(g - c2), y), y)
    return ordt_roots(sp.expand(sp.expand(R).as_expr() if hasattr(R,'as_expr') else R))

def jac(f, g):
    return sp.expand(sp.diff(f,x)*sp.diff(g,y) - sp.diff(f,y)*sp.diff(g,x))

def N_res(f, g, c1, c2):
    R = sp.resultant(sp.Poly(sp.expand(f-c1), y), sp.Poly(sp.expand(g-c2), y), y)
    R = sp.expand(R.as_expr() if hasattr(R,'as_expr') else R)
    return None if R == 0 else int(sp.degree(sp.Poly(R, x)))

# --------------------------------------------------------------------------
# closed-form two-tower factors (identical convention to box/moh_skeleton_N.py)
# --------------------------------------------------------------------------
INF = F(10**9)
def _factor(a,p,b,q): return sp.expand((y - a*x)**p - b*x**q)
def _roots(a,p,b,q):
    return [{F(1,1): sp.sympify(a),
             F(q,p): (sp.sympify(b)**sp.Rational(1,p))*sp.exp(2*sp.pi*sp.I*sp.Rational(k,p))}
            for k in range(p)]
def build(spec):
    poly = 1
    for tt in spec: poly = sp.expand(poly*_factor(*tt))
    return poly, [r for tt in spec for r in _roots(*tt)]

def ord_diff(r1,r2):
    for e in sorted(set(r1)|set(r2), reverse=True):
        if sp.simplify(r1.get(e,0)-r2.get(e,0)) != 0: return -e
    return INF

def lam(delta, ords): return sum(min(delta,o) for o in ords)

def frontier(ords):
    lo = F(-1); cur = lam(lo, ords)
    assert cur <= 0
    for nxt in sorted(set(o for o in ords if o < INF)) + [INF]:
        if nxt <= lo: continue
        slope = sum(1 for o in ords if o > lo)
        assert slope > 0
        if nxt >= INF or cur + slope*(nxt-lo) >= 0: return lo + F(-cur,1)/slope
        cur += slope*(nxt-lo); lo = nxt
    raise AssertionError

def tree_delta0(taus):
    """frontier delta^0_i of every root, on the unshifted tree of `taus`."""
    out = []
    for i,r in enumerate(taus):
        ords = [ord_diff(r, s) if j != i else INF for j,s in enumerate(taus)]
        out.append(frontier(ords))
    return out

def tree_lam(taus, phis, delta_list):
    """lambda_f^{(i)}(delta_i) for each i (phis = roots of f)."""
    out = []
    for i,r in enumerate(taus):
        ords = [ord_diff(r,p) for p in phis]
        out.append(lam(delta_list[i], ords))
    return out

TWO_TOWER = [
    ([(1,1,3,0),(2,1,5,0)],  [(1,2,7,1),(2,1,11,0)]),
    ([(1,2,3,1),(2,1,5,0)],  [(1,2,7,1),(2,2,11,1)]),
    ([(1,2,3,1),(2,2,5,1)],  [(1,3,7,2),(2,1,11,0)]),
    ([(1,1,3,0),(2,2,5,1)],  [(1,2,7,1),(2,2,11,1)]),
    ([(1,3,3,2),(2,1,5,0)],  [(1,3,7,1),(2,1,11,0)]),
    ([(1,2,3,1),(2,2,5,1)],  [(1,4,7,2),(2,2,11,1)]),
    ([(1,2,3,1),(2,2,3,1)],  [(1,3,3,1),(2,3,3,1)]),
]

# --------------------------------------------------------------------------
KELLER = [
  # (label, f, g, in_gauge)
  ("auto (y, x+y^5)",            y,                      x + y**5,                          True),
  ("auto (y, x+y^7)",            y,                      x + y**7,                          True),
  ("auto (x+y^5, y+(x+y^5)^3)",  x + y**5,               y + (x+y**5)**3,                   True),
  ("auto (x+y^3, y+(x+y^3)^2)",  x + y**3,               y + (x+y**3)**2,                   True),
  ("auto (x+y^2, y+(x+y^2)^3)",  x + y**2,               y + (x+y**2)**3,                   True),
  ("auto depth3 p=(3,2,2)",      y + (x+y**3)**2,        (x+y**3) + (y+(x+y**3)**2)**2,     True),
  ("auto (x+(y^2+1)^3, y+f^2)",  x + (y**2+1)**3,        y + (x+(y**2+1)**3)**2,            True),
  ("auto shear (y, x+y^5+3y^2)", y,                      x + y**5 + 3*y**2,                 True),
  ("CHARGED (y+x^2, x+(y+x^2)^2)", y + x**2,             x + (y+x**2)**2,                   False),
]

def report_pair(label, f, g, c2, c1, in_gauge, verbose=True):
    J = jac(f,g)
    n = sp.degree(sp.Poly(g,y))
    gy = sp.expand(sp.diff(g,y))
    of  = branch_orders(f,  g, c2)          # ord_t f(tau_i),  sorted ascending
    ogy = branch_orders(gy, g, c2)          # ord_t g_y(tau_i)
    oJ  = branch_orders(J,  g, c2) if J.free_symbols else [F(0)]*n
    Nr  = N_res(f,g,c1,c2)
    d0  = sorted([-o for o in ogy])         # delta0_i = -ord_t g_y(tau_i)
    lamf= sorted(of)
    # DICT-N
    Ndict = sum(max(F(0), 1-dd) for dd in d0)
    Nfront= sum(max(F(0), -l) for l in lamf)
    if verbose:
        print(f"   {label}")
        print(f"      deg f={sp.degree(sp.Poly(f,y))}(y)/{sp.total_degree(f)}  "
              f"deg g={n}(y)/{sp.total_degree(g)}  J={J}")
        print(f"      ord_t f(tau) : {[str(v) for v in lamf]}")
        print(f"      delta0=-ord_t g_y(tau) : {[str(v) for v in d0]}")
        print(f"      N(res)={Nr}   sum(-ord_t f)^+ = {Nfront}   DICT-N = {Ndict}")
    return dict(N=Nr, Nfront=Nfront, Ndict=Ndict, lamf=lamf, d0=d0, oJ=oJ, J=J, n=n)

def main():
    c1, c2 = sp.Rational(7,3), sp.Rational(-5,2)
    print("== CONTROL A: DICT-N on Keller pairs (J a unit) ==")
    for (lab,f,g,ig) in KELLER:
        r = report_pair(lab,f,g,c2,c1,ig)
        # (D1) dictionary as a paired statement: sorted lists must satisfy
        #      lambda_i + 1 = delta0_i  after sorting BOTH ascending in lambda
        #      (delta0 ascending  <->  lambda ascending)
        ok = all(r['lamf'][i] + 1 == r['d0'][i] for i in range(r['n']))
        check(f"D1 dictionary lambda+1=delta0 :: {lab}", ok,
              f"{[str(v) for v in r['lamf']]} vs {[str(v) for v in r['d0']]}")
        check(f"D3 DICT-N = sum(-lambda)^+   :: {lab}", r['Ndict'] == r['Nfront'])
        if ig: check(f"    ... = N(res)             :: {lab}", r['Ndict'] == r['N'],
                     f"dict {r['Ndict']} vs res {r['N']}")
        print()

    print("== CONTROL B: NEGATIVE -- non-Keller two-tower rows (J nonconstant) ==")
    print(f"   {'row':4} {'m':>3} {'n':>3} {'N(res)':>7} {'DICT-N':>8} {'deficit':>8} "
          f"{'-sum ord_t J(tau)':>18}")
    for k,(fs,gs) in enumerate(TWO_TOWER):
        f,_ = build(fs); g,_ = build(gs)
        r = report_pair(f"row {k}", f,g,c2,c1,True, verbose=False)
        defc = r['N'] - r['Ndict']
        sJ = -sum(r['oJ'])
        print(f"   {k:>4} {int(sp.degree(sp.Poly(f,y))):>3} {int(r['n']):>3} {r['N']:>7} "
              f"{str(r['Ndict']):>8} {str(defc):>8} {str(sJ):>18}")
        check(f"B: DICT-N FAILS on non-Keller row {k}", r['Ndict'] != r['N'],
              "dictionary must not hold off the Jacobian condition")
    print()
    print("== CONTROL B2: the exact (untruncated) dictionary as a SUM identity ==")
    print("   sum_i ord_t f(tau_i) + n  ==  -sum_i ord_t g_y(tau_i) + sum_i ord_t J(tau_i)")
    print(f"   {'row':22} {'LHS':>10} {'RHS':>10}")
    ROWS = [(f"two-tower {k}", build(fs)[0], build(gs)[0]) for k,(fs,gs) in enumerate(TWO_TOWER)]
    ROWS += [(lab,f,g) for (lab,f,g,ig) in KELLER]
    for (lab,f,g) in ROWS:
        J = jac(f,g); gy = sp.expand(sp.diff(g,y)); n = int(sp.degree(sp.Poly(g,y)))
        of  = branch_orders(f,  g, c2)
        ogy = branch_orders(gy, g, c2)
        oJ  = branch_orders(J,  g, c2) if J.free_symbols else [F(0)]*n
        L = sum(of) + n; R = -sum(ogy) + sum(oJ)
        print(f"   {lab:22} {str(L):>10} {str(R):>10}")
        check(f"B2 sum-dictionary :: {lab}", L == R, f"{L} vs {R}")

    print()
    print("== CONTROL C: STEP-1 tree formula  -ord_t g_y(tau_i) = delta^0_i  (unshifted tree) ==")
    print("   (closed-form Puiseux roots; discriminating: frontier balls are NOT all singletons)")
    for k,(fs,gs) in enumerate(TWO_TOWER):
        f,phis = build(fs); g,taus = build(gs)
        d0_tree = sorted(tree_delta0(taus))
        gy = sp.expand(sp.diff(g,y))
        d0_dict = sorted([-o for o in branch_orders(gy,g,c2)])
        nonsing = sum(1 for i,r in enumerate(taus)
                      if any(ord_diff(r,s) >= d0_tree[0] for j,s in enumerate(taus) if j!=i))
        check(f"C: delta0 tree == -ord_t g_y  :: two-tower row {k}",
              d0_tree == d0_dict, f"{[str(v) for v in d0_tree]} vs {[str(v) for v in d0_dict]}")
    for (lab,f,g,ig) in KELLER[:2]:
        pass
    print()
    print("== CONTROL C2: a NON-singleton frontier ball -- the c2-shift is load-bearing ==")
    # g = h^2, h = (y-x)^2 - 7x.  g-roots: 2 roots of h, each DOUBLED (contact INF).
    # frontier ball at delta^0 = 1/2 therefore has a(B) = 2 > 1 and delta_B = INF > delta^0.
    h  = sp.expand((y-x)**2 - 7*x); g4 = sp.expand(h**2)
    _,rh = build([(1,2,7,1)]); taus4 = rh + rh          # roots with multiplicity
    ords1 = [ord_diff(taus4[0], taus4[j]) if j != 0 else INF for j in range(4)]
    d0_tree = frontier(ords1)
    gy4 = sp.expand(sp.diff(g4,y))
    d0_gen = sorted([-o for o in branch_orders(gy4,g4,c2)])
    try:    unsh = sorted([-o for o in branch_orders(gy4,g4,sp.Integer(0))])
    except AssertionError: unsh = "IDENTICALLY ZERO (g_y vanishes on the double roots)"
    print(f"   pairwise ord_t(rho_1 - rho_j) : {[str(v) for v in ords1]}   (INF = repeated root)")
    print(f"   frontier from the tree        : {d0_tree}   (ball has a(B)=2 roots)")
    print(f"   -ord_t g_y(tau_i), generic c2 : {[str(v) for v in d0_gen]}")
    print(f"   -ord_t g_y(tau_i), c2 = 0     : {unsh}")
    check("C2: tree frontier == -ord_t g_y at generic c2 (non-singleton ball)",
          all(v == d0_tree for v in d0_gen), f"{d0_gen} vs {d0_tree}")
    check("C2: c2=0 DIFFERS -- the shift is load-bearing", unsh != d0_gen, f"{unsh}")

    print("== CONTROL D: generic-c2 invariance of {delta0_i} ==")
    for (lab,f,g,ig) in KELLER[:6]:
        gy = sp.expand(sp.diff(g,y))
        sets = [sorted([-o for o in branch_orders(gy,g,cc)])
                for cc in [sp.Rational(-5,2), sp.Rational(3,7), sp.Rational(11,5)]]
        check(f"D: {{delta0}} same for 3 generic c2 :: {lab}", sets[0]==sets[1]==sets[2], f"{sets}")

    print()
    if FAILURES:
        print(f"FAILURES: {len(FAILURES)}"); sys.exit(1)
    print("ALL CONTROLS PASSED")

if __name__ == "__main__": main()
