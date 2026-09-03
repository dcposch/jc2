#!/usr/bin/env python3
"""Stage 2: unchanged maybe_solve t=2,3; Newton-tight + full Horner-cap;
Phi_eff in-budget d2e3 solves.
"""
from __future__ import annotations

import ast
import json
import os
import sys
import time
from collections import Counter
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
BOX = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, BOX)
OUT = os.path.join(HERE, "out")
os.makedirs(OUT, exist_ok=True)

import moh_skeleton_full as MS
from compile import compile_row, maybe_solve
from descent_core import u_s_of
from phi_eff import descend_phi_eff
from solve import solve_d2e3_ab
from solve_twopoint import solve_d2e3_d1, solve_horner_cap, build_horner_cap

LANE_JSON = "/tmp/jc2-lane.R3BIWM/inputs/full-tree-ode-excess-witnesses.json"


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


def slim(sol):
    keys = ("verdict", "n_unknowns", "n_eqs", "empty", "basis_size",
            "unsaturated_empty", "unsaturated_size", "negative_nontrivial",
            "elapsed", "backend", "char", "order", "ring", "rabinowitsch",
            "solver", "drop_high", "slice", "dropped", "error", "notes",
            "control_empty_pass", "family", "stdout_tail")
    return {k: sol.get(k) for k in keys if k in sol}


def k16_parent(t):
    n = 48 * t + 16
    m = 32 * t + 16
    return n, m, [n - 12, n - 2], {2: 3, 3: 3}


def load_excess_52():
    with open(LANE_JSON) as f:
        d = json.load(f)
    return [(ast.literal_eval(k)[0], ast.literal_eval(k)[1],
             list(ast.literal_eval(k)[2]), dict(ast.literal_eval(k)[3]), k)
            for k in d]


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
        out.append((108, m, list(Ms), dict(V)))
    return out


def main():
    t_all = time.time()
    print("== stage2 ==", flush=True)

    print("\n-- unchanged maybe_solve t=2,3 --", flush=True)
    unchanged = {}
    for t in (2, 3):
        n, m, Ms, V = k16_parent(t)
        row = compile_row(n, m, Ms, V, lab="K16 t=%d" % t, solve=False)
        row2 = maybe_solve(dict(row), timeout=30)
        print("  t=%d compile=%s maybe=%s n_unk=%s notes=%s" % (
            t, row.get("verdict"), row2.get("verdict"),
            row2.get("n_unknowns"), row2.get("notes")), flush=True)
        unchanged[t] = dict(compile_verdict=row.get("verdict"),
                            maybe_verdict=row2.get("verdict"),
                            n_unknowns=row2.get("n_unknowns"),
                            n_ord=(row.get("shape") or {}).get("n_ord"),
                            n_ab=(row.get("shape") or {}).get("n_ab"),
                            notes=row2.get("notes"),
                            shape=row.get("shape"),
                            phi=row.get("phi"),
                            descended=row.get("descended"))
    dump("ray_unchanged.json", unchanged)

    print("\n-- t=2 Newton-tight drop5 (19 unk, p.208 remainders) --", flush=True)
    r = solve_horner_cap(28, 20, 25, 3, 1, timeout=90, drop_high=5,
                         backend="singular", char=32003, order="dp")
    print("  t2 slice19 mod", slim(r), flush=True)
    dump("ray_t2_slice19_mod.json", slim(r))
    if r.get("verdict") in ("SATURATED-EMPTY", "SURVIVES", "TIMEOUT", "ERROR"):
        rQ = solve_horner_cap(28, 20, 25, 3, 1, timeout=180, drop_high=5,
                              backend="singular", char=0, order="dp")
        print("  t2 slice19 Q-sing", slim(rQ), flush=True)
        dump("ray_t2_slice19_Q.json", slim(rQ))
        if rQ.get("verdict") in ("TIMEOUT", "ERROR"):
            rS = solve_horner_cap(28, 20, 25, 3, 1, timeout=180, drop_high=5,
                                  backend="sympy", char=0)
            print("  t2 slice19 sympy", slim(rS), flush=True)
            dump("ray_t2_slice19_sympy.json", slim(rS))

    print("\n-- t=2 full Horner-cap 38 unk Singular GF(32003) dp --", flush=True)
    r = solve_horner_cap(28, 20, 25, 3, 1, timeout=180, drop_high=0,
                         backend="singular", char=32003, order="dp")
    print("  t2 full38 mod", slim(r), flush=True)
    dump("ray_t2_full38_mod.json", slim(r))
    if r.get("verdict") == "SATURATED-EMPTY":
        print("  follow-up Q dp 120s", flush=True)
        rQ = solve_horner_cap(28, 20, 25, 3, 1, timeout=120, drop_high=0,
                              backend="singular", char=0, order="dp")
        print("  t2 full38 Q", slim(rQ), flush=True)
        dump("ray_t2_full38_Q.json", slim(rQ))
    elif r.get("verdict") not in ("SURVIVES",):
        print("  retry lp modular 60s", flush=True)
        rL = solve_horner_cap(28, 20, 25, 3, 1, timeout=60, drop_high=0,
                              backend="singular", char=32003, order="lp")
        print("  t2 full38 lp", slim(rL), flush=True)
        dump("ray_t2_full38_lp.json", slim(rL))

    print("\n-- t=3 Newton-tight drop5 (39 unk) Singular GF(32003) --", flush=True)
    r = solve_horner_cap(40, 28, 37, 3, 1, timeout=150, drop_high=5,
                         backend="singular", char=32003, order="dp")
    print("  t3 slice39 mod", slim(r), flush=True)
    dump("ray_t3_slice39_mod.json", slim(r))
    if r.get("verdict") not in ("SATURATED-EMPTY", "SURVIVES"):
        print("  t=3 19-unk drop? keep p.208 remainders: drop until α2-4 β2-3", flush=True)
        # compute drop for that: t=3 interleave until a={2,3,4} b={2,3}
        B = build_horner_cap(40, 28, 37, 3, 1, drop_high=10)
        print("  drop10 nunk", B.get("n_unknowns"), "a", sorted(B.get("alpha", {})),
              "b", sorted(B.get("beta", {})), flush=True)
        r2 = solve_horner_cap(40, 28, 37, 3, 1, timeout=180, drop_high=10,
                              backend="sympy", char=0)
        print("  t3 drop10", slim(r2), flush=True)
        dump("ray_t3_slice_p208.json", slim(r2))

    print("\n-- Phi_eff in-budget d'=2 solves --", flush=True)
    jobs = []
    excess = load_excess_52()
    d108 = load_d108_us1()
    from phi_eff import shape_of_eff
    for tag, rows in (("52", excess), ("D108", [(n, m, Ms, V, None) for n, m, Ms, V in d108])):
        for tup in rows:
            n, m, Ms, V = tup[0], tup[1], tup[2], tup[3]
            S = MS.Skel(n, m, list(Ms), dict(V))
            rec = descend_phi_eff(S)
            if rec.get("s_eff") != 2:
                continue
            C = shape_of_eff(rec)
            if not C.get("ok"):
                jobs.append(dict(tag=tag, parent=(n, m, Ms, V), child=(rec.get("n_prime"), rec.get("m_prime"), rec.get("M_eff"), rec.get("k")),
                                 plan="SHAPE-FAIL:%s" % C.get("reason"), s_eff=2))
                continue
            args = rec["shape_args"]
            if C["dprime"] == 2 and C["two_point"] and C.get("n_ab") and C["n_ab"] <= 40:
                plan, nunk = "d2e3_ab", C["n_ab"]
            elif C["dprime"] == 2 and C["n_ord"] <= 40:
                plan, nunk = "d2e3_d1", C["n_ord"]
            else:
                plan, nunk = "SKIP", C.get("n_ord")
            jobs.append(dict(tag=tag, parent=(n, m, Ms, V), args=args, plan=plan,
                             n_unknowns=nunk, two_point=C["two_point"],
                             dprime=C["dprime"], n_ord=C["n_ord"], n_ab=C["n_ab"],
                             s_eff=2, phi_eff=rec.get("phi_eff"),
                             delta2=str(C["delta2"]), delta1=str(C["delta1"])))

    print("  jobs", Counter(j["plan"] for j in jobs), flush=True)
    solved = []
    for j in jobs:
        print("  %s %s plan=%s nunk=%s" % (j["tag"], j["parent"], j["plan"], j.get("n_unknowns")), flush=True)
        if j["plan"] == "d2e3_ab":
            a = j["args"]
            sol = solve_d2e3_ab(a["n"], a["m"], a["M2"], a["V2"], a["k"], timeout=180)
        elif j["plan"] == "d2e3_d1":
            a = j["args"]
            sol = solve_d2e3_d1(a["n"], a["m"], a["M2"], a["V2"], a["k"], timeout=180)
        else:
            sol = dict(verdict=j["plan"], n_unknowns=j.get("n_unknowns"))
        j["solve"] = slim(sol)
        print("    ->", sol.get("verdict"), "elapsed", sol.get("elapsed"),
              "unsat_empty", sol.get("unsaturated_empty"),
              "neg", sol.get("negative_nontrivial"), flush=True)
        solved.append(j)
        dump("phi_eff_solved.json", solved)

    dump("stage2_summary.json", dict(
        elapsed=time.time() - t_all,
        unchanged={t: unchanged[t]["maybe_verdict"] for t in unchanged},
        phieff=dict(Counter((j.get("solve") or {}).get("verdict") for j in solved)),
        n_jobs=len(solved),
    ))
    print("STAGE2 DONE", time.time() - t_all, flush=True)


if __name__ == "__main__":
    main()
