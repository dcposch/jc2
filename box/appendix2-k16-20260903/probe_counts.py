#!/usr/bin/env python3
"""Shape / Phi_eff / D1-inventory counts.  No Groebner."""
from __future__ import annotations

import ast
import json
import os
import sys
from fractions import Fraction as F
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
BOX = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, BOX)

import moh_skeleton_full as MS
from compile import compile_row
from descent_core import u_s_of
from phi_eff import descend_phi_eff, shape_of_eff
from shape import shape_bundle, h_monomials, beta_monomials

LANE_JSON = "/tmp/jc2-lane.R3BIWM/inputs/full-tree-ode-excess-witnesses.json"


def coeff_monomials(delta1, i, K, max_a):
    out = []
    for b in range(K):
        for a in range(0, max_a + 1):
            if F(a) <= delta1 * F(b + i):
                out.append((a, b))
    return out


def d1_ab_inventory(C):
    """Full D1 count of alpha_i (i=1..e') and beta_i (i=2..d') plus h_free + c."""
    if not C.get("ok"):
        return dict(ok=False, reason=C.get("reason"))
    d1, K, dp, ep, u = C["delta1"], C["K"], C["dprime"], C["eprime"], C["u"]
    n_a = []
    n_b = []
    for i in range(1, ep + 1):
        mons = coeff_monomials(d1, i, K, i)
        n_a.append(len(mons))
    for i in range(2, dp + 1):
        mons = coeff_monomials(d1, i, K, i)
        n_b.append(len(mons))
    n_h = C["n_h"]
    n_full = n_h + sum(n_a) + sum(n_b) + 1
    n_full_a1abs = n_h + sum(n_a[1:]) + sum(n_b) + 1  # alpha1 absorbed
    # Horner-cap (p.208 pattern): dim(i) = min(i, K) for i < last, last of g is K-1
    # alpha1 absorbed: 0; alpha_i i=2..e'-1: min(i, K); alpha_e': K-1 (A,B,z no 1)
    # beta_i i=2..d': min(i, K)  [last beta keeps constant, as p.208 beta3]
    def horner_dim_alpha(i, last):
        if i == 1:
            return 0  # absorbed
        if i == last:
            return min(K - 1, i)  # {A,...,z} no constant; K-1 = 3 for K=4
        return min(i, K)
    def horner_dim_beta(i, last):
        return min(i, K)
    hcap_a = [horner_dim_alpha(i, ep) for i in range(1, ep + 1)]
    hcap_b = [horner_dim_beta(i, dp) for i in range(2, dp + 1)]
    n_hcap = n_h + sum(hcap_a) + sum(hcap_b) + 1
    return dict(
        ok=True,
        n_h=n_h, n_beta_ord=C["n_beta"], n_ord=C["n_ord"], n_ab=C["n_ab"],
        n_alpha_d1=n_a, n_beta_d1=n_b,
        n_full_d1=n_full, n_full_d1_a1abs=n_full_a1abs,
        hcap_alpha=hcap_a, hcap_beta=hcap_b, n_hcap=n_hcap,
        K=K, dprime=dp, eprime=ep, u=u,
        two_point=C["two_point"], delta1=str(C["delta1"]), delta2=str(C["delta2"]),
        h_free=C["h_free"], lead=dict((str(k), v) for k, v in C["lead"].items()),
    )


def k16_parent(t):
    n = 48 * t + 16
    m = 32 * t + 16
    Ms = [n - 12, n - 2]
    V = {2: 3, 3: 3}
    return n, m, Ms, V


def load_excess_52():
    with open(LANE_JSON) as f:
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
        out.append((108, m, list(Ms), dict(V)))
    return out


def summarize_eff(tag, recs):
    n_seff2 = sum(1 for r in recs if r.get("s_eff") == 2)
    n_drop = sum(1 for r in recs if r.get("dropped"))
    n_usgt1 = sum(1 for r in recs if r.get("status") == "US-GT-1")
    print("  %s: N=%d  us>1=%d  drop>0=%d  s_eff=2=%d" % (
        tag, len(recs), n_usgt1, n_drop, n_seff2))
    return n_seff2


def main():
    print("== K16 ray shapes t=1,2,3 ==")
    for t in (1, 2, 3):
        n, m, Ms, V = k16_parent(t)
        S = MS.Skel(n, m, Ms, V)
        rec = descend_phi_eff(S)
        print("  t=%d parent (%s,%s) M=%s V=%s us=%s" % (t, n, m, Ms, V, rec["us"]))
        print("    child n'=%s m'=%s M'=%s k=%s s'=%s den=%s drop=%s s_eff=%s" % (
            rec.get("n_prime"), rec.get("m_prime"), rec.get("M_prime"),
            rec.get("k"), rec.get("s_prime"), rec.get("den_raw"),
            rec.get("dropped"), rec.get("s_eff")))
        row = compile_row(n, m, Ms, V, lab="K16 t=%d" % t, solve=False)
        print("    compile_row verdict=%s n_unk=%s sprime=%s phi=%s" % (
            row.get("verdict"), row.get("n_unknowns"), row.get("sprime"),
            row.get("phi")))
        sh = row.get("shape") or {}
        print("    shape n_h=%s n_beta=%s n_ord=%s n_ab=%s two_point=%s d'=%s e'=%s u=%s h_free=%s" % (
            sh.get("n_h"), sh.get("n_beta"), sh.get("n_ord"), sh.get("n_ab"),
            sh.get("two_point"), sh.get("dprime"), sh.get("eprime"), sh.get("u"),
            sh.get("h_free")))
        args = rec.get("shape_args")
        C = shape_bundle(args["n"], args["m"], args["M2"], args["V2"], args["k"])
        inv = d1_ab_inventory(C)
        print("    D1-full a1kept=%s a1abs=%s  Horner-cap=%s  alpha_d1=%s beta_d1=%s" % (
            inv.get("n_full_d1"), inv.get("n_full_d1_a1abs"), inv.get("n_hcap"),
            inv.get("n_alpha_d1"), inv.get("n_beta_d1")))
        print("    hcap alpha=%s beta=%s  (12)/(13)=%s b12=%s" % (
            inv.get("hcap_alpha"), inv.get("hcap_beta"), sh.get("ok1213"), sh.get("b12")))

    print("\n== 52 excess + Phi_eff ==")
    excess = load_excess_52()
    print("  loaded", len(excess))
    recs52 = []
    seff2_52 = []
    for (n, m, Ms, V, key) in excess:
        S = MS.Skel(n, m, list(Ms), dict(V))
        rec = descend_phi_eff(S)
        rec["key"] = key
        recs52.append(rec)
        if rec.get("s_eff") == 2:
            C = shape_of_eff(rec)
            inv = d1_ab_inventory(C) if C.get("ok") else dict(ok=False, reason=C.get("reason"))
            rec["inv"] = {k: inv[k] for k in inv if k not in ("h_free", "lead", "n_alpha_d1", "n_beta_d1", "hcap_alpha", "hcap_beta")}
            seff2_52.append(rec)
            budget = None
            if C.get("ok"):
                # in-budget if any of n_ab, n_ord, n_hcap, n_full <= 40
                cands = [inv.get("n_ab"), inv.get("n_ord"), inv.get("n_hcap"),
                         inv.get("n_full_d1_a1abs")]
                cands = [x for x in cands if isinstance(x, int)]
                budget = min(cands) if cands else None
            rec["min_count"] = budget
            print("    s_eff=2  (%s,%s) M=%s V=%s -> n'=%s m'=%s M2'=%s V2'=%s k=%s  shape=%s min_count=%s two_pt=%s d'=%s n_ord=%s n_ab=%s n_hcap=%s" % (
                n, m, Ms, V, rec["n_prime"], rec["m_prime"],
                rec.get("shape_args", {}).get("M2"), rec.get("shape_args", {}).get("V2"),
                rec.get("k"), C.get("reason") if not C.get("ok") else "OK",
                budget, (C.get("two_point") if C.get("ok") else None),
                (C.get("dprime") if C.get("ok") else None),
                (C.get("n_ord") if C.get("ok") else None),
                (C.get("n_ab") if C.get("ok") else None),
                inv.get("n_hcap")))
    summarize_eff("52", recs52)
    print("  s_eff=2 listed:", len(seff2_52))
    in40 = [r for r in seff2_52 if isinstance(r.get("min_count"), int) and r["min_count"] <= 40]
    print("  s_eff=2 with some count<=40:", len(in40))

    print("\n== D=108 us1 C_FULL_TREE + Phi_eff ==")
    d108 = load_d108_us1()
    print("  loaded", len(d108))
    recs108 = []
    seff2_108 = []
    for (n, m, Ms, V) in d108:
        S = MS.Skel(n, m, list(Ms), dict(V))
        rec = descend_phi_eff(S)
        recs108.append(rec)
        if rec.get("s_eff") == 2:
            C = shape_of_eff(rec)
            inv = d1_ab_inventory(C) if C.get("ok") else dict(ok=False, reason=C.get("reason"))
            rec["inv"] = {k: inv[k] for k in inv if k not in ("h_free", "lead", "n_alpha_d1", "n_beta_d1", "hcap_alpha", "hcap_beta")}
            seff2_108.append(rec)
            cands = [inv.get("n_ab"), inv.get("n_ord"), inv.get("n_hcap"),
                     inv.get("n_full_d1_a1abs")] if C.get("ok") else []
            cands = [x for x in cands if isinstance(x, int)]
            budget = min(cands) if cands else None
            rec["min_count"] = budget
            print("    s_eff=2  m=%s M=%s V=%s -> n'=%s m'=%s M2'=%s V2'=%s k=%s  shape=%s min_count=%s two_pt=%s d'=%s n_ord=%s n_ab=%s n_hcap=%s" % (
                m, Ms, V, rec["n_prime"], rec["m_prime"],
                rec.get("shape_args", {}).get("M2"), rec.get("shape_args", {}).get("V2"),
                rec.get("k"), C.get("reason") if not C.get("ok") else "OK",
                budget, (C.get("two_point") if C.get("ok") else None),
                (C.get("dprime") if C.get("ok") else None),
                (C.get("n_ord") if C.get("ok") else None),
                (C.get("n_ab") if C.get("ok") else None),
                inv.get("n_hcap")))
    summarize_eff("D108", recs108)
    print("  s_eff=2 listed:", len(seff2_108))
    in40 = [r for r in seff2_108 if isinstance(r.get("min_count"), int) and r["min_count"] <= 40]
    print("  s_eff=2 with some count<=40:", len(in40))

    sink = os.path.join(HERE, "probe_counts.json")
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
        json.dump(conv(dict(
            seff2_52=[{k: r[k] for k in r if k not in ("V_prime", "d_prime", "V_eff", "d_eff")}
                      for r in seff2_52],
            seff2_108=[{k: r[k] for k in r if k not in ("V_prime", "d_prime", "V_eff", "d_eff")}
                       for r in seff2_108],
            n52=len(recs52), n108=len(recs108),
            n_seff2_52=len(seff2_52), n_seff2_108=len(seff2_108),
        )), f, indent=2, sort_keys=True)
    print("wrote", sink)


if __name__ == "__main__":
    main()
