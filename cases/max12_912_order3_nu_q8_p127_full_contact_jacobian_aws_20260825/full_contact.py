#!/usr/bin/env python3
"""Exact full-source corrected-Q8 contact/Jacobian check over F_127."""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import importlib.util
import itertools
import json
from pathlib import Path
import sys


P = 127
ROOT = Path(__file__).resolve().parents[2]
COMPILER = ROOT / "cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py"
COMPILER_SHA256 = "22b0cdc446d1e486d08757df5a3fff83b0506a492f16b9b2cf238966eb947545"
Q8_Z = [-24, -296, -1548, -4428, -7320, -6498, -1782, 1539, 999]


def trim(poly):
    result = [value % P for value in poly]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result or [0]


def add(a, b):
    out = [0] * max(len(a), len(b))
    for index, value in enumerate(a):
        out[index] = (out[index] + value) % P
    for index, value in enumerate(b):
        out[index] = (out[index] + value) % P
    return trim(out)


def neg(a):
    return trim([(-value) % P for value in a])


def sub(a, b):
    return add(a, neg(b))


def scale(a, scalar):
    return trim([(scalar % P) * value for value in a])


def multiply_raw(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            out[i + j] = (out[i + j] + left * right) % P
    return trim(out)


def divmod_poly(a, b):
    remainder = trim(a)
    divisor = trim(b)
    if divisor == [0]:
        raise ZeroDivisionError
    quotient = [0] * max(1, len(remainder) - len(divisor) + 1)
    inverse = pow(divisor[-1], P - 2, P)
    while remainder != [0] and len(remainder) >= len(divisor):
        shift = len(remainder) - len(divisor)
        coefficient = remainder[-1] * inverse % P
        quotient[shift] = coefficient
        for index, value in enumerate(divisor):
            remainder[shift + index] = (
                remainder[shift + index] - coefficient * value
            ) % P
        remainder = trim(remainder)
    return trim(quotient), remainder


def monic(poly):
    poly = trim(poly)
    return scale(poly, pow(poly[-1], P - 2, P))


def gcd_poly(a, b):
    a, b = trim(a), trim(b)
    while b != [0]:
        _, remainder = divmod_poly(a, b)
        a, b = b, remainder
    return monic(a)


Q8 = monic([value % P for value in Q8_Z])


def reduce_q8(poly):
    return divmod_poly(poly, Q8)[1]


def mul(a, b):
    return reduce_q8(multiply_raw(a, b))


def power(a, exponent):
    out = [1]
    base = trim(a)
    while exponent:
        if exponent & 1:
            out = mul(out, base)
        base = mul(base, base)
        exponent >>= 1
    return out


def extended_gcd(a, b):
    r0, r1 = trim(a), trim(b)
    s0, s1 = [1], [0]
    t0, t1 = [0], [1]
    while r1 != [0]:
        quotient, remainder = divmod_poly(r0, r1)
        r0, r1 = r1, remainder
        s0, s1 = s1, sub(s0, multiply_raw(quotient, s1))
        t0, t1 = t1, sub(t0, multiply_raw(quotient, t1))
    inverse = pow(r0[-1], P - 2, P)
    return monic(r0), scale(s0, inverse), scale(t0, inverse)


def inverse(a):
    common, coefficient, _ = extended_gcd(a, Q8)
    if common != [1]:
        raise ZeroDivisionError((a, common))
    result = reduce_q8(coefficient)
    if mul(a, result) != [1]:
        raise AssertionError("inverse failure")
    return result


def divide(a, b):
    return mul(a, inverse(b))


def fraction_mod(value: Fraction):
    return value.numerator % P * pow(value.denominator % P, P - 2, P) % P


def determinant(matrix):
    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise RuntimeError("nonsquare determinant")
    total = [0]
    for permutation in itertools.permutations(range(size)):
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(size)
            for j in range(i + 1, size)
        )
        term = [1]
        for row, column in enumerate(permutation):
            term = mul(term, matrix[row][column])
        total = add(total, neg(term) if inversions % 2 else term)
    return total


def determinant_mod_p(matrix):
    data = [[value % P for value in row] for row in matrix]
    result = 1
    for column in range(len(data)):
        pivot = next(
            (row for row in range(column, len(data)) if data[row][column]),
            None,
        )
        if pivot is None:
            return 0
        if pivot != column:
            data[column], data[pivot] = data[pivot], data[column]
            result = -result
        value = data[column][column] % P
        result = result * value % P
        inverse_value = pow(value, P - 2, P)
        for row in range(column + 1, len(data)):
            factor = data[row][column] * inverse_value % P
            for index in range(column, len(data)):
                data[row][index] = (
                    data[row][index] - factor * data[column][index]
                ) % P
    return result % P


def norm(element):
    degree = len(Q8) - 1
    columns = []
    v = [0, 1]
    for exponent in range(degree):
        image = mul(element, power(v, exponent))
        columns.append(image + [0] * (degree - len(image)))
    matrix = [[columns[column][row] for column in range(degree)] for row in range(degree)]
    return determinant_mod_p(matrix)


def load_compiler():
    got = sha256(COMPILER.read_bytes()).hexdigest()
    if got != COMPILER_SHA256:
        raise RuntimeError((str(COMPILER), got, COMPILER_SHA256))
    spec = importlib.util.spec_from_file_location("q8_full_contact_compiler", COMPILER)
    if spec is None or spec.loader is None:
        raise RuntimeError(COMPILER)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def evaluate_sparse(value, bases):
    total = [0]
    for monomial, scalar in value.items():
        term = [fraction_mod(scalar)]
        for base, exponent in zip(bases, monomial, strict=True):
            term = mul(term, power(base, exponent))
        total = add(total, term)
    return total


def linear_normal_system(value, x_bases):
    constant = [0]
    coefficients = [[0], [0], [0]]
    for monomial, scalar in value.items():
        if monomial[0]:
            continue
        normal = monomial[1:4]
        if sum(normal) > 1 or any(exponent not in (0, 1) for exponent in normal):
            raise RuntimeError(("nonlinear normal term at w=0", monomial))
        term = [fraction_mod(scalar)]
        for base, exponent in zip(x_bases, monomial[4:], strict=True):
            term = mul(term, power(base, exponent))
        if sum(normal) == 0:
            constant = add(constant, term)
        else:
            column = normal.index(1)
            coefficients[column] = add(coefficients[column], term)
    return coefficients, constant


def replace_column(matrix, column, values):
    return [
        [values[row] if index == column else entry for index, entry in enumerate(line)]
        for row, line in enumerate(matrix)
    ]


def unit_record(name, value):
    common = gcd_poly(value, Q8)
    value_norm = norm(value)
    if common != [1] or value_norm == 0:
        raise AssertionError((name, common, value_norm))
    return {
        "name": name,
        "value_low_to_high": trim(value),
        "gcd_with_q8": common,
        "norm_mod_127": value_norm,
    }


def main() -> None:
    Q = load_compiler()
    _, rows, imposed, names = Q.compile_quotient("approx")
    if tuple(imposed) != (1, 3, 5, 7, 2, 4):
        raise RuntimeError(imposed)
    if names != ["w", "c", "d2", "d4", "x1", "x3", "x5"]:
        raise RuntimeError(names)

    zero, one, v = [0], [1], [0, 1]
    D = sub(scale(power(v, 2), 3), [2])
    A2 = add(add(scale(power(v, 2), 3), scale(v, 3)), [1])
    x5 = divide(scale(mul(power(v, 2), A2), -36), D)
    x3 = mul(x5, add(v, [2]))
    correct_factor = add(scale(v, 3), [1])
    x1 = add(
        mul(x5, add(v, [1])),
        divide(mul(power(x5, 2), correct_factor), scale(v, 9)),
    )
    wrong_x1 = add(
        mul(x5, add(v, [1])),
        divide(power(x5, 2), scale(v, 27)),
    )

    matrix = []
    rhs = []
    for ell in (3, 5, 7):
        coefficients, constant = linear_normal_system(rows[ell], [x1, x3, x5])
        matrix.append(coefficients)
        rhs.append(neg(constant))
    normal_det = determinant(matrix)
    normal_det_inverse = inverse(normal_det)
    c, d2, d4 = [
        mul(determinant(replace_column(matrix, column, rhs)), normal_det_inverse)
        for column in range(3)
    ]
    localizer_denominator = mul(x5, sub(x3, scale(x5, 2)))
    inv = inverse(localizer_denominator)
    bases = [zero, c, d2, d4, x1, x3, x5]

    row_residuals = {
        f"e{ell}": evaluate_sparse(rows[ell], bases) for ell in imposed
    }
    ev_residual = sub(add(mul(v, x5), scale(x5, 2)), x3)
    localizer_residual = sub(mul(inv, localizer_denominator), one)
    if any(value != [0] for value in row_residuals.values()):
        raise AssertionError(("row residuals", row_residuals))
    if ev_residual != [0] or localizer_residual != [0]:
        raise AssertionError((ev_residual, localizer_residual))

    wrong_bases = [zero, c, d2, d4, wrong_x1, x3, x5]
    wrong_residuals = {
        f"e{ell}": evaluate_sparse(rows[ell], wrong_bases) for ell in imposed
    }
    if not any(value != [0] for value in wrong_residuals.values()):
        raise AssertionError("old wrong x1 slice unexpectedly passed")

    source_jacobian = []
    for ell in imposed:
        source_row = [
            evaluate_sparse(Q.M.cpartial(rows[ell], column), bases)
            for column in range(1, 7)
        ]
        source_jacobian.append(source_row + [zero, zero])
    localizer_row = [
        zero,
        zero,
        zero,
        zero,
        mul(inv, x5),
        mul(inv, sub(x3, scale(x5, 4))),
        localizer_denominator,
        zero,
    ]
    v_definition_row = [
        zero,
        zero,
        zero,
        zero,
        scale(one, -1),
        add(v, [2]),
        zero,
        x5,
    ]
    full_jacobian = source_jacobian + [localizer_row, v_definition_row]
    full_determinant = determinant(full_jacobian)
    full_gcd = gcd_poly(full_determinant, Q8)
    full_norm = norm(full_determinant)
    if full_gcd != [1] or full_norm == 0:
        raise AssertionError(("full determinant", full_determinant, full_gcd, full_norm))

    derivative_q8 = [index * Q8[index] % P for index in range(1, len(Q8))]
    q8_squarefree = gcd_poly(Q8, derivative_q8) == [1]
    if not q8_squarefree:
        raise AssertionError("Q8bar not squarefree")
    units = [
        unit_record("v", v),
        unit_record("D=3v^2-2", D),
        unit_record("A2=3v^2+3v+1", A2),
        unit_record("normal_3x3_determinant", normal_det),
        unit_record("x5", x5),
        unit_record("x3-2x5", sub(x3, scale(x5, 2))),
        unit_record("localizer_denominator", localizer_denominator),
        unit_record("9v", scale(v, 9)),
    ]
    payload = {
        "case": "max12_912_order3_nu_q8_p127_full_contact_jacobian_aws_20260825",
        "status": "PASS",
        "prime": P,
        "compiler_sha256": COMPILER_SHA256,
        "source_chart": (
            "same approximate-cubic divided quotient: rows r1/t,r3/t,r5/t,r7/t,r2,r4; "
            "plus v*x5-x3+2*x5 and inv*x5*(x3-2*x5)-1"
        ),
        "q8_monic_low_to_high": Q8,
        "q8_squarefree": q8_squarefree,
        "correct_x1_factor": "3*v+1 over 9*v",
        "contact_coordinates_low_to_high": {
            "c": c,
            "d2": d2,
            "d4": d4,
            "x1": x1,
            "x3": x3,
            "x5": x5,
            "inv": inv,
            "v": v,
        },
        "row_residuals": row_residuals,
        "v_definition_residual": ev_residual,
        "localizer_residual": localizer_residual,
        "denominator_units": units,
        "old_wrong_x1_residuals": wrong_residuals,
        "full_relative_jacobian": {
            "rows": 8,
            "columns": ["c", "d2", "d4", "x1", "x3", "x5", "inv", "v"],
            "rank_at_every_geometric_q8_contact": 8,
            "determinant_low_to_high": full_determinant,
            "gcd_determinant_q8": full_gcd,
            "determinant_norm_mod_127": full_norm,
        },
        "scope": (
            "full divided localized source at the eight corrected mod-127 contacts; "
            "independent of plane H_v; no global graph membership, characteristic-zero "
            "no-merger, trajectory, max12, or JC2 conclusion"
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

