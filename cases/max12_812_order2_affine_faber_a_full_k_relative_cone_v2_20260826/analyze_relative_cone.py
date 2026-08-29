#!/usr/bin/env python3
"""Group the exact full-K support and extract the fixed delayed q-cone."""

from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
import json
import os
from pathlib import Path
import platform
import re


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
Q_STDOUT = ROOT / "cases/max12_812_order2_affine_faber_a_full_k_multisupport_20260826/evidence/Box03/run/max12_812_order2_affine_faber_a_full_k_multisupport_20260826T162000Z_q.stdout"
P_STDOUT = ROOT / "cases/max12_812_order2_affine_faber_a_full_k_multisupport_20260826/evidence/r6d/run/max12_812_order2_affine_faber_a_full_k_multisupport_20260826T162000Z_p65521.stdout"
Q_SHA = "1fd637a6918608b488c8e30e134f9a911354f7394ea83741634e04cdc5a7606b"
P_SHA = "13f06fee7fec5eb1c5165c47db7251665a2d6658b85b9ac7f669468ae2bff5f1"

VARIABLES = (
    "J", "mu6", "mu4", "mu2", "K2", "K6", "K10",
    "S0", "S1", "R0", "R1", "Y", "X", "a", "lambda", "M", "E",
    "n0", "n1", "n2", "n3", "qr", "qc", "qp", "k2", "k6", "k10",
)
Q_RE = re.compile(r"^A_KSUP_TERM_EXP=(.*)$")
T_RE = re.compile(r"^A_KSUP_TERM=(.*)$")


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only relative-cone analyzer refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only relative-cone analyzer refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def parse_stdout(path: Path) -> list[tuple[tuple[int, ...], str]]:
    exponents: list[tuple[int, ...]] = []
    terms: list[str] = []
    for line in path.read_text().splitlines():
        match = Q_RE.match(line)
        if match:
            exp = tuple(int(piece) for piece in match.group(1).split(","))
            if len(exp) != len(VARIABLES):
                fail(("bad exponent length", len(exp), exp))
            exponents.append(exp)
        match = T_RE.match(line)
        if match:
            terms.append(match.group(1))
    if len(exponents) != 371 or len(terms) != 371:
        fail(("unexpected support count", len(exponents), len(terms)))
    return list(zip(exponents, terms))


def coefficient(term: str) -> Fraction:
    sign = Fraction(1)
    text = term
    if text.startswith("-"):
        sign = Fraction(-1)
        text = text[1:]
    first = text.split("*", 1)[0]
    if re.fullmatch(r"[0-9]+(?:/[0-9]+)?", first):
        return sign * Fraction(first)
    return sign


def coeff_text(poly: dict[tuple[int, int], Fraction]) -> str:
    pieces: list[str] = []
    for (mexp, eexp), value in sorted(poly.items()):
        factors: list[str] = []
        if mexp:
            factors.append("M" if mexp == 1 else f"M^{mexp}")
        if eexp:
            factors.append("E" if eexp == 1 else f"E^{eexp}")
        body = "*".join(factors) or "1"
        pieces.append(f"({value})*{body}")
    return "+".join(pieces) if pieces else "0"


def line_at_delayed(key: tuple[int, ...]) -> tuple[int, int]:
    fixed = (57, 54, 48, 42, 42, 42, 42)
    intercept = sum(key[index] * fixed[index] for index in range(7))
    slope = 2 * sum(key[index] for index in (7, 8, 9, 10))
    slope += key[11] + key[12]
    intercept += 5 * key[13] + 15 * key[14]
    return intercept, slope


def pareto_pairs(groups: dict[tuple[int, ...], object], load_index: int) -> list[tuple[int, int]]:
    pairs: set[tuple[int, int]] = set()
    for key in groups:
        if key[load_index] != 1:
            continue
        if any(key[index] for index in range(7) if index != load_index):
            continue
        if any(key[index] for index in range(7, 13)):
            continue
        pairs.add((key[13], key[14]))
    return sorted(pair for pair in pairs if not any(other != pair and other[0] <= pair[0] and other[1] <= pair[1] for other in pairs))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    tag = require_aws()
    if digest(Q_STDOUT) != Q_SHA or digest(P_STDOUT) != P_SHA:
        fail("frozen support stdout mismatch")
    q_terms = parse_stdout(Q_STDOUT)
    p_terms = parse_stdout(P_STDOUT)
    q_exponents = [exp for exp, _ in q_terms]
    if q_exponents != [exp for exp, _ in p_terms]:
        fail("Q/F65521 support exponent mismatch")

    groups: dict[tuple[int, ...], dict[tuple[int, int], Fraction]] = defaultdict(lambda: defaultdict(Fraction))
    members: dict[tuple[int, ...], list[str]] = defaultdict(list)
    for exp, term in q_terms:
        if any(exp[index] for index in range(17, len(VARIABLES))):
            fail(("raw variable survived source substitution", exp, term))
        key = exp[:15]
        groups[key][(exp[15], exp[16])] += coefficient(term)
        members[key].append(term)
    groups = {key: {mon: val for mon, val in poly.items() if val} for key, poly in groups.items()}
    if any(not poly for poly in groups.values()):
        fail("zero coefficient group after exact collection")

    intrinsic = [0] * 15
    intrinsic[14] = 3
    intrinsic_key = tuple(intrinsic)
    if groups.get(intrinsic_key) != {(3, 1): Fraction(-1, 16)}:
        fail(("intrinsic coefficient mismatch", groups.get(intrinsic_key)))

    q6_weights = {key: Fraction(a + 6 * b) for key, (a, b) in ((key, line_at_delayed(key)) for key in groups)}
    minimum = min(q6_weights.values())
    q6_minima = sorted(key for key, value in q6_weights.items() if value == minimum)
    if minimum != 45 or q6_minima != [intrinsic_key]:
        fail(("q6 raw-K minimum mismatch", minimum, q6_minima))
    gap = min(value - 45 for key, value in q6_weights.items() if key != intrinsic_key)

    thresholds: dict[Fraction, list[tuple[int, ...]]] = defaultdict(list)
    for key in groups:
        if key == intrinsic_key:
            continue
        intercept, slope = line_at_delayed(key)
        if slope > 0 and intercept < 45:
            threshold = Fraction(45 - intercept, slope)
            if threshold > 0:
                thresholds[threshold].append(key)
        elif slope == 0 and intercept <= 45:
            fail(("q-independent competitor at or below intrinsic", key, intercept))
    max_threshold = max(thresholds, default=Fraction(0))
    max_keys = sorted(thresholds.get(max_threshold, []))

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    group_rows = []
    for key in sorted(groups):
        intercept, slope = line_at_delayed(key)
        group_rows.append({
            "valuation_exponents": list(key),
            "coefficient_ME": coeff_text(groups[key]),
            "member_terms": members[key],
            "delayed_weight_intercept": intercept,
            "delayed_weight_q_slope": slope,
        })
    result = {
        "status": "PASS-A-FULL-K-RELATIVE-CONE-V2",
        "registered_aws_lane": tag,
        "raw_term_count": len(q_terms),
        "coefficient_group_count": len(groups),
        "multi_member_coefficient_groups": sum(len(value) > 1 for value in members.values()),
        "intrinsic_key": list(intrinsic_key),
        "intrinsic_coefficient_ME": coeff_text(groups[intrinsic_key]),
        "q6_minimum": str(minimum),
        "q6_next_margin": str(gap),
        "raw_K_direct_unit_strict_for_q_greater_than": str(max_threshold),
        "raw_K_equality_keys_at_threshold": [list(key) for key in max_keys],
        "raw_K_equality_terms_at_threshold": [members[key] for key in max_keys],
        "row_system_quadratic_load_wall": "30+2*q=42 => q=6 (predecessor rows; not derived from K alone)",
        "row_system_quadratic_cubic_wall": "30+2*q=45 => q=15/2 (predecessor rows; not derived from K alone)",
        "pareto_load_forms_aexp_lamexp": {
            VARIABLES[index]: pareto_pairs(groups, index) for index in (4, 5, 6)
        },
        "pareto_target_forms_aexp_lamexp": {
            VARIABLES[index]: pareto_pairs(groups, index) for index in (2, 3)
        },
        "exact_q_stdout_sha256": digest(Q_STDOUT),
        "prime_stdout_sha256": digest(P_STDOUT),
        "scope": "RAW_NORMALIZED_K_SUPPORT_GROUPING_AND_FIXED_DELAYED_Q_CONE_ONLY_NO_PREDECESSOR_REDUCTION_COEFFICIENT_FACTOR_SATURATION_SOURCE_REES_ORDER2_MAX12_OR_JC2_VERDICT",
    }
    (output / "relative_cone_result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    (output / "coefficient_groups.json").write_text(json.dumps(group_rows, sort_keys=True, indent=2) + "\n")
    print("A_KCONE_RAW_TERM_COUNT=" + str(len(q_terms)))
    print("A_KCONE_GROUP_COUNT=" + str(len(groups)))
    print("A_KCONE_Q6_MINIMUM=" + str(minimum))
    print("A_KCONE_Q6_NEXT_MARGIN=" + str(gap))
    print("A_KCONE_RAW_THRESHOLD=" + str(max_threshold))
    print("A_KCONE_RAW_THRESHOLD_TERM_COUNT=" + str(sum(len(members[key]) for key in max_keys)))
    for key in max_keys:
        print("A_KCONE_THRESHOLD_KEY=" + ",".join(str(value) for value in key))
        print("A_KCONE_THRESHOLD_COEFF=" + coeff_text(groups[key]))
        for term in members[key]:
            print("A_KCONE_THRESHOLD_TERM=" + term)
    for index in (4, 5, 6, 2, 3):
        print("A_KCONE_PARETO_" + VARIABLES[index] + "=" + str(pareto_pairs(groups, index)))
    print("A_KCONE_ENDPOINT=PASS_RAW_K_RELATIVE_CONE_V2")
    print("A_KCONE_DONE=1")
    print("A_KCONE_SCOPE=" + result["scope"])


if __name__ == "__main__":
    main()
