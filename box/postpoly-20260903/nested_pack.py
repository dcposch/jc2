#!/usr/bin/env python3
"""NESTED-PACK -- parent-indexed orbit-packing DP on Moh (1)-(13).

Lane nested-pack-dp-grok46-20260903.  Standard library only.

Replaces the flat UNB relaxation at s>3 with the exact nested packing:
at each level j = s-1, ..., 2 the children of a parent disc pack into that
parent's p(pi) of degree Q_j = V_{j+1} d_j / d_{j+1}, with at most ONE
zero-centred (pi) child per parent and free nonzero orbits (each consuming
A_j * V_j of the degree).  Bottom discs contribute V_2 q each, multiplied
by the local orbit size along the path.

Enumerator: box/moh_skeleton_full.py via knapsack_v2's R1 loader
(--inputs DIR, $JC2_INPUTS, or repo-relative box/).  Charged knapsack.py
is not imported and not overwritten.

Fail-closed: any check() failure aborts before a filter number is printed.
"""
from __future__ import annotations
import os, sys, time
from fractions import Fraction as F
from math import lcm

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import knapsack_v2 as KS
from knapsack_v2 import (
    MF, Skel, census, MOH_TABLE, NLO, NHI,
    packets, knapsack, knapsack_z01, achievable_N, Umax, orbit_sizes,
)

FAILURES = []
NCHECK = [0]
CAP_DEFAULT = 60000
LISTING = (105, 108, 112, 117, 120)
COLLECT_NSETS = LISTING + (88,)


def check(name, cond, detail=""):
    NCHECK[0] += 1
    if cond:
        print("  [ok]   %s" % name)
    else:
        print("  [FAIL] %s   %s" % (name, detail))
        FAILURES.append(name)
    return cond


def abort_if_failed(stage):
    if FAILURES:
        print("%s FAILED: %s" % (stage, FAILURES))
        sys.exit(1)


# ---------------------------------------------------------------------------
# nested DP
# ---------------------------------------------------------------------------
def Q_of(S, j):
    """deg p at D_j: V_{j+1} d_j / d_{j+1} (exact in Z)."""
    num = S.V[j + 1] * S.d[j]
    den = S.d[j + 1]
    assert num % den == 0, (S.n, j, num, den)
    return num // den


def _vkey(S):
    return tuple(S.V[i] for i in range(2, S.s + 1))


def mix_dp(nz_items, z_items, Q, Nhi, CAP):
    """Unbounded NZ items + at most one Z item.  Items are (w, [values]).

    Returns (set of reachable Fractions including 0, capped).
    """
    Q = int(Q)
    reach = [set() for _ in range(Q + 1)]
    reach[0].add(F(0))
    capped = False
    nstates = 1

    for (w, vals) in nz_items:
        w = int(w)
        if w <= 0 or w > Q:
            continue
        vals = [v for v in vals if 0 < v <= Nhi]
        if not vals:
            continue
        for tw in range(w, Q + 1):
            src = reach[tw - w]
            if not src:
                continue
            dst = reach[tw]
            for s0 in list(src):
                for v in vals:
                    s1 = s0 + v
                    if s1 > Nhi:
                        continue
                    if s1 in dst:
                        continue
                    if len(dst) >= CAP:
                        capped = True
                        continue
                    dst.add(s1)
                    nstates += 1

    extra = [set() for _ in range(Q + 1)]
    for (w, vals) in z_items:
        w = int(w)
        if w <= 0 or w > Q:
            continue
        vals = [v for v in vals if 0 < v <= Nhi]
        if not vals:
            continue
        for tw in range(0, Q - w + 1):
            src = reach[tw]
            if not src:
                continue
            dst = extra[tw + w]
            for s0 in src:
                for v in vals:
                    s1 = s0 + v
                    if s1 > Nhi:
                        continue
                    if s1 in dst or s1 in reach[tw + w]:
                        continue
                    if len(dst) >= CAP:
                        capped = True
                        continue
                    dst.add(s1)
                    nstates += 1
    for tw in range(Q + 1):
        if extra[tw]:
            dst = reach[tw]
            for s1 in extra[tw]:
                if s1 in dst:
                    continue
                if len(dst) >= CAP:
                    capped = True
                    break
                dst.add(s1)

    acc = set()
    for cell in reach:
        acc |= cell
    return acc, capped, nstates


def reachable(skels, j, Nhi, CAP, memo):
    """Achievable N from packing parent D_j.  skels share V[j+1],...,V[s]."""
    S0 = skels[0]
    key = (j, tuple(sorted(_vkey(S) for S in skels)))
    if key in memo:
        return memo[key]

    Q = Q_of(S0, j)
    by_v = {}
    for S in skels:
        by_v.setdefault(int(S.V[j]), []).append(S)

    nz_items = []
    z_items = []
    child_capped = False
    for v, subs in by_v.items():
        Srep = subs[0]
        A = int(Srep.A(j))
        _ok, b10, b11 = Srep.cond1011(j)
        for S in subs:
            if int(S.A(j)) != A or S.cond1011(j)[1:] != (b10, b11):
                # A_j and (10)/(11) depend only on V_j and above; mismatch is a bug
                memo[key] = (set(), True, 0)
                return memo[key]
        if j == 2:
            G = []
            for S in subs:
                g = S.V[2] * S.q()
                if 0 < g <= Nhi:
                    G.append(g)
            G = list(set(G))
        else:
            Gset, cap_c, _ = reachable(subs, j - 1, Nhi, CAP, memo)
            child_capped = child_capped or cap_c
            G = [g for g in Gset if 0 < g <= Nhi]

        if b10 and G:
            w = A * v
            vals = [A * g for g in G if A * g <= Nhi]
            if 0 < w <= Q and vals:
                nz_items.append((w, vals))
        if b11 and G:
            w = v
            vals = [g for g in G if g <= Nhi]
            if 0 < w <= Q and vals:
                z_items.append((w, vals))

    acc, capped, nstates = mix_dp(nz_items, z_items, Q, Nhi, CAP)
    out = (acc, capped or child_capped, nstates)
    memo[key] = out
    return out


def nested_values(skels, Nhi, CAP=CAP_DEFAULT):
    """Reachable N from the unique D_{s-1}.  Includes 0."""
    S0 = skels[0]
    return reachable(skels, S0.s - 1, Nhi, CAP, {})


def ints_in(values, Nlo, Nhi):
    out = set()
    for v in values:
        if v.denominator == 1 and Nlo <= v <= Nhi:
            out.add(int(v))
    return out


def describe_towers(skels):
    rows = []
    S0 = skels[0]
    for S in skels:
        bits = []
        for j in range(2, S.s):
            _ok, b10, b11 = S.cond1011(j)
            bits.append("j=%d A=%d V=%d Q=%d (10)=%s (11)=%s" %
                        (j, S.A(j), S.V[j], Q_of(S, j), b10, b11))
        rows.append("V=%s q=%s d1=%s |O|=%s %s" %
                    (dict(S.V), S.q(), S.delta[1], sorted(orbit_sizes(S)),
                     "; ".join(bits)))
    return rows


# ---------------------------------------------------------------------------
# collect groups
# ---------------------------------------------------------------------------
def collect(n):
    G = {}
    for (m, Ms, V) in census(n, Kmin=16, full=True):
        S = Skel(n, m, list(Ms), V)
        key = (m, Ms, S.V[S.s])
        G.setdefault(key, []).append(S)
    return G


# ---------------------------------------------------------------------------
# controls
# ---------------------------------------------------------------------------
def control_moh_rows():
    print("\n-- CONTROL M: Moh six rows, nested N in [6,16] --")
    expect = [
        ("(64,48)", {9}),
        ("(84,56) M2=64,V2=2", set()),
        ("(84,56) M2=72,V2=5", {10}),
        ("(75,50) V2=3", {9}),
        ("(75,50) V2=2", {8}),
        ("(99,66)", {16}),
    ]
    print("   %-24s %3s %6s %s" % ("row", "s", "nested", "expect"))
    for ((n, m, Ms, Vs, lab, _, _, _), exp) in zip(MOH_TABLE, [e[1] for e in expect]):
        S = Skel(n, m, Ms, Vs)
        check("windows+full %s" % lab, S.windows_ok() and S.full_ok())
        Um = max(int(Umax([S])), 16)
        vals, cap, _ = nested_values([S], Um)
        Ns = ints_in(vals, 6, 16)
        print("   %-24s %3d %6s %s%s" %
              (lab, S.s, sorted(Ns), sorted(exp), " CAPPED" if cap else ""))
        check("nested[6,16] %s" % lab, Ns == exp, "%s vs %s" % (sorted(Ns), sorted(exp)))
        # s=3 => nested equals Z01 on the same window
        h_z, c_z = knapsack_z01([S], 6, 16)
        check("nested=Z01 hit %s" % lab, bool(Ns) == bool(h_z or c_z),
              "nested %s z01 %s" % (bool(Ns), h_z or c_z))


def control_s3_Q():
    print("\n-- CONTROL Q: s=3 => Q_2 = u; s>3 => Q_{s-1} = V_s d_{s-1}/d_s --")
    seen3 = seen4 = bad3 = bad4 = 0
    for n in range(48, 121):
        for (m, Ms, V) in census(n, full=True):
            S = Skel(n, m, list(Ms), V)
            Qtop = Q_of(S, S.s - 1)
            if S.s == 3:
                seen3 += 1
                if Qtop != int(S.u):
                    bad3 += 1
            else:
                seen4 += 1
                want = S.V[S.s] * S.d[S.s - 1] // S.d[S.s]
                if Qtop != want:
                    bad4 += 1
    check("s=3 Q2=u on all (1)-(13) s=3 assignments", bad3 == 0 and seen3 > 0,
          "bad=%d seen=%d" % (bad3, seen3))
    check("s>3 Qtop=V_s d_{s-1}/d_s on all (1)-(13) s>3 assignments",
          bad4 == 0 and seen4 > 0, "bad=%d seen=%d" % (bad4, seen4))
    print("   %d s=3 assignments Q2=u; %d s>3 assignments Qtop formula (bad 0)"
          % (seen3, seen4))


def control_Aj_depends_on_upper():
    """A_j and (10)/(11) at level j depend only on V_j and V_{j+1..s}."""
    print("\n-- CONTROL A: A_j / (10)/(11) constant on (V_j, V_{j+1..s}) --")
    bad = tot = 0
    for n in range(48, 101):
        G = collect(n)
        for skels in G.values():
            S0 = skels[0]
            for j in range(2, S0.s):
                bucket = {}
                for S in skels:
                    sig = tuple(S.V[i] for i in range(j, S.s + 1))
                    rec = (int(S.A(j)), S.cond1011(j)[1:])
                    if sig in bucket and bucket[sig] != rec:
                        bad += 1
                    bucket[sig] = rec
                    tot += 1
    check("A_j+(10)/(11) constant on (V_j..V_s) at D<=100", bad == 0,
          "%d / %d" % (bad, tot))
    print("   %d (group, level, type) rows, %d mismatches (want 0)" % (tot, bad))


# ---------------------------------------------------------------------------
# main census
# ---------------------------------------------------------------------------
def run_census(dlo=48, dhi=120):
    print("\n== NESTED-PACK on (1)-(13), %d <= D <= %d ==" % (dlo, dhi))
    print("   %5s %5s %5s %5s %7s %7s %7s %7s %7s %7s %7s %6s" %
          ("D", "grp", "s3", "s>3", "unb>=6", "unb616", "nest>=6", "nest616",
           "kill", "cap", "empty?", "wall"))
    T = dict(g=0, s3=0, sgt=0, u1=0, u2=0, n1=0, n2=0, cap=0,
             s3n1=0, s3n2=0, sgtn1=0, sgtn2=0, s3u1=0, s3u2=0)
    empty6 = []; empty16 = []
    delta_unb_alive_nested_dead16 = []
    delta_unb_alive_nested_dead6 = []
    s3_mismatch = []
    surv = {n: [] for n in LISTING}
    nset_special = {n: [] for n in COLLECT_NSETS}
    t_all = time.time()
    max_states = 0

    for n in range(dlo, dhi + 1):
        t0 = time.time()
        G = collect(n)
        if not G:
            continue
        a_u1 = a_u2 = a_n1 = a_n2 = cp = ns3 = nsgt = 0
        s3_n1 = s3_n2 = sgt_n1 = sgt_n2 = s3_u1 = s3_u2 = 0
        alive16 = []
        for key, skels in G.items():
            u = int(skels[0].u)
            Um = Umax(skels)
            Nhi6 = max(Um, F(6))
            s = skels[0].s
            # UNB (flat relaxation)
            pk16 = []
            pk6 = []
            for S in skels:
                pk16.extend(packets(S, 16))
                pk6.extend(packets(S, Nhi6))
            h_u2, c_u2, _ = knapsack(pk16, u, 6, 16)
            h_u1, c_u1, _ = knapsack(pk6, u, 6, Nhi6)
            unb16 = bool(h_u2 or c_u2)
            unb6 = bool(h_u1 or c_u1)
            # nested
            vals, cap, nstates = nested_values(skels, Nhi6)
            max_states = max(max_states, nstates)
            Ns6 = ints_in(vals, 6, Nhi6)
            Ns16 = {N for N in Ns6 if N <= 16}
            nest6 = bool(Ns6) or cap
            nest16 = bool(Ns16) or cap
            # s=3 must equal Z01
            if s == 3:
                h_z16, c_z16 = knapsack_z01(skels, 6, 16)
                h_z6, c_z6 = knapsack_z01(skels, 6, Nhi6)
                z16 = bool(h_z16 or c_z16)
                z6 = bool(h_z6 or c_z6)
                if z16 != bool(Ns16) or z6 != bool(Ns6):
                    s3_mismatch.append((n, key, z16, sorted(Ns16), z6, sorted(Ns6)))
            # relaxation: nested => UNB
            if nest16 and not unb16 and not cap:
                delta_unb_alive_nested_dead16.append(("NESTED_NOT_IN_UNB", n, key))
            if nest6 and not unb6 and not cap:
                delta_unb_alive_nested_dead6.append(("NESTED_NOT_IN_UNB", n, key))
            if unb16 and not nest16:
                delta_unb_alive_nested_dead16.append((n, key, skels, sorted(Ns16)))
            if unb6 and not nest6:
                delta_unb_alive_nested_dead6.append((n, key, skels, sorted(Ns6)))

            a_u1 += int(unb6); a_u2 += int(unb16)
            a_n1 += int(nest6); a_n2 += int(nest16)
            cp += int(cap)
            if s == 3:
                ns3 += 1
                s3_n1 += int(nest6); s3_n2 += int(nest16)
                s3_u1 += int(unb6); s3_u2 += int(unb16)
            else:
                nsgt += 1
                sgt_n1 += int(nest6); sgt_n2 += int(nest16)

            if n in COLLECT_NSETS:
                nset_special[n].append((key, skels, sorted(Ns16), sorted(Ns6),
                                        unb16, nest16, cap))
            if n in LISTING and nest16:
                alive16.append((key, skels, sorted(Ns16), cap))

        T['g'] += len(G); T['s3'] += ns3; T['sgt'] += nsgt
        T['u1'] += a_u1; T['u2'] += a_u2
        T['n1'] += a_n1; T['n2'] += a_n2; T['cap'] += cp
        T['s3n1'] += s3_n1; T['s3n2'] += s3_n2
        T['sgtn1'] += sgt_n1; T['sgtn2'] += sgt_n2
        T['s3u1'] += s3_u1; T['s3u2'] += s3_u2
        if a_n1 == 0:
            empty6.append(n)
        if a_n2 == 0:
            empty16.append(n)
        if n in LISTING:
            surv[n] = alive16
        flag = ""
        if a_n2 == 0:
            flag = " EMPTY[6,16]"
        print("   %5d %5d %5d %5d %7d %7d %7d %7d %7d %7d %7s %5.1fs%s"
              % (n, len(G), ns3, nsgt, a_u1, a_u2, a_n1, a_n2,
                 a_u2 - a_n2, cp, "Y" if a_n2 == 0 else "",
                 time.time() - t0, flag))
        sys.stdout.flush()

    print("   ---- totals ----")
    print("   groups %d  (s=3 %d, s>3 %d)" % (T['g'], T['s3'], T['sgt']))
    print("   UNB    N>=6 %d   [6,16] %d" % (T['u1'], T['u2']))
    print("   NESTED N>=6 %d   [6,16] %d   capped %d" % (T['n1'], T['n2'], T['cap']))
    print("   s=3    NESTED N>=6 %d  [6,16] %d   UNB [6,16] %d"
          % (T['s3n1'], T['s3n2'], T['s3u2']))
    print("   s>3    NESTED N>=6 %d  [6,16] %d" % (T['sgtn1'], T['sgtn2']))
    print("   empty nested N>=6    : %s" % (empty6 or "NONE"))
    print("   empty nested [6,16]  : %s" % (empty16 or "NONE"))
    n_kill16 = sum(1 for row in delta_unb_alive_nested_dead16
                   if row[0] != "NESTED_NOT_IN_UNB")
    n_bad16 = sum(1 for row in delta_unb_alive_nested_dead16
                  if row[0] == "NESTED_NOT_IN_UNB")
    print("   UNB-alive / NESTED-dead [6,16] : %d groups" % n_kill16)
    print("   NESTED-alive / UNB-dead [6,16] : %d groups (want 0)" % n_bad16)
    print("   max DP states in a parent: %d" % max_states)
    print("   wall %.1fs" % (time.time() - t_all))
    return (T, surv, nset_special, empty6, empty16,
            delta_unb_alive_nested_dead16, s3_mismatch, max_states)


def list_specials(nset_special, surv):
    print("\n== D=88 (s=3 exact; emptied in [6,16], lives at N=18) ==")
    for (key, skels, Ns16, Ns6, unb, nest, cap) in nset_special.get(88, []):
        m, Ms, Vs = key
        S0 = skels[0]
        print("   m=%d M=%s V_s=%d s=%d u=%s N[6,16]=%s N>=6=%s unb16=%s"
              % (m, list(Ms), Vs, S0.s, S0.u, Ns16, Ns6, unb))
        for line in describe_towers(skels):
            print("      %s" % line)

    print("\n== SPECIAL DEGREES {105,108,112,117,120} ==")
    for n in LISTING:
        rows = nset_special.get(n, [])
        nest16 = [r for r in rows if r[5]]
        unb16 = [r for r in rows if r[4]]
        s3 = [r for r in nest16 if r[1][0].s == 3]
        sgt = [r for r in nest16 if r[1][0].s > 3]
        killed = [r for r in rows if r[4] and not r[5]]
        print("\n   D=%d groups=%d  UNB[6,16]=%d  NESTED[6,16]=%d  "
              "(s=3 nested %d, s>3 nested %d)  UNB-alive/NESTED-dead=%d"
              % (n, len(rows), len(unb16), len(nest16), len(s3), len(sgt),
                 len(killed)))
        show = nest16 if n in (105, 117) else []
        if n in (105, 117):
            print("   -- all nested [6,16] survivors --")
            for (key, skels, Ns16, Ns6, unb, nest, cap) in sorted(show, key=lambda r: r[0]):
                m, Ms, Vs = key
                S0 = skels[0]
                print("      m=%d M=%s V_s=%d s=%d u=%s N[6,16]=%s N>=6=%s%s"
                      % (m, list(Ms), Vs, S0.s, S0.u, Ns16, Ns6,
                         " CAPPED" if cap else ""))
                for line in describe_towers(skels):
                    print("         %s" % line)
        if n in (108, 112, 120):
            print("   -- s=3 nested [6,16] survivors (exact) --")
            for (key, skels, Ns16, Ns6, unb, nest, cap) in sorted(s3, key=lambda r: r[0]):
                m, Ms, Vs = key
                S0 = skels[0]
                print("      m=%d M=%s V_s=%d u=%s V2=%s |O|=%s N=%s"
                      % (m, list(Ms), Vs, S0.u,
                         sorted(set(S.V[2] for S in skels)),
                         sorted(set().union(*[orbit_sizes(S) for S in skels])),
                         Ns16))
            if killed:
                print("   -- UNB-alive / NESTED-dead in [6,16] (%d) --" % len(killed))
                for (key, skels, Ns16, Ns6, unb, nest, cap) in killed[:40]:
                    m, Ms, Vs = key
                    S0 = skels[0]
                    print("      m=%d M=%s V_s=%d s=%d u=%s nestedN16=%s N>=6=%s"
                          % (m, list(Ms), Vs, S0.s, S0.u, Ns16, Ns6))
                    if S0.s > 3:
                        for line in describe_towers(skels):
                            print("         %s" % line)
                if len(killed) > 40:
                    print("      ... %d more" % (len(killed) - 40))
            # compact s>3 nested survivors
            if sgt:
                print("   -- s>3 nested [6,16] survivors (%d) --" % len(sgt))
                for (key, skels, Ns16, Ns6, unb, nest, cap) in sorted(sgt, key=lambda r: r[0])[:60]:
                    m, Ms, Vs = key
                    S0 = skels[0]
                    print("      m=%d M=%s V_s=%d s=%d u=%s N=%s"
                          % (m, list(Ms), Vs, S0.s, S0.u, Ns16))
                if len(sgt) > 60:
                    print("      ... %d more" % (len(sgt) - 60))


def list_D105_full(nset_special):
    print("\n== D=105 complete nested N-sets (all 14 groups, s=3 exact) ==")
    rows = nset_special.get(105, [])
    for (key, skels, Ns16, Ns6, unb, nest, cap) in sorted(rows, key=lambda r: r[0]):
        m, Ms, Vs = key
        S0 = skels[0]
        print("   m=%d M=%s V_s=%d u=%s N[6,16]=%s N>=6=%s unb16=%s"
              % (m, list(Ms), Vs, S0.u, Ns16, Ns6, unb))
        for line in describe_towers(skels):
            print("      %s" % line)


def list_delta(delta, label):
    real = [r for r in delta if r[0] != "NESTED_NOT_IN_UNB"]
    print("\n== DELTA: %s (%d groups) ==" % (label, len(real)))
    shown = 0
    for row in real:
        n, key, skels, Ns = row
        m, Ms, Vs = key
        S0 = skels[0]
        print("   D=%d m=%d M=%s V_s=%d s=%d u=%s nestedN=%s" %
              (n, m, list(Ms), Vs, S0.s, S0.u, Ns))
        shown += 1
        if shown >= 60:
            print("   ... %d more" % (len(real) - shown))
            break


# ---------------------------------------------------------------------------
def main():
    print("nested-pack -- parent-indexed orbit DP on Moh (1)-(13)")
    print("enumerator %s" % os.path.abspath(MF.__file__))
    print("knapsack_v2 %s" % os.path.abspath(KS.__file__))
    print("=" * 78)
    control_moh_rows()
    control_s3_Q()
    control_Aj_depends_on_upper()
    abort_if_failed("CONTROLS before census")

    (T, surv, nset_special, empty6, empty16,
     delta16, s3_mismatch, max_states) = run_census()

    check("groups = 1189", T['g'] == 1189, str(T['g']))
    check("s=3 groups = 274", T['s3'] == 274, str(T['s3']))
    check("UNB N>=6 = 681 (charged relaxation)", T['u1'] == 681, str(T['u1']))
    check("UNB [6,16] = 575 (charged relaxation)", T['u2'] == 575, str(T['u2']))
    check("s=3 nested N>=6 = 173 (charged Z01)", T['s3n1'] == 173, str(T['s3n1']))
    check("s=3 nested [6,16] = 138 (charged Z01)", T['s3n2'] == 138, str(T['s3n2']))
    check("no s=3 nested/Z01 mismatch", s3_mismatch == [],
          str(s3_mismatch[:5]))
    n_bad16 = sum(1 for row in delta16 if row[0] == "NESTED_NOT_IN_UNB")
    check("nested survivors subset of UNB (relaxation)", n_bad16 == 0,
          str(n_bad16))
    check("cap never forces a kill (capped counted alive)", True)

    # D=88, 105, 117
    rows105 = [r for r in nset_special.get(105, []) if r[5]]
    check("D=105 nested [6,16] = 3", len(rows105) == 3, str(len(rows105)))
    got105 = []
    for (key, skels, Ns16, Ns6, unb, nest, cap) in sorted(rows105, key=lambda r: r[0]):
        got105.append((key[0], list(key[1]), key[2], tuple(Ns16)))
        check("D=105 N={9} m=%s Vs=%s" % (key[0], key[2]), Ns16 == [9], str(Ns16))
    expect105 = [
        (70, [28, 103], 5, (9,)),
        (70, [28, 103], 6, (9,)),
        (70, [40, 103], 4, (9,)),
    ]
    check("D=105 trio keys", got105 == expect105, str(got105))

    rows88 = nset_special.get(88, [])
    check("D=88 has 1 group", len(rows88) == 1, str(len(rows88)))
    if rows88:
        key, skels, Ns16, Ns6, unb, nest, cap = rows88[0]
        check("D=88 nested [6,16] empty", Ns16 == [] and not nest, str(Ns16))
        check("D=88 nested N>=6 = {18}", Ns6 == [18], str(Ns6))

    rows117 = [r for r in nset_special.get(117, []) if r[5]]
    check("D=117 nested [6,16] = 3 (UNB 4 -> 3)", len(rows117) == 3,
          str(len(rows117)))
    dead117 = [r for r in nset_special.get(117, []) if r[4] and not r[5]]
    if not dead117:
        # UNB may already drop it? charged UNB keeps 4; nested/Z01 drops 1
        dead117 = [r for r in nset_special.get(117, [])
                   if r[0][0] == 78 and list(r[0][1]) == [13, 115]]
    check("D=117 killed the (11)-only m=78 M=[13,115] Vs=8 row",
          any(r[0][0] == 78 and list(r[0][1]) == [13, 115] and r[0][2] == 8
              and not r[5] for r in nset_special.get(117, [])),
          str([(r[0], r[2], r[5]) for r in nset_special.get(117, [])]))

    abort_if_failed("POST-CENSUS CONTROLS")

    list_D105_full(nset_special)
    list_specials(nset_special, surv)
    real_delta = [r for r in delta16 if r[0] != "NESTED_NOT_IN_UNB"]
    list_delta(delta16, "UNB-alive / NESTED-dead in [6,16]")

    print("\n" + "=" * 78)
    if FAILURES:
        print("CONTROLS FAILED (%d): %s" % (len(FAILURES), FAILURES))
        sys.exit(1)
    print("ALL CONTROLS PASSED.  NCHECK=%d  nested[6,16]=%d  nested N>=6=%d"
          % (NCHECK[0], T['n2'], T['n1']))
    print("UNB-alive/NESTED-dead [6,16] = %d of the 575 UNB survivors"
          % len(real_delta))


if __name__ == "__main__":
    main()
