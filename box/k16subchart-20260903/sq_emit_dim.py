#!/usr/bin/env python3
"""Emit weighted-homogeneous dim tests for I_{t,+} (Lemma CONE, Cor. C1).

Two encodings of A_t = Q[y]/(H_t):
  --minpoly : Singular algebraic extension  ring R=(0,Y),(vars),wp(...); minpoly=..
  --yvar    : y adjoined as an ordinary variable with H_t added to the ideal,
              ordering dp.  dim V(I + (H_t)) in A^{n+1} equals dim V(I) in A^n
              because H_t=0 cuts out a finite (2-point) fibre over each point.
The second avoids all algebraic-extension arithmetic and is much cheaper.
Split index t=2 (H_2 reducible over Q) is branched to its two rational fibres.
"""
import sys, pathlib, sympy as sp
sys.path.insert(0, "/home/ubuntu/jc2/box/k16subchart-20260903")
from sq_load import load, weights
HERE = pathlib.Path("/home/ubuntu/jc2/box/k16subchart-20260903")


def clear(e, gens):
    pp = sp.Poly(sp.expand(e), *gens, domain="QQ")
    den = 1
    for co in pp.coeffs():
        den = sp.ilcm(den, sp.Rational(co).q)
    pp = sp.Poly(sp.expand(e*den), *gens, domain="QQ")
    num = sp.gcd(list(pp.coeffs()))
    return sp.expand(pp.as_expr()/num)


def emit(t, chart, mode, char=0):
    D = load(t, chart)
    y, H, vs = D["y"], D["H"], D["variables"]
    wts = weights(t, vs)
    tag = "%s_%s" % (chart, mode)
    fac = sp.factor_list(sp.Poly(H, y))
    split = len(fac[1]) > 1 or fac[1][0][1] > 1
    jobs = []
    if split:
        for i, rt in enumerate(sorted(sp.Poly(H, y).all_roots())):
            jobs.append(("branch%d" % i, {y: sp.nsimplify(rt)}))
    else:
        jobs.append(("field", {}))
    out = []
    for btag, subs in jobs:
        rows = []
        for k in range(1, 2*t):
            e = sp.expand(D["rows"].get(k, 0).subs(subs))
            if e != 0:
                rows.append(e)
        if subs or mode == "minpoly":
            allv = list(vs) + ([] if subs else [y])
            gens = [clear(e, allv) for e in rows]
            if subs:
                hdr = "ring R=%d,(%s),wp(%s);\n" % (
                    char, ",".join(map(str, vs)), ",".join(map(str, wts)))
                extra = []
            else:
                Hm = sp.Poly(H, y).monic().as_expr()
                hdr = ("ring R=(%d,Y),(%s),wp(%s);\nminpoly=%s;\n" % (
                    char, ",".join(map(str, vs)), ",".join(map(str, wts)),
                    str(sp.expand(Hm)).replace(str(y), "Y").replace("**", "^")))
                extra = []
            body = [str(g).replace(str(y), "Y").replace("**", "^") for g in gens]
        else:                                   # yvar encoding
            allv = list(vs) + [y]
            gens = [clear(e, allv) for e in rows] + [clear(H, allv)]
            hdr = "ring R=%d,(%s,Y),dp;\n" % (char, ",".join(map(str, vs)))
            body = [str(g).replace(str(y), "Y").replace("**", "^") for g in gens]
            extra = []
        lines = [hdr, "ideal I=", ",\n".join(body) + ";",
                 "option(redTail);", "ideal G=std(I);",
                 'printf("t=%d %s %s char=%d DIM=%%s NGENS=%%s", dim(G), size(G));'
                 % (t, tag, btag, char),
                 'printf("LEADMON=%s", lead(G));', "quit;"]
        path = HERE/("dim_t%d_%s_%s%s.sing" % (t, tag, btag,
                                               "" if char == 0 else "_p%d" % char))
        path.write_text("\n".join(lines) + "\n")
        out.append(str(path))
    return out


if __name__ == "__main__":
    args = sys.argv[1:]
    chart, mode, char = "spine", "yvar", 0
    rest = []
    for a in args:
        if a.startswith("--chart="):
            chart = a.split("=")[1]
        elif a.startswith("--mode="):
            mode = a.split("=")[1]
        elif a.startswith("--p"):
            char = int(a[3:])
        else:
            rest.append(int(a))
    for t in rest:
        for p in emit(t, chart, mode, char):
            print(p)
