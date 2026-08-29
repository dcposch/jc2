#!/usr/bin/env python3
"""Exact full-mode continuation of the uniform branch-P cascade to D17."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PREDECESSOR = (ROOT / "cases/ggv_8_28_upper_endpoint_uniform_d14_d15_fullmodes_20260828"
               / "verify_uniform_d14_d15.py")
PREDECESSOR_RESULT = PREDECESSOR.with_name("RESULT.json")
RAW = ROOT / "cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json"
RESULT = HERE / "RESULT.json"
PREDECESSOR_SHA256 = "53f2a7a276be4a0aa7f77cc031e270d573fc78b5db64cdb76a0cf6c502e52517"
PREDECESSOR_RESULT_SHA256 = "7546618aa5a40ed983014159c1d39337396607562912570c97cfe2ee779394ea"
RAW_SHA256 = "ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_dependencies():
    assert digest(PREDECESSOR) == PREDECESSOR_SHA256
    assert digest(PREDECESSOR_RESULT) == PREDECESSOR_RESULT_SHA256
    spec = importlib.util.spec_from_file_location("uniform_d14_frozen", PREDECESSOR)
    assert spec is not None and spec.loader is not None
    prior = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(prior)
    assert prior.calculate_result()["status"] == "PASS_EXACT_FIELD_POINT_A_ADIC_CASCADE_THROUGH_D15"
    _, desk = prior.load_dependencies()
    desk.DERIVATIVES.update({
        "b": "b_x", "m": "m_x", "f16": "f16_x", "f17": "f17_x",
    })
    return prior, desk


def characteristic_calculation(desk):
    term, add, scale, mul, shift = (
        desk.la_term, desk.la_add, desk.la_scale, desk.la_mul, desk.la_shift)
    z, v, r, q, t, y = (term(1, 0, name)
                         for name in ("z", "v", "r", "q", "t", "y"))
    F = desk.common_F_prefix()
    F[4] = add(scale(Q(1, 16), v), scale(Q(1, 64), mul(z, z)), term(1, 2, "r"))
    F[5] = add(scale(Q(1, 2), r), scale(Q(1, 64), mul(z, v)), term(1, 2, "q"))
    F[6] = add(scale(Q(1, 2), q), scale(Q(1, 8), mul(r, z)),
               scale(Q(1, 256), mul(v, v)), term(1, 2, "t"))
    F[7] = add(scale(Q(1, 2), t), scale(Q(1, 8), mul(q, z)),
               scale(Q(1, 16), mul(r, v)), term(1, 2, "y"))
    for weight in range(8, 15):
        F[weight] = term(1, 0, f"f{weight}")
    for weight in range(15, 18):
        F[weight] = {}
    _, g = desk.continuation(F, 17)

    kills = {"c6": {}, "c10": {}, "c14": {}}
    base8 = add(scale(Q(1, 2), y), scale(Q(1, 8), mul(t, z)),
                scale(Q(1, 16), mul(q, v)), scale(Q(1, 4), mul(r, r)))
    B = add(term(1, 0, "f8"), scale(-1, base8))
    g16 = desk.la_substitute(g[16], kills)
    numerator16 = add(
        scale(Q(3, 8), mul(B, B)),
        scale(Q(1, 2), mul(term(1, 0, "c8"), B)),
        term(1, 0, "c16"),
    )
    expected_g16_polar = shift(-2, numerator16)
    assert desk.la_negative(g16) == expected_g16_polar

    d16_same_row = scale(-1, desk.la_operator(16, expected_g16_polar))
    # The forced c16 direction is exact homogeneous: it drops from the raw
    # operator, while the numerator derivative remains visible at A^2.
    assert desk.la_mod_a(3, d16_same_row) == scale(
        8, shift(2, desk.la_derivative(numerator16)))

    relation16 = {
        "c16": add(term(1, 2, "m"), scale(Q(-3, 8), mul(term(1, 0, "b"),
                                                                  term(1, 0, "b"))),
                     scale(Q(-1, 2), mul(term(1, 0, "c8"), term(1, 0, "b")))),
        "f8": add(base8, term(1, 0, "b")),
    }
    g16_after = desk.la_substitute(g16, relation16)
    assert desk.la_negative(g16_after) == {}

    before_relation17 = dict(kills)
    before_relation17["f8"] = add(base8, term(1, 0, "b"))
    g17_before_relation16 = desk.la_substitute(g[17], before_relation17)
    base9 = add(scale(Q(1, 2), mul(q, r)), scale(Q(1, 16), mul(t, v)),
                scale(Q(1, 8), mul(y, z)))
    C = add(term(1, 0, "f9"), scale(-1, base9))
    expected_g17_before_relation16 = add(
        scale(Q(-1, 2), shift(-4, add(
            scale(Q(3, 8), mul(term(1, 0, "b"), term(1, 0, "b"))),
            scale(Q(1, 2), mul(term(1, 0, "c8"), term(1, 0, "b"))),
            term(1, 0, "c16"),
        ))),
        shift(-2, mul(add(scale(Q(3, 4), term(1, 0, "b")),
                          scale(Q(1, 2), term(1, 0, "c8"))), C)),
    )
    assert desk.la_negative(g17_before_relation16) == expected_g17_before_relation16
    # Causal firewall for the born indicial mode.  If one illegally retained
    # c16/A^2 without satisfying the raw G16 polynomial window, its linked
    # D17 predecessor and same-row pieces would cancel exactly.  Therefore
    # c16 is fixed by D16 polynomiality, never by a successor-row kill.
    c16_g16 = term(1, -2, "c16")
    c16_g17 = term(Q(-1, 2), -4, "c16")
    f1 = term(1, 2)
    c16_predecessor_mixed = add(
        scale(-4, mul(desk.la_derivative(f1), c16_g16)),
        scale(-7, mul(f1, desk.la_derivative(c16_g16))),
    )
    c16_same_row = desk.la_operator(17, c16_g17)
    assert c16_predecessor_mixed == term(6, -1, "a_x", "c16")
    assert c16_same_row == term(-6, -1, "a_x", "c16")
    assert add(c16_predecessor_mixed, c16_same_row) == {}
    g17_after = desk.la_substitute(desk.la_substitute(g[17], kills), relation16)
    obstruction17 = add(
        scale(Q(3, 4), mul(term(1, 0, "b"), C)),
        scale(Q(1, 2), mul(term(1, 0, "c8"), C)),
        term(Q(-1, 2), 0, "m"),
    )
    expected_g17_polar = shift(-2, obstruction17)
    assert desk.la_negative(g17_after) == expected_g17_polar
    d17 = scale(-1, desk.la_operator(17, expected_g17_polar))
    assert desk.la_mod_a(2, d17) == scale(
        4, mul(term(1, 1, "a_x"), obstruction17))
    desk.DERIVATIVES["ell"] = "ell_x"
    first_stage = scale(-1, desk.la_operator(17, term(1, -1, "ell")))
    assert desk.la_mod_a(3, first_stage) == term(12, 2, "a_x", "ell")

    relation17 = {
        "f9": add(base9, term(1, 0, "d")),
        "m": add(
            scale(Q(3, 2), mul(term(1, 0, "b"), term(1, 0, "d"))),
            mul(term(1, 0, "c8"), term(1, 0, "d")),
            scale(-2, term(1, 2, "n")),
        ),
    }
    desk.DERIVATIVES.update({"d": "d_x", "n": "n_x"})
    g17_polynomial = desk.la_substitute(g17_after, relation17)
    assert desk.la_negative(g17_polynomial) == {}

    constants = {f"c{birth}" for birth in desk.MODES}
    lower_bounds = {8: 0, 9: 1, 10: 1, 11: 1, 12: 2, 13: 2, 14: 2}

    def jet_symbol(symbol, order):
        if symbol in constants:
            return symbol if order == 0 else None
        if symbol.startswith("f") and symbol[1:].isdigit():
            weight = int(symbol[1:])
            if lower_bounds.get(weight, 0) > order:
                return None
        return f"{symbol}{order}"

    def low_jets(item):
        outputs = [{}, {}]
        for (a_power, symbols), coefficient in item.items():
            sign = -1 if a_power % 2 else 1
            constant_symbols = [jet_symbol(symbol, 0) for symbol in symbols]
            if all(symbol is not None for symbol in constant_symbols):
                key = (0, tuple(sorted(constant_symbols)))
                outputs[0][key] = outputs[0].get(key, Q(0)) + sign * coefficient
            for position, symbol in enumerate(symbols):
                linear_symbol = jet_symbol(symbol, 1)
                if linear_symbol is None:
                    continue
                factors = []
                valid = True
                for other_position, other_symbol in enumerate(symbols):
                    value = linear_symbol if other_position == position else jet_symbol(other_symbol, 0)
                    if value is None:
                        valid = False
                        break
                    factors.append(value)
                if valid:
                    key = (0, tuple(sorted(factors)))
                    outputs[1][key] = outputs[1].get(key, Q(0)) + sign * coefficient
        return [{key: value for key, value in output.items() if value} for output in outputs]

    g16_jets = low_jets(g16_after)
    g17_jets = low_jets(g17_polynomial)

    # Gauge-centering identities, checked as exact scalar polynomial algebra.
    # Bhat=B+2c8/3 and J16=c16-c8^2/6 are fixed by the additive F8 gauge.
    lam = term(1, 0, "lambda")
    centered_before = add(term(1, 0, "b"), scale(Q(2, 3), term(1, 0, "c8")))
    centered_after = add(term(1, 0, "b"), lam,
                         scale(Q(2, 3), add(term(1, 0, "c8"), scale(Q(-3, 2), lam))))
    assert centered_before == centered_after
    j_before = add(term(1, 0, "c16"), scale(Q(-1, 6), term(1, 0, "c8", "c8")))
    c8_after = add(term(1, 0, "c8"), scale(Q(-3, 2), lam))
    c16_after = add(term(1, 0, "c16"),
                    scale(Q(-1, 2), mul(term(1, 0, "c8"), lam)),
                    scale(Q(3, 8), mul(lam, lam)))
    j_after = add(c16_after, scale(Q(-1, 6), mul(c8_after, c8_after)))
    assert j_before == j_after
    assert add(scale(3, centered_before),
               scale(-1, add(scale(3, term(1, 0, "b")),
                             scale(2, term(1, 0, "c8"))))) == {}
    return {
        "Delta8": "B=F8-Y/2-T*Z/8-Q*V/16-R^2/4",
        "g16_polar": desk.la_encode(expected_g16_polar),
        "D16_same_row_mod_A3": desk.la_encode(desk.la_mod_a(3, d16_same_row)),
        "D16_polynomiality_relation": "3*B^2+4*c8*B+8*c16=8*A^2*M",
        "D16_c16_uniqueness": "if it exists, c16 is unique because a nonzero scalar cannot lie in (A^2)",
        "Delta9": "C=F9-Q*R/2-T*V/16-Y*Z/8",
        "g17_polar_before_D16_relation": desk.la_encode(
            expected_g17_before_relation16),
        "D17_linked_c16_identity": (
            "g17_polar=-(3*B^2/8+c8*B/2+c16)/(2*A^4)"
            "+(3*B/4+c8/2)*C/A^2; the D16 numerator relation converts "
            "the full A^-4 block, including c16, to -M/(2*A^2)"
        ),
        "D17_c16_causal_firewall": {
            "predecessor_mixed_piece": desk.la_encode(c16_predecessor_mixed),
            "same_row_piece": desk.la_encode(c16_same_row),
            "total": [],
            "conclusion": (
                "D17 does not kill a free c16; c16 is determined only by the "
                "D16 raw-polynomiality condition"
            ),
        },
        "g17_polar_after_D16_relation": desk.la_encode(expected_g17_polar),
        "D17_raw_mod_A2": desk.la_encode(desk.la_mod_a(2, d17)),
        "D17_first_stage": "obstruction17=A*ell",
        "D17_raw_mod_A3_after_first_stage": desk.la_encode(desk.la_mod_a(3, first_stage)),
        "D17_polynomiality_relation": "(3*B+2*c8)*C-2*M=4*A^2*N",
        "D17_uniform_invariant": "K17_uniform=(3*B+2*c8)*C-2*M",
        "D17_after_relation_negative": desk.la_encode(desk.la_negative(g17_polynomial)),
        "gauge_centering": {
            "Bhat": "B+2*c8/3",
            "J16": "c16-c8^2/6",
            "centered_D16_relation": "(3/8)*Bhat^2+J16=A^2*M",
            "gauge_action": (
                "B->B+lambda, c8->c8-3lambda/2, "
                "c12->c12-c4*lambda, "
                "c16->c16-c8*lambda/2+3lambda^2/8"
            ),
            "invariance_checked": True,
            "relation_to_H0": "Bhat(0)=4*H0/3-(Y/2+T*Z/8+Q*V/16+R^2/4)(0)",
            "rootwise_two_branch_core": [
                "at every alpha with A(alpha)=0: Bhat(alpha)^2=-8*J16/3",
                "at every alpha with A(alpha)=0: 3*Bhat(alpha)*C(alpha)=2*M(alpha)",
                "no square root or sign pattern is selected; branches coalesce when J16=0",
            ],
        },
        "positive_lower_window_jets": {
            "G16_X0": desk.la_encode(g16_jets[0]),
            "G16_X1": desk.la_encode(g16_jets[1]),
            "G17_X0": desk.la_encode(g17_jets[0]),
            "G17_X1": desk.la_encode(g17_jets[1]),
        },
    }


def rational_rank(matrix):
    work = [list(row) for row in matrix if any(row)]
    if not work:
        return 0
    row_count, column_count = len(work), len(work[0])
    pivot_row = 0
    for column in range(column_count):
        pivot = next((row for row in range(pivot_row, row_count)
                      if work[row][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][column]
        work[pivot_row] = [value / pivot_value for value in work[pivot_row]]
        for row in range(row_count):
            if row == pivot_row or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [left - factor * right
                         for left, right in zip(work[row], work[pivot_row])]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def literal_window_certificate(desk, raw, weight):
    """Pin the exact raw G_weight window and its map into literal D_weight."""
    window = raw["windows"]["G"][str(weight)]
    row_generators = [(index, generator)
                      for index, generator in enumerate(raw["generators"])
                      if int(generator["row"]) == weight]
    columns = []
    provenance = []
    for degree, slot in zip(range(window["lower"], window["upper"] + 1),
                            window["slots"]):
        direct, serialized = desk.assert_all_513(raw, {slot: Q(1)})
        vector = [serialized[index] for index, _ in row_generators]
        columns.append(vector)
        provenance.append({
            "G_degree": degree,
            "slot": slot,
            "literal_D_row": desk.xp_encode(direct[weight]),
        })
    matrix = [[columns[column][row] for column in range(len(columns))]
              for row in range(len(row_generators))]
    rank = rational_rank(matrix)
    assert rank == len(columns)
    return {
        "weight": weight,
        "raw_G_window": {
            "lower": window["lower"],
            "upper": window["upper"],
            "slots": window["slots"],
        },
        "literal_D_row_sha256": raw["per_row"][str(weight)]["row_sha256"],
        "literal_D_generator_indices_zero_based": [index for index, _ in row_generators],
        "matrix_shape": [len(matrix), len(columns)],
        "rank": rank,
        "nullity": len(columns) - rank,
        "conclusion": (
            "the displayed polynomial raw window is exact and has no homogeneous kernel; "
            "Laurent cancellation must occur before insertion into this window"
        ),
        "columns": provenance,
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
    A2 = desk.xp_power(A, 2)

    def d16_recipe(scalar):
        defect = desk.xp_scale(scalar, X)
        return [
            ("F", 8, defect),
            ("G", 8, desk.xp_scale(Q(3, 2), desk.xp_mul(A2, defect))),
            ("G", 9, desk.xp_scale(Q(3, 4), defect)),
        ]

    d16_unit = desk.xp_scale(6, desk.xp_mul(A2, X))
    d16 = execute_mutation(
        desk, raw, d16_recipe(Q(1)), 16, d16_unit, range(4, 16))
    d16["interpretation"] = (
        "B=X, c8=c16=0: omitting the Laurent G16 term 3*X^2/(8*A^2) "
        "creates the predicted D16 obstruction"
    )
    d16["scaling_power"] = 2
    d16["live_scaling_mutations"] = {}
    for scalar in (Q(-1), Q(2)):
        replay = execute_mutation(
            desk, raw, d16_recipe(scalar), 16,
            desk.xp_scale(scalar * scalar, d16_unit), range(4, 16))
        d16["live_scaling_mutations"][str(scalar)] = replay["residual"]

    # Independently exercise the mixed c8*B coefficient, not merely the B^2
    # term.  This is the exact truncation of F^(3/2)+s*t^8*F^(1/2) through
    # G15 with B=X and c16=0.
    d16_cross = {}
    for scalar in (Q(-1), Q(1), Q(2)):
        defect = X
        assignments = [
            ("F", 8, defect),
            ("G", 8, desk.xp_add(
                desk.xp_scale(Q(3, 2), desk.xp_mul(A2, defect)),
                desk.xp_scale(scalar, A2))),
            ("G", 9, desk.xp_add(
                desk.xp_scale(Q(3, 4), defect), [scalar / 2])),
        ]
        expected = desk.xp_mul(
            A2, desk.xp_add(desk.xp_scale(6, X), [4 * scalar]))
        replay = execute_mutation(
            desk, raw, assignments, 16, expected, range(4, 16))
        d16_cross[str(scalar)] = {
            "c8": str(scalar),
            "residual": replay["residual"],
            "literal_row_provenance": replay["literal_row_provenance"],
        }

    def d17_recipe(scalar):
        defect = desk.xp_scale(scalar, X)
        return [
            ("F", 8, [Q(1)]),
            ("F", 9, defect),
            ("G", 8, desk.xp_scale(Q(3, 2), A2)),
            ("G", 9, desk.xp_add([Q(3, 4)],
                                  desk.xp_scale(Q(3, 2),
                                                desk.xp_mul(A2, defect)))),
            ("G", 10, desk.xp_scale(Q(3, 4), defect)),
        ]

    d17_unit = desk.xp_add(
        desk.xp_scale(3, desk.xp_mul(desk.xp_mul(A, A_x), X)),
        desk.xp_scale(6, A2),
    )
    d17 = execute_mutation(
        desk, raw, d17_recipe(Q(1)), 17, d17_unit, range(4, 17))
    d17["interpretation"] = (
        "B=1, c8=0, c16=-3/8 makes G16 polynomial, while C=X and M=0; "
        "the first residual is exactly -L17((3/4)*X/A^2)"
    )
    d17["scaling_power"] = 1
    d17["live_scaling_mutations"] = {}
    for scalar in (Q(-1), Q(2)):
        replay = execute_mutation(
            desk, raw, d17_recipe(scalar), 17,
            desk.xp_scale(scalar, d17_unit), range(4, 17))
        d17["live_scaling_mutations"][str(scalar)] = replay["residual"]

    def polynomial(terms):
        answer = [Q(0)] * (max(terms, default=-1) + 1)
        for degree, coefficient in terms.items():
            answer[degree] = Q(coefficient)
        return desk.xp_trim(answer)

    # A literal second-lift failure: K is divisible by A but not A^2.  The
    # allowed part of G17 is inserted, while its forbidden constant Laurent
    # quotient is deliberately absent.  This checks the second A-adic step,
    # not merely the first K mod A obstruction.
    second_lift_assignments = [
        ("F", 8, polynomial({0: 1, 2: Q(3, 2), 4: -2,
                              6: Q(-1, 2), 8: 1})),
        ("F", 9, polynomial({2: Q(-3, 16), 4: Q(1, 2)})),
        ("G", 8, polynomial({
            0: Q(3, 2), 2: Q(9, 4), 4: -6, 6: Q(-21, 4),
            8: 9, 10: Q(15, 4), 12: -6, 14: Q(-3, 4), 16: Q(3, 2),
        })),
        ("G", 9, polynomial({
            0: Q(3, 4), 2: Q(27, 32), 4: Q(-3, 4), 6: Q(3, 16),
            8: Q(-3, 4), 10: Q(-9, 32), 12: Q(3, 4),
        })),
        ("G", 10, polynomial({2: Q(-9, 64), 4: Q(3, 8)})),
        ("G", 16, polynomial({
            2: Q(9, 8), 4: Q(-21, 32), 6: Q(-3, 8), 8: Q(3, 8),
        })),
        ("G", 17, polynomial({2: Q(-21, 64), 4: Q(3, 8)})),
    ]
    second_lift_residual = polynomial({
        1: -6, 3: Q(15, 4), 5: 36, 7: Q(-135, 8), 9: -54,
        11: Q(45, 2), 13: 24, 15: Q(-75, 8),
    })
    second_lift = execute_mutation(
        desk, raw, second_lift_assignments, 17, second_lift_residual,
        range(4, 17))
    second_lift.update({
        "B": "1+3*X^2/2-2*X^4-X^6/2+X^8",
        "C": "-3*X^2/16+X^4/2",
        "c8": "0",
        "c16": "-3/8",
        "M": "9*X^2/8-21*X^4/32-3*X^6/8+3*X^8/8",
        "K": "-45*X^2/16+63*X^4/32+33*X^6/8-111*X^8/32-21*X^10/16+3*X^12/2",
        "K_factor": "K=A*L",
        "L": "45*X^2/16-63*X^4/32-21*X^6/16+3*X^8/2",
        "L_mod_A": "-15/32+3*X^2/2 (nonzero)",
        "conclusion": "the second A-adic lift in K in (A^2) is live and necessary",
    })

    exact_points = {}

    def record_exact_point(label, assignments, modes):
        values = {}
        for kind, weight, polynomial in assignments:
            desk.put_window(raw, values, kind, weight, polynomial)
        direct, serialized = desk.assert_all_513(raw, values)
        assert all(not direct[weight] for weight in range(4, 23))
        exact_points[label] = {
            "characteristic_modes": modes,
            "literal_rows_D4_through_D22_before_target_fold": "zero",
            "folded_D22_constant_generator_value": str(serialized[495]),
            "all_513_generators_match_independent_determinant_recurrence": True,
        }

    record_exact_point(
        "forced_c16_positive",
        [("F", 8, [Q(1)])],
        {"B": "1", "c8": "-3/2", "c16": "3/8",
         "N16": "0", "description": "F=(A^2+t/2)^2+t^8; G=(A^2+t/2)^3"},
    )
    record_exact_point(
        "forced_c16_negative",
        [("F", 8, [Q(1)]),
         ("G", 8, desk.xp_scale(Q(3, 2), A2)),
         ("G", 9, [Q(3, 4)])],
        {"B": "1", "c8": "0", "c16": "-3/8",
         "N16": "0", "description": "add (3/2)*t^8*(A^2+t/2) to baseline G"},
    )

    gauge_family = {}
    for scalar in (Q(-1), Q(1), Q(2)):
        values = {}
        desk.put_window(raw, values, "F", 8, [scalar])
        desk.put_window(raw, values, "G", 8, A2)
        desk.put_window(raw, values, "G", 9, [Q(1, 2)])
        direct, serialized = desk.assert_all_513(raw, values)
        assert all(not direct[weight] for weight in range(4, 23))
        transformed_c8 = Q(1) - Q(3, 2) * scalar
        transformed_c16 = -scalar / 2 + Q(3, 8) * scalar * scalar
        assert scalar + Q(2, 3) * transformed_c8 == Q(2, 3)
        assert transformed_c16 - transformed_c8 * transformed_c8 / 6 == Q(-1, 6)
        gauge_family[str(scalar)] = {
            "c8": str(transformed_c8),
            "c16": str(transformed_c16),
            "Bhat": "2/3",
            "J16": "-1/6",
            "folded_D22_constant_generator_value": str(serialized[495]),
        }
    gauge = {
        "literal_family": "F8=lambda; G8=A^2; G9=1/2",
        "all_D4_through_D22_zero_before_target_fold": True,
        "transformation": (
            "B->B+lambda, c8->c8-3*lambda/2, "
            "c12->c12-c4*lambda, "
            "c16->c16-c8*lambda/2+3*lambda^2/8"
        ),
        "c12_note": (
            "the c12 shift is mandatory in the full nine-mode coordinates but has no "
            "D16/D17 tail because F^0 has no positive coefficients; the literal family "
            "shown here has c4=0"
        ),
        "fixed_coordinates": ["Bhat=B+2*c8/3", "J16=c16-c8^2/6"],
        "live_scalars": gauge_family,
    }
    return {
        "D16_quadratic_pole": d16,
        "D16_c8_cross_term": d16_cross,
        "D17_successor_pole": d17,
        "D17_second_A_adic_lift": second_lift,
        "exact_nonzero_c16_points": exact_points,
        "F8_additive_gauge_and_centering": gauge,
    }


def calculate_result():
    assert digest(RAW) == RAW_SHA256
    prior, desk = load_dependencies()
    raw = json.loads(RAW.read_text())
    assert raw["variable_count"] == 303
    assert raw["generator_count"] == len(raw["generators"]) == 513
    calculation = characteristic_calculation(desk)
    predecessor_calculation = prior.calculate_result()["calculation"]
    modes = []
    for birth, exponent in desk.MODES.items():
        if birth < 16:
            status = {
                6: "killed_at_D8",
                10: "killed_at_D11",
                14: "killed_at_D14",
            }.get(birth, "retained_live")
        elif birth == 16:
            status = "retained_and_uniquely_forced_by_D16_polynomiality"
        else:
            status = "retained_unborn"
        modes.append({
            "birth_weight": birth,
            "F_exponent": str(exponent),
            "birth_A_power": int(4 * exponent),
            "support_at_D16": birth <= 16,
            "support_at_D17": birth <= 17,
            "continuation_status": status,
        })
    return {
        "schema": "jc2.ggv.upper_endpoint.uniform_d16_d17_fullmodes.result.v1",
        "status": "PASS_EXACT_FIELD_POINT_CHARACTERISTIC_CASCADE_THROUGH_D17",
        "source": {
            "authoritative_raw_system": str(RAW.relative_to(ROOT)),
            "authoritative_raw_system_sha256": RAW_SHA256,
            "predecessor_checker": str(PREDECESSOR.relative_to(ROOT)),
            "predecessor_checker_sha256": PREDECESSOR_SHA256,
            "predecessor_result": str(PREDECESSOR_RESULT.relative_to(ROOT)),
            "predecessor_result_sha256": PREDECESSOR_RESULT_SHA256,
            "raw_variable_count": 303,
            "raw_generator_count": 513,
            "literal_D16_row_sha256": raw["per_row"]["16"]["row_sha256"],
            "literal_D17_row_sha256": raw["per_row"]["17"]["row_sha256"],
        },
        "complete_mode_schedule": modes,
        "calculation": calculation,
        "carried_positive_lower_window_core": {
            "gauge_invariant_parameter": predecessor_calculation[
                "gauge_invariant_low_jet_parameter"],
            "live_equations_C13_C15": predecessor_calculation[
                "factored_low_window_equations"],
            "new_live_equations_C16_C17": calculation["positive_lower_window_jets"],
            "status": "retained exactly; no scalar equation is solved, dropped, or normalized",
        },
        "literal_raw_window_certificates": {
            "G16": literal_window_certificate(desk, raw, 16),
            "G17": literal_window_certificate(desk, raw, 17),
        },
        "literal_raw_mutations": literal_mutations(desk, raw),
        "theorems": {
            "D16": {
                "defect": calculation["Delta8"],
                "polynomiality_relation": calculation["D16_polynomiality_relation"],
                "centered_relation": calculation["gauge_centering"][
                    "centered_D16_relation"],
                "conclusion": (
                    "c16 is uniquely determined when the relation exists and can be nonzero; "
                    "neither B nor c8 is normalized"
                ),
            },
            "D17": {
                "successor_defect": calculation["Delta9"],
                "polynomiality_relation": calculation["D17_polynomiality_relation"],
                "uniform_invariant": calculation["D17_uniform_invariant"],
                "conclusion": (
                    "the exact successor requires K17_uniform in (A^2); this is the structural "
                    "uniform ancestor candidate of the cutoff-three K relation, not yet an "
                    "asserted specialization identity"
                ),
            },
            "gauge": {
                "action": calculation["gauge_centering"]["gauge_action"],
                "fixed_coordinates": ["Bhat=B+2*c8/3", "J16=c16-c8^2/6"],
                "H0_status": (
                    "H0=c8/2+3*F8(0)/4 is carried from C13--C15 and is invariant; "
                    "no gauge slice is selected"
                ),
            },
        },
        "scope_firewall": [
            "necessary field-point characteristic/polynomial-window consequences only; no endpoint emptiness",
            "D16 is a centered quadratic congruence, not a license to choose a square-root branch",
            "D17 gives ideal membership in (A^2); no cutoff-three transport is asserted without a separate literal map",
            "C13--C17 remain live and are not eliminated or declared exhaustive for later rows",
            "c16 is retained and source-replayed with both signs; c18 and c20 remain mandatory and unconstrained",
            "c8, B, H0, endpoint carriers, and units are not normalized",
            "all nine characteristic modes are retained in the schedule, including forced negative modes",
            "standard-library Fraction arithmetic only; no CAS, AWS, or jc2-lean access",
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
            "D16": result["theorems"]["D16"],
            "D17": result["theorems"]["D17"],
            "check": arguments.check,
        }, sort_keys=True))


if __name__ == "__main__":
    main()
