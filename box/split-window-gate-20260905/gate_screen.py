#!/usr/bin/env python3
"""Independent re-derivation of the split-window screen (hostile gate).

Written from the source derivation, NOT from box/lib/split_window.py:
  * (G) tested by explicit orbit construction over Z/Q acting on root slots,
  * (L) tested by BRUTE FORCE over all 2^r low/high assignments (no monotone
    shortcut), so the tool's "all-eligible-low is optimal" claim is audited.
"""
from fractions import Fraction as F
from math import gcd
from itertools import product
from collections import Counter


def mu_chain(n, m, Ms):
    """Report (2.1): mu_1=M_1=-m, mu_i=(d_{i-1}/d_i)mu_{i-1}+M_i-M_{i-1}."""
    M = [-m] + list(Ms)
    s = len(M)
    d = [n]
    for Mi in M:
        d.append(gcd(d[-1], Mi))
    mu = [F(M[0])]
    for i in range(1, s):
        mu.append(F(d[i - 1], d[i]) * mu[-1] + M[i] - M[i - 1])
    return s, d, [int(x) for x in mu]


def profile(n, m, Ms, Vs):
    """(u_s, v_s, W) or a typed refusal string."""
    s, d, mu = mu_chain(n, m, Ms)
    if s <= 2:
        return ("REFUSE", "s<=2")
    if (-m) + 0 != -m or ([-m] + list(Ms))[-1] != n - 2:
        return ("REFUSE", "M_s!=n-2")
    v = Vs[s]                      # V_s
    d_s = d[s - 1]                 # d[0]=n=d_1 ... d[s-1]=d_s
    u = d_s - v
    if u < 2:
        return ("NOSPLIT", u)
    if v <= u:
        return ("REFUSE", "v<=u")
    W = F(-mu[s - 1] - 2, d_s)
    if W.denominator != 1 or W < 0:
        return ("REFUSE", f"W={W}")
    return ("OK", u, v, int(W), d_s, mu[s - 1])


def window(u, v):
    """1 < rho < v/u, den(rho) <= u, reduced."""
    out = []
    for q in range(1, u + 1):
        for p in range(q + 1, (q * v - 1) // u + 1):
            if gcd(p, q) == 1:
                out.append(F(p, q))
    return sorted(set(out))


def parts(total, cap=None):
    cap = total if cap is None else cap
    if total == 0:
        yield ()
        return
    for first in range(min(total, cap), 0, -1):
        for rest in parts(total - first, first):
            yield (first,) + rest


def genuine(u):
    return [p for p in parts(u) if len(p) >= 2]


def G_ok(lam, Qd):
    """Explicit orbit construction: nonzero roots fall into free Z/Q orbits of
    equal multiplicity; at most one root (z=0) may be fixed."""
    if Qd == 1:
        return True, {"zero": None, "note": "trivial action"}
    freq = Counter(lam)
    for zero_mult in [None] + sorted(freq):
        rem = freq.copy()
        if zero_mult is not None:
            rem[zero_mult] -= 1
            if rem[zero_mult] == 0:
                del rem[zero_mult]
        if all(c % Qd == 0 for c in rem.values()):
            return True, {"zero": zero_mult,
                          "orbits": {mm: c // Qd for mm, c in sorted(rem.items())}}
    return False, {"freq_mod_Q": {mm: c % Qd for mm, c in sorted(freq.items())}}


def L_ok(lam, rho, u, v, W, brute=True):
    """Exact local dichotomy at each distinct root:
         nu = k*lam  (cancelled: a*lam - X*nu = 0), k = a/X = W - t,  nu in Z_{>=0}
         nu = W*lam + 1 (uncancelled)
       feasible iff some assignment has sum(nu) <= deg R = W*u+1."""
    X = F(u) * rho - v
    assert X < 0
    t = (rho - 1) / (v - F(u) * rho)
    k = F(W) - t
    D = W * u + 1
    opts = []
    for lm in lam:
        o = []
        nl = k * lm
        if nl.denominator == 1 and nl >= 0:
            o.append(("low", int(nl)))
        o.append(("high", W * lm + 1))
        opts.append(o)
    best, best_assign = None, None
    if brute:
        for combo in product(*opts):
            tot = sum(c[1] for c in combo)
            if best is None or tot < best:
                best, best_assign = tot, combo
    else:
        best_assign = tuple(o[0] for o in opts)
        best = sum(c[1] for c in best_assign)
    return (best <= D), {"t": str(t), "k": str(k), "X": str(X), "degR": D,
                         "min_sum_nu": best,
                         "assign": [c[0] for c in best_assign]}


def screen(n, m, Ms, Vs, brute=True):
    pr = profile(n, m, Ms, Vs)
    if pr[0] != "OK":
        return {"status": pr[0], "detail": pr[1:]}
    _, u, v, W, d_s, mus = pr
    W_ind_surv = []          # survivors under the W-INDEPENDENT (unrepaired) L
    surv, killed, gadm = [], [], 0
    orders = window(u, v)
    for rho in orders:
        for lam in genuine(u):
            g, gc = G_ok(lam, rho.denominator)
            if g:
                gadm += 1
            l, lc = L_ok(lam, rho, u, v, W, brute)
            # W-independent variant: drop the nu>=0 gate (integrality only)
            t = (rho - 1) / (v - F(u) * rho)
            k = F(W) - t
            optsW = []
            for lm in lam:
                nl = k * lm
                o = []
                if nl.denominator == 1:            # NO sign gate
                    o.append(int(nl))
                o.append(W * lm + 1)
                optsW.append(o)
            bw = min(sum(c) for c in product(*optsW))
            lW = bw <= W * u + 1
            rec = {"rho": str(rho), "Q": rho.denominator, "lam": list(lam),
                   "G": g, "L": l, "Lw": lW, "cert": {"G": gc, "L": lc}}
            (surv if (g and l) else killed).append(rec)
            if g and lW:
                W_ind_surv.append((str(rho), tuple(lam)))
    return {"status": "OK", "u": u, "v": v, "W": W, "d_s": d_s, "mu_s": mus,
            "orders": [str(o) for o in orders], "n_orders": len(orders),
            "n_parts": len(genuine(u)), "raw": len(orders) * len(genuine(u)),
            "G_admissible": gadm, "survivors": surv, "killed": killed,
            "n_surv": len(surv), "n_killed": len(killed),
            "W_independent_survivors": W_ind_surv,
            "n_surv_Windep": len(W_ind_surv)}
