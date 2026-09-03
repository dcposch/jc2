#!/usr/bin/env python3
"""Independent implementation of Moh's *whole factor-tree* restriction.

This does not use candidate_eval.py (or any other candidate implementation).
It imports only the frozen (1)--(13) enumerator and re-derives the extra
factor-partition recursion from Moh 1983, Props. 4.6, 5.3--5.6, the theorem
on p.200, and Prop. A.3.

At a level j the common polynomial p has degree

    P = V[j+1] d[j] / d[j+1]

and the square-free polynomial q has degree

    Q = V[j+1] (n-M[j]) / d[j+1].

If A is the incremental denominator of delta[j], the roots of p consist of
nonzero Galois orbits of A roots (one multiplicity v for every root in an
orbit), and possibly the fixed root zero, of multiplicity b.  Thus

    P = A * sum(v_orbit) + b.

Every root of multiplicity v > d[j]/(n-M[j]) is major and *each* such root
must extend to a valid child tower.  Prop. A.3/p.200 also requires at least
one major root.  Since q is square-free and contains all roots of p, the
number of distinct p-roots may not exceed Q (with the same orbit structure).

The selected V path recorded by the census must embed in this whole tree.
Prop. 5.6 forbids an all-zero chain.  The enriched form implemented here also
keeps a chain "pure after translation" when a nonzero coefficient occurs at
an integral (hence polynomial/removable) exponent, as in Prop. 5.4.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from functools import lru_cache
from fractions import Fraction as F
from math import gcd, lcm

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import moh_skeleton_full_frozen as BASE


class WholeTree:
    """Factor-tree checker for one fixed (n,m,M_2,...,M_s) skeleton."""

    def __init__(self, n, m, Ms, removable_prefix=True, passport=False):
        self.n = n
        self.m = m
        self.s = 1 + len(Ms)
        self.M = {1: -m, **{i + 2: x for i, x in enumerate(Ms)}}
        ds = [n]
        for i in range(1, self.s + 1):
            ds.append(gcd(ds[-1], self.M[i]))
        self.d = {i + 1: ds[i] for i in range(len(ds))}
        self.removable_prefix = removable_prefix
        self.passport = passport

    def _vmap(self, j, high):
        """high=(V_{j+1},...,V_s), in increasing subscript order."""
        assert len(high) == self.s - j
        return {j + 1 + k: v for k, v in enumerate(high)}

    def delta(self, i, high_from_i):
        """Def. 5.1(3); high_from_i is (V_{i+1},...,V_s)."""
        V = self._vmap(i, high_from_i)
        num = F(self.n - self.M[i])
        den = F(self.n - self.M[self.s] - 1)
        for k in range(i + 1, self.s + 1):
            num *= V[k] * (self.n - self.M[k]) - self.d[k]
            den *= V[k] * (self.n - self.M[k - 1]) - self.d[k]
        return 1 - num / den

    def delta_from_node(self, i, j, high):
        """delta_i for i>=j from a node state (j, V_{j+1..s})."""
        assert i >= j
        drop = i - j
        return self.delta(i, high[drop:])

    def A(self, j, high):
        Lj = 1
        for i in range(j + 1, self.s + 1):
            Lj = lcm(Lj, self.delta_from_node(i, j, high).denominator)
        return (Lj * self.delta_from_node(j, j, high)).denominator

    def node_data(self, j, high):
        Vnext = high[0]
        assert (Vnext * self.d[j]) % self.d[j + 1] == 0
        assert (Vnext * (self.n - self.M[j])) % self.d[j + 1] == 0
        P = Vnext * self.d[j] // self.d[j + 1]
        Q = Vnext * (self.n - self.M[j]) // self.d[j + 1]
        A = self.A(j, high)
        h = F(self.d[j], self.n - self.M[j])
        delta = self.delta_from_node(j, j, high)
        return P, Q, A, h, delta

    def root_multiplicity_allowed(self, v, P, Q):
        """Local consequence of the A.3 differential equation.

        At a shared simple q-root alpha of p-multiplicity v, division of
        D(P,Q,p,q)=c p by p and evaluation at alpha gives
        (P-Qv)q_alpha(alpha)=c != 0.  Hence Qv != P.
        """
        return not self.passport or Q * v != P

    @staticmethod
    def is_major(v, h):
        return F(v) > h

    def next_danger(self, danger, label, delta):
        """Whether the prefix is still polynomial-removable after this edge."""
        if not danger:
            return False
        if label == "zero":
            return True
        if not self.removable_prefix:
            return False
        # In Moh's range delta>-1 and delta<1.  An integral exponent is delta=0;
        # Prop. 5.4 absorbs its nonzero coefficient into h(x).
        return delta.denominator == 1

    def bottom_arithmetic(self, high_with_v2):
        """Moh (12)/(13) for a completed path high=(V_2,...,V_s)."""
        assert len(high_with_v2) == self.s - 1
        L1 = 1
        for i in range(2, self.s + 1):
            L1 = lcm(L1, self.delta(i, high_with_v2[i - 1:]).denominator)
        d1 = self.delta(1, high_with_v2)
        A1 = (L1 * d1).denominator
        V2 = high_with_v2[0]
        ns, ms = self.n // self.d[2], self.m // self.d[2]
        c12 = ns * V2 % A1 == 0 and (ms * V2 - 1) % A1 == 0
        c13 = ms * V2 % A1 == 0 and (ns * V2 - 1) % A1 == 0
        return c12 or c13, A1, c12, c13

    def child_generic(self, j, high, v, label, danger, delta):
        ndanger = self.next_danger(danger, label, delta)
        child_high = (v,) + high
        if j == 2:
            ok = self.bottom_arithmetic(child_high)[0]
            # Prop. 5.6: after removal of a polynomial prefix, a pure final
            # pi-root contradicts degree minimality.
            return ok and not ndanger
        return self.generic_node(j - 1, child_high, ndanger) is not None

    @staticmethod
    def _fill(target, max_orbits, allowed, require_major, passport=None):
        """Unbounded orbit knapsack; return a multiplicity tuple or None.

        ``passport=(P,Q,A,b,reserved)`` invokes the cyclic-quotient
        rational-map test; ``reserved`` lists nonzero p-orbits already used by
        the selected path.
        """
        if target < 0 or max_orbits < 0:
            return None
        if passport is None:
            initial_g = initial_plus = 0
        else:
            P, Q, A, b, reserved = passport
            if Q % A != (1 % A):
                return None
            S = (Q - 1) // A
            weights = [(P - Q * b) // A]
            weights += [P - Q * v for v in reserved]
            if any(w == 0 for w in weights) or len(reserved) > S:
                return None
            initial_g = 0
            initial_plus = 0
            for w in weights:
                initial_g = gcd(initial_g, abs(w))
                initial_plus += max(w, 0)

        # Retain gcd and positive divisor degree in the state.  Two factor
        # partitions with the same sum/count need not have the same passport.
        states = {(0, 0, False, initial_g, initial_plus): ()}

        def terminal_ok(k, has_major, gg, dplus):
            if require_major and not has_major:
                return False
            if passport is None:
                return True
            pad = S - len(reserved) - k
            if pad < 0:
                return False
            if pad:
                gg = gcd(gg, P)
                dplus += pad * P
            return gg > 0 and dplus // gg >= S

        for total in range(target + 1):
            layer = [x for x in states.items() if x[0][0] == total]
            for (sm, k, has_major, gg, dplus), witness in layer:
                if sm == target and terminal_ok(k, has_major, gg, dplus):
                    return witness
                if k == max_orbits:
                    continue
                for v, major in allowed:
                    ns = sm + v
                    if ns > target:
                        continue
                    if passport is None:
                        ng, np = 0, 0
                    else:
                        w = P - Q * v
                        if w == 0:
                            continue
                        ng, np = gcd(gg, abs(w)), dplus + max(w, 0)
                    key = (ns, k + 1, has_major or major, ng, np)
                    states.setdefault(key, witness + (v,))
        for (sm, k, has_major, gg, dplus), witness in states.items():
            if sm == target and terminal_ok(k, has_major, gg, dplus):
                return witness
        return None

    @lru_cache(maxsize=None)
    def generic_node(self, j, high, danger):
        """A complete valid factor subtree, with no selected-path constraint."""
        P, Q, A, h, delta = self.node_data(j, high)
        qrem = Q % A
        if qrem not in (0, 1 % A):
            return None
        for b in range(P + 1):
            if (P - b) % A:
                continue
            if b and qrem != (1 % A):  # q must contain the zero root of p
                continue
            if b and not self.root_multiplicity_allowed(b, P, Q):
                continue
            zero_major = b > 0 and self.is_major(b, h)
            if zero_major and not self.child_generic(j, high, b, "zero", danger, delta):
                continue
            root_cost = 1 if b else 0
            kmax = (Q - root_cost) // A
            target = (P - b) // A
            allowed = []
            for v in range(1, target + 1):
                if not self.root_multiplicity_allowed(v, P, Q):
                    continue
                major = self.is_major(v, h)
                if not major or self.child_generic(j, high, v, "nonzero", danger, delta):
                    allowed.append((v, major))
            pp = (P, Q, A, b, ()) if self.passport else None
            coins = self._fill(target, kmax, tuple(allowed), not zero_major, pp)
            if coins is not None:
                return {
                    "j": j, "P": P, "Q": Q, "A": A,
                    "h": str(h), "delta": str(delta), "danger": danger,
                    "b": b, "orbits": list(coins),
                }
        return None

    def child_embed(self, j, high, selected_tail, v, label, danger, delta):
        assert selected_tail and selected_tail[0] == v
        ndanger = self.next_danger(danger, label, delta)
        child_high = (v,) + high
        if j == 2:
            ok = self.bottom_arithmetic(child_high)[0]
            if not ok or ndanger:
                return None
            return {"bottom": True, "label": label,
                    "A1": self.bottom_arithmetic(child_high)[1]}
        return self.embed_node(j - 1, child_high, selected_tail[1:], ndanger)

    def _generic_fill_for_partition(self, target, kmax, j, high, danger, delta,
                                    P, Q, A, h, require_major, b,
                                    reserved=()):
        allowed = []
        for v in range(1, target + 1):
            if not self.root_multiplicity_allowed(v, P, Q):
                continue
            major = self.is_major(v, h)
            if not major or self.child_generic(j, high, v, "nonzero", danger, delta):
                allowed.append((v, major))
        pp = (P, Q, A, b, tuple(reserved)) if self.passport else None
        return self._fill(target, kmax, tuple(allowed), require_major, pp)

    def embed_node(self, j, high, selected_tail, danger):
        """Return witness iff the fixed selected V path embeds in a whole tree."""
        assert len(selected_tail) == j - 1
        selected = selected_tail[0]
        P, Q, A, h, delta = self.node_data(j, high)
        if not self.is_major(selected, h):
            return None
        if not self.root_multiplicity_allowed(selected, P, Q):
            return None
        qrem = Q % A
        if qrem not in (0, 1 % A):
            return None

        # Selected path uses the fixed (zero) root: b must equal V_j.
        b = selected
        if b <= P and (P - b) % A == 0 and qrem == (1 % A):
            child = self.child_embed(j, high, selected_tail, b, "zero", danger, delta)
            if child is not None:
                kmax = (Q - 1) // A
                target = (P - b) // A
                coins = self._generic_fill_for_partition(
                    target, kmax, j, high, danger, delta, P, Q, A, h, False,
                    b)
                if coins is not None:
                    return {"j": j, "selected_label": "zero", "selected": selected,
                            "P": P, "Q": Q, "A": A, "h": str(h),
                            "delta": str(delta), "danger": danger, "b": b,
                            "orbits": list(coins), "child": child}

        # Selected path uses one nonzero A-orbit.  Reserve that orbit, then
        # fill all remaining factors with generic valid roots/orbits.
        child = self.child_embed(j, high, selected_tail, selected,
                                 "nonzero", danger, delta)
        if child is None or A * selected > P:
            return None
        for b in range(P - A * selected + 1):
            rem = P - A * selected - b
            if rem % A:
                continue
            if b and qrem != (1 % A):
                continue
            if b and not self.root_multiplicity_allowed(b, P, Q):
                continue
            zero_major = b > 0 and self.is_major(b, h)
            if zero_major and not self.child_generic(j, high, b, "zero", danger, delta):
                continue
            kmax = (Q - (1 if b else 0)) // A - 1
            target = rem // A
            coins = self._generic_fill_for_partition(
                target, kmax, j, high, danger, delta, P, Q, A, h, False,
                b, (selected,))
            if coins is not None:
                return {"j": j, "selected_label": "nonzero", "selected": selected,
                        "P": P, "Q": Q, "A": A, "h": str(h),
                        "delta": str(delta), "danger": danger, "b": b,
                        "orbits": [selected] + list(coins), "child": child}
        return None

    def embeds(self, Vs):
        """Vs is a dict indexed 2..s from one printed-(1)--(13) row."""
        # Lemma 5.3: top p has exactly two roots; the selected root V_s is
        # major, the complement d_s-V_s minor.  Normalize the selected top
        # coefficient to zero, so its descendant prefix initially is dangerous.
        if not (self.d[self.s] > Vs[self.s] > F(self.d[self.s], 2)):
            return None
        high = (Vs[self.s],)
        selected_tail = tuple(Vs[j] for j in range(self.s - 1, 1, -1))
        return self.embed_node(self.s - 1, high, selected_tail, True)


def row_key(n, m, Ms, V):
    return (n, m, tuple(Ms), tuple(sorted(V.items())))


def filtered_rows(nlo, nhi, Kmin, removable_prefix, passport):
    for n in range(nlo, nhi + 1):
        for m, Ms, V in BASE.census(n, Kmin=Kmin, full=True):
            C = WholeTree(n, m, Ms, removable_prefix=removable_prefix,
                          passport=passport)
            witness = C.embeds(V)
            if witness is not None:
                yield n, m, Ms, V, C, witness


def census_summary(nlo, nhi, Kmin, removable_prefix, passport=False,
                   knapsack=False):
    by_degree = {}
    groups = {}
    rows = []
    t0 = time.time()
    for n, m, Ms, V, C, witness in filtered_rows(
            nlo, nhi, Kmin, removable_prefix, passport):
        S = BASE.Skel(n, m, list(Ms), V)
        group = (m, Ms, S.V[S.s])
        groups.setdefault((n, group), []).append((S.V[2], S.q(), S.u))
        by_degree.setdefault(n, [0, set()])
        by_degree[n][0] += 1
        by_degree[n][1].add(group)
        rows.append((n, m, Ms, V, C, witness))
    out = {
        "range": [nlo, nhi], "Kmin": Kmin,
        "removable_prefix": removable_prefix,
        "passport_local_neq": passport,
        "cyclic_quotient_passport": passport,
        "V_assignments": len(rows), "groups": len(groups),
        "per_degree": {str(n): [a, len(g)] for n, (a, g) in by_degree.items()},
        "wall_seconds": time.time() - t0,
    }
    if knapsack:
        uni_alive = 0
        mixed_alive = 0
        capped = 0
        mixed_per_degree = {}
        for (n, group), items in groups.items():
            if BASE.uni_hits(items, 6, None):
                uni_alive += 1
            hit, cap = BASE.mixed_hit(items, 6, 16)
            if hit or cap:
                mixed_alive += 1
                mixed_per_degree[n] = mixed_per_degree.get(n, 0) + 1
            capped += bool(cap)
        present = sorted({n for n, _g in groups})
        baseline_present = []
        for n in range(nlo, nhi + 1):
            if next(BASE.census(n, Kmin=Kmin, full=True), None) is not None:
                baseline_present.append(n)
        baseline_set = set(baseline_present)
        tree_set = set(present)
        mixed_set = set(mixed_per_degree)
        out.update({
            "uni_N_ge_6_alive": uni_alive,
            "mixed_6_16_alive": mixed_alive,
            "mixed_capped": capped,
            "degrees_with_skeletons": present,
            "baseline_degrees_with_skeletons": baseline_present,
            "tree_empty_degrees_among_baseline": sorted(baseline_set - tree_set),
            "no_baseline_skeleton_degrees": sorted(
                set(range(nlo, nhi + 1)) - baseline_set),
            "degrees_emptied_by_mixed": [n for n in present
                                           if mixed_per_degree.get(n, 0) == 0],
            "all_degrees_empty_after_mixed": sorted(
                set(range(nlo, nhi + 1)) - mixed_set),
            "mixed_alive_per_degree": {str(n): c for n, c in mixed_per_degree.items()},
        })
    return out, rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nlo", type=int, default=48)
    ap.add_argument("--nhi", type=int, default=100)
    ap.add_argument("--Kmin", type=int, default=2)
    ap.add_argument("--zero-only", action="store_true",
                    help="Prop.5.6 danger is broken by any nonzero label")
    ap.add_argument("--knapsack", action="store_true")
    ap.add_argument("--passport", action="store_true",
                    help="also impose the local A.3 condition Q*v != P")
    ap.add_argument("--output")
    args = ap.parse_args()
    summary, rows = census_summary(args.nlo, args.nhi, args.Kmin,
                                   not args.zero_only, args.passport,
                                   args.knapsack)
    published = {
        row_key(n, m, Ms, V) for n, m, Ms, V, _lab, _p2, _p1, _err
        in BASE.MOH_TABLE
    }
    got = {row_key(n, m, Ms, V) for n, m, Ms, V, _C, _w in rows}
    summary["published_kept"] = len(got & published)
    summary["published_missing"] = [repr(x) for x in sorted(published - got)]
    summary["excess_over_published"] = len(got - published)
    summary["survivor_rows"] = [
        {"n": n, "m": m, "Ms": list(Ms), "V": V, "witness": witness}
        for n, m, Ms, V, _C, witness in rows
    ]
    rendered = json.dumps(summary, indent=2, sort_keys=True, default=str)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as fh:
            fh.write(rendered + "\n")
    print(rendered)


if __name__ == "__main__":
    main()
