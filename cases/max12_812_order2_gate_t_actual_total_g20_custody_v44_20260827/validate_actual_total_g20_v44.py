#!/usr/bin/env python3
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


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def canonical_polynomial(polynomial) -> bytes:
    record = [
        [[list(pair) for pair in monomial], [coefficient.numerator, coefficient.denominator]]
        for monomial, coefficient in sorted(polynomial.items())
    ]
    return json.dumps(record, separators=(",", ":")).encode()


def load_parser():
    if digest(PARSER) != PARSER_SHA:
        raise RuntimeError("parser pin")
    spec = importlib.util.spec_from_file_location("v44_validator_parser", PARSER)
    if spec is None or spec.loader is None:
        raise RuntimeError("parser import")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("--result", type=Path, required=True)
    cli.add_argument("--compiler-stderr", type=Path, required=True)
    cli.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    cli.add_argument("--output", type=Path, required=True)
    args = cli.parse_args()
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if (platform.system() != "Linux" or not vendor.is_file()
            or vendor.read_text().strip() != "Amazon EC2"
            or not os.environ.get("JC2_REGISTERED_AWS_LANE", "")):
        raise RuntimeError("registered AWS validator required")
    parser = load_parser()
    result = json.loads(args.result.read_text())
    required_keys = {f"Tg20_{row}" for row in range(1, 8)}
    if (
        result.get("status") != "PASS-ACT-TOT-G20-CUSTODY-V44-COMPILER"
        or result.get("characteristic") != args.characteristic
        or result.get("tail_total") != 569
        or result.get("v35_prefix_polynomial_equalities") != 140
        or result.get("frozen_face_bridges_after_construction") != 14
        or result.get("general_rho_rows_constructed_before_face") is not True
        or result.get("target_terms_through_grade20") != 0
        or set(result.get("row_paths", {})) != required_keys
        or set(result.get("row_sha256", {})) != required_keys
        or set(result.get("grade20_term_counts", {})) != required_keys
        or set(result.get("grade20_rational_canonical_sha256", {})) != required_keys
        or len(result.get("row_truncation_through20_canonical_sha256", {})) != 7
    ):
        raise RuntimeError("compiler result contract")
    if set(result.get("terminal_source_variables", [])) != {
        "ell20", "cs18", "rs18", "az15", "ac15", "ez15", "ec15",
        "k10_16", "k6_8", "k2",
    }:
        raise RuntimeError("terminal source variables")
    if any(not rows for rows in result.get("terminal_receiver_rows", {}).values()):
        raise RuntimeError("terminal receiver census")

    for name, raw_path in result["row_paths"].items():
        path = Path(raw_path)
        if digest(path) != result["row_sha256"][name]:
            raise RuntimeError(("row hash", name))
        polynomial = parser.parse(path)
        if len(polynomial) != result["grade20_term_counts"][name]:
            raise RuntimeError(("term count", name))
        for monomial in polynomial:
            if sum(parser.sigma_weight(variable) * exponent for variable, exponent in monomial) != 20:
                raise RuntimeError(("homogeneity", name, monomial))
            if any(variable == "rho" and exponent % 2 for variable, exponent in monomial):
                raise RuntimeError(("rho parity", name, monomial))
        if args.characteristic == 0:
            observed = sha256(canonical_polynomial(polynomial)).hexdigest()
            if observed != result["grade20_rational_canonical_sha256"][name]:
                raise RuntimeError(("rational canonical hash", name))

    stderr = args.compiler_stderr.read_text()
    if stderr.count("Command being timed:") != 1 or stderr.count("Exit status: 0") != 1:
        raise RuntimeError("resource transcript")
    if any(token in stderr for token in ("Traceback", "Killed", "out of memory", "error occurred")):
        raise RuntimeError("diagnostic token")
    final = {
        "status": "PASS-ACT-TOT-G20-CUSTODY-V44",
        "characteristic": args.characteristic,
        "host": platform.node(),
        "compiler_result_sha256": digest(args.result),
        "row_sha256": result["row_sha256"],
        "grade20_rational_canonical_sha256": result["grade20_rational_canonical_sha256"],
        "row_truncation_through20_canonical_sha256": result["row_truncation_through20_canonical_sha256"],
        "grade20_term_counts": result["grade20_term_counts"],
    }
    args.output.write_text(json.dumps(final, sort_keys=True, indent=2) + "\n")
    print("PASS-ACT-TOT-G20-CUSTODY-V44-VALIDATOR")


if __name__ == "__main__":
    main()

