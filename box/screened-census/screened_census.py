#!/usr/bin/env python3
"""SCREENED CENSUS -- C_FULL_TREE / C_FULL_TREE_ODE composed with nested-pack.

Lane screened-census-grok46-20260903.  Standard library (+ optional sympy).

Composes, per PATH-ARITH(1)--(13) V-assignment:
  C_FULL_TREE (bare), C_FULL_TREE_ODE (operative sharpening),
  and typed SIDE columns C_FULL_TREE_PASSPORT (EXTERNAL) and
  +RECENTER / POLY+ODE (OPEN[FULL-TREE-RECENTER]),
with the exact parent-indexed nested-pack orbit knapsack (N>=6 and [6,16]).

Fail-closed: hash gate; Moh's six survive every screen; unscreened columns
must reproduce 1189 / 587 / 470 groups at D<=120 and 14016 groups at D<=200.
Tree DP state carries the higher V-tuple (Def 5.1(3)).  Passport and
recenter are NEVER folded into operative numbers.

Imports frozen drivers; does not modify them.  No jc2-lean, no ledger.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import sys
import time
from collections import defaultdict
from fractions import Fraction as F
from math import gcd  # noqa: F401  (kept for local algebra helpers)
from pathlib import Path

REPO = Path("/home/ubuntu/jc2")
FROZEN = Path("/tmp/jc2-lane.LGjDKK/inputs")
HERE = Path(__file__).resolve().parent
MOHPROG = REPO / "box" / "mohprog-drivers-20260903"
ORBITS = REPO / "box" / "branch-orbits-v2-20260903"

EXPECTED_SHA = {
    "moh-program-review-sol56-20260903.md":
        "e4bbb5f8e431baed488a2a3dfd856a3f7c4ea7ea006690bcc116f0db9ee60c45",
    "whole-tree-review-grok46-20260903.md":
        "9497e23140ca2c92f99f706e23affbaaaf4dfdab63ce7b93b5dea76933aabf6d",
    "full_tree_partition.py":
        "875c098a2a9465e146c77757e3d197be8af35f46ee4e772321acf8ca33b5fef8",
    "candidate_eval.py":
        "5d1b21222eecc448975c83d3628c22ada5cd26737155ecf2a7a27304ec40e553",
    "tree-independent.py":
        "c2a27632d54576abbca54b9f268a7fa5d2b144497a1e364c93102450a066baf9",
    "nested_pack.py":
        "36b374b21b3768e841ad2cc2168d7e669d9b0d6e6b6c8d1737d203acbd079067",
    "nested-pack-dp-grok46-20260903.md":
        "53d3464817f5c777d0cb106806d590f62556eb8a8dc18c12fc810eb2476cf065",
    "n6-family-review-grok46-20260903.md":
        "982c75da179e263e109d0bf6ba0e8b13e591225c80d0111d24ba32b61be67896",
    "moh_skeleton_full.py":
        "d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2",
}

os.environ.setdefault("JC2_INPUTS", str(FROZEN))
sys.path.insert(0, str(ORBITS))
sys.path.insert(0, str(MOHPROG))

import full_tree_partition as FT  # noqa: E402
import nested_pack as NP  # noqa: E402
from knapsack_v2 import (  # noqa: E402
    Skel, census, MOH_TABLE, packets, orbit_sizes, Umax,
)

FAILURES = []
NCHECK = [0]
TIME_BUDGET_S = 1140.0  # ~19 min for the degree loop; desk-scale < 20 min
DLO, DHI_TARGET = 48, 400
LISTING = (108, 112, 120)
SIDE_DHI = 200  # passport / recenter as far as this, then if time remains


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def check(name, cond, detail=""):
    NCHECK[0] += 1
    if cond:
        print("  [ok]   %s" % name, flush=True)
    else:
        print("  [FAIL] %s   %s" % (name, detail), flush=True)
        FAILURES.append(name)
    return cond


def abort_if_failed(stage):
    if FAILURES:
        print("%s FAILED: %s" % (stage, FAILURES), flush=True)
        sys.exit(1)


def load_tree_independent():
    path = MOHPROG / "tree-independent.py"
    spec = importlib.util.spec_from_file_location("tree_independent", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def row_key(S):
    return (S.n, S.m, tuple(S.M[i] for i in range(2, S.s + 1)),
            tuple((i, S.V[i]) for i in range(2, S.s + 1)))


def group_key(S):
    return (S.m, tuple(S.M[i] for i in range(2, S.s + 1)), S.V[S.s])


def printed_keys():
    return {
        (n, m, tuple(Ms), tuple(sorted(Vs.items())))
        for n, m, Ms, Vs, *_ in MOH_TABLE
    }


def u_s_of(S):
    return int(S.d[S.s] - S.V[S.s])


def minor_delta_sm1(S):
    """Def 5.1(3) at i=s-1 for the complementary top factor u_s = d_s - V_s."""
    us = u_s_of(S)
    if us <= 0:
        return None
    n, M, d, s = S.n, S.M, S.d, S.s
    num = F(n - M[s - 1]) * (us * (n - M[s]) - d[s])
    den = F(n - M[s] - 1) * (us * (n - M[s - 1]) - d[s])
    if den == 0:
        return None
    return 1 - num / den


def prop63_datum(S):
    us = u_s_of(S)
    vs = int(S.V[S.s])
    ds = int(S.d[S.s])
    if us == 1:
        return {
            "u_s": us, "v_s": vs, "d_s": ds,
            "prop63": True,
            "reason": "u_s=1 (Prop 6.4: hypothesis of Prop 6.3 automatic)",
            "delta_star_sm1": None,
            "vs_over_us": str(vs),
        }
    dmin = minor_delta_sm1(S)
    thresh = F(vs, us) if us else None
    ok = (dmin is not None and thresh is not None and dmin >= thresh)
    return {
        "u_s": us, "v_s": vs, "d_s": ds,
        "prop63": bool(ok),
        "reason": ("delta*_s-1 = %s %s v_s/u_s = %s" %
                   (dmin, ">=" if ok else "<", thresh)),
        "delta_star_sm1": str(dmin) if dmin is not None else None,
        "vs_over_us": str(thresh) if thresh is not None else None,
    }


def j2_pack(S):
    """Forced-zero data at j=2 (the kill mechanism of the two dead rays)."""
    P = S.V[3] * S.d[2] // S.d[3]
    A = int(S.A(2))
    h = F(S.d[2], S.n - S.M[2])
    bmin = P % A
    return {
        "P": int(P), "A2": A, "h": str(h), "bmin": int(bmin),
        "P_mod_A2": int(bmin),
        "forced_major_zero": bool(bmin > h),
        "P_div_A2": (bmin == 0),
        "bmin_le_h": bool(bmin <= h),
    }


def cond_bits(S):
    bits = []
    for j in range(2, S.s):
        _ok, b10, b11 = S.cond1011(j)
        bits.append({
            "j": j, "A": int(S.A(j)), "V": int(S.V[j]),
            "by10": bool(b10), "by11": bool(b11),
            "Q": int(NP.Q_of(S, j)),
        })
    return bits


def packet_list(S, Nhi):
    out = []
    for w, c, om, tag in packets(S, Nhi):
        out.append({"w": int(w), "c": str(c), "om": int(om), "tag": tag})
    return out


def nested_of(skels):
    if not skels:
        return {
            "Ns6": [], "Ns16": [], "nest6": False, "nest16": False,
            "cap": False, "nstates": 0,
        }
    Um = Umax(skels)
    Nhi6 = max(Um, F(6))
    vals, cap, nstates = NP.nested_values(skels, Nhi6)
    Ns6 = sorted(NP.ints_in(vals, 6, Nhi6))
    Ns16 = [N for N in Ns6 if N <= 16]
    return {
        "Ns6": Ns6, "Ns16": Ns16,
        "nest6": bool(Ns6) or cap, "nest16": bool(Ns16) or cap,
        "cap": bool(cap), "nstates": int(nstates),
        "Nhi": str(Nhi6), "u": str(skels[0].u),
    }


def clear_tree():
    FT._EVALUATORS.clear()


def screens_of(S, want_side):
    """Evaluate TREE then restrictions. Side columns only if want_side."""
    tree = bool(FT.full_tree_ok(S))
    ode = bool(FT.full_tree_ode_ok(S)) if tree else False
    out = {"tree": tree, "ode": ode, "pass": False, "poly": False, "polyode": False}
    if not want_side or not tree:
        return out
    out["poly"] = bool(FT.full_tree_polynomial_ok(S))
    if ode:
        out["pass"] = bool(FT.full_tree_passport_ok(S))
    if out["poly"] and ode:
        out["polyode"] = bool(FT.full_tree_polynomial_ode_ok(S))
    return out


def hash_gate():
    print("\n-- HASH GATE (frozen inputs) --", flush=True)
    bad = []
    for name, expect in EXPECTED_SHA.items():
        path = FROZEN / name
        if not path.is_file():
            bad.append((name, "MISSING"))
            check("sha256 %s" % name, False, "missing")
            continue
        got = sha256_file(path)
        ok = got == expect
        check("sha256 %s" % name, ok, "got %s" % got)
        if not ok:
            bad.append((name, got))
    abort_if_failed("HASH GATE")
    # workspace copies used for import must match frozen
    check("workspace full_tree_partition.py",
          sha256_file(MOHPROG / "full_tree_partition.py") == EXPECTED_SHA["full_tree_partition.py"])
    check("workspace nested_pack.py",
          sha256_file(ORBITS / "nested_pack.py") == EXPECTED_SHA["nested_pack.py"])
    check("workspace moh_skeleton_full.py",
          sha256_file(REPO / "box" / "moh_skeleton_full.py") == EXPECTED_SHA["moh_skeleton_full.py"])
    abort_if_failed("WORKSPACE HASH")


def control_vtuple_state():
    print("\n-- CONTROL V-TUPLE: tree DP cache carries higher V --", flush=True)
    # s=4 ODE survivor from the charged excess list
    S = Skel(100, 40, [70, 95, 98], {2: 8, 3: 4, 4: 4})
    check("s=4 windows+full", S.windows_ok() and S.full_ok())
    E = FT.evaluator(S, ode_nondegenerate=True)
    ok, wit = E.embeds(S)
    check("s=4 ODE embeds", ok)
    keys = list(E._global_cache.keys()) + list(E._embed_cache.keys())
    # cache_key = (j, path[j+1:], ...) with path holding V_{j+1..s}
    higher = [k[1] for k in keys if isinstance(k, tuple) and len(k) >= 2]
    check("some cache key stores a V-tuple of length>=1",
          any(isinstance(t, tuple) and len(t) >= 1 for t in higher),
          str(higher[:8]))
    check("a key stores length>=2 (V_{s-1}, V_s) at s=4",
          any(isinstance(t, tuple) and len(t) >= 2 for t in higher),
          str(higher[:8]))
    # two different V_3 in the same (n,m,M,V_s) group must not collide
    clear_tree()


def control_moh_screens(TI):
    print("\n-- CONTROL M: Moh six survive every screen --", flush=True)
    expect_n16 = [
        ("(64,48)", {9}),
        ("(84,56) M2=64,V2=2", set()),
        ("(84,56) M2=72,V2=5", {10}),
        ("(75,50) V2=3", {9}),
        ("(75,50) V2=2", {8}),
        ("(99,66)", {16}),
    ]
    for ((n, m, Ms, Vs, lab, _, _, _), exp) in zip(MOH_TABLE, [e[1] for e in expect_n16]):
        S = Skel(n, m, Ms, Vs)
        check("windows+full %s" % lab, S.windows_ok() and S.full_ok())
        sc = screens_of(S, want_side=True)
        check("TREE %s" % lab, sc["tree"])
        check("ODE %s" % lab, sc["ode"])
        check("PASSPORT %s" % lab, sc["pass"])
        check("POLY %s" % lab, sc["poly"])
        check("POLY+ODE %s" % lab, sc["polyode"])
        C0 = TI.WholeTree(n, m, list(Ms), removable_prefix=False, passport=False)
        check("TI-zero TREE %s" % lab, C0.embeds(dict(Vs)) is not None)
        vals, cap, _ = NP.nested_values([S], max(int(Umax([S])), 16))
        Ns = NP.ints_in(vals, 6, 16)
        check("nested[6,16] %s" % lab, Ns == exp, "%s vs %s" % (sorted(Ns), sorted(exp)))
    clear_tree()


def control_n100_threeway(TI):
    print("\n-- CONTROL n<=100: 658 -> 60/58/55/23/20, TI row-for-row --", flush=True)
    t0 = time.time()
    rows = [Skel(n, m, list(Ms), V)
            for n in range(4, 101)
            for m, Ms, V in census(n, Kmin=2, full=True)]
    check("n<=100 Kmin=2 rows = 658", len(rows) == 658, str(len(rows)))
    check("n<=100 (n,m) classes = 63",
          len({(S.n, S.m) for S in rows}) == 63)
    pk = printed_keys()
    got = {row_key(S) for S in rows}
    check("printed keys subset of census", pk <= got)

    sets = {name: set() for name in
            ("tree", "ode", "pass", "poly", "polyode")}
    ti_tree, ti_pass, ti_poly = set(), set(), set()
    disagree = []
    for S in rows:
        k = row_key(S)
        sc = screens_of(S, want_side=True)
        for name in sets:
            if sc[name]:
                sets[name].add(k)
        Vs = {i: S.V[i] for i in range(2, S.s + 1)}
        Ms = [S.M[i] for i in range(2, S.s + 1)]
        C0 = TI.WholeTree(S.n, S.m, Ms, removable_prefix=False, passport=False)
        Cpass = TI.WholeTree(S.n, S.m, Ms, removable_prefix=False, passport=True)
        Cpoly = TI.WholeTree(S.n, S.m, Ms, removable_prefix=True, passport=False)
        t_ok = C0.embeds(Vs) is not None
        p_ok = Cpass.embeds(Vs) is not None
        y_ok = Cpoly.embeds(Vs) is not None
        if t_ok:
            ti_tree.add(k)
        if p_ok:
            ti_pass.add(k)
        if y_ok:
            ti_poly.add(k)
        if t_ok != sc["tree"]:
            disagree.append(("TREE", k))
        if p_ok != sc["pass"]:
            disagree.append(("PASS", k))
        if y_ok != sc["poly"]:
            disagree.append(("POLY", k))
    clear_tree()
    check("C_FULL_TREE rows = 60", len(sets["tree"]) == 60, str(len(sets["tree"])))
    check("C_FULL_TREE_ODE rows = 58", len(sets["ode"]) == 58, str(len(sets["ode"])))
    check("C_FULL_TREE_PASSPORT rows = 55", len(sets["pass"]) == 55, str(len(sets["pass"])))
    check("C_FULL_TREE_POLY rows = 23", len(sets["poly"]) == 23, str(len(sets["poly"])))
    check("C_FULL_TREE_POLY+ODE rows = 20", len(sets["polyode"]) == 20, str(len(sets["polyode"])))
    check("Moh six in TREE", pk <= sets["tree"])
    check("Moh six in ODE", pk <= sets["ode"])
    check("Moh six in PASSPORT", pk <= sets["pass"])
    check("Moh six in POLY", pk <= sets["poly"])
    check("Moh six in POLY+ODE", pk <= sets["polyode"])
    check("FT TREE == TI --zero-only row-for-row",
          sets["tree"] == ti_tree, "disagree %d" % sum(1 for a, _ in disagree if a == "TREE"))
    check("FT PASSPORT == TI --zero-only --passport",
          sets["pass"] == ti_pass)
    check("FT POLY == TI default recenter",
          sets["poly"] == ti_poly)
    check("no FT/TI disagreements", disagree == [], str(disagree[:5]))
    # (75,50) residue
    r7550 = [S for S in rows if (S.n, S.m) == (75, 50) and row_key(S) in sets["ode"]]
    m2v2 = sorted({(S.M[2], S.V[2]) for S in r7550})
    check("(75,50) ODE residue {(55,2),(55,3)}",
          m2v2 == [(55, 2), (55, 3)], str(m2v2))
    print("   n<=100 wall %.2fs" % (time.time() - t0), flush=True)
    return rows, sets


def collect_degree(n, Kmin=16):
    G = {}
    for (m, Ms, V) in census(n, Kmin=Kmin, full=True):
        S = Skel(n, m, list(Ms), V)
        G.setdefault(group_key(S), []).append(S)
    return G


def vrec(S):
    return {str(i): int(S.V[i]) for i in range(2, S.s + 1)}


def describe_assignment(S, Nhi=None):
    if Nhi is None:
        Nhi = max(int(Umax([S])), 16)
    j2 = j2_pack(S)
    d63 = prop63_datum(S)
    _ok, b12, b13 = S.cond1213()
    return {
        "n": S.n, "m": S.m, "s": S.s,
        "M": [S.M[i] for i in range(2, S.s + 1)],
        "V": vrec(S),
        "K": int(S.K), "e": int(S.e), "d": int(S.dd),
        "d_list": [S.d[i] for i in range(1, S.s + 2)],
        "u": str(S.u), "q": str(S.q()),
        "orbit_sizes": sorted(orbit_sizes(S)),
        "packets": packet_list(S, Nhi),
        "cond1011": cond_bits(S),
        "cond12": bool(b12), "cond13": bool(b13),
        "j2": j2,
        "prop63": d63,
        "delta": {str(i): str(S.delta[i]) for i in range(1, S.s + 1)},
    }


def empty_degree_rec():
    return {
        "n": 0, "V": 0, "grp": 0, "s3": 0, "sgt": 0,
        "un_n6": 0, "un_n16": 0, "un_cap": 0,
        "tree_V": 0, "tree_g": 0, "tree_n6": 0, "tree_n16": 0,
        "ode_V": 0, "ode_g": 0, "ode_n6": 0, "ode_n16": 0,
        "pass_V": 0, "pass_g": 0, "pass_n6": 0, "pass_n16": 0,
        "poly_V": 0, "poly_g": 0, "poly_n6": 0, "poly_n16": 0,
        "polyode_V": 0, "polyode_g": 0, "polyode_n6": 0, "polyode_n16": 0,
        "side": False, "wall": 0.0, "max_states": 0, "cap": 0,
        "by_s": {}, "by_Ke": {},
    }


def run_census(dlo, dhi, t_budget, listing=LISTING):
    print("\n== SCREENED CENSUS %d <= D <= %d (budget %.0fs) ==" %
          (dlo, dhi, t_budget), flush=True)
    hdr = ("   %5s %5s %5s %6s %6s %6s %6s %6s %6s %6s %6s %6s %5s" %
           ("D", "grp", "V", "treeG", "odeG", "tN6", "oN6", "oN16",
            "passG", "unN6", "unN16", "empty?", "wall"))
    print(hdr, flush=True)
    t_all = time.time()
    per = {}
    tot = empty_degree_rec()
    listings = {n: [] for n in listing}
    s3_ode_n6 = []  # compact family-search rows
    first_above_100 = None
    stopped_at = None
    max_states = 0
    cap_hits = 0
    baseline_active = []
    tree_empty, ode_empty = [], []
    tree_n6_empty, ode_n6_empty = [], []
    tree_n16_empty, ode_n16_empty = [], []
    un_n6_empty, un_n16_empty = [], []
    want_unscreened_nested_hi = 120

    for n in range(dlo, dhi + 1):
        elapsed = time.time() - t_all
        if elapsed > t_budget:
            stopped_at = n - 1
            print("   TIME BUDGET at D=%d (elapsed %.1fs) -- stop" %
                  (n, elapsed), flush=True)
            break
        t0 = time.time()
        G = collect_degree(n)
        if not G:
            continue
        baseline_active.append(n)
        want_side = (n <= SIDE_DHI)
        want_un_nested = n <= want_unscreened_nested_hi
        rec = empty_degree_rec()
        rec["n"] = n
        rec["grp"] = len(G)
        rec["side"] = want_side
        by_s = defaultdict(lambda: dict(g=0, tree=0, ode=0, ode_n6=0))
        by_Ke = defaultdict(lambda: dict(g=0, tree=0, ode=0, ode_n6=0))

        listing_rows = []
        for key, skels in G.items():
            rec["V"] += len(skels)
            s = skels[0].s
            K, e = int(skels[0].K), int(skels[0].e)
            rec["s3" if s == 3 else "sgt"] += 1
            by_s[s]["g"] += 1
            by_Ke[(K, e, s)]["g"] += 1

            un = nested_of(skels) if want_un_nested else None
            if un:
                rec["un_n6"] += int(un["nest6"])
                rec["un_n16"] += int(un["nest16"])
                rec["un_cap"] += int(un["cap"])
                max_states = max(max_states, un["nstates"])
                cap_hits += int(un["cap"])

            tree_sk, ode_sk = [], []
            pass_sk, poly_sk, polyode_sk = [], [], []
            sc_map = {}
            for S in skels:
                sc = screens_of(S, want_side)
                sc_map[id(S)] = sc
                if sc["tree"]:
                    tree_sk.append(S)
                if sc["ode"]:
                    ode_sk.append(S)
                if sc["pass"]:
                    pass_sk.append(S)
                if sc["poly"]:
                    poly_sk.append(S)
                if sc["polyode"]:
                    polyode_sk.append(S)

            rec["tree_V"] += len(tree_sk)
            rec["ode_V"] += len(ode_sk)
            rec["pass_V"] += len(pass_sk)
            rec["poly_V"] += len(poly_sk)
            rec["polyode_V"] += len(polyode_sk)
            rec["tree_g"] += int(bool(tree_sk))
            rec["ode_g"] += int(bool(ode_sk))
            rec["pass_g"] += int(bool(pass_sk))
            rec["poly_g"] += int(bool(poly_sk))
            rec["polyode_g"] += int(bool(polyode_sk))
            by_s[s]["tree"] += int(bool(tree_sk))
            by_s[s]["ode"] += int(bool(ode_sk))
            by_Ke[(K, e, s)]["tree"] += int(bool(tree_sk))
            by_Ke[(K, e, s)]["ode"] += int(bool(ode_sk))

            tn = nested_of(tree_sk) if tree_sk else None
            on = nested_of(ode_sk) if ode_sk else None
            pn = nested_of(pass_sk) if pass_sk and want_side else None
            yn = nested_of(poly_sk) if poly_sk and want_side else None
            y2 = nested_of(polyode_sk) if polyode_sk and want_side else None
            for pack, prefix in ((tn, "tree"), (on, "ode"), (pn, "pass"),
                                 (yn, "poly"), (y2, "polyode")):
                if not pack:
                    continue
                rec["%s_n6" % prefix] += int(pack["nest6"])
                rec["%s_n16" % prefix] += int(pack["nest16"])
                rec["cap"] += int(pack["cap"])
                max_states = max(max_states, pack["nstates"])
                cap_hits += int(pack["cap"])
            if on and on["nest6"]:
                by_s[s]["ode_n6"] += 1
                by_Ke[(K, e, s)]["ode_n6"] += 1

            if on and on["nest6"] and ode_sk and ode_sk[0].s == 3:
                S0 = ode_sk[0]
                j2 = j2_pack(S0)
                s3_ode_n6.append({
                    "n": n, "m": S0.m, "M": [S0.M[i] for i in range(2, S0.s + 1)],
                    "Vs": int(S0.V[S0.s]),
                    "V2": sorted({int(S.V[2]) for S in ode_sk}),
                    "K": int(S0.K), "e": int(S0.e), "d": int(S0.dd),
                    "d3": int(S0.d[3]), "ds": int(S0.d[S0.s]),
                    "A2": j2["A2"], "P": j2["P"], "bmin": j2["bmin"],
                    "h": j2["h"], "P_div_A2": j2["P_div_A2"],
                    "bmin_le_h": j2["bmin_le_h"],
                    "forced_major_zero": j2["forced_major_zero"],
                    "Ns6": on["Ns6"], "Ns16": on["Ns16"],
                    "u_s": u_s_of(S0), "q": str(S0.q()), "u": str(S0.u),
                    "by10": bool(S0.cond1011(2)[1]),
                    "by11": bool(S0.cond1011(2)[2]),
                })

            if n in listing and on and on["nest16"]:
                Nhi = max(int(Umax(ode_sk)), 16)
                listing_rows.append({
                    "key": [key[0], list(key[1]), key[2]],
                    "s": s,
                    "nested": on,
                    "assignments": [describe_assignment(S, Nhi) for S in ode_sk],
                })

            if first_above_100 is None and n > 100 and on and on["nest6"]:
                Nhi = max(int(Umax(ode_sk)), 16)
                first_above_100 = {
                    "D": n,
                    "key": [key[0], list(key[1]), key[2]],
                    "nested": on,
                    "assignments": [describe_assignment(S, Nhi) for S in ode_sk],
                }

        rec["wall"] = time.time() - t0
        rec["max_states"] = max_states
        rec["by_s"] = {str(k): v for k, v in sorted(by_s.items())}
        rec["by_Ke"] = {"%d,%d,%d" % k: v for k, v in sorted(by_Ke.items())}
        per[n] = rec
        if n in listing:
            listings[n] = listing_rows

        for attr in ("V", "grp", "s3", "sgt", "un_n6", "un_n16", "un_cap",
                     "tree_V", "tree_g", "tree_n6", "tree_n16",
                     "ode_V", "ode_g", "ode_n6", "ode_n16",
                     "pass_V", "pass_g", "pass_n6", "pass_n16",
                     "poly_V", "poly_g", "poly_n6", "poly_n16",
                     "polyode_V", "polyode_g", "polyode_n6", "polyode_n16",
                     "cap"):
            tot[attr] = tot.get(attr, 0) + rec[attr]

        if rec["tree_g"] == 0:
            tree_empty.append(n)
        if rec["ode_g"] == 0:
            ode_empty.append(n)
        if rec["tree_n6"] == 0:
            tree_n6_empty.append(n)
        if rec["ode_n6"] == 0:
            ode_n6_empty.append(n)
        if rec["tree_n16"] == 0:
            tree_n16_empty.append(n)
        if rec["ode_n16"] == 0:
            ode_n16_empty.append(n)
        if want_un_nested and rec["un_n6"] == 0:
            un_n6_empty.append(n)
        if want_un_nested and rec["un_n16"] == 0:
            un_n16_empty.append(n)

        flag = ""
        if rec["ode_n6"] == 0:
            flag = " EMPTY-ODE-N6"
        elif rec["ode_n16"] == 0:
            flag = " EMPTY-ODE[6,16]"
        print("   %5d %5d %5d %6d %6d %6d %6d %6d %6d %6d %6d %6s %4.1fs%s" %
              (n, rec["grp"], rec["V"], rec["tree_g"], rec["ode_g"],
               rec["tree_n6"], rec["ode_n6"], rec["ode_n16"], rec["pass_g"],
               rec["un_n6"], rec["un_n16"],
               "Y" if rec["ode_n6"] == 0 else "",
               rec["wall"], flag), flush=True)
        clear_tree()

        if n == 120:
            check("D<=120 unscreened groups = 1189", tot["grp"] == 1189, str(tot["grp"]))
            check("D<=120 unscreened nested N>=6 = 587", tot["un_n6"] == 587, str(tot["un_n6"]))
            check("D<=120 unscreened nested [6,16] = 470", tot["un_n16"] == 470, str(tot["un_n16"]))
            check("D<=120 TREE V = 183", tot["tree_V"] == 183, str(tot["tree_V"]))
            check("D<=120 TREE groups = 113", tot["tree_g"] == 113, str(tot["tree_g"]))
            check("D<=120 ODE V = 168", tot["ode_V"] == 168, str(tot["ode_V"]))
            check("D<=120 ODE groups = 103", tot["ode_g"] == 103, str(tot["ode_g"]))
            abort_if_failed("CHECKPOINT D<=120")
        if n == 200:
            check("D<=200 unscreened groups = 14016", tot["grp"] == 14016, str(tot["grp"]))
            abort_if_failed("CHECKPOINT D<=200")

    if stopped_at is None:
        stopped_at = dhi
    tot["wall"] = time.time() - t_all
    tot["max_states"] = max_states
    tot["cap"] = cap_hits
    print("   ---- totals through D=%d  wall %.1fs ----" % (stopped_at, tot["wall"]),
          flush=True)
    print("   unscreened groups %d  nested N>=6 %d  [6,16] %d  (nested only D<=%d)" %
          (tot["grp"], tot["un_n6"], tot["un_n16"], want_unscreened_nested_hi),
          flush=True)
    print("   TREE V/g/N6/N16 %d/%d/%d/%d" %
          (tot["tree_V"], tot["tree_g"], tot["tree_n6"], tot["tree_n16"]), flush=True)
    print("   ODE  V/g/N6/N16 %d/%d/%d/%d" %
          (tot["ode_V"], tot["ode_g"], tot["ode_n6"], tot["ode_n16"]), flush=True)
    return {
        "per": per, "tot": tot, "listings": listings,
        "s3_ode_n6": s3_ode_n6, "first_above_100": first_above_100,
        "stopped_at": stopped_at, "baseline_active": baseline_active,
        "tree_empty": tree_empty, "ode_empty": ode_empty,
        "tree_n6_empty": tree_n6_empty, "ode_n6_empty": ode_n6_empty,
        "tree_n16_empty": tree_n16_empty, "ode_n16_empty": ode_n16_empty,
        "un_n6_empty": un_n6_empty, "un_n16_empty": un_n16_empty,
        "max_states": max_states, "cap_hits": cap_hits,
        "wall": tot["wall"],
    }


def residue_n100(rows, ode_keys):
    pk = printed_keys()
    excess = []
    us1 = 0
    for S in rows:
        k = row_key(S)
        if k not in ode_keys or k in pk:
            continue
        d = describe_assignment(S)
        excess.append(d)
        if d["prop63"]["u_s"] == 1:
            us1 += 1
    excess.sort(key=lambda r: (r["n"], r["m"], r["M"], tuple(r["V"].items())))
    return excess, us1


def family_search(s3_rows, dhi):
    """Search s=3 ODE+N>=6 survivors for a closed-form cofinal family."""
    print("\n== FAMILY SEARCH on s=3 ODE + nested N>=6 (D<=%d) ==" % dhi, flush=True)
    out = {
        "n_rows": len(s3_rows),
        "P_div_A2": 0, "bmin_le_h_not_div": 0, "forced_major_zero": 0,
        "by_ed": {}, "APs": [], "symbolic": [],
        "sol_ray_status": [], "a2six_ray_status": [],
        "cofinal_family": None,
        "search_bound": dhi,
    }
    by_ed = defaultdict(list)
    n_div = n_le = n_force = 0
    for r in s3_rows:
        by_ed[(r["e"], r["d"])].append(r)
        if r["P_div_A2"]:
            n_div += 1
        elif r["bmin_le_h"]:
            n_le += 1
        if r["forced_major_zero"]:
            n_force += 1
    out["P_div_A2"] = n_div
    out["bmin_le_h_not_div"] = n_le
    out["forced_major_zero"] = n_force
    out["by_ed"] = {("%d,%d" % k): len(v) for k, v in sorted(by_ed.items())}
    print("   s=3 ODE+N>=6 rows: %d; P|A2 (P%%A2==0): %d; bmin<=h not div: %d; forced major zero (should be 0): %d" %
          (len(s3_rows), n_div, n_le, n_force), flush=True)

    # arithmetic progressions in n for fixed (e,d, V3, A2) or (e,d, u_s, V3)
    buckets = defaultdict(list)
    for r in s3_rows:
        buckets[(r["e"], r["d"], r["Vs"], r["A2"], r["u_s"])].append(r)
    aps = []
    for key, items in buckets.items():
        ns = sorted({it["n"] for it in items})
        if len(ns) < 3:
            continue
        # try common difference
        diffs = [ns[i + 1] - ns[i] for i in range(len(ns) - 1)]
        if len(set(diffs)) == 1 and diffs[0] > 0:
            aps.append({
                "key_e_d_Vs_A2_us": list(key),
                "n": ns, "diff": diffs[0], "count": len(ns),
                "sample": items[0],
            })
    # also A2-constant (e,d,Vs) allowing A2 to vary linearly
    buckets2 = defaultdict(list)
    for r in s3_rows:
        buckets2[(r["e"], r["d"], r["Vs"], r["u_s"])].append(r)
    for key, items in buckets2.items():
        ns = sorted({it["n"] for it in items})
        if len(ns) < 3:
            continue
        items_sorted = sorted(items, key=lambda z: z["n"])
        # unique by n
        uniq = {}
        for it in items_sorted:
            uniq.setdefault(it["n"], it)
        ns = sorted(uniq)
        if len(ns) < 3:
            continue
        diffs = [ns[i + 1] - ns[i] for i in range(len(ns) - 1)]
        if len(set(diffs)) == 1 and diffs[0] > 0:
            aps.append({
                "key_e_d_Vs_us": list(key),
                "n": ns, "diff": diffs[0], "count": len(ns),
                "A2": [uniq[n]["A2"] for n in ns],
                "P": [uniq[n]["P"] for n in ns],
                "M2": [uniq[n]["M"][0] for n in ns],
                "sample": uniq[ns[0]],
            })
    out["APs"] = aps
    print("   arithmetic-progression clusters (>=3 degrees): %d" % len(aps), flush=True)
    for ap in aps[:20]:
        print("      %s n=%s diff=%s" %
              (ap.get("key_e_d_Vs_A2_us") or ap.get("key_e_d_Vs_us"),
               ap["n"], ap["diff"]), flush=True)

    # named dead rays: confirm still dead at every measured member in range
    sol_status = []
    for a in range(0, 40):
        L = 8 * a + 5
        n = 21 * L
        if n < 48 or n > dhi + 200:
            if n > dhi + 200:
                break
            continue
        m = 14 * L
        M2 = 7 * (3 * L + 1) // 4
        try:
            S = Skel(n, m, [M2, n - 2], {2: 1, 3: 5})
        except Exception as ex:
            sol_status.append({"a": a, "n": n, "error": str(ex)})
            continue
        ok_arith = S.windows_ok() and S.full_ok()
        tree = bool(FT.full_tree_ok(S)) if ok_arith else False
        j2 = j2_pack(S) if ok_arith else None
        sol_status.append({
            "a": a, "L": L, "n": n, "arith": ok_arith, "TREE": tree,
            "j2": j2, "in_census_bound": n <= dhi,
        })
        clear_tree()
    out["sol_ray_status"] = sol_status
    a2_status = []
    for t in range(0, 50):
        P = 7 * t + 6
        n = 9 * P
        if n < 48 or n > dhi + 200:
            if n > dhi + 200:
                break
            continue
        m = 6 * P
        M2 = 4 * P
        V3 = 6 * t + 5
        try:
            S = Skel(n, m, [M2, n - 2], {2: 1, 3: V3})
        except Exception as ex:
            a2_status.append({"t": t, "n": n, "error": str(ex)})
            continue
        ok_arith = S.windows_ok() and S.full_ok()
        tree = bool(FT.full_tree_ok(S)) if ok_arith else False
        j2 = j2_pack(S) if ok_arith else None
        a2_status.append({
            "t": t, "P": P, "n": n, "arith": ok_arith, "TREE": tree,
            "j2": j2, "in_census_bound": n <= dhi,
        })
        clear_tree()
    out["a2six_ray_status"] = a2_status
    check("Sol L=8a+5 TREE-dead on every constructed member",
          all(not r.get("TREE") for r in sol_status if "TREE" in r))
    check("A2=6 geometric ray TREE-dead on every constructed member",
          all(not r.get("TREE") for r in a2_status if "TREE" in r))

    # try to prove a candidate AP in a parameter, if any looks linear in M2,A2,P
    try:
        import sympy as sp
        have_sp = True
    except Exception:
        have_sp = False
        print("   sympy not available; AP algebra skipped", flush=True)

    symbolic = []
    if have_sp and aps:
        for ap in aps:
            sample = ap["sample"]
            ns = ap["n"]
            diff = ap["diff"]
            # n = n0 + diff*k, k=0,1,...
            k = sp.symbols("k", integer=True, nonnegative=True)
            n_expr = ns[0] + diff * k
            # fit M2, P, A2 as linear in k from the table
            def fit_lin(vals):
                if len(vals) < 2:
                    return None
                d1 = vals[1] - vals[0]
                if all(vals[i] == vals[0] + d1 * i for i in range(len(vals))):
                    return vals[0] + d1 * k
                return None
            M2s = ap.get("M2") or [sample["M"][0]]
            Ps = ap.get("P") or [sample["P"]]
            A2s = ap.get("A2") or [sample["A2"]]
            rec = {
                "n": str(n_expr), "diff": diff, "degrees": ns,
                "e": sample["e"], "d": sample["d"], "Vs": sample["Vs"],
                "u_s": sample["u_s"],
                "M2_fit": str(fit_lin(M2s)) if "M2" in ap else None,
                "P_fit": str(fit_lin(Ps)) if "P" in ap else None,
                "A2_fit": str(fit_lin(A2s)) if "A2" in ap else None,
            }
            # verify next two terms beyond measured, if they lie in PATH-ARITH
            extra_ok = []
            for kk in range(len(ns), len(ns) + 3):
                n_try = ns[0] + diff * kk
                # reconstruct M2 if linear
                if "M2" in ap and fit_lin(M2s) is not None:
                    M2_try = int(M2s[0] + (M2s[1] - M2s[0]) * kk)
                    m_try = sample["d"] * (n_try // sample["e"]) if n_try % sample["e"] == 0 else None
                    if m_try is None:
                        extra_ok.append({"k": kk, "n": n_try, "skip": "e not dividing n"})
                        continue
                    try:
                        S = Skel(n_try, m_try, [M2_try, n_try - 2],
                                 {2: sample["V2"][0], 3: sample["Vs"]})
                        arith = S.windows_ok() and S.full_ok()
                        tree = bool(FT.full_tree_ok(S)) if arith else False
                        ode = bool(FT.full_tree_ode_ok(S)) if tree else False
                        nest = nested_of([S]) if ode else None
                        extra_ok.append({
                            "k": kk, "n": n_try, "m": m_try, "M2": M2_try,
                            "arith": arith, "TREE": tree, "ODE": ode,
                            "nest6": None if not nest else nest["nest6"],
                            "Ns6": None if not nest else nest["Ns6"],
                        })
                        clear_tree()
                    except Exception as ex:
                        extra_ok.append({"k": kk, "n": n_try, "error": str(ex)})
            rec["extrapolation"] = extra_ok
            # a family is cofinal only if every extrapolated member survives
            if extra_ok and all(x.get("ODE") and x.get("nest6") for x in extra_ok
                                if "ODE" in x):
                rec["extrapolation_survives"] = True
            else:
                rec["extrapolation_survives"] = False
            symbolic.append(rec)
            print("   AP n=%s + %d k; extra %s" %
                  (ns[0], diff, extra_ok), flush=True)

    out["symbolic"] = symbolic
    # cofinal family: an AP whose every measured member AND every
    # extrapolation survives, with an identity P ≡ 0 (mod A2) or bmin<=h
    cofinal = None
    for rec, ap in zip(symbolic, aps):
        if rec.get("extrapolation_survives") and rec.get("degrees") and len(rec["degrees"]) >= 3:
            cofinal = rec
            break
    out["cofinal_family"] = cofinal
    if cofinal:
        print("   COFINAL CANDIDATE: %s" % cofinal, flush=True)
    else:
        print("   no closed-form screened cofinal family isolated up to D<=%d" % dhi,
              flush=True)
    return out


def analyse_measured_families(s3_rows):
    """Cluster measured s=3 ODE+N>=6 rows: (e,d), P%A2==0, linear n."""
    print("\n== MEASURED FAMILY CLUSTERS (s=3 ODE + nested N>=6) --", flush=True)
    by_ed = defaultdict(list)
    pdiv = []
    for r in s3_rows:
        by_ed[(r["e"], r["d"])].append(r)
        if r["P_div_A2"]:
            pdiv.append(r)
    print("   (e,d) histogram of s=3 ODE+N>=6:", flush=True)
    for (e, d), items in sorted(by_ed.items(), key=lambda kv: -len(kv[1])):
        ns = sorted({it["n"] for it in items})
        print("      (e,d)=(%d,%d) rows=%d degrees=%s" %
              (e, d, len(items), ns[:24] if len(ns) <= 24 else ns[:12] + ["..."]),
              flush=True)
    print("   P ≡ 0 (mod A2) rows: %d  degrees %s" %
          (len(pdiv), sorted({r["n"] for r in pdiv})), flush=True)
    # cluster P|A2 by (e,d,Vs,us)
    by = defaultdict(list)
    for r in pdiv:
        by[(r["e"], r["d"], r["Vs"], r["u_s"], tuple(r["V2"]))].append(r)
    clusters = []
    for key, items in by.items():
        ns = sorted({it["n"] for it in items})
        diffs = ([ns[i + 1] - ns[i] for i in range(len(ns) - 1)] if len(ns) > 1 else [])
        clusters.append({
            "e_d_Vs_us_V2": [key[0], key[1], key[2], key[3], list(key[4])],
            "n": ns,
            "common_diff": diffs[0] if diffs and len(set(diffs)) == 1 else None,
            "count": len(ns),
            "A2": [it["A2"] for it in sorted(items, key=lambda z: z["n"])],
            "P": [it["P"] for it in sorted(items, key=lambda z: z["n"])],
            "M2": [it["M"][0] for it in sorted(items, key=lambda z: z["n"])],
            "Ns6": [it["Ns6"] for it in sorted(items, key=lambda z: z["n"])],
        })
    clusters.sort(key=lambda c: -c["count"])
    print("   P|A2 clusters: %d" % len(clusters), flush=True)
    for c in clusters[:20]:
        print("      %s" % c, flush=True)
    return {"n_pdiv": len(pdiv), "clusters": clusters,
            "pdiv_head": pdiv[:60],
            "ed_hist": {("%d,%d" % k): len(v) for k, v in by_ed.items()}}


def main():
    t_start = time.time()
    print("screened-census -- C_FULL_TREE_ODE x nested-pack", flush=True)
    print("frozen %s" % FROZEN, flush=True)
    print("=" * 78, flush=True)
    hash_gate()
    TI = load_tree_independent()
    control_vtuple_state()
    control_moh_screens(TI)
    abort_if_failed("PRE-CENSUS CONTROLS")
    rows100, sets100 = control_n100_threeway(TI)
    abort_if_failed("n<=100 CONTROLS")
    excess, us1 = residue_n100(rows100, sets100["ode"])
    check("ODE excess rows = 52", len(excess) == 52, str(len(excess)))
    print("   of the 52, u_s=1 (Prop 6.3/6.4 automatic): %d" % us1, flush=True)

    remaining = TIME_BUDGET_S - (time.time() - t_start)
    remaining = max(remaining, 60.0)
    census_out = run_census(DLO, DHI_TARGET, remaining)
    abort_if_failed("CENSUS CONTROLS")

    fam = family_search(census_out["s3_ode_n6"], census_out["stopped_at"])
    constr = analyse_measured_families(census_out["s3_ode_n6"])

    payload = {
        "lane": "screened-census-grok46-20260903",
        "frozen_sha256": EXPECTED_SHA,
        "scope": {
            "small": "4<=n<=100,Kmin=2",
            "degree": "48<=D<=%d,Kmin=16" % census_out["stopped_at"],
            "target_Dhi": DHI_TARGET,
            "stopped_at": census_out["stopped_at"],
            "nested_unscreened_through": 120,
            "side_columns_through": SIDE_DHI,
            "operative": "C_FULL_TREE_ODE + nested N>=6 and [6,16]",
            "side": "C_FULL_TREE_PASSPORT (EXTERNAL); +RECENTER / POLY+ODE (OPEN)",
        },
        "n100": {
            "rows": 658,
            "tree": 60, "ode": 58, "pass": 55, "poly": 23, "polyode": 20,
            "excess_ode": 52, "excess_ode_us1": us1,
            "excess": excess,
        },
        "census": {
            "per_degree": {str(k): {kk: vv for kk, vv in v.items()
                                    if kk not in ("by_Ke",)}
                           for k, v in census_out["per"].items()},
            "per_degree_Ke": {str(k): v.get("by_Ke", {})
                              for k, v in census_out["per"].items()},
            "totals": {k: v for k, v in census_out["tot"].items()
                       if k not in ("by_s", "by_Ke", "n")},
            "baseline_active": census_out["baseline_active"],
            "tree_empty": census_out["tree_empty"],
            "ode_empty": census_out["ode_empty"],
            "tree_n6_empty": census_out["tree_n6_empty"],
            "ode_n6_empty": census_out["ode_n6_empty"],
            "tree_n16_empty": census_out["tree_n16_empty"],
            "ode_n16_empty": census_out["ode_n16_empty"],
            "un_n6_empty": census_out["un_n6_empty"],
            "un_n16_empty": census_out["un_n16_empty"],
            "listings": {str(k): v for k, v in census_out["listings"].items()},
            "first_above_100": census_out["first_above_100"],
            "s3_ode_n6": census_out["s3_ode_n6"],
            "max_states": census_out["max_states"],
            "cap_hits": census_out["cap_hits"],
            "wall": census_out["wall"],
        },
        "family": fam,
        "constructive_23": constr,
        "elapsed_seconds": time.time() - t_start,
        "NCHECK": NCHECK[0],
        "FAILURES": FAILURES,
    }
    out_json = HERE / "screened_census.json"
    out_json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print("\nWrote %s (%.1f KB)" % (out_json, out_json.stat().st_size / 1024),
          flush=True)
    print("ALL CONTROLS PASSED. NCHECK=%d  wall %.1fs  D<=%d" %
          (NCHECK[0], time.time() - t_start, census_out["stopped_at"]),
          flush=True)
    if FAILURES:
        sys.exit(1)


if __name__ == "__main__":
    main()
