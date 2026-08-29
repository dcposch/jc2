#!/usr/bin/env python3
"""Analyze the graph-relative K support at the delayed a=3 face (AWS only)."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
import os
from pathlib import Path
import platform
import re


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
Q_STDOUT = ROOT / "cases/max12_812_order2_affine_faber_a_graph_relative_multisupport_20260826/evidence/Box03/aws_q/run/max12_812_order2_affine_faber_a_graph_relative_multisupport_20260826T164514Z_q.stdout"
P_STDOUT = ROOT / "cases/max12_812_order2_affine_faber_a_graph_relative_multisupport_20260826/evidence/r6d/aws_p65521/run/max12_812_order2_affine_faber_a_graph_relative_multisupport_20260826T164514Z_p65521.stdout"
Q_SHA = "40953daef89c5d57ecd14619e6ead4870f81f9c75c1b3e2c33ed029848716a30"
P_SHA = "37961e6a9b120c85d95fc6bc16912cff946050106529cffcb0ce3dacfebba6f5"

VARIABLES = (
    "J", "mu6", "d4", "dm", "d2", "d6", "K10",
    "S0", "S1", "R0", "R1", "Y", "X", "a", "lambda", "M", "E",
    "n0", "n1", "n2", "n3", "qr", "qc", "qp", "k2", "k6", "k10",
)
EXP_RE = re.compile(r"^A_KGRAPH_TERM_EXP=(.*)$")
TERM_RE = re.compile(r"^A_KGRAPH_TERM=(.*)$")


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only graph-relative cone analyzer refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only graph-relative cone analyzer refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def parse(path: Path) -> list[tuple[tuple[int, ...], str]]:
    exponents: list[tuple[int, ...]] = []
    terms: list[str] = []
    for line in path.read_text().splitlines():
        match = EXP_RE.match(line)
        if match:
            exp = tuple(int(piece) for piece in match.group(1).split(","))
            if len(exp) != len(VARIABLES):
                fail(("bad exponent length", len(exp), exp))
            exponents.append(exp)
        match = TERM_RE.match(line)
        if match:
            terms.append(match.group(1))
    if len(exponents) != 365 or len(terms) != 365:
        fail(("unexpected support count", len(exponents), len(terms), path))
    return list(zip(exponents, terms))


def line(exp: tuple[int, ...]) -> tuple[int, int]:
    intercept = 48 * exp[2]
    intercept += 42 * sum(exp[index] for index in (3, 4, 5, 6))
    intercept += 3 * exp[13] + 15 * exp[14]
    slope = 2 * sum(exp[index] for index in (7, 8, 9, 10))
    slope += exp[11] + exp[12]
    return intercept, slope


def has_strict_deviation(exp: tuple[int, ...]) -> bool:
    return any(exp[index] for index in (3, 4, 5))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    tag = require_aws()
    if digest(Q_STDOUT) != Q_SHA or digest(P_STDOUT) != P_SHA:
        fail("frozen graph-relative stdout mismatch")
    q_terms = parse(Q_STDOUT)
    p_terms = parse(P_STDOUT)
    if [exp for exp, _ in q_terms] != [exp for exp, _ in p_terms]:
        fail("exact-Q and prime exponent sequences differ")

    intrinsic = [0] * len(VARIABLES)
    intrinsic[14] = 3
    intrinsic[15] = 3
    intrinsic[16] = 1
    intrinsic_key = tuple(intrinsic)
    intrinsic_terms = [term for exp, term in q_terms if exp == intrinsic_key]
    if intrinsic_terms != ["-1/16*lam^3*M^3*E"]:
        fail(("intrinsic sentinel mismatch", intrinsic_terms))

    q6_rows = []
    for exp, term in q_terms:
        intercept, slope = line(exp)
        weight = intercept + 6 * slope
        q6_rows.append((weight, exp, term, has_strict_deviation(exp)))
    q6_minimum = min(row[0] for row in q6_rows)
    q6_minima = [row for row in q6_rows if row[0] == q6_minimum]
    if q6_minimum != 45:
        fail(("unexpected q=6 minimum", q6_minimum))
    unsafe_q6 = [row for row in q6_minima if row[1] != intrinsic_key and not row[3]]
    if unsafe_q6:
        fail(("nondeviation q=6 tie", unsafe_q6))

    threshold = Fraction(0)
    threshold_rows: list[tuple[tuple[int, ...], str, bool]] = []
    low_constant_rows = []
    unsafe_constant_ties = []
    for exp, term in q_terms:
        if exp == intrinsic_key:
            continue
        intercept, slope = line(exp)
        strict = has_strict_deviation(exp)
        if slope == 0:
            if intercept < 45:
                low_constant_rows.append((exp, term, intercept, strict))
            elif intercept == 45 and not strict:
                unsafe_constant_ties.append((exp, term))
            continue
        candidate = Fraction(45 - intercept, slope)
        if candidate > threshold:
            threshold = candidate
            threshold_rows = [(exp, term, strict)]
        elif candidate == threshold:
            threshold_rows.append((exp, term, strict))
    if low_constant_rows or unsafe_constant_ties:
        fail(("q-independent obstruction", low_constant_rows, unsafe_constant_ties))
    if threshold > 6:
        fail(("threshold exceeds predecessor split", threshold, threshold_rows))
    if threshold == 6 and any(not strict for _, _, strict in threshold_rows):
        fail(("unsafe equality at q=6", threshold_rows))

    bad_graph_terms = []
    for exp, term in q_terms:
        if exp == intrinsic_key or exp[6] == 0 or has_strict_deviation(exp):
            continue
        intercept, slope = line(exp)
        if intercept + 6 * slope <= 45:
            bad_graph_terms.append((exp, term, intercept, slope))
    if bad_graph_terms:
        fail(("central affine-graph term survived at/below 45", bad_graph_terms))

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    result = {
        "status": "PASS-A-GRAPH-RELATIVE-A3-QGE6-DIRECT-UNIT-SUPPORT",
        "registered_aws_lane": tag,
        "term_count": len(q_terms),
        "exact_prime_exponent_sequence_equal": True,
        "intrinsic_term": intrinsic_terms[0],
        "intrinsic_weight": 45,
        "q6_base_minimum": q6_minimum,
        "q6_base_minima": [
            {"term": term, "strict_transverse_deviation": strict, "exponents": list(exp)}
            for _, exp, term, strict in q6_minima
        ],
        "raw_threshold_q": str(threshold),
        "threshold_rows": [
            {"term": term, "strict_transverse_deviation": strict, "exponents": list(exp)}
            for exp, term, strict in threshold_rows
        ],
        "central_K10_terms_at_or_below_45": [],
        "exact_q_stdout_sha256": digest(Q_STDOUT),
        "prime_stdout_sha256": digest(P_STDOUT),
        "scope": "GRAPH_RELATIVE_K_SUPPORT_AT_DELAYED_H15_A3_WITH_STRICT_D6_D2_DM_EXCESS_AND_QGE6_ONLY_NO_PREDECESSOR_SOURCE_REES_ORDER2_MAX12_OR_JC2_VERDICT",
    }
    (output / "graph_relative_cone_a3.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("A_KGRAPH_A3_TERM_COUNT=" + str(len(q_terms)))
    print("A_KGRAPH_A3_Q6_BASE_MINIMUM=" + str(q6_minimum))
    print("A_KGRAPH_A3_Q6_MINIMA_COUNT=" + str(len(q6_minima)))
    for _, exp, term, strict in q6_minima:
        print("A_KGRAPH_A3_Q6_MINIMUM_TERM=" + term)
        print("A_KGRAPH_A3_Q6_MINIMUM_STRICT_DEVIATION=" + str(int(strict)))
        print("A_KGRAPH_A3_Q6_MINIMUM_EXP=" + ",".join(str(value) for value in exp))
    print("A_KGRAPH_A3_THRESHOLD_Q=" + str(threshold))
    print("A_KGRAPH_A3_THRESHOLD_ROWS=" + str(len(threshold_rows)))
    print("A_KGRAPH_A3_CENTRAL_K10_LOW_TERMS=0")
    print("A_KGRAPH_A3_ENDPOINT=PASS_GRAPH_RELATIVE_A3_QGE6_DIRECT_UNIT_SUPPORT")
    print("A_KGRAPH_A3_DONE=1")
    print("A_KGRAPH_A3_SCOPE=" + result["scope"])


if __name__ == "__main__":
    main()
