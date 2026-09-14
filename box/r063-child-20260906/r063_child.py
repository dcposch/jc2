#!/usr/bin/env python3
"""Child complete configurations under printed fixed-list closure.

Reuses box/exact-contact-gate-20260906/{census_replay.py,closure_fixed.py}
identities (cf.patterns, Closure.node packet arithmetic, census_replay actual-L
walker) and licensed own-child data from box.lib.descend_own. Does not rewrite
those identities. The ell-shift is the printed 1 -> 1+ell of Xu Lemma 4.1 /
Moh Prop 4.6(3)* (gate report §7), applied inside the same node.

A configuration is not a polynomial pair. I_m is the unsplit minor floor
(Xu Cor 5.3 formula applied as DATA; child Thm 4.7 is not printed).
"""
from __future__ import annotations

import importlib.util
import json
import sys
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from math import lcm
from pathlib import Path

ROOT = Path("/home/ubuntu/jc2")
HERE = Path(__file__).resolve().parent
LANE = Path("/tmp/jc2-lane.e1ztmS/inputs")
GATE = ROOT / "box" / "exact-contact-gate-20260906"
ROSTER = LANE / "roster.jsonl"

sys.path.insert(0, str(ROOT))
sys.dont_write_bytecode = True


def _load_gate(name: str, path: Path, replacements: list[tuple[str, str]]):
    text = path.read_text()
    for old, new in replacements:
        if old not in text:
            raise RuntimeError(f"{path.name}: replacement anchor not found: {old!r}")
        text = text.replace(old, new)
    spec = importlib.util.spec_from_loader(name, loader=None)
    mod = importlib.util.module_from_spec(spec)
    mod.__file__ = str(path)
    mod.__name__ = name
    sys.modules[name] = mod
    exec(compile(text, str(path), "exec"), mod.__dict__)
    return mod


cr = _load_gate(
    "census_replay",
    GATE / "census_replay.py",
    [("INPUT=Path('/tmp/jc2-lane.QKyQBy/inputs/roster.jsonl')",
      f"INPUT=Path('{ROSTER}')")],
)
cf = _load_gate(
    "closure_fixed",
    GATE / "closure_fixed.py",
    [("ROOT=Path('/tmp/jc2-lane.QKyQBy/inputs')",
      f"ROOT=Path('{LANE}')")],
)

from box.lib.descend_own import (  # noqa: E402
    def51_radii,
    descend_own,
    exact_int,
)


class Src:
    def __init__(self, source: dict):
        self.n = source["n"]
        self.m = source["m"]
        self.s = source["s"]
        self.M = {i + 1: source["M"][i] for i in range(self.s)}
        self.V = {i + 2: source["V"][i] for i in range(len(source["V"]))}


def qstr(x) -> str:
    x = F(x)
    return str(x.numerator) if x.denominator == 1 else str(x)


def ser(x):
    if isinstance(x, F):
        return qstr(x)
    if isinstance(x, dict):
        return {str(k): ser(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [ser(v) for v in x]
    return x


class EllClosure(cf.Closure):
    """Gate Closure.node with the printed 1 -> 1+ell in delta / kappa.

    ungated=True keeps the D1 J even when the residue law fails (for the
    71/4 comparison). Printed-complete trees use ungated=False.
    """

    def __init__(self, row, ell=0, ungated=False):
        super().__init__(row)
        self.ell = int(ell)
        self.one = F(1) + self.ell
        self.ungated = bool(ungated)
        self.hits = []

    @lru_cache(None)
    def node(self, i, rho, kappa, L, selected_path=False):
        n, m = self.n, self.m
        W = n - self.M[i]
        one = self.one
        delta = one - F(W) * kappa / (W * rho - m)
        lam = F(m) * kappa / (W * rho - m)
        A = (L * delta).denominator
        if i == 1:
            rg = F(n) * rho / m
            remf = rho % A
            remg = rg % A
            good = (
                rg.denominator == 1
                and remf in (0, 1)
                and remg in (0, 1)
                and not (remf == remg == 1)
            )
            J = F(n) * rho * kappa / ((n + m) * rho - m)
            rec = {
                "i": i,
                "rho_f": rho,
                "rho_g": rg,
                "kappa": kappa,
                "L": L,
                "delta": delta,
                "A": A,
                "final_J": J,
                "galois_ok": good,
                "remf": remf,
                "remg": int(remg) if rg.denominator == 1 else None,
                "selected_path": selected_path,
            }
            self.log[(i, rho, kappa, L, selected_path)] = rec
            if good or self.ungated:
                return {(J, F(0))}
            return set()
        P = F(rho * self.d[i], m)
        Q = F(rho * W, m)
        if P.denominator > 1 or Q.denominator > 1:
            self.log[(i, rho, kappa, L, selected_path)] = {
                "i": i, "rho_f": rho, "kappa": kappa, "L": L, "delta": delta,
                "P": P, "Q": Q, "failure": "P_or_Q_noninteger",
            }
            return set()
        pats = []
        allvals = set()
        threshold = F(self.d[i], W)
        for z, part in cf.patterns(int(P), int(Q), A, threshold,
                                   self.V[i] if selected_path else None):
            factors = ([(z, 1, "zero")] if z else []) + [(x, A, "orbit") for x in part]
            vals = {(F(0), F(0))}
            factorlog = []
            sel_used = False
            empty = False
            for r, count, typ in factors:
                crho = F(m * r, self.d[i])
                ck = crho * (one - delta) - lam
                assert crho.denominator == 1
                crho = int(crho)
                if ck < 0:
                    cv = {(F(0), -ck / crho)}
                    state = {"type": "minor", "rho": crho, "kappa": ck,
                             "delta": one - ck / crho}
                else:
                    use_sel = selected_path and r == self.V[i] and not sel_used
                    if use_sel:
                        sel_used = True
                    childL = L if typ == "zero" else lcm(L, delta.denominator)
                    cv = self.node(i - 1, crho, ck, childL, use_sel)
                    state = {
                        "type": "major", "i": i - 1, "rho": crho, "kappa": ck,
                        "L": childL, "selected": use_sel, "outcomes": len(cv),
                    }
                factorlog.append({"r": r, "count": count, "kind": typ, **state})
                if not cv:
                    empty = True
                    vals = set()
                    break
                vals = {(a + count * c, b + count * d) for a, b in vals for c, d in cv}
            recp = {
                "z": z, "orbit_multiplicities": part, "factors": factorlog,
                "outcomes": 0 if empty else len(vals),
                "values": sorted(vals),
            }
            pats.append(recp)
            allvals |= vals
        self.log[(i, rho, kappa, L, selected_path)] = {
            "i": i, "rho_f": rho, "kappa": kappa, "L": L, "delta": delta,
            "A": A, "P": P, "Q": Q, "selected_path": selected_path,
            "threshold": threshold, "patterns": pats,
            "outcomes": len(allvals), "values": sorted(allvals),
        }
        return allvals

    def top_kappa(self):
        n, m, s = self.n, self.m, self.s
        W = n - self.M[s]
        delta_s = self.one - F(W) * F(n - self.M[s], n - self.M[s] - 1)
        # Def 5.1 unscaled (1-ratio) times (1+ell): use the source delta if present.
        if "delta" in self.row:
            delta_s = F(self.row["delta"][s - 1])
        kappa = m * (self.one - delta_s) * (W - 1) / W
        return int(m), kappa, delta_s, W

    def walk_selected(self, i, rho, kappa, L, path):
        """Yield (path, values_set, node_rec) for each selected-path pattern."""
        n, m = self.n, self.m
        W = n - self.M[i]
        one = self.one
        delta = one - F(W) * kappa / (W * rho - m)
        lam = F(m) * kappa / (W * rho - m)
        A = (L * delta).denominator
        if i == 1:
            rg = F(n) * rho / m
            remf = rho % A
            remg = rg % A
            good = (
                rg.denominator == 1
                and remf in (0, 1)
                and remg in (0, 1)
                and not (remf == remg == 1)
            )
            J = F(n) * rho * kappa / ((n + m) * rho - m)
            rec = {
                "i": 1, "rho_f": rho, "rho_g": qstr(rg), "L": L, "A": A,
                "delta": qstr(delta), "final_J": qstr(J), "galois_ok": good,
                "remf": remf,
                "remg": int(remg) if rg.denominator == 1 else None,
            }
            vals = {(J, F(0))} if (good or self.ungated) else set()
            yield path, vals, rec
            return
        P = F(rho * self.d[i], m)
        Q = F(rho * W, m)
        if P.denominator > 1 or Q.denominator > 1:
            yield path + (("P_or_Q_noninteger", str(P), str(Q)),), set(), {
                "i": i, "failure": "P_or_Q_noninteger", "P": qstr(P), "Q": qstr(Q),
            }
            return
        threshold = F(self.d[i], W)
        pats = list(cf.patterns(int(P), int(Q), A, threshold, self.V[i]))
        if not pats:
            yield path, set(), {
                "i": i, "rho_f": rho, "L": L, "A": A, "delta": qstr(delta),
                "P": int(P), "Q": int(Q), "threshold": qstr(threshold),
                "n_patterns": 0, "failure": "no_selected_pattern",
            }
            return
        for z, part in pats:
            factors = ([(z, 1, "zero")] if z else []) + [(x, A, "orbit") for x in part]
            acc = {(F(0), F(0))}
            factorlog = []
            sel_used = False
            dead = False
            selected_subs = None
            selected_count = None
            for r, count, typ in factors:
                crho = F(m * r, self.d[i])
                ck = crho * (one - delta) - lam
                assert crho.denominator == 1
                crho = int(crho)
                use_sel = (r == self.V[i]) and not sel_used
                if ck < 0:
                    if use_sel:
                        sel_used = True
                        dead = True
                        factorlog.append({
                            "r": r, "count": count, "kind": typ, "type": "minor",
                            "rho": crho, "selected": True,
                            "failure": "selected_factor_minor",
                        })
                        break
                    cv = {(F(0), -ck / crho)}
                    factorlog.append({
                        "r": r, "count": count, "kind": typ, "type": "minor",
                        "rho": crho, "kappa": qstr(ck),
                        "delta": qstr(one - ck / crho), "selected": False,
                    })
                    acc = {(a + count * c, b + count * d)
                           for a, b in acc for c, d in cv}
                    continue
                childL = L if typ == "zero" else lcm(L, delta.denominator)
                if use_sel:
                    sel_used = True
                    sub = list(self.walk_selected(
                        i - 1, crho, ck, childL,
                        path + ((i, z, tuple(part), typ, r),),
                    ))
                    factorlog.append({
                        "r": r, "count": count, "kind": typ, "type": "major",
                        "i": i - 1, "rho": crho, "kappa": qstr(ck),
                        "L": childL, "selected": True, "n_sub": len(sub),
                    })
                    selected_subs = sub
                    selected_count = count
                    continue
                cv = self.node(i - 1, crho, ck, childL, False)
                factorlog.append({
                    "r": r, "count": count, "kind": typ, "type": "major",
                    "i": i - 1, "rho": crho, "kappa": qstr(ck),
                    "L": childL, "selected": False, "outcomes": len(cv),
                })
                if not cv:
                    dead = True
                    acc = set()
                    break
                acc = {(a + count * c, b + count * d)
                       for a, b in acc for c, d in cv}
            rec = {
                "i": i, "z": z, "orbits": list(part), "L": L, "A": A,
                "delta": qstr(delta), "P": int(P), "Q": int(Q),
                "threshold": qstr(threshold), "factors": factorlog,
                "sel_used": sel_used, "sibling_dead": dead,
            }
            if dead or selected_subs is None:
                yield path + ((i, z, tuple(part),
                               "DEAD" if dead else "NO_SELECTED", None),), set(), rec
                continue
            for subpath, subvals, subrec in selected_subs:
                if not subvals:
                    yield subpath, set(), {"this": rec, "sub": subrec}
                    continue
                outv = {(a + selected_count * c, b + selected_count * d)
                        for a, b in acc for c, d in subvals}
                yield subpath, outv, {"this": rec, "sub": subrec}


def child_source(D, vec, ell):
    n, m, s = int(D["n"]), int(D["m"]), int(D["s"])
    M = {i: exact_int(D["M"][i]) for i in range(1, s + 1)}
    d = {i: exact_int(D["d"][i]) for i in range(1, s + 2)}
    V = {i: exact_int(vec[i - 2]) for i in range(2, s + 1)}
    V[s + 1] = d[s + 1]
    delta = def51_radii(n, M, d, V, ell + 1)
    row = {
        "n": n,
        "m": m,
        "s": s,
        "M": [M[i] for i in range(1, s + 1)],
        "d": [d[i] for i in range(1, s + 2)],
        "V": [V[i] for i in range(2, s + 1)],
        "delta": [delta[i] for i in range(1, s + 1)],
        "v_s": V[s],
        "u_s": d[s] - V[s],
        "ell": ell,
    }
    return row, delta, V, M, d


def path_key(path):
    out = []
    for item in path:
        if not item:
            continue
        if item[0] in ("P_or_Q_noninteger",):
            out.append({"failure": item[0], "P": item[1], "Q": item[2]})
        else:
            i, z, part, kind, r = item
            out.append({
                "level": i, "z": z, "orbits": list(part),
                "selected_kind": kind, "selected_r": r,
            })
    return out


def pack_values(vals, ungated_vals):
    pairs = []
    for im, mn in sorted(vals, key=lambda t: (t[0], t[1])):
        im_xu = F(1) + mn
        pairs.append({
            "I_M": qstr(im),
            "I_m_packets": qstr(mn),
            "I_m": qstr(im_xu),
            "I_M_integral": im.denominator == 1,
            "I_M_ge_I_m": im >= im_xu,
        })
    raw = []
    for im, mn in sorted(ungated_vals, key=lambda t: (t[0], t[1])):
        im_xu = F(1) + mn
        raw.append({
            "I_M": qstr(im),
            "I_m_packets": qstr(mn),
            "I_m": qstr(im_xu),
            "I_M_integral": im.denominator == 1,
            "I_M_ge_I_m": im >= im_xu,
        })
    return pairs, raw


def run_child_convention(row, ell, parent_IM):
    C = EllClosure(row, ell=ell, ungated=False)
    U = EllClosure(row, ell=ell, ungated=True)
    rho, kappa, delta_s, W = C.top_kappa()
    # Cross-check reconstructed delta at the top.
    one = F(1) + ell
    n, m, s = row["n"], row["m"], row["s"]
    rec_delta = one - F(W) * kappa / (W * rho - m)
    assert rec_delta == F(row["delta"][s - 1]), (rec_delta, row["delta"][s - 1])

    cfgs = []
    n_pat = 0
    n_complete = 0
    complete_IM = []
    ungated_IM = []
    for path, vals, rec in C.walk_selected(s, rho, kappa, 1, ()):
        n_pat += 1
        # Matching ungated walk: re-evaluate this selected path by using U.node
        # on the same top; collect all ungated values for the same pattern key.
        cfgs.append({
            "patterns": path_key(path),
            "complete": bool(vals),
            "pairs": pack_values(vals, set())[0],
            "node": ser(rec) if isinstance(rec, dict) else rec,
        })
        if vals:
            n_complete += len(vals)
            complete_IM.extend(vals)
    for path, vals, rec in U.walk_selected(s, rho, kappa, 1, ()):
        ungated_IM.extend(vals)
        # attach ungated pairs onto the matching pattern if possible
        pk = path_key(path)
        for c in cfgs:
            if c["patterns"] == pk:
                c["ungated_pairs"] = pack_values(set(), vals)[1]
                c["ungated_complete_as_numerical"] = bool(vals)
                break
        else:
            cfgs.append({
                "patterns": pk,
                "complete": False,
                "pairs": [],
                "ungated_pairs": pack_values(set(), vals)[1],
                "ungated_complete_as_numerical": bool(vals),
                "node": ser(rec) if isinstance(rec, dict) else rec,
            })

    def d1_leaves(closure):
        leaves = []
        for rec in closure.log.values():
            if not isinstance(rec, dict) or rec.get("i") != 1:
                continue
            leaves.append({
                "rho_f": rec.get("rho_f"),
                "rho_g": qstr(rec["rho_g"]) if "rho_g" in rec else None,
                "L": rec.get("L"),
                "A": rec.get("A"),
                "delta": qstr(rec["delta"]) if "delta" in rec else None,
                "J": qstr(rec["final_J"]) if "final_J" in rec else None,
                "galois_ok": rec.get("galois_ok"),
                "remf": rec.get("remf"),
                "remg": rec.get("remg"),
                "selected_path": rec.get("selected_path"),
            })
        return leaves

    # Also the summed Closure.node at the top (set of complete pairs).
    node_set = C.node(s, rho, kappa, 1, True)
    ungated_set = U.node(s, rho, kappa, 1, True)
    d1_gated = d1_leaves(C)
    d1_ungated = d1_leaves(U)

    def valset(pairs):
        return sorted({(F(p[0]), F(p[1])) for p in pairs})

    complete_pairs = sorted(node_set, key=lambda t: (t[0], t[1]))
    ungated_pairs = sorted(ungated_set, key=lambda t: (t[0], t[1]))
    IM_complete = [im for im, mn in complete_pairs]
    IM_ungated = [im for im, mn in ungated_pairs]
    target = F(parent_IM)
    seventy = F(71, 4)
    return {
        "ell": ell,
        "convention": "shifted" if ell else "unshifted",
        "top": {
            "rho": rho,
            "kappa": qstr(kappa),
            "delta_s": qstr(delta_s),
            "W_s": W,
            "L0": 1,
            "one": qstr(one),
        },
        "n_selected_pattern_paths": n_pat,
        "n_complete_pairs": len(complete_pairs),
        "n_ungated_pairs": len(ungated_pairs),
        "complete_pairs": [
            {
                "I_M": qstr(im),
                "I_m_packets": qstr(mn),
                "I_m": qstr(F(1) + mn),
                "I_M_integral": im.denominator == 1,
                "equals_parent_I_M": im == target,
                "is_71_4": im == seventy,
            }
            for im, mn in complete_pairs
        ],
        "ungated_pairs": [
            {
                "I_M": qstr(im),
                "I_m_packets": qstr(mn),
                "I_m": qstr(F(1) + mn),
                "I_M_integral": im.denominator == 1,
                "equals_parent_I_M": im == target,
                "is_71_4": im == seventy,
            }
            for im, mn in ungated_pairs
        ],
        "complete_I_M": [qstr(x) for x in IM_complete],
        "ungated_I_M": [qstr(x) for x in IM_ungated],
        "any_complete_equals_parent": any(im == target for im in IM_complete),
        "any_ungated_equals_parent": any(im == target for im in IM_ungated),
        "any_complete_is_71_4": any(im == seventy for im in IM_complete),
        "any_ungated_is_71_4": any(im == seventy for im in IM_ungated),
        "d1_gated": d1_gated,
        "d1_ungated": d1_ungated,
        "n_cf_selected_patterns": n_pat,
        "configs": cfgs,
        "census_replay_actual_L_n": None,
    }


def census_actual_L_count(row):
    """Gate actual-L walker starting at the child top (i=s), V extended."""
    src = dict(row)
    src["V"] = list(row["V"]) + [row["d"][-1]]
    n = 0
    pats = []
    for ps in cr.configs(src, i=src["s"], L=1, picked=()):
        n += 1
        pats.append([[p["i"], p["z"], list(p["parts"]), p["selected"], p["A"], p["L"]]
                     for p in ps])
    return n, pats


def parent_control(src):
    C = cf.Closure(src)
    res = C.run()
    return {
        "n_full": len(res["full_outcomes"]),
        "full_outcomes": [[qstr(a), qstr(b)] for a, b in res["full_outcomes"]],
        "survivors": [[qstr(a), qstr(b)] for a, b in res["survivors"]],
        "n_survivors": len(res["survivors"]),
    }


def main():
    rows = {json.loads(l)["row_id"]: json.loads(l) for l in ROSTER.open()}
    targets = {
        "R063": F(19),
        "R009": F(8),
        "R050": F(8),
    }
    out = {
        "schema": "jc2.r063-child-printed-closure/v1",
        "type": "DATA",
        "calculus": {
            "descend_own": "box/lib/descend_own.py",
            "patterns": "box/exact-contact-gate-20260906/closure_fixed.py:patterns",
            "node": "EllClosure = closure_fixed.Closure.node with 1->1+ell",
            "actual_L_walker": "box/exact-contact-gate-20260906/census_replay.py:configs",
            "shift": "Xu Lemma 4.1 -c t^{-ell-2}; Moh Prop 4.6(3)*; ell=v_s-u_s-1",
        },
        "parent_I_M_targets": {"R063": "19", "R009": "8", "R050": "8"},
        "rows": {},
    }
    for rid, parent_IM in targets.items():
        src = rows[rid]["source"]
        D = descend_own(Src(src))
        assert D["route_state"] == "NONEMPTY"
        assert D["descent_license"] == "DETERMINED_PROP6.4"
        assert len(D["V_vectors"]) == 1
        vec = tuple(exact_int(x) for x in D["V_vectors"][0])
        ell = int(D["ell"])
        assert ell == exact_int(D["vs"]) - exact_int(D["us"]) - 1
        parent = parent_control(src)
        rec = {
            "row_id": rid,
            "parent": {
                "n": src["n"], "m": src["m"], "s": src["s"],
                "u_s": src["u_s"], "v_s": src["v_s"],
                "M": src["M"], "d": src["d"], "V": src["V"],
                "delta": src["delta"],
                "printed_closure": parent,
                "target_I_M": qstr(parent_IM),
            },
            "child": {
                "n": int(D["n"]), "m": int(D["m"]), "s": int(D["s"]),
                "ell": ell, "us_parent": int(D["us"]), "vs_parent": int(D["vs"]),
                "M": {str(i): int(D["M"][i]) for i in D["M"]},
                "d": {str(i): int(D["d"][i]) for i in D["d"]},
                "V": list(vec),
                "license": D["descent_license"],
                "top_license": D["top_license"],
                "route_state": D["route_state"],
                "V_type": D["V_type"],
                "dropped": bool(D["dropped"]),
                "radii_agree": all(
                    r.get("effective_formula_agrees") is True
                    for r in D.get("child_radii") or []
                    if "effective_formula_agrees" in r
                ),
            },
            "conventions": {},
        }
        for ell_c, name in ((0, "unshifted"), (ell, "shifted")):
            crow, delta, V, M, d = child_source(D, vec, ell_c)
            rec["child"][f"delta_{name}"] = {str(i): qstr(delta[i]) for i in delta}
            rec["child"][f"u_s_{name}"] = crow["u_s"]
            block = run_child_convention(crow, ell_c, parent_IM)
            n_cr, pats_cr = census_actual_L_count(crow)
            block["census_replay_actual_L_n"] = n_cr
            block["census_replay_actual_L_patterns"] = pats_cr
            rec["conventions"][name] = block
        out["rows"][rid] = rec
        print(
            rid,
            "parent_printed", parent,
            "child", rec["child"]["n"], rec["child"]["m"], rec["child"]["s"],
            "ell", ell, "V", vec,
            "unshifted_complete", rec["conventions"]["unshifted"]["complete_I_M"],
            "unshifted_ungated", rec["conventions"]["unshifted"]["ungated_I_M"],
            "shifted_complete", rec["conventions"]["shifted"]["complete_I_M"],
            "shifted_ungated", rec["conventions"]["shifted"]["ungated_I_M"],
            flush=True,
        )

    out["summary"] = {
        rid: {
            "parent_printed_complete_N": rec["parent"]["printed_closure"]["n_full"],
            "parent_printed_survivors": rec["parent"]["printed_closure"]["survivors"],
            "parent_target_I_M": rec["parent"]["target_I_M"],
            "child_n_m_s_ell_V": [
                rec["child"]["n"], rec["child"]["m"], rec["child"]["s"],
                rec["child"]["ell"], rec["child"]["V"],
            ],
            "unshifted": {
                "n_selected_paths": rec["conventions"]["unshifted"]["n_selected_pattern_paths"],
                "complete_I_M": rec["conventions"]["unshifted"]["complete_I_M"],
                "ungated_I_M": rec["conventions"]["unshifted"]["ungated_I_M"],
                "equals_parent_complete": rec["conventions"]["unshifted"]["any_complete_equals_parent"],
                "equals_parent_ungated": rec["conventions"]["unshifted"]["any_ungated_equals_parent"],
                "has_71_4_complete": rec["conventions"]["unshifted"]["any_complete_is_71_4"],
                "has_71_4_ungated": rec["conventions"]["unshifted"]["any_ungated_is_71_4"],
                "complete_pairs": rec["conventions"]["unshifted"]["complete_pairs"],
                "ungated_pairs": rec["conventions"]["unshifted"]["ungated_pairs"],
            },
            "shifted": {
                "n_selected_paths": rec["conventions"]["shifted"]["n_selected_pattern_paths"],
                "complete_I_M": rec["conventions"]["shifted"]["complete_I_M"],
                "ungated_I_M": rec["conventions"]["shifted"]["ungated_I_M"],
                "equals_parent_complete": rec["conventions"]["shifted"]["any_complete_equals_parent"],
                "equals_parent_ungated": rec["conventions"]["shifted"]["any_ungated_equals_parent"],
                "has_71_4_complete": rec["conventions"]["shifted"]["any_complete_is_71_4"],
                "has_71_4_ungated": rec["conventions"]["shifted"]["any_ungated_is_71_4"],
                "complete_pairs": rec["conventions"]["shifted"]["complete_pairs"],
                "ungated_pairs": rec["conventions"]["shifted"]["ungated_pairs"],
                "d1_ungated": rec["conventions"]["shifted"]["d1_ungated"],
            },
        }
        for rid, rec in out["rows"].items()
    }

    path = HERE / "r063-child.json"
    text = json.dumps(ser(out), indent=2, sort_keys=True) + "\n"
    path.write_text(text)
    print("wrote", path, "bytes", len(text.encode()), flush=True)


if __name__ == "__main__":
    main()
