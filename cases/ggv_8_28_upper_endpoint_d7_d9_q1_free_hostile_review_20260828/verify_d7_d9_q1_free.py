#!/usr/bin/env python3
"""Independent exact review of the branch-P D7--D9 divisor repair.

This standard-library checker deliberately does not import the producer.
Fractional powers are reconstructed by the generalized binomial theorem,
whereas the producer uses a differential recurrence.  A second exact Q[X]
engine serializes non-q1 raw fixtures and checks the determinant rows.
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

SOURCES = {
    ROOT / "xmodel/ggv-upper-endpoint-q1-prefix-d7-d9-divisor-target-sol-ultra-20260828.md":
        "5b3bd56a1921bb0a4ed7ae9ed7c1eabcf5215533a0aae2a769cdcc81927b5401",
    ROOT / "cases/ggv_8_28_upper_endpoint_q1_prefix_d7_d8_target_20260828/verify_q1_prefix_target.py":
        "fceb189badafad877c1142b8925480516111790707954d2000421b8190fde119",
    ROOT / "cases/ggv_8_28_upper_endpoint_q1_prefix_d7_d8_target_20260828/RESULT.json":
        "ba900c6eacc7302491105bec49516d2e95dff982959a3904370b7e540216260b",
    ROOT / "cases/ggv_8_28_upper_endpoint_q1_prefix_d7_d8_target_20260828/TARGET.json":
        "c41f04a93f509adb1f430e808c69cd2171439c9e19fb001c6ea2bf0f29633a46",
    ROOT / "xmodel/ggv-8_28-upper-cascade-w3-w6-sol-ultra-20260827.md":
        "6e3d9104effe39c0dd0e34377bb7bdc6ede4f25f472f9f9c0098706aceffb60a",
    ROOT / "cases/ggv_8_28_upper_cascade_w3_w6_20260827/verify_upper_cascade.py":
        "ac3197988a3c0eba6b717194696b28f772550b789426087cbcfb3e6feee5ac37",
    ROOT / "cases/ggv_8_28_upper_cascade_w3_w6_20260827/RESULT.json":
        "54767fceaa1cc6b3feb64d9d07f7af1e2ffd43a725617123e6e6849091b23615",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


# Sparse Q[A,A^-1, symbols].  A is encoded by its separate integer exponent.
def term(coefficient=1, a_power=0, *symbols):
    coefficient = Q(coefficient)
    if not coefficient:
        return {}
    return {(int(a_power), tuple(sorted(symbols))): coefficient}


def add(*expressions):
    result = {}
    for expression in expressions:
        for key, value in expression.items():
            result[key] = result.get(key, Q(0)) + value
            if not result[key]:
                del result[key]
    return result


def scale(value, expression):
    value = Q(value)
    return {key: value * coefficient for key, coefficient in expression.items()
            if value * coefficient}


def mul(left, right):
    result = {}
    for (la, lv), lc in left.items():
        for (ra, rv), rc in right.items():
            key = (la + ra, tuple(sorted(lv + rv)))
            result[key] = result.get(key, Q(0)) + lc * rc
            if not result[key]:
                del result[key]
    return result


def product(*expressions):
    result = term()
    for expression in expressions:
        result = mul(result, expression)
    return result


def power(expression, exponent):
    result = term()
    for _ in range(exponent):
        result = mul(result, expression)
    return result


def ashift(exponent, expression):
    return {(a_power + exponent, symbols): coefficient
            for (a_power, symbols), coefficient in expression.items()}


def substitute(expression, substitutions):
    result = {}
    for (a_power, symbols), coefficient in expression.items():
        piece = term(coefficient, a_power)
        for symbol in symbols:
            piece = mul(piece, substitutions.get(symbol, term(1, 0, symbol)))
        result = add(result, piece)
    return result


def negative(expression):
    return {key: value for key, value in expression.items() if key[0] < 0}


def encode(expression):
    return [
        {"A_exponent": a_power, "coefficient": str(coefficient),
         "monomial": list(symbols)}
        for (a_power, symbols), coefficient in sorted(expression.items())
    ]


def vars_in(expression):
    return sorted({symbol for _, symbols in expression for symbol in symbols})


def minimum_a_power_with(expression, symbol):
    powers = [a_power for (a_power, symbols) in expression if symbol in symbols]
    return min(powers) if powers else None


def binomial(exponent, count):
    result = Q(1)
    for index in range(count):
        result *= (exponent - index) / (index + 1)
    return result


def series_mul(left, right, maximum):
    result = [{} for _ in range(maximum + 1)]
    for i, lvalue in enumerate(left):
        if not lvalue:
            continue
        for j, rvalue in enumerate(right):
            if i + j > maximum:
                break
            if rvalue:
                result[i + j] = add(result[i + j], mul(lvalue, rvalue))
    return result


def fractional_power_binomial(F, exponent, maximum):
    """Coefficient list for F^exponent from a direct binomial expansion."""
    normalized_tail = [{}] + [ashift(-4, F[index])
                              for index in range(1, maximum + 1)]
    accumulated = [{} for _ in range(maximum + 1)]
    tail_power = [{} for _ in range(maximum + 1)]
    tail_power[0] = term()
    for count in range(maximum + 1):
        coefficient = binomial(exponent, count)
        for weight in range(maximum + 1):
            accumulated[weight] = add(
                accumulated[weight], scale(coefficient, tail_power[weight]))
        tail_power = series_mul(tail_power, normalized_tail, maximum)
    base_power = 4 * exponent
    assert base_power.denominator == 1
    return [ashift(base_power.numerator, item) for item in accumulated]


MODES = {
    2: Q(5, 4), 4: Q(1), 6: Q(3, 4), 8: Q(1, 2),
    10: Q(1, 4), 12: Q(0), 14: Q(-1, 4), 16: Q(-1, 2),
    18: Q(-3, 4), 20: Q(-1),
}


def general_prefix(maximum=9):
    v, z, t = term(1, 0, "v"), term(1, 0, "z"), term(1, 0, "t")
    F = [term(1, 4)]
    F.append(ashift(2, v))
    F.append(scale(Q(1, 4), add(power(v, 2), ashift(2, z))))
    F.append(scale(Q(1, 8), add(mul(v, z), ashift(1, t))))
    for weight in range(4, maximum + 1):
        F.append(term(1, 0, f"f{weight}"))
    return F


def characteristic_rows(F, maximum):
    needed = {Q(3, 2)} | set(MODES.values())
    powers = {exponent: fractional_power_binomial(F, exponent, maximum)
              for exponent in needed}
    G = []
    for weight in range(maximum + 1):
        value = powers[Q(3, 2)][weight]
        for birth, exponent in MODES.items():
            if birth <= weight:
                value = add(value, mul(term(1, 0, f"c{birth}"),
                                       powers[exponent][weight - birth]))
        G.append(value)
    return G


def symbolic_review():
    F = general_prefix(9)
    G = characteristic_rows(F, 9)
    v, z, t = term(1, 0, "v"), term(1, 0, "z"), term(1, 0, "t")
    f4, f5, f6 = (term(1, 0, name) for name in ("f4", "f5", "f6"))
    c2, c6 = term(1, 0, "c2"), term(1, 0, "c6")
    k = add(scale(64, f4), scale(-1, power(z, 2)))

    # c2=0, D7.
    d7_zero = negative(substitute(G[7], {"c2": {}}))
    expected_d7_zero = scale(Q(3, 2048), ashift(
        -2, mul(t, add(ashift(1, k), scale(-2, mul(t, v))))))
    assert d7_zero == expected_d7_zero

    # c2=0, D8, with c6 retained.
    delta = add(ashift(1, k), scale(-4, mul(t, v)))
    n8 = add(
        power(delta, 2),
        scale(-8, ashift(2, product(power(t, 2), z))),
        scale(1024, ashift(3, add(mul(c6, power(v, 2)), mul(f5, t)))),
    )
    expected_d8_zero = scale(Q(3, 32768), ashift(-4, n8))
    d8_zero = negative(substitute(G[8], {"c2": {}}))
    assert d8_zero == expected_d8_zero

    # Active A|V branch: keep every born mode.
    s = term(1, 0, "s")
    active = {"v": ashift(1, s)}
    j = add(k, scale(-2, mul(t, s)))
    expected_d7_active = scale(Q(3, 2048), ashift(-1, mul(t, j)))
    d7_active = negative(substitute(G[7], active))
    assert d7_active == expected_d7_active

    h = add(power(s, 2), scale(-2, z))
    e8_active = add(power(add(k, scale(-4, mul(t, s))), 2),
                    scale(-8, product(power(t, 2), z)))
    p8_active = add(scale(-1, power(h, 3)),
                    scale(-8, mul(h, j)), scale(32, power(t, 2)))
    expected_d8_active = add(
        scale(Q(3, 32768), ashift(-2, e8_active)),
        scale(Q(5, 65536), ashift(-1, mul(c2, p8_active))),
        scale(Q(3, 32), ashift(-1, mul(f5, t))),
    )
    d8_active = negative(substitute(G[8], active))
    assert d8_active == expected_d8_active
    full_d7_active = substitute(G[7], active)
    full_d8_active = substitute(G[8], active)
    assert minimum_a_power_with(full_d7_active, "c2") == 0
    assert minimum_a_power_with(full_d8_active, "c2") == -1
    assert minimum_a_power_with(full_d8_active, "c6") == 1

    # c2=c6=0, D9.  This is reconstructed from the binomial engine.
    n9 = add(
        scale(-48, product(power(t, 2), power(v, 3))),
        scale(1536, ashift(1, product(f4, t, power(v, 2)))),
        scale(-24, ashift(1, product(t, power(v, 2), power(z, 2)))),
        scale(-12288, ashift(2, mul(power(f4, 2), v))),
        scale(384, ashift(2, product(f4, v, power(z, 2)))),
        scale(48, ashift(2, product(power(t, 2), v, z))),
        scale(-3, ashift(2, mul(v, power(z, 4)))),
        scale(-768, ashift(3, product(f4, t, z))),
        scale(-8, ashift(3, power(t, 3))),
        scale(12, ashift(3, mul(t, power(z, 3)))),
        scale(768, ashift(3, mul(f5, add(ashift(1, k),
                                               scale(-4, mul(t, v)))))),
        scale(6144, ashift(5, mul(f6, t))),
    )
    expected_d9_zero = scale(Q(1, 65536), ashift(-6, n9))
    d9_zero = negative(substitute(G[9], {"c2": {}, "c6": {}}))
    assert d9_zero == expected_d9_zero

    # Complete active leading A^-3 class.  No c2/c6/regular mode reaches it.
    active_d9 = negative(substitute(G[9], active))
    full_active_d9 = substitute(G[9], active)
    assert minimum_a_power_with(full_active_d9, "c2") == -2
    assert minimum_a_power_with(full_active_d9, "c6") == 0
    assert minimum_a_power_with(full_active_d9, "f5") == -2
    assert minimum_a_power_with(full_active_d9, "f6") == -1
    assert minimum_a_power_with(full_active_d9, "f9") == 2
    active_leading = ashift(3, {key: value for key, value in active_d9.items()
                                if key[0] == -3})
    Ksym = term(1, 0, "k")
    active_leading_k = substitute(active_leading, {
        "f4": scale(Q(1, 64), add(Ksym, power(z, 2)))})
    expected_active_k = scale(Q(1, 65536), add(
        scale(-3, mul(s, power(Ksym, 2))),
        scale(12, product(t, Ksym, add(scale(2, power(s, 2)), scale(-1, z)))),
        scale(-48, product(s, power(t, 2), add(power(s, 2), scale(-1, z)))),
        scale(-8, power(t, 3)),
    ))
    assert active_leading_k == expected_active_k
    assert not ({"c2", "c4", "c6", "c8", "f5", "f6", "f7", "f8", "f9"}
                & set(vars_in(active_leading_k)))

    # Divisor factorization A=C*B, V=C*V1, T=B*U.
    C, B, u, v1 = (term(1, 0, name) for name in ("C", "B", "u", "v1"))

    def replace_a_by_cb(expression):
        result = {}
        for (a_power, symbols), coefficient in expression.items():
            assert a_power >= 0
            result = add(result, product(
                term(coefficient), power(C, a_power), power(B, a_power),
                term(1, 0, *symbols)))
        return result

    n9_cb = substitute(replace_a_by_cb(n9), {
        "v": mul(C, v1), "t": mul(B, u),
        "f4": scale(Q(1, 64), add(term(1, 0, "k"), power(z, 2))),
    })
    kk = Ksym
    d = add(kk, scale(-4, mul(u, v1)))
    p9 = add(
        scale(-3, mul(v1, power(d, 2))),
        scale(-12, product(power(B, 2), u, z, d)),
        scale(-8, product(power(B, 4), power(u, 3))),
        scale(768, product(C, power(B, 2), f5, d)),
        scale(6144, product(power(C, 2), power(B, 4), f6, u)),
    )
    assert n9_cb == product(power(C, 3), power(B, 2), p9)

    # Root-field reductions, including V1=0.
    p9_c_d7 = substitute(p9, {
        "C": {}, "k": scale(2, mul(u, v1))})
    h8 = add(scale(2, product(power(B, 2), z)), scale(-1, power(v1, 2)))
    expected_c_d7 = add(scale(12, product(power(u, 2), v1, h8)),
                        scale(-8, product(power(B, 4), power(u, 3))))
    assert p9_c_d7 == expected_c_d7

    jj = term(1, 0, "j")
    active_j = substitute(expected_active_k, {
        "k": add(jj, scale(2, mul(t, s)))})
    expected_active_j = scale(Q(1, 65536), add(
        scale(-3, mul(s, power(jj, 2))),
        scale(12, product(t, jj, add(power(s, 2), scale(-1, z)))),
        scale(-12, product(s, power(t, 2), h)),
        scale(-8, power(t, 3)),
    ))
    assert active_j == expected_active_j
    active_after_d7 = substitute(active_j, {"j": {}})
    assert active_after_d7 == scale(Q(1, 65536), add(
        scale(-12, product(s, power(t, 2), h)), scale(-8, power(t, 3))))

    # q1-free post-repair square defect on c2=0.
    u0, w = term(1, 0, "u0"), term(1, 0, "w")
    f4_lift = add(scale(Q(1, 16), mul(v, u0)),
                  scale(Q(1, 64), power(z, 2)), ashift(1, w))
    post = negative(substitute(G[9], {
        "c2": {}, "c6": {}, "t": ashift(1, u0), "f4": f4_lift}))
    expected_post = scale(Q(3, 256), ashift(-2, mul(w, add(
        scale(-16, mul(v, w)),
        ashift(1, add(scale(64, f5), scale(-1, mul(u0, z))))))))
    assert post == expected_post
    # When A|V, c6 is allowed but is regular, so the same c2=0 polar block holds.
    active_f4_lift = substitute(f4_lift, {"v": ashift(1, s)})
    post_active = negative(substitute(G[9], {
        "c2": {}, "t": ashift(1, u0), "f4": active_f4_lift,
        "v": ashift(1, s)}))
    assert post_active == substitute(expected_post, {"v": ashift(1, s)})

    return {
        "method": "direct generalized-binomial expansion, not producer recurrence",
        "all_modes": {str(birth): str(exponent)
                      for birth, exponent in MODES.items()},
        "D7_c2_zero_polar": encode(d7_zero),
        "D8_c2_zero_polar_sha256": hashlib.sha256(
            json.dumps(encode(d8_zero), sort_keys=True,
                       separators=(",", ":")).encode()).hexdigest(),
        "D9_c2_c6_zero_polar_sha256": hashlib.sha256(
            json.dumps(encode(d9_zero), sort_keys=True,
                       separators=(",", ":")).encode()).hexdigest(),
        "D7_active_polar": encode(d7_active),
        "D8_active_polar_sha256": hashlib.sha256(
            json.dumps(encode(d8_active), sort_keys=True,
                       separators=(",", ":")).encode()).hexdigest(),
        "D9_active_A_minus_3": encode(active_leading_k),
        "proper_factorization": (
            "N9=C^3*B^2*(-3*V1*D^2-12*B^2*U*Z*D-8*B^4*U^3"
            "+768*C*B^2*F5*D+6144*C^2*B^4*F6*U), D=K-4*U*V1"),
        "proper_root_division_free_reduction": (
            "after D7: P9=12*U^2*V1*(2*B^2*Z-V1^2)-8*B^4*U^3; "
            "D8 kills the parenthesis, including when V1=0"),
        "active_root_reduction": (
            "after D7 J=0: (-12*S*T^2*(S^2-2Z)-8*T^3)/65536; "
            "D8 kills S^2-2Z"),
        "post_repair_c2_zero": encode(expected_post),
        "regular_mode_firewall": {
            "D9_active_leading_variables": vars_in(active_leading_k),
            "active_minimum_A_powers": {
                "D7_c2": 0, "D8_c2": -1, "D8_c6": 1,
                "D9_c2": -2, "D9_c6": 0, "D9_F5": -2,
                "D9_F6": -1, "D9_same_row_F9": 2,
            },
            "same_row_F9_absent_from_all_D7_D9_polar_targets": True,
            "c4_c8_absent_from_all_D7_D9_polar_targets": True,
            "c6_regular_on_A_divides_V0": True,
        },
    }


# Independent exact Q[X] engine for literal raw fixtures.
def ptrim(poly):
    poly = list(poly)
    while poly and not poly[-1]:
        poly.pop()
    return poly


def padd(*polys):
    result = []
    for poly in polys:
        size = max(len(result), len(poly))
        result = ptrim([
            (result[i] if i < len(result) else Q(0))
            + (poly[i] if i < len(poly) else Q(0)) for i in range(size)])
    return result


def pscale(value, poly):
    return ptrim([Q(value) * coefficient for coefficient in poly])


def pmul(left, right):
    if not left or not right:
        return []
    result = [Q(0)] * (len(left) + len(right) - 1)
    for i, lv in enumerate(left):
        for j, rv in enumerate(right):
            result[i + j] += lv * rv
    return ptrim(result)


def ppow(poly, exponent):
    result = [Q(1)]
    for _ in range(exponent):
        result = pmul(result, poly)
    return result


def pder(poly):
    return ptrim([Q(i) * poly[i] for i in range(1, len(poly))])


def pdivmod(dividend, divisor):
    dividend, divisor = ptrim(dividend), ptrim(divisor)
    assert divisor
    quotient = [Q(0)] * max(0, len(dividend) - len(divisor) + 1)
    remainder = dividend
    while remainder and len(remainder) >= len(divisor):
        degree = len(remainder) - len(divisor)
        factor = remainder[-1] / divisor[-1]
        quotient[degree] += factor
        remainder = padd(remainder, pscale(-factor, [Q(0)] * degree + divisor))
    return ptrim(quotient), ptrim(remainder)


def pgcd(left, right):
    left, right = ptrim(left), ptrim(right)
    while right:
        _, remainder = pdivmod(left, right)
        left, right = right, remainder
    return pscale(1 / left[-1], left) if left else []


def pencode(poly):
    return [str(value) for value in ptrim(poly)]


def evaluate_fraction(expression, A, assignments):
    surviving = []
    for key, coefficient in expression.items():
        _, symbols = key
        if all(assignments[symbol] for symbol in symbols):
            surviving.append((key, coefficient))
    if not surviving:
        return [], [Q(1)]
    minimum = min(key[0] for key, _ in surviving)
    denominator_power = max(0, -minimum)
    numerator = []
    for (a_power, symbols), coefficient in surviving:
        piece = pscale(coefficient, ppow(A, a_power + denominator_power))
        for symbol in symbols:
            piece = pmul(piece, assignments[symbol])
        numerator = padd(numerator, piece)
    denominator = ppow(A, denominator_power)
    common = pgcd(numerator, denominator)
    numerator, remainder = pdivmod(numerator, common)
    assert not remainder
    denominator, remainder = pdivmod(denominator, common)
    assert not remainder
    return numerator, denominator


def evaluate_polynomial(expression, A, assignments):
    numerator, denominator = evaluate_fraction(expression, A, assignments)
    assert denominator == [Q(1)]
    return numerator


def determinant(F, G, maximum):
    rows = []
    for weight in range(maximum + 1):
        row = []
        for i in range(weight + 1):
            j = weight - i
            row = padd(row,
                       pscale(12 - j, pmul(pder(F[i]), G[j])),
                       pscale(i - 8, pmul(F[i], pder(G[j]))))
        rows.append(row)
    return rows


def matrix_rank(rows):
    matrix = [[Q(value) for value in row] for row in rows]
    if not matrix:
        return 0
    nrows, ncols = len(matrix), len(matrix[0])
    rank = 0
    for column in range(ncols):
        pivot = next((row for row in range(rank, nrows)
                      if matrix[row][column]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        value = matrix[rank][column]
        matrix[rank] = [entry / value for entry in matrix[rank]]
        for row in range(nrows):
            if row != rank and matrix[row][column]:
                value = matrix[row][column]
                matrix[row] = [matrix[row][j] - value * matrix[rank][j]
                               for j in range(ncols)]
        rank += 1
        if rank == nrows:
            break
    return rank


def q1_membership(A, V):
    columns = []
    for degree in range(5):
        R = [Q(0)] * degree + [Q(1)]
        columns.append(padd(pmul(pder(A), R), pscale(2, pmul(A, pder(R)))))
    rows = []
    for degree in range(8):
        rows.append([(column[degree] if degree < len(column) else Q(0))
                     for column in columns])
    rank = matrix_rank(rows)
    augmented = [row + [(V[degree] if degree < len(V) else Q(0))]
                 for degree, row in enumerate(rows)]
    return rank, matrix_rank(augmented), rank == matrix_rank(augmented)


def raw_fixture(label, A, assignments, Gexpr, expect_q1):
    Fexpr = general_prefix(9)
    F = [evaluate_polynomial(Fexpr[n], A, assignments) for n in range(10)]
    G = [evaluate_polynomial(Gexpr[n], A, assignments) for n in range(9)]
    rows = determinant(F[:9], G, 8)
    assert rows == [[] for _ in range(9)]
    for n in range(1, 9):
        assert len(F[n]) - 1 <= 16 - n
        assert len(G[n]) - 1 <= 24 - n
    g9_num, g9_den = evaluate_fraction(Gexpr[9], A, assignments)
    assert g9_num and g9_den != [Q(1)]
    q1_rank, q1_augmented_rank, in_q1 = q1_membership(A, assignments["v"])
    assert in_q1 == expect_q1
    return {
        "label": label,
        "A": pencode(A), "V0": pencode(assignments["v"]),
        "T": pencode(assignments["t"]), "Z": pencode(assignments["z"]),
        "F4": pencode(assignments["f4"]), "F5": pencode(assignments["f5"]),
        "modes": {name: pencode(assignments[name])
                  for name in sorted(assignments) if name.startswith("c")},
        "D0_through_D8_zero": True,
        "raw_F_degrees_1_through_8": [len(F[n]) - 1 for n in range(1, 9)],
        "raw_G_degrees_1_through_8": [len(G[n]) - 1 for n in range(1, 9)],
        "D9_characteristic_reduced_numerator": pencode(g9_num),
        "D9_characteristic_reduced_denominator": pencode(g9_den),
        "q1_rank": q1_rank, "q1_augmented_rank": q1_augmented_rank,
        "q1_member": in_q1,
    }


def fixture_review(Gexpr):
    A = [Q(-1), Q(0), Q(0), Q(0), Q(1)]
    C = [Q(-1), Q(1)]
    B, remainder = pdivmod(A, C)
    assert not remainder
    zero_modes = {f"c{birth}": [] for birth in MODES}
    zero_high = {f"f{weight}": [] for weight in range(5, 10)}

    # Proper C, with V1=1 (a unit everywhere).
    v1 = [Q(1)]
    V = pmul(C, v1)
    T = B
    Z = [Q(1, 32)]
    K = padd([Q(4)], pscale(Q(-1, 2), B))
    F4 = pscale(Q(1, 64), padd(K, pmul(Z, Z)))
    proper_unit = raw_fixture("proper_C_non_q1_V1_unit", A, {
        "v": V, "z": Z, "t": T, "f4": F4, **zero_high, **zero_modes,
    }, Gexpr, False)
    proper_unit.update({"C": pencode(C), "B": pencode(B), "V1": pencode(v1)})

    # Proper C, but V1 vanishes at the C-root.  No division by V1 is legal.
    v1_zero_at_c = C
    V = pmul(C, v1_zero_at_c)
    Z = pscale(Q(1, 8), pmul(C, C))
    K = pmul(C, padd([Q(4)], B))
    F4 = pscale(Q(1, 64), padd(K, pmul(Z, Z)))
    proper_vanish = raw_fixture("proper_C_non_q1_V1_vanishes_at_C_root", A, {
        "v": V, "z": Z, "t": T, "f4": F4, **zero_high, **zero_modes,
    }, Gexpr, False)
    proper_vanish.update({"C": pencode(C), "B": pencode(B),
                          "V1": pencode(v1_zero_at_c)})

    # Active C=A fixtures.  c2 and c6 are deliberately nonzero, and F5
    # cancels the full A^-1 D8 mode after the A^-2 condition is imposed.
    active = []
    for scalar_s, expect_q1, label in (
            (Q(0), True, "active_C_A_V1_zero_q1"),
            (Q(1), False, "active_C_A_non_q1")):
        S = [scalar_s] if scalar_s else []
        V = pscale(scalar_s, A)
        T_active = [Q(1)]
        Z_active = [scalar_s * scalar_s / 2]
        K_active = [2 * scalar_s]
        F4_active = pscale(Q(1, 64), padd(K_active, pmul(Z_active, Z_active)))
        assignments = {
            "v": V, "z": Z_active, "t": T_active, "f4": F4_active,
            "f5": [Q(-5, 192)], "f6": [], "f7": [], "f8": [], "f9": [],
            "c2": [Q(1)], "c4": [Q(2)], "c6": [Q(3)], "c8": [Q(5)],
            **{f"c{birth}": [] for birth in MODES if birth > 8},
        }
        item = raw_fixture(label, A, assignments, Gexpr, expect_q1)
        item.update({"C": pencode(A), "B": ["1"], "V1": pencode(S),
                     "c2_and_c6_both_nonzero": True})
        active.append(item)

    # C=1 endpoint: V0 is a unit modulo A and a non-A-multiple T fails at D7.
    c1_assignments = {
        "v": [Q(1)], "z": [], "t": [Q(1)], "f4": [], **zero_high,
        **zero_modes,
    }
    c1_num, c1_den = evaluate_fraction(Gexpr[7], A, c1_assignments)
    assert c1_num and c1_den != [Q(1)]

    return {
        "proper_C_fixtures": [proper_unit, proper_vanish],
        "active_C_A_fixtures": active,
        "C_equals_1_D7_negative_control": {
            "A": pencode(A), "V0": ["1"], "T": ["1"],
            "g7_reduced_numerator": pencode(c1_num),
            "g7_reduced_denominator": pencode(c1_den),
            "meaning": "with gcd(A,V0)=1, a T not divisible by A already fails D7",
        },
    }


def target_payload():
    return {
        "format": "GGV_BRANCH_P_D7_D9_Q1_FREE_HOSTILE_REVIEW_V1",
        "field": "arbitrary characteristic-zero field; conclusions are field-valued/radical in parameter space",
        "hypotheses": {
            "A": "monic squarefree quartic in K[X]",
            "raw_prefix": [
                "F0=A^4", "F1=A^2*V0", "F2=(V0^2+A^2*Z)/4",
                "F3=(V0*Z+A*T)/8",
                "deg(F_n)<=16-n and deg(G_n)<=24-n",
            ],
            "branch_cover": "c2=0 or A divides V0",
            "rows": "D1=...=D9=0, equivalently polynomial characteristic coefficients through weight 9",
            "not_required": ["q1", "R0", "D23", "a translation gauge"],
        },
        "conclusion": "A divides T",
        "proper_divisor_proof": [
            "C=gcd(A,V0), A=C*B, V0=C*V1; D7 first gives B|T, write T=B*U",
            "D7 iff C|U*(K-2*U*V1)",
            "D8 iff A^2 divides (K-4*U*V1)^2-8*B^2*U^2*Z+1024*A*(c6*C^2*V1^2+F5*B*U)",
            "if B is nonconstant D8 forces c6=0",
            "at every C-factor where U is nonzero, D7/D8 reduce P9 to -8*B^4*U^3, contradicting D9",
        ],
        "active_proof": [
            "write V0=A*S and J=K-2*T*S; retain c2 and c6",
            "if T is nonzero at an A-factor, D7 gives J=0 and leading D8 gives S^2=2*Z",
            "the complete A^-3 D9 class then equals -8*T^3/65536; c2,c6 and raw same-row terms cannot cancel it",
        ],
        "post_repair": {
            "c2_zero": "with T=A*U0 and Delta4=A*W, A^2 divides W*(-16*V0*W+A*(64*F5-U0*Z))",
            "root_split": "for C=gcd(A,V0), B=A/C divides W at field points; C need not yet divide W",
            "q1_free": True,
        },
        "scheme_firewall": "The root/residue-field proof uses reduced irreducible factors and nonzero elements as units. It proves radical/field-point divisibility, not ideal membership over nilpotent parameter rings.",
        "translation_gauge": "No translation is needed for D9 repair. The active post-D9 branch remains distinct; the failed raw-window-preservation gauge is not rehabilitated.",
    }


def calculate():
    for path, expected in SOURCES.items():
        assert digest(path) == expected, path
    symbolic = symbolic_review()
    Gexpr = characteristic_rows(general_prefix(9), 9)
    fixtures = fixture_review(Gexpr)
    target = target_payload()
    return {
        "status": "REPAIR_EXACT_Q1_NOT_REQUIRED",
        "verdict": "REPAIR",
        "source_hashes": {str(path.relative_to(ROOT)): expected
                          for path, expected in SOURCES.items()},
        "independence": "No producer code imported; modes use direct binomial expansion; fixtures use a separate Q[X] engine.",
        "symbolic_reconstruction": symbolic,
        "literal_raw_fixtures": fixtures,
        "adjudication": {
            "producer_q1_scoped_theorem": "true",
            "stronger_theorem": "the same D1..D9 => A|T implication is q1-free",
            "actual_wrong_math_from_q1_label": False,
            "required_scope_repair": "drop q1/R0/D23 from the D7-D9 theorem and from the post-D9 c2=0 W split; retain q1 only as an optional later restriction",
        },
        "target_sha256": hashlib.sha256(
            (json.dumps(target, sort_keys=True, indent=2) + "\n").encode()).hexdigest(),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = calculate()
    target = target_payload()
    result_text = json.dumps(result, sort_keys=True, indent=2) + "\n"
    target_text = json.dumps(target, sort_keys=True, indent=2) + "\n"
    if args.check:
        assert RESULT.read_text() == result_text
        assert TARGET.read_text() == target_text
    else:
        RESULT.write_text(result_text)
        TARGET.write_text(target_text)
    print(result["status"])


if __name__ == "__main__":
    main()
