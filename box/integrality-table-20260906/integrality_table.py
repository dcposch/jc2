#!/usr/bin/env python3
"""Corrected integrality table under the printed fixed-list closure.

Reuses the hostile-gate calculus in box/exact-contact-gate-20260906/
(census_replay.patterns/flat_eval and closure_fixed.Closure.node formulas,
patterns(), partitions()). Does not rewrite those identities. Counts trees
with multiplicity; the gate's Closure.node returns unique (I_M, I_m) sets.

I_M is the complete final-major sum (Xu Thm 5.1). A truncated sibling sum is
not that quantity. I_m is the unsplit minor floor (not attainment).
A configuration is not a polynomial pair.
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from math import lcm
from pathlib import Path

GATE = Path(__file__).resolve().parents[1] / "exact-contact-gate-20260906"
sys.path.insert(0, str(GATE))
import census_replay as cr  # noqa: E402
import closure_fixed as cf  # noqa: E402

OUT = Path(__file__).resolve().parent
KNOWN = json.loads((GATE / "closure-fixed-results.json").read_text())

def _roster_path():
    candidates = [
        Path("/tmp/jc2-lane.IaL1Mu/inputs/roster.jsonl"),
        Path("/tmp/jc2-lane.QKyQBy/inputs/roster.jsonl"),
        Path(__file__).resolve().parents[1] / "residual66-20260905" / "roster.jsonl",
    ]
    for p in candidates:
        if p.is_file():
            return p
    raise FileNotFoundError("roster.jsonl")

_ROSTER = _roster_path()
cr.INPUT = _ROSTER
cf.ROWS = {r["row_id"]: r["source"] for r in map(json.loads, _ROSTER.read_text().splitlines())}


def ser(x):
    if isinstance(x, F):
        return str(x)
    if isinstance(x, dict):
        return {str(k): ser(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [ser(v) for v in x]
    return x


def pairkey(im, mn):
    return (str(im), str(mn))


class CountingClosure(cf.Closure):
    """Same node arithmetic as cf.Closure.node; Counter instead of a set; no log."""

    @lru_cache(None)
    def counted(self, i, rho, kappa, L, selected_path=False):
        n, m = self.n, self.m
        W = n - self.M[i]
        delta = 1 - F(W) * kappa / (W * rho - m)
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
            return Counter({(J, F(0)): 1}) if good else Counter()
        P = F(rho * self.d[i], m)
        Q = F(rho * W, m)
        if P.denominator > 1 or Q.denominator > 1:
            return Counter()
        threshold = F(self.d[i], W)
        allvals = Counter()
        selected = self.V[i] if selected_path else None
        for z, part in cf.patterns(int(P), int(Q), A, threshold, selected):
            factors = ([(z, 1, "zero")] if z else []) + [(x, A, "orbit") for x in part]
            vals = Counter({(F(0), F(0)): 1})
            sel_used = False
            for r, count, typ in factors:
                crho = F(m * r, self.d[i])
                ck = crho * (1 - delta) - lam
                assert crho.denominator == 1
                crho = int(crho)
                if ck < 0:
                    cv = Counter({(F(0), -ck / crho): 1})
                else:
                    use_sel = selected_path and r == self.V[i] and not sel_used
                    if use_sel:
                        sel_used = True
                    childL = L if typ == "zero" else lcm(L, delta.denominator)
                    cv = self.counted(i - 1, crho, ck, childL, use_sel)
                if not cv:
                    vals = Counter()
                    break
                new = Counter()
                for (a, b), na in vals.items():
                    for (c, d), nc in cv.items():
                        new[(a + count * c, b + count * d)] += na * nc
                vals = new
            allvals += vals
        return allvals

    def run_counted(self):
        rho = F(self.m * self.row["v_s"], self.d[self.s])
        kappa = 2 * rho - self.m
        assert rho.denominator == 1
        vals = self.counted(self.s - 1, int(rho), kappa, 1, True)
        minor_base = F(self.row["v_s"], self.row["u_s"])
        out = Counter()
        for (im, mn), c in vals.items():
            out[(im, minor_base + mn)] += c
        return minor_base, out


def summarize(counter):
    n = sum(counter.values())
    n_int = sum(c for (im, mn), c in counter.items() if im.denominator == 1)
    n_ge = sum(c for (im, mn), c in counter.items() if im >= mn)
    n_surv = sum(
        c for (im, mn), c in counter.items() if im.denominator == 1 and im >= mn
    )
    pairs = sorted(counter, key=lambda t: (t[0], t[1]))
    surv = [(im, mn) for im, mn in pairs if im.denominator == 1 and im >= mn]
    integral = [(im, mn) for im, mn in pairs if im.denominator == 1]
    return {
        "n_complete": n,
        "n_integral": n_int,
        "n_IM_ge_Im": n_ge,
        "n_survive": n_surv,
        "n_distinct_pairs": len(pairs),
        "n_distinct_survivors": len(surv),
        "pairs": [
            {
                "I_M": str(im),
                "I_m": str(mn),
                "count": counter[(im, mn)],
                "integral": im.denominator == 1,
                "IM_ge_Im": im >= mn,
                "thm51": "PASS" if im.denominator == 1 else "FAIL_nonintegral",
                "cor53": "PASS" if im >= mn else "FAIL_below",
            }
            for im, mn in pairs
        ],
        "survivor_pairs": [[str(im), str(mn)] for im, mn in surv],
        "integral_pairs": [[str(im), str(mn)] for im, mn in integral],
    }


def complete_premature(src, ps, C):
    """Complete one census config: keep the selected tower; continue every
    off-tower major born at level >= 3 by cf.Closure arithmetic at i-1."""
    n, m, s = src["n"], src["m"], src["s"]
    d, M, V = src["d"], src["M"], src["V"]
    delta = list(map(F, src["delta"]))
    by_i = {p["i"]: p for p in ps}

    def combine(fixed_IM, fixed_Im, pieces):
        acc = Counter({(fixed_IM, fixed_Im): 1})
        for num, cv in pieces:
            if not cv:
                return Counter()
            new = Counter()
            for (a, b), na in acc.items():
                for (c, d), nc in cv.items():
                    new[(a + num * c, b + num * d)] += na * nc
            acc = new
        return acc

    def eval_selected(i):
        p = by_i[i]
        groups = ([(p["z"], 1, "zero")] if p["z"] else []) + [
            (r, p["A"], "nonzero") for r in p["parts"]
        ]
        fixed_IM, fixed_Im = F(0), F(0)
        pieces = []
        consumed = False
        for r, num, kind in groups:
            rho = F(m * r, d[i - 1])
            assert rho.denominator == 1
            rho = int(rho)
            lamabs = F(m) * (1 - delta[i - 1]) / F(n - M[i - 1])
            kappa = rho * (1 - delta[i - 1]) - lamabs
            is_selected = r == p["V"] and kind == p["selected"] and not consumed
            if is_selected:
                consumed = True
            childL = p["L"] if kind == "zero" else lcm(p["L"], delta[i - 1].denominator)
            if is_selected:
                if i == 2:
                    pieces.append((num, C.counted(1, rho, kappa, childL, True)))
                else:
                    pieces.append((num, eval_selected(i - 1)))
            elif kappa > 0:
                if i == 2:
                    pieces.append((num, C.counted(1, rho, kappa, childL, False)))
                else:
                    pieces.append((num, C.counted(i - 1, rho, kappa, childL, False)))
            else:
                assert kappa < 0
                fixed_Im += num * (-kappa / rho)
        assert consumed
        return combine(fixed_IM, fixed_Im, pieces)

    vals = eval_selected(s - 1)
    base = F(V[-1], src["u_s"])
    out = Counter()
    for (im, mn), c in vals.items():
        out[(im, mn + base)] += c
    return out


def main():
    rows = cr.read_rows()
    assert [r["row_id"] for r in rows] == [f"R{i:03}" for i in range(1, 67)]

    table = []
    genuine_kills = []
    checks = {
        "target_pairset_matches_gate": {},
        "R009_R050_unique_8": None,
        "R001_zero_survivors": None,
    }

    for row in rows:
        rid = row["row_id"]
        src = row["source"]
        C = CountingClosure(src)
        minor_base, counter = C.run_counted()
        rec = summarize(counter)
        rec.update(
            {
                "row_id": rid,
                "n": src["n"],
                "m": src["m"],
                "s": src["s"],
                "minor_base": str(minor_base),
                "finite_major_levels": src["s"] - 1,
            }
        )
        if rec["n_survive"] == 0:
            genuine_kills.append(rid)
            rec["zero_survivors"] = True
        else:
            rec["zero_survivors"] = False
        table.append(rec)

        if rid in KNOWN:
            gate_surv = {(F(a), F(b)) for a, b in KNOWN[rid]["survivors"]}
            mine = {(F(a), F(b)) for a, b in rec["survivor_pairs"]}
            gate_full = {(F(a), F(b)) for a, b in KNOWN[rid]["full_outcomes"]}
            mine_full = {(F(p["I_M"]), F(p["I_m"])) for p in rec["pairs"]}
            checks["target_pairset_matches_gate"][rid] = {
                "survivors": gate_surv == mine,
                "full_outcomes": gate_full == mine_full,
                "gate_survivors": ser(sorted(gate_surv)),
                "mine_survivors": rec["survivor_pairs"],
            }
            assert gate_surv == mine, (rid, gate_surv, mine)
            assert gate_full == mine_full, (rid, gate_full, mine_full)

    r009 = next(r for r in table if r["row_id"] == "R009")
    r050 = next(r for r in table if r["row_id"] == "R050")
    r001 = next(r for r in table if r["row_id"] == "R001")
    checks["R009_R050_unique_8"] = (
        r009["n_survive"] == 1
        and r050["n_survive"] == 1
        and r009["survivor_pairs"] == [["8", "8"]]
        and r050["survivor_pairs"] == [["8", "8"]]
        and r009["n_distinct_survivors"] == 1
        and r050["n_distinct_survivors"] == 1
    )
    checks["R001_zero_survivors"] = r001["n_survive"] == 0 and r001["pairs"] == [
        {
            "I_M": "4",
            "I_m": "5",
            "count": 1,
            "integral": True,
            "IM_ge_Im": False,
            "thm51": "PASS",
            "cor53": "FAIL_below",
        }
    ]
    assert checks["R009_R050_unique_8"]
    assert r001["n_survive"] == 0

    # Identify the 19 premature flat exclusions and complete them.
    premature = []
    for row in rows:
        src = row["source"]
        C = CountingClosure(src)
        for j, ps in enumerate(cr.census_configs(src)):
            e = cr.flat_eval(src, ps, "selected")
            IM, Im = e["IM_flat"], e["Im_unsplit"]
            flags = [IM.denominator != 1, IM < Im, IM.denominator != 1 and IM >= Im]
            upper = [s for s in e["major_siblings"] if s["level"] >= 3]
            if not (flags[2] and upper):
                continue
            closed = complete_premature(src, ps, C)
            summ = summarize(closed)
            premature.append(
                {
                    "row_id": row["row_id"],
                    "census_index": j,
                    "patterns": [
                        [p["i"], p["z"], list(p["parts"]), p["selected"]] for p in ps
                    ],
                    "IM_flat": str(IM),
                    "Im_unsplit_flat": str(Im),
                    "upper_siblings": [
                        {
                            "level": s["level"],
                            "multiplicity": s["multiplicity"],
                            "count": s["count"],
                            "rho": s["rho"],
                            "kappa": str(s["kappa"]),
                            "L": s["L"],
                            "kind": s["kind"],
                            "J_truncated": str(s["J"]),
                        }
                        for s in upper
                    ],
                    "corrected": summ,
                    "status": (
                        "SURVIVES_AFTER_COMPLETION"
                        if summ["n_survive"]
                        else (
                            "COMPLETE_BUT_NO_SURVIVOR"
                            if summ["n_complete"]
                            else "NO_GALOIS_COMPLETION"
                        )
                    ),
                }
            )
    assert len(premature) == 19, len(premature)

    n_rows_surv = sum(1 for r in table if r["n_survive"] > 0)
    n_rows_complete = sum(1 for r in table if r["n_complete"] > 0)
    compact_rows = []
    for r in table:
        compact_rows.append(
            {
                "row_id": r["row_id"],
                "n_complete": r["n_complete"],
                "n_integral": r["n_integral"],
                "n_IM_ge_Im": r["n_IM_ge_Im"],
                "n_survive": r["n_survive"],
                "zero_survivors": r["zero_survivors"],
                "survivor_pairs": r["survivor_pairs"],
                "n_distinct_pairs": r["n_distinct_pairs"],
            }
        )

    # Drop bulky pair lists from the 66-row block except when small or a kill.
    rows_out = []
    for r in table:
        item = {
            k: r[k]
            for k in (
                "row_id",
                "n",
                "m",
                "s",
                "minor_base",
                "finite_major_levels",
                "n_complete",
                "n_integral",
                "n_IM_ge_Im",
                "n_survive",
                "n_distinct_pairs",
                "n_distinct_survivors",
                "zero_survivors",
                "survivor_pairs",
            )
        }
        if r["n_distinct_pairs"] <= 12 or r["zero_survivors"] or r["row_id"] in {
            "R001",
            "R009",
            "R050",
            "R025",
            "R026",
            "R027",
            "R028",
            "R057",
            "R058",
        }:
            item["pairs"] = r["pairs"]
        rows_out.append(item)

    out = {
        "schema": "jc2.integrality-table-printed-closure/v1",
        "calculus": "box/exact-contact-gate-20260906/{census_replay.py,closure_fixed.py}",
        "printed": {
            "I_def": "Xu §2: I(f_xi,g)=deg_x Res_y(f_xi,g) in Z",
            "Thm_5_1": "Xu p.7: I(f_xi,g)=I_M for a Jacobian pair",
            "Cor_5_3": "I_M >= I_m (unsplit minor is a floor)",
            "closure": "Moh Def 5.1(4) p.179; Prop 5.3 p.180; D1 final by Prop 4.6 p.170",
        },
        "fallacy_v2": "A truncated sum is not the resultant degree. A configuration is not a pair. I_m_unsplit is a floor.",
        "checks": checks,
        "totals": {
            "rows": 66,
            "rows_with_a_complete_config": n_rows_complete,
            "rows_with_a_survivor": n_rows_surv,
            "genuine_kills_zero_survivors": genuine_kills,
            "premature_flat_exclusions": 19,
            "complete_configurations": sum(r["n_complete"] for r in table),
            "integral_configurations": sum(r["n_integral"] for r in table),
            "surviving_configurations": sum(r["n_survive"] for r in table),
        },
        "rows": rows_out,
        "premature_19": premature,
        "compact": compact_rows,
    }
    path = OUT / "integrality-table.json"
    path.write_text(json.dumps(ser(out), separators=(",", ":")) + "\n")
    print(
        json.dumps(
            {
                "json_bytes": path.stat().st_size,
                "totals": out["totals"],
                "R009": {k: r009[k] for k in ("n_complete", "n_integral", "n_survive", "survivor_pairs", "pairs")},
                "R050": {k: r050[k] for k in ("n_complete", "n_integral", "n_survive", "survivor_pairs", "pairs")},
                "R001": {k: r001[k] for k in ("n_complete", "n_integral", "n_survive", "pairs")},
                "premature_status": [
                    (p["row_id"], p["census_index"], p["IM_flat"], p["status"], p["corrected"]["n_complete"], p["corrected"]["n_survive"], p["corrected"]["survivor_pairs"][:6])
                    for p in premature
                ],
                "kills": genuine_kills,
                "target_checks": checks["target_pairset_matches_gate"],
            },
            default=str,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
