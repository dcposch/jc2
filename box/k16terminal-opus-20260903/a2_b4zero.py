#!/usr/bin/env python3
"""A2: the b4=0 restriction of the terminal rows; factored form and support."""
import sys, sympy as sp
sys.path.insert(0, "/home/ubuntu/jc2/box/k16terminal-opus-20260903")
from tf_load import load

for t in [int(a) for a in sys.argv[1:]]:
    D = load(t); b4 = D["b4"]; y = D["y"]
    res = [v for v in D["variables"] if v != b4]
    print("=== t=%d  b4=0 chart, residual vars %s" % (t, [str(v) for v in res]))
    for k in sorted(D["rows"]):
        r = sp.expand(D["rows"][k].subs(b4, 0))
        if r == 0:
            print("  k=%2d : 0" % k); continue
        p = sp.Poly(r, *res) if res else None
        mons = [sp.prod([v**a for v, a in zip(res, m)]) for m, _ in p.terms()] if p else []
        print("  k=%2d : nmon=%d  monomials=%s" % (k, len(mons), [str(m) for m in mons]))
        if len(mons) <= 6:
            print("        %s" % sp.factor(r))
