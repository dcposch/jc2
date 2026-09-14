#!/usr/bin/env python3
"""A1: verify the (6.3) grading on the exact terminal rows; degrees and support."""
import sys, sympy as sp
sys.path.insert(0, "/home/ubuntu/jc2/box/k16terminal-opus-20260903")
from tf_load import load, wt_parts

for t in [int(a) for a in sys.argv[1:]]:
    D = load(t)
    vs = D["variables"]
    print("=== t=%d  vars=%s" % (t, [str(v) for v in vs]))
    print("    H_%d = %s" % (t, D["H"]))
    ok = True
    for k in sorted(D["rows"]):
        r = D["rows"][k]
        parts = wt_parts(r, t, vs)
        ws = sorted(parts)
        p = sp.Poly(sp.expand(r), *vs)
        degs = ",".join("%s:%d" % (str(v), sp.degree(p, v)) for v in vs)
        exp = 4*t+1-k
        tag = "OK" if (ws == [exp] or (k == 0 and ws == [0, exp])) else "MISMATCH"
        if tag == "MISMATCH":
            ok = False
        print("  k=%2d exp_wt=%2d actual_wt=%-12s nmon=%4d degs=[%s] %s"
              % (k, exp, str(ws), len(p.terms()), degs, tag))
        if k == 0:
            print("       band-0 weight-0 part = %s" % parts.get(0, 0))
    print("  GRADING_%d = %s" % (t, "PASS" if ok else "FAIL"))
