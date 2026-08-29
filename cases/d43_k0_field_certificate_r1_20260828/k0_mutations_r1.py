#!/usr/bin/env python3
"""Hostile mutation battery for the D43 `K0` field certificate.

Every load-bearing datum of :class:`k0_field_checker_r1.Spec` is directly
perturbed and the resulting run must fail **at a named gate, for the intended
reason**.  Merely observing "something failed" is not accepted: each MUST_FAIL
entry names the gate that has to report the failure.

Two entries are ``MUST_SURVIVE``.  They perturb a load-bearing datum in a way
that changes no mathematical content (a different representative of the same
class, and a different basis of the same subgroup Delta).  A battery in which
every mutation fails is a battery that is testing its own plumbing rather than
the certificate, so these two are gates on the harness itself.

The module also carries one standalone gate unit test: the order-42 test used
in the charged report's illustrative GP recipe omits the prime 7, and an
explicit element of order 6 passes it.  The corrected gate rejects that element.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import replace
from fractions import Fraction as Fr
from pathlib import Path

import k0_algebra_r1 as KA
import k0_field_checker_r1 as CK

SCHEMA = "d43-k0-field-certificate-mutations-r1"

MUST_FAIL = "MUST_FAIL"
MUST_SURVIVE = "MUST_SURVIVE"

_Q0 = dict(CK.TRUE_Q0)


def _q0_with(key, value):
    d = dict(_Q0)
    d[key] = value
    return tuple(sorted(d.items()))


def _phi42_last_flipped():
    t = list(CK.TRUE_PHI42)
    t[-1] = -1
    return tuple(t)


# name, kind, intended gate(s), spec overrides, note
MUTATIONS = [
    # ---- L0: the literal source ------------------------------------------
    ("M_SRC_PHI42_LAST", MUST_FAIL, ["SRC_PHI42_LITERAL"],
     {"phi42": _phi42_last_flipped()},
     "the charged report's own L0 mutation: Phi42 last entry 1 -> -1"),
    ("M_SRC_PHI42_MIDDLE", MUST_FAIL, ["SRC_PHI42_LITERAL"],
     {"phi42": CK.TRUE_PHI42[:4] + (1,) + CK.TRUE_PHI42[5:]},
     "monicity preserved, so only the literal pin can catch this"),
    ("M_SRC_BASIS_SHAPE", MUST_FAIL, ["SRC_ALGEBRA_BLOCK"],
     {"basis_shape": (12, 2, 3, 3, 3)},
     "shape drift against the literal COEFFICIENT_ALGEBRA block"),
    ("M_SRC_RANK", MUST_FAIL, ["SRC_ALGEBRA_BLOCK", "RANK432_MONIC_BASIS"],
     {"basis_rank": 144},
     "rank drift: 144 was one of the degrees the charged reports left legal"),
    ("M_SRC_DISC", MUST_FAIL, ["PHI42_DISCRIMINANT"],
     {"phi42_disc": 3 ** 6 * 7 ** 10 * 2},
     "an even discriminant would let the r3 layer collapse"),

    # ---- L1: base generation ---------------------------------------------
    ("M_BASE_R3_EXPONENTS", MUST_FAIL, ["BASE_WELLDEFINED"],
     {"r3_exponents": (12, 156)},
     "the report's L1 mutation: r3 := zeta^12+zeta^-12 = zeta_14 + conj"),
    ("M_BASE_H_DENOMINATOR", MUST_FAIL, ["BASE_WELLDEFINED"],
     {"h_halving_denominator": 3},
     "the report's L1 mutation: h := sqrt2*sqrt3/3"),
    ("M_BASE_ORDER42_INCOMPLETE", MUST_FAIL, ["BASE_WELLDEFINED"],
     {"order42_prime_cofactors": (2, 3)},
     "the charged GP recipe's order test omits the prime 7; see the "
     "GATE_UNIT_ORDER42 unit test below for an element that exploits it"),
    ("M_BASE_SURJ_EXPONENT", MUST_FAIL, ["BASE_SURJECTIVE"],
     {"gen_z42_power": 15},
     "the single load-bearing generation line, perturbed"),
    ("M_BASE_SURJ_DROPPED", MUST_FAIL, ["CENSUS_COMPLETE"],
     {"skip_gates": frozenset({"BASE_SURJECTIVE"})},
     "the report's warning: deleting the surjectivity line must be a FAILED "
     "certificate, never a passed one"),
    ("M_BASE_ZETA8", MUST_FAIL, ["BASE_ZETA8"],
     {"zeta8_exponent": 42},
     "zeta_8 misidentified inside Q(zeta_168)"),

    # ---- L2: Kummer -------------------------------------------------------
    ("M_CHAR_PRIME_SILENT", MUST_FAIL, ["KUMMER_HOMS_EXHIBITED"],
     {"character_primes": (105337, 1009)},
     "the report's L3 mutation: 673 -> 105337, whose characters are trivial"),
    ("M_CHAR_SINGLE_PRIME", MUST_FAIL, ["KUMMER_HOMS_EXHIBITED"],
     {"character_primes": (673,)},
     "one prime is not two independent primes"),
    ("M_CHAR_DEGENERATE_GENERATORS", MUST_FAIL, ["KUMMER_RANK_TWO"],
     {"class_generators": ((1, 0), (2, 0))},
     "two dependent classes cannot span (Z/3)^2"),
    ("M_CLASS_TRIVIAL_REPRESENTATIVE", MUST_FAIL,
     ["KUMMER_REPRESENTATIVE_CLASSES"],
     {"class_representatives": ((1, 0), (0, 1), (1, 1), (0, 0))},
     "the report's L2 mutation, in exponent form: a class that IS a cube"),
    ("M_CLASS_COVERAGE", MUST_FAIL, ["KUMMER_REPRESENTATIVE_CLASSES"],
     {"class_representatives": ((1, 0), (0, 1), (1, 1), (1, 1))},
     "four representatives that cover only six of the eight classes"),

    # ---- L3: structure ----------------------------------------------------
    ("M_RAMIFIED_SET", MUST_FAIL, ["RAMIFIED_EXACTLY_2_3_7"],
     {"ramified_primes": (2, 3, 5, 7)},
     "reading the ramified set off ETALE_LOCALIZATION_PRIMES"),
    ("M_UNRAMIFIED_WITNESS", MUST_FAIL, ["RAMIFIED_EXACTLY_2_3_7"],
     {"ramified_primes": (2, 3, 7), "unramified_witness": 7},
     "a witness that is inside the ramified set proves nothing"),
    ("M_COMPONENT_PRODUCT", MUST_FAIL, ["IDEMPOTENTS_ONLY_0_1"],
     {"components": ("K1", "K2", "K3")},
     "emitting a product decomposition, which this packet forbids"),
    ("M_IDEMPOTENT_LIST", MUST_FAIL, ["IDEMPOTENTS_ONLY_0_1"],
     {"idempotents": (0, 1, "e1")},
     "a nontrivial primitive idempotent in the emitted list"),
    ("M_DEGREE", MUST_FAIL, ["FIELD_DEGREE_432", "RANK432_MONIC_BASIS"],
     {"basis_rank": 216},
     "48*9 must equal the declared degree"),

    # ---- L4: frames -------------------------------------------------------
    ("M_FRAME_A1", MUST_FAIL, ["FRAME_RELATIONS"],
     {"frames": ((105337, (2779, 795, 50631, 10114, 50267)),
                 (105673, (13862, 14686, 38664, 46664, 35053)))},
     "the report's L4 mutation: A1 50630 -> 50631"),
    ("M_FRAME_ZETA_ORDER", MUST_FAIL, ["FRAME_RELATIONS"],
     {"frames": ((105337, (1, 795, 50630, 10114, 50267)),
                 (105673, (13862, 14686, 38664, 46664, 35053)))},
     "zeta42 replaced by 1: Phi42(1) != 0 and the order gate would also fire"),
    ("M_FRAME_P2_SHIFT", MUST_FAIL, ["P2_HENSEL_REPLAY"],
     {"p2_frame": (8852313585, 11012141449, 786496672 + 105337,
                   8038065910, 6003627245)},
     "a second p^2 lift over the same p-frame; etaleness forbids it"),
    ("M_SPLIT_COUNT", MUST_FAIL, ["SPLIT_COUNT_432"],
     {"split_count": 144},
     "the frame count is a consistency check with a hard registered value"),

    # ---- L5: the E-conditional layer -------------------------------------
    ("M_Q0_COEFFICIENT", MUST_FAIL,
     ["Q0_NORMAL_FORM", "E_DIRECT_SUBSTITUTION"],
     {"q0_terms": _q0_with((0, 0, 2, 1, 0), Fr(-5, 7))},
     "the report's L5 mutation: q0 coefficient -5/6 -> -5/7"),
    ("M_Q0_MONOMIAL", MUST_FAIL, ["Q0_NORMAL_FORM", "E_DIRECT_SUBSTITUTION"],
     {"q0_terms": tuple(sorted(
         {(0, 0, 2, 1, 0): Fr(-5, 6), (0, 1, 2, 1, 0): Fr(1, 2),
          (7, 0, 1, 2, 0): Fr(2, 3), (7, 1, 2, 1, 0): Fr(-1, 3)}.items()))},
     "A1^2*A2 -> A1*A2^2 in one term: the u-side of q0 is load-bearing"),
    ("M_E_COEFFICIENT", MUST_FAIL,
     ["E_LITERAL_PIN", "E_DIRECT_SUBSTITUTION"],
     {"e_terms": ((9, 5, 2, 4), (9, 5, 3, 4))},
     "(9-5*r3) -> (9+5*r3): the sign that makes E sigma-symmetric"),
    ("M_E_EXPONENT", MUST_FAIL, ["E_LITERAL_PIN", "E_DIRECT_SUBSTITUTION"],
     {"e_terms": ((9, 5, 2, 4), (9, -5, 3, 2))},
     "W2^4 -> W2^2: no longer the displayed fourth-root relation.  Caught "
     "only because the direct substitution is also run at nontrivial scales; "
     "the W2=1 substitution alone is blind to the exponent on W2."),
    ("M_E_DIRECT_DROPPED", MUST_FAIL, ["CENSUS_COMPLETE"],
     {"skip_gates": frozenset({"E_DIRECT_SUBSTITUTION"})},
     "the report's tautological-pass hole: keeping only c = -u^10 and "
     "dropping the direct substitution must FAIL the certificate"),
    ("M_E_SCALES_INSUFFICIENT", MUST_FAIL, ["E_DIRECT_SUBSTITUTION"],
     {"e_substitution_scales": ((1, 0, 0, 0, 0),)},
     "one scale is not two: with a single substitution point the gate could "
     "not see the homogeneity of E on the branch line"),
    ("M_E_SCALES_TRIVIAL", MUST_FAIL, ["E_DIRECT_SUBSTITUTION"],
     {"e_substitution_scales": ((1, 0, 0, 0, 0), (1, 0, 0, 0, 0))},
     "two copies of the same scale is one scale"),
    ("M_BRANCH_COUNT", MUST_FAIL, ["FOUR_K0_RATIONAL_BRANCHES"],
     {"branch_count": 3},
     "three branches is not a complete splitting of t^4-c"),
    ("M_POINTBANK_BRANCH_INDEX", MUST_FAIL, ["POINTBANK_REGRESSION"],
     {"pointbank_expected": ((105337, 7210, 2), (105673, 14755, 0))},
     "branch indices are frame-dependent and are pinned, not inferred"),
    ("M_POINTBANK_RATIO", MUST_FAIL, ["POINTBANK_REGRESSION"],
     {"pointbank_expected": ((105337, 7211, 3), (105673, 14755, 0))},
     "the banked ratio is a registered value, not a fitted one"),

    # ---- harness self-gates: these must NOT fail --------------------------
    ("M_CLASS_REP_EPS_SQUARED", MUST_SURVIVE, [],
     {"class_representatives": ((1, 0), (0, 1), (1, 1), (2, 1))},
     "the charged report's own surviving mutation: eps -> eps^2 = 7+4*sqrt3 "
     "is still a non-cube and still covers all eight classes, so the "
     "certificate must PASS.  A battery that reports this as a failure is "
     "miscoded."),
    ("M_CLASS_GENERATOR_BASIS", MUST_SURVIVE, [],
     {"class_generators": ((1, 0), (1, 1))},
     "generators (alpha1, alpha1*alpha2) are a different basis of the same "
     "Delta; independence is basis-free, so the certificate must PASS."),
]


def gate_unit_order42():
    """The order-42 gate, fed an element of order 6.

    The charged report's illustrative GP recipe tests only
    ``z^42==1 && z^21!=1 && z^14!=1``.  ``zeta_168^28`` has order 6 and passes
    all three, so that gate admits an imprimitive root.  The corrected gate
    also tests ``z^6 != 1`` (the prime 7 of 42) and rejects it.
    """
    C = KA.Cyclo168(KA.cyclotomic(168))
    bad = C.xpow(28)
    one = C.const(1)
    report_gate = (C.pw(bad, 42) == one and C.pw(bad, 21) != one
                   and C.pw(bad, 14) != one)
    corrected_gate = report_gate and C.pw(bad, 6) != one
    true_order = next(d for d in range(1, 169) if C.pw(bad, d) == one)
    return {"element": "zeta_168^28", "true_order": true_order,
            "charged_recipe_gate_accepts": report_gate,
            "corrected_gate_accepts": corrected_gate,
            "verdict": "PASS" if (report_gate and not corrected_gate
                                  and true_order == 6) else "FAIL"}


def gate_unit_source_hash(root, pins):
    """A single flipped nibble in a pinned source hash must be caught."""
    bad = dict(pins["sources"])
    key = sorted(bad)[0]
    good = bad[key]
    bad[key] = ("0" if good[0] != "0" else "1") + good[1:]
    payload = CK.run(CK.Spec(label="M_SRC_HASH"), root, bad,
                     pins["emitter_rel"], pins["rows_rel"], None)
    failed = [g["gate"] for g in payload["gates"] if g["status"] != "PASS"]
    return {"mutated_pin": key, "intended_gate": "SRC_FILE_HASHES",
            "failed_gates": failed,
            "verdict": "PASS" if "SRC_FILE_HASHES" in failed else "FAIL"}


def run_battery(root, pins, pointbanks):
    baseline = CK.run(CK.Spec(label="BASELINE"), root, pins["sources"],
                      pins["emitter_rel"], pins["rows_rel"], pointbanks)
    entries = []
    ok = baseline["all_pass"]
    if not ok:
        entries.append({"mutation": "BASELINE", "kind": "BASELINE",
                        "verdict": "FAIL",
                        "detail": "the unmutated certificate does not pass"})
    for name, kind, intended, overrides, note in MUTATIONS:
        spec = replace(CK.Spec(label=name), **overrides)
        payload = CK.run(spec, root, pins["sources"], pins["emitter_rel"],
                         pins["rows_rel"], pointbanks)
        failed = [g["gate"] for g in payload["gates"] if g["status"] != "PASS"]
        if kind == MUST_FAIL:
            hit = [g for g in intended if g in failed]
            verdict = "PASS" if (failed and hit) else "FAIL"
            reason = ("intended gate(s) %s fired" % hit if verdict == "PASS"
                      else "intended gate(s) %s did not fire; failures were %s"
                           % (intended, failed))
        else:
            verdict = "PASS" if payload["all_pass"] else "FAIL"
            reason = ("mutation legitimately survives" if verdict == "PASS"
                      else "a false mutation was rejected; failures were %s"
                           % failed)
        errors = {g["gate"]: g.get("error") for g in payload["gates"]
                  if g["status"] == "FAIL"}
        entries.append({"mutation": name, "kind": kind, "note": note,
                        "intended_gates": intended, "failed_gates": failed,
                        "gate_errors": errors,
                        "unconditional_k0_theorem":
                            payload["unconditional_k0_theorem"],
                        "e_conditional_ratio_theorem":
                            payload["e_conditional_ratio_theorem"],
                        "verdict": verdict, "reason": reason})
        ok = ok and verdict == "PASS"
    units = {"GATE_UNIT_ORDER42": gate_unit_order42(),
             "GATE_UNIT_SOURCE_HASH": gate_unit_source_hash(root, pins)}
    ok = ok and all(u["verdict"] == "PASS" for u in units.values())
    survive = [e for e in entries if e.get("kind") == MUST_SURVIVE]
    ok = ok and len(survive) >= 1 and all(e["verdict"] == "PASS" for e in survive)
    payload = {
        "schema": SCHEMA,
        "baseline_all_pass": baseline["all_pass"],
        "baseline_census_sha256": baseline["census_sha256"],
        "mutation_count": len(MUTATIONS),
        "must_fail_count": sum(1 for m in MUTATIONS if m[1] == MUST_FAIL),
        "must_survive_count": sum(1 for m in MUTATIONS if m[1] == MUST_SURVIVE),
        "mutations": entries,
        "gate_unit_tests": units,
        "battery_pass": ok,
    }
    payload["battery_sha256"] = hashlib.sha256(
        CK.canonical([[e["mutation"], e["verdict"]] for e in entries])
    ).hexdigest()
    return payload


def build_parser():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", required=True)
    ap.add_argument("--pins", required=True)
    ap.add_argument("--pointbank", action="append", default=[],
                    metavar="PRIME:PATH:SHA256")
    ap.add_argument("--out", default="-")
    return ap


def main(argv=None):
    args = build_parser().parse_args(argv)
    pins = json.loads(Path(args.pins).read_text())
    banks = None
    if args.pointbank:
        spec = []
        for item in args.pointbank:
            prime, path, sha = item.split(":", 2)
            spec.append((int(prime), path, sha))
        banks = CK.read_pointbanks(spec)
    payload = run_battery(args.root, pins, banks)
    blob = CK.canonical(payload)
    if args.out == "-":
        sys.stdout.write(blob.decode("ascii") + "\n")
    else:
        Path(args.out).write_bytes(blob)
    return 0 if payload["battery_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
