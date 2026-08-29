#!/usr/bin/env python3
"""Exact R1 verifier: raw support types and the bounded E22 image obstruction."""

from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CASE = Path(__file__).resolve().parent
PINS = {
    "r0_freeze": (
        "cases/ggv_8_28_keller_face_cusp_jet_pinning_20260827/FREEZE.sha256",
        "6928428f9cc46641a80275e2bbfa62e784c4290ff041f5089ae789507fa8804f",
    ),
    "r0_report": (
        "xmodel/ggv-8_28-keller-face-cusp-jet-pinning-sol-20260827.md",
        "3e4e608d32c44b1b0208bd5472257ba1dbe4cadf4ef5efb2ace49d3d47d756be",
    ),
    "r0_verifier": (
        "cases/ggv_8_28_keller_face_cusp_jet_pinning_20260827/verify.py",
        "ef9acfa90935b32e244367dada67ab35d6454f431f6d43dc35d144b3d08fe46c",
    ),
    "r0_result": (
        "cases/ggv_8_28_keller_face_cusp_jet_pinning_20260827/RESULT.json",
        "46e1b3434badcea007a914ec71bf60d9758ee76d312dc00d252342d52beed76d",
    ),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return tuple(a)


def add(a, b):
    out = [Q(0)] * max(len(a), len(b))
    for i, c in enumerate(a):
        out[i] += c
    for i, c in enumerate(b):
        out[i] += c
    return trim(out)


def scale(a, c):
    return trim([Q(c) * x for x in a])


def mul(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def der(a):
    return trim([Q(i) * a[i] for i in range(1, len(a))] or [Q(0)])


def M(H, Y):
    return add(scale(mul(H, der(Y)), 4), scale(mul(der(H), Y), 6))


def ceil_div(a, b):
    return -((-a) // b)


def slice_2S(n):
    lo = max(0, ceil_div(n - 8, 3))
    hi = 16 - n
    return list(range(lo, hi + 1)) if lo <= hi else []


def slice_3S(n):
    lo = max(0, ceil_div(n - 12, 3))
    hi = 24 - n
    return list(range(lo, hi + 1)) if lo <= hi else []


def xy_from_F(n, i):
    return (i, 8 + 3 * i - n)


def xy_from_G(n, i):
    return (i, 12 + 3 * i - n)


def main():
    pins = {}
    for key, (rel, expected) in PINS.items():
        got = sha256(ROOT / rel)
        assert got == expected, (key, got, expected)
        pins[key] = {"path": rel, "sha256": got}

    # Exact raw polygon slices, derived from
    # 0<=j, 4i-8<=j<=3i+8 (2S) and
    # 0<=j, 4i-12<=j<=3i+12 (3S).
    F_slices = {str(n): slice_2S(n) for n in range(8, 15)}
    G_tail = {str(n): slice_3S(n) for n in range(18, 23)}
    assert F_slices["14"] == [2]
    assert xy_from_F(14, 2) == (2, 0)
    assert xy_from_F(14, 1) == (1, -3)
    assert G_tail["21"] == [3]
    assert G_tail["22"] == []

    H = trim([Q(-1)] + [Q(0)] * 7 + [Q(1)])
    X = (Q(0), Q(1))
    Y_fixture = scale(X, Q(1, 48))
    fixture = M(H, Y_fixture)
    expected = add((Q(1),), scale(H, Q(13, 12)))
    assert fixture == expected

    # There is no polynomial solution of M(Y)=1.  For a nonzero degree-d Y,
    # its leading coefficient becomes (4d+48)*lc(Y) at degree d+7.
    for d in range(0, 65):
        Y = (Q(0),) * d + (Q(1),)
        out = M(H, Y)
        assert len(out) - 1 == d + 7
        assert out[-1] == 4 * d + 48

    # Case A: the E8/E14 solutions are
    # F8=P, G8=(3/2)HP+C H and F14=A, G14=(3/2)HA.
    # The entire E22 cross term is M(A*((3/2)P+C)).  Verify on a dense exact
    # pair rather than only on the rootwise fixture.
    P = (Q(2), Q(-3), Q(5))
    A = (Q(-7), Q(11), Q(13), Q(-2))
    C = Q(17, 5)
    Y_case_a = mul(A, add(scale(P, Q(3, 2)), (C,)))
    case_a_direct = add(
        add(
            scale(mul(H, der(mul(P, A))), 6),
            scale(mul(der(H), mul(P, A)), 9),
        ),
        add(scale(mul(H, der(A)), 4 * C), scale(mul(der(H), A), 6 * C)),
    )
    assert case_a_direct == M(H, Y_case_a)

    # Case B: a first nonresonant U11=A has E22=M((3/4)A^2).
    Y_case_b = scale(mul(A, A), Q(3, 4))
    case_b_direct = add(scale(mul(H, mul(A, der(A))), 6), scale(mul(der(H), mul(A, A)), Q(9, 2)))
    assert case_b_direct == M(H, Y_case_b)

    result = {
        "status": "PASS-R1-BOUNDED-TYPE-REPAIR-AND-E22-IMAGE-OBSTRUCTION",
        "scope": "raw 2S/3S slice typing plus two normalized unit-carrier ansatzes; typed-normal-form completeness remains open",
        "pins": pins,
        "raw_slices": {
            "F_formula": "i in [max(0,ceil((n-8)/3)),16-n], j=8+3i-n",
            "G_formula": "i in [max(0,ceil((n-12)/3)),24-n], j=12+3i-n",
            "F_n_8_through_14": F_slices,
            "G_n_18_through_22": G_tail,
            "F14": "only X^2, pulling back to x^2; local U14=X would pull back to x*y^-3",
            "G22": "empty raw 3S slice",
        },
        "operator": {
            "M": "M(Y)=4H*Y'+6H'*Y",
            "H": "X^8-1",
            "fixture_Y": "X/48",
            "fixture_M_Y": "1+(13/12)H",
            "degree_obstruction": "nonzero deg-d Y has deg M(Y)=d+7 and leading coefficient (4d+48)lc(Y), so M(Y)=1 has no polynomial solution in characteristic zero",
            "mechanical_leading_check": "all monomials Y=X^d for d=0..64",
        },
        "unit_carrier_cases": {
            "V8_U14": "E22=M(A*((3/2)P+C)) for F8=P,G8=(3/2)HP+CH,F14=A,G14=(3/2)HA",
            "U11_self": "E22=M((3/4)A^2) for F11=A,G11=(3/2)HA",
            "verdict": "neither ansatz can produce global E22=1 with polynomial higher-u data",
        },
        "typed_status": {
            "local_fixture": "valid modulo H / at every simple H-root",
            "raw_polynomial_source": "not established; U14=X is not a raw F14 term",
            "completeness_gap": "prove or falsify that every raw 2S/3S jet modulo allowed formal source/target cleanup reduces to the two unit-carrier cases",
        },
        "claims_not_made": [
            "typed-normal-form completeness",
            "exclusion of the full 8_28 family or any GGV family",
            "a Keller pair, counterexample, G2-PSC, G2-BD, or JC2",
        ],
    }
    if "--print-candidate" in sys.argv:
        print(json.dumps(result, sort_keys=True, indent=2))
        return
    frozen = json.loads((CASE / "RESULT_R1.json").read_text())
    assert result == frozen
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
