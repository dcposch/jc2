#!/usr/bin/env python3
"""Controls for second_gen.py.

(a) PARENT REPLAY (l = 0): the level-local engine of second_gen (window + Galois/ODE pattern
    at every level + bottom (12)/(13)) applied to the PARENT towers.  Must accept all 66
    roster parents and all operative rows; its rejections on the (1)-(13) census must be a
    subset of the operative Tree's rejections (implementation control: my conditions are a
    sub-conjunction of the operative screen).
(b) BOTTOM IDENTITY: on the roster, compare the child's (A'_1, N', M') with the parent's
    (A_1, N, M).  Prediction from the metric radii delta'_i = v - u/delta_i (i >= j),
    delta'_i = v-u-(u/e)(1-delta_i) (i < j): A'_1 = den(den(delta_2) delta_1) = A_1 at s=3,u=1.
(c) OUTER-SET PROBE: run descend_own on every operative row; on rows whose outer first-support
    set is nonempty but whose full set is empty, run the child tests on the outer vectors.
    Measures the independent killing power of the child tests on near-miss data.
(d) SD REACH on the (1)-(13) census and the operative set (u_s = 1, complete chain):
    delta'_{s'} = -1  <=>  M_{s-1} = n - d_s(d_s-1);  ell'' at a simple minor point
    = d_{s-1}/d_s - d_s.  Count rows in the SD kill window.
"""
from __future__ import annotations
import os, sys, json, time
from fractions import Fraction as F
from math import gcd, lcm
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = "/home/ubuntu/jc2"
sys.path.insert(0, os.path.join(ROOT, "box", "centre-gate-20260903"))
sys.path.insert(0, ROOT)
import moh_skeleton_full_frozen as B
from opus5_probe import Tree
from box.lib.descend_own import descend_own
sys.path.insert(0, HERE)
import second_gen as SG

ROSTER = SG.ROSTER


def operative(n, m, Ms, V):
    T = Tree(n, m, Ms, gate=False, ode=True, capacity=False, passport=False)
    T.recenter = True; T._memo = {}; T.why = []
    if not (T.d[T.s] > V[T.s] > F(T.d[T.s], 2)):
        return False
    return T.ok(T.s - 1, (V[T.s],), True, tuple(V[i] for i in range(T.s - 1, 1, -1))) is not None


def parent_engine(n, m, Ms, V):
    """Level-local engine on the parent (l = 0).  Returns (alive, detail)."""
    sk = B.Skel(n, m, list(Ms), V)
    s = sk.s
    M = sk.M; d = sk.d
    Vd = {i: sk.V[i] for i in range(2, s + 2)}
    delta = SG.def51_radii(n, M, d, Vd, s, 1)
    assert delta == sk.delta
    Vlev = {i: Vd[i] for i in range(2, s + 1)}
    for j in range(s, 1, -1):
        lt = SG.level_test(n, m, M, d, Vlev, delta, s, j, Vd[j + 1], want_all=False)
        if not lt["alive"]:
            return False, ("level", j, lt["P"], lt["Q"], lt["A"], lt["V"])
    bt = SG.bottom_test(n, m, M, d, Vlev, delta, s)
    if not bt["alive"]:
        return False, ("bottom", bt["A1"], bt["N"], bt["M"])
    return True, None


def main():
    t0 = time.time()
    rows = [json.loads(l) for l in open(ROSTER)]
    out = {}
    # ---------- (a) parent replay on the roster ----------
    W = sys.stdout.write
    W("(a) PARENT REPLAY on the 66 roster parents (l=0)\n")
    bad = []
    for r in rows:
        s = r["source"]
        Ms = s["M"][1:]
        V = {i + 2: s["V"][i] for i in range(len(s["V"]))}
        alive, det = parent_engine(s["n"], s["m"], Ms, V)
        if not alive:
            bad.append((r["row_id"], det))
    W("   rejected roster parents: %d %s\n" % (len(bad), bad))
    out["parent_replay_roster_rejected"] = bad

    # ---------- (a') census-wide ----------
    W("(a') CENSUS (1)-(13), Kmin=2, 16<=n<=200: my engine vs operative Tree\n")
    cnt = Counter(); mine_not_tree = []; sd_window = Counter(); sd_rows = []
    op_rows = []
    for n in range(16, 201):
        for (m, Ms, V) in B.census(n, Kmin=2, full=True):
            op = operative(n, m, Ms, V)
            mine, det = parent_engine(n, m, Ms, V)
            cnt[("op" if op else "nonop", "mine_ok" if mine else "mine_rej")] += 1
            if op and not mine:
                mine_not_tree.append((n, m, Ms, dict(V), det))
            if op:
                op_rows.append((n, m, tuple(Ms), dict(V)))
            # (d) SD reach: u_s = 1 complete chain
            sk = B.Skel(n, m, list(Ms), V); s = sk.s
            ds = sk.d[s]; vs = V[s]; us = ds - vs; ell = vs - us - 1
            if us == 1 and s >= 3:
                dprev = sk.d[s - 1]
                top_minus1 = (sk.M[s - 1] == n - ds * (ds - 1))       # delta'_{s'} = -1
                ell2 = dprev // ds - ds                                # l'' at a simple minor point
                lo_prev = F(dprev, n - sk.M[s - 1])
                simple_minor = (lo_prev >= 1)
                key = ("op" if op else "nonop", "top-1" if top_minus1 else "top!=-1",
                       "ell2<0" if ell2 < 0 else ("ell2=0" if ell2 == 0 else "ell2>0"),
                       "simple-minor" if simple_minor else "simple-major")
                sd_window[key] += 1
                if top_minus1 and ell2 < 0 and simple_minor:
                    sd_rows.append((n, m, Ms, dict(V), op, str(lo_prev)))
    W("   %s\n" % dict(cnt))
    W("   operative rows rejected by my engine (must be 0): %d\n" % len(mine_not_tree))
    for x in mine_not_tree[:10]:
        W("      %s\n" % (x,))
    out["census_counts"] = {"|".join(k): v for k, v in cnt.items()}
    out["operative_rejected_by_mine"] = mine_not_tree[:50]
    W("(d) SD REACH (u_s=1, s>=3) by (operative, delta'_top=-1?, sign(l'' at simple point), simple point minor?):\n")
    for k, v in sorted(sd_window.items()):
        W("   %-45s %d\n" % ("|".join(k), v))
    W("   rows in the SD kill window (top=-1, l''<0, simple point minor): %d\n" % len(sd_rows))
    for x in sd_rows[:15]:
        W("      %s\n" % (x,))
    out["sd_window"] = {"|".join(k): v for k, v in sd_window.items()}
    out["sd_kill_window_rows"] = sd_rows
    W("   [%.0fs]\n" % (time.time() - t0))

    # ---------- (b) bottom identity on the roster ----------
    W("(b) BOTTOM IDENTITY child (A'_1,N',M') vs parent (A_1,N,M) on the roster\n")
    ident = Counter(); nonident = []
    for r in rows:
        s = r["source"]; c = r["own_child"]
        n, m = s["n"], s["m"]; sk = B.Skel(n, m, s["M"][1:], {i + 2: s["V"][i] for i in range(len(s["V"]))})
        A1 = sk.A(1); N = n * s["V"][0] // sk.d[2]; Mm = m * s["V"][0] // sk.d[2]
        sp = c["s_prime"]
        dl = {i + 1: F(c["delta_prime"][i]) for i in range(sp)}
        L = 1
        for i in range(2, sp + 1):
            L = lcm(L, dl[i].denominator)
        A1c = (L * dl[1]).denominator
        Nc = c["n_prime"] * c["V_prime"][0] // c["d_prime"][1]; Mc = c["m_prime"] * c["V_prime"][0] // c["d_prime"][1]
        same = (A1c == A1 and Nc == N and Mc == Mm)
        divides = (A1 % A1c == 0 and Nc == N and Mc == Mm)
        ident[("equal" if same else ("A'|A" if divides else "DIFFERENT"), "u=1" if s["u_s"] == 1 else "u>1")] += 1
        if not same:
            nonident.append((r["row_id"], s["u_s"], A1, A1c, N, Nc, Mm, Mc))
    W("   %s\n" % dict(ident))
    for x in nonident:
        W("      %s\n" % (x,))
    out["bottom_identity"] = {"|".join(k): v for k, v in ident.items()}
    out["bottom_nonidentical"] = nonident

    # ---------- (c) outer-set probe with descend_own ----------
    W("(c) OUTER-SET PROBE: descend_own on all operative rows; child tests on outer vectors of full-empty rows\n")
    t1 = time.time()
    states = Counter(); probe = Counter(); probe_rows = []
    nonempty_keys = set()
    for (n, m, Ms, V) in op_rows:
        sk = B.Skel(n, m, list(Ms), V)
        try:
            D = descend_own(sk)
        except Exception as e:
            states["EXC:" + str(e)[:40]] += 1
            continue
        states[D["route_state"]] += 1
        if D["route_state"] == "NONEMPTY":
            nonempty_keys.add((n, m, tuple(Ms), tuple(V[i] for i in range(2, sk.s + 1))))
            continue
        if D["dropped"] or not D["outer_V_vectors"]:
            continue
        # full set empty, outer nonempty: probe the child tests on each outer vector
        np_, mp, sp, ell, us = D["n"], D["m"], D["s"], D["ell"], D["us"]
        Mp = dict(D["M"]); dp = dict(D["d"])
        for vec in D["outer_V_vectors"]:
            Vp = {i + 2: int(vec[i]) for i in range(sp - 1)}
            if us == 1:
                Vfull = dict(Vp); Vfull[sp + 1] = 1
                dl = SG.def51_radii(np_, Mp, dp, Vfull, sp, ell + 1)
                js = list(range(sp, 1, -1))
            else:
                # prefix: metric radii from the first-nonzero index of this vector
                rec = [x for x in D["diagnostic_radii"] if tuple(x["V"]) == tuple(vec)]
                if not rec:
                    probe["prefix-no-radii"] += 1; continue
                dl = {i: F(v) for i, v in rec[0]["delta"].items()}
                js = list(range(sp - 1, 1, -1))
            alive_go = True; go_fail = None
            for j in js:
                Vnext = 1 if j == sp else Vp[j + 1]
                try:
                    lt = SG.level_test(np_, mp, Mp, dp, Vp, dl, sp, j, Vnext, want_all=False)
                except AssertionError:
                    lt = dict(alive=False, j=j)
                if not lt["alive"]:
                    alive_go = False; go_fail = j; break
            try:
                bt = SG.bottom_test(np_, mp, Mp, dp, Vp, dl, sp)
                alive_b = bt["alive"]
            except AssertionError:
                alive_b = None
            key = ("u=1" if us == 1 else "u>1", "GO-ok" if alive_go else "GO-KILL", "B-ok" if alive_b else ("B-KILL" if alive_b is False else "B-n/a"))
            probe[key] += 1
            if not alive_go or alive_b is False:
                probe_rows.append((n, m, Ms, dict(V), us, [str(x) for x in vec], go_fail, alive_b))
    W("   descend_own route states: %s\n" % dict(states))
    W("   NONEMPTY rows: %d (roster has 66)\n" % len(nonempty_keys))
    W("   outer-vector probe: %s\n" % {"|".join(k): v for k, v in probe.items()})
    for x in probe_rows[:20]:
        W("      %s\n" % (x,))
    out["descend_own_states"] = dict(states)
    out["outer_probe"] = {"|".join(k): v for k, v in probe.items()}
    out["outer_probe_rows"] = probe_rows
    W("   [%.0fs]\n" % (time.time() - t1))
    json.dump(out, open(os.path.join(HERE, "controls.json"), "w"), indent=1, default=str)
    W("wrote controls.json  total %.0fs\n" % (time.time() - t0))


if __name__ == "__main__":
    main()
