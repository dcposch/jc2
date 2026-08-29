#!/usr/bin/env python3
"""Fail-closed high-order p-adic diagnostic for the pristine D43 source.

This adapter follows one deterministic compatible branch of the 184-row
pristine source system at p=105337.  Its declared source ambient has 182
essential coordinates:

    172 effective tail coordinates + 8 fixed coordinates + alpha,beta.

The nominal 190-coordinate differential engine also contains the eight
dense-family tail labels r=39,41.  They are structurally absent from every
selected band <=42 and are required to be literal zero Jacobian columns
before they are removed.

The first digit is reconstructed from the committed mod-p point and must
match the committed p^2 correction digest.  Every later digit uses the
same exact Newton rule, verifies all 184 rows, records the left-cokernel
syndrome, and atomically checkpoints an authenticated state envelope.

FINITE-SCOPE FIREWALL.  A successful run through p^N certifies only a
compatible point of this finite 184-row source truncation modulo p^N that
also passes the necessary E5-consistency relation and W-unit checks at each
committed digit.  Those extra checks do not replay the template, D25, parked
presentation, or inverse variables.  In particular, this is not evidence
that a D43 template branch survives.  It does not certify an assembled
218-row point, a Z_p point, a characteristic-zero point, a formal germ, a
Keller map, or a JC2 counterexample.  An obstruction after p^2 concerns the
particular previously chosen branch; earlier kernel digits were
deterministically set to zero.
"""

from __future__ import annotations

import argparse
import contextlib
import fcntl
import hashlib
import json
import math
import os
import platform
import socket
import tempfile
from dataclasses import asdict
from typing import Callable, Iterable, Mapping, Sequence


HERE = os.path.dirname(os.path.abspath(__file__))

# This module is pure-Python and intentionally importable without NumPy.
# The D43 numerical dependencies are loaded only by prepare_d43_context().
import sys
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import d43_common_integral_emitter as INTEGRAL


PRIME = 105337
FAMILIES = ("tf1", "tf2", "tg1", "tg2", "tg01", "tg02")
DENSE_FAMILIES = ("tf1", "tf2", "tg1", "tg2")
FIXED_COORDS = ("W1", "W2", "uf18", "uf24", "vf1_34", "vf1_36",
                "vf2_34", "vf2_36")
DEAD_TAIL_LABELS = tuple((family, r) for family in DENSE_FAMILIES
                         for r in (39, 41))
P4P1 = {2: -23328, 5: 101088, 8: -186624, 11: 191808,
        14: -120528, 17: 47952, 20: -12096, 23: 1872,
        26: -162, 29: 6}

SCHEMA = "d43-pristine-source-high-hensel-state-v2"
AWS_AUTH_SCHEMA = "d43-pristine-source-high-hensel-aws-auth-v1"
STATUS_READY = "REGISTERED_MOD_P_SOURCE_POINT"
STATUS_FINITE = "FINITE_SOURCE_LIFT_ONLY"
STATUS_OBSTRUCTED = "SPECIFIC_BRANCH_OBSTRUCTED"
STATUS_TEMPLATE_FAILED = "FINITE_RAW_SOURCE_TEMPLATE_GATE_FAILED"
SCOPE = "residue-A, B=84, a00pp, finite raw 184-row Euler/J-source truncation only"
CERTIFIED_CLAIM = (
    "at every successful committed digit, one finite congruence point of "
    "the declared raw 184-row Euler/J-source truncation satisfying the "
    "necessary E=0 and W1,W2 unit gates")
FORBIDDEN_CLAIMS = (
    "assembled 218-row p-adic point",
    "parked/source presentation equivalence",
    "full residue-A/template/D25 p-adic point or upstream exact-equation lift",
    "D43 template-branch evidence or survival from the raw-source lift",
    "indefinite source solvability or formal smoothness",
    "Z_p point",
    "characteristic-zero point",
    "formal germ",
    "ambient polynomial Keller map",
    "JC2 counterexample",
)
EXACT_RELATIONS_REPLAYED = (
    "184 raw Euler/J-source rows",
    "Phi42(zeta)=0, r3^2=3, A1^3=3+r3, A2^3=3-r3, 2h^2=3",
    "necessary E=(9+5r3)A1W1^4+(9-5r3)A2W2^4=0 and W1,W2 unit gates at every committed state",
    "two corrected-243 E5 rows with a common deterministic HM witness and the cube-form E6 row with a nonzero deterministic s1F witness",
    "HW1=h*W1 and HW2=h*W2 inside every source evaluation",
    "literal uf30=0 and the named finite source completion encoded by the evaluator",
)
UPSTREAM_NOT_REPLAYED = (
    "34 parked D21/D23/D25 constraints",
    "W1*uW1-1 and W2*uW2-1 inverse-chart rows",
    "template and low-order reconstruction equations",
    "source-to-NF and reducer membership identities",
)
BRANCH_POLICY = {
    "linear_solver": "deterministic RREF in the sealed 182-coordinate order",
    "free_digits": "all 53 free correction digits are zero at every successful step",
    "p2_anchor": "actual first transition must reproduce the committed frame, RHS, correction, and point hashes",
    "resume": "recompute the registered initial state and every complete transition before accepting stored state",
    "later_obstruction_scope": "specific previously selected branch only; alternative earlier kernel digits remain open",
}
REGISTERED_P2_RHS_SHA256 = \
    "82155c419d48873523ce08be0eeb228155ff0e72338a4867c1f35b34fd71b917"
REGISTERED_P2_CORRECTION_SHA256 = \
    "e3a15fa66ed6f08e3f1c78eb793226ad750ab67a9216ce3dadbaeae82ad79c26"
REGISTERED_P2_POINT_SHA256 = \
    "c8bee81b9e56a32d7695f9905951c7798e6d88a6b9c72725ad08e4bce08530b4"
REGISTERED_P2_FRAME_SHA256 = \
    "24e7917ba65c713e6aa103db4bb48d2a0f53f0cfed64eefe8209457b37f3d9a6"
REGISTERED_P2_W1 = 10092159227
REGISTERED_P2_W2 = 4041263462
REGISTERED_P2_TEMPLATE_GATE_SHA256 = \
    "39702f29d6e1a0b6f45864eca343b555620b41d8cb747b60bca057b3799804e3"
INITIAL_HISTORY_SHA256 = hashlib.sha256(b"[]").hexdigest()
AWS_TARGET_TAGS = {
    16: "D43-PRISTINE-SOURCE-HIGH-HENSEL-R1-N16",
    64: "D43-PRISTINE-SOURCE-HIGH-HENSEL-R1-N64",
}


def registered_claims() -> dict:
    return {
        "certified": CERTIFIED_CLAIM,
        "exact_relations_replayed": list(EXACT_RELATIONS_REPLAYED),
        "upstream_not_replayed": list(UPSTREAM_NOT_REPLAYED),
        "forbidden": list(FORBIDDEN_CLAIMS),
    }


def sha256_path(path: str) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(8 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def sha256_json(value) -> str:
    blob = json.dumps(value, sort_keys=True,
                      separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()


def _poly_eval_exact(coefficients: Iterable[int], value: int) -> int:
    result = 0
    for coefficient in reversed(tuple(coefficients)):
        result = result * value + int(coefficient)
    return result


def lift_simple_root_digit(value: int, prime: int, exponent: int,
                           polynomial: Callable[[int], int],
                           derivative: Callable[[int], int]):
    """Lift one simple root from p^exponent to p^(exponent+1)."""
    if exponent < 1:
        raise ValueError("exponent must be positive")
    step = prime ** exponent
    modulus = step * prime
    value = int(value) % step
    residual = int(polynomial(value))
    if residual % step:
        raise ValueError("input is not a root modulo p^exponent")
    slope = int(derivative(value)) % prime
    if not slope:
        raise ValueError("root is not simple modulo p")
    digit = (-(residual // step) * pow(slope, -1, prime)) % prime
    lifted = value + step * digit
    if polynomial(lifted) % modulus:
        raise AssertionError("simple-root Hensel replay failed")
    return lifted, digit


def _frame_dict(frame: INTEGRAL.RootFrame) -> dict[str, int]:
    return {key: int(value) for key, value in asdict(frame).items()}


def lift_root_frame_digit(frame: INTEGRAL.RootFrame, prime: int,
                          exponent: int):
    """Jointly lift the registered radical frame by one base-p digit.

    r3 is lifted before A1,A2 because their equations contain r3.
    The cyclotomic root uses literal Phi_42, not z^42-1.
    """
    step = prime ** exponent
    frame = frame.reduced(step)
    zeta, dz = lift_simple_root_digit(
        frame.zeta42, prime, exponent,
        lambda z: _poly_eval_exact(INTEGRAL.PHI42, z),
        lambda z: _poly_eval_exact(INTEGRAL.PHI42_DERIV, z))
    r3, dr = lift_simple_root_digit(
        frame.r3, prime, exponent,
        lambda r: r * r - 3, lambda r: 2 * r)
    h, dh = lift_simple_root_digit(
        frame.h, prime, exponent,
        lambda x: 2 * x * x - 3, lambda x: 4 * x)
    A1, da1 = lift_simple_root_digit(
        frame.A1, prime, exponent,
        lambda value: value ** 3 - 3 - r3,
        lambda value: 3 * value * value)
    A2, da2 = lift_simple_root_digit(
        frame.A2, prime, exponent,
        lambda value: value ** 3 - 3 + r3,
        lambda value: 3 * value * value)
    lifted = INTEGRAL.RootFrame(zeta, r3, A1, A2, h)
    modulus = step * prime
    validation = INTEGRAL.validate_specialization(
        modulus, lifted, INTEGRAL.SOURCE_NEWTON_DENOMINATORS)
    return lifted, {
        "digits": {"zeta42": dz, "r3": dr, "A1": da1,
                   "A2": da2, "h": dh},
        "digits_sha256": sha256_json([dz, dr, da1, da2, dh]),
        "frame_sha256": sha256_json(_frame_dict(lifted)),
        "defining_equations_sha256": sha256_json(validation["equations"]),
    }


def factor_matrix(matrix: Sequence[Sequence[int]], prime: int) -> dict:
    """Deterministic RREF together with a left-cokernel basis.

    The returned transform T satisfies T*matrix = rref.  Rows of T below
    the rank are therefore a deterministic basis of the left kernel.
    """
    rows = len(matrix)
    columns = len(matrix[0]) if rows else 0
    if any(len(row) != columns for row in matrix):
        raise ValueError("ragged matrix")
    work = [[int(value) % prime for value in row] for row in matrix]
    transform = [[int(i == j) for j in range(rows)] for i in range(rows)]
    rank = 0
    pivots = []
    for column in range(columns):
        pivot = next((row for row in range(rank, rows)
                      if work[row][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        transform[rank], transform[pivot] = transform[pivot], transform[rank]
        inverse = pow(work[rank][column], -1, prime)
        work[rank] = [value * inverse % prime for value in work[rank]]
        transform[rank] = [value * inverse % prime
                           for value in transform[rank]]
        for row in range(rows):
            if row == rank or not work[row][column]:
                continue
            scale = work[row][column]
            work[row] = [(left - scale * right) % prime
                         for left, right in zip(work[row], work[rank])]
            transform[row] = [(left - scale * right) % prime
                              for left, right in zip(transform[row],
                                                     transform[rank])]
        pivots.append(column)
        rank += 1
        if rank == rows:
            break
    if any(any(row) for row in work[rank:]):
        raise AssertionError("RREF zero-row suffix invariant failed")
    left_cokernel = transform[rank:]
    return {
        "prime": prime,
        "rows": rows,
        "columns": columns,
        "rank": rank,
        "pivot_columns": pivots,
        "free_columns": [column for column in range(columns)
                         if column not in set(pivots)],
        "rref": work,
        "transform": transform,
        "left_cokernel": left_cokernel,
        "matrix_sha256": sha256_json(matrix),
        "rref_sha256": sha256_json(work),
        "left_cokernel_sha256": sha256_json(left_cokernel),
    }


def solve_factored(factor: Mapping, rhs: Sequence[int]) -> dict:
    prime = int(factor["prime"])
    rows = int(factor["rows"])
    columns = int(factor["columns"])
    if len(rhs) != rows:
        raise ValueError("rhs length mismatch")
    transformed = [sum(value * int(rhs[index])
                       for index, value in enumerate(row)) % prime
                   for row in factor["transform"]]
    rank = int(factor["rank"])
    syndrome = transformed[rank:]
    nonzero = [index for index, value in enumerate(syndrome) if value]
    common = {
        "rhs_sha256": sha256_json([int(value) % prime for value in rhs]),
        "transformed_rhs_sha256": sha256_json(transformed),
        "left_cokernel_dimension": rows - rank,
        "left_cokernel_basis_sha256": factor["left_cokernel_sha256"],
        "syndrome_sha256": sha256_json(syndrome),
        "nonzero_syndrome_entries": len(nonzero),
        "solvable": not nonzero,
    }
    if nonzero:
        basis_index = nonzero[0]
        witness = factor["left_cokernel"][basis_index]
        common["obstruction"] = {
            "basis_index": basis_index,
            "pairing_mod_p": syndrome[basis_index],
            "left_kernel_vector": witness,
            "left_kernel_vector_sha256": sha256_json(witness),
        }
        common["solution"] = None
        return common
    solution = [0] * columns
    for row, column in enumerate(factor["pivot_columns"]):
        solution[column] = transformed[row]
    # Independent direct replay against the original matrix reconstructed
    # as T^{-1}*R is intentionally avoided; callers replay J*delta=rhs.
    common["solution"] = solution
    common["solution_sha256"] = sha256_json(solution)
    common["nonzero_solution_coordinates"] = sum(bool(x) for x in solution)
    return common


def apply_digits(values: Mapping[str, int], labels: Sequence,
                 correction: Sequence[int], step: int,
                 modulus: int) -> dict[str, int]:
    if len(labels) != len(correction):
        raise ValueError("coordinate/correction length mismatch")
    out = {str(key): int(value) % step for key, value in values.items()}
    for label, digit in zip(labels, correction):
        key = coordinate_key(label)
        if key not in out:
            raise KeyError("missing coordinate %s" % key)
        out[key] = (out[key] + step * int(digit)) % modulus
    return out


def coordinate_key(label) -> str:
    family, index = label
    return "%s:%s" % (family, index)


def coordinate_label_json(label):
    return [str(label[0]), label[1]]


def template_relation_gate(coordinates: Mapping[str, int],
                           frame: INTEGRAL.RootFrame,
                           modulus: int) -> dict:
    """Replay the necessary minimal-branch E5 consistency condition.

    This is deliberately not an assertion that the raw 184 rows imply E.
    Besides checking E and the W units, it constructs the unique common HM
    witness for the corrected-243 E5 pair and an explicit nonzero s1F witness
    for the cube-form E6 equation.  It does not replay the parked/template
    reconstruction chain from which those equations were derived.
    """
    if isinstance(modulus, bool) or not isinstance(modulus, int) or \
            modulus <= 1:
        raise ValueError("template-relation modulus must exceed one")
    required = ("FIX:W1", "FIX:W2")
    if any(key not in coordinates for key in required):
        raise ValueError("template-relation coordinates are incomplete")
    W1 = int(coordinates["FIX:W1"]) % modulus
    W2 = int(coordinates["FIX:W2"]) % modulus
    r3 = int(frame.r3) % modulus
    A1 = int(frame.A1) % modulus
    A2 = int(frame.A2) % modulus
    first_term = ((9 + 5 * r3) * A1 * pow(W1, 4, modulus)) % modulus
    second_term = ((9 - 5 * r3) * A2 * pow(W2, 4, modulus)) % modulus
    residue = (first_term + second_term) % modulus
    W1_unit = math.gcd(W1, modulus) == 1
    W2_unit = math.gcd(W2, modulus) == 1
    a1 = (3 + r3) % modulus
    a2 = (3 - r3) % modulus
    denominators = {
        "2^6": pow(2, 6, modulus),
        "7^16": pow(7, 16, modulus),
        "4(a1-4)": 4 * (a1 - 4) % modulus,
        "4(a2-4)": 4 * (a2 - 4) % modulus,
    }
    denominator_units = {
        key: math.gcd(value, modulus) == 1
        for key, value in denominators.items()
    }
    e5e6 = {
        "constant_convention": (
            "corrected 243=3^5 E5 coefficient; cube-form E6"),
        "denominator_units": denominator_units,
        "HM_pole1": None,
        "HM_pole2": None,
        "HM_common": False,
        "HM_unit": False,
        "E5_residues_modulus": None,
        "s1F": None,
        "s1F_unit": False,
        "E6_residue_modulus": None,
        "pass": False,
    }
    if all(denominator_units.values()):
        SM = (pow(7, 12, modulus) *
              pow(denominators["2^6"], -1, modulus)) % modulus
        delta_a = (a1 - a2) % modulus
        hm_values = []
        e5_residues = []
        for ai, Ai, Wi, denominator_key in (
                (a1, A1, W1, "4(a1-4)"),
                (a2, A2, W2, "4(a2-4)")):
            load = (243 * pow(SM, 3, modulus) *
                    pow(delta_a, 4, modulus) * pow(ai, 2, modulus) *
                    Ai * pow(Wi, 4, modulus)) % modulus
            hm = (-load * pow(denominators[denominator_key], -1,
                              modulus)) % modulus
            hm_values.append(hm)
            e5_residues.append(
                (denominators[denominator_key] * hm + load) % modulus)
        HM = hm_values[0]
        s1F = (pow(2, 8, modulus) * HM *
               pow(denominators["7^16"], -1, modulus)) % modulus
        e6_residue = (pow(2, 24, modulus) * pow(HM, 3, modulus) -
                      pow(7, 48, modulus) * pow(s1F, 3, modulus)) % modulus
        hm_common = hm_values[0] == hm_values[1]
        hm_unit = math.gcd(HM, modulus) == 1
        s1F_unit = math.gcd(s1F, modulus) == 1
        e5e6.update({
            "SM": SM,
            "HM_pole1": hm_values[0],
            "HM_pole2": hm_values[1],
            "HM_common": hm_common,
            "HM_unit": hm_unit,
            "E5_residues_modulus": e5_residues,
            "s1F": s1F,
            "s1F_unit": s1F_unit,
            "E6_residue_modulus": e6_residue,
            "pass": (hm_common and hm_unit and s1F_unit and
                     e5_residues == [0, 0] and e6_residue == 0),
        })
    passed = (residue == 0 and W1_unit and W2_unit and e5e6["pass"])
    values = {"r3": r3, "A1": A1, "A2": A2, "W1": W1, "W2": W2}
    return {
        "schema": "d43-e5-necessary-template-gate-v1",
        "modulus": modulus,
        "values": values,
        "values_sha256": sha256_json(values),
        "first_term_modulus": first_term,
        "second_term_modulus": second_term,
        "E_residue_modulus": residue,
        "E_zero": residue == 0,
        "W1_unit": W1_unit,
        "W2_unit": W2_unit,
        "eliminated_E5_E6_witness_replay": e5e6,
        "pass": passed,
        "scope": (
            "necessary finite E/W condition plus eliminated E5/E6 tie "
            "witnesses only; no inverse-row, parked, template, or D25 "
            "replay"),
    }


def tail_census() -> dict:
    dense_per_family = len([r for r in range(6, 43) if r != 10])
    even_per_family = len([r for r in range(6, 43, 2) if r != 10])
    nominal_tails = 4 * dense_per_family + 2 * even_per_family
    effective_tails = nominal_tails - len(DEAD_TAIL_LABELS)
    result = {
        "dense_families": 4,
        "dense_tails_per_family": dense_per_family,
        "even_families": 2,
        "even_tails_per_family": even_per_family,
        "nominal_tail_coordinates": nominal_tails,
        "dead_tail_coordinates": len(DEAD_TAIL_LABELS),
        "effective_tail_coordinates": effective_tails,
        "fixed_coordinates": len(FIXED_COORDS),
        "x_side_coordinates": 2,
        "nominal_total_coordinates": nominal_tails + len(FIXED_COORDS) + 2,
        "essential_total_coordinates": effective_tails + len(FIXED_COORDS) + 2,
    }
    if result != {
            "dense_families": 4, "dense_tails_per_family": 36,
            "even_families": 2, "even_tails_per_family": 18,
            "nominal_tail_coordinates": 180, "dead_tail_coordinates": 8,
            "effective_tail_coordinates": 172, "fixed_coordinates": 8,
            "x_side_coordinates": 2, "nominal_total_coordinates": 190,
            "essential_total_coordinates": 182}:
        raise AssertionError("D43 coordinate census drift: %r" % result)
    return result


def structural_dead_tail_gate(row_bands: Sequence[int]) -> dict:
    """Exact truncation/parity reason the eight high odd tails are absent.

    Every selected t-band is even.  In the source factors, every fixed
    t-offset is even except W/HW at offset 5; all other odd variable offsets
    are at least 7.  A monomial containing r=39 or 41 is either odd (hence
    unselected) or needs another odd offset >=5, putting it above band 42.
    """
    if not row_bands or max(row_bands) != 42:
        raise ValueError("expected the complete selected D43 band window")
    if any(band % 2 for band in row_bands):
        raise ValueError("selected row registry contains an odd band")
    minimum_other_odd_offset = 5
    inequalities = {str(r): r + minimum_other_odd_offset
                    for r in (39, 41)}
    if not all(value > 42 for value in inequalities.values()):
        raise AssertionError("dead-tail cutoff proof failed")
    return {
        "selected_rows": len(row_bands),
        "selected_bands_are_even": True,
        "maximum_selected_band": 42,
        "minimum_other_odd_offset": minimum_other_odd_offset,
        "dead_plus_minimum_odd": inequalities,
        "conclusion": "r=39,41 dense-family tails are absent identically from every selected source row",
    }


def source_rows_with_x(context: Mapping, coordinates: Mapping[str, int],
                       frame: INTEGRAL.RootFrame, modulus: int) -> list[int]:
    """Evaluate all 184 pristine rows, including the exact x-side value."""
    C = context["C"]
    point = {"tails": {family: {} for family in FAMILIES}, "fixed": {}}
    for label in context["essential_labels"]:
        value = int(coordinates[coordinate_key(label)]) % modulus
        if label[0] in FAMILIES:
            if value:
                point["tails"][label[0]][int(label[1])] = value
        elif label[0] == "FIX":
            point["fixed"][label[1]] = value
    point["fixed"].update({
        "uf30": 0,
        "A1": frame.A1 % modulus,
        "A2": frame.A2 % modulus,
        "r3": frame.r3 % modulus,
        "h32": frame.h % modulus,
        "HW1": frame.h * point["fixed"]["W1"] % modulus,
        "HW2": frame.h * point["fixed"]["W2"] % modulus,
    })
    alpha = int(coordinates["X:alpha"]) % modulus
    beta = int(coordinates["X:beta"]) % modulus
    values = C.source_rows(point, frame.zeta42 % modulus, modulus)
    inverse_2 = pow(2, -1, modulus)
    sm = pow(7, 12, modulus) * pow(inverse_2, 6, modulus) % modulus
    gm = -pow(7, 18, modulus) * pow(inverse_2, 9, modulus) % modulus
    combination = (3 * alpha - 2 * beta) % modulus
    for index, (eta_degree, row_index) in enumerate(C.X.ROWS_CANON):
        band = C.X.S30[eta_degree] + 6 * row_index
        if band == 42 and eta_degree in P4P1:
            values[index] = (values[index] + 42 * sm * gm
                             * P4P1[eta_degree] * combination) % modulus
    if len(values) != 184:
        raise AssertionError("source evaluator row count drift")
    return values


def _initial_coordinates(point: Mapping, alpha: int, beta: int,
                         labels: Sequence, prime: int) -> dict[str, int]:
    result = {}
    for label in labels:
        if label[0] in FAMILIES:
            value = point["tails"][label[0]].get(int(label[1]), 0)
        elif label[0] == "FIX":
            value = point["fixed"][label[1]]
        elif label == ("X", "alpha"):
            value = alpha
        elif label == ("X", "beta"):
            value = beta
        else:
            raise AssertionError("unknown source label %r" % (label,))
        result[coordinate_key(label)] = int(value) % prime
    return result


def _dependency_hashes(certificate_path: str, p2_reference_path: str) -> dict:
    # Complete local import/data closure of prepare_d43_context().  The AWS
    # payload manifest seals the same files; including them here also makes a
    # resumed state fail closed if any inherited reconstruction dependency
    # changes while preserving the top-level adapter bytes.
    module_names = (
        "d25_eplus.py", "d25_reduce.py", "d43_char0_lift.py",
        "d43_common_integral_emitter.py", "d43_family2.py",
        "d43_full_family.py", "d43_graph_witness.py",
        "d43_nf_certificate.py", "d43_raw_point_system.py",
        "directionb_compress.py", "directionb_residual32_emit.py",
        "directionb_strike.py", "directionb_window.py", "eplus43.py",
        "eplus_certify.py", "fastelim.py", "r1_experiment.py",
        "r1_fullcore.py", "valuation_e.py", "valuation_e2.py",
    )
    paths = {"adapter": os.path.abspath(__file__)}
    paths.update({"module:%s" % name: os.path.join(HERE, name)
                  for name in module_names})
    paths.update({
        "data:d23_atlas_p105337.json": os.path.join(
            HERE, "d23_atlas_p105337.json"),
        "data:directionb_tails_D21.pkl": os.path.join(
            HERE, "..", "directionb_tails_D21.pkl"),
        "certificate": os.path.abspath(certificate_path),
        "p2_reference": os.path.abspath(p2_reference_path),
    })
    return {name: {"path": path, "sha256": sha256_path(path)}
            for name, path in paths.items()}


def prepare_d43_context(certificate_path: str, p2_reference_path: str,
                        prime: int = PRIME) -> dict:
    if prime != PRIME:
        raise ValueError("this registered diagnostic is fixed at p=105337")
    try:
        import d43_char0_lift as C
    except ModuleNotFoundError as error:
        if error.name == "numpy":
            raise RuntimeError("D43 preflight requires a Python environment with NumPy") from error
        raise

    with open(certificate_path, encoding="utf-8") as handle:
        certificate = json.load(handle)
    with open(p2_reference_path, encoding="utf-8") as handle:
        p2_reference = json.load(handle)
    if int(certificate["prime"]) != prime:
        raise ValueError("certificate prime mismatch")

    parked = certificate["point"]["parked_28"]
    external = certificate["point"]["graph_156"]
    point, env, alpha, beta, _provenance, _diag = C.GW.build_operator_point(
        prime, parked, external)
    registered = INTEGRAL.REGISTERED_FRAMES[prime]
    root_point = C.FC.radical_point(prime)
    observed = INTEGRAL.RootFrame(root_point["z"], root_point["r3"],
                                  env["A1"], env["A2"], env["h1"])
    if observed != registered or env["h1"] != env["h2"]:
        raise ValueError("registered a00pp radical frame drift")
    INTEGRAL.validate_registered_prime(prime, observed)
    if point["fixed"].get("uf30", 0) % prime:
        raise ValueError("this source lane requires the literal uf30=0 pin")
    for label in DEAD_TAIL_LABELS:
        if point["tails"][label[0]].get(label[1], 0) % prime:
            raise ValueError("dead nominal coordinate is nonzero at base point: %r" % (label,))

    jacobian, labels, engine_hash = C.source_jacobian(point, prime)
    if len(jacobian) != 184 or len(labels) != 190:
        raise AssertionError("nominal D43 source shape drift")
    label_index = {label: index for index, label in enumerate(labels)}
    if set(DEAD_TAIL_LABELS) - set(label_index):
        raise AssertionError("dead-coordinate registry drift")
    dead_nonzeros = {
        str(label): sum(bool(row[label_index[label]]) for row in jacobian)
        for label in DEAD_TAIL_LABELS
    }
    if any(dead_nonzeros.values()):
        raise AssertionError("purported dead D43 columns are not zero: %r" % dead_nonzeros)
    essential_labels = [label for label in labels
                        if label not in DEAD_TAIL_LABELS]
    essential_columns = [label_index[label] for label in essential_labels]
    essential_jacobian = [[row[column] for column in essential_columns]
                          for row in jacobian]
    census = tail_census()
    if len(essential_labels) != census["essential_total_coordinates"]:
        raise AssertionError("essential coordinate count drift")
    factor = factor_matrix(essential_jacobian, prime)
    if factor["rank"] != 129:
        raise AssertionError("source Jacobian rank drift: %d != 129" % factor["rank"])
    if len(factor["left_cokernel"]) != 55:
        raise AssertionError("left-cokernel dimension drift")

    row_bands = [C.X.S30[a] + 6 * j for a, j in C.X.ROWS_CANON]
    dead_gate = structural_dead_tail_gate(row_bands)
    coordinates = _initial_coordinates(point, alpha, beta,
                                       essential_labels, prime)
    base_values = source_rows_with_x(
        {"C": C, "essential_labels": essential_labels},
        coordinates, registered, prime)
    if any(base_values):
        raise AssertionError("registered source point is not zero mod p")
    base_template_gate = template_relation_gate(
        coordinates, registered, prime)
    if not base_template_gate["pass"]:
        raise AssertionError(
            "registered source point fails the necessary E/W template gate")

    # Exact x-side value formula is checked against the independent dual-jet
    # operator at the base point for both coordinate basis vectors.
    zeta_powers = [pow(registered.zeta42, exponent, prime)
                   for exponent in range(42)]
    x_crosschecks = {}
    for name, test_alpha, test_beta in (("alpha", 1, 0),
                                        ("beta", 0, 1)):
        trial = dict(coordinates)
        trial["X:alpha"] = test_alpha
        trial["X:beta"] = test_beta
        got = source_rows_with_x(
            {"C": C, "essential_labels": essential_labels},
            trial, registered, prime)
        operator, _aux = C.X.build_operator(
            point, prime, test_alpha, test_beta, Z=zeta_powers)
        expected = [int(operator.V[a][C.X.S30[a] + 6 * j]) % prime
                    for a, j in C.X.ROWS_CANON]
        if got != expected:
            raise AssertionError("x-side exact evaluator mismatch: %s" % name)
        x_crosschecks[name] = sha256_json(got)

    # A perturbed-y control checks that the formula is an exact value law,
    # not merely the two x tangent columns at the banked point.  Since U_f
    # and U_g first differ from 1 in slot 42, every slot-42 x term sees only
    # the slot-0 constants S_M,G_M; alpha*beta begins in slot 84.
    perturbed_point = {
        "tails": {family: dict(point["tails"][family])
                  for family in FAMILIES},
        "fixed": dict(point["fixed"]),
    }
    perturbed_coordinates = dict(coordinates)
    perturbations = (("tf1", 6, 17), ("tg02", 12, 23),
                     ("FIX", "W1", 29), ("FIX", "uf18", 31))
    for family, index, increment in perturbations:
        key = coordinate_key((family, index))
        perturbed_coordinates[key] = (
            perturbed_coordinates[key] + increment) % prime
        if family in FAMILIES:
            perturbed_point["tails"][family][index] = \
                perturbed_coordinates[key]
        else:
            perturbed_point["fixed"][index] = perturbed_coordinates[key]
    perturbed_point["fixed"]["HW1"] = (
        registered.h * perturbed_point["fixed"]["W1"]) % prime
    perturbed_coordinates["X:alpha"] = 37
    perturbed_coordinates["X:beta"] = 41
    got = source_rows_with_x(
        {"C": C, "essential_labels": essential_labels},
        perturbed_coordinates, registered, prime)
    operator, _aux = C.X.build_operator(
        perturbed_point, prime, 37, 41, Z=zeta_powers)
    expected = [int(operator.V[a][C.X.S30[a] + 6 * j]) % prime
                for a, j in C.X.ROWS_CANON]
    if got != expected:
        raise AssertionError("x-side exact evaluator mismatch at perturbed y")
    x_crosschecks["perturbed_y_alpha37_beta41"] = sha256_json(got)

    represented = p2_reference["rank_slices"][
        "represented_182_columns_after_dropping_8_reconstructed_tails"]
    expected_dropped = {str(label) for label in DEAD_TAIL_LABELS}
    if set(represented["dropped"]) != expected_dropped:
        raise ValueError("p^2 reference dropped-coordinate drift")
    if (int(represented["rank"]) != 129 or
            int(represented["augmented_rank"]) != 129 or
            not represented["correction_solvable"]):
        raise ValueError("p^2 reference rank/solvability drift")
    expected_p2_correction = represented["p2_replay"]["correction_sha256"]
    expected_p2_rhs = p2_reference["source_model"][
        "minus_F_over_p_sha256"]
    expected_p2_frame = INTEGRAL.RootFrame(
        p2_reference["coefficient_ring"]["roots_mod_p2"]["zeta42"],
        p2_reference["coefficient_ring"]["roots_mod_p2"]["r3"],
        p2_reference["coefficient_ring"]["roots_mod_p2"]["A1"],
        p2_reference["coefficient_ring"]["roots_mod_p2"]["A2"],
        p2_reference["coefficient_ring"]["roots_mod_p2"]["h32"])
    if expected_p2_frame != INTEGRAL.REGISTERED_P2_FRAME_105337:
        raise ValueError("committed p^2 radical frame drift")
    if expected_p2_correction != REGISTERED_P2_CORRECTION_SHA256:
        raise ValueError("committed p^2 correction digest drift")
    if expected_p2_rhs != REGISTERED_P2_RHS_SHA256:
        raise ValueError("committed p^2 RHS digest drift")
    if sha256_json(_frame_dict(expected_p2_frame)) != \
            REGISTERED_P2_FRAME_SHA256:
        raise ValueError("committed p^2 frame digest drift")

    context = {
        "C": C,
        "prime": prime,
        "initial_frame": registered,
        "initial_coordinates": coordinates,
        "essential_labels": essential_labels,
        "essential_jacobian": essential_jacobian,
        "factor": factor,
        "expected_p2_correction_sha256": expected_p2_correction,
        "expected_p2_rhs_sha256": expected_p2_rhs,
        "expected_p2_point_sha256": REGISTERED_P2_POINT_SHA256,
        "expected_p2_frame_sha256": REGISTERED_P2_FRAME_SHA256,
        "expected_p2_frame": expected_p2_frame,
        "dependency_hashes": _dependency_hashes(certificate_path,
                                                  p2_reference_path),
        "invariants": {
            "source_rows": 184,
            "nominal_source_coordinates": 190,
            "coordinate_census": census,
            "dead_labels": [coordinate_label_json(label)
                            for label in DEAD_TAIL_LABELS],
            "dead_columns_nonzero_entries": dead_nonzeros,
            "dead_tail_structural_gate": dead_gate,
            "essential_labels_sha256": sha256_json(
                [coordinate_label_json(label) for label in essential_labels]),
            "source_row_labels_sha256": sha256_json(
                [[a, j, C.X.S30[a] + 6 * j]
                 for a, j in C.X.ROWS_CANON]),
            "source_jacobian_rank_mod_p": factor["rank"],
            "source_jacobian_sha256": factor["matrix_sha256"],
            "source_jacobian_rref_sha256": factor["rref_sha256"],
            "left_cokernel_dimension": len(factor["left_cokernel"]),
            "left_cokernel_basis_sha256": factor["left_cokernel_sha256"],
            "valuation_e2_sha256": engine_hash,
            "base_point_coordinates_sha256": sha256_json(coordinates),
            "base_rows_sha256": sha256_json(base_values),
            "base_template_relation_gate": base_template_gate,
            "x_side_crosschecks": x_crosschecks,
        },
    }
    return context


def _semantic_fingerprint(context: Mapping) -> dict:
    invariants = context["invariants"]
    return {
        # Paths may change when a sealed state is copied to another AWS
        # worker.  Content hashes, not host-specific absolute paths, are the
        # semantic resume gate.
        "dependency_sha256": {
            name: item["sha256"]
            for name, item in context["dependency_hashes"].items()
        },
        "essential_labels_sha256": invariants["essential_labels_sha256"],
        "source_row_labels_sha256": invariants["source_row_labels_sha256"],
        "source_jacobian_sha256": invariants["source_jacobian_sha256"],
        "source_jacobian_rref_sha256": invariants[
            "source_jacobian_rref_sha256"],
        "left_cokernel_basis_sha256": invariants[
            "left_cokernel_basis_sha256"],
        "base_point_coordinates_sha256": invariants[
            "base_point_coordinates_sha256"],
    }


def _atomic_json(path: str, value) -> None:
    directory = os.path.dirname(os.path.abspath(path))
    os.makedirs(directory, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=".d43-hensel-",
                                               suffix=".tmp", dir=directory)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            json.dump(value, handle, indent=1, sort_keys=True)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
        directory_fd = os.open(directory, os.O_RDONLY)
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def write_state(path: str, payload: Mapping) -> str:
    payload = dict(payload)
    envelope = {"payload": payload, "payload_sha256": sha256_json(payload)}
    _atomic_json(path, envelope)
    return envelope["payload_sha256"]


def load_state(path: str) -> dict:
    with open(path, encoding="utf-8") as handle:
        envelope = json.load(handle)
    if set(envelope) != {"payload", "payload_sha256"}:
        raise ValueError("bad state envelope")
    observed = sha256_json(envelope["payload"])
    if observed != envelope["payload_sha256"]:
        raise ValueError("state payload authentication failed")
    return envelope["payload"]


@contextlib.contextmanager
def exclusive_state_lock(path: str):
    """Fail rather than race another writer of the same state path."""
    lock_path = os.path.abspath(path) + ".lock"
    os.makedirs(os.path.dirname(lock_path), exist_ok=True)
    descriptor = os.open(lock_path, os.O_RDWR | os.O_CREAT, 0o600)
    try:
        try:
            fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise RuntimeError("state path is already locked: %s" % path) from error
        yield lock_path
    finally:
        fcntl.flock(descriptor, fcntl.LOCK_UN)
        os.close(descriptor)


def _registered_p2_anchor(context: Mapping) -> dict:
    return {
        "prime": context["prime"],
        "target_exponent": 2,
        "minus_F_over_p_sha256": context["expected_p2_rhs_sha256"],
        "correction_sha256": context["expected_p2_correction_sha256"],
        "corrected_point_sha256": context["expected_p2_point_sha256"],
        "root_frame_sha256": context["expected_p2_frame_sha256"],
        "necessary_template_relation_gate_sha256":
            REGISTERED_P2_TEMPLATE_GATE_SHA256,
    }


def _initial_payload(context: Mapping) -> dict:
    template_gate = template_relation_gate(
        context["initial_coordinates"], context["initial_frame"],
        context["prime"])
    if not template_gate["pass"]:
        raise ValueError("registered initial point fails the necessary E/W gate")
    return {
        "schema": SCHEMA,
        "status": STATUS_READY,
        "scope": SCOPE,
        "prime": context["prime"],
        "exponent": 1,
        "modulus": context["prime"],
        "root_frame": _frame_dict(context["initial_frame"]),
        "coordinates": dict(context["initial_coordinates"]),
        "template_relation_gate": template_gate,
        "history": [],
        "history_sha256": INITIAL_HISTORY_SHA256,
        "semantic_fingerprint": _semantic_fingerprint(context),
        "invariants": context["invariants"],
        "p2_anchor": _registered_p2_anchor(context),
        "branch_policy": dict(BRANCH_POLICY),
        "claims": registered_claims(),
    }


def _frame_from_payload(payload: Mapping) -> INTEGRAL.RootFrame:
    frame = payload["root_frame"]
    return INTEGRAL.RootFrame(frame["zeta42"], frame["r3"], frame["A1"],
                              frame["A2"], frame["h"])


def _seal_history_record(payload: Mapping, record: Mapping):
    previous = payload["history_sha256"]
    core = dict(record)
    core["previous_history_sha256"] = previous
    record_sha256 = sha256_json(core)
    sealed = dict(core)
    sealed["record_sha256"] = record_sha256
    prefix = sha256_json({"previous_history_sha256": previous,
                          "record_sha256": record_sha256})
    sealed["history_prefix_sha256"] = prefix
    return sealed, prefix


def _first_difference(left, right, path="payload"):
    if type(left) is not type(right):
        return "%s type %s != %s" % (path, type(left).__name__,
                                      type(right).__name__)
    if isinstance(left, dict):
        if set(left) != set(right):
            return "%s keys %r != %r" % (path, sorted(left), sorted(right))
        for key in sorted(left):
            difference = _first_difference(left[key], right[key],
                                           "%s.%s" % (path, key))
            if difference:
                return difference
        return None
    if isinstance(left, list):
        if len(left) != len(right):
            return "%s length %d != %d" % (path, len(left), len(right))
        for index, (a, b) in enumerate(zip(left, right)):
            difference = _first_difference(a, b, "%s[%d]" % (path, index))
            if difference:
                return difference
        return None
    return None if left == right else "%s value mismatch" % path


def _cheap_state_shape_gate(payload: Mapping, context: Mapping) -> None:
    if not isinstance(payload, dict):
        raise ValueError("state payload must be a dictionary")
    if payload.get("schema") != SCHEMA:
        raise ValueError("state schema mismatch")
    if payload.get("status") not in (STATUS_READY, STATUS_FINITE,
                                      STATUS_OBSTRUCTED,
                                      STATUS_TEMPLATE_FAILED):
        raise ValueError("state status is not registered")
    if payload.get("scope") != SCOPE:
        raise ValueError("state scope drift")
    if payload.get("branch_policy") != BRANCH_POLICY:
        raise ValueError("state branch policy drift")
    if payload.get("claims") != registered_claims():
        raise ValueError("state claims firewall drift")
    if int(payload.get("prime", 0)) != context["prime"]:
        raise ValueError("state prime mismatch")
    exponent = payload.get("exponent")
    if isinstance(exponent, bool) or not isinstance(exponent, int) or \
            exponent < 1:
        raise ValueError("state exponent is not canonical")
    modulus = context["prime"] ** exponent
    if payload.get("modulus") != modulus:
        raise ValueError("state modulus mismatch")
    if payload.get("semantic_fingerprint") != _semantic_fingerprint(context):
        raise ValueError("state semantic fingerprint drift")
    if payload.get("invariants") != context["invariants"]:
        raise ValueError("state invariant block drift")
    if payload.get("p2_anchor") != _registered_p2_anchor(context):
        raise ValueError("state p^2 anchor drift")
    expected_keys = {coordinate_key(label)
                     for label in context["essential_labels"]}
    coordinates = payload.get("coordinates")
    if not isinstance(coordinates, dict) or set(coordinates) != expected_keys:
        raise ValueError("state coordinate registry mismatch")
    for key, value in coordinates.items():
        if isinstance(value, bool) or not isinstance(value, int) or \
                not 0 <= value < modulus:
            raise ValueError("noncanonical coordinate %s" % key)
    frame = payload.get("root_frame")
    if not isinstance(frame, dict) or set(frame) != {
            "zeta42", "r3", "A1", "A2", "h"}:
        raise ValueError("state root-frame registry mismatch")
    for key, value in frame.items():
        if isinstance(value, bool) or not isinstance(value, int) or \
                not 0 <= value < modulus:
            raise ValueError("noncanonical root-frame value %s" % key)
    observed_template_gate = template_relation_gate(
        coordinates, _frame_from_payload(payload), modulus)
    if payload.get("template_relation_gate") != observed_template_gate:
        raise ValueError("state necessary E/W template gate drift")
    if payload["status"] in (STATUS_READY, STATUS_FINITE) and not \
            observed_template_gate["pass"]:
        raise ValueError("live state fails the necessary E/W template gate")
    if payload["status"] == STATUS_TEMPLATE_FAILED and \
            observed_template_gate["pass"]:
        raise ValueError("template-gate failure status has a passing gate")
    if not isinstance(payload.get("history"), list):
        raise ValueError("state history is not a list")
    history_sha256 = payload.get("history_sha256")
    if not isinstance(history_sha256, str) or len(history_sha256) != 64:
        raise ValueError("state history digest malformed")


def replay_semantic_chain(payload: Mapping, context: Mapping) -> dict:
    """Reconstruct the complete registered branch and compare exactly."""
    _cheap_state_shape_gate(payload, context)
    exponent = payload["exponent"]
    status = payload["status"]
    if exponent == 1 and status == STATUS_FINITE:
        raise ValueError("finite-lift status is invalid at exponent 1")
    if exponent == 1 and status == STATUS_TEMPLATE_FAILED:
        raise ValueError("template-gate failure status is invalid at exponent 1")
    if exponent > 1 and status == STATUS_READY:
        raise ValueError("mod-p-ready status is invalid above exponent 1")

    expected = _initial_payload(context)
    for target in range(2, exponent + 1):
        expected = lift_one_point_digit(context, expected)
        if expected["status"] in (STATUS_OBSTRUCTED,
                                   STATUS_TEMPLATE_FAILED) and \
                target < exponent:
            raise ValueError(
                "registered chain terminates before stored exponent %d" % target)
    if status == STATUS_OBSTRUCTED:
        expected = lift_one_point_digit(context, expected)
        if expected["status"] != STATUS_OBSTRUCTED:
            raise ValueError("stored obstruction is not reproduced")
    difference = _first_difference(payload, expected)
    if difference:
        raise ValueError("semantic state-chain replay mismatch: %s" % difference)
    return expected


def validate_resume_payload(payload: Mapping, context: Mapping) -> None:
    replay_semantic_chain(payload, context)


def lift_one_point_digit(context: Mapping, payload: Mapping) -> dict:
    if payload["status"] not in (STATUS_READY, STATUS_FINITE):
        raise ValueError("only a live deterministic branch can be extended")
    prime = context["prime"]
    exponent = int(payload["exponent"])
    step = prime ** exponent
    modulus = step * prime
    old_frame = _frame_from_payload(payload)
    input_template_gate = template_relation_gate(
        payload["coordinates"], old_frame, step)
    if input_template_gate != payload.get("template_relation_gate") or \
            not input_template_gate["pass"]:
        raise ValueError("input state fails authenticated necessary E/W gate")
    old_rows = source_rows_with_x(context, payload["coordinates"],
                                  old_frame, step)
    if any(old_rows):
        raise ValueError("input point fails before digit %d" % exponent)

    frame, root_meta = lift_root_frame_digit(old_frame, prime, exponent)
    pre_values = source_rows_with_x(context, payload["coordinates"],
                                    frame, modulus)
    if any(value % step for value in pre_values):
        raise AssertionError("coefficient lift broke divisibility by prior modulus")
    rhs = [(-value // step) % prime for value in pre_values]
    solve = solve_factored(context["factor"], rhs)
    digit_record = {
        "from_exponent": exponent,
        "to_exponent": exponent + 1,
        "input_modulus": step,
        "input_root_frame_sha256": sha256_json(_frame_dict(old_frame)),
        "input_coordinate_point_sha256": sha256_json(payload["coordinates"]),
        "input_template_relation_gate": input_template_gate,
        "prior_rows_sha256": sha256_json(old_rows),
        "coefficient_lift": root_meta,
        "pre_correction_values_sha256": sha256_json(pre_values),
        "nonzero_pre_correction_quotients": sum(bool(value) for value in rhs),
        "minus_F_over_p_power_sha256": sha256_json(rhs),
        "linear_system": {key: value for key, value in solve.items()
                          if key != "solution"},
    }
    updated = dict(payload)
    history = list(payload["history"])
    if not solve["solvable"]:
        digit_record["result"] = STATUS_OBSTRUCTED
        digit_record["attempted_root_frame_sha256"] = root_meta[
            "frame_sha256"]
        digit_record, history_sha256 = _seal_history_record(
            payload, digit_record)
        history.append(digit_record)
        updated.update({
            "status": STATUS_OBSTRUCTED,
            "obstruction_attempted_to_exponent": exponent + 1,
            "history": history,
            "history_sha256": history_sha256,
            "obstruction_scope": (
                "No lift of this specific p^%d point to p^%d exists in "
                "the declared essential source ambient. Alternative earlier "
                "kernel digits are not excluded." % (exponent, exponent + 1)),
        })
        return updated

    correction = solve["solution"]
    direct = [sum(row[column] * correction[column]
                  for column in range(len(correction))) % prime
              for row in context["essential_jacobian"]]
    if direct != rhs:
        raise AssertionError("Newton correction fails J*delta=rhs")
    coordinates = apply_digits(payload["coordinates"],
                               context["essential_labels"], correction,
                               step, modulus)
    replay = source_rows_with_x(context, coordinates, frame, modulus)
    if any(replay):
        raise AssertionError("post-correction 184-row replay failed")
    output_template_gate = template_relation_gate(
        coordinates, frame, modulus)
    digit_result = ("SOLVABLE_AND_REPLAYED" if output_template_gate["pass"]
                    else STATUS_TEMPLATE_FAILED)
    digit_record.update({
        "result": digit_result,
        "correction_sha256": solve["solution_sha256"],
        "nonzero_correction_coordinates": solve[
            "nonzero_solution_coordinates"],
        "coordinate_point_sha256": sha256_json(coordinates),
        "replay_rows_sha256": sha256_json(replay),
        "all_184_rows_zero_mod_target": True,
        "output_template_relation_gate": output_template_gate,
    })
    if exponent == 1:
        if solve["rhs_sha256"] != context["expected_p2_rhs_sha256"]:
            raise AssertionError("reconstructed p^2 RHS hash mismatch")
        if solve["solution_sha256"] != context[
                "expected_p2_correction_sha256"]:
            raise AssertionError("reconstructed p^2 correction hash mismatch")
        if frame != context["expected_p2_frame"]:
            raise AssertionError("reconstructed p^2 radical frame mismatch")
        if sha256_json(coordinates) != context["expected_p2_point_sha256"]:
            raise AssertionError("reconstructed p^2 point hash mismatch")
        if coordinates["FIX:W1"] != REGISTERED_P2_W1 or \
                coordinates["FIX:W2"] != REGISTERED_P2_W2:
            raise AssertionError("reconstructed p^2 W coordinates mismatch")
        if sha256_json(output_template_gate) != \
                REGISTERED_P2_TEMPLATE_GATE_SHA256:
            raise AssertionError(
                "reconstructed p^2 necessary E/W gate hash mismatch")
        digit_record["committed_p2_anchor"] = _registered_p2_anchor(context)
    digit_record, history_sha256 = _seal_history_record(payload, digit_record)
    history.append(digit_record)
    if output_template_gate["pass"]:
        next_status = STATUS_FINITE
        finite_conclusion = (
            "A compatible point of the raw 184-row Euler/J-source "
            "truncation exists modulo p^%d along this deterministic "
            "branch and passes the necessary finite E/W gate; this is "
            "not D43 template-branch evidence and no infinite or "
            "characteristic-zero conclusion is licensed."
            % (exponent + 1))
    else:
        next_status = STATUS_TEMPLATE_FAILED
        finite_conclusion = (
            "The raw 184-row Euler/J-source correction exists modulo "
            "p^%d, but it fails the necessary E/W template gate. The "
            "registered raw-source chain terminates here and licenses no "
            "template-conform or branch-survival interpretation."
            % (exponent + 1))
    updated.update({
        "status": next_status,
        "exponent": exponent + 1,
        "modulus": modulus,
        "root_frame": _frame_dict(frame),
        "coordinates": coordinates,
        "template_relation_gate": output_template_gate,
        "history": history,
        "history_sha256": history_sha256,
        "finite_conclusion": finite_conclusion,
    })
    return updated


def _is_sha256(value) -> bool:
    return isinstance(value, str) and len(value) == 64 and all(
        character in "0123456789abcdef" for character in value)


def validate_aws_lane_authorization(target_exponent: int, state_path: str,
                                    report_path: str | None) -> dict | None:
    """Require the route-specific supervisor for every p^3+ request."""
    if target_exponent <= 2:
        return None
    if target_exponent not in AWS_TARGET_TAGS:
        raise RuntimeError("AWS route permits only target exponents 16 and 64")
    marker_path = os.environ.get("JC2_D43_HENSEL_AWS_AUTH", "")
    expected_marker_sha = os.environ.get(
        "JC2_D43_HENSEL_AWS_AUTH_SHA256", "")
    if not marker_path or not _is_sha256(expected_marker_sha):
        raise RuntimeError("p^3+ is forbidden without an authenticated AWS lane marker")
    marker_path = os.path.abspath(marker_path)
    if sha256_path(marker_path) != expected_marker_sha:
        raise RuntimeError("AWS lane marker file hash mismatch")
    marker = load_state(marker_path)
    required_keys = {
        "schema", "target_exponent", "lane_tag", "job_id", "hostname",
        "hostname_sha256", "instance_id", "instance_type",
        "input_manifest_sha256", "prereg_sha256", "runner_sha256",
        "job_identity_sha256", "supervisor_pid", "state_path",
        "report_path", "claims_forbidden_sha256",
    }
    if set(marker) != required_keys:
        raise RuntimeError("AWS lane marker schema fields drift")
    if marker["schema"] != AWS_AUTH_SCHEMA:
        raise RuntimeError("AWS lane marker schema mismatch")
    if platform.system() != "Linux":
        raise RuntimeError("p^3+ source lift is forbidden outside Linux")
    try:
        vendor = open("/sys/class/dmi/id/sys_vendor", encoding="utf-8").read().strip()
    except OSError as error:
        raise RuntimeError("cannot verify Amazon EC2 DMI identity") from error
    if vendor != "Amazon EC2":
        raise RuntimeError("p^3+ source lift is forbidden outside Amazon EC2")
    hostname = socket.gethostname()
    if marker["hostname"] != hostname or marker["hostname_sha256"] != \
            hashlib.sha256(hostname.encode()).hexdigest():
        raise RuntimeError("AWS lane hostname identity mismatch")
    if marker["target_exponent"] != target_exponent or \
            marker["lane_tag"] != AWS_TARGET_TAGS[target_exponent]:
        raise RuntimeError("AWS lane target/tag mismatch")
    if marker["runner_sha256"] != sha256_path(__file__):
        raise RuntimeError("AWS lane runner hash mismatch")
    if marker["state_path"] != os.path.abspath(state_path) or \
            marker["report_path"] != os.path.abspath(report_path or ""):
        raise RuntimeError("AWS lane durable-path mismatch")
    if marker["supervisor_pid"] != os.getppid():
        raise RuntimeError("AWS lane supervisor parent mismatch")
    for key in ("hostname_sha256", "input_manifest_sha256", "prereg_sha256",
                "runner_sha256", "job_identity_sha256",
                "claims_forbidden_sha256"):
        if not _is_sha256(marker[key]):
            raise RuntimeError("AWS lane marker has malformed %s" % key)
    if marker["claims_forbidden_sha256"] != sha256_json(
            list(FORBIDDEN_CLAIMS)):
        raise RuntimeError("AWS lane claims firewall mismatch")
    return marker


def run(target_exponent: int, state_path: str, certificate_path: str,
        p2_reference_path: str, report_path: str | None = None,
        preflight_only: bool = False,
        validate_state_only: bool = False) -> dict:
    if target_exponent < 2:
        raise ValueError("target exponent must be at least 2")
    lane = validate_aws_lane_authorization(target_exponent, state_path,
                                           report_path)
    with exclusive_state_lock(state_path):
        context = prepare_d43_context(certificate_path, p2_reference_path)
        if preflight_only:
            return {
                "status": "PREFLIGHT_PASS_NO_LIFT_RUN",
                "scope": SCOPE,
                "prime": context["prime"],
                "invariants": context["invariants"],
                "semantic_fingerprint": _semantic_fingerprint(context),
                "registered_mod_p_template_relation_gate":
                    template_relation_gate(
                        context["initial_coordinates"],
                        context["initial_frame"], context["prime"]),
                "target_exponent_not_run": target_exponent,
                "branch_policy": dict(BRANCH_POLICY),
                "claims_certified": CERTIFIED_CLAIM,
                "exact_relations_replayed": list(EXACT_RELATIONS_REPLAYED),
                "upstream_not_replayed": list(UPSTREAM_NOT_REPLAYED),
                "claims_forbidden": list(FORBIDDEN_CLAIMS),
                "aws_lane": lane,
            }

        state_existed = os.path.exists(state_path)
        if state_existed:
            payload = load_state(state_path)
            validate_resume_payload(payload, context)
        else:
            if validate_state_only:
                raise ValueError("state validation requested but state is absent")
            payload = _initial_payload(context)
            write_state(state_path, payload)

        if target_exponent == 64 and not (
                state_existed and payload["status"] == STATUS_FINITE and
                payload["exponent"] == 16):
            raise ValueError("target 64 requires an authenticated exact target-16 state")
        if int(payload["exponent"]) > target_exponent:
            raise ValueError("target exponent is below sealed state exponent")
        if validate_state_only:
            report = {
                "status": "SEMANTIC_STATE_CHAIN_VALID",
                "scope": SCOPE,
                "prime": payload["prime"],
                "validated_exponent": payload["exponent"],
                "state_payload_sha256": sha256_json(payload),
                "history_sha256": payload["history_sha256"],
                "necessary_template_relation_gate": payload[
                    "template_relation_gate"],
                "claims_certified": CERTIFIED_CLAIM,
                "exact_relations_replayed": list(EXACT_RELATIONS_REPLAYED),
                "upstream_not_replayed": list(UPSTREAM_NOT_REPLAYED),
                "claims_forbidden": list(FORBIDDEN_CLAIMS),
            }
            if report_path:
                _atomic_json(report_path, report)
            return report

        while (payload["status"] in (STATUS_READY, STATUS_FINITE) and
               int(payload["exponent"]) < target_exponent):
            payload = lift_one_point_digit(context, payload)
            state_digest = write_state(state_path, payload)
            latest = payload["history"][-1]
            print("D43 source digit: p^%d -> p^%d: %s; state %s" %
                  (latest["from_exponent"], latest["to_exponent"],
                   payload["status"], state_digest), flush=True)
        validate_resume_payload(payload, context)
        report = {
            "status": payload["status"],
            "scope": SCOPE,
            "prime": payload["prime"],
            "achieved_exponent": payload["exponent"],
            "achieved_modulus": payload["modulus"],
            "requested_exponent": target_exponent,
            "state_path": os.path.abspath(state_path),
            "state_payload_sha256": sha256_json(payload),
            "history_sha256": payload["history_sha256"],
            "semantic_chain_replay": "PASS_FROM_REGISTERED_MOD_P_STATE",
            "source_rows": 184,
            "essential_coordinates": 182,
            "jacobian_rank_mod_p": 129,
            "left_cokernel_dimension": 55,
            "necessary_template_relation_gate": payload[
                "template_relation_gate"],
            "template_gate_interpretation": (
                "E=0 and W-unit checks are necessary finite conditions "
                "only. The gate constructs and replays the algebraically "
                "eliminated HM and nonzero s1F witnesses for the corrected "
                "E5 pair and cube-form E6. It does not replay inverse rows, "
                "parked/source equivalence, the template reconstruction, "
                "or D25, and is not D43 template-branch evidence."),
            "digits_attempted": len(payload["history"]),
            "last_digit": payload["history"][-1] if payload["history"] else None,
            "branch_policy": dict(BRANCH_POLICY),
            "claims_certified": CERTIFIED_CLAIM,
            "exact_relations_replayed": list(EXACT_RELATIONS_REPLAYED),
            "upstream_not_replayed": list(UPSTREAM_NOT_REPLAYED),
            "claims_forbidden": list(FORBIDDEN_CLAIMS),
            "finite_scope_warning": (
                "Every achieved exponent is finite. It proves neither "
                "indefinite source solvability nor formal smoothness and "
                "licenses none of the forbidden claims."),
            "aws_lane": lane,
        }
        if report_path:
            _atomic_json(report_path, report)
        return report


def fixture_selftest() -> dict:
    prime = 7
    matrix = [[1, 0], [0, 1], [1, 1]]
    factor = factor_matrix(matrix, prime)
    if factor["rank"] != 2 or len(factor["left_cokernel"]) != 1:
        raise AssertionError("fixture factorization failed")
    good = solve_factored(factor, [2, 3, 5])
    bad = solve_factored(factor, [2, 3, 6])
    if not good["solvable"] or good["solution"] != [2, 3]:
        raise AssertionError("fixture compatible solve failed")
    if bad["solvable"] or bad["obstruction"]["pairing_mod_p"] == 0:
        raise AssertionError("fixture obstruction witness failed")

    root = INTEGRAL.REGISTERED_FRAMES[PRIME]
    lifted, _meta = lift_root_frame_digit(root, PRIME, 1)
    if lifted != INTEGRAL.REGISTERED_P2_FRAME_105337:
        raise AssertionError("registered p^2 frame reconstruction failed")
    census = tail_census()
    p2_template_gate = template_relation_gate(
        {"FIX:W1": REGISTERED_P2_W1, "FIX:W2": REGISTERED_P2_W2},
        lifted, PRIME ** 2)
    if not p2_template_gate["pass"] or \
            sha256_json(p2_template_gate) != \
            REGISTERED_P2_TEMPLATE_GATE_SHA256:
        raise AssertionError("registered p^2 E/E5/E6 gate failed")
    dead = structural_dead_tail_gate([6, 8, 10, 12, 14, 16, 18, 20,
                                      22, 24, 26, 28, 30, 32, 34, 36,
                                      38, 40, 42])
    return {
        "status": "PASS",
        "linear_rank": factor["rank"],
        "left_cokernel_dimension": len(factor["left_cokernel"]),
        "compatible_syndrome_zero": good["nonzero_syndrome_entries"] == 0,
        "incompatible_syndrome_nonzero": bad["nonzero_syndrome_entries"] > 0,
        "registered_p2_frame_sha256": sha256_json(_frame_dict(lifted)),
        "registered_p2_template_gate_sha256": sha256_json(
            p2_template_gate),
        "coordinate_census": census,
        "dead_tail_gate": dead,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target-exponent", type=int, default=16)
    parser.add_argument("--state", default=os.path.join(
        HERE, "d43_source_high_hensel_state_p105337.json"))
    parser.add_argument("--certificate", default=os.path.join(
        HERE, "d43_full_certificate_p105337.json"))
    parser.add_argument("--p2-reference", default=os.path.join(
        HERE, "d43_char0_lift_p105337.json"))
    parser.add_argument("--report", default=None)
    parser.add_argument("--preflight-only", action="store_true")
    parser.add_argument("--validate-state-only", action="store_true")
    parser.add_argument("--selftest", action="store_true")
    arguments = parser.parse_args()
    if arguments.selftest:
        print(json.dumps(fixture_selftest(), indent=1, sort_keys=True))
        return
    result = run(arguments.target_exponent, arguments.state,
                 arguments.certificate, arguments.p2_reference,
                 arguments.report, arguments.preflight_only,
                 arguments.validate_state_only)
    print(json.dumps(result, indent=1, sort_keys=True))


if __name__ == "__main__":
    main()
