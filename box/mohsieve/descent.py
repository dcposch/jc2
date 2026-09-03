#!/usr/bin/env python3
"""Moh Prop 6.3 / 6.4 descent as a machine (Fable §5), gated on the p.207 table.

For a (1)–(13) skeleton with u_s = d_s − V_s = 1 emit
    n' = n/d_s, m' = m/d_s, M_i' = M_i/d_s (i ≤ s−1), d_i' = d_i/d_s,
    Jacobian exponent k = v_s − 2
and recurse while u_{s'} = 1, re-running the (1)–(7) gcd/window checks and
M_2' > m'.  The engine TRANSFORMS; it does not kill D = 64, 75, 84, 99 (G8).

u_s > 1 is not Prop 6.3: those rows need the p.209 minor-disc dichotomy.
The (99,66) linear-power branch (n' = u_s n/d_s, k = v_s − u_s − 1 = 4) is a
cross-check of GPT-5.5's Appendix-II X^4 signature, not a general filter.

Load-bearing checks use require(); no ast.Assert in this file.
"""
from __future__ import annotations

import os
import sys
import time
from fractions import Fraction as F
from math import gcd

_HERE = os.path.dirname(os.path.abspath(__file__))
_BOX = os.path.dirname(_HERE)
if _BOX not in sys.path:
    sys.path.insert(0, _BOX)

import moh_skeleton_full as MS  # noqa: E402
try:
    from .gates import require, fail_closed, reset, FAILURES
except ImportError:
    from gates import require, fail_closed, reset, FAILURES  # noqa: E402

# p.207 transformed table (census-rebase §3; GPT-5.5 Card 1 signatures).
# Jacobian column: X^k with k = v_s − 2 when u_s = 1.
P207 = {
    "(64,48)": dict(n=16, m=12, M2=13, k=1, tag="X"),
    "(84,56) M2=64,V2=2": dict(n=21, m=14, M2=16, k=1, tag="X"),
    "(84,56) M2=72,V2=5": dict(n=21, m=14, M2=18, k=1, tag="X"),
    "(75,50) V2=3": dict(n=15, m=10, M2=11, k=2, tag="X^2"),
    "(75,50) V2=2": dict(n=15, m=10, M2=11, k=2, tag="X^2"),
}

# GPT-5.5 fourth-case X^4 branch for (99,66), u_s=3: Fable p.209 linear-power.
P209_9966_LINEAR = dict(n=27, m=18, M2=21, V2=8, k=4, tag="X^4")


def jac_tag(k):
    if k == 1:
        return "X"
    if k == 2:
        return "X^2"
    if k == 4:
        return "X^4"
    return "X^%d" % k


def u_s_of(S):
    return S.d[S.s] - S.V[S.s]


class Datum:
    """Puiseux-characteristic datum; M_s need not equal n-2 (descended)."""

    __slots__ = (
        "n", "m", "s", "M", "d", "V", "k", "status", "m2_gt_m",
        "windows", "gcd_ok", "src_n", "src_m",
    )

    def __init__(self, n, m, M, d, V, k, status, src_n, src_m):
        self.n, self.m = n, m
        self.M, self.d, self.V = dict(M), dict(d), dict(V)
        self.s = max(self.M)
        self.k = k
        self.status = status
        self.src_n, self.src_m = src_n, src_m
        self.m2_gt_m = (2 in self.M) and (self.M[2] > self.m)
        self.gcd_ok = self._gcd_ok()
        self.windows = self._windows_ok()

    def _gcd_ok(self):
        chain = [self.n]
        for i in range(1, self.s + 1):
            chain.append(gcd(chain[-1], self.M[i]))
        for i, val in enumerate(chain):
            want = self.d.get(i + 1)
            if want is None or val != want:
                return False
        return True

    def _windows_ok(self):
        # Def 5.1(2) / search (7) on the inherited V, with V_{s+1} := d_{s+1}
        # if present else 1.  s=1 has no window.
        if self.s < 2:
            return True
        n, M, d, V, s = self.n, self.M, self.d, self.V, self.s
        Vtop = dict(V)
        d_next = d.get(s + 1)
        if d_next is None:
            d_next = gcd(d[s], n - 2) if False else 1
        if (s + 1) not in Vtop:
            Vtop[s + 1] = d_next
        for i in range(2, s + 1):
            if i not in Vtop or i not in d or i not in M:
                return False
            den = n - M[i]
            if den == 0:
                return False
            lo = F(d[i], den)
            dnext = d.get(i + 1, 1)
            if dnext == 0:
                return False
            hi = F(Vtop.get(i + 1, 1) * d[i], dnext)
            if not (Vtop[i] > lo and Vtop[i] <= hi):
                return False
        return True

    def summary(self):
        Ms = [self.M[i] for i in range(2, self.s + 1)]
        return (self.n, self.m, tuple(Ms), self.k, self.status,
                self.m2_gt_m, self.windows, self.gcd_ok)


def from_skel(S):
    M = dict(S.M)
    d = dict(S.d)
    V = {i: S.V[i] for i in range(2, S.s + 2)}
    return Datum(S.n, S.m, M, d, V, k=None, status="SOURCE",
                 src_n=S.n, src_m=S.m)


def _divides(vals, ds):
    return all(x % ds == 0 for x in vals)


def descend_once(D):
    """One Prop 6.3 step. Requires u_s = 1. Returns (Datum|None, flag)."""
    s = D.s
    ds = D.d[s]
    Vs = D.V[s]
    us = ds - Vs
    if us != 1:
        return None, "US-GT-1"
    # G7: M_i / d_s integral for i = 1..s-1; n, m, d_i likewise.
    if not _divides([D.n, D.m] + [D.M[i] for i in range(1, s)]
                    + [D.d[i] for i in range(1, s + 1)], ds):
        return None, "NOT-INTEGRAL"
    n2, m2 = D.n // ds, D.m // ds
    k = Vs - 2
    M2 = {i: D.M[i] // ds for i in range(1, s)}          # drop M_s
    d2 = {i: D.d[i] // ds for i in range(1, s + 1)}       # d_s' = 1
    V2 = {i: D.V[i] for i in range(2, s)}                 # drop V_s
    if (s) in d2 and (s) not in V2:
        V2[s] = d2[s]                                     # V_{s'+1} = d_{s'+1} = 1
    status = "DESCENDED"
    T = Datum(n2, m2, M2, d2, V2, k=k, status=status,
              src_n=D.src_n, src_m=D.src_m)
    if not T.gcd_ok:
        T.status = "GCD-FAIL"
    elif not T.windows:
        T.status = "WINDOW-FAIL"
    elif T.s >= 2 and not T.m2_gt_m:
        T.status = "M2-LE-M"
    else:
        T.status = "TERMINAL" if T.s < 3 or T.d[T.s] < 4 else "DESCENDED-IN-SPACE"
    return T, T.status


def recurse(D, cap=8):
    """Iterate Prop 6.3 while u_{s'} = 1. Returns the chain including source."""
    chain = [D]
    cur = D
    for _ in range(cap):
        if cur.s < 2 or cur.d.get(cur.s, 1) < 1:
            break
        if cur.s not in cur.V:
            break
        us = cur.d[cur.s] - cur.V[cur.s]
        if us != 1:
            break
        nxt, flag = descend_once(cur)
        if nxt is None:
            cur = Datum(cur.n, cur.m, cur.M, cur.d, cur.V, cur.k,
                        flag, cur.src_n, cur.src_m)
            chain.append(cur)
            break
        chain.append(nxt)
        cur = nxt
        if flag in ("NOT-INTEGRAL", "GCD-FAIL", "WINDOW-FAIL"):
            break
        if nxt.s < 2:
            break
    return chain


def minor_linear_branch(S):
    """p.209 linear-power alternative when u_s > 1 (not Prop 6.3).

    n' = u_s n/d_s, m' = u_s m/d_s, M_i' = u_s M_i/d_s, k = v_s − u_s − 1.
    """
    ds = S.d[S.s]
    Vs = S.V[S.s]
    us = ds - Vs
    if us <= 1:
        return None
    if not _divides([S.n, S.m] + [S.M[i] for i in range(1, S.s)], ds):
        return None
    n2 = us * S.n // ds
    m2 = us * S.m // ds
    k = Vs - us - 1
    M2 = {i: us * S.M[i] // ds for i in range(1, S.s)}
    d2 = {i: S.d[i] // ds for i in range(1, S.s + 1)}
    V2 = {i: S.V[i] for i in range(2, S.s)}
    return Datum(n2, m2, M2, d2, V2, k=k, status="MINOR-LINEAR",
                 src_n=S.n, src_m=S.m)


def first_descent(S):
    D = from_skel(S)
    us = u_s_of(S)
    if us != 1:
        return D, "US-GT-1", us
    chain = recurse(D)
    if len(chain) == 1:
        return chain[0], "NO-STEP", us
    return chain[1], chain[1].status, us


def p207_check():
    print("\n== G6: Moh's six rows vs the p.207 transformed table ==")
    for (n, m, Ms, Vs, lab, _, _, _) in MS.MOH_TABLE:
        S = MS.Skel(n, m, Ms, Vs)
        T, status, us = first_descent(S)
        want = P207.get(lab)
        print("   %-24s u_s=%d  -> n'=%s m'=%s M2'=%s k=%s tag=%s status=%s"
              % (lab, us,
                 getattr(T, "n", None) if us == 1 else None,
                 getattr(T, "m", None) if us == 1 else None,
                 T.M.get(2) if us == 1 else None,
                 T.k if us == 1 else None,
                 jac_tag(T.k) if (us == 1 and T.k is not None) else None,
                 status if us == 1 else "US-GT-1"))
        if want is None:
            require("G6 %s has u_s>1 so no Prop 6.3 row (p.207 excludes (99,66))"
                    % lab, us > 1, "u_s=%s" % us)
            continue
        require("G6 %s n'" % lab, T.n == want["n"], "%s vs %s" % (T.n, want["n"]))
        require("G6 %s m'" % lab, T.m == want["m"], "%s vs %s" % (T.m, want["m"]))
        require("G6 %s M2'" % lab, T.M.get(2) == want["M2"],
                "%s vs %s" % (T.M.get(2), want["M2"]))
        require("G6 %s k" % lab, T.k == want["k"], "%s vs %s" % (T.k, want["k"]))
        require("G6 %s tag" % lab, jac_tag(T.k) == want["tag"], jac_tag(T.k))
        require("G6 %s M_i' integral (G7)" % lab,
                status != "NOT-INTEGRAL", status)
        require("G6 %s windows on descended" % lab, T.windows, str(T.windows))
        require("G6 %s gcd chain on descended" % lab, T.gcd_ok, str(T.gcd_ok))
        require("G6 %s M2'>m'" % lab, T.m2_gt_m, "%s > %s" % (T.M.get(2), T.m))


def gpt55_signatures():
    print("\n== GPT-5.5 Appendix-II signature cross-check ==")
    # (16,12,13; X), (21,14,16[18]; X), (15,10,11; X^2), (99,66) X^4
    got = []
    for (n, m, Ms, Vs, lab, _, _, _) in MS.MOH_TABLE:
        S = MS.Skel(n, m, Ms, Vs)
        us = u_s_of(S)
        if us == 1:
            T, status, _ = first_descent(S)
            got.append((T.n, T.m, T.M.get(2), T.k, jac_tag(T.k), lab))
        else:
            ML = minor_linear_branch(S)
            if ML is not None:
                got.append((ML.n, ML.m, ML.M.get(2), ML.k, jac_tag(ML.k), lab))
    print("   compiled signatures:")
    for g in got:
        print("      %s" % (g,))
    require("GPT-5.5 (16,12,13; X) present",
            any(g[:5] == (16, 12, 13, 1, "X") for g in got), str(got))
    require("GPT-5.5 (21,14,16; X) present",
            any(g[:5] == (21, 14, 16, 1, "X") for g in got), str(got))
    require("GPT-5.5 (21,14,18; X) present (bracket)",
            any(g[:5] == (21, 14, 18, 1, "X") for g in got), str(got))
    require("GPT-5.5 (15,10,11; X^2) present",
            any(g[:5] == (15, 10, 11, 2, "X^2") for g in got), str(got))
    require("GPT-5.5 (99,66) X^4 linear branch",
            any(g[:5] == (27, 18, 21, 4, "X^4") for g in got), str(got))
    ML = minor_linear_branch(MS.Skel(99, 66, [77, 97], {3: 8, 2: 8}))
    require("p.209 linear (27,18,21) V2 kept = 8",
            ML is not None and ML.V.get(2) == P209_9966_LINEAR["V2"],
            str(None if ML is None else ML.V))


def trio_descent():
    print("\n== D=105 trio through DESCENT ==")
    specs = [
        ("G1", 105, 70, [28, 103], {2: 1, 3: 5}),
        ("G2", 105, 70, [28, 103], {2: 1, 3: 6}),
        ("G3", 105, 70, [40, 103], {2: 1, 3: 4}),
    ]
    out = {}
    for lab, n, m, Ms, V in specs:
        S = MS.Skel(n, m, Ms, V)
        if not S.full_ok() or not S.windows_ok():
            require("%s is (1)-(13)" % lab, False)
            continue
        us = u_s_of(S)
        T, status, _ = first_descent(S)
        rec = dict(
            lab=lab, n=n, m=m, Ms=Ms, V=dict(sorted(V.items())),
            us=us, ds=S.d[S.s], Vs=S.V[S.s],
            status=status,
            n2=T.n if us == 1 else None,
            m2=T.m if us == 1 else None,
            M2=T.M.get(2) if us == 1 else None,
            k=T.k if us == 1 else None,
            tag=("γ^%d" % T.k) if (us == 1 and T.k is not None) else None,
            m2_gt_m=T.m2_gt_m if us == 1 else None,
            windows=T.windows if us == 1 else None,
        )
        out[lab] = rec
        print("   %s  M=%s V=%s  d_s=%s u_s=%s  -> %s"
              % (lab, Ms, rec["V"], rec["ds"], us,
                 ("%s n'=%s m'=%s M2'=%s k=%s %s status=%s"
                  % (rec["tag"], rec["n2"], rec["m2"], rec["M2"], rec["k"],
                     rec["tag"], status)) if us == 1 else ("US-GT-1 (no Prop 6.3)")))
    require("trio G2 -> (15,10; γ^4, M2'=4)",
            out["G2"]["n2"] == 15 and out["G2"]["m2"] == 10
            and out["G2"]["M2"] == 4 and out["G2"]["k"] == 4,
            str(out["G2"]))
    require("trio G3 -> (21,14; γ^2, M2'=8)",
            out["G3"]["n2"] == 21 and out["G3"]["m2"] == 14
            and out["G3"]["M2"] == 8 and out["G3"]["k"] == 2,
            str(out["G3"]))
    require("trio G1 has u_s=2 (needs p.209 dichotomy)",
            out["G1"]["us"] == 2, str(out["G1"]))
    return out


def campaign_table(dlo=48, dhi=200, Kmin=16, sink=None):
    """Terminal table for every (1)–(13) group with u_s=1 at dlo..dhi.

    Groups are (m, Ms, V_s). First descent uses only V_s, so it is group-level.
    Recursion past the first step needs V_{s-1} (per-row); we record the first
    step here and the fraction with u_s>1.
    """
    print("\n== DESCENT terminal table, %d <= D <= %d, groups with u_s=1 =="
          % (dlo, dhi))
    n_groups = n_us1 = n_usgt1 = 0
    by_status = {}
    moh_deg_alive = {64: 0, 75: 0, 84: 0, 99: 0}
    would_kill = {64: 0, 75: 0, 84: 0, 99: 0}
    lines = []
    t0 = time.time()
    for n in range(dlo, dhi + 1):
        G = {}
        for (m, Ms, V) in MS.census(n, Kmin=Kmin, full=True):
            S = MS.Skel(n, m, list(Ms), V)
            key = (m, tuple(Ms), S.V[S.s])
            G.setdefault(key, S)
        for key, S in G.items():
            n_groups += 1
            us = u_s_of(S)
            if us > 1:
                n_usgt1 += 1
                if n in moh_deg_alive:
                    moh_deg_alive[n] += 1  # still present; engine does not drop
                continue
            n_us1 += 1
            T, status, _ = first_descent(S)
            by_status[status] = by_status.get(status, 0) + 1
            kill_flag = status in ("WINDOW-FAIL", "GCD-FAIL", "NOT-INTEGRAL")
            if n in moh_deg_alive:
                moh_deg_alive[n] += 1
                if kill_flag:
                    would_kill[n] += 1
            rec = (n, S.m, list(key[1]), key[2], us, T.n, T.m, T.M.get(2),
                   T.k, jac_tag(T.k) if T.k is not None else None, status,
                   T.m2_gt_m, T.windows, T.gcd_ok)
            lines.append(rec)
    frac = F(n_usgt1, n_groups) if n_groups else F(0)
    print("   groups %d ; u_s=1 %d ; u_s>1 %d (fraction %s)  [%.1fs]"
          % (n_groups, n_us1, n_usgt1, frac, time.time() - t0))
    print("   first-descent status counts: %s" % sorted(by_status.items()))
    print("   G8 occupancy at Moh degrees (engine does not drop groups): %s"
          % moh_deg_alive)
    print("   of which first-descent hard-fail (not used as a kill): %s"
          % would_kill)
    for d in (64, 75, 84, 99):
        require("G8 D=%d not emptied by descent" % d,
                moh_deg_alive[d] > 0, str(moh_deg_alive[d]))
        require("G8 D=%d not emptied even if WINDOW/GCD/INTEGRAL were kills" % d,
                moh_deg_alive[d] - would_kill[d] > 0,
                "alive %s would_kill %s" % (moh_deg_alive[d], would_kill[d]))
    if sink is not None:
        with open(sink, "w") as f:
            f.write("# n m Ms Vs u_s n' m' M2' k tag status m2>m windows gcd\n")
            for rec in lines:
                f.write("%s\n" % (rec,))
        print("   wrote %d u_s=1 rows to %s" % (len(lines), sink))
    return dict(
        n_groups=n_groups, n_us1=n_us1, n_usgt1=n_usgt1, frac=frac,
        by_status=by_status, moh_deg_alive=moh_deg_alive, lines=lines,
    )


def g7_on_us1_moh():
    print("\n== G7: M_i' integral on every u_s=1 printed row ==")
    for (n, m, Ms, Vs, lab, _, _, _) in MS.MOH_TABLE:
        S = MS.Skel(n, m, Ms, Vs)
        if u_s_of(S) != 1:
            continue
        ds = S.d[S.s]
        ok = all(S.M[i] % ds == 0 for i in range(1, S.s))
        require("G7 %s M_i (i<s) divisible by d_s=%d" % (lab, ds), ok,
                str([S.M[i] for i in range(1, S.s)]))


def campaign_table_from_rows(rows, sink=None):
    """Same as campaign_table but consumes a precomputed Row list from mohsieve."""
    print("\n== DESCENT terminal table from cached (1)-(13) groups ==")
    Gfirst = {}
    for r in rows:
        key = (r.n, r.m, r.Ms, r.S.V[r.S.s])
        Gfirst.setdefault(key, r.S)
    n_groups = n_us1 = n_usgt1 = 0
    by_status = {}
    moh_deg_alive = {64: 0, 75: 0, 84: 0, 99: 0}
    would_kill = {64: 0, 75: 0, 84: 0, 99: 0}
    lines = []
    t0 = time.time()
    for key, S in Gfirst.items():
        n = key[0]
        n_groups += 1
        us = u_s_of(S)
        if us > 1:
            n_usgt1 += 1
            if n in moh_deg_alive:
                moh_deg_alive[n] += 1
            continue
        n_us1 += 1
        T, status, _ = first_descent(S)
        by_status[status] = by_status.get(status, 0) + 1
        kill_flag = status in ("WINDOW-FAIL", "GCD-FAIL", "NOT-INTEGRAL")
        if n in moh_deg_alive:
            moh_deg_alive[n] += 1
            if kill_flag:
                would_kill[n] += 1
        rec = (n, S.m, list(key[2]), key[3], us, T.n, T.m, T.M.get(2),
               T.k, jac_tag(T.k) if T.k is not None else None, status,
               T.m2_gt_m, T.windows, T.gcd_ok)
        lines.append(rec)
    frac = F(n_usgt1, n_groups) if n_groups else F(0)
    print("   groups %d ; u_s=1 %d ; u_s>1 %d (fraction %s)  [%.1fs]"
          % (n_groups, n_us1, n_usgt1, frac, time.time() - t0))
    print("   first-descent status counts: %s" % sorted(by_status.items()))
    print("   G8 occupancy at Moh degrees: %s" % moh_deg_alive)
    print("   of which first-descent hard-fail (not a kill): %s" % would_kill)
    for d in (64, 75, 84, 99):
        require("G8 D=%d not emptied by descent" % d,
                moh_deg_alive[d] > 0, str(moh_deg_alive[d]))
        require("G8 D=%d not emptied even if WINDOW/GCD/INTEGRAL were kills" % d,
                moh_deg_alive[d] - would_kill[d] > 0,
                "alive %s would_kill %s" % (moh_deg_alive[d], would_kill[d]))
    if sink is not None:
        with open(sink, "w") as f:
            f.write("# n m Ms Vs u_s n' m' M2' k tag status m2>m windows gcd\n")
            for rec in lines:
                f.write("%s\n" % (rec,))
        print("   wrote %d u_s=1 rows to %s" % (len(lines), sink))
    return dict(
        n_groups=n_groups, n_us1=n_us1, n_usgt1=n_usgt1, frac=frac,
        by_status=by_status, moh_deg_alive=moh_deg_alive, lines=lines,
    )


def main(dlo=48, dhi=200, sink="box/mohsieve/descent_terminal.txt", rows=None):
    t0 = time.time()
    print("box/mohsieve/descent.py — Prop 6.3/6.4 descent machine")
    reset()
    p207_check()
    gpt55_signatures()
    g7_on_us1_moh()
    trio = trio_descent()
    if rows is not None:
        table = campaign_table_from_rows(rows, sink=sink)
    else:
        table = campaign_table(dlo, dhi, sink=sink)
    print("\nwall descent %.1fs" % (time.time() - t0))
    fail_closed()
    print("ALL descent GATES GREEN.")
    return dict(trio=trio, table=table)


if __name__ == "__main__":
    main()
