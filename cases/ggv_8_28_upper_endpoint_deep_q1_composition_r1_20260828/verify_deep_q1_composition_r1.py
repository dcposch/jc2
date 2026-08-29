#!/usr/bin/env python3
"""Repaired exact q1 composition, window mutation, and D25/q3 gate.

This r1 checker explicitly rejects the false translation-as-raw-gauge step,
retains the lambda=0 face tangent calculation at its honest scope, and
verifies the constants and degree/divisibility mechanism in the D25 q3
collapse of the lambda=0 exact-D=0 branch.
"""

from __future__ import annotations

from fractions import Fraction as Q
import hashlib
import importlib.util
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
NEWTON = (
    ROOT
    / "cases/ggv_8_28_upper_endpoint_deep_newton_kernel_family_20260828"
    / "verify_deep_newton_kernel_family.py"
)
NEWTON_SHA256 = "0b873f2b4e0cdd4f55312dea6bf2d69d4fcbb3bb03c5725c082028148847c99f"
R0 = (
    ROOT
    / "cases/ggv_8_28_upper_endpoint_deep_q1_composition_20260828"
    / "verify_deep_q1_composition.py"
)
R0_SHA256 = "76785c37348a91128bf72b640c4c04130d0b567155e27c0e19a9237085cb0a3e"
TRANSLATION_AUDIT = (
    ROOT
    / "cases/ggv_8_28_upper_endpoint_q1_translation_gauge_audit_20260828"
    / "verify_translation_gauge.py"
)
TRANSLATION_AUDIT_SHA256 = "6a945dc4114a6480f3d344e4f83c9415e553d3b49ad93c260ad42c3acb8cd519"
Q3_REPORT = (
    ROOT
    / "xmodel/ggv-upper-endpoint-deep-q1-q3-composition-sol-ultra-20260828.md"
)
Q3_REPORT_SHA256 = "6958c3986022e28484ea1a0a15a0b09a562dbd94cc2154ade4fe6dbc35000715"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path: Path, expected: str, name: str):
    assert sha256(path) == expected
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def matrix_rank(matrix):
    rows = [list(row) for row in matrix]
    rank = 0
    columns = len(rows[0]) if rows else 0
    for column in range(columns):
        pivot = next((r for r in range(rank, len(rows)) if rows[r][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = rows[rank][column]
        rows[rank] = [value / scale for value in rows[rank]]
        for r in range(len(rows)):
            if r != rank and rows[r][column]:
                factor = rows[r][column]
                rows[r] = [a - factor * b for a, b in zip(rows[r], rows[rank])]
        rank += 1
        if rank == len(rows):
            break
    return rank


def coefficient(poly, degree):
    return poly[degree] if degree < len(poly) else Q(0)


def main():
    newton = load(NEWTON, NEWTON_SHA256, "deep_newton_r1_frozen")
    q1r0 = load(R0, R0_SHA256, "deep_q1_r0_frozen")
    # Pin the independent negative audit even though the two mutations below
    # are reconstructed without importing its implementation.
    assert sha256(TRANSLATION_AUDIT) == TRANSLATION_AUDIT_SHA256
    # Pin, but do not import or modify, the coordinator's frozen q3 derivation.
    # The polynomial computations below independently reconstruct its constants.
    assert sha256(Q3_REPORT) == Q3_REPORT_SHA256
    tail = newton.load_tail()
    up = tail.load_upstream()

    A = [Q(-1), Q(0), Q(0), Q(0), Q(1)]
    Aprime = up.p_derivative(A)

    # q1 active collapse, but no raw-gauge conclusion.
    lam = Q(4, 3)
    R0poly = up.p_scale(lam, A)
    V0 = up.p_add(
        up.p_mul(Aprime, R0poly),
        up.p_scale(2, up.p_mul(A, up.p_derivative(R0poly))),
    )
    assert V0 == up.p_scale(3 * lam, up.p_mul(A, Aprime))
    F0 = up.p_power(A, 4)
    F1 = up.p_mul(up.p_power(A, 3), up.p_scale(3 * lam, Aprime))
    shear = 3 * lam / 4
    assert shear == 1 and F1 == up.p_scale(shear, up.p_derivative(F0))

    # Exact lower-window counterexamples.  For tau_a P(X,t)=P(X-a t,t),
    # the weight-(n+1) contribution from P_n is -a P_n'.
    F8 = [Q(0), Q(1)]
    G12 = [Q(0), Q(1)]
    forbidden_F9 = up.p_scale(-shear, up.p_derivative(F8))
    forbidden_G13 = up.p_scale(-shear, up.p_derivative(G12))
    assert forbidden_F9 == [Q(-1)]
    assert forbidden_G13 == [Q(-1)]
    assert coefficient(forbidden_F9, 0) and coefficient(forbidden_G13, 0)

    # Retain the predecessor's face tangent strictly on lambda=0.  Rebuild
    # the ranks from its exact Jet face coefficients rather than invoking its
    # now-superseded main narrative.
    local_names, face = q1r0.face_rows(newton)
    local_index = {name: i for i, name in enumerate(local_names)}
    local_qef = [[jet.derivative[local_index[name]]
                  for name in ("q", "e", "f")] for jet in face]
    assert matrix_rank(local_qef[:4]) == 3
    assert matrix_rank([
        row + [Q(1) if index == 4 else Q(0)]
        for index, row in enumerate(local_qef)
    ]) == 4

    # D25/q3 constants on lambda=0.  The reviewed closed coefficient is
    # q3=p^5 F3/(4A^4) when F1=0.  Since F3=A^2 U/8 and p^4=A^2,
    # q3=p U/32 on either quadratic twist p^2=+/-A.
    U_test = [Q(2), Q(-3), Q(5)]
    F3_test = up.p_scale(Q(1, 8), up.p_mul(up.p_power(A, 2), U_test))
    q3_p_coefficient = up.p_scale(
        Q(1, 4), up.p_divmod(F3_test, up.p_power(A, 2))[0]
    )
    assert q3_p_coefficient == up.p_scale(Q(1, 32), U_test)

    # Exactness of q3 dX gives, for a rational c,
    #   4A^2 c' + 2AA'c = A^2 U/8.
    # After cancelling A and imposing the reviewed D12 lift A|U, solve the
    # complete degree windows deg c<=6 and U=A(u0+u1 X), deg U<=5.
    columns = []
    for degree in range(7):
        c = [Q(0)] * degree + [Q(1)]
        image = up.p_add(
            up.p_scale(4, up.p_mul(A, up.p_derivative(c))),
            up.p_scale(2, up.p_mul(Aprime, c)),
        )
        columns.append(image)
    for degree in range(2):
        ubar = [Q(0)] * degree + [Q(1)]
        U = up.p_mul(A, ubar)
        image = up.p_scale(Q(-1, 8), up.p_mul(A, U))
        columns.append(image)
    row_count = max(len(poly) for poly in columns)
    matrix = [
        [coefficient(poly, degree) for poly in columns]
        for degree in range(row_count)
    ]
    assert len(columns) == 9 and matrix_rank(matrix) == 9

    # Mutation: without A|U, q3 alone has a nonzero legal-degree solution.
    # c=A and U=48A' satisfy the equation exactly, so the D12 lift is
    # genuinely load-bearing.
    c_mutation = A
    U_mutation = up.p_scale(48, Aprime)
    lhs = up.p_add(
        up.p_scale(4, up.p_mul(up.p_power(A, 2), up.p_derivative(c_mutation))),
        up.p_scale(2, up.p_mul(up.p_mul(A, Aprime), c_mutation)),
    )
    rhs = up.p_scale(Q(1, 8), up.p_mul(up.p_power(A, 2), U_mutation))
    assert lhs == rhs
    _, remainder = up.p_divmod(U_mutation, A)
    assert remainder

    # Full lambda q3 composition.  With S=3lambda A' and
    # Z=(S^2-AQ)/2, the complete reviewed q3 numerator is
    # N=S^3+A(16U-2SQ).  Exactness is 2AC'+A'C=N (after harmless primitive
    # scaling).  D12 A|(QS+4U) fixes the degree<=2 remainder r and hence U.
    lam_general = Q(5, 7)
    Qpoly = [Q(2), Q(-3), Q(4)]
    Asecond = up.p_derivative(Aprime)
    Athird = up.p_derivative(Asecond)
    Sgeneral = up.p_scale(3 * lam_general, Aprime)
    Zgeneral = up.p_scale(Q(1, 2), up.p_add(
        up.p_mul(Sgeneral, Sgeneral),
        up.p_scale(-1, up.p_mul(A, Qpoly)),
    ))
    r_general = up.p_add(
        up.p_scale(-6 * lam_general, Qpoly),
        up.p_scale(-36 * lam_general ** 3, Asecond),
    )
    Ugeneral = up.p_add(
        up.p_scale(
            -3 * lam_general / 4,
            up.p_add(up.p_mul(Aprime, Qpoly), up.p_mul(A, up.p_derivative(Qpoly))),
        ),
        up.p_scale(-Q(9, 2) * lam_general ** 3, up.p_mul(A, Athird)),
    )
    Cgeneral = up.p_add(
        up.p_scale(27 * lam_general ** 3, up.p_mul(Aprime, Aprime)),
        up.p_mul(A, r_general),
    )
    Ngeneral = up.p_add(
        up.p_mul(up.p_mul(Sgeneral, Sgeneral), Sgeneral),
        up.p_mul(A, up.p_add(
            up.p_scale(16, Ugeneral),
            up.p_scale(-2, up.p_mul(Sgeneral, Qpoly)),
        )),
    )
    q3_direct_numerator = up.p_add(
        up.p_scale(16, up.p_add(
            up.p_mul(Sgeneral, Zgeneral), up.p_mul(A, Ugeneral)
        )),
        up.p_scale(-12, up.p_mul(
            Sgeneral,
            up.p_add(up.p_mul(Sgeneral, Sgeneral), Zgeneral),
        )),
        up.p_scale(11, up.p_mul(up.p_mul(Sgeneral, Sgeneral), Sgeneral)),
    )
    assert q3_direct_numerator == Ngeneral
    exactness_operator = up.p_add(
        up.p_scale(2, up.p_mul(A, up.p_derivative(Cgeneral))),
        up.p_mul(Aprime, Cgeneral),
    )
    assert exactness_operator == Ngeneral
    Lgeneral = up.p_add(up.p_mul(Qpoly, Sgeneral), up.p_scale(4, Ugeneral))
    expected_L = up.p_scale(
        -3 * lam_general,
        up.p_mul(A, up.p_add(
            up.p_derivative(Qpoly), up.p_scale(6 * lam_general ** 2, Athird)
        )),
    )
    assert Lgeneral == expected_L
    assert len(r_general) <= 3 and len(Cgeneral) <= 7 and len(Ugeneral) <= 6
    wrong_U = up.p_add(
        Ugeneral,
        up.p_scale(Q(1, 16), up.p_mul(A, Aprime)),
    )
    wrong_N = up.p_add(
        up.p_mul(up.p_mul(Sgeneral, Sgeneral), Sgeneral),
        up.p_mul(A, up.p_add(
            up.p_scale(16, wrong_U),
            up.p_scale(-2, up.p_mul(Sgeneral, Qpoly)),
        )),
    )
    assert exactness_operator != wrong_N

    print("translation_formal_symmetry=true;raw_window_gauge=false")
    print("forbidden_shear_slots=F9[X0],G13[X0]")
    print("lambda0_square_face_tangent_obstructed=true")
    print("q3_license_requires=D23_D24_D25")
    print("q3=p*U/32;primitive_gate=4A^2c_prime+2AA_prime*c=A^2U/8")
    print("D12_A_divides_U_plus_q3_implies=c=U=0")
    print("mutation_without_D12=c=A,U=48A_prime_survives")
    print("general_q3_numerator=S^3+A*(16U-2SQ)")
    print("general_D12_q3_U=-3lambda*(A_prime*Q+A*Q_prime)/4-9lambda^3*A*A_triple_prime/2")
    print("PASS_EXACT_DEEP_Q1_COMPOSITION_R1")


if __name__ == "__main__":
    main()
