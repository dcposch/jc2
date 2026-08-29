#!/usr/bin/env python3
"""Independent exact-Q replay of the localized tail-7 row-14 obstruction."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TAIL7 = ROOT / (
    "cases/ggv_8_28_upper_endpoint_tail7_reduced_20260828/"
    "TAIL7_REDUCED/TAIL_DEFORMATION_SYSTEM.json"
)
SHARED = ROOT / (
    "cases/ggv_8_28_upper_endpoint_tail7_branches_20260828/"
    "BRANCHES/shared_block.json"
)
AWS_STDOUT = ROOT / (
    "cases/ggv_8_28_upper_endpoint_tail7_branches_20260828/"
    "AWS_R6D_SHARED_BLOCK_20260828T010806Z/engine.stdout"
)
EXPECTED = {
    TAIL7: "7edd5ccd471e9eb3e27f0f163b0b337e0fb5057126ec69869f988093defba7aa",
    SHARED: "3e586cc283526efa9c12f51f5be5535d31eaa1b03ee0296783438acabf9feaab",
    HERE / "R14/R14_HOMOGENEOUS.json":
        "5ba0f08eeaf9023d45e64563c82269c57202ac0596208a06145d1bccd793afdf",
    HERE / "R14/R14_P87_ONE_P86_ZERO.json":
        "ea41511595d4cf906a06778ebdf80c69ba8f24f92b693e366a3fd9d8ac1cefa1",
    HERE / "R14/LOCALIZATION_CERTIFICATE.json":
        "291fff50be2573ce1e6a04f5fadecbb95b728506dce522c4f1a465905e9bc831",
    AWS_STDOUT: "85d3aad67e459f6f7d8e84556ccfc462cf15eff6ed37ab51a21cda2559eb64c0",
}


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def compact(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def decode(terms):
    return {tuple(monomial): Q(coefficient) for monomial, coefficient in terms}


def encode(poly):
    return [[list(monomial), str(coefficient)]
            for monomial, coefficient in sorted(poly.items())]


def plus(left, right, factor=Q(1)):
    result = dict(left)
    for monomial, coefficient in right.items():
        result[monomial] = result.get(monomial, Q(0)) + factor * coefficient
        if not result[monomial]:
            del result[monomial]
    return result


def product(left, right):
    result = {}
    for a, ca in left.items():
        for b, cb in right.items():
            monomial = tuple(sorted(a + b))
            result[monomial] = result.get(monomial, Q(0)) + ca * cb
            if not result[monomial]:
                del result[monomial]
    return result


def evaluate(poly, replacements):
    result = {}
    for monomial, coefficient in poly.items():
        term = {(): coefficient}
        for variable in monomial:
            term = product(term, replacements.get(variable, {(variable,): Q(1)}))
        result = plus(result, term)
    return result


def weight(vector):
    values = set()
    for name, _coefficient in vector:
        kind, x_degree, y_degree = name.split("_")
        values.add((8 if kind == "f" else 12)
                   + 3 * int(x_degree) - int(y_degree))
    assert max(values) - min(values) <= 3
    return min(values)


def eliminate(rows, columns):
    work = [([Q(value) for value in coefficients], dict(residual))
            for coefficients, residual in rows]
    pivots = []
    pivot_row = 0
    for column in range(columns):
        selected = next((row for row in range(pivot_row, len(work))
                         if work[row][0][column]), None)
        if selected is None:
            continue
        work[pivot_row], work[selected] = work[selected], work[pivot_row]
        coefficients, residual = work[pivot_row]
        scale = coefficients[column]
        coefficients = [value / scale for value in coefficients]
        residual = {monomial: value / scale
                    for monomial, value in residual.items()}
        work[pivot_row] = coefficients, residual
        for row in range(len(work)):
            if row == pivot_row or not work[row][0][column]:
                continue
            factor = work[row][0][column]
            work[row] = (
                [a - factor * b for a, b in zip(work[row][0], coefficients)],
                plus(work[row][1], residual, -factor),
            )
        pivots.append(column)
        pivot_row += 1
    return work, pivots


def main():
    for path, expected in EXPECTED.items():
        assert sha256(path) == expected, path
    source = json.loads(TAIL7.read_text())
    grouped = {}
    for record in source["constraints"]:
        grouped.setdefault(int(record["row"]), []).append({
            "x_degree": int(record["x_degree"]),
            "poly": decode(record["terms"]),
        })
    weights = {index: weight(vector)
               for index, vector in enumerate(source["nullspace_basis"])}

    replacements = {}
    row14_compatibility = None
    row21_compatibility = None
    replay_log = []
    for row_number in range(14, 22):
        new = sorted(parameter for parameter, parameter_weight in weights.items()
                     if parameter_weight == row_number
                     and parameter not in replacements
                     and parameter not in (32, 87))
        rows = []
        for record in grouped[row_number]:
            poly = evaluate(record["poly"], replacements)
            coefficients = [Q(0)] * len(new)
            residual = {}
            for monomial, coefficient in poly.items():
                hits = [variable for variable in monomial if variable in new]
                if hits:
                    assert len(hits) == 1 and monomial == (hits[0],)
                    coefficients[new.index(hits[0])] += coefficient
                else:
                    residual[monomial] = coefficient
            rows.append((coefficients, residual))
        reduced, pivots = eliminate(rows, len(new))
        free = [column for column in range(len(new)) if column not in set(pivots)]
        for pivot_row, pivot_column in enumerate(pivots):
            coefficients, residual = reduced[pivot_row]
            solution = {monomial: -coefficient
                        for monomial, coefficient in residual.items()}
            for free_column in free:
                if coefficients[free_column]:
                    solution[(new[free_column],)] = -coefficients[free_column]
            replacements[new[pivot_column]] = solution
        compatibility = [residual for coefficients, residual
                         in reduced[len(pivots):] if residual]
        replay_log.append((row_number, len(rows), len(pivots), len(compatibility)))
        if row_number == 14:
            row14_compatibility = compatibility
        if row_number == 21:
            row21_compatibility = compatibility

    assert replay_log == [
        (14, 26, 10, 16), (15, 25, 8, 17), (16, 24, 7, 17),
        (17, 23, 6, 17), (18, 22, 5, 17), (19, 21, 3, 18),
        (20, 20, 2, 18), (21, 19, 1, 18),
    ]
    assert row14_compatibility is not None and row21_compatibility is not None
    assert all(all(len(monomial) == 2 for monomial in poly)
               for poly in row14_compatibility)
    assert {variable for poly in row14_compatibility for monomial in poly
            for variable in monomial} == set(range(78, 88))
    assert row21_compatibility[1] == {(86, 87, 87): Q(-3, 4)}

    endpoint = [evaluate(record["poly"], replacements)
                for record in grouped[22] if record["x_degree"] == 0]
    assert endpoint == [{(): Q(-1), (32, 87): Q(-1)}]

    dehom = [evaluate(poly, {87: {(): Q(1)}, 86: {(): Q(0)}})
             for poly in row14_compatibility]
    dehom_terms = [encode(poly) for poly in dehom]
    shared = json.loads(SHARED.read_text())
    shared_terms = [record["terms"] for record in shared["constraints"]]
    assert dehom_terms == shared_terms
    assert hashlib.sha256(compact(dehom_terms)).hexdigest() == (
        "30607ce7a81e6cbd6d5a8eca54087281399c2835ff68f0945a88c092963d4257"
    )

    stdout = AWS_STDOUT.read_text()
    assert "BASIS_SIZE=1" in stdout
    assert "UNIT=1" in stdout
    assert "J[1]=1" in stdout
    print(json.dumps({
        "status": "PASS",
        "row21_relation": "-(3/4)*p86*p87^2=0",
        "endpoint_relation": "-1-p32*p87=0",
        "ordered_terms_sha256":
            "30607ce7a81e6cbd6d5a8eca54087281399c2835ff68f0945a88c092963d4257",
        "shared_block_unit_literal": "J[1]=1",
        "scope": "all field-valued tail7 endpoint points",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
