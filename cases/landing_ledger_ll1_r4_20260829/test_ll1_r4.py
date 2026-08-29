#!/usr/bin/env python3
"""LL1-R4 acceptance tests: R3 regression suite plus typed-carrier reprice.

R3 deltas against the R2 suite: the A1 tautology
`all(2*nu+2 == 2*nu+2 ...)` is replaced by the honest frozen-fixture
engine-parity gate (pins verified, count-free parse, derived-vs-parsed
comparisons), and the new A6 battery proves the provenance layer fails
CLOSED under source drift (byte tamper, charged-count tamper, deleted
sentence, tampered book pins/record).  Everything else is the reviewed R2
suite unchanged.

Every check uses the explicit `chk` helper (never `assert`), so the suite is
byte-identical under `python -O`.  Exit 0 iff every test passes; the final
line prints the exact test count for the packet report.

Run:  python3 test_ll1_r4.py     and     python3 -O test_ll1_r4.py
"""

from fractions import Fraction
import copy
import hashlib
import json
import math
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ll1_compiler as C
import ll1_validator as V

PASSED = 0
FAILED = []


def chk(cond, name):
    global PASSED
    if cond:
        PASSED += 1
    else:
        FAILED.append(name)
        print("FAIL: %s" % name)


def frac(a, b=1):
    return Fraction(a, b)


# --------------------------------------------------------------------------
# Build the book once (fresh, in-memory) plus the emitted files.
# --------------------------------------------------------------------------
BOOK = C.compile_book()
SUMMARY = C.derive_summary(BOOK)
BOOK_JSON = C.canonical_json(BOOK)


def fresh_book():
    return json.loads(BOOK_JSON)


# ==========================================================================
# A1 -- record parity (corrected: family-I split replaces 5.4 + machine row)
# ==========================================================================

def test_a1():
    entries, offaxis = C.entry_menu(6, 2)
    chk(len(entries) == 1, "A1: unique on-axis entry at td=6,m=2")
    chk(entries and entries[0]["Lambda"] == (3, 3)
        and entries[0]["type"] == (2, 3)
        and entries[0]["poles"] == ((1, 1, 2), (1, 1, 2)),
        "A1: entry pin (a,b,nu)=(1,1,2) both poles, type (2,3)")
    chk(offaxis == [], "A1: off-axis sector empty at td=6 (MP4 prime Lambda)")
    fr = C.entry_frame(entries[0])[0]
    chk((fr["kbar"], fr["M"], fr["rho"], fr["w0"]) ==
        (frac(5), 1, frac(1), frac(2)),
        "A1: entry frame kbar=5, (M,rho,w0)=(1,1,2)")
    chk(fr["w_cert"] == C.W_CLOSED_FORM, "A1: entry w_cert W-CLOSED-FORM")

    chk(C.w_closure(frac(2)) == [frac(2)], "A1: W(2)={2} (no resonant step)")
    # DEPTH check-3 parity samples: W(4)={2,4}, W(6)={2,4,6}
    chk(set(C.w_closure(frac(4))) == {frac(2), frac(4)},
        "A1: DS3 parity W(4)={4,2}")
    chk(set(C.w_closure(frac(6))) == {frac(2), frac(4), frac(6)},
        "A1: DS3 parity W(6)={6,4,2}")
    # ---- honest frozen-fixture engine-parity gate (replaces the R2
    # tautology `all(2*nu+2 == 2*nu+2 ...)`) ----------------------------
    sources = C.load_sources()
    pins = C.verify_source_pins(sources)
    chk(pins == C.SOURCE_PINS
        and pins == BOOK["provenance"]["source_pins"],
        "A1: all seven source pins verify on the current bytes and match "
        "the compiled book")
    texts = {p: b.decode("utf-8") for p, b in sources.items()}
    rec = C.parse_engine_fixture(texts)
    chk(C.canonical_json(rec) ==
        C.canonical_json(BOOK["provenance"]["engine_record"]),
        "A1: count-free re-parse of the fixture bytes equals the compiled "
        "engine record")
    # regression pin of the charged figures (values come from the PARSE,
    # never from the parser: the regexes contain no expected count)
    chk(rec["shapes"] == 26 and rec["mu1_shapes"] == 24
        and rec["nu1_zch_shapes"] == 2 and rec["parent_pairs"] == 351
        and rec["pair_invariance"] == [351, 351]
        and rec["merge_ledger"] == [18427, 17199, 601, 276]
        and rec["zch_suffix_dead"] == 276 and rec["nu1_ode_dead"] == 601,
        "A1: parsed charged figures = 26 shapes (24 mu1 + 2 nu1-zch) / "
        "351 parent pairs / ledger 18427/17199/601/276")
    chk(rec["residue_child"] == {"rho": "1/2", "nu": 3, "M": 2, "kbar": 5},
        "A1: parsed frozen residue child is (1/2,3,2,5) in shape space")
    parity = C.engine_parity_checks(rec)
    chk(len(parity) == 6 and all(r["status"] == "OK" for r in parity)
        and C.canonical_json(parity) ==
        C.canonical_json(BOOK["provenance"]["engine_parity"]),
        "A1: derived-vs-parsed engine parity checks all OK and recorded")
    # the DS4 identity on parsed inputs reproduces the derived child
    pi = rec["prediction_identity"]
    iia = C.iia_cell(3, 1, frac(2))
    chk(frac(pi["w"] * pi["dq"], pi["Delta"]) == iia["kbar"] == frac(5)
        and frac(pi["w"] * pi["dp"], pi["Delta"]) == iia["X"] == frac(3)
        and frac(pi["w"], pi["Delta"]) == iia["X"] / iia["dp"] == frac(1, 2)
        and (pi["dp"], pi["dq"]) == (iia["dp"], iia["dq"]),
        "A1: DS4 identity w*(dq,dp,1)/Delta on parsed inputs = (5,3,1/2) "
        "= the derived admitted child")
    chk("NOT re-run" in rec["scope"]
        and "FIXTURE-CITED"
        in BOOK["trust_snapshot"]["ENGINE-REC"]["source"],
        "A1: 26/351 counts stay fixture-cited (engine not re-run; no "
        "manufactured parity)")
    chk(BOOK["provenance"]["rederivation"]["decision_changes"] == [],
        "A1: consumed-clause rederivation against the pinned current "
        "bytes changes no decision")

    mrecs = {r["record_id"]: r for r in BOOK["sections"]["merge"]}
    chk(mrecs["MERGE/ROOT/parametric-l>=1"]["verdict"] == "DEAD",
        "A1: root meet DEAD (case-I window on certified w=2)")
    chk(mrecs["MERGE/ZCH/0-edge=P1"]["verdict"] == "REJECTED"
        and mrecs["MERGE/ZCH/0-edge=P2"]["verdict"] == "REJECTED",
        "A1: ZCH unreachable (case-III ratio)")
    adm = [r for r in BOOK["sections"]["merge"] if r["verdict"] == "ADMITTED"]
    chk(len(adm) == 1 and adm[0]["record_id"] == "MERGE/IIA/admitted-(2,3,1)",
        "A1: admitted interior menu exactly {IIa(2,3,1)}")
    chk(tuple(adm[0]["child"]["Q"]) == (6, 12, 3, 2, 5)
        and Fraction(adm[0]["child"]["w_trunk"]) == frac(3, 2),
        "A1: admitted child Q=(6,12,3,2,5), w_trunk=3/2")
    cell = adm[0]["cell"]
    chk(cell["M"] == math.gcd(cell["dp"], cell["dq"]) == 2,
        "A1: admitted M derived as gcd of the child shape")
    # IIa uniqueness spot checks from the sealed run
    for (nu, l) in ((5, 1), (3, 3), (7, 1), (5, 3)):
        c = C.iia_cell(nu, l, frac(2))
        chk(c["kbar"].denominator != 1,
            "A1: IIa (2,%d,%d) fails integrality" % (nu, l))
    # dq = 1 (mod nu) (R1.0 forced eta slot at nu>=2) on every emitted cell
    ok = cell["dq"] % cell["nu"] == 1
    cells, _ = C.dirty_cells(
        frac(3, 2), 2, 4,
        nonzero_carrier=C.FULL_ACTUAL_FIRST_SEPARATION)
    ok = ok and all(c["dq"] % c["nu"] == 1 for c in cells)
    chk(ok, "A1: dq=1 (mod nu) on every nu>=2 cell (R1.0 eta slot forced)")
    # family-I corrected split present, no machine-cap row anywhere
    chk(mrecs["MERGE/FAMILY-I/L-odd"]["verdict"] == "DEAD"
        and mrecs["MERGE/FAMILY-I/L-even"]["verdict"] == "DEAD"
        and mrecs["MERGE/FAMILY-I/L-0"]["verdict"] == "REJECTED",
        "A1: family-I split (odd L MP2; even L D9; L=0 impossible)")
    chk("l<=4" not in C.canonical_json(BOOK["sections"]["merge"]),
        "A1: no l<=4 machine-cap row survives in the merge partition")
    chk(mrecs["MERGE/MIXED/all-mu>=2"]["verdict"] == "UNREACHABLE",
        "A1: mixed all-mu>=2 unreachable (mu | M=1), not silently covered")


# ==========================================================================
# A2 -- corrected fail-closed discipline
# ==========================================================================

def test_a2():
    chk(BOOK["uncovered"] == [],
        "A2: real-book UNCOVERED list is EMPTY at this header (and that is "
        "a pass)")
    chk(V.validate(fresh_book(), SUMMARY) == [],
        "A2: validator passes the corrected book")
    # planted theorem-killed open row (the sealed 5.4 row) must FAIL
    b = fresh_book()
    b["uncovered"].append({
        "record_id": "MERGE/NU1-ETA/l-odd>=5",
        "family_spec": {"nu_G": 1, "eps_p": 0, "mu": [1, 1], "l": 5,
                        "eps_q": 1},
        "classification": "UNCOVERED", "verdict": "NA",
        "uncovered": {"h": "uncapped exclusion of the eta-factor family",
                      "smallest_instance": "(dp,dq)=(2,8)",
                      "blocked_consumers": ["td=6 jump-menu exactness"]}})
    fails = V.validate(b)
    chk(any("killed by a cited promoted theorem" in f for f in fails),
        "A2: sealed 5.4 UNCOVERED row is rejected as theorem-killed (D9)")
    # planted unclassified candidate must FAIL
    b = fresh_book()
    del b["sections"]["merge"][0]["classification"]
    fails = V.validate(b)
    chk(any("unclassified candidate" in f for f in fails),
        "A2: unclassified candidate fails closed")
    # UNCOVERED row without h/instance/consumers must FAIL
    b = fresh_book()
    b["uncovered"].append({
        "record_id": "X/incomplete", "classification": "UNCOVERED",
        "verdict": "NA", "family_spec": {"synthetic_shape": True},
        "uncovered": {"h": "missing fields"}})
    fails = V.validate(b)
    chk(any("lacks h/smallest_instance/blocked_consumers" in f
            for f in fails),
        "A2: UNCOVERED row without instance/consumers fails closed")
    # coverage is orthogonal to alive/dead: DEAD rows are COVERED rows
    chk(all(r["classification"] == "COVERED"
            for r in BOOK["sections"]["merge"] if r["verdict"] == "DEAD"),
        "A2: DEAD verdicts live inside COVERED (orthogonality)")
    # the synthetic genuine cap is UNCOVERED with full fields, not rejected
    probes = BOOK["synthetic_probes"]
    chk(len(probes) == 1 and probes[0]["classification"] == "UNCOVERED"
        and all(k in probes[0]["uncovered"] for k in
                ("h", "smallest_instance", "blocked_consumers")),
        "A2: synthetic cap probe emitted UNCOVERED with h/instance/consumers")


# ==========================================================================
# A3 -- post-jump boundary + residue to budget exhaustion
# ==========================================================================

def test_a3():
    cells, pure_b = C.dirty_cells(
        frac(3, 2), 2, 4,
        nonzero_carrier=C.FULL_ACTUAL_FIRST_SEPARATION)
    priced = {(c["dp"], c["dq"]): c for c in cells if c["lam"] > 0}
    chk(set(priced) == {(21, 15), (20, 16), (7, 5)},
        "A3: P0 first-step dirty menu exactly {(21,15),(20,16),(7,5)}")
    a = priced.get((21, 15))
    chk(a and a["nu"] == 7 and a["kbar"] == 5 and a["lam"] == 2
        and a["w_child"] == frac(2, 3) and a["M_child"] == 3,
        "A3: (A)-cell (21,15): nu=7, kbar=5, lam=2 -> (2/3,3)")
    c_ = priced.get((20, 16))
    chk(c_ and c_["nu"] == 5 and c_["kbar"] == 4 and c_["lam"] == 2
        and c_["w_child"] == frac(3, 4) and c_["M_child"] == 4,
        "A3: (C)-cell (20,16): nu=5, kbar=4, lam=2 -> (3/4,4)")
    e = priced.get((7, 5))
    chk(e and e["nu"] == 2 and e["lam"] == 3 and e["M_child"] == 1,
        "A3: eps-cell (7,5): lam=3, M=1 (R6 dead)")
    chk(len(pure_b) == 1 and pure_b[0]["lam_min"] == 3
        and pure_b[0]["w_child"] == frac(3)
        and pure_b[0]["M_divisors"] == [1],
        "A3: pure-b doubling: w->3, M=1, lam>=3 (R6 dead)")
    chk(not any(c["lam"] == 0 for c in cells),
        "A3: no clean resonant survives from (3/2,2) "
        "(Delta=3 forces dq=5, den(w)=2 does not divide 5)")
    # terminals
    t = C.terminal(frac(2, 3), 3)
    chk(t["ok"] and t["j"] == 1 and t["psi"] == 2 and t["budget"] == 3,
        "A3: terminal (2/3,3): j=1, psi=2, budget 3")
    chk(C.budget_verdict(2, 3) == ("ALIVE", 1),
        "A3: (2/3,3) route ALIVE with slack 1")
    t = C.terminal(frac(3, 4), 4)
    chk(t["ok"] and t["j"] == 1 and t["psi"] == 3 and t["budget"] == 2,
        "A3: terminal (3/4,4): j=1, psi=3, budget 2")
    chk(C.budget_verdict(2, 2) == ("ALIVE_FRAGILE", 0),
        "A3: (3/4,4) route ALIVE_FRAGILE (equality)")
    chk(not C.terminal(frac(3, 2), 2)["ok"],
        "A3: direct terminal from w=3/2 rejected (w>=1)")
    chk(not C.terminal(frac(3, 4), 2)["ok"],
        "A3: (3/4,2) has j=1/2 not in N* -- terminal rejected")
    # residue book to budget exhaustion (derived; exact regression pin)
    terms = BOOK["sections"]["residue_terminals"]
    alive = sorted((tuple(t["state"]), t["verdict"], t["psi"],
                    t["slack_or_overrun"]) for t in terms
                   if t["verdict"] in ("ALIVE", "ALIVE_FRAGILE"))
    expected = sorted([
        (("2/3", 3, 2), "ALIVE", 2, 1),
        (("3/4", 4, 2), "ALIVE_FRAGILE", 3, 0),
        (("2/5", 5, 3), "ALIVE", 1, 1),
        (("2/7", 7, 4), "ALIVE_FRAGILE", 1, 0),
        (("2/9", 9, 4), "ALIVE_FRAGILE", 1, 0),
        (("3/8", 8, 4), "ALIVE_FRAGILE", 1, 0),
        (("3/10", 10, 4), "ALIVE_FRAGILE", 1, 0),
    ])
    chk(alive == expected,
        "A3: R4 residue book has exactly 7 reduced-superset survivors")
    # every deeper ALIVE row sits at psi=1 and Sum lam <= 4 = td-2
    chk(all(s[2] <= 4 for (s, _, _, _) in
            [(st, v, p, sl) for (st, v, p, sl) in alive]),
        "A3: budget exhaustion at Sum lam <= td-2 = 4")
    # stuck states are explicitly route-dead
    stuck = sorted(tuple(t["state"]) for t in terms if t.get("route_dead"))
    chk(stuck == sorted([("3/4", 2, 2), ("1", 2, 4), ("2/3", 3, 4),
                         ("2/9", 3, 4), ("3/10", 2, 4), ("3/10", 5, 4),
                         ("3/2", 2, 4), ("3/8", 2, 4), ("3/8", 4, 4)]),
        "A3: exactly 9 non-completing states marked route-dead by the "
        "fixpoint")
    chk(any(t["state"] == ["3/2", 2, 0] and not t.get("route_dead")
            for t in terms),
        "A3: boundary state itself is not route-dead (completes downstream)")


# ==========================================================================
# D9 -- the reconstructed log-obstruction (exact machine verification)
# ==========================================================================

def test_d9():
    for n, want in ((2, 2), (3, 6), (4, 20), (5, 70), (6, 252)):
        got = C.binom_neg(n, n - 1)
        chk(got == ((-1) ** (n - 1)) * want,
            "D9: C(-n,n-1)=(-1)^(n-1) C(2n-2,n-1) at n=%d" % n)
        r = C.d9_residue_check(n, 1, 3)
        chk(r["match"] and r["nonzero"],
            "D9: residue of p^-n matches closed form and is nonzero, n=%d"
            % n)
    for L in (2, 4, 6, 8):
        for roots in ((1, 3), (-2, 5)):
            st = C.d9_ode_status(L, *roots)
            chk(not st["solvable_nonzero_c"],
                "D9: no rational s with c'!=0 at even L=%d, roots %s"
                % (L, roots))
            st0 = C.d9_ode_status(L, *roots, force_s0_zero=True)
            chk(not st0["solvable_nonzero_c"],
                "D9: s(0)=0 subcase equally dead at L=%d, roots %s"
                % (L, roots))
            chk(C.d9_kernel_is_p_power(L, *roots),
                "D9: kernel = span{p^(L/2)} at L=%d, roots %s" % (L, roots))
    # positive control: L=1 (root l=1) IS solvable with the printed closed
    # form s = t - (a1+a2)/2, c' = -(a1-a2)^2/2
    a1, a2 = 1, 3
    s = [Fraction(-(a1 + a2), 2), Fraction(1)]
    img = C.d9_operator(1, a1, a2, s)
    chk(img[0] == Fraction(-(a1 - a2) ** 2, 2)
        and all(c == 0 for c in img[1:]),
        "D9: positive control L=1 solvable, c'=-(a1-a2)^2/2")
    st = C.d9_ode_status(1, a1, a2)
    chk(st["solvable_nonzero_c"], "D9: L=1 solver agrees (solvable)")
    # the old l1_ode_check B/B-eta kills (legacy l=1,3 with eta) are now
    # D9 instances: L = 2, 4
    chk(C.classify_family_I(2, 2)["verdict"] == "DEAD"
        and C.classify_family_I(2, 4)["verdict"] == "DEAD",
        "D9: legacy machine-killed cells (L=2,4) are D9 instances")


# ==========================================================================
# A4 -- hostile mutation battery
# ==========================================================================

def test_a4():
    # (1) duplicate parametrizations classify identically as D9-dead:
    #     raw (2,8) / legacy (l=5,eps_q=1) / family-I L=6 / L=6 with s(0)=0
    nfs = [C.normalize_nu1_merge(2, dp=2, dq=8),
           C.normalize_nu1_merge(2, l=5, eps_q=1),
           C.normalize_nu1_merge(2, L=6, q0_zero=False),
           C.normalize_nu1_merge(2, L=6, q0_zero=True)]
    chk(len({(nf["dp"], nf["dq"], nf["L"]) for nf in nfs}) == 1,
        "A4-1: all four presentations share one normal form (2,8)=I@L6")
    cls = [C.classify_family_I(2, nf["L"], nf["q0_zero"]) for nf in nfs]
    chk(all(c["verdict"] == "DEAD"
            and any(x["rule"] == "D9-LOG" for x in c["cert_chain"])
            for c in cls),
        "A4-1: all four presentations classify identically D9-dead")
    chk(C.classify_family_I(2, 6)["d9_n"] == 4,
        "A4-1: (2,8) has D9 index n=4 (binomial 20)")
    # legacy eps_q=0/1 records are DIFFERENT family-I cells (L=l vs l+1):
    n0 = C.normalize_nu1_merge(2, l=5, eps_q=0)
    n1 = C.normalize_nu1_merge(2, l=5, eps_q=1)
    chk((n0["L"], n1["L"]) == (5, 6),
        "A4-1: eps_q is a location split, not a duplicate degree leaf")

    # (2) the sealed 5.4 legacy classifier (UNCOVERED at l odd >= 5) is a
    #     caught mutant
    def sealed_54_classifier(l, eps_q):
        if eps_q == 1 and l % 2 == 1 and l >= 5:
            return "UNCOVERED"
        if eps_q == 1 and l in (1, 3):
            return "REJECTED(machine l<=4)"
        return "COVERED"
    got = sealed_54_classifier(5, 1)
    nf = C.normalize_nu1_merge(2, l=5, eps_q=1)
    ref = C.classify_family_I(2, nf["L"], nf["q0_zero"])
    chk(got == "UNCOVERED" and ref["verdict"] == "DEAD",
        "A4-2: sealed 5.4 mutant disagrees with D9 and is caught")

    # (3) wrong cached M (R1 clean-axis line applied to a dirty child)
    cells, _ = C.dirty_cells(
        frac(3, 2), 2, 4,
        nonzero_carrier=C.FULL_ACTUAL_FIRST_SEPARATION)
    a = next(c for c in cells if (c["dp"], c["dq"]) == (21, 15))
    cached = math.gcd(2 * a["nu"], a["nu"] + 1)  # mutant: gcd(l nu, nu+1)
    chk(cached == 2 and a["M_child"] == 3 and cached != a["M_child"],
        "A4-3: cached-M mutant (2 != 3 on the (A)-cell) is caught")
    b = fresh_book()
    for r in b["sections"]["suffix"]:
        if r["record_id"] == "SUFFIX/dirty-(21,15)":
            r["family_spec"]["M_child"] = 2  # plant the cached value
    fails = V.validate(b)
    chk(any("M_child != gcd" in f for f in fails),
        "A4-3: validator catches the planted cached M")

    # (4) inconsistent w_cert: merge child stamped W-PRICED (sealed 1.2(c))
    b = fresh_book()
    for r in b["sections"]["merge"]:
        if r["record_id"] == "MERGE/IIA/admitted-(2,3,1)":
            r["child"]["w_cert"] = C.W_PRICED_COMPLETE
    fails = V.validate(b)
    chk(any("must be W-CLOSED-FORM" in f for f in fails),
        "A4-4: merge child stamped W-PRICED is caught")
    b = fresh_book()
    for r in b["sections"]["suffix"]:
        if r["record_id"] == "SUFFIX/dirty-(21,15)":
            r["w_cert_child"] = "W-PRICED(P0)"  # sealed body's stray token
    fails = V.validate(b)
    chk(any("unknown w_cert token" in f for f in fails),
        "A4-4: stray token W-PRICED(P0) is caught (one coherent set)")

    # (5) root-M=1 kill (historical ordering bug): root M=1 is LEGAL
    lc = C.root_local_cell(2, 1)
    chk(lc["M_root"] == 1 and lc["w"] == frac(1, 3)
        and lc["root_M1_legal"],
        "A4-5: legal local root cell r=2,l=1: w=1/3, M_root=1 (not killed)")
    def mutant_root_m1_kill(cell):
        return cell["M_root"] == 1  # kills root M=1 -- the historical bug
    chk(mutant_root_m1_kill(lc) is True,
        "A4-5: mutant kills the legal cell, hence is caught by the law")

    # (6) l>=1 omission at the root: l=0 must raise
    try:
        C.root_local_cell(2, 0)
        chk(False, "A4-6: root l=0 must be impossible")
    except C.LLError:
        chk(True, "A4-6: root l=0 rejected (0 = theta*p)")

    # (7) case-IV at a genuine merge: flip the root record to TERMINAL
    b = fresh_book()
    for r in b["sections"]["merge"]:
        if r["record_id"] == "MERGE/ROOT/parametric-l>=1":
            r["verdict"] = "NA"
            r["classification"] = "TERMINAL"
    fails = V.validate(b)
    chk(any("MERGE/ROOT" in f or "merge verdict drift" in f for f in fails),
        "A4-7: case-IV-at-merge relabel is caught")

    # (8) case-II model of a ZCH edge: the mutant join law admits w=2
    def mutant_zch_join_case2(w_alphabet):
        return [(w, w) for w in w_alphabet]  # case II: w_other = w_0chain
    chk(mutant_zch_join_case2([frac(2)]) != []
        and C.zch_join([frac(2)]) == [],
        "A4-8: case-II model of the 0-edge is caught (DEPTH 5c)")
    b = fresh_book()
    for r in b["sections"]["merge"]:
        if r["record_id"] == "MERGE/ZCH/0-edge=P1":
            r["verdict"] = "ADMITTED"
    fails = V.validate(b)
    chk(any("merge verdict drift" in f for f in fails),
        "A4-8: ZCH flipped to ADMITTED is caught")

    # (9) equal-mu unequal-w join must be rejected (R2.1(i))
    chk(C.join_handshake([frac(2), frac(2)]) == frac(2),
        "A4-9: equal-w join admissible")
    try:
        C.join_handshake([frac(2), frac(3, 2)])
        chk(False, "A4-9: unequal-w join must be rejected")
    except C.LLError:
        chk(True, "A4-9: unequal-w equal-mu join rejected")

    # (10) l-vs-M conflation (the refuted W_off alphabet)
    chk(C.step_legal(2, 2) and not C.step_legal(2, 3)
        and not C.step_legal(3, 2) and C.step_legal(3, 3),
        "A4-10: dirty l must divide the CURRENT M-state")

    # (11) shared-suffix double count flips the slack-1 verdict
    single = C.budget_verdict(2, 3)
    double = C.budget_verdict(4, 3)  # mutant counts the suffix per pole
    chk(single[0] == "ALIVE" and double[0] == "DEAD",
        "A4-11: shared-suffix double count is caught (verdict flip)")

    # (12) equality-route extra printed unit flips FRAGILE -> DEAD
    chk(C.budget_verdict(2, 2)[0] == "ALIVE_FRAGILE"
        and C.budget_verdict(3, 2)[0] == "DEAD",
        "A4-12: planted extra unit kills the equality route")

    # (13) cap-as-rejection: a COVERED record citing a CAP-tier source fails
    b = fresh_book()
    b["sections"]["merge"].append({
        "record_id": "MERGE/CAP-AS-REJECTION",
        "family_spec": {"synthetic_shape": True},
        "classification": "COVERED", "verdict": "REJECTED",
        "why": "swept l<=4, no solution found (engine cap)",
        "cert_chain": [{"rule": "SYN-1", "tier": "CAP",
                        "source": C.TRUST["SYN-1"]["source"]}]})
    fails = V.validate(b)
    chk(any("caps may only produce UNCOVERED" in f for f in fails),
        "A4-13: cap-as-rejection is caught")

    # (14) mutant that rejects the genuine synthetic cap instead of
    #      emitting UNCOVERED
    b = fresh_book()
    b["synthetic_probes"][0]["classification"] = "COVERED"
    b["synthetic_probes"][0]["verdict"] = "REJECTED"
    derived = C.derive_summary(b)
    chk(derived["synthetic_uncovered_count"] == 0
        and C.derive_summary(fresh_book())["synthetic_uncovered_count"] == 1,
        "A4-14: rejecting the genuine cap is visible in the derived summary")
    fails = V.validate(b, SUMMARY)
    chk(any("summary does not match" in f for f in fails),
        "A4-14: validator catches it against the sealed summary")

    # (15) nu>=2 shape with the eta slot dropped (eps_q=0) violates
    #      dq = 1 (mod nu)
    bad_dq = (2 + 1) * 3  # IIa(2,3,1) without the +1
    chk(bad_dq % 3 != 1 and (bad_dq + 1) % 3 == 1,
        "A4-15: dropping the forced eta slot at nu>=2 breaks R1.0")

    # (16) W-SYMBOLIC arrival must not fire the root window
    rows = C.root_meet([(frac(2), C.W_SYMBOLIC)])
    chk(not rows[0]["window_kill"],
        "A4-16: W-SYMBOLIC never kills a root meet")
    rows = C.root_meet([(frac(2), C.W_PRICED_COMPLETE)])
    chk(rows[0]["window_kill"],
        "A4-16: W-PRICED-COMPLETE does kill at w=2")

    # (17) residue tampering: drop one FRAGILE terminal row
    b = fresh_book()
    b["sections"]["residue_terminals"] = [
        t for t in b["sections"]["residue_terminals"]
        if t["state"] != ["3/8", 8, 4]]
    fails = V.validate(b)
    chk(any("residue terminal rows drift" in f for f in fails),
        "A4-17: deleted residue row is caught by re-enumeration")


# ==========================================================================
# A5 -- provenance
# ==========================================================================

def test_a5():
    zch = sorted(r["record_id"] for r in BOOK["sections"]["merge"]
                 if r["record_id"].startswith("MERGE/ZCH"))
    chk(zch == ["MERGE/ZCH/0-edge=P1", "MERGE/ZCH/0-edge=P2"],
        "A5: pole-swapped arrangements are distinct records")
    chains = sorted(r["pole_id"] for r in BOOK["sections"]["chain"])
    chk(chains == ["P1", "P2"], "A5: per-pole chain records not aggregated")
    reg = BOOK["unused_registry"]
    chk(any(e["fate"] == "NO_TREE_VERTEX" and "IIA" in e["vertex"]
            for e in reg),
        "A5: IIa l=1 q-extra registered NO_TREE_VERTEX (St 3.18/MP6(e))")
    chk(sum(1 for e in reg if e["fate"] == "DECK_CONJUGATE") == 2,
        "A5: nu-1 deck-conjugate slots registered parametrically per pole")
    for r in [x for rows in BOOK["sections"].values() for x in rows]:
        if "cert_chain" in r:
            if not all(c["rule"] in BOOK["trust_snapshot"]
                       for c in r["cert_chain"]):
                chk(False, "A5: cert chain fails to resolve in %s"
                    % r.get("record_id"))
                break
    else:
        chk(True, "A5: every cert_chain resolves to the frozen snapshot")
    # residue paths are representative (recorded) and start at BOUNDARY
    chk(all(t["path"][0] == "BOUNDARY"
            for t in BOOK["sections"]["residue_terminals"]),
        "A5: every residue row carries its path provenance from BOUNDARY")


# ==========================================================================
# R4 -- explicit carrier typing and exact full-actual-floor replay
# ==========================================================================

def test_r4_carrier_reprice():
    policy = BOOK["pricing_policy"]
    chk(policy == {
        "nonzero_carrier": C.FULL_ACTUAL_FIRST_SEPARATION,
        "canonical_alias": C.FULL_ACTUAL_EXIT,
        "representative_carrier": C.REPRESENTATIVE,
        "nonzero_floor": ("delta if delta is a positive integer; "
                          "ceil(2*delta) otherwise"),
        "epsilon_zero_rule": "legacy representative AF2",
        "semantics": C.LOWER_FLOOR_ONLY,
        "attainment": False,
    }, "R4-1: exact typed pricing policy; lower floor and no attainment")

    chk(C.representative_nonzero_floor(frac(2, 3)) == 1
        and C.full_actual_nonzero_floor(frac(2, 3)) == 2
        and C.full_actual_nonzero_floor(frac(1, 3)) == 1
        and C.full_actual_nonzero_floor(frac(3)) == 3,
        "R4-2: representative/full floor branch fixtures")
    try:
        C.full_actual_nonzero_floor(frac(0))
        chk(False, "R4-3: full-actual floor must reject nonpositive defect")
    except C.LLError:
        chk(True, "R4-3: full-actual floor rejects nonpositive defect")

    p_rep = C.typed_exit_price(
        frac(17), frac(5), 2, 3, (3,), C.REPRESENTATIVE)
    p_full = C.typed_exit_price(
        frac(17), frac(5), 2, 3, (3,),
        C.FULL_ACTUAL_FIRST_SEPARATION)
    chk(p_rep["applied_total"] == 2
        and p_full["applied_total"] == 3
        and p_rep["representative_total"] ==
            p_full["representative_total"] == 2
        and p_full["full_actual_total"] == 3,
        "R4-4: (17,5) fixture changes only the typed nonzero component")
    chk(p_full["nonzero"][0]["carrier"] ==
        C.FULL_ACTUAL_FIRST_SEPARATION
        and p_full["nonzero"][0]["delta"] == "2/3"
        and p_full["nonzero"][0]["applied_floor"] == 2
        and p_full["epsilon_zero"]["carrier"] == C.REPRESENTATIVE
        and p_full["epsilon_zero"]["applied_floor"] == 1
        and p_full["attainment"] is False,
        "R4-5: nonzero carrier typed full; epsilon remains representative")

    audit = C.repricing_audit()
    chk(C.canonical_json(audit) ==
        C.canonical_json(BOOK["repricing_audit"]),
        "R4-6: emitted audit equals independent exact replay")
    chk(tuple(tuple(r["cell"]) for r in audit["changed_cells"]) ==
        C.EXPECTED_CHANGED_CELLS
        and [r["representative_total"] for r in audit["changed_cells"]]
            == [2, 2, 2, 1]
        and [r["full_actual_total"] for r in audit["changed_cells"]]
            == [3, 3, 3, 2]
        and [r["zero_epsilon_floor"] for r in audit["changed_cells"]]
            == [1, 1, 1, 0],
        "R4-7: exact four movers and unchanged epsilon/zero floors")
    chk(audit["unique_cells_checked"] == 16
        and audit["unchanged_cell_count"] == 12
        and audit["old_alive_count"] == 13
        and audit["new_alive_count"] == 7
        and audit["added_alive"] == [],
        "R4-8: all 16 cells checked, exactly 4 move, inventory 13->7")
    chk(set(tuple(x) for x in audit["removed_alive"]) ==
        set(C.EXPECTED_REMOVED_ALIVE)
        and set(tuple(x) for x in audit["new_alive"]) ==
        set(C.EXPECTED_FULL_ALIVE),
        "R4-9: exact six removed rows and exact seven survivors")

    for row in BOOK["sections"]["residue_steps"]:
        cell = row.get("cell")
        if not cell:
            continue
        pricing = cell["pricing"]
        chk(pricing["nonzero_carrier"] ==
            C.FULL_ACTUAL_FIRST_SEPARATION
            and pricing["semantics"] == C.LOWER_FLOOR_ONLY
            and pricing["attainment"] is False
            and all(c["carrier"] == C.FULL_ACTUAL_FIRST_SEPARATION
                    and c["certificate"] ==
                        "FULL-ACTUAL-FIRST-SEPARATION"
                    for c in pricing["nonzero"])
            and (pricing["epsilon_zero"] is None
                 or pricing["epsilon_zero"]["carrier"] == C.REPRESENTATIVE),
            "R4-10: every emitted cell keeps direction carriers separated")
    pure_rows = [r for r in BOOK["sections"]["residue_steps"]
                 if "PURE-B" in r.get("step", "")]
    chk(pure_rows and all(
        r.get("pricing", {}).get("carrier") == C.REPRESENTATIVE
        and r["pricing"].get("direction") == "EPSILON_ZERO"
        and r["pricing"].get("attainment") is False
        for r in pure_rows),
        "R4-10b: every pure-epsilon row stays representative/no-attainment")

    evidence = C.load_evidence()
    epins, ebodies = C.verify_evidence_pins(evidence)
    chk(epins == BOOK["provenance"]["evidence_pins"]
        and ebodies == BOOK["provenance"]["evidence_body_pins"]
        and len(epins) == 8 and len(ebodies) == 6,
        "R4-11: theorem/review/software pins and body seals re-verify")
    tampered = dict(evidence)
    target = next(iter(C.EVIDENCE_BODY_PINS))
    body = bytearray(tampered[target])
    body[0] ^= 1
    tampered[target] = bytes(body)
    try:
        C.verify_evidence_pins(tampered)
        chk(False, "R4-12: tampered theorem evidence must fail closed")
    except C.LLError as e:
        chk("EVIDENCE DRIFT" in str(e),
            "R4-12: tampered theorem evidence fails closed")

    root = os.path.normpath(os.path.join(HERE, "..", ".."))
    checker = os.path.join(
        root, "cases", "m2_exit_safe_floor_legacy_reprice_r1_20260829",
        "check.py")
    outs = []
    for opt in (False, True):
        cmd = [sys.executable] + (["-O"] if opt else []) + [checker]
        p = subprocess.run(cmd, cwd=root, stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE, check=False)
        chk(p.returncode == 0 and p.stderr == b"",
            "R4-13: frozen legacy checker exits cleanly%s" %
            (" under -O" if opt else ""))
        outs.append(p.stdout)
    chk(outs[0] == outs[1]
        and hashlib.sha256(outs[0]).hexdigest() ==
            "4498beacf2f119d4f3d1b1750e857549e98f76900899983dd32db5d4e5da0011",
        "R4-14: legacy reprice checker ordinary/-O bytes and hash agree")


# ==========================================================================
# A6 -- source-drift mutation battery (every branch must FAIL CLOSED)
# ==========================================================================

def test_a6_source_drift():
    real = C.load_sources()

    # (1) a single flipped byte anywhere in a re-pinned source fails the
    #     pin gate closed (compile-level firewall)
    tam = dict(real)
    body = bytearray(tam["ladder/BOOK-OFFAXIS.md"])
    body[len(body) // 2] ^= 0x01
    tam["ladder/BOOK-OFFAXIS.md"] = bytes(body)
    try:
        C.verify_source_pins(tam)
        chk(False, "A6-1: single-byte source drift must fail the pin gate")
    except C.LLError as e:
        chk("SOURCE DRIFT" in str(e),
            "A6-1: single-byte source drift fails closed at the pin gate")

    # (2) the compiler itself refuses to emit a book from drifted sources
    try:
        C.compile_book(readers=tam)
        chk(False, "A6-2: compile must abort on drifted sources")
    except C.LLError:
        chk(True, "A6-2: compile_book fails closed on drifted sources")

    # (3) charged-count tamper (351 -> 352 parent pairs): even with the
    #     hash gate bypassed, the count-free parse cross-consistency
    #     catches the drift (the untouched 351/351 sentences disagree)
    texts = {p: b.decode("utf-8") for p, b in real.items()}
    t3 = dict(texts)
    t3["ladder/SHEET6-DEPTH-REVIEW.md"] = t3[
        "ladder/SHEET6-DEPTH-REVIEW.md"].replace("351 parent pairs",
                                                 "352 parent pairs")
    try:
        C.parse_engine_fixture(t3)
        chk(False, "A6-3: charged-count tamper must fail the parse")
    except C.LLError as e:
        chk("INCONSISTENT" in str(e),
            "A6-3: 351->352 tamper fails closed on cross-consistency "
            "(hash gate aside)")

    # (4) deleting a charged sentence kills the parse (no silent default)
    t4 = dict(texts)
    t4["ladder/SHEET6-DEPTH.md"] = t4["ladder/SHEET6-DEPTH.md"].replace(
        "pair depth-invariance", "pair depth-in_variance")
    try:
        C.parse_engine_fixture(t4)
        chk(False, "A6-4: deleted charged sentence must fail the parse")
    except C.LLError as e:
        chk("PARSE FAILED" in str(e),
            "A6-4: missing charged sentence fails closed (never "
            "manufactured)")

    # (5) a consumed-clause deletion (P0 finiteness bound) fails the
    #     anchor gate even before any hash is re-pinned
    t5 = dict(texts)
    t5["ladder/BOOK-OFFAXIS.md"] = t5["ladder/BOOK-OFFAXIS.md"].replace(
        "E | l·num(w_G)·T", "E bounded some other way")
    try:
        C.verify_clause_anchors(t5)
        chk(False, "A6-5: removed P0 finiteness clause must fail")
    except C.LLError as e:
        chk("CLAUSE MISSING" in str(e),
            "A6-5: removed P0 finiteness clause fails the anchor gate "
            "independently of the hash pin")

    # (6) tampered book pin -> validator fails against disk
    b = fresh_book()
    b["provenance"]["source_pins"]["ladder/REDUCTION.md"] = "0" * 64
    fails = V.validate(b)
    chk(any("source_pins drift" in f for f in fails),
        "A6-6: tampered in-book pin is caught by disk re-verification")

    # (7) tampered in-book engine record (351 -> 352) -> validator fails
    b = fresh_book()
    b["provenance"]["engine_record"]["parent_pairs"] = 352
    fails = V.validate(b)
    chk(any("engine_record drift" in f for f in fails),
        "A6-7: tampered in-book 351-route count is caught by re-parse")

    # (8) deleted provenance section -> validator fails (R-6 mandatory)
    b = fresh_book()
    del b["provenance"]
    fails = V.validate(b)
    chk(any("provenance section missing" in f for f in fails),
        "A6-8: provenance section is mandatory (fail closed)")

    # (9) a fabricated decision change must block (empty list enforced)
    b = fresh_book()
    b["provenance"]["rederivation"]["decision_changes"] = [
        {"clause": "P0", "change": "fabricated"}]
    fails = V.validate(b)
    chk(any("decision_changes" in f for f in fails),
        "A6-9: any recorded decision change blocks the packet")

    # (10) validator sees the same drifted-source failure (readers hook)
    fails = V.validate(fresh_book(), None, readers=tam)
    chk(any("provenance fail-closed" in f and "SOURCE DRIFT" in f
            for f in fails),
        "A6-10: validator fails closed on drifted source bytes")


# ==========================================================================
# Determinism / emission
# ==========================================================================

def test_determinism():
    b2 = C.compile_book()
    chk(C.canonical_json(b2) == BOOK_JSON,
        "DET: recompiled book is byte-identical")
    s2 = C.derive_summary(b2)
    chk(C.canonical_json(s2) == C.canonical_json(SUMMARY),
        "DET: recomputed summary is byte-identical")
    outdir = os.path.join(HERE, "out")
    with open(os.path.join(outdir, "ll1_book.json")) as f:
        disk = f.read()
    chk(disk == BOOK_JSON + "\n",
        "DET: emitted out/ll1_book.json matches the in-memory compile")
    chk("/Users/" not in BOOK_JSON and "\\u" not in BOOK_JSON[:200],
        "DET: no absolute paths in the book")
    fails = V.validate(json.loads(disk), json.load(
        open(os.path.join(outdir, "ll1_summary.json"))))
    chk(fails == [], "DET: emitted artifacts validate")


# ==========================================================================
# LL-2 pointer parity (entry layer only; no td=7 claims)
# ==========================================================================

def test_ll2_pointer():
    entries, offaxis = C.entry_menu(7, 2)
    chk(entries == [] and len(offaxis) == 1,
        "LL2: td=7,m=2 entry layer is 100%% off-axis (one entry)")
    if offaxis:
        e = offaxis[0]
        chk(e["Lambda"] == (3, 4) and e["type"] == (2, 3)
            and e["poles"] == ((1, 1, 2), (1, 2, 3)),
            "LL2: the off-axis witness (2,3), Lambda=(3,4), "
            "(1,1,2)+(1,2,3) matches BOOK-OFFAXIS sec.1a")


def main():
    test_a1()
    test_a2()
    test_a3()
    test_d9()
    test_a4()
    test_a5()
    test_r4_carrier_reprice()
    test_a6_source_drift()
    test_determinism()
    test_ll2_pointer()
    print("LL1-R4 acceptance   passed: %d   failed: %d"
          % (PASSED, len(FAILED)))
    if FAILED:
        for name in FAILED:
            print("  FAILED: %s" % name)
        return 1
    print("ALL TESTS PASS (%d checks)" % PASSED)
    return 0


if __name__ == "__main__":
    sys.exit(main())
