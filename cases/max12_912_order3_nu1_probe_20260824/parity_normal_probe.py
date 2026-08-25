#!/usr/bin/env python3
"""Exact normal-Jacobian probe along the order-three parity locus.

This is producer-internal scratch, deliberately outside every frozen parity
manifest.  The involution sends ``f(z)`` to ``-f(-z)``.  Its fixed locus has
``a_0=a_2=a_4=a_6=0``; the anti-invariant tail equations are
``r_1=r_3=r_5=r_7=0``.  We compute their exact 4-by-4 normal Jacobian and
specialize the invariant coefficients to

    f=(z^3+p*z)^3+x5*z^5+x3*z^3+x1*z.

No fibre equation is divided out and no trajectory conclusion is made.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations
from pathlib import Path
import importlib.util
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[2]
PARENT = ROOT / "cases/max12_912_order3_fibre_20260824/order3_fibre.py"
GENUS_REPLAY = (
    ROOT / "cases/max12_912_order3_nu_parity_genus5_20260824/replay.py"
)


def load_parent():
    spec = importlib.util.spec_from_file_location("max12_parity_normal_parent", PARENT)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load parent")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def load_genus_replay():
    spec = importlib.util.spec_from_file_location(
        "max12_parity_normal_genus_replay", GENUS_REPLAY
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load genus-five replay")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


P = load_parent()
G = load_genus_replay()
M = P.M


def determinant(matrix, ring):
    size = len(matrix)
    out = {}
    for perm in permutations(range(size)):
        inversions = sum(
            1 for i in range(size) for j in range(i + 1, size)
            if perm[i] > perm[j]
        )
        term = ring.one
        for row, column in enumerate(perm):
            term = M.cmul(term, matrix[row][column])
        out = M.cadd(out, M.cscale(-1 if inversions % 2 else 1, term))
    return out


def to_singular(value, names):
    """Render an exact sparse polynomial without any CAS dependency."""
    if not value:
        return "0"
    terms = []
    for monomial in sorted(value, reverse=True):
        coefficient = value[monomial]
        factors = []
        if coefficient.denominator == 1:
            factors.append(str(abs(coefficient.numerator)))
        else:
            factors.append(
                f"({abs(coefficient.numerator)}/{coefficient.denominator})"
            )
        for name, exponent in zip(names, monomial):
            if exponent == 1:
                factors.append(name)
            elif exponent:
                factors.append(f"{name}^{exponent}")
        term = "*".join(factors)
        if coefficient < 0:
            terms.append("-" + term)
        else:
            terms.append("+" + term)
    return "".join(terms).lstrip("+")


def singular_factor(expressions, names):
    """Factor exact expressions in Singular, communicating only via stdin."""
    commands = [f"ring R=0,({','.join(names)}),dp;"]
    for label, expression in expressions:
        commands.extend(
            [
                f"poly {label}={expression};",
                f'print("{label}_expanded="+string({label}));',
                f'print("{label}_factor="+string(factorize({label},1)));',
            ]
        )
    commands.append("exit;")
    result = subprocess.run(
        ["/opt/homebrew/bin/Singular", "-q"],
        input="\n".join(commands),
        text=True,
        capture_output=True,
        check=True,
    )
    if result.stderr:
        raise RuntimeError(result.stderr)
    return result.stdout


def univariate_string(poly, name="v"):
    """Render increasing-degree Fraction tuple for Singular."""
    value = {
        (exponent,): coefficient
        for exponent, coefficient in enumerate(poly)
        if coefficient
    }
    return to_singular(value, (name,))


def evaluate_rat(value, bases):
    total = G.Rat.constant(0)
    for monomial, coefficient in value.items():
        term = G.Rat.constant(coefficient)
        for exponent, base in zip(monomial, bases):
            term = term * (base ** exponent)
        total = total + term
    return total


def main() -> None:
    compiled = P.compile_fibre()
    tails = compiled["tails"]
    target = M.Ring(["p", "x1", "x3", "x5"])
    p = target.var("p")
    x1 = target.var("x1")
    x3 = target.var("x3")
    x5 = target.var("x5")

    zero = {}
    images = [
        zero,
        x1,
        zero,
        M.cadd(M.cmul(M.cmul(p, p), p), x3),
        zero,
        M.cadd(M.cscale(3, M.cmul(p, p)), x5),
        zero,
        M.cscale(3, p),
        zero,  # k=0
    ]

    odd_rows = (1, 3, 5, 7)
    even_columns = (0, 2, 4, 6)
    matrix = []
    for ell in odd_rows:
        row = []
        for column in even_columns:
            derivative = M.cpartial(tails[ell], column)
            row.append(P.substitute_coeff(derivative, images, target))
        matrix.append(row)

    det = determinant(matrix, target)
    print("normal_rows=r1,r3,r5,r7")
    print("normal_columns=a0,a2,a4,a6")
    expressions = [("nrm", to_singular(det, target.names))]
    for ell in (2, 4, 6, 8):
        specialized = P.substitute_coeff(tails[ell], images, target)
        expressions.append((f"r{ell}", to_singular(specialized, target.names)))
    print(singular_factor(expressions, target.names), end="")

    # Reduce the normal determinant on the exact generic parity chart used by
    # the frozen genus-five replay.  The determinant has divided weight 20;
    # setting p=1 extracts its weight-zero quotient N(v) from det=p^20*N(v).
    v = G.Rat((Fraction(0), Fraction(1)))
    D = G.Rat((Fraction(-2), Fraction(0), Fraction(3)))
    A2 = G.Rat((Fraction(1), Fraction(3), Fraction(3)))
    x5hat = G.Rat.constant(-36) * (v ** 2) * A2 / D
    x3hat = x5hat * (v + G.Rat.constant(2))
    x1hat = (
        x5hat * (v + G.Rat.constant(1))
        + (x5hat ** 2) * G.Rat.constant(Fraction(1, 3))
        / (G.Rat.constant(9) * v)
    )
    quotient = G.evaluate_weighted(
        det,
        [G.Rat.constant(1), x1hat, x3hat, x5hat],
        [1, 4, 3, 2],
        20,
    )
    common = G.pgcd(quotient.numerator, quotient.denominator)
    quotient_numerator, numerator_remainder = G.pdivmod(
        quotient.numerator, common
    )
    quotient_denominator, denominator_remainder = G.pdivmod(
        quotient.denominator, common
    )
    assert numerator_remainder == (Fraction(0),)
    assert denominator_remainder == (Fraction(0),)
    Q12 = (
        Fraction(480), Fraction(4688), Fraction(8664), Fraction(4608),
        Fraction(111060), Fraction(391932), Fraction(-503280),
        Fraction(-5322618), Fraction(-12251574), Fraction(-12217797),
        Fraction(-2488077), Fraction(4809213), Fraction(2893401),
    )
    vpoly = (Fraction(0), Fraction(1))
    A2poly = (Fraction(1), Fraction(3), Fraction(3))
    Dpoly = (Fraction(-2), Fraction(0), Fraction(3))
    expected_numerator = G.pmul(
        G.ppow(vpoly, 14), G.pmul(G.ppow(A2poly, 7), Q12)
    )
    expected_denominator = G.ppow(Dpoly, 10)
    numerator_constant, numerator_check = G.pdivmod(
        quotient_numerator, expected_numerator
    )
    denominator_constant, denominator_check = G.pdivmod(
        quotient_denominator, expected_denominator
    )
    assert numerator_check == (Fraction(0),)
    assert denominator_check == (Fraction(0),)
    assert len(numerator_constant) == len(denominator_constant) == 1
    scalar = numerator_constant[0] / denominator_constant[0]
    A5poly = (
        Fraction(2), Fraction(18), Fraction(69), Fraction(131),
        Fraction(117), Fraction(33),
    )
    assert G.pgcd(Q12, G.derivative(Q12)) == (Fraction(1),)
    assert G.pgcd(Q12, A5poly) == (Fraction(1),)
    assert G.pgcd(Q12, A2poly) == (Fraction(1),)
    assert G.pgcd(Q12, Dpoly) == (Fraction(1),)
    print("generic_identity=det=p^20*N(v)")
    print(
        "N(v)="
        f"({scalar})*v^14*(3*v^2+3*v+1)^7*Q12(v)/(3*v^2-2)^10"
    )
    print("Q12_squarefree_and_coprime_to_A5_A2_D=PASS")

    # Exact corank controls at Q12.  A single 3-by-3 normal minor coprime to
    # Q12 proves rank(J_N)=3 at every Q12 root.  A 3-by-3 invariant minor in
    # d(r2,r4,r6)/d(p,x1,x3,x5) proves that the loaded parity curve is smooth.
    chart_bases = [G.Rat.constant(1), x1hat, x3hat, x5hat]
    one = (Fraction(1),)
    normal_minor_certificate = None
    for omitted_row in range(4):
        for omitted_column in range(4):
            minor_matrix = [
                [
                    matrix[row][column]
                    for column in range(4)
                    if column != omitted_column
                ]
                for row in range(4)
                if row != omitted_row
            ]
            minor = determinant(minor_matrix, target)
            minor_hat = evaluate_rat(minor, chart_bases)
            if G.pgcd(minor_hat.numerator, Q12) == one:
                normal_minor_certificate = (omitted_row, omitted_column)
                break
        if normal_minor_certificate is not None:
            break
    assert normal_minor_certificate is not None

    parity_tails = {
        ell: P.substitute_coeff(tails[ell], images, target)
        for ell in (2, 4, 6)
    }
    invariant_matrix = [
        [M.cpartial(parity_tails[ell], column) for column in range(4)]
        for ell in (2, 4, 6)
    ]
    invariant_minor_certificate = None
    for omitted_column in range(4):
        minor_matrix = [
            [
                invariant_matrix[row][column]
                for column in range(4)
                if column != omitted_column
            ]
            for row in range(3)
        ]
        minor = determinant(minor_matrix, target)
        minor_hat = evaluate_rat(minor, chart_bases)
        if G.pgcd(minor_hat.numerator, Q12) == one:
            invariant_minor_certificate = omitted_column
            break
    assert invariant_minor_certificate is not None
    R6numerator = G.pmul(
        G.ppow(vpoly, 6), G.pmul(G.ppow(A2poly, 3), A5poly)
    )
    R6derivative_numerator = G.padd(
        G.pmul(G.derivative(R6numerator), Dpoly),
        G.pscale(
            -4,
            G.pmul(R6numerator, G.derivative(Dpoly)),
        ),
    )
    assert G.pgcd(R6derivative_numerator, Q12) == one
    print(
        "Q12_normal_rank3_minor=omit_row_"
        f"{normal_minor_certificate[0]}_column_{normal_minor_certificate[1]}"
    )
    print(
        "Q12_invariant_rank3_minor=omit_column_"
        f"{invariant_minor_certificate}"
    )
    print("Q12_corank_and_smooth_fixed_curve=PASS")
    print("Q12_coprime_to_R6_derivative_numerator=PASS")
    print(
        singular_factor(
            [
                ("Nnum", univariate_string(quotient_numerator)),
                ("Nden", univariate_string(quotient_denominator)),
            ],
            ("v",),
        ),
        end="",
    )

    # Involution sanity: even tail equations have zero normal differential,
    # and odd tail equations vanish on the fixed locus.
    for ell in odd_rows:
        if P.substitute_coeff(tails[ell], images, target):
            raise RuntimeError(("odd tail does not vanish", ell))
    for ell in (2, 4, 6, 8):
        for column in even_columns:
            derivative = M.cpartial(tails[ell], column)
            if P.substitute_coeff(derivative, images, target):
                raise RuntimeError(("even tail has normal linear term", ell, column))

    # The approximate-cubic-to-original normal map is triangular with
    # nonzero rational determinant; using original a_even directions does
    # not lose a normal rank boundary.
    print("involution_sanity=PASS")


if __name__ == "__main__":
    main()
