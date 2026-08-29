#!/usr/bin/env python3
"""Small exact replay for the reviewed rank-one HENS-CT control.

Standard-library only.  This does not claim an algebraic CT certificate; it
fixes the receiver gauge, scalar formulas, indices, and mutation controls that
any emitted certificate must respect.
"""

from fractions import Fraction as Q
from math import comb


def binom(a: Q, n: int) -> Q:
    out = Q(1)
    for j in range(n):
        out *= a - j
        out /= j + 1
    return out


def alpha(n: int) -> Q:
    return Q(2, n + 2) * binom(Q(n + 2, 8), n)


def mul(a, b):
    out = {}
    for i, ai in a.items():
        for j, bj in b.items():
            out[i + j] = out.get(i + j, Q(0)) + ai * bj
    return {e: c for e, c in out.items() if c}


def power(a, n):
    out = {0: Q(1)}
    while n:
        if n & 1:
            out = mul(out, a)
        a = mul(a, a)
        n //= 2
    return out


HSHAPE = {0: Q(1), -3: Q(1), -7: Q(1)}


def q_laurent(n: int):
    return {e + 2: alpha(n) * c for e, c in power(HSHAPE, n).items()}


def residue(poly):
    return poly.get(-1, Q(0))


def shifted_coefficient(poly, shift, exponent):
    """Coefficient of X^exponent in X^shift poly."""
    return poly.get(exponent - shift, Q(0))


def d7(n):
    return n * (n + 1) * (n + 3) * (n + 4) * (n + 5) * (n + 6) * (n + 7)


def n7(n):
    out = Q(-1, 8)
    for i in range(7):
        out *= Q(7 * n - 2, 8) + i
    return out


def main():
    cs = []
    for n in range(33):
        qn = q_laurent(n)
        got = residue(qn)
        want = n * alpha(n)
        assert got == want, (n, got, want)
        cs.append(got)

    for n in range(25):
        assert Q(d7(n)) * cs[n + 8] == n7(n) * cs[n], n

    # Correct fixed receiver: m0=b+22 and basis X^(-m0-1)dX.  Its
    # coordinate in X^(-m0)q_n dX is Res(q_n dX).
    for b in range(4):
        m0 = b + 22
        for k in range(5):
            n = b + 4 * k
            qn = q_laurent(n)
            got = shifted_coefficient(qn, -m0, -m0 - 1)
            assert got == cs[n]

    # Mutation 1: omit +22 in the coefficient but retain V_(b+22).
    # At b=1,k=0 this false normalization turns the nonzero 1/4 row into 0.
    b = 1
    q1 = q_laurent(1)
    correct = shifted_coefficient(q1, -(b + 22), -(b + 23))
    wrong = shifted_coefficient(q1, -b, -(b + 23))
    assert correct == Q(1, 4) and wrong == 0

    # Mutation 2: literal/double H^k weighting changes gate coordinates.
    double_weight_witness = None
    for b in range(4):
        for k in range(1, 7):
            n = b + 4 * k
            literal = shifted_coefficient(q_laurent(n), 4 * k, -1)
            if literal != cs[n]:
                double_weight_witness = (b, k, n, cs[n], literal)
                break
        if double_weight_witness:
            break
    assert double_weight_witness is not None

    # Mutation 3: +b projector extracts -b mod 4 rather than b mod 4.
    # Its first physical index differs for b=1.
    assert 1 % 4 != (-1) % 4
    assert cs[1] != cs[3]

    # Mutation 4: C_2 is even because n=6 mod 8 at odd k is class-zero;
    # C_0 is not even (k=1 is n=4 and is nonzero).
    for k in range(1, 7, 2):
        assert cs[2 + 4 * k] == 0
    assert cs[4] != 0

    # Primitive step-eight recurrence startup.  Forward D7(n) is singular
    # only at n=0 on n>=0.  c0=0 is automatic; c1..c8 determine the tail.
    nonnegative_roots = [n for n in range(40) if d7(n) == 0]
    assert nonnegative_roots == [0]

    print("PASS_RANK_ONE_CONTROLS")
    print("receiver[b]=V_(b+22); basis=X^(-(b+23))dX")
    print("index_map: n=b+4k; m=n+22")
    print("scalar_startup: c0=0; check c1..c8; max_physical_n=8; max_row_m=30")
    print("section_startup: b0 k<=2; b1,b2,b3 k<=1")
    print("forward_D7_nonnegative_roots=", nonnegative_roots)
    print("double_H_mutation_witness=", double_weight_witness)
    print("wrong_plus22_mutation: correct=", correct, "wrong=", wrong)
    print("sector_parity: b2_odd_k_zero=true; b0_k1=", cs[4])


if __name__ == "__main__":
    main()

