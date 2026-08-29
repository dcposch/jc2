#!/usr/bin/env python3
"""Exact tail probe for the active-c2 literal D0..D15 survivor.

This is deliberately a small discriminator, not a theorem.  It pins and
loads the frozen independent D8--D15 checker, extends its characteristic
recurrence to weight 22, and solves the newly born scalar modes one at a
time by exact rational polynomial division.  It also enforces the literal
lower and upper X-degree windows from the authoritative branch-P compiler.
"""

from __future__ import annotations

from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
UPSTREAM = (
    ROOT
    / "cases/ggv_8_28_upper_endpoint_active_c2_d11_d13_extension_20260828"
    / "verify_active_c2_extension.py"
)
UPSTREAM_SHA256 = (
    "112650dc27b0e13d76979d5adca9315919ee65cb8d9eaf717c1685f99d96de26"
)
RAW_COMPILER = ROOT / "cases/ggv_8_28_upper_endpoint_branch_p_20260827/compile_endpoint.py"
RAW_COMPILER_SHA256 = (
    "7f840af57695eb0f4e124885a39eabdd0059dad984c917b826d077c77d396be1"
)
RAW_SOURCE = ROOT / "cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json"
RAW_SOURCE_SHA256 = (
    "ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0"
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_upstream():
    assert sha256(UPSTREAM) == UPSTREAM_SHA256
    assert sha256(RAW_COMPILER) == RAW_COMPILER_SHA256
    assert sha256(RAW_SOURCE) == RAW_SOURCE_SHA256
    spec = importlib.util.spec_from_file_location("active_c2_frozen", UPSTREAM)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def l_add(up, *items):
    out = {}
    for item in items:
        for exponent, coefficient in item.items():
            out[exponent] = up.p_add(out.get(exponent, []), coefficient)
            if not out[exponent]:
                del out[exponent]
    return out


def l_scale(up, scalar, item):
    return {exponent: up.p_scale(scalar, coefficient)
            for exponent, coefficient in item.items()
            if up.p_scale(scalar, coefficient)}


def l_mul(up, left, right):
    out = {}
    for left_exponent, left_coefficient in left.items():
        for right_exponent, right_coefficient in right.items():
            exponent = left_exponent + right_exponent
            product = up.p_mul(left_coefficient, right_coefficient)
            out[exponent] = up.p_add(out.get(exponent, []), product)
            if not out[exponent]:
                del out[exponent]
    return out


def l_shift(item, exponent):
    return {old + exponent: coefficient for old, coefficient in item.items()}


def fractional_series_special(up, F, exponent, maximum):
    out = {0: {int(4 * exponent): [Q(1)]}}
    for n in range(1, maximum + 1):
        numerator = {}
        for i in range(1, n + 1):
            numerator = l_add(
                up,
                numerator,
                l_scale(
                    up,
                    (exponent + 1) * i - n,
                    l_mul(up, F[i], out[n - i]),
                ),
            )
        out[n] = l_scale(up, Q(1, n), l_shift(numerator, -4))
    return out


def characteristic_special(up, F, modes, maximum):
    exponents = set(up.MODES.values()) | {Q(3, 2)}
    powers = {
        exponent: fractional_series_special(up, F, exponent, maximum)
        for exponent in exponents
    }
    G = {}
    for n in range(maximum + 1):
        row = powers[Q(3, 2)][n]
        for birth, exponent in up.MODES.items():
            if birth <= n and modes.get(birth):
                row = l_add(
                    up,
                    row,
                    l_scale(up, modes[birth], powers[exponent][n - birth]),
                )
        G[n] = row
    return G


def fraction_of_laurent(up, item, A):
    """Return a reduced-enough polynomial numerator and A-power denominator."""
    if not item:
        return [], [Q(1)], 0
    minimum = min(item)
    denominator_power = max(0, -minimum)
    numerator = []
    for a_exponent, coefficient in item.items():
        piece = up.p_mul(
            coefficient, up.p_power(A, a_exponent + denominator_power)
        )
        numerator = up.p_add(numerator, piece)
    denominator = up.p_power(A, denominator_power)
    quotient, remainder = up.p_divmod(numerator, denominator)
    if not remainder:
        return quotient, [Q(1)], 0
    while denominator_power:
        quotient, remainder = up.p_divmod(numerator, A)
        if remainder:
            break
        numerator = quotient
        denominator_power -= 1
    denominator = up.p_power(A, denominator_power)
    return numerator, denominator, denominator_power


def affine_scalar_for_polynomiality(up, expression0, expression1, A, name):
    """Solve the unique scalar making an affine Laurent expression polynomial."""
    num0, den0, power0 = fraction_of_laurent(up, expression0, A)
    num1, den1, power1 = fraction_of_laurent(up, expression1, A)

    # Compare at one common A-power before taking remainders.
    power = max(power0, power1)
    common = up.p_power(A, power)

    def common_numerator(num, old_power):
        return up.p_mul(num, up.p_power(A, power - old_power))

    n0 = common_numerator(num0, power0)
    n1 = common_numerator(num1, power1)
    delta = up.p_add(n1, up.p_scale(-1, n0))
    _, r0 = up.p_divmod(n0, common)
    _, rd = up.p_divmod(delta, common)

    scalar = None
    size = max(len(r0), len(rd))
    for index in range(size):
        a = r0[index] if index < len(r0) else Q(0)
        b = rd[index] if index < len(rd) else Q(0)
        if b:
            candidate = -a / b
            scalar = candidate if scalar is None else scalar
            assert scalar == candidate, (name, index, scalar, candidate)
        else:
            assert not a, (name, index, a)
    assert scalar is not None, (name, "mode does not control a pole")

    solved_expression = l_add(
        up, expression0,
        l_scale(up, scalar, l_add(up, expression1, l_scale(up, -1, expression0)))
    )
    polynomial, denominator, denominator_power = fraction_of_laurent(
        up, solved_expression, A
    )
    assert denominator_power == 0 and denominator == [Q(1)]
    return scalar, polynomial


def legal_window(poly, lower, upper):
    support = [index for index, coefficient in enumerate(poly) if coefficient]
    return all(lower <= degree <= upper for degree in support), support


def p_product(up, *items):
    out = [Q(1)]
    for item in items:
        out = up.p_mul(out, item)
    return out


def main():
    up = load_upstream()

    A = [Q(-1), Q(0), Q(0), Q(0), Q(1)]
    Z = up.p_scale(Q(1, 2), up.p_add([Q(1)], up.p_scale(-1, A)))
    U = [Q(-1, 4)]
    R = [Q(-1)]
    F4 = up.p_scale(Q(1, 64), up.p_add(up.p_mul(Z, Z), up.p_mul(A, R)))
    F5 = up.p_scale(Q(1, 512), up.p_add(A, [Q(-1)]))
    F = {
        0: {4: [Q(1)]},
        1: {3: [Q(1)]},
        2: {2: up.p_scale(Q(1, 4), up.p_add([Q(1)], Z))},
        3: {1: up.p_scale(Q(1, 8), up.p_add(
            Z, up.p_scale(Q(-1, 4), A)
        ))},
        4: {0: F4},
        5: {0: F5},
        6: {0: [Q(1, 4096)]},
        **{n: {} for n in range(7, 23)},
    }
    modes = {
        2: Q(1),
        4: Q(0),
        6: Q(1),
        8: Q(0),
        10: Q(0),
        12: Q(0),
        14: Q(-6139, 17179869184),
        16: Q(0),
        18: Q(0),
        20: Q(0),
    }

    # Reproduce the frozen D0..D15 raw point before extending it.
    prefix_characteristic = characteristic_special(up, F, modes, 15)
    raw_F = {
        0: up.p_power(A, 4),
        1: up.p_power(A, 3),
        2: up.p_mul(up.p_power(A, 2), F[2][2]),
        3: up.p_mul(A, F[3][1]),
        4: F4,
        5: F5,
        6: [Q(1, 4096)],
        **{n: [] for n in range(7, 16)},
    }
    raw_G = {}
    for weight in range(16):
        polynomial, denominator, power = fraction_of_laurent(
            up, prefix_characteristic[weight], A
        )
        assert power == 0 and denominator == [Q(1)], ("prefix", weight, power)
        raw_G[weight] = polynomial
    raw_D = up.determinant_rows(raw_F, raw_G, 15)
    assert all(not raw_D[weight] for weight in range(16))
    assert raw_G[12] == [Q(4093, 268435456)]
    assert raw_G[13] == raw_G[14] == raw_G[15] == []

    windows = {
        16: (2, 8),
        17: (2, 7),
        18: (2, 6),
        19: (3, 5),
        20: (3, 4),
        21: (3, 3),
    }
    solved_modes = {}
    rows = {}
    c18_zero_has_pole = None
    for weight in range(16, 22):
        born = {16: 16, 18: 18, 20: 20}.get(weight)
        if born:
            modes[born] = Q(0)
            expression0 = characteristic_special(up, F, modes, weight)[weight]
            modes[born] = Q(1)
            expression1 = characteristic_special(up, F, modes, weight)[weight]
            mode_name = f"c{born}"
            scalar, polynomial = affine_scalar_for_polynomiality(
                up, expression0, expression1, A, mode_name
            )
            if born == 18:
                _, _, zero_power = fraction_of_laurent(up, expression0, A)
                c18_zero_has_pole = zero_power > 0
            modes[born] = scalar
            solved_modes[mode_name] = scalar
        else:
            expression = characteristic_special(up, F, modes, weight)[weight]
            polynomial, denominator, power = fraction_of_laurent(
                up, expression, A
            )
            assert power == 0 and denominator == [Q(1)], (weight, power)
        legal, support = legal_window(polynomial, *windows[weight])
        rows[weight] = {
            "polynomial": [str(value) for value in polynomial],
            "support": support,
            "window": list(windows[weight]),
            "window_pass": legal,
        }
        if not legal:
            print(json.dumps({
                "status": "TAIL_WINDOW_OBSTRUCTION",
                "first_weight": weight,
                "solved_modes": {k: str(v) for k, v in solved_modes.items()},
                "rows": rows,
            }, indent=2, sort_keys=True))
            return

    g22_expression = characteristic_special(up, F, modes, 22)[22]
    g22_num, g22_den, g22_power = fraction_of_laurent(up, g22_expression, A)
    Aprime = up.p_derivative(A)
    g22_num_prime = up.p_derivative(g22_num)
    g22_den_prime = up.p_derivative(g22_den)
    # For R=N/D, -L22(R)=40 A^3 A' N/D + 8 A^4 (N'D-ND')/D^2.
    endpoint_numerator = up.p_add(
        up.p_scale(40, p_product(
            up, up.p_power(A, 3), Aprime, g22_num, g22_den
        )),
        up.p_scale(8, up.p_mul(up.p_power(A, 4), up.p_add(
            up.p_mul(g22_num_prime, g22_den),
            up.p_scale(-1, up.p_mul(g22_num, g22_den_prime)),
        ))),
    )
    endpoint_denominator = up.p_mul(g22_den, g22_den)
    endpoint, endpoint_remainder = up.p_divmod(
        endpoint_numerator, endpoint_denominator
    )
    endpoint_is_polynomial = not endpoint_remainder
    assert solved_modes == {
        "c16": Q(0),
        "c18": Q(16369, 140737488355328),
        "c20": Q(0),
    }
    assert c18_zero_has_pole
    assert all(not rows[weight]["polynomial"] for weight in rows)
    assert g22_power == 5
    assert g22_num == [Q(9207, 144115188075855872)]
    assert endpoint_is_polynomial and not endpoint
    full_raw_F = dict(raw_F)
    full_raw_F.update({weight: [] for weight in range(16, 23)})
    full_raw_G = dict(raw_G)
    full_raw_G.update({weight: [] for weight in range(16, 23)})
    full_raw_D = up.determinant_rows(full_raw_F, full_raw_G, 22)
    assert all(not full_raw_D[weight] for weight in range(23))
    assert full_raw_D[22] == endpoint
    # Changing the endpoint operator coefficient from -40 to -39 leaves
    # -k*A'/A^2 on the exact kernel k*A^-5 instead of annihilating it.
    assert Q(39) - Q(8) * Q(5) == Q(-1)

    print(json.dumps({
        "status": "TAIL_CHARACTERISTIC_WINDOWS_PASS",
        "solved_modes": {k: str(v) for k, v in solved_modes.items()},
        "rows": rows,
        "g22_denominator_A_power": g22_power,
        "g22_numerator": [str(value) for value in g22_num],
        "endpoint_is_polynomial": endpoint_is_polynomial,
        "endpoint": [str(value) for value in endpoint] if endpoint_is_polynomial else None,
        "endpoint_remainder": [str(value) for value in endpoint_remainder],
        "endpoint_equals_one": endpoint_is_polynomial and endpoint == [Q(1)],
        "mutations": {
            "c18_zero_leaves_pole": c18_zero_has_pole,
            "endpoint_minus39_kernel_residual_scalar": "-1",
        },
    }, indent=2, sort_keys=True))
    print("PASS_EXACT_ACTIVE_C2_LITERAL_D16_D22_TAIL")


if __name__ == "__main__":
    main()
