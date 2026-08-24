#!/usr/bin/env python3
"""Exact replay for the balanced cyclotomic AS triangular controls.

This is a finite-depth producer check.  It does not classify a fixed-degree
lift locus and makes no all-depth or characteristic-zero inference.
"""

from fractions import Fraction
from hashlib import sha256
import json


def conv(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    return out


def v3_integer(n):
    if n == 0:
        return 10**9
    n = abs(n)
    out = 0
    while n % 3 == 0:
        n //= 3
        out += 1
    return out


def v3_fraction(q):
    return v3_integer(q.numerator) - v3_integer(q.denominator)


def mod_fraction(q, modulus):
    den = q.denominator % modulus
    assert den % 3 != 0
    return (q.numerator % modulus) * pow(den, -1, modulus) % modulus


def build(m):
    assert m >= 3 and m % 2 == 1
    # A=(1+z)(1+...+z^(m-1)); B=A(-z).
    A = [1] + [2] * (m - 1) + [1]
    B = [((-1) ** k) * c for k, c in enumerate(A)]
    product = conv(A, B)
    expected = [0] * (2 * m + 1)
    expected[0] = 1
    expected[2 * m] = -1
    assert product == expected

    # z=3*x^2.  P is the unique zero-constant 3-adic antiderivative
    # of A(3*x^2); Q=y*B(3*x^2).
    P = {
        2 * k + 1: Fraction(A[k] * (3**k), 2 * k + 1)
        for k in range(m + 1)
    }
    Qy = {2 * k: B[k] * (3**k) for k in range(m + 1)}
    assert all(v3_fraction(c) >= 0 for c in P.values())
    assert P[3] % 3 == 2
    assert all(v3_fraction(c) >= 1 for e, c in P.items() if e not in (1, 3))
    assert all(c % 3 == 0 for e, c in Qy.items() if e != 0)

    depth = 2 * m
    degree = 2 * m + 1
    modulus = 3**depth
    next_modulus = 3 ** (depth + 1)
    P_mod = {str(e): mod_fraction(c, modulus) for e, c in P.items()}
    P_clean_next = {
        str(e): mod_fraction(c, next_modulus) for e, c in P.items()
    }
    Q_mod = {str(e): c % modulus for e, c in Qy.items()}

    # det=A(z)B(z)=1-z^(2m)=1-3^(2m)x^(4m).
    residual_exponent = 4 * m
    assert residual_exponent > degree - 1
    return {
        "m": m,
        "degree_cap": degree,
        "survival_depth": depth,
        "A_coefficients": A,
        "B_coefficients": B,
        "AB": {"0": 1, str(2 * m): -1},
        "P_mod_3^depth": P_mod,
        "P_clean_mod_3^(depth+1)": P_clean_next,
        "Qy_mod_3^depth": Q_mod,
        "special_fibre": ["x-x^3", "y"],
        "determinant": f"1-3^{2*m}*x^{4*m}",
        "next_residual_mod3": f"-x^{4*m}",
        "max_next_divergence_degree": degree - 1,
        "terminal_at_next_depth": True,
    }


def main():
    records = [build(m) for m in (3, 5, 7, 9)]

    # The m=3 reduction must recover the separately frozen D7 point, and the
    # next representative must recover its clean x^7 coefficient.
    r3 = records[0]
    assert r3["degree_cap"] == 7
    assert r3["survival_depth"] == 6
    assert r3["P_mod_3^depth"] == {
        "1": 1,
        "3": 2,
        "5": 441,
        "7": 108,
    }
    assert r3["P_clean_mod_3^(depth+1)"]["7"] == 1566
    assert r3["Qy_mod_3^depth"] == {
        "0": 1,
        "2": 723,
        "4": 18,
        "6": 702,
    }

    payload = {
        "family": "odd m>=3, D=2m+1, depth=2m",
        "identity": "A_m(z)A_m(-z)=1-z^(2m)",
        "records": records,
        "scope": "finite-depth triangular terminal controls only",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    digest = sha256(canonical.encode()).hexdigest()
    print(json.dumps(payload, indent=2, sort_keys=True))
    print("PASS-AS-FONLY-P3-BALANCED-CYCLOTOMIC-FAMILY")
    print("m3=FROZEN-D7-POINT-RECOVERED")
    print("m5=D11-SURVIVES-DEPTH10-TERMINAL-DEPTH11")
    print("all_depth_inference=false")
    print(f"payload_sha256={digest}")


if __name__ == "__main__":
    main()
