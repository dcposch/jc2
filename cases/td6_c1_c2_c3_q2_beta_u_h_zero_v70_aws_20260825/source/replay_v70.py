#!/usr/bin/env python3
"""Complete-localization wrapper for raw q2-beta `u-h-zero`/origin runs.

The frozen V69 producer has exact original-row replay and a canonical digest
serializer, but its displayed compatibility denominator omits the transport
chart and first-source denominators.  This wrapper does not alter its algebra.
It pins and imports V69, records every nonconstant transport pivot, computes
the parent-style complete localization, and adds a wrong-row negative control.
"""

from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
PARENT_PATH = (
    HERE.parent / "td6_c1_c2_c3_q2_n13_raw_canonical_v69_20260825"
    / "replay.py"
)
PARENT_SHA256 = "9a518a4b877f32548d99ecfa6a9eb15650a8a301e3277991da98744bed8e5385"
assert sha256(PARENT_PATH.read_bytes()).hexdigest() == PARENT_SHA256
spec = importlib.util.spec_from_file_location("td6_q2_beta_raw_v69", PARENT_PATH)
p = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = p
spec.loader.exec_module(p)

assert p.STRATUM in {"u-h-zero", "origin"}
captured = {}


def monic(value):
    if not value:
        return value
    return value / value.leading_coefficient()


original_factor_transport = p.tri.factor_transport


def factor_transport_with_complete_chart(rows):
    result = original_factor_transport(rows)
    events = result[2]
    chart = p.tri.r.transport_chart_polynomial(events)
    captured["transport_rows"] = rows
    captured["transport_chart"] = chart
    print(f"v70_transport_event_count={len(events)}")
    for index, (row_index, key, pivot, numerator, denominator) in enumerate(events):
        print(
            f"v70_transport_event[{index}]={row_index},{key},{pivot};"
            f"num=({numerator});den=({denominator})"
        )
    print(f"v70_transport_chart_denominator=({chart})")
    print(f"v70_transport_chart_denominator_factor={chart.factor()}", flush=True)
    return result


p.tri.factor_transport = factor_transport_with_complete_chart
original_parameterize = p.parameterize


def parameterize_with_source_denominator(nvariables, rows, stage):
    captured[f"{stage}_rows"] = rows
    source_denominator = p.denominator_lcm_beta(
        coefficient
        for _, row, rhs in rows
        for coefficient in list(row.values()) + [rhs]
    )
    captured[f"{stage}_source_denominator"] = source_denominator
    print(f"v70_{stage}_source_denominator=({source_denominator})")
    print(
        f"v70_{stage}_source_denominator_factor={source_denominator.factor()}",
        flush=True,
    )
    return original_parameterize(nvariables, rows, stage)


p.parameterize = parameterize_with_source_denominator
original_emit = p.emit_stage_incompatibilities


def replay_combination(rows, combination):
    matrix, rhs = {}, p.BetaPoly()
    for source_index, weight in combination.items():
        _, source_row, source_rhs = rows[source_index]
        for variable, coefficient in source_row.items():
            p.add_to_row(matrix, variable, weight * coefficient)
        rhs += weight * source_rhs
    return matrix, rhs


def replay_transport_combination(rows, combination):
    matrix, rhs = {}, p.BetaPoly()
    for source_index, weight in combination.items():
        source_key, source_row, _ = rows[source_index]
        for variable, coefficient in source_row.items():
            p.add_to_row(
                matrix,
                variable,
                weight * p.BetaPoly(p.b.scalar(coefficient)),
            )
        base, derivative = p.b.source_vector_beta(source_key)
        source = p.BetaPoly([
            p.b.from_vector(base), p.b.from_vector(derivative)
        ])
        rhs += weight * source
    return matrix, rhs


def emit_with_complete_localization(dependent, stage):
    bad = [record for record in dependent if record[2]]
    result = original_emit(dependent, stage)
    if not bad:
        return result

    residuals, gcd, bezout = p.polynomial_ideal_gcd(
        [residual for _, _, residual, _ in bad]
    )
    inner_values = list(residuals) + list(bezout)
    for _, _, _, combination in bad:
        inner_values.extend(combination.values())
    if gcd.degree == 0:
        inner_values.append(gcd.inverse())
    inner_denominator = p.denominator_lcm_beta(inner_values)
    transport_chart = captured["transport_chart"]
    source_denominator = (
        captured["transport_chart"] ** 0
        if stage == "transport"
        else captured[f"{stage}_source_denominator"]
    )
    complete = monic(transport_chart * source_denominator * inner_denominator)

    rows = captured[
        "transport_rows" if stage == "transport" else f"{stage}_rows"
    ]
    for index, (_, _, residual, combination) in enumerate(bad):
        replay = (
            replay_transport_combination
            if stage == "transport"
            else replay_combination
        )
        positive_matrix, positive_rhs = replay(rows, combination)
        assert not positive_matrix and positive_rhs == residual
        negative = dict(combination)
        source_index = min(negative)
        negative[source_index] = negative[source_index] + p.BetaPoly(1)
        negative_matrix, negative_rhs = replay(rows, negative)
        assert negative_matrix or negative_rhs != residual
        print(f"v70_{stage}_incompatibility[{index}]_original_row_replay=true")
        print(f"v70_{stage}_incompatibility[{index}]_wrong_row_control=true")

    whole = gcd.degree == 0 and complete.total_degree() == 0
    print(f"v70_{stage}_inner_denominator=({inner_denominator})")
    print(f"v70_{stage}_complete_certificate_denominator=({complete})")
    print(
        f"v70_{stage}_complete_certificate_denominator_factor="
        f"{complete.factor()}"
    )
    print(f"v70_{stage}_whole_raw_stratum_empty={str(whole).lower()}")
    print(
        f"v70_{stage}_remaining_denominator_strata_required="
        f"{str(not whole).lower()}",
        flush=True,
    )
    return result


p.emit_stage_incompatibilities = emit_with_complete_localization


if __name__ == "__main__":
    print("v70_complete_localization_wrapper=true")
    print(f"v70_parent_sha256={PARENT_SHA256}")
    p.main()
