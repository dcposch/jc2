#!/usr/bin/env python3
"""Replay C_FULL_TREE_POLYNOMIAL_ODE on the (1)-(13) census with the actual
centre stabilizer (zero keeps L; nonzero L <- lcm(L, den δ)).

Coarse L_i = lcm(den δ_{i+1..s}) is Moh (8) / moh_skeleton_full.Skel.A and
opus5_probe.Tree.node. Actual L is closure_fixed.py:75 and
own_v_routes.OwnVRouteTree child next_L / descend_own.py:151-152.

A row is necessary tower data, not a polynomial pair. Counts are DATA.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import sys
import time
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from math import gcd, lcm
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path("/home/ubuntu/jc2")
LANE = Path("/tmp/jc2-lane.adumu9/inputs")
OUT_JSON = HERE / "actual-stab-census.json"


def load_mod(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


B = load_mod("moh_skeleton_full", LANE / "moh_skeleton_full.py")
sys.modules["moh_skeleton_full_frozen"] = B

# Uncharged repo read: live opus5_probe Tree, byte-class of the census-coverage
# snapshot. Used as the coarse-control evaluator.
OP_PATH = ROOT / "box" / "wholetree-drivers-20260903" / "opus5_probe.py"
OP = load_mod("opus5_probe_live", OP_PATH)


def qstr(x):
    x = F(x)
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def row_key(n, m, Ms, V):
    if isinstance(V, dict):
        vt = tuple(int(V[i]) for i in range(2, len(Ms) + 2))
    else:
        vt = tuple(int(v) for v in V)
    return (int(n), int(m), tuple(int(x) for x in Ms), vt)


class StabTree:
    """opus5_probe.Tree with an explicit centre-L state.

    actual=False: next_L always lcm(L, den δ)  == Tree.node coarse L.
    actual=True:  next_L = L on a zero factor, lcm(L, den δ) on nonzero.
    ODE / recenter / Prop 5.6 danger / (12)/(13) are the operative flags.
    """

    def __init__(self, n, m, Ms, *, actual=False):
        self.n, self.m = n, m
        full = [-m] + list(Ms)
        self.s = s = len(full)
        self.M = {i + 1: full[i] for i in range(s)}
        d = [n]
        for M in full:
            d.append(gcd(d[-1], M))
        self.d = {i + 1: d[i] for i in range(len(d))}
        self.nstar, self.mstar = n // self.d[2], m // self.d[2]
        self.actual = actual
        self.recenter = True
        self.ode = True
        self.gate = False
        self.capacity = False
        self.passport = False

    def delta(self, i, high):
        num, den = F(self.n - self.M[i]), F(self.n - self.M[self.s] - 1)
        for k, V in zip(range(i + 1, self.s + 1), high):
            num *= V * (self.n - self.M[k]) - self.d[k]
            den *= V * (self.n - self.M[k - 1]) - self.d[k]
        return 1 - num / den

    def ok(self, j, high, danger, need, centre_L):
        key = (j, high, danger, need, centre_L)
        if key in self._memo:
            return self._memo[key]
        r = self._ok(j, high, danger, need, centre_L)
        self._memo[key] = r
        return r

    def _ok(self, j, high, danger, need, centre_L):
        dl = self.delta(j, high)
        A = (centre_L * dl).denominator
        Vp = high[0]
        P = Vp * self.d[j] // self.d[j + 1]
        Q = Vp * (self.n - self.M[j]) // self.d[j + 1]
        assert Vp * self.d[j] % self.d[j + 1] == 0
        assert Vp * (self.n - self.M[j]) % self.d[j + 1] == 0
        lo = F(self.d[j], self.n - self.M[j])
        if need is not None and not (F(need[0]) > lo):
            return None
        removable = self.recenter and dl.denominator == 1 and dl <= 0

        def child(v, is_zero, tail):
            if self.actual and is_zero:
                next_L = centre_L
            else:
                next_L = lcm(centre_L, dl.denominator)
            nd = danger and (is_zero or removable)
            nh = (v,) + high
            if j == 2:
                d1 = self.delta(1, nh)
                A1 = (next_L * d1).denominator
                c12 = self.nstar * v % A1 == 0 and (self.mstar * v - 1) % A1 == 0
                c13 = self.mstar * v % A1 == 0 and (self.nstar * v - 1) % A1 == 0
                if nd:
                    return None
                return {"A1": A1, "V2": v, "zero": is_zero} if (c12 or c13) else None
            return self.ok(j - 1, nh, nd, tail, next_L)

        for b in range(P % A, P + 1, A):
            if self.ode and b > 0 and P == Q * b:
                continue
            zmaj = F(b) > lo
            if zmaj and child(b, True, None) is None:
                continue
            total = (P - b) // A
            cap = (Q - (1 if b > 0 else 0)) // A
            coins = []
            for v in range(1, total + 1):
                if self.ode and P == Q * v:
                    continue
                maj = F(v) > lo
                if maj and child(v, False, None) is None:
                    continue
                coins.append((v, maj))
            modes = [("free", ())] if need is None else []
            if need is not None:
                if b == need[0] and zmaj:
                    modes.append(("zero", ()))
                if any(v == need[0] for v, _ in coins) and need[0] <= total:
                    modes.append(("nonzero", (need[0],)))
            for mode, pre in modes:
                if mode == "zero":
                    sc = child(b, True, need[1:] or None)
                elif mode == "nonzero":
                    sc = child(need[0], False, need[1:] or None)
                else:
                    sc = None
                if mode != "free" and sc is None:
                    continue
                tgt = total - sum(pre)
                kk = cap - len(pre)
                hm = zmaj or bool(pre)
                sol = self.fill(tgt, kk, tuple(coins), hm)
                if sol is not None:
                    return {"j": j, "A": A, "P": P, "Q": Q, "b": b,
                            "delta": str(dl), "lo": str(lo), "mode": mode,
                            "orbits": list(pre) + list(sol), "zero_major": zmaj,
                            "child": sc, "danger": danger, "centre_L": centre_L}
        return None

    def fill(self, target, kmax, coins, has_major):
        if kmax < 0 or target < 0:
            return None

        @lru_cache(maxsize=None)
        def go(rem, k, idx, hm, used):
            if rem == 0:
                return () if hm else None
            if k == 0:
                return None
            for i in range(idx, len(coins)):
                v, maj = coins[i]
                if v > rem:
                    break
                t = go(rem - v, k - 1, i, hm or maj, used + (v,))
                if t is not None:
                    return (v,) + t
            return None

        return go(target, kmax, 0, has_major, ())

    def embeds(self, V):
        self._memo = {}
        if not (self.d[self.s] > V[self.s] > F(self.d[self.s], 2)):
            return None
        need = tuple(V[i] for i in range(self.s - 1, 1, -1))
        return self.ok(self.s - 1, (V[self.s],), True, need, 1)


def operative_live(n, m, Ms, V):
    """C_FULL_TREE_POLYNOMIAL_ODE via live opus5_probe (coarse L)."""
    T = OP.Tree(n, m, Ms, gate=False, ode=True, capacity=False, passport=False)
    T.recenter = True
    T._memo = {}
    T.why = []
    if not (T.d[T.s] > V[T.s] > F(T.d[T.s], 2)):
        return False
    need = tuple(V[i] for i in range(T.s - 1, 1, -1))
    return T.ok(T.s - 1, (V[T.s],), True, need) is not None


def operative_stab(n, m, Ms, V, *, actual):
    T = StabTree(n, m, list(Ms), actual=actual)
    return T.embeds(V) is not None


def ser_row(n, m, Ms, V, extra=None):
    rec = {"n": int(n), "m": int(m),
           "Ms": [int(x) for x in Ms],
           "V": [int(V[i]) for i in range(2, len(Ms) + 2)]}
    if extra:
        rec.update(extra)
    return rec


def selected_zero_routes(S):
    """Zero-route first-nonzero sites on the selected V path.

    A level i is zero-ok when (P - V_i) % A == 0 (Moh (11) / descend_own
    zero_ok). Walking down from the top, every prefix of zero-ok levels is a
    zero route; the first nonzero-ok level below it is a first-nonzero site.
    N_coarse = A_i^{Moh (8)}; N_actual = den(δ_i) on a zero prefix (L=1).
    """
    s, d, V, delta = S.s, S.d, S.V, S.delta
    sites = []
    prefix_zero_c = True
    prefix_zero_a = True
    for i in range(s - 1, 1, -1):
        di = delta[i]
        P = V[i + 1] * d[i] // d[i + 1]
        L_c = 1
        for k in range(i + 1, s + 1):
            L_c = lcm(L_c, delta[k].denominator)
        A_c = (L_c * di).denominator
        A_a = di.denominator  # L=1 on a zero prefix
        z_c = (P - V[i]) % A_c == 0
        z_a = (P - V[i]) % A_a == 0
        nz_c = di > 0 and A_c * V[i] <= P
        nz_a = di > 0 and A_a * V[i] <= P
        if prefix_zero_c and nz_c:
            epsN_c = di * A_c
            sites.append(dict(
                i=i, kind="coarse_zero_prefix",
                eps=qstr(di), L_coarse=L_c, A_coarse=A_c, A_actual=A_a,
                epsN_coarse=qstr(epsN_c),
                epsN_coarse_in_Z=epsN_c.denominator == 1,
                epsN_actual_in_Z=(di * A_a).denominator == 1,
                P=P, V=V[i],
            ))
        if prefix_zero_a and nz_a:
            # descend_own first-nonzero (actual modulus). Record even if
            # already listed, tagged separately.
            epsN_c = di * A_c
            sites.append(dict(
                i=i, kind="actual_zero_prefix",
                eps=qstr(di), L_coarse=L_c, A_coarse=A_c, A_actual=A_a,
                epsN_coarse=qstr(epsN_c),
                epsN_coarse_in_Z=epsN_c.denominator == 1,
                epsN_actual_in_Z=(di * A_a).denominator == 1,
                P=P, V=V[i],
            ))
        if not z_c:
            prefix_zero_c = False
        if not z_a:
            prefix_zero_a = False
        if not prefix_zero_c and not prefix_zero_a:
            break
    return sites


def load_roster():
    out = {}
    for line in open(LANE / "roster.jsonl"):
        r = json.loads(line)
        src = r["source"]
        Ms = src["M"][1:]
        V = {i + 2: src["V"][i] for i in range(len(src["V"]))}
        k = row_key(src["n"], src["m"], Ms, V)
        out[k] = r["row_id"]
    return out


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def r063_control():
    n, m, Ms, V = 168, 112, [140, 160, 166], {2: 3, 3: 21, 4: 3}
    S = B.Skel(n, m, Ms, V)
    sites = selected_zero_routes(S)
    live = operative_live(n, m, Ms, V)
    coarse = operative_stab(n, m, Ms, V, actual=False)
    actual = operative_stab(n, m, Ms, V, actual=True)
    A2_c = S.A(2)
    A2_a = S.delta[2].denominator
    return dict(
        n=n, m=m, Ms=Ms, V=[3, 21, 3], s=S.s,
        delta=[qstr(S.delta[i]) for i in range(1, S.s + 1)],
        L2_coarse=S.L(2), A2_coarse=A2_c, A2_actual=A2_a,
        P3=S.V[4] * S.d[3] // S.d[4], V3=S.V[3],
        eps=qstr(S.delta[2]),
        epsN_coarse=qstr(S.delta[2] * A2_c),
        epsN_actual=qstr(S.delta[2] * A2_a),
        live_op=live, stab_coarse_op=coarse, stab_actual_op=actual,
        sites=sites,
    )


def main():
    t0 = time.monotonic()
    roster = load_roster()
    residual64_ids = {f"R{i:03d}" for i in range(1, 67)} - {"R001", "R063"}
    assert len(roster) == 66
    assert len(residual64_ids) == 64

    ctrl = r063_control()
    print("R063 control", json.dumps(ctrl, indent=2)[:1200], flush=True)
    if not (ctrl["live_op"] and ctrl["stab_coarse_op"]):
        raise SystemExit("R063 must be coarse-operative")
    if ctrl["epsN_coarse"] != "3/5":
        raise SystemExit(f"R063 epsN_coarse expected 3/5 got {ctrl['epsN_coarse']}")
    if ctrl["A2_coarse"] != 2 or ctrl["A2_actual"] != 10:
        raise SystemExit(f"R063 A2 {ctrl['A2_coarse']} / {ctrl['A2_actual']}")

    # Spot-check: StabTree(actual=False) == live opus5_probe on n<=90.
    mismatch = 0
    checked = 0
    for n in range(16, 91):
        for m, Ms, V in B.census(n, Kmin=2, full=True):
            a = operative_live(n, m, Ms, V)
            b = operative_stab(n, m, Ms, V, actual=False)
            checked += 1
            if a != b:
                mismatch += 1
                print("MISMATCH", n, m, Ms, dict(V), a, b, flush=True)
    print(f"coarse StabTree vs live opus5_probe: checked={checked} mismatch={mismatch}",
          flush=True)
    if mismatch:
        raise SystemExit("StabTree(actual=False) disagrees with opus5_probe")

    census = 0
    coarse_keys = []
    actual_keys = []
    recs = {}
    s_hist_c = Counter()
    s_hist_a = Counter()
    n_hist_c = Counter()
    n_hist_a = Counter()

    for n in range(16, 201):
        t1 = time.monotonic()
        nn = 0
        for m, Ms, V in B.census(n, Kmin=2, full=True):
            census += 1
            nn += 1
            k = row_key(n, m, Ms, V)
            live = operative_live(n, m, Ms, V)
            actual = operative_stab(n, m, Ms, V, actual=True)
            if live:
                coarse_keys.append(k)
                s_hist_c[len(Ms) + 1] += 1
                n_hist_c[n] += 1
            if actual:
                actual_keys.append(k)
                s_hist_a[len(Ms) + 1] += 1
                n_hist_a[n] += 1
            if live or actual:
                S = B.Skel(n, m, list(Ms), V)
                sites = selected_zero_routes(S)
                fail_c = any(
                    s["kind"] == "actual_zero_prefix" and not s["epsN_coarse_in_Z"]
                    for s in sites
                )
                fail_c_prefix = any(
                    s["kind"] == "coarse_zero_prefix" and not s["epsN_coarse_in_Z"]
                    for s in sites
                )
                fail_a = any(not s["epsN_actual_in_Z"] for s in sites)
                recs[k] = dict(
                    n=n, m=m, Ms=list(Ms),
                    V=[V[i] for i in range(2, len(Ms) + 2)],
                    s=S.s, us=int(S.d[S.s] - S.V[S.s]),
                    roster=roster.get(k),
                    live=live, actual=actual,
                    epsN_fail_actual_prefix_coarseN=fail_c,
                    epsN_fail_coarse_prefix_coarseN=fail_c_prefix,
                    epsN_fail_actualN=fail_a,
                    sites=[s for s in sites if not s["epsN_coarse_in_Z"]
                           or s["kind"] == "actual_zero_prefix"],
                )
        print(f"  n={n:3d} census+={nn:4d} total={census:5d} "
              f"coarse_op={len(coarse_keys):4d} actual_op={len(actual_keys):4d} "
              f"{time.monotonic()-t1:.1f}s", flush=True)

    coarse_set, actual_set = set(coarse_keys), set(actual_keys)
    lost = sorted(coarse_set - actual_set)
    gained = sorted(actual_set - coarse_set)

    def pack(k):
        n, m, Ms, Vt = k
        rec = recs[k]
        return ser_row(n, m, Ms, {i + 2: Vt[i] for i in range(len(Vt))}, extra=dict(
            s=rec["s"], us=rec["us"], roster=rec["roster"],
            epsN_fail_actual_prefix_coarseN=rec["epsN_fail_actual_prefix_coarseN"],
            epsN_fail_coarse_prefix_coarseN=rec["epsN_fail_coarse_prefix_coarseN"],
            sites=rec["sites"],
        ))

    coarse_op_recs = [recs[k] for k in coarse_keys]
    actual_op_recs = [recs[k] for k in actual_keys]

    def count_fail(rs, field):
        return sum(1 for r in rs if r[field])

    roster_status = []
    for k, rid in sorted(roster.items(), key=lambda kv: kv[1]):
        rec = recs.get(k)
        if rec is None:
            # not operative under either; still record skeleton
            n, m, Ms, Vt = k
            V = {i + 2: Vt[i] for i in range(len(Vt))}
            live = operative_live(n, m, Ms, V)
            actual = operative_stab(n, m, Ms, V, actual=True)
            S = B.Skel(n, m, list(Ms), V)
            sites = selected_zero_routes(S)
            rec = dict(live=live, actual=actual, s=S.s,
                       us=int(S.d[S.s] - S.V[S.s]),
                       epsN_fail_actual_prefix_coarseN=any(
                           s["kind"] == "actual_zero_prefix" and not s["epsN_coarse_in_Z"]
                           for s in sites),
                       sites=sites)
        roster_status.append(dict(
            row_id=rid, n=k[0], m=k[1], Ms=list(k[2]), V=list(k[3]),
            s=rec["s"], us=rec.get("us"),
            coarse_op=bool(rec["live"]), actual_op=bool(rec["actual"]),
            changed=bool(rec["live"]) != bool(rec["actual"]),
            residual64=rid in residual64_ids,
            epsN_fail_actual_prefix_coarseN=rec["epsN_fail_actual_prefix_coarseN"],
            sites=rec.get("sites") or [],
        ))

    roster_changed = [r for r in roster_status if r["changed"]]
    r64_changed = [r for r in roster_status if r["residual64"] and r["changed"]]
    r66_coarse = sum(1 for r in roster_status if r["coarse_op"])
    r66_actual = sum(1 for r in roster_status if r["actual_op"])
    r64_coarse = sum(1 for r in roster_status if r["residual64"] and r["coarse_op"])
    r64_actual = sum(1 for r in roster_status if r["residual64"] and r["actual_op"])

    out = dict(
        schema="jc2.actual-stabilizer-census/v1",
        semantic_type="NECESSARY_TOWER_CONFIGURATION_NOT_POLYNOMIAL_PAIR",
        charged_moh_skeleton_full_sha256=sha256_file(LANE / "moh_skeleton_full.py"),
        census_nlo=16, census_nhi=200, Kmin=2, full=True,
        census=census,
        coarse_operative=len(coarse_keys),
        actual_operative=len(actual_keys),
        lost_count=len(lost),
        gained_count=len(gained),
        s_hist_coarse={str(k): v for k, v in sorted(s_hist_c.items())},
        s_hist_actual={str(k): v for k, v in sorted(s_hist_a.items())},
        roster66=dict(
            coarse_op=r66_coarse, actual_op=r66_actual,
            changed=[r["row_id"] for r in roster_changed],
        ),
        residual64=dict(
            definition="roster 66 minus R001 (Xu Cor.5.3) minus R063 (printed N=0 / child integrality)",
            coarse_op=r64_coarse, actual_op=r64_actual,
            changed=[r["row_id"] for r in r64_changed],
            affected=bool(r64_changed),
        ),
        epsN_screen=dict(
            meaning=("zero-route first-nonzero on the selected path; "
                     "N_coarse = Moh-(8) A_i; N_actual = den(δ_i) (L=1). "
                     "Row fails if some descend_own-style (actual-zero-prefix) "
                     "first-nonzero has ε N_coarse not in Z."),
            coarse_operative_fail_actual_prefix=count_fail(
                coarse_op_recs, "epsN_fail_actual_prefix_coarseN"),
            coarse_operative_fail_coarse_prefix=count_fail(
                coarse_op_recs, "epsN_fail_coarse_prefix_coarseN"),
            actual_operative_fail_actualN=count_fail(
                actual_op_recs, "epsN_fail_actualN"),
            actual_operative_fail_coarseN_on_actual_prefix=count_fail(
                actual_op_recs, "epsN_fail_actual_prefix_coarseN"),
        ),
        r063_control=ctrl,
        lost_rows=[pack(k) for k in lost],
        gained_rows=[pack(k) for k in gained],
        roster_status=roster_status,
        coarse_stabtree_vs_live_mismatch=mismatch,
        seconds=round(time.monotonic() - t0, 2),
    )
    OUT_JSON.write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps({k: out[k] for k in out if k not in
                      ("lost_rows", "gained_rows", "roster_status", "r063_control")},
                     indent=2), flush=True)
    print(f"wrote {OUT_JSON} ({OUT_JSON.stat().st_size} bytes) in {out['seconds']}s",
          flush=True)


if __name__ == "__main__":
    main()
