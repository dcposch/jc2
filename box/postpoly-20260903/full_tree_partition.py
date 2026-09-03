#!/usr/bin/env python3
"""Dynamic program for Moh's full orbit-factor tree, not just one selected path.

At level j, write

    P = A * sum(nonzero-orbit multiplicities) + b,

where b is the multiplicity of the fixed zero factor.  The number of nonzero
orbits is bounded by floor(Q/A), since q is squarefree and contains their
distinct roots.  Every major factor recursively carries a complete lower tree;
minor factors stop.  A major all-zero path through the bottom is rejected by
Proposition 5.6.  At the bottom, every major factor satisfies (12) or (13).

The selected V path of an enumerated row must embed in one such global tree.
"""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from functools import lru_cache
from math import gcd, lcm
from pathlib import Path


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "repro"))
import moh_skeleton_full as M  # noqa: E402


def skel_key(S):
    return S.n, S.m, tuple(S.M[i] for i in range(2, S.s + 1)), S.V[S.s]


def row_key(S):
    return skel_key(S)[:3] + (tuple((i, S.V[i]) for i in range(2, S.s + 1)),)


def fraction_text(x):
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


class TreePartition:
    def __init__(self, S, polynomial_recenter=False, ode_nondegenerate=False, ode_passport=False):
        self.n, self.m, self.s = S.n, S.m, S.s
        self.M = dict(S.M)
        self.d = dict(S.d)
        self.top_V = S.V[S.s]
        self.nstar, self.mstar = S.n // S.d[2], S.m // S.d[2]
        self.polynomial_recenter = polynomial_recenter
        self.ode_passport = ode_passport
        self.ode_nondegenerate = ode_nondegenerate or ode_passport
        self._global_cache = {}
        self._embed_cache = {}
        self.stats = {"global_nodes": 0, "embed_nodes": 0, "partition_states": 0}

    def initial_path(self):
        path = [0] * (self.s + 1)
        path[self.s] = self.top_V
        return tuple(path)

    def radius(self, i, path):
        numerator = Fraction(self.n - self.M[i], 1)
        denominator = Fraction(self.n - self.M[self.s] - 1, 1)
        for j in range(i + 1, self.s + 1):
            assert path[j] > 0
            numerator *= path[j] * (self.n - self.M[j]) - self.d[j]
            denominator *= path[j] * (self.n - self.M[j - 1]) - self.d[j]
        return 1 - numerator / denominator

    def level_data(self, j, path):
        deltas = {i: self.radius(i, path) for i in range(j, self.s + 1)}
        L = 1
        for i in range(j + 1, self.s + 1):
            L = lcm(L, deltas[i].denominator)
        A = (L * deltas[j]).denominator
        pnum = path[j + 1] * self.d[j]
        qnum = path[j + 1] * (self.n - self.M[j])
        assert pnum % self.d[j + 1] == 0 and qnum % self.d[j + 1] == 0
        P = pnum // self.d[j + 1]
        Q = qnum // self.d[j + 1]
        lo = Fraction(self.d[j], self.n - self.M[j])
        return deltas[j], L, A, P, Q, lo

    def bottom(self, path):
        assert all(path[i] > 0 for i in range(2, self.s + 1))
        delta = {i: self.radius(i, path) for i in range(1, self.s + 1)}
        L = 1
        for i in range(2, self.s + 1):
            L = lcm(L, delta[i].denominator)
        A1 = (L * delta[1]).denominator
        v2 = path[2]
        by12 = self.nstar * v2 % A1 == 0 and (self.mstar * v2 - 1) % A1 == 0
        by13 = self.mstar * v2 % A1 == 0 and (self.nstar * v2 - 1) % A1 == 0
        witness = {
            "V2": v2, "delta1": fraction_text(delta[1]), "L1": L, "A1": A1,
            "condition12": by12, "condition13": by13,
        }
        return by12 or by13, witness

    def extend(self, path, j, value):
        work = list(path)
        work[j] = value
        return tuple(work)

    def fill_partition(self, total, max_coins, allowed, initial_major=False,
                       *, A=None, P=None, Q=None, b=None, prefix=()):
        """Return a nondecreasing multiset summing to total, or None."""
        allowed = tuple(sorted(allowed))  # (value, is_major)

        if self.ode_passport:
            assert A is not None and P is not None and Q is not None and b is not None
            # In the cyclic quotient z=pi^A there are exactly
            # S=(Q-1)/A nonzero q-orbits.  Unused slots are p-multiplicity 0.
            # The zero-coordinate weight is (P-Q*b)/A and an orbit of
            # p-multiplicity v has weight P-Q*v.
            # This is an external weighted-tree/passport necessary test, not
            # asserted here to be Moh's program or sufficient ODE realizability.
            assert (Q - 1) % A == 0
            slots = (Q - 1) // A
            w0_num = P - Q * b
            if w0_num % A:
                return None
            weights0 = (w0_num // A,) + tuple(P - Q * v for v in prefix)
            if len(prefix) > slots or any(w == 0 for w in weights0):
                return None
        else:
            slots = 0
            weights0 = ()

        @lru_cache(maxsize=None)
        def visit(remainder, coins_left, start, has_major, used, weight_gcd, dplus):
            self.stats["partition_states"] += 1
            if remainder == 0:
                if not has_major:
                    return None
                if self.ode_passport:
                    pad = slots - used
                    if pad < 0:
                        return None
                    final_gcd = gcd(weight_gcd, P) if pad else weight_gcd
                    final_dplus = dplus + pad * P
                    if final_gcd == 0 or final_dplus // final_gcd < slots:
                        return None
                return ()
            if coins_left == 0:
                return None
            for idx in range(start, len(allowed)):
                value, is_major = allowed[idx]
                if value > remainder:
                    break
                if self.ode_passport:
                    weight = P - Q * value
                    if weight == 0:
                        continue
                    next_gcd = gcd(weight_gcd, abs(weight))
                    next_dplus = dplus + max(weight, 0)
                else:
                    next_gcd, next_dplus = 0, 0
                tail = visit(remainder - value, coins_left - 1, idx,
                             has_major or is_major, used + 1,
                             next_gcd, next_dplus)
                if tail is not None:
                    return (value,) + tail
            return None

        initial_gcd = 0
        initial_dplus = 0
        if self.ode_passport:
            for weight in weights0:
                initial_gcd = gcd(initial_gcd, abs(weight))
                initial_dplus += max(weight, 0)
        return visit(total, max_coins, 0, initial_major, len(prefix),
                     initial_gcd, initial_dplus)

    def passport_certificate(self, A, P, Q, b, coins):
        if not self.ode_passport:
            return None
        slots = (Q - 1) // A
        padded = list(coins) + [0] * (slots - len(coins))
        weights = [(P - Q * b) // A] + [P - Q * value for value in padded]
        divisor = 0
        for weight in weights:
            divisor = gcd(divisor, abs(weight))
        dplus = sum(max(weight, 0) for weight in weights)
        return {
            "slots_S": slots, "p_multiplicities_with_zero_padding": padded,
            "weights": weights, "weight_gcd": divisor,
            "dplus": dplus, "dplus_over_gcd": dplus // divisor,
            "required_lower_bound": slots,
        }

    def child_global(self, j, path, value, is_zero, dangerous):
        newpath = self.extend(path, j, value)
        delta_j = self.radius(j, path)
        removable_nonzero = self.polynomial_recenter and delta_j.denominator == 1 and delta_j <= 0
        newdanger = dangerous and (is_zero or removable_nonzero)
        if j == 2:
            if newdanger:
                return False, {"failure": "Prop5.6 all-zero major reaches bottom"}
            return self.bottom(newpath)
        return self.global_node(j - 1, newpath, newdanger)

    def child_embed(self, j, path, value, is_zero, dangerous, required):
        newpath = self.extend(path, j, value)
        delta_j = self.radius(j, path)
        removable_nonzero = self.polynomial_recenter and delta_j.denominator == 1 and delta_j <= 0
        newdanger = dangerous and (is_zero or removable_nonzero)
        if j == 2:
            if newdanger:
                return False, {"failure": "selected all-zero major reaches bottom"}
            return self.bottom(newpath)
        return self.embed_node(j - 1, newpath, newdanger, required)

    def option_data(self, j, path, dangerous, b, total, lo, P, Q):
        """Validate the unique zero factor and every possible orbit coin."""
        # From P*q'/q-Q*p'/p=c/q at a simple q-root a carrying
        # p-multiplicity u: q'(a)=c/(P-Q*u), hence P-Q*u cannot vanish.
        if self.ode_nondegenerate and b > 0 and P - Q * b == 0:
            return None
        zero_major = b > lo
        zero_child = None
        if zero_major:
            zero_ok, zero_child = self.child_global(j, path, b, True, dangerous)
            if not zero_ok:
                return None
        allowed = []
        child_witness = {}
        for value in range(1, total + 1):
            if self.ode_nondegenerate and P - Q * value == 0:
                continue
            major = value > lo
            if not major:
                allowed.append((value, False))
                continue
            ok, witness = self.child_global(j, path, value, False, dangerous)
            if ok:
                allowed.append((value, True))
                child_witness[value] = witness
        return zero_major, zero_child, allowed, child_witness

    def global_node(self, j, path, dangerous):
        cache_key = (j, path[j + 1 :], dangerous)
        if cache_key in self._global_cache:
            return self._global_cache[cache_key]
        self.stats["global_nodes"] += 1
        delta, L, A, P, Q, lo = self.level_data(j, path)
        if self.ode_passport and Q % A != 1 % A:
            result = False, {"j": j, "A": A, "P": P, "Q": Q,
                             "failure": "passport requires A | Q-1"}
            self._global_cache[cache_key] = result
            return result
        residue = P % A
        first_b = residue
        failures = []
        for b in range(first_b, P + 1, A):
            total = (P - b) // A
            max_orbits = Q // A
            data = self.option_data(j, path, dangerous, b, total, lo, P, Q)
            if data is None:
                failures.append({"b": b, "failure": "zero-major child infeasible"})
                continue
            zero_major, zero_child, allowed, children = data
            coins = self.fill_partition(total, max_orbits, allowed,
                                        initial_major=zero_major,
                                        A=A, P=P, Q=Q, b=b)
            if coins is None:
                failures.append({"b": b, "failure": "no orbit multiset with a major factor"})
                continue
            used_major = sorted({v for v in coins if v > lo})
            witness = {
                "j": j, "dangerous_prefix": dangerous, "delta": fraction_text(delta),
                "L": L, "A": A, "P": P, "Q": Q, "major_threshold": fraction_text(lo),
                "zero_multiplicity": b, "zero_is_major": zero_major,
                "nonzero_orbit_multiplicities": list(coins), "max_nonzero_orbits": max_orbits,
                "zero_child": zero_child,
                "major_nonzero_children": {str(v): children[v] for v in used_major},
            }
            if self.ode_passport:
                witness["passport"] = self.passport_certificate(A, P, Q, b, coins)
            result = True, witness
            self._global_cache[cache_key] = result
            return result
        result = False, {"j": j, "A": A, "P": P, "Q": Q, "failures": failures}
        self._global_cache[cache_key] = result
        return result

    def embed_node(self, j, path, dangerous, required):
        required_tuple = tuple(required[i] for i in range(2, j + 1))
        cache_key = (j, path[j + 1 :], dangerous, required_tuple)
        if cache_key in self._embed_cache:
            return self._embed_cache[cache_key]
        self.stats["embed_nodes"] += 1
        delta, L, A, P, Q, lo = self.level_data(j, path)
        if self.ode_passport and Q % A != 1 % A:
            result = False, {"j": j, "selected_V": required[j], "A": A,
                             "P": P, "Q": Q,
                             "failure": "passport requires A | Q-1"}
            self._embed_cache[cache_key] = result
            return result
        vreq = required[j]
        residue = P % A
        failures = []
        for b in range(residue, P + 1, A):
            total = (P - b) // A
            max_orbits = Q // A
            data = self.option_data(j, path, dangerous, b, total, lo, P, Q)
            if data is None:
                failures.append({"b": b, "failure": "zero-major child infeasible"})
                continue
            zero_major, zero_child, allowed, children = data

            # The selected tower takes the fixed zero factor.
            if b == vreq and vreq > lo:
                selected_ok, selected_child = self.child_embed(j, path, vreq, True, dangerous, required)
                if selected_ok:
                    coins = self.fill_partition(total, max_orbits, allowed,
                                                initial_major=True,
                                                A=A, P=P, Q=Q, b=b)
                    if coins is not None:
                        witness = {
                            "j": j, "selected_mode": "zero", "selected_V": vreq,
                            "dangerous_prefix": dangerous, "delta": fraction_text(delta),
                            "L": L, "A": A, "P": P, "Q": Q,
                            "major_threshold": fraction_text(lo), "zero_multiplicity": b,
                            "nonzero_orbit_multiplicities": list(coins),
                            "selected_child": selected_child,
                        }
                        if self.ode_passport:
                            witness["passport"] = self.passport_certificate(A, P, Q, b, coins)
                        result = True, witness
                        self._embed_cache[cache_key] = result
                        return result

            # The selected tower takes one member of a nonzero A-orbit.
            allowed_values = {value for value, _ in allowed}
            if vreq in allowed_values and vreq > lo and total >= vreq and max_orbits >= 1:
                selected_ok, selected_child = self.child_embed(j, path, vreq, False, dangerous, required)
                if selected_ok:
                    rest = self.fill_partition(total - vreq, max_orbits - 1,
                                               allowed, initial_major=True,
                                               A=A, P=P, Q=Q, b=b,
                                               prefix=(vreq,))
                    if rest is not None:
                        coins = tuple(sorted((vreq,) + rest))
                        witness = {
                            "j": j, "selected_mode": "nonzero", "selected_V": vreq,
                            "dangerous_prefix": dangerous, "delta": fraction_text(delta),
                            "L": L, "A": A, "P": P, "Q": Q,
                            "major_threshold": fraction_text(lo), "zero_multiplicity": b,
                            "nonzero_orbit_multiplicities": list(coins),
                            "selected_child": selected_child,
                        }
                        if self.ode_passport:
                            witness["passport"] = self.passport_certificate(A, P, Q, b, coins)
                        result = True, witness
                        self._embed_cache[cache_key] = result
                        return result
            failures.append({"b": b, "failure": "selected V path not embeddable"})
        result = False, {"j": j, "selected_V": vreq, "A": A, "P": P, "Q": Q, "failures": failures}
        self._embed_cache[cache_key] = result
        return result

    def global_feasible(self):
        return self.global_node(self.s - 1, self.initial_path(), True)

    def embeds(self, S):
        required = {i: S.V[i] for i in range(2, S.s)}
        return self.embed_node(self.s - 1, self.initial_path(), True, required)


_EVALUATORS = {}


def evaluator(S, polynomial_recenter=False, ode_nondegenerate=False, ode_passport=False):
    key = (polynomial_recenter, ode_nondegenerate, ode_passport) + skel_key(S)
    if key not in _EVALUATORS:
        _EVALUATORS[key] = TreePartition(S, polynomial_recenter=polynomial_recenter,
                                         ode_nondegenerate=ode_nondegenerate,
                                         ode_passport=ode_passport)
    return _EVALUATORS[key]


def full_tree_ok(S):
    return evaluator(S).embeds(S)[0]


def full_tree_polynomial_ok(S):
    return evaluator(S, polynomial_recenter=True).embeds(S)[0]


def full_tree_ode_ok(S):
    return evaluator(S, ode_nondegenerate=True).embeds(S)[0]


def full_tree_passport_ok(S):
    return evaluator(S, ode_passport=True).embeds(S)[0]


def full_tree_polynomial_ode_ok(S):
    return evaluator(S, polynomial_recenter=True, ode_nondegenerate=True).embeds(S)[0]


def full_tree_polynomial_passport_ok(S):
    return evaluator(S, polynomial_recenter=True, ode_passport=True).embeds(S)[0]


def audit_n100(polynomial_recenter=False, ode_nondegenerate=False, ode_passport=False):
    rows = [
        M.Skel(n, m, list(Ms), V)
        for n in range(4, 101)
        for m, Ms, V in M.census(n, Kmin=2, full=True)
    ]
    printed = {
        (n, m, tuple(Ms), tuple(sorted(Vs.items())))
        for n, m, Ms, Vs, *_ in M.MOH_TABLE
    }
    audit = []
    survivors = set()
    for S in rows:
        E = evaluator(S, polynomial_recenter=polynomial_recenter,
                      ode_nondegenerate=ode_nondegenerate,
                      ode_passport=ode_passport)
        group_ok, group_witness = E.global_feasible()
        ok, witness = E.embeds(S)
        key = row_key(S)
        if ok:
            survivors.add(key)
        audit.append({
            "row_key": repr(key), "group_feasible": group_ok, "selected_path_embeds": ok,
            "is_printed": key in printed, "witness": witness if ok else None,
            "failure_certificate": None if ok else witness,
        })
    exact = survivors == printed
    tag = "full-tree" + ("-polynomial" if polynomial_recenter else "")
    tag += "-passport" if ode_passport else ("-ode" if ode_nondegenerate else "")
    payload = {
        "algorithm": "exact finite DP over b and bounded nonzero-orbit multisets; every major child recursively checked",
        "polynomial_recenter_danger": polynomial_recenter,
        "ode_weight_nondegeneracy": ode_nondegenerate,
        "ode_passport": ode_passport,
        "input_rows": len(rows), "survivors": len(survivors), "rejected_no_partition": len(rows) - len(survivors),
        "survivors_equal_six_printed": exact,
        "excess_survivors": len(survivors - printed),
        "printed_rows_killed": len(printed - survivors),
        "rows": audit,
    }
    (HERE / f"{tag}-n100-audit.json").write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    witnesses = {item["row_key"]: item["witness"] for item in audit if item["is_printed"]}
    (HERE / f"{tag}-printed-witnesses.json").write_text(json.dumps(witnesses, indent=2, sort_keys=True) + "\n")
    excess_witnesses = {item["row_key"]: item["witness"] for item in audit if item["selected_path_embeds"] and not item["is_printed"]}
    (HERE / f"{tag}-excess-witnesses.json").write_text(json.dumps(excess_witnesses, indent=2, sort_keys=True) + "\n")
    label = "FULL-TREE" + ("-POLYNOMIAL" if polynomial_recenter else "")
    label += "-PASSPORT" if ode_passport else ("-ODE" if ode_nondegenerate else "-PARTITION")
    print(f"{label}: {len(rows)} -> {len(survivors)} rows; rejected {len(rows)-len(survivors)}; exact printed set={exact}; excess={len(survivors-printed)}; printed killed={len(printed-survivors)}")


if __name__ == "__main__":
    audit_n100(False)
    audit_n100(False, True)
    audit_n100(False, False, True)
    audit_n100(True)
    audit_n100(True, True)
    audit_n100(True, False, True)
