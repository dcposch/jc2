#!/usr/bin/env python3
"""Exact STRICT-window arithmetic, with the omitted delta*=1 control.

Mathematical premise, proved in the report from the first split of the
invariant principal minor disc: before v/u, all retained initial polynomials
are powers of one degree-u polynomial; its nonzero root orbit has length
den(delta*), so den(delta*) <= u. This is not an arbitrary search cap.
For u=2 the two distinct-root pattern has multiplicities (1,1).
Prop6.1 prints delta*>=1, so these strict-window checks alone are NOT a
Prop6.3 licence. In particular the boundary identity has polynomial solutions.
"""
from fractions import Fraction as Q
import json
from pathlib import Path


def window(u, v):
    return sorted({Q(a, b) for b in range(1, u + 1)
                   for a in range(b + 1, v * b // u + 1)
                   if 1 < Q(a, b) < Q(v, u)})


def certificate(u, v):
    assert u == 2 and v in (3, 4)
    values = window(u, v)
    if v == 3:
        assert values == []
        return dict(type="DETERMINED", u=u, v=v, window=[], forced_R=False,
                    reason="No first-split denominator <=2 in (1,3/2)")
    assert values == [Q(3, 2)]
    delta = values[0]
    t = (delta - 1) / (v - u * delta)
    assert t == Q(1, 2)
    # k=W-t. Each lambda=1 is high because k*lambda is not integral.
    # Hence sum nu = (W+1)+(W+1) > deg q = 2W+1, for every integral W.
    controls = []
    for W in (1, 5, 17, 59, 1000):
        k = W - t
        assert k.denominator == 2 and 2 * (W + 1) > 2 * W + 1
        controls.append(dict(W=W, k=str(k), sum_nu=2 * (W + 1), q_degree=2 * W + 1))
    return dict(type="DETERMINED", u=u, v=v, window=[str(delta)], forced_R=False,
                partition=[1, 1], t=str(t), symbolic_excess=1, controls=controls,
                reason="Both factors high; 2W+2 roots cannot fit squarefree q of degree 2W+1")


def boundary_control():
    def mul(a, b):
        c = [0] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                c[i + j] += x * y
        return c
    def derivative(a):
        return [i * a[i] for i in range(1, len(a))]
    p = [0, -1, 1]  # pi(pi-1)
    W = 2
    pp = mul(p, p)
    q = mul([2, 1], pp)  # (pi+2)p^W
    lhs = mul(p, derivative(q))
    correction = mul(q, derivative(p))
    rhs = mul(pp, p)
    assert [x - W * y for x, y in zip(lhs, correction)] == rhs
    return dict(type="DETERMINED", delta=1, W=W, p=p, q=q,
                equation="p q_dot - W q p_dot = p^(W+1)", residual_zero=True,
                status="OPEN_RADIUS_BOUNDARY; face solution is not a source pair")


if __name__ == "__main__":
    out = dict(strict_window=[certificate(2, v) for v in (3, 4)],
               boundary=boundary_control())
    Path(__file__).with_name("radius-controls.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))
