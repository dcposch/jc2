#!/usr/bin/env python3
"""Extract the exact graph-relative direct-unit cone 15<H<18 (AWS only)."""

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
        fail("AWS-only H15-H18 analyzer refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only H15-H18 analyzer refused non-Amazon host")
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
            exponent = tuple(int(piece) for piece in match.group(1).split(","))
            if len(exponent) != len(VARIABLES):
                fail(("bad exponent length", len(exponent), exponent))
            exponents.append(exponent)
        match = TERM_RE.match(line)
        if match:
            terms.append(match.group(1))
    if len(exponents) != 365 or len(terms) != 365:
        fail(("unexpected support count", len(exponents), len(terms), path))
    return list(zip(exponents, terms))


def boundary_line(exp: tuple[int, ...]) -> tuple[Fraction, Fraction]:
    """Return weight-3H at alpha=H/3 and q=21-H."""
    constant = Fraction(48 * exp[2])
    constant += Fraction(42 * sum(exp[index] for index in (3, 4, 5, 6)))
    h_coefficient = Fraction(exp[13], 3) + exp[14]
    q_slope = 2 * sum(exp[index] for index in (7, 8, 9, 10))
    q_slope += exp[11] + exp[12]
    constant += 21 * q_slope
    h_coefficient -= q_slope
    h_coefficient -= 3
    return constant, h_coefficient


def value(line: tuple[Fraction, Fraction], h: int) -> Fraction:
    return line[0] + h * line[1]


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
    if any(any(exp[index] for index in (0, 1, *range(17, 27))) for exp, _ in q_terms):
        fail("inactive/raw variable survived graph-relative substitution")

    intrinsic = [0] * len(VARIABLES)
    intrinsic[14] = 3
    intrinsic[15] = 3
    intrinsic[16] = 1
    intrinsic_key = tuple(intrinsic)
    intrinsic_terms = [term for exp, term in q_terms if exp == intrinsic_key]
    if intrinsic_terms != ["-1/16*lam^3*M^3*E"]:
        fail(("intrinsic mismatch", intrinsic_terms))

    unsafe = []
    identically_tied = []
    endpoint_18 = []
    endpoint_15 = []
    for exp, term in q_terms:
        if exp == intrinsic_key:
            continue
        line = boundary_line(exp)
        d15 = value(line, 15)
        d18 = value(line, 18)
        q_slope = 2 * sum(exp[index] for index in (7, 8, 9, 10))
        q_slope += exp[11] + exp[12]
        strict_deviation = sum(exp[index] for index in (3, 4, 5))
        if d15 < 0 or d18 < 0:
            unsafe.append((term, str(d15), str(d18), list(exp)))
        if d15 == 0:
            endpoint_15.append((term, q_slope, strict_deviation, list(exp)))
        if d18 == 0:
            endpoint_18.append((term, q_slope, strict_deviation, list(exp)))
        if d15 == 0 and d18 == 0 and q_slope == 0 and strict_deviation == 0:
            identically_tied.append((term, list(exp)))
    if unsafe or identically_tied:
        fail(("unsafe open-band support", unsafe, identically_tied))

    nonstrict_h18 = [term for term, q_slope, strict, _ in endpoint_18
                     if q_slope == 0 and strict == 0]
    if nonstrict_h18 != ["4*d4*a"]:
        fail(("unexpected H=18 nonstrict wall", nonstrict_h18, endpoint_18))

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    result = {
        "status": "PASS-A-GRAPH-RELATIVE-OPEN-15-H-18-DIRECT-UNIT-SUPPORT",
        "registered_aws_lane": tag,
        "term_count": len(q_terms),
        "exact_prime_exponent_sequence_equal": True,
        "intrinsic_term": intrinsic_terms[0],
        "open_band": "15<H<18",
        "center_bound": "alpha>=H/3",
        "post_graph_kernel_bound": "q>21-H",
        "unsafe_terms": [],
        "identically_tied_nonstrict_terms": [],
        "closed_H18_nonstrict_wall": nonstrict_h18,
        "closed_H15_tie_count": len(endpoint_15),
        "closed_H18_tie_count": len(endpoint_18),
        "exact_q_stdout_sha256": digest(Q_STDOUT),
        "prime_stdout_sha256": digest(P_STDOUT),
        "scope": "GRAPH_RELATIVE_K_SUPPORT_AFTER_GRADE42_PREDECESSOR_QGT21MINUSH_ONLY_NO_PREDECESSOR_SOURCE_REES_ORDER2_MAX12_OR_JC2_VERDICT",
    }
    (output / "graph_relative_h15_h18.json").write_text(
        json.dumps(result, sort_keys=True, indent=2) + "\n"
    )
    print("A_KGRAPH_H1518_TERM_COUNT=" + str(len(q_terms)))
    print("A_KGRAPH_H1518_UNSAFE_COUNT=0")
    print("A_KGRAPH_H1518_IDENTICAL_NONSTRICT_TIES=0")
    print("A_KGRAPH_H1518_H18_NONSTRICT_WALL=" + nonstrict_h18[0])
    print("A_KGRAPH_H1518_ENDPOINT=PASS_OPEN_15_H_18_DIRECT_UNIT_SUPPORT")
    print("A_KGRAPH_H1518_DONE=1")
    print("A_KGRAPH_H1518_SCOPE=" + result["scope"])


if __name__ == "__main__":
    main()
