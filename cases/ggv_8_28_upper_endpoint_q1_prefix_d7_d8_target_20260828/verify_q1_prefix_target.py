#!/usr/bin/env python3
"""Exact desk compiler for the genuine branch-P prefix at D7/D8.

This is intentionally standard-library only.  It reconstructs fractional
characteristic coefficients from F*y'=e*F'*y and keeps all nine born modes.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RESULT = HERE / "RESULT.json"
TARGET = HERE / "TARGET.json"
CASCADE_REPORT = ROOT / "xmodel/ggv-8_28-upper-cascade-w3-w6-sol-ultra-20260827.md"
Q1_REVIEW = ROOT / "xmodel/ggv-survivor-q1-q2-de-rham-gates-fable5-hostile-review-opus5-20260827.md"
CASCADE_CHECKER = ROOT / "cases/ggv_8_28_upper_cascade_w3_w6_20260827/verify_upper_cascade.py"
CASCADE_RESULT = CASCADE_CHECKER.with_name("RESULT.json")
FIXED_ENDPOINT_CHECKER = ROOT / "cases/ggv_8_28_upper_endpoint_uniform_d18_d22_endpoint_collapse_20260828/verify_uniform_d18_d22.py"
FIXED_ENDPOINT_RESULT = FIXED_ENDPOINT_CHECKER.with_name("RESULT.json")

SOURCE_PINS = {
    CASCADE_REPORT: "6e3d9104effe39c0dd0e34377bb7bdc6ede4f25f472f9f9c0098706aceffb60a",
    Q1_REVIEW: "46736edc8aa391e50d3c6a1604937bcad85361c25c25f9e3b4c184e19f8afed1",
    CASCADE_CHECKER: "ac3197988a3c0eba6b717194696b28f772550b789426087cbcfb3e6feee5ac37",
    CASCADE_RESULT: "54767fceaa1cc6b3feb64d9d07f7af1e2ffd43a725617123e6e6849091b23615",
    FIXED_ENDPOINT_CHECKER: "7f946f549094b44f73d4903bb78d803e9eebb6bef8aa02b6679f1f22f89605c9",
    FIXED_ENDPOINT_RESULT: "486fd15224d144fe5341f20f005eb6b90d5e7c62394369354937f965b728d404",
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def la_term(coefficient=1, a_power=0, *symbols):
    coefficient = Q(coefficient)
    return {(a_power, tuple(sorted(symbols))): coefficient} if coefficient else {}


def la_add(*items):
    answer = {}
    for item in items:
        for key, coefficient in item.items():
            answer[key] = answer.get(key, Q(0)) + coefficient
            if not answer[key]:
                del answer[key]
    return answer


def la_scale(coefficient, item):
    coefficient = Q(coefficient)
    return {key: coefficient * value for key, value in item.items()
            if coefficient * value}


def la_mul(left, right):
    answer = {}
    for (left_a, left_symbols), left_coefficient in left.items():
        for (right_a, right_symbols), right_coefficient in right.items():
            key = (left_a + right_a, tuple(sorted(left_symbols + right_symbols)))
            answer[key] = answer.get(key, Q(0)) + left_coefficient * right_coefficient
            if not answer[key]:
                del answer[key]
    return answer


def la_power(item, exponent):
    answer = la_term(1)
    for _ in range(exponent):
        answer = la_mul(answer, item)
    return answer


def la_shift(a_power, item):
    return {(old_power + a_power, symbols): coefficient
            for (old_power, symbols), coefficient in item.items()}


def la_negative(item):
    return {key: coefficient for key, coefficient in item.items() if key[0] < 0}


def la_substitute(item, substitutions):
    answer = {}
    for (a_power, symbols), coefficient in item.items():
        piece = la_term(coefficient, a_power)
        for symbol in symbols:
            piece = la_mul(piece, substitutions.get(symbol, la_term(1, 0, symbol)))
        answer = la_add(answer, piece)
    return answer


def la_encode(item):
    return [
        {"A_exponent": power, "coefficient": str(coefficient),
         "monomial": list(symbols)}
        for (power, symbols), coefficient in sorted(item.items())
    ]


def la_scalar_value(item, assignments):
    substituted = la_substitute(
        item, {name: la_term(value) for name, value in assignments.items()})
    assert all(a_power == 0 and not symbols
               for a_power, symbols in substituted)
    return sum(substituted.values(), Q(0))


def fractional_coefficients(F, exponent, maximum):
    answer = {0: la_term(1, int(4 * exponent))}
    for weight in range(1, maximum + 1):
        numerator = {}
        for index in range(1, weight + 1):
            factor = (exponent + 1) * index - weight
            numerator = la_add(
                numerator,
                la_scale(factor, la_mul(F[index], answer[weight - index])),
            )
        answer[weight] = la_scale(Q(1, weight), la_shift(-4, numerator))
    return answer


MODES = {
    2: Q(5, 4),
    4: Q(1),
    6: Q(3, 4),
    8: Q(1, 2),
    10: Q(1, 4),
    12: Q(0),
    14: Q(-1, 4),
    16: Q(-1, 2),
    18: Q(-3, 4),
    20: Q(-1),
}


def continuation(F, maximum):
    exponents = set(MODES.values()) | {Q(3, 2)}
    powers = {exponent: fractional_coefficients(F, exponent, maximum)
              for exponent in exponents}
    rows = {}
    for weight in range(maximum + 1):
        row = powers[Q(3, 2)][weight]
        for birth, exponent in MODES.items():
            if birth <= weight:
                row = la_add(
                    row,
                    la_mul(la_term(1, 0, f"c{birth}"),
                           powers[exponent][weight - birth]),
                )
        rows[weight] = row
    return powers, rows


def general_prefix(maximum=8):
    v0 = la_term(1, 0, "v0")
    z = la_term(1, 0, "z")
    t = la_term(1, 0, "t")
    F = {
        0: la_term(1, 4),
        1: la_shift(2, v0),
        2: la_add(la_scale(Q(1, 4), la_mul(v0, v0)),
                  la_scale(Q(1, 4), la_shift(2, z))),
        3: la_add(la_scale(Q(1, 8), la_mul(v0, z)),
                  la_scale(Q(1, 8), la_shift(1, t))),
    }
    for weight in range(4, maximum + 1):
        F[weight] = la_term(1, 0, f"f{weight}")
    return F


def xp_trim(poly):
    answer = list(poly)
    while answer and not answer[-1]:
        answer.pop()
    return answer


def xp_add(*items):
    answer = []
    for poly in items:
        size = max(len(answer), len(poly))
        answer = xp_trim([
            (answer[index] if index < len(answer) else Q(0))
            + (poly[index] if index < len(poly) else Q(0))
            for index in range(size)
        ])
    return answer


def xp_scale(coefficient, poly):
    return xp_trim([Q(coefficient) * value for value in poly])


def xp_mul(left, right):
    if not left or not right:
        return []
    answer = [Q(0)] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            answer[i + j] += left_value * right_value
    return xp_trim(answer)


def xp_power(poly, exponent):
    answer = [Q(1)]
    for _ in range(exponent):
        answer = xp_mul(answer, poly)
    return answer


def xp_derivative(poly):
    return xp_trim([Q(index) * poly[index] for index in range(1, len(poly))])


def xp_divmod(dividend, divisor):
    divisor = xp_trim(divisor)
    assert divisor
    remainder = xp_trim(dividend)
    quotient = [Q(0)] * max(0, len(remainder) - len(divisor) + 1)
    while remainder and len(remainder) >= len(divisor):
        degree = len(remainder) - len(divisor)
        factor = remainder[-1] / divisor[-1]
        quotient[degree] += factor
        subtraction = [Q(0)] * degree + xp_scale(factor, divisor)
        remainder = xp_add(remainder, xp_scale(-1, subtraction))
    return xp_trim(quotient), remainder


def xp_monic(poly):
    poly = xp_trim(poly)
    return xp_scale(1 / poly[-1], poly) if poly else []


def xp_gcd(left, right):
    left, right = xp_trim(left), xp_trim(right)
    while right:
        _, remainder = xp_divmod(left, right)
        left, right = right, remainder
    return xp_monic(left)


def xp_encode(poly):
    return [str(value) for value in xp_trim(poly)]


def la_evaluate_polynomial(item, A, assignments):
    """Evaluate a Laurent expression and require its denominator to cancel."""
    if not item:
        return []
    minimum = min(power for power, _ in item)
    denominator_power = max(0, -minimum)
    numerator = []
    for (a_power, symbols), coefficient in item.items():
        piece = xp_scale(coefficient, xp_power(A, a_power + denominator_power))
        for symbol in symbols:
            piece = xp_mul(piece, assignments.get(symbol, []))
        numerator = xp_add(numerator, piece)
    denominator = xp_power(A, denominator_power)
    quotient, remainder = xp_divmod(numerator, denominator)
    assert not remainder
    return quotient


def la_evaluate_fraction(item, A, assignments):
    """Return a reduced exact numerator/denominator for a Laurent expression."""
    if not item:
        return [], [Q(1)]
    # Remove terms killed by the assignment before choosing the denominator.
    surviving = []
    for (a_power, symbols), coefficient in item.items():
        if all(assignments.get(symbol, [Q(1)]) for symbol in symbols):
            surviving.append(((a_power, symbols), coefficient))
    if not surviving:
        return [], [Q(1)]
    minimum = min(key[0] for key, _ in surviving)
    denominator_power = max(0, -minimum)
    numerator = []
    for (a_power, symbols), coefficient in surviving:
        piece = xp_scale(coefficient, xp_power(A, a_power + denominator_power))
        for symbol in symbols:
            piece = xp_mul(piece, assignments.get(symbol, [Q(1)]))
        numerator = xp_add(numerator, piece)
    denominator = xp_power(A, denominator_power)
    common = xp_gcd(numerator, denominator)
    numerator, remainder = xp_divmod(numerator, common)
    assert not remainder
    denominator, remainder = xp_divmod(denominator, common)
    assert not remainder
    return numerator, denominator


def determinant_rows(F, G, maximum):
    rows = {}
    for weight in range(maximum + 1):
        row = []
        for i in range(weight + 1):
            j = weight - i
            row = xp_add(
                row,
                xp_scale(12 - j, xp_mul(xp_derivative(F[i]), G[j])),
                xp_scale(i - 8, xp_mul(F[i], xp_derivative(G[j]))),
            )
        rows[weight] = row
    return rows


def q1_polynomial_controls():
    """Concrete exact mutations for C=gcd(A,V0)=gcd(A,R0)."""
    A = [Q(-1), Q(0), Q(0), Q(0), Q(1)]
    A_x = xp_derivative(A)
    A2 = xp_mul(A, A)
    fixtures = {
        "generic_C_1": [Q(1)],
        "linear_C_X_minus_1": [Q(-1), Q(1)],
        "quadratic_C_X2_minus_1": [Q(-1), Q(0), Q(1)],
        "active_C_A": A,
    }
    outputs = {}
    for label, R0 in fixtures.items():
        R0_x = xp_derivative(R0)
        V0 = xp_add(xp_mul(A_x, R0), xp_scale(2, xp_mul(A, R0_x)))
        q1_preimage = xp_mul(A2, R0)
        image = xp_add(
            xp_scale(2, xp_mul(A, xp_derivative(q1_preimage))),
            xp_scale(-3, xp_mul(A_x, q1_preimage)),
        )
        assert image == xp_mul(A2, V0)
        C_from_V = xp_gcd(A, V0)
        C_from_R = xp_gcd(A, R0)
        assert C_from_V == C_from_R
        B, remainder = xp_divmod(A, C_from_V)
        assert not remainder
        V1, remainder = xp_divmod(V0, C_from_V)
        assert not remainder
        assert xp_gcd(B, V1) == [Q(1)]
        outputs[label] = {
            "R0": xp_encode(R0),
            "V0=A_prime*R0+2*A*R0_prime": xp_encode(V0),
            "C=gcd(A,V0)=gcd(A,R0)": xp_encode(C_from_V),
            "B=A/C": xp_encode(B),
            "V1=V0/C": xp_encode(V1),
            "q1_preimage_Q=A^2*R0": xp_encode(q1_preimage),
            "T_A(Q)=A^2*V0": True,
        }
    expected_active = xp_scale(3, xp_mul(A, A_x))
    assert [Q(value) for value in outputs["active_C_A"][
        "V0=A_prime*R0+2*A*R0_prime"]] == expected_active
    R0 = fixtures["linear_C_X_minus_1"]
    wrong_v0 = xp_add(xp_mul(A_x, R0),
                       xp_scale(-2, xp_mul(A, xp_derivative(R0))))
    correct_image = xp_mul(A2, xp_add(xp_mul(A_x, R0),
                                      xp_scale(2, xp_mul(A, xp_derivative(R0)))))
    wrong_residual = xp_add(correct_image,
                            xp_scale(-1, xp_mul(A2, wrong_v0)))
    assert wrong_residual
    outputs["mutation_wrong_minus_sign_in_V0"] = {
        "wrong_V0": xp_encode(wrong_v0),
        "nonzero_T_A_A2R0_minus_A2_wrongV0": xp_encode(wrong_residual),
    }
    return outputs


def partial_divisor_survivor(rows):
    """A live q1 fixture with D7/D8 polynomial but A not dividing T."""
    A = [Q(-1), Q(0), Q(0), Q(0), Q(1)]
    R0 = [Q(-1), Q(1)]
    A_x = xp_derivative(A)
    V0 = xp_add(xp_mul(A_x, R0), xp_scale(2, xp_mul(A, xp_derivative(R0))))
    C = xp_gcd(A, V0)
    B, remainder = xp_divmod(A, C)
    assert not remainder
    V1, remainder = xp_divmod(V0, C)
    assert not remainder
    U = [Q(1)]
    T = B
    Z = [Q(9, 2)]
    L = [Q(-6)]
    K = xp_add(xp_scale(4, V1), xp_mul(B, L))
    F4 = xp_scale(Q(1, 64), xp_add(K, xp_mul(Z, Z)))
    assert xp_add(xp_scale(64, F4), xp_scale(-1, xp_mul(Z, Z))) == K

    n7 = xp_mul(T, xp_add(xp_mul(A, K),
                           xp_scale(-2, xp_mul(T, V0))))
    n7_quotient, n7_remainder = xp_divmod(n7, xp_power(A, 2))
    assert not n7_remainder
    delta_numerator = xp_add(xp_mul(A, K),
                             xp_scale(-4, xp_mul(T, V0)))
    n8 = xp_add(
        xp_mul(delta_numerator, delta_numerator),
        xp_scale(-8, xp_mul(xp_power(A, 2),
                            xp_mul(xp_mul(T, T), Z))),
    )
    assert not n8
    _, t_remainder = xp_divmod(T, A)
    assert t_remainder

    coefficient_assignments = {
        "v0": V0,
        "z": Z,
        "t": T,
        "f4": F4,
        **{f"f{weight}": [] for weight in range(5, 10)},
        **{f"c{birth}": [] for birth in MODES},
    }


    G = {weight: la_evaluate_polynomial(rows[weight], A,
                                        coefficient_assignments)
         for weight in range(9)}
    A2 = xp_power(A, 2)
    F = {
        0: xp_power(A, 4),
        1: xp_mul(A2, V0),
        2: xp_scale(Q(1, 4), xp_add(xp_mul(V0, V0), xp_mul(A2, Z))),
        3: xp_scale(Q(1, 8), xp_add(xp_mul(V0, Z), xp_mul(A, T))),
        4: F4,
        **{weight: [] for weight in range(5, 9)},
    }
    direct = determinant_rows(F, G, 8)
    assert all(not direct[weight] for weight in range(9))
    assert all(len(F[weight]) - 1 <= 16 - weight for weight in range(1, 9))
    assert all(len(G[weight]) - 1 <= 24 - weight for weight in range(1, 9))
    literal_slots = {}
    for family, coefficients in (("F", F), ("G", G)):
        for weight in range(1, 9):
            window_degree = (16 if family == "F" else 24) - weight
            assert len(coefficients[weight]) <= window_degree + 1
            for degree in range(window_degree + 1):
                value = (coefficients[weight][degree]
                         if degree < len(coefficients[weight]) else Q(0))
                if value:
                    literal_slots[f"{family}{weight}[X^{degree}]"] = str(value)
    literal_slots_sha = hashlib.sha256(json.dumps(
        literal_slots, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

    # Live mutations.  Removing the complementary factor B from T breaks D7;
    # changing the tuned Z while keeping K fixed breaks D8.  These catch the
    # root split and the coefficients 2, 4, and 8 in the compact numerators.
    bad_T = [Q(1)]
    bad_n7 = xp_mul(bad_T, xp_add(xp_mul(A, K),
                                   xp_scale(-2, xp_mul(bad_T, V0))))
    _, bad_n7_remainder = xp_divmod(bad_n7, xp_power(A, 2))
    assert bad_n7_remainder
    bad_Z = xp_add(Z, [Q(1)])
    bad_delta = delta_numerator  # K is held fixed by changing F4 with Z.
    bad_n8 = xp_add(
        xp_mul(bad_delta, bad_delta),
        xp_scale(-8, xp_mul(xp_power(A, 2),
                            xp_mul(xp_mul(T, T), bad_Z))),
    )
    _, bad_n8_remainder = xp_divmod(bad_n8, xp_power(A, 4))
    assert bad_n8_remainder

    # D9 first residual.  F5=F6=0 is the displayed frozen point; F9 is a
    # same-row gauge.  Every same-row correction has image in (A^3), so a
    # nonzero mixed remainder modulo A^3 kills this point independently of F9/G9.
    F9 = dict(F)
    F9[9] = []
    G9 = dict(G)
    G9[9] = []
    mixed9 = determinant_rows(F9, G9, 9)[9]
    mixed9_quotient, mixed9_remainder = xp_divmod(mixed9, xp_power(A, 3))
    assert mixed9_remainder

    # L9(R)=-4*A^3*T_A(R), with exact degree typing for every raw R9 monomial.
    A3 = xp_power(A, 3)
    operator_mutation_residual = None
    for degree in range(16):
        R9 = [Q(0)] * degree + [Q(1)]
        left = xp_add(
            xp_scale(12, xp_mul(xp_mul(A3, xp_derivative(A)), R9)),
            xp_scale(-8, xp_mul(xp_power(A, 4), xp_derivative(R9))),
        )
        t_a = xp_add(
            xp_scale(2, xp_mul(A, xp_derivative(R9))),
            xp_scale(-3, xp_mul(xp_derivative(A), R9)),
        )
        assert left == xp_scale(-4, xp_mul(A3, t_a))
        if degree == 0:
            wrong_sign = xp_add(
                xp_scale(2, xp_mul(A, xp_derivative(R9))),
                xp_scale(3, xp_mul(xp_derivative(A), R9)),
            )
            operator_mutation_residual = xp_add(left,
                                                 xp_scale(4, xp_mul(A3, wrong_sign)))
            assert operator_mutation_residual

    # The characteristic D9 fraction is recorded independently.  Its reduced
    # denominator C^3*B^2 makes the nontrivial root support explicit.
    rows9 = continuation(general_prefix(9), 9)[1]
    d9_numerator, d9_denominator = la_evaluate_fraction(
        rows9[9], A, coefficient_assignments)
    assert d9_denominator == xp_mul(xp_power(C, 3), xp_power(B, 2))
    assert d9_numerator
    return {
        "A": xp_encode(A),
        "R0": xp_encode(R0),
        "V0": xp_encode(V0),
        "C": xp_encode(C),
        "B": xp_encode(B),
        "U": xp_encode(U),
        "T=B*U": xp_encode(T),
        "A_does_not_divide_T": True,
        "Z": xp_encode(Z),
        "K": xp_encode(K),
        "F4": xp_encode(F4),
        "F5_through_F8": "zero",
        "all_modes_c2_through_c20": "zero",
        "D7_numerator_over_A2": xp_encode(n7_quotient),
        "D8_numerator": xp_encode(n8),
        "G7": xp_encode(G[7]),
        "G8": xp_encode(G[8]),
        "F_degrees_1_through_8": [len(F[weight]) - 1 for weight in range(1, 9)],
        "G_degrees_1_through_8": [len(G[weight]) - 1 for weight in range(1, 9)],
        "literal_nonzero_raw_slots_F1_through_G8": literal_slots,
        "literal_nonzero_raw_slot_count": len(literal_slots),
        "literal_nonzero_raw_slots_sha256": literal_slots_sha,
        "literal_window_dimensions": {
            str(weight): {"F": 17 - weight, "G": 25 - weight}
            for weight in range(1, 9)
        },
        "direct_D0_through_D8": [xp_encode(direct[weight]) for weight in range(9)],
        "live_mutations": {
            "drop_complementary_B_from_T_D7_remainder_mod_A2": xp_encode(
                bad_n7_remainder),
            "shift_Z_by_1_with_K_fixed_D8_remainder_mod_A4": xp_encode(
                bad_n8_remainder),
            "wrong_sign_T_A_operator_residual": xp_encode(
                operator_mutation_residual),
        },
        "D9_first_residual": {
            "mixed_row": xp_encode(mixed9),
            "mixed_quotient_on_division_by_A3": xp_encode(mixed9_quotient),
            "mixed_nonzero_remainder_mod_A3": xp_encode(mixed9_remainder),
            "characteristic_reduced_numerator": xp_encode(d9_numerator),
            "characteristic_reduced_denominator": xp_encode(d9_denominator),
            "denominator_factorization": "C^3*B^2",
            "same_row_identity": "L9(R9)=-4*A^3*T_A(R9)",
            "typing": (
                "deg R9<=15; T_A maps K[X]_{<=15} to K[X]_{<=18}; "
                "this is not the q1 primitive's deg<=12 domain"
            ),
            "verdict_for_frozen_point": (
                "killed at D9 before the T_A image test because the mixed row "
                "is not divisible by A^3"
            ),
        },
        "conclusion": (
            "exact q1-compatible nontrivial-root stratum survives D8 with "
            "T not divisible by A; this displayed point is then killed at D9, "
            "so the full divisor-stratum D9 target remains the honest successor"
        ),
    }


def replace_a_by_cb(item):
    answer = {}
    for (a_power, symbols), coefficient in item.items():
        assert a_power >= 0
        factors = symbols + ("C", "B") * a_power
        answer = la_add(answer, la_term(coefficient, 0, *factors))
    return answer


def d9_repair_theorem(rows9):
    """Exact symbolic proof that D9 repairs every D7 T-divisibility escape."""
    one = lambda name: la_term(1, 0, name)
    C, B, u, v, z, k, f5, f6 = map(
        one, ("C", "B", "u", "v", "z", "k", "f5", "f6"))
    d = la_add(k, la_scale(-4, la_mul(u, v)))

    # Reconstruct N9 from the complete recurrence, then perform the divisor
    # substitution rather than trusting a hand-factored target.
    actual_polar = la_negative(la_substitute(rows9[9], {"c2": {}, "c6": {}}))
    n9_from_recurrence = la_scale(65536, la_shift(6, actual_polar))
    n9_cb = replace_a_by_cb(n9_from_recurrence)
    n9_cb = la_substitute(n9_cb, {
        "v0": la_mul(C, v),
        "t": la_mul(B, u),
        "f4": la_scale(Q(1, 64), la_add(k, la_mul(z, z))),
    })
    p9 = la_add(
        la_scale(-3, la_mul(v, la_mul(d, d))),
        la_scale(-12, la_mul(la_mul(la_power(B, 2), u), la_mul(z, d))),
        la_scale(-8, la_mul(la_power(B, 4), la_power(u, 3))),
        la_scale(768, la_mul(la_mul(C, la_power(B, 2)), la_mul(f5, d))),
        la_scale(6144, la_mul(la_mul(la_power(C, 2), la_power(B, 4)),
                              la_mul(f6, u))),
    )
    expected_n9_cb = la_mul(la_mul(la_power(C, 3), la_power(B, 2)), p9)
    assert n9_cb == expected_n9_cb

    # On a C-root with u nonzero, D7 gives k=2uv, hence d=-2uv;
    # D8 gives 2B^2 z=v^2.  P9 then has the exact reduction -8B^4u^3.
    p9_mod_c = la_substitute(p9, {"C": {}})
    p9_d7_branch = la_substitute(p9_mod_c, {"k": la_scale(2, la_mul(u, v))})
    h8 = la_add(la_scale(2, la_mul(la_power(B, 2), z)),
                la_scale(-1, la_mul(v, v)))
    expected_branch = la_add(
        la_scale(12, la_mul(la_mul(la_power(u, 2), v), h8)),
        la_scale(-8, la_mul(la_power(B, 4), la_power(u, 3))),
    )
    assert p9_d7_branch == expected_branch
    load_bearing_cubic = la_scale(-8, la_mul(la_power(B, 4), la_power(u, 3)))
    proper_scalar = la_scalar_value(p9, {
        "C": 0, "B": 1, "u": 1, "v": 1, "z": Q(1, 2),
        "k": 2, "f5": 0, "f6": 0,
    })
    assert proper_scalar == -8
    assert la_scalar_value(la_add(p9, la_scale(-1, load_bearing_cubic)), {
        "C": 0, "B": 1, "u": 1, "v": 1, "z": Q(1, 2),
        "k": 2, "f5": 0, "f6": 0,
    }) == 0

    # Active component V0=A*S.  Extract the literal leading A^-3 class from
    # the complete row; every c2/F5/F6 contribution begins at A^-2 or above.
    active = la_negative(la_substitute(rows9[9], {"v0": la_term(1, 1, "s")}))
    active_leading = la_shift(3, {
        key: coefficient for key, coefficient in active.items() if key[0] == -3
    })
    s, t = one("s"), one("t")
    active_k_form = la_scale(Q(1, 65536), la_add(
        la_scale(-3, la_mul(s, la_power(k, 2))),
        la_scale(12, la_mul(la_mul(t, k),
                            la_add(la_scale(2, la_power(s, 2)), la_scale(-1, z)))),
        la_scale(-48, la_mul(la_mul(s, la_power(t, 2)),
                             la_add(la_power(s, 2), la_scale(-1, z)))),
        la_scale(-8, la_power(t, 3)),
    ))
    active_from_literal = la_substitute(
        active_leading,
        {"f4": la_scale(Q(1, 64), la_add(k, la_power(z, 2)))},
    )
    assert active_from_literal == active_k_form
    j = one("j")
    active_j_form = la_substitute(
        active_k_form, {"k": la_add(j, la_scale(2, la_mul(t, s)))})
    expected_j_form = la_scale(Q(1, 65536), la_add(
        la_scale(-3, la_mul(s, la_power(j, 2))),
        la_scale(12, la_mul(la_mul(t, j),
                            la_add(la_power(s, 2), la_scale(-1, z)))),
        la_scale(-12, la_mul(la_mul(s, la_power(t, 2)),
                             la_add(la_power(s, 2), la_scale(-2, z)))),
        la_scale(-8, la_power(t, 3)),
    ))
    assert active_j_form == expected_j_form
    active_d7_branch = la_substitute(active_j_form, {"j": {}})
    h_active = la_add(la_power(s, 2), la_scale(-2, z))
    expected_active_branch = la_scale(Q(1, 65536), la_add(
        la_scale(-12, la_mul(la_mul(s, la_power(t, 2)), h_active)),
        la_scale(-8, la_power(t, 3)),
    ))
    assert active_d7_branch == expected_active_branch
    active_scalar = la_scalar_value(active_d7_branch, {
        "s": 1, "t": 1, "z": Q(1, 2),
    })
    assert active_scalar == Q(-1, 8192)

    return {
        "proper_divisor_factorization": (
            "N9=C^3*B^2*P9, P9=-3*V1*D^2-12*B^2*U*Z*D-8*B^4*U^3"
            "+768*C*B^2*F5*D+6144*C^2*B^4*F6*U, D=K-4*U*V1"
        ),
        "proper_divisor_factorization_sha256": hashlib.sha256(json.dumps(
            la_encode(n9_cb), sort_keys=True,
            separators=(",", ":")).encode()).hexdigest(),
        "proper_C_root_reduction": (
            "on U!=0, D7 and D8 give D=-2*U*V1 and 2*B^2*Z=V1^2; "
            "then P9=-8*B^4*U^3"
        ),
        "proper_C_root_load_bearing_cubic": la_encode(load_bearing_cubic),
        "active_A_minus_3_literal": la_encode(active_leading),
        "active_compact_K_form": (
            "(-3*S*K^2+12*T*K*(2*S^2-Z)-48*S*T^2*(S^2-Z)-8*T^3)/65536"
        ),
        "active_J_form": (
            "(-3*S*J^2+12*T*J*(S^2-Z)-12*S*T^2*(S^2-2Z)-8*T^3)/65536"
        ),
        "active_root_reduction": (
            "on T!=0, D7 gives J=0 and D8 gives S^2=2Z; "
            "the leading D9 class is -8*T^3/65536"
        ),
        "active_leading_contains_no_c2_F5_F6": True,
        "conclusion": (
            "at every field point on the full q1-compatible branch cover, "
            "D1..D9 force A|T"
        ),
        "mutation_firewall": (
            "dropping the -8 cubic makes both root reductions vanish; its "
            "coefficient and sign are load-bearing"
        ),
        "proper_scalar_mutation": {
            "B=U=V1=1_Z=1/2_K=2": str(proper_scalar),
            "after_dropping_minus_8_cubic": "0",
        },
        "active_scalar_mutation": {
            "S=T=1_Z=1/2_J=0": str(active_scalar),
            "after_dropping_minus_8_cubic": "0",
        },
    }


def target_payload():
    return {
        "format": "GGV_BRANCH_P_Q1_D7_D9_DIVISOR_REPAIR_TARGET_V2",
        "field": "characteristic_zero; field-point/radical semantics only",
        "formal_data": {
            "A": "monic squarefree degree 4",
            "R0": "degree <=4",
            "V0": "A'*R0+2*A*R0'",
            "Z": "degree <=6",
            "T": "degree <=9",
            "F4": "degree <=12",
            "F5": "degree <=11",
            "K": "64*F4-Z^2",
            "characteristic_modes": {
                str(birth): str(exponent) for birth, exponent in MODES.items()
            },
            "raw_windows_retained": {
                f"weight_{weight}": {
                    "F_degree": f"0..{16-weight}",
                    "G_degree": f"0..{24-weight}",
                }
                for weight in range(4, 9)
            },
            "regular_window_firewall": (
                "F6,F7,F8 and all regular pieces of G7,G8 remain present/free; "
                "they do not occur in the polar divisibility target"
            ),
        },
        "branch_cover": {
            "c2_zero": {
                "condition": "c2=0",
                "D7_exact": "A^2 divides T*(A*K-2*T*V0)",
                "D8_exact": (
                    "A^4 divides (A*K-4*T*V0)^2-8*A^2*T^2*Z"
                    "+1024*A^3*(c6*V0^2+F5*T)"
                ),
            },
            "c2_active": {
                "condition": "A divides V0 and c2 remains arbitrary",
                "q1_reduction": "R0=lambda*A and V0=3*lambda*A*A'",
                "write": "V0=A*S (on q1, S=3*lambda*A')",
                "D7_exact": "A divides T*(K-2*T*S)",
                "D8_exact": (
                    "A^2 divides 6*((K-4*T*S)^2-8*T^2*Z)"
                    "+A*(5*c2*P8+6144*F5*T)"
                ),
                "P8": (
                    "-(S^2-2*Z)^3-8*(S^2-2*Z)*(K-2*T*S)+32*T^2"
                ),
                "note": "c6 is regular here and is not killed at D8",
            },
        },
        "q1_divisor_strata_for_c2_zero": {
            "definitions": (
                "C=gcd(A,V0)=gcd(A,R0), A=C*B, V0=C*V1, T=B*U; "
                "gcd(B,V1)=1"
            ),
            "D7_exact": "C divides U*(K-2*U*V1)",
            "D8_exact": (
                "A^2 divides (K-4*U*V1)^2-8*B^2*U^2*Z"
                "+1024*A*(c6*C^2*V1^2+F5*B*U)"
            ),
            "D9_exact_after_c6_zero": "A^6 divides N9",
            "D9_scope": (
                "This displayed N9 is the c2=0/B-nonconstant numerator. "
                "The active component is handled separately by its literal "
                "A^-3 leading class below."
            ),
            "N9": (
                "-48*T^2*V0^3+1536*A*F4*T*V0^2-24*A*T*V0^2*Z^2"
                "-12288*A^2*F4^2*V0+384*A^2*F4*V0*Z^2"
                "+48*A^2*T^2*V0*Z-3*A^2*V0*Z^4-768*A^3*F4*T*Z"
                "-8*A^3*T^3+12*A^3*T*Z^3"
                "+768*A^3*F5*(A*K-4*T*V0)+6144*A^5*F6*T"
            ),
            "root_core_mod_C": [
                "U*(K-2*U*V1)=0",
                "(K-4*U*V1)^2-8*B^2*U^2*Z=0",
            ],
            "root_core_mod_B": [
                "K-4*U*V1=0",
                "if B is nonconstant then c6=0 after the square defect is lifted",
            ],
            "generic_C_1_successor": (
                "T=A*U; D8 gives K-4*U*V0=64*A*W and c6=0; "
                "D9 then has leading -3*V0*W^2/(16*A^2), so A divides W"
            ),
        },
        "D9_divisor_repair_theorem": {
            "proper_C_c2_zero": (
                "N9=C^3*B^2*P9. At a C-root, U!=0 plus D7/D8 gives "
                "P9=-8*B^4*U^3, contradicting D9; hence C|U and A|T."
            ),
            "active_C_A": (
                "With V0=A*S and J=K-2*T*S, the leading A^-3 numerator is "
                "-3*S*J^2+12*T*J*(S^2-Z)-12*S*T^2*(S^2-2Z)-8*T^3. "
                "If T!=0, D7/D8 set J=0 and S^2=2Z, leaving -8*T^3."
            ),
            "conclusion": "D1..D9 force A divides T on every q1/c2 branch",
        },
        "post_repair_smallest_target": {
            "write": (
                "T=A*U0 and Delta4=F4-V0*U0/16-Z^2/64=A*W (the D8 lift)"
            ),
            "c2_zero_D9_exact": (
                "A^2 divides W*(-16*V0*W+A*(64*F5-U0*Z))"
            ),
            "root_shape": (
                "V0=C*V1 forces B|W, but the C-root part remains; this is "
                "the next gauge-invariant square-defect stratification"
            ),
            "active_c2_note": (
                "retain c2 and c6; the active post-repair D9 lower-pole block "
                "must be compiled separately before any D22 transport"
            ),
        },
        "promotion_firewall": (
            "This target is the first changed local block, not an endpoint proof, "
            "not an existence result, and not a license to reuse the V0=1 raw fixture."
        ),
        "first_successor": (
            "Continue the post-repair square defect W rootwise, with the active "
            "c2 lower-pole block retained; do not jump directly to D22."
        ),
        "q1_licensing_firewall": (
            "The q1 locus is a prioritized restriction. The reviewed q1 theorem "
            "requires the D23 licensing row and is not implied by D1..D22 alone."
        ),
    }


def calculate_result(debug=False):
    for path, expected in SOURCE_PINS.items():
        assert digest(path) == expected
    F = general_prefix(8)
    _, g = continuation(F, 8)
    c2_zero = {"c2": {}}
    g7 = la_substitute(g[7], c2_zero)
    expected_g7_negative = la_add(
        la_term(Q(3, 32), -1, "f4", "t"),
        la_term(Q(-3, 2048), -1, "t", "z", "z"),
        la_term(Q(-3, 1024), -2, "t", "t", "v0"),
    )
    assert la_negative(g7) == expected_g7_negative

    f4 = la_term(1, 0, "f4")
    f5 = la_term(1, 0, "f5")
    v0 = la_term(1, 0, "v0")
    z = la_term(1, 0, "z")
    t = la_term(1, 0, "t")
    k = la_add(la_scale(64, f4), la_scale(-1, la_mul(z, z)))
    compact_g7 = la_scale(
        Q(3, 2048),
        la_shift(-2, la_mul(t, la_add(la_shift(1, k),
                                      la_scale(-2, la_mul(t, v0))))),
    )
    assert compact_g7 == expected_g7_negative

    # The full c2-zero D8 numerator is kept before any rootwise split.
    delta_numerator = la_add(la_shift(1, k),
                             la_scale(-4, la_mul(t, v0)))
    n8_zero = la_add(
        la_mul(delta_numerator, delta_numerator),
        la_scale(-8, la_shift(2, la_mul(t, t, z)
                              if False else la_mul(la_mul(t, t), z))),
        la_scale(1024, la_shift(3, la_add(
            la_mul(la_term(1, 0, "c6"), la_mul(v0, v0)),
            la_mul(f5, t),
        ))),
    )
    expected_g8_zero = la_scale(Q(3, 32768), la_shift(-4, n8_zero))
    actual_g8_zero = la_negative(la_substitute(g[8], c2_zero))
    assert actual_g8_zero == expected_g8_zero

    # On the active branch V0=A*S, every c2 pole in D7 becomes regular.
    active_stage = {"v0": la_term(1, 1, "s")}
    actual_g7_active = la_negative(la_substitute(g[7], active_stage))
    active_j7 = la_mul(t, la_add(k, la_scale(-2, la_mul(t, la_term(1, 0, "s")))))
    expected_g7_active = la_scale(Q(3, 2048), la_shift(-1, active_j7))
    assert actual_g7_active == expected_g7_active

    s = la_term(1, 0, "s")
    h = la_add(la_mul(s, s), la_scale(-2, z))
    active_e8 = la_add(
        la_power(la_add(k, la_scale(-4, la_mul(t, s))), 2),
        la_scale(-8, la_mul(la_mul(t, t), z)),
    )
    active_p8 = la_add(
        la_scale(-1, la_power(h, 3)),
        la_scale(-8, la_mul(h, la_add(k, la_scale(-2, la_mul(t, s))))),
        la_scale(32, la_mul(t, t)),
    )
    expected_g8_active = la_add(
        la_scale(Q(3, 32768), la_shift(-2, active_e8)),
        la_scale(Q(5, 65536), la_shift(-1, la_mul(
            la_term(1, 0, "c2"), active_p8))),
        la_scale(Q(3, 32), la_shift(-1, la_mul(f5, t))),
    )
    actual_g8_active = la_negative(la_substitute(g[8], active_stage))
    assert actual_g8_active == expected_g8_active
    generic_c2_poles = la_negative(g[7])
    assert any(power == -5 and symbols == ("c2", "v0", "v0", "v0", "v0", "v0")
               for power, symbols in generic_c2_poles)

    # On the generic q1 chart gcd(A,V0)=1, D7 forces T=A*U.
    generic_stage = {"c2": {}, "t": la_term(1, 1, "u")}
    g7_generic = la_substitute(g[7], generic_stage)
    assert not la_negative(g7_generic)

    g8_generic = la_substitute(g[8], generic_stage)

    delta4 = la_add(
        f4,
        la_scale(Q(-1, 16), la_mul(v0, la_term(1, 0, "u"))),
        la_scale(Q(-1, 64), la_mul(z, z)),
    )
    expected_g8_generic = la_add(
        la_scale(Q(3, 8), la_shift(-2, la_mul(delta4, delta4))),
        la_term(Q(3, 32), -1, "c6", "v0", "v0"),
    )
    assert la_negative(g8_generic) == expected_g8_generic

    # The generic q1 chart continues one more row exactly as the fixed slice,
    # except that the invertible residue V0 multiplies the square obstruction.
    F9 = general_prefix(9)
    _, rows9 = continuation(F9, 9)

    # Exact global D9 target on every c2=0 divisor stratum with B nonconstant,
    # where D8 has already forced c6=0.  Regular c4/c8 and the same-row F9/G9
    # gauges are retained but do not enter this polar numerator.
    f6 = la_term(1, 0, "f6")
    n9 = la_add(
        la_scale(-48, la_mul(la_mul(t, t), la_power(v0, 3))),
        la_scale(1536, la_shift(1, la_mul(la_mul(f4, t), la_power(v0, 2)))),
        la_scale(-24, la_shift(1, la_mul(la_mul(t, la_power(v0, 2)),
                                        la_power(z, 2)))),
        la_scale(-12288, la_shift(2, la_mul(la_power(f4, 2), v0))),
        la_scale(384, la_shift(2, la_mul(la_mul(f4, v0), la_power(z, 2)))),
        la_scale(48, la_shift(2, la_mul(la_mul(la_power(t, 2), v0), z))),
        la_scale(-3, la_shift(2, la_mul(v0, la_power(z, 4)))),
        la_scale(-768, la_shift(3, la_mul(la_mul(f4, t), z))),
        la_scale(-8, la_shift(3, la_power(t, 3))),
        la_scale(12, la_shift(3, la_mul(t, la_power(z, 3)))),
        la_scale(768, la_shift(3, la_mul(
            f5, la_add(la_shift(1, k), la_scale(-4, la_mul(t, v0)))))),
        la_scale(6144, la_shift(5, la_mul(f6, t))),
    )
    expected_g9_zero = la_scale(Q(1, 65536), la_shift(-6, n9))
    actual_g9_zero = la_negative(la_substitute(
        rows9[9], {"c2": {}, "c6": {}}))
    assert actual_g9_zero == expected_g9_zero
    repair = d9_repair_theorem(rows9)

    stage_d7 = {"c2": {}, "t": la_term(1, 1, "u")}
    f4_after_d8 = la_add(
        la_scale(Q(1, 16), la_mul(v0, la_term(1, 0, "u"))),
        la_scale(Q(1, 64), la_mul(z, z)),
        la_term(1, 1, "w"),
    )
    stage_d8 = {"f4": f4_after_d8, "c6": {}}
    g9_generic = la_substitute(la_substitute(rows9[9], stage_d7), stage_d8)
    expected_g9_generic = la_add(
        la_term(Q(-3, 16), -2, "v0", "w", "w"),
        la_term(Q(3, 4), -1, "f5", "w"),
        la_term(Q(-3, 256), -1, "u", "w", "z"),
    )
    assert la_negative(g9_generic) == expected_g9_generic
    compact_post_repair = la_scale(Q(3, 256), la_shift(-2, la_mul(
        la_term(1, 0, "w"),
        la_add(
            la_scale(-16, la_mul(v0, la_term(1, 0, "w"))),
            la_shift(1, la_add(la_scale(64, f5),
                               la_scale(-1, la_mul(la_term(1, 0, "u"), z)))),
        ),
    )))
    assert expected_g9_generic == compact_post_repair
    if debug:
        print("g7 all", json.dumps(la_encode(g[7]), indent=2))
        print("g7 c2=0 negative", json.dumps(la_encode(la_negative(g7)), indent=2))
        print("g8 generic negative", json.dumps(la_encode(la_negative(g8_generic)), indent=2))

    target = target_payload()
    controls = q1_polynomial_controls()
    survivor = partial_divisor_survivor(g)
    full_census = {}
    for weight in (7, 8):
        census = {}
        for a_power, _ in g[weight]:
            census[a_power] = census.get(a_power, 0) + 1
        full_census[str(weight)] = {
            "term_count": len(g[weight]),
            "A_exponent_census": {str(power): count
                                    for power, count in sorted(census.items())},
            "sha256": hashlib.sha256(json.dumps(
                la_encode(g[weight]), sort_keys=True,
                separators=(",", ":")).encode()).hexdigest(),
        }
    return {
        "status": "PASS_EXACT_PROVISIONAL_Q1_PREFIX_D7_D9_DIVISOR_REPAIR",
        "source_pins": {str(path.relative_to(ROOT)): expected
                        for path, expected in SOURCE_PINS.items()},
        "modes": {str(k): str(v) for k, v in MODES.items()},
        "q1_convention": {
            "V0": "A'*R0+2*A*R0'",
            "degree_R0": "<=4",
            "identity": "T_A(A^2*R0)=A^2*V0 for T_A(Q)=2*A*Q'-3*A'*Q",
            "literal_q1_factor_firewall": (
                "the reviewed differential certificate has F1=2*T_A(Q); "
                "over a characteristic-zero field the image subspace is unchanged"
            ),
        },
        "q1_polynomial_controls_A_equals_X4_minus_1": controls,
        "full_characteristic_rows_no_regular_terms_dropped": full_census,
        "raw_window_partial_divisor_survivor": survivor,
        "D7_c2_zero_negative": la_encode(expected_g7_negative),
        "D7_c2_zero_compact": (
            "3*T*(A*(64*F4-Z^2)-2*T*V0)/(2048*A^2)"
        ),
        "D7_active_negative": la_encode(expected_g7_active),
        "D7_active_compact": "3*T*(K-2*T*S)/(2048*A), V0=A*S",
        "D8_c2_zero_negative": la_encode(expected_g8_zero),
        "D8_active_negative": la_encode(expected_g8_active),
        "D8_active_P8": (
            "-(S^2-2*Z)^3-8*(S^2-2*Z)*(K-2*T*S)+32*T^2"
        ),
        "D7_generic_q1_after_T_equals_AU_negative": la_encode(la_negative(g7_generic)),
        "D8_generic_q1_negative": la_encode(la_negative(g8_generic)),
        "D9_generic_q1_negative_after_D8_lift": la_encode(expected_g9_generic),
        "D9_divisor_repair_theorem": repair,
        "post_repair_c2_zero_compact": (
            "g9^-=3*W*(-16*V0*W+A*(64*F5-U0*Z))/(256*A^2)"
        ),
        "earliest_change": {
            "weight": 7,
            "reason": (
                "V0=1 is a unit modulo A and forces A|T; a genuine q1 V0 may "
                "vanish at a subset of the four roots, leaving only A|T^2*V0"
            ),
            "invariant_replacement": (
                "the zero-locus idempotent of V0 in the etale root algebra; "
                "equivalently C=gcd(A,V0)=gcd(A,R0) after a splitting field"
            ),
        },
        "target_sha256": hashlib.sha256(
            (json.dumps(target, sort_keys=True, indent=2) + "\n").encode()
        ).hexdigest(),
        "scope": (
            "Exact characteristic polynomiality through D9 sufficient to prove "
            "A|T on the full q1/c2 branch cover, plus the next c2-zero square-"
            "defect target. No endpoint theorem and no V0=1 raw-513 reuse."
        ),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()
    result = calculate_result(args.debug)
    target = target_payload()
    encoded = json.dumps(result, sort_keys=True, indent=2) + "\n"
    target_encoded = json.dumps(target, sort_keys=True, indent=2) + "\n"
    if args.check:
        assert RESULT.read_text() == encoded
        assert TARGET.read_text() == target_encoded
    else:
        RESULT.write_text(encoded)
        TARGET.write_text(target_encoded)
    print(result["status"])


if __name__ == "__main__":
    main()
