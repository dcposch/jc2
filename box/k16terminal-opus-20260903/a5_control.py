#!/usr/bin/env python3
"""A5: control -- the b4-specialised chart runs must reproduce the b4-specialisation
of the charged full records terminal_laurent_t{2,3,4,5}.json, band by band."""
import json, pathlib, sys, sympy as sp
sys.path.insert(0, "/home/ubuntu/jc2/box/k16terminal-opus-20260903")
from tf_load import load
HERE = pathlib.Path("/home/ubuntu/jc2/box/k16terminal-opus-20260903")

allok = True
for t in [int(a) for a in sys.argv[1:]]:
    D = load(t); b4 = D["b4"]
    for chart in ("0", "1"):
        p = HERE/("chart_t%d_b4_%s.json" % (t, chart))
        if not p.exists():
            print("t=%d chart b4=%s : (not yet built)" % (t, chart)); continue
        rec = json.loads(p.read_text())
        ns = {str(v): v for v in D["variables"] + [D["y"]]}
        ok = True
        for item in rec["terminal"]:
            k = item["band"]
            got = sp.expand(sp.sympify(item["expr"], locals=ns))
            want = sp.expand(D["rows"].get(k, 0).subs(b4, sp.Integer(chart)))
            if sp.simplify(sp.expand(got-want)) != 0:
                ok = False
                print("   band %d MISMATCH" % k)
        allok &= ok
        print("t=%d chart b4=%s : %s (%d bands)"
              % (t, chart, "MATCH" if ok else "MISMATCH", len(rec["terminal"])))
print("CHART_CONTROL = %s" % ("PASS" if allok else "FAIL"))
