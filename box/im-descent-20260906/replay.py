#!/usr/bin/env python3
"""Replay OPEN 3: I'_M vs I_M under Prop 6.3 on the 46 complete u_s=1 rows.

Does not rewrite the packet calculus.  Parent I_M: exact_contact.tower / all_flat.
Child I'_M: child_xu.child_tower / evaluate, with licensed own data from
box.lib.descend_own (not the roster's single own_child representative).
"""
from __future__ import annotations

import importlib.util
import json
import os
import sys
import time
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path("/home/ubuntu/jc2")
HERE = Path(__file__).resolve().parent
LANE_INPUTS = Path("/tmp/jc2-lane.MIFdbX/inputs")
ROSTER = LANE_INPUTS / "roster.jsonl"
EC_DIR = ROOT / "box" / "exact-contact-20260906"

sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(EC_DIR))
sys.dont_write_bytecode = True

from box.lib.descend_own import descend_own, exact_int  # noqa: E402
from exact_contact import all_flat, tower  # noqa: E402

_spec = importlib.util.spec_from_file_location("child_xu", EC_DIR / "child_xu.py")
child_xu = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(child_xu)
from exact_contact import patterns  # noqa: E402


class Src:
    """Minimal source object for descend_own / OwnVRouteTree."""

    def __init__(self, source: dict):
        self.n = source["n"]
        self.m = source["m"]
        self.s = source["s"]
        self.M = {i + 1: source["M"][i] for i in range(self.s)}
        self.V = {i + 2: source["V"][i] for i in range(len(source["V"]))}


def qstr(x) -> str:
    x = Q(x)
    return str(x.numerator) if x.denominator == 1 else str(x)


def pat_str(pat: dict) -> str:
    if not pat:
        return "(none)"
    parts = []
    for i in sorted(pat):
        z, o, ix = pat[i]
        o = list(o) if not isinstance(o, list) else o
        parts.append(f"{i}:z{z}/{o}/s{ix}")
    return ";".join(parts)


def child_configs(T):
    """Same enumeration as child_xu.__main__, returning dicts."""
    levels = list(range(T["s"], 1, -1))
    opts = []
    for i in levels:
        cand = []
        for p in patterns(T["P"][i], T["Qd"][i], T["A"][i], T["V"][i], T["lo"][i]):
            cl = ([p["z"]] if p["z"] > 0 else []) + list(p["orbits"])
            for ix, c in enumerate(cl):
                if c == T["V"][i]:
                    cand.append((p, ix))
        opts.append(cand)
    seen = set()
    out = []
    import itertools
    for combo in itertools.product(*opts) if opts else [()]:
        ch = {i: c[0] for i, c in zip(levels, combo)}
        sl = {i: c[1] for i, c in zip(levels, combo)}
        r = child_xu.evaluate(T, ch, sl)
        if r is None:
            continue
        key = (r["IM"], tuple(r["leaves"]))
        if key in seen:
            continue
        seen.add(key)
        pat = {i: (c[0]["z"], c[0]["orbits"], c[1]) for i, c in zip(levels, combo)}
        nmaj = sum(1 for L in r["leaves"] if "MAJOR-SIB" in L)
        out.append(dict(
            pattern={str(i): [z, list(o), ix] for i, (z, o, ix) in pat.items()},
            pattern_str=pat_str(pat),
            IM=r["IM"],
            IM_integral=(r["IM"].denominator == 1),
            n_major_sib=nmaj,
            n_minor=len(r["minor"]),
        ))
    return out


def oc_from_own(D, vec):
    s = D["s"]
    return dict(
        n_prime=int(D["n"]),
        m_prime=int(D["m"]),
        s_prime=int(s),
        M_prime=[int(D["M"][i]) for i in range(1, s + 1)],
        d_prime=[int(D["d"][i]) for i in range(1, s + 2)],
        V_prime=[exact_int(x) for x in vec],
        ell=int(D["ell"]),
    )


def parent_record(row):
    T = tower(row["source"])
    cfgs = []
    for r in all_flat(T):
        nmaj = sum(1 for L in r["leaves"] if L["kind"] == "major-sibling")
        cfgs.append(dict(
            pattern={str(i): [z, list(o), ix] for i, (z, o, ix) in r["pattern"].items()},
            pattern_str=pat_str(r["pattern"]),
            IM=r["IM"],
            Im=r["Im"],
            IM_integral=(r["IM"].denominator == 1),
            IM_ge_Im=(r["IM"] >= r["Im"]),
            n_major_sib=nmaj,
        ))
    return dict(n=T["n"], m=T["m"], s=T["s"], configs=cfgs)


def classify_row(parent_cfgs, child_cfgs, child_state):
    """Three-way partition used in the report.

    Child undetermined: no licensed V, or no evaluable child pattern.
    Otherwise compare the *surviving* integer values (parent: I_M in Z and
    I_M >= I_m; child: I'_M in Z).  Non-integer sibling-major flats are
    tabulated but not used as the preservation test — they already differ
    on the charged R009/R050 examples that raised OPEN 3.
    """
    if child_state != "NONEMPTY" or not child_cfgs:
        return "child_undetermined"
    S = {c["IM"] for c in parent_cfgs if c["IM_integral"] and c["IM_ge_Im"]}
    Sp = {c["IM"] for c in child_cfgs if c["IM_integral"]}
    if S == Sp and S:
        return "equal_surviving"
    if not S and not Sp:
        return "both_empty_surviving"
    return "difference"


def main():
    t0 = time.monotonic()
    rows = [json.loads(l) for l in open(ROSTER)]
    assert len(rows) == 66

    parent_all = []
    ncfg = nnotint = nlt = nintalone = nsurv = 0
    for row in rows:
        rec = parent_record(row)
        rec["row_id"] = row["row_id"]
        rec["u_s"] = row["source"]["u_s"]
        parent_all.append(rec)
        for c in rec["configs"]:
            ncfg += 1
            if not c["IM_integral"]:
                nnotint += 1
                if c["IM_ge_Im"]:
                    nintalone += 1
            if not c["IM_ge_Im"]:
                nlt += 1
            if c["IM_integral"] and c["IM_ge_Im"]:
                nsurv += 1

    parent_counts = dict(
        n_rows=len(rows),
        n_configs=ncfg,
        n_IM_not_integral=nnotint,
        n_IM_lt_Im=nlt,
        n_killed_by_integrality_alone=nintalone,
        n_surviving_integral_ge=nsurv,
        matches_report_1080=(ncfg == 1080 and nnotint == 995
                             and nlt == 77 and nintalone == 924),
    )

    complete = [row for row in rows if row["source"]["u_s"] == 1]
    assert len(complete) == 46

    per_row = []
    buckets = Counter()
    for row in complete:
        rid = row["row_id"]
        src = row["source"]
        parent = next(p for p in parent_all if p["row_id"] == rid)
        try:
            D = descend_own(Src(src))
            child_err = None
        except Exception as e:  # noqa: BLE001 — record, do not fill
            D = None
            child_err = f"{type(e).__name__}: {e}"

        child_block = dict(
            error=child_err,
            license=None,
            top_license=None,
            route_state=None,
            V_type=None,
            V_vectors=[],
            n_prime=None,
            m_prime=None,
            s_prime=None,
            ell=None,
            dropped=None,
            radii_agree=None,
            roster_V_in_own=None,
            configs=[],
        )
        if D is not None:
            vecs = [tuple(exact_int(x) for x in v) for v in D["V_vectors"]]
            child_block.update(
                license=D["descent_license"],
                top_license=D["top_license"],
                route_state=D["route_state"],
                V_type=D["V_type"],
                V_vectors=vecs,
                n_prime=int(D["n"]),
                m_prime=int(D["m"]),
                s_prime=int(D["s"]),
                ell=int(D["ell"]),
                dropped=bool(D["dropped"]),
            )
            agrees = []
            for rec in D.get("child_radii") or []:
                if "effective_formula_agrees" in rec:
                    agrees.append(bool(rec["effective_formula_agrees"]))
            child_block["radii_agree"] = (all(agrees) if agrees else None)
            roster_V = tuple(row["own_child"]["V_prime"])
            child_block["roster_V_in_own"] = roster_V in vecs if vecs else False
            cfgs = []
            for vec in vecs:
                try:
                    oc = oc_from_own(D, vec)
                    T = child_xu.child_tower(oc, oc["ell"])
                    for c in child_configs(T):
                        c = dict(c)
                        c["V"] = list(vec)
                        c["delta"] = {str(i): qstr(T["delta"][i])
                                      for i in sorted(T["delta"])}
                        c["A"] = {str(i): T["A"][i] for i in sorted(T["A"])}
                        c["lo"] = {str(i): qstr(T["lo"][i])
                                   for i in sorted(T["lo"])}
                        cfgs.append(c)
                except Exception as e:  # noqa: BLE001
                    child_block["error"] = (
                        (child_block["error"] + " | " if child_block["error"] else "")
                        + f"V={vec} {type(e).__name__}: {e}"
                    )
            child_block["configs"] = cfgs

        parent_cfgs = parent["configs"]
        child_cfgs = child_block["configs"]
        state = (child_block["route_state"] if D is not None else "ERROR")
        bucket = classify_row(parent_cfgs, child_cfgs, state or "EMPTY")
        # both-empty-surviving is still a defined comparison of empty sets;
        # report it under difference so it is not silently counted as HOLDS.
        buckets[bucket] += 1

        S = sorted((c["IM"] for c in parent_cfgs
                    if c["IM_integral"] and c["IM_ge_Im"]), key=lambda x: (x.denominator, x))
        Sp = sorted((c["IM"] for c in child_cfgs if c["IM_integral"]),
                    key=lambda x: (x.denominator, x))
        Sset = sorted(set(S), key=lambda x: (x.denominator, x))
        Spset = sorted(set(Sp), key=lambda x: (x.denominator, x))
        allP = sorted(set(c["IM"] for c in parent_cfgs), key=lambda x: (x.denominator, x))
        allC = sorted(set(c["IM"] for c in child_cfgs), key=lambda x: (x.denominator, x))
        T1P = sorted(set(c["IM"] for c in parent_cfgs if c["n_major_sib"] == 0),
                     key=lambda x: (x.denominator, x))
        T1C = sorted(set(c["IM"] for c in child_cfgs if c["n_major_sib"] == 0),
                     key=lambda x: (x.denominator, x))
        T1P_int = sorted(set(c["IM"] for c in parent_cfgs
                             if c["n_major_sib"] == 0 and c["IM_integral"] and c["IM_ge_Im"]),
                         key=lambda x: (x.denominator, x))
        T1C_int = sorted(set(c["IM"] for c in child_cfgs
                             if c["n_major_sib"] == 0 and c["IM_integral"]),
                         key=lambda x: (x.denominator, x))

        per_row.append(dict(
            row_id=rid,
            n=src["n"], m=src["m"], s=src["s"], u_s=src["u_s"],
            parent_n_configs=len(parent_cfgs),
            parent_n_integral=sum(1 for c in parent_cfgs if c["IM_integral"]),
            parent_n_ge=sum(1 for c in parent_cfgs if c["IM_ge_Im"]),
            parent_n_surviving=len(S),
            parent_surviving_IM=[qstr(x) for x in Sset],
            parent_all_IM=[qstr(x) for x in allP],
            parent_T1_IM=[qstr(x) for x in T1P],
            parent_T1_surviving_IM=[qstr(x) for x in T1P_int],
            parent_configs=[dict(
                pattern=c["pattern_str"], IM=qstr(c["IM"]), Im=qstr(c["Im"]),
                integral=c["IM_integral"], ge=c["IM_ge_Im"],
                n_major_sib=c["n_major_sib"],
            ) for c in parent_cfgs],
            child=dict(
                error=child_block["error"],
                license=child_block["license"],
                top_license=child_block["top_license"],
                route_state=child_block["route_state"],
                V_type=child_block["V_type"],
                V_vectors=child_block["V_vectors"],
                n_prime=child_block["n_prime"],
                m_prime=child_block["m_prime"],
                s_prime=child_block["s_prime"],
                ell=child_block["ell"],
                dropped=child_block["dropped"],
                radii_agree=child_block["radii_agree"],
                roster_V_in_own=child_block["roster_V_in_own"],
                n_configs=len(child_cfgs),
                n_integral=sum(1 for c in child_cfgs if c["IM_integral"]),
                surviving_IM=[qstr(x) for x in Spset],
                all_IM=[qstr(x) for x in allC],
                T1_IM=[qstr(x) for x in T1C],
                T1_surviving_IM=[qstr(x) for x in T1C_int],
                configs=[dict(
                    V=c["V"], pattern=c["pattern_str"], IM=qstr(c["IM"]),
                    integral=c["IM_integral"], n_major_sib=c["n_major_sib"],
                    n_minor=c["n_minor"],
                    delta=c["delta"], A=c["A"], lo=c["lo"],
                ) for c in child_cfgs],
            ),
            bucket=bucket,
            surviving_sets_equal=(Sset == Spset and len(Sset) > 0),
            T1_surviving_equal=(T1P_int == T1C_int and len(T1P_int) > 0),
            all_values_equal=(allP == allC and len(allP) > 0),
        ))
        print(
            f"{rid} parent_cfg={len(parent_cfgs)} surv={list(map(qstr, Sset))} "
            f"child_state={state} V={vecs if D else None} "
            f"child_cfg={len(child_cfgs)} IMprime_surv={list(map(qstr, Spset))} "
            f"bucket={bucket} radii_agree={child_block['radii_agree']}",
            flush=True,
        )

    equal_rows = [r["row_id"] for r in per_row if r["bucket"] == "equal_surviving"]
    diff_rows = [r for r in per_row if r["bucket"] in ("difference", "both_empty_surviving")]
    undet_rows = [r["row_id"] for r in per_row if r["bucket"] == "child_undetermined"]
    t1_eq = [r["row_id"] for r in per_row if r["T1_surviving_equal"]]
    all_eq = [r["row_id"] for r in per_row if r["all_values_equal"]]

    out = dict(
        schema="jc2.im-descent-replay/v1",
        charged_roster=str(ROSTER),
        n_complete_us1=46,
        parent_counts=parent_counts,
        buckets=dict(buckets),
        equal_surviving_rows=equal_rows,
        difference_rows=[dict(
            row_id=r["row_id"],
            parent_surviving_IM=r["parent_surviving_IM"],
            child_surviving_IM=r["child"]["surviving_IM"],
            parent_all_IM=r["parent_all_IM"],
            child_all_IM=r["child"]["all_IM"],
            bucket=r["bucket"],
        ) for r in diff_rows],
        child_undetermined_rows=undet_rows,
        T1_surviving_equal_rows=t1_eq,
        all_values_equal_rows=all_eq,
        n_radii_agree=sum(1 for r in per_row if r["child"]["radii_agree"] is True),
        n_roster_V_in_own=sum(1 for r in per_row if r["child"]["roster_V_in_own"]),
        n_set_valued_child=sum(1 for r in per_row if r["child"]["V_type"] == "SET-VALUED"),
        elapsed_s=round(time.monotonic() - t0, 3),
        rows=per_row,
    )
    out_path = HERE / "replay.json"
    text = json.dumps(out, indent=2, sort_keys=True) + "\n"
    out_path.write_text(text)
    print("==== SUMMARY ====", flush=True)
    print("parent_counts", parent_counts, flush=True)
    print("buckets", dict(buckets), flush=True)
    print("equal", equal_rows, flush=True)
    print("diff", [r["row_id"] for r in diff_rows], flush=True)
    print("undet", undet_rows, flush=True)
    print("T1_eq", t1_eq, flush=True)
    print("all_eq", all_eq, flush=True)
    print(f"wrote {out_path} bytes={len(text.encode())} elapsed={out['elapsed_s']}s",
          flush=True)


if __name__ == "__main__":
    main()
