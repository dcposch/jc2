#!/usr/bin/env python3
"""Loader for exact terminal records: charged spine records and b4-chart records."""
import json, pathlib, sympy as sp

SPINE = pathlib.Path("/home/ubuntu/jc2/box/k16spine-20260903")
CHART = pathlib.Path("/home/ubuntu/jc2/box/k16terminal-opus-20260903")
HERE  = pathlib.Path("/home/ubuntu/jc2/box/k16subchart-20260903")


def _paths(t, chart):
    if chart == "spine":
        return [SPINE/("terminal_laurent_t%d.json" % t)]
    return [HERE/("chart_t%d_b4_%s.json" % (t, chart)),
            CHART/("chart_t%d_b4_%s.json" % (t, chart))]


def load(t, chart="spine"):
    for p in _paths(t, chart):
        if p.exists():
            rec = json.loads(p.read_text())
            break
    else:
        raise FileNotFoundError((t, chart))
    q = 2*t+1
    y = sp.Symbol("q%d_1" % q)
    b3, b4 = sp.symbols("b3 b4")
    qv = [sp.Symbol("q%d_0" % j) for j in range(2, t)]     # q_2..q_{t-1}
    variables = ([b4] if chart in ("spine", "free") else []) + qv + [b3]
    ns = {str(v): v for v in variables + [y, b4]}
    rows = {item["band"]: sp.sympify(item["expr"], locals=ns)
            for item in rec["terminal"]}
    H = sp.sympify(rec["H"], locals=ns)
    return dict(t=t, q=q, y=y, b3=b3, b4=b4, qv=qv, variables=variables,
                rows=rows, H=H, rec=rec, path=str(p))


def weights(t, variables):
    w = {sp.Symbol("b4"): 1, sp.Symbol("b3"): t+1}
    for j in range(2, t):
        w[sp.Symbol("q%d_0" % j)] = j
    return [w[v] for v in variables]
