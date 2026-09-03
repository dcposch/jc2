#!/usr/bin/env python3
"""Same-tree Xu screen over the frozen C_FULL_TREE_POLYNOMIAL_ODE census.

The driver keeps the charged finite full-tree model:
  * the Moh row's selected V-path must embed in the tree;
  * every major child recursively carries a lower full tree;
  * minor packets are terminal packets of the finite model;
  * polynomial recentering danger and ODE nondegeneracy are enabled.

For each row it computes:
  (a) the sharpened independent-extrema policy, reproducing the prior 48/33;
  (b) the same-tree Corollary 5.3 test, max_T (IM(T)-Im(T));
  (c) the same-tree all-Xu test.  On one fixed tree, Xu's equation (4.3)
      gives I + IM = deg_y f + weighted_minor + (Im - 1), so the Theorem
      4.7(i) slack deg_y f - 1 + weighted_minor - I equals IM - Im.
      Thus the exact I formula is checked as an equality but is not an
      independent inequality beyond same-tree Corollary 5.3.

All arithmetic is exact Fraction arithmetic.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path


HERE = Path(__file__).resolve().parent
INPUTS = Path(os.environ.get("JC2_LANE_INPUTS", "/tmp/jc2-lane.XDZrUG/inputs"))
sys.path.insert(0, str(INPUTS))

import full_tree_partition as FT  # noqa: E402
import moh_skeleton_full as M  # noqa: E402


def frac_text(x):
    if x is None:
        return None
    if isinstance(x, F):
        return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"
    return str(x)


def parse_frac(text):
    return F(text)


def m_list(S):
    return [S.M[i] for i in range(2, S.s + 1)]


def v_map(S):
    return {str(i): S.V[i] for i in range(2, S.s + 1)}


def row_key(S):
    return (
        S.n,
        S.m,
        tuple(S.M[i] for i in range(2, S.s + 1)),
        tuple((i, S.V[i]) for i in range(2, S.s + 1)),
    )


def group_key(S):
    return (S.n, S.m, tuple(S.M[i] for i in range(2, S.s + 1)), S.V[S.s])


def group_key_text(S):
    return repr(group_key(S))


def u_s_of(S) -> int:
    return S.d[S.s] - S.V[S.s]


def positive_part(x: F) -> F:
    return x if x > 0 else F(0)


def def51(n, Mdict, ddict, Vdict, s, i):
    num = F(n - Mdict[i])
    den = F(n - Mdict[s] - 1)
    if den == 0:
        return None
    for j in range(i + 1, s + 1):
        num *= Vdict[j] * (n - Mdict[j]) - ddict[j]
        den *= Vdict[j] * (n - Mdict[j - 1]) - ddict[j]
        if den == 0:
            return None
    return 1 - num / den


def descend(S):
    us = u_s_of(S)
    ds = S.d[S.s]
    Vs = S.V[S.s]
    k = Vs - us - 1
    n2, m2 = S.n // ds, S.m // ds
    s2 = S.s - 1
    M2 = {i: S.M[i] // ds for i in range(1, s2 + 1)}
    d2 = {i: S.d[i] // ds for i in range(1, s2 + 2)}
    V2 = {i: S.V[i] for i in range(2, s2 + 1)}
    V2[s2 + 1] = d2[s2 + 1]
    return {"n": n2, "m": m2, "s": s2, "M": M2, "d": d2, "V": V2, "k": k}


def truncate_jacobian(D):
    n, s = D["n"], D["s"]
    Mdict, ddict, Vdict = dict(D["M"]), dict(D["d"]), dict(D["V"])
    dropped = 0
    while s >= 1 and Mdict.get(s) == n - 1:
        dropped += 1
        s -= 1
        Mdict.pop(s + 1, None)
        Vdict.pop(s + 1, None)
        if (s + 1) in ddict and s >= 1:
            Vdict[s + 1] = ddict[s + 1]
    D2 = dict(D)
    D2.update({"s": s, "M": Mdict, "d": ddict, "V": Vdict, "dropped": dropped})
    return D2


def phi_on(D):
    n, Mdict, ddict, Vdict, s, k = D["n"], D["M"], D["d"], D["V"], D["s"], D["k"]
    if s < 1 or n - Mdict[s] - 1 == 0:
        return None
    out = []
    for i in range(1, s + 1):
        raw = def51(n, Mdict, ddict, Vdict, s, i)
        if raw is None:
            return None
        out.append((k + 1) * raw)
    return out


def phi_eff(S):
    us = u_s_of(S)
    if us != 1:
        return {"status": "NOT-US1", "u_s": us, "s_eff": None, "two_point": None}
    vals = [S.n, S.m] + [S.M[i] for i in range(1, S.s)] + [S.d[i] for i in range(1, S.s + 1)]
    ds = S.d[S.s]
    if any(x % ds != 0 for x in vals):
        return {"status": "NOT-INTEGRAL", "u_s": us, "s_eff": None, "two_point": None}
    Dt = truncate_jacobian(descend(S))
    ph = phi_on(Dt)
    d2 = ph[1] if ph is not None and Dt["s"] >= 2 else None
    return {
        "status": "OK",
        "u_s": us,
        "s_eff": Dt["s"],
        "dropped": Dt["dropped"],
        "delta": None if ph is None else [frac_text(x) for x in ph],
        "delta2": frac_text(d2),
        "two_point": d2 == F(-1),
    }


@lru_cache(maxsize=None)
def partitions(total: int, max_coins: int, start: int = 1):
    """Nondecreasing positive integer multisets summing to total."""
    if total == 0:
        return ((),)
    if max_coins == 0:
        return ()
    out = []
    for v in range(start, total + 1):
        for rest in partitions(total - v, max_coins - 1, v):
            out.append((v,) + rest)
    return tuple(out)


def pareto(points):
    """Keep only pairs not dominated in both lower-bound slacks."""
    if not points:
        return ()
    best_by_a = {}
    for a, b in points:
        old = best_by_a.get(a)
        if old is None or b > old:
            best_by_a[a] = b
    out = []
    best_b = None
    for a in sorted(best_by_a.keys(), reverse=True):
        b = best_by_a[a]
        if best_b is None or b > best_b:
            out.append((a, b))
            best_b = b
    return tuple(out)


def combine_frontiers(frontiers):
    cur = ((F(0), F(0)),)
    for frontier in frontiers:
        nxt = []
        for a0, b0 in cur:
            for a1, b1 in frontier:
                nxt.append((a0 + a1, b0 + b1))
        cur = pareto(nxt)
        if not cur:
            return ()
    return cur


def scale_frontier(frontier, k: int):
    if k == 1:
        return frontier
    return tuple((k * a, k * b) for a, b in frontier)


@dataclass(frozen=True)
class PrincipalMetrics:
    roots: F
    delta: F
    im: F
    weighted: F
    intersection: F


class SameTree:
    """Exact metric DP over the finite operative tree model."""

    def __init__(self, S):
        self.S = S
        self.E = FT.evaluator(S, polynomial_recenter=True, ode_nondegenerate=True)
        self.required = {i: S.V[i] for i in range(2, S.s)}
        self.stats = {
            "pair_global_nodes": 0,
            "pair_embed_nodes": 0,
            "scalar_global_nodes": 0,
            "scalar_embed_nodes": 0,
            "plans": 0,
            "max_frontier": 0,
            "bottom_mismatch": 0,
        }

    def principal(self) -> PrincipalMetrics:
        S = self.S
        us = u_s_of(S)
        roots = F(us * S.m, S.d[S.s])
        delta = F(S.V[S.s], us)
        im = positive_part(delta - 1)
        weighted = (roots - 1) * im if roots >= 1 else F(0)
        intersection = roots * delta
        return PrincipalMetrics(roots, delta, im, weighted, intersection)

    def node_root_count(self, j, path):
        return F(path[j + 1] * self.S.m, self.S.d[j + 1])

    def child_root_count(self, j, value):
        return F(value * self.S.m, self.S.d[j])

    def minor_delta(self, j, path, value, Sout_c):
        by_distance = Sout_c / self.child_root_count(j, value)
        delta, _L, _A, _P, _Q, lo = self.E.level_data(j, path)
        by_formula = delta + lo * (1 - delta) / value
        if by_distance != by_formula:
            raise AssertionError(
                f"minor delta mismatch {self.S.n},{self.S.m}, j={j}, v={value}: "
                f"{by_distance} != {by_formula}"
            )
        return by_distance

    def terminal_minor_pair(self, j, path, value, orbit, Sout_c):
        roots = self.child_root_count(j, value)
        delta = self.minor_delta(j, path, value, Sout_c)
        im = positive_part(delta - 1)
        weighted = (roots - 1) * im if im > 0 else F(0)
        intersection = roots * delta
        return ((-orbit * im, orbit * (weighted - intersection)),)

    def terminal_minor_scalar(self, j, path, value, orbit, Sout_c, mode):
        if mode == "IM_MAX":
            return F(0)
        delta = self.minor_delta(j, path, value, Sout_c)
        im = orbit * positive_part(delta - 1)
        if mode == "DIFF_MAX":
            return -im
        return im

    def terminal_major_pair(self, j, path, value, orbit, Sout_c):
        newpath = self.E.extend(path, j, value)
        ok, _wit = self.E.bottom(newpath)
        if not ok:
            return ()
        roots = self.child_root_count(j, value)
        delta1 = self.E.radius(1, newpath)
        lambda_neg = F(self.S.n, self.S.m + self.S.n) * (1 - delta1)
        IM = roots * lambda_neg
        S_by_leaf = 1 - lambda_neg
        S_by_dist = Sout_c - (roots - 1) * delta1
        if S_by_leaf != S_by_dist:
            self.stats["bottom_mismatch"] += 1
            raise AssertionError(
                f"bottom S mismatch {self.S.n},{self.S.m}, v={value}: "
                f"{S_by_leaf} != {S_by_dist}"
            )
        intersection = roots * S_by_leaf
        return ((orbit * IM, -orbit * intersection),)

    def terminal_major_scalar(self, j, path, value, orbit, _Sout_c, mode):
        newpath = self.E.extend(path, j, value)
        ok, _wit = self.E.bottom(newpath)
        if not ok:
            return None
        if mode == "IM_MIN":
            return F(0)
        roots = self.child_root_count(j, value)
        delta1 = self.E.radius(1, newpath)
        return orbit * roots * F(self.S.n, self.S.m + self.S.n) * (1 - delta1)

    def child_newdanger(self, j, path, is_zero, dangerous):
        delta_j = self.E.radius(j, path)
        removable_nonzero = delta_j.denominator == 1 and delta_j <= 0
        return dangerous and (is_zero or removable_nonzero)

    @lru_cache(maxsize=None)
    def plans(self, j, path, embed):
        """Return finite split plans at a node.

        A plan is (children, selected_index), with selected_index None for
        global plans.  Each child is (value, orbit_size, is_zero, is_major).
        """
        self.stats["plans"] += 1
        delta, _L, A, P, Q, lo = self.E.level_data(j, path)
        residue = P % A
        out = []
        for b in range(residue, P + 1, A):
            if b > 0 and P - Q * b == 0:
                continue
            total = (P - b) // A
            max_orbits = Q // A
            for coins in partitions(total, max_orbits):
                if any(P - Q * v == 0 for v in coins):
                    continue
                children = []
                if b > 0:
                    children.append((b, 1, True, b > lo))
                for v in coins:
                    children.append((v, A, False, v > lo))
                if not any(child[3] for child in children):
                    continue
                if not embed:
                    out.append((tuple(children), None))
                    continue
                vreq = self.required[j]
                selected = []
                if children and children[0][2] and children[0][0] == vreq and children[0][3]:
                    selected.append(0)
                first_nonzero = None
                for idx, child in enumerate(children):
                    value, _orbit, is_zero, is_major = child
                    if not is_zero and is_major and value == vreq:
                        first_nonzero = idx
                        break
                if first_nonzero is not None:
                    selected.append(first_nonzero)
                for idx in selected:
                    out.append((tuple(children), idx))
        return tuple(out)

    def child_pair(self, j, path, dangerous, Sout_c, child, embed_child):
        value, orbit, is_zero, is_major = child
        if not is_major:
            return self.terminal_minor_pair(j, path, value, orbit, Sout_c)
        newdanger = self.child_newdanger(j, path, is_zero, dangerous)
        if j == 2:
            if newdanger:
                return ()
            return self.terminal_major_pair(j, path, value, orbit, Sout_c)
        newpath = self.E.extend(path, j, value)
        if embed_child:
            return scale_frontier(self.embed_pair(j - 1, newpath, newdanger, Sout_c), orbit)
        return scale_frontier(self.global_pair(j - 1, newpath, newdanger, Sout_c), orbit)

    def child_scalar(self, j, path, dangerous, Sout_c, child, embed_child, mode):
        value, orbit, is_zero, is_major = child
        if not is_major:
            return self.terminal_minor_scalar(j, path, value, orbit, Sout_c, mode)
        newdanger = self.child_newdanger(j, path, is_zero, dangerous)
        if j == 2:
            if newdanger:
                return None
            return self.terminal_major_scalar(j, path, value, orbit, Sout_c, mode)
        newpath = self.E.extend(path, j, value)
        if embed_child:
            score = self.embed_scalar(j - 1, newpath, newdanger, Sout_c, mode)
        else:
            score = self.global_scalar(j - 1, newpath, newdanger, Sout_c, mode)
        if score is None:
            return None
        return orbit * score

    def scalar_child_by_value(self, j, path, dangerous, Sout, value, orbit, is_zero, embed_child, mode):
        delta, _L, _A, _P, _Q, lo = self.E.level_data(j, path)
        Nj = self.node_root_count(j, path)
        Nc = self.child_root_count(j, value)
        Sout_c = Sout - (Nj - Nc) * delta
        child = (value, orbit, is_zero, value > lo)
        return self.child_scalar(j, path, dangerous, Sout_c, child, embed_child, mode)

    @staticmethod
    def multiset_scalar(total, max_coins, options, initial_major, mode):
        opt = tuple(sorted(options, key=lambda item: item[0]))

        @lru_cache(maxsize=None)
        def visit(remainder, coins_left, start, has_major):
            if remainder == 0:
                return F(0) if has_major else None
            if coins_left == 0:
                return None
            best = None
            for idx in range(start, len(opt)):
                value, is_major, score = opt[idx]
                if value > remainder:
                    break
                tail = visit(remainder - value, coins_left - 1, idx, has_major or is_major)
                if tail is None:
                    continue
                candidate = score + tail
                if best is None:
                    best = candidate
                elif mode in ("IM_MAX", "DIFF_MAX") and candidate > best:
                    best = candidate
                elif mode == "IM_MIN" and candidate < best:
                    best = candidate
            return best

        return visit(total, max_coins, 0, initial_major)

    def scalar_options(self, j, path, dangerous, Sout, total, A, P, Q, mode):
        out = []
        for value in range(1, total + 1):
            if P - Q * value == 0:
                continue
            score = self.scalar_child_by_value(
                j, path, dangerous, Sout, value, A, False, False, mode
            )
            if score is None:
                continue
            delta, _L, _A, _P, _Q, lo = self.E.level_data(j, path)
            out.append((value, value > lo, score))
        return out

    def option_scalar(self, j, path, dangerous, Sout, b, selected_mode, mode):
        delta, _L, A, P, Q, lo = self.E.level_data(j, path)
        if b > 0 and P - Q * b == 0:
            return None
        total = (P - b) // A
        max_orbits = Q // A
        zero_score = F(0)
        zero_major = b > lo if b > 0 else False
        if b > 0:
            if zero_major:
                zero_score = self.scalar_child_by_value(
                    j, path, dangerous, Sout, b, 1, True, selected_mode == "zero", mode
                )
                if zero_score is None:
                    return None
            else:
                if selected_mode == "zero":
                    return None
                zero_score = self.scalar_child_by_value(
                    j, path, dangerous, Sout, b, 1, True, False, mode
                )
                if zero_score is None:
                    return None

        rest_total = total
        rest_max = max_orbits
        initial_major = zero_major
        forced_score = F(0)
        if selected_mode == "zero":
            vreq = self.required[j]
            if b != vreq or not zero_major:
                return None
            initial_major = True
        elif selected_mode == "nonzero":
            vreq = self.required[j]
            if not (vreq > lo and rest_total >= vreq and rest_max >= 1):
                return None
            if P - Q * vreq == 0:
                return None
            forced_score = self.scalar_child_by_value(
                j, path, dangerous, Sout, vreq, A, False, True, mode
            )
            if forced_score is None:
                return None
            rest_total -= vreq
            rest_max -= 1
            initial_major = True

        options = self.scalar_options(j, path, dangerous, Sout, total, A, P, Q, mode)
        rest = self.multiset_scalar(rest_total, rest_max, options, initial_major, mode)
        if rest is None:
            return None
        return zero_score + forced_score + rest

    @lru_cache(maxsize=None)
    def global_pair(self, j, path, dangerous, Sout):
        self.stats["pair_global_nodes"] += 1
        delta, _L, _A, _P, _Q, _lo = self.E.level_data(j, path)
        Nj = self.node_root_count(j, path)
        points = []
        for children, selected in self.plans(j, path, False):
            assert selected is None
            frontiers = []
            feasible = True
            for child in children:
                value, _orbit, _is_zero, _is_major = child
                Nc = self.child_root_count(j, value)
                Sout_c = Sout - (Nj - Nc) * delta
                frontier = self.child_pair(j, path, dangerous, Sout_c, child, False)
                if not frontier:
                    feasible = False
                    break
                frontiers.append(frontier)
            if feasible:
                points.extend(combine_frontiers(frontiers))
        result = pareto(points)
        self.stats["max_frontier"] = max(self.stats["max_frontier"], len(result))
        return result

    @lru_cache(maxsize=None)
    def embed_pair(self, j, path, dangerous, Sout):
        self.stats["pair_embed_nodes"] += 1
        delta, _L, _A, _P, _Q, _lo = self.E.level_data(j, path)
        Nj = self.node_root_count(j, path)
        points = []
        for children, selected in self.plans(j, path, True):
            assert selected is not None
            frontiers = []
            feasible = True
            for idx, child in enumerate(children):
                value, _orbit, _is_zero, _is_major = child
                Nc = self.child_root_count(j, value)
                Sout_c = Sout - (Nj - Nc) * delta
                frontier = self.child_pair(j, path, dangerous, Sout_c, child, idx == selected)
                if not frontier:
                    feasible = False
                    break
                frontiers.append(frontier)
            if feasible:
                points.extend(combine_frontiers(frontiers))
        result = pareto(points)
        self.stats["max_frontier"] = max(self.stats["max_frontier"], len(result))
        return result

    @lru_cache(maxsize=None)
    def global_scalar(self, j, path, dangerous, Sout, mode):
        self.stats["scalar_global_nodes"] += 1
        delta, _L, _A, _P, _Q, _lo = self.E.level_data(j, path)
        _ = delta
        best = None
        _delta, _L, A, P, _Q, _lo = self.E.level_data(j, path)
        residue = P % A
        for b in range(residue, P + 1, A):
            total = self.option_scalar(j, path, dangerous, Sout, b, None, mode)
            if total is None:
                continue
            if best is None:
                best = total
            elif mode in ("IM_MAX", "DIFF_MAX") and total > best:
                best = total
            elif mode == "IM_MIN" and total < best:
                best = total
        return best

    @lru_cache(maxsize=None)
    def embed_scalar(self, j, path, dangerous, Sout, mode):
        self.stats["scalar_embed_nodes"] += 1
        delta, _L, _A, _P, _Q, _lo = self.E.level_data(j, path)
        _ = delta
        best = None
        _delta, _L, A, P, _Q, _lo = self.E.level_data(j, path)
        residue = P % A
        for b in range(residue, P + 1, A):
            for selected_mode in ("zero", "nonzero"):
                total = self.option_scalar(j, path, dangerous, Sout, b, selected_mode, mode)
                if total is None:
                    continue
                if best is None:
                    best = total
                elif mode in ("IM_MAX", "DIFF_MAX") and total > best:
                    best = total
                elif mode == "IM_MIN" and total < best:
                    best = total
        return best

    def evaluate(self):
        S = self.S
        path = self.E.initial_path()
        Sout_top = F(u_s_of(S) * S.m, S.d[S.s])
        pr = self.principal()

        im_max = self.embed_scalar(S.s - 1, path, True, Sout_top, "IM_MAX")
        imn = self.embed_scalar(S.s - 1, path, True, Sout_top, "IM_MIN")
        diff = self.embed_scalar(S.s - 1, path, True, Sout_top, "DIFF_MAX")
        if im_max is None or imn is None or diff is None:
            return {"tree_status": "NO-OPERATIVE-TREE", "stats": dict(self.stats)}

        independent_Im = F(1) + pr.im + imn
        max_c53 = diff - (F(1) + pr.im)
        # Xu p.6 equation (4.3), Theorem 5.1, and the definition of Im give
        # deg_y f - 1 + weighted_minor - I(f_xi,f_y) = IM - Im on the same tree.
        max_t47i = max_c53
        any_c53 = max_c53 >= 0
        any_all = any_c53

        return {
            "tree_status": "OK",
            "principal_roots": pr.roots,
            "principal_delta": pr.delta,
            "principal_im": pr.im,
            "principal_weighted": pr.weighted,
            "principal_intersection": pr.intersection,
            "independent_IM_max": im_max,
            "independent_tree_minor_min": imn,
            "independent_Im_min": independent_Im,
            "independent_ok": im_max >= independent_Im,
            "same_tree_frontier_size": None,
            "same_tree_max_c53_slack": max_c53,
            "same_tree_max_t47i_slack": max_t47i,
            "same_tree_best_balanced_c53_slack": max_c53,
            "same_tree_best_balanced_t47i_slack": max_t47i,
            "same_tree_exact_I_constraint": "redundant-with-Cor5.3-by-Xu-4.3",
            "same_tree_c53_ok": any_c53,
            "same_tree_all_ok": any_all,
            "stats": dict(self.stats),
        }


def manual_j2_split(S, *, zero: int, nonzero_values: list[int]):
    """Evaluate Xu's printed one-level split choices with the same metric formulas."""
    E = FT.evaluator(S, polynomial_recenter=True, ode_nondegenerate=True)
    path = list(E.initial_path())
    path[S.s] = S.V[S.s]
    path = tuple(path)
    if S.s != 3:
        raise ValueError("manual replay expects s=3")
    D = SameTree(S)
    delta, _L, A, P, _Q, _lo = E.level_data(2, path)
    if P != A * sum(nonzero_values) + zero:
        raise ValueError("manual split does not match P=A*sum+b")

    pr = D.principal()
    IM = F(0)
    Im = F(1) + pr.im
    I = pr.intersection
    W = pr.weighted
    parts = []
    Nj = D.node_root_count(2, path)

    children = []
    if zero:
        children.append((zero, 1, True))
    for value in nonzero_values:
        children.append((value, A, False))

    for value, orbit, is_zero in children:
        Nc = D.child_root_count(2, value)
        Sout_c = pr.roots - (Nj - Nc) * delta
        lo = F(S.d[2], S.n - S.M[2])
        if value > lo:
            newpath = E.extend(path, 2, value)
            ok, _wit = E.bottom(newpath)
            if not ok:
                raise ValueError("manual major child fails bottom")
            delta1 = E.radius(1, newpath)
            lambda_neg = F(S.n, S.m + S.n) * (1 - delta1)
            major_IM = Nc * lambda_neg
            major_S = 1 - lambda_neg
            major_I = Nc * major_S
            IM += orbit * major_IM
            I += orbit * major_I
            parts.append({
                "kind": "zero-major" if is_zero else "nonzero-major",
                "value": value,
                "orbit": orbit,
                "roots": frac_text(Nc),
                "delta1": frac_text(delta1),
                "IM": frac_text(orbit * major_IM),
                "I": frac_text(orbit * major_I),
            })
        else:
            minor_delta = D.minor_delta(2, path, value, Sout_c)
            im = positive_part(minor_delta - 1)
            weighted = (Nc - 1) * im if im > 0 else F(0)
            intersection = Nc * minor_delta
            Im += orbit * im
            W += orbit * weighted
            I += orbit * intersection
            parts.append({
                "kind": "zero-minor" if is_zero else "nonzero-minor",
                "value": value,
                "orbit": orbit,
                "roots": frac_text(Nc),
                "delta": frac_text(minor_delta),
                "Im": frac_text(orbit * im),
                "weighted": frac_text(orbit * weighted),
                "I": frac_text(orbit * intersection),
            })
    t47_slack = F(S.m - 1) + W - I
    return {
        "n": S.n,
        "m": S.m,
        "M": m_list(S),
        "V": v_map(S),
        "zero": zero,
        "nonzero_values": nonzero_values,
        "A": A,
        "IM": IM,
        "Im": Im,
        "I": I,
        "weighted_minor": W,
        "cor53_slack": IM - Im,
        "t47i_slack": t47_slack,
        "excluded_by_cor53": IM < Im,
        "excluded_by_all": IM < Im or t47_slack < 0,
        "principal": {
            "roots": frac_text(pr.roots),
            "delta": frac_text(pr.delta),
            "Im": frac_text(pr.im),
            "weighted": frac_text(pr.weighted),
            "I": frac_text(pr.intersection),
        },
        "parts": parts,
    }


def jsonable(obj):
    if isinstance(obj, F):
        return frac_text(obj)
    if isinstance(obj, dict):
        return {str(k): jsonable(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [jsonable(v) for v in obj]
    return obj


def stats(rows, ok_field):
    by_group = defaultdict(list)
    for row in rows:
        by_group[row["group_key"]].append(row)
    killed_rows = [row for row in rows if not row[ok_field]]
    killed_groups = {
        key: items for key, items in by_group.items()
        if all(not row[ok_field] for row in items)
    }
    touched_groups = {
        key: items for key, items in by_group.items()
        if any(not row[ok_field] for row in items)
    }
    return {
        "rows": len(rows),
        "groups": len(by_group),
        "killed_rows": len(killed_rows),
        "killed_groups": len(killed_groups),
        "touched_groups": len(touched_groups),
    }


def killed_groups(rows, ok_field):
    by_group = defaultdict(list)
    for row in rows:
        by_group[row["group_key"]].append(row)
    return {
        key: items for key, items in by_group.items()
        if all(not row[ok_field] for row in items)
    }


def compact(row):
    keys = (
        "n", "m", "M", "V", "V_s", "u_s",
        "independent_IM_max", "independent_Im_min",
        "same_tree_max_c53_slack", "same_tree_max_t47i_slack",
        "same_tree_best_balanced_c53_slack", "same_tree_best_balanced_t47i_slack",
        "independent_ok", "same_tree_c53_ok", "same_tree_all_ok",
        "all_killer",
    )
    return {key: row[key] for key in keys if key in row}


def unique_row(rows, predicate, label):
    matches = [row for row in rows if predicate(row)]
    if len(matches) != 1:
        raise AssertionError(f"{label}: expected one row, got {len(matches)}")
    return matches[0]


def run(dlo, dhi):
    t0 = time.perf_counter()
    failures = []
    rows_all = []
    for n in range(dlo, dhi + 1):
        for m, Ms, V in M.census(n, Kmin=16, full=True):
            S = M.Skel(n, m, list(Ms), V)
            if FT.full_tree_polynomial_ode_ok(S):
                rows_all.append(S)
    if len(rows_all) != 1420 or len({group_key(S) for S in rows_all}) != 686:
        failures.append(
            f"operative census expected 1420/686, got {len(rows_all)}/"
            f"{len({group_key(S) for S in rows_all})}"
        )

    calibration = {
        "75_50_split_i": manual_j2_split(
            M.Skel(75, 50, [55, 73], {2: 2, 3: 4}),
            zero=0,
            nonzero_values=[2, 2],
        ),
        "75_50_split_ii": manual_j2_split(
            M.Skel(75, 50, [55, 73], {2: 2, 3: 4}),
            zero=0,
            nonzero_values=[2, 1, 1],
        ),
        "84_56_M2_64_V2_2": manual_j2_split(
            M.Skel(84, 56, [64, 82], {2: 2, 3: 3}),
            zero=0,
            nonzero_values=[2, 1],
        ),
        "84_56_M2_72_V2_5": manual_j2_split(
            M.Skel(84, 56, [72, 82], {2: 5, 3: 3}),
            zero=1,
            nonzero_values=[5],
        ),
    }
    expected_cal = {
        "75_50_split_i": ("8", "4", False),
        "75_50_split_ii": ("4", "6", True),
        "84_56_M2_64_V2_2": ("4", "5", True),
        "84_56_M2_72_V2_5": ("10", "4", False),
    }
    for label, (IM, Im, excluded) in expected_cal.items():
        rec = calibration[label]
        if (frac_text(rec["IM"]), frac_text(rec["Im"]), rec["excluded_by_cor53"]) != (IM, Im, excluded):
            failures.append(f"calibration {label} mismatch")

    row_results = []
    for idx, S in enumerate(rows_all, 1):
        D = SameTree(S)
        ev = D.evaluate()
        rec = {
            "n": S.n,
            "m": S.m,
            "s": S.s,
            "M": m_list(S),
            "V": v_map(S),
            "V_s": S.V[S.s],
            "u_s": u_s_of(S),
            "row_key": repr(row_key(S)),
            "group_key": group_key_text(S),
            "phi_eff": phi_eff(S),
        }
        rec.update(jsonable(ev))
        if rec["tree_status"] == "OK":
            if not rec["same_tree_c53_ok"]:
                rec["all_killer"] = "Corollary 5.3 / Theorem 4.7(ii)"
            elif not rec["same_tree_all_ok"]:
                rec["all_killer"] = "Theorem 3.4 + Theorem 4.7(i)"
            else:
                rec["all_killer"] = "survives"
        else:
            rec["independent_ok"] = False
            rec["same_tree_c53_ok"] = False
            rec["same_tree_all_ok"] = False
            rec["all_killer"] = "NO-OPERATIVE-TREE"
        row_results.append(rec)
        if idx % 100 == 0 or idx == len(rows_all):
            print(
                f"processed {idx}/{len(rows_all)} rows; "
                f"same-tree all killed rows={sum(not r['same_tree_all_ok'] for r in row_results)}",
                flush=True,
            )

    policies = {
        "independent_sharp": stats(row_results, "independent_ok"),
        "same_tree_cor53": stats(row_results, "same_tree_c53_ok"),
        "same_tree_all": stats(row_results, "same_tree_all_ok"),
    }
    if policies["independent_sharp"]["killed_rows"] != 48 or policies["independent_sharp"]["killed_groups"] != 33:
        failures.append(f"independent sharp did not reproduce 48/33: {policies['independent_sharp']}")

    strata = {}
    for label, predicate in (
        ("u_s=1", lambda r: r["u_s"] == 1),
        ("u_s>1", lambda r: r["u_s"] > 1),
    ):
        sub = [r for r in row_results if predicate(r)]
        strata[label] = {
            "independent_sharp": stats(sub, "independent_ok"),
            "same_tree_cor53": stats(sub, "same_tree_c53_ok"),
            "same_tree_all": stats(sub, "same_tree_all_ok"),
        }

    kg_ind = killed_groups(row_results, "independent_ok")
    kg_c53 = killed_groups(row_results, "same_tree_c53_ok")
    kg_all = killed_groups(row_results, "same_tree_all_ok")

    def group_summary(items):
        first = items[0]
        return {
            "n": first["n"],
            "m": first["m"],
            "M": first["M"],
            "V_s": first["V_s"],
            "u_s": first["u_s"],
            "s": first["s"],
            "rows_in_group": len(items),
            "killers": sorted({row["all_killer"] for row in items}),
            "rows": [compact(row) for row in sorted(items, key=lambda r: repr(r["V"]))],
        }

    new_c53_groups = [
        group_summary(items) for key, items in kg_c53.items()
        if key not in kg_ind and items[0]["n"] <= 120
    ]
    new_all_groups = [
        group_summary(items) for key, items in kg_all.items()
        if key not in kg_ind and items[0]["n"] <= 120
    ]
    all_killed_D_le_120 = [
        group_summary(items) for _key, items in kg_all.items()
        if items[0]["n"] <= 120
    ]
    for lst in (new_c53_groups, new_all_groups, all_killed_D_le_120):
        lst.sort(key=lambda r: (r["n"], r["m"], r["M"], r["V_s"]))

    target_99 = unique_row(
        row_results,
        lambda r: r["n"] == 99 and r["m"] == 66 and r["M"] == [77, 97]
        and r["V"] == {"2": 8, "3": 8},
        "(99,66)",
    )
    target_108 = unique_row(
        row_results,
        lambda r: r["n"] == 108 and r["m"] == 72 and r["M"] == [81, 106]
        and r["V"] == {"2": 7, "3": 7},
        "(108,72; V=(7,7))",
    )
    two_point = [
        row for row in row_results
        if row["u_s"] == 1 and row["phi_eff"].get("s_eff") == 2
        and row["phi_eff"].get("two_point") is True
    ]
    k16_specs = (
        (64, 48, [52, 62], {"2": 3, "3": 3}),
        (112, 80, [100, 110], {"2": 3, "3": 3}),
        (160, 112, [148, 158], {"2": 3, "3": 3}),
    )
    k16_rows = [
        unique_row(
            row_results,
            lambda r, n=n, m=m, Ms=Ms, V=V:
                r["n"] == n and r["m"] == m and r["M"] == Ms and r["V"] == V,
            f"K=16 D={n}",
        )
        for n, m, Ms, V in k16_specs
    ]
    if any(not row["same_tree_all_ok"] for row in k16_rows):
        failures.append("K=16 row died under same-tree all constraints")

    targets = {
        "99_66": compact(target_99),
        "108_72_V_7_7": compact(target_108),
        "direct_two_point_list": {
            "rows": len(two_point),
            "groups": len({row["group_key"] for row in two_point}),
            "independent_sharp": stats(two_point, "independent_ok"),
            "same_tree_cor53": stats(two_point, "same_tree_c53_ok"),
            "same_tree_all": stats(two_point, "same_tree_all_ok"),
        },
        "K_16_entries": [compact(row) for row in k16_rows],
    }

    moh_six = []
    for n, m, Ms, Vs, lab, *_rest in M.MOH_TABLE:
        row = unique_row(
            row_results,
            lambda r, n=n, m=m, Ms=list(Ms), V={str(k): v for k, v in Vs.items()}:
                r["n"] == n and r["m"] == m and r["M"] == Ms and r["V"] == V,
            lab,
        )
        moh_six.append({"label": lab, **compact(row)})

    payload = {
        "input_dir": str(INPUTS),
        "elapsed_s": time.perf_counter() - t0,
        "failures": failures,
        "operative": {
            "rows": len(row_results),
            "groups": len({row["group_key"] for row in row_results}),
            "policies": policies,
            "by_u_s_class": strata,
            "new_same_tree_cor53_killed_groups_D_le_120_vs_independent": new_c53_groups,
            "new_same_tree_all_killed_groups_D_le_120_vs_independent": new_all_groups,
            "same_tree_all_killed_groups_D_le_120": all_killed_D_le_120,
            "killers_all_rows": {
                key: sum(row["all_killer"] == key for row in row_results)
                for key in sorted({row["all_killer"] for row in row_results})
            },
            "killers_all_groups": {
                "Corollary 5.3 / Theorem 4.7(ii)": sum(
                    all(row["all_killer"] == "Corollary 5.3 / Theorem 4.7(ii)" for row in items)
                    for items in kg_all.values()
                ),
                "Theorem 3.4 + Theorem 4.7(i)": sum(
                    all(row["all_killer"] == "Theorem 3.4 + Theorem 4.7(i)" for row in items)
                    for items in kg_all.values()
                ),
                "mixed": sum(
                    len({row["all_killer"] for row in items}) > 1
                    for items in kg_all.values()
                ),
            },
        },
        "calibration": jsonable(calibration),
        "moh_six": moh_six,
        "targets": targets,
        "rows": row_results,
    }
    return payload


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dlo", type=int, default=48)
    ap.add_argument("--dhi", type=int, default=200)
    ap.add_argument("--out", default=str(HERE / "same_tree_results.json"))
    args = ap.parse_args()
    payload = run(args.dlo, args.dhi)
    out = Path(args.out)
    out.write_text(json.dumps(jsonable(payload), indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["operative"]["policies"], indent=2, sort_keys=True))
    if payload["failures"]:
        print("FAILURES:", payload["failures"], file=sys.stderr)
        sys.exit(1)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
