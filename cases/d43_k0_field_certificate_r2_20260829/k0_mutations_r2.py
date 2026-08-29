#!/usr/bin/env python3
"""Hostile mutation battery for the D43 `K0` field certificate, R2.

Every load-bearing datum of :class:`k0_field_checker_r2.Spec` is directly
perturbed and the resulting run must fail **at a named gate, for the intended
reason**.  Merely observing "something failed" is not accepted: each MUST_FAIL
entry names the gate that has to report the failure.

R2 additions:

* ``expected_theorems`` on an entry pins the pair
  ``(unconditional_k0_theorem, e_conditional_ratio_theorem)`` that the run must
  report.  These are the executable negative controls for repair D1: a pure L5
  perturbation must leave the unconditional boolean **true**, and a pure
  corroboration failure must leave **both** true while ``all_pass`` is false.
  A battery whose theorem booleans all move together is testing an entangled
  census, which is exactly the R1 defect.
* mutations for every ``Spec`` field the Fable 5 review found unreachable
  (D6), for the new cardinality and prime-set pins (D4), and for the new
  presentation, sigma and leading-term data (D2/D3/D5).
* four gate unit tests, two of which *demonstrate the R1 defects*: the
  order-42 counterexample, and a side-by-side run showing that the R1
  Galois-stability loop is automatic in the quotient and falsifiable only in
  the free ring.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import replace
from fractions import Fraction as Fr
from pathlib import Path

import k0_algebra_r2 as KA
import k0_field_checker_r2 as CK

SCHEMA = "d43-k0-field-certificate-mutations-r2"

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


_BASE_FRAMES = CK.Spec().frames
_BASE_PB = CK.Spec().pointbank_expected

# name, kind, intended gate(s), spec overrides, expected (uncond, e), note
MUTATIONS = [
    # ---- L0: the literal source and the presentation ---------------------
    ("M_SRC_PHI42_LAST", MUST_FAIL, ["SRC_PHI42_LITERAL"],
     {"phi42": _phi42_last_flipped()}, None,
     "the charged report's own L0 mutation: Phi42 last entry 1 -> -1"),
    ("M_SRC_PHI42_MIDDLE", MUST_FAIL, ["SRC_PHI42_LITERAL"],
     {"phi42": CK.TRUE_PHI42[:4] + (1,) + CK.TRUE_PHI42[5:]}, None,
     "monicity preserved, so only the literal pin can catch this"),
    ("M_SRC_BASIS_SHAPE", MUST_FAIL, ["SRC_ALGEBRA_BLOCK"],
     {"basis_shape": (12, 2, 3, 3, 3)}, None,
     "shape drift against the literal COEFFICIENT_ALGEBRA block"),
    ("M_SRC_RANK", MUST_FAIL, ["SRC_ALGEBRA_BLOCK", "RELATION_LEADING_TERMS"],
     {"basis_rank": 144}, None,
     "rank drift: 144 was one of the degrees the charged reports left legal"),
    ("M_SRC_DISC", MUST_FAIL, ["PHI42_DISCRIMINANT"],
     {"phi42_disc": 3 ** 6 * 7 ** 10 * 2}, None,
     "an even discriminant would let the r3 layer collapse"),
    ("M_LEADING_MONOMIALS", MUST_FAIL, ["RELATION_LEADING_TERMS"],
     {"leading_monomials": ((12, 0, 0, 0, 0), (0, 2, 0, 0, 0),
                            (0, 0, 3, 0, 0), (0, 0, 0, 3, 0),
                            (0, 0, 1, 0, 2))}, None,
     "a non-coprime declared leading monomial: the Buchberger first-criterion "
     "certificate must refuse it"),
    ("M_ALPHA_DATA", MUST_FAIL,
     ["SRC_ALGEBRA_BLOCK", "RANK432_INDEPENDENCE"],
     {"alpha_data": ((3, 1), (3, -2))}, None,
     "alpha2 = 3-2*r3 changes the presentation the whole packet is about"),
    ("M_R_SQUARE", MUST_FAIL, ["SRC_ALGEBRA_BLOCK", "BASE_WELLDEFINED"],
     {"r_square": 5}, None,
     "r3^2 = 5 is a different quadratic layer"),
    ("M_H_RELATION", MUST_FAIL, ["SRC_ALGEBRA_BLOCK", "BASE_WELLDEFINED"],
     {"h_relation": (2, 5)}, None,
     "2h^2 = 5 is a different quadratic layer"),
    ("M_RANK_WITNESS_PRIME", MUST_FAIL, ["RANK432_INDEPENDENCE"],
     {"rank_witness_prime": 673}, None,
     "the independence witness must use a prime that carries a registered "
     "frame, not any prime that happens to be 1 mod 168"),

    # ---- L1: base generation ---------------------------------------------
    ("M_BASE_R3_EXPONENTS", MUST_FAIL, ["BASE_WELLDEFINED"],
     {"r3_exponents": (12, 156)}, None,
     "the report's L1 mutation: r3 := zeta^12+zeta^-12 = zeta_14 + conj.  In "
     "R1 the L2 character layer duplicated 14/154 in its own body and kept "
     "certifying the true object; in R2 it reads this field (repair D5)"),
    ("M_BASE_S2_EXPONENTS", MUST_FAIL, ["BASE_WELLDEFINED"],
     {"s2_exponents": (21, 145)}, None,
     "coverage gap named by the R1 review: sqrt2 misidentified"),
    ("M_BASE_H_DENOMINATOR", MUST_FAIL, ["BASE_WELLDEFINED"],
     {"h_halving_denominator": 3}, None,
     "the report's L1 mutation: h := sqrt2*sqrt3/3"),
    ("M_BASE_ORDER42_INCOMPLETE", MUST_FAIL, ["BASE_WELLDEFINED"],
     {"order42_prime_cofactors": (2, 3)}, None,
     "the charged GP recipe's order test omits the prime 7; see the "
     "GATE_UNIT_ORDER42 unit test below for an element that exploits it"),
    ("M_I_ZETA3_EXPONENT", MUST_FAIL, ["BASE_I_SQUARE"],
     {"i_zeta3_exponent": 7}, None,
     "coverage gap named by the R1 review: zeta42^7 is not a cube root of 1"),
    ("M_BASE_ZETA8", MUST_FAIL, ["BASE_ZETA8"],
     {"zeta8_exponent": 42}, None,
     "zeta_8 misidentified inside Q(zeta_168)"),
    ("M_BASE_SURJ_EXPONENT", MUST_FAIL, ["BASE_SURJECTIVE"],
     {"gen_z42_power": 15}, None,
     "the single load-bearing generation line, perturbed"),
    ("M_BASE_GEN_Z8_POWER", MUST_FAIL, ["BASE_SURJECTIVE"],
     {"gen_z8_power": 4}, None,
     "coverage gap named by the R1 review: the other generation exponent"),
    ("M_BASE_SURJ_DROPPED", MUST_FAIL, ["CENSUS_UNCONDITIONAL"],
     {"skip_gates": frozenset({"BASE_SURJECTIVE"})}, (False, True),
     "the report's warning: deleting the surjectivity line must be a FAILED "
     "certificate.  The layer-restricted census makes it fail the "
     "unconditional theorem only"),
    ("M_CONDUCTOR_TOWER", MUST_FAIL, ["BASE_CONDUCTOR_TOWER"],
     {"conductor_tower": (21, 84, 156)}, None,
     "a top conductor whose cyclotomic degree is not 48"),
    ("M_EPS_DATA", MUST_FAIL, ["KUMMER_NORM_COROBORATION"],
     {"eps_data": (3, 1)}, None,
     "3+sqrt3 is not a unit: the norm-corroboration layer must refuse it"),

    # ---- L2: Kummer -------------------------------------------------------
    ("M_CHAR_PRIME_SILENT", MUST_FAIL, ["KUMMER_HOMS_EXHIBITED"],
     {"character_primes": (105337, 1009)}, None,
     "the report's L3 mutation: 673 -> 105337, whose characters are trivial"),
    ("M_CHAR_SINGLE_PRIME", MUST_FAIL, ["KUMMER_HOMS_EXHIBITED"],
     {"character_primes": (673,)}, None,
     "one prime is not two independent primes"),
    ("M_CHAR_PRIME_DUPLICATE", MUST_FAIL, ["KUMMER_HOMS_EXHIBITED"],
     {"character_primes": (673, 673)}, None,
     "coverage gap named by the R1 review: the same prime twice is one prime"),
    ("M_CHAR_DEGENERATE_GENERATORS", MUST_FAIL, ["KUMMER_RANK_TWO"],
     {"class_generators": ((1, 0), (2, 0))}, None,
     "two dependent classes cannot span (Z/3)^2"),
    ("M_CLASS_TRIVIAL_REPRESENTATIVE", MUST_FAIL,
     ["KUMMER_REPRESENTATIVE_CLASSES"],
     {"class_representatives": ((1, 0), (0, 1), (1, 1), (0, 0))}, None,
     "the report's L2 mutation, in exponent form: a class that IS a cube.  In "
     "R1 the (0,0) test was dead code behind the witness search (repair D10)"),
    ("M_CLASS_COVERAGE", MUST_FAIL, ["KUMMER_REPRESENTATIVE_CLASSES"],
     {"class_representatives": ((1, 0), (0, 1), (1, 1), (1, 1))}, None,
     "four representatives that cover only six of the eight classes"),
    ("M_SILENT_PRIMES", MUST_FAIL,
     ["KUMMER_SILENT_PRIME_GUARD", "KUMMER_HOMS_EXHIBITED"],
     {"silent_primes": (105337, 337)}, None,
     "coverage gap named by the R1 review: the silent list must be the "
     "registered frame prime set"),
    ("M_KUMMER_RANK_DROPPED", MUST_FAIL,
     ["FIELD_DEGREE_432", "CENSUS_UNCONDITIONAL"],
     {"skip_gates": frozenset({"KUMMER_RANK_TWO"})}, (False, True),
     "the R1 degree gate multiplied two literals and survived this; the R2 "
     "gate reads the computed Kummer order out of ctx, so deleting L2's rank "
     "gate breaks L3 (repair: no gate recomputes a literal from itself)"),
    ("M_BASE_DIM_DROPPED", MUST_FAIL,
     ["FIELD_DEGREE_432", "CENSUS_UNCONDITIONAL"],
     {"skip_gates": frozenset({"BASE_DIMENSION_48"})}, (False, True),
     "same test on the other factor of the degree"),

    # ---- L3: structure ----------------------------------------------------
    ("M_RAMIFIED_SET", MUST_FAIL, ["RAMIFIED_EXACTLY_2_3_7"],
     {"ramified_primes": (2, 3, 5, 7)}, None,
     "reading the ramified set off ETALE_LOCALIZATION_PRIMES"),
    ("M_UNRAMIFIED_WITNESS", MUST_FAIL, ["RAMIFIED_EXACTLY_2_3_7"],
     {"ramified_primes": (2, 3, 7), "unramified_witness": 7}, None,
     "a witness that is inside the ramified set proves nothing"),
    ("M_COMPONENT_PRODUCT", MUST_FAIL, ["IDEMPOTENTS_ONLY_0_1"],
     {"components": ("KA", "KB", "KC")}, None,
     "emitting a product decomposition, which this packet forbids"),
    ("M_IDEMPOTENT_LIST", MUST_FAIL, ["IDEMPOTENTS_ONLY_0_1"],
     {"idempotents": (0, 1, "e1")}, None,
     "a nontrivial primitive idempotent in the emitted list"),
    ("M_DEGREE", MUST_FAIL, ["FIELD_DEGREE_432", "RELATION_LEADING_TERMS"],
     {"basis_rank": 216}, None,
     "dim_Q(B) * |Delta| must equal the declared degree"),
    ("M_SIGMA_R_SIGN", MUST_FAIL, ["GALOIS_STABILITY_FREE"],
     {"sigma_images": ((0, 1), (1, 1), (3, 1), (2, 1), (4, 1))}, None,
     "sigma without the sign on r3 sends A1^3-(3+r3) outside the relation "
     "set.  In R1 this loop computed sigma(0) == 0 and could not fail"),
    ("M_SIGMA_NO_SWAP", MUST_FAIL, ["GALOIS_STABILITY_FREE"],
     {"sigma_images": ((0, 1), (1, -1), (2, 1), (3, 1), (4, 1))}, None,
     "sigma that negates r3 without swapping A1 and A2 is not a ring map of "
     "this presentation"),
    ("M_SIGMA_PERMUTATION", MUST_FAIL, ["GALOIS_STABILITY_FREE"],
     {"sigma_relation_permutation": (0, 1, 2, 3, 4)}, None,
     "the declared relation permutation is itself pinned"),

    # ---- L4: frames -------------------------------------------------------
    ("M_FRAME_A1", MUST_FAIL, ["FRAME_RELATIONS"],
     {"frames": ((105337, (2779, 795, 50631, 10114, 50267)),
                 (105673, (13862, 14686, 38664, 46664, 35053)))}, None,
     "the report's L4 mutation: A1 50630 -> 50631"),
    ("M_FRAME_SECOND", MUST_FAIL, ["FRAME_RELATIONS"],
     {"frames": ((105337, (2779, 795, 50630, 10114, 50267)),
                 (105673, (13862, 14686, 38664, 46665, 35053)))}, None,
     "coverage gap named by the R1 review: the 105673 frame was never mutated"),
    ("M_FRAME_ZETA_ORDER", MUST_FAIL, ["FRAME_RELATIONS"],
     {"frames": ((105337, (1, 795, 50630, 10114, 50267)),
                 (105673, (13862, 14686, 38664, 46664, 35053)))}, None,
     "zeta42 replaced by 1: Phi42(1) != 0 and the order gate would also fire"),
    ("M_FRAMES_HALVED", MUST_FAIL, ["FRAME_RELATIONS"],
     {"frames": (_BASE_FRAMES[0],)}, None,
     "R1 defect D4, executed: dropping the 105673 frame passed all 36 R1 "
     "gates while the terminal still said 'both registered frames'"),
    ("M_FRAME_PRIME_SET", MUST_FAIL, ["FRAME_RELATIONS"],
     {"registered_primes": (105337, 105337)}, None,
     "the registered prime set is pinned, not inferred from the frame list"),
    ("M_FRAME_P2_SHIFT", MUST_FAIL, ["P2_HENSEL_REPLAY"],
     {"p2_frame": (8852313585, 11012141449, 786496672 + 105337,
                   8038065910, 6003627245)}, None,
     "a second p^2 lift over the same p-frame; etaleness forbids it"),
    ("M_P2_PRIME", MUST_FAIL, ["P2_HENSEL_REPLAY"],
     {"p2_prime": 105673}, None,
     "coverage gap named by the R1 review: the p^2 prime itself"),
    ("M_SPLIT_COUNT", MUST_FAIL, ["SPLIT_COUNT_432"],
     {"split_count": 144}, None,
     "the frame count is a consistency check with a hard registered value"),

    # ---- L5: the E-conditional layer -------------------------------------
    ("M_Q0_COEFFICIENT", MUST_FAIL,
     ["Q0_LITERAL_PIN", "Q0_NORMAL_FORM", "E_DIRECT_SUBSTITUTION"],
     {"q0_terms": _q0_with((0, 0, 2, 1, 0), Fr(-5, 7))}, (True, False),
     "the report's L5 mutation: q0 coefficient -5/6 -> -5/7.  R1 reported "
     "unconditional_k0_theorem FALSE here through the shared census; R2 must "
     "report the unconditional theorem TRUE and only the E theorem FALSE"),
    ("M_Q0_MONOMIAL", MUST_FAIL,
     ["Q0_LITERAL_PIN", "Q0_NORMAL_FORM", "E_DIRECT_SUBSTITUTION"],
     {"q0_terms": tuple(sorted(
         {(0, 0, 2, 1, 0): Fr(-5, 6), (0, 1, 2, 1, 0): Fr(1, 2),
          (7, 0, 1, 2, 0): Fr(2, 3), (7, 1, 2, 1, 0): Fr(-1, 3)}.items()))},
     (True, False),
     "A1^2*A2 -> A1*A2^2 in one term: the u-side of q0 is load-bearing"),
    ("M_E_COEFFICIENT", MUST_FAIL,
     ["E_LITERAL_PIN", "E_DIRECT_SUBSTITUTION"],
     {"e_terms": ((9, 5, 2, 4), (9, 5, 3, 4))}, (True, False),
     "(9-5*r3) -> (9+5*r3): the sign that makes E sigma-symmetric.  R2 also "
     "catches it in the external bridge pin and in the base reduction"),
    ("M_E_EXPONENT", MUST_FAIL,
     ["E_LITERAL_PIN", "E_BASE_REDUCTION", "E_DIRECT_SUBSTITUTION"],
     {"e_terms": ((9, 5, 2, 4), (9, -5, 3, 2))}, (True, False),
     "W2^4 -> W2^2: no longer the displayed fourth-root relation.  Caught "
     "only because the direct substitution is also run at nontrivial scales; "
     "the W2=1 substitution alone is blind to the exponent on W2"),
    ("M_E_DIRECT_DROPPED", MUST_FAIL, ["CENSUS_CONDITIONAL"],
     {"skip_gates": frozenset({"E_DIRECT_SUBSTITUTION"})}, (True, False),
     "the report's tautological-pass hole: keeping only c = -u^10 and "
     "dropping the direct substitution must FAIL the E theorem and leave the "
     "unconditional theorem untouched"),
    ("M_E_SCALES_INSUFFICIENT", MUST_FAIL, ["E_DIRECT_SUBSTITUTION"],
     {"e_substitution_scales": ((1, 0, 0, 0, 0),)}, (True, False),
     "one scale is not two: with a single substitution point the gate could "
     "not see the homogeneity of E on the branch line"),
    ("M_E_SCALES_TRIVIAL", MUST_FAIL, ["E_DIRECT_SUBSTITUTION"],
     {"e_substitution_scales": ((1, 0, 0, 0, 0), (1, 0, 0, 0, 0))},
     (True, False),
     "two copies of the same scale is one scale"),
    ("M_BRANCH_COUNT", MUST_FAIL,
     ["E_BASE_REDUCTION", "FOUR_K0_RATIONAL_BRANCHES"],
     {"branch_count": 3}, (True, False),
     "three branches is not a complete splitting of t^4-c"),
    ("M_POINTBANK_BRANCH_INDEX", MUST_FAIL, ["POINTBANK_REGRESSION"],
     {"pointbank_expected": ((105337, 7210, 2), (105673, 14755, 0))},
     (True, True),
     "branch indices are frame-dependent and are pinned, not inferred.  This "
     "is a CORROBORATION failure: both theorem booleans must stay true and "
     "only all_pass may fall"),
    ("M_POINTBANK_RATIO", MUST_FAIL, ["POINTBANK_REGRESSION"],
     {"pointbank_expected": ((105337, 7211, 3), (105673, 14755, 0))},
     (True, True),
     "the banked ratio is a registered value, not a fitted one"),
    ("M_POINTBANK_HALVED", MUST_FAIL, ["POINTBANK_REGRESSION"],
     {"pointbank_expected": (_BASE_PB[0],)}, (True, True),
     "R1 defect D4, executed: dropping the 105673 regression passed all 36 R1 "
     "gates and had no observable shadow at all"),
    ("M_POINTBANK_PRIME_SET", MUST_FAIL, ["POINTBANK_REGRESSION"],
     {"pointbank_expected": ((105337, 7210, 3), (105337, 7210, 3))},
     (True, True),
     "the pointbank prime set is pinned to the registered primes"),

    # ---- harness self-gates: these must NOT fail --------------------------
    ("M_CLASS_REP_EPS_SQUARED", MUST_SURVIVE, [],
     {"class_representatives": ((1, 0), (0, 1), (1, 1), (2, 1))}, (True, True),
     "the charged report's own surviving mutation: eps -> eps^2 = 7+4*sqrt3 "
     "is still a non-cube and still covers all eight classes, so the "
     "certificate must PASS.  A battery that reports this as a failure is "
     "miscoded."),
    ("M_CLASS_GENERATOR_BASIS", MUST_SURVIVE, [],
     {"class_generators": ((1, 0), (1, 1))}, (True, True),
     "generators (alpha1, alpha1*alpha2) are a different basis of the same "
     "Delta; independence is basis-free, so the certificate must PASS."),
    ("M_CERT_PRIME_ORDER", MUST_SURVIVE, [],
     {"character_primes": (1009, 673)}, (True, True),
     "the certificate primes are a set, not a sequence."),
    ("M_CLASS_REP_ALL_INVERSE", MUST_SURVIVE, [],
     {"class_representatives": ((2, 0), (0, 2), (2, 2), (2, 1))}, (True, True),
     "the inverse of a complete representative set is a complete "
     "representative set."),
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
                     pins["emitter_rel"], pins["rows_rel"], pins["bridge_rel"],
                     pins["theorem_report_rel"], None)
    failed = [g["gate"] for g in payload["gates"] if g["status"] != "PASS"]
    return {"mutated_pin": key, "intended_gate": "SRC_FILE_HASHES",
            "failed_gates": failed,
            "verdict": "PASS" if "SRC_FILE_HASHES" in failed else "FAIL"}


def gate_unit_sigma_free_versus_quotient():
    """Executable demonstration of the R1 defect D3 and of its repair.

    In the quotient every relation is already 0, so ``sigma(relation) == 0``
    holds for *every* sigma table, including tables that are not ring maps of
    the presentation.  In the free ring the same table is rejected.  The unit
    test asserts both halves: the R1 shape passes on a broken sigma, the R2
    shape does not.
    """
    spec = CK.Spec()
    broken = ((0, 1), (1, 1), (3, 1), (2, 1), (4, 1))     # no sign on r3
    alg = KA.K0Algebra(spec.phi42, spec.alpha_data, spec.r_square,
                       Fr(spec.h_relation[1], spec.h_relation[0]))
    z, r, a1, a2, h = (alg.gen(i) for i in range(5))
    (a1c, a1r), (a2c, a2r) = spec.alpha_data
    quotient_values = [
        alg.add(*[alg.scal(alg.pw(z, j), spec.phi42[j]) for j in range(13)]),
        alg.sub(alg.pw(r, 2), alg.const(spec.r_square)),
        alg.sub(alg.pw(a1, 3), alg.add(alg.const(a1c), alg.scal(r, a1r))),
        alg.sub(alg.pw(a2, 3), alg.add(alg.const(a2c), alg.scal(r, a2r))),
        alg.sub(alg.scal(alg.pw(h, 2), spec.h_relation[0]),
                alg.const(spec.h_relation[1])),
    ]
    r1_shape_accepts = all(alg.sigma(v, broken) == {} for v in quotient_values)
    free_rels = alg.free_relations()
    images = alg.sigma_images(broken)
    r2_shape_accepts = all(
        any(KA.fp_substitute(rel, images) == other for other in free_rels)
        for rel in free_rels)
    return {"broken_sigma": [list(t) for t in broken],
            "r1_quotient_shape_accepts": r1_shape_accepts,
            "r2_free_ring_shape_accepts": r2_shape_accepts,
            "verdict": "PASS" if (r1_shape_accepts and not r2_shape_accepts)
                       else "FAIL"}


def gate_unit_leading_term_criterion():
    """A non-coprime leading pair must break the Buchberger first criterion."""
    good = [(12, 0, 0, 0, 0), (0, 2, 0, 0, 0), (0, 0, 3, 0, 0),
            (0, 0, 0, 3, 0), (0, 0, 0, 0, 2)]
    bad = good[:4] + [(0, 0, 1, 0, 2)]

    def pairwise(ms):
        return all(KA.mono_coprime(ms[a], ms[b])
                   for a in range(len(ms)) for b in range(a + 1, len(ms)))

    return {"good_set_pairwise_coprime": pairwise(good),
            "bad_set_pairwise_coprime": pairwise(bad),
            "verdict": "PASS" if (pairwise(good) and not pairwise(bad))
                       else "FAIL"}


def gate_unit_corroboration_separation(root, pins, pointbanks):
    """Skipping the corroboration gate must not move either theorem boolean."""
    spec = replace(CK.Spec(label="M_CORROBORATION_SKIPPED"),
                   skip_gates=frozenset({"POINTBANK_REGRESSION"}))
    payload = CK.run_from_pins(spec, root, pins, pointbanks)
    ok = (payload["unconditional_k0_theorem"] is True
          and payload["e_conditional_ratio_theorem"] is True
          and payload["all_pass"] is False
          and payload["corroboration_ok"] is False)
    return {"unconditional_k0_theorem": payload["unconditional_k0_theorem"],
            "e_conditional_ratio_theorem":
                payload["e_conditional_ratio_theorem"],
            "corroboration_ok": payload["corroboration_ok"],
            "all_pass": payload["all_pass"],
            "verdict": "PASS" if ok else "FAIL"}


def run_battery(root, pins, pointbanks):
    baseline = CK.run_from_pins(CK.Spec(label="BASELINE"), root, pins,
                                pointbanks)
    entries = []
    ok = baseline["all_pass"]
    if not ok:
        entries.append({"mutation": "BASELINE", "kind": "BASELINE",
                        "verdict": "FAIL",
                        "detail": "the unmutated certificate does not pass"})
    separation = {"uncond_true_e_false": 0, "both_true": 0, "uncond_false": 0}
    for name, kind, intended, overrides, expect, note in MUTATIONS:
        spec = replace(CK.Spec(label=name), **overrides)
        payload = CK.run_from_pins(spec, root, pins, pointbanks)
        failed = [g["gate"] for g in payload["gates"] if g["status"] != "PASS"]
        got = (payload["unconditional_k0_theorem"],
               payload["e_conditional_ratio_theorem"])
        if got == (True, False):
            separation["uncond_true_e_false"] += 1
        elif got == (True, True):
            separation["both_true"] += 1
        elif got[0] is False:
            separation["uncond_false"] += 1
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
        if expect is not None and got != tuple(expect):
            verdict = "FAIL"
            reason = ("theorem separation control: reported %s, required %s"
                      % (list(got), list(expect)))
        errors = {g["gate"]: g.get("error") for g in payload["gates"]
                  if g["status"] == "FAIL"}
        entries.append({"mutation": name, "kind": kind, "note": note,
                        "intended_gates": intended, "failed_gates": failed,
                        "gate_errors": errors,
                        "unconditional_k0_theorem": got[0],
                        "e_conditional_ratio_theorem": got[1],
                        "expected_theorems":
                            None if expect is None else list(expect),
                        "corroboration_ok": payload["corroboration_ok"],
                        "all_pass": payload["all_pass"],
                        "verdict": verdict, "reason": reason})
        ok = ok and verdict == "PASS"
    units = {"GATE_UNIT_ORDER42": gate_unit_order42(),
             "GATE_UNIT_SOURCE_HASH": gate_unit_source_hash(root, pins),
             "GATE_UNIT_SIGMA_FREE_VS_QUOTIENT":
                 gate_unit_sigma_free_versus_quotient(),
             "GATE_UNIT_LEADING_TERM_CRITERION":
                 gate_unit_leading_term_criterion(),
             "GATE_UNIT_CORROBORATION_SEPARATION":
                 gate_unit_corroboration_separation(root, pins, pointbanks)}
    ok = ok and all(u["verdict"] == "PASS" for u in units.values())
    survive = [e for e in entries if e.get("kind") == MUST_SURVIVE]
    ok = ok and len(survive) >= 2 and all(e["verdict"] == "PASS"
                                          for e in survive)
    # the D1 controls are only meaningful if both separation classes occur
    ok = ok and separation["uncond_true_e_false"] >= 1
    ok = ok and separation["both_true"] >= 1
    payload = {
        "schema": SCHEMA,
        "baseline_all_pass": baseline["all_pass"],
        "baseline_census_sha256": baseline["census_sha256"],
        "mutation_count": len(MUTATIONS),
        "must_fail_count": sum(1 for m in MUTATIONS if m[1] == MUST_FAIL),
        "must_survive_count": sum(1 for m in MUTATIONS if m[1] == MUST_SURVIVE),
        "theorem_separation_controls": sum(1 for m in MUTATIONS
                                           if m[4] is not None),
        "theorem_separation_census": separation,
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
        items = []
        for item in args.pointbank:
            prime, path, sha = item.split(":", 2)
            items.append((int(prime), path, sha))
        banks = CK.read_pointbanks(items)
    payload = run_battery(args.root, pins, banks)
    blob = CK.canonical(payload)
    if args.out == "-":
        sys.stdout.write(blob.decode("ascii") + "\n")
    else:
        Path(args.out).write_bytes(blob)
    return 0 if payload["battery_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
