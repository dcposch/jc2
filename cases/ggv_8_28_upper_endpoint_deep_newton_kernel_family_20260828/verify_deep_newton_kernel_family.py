#!/usr/bin/env python3
"""Exact checks for the deep A|V0 Newton/kernel packet.

The universal arguments are proved in the accompanying report.  This
standard-library checker pins the literal-tail implementation and replays
the exact identities used as computational evidence:

* the literal point and its t-rescaling covariance through weight 22;
* the pure A^-5 endpoint kernel coefficient;
* the four simultaneous critical-factor vanishings at (X,t)=(0,8);
* the endpoint operator/primitive identity and its order-3/order-5 poles;
* sample instances of the common-root even Newton-face residue recurrence.

It is intentionally small and performs no search.
"""

from __future__ import annotations

from fractions import Fraction as Q
import hashlib
import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TAIL = (
    ROOT
    / "cases/ggv_8_28_upper_endpoint_active_c2_literal_d16_d22_probe_20260828"
    / "probe_literal_tail.py"
)
TAIL_SHA256 = "f3371687df3584bd1dbeac9e9ad05aca8212a6dd35b63c17209916ab9d11fb45"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_tail():
    assert sha256(TAIL) == TAIL_SHA256
    spec = importlib.util.spec_from_file_location("deep_tail_frozen", TAIL)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def p_eval(poly, value):
    out = Q(0)
    for coefficient in reversed(poly):
        out = out * value + coefficient
    return out


def series_mul(left, right, maximum):
    out = [Q(0)] * (maximum + 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j <= maximum:
                out[i + j] += a * b
    return out


def series_power(base, exponent, maximum):
    """Generalized power of a series with constant coefficient one."""
    assert base[0] == 1
    u = list(base)
    u[0] -= 1
    out = [Q(0)] * (maximum + 1)
    power = [Q(0)] * (maximum + 1)
    power[0] = 1
    choose = Q(1)
    for k in range(maximum + 1):
        if k:
            power = series_mul(power, u, maximum)
            choose *= (exponent - (k - 1)) / k
        for degree, coefficient in enumerate(power):
            out[degree] += choose * coefficient
    return out


def face_characteristic(p, low_modes):
    """Kill z^7,...,z^10 by the born modes and return z^11 residue."""
    maximum = 11
    result = series_power(p, Q(3, 2), maximum)
    modes = dict(low_modes)
    for k in range(1, 11):
        if k >= 7:
            modes[k] = -result[k]
        mode = modes.get(k, Q(0))
        if mode:
            power = series_power(p, Q(6 - k, 4), maximum - k)
            for degree, coefficient in enumerate(power):
                result[degree + k] += mode * coefficient
    assert result[7:11] == [Q(0)] * 4
    return modes, result[11]


def main():
    tail = load_tail()
    up = tail.load_upstream()

    A = [Q(-1), Q(0), Q(0), Q(0), Q(1)]
    Z = up.p_scale(Q(1, 2), up.p_add([Q(1)], up.p_scale(-1, A)))
    F4 = up.p_scale(Q(1, 64), up.p_add(up.p_mul(Z, Z), up.p_scale(-1, A)))
    F5 = up.p_scale(Q(1, 512), up.p_add(A, [Q(-1)]))
    F_laurent = {
        0: {4: [Q(1)]},
        1: {3: [Q(1)]},
        2: {2: up.p_scale(Q(1, 4), up.p_add([Q(1)], Z))},
        3: {1: up.p_scale(Q(1, 8), up.p_add(Z, up.p_scale(Q(-1, 4), A)))},
        4: {0: F4},
        5: {0: F5},
        6: {0: [Q(1, 4096)]},
        **{weight: {} for weight in range(7, 23)},
    }
    modes = {
        2: Q(1), 4: Q(0), 6: Q(1), 8: Q(0), 10: Q(0), 12: Q(0),
        14: Q(-6139, 17179869184), 16: Q(0),
        18: Q(16369, 140737488355328), 20: Q(0),
    }
    characteristic = tail.characteristic_special(up, F_laurent, modes, 22)

    # Exact covariance F_s(X,t)=F_1(X,s*t), G_s(X,t)=G_1(X,s*t).
    scale = Q(2)
    scaled_F = {
        weight: {
            a_power: up.p_scale(scale ** weight, coefficient)
            for a_power, coefficient in row.items()
        }
        for weight, row in F_laurent.items()
    }
    scaled_modes = {weight: scale ** weight * value
                    for weight, value in modes.items()}
    scaled_characteristic = tail.characteristic_special(
        up, scaled_F, scaled_modes, 22
    )
    for weight in range(23):
        expected = {
            a_power: up.p_scale(scale ** weight, coefficient)
            for a_power, coefficient in characteristic[weight].items()
        }
        assert scaled_characteristic[weight] == expected

    # A genuinely two-parameter square-prefix test, not obtained from the
    # literal point by t-rescaling when q != s^2.  It is useful as a bounded
    # discriminator for whether the F-level square family automatically
    # extends to a homogeneous raw solution (it need not).
    test_s, test_q = Q(1), Q(2)
    test_Z = up.p_scale(Q(1, 2), up.p_add(
        [test_s * test_s], up.p_scale(-test_q, A)
    ))
    test_U = -test_q * test_s / 4
    test_R = -test_q * test_s * test_s
    test_F4 = up.p_scale(Q(1, 64), up.p_add(
        up.p_mul(test_Z, test_Z), up.p_scale(test_R, A)
    ))
    test_F5 = up.p_scale(
        test_s * test_q / 512,
        up.p_add(up.p_scale(test_q, A), [-test_s * test_s]),
    )
    test_F6 = [test_s * test_s * test_q * test_q / 4096]
    test_prefix = {
        0: {4: [Q(1)]},
        1: {3: [test_s]},
        2: {2: up.p_scale(Q(1, 4), up.p_add([test_s * test_s], test_Z))},
        3: {1: up.p_scale(Q(1, 8), up.p_add(
            up.p_scale(test_s, test_Z), up.p_scale(test_U, A)
        ))},
        4: {0: test_F4}, 5: {0: test_F5}, 6: {0: test_F6},
        **{weight: {} for weight in range(7, 23)},
    }
    test_modes = {
        weight: test_q ** (weight // 2) * value
        for weight, value in modes.items()
    }
    test_characteristic = tail.characteristic_special(
        up, test_prefix, test_modes, 22
    )
    test_polynomial = True
    test_raw_G = {}
    for weight in range(22):
        polynomial, den, power = tail.fraction_of_laurent(
            up, test_characteristic[weight], A
        )
        if den != [Q(1)] or power:
            test_polynomial = False
            break
        test_raw_G[weight] = polynomial
    assert test_polynomial
    test_raw_F = {
        0: up.p_power(A, 4),
        1: up.p_scale(test_s, up.p_power(A, 3)),
        2: up.p_scale(Q(1, 4), up.p_mul(
            up.p_power(A, 2), up.p_add([test_s * test_s], test_Z)
        )),
        3: up.p_scale(Q(1, 8), up.p_mul(
            A, up.p_add(up.p_scale(test_s, test_Z), up.p_scale(test_U, A))
        )),
        4: test_F4, 5: test_F5, 6: test_F6,
        **{weight: [] for weight in range(7, 23)},
    }
    test_raw_G[22] = []
    assert all(not test_raw_G[weight] for weight in range(13, 22))
    assert all(not row for row in up.determinant_rows(
        test_raw_F, test_raw_G, 22
    ).values())
    test_num22, test_den22, test_power22 = tail.fraction_of_laurent(
        up, test_characteristic[22], A
    )
    assert test_num22 == [
        test_q ** 11 * Q(9207, 144115188075855872)
    ]
    assert test_den22 == up.p_power(A, 5) and test_power22 == 5
    mutated_modes = dict(test_modes)
    mutated_modes[18] = Q(0)
    mutated_characteristic = tail.characteristic_special(
        up, test_prefix, mutated_modes, 18
    )
    _, _, mutated_power = tail.fraction_of_laurent(
        up, mutated_characteristic[18], A
    )
    assert mutated_power > 0

    numerator, denominator, denominator_power = tail.fraction_of_laurent(
        up, characteristic[22], A
    )
    assert numerator == [Q(9207, 144115188075855872)]
    assert denominator_power == 5 and denominator == up.p_power(A, 5)

    # Reconstruct literal raw F,G and the determinant's four base factors.
    F = {
        0: up.p_power(A, 4),
        1: up.p_power(A, 3),
        2: up.p_scale(Q(1, 4), up.p_mul(up.p_power(A, 2), up.p_add([Q(1)], Z))),
        3: up.p_scale(Q(1, 8), up.p_mul(A, up.p_add(Z, up.p_scale(Q(-1, 4), A)))),
        4: F4, 5: F5, 6: [Q(1, 4096)],
        **{weight: [] for weight in range(7, 23)},
    }
    G = {}
    for weight in range(22):
        polynomial, den, power = tail.fraction_of_laurent(
            up, characteristic[weight], A
        )
        assert den == [Q(1)] and power == 0
        G[weight] = polynomial
    G[22] = []

    x0, t0 = Q(0), Q(8)
    f_value = sum(p_eval(F[i], x0) * t0 ** i for i in F)
    fx_value = sum(p_eval(up.p_derivative(F[i]), x0) * t0 ** i for i in F)
    ft_value = sum(i * p_eval(F[i], x0) * t0 ** (i - 1)
                   for i in F if i)
    g_value = sum(p_eval(G[i], x0) * t0 ** i for i in G)
    gx_value = sum(p_eval(up.p_derivative(G[i]), x0) * t0 ** i for i in G)
    gt_value = sum(i * p_eval(G[i], x0) * t0 ** (i - 1)
                   for i in G if i)
    assert (f_value, fx_value, t0 * ft_value - 8 * f_value) == (Q(9), Q(0), Q(0))
    assert (g_value, gx_value, 12 * g_value - t0 * gt_value) == (
        Q(1309349), Q(0), Q(0)
    )

    # Universal endpoint operator identity for a nontrivial test polynomial R.
    R = [Q(3), Q(-2), Q(5, 7), Q(0), Q(11)]
    left_operator = up.p_add(
        up.p_scale(-40, up.p_mul(up.p_mul(up.p_power(A, 3), up.p_derivative(A)), R)),
        up.p_scale(-8, up.p_mul(up.p_power(A, 4), up.p_derivative(R))),
    )
    assert up.p_scale(-1, up.p_mul(A, left_operator)) == up.p_scale(
        8, up.p_derivative(up.p_mul(up.p_power(A, 5), R))
    )
    primitive_over_eight = [Q(0), Q(-1, 8), Q(0), Q(0), Q(0), Q(1, 40)]
    assert up.p_derivative(primitive_over_eight) == up.p_scale(Q(1, 8), A)

    # The common-root even face p(z): two independent exact samples.  The
    # recursively born modes kill z^7..z^10 and leave a definite z^11 residue.
    samples = [
        (Q(1), Q(0), Q(0), {1: Q(1), 3: Q(1)}),
        (Q(-3, 2), Q(7), Q(-2, 5), {1: Q(2), 2: Q(-1), 6: Q(3, 7)}),
    ]
    residues = []
    born_modes = []
    for q, e, f8, low_modes in samples:
        p = [
            Q(1), -q / 8, q * q / 256,
            e / 2048, f8,
        ] + [Q(0)] * 7
        born, residue = face_characteristic(p, low_modes)
        assert all(k in born for k in range(7, 11))
        born_modes.append(born)
        residues.append(residue)
    assert born_modes[0][7] == Q(-6139, 17179869184)
    assert born_modes[0][8] == 0
    assert born_modes[0][9] == Q(16369, 140737488355328)
    assert born_modes[0][10] == 0
    assert residues[0] == Q(9207, 144115188075855872)
    assert residues[0] != residues[1]

    # Newton-face pole coefficients used in the universal root argument.
    # If p1 != 0, G15 has the uncancellable coefficient
    # binom(3/2,3)*(p1/256)^3*A^-3.  Once p1=0, if F7 != 0,
    # G14 has binom(3/2,2)*F7^2*A^-2.
    choose_3 = Q(3, 2) * Q(1, 2) * Q(-1, 2) / 6
    choose_2 = Q(3, 2) * Q(1, 2) / 2
    assert choose_3 == Q(-1, 16)
    assert choose_2 == Q(3, 8)

    print("literal_g22_kernel=9207/(2^57*A^5)")
    print("two_parameter_square_test_q2_polynomial_through_21=" + str(test_polynomial))
    print("critical_point=(0,8); all_four_determinant_factors_zero")
    print("common_root_newton_forces=P1(alpha)=F7(alpha)=0")
    print("face_residues=" + ",".join(str(value) for value in residues))
    print("PASS_EXACT_DEEP_NEWTON_KERNEL_FAMILY")


if __name__ == "__main__":
    main()
