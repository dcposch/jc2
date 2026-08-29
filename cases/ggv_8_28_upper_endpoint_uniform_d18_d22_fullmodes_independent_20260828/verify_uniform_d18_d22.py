#!/usr/bin/env python3
"""Independent exact audit of the uniform upper endpoint from D18 to D22.

Only Python standard-library Fraction arithmetic is used.  The Laurent-series
engine in this file is independent of the frozen D16/D17 producer.  That
packet is replayed and hash-pinned solely as the charged starting point.
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
RAW = ROOT / "cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json"
PREDECESSOR = (ROOT / "cases/ggv_8_28_upper_endpoint_uniform_d16_d17_fullmodes_20260828"
               / "verify_uniform_d16_d17.py")
PREDECESSOR_RESULT = PREDECESSOR.with_name("RESULT.json")
RESULT = HERE / "RESULT.json"

RAW_SHA256 = "ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0"
PREDECESSOR_SHA256 = "5904d7b19dc5d46d31a781150c4b6de9e62e32812b554006e92f78f9d76fd5d9"
PREDECESSOR_RESULT_SHA256 = "2a6f363df8fb4aef94f01d7a938e3bfcff15f6db49af3164e36367c9a6d1929a"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def encoded_digest(item) -> str:
    encoded = json.dumps(item, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def replay_predecessor():
    assert digest(PREDECESSOR) == PREDECESSOR_SHA256
    assert digest(PREDECESSOR_RESULT) == PREDECESSOR_RESULT_SHA256
    specification = importlib.util.spec_from_file_location("frozen_uniform_d16_d17", PREDECESSOR)
    assert specification is not None and specification.loader is not None
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    replay = module.calculate_result()
    assert replay["status"] == "PASS_EXACT_FIELD_POINT_CHARACTERISTIC_CASCADE_THROUGH_D17"
    frozen = json.loads(PREDECESSOR_RESULT.read_text())
    assert replay == frozen
    assert frozen["theorems"]["D16"]["polynomiality_relation"] == (
        "3*B^2+4*c8*B+8*c16=8*A^2*M")
    assert frozen["theorems"]["D17"]["polynomiality_relation"] == (
        "(3*B+2*c8)*C-2*M=4*A^2*N")
    return frozen


# Sparse Laurent polynomials in the symbol A.  Coefficients are ordinary
# commutative monomials in named polynomial coefficients.
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
    for (left_power, left_symbols), left_coefficient in left.items():
        for (right_power, right_symbols), right_coefficient in right.items():
            key = (left_power + right_power,
                   tuple(sorted(left_symbols + right_symbols)))
            answer[key] = answer.get(key, Q(0)) + left_coefficient * right_coefficient
            if not answer[key]:
                del answer[key]
    return answer


def la_product(*items):
    answer = la_term(1)
    for item in items:
        answer = la_mul(answer, item)
    return answer


def la_shift(a_power, item):
    return {(old_power + a_power, symbols): coefficient
            for (old_power, symbols), coefficient in item.items()}


DERIVATIVES = {
    name: f"{name}_x"
    for name in (
        "z", "v", "r", "q", "t", "y",
        "b8", "b9", "b10", "b11", "b12", "b13", "b14",
        "m16", "n17", "h18", "h19", "h20", "h21",
        *[f"f{weight}" for weight in range(8, 15)],
    )
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
    """Contribution L_n(R)=4(12-n)A^3 A'R-8A^4 R'."""
    return la_add(
        la_scale(4 * (12 - weight),
                 la_mul(la_shift(3, item), la_term(1, 0, "a_x"))),
        la_scale(-8, la_shift(4, la_derivative(item))),
    )


def la_negative(item):
    return {key: value for key, value in item.items() if key[0] < 0}


def la_mod_a(bound, item):
    return {key: value for key, value in item.items() if key[0] < bound}


def la_substitute(item, substitutions):
    answer = {}
    for (a_power, symbols), coefficient in item.items():
        current = la_term(coefficient, a_power)
        for symbol in symbols:
            current = la_mul(current,
                             substitutions.get(symbol, la_term(1, 0, symbol)))
        answer = la_add(answer, current)
    return answer


def la_encode(item):
    return [
        {"A_exponent": a_power, "coefficient": str(coefficient),
         "monomial": list(symbols)}
        for (a_power, symbols), coefficient in sorted(item.items())
    ]


def fractional_coefficients(F, exponent, maximum):
    """Solve F*y'=exponent*F'*y with y_0=A^(4*exponent)."""
    values = {0: la_term(1, int(4 * exponent))}
    for weight in range(1, maximum + 1):
        numerator = {}
        for index in range(1, weight + 1):
            factor = (exponent + 1) * index - weight
            numerator = la_add(
                numerator,
                la_scale(factor, la_mul(F[index], values[weight - index])),
            )
        values[weight] = la_scale(Q(1, weight), la_shift(-4, numerator))
    return values


MODES = {
    4: Q(1), 6: Q(3, 4), 8: Q(1, 2), 10: Q(1, 4), 12: Q(0),
    14: Q(-1, 4), 16: Q(-1, 2), 18: Q(-3, 4), 20: Q(-1),
}


def continuation(F, maximum):
    exponents = set(MODES.values()) | {Q(3, 2)}
    powers = {exponent: fractional_coefficients(F, exponent, maximum)
              for exponent in exponents}
    G = {}
    for weight in range(maximum + 1):
        coefficient = powers[Q(3, 2)][weight]
        for birth, exponent in MODES.items():
            if birth <= weight:
                coefficient = la_add(
                    coefficient,
                    la_mul(la_term(1, 0, f"c{birth}"),
                           powers[exponent][weight - birth]),
                )
        G[weight] = coefficient
    return powers, G


def formal_determinant_row(F, G, weight):
    """Exact coefficient of the charged determinant recurrence."""
    answer = {}
    for left_weight in range(weight + 1):
        right_weight = weight - left_weight
        if left_weight not in F or right_weight not in G:
            continue
        answer = la_add(
            answer,
            la_scale(12 - right_weight,
                     la_mul(la_derivative(F[left_weight]), G[right_weight])),
            la_scale(left_weight - 8,
                     la_mul(F[left_weight], la_derivative(G[right_weight]))),
        )
    return answer


def square_prefix_and_defects():
    z, v, r, q, t, y = (la_term(1, 0, name)
                         for name in ("z", "v", "r", "q", "t", "y"))
    S = {
        0: la_term(1, 2),
        1: la_term(Q(1, 2)),
        2: la_scale(Q(1, 8), z),
        3: la_scale(Q(1, 16), v),
        4: la_scale(Q(1, 2), r),
        5: la_scale(Q(1, 2), q),
        6: la_scale(Q(1, 2), t),
        7: la_scale(Q(1, 2), y),
    }
    square = {}
    for weight in range(15):
        coefficient = {}
        for index in range(weight + 1):
            if index in S and weight - index in S:
                coefficient = la_add(coefficient,
                                     la_mul(S[index], S[weight - index]))
        square[weight] = coefficient

    expected = {
        8: la_add(la_scale(Q(1, 2), y),
                  la_scale(Q(1, 8), la_mul(t, z)),
                  la_scale(Q(1, 16), la_mul(q, v)),
                  la_scale(Q(1, 4), la_mul(r, r))),
        9: la_add(la_scale(Q(1, 2), la_mul(q, r)),
                  la_scale(Q(1, 16), la_mul(t, v)),
                  la_scale(Q(1, 8), la_mul(y, z))),
        10: la_add(la_scale(Q(1, 4), la_mul(q, q)),
                   la_scale(Q(1, 2), la_mul(r, t)),
                   la_scale(Q(1, 16), la_mul(v, y))),
        11: la_add(la_scale(Q(1, 2), la_mul(q, t)),
                   la_scale(Q(1, 2), la_mul(r, y))),
        12: la_add(la_scale(Q(1, 2), la_mul(q, y)),
                   la_scale(Q(1, 4), la_mul(t, t))),
        13: la_scale(Q(1, 2), la_mul(t, y)),
        14: la_scale(Q(1, 4), la_mul(y, y)),
    }
    assert all(square[weight] == expected[weight] for weight in expected)
    return square, expected


def characteristic_calculation():
    square, bases = square_prefix_and_defects()
    F = dict(square)
    for weight in range(8, 15):
        F[weight] = la_term(1, 0, f"f{weight}")
    for weight in range(15, 23):
        F[weight] = {}
    _, G = continuation(F, 22)
    # This is a direct replay of the determinant recurrence, independent of
    # the coefficient recurrence used to build fractional powers.
    assert all(formal_determinant_row(F, G, weight) == {}
               for weight in range(23))

    b = {weight: la_term(1, 0, f"b{weight}") for weight in range(8, 15)}
    z, v, r, q, t, y = (la_term(1, 0, name)
                         for name in ("z", "v", "r", "q", "t", "y"))
    c8 = la_term(1, 0, "c8")
    a = la_add(la_scale(3, b[8]), la_scale(2, c8))

    initial = {"c6": {}, "c10": {}, "c14": {}}
    for weight in range(8, 15):
        initial[f"f{weight}"] = la_add(bases[weight], b[weight])
    initial["c16"] = la_add(
        la_term(1, 2, "m16"),
        la_scale(Q(-3, 8), la_mul(b[8], b[8])),
        la_scale(Q(-1, 2), la_mul(c8, b[8])),
    )
    relation17 = {
        "m16": la_add(
            la_scale(Q(3, 2), la_mul(b[8], b[9])),
            la_mul(c8, b[9]),
            la_scale(-2, la_term(1, 2, "n17")),
        )
    }

    r18 = la_add(
        la_scale(Q(1, 4), la_mul(a, b[10])),
        la_scale(Q(-1, 16), la_product(a, b[9], z)),
        la_scale(Q(3, 8), la_mul(b[9], b[9])),
        la_term(Q(-1, 2), 0, "n17"),
    )
    g18 = la_substitute(la_substitute(G[18], initial), relation17)
    expected18 = la_add(la_term(1, -3, "c18"), la_shift(-2, r18))
    assert la_negative(g18) == expected18
    c18_g18 = la_term(1, -3, "c18")
    c18_g19 = la_term(Q(-3, 4), -5, "c18")
    f1 = la_term(1, 2)
    c18_predecessor = la_add(
        la_scale(-6, la_mul(la_derivative(f1), c18_g18)),
        la_scale(-7, la_mul(f1, la_derivative(c18_g18))),
    )
    c18_same_row = la_operator(19, c18_g19)
    assert c18_predecessor == la_term(9, -2, "a_x", "c18")
    assert c18_same_row == la_term(-9, -2, "a_x", "c18")
    assert la_add(c18_predecessor, c18_same_row) == {}
    relation18 = {
        "c18": {},
        "n17": la_add(
            la_scale(Q(1, 2), la_mul(a, b[10])),
            la_scale(Q(-1, 8), la_product(a, b[9], z)),
            la_scale(Q(3, 4), la_mul(b[9], b[9])),
            la_scale(-2, la_term(1, 2, "h18")),
        ),
    }
    assert la_negative(la_substitute(g18, relation18)) == {}

    r19 = la_add(
        la_mul(a, la_add(
            la_scale(Q(1, 4), b[11]),
            la_scale(Q(-1, 8), la_mul(b[10], z)),
            la_scale(Q(1, 32),
                     la_mul(b[9], la_add(la_mul(z, z), la_scale(-1, v)))),
        )),
        la_scale(Q(3, 4), la_mul(b[9], b[10])),
        la_scale(Q(-3, 16), la_product(b[9], b[9], z)),
        la_term(Q(-1, 2), 0, "h18"),
    )
    g19 = G[19]
    for substitutions in (initial, relation17, relation18):
        g19 = la_substitute(g19, substitutions)
    assert la_negative(g19) == la_shift(-2, r19)
    relation19 = {
        "h18": la_add(
            la_mul(a, la_add(
                la_scale(Q(1, 2), b[11]),
                la_scale(Q(-1, 4), la_mul(b[10], z)),
                la_scale(Q(1, 16),
                         la_mul(b[9], la_add(la_mul(z, z), la_scale(-1, v)))),
            )),
            la_scale(Q(3, 2), la_mul(b[9], b[10])),
            la_scale(Q(-3, 8), la_product(b[9], b[9], z)),
            la_scale(-2, la_term(1, 2, "h19")),
        )
    }
    assert la_negative(la_substitute(g19, relation19)) == {}

    bracket20 = la_add(
        la_scale(Q(1, 4), b[12]),
        la_scale(Q(-3, 16), la_mul(b[11], z)),
        la_scale(Q(5, 64), la_product(b[10], z, z)),
        la_scale(Q(-1, 16), la_mul(b[10], v)),
        la_scale(Q(-1, 4), la_mul(b[9], r)),
        la_scale(Q(5, 128), la_product(b[9], v, z)),
        la_scale(Q(-5, 256), la_product(b[9], z, z, z)),
    )
    other20 = la_add(
        la_scale(Q(-3, 32), la_product(b[9], b[9], v)),
        la_scale(Q(15, 128), la_product(b[9], b[9], z, z)),
        la_scale(Q(-9, 16), la_product(b[9], b[10], z)),
        la_scale(Q(3, 4), la_mul(b[9], b[11])),
        la_scale(Q(3, 8), la_mul(b[10], b[10])),
    )
    r20 = la_add(la_mul(a, bracket20), other20,
                 la_term(Q(-1, 2), 0, "h19"))
    g20 = G[20]
    for substitutions in (initial, relation17, relation18, relation19):
        g20 = la_substitute(g20, substitutions)
    expected20 = la_add(la_term(1, -4, "c20"), la_shift(-2, r20))
    assert la_negative(g20) == expected20
    c20_g20 = la_term(1, -4, "c20")
    c20_g21 = la_term(-1, -6, "c20")
    c20_predecessor = la_add(
        la_scale(-8, la_mul(la_derivative(f1), c20_g20)),
        la_scale(-7, la_mul(f1, la_derivative(c20_g20))),
    )
    c20_same_row = la_operator(21, c20_g21)
    assert c20_predecessor == la_term(12, -3, "a_x", "c20")
    assert c20_same_row == la_term(-12, -3, "a_x", "c20")
    assert la_add(c20_predecessor, c20_same_row) == {}
    relation20 = {
        "c20": {},
        "h19": la_add(
            la_scale(2, la_mul(a, bracket20)),
            la_scale(2, other20),
            la_scale(-2, la_term(1, 2, "h20")),
        ),
    }
    assert la_negative(la_substitute(g20, relation20)) == {}

    bracket21 = la_add(
        la_scale(Q(1, 4), b[13]),
        la_scale(Q(-1, 4), la_mul(b[12], z)),
        la_scale(Q(9, 64), la_product(b[11], z, z)),
        la_scale(Q(-3, 32), la_mul(b[11], v)),
        la_scale(Q(-1, 2), la_mul(b[10], r)),
        la_scale(Q(3, 32), la_product(b[10], v, z)),
        la_scale(Q(-7, 128), la_product(b[10], z, z, z)),
        la_scale(Q(-1, 4), la_mul(b[9], q)),
        la_scale(Q(3, 8), la_product(b[9], r, z)),
        la_scale(Q(3, 256), la_product(b[9], v, v)),
        la_scale(Q(-21, 512), la_product(b[9], v, z, z)),
        la_scale(Q(7, 512), la_product(b[9], z, z, z, z)),
    )
    other21 = la_add(
        la_scale(Q(-3, 4), la_product(b[9], b[9], r)),
        la_scale(Q(9, 64), la_product(b[9], b[9], v, z)),
        la_scale(Q(-21, 256), la_product(b[9], b[9], z, z, z)),
        la_scale(Q(-9, 32), la_product(b[9], b[10], v)),
        la_scale(Q(27, 64), la_product(b[9], b[10], z, z)),
        la_scale(Q(-3, 4), la_product(b[9], b[11], z)),
        la_scale(Q(3, 4), la_mul(b[9], b[12])),
        la_scale(Q(-3, 8), la_product(b[10], b[10], z)),
        la_scale(Q(3, 4), la_mul(b[10], b[11])),
    )
    r21 = la_add(la_mul(a, bracket21), other21,
                 la_term(Q(-1, 2), 0, "h20"))
    g21 = G[21]
    for substitutions in (initial, relation17, relation18, relation19, relation20):
        g21 = la_substitute(g21, substitutions)
    assert la_negative(g21) == la_shift(-2, r21)
    relation21 = {
        "h20": la_add(
            la_scale(2, la_mul(a, bracket21)),
            la_scale(2, other21),
            la_scale(-2, la_term(1, 2, "h21")),
        )
    }
    assert la_negative(la_substitute(g21, relation21)) == {}

    g22 = G[22]
    for substitutions in (
            initial, relation17, relation18, relation19, relation20, relation21):
        g22 = la_substitute(g22, substitutions)
    negative22 = la_negative(g22)
    assert negative22
    assert {a_power for a_power, _ in negative22} == {-2}
    assert min(a_power for a_power, _ in g22) == -2
    support22 = sorted({a_power for a_power, _ in g22})
    assert support22 == [-2, 0, 2, 4, 6, 8]
    d22_raw = la_scale(-1, la_operator(22, g22))
    assert d22_raw
    assert min(a_power for a_power, _ in d22_raw) >= 1
    assert la_mod_a(1, d22_raw) == {}

    truncated_G = {weight: coefficient for weight, coefficient in G.items()
                   if weight <= 21}
    # Check the endpoint sign before substitutions.  Substitution and
    # differentiation do not commute syntactically unless derivative symbols
    # are also replaced, so the specialized equality is represented by
    # differentiating the already-specialized g22 above.
    assert formal_determinant_row(F, truncated_G, 22) == la_scale(
        -1, la_operator(22, G[22]))

    # A weight-22 homogeneous mode is not an admitted raw slot.  Even if it
    # is appended synthetically, it is the kernel c22/A^5 and contributes
    # zero to D22, so it cannot alter the endpoint conclusion.
    synthetic_c22 = la_term(1, -5, "c22")
    assert la_operator(22, synthetic_c22) == {}

    # Formal first-lift mutations: replacing A^2 by A leaves an actual pole.
    wrong18 = dict(relation18)
    wrong18["n17"] = la_add(
        la_scale(Q(1, 2), la_mul(a, b[10])),
        la_scale(Q(-1, 8), la_product(a, b[9], z)),
        la_scale(Q(3, 4), la_mul(b[9], b[9])),
        la_scale(-2, la_term(1, 1, "h18")),
    )
    assert {power for power, _ in la_negative(la_substitute(g18, wrong18))} == {-1}
    wrong20 = dict(relation20)
    wrong20["h19"] = la_add(
        la_scale(2, la_mul(a, bracket20)), la_scale(2, other20),
        la_scale(-2, la_term(1, 1, "h20")),
    )
    assert {power for power, _ in la_negative(la_substitute(g20, wrong20))} == {-1}

    return {
        "defects": {
            "B8": "F8-Y/2-T*Z/8-Q*V/16-R^2/4",
            "B9": "F9-Q*R/2-T*V/16-Y*Z/8",
            "B10": "F10-Q^2/4-R*T/2-V*Y/16",
            "B11": "F11-Q*T/2-R*Y/2",
            "B12": "F12-Q*Y/2-T^2/4",
            "B13": "F13-T*Y/2",
            "B14": "F14-Y^2/4",
            "square_prefix_coefficients_checked": True,
        },
        "A8": "3*B8+2*c8",
        "R18": la_encode(r18),
        "g18_polar": la_encode(expected18),
        "D18_relation": "c18=0 and R18=A^2*h18",
        "D18_D19_c18_causal_firewall": {
            "predecessor_mixed_piece": la_encode(c18_predecessor),
            "same_row_piece": la_encode(c18_same_row),
            "total": [],
            "conclusion": "D19 does not kill c18; literal D18 polynomiality does",
        },
        "R19": la_encode(r19),
        "g19_polar_after_D18": la_encode(la_shift(-2, r19)),
        "D19_relation": "R19=A^2*h19",
        "R20": la_encode(r20),
        "g20_polar_after_D19": la_encode(expected20),
        "D20_relation": "c20=0 and R20=A^2*h20",
        "D20_D21_c20_causal_firewall": {
            "predecessor_mixed_piece": la_encode(c20_predecessor),
            "same_row_piece": la_encode(c20_same_row),
            "total": [],
            "conclusion": "D21 does not kill c20; literal D20 polynomiality does",
        },
        "R21": la_encode(r21),
        "g21_polar_after_D20": la_encode(la_shift(-2, r21)),
        "D21_relation": "R21=A^2*h21",
        "g22_after_D21": {
            "minimum_A_exponent": -2,
            "complete_A_exponent_support": support22,
            "negative_term_count": len(negative22),
            "negative_part_sha256": encoded_digest(la_encode(negative22)),
            "negative_part": la_encode(negative22),
        },
        "D22_raw": {
            "identity": "D22_raw=-L22(g22), L22(R)=-40*A^3*A_x*R-8*A^4*R_x",
            "minimum_A_exponent": min(power for power, _ in d22_raw),
            "mod_A": la_encode(la_mod_a(1, d22_raw)),
            "conclusion": "D22_raw is in (A), hence cannot equal the scalar 1",
        },
        "synthetic_c22": {
            "term": "c22/A^5",
            "operator_image": [],
            "raw_slot_present": False,
            "conclusion": "the optional newborn kernel cannot change D22_raw",
        },
        "formal_mutations": {
            "D18_only_one_A": "leaves an A^-1 pole",
            "D20_only_one_A": "leaves an A^-1 pole",
            "omit_c18_mode": "misses the independent c18/A^3 birth pole",
            "omit_c20_mode": "misses the independent c20/A^4 birth pole",
        },
    }


# Independent dense Q[X] recurrence for literal RAW_DIRECT_SYSTEM replay.
def xp_trim(item):
    answer = list(item)
    while answer and answer[-1] == 0:
        answer.pop()
    return answer


def xp_add(*items):
    size = max((len(item) for item in items), default=0)
    return xp_trim([
        sum((item[index] if index < len(item) else Q(0) for item in items), Q(0))
        for index in range(size)
    ])


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
    return xp_trim([Q(index) * item[index] for index in range(1, len(item))])


def xp_encode(item):
    return {str(index): str(value) for index, value in enumerate(item) if value}


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


def literal_rows(F, G):
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
    direct = literal_rows(F, G)
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


def literal_window_certificate(raw, weight):
    window = raw["windows"]["G"][str(weight)]
    row_generators = [(index, generator)
                      for index, generator in enumerate(raw["generators"])
                      if int(generator["row"]) == weight]
    columns = []
    provenance = []
    for degree, slot in zip(range(window["lower"], window["upper"] + 1),
                            window["slots"]):
        direct, serialized = assert_all_513(raw, {slot: Q(1)})
        columns.append([serialized[index] for index, _ in row_generators])
        provenance.append({
            "G_degree": degree,
            "slot": slot,
            "literal_D_row": xp_encode(direct[weight]),
        })
    matrix = [[columns[column][row] for column in range(len(columns))]
              for row in range(len(row_generators))]
    rank = rational_rank(matrix)
    assert rank == len(columns) == window["dimension"]
    return {
        "weight": weight,
        "raw_G_window": window,
        "literal_D_row_sha256": raw["per_row"][str(weight)]["row_sha256"],
        "literal_D_generator_indices_zero_based": [index for index, _ in row_generators],
        "matrix_shape": [len(matrix), len(columns)],
        "rank": rank,
        "nullity": len(columns) - rank,
        "columns": provenance,
        "enforcement": (
            "the full characteristic coefficient must equal this literal polynomial "
            "window; quotient symbols h18..h21 are not substituted for raw G slots"
        ),
    }


def row_provenance(raw, serialized, weight):
    return {
        "row": weight,
        "row_sha256": raw["per_row"][str(weight)]["row_sha256"],
        "nonzero_generators": [
            {"generator_index_zero_based": index,
             "x_degree": int(generator["x_degree"]),
             "generator_sha256": generator["sha256"],
             "value": str(value)}
            for index, (generator, value) in enumerate(zip(raw["generators"], serialized))
            if int(generator["row"]) == weight and value
        ],
    }


def polynomial(terms):
    answer = [Q(0)] * (max(terms, default=-1) + 1)
    for degree, value in terms.items():
        answer[degree] = Q(value)
    return xp_trim(answer)


def execute_mutation(raw, assignments, row, expected):
    values = {}
    for kind, weight, value in assignments:
        put_window(raw, values, kind, weight, value)
    direct, serialized = assert_all_513(raw, values)
    assert all(not direct[weight] for weight in range(4, row))
    assert direct[row] == expected
    return {
        "first_residual_row": row,
        "prior_rows_zero": list(range(4, row)),
        "residual": xp_encode(expected),
        "literal_row_provenance": row_provenance(raw, serialized, row),
        "all_513_generators_match_independent_determinant_recurrence": True,
    }


def literal_mutations(raw):
    A = polynomial({0: -1, 4: 1})
    X = polynomial({1: 1})
    X2 = polynomial({2: 1})
    X4 = polynomial({4: 1})
    A2 = xp_power(A, 2)

    residuals = {
        18: polynomial({1: 6, 5: -24, 9: 18}),
        19: polynomial({1: -3, 5: 15, 9: -12}),
        20: polynomial({1: 6, 5: -36, 9: 30}),
        21: polynomial({3: -6, 7: 27, 11: -21}),
    }

    def recipe18(scalar):
        C = xp_scale(scalar, X)
        return [
            ("F", 9, C),
            ("G", 9, xp_scale(Q(3, 2), xp_mul(A2, C))),
            ("G", 10, xp_scale(Q(3, 4), C)),
        ]

    def recipe19(scalar):
        C = xp_scale(scalar, xp_mul(A, X))
        return [
            ("F", 9, C),
            ("G", 9, xp_scale(Q(3, 2), xp_mul(A2, C))),
            ("G", 10, xp_scale(Q(3, 4), C)),
            ("G", 18, xp_scale(Q(3, 8) * scalar * scalar, X2)),
        ]

    def recipe20(scalar):
        D = xp_scale(scalar, X)
        return [
            ("F", 10, D),
            ("G", 10, xp_scale(Q(3, 2), xp_mul(A2, D))),
            ("G", 11, xp_scale(Q(3, 4), D)),
        ]

    def recipe21(scalar):
        D = xp_scale(scalar, xp_mul(A, X2))
        return [
            ("F", 10, D),
            ("G", 10, xp_scale(Q(3, 2), xp_mul(A2, D))),
            ("G", 11, xp_scale(Q(3, 4), D)),
            ("G", 20, xp_scale(Q(3, 8) * scalar * scalar, X4)),
        ]

    recipes = {18: recipe18, 19: recipe19, 20: recipe20, 21: recipe21}
    controls = {}
    for weight in range(18, 22):
        control = execute_mutation(raw, recipes[weight](Q(1)), weight,
                                   residuals[weight])
        control["scaling_power"] = 2
        control["scaled_replays"] = {}
        for scalar in (Q(-1), Q(2)):
            replay = execute_mutation(
                raw, recipes[weight](scalar), weight,
                xp_scale(scalar * scalar, residuals[weight]))
            control["scaled_replays"][str(scalar)] = replay["residual"]
        controls[f"D{weight}_first_failure"] = control

    baseline_direct, baseline_serialized = assert_all_513(raw, {})
    assert all(not baseline_direct[weight] for weight in range(4, 23))
    assert baseline_serialized[495] == Q(-1)
    assert raw["generators"][495]["row"] == 22
    assert raw["generators"][495]["x_degree"] == 0
    assert raw["generators"][495]["terms"][0] == [[], "-1"]

    # Pin the endpoint transfer sign independently in Q[X].
    numerator = polynomial({1: Q(-1, 8), 5: Q(1, 40)})
    assert xp_scale(8, xp_derivative(numerator)) == A
    reversed_numerator = xp_scale(-1, numerator)
    assert xp_scale(8, xp_derivative(reversed_numerator)) == xp_scale(-1, A)

    return {
        **controls,
        "endpoint_convention": {
            "exact_square_rows_D4_through_D22_before_target_fold": "zero",
            "folded_D22_constant_generator_index_zero_based": 495,
            "folded_D22_constant_generator_value": "-1",
            "generator_convention": "D22_raw-1",
            "generator_sha256": raw["generators"][495]["sha256"],
            "particular_sign_check": (
                "N=X^5/40-X/8 has 8*N'=A, so g22=N/A^5 gives "
                "L22(g22)=-1 and D22_raw=+1"
            ),
            "reversed_sign_mutation": "g22=-N/A^5 gives D22_raw=-1 and fails",
            "G22_raw_slot_present": False,
        },
    }


def calculate_result():
    assert digest(RAW) == RAW_SHA256
    predecessor = replay_predecessor()
    raw = json.loads(RAW.read_text())
    assert raw["variable_count"] == 303
    assert raw["generator_count"] == len(raw["generators"]) == 513
    assert raw["charged_rows"] == {
        "zero": list(range(7, 22)),
        "affine_target": {"row": 22, "value": 1},
        "D23_imposed": False,
    }
    assert "22" not in raw["windows"]["G"]
    calculation = characteristic_calculation()
    windows = {f"G{weight}": literal_window_certificate(raw, weight)
               for weight in range(18, 22)}
    mutations = literal_mutations(raw)

    modes = []
    for birth, exponent in MODES.items():
        status = {
            6: "killed_at_D8",
            10: "killed_at_D11",
            14: "killed_at_D14",
            16: "retained_and_forced_by_D16",
            18: "killed_at_D18_by_literal_polynomiality",
            20: "killed_at_D20_by_literal_polynomiality",
        }.get(birth, "retained_live")
        modes.append({
            "birth_weight": birth,
            "F_exponent": str(exponent),
            "birth_A_power": int(4 * exponent),
            "continuation_status": status,
        })

    return {
        "schema": "jc2.ggv.upper_endpoint.uniform_d18_d22_fullmodes.independent.result.v1",
        "status": "PASS_ENDPOINT_TARGET_IMPOSSIBLE_ON_FROZEN_UNIFORM_BRANCH_P_FIXTURE",
        "source": {
            "authoritative_raw_system": str(RAW.relative_to(ROOT)),
            "authoritative_raw_system_sha256": RAW_SHA256,
            "predecessor_checker": str(PREDECESSOR.relative_to(ROOT)),
            "predecessor_checker_sha256": PREDECESSOR_SHA256,
            "predecessor_result": str(PREDECESSOR_RESULT.relative_to(ROOT)),
            "predecessor_result_sha256": PREDECESSOR_RESULT_SHA256,
            "predecessor_replay_status": predecessor["status"],
            "raw_variable_count": raw["variable_count"],
            "raw_generator_count": raw["generator_count"],
            "literal_row_sha256": {
                str(weight): raw["per_row"][str(weight)]["row_sha256"]
                for weight in range(18, 23)
            },
        },
        "complete_nine_mode_schedule": modes,
        "calculation": calculation,
        "literal_raw_window_certificates": windows,
        "literal_raw_mutations": mutations,
        "window_firewall": [
            "G18 is exactly X^2*Q[X] of degree at most 6 (five frozen slots)",
            "G19 is exactly X^3*Q[X] of degree at most 5 (three frozen slots)",
            "G20 is exactly X^3*Q[X] of degree at most 4 (two frozen slots)",
            "G21 is exactly a scalar multiple of X^3 (one frozen slot)",
            "after each pole cancellation, the full characteristic coefficient—not merely its A-adic quotient—must equal the corresponding literal window",
            "all absent low/high coefficients remain live constraints; none is dropped or used as a normalization",
            "the endpoint contradiction is stronger: it needs only these full coefficients to be polynomial, so every stricter literal-window solution is covered",
        ],
        "theorem": {
            "D18": "c18=0 and R18=A^2*h18",
            "D19": "R19=A^2*h19",
            "D20": "c20=0 and R20=A^2*h20",
            "D21": "R21=A^2*h21",
            "D22": (
                "the nine-mode g22 has A-pole order at most 2; hence "
                "D22_raw=-L22(g22) lies in (A) and cannot equal 1"
            ),
            "conclusion": (
                "no field point of the frozen 303-variable/513-generator uniform "
                "upper branch-P fixture satisfies D4=...=D21=0 and D22=1"
            ),
        },
        "universalization_boundary": {
            "new_D18_D22_A_adic_steps": (
                "use only that A is a nonconstant polynomial/nonunit; they do not "
                "evaluate roots or use the coefficients of X^4-1"
            ),
            "fixed_A_gate": (
                "the authoritative raw-window shapes, slot maps, row hashes, and the "
                "normalization feeding the frozen D16/D17 packet are fixture-specific "
                "to A=X^4-1"
            ),
            "claim_scope": "no universalized fixture theorem is claimed here",
        },
        "scope_firewall": [
            "this closes only the frozen uniform upper branch-P endpoint fixture charged by the predecessor packet",
            "it does not assert that every JC2 branch has been transported into this fixture",
            "all nine admitted modes c4 through c20 are present; c6,c10,c14,c18,c20 are killed only at their audited rows",
            "a synthetic newborn c22/A^5 is not a raw variable and is an L22-kernel, so it cannot change D22_raw",
            "literal G18--G21 lower and upper window equations are retained even though the terminal divisibility argument does not need their extra strength",
            "no gauge, root, carrier, sign branch, or unit is selected",
            "no cutoff-three transport identity is asserted",
            "standard-library exact arithmetic only; no CAS, AWS, or jc2-lean access",
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
            "theorem": result["theorem"],
            "g22_min_A_exponent": result["calculation"]["g22_after_D21"][
                "minimum_A_exponent"],
            "D22_raw_mod_A": result["calculation"]["D22_raw"]["mod_A"],
            "check": arguments.check,
        }, sort_keys=True))


if __name__ == "__main__":
    main()
