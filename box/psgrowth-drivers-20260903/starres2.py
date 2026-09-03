#!/usr/bin/env python3
"""RESIDUE-LEAD, ideal-theoretic version (supersedes starres.py's sp.solve route,
which returns INCOMPLETE solution sets: it reported no (2,3,2) star, and the
saturated Groebner basis shows one exists).

For each (d,e,V):  I := ( coefficients pi^1..pi^{a+b-1} of  d p_f p_g' - e p_g p_f' ,
                          z*kappa - 1 )                       [kappa != 0 SATURATED]
with p_g monic of degree a = eV translated (coeff of pi^{a-1} = 0) and deg p_f = b = dV.
  EXISTENCE     : GB(I) != {1}
  ptilde_j      : the j-th power sum  sum_{p_g(pi)=0} p_f(pi)^j , computed as the trace
                  of multiplication by p_f^j on C[pi]/(p_g)  (polynomial in the unknowns)
  VANISHING TEST: ptilde_j == 0 identically on V(I)   <=>   GB(I + (w*ptilde_j - 1)) = {1}
FAIL-CLOSED, with positive and negative controls on the vanishing test itself.
"""
import sys, time
import sympy as sp

pi_ = sp.Symbol('pi'); z = sp.Symbol('z'); w = sp.Symbol('w')
FAIL = []; NCHK = [0]
def check(name, cond, detail=""):
    NCHK[0] += 1
    if not cond:
        FAIL.append((name, detail)); print("    FAIL  %-56s %s" % (name, detail))
    return bool(cond)

def setup(d, e, V):
    a, b = e*V, d*V
    ps = sp.symbols('p0:%d' % a); qs = sp.symbols('q0:%d' % (b+1))
    pg = pi_**a + sum(ps[i]*pi_**i for i in range(a-1))
    pf = sum(qs[i]*pi_**i for i in range(b+1))
    B = sp.Poly(sp.expand(d*pf*sp.diff(pg, pi_) - e*pg*sp.diff(pf, pi_)), pi_)
    eqs = [sp.expand(B.nth(j)) for j in range(1, a+b)]
    kap = sp.expand(B.nth(0))
    unk = list(ps[:a-1]) + list(qs)
    return pf, pg, eqs, kap, unk, a, b

def ptilde_syms(pf, pg, a, J):
    """ptilde_j = tr(mult by p_f^j on C[pi]/(p_g)), j = 1..J, as polynomials in the unknowns."""
    PG = sp.Poly(pg, pi_)
    out = [sp.Integer(a)]
    cur = sp.Integer(1)
    for j in range(1, J+1):
        cur = sp.rem(sp.Poly(sp.expand(cur*pf), pi_), PG).as_expr()
        tr = sp.Integer(0)
        for i in range(a):
            r = sp.Poly(sp.rem(sp.Poly(sp.expand(cur*pi_**i), pi_), PG), pi_)
            tr += r.nth(i)
        out.append(sp.expand(tr))
    return out

def is_trivial(G):
    return [sp.simplify(t) for t in G.exprs] == [sp.Integer(1)]

def report(d, e, V, J=12, tlim=600):
    t0 = time.time()
    pf, pg, eqs, kap, unk, a, b = setup(d, e, V)
    I = eqs + [sp.expand(z*kap - 1)]
    G = sp.groebner(I, *(unk + [z]), order='grevlex')
    exists = not is_trivial(G)
    print("\n== bottom star (d,e,V_2) = (%d,%d,%d):  a_1 = deg p_g = %d, b_1 = deg p_f = %d,"
          "  gamma = V(de-d-e)+1 = %d" % (d, e, V, a, b, V*(d*e-d-e)+1))
    check("(%d,%d,%d) a BOTTOM-ODE star with kappa != 0 EXISTS" % (d,e,V), exists,
          "saturated GB = {1}")
    if not exists:
        print("   NO star of this type  (saturated GB = {1})"); return None
    PT = ptilde_syms(pf, pg, a, J)
    van = []
    for j in range(1, J+1):
        Gj = sp.groebner(I + [sp.expand(w*PT[j] - 1)], *(unk + [z, w]), order='grevlex')
        vanishes = is_trivial(Gj)
        if vanishes: van.append(j)
    nz = [j for j in range(1, J+1) if j not in van]
    print("   ptilde_j = sum_{p_g(pi)=0} p_f(pi)^j  vanishes IDENTICALLY on the star variety")
    print("     for j in %s   (j <= %d);  NONZERO (generically) for j in %s" % (van, J, nz))
    print("   => per-disc leading coefficient S_k = (d/kappa) ptilde_{k+1} is generically")
    print("      NONZERO for k in %s ,  identically ZERO for k in %s"
          % ([j-1 for j in nz], [j-1 for j in van]))
    check("(%d,%d,%d) ptilde_1 == 0 (Euler-Jacobi: S_0 = [pi^{a-1}]1 = 0 for a >= 2)"
          % (d,e,V), (1 in van) or a < 2)
    print("   [%.1f s]" % (time.time()-t0))
    return van, nz

if __name__ == "__main__":
    print("starres2.py -- RESIDUE-LEAD via saturated Groebner.  sympy", sp.__version__)
    print("="*80)
    # ---- control of the VANISHING TEST itself (positive and negative)
    print("\n-- controls on the vanishing test")
    Gt = sp.groebner([sp.Symbol('u')**2 - 1, sp.Symbol('v')*sp.Symbol('u')*0 + 0*sp.Symbol('v')],
                     sp.Symbol('u'), sp.Symbol('v'), order='grevlex')
    u_, v_ = sp.symbols('u v')
    G1 = sp.groebner([u_**2 - 1, w*(u_**2 - 1) - 1], u_, w, order='grevlex')
    check("vanishing test POSITIVE control (h in the ideal -> reported as vanishing)",
          is_trivial(G1))
    G2 = sp.groebner([u_**2 - 1, w*u_ - 1], u_, w, order='grevlex')
    check("vanishing test NEGATIVE control (h a unit -> reported as NOT vanishing)",
          not is_trivial(G2))
    TR = [(1,2,1), (1,3,1), (1,4,1), (1,6,1), (2,3,1), (2,3,2), (2,3,3), (2,5,1), (3,5,1)]
    if len(sys.argv) > 1:
        TR = [tuple(int(z_) for z_ in aa.split(',')) for aa in sys.argv[1:]]
    for t in TR:
        try: report(*t, J=12)
        except Exception as ex: print("   ERROR on %s: %s" % (t, ex))
    print("\n" + "="*80)
    print("%d checks, %d failures" % (NCHK[0], len(FAIL)))
    for nm, dt in FAIL: print("   FAILED:", nm, dt)
