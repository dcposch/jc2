#!/usr/bin/env python3
"""Independent exact audit/extension of the active-c2 upper prefix.

Standard-library only.  The characteristic recurrence, Laurent arithmetic,
univariate raw replay, and determinant rows are reconstructed here rather
than imported from the producer checker.
"""

from __future__ import annotations

from fractions import Fraction as Q


# Sparse Laurent polynomials in A.  A key is (A-exponent, commutative word).
def atom(coefficient=1, a_exponent=0, *word):
    coefficient = Q(coefficient)
    return {(a_exponent, tuple(sorted(word))): coefficient} if coefficient else {}


def add(*items):
    out = {}
    for item in items:
        for key, coefficient in item.items():
            out[key] = out.get(key, Q(0)) + coefficient
            if not out[key]:
                del out[key]
    return out


def scale(coefficient, item):
    coefficient = Q(coefficient)
    return {key: coefficient * value for key, value in item.items()
            if coefficient * value}


def multiply(left, right):
    out = {}
    for (left_a, left_word), left_coefficient in left.items():
        for (right_a, right_word), right_coefficient in right.items():
            key = (left_a + right_a, tuple(sorted(left_word + right_word)))
            out[key] = out.get(key, Q(0)) + left_coefficient * right_coefficient
            if not out[key]:
                del out[key]
    return out


def product(*items):
    out = atom(1)
    for item in items:
        out = multiply(out, item)
    return out


def power(item, exponent):
    return product(*(item for _ in range(exponent)))


def shift(a_exponent, item):
    return {(old + a_exponent, word): coefficient
            for (old, word), coefficient in item.items()}


def substitute(item, replacements):
    out = {}
    for (a_exponent, word), coefficient in item.items():
        piece = atom(coefficient, a_exponent)
        for name in word:
            piece = multiply(piece, replacements.get(name, atom(1, 0, name)))
        out = add(out, piece)
    return out


def negative(item):
    return {key: value for key, value in item.items() if key[0] < 0}


def at_power(item, a_exponent):
    return {key: value for key, value in item.items() if key[0] == a_exponent}


def fractional_series(F, exponent, maximum):
    """Solve F*y'=exponent*F'*y coefficient by coefficient."""
    out = {0: atom(1, int(4 * exponent))}
    for n in range(1, maximum + 1):
        numerator = {}
        for i in range(1, n + 1):
            numerator = add(
                numerator,
                scale((exponent + 1) * i - n,
                      multiply(F[i], out[n - i])),
            )
        out[n] = scale(Q(1, n), shift(-4, numerator))
    return out


MODES = {
    2: Q(5, 4), 4: Q(1), 6: Q(3, 4), 8: Q(1, 2),
    10: Q(1, 4), 12: Q(0), 14: Q(-1, 4), 16: Q(-1, 2),
    18: Q(-3, 4), 20: Q(-1),
}


def characteristic(F, maximum):
    exponents = set(MODES.values()) | {Q(3, 2)}
    powers = {exponent: fractional_series(F, exponent, maximum)
              for exponent in exponents}
    G = {}
    for n in range(maximum + 1):
        row = powers[Q(3, 2)][n]
        for birth, exponent in MODES.items():
            if birth <= n:
                row = add(row, multiply(atom(1, 0, f"c{birth}"),
                                        powers[exponent][n - birth]))
        G[n] = row
    return G


def general_F(maximum):
    v, z, t = atom(1, 0, "v"), atom(1, 0, "z"), atom(1, 0, "t")
    F = {
        0: atom(1, 4),
        1: shift(2, v),
        2: scale(Q(1, 4), add(multiply(v, v), shift(2, z))),
        3: scale(Q(1, 8), add(multiply(v, z), shift(1, t))),
    }
    for n in range(4, maximum + 1):
        F[n] = atom(1, 0, f"f{n}")
    return F


# Small exact polynomial backend for literal raw-window replay.
def trim(poly):
    out = list(poly)
    while out and not out[-1]:
        out.pop()
    return out


def p_add(*items):
    out = []
    for item in items:
        size = max(len(out), len(item))
        out = trim([(out[i] if i < len(out) else Q(0))
                    + (item[i] if i < len(item) else Q(0))
                    for i in range(size)])
    return out


def p_scale(coefficient, poly):
    return trim([Q(coefficient) * value for value in poly])


def p_mul(left, right):
    if not left or not right:
        return []
    out = [Q(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return trim(out)


def p_power(poly, exponent):
    out = [Q(1)]
    for _ in range(exponent):
        out = p_mul(out, poly)
    return out


def p_derivative(poly):
    return trim([Q(i) * poly[i] for i in range(1, len(poly))])


def p_divmod(dividend, divisor):
    divisor, remainder = trim(divisor), trim(dividend)
    assert divisor
    quotient = [Q(0)] * max(0, len(remainder) - len(divisor) + 1)
    while remainder and len(remainder) >= len(divisor):
        degree = len(remainder) - len(divisor)
        coefficient = remainder[-1] / divisor[-1]
        quotient[degree] += coefficient
        remainder = p_add(
            remainder,
            p_scale(-1, [Q(0)] * degree + p_scale(coefficient, divisor)),
        )
    return trim(quotient), trim(remainder)


def evaluate_laurent(item, A, assignments):
    if not item:
        return []
    minimum = min(a_exponent for a_exponent, _ in item)
    denominator_power = max(0, -minimum)
    numerator = []
    for (a_exponent, word), coefficient in item.items():
        piece = p_scale(coefficient,
                        p_power(A, a_exponent + denominator_power))
        for name in word:
            piece = p_mul(piece, assignments.get(name, []))
        numerator = p_add(numerator, piece)
    quotient, remainder = p_divmod(numerator, p_power(A, denominator_power))
    assert not remainder
    return quotient


def determinant_rows(F, G, maximum):
    rows = {}
    for n in range(maximum + 1):
        row = []
        for i in range(n + 1):
            j = n - i
            row = p_add(
                row,
                p_scale(12 - j, p_mul(p_derivative(F[i]), G[j])),
                p_scale(i - 8, p_mul(F[i], p_derivative(G[j]))),
            )
        rows[n] = row
    return rows


def main():
    G = characteristic(general_F(15), 15)
    s, u, z = atom(1, 0, "s"), atom(1, 0, "u"), atom(1, 0, "z")
    r, q, p1 = atom(1, 0, "r"), atom(1, 0, "q"), atom(1, 0, "p1")
    f4, f5, f6, f7 = (atom(1, 0, name)
                      for name in ("f4", "f5", "f6", "f7"))
    c2 = atom(1, 0, "c2")
    K = add(scale(64, f4), scale(-1, power(z, 2)))

    # Independent reconstruction of every charged producer identity.
    active = {"v": shift(1, s), "t": shift(1, u)}
    expected = scale(Q(3, 32768), shift(-2, power(K, 2)))
    assert at_power(substitute(G[8], active), -2) == expected

    f4_K = scale(Q(1, 64), add(power(z, 2), shift(1, r)))
    K_lift = dict(active, f4=f4_K)
    H = add(power(s, 2), scale(-2, z))
    expected = scale(Q(-5, 65536), shift(-1, product(c2, power(H, 3))))
    assert negative(substitute(G[8], K_lift)) == expected

    z_H = scale(Q(1, 2), add(power(s, 2), scale(-1, shift(1, q))))
    D = add(r, scale(-4, product(s, u)))
    P = add(scale(256, f5), scale(-1, product(r, s)),
            scale(2, product(s, s, u)))
    after_H = dict(
        active,
        z=z_H,
        f4=scale(Q(1, 64), add(power(z_H, 2), shift(1, r))),
    )
    expected_D9 = scale(Q(3, 65536), shift(-1, product(D, P)))
    assert negative(substitute(G[9], after_H)) == expected_D9
    expected_D10_deep = scale(
        Q(3, 524288),
        shift(-2, product(P, add(P, scale(-2, product(s, D))))),
    )
    assert at_power(substitute(G[10], after_H), -2) == expected_D10_deep

    f5_P = scale(Q(1, 256), add(product(r, s),
                                  scale(-2, product(s, s, u)),
                                  shift(1, p1)))
    after_P = dict(after_H, f5=f5_P)
    E_general = add(scale(2048, f6), scale(-2, product(s, p1)),
                    product(q, add(r, scale(-8, product(s, u)))),
                    scale(-8, power(u, 2)))
    expected_D10_residual = scale(
        Q(1, 524288),
        shift(-1, product(D, add(scale(20, product(c2, D)),
                                 scale(3, E_general)))),
    )
    assert negative(substitute(G[10], after_P)) == expected_D10_residual

    B11 = add(
        scale(-10, product(c2, s, D)), scale(-3072, product(f6, s)),
        scale(3, product(p1, s, s)),
        scale(-3, product(q, s, add(r, scale(-6, product(s, u))))),
        scale(-6, product(u, add(r, scale(-6, product(s, u))))),
    )
    expected_D11_deep = scale(Q(1, 1048576),
                              shift(-2, product(D, B11)))
    assert at_power(substitute(G[11], after_P), -2) == expected_D11_deep

    # The producer's advertised "D=0 mod A survives D11" is too strong:
    # D=A*d leaves d*B11/A.  The exact D=0 subbranch is valid and is the
    # branch extended below.
    d = atom(1, 0, "d")
    one_A_in_D = substitute(expected_D11_deep, {"r": add(
        scale(4, product(s, u)), shift(1, d))})
    assert any(a_exponent == -1 for a_exponent, _ in one_A_in_D)
    r_exact_D0 = scale(4, product(s, u))
    exact_D0 = dict(
        active,
        z=z_H,
        f4=scale(Q(1, 64), add(power(z_H, 2), shift(1, r_exact_D0))),
        f5=scale(Q(1, 256), add(
            product(r_exact_D0, s), scale(-2, product(s, s, u)),
            shift(1, p1))),
    )

    E = add(scale(2048, f6), scale(-2, product(s, p1)),
            scale(-4, product(q, s, u)), scale(-8, power(u, 2)))
    L = add(product(q, s), scale(4, u))
    M = add(p1, scale(2, product(q, u)))
    N11 = add(scale(5, product(c2, L,
                              add(scale(4, E), power(L, 2)))),
              scale(6, product(E, M)))
    expected_D11_full = scale(Q(1, 4194304), shift(-1, N11))
    assert negative(substitute(G[11], exact_D0)) == expected_D11_full

    expected_D12_deep = scale(
        Q(1, 33554432),
        shift(-2, add(scale(3, power(E, 2)),
                      scale(-2, product(s, N11)))),
    )
    assert at_power(substitute(G[12], exact_D0), -2) == expected_D12_deep

    # Rootwise: N11=0 and 3E^2-2S*N11=0 force E=0; c2!=0 then
    # N11=5*c2*L^3 forces L=0.  Lift both exact divisibilities.
    ell, e1 = atom(1, 0, "ell"), atom(1, 0, "e1")
    u_L = scale(Q(1, 4), add(shift(1, ell), scale(-1, product(q, s))))
    f6_E = scale(Q(1, 2048), add(
        shift(1, e1), scale(2, product(s, p1)),
        scale(4, product(q, s, u_L)), scale(8, power(u_L, 2))))
    r_D0 = scale(4, product(s, u_L))
    z_lifted = z_H
    f4_lifted = scale(Q(1, 64), add(power(z_lifted, 2), shift(1, r_D0)))
    f5_lifted = scale(Q(1, 256), add(
        product(r_D0, s), scale(-2, product(s, s, u_L)), shift(1, p1)))
    lifted = {
        "v": shift(1, s), "t": shift(1, u_L), "z": z_lifted,
        "f4": f4_lifted, "f5": f5_lifted, "f6": f6_E,
    }
    assert not negative(substitute(G[11], lifted))

    J = add(p1, scale(Q(-1, 2), product(s, q, q)))
    N = add(scale(8192, f7), scale(-1, product(e1, s)), product(q, J))
    rung12 = product(J, add(scale(20, product(c2, J)), scale(3, N)))
    expected_D12_residual = scale(Q(1, 8388608), shift(-1, rung12))
    assert negative(substitute(G[12], lifted)) == expected_D12_residual
    expected_D13_deep = scale(Q(-1, 33554432),
                              shift(-2, product(s, rung12)))
    assert at_power(substitute(G[13], lifted), -2) == expected_D13_deep

    # Keep the c2=0,A|V0 stratum separate.  There H is not lifted at D8.
    P0 = add(scale(256, f5), scale(-1, product(r, s)),
             scale(2, product(s, s, u)), scale(2, product(u, H)))
    c2_zero = {"v": shift(1, s), "t": shift(1, u), "f4": f4_K, "c2": {}}
    expected_zero_D9 = scale(Q(3, 65536), shift(-1, product(D, P0)))
    assert negative(substitute(G[9], c2_zero)) == expected_zero_D9
    expected_zero_D10_deep = scale(
        Q(3, 524288), shift(-2, add(
            product(P0, add(P0, scale(-2, product(s, D)))),
            product(H, D, D),
        )))
    assert at_power(substitute(G[10], c2_zero), -2) == expected_zero_D10_deep

    # Literal raw-window survivor through D15 on the active c2 open.
    # A=X^4-1, S=Q=c2=c6=1, ell=e1=0, P1=1/2, F7=...=F15=0.
    # D14 uniquely chooses the displayed c14; D15 then vanishes as well.
    A = [Q(-1), Q(0), Q(0), Q(0), Q(1)]
    Z = p_scale(Q(1, 2), p_add([Q(1)], p_scale(-1, A)))
    U = [Q(-1, 4)]
    R = [Q(-1)]
    F4 = p_scale(Q(1, 64), p_add(p_mul(Z, Z), p_mul(A, R)))
    F5 = p_scale(Q(1, 512), p_add(A, [Q(-1)]))
    assignments = {
        "v": A, "t": p_scale(Q(-1, 4), A), "z": Z,
        "f4": F4, "f5": F5, "f6": [Q(1, 4096)],
        **{f"f{n}": [] for n in range(7, 16)},
        "c2": [Q(1)], "c6": [Q(1)],
        "c14": [Q(-6139, 17179869184)],
        **{f"c{n}": [] for n in (4, 8, 10, 12, 16, 18, 20)},
    }
    raw_G = {n: evaluate_laurent(G[n], A, assignments) for n in range(16)}
    A2 = p_power(A, 2)
    raw_F = {
        0: p_power(A, 4),
        1: p_mul(A2, A),
        2: p_scale(Q(1, 4), p_add(p_mul(A, A), p_mul(A2, Z))),
        3: p_scale(Q(1, 8), p_add(p_mul(A, Z),
                                          p_mul(A, p_scale(Q(-1, 4), A)))),
        4: F4, 5: F5, 6: [Q(1, 4096)],
        **{n: [] for n in range(7, 16)},
    }
    raw_D = determinant_rows(raw_F, raw_G, 15)
    assert all(not raw_D[n] for n in range(16))
    assert all(len(raw_F[n]) - 1 <= 16 - n for n in range(1, 16))
    assert all(len(raw_G[n]) - 1 <= 24 - n for n in range(1, 16))
    assert raw_G[12] == [Q(4093, 268435456)]
    assert raw_G[13] == []
    assert raw_G[14] == []
    assert raw_G[15] == []

    # Mutations catch the two new lifts and the first c6-sensitive successor.
    assert negative(substitute(G[11], {
        "v": shift(1, atom(1)), "t": shift(1, atom(Q(-1, 4))),
        "z": add(atom(Q(1, 2)), atom(Q(-1, 2), 1)),
        "f4": add(atom(Q(1, 32)), atom(Q(-1, 32), 1), atom(Q(1, 256), 2)),
        "f5": add(atom(Q(-1, 256)), atom(Q(1, 512), 1)),
        "f6": {}, "c2": atom(1), "c6": atom(1),
    }))
    mutated = dict(assignments, f7=[Q(1)])
    numerator, remainder = p_divmod(
        # Evaluate A*g13 so the nonzero pole numerator is literal.
        evaluate_laurent(shift(1, G[13]), A, mutated), [Q(1)])
    assert not remainder and numerator == [Q(6139, 8192)]

    print("PASS_REPAIR_ACTIVE_C2_D8_D13_EXTENSION")
    print("charged_prefix=D8,D9,D10,D11 identities exact")
    print("repair=A|D alone does_not clear D*B11/A^2; exact D=0 used")
    print("D11+D12_on_D0=A|E and A|L field-radically on c2!=0")
    print("postlift_D12=J*(20*c2*J+3*N)/(8388608*A)")
    print("raw_survivor=D0..D15 zero; c2=c6=1; c14!=0; literal windows PASS")
    print("c2_zero_companion=kept_separate")


if __name__ == "__main__":
    main()
