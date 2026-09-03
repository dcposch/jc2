#!/usr/bin/env python3
"""One-step Prop 6.3/6.4 descent (u_s = 1).  Labels n', M_i', ... never derivatives.

n' = n/d_s, m' = m/d_s, M_i' = M_i/d_s (i < s), d_i' = d_i/d_s,
V_i' = V_i (i < s), k = v_s - u_s - 1.  SOURCE-READ Prop 6.3(3), p.207 table.
"""
from __future__ import annotations

from math import gcd


def u_s_of(S):
    return S.d[S.s] - S.V[S.s]


def descend_once(S):
    """Return a dict datum or None if u_s != 1 or not integral."""
    s, ds, Vs = S.s, S.d[S.s], S.V[S.s]
    us, vs = ds - Vs, Vs
    if us != 1:
        return None
    vals = [S.n, S.m] + [S.M[i] for i in range(1, s)] + [S.d[i] for i in range(1, s + 1)]
    if any(x % ds != 0 for x in vals):
        return dict(status="NOT-INTEGRAL", us=us, vs=vs, ds=ds)
    n2, m2 = S.n // ds, S.m // ds
    k = vs - us - 1
    M2 = {i: S.M[i] // ds for i in range(1, s)}
    d2 = {i: S.d[i] // ds for i in range(1, s + 1)}
    V2 = {i: S.V[i] for i in range(2, s)}
    if s in d2 and s not in V2:
        V2[s] = d2[s]
    sprime = max(M2) if M2 else 0
    # gcd chain on descended
    chain = [n2]
    gcd_ok = True
    for i in range(1, sprime + 1):
        chain.append(gcd(chain[-1], M2[i]))
        want = d2.get(i + 1)
        if want is None or chain[-1] != want:
            gcd_ok = False
    return dict(
        status="DESCENDED",
        n=n2, m=m2, M=M2, d=d2, V=V2, k=k, s=sprime,
        us=us, vs=vs, ds=ds,
        src_n=S.n, src_m=S.m, src_s=s,
        gcd_ok=gcd_ok,
        m2_gt_m=(2 in M2) and (M2[2] > m2),
    )
