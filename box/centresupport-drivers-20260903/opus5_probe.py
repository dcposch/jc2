#!/usr/bin/env python3
"""Third, independent whole-major-tree implementation + hostile diagnostics.

Written from the page images (Def.5.1 p.179; Prop.5.3 p.180; Prop.4.6 p.170;
p.182 deg p / deg q; p.188 & p.201 (8)-(13); Prop.5.6 p.188; Prop.A.3 p.205).
Only the frozen (1)-(13) enumerator `moh_skeleton_full_frozen` is imported.

Screen flags
------------
capacity : impose A_j | Q_j - 1 at every node (derived; see report Sec.B)
ode      : impose P != Q*u for every p-root multiplicity u (Prop.A.3 / (3.7))
passport : impose d_+/g >= S for the cyclic quotient of p^Q/q^P
recenter : treat a nonzero centre at an integral radius <= 0 as removable
"""
from __future__ import annotations
import json, os, sys, time
from fractions import Fraction as F
from functools import lru_cache
from math import gcd, lcm

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import moh_skeleton_full_frozen as B

TRACE = []


class Tree:
    def __init__(self, n, m, Ms, *, recenter=False, ode=False, capacity=False,
                 passport=False, trace=False, gate=False):
        self.n, self.m = n, m
        full = [-m] + list(Ms)
        self.s = s = len(full)
        self.M = {i + 1: full[i] for i in range(s)}
        d = [n]
        for M in full:
            d.append(gcd(d[-1], M))
        self.d = {i + 1: d[i] for i in range(len(d))}
        self.nstar, self.mstar = n // self.d[2], m // self.d[2]
        self.recenter, self.ode = recenter, ode
        self.capacity, self.passport = capacity, passport
        self.trace = trace
        self.gate = gate
        if gate:
            self.recenter = True   # p.190's y -> y - ax - b removes -1 and 0
        self.why = []

    def free_exponents(self, chain):
        """Non-integral, non-radius lattice points of the centre of D_1."""
        dl = {i: self.delta(i, chain[i-1:]) for i in range(1, self.s+1)}
        radii = {dl[i] for i in range(2, self.s+1)}
        free, L = [], 1
        for i in range(self.s-1, 0, -1):
            L = lcm(L, dl[i+1].denominator)
            e = dl[i+1]
            while e < dl[i]:
                if e not in radii and e.denominator != 1:
                    free.append(e)
                e += F(1, L)
        return free

    # -------- Def 5.1(3), branch-specific --------
    def delta(self, i, high):
        num, den = F(self.n - self.M[i]), F(self.n - self.M[self.s] - 1)
        for k, V in zip(range(i + 1, self.s + 1), high):
            num *= V * (self.n - self.M[k]) - self.d[k]
            den *= V * (self.n - self.M[k - 1]) - self.d[k]
        return 1 - num / den

    def node(self, j, high):
        dl = {i: self.delta(i, high[i - j:]) for i in range(j, self.s + 1)}
        L = 1
        for i in range(j + 1, self.s + 1):
            L = lcm(L, dl[i].denominator)
        A = (L * dl[j]).denominator
        Vp = high[0]
        P = Vp * self.d[j] // self.d[j + 1]
        Q = Vp * (self.n - self.M[j]) // self.d[j + 1]
        assert Vp * self.d[j] % self.d[j + 1] == 0
        assert Vp * (self.n - self.M[j]) % self.d[j + 1] == 0
        return dl[j], L, A, P, Q, F(self.d[j], self.n - self.M[j])

    def bottom(self, high):
        dl = {i: self.delta(i, high[i - 1:]) for i in range(1, self.s + 1)}
        L = 1
        for i in range(2, self.s + 1):
            L = lcm(L, dl[i].denominator)
        A1 = (L * dl[1]).denominator
        V2 = high[0]
        c12 = self.nstar * V2 % A1 == 0 and (self.mstar * V2 - 1) % A1 == 0
        c13 = self.mstar * V2 % A1 == 0 and (self.nstar * V2 - 1) % A1 == 0
        return (c12 or c13), A1, c12, c13

    def pport(self, A, P, Q, b, orbits):
        if (Q - 1) % A:
            return False
        S = (Q - 1) // A
        if len(orbits) > S:
            return False
        w = [(P - Q * b) // A] + [P - Q * v for v in orbits] + [P] * (S - len(orbits))
        if any(x == 0 for x in w):
            return False
        g = 0
        for x in w:
            g = gcd(g, abs(x))
        return g > 0 and sum(x for x in w if x > 0) // g >= S

    # -------- recursion; need = (V_j, V_{j-1}, ..., V_2) or None --------
    def ok(self, j, high, danger, need):
        key = (j, high, danger, need)
        if key in self._memo:
            return self._memo[key]
        r = self._ok(j, high, danger, need)
        self._memo[key] = r
        return r

    def _ok(self, j, high, danger, need):
        dl, L, A, P, Q, lo = self.node(j, high)
        if self.capacity and (Q - 1) % A:
            self.why.append((j, "A does not divide Q-1", A, P, Q))
            return None
        if need is not None and not (F(need[0]) > lo):
            self.why.append((j, "selected V_j not major", need[0], str(lo)))
            return None
        removable = self.recenter and dl.denominator == 1 and dl <= 0

        def child(v, is_zero, tail):
            nd = danger and (is_zero or removable)
            nh = (v,) + high
            if j == 2:
                good, A1, c12, c13 = self.bottom(nh)
                if nd and (not self.gate or not self.free_exponents(nh)):
                    return None
                return {"A1": A1, "V2": v, "zero": is_zero} if good else None
            return self.ok(j - 1, nh, nd, tail)

        for b in range(P % A, P + 1, A):
            if self.ode and b > 0 and P == Q * b:
                continue
            zmaj = F(b) > lo
            # p.200(4): EVERY above-threshold factor extends, including the
            # fixed zero factor, whether or not the recorded path selects it.
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
                sol = self.fill(tgt, kk, tuple(coins), hm, A, P, Q, b, pre)
                if sol is not None:
                    return {"j": j, "A": A, "P": P, "Q": Q, "b": b,
                            "S": (Q - 1) // A if (Q - 1) % A == 0 else None,
                            "delta": str(dl), "lo": str(lo), "mode": mode,
                            "orbits": list(pre) + list(sol), "zero_major": zmaj,
                            "child": sc, "danger": danger}
        self.why.append((j, "no admissible (b, orbit multiset)", A, P, Q,
                         str(lo), high, need))
        return None

    def fill(self, target, kmax, coins, has_major, A, P, Q, b, pre):
        if kmax < 0 or target < 0:
            return None
        pas, pp = self.passport, (A, P, Q, b)

        @lru_cache(maxsize=None)
        def go(rem, k, idx, hm, used):
            if rem == 0:
                if not hm:
                    return None
                if pas and not self.pport(A, P, Q, b, tuple(pre) + used):
                    return None
                return ()
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
        self.why = []
        if not (self.d[self.s] > V[self.s] > F(self.d[self.s], 2)):
            return None
        need = tuple(V[i] for i in range(self.s - 1, 1, -1))
        return self.ok(self.s - 1, (V[self.s],), True, need)


def screens():
    return {
        "TREE":            dict(),
        "TREE_CAP":        dict(capacity=True),
        "TREE_ODE":        dict(ode=True),
        "TREE_ODE_CAP":    dict(ode=True, capacity=True),
        "TREE_ODE_PASS":   dict(ode=True, capacity=True, passport=True),
        "TREE_REC":        dict(recenter=True),
        "TREE_REC_ODE":    dict(recenter=True, ode=True),
        "TREE_REC_PASS":   dict(recenter=True, ode=True, capacity=True, passport=True),
    }


def run_n100():
    rows = [(n, m, Ms, V) for n in range(4, 101)
            for m, Ms, V in B.census(n, Kmin=2, full=True)]
    printed = {(n, m, tuple(Ms), tuple(sorted(V.items())))
               for n, m, Ms, V, *_ in B.MOH_TABLE}
    out = {}
    for name, kw in screens().items():
        t0 = time.time()
        surv = set()
        for n, m, Ms, V in rows:
            if Tree(n, m, Ms, **kw).embeds(V) is not None:
                surv.add((n, m, tuple(Ms), tuple(sorted(V.items()))))
        out[name] = {"rows": len(surv),
                     "classes": len({(k[0], k[1]) for k in surv}),
                     "printed_kept": len(surv & printed),
                     "excess": len(surv - printed),
                     "sec": round(time.time() - t0, 1)}
        print(f"{name:16s} rows={len(surv):5d} classes={out[name]['classes']:3d} "
              f"printed={len(surv & printed)}/6 excess={len(surv-printed):4d} "
              f"({out[name]['sec']}s)", flush=True)
    print("input rows:", len(rows))
    return out


if __name__ == "__main__":
    run_n100()


def run_repaired():
    rows = [(n, m, Ms, V) for n in range(4, 101)
            for m, Ms, V in B.census(n, Kmin=2, full=True)]
    printed = {(n, m, tuple(Ms), tuple(sorted(V.items())))
               for n, m, Ms, V, *_ in B.MOH_TABLE}
    cfg = {
        "PARTITION_ONLY":      dict(),
        "PARTITION_ODE":       dict(ode=True),
        "PARTITION_PASS":      dict(ode=True, capacity=True, passport=True),
        "GATED_TREE":          dict(gate=True),
        "GATED_TREE_ODE":      dict(gate=True, ode=True),
        "GATED_TREE_PASS":     dict(gate=True, ode=True, capacity=True, passport=True),
    }
    import time
    for name, kw in cfg.items():
        no56 = name.startswith("PARTITION")
        t0 = time.time(); surv = set()
        for n, m, Ms, V in rows:
            T = Tree(n, m, Ms, **kw)
            if no56:
                T._memo = {}
                if not (T.d[T.s] > V[T.s] > F(T.d[T.s], 2)):
                    continue
                need = tuple(V[i] for i in range(T.s-1, 1, -1))
                r = T.ok(T.s-1, (V[T.s],), False, need)     # danger disabled
            else:
                r = T.embeds(V)
            if r is not None:
                surv.add((n, m, tuple(Ms), tuple(sorted(V.items()))))
        print(f"{name:18s} rows={len(surv):5d} classes={len({(k[0],k[1]) for k in surv}):3d} "
              f"printed={len(surv & printed)}/6 excess={len(surv-printed):4d} "
              f"({time.time()-t0:.1f}s)", flush=True)
