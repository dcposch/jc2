#!/usr/bin/env python3
"""Exact full-mode uniform continuation through the upper endpoint D22.

This checker uses only ``fractions.Fraction`` and the frozen sparse Laurent
recurrence.  It independently reconstructs D18--D22, retains every raw
polynomial window, and replays selected mutations against all 513 literal
generators in the authoritative branch-P source.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PREDECESSOR = (ROOT / "cases/ggv_8_28_upper_endpoint_uniform_d16_d17_fullmodes_20260828"
               / "verify_uniform_d16_d17.py")
PREDECESSOR_RESULT = PREDECESSOR.with_name("RESULT.json")
RAW = ROOT / "cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json"
RESULT = HERE / "RESULT.json"

PREDECESSOR_SHA256 = "5904d7b19dc5d46d31a781150c4b6de9e62e32812b554006e92f78f9d76fd5d9"
PREDECESSOR_RESULT_SHA256 = "2a6f363df8fb4aef94f01d7a938e3bfcff15f6db49af3164e36367c9a6d1929a"
RAW_SHA256 = "ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_digest(value):
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def load_dependencies():
    assert digest(PREDECESSOR) == PREDECESSOR_SHA256
    assert digest(PREDECESSOR_RESULT) == PREDECESSOR_RESULT_SHA256
    spec = importlib.util.spec_from_file_location("uniform_d16_frozen", PREDECESSOR)
    assert spec is not None and spec.loader is not None
    prior = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(prior)
    replay = prior.calculate_result()
    assert replay["status"] == "PASS_EXACT_FIELD_POINT_CHARACTERISTIC_CASCADE_THROUGH_D17"
    _, desk = prior.load_dependencies()
    # All lower-case letters below denote honest coefficient polynomials in X.
    # Characteristic constants c4,...,c20 intentionally have no derivatives.
    for symbol in ("z", "v", "r", "q", "t", "y", "b", "d", "e", "h",
                   "k", "l", "j", "m", "n", "p", "s", "u", "w"):
        desk.DERIVATIVES[symbol] = f"{symbol}_x"
    for weight in range(8, 15):
        desk.DERIVATIVES[f"f{weight}"] = f"f{weight}_x"
    return prior, desk


def substitute_stages(desk, item, *stages):
    """Apply substitutions sequentially; la_substitute is deliberately one-pass."""
    answer = item
    for stage in stages:
        answer = desk.la_substitute(answer, stage)
    return answer


def characteristic_calculation(desk):
    term, add, scale, mul, shift = (
        desk.la_term, desk.la_add, desk.la_scale, desk.la_mul, desk.la_shift)
    z, v, r, q, t, y = (term(1, 0, name)
                         for name in ("z", "v", "r", "q", "t", "y"))
    c8 = term(1, 0, "c8")
    b, d, e, h, k, l, j = (term(1, 0, name)
                            for name in ("b", "d", "e", "h", "k", "l", "j"))

    F = desk.common_F_prefix()
    F[4] = add(scale(Q(1, 16), v), scale(Q(1, 64), mul(z, z)), term(1, 2, "r"))
    F[5] = add(scale(Q(1, 2), r), scale(Q(1, 64), mul(z, v)), term(1, 2, "q"))
    F[6] = add(scale(Q(1, 2), q), scale(Q(1, 8), mul(r, z)),
               scale(Q(1, 256), mul(v, v)), term(1, 2, "t"))
    F[7] = add(scale(Q(1, 2), t), scale(Q(1, 8), mul(q, z)),
               scale(Q(1, 16), mul(r, v)), term(1, 2, "y"))
    for weight in range(8, 15):
        F[weight] = term(1, 0, f"f{weight}")
    # The authoritative F window stops at weight 14.
    for weight in range(15, 23):
        F[weight] = {}
    _, g = desk.continuation(F, 22)

    kills = {"c6": {}, "c10": {}, "c14": {}}
    base8 = add(scale(Q(1, 2), y), scale(Q(1, 8), mul(t, z)),
                scale(Q(1, 16), mul(q, v)), scale(Q(1, 4), mul(r, r)))
    relation16 = {
        "f8": add(base8, b),
        "c16": add(term(1, 2, "m"), scale(Q(-3, 8), mul(b, b)),
                     scale(Q(-1, 2), mul(c8, b))),
    }
    base9 = add(scale(Q(1, 2), mul(q, r)), scale(Q(1, 16), mul(t, v)),
                scale(Q(1, 8), mul(y, z)))
    relation17 = {
        "f9": add(base9, d),
        "m": add(scale(Q(3, 2), mul(b, d)), mul(c8, d),
                 scale(-2, term(1, 2, "n"))),
    }

    # D18.  The defect is the exact coefficient left after completing the
    # square-root cross terms; no raw-window coefficient is discarded.
    base10 = add(scale(Q(1, 4), mul(d, z)), scale(Q(1, 4), mul(q, q)),
                 scale(Q(1, 2), mul(r, t)), scale(Q(1, 16), mul(v, y)))
    set_f10 = {"f10": add(base10, e)}
    g18_before = substitute_stages(desk, g[18], kills, relation16, relation17,
                                   set_f10)
    p18 = add(mul(add(scale(Q(3, 4), b), scale(Q(1, 2), c8)), e),
              scale(Q(3, 8), mul(d, d)), term(Q(-1, 2), 0, "n"))
    expected_g18_negative = add(term(1, -3, "c18"), shift(-2, p18))
    assert desk.la_negative(g18_before) == expected_g18_negative

    # Polynomial raw G18 implies c18+A*P18 is divisible by A^3.  Mod A gives
    # c18=0; cancelling A then gives P18 in (A^2).
    relation18 = {
        "c18": {},
        "n": add(scale(Q(1, 2), mul(add(scale(3, b), scale(2, c8)), e)),
                 scale(Q(3, 4), mul(d, d)), scale(-2, term(1, 2, "p"))),
    }
    g18_after = substitute_stages(desk, g18_before, relation18)
    assert desk.la_negative(g18_after) == {}

    # D19.
    base11 = add(scale(Q(1, 2), mul(e, z)), scale(Q(1, 8), mul(d, v)),
                 scale(Q(1, 2), mul(q, t)), scale(Q(1, 2), mul(r, y)))
    set_f11 = {"f11": add(base11, h)}
    g19_before = substitute_stages(desk, g[19], kills, relation16, relation17,
                                   set_f10, relation18, set_f11)
    p19 = add(mul(add(scale(Q(3, 4), b), scale(Q(1, 2), c8)), h),
              scale(Q(3, 4), mul(d, e)), term(Q(-1, 2), 0, "p"))
    assert desk.la_negative(g19_before) == shift(-2, p19)
    relation19 = {
        "p": add(scale(Q(1, 2), mul(add(scale(3, b), scale(2, c8)), h)),
                 scale(Q(3, 2), mul(d, e)), scale(-2, term(1, 2, "s"))),
    }
    g19_after = substitute_stages(desk, g19_before, relation19)
    assert desk.la_negative(g19_after) == {}

    # D20.
    base12 = add(mul(d, r), scale(Q(1, 4), mul(e, v)),
                 scale(Q(1, 16), mul(e, mul(z, z))), scale(Q(3, 4), mul(h, z)),
                 scale(Q(1, 2), mul(q, y)), scale(Q(1, 4), mul(t, t)))
    set_f12 = {"f12": add(base12, k)}
    g20_before = substitute_stages(desk, g[20], kills, relation16, relation17,
                                   set_f10, relation18, set_f11, relation19,
                                   set_f12)
    p20 = add(mul(add(scale(Q(3, 4), b), scale(Q(1, 2), c8)), k),
              scale(Q(3, 4), mul(d, h)), scale(Q(3, 8), mul(e, e)),
              term(Q(-1, 2), 0, "s"))
    expected_g20_negative = add(term(1, -4, "c20"), shift(-2, p20))
    assert desk.la_negative(g20_before) == expected_g20_negative
    # Here c20+A^2*P20 must be divisible by A^4, hence c20=0 and P20 in (A^2).
    relation20 = {
        "c20": {},
        "s": add(scale(Q(1, 2), mul(add(scale(3, b), scale(2, c8)), k)),
                 scale(Q(3, 2), mul(d, h)), scale(Q(3, 4), mul(e, e)),
                 scale(-2, term(1, 2, "u"))),
    }
    g20_after = substitute_stages(desk, g20_before, relation20)
    assert desk.la_negative(g20_after) == {}

    # D21.
    base13 = add(mul(d, q), scale(2, mul(e, r)),
                 scale(Q(1, 16), mul(e, mul(v, z))), scale(Q(3, 8), mul(h, v)),
                 scale(Q(3, 16), mul(h, mul(z, z))), mul(k, z),
                 scale(Q(1, 2), mul(t, y)))
    set_f13 = {"f13": add(base13, l)}
    g21_before = substitute_stages(desk, g[21], kills, relation16, relation17,
                                   set_f10, relation18, set_f11, relation19,
                                   set_f12, relation20, set_f13)
    p21 = add(mul(add(scale(Q(3, 4), b), scale(Q(1, 2), c8)), l),
              scale(Q(3, 4), mul(d, k)), scale(Q(3, 4), mul(e, h)),
              term(Q(-1, 2), 0, "u"))
    assert desk.la_negative(g21_before) == shift(-2, p21)
    relation21 = {
        "u": add(scale(Q(1, 2), mul(add(scale(3, b), scale(2, c8)), l)),
                 scale(Q(3, 2), mul(d, k)), scale(Q(3, 2), mul(e, h)),
                 scale(-2, term(1, 2, "w"))),
    }
    g21_after = substitute_stages(desk, g21_before, relation21)
    assert desk.la_negative(g21_after) == {}

    # D22.  The exact F14 cross-term completion is independently reconstructed
    # by factoring the full Laurent coefficient, rather than assumed.
    base14 = add(mul(d, t), scale(2, mul(e, q)), scale(Q(1, 2), mul(e, mul(r, z))),
                 scale(Q(1, 64), mul(e, mul(v, v))), scale(3, mul(h, r)),
                 scale(Q(3, 16), mul(h, mul(v, z))),
                 scale(Q(1, 64), mul(h, mul(z, mul(z, z)))),
                 scale(Q(1, 2), mul(k, v)), scale(Q(3, 8), mul(k, mul(z, z))),
                 scale(Q(5, 4), mul(l, z)), scale(Q(1, 4), mul(y, y)))
    set_f14 = {"f14": add(base14, j)}
    g22_full = substitute_stages(desk, g[22], kills, relation16, relation17,
                                 set_f10, relation18, set_f11, relation19,
                                 set_f12, relation20, set_f13, relation21,
                                 set_f14)
    p22 = add(mul(add(scale(Q(3, 4), b), scale(Q(1, 2), c8)), j),
              scale(Q(3, 4), mul(d, l)), scale(Q(3, 4), mul(e, k)),
              scale(Q(3, 8), mul(h, h)), term(Q(-1, 2), 0, "w"))
    assert desk.la_negative(g22_full) == shift(-2, p22)
    exponent_census = {}
    for a_power, _ in g22_full:
        exponent_census[a_power] = exponent_census.get(a_power, 0) + 1
    assert exponent_census == {-2: 6, 0: 33, 2: 29, 4: 19, 6: 7, 8: 1}

    # There is no raw G22.  At a hypothetical solution through D21, its D22
    # determinant row is therefore -L22(g22_full).  Every term is in (A):
    # the A^-2 part maps to 24*A*A'*P22+8*A^2*P22', while regular terms map
    # to A^3 or higher.
    d22 = scale(-1, desk.la_operator(22, g22_full))
    assert d22
    assert min(a_power for a_power, _ in d22) == 1
    assert all(a_power >= 1 for a_power, _ in d22)
    expected_polar_image = add(
        scale(24, mul(term(1, 1, "a_x"), p22)),
        scale(8, shift(2, desk.la_derivative(p22))),
    )
    assert scale(-1, desk.la_operator(22, shift(-2, p22))) == expected_polar_image

    # Linked-mode causal firewalls: successor rows do not independently kill
    # c18 or c20; their predecessor and same-row pieces cancel exactly.
    f1 = term(1, 2)
    c18_g18 = term(1, -3, "c18")
    c18_g19 = term(Q(-3, 4), -5, "c18")
    c18_predecessor = add(
        scale(-6, mul(desk.la_derivative(f1), c18_g18)),
        scale(-7, mul(f1, desk.la_derivative(c18_g18))))
    c18_same = desk.la_operator(19, c18_g19)
    assert c18_predecessor == term(9, -2, "a_x", "c18")
    assert c18_same == term(-9, -2, "a_x", "c18")
    assert add(c18_predecessor, c18_same) == {}

    c20_g20 = term(1, -4, "c20")
    c20_g21 = term(-1, -6, "c20")
    c20_predecessor = add(
        scale(-8, mul(desk.la_derivative(f1), c20_g20)),
        scale(-7, mul(f1, desk.la_derivative(c20_g20))))
    c20_same = desk.la_operator(21, c20_g21)
    assert c20_predecessor == term(12, -3, "a_x", "c20")
    assert c20_same == term(-12, -3, "a_x", "c20")
    assert add(c20_predecessor, c20_same) == {}

    encoded_g22 = desk.la_encode(g22_full)
    return {
        "D18": {
            "Delta10": "E=F10-D*Z/4-Q^2/4-R*T/2-V*Y/16",
            "g18_negative": desk.la_encode(expected_g18_negative),
            "P18": "(3*B/4+c8/2)*E+3*D^2/8-N/2",
            "conclusion": "c18=0 and P18=A^2*P",
        },
        "D19": {
            "Delta11": "H=F11-E*Z/2-D*V/8-Q*T/2-R*Y/2",
            "g19_negative": desk.la_encode(shift(-2, p19)),
            "P19": "(3*B/4+c8/2)*H+3*D*E/4-P/2",
            "conclusion": "P19=A^2*S",
        },
        "D20": {
            "Delta12": "K=F12-D*R-E*V/4-E*Z^2/16-3*H*Z/4-Q*Y/2-T^2/4",
            "g20_negative": desk.la_encode(expected_g20_negative),
            "P20": "(3*B/4+c8/2)*K+3*D*H/4+3*E^2/8-S/2",
            "conclusion": "c20=0 and P20=A^2*U",
        },
        "D21": {
            "Delta13": "L=F13-D*Q-2*E*R-E*V*Z/16-3*H*V/8-3*H*Z^2/16-K*Z-T*Y/2",
            "g21_negative": desk.la_encode(shift(-2, p21)),
            "P21": "(3*B/4+c8/2)*L+3*D*K/4+3*E*H/4-U/2",
            "conclusion": "P21=A^2*W",
        },
        "D22": {
            "Delta14": (
                "J=F14-D*T-2*E*Q-E*R*Z/2-E*V^2/64-3*H*R-3*H*V*Z/16"
                "-H*Z^3/64-K*V/2-3*K*Z^2/8-5*L*Z/4-Y^2/4"
            ),
            "P22": "(3*B/4+c8/2)*J+3*D*L/4+3*E*K/4+3*H^2/8-W/2",
            "negative_part": desk.la_encode(shift(-2, p22)),
            "full_g22_exponent_census": {str(key): value
                                          for key, value in sorted(exponent_census.items())},
            "full_g22_term_count": len(g22_full),
            "full_g22_sha256": canonical_digest(encoded_g22),
            "corrected_shape": "g22=P22/A^2+H22 with H22 polynomial, not only P22/A^2",
            "minus_L22_min_A_exponent": min(a_power for a_power, _ in d22),
            "minus_L22_term_count": len(d22),
            "minus_L22_sha256": canonical_digest(desk.la_encode(d22)),
            "polar_image": desk.la_encode(expected_polar_image),
            "conclusion": "the complete D22 determinant row lies in the principal ideal (A)",
        },
        "causal_firewalls": {
            "c18_D19_predecessor": desk.la_encode(c18_predecessor),
            "c18_D19_same_row": desk.la_encode(c18_same),
            "c18_D19_total": [],
            "c20_D21_predecessor": desk.la_encode(c20_predecessor),
            "c20_D21_same_row": desk.la_encode(c20_same),
            "c20_D21_total": [],
            "conclusion": "c18 and c20 are forced by their birth-row polynomiality, not successor kills",
        },
    }


def solve_linear(matrix, right):
    """Return the canonical solution with every free variable set to zero."""
    work = [list(row) + [value] for row, value in zip(matrix, right)]
    rows = len(work)
    columns = len(matrix[0]) if matrix else 0
    pivot_row = 0
    pivots = []
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
            work[row] = [left - factor * right_value
                         for left, right_value in zip(work[row], work[pivot_row])]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == rows:
            break
    assert all(any(row[:columns]) or not row[columns] for row in work)
    solution = [Q(0)] * columns
    for row, column in enumerate(pivots):
        solution[column] = work[row][columns]
    return solution


def g_window_columns(desk, raw, weight):
    """Literal same-row map from the allowed raw G_weight window to D_weight."""
    row_degree = raw["per_row"][str(weight)]["raw_polynomial_degree"]
    window = raw["windows"]["G"][str(weight)]
    columns = []
    for slot in window["slots"]:
        _, F, G = desk.reconstruct_literal(raw, {slot: Q(1)})
        row = desk.literal_determinant_rows(F, G)[weight]
        row = row + [Q(0)] * (row_degree + 1 - len(row))
        columns.append(row)
    return columns


def extend_literal_prefix(desk, raw, f_assignments, fixed_g, target,
                          column_cache):
    """Solve each allowed raw G window canonically through target-1."""
    values = {}
    for weight, polynomial in f_assignments:
        desk.put_window(raw, values, "F", weight, polynomial)
    fixed_weights = set()
    for weight, polynomial in fixed_g:
        desk.put_window(raw, values, "G", weight, polynomial)
        fixed_weights.add(weight)
    for weight in range(4, target):
        _, F, G = desk.reconstruct_literal(raw, values)
        row = desk.literal_determinant_rows(F, G)[weight]
        row_degree = raw["per_row"][str(weight)]["raw_polynomial_degree"]
        row = row + [Q(0)] * (row_degree + 1 - len(row))
        if weight in fixed_weights:
            assert not any(row), (weight, desk.xp_encode(row))
            continue
        window = raw["windows"]["G"][str(weight)]
        columns = column_cache.setdefault(
            weight, g_window_columns(desk, raw, weight))
        matrix = [[columns[column][degree] for column in range(len(columns))]
                  for degree in range(row_degree + 1)]
        solution = solve_linear(matrix, [-value for value in row])
        for slot, value in zip(window["slots"], solution):
            values[slot] = value
        _, solved_F, solved_G = desk.reconstruct_literal(raw, values)
        assert not desk.literal_determinant_rows(solved_F, solved_G)[weight]
    direct, serialized = desk.assert_all_513(raw, values)
    assert all(not direct[weight] for weight in range(4, target))
    return values, direct, serialized


def encode_assignments(values):
    return {slot: str(value) for slot, value in sorted(values.items()) if value}


def literal_mutation(desk, raw, label, f_weight, f_polynomial, target,
                     expected, column_cache):
    A = [Q(-1), Q(0), Q(0), Q(0), Q(1)]
    A2 = desk.xp_power(A, 2)
    values, direct, serialized = extend_literal_prefix(
        desk, raw,
        [(8, [Q(1)]), (f_weight, f_polynomial)],
        [(8, desk.xp_scale(Q(3, 2), A2)), (9, [Q(3, 4)])],
        target, column_cache)
    assert direct[target] == expected, (label, desk.xp_encode(direct[target]))
    assignments = encode_assignments(values)
    return {
        "label": label,
        "late_F_assignment": {"weight": f_weight,
                              "polynomial": desk.xp_encode(f_polynomial)},
        "fixed_gauge_data": "F8=1, G8=3*A^2/2, G9=3/4 (c8=0, c16=-3/8)",
        "canonical_raw_assignment_nonzero_count": len(assignments),
        "canonical_raw_assignment_sha256": canonical_digest(assignments),
        "prior_rows_zero": list(range(4, target)),
        "first_residual_row": target,
        "residual": desk.xp_encode(expected),
        "literal_row_provenance": desk.row_provenance(raw, serialized, target),
        "all_513_generators_match_independent_determinant_recurrence": True,
    }


def literal_source_replay(prior, desk, raw):
    A = [Q(-1), Q(0), Q(0), Q(0), Q(1)]
    X = [Q(0), Q(1)]
    X2 = [Q(0), Q(0), Q(1)]
    cache = {}
    recipes = [
        ("D18_P18_live", 10, X, 18,
         [Q(6), Q(0), Q(0), Q(0), Q(-36), Q(0), Q(0), Q(0), Q(30)]),
        ("D19_P19_live", 11, X, 19,
         [Q(6), Q(0), Q(0), Q(0), Q(-48), Q(0), Q(0), Q(0), Q(42)]),
        ("D20_P20_live", 12, X2, 20,
         [Q(0), Q(12), Q(0), Q(0), Q(0), Q(-72), Q(0), Q(0), Q(0), Q(60)]),
        ("D21_P21_live", 13, X2, 21,
         [Q(0), Q(12), Q(0), Q(0), Q(0), Q(-84), Q(0), Q(0), Q(0), Q(72)]),
        ("D22_nonzero_A_multiple", 14, X2, 22,
         [Q(0), Q(12), Q(0), Q(0), Q(0), Q(-96), Q(0), Q(0), Q(0), Q(84)]),
    ]
    mutations = {}
    for label, f_weight, polynomial, target, expected in recipes:
        mutation = literal_mutation(desk, raw, label, f_weight, polynomial,
                                    target, expected, cache)
        mutation["live_scaling_mutations"] = {}
        for scalar in (Q(-1), Q(2)):
            scaled = literal_mutation(
                desk, raw, f"{label}_scale_{scalar}", f_weight,
                desk.xp_scale(scalar, polynomial), target,
                desk.xp_scale(scalar, expected), cache)
            mutation["live_scaling_mutations"][str(scalar)] = {
                "residual": scaled["residual"],
                "canonical_raw_assignment_sha256": scaled[
                    "canonical_raw_assignment_sha256"],
            }
        mutations[label] = mutation

    # The D22 mutation is visibly a nonzero multiple of A.
    d22_polynomial = recipes[-1][-1]
    quotient = [Q(0), Q(-12), Q(0), Q(0), Q(0), Q(84)]
    assert desk.xp_mul(A, quotient) == d22_polynomial
    mutations["D22_nonzero_A_multiple"]["factorization"] = {
        "A": "X^4-1",
        "quotient": desk.xp_encode(quotient),
        "identity_checked": True,
    }

    # Literal endpoint target: the zero determinant row is rejected exactly
    # by generator 495, the X^0 equation D22[X^0]-1.
    direct_zero, serialized_zero = desk.assert_all_513(raw, {})
    assert all(not direct_zero[weight] for weight in range(4, 23))
    assert serialized_zero[495] == -1
    assert all(not value for index, value in enumerate(serialized_zero) if index != 495)
    endpoint_generators = [(index, int(generator["x_degree"]))
                           for index, generator in enumerate(raw["generators"])
                           if int(generator["row"]) == 22]
    assert endpoint_generators == list(zip(range(495, 513), range(18)))
    # 1 has nonzero remainder on division by A=X^4-1.
    assert len(A) == 5 and A[-1] == 1
    assert [Q(1)] != [] and len([Q(1)]) < len(A)

    return {
        "raw_windows": {
            f"G{weight}": prior.literal_window_certificate(desk, raw, weight)
            for weight in range(18, 22)
        },
        "F_window_termination": {
            "last_weight": 14,
            "F15_through_F22_absent": all(str(weight) not in raw["windows"]["F"]
                                           for weight in range(15, 23)),
        },
        "G_window_termination": {
            "last_weight": 21,
            "G22_absent": "22" not in raw["windows"]["G"],
        },
        "mutations": mutations,
        "endpoint_target": {
            "literal_D22_row_sha256": raw["per_row"]["22"]["row_sha256"],
            "raw_polynomial_degree": raw["per_row"]["22"]["raw_polynomial_degree"],
            "target": raw["per_row"]["22"]["target"],
            "literal_generator_indices_zero_based": list(range(495, 513)),
            "literal_generator_degrees": list(range(18)),
            "zero_row_folded_provenance": desk.row_provenance(raw, serialized_zero, 22),
            "conclusion": "all endpoint generators impose D22(X)=1, not only D22[X^0]=1",
        },
    }


def calculate_result():
    assert digest(RAW) == RAW_SHA256
    prior, desk = load_dependencies()
    raw = json.loads(RAW.read_text())
    assert raw["variable_count"] == 303
    assert raw["generator_count"] == len(raw["generators"]) == 513
    calculation = characteristic_calculation(desk)
    literal = literal_source_replay(prior, desk, raw)
    modes = []
    for birth, exponent in desk.MODES.items():
        status = {
            4: "retained_live",
            6: "killed_at_D8",
            8: "retained_live",
            10: "killed_at_D11",
            12: "retained_live",
            14: "killed_at_D14",
            16: "retained_and_forced_by_D16_polynomiality",
            18: "forced_zero_by_D18_polynomiality",
            20: "forced_zero_by_D20_polynomiality",
        }[birth]
        modes.append({
            "birth_weight": birth,
            "F_exponent": str(exponent),
            "birth_A_power": int(4 * exponent),
            "support_at_D22": True,
            "continuation_status": status,
        })
    return {
        "schema": "jc2.ggv.upper_endpoint.uniform_d18_d22_endpoint_collapse.result.v1",
        "status": "PASS_EXACT_FIELD_POINT_UNIFORM_UPPER_ENDPOINT_EMPTY_THROUGH_D22",
        "source": {
            "authoritative_raw_system": str(RAW.relative_to(ROOT)),
            "authoritative_raw_system_sha256": RAW_SHA256,
            "predecessor_checker": str(PREDECESSOR.relative_to(ROOT)),
            "predecessor_checker_sha256": PREDECESSOR_SHA256,
            "predecessor_result": str(PREDECESSOR_RESULT.relative_to(ROOT)),
            "predecessor_result_sha256": PREDECESSOR_RESULT_SHA256,
            "raw_variable_count": 303,
            "raw_generator_count": 513,
            "literal_row_sha256": {
                str(weight): raw["per_row"][str(weight)]["row_sha256"]
                for weight in range(18, 23)
            },
        },
        "complete_mode_schedule": modes,
        "calculation": calculation,
        "literal_raw_source_replay": literal,
        "theorem": {
            "hypothesis": (
                "a field-valued point of the authoritative uniform branch-P raw system "
                "satisfies every D4--D21 generator"
            ),
            "cascade": [
                "D18 forces c18=0 and P18 in (A^2)",
                "D19 forces P19 in (A^2)",
                "D20 forces c20=0 and P20 in (A^2)",
                "D21 forces P21 in (A^2)",
            ],
            "endpoint_identity": "D22=-L22(g22) belongs to (A), A=X^4-1",
            "raw_target": "the eighteen literal endpoint equations require D22(X)=1",
            "contradiction": "1 is not in the proper principal ideal (X^4-1) over a field",
            "conclusion": "the uniform full-fixture upper-endpoint field stratum is empty",
        },
        "correction_to_provisional_claim": (
            "the full g22 has A-exponents -2,0,2,4,6,8; only its polar part is A^-2. "
            "The regular part does not threaten the proof because -L22 sends it into (A^3)."
        ),
        "scope_firewall": [
            "field-valued emptiness only; no scheme-theoretic unit certificate is claimed",
            "the argument uses the complete D22 polynomial target D22=1, not evaluation at X=0 or A=0",
            "all positive lower and upper G18--G21 raw-window restrictions remain mandatory; a hypothetical raw point supplies them automatically and the exact window maps have no homogeneous kernel",
            "c18 and c20 are killed only by their birth-row polynomiality; linked successor cancellations are retained",
            "c4, c8, c12, c16 and every regular part of g18--g22 are retained; no characteristic mode is silently dropped",
            "no endpoint carrier, unit, additive gauge, or sign branch is normalized",
            "the result is conditional on the recursively pinned D8--D17 producer packets until independent hostile review",
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
            "D22": result["calculation"]["D22"],
            "correction": result["correction_to_provisional_claim"],
            "check": arguments.check,
        }, sort_keys=True))


if __name__ == "__main__":
    main()
