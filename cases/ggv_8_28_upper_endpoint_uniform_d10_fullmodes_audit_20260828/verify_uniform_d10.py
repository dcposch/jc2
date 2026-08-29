#!/usr/bin/env python3
"""Independent exact audit of the full-fixture characteristic cascade through D10.

This checker intentionally reconstructs the Laurent recurrence and the literal
513-row determinant source with Python's standard-library Fraction arithmetic.
It does not import the provisional D9 producer.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RAW = ROOT / "cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json"
CHARGED_SCRIPT = (ROOT / "cases/ggv_8_28_upper_endpoint_uniform_d9_fullmodes_20260828"
                  / "verify_uniform_d9.py")
CHARGED_RESULT = (ROOT / "cases/ggv_8_28_upper_endpoint_uniform_d9_fullmodes_20260828"
                  / "RESULT.json")
RESULT = HERE / "RESULT.json"
RAW_SHA256 = "ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0"
CHARGED_SCRIPT_SHA256 = "f4e40d3324a9dc9058b6ec80a01458468b3a90d0d3b4794841e76450c42e8dbc"
CHARGED_RESULT_SHA256 = "9ca90959f284052bf669911c15e675892c1749b0bfed3cb4fd6462156e61b059"


# Sparse Laurent polynomials in A with ordinary symbolic coefficient monomials.
# Key: (power of A, sorted tuple of coefficient symbols).
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


def la_shift(a_power, item):
    return {(old_power + a_power, symbols): coefficient
            for (old_power, symbols), coefficient in item.items()}


DERIVATIVES = {
    "z": "z_x", "v": "v_x", "w": "w_x", "u": "u_x", "r": "r_x",
    "q": "q_x",
    **{f"f{weight}": f"f{weight}_x" for weight in range(5, 12)},
}


def la_derivative(item):
    answer = {}
    for (a_power, symbols), coefficient in item.items():
        if a_power:
            key = (a_power - 1, tuple(sorted(symbols + ("a_x",))))
            answer[key] = answer.get(key, Q(0)) + coefficient * a_power
        for position, symbol in enumerate(symbols):
            derivative = DERIVATIVES.get(symbol)
            if derivative is None:
                continue
            changed = list(symbols)
            changed[position] = derivative
            key = (a_power, tuple(sorted(changed)))
            answer[key] = answer.get(key, Q(0)) + coefficient
    return {key: coefficient for key, coefficient in answer.items() if coefficient}


def la_operator(weight, item):
    """L_n(R)=4(12-n) A^3 A' R - 8 A^4 R'."""
    first = la_scale(4 * (12 - weight),
                     la_mul(la_shift(3, item), la_term(1, 0, "a_x")))
    second = la_scale(-8, la_shift(4, la_derivative(item)))
    return la_add(first, second)


def la_negative(item):
    return {key: coefficient for key, coefficient in item.items() if key[0] < 0}


def la_mod_a(bound, item):
    return {key: coefficient for key, coefficient in item.items() if key[0] < bound}


def la_encode(item):
    return [
        {"A_exponent": a_power, "coefficient": str(coefficient),
         "monomial": list(symbols)}
        for (a_power, symbols), coefficient in sorted(item.items())
    ]


def la_substitute(item, substitutions):
    answer = {}
    for (a_power, symbols), coefficient in item.items():
        term = la_term(coefficient, a_power)
        for symbol in symbols:
            term = la_mul(term, substitutions.get(symbol, la_term(1, 0, symbol)))
        answer = la_add(answer, term)
    return answer


def fractional_coefficients(F, exponent, maximum):
    """Solve F*y'=exponent*F'*y coefficientwise from y_0=A^(4 exponent)."""
    y = {0: la_term(1, int(4 * exponent))}
    for weight in range(1, maximum + 1):
        numerator = {}
        for index in range(1, weight + 1):
            factor = (exponent + 1) * index - weight
            numerator = la_add(numerator,
                               la_scale(factor, la_mul(F[index], y[weight - index])))
        y[weight] = la_scale(Q(1, weight), la_shift(-4, numerator))
    return y


MODES = {
    4: Q(1), 6: Q(3, 4), 8: Q(1, 2), 10: Q(1, 4), 12: Q(0),
    14: Q(-1, 4), 16: Q(-1, 2), 18: Q(-3, 4), 20: Q(-1),
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
                row = la_add(row,
                             la_mul(la_term(1, 0, f"c{birth}"),
                                    powers[exponent][weight - birth]))
        rows[weight] = row
    return powers, rows


def common_F_prefix():
    z = la_term(1, 0, "z")
    v = la_term(1, 0, "v")
    return {
        0: la_term(1, 4),
        1: la_term(1, 2),
        2: la_add(la_term(Q(1, 4)), la_scale(Q(1, 4), la_mul(la_term(1, 2), z))),
        3: la_add(la_scale(Q(1, 8), z),
                  la_scale(Q(1, 8), la_mul(la_term(1, 2), v))),
    }


def characteristic_d8_d9():
    z = la_term(1, 0, "z")
    v = la_term(1, 0, "v")
    w = la_term(1, 0, "w")
    F = common_F_prefix()
    F[4] = la_add(la_scale(Q(1, 16), v),
                  la_scale(Q(1, 64), la_mul(z, z)),
                  la_mul(la_term(1, 1), w))
    for weight in range(5, 10):
        F[weight] = la_term(1, 0, f"f{weight}")
    powers, g = continuation(F, 9)

    expected_g8_polar = la_term(Q(3, 32), -1, "c6")
    expected_g9_polar_after_c6 = la_add(
        la_term(Q(-3, 16), -2, "w", "w"),
        la_term(Q(3, 4), -1, "f5", "w"),
        la_term(Q(-3, 256), -1, "v", "w", "z"),
    )
    assert la_negative(g[8]) == expected_g8_polar
    g9_c6_zero = la_substitute(g[9], {"c6": {}})
    assert la_negative(g9_c6_zero) == expected_g9_polar_after_c6

    d8 = la_scale(-1, la_operator(8, expected_g8_polar))
    assert la_mod_a(3, d8) == la_term(Q(-9, 4), 2, "a_x", "c6")
    d9 = la_scale(-1, la_operator(9, expected_g9_polar_after_c6))
    assert la_mod_a(2, d9) == la_term(Q(21, 4), 1, "a_x", "w", "w")
    return {
        "g8_polar": la_encode(expected_g8_polar),
        "D8_raw_mod_A3": la_encode(la_mod_a(3, d8)),
        "g9_polar_after_c6_zero": la_encode(expected_g9_polar_after_c6),
        "D9_raw_mod_A2": la_encode(la_mod_a(2, d9)),
    }


def characteristic_d10_d11():
    z = la_term(1, 0, "z")
    v = la_term(1, 0, "v")
    u = la_term(1, 0, "u")
    F = common_F_prefix()
    F.update({
        4: la_add(la_scale(Q(1, 16), v),
                  la_scale(Q(1, 64), la_mul(z, z)),
                  la_mul(la_term(1, 2), u)),
    })
    for weight in range(5, 12):
        F[weight] = la_term(1, 0, f"f{weight}")
    powers, g = continuation(F, 11)

    delta5 = la_add(
        la_term(1, 0, "f5"),
        la_term(Q(-1, 2), 0, "u"),
        la_term(Q(-1, 64), 0, "v", "z"),
    )
    c6_zero = {"c6": {}}
    g10_c6_zero = la_substitute(g[10], c6_zero)
    expected_g10_polar = la_scale(Q(3, 8), la_shift(-2, la_mul(delta5, delta5)))
    assert la_negative(g10_c6_zero) == expected_g10_polar
    d10 = la_scale(-1, la_operator(10, expected_g10_polar))
    expected_d10_mod_a2 = la_scale(
        -9, la_mul(la_term(1, 1, "a_x"), la_mul(delta5, delta5)))
    assert la_mod_a(2, d10) == expected_d10_mod_a2

    after_d10 = {
        "c6": {},
        "f5": la_add(
            la_scale(Q(1, 2), u),
            la_scale(Q(1, 64), la_mul(v, z)),
            la_term(1, 1, "r"),
        ),
    }
    g11_after_d10 = la_substitute(g[11], after_d10)
    delta6 = la_add(
        la_term(1, 0, "f6"),
        la_term(Q(-1, 8), 0, "u", "z"),
        la_term(Q(-1, 256), 0, "v", "v"),
    )
    expected_g11_polar = la_add(
        la_term(Q(-3, 16), -2, "r", "r"),
        la_term(Q(1, 4), -1, "c10"),
        la_scale(Q(3, 4), la_shift(-1, la_mul(la_term(1, 0, "r"), delta6))),
    )
    assert la_negative(g11_after_d10) == expected_g11_polar
    d11 = la_scale(-1, la_operator(11, expected_g11_polar))
    assert la_mod_a(2, d11) == la_term(Q(15, 4), 1, "a_x", "r", "r")

    after_second_divisibility = la_substitute(g11_after_d10, {
        "r": la_term(1, 1, "q"),
    })
    assert la_negative(after_second_divisibility) == la_term(Q(1, 4), -1, "c10")
    c10_residual = la_scale(-1, la_operator(
        11, la_term(Q(1, 4), -1, "c10")))
    assert c10_residual == la_term(-3, 2, "a_x", "c10")

    return {
        "post_D9_substitution": {
            "W": "A*R",
            "F4": "V/16+Z^2/64+A^2*R",
        },
        "Delta5": "F5-R/2-Z*V/64",
        "g10_polar": la_encode(expected_g10_polar),
        "D10_raw_mod_A2": la_encode(expected_d10_mod_a2),
        "after_D10_radical": "Delta5=A*S",
        "Delta6": "F6-R*Z/8-V^2/256",
        "g11_polar_after_D10": la_encode(expected_g11_polar),
        "D11_raw_mod_A2": la_encode(la_mod_a(2, d11)),
        "g11_polar_after_second_divisibility": la_encode(
            la_negative(after_second_divisibility)),
        "D11_c10_residual_mod_A3": la_encode(c10_residual),
        "complete_modes_D10": ["c4*F6", "c6*(F^(3/4))_4=0", "c8*Z/8", "c10*A"],
        "complete_modes_D11": ["c4*F7", "c6*(F^(3/4))_5=0", "c8*V/16", "c10/(4*A)"],
    }


# Independent ordinary Q[X] arithmetic for literal raw-source evaluation.
def xp_trim(item):
    answer = list(item)
    while answer and answer[-1] == 0:
        answer.pop()
    return answer


def xp_add(*items):
    length = max((len(item) for item in items), default=0)
    return xp_trim([sum(((item[index] if index < len(item) else Q(0))
                         for item in items), Q(0))
                    for index in range(length)])


def xp_scale(coefficient, item):
    return xp_trim([Q(coefficient) * value for value in item])


def xp_mul(left, right):
    if not left or not right:
        return []
    answer = [Q(0)] * (len(left) + len(right) - 1)
    for left_degree, left_coefficient in enumerate(left):
        for right_degree, right_coefficient in enumerate(right):
            answer[left_degree + right_degree] += left_coefficient * right_coefficient
    return xp_trim(answer)


def xp_power(item, exponent):
    answer = [Q(1)]
    base = list(item)
    while exponent:
        if exponent & 1:
            answer = xp_mul(answer, base)
        base = xp_mul(base, base)
        exponent //= 2
    return answer


def xp_derivative(item):
    return xp_trim([Q(degree) * item[degree] for degree in range(1, len(item))])


def xp_encode(item):
    return {str(degree): str(coefficient) for degree, coefficient in enumerate(item)
            if coefficient}


def put_window(raw, values, kind, weight, polynomial):
    window = raw["windows"][kind][str(weight)]
    for degree, coefficient in enumerate(polynomial):
        if coefficient:
            assert window["lower"] <= degree <= window["upper"], (
                kind, weight, degree, coefficient, window)
    for degree, slot in zip(range(window["lower"], window["upper"] + 1),
                            window["slots"]):
        values[slot] = polynomial[degree] if degree < len(polynomial) else Q(0)


def reconstruct_literal(raw, values):
    A = [Q(-1), Q(0), Q(0), Q(0), Q(1)]
    H = xp_power(A, 2)
    Z = [values.get(f"z_{degree}", Q(0)) for degree in range(7)]
    T = [values.get(f"tt_{degree}", Q(0)) for degree in range(10)]
    F = {
        0: xp_power(H, 2),
        1: H,
        2: xp_scale(Q(1, 4), xp_add([Q(1)], xp_mul(H, Z))),
        3: xp_scale(Q(1, 8), xp_add(Z, xp_mul(A, T))),
    }
    G = {
        0: xp_power(H, 3),
        1: xp_scale(Q(3, 2), xp_power(H, 2)),
    }
    G[2] = xp_add(xp_scale(Q(3, 2), xp_mul(H, F[2])), xp_scale(Q(3, 8), H))
    G[3] = xp_add(xp_scale(Q(3, 2), xp_mul(H, F[3])),
                  xp_scale(Q(3, 4), F[2]), [Q(-1, 16)])
    for kind, destination, weights in (
            ("F", F, range(4, 15)), ("G", G, range(4, 22))):
        for weight in weights:
            window = raw["windows"][kind][str(weight)]
            polynomial = [Q(0)] * (window["upper"] + 1)
            for degree, slot in zip(range(window["lower"], window["upper"] + 1),
                                    window["slots"]):
                polynomial[degree] = values.get(slot, Q(0))
            destination[weight] = xp_trim(polynomial)
    return A, F, G


def literal_determinant_rows(F, G):
    rows = {}
    for weight in range(4, 23):
        row = []
        for left_weight in range(weight + 1):
            right_weight = weight - left_weight
            if left_weight not in F or right_weight not in G:
                continue
            row = xp_add(
                row,
                xp_scale(12 - right_weight,
                         xp_mul(xp_derivative(F[left_weight]), G[right_weight])),
                xp_scale(left_weight - 8,
                         xp_mul(F[left_weight], xp_derivative(G[right_weight]))),
            )
        rows[weight] = row
    return rows


def generator_values(raw, values):
    answer = []
    for generator in raw["generators"]:
        value = Q(0)
        for monomial, encoded_coefficient in generator["terms"]:
            term = Q(encoded_coefficient)
            for variable in monomial:
                term *= values.get(variable, Q(0))
            value += term
        answer.append(value)
    return answer


def assert_all_513(raw, values):
    _, F, G = reconstruct_literal(raw, values)
    direct = literal_determinant_rows(F, G)
    serialized = generator_values(raw, values)
    assert len(serialized) == 513
    for index, (generator, value) in enumerate(zip(raw["generators"], serialized)):
        weight = int(generator["row"])
        degree = int(generator["x_degree"])
        expected = direct[weight][degree] if degree < len(direct[weight]) else Q(0)
        if weight == 22 and degree == 0:
            expected -= 1
        assert value == expected, (index, weight, degree, value, expected)
    return direct, serialized


def row_provenance(raw, serialized, weight):
    answer = []
    for index, (generator, value) in enumerate(zip(raw["generators"], serialized)):
        if int(generator["row"]) == weight and value:
            answer.append({
                "generator_index_zero_based": index,
                "x_degree": int(generator["x_degree"]),
                "generator_sha256": generator["sha256"],
                "value": str(value),
            })
    return {
        "row": weight,
        "row_sha256": raw["per_row"][str(weight)]["row_sha256"],
        "nonzero_generators": answer,
    }


def execute_mutation(raw, assignments, first_residual, expected, prior_zero):
    values = {}
    for kind, weight, polynomial in assignments:
        put_window(raw, values, kind, weight, polynomial)
    direct, serialized = assert_all_513(raw, values)
    assert all(not direct[weight] for weight in prior_zero)
    assert direct[first_residual] == expected, (
        first_residual, direct[first_residual], expected)
    return {
        "first_residual_row": first_residual,
        "prior_rows_zero": list(prior_zero),
        "residual": xp_encode(expected),
        "literal_row_provenance": row_provenance(raw, serialized, first_residual),
        "all_513_serialized_generators_match_independent_determinant_recurrence": True,
    }


def t_series_multiply(left, right, maximum):
    answer = {weight: [] for weight in range(maximum + 1)}
    for left_weight, left_polynomial in left.items():
        for right_weight, right_polynomial in right.items():
            weight = left_weight + right_weight
            if weight <= maximum:
                answer[weight] = xp_add(answer[weight],
                                        xp_mul(left_polynomial, right_polynomial))
    return answer


def literal_mutations(raw):
    A = [Q(-1), Q(0), Q(0), Q(0), Q(1)]
    A_x = xp_derivative(A)
    A2, A3 = xp_power(A, 2), xp_power(A, 3)

    def c6_assign(scalar):
        return [("G", 6, xp_scale(scalar, A3)),
                ("G", 7, xp_scale(Q(3, 4) * scalar, A))]

    def d9_assign(scalar):
        return [("F", 4, xp_scale(scalar, A)),
                ("G", 4, xp_scale(Q(3, 2) * scalar, A3)),
                ("G", 5, xp_scale(Q(3, 4) * scalar, A)),
                ("G", 8, [Q(3, 8) * scalar * scalar])]

    def d10_assign(scalar):
        return [("F", 5, [scalar]),
                ("G", 5, xp_scale(Q(3, 2) * scalar, A2)),
                ("G", 6, [Q(3, 4) * scalar])]

    def d11_square_assign(scalar):
        return [("F", 5, xp_scale(scalar, A)),
                ("G", 5, xp_scale(Q(3, 2) * scalar, A3)),
                ("G", 6, xp_scale(Q(3, 4) * scalar, A)),
                ("G", 10, [Q(3, 8) * scalar * scalar])]

    def d11_c10_assign(scalar):
        return [("G", 10, xp_scale(scalar, A))]

    recipes = {
        "D8_c6": (c6_assign, 8, xp_scale(Q(-9, 4), xp_mul(A2, A_x)), range(4, 8)),
        "D9_W_square": (d9_assign, 9, xp_scale(Q(21, 4), xp_mul(A, A_x)), range(4, 9)),
        "D10_Delta5_square": (d10_assign, 10, xp_scale(-9, xp_mul(A, A_x)), range(4, 10)),
        "D11_second_square": (d11_square_assign, 11,
                               xp_scale(Q(15, 4), xp_mul(A, A_x)), range(4, 11)),
        "D11_c10": (d11_c10_assign, 11, xp_scale(-3, xp_mul(A2, A_x)), range(4, 11)),
    }
    answer = {}
    for label, (recipe, row, expected_unit, prior) in recipes.items():
        base = execute_mutation(raw, recipe(Q(1)), row, expected_unit, prior)
        scaling = {}
        power = 1 if label in {"D8_c6", "D11_c10"} else 2
        for scalar in (Q(-1), Q(2)):
            expected = xp_scale(scalar ** power, expected_unit)
            replay = execute_mutation(raw, recipe(scalar), row, expected, prior)
            scaling[str(scalar)] = replay["residual"]
        base["live_scaling_mutations"] = scaling
        base["scaling_power"] = power
        answer[label] = base

    # A source-level regression for the uniform Z*V/64 term in Delta5.
    # Take Z=V=1,R=0, so the exact square has F5=1/64.  Removing only that
    # term and continuing F^(3/2) through weight nine creates exactly the
    # predicted D10 square residual.
    S = {0: A2, 1: [Q(1, 2)], 2: [Q(1, 8)], 3: [Q(1, 16)]}
    square_F = t_series_multiply(S, S, 14)
    square_G = t_series_multiply(t_series_multiply(S, S, 21), S, 21)
    cross_values = {"z_0": Q(1)}
    cross_values["tt_0"] = Q(-1)
    cross_values["tt_4"] = Q(1)
    for weight in range(4, 15):
        put_window(raw, cross_values, "F", weight, square_F[weight])
    for weight in range(4, 22):
        put_window(raw, cross_values, "G", weight, square_G[weight])
    direct_cross, _ = assert_all_513(raw, cross_values)
    assert all(not direct_cross[weight] for weight in range(4, 23))
    assert square_F[5] == [Q(1, 64)]

    omitted_cross_values = dict(cross_values)
    put_window(raw, omitted_cross_values, "F", 5, [])
    defect = Q(-1, 64)
    for offset, coefficient in enumerate(
            (A2, [Q(1, 2)], [Q(1, 8)], [Q(1, 16)])):
        weight = 5 + offset
        adjusted = xp_add(square_G[weight],
                          xp_scale(Q(3, 2) * defect, coefficient))
        put_window(raw, omitted_cross_values, "G", weight, adjusted)
    direct_omitted, serialized_omitted = assert_all_513(raw, omitted_cross_values)
    assert all(not direct_omitted[weight] for weight in range(4, 10))
    expected_omitted = xp_scale(Q(-9, 4096), xp_mul(A, A_x))
    assert direct_omitted[10] == expected_omitted
    answer["D10_ZV_cross_term_regression"] = {
        "exact_square_assignment": "Z=V=1,R=0; F=S^2,G=S^3 with S=A^2+t/2+t^2/8+t^3/16",
        "required_literal_F5": "1/64=Z*V/64",
        "exact_square_D4_through_D22": "zero before affine target fold",
        "mutation": "set F5=0 and continue F^(3/2) through G9",
        "mutation_rows_D4_through_D9": "zero",
        "mutation_D10": xp_encode(expected_omitted),
        "literal_row_provenance": row_provenance(raw, serialized_omitted, 10),
        "conclusion": "dropping Z*V/64 from Delta5 is detected",
    }

    # Mandatory forced-negative-mode firewall: two literal full-fixture points.
    gauge_values = {}
    put_window(raw, gauge_values, "F", 8, [Q(1)])
    direct, serialized = assert_all_513(raw, gauge_values)
    assert all(not direct[weight] for weight in range(4, 23))
    gauge_plus_values = dict(gauge_values)
    put_window(raw, gauge_plus_values, "G", 8, xp_scale(Q(3, 2), A2))
    put_window(raw, gauge_plus_values, "G", 9, [Q(3, 4)])
    direct_plus, serialized_plus = assert_all_513(raw, gauge_plus_values)
    assert all(not direct_plus[weight] for weight in range(4, 23))
    answer["forced_negative_mode_firewall"] = {
        "point_one": {
            "F": "(A^2+t/2)^2+t^8", "G": "(A^2+t/2)^3",
            "required_modes": {"c8": "-3/2", "c16": "3/8"},
            "all_D4_through_D22_zero_before_affine_target_fold": True,
            "folded_D22_generator_value": str(serialized[495]),
        },
        "point_two": {
            "F": "(A^2+t/2)^2+t^8",
            "G": "(A^2+t/2)^3+(3/2)t^8(A^2+t/2)",
            "required_modes": {"c16": "-3/8"},
            "all_D4_through_D22_zero_before_affine_target_fold": True,
            "folded_D22_generator_value": str(serialized_plus[495]),
        },
        "all_513_generators_replayed_at_both_points": True,
    }
    return answer


def forced_mode_series_firewall():
    F = {weight: {} for weight in range(22)}
    F[0] = la_term(1, 4)
    F[1] = la_term(1, 2)
    F[2] = la_term(Q(1, 4))
    F[8] = la_term(1)
    p32 = fractional_coefficients(F, Q(3, 2), 21)
    p12 = fractional_coefficients(F, Q(1, 2), 21)
    pm12 = fractional_coefficients(F, Q(-1, 2), 21)
    base = {0: la_term(1, 6), 1: la_term(Q(3, 2), 4),
            2: la_term(Q(3, 4), 2), 3: la_term(Q(1, 8))}
    for weight in range(22):
        point_one = p32[weight]
        if weight >= 8:
            point_one = la_add(point_one, la_scale(Q(-3, 2), p12[weight - 8]))
        if weight >= 16:
            point_one = la_add(point_one, la_scale(Q(3, 8), pm12[weight - 16]))
        assert point_one == base.get(weight, {})

        point_two = p32[weight]
        if weight >= 16:
            point_two = la_add(point_two, la_scale(Q(-3, 8), pm12[weight - 16]))
        expected_two = base.get(weight, {})
        if weight == 8:
            expected_two = la_add(expected_two, la_term(Q(3, 2), 2))
        if weight == 9:
            expected_two = la_add(expected_two, la_term(Q(3, 4)))
        assert point_two == expected_two
    return {
        "checked_weights": list(range(22)),
        "identity_one": "B^3=F^(3/2)-(3/2)t^8 F^(1/2)+(3/8)t^16 F^(-1/2) mod t^22",
        "identity_two": "B^3+(3/2)t^8B=F^(3/2)-(3/8)t^16 F^(-1/2) mod t^22",
        "conclusion": "c16 is mandatory and occurs with both signs; c14,c18,c20 remain mandatory continuation coordinates",
    }


def calculate_result():
    assert hashlib.sha256(RAW.read_bytes()).hexdigest() == RAW_SHA256
    assert hashlib.sha256(CHARGED_SCRIPT.read_bytes()).hexdigest() == CHARGED_SCRIPT_SHA256
    assert hashlib.sha256(CHARGED_RESULT.read_bytes()).hexdigest() == CHARGED_RESULT_SHA256
    raw = json.loads(RAW.read_text())
    assert raw["variable_count"] == 303
    assert raw["generator_count"] == len(raw["generators"]) == 513
    assert {int(generator["row"]) for generator in raw["generators"]} == set(range(4, 23))

    mode_schedule = []
    for birth, exponent in MODES.items():
        mode_schedule.append({
            "birth_weight": birth,
            "F_exponent": str(exponent),
            "birth_A_power": 4 * exponent.numerator // exponent.denominator,
            "role": "free_polynomial" if birth <= 12 else "forced_rational",
            "support_at_D10": birth <= 10,
            "support_at_D11": birth <= 11,
            "continuation_status": "retained_mandatory",
        })
    assert [item["birth_A_power"] for item in mode_schedule] == [4, 3, 2, 1, 0, -1, -2, -3, -4]

    return {
        "schema": "jc2.ggv.upper_endpoint.uniform_d10_d11_fullmodes_audit.result.v1",
        "status": "PASS_EXACT_FIELD_POINT_CASCADE_THROUGH_D11",
        "source": {
            "authoritative_raw_system": str(RAW.relative_to(ROOT)),
            "authoritative_raw_system_sha256": RAW_SHA256,
            "raw_variable_count": 303,
            "raw_generator_count": 513,
            "literal_rows": "D4 through D22 inclusive",
            "charged_provisional_script": str(CHARGED_SCRIPT.relative_to(ROOT)),
            "charged_provisional_script_sha256": CHARGED_SCRIPT_SHA256,
            "charged_provisional_result": str(CHARGED_RESULT.relative_to(ROOT)),
            "charged_provisional_result_sha256": CHARGED_RESULT_SHA256,
            "independence": "no import from charged script; Laurent recurrence and all 513 raw evaluations reconstructed here",
        },
        "complete_mode_schedule": mode_schedule,
        "calculation": {
            "D8_D9_independent_replay": characteristic_d8_d9(),
            "D10_D11_extension": characteristic_d10_d11(),
            "forced_mode_series_firewall": forced_mode_series_firewall(),
        },
        "literal_raw_mutations": literal_mutations(raw),
        "theorems": {
            "independent_D8_D9_replay": {
                "hypotheses": [
                    "characteristic-zero field point of the fixed branch-P fixture",
                    "T=A*V",
                    "F4-V/16-Z^2/64=A*W",
                    "D4 through D9 vanish",
                ],
                "conclusions": ["c6=0", "A divides W"],
                "raw_congruences": [
                    "D8=-(9/4)c6*A^2*A' mod A^3",
                    "D9=+(21/4)A*A'*W^2 mod A^2 after c6=0",
                ],
            },
            "D10_square_defect": {
                "post_D9_notation": "W=A*R",
                "honest_uniform_defect": "Delta5=F5-R/2-Z*V/64",
                "hypothesis": "D10=0",
                "polar_identity": "polar(g10)=3*Delta5^2/(8*A^2)",
                "raw_congruence": "D10=-9*A*A'*Delta5^2 mod A^2",
                "complete_born_modes": ["c4", "c6=0", "c8", "c10"],
                "conclusion": "A divides Delta5 at field points",
                "reason": "A=X^4-1 is squarefree",
                "extra_mode_kill": "none",
            },
            "D11_second_divisibility_and_mode_kill": {
                "notation": [
                    "Delta5=A*S",
                    "Delta6=F6-R*Z/8-V^2/256",
                ],
                "polar_identity": (
                    "polar(g11)=-3*S^2/(16*A^2)"
                    "+(c10/4+(3/4)*S*Delta6)/A"
                ),
                "causal_step_one": {
                    "raw_congruence": "D11=+(15/4)A*A'*S^2 mod A^2",
                    "conclusion": "A divides S at field points",
                },
                "causal_step_two": {
                    "substitution": "S=A*Q",
                    "remaining_pole": "c10/(4*A)",
                    "raw_congruence": "D11=-3*c10*A^2*A' mod A^3",
                    "conclusion": "c10=0",
                    "no_cancellation": "all base order-one terms and c4,c8 modes are polynomial; c6=0 and c12 is not born",
                },
                "combined_conclusion": "F5=R/2+Z*V/64+A^2*Q and c10=0",
            },
        },
        "scope_firewall": [
            "field-radical divisibility only; no scheme-theoretic divisibility assertion",
            "the Z*V/64 term is mandatory in the uniform fixture and has a literal live regression",
            "c14,c16,c18,c20 are retained forced rational continuation coordinates, not set to zero",
            "the literal F8 gauge points requiring c16=+/-3/8 are replayed against all 513 generators",
            "no endpoint emptiness, full branch-P classification, Keller-pair theorem, or JC2 conclusion",
            "no CAS, AWS, floating point, interpolation, or root evaluation",
        ],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--dump", action="store_true")
    args = parser.parse_args()
    payload = calculate_result()
    encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
    if args.write:
        RESULT.write_bytes(encoded)
    if args.check:
        assert RESULT.read_bytes() == encoded
    if args.dump:
        print(encoded.decode(), end="")
    else:
        print(json.dumps({
            "status": payload["status"],
            "D10": payload["theorems"]["D10_square_defect"]["conclusion"],
            "D11": payload["theorems"]["D11_second_divisibility_and_mode_kill"]["combined_conclusion"],
            "check": args.check,
        }, sort_keys=True))


if __name__ == "__main__":
    main()
