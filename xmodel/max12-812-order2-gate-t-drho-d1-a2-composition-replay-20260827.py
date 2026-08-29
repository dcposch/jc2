#!/usr/bin/env python3
"""Desk replay for the narrow Gate-T D(rho) / D1 a=2 composition.

This is intentionally not a polynomial exporter and does no Groebner-basis
work.  It checks frozen custody, the actual-total grade-16 construction path,
the two-grade support window, both deck allocations, the decisive residue,
and the quotient-versus-cover negative control from the accompanying report.
"""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

KRB_REPORT = ROOT / "xmodel/max12-812-order2-gate-t-kummer-row-bridge-discriminator-sol-20260827.md"
KRB_REPLAY = ROOT / "xmodel/max12-812-order2-gate-t-kummer-row-bridge-replay-20260827.py"
V28 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g16_v28_20260827/prolong_boundary_g16_v28.py"
V28_FREEZE = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g16_v28_20260827/FREEZE.sha256"
V28_Q_RESULT = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g16_v28_20260827/aws_q/RESULT.json"
D1_COMPILER = ROOT / "cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_20260826/compile_r1_d1_ac.py"
D1_RESULT = ROOT / "cases/max12_812_order2_square_owner_d1_finite_band_a2_a5_fullsupport_20260826/RESULT.md"
D1_FREEZE = ROOT / "cases/max12_812_order2_square_owner_d1_finite_band_a2_a5_fullsupport_20260826/FREEZE.sha256"
D1_EVIDENCE = ROOT / "cases/max12_812_order2_square_owner_d1_finite_band_a2_a5_fullsupport_20260826/EVIDENCE.sha256"
D1_REVIEW = ROOT / "xmodel/max12-812-order2-square-d1-finite-band-a2-a5-hostile-review-grok-20260826.md"
D1_PROMOTION = ROOT / "xmodel/max12-812-order2-square-d1-finite-band-a2-a5-promotion-20260826.md"
FAN = ROOT / "xmodel/max12-812-order2-square-fan-lower-hull-reduction-20260826.md"

PINS = {
    KRB_REPORT: "1b583d5a58ae3c26edd2f394e85e2540871ccfd996ec0bc798b84235c564361a",
    KRB_REPLAY: "f11b24a3447a0602ef5b55891e156b6f179e62179eb8394fd30f4455adf29af5",
    V28: "6c76dc541d27b436a289f1decccd6e90c1424b3a586685e128331c8490b06480",
    V28_FREEZE: "8e54871ffc1555e392eb3f0dc7c84d5dac3685ebb139d98c64b666974775c937",
    V28_Q_RESULT: "c9f89344b4fc92e3ed1deade74a3cbd6301a5d45d9178aa3096f52aa6714b293",
    D1_COMPILER: "e024a13d24a11519f70b535d4b47c47c62538a684b8bc71e79216410cd8ecb7c",
    D1_RESULT: "17c3baa20232dad9dd1356c8e903a863a44480344d81d8aa587216414aad0a61",
    D1_FREEZE: "9c53eecf7aa3a1fbc75012d9566a2d564e7a39da7e9011c6d5fd63cd53431920",
    D1_EVIDENCE: "49264a8d6ae24724ee1005dfac9b4602946f2f3b7a77c0512df237369470f254",
    D1_REVIEW: "e03de4e1fc1816a7141c6bb8060b4a75c2a6b5a08ea4d56ca63582b875cad335",
    D1_PROMOTION: "973f7953d42fdd994d9c7da8ea70fceffc2e8da9002b33f38ea1a17c6922d6d1",
    FAN: "c9ecfe4000092912464e29ecc526ac5c065f950778d31cac81f58fe06622954d",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def custody_check() -> dict[str, str]:
    actual = {str(path.relative_to(ROOT)): digest(path) for path in PINS}
    for path, expected in PINS.items():
        key = str(path.relative_to(ROOT))
        if actual[key] != expected:
            raise AssertionError(("custody mismatch", key, actual[key], expected))
    return actual


def construction_path_check() -> dict[str, object]:
    """Check the hash-pinned code path, without claiming rho!=0 row bytes."""

    v28 = V28.read_text()
    d1 = D1_COMPILER.read_text()
    required_v28 = {
        "kummer_constant": 'p[0] = base.poly_scale(-2, base.poly_mul(base.poly_var("rho"), base.poly_var("rho")))',
        "moving_p_jets": 'p[degree] = base.poly_scale(2, base.poly_var(f"ell{degree}"))',
        "c_shift_two": "c = base.series_shift(c0, 2)",
        "r_quarter": "r = base.series_scale(Fraction(1, 4), base.series_add(base.series_mul(p, p), base.series_shift(r0, 2)))",
        "n3_shift_three": "n3 = base.series_shift(az, 3)",
        "n2_shift_three": "n2 = base.series_shift(ac, 3)",
        "k10_shift_four": "loads = {7: base.series_shift(k10, 4), 8: base.series_shift(k6, 12), 9: base.series_shift(k2, 20)}",
        "degree_sixteen": "base.MAX_DEGREE = 16",
        "seven_total_rows": 'totals = {row: build_row(base, tails[str(row)], row, coefficients, loads) for row in ROWS}',
        "grade16_before_face": "face = {row: parser.specialize(totals[row][16], killed, {}) for row in ROWS}",
    }
    required_d1 = {
        "moving_p": 'pp = "(p+2*sigma*ell1)"',
        "a_order_two": 'az = "(sigma^2*theta*(a1+sigma*aa1))"',
        "c_order_three": 'cz = "(sigma^3*theta*(c1+sigma*cc1))"',
        "r_order_two": 'rz = "(sigma^2*theta*eta*b1)"',
        "grades_15_16": 'extraction(lines, "D1AC_", base, tails, coeffs, loads, 15, 16)',
        "both_orientations": "D1AC_BOTH_ROOT_ORIENTATIONS",
        "unmatched_residue": "D1AC_UNMATCHED_DOUBLE_POLE",
    }
    sentinels = {
        "V28_" + name: snippet in v28 for name, snippet in required_v28.items()
    } | {
        "D1_" + name: snippet in d1 for name, snippet in required_d1.items()
    }
    if not all(sentinels.values()):
        raise AssertionError(("construction-path sentinel", sentinels))

    result = json.loads(V28_Q_RESULT.read_text())
    expected_counts = {
        "Tg16_1": 63,
        "Tg16_2": 86,
        "Tg16_3": 98,
        "Tg16_4": 45,
        "Tg16_5": 77,
        "Tg16_6": 22,
        "Tg16_7": 33,
    }
    if result.get("status") != "PASS-A1-BOUNDARY-PROLONG-G16-V28":
        raise AssertionError(("V28 status", result.get("status")))
    if result.get("grade16_term_counts") != expected_counts:
        raise AssertionError(("V28 grade16 counts", result.get("grade16_term_counts")))
    return {
        "sentinels": sentinels,
        "V28_exact_Q_status": result["status"],
        "V28_rho0_face_term_counts": expected_counts,
        "scope": (
            "V28 executes the universal grade-16 construction before its rho=0 face; "
            "its serialized rows remain rho=0. General-rho equality is the formal "
            "source identity in the KRB report, not a claim about V28 output bytes."
        ),
    }


def support_window_check() -> dict[str, object]:
    a = 2
    g = 11 + 2 * a
    orders = {
        "AC/L": 11 + 2 * a,
        "C2/L2": 12 + 2 * a,
        "RA2/L2_lower_bound": 12 + 3 * a,
        "A3/L3": 15 + 3 * a,
        "k10_R3/L_lower_bound": 10 + 3 * a,
        "k10_RC/L_lower_bound": 12 + 2 * a,
        "k10_R2A/L2_lower_bound": 13 + 3 * a,
        "k10_A2/L": 14 + 2 * a,
        "k6_C/L": 18 + a,
        "k2_R/L_lower_bound": 22 + a,
        "mu2": 28,
        "mu4": 32,
        "mu6": 36,
        "J/4": 38,
    }
    if (g, g + 1) != (15, 16):
        raise AssertionError(("grade window", g))
    in_window = {name for name, order in orders.items() if order <= g + 1}
    expected = {"AC/L", "C2/L2", "k10_R3/L_lower_bound", "k10_RC/L_lower_bound"}
    if in_window != expected:
        raise AssertionError(("support window", in_window, expected))
    # The moving lower-unitriangular transform has offsets zero and one only;
    # ell2 belongs to its offset-two coefficient and cannot enter this window.
    return {
        "contact": {"ord_A": 2, "ord_C": 3, "ord_R": ">=2"},
        "grades": [15, 16],
        "orders": orders,
        "in_window": sorted(in_window),
        "ell2_or_higher_connection_in_window": False,
        "later_R_jet_needed": False,
    }


def mul_linear(left: tuple[Fraction, Fraction], right: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction, Fraction]:
    return (
        left[0] * right[0],
        left[0] * right[1] + left[1] * right[0],
        left[1] * right[1],
    )


def deck_allocation_check() -> dict[str, object]:
    samples = [
        (Fraction(1), Fraction(2), Fraction(3)),
        (Fraction(-2), Fraction(5, 3), Fraction(-7, 4)),
        (Fraction(3, 2), Fraction(-4), Fraction(9, 5)),
    ]
    checked = []
    for rho, au, cv in samples:
        # Coefficient order is constant,z.  L=z^2-rho^2 because p=-2 rho^2.
        L = (-rho * rho, Fraction(0), Fraction(1))
        pos = mul_linear((-au * rho, au), (cv * rho, cv))
        neg = mul_linear((au * rho, au), (-cv * rho, cv))
        wanted = tuple(au * cv * coefficient for coefficient in L)
        if pos != wanted or neg != wanted:
            raise AssertionError(("root allocation", rho, au, cv, pos, neg, wanted))
        residue = Fraction(3, 2) * rho * rho * cv * cv
        if residue == 0:
            raise AssertionError(("residue vanished on registered open", rho, cv))
        checked.append({
            "rho": str(rho),
            "au": str(au),
            "cv": str(cv),
            "AC_equals_au_cv_L_both_decks": True,
            "residue": str(residue),
        })
    return {
        "p_substitution": "p=-2*rho^2",
        "localizer_identity": "D(p*k)=D(rho*k) in characteristic zero",
        "shifted_total_root_pairs": {
            "R0": ["rs2/4+rho*cs2", "rs2/4-rho*cs2"],
            "C0": ["(ec3+rho*ez3)/2", "(ec3-rho*ez3)/2"],
            "A0": ["aaa0+rho*aaa1", "aaa0-rho*aaa1"],
        },
        "stage_zero_pairs_on_this_contact": "all zero; they are not the D1 leading forms",
        "positive_allocation": "A=au*(z-rho), C=cv*(z+rho)",
        "negative_allocation": "A=au*(z+rho), C=cv*(z-rho)",
        "deck_swaps_allocations": True,
        "decisive_residue": "(3/2)*rho^2*cv^2",
        "samples": checked,
    }


def coverage_negative_control() -> dict[str, object]:
    """An invariant empty quotient client need not cover its ambient open."""

    # A=Q[rho,u], tau(rho)=-rho, tau(u)=u.  I=(u-1).  The contact
    # specialization q:A->A/(u) sends I to (-1)=(1), while the ambient
    # D(rho) point rho=1,u=1 lies on V(I).
    q_of_generator = Fraction(-1)
    ambient_point = {"rho": Fraction(1), "u": Fraction(1)}
    generator_at_point = ambient_point["u"] - 1
    if q_of_generator == 0 or generator_at_point != 0:
        raise AssertionError("coverage negative control collapsed")
    return {
        "ring": "Q[rho,u]",
        "deck": "rho |-> -rho, u fixed",
        "ambient_ideal": "(u-1)",
        "contact_quotient": "q: u |-> 0",
        "quotient_ideal": "(1)",
        "ambient_Drho_point": {"rho": "1", "u": "1"},
        "ambient_nonempty": True,
        "conclusion": "deck-equivariant quotient emptiness is not source coverage",
    }


def main() -> None:
    payload = {
        "status": "PASS-GATE-T-DRHO-D1-A2-COMPOSITION-DESK-REPLAY",
        "scope": (
            "ONE_ACTUAL-TOTAL_FINITE-JET CONTACT ON D(rho*k) AFTER THE REVIEWED "
            "GENERIC-SQUARE GATES; NO rho=0, FAN-COVERAGE, G2-PSC, G2-BD, GATE-T, "
            "ORDER-TWO, MAXIMUM-TWELVE, OR JC2 VERDICT"
        ),
        "frozen_sha256": custody_check(),
        "actual_total_grade16_path": construction_path_check(),
        "two_grade_support": support_window_check(),
        "root_and_residue": deck_allocation_check(),
        "coverage_negative_control": coverage_negative_control(),
        "outcome": {
            "local_contact": "PASS: a=2,c=3,r>=2 excluded on D(rho*k)",
            "global_Drho_cover": "INCOMPLETE: other fan cells and zero-normal receiver remain",
            "ramified_fibre": "UNTOUCHED: root-coordinate inverse is unavailable at rho=0",
        },
    }
    print(json.dumps(payload, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
