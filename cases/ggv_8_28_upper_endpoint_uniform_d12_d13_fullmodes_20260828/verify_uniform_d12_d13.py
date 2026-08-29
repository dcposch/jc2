#!/usr/bin/env python3
"""Exact full-mode continuation of the uniform branch-P cascade through D13."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PREDECESSOR = (ROOT / "cases/ggv_8_28_upper_endpoint_uniform_d10_fullmodes_audit_20260828"
               / "verify_uniform_d10.py")
PREDECESSOR_RESULT = PREDECESSOR.with_name("RESULT.json")
RAW = ROOT / "cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json"
RESULT = HERE / "RESULT.json"

PREDECESSOR_SHA256 = "8ebe5f4f099e6cf15b0a4703dfb348aa6cc72df8fdbc60b1d095925fa3746d21"
PREDECESSOR_RESULT_SHA256 = "8ff338bdd47b7a53ba1515a7889823620120f92d718a03349fb9e3fd27014236"
RAW_SHA256 = "ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_predecessor():
    assert digest(PREDECESSOR) == PREDECESSOR_SHA256
    assert digest(PREDECESSOR_RESULT) == PREDECESSOR_RESULT_SHA256
    specification = importlib.util.spec_from_file_location("uniform_d10_frozen", PREDECESSOR)
    assert specification is not None and specification.loader is not None
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    module.DERIVATIVES.update({"s": "s_x", "t": "t_x", "f12": "f12_x", "f13": "f13_x"})
    return module


def characteristic_calculation(desk):
    term, add, scale, mul, shift = (
        desk.la_term, desk.la_add, desk.la_scale, desk.la_mul, desk.la_shift)
    z, v, r, q = (term(1, 0, name) for name in ("z", "v", "r", "q"))
    F = desk.common_F_prefix()
    F[4] = add(scale(Q(1, 16), v), scale(Q(1, 64), mul(z, z)),
               mul(term(1, 2), r))
    F[5] = add(scale(Q(1, 2), r), scale(Q(1, 64), mul(z, v)),
               mul(term(1, 2), q))
    for weight in range(6, 14):
        F[weight] = term(1, 0, f"f{weight}")
    _, g = desk.continuation(F, 13)

    killed = {"c6": {}, "c10": {}}
    delta6 = add(
        term(1, 0, "f6"),
        term(Q(-1, 2), 0, "q"),
        term(Q(-1, 8), 0, "r", "z"),
        term(Q(-1, 256), 0, "v", "v"),
    )
    g12 = desk.la_substitute(g[12], killed)
    expected_g12_polar = scale(Q(3, 8), shift(-2, mul(delta6, delta6)))
    assert desk.la_negative(g12) == expected_g12_polar
    d12 = scale(-1, desk.la_operator(12, expected_g12_polar))
    expected_d12_mod_a2 = scale(
        -6, mul(term(1, 1, "a_x"), mul(delta6, delta6)))
    assert desk.la_mod_a(2, d12) == expected_d12_mod_a2

    after_d12 = dict(killed)
    after_d12["f6"] = add(
        scale(Q(1, 2), q),
        scale(Q(1, 8), mul(r, z)),
        scale(Q(1, 256), mul(v, v)),
        term(1, 1, "s"),
    )
    g13 = desk.la_substitute(g[13], after_d12)
    delta7 = add(
        term(1, 0, "f7"),
        term(Q(-1, 8), 0, "q", "z"),
        term(Q(-1, 16), 0, "r", "v"),
    )
    expected_g13_polar = add(
        term(Q(-3, 16), -2, "s", "s"),
        scale(Q(3, 4), shift(-1, mul(term(1, 0, "s"), delta7))),
    )
    assert desk.la_negative(g13) == expected_g13_polar
    d13 = scale(-1, desk.la_operator(13, expected_g13_polar))
    assert desk.la_mod_a(2, d13) == term(Q(9, 4), 1, "a_x", "s", "s")

    after_second_divisibility = desk.la_substitute(g13, {"s": term(1, 1, "t")})
    assert desk.la_negative(after_second_divisibility) == {}

    return {
        "post_D11_prefix": {
            "F4": "V/16+Z^2/64+A^2*R",
            "F5": "R/2+Z*V/64+A^2*Q",
            "killed_modes": ["c6", "c10"],
        },
        "Delta6": "F6-Q/2-R*Z/8-V^2/256",
        "g12_polar": desk.la_encode(expected_g12_polar),
        "D12_raw_mod_A2": desk.la_encode(expected_d12_mod_a2),
        "D12_conclusion": "Delta6=A*S",
        "D12_extra_mode_kill": "none",
        "Delta7": "F7-Q*Z/8-R*V/16",
        "g13_polar_after_D12": desk.la_encode(expected_g13_polar),
        "D13_raw_mod_A2": desk.la_encode(desk.la_mod_a(2, d13)),
        "D13_conclusion": "S=A*T",
        "combined_conclusion": "F6=Q/2+R*Z/8+V^2/256+A^2*T",
        "D13_remaining_polar_after_second_divisibility": [],
        "D13_extra_mode_kill": "none; c12 is the exact additive G12 constant gauge",
        "complete_modes_D12": [
            "c4*F8", "c6=0", "c8*R/2", "c10=0", "c12"
        ],
        "complete_modes_D13": [
            "c4*F9", "c6=0", "c8*Q/2", "c10=0", "c12*(F^0)_1=0"
        ],
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
    A_x = desk.xp_derivative(A)
    A2, A3 = desk.xp_power(A, 2), desk.xp_power(A, 3)

    def d12_assign(scalar):
        return [
            ("F", 6, [scalar]),
            ("G", 6, desk.xp_scale(Q(3, 2) * scalar, A2)),
            ("G", 7, [Q(3, 4) * scalar]),
        ]

    def d13_assign(scalar):
        return [
            ("F", 6, desk.xp_scale(scalar, A)),
            ("G", 6, desk.xp_scale(Q(3, 2) * scalar, A3)),
            ("G", 7, desk.xp_scale(Q(3, 4) * scalar, A)),
            ("G", 12, [Q(3, 8) * scalar * scalar]),
        ]

    d12_unit = desk.xp_scale(-6, desk.xp_mul(A, A_x))
    d13_unit = desk.xp_scale(Q(9, 4), desk.xp_mul(A, A_x))
    answer = {
        "D12_Delta6_square": execute_mutation(
            desk, raw, d12_assign(Q(1)), 12, d12_unit, range(4, 12)),
        "D13_second_square": execute_mutation(
            desk, raw, d13_assign(Q(1)), 13, d13_unit, range(4, 13)),
    }
    for label, recipe, row, unit, prior in (
            ("D12_Delta6_square", d12_assign, 12, d12_unit, range(4, 12)),
            ("D13_second_square", d13_assign, 13, d13_unit, range(4, 13))):
        answer[label]["scaling_power"] = 2
        answer[label]["live_scaling_mutations"] = {}
        for scalar in (Q(-1), Q(2)):
            replay = execute_mutation(
                desk, raw, recipe(scalar), row,
                desk.xp_scale(scalar * scalar, unit), prior)
            answer[label]["live_scaling_mutations"][str(scalar)] = replay["residual"]

    gauge_values = {}
    desk.put_window(raw, gauge_values, "G", 12, [Q(1)])
    gauge_rows, gauge_serialized = desk.assert_all_513(raw, gauge_values)
    assert all(not gauge_rows[weight] for weight in range(4, 23))
    answer["c12_additive_gauge"] = {
        "assignment": "G12[X^0]=c12=1; every other raw variable zero",
        "all_D4_through_D22_zero_before_affine_target_fold": True,
        "folded_D22_generator_value": str(gauge_serialized[495]),
        "conclusion": "c12 is a global additive gauge and must not be killed",
    }

    # Literal regression for every term in Delta6.  Choose Z=V=1 and
    # R=Q=X so that the exact square respects all later raw lower windows.
    X = [Q(0), Q(1)]
    Sroot = {
        0: A2, 1: [Q(1, 2)], 2: [Q(1, 8)], 3: [Q(1, 16)],
        4: desk.xp_scale(Q(1, 2), X), 5: desk.xp_scale(Q(1, 2), X),
    }
    square_F = desk.t_series_multiply(Sroot, Sroot, 14)
    square_G = desk.t_series_multiply(
        desk.t_series_multiply(Sroot, Sroot, 21), Sroot, 21)
    exact_values = {"z_0": Q(1), "tt_0": Q(-1), "tt_4": Q(1)}
    for weight in range(4, 15):
        desk.put_window(raw, exact_values, "F", weight, square_F[weight])
    for weight in range(4, 22):
        desk.put_window(raw, exact_values, "G", weight, square_G[weight])
    exact_rows, _ = desk.assert_all_513(raw, exact_values)
    assert all(not exact_rows[weight] for weight in range(4, 23))
    required_f6 = [Q(1, 256), Q(5, 8)]
    assert square_F[6] == required_f6

    omitted_values = dict(exact_values)
    desk.put_window(raw, omitted_values, "F", 6, [])
    defect = desk.xp_scale(-1, required_f6)
    for offset in range(6):
        weight = 6 + offset
        adjusted = desk.xp_add(
            square_G[weight],
            desk.xp_scale(Q(3, 2), desk.xp_mul(defect, Sroot[offset])))
        desk.put_window(raw, omitted_values, "G", weight, adjusted)
    omitted_rows, omitted_serialized = desk.assert_all_513(raw, omitted_values)
    assert all(not omitted_rows[weight] for weight in range(4, 12))
    omitted_expected = desk.xp_add(
        desk.xp_scale(-6, desk.xp_mul(desk.xp_mul(A, A_x),
                                     desk.xp_mul(defect, defect))),
        desk.xp_scale(6, desk.xp_mul(A2, desk.xp_mul(defect,
                                                    desk.xp_derivative(defect)))),
    )
    assert omitted_rows[12] == omitted_expected
    answer["Delta6_all_terms_regression"] = {
        "exact_square_assignment": "Z=V=1,R=Q=X in S=A^2+t/2+t^2/8+t^3/16+(X/2)t^4+(X/2)t^5",
        "required_literal_F6": "1/256+(5/8)X=Q/2+R*Z/8+V^2/256",
        "mutation": "set F6=0 and continue F^(3/2) through G11",
        "mutation_rows_D4_through_D11": "zero",
        "mutation_D12": desk.xp_encode(omitted_expected),
        "literal_row_provenance": desk.row_provenance(raw, omitted_serialized, 12),
        "conclusion": "dropping any part of the complete Delta6 correction is detected",
    }
    return answer


def calculate_result():
    assert digest(RAW) == RAW_SHA256
    desk = load_predecessor()
    raw = json.loads(RAW.read_text())
    assert raw["variable_count"] == 303
    assert raw["generator_count"] == len(raw["generators"]) == 513
    modes = []
    for birth, exponent in desk.MODES.items():
        modes.append({
            "birth_weight": birth,
            "F_exponent": str(exponent),
            "birth_A_power": int(4 * exponent),
            "role": "free_polynomial" if birth <= 12 else "forced_rational",
            "support_at_D12": birth <= 12,
            "support_at_D13": birth <= 13,
            "continuation_status": "retained_mandatory",
        })
    assert [item["birth_A_power"] for item in modes] == [4, 3, 2, 1, 0, -1, -2, -3, -4]
    calculation = characteristic_calculation(desk)
    return {
        "schema": "jc2.ggv.upper_endpoint.uniform_d12_d13_fullmodes.result.v1",
        "status": "PASS_EXACT_FIELD_POINT_CASCADE_THROUGH_D13",
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
        "literal_raw_mutations": literal_mutations(desk, raw),
        "theorems": {
            "D12": {
                "defect": calculation["Delta6"],
                "raw_congruence": "D12=-6*A*A'*Delta6^2 mod A^2",
                "conclusion": "A divides Delta6 at field points",
                "extra_mode_kill": "none",
            },
            "D13": {
                "after_D12": "Delta6=A*S",
                "raw_congruence": "D13=+(9/4)*A*A'*S^2 mod A^2",
                "conclusion": calculation["combined_conclusion"],
                "extra_mode_kill": "none",
                "c12_status": "global additive G12[X^0] gauge, source-replayed",
            },
        },
        "scope_firewall": [
            "field-radical prefix only; no scheme-theoretic divisibility",
            "c12 is retained as an exact additive gauge, not killed",
            "c14,c16,c18,c20 remain mandatory forced rational modes",
            "no claim beyond D13 and no endpoint, Keller-pair, or JC2 conclusion",
            "standard-library exact rational arithmetic only; no CAS or AWS",
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
            "D12": result["theorems"]["D12"]["conclusion"],
            "D13": result["theorems"]["D13"]["conclusion"],
            "check": arguments.check,
        }, sort_keys=True))


if __name__ == "__main__":
    main()
