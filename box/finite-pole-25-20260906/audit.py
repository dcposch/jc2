#!/usr/bin/env python3
"""Replay the 25 finite-pole rows through charged descend_own / own_v_routes.

DATA audit only. A necessary configuration is not a polynomial pair.
An empty V' set is kept empty. Prop 5.3 carry is checked on every
above-average packet of the returned source-tree witness.
"""
from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
sys.dont_write_bytecode = True

from box.lib.descend_own import descend_own  # noqa: E402

FP_IDS = [
    "E0022", "E0053", "E0097", "E0120", "E0127",
    "E0301", "E0344", "E0354", "E0355", "E0383",
    "E0415", "E0452", "E0467", "E0468", "E0475",
    "E0483", "E0489", "E0608", "E0724", "E0771",
    "E0773", "E0939", "E0946", "E1263", "E1279",
]

CLAUSE = (
    "descend_own.py:142-144 dropped=(raw_M[s-1]==n'-1); "
    "196-209 PROP6.3_FINITE_POLE obstruction wipes choices; "
    "262-265 route_state=EMPTY_PROP6.3_FINITE_POLE; "
    "256-258 top_license=NO_CHILD_PROP6.3_FINITE_POLE; "
    "build_roster.py:195 live iff V_vectors nonempty; "
    "chart_counts.py:1492 route_state==NONEMPTY; "
    "roster.jsonl provenance.own_route_state"
)
PRINTED = (
    "Moh Prop 4.6 p.170: T_{s-1,initial}=p^A q, q squarefree of degree "
    "V_s*(n-M_{s-1})/d_s; Prop 6.3(1)(2) p.197: T_{s-1}(sigma) monic in "
    "pi over k[gamma]; Prop 6.4 p.198-199 licenses u_s=1. "
    "Code comment descend_own.py:196-201."
)


class Src:
    def __init__(self, n, m, Ms, V):
        self.n = int(n)
        self.m = int(m)
        full = [-self.m] + list(Ms)
        self.s = len(full)
        self.M = {i + 1: int(full[i]) for i in range(self.s)}
        self.V = {2 + i: int(V[i]) for i in range(len(V))}


def ser(x):
    if isinstance(x, Q):
        return (
            f"{x.numerator}/{x.denominator}"
            if x.denominator != 1
            else str(x.numerator)
        )
    if isinstance(x, dict):
        return {str(k): ser(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [ser(v) for v in x]
    return x


def witness_nodes(w, dd, n, MM, out):
    if not w or "j" not in w:
        return
    j = w["j"]
    lo = Q(dd[j], n - MM[j])
    z = w["z"]
    orbits = list(w.get("orbits") or ())
    packets = []
    if z:
        packets.append({"kind": "zero", "r": int(z), "major": bool(Q(z) > lo)})
    for r in orbits:
        packets.append(
            {"kind": "nonzero", "r": int(r), "major": bool(Q(r) > lo)}
        )
    out.append(
        {
            "j": j,
            "delta": ser(w.get("delta")),
            "P": int(w["P"]),
            "Q": int(w["Q"]),
            "A": int(w["A"]),
            "z": int(z),
            "orbits": [int(r) for r in orbits],
            "mode": w.get("mode"),
            "lo": ser(lo),
            "packets": packets,
            "zero_major_child": w.get("zero_major_child") is not None,
            "nonzero_major_children": sorted(
                int(k) for k in (w.get("nonzero_major_children") or {})
            ),
        }
    )
    sc = w.get("selected_child")
    if isinstance(sc, dict) and "j" in sc:
        witness_nodes(sc, dd, n, MM, out)


def majors_carried(w, dd, n, MM):
    notes = []

    def rec(node):
        if not node or "j" not in node:
            return
        j = node["j"]
        lo = Q(dd[j], n - MM[j])
        z = node["z"]
        if z and Q(z) > lo and node.get("zero_major_child") is None:
            notes.append(f"j={j} zero r={z} missing carry")
        kids = node.get("nonzero_major_children") or {}
        for r in set(node.get("orbits") or ()):
            if Q(r) > lo and (r not in kids or kids[r] is None):
                notes.append(f"j={j} nonzero r={r} missing carry")
        sc = node.get("selected_child")
        if isinstance(sc, dict) and "j" in sc:
            rec(sc)

    rec(w)
    return (not notes), notes


def audit_row(eid, rec):
    src = Src(rec["n"], rec["m"], rec["Ms"], rec["V"])
    res = descend_own(src)
    n, s = src.n, src.s
    dd = {int(k): int(v) for k, v in res["source"]["d"].items()}
    MM = {int(k): int(v) for k, v in res["source"]["M"].items()}
    VV = {int(k): int(v) for k, v in res["source"]["V"].items()}
    delta = {int(k): v for k, v in res["source"]["delta"].items()}
    rlev = s - 1
    P = VV[s] * dd[rlev] // dd[s]
    Qv = VV[s] * (n - MM[rlev]) // dd[s]
    lo = Q(dd[rlev], n - MM[rlev])
    zsel = VV[rlev]
    rem = P - zsel
    mu = {int(k): int(v) for k, v in res["source_mu"].items()}
    p_exp = (-mu[rlev] + MM[rlev] - n) // dd[rlev]
    wit = None
    if res["full_source_routes"]:
        wit = res["full_source_routes"][0].get("source_tree_witness")
    nodes = []
    if wit:
        witness_nodes(wit, dd, n, MM, nodes)
    carried, notes = (False, ["no witness"])
    if wit:
        carried, notes = majors_carried(wit, dd, n, MM)
    sm1_unselected_majors = []
    if nodes:
        sm1_unselected_majors = [
            p for p in nodes[0]["packets"]
            if p["kind"] != "zero" and p["major"]
        ]
    classification = "a"
    # (a) child Prop 6.3(1)(2) pole, not an empty first-support set and
    # not a packet-depth termination. Prop 5.3 is recorded, not a reopen.
    if not carried:
        verdict = "OPEN[PREMATURE-CLOSURE]"
    else:
        verdict = "STANDS"
    return {
        "id": eid,
        "n": n,
        "m": rec["m"],
        "s": s,
        "M": [-rec["m"]] + list(rec["Ms"]),
        "d": [dd[i] for i in range(1, s + 2)],
        "V": list(rec["V"]),
        "delta": {str(i): ser(delta[i]) for i in range(1, s + 1)},
        "us": res["us"],
        "vs": res["vs"],
        "ds": res["ds"],
        "ell": res["ell"],
        "n_prime": res["n"],
        "m_prime": res["m"],
        "s_prime": res["s"],
        "raw_M_sminus1": int(res["raw_M"][s - 1]),
        "np_minus_1": res["n"] - 1,
        "dropped": bool(res["dropped"]),
        "route_state": res["route_state"],
        "top_license": res["top_license"],
        "outer_routes": len(res["outer_routes"]),
        "full_source_routes": len(res["full_source_routes"]),
        "routes_after_obstruction": len(res["routes"]),
        "rejected_first_support": list(res["source_tree_rejected_first_support"]),
        "outer_V": [[ser(x) for x in t] for t in res["outer_V_vectors"]],
        "V_vectors": [[ser(x) for x in t] for t in res["V_vectors"]],
        "first_nonzero": [c["first_nonzero"] for c in res["outer_routes"]],
        "obstruction": ser(res["licensed_obstructions"][0])
        if res["licensed_obstructions"]
        else None,
        "sm1": {
            "i": rlev,
            "delta": ser(delta[rlev]),
            "P": P,
            "Q": Qv,
            "lo": ser(lo),
            "selected_V": zsel,
            "selected_major": bool(Q(zsel) > lo),
            "remaining_p_degree": rem,
            "remaining_gt_lo": bool(rem > lo),
        },
        "q_degree": Qv,
        "p_exponent": p_exp,
        "witness_nodes": nodes,
        "sm1_unselected_majors_in_witness": sm1_unselected_majors,
        "prop53_every_above_average_packet_carried": carried,
        "prop53_notes": notes,
        "in_roster": False,
        "roster_field": "actual_rows.roster=null; absent from roster.jsonl",
        "removal_clause": CLAUSE,
        "printed_line": PRINTED,
        "classification": classification,
        "classification_label": (
            "(a) own-V' contradiction at the child: Prop 6.3(1)(2) "
            "monicity of T_{s-1}(sigma) in k[gamma][pi]"
        ),
        "verdict": verdict,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--census",
        type=Path,
        default=ROOT / "box/actual-stabilizer-census-20260906/actual-stab-census.json",
    )
    parser.add_argument(
        "--roster",
        type=Path,
        default=ROOT / "box/residual66-20260905/roster.jsonl",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parent / "finite-pole-25-audit.json",
    )
    args = parser.parse_args()
    census = json.loads(args.census.read_text(encoding="utf-8"))
    by = {r["id"]: r for r in census["actual_rows"]}
    missing = [i for i in FP_IDS if i not in by]
    if missing:
        raise SystemExit(f"missing actual_rows: {missing}")
    roster_keys = set()
    for line in args.roster.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        src = row["source"]
        roster_keys.add(
            (src["n"], src["m"], tuple(src["M"]), tuple(src["V"]))
        )
    rows = []
    for eid in FP_IDS:
        rec = by[eid]
        if rec.get("roster") is not None:
            raise SystemExit(f"{eid} has roster id {rec['roster']}")
        out = audit_row(eid, rec)
        key = (out["n"], out["m"], tuple(out["M"]), tuple(out["V"]))
        out["in_roster"] = key in roster_keys
        if out["in_roster"]:
            raise SystemExit(f"{eid} unexpectedly in roster.jsonl")
        if out["route_state"] != "EMPTY_PROP6.3_FINITE_POLE":
            raise SystemExit(f"{eid} route_state={out['route_state']}")
        if out["full_source_routes"] != 1 or out["routes_after_obstruction"] != 0:
            raise SystemExit(f"{eid} route counts drifted")
        if not out["dropped"] or out["us"] != 1:
            raise SystemExit(f"{eid} dropped/us drifted")
        rows.append(out)
    stands = sum(r["verdict"] == "STANDS" for r in rows)
    open_pc = sum(r["verdict"] == "OPEN[PREMATURE-CLOSURE]" for r in rows)
    payload = {
        "schema": "jc2.finite-pole-25-audit/v1",
        "semantic_type": "NECESSARY_TOWER_CONFIGURATION_NOT_POLYNOMIAL_PAIR",
        "type": "DATA",
        "driver": "box/finite-pole-25-20260906/audit.py",
        "uniform_removal_clause": CLAUSE,
        "printed_line": PRINTED,
        "classification_all": "a",
        "prop53_rule": (
            "Moh Prop 5.3 p.180: every above-average p-factor is carried "
            "to the next prescribed disc. Replay: OwnVRouteTree witness "
            "zero_major_child / nonzero_major_children on every r>lo packet."
        ),
        "counts": {
            "rows": 25,
            "STANDS": stands,
            "OPEN[PREMATURE-CLOSURE]": open_pc,
            "OPEN[other]": 25 - stands - open_pc,
            "in_roster": sum(r["in_roster"] for r in rows),
        },
        "rows": rows,
    }
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "output": str(args.output),
                "bytes": args.output.stat().st_size,
                **payload["counts"],
            }
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
