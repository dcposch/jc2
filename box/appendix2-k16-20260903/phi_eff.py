#!/usr/bin/env python3
"""Phi_eff: Prop 6.3 descent then Moh p.174 drop of M_h = n'-1.

Charged rule (descent-anchor-audit, delta 17(y)):
  If M'_{s'} = n'-1, drop that last exponent and set V_{s*+1} = d_{s*+1}
  on the truncated dictionaries (s* = s'-1). Then delta_i' = (k+1)*Def5.1(3)
  on the effective tuple.

Prime marks are labels, never derivatives.
"""
from __future__ import annotations

from fractions import Fraction as F

from descent_core import descend_once, u_s_of
from shape import def51, shape_bundle, phi_s2


def truncate_jacobian(D):
    """Drop M_s = n-1 (Moh p.174 Definition-Remark).  D is descend_once dict."""
    n = D["n"]
    s = D["s"]
    M = dict(D["M"])
    d = dict(D["d"])
    V = dict(D["V"])
    dropped = 0
    while s >= 1 and M.get(s) == n - 1:
        dropped += 1
        s -= 1
        M.pop(s + 1, None)
        V.pop(s + 1, None)
        if (s + 1) in d and s >= 1:
            V[s + 1] = d[s + 1]
    out = dict(D)
    out.update(s=s, M=M, d=d, V=V, dropped=dropped)
    return out


def phi_on(D):
    """(k+1)*Def5.1(3) on a (possibly truncated) descended tuple. None if den=0."""
    n, M, d, V, s, k = D["n"], D["M"], D["d"], D["V"], D["s"], D["k"]
    if s < 1 or s not in M:
        return None
    if n - M[s] - 1 == 0:
        return None
    out = []
    for i in range(1, s + 1):
        try:
            raw = def51(n, M, d, V, s, i)
        except ZeroDivisionError:
            return None
        if raw is None:
            return None
        out.append((k + 1) * raw)
    return out


def descend_phi_eff(S):
    """One Prop 6.3 step + p.174 drop.  S is a moh_skeleton_full.Skel."""
    us = u_s_of(S)
    rec = dict(
        n=S.n, m=S.m,
        M=[S.M[i] for i in range(1, S.s + 1)],
        V={i: S.V[i] for i in range(2, S.s + 1)},
        d=[S.d[i] for i in range(1, S.s + 2)],
        src_s=S.s, ds=S.d[S.s], us=us, Vs=S.V[S.s],
    )
    if us != 1:
        rec["status"] = "US-GT-1"
        return rec
    D = descend_once(S)
    if D is None or D.get("status") != "DESCENDED":
        rec["status"] = (D or {}).get("status", "NO-DESCENT")
        return rec
    den_raw = D["n"] - D["M"][D["s"]] - 1 if D["s"] in D["M"] else None
    Dt = truncate_jacobian(D)
    den_eff = None
    if Dt["s"] >= 1 and Dt["s"] in Dt["M"]:
        den_eff = Dt["n"] - Dt["M"][Dt["s"]] - 1
    rec.update(
        status="DESCENDED",
        n_prime=D["n"], m_prime=D["m"], k=D["k"],
        s_prime=D["s"],
        M_prime=[D["M"][i] for i in range(1, D["s"] + 1)],
        V_prime=dict(D["V"]),
        d_prime=dict(D["d"]),
        den_raw=den_raw,
        dropped=Dt["dropped"],
        s_eff=Dt["s"],
        M_eff=[Dt["M"][i] for i in range(1, Dt["s"] + 1)] if Dt["s"] >= 1 else [],
        V_eff=dict(Dt["V"]),
        d_eff=dict(Dt["d"]),
        den_eff=den_eff,
        phi_raw=None if den_raw == 0 else [str(x) for x in (phi_on(D) or [])],
        phi_eff=None if den_eff == 0 else [str(x) for x in (phi_on(Dt) or [])],
    )
    if Dt["s"] == 2 and 2 in Dt["M"] and 2 in Dt["V"]:
        rec["shape_args"] = dict(
            n=Dt["n"], m=Dt["m"], M2=Dt["M"][2], V2=Dt["V"][2], k=Dt["k"],
        )
    return rec


def shape_of_eff(rec):
    """shape_bundle on an s_eff=2 Phi_eff child, or a reason it is not applicable."""
    if rec.get("s_eff") != 2:
        return dict(ok=False, reason="S-EFF-NE-2", s_eff=rec.get("s_eff"))
    args = rec.get("shape_args")
    if not args:
        return dict(ok=False, reason="NO-SHAPE-ARGS")
    C = shape_bundle(args["n"], args["m"], args["M2"], args["V2"], args["k"])
    return C
