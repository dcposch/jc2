#!/usr/bin/env python3
"""Coefficientwise Q/F_65521 comparison of the frozen V44R1 G20 rows."""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform
import sys


sys.setrecursionlimit(50000)
ROOT = Path(__file__).resolve().parents[2]
R1 = ROOT / "cases/max12_812_order2_gate_t_actual_total_g20_custody_v44r1_20260827"
Q = R1 / "compiler_pass_validator_failed_v1_aws_q_r6a/compiled"
P = R1 / "compiler_pass_validator_failed_v1_aws_p65521_r6b/compiled"
PARSER = ROOT / "cases/max12_812_order2_p0_total_rees_j2_typed_census_v23_20260827/census_j2_typed_v23.py"
PARSER_SHA = "14f2de22d8cabaea12ac7fc7bf72cca275edbbb6a35dc7c0556a6e18e67c4501"
Q_RESULT_SHA = "229695dc89f7746f9f664d368c82fa618a43f6b0a0e58c45e13fa9881ea390c2"
P_RESULT_SHA = "eedc3abce19573f16ee65b65d06c2755a246878040626a8b8a9b6bb23b26def9"
PRIME = 65521


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_parser():
    if digest(PARSER) != PARSER_SHA:
        raise RuntimeError("parser pin")
    spec = importlib.util.spec_from_file_location("v44r2_cross_parser", PARSER)
    if spec is None or spec.loader is None:
        raise RuntimeError("parser import")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def modular(value: Fraction) -> int:
    return (value.numerator * pow(value.denominator, -1, PRIME)) % PRIME


def main() -> None:
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if (platform.system() != "Linux" or not vendor.is_file()
            or vendor.read_text().strip() != "Amazon EC2"
            or not tag.startswith("max12_812_order2_gate_t_actual_total_g20_custody_v44r2_")):
        raise RuntimeError("registered V44R2 AWS cross-validator required")
    qresult_path, presult_path = Q / "result.json", P / "result.json"
    if digest(qresult_path) != Q_RESULT_SHA or digest(presult_path) != P_RESULT_SHA:
        raise RuntimeError("compiler result pin")
    qresult, presult = json.loads(qresult_path.read_text()), json.loads(presult_path.read_text())
    stable = (
        "compiler_sha256", "base_compiler_sha256", "exact_input_sha256",
        "tail_counts", "tail_total", "v35_prefix_polynomial_equalities",
        "frozen_face_bridges_after_construction", "terminal_source_variables",
        "terminal_receiver_rows", "terminal_grade20_receiver_free",
        "grade20_term_counts", "grade20_supports",
        "grade20_rational_canonical_sha256",
        "row_truncation_through20_canonical_sha256", "target_schedule",
    )
    for field in stable:
        if qresult.get(field) != presult.get(field):
            raise RuntimeError(("cross-lane field", field))
    parser = load_parser()
    shadow_hashes = {}
    for row in range(1, 8):
        name = f"Tg20_{row}"
        qpath, ppath = Q / f"{name}_q.poly", P / f"{name}_p{PRIME}.poly"
        if digest(qpath) != qresult["row_sha256"][name] or digest(ppath) != presult["row_sha256"][name]:
            raise RuntimeError(("row custody", name))
        qpoly, ppoly = parser.parse(qpath), parser.parse(ppath)
        for monomial in set(qpoly) | set(ppoly):
            if modular(qpoly.get(monomial, Fraction(0))) != modular(ppoly.get(monomial, Fraction(0))):
                raise RuntimeError(("modular shadow", name, monomial))
        shadow_hashes[name] = sha256(
            json.dumps(
                [[[list(pair) for pair in monomial], modular(qpoly[monomial])]
                 for monomial in sorted(qpoly) if modular(qpoly[monomial])],
                separators=(",", ":"),
            ).encode()
        ).hexdigest()
    final = {
        "status": "PASS-ACT-TOT-G20-CUSTODY-V44R2-CROSSLANE",
        "host": platform.node(),
        "registered_aws_lane": tag,
        "prime": PRIME,
        "q_result_sha256": Q_RESULT_SHA,
        "p_result_sha256": P_RESULT_SHA,
        "row_modular_shadow_sha256": shadow_hashes,
    }
    output = Path(os.environ["JC2_V44R2_CROSS_OUTPUT"])
    output.write_text(json.dumps(final, sort_keys=True, indent=2) + "\n")
    print(final["status"])


if __name__ == "__main__":
    main()

