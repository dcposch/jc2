#!/usr/bin/env python3
"""S7: the sub-chart restriction as a Groebner degeneration.

Let w give weight 0 to the variables of R and 1 to the others, and let in_w(f)
be the sum of the terms of MINIMAL w-degree.  Then f|_{S_R} = in_w(f) when that
minimum is 0, and in_w(f) has positive w-degree otherwise.  For a homogeneous
ideal I and any weight vector,  dim <in_w(f) : f in G>  >=  dim in_w(I) = dim I.

So  dim <in_w(G)> = 0  certifies dim I = 0 outright, at a fraction of the cost.
This emits that test; the sub-chart rows of S1/S4 are the w-degree-0 part of it.
"""
import sys, pathlib, sympy as sp
sys.path.insert(0, "/home/ubuntu/jc2/box/k16subchart-20260903")
from sq_load import load, weights
from sq_emit_dim import clear
HERE = pathlib.Path("/home/ubuntu/jc2/box/k16subchart-20260903")

RV = int(sys.argv[1])
for arg in sys.argv[2:]:
    tv, chart = (arg.split(":") + ["spine"])[:2]
    tv = int(tv)
    D = load(tv, chart)
    y, b3, H, vs = D["y"], D["b3"], D["H"], D["variables"]
    Q = sp.Symbol("q%d_0" % (tv-RV))
    R = {Q, b3}
    wv = [0 if v in R else 1 for v in vs]
    gens = []
    for k in range(1, 2*tv):
        e = sp.expand(D["rows"].get(k, 0))
        if e == 0:
            continue
        P = sp.Poly(e, *vs)
        best = min(sum(a*w for a, w in zip(mon, wv)) for mon, _ in P.terms())
        ini = sum(co*sp.prod([v**a for v, a in zip(vs, mon)])
                  for mon, co in P.terms()
                  if sum(a*w for a, w in zip(mon, wv)) == best)
        gens.append((k, best, sp.expand(ini)))
    print("=== t=%d chart=%s  R={%s,b3}  w-degree of in_w per band:" % (tv, chart, Q))
    print("   " + ", ".join("k%d:%d" % (k, b) for k, b, _ in gens))
    allv = list(vs) + [y]
    body = [str(clear(g, allv)).replace(str(y), "Y").replace("**", "^")
            for _, _, g in gens] + [str(clear(H, allv)).replace(str(y), "Y").replace("**", "^")]
    lines = ["ring R=0,(%s,Y),dp;" % ",".join(map(str, vs)), "ideal I=",
             ",\n".join(body) + ";", "ideal G=std(I);",
             'printf("t=%d initial_r%d chart=%s DIM=%%s NGENS=%%s", dim(G), size(G));' % (tv, RV, chart),
             'printf("LEADMON=%s", lead(G));', "quit;"]
    p = HERE/("initial_t%d_r%d_%s.sing" % (tv, RV, chart))
    p.write_text("\n".join(lines) + "\n")
    print("   emitted", p.name)
