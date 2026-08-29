#!/usr/bin/env python3
"""Fail-closed emitter for the M>=2 equal-arrival semilinear quotient.

Emits exact PARAMETRIC identities (closed forms + residue classes), never
sampled evidence, and never a search cap.  Every numeric window in the output
is labelled `window` and is a display convenience; all completeness claims are
carried by the closed forms and the residue sets.

    python3 emit_eqjoin.py --output /tmp/eqjoin.json
    python3 -O emit_eqjoin.py --output /tmp/eqjoin-O.json     # must be identical
"""
import argparse
import hashlib
import json
import sys
from fractions import Fraction as Fr

import controls
from eqjoin_semilinear import (EqJoinFamily, MODULE_TAG, classify_unbounded,
                               merge_local, MergeLocalError)
from t1_merge_reduction import (verify_T1_EQ, verify_T1_GEN,
                                eqjoin_T1_solution, eqjoin_T1_symbolic_criterion)

CAP_TOKENS = ("NUCAP", "MAXNU", "nu_cap", "CAP=", "--cap")


def _fr(x):
    x = Fr(x)
    return "%d/%d" % (x.numerator, x.denominator)


def refuse_caps(argv):
    for a in argv:
        for tok in CAP_TOKENS:
            if tok in a:
                raise SystemExit("REFUSED: cap token %r is not accepted by a "
                                 "cap-free emitter" % tok)


def build(catalogue_window=200):
    out = {"module": MODULE_TAG, "schema": "EQJOIN-EMIT/v1"}

    # --- A. the T1 reductions, symbolically ------------------------------
    t1 = {}
    for (r, mu, eps, lex, nu) in [(2, 1, 0, 0, 2), (2, 1, 0, 1, 3), (2, 2, 0, 0, 3),
                                  (2, 3, 1, 2, 4), (3, 2, 0, 0, 5), (3, 1, 0, 2, 2),
                                  (4, 2, 1, 0, 3), (2, 5, 3, 1, 2)]:
        ok, nterms = verify_T1_EQ(r, mu, eps, lex, nu)
        t1["T1-EQ(r=%d,mu=%d,eps=%d,lex=%d,nu=%d)" % (r, mu, eps, lex, nu)] = \
            {"identity_holds": ok, "residual_terms": nterms}
    for (mults, eps, lex, nu) in [([1], 3, 2, 3), ([2, 1], 0, 0, 7), ([1], 2, 1, 7),
                                  ([3, 1, 1], 2, 1, 2), ([2, 2], 1, 0, 3)]:
        ok, nterms = verify_T1_GEN(mults, eps, lex, nu)
        t1["T1-GEN(mults=%s,eps=%d,lex=%d,nu=%d)" % (mults, eps, lex, nu)] = \
            {"identity_holds": ok, "residual_terms": nterms}
    out["t1_reductions"] = t1

    # --- B. the equal-join T1 closed form --------------------------------
    eq = {}
    for (r, mu, eps) in [(2, 3, 0), (2, 5, 2), (3, 2, 0), (3, 4, 1), (4, 3, 0), (5, 7, 4)]:
        rows = []
        for nu in (2, 3, 5, 7, 11):
            sol = eqjoin_T1_solution(r, mu, eps, nu)
            rows.append({"nu": nu, "forced_zero_pi": sol["forced_zero_pi"],
                         "forced_Rad": sol["forced_Rad"],
                         "C_over_A": _fr(sol["C_over_A"]),
                         "alive": sol["alive"],
                         "top_coeff_vanishes": sol["top_coeff_r"] == 0,
                         "criterion_symbolic": eqjoin_T1_symbolic_criterion(r, mu, eps, nu)})
        eq["r=%d,mu=%d,eps=%d" % (r, mu, eps)] = {
            "law": "Rad(t) = t^r - A (A != 0); C = -nu*r*(mu-eps)*A/dq != 0",
            "uniform_in_nu": all(x["forced_zero_pi"] == list(range(1, r))
                                 and x["alive"] and x["top_coeff_vanishes"]
                                 and x["criterion_symbolic"] for x in rows),
            "window_rows": rows,
        }
    out["eqjoin_t1_closed_form"] = eq

    # --- C. the unbounded classification ---------------------------------
    cls = []
    cases = [
        # (r0, mus, ms, lex, eps, whats, zero_arrival, expected)
        (2, [3, 3], [], 0, 0, [Fr(3), Fr(3)], False, "UNBOUNDED_EQJOIN"),
        (3, [2, 2, 2], [], 0, 0, [Fr(3, 2)] * 3, False, "UNBOUNDED_EQJOIN"),
        (2, [3, 3], [], 0, 1, [Fr(3), Fr(3)], False, "UNBOUNDED_EQJOIN"),
        (2, [3, 3], [], 1, 0, [Fr(3), Fr(3)], False, "BOUNDED"),
        (2, [3, 3], [2], 0, 0, [Fr(3), Fr(3)], False, "BOUNDED"),
        (2, [3, 2], [], 0, 0, [Fr(3), Fr(3)], False, "BOUNDED"),
        (2, [3, 3], [], 0, 0, [Fr(3), Fr(2)], False, "BOUNDED"),
        (1, [1], [], 1, 2, [Fr(2), Fr(7, 2)], True, "BOUNDED"),
        (1, [1], [], 1, 3, [Fr(2), Fr(2)], True, "BOUNDED"),
        (2, [2, 2], [], 2, 2, [Fr(1), Fr(1), Fr(1)], True, "BOUNDED"),
        (2, [2, 2], [], 1, 2, [Fr(5, 2), Fr(5, 2), Fr(5, 2)], True, "BOUNDED"),
    ]
    for (r0, mus, ms, lex, eps, whats, za, expected) in cases:
        v, why = classify_unbounded(r0, mus, ms, lex, eps, whats, za)
        cls.append({"r0": r0, "mus": mus, "ms": ms, "lex": lex, "eps": eps,
                    "whats": [_fr(x) for x in whats], "zero_arrival": za,
                    "verdict": v, "expected": expected, "match": v == expected,
                    "reason": why})
    out["unbounded_classification"] = cls

    # --- D. the normalized family catalogue ------------------------------
    fams = []
    for (r, mu, eps, w) in [(2, 3, 0, Fr(3)), (2, 5, 0, Fr(2)), (2, 5, 2, Fr(7, 3)),
                            (3, 2, 0, Fr(3, 2)), (3, 2, 0, Fr(2)), (4, 3, 0, Fr(5, 3)),
                            (2, 9, 4, Fr(5)), (2, 10, 0, Fr(9))]:
        f = EqJoinFamily(r, mu, eps, w)
        rec = f.record()
        rec["family_sha256"] = f.family_hash()
        rec["window_members"] = f.members(2, catalogue_window)
        rec["window"] = [2, catalogue_window]
        rec["exceptional_nu1"] = {k: (_fr(v) if isinstance(v, Fr) else v)
                                  for k, v in f.exceptional_nu1().items()}
        rec["cross_check_merge_local"] = _cross_check(f)
        fams.append(rec)
    out["families"] = fams

    # --- E. the r = 2 MP2 arithmetic (odd-part law) -----------------------
    r2 = []
    for mu in range(1, 25):
        f = EqJoinFamily(2, mu, 0, Fr(3))
        odd = mu
        while odd % 2 == 0:
            odd //= 2
        r2.append({"mu": mu, "odd_part": odd, "infinite": f.is_infinite()})
    out["r2_odd_part_law"] = {
        "statement": "at r = 2, M = gcd(mu-eps, 2*nu+1) is ODD, so MP2 (M>=2) "
                     "forces the odd part of mu-eps to be >= 3",
        "rows": r2,
        "law_holds": all(x["infinite"] == (x["odd_part"] >= 3) for x in r2),
    }

    # --- F. controls ------------------------------------------------------
    c1 = controls.control_td6_residue_cell()
    c2 = controls.control_d9_nu1_log(10)
    c3 = [controls.control_classBC_recurrence(*args)
          for args in [(2, 3, 3), (1, 3, 2), (2, 1, 7), (3, 5, 4), (5, 2, 3)]]
    c4 = controls.control_duplicate_normalization()
    c5 = controls.control_unequal_mu_false_family(6)
    out["controls"] = {
        "C1_td6_residue_cell": {k: (_fr(v) if isinstance(v, Fr) else v)
                                for k, v in c1.items()},
        "C2_d9_nu1_log": c2,
        "C3_classBC_recurrence": [{k: v for k, v in x.items() if k != "rows"} for x in c3],
        "C4_duplicate_normalization": {
            "cell_tuple_collides_at_nu2": c4["cell_tuple_collides_at_nu2"],
            "lambda_differs": c4["differ"]["lambda"],
            "family_hash_differs": c4["differ"]["family_hash"],
            "dp_slopes": c4["dp_slopes"],
            "whole_family_collision": c4["whole_family_collision"],
        },
        "C5_unequal_mu_false_family": c5,
        "C6_caseIII_index_separation": {
            "merge_local_bound": "nu_G <= mu0 * num(what0), what0 the EFFECTIVE "
                                 "0-edge invariant",
            "printed_DEPTH_5c_reading": "what0 = nu_H * w_H  =>  "
                                        "nu_G <= mu0 * nu_H * num(w_H)",
            "promoted_E5_reading": "what0 = nu_G * w_U  =>  the bound is VACUOUS; "
                                   "boundedness instead comes from two-edge "
                                   "consistency, which PINS nu_G",
            "incoming_index_is_separate": True,
        },
    }

    # --- G. uniform-AP consumer table -------------------------------------
    out["uniform_ap_consumers"] = _uniform_table()

    # --- H. the worked td = 12 instance -----------------------------------
    out["td12_instance"] = _td12_instance(catalogue_window)
    return out


def _td12_instance(window):
    """td = 12, m = 3, M-vector [2,2,2], global type (2,3).

    Entry arithmetic (MP4 + Prop 5.6 (19) + L6, derived here, not read from an
    engine): td = sum Lambda_i, Lambda_i >= beta = 3, prime Lambda forces b = 1
    (MP4), so all-b=2 at td = 12 forces Lambda_i = 4 for every i; then
    Lambda = a*b*alpha*beta/nu = 12a/nu = 4 gives nu = 3a and L6
    gcd(a(alpha+beta), nu) = gcd(5a, 3a) = a = 1.  Hence every pole is
    (a,b,nu) = (1,2,3) with w_0 = a(b(alpha+beta)-1)/(b*nu) = 9/6 = 3/2.
    MP1 (sum (r-1) = m-1 = 2) admits a single r = 3 merge."""
    f = EqJoinFamily(3, 2, 0, Fr(3, 2))
    merge_rows = []
    for nu in f.members(2, window):
        rec = merge_local(3, [2, 2, 2], [], 0, 0, [Fr(3, 2)] * 3, nu, False)
        merge_rows.append({"nu": nu, "dp": rec["dp"], "dq": rec["dq"],
                           "kbar": _fr(rec["kbar"]), "X": _fr(rec["X"]),
                           "M": rec["M"], "lambda": rec["lambda"],
                           "w_trunk": _fr(rec["w_child"])})
    # the exact witness route
    l, eps, k, ms, lex, nu = 2, 0, 1, [1], 0, 25
    w = Fr(9, 2)
    P, s = l + sum(ms), 1 + k + lex
    dp, dq = eps + nu * P, 1 + nu * s
    E = l * dq - dp
    kbar = Fr(l) * w * dq / E
    wF = Fr(l) * w * s / E
    MF = __import__("math").gcd(dp, dq)
    X = kbar * Fr(dp, dq)
    lam = max(1, -((-(X - kbar)).numerator // (X - kbar).denominator))
    j = MF * (1 - wF)
    psi = -((-MF) // int(j)) - 1
    return {
        "entry": {"td": 12, "m": 3, "type": [2, 3], "poles": [[1, 2, 3]] * 3,
                  "Lambda": [4, 4, 4], "M": [2, 2, 2], "w0": "3/2",
                  "entry_is_forced": True},
        "merge": {"r": 3, "mu": 2, "eps": 0, "w": "3/2",
                  "family_sha256": f.family_hash(),
                  "period": f.min_period,
                  "residues": sorted(set(x % f.min_period for x in f.residues)),
                  "infinite": f.is_infinite(),
                  "closed_form": {"dp": "6*nu", "dq": "3*nu+1", "E": 2,
                                  "kbar": "3*(3*nu+1)/2", "X": "9*nu",
                                  "M": 2, "w_trunk": "9/2", "lambda": 0},
                  "window_rows": merge_rows},
        "trunk_witness": {"step": {"l": l, "eps": eps, "k": k, "m_j": ms,
                                   "lex": lex, "nu": nu},
                          "dp": dp, "dq": dq, "E": E, "kbar": _fr(kbar),
                          "X": _fr(X), "w_child": _fr(wF), "M_child": MF,
                          "lambda": lam},
        "terminal": {"w": _fr(wF), "M": MF, "j": int(j), "psi": psi,
                     "budget_td_minus_1_minus_psi": 12 - 1 - psi,
                     "sigma_lambda": lam, "fits": lam <= 12 - 1 - psi,
                     "slack": 12 - 1 - psi - lam},
        "verdict": "budget-fitting for EVERY nu in the infinite progression; "
                   "superset-alive only (R4), lambda values are lower bounds",
    }


def _cross_check(f):
    """Independent recomputation through the generic merge_local engine."""
    rows = []
    for nu in f.members(2, 60)[:6]:
        rec = merge_local(f.r, [f.mu] * f.r, [], 0, f.eps, [f.w] * f.r, nu, False)
        rows.append({
            "nu": nu,
            "dp_ok": rec["dp"] == f.dp(nu), "dq_ok": rec["dq"] == f.dq(nu),
            "M_ok": rec["M"] == f.M(nu), "kbar_ok": rec["kbar"] == f.kbar(nu),
            "X_ok": rec["X"] == f.X(nu), "w_child_ok": rec["w_child"] == f.w_child,
            "lambda_ok": rec["lambda"] == f.lam,
            "E_const": set(rec["E"].values()) == {f.E},
            "C_zero": set(rec["C"].values()) == {0},
        })
    return {"rows": rows, "all_ok": all(all(v for k, v in r.items() if k != "nu")
                                        for r in rows)}


def _uniform_table():
    """Which merge-local consumers read nu_G, and how."""
    return [
        {"consumer": "trunk child w", "dependence": "CONSTANT",
         "formula": "w_tr = mu*w*r/(mu-eps)"},
        {"consumer": "trunk child M", "dependence": "PERIODIC mod (mu-eps)",
         "formula": "M = gcd(mu-eps, nu*r+1)"},
        {"consumer": "lambda_G", "dependence": "CONSTANT",
         "formula": "0 if eps=0 else max(1, ceil(mu*w*r/eps))"},
        {"consumer": "terminal psi (P1)", "dependence": "PERIODIC (through M)",
         "formula": "psi = ceil(M/(M*(1-w_t))) - 1 on the trunk terminal"},
        {"consumer": "T1 (Prop 8.1(iv)) verdict", "dependence": "CONSTANT",
         "formula": "alive; Rad = t^r - A forced, C = -nu*r*(mu-eps)*A/dq != 0"},
        {"consumer": "N1 primitivity gcd(kbar,nu)", "dependence": "PERIODIC mod rad(R)",
         "formula": "gcd(kbar,nu)>1 iff some P|nu with v_P(mu*num w) > v_P(den w*(mu-eps))"},
        {"consumer": "kbar_G, X_G, dp, dq", "dependence": "AFFINE, UNBOUNDED",
         "formula": "kbar = mu*w*(nu*r+1)/(mu-eps)"},
        {"consumer": "edge parameter n_e = nu_e*kbar_G - kbar_e",
         "dependence": "AFFINE; positive for all large nu (never used to kill)",
         "formula": "n_e = nu_e*mu*w*(nu*r+1)/(mu-eps) - kbar_e"},
        {"consumer": "later case-III 0-edge, THIS vertex leaving",
         "dependence": "FULL PARAMETER",
         "formula": "what0 = nu_G*w_tr (printed 5c) -> bounded by the sol56 "
                    "two-pole incoming-index theorem"},
    ]


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    refuse_caps(argv)
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", default=None)
    ap.add_argument("--window", type=int, default=200,
                    help="display window for family members (NOT a completeness cap)")
    args = ap.parse_args(argv)
    doc = build(args.window)
    blob = json.dumps(doc, sort_keys=True, separators=(",", ":"))
    digest = hashlib.sha256(blob.encode("utf-8")).hexdigest()
    if args.output:
        with open(args.output, "w") as fh:
            fh.write(blob)
    # fail-closed summary
    ok = True
    ok &= all(v["identity_holds"] for v in doc["t1_reductions"].values())
    ok &= all(v["uniform_in_nu"] for v in doc["eqjoin_t1_closed_form"].values())
    ok &= all(x["match"] for x in doc["unbounded_classification"])
    ok &= all(f["cross_check_merge_local"]["all_ok"] for f in doc["families"])
    ok &= doc["r2_odd_part_law"]["law_holds"]
    ok &= doc["controls"]["C1_td6_residue_cell"]["matches_obstruction_O"]
    ok &= doc["controls"]["C2_d9_nu1_log"]["nu1_reduction_identity"]
    ok &= all(r["nonzero"] for r in doc["controls"]["C2_d9_nu1_log"]["rows"])
    ok &= all(x["recurrence_matches_sol_td7_law"] and x["law_agrees"]
              for x in doc["controls"]["C3_classBC_recurrence"])
    ok &= doc["controls"]["C4_duplicate_normalization"]["cell_tuple_collides_at_nu2"]
    ok &= not doc["controls"]["C4_duplicate_normalization"]["whole_family_collision"]
    ok &= doc["controls"]["C5_unequal_mu_false_family"]["clean"]
    print("emit_sha256 %s" % digest)
    print("t1_identities %d" % len(doc["t1_reductions"]))
    print("families %d" % len(doc["families"]))
    print("EQJOIN_EMIT_%s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
