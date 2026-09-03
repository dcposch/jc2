#!/usr/bin/env python3
"""Targeted (d,e)-fixed linear extensions of D=108 congruence-clean seeds,
plus the K=16 comparison family (which does not keep (d,e)).

Must be run after rigid_congruence.py's imports work (same directory).
"""
from __future__ import annotations

import json
import sys
import time
from fractions import Fraction as F
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "repro"))
import moh_skeleton_full as M  # noqa: E402
import full_tree_partition as FT  # noqa: E402
from rigid_congruence import (  # noqa: E402
    gap_ok, screen_bundle, selected_path, node_tuple, gap_tree,
    uni_packets, try_skel, u_s_of, v_map, m_list, congruence_dump,
    descend_once, appendix2_size, row_record,
)


def nodes_of(S):
    T = gap_tree(S)
    path = selected_path(S)
    out = []
    for j in range(S.s - 1, 1, -1):
        out.append(node_tuple(T, j, path))
        path = T.extend(path, j, S.V[j])
    return out


def eval_member(S):
    if S is None:
        return None
    sb = screen_bundle(S)
    uni = uni_packets(S)
    nd = nodes_of(S)
    cong = all((nt["A_divides_P"] or not nt["forced_major_zero"]) for nt in nd)
    strict = all(nt["A_divides_P"] for nt in nd)
    return {
        "n": S.n, "m": S.m, "M": m_list(S), "V": v_map(S),
        "s": S.s, "K": S.K, "de": [S.dd, S.e],
        "u_s": u_s_of(S),
        "q": str(S.q()),
        "u": str(S.u),
        "ok13": bool(S.windows_ok() and S.full_ok()),
        "screens": {k: sb[k] for k in
                    ("gap_partition", "gap_ode", "gap_passport",
                     "C_FULL_TREE", "C_FULL_TREE_ODE")},
        "uni_N": [p["N"] for p in uni],
        "nodes": [
            {k: nt[k] for k in ("j", "A", "P", "Q", "P_mod_A", "h",
                                "A_divides_P", "forced_major_zero", "Q_gt_P")}
            for nt in nd
        ],
        "cong_b_le_h_or_div": cong,
        "cong_A_div_P": strict,
        "screened": bool(sb["gap_partition"] and uni and min(p["N"] for p in uni) >= 6),
        "screened_passport": bool(sb["gap_passport"] and uni and min(p["N"] for p in uni) >= 6),
        "screened_tree": bool(sb["C_FULL_TREE"] and uni and min(p["N"] for p in uni) >= 6),
    }


def de_fixed_family(seed, lam, vslopes, t_max=40):
    """n=e*(K0+lam t), m=d*(K0+lam t), M_i = n - w_i (i<s), M_s=n-2."""
    d, e, K0 = seed.dd, seed.e, seed.K
    windows = {i: seed.n - seed.M[i] for i in range(2, seed.s)}
    members = []
    for t in range(0, t_max + 1):
        K = K0 + lam * t
        if K < 4:
            members.append({"t": t, "status": "K<4"})
            continue
        n, m = e * K, d * K
        if gcd(d, e) != 1:
            members.append({"t": t, "status": "de-not-coprime"})
            continue
        Ms = []
        for i in range(2, seed.s + 1):
            Ms.append(n - 2 if i == seed.s else n - windows[i])
        Vs = dict(v_map(seed))
        for i, sl in vslopes.items():
            Vs[i] = Vs[i] + sl * t
        S = try_skel(n, m, Ms, Vs)
        if S is None:
            members.append({"t": t, "status": "not-(1)-(13)",
                            "n": n, "m": m, "M": Ms, "V": Vs, "K": K})
            continue
        rec = eval_member(S)
        rec["t"] = t
        rec["status"] = "ok"
        rec["lam"] = lam
        rec["vslopes"] = vslopes
        members.append(rec)
    return members


def k16_family(t_values):
    """AUDIT 17(v) comparison: e=3t+1, d=2t+1, n=16e, m=16d,
    M=(n-12, n-2), V2=V3=3.  Does NOT keep (d,e)."""
    out = []
    for t in t_values:
        e = 3 * t + 1
        d = 2 * t + 1
        if gcd(d, e) != 1:
            out.append({"t": t, "status": "de-not-coprime", "d": d, "e": e})
            continue
        n, m = 16 * e, 16 * d
        Ms = [n - 12, n - 2]
        Vs = {2: 3, 3: 3}
        S = try_skel(n, m, Ms, Vs)
        if S is None:
            out.append({"t": t, "status": "not-(1)-(13)", "n": n, "m": m, "M": Ms, "V": Vs,
                        "de": [d, e]})
            continue
        rec = eval_member(S)
        rec["t"] = t
        rec["status"] = "ok"
        rec["family"] = "K16"
        out.append(rec)
    return out


def summarise(members, label):
    ok = [m for m in members if m.get("status") == "ok"]
    scr = [m for m in ok if m.get("screened")]
    scrp = [m for m in ok if m.get("screened_passport")]
    scrt = [m for m in ok if m.get("screened_tree")]
    cong = [m for m in ok if m.get("cong_A_div_P") and m.get("screened")]
    print("== %s ==" % label)
    print("  defined(1-13) %d / screened-gap %d / passport %d / TREE %d / A|P+screened %d" %
          (len(ok), len(scr), len(scrp), len(scrt), len(cong)))
    print("  screened t:", [m["t"] for m in scr])
    print("  passport t:", [m["t"] for m in scrp])
    print("  TREE t:", [m["t"] for m in scrt])
    print("  A|P t:", [m["t"] for m in cong])
    for m in members[:12]:
        if m.get("status") != "ok":
            print("   t=%s %s n=%s V=%s" % (m.get("t"), m.get("status"), m.get("n"), m.get("V")))
            continue
        nd = m["nodes"]
        bits = ["j%s A=%s P=%s b=%s" % (x["j"], x["A"], x["P"], x["P_mod_A"]) for x in nd]
        print("   t=%s n=%s m=%s M=%s V=%s N=%s gap=%s pass=%s TREE=%s A|P=%s  %s" %
              (m["t"], m["n"], m["m"], m["M"], m["V"], m["uni_N"],
               m["screens"]["gap_partition"], m["screens"]["gap_passport"],
               m["screens"]["C_FULL_TREE"], m["cong_A_div_P"], " | ".join(bits)))
    if len(members) > 12:
        print("   ... (%d total t)" % len(members))
        for m in members[-3:]:
            if m.get("status") == "ok":
                print("   t=%s n=%s V=%s N=%s gap=%s TREE=%s A|P=%s" %
                      (m["t"], m["n"], m["V"], m["uni_N"],
                       m["screens"]["gap_partition"], m["screens"]["C_FULL_TREE"],
                       m["cong_A_div_P"]))
    return {
        "label": label,
        "n_defined": len(ok),
        "screened_t": [m["t"] for m in scr],
        "passport_t": [m["t"] for m in scrp],
        "tree_t": [m["t"] for m in scrt],
        "Adiv_t": [m["t"] for m in cong],
        "members": members,
    }


def second_descent(desc):
    """If s'=3 and u_s'=1, descend again toward Appendix II."""
    if not desc or desc.get("status") != "DESCENDED":
        return None
    if desc.get("s") != 3:
        return None
    n, m = desc["n"], desc["m"]
    M = desc["M"]  # [M2, M3]
    V = desc["V"]  # [V2, V3]
    try:
        S = M.Skel(n, m, list(M), {2: V[0], 3: V[1]})
    except Exception:
        return {"status": "NOT-A-SKEL", "n": n, "m": m, "M": M, "V": V}
    d2 = descend_once(S)
    a2 = appendix2_size(d2) if d2.get("status") == "DESCENDED" else None
    return {"skel_ok": S.windows_ok() and S.full_ok(),
            "u_s": u_s_of(S), "second": d2, "appendix2": a2}


def main():
    t0 = time.time()
    # Seed A: D=108 s=3, A2|P2 (the first ODE UNI survivor)
    seedA = M.Skel(108, 72, [81, 106], {2: 7, 3: 7})
    assert seedA.full_ok() and gap_ok(seedA, True, True)
    # Seed B: D=108 s=4, A_j|P_j at both nodes
    seedB = M.Skel(108, 72, [84, 104, 106], {2: 8, 3: 8, 4: 3})
    assert seedB.full_ok() and gap_ok(seedB, True, True)
    # Seed C: rigid D=108 TREE survivor
    seedC = M.Skel(108, 72, [90, 99, 106], {2: 17, 3: 16, 4: 8})
    assert seedC.full_ok() and FT.full_tree_ok(seedC)

    print("seedA", m_list(seedA), v_map(seedA), nodes_of(seedA))
    print("seedB", m_list(seedB), v_map(seedB), nodes_of(seedB))
    print("seedC", m_list(seedC), v_map(seedC), nodes_of(seedC))

    results = []
    # Seed A: λ multiples that keep d3=gcd(K,27)=9, V2 slope to hold windows
    for lam in (9, 18, 27, 36, 54, 72, 108):
        for a in (0, 1, 2, 3, 4):
            for b in (0, 1, -1):
                mem = de_fixed_family(seedA, lam, {2: a, 3: b}, t_max=24)
                scr = [m for m in mem if m.get("screened")]
                if len(scr) >= 3 or (a, b, lam) in ((0, 0, 36), (1, 0, 36), (2, 0, 36), (1, 0, 27)):
                    results.append(summarise(mem, "A lam=%s V2'=%s V3'=%s" % (lam, a, b)))

    # Seed B
    for lam in (4, 8, 12, 24, 36, 48, 72, 108):
        for a in (0, 1, 2):
            for b in (0, 1, -1):
                mem = de_fixed_family(seedB, lam, {2: a, 3: b}, t_max=24)
                scr = [m for m in mem if m.get("screened")]
                if len(scr) >= 3 or (a, b) == (0, 0) and lam in (12, 24, 36):
                    results.append(summarise(mem, "B lam=%s V2'=%s V3'=%s" % (lam, a, b)))

    # Seed C (rigid)
    for lam in (6, 12, 18, 36, 72):
        for a in (0, 1, -1):
            mem = de_fixed_family(seedC, lam, {2: a, 3: 0}, t_max=16)
            scr = [m for m in mem if m.get("screened")]
            if len(scr) >= 2 or a == 0:
                results.append(summarise(mem, "C lam=%s V2'=%s" % (lam, a)))

    # K=16 comparison, t=1..20 plus a few larger
    k16 = k16_family(list(range(1, 21)) + [30, 40, 50])
    results.append(summarise(k16, "K16 comparison (d,e) NOT fixed"))

    # pick best (d,e)-fixed
    best = None
    for r in results:
        if r["label"].startswith("K16"):
            continue
        n = len(r["screened_t"])
        if best is None or n > len(best["screened_t"]):
            best = r
    print("\nBEST (d,e)-fixed screened count:", None if best is None else
          (best["label"], len(best["screened_t"]), best["screened_t"][:20]))

    # second descent on rigid u_s=1 s'=3 rows
    print("\n== second descent on rigid u_s=1 ==")
    rigid_second = []
    specs = [
        (60, 40, [-10, 45, 58], {2: 11, 3: 8, 4: 4}),
        (80, 60, [68, 78], {2: 7, 3: 3}),
        (96, 72, [-8, 20, 94], {2: 7, 3: 6, 4: 3}),
        (96, 72, [-8, 76, 94], {2: 7, 3: 6, 4: 3}),
        (96, 72, [56, 92, 94], {2: 7, 3: 5, 4: 3}),
        (96, 72, [80, 84, 94], {2: 7, 3: 6, 4: 3}),
        (108, 72, [60, 80, 106], {2: 20, 3: 9, 4: 3}),
        (108, 72, [60, 100, 106], {2: 20, 3: 9, 4: 3}),
        (108, 72, [90, 99, 106], {2: 17, 3: 16, 4: 8}),
        (120, 72, [12, 44, 118], {2: 8, 3: 9, 4: 3}),
        (120, 72, [12, 76, 118], {2: 8, 3: 9, 4: 3}),
        (120, 80, [88, 118], {2: 17, 3: 7}),
        (120, 80, [100, 110, 118], {2: 17, 3: 16, 4: 9}),
    ]
    for n, m, Ms, Vs in specs:
        S = M.Skel(n, m, list(Ms), Vs)
        d1 = descend_once(S)
        d2 = second_descent(d1)
        print(" ", n, m, Ms, "desc1", d1.get("status"), d1.get("n"), d1.get("m"),
              d1.get("M"), d1.get("V"), "s", d1.get("s"),
              "desc2", None if not d2 else (d2.get("skel_ok"), d2.get("u_s"),
                                            (d2.get("second") or {}).get("status"),
                                            (d2.get("appendix2") or {}).get("status"),
                                            (d2.get("appendix2") or {}).get("n_ord")))
        rigid_second.append({"n": n, "m": m, "M": Ms, "V": Vs,
                             "first": {k: d1.get(k) for k in
                                       ("status", "n", "m", "M", "V", "k", "s",
                                        "us", "anchor_zero", "K")},
                             "second": d2})

    payload = {
        "families": [
            {k: v for k, v in r.items() if k != "members"} |
            {"n_members_recorded": len(r["members"]),
             "screened_members": [m for m in r["members"] if m.get("screened")]}
            for r in results
        ],
        "best_de_fixed": None if best is None else {
            "label": best["label"],
            "screened_t": best["screened_t"],
            "passport_t": best["passport_t"],
            "tree_t": best["tree_t"],
            "Adiv_t": best["Adiv_t"],
            "screened_members": [m for m in best["members"] if m.get("screened")],
        },
        "k16": {
            "screened_t": [m["t"] for m in k16 if m.get("screened")],
            "passport_t": [m["t"] for m in k16 if m.get("screened_passport")],
            "tree_t": [m["t"] for m in k16 if m.get("screened_tree")],
            "Adiv_t": [m["t"] for m in k16 if m.get("cong_A_div_P") and m.get("screened")],
            "members": [m for m in k16 if m.get("status") == "ok"],
        },
        "rigid_second_descent": rigid_second,
        "elapsed": time.time() - t0,
    }
    out = HERE / "ray-construction.json"
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print("\nWrote %s in %.2fs" % (out, time.time() - t0))


if __name__ == "__main__":
    main()
