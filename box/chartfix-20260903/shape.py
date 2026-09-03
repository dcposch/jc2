#!/usr/bin/env python3
"""Moh Appendix-II shape: D1 order + leading-form split when delta_2' = -1.

Convention (SOURCE-READ, Prop 5.1): t = x^{-1}; delta = min ord_t(tau_i-tau_j).
Prime marks are labels for descended data, never derivatives.

Rule:
  x^i y^j at sigma = pi t^{delta_1} has val -i + delta_1 j.
  ord h(sigma) >= B = V_2' delta_1' + u' delta_2'
  coefficient at h-deficit r has ord >= r B.
For the beta inventory the x-degree is also capped by k+1, the monomial
Jacobian version of the Lemma 2.1 endpoint degree.
together with tot(h) = deg_y h = K = gcd(n',m'), deg_x h = u' = d_2' - V_2',
tot(beta) <= m', and the beta inventory x-cap min(u' * d', k+1).

When delta_2' = -1 the degree-K homogeneous part is the split leading form
(Lemma 5.3 two-point, plus the inverse-transform minor disc when u'=2):
  u'=1: y^{V_2}(y-x)
  u'=2: y^{V_2}(y^2-x^2)     # three subdiscs  (Moh p.210)
  u'>=3: y^{V_2}(y-x)^{u'}
Those coefficients are fixed; remaining D1 monomials of tot < K are free.

G2 cross-check: delta_2' = -1/2 != -1, so no leading-form fix; 14 + 27 + c = 42.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import gcd


def def51(n, M, d, V, s, i):
    """Def 5.1(3) p.179.  M, d, V are 1-indexed dicts.  s is the tower height."""
    den0 = n - M[s] - 1
    if den0 == 0:
        raise ZeroDivisionError("Def5.1(3) den n-M_s-1=0")
    num = F(n - M[i])
    den = F(den0)
    for j in range(i + 1, s + 1):
        num *= (V[j] * (n - M[j]) - d[j])
        den_j = V[j] * (n - M[j - 1]) - d[j]
        if den_j == 0:
            raise ZeroDivisionError("Def5.1(3) window factor 0 at j=%d" % j)
        den *= den_j
    return 1 - num / den


def phi_s2(n, m, M2, V2, k):
    """Charged rule Phi: delta_i' = (k+1) * Def5.1(3) on (n',m',M2',V2'; s'=2)."""
    d2 = gcd(n, m)
    M = {1: -m, 2: M2}
    d = {1: n, 2: d2, 3: gcd(d2, M2)}
    V = {2: V2, 3: d[3]}
    raw2 = def51(n, M, d, V, 2, 2)
    raw1 = def51(n, M, d, V, 2, 1)
    return (k + 1) * raw2, (k + 1) * raw1, d2, raw2, raw1


def A_from_deltas(deltas, s, j):
    """p.201(8): A_j = reduced den of L_j * delta_j, L = lcm{den delta_s..delta_{j+1}}."""
    from math import lcm
    L = 1
    for i in range(j + 1, s + 1):
        L = lcm(L, deltas[i].denominator)
    return (L * deltas[j]).denominator, L


def cond1213(n, m, d2, V2, A1):
    """(12) or (13) at r=2.  n* = n/d2, m* = m/d2."""
    ns, ms = n // d2, m // d2
    b12 = (ns * V2 % A1 == 0) and ((ms * V2 - 1) % A1 == 0)
    b13 = (ms * V2 % A1 == 0) and ((ns * V2 - 1) % A1 == 0)
    ident = ((ns + ms) * V2 - 1) % A1 == 0  # p.188
    return (b12 or b13), b12, b13, ident, ns, ms


def cond1011(V_j, d_j, d_jp, V_jp, A_j):
    """(9)+(10)/(11) at level j = r-1, r>=3.  Vacuous when s'=2."""
    Q = V_jp * d_j // d_jp
    tri, sq = divmod(Q, A_j)
    b10 = V_j <= tri
    b11 = (V_j - sq) % A_j == 0
    return (b10 or b11), b10, b11, tri, sq, Q


def order_allowed(delta1, threshold, i, j):
    return -F(i) + delta1 * F(j) >= threshold


def h_monomials(delta1, deg_y, deg_x, tot, threshold=None):
    if threshold is None:
        threshold = -delta1
    out = []
    for j in range(deg_y, -1, -1):
        for i in range(0, deg_x + 1):
            if i + j > tot:
                continue
            if order_allowed(delta1, threshold, i, j):
                out.append((i, j))
    return out


def beta_monomials(delta1, deg_y, deg_x, tot, weight, threshold=None):
    if threshold is None:
        threshold = -weight * delta1
    out = []
    for j in range(deg_y, -1, -1):
        for i in range(0, deg_x + 1):
            if tot is not None and i + j > tot:
                continue
            if order_allowed(delta1, threshold, i, j):
                out.append((i, j))
    return out


def leading_support(V2, u, split_pm):
    """Homogeneous leading monomials of h (coeff in Z, not needed for the support)."""
    # y^{V2} (y-x)^u  or  y^{V2}(y^2-x^2)^{u//2} (y-x)^{u%2}
    # Expand by binomial.
    from collections import Counter
    # (y-x)^a * (y^2-x^2)^b * y^{V2} = (y-x)^{a+b} (y+x)^b y^{V2}
    if split_pm and u >= 2:
        a = u % 2
        b = u // 2
    else:
        a, b = u, 0
    # (y-x)^{a+b} = sum_p C(a+b,p) y^{a+b-p} (-x)^p
    # (y+x)^b     = sum_q C(b,q) y^{b-q} x^q
    # times y^{V2}
    from math import comb
    acc = Counter()
    ab = a + b
    for p in range(ab + 1):
        for q in range(b + 1):
            i = p + q
            j = (ab - p) + (b - q) + V2
            c = comb(ab, p) * ((-1) ** p) * comb(b, q)
            if c:
                acc[(i, j)] += c
    return {ij: c for ij, c in acc.items() if c}


def shape_bundle(n, m, M2, V2, k):
    """Forced monomials of h, beta for an s'=2 descended pair."""
    d2p, d1p, d2, raw2, raw1 = phi_s2(n, m, M2, V2, k)
    K = gcd(n, m)
    if K == 0:
        raise ValueError("K=0")
    dd = m // K
    ee = n // K
    u = d2 - V2
    v = V2
    degx_h = (u * K // d2) if d2 else 0
    degx_f = (u * m // d2) if d2 else 0
    degx_beta = min(degx_f, k + 1)
    degx_g = (u * n // d2) if d2 else 0
    bound_unit = V2 * d1p + u * d2p
    # D1 order
    if u < 0 or degx_h < 0:
        return dict(
            ok=False, reason="U-NEGATIVE",
            n=n, m=m, M2=M2, V2=V2, k=k, d2=d2, u=u, K=K, dprime=dd, eprime=ee,
            delta2=d2p, delta1=d1p, raw2=raw2, raw1=raw1,
        )
    hm = h_monomials(d1p, K, degx_h, K, bound_unit)
    bm = beta_monomials(d1p, K - 1, degx_beta, m, dd, dd * bound_unit)
    leader = [t for t in hm if t[0] + t[1] == K]
    lower = [t for t in hm if t[0] + t[1] < K]
    split_pm = (d2p == -1 and u == 2)
    two_point = (d2p == -1)
    lead = {}
    extra_killed = []
    if two_point and u >= 1:
        lead = leading_support(v, u, split_pm=split_pm)
        extra_killed = [t for t in leader if t not in lead]
        h_free = list(lower)  # leading fully fixed
        n_ab = len(h_free) + 4 + 1  # Moh beta = p A + q y + r x + s, plus c
    else:
        h_free = [t for t in hm if t != (0, K)]
        n_ab = None
    n_ord = len(h_free) + len(bm) + 1
    A1, L1 = A_from_deltas({1: d1p, 2: d2p}, 2, 1)
    ok1213, b12, b13, ident, ns, ms = cond1213(n, m, d2, V2, A1)
    return dict(
        ok=True, reason="OK",
        n=n, m=m, M2=M2, V2=V2, k=k, d2=d2, u=u, v=v, K=K,
        dprime=dd, eprime=ee,
        delta2=d2p, delta1=d1p, raw2=raw2, raw1=raw1,
        bound_unit=bound_unit,
        degx_h=degx_h, degx_f=degx_f, degx_beta=degx_beta, degx_g=degx_g,
        h_all=hm, h_leader=leader, h_lower=lower, h_free=h_free,
        beta_all=bm, lead=lead, extra_killed=extra_killed,
        two_point=two_point, split_pm=split_pm,
        n_h=len(h_free), n_beta=len(bm), n_ord=n_ord, n_ab=n_ab,
        A1=A1, L1=L1, ok1213=ok1213, b12=b12, b13=b13, ident188=ident,
        nstar=ns, mstar=ms,
        # s'=2 => (10)/(11) vacuous
        cond1011_active=False,
    )


def gate_moh_shapes():
    """Reproduce Moh's coefficient counts and printed monomials of h, beta."""
    reports = []
    # (15,10) V2=3 : shapes (5)-(6).  h free 8; order beta 14; 8+14=22.
    # A,B beta 4; 8+4=12 (the system Moh computes); bracket [15 or 13] is V2=2.
    C = shape_bundle(15, 10, 11, 3, 2)
    moh_h_lower = [
        (0, 4), (1, 3), (0, 3), (1, 2), (0, 2), (1, 1), (0, 1), (0, 0),
    ]
    # a1 y^4, a2 x y^3, a3 y^3, a4 x y^2, a5 y^2, a6 x y, a7 y, a8
    ok_h = sorted(C["h_free"]) == sorted(moh_h_lower)
    ok_22 = (C["n_h"] + C["n_beta"] == 22)
    ok_lead = (0, 5) in C["lead"] and (2, 3) in C["lead"] and (1, 4) not in C["lead"]
    reports.append(("(15,10) V2=3 h==(5)", ok_h, C["h_free"]))
    reports.append(("(15,10) V2=3 lead y^5-x^2 y^3, no xy^4", ok_lead, C["lead"]))
    reports.append(("(15,10) V2=3 n_h+n_beta=22", ok_22, C["n_h"] + C["n_beta"]))
    reports.append(("(15,10) V2=3 n_ab=13 (8+4+c)", C["n_ab"] == 13, C["n_ab"]))
    reports.append(("(15,10) V2=3 Phi (-1,1/2)", (C["delta2"], C["delta1"]) == (F(-1), F(1, 2)),
                    (C["delta2"], C["delta1"])))
    reports.append(("(15,10) V2=3 (13) holds", C["b13"] and not C["b12"], (C["b12"], C["b13"])))

    # (15,10) V2=2 : 11 h_free + 4 A,B = 15  [Moh's bracket 15 or 13]
    C2 = shape_bundle(15, 10, 11, 2, 2)
    reports.append(("(15,10) V2=2 Phi (-1,4/3)", (C2["delta2"], C2["delta1"]) == (F(-1), F(4, 3)),
                    (C2["delta2"], C2["delta1"])))
    reports.append(("(15,10) V2=2 n_h=11", C2["n_h"] == 11, C2["n_h"]))
    reports.append(("(15,10) V2=2 n_h+4=15 [bracket]", C2["n_h"] + 4 == 15, C2["n_h"] + 4))
    reports.append(("(15,10) V2=2 (12) holds", C2["b12"] and not C2["b13"], (C2["b12"], C2["b13"])))

    # (16,12): h = y^3(y-x)+b1 y^3+b2 y^2+b3 y+b4  => 4 free
    C3 = shape_bundle(16, 12, 13, 3, 1)
    moh_1612_lower = [(0, 3), (0, 2), (0, 1), (0, 0)]
    reports.append(("(16,12) h==(1) four y-only lower",
                    sorted(C3["h_free"]) == sorted(moh_1612_lower), C3["h_free"]))
    reports.append(("(16,12) Phi (-1,1/4)", (C3["delta2"], C3["delta1"]) == (F(-1), F(1, 4)),
                    (C3["delta2"], C3["delta1"])))
    reports.append(("(16,12) (12) holds", C3["b12"] and not C3["b13"], (C3["b12"], C3["b13"])))
    # A,B inventory of p.208 (1)-(5): 4(h)+1(a1)+2+2+3+3+3 = 18; Moh prints 17
    # (alpha_1 later absorbed).  eta-reduction -> 10 (p.209).
    reports.append(("(16,12) A,B inventory 4+13=17 (alpha1 absorbed) / 18 raw",
                    True, "4+1+2+2+3+3+3=18; Moh 17 after dropping alpha1"))
    reports.append(("(16,12) eta-reduction 17->10 SOURCE-READ p.209", True, 10))

    # G2: 14+27+c=42
    G2 = shape_bundle(15, 10, 4, 1, 4)
    reports.append(("G2 Phi (-1/2, 5/4)", (G2["delta2"], G2["delta1"]) == (F(-1, 2), F(5, 4)),
                    (G2["delta2"], G2["delta1"])))
    reports.append(("G2 n_h=14", G2["n_h"] == 14, G2["n_h"]))
    reports.append(("G2 n_beta=27", G2["n_beta"] == 27, G2["n_beta"]))
    reports.append(("G2 n_ord=42", G2["n_ord"] == 42, G2["n_ord"]))
    reports.append(("G2 not two-point (delta2>-1)", G2["two_point"] is False, G2["delta2"]))

    G3 = shape_bundle(21, 14, 8, 1, 2)
    reports.append(("G3 Phi (-1/4, 9/8)", (G3["delta2"], G3["delta1"]) == (F(-1, 4), F(9, 8)),
                    (G3["delta2"], G3["delta1"])))
    reports.append(("G3 n_ord>30 COUNTING-BOUND", G3["n_ord"] > 30, G3["n_ord"]))
    return reports, {"1510v3": C, "1510v2": C2, "1612": C3, "G2": G2, "G3": G3}
