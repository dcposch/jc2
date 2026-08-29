#!/usr/bin/env python3
"""Classify the repaired a=3 graph cone and its q=6 equality face."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V1 = ROOT / "cases/max12_812_order2_affine_faber_a_graph_relative_cone_a3_20260826/analyze_graph_relative_cone_a3.py"
V1_SHA = "d91cfa93e336040faa8874aea741ab96178cd91ffc6071dc37ee2e0734ddafc2"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_v1():
    if digest(V1) != V1_SHA:
        fail("frozen V1 analyzer mismatch")
    spec = importlib.util.spec_from_file_location("graph_a3_v1", V1)
    if spec is None or spec.loader is None:
        fail("cannot load V1 analyzer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only V2 cone analyzer refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only V2 cone analyzer refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    tag = require_aws()
    v1 = load_v1()
    if digest(v1.Q_STDOUT) != v1.Q_SHA or digest(v1.P_STDOUT) != v1.P_SHA:
        fail("frozen graph support mismatch")
    q_terms = v1.parse(v1.Q_STDOUT)
    p_terms = v1.parse(v1.P_STDOUT)
    if [exp for exp, _ in q_terms] != [exp for exp, _ in p_terms]:
        fail("dual exponent sequences differ")

    intrinsic = [0] * len(v1.VARIABLES)
    intrinsic[14] = 3
    intrinsic[15] = 3
    intrinsic[16] = 1
    intrinsic_key = tuple(intrinsic)
    q6_rows = []
    for exp, term in q_terms:
        intercept, slope = v1.line(exp)
        q6_rows.append((intercept + 6 * slope, exp, term, v1.has_strict_deviation(exp)))
    minimum = min(row[0] for row in q6_rows)
    if minimum != 45:
        fail(("unexpected q6 minimum", minimum))
    minima = [row for row in q6_rows if row[0] == minimum]
    nonstrict = [(exp, term) for _, exp, term, strict in minima if exp != intrinsic_key and not strict]
    expected_nonstrict_terms = {
        "-3/8*X^2*a*lam^2*M^2",
        "3/2*Y^2*a*lam^2*E",
    }
    if {term for _, term in nonstrict} != expected_nonstrict_terms or len(nonstrict) != 2:
        fail(("unexpected nonstrict q6 face", nonstrict))
    intrinsic_terms = [term for _, exp, term, _ in minima if exp == intrinsic_key]
    if intrinsic_terms != ["-1/16*lam^3*M^3*E"]:
        fail(("intrinsic mismatch", intrinsic_terms))

    threshold = Fraction(0)
    threshold_rows = []
    below = []
    constant_unsafe = []
    for exp, term in q_terms:
        if exp == intrinsic_key:
            continue
        intercept, slope = v1.line(exp)
        strict = v1.has_strict_deviation(exp)
        if slope == 0:
            if intercept < 45:
                below.append((exp, term, intercept, strict))
            elif intercept == 45 and not strict:
                constant_unsafe.append((exp, term))
            continue
        candidate = Fraction(45 - intercept, slope)
        if candidate > threshold:
            threshold = candidate
            threshold_rows = [(exp, term, strict)]
        elif candidate == threshold:
            threshold_rows.append((exp, term, strict))
    if below or constant_unsafe:
        fail(("q-independent obstruction", below, constant_unsafe))
    if threshold != 6:
        fail(("unexpected q threshold", threshold, threshold_rows))
    threshold_nonstrict = {term for _, term, strict in threshold_rows if not strict}
    if threshold_nonstrict != expected_nonstrict_terms:
        fail(("threshold face mismatch", threshold_rows))

    bad_k10 = []
    for exp, term in q_terms:
        if exp == intrinsic_key or exp[6] == 0 or v1.has_strict_deviation(exp):
            continue
        intercept, slope = v1.line(exp)
        if intercept + 6 * slope <= 45:
            bad_k10.append((exp, term, intercept, slope))
    if bad_k10:
        fail(("central K10 term survived", bad_k10))

    strict_ties = [(exp, term) for _, exp, term, strict in minima if strict]
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    result = {
        "status": "PASS-A-GRAPH-A3-QGT6-DIRECT-UNIT-AND-Q6-EQUALITY-FACE",
        "registered_aws_lane": tag,
        "term_count": len(q_terms),
        "threshold_q": str(threshold),
        "q6_base_minimum": minimum,
        "intrinsic_term": intrinsic_terms[0],
        "q6_nonstrict_competitors": [term for _, term in nonstrict],
        "q6_strict_deviation_ties": [term for _, term in strict_ties],
        "q6_reduced_nondeviation_initial": "lam^2*(-E*lam*M^3/16-3*a*M^2*X^2/8+3*a*E*Y^2/2)",
        "direct_unit_regions": ["a=3 and q>6", "a>3 and q>=6"],
        "exact_q_stdout_sha256": digest(v1.Q_STDOUT),
        "prime_stdout_sha256": digest(v1.P_STDOUT),
        "scope": "GRAPH_RELATIVE_K_SUPPORT_SPLIT_ONLY_Q6_EQUALITY_REQUIRES_PREDECESSOR_REDUCTION_NO_SOURCE_REES_ORDER2_MAX12_OR_JC2_VERDICT",
    }
    (output / "graph_relative_cone_a3_v2.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("A_KGRAPH_A3V2_TERM_COUNT=" + str(len(q_terms)))
    print("A_KGRAPH_A3V2_THRESHOLD_Q=" + str(threshold))
    print("A_KGRAPH_A3V2_Q6_MINIMA_COUNT=" + str(len(minima)))
    print("A_KGRAPH_A3V2_Q6_NONSTRICT_COUNT=" + str(len(nonstrict)))
    print("A_KGRAPH_A3V2_Q6_STRICT_DEVIATION_COUNT=" + str(len(strict_ties)))
    for _, term in nonstrict:
        print("A_KGRAPH_A3V2_Q6_NONSTRICT_TERM=" + term)
    print("A_KGRAPH_A3V2_CENTRAL_K10_LOW_TERMS=0")
    print("A_KGRAPH_A3V2_ENDPOINT=PASS_A3_QGT6_DIRECT_UNIT_AND_Q6_EQUALITY_FACE")
    print("A_KGRAPH_A3V2_DONE=1")
    print("A_KGRAPH_A3V2_SCOPE=" + result["scope"])


if __name__ == "__main__":
    main()
