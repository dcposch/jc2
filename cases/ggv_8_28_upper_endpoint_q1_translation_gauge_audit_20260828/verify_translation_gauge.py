#!/usr/bin/env python3
"""Exact audit of the proposed active-q1 translation gauge."""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RAW = ROOT / "cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json"
RESULT = HERE / "RESULT.json"
RAW_SHA256 = "ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def trim(poly):
    answer = list(poly)
    while answer and not answer[-1]:
        answer.pop()
    return answer


def add(*items):
    answer = []
    for poly in items:
        size = max(len(answer), len(poly))
        answer = trim([
            (answer[index] if index < len(answer) else Q(0))
            + (poly[index] if index < len(poly) else Q(0))
            for index in range(size)
        ])
    return answer


def scale(value, poly):
    return trim([Q(value) * coefficient for coefficient in poly])


def mul(left, right):
    if not left or not right:
        return []
    answer = [Q(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            answer[i + j] += x * y
    return trim(answer)


def power(poly, exponent):
    answer = [Q(1)]
    for _ in range(exponent):
        answer = mul(answer, poly)
    return answer


def derivative(poly, order=1):
    answer = list(poly)
    for _ in range(order):
        answer = trim([Q(index) * answer[index]
                       for index in range(1, len(answer))])
    return answer


def shear_coefficient(coefficients, weight, a):
    """Coefficient of t^weight in P(X-a*t,t)."""
    answer = []
    factorial = 1
    for order in range(weight + 1):
        if order:
            factorial *= order
        source = coefficients.get(weight - order, [])
        answer = add(answer,
                     scale(Q((-a) ** order, factorial),
                           derivative(source, order)))
    return answer


def encode(poly):
    return [str(value) for value in trim(poly)]


def calculate_result():
    assert digest(RAW) == RAW_SHA256
    raw = json.loads(RAW.read_text())
    assert raw["windows"]["F"]["8"]["lower"] == 0
    assert raw["windows"]["F"]["9"]["lower"] == 1
    assert raw["windows"]["G"]["12"]["lower"] == 0
    assert raw["windows"]["G"]["13"]["lower"] == 1

    A = [Q(-1), Q(0), Q(0), Q(0), Q(1)]
    F0 = power(A, 4)
    G0 = power(A, 6)
    lam = Q(4, 3)
    a = Q(3, 4) * lam
    assert a == 1
    V0 = scale(3 * lam, mul(A, derivative(A)))
    F1 = mul(power(A, 2), V0)
    G1 = scale(Q(3, 2), mul(power(A, 2), F1))
    assert F1 == scale(a, derivative(F0))
    assert G1 == scale(a, derivative(G0))
    assert shear_coefficient({0: F0, 1: F1}, 1, a) == []
    assert shear_coefficient({0: G0, 1: G1}, 1, a) == []

    # Literal lower-window counterexamples.  Contributions from F0/F1 have
    # no constant at weight 9, so the allowed F8=X slot leaves -a in F9[X0].
    f_coefficients = {0: F0, 1: F1, 8: [Q(0), Q(1)]}
    transformed_f9 = shear_coefficient(f_coefficients, 9, a)
    assert transformed_f9[0] == -1
    assert raw["windows"]["F"]["9"]["lower"] == 1

    # The same failure occurs independently in G12 -> G13.
    g_coefficients = {0: G0, 1: G1, 12: [Q(0), Q(1)]}
    transformed_g13 = shear_coefficient(g_coefficients, 13, a)
    assert transformed_g13[0] == -1
    assert raw["windows"]["G"]["13"]["lower"] == 1

    # Upper bounds alone are triangularly stable:
    # deg d^k P_{n-k} <= (D-(n-k))-k = D-n.
    for family, top in (("F", 16), ("G", 24)):
        for weight, window in raw["windows"][family].items():
            n = int(weight)
            assert int(window["upper"]) <= top - n

    return {
        "status": "PASS_EXACT_NEGATIVE_TRANSLATION_GAUGE_AUDIT",
        "active_q1": {
            "lambda": str(lam),
            "a=3lambda/4": str(a),
            "V0=3lambda*A*A_prime": encode(V0),
            "F1_equals_a_F0_prime": True,
            "G1_equals_a_G0_prime": True,
            "weight_one_killed_by_X_to_X_minus_a_t": True,
        },
        "formal_equivariance": {
            "operator": "E=F_X*(12-t*d_t)G+((t*d_t)-8)F*G_X",
            "chain_rule": (
                "t*d_t tau_a(P)=tau_a(t*d_t P-a*t*P_X); the two "
                "a*t*F_X*G_X terms cancel, so E(tau_a F,tau_a G)=tau_a E(F,G)"
            ),
            "target_t22_fixed": True,
            "branch_P_F0_G0_fixed": True,
            "upper_degree_bounds_preserved": True,
        },
        "literal_window_counterexamples": {
            "F8_equals_X": {
                "source_window": "F8[X^0..X^8]",
                "transformed_F9": encode(transformed_f9),
                "forbidden_coefficient": "F9[X^0]=-1",
                "target_window": "F9[X^1..X^7]",
            },
            "G12_equals_X": {
                "source_window": "G12[X^0..X^12]",
                "transformed_G13": encode(transformed_g13),
                "forbidden_coefficient": "G13[X^0]=-1",
                "target_window": "G13[X^1..X^11]",
            },
        },
        "verdict": (
            "the formal determinant equation is translation-equivariant, but "
            "the frozen raw Newton-support space is not; lambda cannot be "
            "gauged to zero without an additional solution-locus cancellation theorem"
        ),
        "solution_locus_cancellation": "OPEN_NOT_PROVED",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = calculate_result()
    encoded = json.dumps(result, sort_keys=True, indent=2) + "\n"
    if args.check:
        assert RESULT.read_text() == encoded
    else:
        RESULT.write_text(encoded)
    print(result["status"])


if __name__ == "__main__":
    main()
