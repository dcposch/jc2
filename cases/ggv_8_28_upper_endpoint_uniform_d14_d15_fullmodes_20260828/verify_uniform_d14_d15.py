#!/usr/bin/env python3
"""Exact full-mode A-adic continuation of the uniform branch-P cascade to D15."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PREDECESSOR = (ROOT / "cases/ggv_8_28_upper_endpoint_uniform_d12_d13_fullmodes_20260828"
               / "verify_uniform_d12_d13.py")
PREDECESSOR_RESULT = PREDECESSOR.with_name("RESULT.json")
RAW = ROOT / "cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json"
RESULT = HERE / "RESULT.json"

PREDECESSOR_SHA256 = "e5e2543ca50fc48623ccccf34f548f6171e79b31e6f80c8cfe6f5ca2b6798879"
PREDECESSOR_RESULT_SHA256 = "06ca0152a7d05dd7b4549e74138b482fc572a62acae718751e7230577c5f28c8"
RAW_SHA256 = "ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_dependencies():
    assert digest(PREDECESSOR) == PREDECESSOR_SHA256
    assert digest(PREDECESSOR_RESULT) == PREDECESSOR_RESULT_SHA256
    specification = importlib.util.spec_from_file_location("uniform_d12_frozen", PREDECESSOR)
    assert specification is not None and specification.loader is not None
    prior = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(prior)
    # Replaying the predecessor also recursively checks the pinned D8--D11
    # arithmetic and literal source dependencies.
    predecessor_replay = prior.calculate_result()
    assert predecessor_replay["status"] == "PASS_EXACT_FIELD_POINT_CASCADE_THROUGH_D13"
    desk = prior.load_predecessor()
    desk.DERIVATIVES.update({
        "u": "u_x", "y": "y_x", "f14": "f14_x", "f15": "f15_x",
    })
    return prior, desk


def characteristic_calculation(desk):
    term, add, scale, mul, shift = (
        desk.la_term, desk.la_add, desk.la_scale, desk.la_mul, desk.la_shift)
    z, v, r, q, t = (term(1, 0, name) for name in ("z", "v", "r", "q", "t"))
    F = desk.common_F_prefix()
    F[4] = add(scale(Q(1, 16), v), scale(Q(1, 64), mul(z, z)),
               mul(term(1, 2), r))
    F[5] = add(scale(Q(1, 2), r), scale(Q(1, 64), mul(z, v)),
               mul(term(1, 2), q))
    F[6] = add(scale(Q(1, 2), q), scale(Q(1, 8), mul(r, z)),
               scale(Q(1, 256), mul(v, v)), mul(term(1, 2), t))
    for weight in range(7, 15):
        F[weight] = term(1, 0, f"f{weight}")
    F[15] = {}
    _, g = desk.continuation(F, 15)

    prior_kills = {"c6": {}, "c10": {}}
    delta7 = add(
        term(1, 0, "f7"),
        term(Q(-1, 2), 0, "t"),
        term(Q(-1, 8), 0, "q", "z"),
        term(Q(-1, 16), 0, "r", "v"),
    )
    g14 = desk.la_substitute(g[14], prior_kills)
    expected_g14_polar = add(
        scale(Q(3, 8), shift(-2, mul(delta7, delta7))),
        term(1, -1, "c14"),
    )
    assert desk.la_negative(g14) == expected_g14_polar
    d14_square = scale(-1, desk.la_operator(
        14, scale(Q(3, 8), shift(-2, mul(delta7, delta7)))))
    expected_d14_mod_a2 = scale(
        -3, mul(term(1, 1, "a_x"), mul(delta7, delta7)))
    assert desk.la_mod_a(2, d14_square) == expected_d14_mod_a2
    assert desk.la_operator(14, term(1, -1, "c14")) == {}

    after_first = dict(prior_kills)
    after_first["f7"] = add(
        scale(Q(1, 2), t),
        scale(Q(1, 8), mul(q, z)),
        scale(Q(1, 16), mul(r, v)),
        term(1, 1, "u"),
    )
    g14_after_first = desk.la_substitute(g[14], after_first)
    assert desk.la_negative(g14_after_first) == term(1, -1, "c14")

    delta8 = add(
        term(1, 0, "f8"),
        term(Q(-1, 8), 0, "t", "z"),
        term(Q(-1, 16), 0, "q", "v"),
        term(Q(-1, 4), 0, "r", "r"),
    )
    g15_before_c14_kill = desk.la_substitute(g[15], after_first)
    expected_g15_before_c14_kill = add(
        term(Q(-1, 4), -3, "c14"),
        term(Q(-3, 16), -2, "u", "u"),
        scale(Q(3, 4), shift(-1, mul(term(1, 0, "u"), delta8))),
        term(Q(1, 2), -1, "c8", "u"),
    )
    assert desk.la_negative(g15_before_c14_kill) == expected_g15_before_c14_kill
    c14_g14 = term(1, -1, "c14")
    c14_g15 = term(Q(-1, 4), -3, "c14")
    f1 = term(1, 2)
    mixed_c14_D15 = add(
        scale(-2, mul(desk.la_derivative(f1), c14_g14)),
        scale(-7, mul(f1, desk.la_derivative(c14_g14))),
    )
    assert mixed_c14_D15 == term(3, 0, "a_x", "c14")
    assert desk.la_operator(15, c14_g15) == term(-3, 0, "a_x", "c14")
    assert add(desk.la_operator(15, c14_g15), mixed_c14_D15) == {}

    g15 = desk.la_substitute(g15_before_c14_kill, {"c14": {}})
    expected_g15_polar = add(
        term(Q(-3, 16), -2, "u", "u"),
        scale(Q(3, 4), shift(-1, mul(term(1, 0, "u"), delta8))),
        term(Q(1, 2), -1, "c8", "u"),
    )
    assert desk.la_negative(g15) == expected_g15_polar
    d15 = scale(-1, desk.la_operator(15, expected_g15_polar))
    assert desk.la_mod_a(2, d15) == term(Q(3, 4), 1, "a_x", "u", "u")

    after_second = desk.la_substitute(g15, {"u": term(1, 1, "y")})
    assert desk.la_negative(after_second) == {}

    final_substitution = dict(prior_kills)
    final_substitution.update({
        "c14": {},
        "f7": add(
            scale(Q(1, 2), t),
            scale(Q(1, 8), mul(q, z)),
            scale(Q(1, 16), mul(r, v)),
            term(1, 2, "y"),
        ),
    })
    zero_constant_symbols = {f"f{weight}" for weight in range(9, 16)}

    def constant_jet(item):
        answer = {}
        jet_symbols = {"z", "v", "r", "q", "t", "y"} | {
            f"f{weight}" for weight in range(7, 16)}
        for (a_power, symbols), coefficient in item.items():
            if any(symbol in zero_constant_symbols for symbol in symbols):
                continue
            key = (0, tuple(sorted(f"{symbol}0" if symbol in jet_symbols else symbol
                                   for symbol in symbols)))
            answer[key] = answer.get(key, Q(0)) + coefficient * (-1 if a_power % 2 else 1)
            if not answer[key]:
                del answer[key]
        return answer

    lower_window_compatibilities = {}
    for weight in (13, 14, 15):
        specialized = desk.la_substitute(g[weight], final_substitution)
        assert desk.la_negative(specialized) == {}
        lower_window_compatibilities[f"G{weight}_X0"] = desk.la_encode(
            constant_jet(specialized))
    expected_low = {
        "G13_X0": add(
            term(Q(1, 2), 0, "c8", "q0"), term(Q(3, 4), 0, "f80", "q0"),
            term(Q(-3, 128), 0, "q0", "q0", "v0"),
            term(Q(-3, 16), 0, "q0", "r0", "r0"),
            term(Q(3, 16), 0, "t0", "t0"),
            term(Q(3, 4), 0, "t0", "y0")),
        "G14_X0": add(
            term(Q(1, 2), 0, "c8", "t0"), term(Q(3, 4), 0, "f80", "t0"),
            term(Q(-3, 16), 0, "q0", "q0", "r0"),
            term(Q(-3, 64), 0, "q0", "t0", "v0"),
            term(Q(-3, 16), 0, "r0", "r0", "t0"),
            term(Q(-3, 64), 0, "t0", "t0", "z0"),
            term(Q(3, 8), 0, "y0", "y0")),
        "G15_X0": add(
            term(Q(1, 2), 0, "c8", "y0"), term(Q(3, 4), 0, "f80", "y0"),
            term(Q(-1, 16), 0, "q0", "q0", "q0"),
            term(Q(-3, 8), 0, "q0", "r0", "t0"),
            term(Q(-3, 64), 0, "q0", "v0", "y0"),
            term(Q(-3, 16), 0, "r0", "r0", "y0"),
            term(Q(-3, 128), 0, "t0", "t0", "v0"),
            term(Q(-3, 32), 0, "t0", "y0", "z0"),
            term(Q(-3, 16), 0, "y0", "y0")),
    }
    for label, expected in expected_low.items():
        assert lower_window_compatibilities[label] == desk.la_encode(expected)
    return {
        "post_D13_prefix": {
            "F4": "V/16+Z^2/64+A^2*R",
            "F5": "R/2+Z*V/64+A^2*Q",
            "F6": "Q/2+R*Z/8+V^2/256+A^2*T",
            "killed_modes": ["c6", "c10"],
        },
        "Delta7": "F7-T/2-Q*Z/8-R*V/16",
        "g14_polar": desk.la_encode(expected_g14_polar),
        "D14_square_raw_mod_A2": desk.la_encode(expected_d14_mod_a2),
        "D14_first_conclusion": "Delta7=A*U",
        "g14_polar_after_first_divisibility": desk.la_encode(term(1, -1, "c14")),
        "D14_second_conclusion": "c14=0 by the exact raw G14 polynomial window",
        "c14_operator_identity": "L14(c14/A)=0; it is a rational homogeneous mode, not a polynomial raw kernel",
        "Delta8": "F8-T*Z/8-Q*V/16-R^2/4",
        "g15_polar_before_c14_kill": desk.la_encode(expected_g15_before_c14_kill),
        "D15_c14_same_row_piece": desk.la_encode(desk.la_operator(15, c14_g15)),
        "D15_c14_predecessor_mixed_piece": desk.la_encode(mixed_c14_D15),
        "D15_c14_total": [],
        "D15_c14_causal_firewall": "the two pieces cancel; D15 does not independently constrain c14",
        "g15_polar_after_c14_kill": desk.la_encode(expected_g15_polar),
        "D15_raw_mod_A2": desk.la_encode(desk.la_mod_a(2, d15)),
        "D15_conclusion": "U=A*Y",
        "combined_conclusion": "F7=T/2+Q*Z/8+R*V/16+A^2*Y and c14=0",
        "D15_remaining_polar_after_second_divisibility": [],
        "surviving_c8_term": "c8*Y/2 is polynomial after U=A*Y; D15 does not kill c8",
        "positive_lower_window_compatibilities": lower_window_compatibilities,
        "gauge_invariant_low_jet_parameter": "H0=c8/2+3*F8(0)/4",
        "factored_low_window_equations": {
            "C13": "q0*H0-3*q0^2*v0/128-3*q0*r0^2/16+3*t0^2/16+3*t0*y0/4=0",
            "C14": "t0*H0-3*q0^2*r0/16-3*q0*t0*v0/64-3*r0^2*t0/16-3*t0^2*z0/64+3*y0^2/8=0",
            "C15": "y0*H0-q0^3/16-3*q0*r0*t0/8-3*q0*v0*y0/64-3*r0^2*y0/16-3*t0^2*v0/128-3*t0*y0*z0/32-3*y0^2/16=0",
        },
        "complete_modes_D14": [
            "c4*F10", "c6=0", "c8*T/2", "c10=0", "c12*(F^0)_2=0", "c14/A"
        ],
        "complete_modes_D15": [
            "c4*F11", "c6=0", "c8*(U/(2A)+holomorphic)", "c10=0",
            "c12*(F^0)_3=0", "c14*(-1/(4A^3))=0 after D14"
        ],
    }


def rational_rank(matrix):
    work = [list(row) for row in matrix if any(row)]
    if not work:
        return 0
    rows, columns = len(work), len(work[0])
    pivot_row = 0
    for column in range(columns):
        pivot = next((row for row in range(pivot_row, rows)
                      if work[row][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        factor = work[pivot_row][column]
        work[pivot_row] = [value / factor for value in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [left - factor * right
                         for left, right in zip(work[row], work[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def literal_g14_kernel(desk, raw):
    window = raw["windows"]["G"]["14"]
    row_generators = [(index, generator) for index, generator in enumerate(raw["generators"])
                      if int(generator["row"]) == 14]
    columns = []
    column_provenance = []
    for degree, slot in zip(range(window["lower"], window["upper"] + 1),
                            window["slots"]):
        values = {slot: Q(1)}
        direct, serialized = desk.assert_all_513(raw, values)
        vector = [serialized[index] for index, _ in row_generators]
        columns.append(vector)
        column_provenance.append({
            "G14_degree": degree,
            "slot": slot,
            "literal_D14": desk.xp_encode(direct[14]),
        })
    matrix = [[columns[column][row] for column in range(len(columns))]
              for row in range(len(row_generators))]
    rank = rational_rank(matrix)
    assert rank == len(columns) == 10
    return {
        "raw_G14_window": {"lower": window["lower"], "upper": window["upper"],
                           "slots": window["slots"]},
        "D14_row_sha256": raw["per_row"]["14"]["row_sha256"],
        "D14_generator_indices_zero_based": [index for index, _ in row_generators],
        "matrix_shape": [len(matrix), len(columns)],
        "rank": rank,
        "nullity": len(columns) - rank,
        "conclusion": "no polynomial raw G14 homogeneous kernel can realize or cancel c14/A",
        "columns": column_provenance,
    }


def execute_mutation(desk, raw, assignments, row, expected, prior):
    values = {}
    for kind, weight, polynomial in assignments:
        desk.put_window(raw, values, kind, weight, polynomial)
    direct, serialized = desk.assert_all_513(raw, values)
    assert all(not direct[weight] for weight in prior)
    assert direct[row] == expected
    return {
        "first_residual_row": row,
        "prior_rows_zero": list(prior),
        "residual": desk.xp_encode(expected),
        "literal_row_provenance": desk.row_provenance(raw, serialized, row),
        "all_513_generators_match_independent_determinant_recurrence": True,
    }


def literal_mutations(desk, raw):
    A = [Q(-1), Q(0), Q(0), Q(0), Q(1)]
    X = [Q(0), Q(1)]
    A_x = desk.xp_derivative(A)
    A2, A3, A4 = (desk.xp_power(A, exponent) for exponent in (2, 3, 4))

    def d14_assign(scalar):
        return [
            ("F", 7, [scalar]),
            ("G", 7, desk.xp_scale(Q(3, 2) * scalar, A2)),
            ("G", 8, [Q(3, 4) * scalar]),
        ]

    def d15_assign(scalar):
        u = desk.xp_scale(scalar, X)
        return [
            ("F", 7, desk.xp_mul(A, u)),
            ("G", 7, desk.xp_scale(Q(3, 2), desk.xp_mul(A3, u))),
            ("G", 8, desk.xp_scale(Q(3, 4), desk.xp_mul(A, u))),
            ("G", 14, desk.xp_scale(Q(3, 8), desk.xp_mul(u, u))),
        ]

    d14_unit = desk.xp_scale(-3, desk.xp_mul(A, A_x))
    d15_unit = desk.xp_add(
        desk.xp_scale(Q(3, 4), desk.xp_mul(desk.xp_mul(A, A_x),
                                          desk.xp_mul(X, X))),
        desk.xp_scale(-3, desk.xp_mul(A2, X)),
    )
    answer = {
        "D14_Delta7_square": execute_mutation(
            desk, raw, d14_assign(Q(1)), 14, d14_unit, range(4, 14)),
        "D15_second_square": execute_mutation(
            desk, raw, d15_assign(Q(1)), 15, d15_unit, range(4, 15)),
    }
    for label, recipe, row, unit, prior in (
            ("D14_Delta7_square", d14_assign, 14, d14_unit, range(4, 14)),
            ("D15_second_square", d15_assign, 15, d15_unit, range(4, 15))):
        answer[label]["scaling_power"] = 2
        answer[label]["live_scaling_mutations"] = {}
        for scalar in (Q(-1), Q(2)):
            replay = execute_mutation(
                desk, raw, recipe(scalar), row,
                desk.xp_scale(scalar * scalar, unit), prior)
            answer[label]["live_scaling_mutations"][str(scalar)] = replay["residual"]

    # A literal polynomial continuation with nonzero c8 proves the D15 c8
    # term survives rather than being silently normalized or killed.
    c8_values = {}
    desk.put_window(raw, c8_values, "F", 7, desk.xp_mul(A2, X))
    desk.put_window(raw, c8_values, "G", 7,
                    desk.xp_scale(Q(3, 2), desk.xp_mul(A4, X)))
    desk.put_window(raw, c8_values, "G", 8,
                    desk.xp_add(desk.xp_scale(Q(3, 4), desk.xp_mul(A2, X)), A2))
    desk.put_window(raw, c8_values, "G", 9, [Q(1, 2)])
    desk.put_window(raw, c8_values, "G", 14,
                    desk.xp_scale(Q(3, 8), desk.xp_mul(A2, desk.xp_mul(X, X))))
    desk.put_window(raw, c8_values, "G", 15,
                    desk.xp_add(desk.xp_scale(Q(-3, 16), desk.xp_mul(X, X)),
                                desk.xp_scale(Q(1, 2), X)))
    direct_c8, serialized_c8 = desk.assert_all_513(raw, c8_values)
    assert all(not direct_c8[weight] for weight in range(4, 16))
    answer["D15_c8_survival"] = {
        "assignment": "F=(A^2+t/2)^2+A^2*X*t^7; G=F^(3/2)+t^8*F^(1/2) through G15",
        "mode": "c8=1",
        "rows_D4_through_D15": "zero",
        "all_513_generators_match_direct_recurrence": True,
        "folded_D22_generator_value": str(serialized_c8[495]),
        "conclusion": "D15 does not kill c8",
    }
    answer["c14_birth_laurent_mutations"] = {
        "birth_pole": "c14/A",
        "cleared_numerator_A_times_pole": {
            "c14=-1": "-1", "c14=1": "1", "c14=2": "2"
        },
        "next_row_if_not_killed": "-c14/(4*A^3)",
        "D15_predecessor_mixed_piece": "+3*c14*A'",
        "D15_same_row_piece": "-3*c14*A'",
        "D15_correction": "RETRACTED standalone image: predecessor mixed +3*c14*A' cancels same-row -3*c14*A'",
        "D14_and_D15_row_sha256": [raw["per_row"]["14"]["row_sha256"],
                                        raw["per_row"]["15"]["row_sha256"]],
        "source_window_crosscheck": "see literal_G14_polynomial_kernel rank/nullity certificate",
    }
    gauge_replays = {}
    for scalar in (Q(-1), Q(1), Q(2)):
        values = {}
        desk.put_window(raw, values, "F", 8, [scalar])
        rows, serialized = desk.assert_all_513(raw, values)
        assert all(not rows[weight] for weight in range(4, 23))
        gauge_replays[str(scalar)] = {
            "folded_D22_generator_value": str(serialized[495]),
            "characteristic_c8": str(Q(-3, 2) * scalar),
            "H0": "0",
        }
    answer["F8_constant_gauge_invariance"] = {
        "live_scalars": gauge_replays,
        "transformation": "F8(0)->F8(0)+lambda, c8->c8-3lambda/2",
        "fixed_combination": "H0=c8/2+3F8(0)/4",
        "all_D4_through_D22_zero_before_affine_target_fold": True,
    }
    return answer


def calculate_result():
    assert digest(RAW) == RAW_SHA256
    _, desk = load_dependencies()
    raw = json.loads(RAW.read_text())
    assert raw["variable_count"] == 303
    assert raw["generator_count"] == len(raw["generators"]) == 513
    calculation = characteristic_calculation(desk)
    modes = []
    for birth, exponent in desk.MODES.items():
        modes.append({
            "birth_weight": birth,
            "F_exponent": str(exponent),
            "birth_A_power": int(4 * exponent),
            "support_at_D14": birth <= 14,
            "support_at_D15": birth <= 15,
            "role": "free_polynomial" if birth <= 12 else "forced_rational",
            "continuation_status": "retained_mandatory",
        })
    return {
        "schema": "jc2.ggv.upper_endpoint.uniform_d14_d15_fullmodes.result.v1",
        "status": "PASS_EXACT_FIELD_POINT_A_ADIC_CASCADE_THROUGH_D15",
        "source": {
            "authoritative_raw_system": str(RAW.relative_to(ROOT)),
            "authoritative_raw_system_sha256": RAW_SHA256,
            "predecessor_checker": str(PREDECESSOR.relative_to(ROOT)),
            "predecessor_checker_sha256": PREDECESSOR_SHA256,
            "predecessor_result": str(PREDECESSOR_RESULT.relative_to(ROOT)),
            "predecessor_result_sha256": PREDECESSOR_RESULT_SHA256,
            "raw_variable_count": 303,
            "raw_generator_count": 513,
        },
        "complete_mode_schedule": modes,
        "calculation": calculation,
        "literal_G14_polynomial_kernel": literal_g14_kernel(desk, raw),
        "literal_raw_mutations": literal_mutations(desk, raw),
        "theorems": {
            "D14": {
                "defect": calculation["Delta7"],
                "first_conclusion": "A divides Delta7 at field points",
                "second_conclusion": "c14=0",
                "causal_order": "the A^-2 square cannot be canceled by c14/A; after Delta7=A*U, c14/A is the sole pole",
                "successor_firewall": "D15 does not kill c14: its predecessor mixed +3*c14*A' cancels its same-row -3*c14*A' exactly",
            },
            "D15": {
                "after_D14": "Delta7=A*U and c14=0",
                "conclusion": calculation["combined_conclusion"],
                "c8_status": "survives; its c8*U/(2A) term becomes polynomial after U=A*Y",
                "new_A_adic_branch_invariant": "none",
                "new_positive_lower_window_invariants": ["C14=0", "C15=0"],
            },
            "positive_lower_window_core": {
                "live_equations": calculation["factored_low_window_equations"],
                "gauge_invariant_parameter": calculation["gauge_invariant_low_jet_parameter"],
                "status": "exact necessary scalar compatibilities; not eliminated or normalized",
            },
        },
        "scope_firewall": [
            "field-radical A-adic consequences only; no scheme divisibility",
            "the positive lower-window compatibility equations beginning at G13 are not claimed exhausted here",
            "c14 is derived to vanish on this cascade; c16,c18,c20 remain mandatory and unconstrained",
            "c8 is retained and source-replayed nonzero; no unit normalization is used",
            "no endpoint, Keller-pair, unrestricted branch-P, or JC2 conclusion",
            "standard-library exact arithmetic only; no CAS or AWS",
        ],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--dump", action="store_true")
    arguments = parser.parse_args()
    result = calculate_result()
    encoded = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    if arguments.write:
        RESULT.write_bytes(encoded)
    if arguments.check:
        assert RESULT.read_bytes() == encoded
    if arguments.dump:
        print(encoded.decode(), end="")
    else:
        print(json.dumps({
            "status": result["status"],
            "D14": result["theorems"]["D14"],
            "D15": result["theorems"]["D15"],
            "check": arguments.check,
        }, sort_keys=True))


if __name__ == "__main__":
    main()
