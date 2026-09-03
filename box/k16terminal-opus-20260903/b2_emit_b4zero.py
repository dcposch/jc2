#!/usr/bin/env python3
"""B2: RESIDUAL-ZERO in cone form, from the b4=0 chart records.

I_{t,+}|_{b4=0} = <T_{t,k}|_{b4=0} : 1<=k<2t> is weighted homogeneous in
b3 (weight t+1) and q_{i,0} (weight i), so

    RESIDUAL-ZERO  <=>  V(I_{t,+}|_{b4=0}) = {0}  <=>  dim = 0.

H_t is irreducible over Q unless t=3s^2-1 (t=2,11,26,...); for those we branch.
"""
import json, pathlib, sys, sympy as sp
HERE = pathlib.Path("/home/ubuntu/jc2/box/k16terminal-opus-20260903")

def emit(t, char=0):
    rec = json.loads((HERE/("chart_t%d_b4_0.json" % t)).read_text())
    y = sp.Symbol("q%d_1" % (2*t+1))
    b3 = sp.Symbol("b3")
    qv = [sp.Symbol("q%d_0" % j) for j in range(2, t)]
    vs = qv + [b3]
    wts = list(range(2, t)) + [t+1]
    ns = {str(v): v for v in vs + [y]}
    H = sp.sympify(rec["H"], locals=ns)
    rows = {it["band"]: sp.sympify(it["expr"], locals=ns) for it in rec["terminal"]}
    fac = sp.factor_list(sp.Poly(H, y))
    split = len(fac[1]) > 1 or fac[1][0][1] > 1
    jobs = ([("branch%d" % i, None, {y: sp.nsimplify(r)})
             for i, r in enumerate(sorted(sp.Poly(H, y).all_roots()))] if split
            else [("field", sp.Poly(H, y).monic().as_expr(), {})])
    paths = []
    for tag, minp, subs in jobs:
        allv = vs + ([y] if minp is not None else [])
        gens = []
        for k in range(1, 2*t):
            e = sp.expand(rows.get(k, 0).subs(subs))
            if e == 0:
                continue
            pp = sp.Poly(e, *allv, domain="QQ")
            den = 1
            for co in pp.coeffs():
                den = sp.ilcm(den, sp.Rational(co).q)
            pp = sp.Poly(sp.expand(e*den), *allv, domain="QQ")
            gens.append(sp.expand(pp.as_expr()/sp.gcd(list(pp.coeffs()))))
        names = ",".join(str(v) for v in vs)
        if minp is None:
            hdr = "ring R=%d,(%s),wp(%s);\n" % (char, names, ",".join(map(str, wts)))
        else:
            hdr = ("ring R=(%d,Y),(%s),wp(%s);\nminpoly=%s;\n"
                   % (char, names, ",".join(map(str, wts)),
                      str(minp).replace(str(y), "Y").replace("**", "^")))
        body = ["ideal I=" + ",\n".join(
            str(g).replace(str(y), "Y").replace("**", "^") for g in gens) + ";",
            "ideal G=std(I);",
            'printf("b4zero t=%d %s char=%d NGEN=%d DIM=%%s SIZE=%%s", dim(G), size(G));'
            % (t, tag, char, len(gens)),
            'printf("LEADMON=%s", simplify(lead(G),1));',
            "quit;"]
        p = HERE/("b4zero_dim_t%d_%s%s.sing" % (t, tag, "" if char==0 else "_p%d"%char))
        p.write_text(hdr + "\n".join(body) + "\n")
        paths.append(str(p))
    return paths

CHAR = 0
args = sys.argv[1:]
if args and args[0].startswith("--p"):
    CHAR = int(args[0][3:]); args = args[1:]
for t in [int(a) for a in args]:
    for p in emit(t, CHAR):
        print(p)
