#!/usr/bin/env python3
"""
REDUCIBLE-BRANCH REPRICE -- the NON-PROPER half of JAC-FIBRE, exactly.

The D1-SUBTREE controls are polynomial automorphisms (A_F empty): every branch of
every generic fibre is PROPER and a_0 is never reached.  The reducible branch lives
on the other half.  Here the general law is exercised on branches that ARE
non-proper, with a_0 != 0 included:

  (JF)   ord_t( f(tau) - a_0 )  +  ord_t g_y(tau)  =  -1 + ord_t J(tau)
  (RO')  ord_t g_y(tau) = -delta^0_tau                      [g - c_2 monic in y]
  (NPR)  ord_t( f(tau) - a_0 )  =  delta^0_tau - 1 + ord_t J(tau)
  (SF)   Keller  =>  ord_t(f(tau)-a_0) > 0 at a non-proper branch, so delta^0 > 1
                     STRICTLY; delta^0 = 1 is impossible.

Method: fibres {g = c_2} chosen rational, parametrised by s, so every order is the
order of an explicit rational function of s over Q(c_2).  ord_t h = ord_s h / ord_s t.
Two places per row (s -> 0 and s -> infinity).  All exact; fail-closed.
"""
import sys
import sympy as sp
from fractions import Fraction as F

x, y, s, w, c2 = sp.symbols('x y s w c2')
FAIL = []; NCK = [0]
def check(name, cond, detail=""):
    NCK[0] += 1
    if not cond:
        FAIL.append((name, detail)); print("  FAIL  %-46s %s" % (name, detail))
    return cond

def ords(expr, v):
    """ord_v of a rational function, exactly (None if identically 0)."""
    e = sp.cancel(sp.together(sp.expand(expr)))
    if e == 0: return None
    num, den = sp.fraction(e)
    def lo(p):
        P = sp.Poly(sp.expand(p), v)
        return min(m[0] for m in P.monoms())
    return F(lo(num) - lo(den))

def jac(f, g):
    return sp.expand(sp.diff(f,x)*sp.diff(g,y) - sp.diff(f,y)*sp.diff(g,x))

# rows: (label, f, g, y(s), x(s))  with g(x(s), y(s)) == c_2 identically
def rows():
    R = []
    for k in (2,3,4,5):
        for p in (1,2):
            if p >= k: continue
            for j in (1,2):
                g = y**k + x*y**p
                f = y**j
                R.append(("f=y^%d, g=y^%d+xy^%d" % (j,k,p), f, g, s, (c2-s**k)/s**p))
    # a_0 != 0 rows
    R.append(("f=xy,      g=y^2+xy",   x*y,      y**2+x*y,   s, (c2-s**2)/s))
    R.append(("f=xy+y,    g=y^2+xy",   x*y+y,    y**2+x*y,   s, (c2-s**2)/s))
    R.append(("f=x y^2,   g=y^3+xy^2", x*y**2,   y**3+x*y**2, s, (c2-s**3)/s**2))
    R.append(("f=x^2y^2,  g=y^3+xy^2", x**2*y**2, y**3+x*y**2, s, (c2-s**3)/s**2))
    R.append(("f=y+xy,    g=y^3+xy",   y+x*y,    y**3+x*y,   s, (c2-s**3)/s))
    return R

def run():
    print("== CONTROL R: (JF), (RO') and (NPR) on branches that are NON-PROPER ==")
    print("   %-24s %-6s %8s %8s %8s %8s %6s %s" %
          ("row","place","ord(f-a0)","ord g_y","ord J","delta^0","proper","JF"))
    for (lab, f, g, ys, xs) in rows():
        gsub = sp.simplify(sp.expand(g.subs({x: xs, y: ys})) - c2)
        if not check("param(%s)" % lab, sp.simplify(gsub) == 0, "fibre param wrong"): continue
        J = jac(f, g)
        gy = sp.diff(g, y)
        for place, sub, par in (("s->0", {}, s), ("s->oo", {s: 1/w}, w)):
            X = sp.cancel(xs.subs(sub)); Y = sp.cancel(ys.subs(sub))
            ot = ords(1/X, par)
            if ot is None or ot == 0: continue          # x not going to infinity
            def O(h):
                v = ords(sp.cancel(h.subs({x: X, y: Y})), par)
                return None if v is None else v/ot
            ofull = O(f)
            if ofull is None: continue
            # a_0: the t^0 coefficient of f(tau); zero iff ord_t f < 0
            if ofull < 0:
                a0 = sp.Integer(0)
            else:
                fs = sp.cancel(f.subs({x: X, y: Y}))
                a0 = sp.simplify(sp.limit(fs, par, 0))
            oa = O(f - a0)
            ogy = O(gy); oJ = O(J)
            if oa is None or ogy is None or oJ is None: continue
            d0 = -ogy
            proper = (ofull < 0)
            jf = (oa + ogy == -1 + oJ)
            npr = (oa == d0 - 1 + oJ)
            print("   %-24s %-6s %8s %8s %8s %8s %6s %s" %
                  (lab, place, oa, ogy, oJ, d0, "yes" if proper else "NO",
                   "OK" if jf else "FAIL"))
            check("JF  %s %s" % (lab, place), jf, "%s + %s != -1 + %s" % (oa, ogy, oJ))
            check("NPR %s %s" % (lab, place), npr)
            # the Keller specialisation of (SF): if ord_t J were 0 on this branch,
            # a non-proper branch would need delta^0 = oa + 1 > 1.
            if not proper:
                check("SF  %s %s" % (lab, place), oa > 0,
                      "non-proper branch with ord_t(f-a_0) = %s" % oa)
    print("\n   checks %d, failures %d" % (NCK[0], len(FAIL)))
    return len(FAIL)

if __name__ == "__main__":
    sys.exit(1 if run() else 0)
