#!/usr/bin/env python3
"""Fail-closed preflight for the sparse direct-exact D43 source route.

This tool does not lift finite-field coefficients and does not claim that
the banked normal-form presentation is a characteristic-zero source model.
It only certifies the small support and solver shape of the two banked
points, and checks that the low D21 source really is available over the
committed exact R_ext algebra.  A future exact solver must rebuild the
restricted rows from source formulas over the common radical algebra.
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import os
import pickle
import sys


HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import d43_common_integral_emitter as COMMON
import r1_experiment as R1


PRIMES = (105337, 105673)
EXPECTED_SUPPORT = (
    "tf1_57", "tf1_62", "tf1_67", "tf1_72",
    "tf2_57", "tf2_62", "tf2_67", "tf2_72",
    "tg01_62", "tg02_62", "tg1_57", "tg2_57",
    "x12", "x15", "x20", "x23", "x28", "x31", "x36", "x4",
    "x41", "x7",
)
LOW20 = ("x4", "x7", "x12", "x15", "x20", "x23", "x28",
         "x31", "x36", "x41")
LOW_SOURCE_TO_GRAPH = {
    "tf1_47": "x4", "tf1_52": "x7",
    "tf2_47": "x12", "tf2_52": "x15",
    "tg1_47": "x20", "tg1_52": "x23",
    "tg2_47": "x28", "tg2_52": "x31",
    "tg01_52": "x36", "tg02_52": "x41",
}
NEW30 = ("tf1_57", "tf2_57", "tg1_57", "tg2_57", "tf1_62",
         "tf2_62", "tg01_62", "tg02_62")
NEW40 = ("tf1_67", "tf2_67", "tf1_72", "tf2_72")


def sha256_path(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(8 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def matrix_rank(matrix, prime):
    work = [[int(value) % prime for value in row] for row in matrix]
    rank = 0
    for column in range(len(work[0]) if work else 0):
        pivot = next((i for i in range(rank, len(work))
                      if work[i][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = pow(work[rank][column], -1, prime)
        work[rank] = [value * inverse % prime for value in work[rank]]
        for i in range(len(work)):
            if i != rank and work[i][column]:
                scale = work[i][column]
                work[i] = [(left - scale * right) % prime
                           for left, right in zip(work[i], work[rank])]
        rank += 1
    return rank


def evaluate(row, assignment, prime):
    total = 0
    for monomial, coefficient in row.items():
        value = coefficient
        for name in monomial:
            value = value * assignment[name] % prime
        total = (total + value) % prime
    return total


def restrict_zero(row, retained):
    retained = set(retained)
    return {monomial: coefficient for monomial, coefficient in row.items()
            if all(name in retained for name in monomial)}


def substitute_known(row, known, retained, prime):
    retained = set(retained)
    result = {}
    for monomial, coefficient in row.items():
        value = coefficient
        remaining = []
        for name in monomial:
            if name in known:
                value = value * known[name] % prime
            elif name in retained:
                remaining.append(name)
            else:
                value = 0
                break
        if value:
            key = tuple(sorted(remaining))
            result[key] = (result.get(key, 0) + value) % prime
            if not result[key]:
                del result[key]
    return result


def _audit_exact_d21_source():
    """Audit the proposed lower support directly in exact R_ext rows."""
    path = os.path.join(ROOT, "directionb_tails_D21.pkl")
    with open(path, "rb") as handle:
        bank = pickle.load(handle)
    assert bank["D"] == 21 and 20 in bank["byk"]
    rows = []
    for eta, expression in sorted(bank["byk"][20].items()):
        row = {}
        for monomial, coefficient in expression.items():
            source_names = tuple(bank["vars"][index]
                                 for index in monomial)
            if not all(name in LOW_SOURCE_TO_GRAPH
                       for name in source_names):
                continue
            graph_monomial = tuple(LOW_SOURCE_TO_GRAPH[name]
                                   for name in source_names)
            assert graph_monomial not in row
            row[graph_monomial] = \
                COMMON.collapse_r1_ring_element(coefficient)
        if eta == 0:
            constant = COMMON.collapse_r1_ring_element(
                dict(expression).get((), R1.RZERO))
            constant[(0, 0)] = constant.get(
                (0, 0), COMMON.RadicalCoefficient()) + \
                COMMON.RadicalCoefficient.scalar(42)
            row[()] = constant
        elif () in expression:
            row[()] = COMMON.collapse_r1_ring_element(expression[()])
        assert max(map(len, row), default=0) <= 1
        rows.append({
            "eta": eta,
            "row": row,
        })
    assert len(rows) == 10

    def coefficient_mod_p(polynomial, W1, W2, prime, frame):
        value = 0
        for (power1, power2), coefficient in polynomial.items():
            term = coefficient.specialize(prime, frame)
            term = term * pow(W1, power1, prime) % prime
            term = term * pow(W2, power2, prime) % prime
            value = (value + term) % prime
        return value

    replays = []
    for prime in PRIMES:
        certificate_path = os.path.join(
            HERE, "d43_full_certificate_p%d.json" % prime)
        with open(certificate_path) as handle:
            point = json.load(handle)["point"]
        graph = point["graph_156"]
        parked = point["parked_28"]
        frame = COMMON.REGISTERED_FRAMES[prime]
        matrix = []
        constants = []
        residuals = []
        for item in rows:
            specialized = {
                monomial: coefficient_mod_p(
                    polynomial, parked["W1"], parked["W2"], prime,
                    frame)
                for monomial, polynomial in item["row"].items()
            }
            matrix.append([specialized.get((name,), 0)
                           for name in LOW20])
            constants.append(specialized.get((), 0))
            residuals.append(evaluate(specialized, graph, prime))
        rank = matrix_rank(matrix, prime)
        augmented_rank = matrix_rank(
            [row + [constant]
             for row, constant in zip(matrix, constants)], prime)
        assert not any(residuals)
        assert rank == augmented_rank == 4
        replays.append({
            "prime": prime, "residuals_zero": 10,
            "coefficient_rank": rank,
            "augmented_rank_at_banked_residue": augmented_rank,
        })

    return {
        "path": os.path.relpath(path, ROOT),
        "sha256": sha256_path(path),
        "row20_exact_rows": len(rows),
        "lower_tail_variables": list(LOW20),
        "row20_tail_monomials": sum(len(item["row"]) for item in rows),
        "row20_W_coefficient_terms": sum(
            len(polynomial)
            for item in rows for polynomial in item["row"].values()),
        "max_tail_degree": max(
            len(monomial)
            for item in rows for monomial in item["row"]),
        "modular_replays": replays,
        "meaning": "exact R_ext source rows on the proposed lower support; "
                   "no CRT reconstruction",
        "section_caveat": "both registered modular specializations have "
                          "rank 4 in 10 lower variables; this does not "
                          "certify the exact generic rank or identify the "
                          "banked D25/NF section",
    }


def audit_prime(prime):
    certificate_path = os.path.join(
        HERE, "d43_full_certificate_p%d.json" % prime)
    bank_path = os.path.join(HERE, "d43_full_pointbank_p%d.pkl" % prime)
    slice_path = os.path.join(HERE, "d43_full_slice_p%d.json" % prime)
    graph_path = os.path.join(HERE, "d43_graph_witness_p%d.json" % prime)
    floor_path = os.path.join(HERE, "d43_full_floor_p%d.json" % prime)
    with open(certificate_path) as handle:
        certificate = json.load(handle)
    with open(bank_path, "rb") as handle:
        bank = pickle.load(handle)
    with open(slice_path) as handle:
        full_slice = json.load(handle)
    with open(graph_path) as handle:
        graph_witness = json.load(handle)
    with open(floor_path) as handle:
        floor = json.load(handle)

    assert int(certificate["prime"]) == int(bank["prime"]) == prime
    parked = certificate["point"]["parked_28"]
    graph = certificate["point"]["graph_156"]
    assert graph["Xf_alpha"] == graph["Xg_beta"] == 0
    assert parked["W1"] and parked["W2"]
    assert parked["W1"] * parked["uW1"] % prime == 1
    assert parked["W2"] * parked["uW2"] % prime == 1
    assert all(not value for name, value in parked.items()
               if name not in ("W1", "W2", "uW1", "uW2"))

    assert bank["status"] == "INTERNAL / UNREVIEWED / MOD-p"
    support = tuple(sorted(name for name, value in graph.items() if value))
    assert support == EXPECTED_SUPPORT
    restricted = [restrict_zero(row, support) for row in bank["rows"]]
    live_indices = [i for i, row in enumerate(restricted) if row]
    live = [restricted[i] for i in live_indices]
    bands = collections.Counter(
        int(bank["row_labels"][i][0]) for i in live_indices)
    degrees = [max(map(len, row), default=0) for row in live]
    assert len(live) == 29 and sum(map(len, live)) == 1003
    assert bands == {20: 10, 30: 9, 40: 10}
    assert max(degrees) == 2
    point22 = {name: graph[name] for name in support}
    assert all(evaluate(row, point22, prime) == 0 for row in live)

    known = {}
    block_reports = []
    for band, new_variables in ((20, LOW20), (30, NEW30), (40, NEW40)):
        indices = [i for i in live_indices
                   if int(bank["row_labels"][i][0]) == band]
        current = [substitute_known(bank["rows"][i], known,
                                    new_variables, prime) for i in indices]
        assert all(max(map(len, row), default=0) <= 1 for row in current)
        matrix = [[row.get((name,), 0) for name in new_variables]
                  for row in current]
        constants = [row.get((), 0) for row in current]
        rank = matrix_rank(matrix, prime)
        augmented_rank = matrix_rank(
            [row + [constant] for row, constant in zip(matrix, constants)],
            prime)
        assert rank == augmented_rank == 4
        block_reports.append({
            "band": band, "rows": len(current),
            "new_variables": len(new_variables),
            "rank": rank, "augmented_rank_at_witness": augmented_rank,
            "affine_after_earlier_bands_are_substituted": True,
        })
        known.update({name: graph[name] for name in new_variables})
    assert set(known) == set(support)

    keep101 = set(full_slice["variables_retained"])
    rows101 = [restrict_zero(row, keep101) for row in bank["rows"]]
    degrees101 = [max(map(len, row), default=0) for row in rows101]
    assert len(keep101) == 101 and max(degrees101) == 6
    assert sum(degree > 1 for degree in degrees101) == 151

    raw_slice_path = os.path.join(HERE, "d43_raw_slice_p%d.json" % prime)
    with open(raw_slice_path) as handle:
        raw_slice = json.load(handle)
    keep89 = set(raw_slice["slice"]["variables_kept"])
    rows89 = [restrict_zero(row, keep89) for row in bank["rows"]]
    degrees89 = [max(map(len, row), default=0) for row in rows89]
    assert len(keep89) == 89 and max(degrees89) == 3
    assert sum(degree > 1 for degree in degrees89) == 102

    assert graph_witness["slice"]["kept_variables"] == 89
    assert graph_witness["gates"]["eplus43_floor_gate"].startswith(
        "REJECTED")
    assert floor["checks_all_pass"]
    assert floor["selected_residual_nonzero_count"] == 0

    return {
        "prime": prime,
        "inputs": {
            "certificate": os.path.relpath(certificate_path, ROOT),
            "certificate_sha256": sha256_path(certificate_path),
            "pointbank": os.path.relpath(bank_path, ROOT),
            "pointbank_sha256": sha256_path(bank_path),
        },
        "cell_origin": {
            "parked_nonchart_coordinates_zero": 24,
            "W_chart_units": True,
            "alpha_beta": [0, 0],
        },
        "floor_passing_modular_point_support": {
            "coordinates": list(support), "count": len(support),
            "restricted_rows": len(live), "terms": sum(map(len, live)),
            "max_degree": max(degrees), "live_bands": dict(bands),
            "witness_replay_zero": True,
            "presentation": "banked evaluated graph rows modulo p; not an "
                            "exact raw-source emission",
        },
        "band_triangularity": block_reports,
        "slice_101_is_not_affine": {
            "variables": len(keep101), "max_degree": max(degrees101),
            "live_rows": sum(bool(row) for row in rows101),
            "terms": sum(map(len, rows101)),
            "nonlinear_rows": sum(degree > 1 for degree in degrees101),
        },
        "slice_89_is_not_affine_in_full_banked_presentation": {
            "variables": len(keep89), "max_degree": max(degrees89),
            "live_rows": sum(bool(row) for row in rows89),
            "terms": sum(map(len, rows89)),
            "nonlinear_rows": sum(degree > 1 for degree in degrees89),
        },
        "slice_89_is_not_a_full_source_point": {
            "variables": 89,
            "source_floor": graph_witness["gates"]["eplus43_floor_gate"],
        },
    }


def run():
    reports = [audit_prime(prime) for prime in PRIMES]
    assert reports[0]["floor_passing_modular_point_support"]["coordinates"] \
        == reports[1]["floor_passing_modular_point_support"]["coordinates"]
    return {
        "status": "PREFLIGHT ONLY / EXACT RAW-SOURCE SOLVE NOT YET SEALED",
        "scope": "residue-A, B=84, a00pp, PIN42, alpha=beta=0",
        "verdict": "GO_SMALL_QUADRATIC_SOURCE_REBUILD",
        "exact_low_source": _audit_exact_d21_source(),
        "prime_audits": reports,
        "required_next_artifact": {
            "coefficient_algebra":
                "rank-432 K0 with W1,W2 retained as free polynomial "
                "coordinates during exact row emission",
            "rows":
                "rebuild all 184 pristine rows from source formulas and set "
                "the proposed support complement to zero; only an exact "
                "zero-polynomial check may reduce this to the 29 rows "
                "predicted by the banked modular presentation",
            "solver":
                "exact quadratic GB or band-compatibility elimination for "
                "the relaxed finite J scheme; replay all 184 raw source "
                "rows exactly",
            "template_bridge":
                "separately impose or prove elimination-equivalent the two "
                "individual exact E5 W quartics, chart units, relevant E6 "
                "transport/cube tie, and required nonzero HM/s1F scale "
                "conditions before claiming the intended template locus; "
                "relation E alone is insufficient",
            "forbidden_shortcuts": [
                "CRT/rational-reconstruct the point coordinates",
                "lift the modular NF coefficients",
                "treat the linear modular GB as proof that source rows are affine",
                "use the rejected 89-variable graph witness as a source point",
            ],
        },
        "claim_boundary": {
            "exact_row_emitter": None,
            "relaxed_finite_184_J_point": None,
            "intended_template_conform_point": None,
            "exact_raw_source_point": None,
            "banked_NF_presentation_equivalence": None,
            "JC2_counterexample": None,
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    report = run()
    if args.json:
        print(json.dumps(report, indent=1, sort_keys=True))
    else:
        print("D43 EXACT SPARSE SOURCE PREFLIGHT: PASS; banked modular "
              "support predicts 22 coordinates / 29 quadratic rows; "
              "exact raw-source rebuild remains open")


if __name__ == "__main__":
    main()
