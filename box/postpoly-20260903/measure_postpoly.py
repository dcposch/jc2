#!/usr/bin/env python3
"""POST-POLY CENSUS — desk measurement on frozen copies.

Operative screen: C_FULL_TREE_POLYNOMIAL_ODE
(full_tree_partition.full_tree_polynomial_ode_ok: POLY fires only at
integral δ ≤ 0; ungated Prop 5.6).

Φ_eff is the charged measure_anchor.py rule (AUDIT 17(dd)): Prop 6.3
image, drop terminal M' = n'−1, V_{s*+1}=d_{s*+1}, then
δ' = (k+1)·Def 5.1(3).

Does not modify the frozen copies. Writes results.json only.
"""
from __future__ import annotations

import json
import sys
import time
from collections import defaultdict
from fractions import Fraction as F
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "repro"))

import moh_skeleton_full as M  # noqa: E402
import full_tree_partition as FT  # noqa: E402
from construct_ray import try_skel, k16_family, de_fixed_family  # noqa: E402


FAILURES: list[str] = []


def check(name, cond, detail=""):
    if cond:
        print("  [ok]   %s" % name, flush=True)
        return True
    print("  [FAIL] %s   %s" % (name, detail), flush=True)
    FAILURES.append(name)
    return False


def abort_if_failed(stage):
    if FAILURES:
        print("%s FAILED: %s" % (stage, FAILURES), flush=True)
        sys.exit(1)


def frac_text(x):
    if x is None:
        return None
    if isinstance(x, F):
        return str(x.numerator) if x.denominator == 1 else "%s/%s" % (
            x.numerator, x.denominator)
    return str(x)


def row_key(S):
    return (S.n, S.m, tuple(S.M[i] for i in range(2, S.s + 1)),
            tuple((i, S.V[i]) for i in range(2, S.s + 1)))


def group_key(S):
    return (S.n, S.m, tuple(S.M[i] for i in range(2, S.s + 1)), S.V[S.s])


def v_map(S):
    return {i: S.V[i] for i in range(2, S.s + 1)}


def m_list(S):
    return [S.M[i] for i in range(2, S.s + 1)]


def u_s_of(S):
    return S.d[S.s] - S.V[S.s]


def uni_N(S, nlo=6):
    return sorted(M.uni_hits([(S.V[2], S.q(), S.u)], nlo, None))


# ---------------------------------------------------------------------------
# Φ_eff (byte-faithful to charged measure_anchor.py: def51/descend/truncate/phi_on)
# ---------------------------------------------------------------------------
def def51(n, M, d, V, s, i):
    num = F(n - M[i])
    den = F(n - M[s] - 1)
    if den == 0:
        return None
    for j in range(i + 1, s + 1):
        num *= V[j] * (n - M[j]) - d[j]
        den *= V[j] * (n - M[j - 1]) - d[j]
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
    return {
        "n": n2, "m": m2, "s": s2, "M": M2, "d": d2, "V": V2,
        "k": k, "u_s": us, "d_s": ds, "V_s": Vs,
    }


def truncate_jacobian(D):
    n, s = D["n"], D["s"]
    M, d, V = dict(D["M"]), dict(D["d"]), dict(D["V"])
    dropped = 0
    while s >= 1 and M.get(s) == n - 1:
        dropped += 1
        s -= 1
        M.pop(s + 1, None)
        V.pop(s + 1, None)
        if (s + 1) in d and s >= 1:
            V[s + 1] = d[s + 1]
    D2 = dict(D)
    D2.update({"s": s, "M": M, "d": d, "V": V, "dropped": dropped})
    return D2


def phi_on(D):
    n, M, d, V, s, k = D["n"], D["M"], D["d"], D["V"], D["s"], D["k"]
    if s < 1:
        return None
    if n - M[s] - 1 == 0:
        return None
    out = []
    for i in range(1, s + 1):
        raw = def51(n, M, d, V, s, i)
        if raw is None:
            return None
        out.append((k + 1) * raw)
    return out


def phi_eff(S):
    us = u_s_of(S)
    if us != 1:
        return {"status": "NOT-US1", "u_s": us, "s": S.s, "two_point": False,
                "s_eff": None}
    vals = [S.n, S.m] + [S.M[i] for i in range(1, S.s)] + [
        S.d[i] for i in range(1, S.s + 1)]
    ds = S.d[S.s]
    if any(x % ds != 0 for x in vals):
        return {"status": "NOT-INTEGRAL", "u_s": us, "s": S.s,
                "two_point": False, "s_eff": None}
    D = descend(S)
    Dt = truncate_jacobian(D)
    ph = phi_on(Dt)
    s_eff = Dt["s"]
    Mlist = [int(Dt["M"][i]) for i in range(2, s_eff + 1)] if s_eff >= 2 else []
    Vmap = {i: int(Dt["V"][i]) for i in range(2, s_eff + 1)} if s_eff >= 2 else {}
    Vnext = Dt["V"].get(s_eff + 1)
    d2 = ph[1] if (ph is not None and s_eff >= 2) else None
    two = (d2 == F(-1))
    return {
        "status": "OK",
        "u_s": us,
        "n": Dt["n"], "m": Dt["m"],
        "M": Mlist,
        "V": Vmap,
        "V_next": Vnext,
        "k": Dt["k"],
        "s_raw": D["s"],
        "s_eff": s_eff,
        "dropped": Dt["dropped"],
        "delta": None if ph is None else [frac_text(x) for x in ph],
        "delta2": frac_text(d2),
        "two_point": two,
        "d_s": D["d_s"],
        "V_s": D["V_s"],
    }


def screens(S):
    return {
        "TREE": FT.full_tree_ok(S),
        "ODE": FT.full_tree_ode_ok(S),
        "POLY": FT.full_tree_polynomial_ok(S),
        "POLY_ODE": FT.full_tree_polynomial_ode_ok(S),
    }


def killing(S, polynomial_recenter=True, ode_nondegenerate=True):
    E = FT.evaluator(S, polynomial_recenter=polynomial_recenter,
                     ode_nondegenerate=ode_nondegenerate)
    ok, wit = E.embeds(S)
    if ok:
        return {"ok": True, "j": None, "failure": None}
    if not isinstance(wit, dict):
        return {"ok": False, "j": None, "failure": str(wit)}
    fail = wit.get("failure")
    if not fail and wit.get("failures"):
        kinds = sorted({f.get("failure", "?") for f in wit["failures"]})
        fail = "; ".join(kinds)
    return {"ok": False, "j": wit.get("j"), "failure": fail,
            "A": wit.get("A"), "P": wit.get("P"), "Q": wit.get("Q"),
            "selected_V": wit.get("selected_V")}


def poly_sites(S):
    """Levels j=2..s-1 at which POLY fires (integral δ_j ≤ 0) on the selected path."""
    E = FT.evaluator(S, polynomial_recenter=True, ode_nondegenerate=True)
    path = list(E.initial_path())
    for i in range(2, S.s + 1):
        path[i] = S.V[i]
    path = tuple(path)
    sites = []
    deltas = {}
    for j in range(1, S.s + 1):
        dj = E.radius(j, path)
        deltas[j] = frac_text(dj)
        if j >= 2 and j <= S.s - 1 and dj.denominator == 1 and dj <= 0:
            sites.append({"j": j, "delta": frac_text(dj)})
    return {"sites": sites, "delta": deltas}


def skel_record(S, extra=None):
    rec = {
        "n": S.n, "m": S.m, "s": S.s, "K": S.K,
        "M": m_list(S), "V": v_map(S),
        "d": [S.d[i] for i in range(1, S.s + 2)],
        "u_s": u_s_of(S),
        "N": uni_N(S),
        "screens": screens(S),
        "poly_sites": poly_sites(S),
        "phi_eff": phi_eff(S),
    }
    if extra:
        rec.update(extra)
    rec["kill_POLY_ODE"] = None if rec["screens"]["POLY_ODE"] else killing(S)
    rec["kill_POLY"] = None if rec["screens"]["POLY"] else killing(
        S, polynomial_recenter=True, ode_nondegenerate=False)
    rec["kill_ODE"] = None if rec["screens"]["ODE"] else killing(
        S, polynomial_recenter=False, ode_nondegenerate=True)
    return rec


def compact_phi(ph):
    if not isinstance(ph, dict):
        return ph
    if ph.get("status") != "OK":
        return {"status": ph.get("status"), "u_s": ph.get("u_s"),
                "s": ph.get("s")}
    return {
        "n": ph["n"], "m": ph["m"], "M": ph["M"], "V": ph["V"],
        "k": ph["k"], "s_eff": ph["s_eff"], "dropped": ph["dropped"],
        "delta": ph["delta"], "delta2": ph["delta2"],
        "two_point": ph["two_point"],
    }


KEEP = ("t", "k_ap", "family", "status", "n", "m", "s", "M", "V",
        "u_s", "N", "screens", "poly_sites", "phi_eff",
        "kill_POLY_ODE", "kill_POLY", "kill_ODE", "label")


def slim_rec(rec):
    if not rec.get("screens"):
        return rec
    out = {}
    for kk in KEEP:
        if kk not in rec:
            continue
        vv = rec[kk]
        out[kk] = compact_phi(vv) if kk == "phi_eff" else vv
    return out


# ---------------------------------------------------------------------------
# p.207 closed-form control (charged phi_delta.py rows)
# ---------------------------------------------------------------------------
def control_phi10():
    rows = [
        (16, 12, 13, 3, 1, F(-1), F(1, 4)),
        (21, 14, 16, 2, 1, F(-1, 2), F(7, 6)),
        (21, 14, 18, 5, 1, F(-1), F(1, 3)),
        (15, 10, 11, 3, 2, F(-1), F(1, 2)),
        (15, 10, 11, 2, 2, F(-1), F(4, 3)),
    ]
    ok = True
    for n, m, M2, V2, k, pd2, pd1 in rows:
        d2 = gcd(n, m)
        Md = {1: -m, 2: M2}
        dd = {1: n, 2: d2, 3: gcd(d2, M2)}
        Vd = {2: V2, 3: dd[3]}
        raw2, raw1 = def51(n, Md, dd, Vd, 2, 2), def51(n, Md, dd, Vd, 2, 1)
        p2, p1 = (k + 1) * raw2, (k + 1) * raw1
        ok = ok and (p2 == pd2 and p1 == pd1)
    return ok


def cell_key(ph):
    if ph.get("status") != "OK":
        return ("us>1" if ph.get("u_s", 0) > 1 else ph.get("status"),
                "NA", "NA")
    return ("us=1", ph["s_eff"], "d2=-1" if ph["two_point"] else "not")


def main():
    t0 = time.perf_counter()
    print("== POST-POLY CENSUS  C_FULL_TREE_POLYNOMIAL_ODE + Φ_eff ==",
          flush=True)

    # ---- controls ----
    print("\n-- CONTROLS --", flush=True)
    check("phi 10/10 MATCH", control_phi10())

    moh = []
    for n, m, Ms, Vs, lab, *_ in M.MOH_TABLE:
        S = M.Skel(n, m, list(Ms), dict(Vs))
        moh.append((lab, S))
        scr = screens(S)
        check("Moh %s TREE" % lab, scr["TREE"])
        check("Moh %s ODE" % lab, scr["ODE"])
        check("Moh %s POLY" % lab, scr["POLY"])
        check("Moh %s POLY_ODE" % lab, scr["POLY_ODE"])

    n100_all = [M.Skel(n, m, list(Ms), V)
                for n in range(4, 101)
                for m, Ms, V in M.census(n, Kmin=2, full=True)]
    check("n<=100 (1)-(13) rows = 658", len(n100_all) == 658,
          "got %d" % len(n100_all))
    n100_classes = len({(S.n, S.m) for S in n100_all})
    check("n<=100 (n,m) classes = 63", n100_classes == 63,
          "got %d" % n100_classes)
    abort_if_failed("controls")

    # ---- (6)+(5) n<=100 residue ----
    t1 = time.perf_counter()
    print("\n-- n<=100 screens --", flush=True)
    n100_ode, n100_polyode = [], []
    for S in n100_all:
        if FT.full_tree_ode_ok(S):
            n100_ode.append(S)
        if FT.full_tree_polynomial_ode_ok(S):
            n100_polyode.append(S)
    printed_keys = set()
    for n, m, Ms, Vs, *_ in M.MOH_TABLE:
        S = M.Skel(n, m, list(Ms), dict(Vs))
        printed_keys.add(row_key(S))
    excess = [S for S in n100_polyode if row_key(S) not in printed_keys]
    moh_surv = [S for S in n100_polyode if row_key(S) in printed_keys]
    print("  n<=100 ODE %d  POLY_ODE %d  excess %d  moh-in-POLY %d  classes %d"
          % (len(n100_ode), len(n100_polyode), len(excess), len(moh_surv),
             len({(S.n, S.m) for S in n100_polyode})), flush=True)
    check("n<=100 POLY_ODE = 20", len(n100_polyode) == 20,
          "got %d" % len(n100_polyode))
    check("n<=100 excess = 14", len(excess) == 14, "got %d" % len(excess))
    check("Moh six inside POLY_ODE", len(moh_surv) == 6)
    abort_if_failed("n<=100 counts")

    excess_recs = [skel_record(S) for S in excess]
    moh_recs = [skel_record(S, extra={"label": lab}) for lab, S in moh]

    # ---- (1) K=16 ray t=1..8 ----
    print("\n-- K=16 ray t=1..8 --", flush=True)
    k16 = []
    k16_dicts = k16_family(list(range(1, 9)))
    for rec0 in k16_dicts:
        t = rec0.get("t")
        if rec0.get("status") != "ok":
            k16.append({"t": t, "status": rec0.get("status"),
                        "n": rec0.get("n"), "m": rec0.get("m")})
            print("  t=%s %s" % (t, rec0.get("status")), flush=True)
            continue
        S = try_skel(rec0["n"], rec0["m"], rec0["M"],
                     {int(k): int(v) for k, v in rec0["V"].items()})
        rec = skel_record(S, extra={"t": t, "family": "K16",
                                    "status": "ok"})
        k16.append(rec)
        print("  t=%d n=%d m=%d POLY_ODE=%s sites=%s kill=%s two=%s s_eff=%s"
              % (t, S.n, S.m, rec["screens"]["POLY_ODE"],
                 rec["poly_sites"]["sites"], rec["kill_POLY_ODE"],
                 rec["phi_eff"].get("two_point"), rec["phi_eff"].get("s_eff")),
              flush=True)

    # ---- (1) (d,e)-fixed ray t=6+9k, k=0..5 ----
    print("\n-- (d,e)-fixed ray seedB t=6+9k k=0..5 --", flush=True)
    seedB = M.Skel(108, 72, [84, 104, 106], {2: 8, 3: 8, 4: 3})
    check("seedB (1)-(13)", seedB.windows_ok() and seedB.full_ok())
    members = de_fixed_family(seedB, 8, {2: 2, 3: 0}, t_max=51)
    want_t = [6 + 9 * k for k in range(0, 6)]
    defixed = []
    by_t = {m.get("t"): m for m in members}
    for t in want_t:
        rec0 = by_t.get(t)
        k = (t - 6) // 9
        if rec0 is None or rec0.get("status") != "ok":
            defixed.append({"t": t, "k": k,
                            "status": None if rec0 is None else rec0.get("status")})
            print("  t=%s k=%s MISSING/FAIL %s" % (t, k, rec0), flush=True)
            continue
        S = try_skel(rec0["n"], rec0["m"], rec0["M"],
                     {int(a): int(b) for a, b in rec0["V"].items()})
        rec = skel_record(S, extra={"t": t, "k_ap": k, "family": "de-fixed",
                                    "status": "ok", "lam": 8})
        defixed.append(rec)
        print("  t=%d k=%d n=%d POLY_ODE=%s sites=%s kill=%s two=%s s_eff=%s"
              % (t, k, S.n, rec["screens"]["POLY_ODE"],
                 rec["poly_sites"]["sites"], rec["kill_POLY_ODE"],
                 rec["phi_eff"].get("two_point"), rec["phi_eff"].get("s_eff")),
              flush=True)
    # seed t=0 as extra
    rec_seed = skel_record(seedB, extra={"t": 0, "k_ap": None, "family": "de-fixed-seed"})
    print("  t=0 seed POLY_ODE=%s sites=%s" % (
        rec_seed["screens"]["POLY_ODE"], rec_seed["poly_sites"]["sites"]),
          flush=True)

    # ---- (2) 19 rigid ----
    print("\n-- 19 rigid expdim-0 --", flush=True)
    RIGID = [
        (60, 40, [-10, 45, 58], {2: 11, 3: 8, 4: 4}),
        (80, 60, [68, 78], {2: 7, 3: 3}),
        (84, 63, [49, 82], {2: 7, 3: 5}),
        (96, 72, [-8, 20, 94], {2: 7, 3: 6, 4: 3}),
        (96, 72, [-8, 76, 94], {2: 7, 3: 6, 4: 3}),
        (96, 72, [56, 92, 94], {2: 7, 3: 5, 4: 3}),
        (96, 72, [80, 84, 94], {2: 7, 3: 6, 4: 3}),
        (100, 75, [85, 98], {2: 7, 3: 3}),
        (108, 72, [60, 80, 106], {2: 20, 3: 9, 4: 3}),
        (108, 72, [60, 100, 106], {2: 20, 3: 9, 4: 3}),
        (108, 72, [90, 106], {2: 17, 3: 16}),
        (108, 72, [90, 99, 106], {2: 17, 3: 16, 4: 8}),
        (120, 72, [12, 44, 118], {2: 8, 3: 9, 4: 3}),
        (120, 72, [12, 76, 118], {2: 8, 3: 9, 4: 3}),
        (120, 90, [-10, 25, 118], {2: 7, 3: 6, 4: 3}),
        (120, 90, [-10, 95, 118], {2: 7, 3: 6, 4: 3}),
        (120, 90, [100, 105, 118], {2: 7, 3: 6, 4: 3}),
        (120, 80, [88, 118], {2: 17, 3: 7}),
        (120, 80, [100, 110, 118], {2: 17, 3: 16, 4: 9}),
    ]
    rigid = []
    for n, m, Ms, Vs in RIGID:
        S = M.Skel(n, m, list(Ms), dict(Vs))
        rec = skel_record(S)
        rigid.append(rec)
        print("  (%d,%d) M=%s V=%s us=%s POLY_ODE=%s ODE=%s TREE=%s kill=%s"
              % (n, m, Ms, Vs, rec["u_s"], rec["screens"]["POLY_ODE"],
                 rec["screens"]["ODE"], rec["screens"]["TREE"],
                 rec["kill_POLY_ODE"]), flush=True)
    check("19 rigid recovered", len(rigid) == 19)
    abort_if_failed("rigid")

    # ---- (3) D=108 ODE then POLY ----
    print("\n-- D=108 --", flush=True)
    d108_all = [M.Skel(108, m, list(Ms), V)
                for m, Ms, V in M.census(108, Kmin=16, full=True)]
    d108_ode = [S for S in d108_all if FT.full_tree_ode_ok(S)]
    d108_poly = [S for S in d108_ode if FT.full_tree_polynomial_ode_ok(S)]
    print("  (1)-(13) %d  ODE %d  POLY_ODE %d" % (
        len(d108_all), len(d108_ode), len(d108_poly)), flush=True)
    check("D=108 ODE = 20", len(d108_ode) == 20, "got %d" % len(d108_ode))
    d108_ode_recs = []
    for S in d108_ode:
        rec = skel_record(S)
        d108_ode_recs.append(rec)
        print("  ODE %s M=%s V=%s us=%s POLY=%s sites=%s kill=%s"
              % (("LIVE" if rec["screens"]["POLY_ODE"] else "DEAD"),
                 rec["M"], rec["V"], rec["u_s"], rec["screens"]["POLY_ODE"],
                 rec["poly_sites"]["sites"], rec["kill_POLY_ODE"]),
              flush=True)

    # ---- (4) 48 <= D <= 200 ----
    print("\n-- 48<=D<=200 Kmin=16 POLY_ODE residue --", flush=True)
    t_deg = time.perf_counter()
    baseline_deg = set()
    ode_deg = set()
    poly_rows = []
    ode_count = 0
    n_base = 0
    for n in range(48, 201):
        rows_n = [M.Skel(n, m, list(Ms), V)
                  for m, Ms, V in M.census(n, Kmin=16, full=True)]
        if rows_n:
            baseline_deg.add(n)
        n_base += len(rows_n)
        for S in rows_n:
            if FT.full_tree_ode_ok(S):
                ode_count += 1
                ode_deg.add(n)
                if FT.full_tree_polynomial_ode_ok(S):
                    poly_rows.append(S)
        if n % 16 == 0 or n in (108, 112, 120, 200):
            print("    n=%d  base_cum=%d  ode_cum=%d  poly_cum=%d  (%.1fs)"
                  % (n, n_base, ode_count, len(poly_rows),
                     time.perf_counter() - t_deg), flush=True)

    groups = defaultdict(list)
    for S in poly_rows:
        groups[group_key(S)].append(S)
    uni_groups = {gk for gk, items in groups.items()
                  if M.uni_hits([(S.V[2], S.q(), S.u) for S in items], 6, None)}
    poly_deg = {S.n for S in poly_rows}
    empty_now = sorted(baseline_deg - poly_deg)
    empty_vs_ode = sorted(ode_deg - poly_deg)
    print("  base rows %d deg %d; ODE rows %d deg %d; POLY rows %d groups %d UNI %d deg %d"
          % (n_base, len(baseline_deg), ode_count, len(ode_deg),
             len(poly_rows), len(groups), len(uni_groups), len(poly_deg)),
          flush=True)
    check("D<=200 POLY_ODE rows = 1420", len(poly_rows) == 1420,
          "got %d" % len(poly_rows))
    check("D<=200 POLY_ODE groups = 686", len(groups) == 686,
          "got %d" % len(groups))
    check("D<=200 POLY_ODE UNI = 459", len(uni_groups) == 459,
          "got %d" % len(uni_groups))

    # tabulate
    cells_rows = defaultdict(list)
    cells_groups = defaultdict(set)
    two_point_groups = {}  # gk -> representative info
    for S in poly_rows:
        ph = phi_eff(S)
        ck = cell_key(ph)
        cells_rows[ck].append(S)
        gk = group_key(S)
        cells_groups[ck].add(gk)
        if (ph.get("status") == "OK" and ph.get("u_s") == 1
                and ph.get("s_eff") == 2 and ph.get("two_point")):
            if gk not in two_point_groups:
                two_point_groups[gk] = {
                    "n": S.n, "m": S.m, "M": m_list(S), "V_s": S.V[S.s],
                    "s": S.s, "u_s": 1,
                    "V_paths": [],
                    "N": sorted({N for T in groups[gk] for N in uni_N(T)}),
                    "uni": gk in uni_groups,
                    "phi_eff": compact_phi(ph),
                }
            two_point_groups[gk]["V_paths"].append(v_map(S))

    table = []
    for ck in sorted(cells_rows, key=lambda x: (str(x[0]), str(x[1]), str(x[2]))):
        table.append({
            "u_s": ck[0], "s_eff": ck[1], "two_point": ck[2],
            "rows": len(cells_rows[ck]),
            "groups": len(cells_groups[ck]),
            "uni_groups": len(cells_groups[ck] & uni_groups),
        })
        print("  cell %s  rows=%d groups=%d uni=%d" % (
            ck, len(cells_rows[ck]), len(cells_groups[ck]),
            len(cells_groups[ck] & uni_groups)), flush=True)

    tp_list = sorted(two_point_groups.values(),
                     key=lambda r: (r["n"], r["m"], r["M"], r["V_s"]))
    print("  two-point s_eff=2 u_s=1 groups: %d" % len(tp_list), flush=True)

    per_degree = {}
    for n in sorted(poly_deg | set(empty_now) | {105, 108, 112, 117, 120}):
        nrows = [S for S in poly_rows if S.n == n]
        ngrp = {group_key(S) for S in nrows}
        nuni = ngrp & uni_groups
        per_degree[str(n)] = {
            "rows": len(nrows), "groups": len(ngrp), "uni": len(nuni),
        }

    elapsed = time.perf_counter() - t0
    print("\n== DONE in %.2fs (degree-scan %.2fs) ==" % (
        elapsed, time.perf_counter() - t_deg), flush=True)

    payload = {
        "screen": "C_FULL_TREE_POLYNOMIAL_ODE",
        "elapsed_s": elapsed,
        "controls": {
            "phi_10_of_10": True,
            "moh_six_all_columns": True,
            "n100_1_13": len(n100_all),
            "n100_classes": n100_classes,
        },
        "moh_six": [
            {"label": r.get("label"), "n": r["n"], "m": r["m"], "M": r["M"],
             "V": r["V"], "u_s": r["u_s"], "screens": r["screens"],
             "phi_eff": compact_phi(r["phi_eff"]),
             "poly_sites": r["poly_sites"]}
            for r in moh_recs
        ],
        "k16": [slim_rec(rec) for rec in k16],
        "de_fixed": [slim_rec(rec) for rec in defixed],
        "de_fixed_seed_t0": {
            "n": rec_seed["n"], "m": rec_seed["m"], "M": rec_seed["M"],
            "V": rec_seed["V"], "u_s": rec_seed["u_s"],
            "screens": rec_seed["screens"],
            "poly_sites": rec_seed["poly_sites"],
            "phi_eff": compact_phi(rec_seed["phi_eff"]),
            "kill_POLY_ODE": rec_seed["kill_POLY_ODE"],
        },
        "rigid19": [
            {"n": r["n"], "m": r["m"], "M": r["M"], "V": r["V"], "s": r["s"],
             "u_s": r["u_s"], "N": r["N"], "screens": r["screens"],
             "poly_sites": r["poly_sites"],
             "kill_POLY_ODE": r["kill_POLY_ODE"],
             "kill_POLY": r["kill_POLY"],
             "phi_eff": compact_phi(r["phi_eff"])}
            for r in rigid
        ],
        "d108": {
            "ode_rows": len(d108_ode),
            "poly_rows": len(d108_poly),
            "rows": [
                {"n": r["n"], "m": r["m"], "M": r["M"], "V": r["V"], "s": r["s"],
                 "u_s": r["u_s"], "N": r["N"], "screens": r["screens"],
                 "poly_sites": r["poly_sites"],
                 "kill_POLY_ODE": r["kill_POLY_ODE"],
                 "phi_eff": compact_phi(r["phi_eff"])}
                for r in d108_ode_recs
            ],
        },
        "n100": {
            "ode_rows": len(n100_ode),
            "poly_rows": len(n100_polyode),
            "classes": len({(S.n, S.m) for S in n100_polyode}),
            "excess": 14,
            "excess_rows": [
                {"n": r["n"], "m": r["m"], "M": r["M"], "V": r["V"], "s": r["s"],
                 "u_s": r["u_s"], "N": r["N"],
                 "poly_sites": r["poly_sites"],
                 "phi_eff": compact_phi(r["phi_eff"])}
                for r in excess_recs
            ],
        },
        "D48_200": {
            "baseline_rows": n_base,
            "baseline_degrees": sorted(baseline_deg),
            "ode_rows": ode_count,
            "poly_rows": len(poly_rows),
            "poly_groups": len(groups),
            "poly_uni": len(uni_groups),
            "poly_degrees": sorted(poly_deg),
            "empty_now": empty_now,
            "empty_vs_ode": empty_vs_ode,
            "table": table,
            "per_degree": per_degree,
            "two_point_s2_us1_groups": tp_list,
        },
        "failures": FAILURES,
    }
    out = HERE / "results.json"
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print("Wrote %s (%.1f KB)" % (out, out.stat().st_size / 1024), flush=True)


if __name__ == "__main__":
    main()
