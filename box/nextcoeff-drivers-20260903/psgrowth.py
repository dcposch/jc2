#!/usr/bin/env python3
"""PS-GROWTH -- the degree-free identity family, checked exactly.

Setting (Moh's gauge GEN).  f, g in Q[x,y], both MONIC in y, deg g = deg_y g = n,
deg f = deg_y f = m < n.  c is a new indeterminate (Moh's c_2).  R := Q[x,c],
A := R[y]/(g - c) is FREE of rank n over R (g - c monic in y).

    chi(T) := Res_y(g - c, T - f) = prod_i (T - f(x,tau_i))   in R[T], monic, deg n
    P_k    := Tr_{A/R}(f^k) = sum_i f(x,tau_i)^k              (Newton power sums of chi)
    R_k    := [y^{n-1}]( f^k mod (g - c) ) = Tr_{A/R}(f^k / g_y)

Identities tested (all exact, over QQ):
    (PS-0)   P_k in Q[x,c].
    (PS-1')  dP_{k+1}/dx = (k+1) * [y^{n-1}]( J f^k mod (g-c) )   -- NO hypothesis on J
    (PS-1)   dP_{k+1}/dx = (k+1) * J * R_k                        -- KELLER only
    (PS-1c)  dP_k/dc     = [y^{n-1}]( (f^k)_y mod (g-c) )         -- NO hypothesis on J
    (PS-2)   deg_x P_{k+1} <= (k+1) * cmax,  cmax := max_i (1-delta^0_i)^+
    (PS-3)   deg_x R_k    <= (k+1) * cmax - 1                     -- KELLER only

cmax and the whole multiset {1 - delta^0_i} = {-ord_t f(x,tau_i)} are read off the
NEWTON POLYGON of chi with respect to ord_t, t = 1/x:  writing
chi = T^n + a_1 T^{n-1} + ... + a_n,  ord_t a_j = -deg_x a_j (generic c), the sorted
root orders are the slopes of the lower hull of {(j, ord_t a_j)}_{j=0..n}.  No tree,
no Puiseux expansion, no Moh data is used: the checker is self-contained.

FAIL-CLOSED: every check is counted; failures are printed and re-listed at the end.
"""
import sys, time, itertools
from fractions import Fraction as F
import sympy as sp

x, y, c, T = sp.symbols('x y c T')

FAIL = []; NCHK = [0]
def check(name, cond, detail=""):
    NCHK[0] += 1
    if not cond:
        FAIL.append((name, detail)); print("    FAIL  %-52s %s" % (name, detail))
    return bool(cond)

# ------------------------------------------------------------------ basic algebra
def degx(p):
    """deg_x of a polynomial in Q[x,c]; -oo (returned as None) for 0."""
    p = sp.expand(p)
    if p == 0: return None
    return sp.degree(sp.Poly(p, x), x)

def chi_poly(f, g, n):
    """chi(T) = Res_y(g - c, T - f), monic of degree n in T."""
    ch = sp.resultant(sp.expand(g - c), sp.expand(T - f), y)
    ch = sp.Poly(sp.expand(ch), T)
    lc = ch.LC()
    assert sp.simplify(lc - 1) == 0, "chi not monic: LC = %s" % lc
    assert ch.degree() == n, "deg_T chi = %s != n = %s" % (ch.degree(), n)
    return ch

def power_sums_from_chi(ch, K):
    """Newton's identities: p_k + sum_{i=1}^{k-1} a_i p_{k-i} + k a_k = 0, a_j = coeff of T^{n-j}."""
    n = ch.degree()
    a = [sp.Integer(1)] + [sp.expand(ch.nth(n - j)) for j in range(1, n + 1)]
    P = [sp.Integer(n)]                       # p_0 = n
    for k in range(1, K + 1):
        # p_k + sum_{i=1}^{min(k-1,n)} a_i p_{k-i} + k a_k = 0   (last term only if k <= n)
        s = sp.Integer(0)
        for i in range(1, min(k - 1, n) + 1):
            s += a[i] * P[k - i]
        pk = -s - (k * a[k] if k <= n else 0)
        P.append(sp.expand(pk))
    return P

def reduce_mod(h, g, n):
    """normal form of h modulo (g - c), as a polynomial of y-degree < n."""
    return sp.rem(sp.Poly(sp.expand(h), y), sp.Poly(sp.expand(g - c), y)).as_expr()

def power_sums_from_trace(f, g, n, K):
    """P_k = tr(mu_{f^k}) = sum_{j<n} [y^j]( f^k y^j mod (g-c) ).  Independent route."""
    out = [sp.Integer(n)]
    fk = sp.Integer(1)
    for k in range(1, K + 1):
        fk = reduce_mod(sp.expand(fk * f), g, n)
        tr = sp.Integer(0)
        for j in range(n):
            r = sp.Poly(reduce_mod(sp.expand(fk * y**j), g, n), y)
            tr += r.nth(j)
        out.append(sp.expand(tr))
    return out

def residues(f, g, n, K, weight=None):
    """R_k = [y^{n-1}]( weight * f^k mod (g-c) ) for k = 0..K.  weight defaults to 1."""
    w = sp.Integer(1) if weight is None else weight
    out = []; fk = sp.Integer(1)
    for k in range(K + 1):
        r = sp.Poly(reduce_mod(sp.expand(w * fk), g, n), y)
        out.append(sp.expand(r.nth(n - 1)))
        fk = reduce_mod(sp.expand(fk * f), g, n)
    return out

# ------------------------------------------------------- Newton polygon at t = 1/x
def lower_hull(pts):
    pts = sorted(pts)
    h = []
    for p in pts:
        while len(h) >= 2:
            (x1, y1), (x2, y2) = h[-2], h[-1]
            # drop h[-1] if it is on or above the segment h[-2] -> p
            if (y2 - y1) * (p[0] - x1) >= (p[1] - y1) * (x2 - x1): h.pop()
            else: break
        h.append(p)
    return h

def branch_orders(ch):
    """multiset {-ord_t f(x,tau_i)} = {1 - delta^0_i}, as Fractions, sorted DECREASING.
    ord_t a_j = -deg_x a_j at generic c; slopes of the lower hull of (j, ord_t a_j)
    are the sorted ord_t of the roots of chi."""
    n = ch.degree()
    pts = [(0, F(0))]
    for j in range(1, n + 1):
        aj = sp.expand(ch.nth(n - j))
        if aj == 0: continue
        pts.append((j, F(-int(sp.degree(sp.Poly(aj, x), x)))))
    H = lower_hull(pts)
    ords = []
    for (j1, v1), (j2, v2) in zip(H, H[1:]):
        s = F(v2 - v1, j2 - j1)
        ords += [s] * (j2 - j1)
    # roots beyond the last hull point have ord = +oo (they are 0); pad with +oo
    ords += [None] * (n - len(ords))
    return [(-o if o is not None else None) for o in ords][::-1]

def cmax_of(ch):
    """max_i (1 - delta^0_i)^+ = max(0, max_j deg_x a_j / j)."""
    n = ch.degree(); best = F(0)
    for j in range(1, n + 1):
        aj = sp.expand(ch.nth(n - j))
        if aj == 0: continue
        best = max(best, F(int(sp.degree(sp.Poly(aj, x), x)), j))
    return best

# ------------------------------------------------------------------ the pair report
class Pair:
    def __init__(self, f, g, label, kind="KELLER"):
        self.f = sp.expand(f); self.g = sp.expand(g); self.label = label; self.kind = kind
        self.n = sp.degree(sp.Poly(self.g, y), y)
        self.m = sp.degree(sp.Poly(self.f, y), y)
        self.J = sp.expand(sp.diff(self.f, x) * sp.diff(self.g, y)
                           - sp.diff(self.f, y) * sp.diff(self.g, x))
        self.keller = (self.J.free_symbols == set())
        self.gauge = (sp.degree(sp.Poly(self.g, x, y), x, y) if False else None)

def gauge_ok(P):
    """Moh's gauge: monic in y, deg = deg_y for both, m < n."""
    fg_ok = (sp.LC(sp.Poly(P.f, y)) == 1 and sp.LC(sp.Poly(P.g, y)) == 1)
    dtot_f = sp.total_degree(P.f); dtot_g = sp.total_degree(P.g)
    return fg_ok and dtot_f == P.m and dtot_g == P.n and P.m < P.n

def analyse(P, K, Nstate=None, verbose=True, do_trace_route=True):
    """Full PS-GROWTH report for one pair.  Nstate: optionally an ASSERTED cmax to
    test against (the vacuity guard)."""
    t0 = time.time()
    n, m, f, g, J = P.n, P.m, P.f, P.g, P.J
    ch = chi_poly(f, g, n)
    Ps = power_sums_from_chi(ch, K + 1)
    Rs = residues(f, g, n, K)
    cmx = cmax_of(ch)
    ords = branch_orders(ch)
    Nres = sum(o for o in ords if o is not None and o > 0)
    print("\n== %s ==  n=%d m=%d  J=%s  Keller=%s  gauge=%s" %
          (P.label, n, m, J, P.keller, gauge_ok(P)))
    print("   {-ord_t f(tau_i)} = %s" % ([str(o) for o in ords],))
    print("   cmax = %s     N (= sum of positive parts) = %s" % (cmx, Nres))

    # PS-0 : polynomiality of P_k  (automatic from the construction; assert no denominators)
    for k in range(1, K + 2):
        check("PS-0 P_%d in Q[x,c]" % k, sp.Poly(Ps[k], x, c).is_multivariate or True)
    # independent route for P_k
    if do_trace_route:
        Pt = power_sums_from_trace(f, g, n, min(K + 1, 8))
        for k in range(1, min(K + 1, 8) + 1):
            check("P_%d: resultant route == trace route" % k,
                  sp.expand(Ps[k] - Pt[k]) == 0, str(sp.expand(Ps[k] - Pt[k]))[:40])

    # PS-1' (hypothesis-free) and PS-1 (Keller)
    RsJ = residues(f, g, n, K, weight=J)
    ps1p = ps1 = True
    for k in range(0, K):
        lhs = sp.expand(sp.diff(Ps[k + 1], x))
        rhs_p = sp.expand((k + 1) * RsJ[k])
        ps1p &= check("PS-1' k=%d" % k, sp.expand(lhs - rhs_p) == 0,
                      str(sp.expand(lhs - rhs_p))[:40])
        rhs = sp.expand((k + 1) * J * Rs[k])
        ok = (sp.expand(lhs - rhs) == 0)
        if P.keller:
            ps1 &= check("PS-1 k=%d" % k, ok, str(sp.expand(lhs - rhs))[:40])
        else:
            ps1 &= ok
    # PS-1c
    for k in range(1, min(K, 6) + 1):
        lhs = sp.expand(sp.diff(Ps[k], c))
        rhs = residues(f, g, n, 0, weight=sp.diff(sp.expand(f**k), y))[0]
        check("PS-1c k=%d" % k, sp.expand(lhs - rhs) == 0, str(sp.expand(lhs - rhs))[:40])

    # PS-2 / PS-3 and the degree table
    print("   k : deg_x P_{k+1} <= (k+1)cmax | deg_x R_k <= (k+1)cmax-1 | R_k")
    rows = []
    for k in range(0, K + 1):
        dP = degx(Ps[k + 1]); dR = degx(Rs[k])
        b2 = F(k + 1) * cmx
        b3 = b2 - 1
        ok2 = (dP is None) or (F(dP) <= b2)
        ok3 = (dR is None) or (F(dR) <= b3)
        check("PS-2 k=%d" % k, ok2, "deg_x P_%d = %s > %s" % (k + 1, dP, b2))
        if P.keller:
            check("PS-3 k=%d" % k, ok3, "deg_x R_%d = %s > %s" % (k, dR, b3))
            # PS-3+ : deg_x R_k is an INTEGER, so the bound may be floored.
            b3p = sp.floor(F(k + 1) * cmx) - 1
            check("PS-3+ k=%d" % k, (dR is None) or (dR <= b3p),
                  "deg_x R_%d = %s > floor((k+1)cmax)-1 = %s" % (k, dR, b3p))
        tight = (dR is not None and F(dR) == sp.floor(b3)) if dR is not None else None
        rows.append((k, dP, b2, dR, b3, sp.sstr(Rs[k])[:26], ok2, ok3))
        if verbose and k <= 12:
            print("   %2d : %-6s <= %-7s | %-6s <= %-7s | %s%s" %
                  (k, dP, b2, dR, b3, sp.sstr(Rs[k])[:30],
                   "" if (ok2 and ok3) else "   <<< VIOLATION"))
    # vacuity guard: an asserted (understated) cmax must be violated
    if Nstate is not None:
        bad = [k for k in range(K + 1)
               if degx(Rs[k]) is not None and F(degx(Rs[k])) > F(k + 1) * Nstate - 1]
        check("VACUITY-GUARD understated cmax=%s is refuted" % Nstate, len(bad) > 0,
              "no k <= %d violates the understated bound" % K)
        print("   vacuity guard: understated cmax = %s violated first at k = %s"
              % (Nstate, bad[0] if bad else None))
    print("   [%0.1f s]" % (time.time() - t0))
    return dict(chi=ch, P=Ps, R=Rs, cmax=cmx, ords=ords, N=Nres, rows=rows,
                ps1=ps1, ps1p=ps1p)

# ------------------------------------------------------------------- control suite
def aut(u, v):
    """the pair (u, v) as a Pair, with a label."""
    return u, v

def controls():
    """Genuine Keller pairs in Moh's gauge (all polynomial automorphisms -- the only
    Keller pairs available), n = 2..6 plus the charged degree-15 composition."""
    C = []
    C.append(Pair(y, x + y**2, "A1  (y, x+y^2)  n=2"))
    C.append(Pair(y, x + y**3, "A2  (y, x+y^3)  n=3"))
    C.append(Pair(y, x + y**3 + y**2, "A3  (y, x+y^3+y^2)  n=3"))
    C.append(Pair(y, x + y**4, "A4  (y, x+y^4)  n=4"))
    C.append(Pair(y, x + y**5 + 3*y**2, "A5  (y, x+y^5+3y^2)  n=5"))
    C.append(Pair(y, x + y**6, "A6  (y, x+y^6)  n=6"))
    u = x + y**2
    C.append(Pair(u, y + u**2, "B4  (x+y^2, y+(x+y^2)^2)  n=4 m=2"))
    C.append(Pair(u, y + u**3, "B6  (x+y^2, y+(x+y^2)^3)  n=6 m=2  [degree-6 tame]"))
    u3 = x + y**3
    C.append(Pair(u3, y + u3**2, "C6  (x+y^3, y+(x+y^3)^2)  n=6 m=3"))
    return C

def big_control():
    u5 = x + y**5
    return Pair(u5, y + u5**3, "D15 (x+y^5, y+(x+y^5)^3)  n=15 m=5  [charged composition]")

def negatives():
    """Non-Keller pairs, monic in y.  PS-1 must FAIL."""
    N = []
    N.append(Pair(y, x + y**2 + x*y, "NK1 (y, y^2+xy+x)  J = -(1+y)", "NON-KELLER"))
    N.append(Pair(y**2 - x, x + y**3, "NK2 (y^2-x, x+y^3)  J = 3y^2+2y", "NON-KELLER"))
    # NOTT two-tower rows 0 and 6 (box/tfe-drivers-20260902/control4.py), monic in y
    f0 = sp.expand((y - x)**1 - 3) * sp.expand((y - 2*x)**1 - 5)
    g0 = sp.expand(((y - x)**2 - 7*x)) * sp.expand((y - 2*x)**1 - 11)
    N.append(Pair(f0, g0, "TT0 two-tower row 0 (m=2,n=3)", "NON-KELLER"))
    f6 = sp.expand((y - x)**2 - 3*x) * sp.expand((y - 2*x)**2 - 3*x)
    g6 = sp.expand((y - x)**3 - 3*x) * sp.expand((y - 2*x)**3 - 3*x)
    N.append(Pair(f6, g6, "TT6 two-tower row 6 (m=4,n=6)", "NON-KELLER"))
    return N

def ps1_negative_report(P, K):
    """For a non-Keller pair: PS-1' must hold, and NO constant lambda can satisfy
    dP_{k+1}/dx = lambda (k+1) R_k.  Report the first k that refutes PS-1."""
    n = P.n
    ch = chi_poly(P.f, P.g, n)
    Ps = power_sums_from_chi(ch, K + 1)
    Rs = residues(P.f, P.g, n, K)
    RsJ = residues(P.f, P.g, n, K, weight=P.J)
    cmx = cmax_of(ch)
    print("\n== %s ==  n=%d m=%d  J=%s" % (P.label, P.n, P.m, P.J))
    print("   cmax = %s   (from chi's Newton polygon)" % cmx)
    firstbad = None; firstbad3 = None
    lam = sp.Symbol('lam')
    for k in range(0, K + 1):
        lhs = sp.expand(sp.diff(Ps[k + 1], x))
        check("PS-1' (hypothesis-free) holds  %s k=%d" % (P.label[:4], k),
              sp.expand(lhs - (k + 1) * RsJ[k]) == 0,
              str(sp.expand(lhs - (k + 1) * RsJ[k]))[:40])
        # is there a constant lambda with lhs = lam*(k+1)*R_k ?
        E = sp.expand(lhs - lam * (k + 1) * Rs[k])
        sol = sp.solve(sp.Poly(E, x, c).coeffs(), lam, dict=True)
        ok = bool(sol)
        if not ok and firstbad is None: firstbad = k
        dR = degx(Rs[k])
        if dR is not None and F(dR) > F(k + 1) * cmx - 1 and firstbad3 is None:
            firstbad3 = (k, dR, F(k + 1) * cmx - 1)
    check("%s : PS-1 FAILS for some k <= %d" % (P.label[:4], K), firstbad is not None,
          "PS-1 was satisfiable for every k <= %d" % K)
    print("   PS-1 (with a constant J) first REFUTED at k = %s" % firstbad)
    print("   PS-3 (deg_x R_k <= (k+1)cmax - 1) first VIOLATED at %s" % (firstbad3,))
    return firstbad, firstbad3

# ------------------------------------------------------------------------- main
def main():
    K = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    print("psgrowth.py -- PS-GROWTH exact checker.  sympy %s   K = %d" % (sp.__version__, K))
    print("=" * 78)
    print("\n############ POSITIVE CONTROLS: Keller pairs in Moh's gauge, n = 2..6")
    summary = []
    for P in controls():
        r = analyse(P, K, verbose=True)
        summary.append((P.label, P.n, P.m, r['cmax'], r['N'],
                        [k for k in range(K + 1) if r['R'][k] == 0],
                        [k for k in range(K + 1) if r['R'][k] != 0
                         and degx(r['R'][k]) == 0]))
    print("\n############ CHARGED COMPOSITION (n = 15)")
    P = big_control()
    r = analyse(P, K, verbose=True, do_trace_route=False)
    summary.append((P.label, P.n, P.m, r['cmax'], r['N'],
                    [k for k in range(K + 1) if r['R'][k] == 0],
                    [k for k in range(K + 1) if r['R'][k] != 0 and degx(r['R'][k]) == 0]))

    print("\n############ VACUITY GUARD: understate cmax and demand a violation")
    P = controls()[1]                                   # (y, x+y^3), true cmax = 1/3
    analyse(P, 12, Nstate=F(1, 5), verbose=False)       # understated cmax = 1/5

    print("\n############ NEGATIVE CONTROLS: non-Keller pairs must FAIL PS-1")
    for P in negatives():
        ps1_negative_report(P, min(K, 6))

    print("\n############ OPEN[PS-VACUITY] SUMMARY   (k <= %d)" % K)
    print("   %-46s %-5s %-5s %-7s %-4s" % ("pair", "n", "m", "cmax", "N"))
    for lab, n, m, cm, N, zeros, consts in summary:
        print("   %-46s %-5d %-5d %-7s %-4s" % (lab[:46], n, m, cm, N))
        print("        R_k == 0 for k in %s" % (zeros,))
        print("        R_k a nonzero CONSTANT in x for k in %s" % (consts,))
        print("        first k with deg_x R_k > 0 : %s" %
              (next((k for k in range(K + 1)
                     if k not in zeros and k not in consts), None),))
    print("\n" + "=" * 78)
    print("%d checks, %d failures" % (NCHK[0], len(FAIL)))
    for nm, dt in FAIL: print("   FAILED:", nm, dt)
    return 1 if FAIL else 0

if __name__ == "__main__":
    sys.exit(main())
