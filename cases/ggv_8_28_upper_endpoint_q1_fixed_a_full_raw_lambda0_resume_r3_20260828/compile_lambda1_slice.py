#!/usr/bin/env python3
"""Compile only the literal lambda=1 q1..q13 gate packet."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
COMPILER = HERE / "compile_q_gates.py"
COMPILER_SHA256 = "b487d8b532d303421386c66638a6d7953aa5a4dcf74208cd07c6db885c511201"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_compiler():
    assert sha256(COMPILER) == COMPILER_SHA256
    spec = importlib.util.spec_from_file_location("ggv_split_lambda1_compiler", COMPILER)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def source_pin_check(qg):
    actual = {str(path.relative_to(qg.ROOT)): sha256(path) for path in qg.PINS}
    expected = {str(path.relative_to(qg.ROOT)): digest for path, digest in qg.PINS.items()}
    assert actual == expected, (actual, expected)
    return actual


def desk_check(qg):
    pins = source_pin_check(qg)
    raw = qg.rawc.desk_check()
    qgate = qg.desk_check()
    return {
        "schema": "GGV-8_28-QGATE-LAMBDA1-SPLIT-DESK-v1",
        "status": "LAMBDA1_SPLIT_DESK_PASS",
        "raw_low_prefix": raw,
        "qgate_low_prefix_and_anchor_checks": qgate,
        "pins": pins,
    }


def compile_lambda1(qg, output_dir: Path):
    source_pin_check(qg)
    source = json.loads(qg.RAW_INPUT.read_text())
    windows = qg.ce.raw_windows(source)
    qg.ce.verify_windows(windows)
    F, variables, blocks = qg.full_slice_F(1, windows)
    system = qg.compile_gate_system(
        "lambda_1_full_qgates",
        F,
        variables,
        blocks,
        {
            "lambda": 1,
            "kind": "necessary full-tail de Rham screen for the literal fixed slice",
            "raw_D0_D22_endpoint_equations_in_this_file": False,
            "must_intersect_with_raw_endpoint_system_for_survival": True,
            "lambda_nonzero_normalization_claimed": False,
        },
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    payloads = {
        "Q_GATE_SYSTEM.json": qg.ce.pretty(system),
        "qgates_p65521_lp_std.sing": qg.singular_script(system, 65521, "lp", "std").encode(),
        "qgates_p65519_dp_slimgb.sing": qg.singular_script(system, 65519, "dp", "slimgb").encode(),
        "qgates_p65497_dp_slimgb.sing": qg.singular_script(system, 65497, "dp", "slimgb").encode(),
        "qgates_q_lp_std.sing": qg.singular_script(system, 0, "lp", "std").encode(),
        "qgates_q_lp_tracked.sing": qg.singular_script(
            system, 0, "lp", "std", tracked=True
        ).encode(),
    }
    manifest = {}
    for name, payload in payloads.items():
        (output_dir / name).write_bytes(payload)
        manifest[name] = hashlib.sha256(payload).hexdigest()
    (output_dir / "GENERATED.sha256.json").write_bytes(qg.ce.pretty(manifest))
    return system, manifest


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--desk-check", action="store_true")
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    if args.desk_check == (args.output_dir is not None):
        parser.error("choose exactly one of --desk-check or --output-dir")
    qg = load_compiler()
    if args.desk_check:
        print(json.dumps(desk_check(qg), indent=2, sort_keys=True))
        return
    system, manifest = compile_lambda1(qg, args.output_dir)
    print(json.dumps({
        "status": "LAMBDA1_ONLY_COMPILE_PASS",
        "system_id": system["system_id"],
        "variables": system["variable_count"],
        "equations": system["equation_count"],
        "system_sha256": manifest["Q_GATE_SYSTEM.json"],
        "artifact_count": len(manifest),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
