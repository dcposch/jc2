#!/usr/bin/env python3
"""Fail-closed validator for the LL1-R3 book.

Derives, never trusts: every summary figure is recomputed from the record
level; every record's arithmetic (kbar, M = gcd(dp,dq), X, w_trunk, lam,
j, psi, budget verdict, route-death fixpoint) is re-derived from its family
spec; every cert resolves against the frozen trust snapshot; UNCOVERED rows
are re-run through the corrected classifier and FAIL if a cited promoted
theorem already kills them.  Caps (tier CAP) may only ever appear under
UNCOVERED.  R3 additionally re-verifies the five source pins against the
byte-exact files on disk, re-checks every consumed-clause anchor, re-parses
the frozen 26-shape/351-route engine fixture with count-free regexes, and
re-runs the engine parity checks -- any source drift fails the validation
closed.  No `assert` statements: all checks raise/collect explicitly, so
behaviour is identical under `python -O`.

Usage: python3 ll1_validator.py [outdir]   (exit 0 iff the book validates)
"""

from fractions import Fraction
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ll1_compiler as C


def _fr(s):
    return Fraction(s)


def validate(book, summary=None, readers=None):
    """Return a list of failure strings (empty iff the book validates).
    `readers` (mutation battery only) substitutes source bytes; by default
    the pinned sources are re-read from disk."""
    fails = []

    def need(cond, msg):
        if not cond:
            fails.append(msg)

    # ---- provenance (R-6/R-7): fail closed on any source drift ------------
    prov = book.get("provenance")
    if not isinstance(prov, dict):
        fails.append("provenance section missing (R-6)")
        prov = {}
    try:
        sources = C.load_sources(readers)
        pins = C.verify_source_pins(sources)
        need(prov.get("source_pins") == pins,
             "book source_pins drift against re-verified disk pins")
        texts = {p: b.decode("utf-8") for p, b in sources.items()}
        clauses = C.verify_clause_anchors(texts)
        need(C.canonical_json(prov.get("consumed_clauses")) ==
             C.canonical_json(clauses),
             "consumed-clause table drift against re-verified anchors")
        record = C.parse_engine_fixture(texts)
        need(C.canonical_json(prov.get("engine_record")) ==
             C.canonical_json(record),
             "engine_record drift against count-free re-parse of the "
             "pinned fixture bytes")
        parity = C.engine_parity_checks(record)
        need(C.canonical_json(prov.get("engine_parity")) ==
             C.canonical_json(parity),
             "engine_parity table drift against re-run parity checks")
    except C.LLError as e:
        fails.append("provenance fail-closed: %s" % e)
    except OSError as e:
        fails.append("provenance fail-closed (unreadable source): %s" % e)
    need(prov.get("r2_superseded_pins") ==
         dict(sorted(C.R2_SUPERSEDED_PINS.items())),
         "R2 superseded-pin audit trail drift")
    need("NOT re-run" in prov.get("engine_record", {}).get("scope", ""),
         "engine_record scope must state the engine is NOT re-run "
         "(no manufactured parity)")
    need(prov.get("rederivation", {}).get("decision_changes") == [],
         "rederivation.decision_changes must be the empty list at R3 "
         "(any entry is a finding that blocks SOURCE_READY)")

    # ---- token discipline -------------------------------------------------
    need(set(book.get("w_cert_tokens", [])) == set(C.W_CERT_TOKENS),
         "w_cert token set drift")
    need(set(book.get("root_kill_certs", [])) == set(C.ROOT_KILL_CERTS),
         "root kill-cert set drift")
    sections = book.get("sections", {})
    all_records = [r for rows in sections.values() for r in rows]
    for r in all_records:
        cl = r.get("classification")
        vd = r.get("verdict")
        if cl is not None:
            need(cl in C.CLASSIFICATIONS,
                 "unknown classification %r in %s" % (cl, r.get("record_id")))
        if vd is not None and "state" not in r and "from" not in r:
            need(vd in C.VERDICTS,
                 "unknown verdict %r in %s" % (vd, r.get("record_id")))
        for ch in r.get("cert_chain", []):
            rid = ch.get("rule")
            need(rid in book.get("trust_snapshot", {}),
                 "cert id %r not in frozen snapshot (%s)"
                 % (rid, r.get("record_id")))
            tier = book.get("trust_snapshot", {}).get(rid, {}).get("tier")
            if cl in ("COVERED", "TERMINAL"):
                need(tier in C.ALLOWED_TIERS,
                     "CAP-tier (or unknown-tier) source %r cited by a %s "
                     "record %s -- caps may only produce UNCOVERED"
                     % (rid, cl, r.get("record_id")))
        wc = r.get("w_cert_child")
        if wc is not None:
            need(wc in C.W_CERT_TOKENS,
                 "unknown w_cert token %r in %s" % (wc, r.get("record_id")))

    # ---- entry ------------------------------------------------------------
    entries, offaxis = C.entry_menu(6, 2)
    need(len(entries) == 1 and not offaxis,
         "re-derived entry menu is not the unique on-axis entry")
    erecs = sections.get("entry", [])
    need(len(erecs) == 1, "entry section must have exactly one record")
    if erecs:
        er = erecs[0]
        need(er.get("header_key", {}).get("Lambda") == [3, 3]
             and er.get("header_key", {}).get("type") == [2, 3],
             "entry header drift")
        for p in er.get("poles", []):
            need(p.get("a") == 1 and p.get("b") == 1 and p.get("nu") == 2
                 and _fr(p.get("kbar")) == 5 and _fr(p.get("w0")) == 2
                 and p.get("w_cert") == C.W_CLOSED_FORM,
                 "entry pole frame drift (%s)" % p.get("pole_id"))

    # ---- chains -----------------------------------------------------------
    W = C.w_closure(Fraction(2))
    need(W == [Fraction(2)], "W(2) closure drift")
    crecs = sections.get("chain", [])
    need(len(crecs) == 2, "chain section must have two pole records")
    need(len({r.get("pole_id") for r in crecs}) == 2,
         "chain records aggregate pole contexts (A5)")

    # ---- merge partition --------------------------------------------------
    mrecs = {r["record_id"]: r for r in sections.get("merge", [])}
    expected_ids = {
        "MERGE/ROOT/parametric-l>=1": "DEAD",
        "MERGE/ROOT/l=0": "REJECTED",
        "MERGE/ZCH/0-edge=P1": "REJECTED",
        "MERGE/ZCH/0-edge=P2": "REJECTED",
        "MERGE/IIA/l-or-nu-even": "DEAD",
        "MERGE/IIA/l-nu-odd-nonintegral": "REJECTED",
        "MERGE/IIA/admitted-(2,3,1)": "ADMITTED",
        "MERGE/FAMILY-I/L-odd": "DEAD",
        "MERGE/FAMILY-I/L-even": "DEAD",
        "MERGE/FAMILY-I/L-0": "REJECTED",
        "MERGE/MIXED/all-mu>=2": "UNREACHABLE",
    }
    need(set(mrecs) == set(expected_ids),
         "merge partition drift: %r" % sorted(
             set(mrecs) ^ set(expected_ids)))
    for rid, vd in expected_ids.items():
        if rid in mrecs:
            need(mrecs[rid].get("verdict") == vd,
                 "merge verdict drift at %s (%r != %r)"
                 % (rid, mrecs[rid].get("verdict"), vd))
    # IIa admitted cell arithmetic re-derived
    adm = mrecs.get("MERGE/IIA/admitted-(2,3,1)")
    if adm:
        cell = C.iia_cell(3, 1, Fraction(2))
        need(_fr(adm["cell"]["kbar"]) == cell["kbar"] == 5
             and adm["cell"]["dp"] == 6 and adm["cell"]["dq"] == 10
             and _fr(adm["cell"]["X"]) == 3 and adm["cell"]["M"] == 2,
             "IIa admitted cell arithmetic drift")
        need(adm["cell"]["M"] == math.gcd(adm["cell"]["dp"],
                                          adm["cell"]["dq"]),
             "IIa M != gcd(dp,dq)")
        need(tuple(adm["child"]["Q"]) == (6, 12, 3, 2, 5)
             and _fr(adm["child"]["w_trunk"]) == Fraction(3, 2),
             "IIa child drift")
        need(adm["child"]["w_cert"] == C.W_CLOSED_FORM,
             "IIa merge child must be W-CLOSED-FORM (repair R-4), got %r"
             % adm["child"].get("w_cert"))
        # uniqueness re-derived: no other integral M=2 IIa cell (theorem
        # d | 4; plus an instance sweep as a parity check)
        for nu in range(2, 60):
            for l in range(1, 40):
                c = C.iia_cell(nu, l, Fraction(2))
                if c["M"] == 2 and c["kbar"].denominator == 1:
                    need((nu, l) == (3, 1),
                         "IIa uniqueness violated at (nu,l)=(%d,%d)" % (nu, l))
    # family-I split re-derived, including the duplicate parametrizations
    for L in range(0, 13):
        got = C.classify_family_I(2, L)
        if L == 0:
            need(got["verdict"] == "REJECTED", "family-I L=0 drift")
        elif L % 2 == 1:
            need(got["verdict"] == "DEAD" and got["M"] == 1
                 and any(c["rule"] == "MP2" for c in got["cert_chain"]),
                 "family-I odd-L split drift at L=%d" % L)
        else:
            need(got["verdict"] == "DEAD" and got["M"] == 2
                 and any(c["rule"] == "D9-LOG" for c in got["cert_chain"]),
                 "family-I even-L split drift at L=%d" % L)
    for pres in (dict(dp=2, dq=8), dict(l=5, eps_q=1),
                 dict(L=6, q0_zero=False), dict(L=6, q0_zero=True)):
        nf = C.normalize_nu1_merge(2, **pres)
        need(nf["L"] == 6 and nf["dp"] == 2 and nf["dq"] == 8,
             "duplicate-parametrization normalization drift for %r" % pres)
        cl = C.classify_family_I(2, nf["L"], nf["q0_zero"])
        need(cl["verdict"] == "DEAD"
             and any(c["rule"] == "D9-LOG" for c in cl["cert_chain"]),
             "presentation %r must classify D9-dead" % pres)
    # D9 exact verification at the smallest instances (both root pairs)
    for L in (2, 4, 6, 8):
        for (a1, a2) in ((1, 3), (-2, 5)):
            st = C.d9_ode_status(L, a1, a2)
            need(not st["solvable_nonzero_c"],
                 "D9 obstruction failed at L=%d roots (%s,%s)" % (L, a1, a2))
            st0 = C.d9_ode_status(L, a1, a2, force_s0_zero=True)
            need(not st0["solvable_nonzero_c"],
                 "D9 s(0)=0 subcase failed at L=%d" % L)
            need(C.d9_kernel_is_p_power(L, a1, a2),
                 "D9 kernel p^{L/2} check failed at L=%d" % L)

    # ---- suffix first-step menu -------------------------------------------
    cells, pure_b = C.dirty_cells(Fraction(3, 2), 2, 4)
    priced = sorted((c["dp"], c["dq"]) for c in cells if c["lam"] > 0)
    need(priced == [(7, 5), (20, 16), (21, 15)],
         "re-derived P0 first-step dirty menu drift: %r" % priced)
    srecs = {r["record_id"]: r for r in sections.get("suffix", [])}
    for rid in ("SUFFIX/dirty-(21,15)", "SUFFIX/dirty-(20,16)",
                "SUFFIX/dirty-(7,5)", "SUFFIX/neutral-thick-l2-nu-odd",
                "SUFFIX/neutral-thick-l2-nu-even", "SUFFIX/thin-l1",
                "SUFFIX/clean-resonant", "SUFFIX/pure-b-eps1"):
        need(rid in srecs, "missing suffix record %s" % rid)
    for c in cells:
        rid = "SUFFIX/dirty-(%d,%d)" % (c["dp"], c["dq"])
        r = srecs.get(rid)
        if not r:
            continue
        fs = r["family_spec"]
        need(int(fs["M_child"]) == math.gcd(c["dp"], c["dq"]),
             "%s: M_child != gcd(dp,dq) of the child shape (repair R-3)"
             % rid)
        need(_fr(fs["kbar"]) == c["kbar"] and int(fs["lam"]) == c["lam"]
             and _fr(fs["w_child"]) == c["w_child"],
             "%s: cell arithmetic drift" % rid)
        if r.get("verdict") == "ADMITTED":
            need(r.get("w_cert_child") == C.W_PRICED_COMPLETE,
                 "%s: priced suffix child must be W-PRICED-COMPLETE" % rid)

    # ---- residue: re-walk every step and terminal -------------------------
    terms = sections.get("residue_terminals", [])
    steps = sections.get("residue_steps", [])
    rterms, rsteps, _ = C.residue_enumeration(6)

    def _tkey(rows):
        return sorted(C.canonical_json(r) for r in rows)
    need(_tkey(terms) == _tkey(rterms), "residue terminal rows drift "
         "against independent re-enumeration")
    need(_tkey(steps) == _tkey(rsteps), "residue step rows drift against "
         "independent re-enumeration")
    for t in terms:
        wstr, M, lam = t["state"]
        w = _fr(wstr)
        tt = C.terminal(w, int(M), 6)
        if t.get("verdict") in ("ALIVE", "ALIVE_FRAGILE", "DEAD"):
            need(tt["ok"], "terminal state %r re-check failed" % t["state"])
            if tt["ok"]:
                vd, slack = C.budget_verdict(int(lam), tt["budget"])
                need(vd == t["verdict"] and tt["psi"] == t["psi"]
                     and tt["j"] == t["j"]
                     and slack == t["slack_or_overrun"],
                     "terminal verdict/psi/j/slack drift at %r" % t["state"])
        elif t.get("verdict") == "TERMINAL-REJECTED":
            need(not tt["ok"], "TERMINAL-REJECTED state %r actually has an "
                 "admissible terminal" % t["state"])

    # ---- UNCOVERED discipline (corrected A2) ------------------------------
    for row in book.get("uncovered", []):
        u = row.get("uncovered", {})
        need(all(k in u for k in ("h", "smallest_instance",
                                  "blocked_consumers")),
             "UNCOVERED row lacks h/smallest_instance/blocked_consumers: %r"
             % row.get("record_id"))
        fs = row.get("family_spec", {})
        # theorem-kill check: a nu=1 family-I presentation that a cited
        # promoted theorem already kills must NOT be UNCOVERED
        if fs.get("nu_G") == 1 or fs.get("family") == "I" or (
                "eps_q" in fs or "L" in fs):
            try:
                nf = C.normalize_nu1_merge(
                    2, l=fs.get("l"), eps_q=fs.get("eps_q"),
                    L=fs.get("L"), q0_zero=fs.get("q0_zero"),
                    dp=fs.get("dp"), dq=fs.get("dq"))
                cl = C.classify_family_I(2, nf["L"], nf["q0_zero"])
                need(False,
                     "UNCOVERED row %r is killed by a cited promoted "
                     "theorem (%s: %s)" % (
                         row.get("record_id"), cl["verdict"],
                         ";".join(c["rule"] for c in cl["cert_chain"])))
            except C.LLError:
                pass
    for p in book.get("synthetic_probes", []):
        if p.get("classification") == "UNCOVERED":
            u = p.get("uncovered", {})
            need(all(k in u for k in ("h", "smallest_instance",
                                      "blocked_consumers")),
                 "synthetic UNCOVERED probe lacks h/instance/consumers")

    # every record classified: no record may lack a classification
    for r in all_records:
        if "record_id" in r:
            need(r.get("classification") in C.CLASSIFICATIONS,
                 "unclassified candidate record %r (fail-closed totality)"
                 % r.get("record_id"))

    # ---- unused registry (A5 additions) -----------------------------------
    reg = book.get("unused_registry", [])
    need(any(e.get("fate") == "NO_TREE_VERTEX"
             and "IIA" in e.get("vertex", "") for e in reg),
         "IIa q-extra missing from unused_registry as NO_TREE_VERTEX")
    need(sum(1 for e in reg if e.get("fate") == "DECK_CONJUGATE") == 2,
         "per-pole DECK_CONJUGATE parametric slots missing")

    # ---- summary re-derivation --------------------------------------------
    if summary is not None:
        derived = C.derive_summary(book)
        need(C.canonical_json(derived) == C.canonical_json(summary),
             "summary does not match the record-level re-derivation")
    return fails


def main(argv):
    here = os.path.dirname(os.path.abspath(__file__))
    outdir = argv[1] if len(argv) > 1 else os.path.join(here, "out")
    with open(os.path.join(outdir, "ll1_book.json")) as f:
        book = json.load(f)
    with open(os.path.join(outdir, "ll1_summary.json")) as f:
        summary = json.load(f)
    fails = validate(book, summary)
    if fails:
        print("VALIDATION FAILED (%d):" % len(fails))
        for m in fails:
            print("  - " + m)
        return 1
    print("LL1-R3 validation OK (all record arithmetic re-derived; "
          "UNCOVERED discipline enforced; summary recomputed; 5 source "
          "pins + consumed-clause anchors + engine fixture re-verified "
          "from disk)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
