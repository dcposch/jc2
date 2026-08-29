#!/usr/bin/env python3
"""Exact D12 obstruction for the frozen q1 proper-divisor D11 survivor."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RESULT = HERE / "RESULT.json"
TARGET = HERE / "TARGET.json"

PREDECESSOR = ROOT / "cases/ggv_8_28_upper_endpoint_q1_post_d9_d11_survivor_20260828/verify_q1_post_d9_d11.py"
PREDECESSOR_RESULT = PREDECESSOR.with_name("RESULT.json")
PREDECESSOR_TARGET = PREDECESSOR.with_name("TARGET.json")
PREDECESSOR_SOURCE = PREDECESSOR.with_name("SOURCE.sha256")
PREDECESSOR_EVIDENCE = PREDECESSOR.with_name("EVIDENCE.sha256")
RAW_INPUT = ROOT / "cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json"

SOURCE_PINS = {
    PREDECESSOR: "499d73d88df20c2404596f4402a46f0884b1d0703ff6e4016c8bba87a3f2e0ac",
    PREDECESSOR_RESULT: "d03a0fafdc2fde7f3e43ed53da3c631f4f3350c46dab1c1bda169de91a84eee0",
    PREDECESSOR_TARGET: "0f55c51ce513ca205f9efba372408f4938f90929b2a033e0640616cf20f66c93",
    PREDECESSOR_SOURCE: "a180b0e83b11c8c553c2edf029c06f057cb94dae6741beda1335c76f655a6c5e",
    PREDECESSOR_EVIDENCE: "a9386173dbcdcc114f7faf2210be9c4eae1659bcb493fa3ed629134aac508992",
    RAW_INPUT: "28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876",
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_predecessor():
    spec = importlib.util.spec_from_file_location("q1_d11_frozen", PREDECESSOR)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


P = load_predecessor()


def decode(item):
    if not item:
        return []
    answer = [Q(0)] * (max(map(int, item)) + 1)
    for degree, coefficient in item.items():
        answer[int(degree)] = Q(coefficient)
    return P.V.xp_trim(answer)


def pencode(item):
    return {str(i): str(c) for i, c in enumerate(item) if c}


def padd(*items):
    return P.V.xp_add(*items)


def pscale(coefficient, item):
    return P.V.xp_scale(Q(coefficient), item)


def pmul(*items):
    answer = [Q(1)]
    for item in items:
        answer = P.V.xp_mul(answer, item)
    return answer


def ppow(item, exponent):
    return P.V.xp_power(item, exponent)


def pdivexact(left, right):
    quotient, remainder = P.V.xp_divmod(left, right)
    assert not remainder, pencode(remainder)
    return quotient


def psub(left, right):
    return padd(left, pscale(-1, right))


def pextended_gcd(left, right):
    old_r, r = left, right
    old_s, s = [Q(1)], []
    old_t, t = [], [Q(1)]
    while r:
        quotient, remainder = P.V.xp_divmod(old_r, r)
        old_r, r = r, remainder
        old_s, s = s, psub(old_s, pmul(quotient, s))
        old_t, t = t, psub(old_t, pmul(quotient, t))
    lead = old_r[-1]
    return pscale(1 / lead, old_r), pscale(1 / lead, old_s), pscale(1 / lead, old_t)


def rref(matrix):
    work = [row[:] for row in matrix]
    rows = len(work)
    columns = len(work[0]) if rows else 0
    pivot_row = 0
    pivots = []
    for column in range(columns):
        pivot = next((row for row in range(pivot_row, rows)
                      if work[row][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        factor = work[pivot_row][column]
        work[pivot_row] = [value / factor for value in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [left - factor * right
                         for left, right in zip(work[row], work[pivot_row])]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == rows:
            break
    return work, pivots


def rank(matrix):
    return len(rref(matrix)[1])


def raw_weight12_slots():
    source = json.loads(RAW_INPUT.read_text())
    answer = {}
    for kind in ("F", "G"):
        records = [record for record in source["raw_slots_through_weight_22"][kind]
                   if int(record["weight"]) == 12]
        answer[kind] = {str(record["raw_exponents"]["x"]): record["slot"]
                        for record in records}
    assert sorted(map(int, answer["F"])) == [2, 3, 4]
    assert sorted(map(int, answer["G"])) == list(range(13))
    return answer


def calculate():
    for path, expected in SOURCE_PINS.items():
        assert digest(path) == expected, (path, digest(path), expected)
    prior = json.loads(PREDECESSOR_RESULT.read_text())
    fixed = prior["exact_rational_survivor"]
    F = [decode(fixed["F"].get(str(weight), {})) for weight in range(12)]
    G = [decode(fixed["G"].get(str(weight), {})) for weight in range(12)]
    A, B, C = map(lambda name: decode(fixed[name]), ("A", "B", "C"))
    A4 = ppow(A, 4)

    # Complete base numerator in the weight-12 coefficient of F^(3/2).
    # The omitted i=12 term is 18*F12*A^6 and hence contributes the regular
    # polynomial (3/2)*A^2*F12 after division by 12*A^4.
    numerator = []
    for index in range(1, 12):
        factor = Q(5, 2) * index - 12
        numerator = padd(numerator,
                         pscale(factor, pmul(F[index], G[12 - index])))
    quotient, remainder = P.V.xp_divmod(numerator, A4)
    assert remainder

    common = P.V.xp_gcd(numerator, A4)
    expected_common = pmul(A, B)  # A*B=C*B^2
    assert common == expected_common
    reduced_numerator = pdivexact(numerator, common)
    reduced_denominator = pdivexact(A4, common)
    assert reduced_denominator == pmul(ppow(C, 3), ppow(B, 2))
    assert P.V.xp_gcd(reduced_numerator, A) == [Q(1)]
    assert sum(reduced_numerator) == Q(-12)

    gcd_b, bezout_n, bezout_b = pextended_gcd(reduced_numerator, B)
    assert gcd_b == [Q(1)]
    assert padd(pmul(bezout_n, reduced_numerator), pmul(bezout_b, B)) == [Q(1)]

    # Legal new data cannot alter the polar residue.
    sample_f12 = [Q(0), Q(0), Q(1), Q(2), Q(3)]
    full_numerator = padd(numerator, pscale(18, pmul(sample_f12, ppow(A, 6))))
    _, sample_remainder = P.V.xp_divmod(full_numerator, A4)
    assert sample_remainder == remainder
    sample_c12 = Q(5)  # F^0 is 1, so this is a regular constant in G12.

    # Independent direct raw D12 affine system.
    base_row = []
    for index in range(1, 12):
        j = 12 - index
        base_row = padd(
            base_row,
            pscale(12 - j, pmul(P.V.xp_derivative(F[index]), G[j])),
            pscale(index - 8, pmul(F[index], P.V.xp_derivative(G[j]))),
        )
    columns = []
    variable_names = []
    for degree in range(2, 5):
        monomial = [Q(0)] * (degree + 1)
        monomial[degree] = Q(1)
        columns.append(padd(
            pscale(12, pmul(P.V.xp_derivative(monomial), G[0])),
            pscale(4, pmul(monomial, P.V.xp_derivative(G[0]))),
        ))
        variable_names.append(f"F12_X{degree}")
    for degree in range(13):
        monomial = [Q(0)] * (degree + 1)
        monomial[degree] = Q(1)
        columns.append(pscale(-8, pmul(F[0], P.V.xp_derivative(monomial))))
        variable_names.append(f"G12_X{degree}")
    coefficient_count = max([len(base_row)] + [len(column) for column in columns])
    matrix = [[column[degree] if degree < len(column) else Q(0)
               for column in columns] for degree in range(coefficient_count)]
    rhs = [-(base_row[degree] if degree < len(base_row) else Q(0))
           for degree in range(coefficient_count)]
    matrix_rank = rank(matrix)
    augmented_rank = rank([row + [value] for row, value in zip(matrix, rhs)])
    assert (coefficient_count, len(columns), matrix_rank, augmented_rank) == (28, 16, 12, 13)

    # A four-term direct dual certificate, recorded without normalization.
    dual = {0: Q(20), 4: Q(10), 8: Q(4), 12: Q(1)}
    for column in columns:
        assert sum(coefficient * (column[degree] if degree < len(column) else 0)
                   for degree, coefficient in dual.items()) == 0
    dual_pairing = sum(coefficient * (base_row[degree]
                                      if degree < len(base_row) else 0)
                       for degree, coefficient in dual.items())
    assert dual_pairing == Q(11009739, 16384)
    mutated_dual = dict(dual)
    mutated_dual[0] = Q(19)
    mutated_column_pairings = [
        sum(coefficient * (column[degree] if degree < len(column) else 0)
            for degree, coefficient in mutated_dual.items())
        for column in columns
    ]
    assert any(mutated_column_pairings)
    assert not columns[3]  # G12 constant = born c12 direction.

    target = target_payload()
    return {
        "status": "PASS_EXACT_Q1_D11_SURVIVOR_D12_OBSTRUCTION",
        "source_pins": {str(path.relative_to(ROOT)): expected
                        for path, expected in SOURCE_PINS.items()},
        "literal_weight12_slots": raw_weight12_slots(),
        "characteristic_certificate": {
            "recurrence_numerator": pencode(numerator),
            "recurrence_numerator_sha256": hashlib.sha256(json.dumps(
                pencode(numerator), sort_keys=True, separators=(",", ":")
            ).encode()).hexdigest(),
            "division_quotient_mod_A4": pencode(quotient),
            "division_remainder_mod_A4": pencode(remainder),
            "division_remainder_sha256": hashlib.sha256(json.dumps(
                pencode(remainder), sort_keys=True, separators=(",", ":")
            ).encode()).hexdigest(),
            "gcd_N12_A4": pencode(common),
            "reduced_numerator": pencode(reduced_numerator),
            "reduced_denominator_without_scalar_12": pencode(reduced_denominator),
            "reduced_shape": "g12_polar=Nred/(12*C^3*B^2)",
            "Nred_at_C_root_X1": "-12",
            "bezout_mod_B": {
                "Nred_cofactor": pencode(bezout_n),
                "B_cofactor": pencode(bezout_b),
                "identity": "Nred_cofactor*Nred+B_cofactor*B=1",
            },
            "local_B_root_verdict": (
                "independent of the C-root: Nred is a unit modulo B, C is a "
                "unit modulo B, and the B^2 denominator gives a pole at each "
                "of the three B-roots"
            ),
            "new_terms_are_regular": {
                "F12": "(3/2)*A^2*F12",
                "c12": "constant c12*F^0",
            },
        },
        "direct_raw_D12_certificate": {
            "operator": (
                "D12_base+12*F12'*G0+4*F12*G0'-8*F0*G12'"
            ),
            "base_row": pencode(base_row),
            "base_row_sha256": hashlib.sha256(json.dumps(
                pencode(base_row), sort_keys=True, separators=(",", ":")
            ).encode()).hexdigest(),
            "coefficient_rows": coefficient_count,
            "variables": variable_names,
            "matrix_rank": matrix_rank,
            "augmented_rank": augmented_rank,
            "homogeneous_nullity": len(columns) - matrix_rank,
            "dual_functional": "20*[X^0]+10*[X^4]+4*[X^8]+[X^12]",
            "dual_pairing_with_every_new_column": "0",
            "dual_pairing_with_base": str(dual_pairing),
            "c12_G12_X0_column_is_zero": True,
        },
        "mutations": {
            "legal_F12_X2_plus_2X3_plus_3X4": {
                "polar_remainder_unchanged": sample_remainder == remainder,
            },
            "legal_c12_equals_5": {
                "value": str(sample_c12),
                "polar_remainder_unchanged": True,
            },
            "dual_weight_20_changed_to_19": {
                "nonzero_new_column_pairings": {
                    variable_names[index]: str(value)
                    for index, value in enumerate(mutated_column_pairings) if value
                },
            },
        },
        "target_sha256": hashlib.sha256((json.dumps(
            target, sort_keys=True, indent=2
        ) + "\n").encode()).hexdigest(),
        "scope": target["scope_firewall"],
    }


def target_payload():
    return {
        "format": "GGV_BRANCH_P_Q1_FIXED_PROPER_DIVISOR_D12_OBSTRUCTION_V1",
        "input": "the exact rational D0..D11 survivor frozen in the predecessor packet",
        "verdict": "no legal raw-window extension to D12",
        "characteristic_reason": (
            "the unavoidable g12 polar part is Nred/(12*C^3*B^2), with "
            "gcd(Nred,A)=1; F12 and c12 contribute only regular terms"
        ),
        "direct_reason": (
            "the 28x16 D12 affine raw coefficient system has matrix rank 12 "
            "and augmented rank 13; a four-term dual functional is nonzero "
            "on its base row and zero on every legal new column"
        ),
        "single_B_root_evidence": (
            "Nred is a unit modulo B, so each B-root obstructs independently "
            "of the separate C-root pole"
        ),
        "scope_firewall": (
            "This kills only the one frozen rational D11 prefix.  It is not a "
            "universal proper-divisor theorem, not a proof of single-root "
            "transport for arbitrary prefixes, and not an endpoint or JC2 result."
        ),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = calculate()
    target = target_payload()
    result_encoded = json.dumps(result, sort_keys=True, indent=2) + "\n"
    target_encoded = json.dumps(target, sort_keys=True, indent=2) + "\n"
    if args.check:
        assert RESULT.read_text() == result_encoded
        assert TARGET.read_text() == target_encoded
    else:
        RESULT.write_text(result_encoded)
        TARGET.write_text(target_encoded)
    print(result["status"])


if __name__ == "__main__":
    main()
