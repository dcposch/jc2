#!/usr/bin/env python3
"""C2: verify the derived closed forms alpha_t, phi_t against every available
exact record (charged terminal_laurent_t{2,3,4,5}.json and the b4=0 chart
records built here), by restricting each record to the sub-chart S."""
import json, pathlib, sys, sympy as sp
sys.path.insert(0, "/home/ubuntu/jc2/box/k16terminal-opus-20260903")
from tf_load import load
HERE = pathlib.Path("/home/ubuntu/jc2/box/k16terminal-opus-20260903")

def forms(t):
    """alpha_t, phi_t and c, as elements of Q[y]/(H_t) (substituting d=2qy-(t+1))."""
    tt = sp.Integer(t); q = 2*tt+1; e = 3*tt+1
    Y = sp.Symbol("q%d_1" % (2*t+1)); d = 2*q*Y - (tt+1)
    H = sp.expand(12*q**2*Y**2 - 12*q*(tt+1)*Y + (tt+1)*(3*tt+2))
    def red(x):
        x = sp.cancel(sp.together(sp.expand(x)))
        n, dn = sp.fraction(x)
        n = sp.rem(sp.Poly(sp.expand(n), Y), sp.Poly(H, Y)).as_expr()
        return sp.expand(sp.cancel(n/dn))
    alpha = red(tt*(3*tt+1)*((27*tt**3-30*tt**2+tt-2)*d + (6*tt**3+13*tt**2-3*tt+2))
                / (12*(2*tt+1)**2*(3*tt-1)**2*(3*tt+2)))
    phi = red(-tt*(tt-2)*(3*tt+1)*(6*tt*d-(tt+1)) / (72*(2*tt+1)**3*(3*tt-1)))
    g = red(e*tt*(3*d+2*(tt+1))/(6*q**3))
    c = red(-Y*g)
    return alpha, phi, c, Y, H

def restrict(rows, t, y, b4free):
    """Terminal rows restricted to S: b4=0 and every q_{i,0}=0."""
    out = {}
    subs = {sp.Symbol("q%d_0" % j): 0 for j in range(2, t)}
    if b4free:
        subs[sp.Symbol("b4")] = 0
    for k, r in rows.items():
        out[k] = sp.expand(sp.expand(r).subs(subs))
    return out

allok = True
for t in [int(a) for a in sys.argv[1:]]:
    alpha, phi, c, Y, H = forms(t)
    b3 = sp.Symbol("b3")
    sources = []
    try:
        D = load(t)
        sources.append(("charged terminal_laurent_t%d.json" % t,
                        restrict(D["rows"], t, Y, True)))
    except Exception as ex:
        pass
    p = HERE/("chart_t%d_b4_0.json" % t)
    if p.exists():
        rec = json.loads(p.read_text())
        ns = {"b3": b3, str(Y): Y}
        ns.update({"q%d_0" % j: sp.Symbol("q%d_0" % j) for j in range(2, t)})
        rows = {it["band"]: sp.sympify(it["expr"], locals=ns) for it in rec["terminal"]}
        sources.append(("chart_t%d_b4_0.json" % t, restrict(rows, t, Y, False)))
    for name, rows in sources:
        ok = True
        msgs = []
        for k, r in rows.items():
            want = (c if k == 0 else 0)
            if k == 2*t-1:
                want = alpha*b3**2
            if k == t-2 and t >= 3:
                want = phi*b3**3
            if k == 0 and t == 2:            # t-2 = 0 coincides with the c band
                want = c + phi*b3**3
            diff = sp.simplify(sp.expand(r - want))
            if diff != 0:
                diff = sp.expand(sp.rem(sp.Poly(sp.numer(sp.cancel(diff)), Y),
                                        sp.Poly(H, Y)).as_expr())
            if sp.expand(diff) != 0:
                ok = False; msgs.append("band %d: residue %s" % (k, sp.simplify(diff)))
        allok &= ok
        print("t=%d  %-40s : %s %s" % (t, name, "MATCH" if ok else "MISMATCH",
                                       "; ".join(msgs)[:200]))
print("SUBCHART_FORMULA_CONTROL = %s" % ("PASS" if allok else "FAIL"))
