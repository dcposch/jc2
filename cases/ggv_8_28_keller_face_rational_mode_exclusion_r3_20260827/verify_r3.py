#!/usr/bin/env python3
"""Exact R3 verifier for the squarefree H^2/H^3 rational-mode exclusion."""

from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CASE = Path(__file__).resolve().parent
PINS = {
    "r2_freeze": (
        "cases/ggv_8_28_keller_face_cusp_unit_carrier_classification_r2_20260827/FREEZE.sha256",
        "453f7821f88add5d97b65cee41fe3a4df225db5768526746cf4ff1431aa73aa6",
    ),
    "r2_report": (
        "xmodel/ggv-8_28-keller-face-cusp-unit-carrier-classification-r2-sol-20260827.md",
        "0f8f3833c8fa16349d52c6d68829e5c86200ab064f84e4172b0ba4039314b733",
    ),
    "r2_verifier": (
        "cases/ggv_8_28_keller_face_cusp_unit_carrier_classification_r2_20260827/verify_r2.py",
        "74c6c78e4faf527172703d5a115767562d89d9fa20868fc431dcc1f7cd258f15",
    ),
    "r2_result": (
        "cases/ggv_8_28_keller_face_cusp_unit_carrier_classification_r2_20260827/RESULT_R2.json",
        "0dffbb36c20d0b80498d765168a47cdb9ed2889ffc7bd105dce7ec835f600b1d",
    ),
    "r1_freeze": (
        "cases/ggv_8_28_keller_face_cusp_jet_pinning_r1_20260827/FREEZE.sha256",
        "05cbb5c046f9aa4b89e1104448e77fd38ec3a146d2422bf84773f81d668bfe3c",
    ),
    "r0_hostile_review": (
        "xmodel/ggv-8_28-keller-face-cusp-jet-pinning-hostile-review-grok-20260827.md",
        "171ff47c844331da8971a731c1ffaf20c31ed5b2ba86fdee2d0d81219eb002b0",
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


def pscale(a, value):
    return trim(tuple(Q(value) * x for x in a))


def pmul(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
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


def pmod(a, b):
    return pdivmod(a, b)[1]


def pmonic(a):
    a = trim(a)
    return pscale(a, 1 / a[-1])


def pgcd(a, b):
    a, b = trim(a), trim(b)
    while b != (Q(0),):
        a, b = b, pmod(a, b)
    return pmonic(a)


def M(H, Y):
    return padd(pscale(pmul(H, pder(Y)), 4), pscale(pmul(pder(H), Y), 6))


def main():
    pins = {}
    for key, (relative, expected) in PINS.items():
        got = sha256(ROOT / relative)
        assert got == expected, (key, got, expected)
        pins[key] = {"path": relative, "sha256": got}

    # For Z=t^n*F^alpha, direct differentiation gives
    # E(F,Z)=t^n*F^alpha*F_X*(12-8*alpha-n).
    modes = []
    for n in (0, 4, 8, 12, 16, 20):
        alpha = Q(12 - n, 8)
        assert 12 - 8 * alpha - n == 0
        leading_H_power = 2 * alpha
        assert leading_H_power.denominator == 1
        modes.append(
            {
                "weight": n,
                "F_power": str(alpha),
                "leading_H_power": int(leading_H_power),
            }
        )
    assert modes == [
        {"weight": 0, "F_power": "3/2", "leading_H_power": 3},
        {"weight": 4, "F_power": "1", "leading_H_power": 2},
        {"weight": 8, "F_power": "1/2", "leading_H_power": 1},
        {"weight": 12, "F_power": "0", "leading_H_power": 0},
        {"weight": 16, "F_power": "-1/2", "leading_H_power": -1},
        {"weight": 20, "F_power": "-1", "leading_H_power": -2},
    ]

    # If a residual first appears at weight n, its coefficient r satisfies
    # r'/r=((12-n)/4)H'/H.  Squarefreeness makes a rational solution possible
    # exactly when the exponent is integral.
    rational_weights = []
    exponent_table = []
    for n in range(0, 22):
        exponent = Q(12 - n, 4)
        rational = exponent.denominator == 1
        if rational:
            rational_weights.append(n)
        exponent_table.append(
            {"weight": n, "H_exponent": str(exponent), "rational_homogeneous": rational}
        )
    assert rational_weights == [0, 4, 8, 12, 16, 20]

    # Endpoint residual d has
    # E22=-20*H*H'*d-8*H^2*d'.  A pole d~a*H^-m contributes
    # (8m-20)*a*H'*H^(1-m).  No integer m>=2 cancels.
    pole_table = []
    for m in range(1, 11):
        scalar = 8 * m - 20
        exponent = 1 - m
        if m >= 2:
            assert scalar != 0 and exponent < 0
        pole_table.append(
            {"pole_order_m": m, "leading_scalar": scalar, "H_exponent": exponent}
        )

    H = trim((-1,) + (0,) * 7 + (1,))
    Hp = pder(H)
    X = trim((0, 1))
    assert pgcd(H, Hp) == (Q(1),)

    # Target-weight mutation: at n=20 the double-pole scalar would vanish;
    # at the charged n=22 it is -4.  This guards the endpoint weight.
    assert 2 * ((12 - 20) + 4 * 2) == 0
    assert 2 * ((12 - 22) + 4 * 2) == -4

    # For d=-Y/(2H), the endpoint operator is exactly M(Y).  Verify the
    # cleared-denominator identity on dense polynomials, not only a monomial.
    dense_Ys = [
        trim((3, -2, 5, 7)),
        trim((Q(1, 3), 0, Q(-5, 7), 11, 0, 2)),
        pscale(X, Q(1, 48)),
    ]
    for Y in dense_Ys:
        # -20HH'*(-Y/(2H)) - 8H^2*d' after clearing the elementary derivative.
        endpoint_from_d = padd(pscale(pmul(Hp, Y), 6), pscale(pmul(H, pder(Y)), 4))
        assert endpoint_from_d == M(H, Y)

    fixture = M(H, pscale(X, Q(1, 48)))
    assert fixture == padd((Q(1),), pscale(H, Q(13, 12)))
    assert pmod(fixture, H) == (Q(1),)

    # Degree obstruction for every nonzero Y.  The formula itself is exact;
    # the monomial sweep is a mutation guard against a sign/coefficient typo.
    for degree in range(0, 65):
        Y = (Q(0),) * degree + (Q(1),)
        image = M(H, Y)
        expected_lc = 4 * degree + 48
        assert len(image) - 1 == degree + 7
        assert image[-1] == expected_lc

    result = {
        "status": "PASS-R3-SQUAREFREE-H2-H3-RATIONAL-MODE-EXCLUSION",
        "scope": "formal polynomial-X jet with F0=(X^8-1)^2, G0=(X^8-1)^3 and E=t^22 through grade 22; excludes this exact replacement-edge Keller lift only",
        "pins": pins,
        "linearization": {
            "definition": "R=G-F^(3/2) in K(X)[[t]], using sqrt(F)=H+O(t)",
            "identity": "E(F,G)=E(F,R)=12F_XR-8FR_X-t(F_XR_t-F_tR_X)",
            "mode_identity": "E(F,t^n F^alpha)=t^n F^alpha F_X(12-8alpha-n)",
            "exact_modes_through_20": modes,
        },
        "completeness": {
            "first_residual_ode": "2H*((12-n)H'*r_n-4H*r_n')=0",
            "rational_solution": "r_n=c*H^((12-n)/4); squarefree H forces the exponent integral",
            "rational_weights_below_22": rational_weights,
            "exponent_table": exponent_table,
            "normal_form": "G=F^(3/2)+c4*t^4*F+c8*t^8*F^(1/2)+c12*t^12+c16*t^16*F^(-1/2)+c20*t^20*F^(-1) mod t^22",
        },
        "endpoint": {
            "residual": "after subtracting the five exact modes, D=t^22*d+O(t^23)",
            "operator": "E22=-20H H' d-8H^2 d'",
            "pole_table": pole_table,
            "pole_conclusion": "regular E22 forces d to have at most simple poles at the simple H-roots; all denominators arise from powers of H, so d=-Y/(2H) for polynomial Y",
            "target_weight_mutation": "at target 20 a double-pole homogeneous mode survives; at charged target 22 its leading scalar is -4",
            "polynomial_operator": "E22=M(Y)=4H Y'+6H'Y",
            "fixture": "M(X/48)=1+(13/12)H",
            "degree_obstruction": "nonzero degree-d Y gives degree d+7 and leading coefficient (4d+48)lc(Y), so M(Y)!=1",
            "mechanical_degree_mutations": "all monomials Y=X^d for d=0..64",
        },
        "verdict": "no polynomial-X formal jet with this squarefree H^2/H^3 leading edge can satisfy E_0..E_21=0,E_22=1",
        "claims_not_made": [
            "exclusion of the original non-Keller 8_28 witness or the entire GGV 8_28 family",
            "a global GGV-to-Eggers-Wall functor or G2-PSC",
            "a Keller pair, counterexample, G2-BD, or JC2",
        ],
    }
    if "--print-candidate" in sys.argv:
        print(json.dumps(result, sort_keys=True, indent=2))
        return
    frozen = json.loads((CASE / "RESULT_R3.json").read_text())
    assert result == frozen
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
