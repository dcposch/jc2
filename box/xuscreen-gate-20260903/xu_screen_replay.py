#!/usr/bin/env python3
"""Xu final-root intersection-number screen on the frozen post-POLY census.

The screen is intentionally fail-closed:

* exact IM/Im is replayed only for Xu's split-specific worked examples;
* census rows are tested by the permissive inequality
      max_possible(IM) >= min_forced(Im)
  over all full-tree partitions embedding the selected Moh row.

The implementation imports the frozen lane inputs, not the mutable workspace
copies of the Moh skeleton or full-tree code.
"""
from __future__ import annotations

import json
import sys
import time
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
from math import gcd
from pathlib import Path


HERE = Path(__file__).resolve().parent
INPUTS = Path("/tmp/jc2-lane.AQwgL6/inputs")
sys.path.insert(0, str(INPUTS))

import moh_skeleton_full as M  # noqa: E402
import full_tree_partition as FT  # noqa: E402


FAILURES: list[str] = []


def check(name: str, cond: bool, detail: str = "") -> bool:
    if cond:
        print(f"  [ok]   {name}", flush=True)
        return True
    print(f"  [FAIL] {name}   {detail}", flush=True)
    FAILURES.append(name)
    return False


def abort_if_failed(stage: str) -> None:
    if FAILURES:
        print(f"{stage} FAILED: {FAILURES}", flush=True)
        sys.exit(1)


def frac_text(x):
    if x is None:
        return None
    if isinstance(x, F):
        return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"
    return str(x)


def row_key(S):
    return (
        S.n,
        S.m,
        tuple(S.M[i] for i in range(2, S.s + 1)),
        tuple((i, S.V[i]) for i in range(2, S.s + 1)),
    )


def group_key(S):
    return (S.n, S.m, tuple(S.M[i] for i in range(2, S.s + 1)), S.V[S.s])


def m_list(S):
    return [S.M[i] for i in range(2, S.s + 1)]


def v_map(S):
    return {i: S.V[i] for i in range(2, S.s + 1)}


def u_s_of(S) -> int:
    return S.d[S.s] - S.V[S.s]


def screens(S):
    return {
        "TREE": FT.full_tree_ok(S),
        "ODE": FT.full_tree_ode_ok(S),
        "POLY": FT.full_tree_polynomial_ok(S),
        "POLY_ODE": FT.full_tree_polynomial_ode_ok(S),
    }


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


@dataclass(frozen=True)
class Bound:
    im_min: F
    im_witness: dict
    im_max: F
    imax_witness: dict


class XuBounder:
    """Optimize Xu's IM/Im bounds over operative full-tree embeddings."""

    def __init__(self, S):
        self.S = S
        self.E = FT.evaluator(S, polynomial_recenter=True, ode_nondegenerate=True)
        self.required = {i: S.V[i] for i in range(2, S.s)}

    def principal_im_floor(self) -> F:
        us = u_s_of(self.S)
        if us <= 0:
            return F(0)
        if us > 1:
            return F(0)
        val = F(self.S.V[self.S.s], us) - 1
        return val if val > 0 else F(0)

    def child_danger(self, j, path, is_zero):
        delta_j = self.E.radius(j, path)
        removable_nonzero = delta_j.denominator == 1 and delta_j <= 0
        return is_zero or removable_nonzero

    def minor_order(self, j, path, value: int) -> F:
        delta, _L, _A, _P, _Q, lo = self.E.level_data(j, path)
        return delta + lo * (1 - delta) / value

    def minor_contribution(self, j, path, value: int, orbit_size: int) -> F:
        contrib = self.minor_order(j, path, value) - 1
        return orbit_size * (contrib if contrib > 0 else F(0))

    def major_child_bound(self, j, path, value: int, dangerous: bool, is_zero: bool, embed: bool = False):
        newpath = self.E.extend(path, j, value)
        delta_j = self.E.radius(j, path)
        removable_nonzero = delta_j.denominator == 1 and delta_j <= 0
        newdanger = dangerous and (is_zero or removable_nonzero)
        if j == 2:
            if newdanger:
                return None
            ok, _wit = self.E.bottom(newpath)
            if not ok:
                return None
            delta1 = self.E.radius(1, newpath)
            df = F(value * self.S.m, self.S.d[j])
            lambda_neg = F(self.S.n, self.S.m + self.S.n) * (1 - delta1)
            imax = df * lambda_neg
            return Bound(F(0), {"kind": "major-leaf", "V": value, "IM": frac_text(imax)},
                         imax, {"kind": "major-leaf", "V": value, "IM": frac_text(imax)})
        if embed:
            return self.embed_node(j - 1, newpath, newdanger)
        return self.global_node(j - 1, newpath, newdanger)

    def coin_options(self, j, path, dangerous, total, lo, A, P, Q):
        out = []
        for value in range(1, total + 1):
            if P - Q * value == 0:
                continue
            if value > lo:
                child = self.major_child_bound(j, path, value, dangerous, False)
                if child is None:
                    continue
                out.append({
                    "value": value,
                    "major": True,
                    "im_min": A * child.im_min,
                    "im_max": A * child.im_max,
                    "im_witness": child.im_witness,
                    "imax_witness": child.imax_witness,
                })
            else:
                imc = self.minor_contribution(j, path, value, A)
                out.append({
                    "value": value,
                    "major": False,
                    "im_min": imc,
                    "im_max": F(0),
                    "im_witness": {"kind": "minor-orbit", "V": value, "A": A,
                                   "order": frac_text(self.minor_order(j, path, value)),
                                   "contribution": frac_text(imc)},
                    "imax_witness": None,
                })
        return out

    def multiset_extreme(self, total, max_coins, options, initial_major, mode):
        opt = tuple(sorted(options, key=lambda o: o["value"]))

        @lru_cache(maxsize=None)
        def visit(remainder, coins_left, start, has_major):
            if remainder == 0:
                if has_major:
                    return F(0), []
                return None
            if coins_left == 0:
                return None
            best = None
            for idx in range(start, len(opt)):
                item = opt[idx]
                value = item["value"]
                if value > remainder:
                    break
                tail = visit(
                    remainder - value,
                    coins_left - 1,
                    idx,
                    has_major or item["major"],
                )
                if tail is None:
                    continue
                tail_score, tail_items = tail
                score = item[mode] + tail_score
                candidate = (score, [item] + tail_items)
                if best is None:
                    best = candidate
                elif mode == "im_min" and score < best[0]:
                    best = candidate
                elif mode == "im_max" and score > best[0]:
                    best = candidate
            return best

        return visit(total, max_coins, 0, initial_major)

    def option_bound(self, j, path, dangerous, b, selected_mode=None):
        delta, L, A, P, Q, lo = self.E.level_data(j, path)
        if b > 0 and P - Q * b == 0:
            return None
        total = (P - b) // A
        max_orbits = Q // A
        zero_major = b > lo if b > 0 else False
        zero_im_min = F(0)
        zero_im_max = F(0)
        zero_wit_min = None
        zero_wit_max = None
        if b > 0:
            if zero_major:
                child = self.major_child_bound(j, path, b, dangerous, True,
                                               embed=(selected_mode == "zero"))
                if child is None:
                    return None
                zero_im_min, zero_im_max = child.im_min, child.im_max
                zero_wit_min, zero_wit_max = child.im_witness, child.imax_witness
            else:
                if selected_mode == "zero":
                    return None
                zero_im_min = self.minor_contribution(j, path, b, 1)
                zero_wit_min = {"kind": "minor-zero", "V": b,
                                "order": frac_text(self.minor_order(j, path, b)),
                                "contribution": frac_text(zero_im_min)}

        options = self.coin_options(j, path, dangerous, total, lo, A, P, Q)
        forced_score_min = F(0)
        forced_score_max = F(0)
        forced_items_min = []
        forced_items_max = []
        rest_total = total
        rest_max = max_orbits
        initial_major = zero_major

        if selected_mode == "nonzero":
            vreq = self.required[j]
            if not (vreq > lo and rest_total >= vreq and rest_max >= 1):
                return None
            selected_child = self.major_child_bound(j, path, vreq, dangerous, False, embed=True)
            if selected_child is None:
                return None
            if not any(item["value"] == vreq and item["major"] for item in options):
                return None
            forced_score_min += A * selected_child.im_min
            forced_score_max += A * selected_child.im_max
            forced_items_min.append({"forced-selected-nonzero": vreq,
                                     "A": A, "child": selected_child.im_witness})
            forced_items_max.append({"forced-selected-nonzero": vreq,
                                     "A": A, "child": selected_child.imax_witness})
            rest_total -= vreq
            rest_max -= 1
            initial_major = True
        elif selected_mode == "zero":
            vreq = self.required[j]
            if b != vreq or not zero_major:
                return None
            initial_major = True

        min_rest = self.multiset_extreme(rest_total, rest_max, options, initial_major, "im_min")
        max_rest = self.multiset_extreme(rest_total, rest_max, options, initial_major, "im_max")
        if min_rest is None or max_rest is None:
            return None
        min_score, min_items = min_rest
        max_score, max_items = max_rest
        bdata = {"j": j, "delta": frac_text(delta), "L": L, "A": A, "P": P, "Q": Q,
                 "b": b, "selected_mode": selected_mode}
        return Bound(
            zero_im_min + forced_score_min + min_score,
            {**bdata, "zero": zero_wit_min, "coins": forced_items_min + self.slim_items(min_items, "im")},
            zero_im_max + forced_score_max + max_score,
            {**bdata, "zero": zero_wit_max, "coins": forced_items_max + self.slim_items(max_items, "IM")},
        )

    @staticmethod
    def slim_items(items, mode):
        out = []
        for item in items:
            out.append({
                "V": item["value"],
                "major": item["major"],
                "score": frac_text(item["im_min"] if mode == "im" else item["im_max"]),
            })
        return out

    @lru_cache(maxsize=None)
    def global_node(self, j, path, dangerous):
        delta, L, A, P, Q, _lo = self.E.level_data(j, path)
        residue = P % A
        best_min = None
        best_max = None
        for b in range(residue, P + 1, A):
            bound = self.option_bound(j, path, dangerous, b)
            if bound is None:
                continue
            if best_min is None or bound.im_min < best_min.im_min:
                best_min = bound
            if best_max is None or bound.im_max > best_max.im_max:
                best_max = bound
        if best_min is None or best_max is None:
            return None
        return Bound(best_min.im_min, best_min.im_witness, best_max.im_max, best_max.imax_witness)

    @lru_cache(maxsize=None)
    def embed_node(self, j, path, dangerous):
        delta, L, A, P, Q, lo = self.E.level_data(j, path)
        vreq = self.required[j]
        residue = P % A
        best_min = None
        best_max = None
        for b in range(residue, P + 1, A):
            if b == vreq and vreq > lo:
                bound = self.option_bound(j, path, dangerous, b, selected_mode="zero")
                if bound is not None:
                    if best_min is None or bound.im_min < best_min.im_min:
                        best_min = bound
                    if best_max is None or bound.im_max > best_max.im_max:
                        best_max = bound
            bound = self.option_bound(j, path, dangerous, b, selected_mode="nonzero")
            if bound is not None:
                if best_min is None or bound.im_min < best_min.im_min:
                    best_min = bound
                if best_max is None or bound.im_max > best_max.im_max:
                    best_max = bound
        if best_min is None or best_max is None:
            return None
        return Bound(best_min.im_min, best_min.im_witness, best_max.im_max, best_max.imax_witness)

    def row_bound(self):
        tree = self.embed_node(self.S.s - 1, self.E.initial_path(), True)
        if tree is None:
            return None
        principal = self.principal_im_floor()
        im_floor = F(1) + principal + tree.im_min
        return {
            "IM_max": tree.im_max,
            "Im_min": im_floor,
            "tree_minor_min": tree.im_min,
            "principal_minor_floor": principal,
            "xu_ok": tree.im_max >= im_floor,
            "IM_witness": tree.imax_witness,
            "Im_witness": tree.im_witness,
        }


def manual_j2_split(S, *, zero: int, nonzero_values: list[int]) -> dict:
    E = FT.evaluator(S, polynomial_recenter=True, ode_nondegenerate=True)
    path = list(E.initial_path())
    path[S.s] = S.V[S.s]
    path = tuple(path)
    if S.s != 3:
        raise ValueError("manual replay expects Xu's s=3 examples")
    delta, _L, A, P, _Q, lo = E.level_data(2, path)
    if P != A * sum(nonzero_values) + zero:
        raise ValueError("manual split does not match P=A*sum+b")
    principal = F(S.V[S.s], u_s_of(S)) - 1
    im = F(1) + principal
    IM = F(0)
    parts = []
    if zero:
        order = XuBounder(S).minor_order(2, path, zero)
        if zero > lo:
            b = XuBounder(S).major_child_bound(2, path, zero, True, True)
            if b is None:
                raise ValueError("manual zero major infeasible")
            IM += b.im_max
            parts.append(("zero-major", zero, F(1), b.im_max))
        else:
            im += order - 1
            parts.append(("zero-minor", zero, order, order - 1))
    for value in nonzero_values:
        if value > lo:
            b = XuBounder(S).major_child_bound(2, path, value, True, False)
            if b is None:
                raise ValueError("manual nonzero major infeasible")
            IM += A * b.im_max
            parts.append(("nonzero-major", value, A, A * b.im_max))
        else:
            order = XuBounder(S).minor_order(2, path, value)
            im += A * (order - 1)
            parts.append(("nonzero-minor", value, order, A * (order - 1)))
    return {
        "n": S.n,
        "m": S.m,
        "M": m_list(S),
        "V": v_map(S),
        "zero": zero,
        "nonzero_values": nonzero_values,
        "A": A,
        "delta2": frac_text(delta),
        "principal_order": frac_text(F(S.V[S.s], u_s_of(S))),
        "IM": IM,
        "Im": im,
        "excluded": IM < im,
        "parts": [(a, b, frac_text(c), frac_text(d)) for a, b, c, d in parts],
    }


def xu_summary(S) -> dict:
    bound = XuBounder(S).row_bound()
    if bound is None:
        return {"xu_ok": False, "reason": "NO-EMBED-UNDER-OPERATIVE-SCREEN"}
    return {
        "IM_max": frac_text(bound["IM_max"]),
        "Im_min": frac_text(bound["Im_min"]),
        "tree_minor_min": frac_text(bound["tree_minor_min"]),
        "principal_minor_floor": frac_text(bound["principal_minor_floor"]),
        "xu_ok": bound["xu_ok"],
    }


def jsonable(obj):
    if isinstance(obj, F):
        return frac_text(obj)
    if isinstance(obj, dict):
        return {str(k): jsonable(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [jsonable(v) for v in obj]
    if isinstance(obj, tuple):
        return [jsonable(v) for v in obj]
    return obj


def main():
    t0 = time.perf_counter()
    print("== Xu IM>=Im fail-closed skeleton screen ==", flush=True)
    print(f"Frozen imports: {INPUTS}", flush=True)

    print("\n-- Controls --", flush=True)
    moh = [(lab, M.Skel(n, m, list(Ms), dict(Vs))) for n, m, Ms, Vs, lab, *_ in M.MOH_TABLE]
    for lab, S in moh:
        scr = screens(S)
        check(f"Moh {lab} POLY_ODE operative survivor", scr["POLY_ODE"])
    abort_if_failed("operative Moh controls")

    cal = {
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
        "75_50_split_i_permissive": manual_j2_split(
            M.Skel(75, 50, [55, 73], {2: 2, 3: 4}),
            zero=0,
            nonzero_values=[2, 2],
        ),
    }
    check("Xu (75,50) split ii Im=6 IM=4 excluded",
          cal["75_50_split_ii"]["Im"] == 6 and cal["75_50_split_ii"]["IM"] == 4
          and cal["75_50_split_ii"]["excluded"])
    check("Xu (84,56) M2=64 Im=5 IM=4 excluded",
          cal["84_56_M2_64_V2_2"]["Im"] == 5 and cal["84_56_M2_64_V2_2"]["IM"] == 4
          and cal["84_56_M2_64_V2_2"]["excluded"])
    check("Xu (84,56) M2=72 Im=4 IM=10 not excluded",
          cal["84_56_M2_72_V2_5"]["Im"] == 4 and cal["84_56_M2_72_V2_5"]["IM"] == 10
          and not cal["84_56_M2_72_V2_5"]["excluded"])
    abort_if_failed("Xu calibration")

    print("\n-- Operative census, u_s>1 first --", flush=True)
    rows_all = []
    for n in range(48, 201):
        for m, Ms, V in M.census(n, Kmin=16, full=True):
            S = M.Skel(n, m, list(Ms), V)
            if FT.full_tree_polynomial_ode_ok(S):
                rows_all.append(S)
    check("operative rows D<=200 = 1420", len(rows_all) == 1420, f"got {len(rows_all)}")
    groups_all = defaultdict(list)
    for S in rows_all:
        groups_all[group_key(S)].append(S)
    check("operative groups D<=200 = 686", len(groups_all) == 686, f"got {len(groups_all)}")
    abort_if_failed("operative census")

    row_results = []
    for phase, predicate in (("us_gt_1", lambda S: u_s_of(S) > 1),
                             ("us_eq_1", lambda S: u_s_of(S) == 1)):
        phase_rows = [S for S in rows_all if predicate(S)]
        print(f"  phase {phase}: {len(phase_rows)} rows", flush=True)
        for idx, S in enumerate(phase_rows, 1):
            rec = {
                "phase": phase,
                "n": S.n,
                "m": S.m,
                "s": S.s,
                "M": m_list(S),
                "V": v_map(S),
                "V_s": S.V[S.s],
                "u_s": u_s_of(S),
                "row_key": repr(row_key(S)),
                "group_key": repr(group_key(S)),
                "phi_eff": phi_eff(S),
            }
            rec.update(xu_summary(S))
            row_results.append(rec)
            if idx % 100 == 0 or idx == len(phase_rows):
                killed = sum(1 for r in row_results if not r["xu_ok"])
                print(f"    {phase} {idx}/{len(phase_rows)} processed; killed rows total {killed}",
                      flush=True)

    killed_rows = [r for r in row_results if not r["xu_ok"]]
    by_group = defaultdict(list)
    for r in row_results:
        by_group[r["group_key"]].append(r)
    killed_groups = {gk: items for gk, items in by_group.items()
                     if all(not r["xu_ok"] for r in items)}
    touched_groups = {gk: items for gk, items in by_group.items()
                      if any(not r["xu_ok"] for r in items)}

    strata_rows = defaultdict(lambda: {"rows": 0, "killed_rows": 0, "groups": set(), "killed_groups": set()})
    for r in row_results:
        ph = r["phi_eff"]
        us_class = "u_s>1" if r["u_s"] > 1 else "u_s=1"
        two = "NA" if r["u_s"] > 1 else ("two-point" if ph.get("two_point") else "not-two-point")
        key = (us_class, r["s"], two)
        strata_rows[key]["rows"] += 1
        strata_rows[key]["groups"].add(r["group_key"])
        if not r["xu_ok"]:
            strata_rows[key]["killed_rows"] += 1
    for gk, items in killed_groups.items():
        reps = items
        for key in {(("u_s>1" if r["u_s"] > 1 else "u_s=1"), r["s"],
                     "NA" if r["u_s"] > 1 else ("two-point" if r["phi_eff"].get("two_point") else "not-two-point"))
                    for r in reps}:
            strata_rows[key]["killed_groups"].add(gk)

    strata = []
    for key in sorted(strata_rows):
        data = strata_rows[key]
        strata.append({
            "u_s_class": key[0],
            "s": key[1],
            "two_point": key[2],
            "rows": data["rows"],
            "killed_rows": data["killed_rows"],
            "groups": len(data["groups"]),
            "killed_groups": len(data["killed_groups"]),
        })

    killed_group_list = []
    for gk, items in killed_groups.items():
        first = items[0]
        if first["n"] <= 120:
            killed_group_list.append({
                "n": first["n"],
                "m": first["m"],
                "M": first["M"],
                "V_s": first["V_s"],
                "u_s": first["u_s"],
                "s": first["s"],
                "rows_in_group": len(items),
                "bounds": sorted({(r["IM_max"], r["Im_min"]) for r in items}),
            })
    killed_group_list.sort(key=lambda r: (r["n"], r["m"], r["M"], r["V_s"]))

    moh_status = []
    for lab, S in moh:
        rec = xu_summary(S)
        moh_status.append({
            "label": lab,
            "n": S.n,
            "m": S.m,
            "M": m_list(S),
            "V": v_map(S),
            "u_s": u_s_of(S),
            **rec,
        })

    payload = {
        "input_dir": str(INPUTS),
        "principal_minor_floor_policy": (
            "exact V_s/u_s - 1 for u_s=1; 0 for u_s>1 because the final "
            "principal-minor split number and final orders are not determined "
            "by the skeleton alone"
        ),
        "elapsed_s": time.perf_counter() - t0,
        "controls": {"failures": FAILURES, "calibration": jsonable(cal)},
        "operative": {
            "rows": len(rows_all),
            "groups": len(groups_all),
            "killed_rows": len(killed_rows),
            "killed_groups": len(killed_groups),
            "touched_groups": len(touched_groups),
            "strata": strata,
            "killed_groups_D_le_120": killed_group_list,
        },
        "moh_six": moh_status,
        "rows": row_results,
    }
    out = HERE / "results.json"
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print("\n-- Totals --", flush=True)
    print(f"  killed rows: {len(killed_rows)} / {len(row_results)}", flush=True)
    print(f"  killed groups: {len(killed_groups)} / {len(groups_all)}", flush=True)
    print(f"  touched groups: {len(touched_groups)} / {len(groups_all)}", flush=True)
    print(f"  killed groups D<=120: {len(killed_group_list)}", flush=True)
    print(f"Wrote {out}", flush=True)


if __name__ == "__main__":
    main()
