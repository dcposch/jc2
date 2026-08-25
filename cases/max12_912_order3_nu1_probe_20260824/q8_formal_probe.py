#!/usr/bin/env python3
"""Fresh producer-internal rank/transversality probe at Q8.

This scratch computation consumes only the Faber compiler, reviewed parity
chart, and frozen Q8 erratum.  It imports no conclusion from the quarantined
Q12 branch artifacts.
"""

from __future__ import annotations

from fractions import Fraction
import importlib.util
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]


def load(name, relative):
    path = ROOT / relative
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


P = load("q8_formal_parent", "cases/max12_912_order3_fibre_20260824/order3_fibre.py")
G = load("q8_formal_genus", "cases/max12_912_order3_nu_parity_genus5_20260824/replay.py")
E = load("q8_formal_erratum", "cases/max12_912_order3_nu_parity_normal_q8_erratum_20260824/replay.py")
M = P.M


def main():
    compiled = P.compile_fibre()
    tails = compiled["tails"]
    ring = M.Ring(["p", "x1", "x3", "x5"])
    p = ring.var("p")
    x1 = ring.var("x1")
    x3 = ring.var("x3")
    x5 = ring.var("x5")
    zero = {}
    images = [
        zero, x1, zero,
        M.cadd(M.cmul(M.cmul(p, p), p), x3),
        zero, M.cadd(M.cscale(3, M.cmul(p, p)), x5),
        zero, M.cscale(3, p), zero,
    ]
    normals = (0, 2, 4, 6)
    normal_matrix = [
        [
            P.substitute_coeff(M.cpartial(tails[ell], column), images, ring)
            for column in normals
        ]
        for ell in (1, 3, 5, 7)
    ]
    parity_tails = {
        ell: P.substitute_coeff(tails[ell], images, ring)
        for ell in (2, 4, 6)
    }
    invariant_matrix = [
        [M.cpartial(parity_tails[ell], column) for column in range(4)]
        for ell in (2, 4, 6)
    ]

    vpoly = (Fraction(0), Fraction(1))
    Dpoly = (Fraction(-2), Fraction(0), Fraction(3))
    A2poly = (Fraction(1), Fraction(3), Fraction(3))
    A5poly = (
        Fraction(2), Fraction(18), Fraction(69), Fraction(131),
        Fraction(117), Fraction(33),
    )
    Q8poly = (
        Fraction(24), Fraction(296), Fraction(1548), Fraction(4428),
        Fraction(7320), Fraction(6498), Fraction(1782), Fraction(-1539),
        Fraction(-999),
    )
    v = G.Rat(vpoly)
    D = G.Rat(Dpoly)
    A2 = G.Rat(A2poly)
    x5hat = G.Rat.constant(-36) * (v ** 2) * A2 / D
    x3hat = x5hat * (v + G.Rat.constant(2))
    x1hat = (
        x5hat * (v + G.Rat.constant(1))
        + (x5hat ** 2) * G.Rat((Fraction(1), Fraction(3)))
        / (G.Rat.constant(9) * v)
    )
    chart_bases = [G.Rat.constant(1), x1hat, x3hat, x5hat]
    one = (Fraction(1),)

    normal_certificate = None
    for omitted_row in range(4):
        for omitted_column in range(4):
            minor_matrix = [
                [
                    normal_matrix[row][column]
                    for column in range(4)
                    if column != omitted_column
                ]
                for row in range(4)
                if row != omitted_row
            ]
            minor = E.sparse_determinant(minor_matrix, M, ring)
            value = E.evaluate_rat(minor, chart_bases, G)
            if (
                G.pgcd(value.numerator, Q8poly) == one
                and G.pgcd(value.denominator, Q8poly) == one
            ):
                normal_certificate = (omitted_row, omitted_column)
                break
        if normal_certificate is not None:
            break
    assert normal_certificate is not None

    invariant_certificate = None
    for omitted_column in range(4):
        minor_matrix = [
            [
                invariant_matrix[row][column]
                for column in range(4)
                if column != omitted_column
            ]
            for row in range(3)
        ]
        minor = E.sparse_determinant(minor_matrix, M, ring)
        value = E.evaluate_rat(minor, chart_bases, G)
        if (
            G.pgcd(value.numerator, Q8poly) == one
            and G.pgcd(value.denominator, Q8poly) == one
        ):
            invariant_certificate = omitted_column
            break
    assert invariant_certificate is not None

    r6_numerator = G.pmul(
        G.ppow(vpoly, 6), G.pmul(G.ppow(A2poly, 3), A5poly)
    )
    r6_derivative_numerator = G.padd(
        G.pmul(G.derivative(r6_numerator), Dpoly),
        G.pscale(
            -4, G.pmul(r6_numerator, G.derivative(Dpoly))
        ),
    )
    assert G.pgcd(Q8poly, G.derivative(Q8poly)) == one
    assert G.pgcd(Q8poly, r6_derivative_numerator) == one

    print(
        "normal_rank3=omit_row_"
        f"{normal_certificate[0]}_column_{normal_certificate[1]}"
    )
    print(f"invariant_rank3=omit_column_{invariant_certificate}")
    print("gcd_Q8_R6prime_numerator=1")
    print("fresh_Q8_formal_hypotheses=PASS")


if __name__ == "__main__":
    main()
