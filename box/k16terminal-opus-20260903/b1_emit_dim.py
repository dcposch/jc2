#!/usr/bin/env python3
"""B1: emit the *homogeneous* dimension test for the positive terminal bands.

By Lemma CONE (report Sec.3) the ideal I_{t,+}=<T_{t,1},...,T_{t,2t-1}> is
weighted homogeneous for wt(b4)=1, wt(q_{i,0})=i, wt(b3)=t+1.  Hence its
variety is a weighted cone and

    dim V(I_{t,+}) = 0   <=>   V(I_{t,+}) = {origin}   =>   (8.1).

A homogeneous std is far cheaper than the inhomogeneous unit test used by the
producer, which timed out at t=5 on the b4=1 chart.

H_t is reducible over Q exactly when t=3s^2-1, so for t=2 (s=1) we branch to
the two rational fibres and for 3<=t<=10 we use the quadratic extension field.
"""
import sys, pathlib, sympy as sp
sys.path.insert(0, "/home/ubuntu/jc2/box/k16terminal-opus-20260903")
from tf_load import load
HERE = pathlib.Path("/home/ubuntu/jc2/box/k16terminal-opus-20260903")

def emit(t, char=0):
    D = load(t); y, H = D["y"], D["H"]
    vs = D["variables"]                      # [b4, q2..q_{t-1}, b3]
    wts = [1] + list(range(2, t)) + [t+1]
    names = [str(v) for v in vs]
    fac = sp.factor_list(sp.Poly(H, y))
    split = len(fac[1]) > 1 or fac[1][0][1] > 1
    jobs = []
    if split:
        roots = sorted(sp.Poly(H, y).all_roots())
        for i, r in enumerate(roots):
            subs = {y: sp.nsimplify(r)}
            jobs.append(("branch%d" % i, None, subs))
    else:
        Hm = sp.Poly(H*sp.Integer(1), y).monic().as_expr()
        jobs.append(("field", sp.expand(Hm), {}))
    out = []
    for tag, minp, subs in jobs:
        gens = []
        allv = vs + ([y] if minp is not None else [])
        for k in range(1, 2*t):
            e = sp.expand(D["rows"][k].subs(subs))
            if e == 0:
                continue
            pp = sp.Poly(e, *allv, domain="QQ")
            den = 1
            for co in pp.coeffs():
                den = sp.ilcm(den, sp.Rational(co).q)
            pp = sp.Poly(sp.expand(e*den), *allv, domain="QQ")
            num = sp.gcd(list(pp.coeffs()))
            gens.append(sp.expand(pp.as_expr()/num))
        if minp is None:
            hdr = 'ring R=%d,(%s),wp(%s);\n' % (char, ",".join(names), ",".join(map(str, wts)))
        else:
            hdr = ('ring R=(%d,Y),(%s),wp(%s);\nminpoly=%s;\n'
                   % (char, ",".join(names), ",".join(map(str, wts)),
                      str(minp).replace(str(y), "Y").replace("**", "^")))
        body = ["ideal I="]
        strs = [str(g).replace(str(y), "Y").replace("**", "^") for g in gens]
        body.append(",\n".join(strs) + ";")
        body.append("ideal G=std(I);")
        body.append('printf("t=%s %s char=%s DIM=%%s NGENS=%%s", dim(G), size(G));' % (t, tag, char))
        body.append('printf("LEAD=%s", lead(G));')
        body.append("quit;")
        path = HERE/("dimtest_t%d_%s%s.sing" % (t, tag, "" if char==0 else "_p%d"%char))
        path.write_text(hdr + "\n".join(body) + "\n")
        out.append(str(path))
    return out

CHAR = 0
args = sys.argv[1:]
if args and args[0].startswith("--p"):
    CHAR = int(args[0][3:]); args = args[1:]
for t in [int(a) for a in args]:
    for p in emit(t, CHAR):
        print(p)
