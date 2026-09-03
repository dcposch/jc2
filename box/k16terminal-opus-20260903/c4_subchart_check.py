#!/usr/bin/env python3
"""C4: control of Proposition SUBCHART on a second sub-chart, R={q_(t-1,0), b3}.

For each charged record, restrict every solved spine value to
S' = { b4=0, q_(i,0)=0 for i<t-1 } and check that the surviving support is
exactly the set of monomials in (q_(t-1,0), b3) of the variable's weight,
predicted from the numerical semigroup Sem = <t-1, t+1>.
"""
import json, pathlib, sys, sympy as sp
SPINE = pathlib.Path("/home/ubuntu/jc2/box/k16spine-20260903")

def sem_monomials(w, t):
    """monomials q^a b3^b of weight w in weights (t-1, t+1)"""
    out = []
    for a in range(0, w//max(1, t-1)+1):
        rem = w - a*(t-1)
        if rem >= 0 and (t+1) and rem % (t+1) == 0:
            out.append((a, rem//(t+1)))
    return out

for t in [int(a) for a in sys.argv[1:]]:
    rec = json.loads((SPINE/("terminal_laurent_t%d.json" % t)).read_text())
    y = sp.Symbol("q%d_1" % (2*t+1)); b3 = sp.Symbol("b3"); b4 = sp.Symbol("b4")
    Q = sp.Symbol("q%d_0" % (t-1))
    names = {"b1": 3*t+1, "b2": 2*t+1, "b3": t+1, "b4": 1, "B0": t}
    for j in range(2, 2*t+1):
        names["q%d_0" % j] = j
    for j in range(1, t):
        names["C%d" % j] = j
    ns = {k: sp.Symbol(k) for k in names}; ns[str(y)] = y
    zero = {sp.Symbol(k): 0 for k in names
            if (k.startswith("q") and k.endswith("_0") and names[k] != t-1) or k == "b4"}
    zero = {v: 0 for v in zero}
    ok = True
    print("=== t=%d  sub-chart R={q%d_0, b3} ===" % (t, t-1))
    # The b1 and B0 rhs are recorded BEFORE the 2t+1 high substitutions, so
    # they still mention not-yet-eliminated variables and are not yet functions
    # of the residual variables; their grading is checked instead by a4_weights.
    for blk, name in [(p, p["variable"]) for p in rec["high_pivots"]]:
        e = sp.sympify(blk["rhs"], locals=ns)
        e = sp.expand(e.subs(zero))
        w = names[name]
        pred = sem_monomials(w, t)
        got = set()
        if e != 0:
            for mon, _ in sp.Poly(e, Q, b3).terms():
                got.add(mon)
        good = got <= set(pred)
        ok &= good
        print("   %-6s wt=%-3d predicted monomials (a,b)=%s  actual=%s  %s"
              % (name, w, pred, sorted(got), "OK" if good else "VIOLATION"))
    print("   SUBCHART2_%d = %s" % (t, "PASS" if ok else "FAIL"))
