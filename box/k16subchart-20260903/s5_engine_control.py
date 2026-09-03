#!/usr/bin/env python3
"""S5: control of the fixed-t sub-chart engine (S3) against the exact records.

For every band and every monomial the two coefficients are compared inside A_t:
the engine works in Q[d]/(3d^2-t-1), the records in Q[y]/(H_t); the ring map is
d = 2(2t+1)y-(t+1), declared here and applied to the engine value.
"""
import sys, json, pathlib, sympy as sp
sys.path.insert(0, "/home/ubuntu/jc2/box/k16subchart-20260903")
from sq_load import load
HERE = pathlib.Path("/home/ubuntu/jc2/box/k16subchart-20260903")

RV = int(sys.argv[1])
FIX = json.loads((HERE/("fixed_r%d.json" % RV)).read_text())
dS = sp.Symbol("d")
ok_all = True
for arg in sys.argv[2:]:
    tv, chart = (arg.split(":") + ["spine"])[:2]
    tv = int(tv)
    if str(tv) not in FIX:
        print("=== t=%d : no engine record, skipped" % tv); continue
    D = load(tv, chart)
    y, b3, q = D["y"], D["b3"], 2*tv+1
    Hp = sp.Poly(D["H"], y)
    dval = 2*q*y - (tv+1)
    def A_red(e):
        e = sp.together(sp.expand(e)); n, de = sp.fraction(e)
        n = sp.Poly(sp.expand(n), y).rem(Hp).as_expr(); de = sp.expand(de)
        if de.has(y):
            n = sp.expand(n*sp.invert(sp.Poly(de, y), Hp).as_expr()); de = 1
        return sp.expand(sp.Poly(sp.expand(n/de), y).rem(Hp).as_expr())
    Q = sp.Symbol("q%d_0" % (tv-RV))
    zero = {v: 0 for v in D["variables"] if v not in (Q, b3)}
    rec = {}
    for k in sorted(D["rows"]):
        e = sp.expand(D["rows"][k].subs(zero))
        if e != 0:
            for mon, co in sp.Poly(e, Q, b3).terms():
                if A_red(co) != 0:
                    rec[(k, mon)] = A_red(co)
    eng = {}
    for k, mons in FIX[str(tv)]["rows"].items():
        for mon, (co, _N) in mons.items():
            a, b = [int(z) for z in mon.replace("x^", "").replace("b3^", "").split("*")]
            v = A_red(sp.sympify(co).subs(dS, dval))
            if v != 0:
                eng[(int(k), (a, b))] = v
    keys = sorted(set(rec) | set(eng))
    good = True
    for key in keys:
        same = key in rec and key in eng and A_red(rec[key]-eng[key]) == 0
        good &= same
        if not same:
            print("   MISMATCH k=%s mon=%s rec=%s eng=%s"
                  % (key[0], key[1], rec.get(key), eng.get(key)))
    ok_all &= good
    print("=== t=%d chart=%s : %d (band,monomial) pairs compared : %s"
          % (tv, chart, len(keys), "OK" if good else "FAIL"))
print("ENGINE_RECORD_CONTROL_r%d = %s" % (RV, "PASS" if ok_all else "FAIL"))
