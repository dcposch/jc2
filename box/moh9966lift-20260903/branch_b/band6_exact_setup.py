#!/usr/bin/env python3
"""Emit and verify the exact branch-B band-6 successor system over Q(a)."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp

import local_band_audit as prior


HERE = Path(__file__).resolve().parent
OUT = HERE / "band6_exact_setup.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def add(*polys):
    size = max((len(p) for p in polys), default=0)
    return [sum((p[k] if k < len(p) else 0) for p in polys) for k in range(size)]


def scale(c, p):
    return [c * value for value in p]


def mul(*polys):
    answer = [sp.Integer(1)]
    for right in polys:
        product = [sp.Integer(0)] * (len(answer) + len(right) - 1)
        for i, left_value in enumerate(answer):
            for j, right_value in enumerate(right):
                product[i + j] += left_value * right_value
        answer = product
    return answer


def power(poly, exponent):
    answer = [sp.Integer(1)]
    for _ in range(exponent):
        answer = mul(answer, poly)
    return answer


def monomial(exponent):
    return [sp.Integer(0)] * exponent + [sp.Integer(1)]


def coeff(poly, degree):
    return poly[degree] if 0 <= degree < len(poly) else sp.Integer(0)


def inverse_tail(source, weights):
    answer = [sp.Integer(0)] * (len(weights) + 1)
    for k, weight in enumerate(weights):
        answer[k + 1] = -weight * coeff(source, k)
    return answer


def main() -> None:
    z, a = prior.z, prior.a
    Hexpr = prior.H
    Lexpr = z + 3 * a
    H = [0, 0, 3 * a, 1]
    L = [3 * a, 1]
    W3 = [0, 0, 0, -18 * a, -8]
    W6 = [0, 0, 0, 0, 45 * a, 28]

    # Base expansion and exact fixed inverse-Omega tail weights.
    X = sp.symbols("X")
    base = z**3 * (1 - X**3 * z) ** 8 + 3 * a * z**2 * (1 - X**3 * z) ** 6
    assert sp.expand(sp.expand(base).coeff(X, 0) - Hexpr) == 0
    assert sp.expand(sp.expand(base).coeff(X, 3)
                     - sum(W3[k] * z**k for k in range(len(W3)))) == 0
    assert sp.expand(sp.expand(base).coeff(X, 6)
                     - sum(W6[k] * z**k for k in range(len(W6)))) == 0

    fspace = prior.strict_two_face_basis(66, 12, -2)
    gspace = prior.strict_two_face_basis(99, 18, -3)
    alpha3 = [row["v1"] for row in prior.band_entries(fspace, 3)]
    beta3 = [row["v1"] for row in prior.band_entries(gspace, 3)]
    assert alpha3 == [6, 8, 10, 13, 15, 17, 19, 22, 24, 26, 28, 31, 33, 35, 37]
    assert beta3 == [10, 12, 14, 16, 19, 21, 23, 25, 28, 30, 32, 34, 37, 39, 41, 43, 46, 48, 50, 52, 55, 57, 59, 61]

    # Operator size, rank, resonance, quotient rows, and raw H^5 rows.
    assert prior.operator_rank(6, 20) == 20
    assert sp.expand(prior.operator(6, Hexpr**6)) == 0
    qc = sp.symbols("q0:21")
    qgeneric = sum(qc[k] * z**k for k in range(21))
    operator_poly = sp.Poly(prior.operator(6, qgeneric), z)
    operator_positions = [k for k in range(23) if operator_poly.coeff_monomial(z**k) != 0]
    raw_poly = sp.Poly(3 * Hexpr**5 * prior.operator(6, qgeneric), z)
    raw_positions = [k for k in range(38) if raw_poly.coeff_monomial(z**k) != 0]
    assert operator_positions == list(range(1, 23))
    assert raw_positions == list(range(11, 38))

    # Verify q6 as the x^6 coefficient of the closed generating expression.
    eps, hh = sp.symbols("eps hh")
    symbolic_f = sp.symbols("A1:7")
    b2, b4, b6 = sp.symbols("b2 b4 b6")
    delta = sum(eps ** (i + 1) * symbolic_f[i] / hh**6 for i in range(6))

    def truncated_binomial(exponent, limit):
        return sum(sp.binomial(exponent, j) * delta**j for j in range(limit + 1))

    generating = (
        hh**9 * (3 * (1 + delta) - 2 * truncated_binomial(sp.Rational(3, 2), 6))
        + eps**2 * b2 * hh**8 * truncated_binomial(sp.Rational(4, 3), 4)
        + eps**4 * b4 * hh**7 * truncated_binomial(sp.Rational(7, 6), 2)
        + eps**6 * b6 * hh**6
    )
    A, B, C, E, J, K6 = symbolic_f
    q6 = (
        -sp.Rational(3, 2) * (A * J + B * E) / hh**3
        - sp.Rational(3, 4) * C**2 / hh**3
        + sp.Rational(3, 8) * A**2 * E / hh**9
        + sp.Rational(3, 4) * A * B * C / hh**9
        + sp.Rational(1, 8) * B**3 / hh**9
        - sp.Rational(3, 16) * A**3 * C / hh**15
        - sp.Rational(9, 32) * A**2 * B**2 / hh**15
        + sp.Rational(15, 128) * A**4 * B / hh**21
        - sp.Rational(7, 512) * A**6 / hh**27
        + sp.Rational(4, 3) * b2 * hh**2 * E
        + sp.Rational(4, 9) * b2 * A * C / hh**4
        + sp.Rational(2, 9) * b2 * B**2 / hh**4
        - sp.Rational(4, 27) * b2 * A**2 * B / hh**10
        + sp.Rational(5, 243) * b2 * A**4 / hh**16
        + sp.Rational(7, 6) * b4 * hh * B
        + sp.Rational(7, 72) * b4 * A**2 / hh**5
        + b6 * hh**6
    )
    assert sp.factor(sp.expand(generating).coeff(eps, 6) - q6) == 0

    # Independent differential-jet verification of the band equation.
    hh_z = sp.Symbol("hh_z")
    Az, Bz, Cz, Ez, Jz = sp.symbols("Az Bz Cz Ez Jz")
    jets = {A: Az, B: Bz, C: Cz, E: Ez, J: Jz}

    def derivative(expression):
        return sp.diff(expression, hh) * hh_z + sum(sp.diff(expression, value) * jet for value, jet in jets.items())

    def term(r, value, value_z, s, other):
        return (18 - s) * value_z * other + (r - 12) * value * derivative(other)

    q2 = -sp.Rational(3, 4) * A**2 / hh**3 + b2 * hh**8
    q3 = -sp.Rational(3, 2) * A * B / hh**3 + sp.Rational(1, 8) * A**3 / hh**9 + sp.Rational(4, 3) * b2 * hh**2 * A
    q4 = (
        -sp.Rational(3, 2) * A * C / hh**3 - sp.Rational(3, 4) * B**2 / hh**3
        + sp.Rational(3, 8) * A**2 * B / hh**9 - sp.Rational(3, 64) * A**4 / hh**15
        + sp.Rational(4, 3) * b2 * hh**2 * B + sp.Rational(2, 9) * b2 * A**2 / hh**4 + b4 * hh**7
    )
    q5 = (
        -sp.Rational(3, 2) * (A * E + B * C) / hh**3
        + sp.Rational(3, 8) * (A**2 * C + A * B**2) / hh**9
        - sp.Rational(3, 16) * A**3 * B / hh**15 + sp.Rational(3, 128) * A**5 / hh**21
        + sp.Rational(4, 3) * b2 * hh**2 * C + sp.Rational(4, 9) * b2 * A * B / hh**4
        - sp.Rational(4, 81) * b2 * A**3 / hh**10 + sp.Rational(7, 6) * b4 * hh * A
    )
    g1 = sp.Rational(3, 2) * hh**3 * A
    g2 = (3 * hh**3 * B - q2) / 2
    g3 = (3 * hh**3 * C - q3) / 2
    g4 = (3 * hh**3 * E - q4) / 2
    g5 = (3 * hh**3 * J - q5) / 2
    source6 = term(1, A, Az, 5, g5) + term(2, B, Bz, 4, g4) + term(3, C, Cz, 3, g3) + term(4, E, Ez, 2, g2) + term(5, J, Jz, 1, g1)
    assert sp.factor(3 * hh**5 * (2 * hh * derivative(q6) - 12 * hh_z * q6) + source6) == 0

    # Polynomial coefficient model through band 5, used to certify the fixed
    # band-6 tails and the nine automatic high-window cancellations.
    u = list(sp.symbols("u0:8"))
    v = list(sp.symbols("v0:11"))
    f3new = list(sp.symbols("f3_0:15"))
    f4new = list(sp.symbols("f4_0:14"))
    f5new = list(sp.symbols("f5_0:13"))
    f1p = mul(power(H, 3), u)
    D = mul(monomial(3), power(L, 2))
    f2p = scale(sp.Rational(1, 4), add(mul(u, u), mul(D, v)))
    Fp = add(scale(6, mul(power(H, 5), W3)), f3new)
    q2p = add(scale(-sp.Rational(3, 4), mul(power(H, 3), u, u)), scale(b2, power(H, 8)))
    g2p = scale(sp.Rational(1, 2), add(scale(3, mul(power(H, 3), f2p)), scale(-1, q2p)))
    q3p = add(scale(-sp.Rational(3, 2), mul(u, f2p)), scale(sp.Rational(1, 8), power(u, 3)), scale(sp.Rational(4, 3) * b2, mul(power(H, 5), u)))
    g3p = scale(sp.Rational(1, 2), add(scale(3, mul(power(H, 3), Fp)), scale(-1, q3p)))
    g3newp = add(g3p, scale(-9, mul(power(H, 8), W3)))
    alpha1 = [row["v1"] for row in prior.band_entries(fspace, 1)]
    alpha2 = [row["v1"] for row in prior.band_entries(fspace, 2)]
    Ep = add(inverse_tail(f1p, alpha1), f4new)
    Jp = add(inverse_tail(f2p, alpha2), f5new)
    tailf6 = add(scale(6, mul(power(H, 5), W6)), scale(15, mul(power(H, 4), W3, W3)), inverse_tail(f3new, alpha3))
    tailg6 = add(scale(9, mul(power(H, 8), W6)), scale(36, mul(power(H, 7), W3, W3)), inverse_tail(g3newp, beta3))
    q6tail = add(scale(3, mul(power(H, 3), tailf6)), scale(-2, tailg6))

    R6 = add(
        scale(-93312, mul(monomial(6), power(L, 2), Fp, Fp)),
        scale(55296 * b2, mul(monomial(10), power(L, 4), u, Fp)),
        scale(23328, mul(monomial(3), L, u, v, Fp)),
        scale(-46656, mul(monomial(9), power(L, 4), v, Ep)),
        scale(1728 * b2, mul(monomial(10), power(L, 5), v, v)),
        scale(-1152 * b2, mul(monomial(7), power(L, 3), u, u, v)),
        scale(243, mul(monomial(3), power(L, 2), v, v, v)),
        scale(-320 * b2, mul(monomial(4), L, power(u, 4))),
        scale(-1458, mul(u, u, v, v)),
    )
    Ppol = add(
        scale(-sp.Rational(3, 2), mul(u, Jp)),
        scale(sp.Rational(4, 3) * b2, mul(power(H, 2), Ep)),
        scale(sp.Rational(7, 18) * b4, mul(H, u, u)),
        scale(sp.Rational(7, 24) * b4, mul(monomial(5), power(L, 3), v)),
        scale(b6, power(H, 6)),
    )
    modulus6 = mul(monomial(12), power(L, 5))
    assert len(R6) - 1 == 46 and len(modulus6) - 1 == 17 and coeff(modulus6, 17) == 1
    work = list(R6)
    quotient_high = {}
    for degree in range(46, 37, -1):
        qdegree = degree - 17
        leader = coeff(work, degree)
        quotient_high[qdegree] = leader
        for j, divisor_coefficient in enumerate(modulus6):
            work[qdegree + j] -= leader * divisor_coefficient
    high_window = list(range(21, 30))
    for degree in high_window:
        difference = coeff(Ppol, degree) + quotient_high[degree] / 124416 - coeff(q6tail, degree)
        assert sp.expand(difference) == 0

    # Finish the same monic division and check that the advertised seventeen
    # compatibility rows really are the nonzero remainder coefficients.
    for degree in range(37, 16, -1):
        qdegree = degree - 17
        leader = coeff(work, degree)
        for j, divisor_coefficient in enumerate(modulus6):
            work[qdegree + j] -= leader * divisor_coefficient
    assert all(sp.expand(coeff(work, degree)) == 0 for degree in range(17, 47))
    assert all(sp.expand(coeff(work, degree)) != 0 for degree in range(17))

    # Independent scalar-algebra check of the compact R6 numerator.
    zz, LL, UU, VV, FF, EE, JJ = sp.symbols("zz LL UU VV FF EE JJ")
    HH = zz**2 * LL
    f1s = HH**3 * UU
    f2s = (UU**2 + zz**3 * LL**2 * VV) / 4
    q6_sub = q6.subs({hh: HH, A: f1s, B: f2s, C: FF, E: EE, J: JJ})
    P_sub = -sp.Rational(3, 2) * UU * JJ + sp.Rational(4, 3) * b2 * HH**2 * EE + sp.Rational(7, 18) * b4 * HH * UU**2 + sp.Rational(7, 24) * b4 * zz**5 * LL**3 * VV + b6 * HH**6
    R_sub = (
        -93312 * zz**6 * LL**2 * FF**2 + 55296 * b2 * zz**10 * LL**4 * UU * FF
        + 23328 * zz**3 * LL * UU * VV * FF - 46656 * zz**9 * LL**4 * VV * EE
        + 1728 * b2 * zz**10 * LL**5 * VV**2 - 1152 * b2 * zz**7 * LL**3 * UU**2 * VV
        + 243 * zz**3 * LL**2 * VV**3 - 320 * b2 * zz**4 * LL * UU**4 - 1458 * UU**2 * VV**2
    )
    assert sp.factor(q6_sub - P_sub - R_sub / (124416 * zz**12 * LL**5)) == 0

    result = {
        "status": "PASS",
        "field": "Q(a)",
        "definitions": {
            "L": "z+3*a", "H": "z^2*L", "D": "z^3*L^2",
            "W3": "-8*z^4-18*a*z^3", "W6": "28*z^5+45*a*z^4",
        },
        "new_unknowns": {
            "f6new": {"degree_max": 11, "count": 12},
            "g6new": {"degree_max": 20, "count": 21},
            "total": 33,
        },
        "tails": {
            "alpha3": alpha3, "beta3": beta3,
            "tail_f6": "6*H^5*W6+15*H^4*W3^2-sum(alpha3[k]*f3new[k]*z^(k+1),k=0..14)",
            "tail_g6": "9*H^8*W6+36*H^7*W3^2-sum(beta3[k]*coeff(g3new,z^k)*z^(k+1),k=0..23)",
            "g3new_definition": "g3-9*H^8*W3, with g3=(3*H^3*f3-q3)/2",
        },
        "equation": "E6=sum_{r+s=6}((18-s)*diff(f_r,z)*g_s+(r-12)*f_r*diff(g_s,z))=0",
        "operator": {
            "formula": "L6(q)=2*H*diff(q,z)-12*diff(H,z)*q",
            "domain_degree_max": 20, "domain_dimension": 21, "rank": 20,
            "kernel": "Q(a)*H^6", "kernel_dimension": 1,
            "quotient_row_positions": [1, 22], "quotient_row_count": 22,
            "cokernel_dimension": 2,
            "raw_row_positions_after_3H5": [11, 37], "raw_row_count": 27,
            "new_solution_kernel_dimension": 13,
        },
        "compatibility": {
            "inherited_band5": "z^6*L^2 divides N5",
            "band6_divisibility": "z^12*L^5 divides R6",
            "remainder_rows": {"count": 17, "crt_split": {"at_z_0": 12, "at_z_minus_3a": 5}, "all_structurally_nonzero": True},
            "high_window_candidate_positions": [21, 29],
            "high_window_candidate_count": 9,
            "high_window_identity_cancellations": 9,
            "additional_high_window_equations": 0,
            "allowed_degree": 20,
        },
        "q6_formula_verified": True,
        "differential_jet_identity_verified": True,
        "R6_decomposition_verified": True,
        "high_window_cancellation_verified": True,
        "references": {
            "local_band_audit.py": sha256(HERE / "local_band_audit.py"),
            "local_band_audit.json": sha256(HERE / "local_band_audit.json"),
            "band5_component_audit.json": sha256(HERE / "band5_component_audit.json"),
        },
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
