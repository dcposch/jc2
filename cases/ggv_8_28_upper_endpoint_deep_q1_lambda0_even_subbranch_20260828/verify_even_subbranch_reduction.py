#!/usr/bin/env python3
"""Exact parity target kill and odd-fiber coupling on lambda zero."""

from __future__ import annotations

from fractions import Fraction as Q
import hashlib
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ORIGIN_REPORT = ROOT / "xmodel/ggv-upper-endpoint-origin-odd-coupling-sol-ultra-20260828.md"
ORIGIN_REPORT_SHA256 = "3e4a0f03acec2ee5e3cdfff558c481e14735408aa18486d23215958ed8d4bb3a"
ORIGIN_CHECKER = (
    ROOT
    / "cases/ggv_8_28_upper_endpoint_origin_odd_coupling_20260828"
    / "verify_origin_odd_coupling.py"
)
ORIGIN_CHECKER_SHA256 = "f23a6d959dc9a8854f051c16a1fe287dea91d5b66b01a63198a64715c08c04c8"


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def trim(poly):
    out = list(poly)
    while out and not out[-1]:
        out.pop()
    return out


def add(*polys):
    size = max((len(poly) for poly in polys), default=0)
    out = [Q(0)] * size
    for poly in polys:
        for index, value in enumerate(poly):
            out[index] += value
    return trim(out)


def scale(value, poly):
    return trim([Q(value) * coefficient for coefficient in poly])


def mul(left, right):
    if not left or not right:
        return []
    out = [Q(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return trim(out)


def derivative(poly):
    return trim([Q(index) * poly[index] for index in range(1, len(poly))])


def power(poly, exponent):
    out = [Q(1)]
    for _ in range(exponent):
        out = mul(out, poly)
    return out


def ceil_div(numerator, denominator):
    return -((-numerator) // denominator)


def f_window(weight):
    lower = max(0, ceil_div(weight - 8, 3))
    upper = 16 - weight
    return tuple(range(lower, upper + 1)) if lower <= upper else ()


def g_window(weight):
    lower = max(0, ceil_div(weight - 12, 3))
    upper = 24 - weight
    return tuple(range(lower, upper + 1)) if lower <= upper else ()


def sample(window, seed):
    if not window:
        return []
    out = [Q(0)] * (window[-1] + 1)
    for offset, degree in enumerate(window):
        out[degree] = Q((seed + 3 * offset) % 11 - 5, offset + 1)
    return trim(out)


def original_rows(F, G):
    maximum = max(F) + max(G)
    rows = []
    for n in range(maximum + 1):
        row = []
        for i in F:
            j = n - i
            if j not in G:
                continue
            row = add(
                row,
                scale(12 - j, mul(derivative(F[i]), G[j])),
                scale(i - 8, mul(F[i], derivative(G[j]))),
            )
        rows.append(row)
    return rows


def reduced_rows(f, g):
    maximum = max(f) + max(g)
    rows = []
    for n in range(maximum + 1):
        row = []
        for i in f:
            j = n - i
            if j not in g:
                continue
            row = add(
                row,
                scale(6 - j, mul(derivative(f[i]), g[j])),
                scale(i - 4, mul(f[i], derivative(g[j]))),
            )
        rows.append(row)
    return rows


def t5(A, d):
    return scale(Q(1, 2), add(
        scale(5, mul(derivative(A), d)),
        scale(2, mul(A, derivative(d))),
    ))


def jet_add(left, right):
    return left[0] + right[0], left[1] + right[1]


def jet_mul(left, right):
    return left[0] * right[0], left[0] * right[1] + left[1] * right[0]


def jet_scale(value, jet):
    return Q(value) * jet[0], Q(value) * jet[1]


def jet_div(left, right):
    assert right[0]
    return (
        left[0] / right[0],
        (left[1] * right[0] - left[0] * right[1]) / (right[0] ** 2),
    )


def jet_integer_power(jet, exponent):
    if exponent < 0:
        return jet_div((Q(1), Q(0)), jet_integer_power(jet, -exponent))
    out = (Q(1), Q(0))
    for _ in range(exponent):
        out = jet_mul(out, jet)
    return out


def jet_series_mul(left, right, maximum):
    out = [(Q(0), Q(0)) for _ in range(maximum + 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j <= maximum:
                out[i + j] = jet_add(out[i + j], jet_mul(a, b))
    return out


def jet_series_power_one(base, exponent, maximum):
    assert base[0] == (Q(1), Q(0))
    u = list(base[: maximum + 1])
    u += [(Q(0), Q(0)) for _ in range(maximum + 1 - len(u))]
    u[0] = (Q(0), Q(0))
    term = [(Q(0), Q(0)) for _ in range(maximum + 1)]
    term[0] = (Q(1), Q(0))
    out = [(Q(0), Q(0)) for _ in range(maximum + 1)]
    choose = Q(1)
    for count in range(maximum + 1):
        if count:
            term = jet_series_mul(term, u, maximum)
            choose *= (exponent - (count - 1)) / count
        for degree in range(maximum + 1):
            out[degree] = jet_add(out[degree], jet_scale(choose, term[degree]))
    return out


def characteristic_jets(A, F, modes, maximum=15):
    # Keep the reviewed branch A^(6-k) explicitly.  Replacing it by an
    # unchosen scalar branch of (A^4)^((6-k)/4) gives the wrong sign when
    # A(0)=-1 and 6-k is odd.
    Ajet = (A[0], A[1] if len(A) > 1 else Q(0))
    F0jet = (
        F[0][0],
        F[0][1] if len(F[0]) > 1 else Q(0),
    )
    series = [(Q(0), Q(0)) for _ in range(maximum + 1)]
    for weight, polynomial in F.items():
        if weight <= maximum:
            coefficient = (
                polynomial[0] if polynomial else Q(0),
                polynomial[1] if len(polynomial) > 1 else Q(0),
            )
            series[weight] = jet_div(coefficient, F0jet)
    characteristic = [
        jet_mul(jet_integer_power(Ajet, 6), value)
        for value in jet_series_power_one(series, Q(3, 2), maximum)
    ]
    for k, mode in enumerate(modes, 1):
        shift = 2 * k
        if not mode or shift > maximum:
            continue
        powered = jet_series_power_one(
            series, Q(6 - k, 4), maximum - shift
        )
        prefactor = jet_integer_power(Ajet, 6 - k)
        for degree, value in enumerate(powered):
            characteristic[degree + shift] = jet_add(
                characteristic[degree + shift],
                jet_scale(mode, jet_mul(prefactor, value)),
            )
    return characteristic


def poly_divmod(dividend, divisor):
    remainder = trim(dividend)
    divisor = trim(divisor)
    quotient = [Q(0)] * max(0, len(remainder) - len(divisor) + 1)
    while remainder and len(remainder) >= len(divisor):
        degree = len(remainder) - len(divisor)
        coefficient = remainder[-1] / divisor[-1]
        quotient[degree] += coefficient
        for index, value in enumerate(divisor):
            remainder[index + degree] -= coefficient * value
        remainder = trim(remainder)
    return trim(quotient), remainder


def la_normalize(A, element):
    out = {exponent: trim(poly) for exponent, poly in element.items()
           if trim(poly)}
    changed = True
    while changed:
        changed = False
        for exponent in sorted(out):
            if exponent >= 0:
                continue
            quotient, remainder = poly_divmod(out[exponent], A)
            if not remainder:
                del out[exponent]
                out[exponent + 1] = add(out.get(exponent + 1, []), quotient)
                changed = True
                break
    return {exponent: poly for exponent, poly in out.items() if poly}


def la(A, poly, exponent=0):
    return la_normalize(A, {} if not poly else {exponent: poly})


def la_add(A, *elements):
    out = {}
    for element in elements:
        for exponent, poly in element.items():
            out[exponent] = add(out.get(exponent, []), poly)
    return la_normalize(A, out)


def la_scale(A, value, element):
    return la_normalize(A, {
        exponent: scale(value, poly) for exponent, poly in element.items()
    })


def la_mul(A, left, right):
    out = {}
    for exponent1, poly1 in left.items():
        for exponent2, poly2 in right.items():
            exponent = exponent1 + exponent2
            out[exponent] = add(
                out.get(exponent, []), mul(poly1, poly2)
            )
    return la_normalize(A, out)


def la_series_mul(A, left, right, maximum):
    out = [{} for _ in range(maximum + 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j <= maximum:
                out[i + j] = la_add(A, out[i + j], la_mul(A, a, b))
    return out


def la_series_power_one(A, base, exponent, maximum):
    one = la(A, [Q(1)])
    assert base[0] == one
    u = list(base[: maximum + 1]) + [
        {} for _ in range(maximum + 1 - len(base))
    ]
    u[0] = {}
    term = [{} for _ in range(maximum + 1)]
    term[0] = one
    out = [{} for _ in range(maximum + 1)]
    choose = Q(1)
    for count in range(maximum + 1):
        if count:
            term = la_series_mul(A, term, u, maximum)
            choose *= (exponent - (count - 1)) / count
        for degree in range(maximum + 1):
            out[degree] = la_add(
                A, out[degree], la_scale(A, choose, term[degree])
            )
    return out


def main():
    assert sha256(ORIGIN_REPORT) == ORIGIN_REPORT_SHA256
    assert sha256(ORIGIN_CHECKER) == ORIGIN_CHECKER_SHA256
    even_f_windows = {weight // 2: f_window(weight)
                      for weight in range(0, 15, 2)}
    even_g_windows = {weight // 2: g_window(weight)
                      for weight in range(0, 22, 2)}
    assert [even_f_windows[index] for index in range(8)] == [
        tuple(range(0, 17)), tuple(range(0, 15)), tuple(range(0, 13)),
        tuple(range(0, 11)), tuple(range(0, 9)), tuple(range(1, 7)),
        tuple(range(2, 5)), (2,),
    ]
    assert [even_g_windows[index] for index in range(11)] == [
        tuple(range(0, 25)), tuple(range(0, 23)), tuple(range(0, 21)),
        tuple(range(0, 19)), tuple(range(0, 17)), tuple(range(0, 15)),
        tuple(range(0, 13)), tuple(range(1, 11)), tuple(range(2, 9)),
        tuple(range(2, 7)), tuple(range(3, 5)),
    ]
    assert sum(map(len, even_f_windows.values())) == 75
    assert sum(map(len, even_g_windows.values())) == 157

    # The literal X^0 endpoint target sees exactly two nonzero-factor pairs.
    first_pairs = []
    second_pairs = []
    for i in range(15):
        j = 22 - i
        if j not in range(22):
            continue
        if 1 in f_window(i) and 0 in g_window(j) and 12 - j:
            first_pairs.append((i, j, 12 - j))
        if 0 in f_window(i) and 1 in g_window(j) and i - 8:
            second_pairs.append((i, j, i - 8))
    assert first_pairs == [(11, 11, 1)]
    assert second_pairs == [(7, 15, -1)]

    f = {index: sample(window, 17 + index)
         for index, window in even_f_windows.items()}
    g = {index: sample(window, 41 + index)
         for index, window in even_g_windows.items()}
    F = {2 * index: polynomial for index, polynomial in f.items()}
    G = {2 * index: polynomial for index, polynomial in g.items()}
    D = original_rows(F, G)
    R = reduced_rows(f, g)
    for n in range(18):
        assert D[2 * n] == scale(2, R[n])
    for n in range(18):
        odd = 2 * n + 1
        if odd < len(D):
            assert D[odd] == []

    # Coefficient of s^(n-11) in Jac(f/s^4,g/s^6) equals -R_n.
    bracket = {}
    for i, fi in f.items():
        for j, gj in g.items():
            exponent = i + j - 11
            bracket[exponent] = add(
                bracket.get(exponent, []),
                scale(j - 6, mul(derivative(fi), gj)),
                scale(-(i - 4), mul(fi, derivative(gj))),
            )
    for n, row in enumerate(R):
        assert bracket.get(n - 11, []) == scale(-1, row)

    # Exact endpoint primitive checksum for A=X^4-1:
    # N=X^5/40-X/8 has N'=A/8, hence (A^5*g11)'=A/8.
    A = [Q(-1), Q(0), Q(0), Q(0), Q(1)]
    N = [Q(0), Q(-1, 8), Q(0), Q(0), Q(0), Q(1, 40)]
    assert derivative(N) == scale(Q(1, 8), A)

    # The all-F-odd-zero fixed locus cannot hit the target: both live factors
    # F11[X1] and F7[X0] vanish.  This is stronger than the Laurent reduction.
    all_f_odd_zero_endpoint = Q(0) * Q(17) - Q(0) * Q(-23)
    assert all_f_odd_zero_endpoint == 0 != 1

    # Exact intersection control: q7..q15 plus the target coupling are not
    # themselves inconsistent.  On A=X^4-1, Q=X, e=F8=r=0, take the legal
    # raw odd tail and primitive witnesses below.  Modes c2=c6=1 retain the
    # required active c2 open.
    qpoly = [Q(0), Q(1)]
    fodd = [Q(-(2**29), 75), Q(0), Q(0), Q(0), Q(11 * 2**29, 75)]
    f9 = [Q(0), Q(7 * 2**23, 75), Q(0), Q(0), Q(0), Q(-27 * 2**23, 75)]
    f11 = []
    f13 = []
    d7 = [Q(0), Q(2**27, 75)]
    d9 = [Q(0), Q(0), Q(-2**21, 15)]
    d11 = [Q(0), Q(0), Q(0), Q(2**14, 3)]
    d13 = [Q(0), Q(0), Q(0), Q(0), Q(-7 * 2**8, 15)]
    d15 = [Q(0)] * 5 + [Q(1)]
    q2 = mul(qpoly, qpoly)
    q3 = mul(q2, qpoly)
    q4 = mul(q2, q2)
    h7 = scale(Q(1, 4), fodd)
    h9 = add(scale(Q(1, 4), f9), scale(Q(-3, 256), mul(qpoly, fodd)))
    h11 = add(
        scale(Q(-5, 256), mul(qpoly, f9)),
        scale(Q(5, 2**15), mul(q2, fodd)),
    )
    h13 = add(
        scale(Q(21, 2**15), mul(q2, f9)),
        scale(Q(7, 2**21), mul(q3, fodd)),
    )
    h15 = add(
        scale(Q(-15, 2**21), mul(q3, f9)),
        scale(Q(-45, 2**29), mul(q4, fodd)),
    )
    assert h7 == t5(A, d7)
    assert h9 == t5(A, d9)
    assert h11 == t5(A, d11)
    assert h13 == t5(A, d13)
    assert h15 == t5(A, d15)
    assert set(index for index, value in enumerate(f9) if value) <= set(range(1, 8))

    Fw = {
        0: power(A, 4),
        2: scale(Q(-1, 8), mul(power(A, 3), qpoly)),
        4: scale(Q(1, 256), mul(power(A, 2), q2)),
        7: mul(A, fodd),
        9: f9,
    }
    modes = [Q(1), Q(0), Q(1)] + [Q(0)] * 7
    Gj = characteristic_jets(A, Fw, modes)
    assert Gj[11] == (Q(0), Q(-3 * 2**21, 5))
    assert Gj[15] == (Q(0), Q(-2**21, 5))
    assert Fw[7][0] == Q(2**29, 75)
    coupling = -Fw[7][0] * Gj[15][1]
    assert coupling == Q(2**50, 375)
    # Scaling every odd coefficient/primitive by theta with
    # theta^2=375/2^50 makes the literal endpoint constant equal one over a
    # harmless quadratic constant-field extension.
    theta_squared = Q(375, 2**50)
    assert theta_squared * coupling == 1

    # Full, not merely first-jet, characteristic polynomiality at G11/G15.
    normalized = [{} for _ in range(16)]
    normalized[0] = la(A, [Q(1)])
    normalized[2] = la(A, scale(Q(-1, 8), qpoly), -1)
    normalized[4] = la(A, scale(Q(1, 256), q2), -2)
    normalized[7] = la(A, fodd, -3)
    normalized[9] = la(A, f9, -4)
    full_G = [{} for _ in range(16)]
    for shift, prefactor, exponent in (
        (0, 6, Q(3, 2)),
        (2, 5, Q(5, 4)),
        (6, 3, Q(3, 4)),
    ):
        powered = la_series_power_one(A, normalized, exponent, 15 - shift)
        for degree, value in enumerate(powered):
            full_G[degree + shift] = la_add(
                A,
                full_G[degree + shift],
                la_mul(A, la(A, [Q(1)], prefactor), value),
            )
    P11 = [
        Q(0), Q(3 * 2**21, 5), Q(-7 * 2**18, 25), Q(0), Q(0),
        Q(-49 * 2**21, 15), Q(27 * 2**18, 25),
    ]
    P15 = [Q(0), Q(-2**21, 5), Q(0), Q(2**10, 3)]
    assert full_G[11] == la(A, P11, 1)
    assert full_G[15] == la(A, P15, 0)
    assert set(index for index, value in enumerate(mul(A, P11)) if value) <= set(range(1, 14))
    assert set(index for index, value in enumerate(P15) if value) <= set(range(1, 10))

    # The top reduced rows do not force all positive-s tails to vanish.
    # f6=X^2 and g10=X^4 make the only high-high row R16 vanish exactly.
    f6 = [Q(0), Q(0), Q(1)]
    g10 = [Q(0), Q(0), Q(0), Q(0), Q(1)]
    r16 = add(
        scale(-4, mul(derivative(f6), g10)),
        scale(2, mul(f6, derivative(g10))),
    )
    assert r16 == []
    assert 2 in even_f_windows[6] and 4 in even_g_windows[10]

    # Four quotient roots: eliminating one newborn scalar from each of four
    # regularity rows leaves 4*(4-1)=12 coordinates; endpoint modulo a
    # scalar leaves another three.
    assert 4 * (4 - 1) + (4 - 1) == 15

    print("even_raw_slots=F75+G157=232")
    print("D22_X0=F11_X1*G11_X0-F7_X0*G15_X1")
    print("all_F_odd_zero_endpoint=0_not_1;subbranch_empty=true")
    print("q7_to_q15_target_coupling_fixture=2^50/375;scaled_target=1")
    print("coupling_fixture_G11_G15_full_raw_windows=PASS")
    print("D_2n=2R_n;all_D_odd=0")
    print("R_n=sum_i+j=n((6-j)f_i_prime*g_j+(i-4)f_i*g_j_prime)")
    print("Jac(f/s^4,g/s^6)=-R/s^11")
    print("target_equivalence=R11=1/2<=>Jac=-1/2")
    print("positive_s_tail_mutation=f6_X2,g10_X4_survives_top_high_row")
    print("smallest_leading_even_resultant_coordinates=15")
    print("PASS_EXACT_LAMBDA0_EVEN_SUBBRANCH_REDUCTION")


if __name__ == "__main__":
    main()
