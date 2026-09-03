#!/usr/bin/env python3
"""S8: exact dim test of the restricted ideal I_{t,+}|_{S_r} in A_t[x,b3].

Certifies (3.6) at a fixed t directly from an exact record, independently of
the closed forms: DIM=0 means V(I_{t,+}) meets the (q_{t-r,0},b3)-plane only
at the origin.  A_t is encoded by adjoining y with H_t (dim is unchanged).
"""
import sys, pathlib, sympy as sp
sys.path.insert(0, "/home/ubuntu/jc2/box/k16subchart-20260903")
from sq_load import load
from sq_emit_dim import clear
HERE = pathlib.Path("/home/ubuntu/jc2/box/k16subchart-20260903")
RV = int(sys.argv[1])
for arg in sys.argv[2:]:
    tv, chart = (arg.split(":") + ["spine"])[:2]
    tv = int(tv)
    D = load(tv, chart)
    y, b3, H = D["y"], D["b3"], D["H"]
    Q = sp.Symbol("q%d_0" % (tv-RV))
    zero = {v: 0 for v in D["variables"] if v not in (Q, b3)}
    gens = []
    for k in range(1, 2*tv):
        e = sp.expand(D["rows"].get(k, 0).subs(zero))
        if e != 0:
            gens.append(clear(e, [Q, b3, y]))
    body = [str(g).replace(str(y), "Y").replace("**", "^") for g in gens] \
         + [str(clear(H, [Q, b3, y])).replace(str(y), "Y").replace("**", "^")]
    lines = ["ring R=0,(%s,b3,Y),dp;" % Q, "ideal I=", ",\n".join(body) + ";",
             "ideal G=std(I);",
             'printf("t=%d plane_r%d DIM=%%s NGENS=%%s", dim(G), size(G));' % (tv, RV),
             'printf("LEADMON=%s", lead(G));', "quit;"]
    p = HERE/("plane_t%d_r%d.sing" % (tv, RV))
    p.write_text("\n".join(lines) + "\n")
    print(p.name, "rows=%d" % len(gens))
