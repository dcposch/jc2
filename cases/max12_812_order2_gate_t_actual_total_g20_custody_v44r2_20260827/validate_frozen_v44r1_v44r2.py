#!/usr/bin/env python3
"""Validate one immutable V44R1 compiler output with a sufficient parser recursion limit."""

from __future__ import annotations

import argparse
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
Q_BASE = R1 / "compiler_pass_validator_failed_v1_aws_q_r6a"
P_BASE = R1 / "compiler_pass_validator_failed_v1_aws_p65521_r6b"
PARSER = ROOT / "cases/max12_812_order2_p0_total_rees_j2_typed_census_v23_20260827/census_j2_typed_v23.py"
PARSER_SHA = "14f2de22d8cabaea12ac7fc7bf72cca275edbbb6a35dc7c0556a6e18e67c4501"
COMPILER_SHA = "f25b6204457c707a549a2bee06c467452d35abebc337f715b8012302ddad1a23"
BASE_COMPILER_SHA = "dd8681a66f150069db3e4553caa0fd66e70f360994b9a1328a34a4a50cac5003"
LANES = {
    "q": {
        "characteristic": 0,
        "base": Q_BASE,
        "label": "q",
        "result_sha": "229695dc89f7746f9f664d368c82fa618a43f6b0a0e58c45e13fa9881ea390c2",
        "stdout_sha": "bb913bf9cc1ff45ef3c2eb98389322eff333aca4b9f0c724976200c084ede1c2",
        "stderr_sha": "97c1be916ea6492639ac69e9c1652b135ff9b474aa7e53e7acf750b600ae8ec7",
        "transcript_stem": "max12_812_order2_gate_t_actual_total_g20_custody_v44r1_20260827T091855Z_q_compiler",
    },
    "p65521": {
        "characteristic": 65521,
        "base": P_BASE,
        "label": "p65521",
        "result_sha": "eedc3abce19573f16ee65b65d06c2755a246878040626a8b8a9b6bb23b26def9",
        "stdout_sha": "0cfb28ff3bf846b71c91ce9647d3fa0d4ff5528025bbf182e7181495edb8fcd7",
        "stderr_sha": "b1cc881b162f30c4f59e31241c6d56649e9d4dc1b97bb744d840746b29b56f27",
        "transcript_stem": "max12_812_order2_gate_t_actual_total_g20_custody_v44r1_20260827T091855Z_p65521_compiler",
    },
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def canonical_polynomial(polynomial) -> str:
    record = [
        [[list(pair) for pair in monomial], [coefficient.numerator, coefficient.denominator]]
        for monomial, coefficient in sorted(polynomial.items())
    ]
    return sha256(json.dumps(record, separators=(",", ":")).encode()).hexdigest()


def load_parser():
    if digest(PARSER) != PARSER_SHA:
        raise RuntimeError("parser pin")
    spec = importlib.util.spec_from_file_location("v44r2_parser", PARSER)
    if spec is None or spec.loader is None:
        raise RuntimeError("parser import")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("--lane", choices=tuple(LANES), required=True)
    cli.add_argument("--output", type=Path, required=True)
    args = cli.parse_args()
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if (platform.system() != "Linux" or not vendor.is_file()
            or vendor.read_text().strip() != "Amazon EC2"
            or not tag.startswith("max12_812_order2_gate_t_actual_total_g20_custody_v44r2_")):
        raise RuntimeError("registered V44R2 AWS validator required")
    lane = LANES[args.lane]
    base = lane["base"]
    compiled = base / "compiled"
    result_path = compiled / "result.json"
    stdout_path = base / "run" / f"{lane['transcript_stem']}.stdout"
    stderr_path = base / "run" / f"{lane['transcript_stem']}.stderr"
    if digest(result_path) != lane["result_sha"] or digest(stdout_path) != lane["stdout_sha"] or digest(stderr_path) != lane["stderr_sha"]:
        raise RuntimeError("frozen V44R1 compiler evidence pin")
    stdout = stdout_path.read_text()
    stderr = stderr_path.read_text()
    if stdout.count("PASS-ACT-TOT-G20-CUSTODY-V44R1-COMPILER") != 1:
        raise RuntimeError("compiler PASS transcript")
    if stderr.count("Command being timed:") != 1 or stderr.count("Exit status: 0") != 1:
        raise RuntimeError("compiler resource transcript")
    if any(token in stdout or token in stderr for token in ("Traceback", "FAIL_", "Killed", "out of memory", "error occurred")):
        raise RuntimeError("compiler diagnostic token")

    result = json.loads(result_path.read_text())
    required = {f"Tg20_{row}" for row in range(1, 8)}
    terminal = {"ell20", "cs18", "rs18", "az15", "ac15", "ez15", "ec15", "k10_16", "k6_8", "k2"}
    if (
        result.get("status") != "PASS-ACT-TOT-G20-CUSTODY-V44R1-COMPILER"
        or result.get("characteristic") != lane["characteristic"]
        or result.get("compiler_sha256") != COMPILER_SHA
        or result.get("base_compiler_sha256") != BASE_COMPILER_SHA
        or result.get("terminal_grade20_receiver_free") is not True
        or result.get("general_rho_rows_constructed_before_face") is not True
        or result.get("v35_prefix_polynomial_equalities") != 140
        or result.get("frozen_face_bridges_after_construction") != 14
        or result.get("tail_total") != 569
        or result.get("target_terms_through_grade20") != 0
        or set(result.get("terminal_source_variables", [])) != terminal
        or set(result.get("terminal_receiver_rows", {})) != terminal
        or any(result.get("terminal_receiver_rows", {}).values())
        or set(result.get("row_sha256", {})) != required
        or set(result.get("grade20_term_counts", {})) != required
        or set(result.get("grade20_rational_canonical_sha256", {})) != required
        or len(result.get("row_truncation_through20_canonical_sha256", {})) != 7
    ):
        raise RuntimeError("V44R1 compiler result contract")

    parser = load_parser()
    checked_hashes = {}
    for row in range(1, 8):
        name = f"Tg20_{row}"
        path = compiled / f"{name}_{lane['label']}.poly"
        if digest(path) != result["row_sha256"][name]:
            raise RuntimeError(("row hash", name))
        polynomial = parser.parse(path)
        if len(polynomial) != result["grade20_term_counts"][name]:
            raise RuntimeError(("term count", name))
        for monomial in polynomial:
            weight = sum(parser.sigma_weight(variable) * exponent for variable, exponent in monomial)
            if weight != 20:
                raise RuntimeError(("homogeneity", name, monomial, weight))
            if any(variable == "rho" and exponent % 2 for variable, exponent in monomial):
                raise RuntimeError(("rho parity", name, monomial))
        if args.lane == "q" and canonical_polynomial(polynomial) != result["grade20_rational_canonical_sha256"][name]:
            raise RuntimeError(("rational canonical hash", name))
        checked_hashes[name] = digest(path)

    final = {
        "status": f"PASS-ACT-TOT-G20-CUSTODY-V44R2-{args.lane.upper()}",
        "host": platform.node(),
        "registered_aws_lane": tag,
        "source_characteristic": lane["characteristic"],
        "v44r1_compiler_result_sha256": digest(result_path),
        "v44r1_compiler_sha256": COMPILER_SHA,
        "base_v44_compiler_sha256": BASE_COMPILER_SHA,
        "row_sha256": checked_hashes,
        "grade20_term_counts": result["grade20_term_counts"],
        "grade20_rational_canonical_sha256": result["grade20_rational_canonical_sha256"],
        "row_truncation_through20_canonical_sha256": result["row_truncation_through20_canonical_sha256"],
        "terminal_grade20_receiver_free": True,
    }
    args.output.write_text(json.dumps(final, sort_keys=True, indent=2) + "\n")
    print(final["status"])


if __name__ == "__main__":
    main()

