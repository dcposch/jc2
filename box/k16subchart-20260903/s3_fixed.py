#!/usr/bin/env python3
"""S3: the same sub-chart spine at a fixed integer t (t>=6) and offset r.

Independent evaluation of the closed forms of S1: identical construction with
t specialised before any reduction, so the two agree only if the symbolic
computation is right.  Also prints N(u) for every terminal coefficient.
"""
import sys, json, sympy as sp
sys.path.insert(0, "/home/ubuntu/jc2/box/k16subchart-20260903")
import sq_engine as S

RV = int(sys.argv[1])
OUT = {}
for TV in [int(a) for a in sys.argv[2:]]:
    S.set_r(RV); S.set_t(TV)
    from sq_engine import E, ex, red, spine, x, b3, d, c1, c2, c3, c4, c5
    t = S.t
    O = spine(has_b1=(RV == 1))
    Phi = O["Phi"]
    high = {k: v for k, v in Phi.items() if ex(k) >= 2*TV}
    order = [(E(3, 1, 1), c1), (E(3, 0, 0), c2), (E(2, 2, 1), c3), (E(2, 1, 0), c4)]
    def msplit(ee):
        """single monomial in (x,b3) times an A_t-scalar"""
        ts = sp.Poly(red(ee), x, b3).terms()
        assert len(ts) == 1, ts
        (a, b), co = ts[0]
        return (a, b), co

    SOL = {}
    for key, var in order:
        row = red(high[key].subs(SOL))
        P = sp.Poly(row, var)
        assert P.degree() == 1, (TV, var)
        ml, cl = msplit(P.nth(1))
        mr, cr = msplit(P.nth(0))
        assert ml == mr, (ml, mr)
        SOL[var] = red(-cr/cl)
    bad = [ex(k) for k in high if red(high[k].subs(SOL)) != 0]
    print("=== t=%d r=%d  high bands residual: %s" % (TV, RV, bad or "all zero"))
    rows = {}
    for k in sorted(Phi, reverse=True):
        if ex(k) >= 2*TV:
            continue
        v = red(Phi[k].subs(SOL))
        if v == 0:
            continue
        for mon, co in sp.Poly(v, x, b3).terms():
            co = red(co)
            P = sp.Poly(sp.together(co)*sp.denom(sp.together(co)), d)
            A, B = P.nth(1), P.nth(0)
            den = sp.denom(sp.together(co))
            N = sp.nsimplify((B**2 - A**2*(TV+1)/3)/den**2)
            rows.setdefault(int(ex(k)), {})["x^%d*b3^%d" % mon] = (str(co), str(N))
            print("   k=%-3d wt=%-3d x^%d b3^%d  N=%s"
                  % (ex(k), 4*TV+1-ex(k), mon[0], mon[1], N))
    OUT[TV] = {"c": {str(k): str(v) for k, v in SOL.items()}, "rows": rows}
json.dump(OUT, open("/home/ubuntu/jc2/box/k16subchart-20260903/fixed_r%d.json" % RV, "w"),
          indent=2, sort_keys=True)
