#!/usr/bin/env python3
"""AWS-only coefficientwise Q/F_65521 shadow check for ACT-TOT-G20."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform


ROOT = Path(__file__).resolve().parents[2]
PARSER = ROOT / "cases/max12_812_order2_p0_total_rees_j2_typed_census_v23_20260827/census_j2_typed_v23.py"
PARSER_SHA = "14f2de22d8cabaea12ac7fc7bf72cca275edbbb6a35dc7c0556a6e18e67c4501"
PRIME = 65521


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_parser():
    if digest(PARSER) != PARSER_SHA:
        raise RuntimeError("parser pin")
    spec = importlib.util.spec_from_file_location("v44_cross_parser", PARSER)
    if spec is None or spec.loader is None:
        raise RuntimeError("parser import")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def modular(value: Fraction) -> int:
    return (value.numerator * pow(value.denominator, -1, PRIME)) % PRIME


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("--q-dir", type=Path, required=True)
    cli.add_argument("--p-dir", type=Path, required=True)
    cli.add_argument("--output", type=Path, required=True)
    args = cli.parse_args()
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if (platform.system() != "Linux" or not vendor.is_file()
            or vendor.read_text().strip() != "Amazon EC2"
            or not os.environ.get("JC2_REGISTERED_AWS_LANE", "")):
        raise RuntimeError("registered AWS cross-validator required")
    parser = load_parser()
    qresult_path = args.q_dir / "result.json"
    presult_path = args.p_dir / "result.json"
    qresult = json.loads(qresult_path.read_text())
    presult = json.loads(presult_path.read_text())
    if qresult.get("characteristic") != 0 or presult.get("characteristic") != PRIME:
        raise RuntimeError("lane characteristics")
    stable_fields = (
        "compiler_sha256", "exact_input_sha256", "tail_counts", "tail_total",
        "v35_prefix_polynomial_equalities", "frozen_face_bridges_after_construction",
        "terminal_source_variables", "terminal_receiver_rows", "grade20_term_counts",
        "grade20_supports", "grade20_rational_canonical_sha256",
        "row_truncation_through20_canonical_sha256", "target_schedule",
    )
    for field in stable_fields:
        if qresult.get(field) != presult.get(field):
            raise RuntimeError(("cross-lane field", field))

    shadow_hashes = {}
    for row in range(1, 8):
        name = f"Tg20_{row}"
        qpath = args.q_dir / f"{name}_q.poly"
        ppath = args.p_dir / f"{name}_p{PRIME}.poly"
        if digest(qpath) != qresult["row_sha256"][name] or digest(ppath) != presult["row_sha256"][name]:
            raise RuntimeError(("row custody", name))
        qpoly = parser.parse(qpath)
        ppoly = parser.parse(ppath)
        monomials = set(qpoly) | set(ppoly)
        for monomial in monomials:
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
        "status": "PASS-ACT-TOT-G20-CUSTODY-V44-CROSSLANE-SHADOW",
        "host": platform.node(),
        "prime": PRIME,
        "q_result_sha256": digest(qresult_path),
        "p_result_sha256": digest(presult_path),
        "row_modular_shadow_sha256": shadow_hashes,
    }
    args.output.write_text(json.dumps(final, sort_keys=True, indent=2) + "\n")
    print("PASS-ACT-TOT-G20-CUSTODY-V44-CROSSLANE-SHADOW")


if __name__ == "__main__":
    main()

