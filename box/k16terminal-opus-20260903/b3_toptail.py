#!/usr/bin/env python3
"""B3: TOP-TAIL-UNIT (8.2) re-verified from the b4=1 chart records:
    <T_{t,t},...,T_{t,2t-1}>|_{b4=1} = [1] ?
plus the b3-degree statement proved by the grading:  deg_{b3} T_{t,k} <= 2 for
k >= t-1, and [b3^2] T_{t,2t-1} is a weight-0 scalar (= alpha_t)."""
import json, pathlib, sys, sympy as sp
HERE = pathlib.Path("/home/ubuntu/jc2/box/k16terminal-opus-20260903")

for t in [int(a) for a in sys.argv[1:]]:
    p = HERE/("chart_t%d_b4_1.json" % t)
    if not p.exists():
        print("t=%d : b4=1 chart not built" % t); continue
    rec = json.loads(p.read_text())
    y = sp.Symbol("q%d_1" % (2*t+1)); b3 = sp.Symbol("b3")
    qv = [sp.Symbol("q%d_0" % j) for j in range(2, t)]
    vs = qv + [b3]
    ns = {str(v): v for v in vs + [y]}
    H = sp.sympify(rec["H"], locals=ns)
    rows = {it["band"]: sp.sympify(it["expr"], locals=ns) for it in rec["terminal"]}
    degs = {k: sp.degree(sp.Poly(sp.expand(rows[k]), b3), b3) for k in sorted(rows)}
    print("t=%d  deg_b3 by band: %s" % (t, degs))
    fac = sp.factor_list(sp.Poly(H, y))
    split = len(fac[1]) > 1 or fac[1][0][1] > 1
    jobs = ([("branch%d" % i, None, {y: sp.nsimplify(r)})
             for i, r in enumerate(sorted(sp.Poly(H, y).all_roots()))] if split
            else [("field", sp.Poly(H, y).monic().as_expr(), {})])
    for tag, minp, subs in jobs:
        allv = vs + ([y] if minp is not None else [])
        gens = []
        for k in range(t, 2*t):
            e = sp.expand(rows[k].subs(subs))
            if e == 0:
                continue
            pp = sp.Poly(e, *allv, domain="QQ")
            den = 1
            for co in pp.coeffs():
                den = sp.ilcm(den, sp.Rational(co).q)
            pp = sp.Poly(sp.expand(e*den), *allv, domain="QQ")
            gens.append(sp.expand(pp.as_expr()/sp.gcd(list(pp.coeffs()))))
        names = ",".join(str(v) for v in vs)
        hdr = ("ring R=0,(%s),dp;\n" % names if minp is None else
               "ring R=(0,Y),(%s),dp;\nminpoly=%s;\n"
               % (names, str(minp).replace(str(y), "Y").replace("**", "^")))
        body = ["ideal I=" + ",\n".join(str(g).replace(str(y), "Y").replace("**", "^")
                                       for g in gens) + ";",
                "ideal G=std(I);",
                'printf("TOPTAIL t=%d %s rows=%d UNIT=%%s DIM=%%s",'
                ' (size(G)==1 && G[1]==1), dim(G));' % (t, tag, len(gens)),
                "quit;"]
        q = HERE/("toptail_t%d_%s.sing" % (t, tag))
        q.write_text(hdr + "\n".join(body) + "\n")
        print("  wrote", q.name)
