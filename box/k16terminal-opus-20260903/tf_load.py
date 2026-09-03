#!/usr/bin/env python3
"""Shared loader for the exact terminal Laurent records (box/k16spine-20260903)."""
import json, pathlib, sympy as sp

SPINE = pathlib.Path("/home/ubuntu/jc2/box/k16spine-20260903")

def load(t):
    rec = json.loads((SPINE/("terminal_laurent_t%d.json" % t)).read_text())
    q = 2*t+1
    y = sp.Symbol("q%d_1" % q)
    b3, b4 = sp.symbols("b3 b4")
    qv = [sp.Symbol("q%d_0" % j) for j in range(2, t)]     # q_2..q_{t-1}
    variables = [b4] + qv + [b3]
    ns = {str(v): v for v in variables + [y]}
    rows = {}
    for item in rec["terminal"]:
        rows[item["band"]] = sp.sympify(item["expr"], locals=ns)
    H = sp.sympify(rec["H"], locals=ns)
    return dict(t=t, q=q, y=y, b3=b3, b4=b4, qv=qv, variables=variables,
                rows=rows, H=H, rec=rec)

def weight(t):
    """wt(b4)=1, wt(q_i0)=i, wt(b3)=t+1."""
    w = {sp.Symbol("b4"): 1, sp.Symbol("b3"): t+1}
    for j in range(2, t):
        w[sp.Symbol("q%d_0" % j)] = j
    return w

def wt_parts(expr, t, variables):
    """Split expr into weighted-homogeneous parts (dict weight -> expr)."""
    w = weight(t)
    p = sp.Poly(sp.expand(expr), *variables)
    out = {}
    for mon, coeff in p.terms():
        ww = sum(w[v]*a for v, a in zip(variables, mon))
        term = coeff*sp.prod([v**a for v, a in zip(variables, mon)])
        out[ww] = out.get(ww, 0) + term
    return {k: sp.expand(v) for k, v in out.items()}
