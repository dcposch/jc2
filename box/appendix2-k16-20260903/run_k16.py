#!/usr/bin/env python3
"""K=16 ray compiler run + Phi_eff s_eff=2 sweep.

Does not modify box/appendix2/.  Charged copies in this directory are
byte-identical and read-only.
"""
from __future__ import annotations

import ast
import json
import os
import sys
import time
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
BOX = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, BOX)

import moh_skeleton_full as MS
from compile import compile_row, maybe_solve
from descent_core import u_s_of
from phi_eff import descend_phi_eff, shape_of_eff
from shape import shape_bundle
from solve import solve_1612, solve_d2e3_ab
from solve_twopoint import (
    solve_d2e3_d1, solve_horner_cap, newton_tight_drop_to_budget,
    build_horner_cap, hadic_jac_eqs,
)

LANE_JSON = "/tmp/jc2-lane.R3BIWM/inputs/full-tree-ode-excess-witnesses.json"
OUT = os.path.join(HERE, "out")
os.makedirs(OUT, exist_ok=True)

BUDGET = 40


def conv(o):
    if isinstance(o, F):
        return str(o)
    if isinstance(o, dict):
        return {str(k): conv(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [conv(x) for x in o]
    if isinstance(o, (int, float, str, bool)) or o is None:
        return o
    return str(o)


def dump(name, obj):
    path = os.path.join(OUT, name)
    with open(path, "w") as f:
        json.dump(conv(obj), f, indent=2, sort_keys=True)
    print("  wrote", path, flush=True)
    return path


def k16_parent(t):
    n = 48 * t + 16
    m = 32 * t + 16
    return n, m, [n - 12, n - 2], {2: 3, 3: 3}


def load_excess_52():
    with open(LANE_JSON) as f:
        d = json.load(f)
    rows = []
    for key in d:
        tup = ast.literal_eval(key)
        n, m, Ms, Vt = tup
        rows.append((n, m, list(Ms), dict(Vt), key))
    return rows


def load_d108_us1():
    sys.path.insert(0, os.path.join(BOX, "mohprog-drivers-20260903"))
    import full_tree_partition as FT
    out = []
    for (m, Ms, V) in MS.census(108, Kmin=16, full=True):
        S = MS.Skel(108, m, list(Ms), V)
        if u_s_of(S) != 1:
            continue
        if not FT.full_tree_ok(S):
            continue
        out.append((108, m, list(Ms), dict(V), "D108 m=%s M=%s V=%s" % (m, Ms, V)))
    return out


def slim_shape(C):
    if not C.get("ok"):
        return dict(ok=False, reason=C.get("reason"))
    keys = ("ok", "n", "m", "M2", "V2", "k", "d2", "u", "K", "dprime", "eprime",
            "n_h", "n_beta", "n_ord", "n_ab", "two_point", "split_pm",
            "A1", "ok1213", "b12", "b13", "delta1", "delta2", "h_free")
    out = {}
    for k in keys:
        v = C.get(k)
        out[k] = str(v) if isinstance(v, F) else v
    out["lead"] = {str(a): b for a, b in (C.get("lead") or {}).items()}
    return out


def classify_eff(rec):
    """How to solve an s_eff=2 child, if at all, within BUDGET."""
    C = shape_of_eff(rec)
    rec_out = dict(
        parent=(rec["n"], rec["m"], rec["M"], rec["V"]),
        n_prime=rec.get("n_prime"), m_prime=rec.get("m_prime"),
        k=rec.get("k"), s_eff=rec.get("s_eff"), dropped=rec.get("dropped"),
        M_eff=rec.get("M_eff"), den_eff=rec.get("den_eff"),
        phi_eff=rec.get("phi_eff"),
        shape=slim_shape(C) if isinstance(C, dict) else None,
    )
    if not C.get("ok"):
        rec_out["plan"] = "SHAPE-FAIL:%s" % C.get("reason")
        rec_out["n_unknowns"] = None
        return rec_out
    args = rec["shape_args"]
    rec_out["args"] = args
    if C["dprime"] == 2 and C["two_point"] and C.get("n_ab") and C["n_ab"] <= BUDGET:
        rec_out["plan"] = "d2e3_ab"
        rec_out["n_unknowns"] = C["n_ab"]
    elif C["dprime"] == 2 and C["n_ord"] <= BUDGET:
        rec_out["plan"] = "d2e3_d1"
        rec_out["n_unknowns"] = C["n_ord"]
    elif C["two_point"] and C["u"] == 1 and C["K"] == 4:
        dh, nunk, info = newton_tight_drop_to_budget(
            args["n"], args["m"], args["M2"], args["V2"], args["k"], BUDGET)
        rec_out["hcap_info"] = info
        if dh == 0 and nunk is not None:
            rec_out["plan"] = "horner_cap"
            rec_out["n_unknowns"] = nunk
            rec_out["drop_high"] = 0
        elif nunk is not None:
            rec_out["plan"] = "horner_cap_slice"
            rec_out["n_unknowns"] = nunk
            rec_out["drop_high"] = dh
        else:
            rec_out["plan"] = "COUNTING-BOUND"
            rec_out["n_unknowns"] = C["n_ord"]
    elif C["n_ord"] <= BUDGET:
        rec_out["plan"] = "COUNTING-BOUND-no-branch"
        rec_out["n_unknowns"] = C["n_ord"]
        rec_out["notes"] = "n_ord<=40 but d'=%s two_point=%s not a solver branch" % (
            C["dprime"], C["two_point"])
    else:
        rec_out["plan"] = "COUNTING-BOUND"
        rec_out["n_unknowns"] = C["n_ord"]
    return rec_out


def run_plan(item, timeout=180):
    plan = item.get("plan")
    args = item.get("args") or {}
    n, m, M2, V2, k = args.get("n"), args.get("m"), args.get("M2"), args.get("V2"), args.get("k")
    print("  SOLVE plan=%s (%s,%s; %s; %s; k=%s) nunk=%s" % (
        plan, n, m, M2, V2, k, item.get("n_unknowns")), flush=True)
    if plan == "d2e3_ab":
        return solve_d2e3_ab(n, m, M2, V2, k, timeout=timeout)
    if plan == "d2e3_d1":
        nunk = item.get("n_unknowns") or 0
        if nunk <= 18:
            return solve_d2e3_d1(n, m, M2, V2, k, timeout=timeout)
        # medium: sympy first with shorter cap, else the same
        return solve_d2e3_d1(n, m, M2, V2, k, timeout=timeout)
    if plan in ("horner_cap", "horner_cap_slice"):
        dh = item.get("drop_high") or 0
        nunk = item.get("n_unknowns") or 0
        backend = "sympy" if nunk <= 18 else "singular"
        char = 32003 if (backend == "singular" and nunk > 22) else 0
        r = solve_horner_cap(n, m, M2, V2, k, timeout=timeout,
                             drop_high=dh, backend=backend, char=char, order="dp")
        # if modular SURVIVES, try Q; if modular EMPTY, try a second prime then Q if time
        if backend == "singular" and r.get("verdict") == "SATURATED-EMPTY" and char != 0:
            r2 = solve_horner_cap(n, m, M2, V2, k, timeout=min(timeout, 90),
                                  drop_high=dh, backend="singular", char=0, order="dp")
            r["q_followup"] = {kk: r2.get(kk) for kk in
                               ("verdict", "empty", "elapsed", "backend", "char")}
            if r2.get("verdict") in ("SATURATED-EMPTY", "SURVIVES"):
                r = r2
                r["notes"] = (r.get("notes") or "") + " Q after modular empty"
        if backend == "singular" and r.get("verdict") == "SURVIVES" and char != 0:
            r["notes"] = (r.get("notes") or "") + " modular SURVIVES (char=%s); not a Q witness" % char
        return r
    return dict(verdict=plan, n_unknowns=item.get("n_unknowns"))


def main():
    t_all = time.time()
    print("== appendix2-k16 run  budget=%d ==" % BUDGET, flush=True)

    # --- K16 ray: unchanged compile_row + maybe_solve ---
    print("\n== (1) K16 ray t=1,2,3 compile_row (unchanged) ==", flush=True)
    ray = []
    for t in (1, 2, 3):
        n, m, Ms, V = k16_parent(t)
        row = compile_row(n, m, Ms, V, lab="K16 t=%d" % t, solve=False)
        sh = row.get("shape") or {}
        print("  t=%d (%s,%s)->(%s,%s) M2'=%s V2'=%s k=%s  verdict=%s n_unk=%s n_ord=%s n_ab=%s d'=%s e'=%s h_free=%s Phi=(%s,%s)" % (
            t, n, m, sh.get("n"), sh.get("m"), sh.get("M2"), sh.get("V2"), sh.get("k"),
            row.get("verdict"), row.get("n_unknowns"), sh.get("n_ord"), sh.get("n_ab"),
            sh.get("dprime"), sh.get("eprime"), sh.get("h_free"),
            (row.get("phi") or {}).get("delta2"), (row.get("phi") or {}).get("delta1"),
        ), flush=True)
        ray.append(row)

    print("\n== (1b) maybe_solve unchanged ==", flush=True)
    ray_solved = []
    for t, row in zip((1, 2, 3), ray):
        if t == 1:
            print("  t=1 -> special solve_1612 (18 unk control)", flush=True)
            t1path = os.path.join(OUT, "t1_solve1612.json")
            if os.path.isfile(t1path):
                with open(t1path) as f:
                    sol = json.load(f)
                print("  t=1 reused", t1path, sol.get("verdict"), sol.get("elapsed"), flush=True)
            else:
                sol = solve_1612(timeout=180)
                dump("t1_solve1612.json", sol)
            row = dict(row)
            row["solve"] = sol
            row["verdict"] = sol.get("verdict", row.get("verdict"))
            row["n_unknowns_jac"] = sol.get("n_unknowns")
        else:
            row = maybe_solve(dict(row), timeout=30)
            print("  t=%d maybe_solve -> %s  notes=%s" % (
                t, row.get("verdict"), row.get("notes")), flush=True)
        ray_solved.append(row)

    print("\n== (1c) Horner-cap / Newton-tight on t=2,3 (and t=1 gate of the chart) ==", flush=True)
    extra = []
    # t=1 Horner-cap count gate (do not re-GB unless t=1 file missing)
    B1 = build_horner_cap(16, 12, 13, 3, 1, drop_high=0)
    print("  t=1 horner_cap nunk=%s (want 18) ok=%s" % (B1.get("n_unknowns"), B1.get("ok")), flush=True)
    extra.append(dict(t=1, nunk=B1.get("n_unknowns"), gate18=(B1.get("n_unknowns") == 18)))

    for t, nm in ((2, (28, 20, 25, 3, 1)), (3, (40, 28, 37, 3, 1))):
        n, m, M2, V2, k = nm
        dh, nunk, info = newton_tight_drop_to_budget(n, m, M2, V2, k, BUDGET)
        print("  t=%d horner_cap drop_high=%s nunk=%s info_head=%s" % (
            t, dh, nunk, info[:4]), flush=True)
        item = dict(plan="horner_cap" if dh == 0 else "horner_cap_slice",
                    args=dict(n=n, m=m, M2=M2, V2=V2, k=k),
                    n_unknowns=nunk, drop_high=dh, t=t)
        # modular first for t=2 (38 unk); t=3 is a slice
        timeout = 180 if t == 2 else 120
        sol = run_plan(item, timeout=timeout)
        print("    -> %s elapsed=%s backend=%s empty=%s unsat_empty=%s neg=%s n_eqs=%s" % (
            sol.get("verdict"), sol.get("elapsed"), sol.get("backend"),
            sol.get("empty"), sol.get("unsaturated_empty"),
            sol.get("negative_nontrivial"), sol.get("n_eqs")), flush=True)
        item["solve"] = sol
        extra.append(item)
        dump("ray_t%d_horner.json" % t, item)

        # if t=2 modular/Q empty, also try lex (elimination) only if we still have time
        if sol.get("verdict") not in ("SATURATED-EMPTY", "SURVIVES"):
            print("    retry Singular dp char=32003", flush=True)
            solp = solve_horner_cap(n, m, M2, V2, k, timeout=90, drop_high=dh or 0,
                                    backend="singular", char=32003, order="dp")
            print("    modular ->", solp.get("verdict"), solp.get("elapsed"), flush=True)
            item["modular"] = solp
            if solp.get("verdict") not in ("SATURATED-EMPTY", "SURVIVES"):
                print("    retry Singular lp (elim) char=32003", flush=True)
                soll = solve_horner_cap(n, m, M2, V2, k, timeout=60, drop_high=dh or 0,
                                        backend="singular", char=32003, order="lp")
                print("    lp ->", soll.get("verdict"), soll.get("elapsed"), flush=True)
                item["elim"] = soll

    dump("ray.json", dict(compile=ray_solved, extra=extra))

    # --- Phi_eff ---
    print("\n== (3) Phi_eff on 52 excess + 19 D108 us1 ==", flush=True)
    excess = load_excess_52()
    d108 = load_d108_us1()
    print("  loaded 52=%d D108=%d" % (len(excess), len(d108)), flush=True)

    def collect(rows, tag):
        recs = []
        seff2 = []
        for tup in rows:
            n, m, Ms, V = tup[0], tup[1], tup[2], tup[3]
            lab = tup[4] if len(tup) > 4 else tag
            S = MS.Skel(n, m, list(Ms), dict(V))
            rec = descend_phi_eff(S)
            rec["lab"] = lab
            recs.append(rec)
            if rec.get("s_eff") == 2:
                seff2.append(rec)
        return recs, seff2

    recs52, s2_52 = collect(excess, "52")
    recs108, s2_108 = collect(d108, "D108")
    print("  52: N=%d drop>0=%d s_eff=2=%d" % (
        len(recs52), sum(1 for r in recs52 if r.get("dropped")), len(s2_52)), flush=True)
    print("  D108: N=%d drop>0=%d s_eff=2=%d" % (
        len(recs108), sum(1 for r in recs108 if r.get("dropped")), len(s2_108)), flush=True)

    plans52 = [classify_eff(r) for r in s2_52]
    plans108 = [classify_eff(r) for r in s2_108]

    def show_plans(tag, plans):
        from collections import Counter
        c = Counter(p["plan"] for p in plans)
        print("  %s plans: %s" % (tag, dict(c)), flush=True)
        for p in plans:
            print("    %s  plan=%s nunk=%s two_pt=%s d'=%s" % (
                p["parent"], p["plan"], p.get("n_unknowns"),
                (p.get("shape") or {}).get("two_point"),
                (p.get("shape") or {}).get("dprime")), flush=True)

    show_plans("52 s_eff=2", plans52)
    show_plans("D108 s_eff=2", plans108)
    dump("phi_eff_plans.json", dict(n52=len(recs52), n108=len(recs108),
                                    n_seff2_52=len(s2_52), n_seff2_108=len(s2_108),
                                    plans52=plans52, plans108=plans108,
                                    seff2_52_parents=[p["parent"] for p in plans52],
                                    seff2_108_parents=[p["parent"] for p in plans108]))

    print("\n== (3b) solve every in-budget s_eff=2 row ==", flush=True)
    solved = []
    for tag, plans in (("52", plans52), ("D108", plans108)):
        for p in plans:
            if p["plan"] in ("d2e3_ab", "d2e3_d1", "horner_cap", "horner_cap_slice"):
                nunk = p.get("n_unknowns") or 99
                timeout = 180 if nunk <= 20 else 120
                sol = run_plan(p, timeout=timeout)
                p = dict(p)
                p["solve"] = {kk: sol.get(kk) for kk in sol if kk not in ("C", "family") or sol.get("verdict") == "SURVIVES"}
                p["tag"] = tag
                print("    %s -> %s  nunk=%s elapsed=%s unsat_empty=%s neg=%s" % (
                    p["parent"], sol.get("verdict"), sol.get("n_unknowns"),
                    sol.get("elapsed"), sol.get("unsaturated_empty"),
                    sol.get("negative_nontrivial")), flush=True)
                solved.append(p)
            else:
                p = dict(p)
                p["tag"] = tag
                p["solve"] = dict(verdict=p["plan"], n_unknowns=p.get("n_unknowns"))
                solved.append(p)
    dump("phi_eff_solved.json", solved)

    summary = dict(
        elapsed=time.time() - t_all,
        ray_t1=ray_solved[0].get("verdict") if ray_solved else None,
        ray_t2_unchanged=ray_solved[1].get("verdict") if len(ray_solved) > 1 else None,
        ray_t3_unchanged=ray_solved[2].get("verdict") if len(ray_solved) > 2 else None,
        ray_extra=[{k: e.get(k) for k in ("t", "n_unknowns", "drop_high", "plan") if k in e}
                   | {"verdict": (e.get("solve") or {}).get("verdict")}
                   for e in extra],
        n_seff2_52=len(s2_52), n_seff2_108=len(s2_108),
        seff2_verdicts={},
    )
    from collections import Counter
    summary["seff2_verdicts"] = dict(Counter(
        (s.get("solve") or {}).get("verdict") or s.get("plan") for s in solved))
    dump("summary.json", summary)
    print("\nSUMMARY", json.dumps(conv(summary), indent=2), flush=True)
    print("ALL DONE wall %.1fs" % (time.time() - t_all), flush=True)
    return summary


if __name__ == "__main__":
    main()
