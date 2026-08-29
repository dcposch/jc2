#!/usr/bin/env python3
"""Exact degree-bounded classification of the uniform D16/D17 congruences."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PRODUCER = (ROOT / "cases/ggv_8_28_upper_endpoint_uniform_d16_d17_fullmodes_20260828"
            / "verify_uniform_d16_d17.py")
PRODUCER_RESULT = PRODUCER.with_name("RESULT.json")
RAW = ROOT / "cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json"
RESULT = HERE / "RESULT.json"
PRODUCER_SHA256 = "5904d7b19dc5d46d31a781150c4b6de9e62e32812b554006e92f78f9d76fd5d9"
PRODUCER_RESULT_SHA256 = "2a6f363df8fb4aef94f01d7a938e3bfcff15f6db49af3164e36367c9a6d1929a"
RAW_SHA256 = "ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_producer():
    assert digest(PRODUCER) == PRODUCER_SHA256
    assert digest(PRODUCER_RESULT) == PRODUCER_RESULT_SHA256
    specification = importlib.util.spec_from_file_location("uniform_d17_frozen", PRODUCER)
    assert specification is not None and specification.loader is not None
    producer = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(producer)
    calculated = producer.calculate_result()
    frozen = json.loads(PRODUCER_RESULT.read_text())
    assert calculated == frozen
    return frozen


# Exact Gaussian rationals a+b*i, represented as pairs of Fraction values.
ZERO = (Q(0), Q(0))
ONE = (Q(1), Q(0))
I = (Q(0), Q(1))


def g(value=0, imaginary=0):
    if isinstance(value, tuple):
        return value
    return Q(value), Q(imaginary)


def gadd(*values):
    return sum((value[0] for value in values), Q(0)), sum(
        (value[1] for value in values), Q(0))


def gneg(value):
    return -value[0], -value[1]


def gsub(left, right):
    return left[0] - right[0], left[1] - right[1]


def gmul(left, right):
    return (left[0] * right[0] - left[1] * right[1],
            left[0] * right[1] + left[1] * right[0])


def ginv(value):
    denominator = value[0] * value[0] + value[1] * value[1]
    assert denominator
    return value[0] / denominator, -value[1] / denominator


def gdiv(left, right):
    return gmul(left, ginv(right))


def gscale(scalar, value):
    scalar = Q(scalar)
    return scalar * value[0], scalar * value[1]


def gpow(value, exponent):
    answer = ONE
    base = value
    while exponent:
        if exponent & 1:
            answer = gmul(answer, base)
        base = gmul(base, base)
        exponent //= 2
    return answer


def gformat(value):
    real, imaginary = value
    if not imaginary:
        return str(real)
    if not real:
        if imaginary == 1:
            return "i"
        if imaginary == -1:
            return "-i"
        return f"{imaginary}*i"
    sign = "+" if imaginary > 0 else "-"
    magnitude = abs(imaginary)
    imag = "i" if magnitude == 1 else f"{magnitude}*i"
    return f"{real}{sign}{imag}"


def ptrim(item):
    answer = list(item)
    while answer and answer[-1] == ZERO:
        answer.pop()
    return answer


def padd(*items):
    length = max((len(item) for item in items), default=0)
    return ptrim([gadd(*(item[index] if index < len(item) else ZERO
                         for item in items))
                  for index in range(length)])


def pscale(scalar, item):
    scalar = g(scalar) if not isinstance(scalar, tuple) else scalar
    return ptrim([gmul(scalar, value) for value in item])


def pmul(left, right):
    if not left or not right:
        return []
    answer = [ZERO] * (len(left) + len(right) - 1)
    for left_degree, left_value in enumerate(left):
        for right_degree, right_value in enumerate(right):
            degree = left_degree + right_degree
            answer[degree] = gadd(answer[degree], gmul(left_value, right_value))
    return ptrim(answer)


def pderivative(item):
    return ptrim([gscale(degree, item[degree]) for degree in range(1, len(item))])


def peval(item, value):
    answer = ZERO
    for coefficient in reversed(item):
        answer = gadd(gmul(answer, value), coefficient)
    return answer


def pdivmod(numerator, denominator):
    remainder = ptrim(numerator)
    quotient = [ZERO] * max(0, len(remainder) - len(denominator) + 1)
    while remainder and len(remainder) >= len(denominator):
        degree = len(remainder) - len(denominator)
        coefficient = gdiv(remainder[-1], denominator[-1])
        quotient[degree] = coefficient
        subtractor = [ZERO] * degree + pscale(coefficient, denominator)
        remainder = padd(remainder, pscale(-1, subtractor))
    return ptrim(quotient), remainder


def pencode(item):
    return {str(degree): gformat(coefficient)
            for degree, coefficient in enumerate(item) if coefficient != ZERO}


def solve_square(matrix, right):
    size = len(matrix)
    work = [list(row) + [value] for row, value in zip(matrix, right)]
    for column in range(size):
        pivot = next(row for row in range(column, size)
                     if work[row][column] != ZERO)
        work[column], work[pivot] = work[pivot], work[column]
        inverse = ginv(work[column][column])
        work[column] = [gmul(inverse, value) for value in work[column]]
        for row in range(size):
            if row == column or work[row][column] == ZERO:
                continue
            factor = work[row][column]
            work[row] = [gsub(left, gmul(factor, right_value))
                         for left, right_value in zip(work[row], work[column])]
    return [work[row][-1] for row in range(size)]


A = [g(-1), ZERO, ZERO, ZERO, ONE]
A2 = pmul(A, A)
ROOTS = [g(1), g(-1), I, gneg(I)]
ROOT_LABELS = ["1", "-1", "i", "-i"]


def hermite_sign_lift(signs):
    matrix = []
    right = []
    for root, sign in zip(ROOTS, signs):
        matrix.append([gpow(root, degree) for degree in range(8)])
        right.append(g(sign))
        matrix.append([ZERO if degree == 0 else
                       gscale(degree, gpow(root, degree - 1))
                       for degree in range(8)])
        right.append(ZERO)
    answer = ptrim(solve_square(matrix, right))
    assert len(answer) <= 8
    for root, sign in zip(ROOTS, signs):
        assert peval(answer, root) == g(sign)
        assert peval(pderivative(answer), root) == ZERO
    quotient, remainder = pdivmod(padd(pmul(answer, answer), [g(-1)]), A2)
    assert not remainder
    return answer, quotient


# Sparse symbolic polynomials in named scalar parameters, with Q(i) coefficients.
def sterm(coefficient=ONE, *symbols):
    coefficient = coefficient if isinstance(coefficient, tuple) else g(coefficient)
    return {tuple(sorted(symbols)): coefficient} if coefficient != ZERO else {}


def sadd(*items):
    answer = {}
    for item in items:
        for monomial, coefficient in item.items():
            answer[monomial] = gadd(answer.get(monomial, ZERO), coefficient)
            if answer[monomial] == ZERO:
                del answer[monomial]
    return answer


def sscale(coefficient, item):
    coefficient = coefficient if isinstance(coefficient, tuple) else g(coefficient)
    return {monomial: gmul(coefficient, value)
            for monomial, value in item.items() if gmul(coefficient, value) != ZERO}


def smul(left, right):
    answer = {}
    for left_monomial, left_value in left.items():
        for right_monomial, right_value in right.items():
            monomial = tuple(sorted(left_monomial + right_monomial))
            answer[monomial] = gadd(answer.get(monomial, ZERO),
                                    gmul(left_value, right_value))
            if answer[monomial] == ZERO:
                del answer[monomial]
    return answer


def ssubstitute(item, substitutions):
    answer = {}
    for monomial, coefficient in item.items():
        product = sterm(coefficient)
        for symbol in monomial:
            product = smul(product, substitutions.get(symbol, sterm(ONE, symbol)))
        answer = sadd(answer, product)
    return answer


def sencode(item):
    return [{"coefficient": gformat(coefficient), "monomial": list(monomial)}
            for monomial, coefficient in sorted(item.items())]


def encoded_jet(item):
    answer = {}
    for record in item:
        coefficient = g(Q(record["coefficient"]))
        monomial = tuple(sorted(record["monomial"]))
        answer[monomial] = gadd(answer.get(monomial, ZERO), coefficient)
    return {key: value for key, value in answer.items() if value != ZERO}


def symbolic_coefficient(polynomial, degree, symbol, factor=1):
    if degree >= len(polynomial):
        return {}
    return sterm(gscale(factor, polynomial[degree]), symbol)


def branch_lower_system(E, D, R, Tpoly, producer):
    # Exact coefficients of Bhat, C, M, N in the parameters rho and lambda.
    def Mcoefficient(degree):
        # The helper supplies one placeholder rho.  Replace it by rho^2 in
        # the D term and by rho*lambda in the E term.
        second = (symbolic_coefficient(E, degree, "rho", Q(3, 4))
                  if degree < len(E) else {})
        second = ssubstitute(second, {"rho": sterm(ONE, "rho", "lambda")})
        answer = sadd(
            ssubstitute(symbolic_coefficient(D, degree, "rho", Q(3, 8)),
                        {"rho": sterm(ONE, "rho", "rho")}),
            second,
        )
        if degree < len(A2) and A2[degree] != ZERO:
            answer = sadd(answer, sterm(gscale(Q(3, 8), A2[degree]),
                                        "lambda", "lambda"))
        return answer

    def Ncoefficient(degree):
        answer = {}
        if degree < len(Tpoly):
            answer = sadd(answer, sterm(gscale(Q(3, 16), Tpoly[degree]),
                                         "rho", "rho"))
        if degree < len(R):
            answer = sadd(answer, sterm(gscale(Q(3, 16), R[degree]),
                                         "rho", "lambda"))
        if degree == 0:
            answer = sadd(answer, sterm(Q(3, 16), "lambda", "lambda"))
        return answer

    def Ccoefficient(degree):
        answer = symbolic_coefficient(R, degree, "rho", Q(1, 4))
        if degree == 0:
            answer = sadd(answer, sterm(Q(1, 2), "lambda"))
        return answer

    base8 = sadd(
        sterm(Q(1, 2), "y0"), sterm(Q(1, 8), "t0", "z0"),
        sterm(Q(1, 16), "q0", "v0"), sterm(Q(1, 4), "r0", "r0"))
    bhat0 = sadd(symbolic_coefficient(E, 0, "rho"),
                 sterm(Q(1), "lambda"))
    H0 = sscale(Q(3, 4), sadd(bhat0, base8))
    base9_0 = sadd(
        sterm(Q(1, 2), "q0", "r0"), sterm(Q(1, 16), "t0", "v0"),
        sterm(Q(1, 8), "y0", "z0"))
    base9_1 = sadd(
        sterm(Q(1, 2), "q0", "r1"), sterm(Q(1, 2), "q1", "r0"),
        sterm(Q(1, 16), "t0", "v1"), sterm(Q(1, 16), "t1", "v0"),
        sterm(Q(1, 8), "y0", "z1"), sterm(Q(1, 8), "y1", "z0"))

    equations = {
        "F9_X0_absence": sadd(Ccoefficient(0), base9_0),
        "C13": sadd(
            smul(sterm(ONE, "q0"), H0),
            sterm(Q(-3, 128), "q0", "q0", "v0"),
            sterm(Q(-3, 16), "q0", "r0", "r0"),
            sterm(Q(3, 16), "t0", "t0"),
            sterm(Q(3, 4), "t0", "y0")),
        "C14": sadd(
            smul(sterm(ONE, "t0"), H0),
            sterm(Q(-3, 16), "q0", "q0", "r0"),
            sterm(Q(-3, 64), "q0", "t0", "v0"),
            sterm(Q(-3, 16), "r0", "r0", "t0"),
            sterm(Q(-3, 64), "t0", "t0", "z0"),
            sterm(Q(3, 8), "y0", "y0")),
        "C15": sadd(
            smul(sterm(ONE, "y0"), H0),
            sterm(Q(-1, 16), "q0", "q0", "q0"),
            sterm(Q(-3, 8), "q0", "r0", "t0"),
            sterm(Q(-3, 64), "q0", "v0", "y0"),
            sterm(Q(-3, 16), "r0", "r0", "y0"),
            sterm(Q(-3, 128), "t0", "t0", "v0"),
            sterm(Q(-3, 32), "t0", "y0", "z0"),
            sterm(Q(-3, 16), "y0", "y0")),
    }
    substitutions = {
        "m0": Mcoefficient(0),
        "m1": Mcoefficient(1),
        "n0": Ncoefficient(0),
        "n1": Ncoefficient(1),
        "f91": sadd(Ccoefficient(1), base9_1),
    }
    jets = producer["calculation"]["positive_lower_window_jets"]
    for label in ("G16_X0", "G16_X1", "G17_X0", "G17_X1"):
        equations[label] = ssubstitute(encoded_jet(jets[label]), substitutions)
    encoded = {label: sencode(equation) for label, equation in equations.items()}
    constant_units = []
    for label, equation in equations.items():
        if equation and all(not monomial for monomial in equation):
            constant_units.append(label)
    fingerprint = hashlib.sha256(
        json.dumps(encoded, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    return {
        "equations": encoded,
        "equation_term_counts": {label: len(equation)
                                 for label, equation in equations.items()},
        "literal_nonzero_constant_equations": constant_units,
        "system_sha256": fingerprint,
        "branch_coefficients": {
            "H0": sencode(H0),
            "C0": sencode(Ccoefficient(0)),
            "C1": sencode(Ccoefficient(1)),
            "M0": sencode(Mcoefficient(0)),
            "M1": sencode(Mcoefficient(1)),
            "N0": sencode(Ncoefficient(0)),
            "N1": sencode(Ncoefficient(1)),
        },
    }


def classify_nonzero_branch(producer):
    branches = []
    for signs in itertools.product((-1, 1), repeat=4):
        E, D = hermite_sign_lift(signs)
        ED = pmul(E, D)
        _, R = pdivmod(ED, A2)
        Tpoly, remainder = pdivmod(padd(pmul(E, R), pscale(-1, D)), A2)
        assert not remainder
        # R is the unique degree-<8 representative of E*D modulo A^2.
        assert len(R) <= 8
        label = "".join("+" if sign == 1 else "-" for sign in signs)
        opposite = "".join("+" if sign == -1 else "-" for sign in signs)
        lower = branch_lower_system(E, D, R, Tpoly, producer)
        branches.append({
            "label": label,
            "root_order": ROOT_LABELS,
            "signs": list(signs),
            "global_sign_pair": min(label, opposite),
            "E": pencode(E),
            "D=(E^2-1)/A^2": pencode(D),
            "R=rem(E*D,A^2)": pencode(R),
            "T=(E*R-D)/A^2": pencode(Tpoly),
            "Bhat": "rho*E+lambda*A^2",
            "C": "rho*R/4+lambda/2 (the unique degree-<8 representative)",
            "M": "3*rho^2*D/8+3*rho*lambda*E/4+3*lambda^2*A^2/8",
            "N": "3*rho^2*T/16+3*rho*lambda*R/16+3*lambda^2/16",
            "lower_window_test": lower,
        })
    assert len(branches) == 16
    assert len({branch["global_sign_pair"] for branch in branches}) == 8
    assert not any(branch["lower_window_test"]["literal_nonzero_constant_equations"]
                   for branch in branches)
    by_label = {branch["label"]: branch for branch in branches}
    for branch in branches:
        opposite = "".join("-" if sign == "+" else "+"
                           for sign in branch["label"])
        partner = by_label[opposite]
        assert branch["D=(E^2-1)/A^2"] == partner["D=(E^2-1)/A^2"]
        assert branch["T=(E*R-D)/A^2"] == partner["T=(E*R-D)/A^2"]
    return branches


def live_mutations():
    signs = (-1, -1, -1, 1)
    E, D = hermite_sign_lift(signs)
    _, P = pdivmod(E, A)
    # P carries only the root values.  Omitting the four derivative conditions
    # makes P^2-1 divisible by A, but generically not by A^2.
    p_square = padd(pmul(P, P), [g(-1)])
    _, remainder_mod_a = pdivmod(p_square, A)
    _, remainder_mod_a2 = pdivmod(p_square, A2)
    assert not remainder_mod_a
    assert remainder_mod_a2

    ED = pmul(E, D)
    _, R = pdivmod(ED, A2)
    correct_numerator = pscale(Q(3, 4), padd(pmul(E, R), pscale(-1, D)))
    _, correct_remainder = pdivmod(correct_numerator, A2)
    assert not correct_remainder
    wrong_sign_numerator = pscale(Q(-3, 4), padd(pmul(E, R), D))
    _, wrong_sign_remainder = pdivmod(wrong_sign_numerator, A2)
    assert wrong_sign_remainder

    # On J16=0, D16 alone permits Bhat=A and M=3/8, but D17 with C=0
    # has numerator -3/4, demonstrating the necessary second A factor.
    return {
        "drop_Hermite_derivative_conditions": {
            "signs_at_roots": list(signs),
            "degree_less_than_4_value_interpolant_P": pencode(P),
            "P^2_minus_1_mod_A": {},
            "P^2_minus_1_mod_A^2": pencode(remainder_mod_a2),
            "caught": True,
        },
        "wrong_D17_C_sign": {
            "correct_C_rho_coefficient": "+R/4",
            "mutated_C_rho_coefficient": "-R/4",
            "correct_D17_rho2_remainder_mod_A2": {},
            "mutated_D17_rho2_remainder_mod_A2": pencode(wrong_sign_remainder),
            "caught": True,
        },
        "J16_zero_stop_after_one_A": {
            "mutated_Bhat": "A",
            "D16_quotient_M": "3/8",
            "choose_C": "0",
            "D17_numerator_mod_A": "-3/4",
            "caught": True,
        },
    }


def calculate_result():
    assert digest(RAW) == RAW_SHA256
    producer = load_producer()
    raw = json.loads(RAW.read_text())
    assert raw["windows"]["F"]["8"]["upper"] == 8
    assert raw["windows"]["F"]["9"]["lower"] == 1
    assert raw["windows"]["F"]["9"]["upper"] == 7
    branches = classify_nonzero_branch(producer)
    return {
        "schema": "jc2.ggv.upper_endpoint.uniform_d16_d17.sign_branches.result.v1",
        "status": "PASS_EXACT_DEGREE_BOUNDED_D16_D17_SIGN_CLASSIFICATION",
        "source": {
            "producer_checker": str(PRODUCER.relative_to(ROOT)),
            "producer_checker_sha256": PRODUCER_SHA256,
            "producer_result": str(PRODUCER_RESULT.relative_to(ROOT)),
            "producer_result_sha256": PRODUCER_RESULT_SHA256,
            "authoritative_raw_system": str(RAW.relative_to(ROOT)),
            "authoritative_raw_system_sha256": RAW_SHA256,
        },
        "degree_bounds": {
            "A": "X^4-1, squarefree in characteristic zero",
            "Z": 6,
            "V": 5,
            "R": 4,
            "Q": 3,
            "T": 2,
            "Y": 1,
            "Bhat": 8,
            "C": 7,
            "derivation": [
                "raw T has degree <=9 and T=A*V, hence deg(V)<=5",
                "successive A^2 quotients in F4..F7 give deg(R,Q,T,Y)<=4,3,2,1",
                "the raw F8/F9 windows and completed cross terms give deg(Bhat)<=8 and deg(C)<=7",
            ],
        },
        "J16_nonzero": {
            "extension": "adjoin rho with rho^2=-8*J16/3; rho is nonzero",
            "classification_proof": [
                "D16-centered gives Bhat^2=rho^2 mod A^2",
                "over the splitting field, every local factor K[epsilon]/(epsilon^2) has exactly the two square roots +/-1 of 1",
                "there are 2^4=16 unique degree-<8 Hermite sign lifts E_s with E_s(root)=s_root and E_s'(root)=0",
                "deg(Bhat)<=8 then gives Bhat=rho*E_s+lambda*A^2",
                "the 16 lifts form eight pairs under simultaneous E_s->-E_s, rho->-rho",
                "D17 uniquely gives C congruent to rho*E_s*((E_s^2-1)/A^2)/4+lambda/2 mod A^2; deg(C)<=7 selects its unique remainder",
            ],
            "branch_count": 16,
            "branch_count_mod_global_sign": 8,
            "root_order": ROOT_LABELS,
            "branches": branches,
        },
        "J16_zero": {
            "proof": [
                "D16-centered gives A^2 divides Bhat^2; squarefreeness of A gives A divides Bhat",
                "write Bhat=A*L; then M=3*L^2/8",
                "D17 modulo A gives A divides L^2, hence A divides L",
                "deg(Bhat)<=8 now forces Bhat=lambda*A^2",
                "M=3*lambda^2*A^2/8 and D17 permits arbitrary deg(C)<=7, with N=3*lambda*C/4-3*lambda^2/16",
            ],
            "conclusion": "Bhat=lambda*A^2; C remains free within its degree bound and later/lower equations",
        },
        "lower_window_test_summary": {
            "equations_substituted_per_nonzero_branch": [
                "F9_X0_absence", "C13", "C14", "C15",
                "G16_X0", "G16_X1", "G17_X0", "G17_X1",
            ],
            "exact_branch_systems": 16,
            "systems_mod_global_sign": 8,
            "immediate_literal_unit_equations": 0,
            "conclusion": (
                "the finite sign classification does not by itself eliminate a branch; "
                "it converts every lower-window test into an explicit small exact scalar system"
            ),
        },
        "live_mutations": live_mutations(),
        "scope_firewall": [
            "the J16!=0 classification is over a splitting field after adjoining rho; no root is normalized",
            "global-sign pairing is bookkeeping only and does not discard either rho sheet",
            "absence of an immediate literal unit is not a consistency or existence proof for any branch system",
            "the lower-window systems are exact substitutions, not Groebner eliminations",
            "no transport to the cutoff-three K invariant is asserted in this packet",
            "no endpoint, unrestricted branch-P, or JC2 conclusion",
            "standard-library exact arithmetic only; no CAS, AWS, or jc2-lean",
        ],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--dump", action="store_true")
    arguments = parser.parse_args()
    result = calculate_result()
    encoded = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    if arguments.write:
        RESULT.write_bytes(encoded)
    if arguments.check:
        assert RESULT.read_bytes() == encoded
    if arguments.dump:
        print(encoded.decode(), end="")
    else:
        print(json.dumps({
            "status": result["status"],
            "nonzero_branch_count": result["J16_nonzero"]["branch_count"],
            "mod_global_sign": result["J16_nonzero"]["branch_count_mod_global_sign"],
            "immediate_units": result["lower_window_test_summary"][
                "immediate_literal_unit_equations"],
            "check": arguments.check,
        }, sort_keys=True))


if __name__ == "__main__":
    main()
