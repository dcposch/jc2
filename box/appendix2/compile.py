#!/usr/bin/env python3
"""APPENDIX-II COMPILER.

For a (1)-(13) row with u_s = 1:
  descend (Prop 6.3/6.4), assign radii by Phi, evaluate (8)-(13) on the
  descended pair, apply Moh's SHAPE reduction, emit the polynomial system,
  and solve when #unknowns <= 30.

Fail-closed: Moh's six rows are the calibration set.  The (15,10; V2=3)
pp.210-211 reduction and kill must be reproduced before any new row is
trusted.  python3 -O safe (no load-bearing assert).

s' = 2 means (10)/(11) are vacuous: those constrain V_{r-1} for r = s,...,3,
i.e. j = s-1,...,2, and range(s-1, 1, -1) is empty at s=2.  Only the r=2
endpoint (12)/(13) is active.  SOURCE-READ p.201; implemented in
moh_skeleton_full.Skel.full_ok.
"""
from __future__ import annotations

import ast
import json
import os
import sys
import time
from fractions import Fraction as F
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
BOX = os.path.dirname(HERE)
if BOX not in sys.path:
    sys.path.insert(0, BOX)
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import moh_skeleton_full as MS  # noqa: E402
from descent_core import descend_once, u_s_of  # noqa: E402
from shape import (  # noqa: E402
    phi_s2, shape_bundle, gate_moh_shapes, def51, A_from_deltas, cond1011, cond1213,
)
from solve import (  # noqa: E402
    solve_1510_control2, solve_d2e3_ab, solve_1612, planted_autoscan_us1, Timeout,
)

FAILURES = []


def require(name, cond, detail=""):
    """Load-bearing check; works under python3 -O (not ast.Assert)."""
    if cond:
        print("  [ok]   %s" % name)
        return True
    print("  [FAIL] %s   %s" % (name, detail))
    FAILURES.append(name)
    return False


def row_label(n, m, Ms, V):
    return "(%s,%s; M=%s; V=%s)" % (n, m, list(Ms), dict(sorted(V.items())))


def compile_row(n, m, Ms, V, lab=None, solve=False, timeout=180):
    """Descend + Phi + (8)-(13) + shape.  Optionally solve if <=30 unknowns."""
    S = MS.Skel(n, m, list(Ms), dict(V))
    us = u_s_of(S)
    out = dict(
        lab=lab or row_label(n, m, Ms, V),
        src=(n, m, list(Ms), dict(sorted(V.items()))),
        us=us, src_s=S.s, ds=S.d[S.s], Vs=S.V[S.s],
    )
    if us != 1:
        out["verdict"] = "US-GT-1"
        out["notes"] = "Prop 6.3/6.4 needs u_s=1; p.209 minor-disc dichotomy not applied"
        return out
    D = descend_once(S)
    if D is None or D.get("status") != "DESCENDED":
        out["verdict"] = D.get("status") if D else "NO-DESCENT"
        return out
    out["descended"] = dict(n=D["n"], m=D["m"], M=dict(D["M"]), d=dict(D["d"]),
                            V=dict(D["V"]), k=D["k"], s=D["s"], gcd_ok=D["gcd_ok"],
                            m2_gt_m=D["m2_gt_m"])
    n2, m2, k, sprime = D["n"], D["m"], D["k"], D["s"]
    M2 = D["M"].get(2)
    V2 = D["V"].get(2)
    # Phi as charged: s'=2 on (n',m',M2',V2')
    try:
        d2p, d1p, d2, raw2, raw1 = phi_s2(n2, m2, M2, V2, k)
        phi_ok = True
        phi_err = None
    except Exception as e:
        phi_ok, phi_err = False, "%s: %s" % (type(e).__name__, e)
        d2p = d1p = d2 = raw2 = raw1 = None
    out["phi"] = dict(ok=phi_ok, err=phi_err, delta2=str(d2p) if d2p is not None else None,
                      delta1=str(d1p) if d1p is not None else None,
                      raw2=str(raw2) if raw2 is not None else None,
                      raw1=str(raw1) if raw1 is not None else None,
                      k=k, s_used=2)
    # What s'=2 means for (8)-(11)
    out["sprime"] = sprime
    out["cond1011_note"] = (
        "s'=2 => (10)/(11) VACUOUS (they constrain V_{r-1} for r=s,...,3; "
        "only the r=2 endpoint (12)/(13) is active).  Actual descended s'=%d."
        % sprime
    )
    if sprime == 2 and phi_ok:
        C = shape_bundle(n2, m2, M2, V2, k)
        out["shape"] = {kk: (str(C[kk]) if isinstance(C[kk], F) else C[kk])
                        for kk in ("ok", "reason", "n", "m", "M2", "V2", "k", "d2",
                                   "u", "K", "dprime", "eprime", "n_h", "n_beta",
                                   "n_ord", "n_ab", "two_point", "split_pm",
                                   "A1", "ok1213", "b12", "b13", "ident188",
                                   "cond1011_active", "degx_h", "degx_f", "degx_g")}
        out["shape"]["delta2"] = str(C["delta2"])
        out["shape"]["delta1"] = str(C["delta1"])
        out["shape"]["h_free"] = C["h_free"]
        out["eval_1213"] = dict(A1=C["A1"], b12=C["b12"], b13=C["b13"],
                                ok=C["ok1213"], ident188=C["ident188"])
        # emit unknown count
        if not C["ok"]:
            out["verdict"] = "SHAPE-FAIL:%s" % C["reason"]
            out["n_unknowns"] = None
        elif C["n_ord"] > 30 and (C["n_ab"] is None or C["n_ab"] > 30):
            out["verdict"] = "COUNTING-BOUND"
            out["n_unknowns"] = C["n_ord"]
            out["n_unknowns_ab"] = C["n_ab"]
        else:
            out["n_unknowns"] = C["n_ab"] if (C["two_point"] and C["dprime"] == 2 and C["n_ab"] is not None) else C["n_ord"]
            out["n_unknowns_ord"] = C["n_ord"]
            out["n_unknowns_ab"] = C["n_ab"]
            if not solve:
                out["verdict"] = "EMITTED"
            else:
                out["verdict"] = "SOLVE-PENDING"
    elif sprime != 2:
        # Appendix-II shape is for s'=2.  Do not apply u'=d2-V2 (V2 is not the
        # top multiplicity of a 2-level tower).  Evaluate (8)-(13) on the
        # actual descended tower if Def5.1(3)*(k+1) is defined.
        out["shape"] = dict(ok=False, reason="S-PRIME-GT-2", s=sprime)
        out["n_unknowns"] = None
        out["verdict"] = "S-PRIME-GT-2"
        # try generalized radii
        try:
            Vfull = dict(D["V"])
            dfull = dict(D["d"])
            Mfull = dict(D["M"])
            if (sprime + 1) not in Vfull:
                Vfull[sprime + 1] = dfull.get(sprime + 1, 1)
            deltas = {i: (k + 1) * def51(n2, Mfull, dfull, Vfull, sprime, i)
                      for i in range(1, sprime + 1)}
            out["gen_phi"] = {i: str(deltas[i]) for i in deltas}
            # (10)/(11) at j = sprime-1, ..., 2
            c1011 = {}
            all1011 = True
            for j in range(sprime - 1, 1, -1):
                Aj, Lj = A_from_deltas(deltas, sprime, j)
                ok, b10, b11, tri, sq, Q = cond1011(
                    Vfull[j], dfull[j], dfull[j + 1], Vfull[j + 1], Aj)
                c1011[j] = dict(A=Aj, L=Lj, ok=ok, b10=b10, b11=b11, tri=tri, sq=sq, Q=Q)
                all1011 = all1011 and ok
            A1, L1 = A_from_deltas(deltas, sprime, 1)
            ok1213, b12, b13, ident, ns, ms = cond1213(n2, m2, D["d"][2], D["V"][2], A1)
            out["eval_1011"] = c1011
            out["eval_1213"] = dict(A1=A1, b12=b12, b13=b13, ok=ok1213, ident188=ident)
            out["cond1011_all"] = all1011
            if not all1011 or not ok1213:
                out["verdict"] = "COMBINATORIAL-FAIL"
                out["notes"] = "descended (10)/(11) or (12)/(13) fails on gen-Phi tower"
        except Exception as e:
            out["gen_phi_err"] = "%s: %s" % (type(e).__name__, e)
    else:
        out["verdict"] = "PHI-FAIL"
    return out


def _solve_sub(cmd, spec, timeout=180):
    """Run solve_worker in a killable subprocess.  Cap = timeout seconds."""
    import subprocess, tempfile
    worker = os.path.join(HERE, "solve_worker.py")
    with tempfile.TemporaryDirectory(prefix="a2solve-") as td:
        inp = os.path.join(td, "in.json")
        outp = os.path.join(td, "out.json")
        spec = dict(spec)
        spec["timeout"] = max(timeout * 4, 10000)  # parent kills; worker alarm is backup
        with open(inp, "w") as f:
            json.dump(spec, f)
        try:
            r = subprocess.run(
                [sys.executable, "-u", worker, cmd, inp, outp],
                capture_output=True, text=True, timeout=timeout,
            )
        except subprocess.TimeoutExpired:
            return dict(verdict="TIMEOUT", n_unknowns=spec.get("n_unknowns"),
                        elapsed=timeout, notes="subprocess cap %ss" % timeout)
        if not os.path.isfile(outp):
            return dict(verdict="ERROR", error="no out.json",
                        stderr=(r.stderr or "")[-500:], stdout=(r.stdout or "")[-300:])
        with open(outp) as f:
            return json.load(f)


def maybe_solve(row, timeout=180):
    """Solve an EMITTED / SOLVE-PENDING s'=2 row with <=30 unknowns."""
    if row.get("verdict") not in ("EMITTED", "SOLVE-PENDING", "COUNTING-BOUND"):
        return row
    if row.get("verdict") == "COUNTING-BOUND":
        return row
    sh = row.get("shape") or {}
    if not sh.get("ok"):
        return row
    n, m, M2, V2, k = sh["n"], sh["m"], sh["M2"], sh["V2"], sh["k"]
    # calibration special: (15,10) V2=3 uses the charged control2 path
    if (n, m, M2, V2, k) == (15, 10, 11, 3, 2):
        sol = solve_1510_control2(timeout=timeout)
        row["solve"] = sol
        row["verdict"] = sol["verdict"]
        return row
    if (n, m, M2, V2, k) == (16, 12, 13, 3, 1):
        sol = _solve_sub("moh1612", {"timeout": timeout}, timeout=timeout)
        row["solve"] = sol
        row["verdict"] = sol.get("verdict", "ERROR")
        return row
    if sh.get("two_point") and sh.get("dprime") == 2 and sh.get("n_ab") and sh["n_ab"] <= 30:
        sol = _solve_sub("d2e3_ab",
                         dict(n=n, m=m, M2=M2, V2=V2, k=k, n_unknowns=sh["n_ab"]),
                         timeout=timeout)
        row["solve"] = sol
        row["verdict"] = sol.get("verdict", "ERROR")
        return row
    if sh.get("n_ord") and sh["n_ord"] <= 30:
        if sh.get("dprime") == 2 and not sh.get("two_point"):
            row["verdict"] = "COUNTING-BOUND"
            row["notes"] = "delta2!=-1: A,B not forced; n_ord=%s" % sh["n_ord"]
            return row
        row["verdict"] = "COUNTING-BOUND"
        row["notes"] = "no solver branch for d'=%s e'=%s" % (sh.get("dprime"), sh.get("eprime"))
        return row
    row["verdict"] = "COUNTING-BOUND"
    return row


def load_excess_52():
    path = os.path.join(BOX, "mohprog-drivers-20260903", "full-tree-ode-excess-witnesses.json")
    # prefer frozen copy if present
    frozen = "/tmp/jc2-lane.SaQtV7/inputs/full-tree-ode-excess-witnesses.json"
    if os.path.isfile(frozen):
        path = frozen
    with open(path) as f:
        d = json.load(f)
    rows = []
    for key in d:
        t = ast.literal_eval(key)
        n, m, Ms, Vt = t
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
        out.append((108, m, list(Ms), dict(V), "D108"))
    return out


def run_calibration(timeout=180):
    print("\n== GATE: Phi 10/10 + Moh shapes (22 [15 or 13]; 17->10) + G2=42 ==")
    reports, bundles = gate_moh_shapes()
    for name, ok, detail in reports:
        require(name, ok, str(detail))
    print("\n== GATE: Moh's six: p.207 signatures ==")
    P207 = {
        "(64,48)": (16, 12, 13, 3, 1),
        "(84,56) M2=64,V2=2": (21, 14, 16, 2, 1),
        "(84,56) M2=72,V2=5": (21, 14, 18, 5, 1),
        "(75,50) V2=3": (15, 10, 11, 3, 2),
        "(75,50) V2=2": (15, 10, 11, 2, 2),
    }
    compiled = []
    for (n, m, Ms, Vs, lab, _, _, _) in MS.MOH_TABLE:
        row = compile_row(n, m, Ms, Vs, lab=lab, solve=False)
        compiled.append(row)
        us = row["us"]
        if lab in P207:
            want = P207[lab]
            D = row.get("descended") or {}
            require("%s n'" % lab, D.get("n") == want[0], D.get("n"))
            require("%s m'" % lab, D.get("m") == want[1], D.get("m"))
            require("%s M2'" % lab, D.get("M", {}).get(2) == want[2], D.get("M"))
            require("%s V2'" % lab, D.get("V", {}).get(2) == want[3], D.get("V"))
            require("%s k" % lab, D.get("k") == want[4], D.get("k"))
            require("%s s'=2" % lab, D.get("s") == 2, D.get("s"))
        else:
            require("%s has u_s>1 (p.207 excludes (99,66))" % lab, us > 1, "us=%s" % us)
    return compiled, bundles


def main():
    t_all = time.time()
    print("box/appendix2/compile.py — Appendix-II compiler")
    print("s'=2 => (10)/(11) vacuous; only (12)/(13) active.  Phi = (k+1)*Def5.1(3) s'=2.")
    compiled_moh, bundles = run_calibration(timeout=180)
    if FAILURES:
        print("CALIBRATION FAILED: %s" % FAILURES)
        sys.exit(1)

    print("\n== NEGATIVE CONTROL: (15,10; V2=3) SATURATED-EMPTY (must pass first) ==")
    ctrl = solve_1510_control2(timeout=180)
    for k in ("verdict", "printed_alpha_ok", "printed_gamma_ok", "audited_gamma_ok",
              "case1_contra", "case2_empty", "negative", "positive_seen", "elapsed"):
        print("  %s = %s" % (k, ctrl.get(k)))
    require("CONTROL2 SATURATED-EMPTY", ctrl["verdict"] == "SATURATED-EMPTY")
    require("audited gamma reproduced", ctrl["audited_gamma_ok"] is True)
    require("printed gamma NOT reproduced (ERRATUM)", ctrl["printed_gamma_ok"] is False,
            str(ctrl.get("printed_gamma_ok")))
    require("printed alpha reproduced", ctrl["printed_alpha_ok"] is True)
    require("negative control non-trivial", ctrl.get("negative") is True)
    require("positive controls ran (drop-one)", ctrl.get("positive_seen") is True)
    if FAILURES:
        print("NEGATIVE CONTROL FAILED: %s" % FAILURES)
        sys.exit(1)

    print("\n== POSITIVE CONTROL: planted descended automorphism ==")
    plant = planted_autoscan_us1()
    print("  n_pairs=%s  n_Ms=n-2=%s  planted=%s" % (
        plant["n_pairs"], plant["n_Ms_eq_nminus2"], plant["planted"] if plant["planted"] == "NONE" else "HITS"))
    print("  %s" % plant["notes"][:240])
    if plant["n_Ms_eq_nminus2"] == 0:
        print("  PLANTED: NONE (no autoscan pair has M_s = n-2; Prop 6.3 does not apply)")
    out_plant = plant

    print("\n== SOLVE Moh s'=2 rows with <=30 unknowns ==")
    moh_solved = []
    for row in compiled_moh:
        if row.get("us") != 1:
            moh_solved.append(row)
            print("  %-28s  %s" % (row["lab"], row["verdict"]))
            continue
        row = maybe_solve(row, timeout=180)
        moh_solved.append(row)
        nu = row.get("n_unknowns")
        sol = row.get("solve") or {}
        print("  %-28s  %s  n_unk=%s  n_ord=%s n_ab=%s  elapsed=%s  unsat_empty=%s neg_ok=%s n_eqs=%s" % (
            row["lab"], row["verdict"], nu,
            (row.get("shape") or {}).get("n_ord"),
            (row.get("shape") or {}).get("n_ab"),
            sol.get("elapsed"),
            sol.get("unsaturated_empty"),
            sol.get("negative_nontrivial"),
            sol.get("n_eqs"),
        ))

    for row in moh_solved:
        sol = row.get("solve") or {}
        if row.get("verdict") == "SATURATED-EMPTY" and "unsaturated_empty" in sol:
            require("%s unsaturated is non-trivial (c=0 lives)" % row["lab"],
                    sol.get("unsaturated_empty") is False,
                    str(sol.get("unsaturated_empty")))
            require("%s negative control non-trivial" % row["lab"],
                    sol.get("negative_nontrivial") is True,
                    str(sol.get("negative_nontrivial")))

    print("\n== G2 / G3 cross-check ==")
    g2 = compile_row(105, 70, [28, 103], {2: 1, 3: 6}, lab="G2")
    g3 = compile_row(105, 70, [40, 103], {2: 1, 3: 4}, lab="G3")
    g1 = compile_row(105, 70, [28, 103], {2: 1, 3: 5}, lab="G1")
    for g in (g2, g3, g1):
        print("  %-6s us=%s s'=%s verdict=%s n_unk=%s n_ord=%s Phi=%s" % (
            g["lab"], g["us"], g.get("sprime"), g["verdict"], g.get("n_unknowns"),
            (g.get("shape") or {}).get("n_ord"),
            (g.get("phi") or {}),
        ))
    require("G2 COUNTING-BOUND 42", g2.get("verdict") == "COUNTING-BOUND" and (g2.get("shape") or {}).get("n_ord") == 42,
            str((g2.get("verdict"), (g2.get("shape") or {}).get("n_ord"))))
    require("G3 COUNTING-BOUND", g3.get("verdict") == "COUNTING-BOUND",
            str((g3.get("verdict"), (g3.get("shape") or {}).get("n_ord"))))
    require("G1 US-GT-1", g1.get("verdict") == "US-GT-1", g1.get("verdict"))

    print("\n== 52 C_FULL_TREE_ODE excess at n<=100 ==")
    excess = load_excess_52()
    require("52 excess keys", len(excess) == 52, str(len(excess)))
    n_us1 = 0
    verdicts = {}
    excess_rows = []
    for (n, m, Ms, V, key) in excess:
        row = compile_row(n, m, Ms, V, lab=key, solve=False)
        if row["us"] == 1:
            n_us1 += 1
        # only solve s'=2 with <=30; none of the 52 have parent s=3
        if row.get("verdict") in ("EMITTED", "SOLVE-PENDING"):
            row = maybe_solve(row, timeout=180)
        excess_rows.append(row)
        verdicts[row["verdict"]] = verdicts.get(row["verdict"], 0) + 1
        extra = row.get("gen_phi_err") or ""
        print("  %s  us=%s s'=%s  %s  %s" % (key[:72], row["us"], row.get("sprime"), row["verdict"], extra[:60]))
    print("  u_s=1: %d / 52" % n_us1)
    print("  verdicts: %s" % dict(sorted(verdicts.items())))
    n_die = sum(1 for r in excess_rows if r["verdict"] in (
        "SATURATED-EMPTY", "COMBINATORIAL-FAIL"))
    n_surv = sum(1 for r in excess_rows if r["verdict"] == "SURVIVES")
    n_bound = sum(1 for r in excess_rows if r["verdict"] == "COUNTING-BOUND")
    n_sprime = sum(1 for r in excess_rows if r["verdict"] == "S-PRIME-GT-2")
    print("  coefficient/combinatorial die=%d  SURVIVES=%d  COUNTING-BOUND=%d  S-PRIME-GT-2=%d"
          % (n_die, n_surv, n_bound, n_sprime))

    print("\n== D=108 C_FULL_TREE u_s=1 ==")
    d108 = load_d108_us1()
    print("  n us1 C_FULL_TREE rows at D=108: %d" % len(d108))
    v108 = {}
    rows108 = []
    for (n, m, Ms, V, lab) in d108:
        row = compile_row(n, m, Ms, V, lab="D108 m=%s M=%s V=%s" % (m, Ms, V), solve=False)
        if row.get("verdict") in ("EMITTED", "SOLVE-PENDING"):
            row = maybe_solve(row, timeout=180)
        rows108.append(row)
        v108[row["verdict"]] = v108.get(row["verdict"], 0) + 1
        print("  m=%s M=%s V=%s  s'=%s  %s" % (m, Ms, V, row.get("sprime"), row["verdict"]))
    print("  verdicts: %s" % dict(sorted(v108.items())))

    sink = os.path.join(HERE, "compile_out.json")
    summary = dict(
        moh=[{k: r[k] for k in r if k != "solve"} | {"solve_verdict": (r.get("solve") or {}).get("verdict"),
                                                      "solve_elapsed": (r.get("solve") or {}).get("elapsed")}
             for r in moh_solved],
        control2=ctrl,
        planted=out_plant,
        G2=g2, G3=g3, G1=g1,
        excess_verdicts=verdicts,
        excess_n=len(excess_rows),
        excess_us1=n_us1,
        excess_die=n_die, excess_survives=n_surv, excess_bound=n_bound, excess_sprime=n_sprime,
        d108_n=len(rows108), d108_verdicts=v108,
        failures=FAILURES,
        elapsed=time.time() - t_all,
    )
    # make JSON-safe
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
    with open(sink, "w") as f:
        json.dump(conv(summary), f, indent=2, sort_keys=True)
    print("\nwrote %s  wall %.1fs" % (sink, time.time() - t_all))
    if FAILURES:
        print("FAILURES: %s" % FAILURES)
        sys.exit(1)
    print("ALL compiler GATES GREEN.")
    return summary


if __name__ == "__main__":
    main()
