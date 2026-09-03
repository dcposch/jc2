#!/usr/bin/env python3
"""Exact first bands of the straightened radius-two branch-B chart.

This is deliberately a *slice*, not Moh's omitted full eleven-variable
chart.  In old coordinates (X,Y) the two top directions are straightened to
Y=0 and Y=X, and Omega_0 is X=x^-1, Y=x^3 y.  The code constructs the exact
finite-dimensional old-polynomial spaces which are strict above both fixed
faces, transports their associated graded to z=xy, checks the first four
Jacobian bands over Q(a), and emits the exact compatibility system for band 5.

No conclusion from a nonempty band is promoted to existence of a Keller
pair.  The parameters a and c are never specialized; their nonzero strata are
recorded by separate Rabinowitsch equations in the output.
"""

from __future__ import annotations

import hashlib
import json
import math
from collections import Counter
from fractions import Fraction
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
OUT = HERE / "local_band_audit.json"

z, a = sp.symbols("z a")
H = z**2 * (z + 3 * a)
D = z**3 * (z + 3 * a) ** 2


def strict_two_face_basis(Degree: int, local_pole: int, major_order: int):
    """Basis metadata in the K=t^Degree P(t^-1,w/t) presentation.

    local_pole L means ord P >= -L at w=t^3*z.  At the major face
    w=1+pi*t^(4/3), ``major_order`` is ord P.  Adding one to each
    integralized threshold makes the perturbation strict at both faces.

    An entry represents, up to the harmless sign (-1)^v1,

      X^(Degree-i-k-v1) Y^k (Y-X)^v1,

    and begins locally as x^band z^k (1-x^3 z)^v1 after multiplication by
    x^local_pole.  Thus later inverse-Omega tails occur exactly every three
    bands and are not independent coefficients.
    """
    minor_threshold = Degree - local_pole
    major_threshold = 3 * (Degree + major_order)
    entries = []
    for i in range(Degree + 1):
        cap = Degree - i
        v0 = max(0, math.ceil((minor_threshold + 1 - i) / 3))
        v1 = max(0, math.ceil((major_threshold + 1 - 3 * i) / 4))
        residual_degree = cap - v0 - v1
        for residual_power in range(max(0, residual_degree + 1)):
            k = v0 + residual_power
            band = i + 3 * k - minor_threshold
            x_power = Degree - i - k - v1
            assert x_power >= 0 and band >= 1
            entries.append(
                {
                    "i": i,
                    "k": k,
                    "v0": v0,
                    "v1": v1,
                    "residual_power": residual_power,
                    "old_monomial": (
                        f"X^{x_power}*Y^{k}*(Y-X)^{v1}"
                    ),
                    "start_band": band,
                    "local_series": f"x^{band}*z^{k}*(1-x^3*z)^{v1}",
                }
            )
    return entries


def nonstrict_dimension(Degree: int, local_pole: int, major_order: int) -> int:
    minor_threshold = Degree - local_pole
    major_threshold = 3 * (Degree + major_order)
    total = 0
    for i in range(Degree + 1):
        cap = Degree - i
        v0 = max(0, math.ceil((minor_threshold - i) / 3))
        v1 = max(0, math.ceil((major_threshold - 3 * i) / 4))
        total += max(0, cap - v0 - v1 + 1)
    return total


def start_histogram(entries):
    return dict(sorted(Counter(row["start_band"] for row in entries).items()))


def band_entries(entries, band):
    return sorted(
        [row for row in entries if row["start_band"] == band],
        key=lambda row: row["k"],
    )


def jac_band_term(r, f, s, g):
    """Coefficient contribution to

      18 f_z g - 12 f g_z + x(f_x g_z-f_z g_x).
    """
    return sp.expand((18 - s) * sp.diff(f, z) * g + (r - 12) * f * sp.diff(g, z))


def operator(n, q):
    return sp.expand(2 * H * sp.diff(q, z) + (n - 18) * sp.diff(H, z) * q)


def operator_rank(n: int, q_degree: int) -> int:
    qs = sp.symbols(f"q{n}_0:{q_degree + 1}")
    q = sum(qs[k] * z**k for k in range(q_degree + 1))
    image = sp.Poly(operator(n, q), z)
    rows = image.degree() + 1
    matrix = sp.zeros(rows, len(qs))
    for degree in range(rows):
        coefficient = image.coeff_monomial(z**degree)
        for column, variable in enumerate(qs):
            matrix[degree, column] = coefficient.coeff(variable)
    return matrix.rank()


def coefficient_degree_range(entries, band):
    rows = band_entries(entries, band)
    ks = [row["k"] for row in rows]
    assert ks == list(range(min(ks), max(ks) + 1))
    return [min(ks), max(ks)]


def nonzero_z_rows(poly):
    return len(sp.Poly(sp.expand(poly), z).terms())


def remainder_mod_D(poly):
    """Exact monic reduction modulo D=z^5+6*a*z^4+9*a^2*z^3.

    A small explicit reducer is substantially faster here than a generic
    multivariate-domain division and makes the five band-4 equations fully
    machine-readable in the JSON artifact.
    """
    source = sp.Poly(sp.expand(poly), z)
    coefficients = {
        degree: source.coeff_monomial(z**degree)
        for degree in range(source.degree() + 1)
    }
    for degree in range(source.degree(), 4, -1):
        leader = coefficients.get(degree, 0)
        coefficients[degree] = 0
        coefficients[degree - 1] = sp.expand(
            coefficients.get(degree - 1, 0) - 6 * a * leader
        )
        coefficients[degree - 2] = sp.expand(
            coefficients.get(degree - 2, 0) - 9 * a**2 * leader
        )
    return [sp.factor(coefficients.get(degree, 0)) for degree in range(5)]


def main():
    fspace = strict_two_face_basis(66, 12, -2)
    gspace = strict_two_face_basis(99, 18, -3)
    t2space = strict_two_face_basis(55, 10, Fraction(-5, 3))
    t3space = strict_two_face_basis(145, 25, -5)
    assert len(fspace) == 146
    assert len(gspace) == 336
    assert len(t2space) == 100
    assert len(t3space) == 740
    assert nonstrict_dimension(66, 12, -2) == 181
    assert nonstrict_dimension(99, 18, -3) == 388
    assert nonstrict_dimension(55, 10, Fraction(-5, 3)) == 129
    assert nonstrict_dimension(145, 25, -5) == 816

    # Exact normalized local identity.  If
    # Omega(F)=x^-12*f(x,z), Omega(G)=x^-18*g(x,z), z=xy, then
    # J_xy(Omega(F),Omega(G))=c*x iff E=c*x^31.
    recurrence = (
        "E_n=sum_{r+s=n}((18-s)*diff(f_r,z)*g_s"
        "+(r-12)*f_r*diff(g_s,z))-c*[n=31]"
    )

    # Band 1.
    f1c = sp.symbols("f1_0:17")
    g1c = sp.symbols("g1_0:26")
    f1 = sum(f1c[k] * z**k for k in range(17))
    g1 = sum(g1c[k] * z**k for k in range(26))
    q1 = sp.expand(3 * H**3 * f1 - 2 * g1)
    e1 = sp.expand(jac_band_term(1, f1, 0, H**9) + jac_band_term(0, H**6, 1, g1))
    assert sp.expand(e1 - 3 * H**5 * operator(1, q1)) == 0
    assert nonzero_z_rows(e1) == 32
    assert nonzero_z_rows(operator(1, q1)) == 27
    assert operator_rank(1, 25) == 26
    # q1=0 is an invertible (-2)-pivot presentation of the solution, so the
    # preceding exact factorization already proves E1=0 on it.  Avoid a much
    # slower sequential 26-variable substitution here.

    # Band 2 after the band-1 pivots.
    f2c = sp.symbols("f2_0:16")
    f2 = sum(f2c[k] * z**k for k in range(16))
    b2 = sp.Symbol("b2")
    g1sol = sp.Rational(3, 2) * H**3 * f1
    source2 = sp.expand(jac_band_term(1, f1, 1, g1sol))
    source2_closed = sp.Rational(9, 2) * H**2 * f1 * (
        2 * H * sp.diff(f1, z) - 11 * sp.diff(H, z) * f1
    )
    assert sp.expand(source2 - source2_closed) == 0
    g2generic_c = sp.symbols("g2_0:25")
    g2generic = sum(g2generic_c[k] * z**k for k in range(25))
    e2generic = sp.expand(
        jac_band_term(2, f2, 0, H**9)
        + jac_band_term(0, H**6, 2, g2generic)
        + source2_closed
    )
    assert nonzero_z_rows(e2generic) == 36
    q2generic_c = sp.symbols("qq2_0:25")
    q2generic = sum(q2generic_c[k] * z**k for k in range(25))
    assert nonzero_z_rows(operator(2, q2generic)) == 25
    assert nonzero_z_rows(3 * H**5 * operator(2, q2generic)) == 30
    assert operator_rank(2, 24) == 24

    u12 = sp.symbols("u0:12")
    U12 = sum(u12[k] * z**k for k in range(12))
    f1_band2 = sp.expand(D * U12)
    q2part = sp.cancel(-sp.Rational(3, 4) * f1_band2**2 / H**3)
    assert sp.denom(q2part) == 1
    source2_band2 = sp.Rational(9, 2) * H**2 * f1_band2 * (
        2 * H * sp.diff(f1_band2, z) - 11 * sp.diff(H, z) * f1_band2
    )
    assert sp.expand(3 * H**5 * operator(2, q2part) + source2_band2) == 0
    q2 = sp.expand(q2part + b2 * H**8)
    g2 = sp.expand((3 * H**3 * f2 - q2) / 2)

    # Band 3.  Its rational normal form is checked before imposing the
    # extra divisibility.  Polynomiality upgrades D|f1 to H^3|f1.
    # Check the universal band-3 identity with abstract coefficient
    # functions.  This is dramatically smaller than expanding 28 generic
    # coefficient variables, and is the same differential-polynomial
    # identity.
    FF1 = sp.Function("FF1")(z)
    FF2 = sp.Function("FF2")(z)
    GG1 = sp.Rational(3, 2) * H**3 * FF1
    QQ2 = -sp.Rational(3, 4) * FF1**2 / H**3 + b2 * H**8
    GG2 = (3 * H**3 * FF2 - QQ2) / 2
    QQ3 = (
        -sp.Rational(3, 2) * FF1 * FF2 / H**3
        + sp.Rational(1, 8) * FF1**3 / H**9
        + sp.Rational(4, 3) * b2 * H**2 * FF1
    )
    source3_abstract = jac_band_term(1, FF1, 2, GG2) + jac_band_term(2, FF2, 1, GG1)
    assert sp.simplify(3 * H**5 * operator(3, QQ3) + source3_abstract) == 0
    assert operator_rank(3, 23) == 24
    q3generic_c = sp.symbols("qq3_0:24")
    q3generic = sum(q3generic_c[k] * z**k for k in range(24))
    assert nonzero_z_rows(operator(3, q3generic)) == 25
    assert nonzero_z_rows(3 * H**5 * operator(3, q3generic)) == 30

    u8 = sp.symbols("v0:8")
    U8 = sum(u8[k] * z**k for k in range(8))
    f1_band3 = H**3 * U8
    q3 = sp.expand(
        -sp.Rational(3, 2) * U8 * f2
        + sp.Rational(1, 8) * U8**3
        + sp.Rational(4, 3) * b2 * H**5 * U8
    )

    # Exact band 4.  The inverse-Omega tails from
    # band 1 are fixed, not new coordinates.  Polynomiality of the canonical
    # q4 is equivalent on a!=0 to D | (4*f2-U8^2).
    band1_f = band_entries(fspace, 1)
    band1_g = band_entries(gspace, 1)
    assert [row["k"] for row in band1_f] == list(range(17))
    assert [row["k"] for row in band1_g] == list(range(26))
    tail_f4 = sp.expand(
        sum(-band1_f[k]["v1"] * sp.Poly(f1_band3, z).coeff_monomial(z**k) * z ** (k + 1) for k in range(17))
    )
    g1_band3 = sp.Rational(3, 2) * H**3 * f1_band3
    tail_g4 = sp.expand(
        sum(-band1_g[k]["v1"] * sp.Poly(g1_band3, z).coeff_monomial(z**k) * z ** (k + 1) for k in range(26))
    )
    q4_tail = sp.expand(3 * H**3 * tail_f4 - 2 * tail_g4)
    f3low = sp.symbols("f3_0:15")
    W3 = -8 * z**4 - 18 * a * z**3
    f3 = sp.expand(6 * H**5 * W3 + sum(f3low[k] * z**k for k in range(15)))
    q4_formula_text = (
        "-(3/2)*f1*f3/H^3-(3/4)*f2^2/H^3"
        "+(3/8)*f1^2*f2/H^9-(3/64)*f1^4/H^15"
        "+(4/3)*b2*H^2*f2+(2/9)*b2*f1^2/H^4+b4*H^7"
    )
    b4 = sp.Symbol("b4")
    v11 = sp.symbols("w0:11")
    V11 = sum(v11[k] * z**k for k in range(11))
    f2_band4 = sp.expand((U8**2 + D * V11) / 4)
    # After f1=H^3*U and 4*f2-U^2=D*V, the only apparently rational block
    # collapses to -(3/64)*(D^2/H^3)*V^2.  Here D^2/H^3=z+3a.
    assert sp.cancel(D**2 / H**3) == z + 3 * a
    q4poly = sp.expand(
        -sp.Rational(3, 2) * U8 * f3
        -sp.Rational(3, 64) * (z + 3 * a) * V11**2
        +sp.Rational(4, 3) * b2 * H**2 * f2_band4
        +sp.Rational(2, 9) * b2 * H**2 * U8**2
    )
    assert sp.degree(sp.expand(q4poly - q4_tail), z) <= 22
    q4 = sp.expand(q4poly + b4 * H**7)
    f4new_c = sp.symbols("f4_0:14")
    f4new = sum(f4new_c[k] * z**k for k in range(14))
    f4 = sp.expand(tail_f4 + f4new)
    g4 = sp.expand((3 * H**3 * f4 - q4) / 2)
    g4new = sp.expand(g4 - tail_g4)
    assert sp.degree(g4new, z) <= 22
    assert operator_rank(4, 22) == 22
    q4generic_c = sp.symbols("qq4_0:23")
    q4generic = sum(q4generic_c[k] * z**k for k in range(23))
    assert nonzero_z_rows(operator(4, q4generic)) == 24
    assert nonzero_z_rows(3 * H**5 * operator(4, q4generic)) == 29
    band4_remainders = remainder_mod_D(4 * f2 - U8**2)
    assert len(band4_remainders) == 5

    # Independent differential-polynomial checks of the band-4 formula and
    # of the compact band-5 formula below.  Replacing functions and their
    # first derivatives by algebraically independent jets makes these exact
    # identities over Q, without relying on a numerical specialization.
    hh, hh_z = sp.symbols("hh hh_z")
    AA, AA_z, BB, BB_z, CC, CC_z, EE, EE_z = sp.symbols(
        "AA AA_z BB BB_z CC CC_z EE EE_z"
    )

    def jet_derivative(expression):
        return sp.expand(
            sp.diff(expression, hh) * hh_z
            + sp.diff(expression, AA) * AA_z
            + sp.diff(expression, BB) * BB_z
            + sp.diff(expression, CC) * CC_z
            + sp.diff(expression, EE) * EE_z
        )

    def jet_term(r, ff, ff_z, s, gg):
        return sp.expand(
            (18 - s) * ff_z * gg + (r - 12) * ff * jet_derivative(gg)
        )

    jq2 = -sp.Rational(3, 4) * AA**2 / hh**3 + b2 * hh**8
    jg1 = sp.Rational(3, 2) * hh**3 * AA
    jg2 = (3 * hh**3 * BB - jq2) / 2
    jq3 = (
        -sp.Rational(3, 2) * AA * BB / hh**3
        + sp.Rational(1, 8) * AA**3 / hh**9
        + sp.Rational(4, 3) * b2 * hh**2 * AA
    )
    jg3 = (3 * hh**3 * CC - jq3) / 2
    jq4 = (
        -sp.Rational(3, 2) * AA * CC / hh**3
        - sp.Rational(3, 4) * BB**2 / hh**3
        + sp.Rational(3, 8) * AA**2 * BB / hh**9
        - sp.Rational(3, 64) * AA**4 / hh**15
        + sp.Rational(4, 3) * b2 * hh**2 * BB
        + sp.Rational(2, 9) * b2 * AA**2 / hh**4
        + b4 * hh**7
    )
    jg4 = (3 * hh**3 * EE - jq4) / 2
    jsource4 = (
        jet_term(1, AA, AA_z, 3, jg3)
        + jet_term(2, BB, BB_z, 2, jg2)
        + jet_term(3, CC, CC_z, 1, jg1)
    )
    assert sp.factor(
        3 * hh**5 * (2 * hh * jet_derivative(jq4) - 14 * hh_z * jq4)
        + jsource4
    ) == 0

    # Band 5 is left as the exact next system.  Its fixed tails are the
    # x^3-corrections to band 2.  The rational particular solution has a
    # compact numerator N5 and denominator M5 after the band-4 conditions.
    band2_f = band_entries(fspace, 2)
    band2_g = band_entries(gspace, 2)
    assert [row["k"] for row in band2_f] == list(range(16))
    assert [row["k"] for row in band2_g] == list(range(25))
    q2_band4 = sp.expand(-sp.Rational(3, 4) * H**3 * U8**2 + b2 * H**8)
    g2_band4 = sp.expand((3 * H**3 * f2_band4 - q2_band4) / 2)
    tail_f5 = sp.expand(
        sum(
            -band2_f[k]["v1"]
            * sp.Poly(f2_band4, z).coeff_monomial(z**k)
            * z ** (k + 1)
            for k in range(16)
        )
    )
    tail_g5 = sp.expand(
        sum(
            -band2_g[k]["v1"]
            * sp.Poly(g2_band4, z).coeff_monomial(z**k)
            * z ** (k + 1)
            for k in range(25)
        )
    )
    q5_tail = sp.expand(3 * H**3 * tail_f5 - 2 * tail_g5)
    q5_formula_text = (
        "-(3/2)*(f1*f4+f2*f3)/H^3"
        "+(3/8)*(f1^2*f3+f1*f2^2)/H^9"
        "-(3/16)*f1^3*f2/H^15+(3/128)*f1^5/H^21"
        "+(4/3)*b2*H^2*f3+(4/9)*b2*f1*f2/H^4"
        "-(4/81)*b2*f1^3/H^10+(7/6)*b4*H*f1"
    )
    jq5 = (
        -sp.Rational(3, 2) * (AA * EE + BB * CC) / hh**3
        + sp.Rational(3, 8) * (AA**2 * CC + AA * BB**2) / hh**9
        - sp.Rational(3, 16) * AA**3 * BB / hh**15
        + sp.Rational(3, 128) * AA**5 / hh**21
        + sp.Rational(4, 3) * b2 * hh**2 * CC
        + sp.Rational(4, 9) * b2 * AA * BB / hh**4
        - sp.Rational(4, 81) * b2 * AA**3 / hh**10
        + sp.Rational(7, 6) * b4 * hh * AA
    )
    jsource5 = (
        jet_term(1, AA, AA_z, 4, jg4)
        + jet_term(2, BB, BB_z, 3, jg3)
        + jet_term(3, CC, CC_z, 2, jg2)
        + jet_term(4, EE, EE_z, 1, jg1)
    )
    assert sp.factor(
        3 * hh**5 * (2 * hh * jet_derivative(jq5) - 13 * hh_z * jq5)
        + jsource5
    ) == 0

    sroot = z + 3 * a
    m5 = sp.expand(z**6 * sroot**2)
    # This is 10368 times the numerator of the non-polynomial part of q5.
    n5 = sp.expand(
        243 * U8 * V11**2
        - 3888 * z**3 * sroot * V11 * f3
        + 640 * b2 * z**4 * sroot * U8**3
    )
    quotient5, remainder5 = sp.div(sp.Poly(n5, z), sp.Poly(m5, z))
    band5_remainders = [
        sp.expand(remainder5.coeff_monomial(z**degree)) for degree in range(8)
    ]
    assert all(value != 0 for value in band5_remainders)
    assert quotient5.degree() == 25

    # Once M5|N5, the four apparent high coefficients of q5-q5_tail cancel
    # identically.  Check this without expanding the much larger whole sum.
    def coefficient(expression, degree):
        return sp.Poly(expression, z).coeff_monomial(z**degree)

    def product_coefficient(left, right, degree):
        return sum(
            coefficient(left, index) * coefficient(right, degree - index)
            for index in range(degree + 1)
        )

    p5_term_1 = -sp.Rational(3, 2) * U8 * f4
    p5_term_2 = sp.Rational(4, 3) * b2 * H**2 * f3
    p5_term_3 = sp.Rational(7, 6) * b4 * H**4 * U8
    p5_term_4 = sp.Rational(1, 9) * b2 * U8 * z * sroot * V11
    for degree in range(22, 26):
        high_coefficient = sp.expand(
            coefficient(p5_term_1, degree)
            + coefficient(p5_term_2, degree)
            + coefficient(p5_term_3, degree)
            + coefficient(p5_term_4, degree)
            + quotient5.coeff_monomial(z**degree) / 10368
            - coefficient(q5_tail, degree)
        )
        assert high_coefficient == 0
    assert operator_rank(5, 21) == 22
    q5generic_c = sp.symbols("qq5_0:22")
    q5generic = sum(q5generic_c[k] * z**k for k in range(22))
    assert nonzero_z_rows(operator(5, q5generic)) == 23
    assert nonzero_z_rows(3 * H**5 * operator(5, q5generic)) == 28

    hist_f = start_histogram(fspace)
    hist_g = start_histogram(gspace)
    result = {
        "scope": "STRAIGHTENED-ZERO-JET-TWO-FACE-SLICE; necessary local control, not Moh's omitted full lift",
        "field": "Q(a)",
        "ambient_localized_ring": "Q[a,c,Ta,Tc,...]/(Ta*a-1,Tc*c-1)",
        "rabinowitsch": ["Ta*a-1", "Tc*c-1"],
        "H": str(sp.factor(H)),
        "branch_factor": "a != 0",
        "old_coordinate_base_h": "Y^3*(Y-X)^8+3*a*Y^2*(Y-X)^6",
        "Omega0": "X=x^-1, Y=x^3*y; z=x*y",
        "normalized_jacobian_identity": "18*f_z*g-12*f*g_z+x*(f_x*g_z-f_z*g_x)-c*x^31=0",
        "band_recurrence": recurrence,
        "spaces": {
            "F": {"degree": 66, "nonstrict_dimension": 181, "strict_face_kernel_dimension": 146, "start_histogram": hist_f},
            "G": {"degree": 99, "nonstrict_dimension": 388, "strict_face_kernel_dimension": 336, "start_histogram": hist_g},
            "T2": {"degree": 55, "nonstrict_dimension": 129, "strict_face_kernel_dimension": 100, "start_histogram": start_histogram(t2space)},
            "T3": {"degree": 145, "nonstrict_dimension": 816, "strict_face_kernel_dimension": 740, "start_histogram": start_histogram(t3space)},
            "basis_formula": "X^(D-i-k-v1)*Y^k*(Y-X)^v1 -> x^n*z^k*(1-x^3*z)^v1",
        },
        "bands": [
            {
                "band": 0,
                "data": "f0=H^6, g0=H^9",
                "raw_rows": 0,
                "consistent": True,
                "fiber_dimension_over_Q(a)": 0,
                "total_dimension_including_a": 1,
                "note": "a remains symbolic and is localized; later fiber dimensions exclude a",
            },
            {
                "band": 1,
                "new_unknowns": 43,
                "unknown_split": {"f1_deg_0_16": 17, "g1_deg_0_25": 26},
                "ambient_z_coefficient_slots_deg_0_42": 43,
                "raw_nonzero_z_coefficient_rows": 32,
                "raw_exponent_range": "z^11,...,z^42",
                "H5_quotient_nonzero_rows": 27,
                "quotient_exponent_range": "z^1,...,z^27",
                "rank": 26,
                "pivots": 26,
                "pivot_coefficient": "-2 (the g1 coefficients in q1=3*H^3*f1-2*g1)",
                "solution": "g1=(3/2)*H^3*f1",
                "cumulative_fiber_dimension_over_Q(a)": 17,
                "cumulative_total_dimension_including_a": 18,
            },
            {
                "band": 2,
                "new_unknowns": 41,
                "unknown_split": {"f2_deg_0_15": 16, "g2_deg_0_24": 25},
                "raw_nonzero_z_rows_before_compatibility": 36,
                "raw_exponent_range_before_compatibility": "z^5,...,z^40",
                "raw_nonzero_z_rows_after_compatibility": 30,
                "H5_quotient_nonzero_rows_after_consistency": 25,
                "quotient_exponent_range": "z^1,...,z^25",
                "new_variable_rank": 24,
                "new_variable_pivots": 24,
                "old_parameter_conditions": 5,
                "condition": "H^3 divides f1^2; on a!=0 equivalently D=z^3*(z+3a)^2 divides f1",
                "parameterization": "f1=D*U, deg(U)<=11; q2=3H^3f2-2g2=-(3/4)f1^2/H^3+b2H^8",
                "new_kernel_dimension": 17,
                "cumulative_fiber_dimension_over_Q(a)": 29,
                "cumulative_total_dimension_including_a": 30,
            },
            {
                "band": 3,
                "new_unknowns": 39,
                "unknown_split": {"f3_new_deg_0_14": 15, "g3_new_deg_0_23": 24},
                "new_variable_rank": 24,
                "new_variable_pivots": 24,
                "raw_nonzero_z_rows_after_compatibility": 30,
                "H5_quotient_nonzero_rows_after_consistency": 25,
                "quotient_exponent_range": "z^1,...,z^25",
                "additional_old_parameter_conditions": 4,
                "condition": "H^3 divides f1 (upgrade from D|f1)",
                "parameterization": "f1=H^3*U, deg(U)<=7; q3=-(3/2)U*f2+(1/8)U^3+(4/3)b2H^5U",
                "new_kernel_dimension": 15,
                "cumulative_fiber_dimension_over_Q(a)": 40,
                "cumulative_total_dimension_including_a": 41,
            },
            {
                "band": 4,
                "new_unknowns": 37,
                "unknown_split": {"f4_new_deg_0_13": 14, "g4_new_deg_0_22": 23},
                "fixed_inverse_Omega_tails": "tail_f4=-sum_k v1F(k)[z^k]f1*z^(k+1); likewise g",
                "raw_nonzero_z_rows_after_compatibility": 29,
                "H5_quotient_nonzero_rows_after_consistency": 24,
                "quotient_exponent_range": "z^1,...,z^24",
                "new_variable_rank": 22,
                "new_variable_pivots": 22,
                "old_parameter_conditions": 5,
                "condition": "D divides 4*f2-U^2 (five coefficient equations over Q(a))",
                "parameterization": "f2=(U^2+D*V)/4, deg(V)<=10; q4 is the displayed particular solution plus b4*H^7",
                "new_kernel_dimension": 15,
                "cumulative_fiber_dimension_over_Q(a)": 50,
                "cumulative_total_dimension_including_a": 51,
            },
        ],
        "band_4_certificate": {
            "fixed_inverse_Omega_tails": "tail_f4=-sum_k v1F(k)[z^k]f1*z^(k+1); likewise g; exact v1 arrays below",
            "v1F_band1": [row["v1"] for row in band1_f],
            "v1G_band1": [row["v1"] for row in band1_g],
            "equation": "E4=sum_{r+s=4}((18-s)f_r'g_s+(r-12)f_rg_s')=0",
            "q4_formula": q4_formula_text,
            "consistency_condition": "D divides 4*f2-U^2 (5 coefficient equations, a localized)",
            "consistency_remainder_definition": "band4_remainder_coefficients=[z^k] rem_z(4*f2-U^2,D), k=0,...,4",
            "band4_remainder_coefficients": [str(value) for value in band4_remainders],
            "equivalent_exact_parameterization": "f2=(U^2+D*(w0+w1*z+...+w10*z^10))/4",
            "after_condition": "q4-q4_tail has degree <=22; g4_new=(3*H^3*f4_new-(q4-q4_tail))/2 is allowed; operator rank 22; one H^7 resonance plus 14 common f4 directions",
        },
        "next_band_5": {
            "new_unknowns": 35,
            "unknown_split": {"f5_new_deg_0_12": 13, "g5_new_deg_0_21": 22},
            "fixed_inverse_Omega_tails": "tail_f5=-sum_k v1F_band2(k)[z^k]f2*z^(k+1); likewise g2",
            "v1F_band2": [row["v1"] for row in band2_f],
            "v1G_band2": [row["v1"] for row in band2_g],
            "equation": "E5=sum_{r+s=5}((18-s)f_r'g_s+(r-12)f_rg_s')=0",
            "q5_formula": q5_formula_text,
            "consistency_condition": "M5 divides N5 (eight exact remainder coefficient equations)",
            "M5": "z^6*(z+3*a)^2",
            "N5": "243*U*V^2-3888*z^3*(z+3*a)*V*f3+640*b2*z^4*(z+3*a)*U^3",
            "consistency_remainder_definition": "band5_remainder_coefficients=[z^k] rem_z(N5,M5), k=0,...,7",
            "band5_remainder_coefficients": [str(value) for value in band5_remainders],
            "after_condition": "q5-q5_tail is polynomial of degree <=21; the apparent degrees 22,...,25 cancel identically",
            "new_variable_rank": 22,
            "new_variable_pivots": 22,
            "new_kernel_dimension_before_old_conditions": 13,
            "raw_nonzero_z_rows_after_consistency": 28,
            "H5_quotient_nonzero_rows_after_consistency": 23,
            "quotient_exponent_range": "z^1,...,z^23",
            "status": "UNSOLVED exact next band; no dimension is asserted after its eight nonlinear old-parameter equations",
        },
        "warnings": [
            "a0,a1 and Moh's simultaneous k<<x^-1>>/k<<y^-1>> gauge map are omitted by the source; zero-jet straightening is not proved filtration/polynomiality preserving",
            "nonempty bands are COUNTING-BOUND only",
            "the full Jacobian constant first appears at band 31",
        ],
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    print("output_sha256=" + hashlib.sha256(OUT.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
