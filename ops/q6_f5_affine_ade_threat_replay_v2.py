#!/usr/bin/env python3
"""Fail-closed v2 replay for the q=6 F5 affine-ADE threat map.

V1 incorrectly restricted every reduced strict prime to positive B-degree.
This corrigendum hash-pins the v1 finite engine, replaces only the B-degree
composition domain by nonnegative integers, and records the exact delta from
the old positive-only control.  Necessary lattice data are still not an
effective surface, an incidence, or a polynomial map.
"""

from __future__ import annotations

import contextlib
import hashlib
import importlib.util
import io
import itertools
import json
import sys
from pathlib import Path


V1_SHA256 = "b892cd1520f13f10093fc51f547672cb8145ad4949c92a86a6ecb9055f3bdd46"
V1_OUTPUT_SHA256 = "293f2aee078dbcb0448c57ce4720646503719e2596a9454e709736baa041d602"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def load_v1_engine():
    path = Path(__file__).with_name("q6_f5_affine_ade_threat_replay.py")
    payload = path.read_bytes()
    require(
        hashlib.sha256(payload).hexdigest() == V1_SHA256,
        "hash-pinned v1 q6 engine drifted",
    )
    specification = importlib.util.spec_from_file_location("q6_f5_v1_engine", path)
    require(specification is not None and specification.loader is not None,
            "cannot load hash-pinned v1 q6 engine")
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def nonnegative_compositions(total, weights):
    for values in itertools.product(range(total + 1), repeat=len(weights)):
        if sum(weight * value for weight, value in zip(weights, values)) == total:
            yield values


def positive_control_compositions(total, weights):
    for values in itertools.product(range(1, total + 1), repeat=len(weights)):
        if sum(weight * value for weight, value in zip(weights, values)) == total:
            yield values


def run_engine(engine, generator):
    engine.weighted_positive_compositions = generator
    stream = io.StringIO()
    with contextlib.redirect_stdout(stream):
        engine.main()
    raw = stream.getvalue().encode("utf-8")
    return json.loads(raw), raw


def vertical_class_control(engine):
    zero = (0,) * 9
    candidates = engine.branch_candidates(
        engine.BASE_C,
        (),
        (),
        0,
        2,
        1,
        1,
    )
    require(
        candidates == ((zero, 0),),
        "vertical degree-two class F was not generated exactly",
    )
    partitions = tuple(nonnegative_compositions(4, (1, 1, 1)))
    require(
        (1, 0, 3) in partitions,
        "vertical B3 B-degree partition was not enumerated",
    )
    return {
        "class": "F",
        "a": 0,
        "degree": 2,
        "epsilon": 1,
        "t_contact": 1,
        "x": zero,
        "adjunction_delta": 0,
        "example_partition": (1, 0, 3),
    }


def delta_summary(corrected, positive_control):
    result = {}
    total_added_metas = 0
    total_added_candidates = 0
    for section in ("results", "baseline_controls"):
        result[section] = {}
        for name in sorted(corrected[section]):
            new = corrected[section][name]
            old = positive_control[section][name]
            added_metas = new["branch_feasible_metas"] - old["branch_feasible_metas"]
            added_joins = new["exact_join_metas"] - old["exact_join_metas"]
            added_candidates = (
                new["adjunction_candidate_tuples"]
                - old["adjunction_candidate_tuples"]
            )
            require(added_metas >= 0 and added_joins >= 0 and added_candidates >= 0,
                    "nonnegative B-degree domain removed a v1 candidate")
            total_added_metas += added_metas
            total_added_candidates += added_candidates
            result[section][name] = {
                "added_branch_feasible_metas": added_metas,
                "added_exact_join_metas": added_joins,
                "added_candidate_records": added_candidates,
            }
    require(total_added_metas > 0, "vertical a=0 domain was not exercised")
    require(total_added_candidates > 0, "vertical a=0 candidates were not generated")
    return result, total_added_metas, total_added_candidates


def build_output(corrected_generator=nonnegative_compositions):
    engine = load_v1_engine()
    vertical_witness = vertical_class_control(engine)

    corrected, corrected_raw = run_engine(engine, corrected_generator)
    positive, positive_raw = run_engine(engine, positive_control_compositions)
    require(
        hashlib.sha256(positive_raw).hexdigest() == V1_OUTPUT_SHA256,
        "positive-only control no longer replays v1 output",
    )
    deltas, added_metas, added_candidates = delta_summary(corrected, positive)
    require(
        deltas["results"]["B3_tau_ne0_Delta_ne0"][
            "added_branch_feasible_metas"
        ] == 16,
        "generic B3 vertical-cell exercise count drifted",
    )
    require(
        deltas["results"]["B3_tau0_distinct_residual"][
            "added_branch_feasible_metas"
        ] == 7,
        "tau=0 vertical-cell exercise count drifted",
    )
    require(
        deltas["results"]["U3_A3"]["added_branch_feasible_metas"] == 0,
        "U3 unexpectedly acquired a vertical B-degree meta",
    )
    require(
        deltas["results"]["B3_tau_ne0_Delta0_doubled"][
            "added_branch_feasible_metas"
        ] == 0,
        "coefficient-two nonzero-modulus block unexpectedly owns unit contact",
    )
    require(
        all(data["survivors"] == 0 for data in corrected["results"].values()),
        "q6 affine survivor found after admitting vertical primes",
    )
    require(
        all(
            data["survivors"] == 0
            for data in corrected["baseline_controls"].values()
        ),
        "q6 baseline survivor found after admitting vertical primes",
    )
    require(
        all(
            data["pair_condition_matches_before_carrier"] == 0
            for section in ("results", "baseline_controls")
            for data in corrected[section].values()
        ),
        "q6 pair-condition match found after admitting vertical primes",
    )

    corrected["schema"] = "Q6-AFFINE-ADE-THREAT/v2"
    corrected["B_degree_domain"] = "nonnegative"
    corrected["v1_dependency_sha256"] = V1_SHA256
    corrected["v1_positive_control_output_sha256"] = V1_OUTPUT_SHA256
    corrected["corrected_engine_raw_sha256"] = hashlib.sha256(
        corrected_raw
    ).hexdigest()
    corrected["vertical_enumeration_control"] = {
        "status": "PASS",
        "witness": vertical_witness,
        "added_branch_feasible_metas_total": added_metas,
        "added_candidate_records_total": added_candidates,
        "cell_deltas": deltas,
    }
    return corrected


def main():
    output = build_output()
    print(json.dumps(output, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    try:
        if sys.argv[1:] == ["--mutate-contact"]:
            load_v1_engine().run_failing_mutation()
        elif sys.argv[1:] == ["--mutate-drop-vertical"]:
            # This old-pass/new-fail mutation restores v1's positive-only
            # B-degree domain.  The vertical-domain exercise check must fail.
            build_output(positive_control_compositions)
        else:
            require(not sys.argv[1:], "unknown command-line argument")
            main()
    except RuntimeError as error:
        print("FAIL:" + str(error), file=sys.stderr)
        raise SystemExit(1)
