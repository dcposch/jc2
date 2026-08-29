#!/usr/bin/env python3
"""Matched reverse row/column presentation control for V84R2 block 0,0."""

from hashlib import sha256
import importlib.util
import os
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
PARENT = (
    HERE / "payload" / "jc2" / "cases"
    / "td6_c1_c2_c3_qdead_previous_pole_k2_shard_v84r2_20260826"
    / "replay.py"
)
PARENT_SHA256 = "dd2c05c92b3828493eabde9427487e940d3c838cecbc47dceb6c9c2562d40ee3"
assert sha256(PARENT.read_bytes()).hexdigest() == PARENT_SHA256
assert os.environ.get("TD6_K2_BLOCK_A") == "0"
assert os.environ.get("TD6_K2_BLOCK_B") == "0"

spec = importlib.util.spec_from_file_location("td6_v84s2_parent", PARENT)
m = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = m
spec.loader.exec_module(m)


def solve_cert_reverse_max(rows):
    """Reverse rows and use maximum unit-base pivots, with source replay."""
    pivots, dependent = {}, []
    source = [
        (
            key,
            {variable: m.QuadJet.coerce(value) for variable, value in row.items()},
            m.QuadJet.coerce(rhs),
        )
        for key, row, rhs in rows
    ]
    for source_index in range(len(source) - 1, -1, -1):
        key, original_row, original_rhs = source[source_index]
        row, rhs = dict(original_row), original_rhs
        combination = {source_index: m.QuadJet(1)}
        while True:
            pivot = next(
                (
                    variable for variable in sorted(pivots, reverse=True)
                    if variable in row and row[variable]
                ),
                None,
            )
            if pivot is None:
                break
            factor = row[pivot]
            old_row, old_rhs, old_combination = pivots[pivot]
            for variable, coefficient in old_row.items():
                value = row.get(variable, m.QuadJet()) - factor * coefficient
                if value:
                    row[variable] = value
                else:
                    row.pop(variable, None)
            rhs -= factor * old_rhs
            for old_index, coefficient in old_combination.items():
                value = combination.get(old_index, m.QuadJet()) - factor * coefficient
                if value:
                    combination[old_index] = value
                else:
                    combination.pop(old_index, None)
        base_variables = [
            variable for variable, coefficient in row.items() if coefficient.value
        ]
        if not base_variables:
            replay = {}
            for old_index, coefficient in combination.items():
                _, source_row, source_rhs = source[old_index]
                replay = m.add_polynomial(
                    replay,
                    m.source_polynomial(source_row, source_rhs),
                    coefficient,
                )
            assert replay == m.source_polynomial(row, rhs)
            dependent.append((source_index, key, row, rhs, combination))
            continue
        pivot = max(base_variables)
        inverse = row[pivot].inverse()
        pivots[pivot] = (
            {variable: coefficient * inverse for variable, coefficient in row.items()},
            rhs * inverse,
            {index: coefficient * inverse for index, coefficient in combination.items()},
        )
    for pivot, (row, rhs, combination) in pivots.items():
        replay = {}
        for source_index, coefficient in combination.items():
            _, source_row, source_rhs = source[source_index]
            replay = m.add_polynomial(
                replay, m.source_polynomial(source_row, source_rhs), coefficient
            )
        assert replay == m.source_polynomial(row, rhs), pivot
    return pivots, dependent


def parameterize_ascending(nvariables, rows):
    pivots, dependent = solve_cert_reverse_max(rows)
    free = [variable for variable in range(nvariables) if variable not in pivots]
    parameter_of = {variable: index for index, variable in enumerate(free)}
    forms = [None] * nvariables
    for variable in range(nvariables):
        if variable in parameter_of:
            forms[variable] = (m.QuadJet(), {parameter_of[variable]: m.QuadJet(1)})
            continue
        row, rhs, _ = pivots[variable]
        form = (rhs, {})
        for other, coefficient in row.items():
            if other != variable:
                assert other < variable and forms[other] is not None
                form = m.add_jet_form(form, forms[other], -coefficient)
        forms[variable] = form
    assert all(form is not None for form in forms)
    return pivots, forms, free, dependent


def controls():
    unit = m.QuadJet(1)
    good = [("pivot", {1: unit}, 0), ("dependent", {1: unit}, 0)]
    pivots, forms, free, dependent = parameterize_ascending(2, good)
    assert len(pivots) == 1 and len(dependent) == 1 and len(free) == 1
    assert all(form is not None for form in forms)
    bad = [("pivot", {1: unit}, 0), ("plus-one", {1: unit}, unit)]
    _, incompatible = solve_cert_reverse_max(bad)
    assert len(incompatible) == 1 and incompatible[0][3] != m.QuadJet()
    print("reverse_source_row_order_control=true")
    print("maximum_unit_base_pivot_control=true")
    print("ascending_parameterization_control=true")
    print("matched_reverse_row_column_order_control=true")
    print("dependent_row_positive_control=true")
    print("plus_one_rhs_incompatibility_control=true", flush=True)


def main():
    controls()
    m.solve_cert = solve_cert_reverse_max
    m.parameterize = parameterize_ascending
    print("producer=TD6-V84S2-MATCHED-REVERSE-PRESENTATION-CONTROL")
    print("V84S_unmatched_triangular_harness_failure_not_consumed=true")
    print("generic_reverse_presentation_not_full_Spencer_involutivity=true")
    m.main()
    print("TD6-V84S2-MATCHED-REVERSE-PRESENTATION-CONTROL PASS")


if __name__ == "__main__":
    main()
