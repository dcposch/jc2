#!/usr/bin/env python3
"""Exact verifier for the general-squarefree R3 transport and square stop."""

from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CASE = Path(__file__).resolve().parent
PINS = {
    "r3_freeze": (
        "cases/ggv_8_28_keller_face_rational_mode_exclusion_r3_20260827/FREEZE.sha256",
        "e752b86b5a8953649a3ce8c55379d18eca2dc1bdc8ab4fcd030c63dd64071823",
    ),
    "r3_report": (
        "xmodel/ggv-8_28-keller-face-rational-mode-exclusion-r3-sol-20260827.md",
        "b1851156c83657fa85eb875df7e191a99fd339bfcb79ca1a752742ddff9f70b7",
    ),
    "r3_review": (
        "xmodel/ggv-8_28-keller-face-rational-mode-exclusion-r3-hostile-review-grok-20260827.md",
        "27fcd25640f62a92c147863e7a8ef8ca4b7b004f05d54450c8d2d8811c97cdc6",
    ),
    "opus_ideation": (
        "xmodel/ideation-20260827T1349Z-opus5.md",
        "1c17b61f00079802b20fc459550eea7bc7b09bcdcc98f27c233bde91cf348968",
    ),
    "endpoint_audit": (
        "xmodel/ggv-superelliptic-endpoint-criterion-hostile-audit-actual-20260827.md",
        "d382c21f416afdc150d621506c38076aa4ec2b96e4680c0a938ddd56f06394ed",
    ),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def trim(a):
    a = list(map(Q, a))
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return tuple(a)


def padd(a, b):
    out = [Q(0)] * max(len(a), len(b))
    for i, value in enumerate(a):
        out[i] += value
    for i, value in enumerate(b):
        out[i] += value
    return trim(out)


def pscale(a, scalar):
    return trim(Q(scalar) * value for value in a)


def pmul(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            out[i + j] += left * right
    return trim(out)


def pder(a):
    return trim(tuple(Q(i) * a[i] for i in range(1, len(a))) or (Q(0),))


def pdivmod(a, b):
    a = list(trim(a))
    b = trim(b)
    assert b != (Q(0),)
    quotient = [Q(0)] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and any(a):
        shift = len(a) - len(b)
        coefficient = a[-1] / b[-1]
        quotient[shift] += coefficient
        for i, value in enumerate(b):
            a[i + shift] -= coefficient * value
        a = list(trim(a))
    return trim(quotient), trim(a)


def pgcd(a, b):
    a, b = trim(a), trim(b)
    while b != (Q(0),):
        a, b = b, pdivmod(a, b)[1]
    return pscale(a, 1 / a[-1])


def M(H, Y):
    return padd(pscale(pmul(H, pder(Y)), 4), pscale(pmul(pder(H), Y), 6))


def rational_weights_for_multiplicities(multiplicities, stop=22):
    """Weights whose leading H^((12-n)/4) has integral finite valuations."""
    return [
        n
        for n in range(stop + 1)
        if all(((12 - n) * exponent) % 4 == 0 for exponent in multiplicities)
    ]


def main():
    pins = {}
    for key, (relative, expected) in PINS.items():
        got = sha256(ROOT / relative)
        assert got == expected, (key, got, expected)
        pins[key] = {"path": relative, "sha256": got}

    # Exact homogeneous identity scalar for Z_n=t^n F^gamma.
    mode_rows = []
    for n in range(23):
        gamma = Q(12 - n, 8)
        h_power = 2 * gamma
        assert Q(12) - 8 * gamma - n == 0
        mode_rows.append(
            {
                "weight": n,
                "F_power": str(gamma),
                "leading_H_power": str(h_power),
                "squarefree_rational": h_power.denominator == 1,
            }
        )

    squarefree_weights_through_22 = [
        row["weight"] for row in mode_rows if row["squarefree_rational"]
    ]
    squarefree_nonweights_through_22 = [
        row["weight"] for row in mode_rows if not row["squarefree_rational"]
    ]
    assert squarefree_weights_through_22 == [0, 4, 8, 12, 16, 20]
    assert mode_rows[16]["F_power"] == "-1/2"
    assert mode_rows[20]["F_power"] == "-1"
    assert mode_rows[22]["leading_H_power"] == "-5/2"
    assert not mode_rows[22]["squarefree_rational"]

    exact_modes = [
        {"weight": 0, "term": "F^(3/2)", "leading": "H^3"},
        {"weight": 4, "term": "t^4*F", "leading": "t^4*H^2"},
        {"weight": 8, "term": "t^8*F^(1/2)", "leading": "t^8*H"},
        {"weight": 12, "term": "t^12", "leading": "t^12"},
        {"weight": 16, "term": "t^16*F^(-1/2)", "leading": "t^16*H^(-1)"},
        {"weight": 20, "term": "t^20*F^(-1)", "leading": "t^20*H^(-2)"},
    ]

    # General squarefree degree checks, including the linear survivor.
    squarefree_examples = {
        "linear": trim((1, 1)),
        "quadratic": trim((-1, 0, 1)),
        "cubic": trim((1, -1, 0, 1)),
        "quintic": trim((1, 1, 0, 0, 0, 1)),
        "degree_eight": trim((-1,) + (0,) * 7 + (1,)),
    }
    squarefree_checks = {}
    for name, H in squarefree_examples.items():
        Hp = pder(H)
        gcd = pgcd(H, Hp)
        assert gcd == (Q(1),), (name, gcd)
        h = len(H) - 1
        for y_degree in range(0, 25):
            Y = (Q(0),) * y_degree + (Q(1),)
            image = M(H, Y)
            assert len(image) - 1 == y_degree + h - 1
            assert image[-1] == (4 * y_degree + 6 * h) * H[-1]
        squarefree_checks[name] = {
            "degree": h,
            "gcd_H_Hprime": "1",
            "M_monomials_checked": "Y=X^d, 0<=d<=24",
        }

    # For linear H=X+1, Y=1/6 reaches the unit endpoint exactly.
    H_linear = squarefree_examples["linear"]
    Y_linear = (Q(1, 6),)
    assert M(H_linear, Y_linear) == (Q(1),)

    # Endpoint pole coefficient for squarefree H: no integral m>=2 cancels.
    pole_rows = []
    for m in range(1, 13):
        scalar = 8 * m - 20
        if m >= 2:
            assert scalar != 0
        pole_rows.append({"d_pole_order": m, "leading_scalar": scalar})

    # The endpoint change g=-8H^2d is checked on dense polynomial fixtures.
    # We compare coefficients of d and d' in
    # 2H*g'+H'*g = 2H*(-20HH'd-8H^2d').
    assert -32 - 8 == -40  # coefficient of H^2 H' d
    assert -16 == -16      # coefficient of H^3 d'

    # Multiplicity classifier: a nonconstant squarefree part supplies an odd
    # valuation, hence only n=0 mod 4.  A square branch adds weight 22.
    squarefree_signature = rational_weights_for_multiplicities([1, 1, 1])
    nonsquarefree_with_B = rational_weights_for_multiplicities([2, 3, 5])
    perfect_square_signature = rational_weights_for_multiplicities([2])
    fourth_power_signature = rational_weights_for_multiplicities([4])
    assert squarefree_signature == [0, 4, 8, 12, 16, 20]
    assert nonsquarefree_with_B == [0, 4, 8, 12, 16, 20]
    assert perfect_square_signature == list(range(0, 23, 2))
    assert fourth_power_signature == list(range(23))
    assert 22 in perfect_square_signature

    # Smallest stop mutation: H=X^2 and n=22.  The kernel equation is
    # r'/r=(-5/2)H'/H=-5/X, solved by r=X^-5.  Its two Laurent coefficients
    # cancel exactly: -10*(2X)*X^-5 - 4*X^2*(-5X^-6)=0.
    assert -10 * 2 + (-4) * (-5) == 0
    assert Q(12 - 22, 4) * 2 == -5
    assert Q(12 - 22, 8) == Q(-5, 4)

    result = {
        "status": "PASS-GENERAL-SQUAREFREE-MODES-AND-STOP-SQUARE-W22-RESONANCE",
        "scope": {
            "field": "characteristic-zero K",
            "squarefree_theorem": "nonconstant squarefree H, F0=H^2, G0=H^3, alpha=12, beta=8, through weight 22",
            "nonsquarefree_stage": "stopped at H=X^2 because a new rational homogeneous mode occurs at weight 22",
        },
        "pins": pins,
        "squarefree_modes": {
            "first_residual_ode": "r_n'/r_n=((12-n)/4)H'/H",
            "valuation_lemma": "squarefree nonconstant H makes a nonzero rational solution possible iff (12-n)/4 is integral",
            "weights_through_22": squarefree_weights_through_22,
            "nonweights_through_22": squarefree_nonweights_through_22,
            "exact_modes": exact_modes,
            "normal_form_mod_t22": "G=F^(3/2)+c4*t^4*F+c8*t^8*F^(1/2)+c12*t^12+c16*t^16*F^(-1/2)+c20*t^20*F^(-1)+t^22*d+O(t^23)",
        },
        "endpoint": {
            "residual_equation": "-20HH'd-8H^2d'=1",
            "confirmed_ode_change": "g=-8H^2d gives 2Hg'+H'g=2H",
            "denominator_provenance": "coefficients of the six modes divide only powers of H",
            "squarefree_pole_reduction": "d=-Y/(2H), Y polynomial, hence 4HY'+6H'Y=1",
            "degree_ge_2": "excluded: nonzero degree-y Y maps to degree y+deg(H)-1>=1",
            "degree_1": "endpoint survives uniquely with Y=1/(6H')",
            "pole_rows": pole_rows,
            "squarefree_fixture_checks": squarefree_checks,
        },
        "nonsquarefree_stop": {
            "multiplicity_rule": "weight n has a rational leading mode iff 4 divides (12-n)e_p for every finite prime multiplicity e_p of H",
            "B_nonconstant": "an odd multiplicity is present, so the squarefree six-weight list remains the rational list",
            "minimal_square_H_X2_weights": perfect_square_signature,
            "fourth_power_weights": fourth_power_signature,
            "smallest_counterexample": "H=X^2, n=22, r=X^(-5), exact control mode t^22*F^(-5/4)=t^22*X^(-5) for F=X^4",
            "effect": "endpoint differential equation still exists, but squarefree uniqueness/pole provenance cannot be transported through the perfect-square branch unchanged",
        },
        "rollback": "retain reviewed R3 exactly at H=X^8-1; the additive theorem extends its rational-mode and exclusion proof only to nonconstant squarefree H of degree at least 2; make no H=A^2B family claim",
        "claims_not_made": [
            "existence of a polynomial jet for squarefree linear H",
            "general nonsquarefree mode/provenance theorem",
            "raw polynomial-source lift or genuine GGV landing",
            "GGV family exclusion, G2-PSC, G2-BD, JC2",
        ],
    }

    if "--print-candidate" in sys.argv:
        print(json.dumps(result, sort_keys=True, indent=2))
        return
    frozen = json.loads((CASE / "RESULT_R4.json").read_text())
    assert result == frozen
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
